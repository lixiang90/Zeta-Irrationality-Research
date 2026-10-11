"""Delivery audit for the fixed K2 gap investigation; no mathematical theorem is inferred from hashes."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from pypdf import PdfReader
from odd_zeta_next_routes_delivery_20261004 import local_links, FROZEN

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'
LIBRARY = ROOT / 'literature'
OUTPUT = Path(__file__).with_suffix('.json')
STEMS = {
    'odd_zeta_k2_descent_20261004': 'exact_function_field_inputs_passed',
    'odd_zeta_k2_vertical_20261004': 'all fixed exact identities passed',
    'odd_zeta_k2_regulator_20261004': 'fixed_exact_algebra_passed_no_period_numerics',
    'odd_zeta_bloch_boundary_20261004': 'passed',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def readjson(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def main():
    records = []
    for stem, expected in STEMS.items():
        files = {suffix: RESEARCH/(stem+suffix) for suffix in ['.md','_verify.py','_verify.json']}
        assert all(p.is_file() for p in files.values()), stem
        cert = readjson(files['_verify.json'])
        assert cert['status'] == expected, (stem,cert.get('status'))
        if 'written_proof_sha256' in cert:
            assert cert['written_proof_sha256'] == sha(files['.md'])
        for name,check in cert.get('checks',{}).items():
            assert check['passed'], (stem,name)
        records.append({'report':files['.md'].name,'report_sha256':sha(files['.md']),
                        'script':files['_verify.py'].name,'script_sha256':sha(files['_verify.py']),
                        'certificate':files['_verify.json'].name,'certificate_sha256':sha(files['_verify.json']),
                        'certificate_status':cert['status']})
    previous = readjson(RESEARCH/'odd_zeta_next_routes_delivery_20261004.json')
    frozen = dict(FROZEN)
    frozen.update({r['report']:r['report_sha256'] for r in previous['reports']})
    frozen[previous['main_report']] = previous['main_report_sha256']
    frozen_checks = []
    for name,expected in sorted(frozen.items()):
        actual = sha(RESEARCH/name)
        assert actual == expected, (name,actual,expected)
        frozen_checks.append({'file':name,'sha256':actual,'unchanged':True})

    # Check all earlier archived originals against the recorded immutable digests.
    old_pdfs = []
    for name in ['manifest_global_20261004.json','manifest_bridge_20261004.json','manifest_next_route_20261004.json']:
        for r in readjson(LIBRARY/name)['sources']:
            if 'sha256' not in r:  # no local PDF was claimed for failed records
                continue
            p=LIBRARY/r['file']
            assert sha(p)==r['sha256'], (name,r['file'])
            old_pdfs.append(r['file'])
    manifest = readjson(LIBRARY/'manifest_k2_gap_20261004.json')
    sources = manifest['sources']
    assert len(sources)==8 and len({r['file'] for r in sources})==8
    originals = []
    for r in sources:
        p=LIBRARY/r['file']
        assert b'%PDF-' in p.read_bytes()[:1024], p
        assert sha(p)==r['sha256'], p
        reader = PdfReader(p)
        if reader.is_encrypted:
            assert reader.decrypt(''), p
        assert len(reader.pages)==r['pages'], p
        assert r.get('first_page_identity_visually_checked'), p
        assert (ROOT/r['visual_identity_contact_sheet']).is_file()
        assert r['archive_status'] in ('downloaded','existing_preserved')
        assert r.get('source_pdf_url') in r['pdf_urls'], p
        originals.append({'file':r['file'],'pages':r['pages'],'sha256':r['sha256'],
                          'fixed_version':r['version'],'original_bytes_preserved':True,
                          'visual_identity_checked':True})
    review=RESEARCH/'odd_zeta_bloch_boundary_20261004_review.md'
    assert review.is_file()
    assert sha(RESEARCH/'odd_zeta_bloch_boundary_20261004.md') in review.read_text(encoding='utf-8')
    main_doc=RESEARCH/'odd_zeta_k2_gap_progress_20261004.md'
    result = {
        'status':'delivery_checks_passed','as_of':'2026-10-04',
        'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'main_report':main_doc.name,'main_report_sha256':sha(main_doc),
        'new_irrationality_theorem':False,'new_lean_formalization':False,'parameter_scans':False,
        'reports':records,
        'independent_reviews':{
            'descent':'root and zeta7_moment_extension',
            'vertical':'root and paper_mechanism',
            'regulator':'root and paper_mechanism',
            'bloch_boundary':'paper_mechanism and zeta7_distribution_new'
        },
        'written_review':review.name,'written_review_sha256':sha(review),
        'frozen_previous_reports':frozen_checks,
        'earlier_original_pdf_hash_checks':len(set(old_pdfs)),
        'new_original_source_pdfs':originals,
        'local_links_checked':0,'missing_links':[],
        'scope':'Finite exact certificates check algebraic inputs. Transfer, local boundary lemma, '
                'arithmetic-surface resolution and full Borel regulator injectivity rely on written '
                'proofs and primary sources. The Bloch identity is rational; no integral T=0 or irrationality claim.'
    }
    # The output itself is linked, so create it before resolving references.
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    docs=[RESEARCH/(stem+'.md') for stem in STEMS]
    docs += [main_doc,review,ROOT/'README.md',LIBRARY/'README.md',LIBRARY/'k2_gap_reading_map_20261004.md']
    missing=[];count=0
    for doc in docs:
        for target,path in local_links(doc):
            count+=1
            if not path.exists():
                missing.append({'document':str(doc.relative_to(ROOT)),'target':target})
    result['local_links_checked']=count
    result['missing_links']=missing
    result['status']='delivery_checks_passed' if not missing else 'missing_links'
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    assert not missing, missing
    print(json.dumps({'status':result['status'],'reports':len(records),'new_original_pdfs':len(originals),
                      'frozen_reports':len(frozen_checks),'earlier_original_pdfs':len(set(old_pdfs)),
                      'local_links':count,'new_irrationality_theorem':False,'new_lean_formalization':False},
                     ensure_ascii=False))

if __name__=='__main__':
    main()

