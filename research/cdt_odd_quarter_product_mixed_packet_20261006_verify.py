"""NEW finite checks for complementary-quarter mixed packets.

No old or peer producer is imported or executed.  These finite checks do not
prove the all-prime theorem or the actual rank of the 19-row model.
"""
from fractions import Fraction as F
from math import lcm
from pathlib import Path
from datetime import datetime, timezone
import json

OUT = Path(__file__).with_suffix('.json')
assert not OUT.exists(), 'Preserve prior execution record; do not overwrite it.'


def add(a, b, scale=F(1)):
    out = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += scale * v
    return out


def theta(a, order=1):
    return [v * (i ** order) for i, v in enumerate(a)]


def conv(a, b, n=None, modulus=None):
    size = len(a) + len(b) - 1
    if n is not None: size = min(size, n + 1)
    out = [0 if modulus else F(0)] * size
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            if i + j < size: out[i+j] += u*v
    if modulus: out = [v % modulus for v in out]
    return out


def residue(v, p, power):
    q = p ** power
    assert v.denominator % p != 0, (p, v)
    return (v.numerator * pow(v.denominator, -1, q)) % q


def residues(a, p, power, n=None):
    out = [residue(v, p, power) for v in a]
    if n is not None: out += [0] * (n + 1 - len(out))
    return out


def sum_mod(terms, n, q):
    out = [0] * (n+1)
    for a in terms:
        for i, v in enumerate(a):
            if i <= n: out[i] = (out[i]+v) % q
    return out


def coefficients(n, quarter):
    a = [F(1)]
    for k in range(n):
        a.append(a[-1] * (F(4*k+quarter, 4*k+quarter+2) ** 4))
    return a


def poly_apply(v, rows, p, power, n):
    q = p ** power
    terms = []
    for a, row in zip(v, rows):
        terms.append(conv(residues(a, p, power), residues(row, p, power), n, q))
    return sum_mod(terms, n, q)


def sym_apply(u, v, sym, p, power, n):
    q = p ** power
    terms = []
    for i in range(4):
        for j in range(4):
            coef = conv(residues(u[i], p, power), residues(v[j], p, power), n, q)
            terms.append(conv(coef, residues(sym[min(i,j), max(i,j)], p, power), n, q))
    return sum_mod(terms, n, q)


checks = []


def check(label, truth, **data):
    assert truth, label
    checks.append({'label': label, 'passed': True, **data})


samples = [(5,5), (13,40), (17,70), (3,1), (7,11), (11,29), (19,89)]
for p, n in samples:
    assert p*p > 4*n+1
    split = p % 4 == 1
    d = (p-1)//2
    h = (p-1)//4 if split else (p+1)//4
    A = coefficients(n, 1)
    J = coefficients(n, 3)
    F0 = A.copy(); F0[0] -= F(1,2)
    Frows = [[v*(F(k)-F(1,4))**i for k,v in enumerate(F0)] for i in range(4)]
    Jrows = [[v*(F(k)+F(1,4))**i for k,v in enumerate(J)] for i in range(4)]
    bad = Jrows if split else Frows
    good = Frows if split else Jrows
    U = [[(p**4)*v for v in row] for row in bad]
    check(f'whole_prefix_integrality_p{p}', all(v.denominator % p for row in U+good for v in row), N=n)

    T = [F(1)]; V = [F(0)]
    harmonic = F(0)
    for j in range(1,d+1):
        T.append(T[-1]*(F(2*j-1,2*j)**4))
        harmonic += 4*(F(2,2*j-1)-F(1,j))
        V.append(T[-1]*harmonic)
    e = [theta(T,i) for i in range(4)]
    dv = [V]
    for i in range(1,4): dv.append(add(theta(V,i), theta(T,i-1), F(i)))
    QQ = add(conv(T,dv[1]), conv(e[1],V), F(-1))
    check(f'fast_top_units_p{p}', residue(T[-1],p,1)!=0 and residue(QQ[-1]-T[-1]**2,p,1)==0 and residue(QQ[-1],p,1)!=0)

    seed = J if split else A
    W = [(p**4)*seed[h+k*p] for k in range((n-h)//p+1)] if h <= n else []
    packet_ok = True
    for i in range(4):
        expected = [F(0)]*(n+1)
        for k,w in enumerate(W):
            for j in range(d+1):
                idx = h+k*p+j
                if idx <= n:
                    expected[idx] += e[i][j]*w+p*dv[i][j]*(F(k)+F(1,4))*w
        packet_ok &= residues(U[i],p,2)==residues(expected,p,2)
    check(f'shifted_four_row_packet_p{p}', packet_ok, N=n, blocks=len(W))

    m = []
    for i in range(1,4):
        row = [[F(0)] for _ in range(4)]
        row[0] = [-v for v in e[i]]; row[i] = T
        m.append(row)
    r = []
    annihilator_ok = True
    for i in (2,3):
        C = add(conv(e[i],dv[1]), conv(dv[i],e[1]), F(-1))
        DD = add(conv(T,dv[i]), conv(V,e[i]), F(-1))
        row = [[F(0)] for _ in range(4)]
        row[0] = [-v for v in C]; row[1] = [-v for v in DD]; row[i] = QQ
        r.append(row)
        for fast in (e,dv):
            z = [F(0)]
            for k in range(4): z = add(z,conv(row[k],fast[k]))
            annihilator_ok &= all(v==0 for v in z)
    check(f'exact_second_annihilators_p{p}',annihilator_ok)
    check(f'pure_first_and_second_relations_p{p}', all(not any(poly_apply(row,U,p,1,n)) for row in m) and all(not any(poly_apply(row,U,p,2,n)) for row in r))

    sym = {}
    for i in range(4):
        for j in range(i,4):
            sym[i,j] = [v/2 for v in add(conv(good[i],U[j],n),conv(good[j],U[i],n))]
    check(f'six_mixed_first_relations_p{p}', all(not any(sym_apply(m[i],m[j],sym,p,1,n)) for i in range(3) for j in range(i,3)))
    check(f'three_mixed_second_relations_p{p}', all(not any(sym_apply(r[i],r[j],sym,p,2,n)) for i in range(2) for j in range(i,2)))

A = coefficients(64,1); J = coefficients(64,3)
DA = DJ = 1
all_denominators = True
for n in range(65):
    DA = lcm(DA,A[n].denominator); DJ = lcm(DJ,J[n].denominator)
    L = lcm(*range(1,4*n+2))
    while L % 2 == 0: L //= 2
    all_denominators &= DA*DJ==L**4
check('exact_denominator_product_N0_to64',all_denominators,N_max=64)
check('gamma_and_rank5_cost', F(1,2)*(3*F(2,2)+2*F(1,2))==2 and F(192,25)-F(4,25)==F(188,25))
check('conditional_mixed_gamma_and_cost',F(3)+F(3)+F(1)+F(3,4)==F(31,4) and F(5376,361)-F(31,722)==F(10721,722))

report = {
  'created_utc': datetime.now(timezone.utc).isoformat(),
  'execution_history': [{'attempt':1,'outcome':'passed','producer':'NEW; standard library only; no old or peer mathematical imports'}],
  'samples': [{'p':p,'N':n} for p,n in samples],
  'checks': checks,
  'check_count':len(checks),
  'passed':True,
  'scope': 'Finite actual coefficient packets, polynomial identities and denominator product. All-prime proof remains in the NEW Markdown; actual rank19 is not verified.',
  'numeric_irrationality_theorem':False,
  'lean_formalization':False
}
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'check_count':len(checks),'output':str(OUT)},ensure_ascii=False))
