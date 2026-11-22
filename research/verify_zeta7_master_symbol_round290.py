"""Compare the shared rational polynomial with each original outer-prime pencil."""

from argparse import ArgumentParser
from math import comb, factorial, gcd, lcm, prod

from flint import fmpq, fmpq_mat, fmpq_poly, fmpz_mat, nmod_mat, nmod_poly

from verify_zeta7_polynomial_content_round289 import exact_moments, primes_upto, residue


def pole_coefficients(length):
    # Binomial formula for the exact rational f_j, before choosing a prime.
    values = []
    for j in range(length):
        x = fmpq(2*j+1, 2)
        choose, total = fmpq(1), -x
        for i in range(1, 2*j+2):
            choose = choose*(x+1-i)/i
            total += (2*i-x)*choose**4
        value = -35*total/x
        assert int(value.q) & (int(value.q)-1) == 0
        values.append(value)
    return fmpq_poly(values)


def interpolation(m):
    all_nodes = prod(2*m+2*i-1 for i in range(m))
    return fmpq_poly([fmpq((-1)**j*all_nodes,
                          (2*m+2*j-1)*2**(m-1)*factorial(j)*factorial(m-1-j))
                     for j in range(m)])


def harmonic_shadow(last):
    harmonics = [fmpq(0)]
    for t in range(1, 2*last+1):
        harmonics.append(harmonics[-1]+fmpq(1, t))
    return [-fmpq(35,k)*sum((k-2*i)*comb(k,i)**4*harmonics[k+i]
                              for i in range(k+1)) for k in range(1,last+1)]


def prime_order(value, p):
    assert value
    v = 0
    while value % p == 0:
        v += 1
        value //= p
    return v


