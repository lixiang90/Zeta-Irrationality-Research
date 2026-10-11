"""Rigorous positive-metric and layered bounds for the saved Gr(2,4) pencil.

These are finite-scale bounds. A negative bound is not a small-value example.
"""
import json
import math
import sys
import time
from pathlib import Path
from flint import arb, arb_poly, arb_mat, ctx

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    start = time.perf_counter()
    src = json.loads((ROOT/'zeta35_two_row_pencil.json').read_text())
    cols = src['coefficients']
    ctx.prec = max(abs(c).bit_length() for col in cols for c in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(col)(theta) for col in cols]
    metric = arb_mat(6,6)
    for (i,j),value in zip(src['quadratic_monomials'],values):
        metric[i,j] = metric[j,i] = value if i == j else value/2
    layers = []
    previous = arb(1)
    for size in range(1,7):
        prefix = arb_mat([[metric[i,j] for j in range(size)] for i in range(size)])
        determinant = prefix.det()
        assert determinant > 0
        sigma = determinant/previous
        assert sigma > 0
        layers.append(dict(last_nonzero_coordinate=size-1,
                           schur_log=sigma.log().str(50)))
        previous = determinant
    baseline = values[0]/math.gcd(*cols[0])
    assert baseline > 1
    # Existing complete one-row family is the p12=p13=p23=0 stratum.
    old = json.loads((ROOT/'zeta35_three_direction_bound.json').read_text())
    target_pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    indices = [list(map(tuple,src['quadratic_monomials'])).index(q) for q in target_pairs]
    first = cols[indices[0]][-1]
    old_first = old['coefficients'][0][-1]
    for index,old_col in zip(indices,old['coefficients']):
        assert all(c*old_first == o*first for c,o in zip(cols[index],old_col))
    closed = json.loads((ROOT/'zeta35_three_direction_closed_bound.json').read_text())
    assert arb(closed['all_parameters_log_lower']) > 20
    # If p12 is the last nonzero coordinate, Pluecker forces p03=0.
    # Thus this layer has only p01,p02,p12, with an improved Schur bound.
    subset = [0,1,3]
    submetric = arb_mat([[metric[i,j] for j in subset] for i in subset])
    headmetric = arb_mat([[metric[i,j] for j in subset[:2]] for i in subset[:2]])
    constrained_sigma = submetric.det()/headmetric.det()
    assert constrained_sigma > 0
    constrained = dict(variables=subset,schur_log=constrained_sigma.log().str(50))
    strata_file = ROOT/'zeta35_plucker_strata.json'
    if strata_file.exists():
        strata = json.loads(strata_file.read_text())['results']
        relevant = [row for row in strata if row['variables'] == subset and 'exponent' in row]
        if relevant:
            chosen = min(relevant,key=lambda row: int(row['exponent']))
            d = int(chosen['exponent'])
            bound = constrained_sigma/d
            constrained.update(degree=chosen['degree'],content_upper=str(d),
                               content_upper_log=arb(d).log().str(50),
                               log_lower=bound.log().str(50),
                               lower_exceeds_exp25=bool(bound > arb(25).exp()))
    exponent_file = ROOT/'zeta35_plucker_degree3_hnf.json'
    if exponent_file.exists():
        exponent_data = json.loads(exponent_file.read_text())
        # The arithmetic producer supplies an exact annihilator of its
        # degree-three module, verified separately from this analysis file.
        exponent = int(exponent_data.get('exponent',exponent_data.get('content_upper','0')))
        if exponent:
            for layer in layers:
                layer['degree3_log_lower'] = (arb(layer['schur_log'])-arb(exponent).log()).str(45)
    out = dict(K=80,h=67,head_dimension=65,
               coordinate_order=['p01','p02','p03','p12','p13','p23'],
               positive_definite_verified=True,
               layers=layers,baseline_log=baseline.log().str(50),
               first_three_coordinates_match_previous_family=True,
               p12_p13_p23_zero_log_lower_exceeds=20,
               p12_nonzero_p13_p23_zero_layer=constrained,
               analytic_precision_bits=ctx.prec,seconds=time.perf_counter()-start,
               lean_formalized=False)
    (ROOT/'zeta35_two_row_metric.json').write_text(json.dumps(out,indent=2))
    print(out,flush=True)


if __name__ == '__main__':
    main()
