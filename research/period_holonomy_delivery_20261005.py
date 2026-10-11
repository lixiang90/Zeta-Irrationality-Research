"""Hash, source and scope audit for the period/integral-model research delivery."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from pypdf import PdfReader
from odd_zeta_next_routes_delivery_20261004 import local_links

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/"research";L=ROOT/"literature";OUTPUT=Path(__file__).with_suffix(".json")
EXPECTED={
"period_holonomy_cdt_mechanism_20261005":(
"27483fbfe9d54e0e2bbe982d6959da4586bd9e7490bbb2b64c5c6301e3478299",
"6e843b7345894f275c86eea4b7a564f6a4c27d6eeeef0b94ce6eb2f07febb202",
"533eefce36378ec8d1d430b325c45b9fb095abb2f63715b3c806828f24838159"),
"period_holonomy_target_projection_20261005":(
"36281c471fc0c4013b943222f1e8ab9f8a736e6c69fa63ab87422f120ffc5837",
"ff3b6d55551851315f7fb585ebf1ea44b414e86f0cb7c6b2cd8d75d0befaaa25",
"21b105fa5a174c27995107b96a4bf9b6d17b24fe63d8e93cef67d100a832653e"),
"period_holonomy_integral_models_20261005":(
"b8d4199f6a3b1b97d59481a87157be85652a431b00d444ba04600797b0a9ab1d",
"2e0930fc6206de551086f2199de6bc3fd46a0c726a38560c4889d789b1fa6732",
"c23e725bb9a71f7069a2ad3569ac9c84174bf209bd299475fb120eb79b7b4c11"),
"period_holonomy_dilog_model_20261005":(
"970191f95813c6f14ce45da71b1af2070fdfa000f28168a7d8ff89fa3b34d9be",
"12dd5bfce59114fa37fb860c353b0bd0b82f98d50a51f57521c0fbb4ff1a49e2",
"f593a1988f8947240dc3a7a16f44310c1105f573ef401df3d14d568528fb7e92"),
}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def main():
    reports=[]
    for stem,hashes in EXPECTED.items():
        paths=[R/(stem+suffix) for suffix in [".md","_verify.py","_verify.json"]]
        for p,h in zip(paths,hashes):assert sha(p)==h,p.name
        cert=read(paths[2])
        if "report_sha256" in cert:assert cert["report_sha256"]==hashes[0]
        if "script_sha256" in cert:assert cert["script_sha256"]==hashes[1]
        for c in cert.get("checks",[]):
            if isinstance(c,dict) and "passed" in c:assert c["passed"] is True
        if stem.endswith("cdt_mechanism_20261005"):
            assert cert["status"]=="passed" and cert["number_of_checks"]==120
            assert cert["source_sha256"]==sha(L/"cdt2024_l2_chi_minus3.pdf")
            status="passed"
        elif stem.endswith("target_projection_20261005"):
            assert cert["checks_passed"] is True and cert["smith_invariant_factors"]==[1,18]
            status="exact_assertions_passed"
        elif stem.endswith("integral_models_20261005"):
            assert cert["best_natural_type_tau"]=="25/18"
            assert cert["fixed_prefix_diagnostics"]["1"]["denominator"]==3080
            assert cert["fixed_prefix_diagnostics"]["2"]["denominator"]==9486400
            status="exact_assertions_passed"
        else:
            assert cert["status"]=="fixed_exact_dilog_model_certificates_passed" and cert["check_count"]==117
            status=cert["status"]
        reports.append({"report":paths[0].name,"report_sha256":hashes[0],
            "script":paths[1].name,"script_sha256":hashes[1],
            "certificate":paths[2].name,"certificate_sha256":hashes[2],"certificate_status":status})
    main_report=R/"period_holonomy_progress_20261005.md"
    main_script=R/"period_holonomy_progress_20261005_verify.py"
    main_cert_path=main_script.with_suffix(".json");main_cert=read(main_cert_path)
    assert main_cert["report_sha256"]==sha(main_report) and main_cert["script_sha256"]==sha(main_script)
    assert main_cert["status"]=="fixed_exact_log_integral_coordinates_passed"
    assert main_cert["check_count"]==7 and all(c["passed"] for c in main_cert["checks"])
    previous=read(R/"odd_zeta_primitive_routes_delivery_20261005.json")
    frozen={x["file"]:x["sha256"] for x in previous["frozen_previous_reports"]}
    frozen.update({x["report"]:x["report_sha256"] for x in previous["reports"]})
    frozen[previous["main_report"]]=previous["main_report_sha256"]
    frozen[previous["written_review"]]=previous["written_review_sha256"]
    assert len(frozen)==36
    frozen_records=[]
    for name,h in sorted(frozen.items()):
        assert sha(R/name)==h,name
        frozen_records.append({"file":name,"sha256":h,"unchanged":True})
    aux={x["file"]:x["sha256"] for x in previous["frozen_previous_scripts_and_certificates"]}
    for x in previous["reports"]:
        for key in ["script","certificate"]:aux[x[key]]=x[key+"_sha256"]
    for key in ["script","certificate"]:aux[previous["rational_control"][key]]=previous["rational_control"][key+"_sha256"]
    frozen_aux=[]
    for name,h in sorted(aux.items()):
        assert sha(R/name)==h,name
        frozen_aux.append({"file":name,"sha256":h,"unchanged":True})
    old_pdfs={}
    for name in ["manifest_global_20261004.json","manifest_bridge_20261004.json",
                 "manifest_next_route_20261004.json","manifest_k2_gap_20261004.json",
                 "manifest_explicit_relative_20261004.json","manifest_log_moment_20261005.json",
                 "manifest_primitive_routes_20261005.json"]:
        for x in read(L/name)["sources"]:
            if "sha256" in x:
                assert sha(L/x["file"])==x["sha256"],x["file"]
                old_pdfs[x["file"]]=x["sha256"]
    assert len(old_pdfs)==64,len(old_pdfs)
    pdfs=read(L/"manifest_period_holonomy_20261005.json")["sources"]
    assert len(pdfs)==2
    records=[]
    for x in pdfs:
        p=L/x["file"]
        assert p.read_bytes().startswith(b"%PDF-")
        assert sha(p)==x["sha256"] and p.stat().st_size==x["bytes"]
        assert x["archive_status"] in ["downloaded","existing_preserved"]
        assert x["source_pdf_url"] in x["pdf_urls"]
        reader=PdfReader(p)
        if reader.is_encrypted:assert reader.decrypt("")
        assert len(reader.pages)==x["pages"]
        assert x["first_page_identity_visually_checked"] is True
        assert (ROOT/x["visual_identity_contact_sheet"]).is_file()
        records.append({"file":p.name,"pages":x["pages"],"sha256":x["sha256"],"version":x["version"],
                        "original_bytes_preserved":True,"first_page_identity_visually_checked":True})
    assert sum(x["pages"] for x in records)==234
    webs=read(L/"manifest_period_holonomy_web_20261005.json")["sources"]
    assert len(webs)==3
    for x in webs:
        p=L/x["file"]
        assert sha(p)==x["sha256"] and p.stat().st_size==x["bytes"]
        assert x["identity_token"].lower() in p.read_text(encoding="utf-8").lower()
    review=R/"period_holonomy_review_20261005.md";rt=review.read_text(encoding="utf-8")
    for x in reports:assert x["report_sha256"] in rt
    result={
        "status":"delivery_checks_passed","as_of":"2026-10-05","checked_at_utc":datetime.now(timezone.utc).isoformat(),
        "main_report":main_report.name,"main_report_sha256":sha(main_report),"reports":reports,
        "main_integral_classification_certificate":{"script":main_script.name,"script_sha256":sha(main_script),
            "certificate":main_cert_path.name,"certificate_sha256":sha(main_cert_path),"checks":7},
        "written_review":review.name,"written_review_sha256":sha(review),
        "closed_numeric_consequences_from_CDT":True,"new_global_irrationality_theorem":False,
        "new_project_structural_lemmas_proved":True,"new_lean_formalization":False,"parameter_scans":False,
        "new_verifier_scripts_executed_successfully":5,
        "frozen_previous_reports":frozen_records,"frozen_previous_scripts_and_certificates":frozen_aux,
        "earlier_original_pdf_hash_checks":len(old_pdfs),"new_original_source_pdfs":records,
        "new_original_pdf_pages":234,"new_original_web_sources":webs,
        "scope":"Closed CDT consequences for five rational-dilog combinations and all sixth-point trigamma/polynomial-log integrals. Explicit full rank11 source, compatible rank6 integral quotient, all-content denominator exponents and marked bad support. Cyclotomic rank3 integral Betti model, exact prefix preservation but fine-type change, and natural cost25/18. Uniform periodic-polylog actual cyclic ranks and joint arithmetic/domain projection lattice. No new conductor L-value, odd-zeta or Catalan irrationality theorem; rationality-triggered overconvergence and required all-bad-prime log extensions remain unproved for new applications.",
        "local_links_checked":0,"missing_links":[],
    }
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    docs=[R/(stem+".md") for stem in EXPECTED]+[main_report,review,ROOT/"README.md",L/"README.md",L/"period_holonomy_reading_map_20261005.md"]
    count=0;missing=[]
    for doc in docs:
        for target,path in local_links(doc):
            count+=1
            if not path.exists():missing.append({"document":str(doc.relative_to(ROOT)),"target":target})
    result["local_links_checked"]=count;result["missing_links"]=missing
    result["status"]="delivery_checks_passed" if not missing else "missing_links"
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    assert not missing,missing
    print(json.dumps({"status":result["status"],"technical_reports":4,"new_exact_certificates":5,
        "frozen_previous_reports":len(frozen_records),"frozen_auxiliary_files":len(frozen_aux),
        "earlier_original_pdfs":len(old_pdfs),"new_original_pdfs":2,"new_original_pdf_pages":234,
        "new_original_html":3,"local_links":count,"closed_numeric_CDT_consequences":True,
        "new_global_irrationality_theorem":False,"new_lean_formalization":False},ensure_ascii=False))
if __name__=="__main__":main()

