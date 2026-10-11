"""Bounded four-tail-pair slices as n grows; compatible modular target graphs."""
import itertools
import json
import math
from pathlib import Path
from root_module_deformation import *
from root_modular_rank_search import mulmod


def graph(B,p):
    """Target rows = S times nuisance rows, using a unit two-column pivot."""
    A=[B[1],B[2]]
    ij=next(((i,j) for i,j in itertools.combinations(range(3),2)
             if (A[0][i]*A[1][j]-A[0][j]*A[1][i])%p),None)
    if ij is None:return None
    i,j=ij;d=(A[0][i]*A[1][j]-A[0][j]*A[1][i])%p;inv=pow(d,-1,p)
    sig=[]
    for row in (B[0],B[3]):
        u=(row[i]*A[1][j]-row[j]*A[1][i])*inv%p
        v=(-row[i]*A[0][j]+row[j]*A[0][i])*inv%p
        if any((row[k]-u*A[0][k]-v*A[1][k])%p for k in range(3)):return None
        sig.extend((u,v))
    if not all(any(B[i][j] for i in range(4)) for j in range(3)):return None
    return tuple(sig)


def scan(n,p,source):
    w=n;R=3*n;M=shifted_map(n,w)
    Mp=[[int(x.numerator)*pow(int(x.denominator),-1,p)%p for x in row] for row in M]
    pairs=[]
    for r in range(R+1):
        a,b=node(n,r)%p,node(n,r+1)%p;pairs.append([a*b%p,(-a-b)%p,1])
    hits=[];slices=[]
    for name in ('lower','upper'):
        e=source[name];prefix=e['starts'][:-4];start=prefix[-1]+2 if prefix else (0 if e['infinity'] else 1)
        H=[1] if e['infinity'] else [0,1]
        for s in prefix:H=mulmod(H,pairs[s],p)
        compressed=[[sum(row[k+i]*v for i,v in enumerate(H))%p for k in range(11)] for row in Mp]
        tested=0;count=0
        for t in itertools.combinations(range(start,R-2),4):
            tail=[x+i for i,x in enumerate(t)];Q=[1]
            for s in tail:Q=mulmod(Q,pairs[s],p)
            B=[[sum(row[k+j]*v for k,v in enumerate(Q))%p for j in range(3)] for row in compressed]
            sig=graph(B,p);tested+=1
            if sig is None:continue
            block=root_block(n,prefix+tail,e['infinity'],M)
            C=fmpz_mat([[col[i] for col in block['columns']] for i in range(4)])
            assert mod_rank(rows_of(C),p)==2
            q=list(map(int,cross([C[1,j] for j in range(3)],[C[2,j] for j in range(3)])))
            if all(x<=0 for x in q):q=[-x for x in q]
            sign=0
            if all(x>=0 for x in q):
                val=sum(int(C[3,j])*q[j] for j in range(3));sign=(val>0)-(val<0)
            hits.append(dict(face=name,block=block,graph=list(sig),positive_single_block_sign=sign));count+=1
        assert tested==math.comb(R-start-2,4)
        slices.append(dict(face=name,prefix=prefix,start=start,tested=tested,hits=count))
        print('slice',n,name,tested,count,flush=True)
    groups={}
    for i,h in enumerate(hits):groups.setdefault(tuple(h['graph']),[]).append(i)
    modules=[];rank_deficient=[]
    lo=fmpq(source['lower']['endpoint']);hi=fmpq(source['upper']['endpoint'])
    for ids in groups.values():
        for i,j in itertools.combinations(ids,2):
            blocks=[hits[i]['block'],hits[j]['block']]
            C=fmpz_mat([[col[k] for block in blocks for col in block['columns']] for k in range(4)])
            if C.rank()<4:rank_deficient.append([i,j]);continue
            c=module(n,w,blocks,lo,hi);assert int(c['target_smith'][0])%p==0
            modules.append(dict(hit_indices=[i,j],certificate=c))
    opposite=[]
    for i,j in itertools.combinations(range(len(hits)),2):
        if hits[i]['positive_single_block_sign']*hits[j]['positive_single_block_sign']!=-1:continue
        s,t=hits[i]['graph'],hits[j]['graph']
        rank=mod_rank([[(s[2*a+b]-t[2*a+b])%p for b in range(2)] for a in range(2)],p)
        c=module(n,w,[hits[i]['block'],hits[j]['block']],lo,hi)
        assert c['wedge'] is not None
        assert mod_rank(c['matrix'],p)==2+rank
        assert sum(int(v)%p==0 for v in c['target_smith'])==2-rank
        opposite.append(dict(hit_indices=[i,j],graph_difference_rank=rank,certificate=c))
    return dict(n=n,w=w,p=p,R=R,slices=slices,hits=hits,groups=[v for v in groups.values()],
                compatible_modules=modules,rational_rank_deficient_pairs=rank_deficient,
                opposite_modules=opposite,
                positive_sign_counts={str(s):sum(h['positive_single_block_sign']==s for h in hits) for s in (-1,0,1)})


def main():
    folder=Path(__file__).parent
    sources=json.loads((folder/'growing_positive_moment.json').read_text())['rows'];rows=[]
    for n,p in ((8,67),(12,97),(16,131),(24,193)):
        row=scan(n,p,next(s for s in sources if s['n']==n));rows.append(row)
        print('case',n,'signs',row['positive_sign_counts'],'graphs',len(row['groups']),
              'compatible',len(row['compatible_modules']),'two-sided',sum(m['certificate']['wedge'] is not None for m in row['compatible_modules']),flush=True)
        (folder/'growing_rank_two_graphs.json').write_text(json.dumps(dict(
            scope='Exhaustive four-tail-pair slices, with fixed certified prefixes and root starts at most 3n. Not the full growing root space.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
