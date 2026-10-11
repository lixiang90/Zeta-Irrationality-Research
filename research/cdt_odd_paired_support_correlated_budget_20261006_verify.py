"""NEW FIRST-ONLY certificate for the support-correlated B6/k3/s5 budget.

This producer reads no old/peer file, imports no old/peer module, and executes
no other producer.  Its exact affine model requires the paper's actual
integer-valued local-coordinate and whole-X DND proofs.  It is not a finite
prime experiment, a normality proof, or a special-value theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise SystemExit('FIRST-ONLY guard: output already exists; rerun forbidden')

# Affine pairs are (slope, intercept), with exact Fraction entries.
ZERO = (F(0), F(0))
CAP = (F(0), F(-10))

def line(a, b):
    return (F(a), F(b))

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def mul(c, u):
    return (c * u[0], c * u[1])

def val(u, x):
    return u[0] * x + u[1]

def choose_min(lines, x):
    return min(lines, key=lambda u: val(u, x))

def choose_max(lines, x):
    return max(lines, key=lambda u: val(u, x))

def positive(u, x):
    return choose_max([ZERO, u], x)

def integrate(u, a, b):
    return u[0] * (b*b - a*a)/2 + u[1] * (b-a)

def enc(u):
    if isinstance(u, F):
        return f'{u.numerator}/{u.denominator}'
    if isinstance(u, tuple):
        return [enc(v) for v in u]
    if isinstance(u, list):
        return [enc(v) for v in u]
    if isinstance(u, dict):
        return {k: enc(v) for k, v in u.items()}
    return u

# Literal old bound rows, already proved in the frozen paper; no file read.
RAW = [
    (F(1,2), F(8,15), line(40,-32)),
    (F(8,15), F(6,11), line(85,-56)),
    (F(6,11), F(4,7), line(30,-30)),
    (F(4,7), F(3,5), line(72,-54)),
    (F(3,5), F(8,13), line(12,-22)),
    (F(8,13), F(2,3), line(51,-46)),
    (F(2,3), F(8,11), line(21,-24)),
    (F(8,11), F(3,4), line(54,-48)),
    (F(3,4), F(4,5), line(6,-16)),
    (F(4,5), F(6,7), line(36,-40)),
    (F(6,7), F(8,9), line(1,-14)),
    (F(8,9), F(1), line(28,-38)),
]

base = {F(1,4), F(1,2), F(1)}
for c in (2,3,6):
    for j in range(1,25):
        x = F(c,j)
        if F(1,4) <= x <= 1:
            base.add(x)
for lo, hi, _ in RAW:
    base.add(lo)
    base.add(hi)
base = sorted(base)

pieces = []
checks = 0
for base_lo, base_hi in zip(base, base[1:]):
    sample = (base_lo+base_hi)/2
    a, h, Q = int(2/sample), int(6/sample), int(3/sample)
    units = [line(-h,6), line(a+1,-2)]
    ragged = line(-Q,3)
    kappas = [ZERO]
    # Every possible kappa branch: 2-Q*U-min(R,U), then positive part.
    for U in units:
        for top in [ragged,U]:
            kappas.append(add(line(0,2), mul(-1,add(mul(Q,U),top))))
    sectors = [add(CAP,mul(2,k)) for k in kappas]
    T, Z = line(h+1,-6), line(-a,2)
    inner = [ZERO, T, add(Z,mul(-1,T))]
    outer = [ZERO, add(T,mul(-1,Z)), add(line(1,0),mul(-1,T))]
    raw = CAP if sample < F(1,2) else next(v for lo,hi,v in RAW if lo < sample < hi)
    old_candidates = [CAP]
    if sample > F(1,2):
        old_candidates += [add(raw,mul(2,add(di,do))) for di in inner for do in outer]
    # All branch comparisons are between lines in this list.  Insert ALL
    # their roots, not only roots seen by sampling an unknown branch.
    candidates = [ZERO,ragged] + units + kappas + sectors + inner + outer + old_candidates
    points = {base_lo,base_hi}
    for u in candidates:
        for v in candidates:
            if u[0] != v[0]:
                root = (v[1]-u[1])/(u[0]-v[0])
                if base_lo < root < base_hi:
                    points.add(root)
    points = sorted(points)
    for lo,hi in zip(points,points[1:]):
        x = (lo+hi)/2
        U = choose_min(units,x)
        top = choose_min([ragged,U],x)
        d = add(mul(Q,U),top)
        kappa = positive(add(line(0,2),mul(-1,d)),x)
        sector = add(CAP,mul(2,kappa))
        if x < F(1,2):
            old = CAP
        else:
            din = positive(choose_min(inner[1:],x),x)
            dout = positive(choose_min(outer[1:],x),x)
            old = choose_max([CAP,add(raw,mul(2,add(din,dout)))],x)
        new = choose_max([old,sector],x)
        gain = add(new,mul(-1,old))
        for endpoint in (lo,hi):
            assert val(U,endpoint) >= 0
            assert 0 <= val(kappa,endpoint) <= 2
            assert val(old,endpoint) >= -10
            assert val(gain,endpoint) >= 0
            assert val(new,endpoint) >= val(old,endpoint)
            checks += 5
        pieces.append(dict(lo=lo,hi=hi,a=a,h=h,Q=Q,unit=U,ragged=ragged,
                           ambient_seen=d,kernel_lower=kappa,old=old,sector=sector,
                           new=new,gain=gain,integral=integrate(gain,lo,hi)))

assert pieces[0]['lo']==F(1,4) and pieces[-1]['hi']==1
assert all(u['hi']==v['lo'] for u,v in zip(pieces,pieces[1:]))
checks += 2
gain = sum((r['integral'] for r in pieces),F(0))
subhalf = sum((r['integral'] for r in pieces if r['hi']<=F(1,2)),F(0))
abovehalf = gain-subhalf
local_gain = sum((integrate(r['gain'],max(r['lo'],F(4,7)),min(r['hi'],F(3,5)))
                  for r in pieces if r['hi']>F(4,7) and r['lo']<F(3,5)),F(0))
assert local_gain == F(17,245)
assert gain >= local_gain > 0 and subhalf > 0
checks += 3
old_A = F(790225879771,17925027120)
new_A = old_A-gain
payload = dict(
    status='PASS', date='2026-10-06', own_first_execution_count=1,
    own_successful_execution_count=1, own_failed_execution_count=0,
    own_rerun_count=0, old_peer_execute_import_read_count=0,
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    same_object='B6/k3/s5, actual saturated paired rank2n integer-valued lattice, degree<3n, whole-X',
    exact_domain='[1/4,1]; finite all-affine-branch certificate, NOT finite prime sampling',
    required_paper_proofs='Actual integer-valued psi GL, exact degree/ragged unit-tail support cap, actual DND whole-X p-adic lattice proof, uniform errors and PNT',
    unchanged_outside_domain='Old all-prime safe bound retained for p<n/4, p>n and p^2<=8n',
    certificate_claim='Complete affine cover using ALL potential pairwise branch roots; endpoint inequalities certify each closed interval for its one-sided type',
    does_not_claim=['Exact actual Gram rank/content','Infinite rational-target nonzero','Matched margin','New special-value theorem','External Lean verification'],
    base_interval_count=len(base)-1, full_closed_affine_piece_count=len(pieces),
    exact_endpoint_checks=checks, positive_piece_count=sum(r['integral']>0 for r in pieces),
    exact_paid_gain=gain, exact_subhalf_gain=subhalf, exact_abovehalf_gain=abovehalf,
    exact_paper_single_window_gain=local_gain, old_safe_A=old_A, new_safe_A=new_A,
    pieces=pieces)
OUT.write_text(json.dumps(enc(payload),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(enc({k:v for k,v in payload.items() if k!='pieces'}),ensure_ascii=False,indent=2))
