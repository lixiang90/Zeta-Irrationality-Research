# 恢复四重零点的双极点布局：显式平衡测度与完整行列式衰减

日期：2026-10-06。NEW 全尺度证明。所有旧稿、同行稿及其数学 PY/JSON/manifest 均只读，未执行、import 或重跑。本文自己的 NEW 有理区间证书首次且唯一执行一次，18 项 exact checks 通过；该证书只包围闭式常数，下面的全 n 定理由纸面论证给出。

**本轮进展。** 对 s=5、k=4、任意固定整数 B>4，原先完整右轮廓的正包络有显式平衡测度，支撑半径为

\[
R^2=\frac{(B-4)(B+8)}8.
\tag{E1}
\]

由完整曲率得到新的严格衰减系数 β_eq。B=5、6、8 时分别有 β_eq∈(8.108,8.109)、(18.276,18.277)、(46.406,46.407)。这比冻结稿的 y*=1 tangent bounds 严格改善至少0.465、0.799、3.376。下面给出对每个 n≥1 的有限 n 上界，并证明这个正包络的 n² 能量极限恰等于所得值。因此本文没有把形式 saddle point、数值粒子拟合或矩阵正性当作证明。

目前 safe arithmetic A 上界仍为17.834、35.939、81.249，尚未得到 β>A。没有新的 ζ、L 或 Catalan 无理性/线性无关性结论。该 A 是上界，比较未匹配不是不可能性结论；正包络最优性也不是实际复行列式的最优性。

## E2. 真正完整的布局、归一化与固定 kernel 费用

令 d=B−4、h=dn、F_h=∏_{j=0}^{h−1}j!²，取

\[
R_{n;4,B}(z)=\frac{(Bn)!^2}{(2n)!^4}
\frac{\prod_{m=1}^{2n}(z-m)^4}{\prod_{j=0}^{Bn}(z+j)^2}.
\]

固定 a,b∈Z、b≠0，q(z)=πcotπz、K_5=−4a q''−b q'''。定义实际解析泛函及其归一化 Hankel determinant：

\[
L^{\rm an}(P)=4a\sum_{m\ge1}(R_{n;4,B}P)''(m)
 -b\sum_{m\ge1}(R_{n;4,B}P)'''(m),\qquad
J^{\rm an}_n=\frac{\det[L^{\rm an}(z^{i+j})]_{0\le i,j<h}}{F_h}.
\tag{E2}
\]

degP<2h 保证 deg(RP)≤−3，全部 series 绝对收敛。零阶4大于最高 derivative order3，前2n个整数的全部 residues 都为0。因此完整积分位于 Re z=2n+1/2，没有原三重零点布局的 finite head correction。由冻结 [解析稿](cdt_odd_mixed_double_pole_analytic_decay_20261006.md) D24–D28 的全尺度证明，所有 n≥1、x∈R 有

\[
|R_{n;4,B}(2n+1/2+ix)|\le\frac{A_B}n e^{nG_B(x/n)},\quad
A_B=\frac B{\pi(B+2)}e^{2+1/(6B)},
\]
\[
|K_5(2n+1/2+ix)|\le4D_5e^{-2\pi|x|},\quad
D_5=8\pi^3|a|+4\pi^4|b|.
\tag{E3}
\]

G_B 是偶函数，在 y≥0 的公式为

\[
\begin{aligned}
G_B(y)={}&6\log(y^2+4)-(B+2)\log(y^2+(B+2)^2)\\
&+6y\arctan(2/y)-2y\arctan((B+2)/y)
 +2B\log B-8\log2.
\end{aligned}
\tag{E4}
\]

y=0 取连续极限。令 V(y)=2π|y|−G_B(y)、C_B=2A_B D_5/π。实际复 moment density 满足 |ω_n(x)|≤(C_B/n)e^{−nV(x/n)}。有限 Heine 展开、绝对值和 x_i=ny_i 的 scaling 因而给

\[
|J_n^{\rm an}|\le
\frac{C_B^h n^{h(h-1)}}{h!F_h}\,Z_n,
\quad
Z_n=\int_{\mathbf R^h}\Delta(\mathbf y)^2
e^{-n\sum_iV(y_i)}\,d\mathbf y.
\tag{E5}
\]

