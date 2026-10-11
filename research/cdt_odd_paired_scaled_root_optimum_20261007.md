# 原配对格的根尺度优化、双峰等高条件与可支付的解析率

日期：2026-10-07。本文研究原 B6/κ3/s5、degree<3n、rank2n 的原饱和格 S 与原 whole-X 多项式 D_A(X)。本轮已保存的 NEW elementary FIRST1 source/result/guard 只读；继任撰稿者实际完整阅读三件，不执行、不 import、不重跑。此前 518 冻结记录保持不动。本稿的 all-n 与 all-s 结论是纸面证明；有限有理区间只认证文中注明的实数常量。最终收据待实际独立复核后另存。

## S1. 固定对象和问题

沿用 [coupled Gram 稿 C1–C9](cdt_odd_paired_coupled_gram_decay_20261007.md) 的真实轮廓、原低高列和 determinant1 剪切。设 c_n=2n+1/2、N=floor(n/2)，选

\[
q_{n,s}(z)=((z-c_n)^2+s n^2)^N,\qquad s>0.
\tag{S1}
\]

degree(q)=2N≤n，所有实际 head j=1,…,2n 上 q(j)>0。对每个 1/(z−j) 减去 (q(z)−q(j))/((z−j)q(j))，所得余项 q(z)/((z−j)q(j)) 精确；所减项 degree≤n−1，在原高列 span 中。因此对所有 X，剪切前后 D_A(X) 完全相同。剪切系数可在 Q 或 C 中，整化费用仍作用于这个同一多项式；不假称新列是免费整基。取 s=4/7 时 q 系数有理。

实际复 measure 的正 Gram 包络给此前 C9 的全 n 不等式

\[
|D_A(\xi)|\le
\frac{Z_{H,n} A_n(q)^n}{F_n^2\Gamma_n^2}
\left(\sum_{a\in\mathcal A_n}
\prod_{m=1}^n\frac{|\widetilde\kappa_{a_m}|}{q(a_m)}
\sqrt{\mathcal H_n(a)}\right)^2.
\tag{S2}
\]

这里 ξ=aζ(4)+bζ(5)、b≠0，𝒜_n 为每个 pair {m,2n+1−m} 恰取一个实际 head 的集合，A_n(q)=sup_x W_n(x)|q(c_n+ix)|²；Z_H、F、Γ、κ̃、Hardy determinant 均是此前的同一实际对象。只有假设 ξ∈Q 后，才能把积分取值当作相应 rational input 的 D_A 值。本文不以正 Gram 的严格正性推出真实复行列式非零。

冻结 uniform envelope 为

\[
W_n(ny)\le Cn^{4n+C}(1+|y|)^C e^{nQ(y)},
\quad Q(y)=12\log6-6\log2-6+7J_2(y)-2J_8(y)-2\pi|y|,
\]
\[
J_A(y)=\int_0^A\log\sqrt{v^2+y^2}\,dv.
\tag{S3}
\]

记

\[
M_0=\max_{y\ge0}Q(y),\quad
M(s)=\max_{y\ge0}\{Q(y)+\log|s-y^2|\},
\]
\[
I(s)=\int_0^1\log(s+t^2)\,dt
=\log(1+s)-2+\sqrt{s}(\pi-2\arctan\sqrt{s}),
\quad \varepsilon(s)=M_0-M(s)+I(s).
\tag{S4}
\]

在 y=√s 按 −∞ 解释。I(s) 是实际 head 值产生的项，不能只降低 M(s) 而忽略它。本文求的是单一根尺度 s 的全局最优；不声称它是任意 q、多根分布或实际复相位的全局最优。

## S2. Q 的唯一峰与两个根侧峰

对 y>0，

\[
Q'(y)=7\arctan(2/y)-2\arctan(8/y)-2\pi
=\pi/2-7\arctan(y/2)+2\arctan(y/8),
\]
\[
Q''(y)=\frac{2(y^2-416)}{(4+y^2)(64+y^2)}.
\tag{S5}
\]

Q'(0+)=π/2；Q' 在 (0,√416) 严减，其后严增至 −2π。已保存区间证明 Q'(1)<0（证书的 Q' 在 0、1 上异号检查），故恰有 y_0∈(0,1) 使 Q'(y_0)=0，Q 在 y_0 处唯一最大。Q(y)=−2πy−2log y+O(1) 保证以下 maxima 确实取得。

