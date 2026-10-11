# 交错 ζ 单周期投影的真实轮廓与带权实处界

2026-10-07。令 η(s)=(1−2^{1−s})ζ(s)。本稿在偶整数节点上构造真实 η(s) 投影，使较低周期完全消失，同时保留交错级数的指数轮廓核。它为 ζ(5)、ζ(7) 提供同目标的新解析对象，并非把 β(4) 的 sec 常数移植给非交错 ζ。

固定 2≤r≤7、s=r+1，本文证明实际 determinant 的完整有限 n 上界
\[
\log|\det E_n^\eta|\le-\gamma_r^\eta n^2+O_r(n\log(n+2)).
\tag{A1}
\]
γ 由下文准确的概率测度和定积分定义。ζ(5) 的 γ₄>1 有纯符号证明；ζ(7) 的 γ₆>9/100 有下文可复算的严格复球积分证书。新对象的完整有限处分母由同轮[全素数稿](cdt_eta_projection_all_prime_budget_20261007.md)独立处理。现有安全预算仍远大于上述收缩，无限非零性也未完成；本文不证明新的数值无理性或线性无关性。

## 1. 同目标的实际偶节点对象

令 J={0,…,n−1}、I={n,…,rn−1}、H=rn，采用原真实 Hermite 投影
\[
P_J(z)=\prod_{k\in J}(z-k),\quad Q_I(z)=\prod_{u\in I}(z-u),\quad
B_k=P_J/(z-k),\quad D=P_JQ_I,
\]
\[
\Phi_k(z)=Q_I(z)/B_k(z)^{r-1},\quad
N_k(z)=B_k(z)^r[\Phi_k]_{k,<r}(z),\quad
P_{ku}=N_k(u)/D'(u),\quad F_k=N_k/D.
\tag{A2}
\]
已证 regular-part 条件为 P_{kv}=δ_{kv}（v∈J）及
Σ_{u≠v}P_{ku}/(u−v)^ℓ=0（1≤ℓ≤r−1）。定义
\[
C_r^\eta(u,v)=\int_0^1\!\int_0^1
\frac{x^{2u}y^{2v}}{1+xy}\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
=\sum_{a\ge1}\frac{(-1)^{a-1}}{(a+2u)(a+2v)^r},\qquad E_n^\eta=PC_r^\eta.
\tag{A3}
\]
几何部分和在 0≤xy≤1 一致有界，可用 dominated convergence；所得数值级数绝对收敛。对有限尾 A_{u,b}^η=Σ_{a=1}^{2u}(−1)^{a−1}/a^b，部分分式及 A2 给准确身份
\[
E_n^\eta=q_n^\eta+\eta(s)I_n,\qquad
q_{kv}^\eta=(-1)^{r-1}2^{-r}
\sum_{u\ne v}\frac{P_{ku}(A_{u,1}^\eta-A_{v,1}^\eta)}{(u-v)^r}
-\delta_{kv}A_{v,s}^\eta.
\tag{A4}
\]
偶数移位保持交错相位；一阶差先合成，所有较低 η(b) 系数由 regular-part 条件消去，不假设其有理。η(s) 是 ζ(s) 的非零有理倍数。n=1 时 F₀=1/z、P=(1,0,…,0)，实际 E₁=η(s)，并非误多一个 2^{-s} 因子。

## 2. 同一投影的指数轮廓核

取 c=1/4。若 h 在 Re a≥c 上无极点且 h(a)=O(|a|^{-2})，留数定理直接给
\[
\sum_{j\ge0}(-1)^j h((j+1)/2)
=\int_{\mathbb R}h(c+it)\csc(2\pi(c+it))\,dt
=\int_{\mathbb R}h(c+it)\operatorname{sech}(2\pi t)\,dt.
\tag{A5}
\]
证明在左右边 Re a=c 与 R=M+1/4 的矩形进行：csc(2πa) 在 a=(j+1)/2 的留数为 (−1)^{j+1}/(2π)，左边向下的积分为 −i 倍右侧，留数和为 −i 倍左侧。上下边因指数衰减趋零；右边的积分是 O(R^{-2})。先取高度极限，再令整数 M→∞，所有步骤绝对收敛。

