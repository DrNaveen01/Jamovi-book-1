# Verification record: 20 October 2026

This record describes revision 3 prepared from repository main commit
`411391a1e81828f29055b7aaced890dd49b2f83e`.

## Completed checks

- The source validator passed for 27 registered pages, 16 teaching chapters,
  five teaching figures, 64 bibliography records, 63 cited sources, and 61
  independent numerical calculations.
- A clean HTML and PDF render completed with Quarto 1.10.19 and XeLaTeX from
  TeX Live 2023. The temporary build environment needed the official
  `fontawesome5` TeX package; it was installed for rendering.
- The rendered-output validator passed: 27 HTML pages, 1,909 local links,
  121 CSS assets, 27 PDF download links, 116 citation groups, 63 shared
  references, and a readable 121-page PDF.
- PDF contact sheets covering all 121 pages and a full-size preview of the
  revised preface were inspected. The page-edge check returned no flags.
- A Chromium 131 browser check passed for all 27 pages at a 390-pixel width:
  no horizontal page overflow, JavaScript errors, or failed HTTP responses; all
  132 equations rendered. Desktop and mobile screenshots were inspected.
- Validator regression checks confirmed that filling a reserved box is allowed
  during authoring and that an unexpected unregistered chapter is rejected.
- The practical-completeness presence check correctly failed with 17 empty
  Hands-on sections. This is the expected status of the review edition.

Machine-readable results are in `validation-results.json` and
`render-validation.json`. The final HTML/PDF outputs are included in the complete
project archive. R companion execution, practical jamovi verification, and
final author review remain pending.

## GitHub write limitation

Repository inspection succeeded, but creating a Git tree and a branch through
the connection both returned HTTP 403: `Resource not accessible by integration`.
The updated source could not be pushed and no pull request or deployment was
created. The complete project archive contains the changes for review and later
upload. The workflow configuration has been updated locally; its pinned Quarto
1.8.27 GitHub Actions run has not been executed for this revision.
