"""Exact local Newton/initial-form analysis of the saved two-moment pencil.

All lower-envelope edges and vertices in the nonnegative valuation quadrant
are enumerated by exact one-dimensional half-space intersection.  Initial
forms are entire polynomials in X, not scalar coefficient-content samples.
"""
import json,math,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q

sys.set_int_max_str_digits(0)
PRIMES=[2,3,5,7,11,13]


def vp(q,p):
    if not q:return None
    n,d=abs(int(q.numerator)),int(q.denominator);v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v


def unit(q,p):
    n,d=int(q.numerator),int(q.denominator)
    while n%p==0:n//=p
    while d%p==0:d//=p
    return n*pow(d,-1,p)%p


def supports(terms):
    """Return every nonsingleton minimal support at finite a,b>=0."""
    found={}
    def add(a,b,reason):
        assert a>=0 and b>=0
        values=[F(v)+i*a+j*b for i,j,v in terms];mn=min(values)
        support=tuple(k for k,val in enumerate(values) if val==mn)
        if len(support)>1:
            found.setdefault(support,dict(a=str(a),b=str(b),reason=reason,min_weight=str(mn)))
    add(F(0),F(0),'origin')
    for u,(i,j,v) in enumerate(terms):
        for w in range(u+1,len(terms)):
            ii,jj,vv=terms[w]
            di,dj,d= i-ii,j-jj,vv-v
            if dj:
                # a=t, b=B0+B1*t.
                A0,A1=F(0),F(1);B0,B1=F(d,dj),F(-di,dj)
            else:
                assert di
                A0,A1=F(d,di),F(0);B0,B1=F(0),F(1)
            low,high=F(0),None;possible=True
            constraints=[(A1,A0),(B1,B0)]
            for r,s,z in terms:
                constraints.append(((r-i)*A1+(s-j)*B1,F(z-v)+(r-i)*A0+(s-j)*B0))
            for alpha,beta in constraints:
                if alpha>0:low=max(low,-beta/alpha)
                elif alpha<0:
                    bound=-beta/alpha
                    high=bound if high is None else min(high,bound)
                elif beta<0:possible=False;break
            if not possible or high is not None and low>high:continue
            samples=[low]
            if high is None:samples.append(low+1)
            else:samples.extend([high,(low+high)/2])
            for t in samples:add(A0+A1*t,B0+B1*t,dict(pair=[u,w],interval=[str(low),str(high)]))
    return found


def initial_roots(polys,indices,p):
    roots=[]
    for u in range(1,p):
        for v in range(1,p):
            vec=[0]*38
            for index in indices:
                i,j,co=polys[index]
                scalar=pow(u,i,p)*pow(v,j,p)%p
                for k,a in enumerate(co):vec[k]=(vec[k]+scalar*a)%p
            if not any(vec):roots.append([u,v])
    return roots


def main():
    path=Path(__file__).with_name('zeta7_two_moment_partial_20261004_coefficients.json')
    raw=path.read_bytes();d=json.loads(raw)
    coeff=[(r['i'],r['j'],[Q(c) for c in r['polynomial_coefficients']]) for r in d['coefficients']]
    results=[]
    for p in PRIMES:
        terms=[];ip=[]
        for i,j,cs in coeff:
            v=min(vp(c,p) for c in cs if c)
            terms.append((i,j,v))
            ip.append((i,j,[unit(c,p) if c and vp(c,p)==v else 0 for c in cs]))
        face_data=[]
        for indices,witness in supports(terms).items():
            roots=initial_roots(ip,indices,p)
            face_data.append(dict(support=[list(terms[k][:2]) for k in indices],
                                  witness=witness,unit_roots=roots,
                                  initial_polynomials=[dict(i=ip[k][0],j=ip[k][1],X_coefficients=ip[k][2]) for k in indices]))
        v0=terms[0][2]
        amin=max(0,max(math.ceil(F(v0-v,i)) for i,j,v in terms if i and not j))
        boundary=[]
        for a in range(amin,amin+25):
            bmin=max(0,max(math.ceil(F(v0-v-i*a,j)) for i,j,v in terms if j))
            boundary.append([a,bmin])
        result=dict(p=p,coefficient_content_valuations=[dict(i=i,j=j,v=v) for i,j,v in terms],
                    baseline_content_valuation=v0,
                    minimum_face_count=len(face_data),faces=face_data,
                    cancellation_face_count=sum(bool(r['unit_roots']) for r in face_data),
                    all_initial_unit_roots_absent=not any(r['unit_roots'] for r in face_data),
                    termwise_protection_minimum_x_valuation=amin,
                    termwise_protection_boundary=boundary)
        results.append(result)
        print('p',p,'faces',len(face_data),'cancellation',result['cancellation_face_count'],
              'minimum x',amin,'boundary',boundary[:5],flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,moments=[47,55],
                 source_coefficients_sha256=hashlib.sha256(raw).hexdigest(),results=results,
                 scope='All finite lower-envelope faces for real nonnegative valuations are enumerated; '
                       'the unit-root tests concern all residue units for each given small prime. '
                       'They imply exact content valuations only on faces without unit roots. '
                       'No statement about negative valuations or p=17 is made here.')
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
