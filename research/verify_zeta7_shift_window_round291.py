"""Rational certificates for the shift window, endpoint test and no-carry residues."""

from fractions import Fraction as Q
from functools import cache
from math import comb, factorial, gcd, lcm, log, prod

from verify_zeta7_contact_round288 import derivative_value, primes, rational_part, residue


def log_bounds_between_one_and_two(x):
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    terms = 16
    lo = sum(2*z**(2*j+1)/(2*j+1) for j in range(terms))
    return lo, lo+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))


@cache
def log_bounds(x):
    """Bound log(x) by exactly evaluated, positive rational series."""
    x = Q(x)
    if x < 1:
        lo,hi = log_bounds(1/x)
        return -hi,-lo
    exponent = 0
    while x >= 2:
        x /= 2
        exponent += 1
    lo,hi = log_bounds_between_one_and_two(x)
    l2,h2 = log_bounds_between_one_and_two(Q(2))
    return exponent*l2+lo,exponent*h2+hi


def uniform_prime_windows():
    margins = []
    for i in range(230):
        a,b = Q(i,1000),Q(i+1,1000)
        weight = Q(0)
        for u in range(1,129):
            uhalf = u+Q(1,2)
            for v in range(int(a*u), int(b*uhalf)+1):
                if a == 0 and v:
                    continue
                left = max(u,v/a) if a else Q(u)
                right = min(uhalf,(u+v+1)/(1+b))
                if left<right:
                    weight += Q(1,left)-Q(1,right)
        entropy_upper = (1+b)*log_bounds(1+b)[1]+b*log_bounds(1/b)[1]
        margins.append(7*weight-4*entropy_upper-log_bounds(4)[1])
    assert min(margins)>Q(1,50)
    print("230 rational windows, 128 prime-index bands; smallest certified margin",
          float(min(margins)), "in row",margins.index(min(margins)))


def endpoint_rate():
    def stationary(z):
        return 45*z**4-60*z**5+8*z-5

    bounds = []
    for left,right in [(Q(1,2),Q(3,5)),(Q(4,5),Q(9,10))]:
        sign = stationary(left)>0
        assert (stationary(right)>0) != sign
        for _ in range(54):
            middle = (left+right)/2
            if (stationary(middle)>0)==sign:
                left=middle
            else:
                right=middle
        values = [abs(5*x**4-1) for x in (left,right)]
        lo = left**5*(1-right)**3*min(values)/4
        hi = right**5*(1-left)**3*max(values)/4
        bounds.append((lo,hi))
    assert bounds[0][1]<bounds[1][0]
    lo,hi = bounds[1]
    cl = log_bounds(4)[0]-Q(4,3)*log_bounds(hi)[1]
    cu = log_bounds(4)[1]-Q(4,3)*log_bounds(lo)[0]
    assert Q(1109263630,10**8)<cl<=cu<Q(1109263631,10**8)
    print("balanced test C* enclosed in (11.09263630,11.09263631)")


def lucas_saving():
    intervals = [(Q(0),Q(1,12)),(Q(2,5),Q(5,12)),(Q(4,5),Q(5,6))]
    for j in range(120):
        x = Q(j,120)
        assert (sum((r*x)%1 for r in (3,4,5)) < 1) == any(a <= x < b for a,b in intervals)
    scale, cutoff = 10**16, 10000
    rounded_sum = count = 0
    for k in range(cutoff):
        for a,b in intervals:
            if k+b <= Q(1,12):
                continue
            rounded_sum += int(scale*(b-a)/((k+a)*(k+b)))
            count += 1
    length = sum(b-a for a,b in intervals)
    lo = (Q(rounded_sum,scale)+length/(cutoff+1))/3
    hi = (Q(rounded_sum+count,scale)+length/(cutoff-1))/3
    assert Q(106847591,10**9)<lo<=hi<Q(106847593,10**9)
    print("Lucas saving per n enclosed in (0.106847591,0.106847593)")


def fourth_coefficient(u,v):
    jet = [Q(1)]+[Q(0)]*4
    for a in range(1,u+1):
        local = [Q((-1)**j*comb(j+3,3),(v+a)**j) for j in range(5)]
        jet = [sum(jet[h]*local[j-h] for h in range(j+1)) for j in range(5)]
    return jet[4]


def p_order(x,p):
    assert x
    value = 0
    for h,sign in [(x.numerator,1),(x.denominator,-1)]:
        while h%p==0:
            h //= p
            value += sign
    return value


