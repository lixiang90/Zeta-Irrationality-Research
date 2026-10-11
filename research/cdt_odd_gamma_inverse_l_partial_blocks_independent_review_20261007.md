# 实际 inverse-L 整模型与完整、残余素数块：独立审阅

2026-10-07，审阅者 /root，作者 /root/source_pencil_finalize。结论：**PASS，限于稿中明示的假设与范围**。这是一份纸上独立复核，不是 Lean 验证，也不证明任何新的数值无理性。

## 1. 完整阅读对象与冻结边界

本人实际全文阅读 `research/cdt_odd_gamma_inverse_l_partial_blocks_20261007.md` 的全部七节及 B1–B23；受审候选 SHA256 为 `ac4ac0bf9886ebe1d7f48c0c0dff91c5e643c8fb7be7e69d0ca98f3e477ee204`，15582 bytes。本轮重新读取完整文件后逐式复核，未要求数学改动。

authority 是 `research/cdt_odd_delivery_relative_lift_tensor_reference_20261007.json`，SHA256 `61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd`。既有596条记录只读；本人已重新核对全部记录的 SHA/bytes，并全文阅读五个 guard，未执行它们。原始 paired source 仍为 ξ=αζ(4)+βζ(5)，β≠0；本稿的 ζ(5) inverse-L 校准不自动替代该 source。

本轮独立复核使用固定 CDT PDF66–69 四页以及 Guillera1908.05123v1 PDF3–4、17 三页，均为实际全文读取；另目读已保存的 PDF17 rendering。这七个不同 PDF 页是本人当前轮实际阅读，未继承作者或其他代理页数。未创建、运行、导入或重跑数学 producer，未计算新素数表，未执行 Lean。

## 2. 全指标整模型、指数率与前缀包络

B1 保留原 forcing 的 N、A、P 和实际 inverse-L 系数。B4 的证明逐素数幂比较 factorial carry：当 q≤n 且 q|m，C_q(m)=0；q≤n 且不整除 m 时 C_q(m)≤9；q>n 时 carry 在所需区间单调。这准确支付每一有限处，包括 N 与 A 的小素数，因而 NΓ_n b_n 的整性是全部 n 的结论。

B6 的额外 carry 仅在 n<q≤5n 出现。高素数幂总贡献为 o(n)，首层分拆给137/12，Stirling 给 log h_n/n→logΛ。故 B5 的率245/12−10log2−5log5正确。本文没有将它称为真实 b_n 最小分母的率。

B8 两向均通过：Γ_k|D_n^9；对每个 p≤n 取 k=p^e≤n，则全部 p^j≤k 的 carry 为零，恢复9e。故本显式上界序列的前缀 LCM 恰为 D_n^9。该结论准确阻止直接把逐项率γ填成 CDT 固定 array 的费用；它不声称真实系数的最小前缀分母也必然等于 D_n^9。

## 3. 单层 stripped factorial 与完整块反转

B9 在 a,b<p 下逐块使用 Wilson，范围充分。B10 的高位与低位符号相消；所需 h_q、(2q+1) 与 binomial 因子在5q+e<p下均为单位。

B11 的高位 factorial 比值为 h_l l^9/160，低位比值为160/(h_k k^9)。低位 Wilson 符号为正，高位 stripped factorial 留下负号；(lp−k)^9 的负号在第二等式中恰好抵消。两个显示等式均通过，并只适用于稿中第一层范围，不被提升为 prime-power supercongruence。

B13 完整块的幸存项是 lp 以及 lp−k（1≤k≤d）。P(lp−k)约化为 P(−k)，所以权重全部留在 S_p，外面的 U_q 确实是不带 P(l) 的 reciprocal sum。稿中明确区分 U_q 与 b_q，避免了错误的低指标递推。

## 4. 残余块、边界与条件的精确强度

B14–B15 包含所有幸存的残余项。残余非空强制 C=9 和 q+1≤d，因此没有在允许的 q=d 边界逆取 h_{d+1}。B16 的结论为 min(0,C−8)，而非无条件 C−8；这是关键边界。

B17 首块 prefactor 在 p>31 时是单位，故 S_p=0 与所述 valuation 增益等价。B18 用 n=lp−1、T=S_p−30 和 h_1=30·128，直接得到显示的 −A^l/128。S_p=0 时它仍是非零 p-unit。这个边界否定残余块自动全消失，但不反对 cap8，因为该指标原本 p整。

固定有理 u 的 homogeneous subtraction 在相应 normalized leading residue 上带 p^9；除有限分母素数外不改变这些模 p 身份。稿中对此的范围正确。

## 5. 条件 H 到全部 n、固定 width array

H/B20 是尚未证明的输入。B21 对 p>√(5n) 用单层抵消，较小 p 保留旧 cap 并由 D_floor√(5n)^3 支付高层；3floor(a/2)≥a 对 a≥2 成立。有限 bad primes 与有限初始 n 由固定 M 支付，所有 prime 与指标均有覆盖。

B22 对每个固定 ε>0 先取足够大的 n。a=1、2 时一层平方充分，a≥3 时 ceil(a/2)/a≤2/3，故 D_floorεn^2 支付完整缺口。小 n 再以固定 Mε 支付。证明没有令 ε 随 n 变化。

B23 先缩放整个实际函数包，后使用八列 width1 和两列 widthε；第一行为常数，其他行共同激活，e_i=0。其成本 (8+2ε)(1−m^-2) 以及 ε↓0 的 bound 极限，符合 CDT 有限初始缩放及连续性范围。它没有错误地宣称已经取得 D_n^8 的精确全指标 cap。

## 6. 原件核对与尚未解决之处

Guillera PDF17 Table5 第三项的九个参数、z0 和 P(−k) 与稿中一致；PDF3–4 的陈述是 conjectural supercongruence pattern，不能把同参数表格视为 H 的证明。只在模 p 中把截断延长到长度 p 是合理的，不能据此领取模 p^9 或高素数幂反转。

CDT PDF66–69 支持所用 admissibility、array 成本、固定缩放和连续性接口。其 window denominator 提示也与 B8 的审慎范围一致。

## 7. 最终判定与下轮接口

**PASS：** B4–B8 的全指标 carry 模型、B10–B19 的实际完整及残余块身份，以及明确以 H 为前提的 B21–B23 均通过独立纸证复核。没有发现需要修改候选的数学错误。

H、进一步高阶抵消、实际最小分母和新的数值无理性仍未取得。当前叶子共有的 μ 对数解析限制另由本轮 algebraic-reference 稿处理；本审阅不将 Γ_n 的较小逐项率或条件 cap8 解释成已经越过该几何门槛。该报告是一次固定候选的单向审阅记录，不引用未来交付审计，也不包含 receipt 循环。
