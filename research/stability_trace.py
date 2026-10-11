"""Relative spectral norm from the exact determinant polynomial alone.

C=G^-1/2 B G^-1/2 is real symmetric, and
 tr(C^2)=(P'/P)^2-P''/P at xi=zeta(7).
Thus sqrt(tr(C^2)/deg P)<=||C||<=sqrt(tr(C^2)).
The interval logarithms below are finite-K certificates, NOT asymptotic fits.
"""
import json, argparse, time
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx,arb_mat
from joint_exact import content,experiment


def evaluate(P,x):
    v=arb(0)
    for c in reversed(list(P)):v=v*x+arb(c)
    return v


def trace_certificate(poly,K,aa=None,bb=None):
    P=poly/content(poly);d=P.degree();bits=max(abs(int(c.p)).bit_length() for c in P)+500
    assert d>0
    for attempt in range(4):
        with ctx.workprec(bits):
            x=arb(7).zeta();v=evaluate(P,x);w=evaluate(P.derivative(),x);u=evaluate(P.derivative().derivative(),x)
            if not v>0:bits*=2;continue
            tr2=(w/v)**2-u/v
            if not tr2>0:bits*=2;continue
            upper=tr2.log()/2/K;lower=upper-arb(d).log()/2/K
            result=dict(degree=d,bits=bits,score=(v.log()/K**2).str(25),
                        rho_lower=lower.str(25),rho_upper=upper.str(25),
                        rho_lower_mid=float(lower.mid()),rho_upper_mid=float(upper.mid()),
                        normalization_invariant=True,matrix_crosscheck=False)
            if aa is not None:
                h=(len(aa)+1)//2
                G=arb_mat(h,h,[arb(aa[i+j])+x*arb(bb[i+j]) for i in range(h) for j in range(h)])
                B=arb_mat(h,h,[arb(bb[i+j]) for i in range(h) for j in range(h)])
                M=G.solve(B)
                direct=(M*M).trace()
                assert direct.overlaps(tr2) and direct>0
                result['matrix_crosscheck']=True
            return result
    raise ValueError('insufficient precision')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--extended',action='store_true');args=ap.parse_args()
    folder=Path(__file__).parent;out=Path(__file__).with_suffix('.json');rows=[];start=time.time()
    for path in sorted(folder.glob('joint_cache_K*.json')):
        z=json.loads(path.read_text());r=z['result'];P=fmpq_poly([fmpq(c) for c in z['poly']])
        row=dict(K=r['K'],profile=r['profile'],h=r['h'],source=path.name,
                 **trace_certificate(P,r['K']))
        rows.append(row);print(json.dumps(row),flush=True)
    jobs=[(12,[(1,8)],11),(16,[(1,3),(2,3)],16),(24,[(1,3),(2,3)],24),
          (24,[(1,3),(2,3)],18),(32,[(2,2),(4,4)],24)]
    if args.extended:jobs += [(48,[(2,3),(4,3)],48),(72,[(3,3),(6,3)],72),
                              (40,[(5,8)],35),(80,[(10,8)],70)]
    for K,profile,h in jobs:
        er,P,aa,bb=experiment(K,profile,h)
        row=dict(K=K,profile=profile,h=h,experiment=er,
                 **trace_certificate(P,K,aa if K<=16 else None,bb if K<=16 else None))
        rows.append(row);out.write_text(json.dumps(rows,indent=2))
        print(json.dumps({k:v for k,v in row.items() if k!='experiment'})+f' elapsed={time.time()-start:.1f}s',flush=True)
    out.write_text(json.dumps(rows,indent=2))
