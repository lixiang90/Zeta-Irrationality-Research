"""Verify explicit analytic bounds and CONDITIONAL irrationality thresholds.

The unknown rational intersection denominator D is not estimated here.
No row in the threshold table asserts an unconditional irrationality result.
"""
import json
from pathlib import Path
from flint import arb, fmpq as Q, ctx
from zeta35_uneliminated import phase_certificate, coefficients

ROOT = Path(__file__).parent
ctx.prec = 192


def phase4_certificate():
    lo = Q(11322418823119001, 10**16)
    hi = Q(11322418823119003, 10**16)
    def saddle(x):
        return x**5*(x+2)-(x-1)*(x+1)**5
    assert saddle(lo) > 0 and saddle(hi) < 0
    x = arb('1.1322418823119002', '0.0000000000000001')
    f = 5*x*x.log()-(x-1)*(x-1).log()+(x+2)*(x+2).log()-5*(x+1)*(x+1).log()
    assert f < arb('-3.525')
    return str(f)


def margin(n, D, constant):
    return arb('0.147')*n+2*arb(n).log()-arb(constant*D).log()


def threshold(D, constant):
    n = 1
    while not margin(n, D, constant) > 0:
        n += 1
    if n > 1:
        assert margin(n-1, D, constant) < 0
    return n


def main():
    phases = dict(six=phase_certificate(), four=phase4_certificate())
    assert (2*arb.pi())**2*3*arb(3).sqrt()*(arb(17)/18).exp() < 720
    assert 2*arb.pi()*3*arb(3).sqrt()*(arb(11)/18).exp() < 126
    assert 1/(arb('0.261')*arb(1).exp()) < 2
    assert arb('6.38')-6*arb('1.03883') > arb('0.147')
    assert arb('3.525')-3*arb('1.03883') > arb('0.408')
    table = []
    for power in (0, 6, 20, 100):
        D = 10**power
        table.append(dict(assumed_D_upper_bound=str(D),
                          base_n=threshold(D, 180),
                          mixed_n=threshold(D, 432)))
    # Sanity checks on the exact small forms, independent of the global proof.
    samples = []
    for n in range(1, 11):
        a = coefficients(n)
        e = coefficients(n, 4)
        ctx.prec = 512
        aa, bb, cc = map(int, a['standard'])
        uu, _, vv = map(int, e['standard'])
        L = aa*arb(3).zeta()+bb*arb(5).zeta()+cc
        E = uu*arb(3).zeta()+vv
        base_bound = arb(180)/n**2*(-arb('0.147')*n).exp()
        e_bound = arb(63)/n*(-arb('0.408')*n).exp()
        mixed_bound = arb(432)/n**2*(-arb('0.147')*n).exp()
        assert 0 < L < base_bound
        assert 0 < E < e_bound
        assert L+2*E < mixed_bound
        samples.append(dict(n=n, base_log=str(L.log()),
                            base_bound_log=str(base_bound.log())))
    out = dict(status='Conditional on a bound for D; no unconditional starting index found',
               phases=phases, table=table, samples=samples,
               psi_bound_source='Rosser-Schoenfeld 1962, Theorem 12: psi(x)<1.03883*x for x>0')
    (ROOT/'zeta35_effective_threshold.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(table, indent=2))


if __name__ == '__main__':
    main()
