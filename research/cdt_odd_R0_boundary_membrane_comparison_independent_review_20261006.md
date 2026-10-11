# R₀ boundary / membrane comparison 的独立全文审阅

日期：2026-10-06。审阅者为 conifold arithmetic-hypotheses 代理，未参与被审稿写作。实际完整读取作者最终稿 [boundary membrane comparison](cdt_odd_R0_boundary_membrane_comparison_20261006.md)，SHA256 `2bded7f6e0e6efab5e67f985df38754e5a8b2f99b4e4394d46a6f86a20952c3d`。旧/同行 MD、PY、JSON、manifest 只读；没有执行或 import 任何数学 producer，没有新 PDF 下载。本稿不是形式化证明。

审阅结论：B6–B17 的 support / splitting / flux 比较、B20–B22 的完整四系数恢复成立；B23–B25 的实际 vanishing 尺度和方向与已核输入一致。B18 仍只是未逐 chart 建立的充分估计条件，不能记成 flux-zero 定理；actual local-AJ compatibility由 root 另证。原稿明确保留了这些边界，没有得到 raw-cut scalar 与标记 compact scalar 的完整相等式，也没有新的数值无理性。

## R1. 实际输入范围

本审阅者实际完整读取：

* 被审 boundary / membrane 稿 §§1–8。
* [compact regulator derivative](cdt_odd_R0_regulator_derivative_20261006.md) §§1–8，重点 §6 的全部 boundary components 是 smooth projective rational surfaces，以及 compact H³ 的 open restriction 单射。
* [Yukawa scalar interface](cdt_odd_R0_Yukawa_scalar_interface_20261006.md) §§1–8，核 rational projector、raw cup/Tate convention、Gram matrix inverse、PL 和 contravariant sign。
* [positive-cut comparison](cdt_odd_R0_positive_cut_period_comparison_20261006.md) §§1–7，核 degree-three current、两sheet orientation、absolute convergence 和 Γ/8 修正。
* [conifold arithmetic center](cdt_odd_conifold_arithmetic_center_20261006.md) C1–C7，本轮另外实际读原 Kummer 接口全文及主记录 §§64、68–72。

实际 primary：

