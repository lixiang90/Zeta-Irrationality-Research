# 第276轮：原X剩余预算、实处包络与到期结算

2026-10-20，完成[276一轮任务](growing_pole_primitive_charter_round276_20261020.md)。根核实际goal为active、git工作树干净及修订16的权威账，恢复AGENTS、长期goal、275证明与决定、269原定义和270实际实处。上一goal turn取得完整预算改善、独审及云端提交，分类为progress。

**结论：同一完整净upper再改善 \(1+9\log2\)，但仍为正；既没有充分负预算，也没有排除全部负子列的裸非负lower。原X一轮重开按期结束，下一轮主动作全路线机会成本比较。** 不把安全族增长或一个正定样本冒充最优本原方法no-go。

## 1. 固定对象和完整反证

保持269 G5唯一
\[
X=\zeta(2)+2G,\quad n=8m,\quad N=8m-1,\quad
p_i(z)=z^i+z^{4m}v_i(z),
\]
\[
M_m=R_m+XI_m>0,\quad
Q_m(Z)=\det(R_m+ZI_m),\quad
\lambda_m=\operatorname{den}(Q_m)\in\mathbf Z_{>0}.
\]
原权、坐标z=1+T、空间、目标系数和尺度没有改变。全部反证仍为实际X=u/v、u∈Z、v>0、gcd=1；此时
\[
0<v^m\lambda_mQ_m(X)\in\mathbf Z.
\]
所需出口是同一预定无界子列上的严格负二次limsup。275旧内容信用已计入row规范，不再扣除。

## 2. 新完整内容：每行实际次数支付全部有理头

[有限处证书C6–C18](growing_pole_content_round276.md)重新核完整商部和U的两处导数，先得到对a≥2、整数分子degree≤2a−2的全部有理头清整
\[
B_a^\#=2^{2a}d_{2a-3}^{\,2}.
\]
普通商最大矩索引为2a−3；proper的奇素数每个幂次由两残基计数支付，2处单独结算。未把一个proper系数当成全部头。

原实际次数 \(\deg v_i=4m-1-i\) 进一步给
\[
r_i=N-i,\quad D_i=2\,4^{r_i}d_{r_i},\quad
h_i=16m-3-2i,\quad E_i=D_id_{h_i}.
\]
逐项核原低低、低高、高高乘积，在每个素数幂上证明
\[
\operatorname{diag}(E_i)R_m\operatorname{diag}(E_i)\in M_m(\mathbf Z).
\]
于是同一首一Q有完整整数多项式
\[
F_m^\#=\Lambda_m^\# Q_m,\quad
\Lambda_m^\#=\prod_{i<m}E_i^2,\quad
c_m^\#=\operatorname{content}(F_m^\#),\quad
\lambda_m=\Lambda_m^\#/c_m^\#.
\tag{276.1}
\]

相对275的row多项式，其全系数内容精确满足
\[
F_m^{\rm row}=L_m^\#F_m^\#,\quad
c_m^{\rm row}=L_m^\#c_m^\#,\quad
L_m^\#=\prod_{i<m}(d_{16m}/d_{h_i})^2\in\mathbf Z_{>0}.
\]
标准LCM渐近给
\[
\log\Lambda_m^\#=(45+30\log2+o(1))m^2,\quad
\log L_m^\#=(2+o(1))m^2.
\tag{276.2}
\]
这是新规范内率2的完整内容信用，不是275的L、首项或单个minor。根逐式独核C6–C20；独审代理回到270/275独立复算，完整读域保存在[独审§6](growing_pole_independent_round276.md)。

## 3. 实际实处：保留Newton阶数与求值放大的互补

[实处证书R4–R12](growing_pole_real_rate_round276.md)没有改变原插值解。它对第i行保留 \(B_{m,i}=\binom{m-1}{i}\) 的真实数据，并由Hermite公式给全部整数1≤x≤N上的明确 \(|F_i(x)|\le E_{m,i}^{\rm real}\)。

原Newton恢复逐系数给
\[
|[z^{M-r}]v_i|\le2^r E_{m,i}^{\rm real},\qquad M=4m-1.
\]
在实际1≤z≤2上，\(2^rz^{M-r}\le2^M\)；先把全部系数都粗付2^M、再付最高次数求值，会丢掉这项互补。保留原阶数后，完整有限m证书是
\[
0<\det M_m\le4^m\prod_{i<m}
\left[1+(M-i+1)2^M E_{m,i}^{\rm real}\right]^2.
\]
统一Stirling误差及
\(\sum_{i<m}\log\binom{m-1}{i}=\tfrac12m^2+O(m\log m)\)
给
\[
\boxed{\limsup m^{-2}\log\det M_m
\le\alpha_{\rm new}:=16\log2+1+32\mathfrak h(1/4).}
\tag{276.3}
\]
相比原实处upper严格改善 \(9\log2-1\)。根独立重建逐阶系数、同区间求值及一致误差；有限处作者与独审代理分别全文复核实处稿。没有用达到单首极小范数的辅助多项式替换原p。

