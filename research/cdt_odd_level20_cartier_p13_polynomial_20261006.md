# 固定 p=13 的完整 Hecke 核及多项式 Cartier source 接口

日期：2026-10-06。本文新增，不修改或运行任何冻结 producer。新的单素数 producer 已由作者执行一次，30 项检查通过。结论是 p=13 的两个完整六维矩阵模13可逆，常系数核为零。随后给出一般多项式 source 的准确分块公式；该公式没有证明新的 S1 方向存在，也没有排除所有低次数慢变量关系。

## 1. 固定素数与实际规范

使用冻结 [Hecke space](cdt_odd_level20_hecke_space_20261006.md)、[Cartier kernel](cdt_odd_level20_cartier_kernel_20261006.md) 的实际六维空间。令 r²=5、χ=χ₅、p=13，χ(13)=−1，5 在 F₁₃ 中不是平方，因此剩余域是 k=F₁₃(r)。

原始 q 坐标和 t 坐标为

\[
 t=q\prod_{d\in\{1,2,4,5,10,20\}}\prod_{n\ge1}(1-q^{dn})^{e_d},
 \quad(e_1,e_2,e_4,e_5,e_{10},e_{20})=(3,-4,1,1,-4,3),
\]
\[
 S=\theta_qt/t,\quad A_\delta=E_2+4\delta rF_2(4\tau),\quad
 N_\delta=1-(6-\delta r)t+(1-\delta r)t^2,
\]
\[
 C_\delta=1-(6+2\delta r)t+(6+2\delta r)t^2,
 \quad D_\delta=(1-t)N_\delta C_\delta,
 \quad B_j^\delta=t^jA_\delta S/D_\delta\quad(0\le j\le5).
\tag{P1}
\]

δ=−1 是原减号空间，δ=+1 是共轭加号空间。E₂,0=−1/5。程序同时将两个基乘5，所以每个基的首非零 q 系数为−1；共同缩放不改变 Hecke 矩阵。

独立构造 t 使用 Euler 对数导数递推，而不是导入旧 eta 乘积程序：若 t=qF、F₀=1，则

\[
 v_n=-\sum_{d\mid n}e_d d\,\sigma_1(n/d),\qquad
 nF_n=\sum_{a=1}^nv_aF_{n-a},\qquad S=1+\sum v_nq^n.
\tag{P2}
\]

角色 Eisenstein 系数直接用有限除数和，基函数以整数 t 级数及常数1的 Dδ 进行精确除法。工作精度是 q¹⁵⁶，预先固定的权4、level20 Sturm 界是12。对每个符号的全部六个基，程序计算

\[
 [q^n]T_{13}B=[q^{13n}]B-13^3[q^{n/13}]B,
\tag{P3}
\]

并验证 q⁰,…,q¹² 的完整身份。第二项只在13整除n时出现。目标空间符号为−δ，不能将 T₁₃ 当成某一个 Fricke 空间的自映射。

## 2. 固定 p=13 的准确结果

新的 [producer](cdt_odd_level20_cartier_p13_20261006_verify.py) 和 [JSON](cdt_odd_level20_cartier_p13_20261006_verify.json) 保存两个完整 6×6 矩阵、全部 pivot 和检查标签。列 j 是 T₁₃Bⱼ 在目标空间的基坐标。

\[
 \det T_{13}^{-\to+}
 =567286487912448+256193897766912r,
\]
\[
 \det T_{13}^{+\to-}
 =567286487912448-256193897766912r.
\tag{P4}
\]

它们在 k 中分别是 5+r 与 5−r，范数均为25−5=20≡7，而非0。因此

\[
 \boxed{\operatorname{rank}_k\bar M_{13}^{-\to+}
 =\operatorname{rank}_k\bar M_{13}^{+\to-}=6,
 \qquad\ker\bar M_{13}=0.}
\tag{P5}
\]

这是完整固定素数结论，不是由部分列或若干 q 系数猜测行列式，也不是非普通素数密度结论。故本次没有非零常系数 c₀ 可用于 mixed Bockstein 补正测试。

程序另从显式 level10 cusp u=hF/24、v=(u−hE/24)/4 独立重建基，验证该 level 的完整 Sturm 界 q⁰,…,q⁶，得到

\[
 T_{13}\big|_{S_4(\Gamma_0(10),\chi_5)}=
 \begin{pmatrix}0&-6\\24&0\end{pmatrix}=6T_3.
\tag{P6}
\]

仅在可选谱分量检查中只读冻结 T₃ JSON，不执行旧脚本。T₁₃² 在 Eisenstein、old cusp、new cusp 三分量分别为

\[
 4822416=(1-13^3)^2,\qquad-144,\qquad-2736.
\tag{P7}
\]

这三项也是模13的单位；P5 已由独立完整矩阵直接验证，不依赖谱分量推断。

## 3. 多项式 source 的精确剩余类分块

令原 rank19 source 的六个积分列为 Iⱼ；共同原格规范允许把最高 packet 写成

\[
 \bar\Psi(I_j)=g(t)\sum_{i=0}^5\bar M_{p,ij}\bar\Xi_i(t^p)
 \pmod{t^N},\qquad\Psi=p^4\operatorname{eval},\quad g(0)=1.
\tag{P8}
\]

