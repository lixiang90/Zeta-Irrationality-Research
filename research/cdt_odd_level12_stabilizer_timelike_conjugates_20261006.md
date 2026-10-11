# D12：严格定二次型 translation 排除已知保持群的全部共轭

日期：2026-10-06。独立新纯Markdown证明，不改任何冻结输入，不运行旧或新producer、不搜索word/参数。使用[完整真实整数affine作用](cdt_odd_level12_generator_cocycle_20261006.md)与[已证自由因子](cdt_odd_level12_stabilizer_structure_20261006.md)。

令纯L的actual signed cocycle为cL(g)，K_L=cL⁻¹(0)，H0=〈T,M,M′〉⊂K_L。对basis(1,τ,12τ²)定义

\[
 b_g=\epsilon(g)c_L(g)/(80i\pi^3),\qquad
 \rho_g=\epsilon(g)R_g,\qquad
 \mathsf A_g=\begin{pmatrix}\rho_g&b_g\\0&1\end{pmatrix}.
 \tag{T1}
\]

这些是同一个真实hL/B0hL的affine action；归一后的b_g是real rational/integer quadratic，非替代目标的formalmodule。右作用准确满足A_(g1g2)=A_g2 A_g1。二次型“严格定”指齐次p0Y²+p1XY+12p2X²在所有非zero实(X,Y)上严格同号，等价普通系数的判别式<0且非zero最高系数。

## 1. 全g、全H0的共轭排除定理

\[
 \boxed{b_g\text{严格正定或负定}
 \quad\Longrightarrow\quad K_L\cap gH_0g^{-1}=\{1\}.}
 \tag{T2}
\]

证明先准确保留right action：对h∈H0有b_h=0，且

\[
 \mathsf A_{ghg^{-1}}=\mathsf A_g^{-1}\mathsf A_h\mathsf A_g.
 \tag{T3}
\]

所以实际scalar B0hL保持ghg⁻¹，准确当且仅当

\[
 \mathsf A_{ghg^{-1}}(0)=0
 \quad\Longleftrightarrow\quad
 \mathsf A_h(b_g)=b_g
 \quad\Longleftrightarrow\quad\rho_hb_g=b_g.
 \tag{T4}
\]

此处0是affine三维原点；A_g(0)=b_g，不用未正规化c_g替代。

任意det>0 real Möbius matrix的normalized weight−2 polynomial slash R_h由可逆real variables替换并乘正det倒数，因而分别保存严格正/负定锥。

若ε(h)=−1，则ρ_h=−R_h互换这两个锥，不能固定严格定b_g。

若ε(h)=+1，则h∈H0∩Γ，ρ_h=R_h。Γ=PSLΓ1(12)已由完整Schreier/Bass–Serre证明为torsionfree discrete Fuchsian group。若R_h保存严格正定二次型（负定情况先取反），则把该型变成X²+Y²后，normalized determinant1 matrix h属于SO(2)，即h为identity或elliptic。非identity elliptic在discrete Fuchsian group中必为有限order：否则其powers在compact SO(2)中有identity积聚，违反discreteness。torsionfreeΓ因此迫h=1。

两种sign均已处理，(T4)遂只在h=1时成立，证明(T2)。此证明同时作用于H0中全部hyperbolics、parabolics和signed elliptic/其它odd元素，不靠有限word检查。

## 2. 已证符号一致无限词族的直接应用

冻结freefactor稿(S16–S18)给

\[
 g=h_0a_1^{n_1}h_1\cdots a_r^{n_r}h_r,\quad
 h_i\in H_0,\quad a_i\in\{x_4,x_5,x_9\},\quad n_i\ne0.
\]

若所有ε(prefix before ai)sign(ni)相同，则cL(g)/(iπ³)是同一个严格定锥内的若干nonzero summands之和；所以b_g也严格定，(T2)适用。因而不仅g本身不在K_L，而且它携带的整个conjugate H0除identity外，均不能包含任何真实zero元素。

这包括全部positive extra字、插入任意even-sign H0块，以及(S18)允许的其它prefixsign/幂方向组合。它不是把“每个generator nonzero”误升成“所有reducedwords nonzero”。

联合实际模型C≠0且同时有两项时，其保持群已经证明为KZ∩KL，故上述排除也适用于该intersection；纯L单项目标同样直接适用。这里没有变更未知周期的Galois规范或Taylor整数模型。

## 3. 精确边界与仍未闭合的稳定子

本定理要求b_g严格定。对indefinite型，R_h的固定群可能含hyperbolics；对nonzero null型，可能含parabolics；对b_g=0，H0的全部共轭反而由(T4)保持原点。因此不能将(T2)外推到所有nonzero translations。

已经展示的P4−P5是indefinite，说明相反signed项确实可能落到本定理范围以外。本稿没有分类那些indefinite/null orbit points，也没有证明KL=H0。一个全kernel分类还须处理这些points对knownH0的线性fixedspaces的交，以及并非共轭knownfactor的其它mixed normal forms。

此外(T2)是实际离散群的origin statement。它不把纯粹free-factor malnormality替代period证明，不给CDT Taylor–Smith或capacity免费收益，也不宣布任何新的数值无理性。

## 4. 实际审阅状态

root已实际阅读全文§§1–4，独立复核(T3)的right conjugation、(T4)原点固定条件、negative sign反转定锥、positive sign的compact SO(2)+离散torsionfree论证、(S18)整族应用，以及indefinite/null/zero的范围，限定审阅通过。没有producer、finite verification或word scan；证明只使用两个冻结实际输入及严格定二次型的compact stabilizer事实。本文据此冻结；后续indefinite或完整kernel工作另建稿。
