"""One-time packaging of the original local archive. Do not rerun after publication."""
import gzip
import hashlib
import json
import os
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'archives'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()


def entry(path):
    return {'path': path.relative_to(ROOT).as_posix(), 'bytes': path.stat().st_size, 'sha256': digest(path)}


def dump(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    if (ARCHIVE / 'preservation-manifest.json').exists():
        raise SystemExit('Already packaged; use restore_assets.py, not this one-time tool.')
    ARCHIVE.mkdir(exist_ok=True)
    originals = []
    for name in ['research', 'literature', 'Zeta5Irrational', 'Zeta5-mo271', 'Zeta7Formal', 'tmp/pdfs']:
        for base, dirs, files in os.walk(ROOT / name):
            dirs[:] = [d for d in dirs if d not in ('.git', '.lake', '__pycache__')]
            originals.extend(Path(base) / f for f in files if not f.endswith(('.pyc', '.olean', '.ilean', '.trace')))
    originals.extend(ROOT / name for name in ['README.md', 'Main.lean', 'Scratch3.lean', 'lakefile.toml', 'lake-manifest.json', 'lean-toolchain', 'ZETA5_IS_IRRATIONAL.pdf'])
    records = {p.relative_to(ROOT).as_posix(): entry(p) for p in sorted(set(originals))}
    historic = [ROOT / 'README.md', ROOT / 'literature/README.md', ROOT / 'research/cdt_odd_background_progress_20261006.md', ROOT / 'research/research_global_review_policy.md', *sorted((ROOT / 'research').glob('archive*.py'))]
    history_records = [entry(p) for p in historic]
    with zipfile.ZipFile(ARCHIVE / 'history.zip', 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for p in historic:
            archive.write(p, p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(ARCHIVE / 'history.zip') as archive:
        for item in history_records:
            data = archive.read(item['path'])
            assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256']
            records[item['path']]['storage'] = 'history'
    dump(ARCHIVE / 'history-manifest.json', {'date': '2026-10-11', 'archive': 'archives/history.zip', 'files': history_records})

    assets = []
    for p in sorted((ROOT / 'research').rglob('*.json')):
        if p.stat().st_size < 1_000_000:
            continue
        item = entry(p)
        packed = p.with_name(p.name + '.gz')
        with p.open('rb') as stream, packed.open('xb') as destination:
            with gzip.GzipFile(filename='', mode='wb', fileobj=destination, mtime=0, compresslevel=9) as compressor:
                while block := stream.read(1024 * 1024):
                    compressor.write(block)
        h = hashlib.sha256()
        size = 0
        with gzip.open(packed, 'rb') as stream:
            while block := stream.read(1024 * 1024):
                h.update(block)
                size += len(block)
        assert h.hexdigest() == item['sha256'] and size == item['bytes']
        item.update(stored_path=packed.relative_to(ROOT).as_posix(), stored_bytes=packed.stat().st_size, stored_sha256=digest(packed))
        assets.append(item)
        records[item['path']]['storage'] = 'gzip'
        print(f'Packed {item["path"]}: {item["bytes"]} -> {item["stored_bytes"]}', flush=True)
    dump(ARCHIVE / 'asset-manifest.json', {'date': '2026-10-11', 'format': 'gzip, deterministic mtime=0', 'files': assets})

    alias = ROOT / 'literature/fauzan_zeta5.pdf'
    redundant = ROOT / 'ZETA5_IS_IRRATIONAL.pdf'
    assert digest(alias) == digest(redundant)
    records['ZETA5_IS_IRRATIONAL.pdf'].update(storage='alias', stored_path='literature/fauzan_zeta5.pdf')
    for item in records.values():
        item.setdefault('storage', 'original')
    dump(ARCHIVE / 'preservation-manifest.json', {'date': '2026-10-11', 'scope': 'Original literature, formal source, technical notes, certificates, source screenshots and root Lean configuration; excludes build and Python caches.', 'files': list(records.values())})

    # Delete only exact originals verified above; all targets are inside ROOT.
    delete = [ROOT / item['path'] for item in assets]
    delete += [p for p in historic if p.relative_to(ROOT).as_posix() not in ('README.md', 'literature/README.md')]
    delete += [redundant]
    cleanup = []
    for p in delete:
        resolved = p.resolve()
        assert resolved.is_relative_to(ROOT)
        cleanup.append({'path': p.relative_to(ROOT).as_posix(), 'reason': 'Original bytes retained in gzip, history.zip or identical literature source'})
        p.unlink()
    # Rendered paper pages can be regenerated from the retained original PDF.
    for p in sorted((ROOT / 'pages').glob('*.png')):
        assert p.resolve().is_relative_to(ROOT)
        cleanup.append({**entry(p), 'reason': 'Regenerable page rendering; original PDF retained in literature'})
        p.unlink()
    if (ROOT / 'pages').exists() and not any((ROOT / 'pages').iterdir()):
        (ROOT / 'pages').rmdir()
    dump(ARCHIVE / 'cleanup-manifest.json', {'date': '2026-10-11', 'files': cleanup})
    with (ROOT / '.gitignore').open('a', encoding='utf-8') as stream:
        for item in assets:
            stream.write('/' + item['path'] + '\n')
    print(f'Preserved {len(records)} files; compressed {len(assets)} JSON; historical archive {len(history_records)} files', flush=True)


if __name__ == '__main__':
    main()
