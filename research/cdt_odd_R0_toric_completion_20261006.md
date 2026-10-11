# 非 regular 四二次曲面 toric family 的真正 coordinate-symbol completion

日期：2026-10-06。本稿是新的纸面证明。旧 R0 geometry 稿及 manifest 已实际全文阅读；全部旧数学 Markdown、Python、JSON 与 manifest 只读，未执行、导入或修改 producer。本文不宣称新数值无理性定理，不将 arbitrary inhomogeneous PF 解当成 regulator。

## 1. 精确新结论和仍未完成的比较

令 \(P=(\mathbb P^1_\mathbb Q)^4\)，以 \(v_j=a_j/b_j\) 为坐标，

\[
 \phi(v)=\prod_{j=0}^3\frac{(1+v_j)^2}{v_j},\qquad
 \lambda=256x.
\]

旧稿的 hypersurface 是 \(\phi=\lambda\)，即

\[
 \prod_j(a_j+b_j)^2-\lambda\prod_ja_jb_j=0. \tag{1.1}
\]

记 \(U=\mathbb P^1\setminus\{0,\infty,-1\}\)。本稿构造一个定义于 \(\mathbb Q\) 的 proper toroidal modification \(b:\widetilde P\to P\)，使 rational map \(\phi\) 变成 morphism \(f:\widetilde P\to\mathbb P^1\)。设

\[
 Y=f^{-1}(\mathbb G_m),\qquad Y^*=b^{-1}(U^4)=U^4.
\]

其中 \(Y\) 是光滑四维 quasi-projective variety，\(Y\to\mathbb G_m\) proper，边界 \(E=Y\setminus Y^*\) 是 split SNC divisor。新主结论为

\[
 \boxed{\exists\ \Xi\in CH^4(Y,4)_\mathbb Q:
       \Xi|_{Y^*}=\{v_0,v_1,v_2,v_3\}.} \tag{1.2}
\]

它是**实际 compact-family model 上的 higher-Chow completion**，强于 field Milnor symbol 的所有 tame residues 为零。对每个 smooth fibre \(Y_\lambda\)，pullback 给出真正 \(CH^4(Y_\lambda,4)_\mathbb Q\) class。

以下证明单独处理非 regular 边界，**没有套用 Doran–Kerr published Theorem 3.1 的 n=4 regular case**。它仍不识别 \(AJ(\Xi)\) 与旧稿 \(8[-1,1]^4-T\Gamma_x\) 的具体 marking；不识别其 conifold special value 为 \(R_0-M_0\)。两者的 regulator-current、closed-cycle ambiguity、Tate normalization 与 integral saturation 仍须比较。

## 2. Split SNC 网格与完全确定的局部 monomial 数据

在 \(P\) 上取十二个 coordinate divisors

\[
 S=\bigcup_j\{v_j=0\}\cup\{v_j=\infty\}\cup\{v_j=-1\}.
\]

每个 factor 的三个点互不相交，故 \(S\) 是 split SNC divisor；每个 stratum 是 \(U^{4-s}\)，其中 \(s\le4\) 个不同 factor 被固定。

对某个固定 grid stratum，按被固定的 factor 取参数

\[
 z_i=v_i\ (v_i=0),\quad z_i=1/v_i\ (v_i=\infty),
 \quad z_i=v_i+1\ (v_i=-1).
\]

局部有 exact identity

\[
 \phi=c(z,v_{\rm free})\prod_{i=1}^s z_i^{e_i},\qquad
 e_i=\begin{cases}-1&v_i=0,\infty,\\2&v_i=-1,\end{cases} \tag{2.1}
\]

且 \(c\) 是该 stratum 邻域上的 unit，其在 stratum 上为

\[
 c_S=(-1)^p\prod_{j\text{ free}}\frac{(1+v_j)^2}{v_j},
 \qquad p=\#\{i:v_i=-1\}. \tag{2.2}
\]

例如 \(v_i=\infty\) 时因子同样为 \((1+z_i)^2/z_i\)；不能给 infinity 漏记 pole。因而

\[
 \operatorname{div}(\phi)=2\sum_j[v_j=-1]
              -\sum_j([v_j=0]+[v_j=\infty]). \tag{2.3}
\]

