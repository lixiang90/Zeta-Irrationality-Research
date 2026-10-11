"""Independent checks of Anand, Zenodo 22920911 (2026-09-23 version).

Fractions are used for every arithmetic-integral calculation. This audits the
printed formulas; it does NOT certify their underlying p-adic estimates.
"""
from fractions import Fraction as F
from math import floor, ceil
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from restart_obstruction_certificate import log_iv, outward_decimal, primal_bound

AL = F(3, 40)
LAM = 1 - AL
H = 1 + 3 * AL
DOMAIN = (F(1, 3), 2 * LAM)


class PW:
    """Exact piecewise affine function, ignoring finitely many endpoints."""
    def __init__(self, pieces):
        self.pieces = pieces  # (left, right, slope, intercept)

    @staticmethod
    def constant(v):
        return PW([(*DOMAIN, F(0), F(v))])

    def affine_at(self, x):
        return next((a, b) for l, r, a, b in self.pieces if l < x < r)

    def at(self, x):
        a, b = self.affine_at(x)
        return a * x + b

    def combine(self, other, minimum=False):
        if not isinstance(other, PW):
            other = PW.constant(other)
        ends = sorted(set(v for f in [self, other] for l, r, _, _ in f.pieces for v in [l, r]))
        out = []
        for l, r in zip(ends, ends[1:]):
            a, b = self.affine_at((l + r) / 2)
            c, d = other.affine_at((l + r) / 2)
            if not minimum:
                out.append((l, r, a + c, b + d))
                continue
            points = [l, r]
            if a != c and l < (d - b) / (a - c) < r:
                points.insert(1, (d - b) / (a - c))
            for ll, rr in zip(points, points[1:]):
                aa, bb = (a, b) if (a - c) * (ll + rr) / 2 + b - d <= 0 else (c, d)
                out.append((ll, rr, aa, bb))
        return PW(out)

    __add__ = combine
    __radd__ = combine

    def __mul__(self, k):
        return PW([(l, r, a * k, b * k) for l, r, a, b in self.pieces])
    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -self + other

    def minimum(self, other):
        return self.combine(other, minimum=True)

    def positive(self):
        return -((-self).minimum(0))

    def select(self, other, cut):
        return PW([row for row in self.pieces if row[1] <= cut] +
                  [(max(l, cut), r, a, b) for l, r, a, b in other.pieces if r > cut] +
                  [(l, cut, a, b) for l, r, a, b in self.pieces if l < cut < r])

    def integral(self):
        return sum(a * (r*r - l*l) / 2 + b * (r-l) for l, r, a, b in self.pieces)


def outer():
    y = PW([(*DOMAIN, F(1), F(0))])
    # Eq. (59), including its rank correction; limit of -gamma_out / K.
    v2 = 1 - 2*y
    u2 = (AL + v2 - y).positive()
    t2 = v2.minimum(AL) + u2
    rank = (1 + 6*AL - 3*y).positive().minimum(LAM)
    gamma2 = -9*(1-y) + 16*AL + 7*t2 - rank.minimum(y+u2)
    v1 = 1-y
    u1 = (AL+v1-y).positive()
    t1 = v1.minimum(AL)+u1
    gamma1 = -9*(1-y)+8*t1-rank.minimum(y-AL+u1)
    gamma = gamma2.select(gamma1, F(1, 2)).select(PW.constant(0), F(1))
    r0 = -gamma
    correction = ((1+6*AL-3*y) - (1+2*AL-3*y).positive()).positive()
    correction = correction.select(PW.constant(0), F(1, 2))
    floor1y = PW([(F(1,3), F(1,2), F(0), F(2)),
                  (F(1,2), F(1), F(0), F(1)),
                  (F(1), 2*LAM, F(0), F(0))])
    scalar = -2*LAM*floor1y + sum((2*LAM-j*y).positive() for j in range(1, 8))
    literal = r0-correction+scalar  # Eqs. (71)-(73) read literally.
    consistent = r0+scalar         # Count the rank correction only once.
    table = [
        (F(1,3),F(37,100),F(8),-F(75,8)),
        (F(37,100),F(37,80),F(16),-F(99,8)),
        (F(37,80),F(29,60),F(20),-F(569,40)),
        (F(29,60),F(1,2),F(20),-F(569,40)),
        (F(1,2),F(37,60),F(9),-F(107,10)),
        (F(37,60),F(37,40),F(12),-F(251,20)),
        (F(37,40),F(77,80),F(14),-F(72,5)),
        (F(77,80),F(1),-F(2),F(1)),
        (F(1),F(37,20),-F(2),-F(239,20)),
    ]
    tab = PW(table)
    assert tab.integral() == -F(11002997,720000)
    assert literal.at(F(3,2)) == F(7,20)
    assert consistent.at(F(3,2)) == F(7,20)
    assert tab.at(F(3,2)) == -F(299,20)
    return dict(literal_integral=str(literal.integral()),
                consistent_integral=str(consistent.integral()),
                repeated_rank_integral=str(correction.integral()),
                table_integral=str(tab.integral()),
                literal_decimal=float(literal.integral()),
                consistent_decimal=float(consistent.integral()),
                point=dict(y='3/2',from_definition='7/20',from_table='-299/20'),
                consistent_pieces=[[str(v) for v in row] for row in consistent.pieces])


