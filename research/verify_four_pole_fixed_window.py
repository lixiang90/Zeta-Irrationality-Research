"""Independent Fraction product jets and exact rational zeta enclosures.

Does not import the discovery code or use Arb for numerical verification.
"""
import json
import math
import sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from verify_pure_odd_derivatives import harmonic, zeta_interval, displayed_interval

sys.set_int_max_str_digits(0)


def mul(a,b):
    return [sum((a[j]*b[i-j] for j in range(i+1)),F(0)) for i in range(4)]


def factor(base,power):
    # Generalized binomial coefficient: also works at negative integer power.
    out=[F(1)]
    for i in range(1,4):out.append(out[-1]*F(power-i+1,i*base))
    return out


@lru_cache(None)
def local(n,h,d):
    result=[]
    norm=F(math.factorial(n)**4,math.factorial(h)**(2*d))
    for k in range(n+1):
        b=norm
        jet=[F(1),F(0),F(0),F(0)]
        for a in range(n+1):
            if a!=k:
                b/=F(a-k)**4
                jet=mul(jet,factor(a-k,-4))
        for a in range(1,h+1):
            for base in (-k-a,n-k+a):
                b*=F(base)**d
                jet=mul(jet,factor(base,d))
        seed0=[F(0)]+[b*jet[4-j] for j in range(1,5)]
        z=n-2*k
        jet1=mul(jet,[F(z*z),F(4*z),F(4),F(0)])
        seed1=[F(0)]+[b*jet1[4-j] for j in range(1,5)]
        result.append([seed0,seed1])
    D=math.lcm(*range(1,n+1))
    for k in range(n+1):
        for col in (0,1):
            for j in range(1,5):
                assert result[k][col][j]==(-1)**j*result[n-k][col][j]
                assert (result[k][col][j]*D**(4-j)).denominator==1
    return result


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'four_pole_fixed_window.json').read_text())['rows']
    bounds={s:zeta_interval(s) for s in (5,7,9,11)}
    positive=0;baseline=0
    for idx,row in enumerate(rows):
        n,h,d,s,K=[row[x] for x in ('n','h','d','s','offset')]
        c=local(n,h,d)
        C=[[sum((c[k][col][j] for k in range(n+1)),F(0)) for j in range(5)] for col in range(2)]
        assert all(C[col][j]==0 for col in (0,1) for j in (1,3))
        assert list(map(F,row['C2']))==[C[0][2],C[1][2]]
        assert list(map(F,row['C4']))==[C[0][4],C[1][4]]
        rho=C[1][2]/C[0][2];assert rho==F(row['rho'])
        det=C[0][2]*C[1][4]-C[1][2]*C[0][4]
        assert det==F(row['determinant'])!=0
        if h==0:
            assert det==(-1)**(n+1)*4*math.comb(4*n,2*n)*math.comb(2*n,n)
            assert rho<n*n and C[0][2]>0
            baseline+=1
        cc=[[c[k][1][j]-rho*c[k][0][j] for j in range(5)] for k in range(n+1)]
        assert all(sum(cc[k][j] for k in range(n+1))==0 for j in (1,2,3))
        r=s-4
        a=-sum((math.comb(j+r-1,r)*cc[k][j]*harmonic(k+K,j+r) for k in range(n+1) for j in range(1,5)),F(0))
        b=math.comb(s-1,3)*sum(cc[k][4] for k in range(n+1))
        assert a==F(row['constant']) and b==F(row['zeta_coefficient'])
        den=math.lcm(a.denominator,b.denominator)
        content=math.gcd(int(a*den),int(b*den));scale=F(den,content)
        pair=[int(a*scale),int(b*scale)]
        assert pair==list(map(int,row['primitive_pair'])) and scale==F(row['primitive_scale'])
        D=math.lcm(*range(1,n+K+1));clear=rho.denominator*D**s
        assert clear==int(row['clearing_bound']) and (clear*a).denominator==(clear*b).denominator==1
        zlo,zhi=bounds[s]
        lo,hi=sorted((a+b*zlo,a+b*zhi))
        assert lo>0 or hi<0
        assert (lo>0)==row['positive']
        positive+=int(lo>0)
        for key,lower,upper in [('raw_value',lo,hi),('primitive_value',scale*lo,scale*hi)]:
            shown=displayed_interval(row[key]);assert shown[0]<=lower<=upper<=shown[1],(idx,key)
        assert scale*lo>1 or scale*hi < -1
        if h==0:
            assert lo>0
            if K==0:assert lo>=F(4*math.comb(r+2,2),(n+1)**3)
        if (idx+1)%40==0:print('verified',idx+1,flush=True)
    minima={}
    for s in (5,7,9,11):
        candidates=[x for x in rows if x['h']==0 and x['n']==128 and x['s']==s]
        intervals=[displayed_interval(x['primitive_value']) for x in candidates]
        winner=min(range(len(candidates)),key=lambda i:intervals[i][1])
        assert all(intervals[winner][1]<intervals[i][0] for i in range(len(candidates)) if i!=winner)
        minima[s]=candidates[winner]['offset']
    result=dict(status='passed',records=len(rows),distinct_kernels=local.cache_info().currsize,
                positive=positive,negative=len(rows)-positive,primitive_abs_gt_one=len(rows),
                baseline_determinant_checks=baseline,certified_best_cutoff_at_n128=minima,
                method='Independent truncated products over Fraction; exact rational Euler--Maclaurin bounds M=512,J=512; no Arb or discovery coefficient code.')
    (folder/'verify_four_pole_fixed_window.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result,flush=True)


if __name__=='__main__':main()
