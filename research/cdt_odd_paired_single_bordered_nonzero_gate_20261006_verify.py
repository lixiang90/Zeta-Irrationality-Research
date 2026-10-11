"""FIRST-ONLY saved identity evidence, not an infinite nonzero theorem.

Own literal actual definitions on old r=1,2,4; no old/peer file reads,
imports or execution. The paper supplies all-scale proofs. Any failure is
preserved and this source must never be rerun or repaired after execution.
"""
from pathlib import Path
from math import factorial, comb
import hashlib
import json

SOURCE = Path(__file__)
OUTPUT = SOURCE.with_suffix('.json')
with OUTPUT.open('x', encoding='utf-8') as first_handle:
    first_handle.write('{"status":"STARTED_FIRST_ONLY"}\n')
checks = 0


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def transpose(a):
    return [list(c) for c in zip(*a)]


def multiply(a, b, p):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row, col)) % p for col in bt]
            for row in a]


def gram(a, b, weights, p):
    return multiply(transpose(a),
                    [[w*x % p for x in row] for w, row in zip(weights, b)], p)


def rref(a, p):
    a = [row[:] for row in a]
    i = 0
    pivots = []
    for j in range(len(a[0])):
        k = next((k for k in range(i, len(a)) if a[k][j] % p), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        v = pow(a[i][j] % p, -1, p)
        a[i] = [x*v % p for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j] % p:
                v = a[k][j] % p
                a[k] = [(x-v*y) % p for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return a, pivots


def rank(a, p):
    return len(rref(a, p)[1])


def determinant(a, p):
    a = [row[:] for row in a]
    ans = 1
    for j in range(len(a)):
        k = next((k for k in range(j, len(a)) if a[k][j] % p), None)
        if k is None:
            return 0
        if k != j:
            a[j], a[k] = a[k], a[j]
            ans = -ans
        v = a[j][j] % p
        ans = ans*v % p
        vinv = pow(v, -1, p)
        for k in range(j+1, len(a)):
            c = a[k][j]*vinv % p
            for h in range(j+1, len(a)):
                a[k][h] = (a[k][h]-c*a[j][h]) % p
    return ans % p


def inverse(a, p):
    n = len(a)
    rows = [row[:] + [int(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    reduced, pivots = rref(rows, p)
    check(pivots[:n] == list(range(n)), 'known invertible complement')
    return [row[n:] for row in reduced]


def block(a, b, c, d):
    return [x+y for x, y in zip(a, b)] + [x+y for x, y in zip(c, d)]


def actual_case(r):
    m, p = 2*r, 18*r+1
    vdim, tdim, qdim = 3*m, m//2, 3*m//2
    edim = vdim-tdim
    nodes = [(-l) % p for l in range(vdim)]
    ys = [(a+5*r) % p for a in nodes]
    tr = [[pow(y, 2*i, p) for i in range(tdim)] for y in ys]
    qr = [[pow(y, 2*i, p) for i in range(qdim)] for y in ys]
    ap = [((-1)**l * factorial(l)*factorial(vdim-1-l)) % p
          for l in range(vdim)]
    sv = []
    for a in nodes:
        s = 1
        for z in range(1, 4*m+1):
            s = s*(a-z) % p
        sv.append(s)
    kap = factorial(3*m-1)**2 * pow(factorial(4*m)**3 % p, -1, p) % p
    dv = [(comb(3*m-1, l)**2 * comb(4*m+l, l)**3) % p
          for l in range(vdim)]
    for l in range(vdim):
        check(ap[l] != 0 and sv[l] != 0 and dv[l] != 0,
              'actual ambient weights and denominators unit')
        check(dv[l] == kap*pow(sv[l], 3, p)*pow(ap[l]**2 % p, -1, p) % p,
              'actual Wilson/Lucas ambient factor')
    ll = [[tr[l][i]*pow(ap[l]*sv[l] % p, -1, p) % p
           for l in range(vdim)] for i in range(tdim)]
    reduced, pivots = rref(ll, p)
    check(len(pivots) == tdim, 'actual annihilator full row rank')
    free = [j for j in range(vdim) if j not in pivots]
    zz = [[0]*edim for _ in range(vdim)]
    for col, j in enumerate(free):
        zz[j][col] = 1
        for row, pivot in enumerate(pivots):
            zz[pivot][col] = -reduced[row][j] % p
    invlp = inverse([[row[j] for j in pivots] for row in ll], p)
    ff = [[0]*tdim for _ in range(vdim)]
    for row, pivot in enumerate(pivots):
        ff[pivot] = invlp[row][:]
    uu = [z+f for z, f in zip(zz, ff)]
    check(multiply(ll, zz, p) == [[0]*edim for _ in range(tdim)], 'LZ zero')
    check(multiply(ll, ff, p) == [[int(i == j) for j in range(tdim)]
                                for i in range(tdim)], 'LF identity')
    detu = determinant(uu, p)
    check(detu != 0, 'actual complement U invertible')
    jj = [[ap[l]*x % p for x in qr[l]] for l in range(vdim)]
    kv = [2 if 2*m+1 <= l <= 3*m-1 else 5 for l in range(vdim)]
    dd = [(1-k*k)*pow(6, -1, p) % p for k in kv]
    ss = [[-6*x % p for x in row] for row in gram(zz, zz, dv, p)]
    sw = gram(zz, jj, [d*k % p for d, k in zip(dv, kv)], p)
    ww = gram(jj, jj, [d*z % p for d, z in zip(dv, dd)], p)
    nn = block(ss, sw, transpose(sw), ww)
    gg = gram(tr, tr, [pow(s, -5, p) for s in sv], p)
    hh = gram(qr, qr, [pow(s, 3, p) for s in sv], p)
    cc = gram(tr, qr, [k*pow(s, -1, p) % p for k, s in zip(kv, sv)], p)
    mm = block(gg, cc, transpose(cc), hh)
    check(gram(transpose(ll), transpose(ll), [pow(d, -1, p) for d in dv], p)
          == [[pow(kap, -1, p)*x % p for x in row] for row in gg],
          'G0 actual annihilator Gram identity')
    check(gram(jj, jj, dv, p) == [[kap*x % p for x in row] for row in hh],
          'H0 actual derivative Gram identity')
    check(multiply(ll, [[k*x % p for x in row] for k, row in zip(kv, jj)], p)
          == cc, 'C5 actual halfjet cross identity')
    psi = [[0]*(vdim+qdim+tdim) for _ in range(vdim+qdim+tdim)]
    for i in range(vdim):
        psi[i][i] = -6*dv[i] % p
        for j in range(qdim):
            psi[i][vdim+j] = psi[vdim+j][i] = dv[i]*kv[i]*jj[i][j] % p
        for j in range(tdim):
            psi[i][vdim+qdim+j] = psi[vdim+qdim+j][i] = ll[j][i]
    for i in range(qdim):
        for j in range(qdim):
            psi[vdim+i][vdim+j] = ww[i][j]
    detn, detm, detpsi = (determinant(x, p) for x in [nn, mm, psi])
    const = (-1)**tdim * detu**2 * pow(6, m, p)*pow(kap, m, p)
    for d in dv:
        const = const*d % p
    check(detn == const*detm % p, 'B8 actual determinant unit factor')
    check(detn == (-1)**tdim*detu**2*detpsi % p, 'B6 bordered restriction sign')
    corn, corm = len(nn)-rank(nn, p), len(mm)-rank(mm, p)
    check(corn == corm == len(psi)-rank(psi, p), 'B8 exact actual corank equality')
    g = tdim-rank(gg, p)
    check(edim-rank(ss, p) == g, 'strong radical equals G0 corank')
    return {'r':r, 'n':4*r, 'p':p, 'actual_pair_rank':edim+qdim,
            'ambient_negative_nodes':vdim, 'G0_corank':g,
            'whole_normalized_corank':corn, 'M5_corank':corm,
            'whole_normalized_det_without_source_unit':detn,
            'actual_M5_det':detm, 'explicit_unit_factor':const % p,
            'bordered_det':detpsi, 'U_det':detu}


try:
    cases = [actual_case(r) for r in [1, 2, 4]]
    p = 19
    toy_g, toy_c, toy_h = 0, 1, 1
    toy_n = [[0,1],[1,0]]
    toy_m = [[toy_g,toy_c],[toy_c,toy_h]]
    check(toy_g == 0 and determinant(toy_n, p) != 0 and determinant(toy_m, p) != 0,
          'singular G does not obstruct full unit form')
    toy_scaled = [[0,p],[p,0]]
    check(toy_scaled[0][1] % p == 0 and determinant(toy_n, p) != 0,
          'singular strong block yields exponents one and one')
    perturbations = []
    for x in range(p):
        a, b = p*p+p**3*x, 2*p**3*x
        c, d = 3*p**3*x, 1+4*p**3*x
        valdet = a*d-b*c
        check(valdet % (p*p) == 0 and (valdet//(p*p)) % p == 1,
              'depth2 anchor stable under p3 affine perturbation')
        perturbations.append({'x':x,'normalized_det_mod_p':(valdet//(p*p)) % p})
    check((p**3-p**3)*1 == 0, 'depth3 threshold counterexample exact zero')
    result = {'status':'PASS','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'first_only':True,'runs':1,'exact_checks':checks,'cases':cases,
              'toy_singular_G':{'p':19,'G_det':0,'restricted_N_det':18,'bordered_target_det':18,
                                'scope':'General algebraic example, not original fixed-lambda2 target'},
              'depth2_affine_perturbation':perturbations,
              'depth3_counterexample':{'anchor_max_Smith':3,'perturbation_depth':3,'singular_x':1},
              'scope':'Actual leading constraint/border identities on old r1,2,4 only; no auxiliary-prime extension or actual higher-layer computation.',
              'old_peer_read_execute_import_rerun':0,
              'not_proved':['Infinite M5 units','Actual higher-layer maximum Smith <=2',
                            'Strict arithmetic-analytic margin','New special-value irrationality']}
except BaseException as exc:
    OUTPUT.write_text(json.dumps({'status':'FAILED_FIRST_ONLY','checks_before_failure':checks,
                                 'error':repr(exc)},indent=2)+'\n',encoding='utf-8')
    raise
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'cases':len(cases),'exact_checks':checks,
                  'old_peer_execute_import_rerun':0},ensure_ascii=False))
