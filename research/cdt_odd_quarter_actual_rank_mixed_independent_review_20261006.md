# 互补 quarter 实际秩与混合原格费用的 root 独立核读

日期：2026-10-06。本文是 NEW 审阅；不是作者稿的 producer certificate，也不是数值无理性定理。root 已实际全文读 [actual rank19 稿](cdt_odd_quarter_product_actual_rank19_20261006.md)、[mixed packet 稿](cdt_odd_quarter_product_mixed_packet_20261006.md)、其 NEW PY/JSON（只读），以及 rank 来源收据。原 quarter 真实函数、P4 的 Sp4 和非分裂、原19行闭包、balanced bridge 沿用此前实际核读的冻结证明，本轮不执行旧或同行数学 producer。

## Q1. 共同 PV radical 和 actual cyclic 19

独核结论：rank 稿的 R1–R12 成立。特别需要保留以下三个环节：

* 增广齐次 PV 群确为 Sp4×μ4。P4 的 connected dense monodromy 在 Kummer-character kernel 的 finite-index subgroup 上仍 dense；joint closure 因而不是被误缩为 diagonal graph。
* 两个 translation 模 χV、χ⁻¹V 在 full 群上不相同：Schur 后，(1,i) 的 i/−i 区分排除 intertwiners。只看 connected component 会错失这一点。任何 translation kernel 是 additive group 中的 linear invariant subspace；各 projection 不为零由全群 semisimplicity/cocycle 的 invariant lift 加实际无有理 particular 严证。因此 kernel 真为 Ga8，而不是从两个 separate non-split 扩张直接跳过 joint 条件。
* 八个 jets 在 K0 上代数独立后，Q 的 conjugates C-span 包含 Q、两组四个 homogeneous×particular directions、十个 homogeneous products。Sym²Sp4 标准模不可约且乘积 map 非零，所以最后十项独立。F、J 的代数独立区分其余九项。19维 **C-solution** 下界与既有19维 **C(x)-derivative** 闭包上界分别证明，再接合为 exact19。

无有理 particular 的证明对0、1、其它 ordinary finite points 先排 pole，再用 polynomial 最高 degree 排 constant forcing；F forcing 的转移加1/2准确。原九维系统的群还应除去中央 <(-I,-1)>；作者正确区分原群的两个 components 和 augmented 群的四个 components。

有限代数 cover 保留 G°（regular PV extension 与有限 Galois closure 的线性无交），故保留全部 Ga8 translations，仍有同一个19维 conjugate C-space。它不能把实际最小秩降到19以下。该结论没有分类 full analytic stabilizer，也没有把 PV 群里的任意复常数操作当成算术周期关系。

## Q2. 原四行的 second relations 确为次数2d

root 手工独推坏源 shifted packet：h±1/4=p/4，因此在 x^hT(x)W(x^p) 上，shifted θ 是 fast θ 加 p(θ_s+1/4)。一阶项多出 iθ^(i−1)T，正是作者 d_i。F 的 −1/2 correction 在 p⁴F modp² 中消失，但原19行 forcing没有被删去。

定义 e_i=θ^iT、d_i=θ^iV+iθ^(i−1)T，r_i 的 Q_T、C_i、D_i 是两行矩阵 minors；
\[
 Q_T e_i-C_iT-D_ie_1=0,
 \qquad Q_Td_i-C_iV-D_id_1=0.
\]
这是 exact polynomial cancellation，所有 coefficients≤2d，无需除 T。Q_T 顶项 T_d² 是 p-unit，给 r₂、r₃ 的 primitive count 2(D−2d+1)_+。first 三条仍为3(D−d+1)_+。

primitive 的有限 source-vector 论证使用 modp 独立及 DVR direct summand，未声称 polynomial-ring 换基可逆。L₂⊂L₁ 是真实 evaluation preimage 的嵌套；作者明确没有把 r_i 当作 degree-limited first-family span 的免费新行。这修正了一个容易造成重复信用的陷阱。

回到实际 J 原 Euler 格，固定 shifted→Euler upper-triangular 变换在 odd places 可逆，在2处只造成固定 degree-O(D) 常数费用。因此无条件 gamma_J=2、费用上界188/25正确，比冻结旧113/15改善1/75。

## Q3. 十个 mixed 行与全部 prime powers

对好向量G和坏向量U，Sym packet 是 (GU^t+UG^t)/2。first minors m_i 同时杀 fast e；m_i^tSym m_j 的六个 i,j≥1 relations 真实 modp 为零。second r_i 同时杀 e,d，给三个 i,j≥2 relations 真实 modp² 为零。好向量G无需 constant、fast 或 modulo-p² 的特殊表达。

其 source degrees 分别2d、4d，最高独有 coordinates 的 coefficients T²、Q_T² 都是 p-units。pure bad、Sym、constant/good supports 不交；每个阈值分别相加，没有在同一个 kernel 相加 first 和 second 两层。

精确乘积分母 D_A D_J=odd(D_(4N+1))⁴ 的 endpoint 情形独核通过：inert p 的 b⁻、b⁺ 若相差1，只能跨过4N+1；p≡3 mod4 因而 exponent 为偶数，所以 ceil(b⁻/2)+floor(b⁺/2)=b⁺。N=0单列，不在 log(−1) 上形式代入。这是全 prime-power prefix 等式，不只首负系数观察。

19 species 的 first-layer 费用数组每类prime均为五个零费、十四个四列费。maximum M_b=4min(14/19,(1−t/b)_+) 的积分给 τ=1344b/361。baseline20(D+1)、first/second counts 支持 p≤2D、D、D/2，都在五个零species的 matching window 内；cap4 与56/19纯原格 baseline匹配。归一方式保持原 near-balanced bridge：
\[
 \gamma_{19}=3+3+1+\tfrac34=\tfrac{31}{4},\qquad
 \frac{2\gamma_{19}}{19^2}=\frac{31}{722},
 \quad \kappa_{19,0+}=\frac{10721}{722}.
\]

Q1 的 actual19 现满足 mixed 稿明确保留的秩条件。对共同合法解析叶，actual independent derivative-closed rational system 的 Shidlovsky leading-order flag 与既有 CDT桥继续使用，故这个费用可作为该真实19行源的认证上界；没有声明最优。它仍不能形成数值矛盾。

## Q4. 执行记录与核读范围

root 实际只读 NEW mixed PY 与 JSON，核到脚本确为标准库独立实现、使用真实A/J有理系数、多block p²-prefix和完整矩阵 relations。JSON记录作者首次单次执行52项通过，七个(p,N)中有五个 multiple-block samples，N0..64分母乘积另验；root没有重跑，也没有把有限核验视为全素数或actual19证明。

rank 稿没有数学 producer。两篇作者稿的全尺度证明与本独审承担核心结论；有理端点 Q(1) 的旧投影没有在本轮重新认领首创。仍没有新的奇ζ、Catalan或L值数值无理性、线性无关性或 Lean 定理。
