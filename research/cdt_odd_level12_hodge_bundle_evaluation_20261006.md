# D12 Hodge 束、向量评价与完整斜率账本的限定接口

日期：2026-10-06。新纯 MD 证明及 primary 文献记录。冻结的数学 producer 一律只读，未执行/import；没有参数、素数或 word 扫描。本稿给可直接证明的归约及指标比较引理，并指出真正随次数变化的束接口仍缺什么。**没有获得新的奇 ζ/L 数值结论或新的 CDT 成本折扣。**

## 1. 原始文献已经给的向量斜率公式

[Bost 2001 原件](../literature/bost2001_algebraic_leaves_numdam_20261006.pdf)，印刷 pp.199–200 / PDF39–40，定义 (4.10) 及 Proposition 4.6/(4.14)，直接处理 Hermitian 向量束，而不只标量。设 \(E_D\) 为实际 \(O_K\) 格，\(E_D^n\) 为一个最终为0的饱和 filtration，实际 graded map

\[
\eta_{D,n}:E_{D,K}^n\longrightarrow G_{D,n,K},\qquad
\ker\eta_{D,n}=E_{D,K}^{n+1}.
\tag{H1}
\]

给每个 \(G_{D,n}\) 实际整格和正定有限 Hermitian 范数。令
\(a_{D,n}=\dim_K E_{D,K}^n/E_{D,K}^{n+1}\)，则

\[
\widehat{\deg}_n\overline E_D
\le\sum_n a_{D,n}
\left\{\widehat\mu_{\max}(\overline G_{D,n})
+h(\overline E_D^n,\overline G_{D,n},\eta_{D,n})\right\}.
\tag{H2}
\]

这里 \(\widehat{\deg}_n=\widehat{\deg}/[K:\mathbf Q]\)，而 \(h\) 是所有有限地方及复 embedding 的 operator log-norm 的归一化和。**整格、源度、graded 秩、目标斜率、finite heights 和 archimedean heights 已全部在式中。**用 bundle 替换 scalar 不会自动删掉任一项。

源与 graded lattices 必须是同一个 actual map 的 lattices；一个 \(GL_4(\mathbf Z)\) 周期表示不是 (H1) 的 Taylor evaluation lattice。formal 线性系统的秩也不是 \(a_{D,n}\)。

Bost 原文印刷 p.203 / PDF43 的实际 germ 评价为
\(G_{D,n}=\operatorname{Sym}^n(T_P\widehat V)^*\otimes L_P^D\)，其公式 (4.18) 正是 (H2)。若改成 rank \(r\) 的 bundle section 评价，合法的目标是再 tensor 实际有限 fiber \(E_P\)；对一维 germ，每阶 \(a_{D,n}\le r\)，而 \(\sum_n a_{D,n}=\operatorname{rank}E_D\)。这仅在**整 tuple 的消失阶**定义 filtration 时成立；若评价是与一个真实水平解配对后的 scalar，graded rank 至多1，必须按该配对重新定义 filtration，不能把两种计数混用。

## 2. 可直接使用的 scalar-component 归约引理

设 \(f_1,\ldots,f_m\in\mathbf Q[[t]]^r\) 是 \(\mathbf Q(t)\)-线性无关的实际向量 germs。令

\[
W=\operatorname{span}_{\mathbf Q(t)}\{f_{i,j}:1\le i\le m,1\le j\le r\},
\qquad M=\dim_{\mathbf Q(t)}W.
\tag{H3}
\]

若 \(M\) 有限，则 \(f_i\in W^r\)，因此严格地
\(m\le rM\)。若 \(W\) 尚未证有限，同样可对任意有限 component 子集先应用 scalar 定理，得到一个统一有限上界后再得到有限性。

具体假设所有 actual components 都具有相同安全型
\(c\prod_h\mathrm{LCM}_{\lfloor b_hn\rfloor}\,[t^n]f_{i,j}\in\mathbf Z\)，其中固定整数 \(c\ne0\) 统一，\(\sigma=\sum_h b_h\)。一个合法 \(\varphi\) 同时使这些 scalar components meromorphic，且原文的 fixed pole 清因子条件成立。置

\[
\rho=\log|\varphi'(0)|,\qquad
J=\iint_{\mathbf T^2}\log|\varphi(z)-\varphi(w)|\,dzdw.
\tag{H4}
\]

