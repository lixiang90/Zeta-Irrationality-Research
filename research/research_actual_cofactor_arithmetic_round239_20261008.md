# 第239轮：实际余子式费用已改善，收紧全图门槛后提前全局复盘

2026-10-08。上一238为progress；本轮也有改变行动的实质进展，目标保持active。**尚无新的ζ/L数值无理性或线性无关性定理。** 本轮付了239指定的同一实际余子式全有限处证书；随后通过重查已有精确解析式，证明这项费用upper仍不足以认证当前判据。240提前正式全局复盘，不再自动延长同源素数优化。

## 1. 仍是同一真实目标和actual selector

固定
\[
g_0=t=2I(1/4)=\frac52L(2,\chi_{-3})-
\frac{\pi\log3}{3\sqrt3},\quad
f=(1,F,b_gJ_{g_0}),\quad F=uE,
\]
\[
E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
J_g=\sqrt{1-4u}(g-2I),\quad I'=E/\sqrt{1-4u}.
\]
在目标有理假设g₀∈Q下，b_g为固定正整数且b_gg₀∈Z。沿238已经全阶支付的N=3m、m=D+1、单缺行flag，令
\[
K_m[r,s,E]=\frac{3^{r+s}}{2(r+s)+1},\quad
K_m[r,s,J]=[u^{r+s+1}]J_{g_0},
\]
\[
\delta_h=\det(K_m\text{删第 }h\text{ 行}),\quad
h_* =\max\{h:\delta_h\ne0\}\in[m,2m].
\]
真实完整Taylor评价的det为±b_gᵐδ_(h*)，237内在算术费用是
\[
\mathcal A_D=-\log|b_g^m\delta_{h_*}|. \tag{1}
\]
以下证书统一覆盖全部候选h，不要求知道h_*，也不换最大绝对值minor或Gram平方和。

## 2. 两层整性精确饱和一个新素数窗口

对p>3、p∤b_g、2m<p≤3m，置k=(p−1)/2、h=k+1、L=N−p、G=k−m。完整prefix中的唯一双极点是I_p；由完整卷积与binom(p−1,k)≡(−1)ᵏ，
\[
p^2T_N(c,b,a)\equiv
-2b_g(-3)^ku^p\sqrt{1-4u}\,a
\pmod{(p,u^{N+1})}. \tag{2}
\]
N<3p/2使内奇分母仅有p、外积分分母仅n=p；gS头保持整性。深层kernel恰迫a₀,…,a_L∈pZ_p，index为p^(L+1)。在此kernel上余下输出只有simple p层，且在原阶<h处全整。

第二层按relative orders分成三段：b覆盖0,…,m−1；自由高a列在m,…,k−1形成G阶Jacobi Hankel；低a=pA的双极点残差在k,…,N−h形成S₀=1的单位三角块。中间Hankel的完整det为
\[
2^{3G^2+G}\frac{\prod_{j<G}(j!)^2}
{\prod_{i,j<G}(2i+2j+3)}.
\]
p>4G−1自动成立，故该块为p单位；G=0直接略过gap。第二层onto全部N−h+1输出。因此最大完整prefix整数值格的local index**精确**为
\[
p^{L+1+N-h+1}=p^{2N-3k}. \tag{3}
\]
这饱和该窗口的完整整性收益，未计算actual minor的全部估值。高窗口N<p≤2N−1沿用236已付的精确index p^(N−k)，其它prime保留q_E=d_(2N−1)、q_J=d_Nd_(2N−1)的完整fallback，其中d_t=lcm(1,…,t)。全部素数幂、固定坏prime及原生头仍在账内。

CRT得到同一完整source子格Γ_D，T_NΓ_D全整，index Q_m满足
\[
\log Q_m=\frac{21}{2}m^2+o(m^2). \tag{4}
\]
新窗口比旧安全模型节省3m²/4；两个增长窗口不重叠。旧45/4改善为21/2，但这个raw upper本身仍不是实际费用。

## 3. 同一余子式的2、3整数内容

对任意μ-block的m个rows r₀<⋯<r_(m−1)，Cauchy公式给
\[
\det(\mu_{r_i+j})=
\frac{3^{\sum r_i+\binom m2}2^{m(m-1)}
V(\boldsymbol r)\prod_{j<m}j!}
{\prod_{i,j<m}(2r_i+2j+1)}. \tag{5}
\]
关键整除是
\[
V(\boldsymbol r)/\prod_{j<m}j!
=\det(\binom{r_i}{j})\in\mathbb Z.
\]
故2处奇分母不损失估值，两份factorial与显式2幂给v₂≥2m²−O(m log m)。3处至少有3^(m(m−1))；分母每行是step2 progression，其3进估值总和至多m²/2+O(m log m)，由双factorial主项抵消。因此v₃≥m²−O(m log m)。另一半b_gJ-block的m阶minor在固定2、3处只损O(m log m)，因为全部entries由q_J清分母。

沿两species作完整Laplace展开，相消只提高估值，得到对所有候选h统一成立：
\[
v_2(b_g^m\delta_h)\ge2m^2-O(m\log m),\quad
v_3(b_g^m\delta_h)\ge m^2-O(m\log m). \tag{6}
\]
这是真实rational determinant的内容，来自精确Cauchy式；未以实正性或有限样本认证p-adic行为。

