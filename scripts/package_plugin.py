#!/usr/bin/env python3
"""Build the distributable plugin ZIP from the root plugin sources."""
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'plugin.json').read_text())
compatibility = json.loads((root / '.codex-plugin/plugin.json').read_text())
for field in ('name', 'version', 'description', 'author', 'keywords'):
    if manifest.get(field) != compatibility.get(field):
        raise ValueError(f'Plugin manifests disagree on {field}')
if manifest['extensions']['com.openai']['interface'] != compatibility['interface']:
    raise ValueError('Plugin manifests disagree on interface metadata')
name, version = manifest['name'], manifest['version']
files = [root / 'plugin.json', root / '.codex-plugin/plugin.json']
files += sorted(p for p in (root / 'skills').rglob('*') if p.is_file() and not p.name.startswith('.') and '__pycache__' not in p.parts)
files += sorted(p for p in (root / 'assets').rglob('*') if p.is_file())
assert files and all(p.resolve().is_relative_to(root) for p in files)
for icon in ('composerIcon', 'logo'):
    assert (root / manifest['extensions']['com.openai']['interface'][icon]).is_file()
assert (root / 'skills/dataiku-excel-coach/SKILL.md').is_file()

dist = root / 'dist'
dist.mkdir(exist_ok=True)
archive = dist / f'{name}-{version}.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as package:
    for path in files:
        package.write(path, path.relative_to(root).as_posix())
with zipfile.ZipFile(archive) as package:
    assert package.testzip() is None
    assert 'plugin.json' in package.namelist()
    assert all(not n.endswith(('.xlsx', '.csv', '.jsonl')) for n in package.namelist())

print(f'ZIP: {archive}')
print(f'Validated ZIP integrity and {len(files)} packaged files.')