A3 与 F 的部分分式给
\[
E_{kv}^\eta=-2^{-s}\sum_{j\ge0}
\frac{(-1)^j F_k(-(j+1)/2)}{((j+1)/2+v)^r}
=-2^{-s}\int_{\mathbb R}
\frac{F_k(-a)}{(a+v)^r}\operatorname{sech}(2\pi t)\,dt,\qquad a=c+it.
\tag{A6}
\]
F_k(-a)/(a+v)^r 在此半平面无极点，衰减 O(|a|^{-r-1})，满足 A5。这里先保留相位再取轮廓绝对值，不能先把交错级数逐项取绝对值。

写 Φ_k(k+w)=a_kΣ_{ℓ≥0}h_{k,ℓ}w^ℓ、a_k=Φ_k(k)、h_{k,0}=1，则
\[
F_k(-a)=(-1)^r a_k W_n(a)G_k(a),\quad
W_n(a)=\frac{P_J(-a)^{r-1}}{Q_I(-a)},\quad
G_k(a)=\sum_{\ell=0}^{r-1}\frac{(-1)^\ell h_{k,\ell}}{(a+k)^{r-\ell}}.
\tag{A7}
\]
故 A6 的行常数为 (−1)^{r+1}2^{-s}a_k。a_k 可以非常大，其完整乘积必须支付。

## 3. 固定阶行导数与两个 Cauchy 外积

本节完整重作原[β4 轮廓稿](cdt_beta4_real_determinant_energy_20261007.md) R12–R18 的比较，阶数改为 r−1。取固定圆盘半径 ρ=1/8<c。Cauchy double alternant 与逐行圆盘导数给
\[
\left|\det_{k,i}G_k(a_i)\right|,
\left|\det_{v,i}(a_i+v)^{-r}\right|
\le e^{O_r(n\log(n+2))}
\frac{V_n|\Delta(a)|}{\prod_{i,k}|a_i+k|},
\tag{A8}
\]
其中 V_n=∏_{j=1}^{n-1}j!，Δ(a)=∏_{i<j}(a_j−a_i)。两式的隐含常数可以不同。

细节：对 k 这一行，(a+k)^{-d}=(−1)^{d−1}∂_k^{d−1}(a+k)^{-1}/(d−1)!。A7 的行导数算子是各固定系数 h_{k,ℓ} 乘这些导数，阶数≤r−1。每个阶数的 Cauchy factorial 与 1/(d−1)! 正好抵消。log Φ 的一阶有限调和和为 O_r(log(n+2))，更高阶为 O_r(1)，故 |h_{k,ℓ}|≤C_r(1+log(n+2))^ℓ。全部行系数及 ρ^{-(r-1)n} 只付 O_r(n log(n+2))。

移位 V(J) 的误差由 Σ_{d=1}^{n-1}(n−d)log(1+2ρ/d) 控制；分母误差由 nΣ_{k=0}^{n-1}−log(1−ρ/(c+k)) 控制，两者均 O(nlog(n+2))。若 a_i 重合，两侧都有 Δ(a)=0，身份和上界由连续性成立。

对 A6 用复测度 Andreief（展开 determinant 和 Fubini 即证），保留 Δ(t)^2。两个 Cauchy 分母准确取消 P_J 的两次幂，得到
\[
|\det E_n^\eta|\le e^{O_r(n\log(n+2))}\frac{A_{r,n}}{n!}
\int_{\mathbb R^n}\Delta(t)^2
\prod_i e^{-2\pi|t_i|}
\frac{|P_J(-c-it_i)|^{r-3}}{|Q_I(-c-it_i)|}\,dt_i,
\tag{A9}
\]
\[
A_{r,n}=\Bigl(\prod_k|a_k|\Bigr)V_n^2
=\frac{V_{rn}}{V_{(r-1)n}V_n^{2r-3}}.
\tag{A10}
\]
对于 r=2，A9 的 P_J 指数为 −1，绝不将它丢掉。A10 由各个阶乘精确相乘成立。

