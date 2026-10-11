"""Coupled Schur layers with constant lifts of both mod-p kernels.

The lifted bottom block alone is deliberately compared with the true Schur
complement. Their difference starts at p^2 and can alter higher Smith layers.
"""
import argparse,json,time
from pathlib import Path
from flint import nmod_mat,fmpz_mod_ctx,fmpz_mod_mat
from distribution_modular import smith_mod
from coupled_pencil import normalized_pencil,mat,vp_mod

def counts(slopes):return {str(v):slopes.count(v) for v in sorted(set(slopes))}

def pivot_columns(M):
    R,rank=M.rref();out=[]
    for i in range(rank):out.append(next(j for j in range(R.ncols()) if R[i,j]))
    return out

def unit_inverse(A,p,precision):
    n=A.nrows();ctx=fmpz_mod_ctx(p**precision)
    reduced=nmod_mat(n,n,[int(A[i,j])%p for i in range(n) for j in range(n)],p)
    J0=reduced.inv()
    J=fmpz_mod_mat(n,n,[int(J0[i,j]) for i in range(n) for j in range(n)],ctx)
    I=fmpz_mod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],ctx)
    accuracy=1
    while accuracy<precision:J=J*(2*I-A*J);accuracy*=2
    assert A*J==I
    return J,J0

def split_layer(rows,p,precision):
    n=len(rows);M=mat(rows,p,precision)
    red=nmod_mat(n,n,[v%p for row in rows for v in row],p)
    cols=pivot_columns(red);r=len(cols)
    if r==n:return dict(rank=r,size=n),None
    if not r:
        assert all(v%p==0 for row in rows for v in row)
        return dict(rank=0,size=n,cross_term_zero=True),[[v//p for v in row] for row in rows]
    selected=nmod_mat(n,r,[rows[i][j]%p for i in range(n) for j in cols],p)
    rr=pivot_columns(selected.transpose())
    fr=[i for i in range(n) if i not in rr];fc=[j for j in range(n) if j not in cols]
    def block(rs,cs):return fmpz_mod_mat(len(rs),len(cs),[rows[i][j] for i in rs for j in cs],fmpz_mod_ctx(p**precision))
    A00=block(rr,cols);A01=block(rr,fc);A10=block(fr,cols);A11=block(fr,fc)
    J,J0=unit_inverse(A00,p,precision)
    b01=nmod_mat(r,n-r,[int(A01[i,j])%p for i in range(r) for j in range(n-r)],p)
    b10=nmod_mat(n-r,r,[int(A10[i,j])%p for i in range(n-r) for j in range(r)],p)
    right=-(J0*b01);left=-(b10*J0)
    R=fmpz_mod_mat(r,n-r,[int(right[i,j]) for i in range(r) for j in range(n-r)],fmpz_mod_ctx(p**precision))
    L=fmpz_mod_mat(n-r,r,[int(left[i,j]) for i in range(n-r) for j in range(r)],fmpz_mod_ctx(p**precision))
    E=A10+L*A00;F=A01+A00*R
    D=A11+L*A01+A10*R+L*A00*R
    cross=E*J*F;S=D-cross
    assert S==A11-A10*J*A01
    dd=[[int(D[i,j]) for j in range(n-r)] for i in range(n-r)]
    ss=[[int(S[i,j]) for j in range(n-r)] for i in range(n-r)]
    assert all(v%p==0 for row in dd+ss for v in row)
    cross_min=min(vp_mod(cross[i,j],p,precision) for i in range(n-r) for j in range(n-r))
    assert cross_min>=2
    naive,censored,_=smith_mod(dd,p,precision)
    actual,censored_actual,_=smith_mod(ss,p,precision)
    summary=dict(size=n,rank=r,residual_size=n-r,cross_term_min=cross_min,
                 naive_counts=counts(naive),naive_censored=censored,
                 schur_counts=counts(actual),schur_censored=censored_actual,
                 naive_sum=sum(naive),schur_sum=sum(actual),
                 pivot_rows=rr,pivot_columns=cols)
    return summary,[[v//p for v in row] for row in ss]

def integral_solve_certificate(A,B,p,precision):
    """Smith row operations applied to B; certify A^-1 B integral without inversion."""
    A=[row[:] for row in A];B=[row[:] for row in B];n=len(A);modulus=p**precision
    slopes=[];margins=[]
    for k in range(n):
        s,i,j=min((vp_mod(A[i][j],p,precision),i,j) for i in range(k,n) for j in range(k,n))
        if s>=precision:return dict(certified=False,reason='insufficient precision')
        A[k],A[i]=A[i],A[k];B[k],B[i]=B[i],B[k]
        for row in A:row[k],row[j]=row[j],row[k]
        divisor=p**s;localmod=modulus//divisor;inverse=pow(A[k][k]//divisor,-1,localmod)
        for i in range(k+1,n):
            assert A[i][k]%divisor==0
            factor=(A[i][k]//divisor)*inverse%localmod
            if factor:
                for j in range(k+1,n):A[i][j]=(A[i][j]-factor*A[k][j])%modulus
                for j in range(n):B[i][j]=(B[i][j]-factor*B[k][j])%modulus
            A[i][k]=0
        # Clearing the rest of the pivot row is an integral column operation.
        for j in range(k+1,n):assert A[k][j]%divisor==0;A[k][j]=0
        slopes.append(s);margins.append(min(vp_mod(v,p,precision) for v in B[k])-s)
    return dict(certified=min(margins)>=0,strict=min(margins)>0,
                row_margin=min(margins),smith_counts=counts(slopes))

def analyze(K,N,p,precision=10,solve=False):
    start=time.time();data=normalized_pencil(K,N,p,precision);matrix=data['A'];layers=[];slopes=[]
    for level in range(precision):
        if not matrix:break
        layer,matrix=split_layer(matrix,p,precision-level)
        layer['level']=level;slopes += [level]*layer['rank'];layers.append(layer)
    assert len(slopes)==K-N,'increase precision'
    generic=data['B_min']>=max(slopes);solve_result=None
    if solve or not generic:
        solve_result=integral_solve_certificate(data['A'],data['B'],p,precision)
        assert solve_result.get('smith_counts')==counts(slopes)
        generic=generic or solve_result['certified']
    result=dict(K=K,N=N,p=p,precision=precision,tropical=data['tropical'],B_min=data['B_min'],
                smith_counts=counts(slopes),smith_sum=sum(slopes),
                constant_valuation=data['tropical']+sum(slopes),generic_certified=generic,
                integral_solve=solve_result,component_cancellations=data['component_cancellations'],
                layers=layers,seconds=time.time()-start)
    if generic:result['gauss_valuation']=result['constant_valuation']
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='32:4:11,48:6:17,64:8:23,128:16:43')
    ap.add_argument('--out',default='coupled_schur.json');ap.add_argument('--solve',action='store_true')
    args=ap.parse_args();rows=[];out=Path(__file__).with_name(args.out)
    for item in args.pairs.split(','):
        r=analyze(*map(int,item.split(':')),solve=args.solve);rows.append(r)
        out.write_text(json.dumps(rows,indent=2))
        print(json.dumps({k:v for k,v in r.items() if k not in ['layers','component_cancellations']}),flush=True)
        for layer in r['layers']:
            print('LAYER '+json.dumps({k:v for k,v in layer.items() if k not in ['pivot_rows','pivot_columns']}),flush=True)
