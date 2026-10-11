# 四变量 family symbol 的 KLM current 接口：原件、符号与拉回

日期：2026-10-06。NEW source/read note；不改已冻结 toric completion/uniqueness 稿，不执行或 import 任何旧或 peer 数学 producer。只核 current 接口，不证明旧相对积分链与 compact regulator 的具体 marking，也不宣称数值无理性或线性无关性定理。

## 1. 实际文献与阅读范围

本轮正常验证 TLS 下载三份 primary PDF，没有跳过证书验证。

| 原件 | 本地新文件 | 实际核读及视觉核验 |
|---|---|---|
| Kerr–Lewis–Müller-Stach, The Abel–Jacobi map for higher Chow groups, Compositio Math. 142 (2006), 374–396 | literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf | PDF1–14、16–21；主要 premises 为 PDF9–13、17；视觉核 PDF11、12、13、17 |
| Li, Integral Regulators for Higher Chow Complexes, SIGMA 14 (2018), 118 | literature/li2018_integral_regulators_higher_chow_published_20261006.pdf | 实际全文 PDF1–12；视觉核 PDF2 |
| Kerr–Lewis, The Abel-Jacobi Map for Higher Chow Groups, II, fixed arXiv math/0611333v1 | literature/kerr_lewis2007_abel_jacobi_II_arxiv_v1_20261006.pdf | PDF1–6、50–57、59–61；主要 premises 为 PDF50–51、53–57、59；视觉核 PDF54、59 |

KLII 本地文件是 2006-11-11 的 fixed arXiv v1，文件名中的 2007 指正式发表年；其 PDF 页码等于自身 printed 页码，不能当成 Inventiones printed 页码。KLM 是正式 published PDF，printed 页码 = PDF 页码 +373。

Primary URLs：

