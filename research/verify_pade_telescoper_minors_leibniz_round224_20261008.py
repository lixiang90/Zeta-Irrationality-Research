"""Independent finite matrix check via the defining Leibniz determinant.

Reads the fixed n=6 certificate, not an A/C/Delta sequence.  Does not run or
import its producer.  All seven 6x6 minors are checked without elimination.
The global principal-part and boundary arguments remain paper proofs.
"""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from hashlib import sha256
import json

source = Path(__file__).with_name('pade_telescoper_residual_rank_certificate_round224_20261008.json')
raw = source.read_bytes()
assert len(raw) == 26796
assert sha256(raw).hexdigest() == 'a47a933aca74e035b49233d1f7cbd7106d770f679f5840934cdbfcfc69e4bbd0'
certificate = json.loads(raw)
matrix = [[Fraction(value) for value in row] for row in certificate['remainder_matrix']]
assert len(matrix) == 6 and all(len(row) == 7 for row in matrix)
computed = []
for omitted in range(7):
    columns = [column for column in range(7) if column != omitted]
    determinant = Fraction(0)
    for permutation in permutations(range(6)):
        inversions = sum(permutation[i] > permutation[j] for i in range(6) for j in range(i+1, 6))
        term = Fraction((-1)**inversions)
        for row in range(6):
            term *= matrix[row][columns[permutation[row]]]
        determinant += term
    computed.append((-1)**omitted * determinant)
claimed = [Fraction(value) for value in certificate['signed_maximal_minors']]
assert computed == claimed
assert all(computed)
assert all(sum((row[j]*computed[j] for j in range(7)), Fraction(0)) == 0 for row in matrix)
output = {
    'scope': 'One fixed n=6 6x7 matrix; all seven maximal minors by 720-term Leibniz sums each.',
    'producer_rerun': False, 'arithmetic': 'Fraction exact; independent of producer Gaussian elimination.',
    'source_bytes': len(raw), 'source_sha256': sha256(raw).hexdigest(),
    'all_seven_minors_match': True, 'all_seven_nonzero': True, 'cofactor_kernel': True,
    'signed_minor_numerator_bit_lengths': [abs(value.numerator).bit_length() for value in computed],
    'global_scope_limit': 'Checks the saved finite matrix. Does not replace the global rational reduction proof or pay minimal order/infinite nonzero.',
    'mathematical_runs_for_this_verifier': 1, 'pass': True,
}
target = source.with_name('pade_telescoper_leibniz_review_round224_20261008.json')
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(output, ensure_ascii=False))
