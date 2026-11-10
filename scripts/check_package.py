#!/usr/bin/env python3
"""Static validation for the standalone Controller Forever zhCN language addon."""
from pathlib import Path
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ADDON = ROOT / "addons" / "controller-forever-zhcn" / "ControllerForever_ZH"
RELEASE = ROOT / "releases" / "ControllerForever_ZH-0.2.0-beta.zip"
lua_path = ADDON / "ControllerForever_zhCN.lua"
toc_path = ADDON / "ControllerForever_ZH.toc"

lua = lua_path.read_text(encoding="utf-8")
toc = toc_path.read_text(encoding="utf-8")
assert 'ControllerForever.L.register("zhCN", {' in lua
assert "## Dependencies: ControllerForever" in toc
assert "ControllerForever_zhCN.lua" in toc

pattern = re.compile(r'^\s+\[("(?:\\.|[^"\\])*")\]\s*=\s*("(?:\\.|[^"\\])*"),$', re.MULTILINE)
keys = []
for match in pattern.finditer(lua):
    keys.append(json.loads(match.group(1)))
    json.loads(match.group(2))
assert len(keys) == len(set(keys)), "Duplicate localization keys"
assert len(keys) > 2000, "Unexpectedly few localized strings"
assert sum(line.lstrip().startswith('["') for line in lua.splitlines()) == len(keys), "Malformed Lua row"

with zipfile.ZipFile(RELEASE) as archive:
    assert archive.testzip() is None
    files = set(archive.namelist())
    assert "ControllerForever_ZH/ControllerForever_ZH.toc" in files
    assert "ControllerForever_ZH/ControllerForever_zhCN.lua" in files
    assert archive.read("ControllerForever_ZH/ControllerForever_ZH.toc") == toc_path.read_bytes()
    assert archive.read("ControllerForever_ZH/ControllerForever_zhCN.lua") == lua_path.read_bytes()
print(f"PASS: {len(keys)} unique translation keys, matching TOC, Lua and ZIP contents")