体积中的 n^h 与原 density 的 n^{−h} 抵消；n^{h(h−1)}来自 Vandermonde。未假设 signed/complex weight 正，也未把任意形式 c 的 rational determinant 识别为 E2；这种识别仍须假设 aζ(4)+bζ(5)=c 的实际候选关系。

## E3. 势函数的正混合结构

记 L=B+2，故 d=L−6>0，并令

\[
V_0=V(0)=2L\log L-2B\log B-4\log2.
\tag{E6}
\]

对 y>0，E4 的直接求导及 atan 恒等式给

\[
V'(y)=6\arctan(y/2)-2\arctan(y/L)
 =6\int_2^L\frac{y}{u^2+y^2}\,du
  +4\int_L^\infty\frac{y}{u^2+y^2}\,du.
\tag{E7}
\]

于是 V 在0也光滑，且

\[
V(y)-V_0=3\int_2^L\log(1+y^2/u^2)\,du
 +2\int_L^\infty\log(1+y^2/u^2)\,du.
\tag{E8}
\]

这是正混合，不需要 V 全局 convex。V(y)=2π|y|+2d log|y|+O_B(1) 当 |y|→∞。下面用正混合直接证明支撑及全域变分不等式；单个 inflection 或猜 one-cut 不作为输入。

## E4. 单个 charge 的 resolvent 与全部混合

先任取 r>0、u>0，记 A_u=√(u²+r²)。定义

\[
\rho_{u,r}(x)=\frac{u\sqrt{r^2-x^2}}
{2\pi A_u(u^2+x^2)}\,1_{|x|<r}.
\tag{E9}
\]

其 Cauchy transform 精确为

\[
W_{u,r}(z)=\int\frac{\rho_{u,r}(x)}{z-x}\,dx
 =\frac12\left[\frac{z}{z^2+u^2}
 -\frac{u}{A_u}\frac{\sqrt{z^2-r^2}}{z^2+u^2}\right],
\tag{E10}
\]

sqrt 的支取在无穷处∼z。证明：右式在 z=±iu 的 apparent poles 因 √(−u²−r²)=±iA_u 完全消失；唯一 jump 在 [−r,r]，其上/下值差为−2πiρ_{u,r}；无穷处为 O(1/z)。Cauchy integral（或大圆与 slit 两岸直接积分）即给 E10。其 mass 为

\[
m_u(r)=\frac12(1-u/A_u).
\tag{E11}
\]

按 E7 同样混合密度与 resolvent：

\[
\rho_r(x)=6\int_2^L\rho_{u,r}(x)du
 +4\int_L^\infty\rho_{u,r}(x)du.
\tag{E12}
\]

密度非负，在 (−r,r) 严格正，边缘为非零常数乘 √(r²−x²)，有界。u→∞的 density、mass、resolvent 均为 O_r(u^{−2})，所以各混合与有限 cut 之外的求导、边界极限均有合法 dominating function；r 在 compact 子区间变化时也一致。其 mass 为

\[
m(r)=3(\sqrt{4+r^2}-2)-(\sqrt{L^2+r^2}-L).
\tag{E13}
\]

m'(r)=3r/√(4+r²)−r/√(L²+r²)>0，m(0)=0。在要求 mass=d=L−6 时，E13 等价于

3√(4+R²)=√(L²+R²)。两边正，平方完全等价，唯一解正好为 E1。没有额外 root。下面 μ=ρ_R(x)dx 的 mass 就是 d。

## E5. 全实轴 Euler–Lagrange 不等式；显式 tails

令 U_r(x)=∫log|x−t|ρ_r(t)dt，采用正 log potential 的 convention。在 cut 内由 E10 的两岸和得 2U'_r=V'；U_r 连续至两个端点（密度有界、log singularity 可积）。故对某个 ℓ(r)，

\[
2U_r(x)-V(x)=\ell(r),\quad |x|\le r.
\]

在 x>r，E10 与正混合给

