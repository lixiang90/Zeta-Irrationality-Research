# D12 周期向量叶与 CDT 分子的严格接口

日期：2026-10-06。独立新纯 MD proof note。只读已冻结的实际周期表和 CDT 原文，不执行或导入任何 producer。本文证明普通 Jensen 分子、一个明确的 stationary refinement 及固定范数变换的限制；不证明全周期稳定子的分类，不宣称所有向量束版算术代数化定理都受同一限制，也没有新的数值无理性结论。

## 1. 必须保留的实际算术对象

实际输入是[完整九生成元周期表](cdt_odd_level12_generator_cocycle_20261006.md)的两个函数

\[
h_Z=f_Z-103680\zeta(3),\qquad
h_L=f_{\sigma,L}+34560\sqrt3 L(3,\chi_{12}),
\]

以及同一 weight-2 gauge \(\mathcal B=E_2-12E_2(12\tau)\)。在 \(\Gamma=\ker\chi_{12}\) 上，二者有同一个 weight \(-2\) slash，实际余循环为

\[
c_j(\gamma)=h_j|_{-2}\gamma-h_j
  =80i\pi^3 P_j(\gamma),\qquad
P_j(\gamma)\in\mathbf Z+\mathbf Z\tau+12\mathbf Z\tau^2.
\tag{V1}
\]

表中 \(GL_4(\mathbf Z)\) affine matrices 是这个真实 period representation 的整数模型。CDT 的评价空间则是

\[
E_D=\bigoplus_{i=1}^m K[t]_{\le D} f_i,
\qquad
\psi_D(Q_1,\ldots,Q_m)=\sum_i Q_i f_i\in K[[t]],
\tag{V2}
\]

并用实际 Taylor 系数给它逐阶评价高度；这里 \(m\) 是 \(K(t)\)-线性无关函数的个数，不是矩阵大小、整数余循环的维数或任一 formal solution space 的维数。

原文的明确定位是：CDT §2.12/§2.13，PDF pp.36–37；Theorem 7.0.1，pp.89–90；评价映射 (7.3.8) 及一维 graded pieces，pp.99–100；Theorem 8.0.1，pp.122–123；数域接口 Remark 8.2.42，p.143。本文使用的本地原件是 [CDT PDF](../literature/cdt2024_l2_chi_minus3.pdf)，作者原件 URL 为 https://math.berkeley.edu/~ytang/L2chi.pdf。本文实际回读了上述页及 pp.26–27、97–100、113–116。

除以 \(80i\pi^3\) 使 period translations 整数化，并不使 \(h_j\) 的 Taylor 系数成为数域内的整数。特别，直接改用 \(h_j/(80i\pi^3)\) 会把原数域 Taylor 系数除以一个超越常数。实际周期表不能替换 (V2) 的整模型。

## 2. 带全部原点纤维的 Jensen 引理

