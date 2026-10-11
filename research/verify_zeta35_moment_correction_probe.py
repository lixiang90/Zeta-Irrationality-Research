"""Independent bounded audit of the atom and polynomial-moment probes.

Rebuilds the K=40 mixed rational functional without importing either producer.
It certifies baseline positivity by interval LDL before applying the relative
trace criterion, and checks full rational moments at the outer primes.
"""
import json
import math
import sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat, arb, arb_mat, ctx

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent


def dpoly(k):
    answer = Poly([1])
    for j in range(1, k+1):
        answer *= Poly([j*j, 1])
    return answer


def mu(e):
    pure5 = Q(-1)**e * Q.bernoulli(2*e+2) * (2*e+3)*(2*e+4)*(2*e+5)/24
    shifted3 = Q(-1)**(e+1) * (2*e+5)*Q.bernoulli(2*e+4)/2
    return pure5-3*shifted3


def aq(q):
    return arb(int(q.numerator))/int(q.denominator)


def modq(q, p):
    assert int(q.denominator) % p
    return int(q.numerator)*pow(int(q.denominator), -1, p) % p


def rebuild(k=40, n=3, h=37):
    dn, dk = dpoly(n), dpoly(k)
    w = dn**6
    quotients = [(w*Poly([0]*s+[1]))//dk for s in range(2*h-1)]
    h3 = h5 = Q(0)
    poles = []
    for j in range(1, k+1):
        h3 += Q(1, j**3)
        h5 += Q(1, j**5)
        if j <= n:
            continue
        residue = Q(w(-j*j), math.prod(i*i-j*j for i in range(1,k+1) if i != j))
        const = -j**4*(h5+3*h3)-1+Q(1,2*j)-Q(3*j*j,2)+Q(3*j,2)
        poles.append((j,residue,const))
    aa, bb = [], []
    for s,q in enumerate(quotients):
        a = sum((q[e]*mu(e) for e in range(q.degree()+1)), Q(0))
        b = Q(0)
        for j,residue,const in poles:
            c = residue*Q(-j*j)**s
            a += c*const
            b += c*j**4
        aa.append(a)
        bb.append(b)
    return aa,bb,quotients


def ldl_positive(h):
    dim = h.nrows()
    ll = [[arb(0) for _ in range(dim)] for _ in range(dim)]
    dd = []
    for i in range(dim):
        for j in range(i):
            ll[i][j] = (h[i,j]-sum((ll[i][k]*ll[j][k]*dd[k] for k in range(j)),arb(0)))/dd[j]
        d = h[i,i]-sum((ll[i][k]**2*dd[k] for k in range(i)),arb(0))
        assert d > 0, (i,d)
        dd.append(d)
        ll[i][i] = arb(1)
    return dd


def main():
    data = json.loads((ROOT/'zeta35_infinity_correction_probe.json').read_text(encoding='utf-8'))
    atom = json.loads((ROOT/'zeta35_atom_frobenius_probe.json').read_text(encoding='utf-8'))
    cached = json.loads((ROOT/'zeta35_mixed_moments.json').read_text(encoding='utf-8'))
    cached = next(row for row in cached['rows'] if row['a'] == 3 and row['b'] == 1)
    aa,bb,qq = rebuild()
    assert aa == list(map(Q,cached['constant_entries']))
    assert bb == list(map(Q,cached['linear_entries']))
    # Full rational moments, rather than only polynomial quotients, have the
    # same first-order p-denominator sequence at these four outer primes.
    local_rows = []
    for row in atom['cases'][0]['rows']:
        p,s0,r = row['p'],row['first_bad_matrix_antidiagonal'],row['bad_matrix_rank']
        lam = [modq(p*a,p) for a in aa]
        polynomial_lam = [sum(modq(q[e],p)*modq(p*mu(e),p)
                              for e in range(q.degree()+1)) % p for q in qq]
        assert lam == polynomial_lam
        assert all(modq(p*b,p) == 0 for b in bb)
        assert all(x == 0 for x in lam[:s0])
        assert lam[s0] == 3*pow(2,-1,p) % p
        assert r == 2*37-1-s0
        early = row['frobenius_witness']['early']
        assert early >= 1 and s0-early == p-1
        assert lam[early] == 0 and lam[s0] != 0
        # Every finite sum of p-integral nodes with first-order pole weights
        # satisfies exactly this period, regardless of the number of nodes.
        assert all(pow(q,early,p) == pow(q,s0,p) for q in range(p))
        local_rows.append(dict(p=p,s0=s0,rank=r,full_functional_matches=True))
    ctx.prec = 12000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    h = arb_mat([[aq(aa[i+j])+theta*aq(bb[i+j]) for j in range(37)] for i in range(37)])
    pivots = ldl_positive(h)
    hinv = h.inv()
    corrected = []
    for row in data['rows']:
        corr = [Q(0) for _ in aa]
        for spec in row['moment_specs']:
            p,e,c = spec['p'],spec['e'],Q(spec['correction'])
            assert e == p-3
            assert modq(p*c,p) == 3*pow(2,-1,p) % p
            for s,q in enumerate(qq):
                corr[s] += c*q[e] if e <= q.degree() else 0
        exact_c = fmpq_mat([[corr[i+j] for j in range(37)] for i in range(37)])
        assert exact_c.rank() == row['correction_rank']
        cmat = arb_mat([[aq(corr[i+j]) for j in range(37)] for i in range(37)])
        relative = hinv*cmat
        trace2 = (relative*relative).trace()
        assert (trace2-arb(row['trace_relative_square_interval'])).contains(0)
        certified = trace2 < 1
        assert certified == row['relative_norm_certified']
        if certified:
            # Extra, independent sufficient test using interval LDL.
            ldl_positive(h-cmat)
        corrected.append(dict(primes=row['primes'],rank=exact_c.rank(),
                              trace_square_interval=trace2.str(30),
                              positive_definite_certified=certified))
    out = dict(status='passed',scope='K=40; no asymptotic conclusion; content was not rebuilt',
               exact_full_entry_equalities=146,baseline_ldl_positive_pivots=len(pivots),
               outer_prime_checks=local_rows,corrections=corrected)
    (ROOT/'zeta35_moment_correction_probe_verified.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
