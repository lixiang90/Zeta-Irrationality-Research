# 高偶数 beta 周期投影稿的正式独立审阅

2026-10-07。审阅者：解析分工。结论：PASS，限于正文实际已证的周期等式、递推和充分消元条件；没有新数值无理性结论。

## V1. 最终输入与实际全文读取

唯一被审主稿：

E:/kimi-build/zeta5/research/catalan_higher_even_beta_period_projection_20261007.md

最终 SHA256：2a05a15737d8bedee8a99de83cef55b9a2e60f6ac5942173e5a6b7611f6113dc；14515 bytes。已实际全文读取全部八节及 B1–B22。初稿589b也全文读过；本审阅要求作者在 B20 明确限制 0≤j<L，作者已补正，最终版再次全文读取。原contact只能在这个范围推出系数相等；这项必要范围修订已闭合。

本轮重新全文读取本地 Catalan foundations.tex；本独审不继承任何前轮 producer、PDF 或 prime 审计。其余五个 Catalan 章节也在本人本轮解析任务中实际全文读取，但本审稿的周期证明只需 foundations 与下列独立推导。

实际新增读取域是已有 Lai–Zhou PDF11–14 共4页，另读取 Zudilin2019 和 Ablinger等2014 的原始 arXiv 摘要页。没有下载 PDF，没有执行原数学源码、Lean、证书、素数表或任何 producer。

## V2. C_s 的真实比较

F_1(x)=arcsin(x)/√(1−x²) 的 x^{2k+1} 系数为 1/((2k+1)c_k)；例如首项和递推均与原 m_v 一致。对 s−1 次 Euler 积分，非负被积函数允许 Tonelli，得

\[
C_s=\frac2{(s-2)!}\int_0^1
\frac{\arcsin x}{x\sqrt{1-x^2}}(-\log x)^{s-2}dx.
\]

按 x=2w/(1+w²) 变换，arcsin x=2arctan w、dx/(x√(1−x²))=dw/w，故 B7 的全部系数和 −log2 项正确。

B8 的 beta Mellin 积分分部积分端点项消失：w→0 时 arctan w·log^{s-1}w→0，w→1 时 log^{s-1}w→0。0<w<1 上

\[
0<-\log(2w/(1+w^2))<-\log w.
\]

因此 s=2 等式成立，所有整数 s>2 严格 C_s<4beta(s)。这是实际正积分比较，独立于任何未知的周期关系。它既不声称 C_s 与 beta(s) 无有理关系，也不证明它们线性无关。

## V3. beta(4) 展开与已评价低权重周期

记 L=−log w、B=log(1+w²)、c=log2，B7在s=4为2∫arctan(w)(L+B−c)²dw/w。展开六项后，∫L²=2beta(4)、∫L=beta(3)、∫1=G，恰给 B10：

\[
4\beta(4)-4c\beta(3)+2c^2G+4J_{31}-4cJ_{10}+2J_{20}.
\]

所以没有遗漏 factorial 2 或混合项。beta(3)=π³/32 是经典奇数 beta 评价，本稿没有把这个已知超越值当成新的独立性证明。

B16 的 T_3 也独立核对：T_2 生成式为2(arcsin x)²，一次Euler积分得4∫_0^{π/2}θ²cotθdθ。分部积分后是−8∫θlog(sinθ)dθ。先使用 Abel 系数 r^k 的 Fourier 展开再取 L¹ 极限；∫θcos(2kθ)dθ=((-1)^k−1)/(4k²)，最终为 π²log2−7ζ(3)/2。相应 K_4^−(1)=T_3/4−π²/4+2、K_4^+(1)=T_4/8 正确。未采用未经证明的 T_4 单周期评价。

## V4. 全 boundary 与最高两核

由原 (v+1)m_v=v m_{v-2}：

\[
d m_{d+u}-(d-1)m_{d+u-2}
=(u+1)(m_{d+u-2}-m_{d+u}),
\]

直接给 B11，右端次序确为 lowerweight minus(d−2)−minus(d)。plus系列移两位后 u=0 的边界付款给 +2/(d−1)^{s-1}，从而 B12 的符号和指数均正确。

K_s^+(1) 用 (2k+1)c_k=(2k+2)c_{k+1} 转为 2^{1−s}T_s；minus(1) 为 lowerweight plus(1)−minus(1)，恰是 B13。s≥3 时拆开的低阶系列分别收敛；s=2 必须用原件的 telescoping，不能制造 s=1 的单独发散周期。

