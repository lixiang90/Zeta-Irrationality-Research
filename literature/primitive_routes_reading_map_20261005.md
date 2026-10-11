# 本原分母与路线去重：2026-10-05 文献阅读图

本轮新增五份原始 PDF（97 页）及三份原始 HTML。PDF 均核标题、作者、版本标记、页数与 SHA-256，且实际查看了首页；未修改任何旧原件。见[PDF 清单](manifest_primitive_routes_20261005.json)、[网页清单](manifest_primitive_routes_web_20261005.json)及[来源配置](primitive_routes_sources_20261005.json)。

## 1. 有限域块和：哪些文献真正适用

- **John Greene, 1987**，[原件](greene1987_hypergeometric_finite_fields_author.pdf)，Transactions AMS 301, 77–101，作者站点 25 页。Definition 3.10 以乘法特征定义有限域超几何函数。本项目 \(C_{n,p}\) 是 \(\mathbb F_p\)-值的 Pochhammer 截断；必须另证二者的具体桥接，不能仅因都叫 hypergeometric 就套 character-sum 估计。[作者原件链接](https://www.d.umn.edu/~jgreene/papers/Hypergeometric_Trans.pdf)
- **Amit Ghosh–Kenneth Ward, 2016 v2**，[历史原件](ghosh_ward2016_truncated_hypergeometric_v2_withdrawn.pdf)，41 页，arXiv 1601.06765v2。**该论文后续在 2020-04-23 v4 撤稿**；原始 metadata 的 Comments 记录“Errors in paper uncorrected.”，且 v4 没有 PDF。保留[撤稿网页原始 HTML](ghosh_ward_arxiv_v4_metadata_20261005.html)用于版本审计，**本轮未采用其任何定理**。即使只看旧版的命题范围，其主要对象也是固定参数、变化 argument 的低阶截断，而此处变化的是 \(n\) 参数、argument 固定为 \(-1\)，并不匹配。[v2 metadata](https://arxiv.org/abs/1601.06765v2)，[v4 撤稿记录](https://arxiv.org/abs/1601.06765v4)

本轮[异常素数稿](../research/odd_zeta_exceptional_primes_20261005.md)中的反射分类、常数项表达及条件双计数均独立推导，不依赖撤稿论文。欲用有限域几何，仍须证明实际 index polynomial 的非退化结构及 root-count 界。

## 2. Lucas 与 Dwork：Newton 多面体的实际检查

- **Armin Straub, 2025 v1**，[原件](straub2025_partial_lucas_v1.pdf)，15 页。arXiv v1 时间 2025-11-03，正文作者日期 2025-11-02，分别记录。Theorem 1.2 给 Laurent 常数项序列的 partial Lucas 条件；本项目的 Newton cube 是 \([-1,7]^7\)，允许的低位区只覆盖 \(b<p/7\)，没有覆盖所需 \(n<p\le7n\) 窗口。[固定版本](https://arxiv.org/abs/2511.01174v1)
- **Kira Samol–Duco van Straten, 2009 v1**，[原件](samol_vanstraten2009_dwork_reflexive_v1.pdf)，14 页。Dwork congruence 输入中“唯一内点格点”条件不能删去；本项目 cube 有 \(7^7\) 个内点格点，不是其直接适用对象。新的实际全尺度 Dwork 系统仍需构造，不能从“可写成常数项”自动推出。[固定版本](https://arxiv.org/abs/0911.0797v1)

精确常数项、partial-digit 匹配与 full Lucas 的固定反例均在异常素数稿及其有理证书；不将有限反例升级为所有 Dwork 变体均不可能。

## 3. 真正混合 Padé 的已知参照

- **V. N. Sorokin, 1994**，[English 原件](sorokin1994_nikishin_zeta3_english.pdf)，Russian Mathematical Surveys 49:2, 176–177，2 页，DOI 10.1070/RM1994v049n02ABEH002229。文中给实际混合 Nikishin 的 ζ(3) 逼近、余项及三变量积分；其构造可作为改变余项来源的参照，但定理不能直接推广到 ζ(7)。[期刊 metadata](https://www.mathnet.ru/php/archive.phtml?jrnid=rm&option_lang=eng&paperid=1187&wshow=paper)
- 继续使用库内冻结的 [Smet–Van Assche 作者稿](smet_vanassche2008_mellin_author.pdf) §§2.3、3–5 与 [Wolfs 2024 v2](wolfs2024_multiple_orthogonal_hypergeometric_v2.pdf)。前者用于核 Mellin/type-I/type-II 对偶身份；后者的 \(p<q\) 整性余量不自动支付当前 \(p=q\) polylog 情形。

本轮[Padé 稿](../research/odd_zeta_mixed_pade_20261005.md)明确区分：端点约束 type-I 与旧 type-II 归一化完全相同；单最高对数权的普通正交输入则确实不同，并有平方余项正性，但其真实分母与 content 指数尚需证明。

## 4. 固定滤波器任意阶展开的标准分析输入

[固定滤波器稿](../research/odd_zeta_fixed_shift_filters_20261005.md)补齐任意固定阶局部渐近，再使用共轭谱及代数消去。
保存 [NIST DLMF §2.4 原始 HTML](dlmf_2_4_saddle_20261005.html)与 [§5.11 原始 HTML](dlmf_5_11_stirling_20261005.html)，对应[非退化内点鞍点展开 2.4.15](https://dlmf.nist.gov/2.4.E15)及[Gamma 展开与余项](https://dlmf.nist.gov/5.11)。
这些来源仅支持标准展开工具；实际围道、分支、主峰和离散 Poisson 求和步骤由项目证明逐一核实。

