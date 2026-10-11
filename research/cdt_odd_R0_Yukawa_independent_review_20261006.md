# R₀ Yukawa / scalar interface 的实际全文独立审阅

日期：2026-10-06。审阅者：toric_chow_completion。本文是 NEW 纯证明审阅；旧数学稿、同行 PY/JSON/manifest 均只读，没有执行、导入或修改任何 mathematical producer。本文未重新构建 mirror 的全部 resolution，也没有把有理投影解释为整格饱和定理。

## 1. 被审对象、冻结版本与结论

实际全文审阅并最终回读：

* [Yukawa 主稿](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)，SHA256：172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15。
* [作者来源 receipt](../literature/manifest_cdt_odd_R0_Yukawa_scalar_interface_20261006.json)，SHA256：ae690668ee491d2f3b34f07245d3ec5647a4bd8881aa1f5a3109e83b5d08e121。

独立手核主稿 §§1–8、Y1–Y33。结论：**通过本文明确的范围**。核心正结果是实际 compact rank-four rational orthogonal projector、固定 residue/cup/Tate 规范下的
\[
 \kappa_{\rm raw}=-\frac{(2\pi i)^3}{16},\qquad
 \kappa_{\rm dR}=-\frac1{16},
\]
以及 cohomological derivative 到 scalar PF source 的正确转换。此结论使用已冻结实际 toric/mirror 几何和 half-four 的 connected \(\mathrm{Sp}_4\) 输入；其中 mirror full compact PF 的依据已实际读 primary，不是从一个 torus period 推出的猜测。

审阅不证明 actual scalar current 与 \(W\) 相等，不证明 integral projector、完整 trace/saturation 或新的数值无理性。把另一份已独审 regulator 定理 R12 的 \(c=+16\) 代入 Y5 后，只得到
\[
 P\!\left\{\nu_{\rm raw}+16(2\pi i)^3W\right\}=0,
\]
不能把括号内的实际 homogeneous period 置零。

## 2. 实际读取的冻结输入与 primary

本轮实际全文读 [Kummer interface](cdt_odd_R0_kummer_period_interface_20261006.md)，SHA256：803b3eced9825fe5f40005728430188e36c4a8cd123d41223972cceb23c2e172；其 §6.1 给整个 conifold log branch 的 rank-one 结果和 \(y_0\) 的首系数 \(1/\pi^2\)。不是只读取首项摘要。

本轮实际全文读 [spin 主稿](cdt_odd_classical_spin_pullback_20261006.md)，SHA256：a82ac7c4dfc6b3087ea25ad23be8b87fd5330683784402c65839349acb2b229e；其 §3 固定 connected \(\mathrm{Sp}_4\)、finite-cover 绝对不可约及 nonzero rank-one conifold monodromy。本审阅只读并使用此冻结数学输入，没有执行其旧 verifier，也不扩大该 verifier 的检查范围。

实际 mirror/residue 稿与本审阅者的 toric completion 稿已在本轮前序任务全文读审；分别采用被冻结的 SHA256 43009e569bba25b6f819f0e5f1de0b96fa2db57e1a73817e8b087d294a059912、abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0。这里只调用其实际 degree64 quotient、raw residue scale、compact torus marking、boundary strata smoothness 和唯一 interior node；没有修改两稿。

独立实际读 primary 的范围如下，所有页号均为 PDF 页号：

1. [BKΣZ 原件](../literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf)，79页，SHA256：f124aab462ae953eff9a2c9df28cff63e1b63adad792a572a1c608226fdfac83。本次实际逐整页读 6、7、10、12、14、15、16、17、19。PDF6 Eq2.1 和 PDF7 Table1 核 native PF、\(1/\mu=256\)；PDF12/16/19 核四 quadrics、quotient/resolution、compact mirror；PDF19 Eq2.40 核 canonical form 的 \((2\psi)^4\) scale。没有宣称读全文79页。
2. [Movasati author 原件](../literature/movasati2021_course_hodge_theory_author_20261006.pdf)，380页，SHA256：69830ec409ccd1172f1ec348dad2f6bed59fe4f18342c1a4fab37b0659c85182。本次实际逐整页读 82、93、94、95、131、132、133，并实际视觉读作者已保存的 PDF95 图。PDF93 local quadratic model 的 total dimension 为 \(n\)，vanishing sphere 是 \(S^{n-1}\)；PDF94–95 的 positive anticlockwise PL sign 是 \((-1)^{n(n+1)/2}\)；PDF132 Eq8.4 的 middle pairing 为 \((2\pi i)^{-m}\int\omega_1\wedge\omega_2\)。没有宣称读全文380页。
3. [DK published 原件](../literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf)，204页，SHA256：1911f2f4a805e1a3d218ca247665209f3fe9505aa9bc0ae949b1163d7271ede4。本轮前序 regulator 任务已实际逐整页读 PDF57–83，因而涵盖本次 Y32 所需 PDF73–74 的 monic PF/Yukawa 区分、以及 PDF79–80 Lemma4.1 的 \(\ell=2,3\) 范围。此次不重新下载、不宣称该 lemma 已覆盖非regular \(\ell=4\)。