\[
V'(x)-2U'_r(x)=\sqrt{x^2-r^2}
\left[6\int_2^L\frac{u\,du}{\sqrt{u^2+r^2}(u^2+x^2)}
 +4\int_L^\infty\frac{u\,du}{\sqrt{u^2+r^2}(u^2+x^2)}\right]>0.
\tag{E14}
\]

左侧由偶性反号。所以

\[
2U_r(x)-V(x)\le\ell(r)\quad(x\in\mathbf R),
\tag{E15}
\]

且在 cut 外严格小于。特别对实际 R，令

\[
\mathcal D(x)=V(x)-2U(x)+\ell\ge0.
\tag{E16}
\]

R²=(L²−36)/8<L²/8，因此 L>2R。对 x≥L，只保留 E14 中 u≥x 的4-weight tail，利用 u/√(u²+R²)≥1/√2、u²+x²≤2u²，获得

\[
\mathcal D'(x)\ge\sqrt2\sqrt{1-R^2/x^2}>1.
\]

故 D(x)≥|x|−L 在 |x|≥L；并且

\[
Q_B:=\int_\mathbf R e^{-\mathcal D(x)}dx\le2(L+1).
\tag{E17}
\]

另外由 E9–E12 的逐项正界

\[
0\le\rho_R(x)\le M_B:=\frac R{2\pi}(3-2/L).
\tag{E18}
\]

这两个显式常数将在全 n upper bound 中控制 tail volume 和对角正则化；没有把无限域的有限 sup 直接当作可积上界。

## E6. 对角正则化的自证：负定 kernel

对 ε>0，令 K_ε(x)=½log(x²+ε²)，记 I_ε(ν,σ)=∫∫K_ε(x−y)dν(x)dσ(y)。若 signed finite measure σ 的 mass0且 first absolute moment 有限，则

\[
I_\varepsilon(\sigma,\sigma)
 =-\int_0^\infty\frac{e^{-\varepsilon t}}t
 \left|\int e^{itx}d\sigma(x)\right|^2dt\le0.
\tag{E19}
\]

自证由 K_ε(x)−logε=∫₀∞e^{−εt}(1−cos tx)dt/t 得到。total mass0杀掉两个常数项；cos 双积分为 Fourier modulus²。近0用 first moment 得 |σ̂(t)|=O(t)，远处由 e^{−εt}；因此 Fubini 可先截 t 后 dominated convergence，不缺绝对收敛。本文使用的 σ=ν−μ 中 ν 是有限 empirical measure，μ 有 compact 有界 density，全部条件满足。

对任意 x，由 E18 和直接可积的一维 kernel，

\[
0\le U_\varepsilon(x)-U(x)
\le\frac{M_B}2\int_\mathbf R\log(1+\varepsilon^2/t^2)dt
=\pi M_B\varepsilon.
\tag{E20}
\]

最后积分通过 ε 求导或 t=εu 后 elementary integration by parts 得2πε；不是数值 estimate。I_ε(μ,μ)≥I(μ,μ)。E19也在 ε↓0、有限 log energy 条件下证明普通 log energy 对 mass0 measure 负定，配合 E15 是 μ 的全域平衡变分证据。引用 weighted equilibrium 的一般唯一性时，Saff 的 weight normalization为 w=e^{−V/(2d)}、probability measure μ/d，恰满足其 unbounded admissibility，不混淆 mass d 与 mass1。

## E7. 所有 n≥1 的完整 partition/determinant 上界

令能量

\[
\mathcal E_B=I(\mu,\mu)-\int V\,d\mu.
\tag{E21}
\]

给任意 h=dn 个实数 y_i 取 ν=(1/n)Σδ_{y_i}，其 mass d。E19 对 ν−μ 给 I_ε(ν,ν)≤2I_ε(ν,μ)−I_ε(μ,μ)。因为 K_ε≥log|·|，扣掉 h 个 diagonal K_ε(0)=logε 后，E15–E20 得

\[
\begin{aligned}
2\sum_{i<j}\log|y_i-y_j|-n\sum_iV(y_i)
&\le n^2\mathcal E_B-n\sum_i\mathcal D(y_i)
 +2d\pi M_B\varepsilon n^2-h\log\varepsilon.
\end{aligned}
\tag{E22}
\]

