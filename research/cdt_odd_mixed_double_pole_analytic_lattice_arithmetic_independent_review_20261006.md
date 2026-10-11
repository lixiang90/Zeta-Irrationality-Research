# 双极点解析与 primitive 格接口：算术代理独立审阅

日期：2026-10-06。审阅者 /root/conifold_arithmetic_hypothesis。NEW 独审；旧/同行 producer 执行、import、重跑均为 0，自有数学 producer 为 0。仅读取 MD/PDF/receipt 与 SHA。两份被审正文均实际全文阅读，并独立纸面核算下列范围。

## R1. 固定版本与实际阅读

1. research/cdt_odd_mixed_double_pole_analytic_decay_20261006.md，
   SHA256 c4e8f04f0debe34cf896780424e6ceb256747eaca0d3ed3b9698802757447218。
   实际全文 D1–D31、全部 scope 无截断阅读。
2. literature/manifest_cdt_odd_mixed_double_pole_analytic_decay_20261006.json，
   SHA256 3fa8dfa9dfdb0fd1cbcabc3ecd29def1a3f8b9402b127079fedfa8ca6eca0b25。
   实际全文读取；正文 pin、真实 16 页范围与执行 0 一致。
3. research/cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md，
   SHA256 93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8。
   初候选与 final 各实际全文读 P1–P9；final 明确 P16 仅为 raw 整数约束行，primitive/gcd/saturation 尚须核。

本人本轮实际全文读冻结 mixed H1–H9，SHA e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463；并实际全文读 Lai PDF1–25，SHA 838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，尤其 PDF7–11 的 minor/normalization 与 PDF17–22 的 contour/energy。没有把两位作者的阅读范围冒认为本人的范围，也没有把其参考文献视为已实际阅读。无新 PDF 下载。

自有冻结算术稿 research/cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md，SHA 452b9202ab3460f95e1ac5500092146cbe2ba0f9ed1e0a22bf5acb0a291fe985，是交叉比较对象而非本独审自我批准的替代。其来源 receipt SHA 6a78cda6cf7517cdf47a83548a7974a305dc561b46b99176d0cf8a325dfaaa88。本独审未执行或读取任何 peer producer 以替代纸面证明。

## R2. 完整左轮廓与 all-n 安全衰减

独核 D5–D7：q(z)=πcotπz 的 d 阶导数唯一 principal part 为 (−1)^d d!/(z−m)^(d+1)，故 residue 是 (−1)^d f^(d)(m)。K_s 各项负号与 clockwise 方向再次负号相消，左边向上的 Re z=1/2 积分准确包含全部正整数。s≥4 保证 kernel derivative≥1；竖直衰减与 deg(RP)≤−3 足以让剩余边界趋零。

独核半整数乘积 D8/D9：前 2n 个 factors 的净 exponent 是 +1/2，其余到 6n 的是 −1；Euler cosh 产品给 envelope≤e^(π|x|/2)。R_n(1/2) 的 u_m 表达与 1/(2m+1)≤u_m≤1 给精确 R_n(1/2)≤4，不用有限 n 拟合。

独核 D11 recurrence：若 q^(d)=q'π^(d−1)p_(d−1)(q/π)，用 q'=−(π²+q²)、q''=−2qq' 得 p_(k+1)=−2up_k−(1+u²)p_k'。在半整数竖线 q/π=−i tanh，得到正确固定常数，s5 的 C=128π²|a|+64π³|b| 通过。

独核 D15/D16：两个 generating functions 积分由 cos(arctan z+arctan w) 给 1/(1−zw)，leading coefficient 2^k/k!。Heine/reference change of variables的 exponent 是 h²；结果为 2^h(π/(2c))^(h²)，h=1 也核对为 π/c。带符号 actual measure 只用 absolute envelope，不假设正性。

因此全文的 |J_an|≤C^(3n)3^(−9n²) 对全部 n≥1 严格成立。这是实际完整解析泛函、固定 s 的安全界；不是 arbitrary rational X 的 determinant 无条件界，也没有证明该 exponent 最优。

## R3. crossing、exact rank 与 mixed Heine

独核 D18–D20 与 P13/P14 相符。R 在 m=1,…,2n 的 zero order 恰为 3，故 s5 second derivative vanishes、third derivative 是 R'''(m)P(m)。R''' 的 factorial 公式含 (−1)^m，且全部非零。

evaluation map Q[t]_<3n→Q^(2n) 满射；把 full-head 双线性形式写成 Eᵀ diag(d_m) E，d_m≠0，所以 rank 恰为 2n。该修正不能被“固定 derivative 只付固定 kernel 常数”的说法删除。

独核 mixed Heine D22：选择 k 个 distinct atoms 后的 coefficient为 binom(h,k)k!/h!=1/(h−k)!；重复 atom 被 Vandermonde 杀掉；atom-atom、continuous-continuous、mixed factors 都保留。因此每项至少 n 个 continuous variables，但另有 n² atom 与 mixed energy，不能由此继承31.614…。

## R4. 修复布局的 uniform G/β

独核 D24–D27 与算术稿的同一实际 R、h=(B−k)n 匹配。k=s−1 给最高 derivative k−1，全部 early zeros 消失，右轮廓是真正完整泛函。

独立整理 Stirling prefactor：分出产品的 n powers 后得到

