-- Apply teaching-panel styles without changing the manuscript's content.
local function panel(block, kind)
  if FORMAT:match("latex") then
    return pandoc.Div({
      pandoc.RawBlock("latex", "\\begin{book" .. kind .. "}"),
      block,
      pandoc.RawBlock("latex", "\\end{book" .. kind .. "}")
    })
  end
  return pandoc.Div({block}, pandoc.Attr("", {"book-panel", "book-" .. kind}))
end

-- Permit a line break after an underscore in long variable names in print.
-- The visible identifier and the source code remain unchanged.
function Code(el)
  if not FORMAT:match("latex") or not el.text:find("_", 1, true) then return nil end
  local escapes = { ["\\"]="\\textbackslash{}", ["_"]="\\_\\allowbreak{}",
    ["#"]="\\#", ["$"]="\\$", ["%"]="\\%", ["&"]="\\&", ["{"]="\\{", ["}"]="\\}",
    ["^"]="\\textasciicircum{}", ["~"]="\\textasciitilde{}" }
  local escaped = el.text:gsub(".", function(c) return escapes[c] or c end)
  return pandoc.RawInline("latex", "\\texttt{" .. escaped .. "}")
end

-- Give the short 'Meaning' header enough room for its longer body text.
function Table(el)
  if #el.colspecs == 4 and #el.head.rows > 0 then
    local cells = el.head.rows[1].cells
    if #cells == 4 and pandoc.utils.stringify(cells[1].contents) == "Variable type"
      and pandoc.utils.stringify(cells[2].contents) == "Meaning" then
      local widths = {.14, .24, .27, .35}
      for i = 1, 4 do el.colspecs[i][2] = widths[i] end
      return el
    end
  end
end

function Pandoc(doc)
  local output = pandoc.List()
  local next_panel = nil
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" then
      next_panel = nil
      local title = pandoc.utils.stringify(block.content):lower()
      if block.level == 2 and title == "learning objectives" then
        next_panel = "objectives"
      elseif title:find("illustration", 1, true) or title == "an invented validation audit" then
        next_panel = "example"
      elseif title == "reporting example" then
        next_panel = "reporting"
      end
      output:insert(block)
    elseif next_panel and (block.t == "Para" or block.t == "Plain") then
      output:insert(panel(block, next_panel))
      next_panel = nil
    else
      output:insert(block)
    end
  end
  doc.blocks = output
  return doc
end
