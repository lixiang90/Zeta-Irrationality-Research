# 第242轮 B 实际读取域

2026-10-09。数学程序、CAS/interval运算、prime/parameter scan、Lean run均0。源码下载和hash不是数学执行。只新增本轮 packet文件；未改241、主日志或manifest。

## 实际 FULL 输入

本人实际 FULL 读 A 的本轮 research/logistic_gauss_arithmetic_round242_20261009.md（G1–G16），冻结身份8719 bytes，SHA256 0b2bdf55e221aa353b90aaabaf96b4545d0daa69465e2941166c36cad4191cdf；包括全部 CRT pair、小 prime binomial基原地取消F和所有primepowers。不是以消息代替读取。第241轮完整模型和第240轮 wholefunctional是此前已 FULL 读的冻结输入。

实际 FULL 读既存 pinned root_zeta23/Zeta32/Assembly.lean 的整个文件，仅用于核定需要同时有 arithmetic、analytic、prime-edge三个 node的原数值接口；没有继承原ArithNode常数或AnalyticNode认证。

C本轮初始 all-\(p>n\) 宏观公式先由团队消息收到，本文独立纸核完整atom系数、carry \(\nu\)、可选类数量、Vandermonde损失与F normalization。随后实际 FULL 读冻结 research/logistic_gauss_outer_round242_20261009.md：9354 bytes，SHA256 994ea8727792abc787e8b4b27db5171dc171f23a29bbd7793584eb8c4a9f416c，全部O1–O12；并实际 FULL 读其scope3687 bytes/SHA015c989574732fbfc5850edcc378395b0cb446a880dea08caae3f109940648d3。其初始费用profile已被下面强余项内容取代，不将旧面积或旧下界诊断作为最终方向证据。没有以早先消息冒称读取，未读取C的两份primary全文或其所有imports。

随后实际 FULL 读 Root最终 research/logistic_gauss_graded_head_round242_20261009.md：9113 bytes，SHA256 1daeea8510afa88179d877bbd1a68481ea225d06b4020156411120fd09d46ca5，六节H1–H15和完整九段表。本人独立纸核 all-e integer moments、integer Euler类indicator、全部unit-cycle/partial-head分级展开、s=1 Bernoulli阈值、全部商部/参数系数和同类平方Vandermonde。B正文同时给自含证明（用等价的 \(\mathbb Z_p[t]\) CRT indicator），并实际手算九段积分恰12、outer净面积0和全素数 upper \(529/40+12=1009/40\)。没有以 leading rank或抽样替代完整系数证明；总rank约束在 \(s=3,3/2<x<5/3\) 的旧误算已明确撤回。

## NEW242 pinned primary

commit 669c92bf7a3728e0de9ad80c373bc29fb5ca3d58，官方 raw base https://raw.githubusercontent.com/dtq1997/zeta2-zeta3-linear-independence/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58/ 。下列保存文本均 actual FULL 读。文件名下划线对应原路径斜线；没有编译或读取全部 imports。

| 文件 |bytes|SHA256|
|---|---:|---|
|Zeta32_Arith_Distribution.lean|561|dc180b613f1daef16d7e79b2f051e12ca4e63c80eb7d2a0c6e8787e9bdfb4e6c|
|Zeta32_Arith_Greedy.lean|6852|d37e692a8cedfc045af834492f1d57f9184068f60d65f73d503f897763e7aa83|
|Zeta32_Arith_Local_Alloc.lean|6484|e18ab3f8e03f73bd291c36235c2494364621b13060f16bdd1598f39fee7388da|
|Zeta32_Arith_Outer.lean|8604|5dbb12c1d80c8320f85e68ef0a37baefd8c0bb63651ad719f38e2d9a8f41f725|
|Zeta32_Arith_Profiles.lean|678|debca2f072cc455ce7ea1eaed6fdf642969c62c6c089805ca9da816d36339bc2|
|Zeta32_Arith_Relaxed.lean|8282|58d12364e5500e5d7e0eb834205f29e8ee703aea3329ebb2f0924c0523c3b1a7|
|Zeta32_Arith_Sum_Main.lean|21698|33338bedf29b6047e28c749b0d259d02a3a8e138aef978cdfe54b4e510ccfa15|
|Zeta32_Arith_Sum_Numerics.lean|5639|3422ab2efe92f8804658dca77f0b5eac6bf8fa93d29efe32ba9f6516e711da37|

Greedy/Local.Alloc用于核实际slot和monic/CRT定义。Distribution明确原Tate-algebra路线并未formalized，因此不从标题领取完整新分布。Relaxed完整读了平方完成、column sums、normalization代数和条件；本文用同一代数独立证明c5平移。Profiles、Sum.Main、Numerics用于定位原partition/PNT/有限piece路线；未读Sum.Pieces、Windows或全部PNT imports，不声称重新核196个piece或原5.66数值认证。

本轮R20–R23的有限上下常数完全以纸面variance界及更新后的九段有理梯形积分证明；不依赖未重核的原196-piece结果。最终 \(36/5\) 下界只针对所选连续松弛/class upper-profile积分，未当actualGauss费用下界、精确整数greedy费用下界或全方法排除。早期 \(56/5\)、未落稿的 \(1171/160\) 诊断不属于最终预算结论。旧241/主日志/manifest没有编辑。
