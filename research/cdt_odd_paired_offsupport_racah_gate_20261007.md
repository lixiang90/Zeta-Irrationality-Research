# 支集外 fourth-Racah 门槛的全尺度秩下界

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。本轮基线540冻结记录全部只读；最新保存 audit 为 `cdt_odd_delivery_reference_20261007.json`，SHA `7141ac2383dee7e1f2bf0828c993a17de4c0738b4f8a90dd6a627f9d97a43be3`。实际完整回读冻结 [masked-high 主稿](cdt_odd_paired_masked_high_compression_20261007.md) 九节 M1–M24、物理 SHA `bd107ba87fe707be5d8dc969b29949b05a4afd91e32baef4e41e5f9d4775bb1f`，以及 [restricted-H 主稿](cdt_odd_paired_restricted_H_normality_20261007.md) 八节 H1–H27。当前总主稿只实际读本轮相关 §§152–155；最新 audit 实际读 header/current_progress/execution_history 并完整 JSONparse，不声称数千字段人工全文读。首次 combined 输出截断后，bd107 已单独完整补读。

本文纯纸证，数学 producer execute/import/rerun 0，辅助素数单位表扩展0，没有新 prime 数据。原固定 M5、middle、degree、halfjet 与已付全球费用保留。真正新结论是实际 off-support gate 的秩至少一半并排除奇数维极小秩，而非其 determinant 非零。

## 1. 实际待证门槛与本轮所得

仍取 p=18r+1 素数，F=Fp，u=k²，
\[
S(u)=\prod_{j=5r+1}^{9r}(u-j^2),\qquad
m(u)=\prod_{i=0}^{r-1}(u-i^2),\qquad
D(f)=\tfrac12\sum_{k=-5r}^{5r}S(k^2)^3f(k^2),
\]
\[
\mathcal L(f)=D(mf),\qquad \Phi(f)=D(m^2f)=\mathcal L(mf).
\tag{O1}
\]
冻结 M6–M9 证明 fourth-Racah 的全部 monic polynomials、norms 均正常：
\[
p_n(u)=\kappa_n^{-1}
{}_4F_3\!\left(
\begin{matrix}-n,n-14r-1,-x,x+2r\\-4r,-4r,-4r\end{matrix};1\right),
\quad u=r^2+x(x+2r),\quad0\le n\le4r,
\]
\[
\mathcal L(p_np_j)=\omega_n\delta_{nj},\qquad
\omega_n,\kappa_n\in F^\times.
\tag{O2}
\]
实际 d=2r Christoffel gate 为
\[
\mathcal E=[p_{2r+j}(i^2)]_{i,j=0}^{r-1}.
\tag{O3}
\]

**Theorem O4。** 对每个实际辅助素数且 r≥2，
\[
\boxed{\operatorname{rank}\mathcal E\ge\lceil r/2\rceil,
\qquad
\operatorname{corank}\Phi^{[2r]}
=\operatorname{corank}\mathcal E\le\lfloor r/2\rfloor.}
\tag{O4}
\]
这里 Phi^[2r] 是 W-degree<2r 的完整 leading Gram。本稿没有给真实 r维 high compression D_high 同样的界；restricting a bilinear form 到子空间会另生 radical。r=1 不在 O4 的加强范围内，不新增该素数的有限单位判定。

O4 的证明分三步：一个任意域上 consecutive-degree 正交求值块的秩定理；奇数维极小秩的精确分类；原 Racah 差分方程排除该极小情形。没有将有限域 positivity 作为输入。

## 2. 任意域上的 consecutive-degree 求值秩定理

设 K 是任意域，monic polynomials f_j(z) 满足
\[
f_{j+1}=(z-a_j)f_j-b_jf_{j-1},\qquad
f_0=1,\quad f_{-1}=0,
\tag{O5}
\]
其中本节所用 b_j 都非零。取 n≥1、整数 R≥2、R个不同节点 z_i。要求原序列直到 n+R−1 的全部 b_j 非零，并有本有限窗口的 a_j。定义
\[
E=[f_{n+j}(z_i)]_{i,j=0}^{R-1}.
\tag{O6}
\]

**Theorem O7（一般秩及奇数极小情形）。**
\[
\operatorname{rank}E\ge\lfloor R/2\rfloor.
\tag{O7}
\]
若 R=2s+1≥3，则
\[
\boxed{\operatorname{rank}E=s
\quad\Longleftrightarrow\quad
f_{n+s}(z_i)=0\ \text{对全部 }i.}
\tag{O8}
\]
所以若这些节点不可能全部是任一中央 polynomial 的零点，则奇数窗口的下界提高到 s+1。O7–O8 是自足有限代数证明；不从文献的实域零点交错或 Darboux admissibility 推出它。

