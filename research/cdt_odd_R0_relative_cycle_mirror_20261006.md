# R0−M0 的真实整相对链、Leray tube 与四二次曲面 mirror 的有限商

日期：2026-10-06。本稿是新的数学推导；上一轮 Markdown、Python、JSON、manifest 均只读，未执行、导入或修改任何冻结 producer。已先实际阅读主报告 §§49–54 与当前 delivery 的审计状态。本文不宣称新无理性或线性无关性定理，也不以任意 inhomogeneous PF source 代替 algebraic cycle。

## 1. 输入、目标与本轮增量

沿用已冻结并双独审的记号

\[
 \theta=x\partial_x,\quad P_4=\theta^4-x(\theta+\tfrac12)^4,
 \quad y_0={}_4F_3(\tfrac12^4;1^3;x),
\]
\[
 B(x)={}_5F_4(1^5;\tfrac32^4;x)
 =\int_{[0,1]^4}\frac{du_0\,du_1\,du_2\,du_3}
 {1-x\prod_j(1-u_j^2)},\qquad W=\sqrt{x}B.
\]

冻结输入包括

\[
 P_4W=\frac{\sqrt{x}}{16},\qquad
 B(1)=\frac{\pi^2R_0}{16},\qquad
 M_0=\pi^2y_0(1)=16L(f_8,2).
\]

上一稿 §6.1 已严格证明 \(W-\pi^4y_0/16\) 在 canonical conifold branch 上全纯；这不仅是消掉首项，而是消掉 rank-one logarithmic branch 的全部系数。见冻结文件 [R0 Kummer period interface](cdt_odd_R0_kummer_period_interface_20261006.md)。本轮不重跑其验证，也不重证之前的 M1–3。

本轮的新主结论是：对 \(0<x<1\)，可直接给出真实闭三环面 \(\Gamma_x\subset V_x\) 与正向 Leray tube \(T\Gamma_x\subset U_x\)，满足

\[
 \boxed{\sqrt{x}\int_{T\Gamma_x}\Omega_x=8\pi^4y_0(x).}
 \tag{C1}
\]

因此真实整相对链

\[
 \boxed{\mathcal C_x=8[-1,1]^4-T\Gamma_x}
 \tag{C2}
\]

的周期是

\[
 \sqrt{x}\int_{\mathcal C_x}\Omega_x
 =128\bigl(W-\pi^4y_0/16\bigr),\qquad
 \lim_{x\to1^-}\sqrt{x}\int_{\mathcal C_x}\Omega_x
 =\boxed{8\pi^2(R_0-M_0)}.
 \tag{C3}
\]

这给出此前缺失的真实 Betti marking。\(\pi^4\) 在这里来自三次 contour period 加一次 tube residue，不能当作免费有理 Taylor gauge。另有精确 degree-64 quotient、留数尺度、toric symbol 的 codimension-one 消失，以及明确的 higher-Chow completion 缺口。

## 2. 固定边界的真正相对 pair

设

\[
 A(u)=\prod_{j=0}^3(1-u_j^2),\quad
 F_x(u)=1-xA(u),\quad V_x=\{F_x=0\},\quad
 U_x=\mathbb A^4\setminus V_x,
\]
\[
 D=\bigcup_{j=0}^3\{u_j=1\}\cup\{u_j=-1\},\qquad
 \Omega_x=\frac{du_0\wedge du_1\wedge du_2\wedge du_3}{F_x}.
\]

这里只用真正的八个 affine coordinate faces。由于 \(A|_D=0\)，对所有参数 \(D\cap V_x=\varnothing\)。对 \(0<x<1\)，正向全立方体 \(C=[-1,1]^4\) 给出

\[
 [C]\in H_4(U_x,D;\mathbb Z),\qquad \int_C\Omega_x=16B(x).
 \tag{2.1}
\]

与只取 \([0,1]^4\) 相比，\(u_j=0\) 的内部 faces 已被消掉。更精确地，令 \(G=(\mathbb Z/2)^4\) 按符号作用，\(\chi(g)=\prod_j\epsilon_j\)。按 pushforward 的链方向取

