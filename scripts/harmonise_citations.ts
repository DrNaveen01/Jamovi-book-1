// Match each HTML chapter's citation numbers to the book's shared reference list.
// Run by Quarto's built-in TypeScript runtime; no extra package or network is used.
const output = Deno.env.get("QUARTO_PROJECT_OUTPUT_DIR") || "docs";
const refsPath = `${output}/references.html`;
try {
  Deno.statSync(refsPath);
} catch (error) {
  if (error instanceof Deno.errors.NotFound) {
    console.log("No HTML reference page in this render; citation harmonisation skipped.");
    Deno.exit(0);
  }
  throw error;
}

let references = Deno.readTextFileSync(refsPath);
const numbers = new Map<string, number>();
const pattern = /<div\b[^>]*\bid="(ref-[^"]+)"[^>]*>\s*<div class="csl-left-margin">(\d+)\.\s*<\/div>/g;
for (const match of references.matchAll(pattern)) {
  numbers.set(match[1], Number(match[2]));
}
if (numbers.size === 0) throw new Error("The numbered HTML reference list could not be read.");

// Use first appearance in the registered manuscript, matching the single PDF.
// An HTML-only render can otherwise order the shared list by the BibTeX file.
const config = Deno.readTextFileSync("_quarto.yml");
const pages = [...config.matchAll(/^\s*-\s*(?:part:\s*)?([^\s]+\.qmd)\s*$/gm)]
  .map((match) => match[1]);
const order: string[] = [];
for (const page of pages) {
  const source = Deno.readTextFileSync(page).replace(/<!--[\s\S]*?-->/g, "");
  for (const match of source.matchAll(/@([A-Za-z][A-Za-z0-9_-]*)/g)) {
    const id = `ref-${match[1]}`;
    if (numbers.has(id) && !order.includes(id)) order.push(id);
  }
}
for (const id of numbers.keys()) if (!order.includes(id)) order.push(id);
order.forEach((id, index) => numbers.set(id, index + 1));

const entryPattern = /<div\b[^>]*\bid="(ref-[^"]+)"[^>]*>\s*<div class="csl-left-margin">\d+\.\s*<\/div>\s*<div class="csl-right-inline">[\s\S]*?<\/div>\s*<\/div>/g;
const entries = [...references.matchAll(entryPattern)];
if (entries.length !== numbers.size) throw new Error("Could not read every HTML reference entry.");
const sorted = entries.sort((a, b) => numbers.get(a[1])! - numbers.get(b[1])!)
  .map((entry) => entry[0].replace(/(<div class="csl-left-margin">)\d+\./,
    `$1${numbers.get(entry[1])}.`));
const originalEntries = [...references.matchAll(entryPattern)];
const first = originalEntries[0].index!;
const last = originalEntries[originalEntries.length - 1];
references = references.slice(0, first) + sorted.join("\n") +
  references.slice(last.index! + last[0].length);
Deno.writeTextFileSync(refsPath, references);

let updated = 0;
let citationGroups = 0;
for (const entry of Deno.readDirSync(output)) {
  if (!entry.isFile || !entry.name.endsWith(".html")) continue;
  const path = `${output}/${entry.name}`;
  const original = Deno.readTextFileSync(path);
  const repaired = original.replace(
    /(<span\b[^>]*class="citation"[^>]*data-cites="([^"]+)"[^>]*>)([\s\S]*?)(<\/span>)/g,
    (_whole, opening: string, keys: string, _body: string, closing: string) => {
      const cited = [...new Set(keys.trim().split(/\s+/))].map((key) => {
        const number = numbers.get(`ref-${key}`);
        if (number === undefined) throw new Error(`Missing reference ${key} in ${entry.name}`);
        return { key, number };
      }).sort((a, b) => a.number - b.number);
      const links = cited.map(({ key, number }) =>
        `<a href="references.html#ref-${key}" role="doc-biblioref">${number}</a>`);
      citationGroups++;
      return `${opening}[${links.join(", ")}]${closing}`;
    },
  );
  if (repaired !== original) {
    Deno.writeTextFileSync(path, repaired);
    updated++;
  }
}
console.log(`Shared reference numbering checked: ${citationGroups} citation groups, ${updated} HTML pages updated.`);
