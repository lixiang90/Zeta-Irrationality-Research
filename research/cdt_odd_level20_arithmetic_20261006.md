# level20 的 Q-trace：实际 rank7、三层过滤与完整低成本背景

日期：2026-10-06。本稿新建，旧稿冻结。它把 [真实共轭周期投影](cdt_odd_conjugate_projection_20261005.md) 接到 Q 系数模型和算术账本。仍未得到 L(3,χ₅) 无理性或新的线性无关性。原文的数域入口及已有闭合系统已接实，但列出的单map表受到新的严格Jensen障碍，尚无capacity矛盾。

## 1. 精确规范与几何输入

置 \(r=\sqrt5\)、\(K=\mathbf Q(r)\)、\(c=L(3,\chi_5)\)。反证假设是 \(c\in\mathbf Q\)，不能擅改成 \(c\in K\)。写
\[
 E=E_2(\tau),\quad F=F_2(4\tau),\quad
 u=\theta_q^{-3}\{E_4-5E_4(2\tau)+4E_4(4\tau)\},
\]
\[
 v=\frac54\theta_q^{-3}\{F_4-20F_4(2\tau)+64F_4(4\tau)\},
\qquad u(0)=v(0)=0.
\]
则真实两芽为
\[
 H_-=(E-4rF)(u-rv+5rc/16),\quad
 H_+=(E+4rF)(u+rv-5rc/16).                              \tag{1}
\]
这仅对已明确的代数系数施加共轭；原文的 Mellin/Fricke 恒等式分别证明两个实际周期，不假设未知超越数有 Galois 作用。

根分支给整数双向坐标 \(t=q-3q^2+4q^3-\cdots\)，来自
\[
 h=\frac{\eta(4\tau)^2\eta(5\tau)^2}
 {\eta(\tau)^2\eta(20\tau)^2},\quad t=1/(h+1).
\]
η 单位展开和 leading coefficient1 的形式反演给 \(t(q),q(t)\in\mathbf Z[[q]]\)。后续算术论证只依赖此整数双向性质。所用判别式为
\[
 \Delta=16t^4-32t^3+28t^2-12t+1=16C_-C_+,\qquad
 C_\mp=t^2-t+(3\mp r)/8.                               \tag{2}
\]

以下 actual rank 依赖 [完整几何模型 §§4–7](cdt_odd_level20_model_20261006.md)，而非有限 jet：每个 \(H_\pm\) 的四阶闭包 \(\mathcal W_\pm\) 有常数核，其非平凡商 \(\mathcal N_\pm\) 是共同 Sym²(SL2) 的二次字符扭曲；两者不可约、rank3，gauge 平方分别为有理平方除以本稿 monic \(C_-\)、\(C_+\)（完整模型采用常数项1的 \(C_\pm\)，标签相反、差固定倍数）。未消 cusp 的 log³ 项使两个扩张均非分裂。几何稿的全局 cusp/Bol/module 证明须保留，配套算术证书不代替它。

两商不相同：\(C_\pm\) 各有两个简单根、无共同根，故 \(C_-/C_+\) 不是 \(K(t)\) 中的平方。共同 rank3 底模的 determinants 相同，twist 后 determinant 比值正是此非平凡二次字符（3为奇数），所以不可能同构。因此
\[
 \mathcal W_-\cap\mathcal W_+=K(t)\cdot1,\qquad
 \dim_{K(t)}(\mathcal W_-+\mathcal W_+)=7.               \tag{3}
\]
共同底模在 Γ₀(20) 上的稠密 SL2 monodromy 是这里 irreducibility 的必要输入；仅看到平方根多项式不能推出它。

## 2. Q-trace 与 difference 均保留真实目标

定义
\[
 T=H_-+H_+=2Eu+40Fv-\frac{25}2Fc,
\]
\[
 J=\frac{H_--H_+}{r}=-2Ev-8Fu+\frac58Ec.                \tag{4}
\]
在假设 \(c\in\mathbf Q\) 下，两者均为实际 \(\mathbf Q[[t]]\) 芽，且在选定 Fricke 叶同时正则。

trace 的原点常数确为0，但目标未丢失：\(F=q^4+\cdots\)，故 trace 在 q⁴ 项保留 \(-25c/2\)。difference 的常数为 \(-c/8\)。因而不能只读 trace 的 q⁰ 项就声称目标消失，也不能以差值的有理常数反推无理性。

