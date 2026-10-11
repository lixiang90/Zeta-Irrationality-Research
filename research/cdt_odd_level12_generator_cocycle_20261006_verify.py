"""NEW exact nine-generator period table using finite cusp kernels; no producer imports."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

checks=[]
def check(name,condition):
    passed=bool(condition)
    checks.append({'name':name,'passed':passed})
    if not passed: raise AssertionError(name)
def chi(n):
    n%=12
    return 1 if n in (1,11) else -1 if n in (5,7) else 0
def b3(x): return x**3-F(3,2)*x*x+x/2
def polyadd(p,q): return [a+b for a,b in zip(p,q)]
def polyscale(p,a): return [a*b for b in p]
def polyval(p,x): return sum(c*x**j for j,c in enumerate(p))
def determinant(g):
    a,b,c,d=g
    return a*d-b*c
def matmul(g,h):
    a,b,c,d=g; e,f,l,m=h
    return (a*e+b*l,a*f+b*m,c*e+d*l,c*f+d*m)
def inverse(g):
    a,b,c,d=g; D=determinant(g)
    return (F(d,D),F(-b,D),F(-c,D),F(a,D))
def projective_eq(g,h):
    return g==h or g==tuple(-v for v in h)
def slash(p,g):
    a,b,c,d=g; D=determinant(g); p0,p1,p2=p
    return [F(p0*d*d+p1*b*d+p2*b*b,D),
            F(2*p0*c*d+p1*(a*d+b*c)+2*p2*a*b,D),
            F(p0*c*c+p1*a*c+p2*a*a,D)]

uL={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
uZ={1:1512,2:-27216,3:1944,4:-3456,6:244944,12:-217728}
dL=2880
check('pure L source constraints',sum(uL.values())==-23*dL and sum(F(v,j**3) for j,v in uL.items())==0)
check('pure Z source constraints',sum(uZ.values())==0 and sum(F(v,j**3) for j,v in uZ.items())==-864)
boundary_cache={}
def boundary(a,k):
    """Return exact (hZ,hL)/(i*pi^3) at finite Gamma-infinity cusp a/k."""
    a%=k
    key=(a,k)
    if key in boundary_cache: return boundary_cache[key]
    check(f'finite cusp {a}/{k} admissible',k>0 and k%12==0 and chi(a)==1)
    r=k//12
    C=[F(0)]*k
    # G6: H*K+I*(H/2-J/12), implemented directly with four nonzero character terms.
    for b in (1,5,7,11):
        cb=chi(b)
        for l in range(r):
            C[(b+12*l)%k]+=cb*(F(r-1,2)-l)/r+F(cb,r)*(F(1,2)-F(b,12))
    e=F(2,3)*sum(c*b3(F((a*m)%k,k)) for m,c in enumerate(C))
    G=[F(0)]*k
    # G15: 12*A_k(x)*O_k(x^a); no extraction of any unknown real L-value.
    for b in (1,5,7,11):
        for m in range(1,k):
            G[(r*b+a*m)%k]+=12*chi(b)*(F(1,2)-F(m,k))
    f=F(2,3)*sum(c*b3(F(m,k)) for m,c in enumerate(G))
    Ts={}
    for j in (1,2,3,4,6,12):
        l=k//j
        Ts[j]=F(2,3)*sum((F(1,2)-F(m,l))*b3(F((a*m)%l,l)) for m in range(1,l))
    z=240*sum(F(v,j**3)*Ts[j] for j,v in uZ.items())
    L=240*sum(F(v,j**3)*Ts[j] for j,v in uL.items())+dL*(e+f)
    boundary_cache[key]=(z,L)
    return z,L

def interpolate(xs,ys):
    out=[F(0)]*3
    for i in range(3):
        j,l=[v for v in range(3) if v!=i]
        factor=ys[i]/((xs[i]-xs[j])*(xs[i]-xs[l]))
        out=polyadd(out,polyscale([xs[j]*xs[l],-xs[j]-xs[l],F(1)],factor))
    return out

base=Path(__file__).parent
input_path=base/'cdt_odd_level12_schreier_presentation_20261006_verify.json'
data=json.loads(input_path.read_text(encoding='utf-8-sig'))
expected=[(59,25,-144,-61),(1,1,0,1),(37,29,-60,-47),
          (11,3,-48,-13),(25,16,-36,-23),(11,9,-60,-49),
          (13,4,-36,-11),(13,6,-24,-11),(1,1,-12,-11)]
gens=[tuple(v['matrix']) for v in data['generators']]
check('input exactly the fixed nine matrices',gens==expected)
M=(24,-7,84,-24)
seed=[F(1,12*j) for j in (1,2,3,4)]
seedvalues=[boundary(1,12*j) for j in (1,2,3,4)]
tables=[]
for idx,g in enumerate(gens,1):
    a,b,c,d=g
    check(f'x{idx} Gamma matrix',determinant(g)==1 and c%12==0 and chi(d)==1)
    samples=[]
    for x in seed:
        w=c*x+d
        if not w: continue
        image=(a*x+b)/w
        v=boundary(image.numerator,image.denominator)
        old=seedvalues[seed.index(x)]
        samples.append((x,[w*w*v[s]-old[s] for s in (0,1)]))
    check(f'x{idx} at least three legal finite seeds',len(samples)>=3)
    Pz=interpolate([v[0] for v in samples[:3]],[v[1][0] for v in samples[:3]])
    Pl=interpolate([v[0] for v in samples[:3]],[v[1][1] for v in samples[:3]])
    for x,values in samples:
        check(f'x{idx} independent sample Z at{x}',polyval(Pz,x)==values[0])
        check(f'x{idx} independent sample L at{x}',polyval(Pl,x)==values[1])
    tables.append({'name':f'x{idx}','matrix':list(g),'PZ':Pz,'PL':Pl,
                   'samples':samples})

def word_cocycle(word,field):
    out=[F(0)]*3
    matrix=(1,0,0,1)
    for letter in word:
        g=gens[abs(letter)-1]
        P=tables[abs(letter)-1][field]
        if letter<0:
            g=inverse(g)
            P=polyscale(slash(P,g),-1)
        out=polyadd(slash(out,g),P)
        matrix=matmul(matrix,g)
    return matrix,out

for idx,entry in enumerate(data['generators'],1):
    word=entry['M_conjugation_word']
    matrix,Pz=word_cocycle(word,'PZ')
    _,Pl=word_cocycle(word,'PL')
    check(f'M relation projective matrix x{idx}',projective_eq(matrix,matmul(matmul(M,gens[idx-1]),inverse(M))))
    check(f'M signed cocycle Z x{idx}',Pz==polyscale(slash(tables[idx-1]['PZ'],M),-1))
    check(f'M signed cocycle L x{idx}',Pl==polyscale(slash(tables[idx-1]['PL'],M),-1))
eta=(1,0,12,1)
matrix,Pz=word_cocycle([2,-9],'PZ')
_,Pl=word_cocycle([2,-9],'PL')
check('eta actual fixed free word',matrix==eta)
check('pure Z eta zero',Pz==[F(0)]*3)
check('pure L eta full actual polynomial',Pl==[F(44160),F(529920),F(2073600)])
kword=data['second_elliptic']['Gamma_coset_word']
_,Pz=word_cocycle(kword,'PZ')
_,Pl=word_cocycle(kword,'PL')
check('Mprime Z canonical relation',Pz==[F(0)]*3)
check('Mprime L canonical relation',Pl==[F(0)]*3)

cusps=[]
for entry in data['cusps']:
    matrix,Pz=word_cocycle(entry['word'],'PZ')
    _,Pl=word_cocycle(entry['word'],'PL')
    check(f'cusp P{entry["id"]} actual projective matrix',projective_eq(matrix,tuple(entry['parabolic_matrix'])))
    cusps.append({'id':entry['id'],'cusp':entry['rational_cusp'],
                  'word':entry['word'],'matrix':entry['parabolic_matrix'],'PZ':Pz,'PL':Pl})
relation=[]
for i in (9,6,8,10,3,1,7,5,4,2):
    relation.extend(data['cusps'][i-1]['word'])
matrix,Pz=word_cocycle(relation,'PZ')
_,Pl=word_cocycle(relation,'PL')
check('complete parabolic relation projective matrix',projective_eq(matrix,(1,0,0,1)))
check('complete parabolic relation Z period',Pz==[F(0)]*3)
check('complete parabolic relation L period',Pl==[F(0)]*3)

def serial(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {k:serial(w) for k,w in v.items()}
    if isinstance(v,(list,tuple)): return [serial(w) for w in v]
    return v
result={'scope':'two actual normalized period tables, fixed complete nine-generator presentation',
        'input_json_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
        'passed':len(checks),'checks':checks,'generators':tables,'cusps':cusps,
        'boundary_count':len(boundary_cache)}
Path(__file__).with_suffix('.json').write_text(json.dumps(serial(result),indent=2),encoding='utf-8')
print(json.dumps({'passed':len(checks),'failed':0,'boundary_count':len(boundary_cache),
                  'tables':[serial({k:v for k,v in row.items() if k!='samples'}) for row in tables]}))
