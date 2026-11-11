#!/usr/bin/env python3
from pathlib import Path
import json,re,zipfile
root=Path(__file__).resolve().parents[1]
addon=root/'addons/controller-forever-zhcn/ControllerForever_ZH'
lua=(addon/'ControllerForever_zhCN.lua').read_text(encoding='utf8')
toc=(addon/'ControllerForever_ZH.toc').read_text(encoding='utf8')
assert 'ControllerForever.L.register("zhCN", {' in lua
assert '## Dependencies: ControllerForever' in toc
assert '## Version: 0.4.1-rc' in toc
pat=re.compile(r'^\s+\[("(?:\\.|[^"\\])*")\]\s*=\s*("(?:\\.|[^"\\])*"),$',re.M)
pairs=[(json.loads(k),json.loads(v)) for k,v in pat.findall(lua)]
assert len(pairs)==3357,len(pairs)
assert len({k for k,v in pairs})==len(pairs)
assert sum(line.lstrip().startswith('["') for line in lua.splitlines())==len(pairs)
fmt=re.compile(r'%(?:\d+\$)?[-+#0]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[cdEefFgGiosuxXq]|%%')
for k,v in pairs:
 assert fmt.findall(k)==fmt.findall(v),(k,fmt.findall(k),fmt.findall(v))
 for control in [r'\|c[0-9a-fA-F]{8}',r'\|r',r'\|T',r'\|A']:
  assert re.findall(control,k)==re.findall(control,v),(k,control)
 assert v.strip(),k
stats=json.loads((root/'TRANSLATION_STATS.json').read_text(encoding='utf8'))
assert stats['total_language_entries']==len(pairs)
zipfile_path=root/'releases/ControllerForever_ZH-0.4.1-rc.zip'
with zipfile.ZipFile(zipfile_path) as z:
 assert z.testzip() is None
 assert z.read('ControllerForever_ZH/ControllerForever_ZH.toc')==(addon/'ControllerForever_ZH.toc').read_bytes()
 assert z.read('ControllerForever_ZH/ControllerForever_zhCN.lua')==(addon/'ControllerForever_zhCN.lua').read_bytes()
print('PASS: 3357 entries, keys, controls, placeholders, zip parity')
