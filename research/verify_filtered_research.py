"""Cross-check saved experiment conclusions with interval comparisons."""
import json
from collections import Counter
from pathlib import Path
from flint import arb, ctx, fmpq

ROOT = Path(__file__).parent


def key(row):
    return row['K'], tuple(tuple(x) for x in row['profile']), row['h']


def main():
    rows = sum((json.loads((ROOT/name).read_text()) for name in
                ['filtered_measure_scan.json', 'filtered_measure_extended.json']), [])
    bases = {key(r): r for r in rows if r['label'] == 'baseline'}
    worse = 0; comparisons = 0; degenerate = 0
    with ctx.workprec(200):
        for row in rows:
            base = bases[key(row)]
            if row['degenerate_constant']:
                assert row['degree'] == 0 and row['beta'] == '0' and row['score'] == 0
                degenerate += 1
            elif row['label'] != 'baseline':
                assert arb(row['score_ball']) > arb(base['score_ball'])
                worse += 1
            if row['label'] == 'baseline':
                continue
            pos = row['positivity']
            if fmpq(pos['a1']) > 0:
                lower = arb(fmpq(pos['a1'])/pos['period']**7)
                upper = arb(fmpq(pos['maximum']))
                delta = arb(row['raw_log_ball'])-arb(base['raw_log_ball'])
                assert delta > row['h']*lower.log()
                # The filtered measures tested here all have maximum 1;
                # every nontrivial retained-frequency filter is strictly smaller.
                assert delta < row['h']*upper.log()
                comparisons += 1
    models = json.loads((ROOT/'local_unit_models.json').read_text())
    kinds = Counter()
    for row in models['rows']:
        assert row['all_match']
        for block in row['checks']:
            assert block['matches'] and block['actual_rank'] == block['predicted_rank']
            kinds[block['kind']] += 1
    for data in models['determinants'].values():
        numerator = denominator = 1
        for p, e in data['numerator_factors'].items():
            numerator *= int(p)**e
        for p, e in data['denominator_factors'].items():
            denominator *= int(p)**e
        assert fmpq(numerator, denominator) == fmpq(data['value'])
    result = dict(scan_rows=len(rows), baseline_rows=len(bases), constant_degeneracies=degenerate,
                  nondegenerate_adjustments_worse=worse, measure_comparison_checks=comparisons,
                  local_configurations=len(models['rows']), local_blocks=sum(kinds.values()),
                  local_block_types=dict(kinds), factorization_checks=len(models['determinants']))
    assert (len(rows), len(bases), degenerate, worse, sum(kinds.values())) == (38, 5, 3, 30, 113)
    (ROOT/'filtered_research_verification.json').write_text(json.dumps(result, indent=2))
    print(json.dumps(result))


if __name__ == '__main__':
    main()
