# 本原缺层与正测度路线：独立复核记录

日期：2026-10-05。四份技术报告与上一轮冻结文件分开保存；本记录只描述实际完成的审阅，不把运行脚本等同全尺度证明。

## 1. 已审阅技术稿及最终 SHA-256

| 文件 | 最终报告 SHA-256 | 独立数学审阅 |
|---|---|---|
| [本原根、第二 p-adic 块与三行高度](odd_zeta_log_primitive_20261005.md) | 2fd4bfd843db5a12bfa32c4fce2de003e58d3b37f2ea258ef15f89dc9abc4a0c | root 全文；paper_mechanism §§1–3/5、脚本及新增5.1；distribution §§1/5 |
| [异常素数与平均接口](odd_zeta_exceptional_primes_20261005.md) | c539cc35792769f141deca440c5d47a65e745037358c6b7688cdc03e73a54157 | root 全文，重点§§2–5 |
| [固定有理移位滤波器](odd_zeta_fixed_shift_filters_20261005.md) | 70c958736db4607eba9a4c164d4b71a80abc235006009a64028203deec6d5f99 | paper_mechanism §§2–4及脚本；moment_extension §§3–4；distribution §§1/5 |
| [type-I 对偶、正测度及统一目标](odd_zeta_mixed_pade_20261005.md) | d2ca842d8d4a7be71f9faf76d1721136ce110c779546af0fdd27c54c8d3c71d7 | root 全文；paper_mechanism §§2–5、7–7.3 |

无必要数学修正后冻结技术稿。其中异常素数稿的严格数值下界改为 \(>20.627\)，与已认证的 \(A>1.817,\beta_7<23.19\) 对齐，没有以辨识小数冒充更精确区间。主报告的双节点结论已按审阅限定为共同多项式、a=1,2 简单 Cauchy 核及逐系数过滤。

## 2. 审阅要点

- 本原根稿：真实 \(q_n=\operatorname{den}(-64S/(63B))\) 包含全部 gcd；局部付费 \(\max(0,7+v_p(B)-v_p(p^7S))\) 没有删去目标系数。模 \(p^2\) 块同时计入低位借位及末块；\(\rho_H<0\) 有全 H 的积分证明。真实缺层 \(\mathcal D_n\) 与第二零域的关系是安全不等式。新增三行根分母高度只需相邻有理数分离与真实渐近，ζ 在差中消去；半指数没有被误当本原净预算。
- 异常素数稿：确实区分变化指标与变化自变量的 root count。逐项反转分类的 degree-12 身份、支撑门槛及小支撑权重均成立。自然常数项 cube 的 partial Lucas 范围没有覆盖实际异常窗口；full Lucas 反例范围限于显示的全素数标量身份。条件双计数得到平均好行，不被扩大为每行界；相邻块大值与密度一好行可相交。
- 固定滤波器：mod 3 的 3+5 与 mod 5 的 1+7 配合直接 Frobenius 核验，确实证明八次谱不可约；真实正谱为其共轭。任意固定阶 Stirling/saddle 与离散 Poisson 步骤补齐高重数消去所需误差；滤波首项准确为 \((-1)^m(7/2)_mL^mP^{(m)}(L)/m!\)。结论不涉及未知 content 的指数。
- Padé：端点约束矩矩阵的可逆性由 ECT、正因子和符号变化证明；严格对偶、companion determinant 与 Cauchy determinant 同一尺度对齐。最高 log、Catalan 以及指定正组合都是真正单正测度；平方余项严格正。Chebyshev/Legendre 核 regularity 后，库内 Fidalgo–López Lemma 5.3 的全部单测度假设匹配，零点弱收敛给外域裸指数。完整整数乘子及 gcd 没有被略去，有限 bits 与有限小值没有被外推。

## 3. 主报告及有理对照

[主报告](odd_zeta_primitive_routes_progress_20261005.md)另经 distribution 复核 §§1/4/5/6，moment_extension 复核 §§2/3/5；root 对最终稿负责。主报告新§5.1 的实际有理目标测度 \((1+u)du\)、首尺度精确算术及全尺度正整数成本下界另经 distribution 独立复核通过，并有[独立固定证书](odd_zeta_markov_rational_control_20261005_verify.json)。其全尺度成本下界由正整数至少为 1 和相同裸指数推出，旨在明确统一框架必须使用目标的特殊算术结构，不是 ζ(7) 族的失败定理。

## 4. 验证边界与冻结保全

根代理重新运行四份技术脚本和有理对照脚本，全部通过。它们只核固定代数身份、整数/gcd、有限域、矩阵与有理 Euler 尾界，不证明未证的素数密度或目标系数渐近。全尺度分析与算术依赖上述书面证明。

五份新增 PDF 的全部首页已实际查看，题名、作者与版本标记匹配；97 页、原始 bytes 与 SHA-256 均验证。Ghosh–Ward 论文的后续撤稿状态从保存的原始 v4 HTML 核准，旧版仅作历史审计，未采用其任何定理。

[交付完整性证书](odd_zeta_primitive_routes_delivery_20261005.json)单独核四稿、脚本与证书哈希，上一轮及更早冻结报告、原始 PDF 保持原样，并检查本轮所有本地链接。没有新无理性结论，没有新 Lean 形式化，没有候选参数扫描。

