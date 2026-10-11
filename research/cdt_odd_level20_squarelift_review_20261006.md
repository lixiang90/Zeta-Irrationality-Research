# 平方提升、低次数第二层与原格账本的独立审核

日期：2026-10-06。审核对象是 [平方提升新稿 §§1–6](cdt_odd_level20_square_lift_20261006.md)，依据为此前已审的完整 Frobenius 比值、真实 source packet、Hasse 除子和固定一变量 Smith bridge。结论：模 p² 平方提升成立，它把已存在的第二层消去行的安全次数降到 3p+20；在固定 rank4、rank7 原格中，两个 Smith 阈值合计的已证收益主项为 5D²/6。下文不将它记为第三层，不推广到 balanced tensors，也不声明新的数值无理性结果。冻结旧稿和 producer 均未修改。

## 1. 全 polynomial 曲率输入与依赖范围

沿新稿记 ϑ=t∂ₜ，G=G_p∈Z[t]，deg G≤3p，J=(1−t)Δ，h=ϑlog g_s，𝒯=4q_proj+2ϑh+h²。对 p≥7 的好素数，完整 excellent 比值给

\[
 \Phi(t)/\Phi(s(t))\equiv G(t)\pmod{p^3},
 \qquad s=t(q(t)^p).
\]

它是完整形式级数恒等式。结合 Euler Riccati 关系，得到

\[
 \mathscr R(G)=2G\vartheta^2G-(\vartheta G)^2
             +2hG\vartheta G+\mathcal T G^2
       \equiv0\pmod{p^2}.                         \tag{S1}
\]

J(0)=G(0) mod p=1，所以清 J 后的完整 polynomial numerator 被 p² 整除；形式到 polynomial 的这一推论没有使用 n<p² 的截断 packet。后者仅在将算子应用于真实 H_± 时使用。这个区分正确且必要。

Hasse simple-zero 与 tame Fricke double cover 的已证输入给

\[
 P=G\bmod p=B H_s^2,\quad
 2d+b=3p-3,\quad d=\deg H_s,\quad b=\deg B\le4,
\]

其中 H_s monic、squarefree，且 gcd(H_s,BJt)=1。H_s 是 generic double-root polynomial；本文用下标 s 区分它与研究目标函数 H_±。这些全素数输入沿用已审的 Frobenius/Hasse 稿，不以 p=7、11、13 的有限样本替代。

## 2. 除 p 后取 residue 的合法性

取 coefficientwise integer lifts B₀、H₀，保持 deg B₀=b、deg H₀=d 且 H₀ monic。令 P₀=B₀H₀²，G=P₀+pE。则 E∈Z[t] 且 deg E≤3p。

这里不能直接将 R(P₀) 在 H_s 根上的零值除 p。需要保留整多项式的整除性。事实上，对任意 derivation δ，直接展开给

\[
\begin{split}
 \mathscr R(B_0H_0^2)=H_0^3\{&4B_0(\delta B_0)(\delta H_0)
      +4B_0^2\delta^2H_0+4hB_0^2\delta H_0\\
 &+H_0[2B_0\delta^2B_0-(\delta B_0)^2
                 +2hB_0\delta B_0+\mathcal T B_0^2]\}.
\end{split}                                                   \tag{S2}
\]

因此清 J 后 R_J(P₀) 至少被 H₀² 整除，实际被 H₀³ 整除。同时 G≡P₀ mod p 和(S1)给 R_J(P₀)∈pZ_(p)[t]。写 R_J(P₀)=H₀²V，由 F_p[t] 是整域、H₀ mod p非零可知 V∈pZ_(p)[t]。所以 R_J(P₀)/p 的 reduction 仍被 H_s² 整除。这是所需的 p-saturated 中间步骤；新稿已显式补入。

现在展开 R(P₀+pE)，除 p 再取 mod H_s。其一阶线性项是

\[
 2E\vartheta^2P+2P\vartheta^2E-2(\vartheta P)(\vartheta E)
 +2h[E\vartheta P+P\vartheta E]+2\mathcal T PE.
\]

因为 P=ϑP=0 mod H_s 且 ϑ²P=2B(ϑH_s)² mod H_s，合法获得

\[
 4B(\vartheta H_s)^2\overline E=0\pmod{H_s}.    \tag{S3}
\]

清 J 只再乘一个 unit。ϑH_s=tH_s′ 与 H_s 互素，4、B、J也可逆。因此 H_s|Ē。这是完整 polynomial 结论，而不是将 target 的有限 prefix 方程外推到其它点。

## 3. 平方提升和 bounded branch factor

令 Ē=H_sV，取

\[
 H_1\equiv V/(2B)\pmod{H_s},\quad\deg H_1<d,
 \qquad B_1=(V-2BH_1)/H_s.
\]

deg V≤3p−d，故

\[
 \deg B_1\le\max(3p-2d,b-1)=b+3\le7.
\]

将 H₁、B₁任意 lift 到整数，置 η=H₀+pH₁、β=B₀+pB₁。直接展开得

\[
 G\equiv\beta\eta^2\pmod{p^2},\qquad
 \deg\eta=d,\quad\deg\beta\le b+3.             \tag{S4}
\]

P(0)=1保证 β(0)、η(0) 是 p-adic units。β mod p² 不必仍整除 Δ；其次数可以比 b 多3。使用 deg G≤3p 的完整安全界，正好保留了这3度的余量，因而没有误用 mod p 的 degree 3p−3。

## 4. 二阶行的层数、次数和原 source

令 R=N√C、k=R/g_s，a₁=ϑlog k。用(S4)定义

