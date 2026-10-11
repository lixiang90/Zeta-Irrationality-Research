"""Exact first-order expansion at infinity and the -27 formal exponent."""
import json
import math
from pathlib import Path
from flint import ctx, fmpq, fmpq_mat, fmpq_series
from modular_module_probe import mul, mm, inverse


def main():
    ctx.cap=2
    eps=fmpq_series([0,1]);zero=eps*0;one=zero+1
    power=lambda c,k:[math.comb(k,j)*c**(k-j) for j in range(k+1)]
    def kernels(r,count):
        result=[]
        for i in range(count):
            left=mul(mul([-3+(4-2*r)*eps,one],power(one,8)),power(-eps,2*i))
            right=mul(mul(power(-one,8),[3+(-4+2*r)*eps,one]),power(eps,2*i))
            raw=[(a-b)/2 for a,b in zip(left,right)]
            assert all(raw[j][0]==0 and raw[j][1]==0 for j in range(1,len(raw),2))
            result.append(raw[::2])
        return result
    K=kernels(0,8)
    base=[one*(math.comb(8,r)*(-1)**(8-r)) for r in range(9)]
    cols=[]
    for j in range(4):
        P=[zero]*j+base[:]+[zero]*(3-j)
        for i in reversed(range(8)):
            u=P[i+4]/K[i][i+4]
            for k,x in enumerate(K[i]):P[k]-=u*x
        assert all(x[0]==0 and x[1]==0 for x in P[4:])
        cols.append(P[:4])
    Q=[[cols[j][i] for j in range(4)] for i in range(4)]
    def head(r):
        K=kernels(r,1)[0]
        c=(3+(-4+2*r)*eps)**2
        T=[[zero]*4 for _ in range(4)]
        for j in range(4):
            T[j][j]-=c
            if j<3:T[j+1][j]+=one
            else:
                for i in range(4):T[i][j]-=K[i]/K[4]
        return T
    C=mm(inverse(Q),mm(mm(head(0),head(1)),head(2)))
    R=[[1024*(1-eps)**5*C[j][i]*(1-2*eps)**(2*j) for j in range(4)] for i in range(4)]
    R0=fmpq_mat([[R[i][j][0] for j in range(4)] for i in range(4)])
    R1=fmpq_mat([[R[i][j][1] for j in range(4)] for i in range(4)])
    data=json.loads(Path(__file__).with_name('determinant_shape_probe.json').read_text(encoding='utf-8'))
    assert R0==fmpq_mat([[fmpq(v) for v in row] for row in data['limiting_recurrence']['matrix']])
    v=fmpq_mat([[1],[-3],[9],[-27]])
    w=fmpq_mat([[fmpq(-1,5),-5,fmpq(-43,5),1]])
    assert R0*v==-27*v and w*R0==-27*w
    sigma=(w*R1*v)[0,0]/(-54*(w*v)[0,0])
    assert sigma==-4
    result=dict(scope='Exact truncated-series calculation; formal exponent does not assert rational reducibility.',
                R0=[[str(v) for v in row] for row in R0.tolist()],
                R1=[[str(v) for v in row] for row in R1.tolist()],
                right_eigenvector=['1','-3','9','-27'],left_eigenvector=['-1/5','-5','-43/5','1'],
                formal_power_exponent=str(sigma))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('Exact formal exponent:',sigma)


if __name__=='__main__':main()
