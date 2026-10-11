"""Complete local pencil modulo p^L: quotient moments, poles, and X term.

All p-denominators are cleared before changing basis; extra precision is
retained before tropical normalization. No large-index Bernoulli numbers
are needed. Zero residues give valuation lower bounds, never exact zeros.
"""
import math,time,json,argparse
from pathlib import Path
from flint import fmpq,fmpz_poly,fmpz_mod_ctx,fmpz_mod_mat
from joint_exact import Dcache
from joint_padic import residue,val,hungarian
from layer_projection import local_basis,local_data
from distribution_modular import moments_mod

def vp_mod(a,p,precision):
    a=int(a)
    if not a:return precision
    v=0
    while a%p==0:a//=p;v+=1
    return v

def mat(rows,p,precision):
    n=len(rows);m=len(rows[0]) if n else 0
    return fmpz_mod_mat(n,m,[x for row in rows for x in row],fmpz_mod_ctx(p**precision))

def raw_pencil(K,N,p,precision=24,harmonic_deformation=0):
    """Return p^shift times each component, with absolute accuracy precision."""
    assert p>=7 and p>2*N and p*p>2*K
    h=K-N;W=Dcache(N)**8;D=Dcache(K)
    harmonic=fmpq(0);pole=[];shift=1
    facts=[math.factorial(j) for j in range(2*K+1)]
    for j in range(1,K+1):
        harmonic+=fmpq(1,j**7)
        if j<=N:continue
        r=fmpq((-1)**(j-1)*2*j*j*int(W(-j*j)),facts[K-j]*facts[K+j])
        # Optional controlled diagnostic: not the original zeta(7) functional.
        adjusted=harmonic+(fmpq(harmonic_deformation,p**7) if j>=2*p else 0)
        a=r*(-j**6*adjusted-fmpq(1,6)+fmpq(1,2*j));b=r*j**6
        shift=max(shift,-val(a,p),-val(b,p));pole.append((j,a,b))
    full_precision=shift+precision;modulus=p**full_precision
    maxdegree=8*N+2*h-2-K
    mus=moments_mod(p,max(0,maxdegree+1),precision+1)
    qs=[];P=W;t=fmpz_poly([0,1]);scale=p**(shift-1)
    for e in range(2*h-1):
        Q=P//D
        qs.append(scale*sum(int(c)*mus[k] for k,c in enumerate(Q))%modulus)
        P*=t
    ps=[0]*(2*h-1);bs=[0]*(2*h-1)
    for j,a,b in pole:
        ra=residue(a,p,-shift,full_precision);rb=residue(b,p,-shift,full_precision)
        power=1;step=-j*j%modulus
        for e in range(2*h-1):
            ps[e]=(ps[e]+ra*power)%modulus;bs[e]=(bs[e]+rb*power)%modulus
            power=power*step%modulus
    basis,weights,tags=local_basis(K,N,p);ctx=fmpz_mod_ctx(modulus)
    C=fmpz_mod_mat(h,h,[int(P[j])%modulus for P in basis for j in range(h)],ctx)
    def transform(values):
        H=fmpz_mod_mat(h,h,[values[i+j] for i in range(h) for j in range(h)],ctx)
        return C*H*C.transpose()
    Q=transform(qs);P=transform(ps);B=transform(bs)
    return dict(A=Q+P,B=B,Q=Q,P=P,shift=shift,precision=full_precision,
                weights=weights,tags=tags)

def normalized_pencil(K,N,p,precision=10,padding=10,harmonic_deformation=0):
    raw=raw_pencil(K,N,p,precision+padding,harmonic_deformation);A=raw['A'];B=raw['B'];h=K-N
    S=raw['shift'];L=raw['precision'];
    cost=[[min(vp_mod(A[i,j],p,L),vp_mod(B[i,j],p,L))-S for j in range(h)] for i in range(h)]
    u,v,T=hungarian(cost)
    if max(u)+max(v)>padding:
        return normalized_pencil(K,N,p,precision,2*padding+max(u)+max(v),harmonic_deformation)
    modulus=p**precision
    def normalize(M):
        out=[]
        for i in range(h):
            row=[]
            for j in range(h):
                e=S+u[i]+v[j];a=int(M[i,j])
                if e>=0:
                    assert L-e>=precision and a%p**e==0
                    a//=p**e
                else:a*=p**(-e)
                row.append(a%modulus)
            out.append(row)
        return out
    aa=normalize(A);bb=normalize(B)
    Bmin=min(vp_mod(x,p,precision) for row in bb for x in row)
    cancellations={};max_cancellation=0
    for i in range(h):
        for j in range(h):
            before=min(vp_mod(raw['Q'][i,j],p,L),vp_mod(raw['P'][i,j],p,L))
            after=vp_mod(A[i,j],p,L);gain=after-before
            if gain:
                cancellations[str(gain)]=cancellations.get(str(gain),0)+1
                max_cancellation=max(max_cancellation,gain)
    return dict(A=aa,B=bb,rows=u,cols=v,tropical=T,B_min=Bmin,precision=precision,
                shift=S,component_cancellations=cancellations,
                component_cancellation_max_lower_bound=max_cancellation,tags=raw['tags'])

def audit():
    rows=[]
    for K,N,p in [(32,4,11),(40,5,17),(48,6,17),(64,8,23),(40,1,11),(40,1,17),(40,1,23)]:
        data=normalized_pencil(K,N,p,8);A,B,*_=local_data(K,N,p);h=K-N
        for i in range(h):
            for j in range(h):
                shift=data['rows'][i]+data['cols'][j]
                assert data['A'][i][j]==residue(A[i,j],p,shift,8)
                assert data['B'][i][j]==residue(B[i,j],p,shift,8)
        rows.append(dict(K=K,N=N,p=p,entries=2*h*h,tropical=data['tropical'],B_min=data['B_min']))
        print(json.dumps(rows[-1]),flush=True)
    result=dict(rows=rows,entries_checked=sum(r['entries'] for r in rows))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    print(json.dumps(audit()),flush=True)
