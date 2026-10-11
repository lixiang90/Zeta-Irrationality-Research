# 第259轮固定混合来源：CDT单位周期与卡塔兰完整坏芽

2026-10-10。任务标识 mixed12 沿用最初文件名；实际共同 level 为 **24**，不能把对象称为 X0(12)。唯一固定候选是 CDT 的 A₃、B₃、C₃ 加上 B₄(q)=Σχ₋₄(n)qⁿ/[n²(1+qⁿ)]，目标仍为 1、ζ(2)、L(2,χ₋₃)、G=β(2) 的四项 Q 线性无关。本稿只证明实际 cusp0 的关系提升第一证书；**没有四项数值独立定理，没有实现准入或严格 holonomy 预算。** 数学程序与参数/prime/map 扫描均0。

## M1. 固定对象、level纠正与去重边界

记 q=e^(2πiτ)，τ∈H，χ₋₄(2j+1)=(-1)^j、χ₋₄(2j)=0。采用固定 CDT v2 physical160–162 的精确源

\[
\Theta_3(\tau)=\sum_{m,n\in\mathbf Z}q^{m^2+mn+n^2},\qquad
A_3=\frac{\Theta_3(\tau)+\Theta_3(2\tau)}2,
\]
\[
B_3=\sum_{n\ge1}\frac{\chi_{-3}(n)q^n}{n^2(1+q^n)},\qquad
C_3=\sum_{n\ge1}\chi_{-3}(n)
\left\{\operatorname{Li}_2(q^n)-\tfrac14\operatorname{Li}_2(q^{2n})\right\}.
\tag{M1}
\]

新增固定通道及实际函数是

\[
K_4(q)=\sum_{n\ge1}\frac{\chi_{-4}(n)q^n}{n^2(1-q^n)},\quad
B_4=K_4(q)-2K_4(q^2),\quad H_4=A_3B_4.
\tag{M2}
\]

M2 的等式逐项来自 r/(1−r)−2r²/(1−r²)=r/(1+r)。若 δ=q∂q，则 δ²B₄=E₃,χ₋₄,₁(τ)−8E₃,χ₋₄,₁(2τ)，这是 level8、characterχ₋₄ 的 oldform组合；A₃/B₃/C₃ 使用 level6、characterχ₋₃。因此自然实际共同群是 Γ0(24)，不是 Γ0(12)。本稿不声称已分类所有可能更小的非标准群/商。

有限固定关键词检索没有找到已经记录的这个四项混合 tuple。实际全文核旧218 Lambert carrier、219 Legendre connection、旧 level12 χ12 paired coordinate，并选读220策略 §1–4及旧 Catalan–π²几何 §1：旧218已经证明下面所用 K₄ reciprocity，旧219/220指出未滤波 FK₄仍有 log²，关系补点未过；旧χ12 level12源是另一个 weight4/L(3,χ12) 来源，旧 Catalan–π²几何是 arctan/Ti₂ 悬挂积分。**本稿复用218已有 reciprocity，不把它算作新引理；新增的是固定 dyadic滤波、CDT unit carrier与实际共同 cusp cover 的完整组合。** 有限去重不是全球新颖性证明。

## M2. 精确倒数变换：保留线性τ项及全部dual series

令 u=−2πiτ，Re u>0，定义

\[
\mathcal D(r)=\sum_{m\ge1}\frac{r^m}{m^2(1+r^{2m})},\qquad |r|<1.
\tag{M3}
\]

其级数在紧子圆绝对一致收敛。旧218 §6 eq13–17 已完整纸证的实际恒等式是

\[
K_4(e^{-u})=
\frac{\pi^3}{32u}-\frac G2+\frac{\pi u}{48}
-\frac{u}{4\pi}\mathcal D(e^{-\pi^2/u}).
\tag{M4}
\]

为说明原式并非径向渐近：Mellin kernel 是 Γ(s)ζ(s)β(s+2)。从 Re s>1 移至 Re s=−3/2只穿过s=1,0,−1，残数依次是π³/(32u)、−G/2、πu/48；函数方程给

