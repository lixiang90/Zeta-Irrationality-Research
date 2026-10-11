"""Whole-pencil valuation bounds from integral operations and assignment duals.

All transformations modulo p^L are lifts of integer unimodular operations.
Entry lower bounds and assignment duals certify ALL coefficients of det(A+XB).
An exact determinant specialization supplies the matching upper bound.
"""
import argparse,json,time
from pathlib import Path
from flint import fmpq as Q,fmpq_mat
import zeta35_mixed_moments as mixed
from zeta35_target31 import primes_to
from zeta35_pole_cancellation import val
from zeta35_local_layers import vp_int

def assignment(cost):
    n=len(cost);u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i;j0=0;mins=[10**9]*(n+1);used=[False]*(n+1)
        while True:
            used[j0]=True;i0=p[j0];delta=10**9;j1=0
            for j in range(1,n+1):
                if not used[j]:
                    cur=cost[i0-1][j-1]-u[i0]-v[j]
                    if cur<mins[j]:mins[j]=cur;way[j]=j0
                    if mins[j]<delta:delta=mins[j];j1=j
            for j in range(n+1):
                if used[j]:u[p[j]]+=delta;v[j]-=delta
                else:mins[j]-=delta
            j0=j1
            if p[j0]==0:break
        while True:
            j1=way[j0];p[j0]=p[j1];j0=j1
            if j0==0:break
    match=[0]*n
    for j in range(1,n+1):match[p[j]-1]=j-1
    lower=sum(u[1:])+sum(v[1:])
    assert lower==sum(cost[i][match[i]] for i in range(n))
    assert all(u[i+1]+v[j+1]<=cost[i][j] for i in range(n) for j in range(n))
    return dict(lower=lower,row_weights=u[1:],column_weights=v[1:],matching=match)

def transform(A,B,p,precision=18):
    n=A.nrows();s=max(0,-min(val(A[i,j],p) for i in range(n) for j in range(n) if A[i,j]))
    modulus=p**precision
    def reduce(M):
        result=[]
        for i in range(n):
            row=[]
            for j in range(n):
                q=M[i,j]*p**s
                row.append(int(q.numerator)*pow(int(q.denominator),-1,modulus)%modulus)
            result.append(row)
        return result
    a=reduce(A);b=reduce(B);layers=[];operations=[]
    for k in range(n):
        best=(precision,k,k)
        for i in range(k,n):
            for j in range(k,n):
                w=vp_int(a[i][j],p,precision)
                if w<best[0]:best=(w,i,j)
                if w==0:break
            if best[0]==0:break
        w,i,j=best
        if w==precision:raise ValueError('increase precision')
        a[k],a[i]=a[i],a[k];b[k],b[i]=b[i],b[k]
        for row in a:row[k],row[j]=row[j],row[k]
        for row in b:row[k],row[j]=row[j],row[k]
        power=p**w;inverse=pow(a[k][k]//power,-1,modulus//power)
        left=[];right=[]
        for i in range(k+1,n):
            factor=(a[i][k]//power)*inverse%(modulus//power);left.append(factor)
            if factor:
                for j in range(k+1,n):a[i][j]=(a[i][j]-factor*a[k][j])%modulus
                for j in range(n):b[i][j]=(b[i][j]-factor*b[k][j])%modulus
            a[i][k]=0
        for j in range(k+1,n):
            factor=(a[k][j]//power)*inverse%(modulus//power);right.append(factor)
            if factor:
                for i in range(n):b[i][j]=(b[i][j]-factor*b[i][k])%modulus
            a[k][j]=0
        layers.append(w-s)
        operations.append(dict(pivot=best,row_factors=list(map(str,left)),column_factors=list(map(str,right))))
    costs=[[min((layers[i] if i==j else precision-s),vp_int(b[i][j],p,precision)-s)
            for j in range(n)] for i in range(n)]
    cert=assignment(costs)
    return dict(p=p,precision=precision,scale=s,constant_layers=layers,
        transformed_B_scaled_mod_pL=[[str(x) for x in row] for row in b],
        operations=operations,entry_bounds=costs,**cert)

def run(n):
    start=time.perf_counter();K,N,h,a5,bs=mixed.original.entries(n);a3=mixed.shifted_mu3_entries(n)
    B=fmpq_mat([[bs[i+j] for j in range(h)] for i in range(h)])
    assert all(x.denominator==1 for x in B.entries())
    As=[fmpq_mat([[a5[i+j]-aa*a3[i+j] for j in range(h)] for i in range(h)]) for aa in (0,3)]
    det0=[a.det() for a in As]
    prior=json.loads(Path(__file__).with_name(f'zeta35_target31_n{n}.json').read_text())
    rows=[];outpath=Path(__file__).with_name(f'zeta35_pencil_certificate_n{n}.json')
    for p in primes_to(52*n+2):
        if 3*p<=K:continue
        for index,(aa,A) in enumerate(zip((0,3),As)):
            c=transform(A,B,p)
            assert sum(c['constant_layers'])==val(det0[index],p)
            exact=val(Q(prior['rows'][index]['content']),p)
            assert c['lower']<=exact
            witness=None
            for x in range(3):
                det=det0[index] if x==0 else (A+x*B).det()
                value=val(det,p)
                if value==c['lower']:
                    witness=dict(x=x,determinant_valuation=value);break
            c.update(a=aa,b=1,previous_exact_content_valuation=exact,
                     specialization_witness=witness,sharp=(witness is not None))
            if witness:assert c['lower']==exact
            rows.append(c)
            print('n',n,'p',p,'a',aa,'bound',c['lower'],'exact',exact,'witness',witness,flush=True)
        outpath.write_text(json.dumps(dict(n=n,K=K,h=h,rows=rows,seconds=time.perf_counter()-start),indent=2),encoding='utf-8')
    print('summary',n,'sharp',sum(r['sharp'] for r in rows),'total',len(rows),'seconds',time.perf_counter()-start,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('n',type=int)
    run(parser.parse_args().n)