### 2.1. Associated recurrence 与有限 formal functional

定义 A_j、B_j，j=0,…,R（最后一项只用于构造有限 quotient）：
\[
A_0=1,\ A_1=z-a_n,\qquad B_0=0,\ B_1=1,
\]
\[
A_{j+1}=(z-a_{n+j})A_j-b_{n+j}A_{j-1},
\quad
B_{j+1}=(z-a_{n+j})B_j-b_{n+j}B_{j-1}.
\tag{O9}
\]
由 O5 直接归纳，
\[
\boxed{f_{n+j}=f_n A_j-b_nf_{n-1}B_j.}
\tag{O10}
\]
A_j monic degree j，B_j degree j−1。原 recurrence 的非零 b_j 也证明 f_n 与 f_{n-1} 无共同零点：若一个共同零点存在，逐步倒推必使 f_0=0。

以下只构造一个有限 associated functional，不假设它的所有无限 profiles 非零。取 R阶 Jacobi multiplication matrix，diagonal a_n,…,a_(n+R−1)，上下相邻 entries 为1与 b_(n+1),…,b_(n+R−1)。在 A_0,…,A_(R−1) basis 中置 diagonal pairing
\[
\langle A_i,A_j\rangle=\delta_{ij}\gamma_j,
\qquad \gamma_0=1,\quad
\gamma_j=\prod_{h=1}^j b_{n+h}\ne0.
\]
modulo A_R 的 multiplication by z 对该 pairing 自伴随；这是相邻 entries 的直接核查。定义 mu(h)=〈1,h mod A_R〉，多项式乘法遂给
\[
\mu(A_jz^k)=0\quad(k<j),\qquad
\mu(A_jz^j)=\gamma_j\ne0\quad(j<R).
\tag{O11}
\]
尤其 mu 的所有 leading Hankel profiles 至 R阶均非退化。这个 construction 在任意域成立；不要求 eigenvalues、平方根或正质量。

写其 formal Laurent series
\[
C_\mu(z)=\sum_{k\ge0}\mu(z^k)z^{-k-1}.
\]
Pol 表示 polynomial part。O11 与 O9 准确给
\[
B_j=\operatorname{Pol}(A_j C_\mu),\qquad
A_j C_\mu-B_j=
\gamma_j z^{-j-1}+O(z^{-j-2})\quad(j<R).
\tag{O12}
\]
第一式可从 B0=0、B1=1 和相同 recurrence 归纳；乘 z 时多出的常数为 mu(A_j)=0（j≥1）。第二式只是 O11 的逐项 Laurent 展开，不是解析渐近。

### 2.2. 低秩迫使 rational pair 的余项严格 proper

设 q=rank E，先考虑 2q<R 的情形（否则 O7 已显然）。此时 q+1<R，故前 q+1列有一个非零线性关系，记最高非零指标 l≤q。令
\[
A=\sum_{j=0}^{l}c_jA_j,\qquad
B=\sum_{j=0}^{l}c_jB_j.
\]
deg A=l、deg B≤l−1。取 gcd g，e=deg g，A_*=A/g、B_*=B/g，t=l−e。于是 A_*、B_* coprime，deg A_*=t、deg B_*≤t−1。删去 g 为零的节点，剩余 M≥R−e 个。

O10 给剩余每个节点
\[
(f_n(z_i),-b_nf_{n-1}(z_i))
=c_i(B_*(z_i),-A_*(z_i)),\qquad c_i\ne0.
\tag{O13}
\]
其理由是两个向量都非零，且 A_*、B_* coprime；无需除某个可能为零的 evaluation。故剩余 rows 经非零 scaling 后等于 polynomial evaluations
\[
\Delta_j=A_j B_*-B_j A_*.
\tag{O14}
\]
对 j≤q+1，deg Δ_j≤q+t≤2q−e<R−e≤M。因此这些列的 polynomial evaluation 单射，且其 polynomial span 秩≤q。q+2个 polynomials 至少有两个独立恒等线性关系。

定义
\[
R_*(z)=A_*(z)C_\mu(z)-B_*(z).
\tag{O15}
\]
任一 Δ-polynomial 的线性关系给 (A',B')=(h A_*,h B_*)，因为两个 starred polynomials coprime。O12 的 linearity 给 B'=Pol(A'C_mu)，所以
\[
\operatorname{Pol}(hR_*)=0.
\tag{O16}
\]
若 R_* 有非零 polynomial part，则对任何非零 polynomial h，hR_* 的最高 nonnegative Laurent power 不可能消失。O16 因而只容 h=0，从而只容零 coefficient relation，和上面的至少两个关系矛盾。于是 R_* 严格 proper。

