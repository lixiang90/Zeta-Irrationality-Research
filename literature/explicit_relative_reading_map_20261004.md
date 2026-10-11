# 显式端点、对数矩与 Padé：本轮文献地图

日期：2026-10-04。对应[研究进展](../research/odd_zeta_explicit_relative_progress_20261004.md)。
本轮新增五份作者／机构／arXiv 原始 PDF，保存下载字节；
[清单](manifest_explicit_relative_20261004.json)记录固定来源、版本、页数与 SHA-256。
首页视觉身份核验仅用于确认文件，数学适用范围另由正文阅读与研究报告承担。

## 1. 五份新增原件

| 原件 | 固定版本／本地页数 | 对当前缺口的用途与限制 |
|---|---|---|
| [Fischler–Rivoal：Multiple zeta values, Padé approximation and Vasilyev’s conjecture](fischler_rivoal2013_mzv_pade_vasilyev_v1.pdf) | arXiv:1309.2534v1，提交 2013-09-10；20 页 | Theorem 1 的具体 mixed multiple-polylog Padé 条件、唯一性与多重积分；Proposition 1 的特殊 MZV 评价。高权完整积分仍可含多个奇 ζ，不能指定 ζ(7) 无理。 |
| [Fischler–Rivoal：Approximants de Padé et séries hypergéométriques équilibrées](fischler_rivoal2003_pade_balanced_hypergeometry.pdf) | 作者公开稿；J. Math. Pures Appl. 82 (2003), 1369–1394；PDF 29 页 | 同时 Padé、平衡超几何与奇点特化的结构模板；它解的具体函数问题不同于本项目 scalar log-moment 条件。 |
| [Zudilin：Approximations to -, di- and tri- logarithms](zudilin2004_approximations_di_tri_log_v1.pdf) | arXiv:math/0409023v1，2004-09-02；11 页 | 整数值多项式、部分分式及微分后的分母成本；原文属于方法与逼近贡献，不能据此宣布新无理性定理。 |
| [Krattenthaler–Rivoal：On a linear form for Catalan’s constant](krattenthaler_rivoal2008_catalan_linear_form_v1.pdf) | arXiv:0810.1927v1，2008-10-10；12 页 | Theorems 1–2 的真实系数整性与超几何变换；说明粗 LCM 可以改进，但作者明确结果仍不足证明 \(G\) 无理。 |
| [Prévost–Sorokin：Hermite-Padé approximants and Apéry theorem](prevost_sorokin_hermite_pade_apery_author.pdf) | 机构公开稿 lmpa326；8 页；原件未标明可核实版本日期 | §3 循环 polylog 系统及唯一解，§5 实际 Apéry ζ(3) 近似；低权的成功结构不自动推广到所有奇权。 |

逐份原始来源：
[Fischler–Rivoal 2013 固定 v1](https://arxiv.org/pdf/1309.2534v1)，
[Fischler–Rivoal 作者稿](https://rivoal.perso.math.cnrs.fr/articles/fisridef.pdf)，
[Zudilin 固定 v1](https://arxiv.org/pdf/math/0409023v1)，
[Krattenthaler–Rivoal 固定 v1](https://arxiv.org/pdf/0810.1927v1)，
[Prévost–Sorokin 机构原件](https://www-lmpa.univ-littoral.fr/publications/articles/lmpa326.pdf)。

**版本注意。** 1309.2534 的 arXiv 页面目前列出 v1；其 PDF 内部 Date 为 November 1, 2018，
应与 v1 提交时间分别记录，不能虚构 arXiv v2 或据此称为 2018 新稿。
另有 2013-12-21 的[作者修订稿](https://rivoal.perso.math.cnrs.fr/articles/mzvconj.pdf)，21 页；
本轮没有把它下载并混入上述 v1 清单。Prévost–Sorokin PDF 的编译元数据也不作为出版年份依据。

## 2. 与本轮已证输入的连接

[四项 Steinberg 链](../research/odd_zeta_explicit_steinberg_20261004.md)解决的是固定周期身份：
直接整数 \(T=0\)、有理链、端点 \(-4[i]\) 与完整 Li₂ primitive。
它没有给一个随 \(n\) 改变的逼近族。
沿用[上一轮地图](k2_gap_reading_map_20261004.md)中的 Suslin 五项关系与 Neumann–Yang/Bloch–Wigner 背景，
无需重新下载或改动原件。

[真实 Mellin 分母窗口](../research/odd_zeta_cyclotomic_mellin_20261004.md)强调：
具体候选的约分后分母与全部 gcd 才决定整数形式是否小。
Krattenthaler–Rivoal 的整性改进正是不能只用粗 LCM 作全局排除的文献对照。
本项目的排除已覆盖指定不平衡区间，未排除平衡族或全部 signed 方法。

[普通 Rodrigues 报告](../research/odd_zeta_relative_family_audit_20261004.md)已证明实际非零和精确指数；
高阶导数成本使普通矩消元保留原衰减指数。
Zudilin 2004 的部分分式算术提醒：导数阶数增加，须同步计入分母。

[多阶 log-moment 候选](../research/odd_zeta_log_moment_candidate_20261004.md)已有显式整数系数、
Mellin 零阶和一维唯一性。
Fischler–Rivoal 与 Prévost–Sorokin 的函数系统提示下一步应控制完整 Cauchy/monodromy/endpoint 条件；
其定理没有自动证明本候选的指定端点非零或清分母后净衰减。

## 3. 建议阅读顺序

1. 先对照本项目 log-moment 的 Mellin 因式，再读 Fischler–Rivoal 2013 的 Theorem 1、Proposition 1、§6，
   区分“具体 Padé 问题已解”与“新问题尚须证明”。
2. 用 Prévost–Sorokin §3、§5 检查循环函数闭包如何与实际有理端点结合；
   与当前仅有 scalar 矩条件的差距要写成明确输入。
3. 用 Fischler–Rivoal 2003 与 Zudilin 2004 比较多点条件、平衡超几何、整数值多项式，
   再核本候选的实际共同分母。
4. 用 Krattenthaler–Rivoal Theorems 1–2 检查 content 的真实节省，
   最后比较整数形式的净指数，不能在整性或 recurrence 阶段提前宣布成功。

[来源配置](explicit_relative_sources_20261004.json)可用于固定版本重新取件。
此前的[总体地图](reading_map_20261004.md)、[桥梁地图](bridge_reading_map_20261004.md)、
[新周期地图](next_route_reading_map_20261004.md)和[K₂地图](k2_gap_reading_map_20261004.md)继续保留。