\[
 C=\sum_{g\in G}\chi(g)g_*[0,1]^4.
\]

每个 octant 的 signed pushforward 都恢复 ambient positive orientation，内部 faces 成对相消；这个式子没有把原正立方体误当成闭链。

对 \(x\notin\{0,1\}\)，\(V_x\) 光滑：其上每个 \(1-u_j^2\ne0\)，而 \(dF_x=0\) 强制全部 \(u_j=0\)，继而 \(x=1\)。固定 pair 可在非空 Zariski open base 上作 stratified trivialization，并具有几何 Gauss–Manin 结构；下面的 fibrewise 结论不需要先断言整个 punctured base 上的某个特定 compactification 已满足全部 admissibility 条件。

八个 faces 及其非空交集均为 affine spaces；两个平行 faces 不相交。其 nerve 是四个 \(S^0\) 的 join，故是 \(S^3\)。相应 cohomology 带有

\[
 H^3(D,\mathbb Q)=\mathbb Q(0),\qquad H^4(D,\mathbb Q)=0.
\]

\(G\) 在 \(H^3(D)\) 上的字符就是 \(\chi\)。long exact sequence 与 Gysin 给出

\[
 \boxed{0\longrightarrow\mathbb Q(0)
 \longrightarrow H^4(U_x,D;\mathbb Q)
 \longrightarrow H^3(V_x;\mathbb Q)(-1)
 \longrightarrow0.}
 \tag{2.2}
\]

理由必须保留：\(U_x\) 光滑，\(H^3(U_x)\) 的 weights 至少为 3，而 \(H^3(D)\) 纯 weight 0；MHS strictness 排除了 \(H^3(U_x)\to H^3(D)\)。没有假设 \(H^3(U_x)=0\)，也没有假设 \(H^2(V_x)=0\)。后一个假设对 toric ambient classes 尤其不可靠。另一方面，\(\mathbb A^4\) 的正次 cohomology 为零，故 localization 给出 \(H^4(U_x)\simeq H^3(V_x)(-1)\)。这是实际 pair 的 geometric extension，而不是从 scalar PF 方程事后虚构 extension。

## 3. 闭三环面及符号完整的留数计算

固定 \(0<x<1\)。对 \(j=0,1,2\)，在 \(u_j\)-平面取正向逆时针小椭圆 \(\gamma_j\)，环绕整个线段 \([-1,1]\)。令

\[
 t_j=1-u_j^2,\qquad T=t_0t_1t_2.
\]

小椭圆可取得足够贴近线段，使在其乘积上

\[
 x|T|<1.
 \tag{3.1}
\]

\(t_j\) 在 \(\gamma_j\) 上没有零；该环同时围绕两个简单零点，因而 \(\sqrt{t_j}\) 沿环单值。取其 upper shore 的值为正，在 lower shore 的值为负。取 \(\sqrt{x}>0\)，并取 \(\sqrt{1-xT}\) 为以 1 为中心的主支，由 (3.1) 它在整个三环面上单值。定义

\[
 u_3=\frac{i\sqrt{1-xT}}{\sqrt{x}\sqrt{t_0}\sqrt{t_1}\sqrt{t_2}}.
 \tag{3.2}
\]

则 \(1-u_3^2=1/(xT)\)，故 \(F_x=0\)。这个 graph 是 \(V_x\) 中真正紧的闭三环面 \(\Gamma_x\)，并取 \(\gamma_0\times\gamma_1\times\gamma_2\) 的乘积方向。环面上全部坐标有限，没有以在 infinity 结束的非紧 membrane 代替 cycle。

固定 Poincaré residue convention 为

\[
 \Omega_x=\frac{dF_x}{F_x}\wedge\eta_x,
 \qquad\operatorname{Res}_{V_x}\Omega_x=\eta_x|_{V_x}.
\]

因为 \(d u_3\wedge d u_0\wedge d u_1\wedge d u_2=-d u_0\wedge\cdots\wedge d u_3\)，所以

\[
 \eta_x=-\frac{du_0\wedge du_1\wedge du_2}{2xu_3T}
 =\frac{i}{2\sqrt{x}}
 \frac{du_0\wedge du_1\wedge du_2}
 {\sqrt{t_0}\sqrt{t_1}\sqrt{t_2}\sqrt{1-xT}}.
 \tag{3.3}
\]

