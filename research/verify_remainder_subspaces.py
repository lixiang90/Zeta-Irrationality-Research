"""Independent algebraic checks of the new subspace experiment engines."""
import json
import math
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, arb
from joint_exact import entries, determinant, evaluate_primitive_ball
from mixed_subspaces import run, interpolation, determinant_matrices
from partial_vanishing import basis, run_design

HERE=Path(__file__).parent


def minor(M,rows,cols):
    return fmpq_mat(len(rows),len(cols),[M[i,j] for i in rows for j in cols])


def main():
    tests=[]
    # Actual different subspaces, compared against independent Newton interpolation.
    for K,profile,E,G in [(8,[(1,4)],[0,1,4,5],[0,1,2,3]),
                          (9,[(1,2),(2,3)],[0,2,3,5],[0,1,4,5])]:
        r,P,A,B=run(K,profile,E,G)
        assert P==interpolation(A,B)
        tests.append(dict(kind='mixed_interpolation',K=K,h=len(E),passed=True))
    # Gap zero is an honest monic basis change: no new primitive polynomial.
    for mode in ['mixed','symmetric']:
        K=12;h=10;profile=[(1,4),(2,2)]
        aa,bb=entries(K,profile,h);Pold=determinant(aa,bb,h)
        _,P,A,B=run_design(K,profile,h,4,0,mode)
        assert P==Pold and P==interpolation(A,B)
        tests.append(dict(kind='zero_gap_identity',mode=mode,passed=True))
    # Explicit Cauchy-Binet expansion. Coefficient maximal minors are nonnegative
    # and one is 1; mixed and symmetric determinants are checked as polynomials.
    K=8;h=4;r=2;gap=2;H=h+gap;profile=[(1,4)]
    aa,bb=entries(K,profile,H)
    A=fmpq_mat(H,H,[aa[i+j] for i in range(H) for j in range(H)])
    B=fmpq_mat(H,H,[bb[i+j] for i in range(H) for j in range(H)])
    C=fmpq_mat(h,H,[p[j] for p in basis(h,r,r+gap) for j in range(H)])
    subsets=list(combinations(range(H),h));co={I:minor(C,range(h),I).det() for I in subsets}
    assert all(c>=0 for c in co.values()) and any(c==1 for c in co.values())
    for mode in ['mixed','symmetric']:
        rhs=fmpq_poly([0]);terms=0
        right=co if mode=='symmetric' else {tuple(range(h)):fmpq(1)}
        for I,c in co.items():
            for J,d in right.items():
                if c and d:
                    rhs+=c*d*determinant_matrices(minor(A,I,J),minor(B,I,J));terms+=1
        _,P,*_=run_design(K,profile,h,r,gap,mode)
        assert P==rhs
        tests.append(dict(kind='Cauchy_Binet_polynomial_identity',mode=mode,terms=terms,passed=True))
    # Interval certificates of selected large fixed-ratio polynomials already
    # exist; recompute the local content once through the independent exact P.
    from eight_pole_probe import check
    from joint_padic import val
    data=json.loads((HERE/'remainder_cache_K120_N3.json').read_text())
    P=fmpq_poly([fmpq(c) for c in data['poly']]);row=check(120,3,29,12)
    assert min(val(c,29) for c in P)==row['gauss']
    tests.append(dict(kind='local_gauss_vs_all_exact_coefficients',K=120,N=3,p=29,passed=True))
    summaries=[]
    for name in ['mixed_subspaces24.json','mixed_subspaces48.json','partial_vanishing24.json','partial_vanishing48.json']:
        rows=json.loads((HERE/name).read_text())
        for row in rows:
            assert row['positive_primitive_value'] and arb(row['score_ball'])>0
        baseline={}
        for r in rows:
            if r.get('gap',r['partition_area_E']+r['partition_area_F'])==0:
                baseline[(str(r['profile']),r['h'])]=r
        changes=[r['score']-baseline[(str(r['profile']),r['h'])]['score'] for r in rows
                 if r.get('gap',r['partition_area_E']+r['partition_area_F'])>0]
        assert min(changes)>0
        assert all(arb(r['score_ball'])>arb(baseline[(str(r['profile']),r['h'])]['score_ball'])
                   for r in rows if r.get('gap',r['partition_area_E']+r['partition_area_F'])>0)
        summaries.append(dict(file=name,cases=len(rows),genuine_subspace_changes=len(changes),
                              min_score=min(r['score'] for r in rows),
                              min_per_lambda=min(r['score_per_lambda'] for r in rows),
                              min_score_increase_vs_matched_baseline=min(changes)))
    gains=[]
    for alpha in [F(1,200),F(1,100),F(1,66),F(1,40),F(1,33)]:
        q4=5*alpha*max(F(0),1-33*alpha)/36
        # Conditional only: assumes the same 5N leading gain for EVERY q>=4.
        qmax=math.floor((1/alpha-1)/8)
        hypothetical=sum((5*alpha*(1-(8*q+1)*alpha)/(q*(2*q+1)) for q in range(4,qmax+1)),F(0))
        gains.append(dict(alpha=str(alpha),conditional_q4_gain=str(q4),
                          hypothetical_all_q_gain=str(hypothetical),qmax=qmax))
    assert next(r for r in gains if r['alpha']=='1/40')['conditional_q4_gain']=='7/11520'
    grid=json.loads((HERE/'eight_pole_grid.json').read_text())
    large=json.loads((HERE/'eight_pole_large.json').read_text())
    for r in grid+large:
        assert r['gauss_certified'] and r['fixed_integrality_checked'] and r['slack']>=0
        assert r['first_nullity']>=3*r['N']+1 and r['second_nullity']>=2*r['N']+1
    census=dict(grid_cases=len(grid),grid_equalities=sum(r['slack']==0 for r in grid),
                large_cases=len(large),large_equalities=sum(r['slack']==0 for r in large),
                first_and_second_layer_targets_pass=True)
    result=dict(tests=tests,experiments=summaries,conditional_gains=gains,new_window_census=census,
                warning='Finite checks do not prove the conjectured inner-window bound. No global arithmetic constant has been reduced by these conditional gains.')
    (HERE/'remainder_subspaces_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
