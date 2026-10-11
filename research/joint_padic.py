"""Tropical duals, exact symbolic mod-p rank, and truncated p-adic Smith slopes.

The symbolic rank is over F_p(X), not a sampled specialization. Higher Smith
slopes are at stated integer X values; they are not claimed generic without proof.
"""
from math import log
from flint import fmpq,nmod_poly
from b8_hankel import vp

INF=10**9
def val(q,p): return INF if not q else vp(q.p,p)-vp(q.q,p)


def hungarian(cost):
    n=len(cost);u=[0]*(n+1);v=[0]*(n+1);match=[0]*(n+1);way=[0]*(n+1)
    for row in range(1,n+1):
        match[0]=row;j0=0;mins=[INF]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=match[j0];delta=INF;j1=0
            for j in range(1,n+1):
                if not used[j]:
                    cur=cost[i0-1][j-1]-u[i0]-v[j]
                    if cur<mins[j]: mins[j]=cur;way[j]=j0
                    if mins[j]<delta: delta=mins[j];j1=j
            assert delta<INF
            for j in range(n+1):
                if used[j]:u[match[j]]+=delta;v[j]-=delta
                else:mins[j]-=delta
            j0=j1
            if match[j0]==0:break
        while True:
            j1=way[j0];match[j0]=match[j1];j0=j1
            if j0==0:break
    u=u[1:];v=v[1:]
    assert all(u[i]+v[j]<=cost[i][j] for i in range(n) for j in range(n))
    return u,v,sum(u)+sum(v)


def residue(q,p,shift,precision=1):
    if not q:return 0
    num=int(q.p);den=int(q.q)
    an=vp(num,p);ad=vp(den,p);exponent=an-ad-shift
    assert exponent>=0
    if exponent>=precision:return 0
    modulus=p**precision
    return (num//p**an)*pow(den//p**ad,-1,modulus)*pow(p,exponent,modulus)%modulus


def symbolic_rank(M,p):
    """Fraction-free Bareiss elimination over the polynomial domain F_p[X]."""
    a=[row[:] for row in M];n=len(a);prev=nmod_poly([1],p)
    rank=0
    for k in range(n):
        pivots=[(a[i][j].degree(),i,j) for i in range(k,n) for j in range(k,n) if a[i][j]]
        if not pivots:break
        _,i,j=min(pivots)
        a[k],a[i]=a[i],a[k]
        if j!=k:
            for row in a:row[k],row[j]=row[j],row[k]
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*a[i][j]-a[i][k]*a[k][j]
                quotient,remainder=divmod(numerator,prev)
                assert not remainder
                a[i][j]=quotient
            a[i][k]=nmod_poly([],p)
        prev=pivot;rank+=1
    return rank


def smith_slopes(A,B,p,rows,cols,x,precision=48):
    n=A.nrows();modulus=p**precision
    mat=[[residue(A[i,j]+x*B[i,j],p,rows[i]+cols[j],precision) for j in range(n)] for i in range(n)]
    shift=0;out=[]
    for k in range(n):
        best=None
        for i in range(k,n):
            for j in range(k,n):
                if mat[i][j]:
                    v=vp(mat[i][j],p)
                    if best is None or v<best[0]:best=(v,i,j)
                    if v==0:break
            if best and best[0]==0:break
        if best is None:raise ValueError("increase p-adic precision or avoid a singular specialization")
        exponent,i,j=best
        if exponent:
            divisor=p**exponent
            for r in range(k,n):
                for c in range(k,n):
                    assert mat[r][c]%divisor==0
                    mat[r][c]//=divisor
            shift+=exponent;modulus//=divisor
        mat[k],mat[i]=mat[i],mat[k]
        if j!=k:
            for row in mat:row[k],row[j]=row[j],row[k]
        inv=pow(mat[k][k],-1,modulus)
        for i in range(k+1,n):
            factor=mat[i][k]*inv%modulus
            if factor:
                for j in range(k+1,n):mat[i][j]=(mat[i][j]-factor*mat[k][j])%modulus
            mat[i][k]=0
        out.append(shift)
    return out


def analyze(A,B,polyF,p,symbolic=True):
    n=A.nrows();cost=[[min(val(A[i,j],p),val(B[i,j],p)) for j in range(n)] for i in range(n)]
    rows,cols,T=hungarian(cost)
    actual=min(val(c,p) for c in polyF)
    assert actual>=T
    result=dict(p=p,tropical=T,exact=actual,excess=actual-T)
    if symbolic:
        M=[[nmod_poly([residue(A[i,j],p,rows[i]+cols[j]),residue(B[i,j],p,rows[i]+cols[j])],p)
            for j in range(n)] for i in range(n)]
        rank=symbolic_rank(M,p)
        result.update(symbolic_rank=rank,first_gain=n-rank)
        assert T+n-rank<=actual
    for x in (0,1):
        slopes=smith_slopes(A,B,p,rows,cols,x)
        measured=val(polyF(fmpq(x)),p)
        assert T+sum(slopes)==measured,(p,x,T,slopes,measured)
        result[f"slopes_at_{x}"]={str(s):slopes.count(s) for s in sorted(set(slopes))}
        result[f"extra_at_{x}"]=measured-actual
        if symbolic: assert slopes.count(0)<=result["symbolic_rank"]
    return result
