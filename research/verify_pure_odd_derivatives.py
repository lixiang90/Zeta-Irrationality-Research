"""Independent rational pole jets and rational Euler--Maclaurin enclosures."""
import json
import math
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import sympy as S

sys.set_int_max_str_digits(0)


@lru_cache(None)
def harmonic(n,s):return sum((F(1,k**s) for k in range(1,n+1)),F(0))


@lru_cache(None)
def local_coefficients(n,h,d):
    norm=F(math.factorial(n)**2,math.factorial(h)**d);A=[];B=[]
    for j in range(n+1):
        b=norm*F(math.prod((-j-a)**d for a in range(1,h+1)),
                 math.prod((k-j)**2 for k in range(n+1) if k!=j))
        log_der=sum((F(d,-j-a) for a in range(1,h+1)),F(0))-sum((F(2,k-j) for k in range(n+1) if k!=j),F(0))
        A.append(b*log_der);B.append(b)
    assert sum(A)==0 and all(x.denominator==1 and x>0 for x in B)
    return A,B


def zeta_interval(s,M=512,J=512):
    """EM truncation: the remainder has the sign and <= magnitude of next term.

    For s>1 this follows from the partial fractions of coth in the positive
    Laplace integral for the Hurwitz zeta tail.
    """
    value=sum((F(1,k**s) for k in range(1,M)),F(0))+F(1,(s-1)*M**(s-1))+F(1,2*M**s)
    terms=[]
    for j in range(1,J+2):
        b=S.bernoulli(2*j)
        term=F(int(b.p),int(b.q))*F(math.prod(range(s,s+2*j-1)),math.factorial(2*j)*M**(s+2*j-1))
        if j<=J:value+=term
        else:next_term=term
    return min(value,value+next_term),max(value,value+next_term)


def displayed_interval(text):
    text=text.strip('[]')
    if '+/-' not in text:return F(text),F(text)
    a,b=text.split('+/-');a,b=F(a.strip()),F(b.strip());return a-b,a+b


def head_taylor(n,r):
    """Direct multiplication of local factors, independent of logarithmic jets."""
    cap=r-2
    def mul(a,b):
        c=[F(0)]*min(len(a)+len(b)-1,cap+1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if i+j<len(c):c[i+j]+=x*y
        return c
    P=[F(1)]
    for k in range(1,n):P=mul(P,[F(1),F(-2,k),F(1,k*k)])
    for k in range(1,n+2):P=mul(P,[F((-1)**j*(j+1),k**j) for j in range(cap+1)])
    return -P[cap]/(n*n*(n+1)**2)


def main():
    folder=Path(__file__).parent
    files=['pure_odd_derivative_probe','pure_odd_flat_head','pure_odd_tail_subtraction','pure_odd_head_leakage','pure_odd_cutoff_scan']
    all_rows=[(name,row) for name in files for row in json.loads((folder/(name+'.json')).read_text())['rows']]
    intervals={s:zeta_interval(s) for s in (3,5,7,9,11)}
    signs={};counts={};head_count=0
    for name,row in all_rows:
        n,h,s=row['n'],row['h'],row['s'];d=row.get('zero_multiplicity',2);offset=row.get('summation_offset',0)
        A,B=local_coefficients(n,h,d);assert list(map(F,row['A']))==A and list(map(F,row['B']))==B
        a=-sum((A[j]*harmonic(j+offset,s-1)+(s-1)*B[j]*harmonic(j+offset,s) for j in range(n+1)),F(0))
        b=(s-1)*sum(B);assert a==F(row['constant']) and b==F(row['zeta_coefficient'])
        denominator=math.lcm(a.denominator,b.denominator);content=math.gcd(int(a*denominator),int(b*denominator))
        pair=[int(a*denominator)//content,int(b*denominator)//content]
        assert pair==list(map(int,row['primitive_pair'])) and F(denominator,content)==F(row['primitive_scale'])
        assert denominator==int(row['clearing_denominator']) and content==int(row['output_content'])
        D=math.lcm(*range(1,n+1))
        assert all((D*x).denominator==1 for x in A)
        if offset==0:clear=D**s
        else:
            assert 0<offset<=n and h==n and d==2
            D2=math.lcm(*range(1,n+offset+1));clear=D**s*(D2//D)**(s-2)
        assert (a*clear).denominator==(b*clear).denominator==1
        zl,zu=intervals[s];lower=a+b*zl;upper=a+b*zu
        assert lower>0 or upper<0
        assert (lower>0)==row['positive']
        shown=displayed_interval(row['raw_value']);assert shown[0]<=lower<=upper<=shown[1]
        scale=F(row['primitive_scale']);shown=displayed_interval(row['primitive_value'])
        assert shown[0]<=lower*scale<=upper*scale<=shown[1]
        if 'first_node' in row:
            first=head_taylor(n,s-2);assert first==F(row['first_node'])>0
            shown=displayed_interval(row['raw_to_first_ratio']);assert shown[0]<=lower/first<=upper/first<=shown[1];head_count+=1
        counts[name]=counts.get(name,0)+1;key=(name,'positive' if lower>0 else 'negative');signs[str(key)]=signs.get(str(key),0)+1
    grid=json.loads((folder/'pure_odd_cutoff_scan.json').read_text())
    for best in grid['best']:
        candidates=[r for r in grid['rows'] if r['n']==best['n'] and r['s']==best['s']]
        winner=next(r for r in candidates if r['summation_offset']==best['offset'])
        def abs_bounds(r):
            a,b=displayed_interval(r['primitive_value'])
            return (a,b) if a>0 else (-b,-a)
        assert all(abs_bounds(winner)[1]<abs_bounds(r)[0] for r in candidates if r is not winner)
    result=dict(status='passed',forms=len(all_rows),counts=counts,sign_counts=signs,
                direct_head_Taylor_checks=head_count,zeta_bound='Exact rational Euler--Maclaurin, M=512, J=512; no Arb zeta call.',
                checked='Independent local pole jets, pure output coefficients, primitive normalization, denominator bounds, nonzero finite intervals and first-node jets.')
    (folder/'verify_pure_odd_derivatives.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(result,flush=True)


if __name__=='__main__':main()
