"""Recompute polynomial certificates for the arithmetic-subspace experiments."""
import json
from math import gcd
from functools import reduce
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat, nmod_mat, arb, ctx
from arithmetic_subspaces import integer_pencil, adjugate_coefficients, radical, adjugate_conditions
from joint_exact import evaluate_primitive_ball

ROOT=Path(__file__).parent
JOBS=[(12,1,12),(24,1,24),(24,3,22)]


def polynomial(u,H):
    row=fmpq_mat(1,len(u),u)
    return fmpq_poly([(row*M*row.transpose())[0,0] for M in H])


def main():
    totals=dict(normal_records=0,invalid_after_saturation=0,admissible_selected=0,
                affine_families=0,affine_test_points=0,polynomial_recomputations=0,
                all_witnesses_worse_than_baseline=True)
    summary=[]
    for K,N,m in JOBS:
        normal=json.loads((ROOT/f'arithmetic_subspaces_K{K}_N{N}_m{m}.json').read_text())
        affine=json.loads((ROOT/f'affine_subspaces_K{K}_N{N}_m{m}.json').read_text())
        deep=json.loads((ROOT/f'affine_adjugate_K{K}_N{N}_m{m}.json').read_text())
        affine['rows']+=deep['rows']
        A,B,_=integer_pencil(K,N,m);det,H=adjugate_coefficients(A,B)
        _,deep_conditions,_=adjugate_conditions(H,m,K)
        deep_map=dict(deep_conditions)
        def condition_matrix(condition):
            p=condition['p']
            if condition.get('condition_kind')=='adjugate_kernel':
                return deep_map[p]
            return radical(A,B,p)[0]
        cdet,_,_=evaluate_primitive_ball(det)
        gadj=reduce(gcd,(abs(int(c.p)) for M in H for c in M.entries()),0)
        assert int(cdet.p)**(m-1)%gadj**m==0
        baseline=arb(normal['rows'][0]['score_ball']); unique=set()
        for row in normal['rows']+[x['witness'] for x in affine['rows']]:
            u=row['normal']; assert reduce(gcd,map(abs,u),0)==1
            P=polynomial(u,H)
            assert P==fmpq_poly([fmpq(x) for x in row['poly']])
            ct,lv,_=evaluate_primitive_ball(P)
            assert str(ct)==row['content']
            with ctx.workprec(160):
                assert abs(lv/K**2-arb(row['score_ball']))<arb('1e-27')
                if row['label']!='low_degree_baseline':
                    assert lv/K**2>baseline
            for constraint in row['local']:
                p=constraint['p'];R=condition_matrix(constraint)
                good=not R.transpose()*nmod_mat(m,1,[x%p for x in u],p)
                assert good==constraint['preserved_after_saturation']
            unique.add(tuple(u)); totals['polynomial_recomputations']+=1
        for row in normal['rows']:
            totals['normal_records']+=1
            if row['local'] and not all(c['preserved_after_saturation'] for c in row['local']):
                totals['invalid_after_saturation']+=1
            if 'admissible' in row['label']:
                totals['admissible_selected']+=1
        for row in affine['rows']:
            j=row['chart_coordinate'];cols=[k for k in range(m) if k!=j];n=m-1
            L=fmpq_mat(row['lattice_rows']);a=row['affine_point'];D=int(row['fixed_divisor'])
            assert a[j]==1 and abs(L.det())==int(row['index'])
            for z in [[0]*n,[int(i==0) for i in range(n)],[(-1)**i for i in range(n)]]:
                sub=fmpq_mat(1,n,[a[k] for k in cols])+fmpq_mat(1,n,z)*L
                u=[1 if k==j else int(sub[0,cols.index(k)]) for k in range(m)]
                P=polynomial(u,H)
                assert all(x.q==1 and int(x.p)%D==0 for x in P)
                for condition in row['witness']['local']:
                    p=condition['p'];R=condition_matrix(condition)
                    assert not R.transpose()*nmod_mat(m,1,[x%p for x in u],p)
                totals['affine_test_points']+=1
            with ctx.workprec(160):
                assert arb(row['witness']['score_ball'])<arb(row['existence_score_ball'])
                assert arb(row['existence_score_ball'])<arb(row['coarse_existence_score_ball'])
            assert row['witness_below_existence_bound'] and row['unresolved_fractional_parts']==0
            totals['affine_families']+=1
        admissible=[r for r in normal['rows'] if 'admissible' in r['label']]
        constrained=[r for r in affine['rows'] if r['label']!='unconstrained']
        summary.append(dict(K=K,N=N,m=m,h=m-1,unique_normalized_hyperplanes=len(unique),
                            baseline=normal['rows'][0]['score'],
                            best_admissible_lll=min(r['score'] for r in admissible),
                            best_affine_bound=min(r['existence_score'] for r in affine['rows']),
                            best_constrained_affine_bound=min(r['existence_score'] for r in constrained),
                            best_affine_witness=min(r['witness']['score'] for r in affine['rows']),
                            best_adjugate_bound=min(r['existence_score'] for r in deep['rows']),
                            selected_adjugate_conditions=[dict(p=p,rank=R.ncols()) for p,R in deep_conditions[:3]]))
    result=dict(totals=totals,configurations=summary)
    (ROOT/'arithmetic_subspaces_validation.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
