-- Work around CF 3.9.47 treating a Chinese-only title as an empty glyph label.
-- Keep the upstream result for other languages, custom names and icon-only text.
local CF = ControllerForever
local menu = CF and CF.Menu
if not (menu and type(menu.gtTitle) == "function") then return end
local original = menu.gtTitle
local unpackValues = unpack or table.unpack
local function pack(...) return { n = select("#", ...), ... } end

local function hasChineseWords(text)
    local words = text:gsub("|c%x%x%x%x%x%x%x%x", ""):gsub("|r", "")
        :gsub("|T.-|t", ""):gsub("|A.-|a", "")
    for a, b, c in words:gmatch("([\224-\239])([\128-\191])([\128-\191])") do
        local code = (a:byte() - 224) * 4096 + (b:byte() - 128) * 64 + c:byte() - 128
        if (code >= 0x3400 and code <= 0x4DBF) or (code >= 0x4E00 and code <= 0x9FFF) or (code >= 0xF900 and code <= 0xFAFF) then return true end
    end
    return false
end

menu.gtTitle = function(text, size, maxPx, ...)
    local L = CF.L
    if not (L and type(L.locale) == "function" and L.locale() == "zhCN"
        and type(L.tr) == "function" and type(menu.gt) == "function" and type(text) == "string") then
        return original(text, size, maxPx, ...)
    end
    local result = pack(original(text, size, maxPx, ...))
    if result[1] == text then
        local translated = L.tr(text)
        if type(translated) == "string" and translated ~= text and hasChineseWords(translated) then
            -- The original already tried rendering. Reuse gt with the same glyph-height cap.
            local glyphs = CF.RuleBar
            if maxPx and size and glyphs and type(glyphs.glyphScale) == "function" then
                local ok, scale = pcall(glyphs.glyphScale)
                if ok and type(scale) == "number" and scale > 0 and size * scale > maxPx then size = maxPx / scale end
            end
            local ok, rendered = pcall(menu.gt, text, size)
            if ok and type(rendered) == "string" and hasChineseWords(rendered) then result[1] = rendered end
        end
    end
    return unpackValues(result, 1, result.n)
end