**单独 T、J 的 cyclic rank 都为7。** 它们到 \(\mathcal N_-\oplus\mathcal N_+\) 的投影分别为 \(([H_-],[H_+])\)、\(([H_-]/r,-[H_+]/r)\)，两分量均非零。这里 \([H_\pm]\) 是实际微分闭包模去常数的类，不能把实际芽直接等同于齐次 ODE 的某个 solution \(A_\pm\)。互不同构的两个 simple differential modules 的 direct sum 中，这样的 cyclic vector 生成全 rank6 商。

若该 cyclic span 只有rank6，它便在联合 rank7 空间中给常数核的补空间，导致联合扩张分裂。其两个 rank3 simple summands 各自的 preimage 又使 \(\mathcal W_\pm\) 分裂，矛盾：Sym² 的 cusp monodromy 至多 log²，split constant+Sym² 也不可能产生已核实的非零 log³。所以必须rank7。对 trace 的商上六阶最小算子将 T 映入非零有理函数；因此
\[
 (1,T,\theta_tT,\ldots,\theta_t^5T)                     \tag{5}
\]
是 Q(t) 上实际独立基。对 J 同理。这给 Q 系数入口，实际 rank 是7；既不是免费保留rank4，也不是按两embedding直接计rank8。

## 3. 全素数三层 packet 与全部固定 mixed 基下界

置 \(\kappa=5r/4\)。对充分大 \(p\nmid10\)，各源的最高 packet 系数是 \(1\mp\kappa\chi(p)\)，其范数 \(-109/16\) 排除了除109之外的零素理想。对整数坐标反演，Frobenius 仍给 \(q(t)^p\equiv t^p\bmod(p,t^{2p})\)。因此
\[
 p^3[t^{p+s}]T\equiv[t^s](2E+50\chi(p)F)\pmod p,
\]
\[
 p^3[t^{p+s}]J\equiv[t^s](-8F-\tfrac52\chi(p)E)\pmod p. \tag{6}
\]
尤其 \(E_1=1,F_1=0\)，所以 p+1 层分别为2与 \(-5\chi(p)/2\)：真实 trace 不取消最高三层。

完整安全型为固定常数 \(D_c L_N^3\)，包括全部前缀和全部素数；\(D_c\) 清固定规范及反证假设 c 的分母。源系数整、θ⁻³ 分母 n³、乘固定整 Fourier 芽并经过整数双向坐标，足以逐项证明此型。θ_t 的非负整数幂不增加系数分母。

任意固定 Q(t) mixed 行可写 \(P(T)+Q(J)+a(t)\)。在每个 \(\chi(p)=\epsilon\in\{\pm1\}\) 的素数类，最高 packet 是
\[
 C_\epsilon=(1-\kappa\epsilon)(P+Q/r)A_-
             +(1+\kappa\epsilon)(P-Q/r)A_+.            \tag{7}
\]
式(7)是在最高 packet 上应用固定微分算子后的表达式。完整模型有显式 \(\mathcal L_{3,\pm}H_\pm=U_\pm\in K(t)\)、\(\mathcal L_{3,\pm}A_\pm=0\)。rank3 不可约使 \([H_\pm]\) 与 \(A_\pm\) 的 annihilator 都正好是同一个 minimal \(\mathcal L_{3,\pm}\)，从而 \(P[H_\pm]\mapsto PA_\pm\) 给实际 quotient 到 cyclic A-module 的明确 differential isomorphism。若该行到 rank6 商的投影非零，(7) 不可能是有理常数：两个商独立、各为非平凡 irreducible，不含 trivial factor；两前系数也非零。对每个 \(\epsilon\) 选一个固定非零 offset \(s_\epsilon\) 的非零 Taylor/Laurent 系数。排除固定有理 gauge 的有限坏素数后，在所有该类充分大素数上得到精确三层。这里无需挑选有利 primes，也没有在 primes 上搜索。

固定 \(n^e\) 在 \(n=p+s_\epsilon\) 是 p-unit；固定尺度 \(b<1\) 的 LCM 列最终不到p，任何尺度列在该位置最多一次p。因此任意非constant quotient 行的必要 scales 有三个 \(b\ge1\)，即 \(\sigma\ge3\)。联合rank7 的任意固定合法基中，至多一行是纯 rational；所以
\[
 \boxed{\tau^\flat\ge3(1-1/7^2)=144/49.}               \tag{8}
\]
固定有理 gauge 在有限坏素数处的额外成本不能免掉；(8) 只给必要下界，不宣称任意 gauge 自动保留原安全型。

