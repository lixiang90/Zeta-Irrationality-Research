# p>D 的净 Smith 收益：先扣原行因子

日期：2026-10-06。仅处理冻结 [全局稿](cdt_odd_level20_hasse_global_20261006.md) 的原 E₄,D、E₇,D 与实际 rank4、rank7 系统，不改 source 或 arch metric。已有 p≤D 收益另属原稿。本文证明了一个全素数的终端窗口重复计数定理，并给出中间窗口的明确净收益判据；**尚未证明 p>D 新增正的 D² 收益，也没有数值无理性结论。**

## 1. 净收益的精确定义

令 R=m(D+1)，N=N_D=m(D+1)+O(1) 覆盖实际 primitive Taylor flag V_D。取好 p>D、p²>N，排除固定规范、c 的分母及 packet 首项的固定例外109。在每个未分歧 𝔭∣p，原 source 的 constant block 的 p-分母指数为

\[
 k_p=0\quad(m=4),\qquad
 k_p=1_{p\le2D}+1_{p\le4D}\quad(m=7).
\]

对选定 n∈V_D，原粗账本的指数是 c_p(n)=k_p 当 n<p，c_p(n)=3 当 n≥p。令 M 是 Ψ=p³eval 在实际 leading rows 上的原格整矩阵。先逐行提出**原来已有**的因子

\[
 M=\operatorname{diag}(p^{3-c_p(n)})\,\widetilde M.
 \tag{1}
\]

\(\widetilde M\) 仍整。primitive 旗标的 GL_R(O_{K,𝔭}) 适配不改变该 determinant valuation。由(1)，实际累计有限高度严格等于

\[
 \left(B_p-\Gamma_{p,D}\right)\log\operatorname{Norm}(\mathfrak p),
 \quad B_p=\sum_{n\in V_D}c_p(n),\quad
 \boxed{\Gamma_{p,D}=v_{\mathfrak p}(\det\widetilde M)\ge0.}
 \tag{2}
\]

这才是相对于原粗账本的净收益公式。不能将原 M 的 S1/S2/S3 列计数直接当作 Γ：例如当 k_p=0，整个 constant block 的 p³t^j 都是 S3，但除去早期 p³行因子后是单位列，完全没有新增收益。

按[K:Q]归一化后，对每个 rational p 求和的权仍是 log p，不能再乘两embedding。固定坏 p 与低幂账本沿用原稿。

## 2. 原格在 D、2D、4D 处怎样改变

下表给 p>D 的早期行因子，以及 late rows 的 modp最高层中可能出现的 blocks。source 的局部单位缩放不影响 rank。

| 固定系统与窗口 | k_p | n<p 提出的行因子 | late modp 可出现的 blocks |
|---|---:|---:|---|
| rank4，p>D |0|p³|三个 target blocks|
| rank7，D<p≤2D |2|p|L、T₂、K₂与三个 targets|
| rank7，2D<p≤4D |1|p²|T₂、K₂与三个 targets|
| rank7，p>4D |0|p³|三个 target blocks|

例如 rank7 在 D<p≤2D 时 L source 的 valuation 为−2，T₂、K₂为−1；late最高层分别来自 pL、p²T₂、p²K₂。到2D<p≤4D，L的 p²L最高层消失，而 p²T₂、p²K₂仍可贡献。到p>4D，所有 background blocks在Ψ中modp消失。不能沿用p≤D的统一每个grade成本3。

## 3. 全素数终端定理：原三层成本已被填满

假设

\[
 \boxed{p>N-D.}                                     \tag{3}
\]

对固定 m=4、7且D充分大，(3)自动使全部 source LCM成为p-units：rank4的最大尺度是D，rank7是4D，而N-D分别约3D、6D。令 ℓ=max(N−p,0)≤D，令 l 为 V_D 中 n≥p 的实际row数；p≥N时l=0，下面的结论仍成立。

冻结完整packet给 Y=p³gH 的 modp首项为 t^p·unit；g=Δ²。首系数 A(0)(1∓(5√5/4)χ(p))的范数只产生固定例外109。对每个选定late row n=p+j，选原 target shift t^jY；j≤ℓ−1≤D，所以列合法。按j排序，这些rows/columns在modp下是unit triangular矩阵。另一方面，所有early rows都在p³中。因此整行列消元严格给

\[
 \boxed{M\sim\operatorname{diag}(I_l,p^3B),\quad B\text{整}.}
 \tag{4}
\]

用于消除early rows的乘子仍在p³，故余块确实保持p³；不是仅凭rank的猜测。Smith指数由l个0及其余3+b_i组成，b_i≥0。于是

