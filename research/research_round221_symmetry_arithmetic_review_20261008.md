# 第221轮奇偶商算术稿：独立 FULL 审阅收据

2026-10-08。审阅者：round218_lambert_carrier；目标作者为另一 agent round218_packet_audit。结论：**PASS，限于最终冻结稿所声称的函数身份、完整系数分母、合法算术类型与费用区间。** 不把作者复读称为独审，不确认尚未证明的解析 gate 或新数值无理性。

## 1. 最终身份与实际阅读

实际 FULL 阅读目标 [cyclotomic_symmetry_arithmetic_round221_20261008.md](cyclotomic_symmetry_arithmetic_round221_20261008.md) 的全部七节、P1–P17、表格和运行范围。最终冻结身份为 **13880 bytes**，SHA256 **`ec00ff4c6dd4d76b61d1093234e0525a4d164ffdc66d34ac37c4fcda1e56c28e`**。

先前13814-byte版本也实际 FULL 阅读；审阅提出的唯一必要边界澄清已由作者修订：§4 下界论证排除有限素数集 \(p\mid6c_g\)。取外层 \(M=3p\) 时 p=3 会提供 depth2、总 depth4，因此不能套“外层 depth1、总 depth3”的句子。排除它不改变任何线性主项。修订后本审阅者对最终保存文件再次 FULL 读取，并重新核 SHA256；没有改目标文件。

本轮已实际 FULL 读取冻结220输入八节，18626 bytes、SHA256 `93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42`。这是函数和费用的共同输入；没有重新宣称 FULL 阅读其所有文献。

## 2. 身份、全部素数幂与完整多项式源

独立确认 P1–P5 的换元方向、两投影导数、平方规范、初值、系数及 \((2\theta_t+1)o=2\theta_te-g\)。目标关系确实在所指定初始 branches 补 \(x=\pm1\)、t=1。P6 的 residue 证明支付完整双悬挂的 C(x)-秩五；规范和基域包含关系支付 C(t)-秩五、两个四行投影的秩四，不依赖待证的 G 无理性。

\(q_M\) 正好去除 \(d_M\) 的2-primary部分；其余每个奇素数幂均保留，\(\log q_M=M+o(M)\)，没有“只取奇数所以成本减半”。

P8 的偶包支付所有幂：对奇 p 两个窗给上界3h或3h−1；在2处 \(H_n\) 是2整，固定 \(c_g\) 支付 g，显式整行倍数2移去 e 的固定外层2，\(d_n\) 支付全部 \(v_2(n)\)。

P9–P10 的 odd outer-index lemma 正确。若 \(M<3p^h\) 且 \(v_p(M)=h\)，奇 M 只能是 \(p^h\)，内层 k<M 的 depth≤h−1；否则外层≤h−1、内层≤h。第三层 \(q_{\lfloor M/3\rfloor}\) 至少提供 h−1，因为 p≥3。所有分母都是奇数，p=2 没有隐藏成本；固定 \(c_g\) 支付 g 的所有有限素数分母。初始 M=1、n=0 亦成立。

P11 的乘数对各索引单调。完整源中 \(t^kf_i\) 的0至N输出只读更小索引，所以这些乘数清除所有多项式方向与完整 cutoff；不需要猜测截断取消或满秩。此结论是系数 source 清分母，不是有限jet单射或 endpoint 数值行列式估计。

## 3. 最小 prefix 分母主项

P12 的 \(\operatorname{Den}_a=q_{2N+1}\)、\(\operatorname{Den}_b=q_{2N+1}^2\) 为精确身份；分子是±1，因此每个奇素数幂不会消失。与固定非零整体倍数和 literal \(n^e\) 比较时，取 \(n=(p-1)/2\)、p 不除该倍数，确实保留 p-depth2。这个比较不容许把2n+1免费登记为 n。