Movasati PDF95 后文把 \(H_{n-1}\) pairing 称为 \((-1)^n\)-symmetric，和 middle-intersection 的实际 parity 不一致。本审阅不使用那一句；定理公式的 \(n(n+1)/2\)、\(H_{n-1}\) 及 anticlockwise 范围在原页清楚。本文直接采用 Y19 的有序 Poincaré-dual cup 约定，\(H^3\) pairing 的 skew symmetry 由 degree3 wedge 决定。

没有在此次审阅新增 PDF。作者来源 receipt 的 download/TLS 记录只作为归档元数据；我们实际读取了上述本地固定原件，不把 receipt 的作者阅读声明代替审阅者自己的阅读。

## 3. Native PF gauge 和真正 compact cohomological annihilation

BK 的 native parameter \(z=(2\psi)^{-8}\) 和 Table1 \(1/\mu=256\) 给 normalized \(q=256z=\psi^{-8}=1/x\)。所以 native operator 正是
\[
 P_q=\theta_q^4-q(\theta_q+\tfrac12)^4.
\]
Eq2.40 的四个 tube factors \((2\pi i)^{-4}\) 与四次 residue 相消，不额外留一个 Tate factor。按 ambient orientation 的固定差 \(\epsilon=\pm1\)，
\[
 \Omega_{\rm BK}=16\epsilon\psi^4\omega_M,\qquad
 \omega=4\epsilon x^{-1/2}\Omega_{\rm BK}.
\]
这一 scale 使用实际 \(p^*\omega=64\omega_M\)，不是把 degree64 map 当成 degree-one map。

独立共轭计算：
\[
 \theta_x(x^{-1/2}h(1/x))
 =x^{-1/2}(-\theta_q-\tfrac12)h(q),
\]
继而
\[
 P_x[x^{-1/2}h(1/x)]
 =-x^{1/2}(P_qh)(1/x).
\]
所有 native compact periods 受 primary 的 full PF 控制；全 period 非退化比较因此给 mirror \(H^3\) 中的 cohomological annihilation。不能仅凭一个 \(\Gamma\) period 这样推论。

最终版 Y8a 在共同 resolution \(Z\) 上先以 dense-open residue 比较获得两边 holomorphic three-form 的全局相等，再将 native compact PF 拉回。由于 \(a_*a^*=1\)，\(a^*\) 单射，故真正 \(P_x\omega=0\) 在整个 compact \(H^3(X)\) 中。此论证完整，不需要假设 \(X\) 的额外 cycles 都来自 mirror。

## 4. Degree-one graph projector 与 descent

共同 graph resolution 的 \(a,b\) 均 degree one，proper projection formula 给 \(a_*a^*=b_*b^*=1\)，且拉回对 middle cup 是 isometry。于是 \(a^*a_*\) 是 \(a^*H^3(X)\) 上的 orthogonal projector。

对
\[
 T=(1-a^*a_*)b^*
\]
而言，实际 form equality 使它杀掉 mirror canonical Hodge line。图对应是 horizontal，因此也杀掉 canonical section 的全部 covariant derivatives。Half-four 系统 rank4 且 finite cover 保持 connected \(\mathrm{Sp}_4\)，canonical nonzero section 的 cyclic module不可能是 proper submodule；其 derivative span 必为整个 mirror \(H^3\)。所以 \(T=0\)，并且
\[
 i^*i=b_*a^*a_*b^*=1,\qquad
 \Pi=ii^*=a_*b^*b_*a^*.
\]
这是 actual compact rational orthogonal projector。

