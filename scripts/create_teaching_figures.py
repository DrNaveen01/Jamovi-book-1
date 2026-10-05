"""Rebuild mathematical teaching figures; no clinical data are used."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'images'/'teaching'
OUT.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.family':'serif','font.serif':['Nimbus Roman','DejaVu Serif'],
    'font.size':11,'axes.titlesize':12,'axes.labelsize':11,
    'xtick.labelsize':10,'ytick.labelsize':10,'axes.spines.top':False,
    'axes.spines.right':False,'axes.linewidth':0.8,'figure.facecolor':'white',
    'axes.facecolor':'white','text.color':'#202124','axes.labelcolor':'#202124',
    'savefig.facecolor':'white'})
INK='#354d4a'; LIGHT='#e4ecea'; GREY='#a8aca9'

def finish(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=300,bbox_inches='tight',pad_inches=.08)
    plt.close(fig)

waiting=np.array([2,3,3,4,4,5,6,7,8,18.])
fig,ax=plt.subplots(1,2,figsize=(7.5,3.3),layout='constrained',gridspec_kw={'width_ratios':[1.7,1]})
ax[0].hist(waiting,bins=np.arange(0,22,2),color=LIGHT,edgecolor=INK,linewidth=.8)
ax[0].set(xlabel='Waiting time (minutes)',ylabel='Number of observations',title='Histogram: two-minute bins',xticks=[0,4,8,12,16,20])
ax[0].set_ylim(0,4.5)
ax[1].boxplot(waiting,orientation='vertical',widths=.36,patch_artist=True,
    boxprops={'facecolor':LIGHT,'edgecolor':INK},medianprops={'color':'black','linewidth':1.6},
    whiskerprops={'color':INK},capprops={'color':INK},flierprops={'marker':'o','markerfacecolor':'white','markeredgecolor':INK})
ax[1].set(xlabel='Ten invented values',ylabel='Waiting time (minutes)',title='Boxplot: 1.5-IQR whiskers',xticks=[],ylim=(0,20))
finish(fig,'waiting-distribution')

x=np.linspace(-2,2,41)
ys=[1.7*x+.35*np.sin(5*x),x**3,x**2]
titles=['Roughly linear','Monotonic curve','U-shaped relationship']
fig,ax=plt.subplots(1,3,figsize=(7.5,3.0),layout='constrained')
for a,y,title in zip(ax,ys,titles):
    a.scatter(x,y,s=12,facecolor=INK,edgecolor='none')
    a.set(xlabel='X',ylabel='Y',title=title,xticks=[-2,0,2])
    a.axhline(0,color=GREY,lw=.6,zorder=0)
finish(fig,'relationship-patterns')

# Fixed simulated sample means, from the exact Normal(0, 1/sqrt(25))
# sampling distribution. Keeping their realised values also permits exact
# reproduction in R without relying on matching random-number generators.
rng=np.random.default_rng(20261005)
means=rng.normal(0,1/np.sqrt(25),30)
half=stats.norm.ppf(.975)/np.sqrt(25)
covered=(means-half<=0)&(means+half>=0)
fig,ax=plt.subplots(figsize=(7.5,5.0),layout='constrained')
for i,(m,cover) in enumerate(zip(means,covered),1):
    ax.plot([m-half,m+half],[i,i],color=INK if cover else 'black',lw=1.1,ls='-' if cover else '--')
    ax.scatter([m],[i],s=13,facecolor=INK if cover else 'white',edgecolor=INK if cover else 'black',lw=.8,zorder=3)
ax.axvline(0,color='black',lw=1)
ax.set(xlabel='Sample mean and 95% interval (arbitrary units)',ylabel='Simulated repetition',
    title='Known mean = 0; known SD = 1; n = 25 per repetition\nDashed/open intervals miss the generating mean',ylim=(0,31),yticks=[1,5,10,15,20,25,30])
finish(fig,'confidence-coverage')

x=np.linspace(-2,2,41)
noise=np.random.default_rng(44012).normal(0,.25,len(x))
linear=1+2*x+noise
curved=1+2*x+x**2+.15*np.sin(7*x)
fig,ax=plt.subplots(1,2,figsize=(7.5,3.1),layout='constrained')
for a,y,title in zip(ax,[linear,curved],['Linear mean form','Curved mean fit by a straight line']):
    co=np.polyfit(x,y,1);fit=np.polyval(co,x);resid=y-fit
    a.scatter(fit,resid,s=16,color=INK)
    a.axhline(0,color='black',lw=.8)
    a.set(xlabel='Fitted value (arbitrary units)',ylabel='Residual',title=title,ylim=(-1.7,3))
finish(fig,'regression-diagnostics')

x=np.linspace(-6,6,241);b0=-1.7346010553881064;b1=.8873031950009027
p=1/(1+np.exp(-(b0+b1*x)))
fig,ax=plt.subplots(figsize=(7.5,3.2),layout='constrained')
ax.plot(x,p,color=INK,lw=1.8)
ax.set(xlabel='Predictor (arbitrary units)',ylabel='Modeled event probability',title='Linear log odds, curved probability',ylim=(0,1),xlim=(-6,6))
ax.set_yticks([0,.25,.5,.75,1])
finish(fig,'logistic-curve')

# A complete base-R companion uses the same values and formulas.
r_script=r'''# Rebuild the book's teaching figures using base R only.
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
means <- c(MEANS_REPLACE)
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
noise <- c(NOISE_REPLACE)
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
'''.replace('MEANS_REPLACE',', '.join(f'{m:.15g}' for m in means)).replace('NOISE_REPLACE',', '.join(f'{v:.15g}' for v in noise))
(ROOT/'scripts'/'create_teaching_figures.R').write_text(r_script,encoding='utf-8')
print(f'Created five figures; {covered.sum()}/30 realised intervals cover the generating mean.')
