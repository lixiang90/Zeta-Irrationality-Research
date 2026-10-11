"""Monic integer-valued polynomial pencils, squared to preserve positivity."""
import argparse,json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx
from joint_exact import (Dcache,entries_from_polynomial,determinant_pole_split,
                         evaluate_primitive_ball)
from integer_blocks import scalar


def numerator(N,L,s,u):
    P0=Dcache(N+L)//Dcache(N);P1=Dcache(N+s+L)//Dcache(N+s)
    return P0+u*(P1-P0)


def experiment(K,N,L,s,u):
    Q=numerator(N,L,s,u);W=Dcache(N)**8*Q**2;t=fmpq_poly([0,1]);T=fmpq_poly([1])
    removed=[]
    for j in range(1,K+1):
        if W(-j*j):T*=t+j*j
        else:removed.append(j)
    h=K-N-L;aa,bb=entries_from_polynomial(K,W,h)
    P=determinant_pole_split(aa,bb,T,h);ct,lv,bits=evaluate_primitive_ball(P)
    S=scalar(K,N,[(N,L)],h)
    with ctx.workprec(160):
        lc=arb(S*ct).log()/K**2;score=lv/K**2;real=score+lc
        return dict(K=K,N=N,L=L,s=s,u=u,h=h,degree=P.degree(),removed=removed,
                    numerator=[str(c) for c in Q],content=str(ct),scalar=str(S),
                    score=float(score.mid()),score_ball=score.str(30),
                    real=float(real.mid()),real_ball=real.str(30),
                    arithmetic_gain=float(lc.mid()),arithmetic_gain_ball=lc.str(30),
                    primitive_polynomial=[str(c) for c in P/ct])


def main():
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1)
    p.add_argument('--L',type=int,default=3);p.add_argument('--shifts',default='1,2,4,8')
    p.add_argument('--parameters',default='-4,-3,-2,-1,0,1,2,3,4');a=p.parse_args()
    path=Path(__file__).with_name(f'integer_block_pencils_K{a.K}.json');rows=[]
    for s in map(int,a.shifts.split(',')):
        for u in map(int,a.parameters.split(',')):
            row=experiment(a.K,a.N,a.L,s,u);rows.append(row)
        path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        best=min(rows,key=lambda r:r['score'])
        print(json.dumps(dict(K=a.K,rows=len(rows),best={k:best[k] for k in ('s','u','score','real','arithmetic_gain')})),flush=True)


if __name__=='__main__':main()
