"""NEW one-shot verifier for the new all-scale nilpotent gauge proof.

Constructs the operator and gauge independently from printed formulas.
Reads only the author's NEW finite data, never imports or executes old/peer
mathematical producers. Finite checks support, but do not prove, all-n claims.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as s

t, z = s.symbols("t z")
f0, f1, f2, f3, u = s.symbols("f0 f1 f2 f3 u")
w = 1-t
A0 = -1/(16*w**3)
A1 = (4-5*t)/w**3
A2 = (29*t-15)/(2*w**2)
A3 = (2-8*t)/w
B = (17*t-3)/(2*w**2)
G = s.Matrix([[0,t,0,0], [0,0,t,-1],
              [-t*A0,-t*A1,-t*A2,B],
              [-t*t*A0,-t*t*A1,-t*t*A2,t*B]])
checks = []

def check(label, truth):
    assert truth, label
    checks.append(label)

f4 = (-A0*f0-A1*f1-A2*f2-A3*f3+u/16)/t
y = s.Matrix([f0,f1,f2+t*f3,t*t*f3])
dy = s.Matrix([t*f1,t*f2,2*t*f3+t*t*f4,2*t*t*f3+t**3*f4])
source = s.Matrix([0,0,t*u/16,t*t*u/16])
check("exact jet-to-nilpotent-gauge identity including source",
      all(s.cancel(v)==0 for v in dy-G*y-source))
check("exact fourth-order operator source identity",
      s.cancel(t*w**4*f4+w**3*(2-8*t)*f3
               +w*w*(29*t-15)*f2/2+w*(4-5*t)*f1
               -w*f0/16-w**4*u/16)==0)

G5 = s.zeros(5)
G5[:4,:4] = G
G5[2,4] = t/16
G5[3,4] = t*t/16
G5[4,4] = 7*t/(2*w)
S = s.diag(1,2,4,1,1)
H = (S*G5.subs(t,4*z)*S.inv()).applyfunc(s.cancel)
v = 1-4*z
printed = s.Matrix([
    [0,2*z,0,0,0],
    [0,0,2*z,-2,0],
    [z/v**3,-32*z*(1-5*z)/v**3,-2*z*(116*z-15)/v**2,
     2*(68*z-3)/v**2,z],
    [z*z/v**3,-32*z*z*(1-5*z)/v**3,-2*z*z*(116*z-15)/v**2,
     2*z*(68*z-3)/v**2,z*z],
    [0,0,0,0,14*z/v],
])
check("printed five-dimensional rescaled matrix exact",
      all(s.cancel(e)==0 for e in H-printed))
check("all regular coefficients visibly integral at 2",
      all(s.Poly(s.cancel(e*v**3),z).domain.is_ZZ
          for e in H))
R = H.subs(z,0)
check("residue squares to zero", R*R == s.zeros(5))
check("residue is entrywise divisible by 2", all(e%2==0 for e in R))
nn = s.symbols("n", nonzero=True)
check("exact finite inverse formula",
      (nn*s.eye(5)-R)*(s.eye(5)/nn+R/(nn*nn)) == s.eye(5))

def v2(q):
    if not q:
        return 0
    k=0
    while q%2==0:
        q//=2
        k+=1
    return k

def vf(n):
    return sum(n//(2**k) for k in range(1,n.bit_length()+1))

def beta(n):
    return 2*n+2*vf(n)-n//2

probe = Path(__file__).with_name(
    "cdt_odd_R0_conifold_effective_denominator_20261006_probe.json")
raw = json.loads(probe.read_text(encoding="utf-8"))
summaries = {}
for name, rec in raw["records"].items():
    coeff = [Fraction(x) for x in rec["coefficients"]]
    check(name+" finite 180-degree coefficients obey new proved dyadic bound",
          all(v2(q.denominator)<=beta(n) for n,q in enumerate(coeff)))
    summaries[name] = {
        "degree": len(coeff)-1,
        "maximum_binary_denominator_exponent": max(v2(q.denominator) for q in coeff),
        "new_bound_at_prefix_degree": beta(len(coeff)-1),
    }
check("finite arithmetic identity for the inductive prefix fee",
      all(2*vf(n)-n//2 == sum(max(v2(j),2*v2(j)-1)
                             for j in range(1,n+1))
          for n in range(181)))
check("finite pairs obey beta(a)+beta(b)<=beta(a+b)+1",
      all(beta(a)+beta(b)<=beta(a+b)+1
          for a in range(181) for b in range(181-a)))
out = {
    "status": "exact_identity_verification_and_finite_support_for_paper_proof",
    "executions": 1,
    "old_or_peer_math_producers_executed_or_imported": 0,
    "checks": checks,
    "check_count": len(checks),
    "author_new_data_sha256": hashlib.sha256(probe.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "matrix": [[str(e) for e in row] for row in H.tolist()],
    "residue": [[str(e) for e in row] for row in R.tolist()],
    "prefix_summaries": summaries,
    "limitations": [
        "All-n dyadic bound rests on the written nilpotent-recursion proof.",
        "No claim that odd-prime generic radius hypotheses have been verified.",
        "No Betti integral comparison or irrationality conclusion follows from these checks.",
    ],
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"check_count":len(checks),"prefix_summaries":summaries},indent=2))
