"""Check this delivery without changing frozen reports or original PDFs."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"
STEMS = [
    "odd_zeta_staircase_catalan_20261004",
    "odd_zeta_cover_catalan_20261004",
    "odd_zeta_cover_budget_20261004",
    "odd_zeta_content_geometry_20261004",
    "odd_zeta_new_period_systems_20261004",
    "odd_zeta_bb_fine_budget_20261004",
    "odd_zeta_bb_fixed_gauge_packet_20261004",
    "odd_zeta_cover_elliptic_quotients_20261004",
]
FROZEN = {
    "odd_zeta_bridge_catalan_20261004.md":
        "c06d052d8074305e45c18b9cc7554f50d2aae7fe999a2b2b85a9c8b86d66c42d",
    "odd_zeta_bridge_catalan_system_20261004.md":
        "57992089334e68060999e136520433f206699c932d42e04d7bf471a65f94dae0",
    "odd_zeta_staircase_catalan_20261004.md":
        "8b72ea0e81211d2eb79c3e5a80674ec491d6e82f4c32c49b0c99a28cd9fa3e72",
    "odd_zeta_cover_budget_20261004.md":
        "0af1c3bd03a1c76e076f450af83f3d0f133ffec21d0c69a3d6f7dec0ff191371",
    "odd_zeta_bb_fine_budget_20261004.md":
        "aa96752f7a071063453d41c268ec53e4511a572675db109d6bf6d2ceb79c5761",
    "odd_zeta_bb_fixed_gauge_packet_20261004.md":
        "107a39664a4b65452c86501a992404224e3b150f2ae2b23ad7554511fc2ca5d0",
}
OUTPUT = RESEARCH / "odd_zeta_next_routes_delivery_20261004.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_links(path: Path):
    source = path.read_text(encoding="utf-8-sig")
    fence = chr(96) * 3
    source = re.sub(fence + r"[\s\S]*?" + fence, "", source)
    tick = chr(96)
    source = re.sub(tick + r"[^" + tick + r"\n]*" + tick, "", source)
    source = re.sub(r"\\\[[\s\S]*?\\\]", "", source)
    source = re.sub(r"\\\([\s\S]*?\\\)", "", source)
    for target in re.findall(r"(?<!\\)\[[^\]\n]+\]\(([^)\n]+)\)", source):
        target = target.strip("<>")
        if target.startswith(("https://", "http://", "app://", "codex://", "#")):
            continue
        target = re.sub(r":\d+$", "", target.split("#")[0])
        resolved = Path(target) if re.match(r"^[A-Za-z]:[/\\]", target) else path.parent / target
        yield target, resolved


def main() -> None:
    records = []
    for stem in STEMS:
        files = {suffix: RESEARCH / (stem + suffix) for suffix in [".md", "_verify.py", "_verify.json"]}
        for path in files.values():
            assert path.is_file(), str(path)
        certificate = json.loads(files["_verify.json"].read_text(encoding="utf-8-sig"))
        pass_flags = {
            k: v for k, v in certificate.items()
            if isinstance(v, bool) and k.startswith("all_") and k.endswith("passed")
        }
        assert all(pass_flags.values()), (stem, pass_flags)
        records.append({
            "report": files[".md"].name,
            "report_sha256": sha256(files[".md"]),
            "exact_certificate": files["_verify.json"].name,
            "certificate_sha256": sha256(files["_verify.json"]),
            "certificate_status": certificate.get("status", "exact_checks_passed" if pass_flags else "inspect_scope"),
            "explicit_pass_flags": pass_flags,
            "scope": certificate.get("scope", "See individual certificate and proof"),
        })

    frozen = []
    for name, expected in FROZEN.items():
        actual = sha256(RESEARCH / name)
        assert actual == expected, (name, actual, expected)
        frozen.append({"file": name, "sha256": actual, "unchanged": True})

    manifest_path = ROOT / "literature" / "manifest_next_route_20261004.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert len(manifest["sources"]) == 7
    library = []
    for record in manifest["sources"]:
        pdf = ROOT / "literature" / record["file"]
        assert pdf.read_bytes()[:5] == b"%PDF-"
        assert sha256(pdf) == record["sha256"]
        library.append({
            "file": pdf.name,
            "sha256": record["sha256"],
            "pages": record["pages"],
            "fixed_version": record["version"],
        })

    # Output itself is linked, so create it before checking local references.
    result = {
        "as_of": "2026-10-04",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "delivery_checks_passed",
        "irrationality_theorem_obtained": False,
        "new_lean_formalization": False,
        "parameter_scans": False,
        "reports": records,
        "main_report": "odd_zeta_next_routes_progress_20261004.md",
        "main_report_sha256": sha256(RESEARCH / "odd_zeta_next_routes_progress_20261004.md"),
        "frozen_report_checks": frozen,
        "library_new_original_pdfs": library,
        "independent_read_only_reviews": {
            "staircase_catalan": "paper_mechanism",
            "cover_catalan": "paper_mechanism",
            "cover_budget": "paper_mechanism",
            "content_geometry": "zeta7_moment_extension",
            "new_period_systems": "root and paper_mechanism",
            "bb_fine_budget": "root and paper_mechanism",
            "bb_fixed_gauge_packet": "root and zeta7_distribution_new",
            "cover_elliptic_quotients": "root",
        },
        "proof_scope": (
            "Written all-scale proofs plus exact algebra certificates; finite checks do not replace "
            "analytic continuation, functional independence, or prime arguments. "
            "Natural-basis budget barriers are not impossibility results for arbitrary new systems."
        ),
        "local_links_checked": 0,
        "missing_local_links": [],
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    docs = [RESEARCH / (s + ".md") for s in STEMS]
    docs += [
        RESEARCH / "odd_zeta_next_routes_progress_20261004.md",
        ROOT / "README.md",
        ROOT / "literature" / "README.md",
        ROOT / "literature" / "next_route_reading_map_20261004.md",
    ]
    count, missing = 0, []
    for doc in docs:
        for target, path in local_links(doc):
            count += 1
            if not path.exists():
                missing.append({"document": str(doc.relative_to(ROOT)), "target": target})
    result["local_links_checked"] = count
    result["missing_local_links"] = missing
    result["status"] = "delivery_checks_passed" if not missing else "missing_links"
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    assert not missing, missing
    print(json.dumps({
        "status": result["status"],
        "reports": len(records),
        "original_pdfs": len(library),
        "local_links": count,
        "new_irrationality_theorem": False,
        "new_lean_formalization": False,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