现在逐项计算真实 closed contour。upper shore 逆时针方向为从 \(1\) 到 \(-1\)，lower shore 为从 \(-1\) 到 \(1\)。后者 root 变号，故对每个整数 \(n\ge0\)

\[
 I_n:=\oint_{\gamma_j}\frac{t_j^n\,du_j}{\sqrt{t_j}}
 =-2\int_{-1}^{1}(1-u^2)^{n-1/2}\,du
 =-2\pi\frac{(1/2)_n}{n!}.
 \tag{3.4}
\]

端点小圆的 contribution 趋于零；对 \(n=0\) 也是可积 square-root endpoint。由 (3.1)，binomial expansion 一致绝对收敛，可与 contour integration 交换。因此

\[
 \begin{aligned}
 \int_{\Gamma_x}\eta_x
 &=\frac{i}{2\sqrt{x}}
   \sum_{n\ge0}\frac{(1/2)_n}{n!}x^n I_n^3\\
 &=-\frac{4i\pi^3}{\sqrt{x}}
   \sum_{n\ge0}\frac{(1/2)_n^4}{(n!)^4}x^n
 =\boxed{-\frac{4i\pi^3}{\sqrt{x}}y_0(x)}.
 \end{aligned}
 \tag{3.5}
\]

取 normal variable \(F_x\) 的逆时针小圆，并把该 normal-circle 的方向放在 \(\Gamma_x\) 的方向前面。光滑 divisor 的 oriented normal circle bundle 是闭四维整 cycle \(T\Gamma_x\subset U_x\)。Leray residue theorem 按上述符号给出

\[
 \int_{T\Gamma_x}\Omega_x=2\pi i\int_{\Gamma_x}\eta_x.
\]

代入 (3.5) 得到 (C1)。正号 \(8\pi^4\) 来自 \((2\pi i)(-4i\pi^3)=8\pi^4\)；没有省略 residue 的负号，也没有暗中翻转 \(u_3\) 的支。

## 4. 实际整链的 conifold 修正

\(T\Gamma_x\) 是 absolute integral cycle，\(C\) 是 relative integral chain，故 \(\mathcal C_x=8C-T\Gamma_x\) 是整相对 cycle，边界为 \(8\partial C\subset D\)。直接相加周期，不改 de Rham 模型：

\[
 \begin{aligned}
 \sqrt{x}\int_{\mathcal C_x}\Omega_x
 &=8\cdot16W(x)-8\pi^4y_0(x)\\
 &=128\left(W(x)-\frac{\pi^4}{16}y_0(x)\right).
 \end{aligned}
\]

冻结的 analytic conifold cancellation 于是适用于真实整 relative-cycle period，给出 (C3)。其 rational version 是 \(C-\tfrac18T\Gamma_x\)，period 为 \(\pi^2(R_0-M_0)\) 的 limit。

这里需要精确区分四件事：

1. \(\mathcal C_x\) 是 \(0<x<1\) 上明确给出的实际 integral Betti marking；乘 \(\sqrt{x}\) 可放到 algebraic cover \(x=s^2\) 上的 de Rham form。
2. 其 **period** 可全纯延拓至 conifold，且 limit 是 (C3)。在 \(x=1\) 原立方体经过 node；本稿没有把这条 punctured-family chain 当成已经构造好的 singular-fibre chain，也未标记一个 integral nearby-cycle invariant lift。
3. 没有证明 full relative Betti class 的 monodromy 消失；period-invisible 的额外 open-cohomology sectors 仍须另检。所选 scalar period 的全部 log branch 已消失。
4. Taylor constant 含 \(\pi^4\) 是真实 closed-cycle 的 period normalization，不使 corrected function 变成有理 Taylor solution；\(R_0-M_0\) 本身还除以 \(\pi^2\)，不能因 (C3) 就自动称它是未归一化 KZ period、regulator 值或无理数。

