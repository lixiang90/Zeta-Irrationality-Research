# 第261轮：同一 mixed 关系在 t=∞ 的必坏实芽与精化入口上界

2026-10-10；punctures 子任务。仅核第259–260轮已经固定的同一关系函数、最小整数坐标与 CDT 的 holomorphic-map 接口。本轮不做图或参数优化；数学程序、CAS、数值计算、地图/prime/Padé扫描均0。没有新的数值无理性或线性无关性定理。

**第一证书：反证中的 bare 关系本身必须省略两个有限实点 s=(1±√3)/2，不能只把它们算作扩充 pure 族的费用。** 因此所有合规 holomorphic φ 都满足 λ=log|φ′(0)|<7/4<16/9。固定 bare safe type 的 CDT 8.0.4/8.0.5 仍无正分母；仅改 numerator 的 Bost–Charles/convexity 修正无法救该入口。这个结论不排除另有已付的更低算术 type、不同 map 定理或新来源。

## P1. 固定对象及实际读取范围

Actual FULL 读第259轮 field、mixed、Root gate 三份最终稿，第260轮 analytic、arithmetic 两份最终稿，以及原件节选 Kim–Ma–Ma 物理1–2页、固定 CDT v2物理122–124页。没有把这些节选称为整篇 PDF FULL，也不继承作者未在本轮实际读取的 primary 页域。本轮 primary 节选以 punctures_* 名称保存在 literature/refined_budget_round261_20261010；具体 scope 另列。

沿用已付的真实函数

\[
H=A(a+bB_3+cC_3+dB_4),\qquad a,b,c,d\in\mathbf Q,\quad d\ne0,
\]

其中 d≠0 来自 CDT 已知的前三项线性无关性。固定最小场为 Q(s)，

\[
r=1-2s,\qquad t=\frac{1-r^4}{9-r^4},\qquad
p=t(1-t)(1-9t),
\]
\[
\mathcal D_t=p\partial_t^2+p'\partial_t+3(-1+3t),\qquad
\mathcal D_tH=b+\frac{c}{1-t}+dR_4,
\quad R_4=\frac{(3+r^2)^3}{32r(1+r^2)}.                 \tag{P1.1}
\]

两个齐次实际解为 A、τA。第260轮已付 r=±i 的所有到达叶非零 log²，因此 s=(1±i)/2 必须省略。本轮不重证这两个芽，也不靠它们取得下面更强上界。

本轮只取 t=∞ 的实两 fiber r=±√3；不续完整十 cusp 分类。与260 pure-only 的省略证书不同，下面使用 H 的实际 inhomogeneous resonance，故适用于没有增加 pure 行的 bare tuple。

## P2. 两个实 fiber 的准确 forcing 常数

置 z=1/t=(9-r⁴)/(1-r⁴)。在 r₀=±√3，分母为−8，且

\[
z(r_0)=0,\qquad \left.\frac{dz}{dr}\right|_{r_0}
=\frac{r_0^3}{2}=\frac{3r_0}{2},\qquad
\left.\frac{dz}{ds}\right|_{r_0}=-3r_0\ne0.             \tag{P2.1}
\]

因此 z 是两点的真实未分歧局部参数，不是一个未支付的形式坐标。在这两点 R₄ 本身解析，**没有 forcing pole**，但有

\[
R_4(r_0)=\frac{6^3}{32r_0\cdot4}
=\frac{27}{16r_0}=\pm\frac{9\sqrt3}{16}.
\]

并且 c/(1-t)=cz/(z-1)=O(z)。故完整 forcing 为

\[
F(z):=b+\frac{c}{1-t}+dR_4=F_0+O(z),\qquad
F_0=b\pm\frac{9\sqrt3}{16}d.                            \tag{P2.2}
\]

因为 b,d∈Q 且 d≠0，两种符号的 F₀ 均非零；否则 √3 将为有理数。a 只改变一个齐次解，c 没有常数项，均不能取消 F₀。这一步明确使用**反证关系的有理系数**，没有假设 generic relation，也不把任意复系数强行纳入结论。

## P3. 双重指数1的完整 resonance：所有到达叶均坏

把 p=9t³−10t²+t、∂t=−z²∂z 逐项代入，得到准确算子

