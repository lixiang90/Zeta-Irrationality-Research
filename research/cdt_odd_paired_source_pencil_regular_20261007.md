# 原配对格第一源 pencil 的完整 regularity 判据与实际二阶 tail 接口

2026-10-07，NEW，/root/source_pencil_finalize。前轮518冻结记录只读；本轮本人旧/同行数学程序 execute、import、rerun均0，NEW数学producer执行0，不扩辅助单位素数表。保留原B6/k3/s5、degree<3n、饱和rank2n配对格、fixed rational source ξ=αζ4+βζ5（β≠0）及whole-X行列式。本文是全尺度线性代数和实际精度接口，尚未证明新的特殊值无理性定理。

## P1. 实际 first residual 的输入

实际完整读取冻结[源响应稿](cdt_odd_paired_source_radical_response_20261007.md)S1–S14、[局部Gram稿](cdt_odd_paired_actual_local_gram_layers_20261006.md)G1–G15及[单bordered稿](cdt_odd_paired_single_bordered_nonzero_gate_20261006.md)B1–B8。取n=4r、p=18r+1素数、F=F_p，避开fixed rational source的有限分母及β的素因子。actual exact paired局部basis满足

\[
p^5B_{\alpha,\beta,X}=D_pN_{\alpha,\beta}(X)D_p,
\quad D_p=\operatorname{diag}(1^{5r},p^{3r}),
\quad \overline N=6\bar\beta\mathcal A_5. \tag{P1}
\]

令K=ker A5，k=dim K≤2r，T为其basis的任意整lift。消去leading的已知unit补空间后，真正first Schur residual Rα满足

\[
\boxed{\overline R_\alpha=A+8\bar\alpha G,\quad
A=\overline R_0,\quad G=T^t\mathcal E^tD\mathcal ET.} \tag{P2}
\]

源响应稿已经证明E|K单射，也已经指出这不能推出G非退化。其S14还给rank G≤2rank(θ:K→F^r)。本文不将未知A删掉或自由指定；它必须来自actual exact paired lift及literal β-source。

## P2. 一般 symmetric pencil 的递归消元

**定理P3（完整 regularity staircase）。** 设F为char≠2的任意域，A、G为d阶对称矩阵。以下只除已经确认非退化的常数块和满秩交叉块；算法在有限步终止，并准确判定det(A+tG)是否为零多项式。

1. d=0时det=1。若G非退化，则det(A+tG)的degree恰d，算法以regular终止。
2. 若G退化，取V=U⊕W，W=rad G，G|U非退化。再取W=W1⊕W0，其中W0=rad(A|W)，A11=A|W1非退化。令u=dim U、a=dim W1、b=dim W0。
3. 消去已知unit A11。剩余矩阵为
   \[
   \begin{pmatrix}A'_U+tG_U&B\\B^t&0_b\end{pmatrix},
   \quad A'_U=A_U-A_{U,W1}A_{11}^{-1}A_{W1,U},
   \quad B=A_{U,W0}. \tag{P3}
   \]
   因A(W1,W0)=0，B不含遗漏的Schur修正。
4. 若B未满columnrank，则存在0≠w∈W0、Bw=0，因而w是当前两个系数矩阵的共同kernel，det pencil恒0，算法以singular终止。
5. 若B满columnrank，必有b≤u。取E=ker B^t⊂U，dim E=u−b，并取R补空间，使B^tR=I_b。压缩到E上的两系数矩阵
   \[
   A_E=E^tA'_UE,\qquad G_E=E^tG_UE \tag{P4}
   \]
   组成下一轮pencil A_E+tG_E。它的维数严格下降a+2b；继续步骤1。

证明中所有basis变换均为常数GL，不使用未知det(A+tG)。步骤5按(E,R,W0)排序给

\[
\begin{pmatrix}
A_E+tG_E&D_t&0\\
D_t^t&M_t&I_b\\
0&I_b&0
\end{pmatrix}. \tag{P5}
\]

已知后2b阶border的逆准确为

\[
\begin{pmatrix}M_t&I\\I&0\end{pmatrix}^{-1}
=\begin{pmatrix}0&I\\I&-M_t\end{pmatrix},
\quad\det\begin{pmatrix}M_t&I\\I&0\end{pmatrix}=(-1)^b. \tag{P6}
\]

