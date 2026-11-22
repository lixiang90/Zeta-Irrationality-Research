"""Check the lowest Y coefficient of the rescaled outer-band pencil over F_p."""

from argparse import ArgumentParser
from collections import Counter

from flint import nmod_mat, nmod_poly

from verify_zeta7_polynomial_content_round289 import (
    exact_moments, exact_pencil, normal_indices, primes_upto, residue,
)


def target_moments(p):
    """Return B_k/k for 1 <= k < p. The entries beyond (p-1)/2 vanish."""
    central = 1
    values = []
    for k in range(1, p):
        inv = pow(k, -1, p)
        central = central * (4*k-2) * inv % p
        values.append(30*(-1 if k % 2 else 1)*central*inv % p)
    return values


def pole_moments(p, length):
    """The anti-diagonals p^8 A_{k,k}/k for k=(p+1)/2+j."""
    first = (p+1)//2
    inverses = [0] + [pow(i, -1, p) for i in range(1, 2*length)]
    values = []
    for j in range(length):
        k = first+j
        choose = 1
        acc = -k
        for i in range(1, 2*j+2):
            choose = choose*(k+1-i)*inverses[i] % p
            acc += (2*i-k)*pow(choose, 4, p)
        values.append(-35*acc*pow(k, -1, p) % p)
    assert values[0] == 455*pow(16, -1, p) % p
    return values


def radical_form(p, h, e, target, pole):
    block = nmod_mat(h, h, [target[i+j] for i in range(h) for j in range(h)], p)
    basis, r = block.nullspace()
    if r == 0:
        return 0, 1
    # Each column contains the coefficients of u; row j of the cross-block starts at h+j.
    kernel = nmod_mat(h, r, [int(basis[i,j]) for i in range(h) for j in range(r)], p)
    image = nmod_mat(e, h, [target[h+i+j] for i in range(e) for j in range(h)], p)*kernel
    columns = [nmod_poly([int(image[i, j]) for i in range(e)], p) for j in range(r)]
    finv = nmod_poly(pole[:e], p).inverse_series_trunc(e)
    reduced = [(c*finv).truncate(e) for c in columns]
    gram = nmod_mat(r, r, [int((a*b)[e-1]) for a in columns for b in reduced], p)
    return r, int(gram.det())


def direct_check(p, m, target, pole):
    """Interpolate the entire symbol using exactly m+1 distinct nodes and exact moments."""
    first = (p+1)//2
    h, e = first-m, 2*m-first
    r, gram = radical_form(p, h, e, target, pole)
    actual_a, actual_b = exact_moments(2*m-1)
    reduced_a = [residue(p**8*a, p) for a in actual_a]
    assert reduced_a == [0]*(first-1)+pole[:e]
    assert [residue(b, p) for b in actual_b] == target[:2*m-1]
    vandermonde = nmod_mat(m+1,m+1,[pow(y,i,p) for y in range(m+1) for i in range(m+1)],p)
    evaluations = []
    for y in range(m+1):
        values = [(a+y*b) % p for a,b in zip(reduced_a,target)]
        pencil = nmod_mat(m,m,[values[i+j] for i in range(m) for j in range(m)],p)
        evaluations.append(int(pencil.det()))
    coeffs = vandermonde.solve(nmod_mat(m+1,1,evaluations,p))
    order = next((i for i in range(m+1) if coeffs[i,0]), m+1)
    assert order >= h+r and (order == h+r) == bool(gram)
    print(f"direct (m,p,h,e,r)={(m,p,h,e,r)} order={order} coefficient={coeffs[order,0] if order<=m else 0}")


def census(max_m):
    pairs = 0
    ranks = Counter()
    failures = []
    for p in primes_upto(4*max_m-2):
        if p <= 13:
            continue
        first = (p+1)//2
        min_m, last_m = (p+1)//4+1, min(max_m,(p-1)//2)
        if last_m < min_m:
            continue
        sizes = range(first-last_m, first-min_m+1)
        pairs += len(sizes)
        target = target_moments(p)
        normal = normal_indices(target[:2*sizes[-1]-1], p)
        singular = [h for h in sizes if h not in normal]
        if not singular:
            continue
        pole = pole_moments(p, first-2*singular[0])
        for h in singular:
            m = first-h
            r, gram = radical_form(p,h,m-h,target,pole)
            assert r > 0
            ranks[r] += 1
            if not gram:
                failures.append((m,p,h,r))
    print(f"m<= {max_m}: pairs={pairs}, target defects={dict(ranks)}, singular radical forms={failures}")


def small_primes():
    """Use the actual rational pencil when its first pole need not be a unit."""
    def order(n, p):
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        return v

    a,b = exact_moments(11)
    actual = {m: exact_pencil(m,a,b) for m in range(1,7)}
    rows = []
    for p in primes_upto(13):
        for m in range(1,7):
            if 2*m < p < 4*m-1:
                h = (p+1)//2-m
                content = actual[h][1]
                t = order(content.p,p)-order(content.q,p)
                rows.append((m,p,h,t,order(actual[m][0],p)))
    assert rows == [(2,5,1,1,8),(3,7,1,0,14),(4,11,2,0,16),(5,11,1,0,32),
                    (4,13,3,0,7),(5,13,2,0,21),(6,13,1,0,35)]
    print("p<=13 (m,p,h,small content,monic denominator order):", rows)


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=256)
    args = parser.parse_args()
    small_primes()
    for m,p in ((6,17),(10,29),(18,67),(20,67),(32,103)):
        direct_check(p,m,target_moments(p),pole_moments(p,2*m-(p+1)//2))
    census(args.through)
