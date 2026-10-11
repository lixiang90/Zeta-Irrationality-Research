# D12 任意关系族：完整分母、真实反射周期与共同叶

日期：2026-10-06。新理论证明稿；不修改、执行或导入冻结producer，不扫描参数。本文补[联合触发器](cdt_odd_level12_joint_trigger_20261006.md)的两个缺口：针对同一个任意关系源，直接证明完整分母率及指定componentwise数组下界，并验证固定真实叶和整族坏反射。没有将纯L源的完整U_p身份移植给联合源，没有给新的Smith信用或数值线性无关性定理。

## 1. 同一个固定关系与实际函数

记r=√3，K=Q(r)，χ=χ12。假设
\[
A+B\zeta(3)+C L(3,\chi)=0,\qquad A,B,C\in\mathbf Z,
\quad(B,C)\ne(0,0).
\tag{U1}
\]
固定这一关系，再取已证整数源
\[
\mathcal F=B F_Z+C r F_L,\qquad
\xi=103680(B\zeta(3)+C L(3,\chi))=-103680A\in\mathbf Z.
\tag{U2}
\]
FZ的两canonical实际周期均为ΞZ=103680ζ(3)，FL的原周期为Θ=34560rL(3,χ)、共轭M周期为−Θ。于是两真实函数
\[
H=\mathcal B(f-\xi),\quad \sigma H=\mathcal B(\sigma f-\xi),
\quad f=\theta_q^{-3}\mathcal F,\quad
\mathcal B=E_2-12E_2(12\tau)
\tag{U3}
\]
分别在W与M的canonical粗点下降。坐标t(q)、q(t)全阶在O_K；H及σH满足D_n³整数模型，实际秩都恰4。σ只作用于源和已证整数ξ，没有对未知数值任意施加Galois作用。这些输入及非零关系方向的cusp秩下界在联合触发器J1–J13已证明。

## 2. 第p项的完整主部：直接Lambert系数证明

对p≥5、p∤12，写ε=χ(p)。直接正次数系数
\[
E_{4,p}=240(1+p^3),\quad E_{\chi,p}=1+\varepsilon p^3,
\quad F_{\chi,p}=\varepsilon+p^3
\]
给
\[
\mathcal F_p=\alpha_\varepsilon+p^3\beta_\varepsilon,
\tag{U4}
\]
\[
\alpha_\varepsilon=(362880B-207360C\varepsilon)+294960Cr,
\quad
\beta_\varepsilon=362880B+(292080+2880\varepsilon)Cr-207360C.
\tag{U5}
\]
这里FZ的j1系数是1512·240=362880；FL的j1普通系数为1217·240=292080，加2880Eχ、减69120rFχ。其它j|12 oldscale在prime p无系数，所以(U4)是literal equality，不是只核某个sample或借用完整Hecke packet。

对两ε，
\[
N_\varepsilon=\operatorname{Norm}\alpha_\varepsilon
=(362880B-207360C\varepsilon)^2-3(294960C)^2\ne0.
\tag{U6}
\]
若C0则由B≠0；若C≠0，等号会迫一个有理数等于±√3，矛盾。故对每一个固定非零关系方向，排除N+N−及2、3、11的有限素数后，αε在p上每个place都是unit。这个有限坏集合可以依赖(B,C)；未声称所有关系共享一个固定素数集合。

q中n<p的f系数p-integral。由于\(\mathcal B_0=-11,\mathcal B_1=-24\)，ξinteger，
\[
p^3[H(q)]_p\equiv-11\alpha_\varepsilon,\qquad
p^3[H(q)]_{p+1}\equiv-24\alpha_\varepsilon\pmod{\mathfrak p}
\tag{U7}
\]
在每个好place均成立。σ函数的主部是σ αε，同样是unit。对于这两个index，唯一三层分母项就是f_p；其它项的index不是p倍数，或由n<p的p-integral卷积给出。没有据此宣称n<p²的完整U_p packet或其第二层消除。

## 3. 完整前缀率及合法Euler行的自然数组下界

令D_n=lcm(1,…,n)。源与全阶整数反演给D_n³[H]_n∈O_K。整数unit-triangular的q↔t替换，以及\(\mathcal B_0=-11\)在所有p≠11处的unit性，使完整前缀的最小共同有理分母率保持不变。若M_n是该前缀的最小正整数分母，(U7)迫每个好p≤n有p³|M_n；结合安全upper与素数定理，
\[
\log M_n=3n+o(n).
\tag{U8}
\]
这是固定关系后的全前缀结论，不仅单个系数；σ方向相同。它不是任意混合整格的下界。

写q(t)=t+a₂t²+…，则[t^(p+1)]q(t)^p=p a₂；此前n<p项仍p-integral。因此(U7)的p+1主部在t中仍是−24αε。Euler\(\vartheta=t\,d/dt\)只把该项乘(p+1)或(p+1)²，模p均为1。

采用[完整叶](cdt_odd_level12_full_leaf_20261006.md)的实际清极点因子
\[
g_\delta(t)=(1-4a_\delta t+4t^2)^2,
\quad a_\delta=2+\delta r,\quad g_0=1,\quad g_1=-8a_\delta.
\]
三条合法行满足
\[
p^3[gH]_{p+1}\equiv(88a_\delta-24)\alpha_\varepsilon,
\quad
p^3[g\vartheta H]_{p+1}\equiv-24\alpha_\varepsilon,
\quad
p^3[g\vartheta^2H]_{p+1}\equiv-24\alpha_\varepsilon.
\tag{U9}
\]
前者含g₁H_p，其余两行在p项有Euler因子p或p²，故g₁项模p消失。Norm(88aδ−24)=−128，所以三主部全部非零。