此处 dℓ−I(μ,μ)=E_B，由 E15 在 μ 上积分直接成立。重复节点的左侧为−∞，不等式仍成立。取 ε=1/n，并用 n≥1、D≥0、E17，就有

\[
\boxed{Z_n\le[2(L+1)]^h\,
e^{n^2\mathcal E_B+2d\pi M_B n}\,n^h.}
\tag{E23}
\]

关键是保留并积分 D 的 tail，不只在 R^h 上取 sup。将 E23 代入 E5，得到完全显式、全 n≥1 的结果

\[
\boxed{|J_n^{\rm an}|\le[2(L+1)C_B]^h
\exp\{n^2\mathcal E_B+dR(3-2/L)n\}
\frac{n^{h^2}}{h!\prod_{j<h}j!^2}.}
\tag{E24}
\]

固定 kernel、R_n uniform prefactor、tail volume 和对角 self-energy 全部付费。标准 elementary Stirling 求和给

logF_h=h²logh−(3/2)h²+O(hlog(h+1))、logh!=O(hlog(h+1))。

例如把 logj!=jlogj−j+O(log(j+1)) 从 j=1 到 h−1 相加，再以 increasing xlogx 的 integral comparison 即得；没有 large-n 数值拟合。故

\[
\boxed{\log|J_n^{\rm an}|\le-\beta_{\rm eq}(B)n^2+O_{B,a,b}(n\log(n+1)),}
\quad
\beta_{\rm eq}(B)=-\mathcal E_B+d^2\log d-\frac32d^2.
\tag{E25}
\]

零 determinant 取 log=−∞；本文未用 Z_n>0 推断 J_n 非零。

## E8. 变分常数与能量的实际闭式计算

为使 E25 不依赖未知的二重积分，先计算 ℓ(r)。E9 等于一半质量1的 interval balayage density 减 u/(2A_u) 的 arcsine density；用 x=r cosθ 写为

\[
\rho_{u,r}(x)dx
=\left[\frac{uA_u}{2\pi(u^2+r^2\cos^2\theta)}
-\frac{u}{2\pi A_u}\right]d\theta.
\]

令 t=(A_u−u)/r∈(0,1)。第一个质量1 density（上式的两倍第一项）的 Fourier series为 (1/π)[1+2Σ_{k≥1}(−t²)^kcos2kθ]。结合 log|r cosθ|=log(r/2)+Σ_{k≥1}(−1)^{k−1}cos2kθ/k，积分给

\[
2\int\log|x|\rho_{u,r}(x)dx
=(1-u/A_u)\log(r/2)+\log\frac{2u}{u+A_u}.
\tag{E26}
\]

两级数相乘可先 Abel regularize 后取极限；t<1给第一 series 一致绝对收敛，第二 log singularity 可积，合法。不需假定未计算的 balayage normalization。

对正混合求和，在 x=0 评价 E15 得

\[
\ell(r)=-V_0+2m(r)\log(r/2)+6I_2(r)-2I_L(r),
\]
\[
I_a(r):=\int_a^\infty\log\frac{2u}{u+\sqrt{u^2+r^2}}du
=a-\sqrt{a^2+r^2}-a\log\frac{2a}{a+\sqrt{a^2+r^2}}.
\tag{E27}
\]

右式由 integration by parts 得到；at∞ endpoint为0。于是

\[
\ell(r)=-V_0+2m\log(r/2)-2m
 -12\log\frac4{2+\sqrt{4+r^2}}
 +2L\log\frac{2L}{L+\sqrt{L^2+r^2}}.
\tag{E28}
\]

E27 求导（正尾 integrable）给 ℓ'(r)=2m'(r)log(r/2)。沿此 mass m(r) family，能量 E(r)满足 E'(r)=ℓ(r)m'(r)：微分 I−∫V 得∫(2U_r−V)d(∂_rμ_r)，而该 integrand 在其 support 上等于ℓ。严格合法性可将 x=r cosθ、y=r cosφ 固定到 [0,π]：density weight 光滑且在端点为 O(sin²θ)，其 r derivative 亦如此；log|cosθ−cosφ|可积，V 光滑，compact r interval 具有统一 dominating function。亦可用负定性与 E15 的两个 mass 比较夹逼此导数。r↓0 的能量趋0，m²logr趋0，故 integration by parts 得

