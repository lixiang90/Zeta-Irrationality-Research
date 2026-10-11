# level20 Cartier 核的全素数三维 Hecke 源空间

日期：2026-10-06。本文新建，既有冻结稿不变。正结论把 [原 degree5 核](cdt_odd_level20_cartier_kernel_20261006.md) 的每个符号下六维候选空间收紧为一个固定三维空间：这来自实际 Eisenstein／old cusp／new cusp 分解及 Hecke–Fricke 交换式，适用于所有 p∤20，不是从有限 p 拟合。本文不声称新的 Smith 层或数值无理性。

## 1. 实际六维基和全局整性

沿用 r=√5、K=Q(r)、χ=χ₅、t、S 及 A±。为避免混淆，此处下标 δ=−1,+1 表示 A₋、A₊；其 Fricke eigenvalue 分别−1、+1。定义

\[
F_\delta=A_\delta S,\quad
D_\delta=(1-t)N_\delta C_\delta,\qquad
\mathcal B_j^\delta=t^jF_\delta/D_\delta\quad(0\le j\le5).
\tag{H1}
\]

原除子证明不仅控制 Hecke 比值：它也说明每个 Bⱼ 都是 holomorphic weight4、characterχ、Fricke eigenvalueδ的实际模形式。N 与 ownC 的分母由 F 的零抵消；t1 cusp亦抵消；otherC处分子仍有一阶零；∞时 j≤5 使比值有限。六个芽分别从 −qʲ/5 开始，故独立。

X₀(20) genus1、index36、六 cusp、无 elliptic points，χ在各 cusp stabilizer上平凡。weight4的模形式线丛degree12；尖点形式线丛degree6。genus1 Riemann–Roch 给
\[
\dim M_4(20,\chi)=12,\qquad \dim S_4(20,\chi)=6.
\tag{H2}
\]
H1的两个符号各六个独立形式因此给完整Fricke eigenspace基。

更强的整性不需要新的p-local分母：5A±∈O_K[[q]]且constant−1，S∈Z[[q]]且constant1。5Fδ/Dδ的全部q系数整。算术Hecke也保持O_K系数，因此在缩放基5Bⱼ中所有好Tₚ的两个6×6矩阵都在O_K中；这是leading coefficients为−1的逐项三角回代。原核同时满足
\[
P_p\in O_K[t],\quad\deg P_p\le5,
\tag{H3}
\]
而非只有在p处整。这里仍要求p∤20，并沿用原稿实际符号匹配。

## 2. 尖点旧空间的显式基，而非猜测谱数据

以下E₂、F₂表示χ₅的weight2 Eisenstein源，E₂(∞)=−1/5、F₂(∞)=0；E₂^{ord}是普通quasimodular Eisenstein series。令
\[
S_d=dE_2^{ord}(d\tau)-E_2^{ord}(\tau),\qquad d=2,5,10.
\]
它们是level10的holomorphic weight2平凡角色形式。构造
\[
C_E=E_2(-5S_2-S_5+S_{10}),\qquad
C_F=F_2(-S_2-5S_5+5S_{10}),
\]
\[
u=C_F/24,\qquad v=(C_F-C_E)/96.
\tag{H4}
\]

在cusp c=1,2,5,10，三个S_d的常数分别为
\[
(-1/2,-4/5,-9/10),\quad(1,-4/5,-3/5),
\quad(-1/2,4,3/2),\quad(1,4,9).
\]
E₂仅在5|c时有非零常数，F₂仅在5∤c时有非零常数；H4两括号在对应两cusp均为零。因此u、v确实是尖点形式，其开头为
\[
u=q-4q^4-5q^5+4q^6+23q^9+20q^{10}-28q^{11}+\cdots,
\]
\[
v=q^2-q^3-5q^5+13q^7-4q^8-5q^{10}+4q^{12}+\cdots.
\tag{H5}
\]

