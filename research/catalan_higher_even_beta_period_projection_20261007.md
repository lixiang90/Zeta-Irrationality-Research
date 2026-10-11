# Catalan 对数加权 moment 与高偶数 beta 的真实周期投影

2026-10-07。新研究任务；原审计稿与冻结旧研究文件均不修改。本文只作纸面推导；没有创建、运行、导入或重跑数学 producer，没有素数表、Lean 或行列式数值拟合。外部 `E:/codex-build/math` 只读。本轮实际完整读取 Catalan `build/sections/foundations.tex` 全434行；文献范围见末节。

核心结论：在 Catalan 的原混合核中，仅给内变量增加 `(-log y)^(s-2)/(s-2)!`，对角主周期是逆中心二项式常数 C_s，而非 4 beta(s)。对所有整数 s>2，有严格不等式 0<C_s<4 beta(s)。s=4 时可精确展示混合对数周期，原 Taylor contact 也留下一个非零的最高权重辅助系数。本文给出完整有限周期递推和整数投影的充分条件；没有证明这些新周期的算术独立性，也没有证明 beta(4) 无理。

## 1. 原对象与新权重

为避免把目标整数 s 与积分变量混用，内变量记 y。原论文取 f(t)=sqrt(1-t²)，w=t/(1+f)，星 involution 为 w↦w^(-1)，固定 t、反转 f。行

\[
 R_r=(1-t)^h t^{C-1}w^{r-g},\qquad
 P_r=(R_r+R_r^*)/2,\qquad D_r=t(R_r^*-R_r)/(2f)
 \tag{B1}
\]

其中 P_r、D_r 是整数 Chebyshev 多项式，且

\[
 tP_r/f-D_r=O(t^L).\tag{B2}
\]

本文保持这条等式的原含义。令 s≥2 为整数，定义用户提出的加权 moment

\[
 M_s(i,j)=\int_{-1}^1\int_0^1
 \frac{|t|}{f(t)}\frac{t^i y^j}{1-ty}
 \frac{(-\log y)^{s-2}}{(s-2)!}\,dy\,dt,
\]
\[
 Z_s(i,j)=\int_0^1\int_0^1
 \frac{t^i y^j}{1-ty}
 \frac{(-\log y)^{s-2}}{(s-2)!}\,dy\,dt.\tag{B3}
\]

其中 i,j 为非负整数，M_2、Z_2 正是原文对象。权重非负。对几何级数绝对值取和后，可以逐项积分；所得非零项为 O(u^(-s+1/2))，故 s≥2 收敛。亦可在两个变量中分区直接用原积分的端点对数支配。固定多项式因子保持绝对收敛。

记

\[
 c_k=4^{-k}\binom{2k}{k},\qquad
 m_v=\int_{-1}^1 t^v\frac{|t|}{f(t)}dt
 =\begin{cases}2/((v+1)c_{v/2}),&v\text{偶},\\0,&v\text{奇}.\end{cases}
\]

Gamma 积分给精确级数与 diagonal shift

