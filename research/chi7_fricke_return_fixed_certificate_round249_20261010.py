"""ONE fixed exact certificate, no sampling/scanning.

Inputs are precisely four prescribed order-two returns and cusp b/d values.
Verify matrices/forms; compute the finite Bernoulli sums for their actual
Abel periods. No floating point, numerical periods, or parameter search.
"""
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "chi7_fricke_return_fixed_certificate_round249_20261010.json"
CHI = (0, 1, 1, -1, 1, -1, -1)

def chi(a):
    return CHI[a % 7]

def bern(x):
    x = x - (x.numerator // x.denominator)
    return x*x - x + F(1, 6)

def solve(a, v):
    n = len(v)
    aug = [[F(x) for x in a[i]] + [F(v[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        div = aug[j][j]
        aug[j] = [x/div for x in aug[j]]
        for i in range(n):
            if i != j:
                div = aug[i][j]
                aug[i] = [x-div*y for x, y in zip(aug[i], aug[j])]
    return [row[-1] for row in aug]

def finite_period(b, d):
    # T(z)=Q(z)/(1+...+z^6), Q=z+2z²+z³+2z⁴+z⁵.
    mat = [[sum((j+k) % d == i for k in range(7))
            for j in range(d)] for i in range(d)]
    rhs = [0]*d
    for j, coefficient in ((1,1),(2,2),(3,1),(4,2),(5,1)):
        rhs[j % d] += coefficient
    coeff = solve(mat, rhs)
    assert all(coeff[j] == coeff[(-j) % d] for j in range(d))
    assert all(sum(mat[i][j]*coeff[j] for j in range(d)) == rhs[i]
               for i in range(d))
    c = sum((coeff[j]*bern(F(b*j, d)) for j in range(d)), F(0))
    c2 = sum((coeff[j]*bern(F(2*b*j, d)) for j in range(d)), F(0))
    dcoef = c-F(1,4)*c2
    # Im R = pi² sqrt(7) * rcoef, from the chi_7 Gauss transform.
    rcoef = -F(1,7)*sum(
        (F((-1)**(j+1),2)*chi(a)*bern(F(a,7)+F(b*j,d))
         for j in range(1,d) for a in range(1,7)), F(0))
    return {"T_cyclic_coefficients": [str(x) for x in coeff],
            "C_over_pi2": str(c), "D_over_pi2": str(dcoef),
            "Im_R_over_pi2_sqrt7": str(rcoef)}

def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))
             for j in range(2)] for i in range(2)]

def reduce_form(a,b,c):
    trace = [[a,b,c]]
    while True:
        shift = (a-b)//(2*a)
        if shift:
            c = a*shift*shift+b*shift+c
            b += 2*a*shift
            trace.append([a,b,c])
        if a > c:
            a,b,c = c,-b,a
            trace.append([a,b,c])
            continue
        assert -a < b <= a and a <= c
        assert b*b-4*a*c == -56
        return [a,b,c], trace

rows=[]
for label,a,b,d in (("native",1,0,1), ("plus_cubic",5,1,3),
                    ("minus_cubic",5,-1,3), ("other_real",25,4,9)):
    gamma=[[a,b],[14*b,d]]
    ret=mm(gamma,[[0,-1],[14,0]])
    assert a*d-14*b*b == 1
    assert ret[0][0]+ret[1][1] == 0
    assert mm(ret,ret) == [[-14,0],[0,-14]]
    reduced, reduction=reduce_form(14*d,-28*b,a)
    rows.append({"label":label,"gamma":gamma,"return_matrix":ret,
                 "fixed_point_re":str(F(b,d)),
                 "fixed_point_im_times_sqrt14":str(F(1,d)),
                 "character_d":chi(d),"reduced_form":reduced,
                 "form_reduction":reduction,
                 "period":finite_period(b,d)})
assert len({tuple(row["reduced_form"]) for row in rows}) == 4
assert rows[0]["period"]["D_over_pi2"] == "1/8"
assert rows[0]["period"]["Im_R_over_pi2_sqrt7"] == "0"
assert rows[1]["period"]["D_over_pi2"] == "-5/24"
assert rows[2]["period"]["D_over_pi2"] == "-5/24"
assert rows[1]["period"]["Im_R_over_pi2_sqrt7"] == "4/147"
assert rows[2]["period"]["Im_R_over_pi2_sqrt7"] == "-4/147"
result={"scope":"Exactly four prescribed returns; exact finite sums only",
        "math_executions":1,"parameter_scans":0,"floating_point":False,
        "rows":rows,"status":"PASS"}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
