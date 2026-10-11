# Hasse–Smith 桥梁的独立审阅与一变量特殊界

日期：2026-10-06。审阅 [桥梁稿](cdt_odd_level20_hasse_smith_bridge_20261006.md) 及 [根全局稿](cdt_odd_level20_hasse_global_20261006.md) §§1–5，不修改旧文件。下述界直接推自明确的实际 rank4、rank7 source；没有数值无理性结论，不转移到 balanced tensors 或任意旧成本表。

## 1. 线性 cutoff 已闭合

取 C=Δ²，四元组为 1,g0=CH,g1=CϑH,g2=Cϑ²H。冻结模型有 H'''+a2H''+a1H'+a0H=U≠0，最小齐次阶数4。四元组若有有理关系，就给 H 一个至多二阶非齐次方程；用一个一阶算子消去 forcing，产生至多三阶齐次方程，矛盾。

直接计算
\[
\vartheta^3H=t^3U+(3-ta_2)\vartheta^2H
 +(ta_2-t^2a_1-2)\vartheta H-t^3a_0H.
\]
令 b=tC'/C，则 ϑg0=bg0+g1、ϑg1=bg1+g2，
\[
\vartheta g_2=(b+3-ta_2)g_2+(ta_2-t^2a_1-2)g_1
 -t^3a_0g_0+Ct^3U.
\]
所以实际四维 span 闭于导数。标准 Shidlovsky 零估计（[CDT v2](../literature/cdt2024_l2_chi_minus3.pdf) p52 Theorem3.2.8，同一特征零零估计的常数域 K 版本）给 maxVd≤4(d+1)+c0，c0固定。源格的非零尺度 Ld^-3 不改变 K-vector space 的 vanishing flag。Laurent sections 乘 t^d 后，target 基 t^(n-d) 对应 t^n，n标签不变。故取 Nd=4(d+1)+c、c>max(c0,0)，确实覆盖全部 primitive Taylor flag；这不再是额外假设。

## 2. 保持原格的 Smith 余量

原格及原 metric 全程保留：
\[
E_d=L_d^{-3}\mathcal O_K[t]_{\le d}\oplus
 \mathcal O_K[t]_{\le d}^{\oplus3},\qquad R_d=4(d+1).
\]
arch metric 仍是原 O(1)φ^d 的 orthogonal direct sum，不是普通 coefficient norm。对好𝔭|p、√Nd<p≤d，v𝔭(Ld)=1，Ψ=p³eval<Nd integral，且 Nd<p²。Hasse 的两关系对三个同乘 C 的 target 原样成立；它们作用于 Cϑ^jH，并非 ϑ^j(CH)。d≥δp 时，polynomial multiples 给 s=2(d−δp+1) 个独立 kernel directions，constant block=0。因此 mod𝔭 rank≤Rd−s。

Taylor filtration 是原 DVR 格与 K-linear subspaces 的交，故 saturated；各非零 quotient 自由 rank1，存在 adapted integral basis。选其 Rd 个 leading jets，Ψ 的方阵下三角，对角为 p³cj，其中 cj 是原 quotient unit generator 的 evaluation value。basis change 属于 GL_Rd(O_K,𝔭)，保持原 unit ball。Smith normal form 给
\[
3R_d+\sum_jv_{\mathfrak p}(c_j)\ge s,qquad
\sum_{n\in V_d}h_{\mathfrak p}(\psi^n)
\le(3R_d-s)\log\operatorname{Norm}(\mathfrak p).
\]
它改善原(7.3.10)累计粗界，source degree没有改变。直接换 kernel 逆像格引起的 covolume 抵消不适用于这里。

## 3. 数域归一化与素数主项

normalized degree 除以[K:Q]=2，对好p有Σ𝔭|p f𝔭=2。全部𝔭有相同保守δ界，故 gain至少
\[
G_d=\sum_{p>\sqrt{N_d}\ {\rm good}}(2d-3p-7)_+\log p
=\frac23d^2+o(d^2).
\]
PNT和partial summation给 2dθ(2d/3)−3Σp≤2d/3 p logp 的主项2d²/3。常数端点损失O(d)，删掉p≤√Nd部分至多O(d^1.5)。坏/小p原有LCM贡献全部保留；只有额外固定规范/周期分母给O(d)。固定坏p的原LCM贡献可有O(d logd)，仍由原界控制，未免费删除。

## 4. 一变量全账本

令ρbar、Jbar为embeddings上导数对数及double integral平均。原CDT(7.3.7)给
\[
\widehat{\deg}E_d=(2\overline J+3)d^2+o(d^2).
\]
#Vd=Rd且maxVd≤Rd+O(1)，因此
\[
\sum\max(n,d)=\frac{17}{2}d^2+o(d^2),\qquad
\sum n\ge8d^2+O(d).
\]
原all-prime bound为3Σlog Lmax(n,d)+O(d)。以logLk=k+o(k)统一处理 d≤k≤O(d)，仅在上述已证window扣Gd，得到
\[
\sum h_{\rm fin}\le(51/2-2/3)d^2+o(d^2)
=149d^2/6+o(d^2).
\]
原(7.3.9)给Σh∞≤(−8ρbar+4Jbar)d²+o(d²)。合法共同cover上，Δ²已清finite branch poles；闭盘邻域用φ(rz)、r<1，而不改变source metric。slopes inequality遂给
\[
2\overline J+3\le-8\overline\rho+4\overline J+149/6,
\qquad
\boxed{\overline J\ge4\overline\rho-131/12.}
\]
分母为正时，即
\[
\boxed{4\le\frac{\overline J}{\overline\rho-131/48}.}
\]
这个实际四元组的有效成本从45/16降到131/48，降低1/12；它不是一般denominator-type theorem，也不能直接改旧τ。

## 5. Scope

该bare模型仍有Jbar≥ρbar和ρbar≤log16。要得到quotient<4，必要ρbar>131/36>3>log16，故仍不给数值结论。其它source表、剩余valuation层、高阶关系和balanced tensor兼容性未由本稿排除。独立结论：原格Smith桥梁通过，所述一变量prototype的线性cutoff和全局累计记账可闭合。既有producer及预算不修改。

## 6. 根全局稿实际 rank7 的最后审核

该元组是单个target与背景结合：1,L,T2,K2,gH,gϑH,gϑ²H。它不同于两个共轭target直接合并得到的另一种rank7系统。L,T2,K2的安全型分别为ℓn、ℓn²、ℓn²，三个target为固定因子乘ℓn³。背景只含trivial/sign factors，target模常数商是simple rank3，故交空间只有常数，实际总秩7；各行导数方程亦使其闭合。上述Shidlovsky和primitive flag证明因此原样给N=7(d+1)+O(1)。

CDT原三列开启点u=(1,2,4)，取y=u，精确source为
\[
(\ell_d\ell_{2d}\ell_{4d})^{-1}\mathcal O_K[t]_{\le d}
\oplus(\ell_{2d}\ell_{4d})^{-1}\mathcal O_K[t]_{\le d}
\oplus\ell_{4d}^{-1}\mathcal O_K[t]_{\le d}^{\oplus2}
\oplus\mathcal O_K[t]_{\le d}^{\oplus3}.
\]
窗口p²>N>7d>4d且p≤d，各ℓd,ℓ2d,ℓ4d的valuation恰1。四背景source valuations为−3,−2,−1,−1；各函数prefix的val分别至少0,−1,−2,−2，故整个p³jet integral。两Hasse核方向只占三target blocks，背景blocks取0。因此同一normalized收益2d²/3真实适用，未假设两个target给双倍收益。

原全部primes的有限高度主系数是
\[
\sum_{u=1,2,4}\int_0^7\max(s,u)\,ds
=\frac{49+1}{2}+\frac{49+4}{2}+\frac{49+16}{2}=84.
\]
只减已证2/3后为250/3。HS的finite source degree为Σu²=21，因此source degree=(7Jbar/2+21)d²+o(d²)。arch累计为(−49ρbar/2+7Jbar)d²+o(d²)。slopes给
\[
\frac{49}{2}\bar\rho\le\frac72\bar J+\frac{250}{3}-21,
\qquad
\boxed{7\bar\rho-\bar J\le\frac{374}{21}}.
\]
有效成本为374/147，原该source的18/7减去4/147。它是重新核查明确source和全prime账本得到的特殊界，并不是将bare4的改进直接插入另一张成本表。只有写成quotient时才需ρbar>374/147，线性式自身不需positive denominator。

原Jensen floor及当前共同cover上界仍给必要ρbar>187/63>log16，因此仍无数值矛盾。数域归一化、源格/quotient norm、closed actual system、全prime粗界及收益窗口均通过独立审核；没有重跑或修改root/helper producer。本文在根全局稿 §§1–5 实际正文审阅后冻结。
