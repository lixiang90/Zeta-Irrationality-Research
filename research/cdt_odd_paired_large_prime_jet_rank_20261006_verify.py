"""NEW first-only finite checks of a paper-proved paired large-prime rank theorem.

No old/peer mathematical file is read, imported or executed.  The all-n rank,
minor filtration and all-prime main-rate theorem are proved in the NEW MD;
these finite checks do not establish an infinite auxiliary nonzero theorem.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise RuntimeError('First execution only; preserve existing output, do not rerun.')


def prime(p):
    return p > 1 and all(p % d for d in range(2, math.isqrt(p)+1))


def rank_kernel(rows, width, p):
    a = [[x % p for x in row] for row in rows]
    pivots = []
    for col in range(width):
        r = len(pivots)
        hit = next((j for j in range(r, len(a)) if a[j][col]), None)
        if hit is None:
            continue
        a[r], a[hit] = a[hit], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [x*inv % p for x in a[r]]
        for j in range(len(a)):
            if j == r or not a[j][col]:
                continue
            fac = a[j][col]
            a[j] = [(x-fac*y) % p for x,y in zip(a[j],a[r])]
        pivots.append(col)
    kernel = []
    for free in range(width):
        if free in pivots:
            continue
        v = [0]*width
        v[free] = 1
        for r,col in enumerate(pivots):
            v[col] = -a[r][free] % p
        assert all(sum(x*y for x,y in zip(row,v)) % p == 0 for row in rows)
        kernel.append(v)
    return len(pivots),kernel


def poly(v,t,mod):
    val,der = 0,0
    for c in reversed(v):
        der = (der*t+val) % mod
        val = (val*t+c) % mod
    return val,der


def rising(t,length,p):
    val = 1
    for k in range(length):
        val = val*(t+k) % p
    return val


def predicted_kernel(n,p):
    mid = (p-3*n)//2  # ceil((p-3n-1)/2), including parity exactly
    if p < 4*n:
        return max(4*n-p,mid)
    return max(p-4*n-1,mid)


def scaled_h1(length,p,mod):
    total = 0
    for k in range(1,length+1):
        total += pow(k//p,-1,mod) if k % p == 0 else p*pow(k,-1,mod)
    return total % mod


def small_h(length,power,mod):
    return sum(pow(k,-power,mod) for k in range(1,length+1)) % mod


cases = []
checks = 0
for n in range(1,11):
    width = 3*n
    factorial = [math.factorial(i) for i in range(8*n+1)]
    d = {z:factorial[6*n+z]//factorial[z-1] for z in range(1,2*n+1)}
    for p in range(3*n+1,6*n+1):
        if not prime(p):
            continue
        assert p*p > 8*n and width < p
        R0 = p-2*n if p < 4*n else 6*n+1-p
        actual_rows = []
        for z in range(1,n+1):
            zp = 2*n+1-z
            divisor = math.gcd(d[z],d[zp])
            pp,qq = d[z]//divisor,d[zp]//divisor
            actual_rows.append([(qq*pow(z,i,p)-pp*pow(zp,i,p)) % p for i in range(width)])
        cr,_ = rank_kernel(actual_rows,width,p)
        assert cr == n
        checks += 1
        evaluation = [[pow(-rho,i,p) for i in range(width)] for rho in range(R0)]
        full_rank,weak = rank_kernel(actual_rows+evaluation,width,p)
        expected = predicted_kernel(n,p)
        assert width-full_rank == len(weak) == expected
        checks += 1
        # Exact Wilson unit formulas of the actual primitive constraints.
        for z in range(1,2*n+1):
            unit,order = d[z],0
            while unit % p == 0:
                unit //= p
                order += 1
            if p > 4*n:
                assert order == 1 and unit % p == -rising(z,R0,p) % p
            else:
                H,J = 2*p-6*n,8*n+1-2*p
                bval = math.prod(z-k for k in range(H,2*n+1)) % p
                av = rising(z,R0,p)
                if z < H:
                    assert order == 1 and unit % p == -av*bval % p
                else:
                    bp = math.prod(z-k for k in range(H,2*n+1) if k != z) % p
                    assert order == 2 and unit % p == -2*av*bp % p
            checks += 1
        # All weak reductions vanish at the unit-tail nodes.  Arbitrary
        # integer-coefficient representatives suffice for the jet divisibility
        # check; they are not claimed as exact characteristic-zero paired lifts.
        mod = p*p
        values = [[poly(v,-j,mod) for j in range(6*n+1)] for v in weak]
        for row in values:
            assert all(row[p+rho][0] % p == 0 for rho in range(R0))
            checks += 1
        jet_checks = 0
        for source_a in (0,1):
            weights = []
            for j in range(6*n+1):
                count = j//p
                u4 = (-8*source_a*p*small_h(count,3,mod)-6*small_h(count,4,mod)) % mod
                cp = (5*scaled_h1(j,p,mod)-3*scaled_h1(2*n+j,p,mod)
                      -2*scaled_h1(6*n-j,p,mod)) % mod
                v5 = (cp*u4-24*source_a*p*small_h(count,4,mod)-24*small_h(count,5,mod)) % mod
                w = pow(math.comb(6*n,j),2,mod)*pow(math.comb(2*n+j,j),3,mod) % mod
                if w*u4 % mod or w*v5 % mod:
                    weights.append((j,w*u4 % mod,w*v5 % mod))
            for i in range(len(weak)):
                for l in range(i,len(weak)):
                    value = 0
                    for j,u4,v5 in weights:
                        vi,di = values[i][j]
                        vl,dl = values[l][j]
                        value += p*u4*(di*vl+vi*dl)+v5*vi*vl
                    assert value % mod == 0
                    jet_checks += 1
            for i in range(len(weak)):
                for degree in range(width):
                    value = sum(v5*values[i][j][0]*pow(-j,degree,p) for j,_,v5 in weights)
                    assert value % p == 0
                    jet_checks += 1
        checks += jet_checks
        cases.append({'n':n,'p':p,'actual_constraint_rank':cr,
                      'unit_tail_count':R0,'actual_weak_dimension':expected,
                      'negative_evaluation_rank':2*n-expected,
                      'unconditional_Gauss_lower_bound':-10*n+2*expected,
                      'finite_jet_checks':jet_checks})

old_A = Fraction(1085983123,24190320)
left_gain,right_gain = Fraction(1,6),Fraction(1,2)
new_A = old_A-left_gain-right_gain
assert new_A == Fraction(1069856243,24190320)
assert Fraction(44226,1000) <= new_A < Fraction(44227,1000)
checks += 2
record = {'status':'PASS','own_new_execution_count':1,
          'old_or_peer_execution_import_rerun_count':0,
          'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope':'Finite exact primitive-constraint ranks and low jet divisibility for 1<=n<=10, all primes3n<p<=6n, sources(a,b)=(0,1),(1,1), target terms vanish modulo p2. Arbitrary weak polynomial representatives are not exact characteristic-zero paired lifts.',
          'not_proved_by_code':['All-n theorem','Full Smith equality','Infinite nonzero evaluations','Matched margin'],
          'case_count':len(cases),'exact_checks':checks,'cases':cases,
          'old_safe_A':str(old_A),'paper_all_prime_gain':str(left_gain+right_gain),
          'new_safe_A':str(new_A),'new_safe_A_window':['44.226','44.227']}
OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:record[k] for k in ('status','case_count','exact_checks','paper_all_prime_gain','new_safe_A','new_safe_A_window')},ensure_ascii=False))