def ell(x, z):
    return floor(x-z)+floor(x+z)+1


def inner_r(x):
    T = floor(2*H*x)
    s = H*x-F(T,2)
    q = floor(2*x)
    nplus = x-F(q,2)
    ends = sorted(set([F(0),F(1,2)] + [v for z in [x, AL*x]
                      for v in [z-floor(z), 1-z+floor(z)] if 0 < v < F(1,2)]))
    gam = sum((r-l)*(T-4*ell(AL*x,(l+r)/2)) *
              (T+4*ell(AL*x,(l+r)/2)-ell(x,(l+r)/2)-7)
              for l,r in zip(ends,ends[1:]))
    gam += s*(2*T-q-7)+max(F(0),s-nplus)
    mm = floor(2*LAM*x)
    J = mm*LAM*x-F(mm*(mm+1),4)
    return -gam-(2*LAM*x*floor(x)-16*LAM*x*floor(AL*x)-2*J)


def inner_expansion(x, variance_coefficient=16):
    frac = lambda z:z-floor(z)
    d = lambda z:min(z,1-z)
    sign = lambda z:1 if z < F(1,2) else -1
    f,g,tau,sigma,eta = map(frac,[x,AL*x,2*H*x,2*x,2*LAM*x])
    base = (tau*(tau-sigma)-max(F(0),tau-sigma)+eta*(1-eta))/2
    cross = sign(f)*sign(g)*(min(d(f),d(g))-2*d(f)*d(g))
    return x*(6*LAM+2*LAM*f-16*LAM*g) + base + variance_coefficient*d(g)*(1-2*d(g))-4*cross


def inner():
    coefficients = [F(2),2*AL,2*LAM,2*H,8*AL,2*(1-AL),2*(1+AL),2*(1+2*AL),F(9,20)]
    points = sorted(set([F(3),F(20)]+[F(j)/c for c in coefficients
                        for j in range(floor(3*c)+1,ceil(20*c))]))
    total = F(0)
    for l,r in zip(points,points[1:]):
        x,y = (2*l+r)/3,(l+2*r)/3
        a = (inner_r(y)-inner_r(x))/(y-x)
        b = inner_r(x)-a*x
        for q in [F(1,5),F(1,2),F(4,5)]:
            z = l+(r-l)*q
            assert inner_r(z) == a*z+b == inner_expansion(z)
        total += a*(1/l-1/r)+b*(1/l**2-1/r**2)/2
    assert len(points)-1 == 192
    assert total == F(120667538150827615739401,708353029541942104320000)
    assert inner_r(F(10)) == -F(107,2)
    assert inner_expansion(F(10),25) == -F(419,8)
    # Structural coefficient: (4B)^2 produces 16 B^2 in -Gamma.
    # A crude bound from the corrected expansion: |F| <= 10 lambda,
    # |Q| <= 3, hence |integral_20^infty R/x^3| <= 373/800.
    tail_abs_bound = 10*LAM/20+F(3,2*20**2)
    return dict(pieces=192,integral=str(total),decimal=float(total),
                expansion_counterexample=dict(x='10',definition='-107/2',eq82='-419/8'),
                corrected_variance_coefficient=16,tail_absolute_bound=str(tail_abs_bound))


