"""NEW fixed boundary-linear-algebra certificate; imports no frozen producer."""
from pathlib import Path
import hashlib
import json
import sympy as S
import fitz

BASE = Path(__file__).resolve().parent
INPUT = BASE / 'cdt_odd_level12_generator_cocycle_20261006_verify.json'
PIN = 'b8dfb80d30a4fc276d225d148c76ead7032de51523896664f5c743eb0af966ef'
checks = []

def check(name, value):
    checks.append({'name': name, 'passed': bool(value)})
    if not value:
        raise AssertionError(name)

check('frozen actual period-data hash', hashlib.sha256(INPUT.read_bytes()).hexdigest() == PIN)
data = json.loads(INPUT.read_text(encoding='utf-8'))
raw = [
    (59,25,-144,-61),(1,1,0,1),(37,29,-60,-47),
    (11,3,-48,-13),(25,16,-36,-23),(11,9,-60,-49),
    (13,4,-36,-11),(13,6,-24,-11),(1,1,-12,-11),
]
generators = [S.Matrix(2,2,x) for x in raw]
check('nine actual matrices pinned separately', [tuple(g['matrix']) for g in data['generators']] == raw)
periods = [S.Matrix([S.Rational(x) for x in g['PL']]) for g in data['generators']]

def slash(g):
    a,b,c,d = tuple(g)
    return S.Matrix([[d*d,b*d,b*b],[2*c*d,a*d+b*c,2*a*b],[c*c,a*c,a*a]]) / g.det()

def matrix_word(word):
    out = S.eye(2)
    for letter in word:
        g = generators[abs(letter)-1]
        out = out * (g if letter > 0 else g.inv())
    return out

def cocycle_map(word):
    out = S.zeros(3,27)
    for letter in word:
        j = abs(letter)-1
        g = generators[j]
        embedding = S.zeros(3,27)
        embedding[:,3*j:3*j+3] = S.eye(3)
        if letter < 0:
            g = g.inv()
            embedding = -slash(g) * embedding
        out = slash(g) * out + embedding
    return out

stacked = S.Matrix.vstack(*periods)
Adata = [(1,0,0,1),(5,-2,-12,5),(0,1,-1,0),
         (1,1,-2,-1),(2,1,-3,-1),(1,1,-3,-2),
         (3,1,-4,-1),(1,1,-4,-3),(2,5,-5,-12),(1,0,-6,1)]
widths = [1,1,12,6,4,4,3,3,12,2]
expected = [S.Integer(0),-132480,920,-S.Rational(36160,3),13785,13785,
            -S.Rational(73520,3),-S.Rational(73520,3),0,108480]
T = S.Matrix([[1,1],[0,1]])
rows = []
records = []
for j,(item,avec,w,B) in enumerate(zip(data['cusps'],Adata,widths,expected),1):
    A = S.Matrix(2,2,avec)
    P = S.Matrix(2,2,item['matrix'])
    check(f'cusp {j} actual scaling and width', A.det()==1 and A*T**w*A.inv()==P)
    check(f'cusp {j} exact word matrix', matrix_word(item['word']) == P or matrix_word(item['word']) == -P)
    C = cocycle_map(item['word'])
    p = S.Matrix([S.Rational(x) for x in item['PL']])
    check(f'cusp {j} table rederived from free-generator assignment', C*stacked == p)
    row = slash(A)[2,:] * C
    rows.append(row)
    beta = (slash(A)*p)[2]
    check(f'cusp {j} actual source constant via cubic residue', -beta/(4*w) == B)
    linear = slash(P)-S.eye(3)
    check(f'cusp {j} unipotent linear rank two', linear.rank()==2)
    has_fixed_point = linear.row_join(p).rank()==2
    check(f'cusp {j} affine fixed-point iff beta zero', has_fixed_point == (beta==0))
    records.append({'id':j,'cusp':item['cusp'],'width':w,
                    'source_constant':str(B),'beta':str(beta),
                    'affine_has_fixed_point':has_fixed_point})
