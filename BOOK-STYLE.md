---
editor: 
  markdown: 
    wrap: 72
---

# Book formatting standard

**Working standard 1.0 - 21 October 2026.** Applies to *Hands-On Data
Analysis Using Jamovi, Volume I*. This is the implemented baseline for
author review. The source remains editable and the same teaching content
supplies both formats.

## Visual specification

| Element | PDF edition | HTML edition |
|:------------------|:-------------------------|:---------------------------|
| Page or reading area | A4, 25-mm margins, one-sided review layout | 760-pixel maximum main reading area; responsive on mobile |
| Body text | 12 pt, Times-style serif, 1.1 line stretch | 18 px, matching serif family, 1.62 line height |
| Main chapter title | 24 pt bold black, chapter label above, fine rule below | 2.15 rem bold black; 1.8 rem on mobile |
| Section heading | 15 pt bold black | 1.5 rem; 1.35 rem on mobile |
| Subsection heading | 12.5 pt bold black | 1.17 rem; 1.12 rem on mobile |
| Paragraphs | Justified, no first-line indent, visible space between paragraphs | Left aligned, no first-line indent, visible paragraph spacing |
| Tables | 10.5 pt; horizontal book-style rules; no vertical grid | Approximately 16.5 px; horizontal rules and a light header |
| Captions | Small serif, bold label, sentence case | Approximately 16 px; sentence case |
| Equations | Centred display mathematics with clear vertical spacing | Centred; long expressions scroll within the equation on narrow screens |
| Running information | Short book title, volume/review label, centred page number | Chapter navigation, search, in-page contents and PDF download |

## Typeface and palette

The Windows PDF profile uses installed **Times New Roman**, with Arial
and Consolas where a sans serif or monospaced face is needed. The
default portable profile uses bundled **TeX Gyre Termes**, a Times-style
font, and does not require Microsoft fonts. HTML uses Times New Roman
when installed and the bundled Termes font otherwise. The four bundled
Termes faces are unmodified; their licence and original documentation
are in `fonts/texgyre/`.

Use white pages, near-black body text (`#202320`), black headings, muted
teal (`#285F5A`) for navigation and restrained accents, pale grey
(`#F3F5F3`) for learning panels, and cream (`#FBF7EF`) for the opening
of a worked illustration. Avoid decorative gradients, icons, large
colour fills, or a separate colour scheme for each chapter. Text labels
and headings identify each teaching role; colour is supplementary.

## Teaching components

| Component | Consistent treatment |
|:------------------------|:-----------------------------------------------|
| Learning objectives | Existing heading, followed by a pale-grey panel containing the objectives |
| Worked illustration | Existing heading, with its opening paragraph in a cream panel; tables and calculations remain in the main reading flow |
| Reporting example | Existing heading, with the opening paragraph in a neutral panel |
| Hands-on | Separate heading and the existing pale-teal jamovi workspace note; retain the reserved blank body until practical material is added |
| Review questions | Separate section, a stronger top rule, numbered questions; compact 11-point text in print |
| Answers and reasoning | Separate section with a finer rule; compact 11-point text in print; keep each short review section together |

The formatting filter applies panels to the existing headings. It does
not add examples, change estimates, insert screenshots, or fill the 17
reserved boxes. Only the lead paragraph of an illustration is boxed, so
longer examples, figures, and tables can continue naturally across
pages.

## Chapter order and editorial rules

Retain the sequence: learning objectives; question and data structure;
method and assumptions; worked illustration; interpretation and
reporting; Hands-on; review questions; answers and reasoning. Use the
existing chapter-specific headings where they communicate that sequence
more precisely.

Use sentence case for prose headings and captions. Keep to chapter,
section, and subsection levels for teaching text. Use bold for defined
terms and short emphasis; avoid long bold paragraphs. Write menu paths
in the form `Analyses > T-Tests > Independent Samples T-Test`, with
actual labels verified in the software version used for the
demonstration.

State units in table headers, define abbreviations below tables, and
align numerical columns by their values. Put table captions above and
figure captions below. Use informative captions that identify the
comparison, units, and relevant sample. Add source or licence
information where required. Screenshots must retain the labels and
settings needed to interpret them and remain readable at the final
displayed size.

Use the same group order, reference category, numerical precision,
notation, and estimate throughout each example. Distinguish a generic
formula, defined symbols, substitution, result, and interpretation when
those components are present. Do not add algebra only to create a
decorative formula block.

Preserve the book's existing numbered Vancouver citations in square
brackets. Use bibliography keys and the reference harmonisation step; do
not type numbers manually. Formatting does not change the meaning of
statistical results.

## Apply or revise the standard

-   `styles.scss`: HTML typography, palette, panels, tables, and
    navigation.
-   `includes/pdf-header.tex`: PDF typography, title page, headings,
    panels, captions, running headers and page numbers.
-   `filters/book-style.lua`: assigns the teaching-panel roles from
    existing headings.
-   `_quarto.yml`: page size, text size, line stretch, reading width,
    and default profile.
-   `_quarto-portable.yml`: bundled Times-style font configuration.
-   `_quarto-windows.yml`: native Windows font configuration.

Render both editions from the project root:

``` sh
quarto render --to all
```

The portable profile is selected automatically. To use installed Windows
fonts:

``` sh
quarto render --to all --profile windows
```

Then run `python scripts/validate_project.py` and
`python scripts/check_render.py`. Inspect the PDF after font, margin,
table, equation, screenshot, or heading changes; also check desktop and
narrow HTML layouts. Keep this specification and the implemented values
together when revising the style.

## Implementation references

-   [Quarto: PDF
    basics](https://quarto.org/docs/output-formats/pdf-basics.html)
-   [Quarto: book
    output](https://quarto.org/docs/books/book-output.html)
-   [Quarto: project
    profiles](https://quarto.org/docs/projects/profiles.html)
-   [CTAN: TeX Gyre and its licence](https://ctan.org/pkg/tex-gyre)
