"""NEW fixed algebra certificate; no old producer imports and no scans."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
checks = []

def check(name, assertion):
    passed = bool(assertion)
    checks.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)

a, b, c, d, n = sp.symbols("a b c d n")
gamma = sp.Matrix([[a, b], [c, d]])
M = sp.Matrix([[24, -7], [84, -24]])
T = sp.Matrix([[1, 1], [0, 1]])
A4 = sp.Matrix([[-1, 0], [4, -1]])
A5 = sp.Matrix([[-2, -1], [3, 1]])
x4 = sp.Matrix([[11, 3], [-48, -13]])
x5 = sp.Matrix([[25, 16], [-36, -23]])
check("M determinant 12", M.det() == 12)
check("A4 determinant one", A4.det() == 1)
check("A5 determinant one", A5.det() == 1)
check("x4 primitive cusp scaling PSL central minus", A4*T**(-3)*A4.inv() == -x4)
check("x5 primitive cusp scaling exact", A5*T**4*A5.inv() == x5)
e4 = sp.expand((A4.inv()*gamma*A4)[1, 0])
e5 = sp.expand((A5.inv()*gamma*A5)[1, 0])
o4 = sp.expand((A4.inv()*gamma*M*A4)[1, 0])
o5 = sp.expand((A5.inv()*gamma*M*A5)[1, 0])
check("Gamma self-cusp 4 lower-left identity", e4 == 4*a-16*b+c-4*d)
check("Gamma self-cusp 5 lower-left identity", e5 == 6*a-9*b+4*c-6*d)
check("odd self-cusp 4 numerator identity", o4 == 4*(52*a+180*b+13*c+45*d))
check("odd self-cusp 5 numerator identity", o5 == 3*(69*a+240*b+46*c+160*d))

aa, dd, bb, cc, kappa = sp.symbols("aa dd bb cc kappa", integer=True)
sub = {a:kappa+12*aa, d:kappa+12*dd, b:bb, c:12*cc}
def rational_coeffs_integral(poly):
    return all(z.q == 1 for z in sp.Poly(sp.expand(poly), aa, dd, bb, cc, kappa).coeffs())
check("even cusp4 multiple four full congruence", rational_coeffs_integral(e4.subs(sub)/4))
check("even cusp5 multiple three full congruence", rational_coeffs_integral(e5.subs(sub)/3))
check("odd cusp4 bracket equals kappa modulo12", rational_coeffs_integral((o4.subs(sub)/4-kappa)/12))
check("odd cusp5 bracket equals kappa modulo12", rational_coeffs_integral((o5.subs(sub)/3-kappa)/12))

theta0 = Fraction(232577, 844561)
check("theta0 strictly between0 and1", 0 < theta0 < 1)
check("minimum common height exceeds1/12", 1-theta0 > Fraction(1, 12))
check("even cusp4 height exceeds reciprocal Csquare", Fraction(3,4)*(1-theta0) > Fraction(1,16))
check("even cusp5 height exceeds reciprocal Csquare", Fraction(4,3)*(1-theta0) > Fraction(1,9))
check("odd cusp4 r>=2 threshold", Fraction(3,4)*(4-theta0) > Fraction(3,4))
check("odd cusp5 r>=2 threshold", Fraction(4,3)*(4-theta0) > Fraction(4,3))
discriminant = -188001484800
ratio = Fraction(discriminant, -48)
check("r1 discriminant ratio exact", ratio == 6400*611984)
check("ratio is integer and congruent2 modulo3", ratio.denominator == 1 and ratio.numerator % 3 == 2)
check("trace0 det12 fixed discriminant -48", -4*M.det() == -48)

pins = {}
for name in ["cdt_odd_level12_generator_cocycle_20261006.md", "cdt_odd_level12_schreier_presentation_20261006.md"]:
    pins[name] = hashlib.sha256((HERE/name).read_bytes()).hexdigest()
check("actual cocycle frozen pin", pins["cdt_odd_level12_generator_cocycle_20261006.md"] == "a3f00c593a9fcc3f9b1791b854faa0ad7b721b6c76d67cc52598cd5f919f67ca")
check("full group frozen pin", pins["cdt_odd_level12_schreier_presentation_20261006.md"] == "92ed43b8a1426c66eb65898b016a38012263ae876e753c1bbae2496d104fff9e")

result = {
    "execution_record": "First and single NEW fixed run; no old or peer producers imported or executed; no parameter, word, or prime scans.",
    "passed": sum(row["passed"] for row in checks),
    "checks": checks,
    "identities": {
        "Gamma_cusp4": str(e4), "Gamma_cusp5": str(e5),
        "odd_integer_cusp4": str(o4), "odd_integer_cusp5": str(o5),
        "r1_discriminant_ratio": str(ratio), "theta0": str(theta0),
    },
    "scope": "Only fixed algebra inputs; all-group cusp stabilizers, root transformation, and unknown stabilizer argument are proofs in the Markdown.",
    "pins": pins,
}
dest = HERE / "cdt_odd_level12_stabilizer_parabolic_malnormal_20261006_verify.json"
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(f"{result['passed']} fixed checks passed; wrote {dest.name}")
