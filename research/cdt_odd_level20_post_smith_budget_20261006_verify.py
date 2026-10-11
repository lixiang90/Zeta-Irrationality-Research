"""Read final frozen type-family bounds; no producer imports or parameter scan."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json

HERE = Path(__file__).resolve().parent
INPUT = HERE / 'cdt_odd_level20_pure_budget_20261006_verify.json'
REPORT = Path(__file__).with_name('cdt_odd_level20_post_smith_budget_20261006.md')
checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


data = json.loads(INPUT.read_text(encoding='utf-8'))
check('original_classification_scope_is_prescribed',
      data['status'] == 'exact_specified_pure_helper_type_audit_passed')
expected = [(13, 768, F(1345,507), F(335,117)),
            (14, 1536, F(2577,980), F(3853,1365)),
            (15, 3072, F(1769,675), F(14,5))]
check('three_original_families', len(data['families']) == len(expected))
rows = []
for family, (m, count, lower, target) in zip(data['families'], expected):
    check(f'm{m}_input_identity',
          family['actual_rank_conditional_on_companion_proof'] == m
          and family['specified_type_count'] == count
          and F(family['minimum_total_lower']) == lower)
    original_threshold = m*lower/(m-1)
    check(f'm{m}_original_threshold',
          original_threshold == F(family['necessary_rho_lower']))
    kappa = lower-F(5,3*m*m)
    new_threshold = m*kappa/(m-1)
    check(f'm{m}_optimistic_threshold', new_threshold == target)
    check(f'm{m}_threshold_at_least_14_over_5', new_threshold >= F(14,5))
    rows.append({'m':m, 'type_count':count, 'cost_lower':str(lower),
                 'optimistic_kappa_lower':str(kappa),
                 'optimistic_necessary_rho_lower':str(new_threshold)})
positive_sum = sum((F(14,5)**n/F(factorial(n)) for n in range(11)), F(0))
check('exp_14_over_5_positive_series_lower_exceeds_16', positive_sum > 16)
out = {'status':'exact_post_smith_prescribed_family_budget_passed',
       'scope':'Three preclassified families, ordinary Jensen numerator, original log16 cover, only the certified two target layers. Optimistic lower bound, not a transport optimum or a new irrationality theorem.',
       'checks_passed':len(checks), 'check_labels':checks, 'families':rows,
       'input_certificate':INPUT.name,
       'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'report_sha256':hashlib.sha256(REPORT.read_bytes()).hexdigest(),
       'exp_positive_partial_sum':str(positive_sum),
       'new_numerical_irrationality_theorem':False}
Path(__file__).with_suffix('.json').write_text(
    json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status':out['status'], 'checks_passed':len(checks),
                  'families':rows}, ensure_ascii=False))
