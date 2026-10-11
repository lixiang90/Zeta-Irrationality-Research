#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 比较测度证书生成器 v2（α=3/100 与 1/40，多初值 + 深光滑阶梯，无 SLSQP）。

v1 教训：SLSQP 数值梯度在惩罚目标上爆炸；NM 光滑阶梯稳定收敛至 f ≈ −1.97。
本版：3 组几何初值 × 光滑 {0.03, 0.01, 0.003}，输出每组最优 ×10¹² 候选。
"""
import numpy as np

CSTAR_CACHE = {}
def cstar8(al, lam):
    return -2*lam + 16*al*lam*(1-np.log(al)) + 3*lam**2 - 2*lam**2*np.log(2*lam)

def V8(t, al):
    t = np.asarray(t, float)
    out = np.log1p(t) - 8*al*np.log(t + al*al) - 2 + 16*al
    s = np.sqrt(np.maximum(t, 1e-300))
    atan1 = np.where(t > 1e-12, np.arctan(1.0/s), np.pi/2)
    return out + 2*s*(np.pi + atan1 - 8*np.arctan(al/s))

GRID = np.concatenate([np.linspace(1e-7, 0.005, 600), np.linspace(0.005, 0.05, 600),
                       np.linspace(0.05, 2.0, 2200)])

def U_rho(t, a, b, c):
    m = (a + b) / 2
    inside = (a[None,:] <= t[:,None]) & (t[:,None] <= b[None,:])
    disc = np.sqrt(np.abs((t[:,None] - a[None,:]) * (t[:,None] - b[None,:])))
    U = np.where(inside, np.log((b - a) / 4.0),
                 np.log((np.abs(t[:,None] - m[None,:]) + disc) / 2.0))
    return U @ c

def energy_I(a, b, c):
    S = np.cumsum(c); S0 = np.concatenate([[0.0], S[:-1]])
    return float(np.sum((S**2 - S0**2) * np.log((b - a) / 4.0)))


def project(x):
    x = x.copy()
    a, b = x[:16], x[16:32]
    for j in range(16):
        if b[j] < a[j] + 1/200:
            m = (a[j] + b[j]) / 2
            a[j] = max(1e-9, m - 1/400)
            b[j] = m + 1/400
        if b[j] > 2: b[j] = 2
        if a[j] < 0: a[j] = 1e-9
    x[:16], x[16:32] = a, b
    return x

def pen(x):
    a, b, c = x[:16], x[16:32], x[32:48]
    p = np.sum(np.maximum(0, np.diff(a))) + np.sum(np.maximum(0, -np.diff(b)))
    p += np.sum(np.maximum(0, 1/225 - (b - a))) * 1e4
    p += np.maximum(0, -a.min()) * 1e4 + np.maximum(0, b.max() - 2) * 1e4
    p += np.maximum(0, -c.min()) * 1e4
    return p

def make_run(al):
    lam = 1 - al
    VG = V8(GRID, al)
    Cs = cstar8(al, lam)
    def objective(x, smooth):
        a, b, c = x[:16], x[16:32], x[32:48]
        if pen(x) > 0:
            return 1e6 + 1e6*pen(x) + 1e8*abs(c.sum() - lam)
        U = U_rho(GRID, a, b, c)
        ex = 2*U - VG
        m = ex.max()
        M0s = m + smooth*np.log(np.mean(np.exp((ex - m)/smooth)))
        return lam*M0s - energy_I(a, b, c) + Cs
    def exact(x):
        a, b, c = x[:16], x[16:32], x[32:48]
        U = U_rho(GRID, a, b, c)
        M0 = float((2*U - VG).max())
        return lam*M0 - energy_I(a, b, c) + Cs, M0
    return objective, exact, lam

def nm(x0, objective, smooths=((0.03, 4000), (0.01, 8000), (0.003, 12000))):
    from scipy.optimize import minimize
    x = x0.copy()
    for s, it in smooths:
        r = minimize(lambda y: objective(y, s) + 1e5*pen(y), x,
                     method='Nelder-Mead', options={'maxiter': it, 'xatol': 1e-12, 'fatol': 1e-12})
        x = project(r.x)
    return x

def inits(al):
    # 几何初值：V 极小点在 t ≈ 0.81α² 附近；支撑覆盖 (0, 2)
    tmin = 0.81 * al * al
    outs = []
    for span, bmax in ((8.0, 1.2), (20.0, 0.8), (6.0, 1.8)):
        a0 = tmin/span * np.geomspace(1, 1e-3, 16)
        b0 = np.linspace(8*tmin, bmax, 16)
        c0 = np.linspace(0.09, 0.015, 16); c0 = c0/c0.sum()*(1-al)
        outs.append(np.concatenate([a0, b0, c0]))
    return outs

if __name__ == "__main__":
    D = 10**12
    for al in (0.025,):
        objective, exact, lam = make_run(al)
        print(f"\n===== α = {al}, λ = {lam} =====", flush=True)
        results = []
        for i, x0 in enumerate(inits(al)):
            x = nm(x0, objective)
            f, M0 = exact(x)
            fr, M0r = exact(np.round(x*D)/D)
            results.append((f, fr, x))
            print(f"init{i}: f = {f:.6f} (M0={M0:.4f}) pen={pen(x):.2e} |  有理化 f = {fr:.6f}", flush=True)
            np.save(f'research/measure8_alpha{al}_init{i}.npy', x)
        results.sort(key=lambda t: t[1])
        f, fr, x = results[0]
        xb = results[0][2]
        a, b, c = np.round(xb[:16]*D)/D, np.round(xb[16:32]*D)/D, np.round(xb[32:48]*D)/D
        print(f"最优（有理化后 f = {fr:.6f}）：")
        for j in range(16):
            print(f"({int(round(a[j]*D))},{int(round(b[j]*D))},{int(round(c[j]*D))}),", flush=True)
