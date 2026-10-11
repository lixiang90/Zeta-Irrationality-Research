"""Entrywise certificates for the CRT basis and exceptional-moment split."""
import json
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat
from two_prefix_outer import outer_bound, vp
from joint_exact import Dcache, entries, moment


def check(K,N,M,h,p):
    bound=outer_bound(K,N,M,h,p);L=K-M;t=fmpq_poly([0,1])
    W=fmpq_poly(Dcache(N))**6*Dcache(M)**2
    denom=fmpq_poly(Dcache(K));T=fmpq_poly(Dcache(K)//Dcache(M))
    aa,bb=entries(K,[(N,6),(M,2)],h)
    yy=[];Q=W
    for e in range(2*h-1):
        quotient=Q//denom
        yy.append(sum((quotient[k]*moment(k) for k in range(3*p-4,quotient.degree()+1)),fmpq(0)))
        Q*=t
    A=fmpq_mat(h,h,[aa[i+j]-yy[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    Y=fmpq_mat(h,h,[yy[i+j] for i in range(h) for j in range(h)])
    assert Y.rank()<=bound['moment_rank']
    assert all(not x or vp(x,p)>=-1 for x in Y.entries())
    basis=[];weights=[]
    for info in bound['classes']:
        c=info['c'];ps=[j for j in range(M+1,K+1) if j%p in [c,p-c]]
        local=fmpq_poly([1]);big=fmpq_poly([1])
        for j in ps:
            local*=t+j*j
            if j>p:big*=t+j*j
        O=T//local;n=info['big']
        for i in range(len(ps)):
            basis.append(O*((t+c*c)**i if i<n else big*(t+c*c)**(i-n)))
        weights+=info['twice_weights']
    zero=fmpq_poly([1]);q=K//p
    for j in range(p,K+1,p):zero*=t+j*j
    for i in range(q):basis.append((T//zero)*t**i)
    weights +=[-(2*q-1)]*q
    for i in range(h-L):basis.append(T*t**i)
    weights +=[0]*(h-L)
    assert len(basis)==h and weights==bound['twice_weights']
    C=fmpq_mat(h,h,[Q[j] for Q in basis for j in range(h)])
    assert vp(C.det(),p)==0
    ca=C*A*C.transpose();cb=C*B*C.transpose()
    for matrix in [ca,cb]:
        for i in range(h):
            for j in range(h):
                assert not matrix[i,j] or 2*vp(matrix[i,j],p)>=weights[i]+weights[j],(K,N,M,h,p,i,j)
    return dict(K=K,N=N,M=M,h=h,p=p,moment_rank=bound['moment_rank'],
                actual_correction_rank=Y.rank(),change_of_basis_unit=True,
                coefficient_entry_inequalities=2*h*h,lower=bound['lower'])


def run():
    jobs=[]
    for K,N,M in [(24,1,2),(24,1,4),(48,2,4),(48,2,8)]:
        for h in sorted({K-M,K-N}):
            for p in ([11,13,17] if K==24 else [17,23,29]):
                if p>2*M and 3*p>K:jobs.append((K,N,M,h,p))
    rows=[]
    for job in jobs:
        row=check(*job);rows.append(row);print(json.dumps(row),flush=True)
    Path(__file__).with_name('two_prefix_crt_validation.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')


if __name__=='__main__':run()
