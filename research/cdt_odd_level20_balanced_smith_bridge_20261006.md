# 固定原格 Smith 收益进入 CDT 第八节的均衡张量

日期：2026-10-06。本文新建，冻结旧稿不改。结论是一个限定但已闭合的兼容接口：对 level20 的实际三目标 rows，第一、第二层 polynomial relations 可以进入 CDT §8.2 的近似均衡 species 空间。累计有限高度的归一收益是 γ/m，其中 γ=5/6；完成斜率账本后有效成本才下降 2γ/m²。这不是将单变量 τ 直接代入张量定理。本文先证明两个已核单位表，再给 e=0 的任意数组在一个明确 matching 窗口内的推广。尚无新的数值无理性结果。

## 1. 必须使用的真实 source

原件为 [CDT 固定218页版本](../literature/cdt2024_l2_chi_minus3.pdf)。第129页 (8.2.2) 是

\[
 E_{D,d,\epsilon}=\bigoplus_{i\in V_m^d(\epsilon)}
       f_i\,O_K[t_1,\ldots,t_d]_{\deg_{t_j}\le D},
 \quad f_i=\prod_j f_{i_j}(t_j).
\tag{B1}
\]

已将 Laurent sections 统一乘 ∏t_j^D，并保留原 product L² metrics。这里所有 polynomial coefficients 都整；不能把 [一变量全局稿](cdt_odd_level20_hasse_global_20261006.md) §3 的分母缩放 source 原封不动张量。

V_m^d(ε) 要求每个 species 次数在 d/m±εd，ε>0 固定。令 U_D=⊕_{i=1}^m O_K[t]≤D、R=m(D+1)，则(B1)是 U_D^⊗d 的 primitive coordinate submodule。其 rank q=(D+1)^d #V_m^d(ε)，codimension c=R^d−q，并有

\[
 \eta_{d,\epsilon}=c/R^d=O(e^{-c_\epsilon d}).          \tag{B2}
\]

先固定 d、ε 令 D→∞，再令 d→∞，最后 ε↓0，正是 §8 的顺序。§6.2 的 exact-balanced species 空间只有约 d^{−(m−1)/2} 的比例，而且还限制 polynomial degree vectors；不能用(B2)将以下证明直接移到 §6。

## 2. 最小可复用的 DVR 引理

设 O 为 DVR，A∈M_R(O) 在 fraction field 上可逆，Smith exponents a_i≥0。若已知整数 floors 0≤b_i≤s、b_i≤a_i（按同一 SNF 顺序），令 T=A^⊗d。取任意 primitive submodule E⊂O^{R^d}、rank q、codimension c。若 B 是 T|E 的任何可逆 q-row minor，则

\[
 v(\det B)\ge dR^{d-1}\sum_{i=1}^R b_i-sdc.         \tag{B3}
\]

证明：tensor SNF 的指数是 ∑_j a_{i_j}，certified floors 是 ∑_j b_{i_j}≤sd。对 1≤ℓ≤sd，在 tensor SNF 整基中取 floor≥ℓ 的 basis vectors 所张成的 saturated S_ℓ。其 rank h_ℓ 为该 floor 条件的 tuple 数，且 T(S_ℓ)⊂p^ℓO^{R^d}。S_ℓ∩E 在 E 中 saturated，rank≥h_ℓ−c；其 primitive vectors 的 image 在全部 rows 中被 p^ℓ整除，故在 B 的 rows 中也一样。B 至少有 (h_ℓ−c)_+ 个 Smith exponents≥ℓ。累加至 sd，并用

\[
 \sum_\ell h_\ell
 =\sum_{i_1,\ldots,i_d}\sum_j b_{i_j}
 =dR^{d-1}\sum_i b_i
\]

即得(B3)。不要求局部 SNF basis 保持 species，也不要求不同 ℓ 的子空间互不相交。这正是绕过局部关系混合 H、ϑH、ϑ²H 三种 species 的方式。

## 3. 实际 leading rows 和本地 floors

