# Tail bound for the retuned b=8 growth chain (lam=39/40, al=1/40).
# Mirrors Zeta7/Growth/TailIntegral.lean:
#   grid t_i = 20 + i/3, qT i = (60+i)/3, qT' i = (60+i)/120  (al*t_i)
#   FT = 6*lam + 2*lam*(x-qT) - 16*lam*(al*x - qT')
#   PT = (8*lam/al) * g(1-g) - lam * f(1-f),  f = x - qT, g = al*x - qT'
#   CT = (8*lam/al^2) * G0(g) - lam * G0(f),  G0(v) = v(1-v)(2v-1)/6
#   Pbar = (8*lam/al - lam)/6
#   PhiT = PT/x^2 + 2*CT/x^3 - Pbar/x^2 + lam/x - (43/32)/x^2
#   bound = Phi_1140(400) - Phi_0(20) + SLACK*(1/20^3 - 1/400^3),  SLACK = 2*ceil(CTbd)
#   CTbd = (8*lam/al^2 + lam)/60  (|G0| <= 1/60 on [0,1])
# Also verifies against a high-precision direct integration of (x*F + 43/16)/x^3.
import os
from fractions import Fraction as Fr
lam = Fr(int(os.environ.get('LAM_NUM', 39)), int(os.environ.get('LAM_DEN', 40)))
al = Fr(int(os.environ.get('AL_NUM', 1)), int(os.environ.get('AL_DEN', 40)))
print("lam =", lam, " al =", al)
assert 2 * lam * 400 <= 1000   # layer-cake Jc truncation valid

A6, A2, A16 = 6 * lam, 2 * lam, 16 * lam
CO_P = 8 * lam / al       # PT g-coefficient
CO_C = 8 * lam / al ** 2  # CT G0(g)-coefficient
Pbar = (CO_P - lam) / 6
import math
SLACK = 2 * math.ceil((CO_C + lam) / 60)  # |CT| <= (CO_C+lam)/60; 6*SLACK/3
print("6lam =", A6, " 2lam =", A2, " 16lam =", A16)
print("CO_P =", CO_P, " CO_C =", CO_C, " Pbar =", Pbar, " slack =", SLACK)

def G0(v): return v * (1 - v) * (2 * v - 1) / 6

def qT(i): return Fr((60 + i) // 3)

def qT2(i): return Fr(math.floor((60 + i) * al / 3))  # = floor(al * tT i); exact for any rational al

def FT(i, x):
    return A6 + A2 * (x - qT(i)) - A16 * (al * x - qT2(i))

def PT(i, x):
    f = x - qT(i); g = al * x - qT2(i)
    return CO_P * g * (1 - g) - lam * f * (1 - f)

def CT(i, x):
    return CO_C * G0(al * x - qT2(i)) - lam * G0(x - qT(i))

def PhiT(i, x):
    return PT(i, x) / x ** 2 + 2 * CT(i, x) / x ** 3 - Pbar / x ** 2 + lam / x - Fr(43, 32) / x ** 2

N = 1140
val = PhiT(N, Fr(400)) - PhiT(0, Fr(20)) + SLACK * (1 / Fr(20) ** 3 - 1 / Fr(400) ** 3)
print("tail bound =", val, "=", float(val))

# optional numeric cross-check of the bound against the true integral
if os.environ.get('SKIP_MPMATH'):
    raise SystemExit
import mpmath
mpmath.mp.dps = 50
def fr(x): return x - mpmath.floor(x)
def Ft(x):
    return 6 * float(lam) + 2 * float(lam) * fr(x) - 16 * float(lam) * fr(float(al) * x)
tot = mpmath.mpf(0)
h = mpmath.mpf(1) / 3000
x = mpmath.mpf(20) + h / 2
while x < 400:
    tot += (x * Ft(x) + mpmath.mpf(43) / 16) / x ** 3 * h
    x += h
print("direct integral ~", tot)
print("margin (bound - true):", float(val) - tot)
