"""Independent audits of the new finite certificates and algebraic model."""
import json
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq,fmpq_poly,nmod_poly,nmod_mat
from sympy import primerange
from adjacent_inner_scan import run
from joint_exact import content,Dcache
from joint_padic import val
from inner_window_budget import gain,upper_gain
from eight_local_scalar import rational_model

HERE=Path(__file__).parent


def candidate(row):
    p,N,r,q,K=(row[k] for k in ['p','N','r','q','K'])
    loss=min(2*N+1,max(0,6*N+r-p+3))
    return (14*q-2)*N+5*min(N,r)-7*K+6*q-1-loss


def main():
    rows=json.loads((HERE/'adjacent_inner_scan.json').read_text())+json.loads((HERE/'adjacent_inner_large.json').read_text())
    low=[r for r in rows if r['r']<=(r['p']-1)//2]
    assert all(r['gauss_certified'] and r['gauss']>=candidate(r) for r in low)
    fixed=[r for r in low if r.get('fixed_integral')]
    assert all(r['first']>=3*r['N']+1 and r['second']>=max(0,min(2*r['N']+1,r['p']-r['r']-4*r['N']-2)) for r in fixed)
    upper=[r for r in rows if 1<=r['p']-r['r']<=r['N']]
    for r in upper:
        a=r['p']-r['r'];target=68*r['N']-7*r['K']-6*a+30
        assert r['gauss']>=target
    repeated=json.loads((HERE/'adjacent_inner_repeated.json').read_text())
    assert all(r['gauss']>=candidate(r) for r in repeated)
    full=[]
    for filename,p in [('remainder_cache_K120_N3.json',29),('remainder_cache_K160_N4.json',37),('remainder_cache_K160_N4.json',31)]:
        data=json.loads((HERE/filename).read_text());K=data['result']['K'];N=data['result']['profile'][0][0]
        P=fmpq_poly([fmpq(x) for x in data['poly']]);ct=content(P)
        assert str(ct)==data['content']
        row=run(p,N,K%p,K//p);exact=min(val(c,p) for c in P if c)
        assert row['gauss']==exact==val(ct,p) and exact>=candidate(row)
        full.append(dict(K=K,N=N,p=p,exact_all_coefficients_gauss=exact,modular_gauss=row['gauss'],candidate=candidate(row)))
    rank_checks=0
    for p in primerange(11,44):
        t=nmod_poly([0,1],p);Fpoly=nmod_poly([int(v)%p for v in Dcache((p-1)//2)],p)
        for N in range(1,min(6,(p-1)//2)+1):
            n=3*N+1
            for r in range(N,(p-1)//2+1):
                delta=6*N+r-p+3
                if delta>2*N+1:continue
                dr=nmod_poly([int(v)%p for v in Dcache(r)],p)
                mm=[int((dr*t**k%(Fpoly**2))[p-2]) for k in range(2*n-1)]
                L=nmod_mat(n,n,[mm[i+j] for i in range(n) for j in range(n)],p)
                assert L.rank()==max(0,delta)
                rank_checks+=1
    schur=json.loads((HERE/'eight_schur_probe.json').read_text());good=[r for r in schur if r.get('symmetric')]
    assert all(r['independent_rational_scalar_verified'] and r['evaluation_weights_diagonal'] and r['second_lifts_verified']
               and r['X_coefficients_divisible_by_p2'] for r in good)
    assert gain(F(1,40),4,True)['gain']=='13571/5184000'
    assert gain(F(1,40),4,False)['gain']=='4963/2592000'
    assert F(upper_gain(F(1,40))['gain'])==F(7,16000)
    out=dict(status='All checks passed; uniform determinant localization remains unproved.',
        q4_scan_count=len(rows),q4_lower_half_count=len(low),q4_lower_half_equalities=sum(r['gauss']==candidate(r) for r in low),
        fixed_weight_count=len(fixed),upper_slice_count=len(upper),
        repeated_count=len(repeated),repeated_q_at_least4=sum(r['q']>=4 for r in repeated),
        repeated_q_at_least4_equalities=sum(r['q']>=4 and r['gauss']==candidate(r) for r in repeated),
        full_polynomial_cross_checks=full,laurent_rank_checks=rank_checks,
        schur_count=len(schur),schur_model_verified=len(good),
        singular_complements=[{k:r[k] for k in ['p','N','r','unit_rank','eliminated']} for r in schur if not r.get('symmetric')],
        rational_scalar=str(rational_model()[0]),
        lower_half_conditional_gain='13571/5184000',upper_slice_conditional_gain='7/16000')
    (HERE/'inner_window_extension_validation.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out),flush=True)


if __name__=='__main__':main()
