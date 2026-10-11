"""Full rational Gr(2,3) tail pencils inside uniform zeta(7) mod-6 spaces.

All six quadratic coefficient polynomials, complete contents, and integer
content-bound certificates are exact.  Target values use rigorous Arb balls.
"""
import argparse, itertools, json, math, sys, time
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, fmpz_mat as ZMat, arb, arb_poly, arb_mat, ctx
from joint_exact import entries, content
from zeta7_space_extension_probe import basis, moment_layers, polynomial

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
PREFIX='zeta7_mod6_noncoordinate_20261004'
MONOMIALS=['u0^2','u1^2','u2^2','u0*u1','u0*u2','u1*u2']


def egcd(a,b):
    aa,bb=abs(a),abs(b);s0,s1,t0,t1=1,0,0,1
    while bb:
        q=aa//bb;aa,bb=bb,aa-q*bb
        s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    return aa,s0*(1 if a>=0 else -1),t0*(1 if b>=0 else -1)


def primitive(u):
    g=math.gcd(*u);assert g
    v=tuple(x//g for x in u)
    if next(x for x in v if x)<0:v=tuple(-x for x in v)
    return v


def kernel(u):
    u=primitive(u);x,y,z=u;g,a,b=egcd(x,y)
    if not g:return [(1,0,0),(0,1,0)]
    rows=[(y//g,-x//g,0),(a*z,b*z,-g)]
    cross=(rows[0][1]*rows[1][2]-rows[0][2]*rows[1][1],
           rows[0][2]*rows[1][0]-rows[0][0]*rows[1][2],
           rows[0][0]*rows[1][1]-rows[0][1]*rows[1][0])
    assert cross==u and all(sum(a*b for a,b in zip(row,u))==0 for row in rows)
    return rows


def restricted(A,ks):
    f=A.nrows()-3;h=f+2
    out=[]
    for i in range(h):
        row=[]
        for j in range(h):
            if i<f and j<f:v=A[i,j]
            elif i<f:v=sum((ks[j-f][a]*A[i,f+a] for a in range(3)),Q(0))
            elif j<f:v=sum((ks[i-f][a]*A[f+a,j] for a in range(3)),Q(0))
            else:v=sum((ks[i-f][a]*ks[j-f][b]*A[f+a,f+b] for a in range(3) for b in range(3)),Q(0))
            row.append(v)
        out.append(row)
    return Mat(out)


def exact_plane(A,B,u):
    ks=kernel(u);a,b=restricted(A,ks),restricted(B,ks)
    ans=polynomial(a,b)
    for x in (-1,0,1):assert ans(x)==(a+x*b).det()
    return ans,a,b


def monomials(u):
    x,y,z=u
    return [x*x,y*y,z*z,x*y,x*z,y*z]


def certificate(rows):
    F=ZMat(rows);H,T=F.hnf(transform=True);assert T*F==H
    inds=[i for i in range(H.nrows()) if any(H[i,j] for j in range(H.ncols()))]
    m=F.ncols();assert len(inds)==m
    B=ZMat([[int(H[i,j]) for j in range(m)] for i in inds])
    U=ZMat([[int(T[i,j]) for j in range(F.nrows())] for i in inds])
    assert U*F==B
    inv=Mat(B).inv();coords=Mat(F)*inv
    assert all(v.denominator==1 for v in coords.entries())
    d=math.lcm(*(int(v.denominator) for v in inv.entries()))
    L=ZMat([[int(inv[i,j]*d) for j in range(m)] for i in range(m)])
    C=L*U
    assert C*F==ZMat([[d if i==j else 0 for j in range(m)] for i in range(m)])
    def vals(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
    return dict(rank=m,hnf=vals(B),coefficient_to_hnf=vals(U),content_upper=str(d),
                integer_identity_multiplier=vals(C),identity='C*F=d*I',
                log_content_upper=float(arb(d).log()))


def setup(n):
    K,N,H=40*n,n,39*n;D,W,root,T=basis(K,N,H)
    c=(2*n+5)%6;used=set();R=[]
    for r in range(6):
        if r in used:continue
        s=(c-r)%6;assert s!=r
        R.append(min(r,s));used.update((r,s))
    R.sort();assert all((a+b)%6!=c for a in R for b in R)
    r=33*n-2
    keep=list(range(r))+[i for i in range(r,H) if i%6 in R]
    local,sums,layers=moment_layers(K,N,H,D,W,root)
    assert all(i+j not in sums for i in keep for j in keep)
    aa,bb=entries(K,[(N,8)],H)
    C=Mat([[T[i,j] for j in range(H)] for i in keep])
    A=C*Mat([[aa[i+j] for j in range(H)] for i in range(H)])*C.transpose()
    B=C*Mat([[bb[i+j] for j in range(H)] for i in range(H)])*C.transpose()
    h=len(keep)-1
    return dict(n=n,K=K,N=N,ambient=H,good_dimension=len(keep),dimension=h,
                good_indices=keep,head_indices=keep[:-3],tail_indices=keep[-3:],
                mod6_residues=R,forbidden_residue=c,polynomial_layers=local,
                basis_root=list(map(str,root))),A,B,aa,bb


def value_row(u,cols,theta):
    u=primitive(u);m=monomials(u)
    coefficients=[sum(cols[j][e]*m[j] for j in range(6)) for e in range(len(cols[0]))]
    g=math.gcd(*coefficients);assert g>0
    pr=[v//g for v in coefficients];value=arb_poly(pr)(theta);assert value>0
    return dict(normal=list(map(str,u)),content=str(g),log_primitive=float(value.log()),
                log_primitive_interval=value.log().str(40),
                primitive_degree=max(i for i,v in enumerate(pr) if v))


def run(n):
    start=time.perf_counter();data,A,B,aa,bb=setup(n);K,h=data['K'],data['dimension']
    norms=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]
    Ps=[]
    for u in norms:
        p,_,_=exact_plane(A,B,u);assert p.degree()<=h;Ps.append(p)
        print('K',K,'generator',u,'seconds',round(time.perf_counter()-start,2),flush=True)
    polys=Ps[:3]+[Ps[3]-Ps[0]-Ps[1],Ps[4]-Ps[0]-Ps[2],Ps[5]-Ps[1]-Ps[2]]
    den=math.lcm(*(int(c.denominator) for p in polys for c in p))
    common=math.gcd(*(int(p[e]*den) for p in polys for e in range(h+1)))
    factor=Q(common,den)
    cols=[[int(p[e]/factor) for e in range(h+1)] for p in polys]
    assert math.gcd(*(v for col in cols for v in col))==1
    data.update(common_rational_factor=str(factor),quadratic_monomials=MONOMIALS,
                coefficient_columns=[list(map(str,col)) for col in cols],
                coefficient_rank=ZMat(list(map(list,zip(*cols)))).rank(),
                generator_normals=[list(u) for u in norms])
    path=ROOT/f'{PREFIX}_n{n}.json';path.write_text(json.dumps(data,indent=2),encoding='utf-8')
    # Two non-generator normals verify every coefficient of the quadratic map.
    extra=[]
    for u in ((1,-1,1),(2,1,3)):
        p,_,_=exact_plane(A,B,u)
        expected=sum((polys[j]*monomials(u)[j] for j in range(6)),Poly())
        assert p==expected
        extra.append(dict(normal=list(u),coefficient_checks=h+1,determinant_points=['-1','0','1']))
        print('K',K,'noncoordinate coefficient check',u,flush=True)
    ctx.prec=max(abs(v).bit_length() for col in cols for v in col)+K*K+8000
    theta=arb(7).zeta();q=[arb_poly(col)(theta) for col in cols]
    M=arb_mat([[q[0],q[3]/2,q[4]/2],[q[3]/2,q[1],q[5]/2],[q[4]/2,q[5]/2,q[2]]])
    first2=arb_mat([[M[0,0],M[0,1]],[M[1,0],M[1,1]]])
    assert M[0,0]>0 and first2.det()>0 and M.det()>0
    sigmas=[M[0,0],first2.det()/M[0,0],M.det()/first2.det()]
    subsets=[[0],[0,1,3],list(range(6))];certs=[]
    for j,inds in enumerate(subsets):
        F=[[cols[i][e] for i in inds] for e in range(h+1)]
        cert=certificate(F);d=int(cert['content_upper']);bound=sigmas[j]/d;assert bound>0
        cert.update(last_nonzero_normal_coordinate=j,column_indices=inds,
                    schur_log_interval=sigmas[j].log().str(45),
                    lower_log_interval=bound.log().str(45),lower_log=float(bound.log()))
        certs.append(cert)
        print('K',K,'stratum',j,'content upper log',cert['log_content_upper'],
              'lower log',cert['lower_log'],flush=True)
    # Metric-directed candidates, including large integer normals, rather than
    # treating a small coordinate box as all of projective parameter space.
    spectral=4*M.det()/(M[0,0]+M[1,1]+M[2,2])**2;assert spectral>0
    G=ZMat([[int((M[i,j]/spectral*2**96+Q(1,2)).floor().unique_fmpz())
              for j in range(3)] for i in range(3)])
    L,T=G.lll(rep='gram',gram='exact',transform=True);assert L==T*G*T.transpose()
    vectors=set()
    for v in itertools.product(range(-2,3),repeat=3):
        if v==(0,0,0):continue
        vectors.add(primitive(v))
        vectors.add(primitive(tuple(sum(v[i]*int(T[i,j]) for i in range(3)) for j in range(3))))
    rows=[value_row(u,cols,theta) for u in sorted(vectors)]
    best=min(rows,key=lambda r:r['log_primitive'])
    # Independent same-dimension low-degree baseline, with its entire content.
    a=Mat([[aa[i+j] for j in range(h)] for i in range(h)])
    b=Mat([[bb[i+j] for j in range(h)] for i in range(h)])
    pbase=polynomial(a,b);ct=content(pbase);pr=pbase/ct
    basecoeff=[int(c.numerator) for c in pr];basevalue=arb_poly(basecoeff)(theta);assert basevalue>0
    for x in (-1,0,1):assert pbase(x)==(a+x*b).det()
    baseline=dict(dimension=h,degree=pbase.degree(),content=str(ct),
                  primitive_coefficients=list(map(str,basecoeff)),
                  log_primitive=float(basevalue.log()),log_primitive_interval=basevalue.log().str(40))
    data.update(status='full_quadratic_map_and_integer_certificates_verified',
                independent_noncoordinate_checks=extra,content_certificates=certs,
                global_family_lower_log=min(c['lower_log'] for c in certs),
                positive_metric_pivots=True,metric_approximate=[[M[i,j].str(30) for j in range(3)] for i in range(3)],
                lll_metric=[[str(G[i,j]) for j in range(3)] for i in range(3)],
                lll_transform=[[str(T[i,j]) for j in range(3)] for i in range(3)],
                candidate_count=len(rows),candidates=rows,best_candidate=best,baseline=baseline,
                best_minus_baseline=best['log_primitive']-baseline['log_primitive'],
                seconds=time.perf_counter()-start,
                scope='All rational tail planes covered by the quadratic map and uniform certificates; '
                      'metric-directed candidate search is finite, not a global optimization.')
    path.write_text(json.dumps(data,indent=2),encoding='utf-8')
    print('DONE',K,'family lower log',data['global_family_lower_log'],
          'best log',best['log_primitive'],'baseline log',baseline['log_primitive'],flush=True)
    return dict(file=path.name,n=n,K=K,dimension=h,tail=data['tail_indices'],
                global_family_lower_log=data['global_family_lower_log'],candidate_count=len(rows),
                best_log=best['log_primitive'],baseline_log=baseline['log_primitive'],
                best_minus_baseline=data['best_minus_baseline'])


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',nargs='+',type=int,default=[1,2]);args=p.parse_args()
    out=dict(status='completed',cases=[])
    for n in args.n:
        out['cases'].append(run(n))
        (ROOT/f'{PREFIX}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
