"""Audit the explicit-relative delivery; hashes and finite certificates are not new irrationality proofs."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader
from odd_zeta_next_routes_delivery_20261004 import local_links

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
LIBRARY = ROOT / "literature"
OUTPUT = Path(__file__).with_suffix(".json")
STEMS = {
    "odd_zeta_explicit_steinberg_20261004": "fixed_exact_certificates_passed",
    "odd_zeta_cyclotomic_mellin_20261004": "all fixed exact certificates passed",
    "odd_zeta_relative_family_audit_20261004": "fixed_exact_identities_passed_no_parameter_scan",
    "odd_zeta_log_moment_candidate_20261004": "exact_candidate_inputs_passed",
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def readjson(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def main():
    reports = []
    for stem, expected in STEMS.items():
        paths = {ext: RESEARCH / (stem + ext) for ext in (".md", "_verify.py", "_verify.json")}
        assert all(p.is_file() for p in paths.values()), stem
        certificate = readjson(paths["_verify.json"])
        assert certificate["status"] == expected, (stem, certificate["status"])
        if "written_proof_sha256" in certificate:
            assert certificate["written_proof_sha256"] == sha(paths[".md"]), stem
        for name, flag in certificate.get("checks", {}).items():
            assert flag is True if isinstance(flag, bool) else flag["passed"], (stem, name)
        reports.append({
            "report": paths[".md"].name, "report_sha256": sha(paths[".md"]),
            "script": paths["_verify.py"].name, "script_sha256": sha(paths["_verify.py"]),
            "certificate": paths["_verify.json"].name,
            "certificate_sha256": sha(paths["_verify.json"]), "certificate_status": expected,
        })

    previous = readjson(RESEARCH / "odd_zeta_k2_gap_delivery_20261004.json")
    frozen = {r["file"]: r["sha256"] for r in previous["frozen_previous_reports"]}
    frozen.update({r["report"]: r["report_sha256"] for r in previous["reports"]})
    frozen[previous["main_report"]] = previous["main_report_sha256"]
    frozen[previous["written_review"]] = previous["written_review_sha256"]
    frozen_checks = []
    for name, expected in sorted(frozen.items()):
        assert sha(RESEARCH / name) == expected, name
        frozen_checks.append({"file": name, "sha256": expected, "unchanged": True})
    for record in previous["reports"]:
        for key in ("script", "certificate"):
            assert sha(RESEARCH / record[key]) == record[key + "_sha256"], record[key]

    old_pdf_files = set()
    for name in (
        "manifest_global_20261004.json", "manifest_bridge_20261004.json",
        "manifest_next_route_20261004.json", "manifest_k2_gap_20261004.json",
    ):
        for record in readjson(LIBRARY / name)["sources"]:
            if "sha256" not in record:
                continue
            assert sha(LIBRARY / record["file"]) == record["sha256"], (name, record["file"])
            old_pdf_files.add(record["file"])

    new_sources = readjson(LIBRARY / "manifest_explicit_relative_20261004.json")["sources"]
    assert len(new_sources) == 5 and len({r["file"] for r in new_sources}) == 5
    originals = []
    for record in new_sources:
        pdf = LIBRARY / record["file"]
        assert b"%PDF-" in pdf.read_bytes()[:1024], pdf
        assert sha(pdf) == record["sha256"], pdf
        reader = PdfReader(pdf)
        if reader.is_encrypted:
            assert reader.decrypt(""), pdf
        assert len(reader.pages) == record["pages"], pdf
        assert record.get("first_page_identity_visually_checked"), pdf
        assert (ROOT / record["visual_identity_contact_sheet"]).is_file(), pdf
        assert record["source_pdf_url"] in record["pdf_urls"], pdf
        originals.append({
            "file": pdf.name, "pages": record["pages"], "sha256": record["sha256"],
            "fixed_version": record["version"], "original_bytes_preserved": True,
            "first_page_identity_visually_checked": True,
        })

    review = RESEARCH / "odd_zeta_explicit_relative_review_20261004.md"
    review_text = review.read_text(encoding="utf-8-sig")
    for record in reports:
        assert record["report_sha256"] in review_text, record["report"]
    main_report = RESEARCH / "odd_zeta_explicit_relative_progress_20261004.md"
    result = {
        "status": "delivery_checks_passed", "as_of": "2026-10-04",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "main_report": main_report.name, "main_report_sha256": sha(main_report),
        "new_irrationality_theorem": False, "new_lean_formalization": False,
        "parameter_scans": False, "reports": reports,
        "independent_reviews": {
            "explicit_steinberg": "root; algebra, Steinberg, endpoints, all complex branches",
            "cyclotomic_mellin": "root; paper_mechanism sections 4-6; distribution sections 4-8",
            "relative_family": "root sections 3-7; paper_mechanism sections 3-4",
            "log_moment_candidate": "paper_mechanism and zeta7_distribution_new",
            "main_report": "root and zeta7_distribution_new",
        },
        "written_review": review.name, "written_review_sha256": sha(review),
        "frozen_previous_reports": frozen_checks,
        "earlier_original_pdf_hash_checks": len(old_pdf_files),
        "new_original_source_pdfs": originals,
        "scope": (
            "Integral Milnor T=0 and the rational four-term Bloch identity are fixed identities, "
            "not an irrationality proof. Prime-window/full-gcd no-go results apply only to the "
            "specified unbalanced binomial families. Ordinary Rodrigues has proved nonzero and "
            "decay exponent but no actual primitive-content theorem. The explicit higher-log "
            "candidate has proved moments and uniqueness; endpoint nonzero, actual decay and "
            "minimal denominator budget remain open. All-scale claims rely on written proofs; "
            "finite certificates, visual identity checks and hashes verify their stated inputs."
        ),
        "local_links_checked": 0, "missing_links": [],
    }
    # The audit is linked from the report, so create the output before resolving local references.
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    docs = [RESEARCH / (stem + ".md") for stem in STEMS]
    docs += [
        main_report, review, ROOT / "README.md", LIBRARY / "README.md",
        LIBRARY / "explicit_relative_reading_map_20261004.md",
    ]
    missing = []
    count = 0
    for doc in docs:
        for target, path in local_links(doc):
            count += 1
            if not path.exists():
                missing.append({"document": str(doc.relative_to(ROOT)), "target": target})
    result["local_links_checked"] = count
    result["missing_links"] = missing
    result["status"] = "delivery_checks_passed" if not missing else "missing_links"
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    assert not missing, missing
    print(json.dumps({
        "status": result["status"], "reports": len(reports),
        "new_original_pdfs": len(originals), "frozen_reports": len(frozen_checks),
        "earlier_original_pdfs": len(old_pdf_files), "local_links": count,
        "new_irrationality_theorem": False, "new_lean_formalization": False,
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()

