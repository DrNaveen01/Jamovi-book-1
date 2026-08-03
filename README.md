# Hands-On Data Analysis Using Jamovi

A practical Quarto book for medical students, health researchers, clinicians, and public health professionals learning statistical analysis using jamovi.

The book focuses on selecting appropriate statistical methods, performing analyses in jamovi, interpreting results, and reporting findings clearly.

## Current status

This repository contains the first volume of a planned series.

-   **Title:** *Hands-On Data Analysis Using Jamovi*
-   **Subtitle:** *Foundations and Core Statistical Methods for Health Researchers*
-   **Author:** Dr Naveen Suthar
-   **Format:** Quarto book
-   **Website:** GitHub Pages
-   **Status:** Under active development

## Topics covered

The current volume includes:

-   foundations of health-data analysis;
-   getting started with jamovi;
-   data management;
-   descriptive statistics;
-   graphical presentation;
-   hypothesis testing;
-   comparison of two or more groups;
-   categorical data analysis;
-   correlation;
-   linear regression;
-   logistic regression;
-   interpretation and reporting of results.

Appendices include statistical formulas, test-selection guidance, a glossary, and practice exercises.

## Repository structure

``` text
Jamovi-book-1/
├── .github/workflows/   # GitHub Actions
├── data/                # Practice datasets
├── images/              # Screenshots and figures
├── docs/                # Rendered website
├── *.qmd                # Book chapters
├── _quarto.yml          # Book configuration
├── references.bib       # Bibliography
└── README.md
```

## Requirements

Install:

-   [Quarto](https://quarto.org/)
-   [R](https://cran.r-project.org/)
-   [RStudio](https://posit.co/download/rstudio-desktop/)
-   Git

Required R packages can be installed using:

``` r
install.packages(c("knitr", "rmarkdown"))
```


## Preview locally

``` bash
quarto preview
```

## Render the book

Render the HTML website:

``` bash
quarto render --to html
```

Render all configured formats:

``` bash
quarto render
```

The HTML website is generated in the `docs/` directory.

## Automatic website deployment

GitHub Actions automatically rebuilds and publishes the website whenever changes are pushed to the `main` branch.

Routine workflow:

``` bash
git add .
git commit -m "Update chapter"
git push origin main
```

After the push:

1.  GitHub Actions installs the required software.
2.  Quarto renders the book.
3.  The rendered website is deployed to GitHub Pages.

The workflow can be monitored under the repository's **Actions** tab.

## Adding a chapter

1.  Create a new `.qmd` file.
2.  Add the chapter title and content.
3.  Register the file under `book: chapters:` in `_quarto.yml`.
4.  Run `quarto preview`.
5.  Commit and push the changes.

## Data and confidentiality

Only anonymised, synthetic, or publicly available datasets should be committed.

Do not upload:

-   identifiable patient data;
-   confidential institutional data;
-   passwords or access tokens;
-   restricted research datasets.

## Contribution

Major revisions should preferably be developed on a separate branch.

``` bash
git switch -c revise-chapter-name
```

After editing:

``` bash
quarto render --to html
git add .
git commit -m "Revise chapter name"
git push -u origin revise-chapter-name
```

Minor corrections may be pushed directly to `main`.

## Planned development

Future additions may include:

-   more worked examples;
-   downloadable jamovi `.omv` files;
-   practice datasets and exercises;
-   improved PDF formatting;
-   advanced statistical methods;
-   teaching and workshop resources;
-   additional volumes in the series.

## Website

https://drnaveen01.github.io/Jamovi-book-1/

## Repository

https://github.com/DrNaveen01/Jamovi-book-1

## Copyright

Copyright © 2026 Dr Naveen Suthar.

This repository is currently maintained as a private development project.
All original content is protected by copyright. No licence has yet been granted
for reuse or redistribution.
