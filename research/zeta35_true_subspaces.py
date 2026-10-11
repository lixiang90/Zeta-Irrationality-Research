"""Compare genuinely different monomial subspaces, with exact arithmetic."""
import argparse,itertools,json,math,time
from pathlib import Path
from flint import fmpq as Q,fmpq_poly,fmpq_mat,arb,arb_poly,ctx
from zeta35_target31_scan import entries
from zeta35_target31 import content_and_primitive

def pencil_polynomial(A,B):
    h=A.nrows();rank=B.rank()
    if rank==h:return (-(B.inv()*A)).charpoly()*B.det()
    values=[(A+x*B).det() for x in range(rank+1)]
    poly=fmpq_poly();basis=fmpq_poly([1])
    for k in range(rank+1):
        poly+=values[0]*basis
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
        basis=basis*fmpq_poly([-k,1])/Q(k+1)
    return poly

def test(K,N,m,ambient,omitted,sequences=None):
    start=time.perf_counter()
    if sequences is None:_,aa,bb=entries(K,N,m,ambient)
    else:aa,bb=sequences
    keep=[e for e in range(ambient) if e not in omitted];h=len(keep)
    A=fmpq_mat([[aa[i+j] for j in keep] for i in keep])
    B=fmpq_mat([[bb[i+j] for j in keep] for i in keep])
    poly=pencil_polynomial(A,B)
    assert poly(0)==A.det() and poly(-1)==(A-B).det()
    content,coeff=content_and_primitive(poly)
    ctx.prec=max(abs(v).bit_length() for v in coeff)+K*K+4000
    value=arb_poly(coeff)(3*arb(3).zeta()+arb(5).zeta())
    assert value>0
    return dict(K=K,N=N,m=m,ambient=ambient,h=h,omitted=list(omitted),
        degree=poly.degree(),log_p=float(value.log()),log_interval=str(value.log()),
        content=str(content),seconds=time.perf_counter()-start)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--scale',type=int,default=1)
    args=parser.parse_args();scale=args.scale
    K,N,m,ambient=40*scale,3*scale,4,37*scale
    _,aa,bb=entries(K,N,m,ambient)
    if scale==1:
        candidates=list(itertools.combinations([0,1,2,15,25,30,32,33,34,35,36],2))
    else:
        source=json.loads(Path(__file__).with_name('zeta35_true_subspaces_scale1.json').read_text())
        candidates=[tuple(row['omitted']) for row in sorted(source['rows'],key=lambda r:r['log_p'])[:3]]
        if (35,36) not in candidates:candidates.append((35,36))
    rows=[]
    path=Path(__file__).with_name(f'zeta35_true_subspaces_scale{scale}.json')
    for base in candidates:
        omitted=tuple(scale*i+j for i in base for j in range(scale))
        row=test(K,N,m,ambient,omitted,(aa,bb));rows.append(row)
        path.write_text(json.dumps(dict(scope='finite true-subspace comparisons only',rows=rows),indent=2),encoding='utf-8')
    best=sorted(rows,key=lambda r:r['log_p'])[:8]
    print(json.dumps(dict(cases=len(rows),best=[{k:r[k] for k in ('K','h','omitted','degree','log_p','seconds')} for r in best]),indent=2),flush=True)

if __name__=='__main__':main()