X₀(10) genus0、index18、四cusp与两个order2 elliptic points。在两个elliptic stabilizers的lower-right residue是3或7 mod10，χ取−1；weight4的几何因子取+1，所以每处强制一个odd local zero。valence6扣除两处总weighted zero1及四cusp后，coarse尖点线丛degree1。Riemann–Roch给dimS₄(10,χ)=2，H5两不同首阶故为完整基。相同计算在level5给coarse尖点degree−1，故S₄(5,χ)=0。χ的conductor5排除其余低level尖点源。

对H4使用完整Fourier公式，q⁰…q⁶足以核身份；这里level10的valence/Sturm bound为6。得到实际全函数恒等式
\[
T_3u=4v,\quad T_3v=-u,
\qquad T_3|_{S_4(10,\chi)}=\begin{pmatrix}0&-1\\4&0\end{pmatrix},
\quad T_3^2=-4I.
\tag{H6}
\]
这不是把一个有限prefix当成所有coefficients相等：差已知属于同一个weight4 level10空间，valence使ord∞>6的差必为零。

level20的u(q),v(q),u(q²),v(q²)独立（确定q⁰…q¹²的矩阵rank4）。Atkin–Lehner–Li分解故给四维old cusp空间与二维new cusp空间。标准原始输入见 [Stein作者快照](../literature/stein_modular_forms_computational_author.pdf) PDF173–174／印刷159–160，§9.2、Theorem9.4及其character版。这里只用好Hecke与degeneracy maps相容和new/old直接和，不用未知L值或未经核实的数据库标签。

## 3. 全p约束来自commutant，不来自额外取样

两种χ₅ Eisenstein家族在level20的六个oldforms为E₄(dτ)、F₄(dτ)，d=1,2,4；它们的六cusp常数矩阵rank6，故与S₄的交为零并给完整Eisenstein空间。对p∤20，完整divisor-sum身份给
\[
T_pE_4(d\tau)=(1+\chi(p)p^3)E_4(d\tau),\quad
T_pF_4(d\tau)=\chi(p)(1+\chi(p)p^3)F_4(d\tau).
\tag{H7}
\]
特别T₃在这两个families上的scalar为−26、+26，故T₃²=676I。

全部好Hecke彼此交换，且W_NT_p=χ(p)T_pW_N。H6的T₃有distinct±2i eigenvalues，所以S₄(10,χ)上的任意好Tₚ属于二维commutant CI+CT₃。W₁₀交换式于是强迫
\[
T_p=a_pI\quad(\chi(p)=1),\qquad
T_p=b_pT_3\quad(\chi(p)=-1)
\tag{H8}
\]
在整个level10尖点空间成立；aₚ、bₚ∈Q由H4的有理q基及Fourier操作得到。两个degeneracy copies亦使用同一scalar，故H8适用于level20四维old cusp空间。并不要求W₁₀本身有有理q矩阵。

在H1的actual六维基中，固定T₃从δ到−δ，其平方的精确characteristic polynomial为
\[
\det(X-T_3^2)=(X-676)^3(X+4)^2(X+76).
\tag{H9}
\]
该矩阵由Hecke Fourier公式算出，q⁰…q⁵唯一确定完整函数；另外核到q¹²作为独立规范检查。Eisenstein每Fricke号三维，old cusp每号二维（T₃ invertible且反交换W₂₀），所以剩余的每号一维就是new cusp。H9因此给new空间上T₃²=−76I。它在完整new二维空间亦有distinct eigenvalues；同样的commutant与W₂₀交换论证给H8形式（其aₚ、bₚ当然不必等于old空间的值）。old的Fricke稳定性也可直接核：k4的规范给W₂₀α₁f=4α₂W₁₀f、W₂₀α₂f=(1/4)α₁W₁₀f。Petersson正交new空间于是亦被unitary W₂₀与全部好Hecke保持。

故所有p∤20，在三个实际直接和块Eisenstein、old cusp、new cusp上，Tₚ各自只是一个scalar乘I或T₃。三个块的T₃² eigenvalues是
\[
\lambda_E=676,\qquad\lambda_O=-4,\qquad\lambda_N=-76.
\tag{H10}
\]

