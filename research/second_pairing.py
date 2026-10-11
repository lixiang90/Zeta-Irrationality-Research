"""Exact certificates for the uniform proof in third_layer_analysis.md.

Hermite interpolation separates the first residue matrix into small local
blocks. These blocks supply the Hensel corrections; no higher Smith vectors
are used as input. A finite run is not itself the uniform proof.
"""
import argparse,json,time
from pathlib import Path
from flint import fmpq_poly,fmpq_mat,nmod_mat,nmod_poly
from six_pole_kernel import matrix
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import residue
from kernel_hensel import field,block,lift,divided,FieldImage,as_rows,same_rowspace
import sympy as sp


def symbolic_models():
    H=sp.Symbol('H');nodes=[0,1,-1,-2,2]
    den={z:sp.prod(z-y for y in nodes if y!=z) for z in nodes}
    weights={-1:1,2:1,-2:H}
    def S(k):return sum(sp.Rational(z**k,den[z]) for z in nodes)
    def C(k):return sum(w*sp.Rational(z**k,den[z]) for z,w in weights.items())
    T=[sp.factor(C(8+s)+S(s+2)/6+S(s+1)/2+7*S(s)/12) for s in range(7)]
    V=sp.Matrix(3,3,lambda i,j:T[i+j]);w=sp.Matrix(T[3:6])
    correction=sp.factor(-(w.T*V.inv()*w)[0])
    naive=sp.factor(sp.Rational(7,10)-T[6]);kappa=sp.factor(naive-correction)
    origin=sp.Matrix([[(256*H-3)/12,-sp.Rational(2,3)],[-sp.Rational(2,3),-sp.Rational(17,12)]])
    for expr in [V.det(),origin.det(),kappa]:
        num,_=sp.fraction(sp.factor(expr))
        assert sp.Poly(num,H).content()==1
    return H,T,origin,dict(truncated_moments=[str(t) for t in T],
        truncated_determinant=str(sp.factor(V.det())),origin_determinant=str(sp.factor(origin.det())),
        naive_scalar=str(naive),correction_scalar=str(correction),second_scalar=str(kappa))


def local_solve(normal,target,p):
    P=normal['P'];nf=normal['normal'];rhs=P.transpose()*target
    Y=nmod_mat(nf.nrows(),target.ncols(),[0]*(nf.nrows()*target.ncols()),p)
    for _,_,ii in normal['blocks']:
        sol=block(nf,ii,ii,p).inv()*block(rhs,ii,range(target.ncols()),p)
        for i,k in enumerate(ii):
            for j in range(target.ncols()):Y[k,j]=sol[i,j]
    assert nf*Y==rhs,'target has a component in the radical'
    return P*Y


def mod_expr(expr,H,hv,p):
    value=sp.cancel(expr.subs(H,hv));num,den=sp.fraction(value)
    return int(num)%p*pow(int(den),-1,p)%p


def unit_inverse(A,p,precision):
    mod=p**precision;n=A.nrows()
    J=lift(field(A,p).inv(),mod)
    I=nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],mod)
    accuracy=1
    while accuracy<precision:
        J=J*(2*I-A*J);accuracy*=2
    assert A*J==I
    return J


