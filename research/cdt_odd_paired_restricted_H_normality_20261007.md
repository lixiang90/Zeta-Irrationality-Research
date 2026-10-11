# 掩膜第三 Racah 正常性、低度右逆与真实 restricted-H 的已知边界

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。本轮开始前的518冻结记录全部只读。本文纯纸面推导；新增数学程序执行0，旧或同行数学程序 execute/import/rerun 0，不扩辅助素数单位表。实际固定 λ2、profile(r,3r)、原点 halfjet、middle 和两个固定第五幂种子保留。本文给出全尺度结构定理，尚不证明新特殊值无理性或线性无关性。

## 1. 实际输入与新的掩膜函数

本轮实际全文读取冻结 [第二 Racah 稿](cdt_odd_paired_cross_racah_injectivity_20261007.md) C1–C30、冻结 [完整三次与 middle 稿](cdt_odd_paired_fixed_middle_racah_border_20261006.md) R1–R30。令 p=18r+1 为素数、a=5r、F=Fp、u=y²，
\[
S(u)=\prod_{j=5r+1}^{9r}(u-j^2),\qquad
S(k^2)=\frac{(-1)^{r+k+1}}{(5r-k)!(5r+k)!}.
\tag{H1}
\]
Σ_l 表示 k=−l,…,l 的和。原实际 forms 为
\[
C(f)=\tfrac12(5\Sigma_a-\Sigma_{r-1})S^{-1}f,
\qquad H(f)=\tfrac12(\Sigma_a+\Sigma_{r-1})S^3f.
\tag{H2}
\]
T-space 为 degree<r，Q-space 为 degree<3r。C 为 r×3r 实际矩阵；H 为 3r×3r。实际 M5 的左上 G 保留原第五幂权重，不在本文中改成0。

令
\[
J(f)=\tfrac12\Sigma_a S^{-1}f,
\qquad m(u)=\prod_{j=0}^{r-1}(u-j^2),\qquad J_m(f)=J(mf).
\tag{H3}
\]
原点和全部 middle 节点确实被 m 消去；它是对特定 Q-polynomial 的合法运算，不能据此删除 H2 的原实际 middle。

## 2. 删除首 r 个节点后仍是 Racah：准确归一化

J_m 的剩余节点为 k=r,…,5r，各节点折叠质量准确为 S(k²)^−1 m(k²)。写 k=r+x、N=4r，则
\[
\lambda=x(x+2r)=u-r^2,
\quad m(k^2)=k(k-r+1)_{2r-1},
\quad w_* = S(r^2)^{-1}m(r^2)
=-r(2r-1)!(4r)!(6r)!.
\tag{H4}
\]
w_* 是 F 单位；这里没有原点剩余半质量，因为 k=r≥1。

两相邻质量比为
\[
\frac{S((k+1)^2)^{-1}}{S(k^2)^{-1}}=\frac{5r+k+1}{k-5r},
\qquad
\frac{m((k+1)^2)}{m(k^2)}
=\frac{k+1}{k}\frac{k+r}{k-r+1}.
\tag{H5}
\]
因此准确
\[
J_m(f)=w_*\sum_{x=0}^{4r}v_x f(r^2+\lambda(x)),\qquad
v_x=\frac{(6r+1)_x(2r)_x(r+1)_x}
{(-4r)_x(r)_x x!}.
\tag{H6}
\]
v0=1，所有分母在终止范围内都是单位。

这是 Koekoek–Swarttouw Eq1.2.2 在
\[
(\alpha,\beta,\gamma,\delta)
=(-4r-1,10r+1,6r,-4r-1),\qquad
\gamma+\delta+1=2r,
\tag{H7}
\]
的有限权重。逐因子代入后，上下各有 (-4r)_x、(6r+1)_x 的一次消去，剩下的 well-poised 因子为 (r+1)_x/(r)_x，准确得到 H6。这里不取 g=0 极限，不能沿用前两族的原点2因子。

定义 u-polynomials
\[
\widetilde P_n(u)={}_4F_3
\left(\begin{matrix}-n,n+6r+1,-x,x+2r\\-4r,6r+1,6r+1\end{matrix};1\right),
\quad 0\le n\le4r,
\tag{H8}
\]
其中 u=r²+x(x+2r)。因为
\[
(-x)_j(x+2r)_j=(-1)^j\prod_{i=0}^{j-1}
\bigl(u-r^2-i(i+2r)\bigr),
\tag{H9}
\]
H8 是 degree n 多项式，最高系数
\[
\widetilde\ell_n=
\frac{(n+6r+1)_n}{(-4r)_n(6r+1)_n^2}.
\tag{H10}
\]

## 3. 所有完整掩膜 profiles 的单位范数

