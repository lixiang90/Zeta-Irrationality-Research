"""Exact certificates supporting the seed-space equivalence proved in the note."""
import json
from pathlib import Path
import sympy as s

x=s.symbols('x')
root=Path(__file__).parent
data=json.loads((root/'zeta35_cf_seed_space.json').read_text(encoding='utf-8'))
rows=[]
for group in data['rows']:
    for row in group['rational_seeds']:
        w=s.sympify(row['w'],locals={'x':x})
        w0=w.subs(x,0)
        assert s.expand(w.subs(x,-x-1)-w)==0
        if s.degree(w,x)==0:
            u=s.S.Zero
        else:
            assert s.gcd(w,w.subs(x,x-1))==1
            u=s.rem(w0**2*s.invert(x**5*w.subs(x,x-1),w,x),w,x)
        G=s.cancel(u/w)
        assert s.cancel(G-G.subs(x,-x-1))==0
        ratio=s.sympify(row['local_zeta3_ratio'])
        kernel=w0**2/(x**5*w.subs(x,x-1)*w)
        assert s.cancel(kernel-1/x**5-ratio/x**3-G+G.subs(x,x-1))==0
        A,rem=s.div(x**5*w.subs(x,x-1)+(x+1)**5*w.subs(x,x+1),w,x)
        assert rem==0
        assert s.expand(A-x**5-(x+1)**5-group['c']*(x**3+(x+1)**3)
                        -s.sympify(row['d'])*(2*x+1))==0
        rows.append(dict(degree=2*group['r'],c=group['c'],d=row['d'],
                         w=str(w),U=str(u),zeta3_ratio=str(ratio),
                         correction_at_zero=str(G.subs(x,0))))
out=dict(scope='exact certificates for all rational seeds found through degree 20',rows=rows,
         target_preserving_normalized_seed='1+3*x*(x+1)',
         classification_scope='degree <=20 only, not an all-degree exclusion')
(root/'zeta35_seed_equivalence.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