采用已审闭合独立元组 F₄=(1,gH,gϑH,gϑ²H) 或 F₇=(1,L,T₂,K₂,gH,gϑH,gϑ²H)，g=Δ²，反证假设 L(3,χ₅)∈Q。Shidlovsky 给一变量 leading set V_D 的 #V_D=R、V_D⊂[0,N_D)，N_D=m(D+1)+O(1)。

完整 tensor space 的 leading set 是 V_D^d：一变量 adapted basis 的其余 terms 均在其 leading exponent 之后；tensor 的 leading tuples 各不相同，total-order+lex order 与 componentwise order 相容。对 subspace E，其 leading jumps 是完整空间的子集，所以 V_bal⊂V_D^d。因此 balanced 的实际 leading square minor 是 A_D^⊗d 的 row/column restriction，其中

\[
 A_D=p^3\operatorname{eval}_{V_D}(U_D)
\]

在好 place 整。p>√N_D 即确保每个 coordinate 的全部所需 packet prefix 在 n<p²；不需要 p² 超过 dN_D。令 D_H≤(3p+9)/2，新平方提升行 D₂≤3p+20，则

\[
 k_1=2(D-D_H+1)_+,\qquad k_2=(D-3p-19)_+.
\tag{B4}
\]

它们是原 pure target blocks 中的 primitive directions，分别给 image p 和 p²。多项式次数损耗已包含在(B4)，不是免费 tensor ranks。

pure U_D 的 background floors 还必须恢复：constant block 的 image 在 p³，L block 在 p²，T₂、K₂ blocks 在 p。它们的 source supports 与 target directions 不同。因此可选 0≤b_i≤3 使

\[
 \sum_i b_i=B_m(D+1)+k_1+k_2,
 \quad B_4=3,\quad B_7=7.                         \tag{B5}
\]

具体三个 threshold counts 为：rank4 的 (D+1+k₁,D+1+k₂,D+1)；rank7 的 (4(D+1)+k₁,2(D+1)+k₂,D+1)。这等价于原一变量缩放 source 的成本，但现在是在第八节实际整数 source 内证明的。

由(B3)和 primitive leading flag 的 determinant identity，balanced 累计有限高度在本窗口满足

\[
 \sum_{n\in V_{bal}} h_p(\psi^{(n)})
 \le\{3dq-dR^{d-1}[B_m(D+1)+k_1+k_2]+3dc\}\log\operatorname{Norm}\mathfrak p.
\tag{B6}
\]

这里是对整个 actual flag 的累计估计；没有声称每个 leading coefficient 单独改善。

## 4. 与原 denominator transport 的 baseline 接合

两个单位 e=0 表的 row costs σ 分别为 (0,3,3,3) 和 (0,1,2,2,3,3,3)。原 CDT matching 在 x=p/D∈[0,1] 的 cap 恰为 d∑σ_i/m：将 zero species 配到 normalized exponent n/D 的 [0,1] 段，其它 species 顺序配到 [1,m]，所有 positive columns 均 active。这就是 (8.0.2) 的 admissible transport，不是另外创造一个成本。

为严谨处理有限 discrepancy，先取 p≤(1−δ)D、δ>0 固定，再选 species tolerance 和 exponent discrepancy 足够小。边缘 ((1−δ)D,D] 的损失是 O(δ) 的归一主项，最后 δ↓0。mean row costs 为9/4、2，且 3−B_m/m 正好等于这些值。把(B6)与 q=(1−η)R^d比较，baseline 差至多 O(η dR^d)；由(B2)，该差求 p 后在 d→∞ 消失。

因此这一步从 CDT 第八节真实累计有限高度 bound 中扣去的是

\[
 \lim_{d\to\infty}\lim_{D\to\infty}
 \frac{dR^{d-1}\sum_p(k_1+k_2)\log p}
      {dm^dD^{d+1}}
 =\frac{\gamma}{m},\quad\gamma=\frac23+\frac16=\frac56.
\tag{B7}
\]

式(B7)的 γ/m 是高度归一常数。2γ/m² 只在最后的 rank inequality 归一后出现。小素数、高幂、坏素数、其它 p 窗口使用原 cap；其新的固定例外在 D→∞ 只是 o(D^{d+1})。不换 source，故没有 source-degree 下降与收益抵消。

