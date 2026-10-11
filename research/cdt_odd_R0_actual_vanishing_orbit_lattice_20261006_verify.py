"""NEW self-owned exact matrix verifier; no import of prior/peer producers.

This checks algebraic identities, not actual geometry or lattice saturation.
Run once after the paper proof is written, and disclose every execution.
"""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md"
OUT = ROOT / "cdt_odd_R0_actual_vanishing_orbit_lattice_20261006_verify.json"
checks = []

def ck(name, statement):
    assert bool(statement), name
    checks.append(name)

def zero(mat):
    return all(sp.expand(x) == 0 for x in mat)

I = sp.eye(4)
G = sp.Matrix([[0,8,32,88],[-8,0,8,32],[-32,-8,0,8],[-88,-32,-8,0]])
U = sp.Matrix([[0,0,0,-1],[1,0,0,4],[0,1,0,-6],[0,0,1,4]])
M0 = -U
M1 = sp.Matrix([[1,-8,-32,-88],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
BH = sp.Matrix([[1,4,10,20],[0,-6,-20,-45],[0,4,15,36],[0,-1,-4,-10]])
S = sp.Matrix([[1,0,1,4],[0,1,-4,-11],[0,0,1,0],[0,0,0,1]])
block = sp.Matrix([[0,8,0,0],[-8,0,0,0],[0,0,0,-32],[0,0,32,0]])
v = sp.Matrix([-1,3,-3,1])
ell = sp.Matrix([[1,1,1,1]])
e0 = sp.Matrix([1,0,0,0])
alpha = sp.Matrix([-3,4,-1,0])
gam = v / 2
A = U-I
N = A-A**2/2+A**3/3
k,l,z = sp.symbols("k l z")

ck("Gram skew", G.T == -G)
pf = G[0,1]*G[2,3]-G[0,2]*G[1,3]+G[0,3]*G[1,2]
ck("Pfaffian -256", pf == -256)
ck("Gram determinant 2^16", G.det() == 2**16)
ck("unimodular basis change", S.det() == 1)
ck("integral alternating blocks 8J and -32J", S.T*G*S == block)
snf = smith_normal_form(G, domain=sp.ZZ)
ck("Gram SNF 8,8,32,32", [abs(snf[j,j]) for j in range(4)] == [8,8,32,32])
ck("U integer determinant one", U.det() == 1)
ck("M0 integer determinant one", M0.det() == 1)
ck("M1 integer determinant one", M1.det() == 1)
ck("U preserves Gram", U.T*G*U == G)
ck("M0 preserves Gram", M0.T*G*M0 == G)
ck("M1 preserves Gram", M1.T*G*M1 == G)
ck("physical M0 characteristic (z+1)^4", sp.expand(M0.charpoly(z).as_expr()-(z+1)**4) == 0)
ck("physical M0M1 characteristic (z-1)^4", sp.expand((M0*M1).charpoly(z).as_expr()-(z-1)**4) == 0)
ck("PL exact rank-one", M1-I == e0*sp.Matrix([[0,-8,-32,-88]]))
ck("A order four nilpotent", A**4 == sp.zeros(4) and A**3 != sp.zeros(4))
ck("N square integral expression", N**2 == A**2-A**3)
ck("N cube integral expression", N**3 == A**3)
ck("N cube primitive v ell", N**3 == v*ell)
ck("explicit 6N", 6*N == sp.Matrix([[-11,-2,1,-2],[18,-3,-6,9],[-9,6,3,-18],[2,-1,2,11]]))
Uk = I+k*N+k**2*N**2/2+k**3*N**3/6
Ul = I+l*N+l**2*N**2/2+l**3*N**3/6
Ukl = I+(k+l)*N+(k+l)**2*N**2/2+(k+l)**3*N**3/6
ck("symbolic all-k transport at one", Uk.subs(k,1) == U)
ck("symbolic all-k group law", zero(Uk*Ul-Ukl))
ak = (e0.T*G*Uk*e0)[0]
ck("symbolic all-k actual intersection polynomial", sp.expand(ak-(sp.Rational(8,3)*k**3+sp.Rational(16,3)*k)) == 0)
ck("real involution integer", BH**2 == I)
ck("real involution anti-symplectic", BH.T*G*BH == -G)
ck("real involution reverses U", BH*U*BH == U.inv())
ck("GammaV intersection row -8ell", gam.T*G == -8*ell)
ck("GammaV equals N^3 delta /2", N**3*e0 == 2*gam)
ck("rank-one Gamma expression", N**3 == -gam*(gam.T*G)/4)
ck("remaining real cycle actual integral coordinates", (U-U.inv())*e0-2*gam == alpha)
ck("remaining real cycle conjugation minus", BH*alpha == -alpha)
ck("remaining real cycle delta orthogonal", (e0.T*G*alpha)[0] == 0)
ck("remaining cycle divisibility 16 in orbit lattice", G*alpha == sp.Matrix([0,16,64,144]))
ck("double physical loop cubic charge eight", (M0**2-I)**3 == 8*v*ell)
ck("double physical loop logarithm cubic charge eight", (2*N)**3 == 8*N**3)
den = sp.ilcm(*[x.q for x in G.inv()])
ck("dual orbit lattice exact denominator32", den == 32)

gamma_basis = sp.Matrix.hstack(I[:,0], I[:,1], I[:,2], gam)
gamma_gram = gamma_basis.T*G*gamma_basis
gamma_snf = smith_normal_form(gamma_gram, domain=sp.ZZ)
ck("formal GammaV added index two", abs(gamma_basis.det()) == sp.Rational(1,2))
ck("formal GammaV added Gram SNF8,8,16,16", [abs(gamma_snf[j,j]) for j in range(4)] == [8,8,16,16])

payload = {
    "status": "all_own_exact_matrix_checks_passed",
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "report_sha256": hashlib.sha256(REPORT.read_bytes()).hexdigest(),
    "scope": "Exact matrices and polynomial identities only. Actual cycles, degree-one integral projection, unimodularity, and index256 are established by the paper, not machine verified.",
    "producer_execution_number": 1,
    "old_or_peer_producer_imports_or_executions": 0,
    "checks": checks,
    "check_count": len(checks),
    "intersection_polynomial": str(sp.expand(ak)),
    "gram_pfaffian": int(pf),
    "gram_determinant": int(G.det()),
    "gram_smith_invariant_factors": [8,8,32,32],
    "origin_cube_vector": list(map(int,v)),
    "origin_cube_integer_row": [1,1,1,1],
    "GammaV_orbit_coordinates": [str(t) for t in gam],
    "remaining_integral_cycle_orbit_coordinates": list(map(int,alpha)),
    "physical_M0": [[int(x) for x in row] for row in M0.tolist()],
    "physical_M1": [[int(x) for x in row] for row in M1.tolist()],
    "signed_U": [[int(x) for x in row] for row in U.tolist()],
    "dual_orbit_lattice_denominator": int(den),
}
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status":payload["status"],"check_count":len(checks),"execution_number":1}, ensure_ascii=False))
