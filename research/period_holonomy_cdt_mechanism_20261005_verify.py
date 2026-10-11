"""Exact algebra and outward-ball budget certificates for the fixed CDT v2.

No asserted hypothetical period relation is used as numerical input. The source's
17-function independence and analytic contour integral are explicitly external
theorems, not inferred from these finite coefficient identities.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, lcm, factorial
import hashlib
import json
import sympy as sp
from flint import arb, ctx

ctx.prec = 160
HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')
checks = []


def record(name, condition, **evidence):
    assert bool(condition), name
    checks.append({'name': name, 'passed': True, **evidence})


def L(n):
    result = 1
    for k in range(1, n+1):
        result = lcm(result, k)
    return result


def coefficients(m, J):
    a = 2*m+1
    u = [sum(comb(j,k)*comb(j+k,k)*m**k for k in range(j+1))
         for j in range(J+1)]
    v = [F()] + [sum((F(u[j-t]*u[t-1], t) for t in range(1,j+1)), F())
                  for j in range(1,J+1)]
    for j in range(J):
        uprev, vprev = (u[j-1], v[j-1]) if j else (0, F())
        assert (j+1)*u[j+1]-a*(2*j+1)*u[j]+j*uprev == 0
        assert (j+1)*v[j+1]-a*(2*j+1)*v[j]+j*vprev == (j == 0)
    assert all((L(j)*v[j]).denominator == 1 for j in range(1,J+1))
    return a, u, v


x = sp.Symbol('x')
raw_limit = 18
for m, n in [(2, 3), (10**6, 10**6+1)]:
    a, ua, va = coefficients(m, raw_limit)
    b, ub, vb = coefficients(n, raw_limit)
    record(f'Legendre_integral_coefficients_{m}_{n}',
           va[1] == 1 and va[2] == F(3*a,2)
           and va[3] == F(15*a*a-4,6),
           corrected_H_first_coefficients=[str(t) for t in va[:4]])
    Q4 = 1-4*a*b*x+(-2+4*a*a+4*b*b)*x*x-4*a*b*x**3+x**4
    p2 = sp.Poly((x-1)*x*(1+x)*Q4, x)
    p1 = sp.Poly(-1+8*a*b*x+(5-12*a*a-12*b*b)*x*x+16*a*b*x**3
                 +(-7+4*a*a+4*b*b)*x**4-8*a*b*x**5+3*x**6,x)
    p0 = sp.Poly(a*b+(1-3*a*a-3*b*b)*x+8*a*b*x*x
                 -(2+a*a+b*b)*x**3-a*b*x**4+x**5,x)
    components = {
        'AA': [F(ua[j]*ub[j]) for j in range(raw_limit+1)],
        'HA': [va[j]*ub[j] for j in range(raw_limit+1)],
        'AH': [ua[j]*vb[j] for j in range(raw_limit+1)],
        'HH': [va[j]*vb[j] for j in range(raw_limit+1)]}
    forcing = {
        'AA': sp.Poly(0,x),
        'HA': sp.Poly(-b+3*a*x-3*b*x*x+a*x**3,x),
        'AH': sp.Poly(-a+3*b*x-3*a*x*x+b*x**3,x),
        'HH': sp.Poly(-1+2*x*x-x**4,x)}
    for name, c in components.items():
        residues=[]
        for j in range(13):
            value=F()
            for derivative,p in enumerate([p0,p1,p2]):
                for k in range(p.degree()+1):
                    index=j-k+derivative
                    if index >= derivative:
                        value += int(p.nth(k))*F(factorial(index),factorial(index-derivative))*c[index]
            residues.append(value-F(int(forcing[name].nth(j))))
        record(f'Hadamard_M_identity_{m}_{n}_{name}', all(t == 0 for t in residues))
        record(f'Hadamard_LCM_squared_{m}_{n}_{name}',
               all((L(j)**2*c[j]).denominator == 1 for j in range(raw_limit+1)))

    # S_k=x^k+w(x)^k, w=x/(x-1), y=x+w=xw. Exact recurrence.
    polys = [[2],[0,1]]
    for k in range(2,raw_limit+1):
        out=[0]*(k+1)
        for j,t in enumerate(polys[-1]):out[j+1]+=t
        for j,t in enumerate(polys[-2]):out[j+1]-=t
        polys.append(out)
    record(f'symmetrization_support_{m}_{n}',
           all(all(t == 0 for j,t in enumerate(polys[k]) if j < (k+1)//2)
               for k in range(1,raw_limit+1)))
    for name,c in components.items():
        g = [sum((c[k]*(polys[k][j] if j<len(polys[k]) else 0)
                  for k in range(raw_limit+1)),F()) for j in range(10)]
        record(f'trace_full_LCM_{m}_{n}_{name}',
               all((L(2*j)**2*g[j]).denominator == 1 for j in range(10)))
        for t in range(4):
            record(f'trace_derivative_offset_{m}_{n}_{name}_{t}',
                   all((L(2*j+6)**2*F(factorial(j+t),factorial(j))*g[j+t]).denominator == 1
                       for j in range(7)))
        for exponent in [1,0,-1,-2,-3,-4]:
            terms=[]
            for j in range(1,7):
                index=j-exponent-1
                val=g[index]/j if index>=0 else F()
                terms.append((j*L(2*j+6)**2*val).denominator)
            record(f'trace_integral_staircase_{m}_{n}_{name}_{exponent}',
                   all(t == 1 for t in terms))


# Real five-term dilogarithm identity: both partial derivatives reduce to zero
# after the exact positive-argument log factorizations. No Li2 decimals.
X,Y=sp.symbols('X Y')
LX,LY,L1X,L1Y,L1XY=sp.symbols('LX LY L1X L1Y L1XY')
f4=X*(1-Y)/(1-X*Y)
f5=Y*(1-X)/(1-X*Y)
data=[(1,X,L1X),(1,Y,L1Y),(-1,X*Y,L1XY),
      (-1,f4,L1X-L1XY),(-1,f5,L1Y-L1XY)]
A=(1-X)/(1-X*Y)
B=(1-Y)/(1-X*Y)
for variable in [X,Y]:
    derivative=sum((-sign*log1*sp.diff(f,variable)/f for sign,f,log1 in data),sp.Integer(0))
    derivative-=sp.diff(A,variable)/A*(L1Y-L1XY)+(L1X-L1XY)*sp.diff(B,variable)/B
    record(f'five_term_partial_derivative_{variable}',sp.cancel(derivative)==0)
record('five_term_positive_factorizations',
       sp.cancel((1-f4)-A)==0 and sp.cancel((1-f5)-B)==0)
record('five_term_zero_boundary',
       f4.subs(Y,0)==X and f5.subs(Y,0)==0 and A.subs(Y,0)==1-X and B.subs(Y,0)==1)

m,n=sp.symbols('m n', positive=True)
rx=(n+1)/(n*(m+1))
ry=(m+1)/(m*(n+1))
record('five_rational_target_arguments',
       sp.cancel(rx*ry-1/(m*n))==0
       and sp.cancel(f4.subs({X:rx,Y:ry})-1/(m+1))==0
       and sp.cancel(f5.subs({X:rx,Y:ry})-1/(n+1))==0
       and sp.cancel(A.subs({X:rx,Y:ry})-m/(m+1))==0
       and sp.cancel(B.subs({X:rx,Y:ry})-n/(n+1))==0)
for N,allowed in [(999999,False),(1000000,True)]:
    ratio=F(1,N+1)
    record(f'adjacent_strict_threshold_{N}',(ratio<F(1,10**6))==allowed,
           absolute_ratio_difference=str(ratio), allowed=allowed)

sigma=[0,2,2]+[4]*14
flat=sum((F(2*i+1,17**2)*rate for i,rate in enumerate(sigma)),F())
sharp=F(78419,242760)  # Source v2 (14.5.3), not inferred by this script.
tau=flat+sharp
record('principal_staircase_weight',flat==F(1136,289),tau_flat=str(flat))
record('complete_denominator_rate',tau==F(1032659,242760),tau=str(tau))
R=arb(256*1287)/arb(2516)
margin=R.log()-arb(tau.numerator)/arb(tau.denominator)
bound=arb(10)/margin
record('strict_holonomy_denominator',margin>0,margin_ball=str(margin))
record('seventeen_function_contradiction',margin>arb(10)/arb(17) and bound<17,
       quotient_ball=str(bound), strict_rank=17,
       external_analytic_input='CDT v2 Appendix A.6: Bost-Charles integral <10')
record('naive_uniform_integration_type_fails_same_map',R.log()<5,
       uniform_type='L_(2j)^2 L_j, exponential rate 5',log_conformal_size_ball=str(R.log()))

report_path=HERE/'period_holonomy_cdt_mechanism_20261005.md'
source=HERE.parent/'literature/cdt2024_l2_chi_minus3.pdf'
payload={'status':'passed','date':'2026-10-05','checks':checks,'number_of_checks':len(checks),
         'source_arxiv':'2408.15403v2','source_pages':218,
         'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'report_sha256':hashlib.sha256(report_path.read_bytes()).hexdigest() if report_path.exists() else None,
         'external_inputs':['CDT Theorem C / 14.0.1','CDT Lemma 14.3.1 rank 17',
                            'CDT (14.5.3) fine integration cost',
                            'CDT Corollary 9.0.19 branch descent',
                            'CDT Appendix A.6 analytic contour integral <10'],
         'novelty_scope':'Explicit project corollary and verified bridge; no claim of global first discovery.',
         'not_claimed':['Independent reproof of CDT analytic quadrature',
                        'Irrationality of each of the five Li2 values',
                        'Extension to log 2 log 3 or products of three logs']}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','checks':len(checks),'holonomy_bound_ball':str(bound)},ensure_ascii=False))
