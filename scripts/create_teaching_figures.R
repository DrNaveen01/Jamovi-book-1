# Rebuild the book's teaching figures using base R only.
# Run from the project root. These are invented or mathematical illustrations.
dir.create("images/teaching", recursive = TRUE, showWarnings = FALSE)
ink <- "#354d4a"; light <- "#e4ecea"
open_png <- function(name, width = 2250, height = 990) {
  png(file.path("images/teaching", paste0(name, ".png")), width = width,
      height = height, res = 300, pointsize = 11)
  par(family = "serif", mar = c(4.5, 4.5, 3.2, 1), bty = "l")
}
waiting <- c(2, 3, 3, 4, 4, 5, 6, 7, 8, 18)
open_png("waiting-distribution")
par(mfrow = c(1, 2))
hist(waiting, breaks = seq(0, 20, 2), right = FALSE, col = light,
     border = ink, main = "Histogram: two-minute bins", xlab = "Waiting time (minutes)",
     ylab = "Number of observations")
# Use type-7 quartiles, matching the book and supplied Python figure.
# Base R's default boxplot hinges can differ for this small sample.
q <- unname(quantile(waiting, c(.25, .5, .75), type = 7))
iqr <- q[3] - q[1]
inside <- waiting[waiting >= q[1] - 1.5*iqr & waiting <= q[3] + 1.5*iqr]
outside <- waiting[waiting < q[1] - 1.5*iqr | waiting > q[3] + 1.5*iqr]
bxp(list(stats = matrix(c(min(inside), q, max(inside)), ncol = 1), n = length(waiting),
         conf = matrix(c(NA, NA), ncol = 1), out = outside,
         group = rep(1, length(outside)), names = ""),
    boxfill = light, border = ink, main = "Boxplot: 1.5-IQR whiskers",
    ylab = "Waiting time (minutes)", ylim = c(0, 20))
dev.off()

x <- seq(-2, 2, length.out = 41)
ys <- list(1.7*x + 0.35*sin(5*x), x^3, x^2)
titles <- c("Roughly linear", "Monotonic curve", "U-shaped relationship")
open_png("relationship-patterns", height = 900)
par(mfrow = c(1, 3), mar = c(4, 4, 3, 1))
for (i in seq_along(ys)) {
  plot(x, ys[[i]], pch = 16, cex = 0.65, col = ink, main = titles[i], xlab = "X", ylab = "Y")
  abline(h = 0, col = "grey65", lwd = 0.6)
}
dev.off()

# These exact realised means are shared with the supplied Python renderer.
means <- c(0.131244818076541, -0.0466247109813649, -0.180805530486657, -0.0903442786158396, -0.0116521045859491, -0.042096277310248, -0.11317881123528, -0.283028077832236, -0.167882204623659, 0.246568670291979, -0.291589160947691, -0.0655614166111951, 0.0968647125703713, -0.228120564684683, -0.183355672764194, 0.221459710222924, -0.0216476899632872, 0.12632277537247, -0.438852719020365, -0.150574778607915, -0.348892551700776, 0.246628981204136, 0.120819933128122, 0.202236538976598, 0.00120735138702795, -0.0387528346555857, 0.0365964317893742, 0.182643405067754, 0.155750500676461, 0.00299348287863166)
half <- qnorm(0.975)/sqrt(25)
covered <- (means - half <= 0) & (means + half >= 0)
open_png("confidence-coverage", height = 1500)
plot(NA, xlim = range(means - half, means + half), ylim = c(0, 31),
     xlab = "Sample mean and 95% interval (arbitrary units)", ylab = "Simulated repetition",
     main = "Known mean = 0; known SD = 1; n = 25 per repetition\nDashed/open intervals miss the generating mean")
abline(v = 0, col = "black")
for (i in seq_along(means)) {
  segments(means[i] - half, i, means[i] + half, i, col = if (covered[i]) ink else "black",
           lty = if (covered[i]) 1 else 2)
  points(means[i], i, pch = if (covered[i]) 16 else 1, col = if (covered[i]) ink else "black", cex = .7)
}
dev.off()

open_png("regression-diagnostics", height = 930)
par(mfrow = c(1, 2))
noise <- c(0.280896424004329, -0.0124608436566407, 0.524663852623058, -0.120329840777334, 0.159140397753386, 0.287961229916486, 0.702825757278217, -0.0236272302403268, 0.0206716581683834, 0.0528538701660932, -0.194819812150494, -0.224186904830015, -0.10232293629873, 0.0411374306589421, 0.13510854814079, -0.0970491876454344, -0.0428847428022478, 0.249858218447293, -0.0803635918660561, -0.00126001035897069, 0.274808378322909, -0.184975624523972, -0.107217441531821, -0.186366031738571, 0.247132128371766, 0.710468488990541, -0.00333714200397903, -0.0363227699905731, -0.194946451937763, 0.182123660878437, 0.00610744356797075, -0.0365810914835664, -0.0200571022430538, 0.0111525166613594, -0.151289318381905, -0.155426400248355, 0.0454886281276142, -0.0187401843359373, -0.197199444224074, 0.197351428345569, -0.236144349639209)
linear <- 1 + 2*x + noise
curved <- 1 + 2*x + x^2 + 0.15*sin(7*x)
for (i in 1:2) {
  y <- list(linear, curved)[[i]]
  model <- lm(y ~ x)
  plot(fitted(model), resid(model), pch = 16, cex = .7, col = ink, ylim = c(-1.7, 3),
       main = c("Linear mean form", "Curved mean fit by a straight line")[i],
       xlab = "Fitted value (arbitrary units)", ylab = "Residual")
  abline(h = 0, col = "black")
}
dev.off()

x <- seq(-6, 6, length.out = 241)
p <- plogis(-1.7346010553881064 + 0.8873031950009027*x)
open_png("logistic-curve", height = 960)
plot(x, p, type = "l", lwd = 2, col = ink, ylim = c(0, 1),
     main = "Linear log odds, curved probability",
     xlab = "Predictor (arbitrary units)", ylab = "Modeled event probability")
dev.off()