## 4. 当前源的三个固定方向与六维循环模

取真正源F₋=A₋S。用全空间上的固定polynomial projectors
\[
\Pi_j=\prod_{k\ne j}\frac{T_3^2-\lambda_k}{\lambda_j-\lambda_k},
\qquad F_j=\Pi_jF_-,\quad j=E,O,N.
\tag{H11}
\]
它们分别属于三个实际块。F₋在B₀⁻,…,B₅⁻中的坐标就是D₋的六个polynomial coefficients。精确矩阵给
\[
\operatorname{rank}(F_-,T_3^2F_-,T_3^4F_-)=3,
\]
\[
(T_3^2-676)(T_3^2+4)(T_3^2+76)F_-=0.
\tag{H12}
\]
三projected components因此全部非零且独立；新JSON保存它们的完整固定coordinates与T₃后的正号coordinates，不只保存rank摘要。

H7–H10对任意好p给
\[
T_pF_-\in\begin{cases}
\langle F_E,F_O,F_N\rangle_K,&\chi(p)=1,\\
\langle T_3F_E,T_3F_O,T_3F_N\rangle_K,&\chi(p)=-1.
\end{cases}
\tag{H13}
\]
由于T₃²在各块非零，两号三个方向都独立。它们合成实际六维好Hecke循环模；projectors与T₃已在好Hecke代数中，所以维数是恰六，不是只有上界。

除以匹配的F₋或F₊，得到原Cartier比值Rₚ在每个符号下属于一个固定三维rational-kernel子空间。各固定方向仍以Dδ清分母，numerator degree≤5。谱投影仅有固定分母，统一清一次即可；不能把Pₚ全局整性误读成每个谱坐标在所有places均为unit。

这里不额外声称single-prime images的span恰为三维：H12证明的是完整好Hecke代数循环空间，H13对每个prime给上界。二者的区别保留。固定T₇T₃及T₁₁稳定性是额外检查，未被用来推断其它prime。

## 5. 对真实积分与Smith路线的作用和边界

这个结果将无限p的候选核从两个六维空间收紧到两个三维空间，提供固定的实际Eisenstein／old／new basis。其用途是让modp primitive消元与period-carrier匹配成为一个明确有限维问题，而非重新扫描每个p。

[实际cohomology稿](cdt_odd_level20_cartier_cohomology_20261006.md)的无exact类证明若通过，则每个这样的三维子空间给三个实际新H积分方向；[共同leaf稿](cdt_odd_level20_cartier_primitive_leaf_20261006.md)证明其正规H积分仍有共同完整叶及nD_n³分母。但真实Cartier primitive是Jᴴ+εΘJᴬ，ΘJᴬ不能删除。H13没有证明modp²/³提升，也没有把三kernel directions算成Smith rank。

## 6. 核验范围

[新独立脚本](cdt_odd_level20_hecke_space_20261006.py)及[JSON](cdt_odd_level20_hecke_space_20261006.json)含57项固定exact checks：integer eta t、两sign×六basis×三指定primes的完整q¹²比较、level10显式cusp基和valence足够的T₃身份、old四基独立、六Eisenstein与全cusp常数rank、两commuting operators、固定谱projectors及源Krylovrank。旧producer未import或执行。全p结论依赖本稿的空间维数、实际old/new分解、Hecke交换与commutant证明，有限checks只证明这里明确列出的固定身份，不代替全p逻辑。

helper_tensor_budget 已对实际正文 §§1–4 作限定只读独审，并回读 Stein PDF173–174 的 character old/new 输入：RR的elliptic角色、显式cusp括号、old两copies上的同一I/T₃、new二维commutant、Eisenstein两family比值、全p三维核与六维循环模均通过。conjugate_projection亦独立核同一理论链，特别区分Eisenstein直接系数身份与仅凭T₃²谱不足的推论。两者未执行57check生产器，也未把有限prime稳定性当成全p证明；该审阅不宣称任何新Smith收益。