KS PDF29 Eq1.2.2 的有限正交恒等式准确给
\[
\sum_{x=0}^{4r}v_x\widetilde P_n(r^2+\lambda(x))
\widetilde P_j(r^2+\lambda(x))
=\widetilde\nu_n\delta_{nj},
\tag{H11}
\]
\[
\widetilde\nu_0=
\frac{(-10r-1)_{4r}(2r+1)_{4r}}{(-4r)_{4r}^2},
\qquad
\frac{\widetilde\nu_n}{\widetilde\nu_0}
=\frac{(n+6r+1)_n(n!)^3(10r+2)_n}
{(6r+2)_{2n}(-4r)_n(6r+1)_n^2}.
\tag{H12}
\]
有理身份的使用范围与冻结 C8 相同：固定终止 α+1=−4r，先在通常参数域建立有限和身份，再按参数的有理身份延拓到 H7，最后逐个已知单位分母约化到 F。不要求有限域正定性，也不要求实际 H 的任何 minor 正常。

**Theorem H13。** 每个实际 p=18r+1 及 0≤n≤4r，w_*、ν̃n、ell̃n 全为 F 单位；J_m 的全部 leading profiles d≤4r+1 非退化。

证明：(-4r)_n 在 n≤4r 内没有0；正因子的最大指标是 (10r+2)_(4r) 或 (6r+2)_(8r) 的末项14r+1，严格小于 p。其他非空积的正或负因素绝对值更小。n0空积单独处理。因此 η_n=J_m(P̃_n²)=w_*ν̃_n 为单位，并且
\[
\det J_m^{[d]}=\prod_{n<d}\eta_n/\widetilde\ell_n^2\in F^\times.
\tag{H14}
\]
这里称第三族是因为其真实支持、参数和 g=2r 均不同于完整三次族和完整交叉族。

## 4. actual C 已在 degree<2r 上满行秩

对 degree T<r、degree W<r，实际 H2 严格给
\[
\boxed{C(T,mW)=5J_m(TW).}
\tag{H15}
\]
令 J_r=J_m^[r]。H13 证明 J_r 单位，故 r×r 子矩阵 C(u^i,m u^j)=5J_r 单位。这比冻结 C14 的 degree<3r 范围加强：

**Theorem H16。** 原实际 C 限制于 degree Q<2r 时已经满行秩 r；其右逆可取 degree<2r 的 polynomials
\[
\mathcal R=m\,J_r^{-1}/5.
\tag{H17}
\]
式中矩阵列是 degree<r 的 W-polynomial 系数，再乘 m。全部分母只有已证明单位的 J_r 与5；没有原实际未知 Gram inverse。

令 C_rem=[C(u^i,u^j)]_(i,j<r)，取
\[
\mathcal K_j=u^j-\sum_i\mathcal R_i(C_{\rm rem})_{ij}\quad(j<r),
\qquad
\mathcal K_{r+j}=m\widetilde P_{r+j}\quad(j<r).
\tag{H18}
\]
全部在 ker C：前 r 列由右逆，后 r 列由 J_m 正交与 degree T<r。Euclidean division 按 m 给出各列的独立余数或独立商；故它们组成完整2r kernel basis。前 r 列 degree<2r；后 r 列分别有确切 degrees2r,…,3r−1。

记 U=[R,K]，CU=[I,0]。以 remainder/quotient coordinates 核行列式：乘 m 的 monic synthesis determinant 为1；交换第一组 r 列与第二组 r 列给符号(−1)^r。因此
\[
\boxed{\det U=(-1)^r5^{-r}\det(J_r)^{-1}
\prod_{j=r}^{2r-1}\widetilde\ell_j\in F^\times.}
\tag{H19}
\]
新 U 与冻结 C18 的 U 不同，不混用两个数值尺度。它们均只在辅助有限处作合法局部 congruence，不免费重选 global saturated integer lattice 或解析范数。

## 5. middle 在真实 ker C 上的完整作用

令 u_k=k²、0≤k<r，evaluation map ev_mid(q)=(q(u_k))。R=mW 严格在 middle 为0，故前 r 个 K_j 的 middle values 就是 u_k^j。后 r 个 K_j 的 middle values 为0。distinct squares 及 Vandermonde 证明
\[
0\longrightarrow m\langle\widetilde P_r,\ldots,
\widetilde P_{2r-1}\rangle
\longrightarrow\ker C\xrightarrow{\mathrm{ev}_{\rm mid}}F^r
\longrightarrow0
\tag{H20}
\]
是准确正合列。特别 actual middle update 在 ker C 上秩准确 r，不能因 C-constraints 把它删掉。

沿用冻结 R12–R16：D=(1/2)Σ_a S³ 的 degree<3r 完整三次 Gram 是单位，V_(i,k)=u_k^i，E=diag(e_k) 单位，e0=S(0)³/2、ek=S(k²)³(k>0)，实际 H=D+VEVt。设 K=[K_low,K_high] 为 H18，则
\[
K^tHK=
\begin{pmatrix}
K_{\rm low}^t D K_{\rm low}+W^tEW&K_{\rm low}^tDK_{\rm high}\\
K_{\rm high}^tDK_{\rm low}&K_{\rm high}^tDK_{\rm high}
\end{pmatrix},
\quad W_{kj}=u_k^j.
\tag{H21}
\]
W、E 全为单位，原点半质量保留。middle-only 左上项 WtEW 单位并不意味着加上完整 D 后仍为单位，也不意味右下压缩 D_high 单位；这两处仍可发生有限域相消。

