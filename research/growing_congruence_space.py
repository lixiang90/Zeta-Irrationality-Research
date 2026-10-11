"""Use small rounding costs to impose genuine scalar congruence constraints."""
import argparse,json,math
from pathlib import Path
import mpmath as mp
from flint import fmpq_poly
from growing_integer_space import basis,reduced_round
from joint_exact import Dcache
from rational_square_nodes import experiment


def run(K,N,L,moduli):
    folder=Path(__file__).parent;data=json.loads((folder/f'growing_trace_certificate_K{K}.json').read_text())
    mp.mp.dps=230;A=mp.matrix([[mp.mpf(v) for v in row] for row in data['trace_metric_A_midpoint']]);b=mp.matrix([mp.mpf(v) for v in data['trace_metric_b_midpoint']])
    center=mp.lu_solve(A,-b);P0=fmpq_poly(Dcache(N+L)//Dcache(N));ds=[basis(i)*math.factorial(L)**2 for i in range(L)]
    path=folder/f'growing_congruence_space_K{K}.json';rows=[]
    for modulus in moduli:
        u,T,norm=reduced_round(A,center/modulus);u=[modulus*v for v in u]
        Q=P0+sum((v*x for v,x in zip(ds,u)),fmpq_poly([]));r=experiment(K,N,N+L,'integer',Q,f'modulus_{modulus}')
        r.update(modulus=modulus,parameters=[str(x) for x in u]);rows.append(r)
        path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        print(json.dumps({k:r[k] for k in ['K','modulus','score','real','arithmetic_gain']}),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1);p.add_argument('--L',type=int,default=3)
    p.add_argument('--moduli',default='2,3,6,12,30,60,210');a=p.parse_args();run(a.K,a.N,a.L,list(map(int,a.moduli.split(','))))