## 5. 第八节完整公式及凸性接口

先用普通 Bost–Charles metric或(8.0.4)。第130页 Lemma8.2.5 的 source HS normalized degree 为 J/2；第91页 Definition7.1.2明确 That(1)=J。第140页 (8.2.28) 的 arch term为 −mρ/2+J−Q/(2m)，其中 Q=Σ_h(ΔThat_h)²/Δlog r_h，普通 metric取Q=0。第141–143页原 finite 项是 mτ/2，现在变成 mτ/2−γ/m。斜率不等式的归一主项逐项为

\[
 \bar J/2\le-m\bar\rho/2+\bar J-\bar Q/(2m)
                  +m\tau/2-\gamma/m.
\]

乘2、移项，得到 mρ≤J−Q/m+mτ−2γ/m。普通 metric即

\[
 m\left(\bar\rho-\tau+\frac{2\gamma}{m^2}\right)\le\bar J.
\tag{B8}
\]

故保留原 (8.0.4) 的 numerator，得到

\[
 m(\bar\rho-\kappa_m)\le
 \overline{J-\frac1m\sum_h
       (\widehat T(r_h)-\widehat T(r_{h-1}))^2/
                         (\log r_h-\log r_{h-1})},
\]

对(8.0.5)，必须同时保留更换后的 source HS，不能仍写 J/2。第143页结尾要求 L′=∏_h L_rh^s_h；它只更换 Hermitian metric，底层 O(1)及全部 finite source 不变。按第114–115页(7.6.1)–(7.6.3)，设 H′=L′·L′、C_k=L′·L_rk、β_k=(C_k−C_{k−1})/Δlog r_k。product HS为H′/2；arch residual为

\[
 \frac1m\sum_k[(\beta_{k+1}-\beta_k)C_k
             -\tfrac12(\beta_{k+1}^2-\beta_k^2)\log r_k].
\]

因此乘2后的原 numerator为2C_l−H′−m^{-1}Σ_kβ_k²Δlog r_k。若原 stationary条件成立，β_{k+1}−β_k=ms_k*，summation by parts使该 numerator精确为C_l=L′·L₁=Σ_hs_h*That(r_h)。加入本有限收益只再减2γ/m，于是

\[
 m(\bar\rho-\kappa_m)\le
 \overline{J-\sum_{h<l}s_h^*(\widehat T(1)-\widehat T(r_h))},
 \qquad\kappa_m=\tau-2\gamma/m^2.
\]

这同时对照了原HS与arch变化；没有把新metric的degree遗漏。每个 embedding 用合法实际共同 φ；closure/holonomicity 已证，故无需自动 holonomicity 的较强前提。两种 convexity 的所有原条件仍必须满足。

单位表给 κ₄=45/16−5/48=65/24、κ₇=18/7−5/147=373/147，与一变量账一致；这次一致是(B1)–(B7)推导的结果。已审 corrected numerator floor≥ρ 仍使必要尺度超过 log16，因而兼容性缺口闭合并未直接给新无理性定理。

## 6. e=0 任意数组的限定推广

可把以上接口用于新的 fractional 表，但需先核 matching 窗口。假设目标三 rows 的真实类型是三 unit columns，其余列为0；每个其它 row 的全部安全型为固定常数乘 ∏_h L_floor(b_i,h n)，e_i=0。令

\[
 \nu_i=\#\{h:b_{i,h}>0\},\quad s=\max_i\nu_i\ge3,
 \quad\theta_i=\max_{b_{i,h}>0}1/b_{i,h},
\]

zero row 取 θ_i=0。此窗口明确要求至少一个zero row（当前目标系统均含常数1）；把 θ 按非降序排序后 θ_(1)=0。若没有zero row，下式窗口只能取a₀=0，不能跳过第一个positive θ后宣称有正窗口。设

\[
 a_0=\min_{i\ge2,\theta_{(i)}>0}(i-1)/\theta_{(i)}.
\tag{B9}
\]

