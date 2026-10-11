"""Primitive directions retaining two roots: exact infinite progressions."""
import json
import math
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat, arb, arb_mat, ctx
from sympy import factorint
from directional_congruence import Family
from block_pencil_fixed_divisor import gcdq, eval_newton
from joint_exact import content
from two_prefix_outer import vp


def run():
    fam=Family();h=fam.h;d=2*h;ct0=content(fam.det([0]*3));rows=[]
    inverse=fmpq_mat(fam.E).inv()
    for col in range(3):
        den=math.lcm(*(int(inverse[i,col].q) for i in range(3)))
        v=[int(inverse[i,col]*den) for i in range(3)]
        g=math.gcd(*v);v=[x//g for x in v]
        direction=sum((x*p for x,p in zip(v,fam.ds)),fmpq_poly([]))
        if direction[2]<0:v=[-x for x in v];direction=-direction
        delta=int(direction[2]);j=col+2
        other=fmpq_poly(fam.Q0//fmpq_poly([j*j,1]));assert direction==delta*other
        values=[fam.det([x*k for x in v]) for k in range(d+1)]
        newton=[];layer=values.copy()
        while layer:
            newton.append(layer[0]);layer=[layer[i+1]-layer[i] for i in range(len(layer)-1)]
        G=gcdq(content(P) for P in newton if P);assert G==gcdq(content(P) for P in values)
        for k in (-3,-1,41,77):assert eval_newton(newton,k)==fam.det([x*k for x in v])
        power=[fmpq_poly([]) for _ in range(d+1)];choose=fmpq_poly([1]);t=fmpq_poly([0,1])
        for k,P in enumerate(newton):
            for i,c in enumerate(choose):power[i]+=P*c
            choose=choose*(t-k)/fmpq(k+1)
        ratio=ct0/G;assert ratio.q==1
        requirements=[];modulus=1
        for p,extra in sorted(factorint(int(ratio.p)).items()):
            p=int(p);v0=vp(ct0,p)
            valuations=[None if not P else vp(content(P),p) for P in power]
            sufficient=max([0]+[max(0,(v0-w+k-1)//k) for k,w in enumerate(valuations) if k and w is not None])
            tested=[min(vp(content(eval_newton(newton,p**e*k)),p) for k in range(d+1)) for e in range(sufficient+1)]
            selected=next(e for e,w in enumerate(tested) if w>=v0);modulus*=p**selected
            requirements.append(dict(p=p,baseline=v0,unrestricted_loss=int(extra),sufficient_exponent=sufficient,
                                     exact_minimum_exponent=selected,valuations=tested))
        actual=gcdq(content(eval_newton(newton,modulus*k)) for k in range(d+1))
        assert actual==ct0
        # This product modulus is necessary and sufficient: its prime factors
        # act independently by p-adic density of Z and p-adic units.
        a0,b0=fam.entries(fam.Q0);ap,bp=fam.entries(fam.Q0+direction);am,bm=fam.entries(fam.Q0-direction)
        aa=[(p+m-2*c)/2 for c,p,m in zip(a0,ap,am)];ab=[(p-m)/2 for p,m in zip(ap,am)]
        ba=[(p+m-2*c)/2 for c,p,m in zip(b0,bp,bm)];bb=[(p-m)/2 for p,m in zip(bp,bm)]
        bits=6000;cert=[]
        with ctx.workprec(bits):
            z=arb(7).zeta()
            for sign in (-1,1):
                vals=[arb(modulus**2*a+sign*modulus*b)+z*arb(modulus**2*c+sign*modulus*e)
                      for a,b,c,e in zip(aa,ab,ba,bb)]
                for n in range(1,h+1):
                    det=arb_mat(n,n,[vals[i+k] for i in range(n) for k in range(n)]).det();assert det>0
                    cert.append(dict(sign=sign,size=n,log_determinant_ball=det.log().str(25)))
            premium=(arb(ct0/G).log()/fam.K**2).str(30)
        # An exact scan on a specified finite interval complements the infinite
        # statement, which uses the common divisor only.
        candidates=[dict(k=k,**fam.score([x*k for x in v])) for k in range(-80,21)]
        row=dict(root=j,direction=v,root_shift_step=delta,degree_bound=d,uniform_divisor=str(G),
                 prefix_content=str(ct0),premium_ball=premium,restoring_modulus=str(modulus),
                 restoring_root_shift=str(modulus*delta),prime_requirements=requirements,
                 newton_coefficients=[list(map(str,P)) for P in newton],independent_parameters=[-3,-1,41,77],
                 positive_definite_certificates=cert,precision_bits=bits,candidates=candidates,
                 scope='Every nonzero multiple of the restoring modulus has raw determinant larger than the prefix; specialized excess content is not excluded.')
        rows.append(row)
        print(json.dumps({k:row[k] for k in ['root','direction','root_shift_step','premium_ball','restoring_modulus','restoring_root_shift']}
                         |dict(best=min(candidates,key=lambda r:r['score'])['k'])),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(K=24,N=1,L=3,h=h,rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':run()