\[
\Gamma(s)\zeta(s)\beta(s+2)
=-\frac\pi4\pi^{2s}\Gamma(-s-1)\zeta(1-s)\beta(-s-1).
\tag{M5}
\]

以z=−s−1换元，残余积分由1/(2cosh x)的Mellin transform Γ(z)β(z)识别为 M4 最后一项。交错 kernel 的有限和由e^(−x)控制，ζ(z+2)求和在 Re z=1/2绝对可和；竖线衰减和水平边消失由Stirling及固定带内的Euler–Maclaurin/Abel界支付。所用 primitive Dirichlet 与ζ函数方程是 NIST DLMF25.15.5–6、25.4.2。旧218全文已实际核读；本轮另核这些 primary formulas，不重新执行任何旧producer。

M4最初在u>0成立。两边在Re u>0全纯，且Re(1/u)>0，所以恒等定理给整个右半平面，从而给实际τ∈H的恒等式，而非仅一条径向极限。

对固定B₄直接计算M4(u)−2M4(2u)，主π³/u精确消去，得到

\[
B_4-\frac G2=-\frac{\pi u}{16}
+\frac u\pi\mathcal D(e^{-\pi^2/(2u)})
-\frac{u}{4\pi}\mathcal D(e^{-\pi^2/u}).
\tag{M6}
\]

取 cusp0 坐标

\[
w=-\frac1{24\tau},\quad q_0=e^{2\pi iw},\quad
T(q_0)=\Theta_3(8w)+\tfrac12\Theta_3(4w).
\tag{M7}
\]

则u=−2πiτ，M6准确成为

\[
\boxed{B_4-\frac G2=i\tau
\left\{\frac{\pi^2}{8}-2\mathcal D(q_0^3)
+\tfrac12\mathcal D(q_0^6)\right\}.}
\tag{M8}
\]

τ线性项与两个dual series均保留。删去它们会破坏下面的完整坏芽论证。

## M3. 非平凡单位载体的完整坏芽

对Gram矩阵 [[2,1],[1,2]] 用二维Poisson公式。其det=3，逆阵经n↦−n等价于原阵的1/3倍，故正虚轴确定正号后有

\[
\Theta_3(-1/(3\tau))=-i\sqrt3\tau\Theta_3(\tau).
\tag{M9}
\]

代入τ、2τ并用M7得

\[
\boxed{A_3=\frac{i}{2\sqrt3\tau}T(q_0)
=-\frac{2\sqrt3}{\pi}T(q_0)\log q_0.}
\tag{M10}
\]

T∈C[[q₀⁴]]，T(0)=3/2。乘M8立即得到实际完整恒等式

\[
\boxed{H_4-\frac G2A_3
=-\frac{T(q_0)}{2\sqrt3}
\left\{\frac{\pi^2}{8}-2\mathcal D(q_0^3)
+\tfrac12\mathcal D(q_0^6)\right\}.}
\tag{M11}
\]

右边在q₀=0有完整收敛Taylor series。因此在真实q₀ cusp coordinate 的“germs模亚纯germs”空间中，

\[
[H_4]=\frac G2[A_3].
\tag{M12}
\]

这是整个坏芽对齐，包含全部τ项和dual corrections，强于B₄(q→1)=G/2。A₃的非零log坏芽直接由T(0)=3/2证实；不是用常函数1作为单位carrier。

CDT Lemma11.1.4在其原生x₆ coordinate证明 A₃B₃−L(2,χ₋₃)A₃/2 和 A₃C₃−ζ(2)A₃/4 完整全纯。拉回q₀保持全纯。故对任意固定复系数a,b,c,d，令

\[
F=aA_3+bA_3B_3+cA_3C_3+dH_4,
\quad R=a+bL(2,\chi_{-3})/2+c\zeta(2)/4+dG/2.
\tag{M13}
\]

