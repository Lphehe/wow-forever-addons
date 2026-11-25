-- Run with Lua 5.1: lua5.1 scripts/test_menu_title.lua /path/to/reviewed/ControllerForever_Menu.lua
-- The official source is read locally, not redistributed or downloaded by this test.
local sourcePath = assert(arg[1], "Pass the reviewed official CF 3.9.47 ControllerForever_Menu.lua")
-- Lua 5.1 %w uses the host C character class; make the regression deterministic.
local previousCType = os.setlocale(nil, "ctype")
assert(os.setlocale("C", "ctype"), "C character locale unavailable")
local here = (arg[0] or "scripts/test_menu_title.lua"):match("^(.*[/\\])") or ""
local addon = here .. "../addons/controller-forever-zhcn/ControllerForever_ZH/"
local file = assert(io.open(sourcePath, "rb"))
local source = file:read("*a"):gsub("\r\n", "\n"); file:close()
local books, locale = {}, "zhCN"
ControllerForever = { L = {
    register = function(code, entries) books[code] = entries end,
    locale = function() return locale end,
    tr = function(text) return (books[locale] or {})[text] or text end,
} }
menu = {}; ControllerForever.Menu = menu
local sizes = {}
ruleBar = {
    glyphScale = function() return 2 end,
    glyphText = function(text, size)
        sizes[#sizes + 1] = size
        if text == "仅图标" then return "|Tsample:16|t" end
        return (text:gsub("LB", "|Tsample:16|t"))
    end,
}
ControllerForever.RuleBar = ruleBar
-- Execute the actual three upstream formatting functions after reviewing them.
for _, name in ipairs({ "tr", "gt", "gtTitle" }) do
    local chunk = assert(source:match("(function menu%." .. name .. "%([^\n]*\n.-\nend)"), name .. " not found")
    assert(loadstring(chunk, "@" .. sourcePath .. ":" .. name))()
end
dofile(addon .. "ControllerForever_zhCN.lua")
local english = "Warriors and Rogues: Ranged Set"
local chinese = "战士与潜行者：远程按键组"
assert(ControllerForever.L.tr(english) == chinese)
assert(menu.gtTitle(english, 20, 24) == english, "Expected the unmodified 3.9.47 Chinese-title fallback")
local upstream = menu.gtTitle
menu.gtTitle = function(...) return upstream(...), "extra", nil, 17 end
dofile(addon .. "ControllerForever_MenuTitle.lua")
local title, extra, missing, number = menu.gtTitle(english, 20, 24)
assert(title == chinese and extra == "extra" and missing == nil and number == 17)
assert(sizes[#sizes] == 12, "glyphScale/maxPx cap changed")
assert(menu.gtTitle("Hunters: Melee Set", 20, 24) == "猎人：近战按键组")
assert(menu.gtTitle("My custom profile 8675309", 20, 24) == "My custom profile 8675309")
assert(menu.gtTitle("我的自定义配置", 20, 24) == "我的自定义配置")
books.zhCN["Chinese with glyph"] = "按住 LB"
assert(menu.gtTitle("Chinese with glyph", 20, 24) == "按住 |Tsample:16|t")
assert(sizes[#sizes] == 12)
books.zhCN["Icon-only action"] = "仅图标"
assert(menu.gtTitle("Icon-only action", 20, 24) == "Icon-only action")
books.zhCN["Punctuation and glyph"] = "：LB"
assert(menu.gtTitle("Punctuation and glyph", 20, 24) == "Punctuation and glyph")
locale = "enUS"
assert(menu.gtTitle(english, 20, 24) == english)
books.frFR = { [english] = "Guerriers et voleurs : ensemble distance" }; locale = "frFR"
assert(menu.gtTitle(english, 20, 24) == books.frFR[english])
os.setlocale(previousCType, "ctype")
print("PASS: actual upstream fallback reproduced; Chinese titles, glyph cap, icon-only behavior, custom names, languages and return values verified")
