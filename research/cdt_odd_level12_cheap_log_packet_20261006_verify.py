"""Two preselected D12 log families: exact column arithmetic only.

No previous producer is imported or executed.  No prime or degree search.
The all-order arithmetic and actual rank proof remain in the Markdown.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import math

checks=[]
def ck(name, actual, expected=True):
    checks.append({"name":name,"actual":str(actual),"expected":str(expected),
                   "passed":actual==expected})
    if actual != expected:
        raise AssertionError(name)

def integral(pieces):
    return 2*sum(A*(hi-lo)+B*(hi*hi-lo*lo)/2 for lo,hi,A,B in pieces)

def S(x,Qpos,H,beta):
    return min(Qpos,max(Q(0),1-x),H+max(Q(0),1-x/beta))

columns=[
 ("m13c2",Q(9,13),Q(3,13),Q(1,2),Q(129,169),[
  (Q(0),Q(7,26),Q(9,13),Q(0)),
  (Q(7,26),Q(1,2),Q(16,13),Q(-2)),
  (Q(1,2),Q(10,13),Q(3,13),Q(0)),
  (Q(10,13),Q(1),Q(1),Q(-1))]),
 ("m23c2",Q(19,23),Q(3,23),Q(1,2),Q(369,529),[
  (Q(0),Q(7,46),Q(19,23),Q(0)),
  (Q(7,46),Q(1,2),Q(26,23),Q(-2)),
  (Q(1,2),Q(20,23),Q(3,23),Q(0)),
  (Q(20,23),Q(1),Q(1),Q(-1))]),
 ("m23c3",Q(13,23),Q(3,23),Q(1,3),Q(249,529),[
  (Q(0),Q(13,69),Q(13,23),Q(0)),
  (Q(13,69),Q(1,3),Q(26,23),Q(-3)),
  (Q(1,3),Q(20,23),Q(3,23),Q(0)),
  (Q(20,23),Q(1),Q(1),Q(-1))])]
for label,Qpos,H,beta,expected,pieces in columns:
    for j,(lo,hi,A,B) in enumerate(pieces):
        # Each constraint is affine on this interval: checking endpoints proves
        # dominance of the selected one throughout; the midpoint identifies it.
        for where,x in [("left",lo),("middle",(lo+hi)/2),("right",hi)]:
            ck(f"{label} segment{j} {where}",A+B*x,S(x,Qpos,H,beta))
    ck(label+" exact integral",integral(pieces),expected)

ck("m13 col1",1-Q(1,13)**2,Q(168,169))
ck("m13 col3",1-Q(10,13)**2,Q(69,169))
ck("m23 col1",1-Q(1,23)**2,Q(528,529))
ck("k2 monomial count",math.comb(5,3),10)
ck("k3 monomial count",math.comb(6,3),20)
ck("m13 rank",1+3+6+3,13)
ck("m23 rank",1+3+6+10+3,23)

lower2=Q(15+126+207,169)
lower3=(Q(15)+Q(3,2)*84+Q(11,6)*300+3*129)/529
upper2=Q(168+129+69,169)
upper3=Q(528+369+249,529)
ck("k2 comonotone lower",lower2,Q(348,169))
ck("k3 comonotone lower",lower3,Q(1078,529))
ck("k2 column upper",upper2,Q(366,169))
ck("k3 column upper",upper3,Q(1146,529))
ck("k2 Jensen upper threshold",Q(13,12)*upper2,Q(61,26))
ck("k3 Jensen upper threshold",Q(23,22)*upper3,Q(573,253))
ck("k2 threshold below12/5",Q(61,26)<Q(12,5))
ck("k3 threshold below12/5",Q(573,253)<Q(12,5))

# Strict rational proof C_* > 12/5: r<7/4 and exp(48/5)*(15/4)<16^4.
x=Q(48,5); degree=40
partial=sum(x**j/math.factorial(j) for j in range(degree+1))
tail_first=x**(degree+1)/math.factorial(degree+1)
tail_upper=tail_first/(1-x/Q(degree+2))
ck("sqrt3 below7/4",Q(3)<Q(7,4)**2)
ck("exp48/5 upper times15/4 below16^4",(partial+tail_upper)*Q(15,4)<16**4)

payload={
 "scope":"Fixed k=2,3 columnwise upper arithmetic; no actual radius/J or rank tests.",
 "passed_count":len(checks),"all_passed":all(c["passed"] for c in checks),
 "checks":checks,
 "display_only":{
  "Cstar_upper_cap":math.log(16)-math.log(2+math.sqrt(3))/4,
  "k2_cost_safe_upper":float(upper2),"k3_cost_safe_upper":float(upper3),
  "k2_Jensen_threshold_safe_cost":float(Q(61,26)),
  "k3_Jensen_threshold_safe_cost":float(Q(573,253))}}
Path(__file__).with_suffix(".json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"{len(checks)} fixed exact checks passed")