def arithmetic_examples():
    # Rebuild the jets from the product and A independently from partial fractions.
    jets,denominators = 0,0
    for n in (10,19,30,40,61):
        target = 30*(-1)**n*comb(2*n,n)
        for s in (0,n//5,n):
            t = s+1
            scale = Q(factorial(n),prod(range(t,t+n+1)))**4
            fs = [derivative_value(n,t+j,centered=True) for j in range(4)]
            phi = [(2*t+n+2*j)*Q(prod(range(t,t+j)),prod(range(t+n+1,t+n+1+j)))**4
                   for j in range(4)]
            a = rational_part(n,s)
            c00,c01,c11 = (fs[i]-fs[i+1] for i in range(3))
            det = c00*c11-c01*c01
            assert c00>0 and det>0
            roots = [-a/target,(-a+fs[0]**2/c00)/target,
                     (-a+(c11*fs[0]**2-2*c01*fs[0]*fs[1]+c00*fs[1]**2)/det)/target]
            d0,d1,d2 = (phi[i]-phi[i+1] for i in range(3))
            for p in primes(n):
                u,r = divmod(n,p)
                v,b = divmod(s,p)
                if p*p<=2*(n+s+6) or 2*r>=p or r+b+5>=p:
                    continue
                K = fourth_coefficient(u,v)
                for j in range(4):
                    assert residue(p**4*fs[j]/scale-K*phi[j],p)==0
                    jets+=1
                if residue(K,p)==0 or residue(rational_part(u,v),p)==0:
                    continue
                for candidate,minor in zip(roots,[1,d0,d0*d2-d1*d1]):
                    if residue(Q(minor),p):
                        assert p_order(candidate,p)==-7
                        denominators+=1
    assert jets and denominators
    print("local derivative congruences",jets,"valuations of fully reduced roots",denominators)


@cache
def top_numerator(h):
    from flint import fmpq

    assert h>0 and gcd(h,12)==1
    low,high=fmpq(h,3),fmpq(h,4)
    prefix=[fmpq(1)]
    term=fmpq(1)
    for a in range(1,h+1):
        term *= -(low+1-a)/(5*a)
        prefix.append(prefix[-1]+term)
    choose=fmpq(1)
    total=-high*prefix[h]
    for i in range(1,h+1):
        choose *= (high+1-i)/i
        total += (2*i-high)*choose**4*prefix[h-i]
    numerator,denominator=int(total.p),int(total.q)
    expected=2+8*h+4*(h-h.bit_count())
    assert numerator%2 and (denominator&-denominator).bit_length()-1==expected
    return numerator


def lost_layers(n, p):
    """Return the full local cancellation depth, using the four Laurent coefficients."""
    assert n % 3 == 0 and max(7, 2*n) < p < 4*n
    d, h, modulus = n//3, 4*n-p, p**8
    harmonic = [[0]*(n+1) for _ in range(4)]
    for u in range(1, n+1):
        inv = pow(u, -1, modulus)
        for j in range(1, 4):
            harmonic[j][u] = (harmonic[j][u-1]+inv**j) % modulus
    prefix = [1]
    term = 1
    for a in range(1, min(4*d, h)+1):
        term = -term*(4*d+1-a)*pow(5*a, -1, modulus) % modulus
        prefix.append((prefix[-1]+term) % modulus)

    total = 0
    for i in range(min(n, h)+1):
        coeff = [1]
        for j in range(1, 4):
            coeff.append(4*sum((harmonic[l][n-i]+(-1)**l*harmonic[l][i])*coeff[j-l]
                               for l in range(1, j+1))*pow(j, -1, modulus) % modulus)
        local = sum(comb(7-j, 4)*p**j*((2*i-n)*coeff[j]+(2*coeff[j-1] if j else 0))
                    for j in range(4))
        total += prefix[min(4*d, h-i)]*pow(comb(n, i), 4, modulus)*local
    return sum(total % p**j == 0 for j in range(1, 9))


def other_odd_weights():
    from verify_zeta7_contact_round288 import harmonic, poles

    checks = 0
    for n in (6, 12, 18):
        d = n//3
        for w in (5, 9, 11):
            order = w-3
            target = (w-1)*(w-2)*(-1)**n*comb(2*n, n)
            constants = [-sum(comb(j+order-1, order)*a*harmonic(b+c, j+order)
                              for c, row in enumerate(poles(n)) for j, a in enumerate(row, 1))
                         for b in range(5*d, 9*d+1)]
            r = -sum((-5)**j*comb(4*d, j)*value for j, value in enumerate(constants))/(target*4**(4*d))
            for p in primes(4*n):
                if max(w,7,2*n) < p < 4*n:
                    assert (p_order(r,p) == -(w+1)) == (top_numerator(4*n-p) % p != 0)
                    checks += 1
    print("top valuation checks at weights 5, 9, 11", checks)


def top_band(max_d=120):
    from verify_zeta7_polynomial_content_round289 import primes_upto

    primes=primes_upto(12*max_d)
    count=0
    losses=[]
    depths=[]
    shares=[]
    for d in range(1,max_d+1):
        weight,bad_weight=0,0
        for p in primes:
            if max(7,6*d)<p<12*d:
                count+=1
                lower=(p**256).bit_length()-1
                weight+=lower
                if top_numerator(12*d-p)%p==0:
                    losses.append((3*d,p))
                    depths.append(lost_layers(3*d,p))
                    bad_weight+=lower+1
        if weight:
            shares.append((Q(bad_weight,weight),3*d))
    max_share,max_n=max(shares)
    if max_d == 120:
        assert count == 6603 and len(losses) == 14 and max_n == 6 and max_share < Q(25673,100000)
        assert depths == [1]*14
    print("top band n=3,6,...,",3*max_d,"pairs",count,"eighth-layer losses",len(losses),
          "first losses",losses[:8],"depths",depths,"max rational share upper",float(max_share),"at",max_n)


def balanced_denominators():
    from flint import fmpq, fmpq_mat
    from verify_zeta7_polynomial_content_round289 import exact_moments, primes_upto

    orders = [3,6,9,12,15,18,21,24,27,30,36]
    constants,targets = exact_moments(max(orders))
    terms = 26*max(orders)+30
    complete = [fmpq(1)]+[fmpq(0)]*6
    eta_lower = fmpq(0)
    for j in range(1,terms+1):
        for k in range(1,7):
            complete[k] += complete[k-1]/j
        eta_lower += complete[6]/(j*2**j)
    zeta_lo = fmpq(64,63)*eta_lower
    zeta_hi = zeta_lo+fmpq(64,63*2**terms)
    print("n  bits(q)  bits(q above 4n)  log(q)/n  log(outside)/n  -log(error)/n  bits(q_trial)")
    for n in orders:
        value,target = n*constants[n-1],n*targets[n-1]
        diffs = []
        for t in range(n+1,3*n+1):
            log_coeff = [0]+[4*(-1)**j*sum(fmpq(1,a**j) for a in range(t,t+n+1))
                              for j in range(1,5)]
            coeff = [fmpq(1)]
            for j in range(1,5):
                coeff.append(sum(log_coeff[i]*coeff[j-i] for i in range(1,j+1))/j)
            d = fmpq(1,t*comb(t+n,n))**4*((2*t+n)*coeff[4]+2*coeff[3])
            if n==3:
                check = derivative_value(n,t,centered=True)
                assert d==fmpq(check.numerator,check.denominator)
            diffs.append(d)
        matrix = fmpq_mat(n,n,[diffs[i+j]-diffs[i+j+1] for i in range(n) for j in range(n)])
        vector = fmpq_mat(n,1,diffs[:n])
        correction = (vector.transpose()*matrix.solve(vector))[0,0]
        root = (correction-value)/target
        scale = lcm(*(int(x.q) for x in [value,*diffs]))
        h = int((scale*correction).q)
        q = int(root.q)
        assert q%h==0
        outside,aux = q,h
        for p in primes_upto(4*n):
            while outside%p==0:
                outside//=p
            while aux%p==0:
                aux//=p
        assert aux==outside
        assert (root-zeta_hi)*target<0 and (root-zeta_lo)*target<0
        err_lo,err_hi = sorted([abs(root-zeta_lo),abs(root-zeta_hi)])
        assert err_hi<err_lo*(1+fmpq(1,10**14)) and outside*err_lo>1
        d = n//3
        moments = [value]
        for difference in diffs:
            moments.append(moments[-1]-difference)
        trial = -sum((-5)**j*comb(4*d,j)*moments[2*d+j] for j in range(4*d+1))/(target*4**(4*d))
        qtrial = int(trial.q)
        safe = abs(int(target))*4**(4*d)*lcm(*range(1,4*n+1))**8
        for p in primes_upto(4*n):
            if p>5 and p*p>2*(4*n+1) and (3*d)%p+(4*d)%p+(5*d)%p<p:
                safe//=p
            if max(7,2*n)<p<4*n:
                assert (qtrial%p**8==0)==(top_numerator(4*n-p)%p!=0)
                assert lost_layers(n,p) == 8-p_order(Q(qtrial),p)
        assert safe%qtrial==0 and (root-trial)*target>=0
        assert qtrial*min(abs(trial-zeta_hi),abs(trial-zeta_lo))>1
        print(n,q.bit_length(),outside.bit_length(),f"{log(q)/n:.6f}",f"{log(outside)/n:.6f}",
              f"{-log(float(err_lo))/n:.6f}",qtrial.bit_length())


if __name__ == "__main__":
    uniform_prime_windows()
    endpoint_rate()
    lucas_saving()
    arithmetic_examples()
    balanced_denominators()
    top_band()
    other_odd_weights()
