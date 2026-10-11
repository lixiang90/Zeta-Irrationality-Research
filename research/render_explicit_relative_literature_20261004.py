"""Read-only first-page rendering of the five explicit-relative sources.

Run with C:/Python312/python.exe.  Uses fitz and PIL as requested, preserves
all PDF bytes, and deliberately does not set visual-check flags automatically.
Those flags are recorded only after actual image inspection by the researcher.
"""
from pathlib import Path
import hashlib
import json
import textwrap
import fitz
from PIL import Image, ImageDraw, ImageFont


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / 'literature/manifest_explicit_relative_20261004.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    sources = manifest['sources']
    assert len(sources) == 5
    target = root / 'research/artifacts/explicit_relative_literature_20261004'
    target.mkdir(parents=True, exist_ok=True)
    records, page_images = [], []
    for source in sources:
        path = root / 'literature' / source['file']
        before_hash = digest(path)
        before_size = path.stat().st_size
        assert before_hash == source['sha256'], (path.name, before_hash)
        assert before_size == source['bytes']
        with fitz.open(path) as doc:
            assert len(doc) == source['pages']
            pix = doc[0].get_pixmap(matrix=fitz.Matrix(1.75, 1.75), alpha=False)
            image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
            first_page = target / (path.stem + '_first_page.png')
            image.save(first_page)
            pages = len(doc)
        assert digest(path) == before_hash
        assert path.stat().st_size == before_size
        records.append({'file': path.name, 'pages': pages, 'bytes': before_size,
                        'sha256': before_hash,
                        'first_page_png': first_page.relative_to(root).as_posix()})
        page_images.append(image)

    # Full first pages, without removing margin arXiv version or date footnotes.
    # Individual originals are also retained for legible full-resolution review.
    width, margin, caption_height = 1030, 30, 100
    font_path = Path('C:/Windows/Fonts/arial.ttf')
    font = ImageFont.truetype(str(font_path), 21) if font_path.exists() else ImageFont.load_default()
    thumbs = []
    for image in page_images:
        height = round(image.height * width / image.width)
        thumbs.append(image.resize((width, height), Image.Resampling.LANCZOS))
    cell_height = max(image.height for image in thumbs) + caption_height + 15
    sheet = Image.new('RGB', (2*width + 3*margin, 3*cell_height + 4*margin), '#e8edf2')
    draw = ImageDraw.Draw(sheet)
    for number, (record, image) in enumerate(zip(records, thumbs), 1):
        row, col = divmod(number - 1, 2)
        x, y = margin + col*(width + margin), margin + row*(cell_height + margin)
        draw.rectangle((x, y, x + width, y + cell_height), fill='white')
        caption = f"{number}. {record['file']}"
        lines = textwrap.wrap(caption, width=80)
        for index, line in enumerate(lines):
            draw.text((x + 14, y + 9 + index*25), line, font=font, fill='#15202b')
        draw.text((x + 14, y + 9 + len(lines)*25),
                  f"{record['pages']} pages | SHA256 {record['sha256'][:20]}...",
                  font=font, fill='#425466')
        sheet.paste(image, (x, y + caption_height))
    contact_sheet = target / 'first_page_identity_contact_sheet.png'
    sheet.save(contact_sheet)
    records_out = {'contact_sheet': contact_sheet.relative_to(root).as_posix(),
                   'sources': records,
                   'note': 'Render/hash verification only; no automatic visual identity assertion.'}
    (target / 'render_hashes.json').write_text(
        json.dumps(records_out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(records_out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
