# 混合 ζ 双极点 Hankel 族：全部有限素数的整化、minor 与零阶修复

日期：2026-10-06。作者任务：conifold_arithmetic_hypothesis。

本稿为 NEW 纸面推导。冻结 H9、Lai PDF、旧与同行 MD/PY/JSON/receipt 仅读取；数学 producer 执行、import、重跑次数均为 0。本文没有证明新的 ζ 数值无理性或线性无关性，也没有把 Lai 权重四的 30.83 或 31.614437 当成高权重结论。

## A1. 输入、变量与结论范围

冻结输入 research/cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md 全文，SHA256：

e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463。

实际全文读 Lai, *The linear independence of 1, ζ(3), and ζ(4)*，arXiv:2610.06838v1，PDF 1–25：

literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf，
SHA256 838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58。

Lai PDF 7–11 是经典与 residue minor 估计，12–17 是素数求和，17–22 是右轮廓与实数估计。本文独立证明这些算术步骤的全固定权重版本，另加入真正的整数多项式 common content 与零阶修复；不宣称其权重四全论文已由本任务独立验证。

设 s≥4、κ≥3、B>κ 为固定整数，n≥1。设 a,b∈Z，b≠0；X 是形式变量。记

\[
N=Bn,\qquad M=(B+2)n,\qquad h=(B-\kappa)n,
\]
\[
R_{n;B,\kappa}(t)=
\frac{N!^2}{(2n)!^\kappa}\,
\frac{(t-2n)_{2n}^{\kappa}}{(t)_{N+1}^{2}}.
\tag{A1}
\]

原 H9 恰为 (B,κ,h/n)=(6,3,3)。权重 s 可以增加而不修改原有 R；这给算术与非零定理，但不能自动保留其解析估计。

本文严格给出：

1. 所有 p、所有 n、整个 J(X)∈Q[X] 的 Gauss valuation 下界及有限整化模型；
2. p>√M 的完整 residue minor 整数优化，原 H9 的权重变化只惩罚非首节点；
3. U₀=0 的额外 rank/content 改进及满 rank residue 的准确 confluent Vandermonde 因式分解；
4. κ≥s−1 的修复布局，含无限辅助素数子列上的真正非零证明；s=5 可取 κ=4,B=6，而非必须增加 pole 长度到 B=8；
5. 原 κ=3 布局从 s=5 起的精确轮廓缺项。

未知项仍是匹配该实际布局的实数能量与充分的算术/解析净余量。下述 valuation 下界是可证明的 common content；不是实际 primitive content 的精确等式。

## A2. 部分分式与目标多项式

设 deg P<2h。于是 deg(RP)≤−3。直接在 t=−j 的 double pole 展开得

