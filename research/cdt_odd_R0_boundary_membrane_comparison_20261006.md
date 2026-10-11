# R₀ compact scalar 与 positive-cut scalar：边界通量、膜及四个归一化

日期：2026-10-06。NEW 纸面证明。实际全文读取主报告 §§68–72、冻结 compact derivative、positive-cut comparison、Yukawa 稿；另读 toric completion §§1–5、conifold arithmetic §§C1–C3 和 Deligne Hodge III 原件 PDF35–38。所有旧/同行 MD、PY、JSON、manifest 只读，未执行、import 或重跑数学 producer。

本稿不重复 phase-rotation 的 higher-Chow/AJ class 比较。它区分三个对象：compact cohomology lift、通过一个指定 compact-support trace 得到的 open cohomology lift、非紧的 raw scalar integral。新结论是可严格写出的比较公式和四参数恢复；uniform toroidal current bounds 尚未逐 chart 证明，故未宣布 raw scalar 等于实际标记的 compact regulator。

## 1. 固定输入与实际已有的自由度

取 \(D\subset\{0<|x|<1\}\) 为包含一段正实 interval 的小 contractible disk，固定 \(\sqrt{x}\)。在 \(D\) 上，\(f:X\to D\) 为冻结稿的 smooth proper family，\(E\subset X\) 为 relative SNC boundary，\(U=X\setminus E\)。本文的 \(X_x\) 是 compact threefold，不是原来的 open hypersurface。令
\[
 a=2\pi i,\quad \theta=x\partial_x,\quad
 P=\theta^4-x(\theta+\tfrac12)^4,\quad
 \omega=16\sqrt{x}\rho_{256x}.
 \tag{B1}
\]
已证明的 rank-four compact sector 为 \(V\subset H^3(X_x,\mathbf Q)\)，有 horizontal rational orthogonal projector \(\Pi\)，cyclic basis \(E_j=\nabla_\theta^j\omega\), \(0\le j\le3\)。固定
\[
 Q(\alpha,\beta)=\int_{X_x}\alpha\wedge\beta,
 \qquad \kappa=-a^3/16,
 \qquad Q(\omega,E_3)=\kappa/(1-x).
 \tag{B2}
\]
唯一 family Chow class 的 compact AJ lift \(r\) 满足
\[
 \nabla_\theta r=16\sqrt{x}\omega,
 \quad \nu_{\rm raw}=Q(r,\omega),
 \quad P\nu_{\rm raw}=-a^3\sqrt{x}.
 \tag{B3}
\]
但该 lift 未被唯一标记。对任意 flat \(q\in H^3(X_x,\mathbf Q)\)，\(r+a^4q\) 同样 lift 同一个 AJ class，微分也不变。真实 \(\Gamma\) 已给非零实例：它使 scalar 改变 \(a^4\int_\Gamma\omega\)。因此仅给 family Chow class 和 derivative，不能要求四个 homogeneous coefficients 有唯一绝对值。

已严格比较的 raw open current 是正切 \(R^+\)，其 fibre restriction 为 closed current。其非紧 integral 为
\[
 \nu_{\rm cut}=\int_{U_x}R^+\wedge\omega=-16a^3W,
 \quad P\nu_{\rm cut}=-a^3\sqrt{x}.
 \tag{B4}
\]
在 total \(U_D\) 上，四个 positive cuts 无共同交点：其 \(\phi\) 值为正实且至少256，而 \(D\) 可缩到 \(|256x|<256\)。任意 partial positive-cut subset \(S\) 与各 fibre 也 transverse：若全部未切坐标的 \(\partial\phi/\partial v_j\) 都为0，则这些坐标全部为1；被切坐标为正实，遂 \(\phi\ge256\)，矛盾。故至少一个未切 complex coordinate 的 derivative 非零，允许独立解 fibre 的两个 real equations，cut phases仍独立。逐项 current telescoping 给 \(dR^+=\Omega_Y|_{U_D}\)。Cartan 因而给普通 open cohomology 的实际身份
\[
 \nabla_\theta[R^+|_{U_x}]=16\sqrt{x}\,j^*[\omega].
 \tag{B5}
\]
这是 open current/de Rham 身份，不是完整 compact graph 的 admissibility 声明。

## 2. 新 support lemma：全部 compact H³ 可由紧支撑形式表示