这个构造填补了“减掉 \(\pi^4y_0/16\) 是否有真实 closed Betti cycle”的旧缺口。它没有完成“该相对 extension 是否等于某个 \(CH^4(X,4)\) 的 regulator”的更强缺口。

## 5. 与实际四二次曲面 mirror 的 degree-64 商

使用 BKΣZ 一手论文 PDF 16, 19 的 actual family，而非只因 PF 相同就识别 motives：

\[
 M_\psi\subset\mathbb P^7:\quad
 P_j=X_j^2+Y_j^2-2\psi X_{j+1}Y_{j+1}=0,
 \qquad j\in\mathbb Z/4.
 \tag{5.1}
\]

其 group 为

\[
 \Gamma=(\mu_4)^4/\mu_4^{\rm diag},\quad|\Gamma|=64,
\quad(X_j,Y_j)\mapsto
 (\xi_jX_j,\xi_{j-1}^2\xi_j^{-1}Y_j).
 \tag{5.2}
\]

在 dense open 定义

\[
 u_j=\frac{X_j^2-Y_j^2}{X_j^2+Y_j^2}.
 \tag{5.3}
\]

两项平方在 (5.2) 下均乘 \(\xi_j^2\)，故 (5.3) 为 \(\Gamma\)-invariant。并且

\[
 \prod_j(1-u_j^2)
 =\frac{4^4\prod_j(X_jY_j)^2}
 {\prod_j(X_j^2+Y_j^2)^2}=\psi^{-8}.
\]

因此 map 是

\[
 \boxed{p:M_\psi\dashrightarrow V_x,\qquad x=\psi^8.}
 \tag{5.4}
\]

**参数反演必须保留。** BKΣZ 的 \(z=(2\psi)^{-8}\)，其归一化 hypergeometric parameter 为 \(t=256z=\psi^{-8}=1/x\)。本稿的 cube parameter 不是其 native \(t\)。

下面证明 map degree 是 64，不只给出 invariant rational functions。令

\[
 r_j=X_j/Y_j,\quad s_j=r_j+r_j^{-1},\quad b_j=X_jY_j,
 \quad c=2\psi.
\]

给定 generic \(u\in V_x\)，首先有

\[
 r_j^2=\frac{1+u_j}{1-u_j}.
\]

四个 square roots 原有 16 个选择。closure 的唯一 compatibility 为 \(\prod s_j=c^4\)。其平方自动成立，因为

\[
 \prod s_j^2=\frac{4^4}{A}=c^8.
\]

翻转一个 \(r_j\) 改变 \(s_j\) 的符号；所以恰有 8 个 roots 选择满足 unsquared compatibility。取 projective patch \(Y_0=1\)，则 \(b_0=r_0\)，并令

\[
 b_{j+1}=s_jb_j/c,\qquad j=0,1,2.
\]

接着对 \(j=1,2,3\) 解 \(Y_j^2=b_j/r_j\)，有另外 8 个选择；令 \(X_j=r_jY_j\)。最后 \(P_3=0\) 恰由 \(\prod s_j=c^4\) 保证。共得到 64 个 generic projective points。全部坐标非零时 \(\Gamma\) 作用自由：一个 projectively fixed group element 必须所有 \(\xi_j\) 相同，正是已商去的 diagonal。因此

\[
 \boxed{\mathbb Q(\psi)(M_\psi)^\Gamma
       =\mathbb Q(\psi)(V_{\psi^8})}
 \tag{5.5}
\]

即 \(V_{\psi^8}\) 与实际 compact mirror 的 \(\Gamma\)-quotient **birational**。这里没有声称这个 affine chart 是 compact mirror 的完整整模型。primary 明确 generic \(M_\psi\) 已有 32 个 nodes，compact mirror 还要处理 quotient curves、fixed nodes 与 resolution。

参数反演对应的 PF gauge 也可直接校验：对 \(t=1/x\)

\[
 P_{4,x}[x^{-1/2}y(1/x)]
 =-x^{1/2}(P_{4,t}y)(1/x).
 \tag{5.6}
\]

所以不是把 native MUM point 原封不动搬到 cube 的 \(x=0\)。

## 6. 固定 ambient orientation 的精确 raw residue 尺度

