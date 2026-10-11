"""Finite exact content search in the full integer-valued coordinate lattice."""
import argparse,json,itertools,math
from pathlib import Path
from flint import fmpq_poly
from growing_integer_space import basis,coordinates
from joint_exact import Dcache
from rational_square_nodes import experiment


def run(radius=4):
    K,N,L=24,1,3;P0=fmpq_poly(Dcache(N+L)//Dcache(N));ds=[basis(i)*math.factorial(L)**2 for i in range(L)]
    path=Path(__file__).with_name('growing_space_scan_K24.json');rows=[];best=None
    for u in itertools.product(range(-radius,radius+1),repeat=L):
        Q=P0+sum((d*v for d,v in zip(ds,u)),fmpq_poly([]));r=experiment(K,N,N+L,'integer',Q,'box')
        r['parameters']=list(u);r.pop('primitive_polynomial');rows.append(r)
        if best is None or r['score']<best['score']:
            best=r;print(json.dumps(dict(records=len(rows),u=u,score=r['score'],real=r['real'])),flush=True)
    path.write_text(json.dumps(dict(radius=radius,rows=rows),indent=2),encoding='utf-8')
    print(json.dumps(dict(records=len(rows),best={k:best[k] for k in ['parameters','score','real']})),flush=True)


def vertical():
    P=fmpq_poly(Dcache(4)//Dcache(1));rows=[]
    for c in range(-36,181):
        Q=P(fmpq_poly([-c,1]));cc=coordinates(Q/36)
        if any(x.q!=1 for x in cc):continue
        r=experiment(24,1,4,'integer',Q,'vertical_shift');r['shift']=c;rows.append(r)
    Path(__file__).with_name('growing_space_vertical_shifts.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--radius',type=int,default=4);p.add_argument('--vertical',action='store_true')
    a=p.parse_args();vertical() if a.vertical else run(a.radius)