## 6. restricted-H 的无条件2r边界与核重建

以下 M0 是 **G=0 的诊断矩阵**，只用于表达 restricted H，绝不替换原实际 M5 的 G：
\[
M_0=\begin{pmatrix}0&C\\C^t&H\end{pmatrix},
\qquad H_{22}=K^tHK.
\tag{H22}
\]
按 Q-space 的 U congruence，得到
[[0,I,0],[I,H11,H12],[0,H21,H22]]。首2r hyperbolic block 单位，其 inverse 的下右 r×r block 为0，所以 Schur correction 为0。准确
\[
\det H_{22}=(-1)^r(\det U)^2\det M_0,
\qquad\operatorname{corank}H_{22}=\operatorname{corank}M_0.
\tag{H23}
\]

将 M0 加上已知 middle border −E^−1，再消去已知 D，先得负 cross blocks；以 diag(−I_r,I_r) congruence 变为
\[
\mathcal B_H=
\begin{pmatrix}
-CD^{-1}C^t&CD^{-1}V\\
V^tD^{-1}C^t&-E^{-1}-V^tD^{-1}V
\end{pmatrix}.
\tag{H24}
\]
两次 congruence 的 determinant 与 frozen R18–R20 相同，因而
\[
\boxed{\det H_{22}=(\det U)^2\det E\det D\det\mathcal B_H,
\quad\operatorname{corank}H_{22}=\operatorname{corank}\mathcal B_H.}
\tag{H25}
\]
没有除原实际 H、restricted H、任何 C-leading monomial minor 或第五幂种子。所有 prefactors 都是已证单位。等价对称 gate
\[
\widehat{\mathcal B}_H=
\begin{pmatrix}
CD^{-1}C^t&CD^{-1}V\\
V^tD^{-1}C^t&E^{-1}+V^tD^{-1}V
\end{pmatrix}
\tag{H26}
\]
具有相同 determinant/corank：先取 −B_H，再作 diag(−I,I) congruence；2r 偶数确保整体符号不改变 determinant。

核重建同样准确。若 (t,z)∈ker B_H，则
\[
q=D^{-1}(C^tt-Vz),\quad Cq=0,\quad z=EV^tq,
\quad Hq=C^tt.
\tag{H27}
\]
反向，若 q∈ker C 且 Hq∈im Ct，则由 Ct 单射唯一求 t，再 z=EVtq 得 B_H 核。q0 必迫 t=z0。因此 restricted-H 的真实核是 Hq落在 im Ct 的混合边界现象，范围比 ker H∩ker C 更大。

## 7. 真实新收益与未证条件

H6–H14 证明在实际辅助素数上，消去 middle 节点的 cross functional 自身仍具有全 profiles 正常性；H16–H20 将 actual C 的最低足够 Q-degree 降到2r，给出仅除首r掩膜 norm 的低度右逆、按 degree 排列的完整 kernel 和准确 middle 正合列。H25–H27 把 sufficient condition H|kerC 非退化等价为一个2r、无第五幂种子的已知边界 determinant；它不同于原 M5 的2r gate，后者仍有实际 G。

仍未证明 detB_H≠0。完整 J_m 正常性控制 cross 的商约束，完整 D 正常性控制整个3r空间；两者没有自动控制 D 或 H 在 ker C 上的压缩。H21 的右下 D_high 是一个精确可继续研究的 r×r 子问题。若最终证明 H22 单位，才能使用冻结 C23 的 r阶 actual M5 gate；该 gate 在固定第五幂种子处仍须另证非零。H22 奇异也不表示原 M5 奇异，所以此充分路线不可误称目标的必要条件。

没有无限 actual M5 单位、固定 rational source 无限成功、actual higher Smith 界、same-object strict margin、新ζ/L/Catalan 无理性或 LI。本文所有变换保留原格与已付费用，不从有限域 normality 继承免费 arch improvement。

## 8. primary 实际读取和执行范围

复用已归档 Koekoek–Swarttouw 作者报告，源 [The Askey-scheme of hypergeometric orthogonal polynomials and its q-analogue](https://tudelft.roelofkoekoek.nl/documents/as98.pdf)，本轮实际完整文本 PDF28–29 共2 distinct pages。PDF28 Eq1.2.1 核定义/终止；PDF29 Eq1.2.2 核权重、M 与 norm 的每个因素。未声称本轮阅读170页全文，未新下载，无 TLS bypass。本文 H5/H9/H19/H23–H27 的代数另由自足纸证负责；没有数学 producer 或有限新 prime 数据。

状态：候选完整纸证，等待实际全文独立审阅和作者最终回读后再冻结来源收据；不提前声称 review 已完成。
