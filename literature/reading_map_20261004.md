# 全部奇数 ζ 与 Catalan：文献阅读地图

核对日：2026-10-04。本轮新增 **28份原始PDF**，复用两份已有PDF；以下30条均已保存且可解析。PDF原件保留原字节，未翻译、改写或去除出版方信息。文件名只帮助识别；固定版本、实际下载URL、检索时间、页数与SHA-256以 [归档清单](manifest_global_20261004.json) 为准。

建议先读 [总体研究判断](../research/odd_zeta_global_strategy_20261004.md)，再按以下顺序进入原文：

1. **统一对象**：Brown2014周期综述、Deligne2010 level4；区分已证结构与比较点泛型猜想。
2. **已成功的新证明机制**：CDT2025框架稿，再读CDT2024的L(2,χ₋₃)长文；先理解函数秩、分母与解析容量。
3. **纯目标的几何实例**：Dupont奇ζ动机、Eskandari–Murty–Nemoto Catalan动机最新v3；检查真实投影和整模型。
4. **逼近判据**：Zudilin2017；然后比较ζ(5)论文已有输入与跨权构造的缺口。
5. **防止误用通用定理**：Huber–Wüstholz的1-period范围、Rivoal的G函数特化反例。
6. **最新文献审计**：Lai2026正文Theorem/Claim区别，以及Sun/Wachs声称与批评的配对阅读。

“已证结果”表示原文定理的文献状态，不表示本项目已形式化复核整篇证明。动机结构、p-adic无理性、无理值个数、线性空间维数、指定实值无理性分别标记，不能互相替换。


