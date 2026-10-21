# Hands-On Data Analysis Using Jamovi - Volume I

<<<<<<< HEAD
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
=======
**Author-review project, revision 2 - 5 October 2026 - Dr Naveen Suthar**

The editable manuscript contains 16 teaching chapters, four content appendices,
references, five figures, and review questions with answers. Chapters 3-6 now
separately cover data entry and validation, cleaning and missing values,
transformations, and preparation for a specific analysis.

Every chapter has a separate **Hands-on** heading and an **empty note callout**.
The practice appendix adds one further box: 17 in total. The author will add
jamovi datasets, saved analyses, procedures, and screenshots. Numerical health
examples are invented; no patient-level dataset or `.omv` analysis is included.
Volumes II and III remain planning outlines in `guide/`.

This review project is based on [DrNaveen01/Jamovi-book-1](https://github.com/DrNaveen01/Jamovi-book-1),
main commit `8868df0a5a2bec900bfb72fb9c4efe0ff8859383`. Preparing it did not
change or deploy the GitHub repository. Existing chapter paths are retained,
with three new preparation chapter files.

## Open and review

Extract the ZIP, then open `docs/index.html` or
`docs/jamovi-book-volume-1-review.pdf`. Open `Jamovi-book-1.Rproj` in RStudio to
edit the chapter `.qmd` files. `PROJECT_REVIEW.md` maps the scope and checks;
`AUTHORING.md` explains how to add practical material. Use
`guide/author-review-checklist.md` to record editorial decisions.

## Render

Install [Quarto](https://quarto.org/docs/get-started/) and a XeLaTeX distribution
for PDF. Rendering uses existing prose and images, without executing R or Python
analysis chunks. Both preview formats are written to `docs/`:

```sh
quarto render
quarto preview
```

On Windows, use `quarto render --profile windows` for Times New Roman, Arial,
and Consolas. The default and `portable` profiles use Latin Modern fonts.
`quarto install tinytex` can install Quarto's supported TeX distribution.
Render both formats to retain the complete preview and its PDF download.
The included local KaTeX assets support offline equations. Local browser
restrictions can affect search through `file://`; use `quarto preview` for search.

From RStudio:
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e

```r
source("scripts/render_book.R")
```

<<<<<<< HEAD
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
=======
## Reproduce and check

The figure images are already included. Base R companions are available:
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e

```r
source("scripts/create_teaching_figures.R")
source("scripts/verify_illustrations.R")
```

<<<<<<< HEAD
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
=======
The optional Python tools require NumPy, SciPy, and Matplotlib for figures,
and NumPy and SciPy for validation:

```sh
python scripts/create_teaching_figures.py
python scripts/validate_project.py
```

The R scripts were supplied but not executed in the preparation environment.
The numerical checks were executed independently in Python. Validation covers
the current manuscript, rather than future author-supplied jamovi output.
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e

| Location | Purpose |
|:---------|:--------|
| Root `.qmd` files | Editable manuscript |
| `data/`, `images/` | Author-supplied data and screenshots; existing teaching figures |
<<<<<<< HEAD
| `guide/` | Scope, author review, release checklist, and validation records |
| `scripts/` | Rendering, reproduction, and verification |
| `docs/` | Generated HTML and PDF; rebuilt by the workflow |

The existing `practice-dataset-excercises.qmd` filename is retained for path
compatibility; its reader-facing title is correct. `intro.qmd`, `index-word.qmd`,
and `summary.qmd` are unregistered legacy templates, not book chapters.
=======
| `guide/` | Scope maps, review checklist, source register, and validation records |
| `scripts/` | Rendering, reproduction, and verification |
| `docs/` | Rendered review book |

The existing `practice-dataset-excercises.qmd` filename is retained for path
compatibility; its reader-facing title is correct. The included Pages workflow
is available for a later repository publication and has not been run for this
review project.
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e

Copyright © 2026 Dr Naveen Suthar. All rights reserved. See `copyright.md`.
