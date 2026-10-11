# 平衡测度、配对整格与辅助素数接口：root 独立审阅

日期：2026-10-06。NEW 独立纸面审阅。本文核三份同行新证明；root 自己的 Plücker 稿由 quarter 另独审，不在这里冒充独立自审。root 本轮数学 producer 执行0；全部旧及同行 producer 执行、import、重跑0，外部 Lean0。

## J1. 实际读取的最终对象和范围

1. `research/cdt_odd_paired_head_free_integral_lattice_20261006.md`：最终 SHA **5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b**。实际全文读取 I1–I25，无截断。最初候选 a763 的 I1–I22 先全文读；新增 I23–I25 后补读，再对已将 LP 范围修为 sqrt(8n)<p≤6n 的最终稿全文重读。历史候选不作为最终批准版。
2. `research/cdt_odd_restored_zero_equilibrium_energy_20261006.md`：SHA **264cc3fce8d8417e04e3aea8963010b0f8804c2014692d4a64827c774454f0e6**。实际全文 E1–E35 无截断；独立推导 one-charge potential、质量条件与归一化，逐项核 E26–E32 的积分及消项。另静态全文读取 NEW rational-log PY，SHA **8aabd288de14fa1b0c72fd72a4b9568ec610b9e22af7ea205de472c8b88e7804**，JSON **ef3fc4a69593411eb6ae10b680f4b406a22c823c54a5182043e45fd03b339d66** 只读其方法、范围、18 checks、窗口和 metadata，不宣称重新运行或逐项人工展开巨大的 Fraction 输出。
3. `research/cdt_odd_paired_head_free_auxiliary_prime_20261006.md`：最终 SHA **4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b**。实际全文 A1–A13 读取候选 bb4eeb14，作者只在未冻稿 A11 增补 source D^(2n) 两处 O(n) 费用、A12 明示 probe r 对应 a=−r,b=1；root 实际补读最终 A11–A13。其纸面算式全部独核，NEW finite-probe JSON 只读 scope 和 ten-case metadata，代码的全文静态独审由 toric 另完成。

本轮实际原页：Brown arXiv2604.20741v1 PDF1–10/21–24 共14页，Saff arXiv1010.3760v1 PDF32–36 共5页，Monien arXiv0901.1883v1 PDF1–6 共6页，已归档 Lai PDF23–25 共3页。root 总计本轮实际原页28，三份新PDF归档82页不称全文82页独验。Brown 初次组合输出中间曾截断，5–8另完整补读；PDF抽取的GBK失败不算读取。正文输入的实际独立证明与原页阅读范围分别记录，不把同行读取算作root读取。

## J2. 真实整数基和 finite-place 桥

连续节点的 Newton evaluation 前2n矩阵 triangular diagonal1，cardinal basis 是同一整数值格的 GL(Z) 变换。各 pair 约束除去真实 gcd 后互不相交且 surjective；I8 的 G_m 与高 Newton kernel 正好给整个饱和格。raw pair 基的指数是 ∏g_m，原始阶乘费用至少6n²logn；但同一 Gram 也相应乘其平方，故不能把饱和的 scalar 更换宣称成净余量。

I15 的准确 Newton covolume 由 primitive row/kernel exterior Hodge star 成立，I16 evaluation inner product 由 Vandermonde 恒等式成立。I13 upper fee 的系数18log2−6log3和 I19 在另一个规范下的系数112log2+18log3−49log7独立核准；其范数不能混用。I20只给任意整数基至少一列高度障碍，未偷换成总 n² 费用下界。

I23 的两次 Cauchy–Binet 只传递 actual 2n-minors 的 common bound；I24 需要 largest2n factorial terms n,…,3n−1。I25 限于 sqrt(8n)<p≤6n，避免 p>N 时不存在 residue nodes 的 q_ρ=−1 进入公式；小prime和p>6n另证完整整化。因此新稿的全 finite-place 安全接口通过，但还没有 cheap signed Gauss 主率或目标无限非零。

## J3. 平衡测度确实给全 n，而非形式 saddle

one-charge density E9 具有 half mass；其 resolvent 在 ±iu 的 poles 消掉，jump 与无穷项确定全部 normalization。正混合使 mass 为3(√(4+R²)−2)−(√(L²+R²)−L)。与 d=L−6 相等时恰有 √(L²+R²)=3√(4+R²)，因此 R²=(L²−36)/8，没有第二个合法root。

