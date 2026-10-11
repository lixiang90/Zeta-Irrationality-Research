"""Scale a genuine one-row graph family, with exact content normalization.

Candidate bounds apply to the specified family, never to every subspace.
"""
import argparse
import json
import math
import time
from pathlib import Path
from flint import fmpq_mat as Mat, fmpz_mat as ZMat, arb, arb_poly, ctx
from zeta35_target31_scan import entries
from zeta35_infinity_basis import dyadic_basis, finite_check
from zeta35_true_subspaces import pencil_polynomial

ROOT = Path(__file__).parent


def setup(n, high=None):
    K,N,m,h = 40*n,3*n,4,34*n-1
    if high is None:
        from sympy import nextprime
        p = int(nextprime(K))
        high = (K-m*N+p-3)//2
    assert h <= high < K-N
    _,aa,bb = entries(K,N,m,high+1)
    _,_,_,T = dyadic_basis(K,N,m,high+1)
    A,B,checks = finite_check(K,N,m,aa,bb,T)
    rho = math.prod(row['p'] for row in checks
                    if row['s'] == 2*high or 0 <= row['s']-high <= h-2)
    assert all(i+j != row['s'] for row in checks for i in range(h-1) for j in range(h-1))
    assert all(h-1+j != row['s'] for row in checks for j in range(h-1))
    assert all(2*(h-1) != row['s'] for row in checks)
    def restrict(u,v):
        C = Mat([[int(i == j) for j in range(high+1)] for i in range(h)])
        C[h-1,h-1],C[h-1,high] = u,rho*v
        return C
    return (K,N,m,h,high,rho),A,B,checks,restrict


def generate(n,high=None):
    start = time.perf_counter()
    pars,A,B,checks,restrict = setup(n,high)
    K,N,m,h,high,rho = pars
    print('SETUP',pars,'seconds',time.perf_counter()-start,flush=True)
    polys = []
    for u,v in ((1,0),(0,1),(1,1)):
        C = restrict(u,v)
        AA,BB = C*A*C.transpose(),C*B*C.transpose()
        p = pencil_polynomial(AA,BB)
        for x in (-1,0,1):
            assert p(x) == (AA+x*BB).det()
        assert BB.rank() == h and p.degree() == h
        polys.append(p)
        print('PENCIL',u,v,'seconds',time.perf_counter()-start,flush=True)
    p0,p1,ps = polys
    pc = ps-p0-p1
    denominator = math.lcm(*(int(v.denominator) for p in (p0,pc,p1) for v in p))
    cols = [[int(p[i]*denominator) for i in range(h+1)] for p in (p0,pc,p1)]
    common = math.gcd(*(v for c in cols for v in c))
    cols = [[v//common for v in c] for c in cols]
    C = ZMat(list(map(list,zip(*cols))))
    H,T = C.hnf(transform=True)
    assert T*C == H
    hnf = [[int(H[i,j]) for j in range(3)] for i in range(h+1)]
    assert all(row == [0,0,0] for row in hnf[3:])
    # Verify the reverse row-lattice inclusion instead of a huge det(T).
    coordinates = Mat(C)*Mat(hnf[:3]).inv()
    assert all(v.denominator == 1 for v in coordinates.entries())
    print('ROW_LATTICE_VERIFIED','seconds',time.perf_counter()-start,flush=True)
    ctx.prec = max(abs(v).bit_length() for c in cols for v in c)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(c)(theta) for c in cols]
    assert values[0] > 0 and values[2] > 0
    assert values[0]*values[2]-values[1]**2/4 > 0
    base_content = math.gcd(*cols[0])
    baseline = values[0]/base_content
    out = dict(n=n,K=K,N=N,m=m,h=h,high=high,rho=rho,checks=checks,
               coefficients=cols,hnf=hnf[:3],baseline_content=str(base_content),
               baseline_log=float(baseline.log()),baseline_interval=baseline.log().str(40),
               seconds=time.perf_counter()-start)
    path = ROOT/f'zeta35_graph_scaling_n{n}_q{high}.json'
    path.write_text(json.dumps(out,indent=2))
    print('DONE',path.name,'baseline',out['baseline_log'],'hnf',hnf[:3],flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--n',type=int,required=True)
    p.add_argument('--high',type=int)
    args = p.parse_args()
    generate(args.n,args.high)