* [Deligne, Hodge III](../literature/deligne1974_hodge_III_primary_20261006.pdf)，PDF36–37、40–41（printed39–40、43–44）；Prop8.2.5/8.2.7、Cor8.2.8、relative-cohomology exactness。为定位另外抽取了 §8 相关页，但不冒认全文阅读。既存 SHA `d78d4f46742916cd669279e7db365e4db6a43f38d2dcdec6862c6d27d07216b3`。
* [KLM 2006 published](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，PDF13–14、18–19；§5.6 precise Tate/membrane ambiguity 与 §6–7 extension comparison。既存 SHA `8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9`。

没有重新执行任何 producer 或把作者自己的自检冒认成独审。

## R2. 全部 compact H³ 的 support surjectivity 确实成立

被审稿使用的 \(E_i\) 是实际 smooth projective rational surfaces；紧化 derivative §6 的 dense-open strata为 \(U^2,U\times\mathbf G_m,\mathbf G_m^2\)，lower strata不能再藏一个 surface component。与 \(\mathbf P^2\) 的 common resolution 只需 point blowups，故每个 \(H^3(E_i,\mathbf Q)=0\)。这并不意味着 reducible \(E\) 的 \(H^3(E)\) 为零。

实际 Deligne Prop8.2.7（PDF37）适用于
\(\widetilde E=\coprod E_i\to E\hookrightarrow X\)：\(X\) smooth proper，\(E\) proper，\(\widetilde E\) smooth proper且到 \(E\) surjective。它给
\[
 \ker(H^3(X)\to H^3(E))
  =\ker(H^3(X)\to H^3(\widetilde E)).
\]
右侧是全部 \(H^3(X)\)，因而原 restriction 为零。这个论证避免误删 SNC intersections 的 lower-weight classes。

pair \((X,E)\) 的 exact sequence，连同 \(H^3(X,E)=H^3_c(U)\)，实际给
\[
 H^2(X)\longrightarrow H^2(E)\longrightarrow H^3_c(U)
  \xrightarrow{j_!} H^3(X)\longrightarrow0.
\]
因此 B6–B8 正确，包括
\[
 \ker j_!\simeq\operatorname{coker}(H^2(X)\to H^2(E)).
\]
不要求该 cokernel 零。作为独立交叉核对，已证 \(H^3(X)\to H^3(U)\) 单射的 Poincaré transpose同样给 \(H^3_c(U)\to H^3(X)\) 满射；两条论证一致。

## R3. 指定局部 rational trace 的范围准确

proper relative-SNC family 在小 disk上局部拓扑平凡。B7 形成 exact local systems；contractible disk使它们可平凡化。在一个 fibre 选 rational right inverse后 flat transport，确实得到 B9。作者正确注明这不保证 global、Hodge 或 integral splitting。

对固定这样的 \(\sigma\)，open Poincaré pairing定义
\[
 Q(\tau_\sigma\alpha,v)=\int_U\alpha\wedge\sigma(v).
\]
两边使用相同 degree-three 顺序；非退化 \(Q|_V\) 保证唯一性，rational/flat cup保证 trace rational且horizontal。Projection formula给 \(\tau_\sigma j^*=\Pi\)。这不会无条件杀 higher-weight open classes，作者保留了 dependence on \(\sigma\)。

因此若 \(j^*r-R^+=a^4q_U\) 真正从 phase/AJ comparison得到，trace后才有
\(d_\sigma=a^4\tau_\sigma q_U\)。没有从 open rational class免费推出它原本就是compact class；B17的条件和表达式准确。

## R4. Stokes 的正号、limit和齐次差独核

对 \(\beta\) 代表 \(\sigma(\omega)\)，有 \(\omega-\beta=dk\)；取 \(\chi=1\) near \(E\)，
\(\beta'=\omega-d(\chi k)\) 既紧支撑又与 \(\beta\) 同一 compact-support class，因为差为具有紧支撑 primitive的 \(d((1-\chi)k)\)。

degree \(R^+=3\)、fibre \(dR^+=0\)，故
\[
 d(R^+\wedge\chi k)=-R^+\wedge d(\chi k).
\]
于是 outward boundary给
\[
 \int_{K_\epsilon}R^+\wedge\beta'
  =\int_{K_\epsilon}R^+\wedge\omega
    +\int_{\partial K_\epsilon}R^+\wedge\chi k.
\]
这是作者B13的正号。固定 \(\epsilon\) 可以 current regularization和transverse-cut Stokes解释；紧支撑积分稳定，raw integral已被两sheet绝对收敛证明控制，所以边界 limit 存在。它不必为零。

总空间 \(|x|<1\) 没有四个正实 cuts交点。对任意 proper subset，若所有未切 coordinate 的 complex derivatives 都零，那些coordinates全为1；已切的coordinates正实，从而 \(\phi\ge256\)，与 \(|256x|<256\) 矛盾。故partial cuts与fibres transverse，ordinary open current中 \(dR^+=\Omega_Y\) 和 Cartan 的 B5 有合法适用域。

B5加 horizontal trace给
\(\nabla_\theta\tau_\sigma[R^+]=16\sqrt{x}\omega\)。用已核 scalarization，\(PF_\sigma=-a^3\sqrt{x}\) 与 \(P\nu_{\rm cut}=-a^3\sqrt{x}\) 同时成立，故 \(PB_\sigma=0\)。\(d_\sigma=\Pi r-\tau_\sigma[R^+]\) 是flat complex section。因此
\[
 \nu_{\rm raw}-\nu_{\rm cut}
  =B_\sigma+Q(d_\sigma,\omega)
\]
正确。它保留一个boundary primitive flux与一个flat complex period，未把任何一项删除。

## R5. canonical relative form与rational horizontal trace确应分开

holomorphic three-form在每个 complex surface上拉回为零。用于pair的smooth relative complex
\(\{\alpha:i_i^*\alpha=0\ \forall i\}\)
是fine的。在boundary normal-crossing polydisk内，radial homotopy保持每个 coordinate divisor；原点在boundary上，constant evaluation亦零，所以该complex的boundary stalk acyclic。在 \(U\) 上则是ordinary de Rham complex。因而它确实计算 \(j_!\mathbf C_U\)，给canonical relative class \([\omega,0]\in H^3_c(U)\)，没有把 SNC union当光滑surface。

在可 deformation-retract 到 \(E\) 的regular neighborhood内，relative cohomology零，故可以选 \(d\eta=\omega\) 且各 \(i_i^*\eta=0\)。其face-tangential pullback为 \(O(\epsilon)\)。该canonical class未必等于所选rational horizontal \(\sigma(\omega)\)；差在 \(K\otimes\mathbf C\)，即便top-Hodge lift由 \(F^3K=0\) 唯一，也不能由此得到一个rational horizontal splitting。

B18只列出了可能使canonical-relative flux消失的量化充分条件。要真正使用，必须在current contraction、face measure和corner integrations的同一坐标约定下核准uniform polylog bounds、Jacobian与partition estimates。作者明确说这些尚未完成；本独审也未完成它们。特别是即使canonical flux为零，仍不能自动得 B9 的 \(B_\sigma=0\)。这一条件分界正确。

## R6. 四个齐次系数的恢复和Γ/8目标独核

实际 \(J^{-1}\) 代入 \(-J^{-1}h\) 给被审B20四个coordinates：
\[
 \frac1\kappa\bigl(-x_0h_1/2-x_0h_2+t_0h_3,
 x_0h_0/2-t_0h_2,
 x_0h_0+t_0h_1,-t_0h_0\bigr).
\]
这是covariant compact class的负号；与 contravariant period pairing的 dual sign相符。因cyclic basis及polarization均nondegenerate，四个jets唯一恢复flat complex class，ordinary point上的scalarODE uniqueness给完整 homogeneous solution。

实际 \(\int_\Gamma\omega=-4i\pi^3y_0\)，所以
\[
 \frac{a^4}{8}\int_\Gamma E_j
  =\frac{16\pi^4}{8}(-4i\pi^3\theta^jy_0)
  =-8i\pi^7\theta^jy_0.
\]
B22的四个必要充分条件及常数均正确。一个endpoint有限不能删log方向，\(t\log t\to0\) 即为反例。作者没有用没有证明的uniform derivative estimate替换 \(\theta^jB_\sigma\)，这一点必要且保留正确。

## R7. node / vanishing尺度交叉核证

以 \(g=-\pi^2v\)、\(v=t+3t^2/4+\cdots\)，\(\theta=-(1-t)D\) 与 \(\theta A_\delta=16\sqrt{x}g\) 给
\[
 DA_\delta=16\pi^2v/\sqrt{1-t}.
\]
localunit current在 vanishing sphere上为 \(O(r^4)\)，初值 \(A_\delta(1)=0\) 与B23吻合。

冻结Yukawa实际 \(C_0(-4i\pi^3y_0,g)=4i\pi^3\)，故 \(C_0(y_0,g)=-1\)。\(\Psi\)与 \(g\) 都全纯，endpoint concomitant为零（\(g\) 的初值满足 \([t^2]g=3[t]g/4\)、\([t^0]g=0\)）；因此 \(C_0(W,g)(1)=-\pi^4/16\)。B24的两边有同 derivative，且
\(256(-\pi^4/16)+a^4=0\)，所以其 additive constant准确。

对 \(\nu=Q(r,\omega)\)、\(g=Q(\operatorname{PD}\delta,\omega)\)，dual sign给
\[
 C_0(\nu,g)/\kappa=-Q(r,\operatorname{PD}\delta)
  =Q(\operatorname{PD}\delta,r)=\int_\delta r.
\]
这正是B24的方向。\(\Gamma\cdot\delta=-8\) 意味 \(\delta\cdot\Gamma=8\)，故shift \(-qa^4\operatorname{PD}\Gamma/8\) 恰消去δ值的 \(qa^4\) ambiguity。作者没有把未知 \(q\) 默认设为1。

对于homogeneous四维solution space，\(C_0(\cdot,g)\) 是非零functional，kernel恰为三维holomorphic conifold space：它在holomorphic空间为零，在带log的实际Γ period上非零。所以B25只给三维sector，后续三个实际jets仍需标记。local current确实代表Xi的pullback是root独立稿负责的额外输入，本独审不借这些正确尺度冒认那项完整证明。

## R8. 结论与未完成事项

该作者稿的新增support、局部rational trace、严格Stokes比较和四参数目标均通过本独立全尺度审阅；canonical relative class的构造也成立。它把此前的“存在一个未知homogeneous差”拆成可以实际计算的boundary flux和flat period，并给Γ/8的完整四jet检验向量。

尚未证明：所有corner上的B18 uniform estimate、\(B_\sigma=0\)、指定 trace matrix/整数格、phase/AJ条件M的完整前提、actual membrane已等于Γ/8，或归一化后剩余三jet为零。没有新的ζ、Catalan或L值数值结论。论文正确保留这些局限，审阅结论不扩大其scope。

本轮仅文献抽取/回读、纸面推导与SHA读取；数学producer执行数0，冻结或同行producer执行/import数0，无Lean或PSLQ claim。