\[
 \sum_i(3-\min(a_i,3))=3l=B_p.                      \tag{5}
\]

**整个终端窗口没有任何净的三层分母消除收益，且(5)适用于任意primitive行族。** 实际可能的净收益仅为Σb_i=v(detB)，即超过三层的正Smith整除性；本文没有排除它。

特别是 t^iY，i≥ℓ 的S3性质只来自 n−i<p：保留的原系数本来就p-integral。这些列在(4)既有的S3kernel中，可扩充为其基，不能再加在early-row基线之外。除去原p³行因子后，它们一般在early rows并不为零。

helper_tensor_budget 已独立核对(4)的整消元、余块p³保持和(5)。此结论无须知道V_D的每个数值跳点，无须把O(1)遗漏误计为收益。

## 4. 真正的中间窗口接口

剩余可能的三层窗口是 D<p≤N-D。设 L 是 M 的late rows在modp下的矩阵，r_L为其rank。early rows最多增加R-l维，因此(1)的归一化矩阵满足

\[
 \boxed{\Gamma_{p,D}\ge l-r_L.}                    \tag{6}
\]

这里(6)是**净收益**：先在 \(\widetilde M\) 上得到rank defect，再估det；没有重复计原行因子。若只知道raw M有p个以上S1或S3方向，不能推出(6)的正值。

在rank4的全部p>D以及rank7的p>4D，late只含targets。(6)可化为一个不含未知周期c的明确矩阵。令

\[
 a=\vartheta A/A,\quad b=\vartheta a+a^2,
 \quad\mathcal P_{\ell,D}=
 \big([t^n]t^j,[t^n]t^ja,[t^n]t^jb\big)_
 {0\le n<\ell,\ 0\le j\le D}.                     \tag{7}
\]

完整packet为gA·F(t^p)，F(t^p)/t^p在原点为unit；ϑF(t^p)=0modp。除去这个共同unit的Toeplitz矩阵，full late rank恰是(7)的rank。a可由冻结Hasse式直接构造：

\[
 a=t(N'/N+C'/(2C)+P_p'/P_p)\quad\text{mod }p.
\]

从full prefix转到实际V_D只删O(1) rows，所以(6)给全部好素数的可用接口

\[
 \Gamma_{p,D}\ge
 \big(\ell-\operatorname{rank}\mathcal P_{\ell,D}-O(1)\big)_+.
 \tag{8}
\]

如能统一证明右边为某个正的 s(p,D)，即可按Σs(p,D)logp累计成真正新D²收益。它比收集更多raw packet syzygies更直接。本文没有证明这种positive defect。

现有全形式Hasse一阶行次数约3p/2，平方提升的二阶行次数约3p；在p>D时没有degree≤D的多项式倍数。有限jet可以有新关系，不能把全形式的一阶障碍用于排除它们。

仅按列数也没有forced D² defect：rank4的late长度约(4−p/D)D，低于3D；rank7三个窗口的可能late blocks分别有6、5、3个，late长度依次不超过6D、5D、3D。边界的O(1)偏差不产生D²主项。仍需实际rank、primitive saturation或更高Smith阶的证明。

## 5. 有限证据的最低接口与固定校验

要检验中间窗口，应输出：p,D,N及覆盖flag的依据；每个原source block的valuation；提出(1)后的矩阵；late rank与归一化determinantal ideals。若需要高于三层的收益，必须继续给B或 \(\widetilde M\) 的Smith阶，不能只给Y的最高packet。

检验(7)时完全不需选c的数值。要证明整个归一化矩阵的收益而依赖early target coefficients，则c应保留为p-integral参数；统一结果须对该参数有效，或逐系数证明所有R×R minors被规定p幂整除。某个随意c residue的数值例子不能替代反证假设下的统一结论。

[新rank-only脚本](cdt_odd_level20_large_prime_net_20261006_verify.py)只读冻结Hasse JSON，不重跑producer。四个预选例子为(p,D,N)=(7,3,16)、(11,5,24)的两个split embeddings、(13,6,28)。矩阵(7)的late长度分别为9、13、13、15，精确rank全部等于该长度，没有positive defect。另核a₁=b₁=−5、b₂−a₂=−20以检查规范。见[固定证书](cdt_odd_level20_large_prime_net_20261006_verify.json)。

这些N仅是diagnostic cutoff，不声称是全尺度Shidlovsky的完整实际flag。四例没有证明全部好p的normality，也没有证明Γ=0；它们验证最低接口并避免将维数已被baseline覆盖的kernel误记为新收益。未启动prime或D扫描。
