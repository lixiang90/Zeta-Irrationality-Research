"""Construct two Hensel corrections from explicit polynomial model directions.

Uses field images/cokernels, not the higher Smith decomposition. The two
obstruction row spaces are compared with evaluations and Laurent residues.
All conclusions about actual matrices here are finite parameter certificates.
"""
import argparse,json,time
from pathlib import Path
from flint import nmod_mat,nmod_poly,fmpq_poly,fmpq_mat
from six_pole_kernel import matrix
from coupled_schur import pivot_columns
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import residue


def as_rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def field(M,p):return nmod_mat(M.nrows(),M.ncols(),[int(M[i,j])%p for i in range(M.nrows()) for j in range(M.ncols())],p)
def lift(M,mod):return nmod_mat(M.nrows(),M.ncols(),[int(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols())],mod)
def block(M,rs,cs,p):return nmod_mat(len(rs),len(cs),[int(M[i,j])%p for i in rs for j in cs],p)
def join(A,B,p):
    assert A.nrows()==B.nrows()
    return nmod_mat(A.nrows(),A.ncols()+B.ncols(),[int(M[i,j]) for i in range(A.nrows()) for M in [A,B] for j in range(M.ncols())],p)
def same_rowspace(A,B,p):
    if A.ncols()!=B.ncols():return False
    return A.rank()==B.rank()==join(A.transpose(),B.transpose(),p).rank()


class FieldImage:
    def __init__(self,M,p):
        self.M=M;self.p=p;self.cols=pivot_columns(M);self.rank=len(self.cols)
        n=M.nrows();self.rows=pivot_columns(block(M,range(n),self.cols,p).transpose())
        self.free=[i for i in range(n) if i not in self.rows]
        self.inverse=block(M,self.rows,self.cols,p).inv() if self.rank else None
    def quotient(self,F):
        if not self.rank:return F
        p=self.p;cs=range(F.ncols())
        return block(F,self.free,cs,p)-block(self.M,self.free,self.cols,p)*self.inverse*block(F,self.rows,cs,p)
    def solve(self,F):
        assert not self.quotient(F),'target is not in the image'
        Y=nmod_mat(self.M.ncols(),F.ncols(),[0]*(self.M.ncols()*F.ncols()),self.p)
        if self.rank:
            W=self.inverse*block(F,self.rows,range(F.ncols()),self.p)
            for i,k in enumerate(self.cols):
                for j in range(F.ncols()):Y[k,j]=W[i,j]
        assert self.M*Y==F
        return Y


