"""Independent numerical probes. Numerical results are NOT proof certificates.

Separates the derivative order d (zeta(d+1)) from numerator exponent beta.
The nested-arcsine search has an exact mass equality and an analytic gradient.
"""
import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar


def field(t, alpha, beta=8):
    t = np.asarray(t, dtype=float)
    y = np.sqrt(t)
    return (np.log1p(t) - beta*alpha*np.log(t+alpha*alpha) - 2 + 2*beta*alpha
            + 2*y*(np.pi + np.arctan2(1., y) - beta*np.arctan2(alpha, y)))


def cstar(alpha, lam, beta=8):
    return -2*lam + 2*beta*alpha*lam*(1-np.log(alpha)) + 3*lam*lam - 2*lam*lam*np.log(2*lam)


def uniform_primal(alpha, lam=None, beta=8, right=None):
    lam = 1-alpha if lam is None else lam
    def val(r):
        ev = quad(lambda t: float(field(t, alpha, beta)), 0, r, epsabs=1e-11)[0]/r
        return lam*lam*(np.log(r)-1.5)-lam*ev+cstar(alpha,lam,beta)
    if right is None:
        result = minimize_scalar(lambda r: -val(r), bounds=(.002,2.), method="bounded")
        right = result.x
    return dict(primal=val(right), right=right)


def potentials(t,a,b):
    t = np.asarray(t)[:,None]
    disc = np.sqrt(np.abs((t-a)*(t-b)))
    return np.where((t>=a)&(t<=b), np.log((b-a)/4),
                    np.log((np.abs(t-(a+b)/2)+disc)/2))


def nested_search(alpha, lam=None, beta=8, atoms=40, ab_product=None):
    lam = 1-alpha if lam is None else lam
    if ab_product is None:
        ab_product = alpha**4*1.5
    # Fixed nested intervals, all products a_j*b_j equal ab_product.
    b = np.geomspace(np.sqrt(ab_product)*1.08, 1.8, atoms)
    a = ab_product/b
    assert np.all(np.diff(a)<0) and np.all(np.diff(b)>0)
    grid = np.unique(np.r_[0., np.geomspace(1e-10,3.,1800),a,b])
    P = potentials(grid,a,b)
    H = np.log((b-a)/4)[np.maximum.outer(np.arange(atoms),np.arange(atoms))]
    V = field(grid,alpha,beta)
    C = cstar(alpha,lam,beta)
    A = np.column_stack((-2*P,np.ones(len(grid))))
    x0 = np.r_[np.full(atoms,lam/atoms),np.max(2*P@(np.full(atoms,lam/atoms))-V)]
    def fun(x): return lam*x[-1]-x[:-1]@H@x[:-1]+C
    def jac(x): return np.r_[-2*H@x[:-1],lam]
    cons = [dict(type="eq",fun=lambda x: x[:-1].sum()-lam,
                 jac=lambda x: np.r_[np.ones(atoms),0.]),
            dict(type="ineq",fun=lambda x: A@x+V,jac=lambda x:A)]
    r = minimize(fun,x0,jac=jac,constraints=cons,bounds=[(0,lam)]*atoms+[(None,None)],
                 method="SLSQP", options=dict(maxiter=500,ftol=2e-11))
    c = r.x[:-1]
    # Recheck on a much finer grid, including outside the original range.
    fine = np.unique(np.r_[0.,np.geomspace(1e-12,100,40000),a,b])
    M = float(np.max(2*potentials(fine,a,b)@c-field(fine,alpha,beta)))
    f = lam*M-c@H@c+C
    return dict(alpha=alpha,lam=lam,beta=beta,ab_product=ab_product,success=bool(r.success),
                message=r.message,mass_error=float(c.sum()-lam),numerical_upper=float(f),
                grid_slack=float(M-r.x[-1]),M=M,I=float(c@H@c),
                a=a.tolist(),b=b.tolist(),c=c.tolist(),**uniform_primal(alpha,lam,beta))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpha",type=float,default=.025)
    ap.add_argument("--beta",type=float,default=8)
    ap.add_argument("--atoms",type=int,default=40)
    ap.add_argument("--lam",type=float)
    ap.add_argument("--out",default="restart_nested.json")
    args = ap.parse_args()
    rows=[]
    for factor in [.3,1.,3.,10.]:
        row=nested_search(args.alpha,args.lam,args.beta,args.atoms,args.alpha**4*factor)
        rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ("a","b","c")}),flush=True)
    Path(__file__).with_name(args.out).write_text(json.dumps(rows,indent=2),encoding="utf-8")
