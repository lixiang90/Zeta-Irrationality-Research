"""Retain a block of exact pole zeros while optimizing a growing residual space.

The residual R(-x^2)/(d!)^2 is integer-valued. Q=B_(N,r) R, L=r+d.
Midpoints select candidates; exact determinant contents certify their scores.
"""
import argparse,json,math
from pathlib import Path
import mpmath as mp
from flint import fmpq,fmpq_poly,arb,ctx
from growing_integer_space import basis,coordinates,reduced_round
from rational_square_nodes import experiment
from integer_blocks import scalar
from joint_exact import Dcache


def run(K,N,L,retained):
    folder=Path(__file__).parent;data=json.loads((folder/f'growing_trace_certificate_K{K}.json').read_text())
    mp.mp.dps=230;A=mp.matrix([[mp.mpf(v) for v in row] for row in data['trace_metric_A_midpoint']]);b=mp.matrix([mp.mpf(v) for v in data['trace_metric_b_midpoint']])
    rows=[];P0=fmpq_poly(Dcache(N+L)//Dcache(N));h=K-N-L
    for r in retained:
        d=L-r;assert 0<r<L;fixed=fmpq_poly(Dcache(N+r)//Dcache(N))
        ds=[fixed*basis(i)*math.factorial(d)**2 for i in range(d)]
        cs=[]
        for v in ds:
            c=coordinates(v/math.factorial(L)**2);c+=[fmpq(0)]*(L-len(c));cs.append(c)
        C=mp.matrix([[mp.mpf(int(c.p))/int(c.q) for c in row] for row in cs]);Ar=C*A*C.T;br=C*b
        center=mp.lu_solve(Ar,-br);u,T,norm=reduced_round(Ar,center)
        S=scalar(K,N,[(N,r),(N+r,d)],h)
        for label,ui in [('prefix',[0]*d),('lll',u)]:
            Q=P0+sum((v*x for v,x in zip(ds,ui)),fmpq_poly([]));R=Q//fixed
            assert R*fixed==Q and all(c.q==1 for c in coordinates(R/math.factorial(d)**2))
            row=experiment(K,N,N+L,'integer',Q,f'retained_{r}_{label}')
            with ctx.workprec(160):
                gain=arb(S*fmpq(row['content'])).log()/K**2
                shift=arb(S/fmpq(row['scalar'])).log()/K**2
                row['real']+=float(shift.mid());row['real_ball']=(arb(row['real_ball'])+shift).str(30)
                row['arithmetic_gain']=float(gain.mid());row['scalar']=str(S)
            row.update(retained=r,dimension=d,parameters=[str(x) for x in ui])
            rows.append(row);print(json.dumps({k:row[k] for k in ['K','retained','dimension','label','score','real','arithmetic_gain']}),flush=True)
    (folder/f'retained_prefix_space_K{K}.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1);p.add_argument('--L',type=int,default=3);p.add_argument('--retained',default='1,2')
    a=p.parse_args();run(a.K,a.N,a.L,list(map(int,a.retained.split(','))))
