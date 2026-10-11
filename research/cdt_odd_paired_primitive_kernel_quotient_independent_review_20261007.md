# 原始 primitive 核商稿的独立全文审查

2026-10-07，NEW，审查者 `/root/source_pencil_finalize`。被审稿为 [primitive kernel quotient K1–K18](cdt_odd_paired_primitive_kernel_quotient_20261007.md)，作者稳定候选 SHA `996e261e7fd780f5247b0736380c0bb581e637fedb624de52982793ee8bb6f5b`。本人实际完整读取八节正文，没有以摘要代替全文。本轮数学 producer 创建、执行、import、rerun 均为0，辅助 prime 扩展0；564冻结旧记录仅读。

结论：纸面审查 **PASS**，没有请求修改。通过的是实际有理核商、精确外幂/首次 jet 恒等式及其有条件同对象矛盾接口，不是新特殊值无理性结论。

## 1. 完整核格、商判别量与首次 jet

K1 的核格是饱和整数子模，所以完整整数核基可扩成 unimodular U=[L,K]；这使商基的变换必属于 GL_d(Z)。故 K2 的 q=det(LᵀBL) 带符号且不依赖补基，不把任意有理补空间冒称完整整数商。

E=U^(−t) 的前 d 列为 primitive 整数矩阵，B=ECEᵀ。对 actual rank d 作 Cauchy–Binet，全部 d-minors准确为 q p_I p_J。E 的最大 minors gcd 为1，使这些产品 gcd 仍为1；因此 K3 的分式理想恰是 qZ。低于 actual rank 的外幂没有这个 rank-one 身份，主稿已严格保留此限制。

K5 可在 t≠0 用 kernel 块 tV_KK 消元，再用 polynomial identity 延至 t=0；S_V 正定、a_V=det(KᵀVK)>0，首次非零 coefficient 确为 q a_V。ν=0 时空 determinant 为1，所有公式仍成立。B=diag(1/2,0)、V=diag(1,2) 的反例准确说明：完整 pencil 的整系数不能自动除 a_V 给 q 整性，故 q 不继承 whole-X 40.3145 的模型。

## 2. 高度平方与复数商 Gram

令 G=UᵀU。它的 determinant 为1；逆矩阵的前 d-block 是 EᵀE，用 Schur 互补式得到 det(EᵀE)=det(KᵀK)。Cauchy–Binet给 Σ p_I²=𝔥(K)²。由于 p 为实整数向量，qppᵀ 的 operator 和 Frobenius norm 均准确为 |q|𝔥²。这不是旧 paired 格本身的 covolume，也不是任选高补基制造的额外收益。

P_ij=∫g_i overline(g_j)d|μ| 的 convention 对 complex column 变换 R 给 RᵀP overline(R)。K8 中取 A=P_KK^(−1)P_KL、Z=overline(A)，则 Zᵀ=P_LK P_KK^(−1)，完整展开 (L−KZ)ᵀP overline(L−KZ) 恰为 P_LL−P_LK P_KK^(−1)P_KL。删除这处 conjugation 一般会错；主稿保留了正确约定。BK=0 使同一 complex shear 下 bilinear C 不变，Andreief 的绝对值界适用这些 complex 线性组合。

因此 K9 的第一式 |q|≤detP/det(KᵀPK) 成立。将 K=QR、Q 实正交列分解后，Hermitian compression 的 eigenvalue interlacing 给 det(QᵀPQ) 至少为 P 最小 ν 个 eigenvalues 的乘积，det(R)²=𝔥²；后两项即准确跟随。主稿的 unimodular ambient shear 例子也确实同时改变 e_d(P) 与 𝔥，不能保留旧解析费却人为增高核高度。

## 3. 非零 phase 与真实费用