每个 \(E_{i,x}\) 是 smooth projective rational surface，故 \(H^3(E_{i,x},\mathbf Q)=0\)。令 \(\widetilde E_x=\coprod_iE_{i,x}\to E_x\) 为 SNC union 的 resolution。Deligne Hodge III PDF37 的 Proposition8.2.7，应用于 \(\widetilde E_x\to E_x\hookrightarrow X_x\)，严格给
\[
 \ker[H^3(X_x)\to H^3(E_x)]
 =\ker[H^3(X_x)\to H^3(\widetilde E_x)].
\]
右边为全部 \(H^3(X_x)\)，所以
\[
 \boxed{H^3(X_x,\mathbf Q)\longrightarrow H^3(E_x,\mathbf Q)
        \text{ 是零映射。}}
 \tag{B6}
\]
这里用 actual primary Proposition，不假设 \(H^3(E_x)\) 本身为零；SNC intersections 可能贡献其 lower-weight cohomology。

Deligne 同页证明中的 relative exact sequence于是给
\[
 H^2(X_x,\mathbf Q)\longrightarrow H^2(E_x,\mathbf Q)
 \longrightarrow H^3_c(U_x,\mathbf Q)
 \xrightarrow{j_!}H^3(X_x,\mathbf Q)\longrightarrow0.
 \tag{B7}
\]
故全部 compact degree-three classes都有 compact-support lift；其自由度准确为
\[
 K_x=\ker j_!\simeq
 \operatorname{coker}[H^2(X_x,\mathbf Q)\to H^2(E_x,\mathbf Q)].
 \tag{B8}
\]
本稿不把 \(K_x\) 设为零。先前 \(j^*:H^3(X_x)\to H^3(U_x)\) 的 injectivity 与此 support surjectivity 是不同映射。

relative SNC proper family的局部拓扑平凡化使 B7 成为 local systems 的 exact sequence。在 contractible \(D\) 上，可在一个 fibre 选任意 rational right inverse，再 flat transport，得到一个**指定、非canonical、仅局部**的 rational horizontal splitting
\[
 \sigma:V\longrightarrow H^3_c(U,\mathbf Q),\qquad j_!\sigma=i_V.
 \tag{B9}
\]
这不承诺 global monodromy-compatible splitting，不承诺 Hodge-compatible splitting或integral splitting。若要利用它，必须记录所选 rational Betti basis 和 matrix；仅知存在不能把它当作已经计算好的 normalization。

由 open Poincaré pairing 定义 adjoint trace
\[
 Q(\tau_\sigma\alpha,v)
 =\int_{U_x}\alpha\wedge\sigma(v),\qquad v\in V_x.
 \tag{B10}
\]
nondegenerate compact polarization保证唯一的 rational horizontal \(\tau_\sigma:H^3(U)\to V\)。Projection formula 给 \(\tau_\sigma j^*=\Pi\)。这个 trace 不将 higher-weight open classes 自动杀掉；其值依赖指定的 \(\sigma\)。

## 3. 真正 Stokes 公式：raw integral 与 support trace 相差什么

令 \(\beta_x\) 是 \(\sigma(\omega_x)\) 的 smooth closed compact-support representative，延零到 \(X_x\)。由 \(j_![\beta_x]=[\omega_x]\)，存在 smooth \(2\)-form \(k_x\) on \(X_x\) 使
\[
 dk_x=\omega_x-\beta_x.
 \tag{B11}
\]
取 \(\chi=1\) near \(E_x\)、support在其 collar内；置
\[
 \beta'_x=\omega_x-d(\chi k_x).
 \tag{B12}
\]
它compactly supported于 \(U_x\)，且与 \(\beta_x\) 在 \(H^3_c(U_x)\) 中相同：其差是 \(d[(1-\chi)k_x]\)，primitive亦compactly supported。参数上可用固定 local trivialization及smooth Green operators选取这些forms；无需用该选择固定未知 Betti constants。

