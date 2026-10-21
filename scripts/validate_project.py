"""Verify source completeness and invented numerical examples.

Run from any directory with Python, NumPy, and SciPy. This checks the current
manuscript; it does not verify future author-supplied jamovi output.
"""
from pathlib import Path
import argparse
import json
import re
import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--require-practical", action="store_true",
                    help="Fail if any reserved Hands-on section remains empty. This is only a presence check, not verification of jamovi output.")
args = parser.parse_args()
CHAPTERS = ["role", "getting-started", "data-management", "data-cleaning",
            "data-transformation", "analysis-preparation", "descriptive-statistics",
            "graphical-presentation", "hypothesis-testing-concepts", "comparing-two-means",
            "comparing-more-than-two-means", "categorical-variables", "correlation",
            "linear-regression", "logistic-regression", "reporting-results"]
config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
registered = re.findall(r"(?m)^\s*-\s*(?:part:\s*)?([^\s]+\.qmd)\s*$", config)
assert len(registered) == 27, f"Unexpected registered page count: {len(registered)}"
assert len(registered) == len(set(registered)), "A manuscript page is registered twice"
assert all((ROOT / name).is_file() for name in registered), "A registered source file is missing"
# Legacy templates are retained for compatibility, but do not belong to the book.
legacy_templates = {"intro.qmd", "index-word.qmd", "summary.qmd"}
unregistered = {p.name for p in ROOT.glob("*.qmd")} - set(registered)
assert unregistered <= legacy_templates, f"Unregistered manuscript pages: {sorted(unregistered - legacy_templates)}"
assert '  downloads: [pdf]' in config, "The PDF download is disabled"
assert re.search(r"(?m)^  pdf:\s*$", config), "The main PDF format is missing"
assert 'include-in-header: includes/pdf-header.tex' in config, "PDF header is missing"
assert r"\usepackage{needspace}" in (ROOT / "includes/pdf-header.tex").read_text(), \
    "The PDF review-layout filter requires the needspace package"
bib = (ROOT / "references.bib").read_text(encoding="utf-8")
keys = re.findall(r"@\w+\s*\{\s*([^,]+),", bib)
assert len(keys) == len(set(keys)), "Duplicate bibliography keys"
sources = {name: (ROOT / name).read_text(encoding="utf-8") for name in registered}
text = "\n".join(sources.values())
ids = re.findall(r"\{#([A-Za-z0-9_-]+)", text)
assert len(ids) == len(set(ids)), "Duplicate section or figure identifiers"
refs = set(re.findall(r"(?<!\w)@([A-Za-z][A-Za-z0-9_-]*)", text))
crossrefs = {r for r in refs if r.startswith(("sec-", "fig-", "tbl-", "eq-"))}
assert crossrefs <= set(ids), f"Unknown cross references: {crossrefs-set(ids)}"
citations = refs - crossrefs
assert citations <= set(keys), f"Unknown citations: {citations-set(keys)}"
image_paths = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
for relative in image_paths:
    assert (ROOT / relative).is_file(), f"Missing figure: {relative}"
assert len(image_paths) == 5
assert "Author Name" not in text
assert not re.search(r"(?im)\b(?:TODO|TBD|lorem ipsum)\b", text)

word_counts = {}
for stem in CHAPTERS:
    chapter = sources[stem + ".qmd"]
    for heading in ("## Learning objectives", "## Hands-on", "## Review questions",
                    "## Answers and reasoning"):
        assert heading in chapter, f"Missing {heading} in {stem}"
    for wrapper in ("::: {.review-questions}", "::: {.review-answers}"):
        assert wrapper in chapter, f"Missing print-layout wrapper {wrapper} in {stem}"
    prose = re.sub(r"<!--.*?-->", "", chapter, flags=re.S)
    word_counts[stem] = len(re.findall(r"\b[\w’'-]+\b", prose))
    assert word_counts[stem] > 1000, f"Chapter may be incomplete: {stem}"
    headings = re.split(r"(?m)^## .*$", prose)[1:]
    # All teaching sections must contain text or a reserved callout.
    assert all(section.strip() for section in headings), f"Empty teaching section in {stem}"

