# Level 7 的 CM 留数、第三类分解与实际 C₃ 的周期比较

日期：2026-10-07。作者：`/root/source_pencil_finalize`。状态：新轮纯纸面主稿，待独立全文审查。本文只研究冻结的真实 `LB₃=t³`，不把 forcing、端点或原始 ξ 换成别的对象。

## 1. 实际对象与本轮新增结论

本轮 authority 是 `cdt_odd_delivery_real_gates_kummer_cauchy_extensions_20261007.json`，SHA256 `7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a`，620 条冻结记录（615 数学、5 guards）。冻结主稿 `cdt_odd_level7_polynomial_extension_classes_20261007.md` 的最终 SHA 是 `fc585a055e3b577a862f58202e24eda099394ae1b62e5f33393fb2b868690e7c`；其独审为 `a1aebf1f810e933147d5ce964e5177402146f2954dfd35aa8e4caf51b624db77`。本轮实际全文重新读入这两稿，并重新读 current main §§201–205；不把上轮读域记作本轮读域。

记 θ=t∂t，D=q∂q=(2πi)⁻¹∂τ，χ=χ₋₇。固定

\[
\begin{split}
L&=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),\\
r(\tau)&=\left(\frac{\eta(\tau)}{\eta(7\tau)}\right)^4,
\qquad t=\frac{r}{(r+7)^2},\\
A(\tau)&=1+2\sum_{n\ge1}\chi(n)\frac{q^n}{1-q^n},
\qquad f(\tau)=\eta(\tau)^3\eta(7\tau)^3,\\
h(\tau)&=f(\tau)\frac{t(\tau)^2}{1-t(\tau)},
\qquad LB_3=t^3,\quad B_3(0)=0,\\
E_3(\tau)&=B_3(t(\tau))/A(\tau).
\end{split}\tag{P1}
\]

固定的 q-Taylor 归一化给

\[
\partial_\tau^2E_3=-4\pi^2h,\qquad
C_3=4\pi^2\int_0^\infty y h(iy)\,dy.
\tag{P2}
\]

这里 C₃ 已在冻结稿中证明是 σ=1/28 的完整连接系数，即 `ΔσB₃=C₃ΔσA`，且 `0<C₃<κ/756`，κ=L(f,2)。本文不重新声称特殊值无理性，而新增以下可核接口：

1. h 的所有上半平面极点恰是判别式 −7、−3 的 CM 轨道；分别为二阶、三阶，完整低阶 Laurent 系数可精确写出。
2. −7 点的向量留数在真实代数 Hodge 归一化下恰为 **−[η′]/7**，没有遗留未支付的 Ω 或 2πi 因子。
3. h 可精确分为 CM 第三类部分与第二类部分；既有显式解析 Poincaré-kernel 分解，也有 K-Fourier 系数的代数 de Rham 分解。
4. 第二类 χ-parabolic 类的维数为 2；但尚未算出实际分量及相对 cusp 边界，故不能据此把 C₃宣布为 κ、quasiperiod 或 Rankin L 的已知数值线性组合。

## 2. 完整极点除子与各 cusp

η 在上半平面没有零点。因此 f 在上半平面无零无极点。t 和 h 的有理式为

\[
1-t=\frac{r^2+13r+49}{(r+7)^2},\qquad
h=f\frac{r^2}{(r+7)^2(r^2+13r+49)}.
\tag{P3}
\]

r 在 Γ₀(7) 的两个 cusp ∞、0 分别有一个简单 pole、zero，其他地方无零极点；可由 η-product 及 `r(W₇τ)=49/r(τ)` 看出。这也给出 r 是粗曲线 X₀(7) 的 degree-one 坐标。Yang 固定 v1 PDF15 明确给出 t 在 Γ₀(7)+W₇ 的三个椭圆点的值：

\[
\tau_\sigma=i/\sqrt7\longmapsto1/28,\qquad
u=(5+i\sqrt3)/14\longmapsto1,\qquad
w=(7+i\sqrt7)/14\longmapsto\infty.
\tag{P4}
\]