## 4. 一个真正可用的 Q-rank10 低成本完整表

加入背景 \(1,L,T_2,K_2\)，其中 \(L=-\log(1-t)\)、\(T_2=L^2/2\)，K₂ 取 [已证规范](cdt_odd_algebraic_helpers_20261005.md)。该背景实际rank4、trivial/sign factors，与联合模型的交仅常数：非平凡rank3商不可能落入这类背景。因此选定
\[
 1,\ L,\ K_2,\ T_2,\ T,\theta T,\ldots,\theta^5T
\]
实际 rank10。完整安全类型全部 \(e=0\)，σ行序为
\[
 (0,1,2,2,3,3,3,3,3,3).
\]
只用三个单位scale列，依次在 L、K₂、第一个目标行开启；每列为零前缀与固定常数尾。\(T_2\) 用固定2清因子及 \(L_N^2\) 清，K₂ 用已证 \(L_N^2\)。没有 fractional 列兼容性缺口，全部 sharp 成本为0。因此
\[
 \boxed{\tau^{\rm safe}=279/100=2.79.}                 \tag{9}
\]
只加 L,K₂ 的rank9表是 \(229/81\)；加入T₂确有净收益。

对这个明确元组，分别允许 L、T₂ 的 e=0或1，四张合法 unit-column 表的完整 flat+sharp 成本为：

| \(e_L,e_{T_2}\) | flat | sharp | total |
|---|---:|---:|---:|
|0,0|279/100|0|279/100|
|0,1|137/50|19/100|293/100|
|1,0|69/25|19/100|59/20|
|1,1|271/100|57/200|599/200|

这里 sharp 由 CDT Definition6.0.1 的实际分段有理积分取得；不能只比较 flat。更大 fixed e 对该单位表不降 scales，故没有净收益。上述为四张明确可行表的比较，未宣称任意 fractional columns、其它 gauge 或新背景的最优值。

原文 Theorem6.0.2 的 (6.0.3)，PDF第66页，明确要求每列为零前缀后固定正值尾；只有非递减仍不够。例如先用 \(1,1/2,1/3\) 清 T₃、之后把同列的 \(1/2\) 升为1清K₂，再把 \(1/3\) 升为1清目标，不能直接套该定理。合法修复必须保留 fractions 并另开 unit列，K₂行和变为17/6、目标行和23/6；背景 \(1,L,T_2,T_3,K_2\) 接Q联合模型的rank11成本是2501/726，接单K模型的rank8成本是595/192。因此未把此 varying-positive-columns 矩阵的weighted row sum低成本当成6.0.2的合法输入。

但 **Theorem8.0.1，PDF122–123页，已经允许任意矩阵**；此时必须用 (8.0.2) 的 \(\tau^{\flat\flat}\)，不能用weighted row sums。对上述背景加 q 个三层目标、给 K₂ 额外增加 \(1/3\) 安全成本的三列矩阵，行依次为
\[
 (0,0,0),(1,0,0),(1,\tfrac12,0),
 (1,\tfrac12,\tfrac13),(1,1,\tfrac13),
 \underbrace{(1,1,1),\ldots,(1,1,1)}_{q\text{ 行}},
\]
精确计算给
\[
 \boxed{\tau^{\flat\flat}_{q=3,m=8}=257/96,\qquad
 \tau^{\flat\flat}_{q=6,m=11}=1039/363.}                 \tag{11}
\]
q3 的 comonotone weighted sum121/48只是下界，不能用作成本。式(11)的实际成本均高于此前合法unit表18/7和279/100。

为证实 (11)，把 (8.0.2) 的极限写成 \(2\int_0^1M(x)\,dx\)。\(M(x)\) 是species行质量各1/m（重复目标合并为q/m）、坐标u为[0,1]均匀质量的最大transport payoff \(\sum_h1_{\{x\le b_{i,h}u\}}\)。六种行在四段u区域 \(u<x,\ x\le u<2x,\ 2x\le u<3x,\ u\ge3x\) 的payoff分别为
\[
 (0,0,0,0),(0,1,1,1),(0,1,2,2),
 (0,1,2,3),(0,2,2,3),(0,3,3,3).
\]
四段质量为 \(x,\min(2x,1)-x,(\min(3x,1)-\min(2x,1))_+,(1-3x)_+\)。固定有理分点划分成q3的32段、q6的44段。每段保存两个端点的可行primal flow及一套共同整数dual；端点primal值与同一dual值相等，线性插值便在整段证明最优，无需从浮点拟合推断分段线性。

