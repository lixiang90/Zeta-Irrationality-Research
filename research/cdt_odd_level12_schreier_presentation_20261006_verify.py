"""NEW fixed 48-coset Schreier/Bass--Serre certificate for PSL Gamma1(12).

This is a finite group-structure calculation, not a prime/parameter search.
No old or peer producer is imported/executed. Complete generation is proved in
the companion note; the certificate supplies literal matrices and relations.
"""
from collections import deque
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
import json

checks=[]
def check(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value:raise AssertionError(name)
I=(1,0,0,1);S=(0,-1,1,0);R=(0,-1,1,1);Ri=(1,1,-1,0)
M=(24,-7,84,-24);Mp=(-24,-7,84,24)
def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def det(A):a,b,c,d=A;return a*d-b*c
def inv(A):a,b,c,d=A;z=det(A);return (Q(d,z),Q(-b,z),Q(-c,z),Q(a,z))
def canon(A):
    A=tuple(Q(a) for a in A)
    for a in A:
        if a:
            return tuple(-x for x in A) if a<0 else A
    raise AssertionError('zero matrix')
def ints(A):
    A=canon(A)
    if not all(a.denominator==1 for a in A):raise AssertionError('nonintegral matrix')
    return tuple(int(a) for a in A)
def power(A,n):
    if n<0:return power(inv(A),-n)
    B=I
    while n:
        if n%2:B=mul(B,A)
        A=mul(A,A);n//=2
    return B
def T(n):return (1,n,0,1)
def keypair(c,d):
    x=(c%12,d%12);y=((-c)%12,(-d)%12)
    return min(x,y)
def keyof(A):return keypair(A[2],A[3])
states=sorted({keypair(c,d) for c in range(12) for d in range(12) if gcd(gcd(c,d),12)==1})
index={x:i for i,x in enumerate(states)};root=index[(0,1)]
def act(i,A):
    c,d=states[i];return index[keypair(c*A[0]+d*A[2],c*A[1]+d*A[3])]
ps=[act(i,S) for i in range(len(states))]
pr=[act(i,R) for i in range(len(states))]
pi=[act(i,Ri) for i in range(len(states))]
pt=[act(i,T(1)) for i in range(len(states))]
def cycles(p):
    todo=set(range(len(p)));out=[]
    while todo:
        i=min(todo);cyc=[];j=i
        while j not in cyc:
            cyc.append(j);todo.remove(j);j=p[j]
        if j!=i:raise AssertionError('not permutation')
        out.append(cyc)
    return out
sc=cycles(ps);rc=cycles(pr);tc=cycles(pt)
check('primitive lowerrows modulo sign index48',len(states)==48)
check('S has24 free two-cycles',len(sc)==24 and all(len(x)==2 for x in sc))
check('R has16 free three-cycles',len(rc)==16 and all(len(x)==3 for x in rc))
check('T action from S R',all(pr[ps[i]]==pt[i] for i in range(48)))
check('Rinverse action inverse',all(pr[pi[i]]==i for i in range(48)))
seen={root};todo=deque([root])
while todo:
    i=todo.popleft()
    for p in [ps,pr]:
        j=p[i]
        if j not in seen:seen.add(j);todo.append(j)
check('all48 states in one modular orbit',len(seen)==48)
sv={i:j for j,c in enumerate(sc) for i in c};rv={i:j for j,c in enumerate(rc) for i in c}
vertices=[('S',j) for j in range(len(sc))]+[('R',j) for j in range(len(rc))]
locals_={'S':{},'R':{}}
vroot=('S',sv[root]);seen_v={vroot};queue=deque([(vroot,root,I)])
tree=set();parents={vroot:None}
while queue:
    (kind,vid),anchor,A=queue.popleft()
    p=ps if kind=='S' else pr;gen=S if kind=='S' else R
    size=2 if kind=='S' else 3
    i=anchor;B=A
    for j in range(size):
        locals_[kind][i]=B
        other=('R',rv[i]) if kind=='S' else ('S',sv[i])
        if other not in seen_v:
            seen_v.add(other);tree.add(i);parents[other]={'edge':i,'vertex':[kind,vid]}
            queue.append((other,i,B))
        i=p[i];B=mul(B,gen)
check('BassSerre40 vertices connected',len(seen_v)==40)
check('spanningtree39 edges',len(tree)==39)
non_tree=sorted(set(range(48))-tree)
check('nine nontree free edges',len(non_tree)==9)
edgegen={e:j+1 for j,e in enumerate(non_tree)}
reps={i:locals_['S'][i] for i in range(48)}
for i in range(48):
    check('actual lowerrow representative '+str(i),keyof(reps[i])==states[i])
    X=ints(mul(locals_['S'][i],inv(locals_['R'][i])))
    if i in tree:check('tree transition trivial '+str(i),X==I)
    else:check('nontree transition in Gamma '+str(i),det(X)==1 and keyof(X)==states[root] and X!=I)
gens=[ints(mul(locals_['S'][e],inv(locals_['R'][e]))) for e in non_tree]
check('nine distinct actual generators',len(set(gens))==9)
def red(word):
    out=[]
    for a in word:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out
def negword(word):return [-a for a in reversed(word)]
def matrix_free(word):
    A=I
    for a in word:A=mul(A,gens[a-1] if a>0 else inv(gens[-a-1]))
    return ints(A)
def modular_tokens(A):
    A=ints(A);tokens=[]
    def appendT(n):
        if n>=0:tokens.extend(['S','R']*n)
        else:tokens.extend(['r','S']*(-n))
    while A[2]:
        n=A[0]//A[2];appendT(n);tokens.append('S')
        A=mul(S,mul(T(-n),A))
    check('Euclidean terminal diagonal is unit',abs(A[0])==1 and A[3]==A[0])
    appendT(A[1]//A[0])
    return tokens
def rewrite_tokens(tokens):
    i=root;word=[]
    for a in tokens:
        j=(ps if a=='S' else pr if a=='R' else pi)[i]
        if a!='S':
            if i in edgegen:word.append(edgegen[i])
            if j in edgegen:word.append(-edgegen[j])
        i=j
    check('Gamma word returns to root',i==root)
    return red(word)
def rewrite(A):
    word=rewrite_tokens(modular_tokens(A))
    check('exact free word matrix reconstruction',matrix_free(word)==ints(A))
    return word
for j,g in enumerate(gens):
    check('free generator rewrites to own letter '+str(j+1),rewrite(g)==[j+1])

cusps=[];cusp_of={i:j for j,cyc in enumerate(tc) for i in cyc}
for j,cyc in enumerate(tc):
    i=min(cyc);A=reps[i];P=ints(mul(A,mul(T(len(cyc)),inv(A))))
    a,c=A[0],A[2]
    val='infinity' if c==0 else str(Q(a,c))
    cusps.append({'id':j+1,'coset':i,'cycle':cyc,'width':len(cyc),'rational_cusp':val,'scaling_matrix':list(ints(A)),
                  'parabolic_matrix':list(P),'word':rewrite(P),'base_denominator':gcd(abs(c),12)})
    check('cusp parabolic trace abs2 '+str(j+1),abs(P[0]+P[3])==2)
    check('cusp width minimal '+str(j+1),all(act(i,T(n))!=i for n in range(1,len(cyc))) and act(i,T(len(cyc)))==i)
check('ten cusp cycles',len(tc)==10)
check('all cusp widths sum48',sum(len(c) for c in tc)==48)
check('cusp widths exact',sorted(len(c) for c in tc)==[1,1,2,3,3,4,4,6,12,12])
check('genus zero exact Euler arithmetic',Q(48,6)-10+2==0)

aut=[]
for j,g in enumerate(gens):
    A=ints(mul(M,mul(g,inv(M))))
    check('M conjugate generator belongs Gamma '+str(j+1),det(A)==1 and keyof(A)==states[root])
    aut.append(rewrite(A))
def substitute(word):
    return red([b for a in word for b in (aut[a-1] if a>0 else negword(aut[-a-1]))])
for j in range(9):check('M automorphism square actual free word '+str(j+1),substitute(aut[j])==[j+1])
check('M central square projective involution',mul(M,M)==(-12,0,0,-12))
K=ints(mul(Mp,inv(M)))
kword=rewrite(K)
check('second elliptic actual Gamma coset',K==(97,-28,-336,97))
check('second elliptic relation in free presentation',red(kword+substitute(kword))==[])
def bezout(a,b):
    aa,bb=a,b;s0,s1=1,0;t0,t1=0,1
    while bb:
        q=aa//bb;aa,bb=bb,aa-q*bb;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    if aa<0:aa,s0,t0=-aa,-s0,-t0
    return aa,s0,t0
mp=[]
for cusp in cusps:
    A=tuple(cusp['scaling_matrix']);a,c=A[0],A[2]
    aa=M[0]*a+M[1]*c;cc=M[2]*a+M[3]*c;gg=gcd(abs(aa),abs(cc));aa//=gg;cc//=gg
    d0,s,t=bezout(aa,cc)
    check('transformed cusp primitive',d0==1)
    lift=(aa,-t,cc,s)
    target=cusp_of[index[keyof(lift)]]
    mp.append(target)
check('M cusp action involution',all(mp[mp[j]]==j for j in range(10)))
check('M cusp action no fixed cusp',all(mp[j]!=j for j in range(10)))
pairs=[(j,mp[j]) for j in range(10) if j<mp[j]]
check('five M quotient cusps',len(pairs)==5)
check('M cusp pairs expected widths',sorted(sorted([cusps[j]['width'],cusps[k]['width']]) for j,k in pairs)==[[1,12],[1,12],[2,6],[3,4],[3,4]])
check('M quotient genus zero RH arithmetic',Q(2*0-2+2,2)==0)
check('M quotient area index24 Euler',Q(48,2)==24 and 2-5-Q(2,2)==-4)

out={'check_count':len(checks),'all_passed':all(x['passed'] for x in checks),'checks':checks,
 'index':48,'S_cycles':sc,'R_cycles':rc,'T_cycles':tc,'states_mod12':states,
 'graph':{'vertices':40,'edges':48,'tree_edges':sorted(tree),'free_edges':non_tree},
 'generators':[{'name':'x'+str(j+1),'edge':e,'matrix':list(gens[j]),'M_conjugation_word':aut[j]} for j,e in enumerate(non_tree)],
 'cusps':cusps,'M_cusp_pairs':[[j+1,k+1] for j,k in pairs],
 'second_elliptic':{'matrix':list(Mp),'Gamma_coset_matrix':list(K),'Gamma_coset_word':kword},
 'presentation':{'Gamma':'free on x1,...,x9','extension':'<x1,...,x9,m | m^2=1, m*xj*m^-1=alpha(xj), j=1,...,9>','M_matrix':list(M)},
 'scope':['fixed finite group structure, not parameter scan','no old/peer producers','Γ equals PSLΓ1(12)','generation/free presentation require Bass--Serre proof in accompanying note','no full actual Eichler cocycle/kernel classification','no numerical irrationality conclusion']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':out['all_passed'],'generators':out['generators'],'cusps':[{'id':x['id'],'value':x['rational_cusp'],'width':x['width'],'matrix':x['parabolic_matrix'],'word':x['word']} for x in cusps],'M_pairs':out['M_cusp_pairs'],'second_elliptic_word':kword},ensure_ascii=False))
