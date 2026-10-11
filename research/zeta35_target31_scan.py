"""Finite scan of D_N^m / D_K Gram constructions for 3*zeta(3)+zeta(5)."""
import argparse, json, math, time
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, fmpq_mat, arb, arb_poly, ctx
from zeta35_target31 import content_and_primitive
import zeta35_mixed_moments as mixed

def entries(K,N,m,h=None):
    # D_N(t)>0 for t>=0, so odd positive m also preserve Gram positivity.
    assert 0<=N<K and m>=1
    h=K-N if h is None else h
    assert 1<=h<=K-N
    DN=mixed.original.Dpoly(N);DK=fmpq_poly(mixed.original.Dpoly(K))
    W=fmpq_poly(DN**m);H3=[Q(0)];H5=[Q(0)]
    for j in range(1,K+1):
        H3.append(H3[-1]+Q(1,j**3));H5.append(H5[-1]+Q(1,j**5))
    degree=max(0,m*N+2*h-2-K)
    moments=[]
    for e in range(degree+1):
        mu5=Q(-1)**e*Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24
        moments.append(mu5-3*mixed.mu3(e+1))
    residues={j:Q(DN(-j*j))**m/math.prod(k*k-j*j for k in range(1,K+1) if k!=j)
              for j in range(N+1,K+1)}
    A=[];B=[]
    for e in range(2*h-1):
        quotient=(W*fmpq_poly([0]*e+[1]))//DK
        value=sum((quotient[k]*moments[k] for k in range(quotient.degree()+1)),Q(0))
        linear=Q(0)
        for j,r in residues.items():
            c=r*Q(-j*j)**e
            value+=c*(-j**4*(3*H3[j]+H5[j])-3*Q(j*j-j,2)-1+Q(1,2*j))
            linear+=c*j**4
        A.append(value);B.append(linear)
    return h,A,B

def run(K,N,m,h=None):
    start=time.perf_counter();h,A,B=entries(K,N,m,h)
    Bmat=fmpq_mat([[B[i+j] for j in range(h)] for i in range(h)])
    rank=Bmat.rank()
    if rank==h:
        poly=mixed.original.det_poly(h,A,B)
    else:
        # det(A+XB) has degree at most rank(B). Exact Newton interpolation.
        differences=[fmpq_mat([[A[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
                     for x in range(rank+1)]
        poly=fmpq_poly();basis=fmpq_poly([1])
        for k in range(rank+1):
            poly+=differences[0]*basis
            differences=[differences[i+1]-differences[i] for i in range(len(differences)-1)]
            basis=basis*fmpq_poly([-k,1])/Q(k+1)
        x=Q(-1)
        assert poly(x)==fmpq_mat([[A[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
    assert poly.degree()<=rank
    content,coeff=content_and_primitive(poly)
    ctx.prec=max(abs(v).bit_length() for v in coeff)+K*K+4000
    value=arb_poly(coeff)(3*arb(3).zeta()+arb(5).zeta())
    assert value>0
    logp=float(value.log())
    result=dict(K=K,N=N,m=m,h=h,degree=poly.degree(),linear_rank=rank,log_p=logp,log_p_over_K2=logp/(K*K),
                log_interval=str(value.log()),content=str(content),
                seconds=time.perf_counter()-start)
    print(K,N,m,'h',h,'degree',poly.degree(),'logP',round(logp,6),'scaled',round(logp/(K*K),6),flush=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('K',type=int)
    parser.add_argument('--cases',nargs='*',help='N:m or N:m:h tuples; default broad scan')
    parser.add_argument('--tag',default='',help='suffix for a separate output file')
    args=parser.parse_args()
    cases=[tuple(map(int,s.split(':'))) for s in args.cases] if args.cases else (
        [(0,2)]+[(N,m) for m in (2,4,6,8) for N in (1,2,3,4,5,6,8,10) if N<args.K])
    path=Path(__file__).with_name(f'zeta35_target31_scan_K{args.K}{args.tag}.json')
    rows=[]
    for case in cases:
        rows.append(run(args.K,*case))
        path.write_text(json.dumps(dict(scope='finite_parameter_scan_only',rows=rows),indent=2),encoding='utf-8')
