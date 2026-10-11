"""Exhaustive bounded positive-root slice of the rank-two locus modulo 67."""
import itertools
import json
from pathlib import Path
from root_module_deformation import *
from root_modular_rank_search import mulmod


def main():
    n=w=8;p=67;R=48;M=shifted_map(n,w)
    modM=[[int(x.numerator)*pow(int(x.denominator),-1,p)%p for x in row] for row in M]
    pairs=[]
    for r in range(R+1):
        a,b=node(n,r)%p,node(n,r+1)%p;pairs.append([a*b%p,-a-b,1])
    solutions=[];counts={};tested=0
    for t in itertools.combinations(range(R-2),4):
        starts=[x+i for i,x in enumerate(t)];H=[1]
        for s in starts:H=mulmod(H,pairs[s],p)
        C=[[sum(row[k+j]*v for k,v in enumerate(H))%p for j in range(3)] for row in modM]
        rank=mod_rank(C,p);counts[rank]=counts.get(rank,0)+1;tested+=1
        if rank!=2 or mod_rank([C[1],C[2]],p)!=2:continue
        if not all(any(C[i][j] for i in range(4)) for j in range(3)):continue
        solutions.append(starts)
    assert tested==math.comb(R-2,4)
    folder=Path(__file__).parent
    source=next(r for r in json.loads((folder/'growing_positive_moment.json').read_text())['rows'] if r['n']==8)
    lo=fmpq(source['lower']['endpoint']);hi=fmpq(source['upper']['endpoint'])
    records=[]
    # Inspect every solution, without selecting only an attractive example.
    for starts in solutions:
        second=starts[:];second[-1]+=p
        cert=module(n,w,[root_block(n,starts,True,M),root_block(n,second,True,M)],lo,hi)
        assert int(cert['target_smith'][0])%p==0
        records.append(dict(starts=starts,certificate=cert))
    result=dict(scope='All disjoint adjacent-pair starts 0<=s0<...<s3<=48, modulo 67; no extrapolation.',
                n=n,w=w,p=p,R=R,tested=tested,rank_counts=counts,solutions=solutions,records=records,
                counts_by_radius={str(r):sum(s[-1]<=r for s in solutions) for r in (8,12,16,20,24,32,40,48)})
    (folder/'root_short_lift_scan.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('tested',tested,'counts',counts,'solutions',len(solutions),'min radius',min(s[-1] for s in solutions),flush=True)
    print(result['counts_by_radius'],flush=True)
    print('two-sided',sum(r['certificate']['wedge'] is not None for r in records),flush=True)


if __name__=='__main__':main()
