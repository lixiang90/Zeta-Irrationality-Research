"""Exact inputs for the explicit log-moment candidate.

No assertion here proves the special endpoint integrals nonzero or small.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, factorial, gcd
import hashlib
import json
import sys
import sympy as S

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).with_suffix('.json')
u,z=S.symbols('u z')
cases=[]
for n,q,k in [(1,1,2),(2,2,2),(1,6,7),(1,7,7),(2,7,7)]:
    N=n*q
    coeff=[(-1)**r*comb(N,r)*comb(n+r,n)**q for r in range(N+1)]
    R=sum(c*u**r for r,c in enumerate(coeff))
    mellin=sum(c/(z+r) for r,c in enumerate(coeff))
    formula=(-1)**N*S.Rational(factorial(N),factorial(n)**q)*S.prod((z-j)**q for j in range(1,n+1))/S.prod(z+r for r in range(N+1))
    assert S.cancel(mellin-formula)==0
    moment_count=0
    for m in range(n):
        for j in range(q):
            moment=sum((Fraction(c,(m+r+1)**(j+1)) for r,c in enumerate(coeff)),Fraction())
            assert moment==0,(n,q,m,j,moment)
            moment_count+=1
    Q,B=S.div(R,u+1,u)
    assert all(c.q==1 for c in S.Poly(Q,u).all_coeffs())
    bound=sum(abs(c) for c in coeff)
    assert B==bound and B>0
    rational=sum((Fraction(int(c),(exp[0]+1)**k) for exp,c in S.Poly(Q,u).terms()),Fraction())
    M=rational.denominator;r=rational.numerator
    C=(1<<(k-1))-1;D=1<<(k-1)
    target_coef=M*int(B)*C
    rational_coef=D*r
    content=gcd(abs(target_coef),abs(rational_coef))
    assert content<=D*int(B)*C
    L=1
    for v in range(1,N+1): L=S.ilcm(L,v)
    assert int(L)**k % M==0
    top_moments=None
    if q>=k:
        top_moments=[str(sum((Fraction(c,(m+t+1)**k) for t,c in enumerate(coeff)),Fraction())) for m in range(n)]
        assert all(value=='0' for value in top_moments)
        kernel=S.cancel(1/(1+u)-sum((-u)**m for m in range(n))-(-u)**n/(1+u))
        assert kernel==0
    cases.append({
        'n':n,'q':q,'weight':k,'degree':N,'coefficients':coeff,
        'Mellin_identity_exact':True,'vanishing_moment_count':moment_count,
        'R_minus1':int(B),'rational_part':str(rational),'least_rational_denominator':M,
        'integer_pair_for_zeta':{'target_coefficient':target_coef,'rational_coefficient':rational_coef,
                                'full_gcd':content,'primitive_target_coefficient':target_coef//content,
                                'primitive_rational_coefficient':rational_coef//content},
        'uniform_L_N_power_clears':True,'top_moments_if_q_ge_weight':top_moments
    })
report=ROOT/'research/odd_zeta_log_moment_candidate_20261004.md'
v={
    'status':'exact_candidate_inputs_passed','as_of':'2026-10-04','cases':cases,
    'written_proof_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),
    'all_scale_claims_from_written_proof':[
        'Residue computation of the rational Mellin transform',
        'Zeros of multiplicity q at 1,...,n and all log moments',
        'One-dimensional solution space and integer normalization',
        'Exact pure zeta reduction and finite kernel decomposition for q>=weight'
    ],
    'not_claimed':[
        'Endpoint integral nonzero for every n',
        'Exponential decay or negative primitive budget',
        'Actual denominator exponent for the whole candidate family',
        'Irrationality theorem or new Lean formalization'
    ]
}
OUT.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':v['status'],'cases':len(cases),'vanishing_moments':sum(c['vanishing_moment_count'] for c in cases)},ensure_ascii=False))

