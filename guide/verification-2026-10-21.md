# Formatting verification: 21 October 2026

Revision 4 applies working formatting standard 1.0 from `BOOK-STYLE.md`.
The book was rendered with Quarto 1.8.27, XeLaTeX and the portable font profile.
The 129-page PDF and 27 HTML pages come from the same edited source.

The 16 teaching chapter source files are unchanged. The preface changes only
its revision and date. The source validator passed all 61 numerical checks;
all 17 reserved Hands-on bodies remain empty. Formatting does not establish
practical completeness or replace the author's final content review.

The rendered-output checks passed for local links, anchors, PDF downloads,
CSS assets, shared reference order, and 116 citation groups. All 132 equations
rendered in Chromium 131. The browser reported TeX Gyre Termes as the actual
body font. All 27 pages passed the 390-pixel layout check without horizontal
page overflow, JavaScript errors, or failed HTTP responses.

The PDF page-edge check returned no flags. Contact sheets covering the full
PDF and representative full-size pages were reviewed for typography, title
wrapping, tables, equations, learning panels, and review sections. The separate
five-page formatting preview contains the cover and selected Chapter 10 pages.

The Windows font profile is supplied for installed Times New Roman, Arial, and
Consolas; it was not rendered on this Linux host. Font files in the portable
profile are bundled with their licence and original documentation.

Full machine-readable results are in `formatting-validation.json`,
`validation-results.json`, and `render-validation.json`. The previous day's
verification record remains historical. No GitHub write or deployment is part
of this formatting revision; the updated complete project is supplied for review.
