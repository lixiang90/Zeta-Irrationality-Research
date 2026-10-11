"""Independent local polynomial division, not harmonic-logarithm jets."""
import json
import math
from pathlib import Path

from flint import fmpq, fmpq_poly


def jet(poly,center,size=7):
    coeffs=poly.coeffs()
    return [sum((coeffs[d]*math.comb(d,r)*center**(d-r)
                 for d in range(r,len(coeffs))),fmpq(0)) for r in range(size)]


def check(row):
    n=row['n'];L=row['head'];v=list(map(int,row['integer_lift']['nonnegative_shifted_coefficients']))
    assert all(a>=0 for a in v) and any(v)
    t=fmpq_poly([0,1]);x=2*t+n;y=x*x-(2*(L+1)+n)**2
    P=fmpq_poly([0])
    for a in reversed(v):P=P*y+a
    B=fmpq_poly([1]);D=fmpq_poly([1])
    for ell in range(1,L+1):B*=x*x-(n+2*ell)**2
    for j in range(n+1):D*=(t+j)**7
    N=B*P
    rebuilt=fmpq_poly([0]);out=[fmpq(0)]*8;h=[fmpq(0)]*8
    for j in range(n+1):
        if j:
            for k in range(1,8):h[k]+=fmpq(1,j**k)
        A,rem=divmod(D,(t+j)**7);assert rem==0
        aj=jet(A,-j);nj=jet(N,-j)
        local=[]
        for m in range(7):
            local.append((nj[m]-sum((aj[i]*local[m-i] for i in range(1,m+1)),fmpq(0)))/aj[0])
        for k in range(1,8):
            c=local[7-k]
            quotient,rem=divmod(D,(t+j)**k);assert rem==0
            rebuilt+=c*quotient
            out[k]+=c;out[0]-=c*h[k]
    assert rebuilt==N
    lam=fmpq(row['integer_lift']['unnormalized_output_scale'])
    a,b=map(int,row['primitive_output_pair'])
    assert out==[lam*a,0,0,0,0,0,0,lam*b]
    return dict(n=n,L=L,w=row['w'],numerator_degree=N.degree(),
                denominator_degree=D.degree(),partial_fraction_count=7*(n+1),
                full_polynomial_identity=True,exact_output_identity=True)


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'farey_cone_optimizer.json').read_text())['rows']
    results=[check(rows[0]),check(rows[-1])]
    (folder/'verify_farey_lift.json').write_text(json.dumps(dict(rows=results),indent=2),encoding='utf-8')
    print(json.dumps(results))


if __name__=='__main__':main()