这是 n<N≤p² 的 prefix 身份。Ξ 保留完整 Af carrier，且使用已冻结的 relative k-linear Cartier 规范。g 是同一个实际原格因子；左乘其形式逆只用于评价矩阵的秩比较，不改变 source 的多项式次数或整格。

对 cⱼ(t)∈k[t]、deg cⱼ≤D，唯一写成

\[
 c_j(t)=\sum_{a=0}^{\min(D,p-1)}t^aC_{j,a}(s),\quad s=t^p,
 \quad\deg C_{j,a}\le K_a:=\left\lfloor\frac{D-a}{p}\right\rfloor.
\tag{P9}
\]

相应的慢变量 prefix 行数是

\[
 M_a:=\left\lfloor\frac{N-1-a}{p}\right\rfloor.
\tag{P10}
\]

因为全部 Ξᵢ(0)=0，慢变量第0行没有约束。令 H(K,M) 的列为 (i,l)，0≤i≤5、0≤l≤K，行 m=1,…,M，条目为

\[
 H(K,M)_{m,(i,l)}=[s^{m-l}]\bar\Xi_i(s),
\tag{P11}
\]

负次数系数取0。则六积分 source 的完整 S1 条件恰为各剩余类分别满足

\[
 H(K_a,M_a)(I_{K_a+1}\otimes\bar M_p)\,\mathbf c_a=0.
\tag{P12}
\]

列次序可改为先 i 后 l，只须同步置换。不同 a 的 fast 次数集合不相交，故核是这些块的直接和。若 \bar M_p 为单位，块秩就是 H(Kₐ,Mₐ) 的秩；若不是单位，必须计算复合矩阵，不能将 native kerM 和后续 polynomial convolution 核重复相加。

特别地，P5 不排 p=13 的 polynomial kernel，只排 K=0 的常系数 kernel。

## 4. p≤D 不会仅因重叠自动给出新 S1

取 full leading prefix 足够长 N≥19(D+1)，并保留 N≤p² 的 packet 条件。令 k₀=⌊D/p⌋≥1。对全部 a≤p−1，有

\[
 M_a\ge\left\lfloor\frac{19D+19-p}{p}\right\rfloor
 \ge19k_0-1\ge18k_0,
 \qquad K_a\le k_0.
\tag{P13}
\]

每块只有6(Kₐ+1)列，而

\[
 M_a\ge18k_0\ge6(K_a+1).
\tag{P14}
\]

因此这里没有由“未知数多于方程数”强迫出的核。模 p 指数余类中的 shifts 发生重叠，只是把常系数矩阵换成 P11 的 convolution 矩阵。新的 S1 必须来自真实 polynomial slow syzygy 或有限 prefix rank defect。

一个总能写下的完整多项式关系是 Ξⱼ(s)eᵢ−Ξᵢ(s)eⱼ；使用 degree<p 的慢变量截断时，它的 fast 次数可能达到 p(p−1)。在 p²>N≈19D 的窗口，这个直接构造没有统一落在 source 次数 D 内的保证。这里没有声称所有 syzygy 的次数至少 p²；更短的真实关系仍是待研究的正接口。

若另证明这里的完整实际 Ξ 六列在 C(s) 上独立，则对每个预先固定 K，某个有限 H(K,M) minor 在特征零非零，因而除有限坏素数外仍非零。但该有限排除集及 M 可以依赖 K。不能从一个 constant-coefficient minor 自动得到这一 rational-coefficient 独立性，更不能推广成 K随D/p增长时的统一 mod p 秩下界。相同伴随 L* 的有理解排除与最少项微分引理是可核的入口；本段不以该入口代替完整 carrier 的实际证明。

## 5. 原格、层数与下一步范围

P12 是原六积分 polynomial source 的第一层 mod p 条件，包含全部 prefix；它没有把 mod p 身份除 p 升成 S2/S3。其它13个 species 在共同 p⁴ 规范下已有第一层 floor，它们对 P12 的最高 residue 为0；S1 计数须与这些背景 baseline 及行 baseline 在同一原格比较。

若另构造 ∫R(t)H(t)dt/t，不能直接把它等同于 Σcⱼ(t)Iⱼ：微分后还有 cⱼ′Iⱼ。任何 integration-by-parts、Hermite reduction 或改变 primitive 都须保留实际 source 坐标及分母。仅把 rational relation 清分母至多给出一个新的安全次数上界，不自动给原格的净 Smith 信用。

可执行的正接口是：在 P12 的准确 Toeplitz 块中证明一个 degree≤Kₐ 的真实 relation，并验证它与既有 baseline 的商空间中仍 primitive。当前没有这种全尺度 relation；本次固定 p=13 也没有非零常系数方向可启动原 B11。

## 6. 执行与审阅范围

新 producer 只选择 p=13，作者本轮单次执行30项检查；没有素数扫描、数值周期近似、旧 producer 导入或执行。完整 Sturm 验证是基于冻结实际模形式空间及其整数基的固定 q 计算，不宣称从 finite jets 得到新的全素数定理。

P9–P14 为全尺度线性代数接口，独立于本次数值素数；它们不保证 kernel 为空或非空。root已实际只读全文 P1–P14及新 producer，限定审阅通过，未执行 producer；依其意见将导言明确为模13可逆，并把最后的固定 K 一般化写成需要完整 C(s)-独立性证明的条件句。该审阅不将一个 constant minor 解释成所有 polynomial degrees 的统一证明。本次记录后冻结本文及单次执行的 PY/JSON，不再运行 producer。
