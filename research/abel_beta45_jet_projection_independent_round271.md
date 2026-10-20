# 第271轮：修正目标 4β(5)−3β(4) 的独立接口核查

2026-10-20，`new_primary_271`。根提出Hermite-jet修正后独立纸核；数学计算/扫描/Lean均0，未改状态账。它接在 [Abel纯β(4)候选的反证](abel_beta4_source_independent_round271.md) 之后，不撤销旧纠错。

**结论：修正后的同对象投影、实际正Gram、满秩目标系数通过；新数值结论与完整本原净预算未证。** 原source插值行的费用必须保留，不能无条件继承奇素数p>n整性。以下该有限处引理均限 \(p>\max(n,2)\)；2处另付。

## 1. 唯一实际对象及Hermite存在性

置n=2m−1、c=−m，
\[
R(t)=\frac{\prod_{j=1}^{n}(t+j)^3}{\prod_{k=0}^{n}(t+k+1/2)^3},\quad
x=t-c,\quad w=x^2.
\]
右半极点 \(\rho_k=-k-1/2\)，\(0\le k<m\)，对应 \(x_k=m-k-1/2>0\)、\(w_k=x_k^2\)。在每个ρk写
\[
R(t)=\frac{a_{3,k}}{(t-\rho_k)^3}+\frac{a_{2,k}}{(t-\rho_k)^2}
+\frac{a_{1,k}}{t-\rho_k}+O(1).
\]
直接分离极点给
\[
a_{3,k}=\left(4^{-n}\binom{2k}{k}\binom{2(n-k)}{n-k}\right)^3>0.
\tag{B1}
\]
令 \(g_k=a_{2,k}/a_{3,k}\)、\(h_k=a_{1,k}/a_{3,k}\)，并取
\[
\alpha_k=\frac{3-g_k}{4x_k},\qquad
\gamma_k=-\alpha_k^2-\frac{h_k+4x_kg_k\alpha_k+2\alpha_k}{4x_k^2}.
\tag{B2}
\]
这里γ是p的二阶导数值，避免与Dirichlet β函数混名。所有数据有理，xk非零。m个互异有理节点上的三阶Hermite插值给唯一 \(p_i\in\mathbf Q[w]_{<3m}\)，使
\[
p_i(w_k)=\delta_{ik},\quad p_i'(w_k)=\alpha_k\delta_{ik},\quad
p_i''(w_k)=\gamma_k\delta_{ik}.
\tag{B3}
\]
存在性也可自含由 \(\prod_{l\ne i}(w-w_l)^3\) 乘一个二次多项式实现。各p_i由节点值独立。

## 2. 对完整乘积而非单行验证局部条件

写 \(f_i(t)=p_i((t-c)^2)\)，\(H_{ij}=f_if_j\)。在ρk，链式法则给
\[
H_{ij}=\delta_{ik}\delta_{jk},\quad
H_{ij}'=4x_k\alpha_k\delta_{ik}\delta_{jk},
\]
\[
\frac12H_{ij}''=(2\alpha_k+4x_k^2\gamma_k+4x_k^2\alpha_k^2)
\delta_{ik}\delta_{jk}.
\]
所以Fij=RHij的极点系数恰为
\[
A_{3,k}=a_{3,k}\delta_{ik}\delta_{jk},\qquad
A_{2,k}=3A_{3,k},\qquad A_{1,k}=0.
\tag{B4}
\]
这里二阶导中的 \(4x_k^2\alpha_k^2\) 必须保留；(B2)正好支付它。若i≠j，所有右极点主部均零，反射迫所有左主部也零，因此该Fij实际是一个多项式。这不使Gram退化。

## 3. 全部Abel头、半极点残数和唯一目标