有一个明确的全有限处整数证书。Γ_D的整基变换det为±Q_m，因此对每个h，Q_mb_gᵐδ_h∈Z。令e_p=v_pQ_m、F_m=∏j!、t₃=floor(log₃(6m−1))，定义
\[
c_2=\max\{0,e_2+m(m-1)+2v_2(F_m)-mv_2(q_J)\},
\]
\[
c_3=\max\{0,e_3+m(m-1)+2v_3(F_m)
-m\sum_{a=1}^{t_3}\lceil m/3^a\rceil-mv_3(q_J)\},
\quad C_m=2^{c_2}3^{c_3}.
\]
于是
\[
\boxed{Q_mb_g^m\delta_h\in C_m\mathbb Z,\quad
\log C_m=(\log12)m^2+O(m\log m).} \tag{7}
\]
零minor也满足整除；实际h_*非零由238全阶证明承担。故
\[
\boxed{\mathcal A_D\le\log Q_m-\log C_m,\qquad
a:=\limsup\mathcal A_D/D^2\le\frac{21}{2}-\log12.} \tag{8}
\]
2、3在Q_m中的原费用仅O(m log m)，内容credit不与增长窗口重复计算。237同flag格变换抵消式仍有效：这里改进的是同一内在费用的可证upper，未声称换格改变实际费用。

## 4. 俯瞰解析约束，旧容量upper过松

新upper约8.015，确实低于旧3log(3π³√2/8)门槛。我曾据旧松cap报告窗口打开；进一步重查234已经保存的精确式后，这个继续推断需要收回。对每张保留原生F且F∘φ meromorphic的合法holomorphic共同图，已有
\[
|\phi'(0)|\le C_E=\frac{2\pi}{3}
\mathbf K(1/9)\mathbf K(8/9),\quad
\mathbf K(x)=\int_0^{\pi/2}(1-x\sin^2\theta)^{-1/2}d\theta.
\]
不增加图假设，Cauchy–Schwarz与tanθ换元直接给
\[
\mathbf K(x)^2\le\frac\pi2
\int_0^{\pi/2}\frac{d\theta}{1-x\sin^2\theta}
=\frac{\pi^2}{4\sqrt{1-x}},
\]
\[
\boxed{|\phi'(0)|\le C_{\rm tight}:=\pi^3/2^{7/4}.} \tag{9}
\]
它约9.22，对全体此前合法共同图成立，不加unique-origin或univalent p条件。J的目标mark只进一步限制图。

基本BC判据要a<(9λ−3J)/2，J≥λ使其阈值≤3λ≤3log C_tight。严格比较
\[
\frac{21}{2}-\log12>3\log C_{\rm tight} \tag{10}
\]
可不用浮点核：π³<32及2^(7/4)>16/5给C_tight<10；e³>12给左侧>15/2，e^(5/2)>10给3log10<15/2。因此当前已证upper仍不能认证任何该基本图的严格余量。

同一固定BC line metric下的有限半径凸修正也须精确核，而非只删掉负能量项。令B(t)=min_r{J(r)−t log r}、Q_s=(2/s)∫₀ˢB−J(1)。B非减；对rank1常数源1用同metric、完整monomial flag及det=1校准，斜率式给Q₁≥λ。故Q₃≥Q₁≥λ，严格门槛a<(9λ−3Q₃)/2仍≤3λ。固定有限共同metric多图在相同已付HS/height条件下可作同一校准，范围详见[预算审阅](actual_cofactor_budget_gate_round239_20261008.md)。

这项校准不覆盖不同species metric、D-dependent图/metric、balanced tensor或尚未支付的几何机制。(10)只是现有safe upper不足；**不是实际a的lower，也不是目标无理性不可能定理**。

## 5. 下一轮的方向与验证

239完成了约定算术接口，但更紧全图界关闭了用当前费用证书继续图优化的理由。240提前正式复盘，比较直接holonomy、实际周期投影、mixed-period determinant与其它几何源；优先考虑有具体全尺度投影或严格新费用机制的路线，不继续盲目细化剩余prime或域参数。原目标始终是新的ζ/L数值结论。既有全阶结构资产保留，可在真正新输入出现时恢复。

本轮全部数学为纸面证明；数学程序、小D/素数/参数扫描、新PDF下载、Git修改与Lean构建均0。Root完整读取并独立核算术两稿，完整复读234全图与237 metric稿；新Q/C内容、两层kernel、正确simple截断、整基det及全图CS改善均逐式核。原 elliptic-cover精确式沿用234已核身份，未冒称本轮重新认证全部DLMF或CDT220页。两条独立交叉审阅和最终报告审阅另存。

完整证明：[算术稿](actual_cofactor_arithmetic_round239_20261008.md)、[独立稿](actual_cofactor_arithmetic_independent_round239_20261008.md)。[研究规则](research_global_review_policy.md)已记录下一正式复盘240；本轮本身不重置236计数。实际读域与冻结文件身份存literature/actual_cofactor_arithmetic_sources_round239_20261008。
