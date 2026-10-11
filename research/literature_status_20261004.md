# 原始来源核查与一个普通极点轮廓构造

日期：2026-10-04。检索与计算完成于本轮。本记录没有证明 ζ(7) 或 θ=3ζ(3)+ζ(5) 无理，也没有新增 Lean 定理。

## 1. 当前证据的层次

**ζ(5) 的完成基线成立。** 原稿仍是 [Fauzan，Zenodo 22826419](https://zenodo.org/records/22826419)，2026-09-17 v1。页面最后修改于 2026-09-30，注明后续修订拟在 arXiv 维护；本轮未检索到作者的 arXiv 修订，不能把未检索到说成不存在。

[mo271/Zeta5](https://github.com/mo271/Zeta5) 当前提交为 `7fe736760f4b96bfdb4334b68e3b3124ecbe10b0`。README 明确声明完全证明，并记录三项标准公理。工具链已更新为 v4.34.0-rc1；[Comparator run 36345939791](https://github.com/mo271/Zeta5/actions/runs/36345939791) 为 Success。它将 Solution 与独立 Challenge 声明比较。本项目仍固定旧提交 `00c55bd` 与 v4.33.1；本轮没有升级依赖，也没有用网站状态冒充本地重建结果。

上游的正常化仍取 M=400、全秩损失，并以直接部分分式替代 Tate 代数。其负余量足够证明无理性，不代表原稿中的每一个速度常数均已形式化。另一个独立项目 [danromik/zeta5-irrationality](https://github.com/danromik/zeta5-irrationality/blob/main/README.md) 无 sorry，但显式保留素数定理公理。不能把两种公理范围写成一样。

**ζ(7) 的已审查版本没有新修复。** 直接查询 Zenodo API `/api/records/22920911/versions/latest`，仍返回 22920911，`is_last=true`，最后修改时间 2026-09-23T16:48:00Z。作者备注仍只提出指数数值修订。[原始记录](https://zenodo.org/records/22920911) 与本地 [审计](zenodo_22920911/review.md) 对应的 PDF 一致：p>K 时外区估值为零，但表 5 在 y=3/2 给出 −299/20，而定义给出 7/20。后续不能使用那个负外区积分。这个结论针对已保存的版本，不是对所有可能 ζ(7) 证明的否定。

**固定混合目标仍未解决。** 项目里 K=80 三方向族的全参数下界 [log P(θ)>20](zeta35_macaulay_analysis.md) 有精确证书；它排除指定射影平面族，并不排除所有真子空间、所有 K，或别的构造。

## 2. 原始仓库中新出现的相关路线

[dtq1997/zeta2-zeta3-linear-independence](https://github.com/dtq1997/zeta2-zeta3-linear-independence)，当前提交 `669c92bf7a3728e0de9ad80c373bc29fb5ca3d58`（2026-09-30），声明完成 1、ζ(2)、ζ(3) 的 Q 线性无关。其 Solution 用 Mathlib 的 riemannZeta、LinearIndependent；README 报告仅三项标准公理，以及 Comparator / nanoda 独立核对。本轮读了源文件，没有本地重跑此工程，所以这里保留“作者仓库声明与源码”的证据范围。

对本项目更有价值的是它的机制：整数极点、竖直复轮廓上的 logistic 泛函、Heine 绝对值上界；在一列素数阶上，利用本原多项式模 p 为非零常数排除有理点零值。参考原始源码 [Contour/Moments](https://github.com/dtq1997/zeta2-zeta3-linear-independence/blob/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58/Zeta32/Analytic/Contour/Moments.lean)、[Assembly](https://github.com/dtq1997/zeta2-zeta3-linear-independence/blob/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58/Zeta32/Assembly.lean)。下面的 θ 构造是本轮据此独立推导，不是从该仓库继承新目标的证明。

## 3. 直接对齐 θ 的普通整数极点泛函

记 t=1/2+iy，ρ(y)=(π/2)sech²(πy)，E(f)=∫R f(t)ρ(y)dy。上述源码证明

    E(t^e)=B'_e，B'_1=+1/2；
    E((t+j)^(-k))=k(ζ(k+1)−H_j^(k+1))，k≥1、j≥0。

定义

    Tθ(f)=−E(f''' )/24−(3/2)E(f')。

因为 (t+j)^(-1) 的一阶和三阶导数分别为 −(t+j)^(-2)、−6(t+j)^(-4)，直接得到

    Tθ((t+j)^(-1))=θ−H_j^(5)−3H_j^(3)。                  (1)

因此普通整数极点即可对齐两个未知值，不需平方节点中的 t 乘法。多项式矩为

    M_e=−e(e−1)(e−2)B'_(e−3)/24−(3e/2)B'_(e−1)，       (2)

导数次数不足的项解释为零。所有 M_e 都有理。

沿复轮廓分部积分给出

    Tθ(f)=∫R f(1/2+iy) wθ(y)dy，
    wθ=i(ρ'''/24−3ρ'/2)。                                (3)

三次分部积分要求 f 无轮廓极点、各导数的边界项消失；此处带有限整数极点的有理函数满足这些条件。ρ 及各固定阶导数指数衰减，f 为多项式增长。显式写 tanh(πy)=u，有

    wθ(y)=iρ(y)[(π³/3)u(2−3u²)+3πu]。

这是复权重，不提供原有正 Gram 非零性。它允许先研究 Heine 绝对值上界，再单独寻找模 p 非零性证书。新目标不能直接使用外部仓库的 prime-edge 定理。

## 4. 新构造没有免费恢复矩整性

**命题。** 对每个素数 p≥5，M_e 在 e<2p−1 时 p-整，而

    v_p(M_(2p−1))=−1，pM_(2p−1)≡−3/2 mod p。

纯 ζ(5) 泛函 T5=−E(f''' )/24 的首个坏矩是 e=4p−1。

**证明。** 由 [von Staudt–Clausen 定理](https://dlmf.nist.gov/24.10#i)，B_(2r) 的分母含 p 当且仅当 p−1 整除 2r，且仅含一次。第二项首次可能在 e=p 出现分母，被乘子 e=p 抵消；第二次在 e=2p−1，乘子为 p-单位。此处第一项的 Bernoulli 指标 2p−4 不被 p−1 整除，因此没有抵消。pB_(2p−2)≡−1 给出所写剩余类。

纯 T5 的前三个可能分母分别在 e=p+2、2p+1、3p，被乘子 e−2、e−1、e 抵消；第四次 e=4p−1，三个乘子皆为单位。低次数与 B'_1 特例的分母只涉及 2。证毕。

因此普通节点改写仍把首个坏矩阈值减半。不同节点、矩阵维数和轮廓可能改变总预算，但不能将原 ζ(5) 的算术常数直接迁入。

## 5. 已执行的有限精确实验

取 D_m(t)=∏_(j=1)^m(t+j)，W=D_N(t)^m，矩阵项 Tθ(t^(i+j)W/D_K)。利用 (1)、(2) 的部分分式定义得到 A+XB，再取 Δ(X)=det(A+XB)。全部系数以 fmpq 精确计算；有理 content 除尽后得到本原整数多项式 P，实际 θ 处用 Arb 球算术评估。次数至多 h。用 h+1 个整数插值，另在 −1、h+1 两点直接核对行列式。

第一组 K=5n、N=n、m=4、h=3n：

|n|K|h|log abs P(θ)|
|---|---|---|---|
|1|5|3|16.996451|
|2|10|6|58.760755|
|3|15|9|136.525392|
|4|20|12|240.711657|
|5|25|15|362.745168|
|6|30|18|495.088643|

另扫描 n=1,…,6，m=2,…,8，h∈{2n,3n,4n} 共 126 点。各 n 中非恒定多项式的最佳 log abs P 为 10.276884、40.532611、100.882367、177.563897、256.563648、355.216560，均大于零。这说明这个有限参数盒没有有效小值；不能据此证明普通节点路线渐近失败。

独立诊断器直接对显式 wθ 做高精度数值积分，在 j=0、1、2、5 核对 (1)，在 e=0,…,8 核对 (2)，误差小于 10^−80；并精确核验 p≤101 的全部素数上的首个坏矩阈值。这些是防止符号/移植错误的诊断，数值积分本身不是一般定理证明，也不是 Arb 严格积分证书。

复现：

    python research/zeta35_logistic_contour.py --max-n 6
    python research/zeta35_logistic_contour.py --max-n 6 --scan
    python research/verify_zeta35_logistic_contour.py

文件：`zeta35_logistic_contour.py/.json`、`zeta35_logistic_contour_scan.json`、`verify_zeta35_logistic_contour.py/.json`。

## 6. 继续研究的具体门槛

主线仍应完成真子空间的联合 content / 正行列式预算。普通极点路线作为并行探索，下一步应先做两件事：为新 M_e 推导逐素数完整系数 content 的下界；在 n=p−1 等可控尺度寻找 P mod p 的非零常数或其他排除有理根的证书。只有这两项与真实负的轮廓能量预算同时成立，才可将这一路升级为无理性证明候选。不能把外部 ζ(2)、ζ(3) 的已完成结果直接解释为 θ 已经可证。
