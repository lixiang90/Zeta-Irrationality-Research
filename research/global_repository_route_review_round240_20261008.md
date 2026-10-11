# 第240轮：当前仓库的真实机制与新源准入

2026-10-08，Alternative/A。数学程序0；外部仓库只读。结论是保留一个有界的新 whole-functional 试验，停止以239现有费用 upper继续推动原三维源。新试验的首关应是完整周期投影后的实际整数模型和增长尺度非零证书，不能仅靠目标系数秩、正核或已知常数分别无理。

## 1. 当前状态：没有相对236的新仓库提交

本轮新执行只读 HEAD、origin URL、status、最近五次 log及云端 ls-remote：
本地与远端 main/HEAD均为
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status为空；
origin为 https://github.com/openai/math 。这与236使用的228同步快照相同。
没有 fetch、reset、外部写入或 Lean执行。官方 GitHub页面也仍显示三个提交。

实际FULL读根 README/history、三个相关 preprint README；定向搜索 CONTENTS与目录名。
README说明719稿件的验证程度不同，不能把作者的形式化比例当成本文认证。
Oct7 history的三篇 Hodge/K3撤回、14项修订等仍是同一更新。
限定搜索中：Catalan稿声明 \(G\)无理；Deligne–Drinfeld稿声明形式 Lie代数的自由生成；
Dirichlet/Hecke相关摘要的零点区域并非 even \(L\)值无理性。
“Mahler”目录所指的是凸体体积积猜想，不能移作 Mahler measure周期定理。
没有在这些实际读域发现专门 \(\zeta_7\)、全部 odd \(\zeta\)，或
\(1,\zeta_3,\zeta_5\)数值线性无关的新声明。这个限定结论不证明全球文献不存在结果。
项目的 \(\zeta_5\)baseline来自独立来源，不能改写为 OpenAI math仓库的成果。

## 2. DD的正收益为何不能变成全部 odd-zeta定理

本轮实际完整选读 DD的 introduction及§7 holonomy，未审全文的 characteristic-2上界。
§7的规范是 \(\lambda=(2\pi i)^{-1}\)，regularized interval transport满足
\[
[x^{n-1}y]\Phi
=-\frac{\lambda^n}{(n-1)!}
 \int_0^1\frac{(-\log t)^{n-1}}{1-t}\,dt
=-\lambda^n\zeta(n).
\]
比较两种 holonomy的 operator logarithm后，odd \(n\ge3\)给
\[
[x^{n-1}y]\delta_n(\alpha)=2\lambda^n\zeta(n)\ne0.       \tag{R1}
\]
最后一步仅用正项级数。它支付一个 rational finite-dimensional coefficient
functional的非零，以及经 rational descent得到的形式 Lie生成元；
既不构造越来越小的整数线性形式，也不约束任何数值周期关系。
原文明确写出 “no arithmetic independence assertion”。
因此即使采用其整个形式结构定理，R1也不能解决任一个未知 odd-zeta无理性，
更不能作为目标隔离后的 nonzero/height桥。
来源为[当前作者§7](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/build/sections/07-holonomy.tex)。

## 3. Catalan机制：四个环节确实作用于同一个对象

实际FULL选读 foundations、odd-primes、nonvanishing、real-place、energy、
certificate、conclusion七节；没有以此冒称独立认证完整数值证书或全论文。
其 \(n=48N\)构造用两张代数 sheet \(w\leftrightarrow1/w\)给整多项式
\(P_r,D_r\)，接触条件消除全部指定列中的 \(\zeta_2\)通道。
原完整列池的条目成为 \(\mathbb Q+\mathbb QG\)，再用整数
\(s^{b+k}(1-s)^q\)列过滤构造同一 \(\Delta_N\)。
反证 \(G\in\mathbb Q\)只使这些条目为有理数，不会替代下一步非零证明。

完整 odd-prime处理保留 \(p^2\)层、边界 digit和 inverse列操作；
Cauchy–Binet将全部原池 minor的下界传给实际整数列过滤，而非只清一个 tail。
2-adic估计及完整 prime积分账于是给实际非零 determinant的 product-formula lower。
另一方面，二次 Andréief表示同时保留两类变量、一个 \(t\)-Vandermonde、
两个 \(s\)-Vandermonde，以及代数 sheet混合的 determinant。
uniform interpolation与 Hadamard分支的 \(e^{O(n\log n)}\)误差均被支付，
没有因评价矩阵可能病态而丢掉 separation依赖。