因此Schur修正是[D_t,0]·inverse·[D_t^t,0]^t=0，剩余矩阵恰P4。**没有产生t²项，也没有假定G_E非退化。** 每步的精确det关系是“原pencil det = 非零常数 × 下一轮pencil det”；常数来自det A11、(-1)^b和已明确选择的GL变换det的平方倒数。若起始basis变换为S、U内(E,R)变换为K_U，则该步常数可记

\[
c=\frac{\det A_{11}\,(-1)^b}{(\det S)^2(\det K_U)^2}\in F^\times, \tag{P7}
\]

其中W1消元的triangular变换det=1，空块det=1。符号按同时row/column的排序，平方消除了置换歧义。若G退化，a+b>0，所以a+2b>0；d=0空终点和G=0的边界情形均包含。

若全过程未触发步骤4，终点G_*非退化（包括0阶），于是

\[
\boxed{\det(A+tG)=c_*\det(A_*+tG_*),\quad c_*\ne0,\quad
\deg\det(A+tG)=d_*\le\operatorname{rank}G.} \tag{P8}
\]

反之任一轮步骤4严格推出原det恒0。故这是充分且必要的regularity判据，不只是G unit的另一种说法。第一次压缩维数u−b≤u=rank G给P8的degree界。

## P3. 共同kernel检查不能代替递归判据

在任意char≠2域，取

\[
A=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},
\quad G=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix}.
\]

ker A=span e3，ker G=span e2，两者交为0，但

\[
A+tG=\begin{pmatrix}0&1&t\\1&0&0\\t&0&0\end{pmatrix}
\]

det恒0。P3第一次取U=span(e1,e3)、W=span e2、B=(1,0)^t满columnrank，压缩到E=span e3后得到1阶零pencil，下一轮才检测singular。这是一般线性代数例子，非原目标的实际反例；没有执行程序来产生或推广它。

## P4. 对原 source 的严格条件推论

若actual (A,G) 的P3 staircase以regular终止，则8在F中是unit，det(A+8αG)非零，degree恰d_*≤rank G≤k≤2r。至多d_*个α residue失败；至少p−d_*个residue使实际first residual unit。对这些residue，原N anchor的Smith型为

\[
0^{8r-k},\quad1^k,
\]

并由P1得到

\[
\boxed{v_pD_A(X)=-34r+k,\qquad
p^{34r-k}D_A(X)\bmod p\in F^\times.} \tag{P9}
\]

whole-X归一化模p为常数：X扰动在N中至少p³，故不进入first residual。actual G奇异也允许P9；例如G=0但actual A unit时，全部α residue成功。然而**本文没有证明实际pencil regular**，更没有证明某一fixed rational α在无限辅助素数上成功。每prime坏residue数量小的条件本身不能给fixed rational选择；源响应稿S5的枚举反机制仍适用。

这补强的是原第一高层的非零门槛；单个p≈n只改变O(nlog n)定标，不提供n²算术费用收益。没有重定义source，也没有把ζ5改为ζ7。

## P5. 计算actual A必须保留的精度

以下给实际first residual的literal tail接口，不求出其det。negative base nodes为a_l=−l、0≤l<6r，actual tail为j=p+l。对exact paired局部basis P_i，令ε_i=0（strong）或1（weak），定义整jets

\[
x_{l,i}=P_i(a_l-p)/p^{\epsilon_i},\qquad
y_{l,i}=pP_i'(a_l-p)/p^{\epsilon_i}. \tag{P10}
\]

strong普通导数整，因为ambient degree<12r<p；weak的x整来自actual Hermite kernel。令x_l、y_l为column vectors。局部Gram稿G3的真实form给tail对N的准确贡献

\[
W_{p+l}\{u_l(x_ly_l^t+y_lx_l^t)+v_lx_lx_l^t\},
\quad u_l=p^4U_{p+l},\quad v_l=p^5V_{p+l}. \tag{P11}
\]

在α=0时移去harmonic中唯一p项，设

\[
c_l=5(H_{p+l}-1/p)-3(H_{p+8r+l}-1/p)-2H_{6r-1-l}\in\mathbf Z_p. \tag{P12}
\]

这些端点均<2p，故C_{p+l}=2/p+c_l准确成立。H_{p+l}^{(4)}=p^-4+integral、H_{p+l}^{(5)}=p^-5+integral，遂有

