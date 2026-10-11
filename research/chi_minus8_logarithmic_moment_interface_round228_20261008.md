# 第228轮 χ−8：完整对数矩投影与下一项准入

2026-10-08，B；数学程序0。该对象改变普通移位 Gram 的 rank-one coefficient，但下文固定素数窗口的**全尺度纸证**说明完整 coefficient clearing 仍有至少4N²费用，应立即停止这个普通 integrated Gram 基线。下一项必须先给真正不同的 mixed contact，而非继续安全分母扫描。

χ=χ_{−8} 在模8的1、3、5、7处为1、1、−1、−1，其余为0。记

B(x)=Σ_{n≥1}χ(n)x^n/n²，L₈=L(2,χ)=B(1)，
A(x)=Σ_{n≥1}χ(n)x^n/n，a_m=Σ_{n≤m}χ(n)/n∈Q。

真实原生 branch 满足

A′(x)=(1+x²)/(1+x⁴)，B′(x)=A(x)/x，A(0)=B(0)=0。

## 1. 完整周期选择，所有 j≥1

令 J_m=∫₀¹x^{m−1}B(x)dx。B级数绝对收敛，允许积分；恒等式

1/[n²(n+m)]=1/(mn²)−1/(m²n)+1/[m²(n+m)]

给出，当 m=8j、j≥1 时，

J_{8j}=L₈/(8j)−a_{8j}/(8j)²。                           (U1)

因为 χ(n+m)=χ(n)，最后两项的完整和分别是 −A(1)/m² 和 [A(1)−a_m]/m²，A(1)精确消去。A(1)级数由角色零均值/Dirichlet收敛；移位只删除有限头项，没有非法重排条件收敛级数。这里 L₈ 的下标8不是减去8，且不把 A(1)留下作为未付的π通道。

对全部 0≤r,s<N，置 m=8(r+s+1)，

M_N(r,s)=J_m=L₈ C_N(r,s)−R_N(r,s)，
C_N(r,s)=1/[8(r+s+1)]，R_N(r,s)=a_m/m²。                 (U2)

这给出全部 off-diagonal 的精确 period-coefficient stack。C_N=(1/8)Hilbert_N 正定、rank N；det(GC_N−R_N)的degree是N，最高系数为det C_N>0，确实不同于rank-one shiftGram。

t=x⁸ 的同一实际源为

M_N(r,s)=(1/8)∫₀¹t^{r+s} B(t^{1/8})dt。                 (U3)

B(x)>0 对0<x≤1成立，所以 M_N 正定、det M_N>0 对每个N成立；不是只付有限非零。

## 2. 全部素数的安全 LCD，只给 upper

反证假设 L₈=g∈Q，固定 c_g∈Z_{>0} 清除 g 分母，d_k=lcm(1,…,k)。所有 m≤16N−8，d_{16N}a_m∈Z且 m|d_{16N}，故

d_{16N}³(GC_N−R_N)∈Mat_N(Z[G])，
c_g d_{16N}³ M_N∈Mat_N(Z)，
(c_g d_{16N}³)^N det M_N∈Z_{>0}。                       (U4)

这包含2、全部素数与prime powers；没有√2代数域/坐标缩放的漏账，因为(U1)后的全部coefficients在Q中。固定g分母也已计入。log d_k=k+o(k)给安全费用48N²+o(N²)；它只是完整upper，不是 primitive optimal lower，也不是 CDT τ。

## 3. 满秩的实际误差只在次主阶

在[0,1]，1≤(1+x²)/(1+x⁴)≤2，逐次积分给

x≤A(x)≤2x，x≤B(x)≤2x。

令 H_N(a)=(1/[r+s+a+1])，a=1/8，则实际 Loewner 界是

(1/8)H_N(1/8)≤M_N≤(1/4)H_N(1/8)，C_N=(1/8)H_N(0)。

Cauchy determinant 公式的差积 numerator在两边相同，所以

det H_N(1/8)/det H_N(0)
=∏_{r,s=0}^{N−1}(r+s+1)/(r+s+9/8)。

用 log(1+u)≤u及 Σ_{r,s}1/(r+s+1)≤2N，得到

e^{−N/4}≤det M_N/det C_N≤2^N，
N^{−2}log(det M_N/det C_N)→0。                           (U5)

因此 full-rank 本身没有 extra N² error。更明确：若任意 u_N∈Q× 完整清除 det(GC_N−R_N)的所有多项式系数，则 u_Ndet C_N 是非零整数，(U5)给 |u_Ndet M_N|≥e^{−N/4}；不能获得 exp(−δN²)。这是指定完整 polynomial scalar model 的必要 coefficient 下界，未把(U4)的48当成最优联合格费用。

## 4. 固定窗口给真正的 complete-content 必要费用

现在取任意素数 8N<p<16N，k=ceil(p/8)，q=2N−k；q=0时不贡献。m≤16N−8<2p，且m=8(r+s+1)为p-unit。a_m中唯一可能的p分母是n=p，故

pR_N(r,s) modp = χ(p)/m² ·1_{r+s+1≥k}。                 (U6)

这个 residue matrix只在最后q行/列有支撑；其q×q block以局部下标i,j从0起，支撑 i+j≥q−1，anti-diagonal的m=8k给非零unit。它是 antitriangular 的满rank q矩阵。C_N及其左上(N−q)×(N−q) Cauchy minor 都是p-unit determinant：差积的整数均<p，所有denominators≤8(2N−1)且对应的r+s+1<p。

在 F_N(G)=det(GC_N−R_N)的 G^(N−q) coefficient，恰q个R因子。乘p^q后modp的唯一最深项是（至多差一个符号）

det C_top ·det(pR_bottom) ≠0。

因为全部q个polar行/列只能选最后q行/列，其余项至少少一个pole。因此这个完整 coefficient 的valuation恰−q。若 u_NF_N(G)∈Z[G]，令b_N=det C_N，则u_Nb_N是非零整数且每个上述p都满足v_p(u_Nb_N)≥q。

log|u_Nb_N|≥Σ_{8N<p<16N}q logp
             =4N²+o(N²)。                              (U7)

最后等式用q=2N−p/8+O(1)及θ(x)=x+o(x)的分部积分，主项为∫_{8N}^{16N}(2N−x/8)dx=4N²；不是程序素数扫描。于是(U5)给

|u_NF_N(L₈)|≥exp(4N²+o(N²)−N/4)。                       (U8)

所以此**完整 polynomial scalar-clearing 源**连次主阶 primitive 高度计划也不能通过；安全48并非本论证的最优lower，必要4来自明确完整系数。固定g分母增加O(N)对数费用，不能逆转(U8)。只在假设关系值另付cancellation、修改完整系数池/矩阵或另一个 CDT源，均不在此lower量词内。

这个具体源的完整周期选择、整性upper、每N非零与必要content窗口已付；**立即停止这套普通 integrated Gram 预算**。若重启χ−8，应先交付新的mixed contact/whole-functional coefficient stack及全部nuisance projection；若走CDT，还须独立函数族、合法共同图、all-place费用。(U1)与rank N不替代这些接口。没有证明L₈无理，没有排除其它源，也不自动继承Catalan的prime flags/contact/能量。
