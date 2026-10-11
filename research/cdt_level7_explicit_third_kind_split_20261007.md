# Level 7 的显式第三类分解：完整主部、代数留数与相对 cusp 常数

日期：2026-10-07。作者：`/root/source_pencil_finalize`。状态：本轮唯一 NEW 纸面主稿，已收 root 正式独立全文审查（纸面 PASS）。旧 `cdt_odd_level7_cm_principalparts_comparison_20261007.md` 与620冻结记录保持只读。本文不运行、导入、重跑数学 producer、guard、prime 表或 Lean，不改变原 ξ 或其完整费用。

## 1. 固定对象与这次实际补上的缺口

沿用 authority `cdt_odd_delivery_real_gates_kummer_cauchy_extensions_20261007.json`，SHA256 `7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a`。实际模型来自冻结 `cdt_odd_level7_polynomial_extension_classes_20261007.md`，最终 SHA256 `fc585a055e3b577a862f58202e24eda099394ae1b62e5f33393fb2b868690e7c`；本轮重新全文读入该稿和暂停前草稿，不把旧轮读页继承为本轮阅读。

记

\[
\theta=t\partial_t,  D=q\partial_q=(2\pi i)^{-1}\partial_\tau, 
q=e^{2\pi i\tau}, \chi=\chi_{-7},
\]
\[
\begin{split}
L&=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),\\
r_B&=t(1-t),\\
r&=(\eta(\tau)/\eta(7\tau))^4,  t=r/(r+7)^2,\\
A&=1+2\sum_{n\ge1}\chi(n)q^n/(1-q^n), 
f=\eta(\tau)^3\eta(7\tau)^3,\\
LA&=0,  LB=r_B,  LB_3=t^3,  B(0)=B_3(0)=0,\\
h&=f\,t^2/(1-t),  E_3=B_3/A,  D^2E_3=h.
\end{split}\tag{T1}
\]

所有 analytic 起点均是原坐标的实际 \(\mathbb Q[[t]]\) germ。固定真实 axis continuation 的周期为

\[
\mathcal I(g)=4\pi^2\int_0^\infty y g(iy)\,dy, 
\kappa=L(f,2)=\mathcal I(f),  C_3=\mathcal I(h).
\tag{T2}
\]

冻结模型已证 \(\Delta_\sigma B=\kappa\Delta_\sigma A\)、\(\Delta_\sigma B_3=C_3\Delta_\sigma A\)，\(\sigma=1/28\)，并且 \(0<C_3<\kappa/756\)。这些是完整 germ 的 jump，不只是端点数值。

本稿的显式答案是

\[
\boxed{h=\rho+h_2,  \rho=-ft,  h_2=ft/(1-t), 
h_2=-f/3+D^2G,  G=-1/(6A).}\tag{T3}
\]

旧草稿的三个尚未完成项在这里分别落实为：具有有理 Fourier 系数的真实第三类代表 \(\rho\)；第二类 absolute 类的明确系数 \([h_2]=-[f]/3\)；相对 cusp 边界 \(\mathcal I(D^2G)=1/6\)。因而

\[
\boxed{C_3=\mathcal I(\rho)+1/6-\kappa/3.}\tag{T4}
\]

剩余 \(\mathcal I(\rho)\) 是一个明确的 CM 第三类周期，尚未识别成已知的 Dirichlet、Hecke 或 Rankin L 值，也没有无理性结论。

## 2. 从真实 forcing 逐步推出显式 Bol 分解

这里不能把 \(t^2\) 误写成 \(L(t^2)\)。直接代入实际算子可得

\[
L1=-2t-4t^2, 
\boxed{t^2=-r_B/3+L(-1/6).}\tag{T5}
\]

设 \(B_2\) 是 \(LB_2=t^2,  B_2(0)=0\) 的 normalized analytic germ。实际 recurrence 的最高项为 \(n^2[t^n]B_2\)，所以每一正阶系数唯一确定。式 T5 及 \(A(0)=1\) 给

