# 第272轮：固定 Hermite 来源的显式结构与整数值基

2026-10-20，`positive_source_271`。本稿只处理[272固定对象](abel_beta45_budget_charter_round272_20261020.md)的来源结构。开始时 goal 工具返回 null；`research_state.py show` 为272进行中，`git status --short` 为空。已实际全文读271报告、B1–B7和272任务；未修改状态账或旧稿，未运行数学扫描、CAS或数值程序。

数值目标仍为 \(Y=4\beta(5)-3\beta(4)\)，反证范围为全部实际 \(Y=u/v\)。对象固定 \(n=2m-1\)、271.2–271.7的唯一 \(p_i\)、\(M_m\) 和首一 \(Q_m\)。首问题是能否先证全序列 \(\liminf m^{-2}\log|Q_m(Y)|\ge0\)，以结束负二次接口。本稿**没有得到这个实际下界**；以下整数值来源证书不冒充完整 Euler 头或本原预算。

## 1. 唯一平方节点 Hermite 多项式的闭式

暂按任意固定节点顺序记 \(w_i=x_i^2\)，其中 \(x_i=m-i-1/2\)，\(0\le i<m\)。置
\[
D(w)=\prod_{k<m}(w-w_k),\qquad
\ell_i(w)=\frac{D(w)}{(w-w_i)D'(w_i)},
\]
\[
d_i=\sum_{k\ne i}(w_i-w_k)^{-1},\qquad
e_i=\sum_{k\ne i}(w_i-w_k)^{-2}.
\tag{H1}
\]
这两个符号只表示节点和，不与下文LCM混用。唯一原 \(p_i\) 恰为
\[
p_i(w)=\ell_i(w)^3
\left\{1+u_i(w-w_i)+v_i(w-w_i)^2\right\},
\tag{H2}
\]
\[
u_i=\alpha_i-3d_i,\qquad
v_i=\frac{\gamma_i}{2}-3d_i\alpha_i+
\frac{9d_i^2+3e_i}{2}.
\tag{H3}
\]
证明：在其它节点 \(\ell_i^3\) 有三重零。在 \(w_i\)，\(\ell_i'=d_i\)、\(\ell_i''=d_i^2-e_i\)，故 \((\ell_i^3)'=3d_i\)、\((\ell_i^3)''=9d_i^2-3e_i\)。代入(H3)逐项得到值1、导数 \(\alpha_i\)、二导数 \(\gamma_i\)。次数不超过 \(3m-1\)，因此由Hermite唯一性，它是原对象，未另选来源。

若把节点升序记为 \(w_r=(r+1/2)^2\)，直接分解平方差还给
\[
D'(w_r)=(-1)^{m-1-r}
\frac{(m-1-r)!(m+r)!}{2r+1}.
\tag{H4}
\]
这只是表达原基；不能把上述阶乘直接作为最优来源费用。

## 2. 改用完整连续整数节点；没有更换实际多项式

令
\[
q=t+m-\tfrac12,\qquad
f_i(q)=p_i((q+1/2)^2),\qquad D_0=6m-2.
\tag{H5}
\]
于是原 \(P_i(t)=p_i((t+m)^2)=f_i(t+m-1/2)\)。全部半整数极点在q坐标恰是连续整数
\[
\mathcal J=\{-m,-m+1,\ldots,m-1\}.
\]
右节点 \(q=m-k-1\) 的三jet是
\[
f_i=\delta_{ik},\quad f_i'=s_k\delta_{ik},\quad
f_i''=z_k\delta_{ik},
\]
\[
s_k=\frac{3-g_k}{2},\qquad
z_k=-h_k-2g_ks_k-s_k^2
=-h_k+\frac34g_k^2-\frac32g_k-\frac94.
\tag{H6}
\]
左反射节点的值和二导数相同，一导数相反。第一式来自 \(2x_k\alpha_k\)，第二式来自 \(2\alpha_k+4x_k^2\gamma_k\)；这里消去了表面的 \(x_k^{-1}\)，没有省略乘积jet中的平方项。

\(f_i\) 次数不超过 \(D_0\)。完整连续节点的三jet插值次数界是 \(<6m\)；原反射 \(f_i(-1-q)=f_i(q)\) 使最高奇中心次数消失，与 \(D_0=6m-2\) 一致。因此下面的完整Hermite表达仍恢复同一 \(f_i\)。

## 3. 一份指数级的整数值来源倍数

记
\[
L=\operatorname{lcm}(1,\ldots,2n-1),\qquad C_m=8L^2.
\tag{H7}
\]
此定义也适用于 \(n=1\)。B7的实际公式直接给
\[
Lg_k\in\mathbf Z,\quad L^2g'_k\in\mathbf Z,
\quad 2L^2h_k\in\mathbf Z.
\]
因为其中所有非零奇分母绝对值不超过 \(2n-1\)，整数节点差不超过n。由(H6)，
\[
2Ls_k\in\mathbf Z,\qquad 4L^2z_k\in\mathbf Z.
\tag{H8}
\]

对 \(j\in\mathcal J\)，连续整数节点的Lagrange基可以精确写成
\[
L_j(q)=\binom{q+m}{j+m}
\binom{m-1-q}{m-1-j}.
\tag{H9}
\]
它在全部整数q取整数，且在 \(\mathcal J\) 的值为 \(\delta\)。不需额外符号：第二个binomial的最高项已含正确符号。置
\[
a_j=\sum_{h\in\mathcal J\setminus\{j\}}(j-h)^{-1},\qquad
b_j=\sum_{h\ne j}(j-h)^{-2}.
\]
则 \(La_j,L^2b_j\in\mathbf Z\)。给定任一行在j的jet \((v_j,s_j,z_j)\)，其完整Hermite表达为
\[
\sum_{j\in\mathcal J}L_j(q)^3
\left[
v_j+(s_j-3a_jv_j)(q-j)
 +\left\{\frac{z_j}{2}-3a_js_j+
 \frac{9a_j^2+3b_j}{2}v_j\right\}(q-j)^2
\right].
\tag{H10}
\]
值数据 \(v_j\) 是0或1；其它数据是(H6)及其反射。由(H8)，乘 \(8L^2\) 后(H10)每个方括号系数都是整数。\(L_j^3\) 及 \((q-j)^r\) 都是整数值多项式，故严格得到
\[
\boxed{C_m f_i\in\operatorname{Int}(\mathbf Z)\quad(0\le i<m).}
\tag{H11}
\]
这是同一来源的整数值证书，不是普通单项式整系数声明。

## 4. 半步平移与固定两导数的准确费用

任何次数不超过 \(D_0\) 的整数值多项式都有整数Newton系数：
\(C_mf_i(q)=\sum_{r\le D_0}a_{ir}\binom qr\)，因为 \(a_{ir}=\Delta^r(C_mf_i)(0)\in\mathbf Z\)。令 \(a=m-1/2=m+(-1/2)\)。Vandermonde恒等式和
\[
\binom{-1/2}{r}=(-1)^r4^{-r}\binom{2r}{r}
\]
给 \(4^r\binom ar\in\mathbf Z\)。再展开 \(\binom{t+a}{r}\)，得到
\[
\boxed{K_mP_i\in\operatorname{Int}(\mathbf Z),\qquad
K_m=8\,4^{D_0}L^2.}
\tag{H12}
\]
这里的整数值变量是原t。半步平移只增加2处费用，没有额外奇素数。标准 \(\log d_N=O(N)\) 因而给 \(\log K_m=O(m)\)；有限证书(H12)本身不依赖PNT。

若 \(d_{D_0}=\operatorname{lcm}(1,\ldots,D_0)\)，Newton生成函数逐系数给
\[
\frac d{dt}\binom tr
=\sum_{j=1}^r\frac{(-1)^{j-1}}j\binom t{r-j}.
\tag{H13}
\]
因此 \(K_m d_{D_0}^{\,a}P_i^{(a)}\) 对 \(a=0,1,2\) 都是原t上的整数值多项式。若只对这种已知整数值的多项式取Euler泛函，可再用
\[
\mathcal E\left(\binom tr\right)=\frac{(-1)^r}{2^{r+1}}
\tag{H14}
\]
清整。**这不证明完整 \(F_{ij}=R_mP_iP_j\) 的多项式商部已被同一倍数清整。** 有理函数除法、所有有限调和头及其实际约分仍须由同一完整对象另证；也不能把(H11)/(H12)冒充 \(c_ip_i\in\mathbf Z[w]\) 后套旧引理。

## 5. 对实际下界的限定结论

(H2)在负轴可以提取共同 \(D(w)^3\)，但余下是各节点的有符号合流Cauchy行。各行的最高次数至多 \(3m-1\)，并非已证互异次数的单首正交列。单独一个非零最高系数或每行非零，不能给m阶Gram体积的下界；在非正交单项式基中删掉交叉项也不是合法下界。

本稿没有证明实际 \(\det M_m\) 或 \(|Q_m(Y)|\) 的非负二次率，亦没有把来源整数值倍数升级为完整最优 \(\lambda_m\)。因此首问题未由本分工裁决。所得可直接使用的证书是原Hermite基的显式表达和(H11)–(H13)的指数级整数值来源，供完整本原预算使用；不以这些局部资产延长一轮窗口。

本文所有公式均纸面推导；没有数学producer、样本外推、prime/m/参数扫描或外部Lean执行。
