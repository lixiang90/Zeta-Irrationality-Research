"""One preselected K=1 polynomial slow minor; no producer imports or prime scan.

Exact literal eta logarithmic-derivative recurrence and character E/F formulas.
Only rows1..12 and columns Xi0..5,sXi0..5 are evaluated.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json

ORDER = 12

@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __add__(self, other):
        y = kk(other)
        return K(self.a + y.a, self.b + y.b)
    __radd__ = __add__
    def __neg__(self):
        return K(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-kk(other))
    def __rsub__(self, other):
        return kk(other) - self
    def __mul__(self, other):
        y = kk(other)
        return K(self.a*y.a + 5*self.b*y.b, self.a*y.b + self.b*y.a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        y = kk(other)
        norm = y.a*y.a - 5*y.b*y.b
        if not norm:
            raise ZeroDivisionError
        return self * K(y.a/norm, -y.b/norm)
    def norm(self):
        return self.a*self.a - 5*self.b*self.b
    def conjugate(self):
        return K(self.a, -self.b)
    def encode(self):
        return [str(self.a), str(self.b)]

def kk(x):
    return x if isinstance(x, K) else K(F(x), F(0))

ZERO, ONE, ROOT = K(), K(F(1)), K(F(0), F(1))
labels = []

def check(label, condition):
    if not condition:
        raise AssertionError(label)
    labels.append(label)

def pad(series):
    return list(series) + [ZERO]*(ORDER+1-len(series))

def multiply(a, b):
    out = [ZERO]*(ORDER+1)
    for n in range(ORDER+1):
        out[n] = sum((a[j]*b[n-j] for j in range(n+1)), ZERO)
    return out

def inverse(a):
    out = [ZERO]*(ORDER+1)
    out[0] = ONE/a[0]
    for n in range(1, ORDER+1):
        out[n] = -sum((a[j]*out[n-j] for j in range(1, n+1)), ZERO)/a[0]
    return out

def compose(a, b):
    assert b[0] == ZERO
    out = [ZERO]*(ORDER+1)
    for coefficient in reversed(a):
        out = multiply(out, b)
        out[0] = out[0] + coefficient
    return out

def determinant(rows):
    work = [list(row) for row in rows]
    value = ONE
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if work[i][j] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            work[pivot], work[j] = work[j], work[pivot]
            value = -value
        top = work[j][j]
        value = value * top
        for i in range(j+1, len(rows)):
            multiplier = work[i][j]/top
            for h in range(j+1, len(rows)):
                work[i][h] = work[i][h] - multiplier*work[j][h]
            work[i][j] = ZERO
    return value

def chi(n):
    return (0, 1, -1, -1, 1)[n % 5]

def sigma1(n):
    return sum(d for d in range(1, n+1) if n % d == 0)

# t=q product eta_d^e_d, reconstructed from its literal logarithmic derivative.
eta = {1:3, 2:-4, 4:1, 5:1, 10:-4, 20:3}
log = [0] + [-sum(e*d*sigma1(n//d) for d, e in eta.items() if n % d == 0)
             for n in range(1, ORDER+1)]
unit = [1] + [0]*ORDER
for n in range(1, ORDER+1):
    numerator = sum(log[j]*unit[n-j] for j in range(1, n+1))
    check(f"eta integral recursion n={n}", numerator % n == 0)
    unit[n] = numerator//n
tq = [ZERO] + [kk(x) for x in unit[:ORDER]]
qvar = pad([ZERO, ONE])

# Reversion by solving one new coefficient at a time: t(q)=q+higher terms.
qt = qvar[:]
for n in range(2, ORDER+1):
    qt[n] = -compose(tq, qt)[n]
check("fixed coordinate t first six", tq[1:7] == [kk(x) for x in (1,-3,4,-7,13,-20)])
check("inverse coordinate q first six", qt[1:7] == [kk(x) for x in (1,3,14,82,539,3793)])
check("t(q(t)) full ORDER12", compose(tq, qt) == qvar)
check("q(t(q)) full ORDER12", compose(qt, tq) == qvar)
check("both coordinates integral", all(x.b == 0 and x.a.denominator == 1 for x in tq+qt))

def ef(weight):
    E = [kk(F(-1,5) if weight == 2 else 1)]
    G = [ZERO]
    for n in range(1, ORDER+1):
        E.append(kk(sum(chi(d)*d**(weight-1) for d in range(1,n+1) if n%d == 0)))
        G.append(kk(sum(chi(n//d)*d**(weight-1) for d in range(1,n+1) if n%d == 0)))
    return E, G

def dilate(series, d):
    return [series[n//d] if n%d == 0 else ZERO for n in range(ORDER+1)]

E2, F2 = ef(2)
E4, F4 = ef(4)

def primitives(delta):
    # delta=+1 implements the actual minus source; delta=-1 is its conjugate.
    root = delta*ROOT
    A = [e - 4*root*f for e, f in zip(E2, dilate(F2,4))]
    VE = [a - 5*b + 4*c for a,b,c in zip(E4, dilate(E4,2), dilate(E4,4))]
    VF = [a - 20*b + 64*c for a,b,c in zip(F4, dilate(F4,2), dilate(F4,4))]
    V = [a - F(5,4)*root*b for a,b in zip(VE,VF)]
    f = [ZERO] + [V[n]/(n**3) for n in range(1, ORDER+1)]
    N = pad([ONE, -(6+root), 1+root])
    C = pad([ONE, -(6-2*root), 6-2*root])
    D = multiply(multiply(pad([ONE,-ONE]),N),C)
    carrier = multiply(compose(A,qt),compose(f,qt))
    W = multiply(carrier,inverse(D))
    Xi = [[ZERO] + [W[n-j]/n if n>=j else ZERO for n in range(1, ORDER+1)]
          for j in range(6)]
    check(f"forcing zero constant delta={delta}", V[0] == ZERO)
    check(f"actual f zero constant delta={delta}", f[0] == ZERO)
    check(f"actual A constant delta={delta}", A[0] == kk(F(-1,5)))
    check(f"primitive zero constants delta={delta}", all(col[0] == ZERO for col in Xi))
    check(f"primitive derivative identities delta={delta}",
          all(kk(n)*Xi[j][n] == (W[n-j] if n>=j else ZERO)
              for j in range(6) for n in range(1,ORDER+1)))
    return Xi

minus = primitives(1)
plus = primitives(-1)
check("all actual coefficients conjugate", plus == [[x.conjugate() for x in col] for col in minus])
columns = minus + [[ZERO]+col[:ORDER] for col in minus]
matrix = [[col[n] for col in columns] for n in range(1,ORDER+1)]
det = determinant(matrix)
pluscolumns = plus + [[ZERO]+col[:ORDER] for col in plus]
plusmatrix = [[col[n] for col in pluscolumns] for n in range(1,ORDER+1)]
check("unique preselected K1 minor nonzero", det != ZERO)
check("plus minor conjugate", determinant(plusmatrix) == det.conjugate())
check("minor norm nonzero", det.norm() != 0)
denominators = [x.a.denominator for row in matrix for x in row]
denominators += [x.b.denominator for row in matrix for x in row]
for denominator in denominators:
    for prime in (2,3,5,7,11):
        while denominator % prime == 0:
            denominator //= prime
    assert denominator == 1
check("all minor denominators supported at primes<=12", True)

result = {
    "scope": "One fixed K=1 minor only; ORDER12, rows1..12, columnsXi0..5,sXi0..5. No prime/minor scan, no uniform variable-K theorem or Smith gain.",
    "order": ORDER,
    "minor_rows": list(range(1,ORDER+1)),
    "minor_columns": [f"Xi{j}-" for j in range(6)] + [f"sXi{j}-" for j in range(6)],
    "eta_exponents": eta,
    "matrix": [[x.encode() for x in row] for row in matrix],
    "determinant": det.encode(),
    "determinant_norm": str(det.norm()),
    "bad_norm_numerator": str(abs(det.norm().numerator)),
    "bad_norm_denominator": str(det.norm().denominator),
    "coordinate_tq": [x.encode() for x in tq],
    "coordinate_qt": [x.encode() for x in qt],
    "checks_passed": len(labels),
    "check_labels": labels,
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key:result[key] for key in ("checks_passed","determinant","determinant_norm","bad_norm_numerator")}, ensure_ascii=False))
