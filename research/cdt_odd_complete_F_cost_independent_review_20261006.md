# 完整 F 新8列表与 CDT 费用的独立审阅

日期：2026-10-06。审阅者 quarter_model_review。NEW 记录，旧冻结证明和 producer 均不修改、不执行、不 import。

实际阅读全文[完整 F 成本稿](cdt_odd_complete_F_cost_bridge_20261006.md) C1–C9及§5，包含最终 0<ε<1 参数范围；实际回读[冻结 balanced DVR 桥](cdt_odd_level20_balanced_smith_bridge_20261006.md)全文。此前实际阅读全文的[冻结 H 原格稿](cdt_odd_classical_frobenius_smith_20261006.md)在本次又核对 SHA256 81e995972aead798f8086fdec2fac9e0afd75debcb10fc058e2862b7f185cf64，内容未变。本次另实际提取并读取 [CDT 固定原件](../literature/cdt2024_l2_chi_minus3.pdf) PDF122–123、130、140–143，核对 maximum、HS、arch 与逐 prime finite height 的原归一化。

本独审针对根任务新成本接合；[完整 F 高层稿](cdt_odd_complete_F_high_filtration_20261006.md)由本审阅者本轮另行撰写，不能把这里的复用称为该稿另一名作者的独立验证。该稿全幂层及 packet 的独立审核另由根任务记录。本审阅未执行或读取任何新数学 producer/JSON，故不登记它们的检查状态。

## 1. 同一原 z 整格与全部 finite 地方

C1保留真实 rank10 源与 x=256z。对 odd p，H 四行的安全分母为 odd(Δ₂ₙ₊₁)⁴，F 五行的新安全分母为 odd(Δₙ)⁴odd(Δ₂ₙ)⁴。固定 b=2+ε、0<ε<1 后，H 的2n+1差可在有限初项用 D₀吸收；其余用四个 b columns。F 四个1、四个 b columns，Euler derivatives乘整数 nʲ不增分母，C2的 ν、s=8和列数均准确。

这是 odd-part 安全模型，2处另付旧 V13 的统一前缀清数，其 log=O(logN)。对原 polynomial source 的 R=O(D) 个 graded evaluations，即使逐项全额付费也只有 O(DlogD)=o(D²)。fixed tensor dimension d 时是 O(dDᵈlogD)=o(Dᵈ⁺¹)，D₀的费用更低。原 z 的 H 行2处整；F行有理初值的有限2分母并入 D₀。原 x coefficient 的256⁻ⁿ产生主阶2分母，但本稿始终没有转换到该整格。故原 z 所有地方已计费，没有一个遗漏的 dyadic 主项。

small odd primes与高幂用完整安全 LCM 表的原 bound，其总项仍在 CDT finite 估计内。信用仅删去 p²≤bN_D+O(1) 的 primes：每个新增 count=O(D)、Σ_(p≤O(√D))logp=O(√D)，故删除量 O(D³⁄²)=o(D²)。有限 D₀ primes的信用损失 O(D)，也不改主阶。

## 2. 两组列的 simultaneous maximum

原 CDT (8.0.2) 的统计是 threshold-wise maximum。四个 b 列只要求9条非恒定 species，质量9/10；四个1列只要求其中五条 F，质量1/2。成功 degree 区间分别为 u≥t/b、u≥t，u=n/N_D 均匀。因此任何 coupling 的 payoff 被两项各自上界夹住：

\[
4\min(9/10,(1-t/b)_+)+4\min(1/2,(1-t)_+).
\]

将 constant 放在最低1/10 degrees，H等分中间4/10，F等分最高5/10，同时使非恒定集合为 u≥1/10、F集合为 u≥1/2。它在所有 t 同时达到两项上界，不存在将两个不相容 maximizing couplings相加的缺口。finite species rounding/discrepancy 误差在 CDT 原极限内消失。故 C3 确为完整 maximum。

对质量 a 的成功项，∫₀ᵇmin(a,(1−t/b)₊)dt=b(a−a²/2)。于是

\[
\tau_b=8b(9/10-81/200)+8(1/2-1/8)
=99b/25+3.
\]

C4正确；b↓2时 τ=273/25。这里 prime normalized variable为 t=p/N_D，接合 credit 的 degree-loss积分另用 t=p/D，二者以 N_D~10D转换，未混淆。

## 3. 阈值1/2、5/6及准确 matching 窗口

原 Ψₚ=p⁸eval 的 baseline 是 constant floor8、四条H floor4、五条F floor0，合计24(D+1)。H旧 p⁴H 两层关系乘上额外p⁴，分别进入第5、6阈值；F新 p⁸F 两层进入第1、2阈值。两个块的 supports不同、constant另立；同块第二层嵌入第一层，不被当作额外普通 modp kernel。

