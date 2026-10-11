# 第228轮 rank-one period Gram cap 独立审阅

2026-10-08，B；数学程序0。结论：PASS，最终稿无需数学修正。

本人实际 FULL 读取 [目标最终稿](global_rank_one_period_gram_cap_round228_20261008.md) 五节/式(1)–(8)：6706 bytes，SHA256 cf61f9183615c38fea1c0e574045ff1c0c125745ab1e98dab29990ac1290555e。此前实际 FULL 读初版6700 bytes/SHA6da11d4af79379c76955023826796a787f089b322f8860d50a7ddfe266ffa12a，建议§5普通Q句补绝对值及D=0边界；最终已改为 |vP/K| 与 (D+1)^(−4)。本人重新完整读最终保存文件，没有编辑目标。

独立纸核的关键链：

1. t=x³测度准确为 (−log t)t^(−2/3)/[9(1+t^(1/3)+t^(2/3))]dt，支配(1−t)dt/27。每个 moment 是 L−h_{3j}；对任意有理多项式基，L coefficient是 b bᵀ，b_i=p_i(1)。正 Gram 非零并非有限实例。
2. P=det M·K>0 与 Q/P=L−1/K 来自 matrix determinant lemma。包含常数1给予 K≥1/L；任意 degree≤D 子空间嵌入完整 degree≤D 多项式空间，故只需上界后者的评价范数。
3. Rodrigues q_j 的首项、端点值及j次分部积分边界逐项核过。t=0消去阶j，t=1消去阶j+1，全部边界为0；范数 1/[2(j+1)B_j²] 正确。有限维 Cauchy给 Σ2(j+1)³=(D+1)²(D+2)²/2；无需未读 Christoffel 渐近。
4. 两嵌入是 √3M 与 −√3M+2cbbᵀ。精确 Norm(F(c))/Norm(a)=c²−3(Q/P)²=6L/K−3/K²>0；下界(5)以及任意完整 polynomial scalar clearing 的非零最高系数整数范数≥1，直接给(6)。这是必要 coefficient 条件，不是把 safe LCM 当最优指标下界。
5. Monomial exact rate 的 Chebyshev首一变基/Hadamard上界、权重1−t Gram下界与 B_j≤2^(2j+1) 均正确，给 log det M/N²→−log4、log P/N²同率；Norm清分母必须支付至少2log4的率。

量词通过：任意包含1的有理多项式空间，D随N至多多项式增长；完整 uF(C)系数整性；允许代数unit、最优scalar content及与C无关的可逆行列变换。固定 c分母另付不破坏下界。χ−4/χ−8普通周期移位核确为正，变数后也支配正数倍(1−t)，所以该**相同结构**扩展合法。

停止结论仅为严格 N² 余量不存在，不是全数值方法 no-go。特殊关系点另付 cancellation、另一完整源、真正多period消元与不含1的源未被论证覆盖；primitive最高系数次主阶高度也未被排除或证明。目标最终稿清楚保留这些边界。

这是一份新数学稿独审；本人没有借目标作者scope冒称重新 FULL读CDT、repo或其余primary全文。新文献阅读范围另见 [B228 scope](../literature/global_review_sources_round228_20261008/packet_reading_scope.md)。该短收据保存后本人再 actual FULL复读并登记最终bytes/SHA；无扫描、CAS、PSLQ或producer重跑。