取避开 cuts nontransversality 的 smooth exhaustion \(K_\epsilon\Subset U_x\)，boundary用 outward orientation。固定 \(\epsilon>0\) 时，可由 current regularization或transverse-cut Stokes解释。因为 fibre \(dR^+=0\)、degree \(R^+=3\)，
\[
 d(R^+\wedge\chi k_x)=-R^+\wedge d(\chi k_x).
\]
故精确符号为
\[
 \int_{K_\epsilon}R^+\wedge\beta'_x
 =\int_{K_\epsilon}R^+\wedge\omega_x
   +\int_{\partial K_\epsilon}R^+\wedge\chi k_x.
 \tag{B13}
\]
compact-support integral已稳定，raw integral按冻结正切证明收敛。因此下式边界limit确实存在：
\[
 \boxed{B_\sigma(x):=\lim_{\epsilon\downarrow0}
        \int_{\partial K_\epsilon}R^+\wedge\chi k_x,
 \quad F_\sigma(x):=Q(\tau_\sigma[R^+],\omega)
                 =\nu_{\rm cut}(x)+B_\sigma(x).}
 \tag{B14}
\]
这证明 boundary flux 的存在和符号，不证明它为零。形式 \(i_*T\) 与 \(\omega\) pairing为零，不等于 B14 的 flux为零：后者用的是 boundary **primitive** \(k_x\)，并非 surface上的 \(\omega\)。

B5、B9 给 \(\nabla_\theta\tau_\sigma[R^+]=16\sqrt{x}\omega\)。actual compact scalarization遂给 \(PF_\sigma=-a^3\sqrt{x}\)，所以
\[
 \boxed{PB_\sigma=0.}
 \tag{B15}
\]
此外 \(d_\sigma:=\Pi r-\tau_\sigma[R^+]\) 是flat complex \(V\)-section，故
\[
 \boxed{\nu_{\rm raw}-\nu_{\rm cut}
        =B_\sigma+Q(d_\sigma,\omega).}
 \tag{B16}
\]
这两个项是分开的比较障碍，不把二者设为0。

若另一个实际 phase/AJ proof 建立
\[
 AJ(\Xi_x)|_{U_x}=[R^+]\pmod{H^3(U_x,\mathbf Q(4))},
 \tag{M}
\]
则 \(j^*r-[R^+]=a^4q_U\)，\(q_U\) 为flat rational open class，于是
\[
 d_\sigma=a^4\tau_\sigma(q_U),\qquad
 \nu_{\rm raw}-\nu_{\rm cut}=B_\sigma
             +a^4Q(\tau_\sigma q_U,\omega).
 \tag{B17}
\]
只有在这个**指定 rational trace**下最后一项才被严格识别为compact rational Tate period。不能先验认为 \(q_U\) 本身来自compact cohomology，也不能用M免费消去 Bσ。

## 4. canonical relative form 与 horizontal splitting不可混用

\(\omega\) 作为holomorphic three-form，其 pullback到每个surface \(E_i\) 是逐点0。因而可在SNC pair的relative de Rham complex中取 canonical class \([\omega,0]\in H^3(X,E)\simeq H^3_c(U)\)。该complex可直接用 
\(\{\alpha\in\mathcal A_X^\bullet:i_i^*\alpha=0\ \forall i\}\)
实现：在局部normal-crossing polydisk，保持每个 \(E_i\) 的radial homotopy证明boundary stalk acyclic；该fine complex因此计算pair cohomology。这个表述不把reducible \(E\) 当光滑surface。

在regular boundary neighborhood \(N\) 上，\(N\) 与 \(E\) 同伦等价；relative cohomology为0。因此可取smooth primitive \(\eta\) 满足 \(d\eta=\omega\) 且 \(i_i^*\eta=0\) 对全部 \(E_i\)。由它构造的compact-support form代表 \([\omega,0]\)。在每个smooth boundary face \(r_j=\epsilon\)，其tangential restriction为 \(O(\epsilon)\)。

但是 \([\omega,0]\) 仍未被识别为 B9 的 rational-horizontal \(\sigma(\omega)\)；差在 \(K_x\otimes\mathbf C\)。Hodge filtration 中boundary kernel没有 \(F^3\) 可给 canonical top-Hodge lift，但不使该lift变成rational horizontal splitting。若使用canonical relative pairing，对 \(q_U\) 的pairing必须保留为open rational Tate / relative-period项，不能直接登记成compact closed-cycle period。

