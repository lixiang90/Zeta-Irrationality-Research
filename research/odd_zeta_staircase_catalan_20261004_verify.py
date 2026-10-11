"""Exact symbolic checks for the fixed-coordinate Catalan staircase report.

This is not a proof by finite prime sampling. The all-prime transfer argument,
nonexistence lemmas, and rational-series integrality proof are in the report.
"""
from pathlib import Path
import json
import sympy as s

P, Q, DP, DQ, A, B, C = s.symbols('P Q DP DQ A B C')
M = s.Matrix([[P, Q], [DP+Q*A, P+DQ+Q*B]])
t = -P/Q
Dt = -DP/Q+P*DQ/Q**2
riccati = Dt+t**2-B*t-A
det_check = s.factor(M.det()/Q**2-riccati)
recover_row = s.Matrix([[P+DQ+Q*B, -Q]])*M/M.det()
recover_check = (recover_row-s.Matrix([[1, 0]])).applyfunc(s.factor)

w = s.symbols('w')
aa = (8*w-3)/(16*(1-w))
bb = (3*w-2)/(2*(1-w))
cc = 1/(32*(1-w))
k = 2*w/(1-4*w)
r = -10*w/(1-4*w)
ss = -12*w/(1-4*w)
system = s.Matrix([[0,0,0,0], [0,0,1,0],
                   [cc,aa,bb,0], [0,r,ss,k]])
alpha, beta, gamma = (s.Function(name)(w) for name in ['alpha','beta','gamma'])
row = s.Matrix([[alpha,beta,gamma,1]])
theta_row = row.applyfunc(lambda f: w*s.diff(f,w))+row*system-k*row
expected = s.Matrix([[w*s.diff(alpha,w)-k*alpha+cc*gamma,
                      r+w*s.diff(beta,w)+aa*gamma-k*beta,
                      ss+beta+w*s.diff(gamma,w)+(bb-k)*gamma,0]])
quotient_check = (theta_row-expected).applyfunc(s.factor)

result = {
    'scope': 'Fixed rational combinations in the old coordinate w only; no parameter or prime scan.',
    'generic_two_by_two_determinant': str(s.factor(M.det())),
    'det_over_Q_squared_minus_Riccati': str(det_check),
    'recovery_row_minus_F_projection': [[str(v) for v in row] for row in recover_check.tolist()],
    'quotient_theta_minus_k_difference': [[str(v) for v in row] for row in quotient_check.tolist()],
    'necessary_flat_cost': {str(m): str(4*(1-s.Rational(1,m*m))) for m in [2,3,4]},
    'natural_safe_table_flat_cost': str(s.Rational(3*4+5*4+7*5,16)),
    'all_symbolic_checks_passed': det_check == 0 and recover_check.is_zero_matrix and quotient_check.is_zero_matrix,
    'not_certified_here': ['Riccati and inhomogeneous rational nonexistence (audited in the prior report)',
                           'all-prime early occurrence and rational-series integrality (proved in the companion report)'],
}
assert result['all_symbolic_checks_passed']
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
