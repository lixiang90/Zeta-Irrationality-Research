"""DISTINCT NEW FIRST-ONLY original-S support mechanism; never imports producers."""
import json
import math
import os
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')
guard = OUT.open('x', encoding='utf-8')
guard.write('{"status":"RUNNING_FIRST_ONLY"}\n')
guard.close()
checks = 0

def require(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)

def rank(rows, p):
    pivots = {}
    for row in rows:
        x = list(row)
        for k, v in pivots.items():
            if x[k]:
                b = x[k]
                x = [(a - b*c) % p for a, c in zip(x, v)]
        k = next((k for k, a in enumerate(x) if a), None)
        if k is not None:
            b = pow(x[k], -1, p)
            pivots[k] = [(a*b) % p for a in x]
    return len(pivots)

def greedy_independent(rows, p, target):
    pivots, selected = {}, []
    for index, row in enumerate(rows):
        x = list(row)
        for k, v in pivots.items():
            if x[k]:
                b = x[k]
                x = [(a-b*c) % p for a, c in zip(x, v)]
        k = next((k for k, a in enumerate(x) if a), None)
        if k is not None:
            b = pow(x[k], -1, p)
            pivots[k] = [(a*b) % p for a in x]
            selected.append(index)
            if len(selected) == target:
                break
    return selected

def coefficients(n, p):
    N = 3*n
    columns = []
    for m in range(1, n+1):
        mp = 2*n+1-m
        dm = math.factorial(6*n+m)//math.factorial(m-1)
        dp = math.factorial(6*n+mp)//math.factorial(mp-1)
        g = math.gcd(dm, dp)
        v, w = dm//g, dp//g
        require(math.gcd(v,w) == 1, ('primitive',n,m))
        col = [0]*N
        for z, scale in [(m,v),(mp,w)]:
            for i in range(z-1,2*n):
                col[i] = (col[i]+scale*((-1)**(i-z+1))*math.comb(i,z-1)) % p
        columns.append(col)
    columns += [[int(i==k) for i in range(N)] for k in range(2*n,N)]
    require(len(columns)==2*n, ('complete_S',n))
    for m in range(1,n+1):
        mp=2*n+1-m
        dm=math.factorial(6*n+m)//math.factorial(m-1)
        dp=math.factorial(6*n+mp)//math.factorial(mp-1)
        g=math.gcd(dm,dp)
        v,w=dm//g,dp//g
        for col in columns:
            em=sum(col[i]*math.comb(m-1,i) for i in range(m))%p
            ep=sum(col[i]*math.comb(mp-1,i) for i in range(mp))%p
            require((w*em-v*ep)%p==0, ('actual_primitive_row',n,p,m))
    require(rank(columns,p)==2*n, ('saturated_S_rank',n,p))
    return columns

def projected_row(fvalues, cols, p):
    return [sum(a*b for a,b in zip(fvalues,col))%p for col in cols]

