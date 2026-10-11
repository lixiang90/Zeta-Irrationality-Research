"""NEW finite evidence for an independently proved dual Plucker formula.

First execution only. Reads no previous or peer mathematical files.
Not an infinite-prime rank theorem or an irrationality proof.
"""
from fractions import Fraction
from math import comb, factorial, gcd, isqrt
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise SystemExit('Refusing rerun: finite output already exists')


def primes_upto(limit):
    return [p for p in range(2, limit + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def vp(x, prime):
    x = Fraction(x)
    if not x:
        return None
    a, b = abs(x.numerator), x.denominator
    val = 0
    while a % prime == 0:
        val += 1
        a //= prime
    while b % prime == 0:
        val -= 1
        b //= prime
    return val


def maximal_minor_valuation(matrix, prime):
    """DVR elimination: minimum-entry pivots, unit row/column clears.

    Rectangular full-row-rank matrix over Q; also works for its transpose.
    Pivot valuations sum to the valuation of the maximal determinantal ideal.
    """
    arr = [[Fraction(x) for x in row] for row in matrix]
    row_count, col_count = len(arr), len(arr[0])
    pivots = []
    for k in range(row_count):
        choices = [(vp(arr[i][j], prime), i, j)
                   for i in range(k, row_count)
                   for j in range(k, col_count) if arr[i][j]]
        if not choices:
            raise AssertionError('Matrix lost full row rank over Q')
        val, pi, pj = min(choices)
        arr[k], arr[pi] = arr[pi], arr[k]
        for row in arr:
            row[k], row[pj] = row[pj], row[k]
        pivot = arr[k][k]
        pivots.append(val)
        for i in range(k + 1, row_count):
            mult = arr[i][k] / pivot
            if mult:
                assert vp(mult, prime) >= 0
                for j in range(k + 1, col_count):
                    arr[i][j] -= mult * arr[k][j]
            arr[i][k] = Fraction(0)
        for j in range(k + 1, col_count):
            if arr[k][j]:
                assert vp(arr[k][j] / pivot, prime) >= 0
    assert pivots == sorted(pivots)
    return sum(pivots), pivots


def rank_mod(matrix, prime):
    arr = [[int(x) % prime for x in row] for row in matrix]
    pos = 0
    for col in range(len(arr[0])):
        pi = next((i for i in range(pos, len(arr)) if arr[i][col]), None)
        if pi is None:
            continue
        arr[pos], arr[pi] = arr[pi], arr[pos]
        inv = pow(arr[pos][col], -1, prime)
        arr[pos] = [(x * inv) % prime for x in arr[pos]]
        for i in range(pos + 1, len(arr)):
            mult = arr[i][col]
            if mult:
                arr[i] = [(x - mult*y) % prime
                          for x, y in zip(arr[i], arr[pos])]
        pos += 1
        if pos == len(arr):
            break
    return pos


def falling(a, j):
    return factorial(a) // factorial(a-j) if j <= a else 0


cases = []
for n in range(1, 19):
    size = 2*n
    pairs = []
    dual = []
    primal_transpose = []
    for m in range(1, n+1):
        mirror = size+1-m
        b1, b2 = comb(6*n+m, m-1), comb(6*n+mirror, mirror-1)
        beta = gcd(b1, b2)
        pc, qc = b1//beta, b2//beta
        assert gcd(pc, qc) == 1
        pairs.append((m, mirror, pc, qc))
        dual.append([qc*falling(m-1,j)-pc*falling(mirror-1,j)
                     for j in range(size)])
        coeffs = []
        for j in range(size):
            v1 = (-1)**(j-m+1)*comb(j,m-1) if j >= m-1 else 0
            v2 = (-1)**(j-mirror+1)*comb(j,mirror-1) if j >= mirror-1 else 0
            coeffs.append(Fraction(pc*v1+qc*v2, factorial(j)))
        primal_transpose.append(coeffs)
    for prime in primes_upto(3*n):
        if prime*prime <= 8*n:
            continue
        delta, dual_layers = maximal_minor_valuation(dual, prime)
        primal_min, primal_layers = maximal_minor_valuation(primal_transpose, prime)
        total_low = sum(vp(factorial(j),prime) for j in range(size))
        high = sum(vp(factorial(j),prime) for j in range(size,3*n))
        exact_T = high+total_low-delta
        assert exact_T == high-primal_min
        graph = []
        for m,mirror,pc,qc in pairs:
            row = [0]*prime
            row[(m-1)%prime] += qc
            row[(mirror-1)%prime] -= pc
            graph.append(row)
        modrank = rank_mod(dual,prime)
        graph_rank = rank_mod(graph,prime)
        assert modrank == graph_rank
        assert sum(v == 0 for v in dual_layers) == modrank
        safe_T = sum(vp(factorial(j),prime) for j in range(n,3*n))
        assert high+sum(vp(factorial(j),prime) for j in range(n)) <= exact_T <= safe_T
        cases.append({'n':n,'p':prime,'delta_dual':delta,
                      'dual_Smith_valuations':dual_layers,
                      'dual_rank_modp':modrank,'graph_rank_modp':graph_rank,
                      'primal_minimal_wedge_valuation':primal_min,
                      'primal_Smith_valuations':primal_layers,
                      'T_exact':exact_T,'T_safe':safe_T,
                      'two_sided_factorial_fee_gain':2*(safe_T-exact_T)})

data = {'status':'finite-exact-dual-plucker-probe-only',
        'scope':'n1..18, every prime sqrt(8n)<p<=3n. Exact DVR elimination of dual and primal wedges plus residue graph rank. Does not prove all-n rank layers, a limiting rate, form Smith improvement or irrationality.',
        'execution_count':1,'old_or_peer_execution_import_rerun_count':0,
        'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'case_count':len(cases),'cases':cases}
OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':data['status'],'cases':len(cases),
                  'max_n':18,'output':OUT.name},ensure_ascii=False))
