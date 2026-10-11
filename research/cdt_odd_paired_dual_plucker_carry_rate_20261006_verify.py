"""NEW first-only certificate for the paper's dual-carry rate.

Reads an existing finite evidence JSON as data, never imports/runs its source.
Exact finite comparisons and tent integrals, not the all-scale paper proof.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise SystemExit('Refusing rerun: certificate already exists')
PROBE = Path(__file__).with_name('cdt_odd_paired_dual_plucker_layers_20261006_probe.json')
finite = json.loads(PROBE.read_text(encoding='utf-8'))
comparisons = []
for case in finite['cases']:
    n, p = case['n'], case['p']
    if not (n < p <= 2*n and p > 8):
        continue
    h, e = divmod(6*n+1, p)
    head = 2*n-p-1
    tau = p-e
    defect = max(0, min(tau,head+1-tau,head//2))
    assert head >= 0 and head % 2 == 0
    assert case['delta_dual'] == defect
    assert case['dual_rank_modp'] == n-defect
    assert case['two_sided_factorial_fee_gain'] == 2*defect
    assert all(x in (0,1) for x in case['dual_Smith_valuations'])
    comparisons.append({'n':n,'p':p,'h':h,'e':e,'H':head,
                        'tau':tau,'proved_formula_defect':defect})


def affine_integral(slope, intercept, lo, hi):
    return slope*(hi*hi-lo*lo)/2 + intercept*(hi-lo)


tent_rows = []
for h in (5,4,3):
    lo, peak, hi = F(6,h+1), F(14,2*h+3), F(8,h+2)
    height = (h+1)*peak-6
    assert height == 8-(h+2)*peak == 1-peak/2
    integral = (affine_integral(h+1,-6,lo,peak)
                + affine_integral(-h-2,8,peak,hi))
    assert integral == (hi-lo)*height/2
    if h == 5:
        assert 4*lo-12 >= -10
        gain = 2*integral
        status = 'paid actual gain; old raw4x-12 exceeds cap'
    elif h == 4:
        gain = 2*integral
        status = 'paid actual gain above old raw=-10 cap'
    else:
        assert -3*lo-6 < -10
        gain = F(0)
        status = 'fully hidden by entry cap; raw+2d<=-3x-6<-10'
    tent_rows.append({'h':h,'lo':str(lo),'peak':str(peak),'hi':str(hi),
                      'height':str(height),'integral_d':str(integral),
                      'paid_gain':str(gain),'scope':status})

gain = sum(F(row['paid_gain']) for row in tent_rows)
assert gain == F(6,91)+F(8,165) == F(1718,15015)
base = F(1085983123,24190320)
new = base-gain
assert F(44779,1000) < new < F(44780,1000)
data = {'status':'exact-dual-carry-rate-certificate-pass',
        'scope':'Finite actual dual/probe comparisons and exact tent/cap integrals. Paper supplies complementary-minor identity, graph rank, all-scale Smith layers and PNT. Not actual content equality, infinite unit or irrationality.',
        'execution_count':1,'old_or_peer_execution_import_rerun_count':0,
        'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_json_path':PROBE.name,
        'input_json_sha256':hashlib.sha256(PROBE.read_bytes()).hexdigest(),
        'finite_formula_checks':len(comparisons),
        'formula_comparisons':comparisons,'tent_intervals':tent_rows,
        'base_safe_A':str(base),'strict_safe_gain':str(gain),
        'new_safe_A':str(new),'new_safe_A_window':['44.779','44.780'],
        'unpaid_third_tent':True,
        'not_proved':['Infinite auxiliary-prime nonzero','Strict arithmetic-analytic margin','New numerical irrationality','Lean']}
OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':data['status'],'finite_formula_checks':len(comparisons),
                  'paid_gain':str(gain),'new_safe_A':str(new)},ensure_ascii=False))
