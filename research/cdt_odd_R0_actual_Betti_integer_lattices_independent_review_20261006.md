# 实际消失周期格与 regulator Betti 整扩张：独立审阅

日期：2026-10-06。NEW review。全部旧稿及同行数学 MD/PY/JSON/manifest 只读；没有执行、import、重跑任何旧稿/同行 verifier，没有新的数学 producer。

## I1. 实际全文审阅范围

实际全文独读下列两稿，并核对完整指纹：

- cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md，SHA256 baf29ee041a0ea48c4b64c517cf0712f24c52c4c98893e4c74a98698c7e05586，包括 O1–O38 与执行范围。
- cdt_odd_R0_regulator_Betti_extension_flag_20261006.md，最终候选 SHA256 4abdcbc370b69413b07e837724867897760f493b7ee65e6d0b47a705f96292f4，包括 B1–B14。第一次批量输出截断 B2，随后独立补读 B2–B3；没有把截断内容冒记为已读。

此外本轮实际回读冻结 cdt_odd_R0_Yukawa_scalar_interface_20261006.md 的 Y7a–Y10、Y11–Y20、Y21–Y31 和 Y27 论证，特别 degree-one graph、full cyclic rank-four 与 actual vanishing class；该输入 SHA256 172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15。real Betti normalization、endpoint exterior 与 centered-current compact extension 已在前轮实际全文独审，本轮使用其冻结输入，不冒称本轮重新读 BK/Movasati primary 全文。

## I2. degree-one 整数升级成立

冻结 Y8 的共同 smooth proper resolution \(X\leftarrow Z\to W\) 的两映射 degree one。这里并非 degree-64 mirror cover。对同维闭定向六流形，pullback 与由整数 PD 定义的 pushforward 都是整数映射，且将 torsion 映到 torsion。因而它们下降到 \(H^3(-,\mathbf Z)/\mathrm{tors}\)。

冻结 Y9 已在 \(\mathbf Q\) 上证明
\[
 i=a_*b^*,\qquad q=b_*a^*,\qquad qi=1.
\]
同一几何对应的整数 \(qi-1\) 在 tensor \(\mathbf Q\) 后为零，free abelian endomorphism 到 rational endomorphism 单射，故 \(qi=1\) 也在 free 整格上成立。这一步没有要求预先计算对应的整数矩阵。

PD projection formula 给 \(q=i^\dagger\)，因此
\[
 Q_X(iu,iv)=Q_W(u,qiv)=Q_W(u,v).
\]
故 \(i\) 是整数 isometric split embedding，\(\Pi=iq\) 是整数 self-adjoint projector，像为 saturated rank-four 子格。闭定向六流形的 free middle pairing unimodular，于是该像 unimodular。有限覆盖上构造的 rational 正交 projector 由 cyclic sector 唯一性下降；下降后的 rational 算子在每个 fibre 等于已构造整数算子，所以 integrality 不要求一个额外的 arithmetic deck 平均。

因此 O30–O34/B2 的 integral projector、actual saturated sector 和 index256 均通过。这里升级的是已实际构造 degree-one correspondence 的整数作用，不是将任何 rational projector 免费当作 integral。

## I3. actual orbit 格、交叉数和两种 Smith 信息

从 genuine logshift 和 concomitant 得到对所有整数 \(k\)
\[
 \delta\cdot U^k\delta=\frac83(k^3+2k).
\]
其 integrality 来自 \(k^3+2k\equiv0\bmod3\)，而非有限采样。actual \(U=-M_0\) 在整数 cycles 上作用，故 \(e_j=U^j\delta\) 真正为 closed integral cycles。

Gram 的 Pfaffian 为
\[
 8\cdot8-32\cdot32+88\cdot8=-256,
\]
故 determinant \(2^{16}\)；O13 的 unitriangular 整数换基给 \(8J_2\oplus(-32J_2)\)，因此交叉同态的 Smith 为 \(8,8,32,32\)。它不是包含 \(\Lambda_\delta\subset\Lambda\) 的 Smith。unimodular saturation 给 index256，而实际包含 Smith 尚未被唯一确定；两稿准确区分这两件事。

PL column convention 给 \(M_1e_j=e_j+(e_j\cdot e_0)e_0\)，与 O17/B6 一致。\(U\) 的 companion action 来自 \((U-1)^4=0\)。物理原点为 \(-U\)，平方覆盖为 \(U^2\)；本轮没有把 signed \(U\) 当实际一圈。

O21 的 \(N^3=v\ell\)、primitive row \(\ell=(1,1,1,1)\) 与
\[
 2G=v,\qquad G\cdot z=-8\ell(z),\qquad
 N^3z=\frac{z\cdot G}{4}G
\]
相互一致；真实 double loop 的 cube 因子8保留。O26 的 \(\alpha=-3e_0+4e_1-e_2\) 本身就是 actual integral cycle，即使在 integral projector 升级之前也成立。

## I4. divisibility 补强全部成立

写 \(G=d\gamma\)，\(\gamma\) primitive in unimodular \(\Lambda\)。存在 \(z\in\Lambda\) 使 \(z\cdot\gamma=1\)；整数 \(N^3\) 给 \((d^2/4)\gamma\in\Lambda\)，故 \(d\) even。又 \(\delta\cdot G=8\)，所以 \(d\in\{2,4,8\}\)。这是 possible values，不证明 exact divisibility。

