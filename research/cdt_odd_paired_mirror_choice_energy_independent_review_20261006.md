# Mirror choice energy 的独立数学审阅

2026-10-06，conifold_arithmetic_hypothesis。NEW 独立审阅，不修改被审稿与冻结输入。所有同行/旧数学 producer 仅读，无执行、import 或重跑。本审阅没有新的数学 producer，没有新增外部 PDF。

## R1. 实际读域和 fingerprint

实际完整读取：

- 主稿 research/cdt_odd_paired_mirror_choice_energy_20261006.md，M1–M9、M1–M23 全公式，SHA cc3821c935474ea1b87011383230b91ac04dcb147c2b09d6ce65e5f899438dd7。
- NEW 源码 research/cdt_odd_paired_mirror_choice_energy_20261006_verify.py，完整静态阅读，SHA 03fac0d728b448d8168d8d02972e910d82e0194c840365f99c769d31554a3b6a。不执行、不 import。
- 冻结同对象 energy research/cdt_odd_paired_plucker_energy_rate_20261006.md，E1–E8、全部 E1–E26 公式，SHA 01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a。
- 冻结 gcd research/cdt_odd_paired_primitive_gcd_rate_20261006.md，G1–G10、全部 G1–G13 公式，SHA 77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2。

上述文本分别完整输出、实际阅读，无截断。β0/γ 的既有 producer 本审没有重新执行或重新计算其输出证书；它们的冻结上下界按已登记输入使用，本审实际核的是 mirror 对同一对象的继承与改善。

JSON research/cdt_odd_paired_mirror_choice_energy_20261006_verify.json，SHA eb71f6809d98d793f32abca6df7dff199a5d450de73853a5e5bcfcbe72422b9e：完整文件以普通 JSON parser 读取，确认实际有4096条 cell records；人工静态读全部 metadata、前110行，以及 indices 0,1,793,794,795,4094,4095 的完整 rational bounds。没有声称4096条逐条人工阅读/重新算术验算，也没有运行 producer 复算 cell bounds。4096闭区间的全 q 数学覆盖是下文对完整源码/区间公式的检查范围，不是有限采样的外推。

## R2. 固定 determinant 与系数损失

冻结 E5–E7 给同一实际饱和整数基的 cardinal/high Newton 分解。Mirror M1 保留两个 (j−1)!，其无 gcd 系数满足

