<<<<<<< HEAD
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
=======
# Volume I project status and scope

**Review revision 2:** 5 October 2026.  
**Source repository:** [DrNaveen01/Jamovi-book-1](https://github.com/DrNaveen01/Jamovi-book-1).  
**Baseline main commit:** `8868df0a5a2bec900bfb72fb9c4efe0ff8859383`.

Volume I's teaching manuscript is supplied for author review. Revision 2 expands
the foundation sequence into four dedicated data preparation chapters, giving
16 main chapters. Every chapter retains a separate Hands-on heading and an empty
styled note. The practical material remains reserved for the author.

The teaching scope and editable delivery are aligned. Practical completeness
remains pending: the finished book's hands-on promise requires the author's
verified datasets, saved analyses, screenshots, and demonstrations. The current
project is a review manuscript with an explicit place for that contribution.
Preparing it did not change or deploy the GitHub repository.

## What is provided, intended, and delivered

| Component | Provided in this project | Intended completed-book contribution | Assessment |
|:----------|:-------------------------|:-------------------------------------|:-----------|
| Research and software foundations | Design, target quantity, observation unit, measurement scales, and jamovi orientation | Establish the question and structure before selecting a method | Consistent |
| Data entry and validation | Dedicated Chapter 3: dictionary, row keys, variable properties, entry checks, and import audit | Preserve the recorded measurements and detect discrepancies | Core scope now developed separately |
| Cleaning and missing values | Dedicated Chapter 4: supported corrections, duplicates, coding, sample flow, missingness assumptions, and log | Resolve queries and describe unavailable information transparently | Core scope now developed separately |
| Transformations | Dedicated Chapter 5: units, ratios, change scores, recodes, reversal, composite scores, logs, and standardisation | Derive quantities with explicit definitions and verification | Core scope now developed separately |
| Analysis preparation | Dedicated Chapter 6: specification, eligibility, filters, completeness, matching, denominators, and saved record | Explain precisely which observations enter each result | Core scope now developed separately |
| Description and graphics | Distribution, centre and spread, appropriate tables, figures, and reporting | Describe the data before inference | Consistent |
| Basic inference | Uncertainty, hypotheses, mean comparisons, rank alternatives, categorical methods, and paired binary orientation | Match the procedure to the design and target | Consistent |
| Regression | Correlation, simple linear regression, and a single-predictor logistic introduction | Interpret unadjusted relationships and prepare for later modeling | Consistent with the introductory boundary |
| Interpretation and reporting | Effect scales, CIs, reference groups, sample sizes, denominators, and reporting examples | Produce reviewable methods and results statements | Consistent |
| Hands-on practice | Separate headings and 17 empty styled note callouts | Verified jamovi data, settings, output, interpretation, and learner tasks | Structure supplied; practical content pending by author instruction |
| Learning support | Formulas, selection guide, expanded glossary, ten integrated cases, questions and answers | Consolidate concepts and support independent review | Supplied for review |
| Evidence | 64 bibliography records, 63 cited sources, and a source register | Trace software and methodological claims | Records and citation keys checked |
| Delivery | Quarto sources, RStudio project, HTML/PDF previews, authoring guide, review checklist, and scripts | Maintain an editable book with consistent formats | Supplied; validation record accompanies the previews |
| Volumes II and III | Planning outlines in `guide/` | Adjusted and specialist methods, followed by advanced validity and reproducibility | Planned; full manuscripts remain future work |

## What changed in revision 2

The earlier 13-chapter review compressed entry, cleaning, transformation, and
analysis preparation into `data-management.qmd`. Those four stages now have
separate substantive chapters, matching the previously agreed foundation scope.
The established file remains Chapter 3, titled Data Entry and Validation;
`data-cleaning.qmd`, `data-transformation.qmd`, and `analysis-preparation.qmd`
are new Chapters 4-6. Existing analysis chapter paths are retained and their
reader-facing numbers move accordingly.

The two-group chapter now includes a complete reasoning record for its invented
Welch example, identifies which checks need individual observations, and shows
the reversed contrast as a consistency check. The method-selection appendix,
glossary, preface, foundation introduction, and Volume I scope guide connect to
the expanded preparation sequence. The README is shorter, and the author has a
separate editorial review checklist.

## Inventory and boundaries

The registered manuscript contains 27 source pages: a preface, five part
introductions, 16 main chapters, four content appendices, and references. There
are five existing teaching figures. All 16 chapter Hands-on bodies and the
practice-appendix Hands-on body are empty, containing only author comments.

Small numerical examples, scoring illustrations, and mathematical figures are
explicitly invented. The sample-flow, complete-pair, and event-denominator cases
are separate illustrations and must not be combined as one dataset. No
patient-level practice data, `.omv` files, or jamovi screenshots are included.

The common sequence is question, design, data, method, assumptions, output,
clinical meaning, and reporting. Data preparation is core chapter content.
Introductory regression remains unadjusted; full adjusted modeling, specialist
methods, and formal prediction validation retain their later-volume boundaries.

## Verification record

The source check verifies all registered pages, unique identifiers, cross-references,
citation keys, figure paths, substantive chapter sections, and the 17 deliberately
empty callouts. It independently checks 61 numerical calculations, including
22 new checks of preparation arithmetic, recode boundaries, overlapping missing
measurements, event denominators, and contrast reversal. Results are in
`guide/validation-results.json`.

Rendering uses Quarto 1.8.27, Pandoc 3.6.4, and XeLaTeX. The book does not execute
R or Python analysis chunks. Included local KaTeX assets support offline HTML
mathematics. The post-render script aligns chapter citations with the shared
HTML reference list and the single PDF reference order.

The rendered review covers local links, images, mathematics, citations, empty
callout bodies, desktop and narrow layouts, and PDF pages. The final page count
and render findings are recorded in `guide/render-validation.json`.

Base R companion scripts are provided for figures and independent calculations.
R was unavailable in the preparation environment, so those scripts were not
executed. Numerical verification was performed with Python, NumPy, and SciPy.
This confirms the stated arithmetic, rather than an executed jamovi workflow or
future author-supplied screenshots. Formula descriptions use official jamovi
documentation; function behaviour should also be verified in the author's version.

The supplied Pages workflow has not been run on GitHub for this project.
Publication remains a later repository action.

## Author review and remaining work

Review the chapter depth, clinical relevance, terminology, illustrations,
questions, boundaries, and references. Record requested changes in
`guide/author-review-checklist.md`. Add datasets, dictionaries, saved analyses,
version details, procedures, screenshots, and tasks using `AUTHORING.md`.

Begin the practical sequence with a documented preparation case across Chapters
3-6 and a verified two-group example in Chapter 10. Reconcile counts, units,
contrast direction, missingness, and settings with the printed interpretation.
Where the practical dataset differs, label it as a separate case.

The conceptual teaching manuscript is available for review. Author-supplied
practical material and final subject-matter and editorial review remain before
publication.
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e
