#!/usr/bin/env python3
import re,json,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
addon=root/'addons/controller-forever-zhcn/ControllerForever_ZH'
lua=(addon/'ControllerForever_zhCN.lua').read_text(encoding='utf-8')
toc=(addon/'ControllerForever_ZH.toc').read_text(encoding='utf-8')
assert 'ControllerForever.L.register("zhCN", {' in lua
assert '## Dependencies: ControllerForever' in toc
assert '## Version: 0.3.0-beta' in toc
pat=re.compile(r'^\s+\[("(?:\\.|[^"\\])*")\]\s*=\s*("(?:\\.|[^"\\])*"),$',re.M)
pairs=[(json.loads(k),json.loads(v)) for k,v in pat.findall(lua)]
assert len(pairs)==2289,len(pairs)
assert len({k for k,v in pairs})==len(pairs)
assert sum(x.lstrip().startswith('["') for x in lua.splitlines())==len(pairs)
fmt=re.compile(r'%(?:\d+\$)?(?:\d+)?[dsf]|%%')
bad=[k[:70] for k,v in pairs if fmt.findall(k)!=fmt.findall(v)]
assert not bad,bad[:15]
zp=root/'releases/ControllerForever_ZH-0.3.0-beta.zip'
with zipfile.ZipFile(zp) as z:
 assert z.testzip() is None
 assert z.read('ControllerForever_ZH/ControllerForever_zhCN.lua')==(addon/'ControllerForever_zhCN.lua').read_bytes()
 assert z.read('ControllerForever_ZH/ControllerForever_ZH.toc')==(addon/'ControllerForever_ZH.toc').read_bytes()
stats=json.loads((root/'TRANSLATION_STATS.json').read_text())
assert stats['keys_with_zhCN_entries']==len(pairs)
print('PASS: syntax-friendly strings, unique keys, placeholders and ZIP')