def setup(p,N,a,center=1,precision=6):
    assert sp.isprime(p) and p>=11 and (p+2)//3<=N<=3*p//8 and 0<=a<=N
    K=3*p-1-a;h=K-N;d=3*N-p+1;n=N-a+d;mod=p**precision
    assert mod<2**64
    rows,_,u,v=matrix(K,N,p,a,center,precision)
    M=nmod_mat(rows,mod)
    basis,_,tags=local_basis(K,N,p)
    S=[i for i,t in enumerate(tags) if (t['c']>N and t['i']<4) or (a<t['c']<=N and t['i']<3)]
    R=[i for i in range(h) if i not in S]
    assert all(u[i]-v[i]==1 for i in R)
    U=block(M,S,S,mod)
    if field(U,p).rank()!=len(S):return None
    A=block(M,R,R,mod)-block(M,R,S,mod)*unit_inverse(U,p,precision)*block(M,S,R,mod)
    assert A==A.transpose()
    assert field(A,p)==block(M,R,R,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    phi=fmpq_poly([0,0,1])*(Dcache((p-1)//2)**8//Dcache(N)**5)
    qs=[phi*fmpq_poly([0]*k+[1]) for k in range(n)]
    co=C.transpose().solve(fmpq_mat(h,n,[q[i] for i in range(h) for q in qs]))
    B=nmod_mat(len(R),n,[residue(co[i,k],p,-v[i],precision) for i in R for k in range(n)],mod)
    assert field(B,p).rank()==n and not field(A,p)*field(B,p)
    J=Dcache(N)//Dcache(a)
    mult=nmod_mat(n,d,[int(J[i-j]) if 0<=i-j<len(J) else 0 for i in range(n) for j in range(d)],mod)
    return dict(M=M,A=A,B=B,J=mult,tags=[tags[i] for i in R],h=h,n=n,d=d,u=u,v=v,
                basis=[basis[i] for i in R],column_weights=[v[i] for i in R])


def local_normal_form(z,p,N,a,center):
    """Hermite interpolation separates the residue matrix into local blocks."""
    tags=z['tags'];rr=len(tags);mod=p**6
    A0=field(z['A'],p);m=(p-1)//2;n=z['n']
    visible=[i for i,v in enumerate(z['column_weights']) if v==0]
    hidden=[i for i,v in enumerate(z['column_weights']) if v<0]
    assert len(visible)==2*N+1
    f=nmod_poly([int(c)%p for c in Dcache(m)],p)
    dn=nmod_poly([int(c)%p for c in Dcache(N)],p)
    da=nmod_poly([int(c)%p for c in Dcache(a)],p)
    t=nmod_poly([0,1],p);outer=f//dn
    chi=t*f**6//(dn**3*da)
    polys=[]
    for i in visible:
        quotient,rem=divmod(nmod_poly([int(c)%p for c in z['basis'][i]],p),chi)
        assert not rem;polys.append(quotient)
    coordinates=nmod_mat(2*N+1,2*N+1,[int(q[k]) for k in range(2*N+1) for q in polys],p).inv()
    specs=[('zero',0,0)]+[('inner',c,0) for c in range(1,a+1)]
    specs += [('outer',c,j) for c in range(N+1,m+1) for j in [0,1]]
    s=len(specs)
    E=nmod_mat(s,2*N+1,[int(k==0) if typ=='zero' else
        (pow(-c*c,k,p) if derivative==0 else (0 if k==0 else k*pow(-c*c,k-1,p)%p))
        for typ,c,derivative in specs for k in range(2*N+1)],p)
    coeff=nmod_mat(2*N+1,s,[0]*((2*N+1)*s),p)
    inv=block(E,range(s),range(s),p).inv()
    for i in range(s):
        for j in range(s):coeff[i,j]=inv[i,j]
    radical=t*da*outer**2
    rad=nmod_mat(2*N+1,n,[int(radical[i-j]) if i>=j else 0 for i in range(2*N+1) for j in range(n)],p)
    assert not E*rad
    P=nmod_mat(rr,rr,[0]*(rr*rr),p)
    for j,i in enumerate(hidden):P[i,j]=1
    visible_co=coordinates*coeff;rad_co=coordinates*rad
    for k,i in enumerate(visible):
        for j in range(s):P[i,len(hidden)+j]=visible_co[k,j]
        for j in range(n):P[i,len(hidden)+s+j]=rad_co[k,j]
    assert P.rank()==rr
    normal=P.transpose()*A0*P
    index=lambda c,i:next(k for k,tg in enumerate(tags) if tg['c']==c and tg['i']==i)
    hid=lambda c,i:hidden.index(index(c,i))
    jet=lambda typ,c,d=0:len(hidden)+specs.index((typ,c,d))
    blocks=[('zero',0,[hid(0,0),jet('zero',0)])]
    blocks += [('inner',c,[hid(c,0),hid(c,1),jet('inner',c)]) for c in range(1,a+1)]
    blocks += [('outer',c,[hid(c,4),hid(c,5),jet('outer',c),jet('outer',c,1)]) for c in range(N+1,m+1)]
    labels={i:k for k,(_,_,ii) in enumerate(blocks) for i in ii}
    assert all(not normal[i,j] for i in range(rr) for j in range(rr) if i not in labels or j not in labels or labels[i]!=labels[j])
    H,T,origin,symbols=symbolic_models();hv=(129*pow(128,-1,p)+center)%p
    ts=[mod_expr(x,H,hv,p) for x in T]
    origins=nmod_mat(2,2,[mod_expr(x,H,hv,p) for x in origin],p)
    for typ,c,ii in blocks:
        actual=block(normal,ii,ii,p)
        if typ=='outer':
            assert not block(actual,range(2),range(2),p)
            cross=block(actual,range(2),range(2,4),p)
            assert cross[1,1]==0 and cross[0,1] and cross[1,0] and actual[3,3]==0
        else:
            if typ=='zero':
                amp=int(P[index(0,1),jet('zero',0)]);scales=[1,amp]
                model=origins
            else:
                amp=int(P[index(c,2),jet('inner',c)]);scales=[1,2*c,(2*c)**2*amp]
                model=nmod_mat(3,3,[ts[i+j] for i in range(3) for j in range(3)],p)
            expected=nmod_mat(len(ii),len(ii),[int(model[i,j])*scales[i]*scales[j]%p for i in range(len(ii)) for j in range(len(ii))],p)
            pivot=next((i,j) for i in range(len(ii)) for j in range(len(ii)) if expected[i,j])
            unit=int(actual[pivot[0],pivot[1]])*pow(int(expected[pivot[0],pivot[1]]),-1,p)%p
            assert unit and actual==unit*expected,('local block mismatch',typ,c,as_rows(actual),as_rows(expected))
    return dict(P=P,normal=normal,blocks=blocks,symbolic=symbols,
                ranks=[dict(kind=typ,c=c,rank=block(normal,ii,ii,p).rank(),size=len(ii)) for typ,c,ii in blocks])


def laurent(a,d,p):
    da=nmod_poly([int(c)%p for c in Dcache(a)],p)
    mm=[0 if a==0 else int((nmod_poly([0]*k+[1],p)%da)[a-1]) for k in range(2*d-1)]
    return nmod_mat(d,d,[mm[i+j] for i in range(d) for j in range(d)],p)


def run(p,N,a,center=1,example=False):
    z=setup(p,N,a,center)
    if z is None:return dict(p=p,N=N,a=a,center=center,status='singular local block')
    A,B,J=z['A'],z['B'],z['J'];d=z['d'];n=z['n'];mod=p**6
    A0=field(A,p);I=FieldImage(A0,p)
    normal=local_normal_form(z,p,N,a,center)
    result=dict(p=p,N=N,a=a,center=center,reduced_size=A.nrows(),n=n,d=d,
                symmetric_reduction=True,first_nullity=A.nrows()-I.rank,
                local_normal_form_verified=True,local_ranks=normal['ranks'])
    C1=divided(B.transpose()*A*B,p,1)
    result['first_pairing_rank']=C1.rank()
    if any(r['rank']<r['size'] for r in normal['ranks']):
        result['status']='singular normal form; use the generic parameter field'
        return result
    Z=B*J;target=-divided(A*Z,p,1)
    if I.quotient(target):
        result.update(status='second lift obstructed at this specialization',residual_rank=I.quotient(target).rank())
        return result
    Y=local_solve(normal,target,p)
    assert A0*Y==target
    Q=Z+p*lift(Y,mod)
    F2=divided(A*Q,p,2)
    C2=field(Q,p).transpose()*F2
    assert C2==C2.transpose()
    naive=divided(Z.transpose()*A*Z,p,2)
    correction=Y.transpose()*A0*Y
    assert C2==naive-correction
    model=laurent(a,d,p)
    pivot=next(((i,j) for i in range(d) for j in range(d) if model[i,j]),None)
    scalar=None if pivot is None else int(C2[pivot[0],pivot[1]])*pow(int(model[pivot[0],pivot[1]]),-1,p)%p
    scalar_match=not C2 if scalar is None else C2==scalar*model
    H,T,origin,symbols=symbolic_models();hv=sp.Rational(129,128)+center
    predicted=mod_expr(sp.sympify(symbols['second_scalar']),H,hv,p)
    naive_predicted=mod_expr(sp.sympify(symbols['naive_scalar']),H,hv,p)
    correction_predicted=mod_expr(sp.sympify(symbols['correction_scalar']),H,hv,p)
    assert C2==predicted*model and naive==naive_predicted*model and correction==correction_predicted*model
    # Lift the Laurent radical one more order using C1 and the local solver.
    da=nmod_poly([int(c)%p for c in Dcache(a)],p)
    rad=[da*nmod_poly([0]*k+[1],p) for k in range(d-a)] if a<=d else [nmod_poly([0]*k+[1],p) for k in range(min(d,a-d))]
    third=None;third_status='vacuous';third_count=len(rad)
    if third_count:
        R=nmod_mat(d,third_count,[int(q[i]) for i in range(d) for q in rad],p)
        assert not C2*R
        rhs=-F2*R
        obstruction=field(B,p).transpose()*rhs
        IC=FieldImage(C1,p)
        if IC.quotient(obstruction):
            third_status='first pairing degenerates at this specialization'
        else:
            Tcorr=IC.solve(obstruction)
            Ffirst=divided(A*B,p,1)
            W=local_solve(normal,rhs-Ffirst*Tcorr,p)
            third=Q*lift(R,mod)+p*B*lift(Tcorr,mod)+p**2*lift(W,mod)
            divided(A*third,p,3)
            assert field(third,p).rank()==third_count
            third_status='verified modulo p^3'
    result.update(status='certified second lift',second_pairing_rank=C2.rank(),model_rank=model.rank(),
                  same_radical=same_rowspace(C2,model,p),scalar_multiple=scalar_match,scalar=scalar,
                  naive_rank=naive.rank(),correction_rank=correction.rank(),correction_zero=not correction,
                  universal_scalar_formula=True,predicted_scalar=predicted,local_hensel_solve=True,
                  third_directions=third_count,third_status=third_status,
                  determinant_bound=48*N-24*p+22+a-max(0,min(a,2*d-a)),
                  second_lifts_verified=True,second_pairing=as_rows(C2),model=as_rows(model))
    if example:result['certificate']=dict(A=as_rows(A),B=as_rows(B),Q=as_rows(Q),
        third=as_rows(third) if third is not None else None,modulus=mod)
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--triples',default='11:4:0,11:4:1,11:4:2,11:4:3,11:4:4,31:11:1,31:11:2,31:11:3,31:11:4,31:11:5,31:11:6,43:16:2,43:16:4,43:16:7')
    ap.add_argument('--center',type=int,default=1);ap.add_argument('--out',default='second_pairing.json')
    args=ap.parse_args();results=[];start=time.time()
    for item in args.triples.split(','):
        r=run(*map(int,item.split(':')),args.center,example=item=='11:4:1');results.append(r)
        Path(__file__).with_name(args.out).write_text(json.dumps(results,indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in r.items() if k not in ['certificate','local_ranks','second_pairing','model']})+f' elapsed={time.time()-start:.1f}',flush=True)