- [KLM published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/96E7B429B8B0E96C08890BE3BAC41724/S0010437X05001867a.pdf/abeljacobi_map_for_higher_chow_groups.pdf)。
- [Li published PDF](https://sigma-journal.com/2018/118/sigma18-118.pdf)。
- [KLII fixed arXiv v1](https://arxiv.org/pdf/math/0611333v1)。

三份 SHA、bytes、PDF pages 与 premise 出处另记 NEW receipt literature/manifest_cdt_odd_R0_klm_current_interface_20261006.json。

## 2. Exact exterior identity 与 normalization

采用 KLM §5 的 convention，而不是其 §2 简介的相反 Bloch boundary：

\[
 \partial_B=\sum_{i=1}^n(-1)^{i-1}
       \bigl((\rho_i^\infty)^*-(\rho_i^0)^*\bigr).
 \tag{2.1}
\]

KLM PDF10 / printed383 明确 (2.1)。§5.1（PDF9 / printed382）把 principal log 的 imaginary part 取在 \((-\pi,\pi)\)，并取 \(T_f=f^{-1}(\mathbb R^-)\) 的方向使 \(\partial T_f=(f)_0-(f)_\infty\)。同页有 \(d[\log f]=d\log f-2\pi i\,\delta_{T_f}\)。

对 real-admissible precycle \(Z\in Z^p_{\mathbb R}(X,n)\)，KLM PDF11 / printed384 equation (5.5) 精确给出

\[
 \partial T_Z=T_{\partial_BZ},\qquad
 d[\Omega_Z]=2\pi i\,\Omega_{\partial_BZ},\qquad
 d[R_Z]=\Omega_Z-(2\pi i)^n\delta_{T_Z}
               -2\pi i\,R_{\partial_BZ}.
 \tag{2.2}
\]

该式没有 \(n\le3\) 限制。它是任意 cube degree 的 current identity，不能把仅适用于某类 toric family 的 Doran–Kerr Lemma4.1 的符号直接搬来替代。

KLM PDF12 / printed385 §5.5 的 cohomological normalization 是

\[
 Z\longmapsto(-2\pi i)^{p-n}
     \bigl((2\pi i)^nT_Z,\Omega_Z,R_Z\bigr).
 \tag{2.3}
\]

原文先以 Deligne homology 写出额外的 \((2\pi i)^{-m}\)；经过 Poincaré duality 后该 ambient-dimension 因子消失，PDF13 / printed386 再次明确。Li PDF7 §5.2 也直接写出 (2.3)。因此 \(p=n=4\) 时外因子为1；不能因为 total space 维数4而 fibre 维数3就另乘一个 \(2\pi i\)。

KLM PDF12 明确 \(\Omega_Z=0\) if \(p<n\)；其 geometric 类型为 \((p,p-n)\)。在 \(p=n=4\) 的 smooth 四维 \(Y\) 上，closed \(\Omega_C\) 是 \((4,0)\)-current，因 \(\bar\partial\Omega_C=0\) 而实际是 holomorphic 4-form。这是分布版 Dolbeault lemma 的直接结果。

## 3. 当前 coordinate graph 的形式

冻结 geometry 输入为

\[
 Y^*=U^4,\quad U=\mathbb P^1\setminus\{0,\infty,-1\},\quad
 \xi=\{v_0,v_1,v_2,v_3\},\quad
 \phi=\prod_{j=0}^3(1+v_j)^2/v_j,\quad\lambda=256x.
\]

本轮实际只读冻结 research/cdt_odd_R0_toric_completion_20261006.md 前190行，核实这些定义及 smooth/proper family 输入，不冒充对全文的新独审。

graph 位于 \(Y^*\times(\mathbb P^1\setminus\{1\})^4\)。所有 \(v_j\) 都是 unit，所以没有 cubical \(0,\infty\) face boundary。去掉 \(v_j=1\) 的 graph 部分不造成 current 的额外 residue；\(d\log v_j\) 本来在那里光滑，graph pushforward 给出

\[
 \Omega_\xi=\Omega_4
       :=d\log v_0\wedge d\log v_1\wedge d\log v_2\wedge d\log v_3.
 \tag{3.1}
\]

四个 coordinate 的 real-cut intersections 独立，因而 graph 在 total \(U^4\) 上满足 good real position。KLM PDF10 / printed383 的右侧 delta convention 在 \(n=4\) 给

\[
\begin{aligned}
 R_\xi={}&\log v_0\,d\log v_1\wedge d\log v_2\wedge d\log v_3\\
 &-2\pi i\,\log v_1\,d\log v_2\wedge d\log v_3\,\delta_{T_{v_0}}\\
 &+(-2\pi i)^2\log v_2\,d\log v_3\,\delta_{T_{v_0}\cap T_{v_1}}\\
 &+(-2\pi i)^3\log v_3\,\delta_{T_{v_0}\cap T_{v_1}\cap T_{v_2}}.
\end{aligned}
 \tag{3.2}
\]

对 arbitrary \(n\)，delta 放在微分形式左侧还是右侧会改变表面符号；Li PDF7 §5.2 用左侧 delta 的 \((-2\pi i)^{k-1}\) 形式。不能混用符号与 wedge 次序。式 (3.2) 在 \(n=4\) 的四项无此冲突。

若 \(\Xi\) 的 closed representative 为 \(C\)，而 \(C|_{Y^*}=\xi+\partial_B M\)（\(M\in Z^4(Y^*,5)_{\mathbb Q}\)），则 \(\Omega_M=0\)。利用 (2.2) 第二式得到 exact current equality

\[
 \Omega_C|_{Y^*}=\Omega_\xi. \tag{3.3}
\]

所以真实 Chow completion 的 holomorphic 4-form 由 coordinate symbol 强制确定；没有用任意 PF particular solution 定义 regulator。

## 4. Rational moving 与任意给定 smooth fibre

KLM PDF11 的早期 moving 表述不能当成 integral quasi-isomorphism 的可靠来源。Li PDF2明确：已完成的 Kerr–Lewis proof 经过 rational \(K\)-theory 与 Kleiman transversality，只保证 \(\mathbb Q\)-quasi-isomorphism；Li PDF4 Theorem2.4 在 smooth quasiprojective setting 记下该结论。当前 \(CH^4(-,4)_{\mathbb Q}\) 只需 rational statement。

给定-subvariety版本来自 KLII：

- PDF53 Definition8.12 定义 \(Z^p_{\mathbb R}(X,n)_V\)，要求与固定 smooth \(V\) 及所有 cubical/real faces properly intersect。
- PDF54 Lemma8.14 说明四个 inclusions 均为 quasi-isomorphisms；PDF4已约定 cycle groups 全部 tensor \(\mathbb Q\)。
- 同页 Corollary8.15 与 Lemma8.16 给 localization、open variety 及 prescribed \(V\) 兼容版本。后者要求 \(V\cap D\) proper 且避开 \(D\) 的 codimension2 skeleton；若 \(V\cap D=\varnothing\)，条件自动满足。
- PDF55–57 proof 使用 iterated doubles、\(K\)-theory、realification、Kleiman transversality 与 rational norm，不能读作 integral moving proof。
- PDF59 §8.3明确 \(V\)-intersection higher-Chow chains 的 KLM triple commutes with pullback。PDF50–51 给 normal intersection currents；Lemma8.7 给 filtered quasi-isomorphisms。

应用时将 total space 放在 good projective compactification \(X\setminus D\) 中。当前可取 toroidal \(\widetilde P\)，vertical boundary \(D=f^{-1}(\{0,\infty\})_{\rm red}\) 是 SNC。每个已给定 smooth proper fibre \(V=Y_{\lambda_0}\)，\(\lambda_0\ne0,256,\infty\)，与 \(D\) 不交。于是可在 rational equivalence class 内重新选择 closed \(C_V\)，使 currents 能在这个指定 fibre 上拉回并给出 \(AJ(\Xi|_V)\)。

此结论允许每个给定 fibre 的代表选择；不要求原始 raw current 自动横截所有 fibres。形式限制须经 moving 或 compatible regularization 解释。

## 5. Boundary change 与 membrane 的精确抵消

在 local proper smooth family neighbourhood 中，若已取 rational BM membrane \(\zeta\) with \(\partial\zeta=T_C\)，则 \(p=n=4\) 的 convention 给 \(d\delta_\zeta=\delta_{T_C}\)。所以

\[
 R'_C=R_C+(2\pi i)^4\delta_\zeta,\qquad dR'_C=\Omega_C.
 \tag{5.1}
\]

这是 KLM PDF13 / printed386 的 even-\(n\) correction；BM membrane existence 需由项目 local proof 负责，不能免费由该页 projective theorem 推出。

对 rational real-admissible change \(C'=C+\partial_B M\)，\(M\in Z^4(Y,5)_{\mathbb Q}\)，由 \(\Omega_M=0\) 与 (2.2) 得

\[
 R_{\partial_BM}
       =-\frac1{2\pi i}dR_M-(2\pi i)^4\delta_{T_M},
       \qquad T_{\partial_BM}=\partial T_M.
 \tag{5.2}
\]

选 \(\zeta'=\zeta+T_M\)，即得到

\[
 R'_{C'}-R'_C=-\frac1{2\pi i}dR_M. \tag{5.3}
\]

boundary change 与对应 membrane adjustment 后是 exact-current change，满足 pullback 条件时给同一 fibre cohomology class。若两端已在 real-admissible subcomplex 同调等价，rational moving quasi-isomorphism 的 injectivity 允许在该 subcomplex 找 \(M\)。这是 representative independence 的精确接口。

## 6. Derivative sign 的接口与界限

本 note 未代替主稿证明 local BM primitive existence、smoothing 与 compact fibre regulator comparison。一旦主稿正确把 (5.1) primitive 解释为 local fibre AJ lifts，Cartan identity 给正号：

\[
 \nabla_{\partial_\lambda}[R'_C|_{Y_\lambda}]
       =[\,\iota_{\widetilde{\partial_\lambda}}\Omega_C|_{Y_\lambda}\,].
 \tag{6.1}
\]

在 old geometry 固定的 left residue convention
\[
 \frac{\Omega_4}{\phi-\lambda}
       =\frac{d(\phi-\lambda)}{\phi-\lambda}\wedge\rho_\lambda
         +\text{regular term}
\]
下，\(\Omega_4=d\phi\wedge\rho_\lambda\) 在 fibre 上，故 (6.1) 为 \(+\rho_\lambda\)。若
\(\Omega_x^{\rm old}=16\Omega_4/(\phi-256x)\) 且
\(\omega_x=\sqrt{x}\operatorname{Res}\Omega_x^{\rm old}\)，conversion 为
\[
 \nabla_{\theta_x}AJ=256x\,\rho_\lambda=16\sqrt{x}\,\omega_x.
 \tag{6.2}
\]

(6.1)–(6.2) 是标明前提的 interface deduction。不识别 scalar solution 的 integration constant，不证明 conifold value 为 \(R_0-M_0\)，不提供 compact \(P_4\) projector、integral saturation、closed-chain marking 或数值独立。