\[
\frac{\widetilde\kappa_m}{\widetilde\kappa_{m'}}
=\frac{b_m}{b_{m'}},\qquad m'=2n+1-m.
\]

因为 \(|S'(m)|=|S'(m')|\)，没有额外 factorial credit。由
\(b_{j+1}/b_j=(6n+j+1)/j>1\)，所以
\(\log(b_{m'}/b_m)\) 随 m 递减。包含 k 个左节点的选择至少支付末 k 对的准确平方损失 M6；这不是让系数最优选择与能量最优选择各自独立后再拼接。

Stirling 全端点误差为每项 O(log(n+2))，B 的导数只含可积 log；M7 的 Riemann 误差因此对所有 k uniform 为 O(n log(n+2))。其
\[
P(q)=2\int_{1-q}^1[B(2-t)-B(t)]\,dt
\]
非负且单调：B'正，差在低半区非负。对 f''=log 的原函数直接积分得到 M14，常数和正负号相符。

## R3. Hardy 排序、uniform finite-n 界与闭式

低半区选 d=n−k 个节点、高半区选 k 个节点。低排序的第 i 项在
\([i-\tfrac12,k+i-\tfrac12]\)；高排序第 i 项在
\([k+i-\tfrac12,n+i-\tfrac12]\)。这正是 M8。Ratio
\((\delta_j-\delta_i)/(\delta_j+\delta_i)\) 对 j 坐标递增、对 i 坐标递减，故 M10 三个块逐项是合法上界；不要求选择连续节点。

三种 affine logarithm Riemann sums 的误差可用 strips 分解统一支付。非零 grid 值至少一个整数 unit；靠近零 affine boundary 的 O(n) cells 各有 log 可积误差。其余 cells 的移动一格误差由 \(\sum_{r\le Cn}1/r\) 控制。Moving edge k/n 本身是 grid edge，常数可以独立于 k。因此 M12 的 O(n log(n+2)) 全区间 uniform，含 q=0,1，不只某个固定比例序列。

我逐项积分核过 M13。特别 LL 部分为
\[
f(q+2L)-4f(q+L)+3f(q)+2L f'(q),\quad L=1-q,
\]
即稿中 \(f(2-q)-4f(1)+3f(q)+2(1-q)f'(q)\)；HH 部分给
\(f(3+q)-2f(3)+f(3-q)-2f(1)+2f(1-q)+2qf'(1-q)\)；
LH 的矩形积分给 M13 的同一六项组合。q=0 得2log2，q=1 得稿中单半区公式。

将同一 q 的 P 与 c 相加后取 min，准确给每个真实选择 M16。选择数2^n 和平方只付 O(n)，冻结 E12–E22 的 F_n、Z_H、L_n、Γ_n 保持完全相同。原 n²logn 的4+5−4−5消去不受修改。故 M2/M17 合法用 c_* 取代旧 c_H，且共同 gcd 的 \(-2\log\Gamma_n\) 仅支付一次。

## R4. 4096-cell 证书的源码层面核验

完整源码里的 log 算法使用24项正 atanh series。最后 term 为 z^49，余项
\(2z^{49}/[49(1-z^2)]\) 上界正确。Power-of-two reduction 对负 power 以 scale 交换区间端点；所有后续 add/product/scale 都完整保留 signed interval。Outward floor/ceiling 使 rational 10^-9 输出覆盖内部 exact Fraction。

f 与 f' 在[0,1]递减，零端点分别连续取0。f' 在[1,4]介于−1与 \(4(\log4-1)<2\)；源码另 assert log4 的 interval upper<3/2，所以 midpoint±2 halfwidth 是合法全区间 f14。M13 的全部 arguments 在所用函数的范围内。Products 用四个 corner，允许舍弃相关性增加宽度但不会反向。P 单调给 cell 下界 P(l)，再与0取 max 仍是安全 lower；cell upper 用 P(h)。

所有 index 从0到4095，对应闭区间 \([i/4096,(i+1)/4096]\)，覆盖全部[0,1]，边界重复不妨碍覆盖。程序的 midpoint sample 只给 global minimum 的 upper；global lower 来自全部区间 lower 的 min。这是区间覆盖，与仅4096个采样点不同。

Saved metadata 给 c_*∈[840144459/10^9,84511537/10^8]，minimum lower cell794；所读 index794 的该条 bounds 和相邻条记录吻合该 pin。这里我未逐条重新生成4096个 rational 算术结果；源码的自足数学正确性与作者恰一次 PASS 历史是证书的明确依据。程序不证明 M2 全 n、M19 equality、determinant nonzero 或 arithmetic margin，主稿已准确保留。

## R5. Mirror-constrained 正和的真实变分极限

任一选择经验测度在每个 grid site 至多一粒子，极限 density≤1；选择加其反射等于全部2n中点 grid，所以 \(p(x)+p(2-x)=1\)。这给稿中 weak compact feasible set C。κ 的 Stirling 项对全部选择 uniform，j/n 和2−x 的半格 phase 只付 O(n log n)，所以 M19 的 +4logn 归一化正确。

K≤0且 \(-K\le\log4+\log(1/|x-y|)\) 在近对角。每个 grid site 的 spacing-k 邻点至多2个，直接求和给 M20 的 uniform η(1+|logη|)+log(n)/n。Density≤1 给相同 continuous tail bound。Truncate max(K,−M)，先除原点小方块，再 weak limit；diagonal 的 truncated 补入是 O(M/n)。原点小方块的截断 mass 控制为 O(Mε²)。这些步骤使 log energy 在 C 上连续，并允许先 n、后 ε、后 M 的次序。

Recovery 的 floor-prefix construction 每步 increment 是0或1，因为 n乘一个 cell 的 p 积分≤1；prefix discrepancy≤1/n，配上镜像自动满足每对选一的真实约束。故任意 feasible p 均有 binary recovery，且 M20 保证 energy 也收敛。Compactness给 upper、recovery给 lower，正项logsum与最大项的差只有 O(n)，所以 M19 是所定义正选择和的准确极限。

这没有证明原 complex determinant 的相等，也没有把 weighted low Gram 的 L_n 上界称 equality，主稿对此已明确。

## R6. 严格负定、唯一 maximizer 与 first variation

对 x,y>0，令 u=logx,v=logy；M21 的 odd exponential series 和 square-integral kernel identity 正确。Feasible densities 的有界性和 R5 的 log tail 使 signed difference 的绝对双积分有限，可交换各非正 square 项。若 K-energy为0，ell=1 的 weighted tail连续且 a.e. 为0，故任一有限区间的加权 signed measure 为0，遂差测度为0。这样 K 严格负定，F 严格 concave。C 的 compactness/energy continuity 保证唯一 maximizer。

低半区 perturbation 与高半区反射取相反号后，δF=2∫g_*δp。最大化的盒约束因此给 p=0处g≤0、p=1处g≥0、interior处g=0，主稿符号正确。Concavity使该完整 first-variation condition 充分。M23直接由 M16和极限继承，故未知最优 density 不影响已证 strict upper。

## R7. 结论与审阅边界

主稿 M1–M23 的纸面数学通过。本审准确确认同一饱和格的 mirror-matched 全 n 解析改善，c_* 严格区间接口，正选择和的准确受约束变分极限，以及唯一 maximizer/first variation。冻结 β0 下界、log2>0.693 与新 c_* lower 合成 \(\beta_{\rm mirror}>9.09188285412558\)；再加冻结 γ lower 的两倍得同对象解析率>12.00357285412558，数值相加与严格方向正确。

没有实际解出 p_*；没有两个辅助矩阵的无限 unit/nonzero，也没有足够便宜的 all-prime fee。原 safe cost 与已证解析率的差不能当 actual cost lower bound/no-go。没有新的 ζ/L/Catalan 无理性、线性无关性或 Lean 结论。

本审数学 producer 执行0，同行/旧执行-import-重跑0；没有改旧420 pins。主稿作者的 NEW mirror run 恰1 PASS；既有其他 producer 历史没有混入或抹除。本审不冒认新的 primary PDF 读页。
