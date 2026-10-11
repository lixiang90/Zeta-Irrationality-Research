# 第258轮：CDT 原始关系改图机制与单一 χ−7 来源去重

2026-10-10；CDT 子任务。结论：固定 v2 的 CDT 实际函数族、真实周期投影及完整坏芽已核齐。唯一比较候选 χ−7 的三叶坐标虽然不是旧底坐标的有理重标，却使用第247–248轮已经支付且停止的同一完整 level 14 函数域和同一两周期源；本轮**来源准入失败，按重复源拒绝**。不重开 χ−7，不开第259轮该源续窗，不准入 Padé、real-energy 或 prime 实现。没有新的 ζ/L 数值定理。

## 1. 固定原文、版本与候选边界

CDT 指 Frank Calegari、Vesselin Dimitrov、Yunqing Tang 的 *The linear independence of 1, ζ(2), and L(2, χ−3)*。固定原始文献为 [arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2)，2024-09-16，218页；本地 [固定 PDF](../literature/cdt2024_l2_chi_minus3.pdf) 的 SHA256 为 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。本文 CDT 页码均为此文件物理页，亦等于正文印刷页。

关键完整读域为 §§11–13，pp159–173；另核 §10 的具体纯函数、§9 Corollary 9.0.19、§7 Theorem 7.0.1、Appendix A 的 Lemma A.4.4 与 (A.5.1)。这不是整本218页 FULL 阅读声明。作者当前 [L2chi.pdf](https://www.math.uchicago.edu/~fcale/papers/L2chi.pdf) 有220页，不能混用页码。`openai_dd_full_source_20261007` 是另一篇 *The Deligne–Drinfeld conjecture* 的 KZ holonomy 源，不是 CDT；本轮不把其 odd-weight 抽象深度一结论算成数值来源准入。

先选定的唯一比较候选为 χ−7 的平均 theta carrier 与 dyadic 两 primitive，底坐标固定为
\[
 T=\frac{\eta(\tau)^3\eta(7\tau)^3\eta(14\tau)}{\eta(2\tau)^7}.
\]
没有候选池扩张、参数/prime/maps 扫描。读到第247–248轮旧资产后，以下 χ−7 项全部归为去重审计，不作为新源证书。

## 2. CDT 的实际三函数和真实数值投影

令 χ₃=χ−3，L₃=L(2,χ₃)，ζ=ζ(2)，q=e^{2πiτ}。§11.1.1–11.1.4，pp159–161，固定 Γ₀(6) 的 Hauptmodul
\[
 x=q\prod_{n\ge1}\frac{(1-q^n)^4(1-q^{6n})^8}{(1-q^{2n})^8(1-q^{3n})^4}
 =q-4q^2+10q^3+\cdots.
\]
四 cusp ∞,0,1/3,1/2 对应 x=0,1/9,1,∞。其正式逆 q(x)=x+4x²+22x³+⋯∈xℤ[[x]]。Zagier 的原始案例是 **A 与 C**，不沿用旧稿可能混入的 D 标签。

实际函数为
\[
 \theta_{-3}(q)=1+6\sum_{n\ge1}\chi_3(n)\frac{q^n}{1-q^n},\qquad
 A(q)=\frac{\theta_{-3}(q)+\theta_{-3}(q^2)}2,
\]
\[
 B(q)=\sum_{n\ge1}\frac{\chi_3(n)q^n}{n^2(1+q^n)},\qquad
 C(q)=\sum_{n\ge1}\chi_3(n)\left(\operatorname{Li}_2(q^n)-\frac14\operatorname{Li}_2(q^{2n})\right),
\]
\[
 H_A(x)=A(q(x)),\quad H_B(x)=A(q(x))B(q(x)),\quad H_C(x)=A(q(x))C(q(x)).             \tag{2.1}
\]
H_A=Σₙaₙxⁿ，其中 aₙ=Σₖ₌₀ⁿ binom(n,k)²binom(2k,k)∈ℤ；H_B,H_C 的完整前 N 项由 d_N² 清分母，d_N=lcm(1,…,N)。它们开头为
\[
 H_A=1+3x+15x^2+93x^3+\cdots,\quad
 H_B=x+\frac{23}4x^2+\frac{145}4x^3+\cdots,\quad
 H_C=x+6x^2+\frac{343}9x^3+\cdots.
\]
它们满足 pp162 的实际算子
\[
 \mathcal D=x(1-x)(1-9x)\partial_x^2+(1-20x+27x^2)\partial_x+3(-1+3x),
\]
\[
 \mathcal D H_A=0,\qquad \mathcal D H_B=1,\qquad \mathcal D H_C=\frac1{1-x}.       \tag{2.2}
\]

这里的周期是实际收敛数值。令 p=ψ₁(1/3), r=ψ₁(2/3)，由 ψ₁(z)=Σₖ≥₀(k+z)⁻² 逐余类重排得到
\[
 L_3=(p-r)/9,\qquad \zeta=(p+r)/8.
\]
所以坏芽数值行中的两坐标为 (L₃/2,ζ/4)=((p-r)/18,(p+r)/32)，其有理变换行列式为1/288。这个投影不需要任何 formal period map 的单射性，也不准许任意 Galois 元素作用于已取值周期。

## 3. 原始关系如何删除完整坏芽

令 δ=1/9，Φ₃(v)=1+v+v²，D₀=1-st，N₀=(1-s²)(1-t²)。§11.1.11–11.1.17，pp162–163 的积分给出
\[
 E_B:=H_B-\frac{L_3}2H_A
 =-\frac12\int_{[0,1]^2}\frac{\Phi_3(st)}{\Phi_3(st)^2-9st(1-s^3)(1-t^3)x}\,dsdt,       \tag{3.1}
\]
\[
 E_C:=H_C-\frac\zeta4H_A
 =-\frac14\int_{[0,1]^2}\frac{1}{D_0-x(D_0-N_0)}\,dsdt.                          \tag{3.2}
\]
第二式由 (11.1.14) 的 u=x/(1−x) 与 G_A(u)=H_A(x)/(1+u)、G_C(u)=H_C(x)/(1+u) 换回 x 得到。原文 (11.1.15) 的逐点界为
\[
 0\le\frac{9st(1-s^3)(1-t^3)}{\Phi_3(st)^2}\le1,\qquad 0\le\frac{N_0}{D_0}\le1.
\]
在 ℂ\[1,∞) 的每个紧集，分母中的 1−λx 一致离零。第一积分由 Φ₃(st)⁻¹ 支配，第二由 D₀⁻¹ 支配，后者积分为 ζ(2)<∞；故二者选定分支均在 ℂ\[1,∞) 全纯，特别是 δ 处全纯。x=0 的同一积分分别给 L₃ 与 ζ 的实际值。这一步比两个端点极限更强，支付的是**整个坏芽**。

为把跳变写成明确函数，定义
\[
 z(x)=\frac{27x^2(1-x)}{(1-3x)^3},\quad 1-z(x)=\frac{1-9x}{(1-3x)^3},\quad
 H_A(x)=\frac1{1-3x}\,{}_2F_1\left(\frac13,\frac23;1;z(x)\right).                   \tag{3.3}
\]
此式可由 Gauss 算子 z(1−z)F″+(1−2z)F′−(2/9)F=0 拉回 (2.2) 核证；两残差恒为0，初值1、3及原点递推唯一性确定等式，不是有限头拟合。在 z=1 的对数解中，log(1−z) 系数是
\[
 -\frac1{\Gamma(1/3)\Gamma(2/3)}\,{}_2F_1(1/3,2/3;1;1-z)
 =-\frac{\sqrt3}{2\pi}\,{}_2F_1(1/3,2/3;1;1-z).
\]
取 δ 的逆时针小圈 T_δ，得到完整非零跳变
\[
 J_\delta(x):=(T_\delta-I)H_A(x)
 =\frac{-i\sqrt3}{1-3x}\,{}_2F_1(1/3,2/3;1;1-z(x)),\quad
 J_\delta(\delta)=-\frac{3i\sqrt3}2\ne0.                                      \tag{3.4}
\]
由 (3.1)–(3.2) 的全纯性，
\[
 (T_\delta-I)(H_A,H_B,H_C)
 =J_\delta(x)\,(1,L_3/2,\zeta/4).                                           \tag{3.5}
\]
这是整个局部 monodromy germ 的等式，不只最高 log 项。

假设实际有理数值关系 a+bL₃/2+cζ/4=0，令 H=aH_A+bH_B+cH_C。于是
\[
 H=bE_B+cE_C\quad\text{在 }\mathbb C\setminus[1,\infty)\text{全纯},\qquad
 (T_\delta-I)H=(a+bL_3/2+c\zeta/4)J_\delta=0.                                  \tag{3.6}
\]
非平凡关系的 b,c 不会同时为0，且 b+c/(1−x) 不是零函数，故由 (2.2) H≠0。关系精确作用于共同的坏芽乘子。

H_A 是真实、非平凡的 **unit-period carrier**：H_A(0)=1，却在 δ 有非零对数坏芽。若把它换成端点常函数1，则 a+bH_B+cH_C 的跳变成为 (bL₃/2+cζ/4)J_δ=−aJ_δ，原关系一般不能消去。因此“1 也在目标数值列表”并不自动支付 same bad germ。这与完整坏芽 classes 必须经真实数值行 Θ₃(a,b,c)=a+bL₃/2+cζ/4 因子化的判据吻合。

## 4. 关系之后的共用域、真实秩与 strict 数字

§11.2，pp163–165，取 w=x/(x−1)，y=x+w=x²/(x−1)，G(y)=H(x)+H(w)。δ 与 w(δ)=−1/8 同时投影至 y=−1/72。由 (3.6) 得到主分支 G 在 ℂ\[4,∞) 全纯，y=4 的局部 monodromy 为有限二阶。其 ambient differential equation 仍有 {0,−1/72,4,∞}，返回支路仍能看到 −1/72；不能把这个 singularity 从整个 connection 删除。

P_k=x^k+w^k∈ℤ[y]，P₀=2、P₁=y、P_k=yP_{k−1}−yP_{k−2}，ord_y P_k=ceil(k/2)。所以第 N 个 y 系数用到 x 系数至2N，这解释 d_{2N}² 的真实费用。

Lemma 12.1.1，pp167–170 的14个实际独立函数为七个纯函数 B₁,…,B₇，以及
\[
 G,G',G'',G''',\quad \int_0^yG(v)dv,\quad
 \int_0^y\frac{G(v)-G(0)}v dv,\quad
 \int_0^y\frac{G(v)-G(0)-G'(0)v}{v^2}dv.                                    \tag{4.1}
\]
§10，pp154–158 定义
\[
 B_1=1,\quad B_2=\sum_{n\ge2}\frac{2(n-2)!n!}{(2n)!}y^n,\quad
 B_3=\sum_{n\ge1}\frac{(n-1)!^2}{(2n)!}y^n,
\]
\[
 B_4=(x-w)(\operatorname{Li}_2(x)-\operatorname{Li}_2(w)),\quad
 B_5=\sum_{n\ge1}\frac{(n-1)!^2}{(2n-1)!(2n-1)}y^n,\quad
 B_6=\int_0^y B_3(v)/v\,dv,\quad B_7=\int_0^y B_4(v)/v\,dv.
\]
独立性实际使用绕4、再绕−1/72、再反向绕4的返回支路；B_i 不变而 G 的变化是非零四阶不可约齐次解。随后用 Frobenius 极点阶界与有限线性代数证明没有 primitive relation。不是“微分4次就自动得到4维”；Remark 12.1.12 明示另一个多积分选择会给出假的独立性断言。

§13，pp171–173 的14×2 denominator array 两列为
\[
 (0,2,2,2,2,2,2,2,2,2,2,2,2,2)^t,
 \quad(0,0,0,2,2,2,2,2,2,2,2,2,2,2)^t,
\]
积分向量 e=(0,0,1;0,0,0,0,0,0;1,1,1,1,1)，六个1。原文保留 primitive 的有限 shift d_{2N+3}²，援用 Remark 6.0.12，不把它冒称字面上的 d_{2N}²。费用为
\[
 \tau^\flat=191/49,\qquad \tau^\sharp=27/80,\qquad
 \tau=16603/3920=4.235459\ldots .
\]
§7 pp89–90 的 Theorem 7.0.1 在原 standing assumptions、原 holonomic tuple 与合法 meromorphic pullback 下给
\[
 m\le \frac{\mathcal J(\phi)}{\log|\phi'(0)|-\tau},\qquad
 \mathcal J(\phi)=\int_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w),
\]
其中 holonomic 情形仍必须 log|φ′(0)|>τ。Appendix A pp203–205 选 φ=h∘ψ，h(q)=−256q∏(1+qⁿ)²⁴，
\[
 |\psi'(0)|=\frac{5448339453535586608000000000}{8658833407565631122430056127},\qquad
 |\phi'(0)|=256|\psi'(0)|.
\]
Lemma A.4.4 核 −1/72 的唯一小原像，Corollary 9.0.19 为包含所需小原像的 univalent leaf 与 y=4 的有限 ramification 提供合法性。(A.5.1) 的 contour energy 为 <11.845，故 quotient=13.9938⋯<14，完成矛盾。这里本轮读取原证书，不运行其 energy producer；不把这组数字移交 χ−7。

推广到另一个 cyclotomic 通道时，必须换出能够承担 unit period 的非平凡 carrier，且核全部坏芽因子化、完整其它原像/返回支路、正式整模型和实际独立秩，再为同一 tuple 支付 strict holonomy。只替换 χ、端点值或 trigamma projector 不保留以上证书。

## 5. 唯一 χ−7 比较候选的 all-prefix 与 Abel 核证

令 χ=χ−7，χ(1,…,6)=(+,+,−,+,−,−)，Y=L(2,χ)。取
\[
 A_0(q)=1+2\sum_{n\ge1}\chi(n)\frac{q^n}{1-q^n},\quad
 A_7(q)=\frac{A_0(q)+A_0(q^2)}2
 =1+\sum_{n\ge1}\chi(n)\frac{q^n}{1-q^n}+\sum_{n\ge1}\chi(n)\frac{q^{2n}}{1-q^{2n}},
\]
\[
 B_7=\sum_{n\ge1}\frac{\chi(n)q^n}{n^2(1+q^n)},\quad
 C_7=\sum_{n\ge1}\chi(n)(\operatorname{Li}_2(q^n)-\tfrac14\operatorname{Li}_2(q^{2n})).
\]
故 A₇ 的常数为1，全部 q 系数为整数。若 a_j=Σ_{d|j}χ(d)d²，则
\[
 [q^j]B_7=\sum_{n\mid j}\frac{(-1)^{j/n-1}\chi(n)}{n^2},\qquad
 [q^j]C_7=\frac{a_j-[2\mid j]a_{j/2}}{j^2}.                                  \tag{5.1}
\]
每项分母整除 d_N²（j≤N）；乘 A₇ 保留此 prefix 性质。固定的 T=q∏(1−qⁿ)³(1−q⁷ⁿ)³(1−q¹⁴ⁿ)/(1−q²ⁿ)⁷∈qℤ[[q]]，首项系数1。逐系数递推解 T(q(T))=T，第 n 步未知 q(T) 的第 n 系数系数为1、其余仅含已知整数，故 q(T)∈Tℤ[[T]]。组成 A₇、A₇B₇、A₇C₇ 的第 N 个 T 系数仍只使用 q 次数≤N，因此 all-N 的 d_N² 清分母证明完整。

Abel 极限的支配核不是只说“连续”。令
\[
 F_7(r)=\sum_{n\ge1}\chi(n)r^n
 =\frac{r+r^2-r^3+r^4-r^5-r^6}{1-r^7}
 =\frac{rW_7(r)}{\Phi_7(r)},\quad
 W_7=1+2r+r^2+2r^3+r^4,\quad\Phi_7=1+r+\cdots+r^6.
\]
精确恒等式 Φ₇−rW₇=(1−r²)(1−r⁴) 给 0≤F₇(r)≤1（0≤r≤1），F₇(0)=0、F₇(1)=1。对 0<q<1，B₇ 各项由 n⁻²/2 支配，故 B₇(q)→Y/2。又由绝对重排
\[
 C_7(q)=\sum_{k\ge1}\frac{F_7(q^k)-\tfrac14F_7(q^{2k})}{k^2},
\]
其项由 5/(4k²) 支配，故 C₇(q)→3ζ/4=π²/8。实际数值行是 (1,Y/2,3ζ/4)。若 p_j=ψ₁(j/7)，则 Y/2=Σ_{j=1}^6χ(j)p_j/98，3ζ/4=Σ_{j=1}^6p_j/64，仍是实际 convergent series 的投影。

## 6. T 的三叶 divisor、全部 branch values 与 q→1 fiber

新增原始文献是 Leonardo Colò 的2022年 Aix-Marseille 博士论文 [官方全文](https://theses.fr/2022AIXM0580.pdf)，§2.3.1，物理82页/印刷64页。它给出 E=X₀(14) 模型
\[
 y_{14}^2-5x_{14}y_{14}-2y_{14}=x_{14}^3-3x_{14}^2+3x_{14}-1,
\]
\[
 x_{14}=\frac{\eta_2\eta_7^7}{\eta_1\eta_{14}^7},\qquad
 y_{14}=\frac{\eta_2^8\eta_7^4}{\eta_1^4\eta_{14}^8},\qquad T=x_{14}/y_{14}.       \tag{6.1}
\]
该 Weierstrass 模型 Δ=−21952=−2⁶7³≠0。令 O 为无穷点，Q=(0,1)，P=(1,0)。在 Q，令 y=1+v，局部方程为 v²−8x−5xv+3x²−x³=0，因此 ord_Q x=2；在 P，y(y−5x−2)=(x−1)³，因此 ord_P y=3；在 O，ord_O x=−2、ord_O y=−3。故
\[
 \operatorname{div}(x_{14})=2Q-2O,\quad\operatorname{div}(y_{14})=3P-3O,
 \quad \operatorname{div}(T)=2Q+O-3P.                                      \tag{6.2}
\]
T 的 degree 正好3，不是 genus-zero Hauptmodul。这是具体 divisor 证书，单说 genus1 不构成任何 no-go。

消元 y=x/T 得
\[
 \mathcal P(T,x)=T^2x^3+(-3T^2+5T-1)x^2+(3T^2+2T)x-T^2=0,
\]
\[
 \operatorname{Disc}_x\mathcal P=-T^3(1323T^3-1026T^2+323T-32).                   \tag{6.3}
\]
后一个三次式的 discriminant 为 −2604341376≠0。T=0 在 Q 的 ramification 为2，在 O 为1；三个非零根各有单一 e=2 分支；T=∞ 在 P 的 ramification 为3。总 ramification 为1+3+2=6，与 genus1 degree3 的 Riemann–Hurwitz 核齐。有限非零临界点还可由
\[
 x(x-1)^2(x^3+2x^2-13x-32)=0
\]
筛掉 x=0、1 后的三根核证，式子来自 2y=x³−3x+2 代回4倍曲线方程。

η 的 S 变换在 cusp τ→0 给 R=(8,49)，T(R)=δ₇=8/49，且
\[
 2401\mathcal P(8/49,x)=(x-8)(64x^2-121x+8).
\]
另外两个原像为 x=(121±7√257)/128、y=49x/8；η 商只在 cusp 有零极，E 的四 cusp 为 O,Q,P,R，所以这两个是普通内点。三次 branch polynomial 在 δ₇ 的值为 −2056/2401≠0，整个 fiber 未 ramified；R 的临界分子 2y−x³+3x−2=−392 非零。

这一 fiber 说明：q→1 的一处 cusp 数据不能自动冒称 T-pushforward 的完整坏芽。若此源未曾出现，有限待付条件会是完整 jump 是否仅为同一函数乘 (1,Y/2,3ζ/4)，以及另外两个 fiber/返回支路是否污染；**但去重后本轮不把它列成开放续窗，也不追加支付该已停止源**。

## 7. 第247–248轮旧资产的精确去重与费用变化

本轮独立读核 [247两周期源](chi7_dyadic_two_period_source_round247_20261010.md) 的 D1–D16、[247 dyadic源审计](dyadic_chi7_eisenstein_source_round247_20261010.md)、[247总结](research_round247_dyadic_source_review_20261010.md)、[248完整场费用门](dyadic_field_lift_energy_gate_round248_20261010.md)、[248椭圆统一 cap](dyadic_elliptic_uniform_cap_round248_20261010.md) 与 [248全局审查](research_global_review_round248_20261010.md)。以下已是旧资产，不算本轮新突破。

旧 primitive 为 R_old=K(q)−2K(q²)、D_old=C_raw(q)−¼C_raw(q²)。D3 已给完整恒等式，因此
\[
 B_7=R_{\mathrm{old}},\qquad C_7=D_{\mathrm{old}},\qquad 3\zeta/4=\pi^2/8.
\]
旧 unit carrier 正是 A₀；对同一个数值关系 a+bY/2+cπ²/8=0，旧源 H_old=A₀(a+bR_old+cD_old)。由于 A₀、A₀(q²) 是同 weight1、同 χ 的 level14 模形式，其商是 E 上有理函数。于是
\[
 r=A_7/A_0\in\mathbb Q(E),\quad r(q)=1+O(q),\qquad
 H_{258}=A_7(a+bB_7+cC_7)=rH_{\mathrm{old}}.                                \tag{7.1}
\]
因此在完整函数域上是有理 gauge；导数也满足 H′₂₅₈=r′H_old+rH′_old，周期响应无新方向。旧 D11 已支付完整耦合 Fricke cocycle；247源审计还支付 cusp1/2 的真实最高 log² 污染，其系数为 −343L(3,χ)/(8√7π³)≠0，而不是靠端点极限猜不存在其它 bad period。

旧完整域为 F=ℚ(u,Z)=ℚ(E)，u=(η₇/η₁)⁴，Z=η₂³η₁₄³/(η₁³η₇³)，[F:ℚ(u)]=3，旧底 x_old=u/(1+7u)。T **不是** ℚ(u) 中的 rational rescaling、幂或 Möbius 改名：u 的 ∞-fiber 为 R（pole order2）与 P（pole order1），而 T 仅在 P 有 pole、在 R 有有限值8/49；任何 rational function of u 在 u=∞ 有 pole 就必须同时在二点有 pole。这一差别改变底 pushforward，不改变完整场或 period source。

具体新底完整域仍可用 F=ℚ(T,Z) 表示。由 η-S，Z 在 R 有简单 pole，而 T=8/49 的另外两个普通内点没有 pole。若 Z∈ℚ(T)，它在该 T-value 的 pole 必同时出现在整个未分歧 fiber，矛盾。因 [F:ℚ(T)]=3 为素数，Z∉ℚ(T) 即给 F=ℚ(T,Z)，1,Z,Z² 在 ℚ(T) 上独立。又 Z=q∏(1+qⁿ)³(1+q⁷ⁿ)³∈qℤ[[q]]，q(T) 整，因此三条整数场行仍在。

第248轮已核 normalized differential ω=f₁₄(q)dq/q=(1+O(q))dq，f₁₄=η₁η₂η₇η₁₄，并用确切 Weierstrass 模型及两个真实 cycles 给 period lattice 的 covering radius R_Λ<5/3。对全部合法 multivalent full-field graphs，Abel lift 避免一整个 lattice coset；Bloch 的1/12常数给 |z′(0)|≤12R_Λ<20。因为 T=q+O(q²) 且 pole fiber P 非空，任何同一完整域上的有限 holomorphic T 图仍满足同一 normalized Abel cap
\[
 |\phi'(0)|<20,\qquad\lambda=\log|\phi'(0)|<\log20<3.                         \tag{7.2}
\]
这不是用 genus1 单独否定图；它用旧文已支付的实际 differential、真实 period lattice、遗漏 pole fiber 与 normalized derivative。

旧五行 {1,Z,Z²,H_old,H′_old} 的安全 array 两列均为 (0,0,0,1,1)ᵗ，τ=32/25，m=5。前三整数场行强制其 energy J≥3λ；strict inequality 5(λ−32/25)>J 因而要求 λ>16/5。与 (7.2) 矛盾，所以旧 entry 已停止。

换到 T 后，**不能未经重付就把 m=5、τ=32/25 原样移交**：restriction of scalars、r 的 poles、T 的 branch locus 与 differential conversion 都可能改变 rank/array/index shifts。三整数行和同一 cap 可以明确移交；该坐标的新完整 cyclic rank 与费用没有在本轮支付。cap<20 单独也不证明所有未知 refined budgets 永远不可能。然而本轮没有给出一个区别于旧窗口、已付的 rank/费用收益机制，原 source carrier 在完整域上严格是 (7.1) 的旧 gauge。新符号、新 coordinate divisor 或初始 LCD 不能重开已停止来源。

## 8. 本轮资产与冻结建议

本轮新增独核是：固定 CDT v2 的 (2.1)–(4.1)、实际 trigamma 数值投影、明确 J_δ 函数和非平凡 unit-period carrier；Colò 原始模型下唯一 T 的 divisor/branch/fiber 代数；χ−7 all-N normalization、正式逆与严格 Abel 支配；以及与247–248同一场/同一 primitive 的去重校准。既有 χ−7 全函数 Fricke、坏 cusp 层与 elliptic cap 明确仍属旧资产。

没有取得区别于旧窗口的 χ−7 新关系机制。CDT 的 shared bad germ factorization 可以作为以后筛选真正新来源的校准条件，但只是准入判据，不能算新的数值结果或已准入目标。Magnetic/Question15.2.2 的既有讨论也不作为新准入。本轮建议是冻结此稿、保留去重结论；不自动指定任何新 χ、参数、实现或同源第259轮续窗。

数学 CAS 共 **3 次 Python/SymPy 进程**，只核一个固定 CDT 拉回和一个固定 T 模型：UTC00:05:19 原 HG pullback；00:12:09 T 消元/branch；00:13:18 上述固定式复核及 JSON/source pins 保存。日志审计仅解析本人会话元数据以恢复精确次数，不运行数学。无 parameter、map、prime 或整数 relation 扫描；无旧 producer、Lean、Padé、energy 数值程序；无 main/policy/manifest/git mutation。完整执行范围见本人 reading scope。
