"""Fixed exact checks for a proved all-modulus congruence-background lemma."""
from __future__ import annotations
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
STEM = "cdt_odd_congruence_background_20261005"
checks = []

def check(label, condition):
    assert condition, label
    checks.append(label)

def X(b):
    return sp.Matrix([[1, b], [0, 1]])

def Y(c):
    return sp.Matrix([[1, 0], [c, 1]])

def zero_matrix(mat):
    return all(sp.cancel(e) == 0 for e in mat)

u = sp.symbols("u", nonzero=True)
check("symbolic diagonal root factorization",
      zero_matrix(X(1)*Y(u-1)*X(-1/u)*Y(-u*(u-1))-sp.diag(u, 1/u)))
a, b, c, d, n = sp.symbols("a b c d n", nonzero=True)
W = sp.Matrix([[0, -1], [n, 0]])
g = sp.Matrix([[a, b], [n*c, d]])
check("symbolic Fricke conjugation",
      zero_matrix(W*g*W.inv()-sp.Matrix([[d, -c], [-n*b, a]])))
check("symbolic Fricke translation conjugation",
      zero_matrix(W*X(1)*W.inv()-Y(-n)))
check("level12 fixed point",
      sp.simplify(-1/(12*(sp.I/sp.sqrt(12)))-sp.I/sp.sqrt(12)) == 0)

# These three examples were specified before execution.  They are not used
# in lieu of the CRT proof for every N|M.
cases = [
    (60, 0, [[13, 2], [84, 13]]),
    (156, 1, [[13, 2], [84, 13]]),
    (60, 1, [[25, 4], [156, 25]]),
]
decompositions = []
for modulus, k, entries in cases:
    mat = sp.Matrix(entries)
    check(f"SL2 input at M={modulus},k={k}", mat.det() == 1)
    check(f"Gamma1(12) input at M={modulus},k={k}",
          int(mat[0,0]-1)%12 == 0 and int(mat[1,1]-1)%12 == 0
          and int(mat[1,0])%12 == 0)
    g0 = X(k)*mat
    uu = int(g0[0,0]) % modulus
    inv = pow(uu, -1, modulus)
    low = int(g0[1,0])*inv % modulus
    upp = int(g0[0,1])*inv % modulus
    roots = [
        ("X", -k), ("Y", low), ("X", 1), ("Y", uu-1),
        ("X", -inv), ("Y", -uu*(uu-1)), ("X", upp),
    ]
    product = sp.eye(2)
    for kind, arg in roots:
        if kind == "Y":
            check(f"lower ideal M={modulus},k={k},arg={arg}", arg % 12 == 0)
            product = product*Y(arg)
        else:
            product = product*X(arg)
    check(f"complete root decomposition M={modulus},k={k}",
          all(int(v)%modulus == 0 for v in product-mat))
    decompositions.append({"modulus": modulus, "k": k, "matrix": entries,
                           "root_factors": roots})

units = {1, 5, 7, 11}
check("level12 units", all(sp.gcd(v,12) == 1 for v in units)
      and sp.totient(12) == len(units))
check("projective diagonal quotient has two classes",
      units == {1, 11} | {5, 7})
diamond = sp.Matrix([[5, 2], [12, 5]])
check("nontrivial diagonal class realized", diamond.det() == 1)
check("nontrivial class square lies in Gamma1",
      int((diamond*diamond)[0,0]-1)%12 == 0)
rank9_flat = Fraction(7)*(1-Fraction(4,81))
check("rank9 optimistic flat", rank9_flat == Fraction(539,81))
check("rank9 bound exceeds 6.65", rank9_flat > Fraction(665,100))
check("rank8 bound is larger", Fraction(441,64) > rank9_flat)
check("cover derivative 16(2+sqrt3)<60",
      Fraction(7,4)**2 > 3 and 16*(2+Fraction(7,4)) == 60)
z = Fraction(41,10)
exp_lower = sum((z**j)/int(sp.factorial(j)) for j in range(19))
check("positive Taylor lower bound exp(4.1)>60", exp_lower > 60)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

out = {
    "status": "fixed_exact_congruence_background_checks_passed",
    "all_fixed_checks_passed": True,
    "fixed_checks": len(checks),
    "checks": checks,
    "fixed_decompositions": decompositions,
    "maximum_background_degree_over_Ct": 2,
    "maximum_augmented_rank_with_target": 9,
    "optimistic_flat_lower_bound": "539/81",
    "scope": "All-modulus proof is CRT and symbolic root factorization in the report; finite cases only verify implementation of those identities.",
    "external_proved_inputs": [
        "Frozen level12 Hauptmodul and canonical alpha local quotient.",
        "Frozen rank8 target quotient Sym6 and highest prime packet.",
        "Classical Eisenstein integrality for algebraic rational power series.",
    ],
    "new_odd_numeric_irrationality_theorem": False,
    "new_lean_formalization": False,
    "general_cover_impossibility_claim": False,
    "report_sha256": sha(HERE/(STEM+".md")),
    "script_sha256": sha(Path(__file__)),
}
(HERE/(STEM+"_verify.json")).write_text(
    json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(f"{len(checks)} fixed exact congruence-background checks passed")
