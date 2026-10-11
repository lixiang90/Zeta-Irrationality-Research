# 第241轮完整分布与块证书独审

2026-10-09，B。PASS，无必要数学修正。本人没有运行数学程序、扫描素数、构建 Lean 或重跑本轮唯一固定矩阵核验。

实际 FULL 读取最终 Root 稿 [logistic_prime_edge_full_certificate_round241_20261008.md](logistic_prime_edge_full_certificate_round241_20261008.md)：9100 bytes，SHA256 57e591ba89c52556066ec502c8dbb9d5bc81521cbecfaa18bc0d793fd433c665。不是依据 Root 的 author receipt 声称读取；本次工具输出包含全部五节及全部公式(1)–(13)，并包含同类余因子与 \(w_b\) 不依赖 \(i,k\) 的最后补充。

重点独立纸核如下：

- \(V_r\) 的 pole 值是 \((r+1)!H_j^{(r+2)}\)，与真实 logistic \(B\circ\partial^r\) 和外部 \(1/24\) 一致。多项式分布由 Bernoulli 生成函数及链式因子精确支付；商部乘近分母后仍小于截断次数。
- 近盘完整调和头的 \(p\) 倍数部分精确取消，全部远盘先乘近分母再截断的差由式(5)控制。分母损失至多一阶，故单极点误差至少 \(-1\)；全残数估值至少 \(\beta+1\)，所以完整误差至少 \(\beta\)。不漏 \(j>p\) 或多项式商部。
- 对整个 \(t\phi_a\phi_cD_n^4\) 的零阶数重算，得到 \(c'=(-7,-5,-4)\)。同簇自身主块有统一单位权，异盘和异簇至少高一阶/半阶；\(\beta\ge\rho_a+\rho_c+4\)，所以完整误差与参数项分别高至少4、5阶。
- 三个固定块的归一化是 derivative-only \(V_3\)，外部为 \(w_b/24\)，并非沿用原 \(K_3\) 常数。本人实际 FULL 读本轮固定 producer3992 bytes/SHA881a02e507ca7505c877f3f57d64ab8412363491355810bee660fe59ef8bd8fe 和 JSON1921 bytes/SHA42c02ce2ead856b0787b892ff3bd10b4b502cd5947ee27bd61d5022e707ef590；没有执行。固定常数由首一除法、全部残数和矩阵消元核验，不是 prime 采样证明。
- 完整 CRT 变换 determinant 为单位；在二次局部扩张中的半阶缩放合法，最终 determinant 系数仍在 \(\mathbb Q_p\)。权和 \(5-9p\)、参数系数 \(5k\) 余量、primitive 常数约化、每个固定有理 \(q\) 的无界非零，以及归一化 auxiliary 费用 \(3p-5\) 均一致。

本次 primary 范围是本人已保存并 FULL 读的选定 pinned Lean 文本及第240轮完整泛函稿，详见 [packet_reading_scope.md](../literature/logistic_prime_edge_round241_20261008/packet_reading_scope.md)。未 FULL 读整个仓库或所有 imports，未宣称 Lean 内核认证。PASS 的数值范围仅是该固定源、\(n=p-1\) 和固定有限坏素数之外的非零证书；全素数净费用、完整实处认证和新数值无理性仍未支付。Root 稿和全部旧文件均未修改。
