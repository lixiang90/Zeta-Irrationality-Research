"""Metadata-only delivery audit: never execute/import mathematical producers.

Preserve both older delivery JSON snapshots. This checks file provenance, saved
certificate metadata, primary PDF page counts and Markdown local links only.
"""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone
import fitz

ROOT = Path(__file__).resolve().parents[1]
PRIOR = ROOT / 'research/cdt_odd_delivery_20261007.json'
RECEIPT = ROOT / 'literature/manifest_cdt_odd_paired_multiroot_masked_pencil_root_20261007.json'
MAIN = ROOT / 'research/cdt_odd_background_progress_20261006.md'
OUT = Path(__file__).with_suffix('.json')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_for(name):
    path = (ROOT / name).resolve()
    assert path.is_relative_to(ROOT) and path.is_file(), name
    return path


def check(item):
    path = path_for(item['file'])
    assert digest(path) == item['sha256'], item['file']
    return {**item, 'unchanged': True}


assert digest(PRIOR) == '9bd4942563a5ce123ea914f727b2de8bfcb336ab084a96a9cc932ac83ddc0e51'
prior = json.loads(PRIOR.read_text(encoding='utf-8'))
receipt = json.loads(RECEIPT.read_text(encoding='utf-8'))
assert receipt['state'] == 'FINAL_AFTER_ACTUAL_REVIEW_READS'
old = [check(item) for key in ['previous_frozen_records_checked', 'new_frozen_records_checked']
       for item in prior[key]]
assert len(old) == len({item['file'] for item in old}) == 518
new = [check(item) for item in receipt['new_frozen_records']]
assert len(new) == len({item['file'] for item in new}) == 11
assert not {item['file'] for item in old} & {item['file'] for item in new}
all_frozen = old + new
guards = [item for item in all_frozen if item['file'].endswith('guard.json')]
assert len(guards) == 4

previous_receipts = [check(item) for key in ['previous_final_receipts_checked', 'current_final_receipts_checked']
                     for item in prior[key]]
final_receipts = [check(item) for item in receipt['peer_final_receipts']]
final_receipts.append({'file': str(RECEIPT.relative_to(ROOT)).replace('\\', '/'),
                       'sha256': digest(RECEIPT), 'unchanged': True})

certificates = []
for item in receipt['new_successful_certificates']:
    source = path_for(item['source'])
    result = json.loads(path_for(item['result']).read_text(encoding='utf-8'))
    guard = json.loads(path_for(item['guard']).read_text(encoding='utf-8'))
    assert result['state'] == 'PASS_FIRST1' and result['assertion_count'] == 7
    assert result['source_sha256'] == guard['source_sha256'] == digest(source)
    assert guard['state'] == 'STARTED_FIRST1'
    assert result['s_fixed'] == '4/7'
    certificates.append({**item, 'saved_state_checked': True})
assert len(certificates) == 1

pdfs = []
for item in prior['original_source_pdfs'] + receipt['new_primary_pdfs']:
    checked = check(item)
    with fitz.open(path_for(item['file'])) as document:
        assert len(document) == item['pages'], item['file']
    pdfs.append({**item, **checked})
unique_pdf_pages = {item['sha256']: item['pages'] for item in pdfs}
other_sources = [check(item) for item in prior['other_primary_sources_checked']]
drafts = [check(item) for item in prior['unverified_drafts_hash_checked']]

# Current scope: every unique frozen Markdown file plus the mutable main.
# This is broader than the prior auditor's report/proof list; counts are not
# evidence of mathematical proof and are not compared as deleted/added links.
markdown = {item['file'] for item in all_frozen if item['file'].endswith('.md')}
markdown.add(str(MAIN.relative_to(ROOT)).replace('\\', '/'))
links = 0
for name in sorted(markdown):
    path = path_for(name)
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', path.read_text(encoding='utf-8')):
        if ':' in target or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        if Path(target).suffix.lower() not in {'.md', '.pdf', '.py', '.json', '.tex', '.png', '.html'}:
            continue
        resolved = (path.parent / target).resolve()
        assert resolved.is_file() or resolved == OUT, (name, target)
        links += 1

output = {
    'status': 'file_provenance_checks_passed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Hashes, saved certificate metadata, PDF page counts and local links only; no mathematical producers imported or executed.',
    'prior_delivery': {'file': str(PRIOR.relative_to(ROOT)).replace('\\', '/'), 'sha256': digest(PRIOR)},
    'main_report': str(MAIN.relative_to(ROOT)).replace('\\', '/'),
    'main_report_sha256': digest(MAIN),
    'previous_frozen_records_checked': old,
    'new_frozen_records_checked': new,
    'total_frozen_records': len(all_frozen),
    'total_frozen_mathematical_files': len(all_frozen) - len(guards),
    'total_frozen_guards': len(guards),
    'previous_final_receipts_checked': previous_receipts,
    'current_final_receipts_checked': final_receipts,
    'new_saved_certificates_checked': certificates,
    'technical_report_sets': prior['technical_report_sets'] + len(certificates),
    'proof_and_review_entries': prior['proof_and_review_entries'] + sum(item['file'].endswith('.md') for item in new),
    'original_source_pdfs': pdfs,
    'original_pdf_pages': sum(item['pages'] for item in pdfs),
    'original_unique_pdf_content_count': len(unique_pdf_pages),
    'original_unique_pdf_content_pages': sum(unique_pdf_pages.values()),
    'other_primary_sources_checked': other_sources,
    'unverified_drafts_hash_checked': drafts,
    'local_link_scan_scope': 'All unique frozen Markdown files plus current mutable main.',
    'markdown_files_link_checked': len(markdown),
    'local_links_checked': links,
    'actual_reading_scope': receipt['actual_reading_scope'],
    'mathematical_execution_history': receipt['mathematical_execution_history'],
    'current_progress': receipt['current_progress'],
    'new_numerical_irrationality_theorem': False,
    'new_lean_formalization': False,
    'goal_status': 'active',
}
OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({key: output[key] for key in [
    'status', 'total_frozen_records', 'total_frozen_mathematical_files', 'total_frozen_guards',
    'technical_report_sets', 'proof_and_review_entries', 'original_pdf_pages',
    'original_unique_pdf_content_count', 'original_unique_pdf_content_pages',
    'local_links_checked', 'new_numerical_irrationality_theorem']}, ensure_ascii=False))