\[
\boxed{B_2=-B/3-1/6+A/6.}\tag{T6}
\]

为核对 derivative 的 normalization，令 \(S=Dt/t\)、\(p=(1-t)^2(1-28t)\)。真实 homogeneous basis 是 \(A,\tau A\)。展开两次导数时，\(E\)、\(DE\) 项分别由 \(LA=0\)、\(L(\tau A)=0\) 消失，故

\[
L(AE)=pA S^{-2}D^2E.
\]

Yang 固定 v1 PDF5–6、15 给

\[
\frac{S^2}{A}=f\frac{(1-t)(1-28t)}t, 
D^2(B_R/A)=f\frac{R}{t(1-t)}
\tag{T7}
\]

对同一个 \(LB_R=R\) 成立。第二式也可由第一式与 \(p\) 直接代数核验。[Yang 原件](https://arxiv.org/pdf/0709.1968v1)

以 \(R=t^2\) 代入 T7，再对 T6/A 二次微分，即得

\[
\frac{B_2}{A}=-\frac13\frac BA-\frac1{6A}+\frac16, 
\boxed{h_2=-f/3+D^2(-1/(6A)).}\tag{T8}
\]

这是一条完整 meromorphic identity，最初在 cusp germ 验证后沿上半平面解析延拓。它不依赖某个 numerical relation，也没有把一个未知复数写进 forcing。

T3 的第一等式是字面代数式 \(t^2/(1-t)=-t+t/(1-t)\)。还可明确得到第三类的 actual relative carrier

\[
\boxed{B_\rho=B_3-B_2=B_3+B/3+1/6-A/6, 
LB_\rho=t^3-t^2=-tr_B,  B_\rho(0)=0.}\tag{T9}
\]

这里 \(D^2(B_\rho/A)=\rho\)。冻结 all-prime argument 对 integer polynomial forcing 原封不动适用，故

\[
D_n^2[t^n]B_\rho\in\mathbb Z,  D_n=\operatorname{lcm}(1,\ldots,n).
\tag{T10}
\]

这是原 Taylor 整模型，不是把 \(A(w)\) 等 period 当有理系数。\([t^3-t^2]=[t^3]+[r_B]/3\) 在实际 forcing 商空间中仍有非零第二条分量；因此显式分解没有把新 extension 拆成 rational solution。

## 3. 全部 pole divisors、cusp 零阶和完整 Laurent 主部

\(f\) 在上半平面无零无极点，\(r\) 是粗曲线 \(X_0(7)\) 的 degree-one 坐标，在两个 cusp 只有一阶 pole、zero。令

\[
P(r)=r^2+13r+49, 
1-t=P(r)/(r+7)^2.
\]

三条 form 有完全显式的有理表达

\[
\rho=-f\frac r{(r+7)^2}, 
h_2=f\frac r{P(r)}, 
h=f\frac{r^2}{(r+7)^2P(r)}.
\tag{T11}
\]

由 Yang PDF15 的 elliptic values：

\[
w=(7+i\sqrt7)/14,  r(w)=-7,  t(w)=\infty;
\]
\[
u=(5+i\sqrt3)/14,  t(u)=1, 
W_7u=(-5+i\sqrt3)/14; 
\tau_c=i/\sqrt7,  t(\tau_c)=1/28.
\tag{T12}
\]

\(w\) 满足 \(7w^2-7w+2=0\)，是判别式 −7 的 \(\Gamma_0(7)\) 非椭圆点，而在 Fricke 扩群中为 order 2。\(r+7\) 在 \(\tau-w\) 中一阶，所以 \(t\) pole 阶2。\(\rho,h\) 在这个轨道有二阶 poles，\(h_2\) 在此 analytic，其值为 \(-f(w)\)。

\(u\) 满足 \(7u^2-5u+1=0\)，两个 \(P(r)=0\) 的轨道为判别式 −3 的 \(\Gamma_0(7)\) order-3 点。\(1-t\) 在 \(\tau-u\) 中零阶3；\(h,h_2\) 在两轨道有三阶 poles，\(\rho\) 在此 analytic。\(\tau_c\) 以及其他上半平面点无这三条 form 的 poles。

两个 native cusp 坐标中 \(f,t\) 的零阶均为1，故 \(\rho,h_2\) 的零阶为2，\(h\) 的零阶为3。在 \(q=0\) 处更精确为

\[
\rho=-q^2+O(q^3),  h_2=q^2+O(q^3),  h=q^3+O(q^4).
\tag{T13}
\]

### 3.1 CM−3：second-kind 的全部低阶项确为零

由 T7 的 \(A=S^2t/[f(1-t)(1-28t)]\)，在 \(u\) 处 \(S\) 零阶2，故 \(A\) 零阶1；在 \(w\) 处 \(A\) 非零。完整 degree-two map 与 \(r\) 的 quotient ramification 也排除 \(A\) 的其他上半平面零点。

在任意 −3 lift 写 \(\delta=\tau-u\)、\(a_1=A'_\tau(u)\ne0\)。于是 \(G\) 的完整 principal part 为 \(-1/(6a_1\delta)\)；T8 直接给

\[
\boxed{h_2(\tau)=h(\tau)=\frac1{12\pi^2a_1}\delta^{-3}+O(1).}
\tag{T14}
\]

等式意指二者具有所写相同 principal part，其 regular parts 不要求相同。没有 \(\delta^{-2}\) 或 \(\delta^{-1}\) 项。weight3 的 second-kind 定义正是这两项消失，加上每个 cusp 的 constant term 为零；见 GZ PDF9–10。这说明 \(h_2\) 为真正的第二类 form，而不是仅仅“向量留数恰零”的宽泛说法。

### 3.2 CM−7：第三类完整 affine-log 留数

此处为把 algebraic residue 的比例完全付清，重写实际 local calculation。令 \(d=w-\bar w\)、\(A_w=A(w)\)。以 \(z=1/t\) 计，真实算子为

\[
z^3L=(z-1)^2((z-28)(z\partial_z)^2+14z\partial_z)-4z-2z^2.
\]

\(z^3LB_3=1\)，indicial roots 为0、1/2。若 \(v_0=1+O(z)\) 是齐次 analytic solution，则 \(L\) 的 normalized action 对 \(v_0\log z\) 的 constant 为14，故

\[
B_3=(1/14)v_0\log z+\text{analytic}+b v_{1/2}.
\tag{T15}
\]

\(B_2\) 的右端 \(z^3t^2=z\) 没有 resonant constant，所以在 \(\tau\) 坐标无 logarithm。齐次解空间为 \(A\cdot\operatorname{span}\{1,\tau\}\)。固定 \(w\) 的矩阵

\[
\gamma=7^{-1/2}\begin{pmatrix}7&-4\\14&-7\end{pmatrix}
\]

满足 \(\gamma'(w)=-1\)，实际 multiplier \(A(\gamma\tau)=-i(14\tau-7)A(\tau)/\sqrt7\)。由 \(A_w\ne0\) 在 fixed point 也唯一确定这个乘子。微分给 \(A'_\tau(w)/A_w=-1/d\)。因为 \(z\) 在 \(\delta=\tau-w\) 中零阶2，\(v_0/A\) 的 affine 函数由其 value、derivative 唯一确定为 \((\tau-\bar w)/(A_wd)\)。T9、T15 因而给

\[
\frac{B_\rho}{A}=\frac{\tau-\bar w}{7A_wd}\log(\tau-w)
+\text{holomorphic in }\tau.
\tag{T16}
\]

二次微分并用 \(D^2=-\partial_\tau^2/(4\pi^2)\)，得

\[
\boxed{\rho(\tau)=h(\tau)=\frac1{28\pi^2A_w}
\left(\delta^{-2}-d^{-1}\delta^{-1}\right)+O(1).}
\tag{T17}
\]

同样，T17 是 principal-part 相同，不是 regular parts 相同。尤其 \(\delta^{-1}\) 的 affine correction 不能略掉。所有 \(\Gamma_0(7)\) images 按自己的 \(A_w,d\) 给相同公式。

## 4. Γ₀(7),χ 的明确数域定义和代数留数

\(f\) 为 weight3、character \(\chi\)，\(t\) 为 invariant；因此 \(\rho,h_2\) 均具有同一 character。这些 Fourier series 都在 \(\mathbb Z[[q]]\)。\(G\) 为 meromorphic weight−1、character \(\chi^{-1}=\chi\)，且 \(6G\in\mathbb Z[[q]]\)。Bol identity 给 \(D^2G\) weight3、同 character。这里的“有理定义”是实际 modular/de Rham 意义，而不是把 complex period 宣称为有理。

为使用无 \(-I\) 的普遍椭圆曲线，取 \(\Gamma=\Gamma(7)\)。\(\chi\) 在它上为1；取有限数域 \(K\) 包含完整 level-7 结构、所有 marked CM lifts 及其 CM endomorphisms 的定义域。这里只需要存在这样一个有限域，不声称最小域。BF PDF37 的 q-expansion principle 使上述 Q-Fourier forms 给出 \(K\)-定义的实际 de Rham differential。

\(\Gamma_0(7)/\Gamma(7)\) 有42个元素，effective 粗覆盖 degree21。−7 轨道有21个 lifts；两个 −3 轨道各7个 lifts。两个 cusp 的 lifts 数分别3、21，ramification7、1，所以 \(\rho,h_2\) 在这些 cusp 的零阶分别14、2，\(h\) 分别21、3。odd weight 的 \(-I\) sign 已由 character 配合，不作错误的 invariant 平均。

采用 BF 的实际 Betti normalization

\[
\omega_\rho=(2\pi i)^2\rho(\tau)(X-\tau Y)d\tau.
\]

由 T17 的两个系数逐项计算

\[
\boxed{\operatorname{Res}_w\omega_\rho
=\frac{X-\bar wY}{7A_w(w-\bar w)}.}\tag{T18}
\]

乘 \((2\pi i)^2\) 之前的 residue 是
\(-[28\pi^2A_wd]^{-1}(X-\bar wY)\)，因此 T18 符号为正。在 −3 点，T14 乘 affine \(X-\tau Y\) 没有 residue；\(h_2\) 在每个 finite point 的向量留数均为零。

\(\omega_q=2\pi i(X-\tau Y)\) 是 Tate differential，\(\omega_A=A\omega_q\) 是本模型的代数 Hodge differential。固定 −7 fiber，以 \([\omega]=[\omega_A]\) 为 first CM eigenvector，first period \(\omega_1=2\pi iA_w\)。取 symplectic opposite CM eigenvector \([\eta']\)，\(\langle\omega,\eta'\rangle=1\)。BF Lemma6.3、Remark6.6 的完整 comparison 为

\[
\operatorname{comp}^{-1}(X-\bar wY)
=\frac{\omega_1}{2\pi i}(\bar w-w)[\eta'].
\]

本轮实际渲染图像重新核对了 \(\bar w-w\) 的负号。代入 T18 得

\[
\boxed{\operatorname{Res}^{\rm dR}_w[\omega_\rho]=-[\eta']/7.}
\tag{T19}
\]

这在全部21个 lifts 成立；没有剩余 \(A_w\)、\(\pi\) 或未知 period 倍数。[BF 固定 v2](https://arxiv.org/pdf/2508.04844v2)

任意 meromorphic weight−1 form 的 Bol 二阶导在 ordinary flat frame 中都是局部二次导数，其 weight3 Laurent \(\delta^{-2},\delta^{-1}\) 项为零。因此其向量 residue 也为零。T19 严格推出：不存在 \(a\in\mathbb C\)、全球 meromorphic weight−1 form \(H\)，使

\[
\rho=a f+D^2H.
\tag{T20}
\]

同样，finite cover 不会消去这个非零 residue。这个障碍明确把剩余类与 second-kind/quasiperiod 部分区分开来。

### 4.1 消除旧 kernel 分解的 cusp 自由度

\(S_3(\Gamma_0(7),\chi)=\mathbb C f\)：因为 \(f\) 无上半平面零点，且在两个 cusp 的零阶均1，任意 holomorphic cusp form \(g\) 的 \(g/f\) 是 compact \(X_0(7)\) 的无极点函数。

所以若两条 weight3、χ forms 都 cusp-vanishing、只有 −7 poles 且具有 T17 的相同完整主部，其差必为 \(a f\)。加上规范 \([q]\rho=0\) 后，因为 \([q]f=1\)，该 \(a\) 必为0。因此 **\(\rho=-ft\) 是具有这些主部、character、cusp 条件且一次 Fourier 系数为零的唯一第三类代表**。这给旧稿只存在的 K-Fourier 分解一个显式且规范的实际答案，无须另算 Poincaré kernel 的 transcendental cusp correction。

## 5. 第二类 absolute 类与真实 cusp 边界全部付清

T8 在真实 meromorphic Bol quotient 中给

\[
\boxed{[h_2]=-[f]/3.}\tag{T21}
\]

因此旧二维 second-kind space 中无需新增未知 quasiperiod 分量。GZ PDF9–10 的 quotient 定理可解释 T21，但实际系数 \(-1/3\) 是由原算子 T5–T8 明算出来的。

absolute exactness 不能免费变成 relative integral 为零。沿 \(\tau=iy\)，令 \(g(y)=G(iy)\)。因为 \(D=-\partial_y/(2\pi)\)，

\[
4\pi^2\int_\epsilon^R yD^2G(iy)dy
=[y g'(y)-g(y)]_\epsilon^R.
\tag{T22}
\]

完整 Fricke identity 是

\[
t(W_7\tau)=t(\tau), 
f(W_7\tau)=i7^{3/2}\tau^3f(\tau), 
A(W_7\tau)=-i\sqrt7\tau A(\tau).
\tag{T23}
\]

这些固定 germ 公式分别由 eta inversion 和 T7 求导得来，不以 midpoint 的一个数值代替。

当 \(y\to\infty\)，\(A(iy)=1+O(e^{-2\pi y})\)，其 derivatives 同样指数小，故
\(g(y)=-1/6+O(e^{-2\pi y})\)、\(yg'(y)\to0\)。当 \(y\to0\)，置 \(v=1/(7y)\)。T23 给

\[
A(iy)=\frac{A(iv)}{\sqrt7 y}, 
g(y)=-\frac{\sqrt7 y}{6A(iv)}
=-\frac{\sqrt7 y}{6}+O(y e^{-2\pi/(7y)}).
\tag{T24}
\]

微分后的 error 仍为指数小乘固定 power。于是 \(yg'(y)-g(y)\to0\) 于0，而在∞趋 \(1/6\)。T8、T23 也直接证明 \(D^2G=h_2+f/3\) 在两 cusp 指数衰减乘固定 power，所以 T22 的 improper integral 普通收敛，完全不需要 regularization。最终

\[
\boxed{\mathcal I(D^2G)=1/6, 
\mathcal I(h_2)=1/6-\kappa/3, 
C_3=\mathcal I(\rho)+1/6-\kappa/3.}\tag{T25}
\]

特别注意 \(\mathcal I(\rho)=-\mathcal I(ft)<0\)。若记 \(M_1=\mathcal I(ft)>0\)，正确的式子是
\(M_1=1/6-\kappa/3-C_3\)，不能把右边符号颠倒。

两个 integrand 均沿 imaginary axis 无 pole：r 为正实数，故 \(0<t(iy)\le1/28\)、\(f(iy)>0\)。并且这个轴上的区间严格不是恒等 maximum，所有这里使用的 inequality 皆可取 strict。

## 6. 完整连接常数、实际整模型与可用的数值等价

由 T6、T9 的完整 jump 立即得到

\[
\Delta_\sigma B_2=(1/6-\kappa/3)\Delta_\sigma A, 
\Delta_\sigma B_\rho=\mathcal I(\rho)\Delta_\sigma A.
\tag{T26}
\]

这是保留 \(\mathbb Q[[t]]\) 起点和原 \(D_n^2\) 整模型的真正 CM 第三类 carrier。它没有新增 ordinary forcing pole，也没有把所有其他 monodromy 填掉。若某个 relation 假设使它的数值连接系数为有理数，还须重新证明真正 CDT leaf、rank 和 strict margin；T26 本身不产生无理性。

数值线性组合的 exact rational shear 为

\[
\mathbb Q\text{-span}\{1,\kappa,C_3\}
=\mathbb Q\text{-span}\{1,\kappa,\mathcal I(\rho)\}.
\]

具体地，\(a+b\kappa+cC_3=0\) 等价于
\((a+c/6)+(b-c/3)\kappa+c\mathcal I(\rho)=0\)。这个接口付清全部常数；不宣称两边的三个数已经线性无关。

还有严格的有理范围，证明不需数值代码。因为 \(0<t/(1-t)\le1/27\)，在积分意义下

\[
0<\mathcal I(h_2)<\kappa/27.
\]

以 T25 代入，逐步得到
\(0<1/6-\kappa/3<\kappa/27\)，所以

\[
\boxed{9/20<\kappa<1/2, 
0<C_3<\min(\kappa/756,\,1/6-\kappa/3), 
-\kappa/28<\mathcal I(\rho)<0.}\tag{T27}
\]

最后一个 inequality 来自 \(0<t\le1/28\)。这些范围不排除 rational values，也不把 CM 名称当作 arithmetic independence。

## 7. 剩余周期的确切身份与不能套用的 L 值公式

T19 与实际 normalized cusp-to-cusp path 共同给 \(\mathcal I(\rho)\) 一个确切的定义：它是 Γ₀(7),χ 的、以 CM−7 opposite Hodge eigenvector residue \(-\eta'/7\) 为 puncture 数据、以 \([q]\rho=0\) 固定 cusp ambiguity 的第三类 modular extension period。这个描述是已证 comparison，不是某种 conjectural Rankin 公式。

还可严格检查为何通常的 holomorphic-cusp L-series 不能直接给它名字。\(\rho\) 是1-periodic 的 meromorphic function，故在 punctured q disk 上单值；CM−7 点给

\[
q_w=e^{2\pi iw}=-e^{-\pi/\sqrt7},  |q_w|<1.
\]

T17 的 leading coefficient 非零，q 是 w 处的 local unit coordinate，因此 \(\rho\) 在 \(q_w\) 有真正的二阶 pole。若 \(\rho(q)=\sum c_nq^n\) 的 Taylor radius 为 R，则

\[
0<R\le e^{-\pi/\sqrt7}<1, 
\limsup_{n\to\infty}|c_n|^{1/n}=R^{-1}\ge e^{\pi/\sqrt7}>1.
\tag{T28}
\]

于是对任意固定 complex s，\(c_n/n^s\) 在某个无限 subsequence 上指数增长，甚至不趋0。**普通 Dirichlet series \(\sum c_n/n^s\) 没有任何右收敛半平面。** 所以不能凭 Mellin notation 把 \(\mathcal I(\rho)\) 定义成通常的 \(L(\rho,2)\)，也不能在 q=1 免费求和其 cusp Taylor primitive。真实 integral T2、T25 仍沿没有 pole 的轴普通收敛，这两件事并不冲突。

T28 仅排除这个直接 L-series identification；不排除日后以独立 arithmetic comparison 证明它恰等于某个其他 holomorphic eigenform、Hecke character或 regulator 的特殊值。要做到后者，必须给出保持 T17/T19、q normalization 和 T25 全部端点常数的完整 comparison。

所核 primary 没有给该具体 \(-ft\) 的这种公式。BF PDF42 Remark8.2 的 reciprocity 提供 period 互换框架，但没有计算本例的 cusp/parabolic correction；其 Theorem8.4 假设 cusp cohomology vanishing，本例已有非零 f，不满足。CM Tate/Kummer projection 的 Theorem8.6 是 even k=2m，而 weight3 对应 k=1。PDF49 的 k=1 elliptic Rankin–Selberg comparison 明确是 expected/conjectural，不能填进 T4 充当已证值。[BF primary](https://arxiv.org/pdf/2508.04844v2)

因此本轮实际解决的是三个旧缺口，不是数值无理性：第三类代表从存在性变成 \(-ft\)；第二类 unknown coefficients 从二维接口变成准确 \(-[f]/3\)；相对 cusp boundary 从未支付变成 \(1/6\)。剩下的唯一数值新周期是 \(\mathcal I(\rho)\)，其 global non-Bol 性已由 T19/T20 明确证明。当前不声称全部奇 ζ、未证偶 L 值或任何这个新周期已无理。

## 8. 个人 fresh 阅读、文献来源和审查接口

本轮实际全文读入冻结 fc585 模型 E1–E29/all8sections及暂停前4a1d草稿 P1–P27/all8sections；不修改两文件。所用 primary 本轮重新读取：

- Yang fixed v1，`literature/yang2007_apery_limits_v1_20261006.pdf`，SHA256 `691258e04fb3f9f9fa6a4cc144c8be99d587d0af47f96cbf138ac797a1025109`：PDF **5–6、15–16**，4 distinct pages。[官方版本](https://arxiv.org/pdf/0709.1968v1)
- Brown–Fonseca fixed v2，`literature/cdt_gamma_level7_punctured_sources_20261007/brown_fonseca2025_single_valued_meromorphic_arxiv2508_04844v2.pdf`，SHA256 `17f8556f14261236af621695799387065cd70dae4295b52f3ee6e82d28593a66`：PDF **34、36–37、41–43、49–50**，8 distinct pages；34、36 的既有 render 也本轮重新目读，共轭和 sign 均核对。[官方版本](https://arxiv.org/pdf/2508.04844v2)
- Golyshev–Zagier 现有 author preprint，`literature/cdt_gamma_relative_chain_sources_20261007/golyshev_zagier_interpolated_apery_motivic_gamma_author.pdf`，SHA256 `529a92d1ba0744e00c3d26ea97400ae3da25b0615dea5dacbaa0b3f25697d669`：PDF **9–10**，2 distinct pages；使用 Bol 与 second-kind 定义范围，不借其别的模型的数值值公式。

个人本轮 **14 distinct primary PDF pages**；不包含同行读域，也不复用旧轮页数。另通过官方 arXiv 页面核对 Yang/BF 固定版本，并对 exact meromorphic weight3 L-value 方向搜索 primary；没有发现可合法调用的本例数值公式，也没有由搜索阴性推断“文献中绝无这样的恒等式”。本轮新 PDF 下载0；只复用既有 normal-TLS 档案，不重复存档。

独立审查重点为 T5/T6 的 forcing sign；T14/T17 的完整低阶项；T18/T19 的 conjugation 与 Tate factors；T24 的两端导数边界；T25/T27 的积分符号；T28 的 direct L-series 排除范围。正式 incoming review、作者最后全文回读前不生成 FINAL receipt；最终单向 receipt 不 pin mutable main、peer receipt 或 future audit。
