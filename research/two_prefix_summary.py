"""Audit saved two-prefix data and independently certify selected winners."""
import json
from pathlib import Path
from math import lcm
from flint import fmpq, fmpq_poly, fmpz_mat, ctx, arb
from two_prefix_outer import vp, outer_bound
from joint_exact import entries, content, norm_scalar, evaluate_primitive_ball

ROOT=Path(__file__).parent


def run():
    totals=dict(exact_records=0,unique_configurations=0,local_checks=0,local_equalities=0,
                nontrivial_local_checks=0,nontrivial_local_equalities=0,interpolation_points=0)
    summary=[];keys=set();counterexamples=[]
    for K in [24,48,72,96]:
        data=json.loads((ROOT/f'two_prefix_outer_K{K}.json').read_text())['rows']
        controls=json.loads((ROOT/f'two_prefix_controls_K{K}.json').read_text())['rows']
        assert len(data)==(15 if K==24 else 11) and len(controls)==6
        for row in data+controls:
            N,M,h=row['N'],row['M'],row['h'];keys.add((K,N,M,h))
            P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']]);ct=fmpq(row['content'])
            assert content(P)==1
            assert P.degree()==min(h,K-M)
            _,lv,_=evaluate_primitive_ball(P)
            normct=ct*norm_scalar(K,[(N,6),(M,2)],h)
            assert normct==fmpq(row['normalized_content'])
            with ctx.workprec(160):
                assert abs(lv/K**2-arb(row['score_ball']))<arb('1e-27')
                assert abs(arb(normct).log()/K**2-arb(row['arithmetic_gain_ball']))<arb('1e-27')
                assert abs((lv+arb(normct).log())/K**2-arb(row['real_ball']))<arb('1e-27')
            for q in row['local']:
                p=q['p'];low=outer_bound(K,N,M,h,p)
                actual=min(vp(c*ct,p) for c in P if c)
                assert actual==q['actual']==vp(ct,p) and actual>=low['lower']==q['lower']
                totals['local_checks']+=1;totals['local_equalities']+=int(actual==low['lower'])
                if low['lower']<0:
                    totals['nontrivial_local_checks']+=1
                    totals['nontrivial_local_equalities']+=int(actual==low['lower'])
                if h==K-N:
                    wrong_rank=min(h,max(0,K+6*N-3*p+3))
                    wrong_lower=low['base']-min(wrong_rank,low['zero_weights'])
                    if wrong_lower>actual:
                        counterexamples.append(dict(K=K,N=N,M=M,h=h,p=p,
                                                    wrong_lower=wrong_lower,actual=actual,
                                                    corrected_lower=low['lower']))
            totals['exact_records']+=1
        best=min(data,key=lambda r:r['score'])
        same=next(r for r in controls if r['h']==best['h'])
        original=next(r for r in controls if r['h']==K-best['N'])
        fixed_h=next(r for r in data if r['M']==2*r['N'] and r['h']==K-r['N'])
        assert best['h']==K-best['M']
        with ctx.workprec(160):
            real_cost=arb(best['real_ball'])-arb(same['real_ball'])
            arithmetic_gain=arb(best['arithmetic_gain_ball'])-arb(same['arithmetic_gain_ball'])
            improvement=arb(same['score_ball'])-arb(best['score_ball'])
            assert real_cost>0 and improvement>0
            assert abs(arithmetic_gain-real_cost-improvement)<arb('1e-27')
            comparison=dict(K=K,N=best['N'],M=best['M'],h=best['h'],degree=best['degree'],
                            original=original['score'],previous_M2N=fixed_h['score'],
                            candidate=best['score'],same_dimension_control=same['score'],
                            real_cost=float(real_cost.mid()),arithmetic_gain=float(arithmetic_gain.mid()),
                            improvement=float(improvement.mid()),improvement_ball=improvement.str(30))
        # h=K-M: nonzero pole Gram determinant gives degree at most h.
        # h+1 exact full Hankel determinants independently determine it.
        N,M,h=best['N'],best['M'],best['h']
        P=fmpq_poly([fmpq(c) for c in best['primitive_polynomial']])*fmpq(best['content'])
        aa,bb=entries(K,[(N,6),(M,2)],h)
        den=lcm(*(int(x.q) for x in aa+bb))
        A=fmpz_mat(h,h,[int(aa[i+j]*den) for i in range(h) for j in range(h)])
        B=fmpz_mat(h,h,[int(bb[i+j]*den) for i in range(h) for j in range(h)])
        print('full polynomial check',K,N,M,h,flush=True)
        for x in range(h+1):
            assert (A+B*x).det()==P(x)*den**h
            totals['interpolation_points']+=1
        summary.append(comparison);print(json.dumps(comparison),flush=True)
    totals['unique_configurations']=len(keys)
    crt=json.loads((ROOT/'two_prefix_crt_validation.json').read_text())
    totals['crt_certificates']=len(crt)
    totals['entrywise_inequalities']=sum(r['coefficient_entry_inequalities'] for r in crt)
    result=dict(totals=totals,comparisons=summary,
                incorrect_old_moment_rank_counterexamples=counterexamples)
    (ROOT/'two_prefix_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(totals),flush=True)
    return result


if __name__=='__main__':run()