## 算术 holonomy、模形式及 p-adic 对照

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [The linear independence of 1, zeta(2), and L(2, chi_{-3})](cdt2024_l2_chi_minus3.pdf) · [来源](https://arxiv.org/abs/2408.15403v2) | arXiv:2408.15403v2, 2024-09-16 | 218 | 已证结果。证明1、ζ(2)、L(2,χ₋₃)线性无关；非Catalan定理。 |
| [Arithmetic holonomy bounds and effective Diophantine approximation](cdt2025_arithmetic_holonomy.pdf) · [来源](https://arxiv.org/abs/2510.04156v1) | arXiv:2510.04156v1, 2025-10-05 | 20 | 框架与已证应用。统一判据；实与2-adic Catalan周期项不同。 |
| [The unbounded denominators conjecture](cdt2024_unbounded_denominators.pdf) · [来源](https://arxiv.org/abs/2109.09040v4) | arXiv:2109.09040v4, 2024-09-16 | 62 | 已证结果。模形式与算术holonomy的技术来源；非所有周期无理性定理。 |
| [Irrationality of certain p-adic periods for small p](calegari2004_padic_irrationality.pdf) · [来源](https://arxiv.org/abs/math/0408214v1) | arXiv:math/0408214v1, 2004-08-16 | 11 | p-adic已证结果。区分p-adic周期与实周期。 PDF内部正文日期2018-10-28，与arXiv提交日不同，按字节归档。 |

## 动机、周期与调节子

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Mixed Tate motives over Z](brown2012_mixed_tate_motives.pdf) · [来源](https://annals.math.princeton.edu/2012/175-2/p10) | Annals of Mathematics 175(2), 2012, 949-976 | 28 | 动机层已证结构。数值周期的独立性还需周期猜想。 |
| [Motivic periods and P1 minus {0,1,infinity}](brown2014_motivic_periods.pdf) · [来源](https://arxiv.org/abs/1407.5165v1) | arXiv:1407.5165v1, 2014-07-19 | 25 | 框架与猜想。ICM2014；作者URL里的v3不等于arXiv v3。 |
| [Notes on motivic periods](brown2017_notes_motivic_periods.pdf) · [来源](https://arxiv.org/abs/1512.06410v3) | arXiv:1512.06410v3, 2017-02-22 | 66 | 框架。形式周期、比较映射与数值关系的边界。 |
| [Le groupe fondamental unipotent motivique de Gm - mu_N, pour N=2,3,4,6 ou 8](deligne2010_cyclotomic_fundamental_group.pdf) · [来源](https://www.numdam.org/item/PMIHES_2010__112__101_0/) | Publications mathematiques de l'IHES 112 (2010), 101-141 | 41 | 已证结构及条件性猜想。level 4包含ζ奇数值与β偶数值；Conj.5.6并非已证。 |
| [Groupes fondamentaux motiviques de Tate mixte](deligne_goncharov2005_mixed_tate.pdf) · [来源](https://www.numdam.org/item/ASENS_2005_4_38_1_1_0/) | Annales scientifiques de l'ENS 38(1) (2005), 1-56 | 56 | 动机框架。混合Tate与cyclotomic基本群。 |
| [Cohomologie de SLn et valeurs de fonctions zeta aux points entiers](borel1977_regulators_l_values.pdf) · [来源](https://www.numdam.org/item/ASNSP_1977_4_4_4_613_0/) | Annali della Scuola Normale Superiore di Pisa 4(4) (1977), 613-636 | 25 | 调节子已证结果。须连同1980勘误阅读；非零regulator不自动推出无理。 |
| [Corrections to Cohomologie de SLn et valeurs de fonctions zeta aux points entiers](borel1980_regulators_erratum.pdf) · [来源](https://www.numdam.org/item/ASNSP_1980_4_7_2_373_0/) | Annali della Scuola Normale Superiore di Pisa 7(2) (1980), 373 | 2 | 勘误。Borel1977配套勘误。 |
| [Transcendence and linear relations of 1-periods](huber_wustholz2018_one_periods.pdf) · [来源](https://arxiv.org/abs/1805.10104v8) | arXiv:1805.10104v8, 2022-04-21; monograph final draft | 237 | 1-period已证结果。适用1-motives；高权ζ与Catalan不能直接套用。 |
| [Periods and the conjectures of Grothendieck and Kontsevich-Zagier](ayoub_periods_gkz.pdf) · [来源](https://www.math.uzh.ch/en/fileadmin/user/ayoub/publikation/periods_GKZ.pdf) | 作者公开稿；归档时未确认稿件日期 | 9 | 功能版本与数值猜想边界。函数周期理论与数值周期猜想不能混同。 |
| [G-functions, motives, and unlikely intersections - old and new](andre2026_g_functions_motives.pdf) · [来源](https://ems.press/journals/rlm/articles/14299473) | RLM36(2025), 381-392; published 2026-01-30, DOI10.4171/RLM/1075 | 12 | 综述与方法边界。期刊卷年2025，实际发表日2026；非固定周期普遍无理性定理。 |

## 单目标判据、几何积分与最新维数界

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Irrationality proofs for zeta values, moduli spaces and dinner parties](brown2014_irrationality_moduli.pdf) · [来源](https://arxiv.org/abs/1412.6508v1) | arXiv:1412.6508v1, 2014-12-19 | 39 | 几何统一构造。M0,n容纳Apéry和Ball-Rivoal；不自动隔离每个ζ值。 |
| [Odd zeta motive and linear forms in odd zeta values](dupont2018_odd_zeta_motive.pdf) · [来源](https://arxiv.org/abs/1601.00950v3) | arXiv:1601.00950v3, 2018-06-10; Compositio154(2018),342-379 | 31 | 动机与线性型构造。v3修正Prop.3.12并匹配发表版。 |
| [A determinantal approach to irrationality](zudilin2017_determinantal_irrationality.pdf) · [来源](https://arxiv.org/abs/1507.05697v2) | arXiv:1507.05697v2; Constructive Approximation45(2017),301-310 | 9 | 一般行列式判据。行列式无理性判据早于ζ(5)新论文。 |
| [Hankel determinants of zeta values](haynes_zudilin2015_hankel_zeta.pdf) · [来源](https://sigma-journal.com/2015/101/) | SIGMA11(2015),101 | 5 | Hankel已证结果。族无理性或分母超指数增长的二择；不指定每个ζ值。 |
| [Small improvements to the Ball-Rivoal theorem and its p-adic variant](lai2026_ball_rivoal_improvements.pdf) · [来源](https://arxiv.org/abs/2407.14236v3) | arXiv:2407.14236v3, 2026-09-25 | 50 | 定理与计算Claim分列。正文Theorem常数1.009；计算强化1.119356列Claim，非同一审查级别。 |
| [On cellular rational approximations to zeta(5)](brown_zudilin_cellular.pdf) · [来源](https://arxiv.org/abs/2210.03391v3) | 已有文件：arXiv:2210.03391v3, 2026-01-29 | 32 | 已有文件复用。保留现有原件；有效逼近指数0.86本身不超过无理性门槛。 |
| [Linear independence of odd zeta values using Siegel's lemma](fischler_siegel_odd_zeta.pdf) · [来源](https://arxiv.org/abs/2109.10136v3) | 已有文件：arXiv:2109.10136v3；本地正文日期2025-12-01 | 44 | 已有文件；版本差异记录。现有PDF44页；网页HTML正文日期不同，保留字节与SHA，不擅自覆盖。 |

## 模变换与奇数 ζ

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Ramanujan's formula for zeta(2n+1)](berndt_straub2017_ramanujan_zeta.pdf) · [来源](https://arxiv.org/abs/1701.02964v1) | arXiv:1701.02964v1, 2017-01-11 | 21 | 模变换综述。模变换含其他周期或Lambert级数；不是Euler型奇数值公式。 |

## Catalan 与 Dirichlet L 值

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Mixed motives and linear forms in the Catalan constant](eskandari_murty_nemoto2025_catalan_motive.pdf) · [来源](https://arxiv.org/abs/2510.20648v3) | arXiv:2510.20648v3, 2026-08-29 | 39 | 动机已证构造；无理性未得。Q上非mixed Tate；Q(i)后mixed Tate；需实际分母和整Chebyshev改进。 |
| [On two families of period integrals related to Catalan's constant](eskandari2026_catalan_period_families.pdf) · [来源](https://arxiv.org/abs/2609.26308v1) | arXiv:2609.26308v1, 2026-09-22 | 16 | 周期族比较。部分新几何族与旧超几何族相等；有理归一化不能省略。 |
| [Diophantine properties of numbers related to Catalan's constant](rivoal_zudilin2003_catalan_relatives.pdf) · [来源](https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf) | Math. Ann.326(2003),705-721; 作者公开稿 | 17 | 偶β族已证结果。无限多偶β无理、七个中至少一个；不指定Catalan。 |
| [Irrationality of values of L-functions of Dirichlet characters](fischler2020_dirichlet_irrationality.pdf) · [来源](https://arxiv.org/abs/1904.02402v1) | arXiv:1904.02402v1; JLMS2020 DOI10.1112/jlms.12290 | 25 | 周期函数L值族定理。固定奇偶下的维数和计数，非每个指定值。 |

## G 函数：可用范围与反例

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Remarks on the impossibility of a Siegel-Shidlovskii like theorem for G-functions](rivoal2015_g_function_counterexamples.pdf) · [来源](https://hrj.episciences.org/1357) | Hardy-Ramanujan Journal38(2015),29-35; HAL01253639v1 | 7 | G函数普遍特化类比的反例。函数代数独立不能普遍传递到G函数值。 |
| [On Siegel's problem and Dwork's conjecture for G-functions](fresan_lam_qin2025_g_functions.pdf) · [来源](https://arxiv.org/abs/2502.02147v1) | arXiv:2502.02147v1, 2025-02-04 | 24 | 超几何化范围反例。几何局部系统不都能归入所讨论超几何拉回范围。 |

## 证明声称及批评稿：配对阅读

| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |
| --- | --- | ---: | --- |
| [Catalan's constant is irrational](sun2026_catalan_claim.pdf) · [来源](https://arxiv.org/abs/2609.04176v1) | arXiv:2609.04176v1, 2026-09-03 | 20 | 证明声称；本项目未采纳为定理。同时保存Wachs批评；不据摘要认定无理性已解决。 |
| [A note on a recent claimed proof of the irrationality of Catalan's constant](catalan2026_claim_critique.pdf) · [来源](https://arxiv.org/abs/2609.22339v1) | arXiv:2609.22339v1, 2026-09-16 | 8 | 批评预印本；范围限定。指出展示的渐近推导未闭合；不等于证明最终不等式必假。 |

## 版本与验证注意

- Brown2012 Annals原件可直接打开；PDF含空打开密码的出版方加密标记。验证时仅在内存读取，保存字节完全不变。
- Borel1980为两页归档PDF，含NUMDAM封面；不要把PDF页数与文章的单页出版页码混同。
- Brown2014本地为arXiv v1。动机专题中另引作者v3的页码，不能直接套到本地v1；这是不同版本来源。
- Brown–Zudilin已有文件是2210.03391v3；本轮保留原件。Fischler已有文件标2109.10136v3、正文日期2025-12-01，而当前HTML正文日期不同；未覆盖文件，也未因版本号相同宣称字节相同。
- Calegari2004归档固定arXiv v1，但PDF正文内部日期为2018-10-28；两个日期都保留。
- 六篇代表原件的首页已渲染抽查，见 [验证图](../research/archive_validation_20261004.png)。PDF签名/解析/页数/SHA检查只确认归档完整性，不确认数学证明正确。

已有经典论文、ζ(5)形式化对象及p-adic资料继续保留在 [原有索引](README.md)。新增PDF来源配置为 [global_sources_20261004.json](global_sources_20261004.json)；下载与索引脚本位于research，均不覆盖已有PDF。