\[
\mathcal E_B=d\ell(R)-d^2\log(R/2)
 +\int_0^R\frac{m(r)^2}r\,dr.
\tag{E29}
\]

这一步保留了 mass derivative，不能直接把 ℓ 乘 d 当作完整能量。

## E9. 消去剩余一维积分；β 完全为有理数的 logarithms

令 T=R²、A=√(4+T)、C=√(L²+T)。实际端点有 C=3A。定义

\[
J_a(T)=\sqrt{a^2+T}-a-a\log\frac{a+\sqrt{a^2+T}}{2a},
\]
\[
J_{2,L}(T)=\int_0^R\frac{\sqrt{(r^2+4)(r^2+L^2)}-2L}r\,dr.
\]

展开 m(r)=3√(4+r²)−√(L²+r²)+d，并在 r=0 消掉常数项，就有

\[
\int_0^R\frac{m(r)^2}rdr
=5T-6J_{2,L}(T)+6dJ_2(T)-2dJ_L(T).
\tag{E30}
\]

令 M=L²+4、P=4L²、S(t)=√(t²+Mt+P)。一个直接求导即可核的 primitive 是

\[
\int\frac{S(t)}t dt
=S(t)+\frac M2\log(t+M/2+S(t))
-2L\log\frac{2LS(t)+P+(M/2)t}{t}.
\]

分别扣掉2L logt并取0 endpoint，得到

\[
J_{2,L}(T)=\frac12\left[S(T)-2L+
\frac M2\log\frac{T+M/2+S(T)}{M/2+2L}
-2L\log\frac{2LS(T)+P+(M/2)T}{2P}\right].
\tag{E31}
\]

在 T=(L²−36)/8 时，S(T)=3(L²−4)/8；两个 log arguments 精确分别化为 2(L−2)/(L+2) 与 (L²−4)(L+6)²/(128L²)。把 E28–E31 代入 E25，所有含 A,C 的 log 项抵消，剩余多项式项化成−d²，最终得到

\[
\boxed{\begin{aligned}
\beta_{\rm eq}(B)={}&d[2L\log L-2B\log B-4\log2]
 +\frac{d^2}2\log\frac{32d}{d+12}-d^2\\
&+\frac32(L^2+4)\log\frac{2(L-2)}{L+2}
 -6L\log\frac{(L^2-4)(L+6)^2}{128L^2},
\quad d=B-4,\ L=B+2.
\end{aligned}}
\tag{E32}
\]

Intermediate check：E29也给 β=dV₀+d²log(2d/R)−(3/2)d²−5T+6J_{2,L}(T)。利用4T=(d²/2)+6d，即还原 E32。这个 check 可以独立定位符号、factor2与 h normalization。

## E10. 严格数值窗口与实际改善

NEW [有理区间证书](cdt_odd_restored_zero_equilibrium_energy_verify_20261006.py) 只首次执行一次，输出 [NEW certificate](cdt_odd_restored_zero_equilibrium_energy_verify_20261006.json)。对 r∈[1,2] 用 t=(r−1)/(r+1)，

\[
2\sum_{j=0}^{79}\frac{t^{2j+1}}{2j+1}
\le\log r\le
2\sum_{j=0}^{79}\frac{t^{2j+1}}{2j+1}
 +\frac{2t^{161}}{161(1-t^2)}.
\tag{E33}
\]

任意 positive rational r 以2的整幂移到 [1,2)，log2同样求有理上下界；negative coefficients 反转 interval endpoints。全部输出使用 Fraction，未用 float、finite n fit、PSLQ。18 checks包括 mass squared identity、E31 arguments 的有理恒等式、窗口及与冻结 tangent/cost 上界的方向核对。