为避免与 primary 的 form normalization 混淆，单独定义 raw algebraic form。取 ambient projective coordinate order

\[
 (Y_0,X_0,X_1,Y_1,X_2,Y_2,X_3,Y_3).
\]

在 \(Y_0=1\) 上，其 ambient volume 为

\[
 \mu_7=dX_0\wedge dX_1\wedge dY_1\wedge dX_2
       \wedge dY_2\wedge dX_3\wedge dY_3.
\]

取 \(P_0,P_1,P_2,P_3\) 的 iterated residue order，定义 \(\omega_M=\operatorname{Res}(\mu_7/(P_0P_1P_2P_3))\)。这是 **本文** 的 raw form；BKΣZ Eq. (2.40) 另乘 \((2\psi)^4\)，且其 ambient coordinate order 不同，不可偷换其 integral period normalization。

在上述 \((r,b)\) coordinates 中，\(b_0=r_0\)，令 \(S=\prod s_j\)、\(Q=S-c^4\)。先有

\[
 \mu_7=-\frac{dr_0\wedge dr_1\wedge dr_2\wedge dr_3
                    \wedge db_1\wedge db_2\wedge db_3}
                  {8r_1r_2r_3}.
\]

前三个 equations 对 \((b_1,b_2,b_3)\) 的 Jacobian 为 \((-c)^3\)；elimination 后 \(P_3=b_0Q/c^3\)。因此

\[
 \omega_M=\operatorname{Res}_{Q=0}
 \frac{dr_0\wedge\cdots\wedge dr_3}{8\prod_jr_j\,Q}.
 \tag{6.1}
\]

另一方面 \(du_j=4r_j(r_j^2+1)^{-2}dr_j\)，且

\[
 F_x=\frac{(S-c^4)(S+c^4)}{S^2},\qquad c^8=256x.
\]

故在该 chart

\[
 p^*\Omega_x=\frac{256\,dr_0\wedge\cdots\wedge dr_3}
                  {\prod_jr_j\,Q(S+c^4)}.
\]

对 \(Q=0\) 取 residue 并与 (6.1) 比較，得到

\[
 \boxed{p^*\operatorname{Res}\Omega_x
        =\frac{64}{\psi^4}\omega_M},\qquad
 \boxed{\sqrt{x}\,p^*\operatorname{Res}\Omega_x=64\omega_M}
 \quad(\sqrt{x}=\psi^4).
 \tag{6.2}
\]

第二式展示 \(\sqrt{x}\) 在 actual geometry 内的用途；它不是仅从 forcing 的外观猜一个 half-twist。系数 64 是固定 raw form 与 fixed orientation 的精确计算，但本稿没有从它免费推出 compact resolution 的 integral trace matrix、saturation 或完整 quotient lattice。

## 7. 另一个精确 finite quotient：标准 Euler double cover

\(G_{\rm even}=\ker\chi\) 的阶为 8。其 function field 用

\[
 t_i=1-u_i^2\quad(i=0,1,2),\quad
 v=u_0u_1u_2u_3,\quad z=T v
\]

生成，并满足

\[
 z^2=-\frac{T(1-t_0)(1-t_1)(1-t_2)(1-xT)}{x}.
\]

在 \(\kappa^2=-x\) 的 algebraic base extension 上令 \(w=\kappa z\)，得到

\[
 \boxed{w^2=t_0t_1t_2(1-t_0)(1-t_1)(1-t_2)(1-xt_0t_1t_2).}
 \tag{7.1}
\]

这是精确 degree-8 function-field quotient；不是只说两个 equations “形式类似”。留数 convention 与 §3 相同，\(dt_i=-2u_i du_i\)，故

\[
 \operatorname{Res}\Omega_x=\frac{dt_0\wedge dt_1\wedge dt_2}{16xz}
 =-\frac{dt_0\wedge dt_1\wedge dt_2}{16\kappa w}.
 \tag{7.2}
\]

取 \(\kappa=i\sqrt{x}\) 时即 \(i\beta_x/(16\sqrt{x})\)，\(\beta_x=dt_0dt_1dt_2/w\)。这个 quotient 可用于下一轮 compact cycle 与 integral lattice 比较；本文 §3 的 actual affine torus 已经给出 closed cycle，故不需要将有 branch crossings 的 compact real box 未经 resolution 就当成 smooth integral cycle。

