# 第282轮任务 · 导子为8的 Markov 逼近的完整分母

2026-11-20。依据[281复盘](global_source_review_round281.md)，限一完成轮，只检验以下带边矩阵的算术。始终取 \(L=L(2,\chi_{-8})\)，反证包括所有既约 \(L=u/v\)，\(u\in\mathbb Z,\ v>0\)。

对 \(s\ge1\)，固定 \(\mu_j=(4j+1)^{-2}+(4j+3)^{-2}\)，\(b_i=\mu_i,\ K_{ij}=\mu_{i+j}+\mu_{i+j+1}\)，指标 \(0\le i,j<s\)。设 \(\Lambda_s=\operatorname{lcm}(1,3,\ldots,8s-1)^2,\ A=\Lambda_s K,\ w=\Lambda_s b\)，令
\[
H=\Lambda_s\det A,\qquad N=w^t\operatorname{adj}(A)w,\qquad
r_s=N/H,\qquad c_s=H/\gcd(H,N).
\]
同一 \(E_s=L-r_s>0\) 的裸率已为 \(-\eta=-2\log(3+2\sqrt2)\)。严格出口需要固定 \(\delta>0\) 和一个预定无界子列上 \(\log c_s\le(\eta-\delta)s\)，从而反证下的正整数 \(vc_sE_s\) 趋零。[全矩阵来源及变分证明](full_net_gate_round281.md) · [独立复核](markov_candidate_audit_round281.md)

**首命题。** 将已有平方 Cauchy 子式扩到 \(N,H\) 两者，核其全部共同因子能否给出上述线性界。先找精确的两坐标表示，再检验可证明的共同整除，特别是步长4在分母全奇时对两侧差分的作用。分别给出约分后可证的上界及尚需的内容。用有限例子核符号和索引时，只用来决定通式是否须改。

**停止条件。** 若仅得到未知行列式或 permanent 之比，或清整后的可靠上界仍为二次或 \(s\log s\) 量级，本窗口到期关闭。只有改善同一原整数对的完整上界才能登记预算进展。无论改善与否，到期后先比较其他路线，未达到严格线性门槛不得宣布无理性。另一来源的内容、扩大规模或素数扫描均不延长本窗口。
