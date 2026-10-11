# R₀ noncompact Tate boundary proof：独立实际全文审阅

日期：2026-10-06。NEW 独立纸面审阅。审阅者实际全文读取
[被审稿](cdt_odd_R0_noncompact_Tate_boundary_period_20261006.md)，最初实际全文读 fb91af4863780752de6cdd215efc1714c15e0d9bd0f3dcd086656071ac8d578b，作者修订排版后再次实际全文回读最终 SHA256
00d1cb69f8cf783b842dd5c53331368bcf95fddf69135e80f614c4f0598372c1。
旧稿、同行稿、PY、JSON、manifest 均只读；数学 producer 执行/import/rerun 数为0。

**结论：N2/N3 的实际非紧化 Tate 障碍、N8–N10 的单 chart 修正，以及 N11/N12 的 open-class/raw-scalar 身份，均通过独立核查。** 该原始 positive current 的 relative boundary 非零，不能再被当成“或许可证明为零”。这与另一个 centered representative 可具有 compact extension 完全相容。被审稿没有从一个 chart 宣称所有 corners 已完成；本审阅不替同行全 corner 定理作证。

## 1. Actual chart 不是抽象 valuation 计算

实际回读冻结 [toric completion](cdt_odd_R0_toric_completion_20261006.md) §§1–5 和 §6 起始。最初 order function \(\ell=2b_0-b_1\)，以 \(\ell=0\) 切二维第一象限确实产生 primitive ray \((1,2)\)。后续 regular subdivision 不删已有 ray；在该 divisor 的 generic torus chart 可以使用
\[
 v_0=-1+s,\qquad v_1=s^2w,\quad w\ne0.
 \tag{I1}
\]
cone \(((1,2),(0,1))\) 的 determinant 为1。即使这个 cone 被继续细分，ray 的 generic chart 不变；只须避开它的其余 orbit faces。此论证使用冻结 fixed-lattice monomial modification，不使用 ramified square-root cover。

直接代入 \(\phi=\lambda\) 给
\[
 \phi=\frac{s^2}{-1+s}\frac{(1+s^2w)^2}{s^2w}\Phi,
 \qquad F=\Phi(1+s^2w)^2-\lambda(-1+s)w.
 \tag{I2}
\]
故 \(w_0=-\Phi/\lambda\ne0\)，\(F_w|_{s=0}=\lambda\ne0\)。在所选 free-coordinate compact annuli 上，\(\Phi\) 与 \(\lambda\) 有非零下界。implicit-function neighborhoods 的有限覆盖及根在 \(s=0\) 的唯一性，给统一小 \(\epsilon\) 和粘接后的 holomorphic \(w\)。这是定义在实际 compact fibre 的 chart，不能把其 \(s=0\) 一并删掉。

取盘的 complex orientation 和 free \(v_2,v_3\) 圆的 CCW orientation：
\[
 B^4=D_s^2\times S^1_{v_2}\times S^1_{v_3},\qquad
 T^3=\partial B^4.
 \tag{I3}
\]
盘的 dimension2 是偶数，free circles 没有边界，所以 product-boundary convention 给 \(T^3\) 的顺序为 CCW \((s,v_2,v_3)\)，无额外负号。I2 保证 \(s\ne0\) 时所有 coordinates 留在 open \(U_\lambda\)；\(B^4\) 留在 compact \(X_\lambda\)。因此 \(T^3\) 是 actual open cycle、actual compact boundary。

## 2. Exact residue、非compact结论及 relative obstruction

在整个 \(s\)-disk 上 \(v_0\) 靠近 \(-1\)，避开 \(v_0>0\)。因此 positive current 的后三项在这里本来为零，不涉及多重 distribution 的评价；第一项为
\[
 \left(\frac a2+\log(1-s)\right)
 \left(2\frac{ds}s+d\log w\right)
 d\log v_2d\log v_3.
 \tag{I4}
\]
free 部分的 \(d\log w\) wedge 为零，normal 部分 holomorphic，无 residue。唯一 residue 是 \(a\,ds/s\)。normal period 为 \(a^2\)，两个 free periods 各为 \(a\)，所以
\[
 \int_{T^3}R_4^+=a^4.
 \tag{I5}
\]
这是精确 period，非 asymptotic limit 或 formal residue。

