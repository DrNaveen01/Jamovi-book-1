# Hands-On Data Analysis Using Jamovi - Volume I

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

```r
source("scripts/render_book.R")
```

## Reproduce and check

The figure images are already included. Base R companions are available:

```r
source("scripts/create_teaching_figures.R")
source("scripts/verify_illustrations.R")
```

The optional Python tools require NumPy, SciPy, and Matplotlib for figures,
and NumPy and SciPy for validation:

```sh
python scripts/create_teaching_figures.py
python scripts/validate_project.py
```

The R scripts were supplied but not executed in the preparation environment.
The numerical checks were executed independently in Python. Validation covers
the current manuscript, rather than future author-supplied jamovi output.

| Location | Purpose |
|:---------|:--------|
| Root `.qmd` files | Editable manuscript |
| `data/`, `images/` | Author-supplied data and screenshots; existing teaching figures |
| `guide/` | Scope maps, review checklist, source register, and validation records |
| `scripts/` | Rendering, reproduction, and verification |
| `docs/` | Rendered review book |

The existing `practice-dataset-excercises.qmd` filename is retained for path
compatibility; its reader-facing title is correct. The included Pages workflow
is available for a later repository publication and has not been run for this
review project.

Copyright © 2026 Dr Naveen Suthar. All rights reserved. See `copyright.md`.
