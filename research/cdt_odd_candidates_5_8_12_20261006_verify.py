"""Fixed exact checks for three quadratic L3 candidates; no prime/parameter scan.

Only this new local certificate is executed, never any downloaded code.
The finite checks accompany the global lattice, eta-divisor and genus proofs
in cdt_odd_candidates_5_8_12_20261006.md; they do not prove irrationality.
"""
from pathlib import Path
import hashlib
import json
import math
import sympy as sp
import fitz

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix('.json')
checks = []

def check(label, condition):
    if not condition:
        raise AssertionError(label)
    checks.append(label)

def dedekind(a, c):
    if c == 1:
        return sp.Rational(0)
    return sum((sp.Rational(n, c)-sp.Rational(1, 2))
               * (sp.Rational((a*n) % c, c)-sp.Rational(1, 2))
               for n in range(1, c))

def eta_order(level, exponents, c):
    return sp.Rational(level, 24*math.gcd(c*c, level))*sum(
        sp.Rational(r*math.gcd(c, d)**2, d) for d, r in exponents.items())

def eta_constant(exponents, a, c):
    # From eta(M z)=eps(M)(c'z+d')^(1/2)eta(z), after cancellation
    # of the common y factors and of the exponential cusp order.
    phase = sp.Rational(a, 12*c)*sum(d*r for d, r in exponents.items())
    modulus_squared = sp.Rational(1)
    for d, r in exponents.items():
        g = math.gcd(c, d)
        ap, cp = d*a//g, c//g
        dp = 0 if cp == 1 else pow(ap, -1, cp)
        phase -= r*dedekind(dp, cp)
        modulus_squared *= sp.Rational(d, g)**(-r)
    return sp.simplify(phase), sp.simplify(modulus_squared)

