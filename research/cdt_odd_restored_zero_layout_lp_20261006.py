"""NEW standalone rational residue-LP integration for zero-restored layouts.
No old or peer producer imports. Bounds are for the proved minor model.
"""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json
import math


def floor(x):
    return x.numerator // x.denominator


def value(ab, x):
    return ab[0]*x+ab[1]


def groups(s, k, B, x):
    A, C = floor(B/x), floor(2/x)
    cuts = [(Q(0),Q(0)),(-Q(A),Q(B)),(Q(C+1),Q(-2)),(Q(1),Q(0))]
    cuts.sort(key=lambda ab:value(ab,x))
    ans=defaultdict(lambda:[Q(0),Q(0)])
    for lo,hi in zip(cuts,cuts[1:]):
        mass=(hi[0]-lo[0],hi[1]-lo[1])
        if value(mass,x)==0:
            continue
        assert value(mass,x)>0
        u=(value(lo,x)+value(hi,x))/(2*x)
        q=floor(B/x-u)
        w=2*int(u>B/x-A)+k*int(u>=1-(2/x-C))
        e=int(x>B-x*u and x>2+x*u)
        previous=None
        for m in range(1,2*(q+1)+1):
            delta=2*m+w-s-2+(s-1)*int(m>2*q)+e*(int(m==1)-int(m==2))
            assert previous is None or delta>=previous
            previous=delta
            ans[delta][0]+=mass[0]
            ans[delta][1]+=mass[1]
    return sorted((cost,tuple(mass)) for cost,mass in ans.items())


def optimum(s,k,B,x):
    d=B-k
    c=floor(d/x)
    result=(Q(c*(c+1)),Q(-2*d*c))
    used=(Q(0),Q(0))
    for cost,mass in groups(s,k,B,x):
        nxt=(used[0]+mass[0],used[1]+mass[1])
        if value(nxt,x)>=d:
            rest=(-used[0],Q(d)-used[1])
            return (result[0]+cost*rest[0],result[1]+cost*rest[1])
        result=(result[0]+cost*mass[0],result[1]+cost*mass[1])
        used=nxt
    raise AssertionError("rank resource insufficient")


def integrate(s,k,B,eps):
    d=B-k
    cuts={eps,Q(B)}
    for numerator in (2,d,B,B+2):
        for j in range(1,floor(Q(numerator)/eps)+1):
            z=Q(numerator,j)
            if eps<z<B:
                cuts.add(z)
    cc=sorted(cuts)
    pieces=[]
    for l,r in zip(cc,cc[1:]):
        xx=(l+r)/2
        more={l,r}
        used=(Q(0),Q(0))
        for _,mass in groups(s,k,B,xx):
            used=(used[0]+mass[0],used[1]+mass[1])
            if used[0]:
                z=(Q(d)-used[1])/used[0]
                if l<z<r:
                    more.add(z)
        mm=sorted(more)
        for a,b in zip(mm,mm[1:]):
            ab=optimum(s,k,B,(a+b)/2)
            for z in ((3*a+b)/4,(a+3*b)/4):
                assert value(ab,z)==value(optimum(s,k,B,z),z)
            if pieces and pieces[-1][1]==a and pieces[-1][2]==ab:
                pieces[-1]=(pieces[-1][0],b,ab)
            else:
                pieces.append((a,b,ab))
    integ=sum(a*(r*r-l*l)/2+b*(r-l) for l,r,(a,b) in pieces)
    tail=-d*s*eps-Q((k+2)**2+4,32)*eps**2
    safeA=-integ-tail
    # Orientation only: strict mathematical bounds use the exact expressions.
    y=1.0
    lam=(k+2)*math.atan(2/y)-2*math.atan((B+2)/y)
    kap=2*math.pi-lam
    c1=(k+2)*math.log(y*y+4)-(B+2)*math.log(y*y+(B+2)**2)+2*B*math.log(B)-2*k*math.log(2)
    energy=d*d*math.log(2*kap/math.pi)-d*c1
    assert 0<lam<2*math.pi
    return {
        "s":s,"zero_multiplicity":k,"pole_B":B,"rank_slope":d,"epsilon":str(eps),
        "piece_count":len(pieces),"exact_main_integral":str(integ),"tail_lower_bound":str(tail),
        "safe_A_upper_bound":str(safeA),"safe_A_decimal_orientation_only":float(safeA),
        "energy_y1_decimal_orientation_only":energy,"margin_decimal_orientation_only":energy-float(safeA),
        "pieces":[{"left":str(l),"right":str(r),"slope":str(a),"intercept":str(b)} for l,r,(a,b) in pieces],
    }


if __name__=="__main__":
    results=[integrate(5,4,B,Q(1,20)) for B in (5,6,8)]
    out={"status":"exact_restored_layout_minor_model_integrated","new_producer_execution_ordinal":1,
         "scope":"Exact rational arithmetic upper bounds; floating energy/margin is orientation only, not a new numerical theorem.",
         "old_or_peer_producer_execution_import_rerun":0,"results":results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{key:r[key] for key in ('s','pole_B','rank_slope','piece_count','safe_A_decimal_orientation_only','energy_y1_decimal_orientation_only','margin_decimal_orientation_only')} for r in results]))