## 4. 全权重势及尺度取消

对所有实 x，取 t=nx。关于 y 的 log√(x²+y²) 单调，按节点 (k+c)/n 作 Riemann 比较给一致估计
\[
\log|P_J(-c-inx)|
=n\log n+\frac n2\int_0^1\log(x^2+y^2)dy+O(\log(n+2)),
\]
\[
\log|Q_I(-c-inx)|
=(r-1)n\log n+\frac n2\int_1^r\log(x^2+y^2)dy+O_r(1).
\tag{A11}
\]
第一式在首格令 y=w/n；点值与首格积分的差为 log√(c²+(nx)²)−∫₀¹log√(w²+(nx)²)dw，它对 nx 一致有界。余格的误差望远镜至多 log n+O(1)。第二式因 y≥1 而导数≤1/y，直接有一致 O_r(1)。因此 r=2 的负指数也已被双向误差覆盖。

令
\[
V_r(x)=2\pi|x|+\frac12\int_1^r\log(x^2+y^2)dy
-\frac{r-3}{2}\int_0^1\log(x^2+y^2)dy,
\]
\[
\mathcal Z_{r,n}=\frac1{n!}\int_{\mathbb R^n}\Delta(x)^2e^{-n\sum_iV_r(x_i)}dx,
\quad
\kappa_r=\frac{r^2}2\log r-\frac{(r-1)^2}2\log(r-1)-\frac32.
\tag{A12}
\]
A9–A11 的权重给 −2n²logn，变量代换与 Vandermonde 给 +n²logn，而
log A_{r,n}=n²logn+κ_r n²+O_r(nlog(n+2))。故完整尺度准确取消：
\[
\log|\det E_n^\eta|\le\kappa_r n^2+\log\mathcal Z_{r,n}+O_r(n\log(n+2)).
\tag{A13}
\]
势 V_r 为偶函数、全局 Lipschitz，且 V_r(x)=2π|x|+2log|x|+O_r(1) 于无穷远。

## 5. 含负 charge 的显式正概率平衡测度

对 2≤r≤7，令 a>0 为
\[
(7-r)a=\sqrt{r^2+a^2}-(r-2)\sqrt{1+a^2}.
\tag{A14}
\]
的唯一正解。把右式移至左边，函数在0为 −2、在无穷远为 4a+o(a)；其导数在 r≤6 时由 7−r−a/√(r²+a²)>0 以及非负余项为正，在 r=7 时为 a(5/√(1+a²)−1/√(49+a²))>0。因此唯一性成立。特别
\[
a_4^2=1/3,\quad a_6^2=(11-\sqrt{46})/6,\quad a_7^2=1.
\tag{A15}
\]
这些根另满足未平方的 A14，不以平方方程的任意根替代。

