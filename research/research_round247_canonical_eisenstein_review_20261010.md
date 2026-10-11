# A 独立审阅 B247 canonical Eisenstein源

2026-10-10。结论：**PASS，无必要数学修订**。这是对 B 的独立纸审，不以其作者自校验代替审阅。

本人实际 FULL 读取最终 `canonical_eisenstein_nonholonomic_round247_20261010.md` 全部五节 N1–N14：8583 B，SHA256 `63956362354d4f1fb41fb166838bac80af30dc632521573c31f9f7a7133c2372`；及 `packet_reading_scope.md` 全文：3744 B，SHA256 `c9951088baf251bb7e693e047700deebbfb4f8d9a79a3f20d6c2f2d0114d99a5`。两份均按保存字节重新核身份。

1. **真实forcing。** N2 的字符由 Yang 的函数身份与 t 不变性得出；Γ₀(7) 的 U 分支支付 τA 为第二解。无 δ 一次项使 δ-Wronskian 恒定，native 极限为 1/(2πi)，故 δlog q=A⁻²。展开 N4 的两个交叉项确实相消。N5 的 f=uA³/P 与 N9 的正项 +(8/7)P²A⁻³ 均准确。e₁/f 的 Laurent degree bound 及 canonical 全 prefix d_N² 模型没有由有限头外推。

2. **实际返回路径与无限独立。** A 的零点、u′零点及有限 ODE坏点预像在 H 内局部有限离散；u 与变换律使 UTᵏτ₀保持未删。避开离散集的路径存在，其 u 投影真实闭合且沿路有 local inverse。终点 inverse 为 UTᵏτ(u)，返回芽即 (7τ+7k+1)⁻³F₀。除以局部非零 F₀ 并以 τ 作变量后，任何有限关系成为有理函数身份；不同实轴三阶 pole 逐项迫所有系数为0。无需将这些实轴点冒称 H 内奇点。普通点的有限阶 ODE 解空间不可能包含全部返回芽，因此 A⁻³ 非 D-finite 的证明完整。

3. **固定微分过滤。** 若 canonical源或其常数 A 补偿 D-finite，N9 的有理运算会使 A⁻³ D-finite，矛盾。若非零 Q∈C(u)[∂u] 的输出 D-finite，其 annihilator H 给非零 HQ；该 Ore 环 leading coefficient 乘积非零，故输入亦 D-finite，仍矛盾。Qy=0 同样直接给 annihilator。输出/输入另加固定 D-finite 项的扩展只调用准确闭包性质。

4. **停止范围。** 结论仅关闭同一 u 上 canonical 单一方向的拟议有限 holonomic scalar/cyclic入口；它不是所有直接 CDT 的必要假设，也不排除多个相关非D-finite方向的抵消。尤其不能由本稿关闭 A247 的 correlated level14 dyadic源。没有领取 Y 数值定理、全leaf投影或严格预算。

数学程序/CAS/Lean、素数/参数/map扫描、新primary查读或下载均0；未改 B/Root/历史资产。本人实际 FULL 保存复读本收据；准确读域另存本轮 `alternative_review_scope.md`。
