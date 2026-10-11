# 对数矩新轮：五份技术稿的独立审阅与量词记录

日期：2026-10-05。记录者：paper_mechanism。本稿只登记本轮实际审阅范围和最终技术输入；不改变 2026-10-04 的冻结报告，不给新无理性定理。

## 1. 被审对象、版本与审阅者

| 技术稿 | 最终 SHA256 | 本轮数学审阅范围 |
|---|---|---|
| [nonzero](E:/kimi-build/zeta5/research/odd_zeta_log_nonzero_20261005.md) | `b7a3b36ccbb5d4f9c208f1b58d2ca3407228120fa5453fc27e070751d717f171` | paper_mechanism 作者；根任务独立全文；distribution 独立 §§4–5 与 §2 原文匹配；通过 |
| [uniform endpoint](E:/kimi-build/zeta5/research/odd_zeta_uniform_endpoint_nonzero_20261005.md) | `f939374a37b6006b498c934575724520cd44cb793d20571926db0d111b683018` | paper_mechanism 作者；根任务与 moment_extension 分别独立全文；通过 |
| [saddle](E:/kimi-build/zeta5/research/odd_zeta_log_saddle_20261005.md) | `6389841b0700a5ab897ec395d8b83db3d2c09ccd679ef3e48ad9d7117c851288` | 根任务作者；paper_mechanism 独立 §§1–5、新增代数化段与 §6 条件预算；distribution 独立 §§1–5；通过 |
| [arithmetic](E:/kimi-build/zeta5/research/odd_zeta_log_arithmetic_20261005.md) | `9e675637cdd5c5c38e0afc23ea8ec5326c6f39c1438581a3846fc3ce6149f36d` | moment_extension 作者；根任务独立 §§1–6；distribution 独立 §§3–6 并独立推得相同 B 主项；paper_mechanism 独立 §§1–6 书面数学及六个 κ 的有理复算；通过 |
| [structure](E:/kimi-build/zeta5/research/odd_zeta_log_structure_20261005.md) | `a3ee91ef81375dc77b4171ce4b734be5453319a0433a70653347143ffeb9c952` | distribution 作者；根任务与 moment_extension 分别独立数学 §§2–4，根任务另核 §6 的 Pick 范围与 §7 的 Meijer-G/curve；通过。本人登记该独立审阅，不冒称已独立复核其全稿 |

这些分工名指本项目相应代理。作者自己的精确证书与另一代理的书面数学审核分别列明；有限脚本不承担无限尺度证明。

## 2. 非零与统一引理：实际新进展及范围

完整 Euler–Rodrigues 与伴随身份的边界项合法；扩展 Chebyshev 测试空间给全部 polynomial 的内部单根，但不自动给单独 Cauchy component 非零。两个固定伴随核点与两个固定端点的符号由完全有理 log₂/Euler-η 界认证，故本族固定符号及直接伴随非负核的提议失败。

q=7 的 `p=7n−1` 局部结论准确：Lucas 仅四位项存活；`v_p(S)=−7`、B 为单位、候选有理根的 `p⁷α modp=32/63`，本原整数对 p 赋值为 `(7,0)`。C 的固定素因子均不在当前 progression 中。Dirichlet 与“有一零项则目标先成为有理数”的分母论证给无条件最终非零子序列，没有预设 ζ(7) 无理。

统一稿的每个固定 q,k 版本保留有限删素数条件及 `p>2q`；Catalan 改用 `p=2qn−1`，只需最高 quotient coefficient 为单位，不要求 B 为单位，其候选根赋值更精确为 `−2−v_p(B)`。两类本原 pair 账本完整。结论都是指定无穷子序列仅有限零项，阈值一般非有效；没有对全部参数或全部 n 的非零量词。一个变化素数只支付 `O(logn)` 成本，不给线性于 n 的预算。

## 3. 围道与强渐近：本人已核的关键依赖

核过 Mellin–Barnes 的正负抵消；`K^(6)` 必须是第六阶导数；实轴 1 至 n 的七阶零/极点正好抵消。后续水平变形在上、下半平面进行，没有跨过 n 之后仍存在的实轴极点。Gamma 比值的 `n⁻⁴`、h 及完整高斯常数 D 匹配。

有理 Rouché 左侧使用 L₁ 上界、右侧使用单分量下界，故根盘存在性是精确证明；Acb 外包覆盖整盘并选定 `F′=−iπ`。纵线 g 的一转点结构、较外 saddle 的唯一全局峰、连接矩形的 `ReF′>0`、连接段严格较小的指数及无穷尾均闭合。起始 Γ 参数的实部仅为 1/2，需要一致有界的乘性余项，稿中没有误称该段余项为 `O(1/n)`。

局部 Gaussian 奇项抵消和共轭相加给正确的 `n⁻⁷ᐟ² Re(DΛⁿ)`，误差针对复 saddle 振幅。新增 `H*=F−wF′` 与代数 Λ 的负号准确，不引入 phase 是 π 无理倍的假设。只需被认证的 `sinΘ≠0` 即给每个充分大的相邻两项块至少一项指数大，以及 raw `limsup log|I|/n=A>1.817`。没有宣称每个单项增长或非零。

## 4. 算术与联合预算：本人已核的关键依赖

正尾和与 `S<0`、Stirling 熵函数严格最大点、离散 Laplace 主项和 β 化简均成立。Lucas 块的 carry 截断、六个非零有理 κ、单位集合等价及无限反射消失族正确；本人另直接用 Fraction 重算全部六个 κ，与表吻合。非单位情况不能约掉 C；反射例也不能推出正比例的加权例外集合。

完整 gcd 的奇素数简化、2 层区别和 `h≤64 gcd(63B,s)≤4032B` 正确。指定单位素数的七层在本原化后保留。有限带权窗口下界中的 42 与安全 LCM 上界中的 49 不可互换。

saddle 最终 §6 在每个大值块选出的无穷子序列上合成

\[
\limsup\frac1n\log|\ell_n|\ge A+42-\beta_7-7e,
\quad e=\limsup\frac{E_n}{n}.
\]

它使用对所有尺度成立的算术有限界，不要求每个实际积分最终非零。`A>1.817,β₇<23.19,e≤2.94` 给严格正下界，保守余量为 0.047。但 `e≤2.94` 尚未证明；e 是带 logp 权重的量，不是素数个数比例。此条件失败判据不是无条件完整本原失败结论，也不排除特殊子序列或新的整数尺度组合。

## 5. 结构稿与下一研究的准确接口

根任务独立核 structure 的有理 Cauchy 闭合、通过 monodromy 的实际函数独立、最高 component 的 cyclic determinant，以及 log-normalized 基本解组。此处的 rank q+1 来自标准 polylog rational gauge；不把它宣传为新的目标常数或扩大解析域，也不由函数秩推指定端点无理。

本轮闭合了 q=7 的真实 raw 振荡指数和可用的非零机制。未闭合的是算术非单位集合的带权分布、完整本原成本，以及任何改造后族的净负指数。后续若改变节点、尺度组合或 mixed 条件，须重核真实纯性、非零、高度与 gcd，不能仅消掉一个渐近首项就认作指数节省。

无剩余必要实质纠错。五技术稿的作者均已确认最终版本；structure 的最后修改仅增加本地 PDF 导航，数学不变。此记录的版本哈希和审阅范围用于最终总核验；旧冻结稿保持不动。本记录此版本冻结。