因此全数组属于 B14 的有限生成空间。模低权重后，minus的偶数递推从 C_s 传播 c_{d/2}，minus奇数起始属低权重；plus的奇数从2^{1−s}T_s传播c_{(d−1)/2}，plus偶数在d=2处系数为零。再作diagonal reduction，得到 B15 的两侧支撑和两个kernel的精确归一化。这是完整边界证明，不只核对对角。

## V5. Z_s 部分分式、contact 范围与非零辅助标量

令 n=j+u+1、d=i−j。恒等式

\[
\frac1{(n+d)n^{s-1}}=
\frac{(-1)^{s-1}}{d^{s-1}(n+d)}
+\sum_{a=1}^{s-1}\frac{(-1)^{s-1-a}}{d^{s-a}n^a}
\]

给 B18；order1 两尾相消后的系数为
(-1)^{s-2}(H_i^{(1)}−H_j^{(1)})/d^{s-1}。d<0 时 n+d≥1，合并仍合法。i=j 时完整 diagonal 为 ζ(s)−H_i^{(s)}，B17 的负有限尾正确；B19 的三个符号亦正确。

最终稿已显式限制 j<L。此时原 contact 仅把 T_s-kernel 收缩为 D_j，而 diagonal Z 的最高项为 ζ(s)D_j，故 B20 的残留标量正是 2^{1−s}T_s−3ζ(s)/2。

对于 s=4，用中央二项式最大项估计 c_k≥1/(2k+1)，有 T_4≤2ζ(3)+ζ(4)。递减积分比较给 ζ(3)<3/2、ζ(4)<4/3，故 T_4<13/3，T_4/8<13/24<3/2<3ζ(4)/2。因此 B21 严格为负。这个标量非零与某些列可能 D_j=0 的情况已经区别；没有据形式符号数量推断未知周期的有理独立性。

## V6. 有理投影与解析/整模型的范围

对实际有限period coefficient arrays强制 nuisance符号的所有系数为零，是无需未知period独立性的充分条件。得到一个有理核，不自动保证目标map非零或足够rank；清分母不是unimodular变换，必须支付index/height。正文明确保留这些条件。

B22 的直接beta Mellin carrier确实是Q+Qbeta(s)，符号由把级数索引向后移d位得到。正文没有把它当作原sqrt混合核，也没有从一个标量moment的识别推导全部mixed matrix的单目标投影。

外权重 artanh(|t|)^{s-2}/(s−1)! 的beta起始校准也正确：配对±t后的integrand为2artanh(t)^{s-1}/((s−1)!f)，再置u=√((1−t)/(1+t))得到4beta(s)。它改变全部outer moments与整数模型，不能用它证明B3内权重已经单目标。

固定正密度能否保原energy是另一个具体解析问题。本文§7的未闭合说明不能理解为全方法不可能的定理；也没有被审稿宣称新的投影可以免费保留原实费用。原p² layer、两discrepancy、48seed仅已在原数组证明；正文没有将它们移植成新证明。

## V7. 原始文献的真实核对

Lai–Zhou已有PDF11–14已实际提取并阅读。PDF12的Theorem6.1为beta(2),beta(4),beta(6),beta(8),beta(10)中至少一个无理；PDF13–14的normalization、lcm、prime-saving与特定hypergeometric输入绑定。它没有单独给beta(4)，不能把该成本用于本稿新moment数组。本文所述历史结论的范围正确。

Zudilin2019原始[摘要](https://arxiv.org/abs/1804.09922v2)确认六个beta值中至少一个无理。本人未读其期刊全文，故只核此摘要支持的结论，不继承作者更广的读取域。Ablinger等2014原始[摘要](https://arxiv.org/abs/1407.1822)确实将binomial/inverse-binomial Mellin sums与sqrt字母的iterated integrals相联；这只是背景，本稿具体B7/B10仍由前述纸面计算证明。

没有根据旧论文的Catalan open句子判断2026现状，也没有声称已搜索尽全部最新beta(4)文献。

## V8. 最终结论与执行范围

最终2a05主稿数学PASS。必要B20列范围修订已由作者完成并全文回读；本独审最终输入已再次实际全文读取。其结果是准确识别错误简单推广、给出实际周期桥和完整递推，不是beta(4)无理性证明。

本审阅实际scope：主稿全部八节B1–B22；本地foundations全文；Lai PDF11–14共4 distinct页；两原始arXiv摘要。没有复算原有mod101 pivots、Catalan能量certificate或任何新矩阵。原/同行数学producer创建/执行/import/rerun=0，prime/Lean=0，新增PDF下载=0。旧研究和冻结文件未修改。
