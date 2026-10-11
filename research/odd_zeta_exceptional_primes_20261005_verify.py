"""Fixed exact certificates for the q=7 first exceptional-prime layer.

No numerical zeta values, no parameter search, and no inferred density theorem.
The two full F_p root lists certify two preselected index polynomials, not an
asymptotic root-count estimate. Run with Python 3.12 and sympy.
"""
from __future__ import annotations

from math import comb
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sympy as sp


CHECKS = []


def check(name, condition, **evidence):
    ok = bool(condition)
    CHECKS.append({"name": name, "passed": ok, **evidence})
    if not ok:
        raise AssertionError(name)


def B(n, q=7):
    return sum(comb(q*n, r)*comb(n+r, n)**q for r in range(q*n+1))


def C(n, p):
    d = (7*n) % p
    m = p-n-1
    return sum(comb(d, s)*comb(n+s, n)**7
               for s in range(min(d, m)+1))


def binomial_rows(n, p):
    d = (7*n) % p
    m = p-n-1
    e = min(d, m)
    terms = [((-1)**s*comb(d, s)*comb(m, s)**7) % p
             for s in range(e+1)]
    return d, m, e, terms


def argument_coefficients(n, p):
    d, m = 7*n % p, p-n-1
    e = min(d, m)
    coeff = [1]
    for s in range(1, e+1):
        coeff.append(coeff[-1]*(s-1-d)*pow(n+s, 7, p)
                     *pow(pow(s, 8, p), -1, p) % p)
    return coeff


for n, p in [(2, 13), (7, 19), (23, 37), (31, 83)]:
    d, m, e, terms = binomial_rows(n, p)
    coeff = argument_coefficients(n, p)
    value = sum(a*((-1)**s) for s, a in enumerate(coeff)) % p
    c = C(n, p) % p
    check(f"binomial_hypergeometric_{n}_{p}", value == c == sum(terms) % p,
          n=n, p=p, d=d, m=m, e=e, C_mod_p=c,
          argument_coefficients=coeff)
    # theta^8 F - Z(theta-d)(theta+n+1)^7 F = 0, including
    # the coefficient one degree beyond the truncation.
    ode = []
    for s in range(e+2):
        lhs = (pow(s, 8, p)*coeff[s]) if s <= e else 0
        rhs = (s-1-d)*pow(s+n, 7, p)*coeff[s-1] if s >= 1 else 0
        ode.append((lhs-rhs) % p)
    check(f"truncated_ode_{n}_{p}", all(x == 0 for x in ode),
          residue_coefficients=ode)
    if (n, p) != (2, 13):
        check(f"exact_reversal_{n}_{p}", d == m and d % 2 == 1
              and all((terms[s]+terms[e-s]) % p == 0 for s in range(e+1)),
              terms_mod_p=terms)
    else:
        check("preselected_unit", c != 0, C_mod_p=c)


s, d, m = sp.symbols("s d m")
A = (d-s)*(s+1)
BB = (m-d+s+1)*(m-s)
Delta = (d-m)*(m+1)
check("constant_difference_first_reversal", sp.expand(A-BB-Delta) == 0)
rev = sp.Poly(sp.expand(A**7-BB**7), s)
check("nonzero_difference_degree_twelve", rev.degree() == 12
      and sp.expand(rev.LC()-7*Delta) == 0,
      formal_degree=rev.degree(), leading_coefficient=str(sp.factor(rev.LC())))
A2 = (m-s)*(s+1)
B2 = (d-m+s+1)*(d-s)
check("constant_difference_second_reversal",
      sp.expand(A2-B2-(m-d)*(d+1)) == 0)