先假设 \(\phi\) 在闭单位圆盘的某个开邻域全纯，\(\phi(0)=0\)、\(\phi'(0)\ne0\)。令

\[
\rho=\log|\phi'(0)|,
\qquad
Z_\phi=\sum_{\substack{a\in\mathbb D\setminus\{0\}\\\phi(a)=0}}
       \operatorname{ord}_a(\phi)\log\frac1{|a|}\ge0.
\tag{V3}
\]

这是有限的 Jensen zero-counting 项。边界零点的对数奇点可积；它们不贡献 (V3)，因为其 Jensen 权为零。\(0\) 的零阶恰为一。

对 \(0\le r\le1\)，定义

\[
I_\phi(r,1)=\int_{\mathbb T}\int_{\mathbb T}
   \log|\phi(rz)-\phi(w)|\,d\mu(z)d\mu(w),
\qquad J_\phi=I_\phi(1,1),
\tag{V4}
\]

其中 \(\mu\) 是概率 Haar 测度。\(r=0\) 时把 \(\phi(rz)\) 解释为零。固定除有限个边界零点以外的 \(w\)，对 \(z\mapsto\phi(rz)-\phi(w)\) 应用 Jensen 不等式，得到

\[
\int_{\mathbb T}\log|\phi(rz)-\phi(w)|\,d\mu(z)
\ge \log|\phi(w)|.
\]

再对 \(w\) 积分，并对 \(\phi(t)/t\) 应用 Jensen 公式，便有

\[
\boxed{I_\phi(r,1)\ge\int_{\mathbb T}\log|\phi(w)|d\mu(w)
       =\rho+Z_\phi.}
\tag{V5}
\]

特别

\[
\boxed{J_\phi\ge\rho+Z_\phi.}
\tag{V6}
\]

这个证明没有假设 \(\phi^{-1}(0)=\{0\}\)。对只在开圆盘上全纯的 maps，可先应用于 \(\phi_R(z)=\phi(Rz)\)、\(R<1\)，再令 \(R\uparrow1\)。本文只在 \(\log|\phi(Rw)|\) 的 Jensen 极限存在、(V4) 的积分具有该极限且允许上述径向极限时使用边界版本；若缺这些边界条件，保留每个 \(R<1\) 的结论，不能直接写未定义的 boundary integral。零点项亦按 Jensen 极限定义，可能为无穷。

对多个数域嵌入的合法 maps，逐嵌入应用并平均即可：

\[
\overline J\ge\overline\rho+\overline Z.
\tag{V7}
\]

没有对未知 period 任意施加 Galois 作用；这里的嵌入作用只来自已证明属于数域的 formal arithmetic data。

## 3. 一个实际 stationary refinement 的同方向限制

这里只采用 CDT §7.6 的明确 refinement。固定
\(0<r_0<\cdots<r_l=1\)，并令

\[
I_{hk}=\int_{\mathbb T^2}
\log|\phi(r_hz)-\phi(r_kw)|\,d\mu(z)d\mu(w).
\]

选取 \(s_h\ge0\)、\(\sum_hs_h=1\)，令

\[
\beta_k=\frac{\sum_hs_h(I_{hk}-I_{h,k-1})}
                   {\log r_k-\log r_{k-1}},
\quad\beta_0=0,\quad\beta_{l+1}=m.
\]

若这些实际权满足 CDT (7.6.5) 的 stationary equations

\[
s_h=\frac{\beta_{h+1}-\beta_h}{m}
\quad(0\le h\le l),
\tag{V8}
\]

本文只在这些 stationary equations 与 \(\sum_hs_h=1\) 联立所得线性系统具有唯一实解，且该唯一解的所有分量均属于 \([0,1]\) 时使用 Theorem 7.6.4；这是原文 (7.6.5) 的明确条件，不能只选一个不经唯一性证明的非负候选权。在这个范围内，定理的分子恰为

\[
N_{\rm stat}=\sum_{h=0}^l s_h I_\phi(r_h,1).
\tag{V9}
\]

逐项使用 (V5)，有

\[
\boxed{N_{\rm stat}\ge\rho+Z_\phi.}
\tag{V10}
\]

这个推论没有使用“完整 kernel 已知”，也没有假设 map 单叶。它只涵盖 (V8) 确立的非负 stationary 权分子；不把任意非 stationary raw metric、任意多 map 输入或所有可能的向量束指标包括在内。

若某个已合法证明的算术成本为 \(\kappa\)，且要以 ordinary CDT 或本节 stationary bound 得到严格 rank contradiction，必须有

\[
m(\overline\rho-\kappa)>\overline N.
\]

由 (V7)/(V10)，一个必要条件因此是

\[
\boxed{(m-1)\overline\rho>m\kappa+\overline Z.}
\tag{V11}
\]

这是分子的下界所给的必要条件，不是 \(J\) 的上界，亦不保证可达到。额外原点原像会增加 \(\overline Z\)；它们可能同时允许更大的 \(\overline\rho\)，所以本文不以 (V11) 单独排除所有多零点 maps。

## 4. 唯一原点原像属于哪一层假设

CDT Theorem 7.0.1/8.0.1 的 rank bound 不要求 \(\phi^{-1}(0)=\{0\}\)。实际 branch 的合法性接口 Proposition 2.9.3/PDF p.26 本身要求 \(\phi^{-1}(\Sigma_0)\subset\Omega\)，以及 \(\phi|_\Omega\) 的 univalence，使所有需要填入的初始 regular punctures 的原像落在同一个局部单叶邻域。仅当 \(0\in\Sigma_0\) 时，这两项与 \(\phi(0)=0\) 才推出 \(\phi^{-1}(0)=\{0\}\)；并非每一个 Proposition 2.9.3 实例都把“原点唯一原像”作为字面的独立条件。Remark 2.9.5/p.27 解释 \(\Sigma_0=\{0\}\) 的 modular lambda universal map。Carathéodory 的 \(|\phi'(0)|\le16\) 在 p.24 使用“省略1、原点唯一原像”的额外条件。

因此，取消唯一原点原像之前必须分别证明：

1. 同一个实际 arithmetic germ 沿该 map 的所有路径给出单值 meromorphic pullback；其他零点附近的分支不能用初始 regular 分支冒充。
2. 该 map 的真正 \(\overline\rho\) 与 numerator upper bound；不能把旧的16上限直接移植到放宽后的 map。
3. (V11) 中额外的 Jensen 零点项。

现在的完整 affine period 表可以判定任何一个指定 word 是否固定实际 scalar；它本身不允许把所有 \(\Gamma\)-fibers 填进同一实际解析叶。非零 parabolic period 会在某些新增 cusp 产生多项式 log 项，它们作为 local-system sections 的形式延拓与 meromorphic scalar pullback 是不同条件。

## 5. 固定周期向量化不会直接改同一 map 的主项

在 scalar CDT proof 中，实际 functions 的增长常数与清 pole 的固定函数进入 Cauchy 估计的 \(o(D)\) 项。主项由 base coordinate map 的 Bost–Charles metric 决定：

\[
h_\infty(\psi_D^{(n)})\le
-n\rho+D J_\phi+o(D)
\tag{V12}
\]

见原文 (7.3.9)/p.100；source 的 Hilbert–Samuel 主项是 \(mJ_\phi D^2/2\)，见 (7.3.7)/p.99。高维版本的对应主项是 (8.2.28)/p.140。

一个可直接证明的比较引理是：若对同一个有限 source space 与同一个 graded target space，更换范数后存在与 \(D,n\) 无关的 \(C\ge1\)，使两套范数满足

\[
C^{-1}\|x\|_1\le\|x\|_2\le C\|x\|_1,
\]

则 local evaluation heights 的变化至多 \(2\log C\)，source arithmetic degree 的变化至多 \((\operatorname{rank}E_D)\log C=O(D)\)。因 leading grades 只有 \(m(D+1)\) 个，评价高度总变化也是 \(O(D)\)，不改变 \(D^2\) 主项。固定 constant change-of-basis 的 archimedean 比较正是这个情形；若需要计算它的有限素数 lattice index，应另外计算，不能从 period representation 的整数性推出。

更一般的 period-projected vector leaf 若要获得主项收益，必须打破这个固定比较的范围，例如给出真正扩大了的合法 scalar map，或证明一个不同评价空间/随 \(D\) 变化的指标。后者需要实际 source rank、graded ranks、积分模型、source arithmetic degree 和评价高度一起重新推导。本文不宣布一个未证明的“vector CDT”替代 Theorem 7/8。

完整表还立即排除一种尤其容易误用的做法：不存在一套固定正定 Hermitian form 使所有这些 affine matrices 成为 isometries。纯 L 的 \(\eta\) 矩阵是

\[
A_{\eta,L}=
\begin{pmatrix}
1&0&0&552\\24&1&0&6624\\12&1&1&2160\\0&0&0&1
\end{pmatrix},\qquad
(A_{\eta,L}-I)^3=13248E_{34}\ne0.
\tag{V13}
\]

若它保持正定 Hermitian form，就在一个 orthonormal basis 中为 unitary，因此可对角化；但 (V13) 是非平凡 unipotent Jordan block，矛盾。\(\det A=\pm1\) 控制体积，不能冒充 operator norm 为1。允许随 base point 变化的 metric 仍是开放接口，需实际计算其 curvature 与评价高度；本引理不排除它。

## 6. 可执行的下一入口与未获得的收益

不必先分类 full kernel，仍可以推进以下明确输入：由全九表证明一组新的具体 zero words，对其真实 scalar 稳定子建立合法 leaf/fundamental domain，并给 \(\overline J\) 的 upper bound 与 \(\overline\rho\) 的 lower bound；比较时使用 (V11)，若存在多零点则保留 \(\overline Z\)。这与已有 source/算术成本接口相容。

另一条可能的入口是一个真正的 varying Hermitian bundle 指标；最低可执行引理必须同时给：实际 scalar arithmetic germs 到该评价空间的单射、每阶 graded rank、同一整格的 finite heights、source Hilbert–Samuel degree，以及 leading-order archimedean estimate。仅给 \(GL_4(\mathbf Z)\) 周期矩阵或一个 period-invariant formal quotient 不满足这些条件。

本稿实际已证明的是 (V5)–(V11)、固定范数比较及 (V13) 的正定 flat metric 障碍。没有取得新的 \(\kappa\)、容量收益或数值 L-value 结论。根任务正在另稿处理共同 Bol 系统及 affine Zariski closure；本文不以未完成的 Picard–Vessiot 结论作为上述解析引理的前提。

## 7. 执行与审阅记录

本稿为纯 MD。只读实际冻结周期表、联合完整模型和 CDT 2024/2025 本地原件；没有运行/import producer，没有素数或参数搜索，也没有将旧 JSON checks 当作新证明。上述解析公式由正文的 Jensen 与范数比较证明承担。

根任务已实际全文只读独审 §§1–7，重推 (V5)–(V11)、固定范数的 \(D^2\) 主项比较及非平凡 unipotent 的 flat positive-metric 障碍，并实际回读 CDT PDF pp.26–27、114–116 的 branch 与 stationary 接口，数学链通过。按该独审将 stationary 系统的唯一非负解及 \(0\in\Sigma_0\) 时的唯一原点推论明确限定。根任务未执行 producer；本稿没有 producer。本文件在上述范围冻结，后续审阅只作外部记录，不为新增审阅改冻结文件。
