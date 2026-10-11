"""Fixed fourth-order poles; exact elimination shared by all odd targets.

All numerical conclusions are finite experiments. See the companion report.
"""
import json
import math
import sys
from pathlib import Path
from functools import lru_cache
from flint import fmpq as Q, arb, ctx
from critical_lift_probe import harmonic_table, primitive

sys.set_int_max_str_digits(0)


@lru_cache(None)
def coefficients(n, h, d):
    assert d % 2 == 0 and d*h <= 2*n and (d or h == 0)
    H = harmonic_table(n+h, 3)
    local = []
    for k in range(n+1):
        b = Q(math.comb(n,k)**4 * (math.comb(k+h,h)*math.comb(n-k+h,h))**d)
        ell = [Q(0)]
        for m in range(1,4):
            ell.append(Q(4*(-1)**m,m)*(H[n-k][m]+(-1)**m*H[k][m])
                       +Q(d*(-1)**(m-1),m)*((-1)**m*(H[k+h][m]-H[k][m])
                                                    +H[n-k+h][m]-H[n-k][m]))
        e = [Q(1)]
        for i in range(1,4):
            e.append(sum((m*ell[m]*e[i-m] for m in range(1,i+1)),Q(0))/i)
        z = n-2*k
        p = [z*z,4*z,4]
        c0 = [Q(0)]+[b*e[4-j] for j in range(1,5)]
        c1 = [Q(0)]+[b*sum((p[m]*e[4-j-m] for m in range(min(2,4-j)+1)),Q(0)) for j in range(1,5)]
        local.append([c0,c1])
    C = [[sum((local[k][col][j] for k in range(n+1)),Q(0)) for j in range(5)] for col in range(2)]
    assert all(C[col][j] == 0 for col in range(2) for j in (1,3))
    assert C[0][2]
    rho = C[1][2]/C[0][2]
    eliminated = [[local[k][1][j]-rho*local[k][0][j] for j in range(5)] for k in range(n+1)]
    return local,C,rho,eliminated


def row(n,h,d,s,offset=0):
    _,C,rho,c = coefficients(n,h,d)
    r = s-4
    H = harmonic_table(n+offset,s)
    a = -sum((Q(math.comb(j+r-1,r))*c[k][j]*H[k+offset][j+r]
              for k in range(n+1) for j in range(1,5)),Q(0))
    b = Q(math.comb(s-1,3))*(C[1][4]-rho*C[0][4])
    assert b
    pair,scale = primitive([a,b])
    D = math.lcm(*range(1,n+offset+1))
    assert h <= n
    clear = int(rho.denominator)*D**s
    assert (a*clear).denominator == (b*clear).denominator == 1
    bits = 2*max(abs(x).bit_length() for x in pair)+768
    with ctx.workprec(bits):
        value = arb(pair[0])+arb(pair[1])*arb(s).zeta()
        assert not value.contains(0)
        raw = value/arb(scale)
        return dict(n=n,h=h,d=d,s=s,offset=offset,rho=str(rho),
                    C2=list(map(str,[C[0][2],C[1][2]])),
                    C4=list(map(str,[C[0][4],C[1][4]])),
                    determinant=str(C[0][2]*C[1][4]-C[1][2]*C[0][4]),
                    constant=str(a),zeta_coefficient=str(b),primitive_pair=list(map(str,pair)),
                    primitive_scale=str(scale),clearing_bound=str(clear),
                    raw_value=raw.str(30),primitive_value=value.str(30),
                    positive=bool(value>0),primitive_abs_gt_one=bool(abs(value)>1),
                    log_raw_per_n=(abs(raw).log()/n).str(20),
                    log_scale_per_n=(arb(scale).log()/n).str(20),
                    log_primitive_per_n=(abs(value).log()/n).str(20),
                    tail_kernel_positive=bool(rho<(n+2*h+2)**2),
                    flat_head=(d>=s-3 or h==0))


def main():
    rows=[]
    # The exact same kernel is used across s in each of these groups.
    for n in (4,8,16,32,64,128):
        for s in (5,7,9,11):rows.append(row(n,0,0,s))
    for h in (2,4,8,16,32):
        for s in (5,7,9,11):rows.append(row(h,h,2,s))
    for s in (5,7,9,11):
        d=s-3
        for h in (2,4,8,16,32):
            for extra in (0,h//2,h):
                n=d*h//2+extra
                rows.append(row(n,h,d,s))
    # A translated baseline is completely monotone and avoids all finite head
    # derivatives; its larger harmonic denominators are explicitly charged.
    for n in (32,64,128):
        for s in (5,7,9,11):
            for offset in (n//4,n//2,n,2*n):rows.append(row(n,0,0,s,offset))
    result=dict(description='Monic kernel ((2t+n)^2-rho) F_{n,h,d}; exact final primitive pair.',rows=rows)
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('records',len(rows),'positive',sum(x['positive'] for x in rows),
          'abs_gt_one',sum(x['primitive_abs_gt_one'] for x in rows),flush=True)
    for x in rows:
        if (x['h']==0 and x['n']==128) or (x['h']==32 and x['d']==x['s']-3 and x['n']==x['d']*16):
            print({k:x[k] for k in ('n','h','d','s','log_raw_per_n','log_scale_per_n','log_primitive_per_n','positive')})


if __name__=='__main__':main()
