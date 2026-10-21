<<<<<<< HEAD
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
=======
-- Keep each short review-question or review-answer block together in print.
-- The teaching text and deliberately empty Hands-on boxes are unchanged.
function Div(el)
  if FORMAT:match("latex") and (el.classes:includes("review-answers") or
                               el.classes:includes("review-questions")) then
    local lines = el.classes:includes("review-answers") and 14 or 10
    el.content:insert(1, pandoc.RawBlock("latex", "\\Needspace{" .. lines .. "\\baselineskip}\\begin{samepage}"))
    el.content:insert(pandoc.RawBlock("latex", "\\end{samepage}"))
>>>>>>> 411391a1e81828f29055b7aaced890dd49b2f83e
    return el
  end
end
