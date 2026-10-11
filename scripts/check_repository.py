"""Check curated links and preservation of original research, literature and formal sources."""
import argparse
import hashlib
import json
import os
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick', action='store_true', help='Check paths and sizes without hashing preserved files')
    args = parser.parse_args()
    assets = json.loads((ROOT / 'archives/asset-manifest.json').read_text(encoding='utf-8'))['files']
    compressed = {item['path']: item for item in assets}
    preservation = json.loads((ROOT / 'archives/preservation-manifest.json').read_text(encoding='utf-8'))['files']
    history = json.loads((ROOT / 'archives/history-manifest.json').read_text(encoding='utf-8'))['files']
    archived = {item['path']: item for item in history}
    errors = []
    with zipfile.ZipFile(ROOT / 'archives/history.zip') as archive:
        for item in preservation:
            relative = item['path']
            if item['storage'] == 'history':
                try:
                    data = archive.read(relative)
                    if len(data) != item['bytes'] or (not args.quick and hashlib.sha256(data).hexdigest() != item['sha256']):
                        errors.append(f'History integrity: {relative}')
                except KeyError:
                    errors.append(f'Missing history: {relative}')
            elif item['storage'] == 'gzip':
                packaged = compressed[relative]
                path = ROOT / packaged['stored_path']
                if not path.is_file() or path.stat().st_size != packaged['stored_bytes']:
                    errors.append(f'Missing/changed package: {relative}')
                elif not args.quick and sha(path) != packaged['stored_sha256']:
                    errors.append(f'Compressed integrity: {relative}')
            else:
                path = ROOT / item.get('stored_path', relative)
                if not path.is_file() or path.stat().st_size != item['bytes']:
                    errors.append(f'Missing/changed original: {relative}')
                elif not args.quick and sha(path) != item['sha256']:
                    errors.append(f'Original integrity: {relative}')

    curated = [ROOT / 'README.md', ROOT / 'research/README.md', ROOT / 'literature/README.md', ROOT / 'literature/CATALOG.md', *sorted((ROOT / 'docs').glob('*.md'))]
    for document in curated:
        for link in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8-sig')):
            link = link.strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
                continue
            target = (document.parent / unquote(link.split('#', 1)[0])).resolve()
            try:
                relative = target.relative_to(ROOT).as_posix()
            except ValueError:
                errors.append(f'Link outside repository: {document.name}: {link}')
                continue
            if not target.exists():
                errors.append(f'Broken link: {document.relative_to(ROOT)}: {link}')
    for directory, subdirs, files in os.walk(ROOT):
        subdirs[:] = [name for name in subdirs if name not in ('.lake', '.git', '__pycache__', 'pages')]
        for name in files:
            path = Path(directory) / name
            if path.stat().st_size >= 100 * 1024 * 1024 and path.relative_to(ROOT).as_posix() not in compressed:
                errors.append(f'GitHub oversized asset: {path.relative_to(ROOT)}')
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print(f'PASS: {len(curated)} curated documents, {len(preservation)} preserved files, {len(assets)} compressed assets, {len(history)} historical originals')


if __name__ == '__main__':
    main()
