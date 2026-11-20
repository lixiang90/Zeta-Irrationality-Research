# 第281轮独审：\(L(2,\chi_{-8})\) 的正余项与既约分母

2026-11-20。审阅[竞争稿 F281.1–10](full_net_gate_round281.md)。取 \(L=L(2,\chi_{-8})\)，包括所有反证 \(L=u/v\)、\(u\in\mathbb Z\)、\(v>0\)、\((u,v)=1\)。本次核对的是指定有理数 \(r_s=b_s^tK_s^{-1}b_s\) 的净指数。若只得到 \(\det K_s\) 的因子，数值实施仍缺同一标量的既约分母。

**F281.1–2，旧双 Hahn 族。** 在该族任一预定无界子列，(278.3) 给出精确净率 \(\kappa-\liminf n^{-1}\log g_n\)，其中 \(\kappa=8+12\log2\)。P6b 的单支整除式给 \(\log\gcd(B,C)\le 2n+o(n)\)，奇 LCM 平方给 \(8n+o(n)\)，两个 \(b^3\) 合计 \(O(\log n)\)。所以指定乘积 \(\mathcal H_n\) 的率至多 12。由 \(g_n=\gcd(g_n,\mathcal H_n)h_n\)，严格负净率确实要求 \(\liminf n^{-1}\log h_n>12\log2-4\)。同一素数更高的幂也可贡献 \(h_n\)。此推导没有给出完整 \(g_n\) 的增长界。[278.1–3](wilson_square_budget_round278.md) · [P6a–P6b](wilson_primitive_round278.md)

**F281.3–7，Markov 族。** \(x^{4j}(1+x^2)(-1)^j\) 的系数依次给模八的四个奇数余类。乘 \(-\log x\) 后逐项积分，换元 \(u=x^4\)，得稿中的 \(d\mu\) 和 \(\mu_j=(4j+1)^{-2}+(4j+3)^{-2}\)。设 \(d\sigma=d\mu/(1+u)\)，对 \(\deg W<s\) 展开
\[
\int [1-(1+u)W]^2d\sigma=L-2b_s^tw+w^tK_sw .
\]
这里 \(w\) 是 \(W\) 的系数向量。正密度使 \(K_s\) 正定，极小值恰为 \(E_s=L-r_s>0\)，残差多项式在 \(-1\) 处为 1。极小残差对 \(1,u,\ldots,u^{s-1}\) 在 \(d\mu\) 下正交，故等于 \(P_s/P_s(-1)\)。这从同一泛函独立得到 F281.4–5。

上界的 Chebyshev 测试多项式给 \(E_s\le4L(3+2\sqrt2)^{-2s}\)。下界在 \(I=[\epsilon,1-\epsilon]\) 上取密度最小值 \(c_\epsilon>0\)，令 \(\ell=1-2\epsilon\)。对 \(I\) 上的正交 Legendre 基，\(-1\) 对应的坐标为 \(-3/\ell\)，点值平方之和至多 \((s+1)^2\rho_\epsilon^{2s}/\ell\)，其中 \(\rho_\epsilon=(3+\sqrt{9-\ell^2})/\ell\)。点值的 Cauchy–Schwarz 不等式给 \(E_s\ge c_\epsilon\ell(s+1)^{-2}\rho_\epsilon^{-2s}\)。先令 \(s\to\infty\)，再令 \(\epsilon\downarrow0\)，得 \(\log E_s/s\to-\eta\)，\(\eta=2\log(3+2\sqrt2)\)。若 \(r_s=a_s/c_s\) 既约，则反证下 \(vc_sE_s\) 是正整数。严格负线性净率等价于同一子列上 \(\limsup s^{-1}\log c_s<\eta\)；临界情形的次指数行为另待研究。

**F281.8，实际分母。** 最大矩下标 \(2s-1\) 的最大奇底数为 \(8s-1\)。取稿中的 \(\Lambda_s,A,w\)，有 \(r_s=w^t\operatorname{adj}(A)w/(\Lambda_s\det A)\)。一个固定尺度即可检验单靠矩项的 LCM 是否覆盖此标量。在 \(s=1\)，\(\mu_0=10/9,\ \mu_1=74/1225\)，故
\[
K_1=12916/11025,\qquad
r_1=\mu_0^2/K_1=\frac{30625}{9\cdot3229}.
\]
分子是 \(5^4 7^2\)，\(3229\) 与 \(2\cdot3\cdot5\cdot7\) 互素。这给出本目标的一个已约分反例，\(c_1\) 含 \(\Lambda_1=105^2\) 支撑之外的素因子。它仅判定“所有 \(s\) 都可只收矩项 LCM”的说法。对一般 \(s\)，矩有界、\(\log\Lambda_s=O(s)\)，Hadamard 给出的 \(\log c_s=O(s^2)\) 与严格线性门槛之间仍有缺口。

**F281.9–10，Borchardt 分解的范围。** \(D\) 的相邻偶、奇两行相同。指标递增时，其非零最大子式须略去一组，其余每组取一行。删去第 \(k\) 组后，前 \(k\) 行与余行分别形成单位对角的三角块，子式等于 1。故 Cauchy–Binet 产生恰 \((s+1)2^s\) 项。对每一项，递增节点的 Vandermonde 为正、所有和 \(x_i+y_j>0\)。重读原件首页 §1 式 (1)、(3) 与 permanent 定义，得到 F281.10 的符号和全部分母。这份分解的左侧是 \(\det K_s\)。它没有给出与 \(w^t\operatorname{adj}(A)w\) 的公因子或约分后的线性上界。现有证据支持一次完整分子、分母的来源核查；数值准入仍需上述严格余量。[Ishikawa–Kawamuko–Okada，首页](https://arxiv.org/pdf/math/0408364v3)
