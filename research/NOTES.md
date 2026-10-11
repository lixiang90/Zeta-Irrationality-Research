# ζ(7) 无理性研究笔记

状态：**b=8 可行性判定已完成**（见 `b8_verdict.md`，终稿 2026-09-24：
最优轨道可行、论文 γ-界轨道需再工程）。本笔记保留攻关过程的推导与验证记录。

## 1. 类比构造（已推导）

对任意导数阶 a，权 w(y) = (2π)ᵃyᵃ⁺¹f⁽ᵃ⁾(y)/(a!/2)（f = 1/(e^{2πy}−1)）给出：

- **多项式矩恒为有理数**：μ(t^e) = (−1)ᵉB_{2e+2}·∏_{i=3}^{a+1}(2e+i)/a!（ζ(2e+2) 经 Euler 公式消去 π——该方法的核心奇迹，对一切 a 成立）。
- ζ(7) 只经极点值进入。经六次分部积分：(d/dy)⁶[y⁷/(y²+a²)] = −720a⁶·Re(y−ia)⁻⁷。

## 2. ζ(7) 极点值：**精确闭式已建立**（修正版）

**【重大更正】** 2026-09-23 早间版报告的"边界残差 r(a) ≈ −0.0507/a²、含非初等
常数、构成 p-adic 障碍"**系脚本 bug**：Σ_l l⁶q^l 的 Eulerian 闭式分母为 (1−q)⁷
（上一版误写 (1−q)⁶）。修正后残差完全消失，"π 污染"担心不成立。