这将 repeated face roots 变成一个具体 split toroidal rational map，而不是假设原 hypersurface boundary reduced。

## 3. 可复查的 resolution：先切 hyperplane，再 regularize 原 lattice

原 cone complex 的每个 cone 是 \(\sigma_S=\mathbb R_{\ge0}^s\)，原 lattice 为 \(N_S=\mathbb Z^s\)。线性函数是

\[
 \ell_S(a)=\sum_i e_i a_i.
\]

先将每个 cone 以 \(\ell_S=0\) 切成两个 closed half-cones 及其 faces；不同 cones 上的限制相容。这个 subdivision 是 rational coherent subdivision：局部 support function 为 \(\max(0,\ell_S)\)。

这也直接来自 local normalized graph construction。写 \(e=e_+-e_-\)，rational map 的 graph 是 monomial ideal

\[
 (z^{e_+},z^{e_-})
\]

的 blowup，随后 normalization；(2.1) 的 invertible factors 不改变这个 ideal。于是得到 split toroidal model，所有 cones 都完全落在 \(\ell_S\ge0\) 或 \(\ell_S\le0\) 中，rational map 已无 indeterminacy。

再取兼容的 projective regular subdivision，**保持原 lattice \(N_S\)**。所用标准 toroidal resolution theorem 为 KKMS II §2 Theorem 11*, p.94；其准确形式可在 Abramovich–de Jong original v1 PDF3 Theorem0.4 实际读到：strict toroidal embedding 存在 canonical ideal 的 nonsingular blowup。这里采用的是其 **toroidal/monomial modification**：先在有限 cone complex 上作兼容 simplicial subdivision，再在同一 integral lattice 中 regularize；每一进一步 cone 仍 contained in 某个已有 half-cone。不是对 underlying graph 施行 arbitrary Hironaka resolution，也不是用该文 Theorem0.1 的任意 smooth center。所选 regular subdivision 只增加 toroidal orbit strata。

所有 boundary components、cones 和 local monomial data 在 \(\mathbb Q\) 上 split。一个 stratum 邻域的 modification 是 integral toric monomial construction 与该 stratum 的乘积；不同邻域的 monomial ideal 在重叠上只相差 invertible generators，按 cone complex 的 face restrictions 相容。故可把该 projective toroidal construction 定义于 \(\mathbb Q\)。没有 extension of function fields，也没有从半整数 lattice 偷换成 ramified base change。

新保存的 KKMS ChapterIII PDF29 的 printed161 Theorem4.1 是**允许 denominators 改变的 polyhedral subdivision theorem**；本稿不误用它来声称 fixed-lattice regularity。它仅支持 subdivision 的标准背景。真正使用的是上述 fixed-lattice toroidal resolution theorem。

因为 refinement 仍位于切开的 half-cones，map \(f:\widetilde P\to\mathbb P^1\) 保持为 morphism。来源为 proper projective modifications，故 \(f\) proper。所有新 boundary components 在光滑 toroidal model 上形成 SNC。

### 3.1 一个确切的二阶边界 chart

取 \(v_0=0,v_1=-1\)，令 \(z=v_0,w=v_1+1\)，其余 \(v_2,v_3\in U\)。有

\[
 \phi=\frac{w^2}{z}
       \frac{(1+z)^2}{w-1}\phi_{23},\quad
 \phi_{23}=\frac{(1+v_2)^2(1+v_3)^2}{v_2v_3}. \tag{3.1}
\]

二维 fan 的 ordered rays 可取

\[
 (1,0),\ (2,1),\ (1,1),\ (0,1).
\]

相邻 determinants 全为1，所以两次 ordinary toroidal blowup 已产生 smooth chart。horizontal ray 为 \((2,1)\)，邻近两条 rays 的 \(\ell=-a_z+2a_w\) 分别为 \(-1,+1\)。删掉 \(f=0,\infty\) 后两侧 vertical divisors 被去掉，留下该 exceptional divisor 的 open stratum。

在 horizontal stratum 上 \(q=z/w^2\in\mathbb G_m\)，且

\[
 \lambda=-\phi_{23}/q. \tag{3.2}
\]