可以直接逐阈值看到 C7：第1层至少5(D+1)+k_F,1；第2层至少5(D+1)+k_F,2；第3、4层各至少5(D+1)；第5层至少(D+1)+k_H,1；第6层至少(D+1)+k_H,2；第7、8层各至少D+1。相加即24(D+1)+全部四个k。其 primitive counts的 degree损耗与原导数支持保持一致。

sorted θ为0、四个1/b、五个1。一般 matching 参数实际是 min(b,5)。初阅时指出原只写 ε>0 的范围不足；根任务在 NEW成本稿尚未冻结时已明确修为0<ε<1，本次实际回读最终全文。因此2<b<3<5，最终 a₀=b准确。p≤(2−δ)D时全部positive columns active，原 cap=56/10=28/5，与 pure matrix net baseline 8−24/10=28/5完全相同。H信用窗口端点2D、2D/3，F为D、D/3；全部在该同一原 baseline的严格匹配窗口内。

## 4. cap8 的真实 near-balanced determinant

冻结桥的 DVR 引理只用 capped Smith floors及primitive restriction，并不依赖原 cap等于3。cap8时 tensor每个 floor≤8d，对各 threshold 的 saturated SNF方向与 balanced source求交，rank损失至多 codimension c。累加至8d，得到 actual determinant valuation至少 dRᵈ⁻¹Σβ−8dc。

near-balanced source是原整数 polynomial source张量中的 primitive coordinate submodule，c/Rᵈ→0。实际 full tensor的leading tuples为V_Dᵈ，balanced leading rows取其子集；上述不等式适用于这一真实 square row minor。对 baseline 的 restriction误差及8dc求 primes后，原规定 fixed tolerance先D→∞、再tensor limit、最后tolerance→0可令误差消失。局部 Smith basis无需保持 species，也没有作为一个新 arch basis使用。

按 C6准确截断次数，prime number theorem/partial summation给

\[
\gamma_H=3\int_0^2(1-t/2)dt
+2\int_0^{2/3}(1-3t/2)dt=11/3,
\]
\[
\gamma_F=4\int_0^1(1-t)dt
+3\int_0^{1/3}(1-3t)dt=5/2,
\quad\gamma=37/6.
\]

常数 degree shifts只给 O(D)而非D²。tensor信用除原 d·10ᵈDᵈ⁺¹主阶后为 γ/10；这里没有素数 residue-class密度因子，所有 sufficiently large odd primes均使用相同关系。严格2−δ窗口最后δ↓0保留上述积分。

## 5. HS、arch 移项及 κ 的含义

原 PDF130的(8.2.6)给普通 source的normalized degree J_φ/2；PDF140的(8.2.28)在无subradius correction时给 −10ρ/2+J_φ；PDF142的(8.2.34)给 finite baseline 10τ_b/2。新同源determinant信用减去 γ/10。由 slope inequality

\[
J_\phi/2\le-10\rho/2+J_\phi+10\tau_b/2-\gamma/10,
\]

乘2移项即10(ρ−κ_ε)≤J_φ，

\[
\kappa_\varepsilon=\tau_b-\frac{2\gamma}{10^2}
=\frac{99(2+\varepsilon)}{25}+3-\frac{37}{300},
\quad \kappa_{0+}=\frac{3239}{300}.
\]

C8/C9及37/300的最终归一化通过；γ/10是高度信用，不能直接当作最终κ折扣。这个κ是实际原z、普通metric、新8列安全表的可认证上界，没有证明必要下界或最优值。

已认证的该原z叶类ρ≤−log16，仍不给数值矛盾。此失败限定于列明源/表/叶/metric，不排除其它整格、真实周期消除或解析叶。通过的进展是完整F新信用确实进入CDT原格成本；不是新的ζ/L数值无理性或线性无关性结果。

## 6. 最终审阅状态

最终 C1–C9通过，前提为实际修订后的0<ε<1。已核maximum同时可达、全部places原z费用、H/F分离与nested阈值、matching baseline、cap8 saturated near-balanced determinant、prime sums、ordinary HS/arch移项及3239/300。没有执行、import、修改任何数学 producer，也没有以有限检查或green manifest替代这些全尺度证明。

本稿只新增成本独审证据，不改变既有冻结稿。原source的最小rank、全幂层F模型及局部packet各依赖其明确独立输入，不因这里费用接合通过而自动变成新数值定理或Lean证明。
