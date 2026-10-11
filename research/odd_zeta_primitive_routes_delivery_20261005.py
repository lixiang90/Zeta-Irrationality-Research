"""Delivery/hash audit for the primitive-budget and Markov-interface research."""
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
 "odd_zeta_log_primitive_20261005":("fixed_exact_primitive_jet_certificates_passed","2fd4bfd843db5a12bfa32c4fce2de003e58d3b37f2ea258ef15f89dc9abc4a0c"),
 "odd_zeta_exceptional_primes_20261005":("passed","c539cc35792769f141deca440c5d47a65e745037358c6b7688cdc03e73a54157"),
 "odd_zeta_fixed_shift_filters_20261005":("fixed_exact_filter_certificates_passed","70c958736db4607eba9a4c164d4b71a80abc235006009a64028203deec6d5f99"),
 "odd_zeta_mixed_pade_20261005":("fixed_exact_mixed_pade_certificates_passed","d2ca842d8d4a7be71f9faf76d1721136ce110c779546af0fdd27c54c8d3c71d7"),
}
def sha(path):
 return hashlib.sha256(path.read_bytes()).hexdigest()
def readjson(path):
 return json.loads(path.read_text(encoding="utf-8-sig"))

def main():
 reports=[]
 for stem,(status,expected) in STEMS.items():
  doc=RESEARCH/(stem+".md"); script=RESEARCH/(stem+"_verify.py"); certpath=RESEARCH/(stem+"_verify.json")
  cert=readjson(certpath)
  assert sha(doc)==expected,doc
  assert cert["status"]==status,stem
  if "report_sha256" in cert: assert cert["report_sha256"]==sha(doc),stem
  if "script_sha256" in cert: assert cert["script_sha256"]==sha(script),stem
  for item in cert.get("checks",[]):
   assert item["passed"] is True,(stem,item)
  reports.append({"report":doc.name,"report_sha256":sha(doc),
                 "script":script.name,"script_sha256":sha(script),
                 "certificate":certpath.name,"certificate_sha256":sha(certpath),
                 "certificate_status":status})
 main_report=RESEARCH/"odd_zeta_primitive_routes_progress_20261005.md"
 controlscript=RESEARCH/"odd_zeta_markov_rational_control_20261005_verify.py"
 controlpath=controlscript.with_suffix(".json")
 control=readjson(controlpath)
 assert control["status"]=="fixed_exact_rational_control_passed"
 assert control["report_sha256"]==sha(main_report)
 assert control["script_sha256"]==sha(controlscript)

 previous=readjson(RESEARCH/"odd_zeta_log_moment_delivery_20261005.json")
 frozen={r["file"]:r["sha256"] for r in previous["frozen_previous_reports"]}
 frozen.update({r["report"]:r["report_sha256"] for r in previous["reports"]})
 frozen[previous["main_report"]]=previous["main_report_sha256"]
 frozen[previous["written_review"]]=previous["written_review_sha256"]
 frozen_records=[]
 for name,expected in sorted(frozen.items()):
  assert sha(RESEARCH/name)==expected,name
  frozen_records.append({"file":name,"sha256":expected,"unchanged":True})
 frozen_aux=[]
 for prevname in ("odd_zeta_log_moment_delivery_20261005.json","odd_zeta_explicit_relative_delivery_20261004.json"):
  prev=readjson(RESEARCH/prevname)
  for item in prev["reports"]:
   for field in ("script","certificate"):
    path=RESEARCH/item[field]
    assert sha(path)==item[field+"_sha256"],path
    frozen_aux.append({"file":path.name,"sha256":sha(path),"unchanged":True})

 old_pdfs={}
 for manifest in ("manifest_global_20261004.json","manifest_bridge_20261004.json",
                  "manifest_next_route_20261004.json","manifest_k2_gap_20261004.json",
                  "manifest_explicit_relative_20261004.json","manifest_log_moment_20261005.json"):
  for r in readjson(LIBRARY/manifest)["sources"]:
   if "sha256" in r:
    assert sha(LIBRARY/r["file"])==r["sha256"],r["file"]
    old_pdfs[r["file"]]=r["sha256"]
 assert len(old_pdfs)==59,len(old_pdfs)
 records=[]
 new=readjson(LIBRARY/"manifest_primitive_routes_20261005.json")["sources"]
 assert len(new)==5
 for r in new:
  p=LIBRARY/r["file"]
  assert r["archive_status"] in ("downloaded","existing_preserved")
  assert p.read_bytes().startswith(b"%PDF-")
  assert sha(p)==r["sha256"] and p.stat().st_size==r["bytes"],p
  pdf=PdfReader(p)
  if pdf.is_encrypted: assert pdf.decrypt("")
  assert len(pdf.pages)==r["pages"],p
  assert r["first_page_identity_visually_checked"] is True,p
  assert (ROOT/r["visual_identity_contact_sheet"]).is_file(),p
  assert r["source_pdf_url"] in r["pdf_urls"],p
  records.append({"file":p.name,"pages":r["pages"],"sha256":r["sha256"],"version":r["version"],
                  "original_bytes_preserved":True,"first_page_identity_visually_checked":True})
 assert sum(r["pages"] for r in records)==97
 history=next(r for r in new if r["file"].startswith("ghosh_ward"))
 assert history["later_withdrawal"]["theorems_adopted"] is False
 assert history["later_withdrawal"]["no_pdf_in_v4"] is True
 webs=readjson(LIBRARY/"manifest_primitive_routes_web_20261005.json")["sources"]
 assert len(webs)==3
 for r in webs:
  p=LIBRARY/r["file"]
  assert sha(p)==r["sha256"] and p.stat().st_size==r["bytes"],p
  assert r["identity_token"].lower() in p.read_text(encoding="utf-8").lower()
 withdrawal=(LIBRARY/"ghosh_ward_arxiv_v4_metadata_20261005.html").read_text(encoding="utf-8")
 assert "Errors in paper uncorrected" in withdrawal
 assert "No PDF available" in withdrawal

 review=RESEARCH/"odd_zeta_primitive_routes_review_20261005.md"
 rt=review.read_text(encoding="utf-8")
 for r in reports: assert r["report_sha256"] in rt,r["report"]
 result={
  "status":"delivery_checks_passed","as_of":"2026-10-05",
  "checked_at_utc":datetime.now(timezone.utc).isoformat(),
  "main_report":main_report.name,"main_report_sha256":sha(main_report),
  "reports":reports,"written_review":review.name,"written_review_sha256":sha(review),
  "rational_control":{"script":controlscript.name,"script_sha256":sha(controlscript),
                      "certificate":controlpath.name,"certificate_sha256":sha(controlpath)},
  "new_irrationality_theorem":False,"new_lean_formalization":False,"parameter_scans":False,
  "new_verifier_scripts_executed_successfully":5,
  "frozen_previous_reports":frozen_records,"frozen_previous_scripts_and_certificates":frozen_aux,
  "earlier_original_pdf_hash_checks":len(old_pdfs),
  "new_original_source_pdfs":records,"new_original_pdf_pages":97,
  "new_original_web_sources":webs,
  "withdrawn_source_theorems_adopted":False,
  "scope":"True root-denominator costs and a second p-adic jet are proved; weighted residual layer losses remain unbounded. A three-row true-denominator exponential lower bound is unconditional but insufficient for the primitive net budget. Fixed rational filters and a specified endpoint type-I family do not change the relevant raw/normalized exponential advantage. Single positive rational-moment measures give common strictly positive Markov errors and a verified bare exponential rate for fixed odd zeta values, Catalan and the specified positive combination; the complete integer coefficient budget is unproved. A rational-target control input proves that positivity and rational moments alone cannot close a universal below-threshold arithmetic bound. Finite certificates do not replace the written all-scale proofs.",
  "local_links_checked":0,"missing_links":[],
 }
 OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 docs=[RESEARCH/(stem+".md") for stem in STEMS]
 docs += [main_report,review,ROOT/"README.md",LIBRARY/"README.md",LIBRARY/"primitive_routes_reading_map_20261005.md"]
 missing=[];count=0
 for doc in docs:
  for target,path in local_links(doc):
   count+=1
   if not path.exists(): missing.append({"document":str(doc.relative_to(ROOT)),"target":target})
 result["local_links_checked"]=count;result["missing_links"]=missing
 result["status"]="delivery_checks_passed" if not missing else "missing_links"
 OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 assert not missing,missing
 print(json.dumps({"status":result["status"],"reports":len(reports),"new_original_pdfs":len(records),
                   "new_original_pdf_pages":97,"new_original_html":len(webs),"frozen_reports":len(frozen_records),
                   "earlier_original_pdfs":len(old_pdfs),"local_links":count,
                   "new_irrationality_theorem":False,"new_lean_formalization":False},ensure_ascii=False))
if __name__=="__main__":
 main()

