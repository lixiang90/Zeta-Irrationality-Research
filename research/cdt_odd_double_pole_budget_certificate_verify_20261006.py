"""NEW independent exact-rational certificate checks; imports no producers."""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def log_bounds(x,N=120):
    assert x>0
    shift=0
    while x>=2:
        x/=2; shift+=1
    while x<1:
        x*=2; shift-=1
    def base(v):
        z=(v-1)/(v+1)
        partial=2*sum(z**(2*i+1)/Q(2*i+1) for i in range(N))
        err=2*abs(z)**(2*N+1)/(Q(2*N+1)*(1-z*z))
        return partial-err,partial+err
    lo,hi=base(x)
    if shift:
        a,b=base(Q(2))
        lo+=shift*(a if shift>0 else b)
        hi+=shift*(b if shift>0 else a)
    return lo,hi


def atan_bounds(x,N=120):
    assert 0<x<=Q(1,2)
    partial=sum((-1)**i*x**(2*i+1)/Q(2*i+1) for i in range(N))
    next_term=(-1)**N*x**(2*N+1)/Q(2*N+1)
    return min(partial,partial+next_term),max(partial,partial+next_term)


def linear(terms):
    lo=hi=Q(0)
    for coefficient,(a,b) in terms:
        lo+=coefficient*(a if coefficient>=0 else b)
        hi+=coefficient*(b if coefficient>=0 else a)
    return lo,hi


def energy_bounds(B):
    k=4; d=B-k
    pi=linear([(16,atan_bounds(Q(1,5))),(-4,atan_bounds(Q(1,239)))])
    kap=linear([(6,atan_bounds(Q(1,2))),(-2,atan_bounds(Q(1,B+2)))])
    c1=linear([(6,log_bounds(Q(5))),(-(B+2),log_bounds(Q((B+2)**2+1))),
               (2*B,log_bounds(Q(B))),(-8,log_bounds(Q(2)))])
    ratio=(2*kap[0]/pi[1],2*kap[1]/pi[0])
    logarithm=(log_bounds(ratio[0])[0],log_bounds(ratio[1])[1])
    return linear([(d*d,logarithm),(-d,c1)])


def check_integral(r,end):
    eps=Q(r['epsilon'])
    left=eps; total=Q(0)
    for piece in r['pieces']:
        l,rr,a,b=(Q(piece[k]) for k in ('left','right','slope','intercept'))
        assert l==left and l<rr
        total+=a*(rr*rr-l*l)/2+b*(rr-l)
        left=rr
    assert left==end
    assert total==Q(r['exact_main_integral'])
    tail=Q(r.get('tail_lower_bound',r.get('proved_tail_lower_bound')))
    assert Q(r['safe_A_upper_bound'])==-total-tail
    return Q(r['safe_A_upper_bound'])


if __name__=='__main__':
    old=json.loads((ROOT/'cdt_odd_double_pole_residue_lp_20261006.json').read_text(encoding='utf-8'))['results']
    old_caps={4:Q(30409,1000),5:Q(46159,1000),7:Q(77659,1000)}
    checks=[]
    for r in old:
        A=check_integral(r,Q(6))
        assert A<old_caps[r['s']]
        checks.append({'layout':'old_6_3','s':r['s'],'A_strict_upper':str(old_caps[r['s']])})
    baseline=old[0]
    for r in old[1:]:
        assert len(r['pieces'])==len(baseline['pieces'])
        for aa,bb in zip(baseline['pieces'],r['pieces']):
            assert (aa['left'],aa['right'])==(bb['left'],bb['right'])
            l,rr=Q(aa['left']),Q(aa['right'])
            delta=r['s']-4
            if rr<=Q(9,2):
                expected=(Q(0),Q(-3*delta))
            else:
                assert l>=Q(9,2)
                expected=(Q(2*delta),Q(-12*delta))
            observed=(Q(bb['slope'])-Q(aa['slope']),Q(bb['intercept'])-Q(aa['intercept']))
            assert observed==expected
    restored=json.loads((ROOT/'cdt_odd_restored_zero_layout_lp_20261006.json').read_text(encoding='utf-8'))['results']
    caps={5:Q(17834,1000),6:Q(35939,1000),8:Q(81249,1000)}
    energy_windows={5:(Q(7642,1000),Q(7643,1000)),6:(Q(17476,1000),Q(17477,1000)),8:(Q(43029,1000),Q(43030,1000))}
    for r in restored:
        B=r['pole_B']; A=check_integral(r,Q(B)); lo,hi=energy_bounds(B)
        assert A<caps[B]
        window=energy_windows[B]
        assert window[0]<lo<=hi<window[1]
        assert hi<A  # Obtained bounds do not supply B_an>A; not an actual-cost lower bound.
        checks.append({'layout':'restored_4','pole_B':B,'A_strict_upper':str(caps[B]),
                       'energy_strict_window':[str(z) for z in window],
                       'proved_obtained_bounds_not_positive_margin':True})
    out={'status':'exact_certificate_checks_passed','new_producer_execution_ordinal':1,
         'scope':'Exact rational integration consistency, weight-penalty identity and elementary log/atan energy intervals only; source applicability is paper proof. No irrationality theorem or lower bound for actual arithmetic cost.',
         'old_or_peer_producer_execution_import_rerun':0,'checks':checks}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':out['status'],'checked_layouts':len(checks),'old_or_peer_imports':0}))