276.1–276.3合并得到本轮最佳完整净证书
\[
\boxed{\limsup m^{-2}\log|\lambda_mQ_m(X)|
\le C_{\rm new}:=46+46\log2+32\mathfrak h(1/4)>0.}
\tag{276.4}
\]
相对于275完整upper，下降恰为 \(1+9\log2\)。算术与实处作用于同一实际对象，两个收益没有重复扣除。

原270实际lower与276.2又给新未约内容安全族
\[
\liminf m^{-2}\log(\Lambda_m^\#\det M_m)
\ge\kappa_\#:=45+16\log2-8\log(3+2\sqrt2)>0.
\tag{276.5}
\]
若某同一子列上成功且负余量δ>0，则必要
\(\liminf m^{-2}\log c_m^\#\ge\kappa_\#+\delta\)。
这不是充分门槛，不证明最优λ失败。276.4仍不准入数值反证。

## 4. 首问题未决：样本、Euler附加约束与有限部纠错

全序列裸lower仍只有
\[
\liminf m^{-2}\log Q_m(X)\ge
-8\log(3+2\sqrt2)-14\log2<0.
\]
因而不能由λ≥1排除所有负二次子列。若全尺度 \(R_m\succeq0\) 成立，确有 \(M_m\succeq XI_m\)，足以给裸liminf≥0；本轮没有证明此提案。

执行前声明用途后，根只对一个固定m=2作[精确重建](growing_pole_actual_diagnostic_round276.py)，[结果](growing_pole_actual_diagnostic_round276.json)通过全部G5定义及四周期栏断言。两个严格正的Sylvester主minor证明 \(R_2\succ0\)。脚本初版的两类节点索引错误被周期断言捕获，修正为j//2后通过，再补全G5定义断言；所有执行均为这同一固定对象，没有m或素数扫描。独审只读源码/JSON，并用Fraction核已有主minor等式，不产生新样本。有限正定证书没有升级为无界结论。

独审作者另从原Hermite约束导出收敛尾部积分：对 \(-1<\alpha<i\)，
\[
2H_i(\alpha)+b_{N-i}(\alpha)
=-\frac{\sin\pi\alpha}{\pi}
\int_1^\infty
\{2v_i(z)+z^{-(4m-i)}\}(z-1)^\alpha z^{-4m}\,dz.
\tag{276.6}
\]
根以逐单项式beta积分独立核此式及其零矩/归一化，见[独审I276.2–4](growing_pole_independent_round276.md)。这些是原对象的真实附加约束，但作用于可变号函数，域延伸到z>2，不能直接给原正Gram的下界。

全半轴Mellin有限部提案也未通过。原proper核的 \(\alpha=1\) 展开在负导数后保留
\[
G_{ij}''(1)+2\zeta(2)G_{ij}(1),\qquad
G_{ij}''(1)=[z^N]L(z)^2p_i(z)p_j(z).
\]
G6没有杀掉额外 \(C_{L^2}\) 栏；初步省略该项的纯常数矩阵式已撤回。有限部亦不保持点态符号，例如
\[
\operatorname{FP}\int_1^\infty-\log T\,(1-3/T^2)^2\,dT=4>0.
\]
所以尾部负权不能直接推出有限部矩阵负半定。这是对一般推理的反例，不是原G5的反例；纠错链见[独审§7](growing_pole_independent_round276.md)及实处稿末。

## 5. 关闭范围、宏观含义与短交接

本轮登记为完整净预算改善，依据是276.1–276.4，不是有限样本、附加结构、文件数或局部反例。数值准入仍false，goal未实现；没有新指定值无理性定理或全球新颖性声明。

同时，276一轮重开按期结束。原sourcekey、270关闭和275有证重开链保留；不能用本轮已记账的率2或实处upper再次自动续期。裸非负lower、原R全m半正定及充分负本原率均未付，没有宣布全部最优本原来源失败。

本轮还明确了后续机会成本：\(\lambda_m\ge1\)，而当前裸实处upper本身为正；即使把安全费用全部约掉，**保持这个绝对值/Hadamard包络**仍不能得到负净率。因此仅在这套包络下继续减算术费用的投入不再有足够的最终接口。重开应有改变真实实率包络的全尺度机制，或已经闭合的同对象严格负预算；只多减一个正费用常数不够。这不是实际裸率非负的证明。

安排[277主动宏观比较](source_gate_charter_round277_20261020.md)，先比较能改变实际实率/余项的来源与证据，避免因累计减费而失去最终目标。最近正式复盘275，完成276后距其一轮、停滞0；主动复盘因窗口到期，未伪报两轮停滞。下一动作和证据只写入program.json并生成STATE。

本轮没有新外部一手输入、Lean构建或全量历史重算。原文献、形式化和冻结资产不变；数学有限证书、已审结构与未付数值条件继续分开。goal运行仍服从用户暂停及工具限额，不因数学困难标blocked/complete。