令 ω_a(dx)=dx/(π√(a²−x²))、ν_y(dx)=y√(y²+a²)ω_a(dx)/(x²+y²)，皆为概率。λ_a=(2π/π)∫₀ᵃω_s ds 的质量为2a。定义先验符号组合
\[
\mu=\lambda_a+\frac12\int_1^r\nu_y\,dy
-\frac{r-3}{2}\int_0^1\nu_y\,dy-2a\omega_a.
\tag{A16}
\]
其质量准确为1。用 A14 消去 inverse-square-root 边缘，设 s_x=√(a²−x²)，其密度为
\[
\rho_r(x)=\frac2\pi\log\frac{a+s_x}{|x|}
+\frac{s_x}{2\pi}\left[
\int_1^r\frac{y\,dy}{(x^2+y^2)\sqrt{a^2+y^2}}
-(r-3)\int_0^1\frac{y\,dy}{(x^2+y^2)\sqrt{a^2+y^2}}\right].
\tag{A17}
\]
负 charge 的正性须核实。令 f_x(y)=y/((x²+y²)√(a²+y²))。变量 q=√(a²+y²) 给
∫₀^∞f_x(y)dy=s_x^{-1}log((a+s_x)/|x|)。故准确地
\[
\rho_r(x)=\frac{s_x}{2\pi}\left[(7-r)\int_0^1f_x(y)dy
+5\int_1^rf_x(y)dy+4\int_r^\infty f_x(y)dy\right]>0
\quad(0<|x|<a).
\tag{A18}
\]
μ 因而为真实概率，不是签名测度的假定解。它有有限对数能量，ρ≤C_r(1+|log|x||)。另一便于复算的准确式为
\[
\rho_r(x)=\frac1{2\pi}\left[(7-r)\operatorname{atanh}(s_x/a)
+(r-2)\operatorname{atanh}(s_x/\sqrt{a^2+1})
-\operatorname{atanh}(s_x/\sqrt{a^2+r^2})\right].
\tag{A19}
\]

## 6. 内外势身份及准确常数

记 U_μ=∫log|z−x|dμ(x)。ω_a 的 Cauchy transform 为1/√(z²−a²)，ν_y 的为
(z+y√(y²+a²)/√(z²−a²))/(z²+y²)，λ_a 的为2arcsin(a/z)。内部主值给
2U_μ'(x)=V_r'(x)（0<|x|<a）。偶对称和势连续性将0两侧连接。

对 x>a，置 t=√(x²−a²)、f_x(y)=y/((x²+y²)√(a²+y²))。A14 与 Cauchy transform 准确给
\[
(2U_\mu-V_r)'(x)
=-t\left[(7-r)\int_0^1f_x(y)dy
+5\int_1^rf_x(y)dy+4\int_r^\infty f_x(y)dy\right]<0.
\tag{A20}
\]
这里使用 ∫₀^∞f_xdy=t^{-1}arctan(t/a) 与 arcsin(a/x)=π/2−arctan(t/a)。故实轴上的 Frostman 身份和严格外部不等式均已直接验证。

定义 φ_a(y)=ylogy−y−yarsinh(y/a)+√(a²+y²)，φ_a(0)=a。arcsine/ν_y 的0点 log 势积分给
\[
U_0=U_\mu(0)=-2a+\frac12\left[\phi_a(r)-(r-2)\phi_a(1)+(r-3)a\right],
\quad V_0=V_r(0)=r\log r-2,
\]
\[
\ell=2U_0-V_0,\quad
J_r=\ell/2-\frac12\int_{-a}^aV_r(x)\rho_r(x)dx,
\quad \gamma_r^\eta=-\kappa_r-J_r.
\tag{A21}
\]
尤其 V₀ 非零，不能将 ℓ 错作2U₀。ν_y 的0点势为 logy−arsinh(y/a)，对 y↓0 只有可积 log 奇异；将其代入 A16，arcsine 项准确取消，得到 A21。

由已直接证明的势条件、ρ 的 log 密度上界、V 的 Lipschitz 性和线性增长，[带权能量稿](cdt_beta4_weighted_energy_20261007.md) W23–W29 的有限 n 引理逐项适用：以半径 (n+1)^{-2} 的圆周平滑经验测度，零质量 log 能量≤0；一致势模量为 O_r(ε(1+|logε|)²)。在积分中留下一份 e^{-V_r} 支付非紧尾（其积分有限），得到
\[
\log\mathcal Z_{r,n}\le J_r n^2+O_r(n\log(n+2)).
\tag{A22}
\]
V_r 即使可能有负值，也只改变有限区间中的常数：无穷远仍有正线性增长，因此 W25 的 λ_n=1−1/n 外部控制与最后剩余积分仍有效。A13/A22 证明 A1。没有把振荡积分的上界误作渐近等号。

## 7. ζ5 的符号衰减及 ζ7 的严格区间证书

