# 真实核方向的连续—离散相对谱：原高列指数通道与首次 jet 的精确损失

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority 为 main §§171–175 和 delivery_kernel_profiles 快照 SHA313ad01a4abe88dd8a8193561b30232dfa131c8832d126af18390eafc8514e72；572 旧冻结记录（567 数学、5 guards）只读。唯一 NEW 主稿，纯纸证；数学 producer 创建/execute/import/rerun、辅助 prime 扩表、Lean 均0。以下谱结论在原饱和 basis 同时使用 P 与 V；不以任意核 height 代替真实核方向，不把充分条件当作新的特殊值无理性结论。

## 1. 本轮读域、原对象与新增结果

本轮 actual FULL 回读：primitive-kernel K1–K18/all8节；mixed-node entropy S1–S27/all10节；Hasse H1–H17/all8节；coupled C1–C23；actual-local G1–G15；compound analytic A1–A27/all10节；original lattice I1–I25；Hasse arithmetic J1–J18/all7节；primitive-gcd G1–G13。Hasse 初次组合输出的省略段已另实际补读 H8–H13；不把省略的输出算全文。当前总稿实际读 §§171–175。Audit 完整 JSONparse/header/current_progress；一次过宽字段输出截断后只据实际读到的字段、schema 与计数字段描述读域，不称人工全文读全部572记录或本人全量物理 SHA 审计。旧 successful producer/结果/guard 没有执行、import 或重跑。

固定真实源
\[
\xi=\alpha\zeta(4)+\beta\zeta(5),\quad \alpha,\beta\in\mathbf Q,\quad\beta\ne0,
\]
原 degree<3n、rank m=2n 的饱和整数值 basis 为
\[
g=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\qquad
f_i(z)=\binom{z-1}{i}.
\tag{R1}
\]
在原数值 ξ 的真实轮廓上
\[
B_{ij}=\int g_i g_j\,d\mu,\quad
P_{ij}=\int g_i\overline{g_j}\,d|\mu|,\quad P>0,
\]
\[
V=24\sum_{j=0}^{6n}W_j\,v_jv_j^t>0,\quad
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad v_j=(g_i(-j))_i.
\tag{R2}
\]
这里 B=B_n(ξ)，原 affine pencil 为 B_n(X+t)=B_n(X)+tV。原 real symmetry、degree、节点及 source 权重不改。定义
\[
J_k=[t^k]\det(B+tV),\qquad H_k=[t^k]\det(P+tV).
\tag{R3}
\]
冻结 H13 给 |J_k|≤H_k，不能把 k0 的较强 full determinant 界搬给 k>0。

本稿得到两个自足新结论。一是原相对 Gram 至少 n 个特征值指数级大：
\[
R=P^{-1/2}VP^{-1/2},\qquad
\boxed{\lambda_n(R)\ge c(n+2)^{-C}e^{a_*n},\quad
a_*=\frac{17}{2}-6\log3+2\log2>\frac{13}{4},}
\tag{R4}
\]
λ 按降序；c,C 只依赖固定源。于是每个0≤ν≤n有
\[
\boxed{\log e_\nu(R)\ge a_*\nu n-O(n\log(n+2)).}
\tag{R5}
\]
这是原真实高列/负节点的全尺度定理；不是 finite sampling 或自由子空间猜测。

二是若假设 ξ=c∈Q，令 actual rank d、ν=m−d，并在无限已证适用 n=4r 上取 ν≤n/2 的真实 primitive 核基 K，则
\[
\boxed{|J_\nu|=H_\nu\,\mathcal L_K\,\Theta_d,\qquad
\mathcal L_K=\frac{\det(K^tVK)}
{\det(K^tPK)\,e_\nu(R)}\in(0,1].}
\tag{R6}
\]
Θ_d 是原 phase compression 的非零 d 个 singular values 的乘积；ν0 时空 det=1、\(\mathcal L_K=1\)。R6 准确拆出原 mixed 正包络相对真实首次 jet 的损失，不付一个人为选择的 kernel height。尚未证明 \(-\log\mathcal L_K\) 或 \(-\log\Theta_d\) 有足够 n² 主率。

## 2. 原 high 负节点评价矩阵的显式逆

