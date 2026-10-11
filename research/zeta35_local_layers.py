"""Finite p-adic Smith layers of constant terms, checked against exact dets."""
import argparse,json
from collections import Counter
from pathlib import Path
from flint import fmpq as Q,fmpq_mat
import zeta35_mixed_moments as mixed
from zeta35_target31 import primes_to
from zeta35_pole_cancellation import val

def vp_int(a,p,cap):
    if not a:return cap
    v=0
    while a%p==0:a//=p;v+=1
    return v

def smith_layers(A,p,precision=16):
    n=A.nrows();s=max(0,-min(val(A[i,j],p) for i in range(n) for j in range(n) if A[i,j]))
    modulus=p**precision
    mat=[]
    for i in range(n):
        row=[]
        for j in range(n):
            q=A[i,j]*p**s
            row.append(int(q.numerator)*pow(int(q.denominator),-1,modulus)%modulus)
        mat.append(row)
    result=[]
    for k in range(n):
        best=(precision,k,k)
        for i in range(k,n):
            for j in range(k,n):
                v=vp_int(mat[i][j],p,precision)
                if v<best[0]:best=(v,i,j)
                if v==0:break
            if best[0]==0:break
        v,i,j=best
        if v==precision:raise ValueError('increase local precision')
        mat[k],mat[i]=mat[i],mat[k]
        for row in mat:row[k],row[j]=row[j],row[k]
        power=p**v;inv=pow(mat[k][k]//power,-1,modulus//power)
        for i in range(k+1,n):
            factor=(mat[i][k]//power)*inv%(modulus//power)
            if factor:
                for j in range(k+1,n):mat[i][j]=(mat[i][j]-factor*mat[k][j])%modulus
            mat[i][k]=0
        result.append(v-s)
    assert result==sorted(result)
    return result

def main(n):
    K,N,h,a5,B=mixed.original.entries(n);a3=mixed.shifted_mu3_entries(n)
    pure=fmpq_mat([[a5[i+j] for j in range(h)] for i in range(h)])
    target=fmpq_mat([[a5[i+j]-3*a3[i+j] for j in range(h)] for i in range(h)])
    determinants=[pure.det(),target.det()]
    prior=json.loads(Path(__file__).with_name(f'zeta35_target31_n{n}.json').read_text())
    contents=[Q(row['content']) for row in prior['rows']]
    rows=[]
    for p in primes_to(52*n+2):
        if 3*p<=K:continue
        layers=[smith_layers(M,p) for M in (pure,target)]
        detv=[val(d,p) for d in determinants]
        assert [sum(x) for x in layers]==detv
        contentv=[val(c,p) for c in contents]
        row=dict(p=p,pure_layers=dict(Counter(layers[0])),target_layers=dict(Counter(layers[1])),
            determinant_valuations=detv,content_valuations=contentv,
            constant_attains_content=[a==b for a,b in zip(detv,contentv)])
        rows.append(row)
    out=dict(n=n,K=K,h=h,scope='Smith layers at X=0 only, not a polynomial Smith form',rows=rows)
    Path(__file__).with_name(f'zeta35_local_layers_n{n}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('n',type=int)
    main(parser.parse_args().n)
