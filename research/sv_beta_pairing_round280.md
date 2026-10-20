# 第280轮：非对角复Beta精确分解与固定9jet的秩裁决

2026-10-20。完成[280一轮来源核查](sv_beta_pairing_charter_round280_20261020.md)。根恢复实际goal为active、工作树干净、修订20的STATE/权威账，读取AGENTS、长期goal、279决定、周期来源及章程。上一goal turn完成279独审、宏观决策、状态及精确提交的云端检查，分类为progress；279的数学feasibility_progress=false与这个turn分类分开。

**结论：原候选非对角因子式成立；固定九阶系数矩阵在m≥8时实际秩恰8、惯性为(4,4,m−8)，m≥9的行列式恒零，ζ7系数矩阵实际秩恰1。该增长Gram实现按一轮停止条件关闭。** 这是同一实际正则化对象的全尺度证书，不是新的无理性定理，也不否定全部单值周期或变化jet的构造。

## 1. 实际对象、反证和来源

固定Q(z)=z(1−z)、i,j=1,…,m，全部参数与[279对角身份](period_source_gate_round279.md)一致：
\[
I_{ij}(t)=\frac1\pi\int_{\mathbf C}
Q(z)^i\overline{Q(z)^j}|z|^{2t-2}|1-z|^{2t-2}d^2z,\quad
\mathcal K_{ij}(t)=\frac t2\operatorname{AC}I_{ij}(t),\quad
M_m=([t^9]\mathcal K_{ij}(t)).
\]
每对(i,j)的绝对收敛条带由0、1、∞的径向幂精确给出
\[
-(i+j)/2<\operatorname{Re}t<(1-i-j)/2.
\tag{S280.1}
\]
定义取实对数的模幂及整数多项式Q^i、barQ^j，没有额外分支选择。先在各自条带积分，再作明确亚纯延拓；不假设整矩阵共享同一条带。t作复变量，barQ没有把t变成bar t。

数值目标仍是新的ζ7无理；全部反证ζ7=u/v、u∈Z、v>0、gcd=1。ζ3、ζ5、ζ3²不假设有理。若实际纯多项式Q_m有degree d_m，整系数清整λ_m，则必须同一预定无界子列上非零且对每个v满足
\[
\log\lambda_m+\log|Q_m(\zeta7)|+d_m\log v\longrightarrow-\infty.
\tag{S280.2}
\]
本轮将在这一步以前精确证出原行列式恒零，不能以费用或形式函数秩绕过非零要求。

独立证明稿为[非对角公式](sv_beta_formula_round280.md)、[锐秩与整数坐标](sv_beta_rank_round280.md)、[反证及来源独审](sv_beta_independent_round280.md)。根另独立推导下列Schwinger积分链和代数分解，再逐式交叉核查；作者不自作独审。

## 2. 从实际收敛积分证明非对角公式

先令i≥j、d=i−j、s=t+j，并取S280.1中的实t。则
\[
I_{ij}(t)=\frac1\pi\int Q(z)^d
|z|^{2s-2}|1-z|^{2s-2}d^2z,\qquad
-d/2<s<(1-d)/2.
\]
用两个正Laplace参数表示模幂，1−s>0：
\[
|z|^{2s-2}=\Gamma(1-s)^{-1}
\int_0^\infty u^{-s}e^{-u|z|^2}du.
\]
带绝对值的三重积分由Tonelli恰回到原绝对收敛积分，故复数多项式也可合法Fubini。对u,v>0，圆对称复Gaussian的全纯矩给
\[
\frac1\pi\int_{\mathbf C}Q(z)^d
e^{-u|z|^2-v|1-z|^2}d^2z
=\frac{e^{-uv/(u+v)}}{u+v}
\left(\frac{uv}{(u+v)^2}\right)^d.
\]
这是平移后每个非零全纯圆矩为0的有限多项式身份，不用未收敛的分部积分。

代入u=λx、v=λ(1−x)后，λ指数为−2s；依次积分得到
\[
I_{ij}(t)=
\frac{\Gamma(1-2s)\Gamma(s+d)^2}
{\Gamma(1-s)^2\Gamma(2s+2d)}
=\frac{\Gamma(t+i)^2\Gamma(1-2t-2j)}
{\Gamma(1-t-j)^2\Gamma(2t+2i)}.
\tag{S280.3}
\]
条件1−2s>0、s+d>0由上述实际条带满足。双方在复条带全纯，用恒等定理再按Gamma侧作唯一亚纯延拓。

Gamma递推相对于J(t,t)给
\[
\boxed{\mathcal K_{ij}(t)=B(t)v_i(t)v_j(t)},\qquad
B(t)=\frac t2J(t,t),\quad
v_i(t)=\frac{(t)_i^2}{(2t)_{2i}}.
\tag{S280.4}
\]
反射侧(1−t−j)_j的两个符号相乘为正，(1−2t−2j)₂j也为偶长度；没有残留phase。i<j由复共轭与实系数延拓得到同式，因而全i,j对称。对角精确回到279的K_i，归一和共轭均一致。