K10 与冻结 coupled C23 使用相同 P 和原 complex measure：T=P^(−1/2)B(P^(−1/2))ᵀ，||T||≤1、rankT=d。C_d(T) 的 operator norm 是非零 d 个 singular values 的乘积 Θ_d，不是已为0的全 detT。复矩阵 transpose 与原矩阵具有相同 singular values，故两侧 sqrtP 的 exterior norm 的乘积是 P 最大 d 个 eigenvalues 的乘积。结合准确 K7，即得 K11。正文没有把 fixed-size phase defect 或 O(n) 的 loss 冒称 n² 主率。

我实际全文读取冻结 [node N1–N17](cdt_odd_paired_partial_minor_node_budget_20261007.md)、[analytic A1–A27](cdt_odd_paired_compound_mixed_jet_analytic_20261007.md)、[partial P1–P14](cdt_odd_paired_partial_compound_transfer_20261007.md) 与 [coupled C1–C23](cdt_odd_paired_coupled_gram_decay_20261007.md)。首次组合输出在 analytic/partial 中截断，随后单独完整补读这两稿；不将截断当全文。

扩到 3n/2≤d≤2n 的 K12 合法：3n<p≤4n 时 u=p−2n>n，使 d<2u，−2 的 weight3-tail 不进入贪心；4n<p≤6n 时没有这种 tail，余下 head 的0槽有足够容量。真实二阶 node minor −(WU)²、全部非主子式的 block row/column 匹配和双 Cauchy–Binet证明均不依赖未知评价单位。p≤3n、p>6n 和 fixed rational denominators 沿完整原模型支付。

K13 的 gain 手积分检查如下：3<x<4 得 (λ−1)²；4<x<6 换 u=6−x，三段 gain 面积为 7λ²/6、λ²/4、λ²/4，总 5λ²/3。于是 A_rank=32λ−1−8λ²/3，λ=3/2 回到41、λ=2 给157/3。有限 u 的+1 仅造成 uniform O(1) 每 prime；有界分段 affine 族在 compact λ 区间的 PNT 转移可由有限网格与一致 Lipschitz 逼近证明，不依赖新 sampling 或执行。K15 再利用 gcd p_Ip_J=1，准确把全部 minors 的共同整化传给 q；固定(DM)^d费用为 O(n)。

## 4. 判据范围、文献与实际阅读证据

冻结 analytic A4 是全部 n≤d≤2n 的原 basis 界，因此适用于 adaptive actual d_n。K16 与 γ 的冻结全尺度 limit匹配；K18 的差值和两 endpoint 455/12−2γ、45−2γ 手算一致，且在 [3/2,2] 单调递增。K17 在无限适用子列的 strict liminf 条件与 K11/K15 给同一个 q 的整数–解析矛盾，量词正确。

但本文没有 actual η_n 或 ω_n 足够的 lower，ν=0 分支也不能强行提供 kernel height；这些限制已在正文说明。没有把 matrix rank 代入 CDT 独立函数数，没有换目标为 ζ(7)/Catalan，没有新的数值无理性、线性无关性或 Lean 定理。

本轮本人另实际完整文本读取 Zhang–Cheng 原件 [arXiv1707.05941v1](https://arxiv.org/abs/1707.05941v1)，[归档 PDF](../literature/cdt_paired_kernel_height_sources_20261007/zhang_cheng2017_efficient_bombieri_vaaler_arxiv1707_05941v1.pdf)，PDF1–7 全部七页，SHA `eb1ac14a228b64219dfef2814d430524fb6a7fa8846f6c92f4a27b033193656a`。Theorems1.3–1.4、2.4–2.7 与 §§2–3 区分 kernel covolume、minor gcd 和 small solutions upper；不会反推出本稿所需的大 height lower。文档提取的首次 GBK 输出未显示全文，改 UTF-8 后完整读完；这是 PDF 文本读取，不是数学 producer 执行，也没有运行该文算法。

本轮个人 primary PDF distinct 页数目前为11：固定 CDT v2 PDF66–69 四页，以及上述 Zhang–Cheng PDF1–7 七页；没有继承上轮 ICM/Borodin/长稿页域。此审查全文读后再由作者收审，最终单向来源另存；不 pin mutable 总稿、未来 audit 或未来 peer receipt。
