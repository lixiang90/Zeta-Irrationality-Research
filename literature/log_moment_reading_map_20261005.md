# 对数矩、多重正交与端点渐近：2026-10-05 文献地图

对应[本轮研究进展](../research/odd_zeta_log_moment_progress_20261005.md)。
本轮新增六份原始 PDF，保持取件字节；[清单](manifest_log_moment_20261005.json)记录版本、
实际 URL、页数、SHA-256 与首页身份，[来源配置](log_moment_sources_20261005.json)可复跑取件。
总计 191 页。数学适用范围由读原文与具体参数匹配承担，视觉与散列检查只确认文件身份。

## 1. 直接匹配与不能直接移植的定理

| 保存的原件 | 固定版本／页数 | 当前用途和适用边界 |
|---|---|---|
| [Smet–Van Assche：Mellin transforms for multiple Jacobi–Piñeiro polynomials](smet_vanassche2008_mellin_author.pdf) | 作者稿首页 2008-08-06；25 页 | Th.2.4 直接处理合流 log 权，取 α=0、对角指标即本候选；只支付 Mellin 因式与正交结构，不自动证明最高 Cauchy 端点非零。 |
| [Kalmykov–Lysov–Shukla：Strong asymptotics for Jacobi-Piñeiro orthogonal polynomials](kalmykov_lysov_shukla2026_jacobi_pineiro_asymptotics_v1.pdf) | arXiv:2608.20594v1，2026-08-20；56 页 | 两权非合流的 Riemann–Hilbert 强渐近；Th.7.1 的另一个 β=0 变体还要求固定非对角比例。不能直接代入七权、合流最高 Cauchy 分量。 |
| [Lysov：Integral representations for the Jacobi–Piñeiro polynomials and the functions of the second kind](lysov2019_jacobi_pineiro_integral_representations.pdf) | 出版原件，2019；Probl.Anal.Issues Anal.8(26):3,83–95；13 页 | scalar equation 与正确归一化 second-kind 分离模板；Th.1 双积分及负轴辅助余项限两权、参数差条件，不能混同裸最高 Cauchy 分量。 |
| [Neuschel–Van Assche：Asymptotic zero distribution of Jacobi-Piñeiro and multiple Laguerre polynomials](neuschel_vanassche2016_zero_distribution_v2.pdf) | arXiv:1509.04542v2，提交记录 2016-01-07；19 页 | 一般多重正交的 type-II 零点分布；即使另证合流极限，仍不等于某个 Cauchy 端点的强渐近和非零。 |
| [Wolfs：Applications of multiple orthogonal polynomials with hypergeometric moment generating functions](wolfs2024_multiple_orthogonal_hypergeometric_v2.pdf) | arXiv:2401.08312v2，2024-04-16；39 页 | explicit hypergeometric Hermite–Padé；Th.5.10 的 \(p<q\) factorial 余裕是必要假设，文中 §5.2 明确区分 polylog \(p=q\) 边界。 |
| [Fidalgo Prieto–López Lagomasino：Nikishin systems are perfect](fidalgo_lopez2010_nikishin_perfect_v1.pdf) | arXiv:1001.0554v1，2010-01-04；39 页 | 真实 generating measures、支持、正则性和指标条件；仅有 AT/extended Chebyshev 性质不能调用其所有 logarithmic/ratio asymptotics。 |

原始来源分别为：
[Smet–Van Assche 作者 PDF](https://wis.kuleuven.be/analyse/members/walter/mellin.pdf)，
[Kalmykov–Lysov–Shukla 固定 v1](https://arxiv.org/pdf/2608.20594v1)，
[Lysov 出版 PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=pa&option_lang=eng&paperid=274&what=fullt)，
[Neuschel–Van Assche 固定 v2](https://arxiv.org/pdf/1509.04542v2)，
[Wolfs 固定 v2](https://arxiv.org/pdf/2401.08312v2)，
[Fidalgo Prieto–López Lagomasino 固定 v1](https://arxiv.org/pdf/1001.0554v1)。

**版本注意。** Smet–Van Assche 保存的是首页 2008-08-06 的作者稿；
其 J.Approx.Theory 162(2010),782–806 的发表题目另含 “and a q-analogue”，不能混作同一版本。
Neuschel–Van Assche 的 arXiv v2 提交戳为 2016-01-07，PDF 内作者日期另为 2018-08-15；
清单分别保留，不推断额外 arXiv 修订。编译元数据不是新的出版日期。

## 2. 与本项目输入的准确连接

[结构报告](../research/odd_zeta_log_structure_20261005.md)将本候选完全识别为
合流 Jacobi–Piñeiro type-II 的整数归一化，
另直接推导 Cauchy/polylog rational gauge、实际最小阶数 \(q+1\) 与 log-normalized 基本解组。
Smet–Van Assche 提供的原始 theorem 直接匹配；无需借未证明的合流连续性。

[围道报告](../research/odd_zeta_log_saddle_20261005.md)独立分析实际最高 Cauchy 目标，
没有把外域 polynomial 或任一辅助基本解的渐近当作该目标的渐近。
统一 Gamma 展开参照 [NIST DLMF §5.11](https://dlmf.nist.gov/5.11)；
实际变形围道、相位、连接段与唯一主峰在项目报告中逐项证明。
已得正 limsup 指数与相邻块非零，完整本原预算另需算术。

[算术报告](../research/odd_zeta_log_arithmetic_20261005.md)的 Lucas 因子与反射例、
[非零报告](../research/odd_zeta_log_nonzero_20261005.md)及
[统一非零接口](../research/odd_zeta_uniform_endpoint_nonzero_20261005.md)
是具体整数/有理系数的推导，不能从上述正常性、实根或 perfectness 定理自动继承。
Dirichlet 和素数定理是明确的标准外部输入；有限例不证明它们。

## 3. 优先阅读顺序

1. Smet–Van Assche Th.2.4 与 §2.2：核归一化、变量平移和精确矩零点。
2. Lysov §2–3：区分裸 Cauchy 分量与归一化基本解；核负轴辅助测度如何进入。
3. Kalmykov–Lysov–Shukla 的全局两权假设与 Th.7.1 的特定变体；
   对照本项目直接围道证明，不能把“已有强渐近”改称当前目标定理。
4. Wolfs §5.2、Th.5.9–5.10：核 factorial 余裕在 polylog 边界为什么丢失。
5. Fidalgo Prieto–López Lagomasino Th.1.5–1.6：写出真正的测度和支持条件，
   再判断是否能建立新的 Nikishin 实现；AT 性质只是其中一部分。
6. Neuschel–Van Assche Th.1.1：将零点分布用于 polynomial 高度或潜势，
   不将其替代目标端点相消。

此前的[显式端点与 Padé 地图](explicit_relative_reading_map_20261004.md)、
[K₂地图](k2_gap_reading_map_20261004.md)与[总体地图](reading_map_20261004.md)保持冻结。
本轮未发现可直接套入 \(q=7,\alpha=0,\text{diagonal},z=-1\) 裸最高 Cauchy 分量的现成定理；
这个判断仅限于上述已审阅原件，不是文献不存在性结论。

