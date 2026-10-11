"""Check local Markdown links and integrity of the frozen bridge report."""
from pathlib import Path
import re
import json
import hashlib

base=Path(__file__).resolve().parents[1]
files=[base/'README.md',base/'literature/README.md',
       base/'literature/bridge_reading_map_20261004.md',
       *base.glob('research/odd_zeta_bridge*.md')]
missing=[]
count=0
for p in files:
    text=p.read_text(encoding='utf-8')
    text=re.sub(r'```.*?```','',text,flags=re.S)
    text=re.sub(r'`[^`]*`','',text)
    text=re.sub(r'\\\[.*?\\\]','',text,flags=re.S)
    for link in re.findall(r'\]\(([^\n)]+)\)',text):
        if link.startswith(('http:','https:','#','mailto:')):
            continue
        target=link.strip('<>').split('#')[0]
        if target.startswith('/E:/'):
            target=target[1:]
        candidate=Path(target) if re.match(r'^[A-Za-z]:/',target) else p.parent/target
        if not candidate.exists():
            missing.append({'from':str(p),'target':link})
        count+=1
frozen=base/'research/odd_zeta_bridge_catalan_20261004.md'
digest=hashlib.sha256(frozen.read_bytes()).hexdigest()
assert digest=='c06d052d8074305e45c18b9cc7554f50d2aae7fe999a2b2b85a9c8b86d66c42d'
result={'checked_files':[str(p) for p in files],
        'local_links_checked':count,'missing_links':missing,
        'frozen_catalan_report_unchanged':True,'frozen_sha256':digest}
(base/'research/odd_zeta_bridge_delivery_20261004.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'local_links_checked':count,'missing_links':missing,
                  'frozen_catalan_report_unchanged':True},ensure_ascii=False,indent=2))
assert not missing
