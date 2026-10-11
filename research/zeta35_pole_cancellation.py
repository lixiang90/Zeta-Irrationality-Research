"""Exact p-integrality and Schur-block certificates, no asymptotic claim."""
import argparse,json,math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly,nmod_mat
import zeta35_mixed_moments as mixed
from zeta35_target31 import primes_to
from zeta35_target31_scan import entries

def mu5(e):return Q(-1)**e*Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24
def nu(e):return mu5(e)-3*mixed.mu3(e+1)
def integral(q,p):return int(q.denominator)%p!=0
def mod(q,p):
    assert integral(q,p),(q,p)
    return int(q.numerator)*pow(int(q.denominator),-1,p)%p
def val(q,p):
    if not q:return None
    num,den=abs(int(q.numerator)),int(q.denominator);v=0
    while num%p==0:num//=p;v+=1
    while den%p==0:den//=p;v-=1
    return v

def run(K,N,m,h=None):
    h,A,B=entries(K,N,m,h)
    W=fmpq_poly(mixed.original.Dpoly(N)**m);D=fmpq_poly(mixed.original.Dpoly(K))
    quotients=[W*fmpq_poly([0]*s+[1])//D for s in range(2*h-1)]
    poly=[sum((q[e]*nu(e) for e in range(q.degree()+1)),Q(0)) for q in quotients]
    pole=[a-v for a,v in zip(A,poly)]
    rows=[]
    for p in primes_to(2*h+m*N-K+4):
        r=2*h+m*N-K+2-p
        if p<=max(K,3) or not 0<r<=h:continue
        assert all(integral(a,p) for a in pole)
        assert all(integral(b,p) for b in B)
        high=[sum((q[e]*nu(e) for e in range(p-3,q.degree()+1)),Q(0)) for q in quotients]
        low=[a-v for a,v in zip(A,high)]
        assert all(integral(a,p) for a in low)
        z=h-r
        H=nmod_mat([[mod(p*high[i+j],p) for j in range(h)] for i in range(h)],p)
        assert H.rank()==r
        witnesses=[]
        for x in range(4):
            T=nmod_mat([[mod(A[i+j]+x*B[i+j],p) for j in range(z)] for i in range(z)],p)
            det=int(T.det()) if z else 1
            if det:
                witnesses.append(dict(x=x,top_det_mod_p=det));break
        exact=None
        if K%40==0 and N*40==K*3 and m==6 and h==37*(K//40):
            old=Path(__file__).with_name(f'zeta35_target31_n{K//40}.json')
            if old.exists():
                data=json.loads(old.read_text())
                v5=val(Q(data['rows'][0]['content']),p)
                vt=val(Q(data['rows'][1]['content']),p)
                exact=dict(pure_content_valuation=v5,mixed_content_valuation=vt)
                if witnesses:
                    assert vt==-r
                    x=witnesses[0]['x']
                    targetrow=data['rows'][1]
                    value=Q(targetrow['content'])*sum(int(c)*x**i for i,c in enumerate(targetrow['primitive_coefficients']))
                    actual=mod(p**r*value,p)
                    sign=(-1)**(r*(r-1)//2)
                    predicted=sign*pow(3*pow(2,-1,p)%p,r,p)*witnesses[0]['top_det_mod_p']%p
                    assert actual==predicted
                    exact['block_congruence_mod_p']=actual
        row=dict(p=p,high_rank=r,top_size=z,pole_integral=True,
                 top_block_witnesses=witnesses,certified_content_valuation=-r if witnesses else None,
                 previous_exact_content=exact)
        rows.append(row)
    out=dict(K=K,N=N,m=m,h=h,scope='finite prime certificates; general pole-integrality proof in report',rows=rows)
    path=Path(__file__).with_name(f'zeta35_pole_cancellation_{K}_{N}_{m}_{h}.json')
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('K',type=int);p.add_argument('N',type=int)
    p.add_argument('m',type=int);p.add_argument('h',type=int,nargs='?')
    a=p.parse_args();run(a.K,a.N,a.m,a.h)
