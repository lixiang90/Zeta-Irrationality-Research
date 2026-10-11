"""Delivery integrity audit for the fixed 2026-10-05 log-moment research."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader
from odd_zeta_next_routes_delivery_20261004 import local_links

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/"research"
LIBRARY=ROOT/"literature"
OUTPUT=Path(__file__).with_suffix(".json")
STEMS={
    "odd_zeta_log_saddle_20261005":"saddle_input_certificates_passed",
    "odd_zeta_log_nonzero_20261005":"passed",
    "odd_zeta_uniform_endpoint_nonzero_20261005":"passed",
    "odd_zeta_log_arithmetic_20261005":"fixed_exact_arithmetic_certificates_passed",
    "odd_zeta_log_structure_20261005":"fixed_exact_structure_certificates_passed",
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def readjson(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def main():
    reports=[]
    for stem,status in STEMS.items():
        files={ext:RESEARCH/(stem+ext) for ext in (".md","_verify.py","_verify.json")}
        assert all(p.is_file() for p in files.values()),stem
        cert=readjson(files["_verify.json"])
        assert cert["status"]==status,(stem,cert["status"])
        for field in ("written_proof_sha256","report_sha256"):
            if field in cert:
                assert cert[field]==sha(files[".md"]),stem
        if "script_sha256" in cert:
            assert cert["script_sha256"]==sha(files["_verify.py"]),stem
        for name,value in cert.get("checks",{}).items():
            assert value is True,(stem,name)
        reports.append({
            "report":files[".md"].name,"report_sha256":sha(files[".md"]),
            "script":files["_verify.py"].name,"script_sha256":sha(files["_verify.py"]),
            "certificate":files["_verify.json"].name,"certificate_sha256":sha(files["_verify.json"]),
            "certificate_status":status,
        })

    previous=readjson(RESEARCH/"odd_zeta_explicit_relative_delivery_20261004.json")
    frozen={r["file"]:r["sha256"] for r in previous["frozen_previous_reports"]}
    frozen.update({r["report"]:r["report_sha256"] for r in previous["reports"]})
    frozen[previous["main_report"]]=previous["main_report_sha256"]
    frozen[previous["written_review"]]=previous["written_review_sha256"]
    frozen_checks=[]
    for name,expected in sorted(frozen.items()):
        assert sha(RESEARCH/name)==expected,name
        frozen_checks.append({"file":name,"sha256":expected,"unchanged":True})
    for record in previous["reports"]:
        for field in ("script","certificate"):
            assert sha(RESEARCH/record[field])==record[field+"_sha256"],record[field]

    old_pdfs=set()
    for name in (
        "manifest_global_20261004.json","manifest_bridge_20261004.json",
        "manifest_next_route_20261004.json","manifest_k2_gap_20261004.json",
        "manifest_explicit_relative_20261004.json",
    ):
        for record in readjson(LIBRARY/name)["sources"]:
            if "sha256" not in record:
                continue
            assert sha(LIBRARY/record["file"])==record["sha256"],(name,record["file"])
            old_pdfs.add(record["file"])

    new_sources=readjson(LIBRARY/"manifest_log_moment_20261005.json")["sources"]
    assert len(new_sources)==6 and len({r["file"] for r in new_sources})==6
    original_records=[]
    for r in new_sources:
        path=LIBRARY/r["file"]
        assert b"%PDF-" in path.read_bytes()[:1024],path
        assert sha(path)==r["sha256"],path
        reader=PdfReader(path)
        if reader.is_encrypted:
            assert reader.decrypt(""),path
        assert len(reader.pages)==r["pages"],path
        assert r.get("first_page_identity_visually_checked"),path
        assert (ROOT/r["visual_identity_contact_sheet"]).is_file(),path
        assert r["source_pdf_url"] in r["pdf_urls"],path
        original_records.append({
            "file":path.name,"pages":r["pages"],"sha256":r["sha256"],
            "fixed_version":r["version"],"original_bytes_preserved":True,
            "first_page_identity_visually_checked":True,
        })
    assert sum(r["pages"] for r in original_records)==191

    review=RESEARCH/"odd_zeta_log_moment_review_20261005.md"
    review_text=review.read_text(encoding="utf-8-sig")
    for record in reports:
        assert record["report_sha256"] in review_text,record["report"]
    main_report=RESEARCH/"odd_zeta_log_moment_progress_20261005.md"
    result={
        "status":"delivery_checks_passed","as_of":"2026-10-05",
        "checked_at_utc":datetime.now(timezone.utc).isoformat(),
        "main_report":main_report.name,"main_report_sha256":sha(main_report),
        "new_irrationality_theorem":False,"new_lean_formalization":False,
        "parameter_scans":False,"reports":reports,
        "independent_reviews":{
            "saddle":"paper_mechanism sections1-5 plus algebraic Lambda and conditional budget; distribution1-5",
            "nonzero":"root full; distribution4-5 and source matching",
            "uniform_nonzero":"root and moment_extension full",
            "arithmetic":"root1-6; distribution3-6 plus independent height; paper_mechanism1-6 and exact kappas",
            "structure":"root and moment_extension mathematics2-4; external source matching by author",
            "main_report":"root and zeta7_distribution_new",
        },
        "written_review":review.name,"written_review_sha256":sha(review),
        "frozen_previous_reports":frozen_checks,
        "earlier_original_pdf_hash_checks":len(old_pdfs),
        "new_original_source_pdfs":original_records,"new_original_pdf_pages":191,
        "scope":(
            "The raw q7 endpoint has proved oscillatory strong asymptotics and positive limsup; "
            "adjacent two-term blocks contain an exponentially large nonzero term. "
            "Prime-filter arguments give eventual nonzero on specified infinite subsequences for fixed "
            "zeta weights and Catalan without assuming irrationality. Actual target height, local Lucas "
            "factors and full gcd formulas are proved. The bound on weighted exceptional primes "
            "needed for the primitive no-go criterion is unproved. Raw growth and safe-LCM failure "
            "are not unconditional primitive failure. Finite certificates, hashes and visual checks "
            "do not replace the all-scale written analytic and arithmetic proofs."
        ),
        "local_links_checked":0,"missing_links":[],
    }
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    docs=[RESEARCH/(stem+".md") for stem in STEMS]
    docs += [main_report,review,ROOT/"README.md",LIBRARY/"README.md",LIBRARY/"log_moment_reading_map_20261005.md"]
    missing=[];count=0
    for doc in docs:
        for target,path in local_links(doc):
            count+=1
            if not path.exists():
                missing.append({"document":str(doc.relative_to(ROOT)),"target":target})
    result["local_links_checked"]=count
    result["missing_links"]=missing
    result["status"]="delivery_checks_passed" if not missing else "missing_links"
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    assert not missing,missing
    print(json.dumps({
        "status":result["status"],"reports":len(reports),"new_original_pdfs":len(original_records),
        "new_original_pdf_pages":191,"frozen_reports":len(frozen_checks),
        "earlier_original_pdfs":len(old_pdfs),"local_links":count,
        "new_irrationality_theorem":False,"new_lean_formalization":False,
    },ensure_ascii=False))
if __name__=="__main__":
    main()