w 满足 `7w²−7w+2=0`，故判别式为 −7。它是 Γ₀(7) 的非椭圆点、Γ₀(7)+W₇ 的 order-2 点；r(w)=−7，r−r(w)=r+7 的局部零阶是 1，t 的局部 pole 阶是 2。于是 h 在该 Γ₀(7) 轨道有二阶 pole。

`r²+13r+49` 的两个根为 `(-13±3i√3)/2`。它们对应 Γ₀(7) 的两个 order-3 CM 轨道，被 Fricke 交换；代表可取 u 和 `W₇u=(-5+i√3)/14`。u 满足 `7u²−5u+1=0`，判别式 −3。r−r(u) 和 1−t 在上半平面局部坐标 τ−u 的零阶均为 3。因此 h 在两个轨道都有三阶 pole。σ 点没有 h 的 pole，因为 t=1/28，且 f 非零。

在两个 native cusp 坐标中 f、t 都有零阶 1，所以 h 有零阶 3。式 P3 排除了所有其他极点，包括 cusps。

为避免 odd weight 的 −I 问题，下文采用 Γ=Γ(7)，不含 −I，并在有限数域 K 上使用具有完整 level-7 结构的普遍椭圆曲线。Γ₀(7)/Γ(7) 有 42 个元素；粗曲线覆盖度为 21。−7 点的 Γ₀ stabilizer 为 {±I}，所以有 **21 个 Γ(7) lift**；两个 −3 轨道各有 stabilizer 阶 6，各有 7 个 lift，共 **14 个 lift**。∞、0 两 cusp 分别有 3、21 个 lift，ramification 分别为 7、1；h 的 cusp 零阶分别为 21、3。这里只使用轨道与零阶，不依赖数值计算或新 prime。

## 3. 完整 principal parts：−3 与 −7 的区别

令 S=Dt/t。Yang 的真实恒等式

\[
A=\frac{S^2}{f}\frac{t}{(1-t)(1-28t)}
\tag{P5}
\]

与 f 在上半平面不消失一起，给出 A 在 −3 点的零阶为 1，在 −7 点不消失。

### 3.1 判别式 −3：只有三阶 Laurent 项

固定任意 −3 lift u。写 δ=τ−u，`A(τ)=A′τ(u)δ+O(δ²)`，且 `A′τ(u)≠0`。在 t=1，L 的 homogeneous exponents 为 1/3、2/3。非齐次方程 `LB₃=t³` 有 analytic particular solution，常数项由 `−6B₃(1)=1` 决定；其余 homogeneous 项在 τ 坐标变成 holomorphic 的 δ、δ² 项。因此