boxes = re.findall(r'::: \{\.callout-note \.hands-on-note[^\n]*\}\n(.*?)\n:::', text, re.S)
assert len(boxes) == len(CHAPTERS) + 1, f"Expected 17 reserved callouts, found {len(boxes)}"
empty_boxes = sum(not re.sub(r"<!--.*?-->", "", body, flags=re.S).strip() for body in boxes)
if args.require_practical:
    assert empty_boxes == 0, f"Practical sections remain empty: {empty_boxes}; add and verify the author's jamovi material before a complete hands-on release"

values = {}
def check(name, calculated, expected=None, atol=1e-6):
    a = np.asarray(calculated, dtype=float)
    if expected is not None:
        assert np.allclose(a, expected, atol=atol, rtol=0), f"Numerical mismatch: {name}: {a}"
    values[name] = a.tolist()
    return a

waiting = np.array([2, 3, 3, 4, 4, 5, 6, 7, 8, 18.])
check("waiting_mean", waiting.mean(), 6)
check("waiting_median", np.median(waiting), 4.5)
check("waiting_sample_sd", waiting.std(ddof=1), 4.6188021535)
check("waiting_type7_quartiles", np.quantile(waiting, [.25, .75]), [3.25, 6.75])
check("mean_t95ci", 136+np.array([-1, 1])*stats.t.ppf(.975, 99)*1.8,
      [132.428409491, 139.571590509])
v1, v2 = 14**2/60, 16**2/60
se = np.sqrt(v1+v2)
df = (v1+v2)**2/(v1**2/59+v2**2/59)
check("welch_df", df, 115.9567492689)
check("welch_t", -6/se, -2.1860377540)
check("welch_p", 2*stats.t.sf(abs(-6/se), df), .03082226804)
check("welch_95ci", -6+np.array([-1, 1])*stats.t.ppf(.975, df)*se,
      [-11.436229405, -.563770595])
paired_se = 10/np.sqrt(30)
check("paired_t", -8/paired_se, -4.3817804600)
check("paired_p", 2*stats.t.sf(abs(-8/paired_se), 29), .0001407005)
check("paired_95ci", -8+np.array([-1, 1])*stats.t.ppf(.975, 29)*paired_se,
      [-11.734061369, -4.265938631])
ssb = np.sum(20*(np.array([125, 130, 135])-130)**2)
ssw = 3*19*100
f = (ssb/2)/(ssw/57)
check("anova_F", f, 5)
check("anova_p", stats.f.sf(f, 2, 57), .00998392959)
check("anova_eta_squared", ssb/(ssb+ssw), .1492537313)
tab = np.array([[30, 70], [15, 85]])
chi, p, _, expected = stats.chi2_contingency(tab, correction=False)
check("chi_square", chi, 6.4516129032)
check("chi_square_p", p, .01108516638)
check("chi_expected_counts", expected, [[22.5, 77.5], [22.5, 77.5]])
check("fisher_two_sided_p", stats.fisher_exact(tab).pvalue, .01714902277)
z = stats.norm.ppf(.975)
rd_se = np.sqrt(.3*.7/100+.15*.85/100)
check("risk_difference_wald_95ci", .15+np.array([-1, 1])*z*rd_se)
rr_se = np.sqrt(1/30-1/100+1/15-1/100)
check("risk_ratio_logwald_95ci", np.exp(np.log(2)+np.array([-1, 1])*z*rr_se),
      [1.14887781, 3.48165832])
odds_ratio = 30*85/(70*15)
logor_se = np.sqrt(np.sum(1/tab))
check("cross_product_OR", odds_ratio, 2.4285714286)
check("OR_logwald_95ci", np.exp(np.log(odds_ratio)+np.array([-1, 1])*z*logor_se),
      [1.21099921, 4.87032456])
check("paired_binary_exact_p", stats.binomtest(15, 20, .5).pvalue)
for r in [.6, .3]:
    t = r*np.sqrt(48/(1-r*r))
    check(f"pearson_{r}_p", 2*stats.t.sf(abs(t), 48))
    check(f"pearson_{r}_fisher95ci", np.tanh(np.arctanh(r)+np.array([-1, 1])*z/np.sqrt(47)))
check("linear_slope_95ci", .5+np.array([-1, 1])*stats.t.ppf(.975, 58)*.1,
      [.2998282516, .7001717484])