按前稿的唯一分解写 \(F_{ij}=Q_{ij}+F_{ij}^{\mathrm{proper}}\)，定义
\[
A_0(F)=\operatorname{Abel}\sum_{l\ge0}(-1)^lF''(l)
=\rho(F)+\tau(F)\beta(4),
\]
其中ρ包括全部有限调和头与 \(\mathcal E(Q'')\)。这里Q现在一般只有有理系数，不能再称dyadic。反射仍给奇周期栏相消。由(B4)
\[
\tau(F_{ij})=576\sum_{k=0}^{m-1}(-1)^ka_{3,k}\delta_{ik}\delta_{jk}.
\]
中心向上竖线的确切身份是
\[
J_{ij}=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}F_{ij}(t)(\pi\csc\pi t)''dt
=-A_0(F_{ij})+\frac52\pi^5\sum_{k=0}^{m-1}(-1)^ka_{3,k}\delta_{ik}\delta_{jk}.
\]
没有遗漏t=0有限头：A₀已经把它加回；若从A₁起步须另减F''(0)。用 \(\beta(5)=5\pi^5/1536\)，得到
\[
\boxed{\ J=A+BY,\quad Y=4\beta(5)-3\beta(4),\quad
A_{ij}=-\rho(F_{ij})\in\mathbf Q,\quad
B=192\operatorname{diag}_{0\le k<m}((-1)^ka_{3,k}).\ }
\tag{B5}
\]
β(5)身份可由 \((\pi\csc\pi t)''''|_{t=1/2}=5\pi^5\) 的双边partial fraction导数直接得到。B的rank恰m；没有借用周期独立性或有限样本。

## 4. 正性与反证范围

令 \(\mu_m\) 为前稿§5的严格正测度。Fij的中心积分给
\[
(-1)^{m+1}J_{ij}=\int_{\mathbf R}p_i(-y^2)p_j(-y^2)d\mu_m(y).
\tag{B6}
\]
右侧是实际正Gram。非零多项式不可能在负半轴恒零，p_i独立且测度有连续正支撑，所以任意m均严格正定，特别 \(\det J(Y)\ne0\)。

这里 \(d\mu_m\) 的密度前因子为 \(\pi^2/2\)，积分域按(B6)是**整个 \(\mathbf R\)**。若把偶积分改写为 \(0<y<\infty\)，同一密度的前因子必须为 \(\pi^2\)。这与前稿§5的 \((2\pi i)^{-1}dt=dy/(2\pi)\) 归一化一致。

因此若假设实际Y=v∈Q，矩阵(B5)便是同一个有理、非零实际Gram。这支付该目标的全部有理反证所需的实际非零。它不证明任意与实际Y无关的有理参数v都使 \(\det(A+Bv)\ne0\)；B满秩只保证该多项式degree恰m。

## 5. source费用：奇素数p>n只能在清行后使用

节点差有精确分解
\[
w_k-w_l=(l-k)(2m-k-l-1).
\]
故Hermite插值的节点差逆在奇素数p>n处无新分母。但(B2)含有
\[
g_k=6\sum_{j=1}^n\frac1{2j-2k-1}
-3\sum_{\substack{0\le h\le n\\h\ne k}}\frac1{h-k},
\tag{B7}
\]
\[
h_k=\tfrac12(g_k^2+g'_k),\quad
g'_k=-12\sum_{j=1}^n(2j-2k-1)^{-2}
+3\sum_{h\ne k}(h-k)^{-2}.
\]
奇分母最大2n−1，可能大于n。若n<p≤2n−1并且某 \(2j-2k-1=p\)，则gk有6/p主项；在排除固定小素数后，α可有估值−1、γ可有估值−2。这会进入p_i及多项式Qij，不能因(B4)中proper主部p整便忽略Euler多项式头。

取正整数ci使 \(c_ip_i\in\mathbf Z[w]\)，C=diag(ci)。前稿修正后的双头论证可严格用于清行后的Fij，给
\[
C A C\in M_m(\mathbf Z_p)\quad(p>\max(n,2)),
\]
而B本身dyadic。故清行提供的是可计费的保证，det scaling为 \((\prod_i c_i)^2\)，费用 \(2\sum_i\log c_i\)。并非宣称这一保证最优，或这笔费用可与最终primitive内容重复领取。

由(B2)、(B7)及Hermite逆的因子可先限定ci的prime support为2及≤2n−1的奇素数；因此raw A在 \(p>\max(2,2n-1)\) 时整。奇素数区间n<p≤2n−1和其它小素数/高次幂（包括2处）的实际内容仍须全尺度结算。这里未给完整费用率、实能量率或严格净余量。

## 6. 既有结果的准确关系

实际读旧 `cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md` H7–H9：H7的条件角色目标族包含s=5、r=3/4、χ=χ−4的Y/4，但没有此目标的数值定理；H9的已证无限非零属于ζ的double-pole布局，不能直接转给角色多轮廓。它也没有这次中心正Gram及(B3)的完整乘积投影。

本轮已核的一手 [Hexagon 2610.00285v2](https://hexagonmath.org/pdf/2610.00285v2) 及固定formal声明只有β(4),…,β(36)中至少一个无理，不直接覆盖固定Y；β(5)是π⁵有理倍数本身也不推出Y无理。定向文献检索未找到Y已被明确数值定理覆盖，但不声称全球穷尽。

因此可以把(B5)–(B6)登记为该固定目标的新实际结构接口；不登记为新无理性定理，也不凭它自动获准超期预算投入。
