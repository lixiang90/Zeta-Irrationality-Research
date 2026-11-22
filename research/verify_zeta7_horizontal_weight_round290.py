"""Check the horizontal Fermat-quotient identity and the edge of the pure-Q test."""

from argparse import ArgumentParser
from collections import defaultdict
from math import factorial, gcd, lcm, log, prod
from time import perf_counter

from flint import fmpz_mat, nmod_mat

from verify_zeta7_polynomial_content_round289 import (
    exact_moments, modular_data, normal_indices, primes_upto,
)


def fermat_difference(p, size):
    """Toeplitz coefficients Δ²((k^p-k)/p) for 0 <= k < size."""
    modulus = p*p
    g = [(pow(k, p, modulus)-k)//p % p for k in range(size+1)]
    return [0] + [(g[k+1]+g[k-1]-2*g[k]) % p for k in range(1,size)]


def complement_check(p, m):
    h = (p+1)//2-m
    size = 2*m-2
    _, moments = modular_data(p, 2*h-1)
    hankel = nmod_mat(h,h,[moments[i+j] for i in range(h) for j in range(h)],p)
    difference = fermat_difference(p, size)
    def entry(k):
        return difference[k] if k>=0 else -difference[-k]
    toeplitz = nmod_mat(size,size,[entry(i-j) for i in range(size)
                                  for j in range(size)],p)
    small_kernel = h-hankel.rank()
    assert 2*small_kernel == size-toeplitz.rank()
    return small_kernel


def shared_leading_filter(m, primes):
    """One integer gcd for the leading singularities at every prime in I_m."""
    modulus = prod(primes)
    exponent = lcm(*(p-1 for p in primes))
    assert gcd(exponent,modulus)==1
    size = 2*m-2
    values = [((pow(k,exponent+1,modulus**2)-k)//modulus) % modulus
              for k in range(size+1)]
    difference = [0]+[(values[k+1]+values[k-1]-2*values[k]) % modulus
                      for k in range(1,size)]
    entries = [difference[i-j] if i>=j else -difference[j-i]
               for i in range(size) for j in range(size)]
    # The squarefree modulus gives the same gcd for a Pfaffian and its square.
    return gcd(modulus,int(fmpz_mat(size,size,entries).det()))


def coefficients_from_values(values, modulus):
    """Interpolate in the falling-factorial basis; all j! are units here."""
    coefficients = [0]*len(values)
    basis = [1]
    for j in range(len(coefficients)):
        weight = values[0]*pow(factorial(j),-1,modulus) % modulus
        for i,a in enumerate(basis):
            coefficients[i] = (coefficients[i]+weight*a) % modulus
        values = [(y-x) % modulus for x,y in zip(values,values[1:])]
        basis = [(-j*a+b) % modulus for a,b in zip(basis+[0],[0]+basis)]
    return coefficients


def prefix_certificate(m):
    from verify_zeta7_outer_symbol_round289 import pole_moments, target_moments
    primes = [p for p in primes_upto(4*m-2) if p>max(13,2*m)]
    modulus = prod(primes)
    small = lcm(*range(1,2*m+1))
    big = small*lcm(*range(1,4*m+1))**8
    a,b = exact_moments(2*m-1)
    def clear_moment(x,scale):
        value = scale*x
        assert value.q==1
        return int(value.p) % modulus
    a = [clear_moment(x,big) for x in a]
    b = [clear_moment(x,small) for x in b]
    values = []
    for y in range(m+1):
        moments = [(x+y*t) % modulus for x,t in zip(a,b)]
        values.append(int(fmpz_mat(m,m,[moments[i+j] for i in range(m)
                                        for j in range(m)]).det()) % modulus)
    coefficients = coefficients_from_values(values,modulus)
    content = modulus
    prefix = []
    for coefficient in coefficients:
        content = gcd(content,coefficient)
        prefix.append(content)
    first_factor = shared_leading_filter(m,primes)
    for p in primes:
        center = (p+1)//2
        h = center-m
        e = m-h
        target = target_moments(p)
        pole = [0]*(center-1)+pole_moments(p,e)
        values = []
        for y in range(m+1):
            moments = [(x+y*t) % p for x,t in zip(pole,target)]
            values.append(int(nmod_mat(m,m,[moments[i+j] for i in range(m)
                                            for j in range(m)],p).det()))
        local = coefficients_from_values(values,p)
        v = big//p**8
        assert all(coefficients[j] % p == (local[j]*pow(v,m-j,p)*pow(small,j,p)) % p
                   for j in range(m+1))
        order = next((j for j,c in enumerate(local) if c), m)
        assert (first_factor % p==0) == (local[h]==0)
        assert all((prefix[j] % p==0)==(j<order) for j in range(m))
    print(f"m={m} shared leading gcd={first_factor}, all coefficient prefixes verified")


def self_check():
    checked = 0
    defects = []
    for p in primes_upto(131):
        if p<=13:
            continue
        for m in range((p+1)//4+1,(p-1)//2+1):
            r = complement_check(p,m)
            checked += 1
            if r:
                defects.append((m,p,r))
    for p in (17,1093,3511):
        # m=2 now tests the algebraic identity outside the contact band.
        h = (p+1)//2-2
        _, moments = modular_data(p,2*h-1)
        singular = h not in normal_indices(moments,p)
        assert singular == (pow(2,p-1,p*p)==1)
        assert singular == (fermat_difference(p,2)[1]==0)
    print(f"Complement coranks: {checked} actual pairs through p=131; defects={defects}")
    print("m=2 extension: Wieferich equivalence verified at p=17,1093,3511")
    for m in (10,18,32,36):
        prefix_certificate(m)


def census(prime_cap):
    # R289 D9 certified r=1 and a nonsingular radical at every leading failure
    # for p<=18000, so the pure-Q event there is exactly r=1 and e<=15.
    if not 17<=prime_cap<=18000:
        raise ValueError("the cited R289 radical certificate covers 17 <= p <= 18000")
    full_m = (prime_cap+2)//4
    count = complete_count = singular_count = 0
    edge = []
    band = defaultdict(list)
    for p in primes_upto(prime_cap):
        if p<=13:
            continue
        center = (p+1)//2
        max_h = (p-1)//4
        _, leading = modular_data(p,2*max_h-1)
        normal = normal_indices(leading,p)
        for h in range(1,max_h+1):
            m = center-h
            e = m-h
            count += 1
            if m<=full_m:
                complete_count += 1
            if h in normal:
                continue
            singular_count += 1
            assert h==1 or h-1 in normal
            if e<=15:
                edge.append((m,p,h,e))
    if prime_cap==18000:
        assert (count,singular_count)==(4350788,494)
        assert sorted(edge)==[(10,29,5,5),(18,67,16,2),(20,67,14,6),
                              (26,97,23,3),(27,103,25,2),(32,103,20,12),
                              (3452,13781,3439,13)]
    for m,p,h,e in edge:
        if m<=full_m:
            band[m].append((p,e))
    print(f"p<={prime_cap}: {count} pairs, {singular_count} singular, pure-Q={sorted(edge)}")
    print(f"complete m=1..{full_m}: {complete_count} pairs")
    for m,events in sorted(band.items()):
        primes = [p for p in primes_upto(4*m-2) if p>max(13,2*m)]
        terms = [(p,2*m-(p+1)//2) for p in primes]
        # floor(256 log2 p) and the next integer enclose each weight exactly.
        def bounds(weighted):
            lower = sum(e*((p**256).bit_length()-1) for p,e in weighted)
            return lower, lower+sum(e for p,e in weighted)
        lo,hi = bounds(events)
        full_lo,full_hi = bounds(terms)
        if 250*lo > 19*full_hi:
            comparison = "above"
        elif 40*hi < 3*full_lo:
            comparison = "below"
        else:
            raise ArithmeticError("integer bounds do not separate the target")
        ratio = sum(e*log(p) for p,e in events)/sum(e*log(p) for p,e in terms)
        print(f"m={m:4} weighted share={ratio:.12f} {comparison} 1-(4/3)log(2)")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--prime-cap",type=int,default=18000)
    parser.add_argument("--self-check",action="store_true")
    args = parser.parse_args()
    started = perf_counter()
    if args.self_check:
        self_check()
    census(args.prime_cap)
    print(f"Elapsed {perf_counter()-started:.3f}s")