def symbol(m, poles, target, interpolation_poly=None):
    if interpolation_poly is None:
        interpolation_poly = interpolation(m)
    coeff = (poles*interpolation_poly).truncate(m)
    base = fmpq_mat(m,m,[coeff[i-j] if i>=j else 0 for i in range(m) for j in range(m)])
    slope = fmpq_mat(m,m,[target[m+i-j-1] for i in range(m) for j in range(m)])
    matrix = slope.solve(base)
    sign = (-1)**(m*(m-1)//2)
    polynomial = (-matrix).charpoly() * (sign*slope.det())
    assert polynomial[0] == sign*(poles[0]*interpolation_poly[0])**m
    return interpolation_poly, coeff, matrix, polynomial


def smith_check(m, interpolation_poly):
    scale = lcm(*(int(x.q) for x in interpolation_poly))
    entries = [int(scale*interpolation_poly[i-j]) if i>=j else 0
               for i in range(m) for j in range(m)]
    values = fmpz_mat(m,m,entries).snf()
    return [int(values[i,i]) for i in range(m)]


def interpolate_at_integers(values, one, variable, divide):
    """Newton interpolation at the consecutive nodes 0, 1, ... over a field."""
    differences = list(values)
    result, basis = 0*one, one
    for k in range(len(values)):
        result += differences[0]*basis
        if len(differences) == 1:
            break
        differences = [b-a for a,b in zip(differences, differences[1:])]
        basis = divide(basis*(variable-k), k+1)
    return result


def factor_check(m, poles, target, master):
    x = fmpq_poly([0,1])
    one = fmpq_poly([1])
    max_degree = m*(m-1)
    rows = []
    for t in range(max_degree+1):
        local = sum((comb(t,k)*(x-1)**k for k in range(min(t,m-1)+1)), 0*one)
        rows.append(symbol(m,poles,target,local)[3])
    for i in range(m+1):
        degree = (m-1)*(m-i)
        values = [row[i] for row in rows[:degree+1]]
        coefficient = interpolate_at_integers(values, one, x, lambda poly,k: poly/k)
        assert coefficient(fmpq(1,2)-m) == master[i]
        assert coefficient(i) != 0
        for a in range(i+1,m):
            q,b = divmod(m,a)
            factor = (x-a)**(q*(a-i)+max(0,b-i))
            coefficient, remainder = divmod(coefficient, factor)
            assert not remainder
        if 1 <= i < m:
            bound = i + sum(i*(m//a)+min(i,m%a) for a in range(i+1,m))
            assert coefficient.degree() <= bound


def long_block_check():
    cases = 0
    for t,numerator,denominator in ((20,93751,100000),(22,47,50)):
        for m in [*range(2,257),10**6+7,10**12+39]:
            edges = [(numerator**j*m+denominator**j-1)//denominator**j for j in range(t+1)]
            for top,bottom in zip(edges,edges[1:]):
                if top==bottom:
                    continue
                left = m-bottom
                right = m-(15*(top-1)+15)//16
                for e in (bottom,top-1):
                    assert m-e<=left<=right<=m-e+e//16
                if m>10**12:
                    assert right>=left+1
                cases += 1
    return cases


def strip_scan(last):
    """Count single-coefficient witnesses that survive even though the zero block fails."""
    primes = primes_upto(4*last-2)
    poles = pole_coefficients(last)
    betas = [fmpq(30*(-1)**k*comb(2*k,k),k) for k in range(1,2*last)]
    totals = {t: [0,0,0,0] for t in (20,22)}
    first_false = {}
    for m in range(1,last+1):
        edges = [(15**j*m+16**j-1)//16**j for j in range(23)]
        for p in primes:
            if not max(13,2*m)<p<4*m-1:
                continue
            h = (p+1)//2-m
            e = m-h
            high = [0]*(m+h-1)+[residue(poles[j],p) for j in range(e)]
            low = [residue(b,p) for b in betas[:2*m-1]]
            const = nmod_mat(m,m,[high[i+j] for i in range(m) for j in range(m)],p)
            slope = nmod_mat(m,m,[low[i+j] for i in range(m) for j in range(m)],p)
            determinant = slope.det()
            if determinant:
                poly = (-slope.solve(const)).charpoly()*determinant
            else:
                values = [int((const+v*slope).det()) for v in range(m+1)]
                poly = interpolate_at_integers(values, nmod_poly([1],p), nmod_poly([0,1],p),
                                               lambda q,k: q*pow(k,-1,p))
            event = all(not poly[i] for i in range(h,h+e//16+1))
            for t,counts in totals.items():
                if e<edges[t]:
                    counts[0] += 1
                    continue
                j = next(j for j in range(t) if edges[j+1]<=e<edges[j])
                i = m-edges[j+1]
                assert h<=i<=h+e//16
                witness = not poly[i]
                assert not event or witness
                counts[1] += 1
                counts[2] += int(witness)
                counts[3] += int(event)
                if witness and not event:
                    first_false.setdefault(t,(m,p,h,e,i))
    print("strip scan m <=",last,"(edge, covered, zero witness, full event within cover)",totals)
    print("first excess witness (m,p,h,e,i)",first_false)


def run():
    sizes = list(range(1,33))+[36]
    last = 2*max(sizes)-1
    rational, target = exact_moments(last)
    shadow = harmonic_shadow(last)
    poles = pole_coefficients(max(sizes))
    primes = primes_upto(4*max(sizes)-2)
    pairs = matrix_powers = smith_tests = discriminants = parameter_tests = 0
    exceptions = []
    for m in sizes:
        ell, coefficients, matrix, polynomial = symbol(m,poles,target)
        for i in range(m-1):
            assert (i+1)*polynomial[i+1]**2 > (i+2)*polynomial[i]*polynomial[i+2]
            discriminants += 1
        if m<=6:
            factor_check(m,poles,target,polynomial)
            parameter_tests += m+1
        smith = smith_check(m,ell) if m<=18 else None
        for p in primes:
            if not 2*m<p<4*m-1:
                continue
            pairs += 1
            h=(p+1)//2-m
            e=m-h
            assert [residue(ell[i],p) for i in range(m)] == [int(i==h) for i in range(m)]
            for i in range(m):
                assert prime_order(int(ell[i].p),p)==int(i!=h)
            actual=[residue(p**8*x,p) for x in rational[:2*m-1]]
            assert actual==[residue(p*x,p) for x in shadow[:2*m-1]]
            expected=[residue(coefficients[d],p) if d>=0 else 0 for d in range(1-m,m)]
            assert actual==expected
            betas=[residue(x,p) for x in target[:2*m-1]]
            reduced=[residue(polynomial[i],p) for i in range(m+1)]
            for y in range(m+1):
                moments=[(x+y*b)%p for x,b in zip(actual,betas)]
                value=nmod_mat(m,m,[moments[i+j] for i in range(m) for j in range(m)],p).det()
                assert int(value)==sum(c*pow(y,i,p) for i,c in enumerate(reduced))%p
            s=e//16+1
            event=not any(reduced[h:h+s])
            if event:
                exceptions.append((m,p,e))
            if p>13 and reduced[m]:
                mat=nmod_mat(m,m,[residue(matrix[i,j],p) for i in range(m) for j in range(m)],p)
                assert (int((mat**(s+1)).rank())<=e-s)==event
                matrix_powers+=1
            if smith is not None:
                q,b=divmod(m,h)
                assert [prime_order(x,p) for x in smith]==[0]*e+[q]*(h-b)+[q+1]*b
                smith_tests+=1
            for j in range(22):
                a=(15**j*m+16**j-1)//16**j
                b=(15**(j+1)*m+16**(j+1)-1)//16**(j+1)
                if b<=e<a:
                    i=m-b
                    assert h<=i<=h+s-1
                    if event:
                        assert gcd(int(polynomial[i].p),p)==p
    print("exact master/shadow/original pairs",pairs,"power tests",matrix_powers,
          "integer Smith tests",smith_tests)
    print("pure events (m,p,e)",exceptions)
    print("positive Laguerre expressions",discriminants,"factored parameter polynomials",parameter_tests)
    assert [(m,p) for m,p,e in exceptions if p<=13] == [(2,5),(3,7),(4,13),(5,13),(6,13)]
    print("long common index intervals",long_block_check())


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--strips", type=int, metavar="M", help="check the single-coefficient covers up to order M")
    args = parser.parse_args()
    run()
    if args.strips:
        strip_scan(args.strips)
