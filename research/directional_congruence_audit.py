"""Rigorous trace bounds and finite content witnesses for directional lattices."""
import json
import math
import time
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpz_mat, arb, arb_mat, ctx
from directional_congruence import Family, matrix_rows
from block_pencil_fixed_divisor import gcdq
from joint_exact import content

FOLDER=Path(__file__).parent


def arb_metric(fam):
    # Caller must keep the selected precision active for all matrix operations.
    h,L=fam.h,fam.L
    z=arb(7).zeta();mom=[arb(a)+arb(b)*z for a,b in zip(fam.aa,fam.bb)]
    vv=[sum((arb(c)*mom[e+k] for k,c in enumerate(fam.Q0**2)),arb(0)) for e in range(2*h-1)]
    H=arb_mat(h,h,[vv[i+j] for i in range(h) for j in range(h)]);inv=H.inv()
    kernel=[arb(0) for _ in range(2*h-1)]
    for i in range(h):
        for j in range(h):kernel[i+j]+=inv[i,j]
    mm=[sum((kernel[e]*mom[e+k] for e in range(2*h-1)),arb(0)) for k in range(2*L+1)]
    def inner(P,Q):return sum((arb(c)*mm[k] for k,c in enumerate(P*Q)),arb(0))
    A=arb_mat(L,L,[inner(p,q) for p in fam.ds for q in fam.ds]);b=arb_mat(L,1,[inner(fam.Q0,p) for p in fam.ds])
    minimum=arb(h)-(b.transpose()*A.inv()*b)[0,0]
    assert minimum>0
    return A,b,minimum


def run():
    data=json.loads((FOLDER/'directional_congruence_K24.json').read_text());fam=Family()
    bits=max(max(abs(int(x.p)).bit_length(),int(x.q).bit_length()) for x in fam.aa+fam.bb)+3000
    ct0=content(fam.det([0]*fam.L));cache={(0,)*fam.L:ct0};rows=[];start=time.time()
    with ctx.workprec(bits):
        A,b,minimum=arb_metric(fam)
        for r in data['rows']:
            B=r['basis'];U=r['reduced_basis']
            points=[(0,)*fam.L]+[tuple(v) for v in U]+[tuple(-x for x in v) for v in U]
            points.append(tuple(map(int,r['candidate']['parameters'])))
            for u in points:
                if u not in cache:cache[u]=content(fam.det(u))
            G=gcdq(cache[u] for u in points)
            ub=arb_mat(fam.L,fam.L,[x for row in U for x in row]);gram=ub*A*ub.transpose()
            epsilon=sum((gram[i,i] for i in range(fam.L)),arb(0))/4
            premium=arb(ct0/G).log()/fam.K**2
            ideal_gap=premium+fam.h*(minimum/fam.h).log()/fam.K**2
            rounding_gap=premium+fam.h*((minimum+epsilon)/fam.h).log()/fam.K**2
            rows.append(dict(moduli=r['moduli'],index=r['index'],basis=B,reduced_basis=U,
                sampled_gcd_upper=str(G),witnesses=[dict(u=list(u),content=str(cache[u])) for u in points],
                premium_lower_ball=premium.str(30),rounding_cost_ball=epsilon.str(30),
                ideal_trace_gap_lower_ball=ideal_gap.str(30),rounded_trace_gap_lower_ball=rounding_gap.str(30),
                ideal_trace_obstructed=bool(ideal_gap>0),rounded_trace_obstructed=bool(rounding_gap>0),
                ideal_trace_gap_midpoint=float(ideal_gap.mid()),rounded_trace_gap_midpoint=float(rounding_gap.mid())))
            if len(rows)%20==0:print(json.dumps(dict(processed=len(rows),elapsed=time.time()-start)),flush=True)
        result=dict(K=fam.K,N=fam.N,L=fam.L,h=fam.h,precision_bits=bits,prefix_content=str(ct0),
            minimum_ball=minimum.str(35),rows=rows,distinct_content_evaluations=len(cache),
            scope='Sample gcds are upper bounds on the uniform divisors; positive gaps obstruct only the stated trace/uniform-divisor certificate.')
    path=FOLDER/'directional_congruence_audit.json';path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    best=sorted(rows,key=lambda r:r['ideal_trace_gap_midpoint'])[:8]
    print(json.dumps(dict(path=str(path),ideal_obstructed=sum(r['ideal_trace_obstructed'] for r in rows),
                         rounded_obstructed=sum(r['rounded_trace_obstructed'] for r in rows),total=len(rows),
                         best=[{k:r[k] for k in ['moduli','ideal_trace_gap_lower_ball','rounded_trace_gap_lower_ball']} for r in best])),flush=True)


if __name__=='__main__':run()
