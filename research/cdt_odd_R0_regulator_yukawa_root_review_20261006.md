# R0 compact regulator、Yukawa 与正切周期接口的 root 审阅

日期：2026-10-06。NEW 审阅文件。对下列 peer 证明做独立数学审阅，对 root 自己的正切稿只作交叉接口说明；不把 self-check 写成 independent review。所有冻结 MD/PY/JSON/manifest 只读，未执行、import 或 rerun mathematical producer；本轮数学 producer 执行数为0。

## 1. 实际阅读及原件核验

本轮完整实际读：

* [compact regulator derivative](cdt_odd_R0_regulator_derivative_20261006.md)。
* [rational compact projector 与 Yukawa](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)。
* [KLM 一手来源接口 note](cdt_odd_R0_klm_current_interface_20261006.md)。
* 冻结 [真实 relative chain 与 mirror](cdt_odd_R0_relative_cycle_mirror_20261006.md) §§1–13。

root 本轮独立 actual primary reads：KLM PDF1–2,10–14,18–19；KLII PDF50–55,57–59（核心为50–54,59）；Li2018 PDF2–4；Deligne HodgeIII PDF36–38，另将37 render/view，实际核 Cor8.2.8 的 Gysin 上标和 source degree；Movasati author PDF94–95，核 positive anticlockwise、total dimension n 与 intersection 顺序；BKΣZ PDF6–7,12–14,17,19，核实际 compact mirror、half-four PF、resolved quotient 和 canonical form Eq2.40。没有宣称全文读取这些 PDF。

Deligne 原页的 root 视觉 artifact：[PDF37](artifacts/cdt_odd_R0_positive_cut_period_comparison_20261006/deligne37.png)。新增原件、版本、TLS 来源、SHA 与阅读范围纳入作者 NEW receipts；审阅数学稿及 receipt 的哈希在可变 delivery audit 最终登记，旧文件不改。

## 2. Compact derivative 的独立检查

ray order 的计算是全尺度的：fixed −1 坐标把 \(d\log(v_i)\) 写成 unit·\(z_i d\log z_i\)；horizontal primitive ray 满足 \(2\sum_{-1}a_i=\sum_{0,\infty}a_i\)，所以 top form order \(\sum_{-1}a_i-1\ge0\)。其他有 pole 的 vertical divisors 已删除。Smoothness/Hartogs 对 canonical sheaf 给真正全局 \(\Omega_Y\)，不是只在 strata generic points 得出 formal equality。

closed representative 的 \(\Omega_C\in F^4D^4\) 是 \((4,0)\)-current，\(d\Omega_C=0\) 后分布版 \(\bar\partial\) regularity 给真正 holomorphic form。Restriction class difference 是 \(\partial_B M\)，\(M\) 的 \((p,n)=(4,5)\)，于是 \(F^4D^3=0\)。这严格强制 \(\Omega_C=\Omega_Y\)，与 chosen precycle 的 boundary correction 无关。

Local proper smooth disk 的 ordinary \(H^4\) 等于 fibre \(H^4\)，而 fibre 上 holomorphic 4-form 为0；所以 \(T_C\) 的 rational BM class 为0，有 rational BM5 membrane。原始 cohomological prefactor 在 \(p=n=4\) 为1，膜为 \(+(2\pi i)^4\delta_\zeta\)。没有因为 total/fibre dimension 差一另乘 \(2\pi i\)。

对 changed representative，独立检查 KLM differential 给

\[
 R_{\partial_BM}=-dR_M/(2\pi i)-(2\pi i)^4\delta_{T_M}.
\]

同时将 membrane 改为 \(\zeta+T_M\)，两个 delta corrections 正好相消，剩下 exact current。这一抵消是 fibre regulator lift 的必要步骤。KLII prescribed-fibre moving 与 intersection-current quasi-isomorphism 可用于 pullback；本例 vertical SNC boundary 与给定 fibre 不交，满足其条件。没有要求一个 raw graph 自动横截所有 fibres。

ordinary de Rham smoothing 后，Cartan 将 Gauss–Manin derivative 变为 contraction of \(\Omega_Y=d\lambda\wedge\rho_\lambda\)。LEFT convention 因而给正号，转换回旧 cube form 为

\[
 \nabla_{\partial_\lambda}R=+\rho_\lambda,
 \qquad\nabla_{\theta_x}R=+16\sqrt{x}\,\omega_x.
\]

这个全尺度结论可以通过；它纠正冻结稿中仍带问号的 negative candidate，未改写冻结正文，也未将 DK ell2,3 lemma 当成 ell4 theorem。

## 3. Restriction injection 和 family 非平坦性的检查

实际 boundary components 的 dense fibre strata 是 \(U^2,U\times G_m,G_m^2\)；lower strata 至多维1，不能隐藏另一维2 component。每个 compact component 为 smooth projective rational surface，因此 \(H^1=H^3=0\)。

Deligne Cor8.2.8 在 target \(H^3(X)\) 的 Gysin source 是 \(\oplus H^1(E_i)(-1)\)，等价于 surface PD 下 \(\oplus H_3(E_i)\)。因此 compact \(H^3(X,Q)\to H^3(X^*,Q)\) 的 kernel 确为零。这个 corollary 已处理 SNC union 的交点贡献，不能另把开放 \(H^3\) 的所有 mixed-weight directions 说成 compact。

