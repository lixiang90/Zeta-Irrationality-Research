"""Restore compressed research JSON to its original path, checking original SHA-256."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def restore(item, verify_only=False):
    target = (ROOT / item['path']).resolve()
    source = (ROOT / item['stored_path']).resolve()
    if not target.is_relative_to(ROOT) or not source.is_relative_to(ROOT):
        raise ValueError('Asset path escapes the repository')
    digest = hashlib.sha256()
    size = 0
    temporary = target.with_name(target.name + '.restoring')
    if target.exists() and not verify_only:
        if target.stat().st_size == item['bytes'] and hashlib.sha256(target.read_bytes()).hexdigest() == item['sha256']:
            return 'already restored'
        raise ValueError(f'Refusing to overwrite different file: {target}')
    output = None
    temporary_created = False
    try:
        if not verify_only:
            target.parent.mkdir(parents=True, exist_ok=True)
            output = temporary.open('xb')
            temporary_created = True
        with gzip.open(source, 'rb') as stream:
            while block := stream.read(1024 * 1024):
                digest.update(block)
                size += len(block)
                if output:
                    output.write(block)
        if size != item['bytes'] or digest.hexdigest() != item['sha256']:
            raise ValueError(f'Original integrity mismatch: {item["path"]}')
        if output:
            output.close()
            output = None
            temporary.replace(target)
        return 'verified' if verify_only else 'restored'
    finally:
        if output:
            output.close()
        if temporary_created and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--all', action='store_true')
    selection.add_argument('--path', help='Original repository-relative JSON path')
    parser.add_argument('--verify-only', action='store_true', help='Validate without writing restored files')
    args = parser.parse_args()
    entries = json.loads((ROOT / 'archives/asset-manifest.json').read_text(encoding='utf-8'))['files']
    if args.path:
        normalized = args.path.replace('\\', '/')
        entries = [item for item in entries if item['path'] == normalized]
        if not entries:
            parser.error(f'Path is not in asset manifest: {args.path}')
    for item in entries:
        print(f'{restore(item, args.verify_only)}: {item["path"]}')
    print(f'{len(entries)} assets complete')


if __name__ == '__main__':
    main()
