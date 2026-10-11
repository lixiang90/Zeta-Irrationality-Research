# 第241轮 B 实际读取域

2026-10-09；轮次文件名仍用20261008。本人数学程序、CAS、prime/parameter 扫描、Lean run 均为0。下载、读取、hash是文档操作。本稿不是全部仓库/依赖的 FULL 审核。

## 已有输入

实际 FULL 读取 research/global_logistic_whole_functional_bridge_round240_20261008.md：9796 bytes，SHA256 a655168bbd86afbacecf29bd91d396c7ce848bd5ea418a3300b71de36a5e316c。它支付完整数值投影，不继承未付 primitive 算术。

实际 FULL 读取已保存 pinned 源码的 Zeta32/Family.lean、Interfaces.lean、PrimeObstruction.lean、PrimeEdge/LocalShape.lean、PrimeEdge/Gram.lean。均来自240目录 root_zeta23、下述 commit；没有读取全部 public imports。原泛函的旧块 determinant 和 prime-edge theorem 只用于识别接口，不作为新源结论。

## NEW241 pinned packet

官方 raw GitHub base：https://raw.githubusercontent.com/dtq1997/zeta2-zeta3-linear-independence/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58/ 。以下下载成功并实际 FULL 读全部保存文本，文件名下划线对应原路径斜线。未编译。

| 文件 | bytes | SHA256 |
|---|---:|---|
| Zeta32_Arith_Local_Entry.lean |15163|c52102feb327500c245b356711ea4589c43f23c438402696cd17c14078e4308c|
| Zeta32_PrimeEdge_Basis.lean |6314|4c5588291c6eff2277e79c872dc7e5d2876325ff3f345abd3b67f319ac80ef5e|
| Zeta32_PrimeEdge_Blocks.lean |2444|cf3f0b1d648a592bdc6eaa9f3097ed10065f15f0b7475762eedc028a0d2f0f43|
| Zeta32_PrimeEdge_Disc_Bernoulli.lean |6604|30240f0e8e00ac84b2dcb71b3803ed5994b49d7d7a4278185b00065c3eaef713|
| Zeta32_PrimeEdge_Disc_Core.lean |4125|8983f741cbbbdd0963078f0a7f09138db7f745b6146a8963f7b6d1b825e85dd8|
| Zeta32_PrimeEdge_Local.lean |3532|88ea18b14350451a724a32f41cdb973f39b5ee7a7ad75f02c8ee308021caac38|
| Zeta32_PrimeEdge_Reduction.lean |1939|a72a538474adb01a300599371995b26350c7ee8a9d4144ce6b0260f8c6248e26|

本人重新纸证三阶整性（取消前三个 Bernoulli 可能极点）、完整 polynomial/near/far 分布误差、全部 CRT tuple 的盘指数、半阶交叉消失、参数余量和 primitive 比例。原一阶源码不是这些新公式的自动认证。

## 固定精确核验的使用

实际 FULL 读取 research/logistic_prime_edge_fixed_blocks_round241_20261008.py 和同名 JSON。producer 使用 Fraction、首一除法、全部残数和有理消元，对三个固定矩阵做一次精确核验；不是变化的 \(p\) 测试。程序对象是 \(V_3^\circ=B\circ\partial^3\)，本稿归一化为 \(V_3^\circ/24\)，其 determinant 分别除 \(24^4,24^3,24^2\)。运行由另一代理登记，本人没有重跑，本人数学执行为0。程序明确防止再次覆盖结果。

全素数非零由新稿全尺度证明支付；没有将原公告或有限执行外推为数值无理性、全 \(n\) 非零或全素数 primitive 费用。
