"""Exact classification of rational polynomial seeds in a restricted CF family.

This classifies symmetric polynomial solutions, not all CFs and not all limits.
The zeta3 coefficient below is a local Laurent coefficient only unless a global
telescoping identity is also supplied.
"""
import json
from pathlib import Path
import sympy as s

x,d=s.symbols('x d')
t=x*(x+1)


def classify(r):
    c=2*r*(r+2)
    basis=[t**j for j in range(r+1)]
    columns=[]
    for f in basis:
        L=s.expand((x+1)**5*f.subs(x,x+1)+x**5*f.subs(x,x-1)
                   -(x**5+(x+1)**5+c*(x**3+(x+1)**3))*f)
        residual,rem=s.div(L,2*x+1,x)
        assert rem==0
        col=[s.S(0)]*(r+1)
        for j in reversed(range(r+1)):
            col[j]=s.expand(residual).coeff(x,2*j)
            residual=s.expand(residual-col[j]*basis[j])
        assert residual==0
        columns.append(col)
    M=s.Matrix(r+1,r+1,lambda i,j:columns[j][i])
    cp=M.charpoly(d).as_expr()
    roots=s.polys.polytools.ground_roots(cp,d)
    rows=[]
    for root in roots:
        null=(M-root*s.eye(r+1)).nullspace()
        assert len(null)==1
        v=null[0]/null[0][-1]
        w=s.expand(sum(v[j]*basis[j] for j in range(r+1)))
        assert s.expand((x+1)**5*w.subs(x,x+1)+x**5*w.subs(x,x-1)
                        -(x**5+(x+1)**5+c*(x**3+(x+1)**3)+root*(2*x+1))*w)==0
        w0=w.subs(x,0)
        if w0:
            product=s.Poly(s.expand(w.subs(x,x-1)*w),x)
            ratio=-product.coeff_monomial(x**2)/w0**2
        else:
            ratio=None
        rows.append(dict(d=str(root),w=str(w),w0=str(w0),
                         local_zeta3_ratio=str(ratio),
                         target_ratio_match=ratio==3))
    return dict(r=r,c=c,characteristic_polynomial=str(s.factor(cp)),
                rational_seeds=rows)


if __name__=='__main__':
    rows=[classify(r) for r in range(11)]
    # Independent telescoping certificate for the quartic seed.
    w=lambda z:(z*(z+1))**2+s.Rational(14,5)*z*(z+1)+s.Rational(4,5)
    g=lambda z:(s.Rational(11,8)*z*(z+1)+s.Rational(273,80))/w(z)
    assert s.cancel(s.Rational(16,25)/(x**5*w(x-1)*w(x))
                    -1/x**5-s.Rational(11,4)/x**3-g(x)+g(x-1))==0
    out=dict(scope='exact restricted seed classification for degrees 0 through 20',rows=rows,
             quartic_telescoping_verified=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    for row in rows:
        print('degree',2*row['r'],'c',row['c'],
              [(v['d'],v['local_zeta3_ratio']) for v in row['rational_seeds']],flush=True)
