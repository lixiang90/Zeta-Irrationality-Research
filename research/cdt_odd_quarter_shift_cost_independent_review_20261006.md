# 四分之一移位 restricted 费用与原格信用的独立审阅

日期：2026-10-06。审阅者 quarter_model_review；这是另建的 NEW 成本审阅记录，先前[模型/packet 审阅稿](cdt_odd_quarter_shift_independent_review_20261006.md)保持冻结。未执行或 import 数学 producer。

实际阅读全文 [新 Smith 稿](cdt_odd_quarter_shift_smith_20261006.md) §§1–6、[冻结 balanced 桥](cdt_odd_level20_balanced_smith_bridge_20261006.md) §§1–7；另实际提取并读取 [CDT 固定原件](../literature/cdt2024_l2_chi_minus3.pdf) PDF122–124、129–131、140–143。原件中实际核对 (8.0.2) 的 maximum、(8.2.2)/(8.2.6) 的同一 source/HS、(8.2.28) 的 arch 项，以及 (8.2.30)–(8.2.34) 的逐 prime finite height 主项。此范围没有覆盖新未阅完整 F 的 packet，也不包括改变 arch metric 的其它变体。

## 1. restricted LCM 表与剩余地方

Q10 的 split 首层及高层被四个 Δ⁺_(⌊bn⌋) 清，其中 b=4+ε，ε>0 固定，Δ⁺_M=∏_(p≡1(4))p^⌊log_pM⌋。因为 bn≥4n+1 对全部充分大 n 成立，有限初项用固定整数 D₀ 处理。

inert 部分的所有 p²ʲ 层只涉及 p≤√(4N+1)。粗计每个 prime 的全部层数≤O(logN)，prime 数量≤O(√N)，每层 logp≤O(logN)，即足够得到统一前缀清分母的 log 为 O(√N log²N)。split j≥2 层也有同样界。Euler derivatives 仅乘整数，不增分母；n=0 项整。原 source 的 shifted coefficient indices 均≤N_D=5D+O(1)，所以该统一整数确实同时清全部所需 evaluation entries。

即使把这个额外整数逐 source column/graded evaluation 全额付费，一变量 rank O(D) 时费用≤O(D√D log²D)=o(D²)。fixed tensor dimension d 时，每个 tensor coefficient 至多付 d 倍；rank q=O(Dᵈ)，累计增加 O(dDᵈ√D log²D)=o(Dᵈ⁺¹)。这在原规定先 D→∞、后 d→∞ 的次序中消失。有限 D₀ 同理只加 O(dDᵈ)，也是小项。p=2 的 coefficient、Euler derivative 和整数 polynomial source 本来都整，故 dyadic contribution 为0，不是漏记一个主项。

restricted 表没有被当作 CDT 已陈述定理的普通 LCM 类型。原 PDF141 的 (8.2.30) 是逐 p 分母估计，(8.2.31) 对稀少 bad-degree tuples 的粗界在限制 prime 子集后仍成立；其 (8.2.33) 的大 prime 主项在 p≡1(4) 上由 AP prime number theorem 重做。因为所有权函数在有限个线性区间上连续分段，partial summation 给 ∑_(p≡1(4))F(p/N)logp~(N/2)∫F。于是原 maximum transport 的主项恰乘1/2，而上段已经付清其余 primes 与高幂。此为受限逐 prime height 推广，所需 source、HS 和 arch 估计均未改变。

## 2. 精确 maximum 与两种变量的归一化

五个 species 中 constant 占1/5，其四列 b 都为0；四个 positive species 总质量4/5，各有四列同一个 b。normalized coefficient degree u=n/N 在[0,1]均匀。固定 threshold t=p/N 时，可成功 degree 质量为 (1−t/b)₊，可成功 species 质量为4/5。四列同时 active，故 payoff≤4min(4/5,(1−t/b)₊)。

把 constant species 配到 u∈[0,1/5]，positive species等分 u∈[1/5,1]，就在所有 thresholds 同时达到该上界。有限 tensor 的 rounding、species tolerance、degree discrepancy 误差在原极限内消失。因此 S11 确为 maximum：

\[
M_b(t)=4\min(4/5,(1-t/b)_+).
\]

它在 0≤t≤b/5 为16/5，然后线性降到 t=b 的0。积分给

\[
\tau_b=2\int_0^bM_b(t)dt=96b/25,
\qquad \tau_b^{\rm split}=48b/25.
\]

此处 t=p/N，N~5D。all-active 条件 t≤b/5 等价于 p≤bD；不能把它误读为 p≤bD/5。S13 的积分另用 t=p/D，其信用窗口为 p≤2D 和 p≤2D/3，两窗口均严格在 bD 中（b>4）。这两个变量分别来自原 denominator transport 与 polynomial relation degree loss，转换一致。