species/discrepancy极限与该transport完全对应：任意balanced离散点的极限给合法coupling及upper；任意有限interval coupling可用有理网格和整数配额逼近，保留species平衡和坐标discrepancy趋零，给lower。payoff只有有限阈值，边界为Lebesgue零测，故积分极限成立。逐列单独最大给同一安全upper，q3三项为63/64、15/16、145/192，q6三项为120/121、117/121、328/363；完整primal/dual证明这些upper确能同时达到。

**删掉 K₂ 的多余 inflation，及真正 T₄/T₅/K₂L 背景。** 固定背景为
\[
 \mathcal B_R=(1,L,T_2,\ldots,T_R,K_2),\qquad T_j=L^j/j!.
\]
有限个这些函数在 Q(t)、K(t) 上均独立：已证 K₂、L 的代数独立排除了多项式关系。其闭包由 \(T_j'=T_{j-1}/(1-t)\) 和 K₂ 的已证一阶递推给出，trivial/sign factors 与两个 rank3 target quotients 的交仍只有常数。因此接单 K 模型时实际 rank 为 R+5，接 Q-joint 模型时为 R+8。再加 K₂L 的情形也独立、闭合，因为其导数只另用 K₂、L²。

T_j 的全部前缀安全清型是固定 \(j!\) 乘
\(\prod_{h=1}^jL_{\lfloor N/h\rfloor}\)：乘积系数的 j 个指标排序后第 h 个至多 N/h。K₂ 的型仍为 \(L_N^2\)，所以在 R 列中用 \((1,1,0,\ldots,0)\)，无需额外 \(1/3\)。K₂L 用已证 product 型 \(L_N^2L_{\lfloor N/2\rfloor}\)，即 \((1,1,1/2,0,\ldots,0)\)。三层 target 用 \((1,1,1,0,\ldots,0)\)。所有表均 e=0；缺列均填0。

以下六张固定表按 Theorem8.0.1 的真实 transport 得到精确成本。各行 species 质量1/m，q个重复 targets 合并质量q/m。阈值区域为 \(kx\le u<(k+1)x\)、\(0\le k<R\)，及 \(u\ge Rx\)，payoff 是本行 scales 满足 \(b u\ge x\) 的数量。

| 实际背景与目标 | m | comonotone 下界 | 真 \(\tau^{\flat\flat}\) | plain Jensen 必要 \(\rho\) |
|---|---:|---:|---:|---:|
| \(\mathcal B_3\)，单K，q3 |8|475/192|167/64|>167/56|
| \(\mathcal B_3\)，Q-joint，q6 |11|988/363|340/121|>34/11|
| \(\mathcal B_4\)，单K，q3 |9|797/324|2597/972|>2597/864|
| \(\mathcal B_4\)，Q-joint，q6 |12|1553/576|4937/1728|>4937/1584|
| \(\mathcal B_5\)，单K，q3 |10|926/375|1369/500|>1369/450|
| \(\mathcal B_4+K_2L\)，单K，q3 |10|999/400|1087/400|>1087/360|

这些数字由 [actual-table producer](cdt_odd_level20_transport_actual_20261006_verify.py) 和 [全部区间 primal/dual 证书](cdt_odd_level20_transport_actual_20261006_verify.json) 独立证明；不把 comonotone 下界当清分母成本。特别是 T₄、m9 表的 naive 必要量797/288略小于log16，但真实量2597/864严格大于3，关闭这一微小窗口。这里是六个明确完整系统的校准，不是所有背景、所有 gauges 或所有算术类型的最优性断言。

这些背景也通过解析入口：对 holomorphic φ 且 \(1\notin\varphi(D)\)，\(L\circ\varphi\) 及所有 T_j 单值 holomorphic；K₂ 满足
\[
 \frac d{dz}K_2(\varphi(z))=
 \frac{\varphi'}{2(1-\varphi)}K_2(\varphi(z))+
 \frac{\varphi' L(\varphi)}{\varphi(1-\varphi)}.
\]
后项在 \(\varphi=0\) 可去，系数在 simply connected D 上 holomorphic，故原点的实际 K₂ 芽唯一延拓到全盘。其有限乘积也 holomorphic。此证明不借用齐次 solutions \(A_\pm\tau^j\) 的 G-invariance。

当前解析端只需给 **同一合法 φ 的**
\[
 J(\varphi)<10(\log|\varphi'(0)|-279/100)               \tag{10}
\]
便能与实际rank10冲突。它是新的明确研究门槛，尚未验证 (10)；正分母本身也不是完成证明。

## 5. Norm 是另一真实芽：不免费计 rank

令 \(N=H_-H_+=(T^2-5J^2)/4\)。在 c∈Q 假设下它有Q系数、真实 Fricke 正则性，常数为 \(-5c^2/256\)。目标现在是二次，不是原来的线性 period coefficient。

两H的 \(L_N^3\) 安全型经 convolution 给
\[
 D_c^2\,L_N^3L_{\lfloor N/2\rfloor}^3
\]
（必要时乘固定4归一化），安全和9/2：排序两个指标，一个至多N、另一个至多N/2。最高 packet 则为
\[
 p^6[t^{2p+s}]N\equiv-\frac{109}{16}[t^s]A_-A_+\pmod p.
\]
\(A_-A_+=E^2-80F^2\) 的 t¹项为 \(-2/5\)，因此在2p+1有六层 residue109/40。这要求六列 \(b\ge1/2\)，给必要 \(\sigma\ge3\)，和安全9/2不同。

未作进一步结构辨识时，N的 cyclic closure 严格嵌于 \(\mathcal W_-\otimes\mathcal W_+\)，故rank至多16。如果完整几何的共同 Sym² gauge 输入已核实，则初始 \(A_-\otimes A_+\) 属于 Sym⁴ 最高权分量（rank5），而非全 rank9 tensor商；其preimage kernel rank7，进一步给 cyclic rank≤12。这里不宣称实际等于12，也不把形式 tensor 的16或9作为新独立函数数。需给独立rank证明后才可建完整Norm表；这一路线暂不排除。

## 6. 原文已有的数域入口与已闭合系统的限定引理

若保留单个 K-rank4 模型，不先Q-trace，在K上加同一背景 \(1,L,T_2,K_2\)，实际K-rank7，全部unit列/e0的算术数是
\[
 \tau^{\rm safe}_K=18/7,
\]
低于Q-trace rank10的279/100。原文 **Remark8.2.42，PDF143页，明确给数域版本**，两处archimedean收益和capacity共同平均；字面条件 \(\overline\rho>\sigma_m\) 用于先推出holonomicity。在已经证明闭合微分系统的情形，可使用Theorem8.0.1的已holonomic分支及Remark8.2.41，避免重复这一步。

**限定数域引理（e=0、已有闭合系统、任意非负矩阵）。** 设 \(f_1,\ldots,f_m\in K[[t]]\) 为K(t)独立的闭合微分系统。固定共同清因子后，系数具有OK整模型及Theorem8.0.1的固定非负 b表，成本 \(\tau=\tau^{\flat\flat}(b)\)；constant-tail类型是 \(\tau^{\flat\flat}=\tau^\flat\) 的特例。对每个 \(\sigma:K\to\mathbf C\)，取合法holomorphic \(\varphi_\sigma:D\to\mathbf C\)，0映到0且导数非零；各拉回必须holomorphic，或其全部极点能由一个固定K[t]多项式的共轭在φ像中清除（固定offset不改变τ）。置
\[
 \overline\rho=\frac1{[K:\mathbf Q]}\sum_\sigma
 \log|\varphi_\sigma'(0)|,\qquad
 \overline J=\frac1{[K:\mathbf Q]}\sum_\sigma J(\varphi_\sigma).
\]
若 \(\overline\rho>\tau\)，则
\[
 \boxed{m\le\frac{\overline J}{\overline\rho-\tau}.}       \tag{12}
\]

证明按原文§8.2逐项：以OK直和替换Z的balanced auxiliary lattice，在各embedding赋予各φ的Bost–Charles metric。Arakelov degree按[K:Q]归一化，使(8.2.28)中的archimedean项变为 \(-m\overline\rho/2+\overline J/2\)。rational LCM清型在p的全部prime ideals满足 \(\sum_{\mathfrak p\mid p}e_{\mathfrak p}f_{\mathfrak p}=[K:\mathbf Q]\)，所以归一化后的非arch估计仍为原(8.2.34)的 \(m\tau^{\flat\flat}/2\)。任意矩阵直接保留(8.0.2)的 balanced maximum；数域替换不改这些计数。constant-tail表由Remark8.0.6给 \(\tau^{\flat\flat}=\tau^\flat\)，e=0没有sharp。固定清因子只有O(d)贡献，除以dD后消失。

已有闭合微分系统提供数域Shidlovsky的functional order界（原文Remark8.2.41），给同一leading-exponent分布；故不需要André准则从 \(\overline\rho>\sigma_m\) 新推holonomicity。OK上的斜率不等式及Hilbert–Samuel项正是Remark8.2.42已给的数域proof。收集两项并取原文相同极限，得到 \(\overline J\ge m(\overline\rho-\tau)\)，即(12)。这限定引理是原文已holonomic分支的逐项数域推广，不另声称自动holonomicity；不处理任意未知meromorphic pole集合，也不把未核实的φ当合法。

本项目K-rank7、τ18/7及§4各单K任意矩阵表均符合算术与闭合系统输入；两个系数embedding分别就是实际H−、H+。[完整叶报告 §8](cdt_odd_level20_leaf_20261006.md)已证明同一 full G cover 对两embedding实际芽合法，target derivatives 的有限branch poles由固定 \(\Delta^2\) 清掉，§4背景也都合法。尚未得到足够严格的capacity收益，不能只取有利embedding。

## 7. Jensen 给当前单map公式的额外必要门槛

正分母不是capacity成功。对在闭盘邻域holomorphic的任意非constantφ、φ(0)=0，两次Jensen给
\[
 \int_{\mathbb T}\log|\varphi(z)-\varphi(w)|\,d\mu(z)
 \ge\log|\varphi(w)|,\qquad
 J(\varphi)\ge\log|\varphi'(0)|.
\]
边界有限零点可取径向极限，log奇点可积。逐embedding平均得到 \(\overline J\ge\overline\rho\)。因此未采用convexity修正的(12)若要strictly小于实际m，必要条件是
\[
 \boxed{\overline\rho>\frac m{m-1}\tau.}                \tag{13}
\]
K-rank7/τ18/7需要 \(\overline\rho>3\)；Q-rank10/τ279/100需要 \(\rho>31/10\)；inflated arbitrary矩阵的K-rank8/τ257/96也需要 \(\overline\rho>257/84>3\)。§4最后六张 actual 表的严格必要量已列于表中，全部大于log16；最小167/56也大于 \(29/10>\log16\)，其余五个都大于3。因此简单添加 T₄、T₅ 或 K₂L 并使用这些完整清型没有突破plain门槛。

[实际叶报告 §6](cdt_odd_level20_leaf_20261006.md)证明：保留原点唯一preimage、避开真log cusp1的holomorphic cover有 \(\rho\le\log16<3\)。故这些明确单map表连完整capacity必要门槛也过不了。这个普通Jensen论证本身不自动覆盖凸性修正。

另有 [独立凸性报告 §§3、4、6](cdt_odd_level20_convexity_20261006.md)分别处理真实修正项：CDT §7.1 的合法 slope 修正、§7.6.4 的非负 stationary weights，以及全部 univalent maps 的 raw §7.6.2 weights，其 corrected numerator 仍 \(\ge\rho\)。因此本稿上述各表在这些明确公式下也受同一必要门槛，不能通过再优化这些修正获救。这里仍不排除 nonunivalent raw metrics、binomial metrics、一般多map、不同返回原点规则、真period商或其它更便宜背景；若允许meromorphic φ有极点，Jensen需计pole项，且真实cusp∞的log³仍必须处理。

## 8. 精确证书范围与尚缺的最后环节

配套 [脚本](cdt_odd_level20_arithmetic_20261006_verify.py) 和 [证书](cdt_odd_level20_arithmetic_20261006_verify.json) 核固定 trace/difference恒等式、quadratic twist方程、整数坐标jet、两预选prime类的完整packet、norm六层、全部前缀安全型、rank10四张exact预算，以及K/Q成本比较；[transport脚本](cdt_odd_level20_transport_probe_20261006.py)和[完整primal/dual证书](cdt_odd_level20_transport_20261006_verify.json)独立覆盖(11)的全部区间；[actual-table脚本](cdt_odd_level20_transport_actual_20261006_verify.py)和[六表证书](cdt_odd_level20_transport_actual_20261006_verify.json)覆盖删inflation后的六张完整表。它们不从有限展开认定 actual rank，也不计算未知L值小数。数域引理及Jensen不等式由正文证明，程序只核相应精确常数与门槛。

本稿补出的可执行输入是Q-trace实际rank7与6个三层方向、rank10安全成本279/100，以及限定数域引理。已有完整几何证明还须接到能跨过§7障碍的新背景或未覆盖的metric/多map界，才能得到新的数值结论。保留Norm及更多真正背景是后续方向；没有把未验证的capacity或field Galois假设计入证明。