因此该 family boundary stratum 正是 \(U^2\times\mathbb G_m_q\)，也正是 \(U^2\times\mathbb G_{m,\lambda}\)。其 symbol residue 是 \(2\{-1,v_2,v_3\}\)，在真正 \(CH^3\) group 中 rationally 为零。此 chart 不以 formal analytic resolution 代替 algebraic blowup。

## 4. 所有 horizontal strata 的完整形状

令 refined cone \(\tau\subset\sigma_S\) 的 dimension 为 \(r>0\)，且相对内部落在原 \(s\)-cone 的内部。其 associated stratum 在 \(\widetilde P\) 上 codimension \(r\)，normal torus 的 rank 为 \(s-r\)。该 stratum 落在 \(Y=f^{-1}(\mathbb G_m)\) 当且仅当

\[
 \tau\subset\ker\ell_S. \tag{4.1}
\]

理由：在正/负 half-cone 中，任何具有正/负 order 的 ray 都使 stratum 分别落在 \(f=0/\infty\)；被删去后所有 surviving rays 都只能 horizontal。

非零 horizontal cone 的最小原 support \(S\) 必同时含正、负 exponents：其 relative interior 有某个 vector \(a\) 在这 \(s\) 个 original coordinates 上全部 strictly positive，而 \(\sum e_i a_i=0\)；若只有一种符号不可能等于0。因此 \(s\ge2\)，且至少一个固定 coordinate 是 \(-1\)，另一个为 \(0\) 或 \(\infty\)。又 \(\ell_S\ne0\)，故 \(\dim\ker\ell_S=s-1\)；\(\operatorname{span}(\tau)\subset\ker\ell_S\) 严格给 \(r\le s-1\le3\)。

这里可直接证明 orbit bundle **全局** split，不只在 étale topology 中 split。对每个被固定的 factor，用 §2 的 \(z_i\) chart：在 \(0\) 或 \(\infty\) 的 chart 是 \(\mathbb A^1\setminus\{-1\}\)，在 \(-1\) 的 chart 是 \(\mathbb A^1\setminus\{1\}\)。因此同一个 fixed grid stratum 的完整 Zariski neighborhood，是 \(\mathbb A^s\times U^{4-s}\) 的一个 explicit open subset，且在每个 fixed factor 上都有 **同一个全局参数** \(z_i\)。其 normal lines 确是固定 \(\mathbb P^1\) 因子的 tangent lines，全部 trivial over \(U^{4-s}\)，没有 transition character 或 permutation。

在这个 neighborhood 上，每个 selected monomial modification 就是相应 split toric modification \(X_{\Sigma_S}\to\mathbb A^s\) 与 \(U^{4-s}\) 的乘积，再限制 open subset。若 \(\tau\) 的 minimum original support 正是这 \(s\) 个 coordinates，则每个 \(z_i\) 在 associated orbit \(O_\tau\) 上为0：其 original coordinate character 对某个 \(\tau\) ray 有 strictly positive pairing。故上述 chart 中移除的非零值 \(z_i=\pm1\) **完全不删掉任何 orbit point**。这样整个 stratum 已被一个 global product chart 覆盖，而不是在若干可能 twisted local charts 间粘接。于是 \(O_\tau\simeq\mathbb G_m^{s-r}\) 给出实际 algebraic stratum

\[
 \boxed{D_{S,\tau}^{\circ}\simeq
        U^{4-s}\times\mathbb G_m^{s-r}.} \tag{4.2}
\]

在其上 \(f=c_S\chi_{\ell_S}\)。因为 \(\ell_S\) 具有一个 \(-1\) coefficient，它是 primitive character；它在 quotient lattice \(N_S/N_\tau\) 上仍 primitive（选原 \(-1\) coordinate vector，其 image 的 pairing 为 \(-1\)）。用 \(GL_{s-r}(\mathbb Z)\) basis change，再将其中一个 torus coordinate 乘 invertible \(c_S\)，得到

\[
 D_{S,\tau}^{\circ}\simeq
 U^{4-s}\times\mathbb G_m^{s-r-1}\times\mathbb G_{m,\lambda}, \tag{4.3}
\]

且 \(f\) 是最后一项 projection。没有在此引入 square-root extension 或 nontrivial torus form。这特别证明 \(f\) 在所有 boundary strata 上 smooth。

