# 第244轮：仓库、原始文献与下一数值出口的有界复盘

2026-10-09启动，2026-10-10完成。C独立核查；文件名保留启动日。数学程序、CAS、扫描、Lean执行、外部仓库写入均0。主目标仍是一个新的ζ/L数值定理，本轮没有完成这个目标。

## 1. 仓库没有产生新的直接替代结论

实际只读核验 E:/codex-build/math：HEAD为
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，最新提交日期
2026-10-07T22:20:00-07:00，工作树及普通untracked检查为空。
2026-10-09T16:10:32Z实际 ls-remote 返回公开
[openai/math](https://github.com/openai/math) 的HEAD/main同一SHA。
没有fetch、checkout、reset或写外部repo；与236已记本地身份相同。

本轮FULL读README、history及Catalan目录README，CONTENTS/tree只作相关名称定位。
README明确各稿处于不同验证阶段，并非全部有Lean formalization；
其约42%是仓库自述的top-line统计，不能转成“本人核过全部Lean”。
10月7日history包含三篇因共同符号错误撤回、其它修订和formalization增补，
没有宣布本项目所需的新指定ζ/L数值定理。
[Catalan稿](https://github.com/openai/math/tree/main/preprints/Catalans-constant-is-irrational-September-24-2026)
是仓库明确声明的2026结果；本轮只复核其身份/目录，不重读全部proof artifacts、
不重跑finite seeds或Lean。既有236核心源码审读是历史范围，不能包装成本轮新验证。
Dirichlet L的zero-free half-plane标题也不能解释成其特殊值全部无理。

Qian Tang的
[zeta2-zeta3仓库](https://github.com/dtq1997/zeta2-zeta3-linear-independence)
本次公开HEAD/main为
669c92bf7a3728e0de9ad80c373bc29fb5ca3d58，与240固定身份相同。
本人FULL读其README：作者声明 \(1,\zeta(2),\zeta(3)\) 的Q-LI以及Lean/kernel
检查方法。本轮没有执行这些检查，也没有FULL读取全部依赖源码。
它的完整多周期泛函是240已采用的机制，不能以远端没有新提交为由宣布K5
预算或其它L值问题已解决。

## 2. Lai的具体机制与移植边界

[Lai arXiv:2610.06838](https://arxiv.org/abs/2610.06838) 当前页面列v1，
提交于2026-10-05；本轮没有看到journal reference，不称已经期刊发表。
复用固定25页原件，FULL读物理PDF3–6、20–23，另视觉核PDF6。
原文声明证明 \(1,\zeta(3),\zeta(4)\) 的Q-LI。本次有界审读确认所用对象是
\[
 R_n(t)=\frac{(6n)!^2}{(2n)!^3}
       \frac{(t-2n)_{2n}^{\,3}}{(t)_{6n+1}^{\,2}},
\quad
 \mathcal L_n(P)=-3a\sum_{m\ge1}(R_nP)'(m)
                      +b\sum_{m\ge1}(R_nP)''(m).
\]
这里假设实际关系 \(a\zeta(3)+b\zeta(4)=c\)，由Apéry定理得到 \(b\ne0\)。
对 \(\deg P<6n\)，\(R_nP\) 是严格proper rational function，原文Lemma2.2
保留完整调和头和有理修正，没有本项目K5的多项式商部。

其无界非零关尤其具体：\(q\equiv1\bmod9\)、\(q>|b|\)，令
\(m=(q-1)/9,\ n=2m\)。实际Hermite基中的局部二维块为
\[
 b_j\begin{pmatrix}-10b&8b\\8b&-6b\end{pmatrix},
\qquad \det=-4b^2b_j^2\in\mathbf Z_q^\times.
\]
其它盘为q倍数，故实际关系点的整个det非零；Dirichlet给无穷这样的q。
这是可迁移的“完整关系—局部块单位—无界非零”接口，
不是generic polynomial非零。原文20–22的绝对Heine/双曲余弦界与这个同一
分式匹配；全prime费用章节本轮没有FULL审通，故不把其约30.83与31.6
作为本人新认证的完整proof，更不把其数值差额移给K5或χ₋₇。
这篇及Tang机制在240已知，244没有因重复读取获得新的K5费用证书。

## 3. CDT原件必须按实际响应身份引用

本轮唯一一次fresh GET
[作者L2chi.pdf](https://math.berkeley.edu/~ytang/L2chi.pdf)
返回HTTP200，3621996 bytes，SHA256
7100fc291bb5c2bce4880d725eeba11e73114b0a20b4277f522030f855d89835，
pdfinfo为218页，Last-Modified为2025-12-10。
这与已存228作者原件220页、3628820 bytes、
9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c
不同；Root web索引也曾显示220页。页数不能唯一识别版本，不能推断变动原因、
撤回或缓存原因。本轮只绑定实际下载字节，不宣布它是所有公开载体的统一最新版。
[arXiv页](https://arxiv.org/abs/2408.15403) 仍列2024-09-16的v2/218页；
也不能仅凭此把fresh作者原件等同旧v2。

本人FULL读fresh PDF1–5、33–35，视觉核PDF34。
Theorem A仍是 \(1,\pi^2,L(2,\chi_{-3})\) 的Q-LI。
fresh的Theorem2.11.17明确只有
\[
 1,\quad \pi/\sqrt3,\quad
 3L(2,\chi_{-3})-\pi\log3/\sqrt3
\]
三项；不能把历史四项读域继承成本次或当前版结论。
这也没有直接覆盖此前
\(t=(5/2)L(2,\chi_{-3})-\pi\log3/(3\sqrt3)\)：分别两个LI集合
不能自动给它的指定有理组合非零。

另复用当前官方20页
[CDT quantitative/ICM稿](https://arxiv.org/abs/2510.04156)，
FULL读PDF3–5。其中Theorem2.1的全部statement要求
holonomic、Q(x)-independent、完整LCM类型以及同一
holomorphic \(\phi:(\mathbb D,0)\to(\mathbb C,0)\)，每个 \(f_i\circ\phi\)
允许meromorphic，且 \(\log|\phi'(0)|>\tau\)。
有理普通点pole的取消不自带假设敏感的合法图收益；先额外建立Betti/Hodge
也不是这个直接定理的硬门槛。Remark2.5保留literal \(n^{e_i}\) 的
\(\tau^\sharp(e)\) 费用。本人没有在本轮重新FULL证明§6–8或Theorem2.6；
其多place条件不能因为摘要说“effective”就免费领取。

## 4. 有限覆盖检查：导子7不是空白名称，也不是已证数值出口

本轮限于上述官方来源和少量arXiv指定关键词检索。未命中某个irrationality
定理不能证明全球未解决。Sun的2026 Catalan claim及Eskandari2026
approximation稿，本轮只读官方摘要/版本元数据：前者声明irrationality，
后者声明将特定逼近指数由0.52改善为0.62；没有FULL读证明，均不追加为
本项目已验证的数值定理。

对 \(Y=L(2,\chi_{-7})\)，
[Sun–Zhou 2602.12091v2](https://arxiv.org/html/2602.12091v2)
已经给出确切后备入口。本人实际读并保存引言至完整Theorem1.1及Table1；
特别公式(1.12)为
\[
 \sum_{k\ge0}\binom{2k}k^3
 \left(H_{2k}^{(2)}-\frac{25}{92}H_k^{(2)}
       +\frac{735Y-86\pi^2}{1104}\right)4096^{-k}=0.
\]
Table1的CM点为 \(z=i\sqrt7/2\)，binomial参数 \(2^{-12}\)，
\(r(z)=1/46\)。原文通过modular/Eichler/Epstein表示给这种评价身份；
这个已读statement范围没有声称Y无理，也不付同源完整整模型或关系点非零。
它可保留为准确导子匹配的后备源，不能立刻恢复增logdepth/裸评价的旧路线。
本轮未读它的全部证明，故不将作者完整恒等式证明冒称本人独立认证。

## 5. 唯一具体下一候选及四接口

本轮选择的是A244固定的非对称χ₋₇完整泛函，保留原
\(R_n=D_n^4/D_{5n}\)、\(h=3n\)：
\[
 V_\chi(f)=-49^{-1}\sum_{a=1}^{6}\chi(a)
 B\big((t+a/7-1)f(t+a/7-1)\big).
\]
其简单极点输出恰为 \(j(Y-H_{7j,\chi}^{(2)})\)，多项式商部是有理
Bernoulli值。本人FULL读A244最终稿和Root244对称稿，按它们实际对象记录：

| 必须匹配的接口 | 非对称原 \(R_n\) | 对称后备 \(R_n(t)R_n(-t)\) |
|---|---|---|
| 完整目标投影 | D1–D3已付，不丢商部或其它行列 | 正负简单极点/商部投影已付 |
| 全系数整模型与净预算 | D7完整safe LCD已付；fixed7及全prime primitive净费用未付 | 不能继承非对称模型的费用，独立净预算未付 |
| 每个固定有理关系点的无界非零 | 仍未付；正密度乘复相位不证明它 | 真值处正Gram已给所有n/h非零；假设Y=q即给实际q非零 |
| 同对象实处界/严格差额 | 统一Re0线及D6 leading Heine envelope转移已付；−6仍条件于原完整Fstar认证 | \(|R_n|^2\) 改变外场，独立能量未付，不能借D6的−6 |

这是不同于241K5边缘Gram的具体结构入口：最高头阶数从5降到2，
完整空间仍只有Y和有理数。但它同时把调和头支持扩大到35n。
A/Root已明确支付 \(35n/2<p<35n\) 的首层rank-k及合法
\(v_p(d_n)\le2k\)；积分175/4只是该粗上界的贡献，不是费用lower、
也不证明这个候选不可能。fixed7的degree-dependent Bernoulli费用同样
不能放进 \(o(n^2)\)。

因此下一次只批准一次固定对象预算准入：完整计入新增
\(5n<p\le35n\)、fixed7、其余prime powers及同一 \(S_n^h/F_n\)，
先给能够改变strict比较的宏观机制。若只有common LCD或局部小省，
暂停该候选，不自动延长六轮。只有预算方向可达，才继续非对称源自己的
无界非零。对称后备已有非零关，但没有资格用非对称能量替代它的首关。
原K5默认逐层优化在244结束；既有完整投影、∞非零和全prime引理保留，
不把当前上界不足改写成全方法no-go。

实际读取身份、未读范围、唯一fresh PDF及数学0账见
[本轮scope](../literature/global_review_sources_round244_20261009/dual_reading_scope.md)。
