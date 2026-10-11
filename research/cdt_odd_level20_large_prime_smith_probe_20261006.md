# 四个大素数 Taylor 矩阵的 Smith 见证与边界收益

日期：2026-10-06。本文记录四个预先指定的 square Taylor coefficient maps，不是未知 Shidlovsky leading flag，也不证明渐近收益或任何周期无理性。既有冻结 producer 均未导入或执行。

## 1. 计算对象与可直接核验的证书

采用已审 level20 实际 t/q 坐标、divisor sums、三目标 packet，以及原 rank4/rank7 source 的素数缩放。四组输入固定为 (p,D,m,r modp)=(11,5,4,4),(11,5,7,4),(19,4,4,9),(41,5,7,13)，都满足 D<p<N=m(D+1)<p²。只取 n=0,...,N−1 的全部 Taylor rows。

[新脚本](cdt_odd_level20_large_prime_smith_probe_20261006.py) 使用精确模 p³ 算术。对每个 coefficient matrix M，[证书](cdt_odd_level20_large_prime_smith_probe_20261006.json)保留 M、X、Y 和 diagonal，满足

\[
 XM Y=\operatorname{diag}(p^{a_1},\ldots,p^{a_N})\pmod {p^3},
 \qquad \operatorname{rank}_{\mathbf F_p}X
       =\operatorname{rank}_{\mathbf F_p}Y=N.
\]

这里 a_i∈{0,1,2,3}，a_i=3 表示实际指数至少3。X、Y是显式单位变换，所以该等式确实证明 capped Smith exponents；零对角元不意味着实际指数恰为3。38项检查覆盖坐标反演、split root、packet首项、完整矩阵恒等式、单位变换及本表成本。独立 agent 只读全部见证，重复矩阵乘法和域上消元核验通过；未重新运行 producer。

此前直接计算巨大整数提升的 Smith normal form 未完成，进程已终止。本证书改为有限模环中的显式等价变换，不依赖那次未完成计算。

## 2. 实际有限结果

记 k_p 为原 constant block 的 denominator valuation。本组 Taylor rows 的原成本为 B_p=k_p·min(p,N)+3(N−p)_+，新 capped cost 为 Σ_i(3−a_i)。

| p,D,m | counts a=0,1,2,≥3 | B_p | capped cost | 净收益 |
|---|---|---:|---:|---:|
|11,5,4|13,0,0,11|39|39|0|
|11,5,7|30,1,11,0|104|103|1|
|19,4,4|1,0,0,19|3|3|0|
|41,5,7|1,0,0,41|3|3|0|

两个末端窗口样本与[全尺度末端命题](cdt_odd_level20_large_prime_net_20261006.md)相符。前三层的 capped cost 之外仍可能存在更高指数，本文没有计算它们。

## 3. 唯一有限收益的机制

在 rank7 的 2D<p≤4D 窗口，p³缩放后的 constant、L 两块模 p 为零；只有 T₂、K₂和三目标，共5(D+1)列，能在 late rows 模p非零。取本实验 N=7(D+1)，late row 数为 N−p。因此强制 rank defect 至少

\[
 (N-p-5(D+1))_+=(2(D+1)-p)_+.
\]

对 p=11,D=5，该值恰为1。证书给 late rank=30，达到全部30列的上界，所以全部观察到的收益正是这一个边界缺口。正值仅出现在 2D<p<2D+2，窗口宽度和缺口均为O(1)；随D求和的贡献为O(logD)，不是D²主项。

在真正 leading set V_D⊂[0,N_D)、N_D=7(D+1)+O(1) 中，缺少的 early rows 和端点偏移最多O(1)。上述**列数边界机制**仍只给o(D²)。这不排除其它中间窗口的特殊关系或正 Smith 整除性；也不把本实验的全部 Taylor rows 当作实际 primitive flag。

## 4. 对后续行动的影响

本表不给新的正D²收益。后续需证明固定宽度边界之外的真实 late rank defect，或评价矩阵超过三层的整除性，并保留原 row factors 后计算净收益。没有理由扩展同一边界样本来推断数值定理。
