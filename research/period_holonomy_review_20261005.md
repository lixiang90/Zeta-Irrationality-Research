# 本轮独立审阅记录

日期：2026-10-05。审阅对象为本轮四份技术稿及总览；旧报告没有改写。以下通过指明确的数学论证与范围检查，不等于 Lean 形式化，不替代已引用的 CDT 定理。精确证书支持符号实现及固定实例，通用结论依据正文证明。

## 1. CDT 机制与实际五项转移

[报告](period_holonomy_cdt_mechanism_20261005.md) SHA-256：
27483fbfe9d54e0e2bbe982d6959da4586bd9e7490bbb2b64c5c6301e3478299。

根代理独立读 §§2–5，核两变量实五项微分/零边界、正参数映射、邻接严格阈值、A/H 卷积整数公式、真实 Hadamard 有理化、trace 系数倍增及六积分账本、17 行主成本与严格余量。通过。distribution 另只读审 §2 的真实五项身份与阈值，通过。

原文 Lemma 14.3.1、Corollary 9.0.19、fine 积分成本最小化及 Appendix A.6 的 J<10，明确作为外部已证输入采用。未冒称本项目的 120 项有限核验重新证明它们。固定 v2 的局部显示问题已按真实定义/微分方程解决，不由此扩大评价原主定理。

## 2. 六分点、Lerch 与周期系数系统

[报告](period_holonomy_target_projection_20261005.md) SHA-256：
36281c471fc0c4013b943222f1e8ab9f8a736e6c69fa63ab87422f120ffc5837。

根代理独立读 §§2–7，核六残数坐标、递推有理边界、数值分类依赖 Theorem A、SNF 与饱和核、非单射投影的完整 content、随参数增长的新素数、实际 cyclic rank 2t+1、原空间 local monodromy 核、共同前缀整格与 coarse holonomy 失败的限定范围。新增 §5.1 的跨模数/权重秩 s+1、真实覆盖选行、mean-zero 取消 1 分支，以及同时纯 L/删分支的饱和核与 L/4 像均独立核过。通过。

paper_mechanism 另只读审旧 §§5–7、§4 primitive 缩放/content 及新增 (26a)，通过；未将其审核范围扩大为新增 §5.1。这里的 uniform 低微分秩不自动具有同秩 Betti 有理商。

## 3. 三级整数正例与 fine 类型

[报告](period_holonomy_integral_models_20261005.md) SHA-256：
b8d4199f6a3b1b97d59481a87157be85652a431b00d444ba04600797b0a9ab1d。

根代理独立读全文，核实际秩 3、明确三列整数 Betti 格与负实路径 monodromy、几何坏支持 {3}、两次 blowup 的完整 chart、regular/SNC 与非 reduced fiber 的区分、整三角正逆变换、全部前缀精确分母、p+1 序号类型障碍，以及自然基最优成本两边同为 25/18。通过。

paper_mechanism 另审 §§2–6 及实际秩/常数剪切/−1 所有支障碍；distribution 另审 §§4–6；均通过。坏 3 全局整 logarithmic 延拓没有构造，作者明确保留该缺口。曲面 regular 性与原点分母控制不被替换成全素数晶体格。

## 4. 五项完整来源、秩 6 商与真实指数

[报告](period_holonomy_dilog_model_20261005.md) SHA-256：
970191f95813c6f14ce45da71b1af2070fdfa000f28168a7d8ff89fa3b34d9be。

作者根代理给出全文证明及 117 项精确核验。moment 独立审 §§4–5 与后增秩 6 有理 de Rham 整下降、六个实际独立芽、Frobenius 全尺度分母指数；paper_mechanism 另审 §§1–6 的核心数学，均通过。

专门核到最小 D=N(N+1)^2(N+2)，不能额外除以 gcd(N,2)。N=2 的固定 lcm 边界例独立认证。十个差值及评价因子列出全部标记碰撞支持；未把清 D 当作几何全部坏支持。

rank3 de Rham projection 的复核 8 维，对指定 rank11 Betti 有理来源只有 5 维核，且该核的有理 de Rham/整比较确相容，得到完整 rank6 quotient。来源、分支、指数矩阵和 primitive 稳定核全部明示。没有声称所有实现最低秩 6，也没有将 Betti 秩下界直接代入 CDT 的实际函数参数。

全部内容公式与固定 N 的单行/6行/11行公共前缀指数均核。证明单行指数时仅排固定 T1 的有限素数，p|D 的近尾序号另处理；O_N 常数不能当成 N 随截断变化的统一常数。公共分母指数没有冒充 fine 参数 τ。

## 5. 总览中的实际积分分类

[总览](period_holonomy_progress_20261005.md) 的 (8)–(10) 由实际绝对收敛级数逐项积分，映到完整 (1,ζ2,L2χ−3) 基，再使用已证 Theorem A。额外精确证书核纯 L 正积分、值 1 的正积分、混合积分与零周期积分，并保留有理平移坐标。证明适用于任意有理多项式 P，不靠四个实例推断一般无理性。

总览中五项 Li2 推论、trigamma/积分分类均标明是 CDT 定理的后果。新的结构引理为项目内直接证明，未宣称全球首次性。尚未得到新导子 L 值、ζ7 或 Catalan 无理性，也未新增 Lean 形式化。

## 6. 原件、证书与冻结范围

本轮两份原始 PDF 已检查签名、解析页数、SHA-256、首页渲染身份；新增 220 页作者快照未替换固定 218 页 v2。三份官方 HTML 保留原字节与来源。
[阅读地图](../literature/period_holonomy_reading_map_20261005.md) 记录实际用途。

[交付脚本](period_holonomy_delivery_20261005.py) 检查：
四技术稿与总览的五份精确证书、四稿固定散列及本审阅所引散列、
此前链式冻结的 36 份报告及此前脚本/证书、
此前本阶段归档的 64 份原始 PDF、
新增两份 234 页 PDF、三份 HTML 与全部当前本地链接。
审计执行结果见 [JSON](period_holonomy_delivery_20261005.json)。

