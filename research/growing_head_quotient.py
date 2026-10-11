"""Exact kernel bases and output-lattice indices for growing head-zero spaces."""
import json
import math
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form
from flint import arb, ctx, fmpq, fmpz_poly
from critical_lift_probe import output_map


def kernel_polynomial(n, head, i):
    x=fmpz_poly([0,1])
    raw=(x-n-2*head-2)*(x+n)**8*(x-1)**(2*i)-(x-n)**8*(x+n+2*head+2)*(x+1)**(2*i)
    assert all(raw[j]==0 for j in range(1,raw.degree()+1,2))
    assert all(int(a)%2==0 for a in raw.coeffs())
    even=[int(raw[2*j])//2 for j in range(raw.degree()//2+1)]
    assert even[-1]==7*n-2*head-2*(i+1)
    content=math.gcd(*even)
    primitive=[a//content for a in even]
    return primitive,content


def check(n,head,w):
    assert 7*n-2*head-2*w>=1
    out,_=output_map(n,head=head,degrees=tuple(range(0,2*(w+4),2)))
    rows=[out[k] for k in (0,3,5,7)]
    diagonals=[];contents=[];kernels=[]
    for i in range(w):
        kernel,content=kernel_polynomial(n,head,i)
        diagonals.append(kernel[-1]);contents.append(content);kernels.append(kernel)
        for row in rows:
            assert sum((row[j]*kernel[j] for j in range(len(kernel))),fmpq(0))==0
    den=math.lcm(*(int(x.denominator) for row in rows for x in row))
    matrix=sp.Matrix([[int(x*den) for x in row] for row in rows])
    base=matrix[:,:4]
    base_det=abs(int(base.det()))
    assert base_det
    hnf=hermite_normal_form(matrix)
    full_det=abs(int(hnf.det()))
    assert base_det%full_det==0
    image_index=base_det//full_det
    triangular_index=math.prod(diagonals)
    assert triangular_index%image_index==0
    # Put eliminated coordinates last. Column HNF is upper triangular, so
    # its first two columns give the exact intersection with a3=a5=0.
    permuted=matrix[[0,3,1,2],:]
    h0=hermite_normal_form(permuted[:,:4])
    hw=hermite_normal_form(permuted)
    assert all(h0[i,j]==0 and hw[i,j]==0 for i in range(4) for j in range(i))
    target0=abs(int(h0[:2,:2].det()));targetw=abs(int(hw[:2,:2].det()))
    assert target0%targetw==0
    target_index=target0//targetw
    assert image_index%target_index==0
    inclusion=hw[:2,:2].inv()*h0[:2,:2]
    assert all(x.q==1 for x in inclusion)
    smith1=math.gcd(*(int(x) for x in inclusion))
    smith2=target_index//smith1
    assert smith2%smith1==0
    with ctx.workprec(128):
        log_index=(arb(image_index).log()/n).str(18)
        log_target_index=(arb(target_index).log()/n).str(18)
    return dict(n=n,head=head,w=w,domain_dimension=w+4,formal_output_rank=4,kernel_dimension=w,
                primitive_kernel_leading_coefficients=diagonals,kernel_contents=contents,
                primitive_kernel_coefficients=kernels,
                output_lattice_enlargement_index=str(image_index),
                log_output_index_per_n=log_index,
                target_plane_index=str(target_index),
                target_plane_smith_factors=[str(smith1),str(smith2)],
                log_target_plane_index_per_n=log_target_index,
                triangular_index_bound=str(triangular_index),
                raw_index_bound=str(math.prod(7*n-2*head-2*k for k in range(1,w+1))))


def main():
    rows=[]
    for n,head in ((2,0),(4,0),(4,4),(8,8),(12,12)):
        for w in (1,2,4):
            if 7*n-2*head-2*w>=1:
                row=check(n,head,w);rows.append(row)
                print(json.dumps({k:row[k] for k in ('n','head','w','output_lattice_enlargement_index','triangular_index_bound')}),flush=True)
    for n in (8,16,24):
        for w in sorted(set((n//2,n))):
            if any(r['n']==n and r['head']==n and r['w']==w for r in rows):continue
            row=check(n,n,w);rows.append(row)
            print(json.dumps({k:row[k] for k in ('n','head','w','log_output_index_per_n','log_target_plane_index_per_n')}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope='Exact finite checks of the general kernel and index theorem.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