只取已有 source 节点 j=0,…,n−1，原 high 列 k=0,…,n−1。在这些节点，
\[
f_{2n+k}(-j)=(-1)^{2n+k}\binom{2n+k+j}{j}.
\]
去掉列 signs，置 \(Y_{jk}=\binom{2n+k+j}{j}\)。Vandermonde 恒等式给 exact 整数分解
\[
Y=AB,\qquad
A_{jl}=\begin{cases}\binom{2n+j}{j-l}&l\le j,\\0&l>j,\end{cases}
\quad
B_{lk}=\begin{cases}\binom{k}{l}&l\le k,\\0&l>k.\end{cases}
\tag{R7}
\]
两矩阵 triangular、diagonal1；这不是声称 actual B 高块为 unit。

其逆完全明确：
\[
(A^{-1})_{jl}=(-1)^{j-l}\binom{2n+j}{j-l},\qquad
(B^{-1})_{lk}=(-1)^{k-l}\binom{k}{l}.
\tag{R8}
\]
A 的乘法检查使用
\[
\binom{2n+j}{j-r}\binom{2n+r}{r-l}
=\binom{2n+j}{j-l}\binom{j-l}{r-l}
\]
和 \(\sum_{q=0}^{j-l}(-1)^q\binom{j-l}{q}=(1-1)^{j-l}\)；B 同理。故 detY=1，所有有限 n 及 j0、k0 都被包含。此 determinant 用于一个明确的 source evaluation 下界，不是原 whole determinant 非零证书。

对 n×n 矩阵，operator norm≤Frobenius norm≤n·maxentry。由于 j−l≤n−1、2n+j≤3n−1，
\[
\|A^{-1}\|\le n\binom{3n}{n},\quad
\|B^{-1}\|\le n2^n,\qquad
\boxed{\|Y^{-1}\|\le n^2\,2^n\binom{3n}{n}.}
\tag{R9}
\]
binom(3n,q) 在0≤q≤n非降，故这里没有遗漏较小 q 的大 entry。列 sign 矩阵正交，保持 singular values。

## 3. 完整 source 权重与原连续 high 费用共同给指数通道

原 W_j 是正整数，故每个 W_j≥1，未换成带符号权重或删除 source 常数24。保留真实列 sign 矩阵 D=diag((-1)^(2n+k))，只取前 n 节点得到 Loewner lower
\[
V_{hh}\succeq24\,D Y^*Y D
\succeq24\,n^{-4}\,4^{-n}\binom{3n}{n}^{-2}I_n.
\tag{R10}
\]
这里下标 hh 只指原 n 个 high 坐标，不是另选一个任意 high basis。

二项分布单项≤1给
\[
\binom{3n}{n}\le
\exp[n(3\log3-2\log2)].
\]
所以
\[
\boxed{V_{hh}\succeq24\,n^{-4}
e^{-n(6\log3-2\log2)}I_n.}
\tag{R11}
\]
它比只从 detV 整性推出极差的最小特征值下界更具体：付清了 evaluation inverse 的全部指数 norm，不以 detY1 冒称 \(\|Y^{-1}\|=1\)。

冻结 A12 在同一原高列给统一 diagonal bound
\[
P_{n+1+k,n+1+k}\le C_0(n+2)^{C_1}e^{-17n/2}.
\]
正 Gram 的 λmax≤trace，因此
\[
\boxed{P_{hh}\preceq C_0 n(n+2)^{C_1}e^{-17n/2}I_n.}
\tag{R12}
\]
这里所有 high factorial、真实轮廓 W 与 exponential tail 已由本轮 FULL 读的 A11–A12 支付；不从另一个基借 bound。

由 R11–R12，对每个原 high 子空间中的非零 x，
\[
\frac{x^*Vx}{x^*Px}\ge
\frac{24}{C_0}\,n^{-5}(n+2)^{-C_1}e^{a_*n}.
\tag{R13}
\]
映射 y=P^{1/2}x 是可逆的，其 high image 维数恰 n，且商为 y*Ry/||y||²。Hermitian min-max 因而证明 R4。至少 n 个 eigenvalues≥同一右端，取其中任意 ν≤n 的 product，得 R5；组合数未被当作 n² 主率。

常数比较也不用数学程序：冻结 S11 的有理 log 界给
\[
\log3=\log2+\log(3/2)<10987/10000,\qquad
\log2>693/1000.
\]
故
\[
a_*>\frac{17}{2}-6\cdot\frac{10987}{10000}
+2\cdot\frac{693}{1000}
=\frac{16469}{5000}>\frac{13}{4}.
\tag{R14}
\]
最后余量为219/5000。可把 a_* 放宽为13/4得到纯有理指数通道，但以下保留准确 a_*。

