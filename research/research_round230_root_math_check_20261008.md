# 第230轮 Root 数学独审（范围明确）

实际 FULL 读取并逐式检查 A 的
`q2_signed_moment_analytic_nonzero_round230_20261008.md`（6942 B，
ce674d4f64739464f46dd960bce8108b29b196969dbc4db65cf2c0e3eca32a6e）。
实际 FULL 读取唯一精确 producer；仅将 primality trial bound 改为 isqrt
后执行一次，exit 0 PASS。JSON 全矩阵打印被工具截断，未称其全文人工复读；
生产器实际输出的八行 compact rank record 则完整可见。

## 1. A 解析笔记 PASS

A1 的 π/4 换权常数正确：乘 ν 后恢复冻结229的1/4双积分。
级数分母 (n+d−s+1/2)² 与 Euler 操作 (D−s)² 相抵，
共同非齐次项为 πx^(d+1/2)/(4(1−x))，并非齐次系统。
near0 的 x^j log x（j≤d）与 x^(d+1/2)·analytic 确实不能相抵；
其后正权 Q² 积分支付完整函数独立。

矩右核 A4–A5 与原2m列池严格等价；H_p 的 m 个内部零点给
跨度 R/∏(1−xy_j)，分母在[0,1]为正，所以 p 至少 m 次变号。
这与 A4 的至少 m−1 次变号并不相加，未产生次数矛盾。
log 权的内点零确实排除保留低指标块的直接全指标 AT 调用，
没有排除另证的 balanced 指标或合法变换。d0 校准 W0=−Θ 正确。
A 不以函数秩代矩秩、不以非 AT 反推矩零，边界均 PASS。
Root 未重新全文读取39页 primary；随后实际定向读取已保存选页文本中的
Definitions1.1–1.4、常号测度/相邻不交支撑要求及 Theorems1.1–1.2，
核对 A 对定理边界的表述。完整选页读取仍归 A。

## 2. Root 条件非零引理及精确生产器 PASS

对 g∈Z_(p)，将 W_d(g) 的下部 m 行各乘 p，得到
p^m W_d(g)=det[B; pgA+paᵀ]。A、B 的 p 整性使 pgA 模 p 消失。
残差栈的非零因此给精确 v_p W_d(g)=−m，而非仅下界。
在 Θ∈Q 的假设下，分母只排除有限素数；所需无界 d,p 子族仍未证。
这一步没有使用 E 的模 p 可逆性或未经饱和的整数核基。

producer 的 Fraction 递推和独立 α/ρ 有限和对 l=0,…,25 相等校验；
模 p 取数之前断言分母 p-unit，消元对矩阵副本做有限域合法行操作。
八案例是文件中预选固定列表，未执行参数扫描，未从样本推无限。

## 3. 完整残差纸式的独立校准

令 k=(p−1)/2，η=2(−1)^k。Wilson/binomial 同余及 Fermat 给
p m_(2k)=η；偶矩递推给 p m_(2(k+b))=η c_b。
有限头项的最大偶矩指数为2(r+d−1)，故支持从 r=h=k+1−d 开始。

在最小案例 d1,p5 中，h2、η2。B/C 提出的完整卷积式
pa_(h+u,s)=−ηΣ_(t=0)^u c_t/[2(d−s−u+t)−1]²
给 active 两行 (3,3)、(2,1)，与实际 JSON 可见的两列一致。
这项手工校准没有新增程序执行；全尺度式的完整证明由 B/C 新稿承担。

## 4. 初始 Hankel 的独立 Fourier 校准

令 x=(1+cosθ)/2，ν=dθ/π。2log(4x) 的 Fourier 展开为
4Σ_(n≥1)(−1)^(n−1)cos(nθ)/n（积分意义足够）。
对 T_j(2x−1) 的矩，B00=0、B0j=2(−1)^(j−1)/j；
i≠j>0 时 Bij=(−1)^(i+j−1)(1/(i+j)+1/|i−j|)，
Bii=−1/(2i)。这些系数由 cos product 与正交直接得到，C 已独立确认。
d2 的原 Hankel 行列式可手算为−23/1536；所以未声称普通 Selberg 乘积式。
模 p 分母为 unit 仍不支付其行列式分子为 unit。

数学执行累计1，失败0；文档读取出现一次错误路径（随后按 rg inventory
定位正确文件），不计作数学执行。没有 Git 操作、Lean 构建或数值 LI 声明。

## 5. C 最终数学稿 FULL 独审 PASS

实际 FULL 读取 `q2_residue_saturation_interface_round230_20261008.md`
5391 B / cd9003d7c29d1154543ed3e241464a6bb12c3076675723e58c999423aa32b35f。
R1 全有限头合并与先前独立推导相符；R2 明确同步变换 B 的 active 列，
没有以平方 Cauchy 自身秩偷换完整栈秩。
R3 的 monic Chebyshev 缩放乘积平方为2^(−2d²)，符号为(−1)^m。
boundary η2，pa 块的(−2)^m再乘反序后的4^(−m)，故 R4 整体因子
确为2^(−m−2d²)。普通 Cauchy 行列式为unit；Borchardt恒等式归纳正确，
但 perH 为unit并未证明，稿中保留此缺口。

饱和变换的行列式估值为−e，所以原 W 的估值须加 e。
D=pC_g 的秩 r 枢轴消元后，剩余 m−r 行各含 p；故
v_p detC_g=−m+(m−r)+v_pdetS1=−r+v_pdetS1。
R5 的 e−r 项与目标 gA 的保留均正确。这是一条条件恒等式，
没有断言 Schur 残块已满秩或另一层非零。全尺度/strict边界 PASS。

## 6. B 最终完整卷积稿 FULL 独审 PASS

实际 FULL 读取 `q2_complete_residue_convolution_round230_20261008.md`
6290 B / b7d07a53e494c9f6c031e7fb28fd52d3f9316ee6cc878d97c90aaf78497dbd46。
R1把奇v有限头完整换为 v=0,…,d−s−1，与冻结对象一致。
R5–R6生成函数比较正确，1≤q≤k保证所取系数的分母都是p-unit。
两段指标分别0≤t≤b和max(0,b+1)≤t≤u，恰合为0≤t≤u，
所以 R7–R8 并非删头后的局部替代。

R9从下部映射的核限制给准确秩加法；右变换(Tᵀ)^−1方向正确，
必须同时作用于上 B 的 active 列。q<m 时第一残差层确有缺陷，
而本轮主窗口 q≥m 仍须付 kernel restriction 的秩，不从缺陷反推 W 零。
R10的标量(−η)^m与C的进一步R4身份相容。d1,p5手算det3正确。
B的全增长窗口公式与C的较窄窗口独立证明一致；均未付无界nondivisibility。
