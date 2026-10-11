"""Independent polynomial checks and the multiset CRT allocation bound."""
import heapq
import json
import math
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat, fmpz_mat
from sympy import primerange
from joint_exact import entries, content, norm_scalar
from two_prefix_outer import vp


def offsets(K,profile,p):
    eta=[0]*((p+1)//2);full=eta.copy()
    for j in range(1,K+1):full[min(j%p,(-j)%p)]+=1
    for M,e in profile:
        for j in range(1,M+1):eta[min(j%p,(-j)%p)]+=e
    return [1+2*eta[0]-2*full[0]]+[eta[c]-full[c]-6 for c in range(1,len(full))]


def allocation(K,profile,h,p):
    degree=sum(M*e for M,e in profile)
    assert p>=7 and p*p>max(2*K,2*degree+4*h-2*K+4)
    beta=offsets(K,profile,p);heap=[(v,c) for c,v in enumerate(beta)];heapq.heapify(heap)
    counts=[0]*len(beta);weights=[];labels=[]
    for _ in range(h):
        value,c=heapq.heappop(heap);weights.append(value);labels.append((c,counts[c]));counts[c]+=1
        heapq.heappush(heap,(value+(4 if c==0 else 2),c))
    return dict(bound=sum(weights),offsets=beta,counts=counts,weights=weights,labels=labels)


def local_basis_check(K,N,A,B,p):
    h=K-4*N;profile=[(N,4),(A,2),(B,2)];r=allocation(K,profile,h,p)
    t=fmpq_poly([0,1]);parts=[(t+c*c)**n for c,n in enumerate(r['counts'])]
    total=fmpq_poly([1])
    for f in parts:total*=f
    basis=[(total//parts[c])*(t+c*c)**i for c,i in r['labels']]
    C=fmpq_mat(h,h,[q[i] for q in basis for i in range(h)]);assert vp(C.det(),p)==0
    aa,bb=entries(K,profile,h);count=0
    for vv in (aa,bb):
        M=fmpq_mat(h,h,[vv[i+j] for i in range(h) for j in range(h)]);M=C*M*C.transpose()
        for i in range(h):
            for j in range(h):
                if M[i,j]:assert 2*vp(M[i,j],p)>=r['weights'][i]+r['weights'][j]
                count+=1
    return dict(K=K,N=N,A=A,B=B,p=p,bound=r['bound'],entries=count)


def polynomial_check(r):
    K,N,A,B,h=(r[k] for k in ['K','N','A','B','h']);profile=[(N,4),(A,2),(B,2)]
    aa,bb=entries(K,profile,h);P=fmpq_poly([fmpq(c) for c in r['raw_polynomial']])
    den=math.lcm(*(int(c.q) for c in aa+bb));scale=den**h
    for x in range(h+1):
        M=fmpz_mat(h,h,[int(den*(aa[i+j]+x*bb[i+j])) for i in range(h) for j in range(h)])
        assert M.det()==P(x)*scale
    return dict(K=K,N=N,A=A,B=B,specializations=h+1)


def main():
    folder=Path(__file__).parent;data=json.loads((folder/'overlapping_prefix_scan.json').read_text());primes=[];small=[]
    for r in data['rows']:
        K,N,A,B,h=(r[k] for k in ['K','N','A','B','h']);profile=[(N,4),(A,2),(B,2)]
        assert A+B==5*N and 4*N+2*A+2*B+2*h-2-K==K+6*N-2
        P=fmpq_poly([fmpq(c) for c in r['raw_polynomial']]);ct=content(P);assert str(ct)==r['content']
        S=norm_scalar(K,profile,h);d=4*K+12*N+3
        for p in primerange(2,2*K+1):
            power=1;e=0
            while power*p<=d+1:power*=p;e+=1
            lower=-8*h*e-h*vp(720,p);actual=vp(S*ct,p);assert actual>=lower
            small.append(dict(K=K,A=A,p=p,actual=actual,lower=lower))
            if p<7 or p*p<=2*K+12*N+4:continue
            bound=allocation(K,profile,h,p)['bound'];actual=vp(ct,p);assert actual>=bound
            primes.append(dict(K=K,A=A,p=p,actual=actual,bound=bound))
    checks=[polynomial_check(next(r for r in data['rows'] if r['K']==K and r['A']==A)) for K,A in [(24,2),(48,4)]]
    bases=[local_basis_check(*args) for args in [(24,1,2,3,11),(24,1,2,3,13),(48,2,4,6,13),(48,2,4,6,17)]]
    result=dict(records=len(data['rows']),allocation_checks=primes,small_prime_checks=small,polynomial_checks=checks,local_bases=bases,
                scope='Finite exact checks supporting the written general multiset proof; not a Lean compilation or an asymptotic irrationality certificate.')
    path=folder/'overlapping_prefix_validation.json';path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(records=len(data['rows']),allocation_checks=len(primes),small_prime_checks=len(small),
                         polynomial_specializations=sum(r['specializations'] for r in checks),basis_entries=sum(r['entries'] for r in bases))),flush=True)


if __name__=='__main__':main()