\[
\mathcal D_tH=z(9-10z+z^2)H''+(-9+z^2)H'
 +(9/z-3)H.                                            \tag{P3.1}
\]

等价地，θz=z∂z 时

\[
z\mathcal D_tH=(9-10z+z^2)\theta_z^2H
 +(-18+10z)\theta_zH+(9-3z)H.
\]

首算子为9(θz−1)²，所以两个齐次指数均为1。置 H=zY、Q(z)=9−10z+z²，进一步有**完整恒等式**

\[
\boxed{\mathcal D_t(zY)
=z\{(zQ(z)Y')'+(z-3)Y\}.}                             \tag{P3.2}
\]

对应的齐次 Y 方程为 (zQY′)′+(z−3)Y=0；其解析 Frobenius 解 V 满足 V(0)=1，另一齐次解是 Vlog z+W，W 解析。双根0的标准 Frobenius 递推在 n≥1 的新系数上具有非零9n²，支付 V 的存在与收敛；没有使用有限头猜测。

由 (P3.2)，Y 方程右边为 F(z)/z。以 V 化简得到准确 variation identity

\[
\boxed{(zQ V^2(Y/V)')'=V\,F(z)/z.}                    \tag{P3.3}
\]

右边 F₀/z+O(1)，左内系数 zQV²=9z(1+O(z))。在任一小扇形连续两次积分，因此每一个局部到达解都有

\[
\boxed{H(z)=\frac{F_0}{18}\,zV(z)\log^2z
       +O(z\log z)+O(z),\qquad F_0\ne0.}               \tag{P3.4}
\]

这里首项的完整解析因子 V(0)=1；低阶 log 与解析部分依赖到达路径。任意两条到达叶之差是同一齐次方程的解，所以只含 zV 及 zVlog z+zW，不能取消非零二次 log 首系数。换一个 log branch 也只改变一次 log 和解析部分。故这不是 canonical leaf 的单侧渐近，而是**所有到达叶**的局部非亚纯性证书。

另可直接审计 (P3.1)：假设 H 是 meromorphic Laurent 解，最低负阶的9(n−1)²不可能匹配 RHS 的 F₀z+O(z²)，故无负阶；零阶同样迫0；指数1的左边 resonance 系数为0，而右边指数1为 F₀≠0，矛盾。此审计与 variation identity 相互独立地排除了“有极点可吸收 forcing”的误领。

有限分歧不能修复此芽。若 z=κwᵉ(1+O(w))，κ≠0、e≥1，则 H 的首非亚纯项为

\[
\frac{F_0\kappa e^2}{18}w^e\log^2w,
\]

系数仍非零；解析因子及 log branch 的改变只能加入较低 log。正幂乘 log² 仍有无限局部 monodromy，不能成为 Laurent 亚纯芽。任何非恒定 holomorphic φ 若命中该点，命中阶有限且正，故其 pullback 同样非亚纯。于是 bare H 已经强迫

\[
\boxed{\phi(\mathbb D)\cap\{\alpha,\beta\}=\varnothing,
\qquad \alpha=\frac{1-\sqrt3}{2},\quad
\beta=\frac{1+\sqrt3}{2}.}                             \tag{P3.5}
\]

只要 H∘φ 需要 meromorphic，此必要条件就成立；无需另外分析 θsH，也不受潜在数值关系填掉 s=1/2 指定芽影响。

## P4. 虚两 fiber 的边界：不能从 forcing 外观免费再领省略值

在 r₀=±i√3，z仍是未分歧参数，但 3+r² 有 simple zero，R₄=O(z³)，因此 F(z)=b+O(z)。若 b≠0，同一推导给 H 首项 (b/18)zVlog²z，两个虚点也必省略。

然而本反证范围允许 b=0。此时 F(z)=O(z)，(P3.3)右边为解析函数；选积分常数使第一积分在 z=0 为0，就得到一个解析的 Y，故 H=zY 是局部解析解。也可用9n²≠0的递推逐阶构造并由 Frobenius 得收敛。实际全局 H 的连接常数可能留下一次 log，但本轮没有支付这种连接数据。因此**没有断言 b=0 时实际所有叶可填，也没有断言两个虚点必须省略**。这是一个 forcing-only 判据的明确限制，不是局部解被免费认作实际 H。

同样若允许任意复 b，实某一 F₀可以为0，所以 (P3.5) 不适用于那种被扩大后的关系类。当前 Q 关系恰已排除该例外。

## P5. 同一 holomorphic 图的严格 derivative cap

Primary 使用 Kim–Ma–Ma, *Estimates of the hyperbolic metric on the twice punctured plane*, Ann. Acad. Sci. Fenn. Math. 40 (2015), 875–887，物理1–2页，DOI [10.5186/aasfm.2015.4058](https://doi.org/10.5186/aasfm.2015.4058)。曲率−1，disk 密度2/(1−|z|²)；原件 (1.2)、(1.3) 及紧接的 Landau 结论是

\[
K_L=\frac{\Gamma(1/4)^4}{4\pi^2},\qquad
|f'(0)|\le2|f(0)|\bigl(|\log|f(0)||+K_L\bigr)
\]

对 holomorphic f:D→C\{0,1}。令 f=(φ−α)/(β−α)，φ(0)=0，则

\[
|f(0)|=\frac{\sqrt3-1}{2\sqrt3},\quad
|\phi'(0)|\le(\sqrt3-1)\{\log(3+\sqrt3)+K_L\}.          \tag{P5.1}
\]

使用260已付且本轮纸面复核的严格积分 Cauchy–Schwarz：
Γ(5/4)²<Γ(1)Γ(3/2)=√π/2，Γ(1/4)=4Γ(5/4)，所以 K_L<16/π<16/3。√3<7/4 给 √3−1<3/4；3+√3<5，而 exp2>1+2+2=5，所以 log(3+√3)<2。于是

\[
\boxed{|\phi'(0)|<\frac34(2+16/3)=11/2.}              \tag{P5.2}
\]

不使用十进制近似、数值程序或地图拟合。进一步，exp(7/4) 的0–4项正 Taylor 和为

\[
1+\frac74+\frac{49}{32}+\frac{343}{384}
 +\frac{2401}{6144}=\frac{34193}{6144}
 >\frac{33792}{6144}=\frac{11}{2}.
\]

因此严格得到

\[
\boxed{\lambda=\log|\phi'(0)|<\log(11/2)<7/4<16/9.}     \tag{P5.3}
\]

该上界属于整个合规 holomorphic 图类别，不是某个候选图的 safe upper，也不是关于 actual numerical error 的 lower bound。若 φ 只 meromorphic 并容许极点，本 Landau 结论不能直接使用；该不同接口未付。

## P6. 对当前精化预算的决定

第259轮 bare tuple (1,C₀H,C₀θsH) 的 actual rank3、两列(0,1,1)、e=0与全prefix dN² 已付，τ=τ♭♭+τ♯=16/9。固定 CDT v2物理123页的 Theorem8.0.1 明文要求 λ>τ（已 holonomic 的分支）；(8.0.4)、(8.0.5) 的 Bost–Charles/convexity 修正只减 numerator，分母依然 λ−τ。

本轮 (P5.3) 给 λ−16/9<−1/36。故在这个 fixed safe type、同一坐标/来源和 holomorphic-map 入口，**连正分母条件都不可能成立**，不是 numerator 是否够小的微调问题。仅支付8.0.4或8.0.5凸性修正而不改变实际算术 type，不能准入；本轮不继续该修正的地图/半径实现。

对一个仍使用本 holomorphic 图界但另有真实新算术 type 的未来入口，λ>τnew 的必要条件是 τnew<log(11/2)；相对当前 type，必要节省严格大于16/9−log(11/2)>1/36。它仅是必要改进幅度，不是已付新 type，也不是最终 rank 矛盾的充分严格余量。若另换关系架构、来源或 map 定理，要重新列同对象域与完整账本，不能把本界外推成全部方法 no-go。

本轮的有界第一证书已经回答任务：两实点属于 bare 的实际全叶坏芽，其 cap 小于16/9。停止 fixed bare safe-type 的默认凸性优化；不续完整十 cusp、maps、参数或 Padé。保持所有真实投影/field/rank/整模型资产，数值目标仍未证明。Parent的算术分支另审实际 finer type，本稿不预领其结果，不修改260 manifest、main、policy，也不执行archive。
