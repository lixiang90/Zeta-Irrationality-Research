# 第227轮进展：全处预算、固定3内容与路线降级

2026-10-08。研究目标继续 active；本轮没有新的 ζ/L 数值无理性或线性无关性定理。三项纸面结果推进了实际接口，但没有得到原包的正净收益完整模型。**从本轮起，固定222–226 Padé包降为结构工具，不再作为默认数值路线；228进行正式全局回顾。**

## 1. 已证明的实际算术障碍

最高周期行保持原公式

`A_{7,n}=(189/32)Σ_{k=0}^n(-1)^k binom(n,k)^6 binom(n+k,n)^3 binom(2n-k,n)^3`。

取 n=2·3^e，模3二项式稀疏性使端点外的每一项被3^6整除，两个端点之和恰为2·binom(4·3^e,2·3^e)^3，其估值为3。因此

`v_3(A_{7,2·3^e})=6` 对所有 e≥0 成立。

于是原 F_7(z)=Σ_r A_{7,2r}z^r 的3-adic Taylor半径恰为1。实际生成ODE的非零有限谱点均在3-adic半径至少27处；ordinary点不允许亚纯解出现pole。结合一元盘上的因子消去，证明同一个原生芽也不能亚纯延到任何center0、半径大于1的rigid盘。

这排除保留原 A_7 行的正3-affine入口，并排除对该行作正3深度缩放后仍由有限固定LCM列整化。**不自动移植到 Δ、Ξ、H_g=gΔ+Ξ 或其共同图。** 相邻行的低阶jets、有限tail与exterior消去仍是各自的算术问题。[完整证明与范围](pade_fixed_three_content_gate_round227_20261008.md)

## 2. 当前安全数组的全部有限处预算

在反证假设 ζ(7)=g∈Q 下，H_g 的实际系数是 J_n。对无限非零的有理序列 a_n，若增长率为 T、Q_na_n为整数、log Q_n/n的上极限≤σ，且所有p-adic Taylor半径 R_p≥1，则乘积公式给

`sup_{P finite}Σ_{p∈P}log R_p ≤ log T+σ`。

因此不能把各个有限处的正半径贡献无限独立累加。对当前已付数组，要求arch图单叶，finite图的整个映像留在原 H_g 的Taylor盘内；包括任意nonlinear finite图与全部有限处同时参与。真实energy与上述预算共同给：

- 两行 `(1,H_g)`：margin≤log4−13−13ε/2<0。
- 三行 `(1,D,H_g)`：margin≤2log4−10/3−5ε/3−2log(M/T)<0。

这里 ε>0 吸收 `2n+4` 的有限prefix；没有把极限表当literal数组。结论限于该安全数组和上述图类，**不是最优联合格费用的下界，也不排除过Taylor盘的实际亚纯延拓或ramified arch图**。

另已证明同一完整 S'-integer 数组对象的任意scalar/unit归一化可运输全部place图；乘积公式使全处 L、E及margin保持。literal最优整模型、projector改变源等情形另需证明。[全处证明与范围](pade_all_place_budget_round227_20261008.md)

## 3. 为什么现有局部信息不能证明所有大图失败

局部reflection有很大的固定空间。指定原生叶有非零半整数branch，不代表同一奇点的每个reachable叶都分支。即使整体monodromy不可约，也不能补上这个全称量词。

一个精确holonomic反例是 w³−3w=z、w(0)=0：其原生芽在±2有真实square-root分支，二阶方程的二维monodromy表示是不可约S3标准表示，`{1,w,w²}` 在Q(z)上秩3。但是

`Φ_K(ζ)=K³ζ³−3Kζ`，`w∘Φ_K=Kζ`，`|Φ_K'(0)|=3K`。

该图可有到达正则叶的simple前像，且导数任意大。其真实energy至少3logK，所以rank3的 `3log|Φ_K'(0)|−E` 至多3log3；原 w 的3-adic系数还具有线性负估值，不能靠有限固定LCM整化。它只否定从局部数据推出所有图上限的逻辑，**不是当前包的新图、CDT反例或免费正入口**。[完整反例、能量和条件界](pade_ramified_leaf_capacity_diagnostic_round227_20261008.md)

## 4. 大局判断与下一步

当前方向已经识别了实质障碍；继续调整raw univalent尺度、safe166/9或形式谱因子，不能解决这些缺口。固定包作为结构工具保留；再次主攻须先给同一目标的完整新模型，并明确正余量，或证明完整算术费用确实下降。

新保存并选读的 Fischler–Rivoal 文献表明，G-function实值的任意半径表示和相应过收敛逼近已存在，作者指出分母增长阻碍了其数论应用。Dreyfus–Rivoal 则排除了覆盖整个G-function类的固定复杂度超几何表示方案；它没有否定ζ/L特殊族或统一算术方法。两篇的准确条件与保存路径见[路线决定](pade_route_stop_and_global_inputs_round227_20261008.md)、[读取范围](../literature/pade_admission_stop_sources_round227_20261008/root_reading_scope.md)。

228正式比较仓库 ζ(5)/Catalan/CDT 构造的正收益机制、可控制整模型的受限周期族，以及更低费用的新 ζ/L 或周期组合目标。每条候选须有具体目标、新颖性、下一项可证接口和继续/放弃条件。上次正式回顾222，下一次228；用户要求每4～8轮，默认每6轮。两轮无核心接口推进或发现结构障碍时提前检查方向。

## 5. 审读、执行与保存边界

A/B/C各稿作者完整复读，Root实际完整独审三项数学稿及来源scope；B稿的一项conditional affine充分阈值需保留3-adic离散值群，最终稿按此修正。另有B独审A、A独审C、C独审Root方向及本报告，回执单独保存，不以作者自读代替独审。

本轮数学程序运行0：无CAS、序列取样、参数/素数扫描、数值积分、PSLQ、旧proof producer复跑或Lean构建。原作者文献保存与选段文字提取、哈希/链接检查属于文档操作；没有重新核当前云端仓库，也没有编辑 `E:/codex-build/math`。

原PDF的保存不代表完整阅读：Root仅实际完整读FR物理1–6及19–20、DR物理1–6；A/C/B自己的精确选读范围分别登记。最终manifest只核档案身份、链接与正文前缀，不把这些检查当数学形式化验证。[本轮manifest](../literature/manifest_cdt_pade_route_stop_round227_20261008.json)
