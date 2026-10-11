# 第224轮进展：无限非零、共享递推与真实解析模型

2026-10-08。本轮沿第222轮全局审查所选的固定R_n构造推进，取得两项核心缺口的实际补全：**目标行列式Δ无限非零；A₃、A₅、A₇与完整C共享显式六阶递推。** 同时把三列period转成真实三频率和紧支撑实核。尚未得到ζ(7)、Catalan常数或其他指定数的无理性、线性无关性新定理。

## 1. 当前固定对象与结果边界

继续使用[222固定数学包](relation_source_architecture_global_round222_20261008.md)中的R_n以及完整交错导数和I_n；对偶n保留

`I_n=A₃,n ζ(3)+A₅,n ζ(5)+A₇,n ζ(7)+C_n`。

令r=n/2，a,b,c,q分别为四个系数列；Δ_r=det(a,b,c)、Ξ_r=det(a,b,q)、J_r=det(a,b,I)，均取r,r+1,r+2三行。完整身份是 `J=Δζ(7)+Ξ`。对固定有理g，H_g的系数gΔ+Ξ无条件定义；只有假设ζ(7)=g，才有H_g=ΣJ_r z^r。三频率模型也只变换前三列，不替代C。

[223报告](research_pade_structure_round223_20261008.md)已付全素数幂denominator、G-function存在性以及I_n的实际衰减。223没有声称Δ无限非零或实际显式算子；这两项本轮得到补全。有限Δ₀与递推存在性从未用于冒充无界非零。

## 2. 全素数尺度上的无限非零定理

[完整p-adic证明](pade_infinite_nonzero_residual_round224_20261008.md)证明：对每个p>37，且p不整除固定整数K=7763789492179875，

\[
 \frac{\Delta_{(p-1)/2}}p\equiv\frac{7763789492179875}{4}\pmod p,
 \qquad v_p(\Delta_{(p-1)/2})=1.
\]

因此Δ在无限多个不同r上非零。这个结果是原实际三列、实际连续三行的定理；不是参数家族或有限素数实验的外推。

关键是推进223第一层rank2 residual：n=p−1,p+1,p+3三行先做已付整性的缩放，再用两次exact integral shear。coarse反射z↦−1−z使degree≤2只见y=z+1/2，degree3首次出现独立y³方向。未知深层标量完整留在y方向，由重复列的det严格消去；已计算的cubic常数留下固定非零K/4。完整unit blocks、signed denominator、其余partial clusters和两个pole的error全已计入。

固定m=1,3的有理harmonic常数由一次Fraction程序核验；全p量词由纸面展开支付。[Root独审](research_round224_infinite_nonzero_review_20261008.md)和[A第二独审](research_round224_infinite_nonzero_second_review_20261008.md)分别独立FULL复核，均PASS。它不证明Ξ、J或H_g无限非零，不证明Δ非有理，不给最优full-prefix算术费用或ζ(7)无理性。

## 3. 共享六阶递推与完整边界

[中心移动telescoper](pade_centered_even_telescoper_round224_20261008.md)在Q(n,z)中显式定义中心移动j=0,…,6的九阶principal-part消去。正负两族pole及无穷远余项全付后，余项落在对称degree≤10的六维多项式空间。6×7矩阵的交错最大minor给同一个非零λ₀,…,λ₆；固定n=6的七个minor均非零。

所得递推在r=n/2变量是六阶，在普通n单步shift中是十二阶。系数由有限jets、principal parts和determinants明确给出，未完全展开成巨大多项式，也未认证最小阶。整个双边period的0、2、4阶jets支付三列共享λ；独立半直线telescoping另外支付I及完整C共享同一λ。下端在t=6由三重零消去，移动产生的所有有限head也逐项为零，尾端由有理certificate实际衰减支付。

r-companion的三次外积给明确20维差分系统；Δ、Ξ、固定有理g的H_g均为同一系统的指定coordinate，并有order≤20 scalar差分算子。**20是差分状态维数，尚不是CDT的最小微分/cyclic秩。** 原G-function生成式的θ-operator及其最小模型需要继续研究。

A固定n=6程序1次得到完整余项矩阵；Root另一次以Leibniz定义独立核七个minor和cofactor kernel，不重跑producer。[算子独审](research_round224_telescoper_review_20261008.md)PASS。有限矩阵验证与全局有理推导、完整边界各有明确责任。

## 4. 真实三频率与实核，不再只有形式period

[双边period模型](pade_bilateral_period_model_round224_20261008.md)保持完整C身份，证明经sin⁶规范化后的period恰为cos(πv)、cos(3πv)、cos(5πv)的线性组合。三频率系数B与 `(S₂/π⁴,S₄/π²,S₆)` 的变换det为1/64，并有