若 \(\rho>\sigma\)，CDT Theorem8.0.1（PDF122–123；uniform 非负 b 表且 e=0）给

\[
M\le\frac{J}{\rho-\sigma},\qquad
\boxed{m\le\frac{rJ}{\rho-\sigma}.}
\tag{H5}
\]

证明：从 actual components 选 \(M\) 个 scalar basis 元素，各自仍有原型；uniform 表的 \(\tau^{\flat\flat}=\sigma\)，不用称 arbitrary rational-linear combination 同样具有原型。先用 scalar 定理再用 (H3)。若已有 scalar holonomicity，可按定理的已 holonomic 分支；此处 uniform 表的 positivity 条件本来已满足。

数域版本有完全相同的纯线性代数 \(m\le rM\)。若 actual scalar 系统符合已证明的[限定数域引理](cdt_odd_level20_arithmetic_20261006.md) §6，则 (H5) 中 \(J,\rho\) 替换各 embedding 的共同平均。未知非 holonomic components 不能仅借该限定引理省略自动 holonomicity 的前提。

**适用限制：**这里的 component frame 必须实际在 \(K[[t]]\) 上且已核分母及各 embedding 的 continuation。PV fundamental frame、\(\tau=\log q/(2\pi i)\) 的 frame、非全纯 Hodge orthogonal projection 都不满足这个假设。选择 rank3 frame 后保留旧 scalar upper bound 而不付因子3，是无效的归约。

## 3. 一个精确的指标抵消与一个固定 log-growth 比较引理

**纤维 rescaling 精确抵消。**固定所有有限整格，若某个目标范数换成 \(e^{-c}\|\cdot\|\)，则
\(\widehat\mu_{\max}(G)\) 增加 \(c\)，operator height 减少 \(c\)。在 (H2) 中严格抵消，甚至不只主项。

更一般对
\(G_{D,n}=E_P\otimes L_P^D\otimes(T_P^*)^n\)，若 \(E_P,L_P,T_P\) 的范数分别乘 \(e^{-a},e^{-c},e^{-b}\)，则目标范数乘
\(e^{-a-Dc+nb}\)，目标斜率增加 \(a+Dc-nb\)，height 减少同一数量。不能只记正 Hodge slope 或只记 \(-n\rho\)。全局 rescale \(L\) 时源范数及源 arithmetic degree 也必须相应变化。

**固定 log-growth 引理。**令 \(X\) 为固定光滑紧复曲线，\(S\) 为有限点集，\(L\) 为带连续 Hermitian metric 的固定 line bundle，\(E\) 为固定 holomorphic rank \(r\) bundle。令 \(h_0\) 为 \(E\) 的 smooth positive metric，\(h\) 在 \(X\setminus S\) 正定，且存在固定 \(A,C\) 使

\[
C^{-1}W^{-A}h_0\le h\le CW^Ah_0,
\qquad W=1+\sum_{s\in S}\log^+\frac1{d(x,s)}.
\tag{H6}
\]

用一个固定 smooth positive volume form 计算
\(H^0(X,L^D\otimes E)\) 的两个 L2 norms。则

\[
e^{-o(D)}\|s\|_{0,D}\le\|s\|_{h,D}
\le e^{o(D)}\|s\|_{0,D},
\quad\text{对所有 }s\text{ 一致。}
\tag{H7}
\]

