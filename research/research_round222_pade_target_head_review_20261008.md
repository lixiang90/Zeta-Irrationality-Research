# 第222轮 Padé 目标系数有限起点独立复核

2026-10-08。审阅者 round218_lambert_carrier。结论 **PASS**：Root三个有限尺度的系数及Δ₀均由独立 exact 表达式复核；新增伴随稿的结论边界正确。没有重跑Root producer，没有修改旧11908-byte论文、目标证书、旧稿、main或manifest。

实际完整读取的冻结输入：

| 文件 | bytes | SHA256 |
|---|---:|---|
| [Root producer](certify_pade_target_head_round222_20261008.py) | 2046 | `f6c4c10658ef388bc05a77d6331f254ec25cd64a370dac23da5bd0acde41df1e` |
| [Root输出](pade_target_head_certificate_round222_20261008.json) | 550 | `5f718666ac8e40e74bf4d7c1946ed1938ed68275d72b866d9032f32a05323127` |
| [有限非零伴随稿](pade_target_head_nonzero_round222_20261008.md) | 3006 | `c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f` |
| [公式原稿](relation_source_architecture_global_round222_20261008.md) | 11908 | `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d` |

原稿是本人作者稿，本次FULL复读它作为公式输入，不冒充该稿的独立审阅；本收据独审Root新增producer、输出与伴随结论。

独立算法令F(v)=v⁶R_n(−k+v)。直接由整数距离乘积求F(0)，不使用Root的截断factor convolution或导入其代码。设

L_r=(log F)^(r)(0)
= (−1)^(r−1)(r−1)! [3Σ_{j=1}^n ((−k−j)^(−r)+(n+j−k)^(−r))
                         −6Σ_{b=0,b≠k}^n(b−k)^(−r)].

这表示正则部分的有理log导数，不需要给负整数距离选择复log值。从F′=F(log F)′逐次Leibniz得Bell递推

Y₀=F(0),
Y_h=Σ_{r=1}^h binom(h−1,r−1)L_rY_{h−r},
c_{6−h,k,n}=Y_h/h!,  0≤h≤5.

全部在Fraction中计算，再按原稿P5形成三个A。另逐项核c_{j,n−k}=(−1)^j c_{j,k}；行列式使用记录行交换符号的有理Gaussian消元，与Root的Laplace展开分开。结果：

| n | A₃ | A₅ | A₇ |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 189/32 |
| 2 | −6951213/16 | −2983095/4 | −546021/2 |
| 4 | 4058945965642073/768 | 142953289482825/16 | 5759038915875/2 |

Δ₀=11581683398946533579805/32768>0，与Root证书完全一致。由P10–P11的列顺序，目标系数没有反号；这一结果排除Δ序列恒为零、Δ生成级数恒零及起点三行退化。

**只证明这个有限非零起点。** n=0本来就是纯ζ(7)，不能由该矩阵排除Δ_r最终为零，更不能推无限多个非零项、actual n-recurrence、最小holonomic秩、真实主奇点、严格过收敛或ζ(7)无理。旧稿当时“未证明任何Δ非零”的历史状态通过新伴随稿更新；P13费用与两个半径下界均没有因此得到改进。

独立保存并实际FULL读取代码与全部输出：

- [Bell verifier](review_pade_target_head_bell_round222_20261008.py)：4138B，SHA256 `5d927f6204f43322ebfbed3d2307124bf1993f0a79fb60f432f0ac110bfd47f7`。
- [独立完整输出](pade_target_head_bell_review_round222_20261008.json)：3271B，SHA256 `c39442df73ecaa941eb9c535c87df0dd80f69e78f0ace6e8bf41ec7199b80740`，包含全部有限极点c_j，exit0。

本任务独立数学程序 **1次**，仅预定n=0,2,4和一个3×3行列式；加Root原producer1次，本次新增有限证书合计 **2次**。无重跑、参数/prime扫描、浮点、数值周期、CAS、PSLQ、Lean或Git；没有新增primary文献读取。收据保存后作者实际完整复读，身份另行报告。