\[
\frac{2B}{2^k}\pi^{1-k/2}n^{-1-k/2};
\]

numerator midpoint error 给 2^k n^(k/2)e^(k/2)，denominator endpoints给 1/[2(B+2)]。合并恰为

\[
\frac{B}{B+2}\pi^{1-k/2}e^{k/2+1/(6B)}/n.
\]

指数积分的常数项与 G 的 2B log B−2k log2 相符，没有遗失全 n uniform-in-x error。

独核 G''：numerator为
2[(B−k)y²−(B+2)((k+2)(B+2)−4)]。G' 从 kπ/2 下降至负 minimum，然后从负侧上升到0。因此任意 0<G'(y*)<2π 的 y* 给全半轴合法 tangent envelope，不能错误地要求整个 G concave。

exact reference integral 与 h=dn 给 β=d²log(2κ/π)−dc₁，符合 D30 的全部 scaling。B5、B6、B8 的 D31 exact 表达均正确，κ_B>69/28、2κ_B/π>69/44，三个 R_B>1 的整数比较通过，故三个 β_B 严格为正。

本独审没有算术费用优于这些 β 的证明。正 analytic β 不等于正 matched margin；没有沿用 Lai 的30.83或31.6。

## R5. 单目标 polynomial 与真实 normalization

P1/P2 的 a=−r,b=1,c=X 代入准确识别 ξ=ζ(s)−rζ(s−1)，不用额外 period identity。X-leading matrix为正 definite weighted evaluation Gram，故 polynomial degree准确 h。

P3 normalization invariance 严格：任意正有理 c_n 同时使 primitive multiplier缩为 d_n/c_n，log|C(ξ)|对应增加 log c_n，strict margin保持不变。完整空间同一 form 的 rational congruence只乘(det A_n)²；若要移除 apparent local denominators，必须保留其 index与archimedean factor。新增 subspace不属于这项整体因子不变性。

binomial lattice的真实 diagonal1/i! 与全部 factorial normalization一致；P4 的 auxiliary primes h<p 才使它 p-unimodular，不能一般化成全 p 免费。

## R6. 精确辅助素数 Smith/minor 与 primitive reduction

对 p=9m+1、q=3m、h=2q，未缩放 Hermite cardinal basis是 p-unimodular，scaled T 的 v_p(det T)=3q。P5 的 EE/EF/FF leading blocks准确；p>s+1 使 EE leading unit。B_EE^−1B_EF∈p Mat(Z_p)，可作 integral unimodular Schur elimination。

Schur FF leading coefficient为正的 uD/(s+1)，不是负号。由此确得 q 个 −s 与 q 个 −(s−2) Smith exponents，k 阶 minor ideal 等于 P8。该结论针对实际 specialization，也给全 X coefficients 的相应 Gauss determinant结论。

还原 T 后的 Gauss valuation为 −h(s−1)，scaled determinant mod p 是非零常数。global primitive scaling d_n必须在此 p 有 valuation h(s−1)，故 primitive polynomial mod p 仍是非零常数，避开任何固定 rational value分母后即有无限 nonzero evaluations。

单个 auxiliary p 的新增 s5费用3n是实际指数，不是 safe estimate；但其 log费用只有 O(n log n)，不能以此宣称全 p 的 n² 费用下界。

一般 k,B 的 auxiliary prime为 p=(B+k)m+1，q=(B−k)m。k>2 保证全部 tail W unit及 C leading2/p；还原 normalization 时 h<2p、v_p(∏i!²)=2(h−p)_+。P20与算术稿 A30a 的 −h(s−1)−2(h−p)_+ 完全一致。B>3k 的附加费用没有被删去。

## R7. paired head-free subspace与真实格缺口

P15 的 m↔2n+1−m 配对使 factorial numerator相同、sign相反。条件 P(m)/d_m=P(m')/d_m' 恰清除双线性 head 的每一对，并且 n 条独立条件给 dimension2n。它是 rank2n split form的 maximal isotropic部分加 n 维evaluation kernel，数学成立。

final93c9 的 P16 现在明确为尚未经 gcd 约除的整数约束行。取 primitive rows 与整个 saturation确是后续费用，不能把 raw系数直接叫 primitive。P17 的 first-pair ratio binom(8n,2n−1) 与 (16log2−6log3)n height 正确；该实际比率不会因逐行共同 gcd 改变，但它仍不是总 lattice determinant/index 的计算。

该 2n subspace 的 X-leading degree成立；无穷 rational nonzero、全 prime saturated格与相应 energy均未证明。full-space nondegeneracy不自动传给 restricted evaluation。

## R8. 审阅结论与边界

两个 final pins 的上述全部 scope 通过。解析稿提供完整 all-n bound、真实 crossing 与 corrected-layout β；格稿提供 actual target、primitive/infinite-nonzero机制、精确 auxiliary Smith/minor 与 general factorial费用；新 paired2n方向保留费用缺口。

本独审没有读或执行 root 本轮 LP producer/JSON 来验证一个 budget数值，也没有在此 review 中核准 root 的新的数值 certificate。它不含新的 ζ、L 或 Catalan 无理性、线性无关性或 Lean结论。

本 NEW review 保存后实际全文回读并冻结，旧证明与历史收据均不修改。
