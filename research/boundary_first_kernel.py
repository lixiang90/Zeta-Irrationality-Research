"""Audit a written uniform first-kernel estimate in the reduced boundary.

The estimate for G(E_i, Phi_1 R) has a direct Taylor/residue proof, recorded in
boundary_kernel_analysis.md. Integrality of the whole normalized matrix and
the deeper lifts are separately labelled finite checks, not uniform results.
"""
import argparse,json,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,nmod_mat
from boundary_structure import matrices
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import val,residue


def weights(tags):
    u=[];v=[]
    for q in tags:
        c,i=q['c'],q['i']
        u.append(1 if c==0 else (int(i>0) if q['delta'] else (-5 if i<2 else -1)))
        v.append(-2 if c and not q['delta'] else 0)
    return u,v


def analyze(p,N):
    A,B,tags,aa,bb=matrices(p,N);h=A.nrows();u,v=weights(tags)
    F=Dcache((p-1)//2);phi=fmpq_poly([0,1])*(F**6//Dcache(N)**5)
    dim=h-phi.degree();d=3*N-p+1
    assert dim==N+d and sum(u)+sum(v)==22*N-10*p+11
    basis,_,_=local_basis(2*p-1,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    Q=[phi*fmpq_poly([0]*k+[1]) for k in range(dim)]
    co=C.transpose().solve(fmpq_mat(h,dim,[q[i] for i in range(h) for q in Q]))
    AQ=A*co;BQ=B*co
    entry_margin=min(min(val(A[i,j],p),val(B[i,j],p))-u[i]-v[j]
                     for i in range(h) for j in range(h))
    kernel_margin=min(min(val(AQ[i,k],p),val(BQ[i,k],p))-u[i]-1
                      for i in range(h) for k in range(dim))
    coord_margin=min(val(co[i,k],p)+v[i] for i in range(h) for k in range(dim))
    assert kernel_margin>=0 and coord_margin>=0
    Z=[[residue(co[i,k],p,-v[i]) for k in range(dim)] for i in range(h)]
    assert nmod_mat(Z,p).rank()==dim
    if entry_margin>=0:
        M=nmod_mat([[residue(A[i,j],p,u[i]+v[j]) for j in range(h)] for i in range(h)],p)
        MB=nmod_mat([[residue(B[i,j],p,u[i]+v[j]) for j in range(h)] for i in range(h)],p)
        assert not (M*nmod_mat(Z,p)) and not (MB*nmod_mat(Z,p))
        rank=M.rank();assert rank<=h-dim
    else:rank=None
    # The obvious integer lift of Phi_3 is not generally a third-level lift.
    deep=phi*Dcache(N)
    b=C.transpose().solve(fmpq_mat(h,1,[deep[i] for i in range(h)]))
    Ab=A*b
    naive_depth=min(val(Ab[i,0],p)-u[i] for i in range(h))
    return dict(p=p,N=N,h=h,d=d,first_kernel_dimension=dim,
                uniform_estimate_audit_margin=kernel_margin,
                coordinate_integrality_margin=coord_margin,
                whole_matrix_integral_finite_check=entry_margin>=0,
                fixed_tropical=sum(u)+sum(v),finite_rank=rank,rank_upper_target=h-dim,
                naive_Phi3_normalized_depth=naive_depth,
                audited_scalar_entries=2*h*dim)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='11:4,13:5,17:6,19:7,23:8,29:10,31:11,37:13,41:14,41:15,43:15,43:16,47:16,47:17,53:18,53:19,59:20,59:21,59:22,61:21,61:22')
    args=ap.parse_args();rows=[];start=time.time()
    for pair in args.pairs.split(','):
        r=analyze(*map(int,pair.split(':')));rows.append(r)
        Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps(r)+f' time={time.time()-start:.1f}',flush=True)
