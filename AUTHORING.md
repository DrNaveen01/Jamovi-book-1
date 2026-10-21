# Adding the Hands-on material

Follow `BOOK-STYLE.md` for typography, teaching panels, tables, figures, equations,
and captions. The formatting theme applies to both editions without changing the
reserved Hands-on source structure.

Each teaching chapter ends with a separate Hands-on subsection followed by an
empty note callout. The box has a distinct pale background and border in HTML.
The source currently contains only an author comment. Keep the heading and
callout classes when inserting your material.

```markdown
## Hands-on {#hands-on-your-chapter}

::: {.callout-note .hands-on-note title="jamovi workspace" icon=false}
<!-- Add your dataset, procedure, screenshots, interpretation, and task here. -->
:::
```

Use the existing chapter-specific heading ID rather than `hands-on-your-chapter`.
The PDF and HTML share the same teaching source. After editing, render both
formats and check that the callout and screenshots fit their pages.

Run `python scripts/validate_project.py` while the book is in review. It permits
both completed and reserved boxes. Before a complete hands-on release, run it
with `--require-practical` to reject empty boxes, then verify every demonstration
in jamovi. Render both formats with `quarto render --to all --profile portable`
and run `python scripts/check_render.py` before checking the final layout.

## A practical section to complete

Start with the health question, the unit of observation, and the outcome and
predictor or group variables. Link the dataset and its dictionary. State the
jamovi version and the module version where relevant. Describe the analytical
choices, then show the screenshots needed to understand those choices and the
result. Explain the estimate, uncertainty, denominator, and reference group.
Finish with one task the reader can attempt and a reporting sentence.

These are authoring instructions, not text already inserted into the empty boxes.
No patient-level teaching dataset has been generated for this manuscript.

## Four preparation demonstrations

Chapters 3-6 now have separate teaching and practical responsibilities. Use one
documented source case across them where feasible, so the reader can follow how
the analytical file is developed.

| Chapter | Material to add in its reserved box |
|:--------|:-----------------------------------|
| Data entry and validation | Collection definitions, dictionary, import audit, type settings, and source queries |
| Cleaning and missing values | Supported corrections, duplicate decisions, mapping checks, missingness table, and log |
| Transformations | Derived-variable definitions, formulas, recode boundaries, missing-input checks, and verified values |
| Analysis preparation | Question and target, eligibility, required variables, filters, matching, and reconciled sample counts |

The printed sample-flow, complete-pair, and event-denominator examples are
separate invented illustrations. Do not combine their counts as one study.
The formula examples are supported by documentation and independent arithmetic;
the project does not contain an executed jamovi demonstration of them. Verify
function behaviour, missing values, and active filters in the version you use.

## Add files and links

Put data and saved analyses in `data/`. Put screenshots in `images/`, preferably
within a chapter folder. Use short filenames without spaces, for example
`data/two-means.omv` and `images/two-means/welch-output.png`. Use synthetic,
properly de-identified, or suitably licensed public data, with a data dictionary.
Record the source, permitted use, version date, units, missing codes, category
labels, reference levels, and expected observation count.

Within the callout, a dataset link and screenshot can be inserted as follows
after the corresponding files have actually been added:

```markdown
[Download the saved jamovi analysis](data/two-means.omv)

![Welch comparison with the group order and confidence interval visible.](images/two-means/welch-output.png){#fig-two-means-output width=95% fig-alt="jamovi output for the specified independent-group comparison"}
```

Give every figure a unique ID and an informative caption. Crop away unrelated
interface areas while retaining the labels, sample size, choices, and values
needed to interpret the output. Use readable screenshots without identifiers.
Do not insert broken links as temporary examples in the live chapters.

## Keep the teaching example and practical result coherent

The manuscript contains small invented examples with calculated summaries.
They are complete illustrations, rather than summaries of an included raw
dataset. Some cannot uniquely determine a patient-level dataset. The chapter's
example and your practical case may use different data, but label that clearly.

If you intend the practical output to reproduce a printed numerical example,
verify that the observation count, units, direction, analysis settings, missing
data handling, estimate, interval, and p-value actually agree. Otherwise describe
the Hands-on material as a separate practice case. Do not silently imply that
an unrelated dataset produced the printed values.

The waiting-time figure uses type-7 quartiles. Other software conventions can
give slightly different quartiles in a small sample. Pearson chi-square examples
are uncorrected; Fisher's conditional odds-ratio estimate is distinguished from
the simple cross-product estimate. Keep those method labels when comparing output.

## Review the chapter

Use the sequence **question → design → data → method → assumptions → output →
clinical meaning → reporting**. Check that the Hands-on example teaches the
chapter's stated objective and stays within Volume I. The logistic chapter is
a single-predictor introduction; adjusted modeling belongs to Volume II.

References are in `references.bib`. Use citation keys such as `[@jamoviDesc]`
instead of typing reference numbers. Update the source register when adding a
new source. Cross-references use the existing section and figure IDs.

Run the illustration verification after changing a numerical example. The current
scripts verify the stated calculations; new examples need their own independent
calculation before being treated as checked. Preview at a narrow browser width
and review the PDF after adding wide tables or screenshots.
