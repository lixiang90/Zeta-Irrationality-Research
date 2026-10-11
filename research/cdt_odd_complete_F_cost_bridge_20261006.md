# 完整 rank10 源的8列整模型与 CDT 费用接合

日期：2026-10-06。NEW 纯证明。使用本轮[完整 F 的全素数幂及高层 packet](cdt_odd_complete_F_high_filtration_20261006.md)、冻结的[H 原格 packet](cdt_odd_classical_frobenius_smith_20261006.md)与[near-balanced DVR 桥](cdt_odd_level20_balanced_smith_bridge_20261006.md)。旧 producer 不执行、不导入、不改写。本文核算的是可证明的费用上界，不是最优费用或数值无理性定理。

## 1. 同一个源和所有地方的安全表

保留原 z 坐标 x=256z，实际 rank10 函数
\[
(1,H_z,\theta H_z,\theta^2H_z,\theta^3H_z,
F_z,\theta F_z,\ldots,\theta^4F_z).
\tag{C1}
\]
仅在反证假设目标有理时 F_z 的初值有理；固定初始分母并入 D_0。准确 forcing 保持原状。令 b=2+\varepsilon、0<\varepsilon<1，所有 e_i=0。一个安全 LCM 表为：常数的8列都为0；四条 H species 每条4个 b 列与4个0列；五条 F species 每条4个1列与4个 b 列。因此
\[
m=10,\quad s=8,\quad
\nu=(0,4,4,4,4,8,8,8,8,8),\quad\sum_i\nu_i=56.
\tag{C2}
\]
H 用准确 odd-part \(\Delta_{2n+1}^4\)，有限 n 的差由固定初始因子吸收；F 用新证 odd-part \(\Delta_n^4\Delta_{2n}^4\)。Euler derivatives 不增加分母。

原 z 的2处依旧用冻结 V13 安全模型：全前缀清数的 log 是 O(log N)。固定 D_0 亦只给 O(1)；在完整 polynomial source 中累计至多 O(D log D)=o(D²)，固定张量维数后仍为低阶项。小素数的高次幂可直接按这张完整 LCM 表计费，不假装它们为零。native x 的 256^{-n} 产生的 dyadic 主项没有被转移或删除；本文结论只针对 C1 原 z 的整格。

## 2. 原最大 transport 的完整计算

原 CDT (8.0.2) 对每个阈值取 admissible coupling 的 maximum。取归一化评价次数 u=n/N_D∈[0,1]，species 各质量1/10。9条非恒定 species 共同有4个 b 列，五条 F 另有4个1列。阈值 t=p/N_D 的 payoff 上界为
\[
M_b(t)=4\min\{9/10,(1-t/b)_+\}
       +4\min\{1/2,(1-t)_+\}.
\tag{C3}
\]
第一项分别受非恒定总质量及成功次数区间长度限制；第二项受 F 质量及其成功次数区间限制。它们可同时达到：把常数 species 配 u∈[0,1/10]，四条 H 等分 [1/10,1/2]，五条 F 等分 [1/2,1]。该 coupling 在任意 t 同时达到两项上界，因此 C3 是真正 maximum，非猜测的可行下界。原 finite discrepancy/tolerance 极限按冻结桥处理。

故全密度 baseline 为
\[
\begin{aligned}
\tau_b&=2\int_0^\infty M_b(t)\,dt\\
&=8b\left(\frac9{10}-\frac12\left(\frac9{10}\right)^2\right)
 +8\left(\frac12-\frac12\left(\frac12\right)^2\right)\\
&=\boxed{\frac{99b}{25}+3}.
\end{aligned}\tag{C4}
\]
尤其 b↓2 时 \(\tau\to273/25\)。这是完整10 species 的原 transport，不是把 row denominator 的指数增长率直接当作 CDT 费用。

## 3. 两个支持块的同一 Smith baseline

取原 source E_D，R=10(D+1)，实际 leading rows V_D⊂[0,N_D)，N_D=10D+O(1)。对 odd p∤D_0、p²>bN_D+O(1)，考虑真正 square matrix \(\Psi_p=p^8\operatorname{eval}_{V_D}\)。常数方向 image⊂p⁸、四条 H 的方向 image⊂p⁴、五条 F 方向 image⊂1。baseline floors 合计
\[
\boxed{24(D+1)}.\tag{C5}
\]