R_* 不可能为0；否则 mu(z^k A_*) 对 k=0,…,t 全为0，违背 O11 的 (t+1)阶 leading Gram 单位。因此
\[
R_*=c z^{-v-1}+O(z^{-v-2}),\qquad
c\ne0,\quad0\le v\le t.
\tag{O17}
\]
v≤t 同样由 (t+1)阶 Gram 单位推出。这里的严格 proper 性不是预先添加的 Padé 条件，而是低秩在足够多不同节点上被迫产生的条件。

### 2.3. 已知非零 norms 阻止过长低秩

对 j≥t，O12 给
\[
\Delta_j=-\operatorname{Pol}(A_jR_*),
\tag{O18}
\]
因为 A_*(A_jC_mu−B_j) 无 polynomial part。对 j≥t+1，O17 因而准确给 deg Δ_j=j−v−1，leading coefficient 为−c。

取
\[
t+1\le j\le\min(R-1,R-e+v).
\]
这些 polynomials 具有不同非负次数，且每个次数<M，因此其在剩余 M节点上独立。故
\[
q\ge R-t-1-\max(0,e-v-1)
\ge R-l-1\ge R-q-1.
\tag{O19}
\]
空区间时同一计数是0；在当前 2q<R、l≤q 的范围，最后下界非负且用于上述实际区间。于是 2q≥R−1，证明 O7。论证不使用复数符号、实域 positivity 或节点排序。

## 3. 奇数维极小秩必是全部中央零点

设 R=2s+1≥3 且 q=s。2q<R，上一 proof 全部适用。O19 的更精确计数还迫使
\[
e=0,\qquad t=l=s.
\tag{O20}
\]
确实若 e≥1，则 max(0,e−v−1)≤e−1，O19 给 q≥R−l≥s+1；若 e=0而t<s，仍有 q≥2s−t≥s+1。

此时没有删节点。对 j<s，deg Δ_j≤j+s−1≤2s−2；对 j≥s，O18 给 degree≤j−v−1≤2s−1。故全部 R列 polynomial evaluation 均单射，polynomial Δ-block 的 nullity 为 s+1。

每个恒等关系均为 (A',B')=(h A_*,h B_*)，deg h≤s。由 O17，Pol(hR_*)=0 当且仅当 deg h≤v。因此该关系空间准确为 v+1维。于是 v=s，O11 的 monic normality 迫使 A_* 为 A_s 的常数倍，B_* 为 B_s 的同一倍。原节点关系 O10 遂是
\[
f_{n+s}(z_i)=0\quad\text{全部 }i.
\tag{O21}
\]

反向，若 O21 成立，A_s 与 B_s coprime（由 recurrence 的 adjacent Casoratian product 为非零 b 的乘积直接证明），故 O13 在全部节点成立且 starred pair 可取 (A_s,B_s)。O12 给 R_*=gamma_s z^(−s−1)+…；j≥s 时 Δ_j 次数≤j−s−1，j<s 时用 O12 另一项的 polynomial part 得次数≤s−j−1。因此全部 Δ_j degree≤s−1，rank≤s；j=s+1,…,2s 的次数准确0,…,s−1且 leading coefficient 非零，又给 rank≥s。这完成 O8 的双向分类。

O8 本身说明一般准定性不能自动提高为满秩：奇数窗口若把节点全选为中央 polynomial 的不同零点，其极小秩确可出现。本稿提高 actual Racah 的界时必须额外排除这个具体机制。

## 4. 实际 Racah 的 regular 差分边界排除中央零点

实际 O2 的 monic polynomials 满足 O5，b_j=omega_j/omega_(j−1) 单位；取 n=2r、R=r，目标 columns 的 degrees至3r−1。有限 associated quotient 至多再用下一项 p_(3r) 确定最后 recurrence coefficient，仍完全处于冻结 M8 的已证 degree≤4r 范围内。节点 i²，i=0,…,r−1，在 F 中互不相同。

KS PDF30 Eq1.2.5，代入冻结参数 (−4r−1,−10r−1,−4r−1,6r)，再置 k=x+r，准确给 y(k)=R_n^L(k²)：
\[
n(n-14r-1)y(k)
=B_0(k)\bigl(y(k+1)-y(k)\bigr)
\mathbin{+}D_0(k)\bigl(y(k-1)-y(k)\bigr),
\]
\[
B_0(k)=\frac{(k-5r)^3(k+r)}{2k(2k+1)},\qquad
D_0(k)=\frac{(k-r)(k+5r)^3}{2k(2k-1)}.
\tag{O22}
\]
这是同一 R_n^L polynomial 的有理身份。x=−1、即 k=r−1≥1 时，所有 displayed denominators 单位，且
\[
B_0(r-1)=-\frac{(4r+1)^3}{2(r-1)}\ne0.
\tag{O23}
\]
若一个 R_n^L 在全部 i²、i<r 上为0，特别 y(r−2)=y(r−1)=0；在 k=r−1 应用 O22 即给 y(r)=0。但 x=0 的 O2 定义给 R_n^L(r²)=1，矛盾。

