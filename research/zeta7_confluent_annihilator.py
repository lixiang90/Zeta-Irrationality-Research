"""Exact minimal-degree nuisance annihilator, avoiding ill-conditioned LP.

Solve a monic W of degree 2h-1 against the first 2h-1 zeta6 coefficient
moments. When 4h<=3K-1, zeta5 coefficients vanish by degree alone.
Coefficient positivity is checked exactly per case, not assumed universally.
"""
import json
from pathlib import Path
from flint import fmpq as Q, fmpq_mat, arb, arb_mat, ctx
from zeta7_confluent_gram_probe import coefficient_sequences, evaluate_exact, aq


def run(K,h):
    L=2*h-1
    assert 4*h<=3*K-1
    seqs=coefficient_sequences(K,L+2*h-2)
    M=fmpq_mat([[seqs[2][s+e] for e in range(L)] for s in range(L)])
    rhs=fmpq_mat(L,1,[-seqs[2][s+L] for s in range(L)])
    result=dict(K=K,h=h,annihilator_degree=L,zeta6_square_constraint_rank=M.rank())
    if M.det()==0:
        result['status']='singular_constraint_matrix'
        return result
    sol=M.inv()*rhs
    coeff=[sol[e,0] for e in range(L)]+[Q(1)]
    result['all_numerator_coefficients_positive']=all(c>0 for c in coeff)
    if all(c>=0 for c in coeff):
        result.update(evaluate_exact(K,h,coeff,seqs))
        result['status']='finite_exact_and_arb_checks_passed'
    else:
        result['status']='coefficient_positivity_not_available'
        result['rational_numerator']=list(map(str,coeff))
        entries=[[sum((seq[s+e]*c for e,c in enumerate(coeff)),Q(0))
                  for s in range(2*h-1)] for seq in seqs]
        assert all(v==0 for j in (1,2) for v in entries[j])
        ctx.prec=14000
        xi=arb(7).zeta()
        S=[[aq(entries[0][i+j])+xi*aq(entries[3][i+j]) for j in range(h)] for i in range(h)]
        signs=[]; pivots=[]
        for k in range(h):
            pivot=S[k][k]
            assert not pivot.contains(0)
            signs.append(1 if pivot>0 else -1)
            pivots.append(pivot.str(45))
            for i in range(k+1,h):
                for j in range(i,h):
                    S[i][j]-=S[i][k]*S[j][k]/pivot
                    S[j][i]=S[i][j]
        result.update(gram_ldl_signs=signs,gram_ldl_pivots=pivots,
                      gram_positive_definite=all(s==1 for s in signs),
                      gram_negative_definite=all(s==-1 for s in signs),
                      gram_indefinite=1 in signs and -1 in signs)
        from sympy import Poly, Rational, Symbol, oo
        t=Symbol('t')
        P=Poly.from_list([Rational(str(c)) for c in reversed(coeff)],t)
        result['numerator_positive_real_root_count']=int(P.count_roots(0,oo))
        if all(s==-1 for s in signs):
            for key in ('gram_ldl_signs','gram_ldl_pivots','gram_positive_definite',
                        'gram_negative_definite','gram_indefinite'):
                result['monic_'+key]=result.pop(key)
            result.update(evaluate_exact(K,h,[-c for c in coeff],seqs,require_nonnegative=False))
            result['signed_orientation']=-1
            result['gram_positive_definite']=True
            result['status']='finite_truncated_positive_exact_and_arb_checks_passed'
    print(K,h,result['status'],'score',result.get('normalized_log_primitive'),flush=True)
    return result


if __name__=='__main__':
    records=[run(K,K//2) for K in (2,4,6,8,12,16,24)]
    records += [run(K,K//3) for K in (12,24,36)]
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Exact finite monic-annihilator family. No universal coefficient positivity '
              'or asymptotic denominator/decay assertion.',records=records),indent=2),encoding='utf-8')