## 4. 真实 moment-annihilator与原 Schur 商

现在只在有理性假设 ξ=c 下使用完整 primitive 核格
\[
K\text{ 为 }\ker B\cap\mathbf Z^m\text{ 的完整基},\quad
U=[L,K]\in GL_m(\mathbf Z),\quad
U^tBU=\operatorname{diag}(C,0),\quad q=\det C\ne0.
\tag{R15}
\]
冻结 K1–K5 已证明这种补全与首次因子化合法。K 对应的 polynomials 满足真正的 annihilator 条件
\[
\int \left(\sum_iK_{ia}g_i(z)\right)g_j(z)\,d\mu(z)=0
\quad(1\le a\le\nu,\ 1\le j\le m).
\tag{R16}
\]
不是只对几个 sampled moments 为0；其 Hermitian norm \(\det(K^tPK)\) 仍正。

记 \(a_P=\det(K^tPK)>0,\ a_V=\det(K^tVK)>0\)。真实首次 jet 是
\[
J_\nu=q\,a_V\ne0.
\tag{R17}
\]
P 按 U 的实际 Schur complement给 \(P_Q\)，准确
\[
\det P_Q=\det P/a_P.
\]
complex kernel shear使用冻结 K8 的 conjugation 约定，q不变；\(|q|\le\det P_Q\)。不能从 BK0推出 P 的 cross block为0，也不能把连续 measure 与离散 source 免费交换。

为证明比 upper 更精确的 phase 身份，令 E 为 U^{-t} 前 d 列，B=ECE^t，取
\[
T=P^{-1/2}B(P^{-1/2})^t,\qquad
\Theta_d=\prod_{i=1}^d\sigma_i(T)>0.
\tag{R18}
\]
实际 phase contraction使各 σ_i≤1。rank-d compound为
\(C_d(T)=q\,w w^t\)，其中 w 是 \(P^{-1/2}E\) 的 d 阶 wedge。complex rank-one 对称矩阵 \(w w^t\) 的唯一非零 singular value为||w||²。因此
\[
\Theta_d=|q|\det(E^tP^{-1}E).
\]
Jacobi 互补 minor 身份应用于 U^tPU（detU²1），其 inverse 前 d block恰 E^tP^{-1}E，得
\[
\boxed{\Theta_d=|q|\frac{a_P}{\det P},\qquad
|q|=\frac{\det P}{a_P}\Theta_d.}
\tag{R19}
\]
这一步保留非零 phase 乘积而非已为0的 full detT。ν0 同样成立。R19在这里自证，不把 root 尚未冻结的新稿视为已读输入。

## 5. 连续—离散相对核损失的精确身份与不变性

正 Gram 特征多项式给
\[
H_\nu=\det P\,e_\nu(R).
\tag{R20}
\]
令 \(A=K^tPK\)，
\[
F=P^{1/2}K A^{-1/2},\quad F^*F=I_\nu,\qquad
R_K=F^*RF=A^{-1/2}(K^tVK)A^{-1/2}>0.
\]
\[
\boxed{\det R_K=a_V/a_P,\qquad
\mathcal L_K=\det R_K/e_\nu(R).}
\tag{R21}
\]
Hermitian compression 的最大ν个 product不超过R最大ν个 product，后者≤eν(R)，故0<\(\mathcal L_K\)≤1。ν∈(0,m)时 eν 是全部 positive products 的和，严格大于最大的单项，故 \(\mathcal L_K<1\)；此严格有限差不自动有 n²率。ν0空compression、e01给 \(\mathcal L_K=1\)。

将 R17/R19/R20结合，证明 R6 的 equality。它将真实核商、kernel source factor、原 mixed 正包络和真实 nonzero phase 连在同一首次 Jν 上。若选一个高height自由核而非实际 BK0，R17/R19不成立。

另一个完全等价且经常更方便的离散归一化为
\[
M=V^{-1/2}PV^{-1/2},\quad
Z=V^{1/2}K(K^tVK)^{-1/2},\quad Z^*Z=I_\nu,
\]
\[
\boxed{\mathcal L_K=
\frac1{\det(Z^*MZ)\,e_\nu(M^{-1})}
=\frac{\det M}{\det(Z^*MZ)\,e_d(M)}.}
\tag{R22}
\]
R 和 M^{-1}具有相同 eigenvalues，理由是 AB 与 BA的正 definite相似关系；\(e_d(M)=\det M\,e_\nu(M^{-1})\)。所有 Gram 同时变基，不能对 P 单独剪切再保留旧 V。