\[
 M_s(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{(j+u+1)^{s-1}},\qquad
 Z_s(i,j)=\sum_{u\ge0}\frac1{(i+u+1)(j+u+1)^{s-1}},
\]
\[
 M_s(i,j)-M_s(i+1,j+1)=\frac{m_i}{(j+1)^{s-1}}.\tag{B4}
\]

## 2. 对角实际产生什么：全 s 的精确比较

设

\[
 C_s=M_s(0,0)=2\sum_{k\ge0}\frac1{(2k+1)^s c_k}.\tag{B5}
\]

由 B4，任意对角都是同一周期加有限有理尾：

\[
 M_s(i,i)=C_s-\sum_{v=0}^{i-1}\frac{m_v}{(v+1)^{s-1}}.
 \tag{B6}
\]

这里的 1/c_k 是真实半整数 Beta moment 的倒中心二项式因子；不是 Dirichlet character (-1)^k。

为了精确比较 C_s 与 beta(s)，定义

\[
 F_a(x)=\sum_{k\ge0}\frac{x^{2k+1}}{(2k+1)^a c_k}\quad(0\le x<1).
\]

标准 arcsin 幂级数与一次求导，或其一阶微分方程，给

\[
 F_1(x)=\frac{\arcsin x}{\sqrt{1-x^2}},\qquad
 F_a(x)=\int_0^x F_{a-1}(z)\frac{dz}{z}\quad(a\ge2).
\]

迭代后，所有被积函数非负，Tonelli 与端点收敛给

\[
 C_s=\frac2{(s-2)!}\int_0^1
 \frac{\arcsin x}{x\sqrt{1-x^2}}(-\log x)^{s-2}dx.
\]

置 x=2w/(1+w²)，0≤w≤1，arcsin x=2 arctan w，且
dx/(x sqrt(1-x²))=dw/w。于是得到关键精确等式

\[
 C_s=\frac4{(s-2)!}\int_0^1\frac{\arctan w}{w}
 \left[-\log w+\log(1+w^2)-\log2\right]^{s-2}dw.
 \tag{B7}
\]

另一方面，Dirichlet beta 的 Mellin 积分及一次分部积分给

\[
 \beta(s)=\frac1{(s-1)!}\int_0^1
 \frac{(-\log w)^{s-1}}{1+w^2}dw
 =\frac1{(s-2)!}\int_0^1\frac{\arctan w}{w}(-\log w)^{s-2}dw.
 \tag{B8}
\]

第一式由交错几何级数或 Abel 参数取极限证明；边界项在 w=0、1 均为零。对 0<w<1，

\[
 0< -\log\frac{2w}{1+w^2} < -\log w.
\]

因此 B7–B8 严格推出

\[
 C_2=4\beta(2)=4G,\qquad
 0<C_s<4\beta(s)\quad(s>2).\tag{B9}
\]

这排除了“原主周期不变，只把 beta(2) 换成 beta(s)”这一具体推广。B9 没有排除 C_s 与 beta(s) 之间可能存在别的未证明算术关系，也不是独立性定理。

## 3. beta(4) 的明确混合周期

记 L(w)=-log w、J_{10}=∫ arctan(w) log(1+w²)dw/w，

\[
 J_{31}=\int_0^1\frac{\arctan w}{w}L(w)\log(1+w^2)dw,
 \qquad
 J_{20}=\int_0^1\frac{\arctan w}{w}\log^2(1+w^2)dw.
\]

以上记号只是积分标签，不声称按下标具有标准多重 zeta 编号。展开 B7 的平方，得到

\[
 \boxed{C_4=4\beta(4)-4\log2\,\beta(3)+2\log^22\,G
 +4J_{31}-4\log2\,J_{10}+2J_{20}.}\tag{B10}
\]

其中 beta(3)=π³/32。因此明确出现 π³log2、Glog²2 和混合 arctan/log 积分。它们可写成字母 0,i,-i 的迭代积分及 log2 的乘积，但本文没有把这些实际周期假定为线性独立，也没有声称 B10 已是最小周期基。平方的逐点比较证明 B10 中的总修正严格为负，故不是简单的消失项。

同样 C_3=4beta(3)+4J_{10}-4log2 G。一般 B7 的二项展开在所有高权重引入混合 log(1+w²) 插入项；这正是以 log y 权重增加 order 时必须面对的新周期。

## 4. 完整 moment 数组的有限周期递推

定义 K_s^-(d)=M_s(d,0)、K_s^+(d)=M_s(0,d)，以及

\[
 T_s=\sum_{k\ge1}\frac1{k^s c_k}\qquad(s\ge2).
\]

对 s≥3、d≥2，利用 (v+1)m_v=v m_{v-2} 并逐项相减可得

\[
 dK_s^-(d)=(d-1)K_s^-(d-2)
 +K_{s-1}^-(d-2)-K_{s-1}^-(d),\tag{B11}
\]
\[
 (d-1)K_s^+(d)=(d-2)K_s^+(d-2)
 +K_{s-1}^+(d)-K_{s-1}^+(d-2)
 +\frac2{(d-1)^{s-1}}.\tag{B12}
\]

B11 的被减项是
[d m_{d+u}-(d-1)m_{d+u-2}]/(u+1)^(s-1)
=(m_{d+u-2}-m_{d+u})/(u+1)^(s-2)。B12 先把第一个级数移两位，再保留 u=0 的边界项；它恰好产生显示的 2/(d-1)^(s-1)。因 s≥3，拆开的两个低权重级数均收敛。s=2 使用原文的两个 rational boundary recurrence，不能把各自发散的 s=1 级数拆开。

起点完全由三类周期给出：

\[
 K_s^-(0)=K_s^+(0)=C_s,\qquad
 K_s^+(1)=2^{1-s}T_s,\qquad
 K_2^-(1)=2,\qquad
 K_s^-(1)=2^{2-s}T_{s-1}-K_{s-1}^-(1)\ (s\ge3).
 \tag{B13}
\]

第二式用 (2k+1)c_k=(2k+2)c_{k+1}。最后一式用
1/(v^q(v+1))=1/v^q-1/(v^(q-1)(v+1))；两个级数在 q≥2 时分别收敛。

故 B4、B11–B13 给全 i,j 的无歧义有限递推，并证明

\[
 M_s(i,j)\in\operatorname{Span}_{\mathbf Q}
 \{1,C_2,\ldots,C_s,T_2,\ldots,T_s\}.\tag{B14}
\]

更精确地，模低权重空间 V_{s-1}=Span_Q{1,C_2,…,C_{s-1},T_2,…,T_{s-1}}，齐次传播给

\[
 M_s(i,j)=C_s c_{(i-j)/2}
 +2^{1-s}T_s c_{(j-i-1)/2}+E_s(i,j),\qquad
 E_s(i,j)\in V_{s-1}.\tag{B15}
\]

如原文，c_z 在 z 非非负整数时为零。对于 i<j 的偶数 boundary，d=2 时齐次系数为0，所以不会从 K_s^+(0) 传播 C_s；正是 B15 的单边支撑。对于奇数 plus boundary，齐次系数为 c_{(d-1)/2}。这些事实支付了差分两侧的所有分支。

权重4的一个已完全评价的起点是

\[
 T_2=\frac{\pi^2}{2},\qquad
 T_3=\pi^2\log2-\frac72\zeta(3),\qquad
 K_4^-(1)=\frac14T_3-\frac{\pi^2}{4}+2,
 \quad K_4^+(1)=\frac18T_4.\tag{B16}
\]

T_2 的 arcsin² 生成式为 Σ x^(2k)/(k²c_k)=2(arcsin x)²。一次 Euler 积分给
T_3=4∫_0^(π/2)θ²cotθ dθ=-8∫θ log(sinθ)dθ。
用 Abel 正则化的 log(sinθ)=-log2-Σ cos(2kθ)/k，积分 θcos(2kθ)=[(-1)^k-1]/(4k²)，便得到 B16。Abel 级数先在参数小于1时逐项积分，随后靠 log-sine 的可积支配或 L¹收敛取极限。本文没有无来源地把 T_4 化为单个 ζ(4)。

## 5. Z_s 的全部残数与原 contact 的实际残留

令 H_j^(a)=Σ_(k=1)^j k^(-a)。i=j 时

\[
 Z_s(i,i)=\zeta(s)-H_i^{(s)}.\tag{B17}
\]

i≠j，设 d=i-j。对 n=j+u+1 作精确部分分式并合并两个 harmonic order1 尾，得到

\[
 Z_s(i,j)=\sum_{a=2}^{s-1}
 \frac{(-1)^{s-1-a}}{d^{s-a}}(\zeta(a)-H_j^{(a)})
 +\frac{(-1)^{s-2}}{d^{s-1}}(H_i^{(1)}-H_j^{(1)}).
 \tag{B18}
\]

空和为零，故 s=2 也正确；d<0 时原 n+d 始终为正，合并 harmonic tail 同样合法。特别

\[
 Z_4(i,j)=\frac{\zeta(3)-H_j^{(3)}}d
 -\frac{\zeta(2)-H_j^{(2)}}{d^2}
 +\frac{H_i^{(1)}-H_j^{(1)}}{d^3}\quad(i\ne j).\tag{B19}
\]

若对原整数 P,D 保持 B2，列索引满足 0≤j<L（尤其包括原 raw 列 b≤j<L），并仍定义 F_{s,j}=M_s(P,j)-(3/2)Z_s(D,j)，B15–B18 给精确结构

\[
 F_{s,j}=C_s\sum_i P_i c_{(i-j)/2}
 +\left(2^{1-s}T_s-\frac32\zeta(s)\right)D_j
 +E_{s,j},\tag{B20}
\]

其中 E_{s,j}∈Span_Q{1,C_2,…,C_{s-1},T_2,…,T_{s-1},ζ(2),…,ζ(s-1)}。
原因是 B2 仅在 j<L 时告诉 Σ_i P_i c_{(j-i-1)/2}=D_j；它并不证明 2^(1-s)T_s=(3/2)ζ(s)。s=2 该恒等式成立，恰给原文的 ζ(2) 消去；s=4 不成立。

这后一断言可不用任何数值拟合严格核实。中央二项式是二项式行的最大项，故 c_k≥1/(2k+1)，从而

\[
 0<T_4\le2\zeta(3)+\zeta(4)\le\frac{13}{3}.
\]

因此 T_4/8≤13/24<3/2<(3/2)ζ(4)，即

\[
 T_4/8-(3/2)\zeta(4)<0.\tag{B21}
\]

原列接触条件确留下一个非零最高权重辅助系数；除非该列 D_j=0，不能仅凭 contact 把它消掉。B20 是实际等式；本文不从“形式上有多个符号”推出这些周期的 Q 独立性，也不排除其他额外构造可能把其总和消掉。

## 6. 整数行列投影能做到的事及必须另外证明的事

B4、B11–B18 的所有 coefficient arrays 都是有理数。因此在任意有限的行/列/degree 集合上，可以先以自由形式符号 C_a,T_a,ζ(a) 记录实际恒等式，再构造明确的有限有理矩阵，对每个不需要的符号逐列强制其系数为零。解这个有理线性系统后清公共分母，得到整数行组合或整数列组合。这是一个严格的充分消元条件，不要求未知周期线性独立。

它仍需支付三件事：存在非零解；目标 C_s 的系数没有同时被杀；有足够多这样的解形成非退化原矩阵。形式 dimension count 只保证整个核非零时，不能保证目标 map 在该核上的 rank。清分母后得到的整数投影不是 unimodular 变换，其指数/高度要重新计入全部有限处成本。

即使上述投影成功，B14 中直接剩下的目标也是 C_s；把它换成 beta(s) 还必须在 B7/B10 的混合 log 插入项上增加真正周期比较或相对链投影。B10 包含 log2 系数与周期乘积，不能把它们当作有理 row coefficients。原 P,D 的 Chebyshev 整系数及完整 contact 本身没有提供这个比较。

一个确实单目标、但改变原 carrier 的最小对照是

\[
 \mathcal B_s(d)=\frac1{(s-1)!}\int_0^1
 \frac{x^{2d}(-\log x)^{s-1}}{1+x^2}dx
 =(-1)^d\left[\beta(s)-\sum_{k=0}^{d-1}\frac{(-1)^k}{(2k+1)^s}\right].
 \tag{B22}
\]

故任意整数 even polynomial 的此类积分严格属于 Q+Q beta(s)，并没有 inverse-binomial 辅助周期。这是基本 Mellin/有限尾等式，不是新的无理性结果；root 的独立研究正在针对更完整的有理双变量核与合流 Cauchy 投影支付额外条件，本文不重复其构造或预算。

另一个仅用于校验主周期的外权重改动是：在原 M_2(0,0) 的 outer measure 乘 artanh(|t|)^(s-2)/(s-1)!。正负半轴合并给 2∫artanh(t)^(s-1)dt/f(t)/(s-1)!，置 x=sqrt((1-t)/(1+t)) 即得 4beta(s)。它也改变了所有 outer moments 和 p-adic model；不是在 B3 下实现的整数多项式投影。

## 7. 现在的算术、解析与非零障碍

对于 B3，假设 beta(s) 有理并不使原 F_{s,j} 或原 filtered determinant 有理，因为 B20 中 C_s、T_s 和低权重周期仍在。因而暂不能启动原 Catalan 的有理 product formula 矛盾。即使改投影只保留 C_s，也是在研究不同常数的无理性。

完整 p 模型必须重建。B4 的分母指数从1变成 s-1，B11–B12 又跨权重耦合；原 p² 层、2-adic 两个齐次 discrepancy、固定48种子的 Frobenius 分解都不是自动保留。新的算术需要逐 entry 原格、所有 full minors、清分母指数和固定 source/target 的输入分母。不能仅把原最终费用按 s/2 缩放或按列数猜测。

解析端也要重新估计。s 固定时 log y 在端点的增长是可积的，但行列式的交替展开和可能的新投影高度决定真正 n² 预算；仅把积分绝对值乘一个常数不证明原 determinant 的同样 exponential gain。B22 的直接 beta carrier 避开了周期污染，却仍需共同分母增长、非零尺度以及足够强的 archimedean shrinkage。

由此本轮得到的是一个明确的分流标准：沿原 sqrt measure 增加 log y 权重，必须处理 B10/B20 的新周期；沿直接 rational beta Mellin carrier，则周期投影简单，但须重新支付整模型和行列式增益。没有证明所有高偶数 beta 不可能用 Catalan 方法，也没有宣称某个一般 no-go。

## 8. 原始文献与实际读取范围

本轮实际全文读取本地 Catalan `foundations.tex`434行，核对 B1–B4 的原行、原 measure、m_v、boundary recurrence、contact 和 integer filter 定义。本轮没有执行原仓库 scripts、Lean 或 Comparator。

已去重并复用 `literature/lai2021_at_least_two.pdf`（14页，SHA256 `33c0d91dd1209fbf767be9c94c09c305124be3a1d6773a1341f1a01d22ad0369`）；实际阅读 PDF11–14 共4页，其中 PDF12–14 为 §6 与 Theorem6.1。Lai–Zhou 证明 beta(2),beta(4),beta(6),beta(8),beta(10) 中至少一个无理，不指定 beta(4)。其 normalization/lcm/prime saving 是特定 hypergeometric 输入的已证费用，不能用于本文新数组。[Lai–Zhou 原文 §6](https://arxiv.org/html/2103.00904v2#S6)。

已读取 Zudilin2019 原始 arXiv 摘要页及期刊 theorem 段落，确认六个 beta 值中至少一个无理的历史结果；未把旧文的 Catalan open 句子当成2026年结论。[Zudilin2019](https://arxiv.org/abs/1804.09922v2)。本文不依赖未核的搜索结果宣布 beta(4) 的最新绝对状态，而只报告所核原文定理没有单独证明该目标。

已读取 Ablinger–Blümlein–Raab–Schneider2014 原始 arXiv 摘要页：inverse-binomial Mellin sums 与 sqrt-valued alphabets、iterated integrals 相连。这提供本文 B7/B10 的文献背景，本文所有具体等式均在上述段落自行推导，不把 abstract 当作 B10 的现成定理。[原始论文页](https://arxiv.org/abs/1407.1822)。没有下载新的 PDF；没有重复归档旧 PDF，也没有继承其他作者的原件阅读页数。

本轮实质结果是 B7–B10 的精确周期桥与严格不等式、B11–B15 的全数组递推、B18–B21 的全部 zeta 残数及原 contact 的真实残留。下一步需要真正 target projection 与原格预算，而非 prime sampling 或有限数值拟合。