因此每条指定Euler行的任意固定componentwise模型
\(n^{e_i}\prod_\ell D_{\lfloor b_{i\ell}n\rfloor}\)，b≥0、e≥0，要清全部系数，就至少有三个b_iℓ≥1。理由在n=p+1：n^e没有p因子；b<1的LCM对大p不含p；每个固定b的LCM此时最多含一层p。这个全尺度论证不包括任意换基或mixed Smith格，也不宣称联合源具有纯L的完整U_p swap。

## 4. 纯ζ源的额外真实零余循环

令hZ=fZ−ΞZ，hL=fσ,L+Θ。已证canonical identities给
\[
h_Z|_{-2}T=h_Z,\quad h_Z|_{-2}W=-h_Z,\quad
h_Z|_{-2}M=-h_Z.
\tag{U10}
\]
由η=WT⁻¹W⁻¹、M′=WMW⁻¹，准确得到
\[
h_Z|\eta=h_Z,\quad h_Z|M'=-h_Z,
\quad h_Z|J_n=-h_Z\quad(n\in\mathbf Z),
\quad J_n=\eta^n M\eta^{-n}.
\tag{U11}
\]
这些是实际复函数的identities；W虽不必在〈Γ,M〉内，其实际anti身份已证明，所以用它推η并非形式source对称。

联合共轭primitive准确是
\[
\sigma f-\xi=B h_Z-Cr h_L.
\tag{U12}
\]
在Γ及ΓM两源有共同sign ε；特别εJn=−1。用[完整反射族](cdt_odd_level12_signed_cocycle_20261006.md)的真实cL(Jn)，
\[
c_{B,C}(J_n)=-Cr\,c_L(J_n)
=-Cr\,i\pi^3 s_nQ_{J_n},
\quad
s_n=\frac{1920n(644n^2+552n+147)}{84n^2+48n+7}.
\tag{U13}
\]
因此C≠0且n≠0时，全关系族都保留非零坏carrier。准确实际endpoint周期是
\[
\lambda_{B,C;J_n}=\xi-Cr\,i\pi^3s_n.
\tag{U14}
\]
C=0时纯ζ方向的整族defect为0，不能将(U13)误称所有(B,C)非零都坏；但有理关系C0会与已知ζ(3)无理性冲突。本文不将已知Apéry结论计为新结果。

## 5. 全Γ的共同理性接口与关系方向的kernel

对纯ζ源，Σ_j uZj=0、Σ_j uZj/j³=−864。沿全部finite Γ∞尖点，普通Lambert pole依第一式消失，其实部依第二式恰为ΞZ；[全Γ尖点证明](cdt_odd_level12_gamma_cocycle_20261006.md)的G14普通finite polynomial及G18–G20路径/interpolation逐项适用。因此
\[
c_Z(\gamma)/(i\pi^3)\in\mathbf Q[\tau]_{\le2}
\quad(\gamma\in\langle\Gamma,M\rangle).
\tag{U15}
\]
纯L同一结论已由该稿G21–G22全尺度证明。于是整个实际群上的联合cocycle为
\[
c_{B,C}/(i\pi^3)=B P_Z-CrP_L,
\quad P_Z,P_L\in\mathbf Q[\tau]_{\le2}.
\tag{U16}
\]
若B、C都非零，1与r的有理独立性使cBC(γ)=0准确等价于PZ(γ)=PL(γ)=0。因gauge B0在该群上有同sign，实际scalar稳定子为两个真实稳定子的交。B0/C0的单周期方向分别单独处理。这个交描述没有分类任何一个完整kernel，也未从T/M/η样本推全群。

## 6. 固定共同叶和两数组的结论可用于整个关系族

(U3)与(U10)及纯L的T/M/M′ identities给全部关系族原支〈T,W〉、共轭支〈T,M,M′〉的实际下降。canonical粗点由真实anti身份保证even；其它fiber保持ordinary ram2。原点Taylor、源/gauge上半平面全纯和坐标除子与(B,C)无关，gδ清导数极点的局部order证明因而直接适用。这样闭合了这些**指定**共同叶，未分类更大的真实稳定子。

联合触发器的非零cusp log³确保每个方向实际rank4；homogeneous Sym²商与source无关、不可约。[三对数背景](cdt_odd_level12_cheap_log_packet_20261006.md)的所有composition factors为一维trivial，故与任一该目标闭包的交只有常数。两个固定合并数组实际rank仍为13/23；它们的合法分母类型及[精确运输成本](cdt_odd_level12_cheap_log_transport_20261006.md)不依赖关系系数。

[Green半径](cdt_odd_level12_hecke_radius_20261006.md)和[扩充半径](cdt_odd_level12_augmented_radius_20261006.md)也只取决于实际map，而非source系数。因此前轮的两指定plain-CDT数组在这些指定盘上失败，现对全部固定非零关系方向同样成立。此结论不排新mixed格、新背景、不同全稳定子或新的period模型。

## 7. 审阅与研究边界

本稿为纯MD全尺度证明，不另写重复实现的测试。关键数字均来自literal prime系数、已证actual periods及全Γ finite kernel；不是把已存JSON当数学主结论。conjugate_projection已实际全文只读独审，重推U4–U16、全部norm非零、p+1Euler/g、hZ的真实η/M′/Jn身份、BC稳定子交及指定共同叶/13,23数组范围，通过；按其意见将§1的整性明确限于坐标与D_n³模型，没有将H系数字面称为整。未执行producer。旧冻结文件保持原样，没有新的数值线性无关性或Lean结果。本稿在上述范围冻结。
