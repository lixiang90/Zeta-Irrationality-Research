"""Fixed late-packet rank checks; does not rerun any frozen producer.

The cutoffs below are diagnostic finite cutoffs, not a claimed uniform
Shidlovsky constant or the complete actual primitive Taylor flag.
"""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'cdt_odd_level20_hasse_20261006_verify.json'
OUT = BASE / 'cdt_odd_level20_large_prime_net_20261006_verify.json'


class Field:
    def __init__(self, p, root):
        self.p, self.root = p, root
        self.zero = (0, 0)
        self.one = (1, 0)
        self.r = (0, 1) if root is None else (root, 0)

    def scalar(self, n):
        return (n % self.p, 0)

    def add(self, x, y):
        return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)

    def neg(self, x):
        return ((-x[0]) % self.p, (-x[1]) % self.p)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        return ((x[0]*y[0] + 5*x[1]*y[1]) % self.p,
                (x[0]*y[1] + x[1]*y[0]) % self.p)

    def inv(self, x):
        norm = (x[0]*x[0] - 5*x[1]*x[1]) % self.p
        assert norm != 0
        z = pow(norm, -1, self.p)
        return ((x[0]*z) % self.p, (-x[1]*z) % self.p)


def mul_series(f, a, b, n):
    out = [f.zero] * n
    for i, x in enumerate(a[:n]):
        for j, y in enumerate(b[:n-i]):
            out[i+j] = f.add(out[i+j], f.mul(x, y))
    return out


def inverse_series(f, a, n):
    out = [f.zero] * n
    out[0] = f.inv(a[0])
    for k in range(1, n):
        s = f.zero
        for j in range(1, min(k+1, len(a))):
            s = f.add(s, f.mul(a[j], out[k-j]))
        out[k] = f.neg(f.mul(out[0], s))
    return out


def log_derivative(f, a, n):
    derivative = [f.mul(f.scalar(i), a[i]) for i in range(1, len(a))]
    return mul_series(f, derivative, inverse_series(f, a, n), n)


def rank(f, rows):
    a = [r[:] for r in rows]
    nr, nc, k = len(a), len(a[0]), 0
    for j in range(nc):
        pivot = next((i for i in range(k, nr) if a[i][j] != f.zero), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        z = f.inv(a[k][j])
        a[k] = [f.mul(x, z) for x in a[k]]
        for i in range(k+1, nr):
            if a[i][j] != f.zero:
                z = a[i][j]
                a[i] = [f.sub(x, f.mul(z, y)) for x, y in zip(a[i], a[k])]
        k += 1
        if k == nr:
            break
    return k


def main():
    cert = json.loads(SOURCE.read_text(encoding='utf-8'))
    fixed = {x['prime']: x['hasse_polynomial'] for x in cert['fixed_samples']}
    results = []
    for p, degree, root in [(7, 3, None), (11, 5, 4), (11, 5, 7), (13, 6, None)]:
        f = Field(p, root)
        cutoff = 4*(degree+1)
        ell = cutoff-p
        assert degree < p and cutoff < p*p
        n_poly = [f.one, f.neg(f.add(f.scalar(6), f.r)), f.add(f.one, f.r)]
        c_poly = [f.one, f.neg(f.sub(f.scalar(6), f.mul(f.scalar(2), f.r))),
                  f.sub(f.scalar(6), f.mul(f.scalar(2), f.r))]
        p_poly = [f.scalar(x) for x in fixed[p]]
        terms = [log_derivative(f, n_poly, ell),
                 [f.mul(f.inv(f.scalar(2)), x) for x in log_derivative(f, c_poly, ell)],
                 log_derivative(f, p_poly, ell)]
        plain = [f.add(f.add(terms[0][i], terms[1][i]), terms[2][i]) for i in range(ell)]
        a = [f.zero] + plain[:-1]
        square = mul_series(f, a, a, ell)
        b = [f.add(f.mul(f.scalar(i), a[i]), square[i]) for i in range(ell)]
        assert a[0] == b[0] == f.zero
        assert a[1] == b[1] == f.scalar(-5)
        assert f.sub(b[2], a[2]) == f.scalar(-20)
        functions = [[f.one] + [f.zero]*(ell-1), a, b]
        rows = []
        for i in range(ell):
            rows.append([g[i-j] if 0 <= i-j < ell else f.zero
                         for g in functions for j in range(degree+1)])
        actual_rank = rank(f, rows)
        assert actual_rank == ell
        results.append({'prime': p, 'degree': degree, 'residue_root': root,
                        'diagnostic_cutoff': cutoff, 'late_length': ell,
                        'columns': 3*(degree+1), 'exact_rank': actual_rank,
                        'late_defect': ell-actual_rank})
    out = {'status': 'fixed_late_packet_rank_checks_passed',
           'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'fixed_results': results,
           'scope': 'Exact ranks of four preselected target late-packet matrices. '
                    'No prime scan, no complete primitive Taylor flag, no all-prime '
                    'normality theorem, no positive net Smith gain, no numerical theorem.'}
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False))


if __name__ == '__main__':
    main()
