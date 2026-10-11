"""Exact positive Gram determinants with integer and half-integer square nodes.

The functional itself is unchanged. Only denominator poles and numerator zeros
are changed. No old local divisibility bounds are assumed for the new nodes.
"""
import argparse,json,math
from functools import lru_cache
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx
from joint_exact import moment,determinant_pole_split,evaluate_primitive_ball
from integer_blocks import scalar


@lru_cache(None)
def pole(a):
    a=fmpq(a);assert a>0 and a.q in (1,2)
    if a.q==1:
        j=int(a);tail=sum((fmpq(1,k**7) for k in range(1,j)),fmpq(0));mult=1
    else:
        j=(int(a.p)-1)//2
        tail=sum((fmpq(2**7,(2*k+1)**7) for k in range(j)),fmpq(0));mult=127
    return -a**6*tail-1/(2*a)-fmpq(1,6),a**6*mult


def node_list(K,kind):
    if kind=='integer':return [fmpq(j) for j in range(1,K+1)]
    if kind=='half':return [fmpq(2*j-1,2) for j in range(1,K+1)]
    if kind=='dense_half':return [fmpq(j,2) for j in range(1,K+1)]
    if kind=='odd':return [fmpq(2*j-1) for j in range(1,K+1)]
    if kind=='even':return [fmpq(2*j) for j in range(1,K+1)]
    if kind=='square':return [fmpq(j*j) for j in range(1,K+1)]
    if kind=='alternating':return [fmpq(2*j-(j%2),2) for j in range(1,K+1)]
    if kind.startswith('half_prefix:'):
        cutoff=int(kind.split(':')[1]);return [fmpq(2*j-(j<=cutoff),2) for j in range(1,K+1)]
    raise ValueError(kind)


def product(nodes):
    out=fmpq_poly([1])
    for a in nodes:out*=fmpq_poly([a*a,1])
    return out


def entries_nodes(nodes,W,h):
    assert len(set(nodes))==len(nodes) and all(a>0 for a in nodes)
    D=product(nodes);deriv=D.derivative();data=[];T=fmpq_poly([1])
    for a in nodes:
        residue=W(-a*a)/deriv(-a*a)
        if residue:
            ca,cb=pole(a);data.append((a,residue,ca,cb));T*=fmpq_poly([a*a,1])
    aa=[];bb=[];P=W;powers=[fmpq(1)]*len(data)
    for e in range(2*h-1):
        quotient=P//D;av=sum((c*moment(k) for k,c in enumerate(quotient)),fmpq(0));bv=fmpq(0)
        for i,(a,residue,ca,cb) in enumerate(data):
            value=residue*powers[i];av+=value*ca;bv+=value*cb;powers[i]*=-a*a
        aa.append(av);bb.append(bv);P*=fmpq_poly([0,1])
    return aa,bb,T


def experiment(K,N,M,kind,Q=None,label=None):
    nodes=node_list(K,kind);h=K-M
    W=product(nodes[:N])**6*product(nodes[:M])**2 if Q is None else product(nodes[:N])**8*Q**2
    aa,bb,T=entries_nodes(nodes,W,h);P=determinant_pole_split(aa,bb,T,h)
    ct,lv,bits=evaluate_primitive_ball(P)
    # A shared scalar is only for an auditable decomposition, not a claimed
    # small-prime normalization for arbitrary nodes.
    S=scalar(K,N,[(N,M-N)],h)
    with ctx.workprec(160):
        score=lv/K**2;gain=arb(S*ct).log()/K**2
        row=dict(K=K,N=N,M=M,h=h,kind=kind,label=label or kind,degree=P.degree(),
                 score=float(score.mid()),score_ball=score.str(30),
                 real=float((score+gain).mid()),real_ball=(score+gain).str(30),
                 arithmetic_gain=float(gain.mid()),content=str(ct),scalar=str(S),
                 primitive_polynomial=[str(c) for c in P/ct],precision_bits=bits)
    if Q is not None:row['Q']=[str(c) for c in Q]
    return row


def run(K,N,Ms,kinds):
    path=Path(__file__).with_name(f'rational_square_nodes_K{K}.json')
    rows=json.loads(path.read_text())['rows'] if path.exists() else []
    seen={(r['N'],r['M'],r['kind']) for r in rows}
    for M in Ms:
        for kind in kinds:
            if (N,M,kind) in seen:continue
            r=experiment(K,N,M,kind);rows.append(r)
            path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
            print(json.dumps({k:r[k] for k in ('K','N','M','kind','score','real','arithmetic_gain')}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1)
    p.add_argument('--Ms',default='2,3,4,5');p.add_argument('--kinds',default='integer,half,dense_half,odd,even,alternating,half_prefix:4,half_prefix:12')
    a=p.parse_args();run(a.K,a.N,list(map(int,a.Ms.split(','))),a.kinds.split(','))
