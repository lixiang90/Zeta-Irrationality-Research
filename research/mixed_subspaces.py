"""Positive mixed Hankel minors with genuinely different row/column spaces.

For increasing nonnegative exponent sets E,F, Andreief and generalized
Vandermonde positivity give det[mu(W t^(e_i+f_j)/D_K)] > 0 at zeta(7).
Finite exact content and Arb values are experiments, not asymptotic proofs.
"""
import argparse
import json
import math
import time
from functools import lru_cache
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, arb, ctx
from joint_exact import entries, canonical, evaluate_primitive_ball


def determinant_matrices(A, B):
    h = A.nrows()
    lead = B.det()
    if lead:
        return (-(B.inv()*A)).charpoly()*lead
    constant = A.det()
    if constant:
        cp = (-(A.inv()*B)).charpoly()
        return fmpq_poly([cp[h-i] for i in range(h+1)])*constant
    return interpolation(A, B)


def interpolation(A, B):
    h = A.nrows()
    values = [(A+B*fmpq(j)).det() for j in range(h+1)]
    poly = fmpq_poly([0]); basis = fmpq_poly([1])
    for j in range(h+1):
        poly += basis*values[0]
        values = [values[i+1]-values[i] for i in range(len(values)-1)]
        basis = basis*fmpq_poly([-j, 1])/fmpq(j+1)
    assert poly(h+2) == (A+B*fmpq(h+2)).det()
    return poly


@lru_cache(None)
def moments(K, profile, H):
    return entries(K, profile, H)


def exponents(h, split, gap):
    assert 0 <= split <= h and gap >= 0
    return tuple(range(split))+tuple(range(split+gap, h+gap))


def run(K, profile, E, F, H=None, polys_E=None, polys_F=None):
    profile = canonical(profile)
    E, F = tuple(E), tuple(F)
    assert len(E) == len(F) and list(E) == sorted(set(E)) and list(F) == sorted(set(F))
    h = len(E)
    H = H or (E[-1]+F[-1]+3)//2
    assert 2*H-2 >= E[-1]+F[-1]
    aa, bb = moments(K, profile, H)
    if polys_E is None and polys_F is None:
        A = fmpq_mat(h, h, [aa[i+j] for i in E for j in F])
        B = fmpq_mat(h, h, [bb[i+j] for i in E for j in F])
    else:
        assert H > max(E[-1], F[-1])
        if polys_E is None:
            polys_E = [fmpq_poly([0]*e+[1]) for e in E]
        if polys_F is None:
            polys_F = [fmpq_poly([0]*e+[1]) for e in F]
        assert [p.degree() for p in polys_E] == list(E)
        assert [p.degree() for p in polys_F] == list(F)
        C = fmpq_mat(h,H,[p[j] for p in polys_E for j in range(H)])
        D = fmpq_mat(h,H,[p[j] for p in polys_F for j in range(H)])
        A0 = fmpq_mat(H,H,[aa[i+j] for i in range(H) for j in range(H)])
        B0 = fmpq_mat(H,H,[bb[i+j] for i in range(H) for j in range(H)])
        A = C*A0*D.transpose(); B = C*B0*D.transpose()
    P = determinant_matrices(A, B)
    assert P.degree() <= min(h, K-max((n for n,b in profile), default=0))
    ct, logvalue, bits = evaluate_primitive_ball(P)
    # Positive diagonal scaling. It reduces to the old determinant scaling
    # for E=F=(0,...,h-1); score itself is invariant under rational scalars.
    bottom = math.prod(math.factorial(n)**b for n,b in profile)
    S = fmpq(math.factorial(K), bottom)**(2*h)
    for e in E+F:
        if e:
            S *= fmpq(2, math.factorial(2*e))
    with ctx.workprec(160):
        J = logvalue/K**2
        arithmetic = -arb(ct*S).log()/K**2
        real = J-arithmetic
        result = dict(K=K, profile=[list(p) for p in profile], h=h, degree=P.degree(),
                      E=list(E), F=list(F), partition_area_E=sum(e-i for i,e in enumerate(E)),
                      partition_area_F=sum(f-i for i,f in enumerate(F)),
                      score=float(J.mid()), score_ball=J.str(30),
                      score_per_lambda=float((J*K/h).mid()),
                      arithmetic_ball=arithmetic.str(30), real_ball=real.str(30),
                      precision_bits=bits, positive_primitive_value=True)
    return result, P, A, B


def search():
    ap = argparse.ArgumentParser()
    ap.add_argument('--K', type=int, default=24)
    ap.add_argument('--refine', action='store_true')
    args = ap.parse_args()
    K = args.K
    assert K%24 == 0
    m = K//24
    jobs = []
    if args.refine:
        prior = json.loads(Path(__file__).with_name('mixed_subspaces24.json').read_text())
        mixed = [r for r in prior if r['partition_area_E']+r['partition_area_F'] > 0]
        selected = sorted(mixed, key=lambda r:r['score_per_lambda'])[:4]
        # Match each selected candidate with its unchanged subspace baseline.
        for r in selected:
            d = r['design']
            jobs.append(([(n*m,b) for n,b in r['profile']],r['h']*m,
                         d['split_E']*m,d['gap_E']*m,d['split_F']*m,d['gap_F']*m))
            jobs.append(([(n*m,b) for n,b in r['profile']],r['h']*m,0,0,0,0))
    else:
        for profile in [[(m,8)],[(m,3),(2*m,3)],[(m,4),(2*m,2)],[(m,3),(2*m,2),(3*m,1)]]:
            for h in [18*m,24*m]:
                jobs.append((profile,h,0,0,0,0))
                for gap in [2*m,4*m,6*m]:
                    for split in [h//3,2*h//3]:
                        jobs.extend([(profile,h,split,gap,0,0),
                                     (profile,h,split,gap,split,gap)])
    rows=[];done=set();start=time.time()
    out=Path(__file__).with_name(f'mixed_subspaces{K}.json')
    for profile,h,se,ge,sf,gf in jobs:
        key=(tuple(profile),h,se,ge,sf,gf)
        if key in done: continue
        done.add(key)
        E=exponents(h,se,ge); F=exponents(h,sf,gf)
        r,*_=run(K,profile,E,F,H=h+6*m)
        r['design']=dict(split_E=se,gap_E=ge,split_F=sf,gap_F=gf)
        rows.append(r)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        if len(rows)%10==0 or args.refine:
            best=min(rows,key=lambda t:t['score_per_lambda'])
            print(f"K={K} cases={len(rows)} best={best['score']:.9f} per_lambda={best['score_per_lambda']:.9f} seconds={time.time()-start:.1f}",flush=True)
    print('completed',len(rows),'seconds',time.time()-start,flush=True)


if __name__ == '__main__':
    search()
