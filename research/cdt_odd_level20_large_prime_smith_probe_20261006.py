"""Four preassigned large-prime coefficient maps, with capped Smith exponents.

This evaluates all coefficients in the stated square prefix, not the global
primitive leading flag.  It cannot prove a D-asymptotic gain or irrationality.
No frozen producer is imported or executed.  All arithmetic is exact.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(label, condition):
    assert condition, label
    CHECKS.append(label)


def capped_smith(matrix, p):
    modulus = p**3
    a = [row[:] for row in matrix]
    nr, nc = len(a), len(a[0])
    left = [[int(i == j) for j in range(nr)] for i in range(nr)]
    right = [[int(i == j) for j in range(nc)] for i in range(nc)]
    pivots = []
    def val(x):
        if x == 0: return 3
        if x % p: return 0
        return 1 if x % (p*p) else 2
    for k in range(min(nr, nc)):
        v, i, j = min((val(a[i][j]), i, j)
                      for i in range(k, nr) for j in range(k, nc))
        if v == 3: break
        a[k], a[i] = a[i], a[k]
        left[k], left[i] = left[i], left[k]
        for row in a: row[k], row[j] = row[j], row[k]
        for row in right: row[k], row[j] = row[j], row[k]
        power = p**v
        inverse = pow(a[k][k]//power, -1, modulus)
        a[k] = [(x*inverse) % modulus for x in a[k]]
        left[k] = [(x*inverse) % modulus for x in left[k]]
        assert a[k][k] == power
        for i in range(k+1, nr):
            factor = a[i][k]//power
            a[i] = [(x-factor*y) % modulus for x, y in zip(a[i], a[k])]
            left[i] = [(x-factor*y) % modulus for x, y in zip(left[i], left[k])]
        for j in range(k+1, nc):
            factor = a[k][j]//power
            for table in (a, right):
                for row in table:
                    row[j] = (row[j]-factor*row[k]) % modulus
        pivots.append(v)
    exponents = pivots + [3]*(nc-len(pivots))
    return exponents, {'left': left, 'right': right, 'diagonal': a}


def matrix_product(a, b, modulus):
    columns = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) % modulus
             for col in columns] for row in a]


def field_rank(matrix, p):
    """Independent field elimination, used only to certify unit transforms."""
    a = [[x % p for x in row] for row in matrix]
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][j], -1, p)
        a[rank] = [x*inverse % p for x in a[rank]]
        for i in range(rank+1, len(a)):
            factor = a[i][j]
            a[i] = [(x-factor*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def run(p, D, m, root):
    modulus = p**3
    size = m*(D+1)
    check(f'p{p}_m{m}_window', D < p < size < p*p)
    # Hensel lift a split residue root of 5 to Z/p^3Z.
    r = root
    for _ in range(3): r = (r-(r*r-5)*pow(2*r, -1, modulus)) % modulus
    check(f'p{p}_m{m}_split_root', (r*r-5) % modulus == 0)
    def pad(a, n=size): return list(a[:n])+[0]*max(0, n-len(a))
    def mul(a,b):
        out = [0]*len(a)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:len(a)-i]):
                    if y: out[i+j] = (out[i+j]+x*y) % modulus
        return out
    def inv(a):
        out = pad([pow(a[0],-1,modulus)],len(a))
        for n in range(1,len(a)):
            out[n] = -out[0]*sum(a[j]*out[n-j] for j in range(1,n+1)) % modulus
        return out
    def compose(a,b):
        out = [0]*len(b); power = pad([1],len(b))
        for i,c in enumerate(a[:len(b)]):
            if c:
                out = [(x+c*y) % modulus for x,y in zip(out,power)]
            if i+1 < len(b): power = mul(power,b)
        return out
    def derivative(a): return [i*a[i] % modulus for i in range(1,len(a))]+[0]
    def revert(a):
        b = [0,1]
        while len(b) < len(a):
            n = min(2*len(b)-1,len(a)); b = pad(b,n)
            error = compose(a[:n],b); error[1] = (error[1]-1) % modulus
            correction = mul(error,inv(compose(derivative(a)[:n],b)))
            b = [(x-y) % modulus for x,y in zip(b,correction)]
        return b
    def eta(exponents):
        out = pad([1])
        for d,e in zip([1,2,4,5,10,20],exponents):
            for n in range(d,size,d):
                factor = [0]*size
                for j in range((size-1)//n+1):
                    bc = comb(e,j) if e >= 0 and j <= e else (0 if e >= 0 else (-1)**j*comb(-e+j-1,j))
                    factor[j*n] = (-1)**j*bc % modulus
                out = mul(out,factor)
        return out
    def rational_mod(x):
        assert x.denominator % p
        return x.numerator*pow(x.denominator,-1,modulus) % modulus
    def chi(n): return (0,1,-1,-1,1)[n % 5]
    U = eta([-2,0,2,2,0,-2]); U[1] = (U[1]+1) % modulus
    tq = pad([0]+inv(U)); qt = revert(tq)
    check(f'p{p}_m{m}_coordinate_reversion', compose(tq,qt) == pad([0,1]))
    AE = pad([-pow(5,-1,modulus)]+[sum(chi(d)*d for d in range(1,n+1) if n%d == 0) for n in range(1,size)])
    AF = pad([0]+[-4*sum(chi((n//4)//d)*d for d in range(1,n//4+1) if (n//4)%d == 0) if n%4 == 0 else 0 for n in range(1,size)])
    EK = [0]+[sum(chi(d)*d**3 for d in range(1,n+1) if n%d == 0) for n in range(1,size)]
    FK = [0]+[sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d == 0) for n in range(1,size)]
    VE = [0]+[EK[n]-(5*EK[n//2] if n%2 == 0 else 0)+(4*EK[n//4] if n%4 == 0 else 0) for n in range(1,size)]
    VF = [0]+[-5*pow(4,-1,modulus)*(FK[n]-(20*FK[n//2] if n%2 == 0 else 0)+(64*FK[n//4] if n%4 == 0 else 0)) % modulus for n in range(1,size)]
    source = [0]*size
    for n in range(p,size,p):
        source[n] = (VE[n]+r*VF[n])*pow(n//p,-3,modulus) % modulus
    A = compose([(x+r*y) % modulus for x,y in zip(AE,AF)],qt)
    Y = mul(A,compose(source,qt))
    check(f'p{p}_m{m}_target_packet_first_order', not any(x % p for x in Y[:p]) and Y[p] % p != 0)
    Delta = pad([1,-12,28,-32,16]); g = mul(Delta,Delta)
    target = [mul(g,[(n**j*x) % modulus for n,x in enumerate(Y)]) for j in range(3)]
    if m == 4:
        k = 0
        functions = [pad([p**3 % modulus])]+target
    else:
        k = int(p <= D)+int(p <= 2*D)+int(p <= 4*D)
        source_L = int(p <= 2*D)+int(p <= 4*D)
        source_TK = int(p <= 4*D)
        pL = [0]+[rational_mod(F(p,n)) for n in range(1,size)]
        psi_L = [(p**(2-source_L)*x) % modulus for x in pL]
        psi_T = [(p**(1-source_TK)*pow(2,-1,modulus)*x) % modulus for x in mul(pL,pL)]
        kk = [F(0)]; cumulative_K = F(0); harmonic = F(0)
        for n in range(1,size):
            harmonic += F(1,n)
            kn = (cumulative_K/2+harmonic)/n
            kk.append(kn); cumulative_K += kn
        psi_K = [rational_mod(p**(3-source_TK)*x) for x in kk]
        functions = [pad([p**(3-k) % modulus]),psi_L,psi_T,psi_K]+target
    matrix = [[functions[j][n-i] if n >= i else 0 for j in range(m) for i in range(D+1)] for n in range(size)]
    exponents, witness = capped_smith(matrix,p)
    diagonal = [[p**exponents[i] % modulus if i == j else 0
                 for j in range(size)] for i in range(size)]
    product = matrix_product(matrix_product(witness['left'], matrix, modulus),
                             witness['right'], modulus)
    check(f'p{p}_m{m}_explicit_Smith_identity', product == diagonal == witness['diagonal'])
    check(f'p{p}_m{m}_left_transform_is_unit', field_rank(witness['left'],p) == size)
    check(f'p{p}_m{m}_right_transform_is_unit', field_rank(witness['right'],p) == size)
    check(f'p{p}_m{m}_modp_rank_matches_zero_exponents', field_rank(matrix,p) == exponents.count(0))
    cost = sum(3-v for v in exponents)
    baseline = k*min(p,size)+3*max(size-p,0)
    check(f'p{p}_m{m}_row_factor_baseline', cost <= baseline)
    terminal = p >= size-D
    if terminal: check(f'p{p}_m{m}_terminal_has_no_capped_gain', cost == baseline)
    return {'p':p,'D':D,'m':m,'split_root_modp':root,'prefix_exclusive':size,
            'square_coefficient_map_only':True,'terminal_window':terminal,
            'original_source_k_p':k,'capped_smith_exponent_counts':{str(i):exponents.count(i) for i in range(4)},
            'baseline_for_these_Taylor_rows':baseline,'capped_finite_cost':cost,
            'net_capped_gain_on_this_square_prefix':baseline-cost,
            'smith_witness_mod_p3':{'coefficient_matrix':matrix, **witness}}


if __name__ == '__main__':
    cases = [(11,5,4,4),(11,5,7,4),(19,4,4,9),(41,5,7,13)]
    samples = [run(*case) for case in cases]
    out = {'scope':'Four prescribed split-prime square Taylor maps. Not the global leading flag, not an asymptotic gain, not a period evaluation or irrationality proof.',
           'checks_passed':len(CHECKS),'check_labels':CHECKS,'samples':samples,
           'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(CHECKS),'samples':[
        {k:v for k,v in sample.items() if k != 'smith_witness_mod_p3'}
        for sample in samples]},ensure_ascii=False))
