"""Exact rational control input for the common Markov interface."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path(__file__).resolve().parent
report=root/"odd_zeta_primitive_routes_progress_20261005.md"
mu0=F(1)+F(1,2)
mu1=F(1,2)+F(1,3)
p_const=-mu1/mu0
assert p_const==-F(5,9)
assert 9*mu1-5*mu0==0
B=-14
S=9*mu0
target=F(1)
J=B*target+S
I=J/B
approx=-S/B
assert S==F(27,2) and J==-F(1,2)
assert I==F(1,28) and approx==F(27,28)
assert approx.denominator*I==1
out={
 "status":"fixed_exact_rational_control_passed",
 "report_sha256":sha256(report.read_bytes()).hexdigest(),
 "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
 "measure":"(1+u) du on [0,1]",
 "target":"1",
 "moment_formula":"1/(m+1)+1/(m+2)",
 "fixed_s":1,
 "P":"u-5/9","Q":"9u-5","B":B,"S":str(S),
 "normalized_error":str(I),"reduced_approximant":str(approx),
 "primitive_value":1,
 "all_scale_input":"The regular Markov error exponent is proved in the report. Positive rational-target primitive values are positive integers; finite input only verifies the first-scale arithmetic.",
 "no_irrationality_claim":True,
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":out["status"],"output":str(path)}))

