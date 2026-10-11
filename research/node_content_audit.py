"""Exact prime-by-prime audit of new node families against integer nodes."""
import json,math
from pathlib import Path
from flint import fmpq
from sympy import primerange
from two_prefix_outer import vp


def main():
    folder=Path(__file__).parent;rows=[]
    for K in (24,48,96):
        data=json.loads((folder/f'rational_square_nodes_K{K}.json').read_text())['rows']
        for r in data:
            if r['kind']=='integer':continue
            base=next(b for b in data if b['M']==r['M'] and b['kind']=='integer')
            ratio=fmpq(base['content'])/fmpq(r['content']);residual=ratio;local=[];bands={'p=2':0.,'2<p<=K':0.,'p>K':0.}
            for p in primerange(2,max(128,4*K+12*r['N']+20)):
                v=vp(ratio,p)
                if v:
                    residual/=fmpq(p)**v;value=v*math.log(p)/K**2
                    bands['p=2' if p==2 else '2<p<=K' if p<=K else 'p>K']+=value
                    local.append(dict(p=int(p),loss_exponent=v,loss_per_K2=value))
            assert residual==1,(K,r['kind'],residual)
            rows.append(dict(K=K,N=r['N'],M=r['M'],kind=r['kind'],real_change=r['real']-base['real'],
                             arithmetic_loss=base['arithmetic_gain']-r['arithmetic_gain'],bands=bands,local=local))
    (folder/'node_content_audit.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    print(json.dumps([r for r in rows if r['M']==r['K']//6 and r['kind'] in ('half','dense_half')]),flush=True)


if __name__=='__main__':main()