## 8. 真正的 toric 变换与 Stieltjes period

令

\[
 v_j=\frac{1+u_j}{1-u_j},\qquad
 \phi(v)=\prod_j(v_j+2+v_j^{-1})
       =\frac{\prod_j(v_j+1)^2}{\prod_jv_j}.
\]

则 \(A=256/\phi\)、\(du_j=2dv_j/(v_j+1)^2\)，从而有 exact identity

\[
 \boxed{\Omega_x=\frac{16\,d\log v_0\wedge\cdots\wedge d\log v_3}
                        {\phi(v)-256x}.}
 \tag{8.1}
\]

全 cube 映到正实 orthant，故

\[
 \boxed{B(x)=\int_{(0,\infty)^4}
                  \frac{d\log v_0\cdots d\log v_3}{\phi(v)-256x}.}
 \tag{8.2}
\]

\(B(0)=1\) 也由四个 \(\int_0^\infty dv/(1+v)^2=1\) 核验。这里是确定的 positive real relative period / Stieltjes-type integral，没有自动识别为某个 Mahler-measure special value。对应 toric family 为 \(\phi=256x\)，即 \(1-t\phi=0\) 的 \(t=1/(256x)\)；\(\operatorname{CT}\phi^n=\binom{2n}{n}^4\)，归一化 holomorphic period parameter 再次是 \(1/x\)。

在 \((\mathbb P^1)^4\) 中，该 hypersurface 的 multihomogeneous equation 为

\[
 \boxed{\prod_j(a_j+b_j)^2-256x\prod_ja_jb_j=0,}
 \tag{8.3}
\]

各 factor degree 为 \((2,2,2,2)\)。这是研究 boundary correction 与 higher-Chow lift 的具体模型。

## 9. Coordinate Milnor K4 symbol 的全部 divisorial boundary residues

取 generic smooth fibre 的 rational function field，定义

\[
 \xi=\{v_0,v_1,v_2,v_3\}\in K_4^M(k(V_x))\otimes\mathbb Q.
\]

**命题。** 对 (8.3) 任意 proper resolution 上的每个 boundary divisorial valuation，\(\partial_E\xi=0\) in \(K_3^M(k(E))\otimes\mathbb Q\)。

证明：boundary center 至少一个 coordinate \(a_jb_j=0\)。由 (8.3)，至少一个 \(a_k+b_k=0\)；这样的 \(k\) 与那个 vanishing coordinate 不同，因为同一 projective coordinate pair 不会同时为零。因此至少一个 \(v_k\) 沿 valuation 为 unit，并有 residue \(\bar v_k=-1\)。把该 unit 移到 symbol 首位；Milnor residue 与 unit product compatible，\(\partial_E\xi\) 含有 \(\{-1\}\) 因子，故是 2-torsion，在 \(\mathbb Q\) 后为零。这也覆盖 exceptional divisors：只要 center 在 toric boundary，某个 coordinate 的 residue 仍是 \(-1\)。center 在 torus 的 valuations 则所有 \(v_j\) 为 units，tame residue 自动为零。证毕。

这个结果是 **codimension-one unramified Milnor K4 condition**。本稿没有把它等同于 Doran–Kerr 的完整 temperedness，也没有由它推出 \(\xi\) 已有 global \(CH^4(X,4)\) lift：higher-Chow boundary class 的 field restriction 可丢失信息，而且 n=4 的 completion spectral sequence 还有 \(d_2\) 问题。

## 10. 一手 Doran–Kerr 定理的精确可用与不可用范围

