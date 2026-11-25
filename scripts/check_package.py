#!/usr/bin/env python3
from pathlib import Path
import json,re,zipfile
root=Path(__file__).resolve().parents[1]
addon=root/'addons/controller-forever-zhcn/ControllerForever_ZH'
lua=(addon/'ControllerForever_zhCN.lua').read_text(encoding='utf8')
toc=(addon/'ControllerForever_ZH.toc').read_text(encoding='utf8')
assert 'ControllerForever.L.register("zhCN", {' in lua
assert '## Dependencies: ControllerForever' in toc
assert '## OptionalDeps: ControllerForever_Locales' in toc
assert toc.splitlines().index('ControllerForever_zhCN.lua') < toc.splitlines().index('ControllerForever_MenuTitle.lua')
assert '## Version: 0.4.1-rc' in toc
pat=re.compile(r'^\s+\[("(?:\\.|[^"\\])*")\]\s*=\s*("(?:\\.|[^"\\])*"),$',re.M)
pairs=[(json.loads(k),json.loads(v)) for k,v in pat.findall(lua)]
stats=json.loads((root/'TRANSLATION_STATS.json').read_text(encoding='utf8'))
assert len(pairs)==stats['total_language_entries'],len(pairs)
assert dict(pairs)['Warriors and Rogues: Ranged Set']=='战士与潜行者：远程按键组'
assert dict(pairs)['Hunters: Melee Set']=='猎人：近战按键组'
assert len({k for k,v in pairs})==len(pairs)
assert sum(line.lstrip().startswith('["') for line in lua.splitlines())==len(pairs)
fmt=re.compile(r'%(?:\d+\$)?[-+#0]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[cdEefFgGiosuxXq]|%%')
for k,v in pairs:
 assert fmt.findall(k)==fmt.findall(v),(k,fmt.findall(k),fmt.findall(v))
 for control in [r'\|c[0-9a-fA-F]{8}',r'\|r',r'\|T',r'\|A']:
  assert re.findall(control,k)==re.findall(control,v),(k,control)
 assert v.strip(),k
zipfile_path=root/'releases/ControllerForever_ZH-0.4.1-rc.zip'
with zipfile.ZipFile(zipfile_path) as z:
 assert z.testzip() is None
 assert z.read('ControllerForever_ZH/ControllerForever_ZH.toc')==(addon/'ControllerForever_ZH.toc').read_bytes()
 assert z.read('ControllerForever_ZH/ControllerForever_zhCN.lua')==(addon/'ControllerForever_zhCN.lua').read_bytes()
 assert z.read('ControllerForever_ZH/ControllerForever_MenuTitle.lua')==(addon/'ControllerForever_MenuTitle.lua').read_bytes()
print(f'PASS: {len(pairs)} entries, keys, controls, placeholders, optional dependency, zip parity')