左侧 f_s^L(y)=Q(y)+log(s−y²)，0≤y<√s。其导数在 0+ 为 π/2。在 y<min(y_0,√s) 内 Q''<0 且 log 项严格凹；若 y≥y_0，其导数已严格负。因此左侧唯一最大点 a(s) 满足

\[
0<a(s)<\min(y_0,\sqrt{s}),\quad
Q'(a)=\frac{2a}{s-a^2},\quad
s=a^2+\frac{2a}{Q'(a)}.
\tag{S6}
\]

最后右端对 a∈(0,y_0) 的导数为 2a+2/Q'(a)−2aQ''(a)/Q'(a)²>0，范围 (0,∞)。因此 a(s) 严格递增，且左右极限为 0 与 y_0。

右侧 f_s^R(y)=Q(y)+log(y²−s)，y>√s。对所有 y>0，有 Q''(y)<2/y²；对 y²>s，

\[
\frac{2(y^2+s)}{(y^2-s)^2}>\frac2{y^2},
\quad (y^2+s)y^2-(y^2-s)^2=s(3y^2-s)>0.
\]

故 f_s^R''<0，在整个右侧严格凹。其导数在 √s+ 为 +∞，在 ∞ 为 −2π；唯一最大点 b(s) 满足

\[
b(s)>\max(y_0,\sqrt{s}),\quad
Q'(b)+\frac{2b}{b^2-s}=0,\quad
s=b^2+\frac{2b}{Q'(b)}.
\tag{S7}
\]

由 ∂_s f_s^R'=2y/(y²−s)²>0 与 f_s^R''<0，隐函数定理给 b'(s)>0。这里没有用 Q 在全实轴凹的错误前提；Q'' 在很大 y 上确实变号，但右侧 log 曲率足够保证 f_s^R 严凹。

## S3. 单一尺度的唯一全局最优

记 L(s)=f_s^L(a(s))、R(s)=f_s^R(b(s))。它们光滑，envelope 导数为

\[
L'(s)=\frac1{s-a(s)^2}>\frac1s,\qquad
R'(s)=-\frac1{b(s)^2-s}<0,
\quad 0<I'(s)=\int_0^1\frac{dt}{s+t^2}<\frac1s.
\tag{S8}
\]

L−R 严格递增。s→0+ 时 L≤M_0+log s→−∞，而 R≥Q(1)+log(1−s) 对小 s 有下界。s→∞ 时 L≥Q(0)+log s→∞；由 Q(y)≤C−πy 对足够大 y，

\[
R(s)\le\sup_{y>\sqrt{s}}\{C-\pi y+2\log y\}\longrightarrow-\infty.
\]

所以恰有 s_*∈(0,∞) 使 L(s_*)=R(s_*)。M(s)=max(L,R)，故

* s<s_* 时，ε'=I'−R'>0；
* s>s_* 时，ε'=I'−L'<0。

这证明 s_* 是整个 s>0 家族的唯一全局最大点，且其两个峰准确等高。它是一个完全确定的 transcendental scalar problem；不是将有限网格中最大的点冒称全局极值。

已保存 FIRST1 以 Fraction 做 atan alternating remainder、log geometric remainder、Machin π 与 sqrt 二分区间，再作带严格符号检查的 nested bisection。outer bisections 完成 18 步，保存结果为

\[
0.560665893554\le s_*\le0.560666656495,
\]
\[
0.219991954803\le a(s_*)\le0.219992117751,
\quad1.328867966712\le b(s_*)\le1.328868225789,
\]
\[
0.620411691946\le\varepsilon(s_*)\le0.620412917931.
\tag{S9}
\]

所有写出小数均是以 denominator10¹² 保存的有理端点。S6–S8 的单调性说明这些有限区间确实括住唯一全局解。特别地，源码的 M_* lower=max(L(s_lo)_lower,R(s_hi)_lower)、upper=min(L(s_hi)_upper,R(s_lo)_upper) 来自 L 增、R 减；b 的端点拼接来自 b 增。纸面唯一性证明与有限实数证书的职责明确分开。

## S4. 无需求最优根：s=4/7 的全轴保守证明

固定 s=4/7，设 f(y)=Q(y)+log|s−y²|。在左侧 y∈[0,√s)，由 y<1 得 Q''≤−51/20，且

\[
\frac{2(s+y^2)}{(s-y^2)^2}\ge\frac2s=\frac72.
\]

因此 f''≤−c_L，c_L=121/20。取 y_L=1/4，

\[
f(y_L)=Q(1/4)+\log(57/112),\quad
d_L=f'(y_L)=Q'(1/4)-56/57,
\]
\[
L(s)\le U_L:=f(y_L)+d_L^2/(2c_L).
\tag{S10}
\]

这来自全左区间的强凹性切线二次式，最大值取遍全部实数得到的上界，故不需要预先数值定位左峰。

在右侧 √s<y≤2，Q'''=28y/(4+y²)²−32y/(64+y²)²>0，故 Q''≤Q''(2)=−103/68。函数 2(t+s)/(t−s)² 对 t>s 严减，因而在 t=y²≤4 上 ≥7/9。于是

\[
f''\le-c_R,\quad c_R=103/68+7/9=1403/612.
\]

取 y_R=4/3，

\[
f(y_R)=Q(4/3)+\log(76/63),\quad
d_R=f'(y_R)=Q'(4/3)+42/19,
\]
\[
\sup_{\sqrt{s}<y\le2}f(y)\le U_R:=f(y_R)+d_R^2/(2c_R).
\tag{S11}
\]

证书严格给 d_R<0，而 S2 已证明右侧导数严格递减。因此 y≥4/3 的 f 已严格递减，特别是 y>2 的尾部不会增加 supremum。S11 覆盖整个右侧；Q 偶性覆盖负轴。

已保存有理区间为

| quantity | lower | upper |
|---|---:|---:|
| Q(1/2) | −9.841198709822 | −9.841198709821 |
| U_L | −10.604814987801 | −10.604814987800 |
| U_R | −10.635521815580 | −10.635521815579 |
| I(4/7) | −0.151796758678 | −0.151796758677 |
| Q(1/2)−U_L+I | 0.611819519300 | 0.611819519301 |
| Q(1/2)−U_R+I | 0.642526347079 | 0.642526347080 |
| d_L | −0.219665108523 | −0.219665108522 |
| d_R | −0.004398227420 | −0.004398227419 |

由于 M_0≥Q(1/2)、M(4/7)≤max(U_L,U_R)，整个实轴的纸面不等式与上述严格区间共同给

\[
\boxed{\varepsilon(4/7)>3/5.}
\tag{S12}
\]

I(4/7) 本身负：收益来自 numerator 的更大下降超过了实际 head 项的损失。不能把 I 的符号或两个 head 镜像值凭空替换。

## S5. 将 ε(s) 支付到同一个 all-n determinant

令 θ_n=2N/n∈[0,1]，沿竖线 |q(c_n+iny)|²=n^(4N)|s−y²|^(2N)。逐点 convex combination 给

\[
\sup_y\{Q(y)+\theta_n\log|s-y^2|\}
\le(1-\theta_n)M_0+\theta_n M(s).
\tag{S13}
\]

从 S3 的 uniform envelope，固定 s 的全轴 tail 有 Q+θlog|s−y²|≤−π|y|+C_s，uniformly θ∈[0,1]。compact 上 polynomial prefactor 有界，tail 的指数吸收它。因此

\[
\log A_n(q)\le(4n+4N+C)\log n
+n[(1-\theta_n)M_0+\theta_n M(s)]+O_s(1).
\tag{S14}
\]

对每个 mirror choice，δ_left=2n+1/2−m、δ_right=m−1/2；实际 δ_choice≥m−1/2。故

\[
\sum_m\log q(a_m)\ge2Nn\log n
+N\sum_{m=1}^n\log\left(s+\left(\frac{m-1/2}{n}\right)^2\right).
\tag{S15}
\]

固定 s>0 下 log(s+t²) 在 [0,1] 光滑且 Lipschitz，midpoint sum=nI(s)+O_s(1)。因此 S2 中所有 mirror summands 的 q 费用被同一个 n^(−2Nn)exp(−NnI(s)+O_s(N)) 支配。两 mirror q 值一般不同；S15 逐个对实际值计费，没有假设镜像相等。

由 S14–S15，整个 common low factor 的 logarithm ≤

\[
4n^2\log n+n^2M_0-2Nn\varepsilon(s)+O_s(n\log n).
\tag{S16}
\]

even n 时 2Nn=n²，odd n 时 n²−n；差为 O_s(n)。n=1 取 q=1 后增大常数即可。原 high Gram、factorial、mirror Hardy sum、原 Γ_n 全部仍支付且只支付一次。接此前已证 rate 可先准确写为

\[
\log|D_{A,n}(\xi)|\le
-(\beta_{\rm mirror}+\varepsilon(s))n^2
-2\log\Gamma_n+O_s(n\log n).
\tag{S17}
\]

这里 β_mirror>9.09188285412558，liminf logΓ_n/n²≥γ≥1.455845。没有把 gcd 余项未经证明改成 O(nlog n)。用 S12 得同一原格的严格保守结论

\[
\boxed{\limsup_{n\to\infty}
\frac{\log|D_{A,n}(\xi)|}{n^2}<-12.60357285412558.}
\tag{S18}
\]

log0=−∞。S9 的最优根还给 ε(s_*)≥0.620411691946，故可获得相应更强的单家族 paper rate；实际有理实现可直接用 s=4/7，或由 ε 连续性选择邻近有理尺度。本文的简洁明确保守界采用 S18。

同一原格 safe signed rational normalization scale 为约 40.314517426059346，仍未形成足够大的同对象 strict margin。这个 safe upper scale 不是实际最小整化费用的下界。因此 S18 没有证明该方法绝对不能成功；它也没有证明 D_A(ξ) 无限次非零、固定有理 source 无限成功、辅助 Smith/unit 全尺度结论或新的数值无理性定理。

## S6. 证据、数学范围和一手文献

完整只读检查的三个 NEW 文件：

* [source](cdt_odd_paired_scaled_root_optimum_20261007_certify.py)，SHA256 `95e7ff89a97a6633de4441288a32c787d6ef59aa16efc93d7d50dec5f744e242`。
* [result](cdt_odd_paired_scaled_root_optimum_20261007_certify.json)，SHA256 `321d0da51964c27e6fa710d844b2d251071e2736cf6bc5b6047b8d0b1b1855ff`，state `PASS_FIRST1`，7 explicit assertions，18 outer bisections。
* [guard](cdt_odd_paired_scaled_root_optimum_20261007_certify_guard.json)，SHA256 `e1e97654436d92dada737c0a9dee938008df3b976e85d67cc51a422647364189`，state `STARTED_FIRST1`、exclusive-create。guard 的开始标签不被擅改为完成标签；成功状态从 result 取得。

该程序只处理 elementary real intervals，未执行 prime、rank、determinant experiment，没有 Lean。S6–S8 的 all-s theorem、S10–S11 的全轴曲率、S13–S17 的 all-n 费用支付是本文纸面证明，不能把 7 个有限断言解释为它们的自动验证。三个成功文件永久保持，不 rerun。

本轮已下载的一手原件为 Mhaskar–Saff, *Weighted Analogues of Capacity, Transfinite Diameter, and Chebyshev Constant*, Constructive Approximation 8 (1992), 105–124；作者站 [125.pdf](https://www.math.vanderbilt.edu/saffeb/texts/125.pdf)，本地 [PDF](../literature/cdt_paired_scaled_root_sources_20261007/mhaskar_saff1992_weighted_capacity_author_125.pdf)，20页、832318 bytes，SHA256 `66d00d46fb0e2f4da7b4c23e98dcc39b5687587e179a77813b27caa859968aa5`。本文撰稿者实际完整提取阅读 PDF1–5、11–12，共7 distinct页；没有声称整篇读完，也未重新下载。

PDF3 的 weighted Chebyshev 定义 Eq2.7–2.10 明确是 monic normalization；PDF4 的 Definition2.4 列出 admissible weight；PDF5 的 Theorem3.1 给 weighted equilibrium measure 与变分条件；PDF11–12 的 Theorem4.1、Corollary4.2、Theorem4.3 把 weighted polynomial norm 的有效支集与 Chebyshev 常数连接起来。这些是一手的研究方向依据。本项目目标 ε(s) 还含依 root 变化的 head integral I(s)，不是固定 weight 下简单 monic norm 最小化；因此没有直接引用该书面 theorem 宣告本项目 root distribution 最优或 determinant 非零。S1–S18 的结论均由当前实际模型直接证明。

本轮推进点是：单根尺度家族的唯一全局最优、显式有理尺度 4/7 的 ε>3/5、同原格全 n 的可支付 rate 改善。下一问题是多根分布、真实复相位和算术残余配对；单家族解不封闭这些方向。独立复核与最终一向收据另行保存，本文不提前声明已经完成。
