"""Independent base determinant, limiting algebra, and rational-stagnation audit."""
import json
import math
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def multiply(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c


def determinant(a):
    a=[row[:] for row in a]
    result=F(1)
    for i in range(len(a)):
        p=next(j for j in range(i,len(a)) if a[j][i])
        if p!=i:
            a[p],a[i]=a[i],a[p]
            result=-result
        pivot=a[i][i]
        result*=pivot
        for j in range(i+1,len(a)):
            q=a[j][i]/pivot
            a[j]=[x-q*y for x,y in zip(a[j],a[i])]
    return result


def base_matrix():
    rows=[[F(0)]*4 for _ in range(4)]
    for col in range(4):
        for j in range(3):
            denominator=[F(1)]
            for ell in range(3):
                if ell!=j:
                    denominator=multiply(denominator,[F(math.comb(7,r)*(ell-j)**(7-r)) for r in range(8)])
            degree=2*col
            numerator=[F(math.comb(degree,r)*2**r*(2-2*j)**(degree-r))
                       for r in range(degree+1)]+[F(0)]*(6-degree)
            quotient=[]
            for r in range(7):
                quotient.append((numerator[r]-sum(denominator[k]*quotient[r-k] for k in range(1,r+1)))/denominator[0])
            for k in range(1,8):
                c=quotient[7-k]
                rows[0][col]-=c*sum((F(1,ell**k) for ell in range(1,j+1)),F(0))
                if k in (3,5,7): rows[(3,5,7).index(k)+1][col]+=c
    return rows


def main():
    base=base_matrix()
    assert determinant(base)==F(-45,8192)
    data=json.loads(Path(__file__).with_name('determinant_shape_probe.json').read_text(encoding='utf-8'))
    z,x,y=sp.symbols('z x y')
    kernel=5*z**4-28*z**3-154*z**2-76*z-3
    polynomial=(y+27)*(y**3+573091*y**2+17973501862*y-3125)
    resultant=sp.resultant(kernel,y*(z-1)**8-1024*(z-9)**3,z)
    assert sp.expand(resultant-2**64*polynomial)==0
    matrix=sp.Matrix([[sp.Rational(a) for a in row] for row in data['limiting_recurrence']['matrix']])
    assert sp.expand(matrix.charpoly(y).as_expr()-polynomial)==0
    assert sp.expand(kernel.subs(z,(2*x+1)**2)-256*((x-1)*(x+1)**8-x**8*(x+2)))==0
    cubic=y**3+573091*y**2+17973501862*y-3125
    intervals=[(-539795,-539793),(-33298,-33296),(F(0),F(1,10**6))]
    assert all(cubic.subs(y,a)*cubic.subs(y,b)<0 for a,b in intervals)
    # Independent exact Gauss reduction of a rational target with shrinking area.
    rational_models=[]
    for n in (2,4,8,16):
        E=F(1,2**n); delta=F(1,2**(4*n)); eps=E*E*delta; r=F(3,2)
        G=[[1/E**2,r/E**2],[r/E**2,(r*r+eps*eps)/E**2]]
        def dot(a,b): return sum(a[i]*G[i][j]*b[j] for i in range(2) for j in range(2))
        a,b=[1,0],[0,1]
        while True:
            if dot(b,b)<dot(a,a): a,b=b,a
            ratio=dot(a,b)/dot(a,a)
            if abs(ratio)<=F(1,2): break
            v=ratio+F(1,2); k=v.numerator//v.denominator
            b=[b[i]-k*a[i] for i in range(2)]
        assert dot(a,a)==(2*E*delta)**2
        assert E*E*dot(b,b)==F(1,4)+eps*eps
        rational_models.append(dict(n=n,first_squared=str(dot(a,a)),scaled_second_squared=str(E*E*dot(b,b))))
    result=dict(base_determinant=str(determinant(base)),base_matrix=[[str(v) for v in row] for row in base],
                independent_resultant_and_characteristic_polynomial=True,saddle_polynomial_identity=True,
                cubic_root_intervals=[[str(a),str(b)] for a,b in intervals],rational_stagnation_models=rational_models)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('Independent Fraction/SymPy verification passed: base determinant, spectral algebra, saddle identity, and 4 rational models.')


if __name__=='__main__': main()
