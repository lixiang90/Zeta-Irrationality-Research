"""Arb certificates for trace-based integer-parameter existence bounds.

The gcd of finitely many sampled contents is only an UPPER bound for the
whole affine family's fixed divisor. This direction suffices for the stated
obstruction to the trace/fixed-divisor method.
"""
import argparse,json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpz_mat,arb,arb_mat,ctx
from rational_square_nodes import entries_nodes,node_list,product
from growing_integer_space import basis
from block_pencil_fixed_divisor import gcdq


def run(K,N,L):
    folder=Path(__file__).parent;data=json.loads((folder/f'growing_integer_space_K{K}_L{L}_integer.json').read_text())
    h=K-N-L;nodes=node_list(K,'integer');P0=product(nodes[N:N+L]);ds=[basis(i)*math.factorial(L)**2 for i in range(L)]
    aa,bb,_=entries_nodes(nodes,product(nodes[:N])**8,K-N)
    bits=max(max(abs(int(q.p)).bit_length(),int(q.q).bit_length()) for q in aa+bb)+3000
    T=fmpz_mat(data['lll_transform']);assert abs(int(T.det()))==1
    samples=data['rows'].copy()
    if K==24:samples+=json.loads((folder/'growing_space_scan_K24.json').read_text())['rows']
    G=gcdq(fmpq(r['content']) for r in samples);ct0=fmpq(data['rows'][0]['content'])
    with ctx.workprec(bits):
        z=arb(7).zeta();mom=[arb(a)+arb(b)*z for a,b in zip(aa,bb)]
        vv=[sum((arb(c)*mom[e+i] for i,c in enumerate(P0**2)),arb(0)) for e in range(2*h-1)]
        H=arb_mat(h,h,[vv[i+j] for i in range(h) for j in range(h)]);inv=H.inv()
        kernel=[arb(0) for _ in range(2*h-1)]
        for i in range(h):
            for j in range(h):kernel[i+j]+=inv[i,j]
        tm=[sum((kernel[e]*mom[e+k] for e in range(2*h-1)),arb(0)) for k in range(2*L+1)]
        def inner(A,B):return sum((arb(c)*tm[i] for i,c in enumerate(A*B)),arb(0))
        A=arb_mat(L,L,[inner(a,b) for a in ds for b in ds]);b=arb_mat(L,1,[inner(P0,a) for a in ds])
        minimum=arb(h)-(b.transpose()*A.inv()*b)[0,0]
        t=arb_mat(L,L,[arb(T[i,j]) for i in range(L) for j in range(L)]);red=t*A*t.transpose()
        rounding=sum((red[i,i] for i in range(L)),arb(0))/4
        bound=minimum+rounding;assert minimum>0 and bound<h
        premium=arb(ct0/G).log()/K**2
        best_trace_bound_gain=arb(h)*(minimum/h).log()/K**2
        existence_gain=arb(h)*(bound/h).log()/K**2
        obstruction=premium+best_trace_bound_gain;assert obstruction>0
        r=dict(K=K,N=N,L=L,h=h,precision_bits=bits,sampled_contents=len(samples),
               sampled_gcd=str(G),prefix_content=str(ct0),
               trace_minimum_ball=minimum.str(35),rounding_cost_ball=rounding.str(35),
               trace_upper_ball=bound.str(35),real_existence_gain_ball=existence_gain.str(35),
               fixed_divisor_loss_lower_ball=premium.str(35),
               ideal_trace_method_gap_lower_ball=obstruction.str(35),
               trace_metric_A_midpoint=[[A[i,j].mid().str(250,radius=False) for j in range(L)] for i in range(L)],
               trace_metric_b_midpoint=[b[i,0].mid().str(250,radius=False) for i in range(L)],
               scope='The sampled gcd bounds the full-family fixed divisor from above; this obstructs the trace/AM-GM bound using that divisor, not individual candidates or other determinant estimates.')
    path=folder/f'growing_trace_certificate_K{K}.json';path.write_text(json.dumps(r,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ['sampled_gcd','prefix_content','scope','trace_metric_A_midpoint','trace_metric_b_midpoint']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1);p.add_argument('--L',type=int,default=3)
    a=p.parse_args();run(a.K,a.N,a.L)