\[
 \Delta_r=\frac{8505\pi^6}{4}
 \det\bigl[B_{j,2r+2h}\bigr]_{h=0,1,2;\ j=1,3,5}.
\]

同时得到一般最高pole阶2m的精确m频率投影，升序规范化系数到升序奇频率的det为 `2^(−m(m−1))`。这是整个函数的自足恒等式，尚不支付有理/代数系数域下的CDT微秩；变换含π²，不能免费当作Q上的shear。[C独立审阅](research_round224_bilateral_period_review_20261008.md)PASS。

[直接Fourier模型](pade_direct_fourier_kernel_round224_20261008.md)还构造紧支撑实函数

\[
 w_r(t)=\frac{2^{2r-1}}{\pi(2r)!}\cos^{2r}(t/2)\mathbf1_{|t|\le\pi},
 \quad U_r=w_r^{*6},\quad
 K_r=\prod_{a=r+1}^{3r}(a^2+\partial_t^2)^3 U_r.
\]

采用普通未归一化卷积。U_r≥0，K_r∈C⁴、支撑在[−6π,6π]，所有所需边界derivatives为零，普通分部积分完整成立。实际B系数为 `B_{j,2r}=4π(−1)^r K_r(jπ)`，因而

\[
 \Delta_r=136080\pi^9(-1)^{r+1}
 \det[K_{r+h}(j\pi)]_{h=0,1,2;\ j=1,3,5}.
\]

[B独立审阅](research_round224_fourier_kernel_review_20261008.md)逐项核2π规范化、ordinary convolution、regularity及有限边界，PASS。U正不推出高阶微分后的K正；尚无K的total positivity、主增长模式或三值Chebyshev定理。

## 5. 接下来怎样推进，怎样避免局部最优

当前地图发生了实质改变：Δ的无限非零门已支付，无需继续提高同一prime residual的层数；实际共享递推和实核已经可供全局解析研究。下一轮的中心问题是 **原固定序列的真实主奇点/增长模式，以及ζ(7)=g关系是否给予严格解析增益**。

可以从共享递推的主符号或三个K_r(jπ)的实际渐近进入；要说明主mode是否相同、是否消去，以及如何映到Δ/Ξ/H_g的同一微分模型。不能仅因三频率或20维差分状态就指定CDT秩，也不能用一个新的安全上界与另一个安全下界冒充严格比较。若完整dominant data没有关系选择性增益，须及时转向其他source/目标而非增加参数或素数扫描。

223已经给I_n=O(n⁻⁵log(n)ρⁿ)，ρ=2⁴²/3²⁷<1；其J上界的底数 `2⁶⁰ρ²>1`，故尚无J绝对衰减。完整denominator的安全指数Δ为12，Ξ/H为26，conditional flat(0,12,26)费用166/9亦不是已过CDT门槛。还缺实际微分最小模型与秩、generic singularity和relation strict overconvergence，以及同源完整算术/解析strict comparison。

按用户每4–8轮俯瞰全局的要求：最近正式全局复盘为222，正常下一次228，窗口226–230；结构性反例/上限或连续两轮无核心接口进展会提前触发。本轮是核心进展，不重置六轮节奏。此前223的有效结构进展与本轮更强进展均保留，不把归档文件数量视作数学收益。

## 6. 执行与封存

数学程序合计 **3次**：A固定n=6余项矩阵一次；B固定m=1,3常数一次；Root保存矩阵的七minor独立Leibniz核验一次。四份数学稿、全p推导及所有同行纸核没有额外程序。没有CAS、recurrence guessing、参数/素数/order扫描、PSLQ、数值积分、Lean、旧producer重跑或Git操作。未重查仓库/cloud状态，222的身份只复用。

本轮新增PDF0。Root实际选读DLMF4.22E5及短TEX；C选读DLMF1.8、1.14、5.12用到的公式和完整条件，保存HTML3及短TEX5。完整下载HTML不登记整页FULL；Root额外FULL读这五份短TEX，仅公式范围。A官方实现页面选读仅登记于作者来源记录；Root只FULL读该记录，不冒称读其网页。所有数学关键边界在稿内有自足推导。

最终读取范围在 [Root scope](../literature/pade_nonvanishing_sources_round224_20261008/root_reading_scope.md)。独立报告审查另存 [报告收据](research_round224_report_review_20261008.md)。新[manifest](../literature/manifest_cdt_pade_nonvanishing_round224_20261008.json)将核前轮不可变pins，完整保留223 main前缀，只追加本报告；不修改冻结数学输入。goal保持active：本轮补上构造非退化与实际算子，不代表已经完成数值无理性目标。