check("linear_slope_p", 2*stats.t.sf(5, 58), .0000056184207)
check("linear_R_squared", 25/83, .3012048193)
intercept = np.log(.15/.85)
coefficient = np.log(odds_ratio)
check("logistic_intercept", intercept, -1.7346010554)
check("logistic_coefficient", coefficient, .8873031950)
check("logistic_wald_p", 2*stats.norm.sf(abs(coefficient/logor_se)), .01244762952)
check("logistic_probabilities", 1/(1+np.exp(-(intercept+coefficient*np.array([0, 1])))), [.15, .30])
a, b = np.array([2, 4, 6, 8]), np.array([1, 3, 5, 7])
rank_sum = stats.rankdata(np.concatenate([a, b]))[:4].sum()
check("rank_sum_A", rank_sum, 20)
check("mann_whitney_U_A", rank_sum-4*5/2, 10)
d = np.array([-4, -2, -1, 3, 6])
ranks = stats.rankdata(abs(d))
check("signed_rank_positive_negative", [ranks[d > 0].sum(), ranks[d < 0].sum()], [8, 7])
means = np.random.default_rng(20261005).normal(0, 1/np.sqrt(25), 30)
half = z/np.sqrt(25)
check("simulated_intervals_covering_mean", ((means-half <= 0)&(means+half >= 0)).sum(), 29)

# Independent checks of the preparation chapters' invented arithmetic and rules.
check("cleaning_distinct_and_eligible", [204-4, 204-4-8], [200, 192])
check("cleaning_followup_available", [192-12, 96-4, 96-8], [180, 92, 88])
check("cleaning_missing_percentages", 100*np.array([12/192, 4/96, 8/96]),
      [6.25, 4.1666666667, 8.3333333333])
check("cleaning_observed_percentage", 100*180/192, 93.75)
check("height_metres", 160/100, 1.6)
check("BMI_correct_units", 80/(160/100)**2, 31.25)
check("BMI_wrong_height_units", 80/160**2, .003125)
check("absolute_change", 138-146, -8)
check("individual_percentage_change", 100*(138-146)/146, -5.4794520548)
check("reverse_item_scores", 6-np.arange(1, 6), [5, 4, 3, 2, 1])
items = np.array([4, 5, 3])
check("complete_item_sum_and_mean", [items.sum(), items.mean()], [12, 4])
check("equal_log_ratio_differences", np.diff(np.log([10, 20, 40])),
      [.6931471806, .6931471806])
check("arithmetic_and_geometric_means", [np.mean([10, 40]), np.exp(np.mean(np.log([10, 40])))],
      [25, 20])
check("specified_reference_z", (140-130)/10, 1)
boundaries = np.array([0, 9.999, 10, 19.999, 20])
check("waiting_category_boundary_codes", np.searchsorted([10, 20], boundaries, side="right"),
      [0, 0, 1, 1, 2])
check("invalid_waiting_input_flags", ~np.isfinite([-1, np.nan]) | (np.array([-1, np.nan]) < 0),
      [1, 1])
check("complete_pair_count", 120-(6+8-2), 108)
check("pair_availability_breakdown", [120-(6+8-2), 6-2, 8-2, 2], [108, 4, 6, 2])
check("available_baseline_and_followup", [120-6, 120-8], [114, 112])
check("known_status_event_percentage", 100*36/180, 20)
check("eligible_event_accounting_bounds", 100*np.array([36, 36+(192-180)])/192, [18.75, 25])
check("reversed_welch_95ci", -np.array(values["welch_95ci"])[::-1],
      [.563770595, 11.436229405])

report = {
    "status": "passed", "registered_pages": len(registered), "main_chapters": len(CHAPTERS),
    "content_appendices": 4, "hands_on_callouts": len(boxes),
    "empty_hands_on_callouts": empty_boxes,
    "unregistered_legacy_templates": sorted(unregistered),
    "teaching_figures": len(image_paths), "bibliography_records": len(keys),
    "cited_sources": len(citations), "approximate_chapter_word_counts": word_counts,
    "numerical_calculations": len(values), "illustration_values": values,
    "limitations": ["R companion scripts were supplied; this Python check does not execute R.",
                    "Author-supplied jamovi datasets and screenshots remain to be added."]
}
(ROOT / "guide" / "validation-results.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k not in
                  ("illustration_values", "approximate_chapter_word_counts", "limitations")}, indent=2))