**工具**：DLMF [25.11.29](https://dlmf.nist.gov/25.11.E29)（Hermite 公式）：
2∫₀^∞ f(y)·Im(a−iy)⁻ˢ dy = ζ(s,a) − a^{1−s}/(s−1) − a⁻ˢ/2。
六次 IBP 边界干净（u = y⁷/(y²+a²) 在 0 有 7 阶零点），配合上式得**精确恒等式**：

  **I7(a) = a⁶ζ(7,a) − 1/(2a) − 1/6**（60 位数值验证通过；`zeta7_pole_values.py`）

**μ 泛函极点值**（与论文式 (2.3) 完全同构）：

  **μ_{7,X}(1/(t+j²)) = j⁶(X − H_j⁽⁷⁾) − 1/6 + 1/(2j)**

→ 极点数据全为有理数/H⁽⁷⁾，Fauzan §3–5 的 ℚ_p 机器**在数据层面无障碍**。

**τ-机器 b=8 恒等式（数值验证通过）**：
τ₈(x^m) = m(m−1)(m−2)(m−3)(m−4)·B_{m−5}/720 满足
τ₈((x+1)^e − x^e) = [e≥6]·e!/(e−6)!/720（e = 5,6,7,8,10 全部精确）。
**约定陷阱**：τ 的 κ_d 必须取 **B₁ = +1/2（经典约定）**；论文声明的 "B₁ = −1/2"
仅适用于 μ-矩公式（偶数指标 B，约定无关）。论文未写清此分工。

**【对 Lean 项目的重要发现】**：`eq_3_3_poly` / `eq_3_2_poly` 的 μ-世界字面
陈述**为假**（(3.2)/(3.3) 属于 τ-世界；μ(P(X+1)−P(X)) ≠ C(P⁗(0)/24)，
反例 P=X⁴：LHS = 121/12 ≠ 0）。两个 sorry 目标需重述（τ 版本或 pullback
形式），否则填补必败。

## 3. 实侧常数探针（对数能量比较测度，Lemma 6.1 类比）

校准：用论文 Table 1 的 ρ 复算，I(ρ)、C_* 与论文 9 位数字吻合；直方图+SLSQP 优化器
b=6 得 −2.56（论文证书 −1.367，其 ρ 未优化、为有理证书牺牲）。

(α, λ) 扫描（b=8，ζ(7) 类比；min f = λM₀ − I(ρ) + C_*）：

| b | α | λ | min f |
|---|---|---|---|
| 8 | 0.075 | 0.925 | −1.54 |
| 8 | **0.050** | 0.925 | **−2.38** |
| 8 | 0.100 | 0.925 | −0.79 |
| 8 | 0.050 | 0.850 | −2.05 |
| 8 | 0.075 | 0.850 | −1.29 |
| 6（控制） | 0.075 | 0.925 | −2.40 |

**结论**：调小 α（N/K 比）后 b=8 实侧常数与 b=6 持平（≈ −2.4），且趋势指向更小的 α。
实侧不是瓶颈；ζ(7) 的全部难度集中在算术侧（A_*₈ ≈ 1.8–2.2 需 < |Ū₈| ≈ 2.4）。

## 4. 下一步（按优先级）

1. **b=8 算术侧重做**（核心，论文 §3–5 的推广，数据已确认干净）：
   - 分布公式 τ(g) = p^{−6}Σ_{a=0}^{p−1}τ_Y(g(a+px))（b=6 时为 p^{−4}）；
   - 小素数界 (3.12)-类比：v_p^G ≥ −8h⌊log_p(5K)⌋ − h·v_p(720)；
   - 内区/外区权重分配（b(x,z) = 4ℓ(αx,z)，权重 (ℓ+6)/2 等）与 Lemma 4.2 类比
     （秩损失 min(r,z) 的折损需重算——mo271 的偏差记录提示此处有 9/640 量级的坑）；
   - 在新 α（≈0.05）下重新调谐 (K:N:h) 比例。
2. α → 0.03–0.04 的更深实侧扫描，与算术侧联动。
3. 若 1–2 闭合，启动 mo271 式证书管线（其 scripts/ 的 b=8 版本）。
4. Lean 侧：~~重述 eq_3_2_poly/eq_3_3_poly 为 τ-世界版本~~
   **【2026-09-24 进展】τ₈ 侧两个核心 sorry 已消灭**（`Zeta7Formal/Zeta7/Tau.lean`）：
   - `kappa_difference`（式 (3.3)-类比）：∑_{k<e} C(e,k)κ(k) = [e≥6]·e!/(e−6)!/720
     完整证明。路线：mathlib 的 `sum_bernoulli'`（Bernoulli 二项和 = n）+
     `(k)₅·C(e,k) = (e)₅·C(e−5,k−5)` 折叠（`choose_mul_factorial_mul_factorial`），
     比生成函数系数比较更短；`kappa_egf`（解析版，Real.exp）保留为独立目标。
   - `kappa_val`（式 (3.10)/(3.12) 分量的 von Staudt 界）：p ≥ 7、d ≥ 5 时
     v_p(κ_d) ≥ −1 完整证明。路线：mathlib 的 von Staudt–Clausen
     （`Bernoulli.vonStaudt_clausen`）+ `padicValRat.min_le_padicValRat_add`
     超度量不等式（修正和每项为正 ⇒ 部分和 ≠ 0，绕开零和尴尬）。
   - `Main.lean` 的 `tau8_difference`（原带 `-κ e` 尾项，**证伪**：e=6 时 1/2 ≠ 1，
     已按数值验证重述）与 `kappa_valuation` 均已接为上述定理的推论，sorry 清空。
   - 桥引理：`bernClassic = bernoulli'`（B̃₁=+1/2 约定），`bernoulli'_eq_ite`。
   - 剩余 sorry：`pole_value_exact`（需 Hermite 公式 s=7 的 mathlib 化）、
     `main_estimate`（判定层主定理）。
   **【2026-09-24 进展 2】`harmonic7_valuation` 已消灭**
   （`Zeta7Formal/Zeta7/Harmonic.lean` 的 `harmonic7_val_aux`）：
   v_p(H_j⁽⁷⁾) ≥ −7⌊log_p j⌋ 对任意素数 p 完整证明。路线：对 j 归纳，
   单项界由 `Nat.divMaxPow_mul_pow_padicValNat`（p^padicValNat ∣ n）+
   `Nat.le_log_iff_pow_le` 给出，合并用 `padicValRat.min_le_padicValRat_add`
   超度量不等式（和为零时 RHS ≤ 0 单独处理）。
   **【2026-09-24 进展 3】`kappa_egf` 已消灭**（重述为形式幂级数版）：
   - 陈述：`C 720 · (Σ κ(m)/m!·tᵐ) = t⁵ · bernoulli'PowerSeries`（ℚ⟦X⟧），
     逐项系数比较（`factorial_five`：720·κ(j+5)/(j+5)! = B̃_j/j!），
     无 sorry（`Zeta7Formal/Zeta7/Tau.lean`）。
   - 推论 `kappa_egf_mul_exp`：`720·F·(e^t−1) = t⁶·e^t`，即解析闭式
     `t⁶/(720(e^t−1)) + t⁶/720`（`b8_machinery.py` §1 验证）的有理重写；
     原 tsum/Real.exp 解析版陈述不再需要（收敛-延拓论证属分析侧，另行处理）。
   - 数学内容：EGF 侧就此闭合——τ₈ 三条恒等式（差分、von Staudt 界、EGF）
     全部形式化完成。
   **【2026-09-24 进展 4】b=8 算术侧 · 分布公式已严格推导并精确验证**
   （`b8_arithmetic.md` §B2 + `research/b8_distribution.py`）：
   - 命题 1（几何和）：Σ_a e^{at}F₀(pt) = p⁶F₀(t)（B₁=−1/2 EGF），
     对任意正整数 p（不必素）严格成立；命题 2（系数比较）得多项式版
     τ⁻(g) = p^{−6}Σ_a τ⁻(g(a+pX))。
   - **约定陷阱（修正早先推测）**：plus 约定修正项
     c6(g) − Σ_{n≥6}C(n,6)S_{n−6}(p)c_n(g)（幂和 S）对奇 g **不消失**
     （x⁷, p=2 给 −7）；构造适用版为 p⁶τ(g) = Σ_a τ⁻(g(a+pX))，
     RHS 钉死 minus 约定（LHS 对奇 g 约定无关）。
   - 精确验证（纯 Fraction，无浮点）：核心恒等式 1640 例（p=1..40 含合数、
     m=0..40）+ 修正项公式 780 例 + 构造版 780 例，全部零违规。
   - Lean 登记：`Zeta7Formal/Zeta7/Distribution.lean`（`tauPoly`/`tauPolyMinus`/
     `kappaMinus` 定义 + `distribution_odd` 目标陈述，含证明路线）。
   **【2026-09-25 进展 5】C_p 精确式与 p-进赋值界已钉死**
   （`b8_arithmetic.md` §B3 + `research/b8_cp_shift.py`，全节零违规）：
   - 命题 1（Hurwitz 整数部提取）：H⁽⁷⁾_{a+pr} = ζ(7) − p^{−7}Σ_{c=1}^{p}ζ(7,r+c/p)
     + Σ_{v=pr+1}^{pr+a}v^{−7}（p 不必素；拆成整数部提取 1a + 乘法公式有限形式 1b
     两个精确有限恒等式验证，p=3..13 全组合零违规）。
   - 命题 2（Y-位移分解）：p⁷H⁽⁷⁾_{a+pr} − H⁽⁷⁾_r = (p⁷−1)ζ(7) + E_a(r)，
     E_a(r) = O(r^{−7}) 数值同阶确认；(p⁷−1)ζ(7) 被机器 Y = p⁷X + C_p 吸收。
   - 命题 3（C_p 精确式）：C_p = −Σ_{a=1}^{p−1}Σ_{k≥0}C(k+5,5)B_k(a/p)^{−k−6} ∈ ℤ_p，
     逐项 v_p ≥ k+5（von Staudt）p-进收敛；渐近系数恒等式
     6·(B_{2k}/(2k)!)·(7)_{2k−1} = C(2k+5,5)B_{2k} 精确验证（k≤11）。
   - 赋值定理：p > 7 ⟹ v_p(C_p) = 7；v_7(C_7) = 6 **精确**（退化素数，
     Σa^{−6} ≡ −1 mod 7）；v_5 = 7、v_3 = v_2 = 6。精确分数合并计算
     （p ≤ 97 全素数，余项 k≥11 的 v_p ≥ 16 严格隔离）零违规。
     b=6 对照：退化素数 p=5 给 v_5=4，与机器 p ≥ 7 排除相容。
   - 机器含义：p=7 的半阶损失归入 §C.6 小素数界 (3.12)-类比的 7-adic 成本；
     与 DirectBound 路线相容（C_p 只需以赋值界形式进入 Lean）。
   - 诚实声明：与论文 (3.5) 的逐字对应是推断（论文原文本地不可得），
     登记「待论文核对」。
   **【2026-09-25 进展 6】b=8 版 (3.12)-类比逐项损耗表已钉死**
   （`b8_arithmetic.md` §C7 + `research/b8_small_prime_loss.py`，全节零违规）：
   - 四项损耗逐一精确验证：①极点阶乘比 ≥ −⌊log_p 2K⌋（闭式
     ∏_{s≠r}(r−s) = (−1)^{K−ρ}(K−ρ)!(K+ρ)!/ρ，digit-sum 证 + 直接乘积复核，
     锋利：p=2,K=3,r=3 与 p=7,K=6,r=6 精确取等）；②调和主部
     ≥ −7⌊log_p j⌋（p ≤ 97、j ≤ 1500 零违规，j = pᵐ 精确取等）；
     ③κ 归一化 ≥ −(1+v_p(720))；④C_p ≥ −v_p(C_p)（复算 §B3）。
   - 常数表：路线 A（分布公式）L_p = 1+v_p(720)+v_p(C_p) = (11,9,9,7,8)，
     p = (2,3,5,7,≥11)，一致上界 11；路线 B（DirectBound，mo271 策略）
     L_p^B = 1+v_p(720) = (5,3,2,1,1)，一致上界 5。b=8 版 (3.12)：
     v_p^G(F_K) ≥ −8h⌊log_p(c_{α,λ}K)⌋ − h·L_p。
   - 经验复核：184 个 hankel 全量数据点（n=1..6）对加强界
     −8h⌊log_p 5K⌋ − h·L_p 最小余量 454 ≫ 0，零违规；常数不构成额外风险。
   - 过程修正：初版用浮点 log 取整在 j = 243 = 3⁵ 出假违规，已全部改
     精确整数 ilog（同类型隐患清除）；极点闭式的负 r 符号差与赋值无关，
     复核改比对绝对值。
   - 待办（§C8）：论文逐项结构核对；Lean 侧登记 b=8 版 DirectBound
     目标陈述（VG_H7、VG_res 平移、合成界 min_c(e_c−ℓ_c) − 6）。
   **【2026-09-25 进展 7】b=8 DirectBound 骨架已建并编译通过**
   （`Zeta7Formal/Zeta7/Arith/DirectBound.lean`，`lake build` 8710 jobs
   成功，3 条登记 sorry）：
   - 结构（镜像 mo271 `Apery/Arith/{Val,DirectBound}`）：一、极点函数定义
     （piPl/polyPart/resP/dd/tauX8/numOf/cnt/plc/Sep，tauX8 用 tauPoly+H7）；
     二、VG/GV 赋值工具箱；三、整数赋值与留数界；四、VG_H7；五、合成链目标。
   - **已证**：VG/GV 全部代数（zero/mono/add/sub/mul/sum/prod/intCast/inv/
     of_eq/primePow、GV 全套）、`VG_res`（留数界 e_c−ℓ_c+1，b-无关纯移植）、
     **`VG_H7`（j < p² ⟹ v_p(H⁽⁷⁾_j) ≥ −7，由 harmonic7_val_aux 合成——
     b=6 的 VG_H5/−5 的 b=8 平移，损耗表 §C7 第②行正式入 Lean）**、
     `padicValNat_720`（p ≥ 7 ⟹ v_p(720) = 0，机器素数区）。
   - **登记 sorry（附证明路线）**：`tauPoly8_bound`（b=8 版 tau_bound：
     β − 7⌊log_p(d+1)⌋ − (1+v_p(720))，需移植 BinomBasis 的 BinRep 机制）；
     `VG_polyPart_eval8`（移植 DirectPoly.lean，b-无关）；`tauX8_direct`
     （合成界 GV(τ₈,X g) ≥ min_c(e_c−ℓ_c) − 6，−6 = −7+1）。
   - 编译修正：`Mathlib.Algebra.Polynomial.Eval` 在本版 Mathlib 不存在
     （改 `Eval.Defs`）；`Nat.log_lt_of_lt_pow` 签名首参为 `y ≠ 0`（真数），
     m = 0 分支单独处理；移植笔误 `Finset.mem_of_mem` → `mem_insert_of_mem`。
   - 下一步：先灭 `VG_polyPart_eval8`（纯移植），再 `tauPoly8_bound`。
   **【2026-09-25 进展 8】VG_polyPart_eval8 已消灭**（DirectPoly.lean 完整移植，
   编译 8710 jobs 通过，文件剩 2 条 sorry：tauPoly8_bound、tauX8_direct）：
   - 移植清单（全部 b-无关，原样落地）：pole 定义链 `piPl_monic`/
     `natDegree_piPl`/`lagrange_basis_eq`/`partial_fractionsP`（Lagrange 插值，
     需加导入 `Mathlib.LinearAlgebra.Lagrange`）；IntPoly 工具 `VG.pow`/
     `VG.eval`/`VG.eval_zero`/`GV.pow`/`GV.comp`/`GV.divByMonic_X_sub_C`/
     `GV.multiset_prod`/`factor_roots`；DirectPoly 复合引理组 `prod_erase_split`/
     `GV_lin_comp_class`/`GV_lin_comp`/`GV_numOf_comp`/`lin_comp_eq`。
   - 主证明（约 170 行）按类分裂 `A = Πc·H + Πo·I`（hAHI）→ Part A 直接估值
     `P(m) = H(m)/Πo(m) − Σ res_r/(m−r)` → Part B 代换 `x = m+pz` +
     `factor_roots` 分解得 `v_p(H(m)) ≥ e−ℓ` → Part C 合并，与 b=6 逐行对应。
   - 移植排错记录：漏移植 `VG.pow` 与 `GV.prod` 两处（后者报错形态是
     `GV.prod` 被解析成 `Function.prod`，提示「参数名 p 不存在」——
     命名空间内缺名时优先怀疑漏移植而非名称解析怪癖）。
   - 下一步：灭 `tauPoly8_bound`（移植 BinomBasis 的 BinRep 机制，
     导数链 3→5、24→720），随后 tauX8_direct 纯组装即可闭合。
   **【2026-09-25 进展 9】BinomBasis/TauBound 移植完成，tau8_bound 已证**
   （DirectBound.lean 编译 8710 jobs 通过；全项目剩 3 条 sorry：Distribution
   1 + DirectBound 的 `tauPolyMinus_eq_tau8`、`tauX8_direct`）：
   - 决定**不走 tauPoly↔Lb 桥接**，镜像 mo271 直接用 Lb 定义
     `tau8 P := Lb (derivative^[5] P) / 720` 并证 `tau8_bound`；
     `tauX8` 的定义从 `tauPoly` 换成 `tau8`。桥接恒等式
     `tauPolyMinus_eq_tau8` 登记为 sorry（连接 Distribution 世界时才需要）。
     安全性论证：kappaMinus m = kappa m − [m=6]，kappa 用 bernoulli'
     （B₁=+1/2）；由 bernoulli'_eq_ite 得 kappaMinus m = (m)₅·bernoulli(m−5)/720
     全 m 成立（m=6 用 bernoulli_one 验证 −1/2 = −1/2），两边同为
     Lb(P⁽⁵⁾)/720 型线性泛函。
   - **常数修正（重要）**：此前登记的 `7⌊log_p(d+1)⌋ + (1+v_p(720))` 是
     **高估**。BinRep 机制实际给出 `6⌊log_p(d+1)⌋ + v_p(720)`：5 次求导
     各损失 ≤⌊log_p⌋（5 份）+ Lb 损失 ⌊log_p(d+1)⌋（1 份）= 6；b=6 同构
     为 3+1=4。von Staudt 的 −1 被 Lb 项吸收，`+1` 常数不存在。
     tau8_bound 陈述：`VG p (tau8 P) (β − 6·Nat.log p (d+1) − padicValNat p 720)`。
   - 移植清单：Lb 全套（add/smul/C_mul/monomial/X_pow/sum/neg/sub/shift）、
     bin 全套（eval_nat/zero/eval_zero/comp_add_one、Pascal）、dcoef、
     derivative_bin、newton、BinRep 机制（derivative_bin'/VG_dcoef/
     BinRep.derivative/Lb/mono/binRep_of_values）、VG_inv_720、VG.inv_nat。
     新导入：ForwardDiff、Pochhammer、Bernoulli。
   - 编译排错记录：Lb_smul/Lb_monomial 必须逐字用 mo271 原文（unfold Lb +
     sum_smul_index/sum_monomial_index，改写版全失败）；漏移植 VG.inv_nat
     （在 mo271 是 Val.lean 而非 BinomBasis）；tau8 定义依赖 Lb，须置于
     Lb 之后（tauX8 一并下移）；`exact this.mono (by linarith)` 出现
     元变量未赋值（改 `refine this.mono ?_; linarith`）。
   - 下一步：灭最后一条 DirectBound sorry `tauX8_direct`（纯组装：tau8_bound
     + VG_polyPart_eval8 + VG_H7 + VG_res，β − 6；镜像 mo271 DirectPoly 末尾
     tauX_direct）。



   **【2026-09-25 进展 10】tauX8_direct 已证——DirectBound 全部主定理闭合**
   （编译 8710 jobs 通过；全项目剩 2 条 sorry：Distribution.lean:53（早期登记）、
   `tauPolyMinus_eq_tau8`（桥接））：
   - 纯组装，逐行镜像 mo271 `DirectPoly.lean` 末尾 `tauX_direct`：tauX8 展开为
     C(tau8 polyPart) + Σ C(res_r)·(C(H7)−X)；第一部 tau8_bound（d = Z.card −
     Pl.card，hdeg ⟹ ⌊log_p(d+1)⌋ ≤ 1，padicValNat_720 消 720 项）给
     ≥ β − 6；第二部 VG_res（e_c−ℓ_c+1）× VG_H7（−7）+ hβ 给 ≥ β − 6。
   - 补移植 `natDegree_numOf_le`（mo271 DirectPoly:247，b-无关）。
   - 里程碑意义：b=8 小素数界 (3.12)-类比的单步核在 Lean 中完整成立
     （GV(τ₈,X g) ≥ min_c(e_c−ℓ_c) − 6，p ≥ 7）。§C7 损耗表第 ①③ 行
     （二项表示 6·log + 720 分母）与第 ② 行（调和 −7）+ 留数 +1 全部入 Lean。
   - 下一步选项：(a) 灭桥接 `tauPolyMinus_eq_tau8`（单项式 + bernoulli'_eq_ite，
     连 Distribution 世界）；(b) Distribution.lean:53 的早期登记 sorry；
     (c) 回到算术侧推进 §D 行列式界 (K:N:h) 重标定。
   **【2026-09-25 进展 11】桥接 tauPolyMinus_eq_tau8 已证——DirectBound 世界与
   Distribution 世界接通**（编译 8710 jobs 通过；**全项目只剩 1 条 sorry**：
   Distribution.lean:53 的早期登记目标）：
   - 证明结构：tau8 线性引理组（`iterate_derivative_five_add`/`_C_mul`
     （内向外逐层 map_add/derivative_C_mul）、`tau8_zero`/`tau8_add`/`tau8_C_mul`）
     + `tau8_eq_sum`（as_sum_support_C_mul_X_pow 逐项取值）⟹ 归约到单项式核
     `kappaMinus_eq_tau8_X_pow`：`tau8 (X^i) = (i)₅·B_{i−5}/720`
     （iterate_derivative_X_pow_eq_natCast_mul + Lb_C_mul/Lb_X_pow）对
     kappaMinus 按 i<5 / i=6 / i≥5≠6 三分（i<5 用 descFactorial_eq_zero_iff_lt；
     i=6 用 norm_num + bernoulli_one 算出 −1/2 = −1/2；主情形乘积用
     prod_Ico_eq_prod_range 对 descFactorial_eq_prod_range + prod_range_reflect
     + cast_prod 逐项 omega）。
   - 新导入：`Mathlib.Algebra.Polynomial.Degree.Support`、
     `Mathlib.Data.Nat.Factorial.BigOperators`。
   - 排错记录：`bernoulli_one` 有 Polynomial.bernoulli_one 歧义（须写
     `_root_.bernoulli_one`）；descFactorial 的乘积表示在 Nat.cast 之下，
     reflect 后须补 `Nat.cast_prod` 把 cast 推进乘积内才能 prod_congr。
   - 下一步：Distribution.lean:53（分布恒等式本体：p⁶·τ(g) = Σ_a τ⁻(g(a+pX))，
     EGF 管线，kappa_egf 已完成后的合成步骤）。
   **【2026-09-25 进展 12】distribution_odd 已证——分布恒等式全链入 Lean；
   pole_value_exact 已证——Main.lean 只剩 main_estimate 一条终极 sorry**
   （Distribution.lean 编译 3053 jobs、全项目 8944 jobs 通过）：
   - 分布恒等式证明链：minus 约定函数方程 `kappaMinus_egf_mul_exp`
     （720·B⁻(eᵗ−1)=t⁶，κ⁻ 分拆 + kappa_egf_mul_exp 消 eᵗ 项）→
     rescale 标度版（纯 RingHom 运算，exp^p = rescale p exp）→
     `distribution_series`（两边乘 eᵗ−1，几何和坍缩 + 整环消去）→
     `distribution_power_sum`（取系数 m，antidiagonal→range 转换 +
     C(m,j)·j!·(m−j)! = m! 归并阶乘）→ tauPolyMinus 线性性四引理
     （X_pow/C_mul/add/sum）+ `tauPolyMinus_comp_lin`（二项展开）→
     `distribution_minus`（一切 g 成立）→ `distribution_odd`（奇性
     ⟹ tauPoly = tauPolyMinus，第 6 项两约定差不参与）。
   - pole_value_exact（式 (2.3)-类比）改走纯代数路线证毕，无需 DLMF
     25.11.29：P = D j/(X+j²) = D(j−1) 次数低于 D j（商部为零）；
     i<j 极点处分子分母同 0（ℚ 中 0/0=0，项消失）；i=j 处由
     D j = (X+j²)·D(j−1) 求导得残差恰 1。矩表示（Euler 消 π）由 μX
     构造定义层承担，与 Apery.μX 同构。
   - 排错记录：(a) rw 关联链用显式参数限定命中位置（mul_assoc/mul_comm）；
     (b) `set` 折叠的局部变量会让后续 rw 匹配显式项失败——恒等式证明中
     尽量写显式项；(c) PowerSeries.coeff 是 bundled 线性映射，用
     map_sub/map_sum；(d) coeff_mul 的 antidiagonal 转换用
     `Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk`；(e) `Finset.sum_comm'`
     带 ∀-iff 侧条件，无条件交换用 `Finset.sum_comm`；(f) 二项定理
     `add_pow` 输出形态为 x^m·y^(n−m)·↑choose（choose 最后且为 ℕ-直cast），
     链首需 mul_comm 归位 + ← map_natCast 化 C 形；(g) 含阶乘分母的域恒等式
     `ring` 关不掉（原子 a·a⁻¹ 不化简），field_simp 用上下文的 ≠0 假设
     清分母后自洽；(h) `exact_mod_cast` 在 term 位置必须包 `by`；
     (i) rw [def] 依赖 equation lemma，def 展开优先 `conv` + rw [D] 组合。
   - 里程碑意义：b=8 分布恒等式（§B2 命题 2 + 推论）在 Lean 完整成立；
     判定层入口 pole_value_exact 闭合。**全项目仅剩 main_estimate**
     （终极主估计，依赖 Degree/Positivity/Normalization/RealBound 全链，
     镜像 mo271；doc 中已登记依赖链与常数调谐状态）。
   - 下一步：main_estimate 链的第一步——镜像 mo271 Degree.lean 建
     Zeta7/Degree.lean（b=8 版 μX_eq：μX K P = C(Σ res·j⁶)·X +
     C(μpoly 商部 + Σ res·(−j⁶H⁷_j −1/6 +1/(2j)))，纯代数恒等变形 +
     natDegree ≤ 1 + coeff_μX_one）；或回算术侧 §D 行列式界 (K:N:h) 重标定。
   **【2026-09-25 进展 13】`Zeta7/Degree.lean` 建成——式 (2.9)-类比（deg Δ = deg F = 37n）
   在 Lean 完整成立**（一次编译通过，全项目 8945 jobs）：
   - 逐行镜像 `Apery.Degree`（mathlib rev 一致 0df444a，引理名零改动），b=8 差异点
     仅三处：极点值权重 j⁴→j⁶（poleValue_eq/μX_eq/coeff_G_one）、D_N 幂 6→8
     （weight/coeff_G_one）、常数 −1/4→−1/6；`μX_eq` 用同一 simp only 集
     （mul_add/←mul_assoc/←C_mul/sum_add_distrib/←sum_mul/←map_sum/C_add）+ ring 收拾。
   - 全部引理 mathlib 原生：coeff_prod_of_natDegree_le、natDegree_sum_le_of_forall_le
     （BigOperators）、compute_degree!、vandermonde 系、derivative_prod_finset、
     Finset.sum_Ico 系；node/weight 定义 (K:N:h)=40:3:37 与 b 无关。
   - 里程碑意义：main_estimate 链第一块砖落地——G_K(X) 条目仿射性、X-系数矩阵
     = Vᵀ diag(w) V、Δ/F 次数恰为 37n 全部就绪（Q.natDegree = 37n 条件已备）。
   - 下一步：镜像 mo271 `Positivity.lean`（aeval_μX 实侧表示 + 正性），
     或回算术侧 §D 行列式界 (K:N:h) 重标定（判定 b8_verdict.md 指出 α 需
     0.03–0.05，Constants 层参数化将影响 Normalization/RealBound 的镜像方式）。

   **【2026-09-25 进展 14】`Zeta7/Positivity.lean` 建成——矩表示 + `Δ_n(ζ(7)) > 0`
   全链闭合，全项目仅剩 `main_estimate` 一条 sorry**（lake build 8954 jobs 通过）：
   - 逐行镜像 `Apery.Positivity`，b=8 差异点四处：极点值 j⁴→j⁶、−1/4→−1/6
     （pole_moment/aeval_μX，引理名仍 hermite_pole）；权重幂 6→8（ν/integrand_eq/
     Δ_pos 内所有 `D (3n)^6`→`D (3n)^8`）；`w_le` 常数 32y+11 → **128y+41**
     （integrableOn_pole 的 hg 控制函数，常数必须照抄 Weight.lean，不可用 s=5 值）。
   - **mo271 模板第四、五处潜伏 bug（本轮实锤）**：
     1. `integrableOn_pole` 依赖的 `integrableOn_pow_mul_exp_neg_mul` 在 mathlib
        不存在；正解是 `integrableOn_rpow_mul_exp_neg_mul_rpow (hs)(hp)(hb)`，输出
        `x ^ s * exp (-b * x ^ p)` 为 rpow 形式，需 simp [Nat.cast_*, Real.rpow_*,
        pow_*] + congr 1; ring 化回目标的多项式幂形式（e=0/e=1 两版）。
     2. `Δ_pos` 的 `set M := (G n).map (aeval zeta7)` 后 `hentry := fun i j =>
        (moment_rep _ _).2` 依赖的 defeq 展开在本 mathlib 上要么超时要么失配
        （whnf >800k 心跳）；修法是去掉 set，全程显式写 `((G n).map (aeval zeta7)) i j`，
        hentry 用 `intro i j; rw [Matrix.map_apply]; exact (moment_rep _ _).2`，
        并在 Δ_pos 顶部加 `set_option maxHeartbeats 800000 in`。
   - 里程碑意义：Proposition 2.2-类比（s=7 矩表示）与正性判定（外区/中区
     估值所需的 Δ_pos 前提）全部入 Lean；main_estimate 的依赖链
     Degree ✓ / Positivity ✓ / Normalization / RealBound / MainEstimate
     已两块砖落地。
   - 下一步：`Zeta7/Normalization.lean`（Δ 的既约分解 S_K^? · F_K 与系数界），
     或先做 `Zeta7/Constants.lean` 把 α（(K:N:h) 重标定 0.03–0.05）参数化
     以免 Normalization 返工。

   **【2026-09-25 进展 15】`Zeta7/Normalization.lean` 建成——§5 归一化参照层落地，
   (3.12)-类比常数入 Lean**（一次编译通过，全项目 8955 jobs）：
   - 镜像 `Apery.Normalization`（mo271 自述该文件仅为参照 + `vS` 通道，证明实际走
     `Norm.lean` 的已证界）。b=无关部分逐行照搬（ellA/InnerData 骨架/rank/eps/
     T/E/total、mKM 与 mKM_pos）。
   - **b=8 活常数**：`Lp` 第一分支（(3.12)-类比）换为
     `−8h⌊log_p 5K⌋ − h·v_p(720)`（§C7/D 钉死；8 = 7+1 的 1 并入 log 系数，
     与 Arith/DirectBound 已证单步核 `GV ≥ min_c(e_c−ℓ_c) − 6` 同构）。
   - **REF(b=6) 冻结**：γ 机器 `gammaIn` (4.8) / `gammaOut` (4.14) 及 `w`/`w0`/
     `L0` 的 b=6 常数原样保留并逐处 `-- REF(b=6)` 标注——`b8_verdict.md` 判定
     论文 γ-轨对 b=8 不可行、需 mo271 式再工程（mo271 对 b=6 亦修正三处），
     b=8 类比常数在 `Norm.lean` 镜像时按已证界重建后同步替换。`vS` 直接消费
     本库 `Construction.S`（b=8 结构 `(N!)^{16h}` 已就位）。
   - 里程碑意义：main_estimate 链 Degree ✓ / Positivity ✓ / Normalization(参照)✓
     / Norm(实归一化) / RealBound / MainEstimate；算术树剩余 ≈5000 行
     （mo271 `Apery/Arith/*` + `Legendre.lean`），本库已先行落地其中
     DirectBound 一支（§C7 损耗表 ①②③ 入 Lean）。
   - 下一步：镜像 `Apery/Legendre.lean`（`vS` 的 Legendre 阶乘公式计算，
     b-结构相关、是 Norm.lean 的第一依赖），或先建 `Zeta7/Norm.lean` 骨架
     登记 Lp/mN/integral_mN 目标陈述（InnerOK/OuterOK 的 b=8 常数按
     b8_verdict.md 最优轨道再工程）。

   **【2026-09-25 进展 16】`Zeta7/Legendre.lean` + `Zeta7/Norm.lean` 骨架建成——
   vS 计算与实归一化层落地，(3.12)-类比组装版登记为目标**（编译通过，
   全项目 8957 jobs，sorry 新增 1 条至 2 条：main_estimate + GV_F_Lsmall）：
   - `Legendre.lean` 镜像 `Apery.Legendre`：`padicValNat_finset_prod`（赋值乘积，
     b-无关）、`S_eq_div`（b=8：分母 `(3n)!^{16h}`）、`vS_eq`（(5.3)-类比，
     12h→16h 为唯一差异；`hn : 0 < n` 本库版本已有，直接用）。
   - `Norm.lean` 骨架（镜像 `Apery.Norm` 可立即证成部分 + 目标登记）：
     * 已证：`GV_F_of_Δ`（Δ→F 赋值平移）、`vSK_big`（p > 2h ⟹ v_p(S_K)=0，
       走本库 vS_eq，16h 幂次下同样归零）、`rat_int_of_VG`（处处 p-integral ⟹ 整数，
       integral_mN 的收尾引理）；`Mcut`/`vSK`/`Lsmall` 定义落地。
     * **b=8 活常数钉死**：`Lsmall = −(8·h·⌊log_p 200n⌋ + h·v_p(720))`；组装
       系数 8 = 6（每行 tau8_bound：5 求导 + Lb）+ 2（极点/Y-位移 K 项），
       与 §E "8 = 7+1" 拆分等价。
     * **(3.12)-类比组装版 `GV_F_Lsmall` 登记为 sorry**（附证明路线）：
       镜像 `Arith/SmallPrimeF.lean`（qP + PoleVal/MomentVal/Pullback 三支），
       单步核换已证 `tauX8_direct`（β−6）与 `VG_H7`。
     * **文档勘误（本轮发现并消解的分歧）**：§C7 表/§D 的"L_p^B = 1+v_p(720)"
       与已证 `tau8_bound`（常数仅 v_p(720)，von Staudt −1 已被 Lb 吸收，
       §C8 常数修正）不一致；采信已证界与经验零违规用的
       `−8h⌊log⌋ − h·v_p(720)`，Normalization/Norm 两文件已按此对齐。
   - 待建（Norm.lean 尾部已列镜像顺序）：Lp/mN/integral_mN 依赖内区/外区
     估值机器（γ 再工程主战场 = `Arith/InnerAlloc` + `Arith/OuterEntryMain`）；
     先灭 GV_F_Lsmall 需移植 `Arith/{PoleVal,MomentVal,Pullback}`。
   - 下一步：移植 `Arith/PoleVal.lean`（极点行赋值界，231 行，b-差异：
     极点值权重 j⁴→j⁶、常数 −1/4→−1/6、24→720），或先 `Arith/ClassFrame`
     （PlK/Sep 类框架，内区外区机器的共同地基）。

   **【2026-09-25 进展 17】`Zeta7/Arith/PoleVal.lean` 移植完成——极点值赋值界
   全链入 Lean**（编译通过，全项目 8958 jobs，sorry 仍 2 条）：
   - 镜像 `Apery/Arith/PoleVal` 全 13 引理。b=8 差异（全部落在照抄会错的点上）：
     * 指数 5→7（VG_H7_lt/VG_pair/VG_H7_pm1/H7_succ'/H7_split/GV_poleValue_congr
       的配对同余与求和重排）；
     * 极点权重 j⁴→j⁶、`VG_quarter`(1/4) → `VG_sixth`(1/6)——**假设升级
       `3 ≤ p` → `5 ≤ p`**（3∣6 而 3∤4；机器素数区 p ≥ 7 无碍）；
     * `GV_poleValue_sq` 界 −5 → **−7**：直接接本库已证 `DirectBound.VG_H7`
       （j < p² ⟹ v_p(H⁽⁷⁾_j) ≥ −7，harmonic7_val_aux 合成）；
     * `GV_poleValue_mul` 界 −1 **保持闭合**：v_p(j⁶) = 6 与 −7 恰合成
       6 + (−7) = −1（b=6 为 4 + (−5) = −1）——b=8 的 self-calibration；
     * `GV_poleValue_congr`（poleValue(p−c) ≡ poleValue c mod p）常数项 −1/6
       相消，无需 VG_sixth，保持 3 ≤ p。
   - **mo271 模板第六处潜伏 bug（实锤）**：`GV_poleValue_congr` 尾部
     `rw [padicValNat.mul (by omega) (by omega), ...]` 的 by-omega 块在
     rw 项内对**未赋值的 metavars**（mul 的两个隐式非零参数）运行，留下
     `⊢ ?m = 0` 未解目标；修法：先 `have` 出 `hc0'/hd0'/hd1/hdp` 显式项再 rw。
     （同模式 `padicValNat.mul (by omega) (by omega)` 在文件其余两处能过系
     unification 恰好先赋值——脆弱，移植同类代码时一律外提。）
   - 里程碑意义：灭 `GV_F_Lsmall` 的三支缺件完成 1/3（PoleVal ✓；
     MomentVal 矩行赋值、Pullback p²-分离提升待移植）；GV_poleValue_lt/sq/mul
     也是内区/外区估值机器（SmallPrime 系）的公共零件。
   - 下一步：移植 `Arith/MomentVal.lean`（矩行赋值，107 行：μ 矩的
     p-整性，b-差异集中在 Eulerian/Bernoulli 系数 24→720 与七因子矩公式），
     或 `Arith/Pullback.lean`（236 行，Sep 条件下赋值提升）。

   **【2026-09-25 进展 18】`Zeta7/Arith/MomentVal.lean` 移植完成——矩赋值界
   入 Lean**（一次编译通过，全项目 8959 jobs，sorry 仍 2 条）：
   - 镜像 `Apery/Arith/MomentVal` 全 5 引理。b=8 差异：
     * 矩公式三因子/24 → **五因子/720**（(2e+3)...(2e+7)）；
     * `VG_inv24`（24 = 2³·3，`p ≥ 5`）→ `VG_inv720`——**素数 5 进入归一化**
       （720 = 2⁴·3²·5），假设升级为 `p ≥ 7`（= 本库机器素数区，接已证
       `DirectBound.padicValNat_720`）；`VG_μmono`/`VG_μmono_int` 同步升级；
     * `VG_μmono` 界保持 −1（bernoulli_even 的 −1 独扛）；`VG_μmono_int` 的
       j ∈ {1,2,3} 三分情形按五因子重写：`p ∣ 2e+{3,4,5}` 分别由
       2e+2 = j(p−1) 给出，显式 `Dvd.dvd.mul_right/mul_left` 链延伸两个因子。
   - **mo271 模板第七处隐患（规避）**：原三因子 `mul_right` 嵌套 `_` 模式
     （`mul_right (mul_right (mul_right ⟨1, _⟩ _) _) _`）对五因子不可机械
     延伸且从未编译验证；已改为全显式参数链。
   - 里程碑：灭 `GV_F_Lsmall` 的三支缺件完成 2/3（PoleVal ✓ MomentVal ✓；
     剩 Pullback）；`VG_μmono(_int)` 同时是 SmallPrime 系（内区/外区机器）
     的公共零件。
   - 下一步：移植 `Arith/Pullback.lean`（236 行：Sep p Pl 条件下
     `GV p (P.comp (p²·X + ...))` 的赋值提升，b-差异待读原文后登记），
     三支齐了即可组装 `SmallPrimeF` 灭 `GV_F_Lsmall`。

   **【2026-09-25 进展 19】`Zeta7/Arith/Pullback.lean` 移植完成——pullback
   恒等式 (3.1)-类比入 Lean，三支缺件齐**（编译通过，全项目 8960 jobs，
   sorry 仍 2 条）：
   - 镜像 `Apery/Arith/Pullback`：τ₈ 线性性（neg/sum；add/C_mul 已在
     DirectBound）、`tau8_X_pow(odd)`、`tau8_pull_poly`、`PlK/piPl_PlK/Bj`、
     `polyPart_pull8`、`resP_pull8`、`μX_eq_tauX8`（(3.1)-类比主恒等式）。
   - **b=8 差异（余式次数 5→7 的全部落点）**：
     * pullback 因子 `x⁵` → `x⁷`；留数分子 `r⁴/2` → `r⁶/2`（`r⁷/(−2r)`）；
     * 每极点余式 三次 `−X³−j²X` → **五次** `−X⁵−j²X³−j⁴X`（来自
       `x⁷ = (x²+j²)(x⁵−j²x³+j⁴x) − j⁶x`）；`tau_cubic`(−1/4) →
       `tau8_quintic`(−1/6)（`∂⁵(−X⁵) = −120`，`−120·B₀/720`）；
     * `polyPart_pull8` 余式候选 `C(j⁴)XBj` → `C(j⁶)XBj`。
   - **移植陷阱两则（实锤）**：
     1. **ring 原子坍缩**：hj 恒等式 `X⁷ = j⁶X + (j²−X²)Q` 中 `C(j⁶)`、`C(j⁴)`
        若作为独立原子则等式为假（残差 `(j⁴−j²²)X³`）。b=6 模板用
        `e : C(j⁴) = C(j²)²` 天然单原子；b=8 须**双重写**
        `C(j⁶) = C(j²)³`、`C(j⁴) = C(j²)²` 把 j⁶/j⁴/j² 全部坍缩到单一原子
        `C(j²)` 后 ring 方闭。教训：镜像含多幂次 j 的 ring 收尾时先检查
        原子独立性。
     2. `tau8_add`/`tau8_C_mul` 已在 DirectBound 声明，重复声明报
        "already been declared"——移植前先 grep 已有名。
   - 里程碑：μX 世界 ↔ τ₈,X 世界在 b=8 正式接通（`μX_eq_tauX8`）；
     GV_F_Lsmall 的三支缺件（PoleVal/MomentVal/Pullback）全部就绪，
     下一步可镜像 `Arith/SmallPrimeF.lean`（283 行）组装 (3.12)-类比，
     灭 `Norm.GV_F_Lsmall` sorry。
   - 下一步：镜像 `Arith/SmallPrimeF.lean`：qP 行多项式构造 +
     `small_prime_bound`（b=8：每行界 `β − 6⌊log⌋ − v_p(720)` 已由
     tau8_bound 给出，K 相关主项系数 6→8），收尾后 Norm.lean 只剩
     内区/外区机器。

   **【2026-09-25 进展 20】SmallPrime 系五文件镜像完成，(3.12)-类比
   `GV_F_Lsmall` 消灭**（全项目 8965 jobs 编译通过，sorry 只剩
   Main.lean `main_estimate` 一条）：
   - 新文件 `Zeta7/Arith/{SmallPrime,SmallPrimeRes,SmallPrimeTau,
     BasisChange,SmallPrimeF}.lean`（+`DirectBound` 补 `GV.det_GV`）。
   - **7-vs-8 之争定案**（动笔前重读 mo271 SmallPrimeTau 原文解决）：
     b=6 每行界 −6⌊log⌋−v_p(24) 的 6 = 5+1 = 调和 H⁽⁵⁾(−5⌊log⌋) + 残差
     (−1⌊log⌋)；b=8 平移为 7+1 = **8**，pole 分支 GV.C_mul(hres, hH)
     直接给 −8⌊log⌋，polyPart 分支 tau8_bound 的 −6⌊log⌋−v_p(720) 单调
     汇入 −8⌊log⌋−v_p(720)。登记的 `Norm.Lsmall`（−8h⌊log⌋−h·v_p(720)）
     **无需任何改动**；早前"8 = 6每行+2 Y-位移"的记账系误读，已修正
     Norm.lean doc 与 b8_arithmetic §C7 勘误段。
   - **b=8 常数/形状落点**（相对 mo271 原文）：
     * `crude_tauX8`：−6⌊log⌋−v_p(24) → −8⌊log⌋−v_p(720)；pole 项用新证
       `VG_H7_log`（−7⌊log_p m⌋，镜像 VG_H5_log，inv_nat.pow 7）。
     * `det_basis_change`：`D(3n)^6` → `^8`（唯一改动，其余 b-无关）。
     * `SmallPrimeF`：`S_eq_qlead` 的 `(N!)¹²`→`^16`；`X^5`→`X^7`、
       `z^5`→`z^7`、`(D/(N!)²)^6`→`^8`；`d := 5+12N+4(h−1)`→
       `7+16N+4(h−1)`（= 155n+3，hd1/hdK 仍 omega 可证）；
       hentry 每行界 `−3Λ−v_p(24)/2` 对半 → `−4Λ−v_p(720)/2`（8 偶数，
       恰好对半）；`hpull` 因本库 `pull8` 不带阶乘因子需重组（e1/e2 拆
       `C c` 与 `C((−1)^K/(N!)¹⁶)`，ring 收尾）。
   - 陷阱三则（实锤）：① `det_GV` 放进 `GV` 命名空间后引用须写
     `GV.det_GV`（裸名报 unknown identifier，且其失败会级联把错误
     定位甩到前文 `have` 处，勿被误导）；② `(720:ℚ)` 是 OfNat 字面量，
     `padicValRat.of_nat` 的 `↑?n` 模式匹配不上，须先
     `show ((720:ℚ) = ((720:ℕ):ℚ)) by norm_num` 再 of_nat + Int.cast_natCast
     收双重 cast；③ mo271 的 `rw [show 12*(37n) = 12*(37n) by rfl]` 类
     no-op 可直接删（b=8 版 `S_eq_qlead` 用 `div_pow, ← pow_mul ×2,
     field_simp` 干净收尾）。
   - 里程碑：**小素数区 (3.12) 全链入 Lean**，mo271 Arith 侧只剩
     内区（InnerAlloc/InnerWeights/ClassCount/LowRank 等）与外区
     （OuterEntry*/OuterBasis/OuterFrame）两大机器未镜像。
   - 下一步：镜像 `Arith/InnerAlloc` 系（water-filling，γ 常数按
     b8_verdict.md 再工程）或外区机器，推进 `Lp`/`mN`/`integral_mN`。

   **【2026-09-25 进展 21】内区 water-filling 机器六文件镜像完成**
   （全项目 8971 jobs 编译通过，sorry 仍只 Main.lean `main_estimate` 一条）：
   - 新文件 `Zeta7/Arith/{TEntry,Unimodular,ClassFrame,ClassCount,InnerWeights,
     InnerAlloc}.lean`，依赖链 TEntry → Unimodular → ClassFrame → ClassCount →
     InnerWeights → InnerAlloc（与 mo271 同序），全部一次编译通过。
   - **b=8 常数落点**（本轮核心工作——每条都与已证界核对过配对关系）：
     * `TEntry`：`xroots` 的零点根 5→**7**（pull8 的 X⁷）、`cnt_xroots` 同、
       `μX_tpol_bound` 出口 β−4 → **β−6**（tauX8_direct）、次数条件
       `5 + 2M.card − 2K + 1` → `7 + …`；
     * `ClassFrame`：`entryRoots` 的 D_N 幂 6→**8**（nsmul）、`classCount`
       零点类贡献 5→**7**、`class_frame` 入口平移 +4→**+6**、
       hdeg 的 `5 + 2(18n + 74n)` → `7 + 2(24n + 74n)`（8·3n=24n）；
     * `ClassCount`：`Bse = 7[a=0] + 8 S_N(a) − S_K(a)`（5→7、6→8）、
       `count_DN` nsmul 6→8；
     * `InnerWeights`：权重位移 `(b a − 4)/2` → **`(b a − 6)/2`**（配 ACI 的
       `+6 ≤`——与 tauX8 损失 β−6 吸收配对，等价于 §C7 的"每行 6 份 log 中
       5 求导 + 1 Lb"结构）、hdeg 同步、`inner_bound`/`inner_bound_cap`
       （后者只需零类条件 Z）；
     * `InnerAlloc`：`hβ : b c = (β c : ℚ) + 6`（+4→+6，与 topw 的 −6 配对）、
       零类赤字 `(b 0 − 6)/2`；`lrow/psiR/PhiK/kfSel/allocK/sum_deficit_le`
       纯整数/有理组合数学，b-无关照搬。
   - 里程碑：`inner_bound_cap`（b=8）入 Lean——给定 L、hZ 等边条件即给出
     `GV p (Δ n) (2 ∑ wcap)`；`PhiK_le_kf` 凹性比较与 `sum_wcap_allocK`
     权重和估计（Φ(kf) − B₀）全部可用。**Norm.Lp 第二分支（内区
     `vSK + ⌊2·WI⌋`）的算术侧组件已齐**，待做的是把它们在 Norm.lean 里
     实例化（β 偏移取 Bse 的类计数、kf 取 kfSel、L0min/klo/ktop 按
     200n 参数钉死）并合成 `Lp`/`mN`/`integral_mN`。
   - 陷阱零新增：六文件全部一次编译通过——b=8 平移至此已高度机械化
     （5/6/4 三个 magic number 分别来自 X 幂次、D 幂次、损失吸收，
     替换前逐处确认配对关系即可）。
   - 下一步：（a）Norm.lean 实例化内区分支 + 登记 Lp 陈述；（b）外区机器
     （mo271 `Arith/OuterEntry*` 系，规模更大）；（c）或回研究侧推进
     γ 常数再工程（b8_verdict.md）。

   **【2026-09-25 进展 22】Norm.lean 内区实例化 + Lp/mN/integral_mN 落地**
   （全项目 8971 jobs 编译通过；sorry 2 条 = `main_estimate` + 新登记的
   `GV_F_big`，后者有明确消灭路线）：
   - 实例化（镜像 mo271 `Norm.lean` 中部，全部一次编译通过）：
     `betaI = 8·ℓ_N(c) − ℓ_K(c) − 6`（与 InnerAlloc 的 `hβ : Bse c = β c + 6`
     精确配对）、`kloI/ktopI/L0I`（γ 常数沿用 mo271 数值，InnerOK 门控）、
     `allocI`、`InnerOK`（`7 ≤ p`、hdeg `7+2(24n+74n)−80n+1 < p²`、
     hZ 的 `(Bse 0 − 6)/2`）、`WI`、`Sep_PlK`、`GV_F_inner`。
   - **`Lp`（三分支）+ `GV_F_Lp`（全分支已证）**：小素数 Lsmall / 内区
     vSK+⌊2WI⌋（InnerOK 门控）/ 外区暂回退 Lsmall——外区回退使
     GV_F_Lp 不依赖外区机器即完整。
   - **整性链闭合**：`mN`/`mN_pos`/`padicValRat_mN`（`omit hp`，
     `Finset.sum_ite_eq'` 收尾）/`integral_mN`（Proposition 5.1-类比）
     全部已证。**Proposition 5.1 在 b=8 成立**（modulo GV_F_big）。
   - **新登记目标 `GV_F_big`**：`p > 2h ⟹ GV p (F n) 0`。mo271 走外区
     `GV_F_outer`；边条件推导（`OuterOK_big` 性质：p>2·37n ⟹ p 奇、
     7≤p、40n<3p、80n<p²、3n<p）已写入 doc，移植 `Arith/OuterEntry*`
     系后一步可灭。这是 mo271 Arith 侧**最后一块**未镜像区域。
   - 下一步：镜像外区机器（`Arith/{OuterFrame,OuterBasis,OuterEntries,
     OuterEntry,OuterEntryMain,PoleFun}`，先侦察规模与 b-相关点），
     灭 `GV_F_big`；此后 Norm 层全绿，只剩 Main.lean 的
     `main_estimate`（连 ζ(7) 无理性的总装：积分估计 + 行列式下界 +
     0 < |Q·ζ(7)+P| < 1 收尾）。

  **【2026-09-25 进展 23】外区机器五文件镜像 + `GV_F_big` 已灭，Norm 层全绿**
  （全项目 8977 jobs 编译通过；**sorry 仅剩 `main_estimate` 一条**——
  mo271 Arith/Norm 侧镜像至此 100% 完成）：
  - 新建 `Zeta7/Arith/{OuterFrame,OuterEntry,OuterBasis,OuterEntries,
    OuterEntryMain}.lean`（分别 215/133/145/279/511 行原文），全部一次或
    二次编译通过。PoleFun 未重建——本库 DirectBound/Pullback 已有全部对应。
  - b=8 平移点（逐处核对后落地）：
    1. `D(3n)^6` → `D(3n)^8`；`D_pow_mul_X_pow_int` 同改（simp only 不奏效，
       须用 mo271 同款显式 `rw [map_mul, map_pow, map_pow, map_X, …]`）；
    2. `hβ0zero` 的 `18n` → `24n`（= 8·3n，商 `D(3n)^8·X^e / D(40n)` 次数
       `e + 24n − 40n`）；`outer_frame`/`outer_bound` 秩项 `22n` → `16n`
       （= 40n − 24n）；
    3. `VG_p_μGe`/`VG_μpoly_sub_μGe`/`VG_res_entry`/`padicValRat_den_le` 的
       `5≤p`/`3≤p` → `7≤p`；
    4. `entryO` 首项 `6 • [1..3n]` → `8 • [1..3n]`（OuterEntries），
       `num_count`/`VG_res_entry` 的 `6·δ` → `8·δ`（OuterEntryMain）；
    5. **wO 权重常数 4 → 6**（本轮唯一需要算术推导的平移）：b=8 每极点合计
       下界 `8δ + is + it − ℓ + 1 − 7`（`GV_poleValue_sq` 界 −7），权重和
       `is + it + 6δ − ℓ − C` 要求 `C ≥ 6 − 2δ`，故 `(ℓ+4)/2` → `(ℓ+6)/2`，
       而 `3·delC` 系数**恰好不变**（δ 项 8δ 对 6δ 的余量 2δ 吸收 −7 对 −5
       的劣化）。b=6 时 C=4 是等式闭合。
  - Norm.lean 外区实例化：`OuterOK`（b=8 已是 7≤p）、`WO`（`haveI` 技巧
    在 def 内提供 Fact 实例；秩项 16n）、`Lp` 第四分支 + `GV_F_Lp`
    五个 split_ifs 叶子、`GV_F_outer`、`OuterOK_big`、`WO_big`
    （`37n − ((2p+16n−3) − (37n−1)) = 0` 由 `p > 74n` 经 omega 给出）、
    **`GV_F_big` 消灭**（GV_F_outer + vSK_big + WO_big 三步）。
  - 陷阱实录：mo271 `pole_case_zero` 里 `GV_poleValue_mul` 结论配 `GV`
    （多项式版），照抄时误写 `VG`（有理数版）报类型错——GV/VG 形近，
    移植 pole 相关断言时须看目标类型。
  - **里程碑**：`integral_mN`（Proposition 5.1-类比）现在**无条件成立**；
    Zeta7Formal 只剩 `Main.lean` 的 `main_estimate`（总装：积分上界
    `0 < |Q ζ(7) + P| < e^{−c n²}` + 行列式/尺寸下界）。
  - 下一步：总装侧。mo271 对应 `Main.lean`/`Estimate.lean`/`LowerBound.lean`
    系（积分矩估计 + 行列式非零下界）。先侦察 mo271 Main 侧规模与
    b-相关点，再定镜像顺序。

  **【2026-09-25 进展 24】Growth 机器（Proposition 5.2-类比）开工：b-无关脚手架镜像**
  （新增 7 文件全部编译通过；全项目仍只余 `main_estimate` 一条 sorry）：
  - 总装链侦察（mo271）：`main_estimate` ⟸ `real_bound'`（RealBound，靠实分析机器）
    + `growth_mN`（Growth.lean）+ `integral_mN`（已证）。`growth_mN` 拆四段素数和：
    小素数 p≤K/400（PNT）/ tail K/400<p≤K/20 / 内区表 K/20<p≤K/3 / 外区表
    K/3<p≤2h，后三段经 `psum` 机器压成 ∫f/x³。
  - 已镜像（b-无关）：`Zeta7/{PNT,PrimeSum,PrimeSumStep,PrimeSumIntegral}.lean`
    （θ~x 的 ε 形式、wsum Abel 求和与极限、psum 分段 Darboux/积分上界）、
    `Zeta7/Growth/{PieceIdx,Integral,Assembly1}.lean`（分区定位、∫(Ax+B)/x³、
    log_mN 分解、sum_split4、cPrime 工具链）。
  - **b=8 平移首例（small_range_le）**：系数 6·37n → 8·37n（Lsmall 的 8=7+1）；
    `v_p(24)`（界 4、阈值 k≤24、和 ≤100）→ `v_p(720)`（界 7——log 720 =
    log(720/512)+9log2 < 0.41+6.24 < 7；阈值 k≤5——素因子全 ≤5，新引理
    `prime_dvd_720_le_five`；和 ≤35）。结果比 b=6 更紧（35 < 100）。
  - 陷阱：`Nat.prime_dvd_prime_iff_eq`（非 `Prime.dvd_prime_iff_eq`）；
    term 模式 `fun hd =>` 后接 `have/omega` 必须包 `by`。
  - **剩余阻塞（研究侧）**：tail/内区/外区三段表的 b=8 精确有理数据
    （mo271 由 TableGen 生成 125+13+1140 段证书；本判定文件的拟合值
    ∫R₈=0.1931、I_out=1.5362 是观测值，需升级为类级精确和 + 分段线性
    证书）、b=8 Aeff/U 常数与 margin 验证。
  - 下一步：研究侧建 b=8 表管道（参照 mo271 `TableGen.lean` 的算法：
    类数据 → 每段最大偏移 → 线性上界证书），或继续镜像 b-无关部分
    （Assembly3 的 range_sum_le、theta_le_two、low_order 骨架）。

  **【2026-09-25 进展 25】研究侧 b=8 三段表精确管道建成（b8_tablegen.py），
  b=6 三值精确复现，A_*₈ = 1.9446 钉死**
  （`research/b8_tablegen.py`，产物 `research/b8_tables.json`）：
  - **b 依赖公式全部钉死**（逐条溯源 mo271 原文 + 本库已证 b=8 平移点）：
    * `Ein_b`：`12u⌊αx⌋→2b·u⌊αx⌋`，`psiR(k, 2b·q'−2q−(b−2)+b·a'−a)`
      （betaI = b·SX(N)−SX(K)−(b−2)；本库 PoleVal 4+(−5)→6+(−7) 自校准）；
    * `Eout_b`：`GO` 的 `(2q+a+4)/2→(2q+a+(b−2))/2`（进展 23 权重推导），
      `max 0 (13/10 x−2)→max 0 ((λ+(b−1)α)x−2)`（秩损失 22n→16n 推出 29/20）；
    * `Ftail_b` = (b−2)λ + 2λ{x} − 2b·λ{αx}（b=6: 4λ ✓；b=8: 6λ——tail_Lp_le
      逐步追踪 5hR→7hR 与 PT' 约束 6λ 两条独立推导吻合）；
    * tail 加性常数 `(5+(b+1)²)/32`（quad m/16 + popoviciu 值域 b+1 的 (b+1)²m/16；
      b=6: 27/16 ✓，b=8: 43/16；曾误用 2b−3 作值域被 b=6 校准当场抓住）；
    * 尾段 PT/CT/P̄：`c_g = bλ/α`（74→296/3），`CT 系数 c_g/α`（→11840/9），
      `P̄ = (c_g−λ)/6`（→11729/720），slack 系数 34→44（M=17→22）。
  - **校准（全精确命中）**：b=6 复刻 run 精确复现论文/mo271 三值——内区
    125 段 ∫₃²⁰ = 322437603634266857629/7535670527041937280000 ✓、外区 13 段
    129101/96000 ✓、tail 上界 −6843153/128000000 ✓（且 ≥ 真值 −0.05671，
    真值含对数项 407/400·ln20——mo271 有理上界的吸收机制确认）。
  - **b=8 精确产出**：
    * 内区 **131 段**，∫₃²⁰ = 120667538150827615739401/708353029541942104320000
      ≈ 0.1703494347（全部 kIn 过 admissibility 断言 −2q−6 ≤ k ≤ 8q+20）；
    * 外区 **14 段**，∫ = 263569/144000 ≈ 1.8303402778；
    * tail 有理上界 **−21553919/384000000** ≈ −0.056130（真值 ≈ −0.060298，
      对数系数 37/50·ln20）。
  - **A_*₈ = 137743476530383649272771363/70835302954194210432000000 ≈ 1.94456**
    （b=6 论文对照 1.33413）。与实侧 Ū₈(α=0.03) = −3.18 合并：
    **1.9446 − 3.18 ≈ −1.24 < 0，margin 充足，b=8 判定维持可行**。
    注：旧拟合观测（∫R₈≈0.193、I_out≈1.536）与精确值（0.170、1.830）偏差
    ~0.3/0.02——正是 b8_verdict.md 诚实声明第 1 条指出的"观测须升级为类级
    精确证书"，本轮升级完成，判定方向不变且更可靠。
  - 下一步：Lean 侧镜像 TableGen/TailPrime/TailIntegral/InnerPrime/InnerSum/
    InnerTable(131 段)/OuterPrime/OuterTable/TablePrime + Assembly2-4 + Constants
    （Ein_8/Eout_8/Ftail_8 定义 + b=8 表数据入 Lean），落地 growth_mN。

**【2026-09-25 进展 26】Growth 表机器 b=8 镜像完成：TailPrime/TablePrime/OuterPrime/TableGen + 三段表生成并全部编译通过**

- `Zeta7/Growth/TailPrime.lean`（307 行级，b=8：popoviciu 值域 9 版、Ftail `6λ+16λ{x}−16λ{αx}` 形式、s4 加性 `43/16`、hklo 新 `−2q−8`）一次编译通过。
- `Zeta7/Growth/TablePrime.lean`：bIn `16q'−2q−6+8b−a`、Ein 的 `16`、hdeg `7+2(24n+74n)−80n+1`。
- `Zeta7/Growth/OuterPrime.lean`：GO `+6`、Eout `max 0 (29/20 x − 2)`、秩损失 `16n`（hr 的 `58n` 恰好恒等）、零类亏界 `−4` 不变（LoC ≤ 2 且每项 ≥ −2）、Cout `+11` 不变。
- `Zeta7/Growth/TableGen.lean`：Ein_expand `16`、Eout_expand `29/20`，其余 b-无关闭式逐行镜像。
- 生成器 `research/gen_lean_b8.py`（从 `b8_tables.json` 读 131+14 段，模板照搬 mo271 三个生成器；**已修陷阱**：inner_table_k 断言与陈述用新 kloI `−2q−8`；OuterTable 的 max 项 `29/20`；文件头 import 必须在 set_option 之前）。
- 生成文件：`InnerTable.lean`（131 段，4464 行，编译 ~228s）、`InnerSum.lean`（tIn_mono/inner_table/inner_table_k，编译 ~56s）、`OuterTable.lean`（14 段）。全部编译零错误。
- 生成前校验：131 段全部满足 `-2q-8 ≤ k ≤ 8q+20`；抽查 4 个内段 + 全部 14 个外段的 Ein8/Eout8 与表内 (a,b) 线性拟合在分点 1/10、1/2、9/10 处精确相等。

**【2026-09-25 进展 27】Growth 链条全线打通：`growth_mN` 落地，全库编译零错误，仅剩主定理一处 sorry**

- `Zeta7/Growth/TailIntegral.lean`（b=8 全常数平移：FT `111/20`/`−74/5`、gT 加性 `43/16`、PT `296/3`、CT `11840/9`、P̄ `11729/720`、PhiT `43/32`、slack `44`；Python 预核验望远镜末端值 = −21553919/384000000 精确命中，Lean `norm_num` 终步通过）。
- `Zeta7/Constants.lean`（新建）：U = −159/50（观测值门控，doc 声明）、Astar = 137743476530383649272771363/70835302954194210432000000、A(M) 带 b=8 的 P̄、A200 = 140008647356341045663172731/70835302954194210432000000（A_200_eq 与 margin 的 norm_num 均通过）、Aeff = 198/100、Aeff_margin = −6/5 < 0、Kr。
- `Zeta7/Growth/Constants.lean`：sum_abs_bIn_le 改 `16q'−2q−6+8b−a`、下界 `-2q−8`、界 `16q+30`；abs_GO_le 的 `+6`。
- `Zeta7/Growth/Assembly2.lean`：Bmax_le 的 `7+16q'−2q−6`、ktop_sub_klo `10q+28`；Ctail/Ctab/Cout 的 10⁷/10⁸/10⁵ 界重放核算：≤ 9,659,165 / 22,079,569 / 12,611，全部闭合。
- `Zeta7/Growth/TableIntegrals.lean`：inner_integrals（131 段，b=8 内区积分）与 outer_integrals（14 段）两个大 norm_num 精确命中表数据。
- `Zeta7/Growth/Assembly3.lean`：**发现并修正一处真错**——b=8 的 hdeg 展开为 116n+8（非 mo271 b=6 的 104n+6），原阈值 10400 与 hsq 强度均不足；提升到 `hn : 12000 ≤ n`、`hsq : 11600n+900 ≤ 100k²`（nlinarith 可证，因 100k² ≥ (n+1)²）。三个 range 引理全部随动。
- `Zeta7/Growth/Assembly4.lean`：段数 131/14、三个极限值换 b=8 精确分数；尾段 Lipschitz 恒等式系数 `111/20`、`74/5`、`37/50`（斜率核验：max|aIn|=19.175、max|aOut|=14.65 ≤ 100）。
- `Zeta7/Growth.lean` 总装：`growth_mN` 落地（阈值 12000、小素数系数 8·37n、主项和 1.96306 < 1.98−1/1000 由 norm_num 命中）。
- 全库 `lake build` 零错误。剩余 sorry 仅 `Main.lean:185` 主定理本身（顶层研究目标，按设计门控登记）；DirectBound 与 Tau 中的 "sorry" 字样均为文档提及，无实质 sorry。

**【2026-09-25 进展 28】RealBound/实侧链盘点完成，第一波（b-无关基础层）镜像并全部编译通过**

盘点结论（mo271 RealBound+MainEstimate 的 import 闭包对照本库）：
- **本库已有**：Weight、Hermite、HermiteFormula、HermiteIBP、HermiteIntegrals、Legendre、Construction、Moments、Degree、PartialFractions、Positivity、Normalization、PNT、PrimeSum 系、Growth 全链。
- **第一波已镜像（本轮，全部编译通过）**：`Gaussian.lean`（高斯/配方/Fubini）、`Andreief.lean`（(6.10) 行列式恒等式）、`Stirling.lean`（log 阶乘界，sed 直译）、`ZeroMass.lean`（截断核零质量能量非正，Lemma 6.2 类比）、`Kernel.lean`（`Ltr→log r` 极限）、`DetIntegral.lean`（(6.10) Hankel 多重积分；`D(3n)^6→^8`）。
- **剩余缺口（拓扑序）**：①Energy 链：CircleAtoms、Energy、EnergyAtoms、EnergyBlocks、EnergyRaw、EnergyLimit、EnergyFinal、EnergyBound（应为 b-无关或轻依赖，待逐文件确认）；②Potential 链：Potential、PotentialV、ArcsineAtoms、ArcsinePotential（同上）；③Certificates；④`Measure.lean`——**b 依赖数值**（table1 十六段 arcsine 分量、M0 = −1329/200、Irho 都依赖权函数，b=8 需重算）；⑤`EnergyConst.lean` + `TableCheck.lean` + `Table/*`（~15MB 数值证书，b=6 的 U 证书重心，**b=8 需研究侧重算 Ū₈ 的完整离散化**——目前只有 α=0.03 的观测值 −3.18，无可形式化的分段数据）；⑥Stirling 应用、RealBound、MainEstimate、Criterion 合拢。
- 注意：λ=37/40、α=3/40 在 b=8 不变（Growth 链已确认），b 只进权函数/导数次数/ν 的幂次。
