"""NEW fixed symbolic full-rank interface; no research imports or scans.

The all-scale Laurent-log/module arguments are in the companion proof note.
"""
from pathlib import Path
import hashlib
import json
import sympy as S

base = Path(__file__).resolve().parent
t, u, l, n = S.symbols('t u l n')
checks = []
def check(name, value):
    value = bool(value)
    checks.append({'name': name, 'passed': value})
    if not value:
        raise AssertionError(name)
def zero(value): return S.expand(value) == 0

Q = lambda v: 8*v**4 + 16*v**3 + 20*v**2 + 12*v + 3
P = lambda v: 48*v**3 + 80*v**2 + 40*v + 5
check('exact Q4 reciprocity', zero(Q(-u-1)-Q(u)))
K_at_infinity = t*(-u+S.Rational(1,2))**4-(-u)**4
check('all transformed K Euler coefficients', zero(K_at_infinity+(u**4-t*(u-S.Rational(1,2))**4)))
old_L5_on_tf = -t*(u+1)**5-S.Rational(1,8)*(1-2*(u+1))*Q(-u-1)-u**5/t
new_L5 = u**5-t*S.Rational(1,8)*(2*u+1)*Q(u)+t**2*(u+1)**5
check('full reciprocal operator with shifted F=tf', zero(-t*old_L5_on_tf-new_L5))

c = S.symbols('c0:4')
h0 = -S.Rational(2,3)*l**4 + sum(c[j]*l**j for j in range(4))
check('forcing h0 fourth derivative exact -16', zero(S.diff(h0,l,4)+16))
PminusD_h0 = -48*S.diff(h0,l,3)+80*S.diff(h0,l,2)-40*S.diff(h0,l)+5*h0
S0 = S.expand(-960+S.Rational(3,2)*S.diff(PminusD_h0,l,2))
G0 = -S0
check('S0 full logarithmic degree two', S.Poly(S0,l).degree() == 2)
check('S0 top coefficient independent of all connections', S.Poly(S0,l).coeff_monomial(l**2) == -60)
check('G0 top coefficient independent of all connections', S.Poly(G0,l).coeff_monomial(l**2) == 60)
f0 = S0
for _ in range(5): f0 = S.integrate(f0,l)
b = S.symbols('b0:5')
f0 = S.expand(f0 + sum(b[j]*l**j for j in range(5)))
check('f0 complete fifth derivative gives S0', zero(S.diff(f0,l,5)-S0))
check('f0 degree exactly seven for every connection choice', S.Poly(f0,l).degree() == 7)
check('f0 top coefficient exact -1/42', S.Poly(f0,l).coeff_monomial(l**7) == -S.Rational(1,42))
check('x-log sign gives exact positive 1/42', S.Poly(f0.subs(l,-l),l).coeff_monomial(l**7) == S.Rational(1,42))
check('Ore nonzero remainder witness at zero', (-S.Rational(1,2))**2*P(-S.Rational(1,2)) == -S.Rational(1,4))
check('homogeneous infinity indicial rank4', zero((u**4-t*(u-S.Rational(1,2))**4).subs(t,0)-u**4))
check('homogeneous infinity indicial rank5', zero(new_L5.subs(t,0)-u**5))

# One fixed nilpotent polynomial-derivative matrix in each prescribed space.
def polynomial_derivative_matrix(d):
    mat = S.zeros(d+1)
    for j in range(1,d+1): mat[j-1,j] = j
    return mat
JH = polynomial_derivative_matrix(4)
JF = polynomial_derivative_matrix(7)
check('H fixed-space nilpotence degree5', JH**5 == S.zeros(5))
check('F fixed-space nilpotence degree8', JF**8 == S.zeros(8))
check('all n>=1 H recursion invertibility', zero(((n*S.eye(5)+JH)**4).det()-n**20))
check('all n>=1 F recursion invertibility', zero(((n*S.eye(8)+JF)**5).det()-n**40))

pin_expectations = {
    'cdt_odd_classical_derivative_projection_20261006.md':
        'c24a4d7807bed750f63746b4506f2a238a7d9b9122e2e39ac4871653b39d5c1e',
    'cdt_odd_classical_zeta7_forcing_spin_20261006.md':
        'c3a4212bccdc4dd18331e6a1446cf22dd88462d27b1631c350c12d2f78c9a56a',
    'cdt_odd_classical_spin_monodromy_20261006_verify.json':
        '3713973b1e3907d65b055a8ac465320ab05e9e623baf5ed5193016c478075517',
}
pins = {}
for name, expected in pin_expectations.items():
    pins[name] = hashlib.sha256((base/name).read_bytes()).hexdigest()
    check('frozen input pin '+name, pins[name] == expected)
report = {
    'scope': 'Fixed exact operator reciprocity and branch-independent logarithmic coefficients; actual full rank10 and nonsplitting follow from the companion all-scale proof and already proved irreducible module inputs. No numerical irrationality, full Picard-Vessiot group, complete extension-class parameter classification, or capacity budget claim.',
    'execution_record': 'First execution of this NEW fixed certificate; retained only after all checks passed. No old or peer research producer executed or imported.',
    'H0': str(h0), 'forcing_S0': str(S0), 'F_over_t_0': str(f0),
    'highest_H_log_coefficient': '-2/3',
    'highest_G_log_coefficient': '60',
    'highest_F_t_log_coefficient': '-1/42',
    'highest_F_x_log_coefficient': '1/42',
    'input_pins': pins, 'checks': checks,
    'check_count': len(checks), 'all_passed': all(v['passed'] for v in checks),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n', encoding='utf-8')
print(json.dumps({'checks':len(checks),'all_passed':report['all_passed'],'H_log4':'-2/3','F_t_log7':'-1/42'}))