P13 下界的 \(n=p\) 在 \(p\le N\) 给深度三；在 \(N<p\le2N-1\)，\(n=(p+1)/2\) 给深度二。内层每次只有一个 p 项，\(p\nmid6c_g\)，所以固定 g 和其他项不能相消该最低 valuation。结合 P8 上界、PNT 得 \(\log\operatorname{Den}_{2c_ge}=5N+o(N)\)。

P14 下界对 \(p\le(2N+1)/3\) 取外层3p，内层只有奇倍数 p，给深度三；对其余至2N−1的 p，取 \(n=(p+1)/2\)，外层p+2为p-unit，给深度二。p=3 已由修订排除。P10 给 \(\log q_{2N+1}^2+\log q_{\lfloor(2N+1)/3\rfloor}=(14/3)N+o(N)\) 的上界，恰与 prime 下界相合。高次 prime powers 已由上界支付，确定主项的下界只需 primes；有限排除集贡献 o(N)。

完整五行共同 prefix 分母仍有5N主项，因为含偶行。这些精确逐行主项不等于最优联合格指数或最优 CDT 费用；原稿对这个范围的区分正确。

## 4. CDT 表、任意数组与坐标费用

逐项核算得到偶四行费用61/16；literal n 的7/16必须计入，不能只用27/8。奇四行实际三列宽度2、2、2/3给 \(\tau_t=11/3\)，节省7/48；原 x 奇源宽度1、1、1/3给 \(\tau_x=11/6\)，节省7/96。平方商将该同源类型全部加倍，收益来自 odd outer-index lemma。

完整五行的普通安全 cap 为106/25。原稿正确拒绝用 row sums 将 \(d_n\) 偷换为 \(d_{\lfloor2n/3\rfloor}d_{\lfloor n/3\rfloor}\)：二者会遗漏 \(p\in(2n/3,n]\)。

独立实际读取 CDT fixed-v2 printed pages122–123 的完整 Theorem8.0.1、(8.0.2) balanced/discrepancy定义及 Remark8.0.6。对 P16 的真实非-staircase数组，前两列上界分别48/25、42/25。第三列计数上界

\[
C(s)=\min\{2/5,(1-s)_+,1/5+(1-3s/2)_+\}
\]

确有原稿列出的四段，纸面积分给 \(2\int C=3/5\)，因此总上界21/5。逐列最优未假定同时实现。两大列按类别顺序可同时实现18/5，第三列非负，故确有 \(18/5\le\tau_{\flat\flat}\le21/5\)。不把上界当成失败所需下界；不冒称 sharp值。固定 cutoff shifts 的每列误差至多2ε，有限初始项统一缩放后取极限合法。

P17 仅使用 arbitrary-array theorem 的算术定义，没有将其解析 numerator 偷换成普通 theorem。是否有共同实际图及严格 holonomy quotient 仍须另证。

§6 的有理缩放账本亦正确：\(t=\kappa v\)、既约分母B0需要安全全jet因子 \(B0^N\)，同时图导数除以κ；整数缩放可能消除的 dyadic prefix 部分仅 O(logN)，不能变成免费线性收益。完整系数 cutoff 与源列规范始终保留。

## 5. Primary 和执行 scope

使用 [CDT fixed v2](https://arxiv.org/pdf/2408.15403v2) 的本地冻结文件，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771` 已由本审阅者重核。本轮新增实际 primary 读取仅为 printed122–123选页；fixed-shift Remark6.0.12 printed67及68开头已在本轮解析稿工作中实际读过。未声称 FULL 阅读218页文献、未用短稿替换它；没有新增下载。

数学程序、CAS、prime/parameter scans、数值积分、PSLQ、Lean、Git均为0。一次 pdftotext 仅提取现有PDF的指定 documentary 页，不是数学程序。工具只读全文、取metadata/SHA256并写本 NEW receipt。保存后将对本收据实际 FULL 作者复读；该收据作者复读与对另一作者目标的独立 FULL 审阅分开登记。旧数学文件、main、manifest未改。
