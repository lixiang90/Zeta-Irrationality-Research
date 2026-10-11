# Root234实际读取范围

2026-10-08。本轮复用已有原件，新增PDF下载0、数学程序0、参数扫描0、Git操作0、Lean构建0。

## 原文选页

当前220页作者版CDT原件为 literature/global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf，3628820 B，SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c，来源 https://math.uchicago.edu/~fcale/papers/L2chi.pdf。

Root实际FULL读取并保存当前物理PDF16–17页和34页选文：root_current_cdt_pdf16_17.txt（7437 B）与root_current_cdt_pdf34.txt（3180 B）。另实际FULL读C保存的当前PDF25页选文 dual_cdt_current_pdf25.txt（3773 B），核对Theorem2.8.4与Conjecture2.8.1的范围。这里FULL仅指这些完整选页，不指220页全文。固定218页v2的四项陈述与当前220页的三项陈述分别登记，不猜测版本变动原因。

Root实际读取DLMF19.4、19.7中完整椭圆积分的导数与Legendre关系的选定公式，来源 https://dlmf.nist.gov/19.4 与 https://dlmf.nist.gov/19.7；记录见root_dlmf_elliptic_selected.md。未读整个DLMF章节。全图容量公式是Root由这些公式自行推导，已显式区分modulus k和参数x=k²。

## 本轮数学稿和审阅

Root已实际FULL读以下最终全文，并直接核对证明：

- truncated_rational_source_exact_lcd_round234_20261008.md：6081 B / 255c474af62a9d85f15b67b2932e652b0676dcef50830f03e8aa45274aec87bf。
- truncated_meromorphic_all_map_cap_round234_20261008.md：4408 B / 9211d4ccf424ede0cf1fe94def12191c0747c5e364da7c723dd4b797ce73e390；最终补入展开中的加号后已再次FULL读。
- truncated_rational_source_rank_leaf_gate_round234_20261008.md：9707 B / 2c7bb29c41b935159a9f9ad8d97107dbcd3173d436777895e8461651e14c5b8f。
- truncated_rational_pullback_integral_flags_round234_20261008.md：9529 B / ca350ab2f584583fe0146684afb112867280d73dc92b44036037945051dc2f03。
- truncated_fixed_basis_denominator_floor_round234_20261008.md：6484 B / eea286f00d9c9168558519f753079d0e5de96d0a06cf8eec960b0b7333d936d2。
- truncated_target_primary_coverage_round234_20261008.md：4756 B / 187aa8288531b182978c13b8ce2c7fe15fd4f7366241c7b22cbd6e3a0d0d10a7。

Root也实际FULL读取A、B、C各自最终reading_scope，范围分别以其文件为准；代理的原文FULL读取不冒作Root自己的原文FULL。A已独立FULL核读Root最终两数学稿，B独立支付固定换基下界；Root直接复核了两者。

## 历史输入与限制

Root实际FULL读233规范化稿、233报告、233 manifest；没有运行旧producer/archive，没有全文重审既有主日志。本轮末为选择下一方向，仅选读既有低成本polylog报告开头至第6节开头，不称全文认证。C另作既有相关稿的限定段落核对，其消息仅用于方向选择。

本轮证明限定固定u坐标、固定有理g、完整三维源的固定Q(u)换基和basic CDT数组。没有证明随尺度联合整格的最优性，没有认证所有更强CDT判据，没有宣称新数值定理或目标的全球新颖性。仓库状态只继承232轮已核证据，本轮未重新同步或远端核对。新增文件身份在234 manifest中一次记录。