\[
u_l\equiv-6\beta\pmod{p^2},\qquad
v_l\equiv-36\beta-6p\beta c_l\pmod{p^2}. \tag{P13}
\]

任意α的增量为u_l−u_l|α0≡−8αp、v_l−v_l|α0≡−40αp (mod p²)，准确恢复源响应稿S6，而非自由扰动。X项含p⁵，不影响P13。

**head不进入first residual。** j<p时U_0整，V_0 valuation≥−1，故p⁵V_0至少p⁴；两侧Dp各至多除p，归一化后仍至少p²。derivative项p⁵U_0两侧最坏除p²仍至少p³。所有weights是整数，不能降低这些界。source α和X同样已支付；auxiliary域不存在nonunit tail。故在同一个exact局部basis中

\[
\boxed{N_{0,\beta}(0)\equiv
\sum_{l=0}^{6r-1}W_{p+l}\beta\{-6(x_ly_l^t+y_lx_l^t)
-(36+6pc_l)x_lx_l^t\}\pmod{p^2}.} \tag{P14}
\]

W_{p+l}必须取literal binomial weight mod p²，c_l只需modp，β取其fixed rational的modp²像。取T为K的整lift，leading N杀T，原Schur的cross两边均有p，故

\[
\boxed{A=\bigl(T^tN_{0,\beta}(0)T/p\bigr)\bmod p.} \tag{P15}
\]

只在明确知道numerator被p整除后使用P15；N modp²足够，不能先modp后除p。changing T by p times任意整矩阵不改变P15，因为leading matrix杀K。实际补空间选择同样不影响它作为K上的form。

P14所需最小jet精度为：strong P(a−p) modp²、P'(a−p) modp；weak P(a−p) modp³、P'(a−p) modp²。特别是weak values除p后，需要比冻结modp² halfjet代表多一层，不能把旧代表直接当actual A的数据。

## P6. halfjet未知项如何进入A

令A_node(t)=∏_{l=0}^{6r-1}(t+l)，I为其与reflection的共同节点因子，B_node=(A_node/I)I'。一个actual exact weak lift可写为

\[
P_Q=A_{node}Q+(p/2)B_{node}Q+p^2R_Q+O(p^3), \tag{P16}
\]

其中R_Q不是自由参数，必须由原char0 paired约束确定。普通Taylor在a_l处给

\[
x_{l,Q}=(\eta_l-1)J_{l,Q}
+p\{\tfrac12(A_{node}Q)''(a_l)-\tfrac12(B_{node}Q)'(a_l)+R_Q(a_l)\}\pmod{p^2},
\]
\[
y_{l,Q}=J_{l,Q}
+p\{-(A_{node}Q)''(a_l)+\tfrac12(B_{node}Q)'(a_l)\}\pmod{p^2}. \tag{P17}
\]

这里J=A_node'Q，B_node(a)=χ_l A_node'(a)=2η_l A_node'(a)，所以leading x严格是(η−1)J，包含真实−p平移。p²R_Q'不进入y的modp²，但R_Q(a)进入x的p层。strong lift P=P0+pP1+O(p²)给

\[
x_l=P_0(a_l)+p\{P_1(a_l)-P_0'(a_l)\}\pmod{p^2},
\quad y_l=pP_0'(a_l)\pmod{p^2}. \tag{P18}
\]

P17–18说明下一步该求什么：在原完整S坐标中解exact paired lift的所需二阶值，而非增加模p自由源或导数。本文未证明这些未知项在K上自动消失，也未算出actual A或higher Smith。

## P7. 核查范围与下一门槛

本轮本人数学producer执行0、失败0、rerun0、旧/同行execute/import0、new auxiliary prime0、Lean0；P3–18由实际完整读到的原定义和本稿纸推承担。未新下载文献；本稿不把generic singular-matrix perturbation或复数域结果当有限域实际regularity。最终独立审阅和immutable来源receipt将另登记；当前candidate未冻结。

新得到完整有限域regularity判据、其degree refinement及actual A的精确tail/jet接口。尚缺：actual staircase无限regular；fixed rational source无限成功；whole determinant无限非零；解析与算术strict margin；目标数值的新无理性/线性无关性结论。
