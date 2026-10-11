# C236 独立数学审阅

2026-10-08，审阅者 /root/round218_lambert_carrier。实际 FULL 读最终 research/global_catalan_weight4_review_round236_20261008.md，13797 bytes，SHA256 cf93376bf4add588566fc577a3cf3bf682b5164dc9b1e02036e1e588cbfbb6a0。未修改目标。数学程序、扫描、旧 producer 复跑0；未新增 primary 读域。

**结论：C6–C10 的新命题及全稿移植边界 PASS，无必要修正。** 此收据不重新认证原 Catalan 证明的全部 finite pivots、root brackets、interval tables 或 Lean。

从 C5 直接代入 q=4/(1−z²)、r=−4z/(1−z²)，独立得到
\[
 S_z=\frac z{1-z^2}S+\frac{2(\ell+J)^3}{1-z^2},
 \qquad (\sqrt{1-z^2}S)_z=\frac{2(\ell+J)^3}{\sqrt{1-z^2}}.
\]
q-meromorphic germ 的 z-Laurent 必须 even。齐次解为常数乘 (1−z²)^{-1/2}，所以 S(0) 的全部贡献均 even；OddS 恰为 C7，非零首项2ℓ³z与目标 c4 无关。消去端点数值不能取消全部奇数 jet。

独核背景 odd：rℓ、2ℓJ、r(ℓ³+3ℓJ²)。沿指定上半平面路径继续到∞，
\[
 J=i\pi+2/z+O(z^{-3}),\quad \sqrt{1-z^2}=-iz(1+O(z^{-2})),
 \quad \operatorname{Odd}S=8\pi^2\ell\,\log z/z+O(1/z).
\]
这里 ℓ=±iπ，系数非零；符号与积分因子一致。背景、J以及任意 rational q 系数在该∞叶都有收敛 Laurent，没有 logz。非零 A(q(z)) 只能提供有限阶零或极，不能消掉这一 logarithmic monodromy。因此 C9 不可能是局部恒等式，证明所有保留 S 的固定 C(q) 线性组合（degree 任意）均不能在 q4 亚纯。证明包含 rational target shift，不依赖 c4 是否有理。

全稿 C1–C4 正确区分：完整 entry 的辅助周期消去、独立无限素数非消失、全层整模型及同一 mixed determinant 的实处估计。其原证书数值在本收据中只按稿件明确的源输入采用，未复算。原目标、原 period arrays、48×48 seeds 和二次费用不能由增加 log 权重直接搬到 c4；π²G 亦不能当作有理系数。

C9 的下一门槛是真实全 entry period projection，须在 nuisance kernel 上保留足够目标 rank，并支付原格与同对象解析表示。C6 不关闭 growing mixed kernels、非线性 determinant 投影或所有偶 ramified 图；与其结论和停止条件相容。没有新 β(4)/c4 数值无理性或LI结论。

本收据已保存后实际 FULL 自读；作者自读与上述独立目标审阅分别记录。