在cut外 E14 的全部 integrals 为正，直接给全实轴 Euler–Lagrange 不等式；不依赖 V 全局凸。E17保留 tail defect 并证 Q≤2(L+1)，E18给有界密度。regularized log kernel 的 mass-zero Fourier energy为负，ε=1/n 控制 empirical diagonal；E22 的 self-energy 为 hlogn，正则误差仅 O(n)。将 tail defect 真正积分后，E24 付清 uniform R、固定cot kernel、无限域和 normalization，故是所有n≥1的严格 bound。

闭式检查：one-charge on-cut potential 等于半个 point-charge log potential 减去其 Green constant 和 arcsine constant；这与 E26 的 Fourier 积分一致。对 mass family E'(r)=ℓm'，积分得到 E29，保留 ∫m²/r。E30–E31 的 primitive 用直接求导核准；C=3A 时 A/C logs 恰抵消，先得 β=dV0+d²log(2d/R)−3d²/2−5T+6J_{2,L}，再化为 E32。最后的−d²与 normalization −3d²/2 均不是遗漏。

NEW PY 的 atanh-log tail 方向、负系数 endpoint 反转和2幂缩放正确，整数窗口是该 closed constant 的有理证书。它不证明全 n theorem；全 n 来自上述纸面论证。β严格改善旧 y*=1 tangent，但仍不足以超过现有 safe A。Jensen E34 与 regularized upper 给固定正包络的精确 n² energy；这个 sharp model 不等于 actual complex determinant 的 lower bound，更不能宣称整个方法 no-go。

## J4. 配对的实际 first jet 与两个 matrix gates

辅助 p=9m+1>2 必使m偶数。去唯一p后 positive d_z/p 是unit，constraints局部满射，basis无隐藏index。负 evaluation kernel是 AQ，Q反射even、degree<3m，dim3m/2，故 image E 的实际dim为5m/2。E的 annihilator 由 head barycentric rows degT<m 及 finite residues 得到；T反射even，所以 dim m/2。

W=K S³/A'² 与 v_T=T A'/(K S⁴) 给 orthogonal-complement Gram=K^−1 G0，因此 detG0≠0 等价 strong restriction 非退化。shared roots I 的degree m−1，head harmonic reflection给 I'/I；actual paired lift 含 p(A/I)I'Q/2，shared节点 E/p= j/2 而不是0。模p² constraints 后可用 split surjection 修成 exact paired lift。

weak-leading 独立手核：k=s−(s+1)η，d_s=(1−k²)/(s+1)。whole Taylor/source/head/W errors 在 strong-weak 为 O(p²)，weak-weak 为 O(p³)，不进入 leading coefficients。以强块作 integral Schur，weak 为

\[
\frac{uK}{s+1}(H_0-C_sG_0^{-1}C_s^{\mathsf T}).
\]

故两显式 finite-field determinants detG0 与 detM_s 同时为unit时，实际 saturated restriction 的 Smith为 (−s)^{5m/2},(−(s−2))^{3m/2}，whole polynomial Gauss为−m(4s−3)，leading reduction为非零常数。其独立于a/X的范围和固定分母例外都正确。

此 theorem 保留两个条件；尚未证明它们在无限辅助素数同时满足。五p、两source的十个 exact cases与模型吻合，不能抹去该hypothesis。单个auxiliary-p费用也只有 O(nlogn)，没有 n² 主率结论。A30–A31的 full-complement 加 middle correction 反射身份正确，不能丢弃middle。

## J5. 审阅结论和剩余目标

上述三份同行新证明在明确范围通过。root 自己的配对解析稿由 quarter 的 NEW 独审，SHA **5b9b5ff67c7aeaea6be24a03a8d9734e15c404aa56dec5c9a577c34ca2ca5d3e**，实际全文只读核准；它建立同一格的 generalized Vandermonde/positive Gram upper bound和 weighted Plücker接口，不提供 actual nonzero。恢复四重零点与配对原布局是两个对象，不能交叉借用便宜费用或衰减。

本轮正面进展是真实平衡能量的改进与固定正包络阈值、完整饱和格、准确 first-jet/block 条件、同一对象的全 finite-place/解析接口。仍缺 paired 两矩阵的无限unit证明、各实际 minor的匹配解析主率、足够便宜的 signed content与最终严格净余量。没有新的 ζ/L/Catalan数值无理性、线性无关性、外部Lean或完整外部论文kernel重验证。本审仅冻结自己的 NEW 文件；历史输入不改，来源和执行 pins 另保存。