K任意可逆基变换同时乘 aP、aV 同一个 |det|²，故 R21不变。原 ambient实可逆变基同时变 B,P,V,K时 generalized eigenvalues与R_K的 determinant也不变。Jν与Hν同乘det²，所以 R6总比值不变。这里没有 primitive kernel covolume的人为增高，没有新增 finite-place index；q自身的算术不能因除去 aV而无偿继承 whole-jet 整性。

## 6. 可量化的相对谱信用与它的必要尺度

定义真正的核方向信用
\[
\mathfrak c_K=-\log\mathcal L_K
=\log e_\nu(R)-\log\det R_K\ge0.
\]
若 \(\rho_{\min},\rho_{\max}\) 为 R 的极端 eigenvalues，则 compression interlacing及 elementary sum 给
\[
\det R_K\ge\rho_{\min}^{\nu},\quad
e_\nu(R)\le\binom m\nu\rho_{\max}^{\nu},
\]
\[
\boxed{0\le\mathfrak c_K\le
\log\binom m\nu+\nu\log\operatorname{cond}(R).}
\tag{R23}
\]
m=2n时 logbinom≤2nlog2。因此若实际 logcond(R)=o(n)，这个 kernel-relative credit只有o(n²)；单纯有 ν~κn个方向或固定谱亏损不够。相反大 cond也是必要性提示，不能从它反推实际 kernel 已得到信用。

本稿真实原高列 R5进一步给
\[
\boxed{\mathfrak c_K\ge
a_*\nu n-\log\det R_K-O(n\log(n+2)).}
\tag{R24}
\]
若实际原kernel的全部 relative compression eigenvalues≤b_n，得
\(\mathfrak c_K\ge\nu\log(a_n/b_n)\)，其中 a_n是R4右端。更一般只需实际 determinant upper
\[
\log\det R_K\le b\,\nu n+o(n²),\quad b<a_*,
\]
并有ν/n→κ>0，即得
\[
\liminf n^{-2}\mathfrak c_K\ge\kappa(a_*-b)>0.
\tag{R25}
\]
这给一个具体原节点常数 a_*>13/4 的新目标，替代任意核height lower。R24本身已无条件成立；R25中的 kernel upper尚未证明。

可用真正 min-max 测试该 upper：若 \(\Pi\) 是 R 的某个 large-spectrum spectral projection，且 A≥b>0、0≤η≤1，并有
\(R\preceq bI+(A-b)\Pi\)、\(F^*\Pi F\preceq\eta I\)，则
\(R_K\preceq[b+(A-b)\eta]I\)。
这是 actual P-normalized kernel和 actual R同一空间的条件；一个在原 Euclidean规范里很小的坐标 projection不能免费代替它。若A/b指数级大，只有固定η<1一般仍不足，需相应指数级小的η或 determinant层面更精细的方向估计。

## 7. 有限 signed-moment反例：annihilator、degree与rank本身不给净信用

以下纯纸构造只检验“moment-annihilator + integer-valued degree<3n + SPD source + rank≥3n/2”这组一般条件；它不属于原paired-head/cot/W_j模型，不是原问题或所有方法的no-go。

取 n为4的倍数、m=2n、ν=n/2、d=3n/2、N=d+2ν=5n/2<3n。负连续整数节点 −s（0≤s<N）的cardinal
\[
\ell_s(z)=\binom{-z}{s}\binom{N-1+z}{N-1-s}
\]
degree N−1、integer-valued、\(\ell_s(-t)=\delta_{st}\)。取m个整数值 polynomials：前d个为\(\ell_0,\ldots,\ell_{d-1}\)，后ν个为
\(h_j=\ell_{d+2j}+\ell_{d+2j+1}\)。
它们形成其span的完整primitive基；在N个evaluation整数坐标，每pair的sum可由一个single cardinal补成2×2unimodular基。全部cardinal再加 degree N,…,3n−1 的反射Newton列 binom(−z,i) 完成 ambient整数值格：后者在这些负节点全为0，前N阶反射Newton评价矩阵是整数unimodular。没有非整插值分母。

