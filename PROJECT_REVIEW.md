# Volume I status and early-release preparation

**Revision 4: 21 October 2026.** Reviewed source: main commit
`411391a1e81828f29055b7aaced890dd49b2f83e` in
[DrNaveen01/Jamovi-book-1](https://github.com/DrNaveen01/Jamovi-book-1).

## Formatting revision

Revision 4 applies the working standard in `BOOK-STYLE.md`: 12-point Times-style
print text, a fixed heading hierarchy, a new title-page treatment, learning and
example panels, restrained teal accents, horizontal table rules, consistent
captions, and responsive web typography. The portable font is bundled with its
licence. Chapter text, numerical examples, citation keys, and the 17 reserved
Hands-on bodies retain their content. The previous revision-3 delivery repairs
are retained below as the release-preparation history.

## Current scope

The registered manuscript contains 27 source pages: a preface, five part
introductions, 16 teaching chapters, four content appendices, and references.
The foundation sequence separates data entry and validation, cleaning and
missingness, transformations, and preparation for a specific analysis.
Introductory linear and logistic regression remain unadjusted; adjusted and
specialist methods retain their later-volume boundaries.

Every teaching chapter and the practice appendix retains a separate Hands-on
subsection and styled note box. These 17 boxes are deliberately reserved for
the author. No patient-level practice dataset, saved `.omv` analysis, or jamovi
screenshot is currently supplied. Small numerical examples are invented.

## Confirmed release blockers and repairs

| Finding at the reviewed commit | Revision 3 change |
|:-------------------------------|:------------------|
| Latest publication build failed at `\Needspace` | Restore the full XeLaTeX format and `includes/pdf-header.tex`, which loads `needspace` |
| PDF format was commented out; the portable profile supplied only font settings | Keep the full shared PDF configuration in `_quarto.yml`; use profiles only for fonts |
| PDF downloads were disabled | Restore the sidebar PDF download and check the target after rendering |
| Source validator rejected three unregistered legacy templates | Allow the three named templates while rejecting unexpected unregistered manuscript pages |
| Validator required every Hands-on box to remain empty | Preserve the scaffold, count empty boxes, and provide an explicit practical-completeness presence check |
| Publishing did not run source or rendered-output validation | Check arithmetic and sources, render both formats, then check local links, citations, and PDF |
| Tracked render caches could preserve obsolete citation output | Remove the generated cache from version control and clear it in CI |
| Pull requests had no book preview build | Build pull requests and retain review artifacts without deploying |
| README described an extracted review ZIP and an incorrect RStudio filename | Document the actual repository, project filename, configuration, rendering, and publishing behaviour |

The failed run is [37302852996](https://github.com/DrNaveen01/Jamovi-book-1/actions/runs/37302852996).
The error was an undefined `\Needspace` command, rather than an error in a
statistical calculation.

## Verification and its limits

`python scripts/validate_project.py` verifies the registered manuscript,
identifiers, citations, figures, Hands-on structure, required PDF configuration,
and 61 independent numerical calculations. The normal review build permits
reserved practical boxes to remain empty. `--require-practical` rejects empty
boxes but cannot establish that a demonstration is correct.

`python scripts/check_render.py` verifies all registered HTML pages, local
links and anchors, CSS assets, shared reference order and citation numbering,
PDF readability and header, and the PDF download. Its current results are in
`guide/render-validation.json`; source results are in
`guide/validation-results.json`. GitHub Actions repeats these checks against
the same revision before publication.

The current work repairs delivery and clarifies readiness. It does not establish
that the manuscript has passed a new complete statistical peer review, that the
R companions have been executed, or that jamovi demonstrations have been tested.

## Remaining author contribution

The conceptual text, questions, illustrations, and editable source are available
for review. Complete and verify practical material using
[the early-release checklist](guide/early-release-checklist.md) and
[AUTHORING.md](AUTHORING.md). Keep the reserved Hands-on format. Label any early
circulation as an author-review edition while those sections remain pending.
Final publication as a complete hands-on book requires the practical workflows
and the author’s subject-matter and editorial review.

## Build references

- [Quarto book output and downloads](https://quarto.org/docs/books/book-output.html)
- [Quarto project profiles](https://quarto.org/docs/projects/profiles.html)
- [Quarto project scripts](https://quarto.org/docs/projects/scripts.html)

Statistical and software references for teaching content remain in
`references.bib` and `guide/source-register.csv`.
