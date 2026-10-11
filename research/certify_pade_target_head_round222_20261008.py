"""One exact finite certificate for the target coefficient Delta_0, not infinite nonzero."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

DEGREE = 5

def multiply(left, right):
    return [sum((left[j] * right[i-j] for j in range(i+1)), Q(0)) for i in range(DEGREE+1)]

def factor(distance, power):
    if power == 3:
        return [Q(comb(3, h), distance**h) if h <= 3 else Q(0) for h in range(DEGREE+1)]
    assert power == -6
    return [Q((-1)**h * comb(5+h, h), distance**h) for h in range(DEGREE+1)]

def row(n):
    assert n % 2 == 0
    totals = {s: Q(0) for s in (3, 5, 7)}
    for k in range(n+1):
        top = (comb(n, k)**2 * comb(n+k, n) * comb(2*n-k, n))**3
        regular = [Q(1)] + [Q(0)] * DEGREE
        for j in range(1, n+1):
            regular = multiply(regular, factor(-k-j, 3))
            regular = multiply(regular, factor(n+j-k, 3))
        for r in range(n+1):
            if r != k:
                regular = multiply(regular, factor(r-k, -6))
        for s in totals:
            totals[s] += (-1)**k * top * regular[7-s]
    return [Q(s-1) * (1-Q(1, 2**(s-1))) * totals[s] for s in (3, 5, 7)]

rows = [row(n) for n in (0, 2, 4)]
a, b, c = rows
delta = a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0])
assert a == [Q(0), Q(0), Q(189, 32)]
assert delta == Q(189, 32) * (b[0]*c[1]-c[0]*b[1]) and delta != 0
record = {'round': 222, 'scope': 'Only exact Delta_0 from n=0,2,4. No claim of infinite nonzero, holonomic rank or overconvergence.',
          'rows': [{'n': n, 'A3': str(values[0]), 'A5': str(values[1]), 'A7': str(values[2])} for n, values in zip((0,2,4), rows)],
          'Delta0': str(delta), 'nonzero': True}
output = Path(__file__).with_name('pade_target_head_certificate_round222_20261008.json')
assert not output.exists(), 'Do not overwrite a frozen certificate.'
output.write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
