# R0 Kummer 全函数接口的独立限定审阅

日期：2026-10-06。审阅者 current_full_source。实际全文只读 research/cdt_odd_R0_kummer_period_interface_20261006.md；数学审阅限 §§2–6 及其引用的 R1–R4 定义，不认领 §7 新 PDF 的原件阅读。未执行或导入任何数学 producer；以下是独立手推，不是有限软件证书。

1. **真实 B/H 同一性通过。** H 的 n≥1 系数为 \(h_n=\pi^2\Gamma(n)^4/\Gamma(n+3/2)^4\)，B 的 n≥0 系数为 \(b_n=\pi^2\Gamma(n+1)^4/[16\Gamma(n+3/2)^4]\)、b0=1。因此 n⁴h_n=16b_n，准确给 \(B=1+\theta^4H/16\)。KB 的系数递推为 \((n+1/2)^4b_n=n^4b_{n-1}\)，首项 forcing1/16 通过。乘 √x 后 P4 的两项同时 shift θ→θ+1/2，故 \(P_4(\sqrt x B)=\sqrt x/16\)，未混用先前 Z4 的 constant forcing。

2. **beta period 与尺度通过。** 单积分 \(\int_0^1(1-u^2)^n du=\sqrt\pi\Gamma(n+1)/[2\Gamma(n+3/2)]\)，四次乘积恰为 b_n。正项 Tonelli 给实 x≤1，|x|<1 的一致几何级数给复参数公式。端点奇点1−A≥Σu_j²/4，四维径向 \(r^3/r^2\) 可积，因此 B1 是真实有限 rational-form period。Gamma/central-binomial 规范亦通过；只把 π²R0 称为 period，未把除 π² 自动放进 period 环。

3. **rank5/nonsplit 通过，依赖明确的冻结 P4 不可约输入。** KB 与 P4 的 rank1 Kummer twist 同构保持绝对不可约。0 的根−1/2、1 的根0,1,1,2、其它点 ordinary 均排 rational particular 的有限极点；polynomial 最高项产生 −(d+1)⁴a_d x^(d+1)，与 constant forcing 矛盾。θKB 的五阶 scalar operator是 \(\theta(\theta+1/2)^4-x(\theta+1)^5\)，为 regular-singular hypergeometric operator，故 single-valued global solution 的 moderate growth 给各 punctures meromorphic、继而 rational。扩张若 split 便有这样的 particular lift，已排除。非零 monodromy difference 在不可约四维 homogeneous 层中生成全层，加 B quotient 给最小秩5。没有将任意局部解析 particular 误判为 rational。

4. **local0 与平方 cover 比较通过。** θKB 的 exponents 为0及−1/2四重。唯一 Taylor particular B0=1 独立于 J4(−1) 齐次块；乘 √x 后准确为 J4(1)⊕(−1)。Z4 的 constant forcing 非零，在 MUM0 产生 log⁴ particular，故其 θP4 扩张为 J5(1)。x=u² 将 monodromy 平方：J4(1) 保持 Jordan length4，(−1)²=1，而 J5(1) 保持 length5。两者在该 cover 上仍不同构；不能据 endpoint relation 移植完整扩张。局部分裂与全局 nonsplit 相容。

5. **conifold obstruction 通过。** r_n=n^(−2)+O(n^(−3))，与 \((n+1)^{-2}\) 的差乘 n 绝对可和，所以 r−Li2/x 的一阶导数在1有有限实边界值。由 \((\operatorname{Li}_2(x)/x)'=-\log(1-x)/x^2-\operatorname{Li}_2(x)/x^2\)，得 r′=−log(1−x)+O(1) 与 r(1−t)=R0+t logt+O(t)，scaleπ²/16亦通过。这足以排任何仅减端点常数所得 holomorphic germ。结合 regular-singular Frobenius 展开也保留实际非零 log branch；本审阅没有计算其完整 Betti-cycle coefficient 或全部 conifold monodromy matrix。无需有理端点假设；该假设本身不会消 log branch。

限定结论：§§2–6 的全函数、period scale、rank/nonsplit、local0 comparison 与 conifold nonholomorphy 数学链通过。未独立重证冻结 Sp4 输入，未审核 §7 新文献中的具体 algebraic cycles，未构建 geometric normal function、integral Betti lattice、homogeneous conifold correction 或 CDT budget，也没有数值无理性/线性无关性结论。
