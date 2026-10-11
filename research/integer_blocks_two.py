"""Two disjoint block scan with a fixed total number of deleted poles."""
import json
from pathlib import Path
from integer_blocks import experiment


def main():
    K,N,total=24,1,3;rows=[];path=Path(__file__).with_name('integer_blocks_two.json')
    for L1 in (1,2):
        L2=total-L1
        for a in range(N,K-total+1):
            for b in range(a+L1,K-L2+1):
                row=experiment(K,N,[(a,L1),(b,L2)]);rows.append(row)
            path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        best=min(rows,key=lambda r:r['score'])
        print(json.dumps(dict(rows=len(rows),best_blocks=best['blocks'],best_score=best['score'])),flush=True)
    path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
