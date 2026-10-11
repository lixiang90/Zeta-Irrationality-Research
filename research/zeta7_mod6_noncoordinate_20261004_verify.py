"""Independent verifier for the saved exact pencil and content identities.

Checks identities from the saved integers, not floating scores; re-evaluates
all primitive polynomials with Arb; checks selected large-parameter determinants.
"""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_mat as Mat, fmpz_mat as ZMat, arb, arb_poly, arb_mat, ctx
from sympy import primerange
from zeta7_mod6_noncoordinate_20261004 import setup, restricted, kernel

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
PREFIX='zeta7_mod6_noncoordinate_20261004'
QUAD=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]

def integers(rows):return ZMat([[int(v) for v in row] for row in rows])

def check_certificate(rows,cert):
    F=integers(rows);B=integers(cert['hnf']);U=integers(cert['coefficient_to_hnf'])
    C=integers(cert['integer_identity_multiplier']);d=int(cert['content_upper'])
    m=F.ncols()
    assert U*F==B
    assert C*F==ZMat([[d if i==j else 0 for j in range(m)] for i in range(m)])
    coordinates=Mat(F)*Mat(B).inv()
    assert all(v.denominator==1 for v in coordinates.entries())
    assert d==math.lcm(*(int(v.denominator) for v in Mat(B).inv().entries()))
    return m*F.nrows()+m*m

def local_cap(d,K):
    remaining=d;vals=[]
    for p in primerange(2,K+1):
        e=0
        while remaining%p==0:remaining//=p;e+=1
        if e:vals.append(dict(prime=p,valuation=e,log_contribution=e*math.log(p)))
    return dict(primes_at_most_K=vals,residual=str(remaining),residual_log=math.log(remaining))

def run(n):
    data=json.loads((ROOT/f'{PREFIX}_n{n}.json').read_text(encoding='utf-8'))
    refine=json.loads((ROOT/f'{PREFIX}_refine_n{n}.json').read_text(encoding='utf-8'))
    cols=[[int(v) for v in c] for c in data['coefficient_columns']]
    assert math.gcd(*(x for c in cols for x in c))==1
    ctx.prec=max(abs(v).bit_length() for c in cols for v in c)+data['K']**2+10000
    theta=arb(7).zeta();q=[arb_poly(c)(theta) for c in cols]
    M=arb_mat([[q[0],q[3]/2,q[4]/2],[q[3]/2,q[1],q[5]/2],[q[4]/2,q[5]/2,q[2]]])
    M2=arb_mat([[M[0,0],M[0,1]],[M[1,0],M[1,1]]])
    assert M[0,0]>0 and M2.det()>0 and M.det()>0
    sigma=[M[0,0],M2.det()/M[0,0],M.det()/M2.det()]
    count=0;ds=[]
    for j,cert in enumerate(data['content_certificates']):
        inds=cert['column_indices'];rows=[[cols[i][e] for i in inds] for e in range(len(cols[0]))]
        count+=check_certificate(rows,cert);d=int(cert['content_upper'])
        if j:
            improved=refine['strata'][j-1]
            for lift in improved['cases']:
                target=[tuple(e) for e in lift['monomials']];idx={e:i for i,e in enumerate(target)}
                rows=[];B=[[int(v) for v in row] for row in cert['hnf']]
                for desc in lift['row_descriptions']:
                    row=[0]*len(target);v=desc['multiplier']
                    for a,i in zip(B[desc['hnf_row']],inds):
                        e=tuple(x+y for x,y in zip(v,QUAD[i][:j+1]));row[idx[e]]+=a
                    rows.append(row)
                count+=check_certificate(rows,lift);d=math.gcd(d,int(lift['content_upper']))
        ds.append(d)
    bounds=[sigma[j]/ds[j] for j in range(3)];logs=[x.log() for x in bounds]
    floor=min(int(x.floor().unique_fmpz()) for x in logs)
    assert all(x>floor for x in logs) and floor>0
    base=arb_poly([int(v) for v in data['baseline']['primitive_coefficients']])(theta)
    assert base>0
    assert all(logs[j]-base.log()>0 for j in (0,1))
    rows=[]
    for row in data['candidates']:
        u=[int(v) for v in row['normal']];assert math.gcd(*u)==1
        x,y,z=u;mons=[x*x,y*y,z*z,x*y,x*z,y*z]
        coeff=[sum(cols[j][e]*mons[j] for j in range(6)) for e in range(len(cols[0]))]
        g=math.gcd(*coeff);assert str(g)==row['content']
        value=arb_poly([v//g for v in coeff])(theta);assert value>0
        assert value.log().overlaps(arb(row['log_primitive_interval']))
        assert value>base
        rows.append((value,row,u))
    genuine=[x for x in rows if sum(v!=0 for v in x[2])>=2]
    best=min(rows,key=lambda x:float(x[0].log()))
    bestg=min(genuine,key=lambda x:float(x[0].log()))
    assert all(value>=best[0] or value.overlaps(best[0]) for value,_,_ in rows)
    # Reconstruct source Gram matrices and verify the large LLL-directed normal.
    _,A,B,_,_=setup(n);u=bestg[2];ks=kernel(u);a,b=restricted(A,ks),restricted(B,ks)
    x,y,z=u;mons=[x*x,y*y,z*z,x*y,x*z,y*z]
    c=[sum(cols[j][e]*mons[j] for j in range(6)) for e in range(len(cols[0]))]
    factor=Q(data['common_rational_factor'])
    for point in (-1,0,1):
        evaluation=sum((Q(v)*point**e for e,v in enumerate(c)),Q(0))
        assert factor*evaluation==(a+point*b).det()
    return dict(n=n,K=data['K'],dimension=data['dimension'],integer_identity_checks=count,
                rigorous_global_log_floor=floor,
                refined_log_bounds=[x.str(42) for x in logs],
                u2_zero_above_baseline=(logs[1]-base.log()).str(42),
                content_caps=[dict(stratum=j,content_upper=str(d),local=local_cap(d,data['K'])) for j,d in enumerate(ds)],
                candidate_count=len(rows),all_candidates_above_baseline=True,
                best_candidate=best[1],best_genuine_noncoordinate=bestg[1],
                large_normal_det_checks=dict(normal=u,points=[-1,0,1]))

if __name__=='__main__':
    out=dict(status='independently_verified',cases=[run(n) for n in (1,2)])
    (ROOT/f'{PREFIX}_verify.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    for c in out['cases']:
        print('K',c['K'],'integer checks',c['integer_identity_checks'],
              'global log >',c['rigorous_global_log_floor'],'best noncoordinate',
              c['best_genuine_noncoordinate']['normal'],
              c['best_genuine_noncoordinate']['log_primitive'],flush=True)
