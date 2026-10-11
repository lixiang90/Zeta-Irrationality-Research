"""Finite exact searches for a rational dressing of the -27 mode."""
import json
import math
from pathlib import Path

from flint import fmpq, fmpq_mat
from determinant_shape_probe import transfer_matrix, head_matrix


def recurrence_matrix(N):
    Q,_,_=transfer_matrix(N,N-3)
    T=head_matrix(N,N-3)*head_matrix(N,N-2)*head_matrix(N,N-1)
    return (Q.inv()*T).transpose()*(4**5*(N*(N-1))**5)


def nullspace(rows, columns):
    reduced,rank=fmpq_mat(rows).rref()
    pivots=[]
    for i in range(rank):
        pivots.append(next(j for j in range(columns) if reduced[i,j]))
    free=[j for j in range(columns) if j not in pivots]
    vectors=[]
    for j in free:
        v=[fmpq(0)]*columns;v[j]=fmpq(1)
        for i,p in enumerate(pivots):v[p]=-reduced[i,j]
        vectors.append(v)
    return vectors,rank


def modular_rank_certificate(rows, columns):
    for prime in (1000003,1000033):
        if any(int(x.denominator)%prime==0 for row in rows for x in row):continue
        A=[[int(x.numerator)%prime*pow(int(x.denominator)%prime,-1,prime)%prime for x in row] for row in rows]
        rank=0
        for col in range(columns):
            choices=[i for i in range(rank,len(A)) if A[i][col]]
            if not choices:continue
            p=choices[0];A[p],A[rank]=A[rank],A[p]
            inverse=pow(A[rank][col],-1,prime)
            A[rank]=[x*inverse%prime for x in A[rank]]
            for i in range(rank+1,len(A)):
                c=A[i][col]
                if c:A[i]=[(x-c*y)%prime for x,y in zip(A[i],A[rank])]
            rank+=1
        if rank==columns:return dict(prime=prime,rank=rank)
    raise AssertionError('No independent modular full-rank certificate found')


def search(denominator, degree, matrices, dual=False, base_kind='dixon'):
    # y_n = (-1)^(n/2) (3n/2)! / (n/2)!^3 * P(n)/D(n).
    # P_i has degree <= 2i+degree-3, matching the observed n^-4 exponent.
    offset=3 if base_kind=='dixon' else 4
    sizes=[max(0,degree+offset+1-2*i) if dual else max(0,2*i+degree-offset+1) for i in range(4)]
    terms=[(i,j) for i in range(4) for j in range(sizes[i])]
    rows=[]
    for N,R in matrices:
        if denominator(N)==0 or denominator(N-2)==0: continue
        if base_kind=='dixon': base=-fmpq(3*(3*N-2)*(3*N-4),N*N)
        elif base_kind=='half_shift': base=-fmpq(3*(3*N-2)*(3*N-4),(N-1)**2)
        else: base=fmpq(-27)
        ratio=base*fmpq(denominator(N),denominator(N-2)) if dual else base*fmpq(denominator(N-2),denominator(N))
        for k in range(4):
            if dual:
                rows.append([N**j*R[i,k]-(ratio*(N-2)**j if k==i else 0) for i,j in terms])
            else:
                rows.append([R[k,i]*(N-2)**j-(ratio*N**j if k==i else 0) for i,j in terms])
        if len(rows)>=len(terms)+12:
            vectors,rank=nullspace(rows,len(terms))
            if not vectors:
                certificate=modular_rank_certificate(rows,len(terms))
                return dict(unknowns=len(terms),rank=rank,sampled_equations=len(rows),solutions=[],
                            independent_modular_rank=certificate)
    vectors,rank=nullspace(rows,len(terms))
    return dict(unknowns=len(terms),rank=rank,sampled_equations=len(rows),
                solutions=[[[str(v[terms.index((i,j))]) for j in range(sizes[i])] for i in range(4)] for v in vectors])


def main():
    matrices=[(N,recurrence_matrix(N)) for N in range(4,100,2)]
    denominators=[('n^3',lambda n:n**3,3),
                  ('(n+1)^3',lambda n:(n+1)**3,3),
                  ('n(n+1)(n+2)',lambda n:n*(n+1)*(n+2),3),
                  ('n^2(n+1)',lambda n:n*n*(n+1),3),
                  ('n(n+1)^2',lambda n:n*(n+1)**2,3),
                  ('(n-1)n(n+1)',lambda n:(n-1)*n*(n+1),3),
                  ('n^3(n+1)^3',lambda n:n**3*(n+1)**3,6),
                  ('(n-1)^3*n^3*(n+1)^3*(n+2)^3',lambda n:math.prod((n+j)**3 for j in (-1,0,1,2)),12),
                  ('n*(3n-2)*(3n-4)',lambda n:n*(3*n-2)*(3*n-4),3),
                  ('n*(3n+2)*(3n+4)',lambda n:n*(3*n+2)*(3*n+4),3),
                  ('extended singular-factor denominator',lambda n:math.prod((n+j)**3 for j in (-1,0,1,2))*math.prod((3*n+j)**2 for j in (-4,-2,2,4))*math.prod(5*n-j for j in (2,4,6,8)),24)]
    rows=[]
    for name,den,degree in denominators:
        for dual in (False,True):
            result=search(den,degree,matrices,dual);result['denominator']=name;result['dual']=dual;result['base']='dixon'
            rows.append(result)
            print(json.dumps(result),flush=True)
    for name,den,degree in [('n^4',lambda n:n**4,4),('(n+1)^4',lambda n:(n+1)**4,4),
                            ('n^2(n+1)^2',lambda n:n*n*(n+1)**2,4),
                            ('(n-1)n(n+1)(n+2)',lambda n:(n-1)*n*(n+1)*(n+2),4),
                            denominators[-1]]:
        for dual in (False,True):
            for base_kind in ('constant','half_shift'):
                result=search(den,degree,matrices,dual,base_kind);result.update(denominator=name,dual=dual,base=base_kind)
                rows.append(result);print(json.dumps(result),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope='Finite ansatz exclusions only; not a general irreducibility theorem.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
