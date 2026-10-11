"""Finite-field closed-shift monodromy of the exact four-dimensional recurrence."""
import itertools
import json
import math
from pathlib import Path
from flint import fq_default_ctx


def mul(a,b):
    c=[a[0]*0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),A[0][0]*0)
             for j in range(len(B[0]))] for i in range(len(A))]


def inverse(A):
    zero=A[0][0]*0;one=zero+1;n=len(A)
    B=[row[:]+[one if i==j else zero for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        p=next(j for j in range(i,n) if B[j][i]!=zero)
        B[i],B[p]=B[p],B[i]
        u=B[i][i];B[i]=[x/u for x in B[i]]
        for j in range(n):
            if j!=i:
                u=B[j][i];B[j]=[x-u*y for x,y in zip(B[j],B[i])]
    return [row[n:] for row in B]


def determinant(A):
    B=[row[:] for row in A];zero=A[0][0]*0;value=zero+1
    for i in range(len(B)):
        candidates=[j for j in range(i,len(B)) if B[j][i]!=zero]
        if not candidates:return zero
        p=candidates[0]
        if p!=i:B[i],B[p]=B[p],B[i];value=-value
        u=B[i][i];value*=u
        for j in range(i+1,len(B)):
            v=B[j][i]/u;B[j]=[x-v*y for x,y in zip(B[j],B[i])]
    return value


def kernels(N,L,count):
    zero=N*0;one=zero+1
    power=lambda c,k:[math.comb(k,j)*c**(k-j) for j in range(k+1)]
    result=[]
    for i in range(count):
        left=mul(mul([-N-2*L-2,one],power(N,8)),power(-one,2*i))
        right=mul(mul(power(-N,8),[N+2*L+2,one]),power(one,2*i))
        raw=[(a-b)/2 for a,b in zip(left,right)]
        assert all(raw[j]==zero for j in range(1,len(raw),2))
        even=raw[::2]
        assert even[-1]==7*N-2*L-2*i-2
        result.append(even)
    return result


def head(N,L):
    K=kernels(N,L,1)[0];zero=N*0;one=zero+1
    T=[[zero]*4 for _ in range(4)]
    for j in range(4):
        T[j][j]-=(N+2*L+2)**2
        if j<3:T[j+1][j]+=one
        else:
            for i in range(4):T[i][j]-=K[i]/K[4]
    return T


def recurrence(N):
    L=N-3;zero=N*0
    K=kernels(N,L,8)
    columns=[]
    base=[math.comb(8,r)*(-N*N)**(8-r) for r in range(9)]
    for j in range(4):
        P=[zero]*j+base[:]+[zero]*(3-j)
        for i in reversed(range(8)):
            u=P[i+4]/K[i][i+4]
            for r,k in enumerate(K[i]):P[r]-=u*k
        assert all(x==zero for x in P[4:])
        columns.append(P[:4])
    Q=[[columns[j][i] for j in range(4)] for i in range(4)]
    C=mm(inverse(Q),mm(mm(head(N,L),head(N,L+1)),head(N,L+2)))
    scale=4**5*(N*(N-1))**5
    return [[C[j][i]*scale for j in range(4)] for i in range(4)]


def probe(p):
    C=fq_default_ctx(p,2,'a');a=C.gen();zero=C.zero();one=C.one()
    P=[[one if i==j else zero for j in range(4)] for i in range(4)]
    for j in range(1,p+1):P=mm(recurrence(a+2*j),P)
    assert determinant(P)!=zero
    exceptional=determinant([[P[i][j]+(27 if i==j else 0) for j in range(4)] for i in range(4)])==zero
    roots=[]
    for c,d in itertools.product(range(p),repeat=2):
        u=C(c)+C(d)*a
        test=[[P[i][j]-(u if i==j else zero) for j in range(4)] for i in range(4)]
        if determinant(test)==zero:roots.append([c,d])
    return dict(prime=p,field=str(C),monodromy=[[str(x) for x in row] for row in P],
                rational_specialization_eigenvalues=roots,has_eigenvalue=bool(roots),
                exceptional_minus27_eigenvalue_present=exceptional)


def main():
    from exceptional_mode_probe import recurrence_matrix
    prime=101
    base=fq_default_ctx(prime,1,'b')
    for N in (4,6,8,12):
        exact=recurrence_matrix(N)
        reduced=recurrence(base(N))
        assert all(reduced[i][j]==base(int(exact[i,j].numerator))/base(int(exact[i,j].denominator))
                   for i in range(4) for j in range(4))
    rows=[]
    for p in (7,11,13,17,19):
        row=probe(p);rows.append(row)
        print(json.dumps(row),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope='Specialized modular obstruction test; a root is inconclusive.',
                rational_recurrence_reduction_checks=4,rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
