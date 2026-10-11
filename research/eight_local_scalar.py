"""A rational nine-node local model for the Laurent scalar.

Its equality to the full Schur model still needs a uniform localization proof.
"""
import json
from functools import lru_cache
from pathlib import Path
from flint import fmpq,fmpq_mat,fmpq_poly
from joint_padic import residue


@lru_cache(None)
def rational_model():
    z=fmpq_poly([0,1]);nodes=list(range(-4,5));D=fmpq_poly([1])
    for a in nodes:D*=z-a
    H=[fmpq(0)]
    for j in range(1,5):H.append(H[-1]+fmpq(1,j**7))
    weights={a:H[-a if a<0 else max(0,a-1)] for a in nodes}
    ls={5:fmpq(1,6),6:fmpq(1,2),7:fmpq(7,12),9:fmpq(-7,10)}
    def L(P):return sum((P[e]*v for e,v in ls.items()),fmpq(0))
    dd=D.derivative()
    moments=[]
    for e in range(17):
        P=z**e
        moments.append(sum((weights[a]*P(a)/dd(a) for a in nodes),fmpq(0))+L(P//D))
    V=fmpq_mat(9,9,[moments[i+j] for i in range(9) for j in range(9)])
    w=fmpq_mat(9,1,[L(z**i) for i in range(9)])
    kappa=-L(D)+(w.transpose()*V.inv()*w)[0,0]
    out=dict(matrix=[[str(V[i,j]) for j in range(9)] for i in range(9)],
             cross=[str(w[i,0]) for i in range(9)],bare=str(L(D)),
             determinant=str(V.det()),correction=str((w.transpose()*V.inv()*w)[0,0]),kappa=str(kappa))
    return kappa,out


def model():
    kappa,base=rational_model();out=dict(base)
    data=json.loads(Path(__file__).with_name('eight_schur_probe.json').read_text())
    out['checks']=[dict(p=x['p'],N=x['N'],r=x['r'],observed=x['laurent_scalar'],
                    predicted=residue(kappa,x['p'],0),matches=residue(kappa,x['p'],0)==x['laurent_scalar'])
                    for x in data if x.get('laurent_scalar') is not None]
    assert all(x['matches'] for x in out['checks'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k not in ['matrix','cross']}),flush=True)
    return out


if __name__=='__main__':model()
