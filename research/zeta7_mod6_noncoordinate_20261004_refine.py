"""Bounded Macaulay refinement of the complete content certificates.

Reads the saved quadratic coefficient pencil; makes no determinant assumptions.
The integer identity C*M=d*I means every primitive normal has content dividing d.
"""
import argparse, itertools, json, math, sys, time
from pathlib import Path
from flint import fmpz_mat as ZMat, fmpq_mat as Mat, arb, arb_poly, arb_mat, ctx
from zeta7_mod6_noncoordinate_20261004 import certificate

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
PREFIX='zeta7_mod6_noncoordinate_20261004'
QUAD=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]

def mons(dim,degree):
    return [v for v in itertools.product(range(degree+1),repeat=dim) if sum(v)==degree]

def macaulay(B,exponents,degree):
    dim=len(exponents[0]);target=mons(dim,degree);index={e:i for i,e in enumerate(target)}
    factors=mons(dim,degree-2);rows=[];descriptions=[]
    for i,row in enumerate(B):
        for v in factors:
            out=[0]*len(target)
            for a,e in zip(row,exponents):
                out[index[tuple(x+y for x,y in zip(v,e))]]+=a
            rows.append(out);descriptions.append(dict(hnf_row=i,multiplier=list(v)))
    return rows,target,descriptions

def run(n,degrees):
    src=json.loads((ROOT/f'{PREFIX}_n{n}.json').read_text(encoding='utf-8'))
    cols=[[int(c) for c in row] for row in src['coefficient_columns']]
    ctx.prec=max(abs(v).bit_length() for col in cols for v in col)+src['K']**2+8000
    theta=arb(7).zeta();q=[arb_poly(c)(theta) for c in cols]
    M=arb_mat([[q[0],q[3]/2,q[4]/2],[q[3]/2,q[1],q[5]/2],[q[4]/2,q[5]/2,q[2]]])
    M2=arb_mat([[M[0,0],M[0,1]],[M[1,0],M[1,1]]])
    sigma=[M[0,0],M2.det()/M[0,0],M.det()/M2.det()]
    out=dict(n=n,K=src['K'],source=f'{PREFIX}_n{n}.json',strata=[])
    for j in (1,2):
        original=src['content_certificates'][j];inds=original['column_indices']
        B=[[int(v) for v in row] for row in original['hnf']]
        exps=[QUAD[i][:j+1] for i in inds];cases=[]
        for degree in degrees:
            start=time.perf_counter();rows,target,desc=macaulay(B,exps,degree)
            cert=certificate(rows);bound=sigma[j]/int(cert['content_upper'])
            cert.update(degree=degree,monomials=[list(e) for e in target],
                        row_descriptions=desc,lower_log_interval=bound.log().str(45),
                        lower_log=float(bound.log()),seconds=time.perf_counter()-start)
            cases.append(cert)
            print('K',src['K'],'stratum',j,'degree',degree,'logd',cert['log_content_upper'],
                  'lower',cert['lower_log'],'seconds',cert['seconds'],flush=True)
        best=min([original]+cases,key=lambda c:int(c['content_upper']))
        out['strata'].append(dict(stratum=j,cases=cases,best_content_upper=best['content_upper'],
                                 best_lower_log=float((sigma[j]/int(best['content_upper'])).log())))
    out['global_family_lower_log']=min(src['content_certificates'][0]['lower_log'],
                                      *(x['best_lower_log'] for x in out['strata']))
    out['baseline_log']=src['baseline']['log_primitive']
    out['uniformly_above_baseline']=out['global_family_lower_log']>out['baseline_log']
    (ROOT/f'{PREFIX}_refine_n{n}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    return dict(n=n,K=src['K'],global_family_lower_log=out['global_family_lower_log'],
                baseline_log=out['baseline_log'],uniformly_above_baseline=out['uniformly_above_baseline'])

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--n',type=int,nargs='+',default=[1,2])
    parser.add_argument('--degrees',type=int,nargs='+',default=[3,4]);args=parser.parse_args()
    results=[]
    for n in args.n:results.append(run(n,args.degrees))
    (ROOT/f'{PREFIX}_refine.json').write_text(json.dumps(dict(status='complete',cases=results),indent=2),encoding='utf-8')