冻结 H packet 和本轮完整 F packet 分别给
\[
\begin{aligned}
k_{H,1}&=3(D-(p+1)/2+1)_+,\quad
k_{H,2}=2(D-3(p+1)/2+1)_+,\\
k_{F,1}&=4(D-p+2)_+,\quad
k_{F,2}=3(D-3p+4)_+.
\end{aligned}\tag{C6}
\]
H 两族在 \(\Psi_p\) 的第5、6阈值，F 两族在第1、2阈值；每块第二族 modp 嵌入第一族，而且 H/F 块支持分离。常数方向与二者亦分离。因此 capped floors \(0\le\beta_i\le8\) 满足
\[
\boxed{\sum_i\beta_i\ge24(D+1)+k_{H,1}+k_{H,2}+k_{F,1}+k_{F,2}.}
\tag{C7}
\]
没有把第二层当作额外普通 modp 独立核，也没有用 prime-dependent 全局基改变 arch metric。

sorted matching 参数为 θ=(0,1/b,1/b,1/b,1/b,1,1,1,1,1)，故冻结桥给 a_0=b。对 p≤(2−δ)D，原最大 transport 全列 active，cap 正是 \(56/10=28/5\)。同一 pure matrix baseline 正是 \(8-24/10=28/5\)；两个数完全相同。C6 的所有信用窗口包含于此匹配窗口（H 第一层终点2D，其它更小），所以 C7 可以在原 baseline 扣信用。

## 4. balanced 接合、积分及费用

冻结 DVR 桥的 saturated intersection 证明直接用 cap8：对固定 tensor dimension d，tensor floors 合计至少 dR^{d−1} 次 C7，near-balanced primitive restriction 的损失至多8dc，其中 c/R^d→0。实际 balanced leading rows 包含于 V_D^d；因此这是原 polynomial source 的 graded evaluation 信用，而非另一个未经比较的矩阵。

先固定 ε、d、严格窗口 δ、species/degree tolerance，取 D→∞；再按冻结桥取 discrepancy、张量及 δ 极限。删去 p²≤bN_D+O(1) 的小素数只损 o(D²)。全密度 prime sums 的 normalized 信用为
\[
\begin{aligned}
\gamma_H&=3\int_0^2(1-t/2)dt
          +2\int_0^{2/3}(1-3t/2)dt=11/3,\\
\gamma_F&=4\int_0^1(1-t)dt
          +3\int_0^{1/3}(1-3t)dt=5/2,\\
\gamma&=\boxed{37/6}.
\end{aligned}\tag{C8}
\]
沿原 Hilbert–Samuel/source-degree/ordinary arch 归一化，有限费用折扣是 \(2\gamma/m^2=37/300\)，不是 \(\gamma/m\)。于是同一 source 的可认证输入为
\[
\boxed{\kappa_\varepsilon=\frac{99(2+\varepsilon)}{25}+3-\frac{37}{300},
\qquad\kappa_0=\frac{3239}{300}.}\tag{C9}
\]
对应原 CDT 形式为 \(10(\rho-\kappa_\varepsilon)\le J_\varphi\)，这里 J 是 ordinary Jensen。

## 5. 进展与准确限制

本轮把完整 F 的安全列从11降到8；在同一实际 rank10 源上新增 \(\gamma_F=5/2\)，并将原格全部高层信用闭合到成本。C9 是实际改进的安全上界，未证明最优费用。

已证明的 omit1/unique simple0 原 z 叶类仍有 \(\rho\le-\log16\)。C9 与该解析输入没有数值矛盾；原目标 forcing、周期 carrier 和其真实 rank10 全部保留。本文没有证明任何新奇 ζ/L 数值无理性或线性无关性，也没有 Lean 形式化。新几何比较或新整格可继续改进，不能把这张表的失败扩大为所有方法的失败。

本稿为全尺度证明；没有新增有限样本 producer，未用样本检查替代 prime sums 或 DVR 接合。独立审阅及实际阅读范围将另记于 NEW review。