注意：k=0 的有理差分算子有 removable combination，却可能含 jet；本 proof 从未在这个 singular origin 代入，实际只在 k=r−1≥1 运算，r=2时也合法。KS Eq1.2.5 的 polynomial/rational身份先成立于通常参数，再经 normal denominators 约化，在当前负 x=−1 仍合法；未把文献的正支持范围当作有限域符号。

于是 r≥2 时任何中央 polynomial 都不可能在这 r个 omitted nodes 全部为0。r偶数时 O7 直接给 rank E≥r/2；r奇数≥3时 O8 排除 rank=(r−1)/2，给 rank≥(r+1)/2。完成 O4 第一条。

## 5. determinant 恒等式提升为准确 kernel 同构

令 W-space=F[u]_(degree<2r)，其 Phi Gram 的 kernel 为
\[
\mathscr K_\Phi=\{W:\Phi(WT)=0\text{ 对全部 }\deg T<2r\}.
\]
乘 m 给 f=mW，degree f<3r。O1 给 L(fT)=0，O2 完整 normality 因而等价于
\[
f\in\langle p_{2r},\ldots,p_{3r-1}\rangle.
\]
同时 f 在所有 i²、i<r 为0。因此
\[
\boxed{W\longmapsto mW
\quad\text{给 }\mathscr K_\Phi\simeq\ker\mathcal E.}
\tag{O24}
\]
反向，E核中的 coefficients 给一份 high polynomial f；不同 omitted roots 的 factor theorem 给 m整除f，其唯一商 W degree<2r，L-orthogonality 即是 Phi radical 条件。这不除 Phi、E 或任何未知 norm；只用已证单位的 L leading profiles。

O24 在 singular gate 时也成立，比冻结 M10 的 determinant identity 更明确地控制实际缺陷维数。结合第4节，准确得到
\[
\operatorname{rank}\Phi^{[2r]}
\ge2r-\lfloor r/2\rfloor.
\tag{O25}
\]
所有变换只在当前有限处定义相同实际 kernel，没有改动 global lattice 或计算任何 archimedean 费用。

## 6. 新收益、限制及下一问题

本轮从“r阶未知 determinant”推进为可证明的全辅助域缺陷上界：r≥2 时缺陷最多 floor(r/2)。证明还完整分类了任意域上一般 odd-window 极小秩机制，并用真实差分边界排除它；不是将上一 determinant公式重复记为新结果。

未证明 rank E=r、Phi^[2r]非退化，未证明 D_high 非退化或相同 rank 下界，未证明 restricted-H、fixed M5无限单位、actual higher Smith 或 fixed rational source无限成功。Phi完整2r form 的 radical 已受控，但一个 r维 subspace 的压缩仍可额外退化；不能直接把 O25 传给第三-Racah high basis。无新ζ/L/Catalan无理性或线性无关性结论，无Lean。

本稿仅在假设 2 rank E<r 时，由足够多节点逼出 O15–O17 的严格 proper 条件；实际 rank 已至少 ceil(r/2)，不能把该条件无偿移到仍可能存在的中间秩 kernel。提高到满秩需要另建适用更宽窗口的 interpolation/差分边界控制，或直接证明实际 structured minor 不相消。这些加强没有在本稿中预先假设。

## 7. 文献与实际读域

复用 Koekoek–Swarttouw 作者报告 [primary URL](https://tudelft.roelofkoekoek.nl/documents/as98.pdf)、[冻结本地PDF](../literature/cdt_paired_pearson_rankone_sources_20261006/koekoek_swarttouw1998_askey_scheme_report98_17.pdf)，SHA `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`，737178bytes，170归档页。本轮实际完整文本 PDF28、29、30，共3 distinct pages；Eq1.2.1、norm、monic recurrence及Eq1.2.5完整差分式实际已读。不声称170页全文读完。

在线搜索了 multivariable Selberg/Racah 和 Casoratian 原始文献方向，未套用其 generic normalization、positive domain 或未匹配的 balance，也未下载重复原件。本稿 O7–O21 用自足 finite-Jacobi/Laurent证明；O22 的 primary 源为上述实际读过的KS页。新数学 producer/source0，新增PDF0，TLS bypass0。一次PDF文本输出遇到终端GBK encoding错误，修正stdout UTF-8后完成阅读；这只是文献读取，不是数学失败或重跑。

状态：NEW 完整候选纸证，等待实际全文独立审阅、作者最终回读和最后一向来源收据。540既存记录不改动，不提前声明审阅已完成。