energy展开保留耦合负平方，形如
\[
-\kappa\sum_{k\ge1}\frac{A_k^2}{k}
-\frac12\sum_{k\ge1}\frac{(B_k-2C_k)^2}{k}.             \tag{R2}
\]
这不是删去一个 species再沿用原最小增长率。
证书节用固定 rational trial、完整临界点计数、端点与余项控制给严格 upper。
作者原稿比较的是同一归一化
\(\log|\Delta_N|/n^2-\tfrac12\log2\)：
lower大于 \(-2.29084\)，upper小于 \(-2.2909\)。
本文读取证书的算法与范围，没有复跑其中的有限消元、pivot或数值常数。

可移植的是“完整 period stack → 整数列过滤 → all-prime模型 → actual∞nonzero
→ mixed energy”的同对象链。单独的正性、形式满秩或代数覆盖都不是这条链。
来源为[当前作者非零节](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/nonvanishing.tex)
与[混合能量节](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/energy.tex)。

## 4. 一个具体可终止的增长尺度非零首证书

从上述非零节抽取如下自足线性代数接口。固定
\(B_0,B_1\in M_h(\mathbb Q)\)。对奇素数p，令
\(\Pi_pe_0=0,\ \Pi_pe_i=e_{p-i}\ (1\le i<p)\)。
假设对每个充分大奇素数p，一个**实际已选择**的 \(hp\times hp\)周期 determinant
\(\Delta_p\)在反证关系下经逐条目 \(p^2\)归一化后全部p-整，
模p可由可逆行/列变换归约为
\[
M_p=I_p\otimes B_0+\Pi_p\otimes B_1.                   \tag{R3}
\]
这个假设包含完整有限头、实际过滤和全部边界，不能用 ambient stack的秩替代。
则
\[
\det M_p=
\det B_0\,\det(B_0+B_1)^{(p-1)/2}
          \det(B_0-B_1)^{(p-1)/2}.                    \tag{R4}
\]
证明：除 \(e_0\)外，\(i,p-i\)各配成二维交换块；
在特征非2时其两个 eigenvectors的 eigenvalues为 \(1,-1\)。
分别在这三类 invariant blocks上取 determinant即可。

若三个固定 rational determinants均非零，排除其 numerator、denominator的
固定坏素数，并保持R3已证明的归约范围后，每个充分大p的 R4都是 unit。因此
\[
v_p(\Delta_p)=-2hp,\qquad \Delta_p\ne0                 \tag{R5}
\]
对所有充分大p成立。这是无界尺度证明，而非把固定几个p的非零头外推。
Catalan原稿正是在 \(h=48,N=p\)上构造该桥，并用三个固定矩阵的有限证书支付
R4非零。本文的 R3–R5是条件接口，不声称新 logistic源已经满足R3。

故新主线第一关可限定为：能否从**完整所选矩阵**的 prime edge取得R3，
或一个同样有限且所有增长尺度有效的替代分块？如果 residue仍含随p变化的
未控 harmonic/Fermat参数，就必须证明相应单位条件；不能只复用Catalan的三个常数。
无论R5成功与否，全部 primitive Gauss内容及非prime尺度费用仍是独立关。

## 5. 第239轮后应换对象，而不是调旧预算

本轮FULL复读冻结239预算稿：对同一三维 truncated源、同actual flag和
已经支付 Hilbert–Samuel/uniform heights的固定共同BC metric，
rank-one校准给 strict矛盾的必要式
\[
\kappa<3\lambda_*,\qquad
\lambda_*\le\log C_\dagger,\quad
C_\dagger=\pi^3/2^{7/4}<10.
\]
目前已证 \(\kappa_{\rm safe}=21/2-\log12>8\)，而
\(3\log C_\dagger<15/2\)。现有 upper不能支付这种证书。
这没有证明最优 actual费用的 lower，也没有排除新的 species metric、
degree-dependent源、有限处解析图或不同 whole-functional对象。

236的 cellular低维例还给一个实际 warning：完整积分中快速模式的增长率，
在消去 \(\zeta_2\)通道后未必保留。投影形式本身是资产；沿用原 energy而
不重做真实 determinant比较则不是资产。
固定 \(M_{0,10}\)原配置的十一通道已支付，六通道仍须全部n的
relative-boundary reduction。239的 D3三禁通道证书是具体后备首关，
238的换形反例没有否定原 \(\omega\)，但也没有为原 \(\omega\)填上证书。
因此 cellular保留条件后备，不因 formal rank或论文possible
“\(\zeta_5,\zeta_7\)至少一个无理”而自动恢复主线。
项目采用的 \(\zeta_5\)baseline使后一出口不能算新的目标。

