# Independently calculate the manuscript's invented statistical illustrations.
# Run from the project root. Base R only; no patient-level data are exported.
results <- list()
record <- function(name, value, expected = NULL, tolerance = 1e-6) {
  if (!is.null(expected)) {
    stopifnot(length(value) == length(expected),
              all(abs(as.numeric(value) - as.numeric(expected)) <= tolerance))
  }
  results[[name]] <<- as.numeric(value)
  invisible(value)
}

waiting <- c(2, 3, 3, 4, 4, 5, 6, 7, 8, 18)
record("waiting_mean", mean(waiting), 6)
record("waiting_median", median(waiting), 4.5)
record("waiting_sd", sd(waiting), 4.6188021535)
record("waiting_quartiles_type7", quantile(waiting, c(.25, .75), type = 7), c(3.25, 6.75))
record("waiting_iqr", IQR(waiting, type = 7), 3.5)

record("mean_95ci", 136 + c(-1, 1)*qt(.975, 99)*18/sqrt(100),
       c(132.428409491, 139.571590509))

# Independent-group Welch procedure from stated sufficient summaries.
n1 <- 60; n2 <- 60; m1 <- 128; m2 <- 134; s1 <- 14; s2 <- 16
v1 <- s1^2/n1; v2 <- s2^2/n2
se <- sqrt(v1 + v2)
df <- (v1 + v2)^2/(v1^2/(n1-1) + v2^2/(n2-1))
t_value <- (m1-m2)/se
record("welch_se", se, 2.7446918467)
record("welch_df", df, 115.9567492689)
record("welch_t", t_value, -2.1860377540)
record("welch_p", 2*pt(-abs(t_value), df), .03082226804)
record("welch_95ci", (m1-m2) + c(-1, 1)*qt(.975, df)*se,
       c(-11.436229405, -.563770595))

# Paired analysis of the difference summaries; complete-pair n = 30.
se <- 10/sqrt(30); t_value <- -8/se
record("paired_t", t_value, -4.3817804600)
record("paired_p", 2*pt(-abs(t_value), 29), .0001407005)
record("paired_95ci", -8 + c(-1, 1)*qt(.975, 29)*se,
       c(-11.734061369, -4.265938631))

sizes <- c(20, 20, 20); means <- c(125, 130, 135); sds <- c(10, 10, 10)
grand <- weighted.mean(means, sizes)
ss_between <- sum(sizes*(means-grand)^2)
ss_within <- sum((sizes-1)*sds^2)
F_value <- (ss_between/2)/(ss_within/57)
record("anova_F", F_value, 5)
record("anova_p", pf(F_value, 2, 57, lower.tail = FALSE), .00998392959)
record("anova_eta_squared", ss_between/(ss_between+ss_within), .1492537313)

tab <- matrix(c(30, 70, 15, 85), nrow = 2, byrow = TRUE,
              dimnames = list(Group = c("A", "B"), Event = c("Present", "Absent")))
chi <- chisq.test(tab, correct = FALSE)
record("chi_square_uncorrected", unname(chi$statistic), 6.4516129032)
record("chi_square_p", chi$p.value, .01108516638)
record("fisher_two_sided_p", fisher.test(tab)$p.value, .01714902277)
# Fisher's conditional estimate is distinct from the cross-product OR below.
record("fisher_conditional_OR", unname(fisher.test(tab)$estimate))
p1 <- 30/100; p0 <- 15/100
rd <- p1-p0; rd_se <- sqrt(p1*(1-p1)/100 + p0*(1-p0)/100)
record("risk_difference", rd, .15)
record("risk_difference_wald_95ci", rd + c(-1, 1)*qnorm(.975)*rd_se)
rr <- p1/p0; rr_se <- sqrt(1/30-1/100+1/15-1/100)
record("risk_ratio", rr, 2)
record("risk_ratio_logwald_95ci", exp(log(rr) + c(-1, 1)*qnorm(.975)*rr_se),
       c(1.14887781, 3.48165832))