\[
 a_{0,new}=\vartheta N/N+\tfrac12\vartheta C/C
            +\vartheta\beta/\beta+2\vartheta\eta/\eta.
\]

因原点所有分母为 unit，a₀,new≡ϑlog(RG) mod p²。它只需这一精度：对 Y=p³H_± 的完整 n<p² 前缀，Y及其 Euler derivatives 在好 place 整；以 a₀,new 替换旧 a₀ 只改变 p² 项，ϑ−a₁仍保留这个理想。因此

\[
 (\vartheta-a_1)(\vartheta-a_{0,new})Y
      \equiv0\pmod{p^2,t^{p^2}}.                \tag{S5}
\]

取 D₀=NCβη、M₀=D₀a₀,new、D₁=N(1−t)C_o、M₁=D₁a₁。各项是 p-integral polynomials，deg D₀、deg M₀≤d+b+7，deg D₁、deg M₁≤5。operator identity

\[
 L_2=(D_1D_0\vartheta-D_1\vartheta D_0-D_0M_1)
                        (D_0\vartheta-M_0)
     =D_1D_0^2(\vartheta-a_1)(\vartheta-a_{0,new})
\]

成立，不能将 Euler derivative 对 coefficients 的作用略掉。其三个 coordinates 的安全 degree 为

\[
 \delta_2\le2d+2b+19=3p+b+16\le3p+20.         \tag{S6}
\]

最高 coordinate 是 D₁D₀²，mod p 非零且原点为 unit。因此 degree≤D 的 polynomial multiples 给至少 (D−3p−19)_+ 个 reduction-independent primitive source vectors，image 在 p² 内。

这一行只用三个 target blocks，constant block 坐标取0，故在已冻结 E₄,D 和 E₇,D 中均直接合法。实际 target basis 使用固定 g=Δ² 时，组合输出整体多一个 g，而 source coefficients 不变：Σlᵢ(gϑⁱH)=gΣlᵢϑⁱH。这里没有消去三阶 Bol forcing，没有增添或假借廉价 constant 方向，也没有改变 source degree。模 p² 的 connection 替换不授权将新的三次链条当作 mod p³ 输入。

## 5. 两个 Smith 阈值和 D² 主项

固定实际 leading cutoff N=m(D+1)+O(1)、m=4或7。取 √N<p≤D，排除已固定的坏素数和未知有理周期分母的素因子。对 Ψ=p³eval 的 leading square minor，设 Smith exponents 为 aᵢ。

旧 Hasse 两个 primitive 一阶方向仍给

\[
 \#\{a_i\ge1\}\ge k_1
       =2(D-\delta_H+1)_+,\quad
 \delta_H\le(3p+9)/2.
\]

新行给

\[
 \#\{a_i\ge2\}\ge k_2=(D-3p-19)_+.
\]

这两族可以重叠；正确的推论是 Σaᵢ≥k₁+k₂，因为它们属于两个不同 filtration thresholds。不能额外要求或声称 k₂ 是又一组与旧族无交的 ordinary kernels，更不能把本行算成第三层。

PNT 及数域 place 的归一平均给

\[
 \sum_p k_1\log p=(2/3+o(1))D^2,\qquad
 \sum_p k_2\log p=(1/6+o(1))D^2.              \tag{S7}
\]

对应积分为 2∫₀^(2/3)(1−3x/2)dx=2/3 与 ∫₀^(1/3)(1−3x)dx=1/6。固定 degree offsets、p≤√N 的窗口和固定例外素数只改变 o(D²)。故同一个固定原格的已证收益是 γ=5/6。未处理的高度项沿用原安全上界，不涉及换格后的 source-degree 抵消。

## 6. 原 source 的完整一变量预算

原 finite 主项为 bare rank4 的51/2、rank7的84。减去(S7)，得

\[
 F_4=74/3,\qquad F_7=499/6.
\]

source Hilbert–Samuel 项保持 2J+3 与 7J/2+21；arch terms 保持 −8ρ+4J 与 −49ρ/2+7J。原 source 完全未改，所以其常数3、21不能再扣一次。完整账本给

\[
 4\rho-J\le65/6,\qquad
 7\rho-J\le373/21.                            \tag{S8}
\]

等价地，定义本固定系统专用的有效常数 κ₄=65/24、κ₇=373/147，有 m(ρ−κ_m)≤J。它们是上述固定 source、leading flag 和度量所得不等式的记法，不是替换 CDT 任意矩阵或 tensor 定理中 τ 的通用新常数。

在当前单覆盖的 ordinary Jensen 界 J≥ρ 下，要产生 m 维矛盾至少需要 ρ>65/18（rank4）或 ρ>373/126（rank7）。两者仍大于 genuine cusp 1 的 ceiling log16。因此该结构进展尚未证明未知周期无理。这个结论只针对本固定账本和该解析界；不排除新的算术行、更低 degree、不同背景或其它合法度量。

## 7. 执行和审阅记录

作者 square-lift producer 的最终记录是51个精确检查，固定 p=7、11、13、完整 polynomial coefficients；本审核未重跑该 producer，也未重做冻结 source packet。其 JSON SHA256 为 667c896a32a52ff815e53afb4a3e8b6b79d7cd92f1b1e4de98c9ebf5955099b1。

本次另执行了10项独立 symbolic/rational checks：任意 derivation 下(S2)展开、线性化 residue(S3)、两个 PNT 积分、γ 与两个 finite 主项、两个完整有效常数，以及 peer capped-cost 积分12、25。全部通过。这些核算支持明确代数恒等式与有理账本；全素数性来自 §§1–5 的证明。旧冻结审阅、第三层 producer 和 Frobenius producer 均保持原样。
