"""Exact obstruction to regular finite-node atoms cancelling outer bad moments.

This tests one new functional-correction proposal, not irrationality.  All
arithmetic is over finite fields; no zeta approximation is used.
"""
import json
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, nmod_mat
from zeta35_target31 import primes_to
import zeta35_mixed_moments as mixed


def modq(q, p):
    assert int(q.denominator) % p != 0
    return int(q.numerator) * pow(int(q.denominator), -1, p) % p


def case(n, m=6):
    K, N, h = 40*n, 3*n, 37*n
    w = m*N
    degree = w + 2*h - 2 - K
    W = Poly(mixed.original.Dpoly(N)**m)
    D = Poly(mixed.original.Dpoly(K))
    moments = [Q(-1)**e * Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24
               - 3*mixed.mu3(e+1) for e in range(degree+1)]
    quotients = [(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    rows = []
    for p in primes_to(degree+3):
        if p <= K:
            continue
        gamma = [modq(p*x, p) for x in moments]
        bad = [e for e, g in enumerate(gamma) if g]
        if not bad:
            continue
        assert min(bad) == p-3
        sequence = [sum(modq(q[e], p)*gamma[e] for e in range(q.degree()+1)) % p
                    for q in quotients]
        s0 = K-w+p-3
        earlier = K-w-2
        assert 1 <= earlier < s0 <= 2*h-2
        assert sequence[earlier] == 0
        assert sequence[s0] == 3*pow(2, -1, p) % p
        assert s0-earlier == p-1
        H = nmod_mat([[sequence[i+j] for j in range(h)] for i in range(h)], p)
        r = 2*h+w-K+2-p
        assert H.rank() == r
        # Includes every F_p node; repeated nodes cannot enlarge its span.
        atoms = [[pow(q, s, p) for q in range(p)] for s in range(2*h-1)]
        B = nmod_mat(atoms, p)
        augmented = nmod_mat([atoms[s]+[sequence[s]] for s in range(2*h-1)], p)
        assert B.rank() == p
        assert augmented.rank() == p+1
        row = dict(p=p, first_bad_moment=p-3, first_bad_matrix_antidiagonal=s0,
                   bad_matrix_rank=r, all_regular_atom_span_rank=B.rank(),
                   augmented_span_rank=augmented.rank(),
                   frobenius_witness=dict(early=earlier, late=s0,
                        early_value=sequence[earlier], late_value=sequence[s0]),
                   obstruction=True)
        rows.append(row)
        print('n', n, 'p', p, 'bad rank', r, 'atom ranks', p, p+1, flush=True)
    return dict(n=n,K=K,N=N,m=m,h=h,w=w,degree=degree,rows=rows)


if __name__ == '__main__':
    data = dict(status='passed',
                scope='Regular p-integral finite nodes, atom weights with p*d integral; '
                      'no exclusion of singular nodes, derivative functionals, '
                      'or different rational corrections.',
                cases=[case(n) for n in (1,2,3)])
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