or <- 30*85/(70*15); logor_se <- sqrt(sum(1/tab))
record("cross_product_OR", or, 2.4285714286)
record("OR_logwald_95ci", exp(log(or) + c(-1, 1)*qnorm(.975)*logor_se),
       c(1.21099921, 4.87032456))

# Conditional exact test on the 20 discordant paired observations.
record("paired_binary_exact_p", binom.test(15, 20, p = .5)$p.value)

for (r in c(.6, .3)) {
  t_value <- r*sqrt(48/(1-r^2))
  record(paste0("pearson_", r, "_p"), 2*pt(-abs(t_value), 48))
  record(paste0("pearson_", r, "_fisher_95ci"),
         tanh(atanh(r) + c(-1, 1)*qnorm(.975)/sqrt(47)))
}

record("linear_slope_95ci", .5 + c(-1, 1)*qt(.975, 58)*.1,
       c(.2998282516, .7001717484))
record("linear_slope_p", 2*pt(-5, 58), .0000056184207)
record("linear_R_squared", 25/(25+58), .3012048193)

intercept <- qlogis(.15); coefficient <- log(or)
record("logistic_intercept", intercept, -1.7346010554)
record("logistic_coefficient", coefficient, .8873031950)
record("logistic_wald_p", 2*pnorm(-abs(coefficient/logor_se)), .01244762952)
record("logistic_probabilities", plogis(intercept + coefficient*c(0, 1)), c(.15, .30))

a <- c(2, 4, 6, 8); b <- c(1, 3, 5, 7)
rank_sum <- sum(rank(c(a, b))[seq_along(a)])
record("rank_sum_A", rank_sum, 20)
record("mann_whitney_U_A", rank_sum-length(a)*(length(a)+1)/2, 10)
d <- c(-4, -2, -1, 3, 6); ranks <- rank(abs(d))
record("signed_rank_positive_negative", c(sum(ranks[d > 0]), sum(ranks[d < 0])), c(8, 7))

# Data preparation: independent arithmetic, not execution of jamovi formulas.
record("cleaning_distinct_and_eligible", c(204-4, 204-4-8), c(200, 192))
record("cleaning_followup_available", c(192-12, 96-4, 96-8), c(180, 92, 88))
record("cleaning_missing_percentages", 100*c(12/192, 4/96, 8/96),
       c(6.25, 4.1666666667, 8.3333333333))
record("cleaning_observed_percentage", 100*180/192, 93.75)
record("height_metres", 160/100, 1.6)
record("BMI_correct_units", 80/(160/100)^2, 31.25)
record("BMI_wrong_height_units", 80/160^2, .003125)
record("absolute_change", 138-146, -8)
record("individual_percentage_change", 100*(138-146)/146, -5.4794520548)
record("reverse_item_scores", 6-seq_len(5), c(5, 4, 3, 2, 1))
items <- c(4, 5, 3)
record("complete_item_sum_and_mean", c(sum(items), mean(items)), c(12, 4))
record("equal_log_ratio_differences", diff(log(c(10, 20, 40))),
       c(.6931471806, .6931471806))
record("arithmetic_and_geometric_means", c(mean(c(10, 40)), exp(mean(log(c(10, 40))))),
       c(25, 20))
record("specified_reference_z", (140-130)/10, 1)
record("waiting_category_boundary_codes", findInterval(c(0, 9.999, 10, 19.999, 20), c(10, 20)),
       c(0, 0, 1, 1, 2))
record("invalid_waiting_input_flags", !is.finite(c(-1, NA_real_)) | c(-1, NA_real_) < 0,
       c(1, 1))
record("complete_pair_count", 120-(6+8-2), 108)
record("pair_availability_breakdown", c(120-(6+8-2), 6-2, 8-2, 2), c(108, 4, 6, 2))
record("available_baseline_and_followup", c(120-6, 120-8), c(114, 112))
record("known_status_event_percentage", 100*36/180, 20)
record("eligible_event_accounting_bounds", 100*c(36, 36+(192-180))/192, c(18.75, 25))
record("reversed_welch_95ci", -rev(results$welch_95ci), c(.563770595, 11.436229405))

cat("Illustration checks passed. Values below are calculations from invented examples.\n")
print(results, digits = 10)