def energy():
    lengths=list(map(F,['.87','.8','.7','.6','.5','.4','.3','.25','.2','.15','.12','.1','.08','.06','.04','.02']))
    weights=list(map(F,['.1','.08','.06']+['.05']*11+['.015','.12']))
    assert sum(weights) == LAM
    true = sum(weights[i]*weights[j]*log_iv(max(lengths[i],lengths[j])/4)
               for i in range(16) for j in range(16))
    printed = sum((sum(weights[:i+1])**2-sum(weights[:i])**2)*log_iv(lengths[i]/4)
                  for i in range(16))
    C = -2*LAM+16*AL*LAM*(1-log_iv(AL))+3*LAM**2-2*LAM**2*log_iv(2*LAM)
    # Isolating the energy correction; potential M=-5.45 not certified here.
    corrected_bound = -LAM*F(109,20)-true+C
    return dict(mass=str(sum(weights)),true_energy=outward_decimal(true),
                eq110_energy=outward_decimal(printed),Cstar=outward_decimal(C),
                real_bound_if_M_valid=outward_decimal(corrected_bound),
                comparison_method_lower_bound=outward_decimal(primal_bound(AL)))


def relative_norm():
    """Exact rational enclosure of the paper's useful conditional norm bound."""
    from restart_obstruction_certificate import IV, PI, iv
    from math import isqrt
    def sqrt_iv(q):
        scale=10**30
        k=isqrt(q.numerator*scale*scale//q.denominator)
        return IV(F(k,scale),F(k+1,scale))
    sq3=sqrt_iv(F(3));sq114=sqrt_iv(F(114))
    R=(43+4*sq114)/5
    logR=IV(log_iv(R.lo).lo,log_iv(R.hi).hi)
    kappa=2*PI/sq3+log_iv(F(4,3))+F(3,5)*log_iv(18)+LAM*(1+log_iv(F(1600,111)))+2*LAM*logR
    assert kappa.hi<F(14301,1000)
    # If a valid decay epsilon later exists, any exponent nu>lambda*rho/epsilon
    # follows by choosing lambda/epsilon<c<nu/rho in the standard integer argument.
    return dict(kappa_interval=outward_decimal(kappa,15),rho='14301/1000',
                conditional_threshold_numerator=str(LAM*F(14301,1000)),
                status='norm bound useful independently; claimed irrationality exponent requires unproved decay')


def repaired_prime_sum():
    """What Eqs. (59),(66),(68) would give, granting their local estimates.

    Integrate directly to M=200, avoiding the paper's tail constant entirely.
    This does not establish the local estimates as theorems.
    """
    M=200
    cs=[F(2),2*AL,2*LAM,2*H,8*AL,2*(1-AL),2*(1+AL),2*(1+2*AL),F(9,20)]
    points=sorted(set([F(3),F(M)]+[F(j)/c for c in cs
                      for j in range(floor(3*c)+1,ceil(M*c))]))
    value=F(0)
    for l,r in zip(points,points[1:]):
        x,y=(2*l+r)/3,(l+2*r)/3
        a=(inner_expansion(y)-inner_expansion(x))/(y-x)
        b=inner_expansion(x)-a*x
        assert inner_expansion((l+r)/2)==a*(l+r)/2+b
        value += a*(1/l-1/r)+b*(1/l**2-1/r**2)/2
    A=8*LAM/M+value+F(outer()['consistent_integral'])
    gap=primal_bound(AL)+A
    assert gap.lo>0
    return dict(M=M,pieces=len(points)-1,inner_integral_decimal=float(value),
                arithmetic_constant_decimal=float(A),
                arithmetic_constant_exact=str(A),
                comparison_obstruction=outward_decimal(gap),
                status='conditional on printed local estimates; this arithmetic bound cannot close via comparison-measure optimization alone')


def run():
    out=dict(source='https://zenodo.org/records/22920911',outer=outer(),inner=inner(),
             energy=energy(),relative_norm=relative_norm(),repaired_prime_sum=repaired_prime_sum())
    # Even granting all other printed constants, fixing Table 5 alone removes
    # the asserted negative final margin. This is not a certified repaired proof.
    A0=F(9928298118277006344769,7535670527041937280000)
    innerI=F(out['inner']['integral'])
    adjustment=9*LAM/200-F(11549,720*200**2)+F(44,200**3)
    out['replace_table_only']={mode:str(A0+innerI+F(out['outer'][mode])+adjustment+F(44,25))
                               for mode in ['literal_integral','consistent_integral']}
    Path(__file__).with_name('audit.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    display={**out,'outer':{k:v for k,v in out['outer'].items() if k!='consistent_pieces'},
             'repaired_prime_sum':{k:v for k,v in out['repaired_prime_sum'].items() if k!='arithmetic_constant_exact'}}
    print(json.dumps(display,indent=2))


if __name__=='__main__':
    run()