一个可执行的充分条件为：对全部boundary corner charts及参数compact subdisk，rawcut angular Jacobians具有uniform lower bound，其regularized currents仅有uniform polylogarithmic增长；则 \(\eta|_{r_j=\epsilon}=O(\epsilon)\) 给各面flux \(O(\epsilon|\log\epsilon|^N)\to0\)，得到
\[
 \int_U R^+\wedge[\omega,0]=\nu_{\rm cut}.
 \tag{B18, conditional}
\]
horizontal rays的实际order \(\operatorname{ord}\Omega=\sum_{v_i=-1}a_i-1\ge0\) 有利于该estimate；且至少一个coordinate趋于−1，其positive cut不穿该collar。原fixed-lattice monomial角度矩阵也提供rank检验。然而当前尚未在所有overlapping corners、cut subsets和fibreconstraint上给出uniform determinant与partition-of-unity estimates。本稿不把这几条局部迹象提升为B18证明，也不从B18免费推出Bσ=0。

## 5. 四个系数的唯一恢复及实际Γ/8目标

取ordinary point \(x_0\in D\)，\(t_0=1-x_0\)。令
\[
 H=\nu_{\rm raw}-\nu_{\rm cut},\qquad
 h_j=(\theta^jH)(x_0),\quad0\le j\le3.
 \tag{B19}
\]
\(PH=0\)，所以四个 \(h_j\) 唯一确定它。存在唯一flat complex class \(d_H\in V\otimes\mathbf C\) 使 \(H=Q(d_H,\omega)\)。冻结Yukawa的actual Gram inverse给
\[
\begin{aligned}
 d_H={1\over\kappa}\{&(-x_0h_1/2-x_0h_2+t_0h_3)E_0
 +(x_0h_0/2-t_0h_2)E_1\\
 &+(x_0h_0+t_0h_1)E_2-t_0h_0E_3\}_{x=x_0}.
\end{aligned}
 \tag{B20}
\]
符号是 \(-J^{-1}h\)，不是 \(+J^{-1}h\)。它确定representation中的flat class，而不是凭19维或其它module闭包猜scalar维数。

若取四个实际rational \(V\)-cycles \(\gamma_a\)，令
\[
 M_{ja}=\int_{\gamma_a}E_j(x_0),\qquad
 y_a(x)=\int_{\gamma_a}\omega_x,
\]
则 \(M\) 可逆，\(H=\sum_ac_ay_a\)、\(c=M^{-1}h\)。必须记录cycle transport与matrix；不能以formal Frobenius basis替代actual integral marking。

具体可检验的数据由 B16 给
\[
 h_j=(\theta^j B_\sigma)(x_0)
      +Q(d_\sigma,E_j(x_0)).
 \tag{B21}
\]
不能未经uniform differentiation estimate把 
\(\theta^jB_\sigma\)
替换成某个猜测的单独boundary integral of \(E_j\)；需在固定family trivialization下连同moving domain、cut和primitive一起微分。B13–B14给无此偷换的definition。

已严格知道的候选修正是
\[
 \nu_{\rm corr}=\nu_{\rm cut}+{a^4\over8}\int_\Gamma\omega.
\]
因此 actual marked equality \(\nu_{\rm raw}=\nu_{\rm corr}\) 的**完整四个必要充分条件**为
\[
 \boxed{h_j={a^4\over8}\int_\Gamma E_j(x_0)
             =-8i\pi^7(\theta^jy_0)(x_0),\quad j=0,1,2,3.}
 \tag{B22}
\]
这给具体目标向量，而不是只求一个自由常数。Γ/8只给rank-one period修正，不消除其余三个方向；有限endpoint也不消除任何方向，因为conifold \(t\log t\) 解同样趋于0。

## 6. 节点vanishing归一化只解决其中一项

