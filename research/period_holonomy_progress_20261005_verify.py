"""Exact coordinate certificate for the closed polynomial logarithmic integral family."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd,lcm
import hashlib,json
FILE=Path(__file__).resolve()
REPORT=FILE.with_name("period_holonomy_progress_20261005.md")
a=[12,4,3,4,12,1];b=[5,1,0,-1,-5,0]
checks=[]
def check(name,condition):
    checks.append({"name":name,"passed":bool(condition)})
    assert condition,name
def trigamma_row(n):
    q,r=divmod(n-1,6);r+=1
    C=-36*sum((Q(1,(r+6*j)**2) for j in range(q)),Q(0))
    return (C,Q(a[r-1]),Q(9,2)*b[r-1])
def integral_row(poly):
    row=[Q(0),Q(0),Q(0)]
    for k,v in poly.items():
        tr=trigamma_row(k+1)
        row=[x+Q(v)*y/36 for x,y in zip(row,tr)]
    return row
cases=[
 ("pure_L_positive_integral",{1:1,3:-1},[Q(0),Q(0),Q(1,4)]),
 ("rational_positive_integral",{0:1,6:-1},[Q(1),Q(0),Q(0)]),
 ("mixed_positive_integral",{0:1,1:-1},[Q(0),Q(2,9),Q(1,2)]),
 ("zero_true_period_integral",{0:1,1:-5,5:8},[Q(0),Q(0),Q(0)]),
]
records=[]
for name,poly,expected in cases:
    row=integral_row(poly)
    check(name,row==expected)
    records.append({"name":name,"polynomial":poly,"C_A_B":[str(x) for x in row],"is_rational_by_CDT":row[1]==row[2]==0})
check("trigamma7_boundary",trigamma_row(7)==(Q(-36),Q(12),Q(45,2)))
check("trigamma13_boundary",trigamma_row(13)==(Q(-1800,49),Q(12),Q(45,2)))
# Clearing complete coordinate content retains the rational boundary column.
row=integral_row({0:1,6:-1});D=lcm(*[x.denominator for x in row]);ints=[int(D*x) for x in row]
check("complete_integral_content",gcd(*ints)==1 and ints==[1,0,0])
result={"status":"fixed_exact_log_integral_coordinates_passed","as_of":"2026-10-05",
 "report_sha256":hashlib.sha256(REPORT.read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(FILE.read_bytes()).hexdigest(),
 "checks":checks,"check_count":len(checks),"fixed_examples":records,
 "external_input":"CDT Theorem A: 1,zeta(2),L(2,chi_-3) are Q-linearly independent.",
 "scope":"Exact period coordinates; actual integral identities and complete-family proofs are in the report.",
 "new_global_irrationality_theorem":False,"new_lean_formalization":False,"parameter_scan":False}
FILE.with_suffix(".json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"checks":len(checks),"report_sha256":result["report_sha256"]}))