此外 interior \(U^4\) 上 \(\partial_{v_j}\log\phi=(v_j-1)/(v_j(1+v_j))\)；全部 derivatives 为0只可能 \(v_j=1\) for all \(j\)，其 \(\lambda=256\)。所以整个 proper fibre \(Y_\lambda\) 对 \(\lambda\in\mathbb G_m\setminus\{256\}\) 光滑；不是只知道 unspecified generic open smooth。本稿仍不把 singular fibre \(\lambda=256\) 的 higher-Chow pullback、nearby integral marking或special value自动视为已构造。

于是对 codimension2 family strata，只可能有

\[
 s=3:\quad U\times\mathbb G_m;\qquad
 s=4:\quad\mathbb G_m^2. \tag{4.4}
\]

这些是 family over \(\mathbb Q\) 的二维 strata；不能把它们改看为 Spec\(\mathbb Q(x)\) 后，再无依据套用 totally-real-number-field vanishing。另一方面 codimension3 strata 为 \(\mathbb G_m\)，codimension4 horizontal stratum 不存在。

## 5. d1 在实际 higher-Chow boundary groups 中消失

取

\[
 \xi=\{v_0,v_1,v_2,v_3\}\in CH^4(Y^*,4)_\mathbb Q.
\]

每个 irreducible horizontal boundary divisor \(E_\alpha\) 都映到一个含 \(\{v_j=-1\}\) 的 original center。因此该 divisor 的全部 points 上

\[
 v_j|_{E_\alpha}=-1.
\]

函数 \(v_j\) 在含整个 \(E_\alpha\) 的 open neighborhood \(b^{-1}(v_j\ne0,\infty)\) 上是 regular unit。将该 unit 移到 symbol 的首项，higher-Chow localization 的 product compatibility 给出

\[
 \operatorname{Res}_{E_\alpha^{\circ}}(\xi)
 =\{-1\}\cdot
   \operatorname{Res}_{E_\alpha^{\circ}}
        \{v_0,\ldots,\widehat v_j,\ldots,v_3\}.
\]

由于 \(\{-1\}\) 在 \(CH^1(E_\alpha^{\circ},1)\) 中为2-torsion，rationally 为0，故

\[
 \boxed{\operatorname{Res}_{E_\alpha^{\circ}}\xi=0
       \quad\text{in }CH^3(E_\alpha^{\circ},3)_\mathbb Q.} \tag{5.1}
\]

这里 product formula 应用于整条 stratum 上的 unit，不是将 higher-Chow class 先映到其 generic function field。因此确实得到 localization spectral sequence 的 \(d_1\xi=0\)，没有遗漏旧稿强调的 possible field-restriction kernel。

## 6. 实际 d2 target 为零，而不是“第二次 tame residue为零”

以下使用标准 higher-Chow identities：对 smooth \(Z\)，\(CH^1(Z,q)=0\) for \(q\ge2\)；projective bundle formula；localization。

这里 general codimension-one vanishing 已由新保存的 MVW2006 primary 逐页核准：Theorem4.1/Corollary4.2 给 weight-one motivic complex \(\mathbb Z(1)[1]\simeq\mathbb G_m\)，Theorem19.1 给 \(CH^1(Z,q)=H^{2-q,1}(Z,\mathbb Z)\)，而 \(2-q\le0\) 的这些 weight-one groups 为0。实际阅读范围是 PDF40–42 与174,176–178。它与下一条 totally-real-field 算术 vanishing 是不同的输入。

再由 Borel/Suslin 的 totally-real-number-field结果，

\[
 CH^2(\mathbb Q,3)_\mathbb Q=K_3^{\mathrm{ind}}(\mathbb Q)_\mathbb Q=0.
\]

这些算术 identities 在 DK original published PDF26 (printed422) 已实际读到。

Rational projective bundle formula 已在 Levine1994 PDF84–85（printed317–318）Corollary5.4实际核读；products、pullback及projection compatibility见PDF79–83 Theorem5.2。未把Levine此节未陈述的 general \(CH^1\) vanishing归到该primary的覆盖。

**Lemma.** 若 \(Z/\mathbb Q\) 光滑、\(CH^2(Z,3)_\mathbb Q=0\)，且 \(A\) 是从 \(\mathbb P^1_\mathbb Q\) 删掉非空有限多个 \(\mathbb Q\)-points 所得 open curve，则 \(CH^2(Z\times A,3)_\mathbb Q=0\)。

