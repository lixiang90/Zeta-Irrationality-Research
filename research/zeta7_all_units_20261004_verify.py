"""Independent certificate replay; no producer reduction/lifting code is used.

Reconstructs every matrix from the original rational coefficient cache, checks
the stored coefficient-lattice identities, and directly enumerates all binary
unit lifts needed to certify the finite v2(x)=47,...,64 exclusion.
"""
import hashlib
import json
import math
import sys
from pathlib import Path
from flint import fmpq as Q, arb, ctx

sys.set_int_max_str_digits(0)
FOLDER = Path(__file__).parent


def read(name):
    return json.loads((FOLDER / name).read_text(encoding="utf-8"))


def vq(c, p):
    if not c:
        return None
    n, d = abs(int(c.numerator)), int(c.denominator)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def residue(c, p, modulus):
    n, d = int(c.numerator), int(c.denominator)
    assert d % p
    return (n * pow(d, -1, modulus)) % modulus


def identity(matrix, multipliers, column, conductor, p, D):
    modulus = p ** D
    R = list(map(int, multipliers))
    assert len(R) == len(matrix)
    actual = [sum(r * row[j] for r, row in zip(R, matrix)) % modulus
              for j in range(len(matrix[0]))]
    assert actual == [p ** conductor % modulus if j == column else 0
                      for j in range(len(matrix[0]))]


def lifted_matrix(oldA, oldmonomials, monomials, labels):
    index = {m: i for i, m in enumerate(monomials)}
    result = []
    for k, a, b in labels:
        row = [0] * len(monomials)
        for (i, j), c in zip(oldmonomials, oldA[k]):
            row[index[(i + a, j + b)]] = c
        result.append(row)
    return result


def binary_empty_tree(coeff, a, b, v0, last_layer, x_only=False):
    weighted = [(i, j, k, c * Q(2) ** (i*a + j*b))
                for i, j, cs in coeff if not (x_only and j)
                for k, c in enumerate(cs) if c]
    m = min(vq(c, 2) for i, j, k, c in weighted)
    D = v0 - m
    assert D > 0
    modulus = 2 ** D
    rows = {}
    for i, j, k, c in weighted:
        scaled = c / Q(2) ** m
        e = vq(scaled, 2)
        if e < D:
            rows.setdefault(k, []).append((i, j, residue(scaled, 2, modulus), e))

    # Direct evaluation of every lifted pair, with no Jacobian shortcut.
    def zero(u, v, r):
        mod = 2 ** r
        up = [pow(u, i, mod) for i in range(11)]
        vp = [pow(v, j, mod) for j in range(3)]
        return all(sum(c * up[i] * vp[j] for i, j, c, e in terms if e < r) % mod == 0
                   for terms in rows.values())

    roots = [(1, 1)] if zero(1, 1, 1) else []
    maximum = len(roots)
    tested = 1
    if not roots:
        return dict(empty_at_layer=1, maximum_branches=0, pairs_directly_evaluated=tested)
    for r in range(2, last_layer + 1):
        half = 2 ** (r - 1)
        candidates = [(u + aa*half, v + bb*half)
                      for u, v in roots for aa in range(2)
                      for bb in ([0] if x_only else range(2))]
        roots = [(u, v) for u, v in candidates if zero(u, v, r)]
        tested += len(candidates)
        maximum = max(maximum, len(roots))
        if not roots:
            return dict(empty_at_layer=r, maximum_branches=maximum,
                        pairs_directly_evaluated=tested)
    raise AssertionError("Stored all-unit exclusion did not replay as an empty complete tree")


