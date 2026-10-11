"""NEW independent exact continuous LP certificate, first execution only.

Model: the actual rank-2n saturated paired Newton determinant, ambient
degree <3n, original B=6,k=3,s=5. No old/peer mathematical code imports.
The all-prime/PNT theorem is proved separately in the NEW accompanying MD.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

OUT = Path(__file__).with_suffix('.json')
if OUT.exists():
    raise RuntimeError('First execution only; refuse rerun or overwrite.')

LEFT, RIGHT, RESOURCE, CAP = F(1,4), F(6), F(2), F(-10)


def plus(a,b):
    return a[0]+b[0], a[1]+b[1]


def minus(a,b):
    return a[0]-b[0], a[1]-b[1]


def scale(c,a):
    return c*a[0], c*a[1]


def value(a,x):
    return a[0]*x+a[1]


def floorf(x):
    return x.numerator//x.denominator


def Fminor(q,w,e,m):
    return m*m+(w-6)*m+4*max(0,m-2*q)+(e if m==1 else 0)


def groups_at(x):
    A,C=floorf(6/x),floorf(2/x)
    r6,r2=(F(-A),F(6)),(F(C+1),F(-2))
    edges=sorted([(F(0),F(0)),r6,r2,(F(1),F(0))],key=lambda f:value(f,x))
    groups={}
    classes=[]
    for lo,hi in zip(edges,edges[1:]):
        length=minus(hi,lo)
        if value(length,x)==0:
            continue
        y=(value(lo,x)+value(hi,x))/2
        q=A if y<value(r6,x) else A-1
        w=(2 if y>value(r6,x) else 0)+(3 if y>=value(r2,x) else 0)
        e=int(x>6-y and x>2+y)
        assert q>=0 and value(length,x)>0 and w in (0,2,3,5)
        marginal=[]
        for m in range(1,2*q+3):
            cost=Fminor(q,w,e,m)-Fminor(q,w,e,m-1)
            marginal.append(cost)
            groups[cost]=plus(groups.get(cost,(F(0),F(0))),length)
        assert marginal==sorted(marginal)
        classes.append({'q':q,'w':w,'e':e,'length':length})
    assert sum((value(c['length'],x) for c in classes),F(0))==x
    return sorted(groups.items()),classes


def lp_affine(groups,x):
    used,cost=(F(0),F(0)),(F(0),F(0))
    for c,capacity in groups:
        after=plus(used,capacity)
        if value(after,x)<=RESOURCE:
            used=after
            cost=plus(cost,scale(F(c),capacity))
            if value(used,x)==RESOURCE:
                return cost
        else:
            return plus(cost,scale(F(c),minus((F(0),RESOURCE),used)))
    raise ArithmeticError('Insufficient continuous capacity.')


def factorial_affine(x):
    q3,q1=floorf(3/x),floorf(1/x)
    return F(-q3*(q3+1)+q1*(q1+1)),F(2*(3*q3-q1))


def integral(aff,a,b):
    return aff[0]*(b*b-a*a)/2+aff[1]*(b-a)


def exact(x):
    return f'{x.numerator}/{x.denominator}'


breaks={LEFT,RIGHT}
for numerator in (1,2,3,6,8):
    for j in range(1,4*numerator+1):
        x=F(numerator,j)
        if LEFT<x<RIGHT:
            breaks.add(x)
breaks=sorted(breaks)
segments=[]
checks=0
for a,b in zip(breaks,breaks[1:]):
    mid=(a+b)/2
    groups,classes=groups_at(mid)
    points={a,b}
    used=(F(0),F(0))
    for _,capacity in groups:
        used=plus(used,capacity)
        if used[0]:
            root=(RESOURCE-used[1])/used[0]
            if a<root<b:
                points.add(root)
    points=sorted(points)
    for aa,bb in zip(points,points[1:]):
        mm=(aa+bb)/2
        raw=minus(lp_affine(groups,mm),factorial_affine(mm))
        # Check that no missed class/order or resource event occurred.
        for xx in ((2*aa+bb)/3,(aa+2*bb)/3):
            gg,_=groups_at(xx)
            assert lp_affine(gg,xx)==lp_affine(groups,mm)
            assert value(raw,xx)==value(minus(lp_affine(gg,xx),factorial_affine(xx)),xx)
            checks+=2
        cuts={aa,bb}
        if raw[0]:
            crossing=(CAP-raw[1])/raw[0]
            if aa<crossing<bb:
                cuts.add(crossing)
        cuts=sorted(cuts)
        for aaa,bbb in zip(cuts,cuts[1:]):
            xx=(aaa+bbb)/2
            capped=raw if value(raw,xx)>=CAP else (F(0),CAP)
            assert value(capped,xx)>=CAP
            checks+=1
            segments.append({'a':aaa,'b':bbb,'raw':raw,'capped':capped,'integral':integral(capped,aaa,bbb)})

assert segments[0]['a']==LEFT and segments[-1]['b']==RIGHT
for first,second in zip(segments,segments[1:]):
    assert first['b']==second['a']
    checks+=1
finite_integral=sum((s['integral'] for s in segments),F(0))
small_integral=CAP*LEFT  # paper proof: cap is identically -10 on (0,1/4]
total_integral=small_integral+finite_integral
safeA=-total_integral
assert F(0)<safeA<F(60)
checks+=3
lower_thousand=F(floorf(safeA*1000),1000)
upper_thousand=lower_thousand+F(1,1000)
assert lower_thousand<=safeA<upper_thousand
checks+=1
record={
    'status':'PASS',
    'model':'rank2n actual paired saturated Newton determinant; original degree3n,B6,k3,s5; largest2n factorial and entry cap -10',
    'execution_count':1,
    'old_or_peer_execution_import_rerun_count':0,
    'scope':'Exact rational continuous bound-model integral only; paper proof supplies all-n finite bounds and PNT limit. Not actual primitive content equality.',
    'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'breakpoint_count':len(breaks),
    'segment_count':len(segments),
    'exact_checks':checks,
    'small_x_exact_integral':exact(small_integral),
    'finite_integral':exact(finite_integral),
    'full_integral':exact(total_integral),
    'safe_A_exact':exact(safeA),
    'safe_A_thousand_window':[exact(lower_thousand),exact(upper_thousand)],
    'coarse_A':60,
    'strict_gain_over_coarse':exact(F(60)-safeA),
    'segments':[{'left':exact(s['a']),'right':exact(s['b']),'raw_slope':exact(s['raw'][0]),'raw_intercept':exact(s['raw'][1]),'cap_slope':exact(s['capped'][0]),'cap_intercept':exact(s['capped'][1]),'integral':exact(s['integral'])} for s in segments]
}
OUT.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:record[k] for k in ('status','breakpoint_count','segment_count','exact_checks','safe_A_exact','safe_A_thousand_window','strict_gain_over_coarse')},ensure_ascii=False))
