"""Higher p-adic restrictions of the content-free adjugate pencil.

All flag arithmetic is exact. A coordinate equal to one guarantees primitive
normals; the affine existence bound includes the full restricted lattice cost.
"""
import argparse
import json
from functools import reduce
from math import gcd
from itertools import product
from pathlib import Path

from flint import fmpz_mat, fmpq_mat, nmod_mat
from arithmetic_subspaces import (integer_pencil, adjugate_coefficients,
                                  rational_metric, congruence_kernel, valuation)
from affine_subspace_existence import chart_result


def identity(m):
    return fmpz_mat([[int(i == j) for j in range(m)] for i in range(m)])


def rows(T):
    return [[int(T[i,j]) for j in range(T.ncols())] for i in range(T.nrows())]


def matrix_content(matrices):
    return reduce(gcd, (abs(int(x)) for H in matrices for x in H.entries()), 0)


def integral_coefficients(H):
    g = matrix_content(H)
    return g, [fmpz_mat(T.nrows(), T.ncols(), [int(x/g) for x in T.entries()]) for T in H]


def restrict(F, T):
    return [T*H*T.transpose() for H in F]


def residual_forms(F,T,p):
    restricted=restrict(F,T)
    exponent=valuation(matrix_content(restricted),p)
    m=T.nrows()
    forms=[nmod_mat(m,m,[(int(x)//p**exponent)%p for x in H.entries()],p) for H in restricted]
    stack=nmod_mat(m*len(F),m,[int(x) for H in forms for x in H.entries()],p)
    rr,r=stack.rref()
    L=nmod_mat(r,m,[int(rr[i,j]) for i in range(r) for j in range(m)],p)
    pivots=[next(j for j in range(m) if L[i,j]) for i in range(r)]
    Q=[nmod_mat(r,r,[int(H[i,j]) for i in pivots for j in pivots],p) for H in forms]
    assert all(H==L.transpose()*q*L for H,q in zip(forms,Q))
    ss=nmod_mat(len(Q),r*r,[int(x) for q in Q for x in q.entries()],p)
    basis,dimension=ss.rref()
    independent=[nmod_mat(r,r,[int(basis[i,k]) for k in range(r*r)],p) for i in range(dimension)]
    return exponent,L,independent


def null_rows(C,p):
    N,d=C.nullspace()
    return nmod_mat(d,C.ncols(),[int(N[j,i]) for i in range(d) for j in range(C.ncols())],p)


def isotropic_space(Q,p):
    """Radical plus a maximal totally isotropic space of one symmetric form."""
    n=Q.nrows()
    E=nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],p)
    diagonal=[]; vectors=[]
    while E.nrows():
        R=E*Q*E.transpose(); d=E.nrows()
        if not R:
            break
        v=[0]*d
        pivot=next((i for i in range(d) if R[i,i]),None)
        if pivot is None:
            i,j=next((i,j) for i in range(d) for j in range(i+1,d) if R[i,j])
            v[i]=v[j]=1
        else:
            v[pivot]=1
        vv=nmod_mat(1,d,v,p)
        diagonal.append(int((vv*R*vv.transpose())[0,0]))
        vectors.append([int(x) for x in (vv*E).entries()])
        E=null_rows(vv*R,p)*E
    radical_rows=rows(E)
    V=nmod_mat(len(vectors),n,[x for v in vectors for x in v],p)
    selected=[]
    # Repeated hyperbolic-plane splitting, searching at most three variables.
    while V.nrows():
        R=V*Q*V.transpose(); d=V.nrows()
        # R need not stay diagonal after taking an orthogonal complement.
        v=None
        for values in product(range(p),repeat=min(d,3)):
            if not any(values):
                continue
            candidate=list(values)+[0]*(d-min(d,3))
            vv=nmod_mat(1,d,candidate,p)
            if not vv*R*vv.transpose():
                v=vv; break
        if v is None:
            assert d<=2
            break
        b=v*R
        pivot=next(i for i in range(d) if b[0,i])
        w=[0]*d; w[pivot]=pow(int(b[0,pivot]),-1,p)
        w=nmod_mat(1,d,w,p)
        w=w-v*(int((w*R*w.transpose())[0,0])*pow(2,-1,p)%p)
        assert not w*R*w.transpose() and int((v*R*w.transpose())[0,0])==1
        selected.append([int(x) for x in (v*V).entries()])
        equations=nmod_mat(2,d,list((v*R).entries())+list((w*R).entries()),p)
        V=null_rows(equations,p)*V
    result=nmod_mat(len(radical_rows)+len(selected),n,
                    [x for v in radical_rows+selected for x in v],p)
    assert result.rank()==result.nrows() and not result*Q*result.transpose()
    return result


def common_isotropic_space(Q,p):
    r=Q[0].nrows()
    E=nmod_mat(r,r,[int(i==j) for i in range(r) for j in range(r)],p)
    # Low-rank forms first: their unavoidable anisotropic directions can
    # simplify the whole system before a discretionary Witt choice is made.
    for q in sorted(Q,key=lambda q:q.rank()):
        E=isotropic_space(E*q*E.transpose(),p)*E
    assert all(not E*q*E.transpose() for q in Q)
    return E


def advance(F, T, p, strategy='radical'):
    """Require the common radical of the current residual coefficient forms."""
    m = T.nrows()
    restricted = restrict(F, T)
    before = valuation(matrix_content(restricted), p)
    stack = nmod_mat(m*len(F), m,
                     [(int(x)//p**before) % p for H in restricted for x in H.entries()], p)
    rank = stack.rank()
    assert 0 < rank <= m
    isotropic_dimension=0
    E=None
    if strategy=='isotropic':
        _,L,Q=residual_forms(F,T,p)
        E=common_isotropic_space(Q,p)
        isotropic_dimension=E.nrows()
        constraints=null_rows(E,p)*L
    else:
        constraints=stack
    S = congruence_kernel(constraints, p)
    updated = (S*T).hnf()
    after = valuation(matrix_content(restrict(F, updated)), p)
    assert after >= before+1
    assert abs(updated.det()) == abs(T.det())*p**(rank-isotropic_dimension)
    return updated, dict(p=p, rank=rank, exponent_before=before, exponent_after=after,
                        index_exponent=valuation(updated.det(),p),
                        primitive_mod_p=any(int(x) % p for x in updated.entries()),
                        isotropic_dimension=isotropic_dimension,
                        isotropic_rows=rows(E) if E is not None else [])


def lattice_chart(T, j):
    """All vectors in the row lattice with coordinate j equal to one."""
    m = T.nrows()
    column = fmpz_mat(m, 1, [int(T[i,j]) for i in range(m)])
    h, U = column.hnf(transform=True)
    if h[0,0] != 1:
        return None
    assert abs(U.det()) == 1 and U*column == h
    W = U*T
    assert W[0,j] == 1 and all(W[i,j] == 0 for i in range(1,m))
    cols = [k for k in range(m) if k != j]
    a = fmpz_mat(1,m-1,[W[0,k] for k in cols])
    L = fmpz_mat(m-1,m-1,[W[i,k] for i in range(1,m) for k in cols])
    assert abs(L.det()) == abs(T.det())
    return cols, a, L


def run(K, N, m, primes, depth, bounds, strategy='radical', joint=False):
    A,B,_ = integer_pencil(K,N,m)
    det,H = adjugate_coefficients(A,B)
    g,F = integral_coefficients(H)
    dual = rational_metric(A,B)[0] if bounds else None
    data = dict(K=K,N=N,m=m,h=m-1,strategy=strategy,adjugate_content=str(g),flags=[],charts=[])
    prefix='padic_subspace_flags' if strategy=='radical' else 'isotropic_subspace_flags'
    output = Path(__file__).with_name(f'{prefix}_K{K}_N{N}_m{m}.json')
    jobs=[]
    for p in primes:
        T=identity(m)
        for level in range(1,depth+1):
            e,L,Q=residual_forms(F,T,p)
            T,record=advance(F,T,p,strategy)
            record.update(step=level,lattice_rows=rows(T),residual_row_basis=rows(L),
                          residual_form_basis=[rows(q) for q in Q],form_span_dimension=len(Q))
            feasible=[j for j in range(m) if lattice_chart(T,j) is not None]
            record['feasible_coordinates']=feasible
            data['flags'].append(record)
            print(json.dumps({k:v for k,v in record.items() if k not in
                              ['lattice_rows','residual_row_basis','residual_form_basis','isotropic_rows']}),flush=True)
            if feasible:
                jobs.append((f'p{p}_step{level}',T,sorted({feasible[0],feasible[-1]})))
            if not record['primitive_mod_p']:
                break
    if joint:
        T=identity(m)
        for p in primes:
            for level in range(depth):
                T,record=advance(F,T,p,strategy)
        feasible=[j for j in range(m) if lattice_chart(T,j) is not None]
        if feasible:
            jobs.append((f'joint_depth{depth}',T,sorted({feasible[0],feasible[-1]})))
    if bounds:
        for label,T,coordinates in jobs:
            for j in coordinates:
                result=chart_result(K,A,B,det,H,dual,j,[],label,'higher_padic',g,
                                    chart_override=lattice_chart(T,j))
                result['ambient_lattice_rows']=rows(T)
                assert int(result['fixed_divisor']) % (g*matrix_content(restrict(F,T))) == 0
                data['charts'].append(result)
                print(json.dumps(dict(label=label,j=j,bound=result['existence_score'],
                                      witness=result['witness']['score'],
                                      relative_divisor=str(int(result['fixed_divisor'])//g))),flush=True)
                output.write_text(json.dumps(data,indent=2),encoding='utf-8')
    output.write_text(json.dumps(data,indent=2),encoding='utf-8')
    return data


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--K',type=int,default=24)
    parser.add_argument('--N',type=int,default=1)
    parser.add_argument('--m',type=int)
    parser.add_argument('--primes',type=int,nargs='+',default=[3,7,17])
    parser.add_argument('--depth',type=int,default=3)
    parser.add_argument('--bounds',action='store_true')
    parser.add_argument('--strategy',choices=['radical','isotropic'],default='radical')
    parser.add_argument('--joint',action='store_true')
    args=parser.parse_args()
    run(args.K,args.N,args.m or args.K-args.N+1,args.primes,args.depth,args.bounds,args.strategy,args.joint)
