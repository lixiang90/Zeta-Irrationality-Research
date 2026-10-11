"""NEW fixed Nielsen/Tietze certificate, not a word search.

No old or peer producer is imported or executed.  All words and matrices
below are literal frozen-input data.  The all-group proof is in the sibling
Markdown note; these checks verify its displayed finite substitutions.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})
    if not condition:
        raise AssertionError(name)


def red(word):
    out = []
    for letter in word:
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return out


def mul(*words):
    return red([letter for word in words for letter in word])


def inv(word):
    return [-x for x in word[::-1]]


def substitute(word, images):
    return mul(*(images[x] if x > 0 else inv(images[-x]) for x in word))


U = [2, 5, 8, -1]
V = mul(U, [7, -4])
alpha = {
    1: mul(V, [2, -9], inv(V)),
    2: mul([2, 5, 3, -6], inv(V)),
    3: mul(V, [6, 3, -6], inv(V)),
    4: mul(U, [-7], inv(U)),
    5: mul(V, [6, -3, -5, -6], inv(V)),
    6: mul(U, [3, -6], inv(V)),
    7: mul(V, [-7], inv(U)),
    8: mul(V, [6, -9], inv(V)),
    9: mul(U, [-8, 3, -6], inv(V)),
}
k = [-7, 1, -8, -5, -2]
# New basis order: T, k, u, a, b, c, p, q, v.
new_in_old = {
    1: [2], 2: k, 3: alpha[2], 4: [4], 5: [5], 6: [9],
    7: alpha[4], 8: alpha[5], 9: alpha[9],
}
old_in_new = {
    1: [2, -7, 3, -9, 7, -2],
    2: [1],
    3: [-5, -1, 3, -8, -3, 1],
    4: [4], 5: [5],
    6: [4, 2, -8, -3, 1],
    7: [2, -7, -2],
    8: [-5, -1, 3, -9, 7, -2],
    9: [6],
}
new_alpha = {
    1: [3], 2: [-2], 3: [1], 4: [7], 5: [8], 6: [9],
    7: [4], 8: [5], 9: [6],
}
for j in range(1, 10):
    check(f"old-alpha-involution-{j}", substitute(alpha[j], alpha) == [j])
    check(f"old-from-new-from-old-{j}",
          substitute(old_in_new[j], new_in_old) == [j])
    check(f"new-from-old-from-new-{j}",
          substitute(new_in_old[j], old_in_new) == [j])
    check(f"new-alpha-exact-{j}",
          substitute(substitute(new_in_old[j], alpha), old_in_new)
          == new_alpha[j])
check("alpha-k-is-inverse", substitute(k, alpha) == inv(k))
check("U-rewrite", substitute(U, old_in_new) == [7, -2])
check("V-rewrite", substitute(V, old_in_new) == [-2, -4])


def mm(A, B):
    return tuple(tuple(sum(A[i][l]*B[l][j] for l in range(2))
                       for j in range(2)) for i in range(2))


def mi(A):
    a, b, c_, d = A[0][0], A[0][1], A[1][0], A[1][1]
    determinant = a*d-b*c_
    return ((d/determinant, -b/determinant),
            (-c_/determinant, a/determinant))


def canon(A):
    first = next(x for row in A for x in row if x)
    return tuple(tuple(x/first for x in row) for row in A)


I2 = ((F(1), F(0)), (F(0), F(1)))
matrices = {
    1: ((59, 25), (-144, -61)), 2: ((1, 1), (0, 1)),
    3: ((37, 29), (-60, -47)), 4: ((11, 3), (-48, -13)),
    5: ((25, 16), (-36, -23)), 6: ((11, 9), (-60, -49)),
    7: ((13, 4), (-36, -11)), 8: ((13, 6), (-24, -11)),
    9: ((1, 1), (-12, -11)),
}
matrices = {j: tuple(tuple(F(x) for x in row) for row in A)
            for j, A in matrices.items()}
M = ((F(24), F(-7)), (F(84), F(-24)))
Mprime = ((F(-24), F(-7)), (F(84), F(24)))


def word_matrix(word):
    value = I2
    for letter in word:
        value = mm(value, matrices[letter] if letter > 0
                   else mi(matrices[-letter]))
    return value


for j in range(1, 10):
    check(f"literal-alpha-matrix-{j}", canon(word_matrix(alpha[j]))
          == canon(mm(mm(M, matrices[j]), mi(M))))
check("M-involution", canon(mm(M, M)) == canon(I2))
check("Mprime-involution", canon(mm(Mprime, Mprime)) == canon(I2))
check("kM-is-Mprime", canon(mm(word_matrix(k), M)) == canon(Mprime))
check("k-literal-projective", canon(word_matrix(k))
      == canon(((F(97), F(-28)), (F(-336), F(97)))))

# Pure Z/L nonzero complementary generators. Ordinary polynomial coordinates
# c/(i*pi^3), fixed from the already independently reviewed actual table.
PZ = {4: (-2367360, -17210880, -31311360),
      5: (-1365120, -4354560, -3525120), 9: (0, 0, 0)}
PL = {4: (-2266160, -16555200, -30256320),
      5: (-1329040, -4311360, -3531840),
      9: (-1587840, -3617280, -2073600)}
for j in (4, 5, 9):
    check(f"pureL-extra-{j}-nonzero", any(PL[j]))
check("pureZ-extra-9-zero", not any(PZ[9]))
check("pureZ-extra-4-nonzero", any(PZ[4]))
check("pureZ-extra-5-nonzero", any(PZ[5]))

# Fixed local cone check: even two negative-definite generator translations
# have an indefinite difference. It is an obstruction to a naive cone proof,
# not a search for a zero word.
for j in (4, 5, 9):
    a0, a1, a2 = PL[j]
    check(f"pureL-extra-{j}-negative-definite", a2 < 0 and a1*a1-4*a0*a2 < 0)
diff = tuple(PL[4][i]-PL[5][i] for i in range(3))
check("pureL-4minus5-indefinite", diff[1]**2-4*diff[0]*diff[2] > 0)

input_pins = {
    "cdt_odd_level12_schreier_presentation_20261006.md":
    "92ed43b8a1426c66eb65898b016a38012263ae876e753c1bbae2496d104fff9e",
    "cdt_odd_level12_generator_cocycle_20261006.md":
    "a3f00c593a9fcc3f9b1791b854faa0ad7b721b6c76d67cc52598cd5f919f67ca",
}
for name, digest in input_pins.items():
    check(f"frozen-input-pin-{name}",
          hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest)

payload = {
    "description": "Fixed new free-basis certificate; no word search or old producer",
    "run_history": (
        "First execution stopped at k-literal: the fixed free word gives the "
        "opposite central SL2 representative of the same PSL2 matrix. "
        "Only that assertion was corrected to the projective comparison "
        "already used for M/Mprime and all conjugations. Second execution "
        "passed; mathematical words, period inputs and basis formulas unchanged."
    ),
    "basis_order": ["T", "k", "u", "a=x4", "b=x5", "c=x9", "p", "q", "v"],
    "new_in_old": new_in_old, "old_in_new": old_in_new,
    "new_alpha": new_alpha, "literal_matrices": matrices,
    "pureL_extra_periods": PL, "pureZ_extra_periods": PZ,
    "pureL_4minus5_indefinite": diff,
    "input_pins": input_pins, "checks": checks,
    "check_count": len(checks), "all_passed": all(x["passed"] for x in checks),
}
out = HERE / "cdt_odd_level12_stabilizer_structure_20261006_verify.json"
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2,
                          default=lambda x: str(x))+"\n", encoding="utf-8")
print(f"{len(checks)} fixed checks passed; wrote {out.name}")