其 image 是含 actual holomorphic form 的唯一 rank4 cyclic span。更换共同 resolution 或作 cover deck transformation 后，该 span 不变；nondegenerate pairing 的 orthogonal projector 唯一，因而在有理 local system 中下降。此论证下降的是有理 cohomological projector；并未断言有限覆盖上任一所选 graph 本身作为 cycle 已下降，更未证明 integral matrix、saturation 或 projector 无分母。

## 5. Cyclic cup matrix、dual sign 和 concomitant

独立从 Hodge zeros 与 flatness 得
\[
 Q(E_1,E_2)=-Y,\quad Q(E_1,E_3)=-\theta Y,\quad
 2\theta Y=-p_3Y,
\]
因此
\[
 Y=\frac{\kappa}{1-x},\qquad
 Q(E_2,E_3)
 =-\theta^2Y-p_3\theta Y-p_2Y
 =\frac{\kappa x}{2(1-x)^2}.
\]
主稿 Y13 的 inverse 已按四行逐项手乘核验；其 Pfaffian \(-Y^2\) 与 nondegeneracy 一致。

若 \(\alpha=\sum a_jE_j\)，则 \(v_j=Q(\alpha,E_j)\) 的列向量是 \(-Ja\)，故 \(\Pi\alpha=-\sum(J^{-1}v)_jE_j\)。对两个 Poincaré-dual coordinate columns \(a,b\)，period columns \(h=-Ja,\ k=-Jb\)，于是
\[
 h^TJ^{-1}k=-a^TJb.
\]
因此 Y20 的 contravariant negative sign 必须保留；它与 Y19 的 ordered cup/intersection 约定相容。

独立用 Leibniz 展开 Y16：混合项全部相消，留下
\[
\begin{aligned}
 \theta\mathcal C_0(h,k)={}&(1-x)(\theta^4h\,k-h\theta^4k)\\
 &+2x(h\theta^3k-\theta^3h\,k)
 +\tfrac32x(h\theta^2k-\theta^2h\,k)
 +\tfrac x2(h\theta k-\theta h\,k),
\end{aligned}
\]
恰为 \((Ph)k-h(Pk)\)。这是全函数恒等式，不是几个局部系数的检验。Y15 对 measure \(dx/x\) 的 self-adjoint 计算也正确；monic \(P/(1-x)\) 没有被误作相同 adjoint。

## 6. Actual node、total dimension 和 PL intersection

在光滑四维 total space \(Y\) 上，唯一 critical point 是 \(u=0,x=1\)，boundary 各 surviving strata 上的 map smooth。局部
\[
 F_x=x(f-\tau),\qquad f=\sum u_j^2+O(|u|^4),\qquad
 \tau=(x-1)/x.
\]
Real Morse coordinates 在0的 Jacobian 可取 \(+1\)。左 residue 在 outward oriented \(S^3_{\sqrt\tau}\) 上为 area form 除以 \(2\sqrt\tau\)。乘回 \(\sqrt{x}/x\)，实际首项是
\[
 g(x)=\pi^2(x-1)+O((x-1)^2).
\]
因此 \(g=a t+O(t^2)\), \(t=1-x,\ a=-\pi^2\)，没有漏掉 radius、residue 的 \(1/2\) 或 \(\sqrt{x}/x\)。

Movasati 定理这里使用 total complex dimension \(n=4\)，不是 fibre dimension3；\((-1)^{n(n+1)/2}=+1\)，且 positive anticlockwise continuation 使 \(\log t\) 增加 \(2\pi i\)。冻结 actual torus period
\[
 h=-4i\pi^3y_0,\qquad
 h=H+c\,t\log t+\cdots,\quad c=-4i\pi
\]
给 jump \(8\pi^2t+\cdots=-8g\)。因此实际 PL intersection 为 \(\Gamma\cdot\delta=-8\)。

Proper family 只有此一个 ordinary quadratic critical point，故 \(T-1\) 的 image 是 vanishing line；compact rank4 sector 的 conifold transvection 非零。Horizontal \(\Pi\) 使 \(\operatorname{PD}\delta\) 属于该 sector，从而 projected cup 仍给 \(-8\)。此处不假设 \(\Gamma\) 没有其他 compact sector，也不把 \(\delta\) 当成未经标定的 primitive lattice generator。

## 7. Regular cancellation 与 \(\kappa\) 的独立决定

