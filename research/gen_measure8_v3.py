#!/usr/bin/env python3
# α=1/40 测度优化 v3：L-BFGS-B（数值梯度，光滑 max）+ 多初值 + NM 抛光。
# 目标：嵌套 arcsine 16 原子族内 f = λM0 − I(ρ) + C* ≤ −3.43（门控：Aeff(39n)=3.4242）。
import numpy as np
import sys
sys.path.insert(0, 'research')
from gen_measure8 import (cstar8, V8, GRID, U_rho, energy_I, project, pen, inits)

AL = 0.025
LAM = 1 - AL
VG = V8(GRID, AL)
CS = cstar8(AL, LAM)
D = 10**12

def objective_smooth(x, smooth):
    a, b, c = x[:16], x[16:32], x[32:48]
    p = pen(x)
    if p > 0:
        return 1e6 + 1e6*p + 1e8*abs(c.sum() - LAM)
    U = U_rho(GRID, a, b, c)
    ex = 2*U - VG
    m = ex.max()
    M0s = m + smooth*np.log(np.mean(np.exp((ex - m)/smooth)))
    return LAM*M0s - energy_I(a, b, c) + CS

def exact(x):
    a, b, c = x[:16], x[16:32], x[32:48]
    U = U_rho(GRID, a, b, c)
    M0 = float((2*U - VG).max())
    return LAM*M0 - energy_I(a, b, c) + CS, M0

def run():
    from scipy.optimize import minimize
    best = (1e9, None)
    for i, x0 in enumerate(inits(AL)):
        x = x0.copy()
        for smooth in (0.02, 0.006, 0.002):
            r = minimize(lambda y: objective_smooth(y, smooth), x, method='L-BFGS-B',
                         options={'maxiter': 1500, 'ftol': 1e-15, 'gtol': 1e-10})
            x = project(r.x)
        r = minimize(lambda y: objective_smooth(y, 0.0005), x, method='Nelder-Mead',
                     options={'maxiter': 8000, 'xatol': 1e-13, 'fatol': 1e-13})
        x = project(r.x)
        f, M0 = exact(x)
        fr, M0r = exact(np.round(x*D)/D)
        print(f"init{i}: f = {f:.6f} (M0={M0:.4f}) pen={pen(x):.2e} | 有理化 f = {fr:.6f}", flush=True)
        if fr < best[0]:
            best = (fr, x.copy())
    fr, x = best
    print(f"最优（有理化后 f = {fr:.6f}）：", flush=True)
    for j in range(16):
        a, b, c = int(round(x[j]*D)), int(round(x[16+j]*D)), int(round(x[32+j]*D))
        print(f"({a},{b},{c}),", flush=True)

if __name__ == "__main__":
    run()