def source_case(n,p):
    require(p>5 and p<=2*n and p*p>8*n, ('domain',n,p))
    require(all(p%d for d in range(2,math.isqrt(p)+1)), ('prime',p))
    a,r2=divmod(2*n,p); Q,R=divmod(3*n,p); h,r6=divmod(6*n,p)
    V=p-r2; u=min(r6+1,V)
    U=set(range(u)); sig=lambda r: V-1-r
    cols=coefficients(n,p)
    rows,labels=[],[]
    for j in range(6*n+1):
        fv=[((-1)**i)*math.comb(j+i,i)%p for i in range(3*n)]
        dv=[]
        for i in range(3*n):
            dv.append(sum(((-1)**(k-1))*pow(k,-1,p)*fv[i-k*p]
                          for k in range(1,i//p+1))%p)
        rows += [projected_row(fv,cols,p),projected_row(dv,cols,p)]
        labels += [(j,'value'),(j,'scaled_derivative')]
    d=2*n
    profiles={
        'value_first':list(range(0,2*d,2)),
        'derivative_only':list(range(1,2*d,2)),
        'interleaved_first':list(range(d)),
        'unit_residue_first':sorted(range(len(rows)),key=lambda i:(labels[i][0]%p not in U,labels[i][0]%p,labels[i][0],i%2))[:d],
    }
    vals=rows[::2]
    greedy=greedy_independent(vals,p,d)
    require(len(greedy)==d, ('actual_consecutive_value_fullrank',n,p))
    profiles['greedy_fullrank_values']=[2*k for k in greedy]
    records=[]
    ft=a*u-a*max(0,2*u-V)//2
    for name,I in profiles.items():
        require(len(I)==d and len(set(I))==d, ('selected_d',n,p,name))
        count=Counter(labels[i][0]%p for i in I)
        B={r for r in range(p) if count[r]>Q}; C=B & U
        outside=C-{sig(r) for r in U}
        both=C & {sig(r) for r in C}
        numerator=2*a*len(outside)+a*len(both)
        require(numerator%2==0, ('fB_integer',n,p,name))
        fB=numerator//2
        base=sum(min(count[r],Q) for r in range(p))+min(R,len(B))
        actual=rank([rows[i] for i in I],p)
        require(actual<=base-fB, ('supported_rank',n,p,name,actual,base,fB))
        records.append({'name':name,'rank':actual,'coefficient_cap':base,'f_supported':fB,
                        'f_global':ft,'naive_global_cap':base-ft,
                        'global_subtraction_invalid':actual>base-ft,
                        'B':sorted(B),'C':sorted(C),'residue_counts':[count[r] for r in range(p)],
                        'selected_rows':[{'j':labels[i][0],'type':labels[i][1]} for i in I]})
    require(records[-1]['rank']==d, ('fullrank_selection',n,p))
    return {'n':n,'p':p,'a':a,'Q':Q,'R':R,'h':h,'V':V,'u':u,'profiles':records}

def affine_math():
    lo,mid,hi=F(2,3),F(19,27),F(17,24)
    def alpha(w,q,lam,eta):
        return min(w*r+4*max(0,r-2*q)+2*max(0,r-4)-lam*r-eta*int(r>4)
                   for r in range(2*q+3))
    candidates=[]
    for lam in range(12):
        for eta in range(3):
            z=alpha(0,8,lam,eta); t=alpha(3,8,lam,eta); v=alpha(5,7,lam,eta)
            slope=4*(2-eta)+3*z-11*t+9*v
            intercept=-10+2*lam-3*(2-eta)-2*z+8*t-6*v
            for x in [lo,hi]:
                require(slope*x+intercept<=48-78*x, ('baseline_face',lam,eta,x))
            candidates.append({'lambda':lam,'eta':eta,'slope':slope,'intercept':intercept})
    def price(w,q,r):
        return w*r+4*max(0,r-2*q)+2*max(0,r-4)-3*r-2*int(r>4)
    for r in range(19):
        require(price(0,8,r)>=(-26 if r>4 else -12), ('unitprice',r))
        require(price(3,8,r)>=0, ('w3price',r))
    for r in range(17):
        require(price(5,7,r)>=0, ('w5price',r))
    for r in range(19):
        require(price(0,8,r)+2*int(r>4)>=-24, ('loop',r))
        for s in range(19):
            require(price(0,8,r)+price(0,8,s)+4*int(r>4 and s>4)>=-48, ('pair',r,s))
    def integral(slope,intercept,l,h):
        return slope*(h*h-l*l)/2+intercept*(h-l)
    left=integral(6,-4,lo,mid); right=integral(-48,34,mid,hi)
    require(left==F(1,243) and right==F(1,1944), 'two_gain_pieces')
    require(left+right==F(1,216), 'positive_paid_gain')
    return {'domain':{'lo':str(lo),'hi':str(hi),'cross':str(mid)},'old_36_faces':candidates,
            'gain_left':str(left),'gain_right':str(right),'gain_total':str(left+right),
            'new_slope':-72,'new_intercept':44,'all_scale_proof_is_paper':True}

try:
    literal_cases=[(19,13),(27,19),(53,37),(10,11),(33,19),(55,41)]
    saved=[source_case(n,p) for n,p in literal_cases]
    affine=affine_math()
    invalid=[{'n':c['n'],'p':c['p'],'profile':v['name'],'rank':v['rank'],
              'cap':v['coefficient_cap'],'f_global':v['f_global'],'f_supported':v['f_supported']}
             for c in saved for v in c['profiles'] if v['global_subtraction_invalid']]
    require(bool(invalid), 'actual_counterexample_to_global_subtraction')
    result={'status':'PASS','first_execution_count':1,'successful_executions':1,'failed_executions':0,
            'reruns':0,'old_or_peer_producer_execution_or_import':0,'external_Lean':0,
            'checks':checks,'actual_original_S_cases':len(saved),'profiles_per_case':5,
            'cases':saved,'global_credit_counterexamples':invalid,'affine_certificate':affine,
            'scope':'finite original-S selected jet ranks and exact affine guard; no auxiliary unit calculation; not the all-scale proof'}
    OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'checks':checks,'cases':len(saved),
                      'counterexamples':len(invalid),'gain':affine['gain_total']}))
except BaseException as exc:
    OUT.write_text(json.dumps({'status':'FAILED_FIRST_ONLY','first_execution_count':1,
                              'reruns':0,'checks_before_failure':checks,'error':repr(exc)},indent=2)+'\n',encoding='utf-8')
    raise