有[F]=R[A₃]，且F在q₀=0亚纯当且仅当R=0（此时实际全纯）。因此潜在的四项Q关系确实消去一个实际完整坏芽；**M13自身不是数值关系不存在的证明。**

## M4. 精确finite ramification：不得在CDT旧底免费补点

固定CDT坐标x₆在Γ0(6)cusp0的width是6，而Γ0(24)该cusp的width是24。CDT uniformization x₆是该旧曲线的degree1 coordinate，在该cusp有x₆=1/9，因此

\[
x_6-1/9=cq_0^4+O(q_0^8),\qquad c\ne0.
\tag{M14}
\]

T所有非constant幂均至少q₀⁴，D(r)=r+O(r²)。M11 的q₀³系数是

\[
-\frac{3/2}{2\sqrt3}(-2)=\frac{\sqrt3}{2}\ne0.
\tag{M15}
\]

因gcd(3,4)=1，M11在旧x₆底上的完整局部ramification index **恰为4**。具体地，减去q₀常数项后首项为非零q₀³，旧底的正向loop把它乘以e^(2πi·3/4)；任何小于4的循环幂不能恢复。四次local pullback让所有整数q₀幂单值。

因此M11只证明在实际level24 cusp/其character cover上全纯，不能写成“x₆=1/9已亚纯”或沿用CDT原P¹图。即使数值关系消掉log，d≠0的卡塔兰项还留下这个有限四叶障碍；完整关系组合的B₃/C₃ residual仅含q₀⁴倍幂，不能取消M15。Γ0(24)→Γ0(6)degree4，并在这个cusp完全分歧；全field与character背景必须进入后续共同图。

## M5. 算术已付范围与后续第一门槛

A₃∈Z[[q]]。B₃、C₃、B₄的每个degree≤N系数是整数线性组合的1/n²，n≤N；d_N=lcm(1,…,N)统一清整个prefix。因此四函数在q上的safe multiplier为d_N²（给有理关系另乘一个固定常数清a,b,c,d分母）。CDT x₆(q)=q+Z[[q]]及q(x₆)=x₆+Z[[x₆]]保证同一个safe multiplier仍清旧x₆ Taylor prefix。这个全N结论来自级数与整数formal反演，不是有限头样本。

**算术prefix和局部M13不自动支付完整curve推前费用。** 本稿没有断言共同background P¹、没有删去χ₋₃与χ₋₄/χ12的character、没有计算实际全family rank或holonomy array，也没有任何解析图导数/能量和strict余量。H₄的weight0 forcing带χ12，完整背景可能需要显式character carrier/cover；其它子任务须从实际完整field证明其rank及整模型，不能从“四个period”取rank4。

同轮field稿另给出并已交叉独核的更小实际入口：完整odd germ使forcing的character变为ψ(γ)=χ12(d)(−1)^(c/12)，其kernel是旧kerχ12⊂Γ0(12)的半平移共轭。s=−u_old(−q)具有全阶整数inverse；令v=s(1−s)，则x₆=v(1−2v)/[(1+2v)(1−v)]，h=(δ²B₄)/A₃³=v(1−2s)³/(1+2v)³，且Q(x₆,h)=Q(s)degree4。因此表面的genus1/degree8共同模场不能强制充作本forcing的最低费用。该field稿F2–F9的完整数学链已经独核；其单一假设关系H的bare rank3、全prefix入口另有具体证明，不能仅从降场推断，也不表示九条原函数都独立。**最低场的改进仍未支付全部合法解析图、返回支路或严格holonomy能量**，本轮不启动实现窗口。

结算：这一唯一固定候选通过**覆盖曲面上的完整关系提升第一证书**，不能获得实现准入。若完整背景和同对象strict预算没有新的证据，则不得以此局部成功延长优化窗口；第260轮正式全局复盘继续按既定clock执行。来源、本人实际读域和执行次数见同轮mixed_reading_scope.md。
