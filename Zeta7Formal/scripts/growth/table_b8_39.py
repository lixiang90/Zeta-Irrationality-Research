# b=8 growth tables, parameterized by tuning (lam = 1 - al, al = N/K).
# Ein/Eout mirror Zeta7/Growth/{TablePrime,OuterPrime}.lean (b=8 coefficients:
# 16, B = 16q' - 2q - 6, 8b - a; GO +6; Eout max-term coefficient CMAX).
# CMAX defaults to the minimal legal value lam + (b-1)*al = 1 + 6*al (rank loss).
from fractions import Fraction as Fr
import math, os
lam = Fr(int(os.environ.get('LAM_NUM', 39)), int(os.environ.get('LAM_DEN', 40)))
al = Fr(int(os.environ.get('AL_NUM', 1)), int(os.environ.get('AL_DEN', 40)))
if 'CMAX_NUM' in os.environ:
    CMAX = Fr(int(os.environ['CMAX_NUM']), int(os.environ.get('CMAX_DEN', 1)))
else:
    CMAX = 1 + 6 * al

def fl(x): return math.floor(x)

def lrow(k, b):
    t = k - b + 1
    return max(0, t // 2)

def psiR(k, b):
    L = lrow(k, b); t = k - b
    return Fr(L * (t - L + 1), 2)

def bcoef(h): return [h(0), h(1) - h(0), h(2) - h(1)]

def cvLo(f): return [Fr(0), Fr(0), 1 - f]

def cvHi(f): return [Fr(1, 2), f, Fr(1, 2)]

def ccount(f, g, i, j):
    return max(Fr(0), min(min(cvHi(f)[i], cvHi(g)[j]), Fr(1, 2)) -
                    max(max(cvLo(f)[i], cvLo(g)[j]), Fr(0)))

def Jc_fast(u):
    mu = fl(2 * u); return mu * u - Fr(mu * (mu + 1), 4)

def Ein(x, k):
    q = fl(x); qq = fl(al * x); u = lam * x
    B = 16 * qq - 2 * q - 6
    h = lambda a, b: psiR(k, B + 8 * b - a)
    s = Fr(0)
    for i in range(3):
        for j in range(3):
            c = bcoef(lambda a: bcoef(lambda b: h(a, b))[j])[i]
            s += c * ccount(x - q, al * x - qq, i, j)
    return -2 * u * q + 16 * u * qq + 2 * Jc_fast(u) - u * k + 2 * s

def GO(q, a, d):
    L = 2 * q + a - 2
    if L <= 0: return Fr(0)
    return sum(min(Fr(0), i + 3 * d - Fr(2 * q + a + 6, 2)) for i in range(L))

def Eout(x, cm=CMAX):
    q = fl(x); u = lam * x
    s = Fr(0)
    for i in range(3):
        for j in range(3):
            c = bcoef(lambda a: bcoef(lambda b: GO(q, a, b))[j])[i]
            s += c * ccount(x - q, al * x - fl(al * x), i, j)
    return -2 * u * q + 2 * Jc_fast(u) - 2 * s + max(Fr(0), cm * x - 2)
