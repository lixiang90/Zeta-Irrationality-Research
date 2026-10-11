"""NEW first-only finite mechanism certificate for the all-prime CRT paper.

No old/peer mathematical program or certificate is read, imported or run.
The paper proves CRT, all-scale packet and capacity statements. This checks
finite exact basis identities and independently compares original and orbit
DVR invariants, including small primes with higher factorial layers.
"""
from pathlib import Path
from fractions import Fraction
import math
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise RuntimeError('First execution only: preserve existing output; no rerun.')


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p)+1))


def vp(x, p):
    x = Fraction(x)
    assert x
    def integer_v(a):
        a = abs(a)
        v = 0
        while a % p == 0:
            a //= p
            v += 1
        return v
    return integer_v(x.numerator)-integer_v(x.denominator)


def rank_mod(rows, p):
    if not rows:
        return 0
    a = [[x % p for x in row] for row in rows]
    rank = 0
    for c in range(len(a[0])):
        hit = next((i for i in range(rank,len(a)) if a[i][c]),None)
        if hit is None:
            continue
        a[rank],a[hit] = a[hit],a[rank]
        inv = pow(a[rank][c],-1,p)
        a[rank] = [x*inv % p for x in a[rank]]
        for i in range(rank+1,len(a)):
            fac = a[i][c]
            if fac:
                a[i] = [(x-fac*y) % p for x,y in zip(a[i],a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def dvr_invariants(rows,p):
    if not rows:
        return []
    a = [[Fraction(x) for x in row] for row in rows]
    m,width = len(a),len(a[0])
    result = []
    for stage in range(m):
        choices = [(vp(a[i][j],p),i,j)
                   for i in range(stage,m) for j in range(stage,width)
                   if a[i][j]]
        assert choices, 'Actual block must have full row rank'
        order,i,j = min(choices)
        a[stage],a[i] = a[i],a[stage]
        for row in a:
            row[stage],row[j] = row[j],row[stage]
        pivot = a[stage][stage]
        for i in range(stage+1,m):
            fac = a[i][stage]/pivot
            if fac:
                assert vp(fac,p) >= 0
                for j in range(stage+1,width):
                    a[i][j] -= fac*a[stage][j]
            a[i][stage] = Fraction(0)
        # Clearing the remaining pivot row uses column operations with
        # coefficients in Z_p and leaves the lower-right block unchanged.
        for j in range(stage+1,width):
            fac = a[stage][j]/pivot
            if fac:
                assert vp(fac,p) >= 0
            a[stage][j] = Fraction(0)
        result.append(order)
    assert result == sorted(result) and all(v >= 0 for v in result)
    return result


def determinant(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    value = Fraction(1)
    for c in range(len(a)):
        hit = next((i for i in range(c,len(a)) if a[i][c]),None)
        assert hit is not None
        if hit != c:
            a[c],a[hit] = a[hit],a[c]
            value = -value
        pivot = a[c][c]
        value *= pivot
        for i in range(c+1,len(a)):
            fac = a[i][c]/pivot
            for j in range(c+1,len(a)):
                a[i][j] -= fac*a[c][j]
            a[i][c] = Fraction(0)
    return value


cases = []
identity_checks = 0
capacity_cases = 0
for n in range(1,13):
    M = 2*n
    fac = [math.factorial(i) for i in range(8*n+1)]
    ds = [fac[6*n+k+1]//fac[k] for k in range(M)]
    pairs = []
    original = []
    for k in range(n):
        kp = M-1-k
        divisor = math.gcd(ds[k],ds[kp])
        pp,qq = ds[k]//divisor,ds[kp]//divisor
        pairs.append((k,kp,pp,qq))
        original.append([qq*(fac[k]//fac[k-j] if j <= k else 0)
                         -pp*(fac[kp]//fac[kp-j] if j <= kp else 0)
                         for j in range(M)])
    for p in range(2,M+1):
        if not is_prime(p):
            continue
        lengths = {r:len(range(r,M,p)) for r in range(min(p,M))}
        columns = [(r,j) for r,L in lengths.items() for j in range(L)]
        W = [[p**j*fac[j]*math.comb((k-r)//p,j)
              if k % p == r and (k-r)//p >= j else 0
              for r,j in columns] for k in range(M)]
        U = [[sum(Fraction((-1)**(j-k)*math.comb(j,k)*W[k][c],fac[j])
                  for k in range(j+1))
              for c in range(M)] for j in range(M)]
        assert all(not x or vp(x,p) >= 0 for row in U for x in row)
        assert vp(determinant(U),p) == 0
        K = [[qq*W[k][c]-pp*W[kp][c] for c in range(M)]
             for k,kp,pp,qq in pairs]
        for i in range(n):
            for c in range(M):
                assert sum(original[i][j]*U[j][c] for j in range(M)) == K[i][c]
                identity_checks += 1
        alpha = dvr_invariants(original,p)
        orbitalpha = []
        orbitrecords = []
        visited = set()
        baseline_sum = 0
        extra = 0
        h,e = divmod(6*n+1,p)
        threshold = p-e
        for r,L in lengths.items():
            if r in visited:
                continue
            s = (M-1-r) % p
            assert s in lengths and lengths[s] == L
            residues = {r,s}
            visited.update(residues)
            row_ids = [i for i,(k,kp,pp,qq) in enumerate(pairs) if k % p in residues]
            col_ids = [c for c,(t,j) in enumerate(columns) if t in residues]
            block = [[K[i][c] for c in col_ids] for i in row_ids]
            assert len(row_ids) == (L if r != s else L//2)
            assert r != s or L % 2 == 0
            beta = dvr_invariants(block,p)
            orbitalpha += beta
            weights = sorted(j+vp(fac[j],p) for t,j in columns if t in residues)
            base = sum(weights[:len(row_ids)])
            baseline_sum += base
            mixed = r != s and (r >= threshold) != (s >= threshold)
            credit = L//2 if mixed and p*p > 8*n else 0
            extra += credit
            assert sum(beta) >= base+credit
            orbitrecords.append({'residues':sorted(residues),'length':L,
                                 'rows':len(row_ids),'Smith_valuations':beta,
                                 'cheapest_column_baseline':base,
                                 'mixed_carry':mixed,'proved_capacity_credit':credit})
        assert sorted(orbitalpha) == alpha
        baseline = sum(vp(fac[i],p) for i in range(n))
        assert baseline_sum == baseline
        if p*p > 8*n:
            a,b = divmod(M,p)
            inner = max(0,min(threshold,b-threshold))
            outer = max(0,min(threshold-b,p-threshold))
            assert extra == ((a+1)//2)*inner+(a//2)*outer
            assert sum(alpha) >= baseline+extra
            capacity_cases += 1
        cases.append({'n':n,'p':p,'actual_Smith_valuations':alpha,
                      'delta_actual':sum(alpha),'baseline_delta':baseline,
                      'capacity_extra':extra,'basis_p_integral_and_GL':True,
                      'orbit_Smith_union_exact':True,'orbits':orbitrecords})

record = {
    'status':'finite-exact-residue-CRT-mechanism-pass',
    'scope':'n1..12, every prime p<=2n. Exact local GL basis, actual weighted matrix identity and independent original/orbit DVR invariants, including small-prime high factorial layers. Capacity formula checked only when p2>8n. Finite mechanism, not an all-scale or infinite-unit proof.',
    'execution_count':1,'old_or_peer_execution_import_rerun_count':0,
    'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'case_count':len(cases),'capacity_case_count':capacity_cases,
    'exact_matrix_identity_entry_checks':identity_checks,
    'cases':cases,
    'not_proved_by_code':['All-n CRT proof','Every prime-window closed Smith formula',
                          'Paid all-prime n2 gain','Infinite target units or nonzero',
                          'Strict margin','Numerical irrationality','Lean']
}
OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:record[k] for k in ('status','case_count','capacity_case_count',
                                      'exact_matrix_identity_entry_checks')},ensure_ascii=False))