## 3. 同原格 baseline 与 tensor 信用

同一五函数原整数 polynomial source E_D 的 rank R=5(D+1)。对 good split p，p⁴eval 整；constant 的 D+1 个方向有 floor4，其余四行只用 safety floor0。两层 packet 原格关系给 capped floor 和≥4(D+1)+k₁+k₂，其中 k₁=3(D−(p−1)/2+1)₊、k₂=2(D−3(p−1)/2+1)₊，cap4。

没有额外 Smith 收益时，这个 pure matrix 的 net per-coordinate height baseline 为

\[
4-\frac{4(D+1)}{5(D+1)}=16/5,
\]

恰等于上节 p≤bD 中原 restricted transport 在该 prime 的 all-active payoff。prime 是否 split 决定该项是否出现，但不改变单 prime 的16/5。故可在同一窗口把实际 floor 信用从原 finite bound 中扣除；没有从不同格、不同 degree 窗口的费用中任意减一个 kernel 维数。

独立确认 DVR restriction 引理：tensor SNF 每个 certified floor≤4d；对各整数 threshold ℓ≤4d，floor≥ℓ 的基方向张成 saturated submodule，交 balanced primitive source rank 至少 h_ℓ−c，因而其任意可逆 square row minor 至少有 (h_ℓ−c)₊ 个 exponents≥ℓ。累加给下界 dRᵈ⁻¹Σβᵢ−4dc。balanced coordinate source 的 c/Rᵈ→0，actual leading tuples 在 V_Dᵈ 中，故这是 actual graded determinant 信用而非新全局 scaled basis。

所有信用只在严格 p≤(2−δ)D 内窗使用并最后 δ↓0。为同时清 restricted 列与 packet，取 p²>bN_D；删去的小 primes 最多付 O(D√D log²D)=o(D²) 新信用。constant floor 和 transport 的 species/discrepancy 误差在固定 margin、依次取 D、tensor、tolerance 极限后消失。

AP-PNT 与 partial summation 给

\[
\sum_{p\equiv1(4)}(k_1+k_2)\log p
=\gamma D^2+o(D^2),\quad
\gamma=\frac12\left[3\int_0^2(1-t/2)dt
+2\int_0^{2/3}(1-3t/2)dt\right]=11/6.
\]

tensor floor 信用除原主阶 d·5ᵈDᵈ⁺¹ 后为 γ/5。密度1/2只计了一次；split baseline 也已经乘过1/2，不会再将信用减半。

## 4. HS/arch 移项与准确结论

实际读取原 PDF130 的 (8.2.6) 给 source normalized degree J_φ/2；PDF140 的 (8.2.28) 在 ordinary metric、无 subradius correction 时给 −5ρ/2+J_φ；PDF142 的 (8.2.34) 给 finite 主项 5τ_split/2。上節的实际 determinant 信用将最后一项变成 5τ_split/2−γ/5。斜率不等式因而是

\[
J_\phi/2\le-5\rho/2+J_\phi+5\tau_{\rm split}/2-\gamma/5.
\]

乘2移项，得到

\[
5(\rho-\kappa_\varepsilon)\le J_\phi,
\quad \kappa_\varepsilon=
\frac{48(4+\varepsilon)}{25}-\frac{2(11/6)}{25}
=\frac{48(4+\varepsilon)}{25}-\frac{11}{75}.
\]

所以 κ_(0+)=192/25−11/75=113/15 正确，作为给定 native-x source/ordinary metric 的可认证 finite 成本上界。全文没有证明它是最优或必要下界。原 omit1/unique simple0 类 ρ≤log16<3，而本 κ>7，因此这一具体输入不产生 CDT 数值矛盾；它不能据此排除其它整格、信用、周期消除或解析叶。

## 5. 通过范围及执行记录

通过：S10 restricted 整模型及全部其它 finite places 的低阶费用；S11/S12 exact maximum 与其 split 推广；S9 到 balanced actual determinant 的同原格接合；S13 AP-PNT 信用；S14 ordinary HS/arch 归一化。§§1–3 的 packet 与 primitive counts 与先前实际独审一致，新的 S6 快慢表示也实际核对，不必靠有限 producer 才得出此结论。

没有执行、import 或修改任何数学 producer；没有用有限样本替代 full-prefix、AP-PNT、DVR 或 tensor 极限论证；未读取新 producer/JSON，故不报告其检查次数或通过状态。没有新数值无理性定理或 Lean 验证。本稿保存为本轮额外独审证据，原数学 producer 的后续执行由根任务独立记录。