boundary = S.Matrix.vstack(*rows)
gauge = S.Matrix.vstack(*[slash(g)-S.eye(3) for g in generators])
check('all-cocycle assignment space dimension 27', boundary.cols==27)
check('boundary restriction rank ten', boundary.rank()==10)
check('coboundary rank three', gauge.rank()==3)
check('boundary kills every coboundary', boundary*gauge == S.zeros(10,3))
check('H1 dimension24, parabolic kernel14', 27-gauge.rank()==24 and 27-boundary.rank()-gauge.rank()==14)

M = S.Matrix([[24,-7],[84,-24]])
Mp = S.Matrix([[-24,-7],[84,24]])
kword = [-7,1,-8,-5,-2]
k = matrix_word(kword)
expected_k = S.Matrix([[97,-28],[-336,97]])
check('known zero hyperbolic exact PSL matrix', k == expected_k or k == -expected_k)
check('known zero hyperbolic period', cocycle_map(kword)*stacked == S.zeros(3,1))
check('known zero is genuinely hyperbolic', k.det()==1 and abs(k.trace())==194)
q = S.Matrix([1,0,-12])
check('same-cocycle-class gauge is M anti', slash(M)*q == -q)
check('same-cocycle-class gauge is Mprime anti', slash(Mp)*q == -q)
check('same-cocycle-class gauge destroys T zero', (slash(T)-S.eye(3))*q == S.Matrix([-12,-24,0]))
check('M signed cone flip at positive quadratic', (-slash(M)*S.Matrix([1,0,1]))[0] < 0)

report = {'scope':'NEW fixed pure-L boundary residues, affine fixed-point obstructions and cohomology dimensions; not full stabilizer classification',
          'input_json_sha256':PIN,'passed':len(checks),'checks':checks,
          'boundary_rank':10,'coboundary_rank':3,'H1_dimension':24,
          'parabolic_cohomology_dimension':14,'cusps':records,
          'zero_source_cusp_ids':[1,9],
          'gauge_polynomial':'1-12*tau^2','zero_hyperbolic':[int(x) for x in k]}
out = BASE / 'cdt_odd_level12_stabilizer_boundary_20261006_verify.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

LIT = BASE.parent / 'literature'
docs = [
 ('dgk_strip_author_20261006.pdf','https://www.ihes.fr/~/kassel/Strip.pdf',
  'Danciger–Guéritaud–Kassel, Margulis spacetimes via the arc complex',
  'Actual primary targeted reading: printed pp3–6,46–48; convex-cocompact/admissible and generalized-strip scope only.'),
 ('panda2024_decorated_margulis_v2_20261006.pdf','https://arxiv.org/pdf/2306.09985v2',
  'Pallavi Panda, Parametrisation of decorated Margulis spacetimes using strip deformations, v2 2024-02-09',
  'Actual primary targeted reading: PDF pp2–3,15–18; crowned boundary spikes and admissible cone, not a ten-interior-cusp surface theorem.'),
 ('pasol_popa_period_polynomials_20261006.pdf','https://arxiv.org/pdf/1202.5802',
  'Paşol–Popa, Modular forms and period polynomials',
  'Actual primary targeted reading: PDF pp22–23, Prop8.1/8.2; extended-period constant terms and Eisenstein basis, not zero-subgroup classification.'),
]
manifest = []
for filename,url,title,reading in docs:
    path = LIT / filename
    with fitz.open(path) as pdf:
        pages = len(pdf)
        first = pdf[0].get_text()[:1400]
    manifest.append({'file':filename,'url':url,'title':title,'pages':pages,
                     'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                     'reading_scope':reading,'first_page_excerpt_for_version':first})
(LIT/'manifest_cdt_odd_stabilizer_boundary_20261006.json').write_text(
    json.dumps({'scope':'new targeted primary literature for pure-L stabilizer boundary/strip applicability audit',
                'papers':manifest},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'output':str(out),'boundary_rank':10,
                  'cohomology_dimensions':[24,14],'source_zero_cusps':[1,9]}))