root独立提出的actual local regulator检验可与本稿接合。在node \(v_j\simeq1\) 的小neighborhood，negative cuts避开，有
\[
 R_{\rm loc}=\log v_0\,d\log v_1\wedge d\log v_2\wedge d\log v_3.
\]
realvanishingsphere半径 \(r\) 上其integral为 \(O(r^4)\)，故 \(A_\delta(1)=0\)。冻结actual vanishing period \(g=-\pi^2v(t)\)，\(v(t)=t+3t^2/4+\cdots\)，与B5的positive derivative给
\[
 A_\delta(t)=16\pi^2\int_0^t{v(s)\over\sqrt{1-s}}ds.
 \tag{B23}
\]
concomitant满足 \(\theta C_0(W,g)=\sqrt{x}g/16\)。actual \(C_0(y_0,g)=-1\)，analytic \(\Psi=W-\pi^4y_0/16\) 与 \(g\) 的endpoint concomitant为0，遂
\[
 A_\delta=256C_0(W,g)+a^4
 ={C_0(\nu_{\rm corr},g)\over\kappa}.
 \tag{B24}
\]
此处PD dual sign给 \(C_0(\nu_{\rm raw},g)/\kappa=\int_\delta r\)。如果actual local AJ pullback已经核准，compactlift的δ值为 \(A_\delta+a^4q\)，\(q\in\mathbf Q\)。由于 \(\delta\cdot\Gamma=8\)，调膜 
\(-q a^4PD(\Gamma)/8\)
可令它恰为 \(A_\delta\)；不能默认未标记的 \(q=1\)。这一证明的actual local-AJ compatibility与最终source范围由root的独立稿负责，本稿只独核公式、方向与尺度。

归一化后
\[
 C_0(\nu_{\rm raw}-\nu_{\rm corr},g)=0.
 \tag{B25}
\]
homogeneous PF的PL log方向由该非零linear functional测出，所以差额落在三维conifold holomorphic sector。其三个Taylor data \(c_0,c_1,c_2\) 可自由指定，冻结C3递推唯一决定以后各项。故B25之后，精确要求三个actual holomorphic jets为0才能完成比较；不能从holomorphy或boundedness把这三个系数删除。

## 7. 可执行的全尺度下一步和本轮边界

1. 明确实际lift：记录rational admissible \(C\)、Bloch homotopy \(M\)、membrane \(\zeta\) 及其允许的closed-cycle adjustment。一个AJ class不足以唯一指定这些数据。
2. 为B9选择实际rational Betti splitting matrix，或坚持canonical relative form并保留open lattice项；不能混用两种trace。
3. 对有限fixed-lattice regular fan逐cone列出cut subset、原exponent matrix和fibre constraint的real Jacobian。只有uniform bounds、corner partitions和moving-parameter estimates全部完成，才可把B18从候选升为定理。
4. 独立phase/AJ proof一旦给M，计算 \(q_U\) 与所选trace的 \(\tau_\sigma(q_U)\)，同时求四个Bσ jets。用B22直接核准Γ/8；若先完成B25，便只剩三个actual holomorphic jets，但仍须实际证明。

本轮实际正结果是B6–B17的support与Stokes比较接口，以及B20–B22的完整系数恢复。未证明Bσ=0、未标记actual membrane等于Γ/8、未得到任何目标数的新无理性/线性无关性。新增数学producer执行数0；旧/同行producer执行或import数0。

## 8. 实际输入与source receipt

* [冻结compact derivative](cdt_odd_R0_regulator_derivative_20261006.md)，实际全文；SHA256 `5a3ba4ed679a5565375efdb0b9c39e4a69338e72bcce5938b5a34356d816e091`。
* [冻结positive-cut comparison](cdt_odd_R0_positive_cut_period_comparison_20261006.md)，实际全文；SHA256 `fb44cacdd85484887a51c90c7547432eff5ceb0516b356a3fbc26a5f97f65dc8`。
* [冻结Yukawa](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)，实际全文；SHA256 `172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15`。
* [toric completion](cdt_odd_R0_toric_completion_20261006.md)本轮实际 §§1–5；[conifold recurrence](cdt_odd_conifold_arithmetic_center_20261006.md)本轮实际C1–C3。不冒认本轮额外全文阅读。
* [Deligne Hodge III actual primary](../literature/deligne1974_hodge_III_primary_20261006.pdf)，本轮实际PDF35–38：Prop8.2.7和Cor8.2.8的relative sequence，未声称全书/全文阅读。SHA256 `d78d4f46742916cd669279e7db365e4db6a43f38d2dcdec6862c6d27d07216b3`。使用既存已验证primary，本稿无新增下载。
* KLM2006 published primary PDF10–14、18–19在上一轮独审已实际读；本轮为local vanishing稿独审实际另读PDF8、12–13：unit product、ring map及p=n4 evaluation。SHA256 `8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9`。本稿Stokes符号、local relative-form lemma和四参数公式为独立纸面推导。