从 ∫₀^∞log(1+x²/y²)dy=π|x| 得
\[
V_r(x)\ge V_0+\frac{(7-r)\pi}{2}|x|\quad(3\le r\le6).
\tag{A23}
\]
线性势 c|x| 的最大加权 log 能量为 log(π/(2c))−3/2（可由 λ_{π/c} 直接重证）。r=4 代入 c=3π/2 给纯符号界
\[
\gamma_4^\eta\ge1+\frac{11}{2}\log3-4\log4>1,
\tag{A24}
\]
最后一步等价于 3¹¹>4⁸，可由整数比较确认。它不需要浮点。

对 r=6，令 ε=2^{-16}，以 x=a sinθ、s_x=a cosθ 写 A19，使用稳定身份 atanh(cosθ)=log cot(θ/2)。由 A23，V₆≥V₀>0，而 A18 给ρ>0。因此删去 θ∈(0,ε) 的正积分后
\[
\gamma_6^\eta\ge-\kappa_6-U_0+V_0/2+
\frac12\int_\varepsilon^{\pi/2}2V_6(a\sin\theta)\rho_6(a\sin\theta)a\cos\theta\,d\theta.
\tag{A25}
\]
下列全新内联 Python/python-flint 调用在160-bit精度完成严格复球积分；所有 log 的 analytic flag 正确转交，分支不可解析的球返回非有限值。官方接口语义核于[python-flint acb 文档](https://python-flint.readthedocs.io/en/latest/acb.html)。这不是普通高精度浮点或 Lean 形式化。

```python
from flint import arb, acb, ctx
ctx.prec = 160
r = 6
aa = (arb(11) - arb(46).sqrt()) / 6
a, pi = aa.sqrt(), arb.pi()
eps = arb(1) / 2**16
q1, qr = (aa+1).sqrt(), (aa+r*r).sqrt()
def log(z, analytic): return z.log(analytic=analytic)
def atanh(z, analytic):
    return (log(1+z, analytic)-log(1-z, analytic))/2
def atan(z, analytic):
    return (log(1+acb(0,1)*z, analytic)
            -log(1-acb(0,1)*z, analytic))/acb(0,2)
v0 = arb(r)*arb(r).log()-2
u0 = -2*a
for y, c in ((r,1), (1,-(r-2))):
    yy = arb(y)
    phi = yy*yy.log()-yy-yy*(yy/a).asinh()+(aa+yy*yy).sqrt()
    u0 += c*phi/2
u0 += (r-3)*a/2
kap = arb(r*r)/2*arb(r).log()-arb((r-1)**2)/2*arb(r-1).log()-arb(3)/2
def f(t, analytic):
    sx, x = a*t.cos(), a*t.sin()
    rho = ((7-r)*log((t/2).cos()/(t/2).sin(), analytic)
           +(r-2)*atanh(sx/q1, analytic)-atanh(sx/qr, analytic))/(2*pi)
    v = (v0+(7-r)*pi*x/2+x*((r-2)*atan(x, analytic)-atan(x/r, analytic))
         +arb(r)/2*log(1+x*x/(r*r), analytic)
         -arb(r-2)/2*log(1+x*x, analytic))
    return 2*v*rho*a*t.cos()
ev = acb.integral(f, eps, pi/2, rel_tol=arb('1e-16'),
                 abs_tol=arb('1e-16'), eval_limit=100000, depth_limit=60)
g = -kap-u0+v0/2+ev.real/2
print(ev, g, g > arb(9)/100, ev.imag.contains(0))
```

实际输出为截断 EV∈[9.50783214393832±5.54·10^{-15}]、其虚部包含0；A25右侧 g∈[0.095581636697492±7.81·10^{-16}]，并返回 g>9/100 为 True。因此严格有
\[
\boxed{\gamma_6^\eta>9/100.}
\tag{A26}
\]
这一小区间包围的是严格下界 g，不是未截断 γ 的整个值。50位 mpmath 另算完整定积分仅作说明：γ₄≈1.5530387621、γ₆≈0.0958612541、γ₇≈−0.7952910505。r=7 的负上界信息不是实际 determinant 增长或普遍不可能性证明。

## 8. 现有两个精确常数仍没有严格费用差额

这一步也不只靠说明性小数。Frostman 条件和零质量能量证明 J_r 是实际势的最大加权能量。取 [−1,1] 上的均匀概率 ν，I(ν)=log2−3/2。对于 r≥3 和 |x|≤1，A12 给
V_r(x)≤V₀+2π|x|+(r−1)log2/2，因此
\[
J_r\ge\log2-3/2-V_0-\pi-(r-1)\log2/2,
\quad
\gamma_r^\eta\le V_0+\pi+3/2+(r-3)\log2/2-\kappa_r.
\tag{A27}
\]
r4右侧为 π+1−(15/2)log2+(9/2)log3；r6为 π+1−(21/2)log2−12log3+(25/2)log5。使用纯有理级数界 π<22/7、log2>69/100、109/100<log3<11/10、log5<161/100，可得
\[
\gamma_4^\eta<1097/280<4<9389/630=C_\eta(4),\qquad
\gamma_6^\eta<138/35<4<503807/20020=C_\eta(6).
\tag{A28}
\]
π界由正积分 ∫₀¹x⁴(1−x)⁴/(1+x²)dx=22/7−π 给出。log2 的前两项为56/81>69/100，log3 的前三项为263/240>109/100，来自 log u=2Σ_{k≥0}((u−1)/(u+1))^{2k+1}/(2k+1)。上界用正指数级数：e^{11/10} 的前9项>3，e^{161/100} 的前12项>5；本轮新 inline Fraction 已准确核两项有限和及两个有理 B 上界。因此上述安全有限处常数与这个确切平衡上界确实没有费用余量。它们不是最小分母与真实振荡 determinant 极限，A28不证明该模型整体不可能成功。

## 9. 作用范围与本轮检查

此处已把真实单周期投影、全行归一化、交错轮廓、一般固定阶行导数、全权重平衡和有限 n 能量连接。它改变了前轮 plain ζ 的正上界，确实为同一个 ζ5/ζ7 目标获得指数收缩；整模型费用与非零仍需同对象支付。依据 CDT 的[有效 holonomy 版本 §2.1](https://arxiv.org/html/2510.04156v1#S2)，有限矩阵模型不能替代实际 Q[[x]] 函数芽的独立 Q(x) 秩、denominator types 与共同亚纯映射。本文没有这样替代。

root 实际全文读 β4 weighted 稿 W1–W33；β4原轮廓稿本轮实际读取 R3–R25，A5–A13 另独立重证；一般 ζ 算术稿的正文在本轮一次批量输出曾截断，未据该次读取声称全文再读。新增计算为：前续轮一段40位浮点因 cosθ 在极小 θ 舍入为1而失效，无结果采用；当前以 logcot 和正确非零 V₀ 修正的50位说明计算；当前一段严格复球证书；当前一段 A28 有理级数验证。没有运行旧producer、guard、prime table或Lean。新增PDF页数0，文献PDF下载0。

独立 energy 代理已实际全文审查原八节 A1–A26，逐项重推轮廓符号和常数、一般r导数和全部规模、全x Riemann误差、负charge的正性及严格外部不等式、非零V₀、删去正tail的下界；数学 PASS。另独立复跑160-bit复球证书，EV和g的输出逐位一致、有限性与虚部包含0、g>9/100全部通过，未将50位说明值称为已独立复算。新增 A27/A28 又经该代理实际全文回读最终九节并独审：均匀试测度能量、全势上界方向、r4/r6化简、π正积分与当前费用比较全部 PASS，另以新 inline Fraction 独立核两项有限指数和、log下界及两个有理上界。root 收讫后修正 A6/A16 两处 LaTeX 空格排版，回读最终全文；本稿尚无机器形式化验证。官方 acb 原始网页和读取范围另存于[本轮文献记录](../literature/python_flint_acb_integral_docs_20261007.json)。
