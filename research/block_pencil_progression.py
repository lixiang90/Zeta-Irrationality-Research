"""An infinite progression retaining prefix content, with a real-side audit."""
import json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,arb_mat,ctx
from sympy import factorint
from joint_exact import entries_from_polynomial,Dcache,content
from block_pencil_fixed_divisor import eval_newton,gcdq
from integer_block_pencils import numerator
from two_prefix_outer import vp


def main():
    folder=Path(__file__).parent;data=json.loads((folder/'block_pencil_fixed_divisor.json').read_text())
    K,N,L,s,h=(data[k] for k in ('K','N','L','s','h'));d=2*h
    newton=[fmpq_poly([fmpq(c) for c in row]) for row in data['newton_coefficients']]
    power=[fmpq_poly([]) for _ in range(d+1)];choose=fmpq_poly([1]);t=fmpq_poly([0,1])
    for k,P in enumerate(newton):
        for j,c in enumerate(choose):power[j]+=P*c
        choose=choose*(t-k)/fmpq(k+1)
    ct0=fmpq(data['prefix_content']);G=fmpq(data['uniform_content']);ratio=ct0/G
    assert ratio.q==1
    factors=factorint(int(ratio.p));rows=[];modulus=1
    for p,extra in sorted(factors.items()):
        p=int(p);v0=vp(ct0,p)
        valuations=[None if not P else vp(content(P),p) for P in power]
        e=max([0]+[max(0,(v0-v+j-1)//j) for j,v in enumerate(valuations) if j and v is not None])
        assert all(v is None or v+e*j>=v0 for j,v in enumerate(valuations))
        tested=[]
        for j in range(e+1):
            exact=min(vp(content(eval_newton(newton,p**j*v)),p) for v in range(d+1))
            tested.append(exact)
        chosen=next(j for j,v in enumerate(tested) if v>=v0)
        modulus*=p**chosen
        rows.append(dict(p=p,prefix_valuation=v0,extra_over_unrestricted=int(extra),
                         coefficient_sufficient_exponent=e,exact_minimum_exponent=chosen,
                         progression_valuations=tested,power_coefficient_valuations=valuations))
    assert modulus>1
    # At every other prime the unrestricted fixed divisor already suffices.
    restricted=[eval_newton(newton,modulus*v) for v in range(d+1)]
    assert gcdq(content(P) for P in restricted)==ct0
    # Coefficient pencils of H(u)=u^2 A+u B+C, evaluated using rigorous balls.
    tensors={}
    for u in (-1,0,1):
        Q=numerator(N,L,s,u);tensors[u]=entries_from_polynomial(K,Dcache(N)**8*Q**2,h)
    aa=[];bb=[]
    for kind in (0,1):
        out=[]
        for j in range(2*h-1):
            A=(tensors[1][kind][j]+tensors[-1][kind][j]-2*tensors[0][kind][j])/2
            B=(tensors[1][kind][j]-tensors[-1][kind][j])/2
            out.append(modulus*modulus*A-modulus*B)
        (aa if kind==0 else bb).extend(out)
    bits=max(max(abs(int(v.p)).bit_length(),int(v.q).bit_length()) for v in aa+bb)+1500
    with ctx.workprec(bits):
        z=arb(7).zeta();vals=[arb(a)+arb(b)*z for a,b in zip(aa,bb)];certs=[]
        for n in range(1,h+1):
            mat=arb_mat(n,n,[vals[i+j] for i in range(n) for j in range(n)])
            det=mat.det();assert det>0,(n,bits)
            certs.append(dict(size=n,log_determinant_ball=det.log().str(25)))
    result=dict(K=K,N=N,L=L,s=s,h=h,modulus=str(modulus),prime_requirements=rows,
                exact_progression_uniform_content=str(ct0),progression_samples=d+1,
                positive_definite_matrix='H(-modulus)-H(0)',precision_bits=bits,
                sylvester_certificates=certs,
                scope='For every nonzero integer v, Delta(modulus*v,zeta7)/ct0 > Delta(0,zeta7)/ct0; actual specialized content may be larger.')
    (folder/'block_pencil_progression.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('sylvester_certificates','exact_progression_uniform_content','prime_requirements')}
                    |dict(prime_requirements=[{k:v for k,v in row.items() if k!='power_coefficient_valuations'} for row in rows])),flush=True)


if __name__=='__main__':main()