若 \(\delta=d_\delta\delta_0\)，整数 automorphism \(U\) 给
\[
 d_\delta^2\mid\delta\cdot U\delta=8,
\]
故 \(d_\delta\in\{1,2\}\)；后一 case 强迫 \(d\in\{2,4\}\)。

B7.7 的新增 \(\alpha\) even 证明也通过：在四维 symplectic \(\Lambda/2\Lambda\) 中，\(\bar\delta\) 的全部 \(U\)-orbit span 因全部交点 divisible8 而 isotropic，故维数至多2。该 span \(U\)-stable，\((U-1)^4=0\) 在特征2仍成立，因而限制到这个维数至多2的 span 上有 \((U-1)^2=0\)。由
\[
 \alpha=2(U-1)\delta-(U-1)^2\delta
\]
可得 \(\alpha\in2\Lambda\)。再由 \(\alpha\cdot U\alpha=-64\) 的平方整除，divisibility 属于 \(\{2,4,8\}\)。未将这些 possible cases 偷换成一个 actual primitive basis。

## I5. actual rank-five cocycle 和 marking 成本

中心化 compact current 的指定 scalar 是 \(-16a^3W\)，修正 scalar 是 \(-16a^3\Psi\)。令 \(f_z=-aQ(z,\omega)/16\)，Betti normalization \(r_c/a^4\) 与这两个 scalar 一致。

原点 \(W^\gamma=-W\) 及 \(\chi=-1\) 给 \(c_0=0\)；conifold \(M_1G=G-8\delta\)、\(Q(G,\omega)=a^3y_0/2\) 和 \(a^4=16\pi^4\) 给
\[
 W^{\gamma_1}-W=-ag/16=f_\delta,\qquad c_1=\delta.
\]
推向量使用完整 period germ 的 injectivity，不是 single-point 数值。整数 monodromy 及 cocycle 递推使所有 word 的 cocycle 都在 \(\Lambda\)，这是全 word-length 结论。整个 scalar rank-five system 需 twist by \(\chi\)，使原点 \(J_4(+1)\oplus(-1)\)，B5 记号准确。

修正 splitting \(u=G/8\) 后，两生成元给 \(-G/4,0\)。由 \(G\) even，cochain 安全成本4、所有 cocycle 安全成本2成立；没有宣称最小成本，也没有由 selected free Betti extension 推出 integral higher-Chow completion 成本。

## I6. rank-nine 整格、CRT 与端点目标

unimodular pairing \(\wedge^2\Lambda\to\mathbf Z\) surjective，故 canonical \(\wedge^3E_5\to\chi\) 的 kernel 是 saturated rank-nine 整格；其 centered origin decomposition 为
\[
 \wedge^3\Lambda\oplus e_c\wedge\wedge^2_0\Lambda.
\]
第二块的 unipotent length5 可直接由 \(N^4(e_3\wedge e_2)=2e_1\wedge e_0\ne0\) 验证。rank-five CRT 的 universal 成本16、最高旗标成本2，以及 rank-nine CRT 成本256、最高旗标成本32，均由 degree-less-than-minpoly 的 leading coefficient 决定。实际 centered splitting 使这些算子在所选 Betti 格上成本1；这与 universal polynomial 不同，不存在矛盾。

这些 origin spectral projectors 不与全局 conifold action 交换，不能当作 horizontal algebraic gauge。symplectic contraction \(\wedge^3\Lambda\to\Lambda\) 在 unimodular symplectic basis 中为 signed permutation，故是整数同构。

最终 B11 正确使用
\[
 \Phi(q)=\Phi_h+q(Y_{g_0}\wedge Y_{g_1}\wedge Y_{g_2}),
 \qquad N_0^3p_+\Phi(q)=0\Longleftrightarrow q=\alpha_0.
\]
最新稿明确登记并改掉了 \(y_0\) wedge 平移。本稿的实际审阅指纹4abd…92f4已包含这个修正；不将旧候选列入通过范围。

Betti 整格不使 analytic \(g_1,g_2\) 的 Taylor normalization 免费成为 rational Betti coordinates，也不删除 D7 前缀、bad-prime \(C\)、CDT meromorphic/容量条件。该端点旗标不能填平 canonical origin，见本轮独立 endpoint/holonomy 稿的有限覆盖 no-go。这些限制在两稿中保留准确。

## I7. 审阅结论及边界

两稿的上述全尺度整数几何/Betti 证明通过。本轮实质进展是 integral compact projection、actual saturated unimodular rank-four sector、orbit index256、明确 monodromy/cocycles、\(\Gamma\) even 与 \(\alpha\) even，以及整数 origin flag 算子。

本审阅没有执行或 import orbit verifier/certificate；没有声称它们验证了几何假设。没有本轮新 primary 下载或新增 Lean。没有由 Betti 整数性推出 Taylor all-place integrality、\(C=16\)、或任何 ζ/L/Catalan 数值无理性结论。all-odd \(p\)-adic Gauss–Manin generic radius 是另一接口，须另行证明 proper smooth integral model 与必要 de Rham 局部自由条件。