证明：projective bundle formula 给

\[
 CH^2(Z\times\mathbb P^1,3)
 =CH^2(Z,3)\oplus CH^1(Z,3)=0.
\]

从该 projective line 删去那些 rational sections，localization sequence 的相邻部分为

\[
 CH^2(Z\times\mathbb P^1,3)\to CH^2(Z\times A,3)
 \to\bigoplus_{a\text{ removed}}CH^1(Z,2)=0.
\]

故中间 group 为0。证毕。两次迭代即得

\[
 \boxed{CH^2(U\times\mathbb G_m,3)_\mathbb Q
       =CH^2(\mathbb G_m^2,3)_\mathbb Q=0.} \tag{6.1}
\]

令 \(D^r\) 为全部 boundary strata 中 codimension 至少 \(r\) 的 closure，\(D^{r,*}=D^r\setminus D^{r+1}\)。它们是 (4.2) 的 smooth disjoint unions，形成 pure-codimension filtration。DK PDF29 (printed425) 实际给出的 general localization spectral sequence 为

\[
 E_1^{a,b}(4)=
 \begin{cases}CH^4(Y^*,-b),&a=0,\\
 CH^{4-a}(D^{a,*},-a-b),&a>0,
 \end{cases}
 \quad\Longrightarrow CH^4(Y,-a-b).
\]

在 \(E_r^{0,-4}\) 上，\(d_r\) target 是

\[
 CH^{4-r}(D^{r,*},3)_\mathbb Q
\]

的 subquotient。式 (5.1) 给 \(d_1\xi=0\)；(4.4) 与 (6.1) 给 \(d_2\) target **本身为0**。\(d_3\) target 是 \(CH^1(D^{3,*},3)=0\)；\(D^4=\varnothing\)，故无更高 target。因此

\[
 \xi\in E_\infty^{0,-4}
 =\operatorname{im}\bigl(CH^4(Y,4)_\mathbb Q
       \to CH^4(Y^*,4)_\mathbb Q\bigr).
\]

这严格证明 (1.2)。**并未将 \(d_2\) 误认作某个 iterated tame residue**，而是通过完整 family strata 的 actual higher-Chow groups 排除了它。

## 7. 对目标研究真正改变的输入和剩余缺口

现在可选择真正 \(\Xi\) 并研究其 regulator，不再只有 arbitrary scalar forcing 或 unramified field symbol。这个 positive lift 不要求原 \(\phi\) Δ-regular，也不要求把 nonreduced faces 当成 reduced。

但以下四项仍未证明，不能由 completion 自动推出：

1. 若两个 family completions 有差，localization 说明差只能来自 boundary-supported motivic classes。应实际计算该 kernel，不能先假定它非零，也不能免费视为0；即使 family completion 唯一，Abel–Jacobi 的具体 Betti lift 和 fibrewise completion 仍是另外的比较。
2. \(AJ(\Xi)\) 与旧 relative Betti chain 的 scalar period identity，需要 KLM current、真实 chains 及 Tate factors 的具体等式；相同 PF quotient 不够。
3. 本稿未写 admissible regulator normal function 的 full rank5 integral Betti/de Rham quotient、trace/saturation、conifold integral nearby-cycle lift。
4. Motivic lift 不等于 \(R_0-M_0\) 或 \(\zeta(7)\) 的新无理性；CDT 全 place 费用和解析叶仍须匹配完整模型。

下一个可验证行动应是将本稿的 actual coordinate symbol regulator restricted to positive orthant 与旧 Stieltjes period (8.2) 对照；先确定 regulator differential 的 cohomology class，再比较 actual tube 的 homogeneous ambiguity。

## 8. 下一步 regulator differential 的候选接口（明确条件）

DK published PDF79–80 的 Lemma4.1 通过 KLM currents 计算 hypersurface coefficient variation 的 Gauss–Manin derivative。其已陈述版本对 \(\ell=2,3\) 的 Δ-regular family；其 proof 所用 exterior-form identity 提示本例可单独重做 \(\ell=4\)，但本稿没有直接声称该 Lemma 已覆盖我们的非regular compact boundary。

