"""Exploratory generalization: derivative order d and numerator beta are separate.

The beta=8, d=6 slice is checked against the project's exact arithmetic tables.
Other slices are conjectural extensions of the local estimates, NOT proved bounds.
"""
import numpy as np
from scipy.integrate import quad


def class_data(x,alpha):
    f=x-np.floor(x); g=alpha*x-np.floor(alpha*x)
    lo_f=[0*x,0*x,1-f]; hi_f=[0*x+.5,f,0*x+.5]
    lo_g=[0*x,0*x,1-g]; hi_g=[0*x+.5,g,0*x+.5]
    return [[np.maximum(0,np.minimum(np.minimum(hi_f[i],hi_g[j]),.5)
                        -np.maximum(np.maximum(lo_f[i],lo_g[j]),0))
             for j in range(3)] for i in range(3)]


def expected(h, counts):
    # Two finite differences in each count variable (the existing bcoef method).
    v=[[h(i,j) for j in range(3)] for i in range(3)]
    v=[[row[0],row[1]-row[0],row[2]-row[1]] for row in v]
    v=[v[0],[v[1][j]-v[0][j] for j in range(3)],
       [v[2][j]-v[1][j] for j in range(3)]]
    return sum(v[i][j]*counts[i][j] for i in range(3) for j in range(3))


def jc(u):
    m=np.floor(2*u)
    return m*u-m*(m+1)/4


def ein(x,alpha,beta=8,d=6):
    x=np.asarray(x)[:,None]; lam=1-alpha
    q=np.floor(x); qp=np.floor(alpha*x); u=lam*x
    base=2*beta*qp-2*q-d
    # The minimizer is near k = 4u + average local beta.
    center=np.floor(4*u+base+2*beta*(alpha*x-qp)-2*(x-q))
    k=center+np.arange(-2*int(beta)-12,2*int(beta)+13)[None,:]
    def psi(a,b):
        t=k-(base+beta*b-a)
        L=np.maximum(0,np.floor((t+1)/2))
        return L*(t-L+1)/2
    cost=-2*u*q+2*beta*u*qp+2*jc(u)-u*k+2*expected(psi,class_data(x,alpha))
    idx=np.argmin(cost,axis=1)
    assert np.all((idx>0)&(idx<cost.shape[1]-1))
    return np.min(cost,axis=1)


def eout(x,alpha,beta=8,d=6):
    x=np.asarray(x); lam=1-alpha; q=np.floor(x); u=lam*x
    def go(a,delta):
        ell=2*q+a
        L=np.maximum(0,ell-2)
        return sum(np.where(i<L,np.minimum(0,i+(beta/2-1)*delta-(ell+d)/2),0)
                   for i in range(6))
    return -2*u*q+2*jc(u)-2*expected(go,class_data(x,alpha))+np.maximum(0,(1+(beta-2)*alpha)*x-2)


def tail(alpha,beta=8,d=6,M=400):
    lam=1-alpha; C=(5+(beta+1)**2)/32
    pts=sorted(set([20.,float(M)]+list(np.arange(21,M,dtype=float))+
                   [j/alpha for j in range(int(20*alpha)+1,int(M*alpha)+1) if 20<j/alpha<M]))
    total=0.
    for l,r in zip(pts,pts[1:]):
        mid=(l+r)/2
        aa=2*lam*(1-beta*alpha)
        bb=lam*(d-2*np.floor(mid)+2*beta*np.floor(alpha*mid))
        total+=aa*np.log(r/l)+bb*(1/l-1/r)+C/2*(1/l**2-1/r**2)
    return total


def arithmetic(alpha,beta=8,d=6,n=12000):
    def midint(fun,l,r):
        x=l+(np.arange(n)+.5)*(r-l)/n
        return float(np.sum(fun(x)/x**3)*(r-l)/n)
    inside=midint(lambda x:ein(x,alpha,beta,d),3,20)
    outside=midint(lambda x:eout(x,alpha,beta,d),1/(2*(1-alpha)),3)
    end=tail(alpha,beta,d)
    small=(d+2)*(1-alpha)/400
    return dict(inner=inside,outer=outside,tail=end,small=small,A=inside+outside+end+small)


if __name__=="__main__":
    import json
    from pathlib import Path
    from restart_probe import uniform_primal
    rows=[]
    for beta in [2,4,6,8,10,12,16]:
        for alpha in [.015,.025,.04,.06,.075,.10,.125]:
            row=dict(alpha=alpha,beta=beta,**arithmetic(alpha,beta),**uniform_primal(alpha,beta=beta))
            row["primal_gap"]=row["A"]+row["primal"]
            rows.append(row)
            print(json.dumps(row),flush=True)
    Path(__file__).with_name("restart_arithmetic_scan.json").write_text(json.dumps(rows,indent=2))