actual compact \(r\) 为 fibrewise closed cohomology lift，它在 I3 上为0。将 N1 评价得
\[
 \langle a_U,T^3\rangle=-1.
 \tag{I6}
\]
任何 \(j^*q\)、\(q\in H^3(X,\mathbf Q)\) 在 \(T^3\) 上都为0，所以所有合法 compact Tate lift 都保留 I6。若 \(a_U\) 来自 compact image 会与 I6 矛盾。冻结 positive-cut-class C13 的 Poincaré–Lefschetz exact sequence 遂使其 relative boundary 非零。没有用“compact cycle 周期非零”的猜测，也没有把一个任意 rational horizontal splitting 当 compact image。

特别是：固定 \(R_4^+\) 后，real averaging 或实际 \(\Gamma/8\) 修正只能加入 compact image，不能消去 I6。对 **open representative** 改用下面 counterterm 是不同操作。

## 3. Counterterm 的 rational lattice、local regularity 与 canonical trace

\[
 \beta_0=\frac a2\,d\log v_1d\log v_2d\log v_3,\qquad
 [\beta_0]/a^4=\frac12
 \prod_{j=1}^3[d\log v_j/a].
 \tag{I7}
\]
各 normalized log form 是 unit 的 integral degree-one class，所以 I7 确在 rational **open** lattice。normal \(v_1\) winding 为2，给同一 period \(a^4\)。若它 compact 则会违反 I3，因此它也确切非compact。

减去 \(\beta_0\) 后 I4 的 \(\log(1-s)/s\) holomorphic，因此整 disk 上无 normal pole。不是只消去一个 period 而遗漏 local current residue；这里没有切割 support 的其余项。

在 motivic 层将 \(v_0\) 换为 \(-v_0\) 的差含 \(\{-1\}\)，它是2-torsion，rational symbol 不变。principal unit \(-v_0\) 的负实 cut 正是原 \(v_0\) 的正实 cut，其 log 为 \(L_0^+-a/2\)；\(d\log\) 与 cut coorientation 不变。KLM product 于是给普通 third component 恰减 \(\beta_0\)。这是 rational equality，不能声称 integral symbol 完全相同。

raw type pairing 为0，因为 \(\beta_0\wedge\omega\) 是 complex-threefold 上 \((6,0)\) form。canonical relative trace 也为0，但需要额外 filtered argument：
\[
 [\beta_0]\in F^3H^3(U),\quad
 [(\omega,0)]\in F^3H_c^3(U),\quad
 F^3\cup F^3\subset F^6H_c^6(U)=0.
 \tag{I8}
\]
log forms 在 toric modification 上仍为 monomial log forms 加 regular forms，故其绝对 class 的 \(F^3\) 范围成立。holomorphic compact 3-form 在每个 boundary surface 及其更低 dimensional intersections 上 restriction 为0，因此 \((\omega,0)\) 是 relative filtered-cone 的 \(F^3\) cocycle。relative filtered wedge 与 cup 相容；smooth connected complex-threefold 的 \(H_c^6\) 为 \(\mathbf Q(-3)\)，其 \(F^6=0\)。

实际原文 Deligne HodgeIII PDF37 的 8.2.10/11 给 absolute cup 的 MHS 兼容，PDF40–41 的 8.3.8/9 给 relative MHS 及 bifiltered cone。I8 使用 relative cone 的 filtered wedge，而非把 absolute cup 陈述直接改名成 relative theorem。任意非-Hodge rational horizontal splitting 不满足 I8 的前提，其 support trace 未由本论证判零。

## 4. All-unit centering、sheet sign 和逐 sheet 收敛

