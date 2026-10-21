-- Keep the short review sections together, with compact end-of-chapter spacing.
-- A modest minimum avoids the old fourteen-line reservation and large gaps.
function Div(el)
  if FORMAT:match("latex") and (el.classes:includes("review-answers") or
                               el.classes:includes("review-questions")) then
    el.content:insert(1, pandoc.RawBlock("latex",
      "\\begingroup\\fontsize{11}{14}\\selectfont\\setlength{\\parskip}{3pt}" ..
      "\\titlespacing*{\\section}{0pt}{10pt}{5pt}" ..
      "\\Needspace{5\\baselineskip}\\begin{samepage}"))
    el.content:insert(pandoc.RawBlock("latex", "\\end{samepage}\\endgroup"))
    return el
  end
end
