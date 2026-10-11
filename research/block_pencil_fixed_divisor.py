"""Exact uniform divisors for an infinite integer-parameter determinant family.

Degree in u is <=2h, so 2h+1 samples determine the fixed divisor for all
integer u, and for each progression u=a+p v. Sampling here is a theorem.
"""
import json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx
from joint_exact import content
from integer_block_pencils import experiment
from two_prefix_outer import vp


def gcdq(values):
    num=0;den=1
    for q in values:num=math.gcd(num,int(q.p));den=math.lcm(den,int(q.q))
    return fmpq(num,den)


def eval_newton(newton,u):
    b=1;out=fmpq_poly([])
    for k,P in enumerate(newton):
        out+=P*b;b=b*(u-k)//(k+1)
    return out


def main():
    K,N,L,s=24,1,3,1;h=K-N-L;d=2*h;values=[];samples=[]
    for u in range(d+1):
        row=experiment(K,N,L,s,u);samples.append(row)
        values.append(fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])*fmpq(row['content']))
    newton=[];layer=values.copy()
    while layer:
        newton.append(layer[0]);layer=[layer[i+1]-layer[i] for i in range(len(layer)-1)]
    uniform=gcdq(content(P) for P in newton if P)
    assert uniform==gcdq(content(P) for P in values)
    for u in (-3,-1,41,100):
        row=experiment(K,N,L,s,u)
        direct=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])*fmpq(row['content'])
        assert eval_newton(newton,u)==direct
    primes=[2,3,5,7,11,17,19,23];limit=(d+1)*max(primes);vps=[];diffs=newton.copy()
    for u in range(limit):
        P=diffs[0];ct=content(P);vps.append({p:vp(ct,p) for p in primes})
        assert all(c.q==1 for c in P/uniform)
        for k in range(d):diffs[k]+=diffs[k+1]
    rows=[]
    for p in primes:
        baseline=vp(uniform,p)
        exponents=[min(vps[a+p*v][p] for v in range(d+1)) for a in range(p)]
        assert min(exponents)==baseline
        rows.append(dict(p=p,unrestricted=baseline,classes=exponents,
                         extra_divisibility=[v-baseline for v in exponents],
                         best_residues=[a for a,v in enumerate(exponents) if v==max(exponents)],
                         baseline_u0=vps[0][p],class_u0=exponents[0]))
    with ctx.workprec(160):
        premium=arb(fmpq(samples[0]['content'])/uniform).log()/K**2
        info=dict(K=K,N=N,L=L,s=s,h=h,parameter_degree_bound=d,
                  actual_parameter_degree=max(k for k,P in enumerate(newton) if P),
                  uniform_content=str(uniform),prefix_content=samples[0]['content'],
                  prefix_over_uniform_log_per_K2=premium.str(30),
                  newton_coefficients=[[str(c) for c in P] for P in newton],
                  progression_results=rows,integer_values_checked=limit,
                  independent_parameter_checks=[-3,-1,41,100])
    Path(__file__).with_suffix('.json').write_text(json.dumps(info,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in info.items() if k not in ('newton_coefficients','uniform_content','prefix_content')}),flush=True)


if __name__=='__main__':main()
