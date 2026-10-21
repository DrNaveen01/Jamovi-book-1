"""Check HTML/PDF output after `quarto render --to all --profile portable`.

Checks files, links, shared citations and PDF readability. This does not
replace visual review or verification of the author's jamovi demonstrations.
"""
from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs"
config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
pages = re.findall(r"(?m)^\s*-\s*(?:part:\s*)?([^\s]+\.qmd)\s*$", config)
book_name = re.search(r'(?m)^  output-file: "([^"]+)"', config).group(1)
revision_date = re.search(r'(?m)^  date: "([^"]+)"', config).group(1)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.duplicate_ids = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                self.duplicate_ids.append(attrs["id"])
            self.ids.add(attrs["id"])
        field = "href" if tag in ("a", "link") else "src" if tag in ("img", "script") else None
        if field and attrs.get(field):
            self.links.append(attrs[field])


html_sources = {}
parsed = {}
for source in pages:
    relative = Path(source).with_suffix(".html")
    path = OUTPUT / relative
    assert path.is_file(), f"Missing rendered chapter: {relative}"
    text = path.read_text(encoding="utf-8")
    assert not re.search(r"(?:<strong>\?\?|@(?:sec|fig|tbl|eq)-[A-Za-z])", text), \
        f"Unresolved cross-reference: {relative}"
    page = Page(text)
    assert not page.duplicate_ids, f"Duplicate HTML identifiers in {relative}: {page.duplicate_ids}"
    html_sources[path] = text
    parsed[path] = page

link_count = 0
pdf_links = 0
for path, page in parsed.items():
    for raw in page.links:
        url = urlsplit(unescape(raw))
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target == OUTPUT or OUTPUT in target.parents, f"Link leaves book output: {path.name}: {raw}"
        if target.is_dir():
            target = target / "index.html"
        assert target.is_file(), f"Broken local link in {path.name}: {raw}"
        if url.fragment and target.suffix == ".html":
            parsed_target = parsed.get(target) or Page(target.read_text(encoding="utf-8"))
            assert unquote(url.fragment) in parsed_target.ids, f"Broken anchor in {path.name}: {raw}"
        link_count += 1
        if target.name == book_name + ".pdf":
            pdf_links += 1
assert pdf_links >= len(pages), "The PDF download must be linked from each book page"

# Include CSS dependencies, such as local KaTeX fonts for offline mathematics.
css_asset_count = 0
for path in OUTPUT.rglob("*.css"):
    for raw in re.findall(r"url\(\s*['\"]?([^\s)'\"]+)", path.read_text(encoding="utf-8")):
        url = urlsplit(raw)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        assert target.is_file(), f"Missing CSS asset in {path.relative_to(OUTPUT)}: {raw}"
        css_asset_count += 1

reference_text = html_sources[OUTPUT / "references.html"]
numbers = {key: int(number) for key, number in re.findall(
    r'<div\b[^>]*\bid="ref-([^"]+)"[^>]*>\s*<div class="csl-left-margin">(\d+)\.', reference_text)}
assert numbers, "The shared numbered bibliography is missing"
assert sorted(numbers.values()) == list(range(1, len(numbers) + 1)), "Bibliography numbering is not continuous"
source_order = []
for source in pages:
    text = re.sub(r"<!--.*?-->", "", (ROOT / source).read_text(encoding="utf-8"), flags=re.S)
    for key in re.findall(r"@([A-Za-z][A-Za-z0-9_-]*)", text):
        if key in numbers and key not in source_order:
            source_order.append(key)
assert all(numbers[key] == index + 1 for index, key in enumerate(source_order)), \
    "Shared references do not follow first citation in the book"
citation_groups = 0
for path, text in html_sources.items():
    for keys, body in re.findall(
        r'<span\b[^>]*class="citation"[^>]*data-cites="([^"]+)"[^>]*>(.*?)</span>', text, re.S):
        expected = sorted(set(keys.split()), key=lambda key: numbers[key])
        actual = re.findall(r'href="references.html#ref-([^"]+)"[^>]*>(\d+)</a>', body)
        assert actual == [(key, str(numbers[key])) for key in expected], \
            f"Inconsistent citation numbering in {path.name}: {keys}"
        citation_groups += 1
assert citation_groups > 0, "No checked citation groups were found"

pdf = OUTPUT / (book_name + ".pdf")
assert pdf.is_file() and pdf.stat().st_size > 10000, "The rendered PDF is missing or empty"
reader = PdfReader(pdf, strict=True)
assert not reader.is_encrypted, "The book PDF should be readable without a password"
assert len(reader.pages) >= len(pages), "The PDF appears to contain only part of the book"
pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
pdf_text = re.sub(r"(?<=\w)-\n(?=\w)", "", pdf_text)
pdf_text = re.sub(r"\s+", " ", pdf_text)
assert "Hands-On Data Analysis Using Jamovi" in pdf_text, "Unexpected PDF title"
assert "Practical jamovi demonstrations remain pending" in pdf_text, "PDF revision notice is missing"
assert "Volume I | Review draft" in pdf_text, "The PDF header was not loaded"

checked_sources = sorted(set(pages + ["_quarto.yml", "_quarto-portable.yml", "_quarto-windows.yml",
                                      "BOOK-STYLE.md", "references.bib", "vancouver.csl", "styles.scss"])
                         | {str(p.relative_to(ROOT)) for directory in ("includes", "filters", "scripts", "fonts")
                            for p in (ROOT / directory).rglob("*")
                            if p.is_file() and "__pycache__" not in p.parts})
digest = hashlib.sha256()
for relative in checked_sources:
    digest.update(relative.encode() + b"\0" + (ROOT / relative).read_bytes())
report = {
    "status": "passed", "revision": 4, "date": revision_date,
    "source_sha256": digest.hexdigest(), "html_pages_checked": len(pages),
    "local_links_checked": link_count, "css_assets_checked": css_asset_count,
    "pdf_download_links": pdf_links, "citation_groups_checked": citation_groups,
    "shared_numbered_references": len(numbers), "pdf_pages": len(reader.pages),
    "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
    "limits": ["Automated checks do not replace visual or final author review.",
               "Reserved Hands-on sections remain pending; no executed jamovi workflow is claimed."]
}
serialized = json.dumps(report, indent=2) + "\n"
(ROOT / "guide/render-validation.json").write_text(serialized, encoding="utf-8")
(OUTPUT / "build-validation.json").write_text(serialized, encoding="utf-8")
print(serialized, end="")
