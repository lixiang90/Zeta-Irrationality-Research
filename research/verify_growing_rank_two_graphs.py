"""Independent maps and complete rescan of the bounded root slices."""
import itertools
import json
import math
from pathlib import Path
from fractions import Fraction as F
from verify_root_module_deformation import independent_map,verify,rankmod,det,node


def mulmod(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return c


def signature(B,p):
    pivot=next(((i,j) for i,j in itertools.combinations(range(3),2)
                if (B[1][i]*B[2][j]-B[1][j]*B[2][i])%p),None)
    if pivot is None:return None
    i,j=pivot;other=3-i-j
    if any(det([[B[r][k] for k in range(3)] for r in (1,2,target)])%p for target in (0,3)):return None
    if not all(any(B[i][j] for i in range(4)) for j in range(3)):return None
    a,b,c,d=B[1][i],B[1][j],B[2][i],B[2][j];inv=pow((a*d-b*c)%p,-1,p)
    return [(B[t][i]*d-B[t][j]*c)*inv%p if z==0 else
            (B[t][j]*a-B[t][i]*b)*inv%p for t in (0,3) for z in (0,1)]


def main():
    folder=Path(__file__).parent;data=json.loads((folder/'growing_rank_two_graphs.json').read_text())
    sources=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    total=modules=hit_count=0;opposite_ranks={0:0,1:0,2:0}
    for row in data['rows']:
        n,p,R=row['n'],row['p'],row['R'];source=next(s for s in sources if s['n']==n)
        M=independent_map(n,n)
        Mp=[[x.numerator*pow(x.denominator,-1,p)%p for x in line] for line in M]
        pairs=[[node(n,r)*node(n,r+1)%p,(-node(n,r)-node(n,r+1))%p,1] for r in range(R+1)]
        found=[]
        for sl in row['slices']:
            name=sl['face'];edge=source[name];prefix=edge['starts'][:-4]
            assert prefix==sl['prefix'];start=prefix[-1]+2 if prefix else (0 if edge['infinity'] else 1)
            assert start==sl['start'];H=[1] if edge['infinity'] else [0,1]
            for s in prefix:H=mulmod(H,pairs[s],p)
            compressed=[[sum(line[i+k]*v for i,v in enumerate(H))%p for k in range(11)] for line in Mp]
            tested=0;hits=0
            for t in itertools.combinations(range(start,R-2),4):
                tail=[a+i for i,a in enumerate(t)];Q=[1]
                for s in tail:Q=mulmod(Q,pairs[s],p)
                B=[[sum(line[k+j]*v for k,v in enumerate(Q))%p for j in range(3)] for line in compressed]
                sig=signature(B,p);tested+=1
                if sig is not None:found.append((name,prefix+tail,sig));hits+=1
            assert tested==sl['tested'] and hits==sl['hits'];total+=tested
        assert len(found)==len(row['hits']);hit_count+=len(found)
        for (name,starts,sig),hit in zip(found,row['hits']):
            assert name==hit['face'] and starts==hit['block']['starts'] and sig==hit['graph']
            cols=hit['block']['columns'];C=[[c[i] for c in cols] for i in range(4)]
            assert signature(C,p)==sig
            q=[C[1][1]*C[2][2]-C[1][2]*C[2][1],C[1][2]*C[2][0]-C[1][0]*C[2][2],C[1][0]*C[2][1]-C[1][1]*C[2][0]]
            if all(x<=0 for x in q):q=[-x for x in q]
            z=sum(a*b for a,b in zip(C[3],q));sign=((z>0)-(z<0)) if all(x>=0 for x in q) else 0
            assert sign==hit['positive_single_block_sign']
        lo,hi=F(source['lower']['endpoint']),F(source['upper']['endpoint'])
        groups={}
        for i,h in enumerate(row['hits']):groups.setdefault(tuple(h['graph']),[]).append(i)
        assert list(groups.values())==row['groups']
        expected_compatible={tuple(ij) for ids in groups.values() for ij in itertools.combinations(ids,2)}
        assert expected_compatible=={tuple(m['hit_indices']) for m in row['compatible_modules']}|{tuple(ij) for ij in row['rational_rank_deficient_pairs']}
        for rec in row['compatible_modules']+row['opposite_modules']:
            c=rec['certificate'];i,j=rec['hit_indices']
            assert c['blocks']==[row['hits'][i]['block'],row['hits'][j]['block']]
            C=verify(c,lo,hi);modules+=1
            S,T=row['hits'][i]['graph'],row['hits'][j]['graph'];difference=[[S[2*a+b]-T[2*a+b] for b in range(2)] for a in range(2)]
            r=rankmod(difference,p);assert rankmod(C,p)==2+r
            assert sum(int(x)%p==0 for x in c['target_smith'])==2-r
            if 'graph_difference_rank' in rec:
                assert r==rec['graph_difference_rank'];opposite_ranks[r]+=1;assert c['wedge'] is not None
            else:assert r==0
        print('verified growing slice',n,'hits',len(found),flush=True)
    result=dict(status='passed',independent_root_configurations=total,rank_two_blocks=hit_count,
                fully_verified_modules=modules,opposite_graph_difference_ranks=opposite_ranks)
    (folder/'verify_growing_rank_two_graphs.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(result,flush=True)


if __name__=='__main__':main()
