#!/usr/bin/env python3
from pathlib import Path
import json,zipfile
root=Path(__file__).resolve().parents[1]
source=root/'extension'
meta=json.loads((source/'manifest.json').read_text())
destination=root/'dist'/('v1-modern-dashboard-'+meta['version']+'.zip')
destination.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(source.rglob('*')):
        if p.is_file():
            z.write(p,p.relative_to(source).as_posix())
print(destination)
