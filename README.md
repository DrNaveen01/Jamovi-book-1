# Hands-On Data Analysis Using Jamovi - Volume I

**Author-review edition, revision 4 - 21 October 2026 - Dr Naveen Suthar**

Volume I contains 16 teaching chapters, four content appendices, references,
five teaching figures, and questions with answers. It covers foundations,
data preparation, description, basic inference, correlation, introductory
regression, and reporting. Volumes II and III remain outlines in `guide/`.

**Release status:** conceptual manuscript available for review. All 17 reserved
Hands-on note boxes remain empty for the author’s datasets, saved analyses,
procedures, and screenshots. The present edition is not a completed practical
book. Numerical health examples are invented teaching illustrations.

[Early-release checklist](guide/early-release-checklist.md) records the remaining
work and the minimum practical workflow for each chapter. [AUTHORING.md](AUTHORING.md)
explains how to add that material without changing the established layout.

## Formatting standard

`BOOK-STYLE.md` specifies the implemented typography, colours, teaching panels,
tables, equations, captions, and chapter hierarchy. Revision 4 applies the same
style roles to HTML and PDF, with a bundled Times-style font for the portable
build. The Windows profile uses installed Times New Roman. The portable profile
is now the default when no profile is specified.

## Open the project

Open `Hands-On Data Analysis Using Jamovi.Rproj` in RStudio. Edit the root `.qmd`
files. There is **one main project configuration**, `_quarto.yml`.
`_quarto-portable.yml` and `_quarto-windows.yml` only override PDF fonts;
do not rename or replace the main configuration with them.

## Render HTML and PDF

Install [Quarto](https://quarto.org/docs/get-started/) and a XeLaTeX distribution.
The book uses supplied prose and images; rendering does not execute R or Python
analysis chunks. Run from the project root:

```sh
quarto render --to all --profile portable
quarto preview --to html
```

For Times New Roman, Arial, and Consolas on Windows:

```sh
quarto render --to all --profile windows
```

The profiles use the same manuscript and PDF header. The portable profile uses
the bundled TeX Gyre Termes font; the Windows profile uses installed Times New Roman. `quarto install tinytex`
installs a supported TeX distribution if one is needed. The complete render
writes `docs/index.html` and `docs/jamovi-book-volume-1-review.pdf`, and adds the
PDF download to the HTML sidebar. The output filename is retained for link
compatibility. Local KaTeX assets support offline equations. Use `quarto preview`
when browser restrictions affect search through a directly opened local file.

From RStudio, render both formats with:

```r
source("scripts/render_book.R")
```

After sourcing, `render_book(format = "html")` or `render_book(format = "pdf")`
renders one format. A one-format preview does not verify the other format.

## Validate

Use Python 3.12 and the pinned validation dependencies:

```sh
python -m pip install -r scripts/requirements-validation.txt
python scripts/validate_project.py
quarto render --to all --profile portable
python scripts/check_render.py
```

The source check verifies chapter registration, identifiers, references,
figures, Hands-on structure, PDF configuration, and the invented numerical
illustrations. It reports empty practical sections without rejecting an
intentionally unfinished review edition. After practical work is added:

```sh
python scripts/validate_project.py --require-practical
```

This additional check rejects empty Hands-on sections. Passing it establishes
content presence; the author must still verify data, settings, saved analyses,
output, and interpretation. The rendered-output check verifies local links and
anchors, CSS assets, shared citation numbering, a readable PDF, and its download
links. Reports are written to `guide/`; the output report is also included in
`docs/build-validation.json`.

Optional base R companions remain available:

```r
source("scripts/create_teaching_figures.R")
source("scripts/verify_illustrations.R")
```

R companion execution and an actual jamovi demonstration are separate checks;
neither is implied by the Python validation results.

## GitHub publication

Pull requests build and validate both formats and save a downloadable review
artifact in GitHub Actions. They do not deploy. Pushes to `main`, or manual
workflow runs on `main`, publish the checked `docs/` output to the existing
GitHub Pages site. A source, render, link, citation, or PDF failure blocks upload
and deployment. Quarto is pinned to 1.8.27 in the workflow.

The 5 October build failed because the PDF format omitted the header needed by
the review-layout filter. Revision 3 restores the complete PDF format and header,
restores the PDF download, and adds source and output checks before publication.
Generated render caches are excluded from version control. The established
Hands-on boxes and chapter paths are retained.

| Location | Purpose |
|:---------|:--------|
| Root `.qmd` files | Editable manuscript |
| `data/`, `images/` | Author-supplied data and screenshots; existing teaching figures |
| `guide/` | Scope, author review, release checklist, and validation records |
| `scripts/` | Rendering, reproduction, and verification |
| `docs/` | Generated HTML and PDF; rebuilt by the workflow |

The existing `practice-dataset-excercises.qmd` filename is retained for path
compatibility; its reader-facing title is correct. `intro.qmd`, `index-word.qmd`,
and `summary.qmd` are unregistered legacy templates, not book chapters.

Copyright © 2026 Dr Naveen Suthar. All rights reserved. See `copyright.md`.
