# Early-release checklist

**Working revision: 4, 21 October 2026.** Scope: Volume I only, 16 teaching
chapters and the existing appendices. Keep the current sequence and the
introductory boundary of regression. Volumes II and III remain future work.

## Release position

A review edition can be assessed from the conceptual text, exercises, and
rendered previews. A complete hands-on release still requires the author’s
verified practical material. All 16 chapter boxes and the practice-appendix
box remain empty. Revision 3 labels that limitation in both reader formats.

The availability constraint for 20–21 October is handled by separating build
and documentation work from the author-dependent demonstrations. No publication
date, completed jamovi workflow, or final author approval is assumed.

## Automated build work

- [x] Restore one complete shared HTML/PDF configuration.
- [x] Preserve the Windows and portable font overrides.
- [x] Restore the PDF download and require its target to exist.
- [x] Check chapter registration, citation keys, identifiers, figures, and numerical illustrations.
- [x] Permit the author to fill the reserved boxes without breaking the review validator.
- [x] Build pull-request previews and keep deployment limited to `main`.
- [x] Check rendered local links, anchors, CSS dependencies, citations, and PDF readability.

The validation JSON files contain the measured results for the checked build.
A successful build verifies delivery; it does not complete the teaching review.

## Minimum practical workflow by chapter

Use one documented preparation case for Chapters 2–8 and separate analysis cases
where a different design is needed. Reuse appropriate datasets rather than
creating one unrelated file per chapter. These are contribution requirements,
not claims about material already supplied.

| Chapter | Practical contribution still required |
|:--------|:--------------------------------------|
| 1. Role of statistics | One question mapped to design, observation unit, variables, and target quantity |
| 2. Getting started | Import a documented dataset, set properties, and save an `.omv` file |
| 3. Data entry and validation | Dictionary, row key, coding, type settings, and import checks |
| 4. Cleaning and missing values | Resolved query, missingness summary, and auditable correction log |
| 5. Transformations | Verified derived variables, recode boundaries, and missing-input behaviour |
| 6. Analysis preparation | Eligibility/filter record, denominator, and complete-pair count |
| 7. Descriptive statistics | Frequency and continuous summaries with denominators and units |
| 8. Graphical presentation | Readable categorical and continuous plots with interpretation |
| 9. Estimation and hypothesis testing | Estimate, CI, test result, and a contextual interpretation |
| 10. Two-group comparisons | Independent and paired workflows; relevant assumptions and reported contrasts |
| 11. More than two groups | Omnibus comparison, stated multiple-comparison approach, and interpretation |
| 12. Categorical associations | Independent contingency table and paired-binary orientation; counts and effect scale |
| 13. Correlation | Scatterplot, selected coefficient, interval, sample size, and interpretation |
| 14. Simple linear regression | One-predictor model, diagnostic checks, units, and reported slope |
| 15. Introductory logistic regression | Outcome coding, reference group, unadjusted OR, CI, and probability interpretation |
| 16. Reporting | A coherent methods/results passage and matching table or figure |
| Practice appendix | At least one integrated downloadable case with tasks and checked answers |

For each demonstration, supply the dataset and dictionary, jamovi and module
versions, analysis options, saved analysis, legible output, interpretation, and
one learner task. Retain the separate Hands-on heading and note callout.
A screenshot alone is insufficient to reproduce an analysis. Printed examples
need not match a separate practice case, but that distinction must be explicit.

## Author review order

1. Review one preparation workflow across Chapters 3–6 and one analysis workflow
   in Chapter 10 to establish a consistent contribution standard.
2. Complete the remaining demonstrations using that standard; verify denominators,
   units, direction of contrasts, reference categories, and missing-value handling.
3. Review the conceptual text, numerical illustrations, answers, sources, and
   volume boundaries with the existing `author-review-checklist.md`.
4. Run the source check with `--require-practical`, render both formats, and run
   `check_render.py`. Inspect the final PDF and desktop/mobile HTML layouts.
5. Record the final review decisions and version before a completed-book release.

## Final release record

- [ ] Practical workflows and integrated case verified in jamovi.
- [ ] All reserved boxes filled and `--require-practical` passed.
- [ ] Final subject-matter and editorial review recorded.
- [ ] HTML and PDF generated from the same reviewed revision.
- [ ] PDF pages and desktop/mobile book inspected after the final content change.
- [ ] Public download checked after deployment; release version recorded.

Until these steps are complete, retain the author-review label and the practical
status notice. This list does not require expanding the agreed Volume I scope.