|B|h|R²|β_eq严格窗口|相对冻结 tangent upper 的严格 gain|冻结 safe A 上界|
|---|---:|---:|---:|---:|---:|
|5|n|13/8|(8.108,8.109)|>0.465|17.834|
|6|2n|7/2|(18.276,18.277)|>0.799|35.939|
|8|4n|8|(46.406,46.407)|>3.376|81.249|

旧 tangent windows (7.642,7.643)、(17.476,17.477)、(43.029,43.030) 来自已冻结且本轮实际全文回读的 [root budget](cdt_odd_double_pole_layout_budget_root_20261006.md) R8；本文没有执行其三个 producer。表的严格 gain 只比较已证明常数的 bound，不称旧 bound 最优。当前 safe A−β 的 gap 仍为 positive；A 是真实费用的安全上界，不能把此差号变成费用下界或 no-go。

## E11. 正包络的精确 n² 门槛及其范围

E23 给 limsup n^{−2}logZ_n≤E_B。反向也可实际证明，令 p(x)=ρ_R(x)/d 是 cut 上 probability density。有界、端点 square-root vanishing 保证 log energy I(p)与 entropy H(p)=∫p logp 都有限。将 Z_n 的积分限制到 cut，按 p^h 改写，Jensen 给

\[
\log Z_n\ge h(h-1)I(p)-nh\int Vp-hH(p)
=n^2\mathcal E_B-dn[I(p)+H(p)].
\tag{E34}
\]

被取 log 的 random positive density 几乎处处 positive；重复节点为概率0，log integrable。由 E23、E34，

\[
\boxed{\lim_{n\to\infty}n^{-2}\log Z_n=\mathcal E_B.}
\tag{E35}
\]

所以 E25 的 β_eq 是**E3 的固定右直线正包络 model**在当前归一化下的精确 n² 系数。继续将同一个 Z_n 换成更漂亮的 tangent、reference norm 或 Fekete upper bound，不能突破 E35；能严格改善的是以前对该 model 的粗上界。E35不是 actual complex J 的 lower bound，复 phase cancellation 可使真实 J 更小甚至0；更好的 contour、真正不同正包络、整格 content、paired restriction 仍可能改变 margin。

也没有默认 real contour shift 可任意向右：跨过 m>2n 的新整数会产生真实 residues。本文全部证明固定在 Re z=2n+1/2；任何 contour deformation 尚须逐项核完整 residue 与 complex Vandermonde energy。

## E12. 一手来源、实际阅读与冻结状态

实际全文重读冻结解析稿 D1–D31，SHA c4e8f04f0debe34cf896780424e6ceb256747eaca0d3ed3b9698802757447218；实际全文重读 root budget R1–R9，SHA644f7dbf8e01ec85f938c49435becded48533c88577f712999b6eecb0ae7c3c5。原件 Lai 的前轮实际阅读范围仅 PDF1–7、17–25，共16页；本轮没有重新登记为全文25页。

实际读取父任务正常TLS新增归档的 [Saff2010](../literature/saff2010_logarithmic_potential_arxiv1010_3760v1_20261006.pdf) PDF32–36，尤其 §6 的 admissible unbounded weight、Theorem6.1、(6.2) variational characterization，PDF33中的 mass1 convention。原件36页、SHA cfbeaad8cf695fc1b5528fd56295d7e3053056634c6841765a434ce9b074d862；首个GBK抽文本中断，UTF-8重新读取上述完整5页成功，不将失败输出当作已读。归档由父任务完成，本文未下载或改该PDF；没有声称读全36页、Brown34页或Monien12页。可复核原件链接：[arXiv1010.3760v1](https://arxiv.org/pdf/1010.3760v1)。本文 E9–E35 使用显式自证，不从一般 Fekete theorem 直接省掉 n-dependent weight、无限 tail 或 self-energy。

NEW来源收据另存 literature/manifest_cdt_odd_restored_zero_equilibrium_energy_20261006.json，记录 actual scope 与最终 pins。自己数学 producer=1个×首次一次；旧/同行 producer=0。PDF文本抽取、hash与metadata读取不是数学 producer。保存后全文回读，独审另存；本文结论未获 Lean 认证。
