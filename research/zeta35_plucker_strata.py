"""Finite-degree content exponents on two exact Pluecker strata."""
import argparse,json,sys,time,math,itertools
from pathlib import Path
from flint import fmpz_mat as Z,fmpq_mat as Q
from zeta35_plucker_content import macaulay,modular_rank
from sympy import primerange
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
s=json.loads((ROOT/'zeta35_plucker_degree2.json').read_text())
parser=argparse.ArgumentParser()
parser.add_argument('--p12-max-degree',type=int,default=6)
parser.add_argument('--p13-max-degree',type=int,default=3)
args=parser.parse_args()
results=[]
for variables,max_degree in [([0,1,3],args.p12_max_degree),([0,1,2,3,4],args.p13_max_degree)]:
 pairs=list(itertools.combinations_with_replacement(variables,2));indices=[s['quadratic_monomials'].index(list(pair)) for pair in pairs];matrix=Z([[row[j] for j in indices] for row in s['hnf']]);hnf=matrix.hnf();H=[[int(hnf[i,j]) for j in range(len(pairs))] for i in range(hnf.nrows()) if any(hnf[i,j] for j in range(len(pairs)))];quad=[tuple((2 if i==a==b else 1 if i==a or i==b else 0) for i in variables) for a,b in pairs]
 print('STRATUM',variables,'QUADRATIC_RANK',len(H),flush=True)
 for degree in range(2,max_degree+1):
  start=time.perf_counter();mons,_,rows=macaulay(H,degree,quad);rank=modular_rank(rows,1000000007);item=dict(variables=variables,degree=degree,shape=[len(rows),len(mons)],modular_rank=rank)
  if rank==len(mons):
   HH=Z(rows).hnf();n=len(mons);basis=Z([[HH[i,j] for j in range(n)] for i in range(n)]);inverse=Q(basis).inv();d=math.lcm(*(int(v.denominator) for v in inverse.entries()));remaining=d;factors={}
   for p in primerange(2,10001):
    e=0
    while remaining%p==0:remaining//=p;e+=1
    if e:factors[int(p)]=e
   item.update(exponent=str(d),exponent_log=math.log(d),small_prime_factors=factors,remaining_factor=str(remaining),hnf=[[str(basis[i,j]) for j in range(n)] for i in range(n)])
  item['seconds']=time.perf_counter()-start;results.append(item);(ROOT/'zeta35_plucker_strata.json').write_text(json.dumps(dict(scope='exact restricted homogeneous row modules; not a polynomial-value lower bound',results=results),indent=2));print({k:v for k,v in item.items() if k not in ('hnf','exponent')},flush=True)

