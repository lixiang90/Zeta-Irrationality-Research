"""Read-only file provenance audit. Never import or execute research producers.

This checks saved files, PDF metadata and links; it does not prove mathematics.
The 20261006 delivery snapshot remains unchanged.
"""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone
import fitz

ROOT = Path(__file__).resolve().parents[1]
PRIOR = ROOT / 'research/cdt_odd_delivery_20261006.json'
RECEIPT = ROOT / 'literature/manifest_cdt_odd_paired_coupled_cross_source_root_20261007.json'
MAIN = ROOT / 'research/cdt_odd_background_progress_20261006.md'
OUT = ROOT / 'research/cdt_odd_delivery_20261007.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def path_for(name):
    path = (ROOT / name).resolve()
    assert path.is_relative_to(ROOT) and path.is_file(), name
    return path


def check(item, prefix=''):
    name = prefix + item['file']
    path = path_for(name)
    assert digest(path) == item['sha256'], name
    return {'file': name, 'sha256': item['sha256'], 'unchanged': True}


assert digest(PRIOR) == '8963ba9b895508a2fed9438d3011175b556bf6fc4d1b3dacf3b75a314b58b603'
prior = json.loads(PRIOR.read_text(encoding='utf-8'))
receipt = json.loads(RECEIPT.read_text(encoding='utf-8'))
assert receipt['state'] == 'FINAL_AFTER_ACTUAL_REVIEW_READS'
old = []
for key in ['earlier_frozen_files_checked', 'current_frozen_inputs_checked']:
    old.extend(check(item, 'research/') for item in prior[key])
assert len(old) == len({item['file'] for item in old}) == 504
previous_receipts = [check(item) for item in prior['current_round_new_source_receipt_pins']]
new = [check(item) for item in receipt['new_frozen_records']]
assert len(new) == len({item['file'] for item in new}) == 14
assert not set(item['file'] for item in new) & set(item['file'] for item in old)
new_guards = [item for item in new if item['file'].endswith('guard.json')]
assert len(new_guards) == 2
final_receipts = [check(item) for item in receipt['peer_final_receipts']]
final_receipts.append({'file': str(RECEIPT.relative_to(ROOT)).replace('\\', '/'),
                       'sha256': digest(RECEIPT), 'unchanged': True})

# Parsing a saved certificate is data inspection, not execution of its source.
certificates = []
for item in receipt['new_successful_certificates']:
    source = path_for(item['source'])
    result_path = path_for(item['result'])
    guard_path = path_for(item['guard'])
    result = json.loads(result_path.read_text(encoding='utf-8'))
    guard = json.loads(guard_path.read_text(encoding='utf-8'))
    if item['kind'] == 'source_radical':
        assert result['status'] == 'PASS' and result['first_only'] is True
        assert result['checks'] == 4694
        assert guard['source_sha256'] == digest(source)
    else:
        assert result['state'] == 'PASS_FIRST1'
        assert result['producer_sha256'] == digest(source)
        assert len(result['strict_positive_comparisons']) == 8
        assert guard['rerun_forbidden'] is True
    assert guard['state'] == 'STARTED_FIRST1'
    certificates.append({**item, 'saved_state_checked': True})

pdfs = []
for item in prior['original_source_pdfs'] + receipt['new_primary_pdfs']:
    checked = check(item)
    with fitz.open(path_for(item['file'])) as document:
        assert len(document) == item['pages'], item['file']
    pdfs.append({**item, **checked})
assert len(pdfs) == 110
assert sum(item['pages'] for item in pdfs) == 5538
unique_pdf_pages = {item['sha256']: item['pages'] for item in pdfs}
assert len(unique_pdf_pages) == 109
assert sum(unique_pdf_pages.values()) == 5459
other_sources = []
for key in ['original_source_html_snapshots', 'original_source_code_snapshots']:
    other_sources.extend(check(item) for item in prior[key])
drafts = [check(item, 'literature/') for item in prior['unverified_external_draft_snapshots']]

report_files = ['research/' + item['report'] for item in prior['reports']]
proof_files = ['research/' + item['file'] for item in prior['new_proof_and_review_files']]
new_markdown = [item['file'] for item in new if item['file'].endswith('.md')]
report_files.extend(item['report'] for item in receipt['new_successful_certificates'])
proof_files.extend(new_markdown)
# Keep the historical audit's counting convention: report/proof lists may overlap.
links = 0
for name in ['research/' + prior['main_report']] + proof_files[1:] + report_files:
    path = path_for(name)
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)',
                             path.read_text(encoding='utf-8')):
        if ':' in target or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        if Path(target).suffix.lower() not in {'.md', '.pdf', '.py', '.json', '.tex', '.png', '.html'}:
            continue
        resolved = (path.parent / target).resolve()
        # This invocation creates its own output after all other checks pass.
        assert resolved.is_file() or resolved == OUT, (name, target)
        links += 1

output = {
    'status': 'file_provenance_checks_passed',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'File hashes, saved certificate metadata, PDF page counts and local links only; no mathematical producers imported or executed.',
    'metadata_audit_history': 'Initial metadata-only invocation stopped on a wrong research/ prefix for an unchanged historical literature/ draft. Corrected the auditor path only; no research producer or frozen input was modified or rerun.',
    'prior_delivery': {'file': str(PRIOR.relative_to(ROOT)).replace('\\', '/'), 'sha256': digest(PRIOR)},
    'main_report': str(MAIN.relative_to(ROOT)).replace('\\', '/'),
    'main_report_sha256': digest(MAIN),
    'previous_frozen_records_checked': old,
    'new_frozen_records_checked': new,
    'total_frozen_records': len(old) + len(new),
    'total_frozen_mathematical_files': 515,
    'total_frozen_guards': 3,
    'previous_final_receipts_checked': previous_receipts,
    'current_final_receipts_checked': final_receipts,
    'new_saved_certificates_checked': certificates,
    'technical_report_sets': len(report_files),
    'proof_and_review_entries': len(proof_files),
    'original_source_pdfs': pdfs,
    'original_pdf_pages': sum(item['pages'] for item in pdfs),
    'original_unique_pdf_content_count': len(unique_pdf_pages),
    'original_unique_pdf_content_pages': sum(unique_pdf_pages.values()),
    'other_primary_sources_checked': other_sources,
    'unverified_drafts_hash_checked': drafts,
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
    'status', 'total_frozen_records', 'technical_report_sets',
    'proof_and_review_entries', 'original_pdf_pages',
    'original_unique_pdf_content_count', 'original_unique_pdf_content_pages',
    'local_links_checked', 'new_numerical_irrationality_theorem']}, ensure_ascii=False))