N11 每个 unit 改成 \(-v_j\)。first/second components 不变，对数同时减 \(a/2\)，exact KLM product 产生作者所写的 centered third component。其 rational open Deligne class 与原 symbol 相同；在 \(0<x<1\) 上 four-positive-cut intersection 为空，因此 fibrewise current closed。

实际全文回读冻结 [positive-cut period comparison](cdt_odd_R0_positive_cut_period_comparison_20261006.md)。normal-first triple cut 的 permutation 为 \([1,3,5,0,2,4]\)，六次 inversion 给+。两个 sheet 的 free-coordinate orientation 均相同，LEFT residue 给
\[
 \omega_+=\frac{i\,d\log^3v}{2\sqrt{\Phi_{012}-64x}},
 \qquad
 \omega_-=-\frac{i\,d\log^3v}{2\sqrt{\Phi_{012}-64x}}.
 \tag{I9}
\]
前三项仍含 holomorphic \(d\log\)，与 \(\omega\) wedge 为0。最后一项的 centered constant correction 是同一 triple-cut orientation 下的 \((a^4/2)\int\omega\)，两 sheet I9 精确相消。

这一步亦可直接独立核绝对收敛。每张 constant-correction sheet 的 density 为 \(d\log^3v/(2\sqrt{\Phi_{012}-64x})\)，故两张总 absolute norm 不超过
\[
 \frac1{\sqrt{1-x}}\int_{(0,\infty)^3}
 \frac{d\log^3v}{\sqrt{\Phi_{012}}}
 =\frac{\pi^3}{\sqrt{1-x}}.
 \tag{I10}
\]
因此不是在两个各自发散的 sheet 上形式相消。原 logarithm-weighted sheets 的 absolute norm 已由冻结稿核为至多 \(\pi^4/\sqrt{1-x}\)。N12 的 raw identity
\[
 \int R_4^c\wedge\omega=\int R_4^+\wedge\omega=-16a^3W
 \tag{I11}
\]
通过，且未改变 Tate normalization。

## 5. 结论范围、排版和实际来源

此局部非compact障碍已经是正定理；centered current 的某个 chosen compact extension若被全corner证明建立，I11 与其 scalar comparison 可以进一步接合。**本审阅没有实际阅读或审查那个另稿，因此不把它作为已证输入。** 同理，本例原始 \(R_4^+\) 的 noncompact Tate boundary 与任意 compact real-compatible lift 剩余一维选择自由是两件不同的事，均不能误当成已选定 centered marking 的未解比较。

初读 fb91af… 发现两处纯 TeX 排版残留：N9 的 frac12 实际保存为 TAB+“frac12”；§5 两 sheet display 的分子仍有一个 comma。作者在尚未正式冻结的本轮 NEW 稿中纠正它们并登记修订，数学不变。独审随后实际全文回读终稿 00d1cb…，N9 与两 sheet 公式均正确。审阅者没有修改被审稿，也没有修改任何旧冻结文件。

本轮实际来源：

* 被审稿：实际全文读 fb91af… 初稿并再次实际全文读 00d1cb… 终稿，验证最终 hash。
* Toric completion：实际读 §§1–5、§6 起始；SHA abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0。
* Positive-cut comparison：实际全文读；SHA fb44cacdd85484887a51c90c7547432eff5ceb0516b356a3fbc26a5f97f65dc8。
* Compact positive-cut class：本轮在此前 real proof 任务实际全文读；SHA 094aa342bb462a080c99b525110e8b1738acb58897aa2e4fbe9aa991a521c5d7。
* [Deligne HodgeIII primary](../literature/deligne1974_hodge_III_primary_20261006.pdf)：本独审实际 PDF37–41 全部文本；SHA d78d4f46742916cd669279e7db365e4db6a43f38d2dcdec6862c6d27d07216b3。
* [KLM published primary](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)：本独审实际 PDF7–8、12；unit current、Prop4.2 product、derived/ring naturality；SHA 8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9。

Python 仅为实际 PDF text extraction。无新增 PDF、无参数搜索、无 verifier、无数学 producer 执行/import/rerun。没有新数值无理性、线性无关性、整格饱和或Lean结论。
