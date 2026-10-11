"""Component audit for the uniform fixed-weight normalization theorem.

The proof uses the six-root Taylor packet, not a fitted valuation table.
All Q/P/D/B entries are checked separately; polynomial/pole cancellation
cannot conceal a failed component bound.
"""
import json,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat
from joint_exact import Dcache,moment
from joint_padic import val
from coupled_pencil import raw_pencil,vp_mod
from six_pole_kernel import weights
from boundary_first_kernel import weights as boundary_weights
from boundary_structure import matrices
from layer_projection import local_basis


def packet_audit():
    packet=fmpq_poly([1])
    for k in range(-3,3):packet*=fmpq_poly([-k,1])
    assert packet[5]==3 and packet[4]==-5 and packet[6]==1
    coefficient=packet[4]/6-packet[5]/2+fmpq(7,12)
    assert coefficient==fmpq(-7,4)
    Z=[0,1,-1,2]
    residues=[]
    for z in [-1,2]:
        denominator=1
        for y in Z:
            if y!=z:denominator*=z-y
        residues.append(fmpq((z+2)*(z-3),denominator))
    assert sum(residues)==0
    return dict(packet_coefficients=[str(x) for x in packet],
                next_local_coefficient=str(coefficient),
                boundary_pole_residues=[str(x) for x in residues])


def full(p,N,a):
    K=3*p-1-a;h=K-N
    z=raw_pencil(K,N,p,20);z1=raw_pencil(K,N,p,20,harmonic_deformation=1)
    assert z['shift']==z1['shift']
    u,v=weights(z['tags'],a);S=z['shift'];L=z['precision']
    components={'Q':z['Q'],'P':z['P'],'D':z1['A']-z['A'],'B':z['B']}
    margins={name:min(vp_mod(M[i,j],p,L)-S-u[i]-v[j]
                      for i in range(h) for j in range(h)) for name,M in components.items()}
    assert min(margins.values())>=0 and margins['B']>=5
    return dict(p=p,N=N,a=a,K=K,h=h,component_margins=margins,entries=4*h*h)


def boundary(p,N):
    A,B,tags,aa,bb=matrices(p,N);h=A.nrows();K=2*p-1
    u,v=boundary_weights(tags);W=Dcache(N)**8
    for j in range(2*p,3*p):W*=fmpq_poly([j*j,1])
    D=Dcache(K);qq=[];poly=W;t=fmpq_poly([0,1])
    for e in range(2*h-1):
        Q=poly//D
        qq.append(sum((q*moment(k) for k,q in enumerate(Q)),fmpq(0)))
        poly*=t
    basis,_,_=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    Q=C*fmpq_mat(h,h,[qq[i+j] for i in range(h) for j in range(h)])*C.transpose()
    components={'Q':Q,'P':A-Q,'B':B}
    margins={name:min(val(M[i,j],p)-u[i]-v[j] for i in range(h) for j in range(h))
             for name,M in components.items()}
    assert min(margins.values())>=0 and margins['B']>=4
    return dict(p=p,N=N,h=h,component_margins=margins,entries=3*h*h)


if __name__=='__main__':
    result=dict(symbolic=packet_audit(),full=[],boundary=[]);start=time.time()
    for p,N,a in [(11,4,a) for a in range(5)]+[(13,5,a) for a in range(6)]+[(17,6,0),(17,6,3),(17,6,6),(43,16,0),(43,16,7),(53,18,0)]:
        r=full(p,N,a);result['full'].append(r);print(json.dumps(r),flush=True)
    for p,N in [(11,4),(13,5),(17,6),(23,8),(43,16)]:
        r=boundary(p,N);result['boundary'].append(r);print(json.dumps(r),flush=True)
    result.update(entries=sum(r['entries'] for r in result['full']+result['boundary']),seconds=time.time()-start)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['full','boundary']}),flush=True)