在 smooth locus \(\lambda\ne256\) 上，候选 identity 按该 proof 的 residue convention 是

\[
 \nabla_{\partial_\lambda}AJ(\Xi_\lambda)
 \stackrel{?}{=}-\left[\operatorname{Res}
       \frac{d\log v_0\wedge\cdots\wedge d\log v_3}{\phi-\lambda}\right].
\]

与旧 exact form \(\Omega_x=16d\log v^4/(\phi-256x)\) 比较，若实际 regulator current、boundary-supported completion ambiguity 与 compact pure-sector restriction 都已处理，则 \(\omega=\sqrt{x}\operatorname{Res}\Omega_x\) 规范会给候选

\[
 \nabla_{\theta_x}AJ\stackrel{?}{=}-16\sqrt{x}\,[\omega].
\]

这解释为什么完成 symbol 后的来源**可能**与 \(P_4W=\sqrt{x}/16\) 同型。但本稿未计算 exact Yukawa constant \(\kappa\)，未建立完整 compact integral projector，未证明与旧 \(8C-T\Gamma\) marking 的 current equality；因此不能把上述问号删掉，不能推断 \(AJ(\Xi)\) 的 conifold value 已等于 \(R_0-M_0\)。

## 9. 一手来源与阅读边界

* Doran–Kerr, *Algebraic K-theory of toric hypersurfaces*, published CNTP5(2011), [本地204页原件](../literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf)，本轮实际读 PDF25–29、48–56、71–83：higher-Chow graph/product/localization conventions、Borel vanishing、一般 local-global spectral sequence、不能直接套的n=4 completion theorem，以及regulator/current/inhomogeneous-source的准确范围。没有重读全文。
* Abramovich–de Jong, *Smoothness, Semistability, and Toroidal Geometry*, [fixed arXiv v1](https://arxiv.org/pdf/alg-geom/9603018v1)，[本轮保存](../literature/abramovich_dejong1996_smoothness_toroidal_v1_20261006.pdf)，12PDF页；实际读PDF1–3，Theorem0.4明确引用 KKMS II§2 Theorem11* 的 strict toroidal nonsingular modification。PDF首页编译日期2018-10-22，不把它误当成发表日期；arXiv版本固定v1（1996-03-24）。
* KKMS, *Toroidal Embeddings I*, ChapterIII（Knudsen）[本轮保存的31张双页scan](../literature/kkms1973_toroidal_subdivisions_chapterIII_20261006.pdf)，[institutional source](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/MumfordDavid/KKMS-chapter3.pdf)。实际视读PDF4–5（printed110–113）、27–30（printed156–163）；确认 rational/projective subdivision definitions和Theorem4.1。该Theorem允许denominators，本稿明确不用它代替 fixed-lattice resolution。
* Levine, *Bloch's higher Chow groups revisited*, Astérisque226(1994),235–320，[本轮保存87PDF页primary](../literature/levine1994_higher_chow_revisited_20261006.pdf)，[Numdam original](https://www.numdam.org/article/AST_1994__226__235_0.pdf)。实际读PDF79–85（printed312–318）：Theorem5.2的products、pullback、projection formula，Corollary5.4的rational projective bundle formula。未宣称阅读全文或该节单独证明 general codimension-one vanishing。
* Mazza–Voevodsky–Weibel, *Lecture Notes on Motivic Cohomology* (Clay Mathematics Monographs2,2006)，[官方primary](https://www.claymath.org/wp-content/uploads/2022/03/Motivic-Cohomology.pdf)，[本轮另一 agent 保存的234页原件](../literature/mazza_voevodsky_weibel2006_motivic_cohomology_clay_20261006.pdf)。本 agent 也实际读PDF40–42（printed25–27）Theorem4.1/Corollary4.2及proof4.3–4.6；PDF174,176–178（printed159,161–163）Theorem19.1及其proof。用于区分真正 weight-one higher-Chow vanishing和field Milnor tame条件；没有宣称已读全文。

本文是纸面符号证明；未创建或运行 mathematical producer；没有 numerical PSLQ 或 Lean claim。独立审查应单独登记 actual source 与 proof scope，特别是 (4.2) 的 global split orbit-bundle identification 和所选 toroidal resolution 的 fixed-lattice compatibility。
