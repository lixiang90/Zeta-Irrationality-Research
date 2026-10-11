"""NEW first-only exact certificate. Never reads or executes other producers."""
from pathlib import Path
from fractions import Fraction
from math import comb, gcd
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise SystemExit('Refuse rerun: first-only output already exists')


def binomial(z, i):
    return comb(z, i) if z >= 0 else (-1) ** i * comb(i-z-1, i)


def rank_mod(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    row = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inverse = pow(a[row][col], -1, p)
        a[row] = [v * inverse % p for v in a[row]]
        for i in range(row+1, len(a)):
            if a[i][col]:
                c = a[i][col]
                a[i] = [(x-c*y) % p for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def profiles(n, p):
    result = []
    for rho in range(p):
        q = (6*n-rho)//p
        w = 2*(6*n//p)-2*q + 3*((2*n+rho)//p)-3*(2*n//p)
        assert w in (0, 2, 3, 5)
        result.append((q, w))
    return result


def weighted_dp(n, p, types):
    Q, R = divmod(3*n, p)
    d = 2*n
    table = {(0, 0): (0, ())}
    for q, w in types:
        nxt = {}
        for (used, credits), (cost, allocation) in table.items():
            for r in range(min(2*q+2, d-used)+1):
                base = w*r + 4*max(0, r-2*q) + 2*max(0, r-Q)
                choices = (0, 1) if r > Q and credits < R else (0,)
                for credit in choices:
                    key = (used+r, credits+credit)
                    value = (cost+base-2*credit, allocation+(r,))
                    if key not in nxt or value[0] < nxt[key][0]:
                        nxt[key] = value
        table = nxt
    answer = min(value for (used, _), value in table.items() if used == d)
    allocation = answer[1]
    actual = sum(w*r+4*max(0,r-2*q)+2*max(0,r-Q)
                 for (q,w),r in zip(types,allocation))
    actual -= 2*min(R,sum(r>Q for r in allocation))
    assert actual == answer[0]
    return answer


def paired_newton(n, p):
    d, ambient = 2*n, 3*n
    columns = []
    for m in range(1,n+1):
        mirror = 2*n+1-m
        bm, bj = comb(6*n+m, m-1), comb(6*n+mirror, mirror-1)
        g = gcd(bm,bj)
        pm, qm = bm//g, bj//g
        vector = []
        for i in range(ambient):
            cm = (-1)**(i-m+1)*comb(i,m-1) if m-1<=i<2*n else 0
            cj = (-1)**(i-mirror+1)*comb(i,mirror-1) if mirror-1<=i<2*n else 0
            vector.append((pm*cm+qm*cj)%p)
        columns.append(vector)
    for i in range(2*n,3*n):
        columns.append([int(j==i) for j in range(ambient)])
    assert len(columns)==d
    assert rank_mod(list(map(list,zip(*columns))),p)==d
    return columns


def actual_rows(n, p, allocation, types):
    columns = paired_newton(n,p)
    rows, labels = [], []
    for rho, ((q,w),count) in enumerate(zip(types,allocation)):
        selected = []
        # Tail rows have smaller actual node-block weight than head.
        for ell in list(range(1,q+1))+[0]:
            for kind in (0,1):
                if len(selected)<count:
                    selected.append((rho+ell*p,kind))
        assert len(selected)==count
        for j,kind in selected:
            z=-j
            values=[binomial(z-1,i)%p for i in range(3*n)]
            if kind:
                deriv=[]
                for i in range(3*n):
                    v=0
                    for ell in range(1,i//p+1):
                        v += (-1)**(ell-1)*pow(ell,-1,p)*values[i-ell*p]
                    deriv.append(v%p)
                values=deriv
            rows.append([sum(c*v for c,v in zip(column,values))%p
                         for column in columns])
            labels.append([j,kind])
    Q,R=divmod(3*n,p)
    cap=sum(min(r,Q) for r in allocation)+min(R,sum(r>Q for r in allocation))
    observed=rank_mod(rows,p)
    assert observed<=cap
    return {'observed_rank':observed,'paper_rank_upper_bound':cap,
            'selected_actual_jet_rows':labels,
            'determinant_divisibility_at_least':2*n-cap}


checks=0
cases=[]
for n,p in [(23,17),(31,23),(55,41)]:
    assert p>5 and p*p>8*n and Fraction(31,42)<Fraction(p,n)<Fraction(3,4)
    assert all(p%d for d in range(2,int(p**0.5)+1))
    types=profiles(n,p)
    Q,R=divmod(3*n,p)
    assert Q==4
    counts={w:sum(v==w for _,v in types) for w in (0,2,3,5)}
    assert counts=={0:6*n-8*p+1,2:11*p-8*n-1,3:0,5:2*n-2*p}
    for q,w in types:
        assert q==(8 if w==0 else 7)
        for r in range(2*q+3):
            local=w*r+4*max(0,r-2*q)+2*max(0,r-Q)
            bound=4*r-(40 if w==0 else 8 if w==2 else 0)
            assert local>=bound
            checks+=1
    omega,allocation=weighted_dp(n,p,types)
    dual=240*p-174*n-32
    assert omega>=dual
    unittail=max(0,2*n-Q*counts[0]-min(R,counts[0]))*2
    rank=actual_rows(n,p,allocation,types)
    cases.append({'n':n,'p':p,'types':counts,'Q':Q,'R':R,
                  'weighted_optimum':omega,'explicit_dual_lower_bound':dual,
                  'unit_tail_DND_credit':unittail,
                  'weighted_minus_DND_credit':omega-unittail,
                  'allocation':list(allocation),'actual_paired_rank_check':rank})
    checks+=8

left,right=Fraction(31,42),Fraction(3,4)
gain=84*(right*right-left*left)-124*(right-left)
assert gain==Fraction(1,84)
for x in (left,(left+right)/2,right):
    old=38*x-36
    one=72*x-60
    weighted=240*x-184
    assert one>old and weighted>=one
    checks+=2
assert cases[-1]['weighted_minus_DND_credit']>0
result={'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'first_only':True,'runs':{'new_self':1,'old_or_peer':0,'imports_old_or_peer':0},
        'scope':'Three specified actual paired jet minors and exact weighted-profile DP; no actual Gram determinant, no infinite nonzero theorem.',
        'cases':cases,'exact_assertions':checks,
        'paid_interval':[str(left),str(right)],'extra_paid_gain':str(gain),
        'no_new_irrationality_or_lean_claim':True}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','cases':len(cases),'checks':checks,
                  'gain':str(gain),'last_extra_credit':cases[-1]['weighted_minus_DND_credit']},ensure_ascii=False))