置ε=2^{-n²}，取
\[
d\mu=\sum_{s<d}\delta_{-s}
+\frac\epsilon2\sum_{j<\nu}
(\delta_{-(d+2j)}-\delta_{-(d+2j+1)}),
\]
\[
d\sigma=\sum_{s<d}\delta_{-s}
+\sum_{j<\nu}\delta_{-(d+2j)}.
\]
这是一组 finite real signed moments与positive source，literal各Gram为
\[
B=\operatorname{diag}(1^d,0^\nu),\quad
P=\operatorname{diag}(1^d,\epsilon^\nu),\quad V=I_m.
\tag{R26}
\]
B+tV整多项式，primitive K最后ν个coordinate directions；全部R16 moments恰为0，rank d，首次 Jν=1、q=1、aV1。phase T=diag(1^d,0ν)，所以Θ_d=1。

但是
\[
H_\nu=e_d(P)=\sum_{\ell=0}^{\nu}
\binom d\ell\binom\nu\ell\epsilon^\ell,\qquad
\mathcal L_K=H_\nu^{-1}.
\]
由 \(\binom d\ell\binom\nu\ell\le(d\nu)^\ell/(\ell!)^2\)，
\[
\boxed{0<-\log\mathcal L_K=\log H_\nu
\le d\nu\,2^{-n²}\longrightarrow0.}
\tag{R27}
\]
尽管 R具有ν个极大的relative eigenvalues，真实kernel恰占这些昂贵方向，分母eν的收益被detR_K抵消。这证明必须使用真实paired/轮廓/source几何来估方向；R16本身不会迫使positive P norm大，也不会给R25。这里有限构造没有创建或执行数学producer，没有把原degree范围相同偷换为原空间相同。

## 8. 原首次jet的完整费用比较与仍未达成的目标

在假设 ξ=c 的无限适用 n=4r上，原actualν≤n/2、Jν≠0。设κ_n=ν/n，\(\mathfrak p_n=-\log\Theta_d\ge0\)。R6及冻结S4给真正的 same-object upper
\[
\log|J_\nu|\le
\left[-\frac{22}{3}-2\gamma+
\kappa_n(\Theta+\frac{17}{2})\right]n²
-\mathfrak c_{K_n}-\mathfrak p_n+o(n²),
\quad \Theta=K_3<11557/400.
\tag{R28}
\]
每项都作用同一original Jν；原Γ只在S4支付一次。R6的relative ratios已包含所有source norms，无第二次gcd信用。此处Θ是节点熵常数，Θ_d是nonzero phase product，二者不同。

本轮 FULL 读的 arithmetic J16/J18给同一ν全部有限处safe尺度
\[
|J_\nu|\ge\exp[-(A_{\rm full}-5\kappa_n²/4)n²-o(n²)]
\]
和固定(DM)^{2n-ν}整数因子；D、M均固定、O(n)费保留。因此一个明确充分条件是在同一无限subsequence上
\[
\boxed{\liminf\left[
\frac{\mathfrak c_{K_n}+\mathfrak p_n}{n²}
-A_{\rm full}+\frac54\kappa_n²+\frac{22}{3}
+2\gamma-\kappa_n(\Theta+\frac{17}{2})
\right]>0.}
\tag{R29}
\]
它不是达成结论。κ可为0，此时\(\mathfrak c=0\)，需要独立phase/更强full-det或更低算术费；不能给所有adaptive阶数套half费用。若研究primitive商q，应另用其actual-rank完整整化；R17里的aV不能被免费除掉。原q的rank-model upper以及今后新的q费用需独立同对象审阅，不把partial41移给jets。

目前没有实际 \(\log\det R_K\) 的充分upper，没有Θ_d的充分n²损失，没有R29 strict margin。R4–R5是新的真实n²谱通道；R24把它精确定位到需要控制的kernel compression，R27排除了仅凭一般annihilator条件的免费推论。尚无新的ζ/L/Catalan数值无理性、线性无关性或Lean结论。

## 9. 来源、边界与归档状态

新增PDF/HTML/code下载0，本轮原始PDF实际读页0；不继承旧root/peer原件页域。新证明只用已经实际全文读的原定义，并自证finite binomial inverse、Loewner、min-max、Jacobi compound、relative coefficient identity、conditional compression及边界反例。无数学producer、无prime表或auxiliary-prime延伸。

下一真正算术敏感解析目标是R24中的actual kernel determinant upper，或同一原phase的nonzero singular-value损失；不能只在自由kernel上造height、令μ moments消失后删除|μ|norm、或以large-spectrum存在替代方向估计。准确counterexample只限第7节的一般Gram条件，不排除原paired/离散—连续系统的更强结构。本文唯一NEW完整候选待actual FULL独审、作者收审后最终FULL回读及单向FINAL来源收据；572旧冻结记录仍不改动。