def genus0(level):
    mu = level*sp.prod(sp.Rational(p+1, p) for p in sp.factorint(level))
    cusps = sum(sp.totient(math.gcd(d, level//d)) for d in sp.divisors(level))
    e2 = sum((x*x+1) % level == 0 for x in range(level))
    e3 = sum((x*x+x+1) % level == 0 for x in range(level))
    return sp.simplify(1+mu/12-sp.Rational(e2, 4)-sp.Rational(e3, 3)-cusps/2), int(cusps), int(mu)

rows = []
expected = {5: (sp.Rational(-2, 5), 2), 8: (-1, 11), 12: (-2, 46)}
for D in (5, 8, 12):
    char = [sp.kronecker_symbol(D, a) for a in range(1, D+1)]
    B2 = D*sum(char[a-1]*sp.bernoulli(2, sp.Rational(a, D)) for a in range(1, D+1))
    B4 = D**3*sum(char[a-1]*sp.bernoulli(4, sp.Rational(a, D)) for a in range(1, D+1))
    lm1, lm3 = sp.simplify(-B2/2), sp.simplify(-B4/4)
    check(f'D{D}: L(-1)', lm1 == expected[D][0])
    check(f'D{D}: L(-3)', lm3 == expected[D][1])
    check(f'D{D}: even character with full period', char[D-2] == 1 and all(
        any(char[a-1] != char[(a+d-1) % D] for a in range(1, D+1))
        for d in sp.divisors(D) if d != D))
    kappa = D*sp.sqrt(D)
    c2, c4 = lm1/2, lm3/2
    theta = -kappa/16
    zeta_mix = -120*c4*sp.Rational(D-1, D)
    chi_mix = (D*D-1)*kappa/2
    check(f'D{D}: mixed source constant zero', c4*(1-D*D)+(D*D-1)*c4 == 0)
    check(f'D{D}: two-old conjugate L2 nonzero', lm1 != 0)
    rows.append({'D': D, 'character': list(map(int, char)), 'c2': str(c2),
                 'c4': str(c4), 'kappa4': str(kappa), 'pure_theta_factor': str(theta),
                 'mixed_zeta3_factor': str(zeta_mix), 'mixed_L3_factor': str(chi_mix),
                 'two_old_conjugate_L2_over_pi2': str(lm1/4), 'three_old_level': 4*D})

x = sp.Symbol('x')
PE, PF = (1-x)*(1-4*x), (1-4*x)*(1-16*x)
check('three-old E constant cancels', PE.subs(x, 1) == 0)
check('both middle E/F terms vanish', PE.subs(x, sp.Rational(1, 4)) == PF.subs(x, sp.Rational(1, 4)) == 0)
check('F at s3', PF.subs(x, sp.Rational(1, 8)) == sp.Rational(-1, 2))
check('E at s1', PE.subs(x, sp.Rational(1, 2)) == sp.Rational(-1, 2))
check('E at s3', PE.subs(x, sp.Rational(1, 8)) == sp.Rational(7, 16))

geometry = {}
for n, wanted in ((5,0),(8,0),(12,0),(16,0),(20,1),(24,1),(32,1),(48,3)):
    g, c, mu = genus0(n)
    check(f'X0({n}) genus', g == wanted)
    geometry[str(n)] = {'genus': str(g), 'cusps': c, 'index_PSL': mu}

H = {1:-2, 2:3, 4:-1, 8:-1, 16:3, 32:-2}
B = {4:2, 8:2}
check('h32 weight zero', sum(H.values()) == 0)
check('h32 eta congruences', sum(d*r for d,r in H.items()) % 24 == 0
      and sum((32//d)*r for d,r in H.items()) % 24 == 0)
check('h32 eta character trivial', sp.prod(sp.Rational(d)**r for d,r in H.items()) == 1)
check('h32 Fricke pairing and prefactor', all(H[d] == H[32//d] for d in H)
      and sp.prod(sp.Rational(32,d)**sp.Rational(r,2) for d,r in H.items()) == 1)
check('B32 weight two and Fricke pairing', sum(B.values()) == 4 and B[4] == B[8])
check('B32 eta congruences and trivial character', sum(d*r for d,r in B.items()) % 24 == 0
      and sum((32//d)*r for d,r in B.items()) % 24 == 0
      and sp.sqrt(sp.prod(sp.Rational(d)**r for d,r in B.items())).is_Integer)
check('B32 Fricke prefactor modulus one', sp.prod(sp.Rational(32,d)**sp.Rational(r,2) for d,r in B.items()) / 32 == 1)
cusp_rows = []
for c, count, h_ord in ((1,1,-1),(2,1,1),(4,2,0),(8,2,0),(16,1,1),(32,1,-1)):
    check(f'h32 cusp denominator{c} order', eta_order(32,H,c) == h_ord)
    check(f'B32 cusp denominator{c} order', eta_order(32,B,c) == 1)
    check(f'cusp denominator{c} multiplicity', sp.totient(math.gcd(c,32//c)) == count)
    cusp_rows.append({'denominator':c,'count':count,'h_order':h_ord,'B_order':1})
check('all eight cusps covered', sum(r['count'] for r in cusp_rows) == 8)
check('h32 degree exactly two', sum(-r['h_order']*r['count'] for r in cusp_rows if r['h_order']<0) == 2)
phase_rows = []
for a,c,ph,wanted in ((1,4,sp.Rational(-1,4),'1-i'),(3,4,sp.Rational(-7,4),'1+i'),
                       (1,8,sp.Rational(1,4),'1+i'),(3,8,sp.Rational(-1,4),'1-i')):
    phase, normsq = eta_constant(H,a,c)
    check(f'h32 cusp {a}/{c} phase', phase == ph)
    check(f'h32 cusp {a}/{c} modulus squared', normsq == 2)
    val = sp.simplify(sp.sqrt(normsq)*sp.exp(sp.pi*sp.I*phase).expand(complex=True))
    check(f'h32 cusp {a}/{c} full value', sp.simplify(val - (1+sp.I if wanted=='1+i' else 1-sp.I)) == 0)
    phase_rows.append({'a':a,'c':c,'phase_over_pi':str(phase),'modulus_squared':str(normsq),'h_value':wanted})

# Character cover of X0(8)/X0(12): exactly two ramified cusps.
cover_rows = []
for D, expected_branch in ((8,[2,4]),(12,[2,6])):
    branches=[]
    for c in sp.divisors(D):
        width=D//math.gcd(c*c,D)
        if sp.kronecker_symbol(D,1-c*width) == -1:
            branches.append(int(c))
    check(f'D{D} character cover branches', branches == expected_branch)
    check(f'D{D} no elliptic branch omitted', genus0(D)[0] == 0 and D%4 == 0)
    cover_rows.append({'D':D,'branched_cusp_denominators':branches,
                       'genus_kernel_chi_by_Riemann_Hurwitz':0})

manifest=[]
for filename,url,title in (
    ('yang2007_apery_limits_v1_20261006.pdf','https://arxiv.org/pdf/0709.1968v1','Yifan Yang, Apery limits and special values of L-functions, arXiv:0709.1968v1'),
    ('ogg1974_hyperelliptic_modular_curves_20261006.pdf','https://www.numdam.org/article/BSMF_1974__102__449_0.pdf','A. P. Ogg, Hyperelliptic modular curves, BSMF 102 (1974), 449-462')):
    p=ROOT/'literature'/filename
    manifest.append({'filename':filename,'url':url,'title':title,'pages':fitz.open(p).page_count,
                     'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})

reused=[]
prior=json.loads((ROOT/'literature'/'cdt_odd_sources_20261005.json').read_text(encoding='utf-8'))['sources']
for filename in ('beukers1987_modular_irrationality.pdf','rouse_webb2014_eta_quotients_v3.pdf',
                 'zagier2009_apery_like_recurrences.pdf'):
    entry=next(e for e in prior if e['file']==filename)
    p=ROOT/'literature'/filename
    reused.append({'filename':filename,'title':entry['title'],'url':entry['source_url'],
                   'version':entry['version'],'pages':fitz.open(p).page_count,
                   'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
p=ROOT/'literature'/'cdt2024_l2_chi_minus3.pdf'
reused.append({'filename':p.name,'title':'Calegari-Dimitrov-Tang, The linear independence of 1, zeta(2), and L(2,chi_-3)',
               'url':'https://arxiv.org/abs/2408.15403v2','version':'v2 2024-09-16',
               'pages':fitz.open(p).page_count,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})

payload={'scope':'Fixed exact arithmetic, eta cusp divisor/phase, and genus checks only; no irrationality theorem, parameter or prime scan.',
         'check_count':len(checks),'checks':checks,'candidate_rows':rows,'geometry':geometry,
         'eta32_cusps':cusp_rows,'eta32_finite_phases':phase_rows,'character_covers':cover_rows,
         'new_sources':manifest,'reused_sources':reused}
OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'literature'/'manifest_cdt_candidates_5_8_12_20261006.json').write_text(
    json.dumps({'date':'2026-10-06','new_primary_documents':manifest,'reused_primary_documents':reused,
                'note':'Original PDF bytes preserved; no downloaded source code executed.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} fixed exact checks passed; {OUT.name}')