def divided(M,p,power):
    divisor=p**power
    assert all(int(M[i,j])%divisor==0 for i in range(M.nrows()) for j in range(M.ncols()))
    return nmod_mat(M.nrows(),M.ncols(),[int(M[i,j])//divisor%p for i in range(M.nrows()) for j in range(M.ncols())],p)


def run(p,N,a,center=1,example=False):
    K=3*p-1-a;h=K-N;d=3*N-p+1;precision=6;mod=p**precision
    assert mod<2**64
    rows,B,u,v=matrix(K,N,p,a,center,precision);M=nmod_mat(rows,mod);M0=field(M,p)
    basis,_,tags=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    phi=fmpq_poly([0,0,1])*(Dcache((p-1)//2)**8//Dcache(N)**5)
    n1=N-a+d;polys=[phi*fmpq_poly([0]*k+[1]) for k in range(n1)]
    co=C.transpose().solve(fmpq_mat(h,n1,[q[i] for i in range(h) for q in polys]))
    Z=nmod_mat(h,n1,[residue(co[i,k],p,-v[i],precision) for i in range(h) for k in range(n1)],mod)
    assert field(Z,p).rank()==n1 and not M0*field(Z,p)
    I0=FieldImage(M0,p)
    assert h-I0.rank==n1,'first model is not the full kernel at this parameter'
    F1=divided(M*Z,p,1);O1=I0.quotient(F1)
    value_factorization=all(int(F1[i,k])==(int(F1[i,0])*pow((-tag['c']**2)%p,k,p))%p
                            for i,tag in enumerate(tags) for k in range(n1))
    E=nmod_mat(N-a,n1,[pow((-j*j)%p,k,p) for j in range(a+1,N+1) for k in range(n1)],p)
    assert same_rowspace(O1,E,p)
    J=Dcache(N)//Dcache(a)
    mult=nmod_mat(n1,d,[int(J[i-j]) if 0<=i-j<len(J) else 0 for i in range(n1) for j in range(d)],mod)
    Z2=Z*mult;Y=I0.solve(-divided(M*Z2,p,1));Q2=Z2+p*lift(Y,mod)
    # A lower-dimensional polynomial ansatz for the first correction.
    # Failure would not affect the general Hensel certificate above.
    m=(p-1)//2;theta=phi//Dcache(m)
    trial_polys=[theta*fmpq_poly([0]*k+[1]) for k in range(m)]
    trial_co=C.transpose().solve(fmpq_mat(h,m,[q[i] for i in range(h) for q in trial_polys]))
    trial=nmod_mat(h,m,[residue(trial_co[i,k],p,-v[i]) for i in range(h) for k in range(m)],p)
    trial_image=FieldImage(M0*trial,p);trial_target=-divided(M*Z2,p,1)
    trial_ok=not trial_image.quotient(trial_target)
    trial_coefficients=as_rows(trial_image.solve(trial_target)) if trial_ok else None
    F2=divided(M*Q2,p,2)
    H=join(M0,F1,p);I1=FieldImage(H,p);O2=I1.quotient(F2)
    assert h-I1.rank==d
    da=nmod_poly([int(c)%p for c in Dcache(a)],p);mom=[]
    for k in range(2*d-1):mom.append(0 if a==0 else int((nmod_poly([0]*k+[1],p)%da)[a-1]))
    Laurent=nmod_mat(d,d,[mom[i+j] for i in range(d) for j in range(d)],p)
    assert same_rowspace(O2,Laurent,p)
    radical=[da*nmod_poly([0]*k+[1],p) for k in range(d-a)] if a<=d else [nmod_poly([0]*k+[1],p) for k in range(min(d,a-d))]
    r=len(radical);Z3=None
    if r:
        R=nmod_mat(d,r,[int(q[i]) for i in range(d) for q in radical],p)
        base=Q2*lift(R,mod);target=-divided(M*base,p,2)
        solved=I1.solve(target)
        W=block(solved,range(h),range(r),p)
        T=block(solved,range(h,h+n1),range(r),p)
        Z3=base+p**2*lift(W,mod)+p*Z*lift(T,mod)
        divided(M*Z3,p,3)
        assert field(Z3,p).rank()==r
    result=dict(p=p,N=N,a=a,center=center,h=h,d=d,
                first_obstruction_shape=[O1.nrows(),O1.ncols()],first_obstruction_rank=O1.rank(),
                first_rowspace_equals_evaluation=True,raw_first_obstruction_local_values=value_factorization,
                second_obstruction_shape=[O2.nrows(),O2.ncols()],second_obstruction_rank=O2.rank(),
                second_rowspace_equals_Laurent=True,second_lifts=d,third_lifts=r,
                second_lifts_verified_mod_p2=True,third_lifts_verified_mod_p3=True,
                reduced_correction_space_dimension=m,reduced_correction_image_rank=trial_image.rank,
                reduced_correction_succeeds=trial_ok)
    if example and r:
        result['certificate']=dict(modulus=p**3,M=[[x%p**3 for x in row] for row in rows],
                                   Z3=[[int(Z3[i,j])%p**3 for j in range(r)] for i in range(h)],
                                   first_obstruction=as_rows(O1),second_obstruction=as_rows(O2),
                                   Laurent=as_rows(Laurent),reduced_first_correction_coefficients=trial_coefficients)
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--triples',default='11:4:0,11:4:1,11:4:2,11:4:3,11:4:4,13:5:0,13:5:2,13:5:4,13:5:5,17:6:1,17:6:3,17:6:5,43:16:3,43:16:7,53:18:1,53:18:3')
    args=ap.parse_args();results=[];start=time.time()
    for item in args.triples.split(','):
        p,N,a=map(int,item.split(':'));r=run(p,N,a,example=(p,N,a)==(11,4,1));results.append(r)
        Path(__file__).with_suffix('.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in r.items() if k!='certificate'})+f' time={time.time()-start:.1f}',flush=True)
