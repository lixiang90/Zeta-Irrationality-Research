"""Independent full-polynomial residue audit of general integer/half-integer poles."""
import json,math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
from zeta35_broad_search import orders,coefficient_map,aligned


def verify(seed,scale=1,mode='fixed'):
    N=seed['N']*scale;M=seed['M']*scale;shape=seed['shape'];spacing=seed['spacing']
    old=Q(seed['offset']);offset=scale*int(old.floor())+old-int(old.floor())
    i=seed['i']*(scale if mode=='scaled' else 1);j=seed['j']*(scale if mode=='scaled' else 1)
    extra=tuple(v*scale for v in seed.get('extra_blocks',()))
    rows=coefficient_map(N,M,j,shape,spacing,offset,extra)
    a,b=seed['a'],seed['b'];Ti=b*rows[i][1]-a*rows[i][0];Tj=b*rows[j][1]-a*rows[j][0]
    if i==j:
        assert Ti==0;u,v=1,0
    else:
        assert Ti*Tj<0;u,v=abs(Tj),abs(Ti)
    poles=[offset+spacing*k for k in range(N+1)];es=orders(N,shape)
    center=2*offset+spacing*N;shift=(M+1)*(M+center+1)
    z=Poly([-shift,center,1]);W=u*z**i+v*z**j
    for block in (M,)+extra:
        for k in range(1,block+1):W*=Poly([-k*(center+k),center,1])
    D=Poly([1])
    for pole,e in zip(poles,es):D*=Poly([pole,1])**e
    assert W.degree()<=D.degree()-2
    wd=[W]
    for k in range(4):wd.append(wd[-1].derivative())
    total=[Q(0)]*6;constant=Q(0);half=offset.denominator==2
    for pole,e in zip(poles,es):
        localD,rem=divmod(D,Poly([pole,1])**e);assert not rem
        dd=[localD]
        for k in range(e-1):dd.append(dd[-1].derivative())
        num=[wd[k](-pole)/math.factorial(k) for k in range(e)]
        den=[dd[k](-pole)/math.factorial(k) for k in range(e)]
        series=[]
        for k in range(e):series.append((num[k]-sum((den[l]*series[k-l] for l in range(1,k+1)),Q(0)))/den[0])
        for s in range(1,e+1):
            cs=series[e-s];total[s]+=cs
            H=(sum((Q(2**s,(2*k+1)**s) for k in range(int(pole.floor())+1)),Q(0)) if half
               else sum((Q(1,k**s) for k in range(1,int(pole)+1)),Q(0)))
            constant-=cs*H
    assert total[1]==total[2]==total[4]==0
    A=(31 if half else 1)*total[5];B=(7 if half else 1)*total[3]
    assert b*B==a*A
    rawq=A/b;den=math.lcm(int(rawq.denominator),int(constant.denominator))
    q,c=int(rawq*den),int(constant*den);g=math.gcd(q,c);q//=g;c//=g
    assert (q,c)==aligned(rows,i,j,a,b)
    ctx.prec=max(abs(q).bit_length(),abs(c).bit_length())+512
    value=q*(a*arb(3).zeta()+b*arb(5).zeta())+c
    assert value>0
    return dict(N=N,M=M,a=a,b=b,shape=shape,spacing=spacing,offset=str(offset),mode=mode,i=i,j=j,
                q=str(q),c=str(c),log_interval=value.log().str(25),log_L=float(value.log()))


if __name__=='__main__':
    root=Path(__file__).parent
    source=json.loads((root/'zeta35_broad_search_stage3.json').read_text())['records']
    seen=set();selected=[]
    for r in source:
        key=(r['seed']['shape'],Q(r['seed']['offset']).denominator)
        if key not in seen:selected.append(r);seen.add(key)
    results=[]
    for r in selected:
        for scale in (1,4):
            if scale==4 and r['levels'][1]['status']!='verified':continue
            row=verify(r['seed'],scale,r['mode']);results.append(row)
            print('verified',row['N'],row['shape'],row['offset'],round(row['log_L'],5),flush=True)
    results.append(verify(source[0]['seed'],16,source[0]['mode']))
    (root/'verify_zeta35_broad_search.json').write_text(json.dumps(dict(status='passed',rows=results),indent=2),encoding='utf-8')