\[
A_{2,j}=W_jP(-j),\quad
A_{1,j}=W_j(P'(-j)+C_jP(-j)),
\]
\[
W_j=\binom Nj^2\binom{2n+j}{j}^{\kappa}\in Z,
\quad
C_j=(\kappa+2)H_j-\kappa H_{2n+j}-2H_{N-j}.
\tag{A2}
\]

Σ A₁,j=0，因为 RP 在无穷远没有 t⁻¹ 项。逐项求导及求和，代入假设 aζ(s−1)+bζ(s)=X，得到有理系数泛函

\[
\Lambda_X(P)=\sum_{j=0}^{N}W_j\{U_jP'(-j)+V_j(X)P(-j)\},
\tag{A3}
\]
\[
U_j=-(s-1)a(s-3)!H_j^{(s-2)}
      -b(s-2)!H_j^{(s-1)},
\]
\[
V_j(X)=C_jU_j+(s-1)!\{X-aH_j^{(s-1)}-bH_j^{(s)}\}.
\tag{A4}
\]

式 (A3) 本身不需要数值假设：它定义 Λ_X:Q[t]_<2h→Q[X]。只有把它识别为实际 ζ 导数和，才需 aζ(s−1)+bζ(s)=X。

令

\[
J_{n,s;B,\kappa}(X)=
\frac{\det[\Lambda_X(t^{i+j})]_{0\le i,j<h}}
{\prod_{i=0}^{h-1}i!^2}\in Q[X].
\tag{A5}
\]

其次数至多 h。用 f_i(t)=binom(t,i)，三角基变换的对角为 1/i!，所以

\[
J(X)=\det[\Lambda_X(f_i f_j)]_{0\le i,j<h}.
\tag{A6}
\]

这一步保留了 factorial 基变换费用，没有把它当成免费整数基。

以下 v_p 在 Q[X] 上指 Gauss valuation：非零多项式所有系数的最小 p-adic valuation；v_p(0)=+∞。它满足乘法与非 Archimedean 加法估计。因此一切矩阵/minor 论证都同时控制全部 X 系数，不只是一个指定整数 X。

## A3. 整数值基的导数与所有小素数

定义 L_p(T)=floor(log_p T)，T≥1；L_p(0)=0。令 D_i=lcm(1,…,i)，D₀=1。

Vandermonde 恒等式在参数 u=0 求导给出

\[
f_i'(t)=\sum_{r=1}^{i}\frac{(-1)^{r-1}}r f_{i-r}(t).
\tag{A7}
\]

对任何整数 t，f_i(t)∈Z，故 D_i f_i'(t)∈Z。乘积求导说明 D_{h-1}(f_i f_j)'(t)∈Z。

有限 harmonic 和满足 v_p(H_j^(r))≥−r L_p(N)，j≤N。以下常数没有依赖 a,b 的 p-unit 假设：

\[
u_p=\min\{v_p((s-1)(s-3)!)-(s-2)L_p(N),
             v_p((s-2)!)-(s-1)L_p(N)\},
\]
\[
\chi_p=\min\{v_p(\kappa+2)-L_p(N),
                v_p(\kappa)-L_p(M),
                v_p(2)-L_p(N)\},
\]
\[
\eta_p=\min\{u_p-L_p(h-1),\ u_p+\chi_p,\
                    v_p((s-1)!)-sL_p(N)\}.
\tag{A8}
\]

由 (A2)–(A4)、W_j∈Z 与 (A7)，每个 (A6) 矩阵元的 Gauss valuation≥η_p，故

\[
v_p(J(X))\ge h\eta_p\ge-hsL_p(M).
\tag{A9}
\]

这适用于包括 p≤s 的全部有限素数。固定 factorial 的额外可整性已在 η_p 中明确保留。需要 a,b 的额外费用改善时，可在 u_p 两项分别加 v_p(a),v_p(b)，但第三项必须保留 X 系数本身的 valuation，不能免费加 v_p(X)。

例如原 H9 的 s=5、κ=3，对 p=2 有

\[
v_2(J)\ge
-h\max\{4L_2(N)+L_2(M)-1,\ 5L_2(N)-3\},
\tag{A10}
\]

对 p=3 有 v₃(J)≥−h(4L₃(N)+L₃(M)−1)，对 p≥5 有 v_p(J)≥−h(4L_p(N)+L_p(M))。这些是有限 n 的保证；小素数改善只影响 o(n²) 费用，不能代替主率比较。

## A4. 所有 p>N 的真正整数性

若 p>N，则 f_i(-j) 与导数都是 p-integral，H_j^(r)、H_{N-j} 均 p-integral，因为 j,h−1≤N。

唯一可能的分母来自 H_{2n+j}，其下标≤M；因 B≥4，M<2N<2p，所以最多出现一个 p，valuation≥−1。若 2n+j≥p，Legendre 公式给

\[
v_p\binom{2n+j}{j}=1
\]

（2n,j<p，且 2n+j<2p）。于是 v_p(W_j)≥κ≥3，足以清除该 harmonic 的 p 分母。若 2n+j<p，根本没有该分母。因此

\[
v_p(J(X))\ge0\qquad(p>N).
\tag{A11}
\]

此证明也覆盖 N<p≤M，不能仅以“R 的 pole 小于 p”跳过 C_j 的较长 harmonic。

## A5. 大素数的 residue 分解

以下 p>√M，p≤N。对 0≤ρ<p，定义

\[
q_\rho=\left\lfloor\frac{N-\rho}{p}\right\rfloor,\qquad
w_\rho=2\left\lfloor\frac Np\right\rfloor-2q_\rho
 +\kappa\left\lfloor\frac{2n+\rho}{p}\right\rfloor
 -\kappa\left\lfloor\frac{2n}{p}\right\rfloor.
\tag{A12}
\]

因为 p²>M，全部 factorial 的 Legendre 公式只有第一层。对 j=ρ+ℓp，0≤ℓ≤qρ，

\[
v_p(W_j)=w_\rho\in\{0,2,\kappa,\kappa+2\}.
\tag{A13}
\]

将 (A3) 限制到 j≡ρ mod p，得双线性矩阵 Bρ。整数 unitriangular 平移 t^i↔(t+ρ)^i 不改变任意阶 minor 的共同 valuation 下界。用该平移基，写 Bρ=A₀+A_tail：

* ℓ=0 只有 (0,0)、(0,1)、(1,0) 三个可能非零位置，rank A₀≤2；
* 每个 ℓ≥1 节点的泛函是 evaluation/first derivative 的二阶双线性形式，故 rank A_tail≤2qρ。

首节点因 ρ<p，Uρ p-integral，Vρ≥−1。tail 因 harmonic 下标≤M<p²，U≥−(s−1)，V≥−s。于是

\[
v_p((A_{\rm tail})_{ij})\ge i+j+w_\rho-s,\qquad
v_p((A_0)_{ij})\ge i+j+w_\rho-1.
\tag{A14}
\]

tail 导数除以 −ℓp 产生一层 p 分母，这与 U 的 −(s−1) 正好相加为 −s；不能漏算该导数费用。

## A6. 全权重 minor 定理及准确权重惩罚

定义

\[
\delta_\rho={\bf1}_{p>\max(N-\rho,2n+\rho)},
\]
\[
F_{s,\rho}(m)=
m^2+(w_\rho-s-1)m
 +(s-1)\max(0,m-2q_\rho)
 +\delta_\rho{\bf1}_{m=1}.
\tag{A15}
\]

任意 m×m minor 的 Gauss valuation≥F_s,ρ(m)，且 m>2qρ+2 时该 minor 为 0。

证明：按列展开 A₀+A_tail。非零项至多取 2qρ 个 tail 列。因此至少 max(0,m−2qρ) 个 head 列获得 (s−1) 的改善。行/列指标总和各≥m(m−1)/2，给二次项 m²−m。唯一额外 singleton 情形是 qρ=0 且 2n+ρ<p，此时 Cρ 也 p-integral，增加 δρ。随后在整数平移矩阵两侧用 Cauchy–Binet，得到原 t^i 基的同一 minor 下界。证明对 Gauss valuation 逐系数成立。

对原 H9 的 κ=3,B=6，Lai 的 F₄ 被严格恢复。并且

\[
F_{s,\rho}(m)-F_{4,\rho}(m)
=-(s-4)\min(m,2q_\rho).
\tag{A16}
\]

权重增加只惩罚 tail 的实际占用数。用 −(s−4)m 替代右侧虽给安全弱界，却丢掉了 qρ=0 以及已用满 tail 的真实改善。

## A7. U₀=0 的有限 rank/content 补强

对 ρ=0，U₀=0，V₀(X)=(s−1)!X，W₀=1。此处 head 是 integral rank 1，而不是一般 rank 2、valuation −1 的 head。因此可把容量改为

\[
c_0=2q_0+1
\]

并采用较强 minor 下界

\[
F^\star_{s,0}(m)=m^2-(s+1)m
 +s\max(0,m-2q_0),\qquad0\le m\le c_0.
\tag{A17}
\]

对 ρ>0 仍令 cρ=2qρ+2，F*ρ=Fρ。证明同 A6，唯一 head 列比 tail 改善 s，而非 s−1；m>2q₀+1 时 rank 强迫 minor 为 0。

如果专门取 X=0，则首节点完全消失，容量可进一步降至 2q₀。这不是全 X 多项式的性质，不能用于一个未知有理目标值。

该 rank 1 修正在每个 p 只涉及一个 residue，不能未经估计把它包装成 n² 主费用下降。

## A8. 有限 n 的完整整数优化与全系数模型

设

\[
E_p=2\sum_{i=0}^{h-1}\left\lfloor\frac ip\right\rfloor
=v_p\prod_{i=0}^{h-1}i!^2,\quad(p>\sqrt M),
\]
\[
\mathcal L_p=-E_p+
\min_{\substack{0\le m_\rho\le c_\rho,\ m_\rho\in Z\\
                  \sum_{\rho=0}^{p-1}m_\rho=h}}
\sum_{\rho=0}^{p-1}F^\star_{s,\rho}(m_\rho).
\tag{A18}
\]

矩阵 ΣρBρ 的行/列 Laplace 展开是各 residue 的相同阶 minor 的乘积之和。因此

\[
v_p(J(X))\ge\mathcal L_p.
\tag{A19}
\]

容量总和为 2(N+1)−1=2N+1>h，故优化集合非空。式 (A18) 的 factorial 费用 E_p 必须扣除；不能把 monomial determinant 的 valuation 当成 J 的 valuation。

该有限优化完全离散、精确且无需求解程序。每个 F* 在其有限整数区间上离散凸：相邻 marginal 增量递增；δ singleton 只把相邻差从 2 改为 0，仍不破坏凸性。取全部 residue marginal 增量中的 h 个最小值，可在平局时按前缀选取，恰好实现此最小值。这提供可审阅的有限模型计算规则。

定义全部素数的整数下界

\[
\ell_p=
\begin{cases}
\max(h\eta_p,\mathcal L_p),&\sqrt M<p\le N,\\
h\eta_p,&p\le\sqrt M,\\
0,&p>N.
\end{cases}
\tag{A20}
\]

令 Q_n=∏_{p≤N}p^ell_p∈Q_{>0}。则

\[
\boxed{J_{n,s;B,\kappa}(X)/Q_n\in Z[X].}
\tag{A21}
\]

若只要一个整数清分母，D_n=∏p p^max(0,−ell_p) 足够。若保留正 valuation，则 D_nJ 的全部系数还共同被 A_n=∏p p^max(0,ell_p) 整除。Q_n=A_n/D_n 才是本方法实际提供的 common-content 比率。

没有理由把 D_nJ 直接称 primitive polynomial；(A21) 是 common content 下界，而非所有系数 gcd 已准确确定。

若给定 X=c∈Z 且 J(c)≠0，则 (A21) 给出 |J(c)|≥Q_n。若 X=u/v 为既约有理数，则 v^hJ(u/v)/Q_n∈Z，需付 h log v。固定 v 对 n² 主率为 o(n²)，但有限整化中必须保留。对 a,b∈Q 同样先付固定公共分母的 h 次幂，不能声明免费。

## A9. 不用大素数优化也成立的显式主率

令

\[
D_{n,s}^{\rm coarse}=
\prod_{p\le N}p^{hsL_p(M)}.
\tag{A22}
\]

由 A3/A4，D_coarse·J(X)∈Z[X]，全部 n 都成立。小素数 p≤√M 的对数费用为 O_{B,κ,s}(n^(3/2) log n)；大素数的 L_p(M)=1。由素数定理，

\[
\log D_{n,s}^{\rm coarse}
\le \{sB(B-\kappa)+o(1)\}n^2.
\tag{A23}
\]

此为严格 upper bound，不是 actual denominator 的 lower bound。A8 的 signed content 和 residue 优化通常更好，须独立求和才能报新常数。

| 布局 | h/n | s=5 的粗主率 upper bound | 右轮廓是否无 crossing |
|---|---:|---:|---|
| 原 H9：B=6,κ=3 | 3 | 90 | 否 |
| 修复：B=6,κ=4 | 2 | 60 | 是 |
| 修复：B=8,κ=4 | 4 | 160 | 是 |
| 最小 pole 布局：B=5,κ=4 | 1 | 25 | 是 |

最后一行的粗算术费用较小，并不表示净余量较好：determinant 大小、R 的能量、pole 长度全部改变，必须重新比较。原 H9 的 s=7 粗主率为 126。

## A10. residue 满 rank determinant 的精确因式分解

固定 residue ρ，令 r=qρ+1，节点 zℓ=−ρ−ℓp。若取前 2r 个 monomial 基，完整节点双线性矩阵有分解 YDYᵀ，其中 Y 的两列分别为 evaluation 与 first derivative，

\[
D_\ell=\begin{pmatrix}W_{j_\ell}V_{j_\ell}&W_{j_\ell}U_{j_\ell}\\
W_{j_\ell}U_{j_\ell}&0\end{pmatrix}.
\]

confluent Vandermonde 给 det Y=±∏_{u<v}(z_v−z_u)^4，故

\[
\det B_\rho=
(-1)^r
\left(\prod_{\ell=0}^{q_\rho}W_{j_\ell}^2U_{j_\ell}^2\right)
\prod_{0\le u<v\le q_\rho}(z_v-z_u)^8.
\tag{A24}
\]

这是每个 residue 的满 rank determinant 恒等式，不是全矩阵 determinant 的单项等式。p²>M 保证 qρ<p，所有 1≤v−u≤qρ 是 p-unit。若 Uρ 是 p-unit、各 tail U 的 valuation 都等于 −(s−1)，则

\[
v_p(\det B_\rho)=
2(q_\rho+1)w_\rho+4q_\rho(q_\rho+1)-2q_\rho(s-1)
=F_{s,\rho}(2q_\rho+2).
\tag{A25}
\]

因此 double-pole 的 det Dℓ=−W²U² 消去了 V，却没有消掉导数/Vandermonde 的实际费用；本 minor 下界在这些 unit 条件下恰好饱和。不能仅凭“2×2 determinant 不含 V”声称额外统一主率节省。

ρ=0 的 U₀=0 恰使 (A24) 为零，与 A7 的 rank 下降一致。对于实际 a,b，有些其他 Uρ 或 tail harmonic 也可能有额外 p-divisibility；本文不假设其在全部 p、n 上成立。

## A11. 一般布局的无限辅助素数非零证明

设 n=2m，p=(B+κ)m+1 是素数，且 p>max(s,|b|)。令 d=(B−κ)m，则 h=2d、N=2Bm。κ>2 给

\[
d<p,\quad N<2p,\quad 4m+d< p.
\tag{A26}
\]

恰有 d 个 j≥p：j=p+ℓ，0≤ℓ<d。它们的 W_j 是 p-unit：两个 binomial 均无 p-adic carry。并且

\[
H_j^{(v)}=p^{-v}+O(Z_p),\quad
C_j=2p^{-1}+O(Z_p).
\]

令 u=(s−2)!b，为 p-unit。则

\[
U_j=-u p^{-(s-1)}+O(p^{-(s-2)}Z_p),\quad
V_j(X)=-(s+1)u p^{-s}+O(p^{-(s-1)}Z_p[X]).
\tag{A27}
\]

X∈Z_p 的系数项是 integral，故不影响该 leading block。

在节点 −k，0≤k<d，取 Lagrange F_k，满足 F_k(−ℓ)=δ_kℓ，系数属于 Z_p；令 c_k=F_k'(−k)，

\[
P_k=p^2(1-2c_k(t+k))F_k(t)^2,\qquad
Q_k=p(t+k)F_k(t)^2.
\tag{A28}
\]

它们的次数都≤2d−1；在 −ℓ 处分别有 evaluation/derivative 值 (p²δ,0) 与 (0,pδ)，故构成 degree<h 的 Q 基。在 j=p+ℓ 的 Taylor 展开为

\[
P_k(-j)=p^2\delta_{k\ell}+O(p^4),\quad P_k'(-j)=O(p^3),
\]
\[
Q_k(-j)=-p^2\delta_{k\ell}+O(p^3),\quad
Q_k'(-j)=p\delta_{k\ell}+O(p^2).
\tag{A29}
\]

在 j<p，U_j integral，V_j≥−1，(A28) 的 p²/p 因子使 p^(s−4)B(P,Q) 的贡献模 p 全部为零。结合 (A27)–(A29)，p^(s−4)B 在该 2d 维基中的 reduction 是 d 个不相混的 blocks

\[
uW_{p+\ell}
\begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix},
\qquad\det= -u^2W_{p+\ell}^2\ne0.
\tag{A30}
\]

所以 J(X) 的相应 scaled determinant reduction 是非零常数，特别每个 X∈Z_p 的实际 J(X)≠0。该结论也适用于固定有理 X，只需 p 不整除其分母。这里并没有免除 (A28) 的真实 p-adic 基变换指数。

准确指数亦可从该证明读取：未缩放的 Hermite cardinal 基之 determinant 是 p-unit，因为 d<p，节点差的 confluent Vandermonde 是 p-unit。乘 P_k 的 p² 与 Q_k 的 p 后，基变换 T 的 v_p(det T)=3d。故 (A30) 给 v_p(det B_monomial)=−h(s−4)−6d=−h(s−1)。由于 h<2p，factorial normalization 的 valuation 为 2(h−p)_+，从而

\[
v_p(J(X))=-h(s-1)-2(h-p)_+,\qquad
p^{h(s-1)+2(h-p)_+}J(X)\bmod p
\text{ 是非零常数}.
\tag{A30a}
\]

这里第一式是整个多项式的 Gauss valuation，也对每个 X∈Z_p 的 specialization 成立。B>3κ 时 h 可能大于 p，不能把 2(h−p)_+ 免费删掉；原 H9 与本稿 s=5 的 B=5、6、8 均有 h<p，因此该附加费用为零。辅助素数单 p 的指数贡献是 O(n log n)，不是全素数 n² 主率的证明。

Dirichlet 定理给无限多个 p≡1 mod(B+κ)，故无限多个 m。原 H9 是 p=9m+1；κ=4,B=6 的 s=5 修复为 p=10m+1；κ=4,B=8 为 p=12m+1；κ=4,B=5 为 p=9m+1。

## A12. 三重零的解析 crossing 缺项

设 f=RP。对 d≥1，(πcotπz)^(d) 的 principal part 为 (−1)^d d!/(z−m)^(d+1)。因此实际导数和的右侧轮廓 kernel 可以取

\[
K_{s,a,b}(z)=
-(s-1)a(\pi\cot\pi z)^{(s-3)}
-b(\pi\cot\pi z)^{(s-2)}.
\tag{A31}
\]

与 Lai 相同的 clockwise residue 方向给

\[
\frac1{2\pi i}\int_{2n+1/2-i\infty}^{2n+1/2+i\infty}
 f(z)K_{s,a,b}(z)\,dz
=(-1)^{s-3}(s-1)a\sum_{m\ge2n+1} f^{(s-3)}(m)
 +(-1)^{s-2}b\sum_{m\ge2n+1}f^{(s-2)}(m).
\tag{A32}
\]

kernel 在竖线上指数衰减；RP 在无穷远次数≤−3，因此矩形水平与右侧边界极限合法。但 (A32) 只包含 tail。完整泛函还必须加 m=1,…,2n 的有限导数和。

当 κ=3,s=5，f''(m)=0，f'''(m)=R'''(m)P(m)，故准确补项为

\[
\Lambda_{\rm actual}(P)=
\frac1{2\pi i}\int fK_{5,a,b}
-b\sum_{m=1}^{2n}R'''(m)P(m).
\tag{A33}
\]

在双线性形式上补项为 −bΣR'''(m)P(m)Q(m)，rank≤2n。它不是小的固定常数项；其 rank 随 n 增长，因此不能删除后沿用纯 contour Gram 的 n² 能量。

一般 κ=3,s≥5，补项涉及 (PQ) 的最高 s−5 阶导数，每个节点 jet 维数≤s−4，总 rank≤2n(s−4)，再与 h 取较小者。这也不提供纯 Gram 估计。

## A13. 零阶修复与真正尚未跨过的 gate

若 κ≥s−1，则 derivative 阶数 s−3,s−2 都小于 κ，所有前 2n 节点导数为零，(A32) 恰是完整实际泛函。A2–A11 的部分分式、全有限整化与无限非零子列同时成立。由此得到一个实际可用于新解析研究的布局族，不依赖未证的 crossing 消失。

然而需要重新计算 G_{B,κ}、h 的 log-gas 能量和全素数 signed content 的 n² 费用；不能在 κ 或 B 变化后继承 Lai 的 30.83、31 或31.614437。Lai PDF22 的 Proposition6.6 写的是保守有效界31，其证明给明确常数31.614437…；二者都只针对其 s=4 的实际泛函。

本文没有使用任何 n-dependent basis 将费用藏到未计的 index 中。修复布局的辅助素数非零是已证结论，完整算术模型是已证结论，匹配解析 margin 及新的数值结论尚未证明。

## A14. 本轮可交付的严格进展

原 H9 全固定 s 的缺口现在被分解为两个独立项：

* 算术方面，A8 是全 finite places、全 X 系数的精确有限模型，A6 明确实际权重惩罚，A7/A10 保留真实 rank/content 机制。
* 解析方面，A12 证明 s≥5 的原布局确有 crossing；A13 给出无 crossing 的新实际布局，且 A11 完整证明其无限非零子列。

下一步应比较 κ=s−1、可调 B>s−1 的真实 signed-content 与能量，优先 s=5 的 B=5、6、8。若两项不匹配，应修改布局或建立真正的新全素数 content；不能把 safe bound 当实际分母下界，也不能以高阶 kernel 的固定常数替换原 contour 移动所需的零阶。
