"""Fixed exact certificates for the fixed rational shift filter theorem.

The analytic all-orders asymptotics are proved in the paired report; this file
certifies its algebraic inputs and finitely many representative filter identities.
"""
from pathlib import Path
from hashlib import sha256
import json
import math
import sympy as sp

BASE = Path(__file__).resolve().parent
REPORT = BASE / "odd_zeta_fixed_shift_filters_20261005.md"
OUT = BASE / "odd_zeta_fixed_shift_filters_20261005_verify.json"
x, v, w, t = sp.symbols("x v w t")
p = w**8 + (w-1)**7*(w+7)
f = 7**7*(v+1)**8 + 8**8*v**7
Q = sp.Poly(sp.resultant(f, x+v**7, v), x, domain=sp.ZZ)
checks = []

def record(name, condition, details=None):
    assert condition, name
    item = {"name": name, "passed": True}
    if details is not None:
        item["details"] = details
    checks.append(item)

record("rational_spectral_substitution",
       sp.cancel(p.subs(w, 7*(v+1)/(7-v))-7*f/(7-v)**8)==0)
record("resultant_degree_primitive_leading_constant",
       Q.degree()==8 and Q.content()==1 and Q.LC()==7**49
       and Q.TC()==7**49)
record("spectral_resultant_identity",
       sp.rem(Q.as_expr().subs(x, -v**7), f, v)==0)

factors = {
    3: [x**3-x**2-x-1, x**5+x**4+x-1],
    5: [x+2, x**7+2*x**5+x**4+x**3-2*x**2-2],
}
factor_certificates = []
for prime, gs in factors.items():
    scalar = int(Q.LC()) % prime
    product = scalar*sp.prod(gs)
    record("modular_product_" + str(prime),
           sp.Poly(Q.as_expr()-product, x, modulus=prime).is_zero)
    record("modular_degree_preserved_" + str(prime), scalar!=0)
    for expr in gs:
        g = sp.Poly(expr, x, modulus=prime).monic()
        d = g.degree()
        def frobenius(k):
            r = sp.Poly(x, x, modulus=prime)
            for _ in range(k):
                r = r.pow(prime).rem(g)
            return r
        rr = (frobenius(d)-sp.Poly(x,x,modulus=prime)).rem(g)
        divisors = list(sp.factorint(d)) if d>1 else []
        gcds = []
        for divisor in divisors:
            h = sp.gcd(g, frobenius(d//divisor)
                       -sp.Poly(x,x,modulus=prime))
            gcds.append({"degree_prime_divisor":divisor,"gcd_degree":h.degree()})
            record("frobenius_gcd_%s_%s_%s"%(prime,d,divisor), h.degree()==0)
        record("frobenius_full_%s_%s"%(prime,d), rr.is_zero)
        factor_certificates.append({
            "prime":prime,"factor_coefficients_descending":[int(c)%prime for c in g.all_coeffs()],
            "degree":d,"full_frobenius_remainder_zero":True,"gcd_certificates":gcds,
        })
sets=[]
for prime, gs in factors.items():
    degs=[sp.degree(g,x) for g in gs]
    subsets={sum(degs[j] for j in range(len(degs)) if mask & (1<<j))
             for mask in range(1, 1<<len(degs))}
    sets.append({int(a) for a in subsets if 0<a<8})
record("proper_factor_degree_sets_disjoint", not sets[0].intersection(sets[1]),
       {"mod3":sorted(sets[0]),"mod5":sorted(sets[1])})
# Check the two exact identities separately, without any floating-point roots.
record("real_height_polynomial_identity",
       sp.expand(p.subs(w,-t) - (t**8-(7-t)*(1+t)**7))==0)
record("real_height_spectral_identity",
       sp.cancel(-((7*(w-1)/(w+7))**7).subs(w,-t)
                 -(7*(1+t)/(7-t))**7)==0)

alpha = sp.Rational(7,2)
filter_checks=[]
# Fixed multiplicities 0,1,2,3: representative algebra only, not a universal
# analytic theorem. General proof is section 4 of the report.
for m in (0,1,2,3):
    for power in range(m+1):
        moment = sum((-1)**(m-j)*sp.binomial(m,j)*j**power
                     for j in range(m+1))
        expected = 0 if power<m else math.factorial(m)
        record("filter_moment_%s_%s"%(m,power), moment==expected)
    leading = (-1)**m * sp.rf(alpha,m)
    record("filter_leading_nonzero_%s"%m, leading!=0)
    filter_checks.append({"multiplicity":m,"leading_for_(E-L)^m_divided_by_L^m":str(leading)})
record("noninteger_exponent_rising_factorial_structure",
       alpha>0 and alpha.q==2)

payload={
    "status":"fixed_exact_filter_certificates_passed",
    "as_of":"2026-10-05",
    "report_sha256":sha256(REPORT.read_bytes()).hexdigest(),
    "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
    "new_irrationality_theorem":False,
    "new_lean_formalization":False,
    "parameter_scans":False,
    "Q_coefficients_descending":[int(c) for c in Q.all_coeffs()],
    "Q_definition":"resultant_v(7^7(v+1)^8+8^8v^7,X+v^7)",
    "factor_certificates":factor_certificates,
    "filter_fixed_representatives":filter_checks,
    "checks":checks,
    "analytic_scope":"All-orders asymptotics and the universal fixed-filter lemma are proved in the report, not by this finite certificate.",
}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":payload["status"],"checks":len(checks),"output":str(OUT)},ensure_ascii=False))