对于 p≤a₀D，给第 i 个 species 配 n/D∈[i−1,i]，使所有 positive columns 都 active；故原 τ♭♭ transport cap 在该窗口正好是 d∑ν_i/m。对 finite discrepancy 仍用严格内窗和最后极限。

采用 pure matrix p^s eval，background baseline floors 是 s−ν_i，target baseline 是 s−3；target 新关系额外提供 thresholds s−2、s−1 的 k₁、k₂。全 floor 和为 [sm−∑ν_i](D+1)+k₁+k₂，且 floor≤s。以(B3)的 sdc 代替3dc，完全相同证明给

\[
 \kappa=\tau^{\flat\flat}(b)-2\gamma(a)/m^2,
\quad a=\min(a_0,1),
\]

\[
 \gamma(a)=2\int_0^{\min(a,2/3)}(1-3x/2)\,dx
           +\int_0^{\min(a,1/3)}(1-3x)\,dx.       \tag{B10}
\]

p²>(max b_i,h)N_D 的下界仍只删 O(√D) 的 primes。a₀≥2/3 就保留完整 γ=5/6。该充分条件不声称包含任意 e_i>0 类型；后者的序号因子与原 τ♯ 分割必须重新接合。

例如 [已冻结 arithmetic actual 表](cdt_odd_level20_arithmetic_20261006.md) 中单目标 q3 的 B₃、B₄、B₅、B₄+K₂L 四个数组均有 a₀=1：T_j 的 θ=j，K₂ 的 θ=1，K₂L 的 θ=2；目标 θ=1。原表真实 τ♭♭ 和新 κ/必要尺度分别为

| fixed system | m | original τ♭♭ | κ after γ=5/6 | Jensen necessary ρ |
|---|---:|---:|---:|---:|
| B₃+target3 |8|167/64|31/12|>62/21|
| B₄+target3 |9|2597/972|859/324|>859/288|
| B₅+target3 |10|1369/500|2041/750|>2041/675|
| B₄+K₂L+target3 |10|1087/400|3241/1200|>3241/1080|

都仍大于29/10>log16。这里只复用四张已完整核算的 transport 表，不重跑 producer，不以 comonotone 下界替代真实 τ，也不自动处理 Q-joint 的六目标 basis。

## 7. 核验、剩余范围与最小执行接口

root 已独立认可(B3)的 saturated intersection 证明和 V_bal⊂V_D^d，并要求明确(B7)的归一化及严格内窗极限；本文已遵照处理。low_period_closure指出(B9)跳过i=1须显式要求zero row，本文已补充；四张固定表均满足。另逐行对照原PDF pp130、140–143、122–124及pp114–116，补出了(8.0.5)改变metric后的真正HS项。最终限定只读独审已完成：conjugate_projection通过实际§§2–3的DVR、leading和背景/目标阈值合并；low_period_closure通过实际§§4/6的原transport baseline、严格内窗与归一化；root通过§5的原PDF HS/archmetric归一化。各审阅者均未重跑本文producer，未以这些限定审阅代替其它部分的证明。配套 [脚本](cdt_odd_level20_balanced_smith_bridge_20261006_verify.py) 与 [证书](cdt_odd_level20_balanced_smith_bridge_20261006_verify.json)通过42项固定精确检查，仅核有限 floor generating-function identities、积分、有理常数和四个 fixed matching inputs。没有计算未知 L 值、没有 prime/parameter 搜索；全尺度结论来自本文证明。

最小可执行 lemma 是(B3)：给出实际 one-variable full jet matrix 的 certified capped Smith floors、full tensor leading set、balanced primitive source codimension，并比较该 prime window 的原 transport baseline。若这四个条件不齐，不能代入 τ 改进。当前已闭合第八节 near-balanced、e=0、列明目标三 rows 的接口；exact-balanced 第六节、e_i>0 fine types、Q-joint 六目标的完整局部系统，以及一般不同 degree/species filters 仍需各自证明。本文不建立第三层，也没有改变真实解析 cover 的容量上限。
