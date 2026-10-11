"""Finite-field search for rank-two root blocks with nuisance rank two."""
import json
import random
from pathlib import Path
from root_module_deformation import mod_rank, node, shifted_map


def mulmod(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c


def scan(n,w,p):
    M=shifted_map(n,w)
    M=[[int(x.numerator)*pow(int(x.denominator),-1,p)%p for x in row] for row in M]
    pair=[]
    for r in range(p):
        a,b=node(n,r)%p,node(n,r+1)%p
        pair.append([a*b%p,-a-b,1])
    H=[1];prefix=list(range(0,w-4,2))
    for s in prefix:H=mulmod(H,pair[s],p)
    solutions=[];rank_counts={};nuisance_two=0;nonzero_columns=0
    for a in range(p):
        h=mulmod(H,pair[a],p)
        for b in range(a,p):
            poly=mulmod(h,pair[b],p)
            C=[[sum(row[k+j]*v for k,v in enumerate(poly))%p for j in range(3)] for row in M]
            rank=mod_rank(C,p);rank_counts[rank]=rank_counts.get(rank,0)+1
            if rank>2:continue
            if mod_rank([C[1],C[2]],p)!=2:continue
            nuisance_two+=1
            if not all(any(C[i][j] for i in range(4)) for j in range(3)):continue
            nonzero_columns+=1;solutions.append(dict(residues=[a,b],matrix=C))
    return dict(n=n,w=w,p=p,prefix=prefix,tested=p*(p+1)//2,rank_counts=rank_counts,
                rank_two_with_nuisance_two=nuisance_two,nonzero_columns=nonzero_columns,solutions=solutions)


def broad_scan(trials=30000):
    n=w=8;p=67;M=shifted_map(n,w)
    M=[[int(x.numerator)*pow(int(x.denominator),-1,p)%p for x in row] for row in M]
    pairs=[]
    for r in range(p):
        a,b=node(n,r)%p,node(n,r+1)%p;pairs.append([a*b%p,-a-b,1])
    rng=random.Random(20261002);counts={};solutions=[]
    for trial in range(trials):
        starts=sorted(rng.randrange(p) for _ in range(4));H=[1]
        for r in starts:H=mulmod(H,pairs[r],p)
        C=[[sum(row[k+j]*v for k,v in enumerate(H))%p for j in range(3)] for row in M]
        rank=mod_rank(C,p);counts[rank]=counts.get(rank,0)+1
        if rank==2 and mod_rank([C[1],C[2]],p)==2 and all(any(C[i][j] for i in range(4)) for j in range(3)):
            solutions.append(dict(trial=trial,starts=starts,matrix=C))
    return dict(n=n,w=w,p=p,trials=trials,seed=20261002,rank_counts=counts,solutions=solutions)


if __name__=='__main__':
    rows=[]
    for n,w,p in ((8,8,67),(8,8,71),(8,8,101),(8,8,131)):
        row=scan(n,w,p);rows.append(row)
        print(n,w,p,row['rank_counts'],'usable',len(row['solutions']),flush=True)
    broad=broad_scan();print('broad search',broad['rank_counts'],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope='Exhaustive two-residue slices and a seeded four-residue sample.',rows=rows,broad=broad),indent=2),encoding='utf-8')
