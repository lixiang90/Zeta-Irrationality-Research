"""Extreme-ray reduction of the coefficientwise positive numerator cone."""
import json
from pathlib import Path
from flint import fmpq as Q
from zeta35_numerator_space import coefficient_map, evaluate, primitive


def run(N,M,d):
    shift=(M+1)*(M+N+1)
    rows=coefficient_map(N,M,d,shift)
    T=[r[1]-3*r[0] for r in rows]
    rays=[]
    for i in range(d+1):
        if T[i]==0:
            rays.append((i,i,Q(1),Q(0)))
        for j in range(i+1,d+1):
            if T[i]*T[j]<0:
                rays.append((i,j,abs(T[j]),abs(T[i])))
    endpoints={};records=[]
    for i,j,u,v in rays:
        A=u*rows[i][0]+v*rows[j][0]
        B=u*rows[i][1]+v*rows[j][1]
        C=u*rows[i][2]+v*rows[j][2]
        assert B==3*A
        value=evaluate(A,C)
        rec=dict(i=i,j=j,u=str(u),v=str(v),**value)
        records.append(rec)
        if A:
            side='lower' if A>0 else 'upper'
            bound=-C/A
            if side not in endpoints or (bound>endpoints[side][0] if A>0 else bound<endpoints[side][0]):
                endpoints[side]=(bound,len(records)-1)
    assert records
    best=min(records,key=lambda z:z['log_L'])
    result=dict(N=N,M=M,d=d,shift=shift,target_signs=[int(t>0)-int(t<0) for t in T],
                ray_count=len(rays),best=best,
                endpoints={k:dict(bound=str(v[0]),ray=records[v[1]]) for k,v in endpoints.items()},
                rows=[[str(v) for v in row] for row in rows])
    print('cone',N,M,d,'rays',len(rays),'best',best['i'],best['j'],round(best['log_L'],6),
          'sides',list(endpoints),flush=True)
    return result


if __name__=='__main__':
    results=[]
    for N in (10,20,40,80):
        M=N;maxd=(5*N+3-2*M)//2
        for d in sorted(set((1,min(4,maxd),min(N//2,maxd),maxd))):
            results.append(run(N,M,d))
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='exact extreme rays of a sufficient positivity cone; not all positive polynomials',
        cases=results),indent=2),encoding='utf-8')