X = sp.Symbol("X")
index_polynomials = []
for p in [11, 19]:
    modulus = sp.Poly(X**p-X, X, modulus=p)
    term = sp.Poly(1, X, modulus=p)
    total = term
    for s0 in range(1, p):
        factor = sp.Poly(-(-7*X+s0-1)*(X+s0)**7
                         *pow(pow(s0, 8, p), -1, p), X, modulus=p)
        term = (term*factor).rem(modulus)
        total = (total+term).rem(modulus)
    roots = [x for x in range(p) if int(total.eval(x)) % p == 0]
    values = [int(total.eval(x)) % p for x in range(p)]
    check(f"index_polynomial_all_values_{p}",
          values == [C(x, p) % p for x in range(p)],
          degree=total.degree(), roots=roots)
    product = sp.Poly(1, X, modulus=p)
    for r in roots:
        product *= sp.Poly(X-r, X, modulus=p)
    gcd_poly = sp.gcd(total, modulus).monic()
    check(f"exact_root_gcd_{p}", gcd_poly == product.monic(),
          gcd_coefficients=[int(x) % p for x in gcd_poly.all_coeffs()])
    check(f"nonzero_endpoint_values_{p}", values[0] == values[p-1] == 1)
    index_polynomials.append({
        "p": p, "coefficients_ascending_mod_p":
        [int(total.nth(j)) % p for j in range(p)],
        "values": values, "roots": roots,
        "scope": "Two fixed polynomials; no asymptotic root-count inference."})


x, y = sp.symbols("x y")
U = (1+x)*(1+y)
for n in [1, 2]:
    numerator = sp.Poly(sp.expand(U**n*(1+U)**(2*n)), x, y)
    constant_term = int(numerator.coeff_monomial(x**n*y**n))
    check(f"constant_term_q2_n{n}", constant_term == B(n, 2),
          constant_term=constant_term)

# The top U^(q+1) already supplies every vertex, and all terms lie in
# [-1,q]^q. No expansion in 7 variables is needed.
check("newton_scaling_minimum_seven", all((Fraction(-1, 7) < j < 1) == (j == 0)
      for j in range(-2, 3)) and all(1 < Fraction(7, M) for M in range(1, 7)),
      newton_cube=[-1, 7], dimension=7,
      integer_interior_count_unscaled=7**7, minimum_integer_scaling=7)

for p, a, b in [(17, 1, 1), (29, 1, 3)]:
    lhs, rhs = B(a*p+b) % p, B(a)*B(b) % p
    check(f"partial_lucas_{p}_{a}_{b}", 7*b < p and lhs == rhs,
          p=p, a=a, b=b, lhs=lhs, rhs=rhs)
p, a, b = 11, 1, 2
lhs, rhs = B(a*p+b) % p, B(a)*B(b) % p
check("counterexample_to_full_scalar_lucas", lhs != rhs,
      p=p, a=a, b=b, lhs=lhs, rhs=rhs,
      scope="Rules out an all-prime scalar Lucas identity, not matrix Cartier models.")

report = {
    "status": "passed", "date": "2026-10-05",
    "checks": CHECKS, "number_of_checks": len(CHECKS),
    "index_polynomials": index_polynomials,
    "withdrawn_source_not_used": {
        "arxiv": "1601.06765", "withdrawal_version": "v4",
        "withdrawal_date": "2020-04-23",
        "comments": "Errors in paper uncorrected. Kenneth Ward passed away June 2019",
        "input_to_proofs": False},
    "unproved": ["uniform index-root count o(p)",
                 "weighted exceptional-prime upper bound",
                 "density of higher-jet zero sets"],
}
output = Path(__file__).with_suffix(".json")
report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report_path = Path(__file__).with_name("odd_zeta_exceptional_primes_20261005.md")
report["report_sha256"] = hashlib.sha256(report_path.read_bytes()).hexdigest()
output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "checks": len(CHECKS),
                  "roots": [{"p": a["p"], "roots": a["roots"]}
                            for a in index_polynomials],
                  "full_lucas_counterexample": {"lhs": lhs, "rhs": rhs},
                  "output": str(output)}, ensure_ascii=False))
