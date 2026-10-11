# 统一框架桥梁研究：补充文献与可证明的中间结果

日期：2026-10-04。本次桥梁研究另存3份开放原始PDF；与上一阶段的28份新增文献、2份复用记录分开记账。来源、版本、页数、SHA-256及首页文字见 [归档清单](manifest_bridge_20261004.json)。原件未修改。

本轮研究入口：[桥梁进展报告](../research/odd_zeta_bridge_progress_20261004.md)。其中的证明属于项目研究稿，未声称文献首创，也未得到新的指定ζ或Catalan无理性定理。

|文献与原始版本|本地原件|用于补哪处缺口|不能直接推出什么|
|---|---|---|---|
|Peter B. Borwein、Igor E. Pritsker，*The multivariate integer Chebyshev problem*，Constr. Approx.30(2009),299–310；[arXiv v1，2013-07-20](https://arxiv.org/abs/1307.5456v1)|[11页PDF](borwein_pritsker2009_multivariate_integer_chebyshev.pdf)|明确多元整Chebyshev范数与渐近常数的定义。本项目另证菱形域下界以及正积分全族障碍。|该文没有给Catalan实际本原系数的content增长定理。|
|Jean-Benoît Bost、François Charles，*Quasi-projective and formal-analytic arithmetic surfaces*，[v2，2022-09-14](https://arxiv.org/abs/2206.14242v2)|[189页PDF](bost_charles2022_arithmetic_surfaces.pdf)|算术曲面、formal-analytic geometry与holonomicity的结构背景；结合CDT理解秩、分母和解析容量必须作用于同一函数空间。|算术代数化结果不等于全部高权周期数值映射的单射。|
|Clément Dupont、Javier Fresán，*A construction of the polylogarithm motive*，Épijournal de Géométrie Algébrique9(2025),Article3；[v2，2025-02-18](https://arxiv.org/abs/2305.00789v2)|[32页PDF](dupont_fresan2025_polylogarithm_motive.pdf)|经典多重对数局部系统的真实相对上同调实现；帮助区分实际子商周期与形式删项。|真实动机构造本身不保证低分母的纯目标逼近或指定数值无理。|

建议配套阅读已有原件，而非单独使用以上三篇：

- [CDT长文v2](cdt2024_l2_chi_minus3.pdf)与[框架稿](cdt2025_arithmetic_holonomy.pdf)：同时核对允许函数空间的实际秩、分母类型和解析容量。
- [Eskandari–Murty–Nemoto Catalan动机](eskandari_murty_nemoto2025_catalan_motive.pdf)，Theorem8.3.1、Remark8.3.4：本轮正积分和真实整投影的原始输入。
- [Eskandari周期积分族](eskandari2026_catalan_period_families.pdf)（[原始版本](https://arxiv.org/abs/2609.26308v1)），Proposition5.1：纯G生成函数、非齐次递推和四维系统的原始输入。

项目中间结果及复核入口：

- [正整数多项式周期的全族下界](../research/odd_zeta_bridge_positive_integral_20261004.md)：给出完整证明及必要content指数。
- [真实动机投影与整格费用](../research/odd_zeta_bridge_projection_20261004.md)：实际拉回子对象、饱和格与Catalan四弧模型。
- [本原外积消元与参数秩](../research/odd_zeta_bridge_rank_20261004.md)：用完整子式content计算消元费用。
- [微分消元生存条件与monodromy障碍](../research/odd_zeta_bridge_differential_20261004.md)：明确何时消去干扰同时消掉目标。
- [Catalan纯周期芽及分母上界](../research/odd_zeta_bridge_catalan_20261004.md)：安全分母指数由6降到5，未把上界当最小分母。
- [Catalan实际四维函数独立性](../research/odd_zeta_bridge_catalan_system_20261004.md)：与G的有理性无关的函数独立和最小阶数4，并证明辅助函数的精确前缀分母及目标芽的分母指数下界4；[精确证书](../research/odd_zeta_bridge_catalan_system_20261004_verify.json)。

这些工作保留了全部奇ζ和偶β的统一几何入口，同时将尚未证明的输入存在命题与已完成的局部桥梁分开。没有用动机非平凡性、有限系数检查或一个较大的公因子冒充数值无理性。
