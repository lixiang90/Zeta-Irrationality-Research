# 显式相对链与 Mellin 候选：本轮独立审阅记录

日期：2026-10-04。审阅者：paper_mechanism。本稿冻结所列范围的只读数学审阅结论；不修改被审原稿，不给 ζ(7) 或 Catalan 常数的无理性结论。

## 1. 根分支高阶对数矩候选：本人审 §§1–4，通过

对象：[odd_zeta_log_moment_candidate_20261004.md](E:/kimi-build/zeta5/research/odd_zeta_log_moment_candidate_20261004.md)。最终核对 SHA256：

`f00c2b6f95844c8949350eb51968abda08b6904efce8687dcd4ab33845322f15`。

逐点核过 Mellin 有理函数在所有 `z=−r` 的留数、无多项式部分、`z=1,...,n` 的 q 阶零与全部指定 log 矩消元，以及 degree≤qn 范围的唯一性。纯 ζ(7) 的真实余数系数与安全整数化身份成立。另独立重算 `(n,q)=(1,6)` 的七个整数系数、`B=725200` 及有理常数，吻合。

必须保留的范围区别是：`q=6` 只消 log 次数 0 至 5，不能消掉 ζ(7) 核中的 log⁶；`q≥k` 才能用完整有限几何展开得到式 (4.2) 的尾项身份。本人建议将后者条件写在式前，作者已补。安全估计 `|I_k|≤B/(n+1)^k` 不给小值；其右端指数增长也不能证明实际积分增长。该候选的实际非零、绝对衰减指数、最小共同分母与完整系数 gcd 仍未证明。整数 polynomial 的常数系数为 1 不等于最终线性型本原。

## 2. 二项式 cyclotomic Mellin 族：本人审 §§4–6，通过

对象：[odd_zeta_cyclotomic_mellin_20261004.md](E:/kimi-build/zeta5/research/odd_zeta_cyclotomic_mellin_20261004.md)。最终核对 SHA256：

`9a2c843c9de0ff30c5790aff827869abd27b3e0681dc4ec1ccdd5fab1db6638e`。

实际有理常数写成 `r/M` 后，逐素数的 `gcd(M,r)=1` 确保完整线性型 content 被 `D₀|BC|` 控制；包括 `r=0` 时 `M=1` 的边界情形。一般引理需要 `B,C` 非零；本人指出原措辞未显写 `C≠0`，作者已补，既有应用无变化。

严格 prime windows 中的所有 p 倍数分母均落在已认证的低 quotient 区域，`p²>D` 及固定有理 partial sum 的有限坏素数处理正确。纯 beta 使用奇数交错 partial sum；纯 zeta 必须从 `h≥2` 的偶数 partial sum 开始，不能使用 h=1。窗口互不交与 PNT 给的是实际最小分母下界，结合完整 gcd 才得到实际本原预算。分段公式连续，`a/b≥4` 的导数与起点正下界均通过。其失败结论严格限于文中指定固定二项式纯目标族，不能推广至任意带符号滤波。

根任务另独立审了该稿 §§4–8，包括 parity 与 Legendre 论证并确认通过；该更广范围是根任务审阅，不冒充本人的独立复核范围。

## 3. 普通 Rodrigues 族：本人审 §§3–4，通过

对象：[odd_zeta_relative_family_audit_20261004.md](E:/kimi-build/zeta5/research/odd_zeta_relative_family_audit_20261004.md)。最终范围措辞修订后核对 SHA256：

`a732cc05e14fbe3a98bf591f48658410c0fff1ac7c1fb3d5e53097a837a46e19`。

整数展开、普通矩消元、严格完全单调核与全部分部积分边界项正确，因此实际纯目标积分非零不依赖目标无理性。Stirling 导数身份的最低项准确抵消新增的 `u^n`；非负上下界与 beta/Laplace 估计给固定 `A,k` 下准确指数 `−ρ_A`。Catalan 半幂 kernel 的导数卷积只增加次指数因子，指数相同。

文中安全倍率后的正值发散有严格证明；这仍不是实际本原 content 的全族障碍。根任务另外复核了该稿分析及归一化下界，本人不将其列为独立审过的 §§3–4 以外结论。最终 §8 已准确说明：显式链仅参数 `ρ,c` 降到有理 conic 商，四个 Bloch arguments 一般仍在 `K(C)`，整条链不能称为 genus-zero chain。

## 4. 本轮显式链交付及交叉核验

本人新报告 [odd_zeta_explicit_steinberg_20261004.md](E:/kimi-build/zeta5/research/odd_zeta_explicit_steinberg_20261004.md) 的核对 SHA256 为 `07a4224bdcaef15776bd8552258acd0aea6204819f12097e8706ae2938220736`。它给出四项实际链 `δε₀=w`、函数域 Milnor K₂ 中整系数 `T=0`、八个明确 five-term 关系的有理端点身份，以及沿真实路径的复原函数与全部分支常数。配套固定精确证书通过 45 项检查，无参数扫描、无目标小数值测试。根任务独立核过整系数 Steinberg 简化、具体整数端点的平方条件、five-term 消去及复原函数两端常数，通过。

整数与有理范围需保留：具体域含 `√2`，使整数端点中的 `(-1)⊗2` 为零；一般域不享有该结论。有理端点等式 `β=−4[i]` 不自动升级为无扭的整数等式。旧 transfer 报告的 `4T=0` 仍正确，已由本轮直接整系数 `T=0` 加强。以上均为函数域/相对端点结论，不自动产生随 degree 指数增长的有用 content。

## 5. 冻结后可继续的问题

下一研究所需的新命题已经具体化：对 q≥7 对数矩族证明实际端点值非零，并估计其绝对指数及实际分母/content；或对普通 Rodrigues 族证明实际 content 的全尺度节省或障碍。有限小例、消元唯一性、固定安全倍率、形式动机投影均不能代替其中任一项。本轮所审身份与已证明预算可作为基线；没有新的无理性定理。