\[
E_3(\tau)=-\frac{1}{6A'_\tau(u)}\delta^{-1}+H_u(\tau),
\qquad H_u\text{ holomorphic}.
\tag{P6}
\]

这是完整 principal part，不要求 B₃ 的某个特殊 branch。对 P6 二次微分并用 P2，得到

\[
\boxed{h(\tau)=\frac{1}{12\pi^2A'_\tau(u)}\delta^{-3}+O(1).}
\tag{P7}
\]

特别地 **δ⁻²、δ⁻¹ 两项严格为零**。这比只观察三阶 pole 更强：weight 3 的第二类条件正是所有上半平面 poles 的这两个系数消失。

### 3.2 判别式 −7：不可消去的 affine log

在 w=(7+i√7)/14，令 δ=τ−w，d=w−w̄，A_w=A(w)≠0。冻结稿的真实 infinity 展开为

\[
B_3=\frac1{14}v_0(z)\log z+\text{analytic in }z
+b\,v_{1/2}(z),\quad z=1/t,\quad v_0(0)=1.
\tag{P8}
\]

完整 homogeneous space 在 τ 坐标为 `A·span{1,τ}`。故 v₀/A 是 affine。固定 w 的 Γ₀(7)+W₇ 矩阵可取

\[
\gamma=\frac1{\sqrt7}\begin{pmatrix}7&-4\\14&-7\end{pmatrix},
\quad\gamma'(w)=-1.
\]

A 的 weight-one 变换为 `A(γτ)=ν(14τ−7)A(τ)/√7`，ν=−i，且 w 处乘子为 1。微分得到

\[
\frac{A'_\tau(w)}{A_w}=-\frac1{w-\bar w}.
\tag{P9}
\]

这里 ν 可由 P5 与 η 的 Fricke 变换直接推出；不从数值拟合它。由于 z′τ(w)=0，v₀/A 的值、导数分别为 `1/A_w`、`−A′τ(w)/A_w²`，从而完整 affine 函数是

\[
v_0/A=\frac{\tau-\bar w}{A_w(w-\bar w)}.
\tag{P10}
\]

`z=δ²·(analytic unit)`，所以 P8 给完整局部表示

\[
\boxed{E_3(\tau)=\frac{\tau-\bar w}{7A_wd}\log(\tau-w)+H_w(\tau),
\quad H_w\text{ holomorphic}.}
\tag{P11}
\]

二次微分得完整二阶 principal part

\[
\boxed{h(\tau)=K_w\left(\delta^{-2}-d^{-1}\delta^{-1}\right)+O(1),
\qquad K_w=\frac1{28\pi^2A_w}.}
\tag{P12}
\]

这同样适用于所有 Γ₀(7) images：用对应 A_w、d。微分公式也符合 weight 3 的 covariance；不能只保留 δ⁻²而漏掉 δ⁻¹。

## 4. 真正代数留数：精确 −η′/7

采用 BF 的 Betti 归一化

\[
\omega_h=(2\pi i)^2 h(\tau)(X-\tau Y)\,d\tau.
\tag{P13}
\]

由 P12，先在 Betti 基底中直接计算：

\[
\boxed{\operatorname{Res}_w\omega_h
=\frac{X-\bar wY}{7A_w(w-\bar w)}\ne0.}
\tag{P14}
\]

验证符号：未乘 `(2πi)²` 的 residue 为
`−K_w[d⁻¹(X−wY)+Y]=−K_wd⁻¹(X−w̄Y)`；乘 `−4π²` 后得到 P14。在 −3 点，P7 乘 affine `X−τY` 无 δ⁻¹项，故向量留数为零。

为了付清 P14 中的周期，取 K 包含完整 level-7 marked CM 点的定义域及 CM fields。这里仅断言存在这样的有限数域，不猜它的最小次数。q-expansion principle 下

\[
[\omega_q]=2\pi i(X-\tau Y),\qquad
[\omega_A]=A(\tau)[\omega_q]
\tag{P15}
\]

是实际代数 Hodge 微分；A 的 Fourier 系数有理且 weight 为 1。取 w 处 `[ω]=[ω_A]`，第一周期为 **ω₁=2πiA_w**。选 K-代数 symplectic CM eigenbasis `[ω],[η′]`，`⟨ω,η′⟩=1`，其中 η′ 属于与 ω 相反的 CM 特征线。BF Lemma 6.3、6.4、Remark 6.6 的精确公式为

\[
\operatorname{comp}^{-1}(X-\bar wY)
=\frac{\omega_1}{2\pi i}(\bar w-w)[\eta'].
\tag{P16}
\]

P16 的共轭和符号已实际渲染目读 BF PDF34、36；不能用丢失 overline 的文本提取代替。将 P16、ω₁=2πiA_w 代入 P14：

\[
\boxed{\operatorname{Res}^{\mathrm{dR}}_w[\omega_h]=-[\eta']/7.}
\tag{P17}
\]

因此 h 的实际 punctured de Rham 类映到一个明确的 **代数 CM fiber eigenvector**，而非“某个未知周期倍数”。所有 21 个 lift 都按自己的 ω_A、symplectic η′ 给 P17。非零 residue 在有限 cover 下仍非零；它不能由全球 meromorphic weight −1 的 Bol 二阶导消去。

这一结论来自已证明的代数 comparison 与原始 L 的 local log，不使用 BF 的 odd-weight Rankin–Selberg conjecture，也不将 C₃替换为别的 period。

## 5. 显式第三类 kernel 与 K-系数分解

### 5.1 指定解析 kernel 的精确分解

对 Γ=Γ(7) 定义 BF 实际 kernel

\[
\psi^{1,0}(\tau,w)=\frac{w-\bar w}{(\tau-w)^2(\tau-\bar w)},\qquad
\Psi^{1,0}_\Gamma(\tau,w)
=\sum_{\gamma\in\Gamma}j_\gamma(\tau)^{-3}\psi^{1,0}(\gamma\tau,w).
\tag{P18}
\]

Γ 不含 −I，w 无 stabilizer。weight 3 series 绝对且 locally normally 收敛（离 pole 集），在所有 cusp 消失；BF Proposition 3.3、Corollary 3.11 给其 sole orbit pole 的完整 principal part。直接展开

\[
\psi^{1,0}(\tau,w)=\delta^{-2}-d^{-1}\delta^{-1}+O(1).
\]

令 w₁,…,w₂₁ 是 −7 lift 的 representatives，K_i=1/(28π²A(w_i))。则

\[
\boxed{h^{(2)}_{\rm an}
=h-\sum_{i=1}^{21}K_i\Psi^{1,0}_\Gamma(\tau,w_i)}
\tag{P19}
\]

只有 14 个 −3 lift 的纯三阶 poles，且 cusp constant terms 全为零。依 GZ PDF9–10 的字面定义，P19 是真正 weight-3 **meromorphic cuspform of the second kind**。h 本身不是第二类。

每个积分在 imaginary axis 上都合法：Γ₀(7) 的 CM−7、−3 orbit 均不能落在该轴，因为 primitive quadratic 的 middle coefficient 若为 0，discriminant 必为 4 的倍数。kernel 在两个积分端 cusp 消失。故 P2 精确成为

\[
\boxed{C_3=\sum_{i=1}^{21}K_i\mathcal I(\Psi^{1,0}_\Gamma(\cdot,w_i))
+\mathcal I(h^{(2)}_{\rm an}),\quad
\mathcal I(g)=4\pi^2\int_0^\infty y g(iy)\,dy.}
\tag{P20}
\]

这是固定对象的 exact formula，不是把任意 log2 或别的 complex constant 偷放进 forcing。

### 5.2 留数归一化的 K-Fourier 第三类 form

BF Theorem 7.2、equation (7.4) 给每个 w_i 一个 K-Fourier weight-3 form g_i：

\[
g_i\text{ vanishes at cusps, has poles only at }\Gamma w_i
\text{ of order}\le2,\qquad
\operatorname{Res}^{\rm dR}_{w_i}\omega_{g_i}=[\eta_i'].
\tag{P21}
\]

这里用 m=1,n=0、Γ_{w_i}={I}，所以 BF 的 κ^{1,0}_{Γ,w_i}=1。该 form 由 residue sequence 构造，不唯一；本文不虚称已经得到其 finite Fourier formula。其存在是已证明 theorem 的实际实例，不依赖 odd-weight conjecture。

设 ρ₀=−Σg_i/7。它的所有向量留数与 h 相同。对一个 pole≤2 的 form，系数 `(a₋₂,a₋₁)` 的 residue 映射

\[
(a_{-2},a_{-1})\longmapsto
(2\pi i)^2\bigl(a_{-1}(X-wY)-a_{-2}Y\bigr)
\tag{P22}
\]

是单射。因此 ρ₀与 h 在所有 −7 点有完整相同的 principal parts，而非仅同一个 scalar residue。

还可恢复真正 Γ₀(7),χ 对称性。取 slash 为 `(g|₃γ)(τ)=jγ(τ)⁻³g(γτ)`，并令

\[
\rho=\frac1{42}\sum_{\gamma\in\Gamma(7)\backslash\Gamma_0(7)}
\chi(\gamma)^{-1}(\rho_0|_3\gamma).
\tag{P23}
\]

Γ(7) 正规，χ 在其上为 1；χ(−I)=−1 与 weight3 的 sign 配合，所以 P23 不是错误的 −I 平均。有限群投影保留 K-Fourier 性、cusp vanishing、−7 pole divisor，并因 h 已 χ-equivariant 而保留它的完整 principal parts。于是

\[
\boxed{h=\rho+h^{(2)}_K,\qquad
\rho,h^{(2)}_K\text{ have K-Fourier coefficients and character }\chi,}
\tag{P24}
\]

ρ 只有 −7 二阶 poles；h²_K 只有 −3 纯三阶 poles。两者都 cusp-vanishing，故 `C₃=I(ρ)+I(h²_K)` 收敛且精确。这给出实际数域定义的第三类/第二类 comparison，而非仅复系数 decomposition。

P19 与 P24 的 cusp 分量仍须区别。BF Proposition 7.5 在 ω₁=2πiA(w_i) 的归一化下给

\[
\Psi^{1,0}_\Gamma=(2\pi i)\omega_1g_i+c_i,\qquad
K_i(2\pi i)\omega_1=-1/7,
\tag{P25}
\]

其中 c_i 是有 complex coefficients 的 holomorphic cuspform。式 P25 再次精确核对 P17 的 sign 和 period cancellation；**不能把 ΣK_ic_i 当成已知 Q-系数的 f 倍数或免费略去**。

## 6. 第二类的二维部分、相对端点与 elliptic-log 排除

f 在上半平面无零，在 Γ₀(7) 两个 cusp 的 native order 都是 1。因此任意 `g∈S₃(Γ₀(7),χ)` 的 g/f 是 compact X₀(7) 上无极点的函数，必为常数：

\[
\boxed{S_3(\Gamma_0(7),\chi)=\mathbf C f.}
\tag{P26}
\]

在 Γ(7) 上应用 GZ 的 second-kind/Bol quotient，再取 P23 的 χ-eigensummand；Eichler–Shimura identification 及 complex-conjugate summand 给 χ-parabolic quotient dimension 2。χ 为实 character，K-base change 后仍是二维。故 h²_K 的 class 位于某个 K-basis `[f],[F]` 的 span，其中 F 是一个 K-defined second-kind representative；这是一条可付费的有限维接口。

但本文没有算出实际 coefficients `[h²_K]=a[f]+b[F]`，也没有规范 F 的 cusp primitive。即使以后得到
`h²_K−af−bF=D²G`，在 **相对 cusp path** 上也必须保留

\[
\mathcal I(D^2G)=\bigl[y\,\partial_yG(iy)-G(iy)\bigr]_{y=0}^{y=\infty}
\tag{P27}
\]

（若 divergent 则须指定 regularization），不能从 absolute cohomology 的 exactness 推出 Mellin integral 为零。P27 由 `D=(2πi)⁻¹∂τ`、`∂y=i∂τ` 直接分部积分，符号包括 P2 的 4π²。当前可靠的数值公式是 P20/P24 的 convergent integrals。

另有一个严格排除：E₃不能在 −7 点邻域成为真实 smooth elliptic family 的 **algebraic section 的 elliptic logarithm**，即使允许 finite algebraic base change 和加 homogeneous affine period。证明不需要把文献 abstract theorem 套上去：在该 smooth fiber 上，代数 section 经有限 cover 去掉 algebraic ramification 后，由 properness 延拓为 holomorphic section；局部指数映射可取 holomorphic logarithm，差别只有 holomorphic periods。P11 的非零 affine×logδ 在 `δ=s^N` 后仍含 Nlog s，加 affine period也不能消去，矛盾。此排除限于 smooth fiber 上的 algebraic section，不排除 punctured normal functions、regulators、higher extensions 等确可有 log 的对象。

局部 principal parts 本身也不能唯一给出 C₃：加 a·f 不改变全部 finite poles/residues，却将 I 值改为 `C₃+aκ`。这里 h 已固定，当然不能任意改它；这个例子说明从 local residue 数据跳到数值公式会丢失实在的 parabolic/endpoint 分量。

## 7. 与新特殊值结论的实际距离

本轮正面结果是：实际 B₃并不是未指定的“某个椭圆周期”。它的新增 local extension precisely targets **21 个 CM−7 fibers 的代数对偶 CM eigenvectors −η′/7**；−3 点只有第二类 poles。P24 建立了 K-定义的 third-kind/second-kind decomposition；P26 把后一 absolute parabolic class 限定到二维。

还缺三项，不能并成一句存在性：选出实际 χ-descended ρ 的明确 algebraic formula；计算 h²_K 在规范第二类基底的分量；支付 relative cusp path 的 full boundary constants。完成后才有可能把 C₃化成可命名的 CM-extension period、quasiperiod 或某个已证 Rankin/regulator value。BF odd-weight k=1 的 conjectural comparison 不承担这些任务。本文没有证明 C₃的无理性、C₃与κ的数值线性无关性，或 log2 型 carrier；原 ξ 与原完整源费用也没有改动。

这同时给下一步明确审核目标：任何特殊值公式必须与 P7/P12 的完整 Laurent principal parts、P17 的 algebraic residue，以及 P2 的 normalized cusp-to-cusp integral 同时一致。

## 8. 本轮原件、读域与可复核记录

个人本轮实际完整 primary PDF 页域（不继承同行或旧轮）：

- Yang 固定 v1，`literature/yang2007_apery_limits_v1_20261006.pdf`，SHA `691258e04fb3f9f9fa6a4cc144c8be99d587d0af47f96cbf138ac797a1025109`：PDF **5–6、15–16**，4 distinct 页。原件 [arXiv v1](https://arxiv.org/pdf/0709.1968v1)。
- Golyshev–Zagier 现有 author preprint，`literature/cdt_gamma_relative_chain_sources_20261007/golyshev_zagier_interpolated_apery_motivic_gamma_author.pdf`，SHA `529a92d1ba0744e00c3d26ea97400ae3da25b0615dea5dacbaa0b3f25697d669`：PDF **9–10**，2 distinct 页。复用现有原件，没有另下 published PDF。
- Brown–Fonseca 固定 v2，`literature/cdt_gamma_level7_punctured_sources_20261007/brown_fonseca2025_single_valued_meromorphic_arxiv2508_04844v2.pdf`，SHA `17f8556f14261236af621695799387065cd70dae4295b52f3ee6e82d28593a66`：PDF **13、15–17、26、29–30、33–39**，14 distinct 页。原件 [arXiv v2](https://arxiv.org/pdf/2508.04844v2)。使用已证 Proposition 3.3、Corollary 3.11、Lemma 6.3–6.4、Remark 6.6、Theorem 7.2、Proposition 7.5；不使用 odd-weight conjectural comparison。

个人总计 **20 distinct primary PDF 页**。依 PDF skill 实际渲染目读 BF PDF **13、34、36、39**，尤其核 ψ 分母、共轭、P16 的负号和 P25 的 `(2πi)ω₁`。这是 visual 核对，不新增 distinct 页。

本轮 primary 搜索也发现 Corvaja–Zannier 的 *Unramified sections of the Legendre scheme and modular forms* 及其 Corrigendum 信息，但未下载、未把其中 theorem 当证明输入；上文 elliptic-log 排除给出独立 local proof。没有新下载原件，因此没有绕过全138 fingerprint 去重流程或发生 TLS 降级。本文不创建或执行任何数学 producer，不 import/rerun 旧/同行数学程序，不执行 guard/Lean，不扩 prime 表。仅 PDF 文本提取/渲染和 hash、JSON 等 documentary 操作。旧620记录保持只读。

本稿在正式 incoming FULL review、作者最后 FULL 回读之前不冻结 FINAL receipt；receipt 不 pin mutable main、peer receipt 或 future audit。