这里不要求 h 在 S 有 finite fiber value，也不要求 \(L\) 的 metric smooth。证明如下。记 \(M_D=\sup_X\|s(x)\|_{L^D\otimes h_0}\)。\(W^A\) 可积，所以 \(\|s\|_{h,D}\le C_1M_D\)。给 \(\epsilon>0\)，取固定有限小 chart，使 \(L\) 的 local log-weight 振荡不超过 \(\epsilon\)，且 \(h_0\) 的 frame comparison 统一。在 \(M_D\) 取到的点，至少一个 holomorphic component 大于固定倍数的局部 vector 长度。Cauchy derivative bound 给该 component 在半径 \(c_\epsilon e^{-\epsilon D}\) 的小圆盘仍大于该值的一半；换回 metric 后长度至少 \(c'_epsilon M_De^{-\epsilon D}\)。圆盘中剔除离 S 最接近的小同心子盘，可取面积至少固定倍数的 \(e^{-2\epsilon D}\) 子集，其 \(W\le C_epsilon(D+1)\)。故

\[
\|s\|_{h,D}^2\ge
c''_\epsilon M_D^2e^{-4\epsilon D}(D+1)^{-A}.
\tag{H8}
\]

相同论证也适用于 \(h_0\)，从而两个 L2 norms 相对 log-distortion 至多 \(2\epsilon D+O_\epsilon(\log(D+1))\)。先 \(D\to\infty\)，再 \(\epsilon\downarrow0\)，得到 (H7)。有限点附近的子集选择可统一：一个小圆盘的固定面积比例避开全部半径为其半径固定小倍数的 S-邻域；在该子集到 S 的距离有此下界。若最大点本身位于 S，同一论证仍成立。

**完整 slope 后果。**假设同一 actual source lattice 与 evaluation maps 已给定，\(R_D=O(D)\)、\(\sum_n a_{D,n}=R_D\)，目标使用固定非退化 finite fiber norm。只更换源的固定 log-growth metric 时，源 degree 的差至多 \(R_Do(D)=o(D^2)\)，每个 quotient source norm 也有 (H7)，所以所有评价高度加权和的差至多 \(\sum_na_{D,n}o(D)=o(D^2)\)。固定 fiber comparison 只再给 \(O(D)\)。finite-place operator norms 在**同一格、同一 map**下完全不变。因此这种固定 Hodge metric 的更换不能改善既有账本的 \(D^2\) 主项。

这个后果不把另一个未经核算的 model 或 scalar 配对称为“同一 map”；也不证明任何未知 finite evaluation height 小。其结论正是一个可检验的指标比较引理，而非一个新 vector-CDT 定理。

对固定 \(d\) 个这样的曲线及 fixed external tensor bundle，证明逐字改为小 polydisc：半径 \(ce^{-\epsilon D}\) 的有效 volume 为 \(\gg e^{-2d\epsilon D}\)，log 权只给固定次幂的 \(D+1\) 因子，所以仍有统一 \(e^{o(D)}\) norm comparison。若 source rank 为 \(O(D^d)\)，总 degree/height 差为 \(o(D^{d+1})\)。这与 CDT **先 \(D\to\infty\) 固定 d，再 \(d\to\infty\)** 的极限次序相容，不要求误差 uniform in d；不覆盖 \(d=d(D)\) 或 \(\operatorname{Sym}^D\mathcal E\)。

## 4. 实际 D12 Sym² 束的几何度账本

现有实际 Γ 是 torsionfree、genus0、index48、10cusps。采用 \(SL\Gamma_1(12)\) 的 unipotent lift；只使用 PSL 代表时 weight1 的符号不可省略，以下 even-weight 账本没有该歧义。Kodaira–Spencer 为

\[
\omega^2\simeq\Omega^1_X(\log S),\qquad
\deg\omega=4.
\tag{H9}
\]

这是 \(\deg\Omega^1_X(\log S)=-2+10=8\)，与 index/12=4 一致。rank2 logarithmic de Rham Hodge filtration 是
\(0\to\omega\to\mathcal H\to\omega^{-1}\to0\)。在 \(X\simeq\mathbf P^1\) 上，该 holomorphic extension 的 Ext1 为 \(H^1(O(8))=0\)，故仅作为 holomorphic bundle 它分裂。于是

\[
\mathcal E=\operatorname{Sym}^2\mathcal H
\simeq O(8)\oplus O\oplus O(-8),\quad
\deg\mathcal E=0.
\tag{H10}
\]

这里不声称 connection 分裂或 invariant Hodge line 的存在。共同 Sym² monodromy 已证 irreducible；正度的 \(O(8)\) Hodge line 不是 horizontal submodule，Kodaira–Spencer/Higgs map 非零。

ICM2006 Theorem3.1/PDF8 的 function-field algebraization 要求实际 formal germ 延拓及其 normal bundle ample。如果试图把整个 (H10) 当作这个 normal bundle，它有 \(O(-8)\) quotient，因而不是 ample；只选正度 Hodge line又未给相应的 actual horizontal germ。这个观察只否定该直接套用，不否定其他实际 normal bundle 的构造。

固定源几何范例为
\(S_D=H^0(X,O(D)\otimes\mathcal E)\)。对 \(D\ge8\)，严格地

\[
R_D=(D+9)+(D+1)+(D-7)=3(D+1).
\tag{H11}
\]

它的 **whole-vector 消失阶** filtration 是
\(S_D^n=H^0(X,O(D)\otimes\mathcal E(-nP))\)。逐个 \(O(D+c)\)、\(c=8,0,-8\)，在第 n 阶有一个非零 grade 当且仅当 \(n\le D+c\)，故严格地

\[
a_{D,n}=\begin{cases}
3,&0\le n\le D-8,\\
2,&D-7\le n\le D,\\
1,&D+1\le n\le D+8,\\
0,&n>D+8.
\end{cases}
\qquad\sum_na_{D,n}=3(D+1).
\tag{H11a}
\]

最后 order 是 \(D+8\)，不是 \(3D\)；每阶最多3个方向。它**不是**与 actual 水平 scalar solution 配对后的 leading filtration，后者每阶最多1个方向、必须另给零估计。不能把 (H11a) 的 source rank、正 Hodge line 和旧 scalar 的 \(mD\) coverage 拼成一个不存在的评价包。

degree8 并未把 rank3 算成 rank1，也未增加 \(D^2\) 正主项。若已给 fixed integral model、fixed singular metrics 满足 (H6)，各固定 degree shifts 的源 Hermitian degree 主项是
\(3\widehat{c_1}(\overline{O(1)})^2D^2/2\)。理由是三个固定 shifts \(D+8,D,D-8\) 的既有 line Hilbert–Samuel 主项与 (H7)；固定 coherent model 的 generic splitting 若只差有限 vertical denominators，使用一个固定非零整数夹住两 sheaves，source index 至多 \(O(R_D)=O(D)\)。这不替任何新的 graded evaluation map 核 finite heights。

原始 singular-HS 支持是 [Berman–Freixas](../literature/berman_freixas2014_singular_hilbert_samuel_arxiv_20261006.pdf) Theorem1.2/PDF3，正文 Theorem4.6/PDF17：在其 semi-positive、generic big/semi-ample、vertical nef、log-singular 的明确条件下，\(H^0(L^D\otimes N)\) 的固定 log-singular twist \(N\) 不改 leading degree。不能在未核 semi-positivity/regularity 时直接套这个定理到某个新的 CDT metric；上面的 (H7) 特意只作 norm comparison。

在 Tate cusp，Hodge line 的范数平方是 \(\operatorname{Im}\tau\) 的固定倍数；其 dual 为倒数，Sym² 的 Hodge graded norm 平方有 \(y^2,1,y^{-2}\) 的尺度，\(y\asymp\log(1/|q_c|)\)。这是 (H6) 的固定 log-power 类型，而非一个有限正定的 cusp fiber metric。Burgos–Kramer–Kühn 的原件 PDF61–62 / 印刷679–680，Definition4.25、Proposition4.27 及 PDF87 / 印刷705 的 Theorems6.2–6.3 描述 fully decomposed automorphic bundle 的 singular metric 与 canonical extension；不以该定理自动证明整个非分裂 flat extension 的 metric，也不提供未核算的 cusp Taylor jet norm。若换成 Deligne/tangential fiber 必须明确选择有限 metric 与整格，再用 (H2)。

## 5. 真正 primitive 的 affine extension 与尚未完成的评价接口

上述 rank3 束只承载齐次 carrier。实际 \(H_Z,H_L\) 有非分裂 forcing；[冻结 affine/PV 稿](cdt_odd_level12_affine_galois_20261006.md) 已证单周期 \(\mathbf G_a^3\rtimes PSL_2\)、双周期 \(\mathbf G_a^6\rtimes PSL_2\)，并已实际独审。单目标的正确 rank4 包含的是 affine extension

\[
0\longrightarrow\mathcal E\longrightarrow\mathcal F_j
\longrightarrow O\longrightarrow0,
\tag{H12}
\]

而不是把 primitive 作为三个齐次 section。一个具体 log-connection extension 可由已证 rank4 rational companion 系统在 char0 构造；本文未构造其完整 \(O_K\) arithmetic model 或所有 cusp finite jet lattices。若固定 model 存在且其 source bundle rank4、degree0，则 Riemann–Roch 给大 D 的 rank \(4(D+1)\)；这仍不是已经证明的 scalar graded rank 或 Taylor integrality。

去掉 gauge 的真实 \(h_j\) 已在[另一冻稿](cdt_odd_level12_nongauged_rank_20261006.md) 证明不 Dfinite over \(\mathbf C(v)\)。所以 cheap \(n^{-3},n^{-2},n^{-1}\) q-denominators 不能据此被装入一个 gratis rank3/4 scalar 评价包。它可能作为 genuine bundle/affine section 的数据，但必须实际建立 (H1)，核 \(a_{D,n}\)、multiplicity estimate、source lattice、cusp graded lattice 和 finite operator height。

## 6. 能改变主项的最小正接口与严格缺口

本轮保留一个定向 positive 接口：采用 genuinely D-varying bundle/metric，并证明下列数据属于**同一 actual evaluation**：

1. \(E_D\) 的实际 \(O_K\) lattice、\(R_D\)、\(\widehat\deg E_D=A D^2+o(D^2)\)；
2. 饱和 leading filtration、全 \(a_{D,n}\)，以及 order coverage 的零估计；
3. 每个 graded lattice/metric 的 \(\widehat\mu_{\max}\)，及 finite heights 的和；
4. archimedean height 总项，包括 curvature/Green boundary terms，给明确 \(B D^2+o(D^2)\)；
5. 在 (H2) 中严格证明 \(A>B\)。

只改变固定 rank3 Hodge metric 满足 (H6) 时，§3 已证明不改变这两个主项之差。若改用 \(\omega^{kD}\)，它的 generic degree 是 \(4kD\)；若 \(L=O(1)\)，source rank 成为 \(r(1+4k)D+O(1)\)，并改变 source HS 及 fiber terms。若用 \(\operatorname{Sym}^D\mathcal E\)，rank 已为 \(\binom{D+2}{2}\)，不能保留旧 \(m(D+1)\) 或旧 balanced species 公式。这些改变有可能有价值，但收益必须由完整 (H2) 给出。

Bost 的 algebraicity 不是另一种免费向量秩界：[2001原文](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf) Theorem3.4（印刷185–186 / PDF25–26）、§3.4 的 sizes，以及 Proposition4.12（印刷206 / PDF46）分别要求实际 formal germ 的 finite-place sizes、Liouville/archimedean 条件和合法 regular point。一般 Gauss–Manin 的 nilpotent p-curvature 不能写成 vanishing p-curvature；已有 Hasse 一/二层 Smith 关系也不自动给 almost-all-p vanishing。当前 cusp 是 log-singular 点，更不能直接冒充该光滑 formal foliation 定理的 regular point。

### 6.1 当前真实 scalar graph 的 Bost-size 条件确实失败

这不是仅“尚未验证”。对一个好地方 \(\mathfrak p\mid p\)，设
\(f(t)=\sum_{n\ge1}a_nt^n\)，\(a_1,\ldots,a_{p-1}\in O_{\mathfrak p}\)，
\(|a_p|_{\mathfrak p}=|p|_{\mathfrak p}^{-3}\)。令 \(\widehat V\) 为平面上的实际 graph \(y=f(t)\)，采用平面整模型及其原点。

Bost PDF22–24 定义 \(G_\omega(R)\) 由 formal automorphisms \(\Phi\) 满足
\(D\Phi(0)\in GL_2(O_{\mathfrak p})\)、\(\|\Phi_i\|_R\le R\)。假设 \(\Phi\) flatten 该 graph。把 \(\Phi\) 限制在第一坐标轴，得
\(t=u(z),y=v(z)=f(u(z))\)。其 Jacobian 第一列为
\((u_1,a_1u_1)\)，是 primitive integral vector；因 \(a_1\) 整，\(u_1\) 必为单位。并且所有 \(u_j,v_j\) 的绝对值都至多 \(R^{1-j}\)。对 \(1\le n<p\)，

\[
\big|[z^p]a_nu(z)^n\big|_{\mathfrak p}\le R^{n-p}\le R^{1-p}.
\]

由 \([z^p]v=a_pu_1^p+\sum_{n<p}[z^p]a_nu^n\) 及非arch triangle，
\(|p|_{\mathfrak p}^{-3}=|a_pu_1^p|_{\mathfrak p}\le R^{1-p}\)。因此对其 supremum size 严格有

\[
\boxed{R_{\mathfrak p}(\widehat V)
\le |p|_{\mathfrak p}^{3/(p-1)}.}
\tag{H14}
\]

这是对所有合法 flattening 的证明，不只是原坐标 graph 的 convergence-radius estimate。

在纯 \(L(3,\chi_{12})\in\mathbf Q\) 反证假设下，取
\(f=D_0(H-H(0))\)，或者取 \(f=D_0(gH-g(0)H(0))\)、\(g\in O_K[t]\)、\(g(0)\) 为单位。冻结[全前缀分母稿](cdt_odd_level12_source_denominators_20261006.md) (D4)–(D5) 正好给上述前 p−1 项整及第 p 项赋值−3，除固定有限坏素数外，对每个 \(\mathfrak p\mid p\) 都成立。Bost 使用 \(|p|_{\mathfrak p}=\operatorname{Norm}(\mathfrak p)^{-e_{\mathfrak p}}\)，所以

\[
\sum_{\mathfrak p}\log R_{\mathfrak p}^{-1}
\ge3[K:\mathbf Q]\sum_{p\notin S}\frac{\log p}{p-1}
=+\infty.
\tag{H15}
\]

Theorem3.4 的必要前提 \(\sum\log R_{\mathfrak p}^{-1}<\infty\) 因而确实不成立。Bost PDF25 明确说明换任一**固定** arithmetic model 后 sizes 只在有限 places 改变；故此失败不能由固定 reembedding 或固定 integral model 更换消除。CDT 能处理 LCM 型分母，正是它不要求 (H15) 的和有限。

这只针对此实际 scalar graph 和该 Bost-size 判据，不排不同 actual bundle germ、随 p 适配的原格、Cartier 消去或另外一种 nonarchimedean theorem。也不把 graph 本身的 smoothness 与 cusp 处某个 log-connection 的 regular-point 条件混同。

此外，原始 [Bost–Charles](../literature/bost_charles2022_arithmetic_surfaces.pdf) Theorem8.2.2/PDF151 确实允许 fixed Hermitian vector bundle 的 θ-finiteness，但其精确 quadratic bound (8.2.3) 是针对 **line tensor powers**：

\[
\limsup D^{-2}h^0_\theta(\widetilde V,M^D)
\le\frac{(M\cdot(P,g))^2}{2\widehat\deg N_P\widetilde V},
\quad
M\cdot(P,g)=\widehat\deg P^*M+\sum_\sigma\int g_\sigma c_1(M_\sigma).
\tag{H13}
\]

curvature、fiber degree 和 pseudoconcavity denominator 都在其中。它不称所有 fixed vector bundles 有同一 scalar bound，更不允许只保留 Hodge curvature 的有利部分。可检验的下一任务因此是构造一个 actual D-varying bundle 的 (H1)–(H2)/(H13) 完整模型，而非继续固定 degree8 的指标调权。

## 7. 阅读、保存与证明范围

新原件保存于 literature；[独立新清单](../literature/manifest_cdt_odd_hodge_bundle_20261006.json) 记录 URL、版本、页数、SHA 和实际阅读范围。Berman–Freixas 作者链接返回404，改保存官方 arXiv1209.0996v1；未禁用 HTTPS certificate verification。

本稿纯 MD，没有 mathematical producer 或 JSON checks。实际只读 CDT PDF122–123、89–90 的 scalar theorem / 99 的 source degree 规范，Bost2001 PDF22–26、36–40、43–46，ICM2006 PDF1–3、7–9、16–18，Bost–Charles PDF151–153，Berman–Freixas PDF1–3、17–19，BKK PDF1–3、6、61–62、85–87；BKK PDF90–95 仅定位相关定理及 proof 结构；没有把未读部分称为已审。§2–3、§6.1 的证明由本稿承担；§4 的 degree 规范由实际 Γ/cusp 输入及 Kodaira–Spencer 给出，不是 arithmetic evaluation integrality 的证明。真正 D-varying 原格净优势仍开放。

根任务已实际全文只读独审 §§1–7（含 §6.1），在声明范围内通过 log-growth norm comparison、scalar-component penalty、完整 slope 账本和 actual scalargraph 的 Bost-size 障碍；根任务未执行 producer。按该审阅的明确要求补入 (H11a) 的 whole-vector grade 计数及固定 d product 的先 D 后 d 比较，均附本稿证明，不把它们当成水平 scalar pairing 的覆盖结论。

conjugate_projection 已实际只读独审 §6.1/H14，重推 primitive Jacobian 第一列、全部低阶系数的 \(R^{n-p}\) 界和非arch triangle；H14/H15 的声明范围通过。该独审未重新证明 frozen source_denominators 的赋值输入，也未重审 Bost fixed-model invariance，不作为新 bundle 净信用的审阅。本纯 MD 及本轮独立 literature manifest 在上述范围冻结；没有新增 mathematical producer。
