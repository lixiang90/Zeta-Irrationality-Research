"""Finite exact rank classification in the independent principal-part basis."""
import json
from pathlib import Path
from flint import fmpz_mat

def matrix(nodes,h):
    rows=[]
    # Multiply each zeta5 row by 2 and each zeta6 row by 8.
    for nuisance in (5,6):
        for s in range(2*h-1):
            row=[]
            for x in nodes:
                r=-x*x;power=r**s
                row.extend([2*r*r*power,2*(s+2)*r*power,(s+1)*(s+2)*power] if nuisance==5 else
                           [0,20*x**3*power,-(35+20*s)*x*power])
            rows.append(row)
    return fmpz_mat(rows)

def main():
    records=[];exceptions=[]
    families=[('consecutive',lambda K:list(range(1,K+1)),24),
              ('odd_nodes',lambda K:[2*j-1 for j in range(1,K+1)],12),
              ('square_nodes',lambda K:[j*j for j in range(1,K+1)],12),
              ('geometric_nodes',lambda K:[2**j for j in range(K)],12)]
    for name,build,maximum in families:
        for K in range(2,maximum+1):
            nodes=build(K);ranks=[]
            for h in range(1,K+1):
                actual=matrix(nodes,h).rank();predicted=min(4*h-2,3*K)
                ranks.append(actual)
                if actual!=predicted:exceptions.append(dict(family=name,K=K,h=h,rank=actual,predicted=predicted))
            records.append(dict(family=name,K=K,nodes=nodes,h_range=[1,K],exact_ranks=ranks,
                                kernel_dimensions=[3*K-v for v in ranks]))
    out=dict(status='finite_exact_rank_classification_complete',records=records,total_rank_cases=sum(r['K'] for r in records),
             candidate_rank_formula='min(4*h-2,3*K)',exceptions=exceptions,
             scope='Finite exact classification only. The candidate formula has not been proved for all nodes or K.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(dict(status=out['status'],cases=out['total_rank_cases'],exceptions=exceptions),indent=2),flush=True)

if __name__=='__main__':main()