根另实际读[Neretin 2212.09112v2 §1.1–1.2，式(1.6)–(1.7)](https://arxiv.org/html/2212.09112v2)：取双指数(t+i|t+j)两次，Gammaᶜ的i幂在商中相消，也给S280.3及S280.1。这里只用作一手交叉核对；Schwinger证明自足支付本特化。旧来源个别收敛印误按独审稿保留，不照抄为本对象的域。

## 3. 完整周期和可审的8维矩阵

由重复Gamma恒等式
\[
v_i(t)=t w_i(t),\qquad
w_i(t)=4^{-i}\frac{(t+1)_{i-1}}{(t+1/2)_i},
\quad
a_{i,p}=[t^p]w_i(t)\in\mathbf Q.
\]
所有w_i在0正则，a_{i,0}=((i−1)!)²/[2(2i−1)!]>0。记B(t)=Σb_rt^r；固定9jet只需
\[
b_0=1,\ b_1=b_2=b_4=0,\quad
b_3=4\zeta3,\ b_5=12\zeta5,\ b_6=8\zeta3^2,\ b_7=36\zeta7.
\]
故没有新增周期，全部有理头与背景均保留：
\[
M_{ij}=\sum_{\substack{p,q\ge0\\p+q\le7}}
a_{i,p}a_{j,q}b_{7-p-q},\qquad
\boxed{M_m=A_m H A_m^{\,t}},
\tag{S280.5}
\]
其中A_m=(a_{i,p})，p=0,…,7，H=(b_{7-p-q})₀≤p,q≤7，负下标定义为0。

ζ7系数恰为36a₀a₀ᵗ，a₀=(a_{i,0})，所以对每个m≥1实际秩恰1。其它b_r没有假设数值独立；S280.5本身已给实际秩≤8。

## 4. 锐秩、惯性和全尺度停止

对任意k≥1，前k个w_i的低k阶系数矩阵A⁽ᵏ⁾可逆。根复核[秩稿](sv_beta_rank_round280.md)的一般证书：乘共同分母D_k(t)=(t+1/2)_k，得到degree k−1的多项式
\[
4^{-i}(t+1)_{i-1}(t+i+1/2)_{k-i}.
\]
在t=−j、j=1,…,k评价，i>j全零，对角非零。除Vandermonde及D_k(0)^k精确给
\[
\det A^{(k)}
=4^{-k(k+1)/2}
\frac{\prod_{r=0}^{k-1}(1/2)_r}{((1/2)_k)^k}>0.
\tag{S280.6}
\]
这不是数值样本或有限拟合。

H的反对角为1、反对角下侧为0，detH=(−1)²⁸=1。以p=0..3和4..7分块，H=[[C,D],[Dᵗ,0]]，D可逆；合同消去C后惯性为(4,4)。由A₈可逆和m≥8时A_m满列，
\[
\boxed{\operatorname{rank}M_m=8,\quad
\operatorname{inertia}M_m=(4,4,m-8)\quad(m\ge8).}
\tag{S280.7}
\]
尤其
\[
\det M_8=(\det A^{(8)})^2\in\mathbf Q_{>0},\qquad
\boxed{\det M_m=0\quad(m\ge9).}
\tag{S280.8}
\]
任意8×8子式也是两个有理A子式的乘积，任意9×9子式为0。这些是实际特殊值矩阵的结论，不依赖任何ζ代数独立猜想。m<8只保留已证上界，不从A满行在不定H中冒称M满秩。

所以原m增长行列式在每条无界子列上最终为0；任何清整、primitive内容、反证分母v或非零尺度因子都不能修复S280.2所需非零性。m=8行列式只是有理常数，也不隔离新的无理性。固定有限规模的其它minor、移动节点、增长jet、非多项式权或多变量来源不由此被全部否定；它们没有在本窗口得到净预算或准入。

## 5. 决定、范围和恢复交接

280来源核查按期完成并关闭。公式、完整周期和锐实际秩均已付；feasibility_progress=false，numeric_admission=false，连续未改善4。没有改善指定值的完整净预算，不以完整no-go、文件或独审重置计数；goal仍active且未实现。

同一因子式对任意固定J≥2立即给[t^J]矩阵秩≤J−1；这说明改成另一个固定jet不能生成无界规模非零行列式。J随m增长不在证书范围，重开须另有改变原秩障碍的真实机制，并付新高周期投影、全部费用、实际非零和净余量；不能仅提高jet数字续期。

最近正式宏观复盘仍279。新增一完成轮后，停滞4触发[281全路线比较](source_gate_charter_round281_20261020.md)，最多一轮；不在本turn提前执行，也不默认返回旧source。比较以279完整量级和本轮准确停止为输入，选择证据能改变最终接口的机制；若无合格者，只能给明确最小来源核查。

本轮没有数学CAS、参数/素数/规模扫描、历史producer或Lean构建。根逐式独核三稿；rank与audit另独核公式的自足积分链，formula与audit另独核锐秩及全k minor，audit另核根结算/281量词，均通过，实际范围按最终审核补记保存。仓库状态、资产、链接和CI只验证组织/保存，不能认证本数学证明。文献、形式化、原冻结清单及纠错链均保留。