本轮新增保存 published primary PDF：Doran–Kerr, *Algebraic K-theory of toric hypersurfaces*, CNTP **5** (2011), 397–600, DOI [10.4310/CNTP.2011.v5.n2.a3](https://doi.org/10.4310/CNTP.2011.v5.n2.a3)，204 PDF pages。使用 published Theorem **3.1**；author snapshot 的 numbering 不同，本稿不混用。

实际阅读并核对：PDF 7–9；48–56；73–78；79–82。PDF 53 与 55 已 render 并实际视读，分别对应 printed 449 与 451。没有宣称阅读全文。

关键事实如下。

1. PDF 48–50, Definition 3.1：regular 要求 generic \(\lambda-\phi\) Δ-regular。Definition 3.2 的 temperedness 要求各 toric-face coordinate symbols 在相应 **higher Chow groups** 中 trivial（rational coefficients），不只是 function-field tame residues 为零。
2. PDF 53, Theorem 3.1：n=4 还要求 regular、totally real field，以及 two-face/edge components 的 stated rationality/dominant-morphism 条件。\(\phi\) 的 coefficients 在 \(\mathbb Q\)，但下面的 regularity 条件明确失败。
3. PDF 55–56：smooth completion proof 中，n=2,3 的 kernel 条件是 \(\ker d_1\)，而 n=4 是 \(\ker d_1\cap\ker d_2\)。该 \(d_2\) 不是简单的第二 iterated tame residue。作者用 \(K_3^{\rm ind}(K)\otimes\mathbb Q=0\)（totally real K）与 rational curve strata 来消除 obstruction。此处不能只用 §9 的 unramified condition 越过去。
4. PDF 73–74：其 higher normal function 与 forcing/Yukawa formula 先假设 actual motivic completion 已经构造。这里的 \(B\) 实相对链不是已给出的 higher-Chow cycle。
5. PDF 75, Remark 4.5(iii)：作者明确指出，要产生 n=4 的更多此类例子可能需要放宽 regularity / generic-fibre singularity 条件。这是当前问题的针对性缺口，而不是“读到一个普遍定理就完成 regulator 识别”。

现在直接检验本例：\(\phi\) 的 Newton polytope 为 \([-1,1]^4\)，是 reflexive。每一个 facet polynomial，除去 monomial unit 后，含有

\[
 \prod_{j\ne k}(v_j+1)^2.
\]

其 face hypersurface 有 nonreduced components（例如 \(v_j=-1\)），因此不 Δ-regular。故

\[
 \boxed{\phi\text{ reflexive，但不 regular；published Theorem 3.1 不能直接套用。}}
 \tag{10.1}
\]

这不是数值怀疑，而是具体 facet equation 的严格反例。正因为边界由 \(v_j=-1\) 构成，§9 的 tame vanishing 特别强；但同一个 repeated-root 结构也产生 regularity failure。必须处理这个明确的几何障碍。

## 11. Gauss–Manin quotient 与监管结论的边界

当前已经有 actual relative pair、actual integral relative marking、actual closed tube、精确 finite quotient，以及正则化 **period**。所以“这个 scalar period 没有任何真实几何链支撑”的缺口已被填掉。

完整 \(H^3(V_x)\) 及其 \(\chi\)-sector 的维数，本稿不假定为 4；open/boundary cohomology 可含额外 Tate 或其他 components。式 (5.5) 与 (6.2) 识别的是 compact CY 的 canonical-form sector 和 actual birational model，而不是所有 open relative cohomology。通过共同 proper resolution、restriction 的 MHS weight filtration，可以继续抽取 compact rank-four pure sector；完整 integral quotient 与 saturation 仍需逐项给出，不能仅由 absolute irreducible PF module 自动填空。

当这一 pure-sector restriction / projector 的完整模型被标记后，(2.2) 沿它抽取的 dual extension 将具有形式

\[
 0\longrightarrow\mathbb V_4^\vee(1)
 \longrightarrow\mathbb E^\vee\longrightarrow\mathbb Q(0)
 \longrightarrow0.
\]

compact weight-three polarization 给 \(\mathbb V_4^\vee(1)\simeq\mathbb V_4(4)\)，weight −5。它符合 Hodge-theoretic higher normal-function 的 weight，而不是普通 curve normal function 的 weight −1。本稿明确只把它当作 **下一步要完整标记的 geometric sector**；不宣称 arbitrary \(\sqrt{x}\) forcing 已证明某个 admissible algebraic normal function，也不宣称已获得 motivic cohomology class。

实际 cycle (C2) 已经给 arithmetic holonomy 测试一个明确对象：必须以 \(8C-T\Gamma\) 的 full relative array 与 boundary constant 为基底；不能再只拿一个 scalar homogeneous period 或任意 numerical combination 代替它。\(\sqrt{x}\) cover、tube 的 Tate normalization、factor 8 与 quotient degree 64 都必须保留。

## 12. 新的可执行缺口清单

下一轮优先项已经变得具体。

* 在 (8.3) 上作 explicit boundary resolution / hyper-resolution，记录 repeated components 与 exceptional divisors；证明 coordinate symbol 的 **higher-Chow boundary classes** 消失，而不只证明其 generic tame residues。
* 建立相应 completion double complex，实际定位 n=4 的 \(d_2\) target；若 strata 全由 rational pieces 组成，证明所需 \(K_3^{\rm ind}\) / gluing obstruction 消失，或明确得到非零 obstruction。
* 将所得真正 \(CH^4(X,4)\) regulator current 与 §3–4 的 tube/cube marking 比较：normalization、conifold limit、inhomogeneous source 三项都须吻合。不能因它们满足同一 scalar PF 就跳过这个比较。
* 为 compact pure rank-four sector 和 relative extension 写出 integral Betti/de Rham quotient、trace 与 saturation；然后检验 CDT 型完整算术 holonomy 的成本，而不是把 \(\pi^4\) 或 finite-quotient trace 当作免费 gauge。

本轮得到的是新的精确 geometric-period / cycle result (C1)–(C3)、degree-64 birational quotient 和所有 divisorial tame vanishing。尚未得到 \(R_0-M_0\)、\(L(f_8,4)\)、\(\zeta(7)\) 或任何其他目标数的新无理性结论。

## 13. 本轮来源与可复查文件

* 冻结背景输入：[R0 Kummer period interface](cdt_odd_R0_kummer_period_interface_20261006.md) §6.1；[主报告](cdt_odd_background_progress_20261006.md) §§49–54。本轮不改这些输入。
* BKΣZ：[本地原件](../literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf)，本轮 actual read PDF 16–17, 19，分别检验 equations、group、nodes、compact quotient 与 Eq. (2.40) form normalization。
* Doran–Kerr：[本轮 published 原件](../literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf)，[publisher PDF](https://intlpress.com/site/pub/files/_fulltext/journals/cntp/2011/0005/0002/CNTP-2011-0005-0002-a003.pdf)。实际阅读范围见 §10；visual artifacts 位于 [PDF53](artifacts/cdt_odd_R0_relative_cycle_mirror_20261006/doran_kerr_pdf53.png)、[PDF55](artifacts/cdt_odd_R0_relative_cycle_mirror_20261006/doran_kerr_pdf55.png)。
* Relative MHS 的 foundational reference 为 Deligne, *Théorie de Hodge III*, PMIHÉS **44** (1974), 5–77, DOI [10.1007/BF02685881](https://doi.org/10.1007/BF02685881)，[本轮保存的 Numdam 原件](../literature/deligne1974_hodge_III_primary_20261006.pdf)，74 PDF pages。实际阅读 PDF 35–41（printed 38–44）：Proposition 8.2.2 的 functoriality、Theorem 8.2.4(iv) 的 smooth cohomology weight lower bound、Proposition 8.3.5 的 simplicial MHS spectral sequence、Example 8.3.8 与 Proposition 8.3.9 的 relative MHS exact sequence。PDF 35 与 40 已 render 并实际视读，核实 p+q≥n 与 relative exact sequence；[PDF35 artifact](artifacts/cdt_odd_R0_relative_cycle_mirror_20261006/deligne_hodgeIII_pdf35.png)、[PDF40 artifact](artifacts/cdt_odd_R0_relative_cycle_mirror_20261006/deligne_hodgeIII_pdf40.png)。本轮独立计算 D 的 nerve 与 weights，未以泛称 MHS 代替 pair construction；未宣称已读 Deligne 全文。

本文所有新数学结论为纸面符号推导；未创建或运行 mathematical producer，未使用数值 PSLQ，未宣称 Lean formalization。
