#!/usr/bin/env python3
# 嵌套 arcsine 族 f(α) 扫描：α ∈ {0.06, 0.05, 0.045, 0.04, 0.03}，L-BFGS-B + NM 抛光。
import numpy as np
import sys
sys.path.insert(0, 'research')
from gen_measure8 import cstar8, V8, GRID, U_rho, energy_I, project, pen, inits
from scipy.optimize import minimize

D = 10**12
def run(al):
    lam = 1 - al
    VG = V8(GRID, al); CS = cstar8(al, lam)
    def obj(x, smooth):
        a, b, c = x[:16], x[16:32], x[32:48]
        p = pen(x)
        if p > 0: return 1e6 + 1e6*p + 1e8*abs(c.sum()-lam)
        U = U_rho(GRID, a, b, c); ex = 2*U - VG; m = ex.max()
        return lam*(m + smooth*np.log(np.mean(np.exp((ex-m)/smooth)))) - energy_I(a,b,c) + CS
    def exact(x):
        a, b, c = x[:16], x[16:32], x[32:48]
        return lam*float((2*U_rho(GRID,a,b,c)-VG).max()) - energy_I(a,b,c) + CS
    best = 1e9
    for i, x0 in enumerate(inits(al)):
        x = x0.copy()
        for s in (0.02, 0.006, 0.002):
            r = minimize(lambda y: obj(y, s), x, method='L-BFGS-B',
                         options={'maxiter': 1200, 'ftol': 1e-15})
            x = project(r.x)
        r = minimize(lambda y: obj(y, 0.0005), x, method='Nelder-Mead',
                     options={'maxiter': 6000, 'xatol': 1e-13, 'fatol': 1e-13})
        x = project(r.x)
        f = exact(x); fr = exact(np.round(x*D)/D)
        print(f"  al={al} init{i}: f={f:.6f} | 有理化 f={fr:.6f}", flush=True)
        best = min(best, fr)
    print(f"al={al}: BEST f = {best:.6f}", flush=True)
    return best

if __name__ == "__main__":
    for al in (0.06, 0.05, 0.045, 0.04, 0.03):
        run(al)