对 rational AJ 使用 \(F^4H^3=0\)，并在 \(Q\)-vector spaces 上 tensor \(C/Q(4)\) 的 exactness，才得到 corresponding class injection；这不是 integral saturation 的陈述。

真实 \(\Gamma\) 对 \(\rho\) 的 period 在 \(0<x<1\) 非零，所以 regulator family 非平坦。对 each rational flat Tate value，holomorphic lift 的 equality locus 至多 discrete；countable rational lattice 给 very-general 非零。这个结论不能推出任何指定 algebraic fibre 的 AJ 非零，因为 algebraic parameters 本身也只是 countable。

## 4. Rational compact sector、matrix 与 node 常数

projector 稿以实际 degree64 quotient 的 resolved compact mirror 为输入，使用其 rank4 canonical-form VHS。共同 resolution 的 degree-one maps \(X\xleftarrow aZ\xrightarrow b\mathcal W\) 给 \(i=a_*b^*\)。\((1-a^*a_*)b^*\) 在真正 holomorphic line 上为0，flatness 和实际不可约 rank4 cyclicity 令它在整个 \(H^3(\mathcal W)\) 上为0，故 \(i^*i=1\)，\(\Pi=a_*b^*b_*a^*\) 是实际 rational orthogonal projector。这里图的 two degree-one maps 与旧 degree64 quotient 不混用。

canonical form 的 cohomological PF 输入必须包含实际 \(q=1/x\) gauge；不能仅因一条 \(\Gamma\) period 满足 \(P_4\) 就断言 \(P_4\omega=0\)。Eq2.40 的尺度 \((2\psi)^4\omega_M\) 与旧 \(p^*\omega=64\omega_M\) 给 \(\omega=4\epsilon x^{-1/2}\Omega_{BK}\)，其中 fixed ambient sign \(\epsilon\) 不影响 PF。反演 identity 把完整 PF 转为 \(P_{4,x}\omega=0\)，而不是从一个 scalar solution 反推。

独立手核 cyclic matrix 与 inverse：\(Y=\kappa/(1-x)\)，\(Q(E_1,E_2)=-Y\)，\(Q(E_1,E_3)=-\theta Y\)，\(Q(E_2,E_3)=\kappa x/[2(1-x)^2]\)；inverse 的上三角 entries 为 \(x/(2\kappa),x/\kappa,-(1-x)/\kappa,(1-x)/\kappa,0,0\)。投影 coordinate formula 的前置负号来自 \(v=J^Tc=-Jc\)，正确。

\(P_4\) 关于 \(dx/x\) self-adjoint。稿中的 concomitant derivative 为 \((Ph)k-h(Pk)\)，而其 dual solution pairing 是 **negative** compact cup pairing；这个 contravariant 符号不能省略。

独立 node 检查：LEFT residue 在 real outward sphere 的首项是 \(+\pi^2(x-1)\)，所以 \(t=1-x\) 的 vanishing period \(g=at+bt^2+\cdots\) 有 \(a=-\pi^2\)。真实 torus period \(h=-4i\pi^3y_0\) 的 \(t\log t\) 系数 \(c=-4i\pi\)。Movasati 的 anticlockwise PL total dimension n4 给正 transvection；因此 \(\Gamma\cdot\delta=-8\)。

手核 conifold regular-part cancellation：\(P(g\log t)\) 的 \(t^{-1}\) coefficient 为 \(2b-3a/2\)，故 \(b=3a/4\)。concomitant 中 analytic part contribution 为 \(H(0)(-3a/2+2b)=0\)，log contributions 的常数为 \(0,-ca,+ca,+ca\)，总和 \(ca=4i\pi^3\)。所以

\[
 \kappa_{\rm raw}=-\frac{(2\pi i)^3}{16},\quad
 \kappa_{\rm dR}=-\frac1{16}.
\]

这个计算独立于 root raw KLM integral，并没有从期待的 period equality 倒推常数。

## 5. 新接口接合及不能越过的结论

将已证明的 compact derivative \(c=+16\) 代入独立 scalarization，actual compact scalar lift 满足

\[
 P_4\nu_{\rm raw}=-(2\pi i)^3\sqrt{x},\qquad
 P_4\left(-\frac{\nu_{\rm raw}}{16(2\pi i)^3}\right)=\sqrt{x}/16.
\]

actual leading coefficient \(1-x\) 必须乘回去，故无伪造的 conifold pole。它与 root [正切 raw period](cdt_odd_R0_positive_cut_period_comparison_20261006.md) 的 forcing 吻合，得到

\[
 \nu_{\rm raw}+16(2\pi i)^3W\in\ker P_4.
\]

这是 **forcing comparison**，还不是 actual marked equality。root 自稿计算的 \(\Gamma/8\) correction 与 \(8C-T\Gamma\) exact integral identity 给下一轮明确的 membrane 目标，但仍须证明 actual compact cycle representative 的 closed-period coefficients。

审阅结论：compact derivative、rational compact injection、rational projector、exact Yukawa 和 scalar forcing 可按正文限定作用域采用。root 正切稿应由 peer 单独独审。仍未完成：actual completed current 与 cube/tube lift 的精确匹配；完整 integral Betti/de Rham trace/saturation；三个 conifold jets 的算术；足够的 CDT 全 place 费用差额。没有新的 ζ、L 或 Catalan 数值无理性、线性无关性或 Lean 定理。
