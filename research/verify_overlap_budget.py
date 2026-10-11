"""Independent density integration, envelope, tail, and real-side checks."""
import json
import math
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
from overlap_asymptotic_budget import profile,geometry,candidate_lines,tail_budget,real_lower
from two_prefix_budget import deficit,linval
from global_envelope import area
from restart_obstruction_certificate import outward_decimal


def direct_density(alpha,a,x):
    roots,b,lam=profile(alpha,a);cuts={F(0),F(1,2)}
    # Construct breakpoints directly in u, independently of affine-cell geometry.
    for z in [x]+[c*x for c in roots]:
        frac=z-math.floor(z)
        for u in (frac,1-frac):
            if 0<u<F(1,2):cuts.add(u)
    cuts=sorted(cuts);cells=[]
    def count(z,u):return sum(-z<j+u<z for j in range(-math.ceil(z)-2,math.ceil(z)+2))
    for l,r in zip(cuts,cuts[1:]):
        u=(l+r)/2;ell=count(x,u);removed=count(b*x,u)
        eta=sum(e*count(c*x,u) for c,e in roots.items())
        small=count(min(F(1),x),u)-count(min(F(1),b*x),u);big=ell-removed-small
        ws=[min(0,2*i+eta-ell-6) for i in range(big)]+[0]*small
        cells.append((r-l,eta-ell-6,ws))
    q,j=math.floor(x),math.floor(2*lam*x)
    norm=lam*x*(-2*q+2*sum(e*math.floor(c*x) for c,e in roots.items())+2*j)-F(j*(j+1),2)
    rank=min(lam*x,max(F(0),(sum(c*e for c,e in roots.items())+2*lam-1)*x-3))
    scores=[]
    for k in range(min(b for length,b,ws in cells)-2,max(b for length,b,ws in cells)+math.ceil(4*lam*x)+5):
        scores.append(norm-lam*x*k+sum(length*deficit(k,b) for length,b,ws in cells))
    for clipped in (False,True):
        histogram={}
        for length,_,ws in cells:
            for w in ws:
                if clipped:w=min(-1,w)
                histogram[w]=histogram.get(w,F(0))+length
        remaining=lam*x;total=F(0)
        for w,count in sorted(histogram.items()):
            take=min(remaining,count);total+=take*w;remaining-=take
        assert remaining==0
        scores.append(norm-total+(0 if clipped else rank))
    return min(scores)


def mval(x):return mp.mpf(x.numerator)/x.denominator


def main():
    folder=Path(__file__).parent;rows=[]
    for name in ('overlap_asymptotic_budget.json','overlap_budget_alpha40.json','overlap_budget_alpha16.json'):
        rows+=json.loads((folder/name).read_text())['rows']
    pieces_checked=0;density_checks=0;tail_checks=0;real=[]
    for row in rows:
        alpha,a=F(row['alpha']),F(row['a']);roots,b,lam=profile(alpha,a)
        cuts=geometry(alpha,a,row['cutoff']);pieces=[]
        for saved in row['pieces']:
            l,r=map(F,saved[:2]);name=saved[2];line=tuple(map(F,saved[3:]));mid=(l+r)/2
            cell=next((s,t) for s,t in zip(cuts,cuts[1:]) if s<mid<t)
            cand=candidate_lines(alpha,a,*cell);assert cand[name]==line
            assert all(linval(line,x)<=linval(v,x) for x in (l,r) for v in cand.values())
            assert direct_density(alpha,a,mid)==linval(line,mid)
            pieces.append((l,r,name,*line));pieces_checked+=1;density_checks+=1
        tail,info=tail_budget(alpha,a,row['cutoff'],row['tail_end']);A=area(pieces)+tail
        assert outward_decimal(A)==row['arithmetic_interval']
        s=F(row['test_s']);B=real_lower(alpha,a,s);assert outward_decimal(A+B)==row['gap_interval']
        # Direct numerical integral uses the original potential, not J(c,s).
        with mp.workdps(65):
            sm,lm=mval(s),mval(lam)
            def phi(c,t):
                cm=mval(c);y=mp.sqrt(t)
                return cm*mp.log(t+cm*cm)-2*cm+2*y*mp.atan(cm/y) if t else 2*cm*(mp.log(cm)-1)
            def V(t):return 2*mp.pi*mp.sqrt(t)+phi(F(1),t)-sum(e*phi(c,t) for c,e in roots.items())
            C=-2*lm+sum(2*e*mval(c)*lm*(1-mp.log(mval(c))) for c,e in roots.items())+3*lm*lm-2*lm*lm*mp.log(2*lm)
            value=lm*lm*(mp.log(sm*sm)-mp.mpf('1.5'))-lm*mp.quad(V,[0,sm*sm])/(sm*sm)+C
            assert abs(value-mval((B.lo+B.hi)/2))<mp.mpf('1e-35')
            real.append(dict(alpha=str(alpha),a=str(a),independent_numeric=str(value)))
        for x in (F(40),F(81,2),F(101,2),F(100),F(3991,10)):
            upper=lam*x*(6+2*(x-math.floor(x))-2*sum(e*(c*x-math.floor(c*x)) for c,e in roots.items()))+F(43,16)
            assert direct_density(alpha,a,x+F(1,10**6))<=upper+F(1,1000)
            tail_checks+=1
    # The new compression formula reduces exactly to the old full-pole budget.
    old=json.loads((folder/'two_prefix_budget_refined.json').read_text())['rows']
    baseline=next(r for r in old if r['alpha']=='1/24' and r['beta']=='1/6')
    current=rows[0];assert current['arithmetic_interval']==baseline['A_interval']
    assert current['gap_interval']==baseline['budget_obstruction_interval']
    crt=json.loads((folder/'overlap_truncated_crt.json').read_text())['rows'];slacks=[]
    for K,N,A,B in [(24,1,2,3),(48,2,4,6),(72,3,7,8),(96,4,9,11)]:
        records=[r for r in crt if r['K']==K and r['profile']==[[N,4],[A,2],[B,2]]]
        slacks.append(dict(K=K,N=N,A=A,B=B,checked=len(records),
                           weighted_slack=sum(r['slack']*math.log(r['p'])/K**2 for r in records),
                           nonzero=[r for r in records if r['slack']]))
    result=dict(budgets=len(rows),envelope_pieces=pieces_checked,direct_density_checks=density_checks,
                tail_sanity_checks=tail_checks,real_cross_checks=real,baseline_matches_old_exactly=True,finite_slacks=slacks)
    (folder/'overlap_budget_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['real_cross_checks','finite_slacks']}),flush=True)


if __name__=='__main__':main()