独立把 \(\theta=-(1-t)\partial_t\) 展开得到 Y28 全部五个 coefficient。设
\[
 g=at+bt^2+\cdots,\qquad
 h=H+(c/a)g\log t.
\]
为核 Y29，仅需 \(P(g\log t)\) 的负次幂：
\[
 (g\log t)'''=-a/t^2+2b/t+\cdots,\qquad
 (g\log t)''''=2a/t^3-2b/t^2+\cdots.
\]
四阶 coefficient \(t-4t^2+\cdots\)、三阶 \(2-14t+\cdots\)、二阶 \(-15/2+\cdots\) 给 \(t^{-1}\) 的总 coefficient
\[
 (-2b-8a)+(4b+14a)-15a/2=2b-3a/2.
\]
Analytic \(H\) 不可能产生负次幂，故 \(b=3a/4\)。

在 concomitant 中，\(H\) 的可存活 limit 仅为
\[
 H(0)\{-a/2+(2b-a)\}=H(0)(2b-3a/2)=0.
\]
这说明不能只计算 log 项后忽略 regular part；实际 cancellation 确实成立。

对 log 项，使用
\[
 \theta\log t=-1/t+1,\quad
 \theta^2\log t=-1/t^2+1/t,\quad
 \theta^3\log t=-2/t^3+3/t^2-1/t
\]
逐项代回 Y16，四个 limits 为 \(0,-ca,+ca,+ca\)。所以
\[
 \mathcal C_0(h,g)=ca=4i\pi^3.
\]
与 projected PD/intersection negative sign 联合，\(\mathcal C_0/\kappa_{\rm raw}=8\)，给
\[
 \kappa_{\rm raw}=i\pi^3/2
 =-(2\pi i)^3/16,\qquad
 \kappa_{\rm dR}=-1/16.
\]
此推导不使用待比较的 raw KLM period。主稿的 \(\kappa\) 不是从 desired forcing 倒推，也不是直接套 BK Table1 的另一规范常数。

## 8. Scalarization 与本审阅允许的合并结论

若 actual compact lift 满足 \(\nabla_\theta r=c\sqrt{x}\omega\)，Hodge zeros 使前三阶 scalar derivatives 分别为 \(Q(r,E_j)\)。第四阶才新增 \(c\sqrt{x}Q(E_0,E_3)\)。所以
\[
 \frac{P}{1-x}\nu=c\sqrt{x}Y,\qquad
 P\nu=\kappa c\sqrt{x}.
\]
主稿 Y32 正确保留 actual leading factor \(1-x\)；没有错误地留下 \(1/(1-x)\) conifold source。

本审阅者另著、已由 root 独立全文读审的 [compact derivative 稿](cdt_odd_R0_regulator_derivative_20261006.md)，冻结 SHA256：5a3ba4ed679a5565375efdb0b9c39e4a69338e72bcce5938b5a34356d816e091，R12 已给 actual compact \(c=+16\)。本次是独立审 Yukawa，不把审阅者自己的 derivative 稿称为再次独立审过。将该已单独审阅定理与此次通过的 Y32 合并，得到
\[
 P\nu_{\rm raw}=-(2\pi i)^3\sqrt{x},\qquad
 P\nu_{\rm dR}=-\sqrt{x},\qquad
 P\widehat\nu=\sqrt{x}/16,\quad
 \widehat\nu=-\nu_{\rm dR}/16.
\]
仍只推出 \(\widehat\nu-W\in\ker P\)。Actual cube/cut marking、graph closure、bounding membrane、flat rational Tate lift 及 conifold transport 的匹配没有由此被证明。

## 9. 审阅状态与执行记录

最终状态：Y1–Y33 的数学推导在已注明冻结/primary 几何输入下通过；尤其 final Y8a 的 compact cohomological PF、新 degree-one projector、PD dual sign、total-dimension PL、node 首项、regular cancellation 和 raw/dR 常数均已独立实际核验。

使用 PowerShell 只读文件，Python fitz 仅抽取 primary PDF 页和 hashlib 元数据；PDF95 用 image viewer 实际视觉读。一次只读 PDF 输出遇到终端 GBK 编码错误，改为 UTF-8 后完成，未产生数学文件或改变输入。未运行 symbolic algebra、有限 math verifier、旧/同行 producer、PSLQ 或 Lean；所以本文不将任何有限检查冒充上述全尺度证明。
