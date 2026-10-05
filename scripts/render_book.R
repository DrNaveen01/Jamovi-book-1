# Render the editable book from RStudio or Rscript. No R package is required.
render_book <- function(format = c("all", "html", "pdf"), profile = NULL) {
  format <- match.arg(format)
  if (!file.exists("_quarto.yml")) {
    stop("Set the working directory to the book project root first.")
  }
  quarto <- unname(Sys.which("quarto"))
  if (!nzchar(quarto)) stop("Install Quarto and make quarto available on PATH.")
  if (is.null(profile) && .Platform$OS.type == "windows") profile <- "windows"
  if (!is.null(profile) && !profile %in% c("windows", "portable")) {
    stop("Use profile = 'windows', profile = 'portable', or profile = NULL.")
  }
  args <- "render"
  if (format != "all") args <- c(args, "--to", format)
  if (!is.null(profile)) args <- c(args, "--profile", profile)
  status <- system2(quarto, args)
  if (status != 0L) stop("Quarto render failed; inspect its output above.")
  invisible(status)
}

# source("scripts/render_book.R") renders both formats immediately.
render_book()
