"""Exact elementary-divisor tests for the equal-slope weight-seven Hankel pencil."""

from argparse import ArgumentParser
from bisect import bisect_left, bisect_right
from fractions import Fraction
from math import comb, factorial, gcd, isqrt, lcm, log, prod
from time import perf_counter

import numpy as np
from flint import fmpq, fmpq_mat, fmpz, fmpz_mat, nmod_mat, nmod_poly


def primes_upto(limit):
    flags = bytearray(b'\1') * (limit + 1)
    flags[:2] = b'\0\0'
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p*p::p] = b'\0' * ((limit-p*p)//p + 1)
    return [p for p in range(2, limit + 1) if flags[p]]


def normal_indices(moments, p):
    """Indices of invertible leading Hankel matrices via the finite Laurent fraction."""
    size = (len(moments) + 1)//2
    # An arbitrary last term does not affect the size-size Hankel determinant.
    terms = [int(s) for s in moments[:2*size]]
    terms.extend([0] * (2*size-len(terms)))
    left = nmod_poly([0]*(2*size) + [1], p)
    right = nmod_poly(terms[::-1], p)
    indices = set()
    degree = 0
    while right:
        degree += left.degree() - right.degree()
        if degree > size:
            break
        indices.add(degree)
        if degree == size:
            break
        left, right = right, left % right
    return indices


def modular_data(prime, n_max):
    # All denominators used in the constant moments are at most 2*n_max < prime.
    inverses = [0, 1]
    for k in range(2, 2*n_max + 1):
        inverses.append(-((prime//k)*inverses[prime % k]) % prime)
    leading = []
    central = 1
    for k in range(1, n_max+1):
        central = central * (4*k-2)*inverses[k] % prime
        leading.append(30*(-1 if k % 2 else 1)*central*inverses[k] % prime)
    return inverses, leading


def constant_moments_mod(p, n_max, inverses):
    """Vectorized partial fractions, with exact word-integer operations modulo p."""
    # Each harmonic is reduced before multiplication; the signed jet is below 100*p^3.
    if 100*p**3 >= (1 << 63):
        raise ValueError("the vectorized word bound is exceeded at this prime")
    inv = np.asarray(inverses[:2*n_max+1], dtype=np.int64)
    harmonic = [None]
    powers = np.ones_like(inv)
    for _ in range(8):
        powers = (powers*inv) % p
        harmonic.append(np.cumsum(powers, dtype=np.int64) % p)
    fac = [1]
    inv_fac = [1]
    for k in range(1, n_max+1):
        fac.append((fac[-1]*k) % p)
        inv_fac.append(inv_fac[-1]*inverses[k] % p)
    fourth = np.asarray([pow(v, 4, p) for v in inv_fac], dtype=np.int64)
    indices = np.arange(n_max+1, dtype=np.int64)
    out = []
    for n in range(1, n_max+1):
        fwd = slice(0, n+1)
        rev = slice(n, None, -1)
        to_harm = slice(n, 2*n+1)
        r = n-2*indices[fwd]
        t1 = (4*(harmonic[1][fwd]-harmonic[1][rev])) % p
        g2 = (4*(harmonic[2][fwd]+harmonic[2][rev])) % p
        g3 = (4*(harmonic[3][fwd]-harmonic[3][rev])) % p
        t2 = ((t1*t1+g2) % p * inverses[2]) % p
        t3 = ((t1*t2+g2*t1+g3) % p * inverses[3]) % p
        jet = ((r*t3+2*t2)*harmonic[5][to_harm]
               +5*(r*t2+2*t1)*harmonic[6][to_harm]
               +15*(r*t1+2)*harmonic[7][to_harm]
               +35*r*harmonic[8][to_harm]) % p
        weights = (fourth[fwd]*fourth[rev]) % p
        value = int(np.sum((jet*weights) % p, dtype=np.int64))
        out.append(-value*pow(fac[n], 4, p)*inverses[n] % p)
    return out


def exact_moments(n_max):
    harmonic = [[fmpq(0)] for _ in range(9)]
    for j in range(1, 9):
        for k in range(1, 2*n_max+1):
            harmonic[j].append(harmonic[j][-1]+fmpq(1, k**j))
    constant, leading = [], []
    for n in range(1, n_max+1):
        value = fmpq(0)
        for c in range(n+1):
            r = n-2*c
            j1 = 4*(harmonic[1][c]-harmonic[1][n-c])
            g2 = 4*(harmonic[2][c]+harmonic[2][n-c])
            g3 = 4*(harmonic[3][c]-harmonic[3][n-c])
            j2 = (j1*j1+g2)/2
            j3 = (j1*j2+g2*j1+g3)/3
            jet = ((r*j3+2*j2)*harmonic[5][n+c]
                   +5*(r*j2+2*j1)*harmonic[6][n+c]
                   +15*(r*j1+2)*harmonic[7][n+c]
                   +35*r*harmonic[8][n+c])
            value -= comb(n,c)**4*jet
        constant.append(value/n)
        leading.append(fmpq(30*(-1)**n*comb(2*n, n), n))
    return constant, leading


def residue(value, modulus):
    return int(value.p) * pow(int(value.q), -1, modulus) % modulus


def pencil_matrix(moments, size, matrix_type):
    return matrix_type(size, size, [moments[i+j] for i in range(size) for j in range(size)])


def polynomial_fallback(size, p, bits=8):
    """All size+1 values, enough since the evaluation nodes are distinct modulo p."""
    constant, leading = exact_moments(2*size-1)
    modulus = p**bits
    const = [residue(a, modulus) for a in constant]
    lead = [residue(b, modulus) for b in leading]
    order = bits
    for t in range(size+1):
        values = [(a+t*b) % modulus for a,b in zip(const,lead)]
        det = int(pencil_matrix(values, size, fmpz_mat).det()) % modulus
        if det:
            v = 0
            while det % p == 0:
                v += 1
                det //= p
            order = min(order, v)
            if order == 0:
                break
    return order


def band_budget(max_m, primes, survivors):
    """Certify the finite top-band contribution using rational enclosures for log2(p)."""
    unit = 256
    lower = [0]
    times_prime = [0]
    prime_sum = [0]
    for p in primes:
        value = (p**unit).bit_length()-1
        lower.append(lower[-1]+value)
        times_prime.append(times_prime[-1]+p*value)
        prime_sum.append(prime_sum[-1]+p)
    corrections={}
    for m,p,h,v in survivors:
        corrections.setdefault(m,{})[p]=v if v<8 else 8*(m-h)
    below=[]
    ambiguous=[]
    for m in range(1,max_m+1):
        i=bisect_right(primes,2*m)
        j=bisect_left(primes,4*m-1)
        bound=4*((4*m-1)*(lower[j]-lower[i])-(times_prime[j]-times_prime[i]))
        width=4*((4*m-1)*(j-i)-(prime_sum[j]-prime_sum[i]))
        for p,lost in corrections.get(m,{}).items():
            bound-=lost*((p**unit).bit_length()-1)
            width-=lost
        target=10*m*m*unit
        if bound>target:
            continue
        if bound+width>target:
            ambiguous.append(m)
            actual=prod(p**(8*(2*m-(p+1)//2)-corrections.get(m,{}).get(p,0))
                        for p in primes[i:j])
            if actual>1<<(10*m*m):
                continue
        below.append(m)
    print("Top band alone at or below 1024^(m^2):",below,
          "exact product tie-breaks:",ambiguous,flush=True)
    return below


def check_band(max_m):
    primes = [p for p in primes_upto(4*max_m-2) if p>13]
    totals = [0]*(max_m+1)
    leading_failures = []
    constant_failures = []
    survivors = []
    for p in primes:
        first = (p+1)//2
        lo_m = (p+1)//4 + 1
        hi_m = min(max_m, (p-1)//2)
        if lo_m > hi_m:
            continue
        hs = range(first-hi_m, first-lo_m+1)
        for h in hs:
            totals[first-h] += 1
        n_max = 2*hs[-1]-1
        inverses, leading = modular_data(p, n_max)
        lead_units = normal_indices(leading, p)
        missing = [h for h in hs if h not in lead_units]
        if not missing:
            continue
        leading_failures.extend((first-h,p,h) for h in missing)
        constants = constant_moments_mod(p, 2*missing[-1]-1, inverses)
        const_units = normal_indices(constants, p)
        for h in missing:
            if h in const_units:
                continue
            triple = (first-h,p,h)
            constant_failures.append(triple)
            for t in range(1,h+1):
                values = [(a+t*b) % p for a,b in zip(constants[:2*h-1],leading)]
                if h in normal_indices(values,p):
                    break
            else:
                v = polynomial_fallback(h, p)
                assert v>0
                survivors.append((*triple,v))
    total=sum(totals)
    print(f"Continuous m=1..{max_m}, primes={len(primes)}, pairs={total}, "
          f"leading_unit={total-len(leading_failures)}, constant_rescue="
          f"{len(leading_failures)-len(constant_failures)}, fallback={constant_failures}, "
          f"positive_content_mod_p8={survivors}",flush=True)
    for d in (64,128,256,512,1024,2048,4096):
        if d <= max_m:
            print("through",d,"pairs",sum(totals[:d+1]),"leading_failures",
                  sum(m<=d for m,p,h in leading_failures),flush=True)
    if leading_failures:
        print("first and last leading failures:", leading_failures[:4], leading_failures[-4:],
              "max h:", max(h for m,p,h in leading_failures),flush=True)
    band_budget(max_m,primes,survivors)
    return totals, leading_failures, constant_failures, survivors


def exact_pencil(size, constants, leading):
    """Return actual monic denominator and rational content using falling-factorial gcd."""
    a, b, row_scales = [], [], []
    for i in range(size):
        row_a = constants[i:i+size]
        row_b = leading[i:i+size]
        scale = lcm(*(int(x.q) for x in row_a+row_b))
        row_scales.append(scale)
        a.extend((scale*x).p for x in row_a)
        b.extend((scale*x).p for x in row_b)
    pencil = fmpz_mat(size,size,a)
    slopes = fmpz_mat(size,size,b)
    values=[]
    for _ in range(size+1):
        values.append(pencil.det())
        pencil += slopes
    coeff_gcd = fmpz(0)
    for j in range(size+1):
        coeff, rem = divmod(values[0],factorial(j))
        assert not rem
        coeff_gcd = coeff_gcd.gcd(coeff)
        values = [y-x for x,y in zip(values,values[1:])]
    assert coeff == slopes.det()
    dstar = abs(coeff)//coeff_gcd
    content = fmpq(coeff_gcd, prod(row_scales))
    if size <= 8:
        cmat = pencil_matrix(constants,size,fmpq_mat)
        bmat = pencil_matrix(leading,size,fmpq_mat)
        monic = bmat.solve(-cmat).charpoly()
        assert monic.denom() == dstar
        assert abs(bmat.det()) == content*dstar
    return dstar, content


def denominators(*sequences):
    den, ratios = [], []
    prev = 1
    for values in zip(*sequences):
        d=lcm(prev,*(int(x.q) for x in values))
        den.append(d)
        ratios.append(d//prev)
        prev=d
    return den,ratios


def shifted_moments(moments,den):
    """Integer moments after x -> x+4, with a nested denominator chain."""
    values=[]
    for i,d in enumerate(den):
        weights=[comb(i,j) << (2*(i-j)) for j in range(i+1)]
        values.append(sum(((d*x).p*w for w,x in zip(weights,moments)),fmpz(0)))
    return values


def leading_minors(row,growth):
    """All leading determinants by normalized Desnanot--Jacobi condensation."""
    previous = [fmpz(1)]*(len(row)+2)
    yield row[0]
    for h in range(2,(len(row)+1)//2+1):
        current=[]
        for s in range(len(row)-2):
            num = (growth[s+h-1]*row[s]*row[s+2]
                   -growth[s+2*h-2]*row[s+1]**2)
            val, remainder = divmod(num, previous[s+2])
            assert not remainder and val>0
            current.append(val)
        previous,row=row,current
        yield row[0]


def all_exact_pencils(max_m):
    constants, leading = exact_moments(2*max_m-1)
    den, growth=denominators(constants,leading)
    aa,bb=shifted_moments(constants,den),shifted_moments(leading,den)
    samples = [[] for _ in range(max_m+1)]
    for t in range(max_m+1):
        row = [x-t*y for x,y in zip(aa,bb)]
        for h,minor in enumerate(leading_minors(row,growth),1):
            if t<=h:
                samples[h].append(minor)
    output=[]
    for m in range(1,max_m+1):
        values=samples[m]
        content=fmpz(0)
        for j in range(m+1):
            coeff,rem=divmod(values[0],factorial(j))
            assert not rem
            content=content.gcd(coeff)
            values=[y-x for x,y in zip(values,values[1:])]
        assert coeff>0
        dstar=coeff//content
        rational_content=fmpq(content,prod(den[m-1:2*m-1]))
        if m<=12:
            assert (dstar,rational_content)==exact_pencil(m,constants,leading)
        output.append((dstar,rational_content))
    return output


def all_prime_witnesses(max_h):
    const,lead=exact_moments(2*max_h-1)
    nums=[]
    for is_leading, sequence in ((False,const),(True,[-x for x in lead])):
        den,growth=denominators(sequence)
        minors=leading_minors(shifted_moments(sequence,den),growth)
        numerators = []
        hilbert_inverse = 1
        for h,minor in enumerate(minors,1):
            value = fmpq(minor,prod(den[h-1:2*h-1]))
            numerators.append(value.p)
            if is_leading:
                hilbert_inverse *= (2*h-1)*comb(2*h-2,h-1)**2
                normalized = value*fmpq(hilbert_inverse,30**h)
                assert normalized.q == 1 and 1 <= normalized.p <= 1 << (2*h*h-h)
                assert normalized.p % (1 << (h+1)) == 1 << h
        nums.append(numerators)
    survivors=[]
    primes=primes_upto(max(13,4*max_h-2))
    for h,(c,b) in enumerate(zip(*nums),1):
        common=c.gcd(b)
        for p in primes:
            if p>max(13,4*h-2):
                break
            while common%p==0:
                common//=p
        if common!=1:
            survivors.append((h,common))
    print(f"All-prime witnesses h=1..{max_h}: residual gcds after "
          f"stripping primes <=max(13,4h-2): {survivors}",flush=True)
    return survivors


def report_exact(m,dstar,content,elapsed=None):
    remainder = content.p
    for p in primes_upto(max(13,4*m-2)):
        while remainder % p == 0:
            remainder //= p
    threshold = fmpz(1) << (10*m*m)
    relation = ">" if dstar>threshold else ("=" if dstar==threshold else "<")
    extra=str(dstar) if m<=3 else (f"t={elapsed:.3f}s" if elapsed is not None else "")
    print(m,dstar.bit_length(),f"{log(int(dstar))/m**2:.9f}",relation,
          remainder,extra,flush=True)


def run_exact(sizes):
    constants, leading = exact_moments(2*max(sizes)-1)
    print("m dstar_bits log_dstar/m^2 cmp_1024^(m^2) stripped_content_numerator sample_dstar",flush=True)
    for m in sizes:
        since = perf_counter()
        dstar, content = exact_pencil(m,constants,leading)
        report_exact(m,dstar,content,perf_counter()-since)


def self_check():
    from verify_zeta7_contact_round288 import rational_part
    a,b=exact_moments(39)
    for k in range(1,40):
        assert Fraction(int(a[k-1].p),int(a[k-1].q)) == rational_part(k,k)/k
    for p in (83,89,97,167,457):
        n=39
        inverses, lead=modular_data(p,n)
        constant=constant_moments_mod(p,n,inverses)
        assert constant==[residue(x,p) for x in a]
        assert lead==[residue(x,p) for x in b]
        for moments in (lead,constant,[0,0,1]+lead[:-3]):
            normal=normal_indices(moments,p)
            for h in range(1,21):
                det=nmod_mat(h,h,[moments[i+j] for i in range(h) for j in range(h)],p).det()
                assert (h in normal) == bool(det)
    all_exact_pencils(8)
    assert polynomial_fallback(5,29)==0
    print("Self-check: exact moments through 39, modular moments and 300 direct Hankel determinants.",flush=True)


if __name__ == "__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--band",type=int,default=0,metavar="MAX_M")
    parser.add_argument("--exact",type=int,nargs="+",default=[])
    parser.add_argument("--through",type=int,default=0,metavar="MAX_M")
    parser.add_argument("--fixed",type=int,default=0,metavar="MAX_H")
    parser.add_argument("--self-check",action="store_true")
    args=parser.parse_args()
    if not args.band and not args.exact and not args.through and not args.fixed and not args.self_check:
        args.self_check=True
    started=perf_counter()
    if args.self_check:
        self_check()
    if args.band:
        check_band(args.band)
    if args.exact:
        run_exact(args.exact)
    if args.through:
        print("m dstar_bits log_dstar/m^2 cmp_1024^(m^2) stripped_content_numerator sample_dstar")
        for m,(dstar,content) in enumerate(all_exact_pencils(args.through),1):
            report_exact(m,dstar,content)
    if args.fixed:
        all_prime_witnesses(args.fixed)
    print(f"Elapsed {perf_counter()-started:.3f}s",flush=True)
