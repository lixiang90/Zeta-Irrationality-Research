"""Joint lattice-preservation certificates for A+delta*D+X*B.

If A_c^-1 D and A_c^-1 B are integral, then det(A+delta D+XB)/det(A_c)
is a polynomial with integral coefficients in delta-c and X. This covers
all p-integral parameter specializations without inverting special minors.
"""
import json,time,argparse
from pathlib import Path
from coupled_pencil import raw_pencil,vp_mod
from joint_padic import hungarian
from coupled_schur import integral_solve_certificate,counts
from distribution_modular import smith_mod
from coupled_candidate_law import prediction


def data(K,N,p,precision=10,padding=12):
    raws=[raw_pencil(K,N,p,precision+padding,harmonic_deformation=d) for d in [0,1]]
    shift=max(z['shift'] for z in raws);L=shift+precision+padding;modulus=p**L;h=K-N
    def scaled(z,key):
        factor=p**(shift-z['shift'])
        return [[int(z[key][i,j])*factor%modulus for j in range(h)] for i in range(h)]
    A=scaled(raws[0],'A');A1=scaled(raws[1],'A');B=scaled(raws[0],'B')
    assert B==scaled(raws[1],'B')
    D=[[(A1[i][j]-A[i][j])%modulus for j in range(h)] for i in range(h)]
    cost=[[min(vp_mod(M[i][j],p,L) for M in [A,B,D])-shift for j in range(h)] for i in range(h)]
    u,v,T=hungarian(cost)
    if max(u)+max(v)>padding:return data(K,N,p,precision,2*padding+max(u)+max(v))
    def norm(M):
        out=[]
        for i in range(h):
            row=[]
            for j in range(h):
                e=shift+u[i]+v[j];z=M[i][j]
                if e>=0:
                    assert L-e>=precision and z%p**e==0
                    z//=p**e
                else:z*=p**(-e)
                row.append(z%p**precision)
            out.append(row)
        return out
    return dict(A=norm(A),B=norm(B),D=norm(D),tropical=T,precision=precision)


def certify(K,N,p):
    z=data(K,N,p);h=K-N;precision=z['precision'];modulus=p**precision
    trials=[];pre=prediction(K,N,p)
    for c in [0,1,2,3,4]:
        A=[[(z['A'][i][j]+c*z['D'][i][j])%modulus for j in range(h)] for i in range(h)]
        ss,censored,_=smith_mod(A,p,precision)
        assert not censored
        certB=integral_solve_certificate(A,z['B'],p,precision)
        certD=integral_solve_certificate(A,z['D'],p,precision)
        trial=dict(center=c,valuation=z['tropical']+sum(ss),smith_counts=counts(ss),
                   B_integral=certB['certified'],D_integral=certD['certified'],
                   B_margin=certB['row_margin'],D_margin=certD['row_margin'])
        trials.append(trial)
        if certB['certified'] and certD['certified']:break
    ok=trials[-1]['B_integral'] and trials[-1]['D_integral']
    return dict(K=K,N=N,p=p,target=pre['gauss'],tropical=z['tropical'],
                joint_lattice_certified=ok,
                uniform_lower=trials[-1]['valuation'] if ok else None,trials=trials)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='32:4:11,38:5:13,50:6:17,68:8:23,128:16:43,158:18:53,176:22:59,248:31:83')
    ap.add_argument('--out',default='parameter_lattice.json');args=ap.parse_args()
    out=Path(__file__).with_name(args.out);rows=[];start=time.time()
    for item in args.pairs.split(','):
        r=certify(*map(int,item.split(':')));rows.append(r)
        out.write_text(json.dumps(dict(rows=rows),indent=2))
        print(json.dumps(r)+f' elapsed={time.time()-start:.1f}s',flush=True)