## 6. 新primary限定补充：混合偶值不是K5

本轮按Root请求有限新增读取 Li Lai的[arXiv2610.06838v1](https://arxiv.org/html/2610.06838v1)
（Oct5）：abstract、完整§1、§2定义/partial-fraction身份及§6尾部。
其 Theorem1.6声明 \(1,\zeta(3),\zeta(4)\)在 \(\mathbb Q\)上线性无关。
指定 double-pole rational核配合一、二阶导数，将反证关系
\(a\zeta_3+b\zeta_4=c\)变成整个 rational functional；
局部 matrix rank/整除给作者的费用 lower，contour/Heine及 sech正交给严格 upper。
本文未读§3–5全证明，未独立认证其全部 arithmetic与nonzero。
该声明不覆盖 \(3\zeta_3+\zeta_5\)，也不推出 \(1,\zeta_3,\zeta_5\)线性无关。
它支持 mixed whole-functional与联合整模型这种不同机制的可行性，
不能支付当前K5的 primitive内容或 prime-edge非零。

## 7. 资源选择与真实目标

本轮实际FULL读Root新
[logistic全泛函稿](global_logistic_whole_functional_bridge_round240_20261008.md)，
独立纸核其简单极点投影、固定阶分部积分、完整商部以及无穷远 anti-triangle：
\[
U_c(f)=a(f)\sum c_k\zeta(k)+b_c(f),\qquad
|W_c|\le C_c\rho,\qquad
a_e=0\ (e\le n-3),\quad a_{n-2}=-1.
\]
最后两式给目标系数块 rank至少 \(n-1\)。固定c的 \(C_c^{3n}\)只付
\(O_c(n)\)费用，故同一 absolute Heine envelope的 leading upper可转移。
完整安全条目 LCD也包括多项式商部和 Bernoulli头。
这里没有FULL读Tang整个依赖或 FstarInput全部数值证书；
作者源的归一化 \(-6n^2\)upper仍只作条件转移，不冒认为本轮独立完整核证。
另已实际FULL读B最终
[直接holonomy比较稿](global_direct_holonomy_review_round240_20261008.md)。
它的低权备用 \(2G-\tfrac\pi2\log2\)支付native补点与安全LCM；
当前两张显式图仍不满足该safe类型的必要导数门槛。这个备用不优先于上述
whole-functional准入，也不能将native补点免费扩到所有transported叶。

这个方向值得唯一有界新试验：它改变了旧三维BC的源，也改变了228的
rank-one positive-Gram目标 channel。上述 rank/upper输入仍不支付
primitive integer内容或实际 determinant无限非零。推荐先选
\[
X=3\zeta(3)+\zeta(5)
\]
的完整矩阵，争取R3类 prime-edge证书与同对象全系数 Gauss费用；
在这关前不扩到 \(\zeta_7\)或更多权重。
若首个有界检验取 \(n=p-1\)，必须重付该实际尺寸的商部、有限头与边界；
Catalan的 \(N=p\)分块范式并不自动成为这个子族的证书。
两个常数分别无理并不推出这个组合无理：例如
\(\alpha\notin\mathbb Q,\ \beta=1-3\alpha\notin\mathbb Q\)，
仍有 \(3\alpha+\beta=1\)。故采用现有 \(\zeta_3,\zeta_5\)baseline不会消灭该目标；
限定搜索未见已有 exact-combination结果也不是全球新颖性证明。

成功标准须是全部n或一个已证明无界的增长子族上的实际投影、完整费用和
nonzero，以及同一 determinant的严格实处余量。失败标准是在有界首关只得到
有限样本、形式 rank或新的安全 entry LCD；此时记录具体未付环节并停止扩权。
M₀,₁₀不默认升级，原 truncated源也不因切换候选而恢复旧参数优化。
新窗口由Root正式报告与policy安排，本文不重置正式复盘周期。
Tang原repo和其它Li2 preprint由Root负责核心读取，本文未重复审阅或声称
Lean核认证。本轮没有新数值定理。

精确读域见[本轮scope](../literature/global_review_sources_round240_20261008/alternative_reading_scope.md)。
只新增本稿和来源副本；数学程序、producer重跑、参数扫描、Lean执行均0。
保存后作者实际FULL复读；这不冒充独立审核。
