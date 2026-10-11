"""Test the repeated-root direction at matched numerator degree and dimension.

W=D_N^4 D_A^2 D_B^2, A+B=5N; h=K-4N. A>=N. The original
two-prefix baseline is A=N, B=4N. This overlaps root blocks, so the
disjoint-block local bounds are not used.
"""
import argparse
import json
from pathlib import Path
from flint import arb, ctx
from joint_exact import experiment, content


def run(scales):
    path=Path(__file__).with_suffix('.json');rows=[]
    for K,N in scales:
        base_ct=None;base_value_log=None
        for A in range(N,(5*N)//2+1):
            B=5*N-A;h=K-4*N
            r,P,aa,bb=experiment(K,[(N,4),(A,2),(B,2)],h)
            ct=content(P)
            with ctx.workprec(160):
                log_value=arb(r['score_ball'])*K**2+arb(ct).log()
                if A==N:base_ct=ct;base_value_log=log_value
                real_change=(log_value-base_value_log)/K**2
                content_change=arb(ct/base_ct).log()/K**2
            r.update(N=N,A=A,B=B,content=str(ct),raw_polynomial=list(map(str,P)),
                     matched_raw_real_change_ball=real_change.str(30),content_gain_ball=content_change.str(30))
            rows.append(r);path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
            print(json.dumps({k:r[k] for k in ['K','N','A','B','score','score_ball','matched_raw_real_change_ball','content_gain_ball']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--scales',default='24:1,48:2,72:3,96:4');a=p.parse_args()
    run([tuple(map(int,s.split(':'))) for s in a.scales.split(',')])