def main():
    source = "zeta7_two_moment_partial_20261004_coefficients.json"
    raw = (FOLDER / source).read_bytes()
    data = json.loads(raw)
    coeff = [(r["i"], r["j"], [Q(c) for c in r["polynomial_coefficients"]])
             for r in data["coefficients"]]
    oldmonomials = [(i, j) for i, j, cs in coeff]
    G = [[cs[k] if k < len(cs) else Q(0) for i, j, cs in coeff] for k in range(38)]
    ct0 = Q(read("zeta7_joint_lattice_20261004_completion.json")["original_baseline_content"])
    checked_files = [source, "zeta7_joint_lattice_20261004_completion.json"]
    base = read("zeta7_all_units_20261004.json")
    assert base["status"] == "passed"
    assert base["source_coefficients_sha256"] == hashlib.sha256(raw).hexdigest()
    assert list(map(tuple, base["monomials"])) == oldmonomials
    base_checks = []
    for result in base["results"]:
        p, D = result["p"], result["target_power"]
        m = min(vq(c, p) for row in G for c in row if c)
        assert m == result["coefficient_minimum_valuation"]
        assert vq(ct0, p) - m == D
        A = [[residue(c / Q(p)**m, p, p**D) for c in row] for row in G]
        assert A == [list(map(int, row)) for row in result["scaled_coefficient_matrix"]]
        for column, c in enumerate(result["constraints"]):
            assert (c["i"], c["j"]) == oldmonomials[column]
            identity(A, c["multipliers"], column, c["conductor"], p, D)
            assert c["necessary_weight"] == D - c["conductor"]
        bound = max(0, max(math.ceil(c["necessary_weight"]/c["i"])
                           for c in result["constraints"] if c["i"] and not c["j"]))
        assert bound == result["all_unit_minimum_x_valuation"]
        base_checks.append(dict(p=p, x_valuation_bound=bound, identities_checked=27))
        print("replayed degree0 prime", p, flush=True)
    checked_files.append("zeta7_all_units_20261004.json")

    macaulay_checks = []
    strongest = {}
    for degree in [2, 4, 6, 8]:
        name = f"zeta7_all_units_20261004_macaulay_d{degree}.json"
        d = read(name)
        assert d["status"] == "passed"
        assert d["source_coefficients_sha256"] == hashlib.sha256(raw).hexdigest()
        monomials = list(map(tuple, d["monomials"]))
        for result in d["results"]:
            p, D, m = result["p"], result["target_power"], result["coefficient_minimum_valuation"]
            assert m == min(vq(c, p) for row in G for c in row if c)
            assert vq(ct0, p) - m == D
            oldA = [[residue(c / Q(p)**m, p, p**D) for c in row] for row in G]
            A = lifted_matrix(oldA, oldmonomials, monomials, result["row_labels"])
            assert A == [list(map(int, row)) for row in result["scaled_macaulay_matrix"]]
            # Replay every stored nontrivial pure-x identity, not just the best.
            count = 0
            for c in result["pure_x_certificates"]:
                assert c["minimum_x_valuation"] == max(0, math.ceil((D-c["conductor"])/c["i"]))
                if c["conductor"] < D:
                    identity(A, c["multipliers"], monomials.index((c["i"], 0)), c["conductor"], p, D)
                    count += 1
            bound = max(c["minimum_x_valuation"] for c in result["pure_x_certificates"])
            assert bound == result["all_unit_minimum_x_valuation"]
            best = next(c for c in result["pure_x_certificates"] if c["minimum_x_valuation"] == bound)
            macaulay_checks.append(dict(degree=degree, p=p, x_valuation_bound=bound,
                                        rows=len(A), columns=len(monomials), identities_checked=count,
                                        best_monomial=best["i"], best_conductor=best["conductor"]))
            if degree == 8:
                strongest[p] = bound
            print("replayed Macaulay", degree, p, "bound", bound, flush=True)
        checked_files.append(name)

    name = "zeta7_all_units_20261004_unit_ideal_p2_d4.json"
    units = read(name)
    assert units["status"] == "passed"
    unit_checks = []
    certified_faces = set()
    v0 = vq(ct0, 2)
    for result in units["results"]:
        a, b, D, m = result["a"], result["b"], result["target_power"], result["coefficient_minimum_valuation"]
        assert m == min(vq(c, 2)+i*a+j*b for i, j, cs in coeff for c in cs if c)
        assert v0 - m == D
        oldA = [[residue(c * Q(2)**(i*a+j*b-m), 2, 2**D)
                 for (i, j), c in zip(oldmonomials, row)] for row in G]
        monomials = list(map(tuple, result["monomials"]))
        # This producer omits monomials whose every coefficient is 0 modulo 2^D.
        index = {m: i for i, m in enumerate(monomials)}
        A = []
        for k, r, s in result["row_labels"]:
            row = [0] * len(monomials)
            for (i, j), c in zip(oldmonomials, oldA[k]):
                if c:
                    row[index[(i+r, j+s)]] = c
            A.append(row)
        assert A == [list(map(int, row)) for row in result["scaled_macaulay_matrix"]]
        if result["all_unit_exclusion_certified"]:
            assert result["conductor"] < D
            identity(A, result["multipliers"], monomials.index(tuple(result["unit_monomial"])),
                     result["conductor"], 2, D)
            certified_faces.add((a, b))
        else:
            assert result["conductor"] == D
        unit_checks.append(dict(a=a, b=b, conductor=result["conductor"], target_power=D,
                                exclusion_certified=result["all_unit_exclusion_certified"]))
        print("replayed unit face", a, b, flush=True)
    checked_files.append(name)

    name = "zeta7_all_units_20261004_hensel_p2.json"
    h = read(name)
    assert h["status"] == "passed"
    terms = [(i, j, min(vq(c, 2) for c in cs if c)) for i, j, cs in coeff]
    coefficient_valuations = [(i, j, k, vq(c, 2)) for i, j, cs in coeff
                              for k, c in enumerate(cs) if c]
    finite_checks = []
    for saved in h["rows"]:
        a = saved["a"]
        if a >= 65:
            continue
        bcut = max(0, max(math.ceil((v0-v-i*a)/j) for i, j, v in terms if j))
        assert saved["y_cutoff"] == bcut
        finite_cases = {c["b"]: c for c in saved["cases"] if "b" in c}
        initial_candidates = []
        # Reconstruct every lowest coefficient polynomial rather than trust the
        # old face-support map to identify the complete set of candidate b.
        for b in range(bcut):
            weights = [(k, e+i*a+j*b) for i, j, k, e in coefficient_valuations]
            m = min(w for k, w in weights)
            # In F_2 the only unit is 1, including the leading unit of each
            # rational coefficient.  Thus the initial coefficient is exactly
            # the parity of the number of minimal terms at each X power.
            residues = [0] * 38
            for k, w in weights:
                if w == m:
                    residues[k] ^= 1
            if not any(residues):
                initial_candidates.append(b)
        assert set(initial_candidates) == set(finite_cases)
        row_checks = []
        for b, case in finite_cases.items():
            if case["status"] == "excluded_all_units":
                replay = binary_empty_tree(coeff, a, b, v0, case["obstruction_layer"])
                row_checks.append(dict(b=b, method="complete direct binary lifting", **replay))
            else:
                assert (a, b) in certified_faces
                row_checks.append(dict(b=b, method="checked unit-ideal monomial identity"))
        tail = next(c for c in saved["cases"] if "b_range" in c)
        assert tail["b_range"] == [bcut, "infinity"]
        assert all(v+i*a+j*bcut >= v0 for i, j, v in terms if j)
        assert tail["status"] == "excluded_all_units"
        replay = binary_empty_tree(coeff, a, bcut, v0, tail["obstruction_layer"], x_only=True)
        row_checks.append(dict(b_range=[bcut, "infinity"], method="complete direct x-only lifting", **replay))
        finite_checks.append(dict(a=a, all_nonnegative_y_valuations_excluded=True,
                                 initially_excluded_y_valuations=bcut-len(initial_candidates), checks=row_checks))
        print("directly replayed all binary units for a", a, flush=True)
    assert [r["a"] for r in finite_checks] == list(range(47, 65))
    checked_files.append(name)

    ctx.prec = 192
    raw_M = 2**47 * 3**22 * 5**9 * 7**5 * 11
    refined_M = 2**65 * 3**22 * 5**9 * 7**5 * 11
    assert refined_M > 2**138 and refined_M < 2**150
    def alog(n):
        return str((arb(n) / arb(17)).log())
    global_checks = dict(natural_parameter_scope="x=n/17 with nonzero integral n; y integral at 2,3,5,7,11 (e.g. y=m/17)",
                         degree8_integer_numerator_minimum=str(raw_M), degree8_log_abs_x_minimum=alog(raw_M),
                         face_refined_integer_numerator_minimum=str(refined_M),
                         face_refined_log_abs_x_minimum=alog(refined_M),
                         negative_pd_numerator_upper=str(2**138), positive_pd_numerator_upper=str(2**150),
                         refined_minimum_exceeds_negative_pd_upper=True,
                         refined_minimum_exceeds_positive_pd_upper=False,
                         numerator_minimum_over_negative_pd_upper=str(arb(refined_M)/arb(2**138)))
    out = dict(status="passed", source_coefficients_sha256=hashlib.sha256(raw).hexdigest(),
               degree0_certificates=base_checks, macaulay_certificates=macaulay_checks,
               fixed_face_certificates=unit_checks, complete_finite_binary_exclusions=finite_checks,
               all_integral_unit_necessary_x_valuations_degree8=strongest,
               all_integral_unit_necessary_x_valuations_with_finite_faces={**strongest, 2:65},
               positivity_comparison=global_checks,
               file_hashes={n: hashlib.sha256((FOLDER/n).read_bytes()).hexdigest() for n in checked_files},
               scope="No higher unit digit is sampled in the certified statements. Finite Macaulay degree is not an ideal-completeness claim. Capped Hensel fronts at a>=65 are unresolved; parameters with new small-prime denominators are outside scope.")
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("passed: every saved coefficient identity rebuilt and checked", flush=True)
    print("degree8 all-unit bounds", strongest, flush=True)
    print("p2 finite faces independently exclude every a=47,...,64 and every b>=0", flush=True)
    print("refined log |x| lower", global_checks["face_refined_log_abs_x_minimum"], flush=True)
    print("natural denominator-17 negative x excluded; positive x remains open", flush=True)


if __name__ == "__main__":
    main()
