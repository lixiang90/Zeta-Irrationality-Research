# D12 的零真实周期 Eisenstein 校正：完整整数反射族与合法解析叶

日期：2026-10-06。本文构造对每个整数 n 都成立的实际 source 与真实反射族；不执行/import任何冻结 producer，不作短 word、素数或研究参数扫描。它保留纯 \(L(3,\chi_{12})\) 周期，尚不是新的无理性定理，也不声称新增反射自动改善解析容量。

## 1. 零 Apéry 周期的实际 source

使用冻结的真实源
\[
\begin{aligned}
F_L={}&1217E_4-14082E_4(2\tau)+6255E_4(3\tau)-11120E_4(4\tau)\\
&+126738E_4(6\tau)-175248E_4(12\tau)
+2880E_\chi-69120\sqrt3F_\chi .
\end{aligned}
\]
\(E_\chi=E_4(1,\chi_{12})\) 的常数为23，\(F_\chi=E_4(\chi_{12},1)\) 的常数为0，均取原稿规范。令
\[
\Theta=34560\sqrt3L(3,\chi_{12}),\quad
f_L=\theta_q^{-3}F_L,\quad
h_-=f_L-\Theta,\quad h_+=\sigma f_L+\Theta .
\tag{1}
\]
primitive 的 q 常数均为0；\(\sigma\) 仅作用于源系数，暂不作用于未知 L 数值。原稿证明 \(h_-|_{-2}W=-h_-\)、\(h_+|_{-2}M=-h_+\)。

定义非零 rational source
\[
\boxed{R=E_4-66E_4(2\tau)+495E_4(3\tau)-880E_4(4\tau)
+594E_4(6\tau)-144E_4(12\tau).}
\tag{2}
\]
它是 \(G_1-66G_2+495G_3\)，\(G_3=E_4(3\tau)-(16/9)E_4(4\tau)\)，首个 q 系数为240。令 \(P_R(s)=\sum_{j\mid12}r_jj^{-s}\)，则
\[
P_R(0)=P_R(1)=P_R(2)=P_R(3)=0,\quad
L(R,s)=240P_R(s)\zeta(s)\zeta(s-3).
\tag{3}
\]
\(s=1\) 处两 ζ 因子的 pole/zero 相消后有限，故 \(P_R(1)=0\) 确保 \(L(R,1)=0\)；其余两点给 \(L(R,2)=L(R,3)=0\)。oldform 公式
\(E_4(j\tau)|_4W=(144/j^4)E_4(12\tau/j)\) 给 \(R|_4W=-R\)。
若 \(f_R=\theta_q^{-3}R\) 且 q 常数为0，真实 Mellin/Eichler 公式给
\[
f_R|_{-2}W=-f_R,\qquad f_R|_{-2}T=f_R.
\tag{4}
\]
所以加任意 rational \(sR\) 保留真实 Θ、q 正则性和第一支 W identity，改变的是实际 Tate cocycle。

## 2. 完整 cocycle 规范与反射 eigline

取
\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\
W=\begin{pmatrix}0&-1\\12&0\end{pmatrix},\
M=\begin{pmatrix}24&-7\\84&-24\end{pmatrix},\
\eta=WT^{-1}W^{-1}=\begin{pmatrix}1&0\\12&1\end{pmatrix}.
\tag{5}
\]
在 \(\Gamma=\ker\chi_{12}\) 上 \(\varepsilon=+1\)，在 \(M\Gamma\) 上 \(\varepsilon=-1\)。对 h 为 \(h_+\) 或 \(f_R\)，
\[
c_h(g)=h|_{-2}g-\varepsilon_g h,\qquad
c_h(g_1g_2)=c_h(g_1)|_{-2}g_2+\varepsilon_{g_1}c_h(g_2).
\tag{6}
\]
冻结的完整 generator-period表给
\[
c_L(M)=0,\qquad
c_L(\eta)/(i\pi^3)=(44160,529920,2073600).
\tag{7}
\]
vector使用 ordinary basis \((1,\tau,\tau^2)\)。由(4)和群 identity，\(c_R(\eta)=0\)。

令 \(Q_M=1+12(7\tau-2)^2=49-336\tau+588\tau^2\)。新独立有限 Bernoulli 计算给
\[
f_R(\tau=2/7+i0)=-1920i\pi^3/7.
\tag{8}
\]
此 cusp 的 source 常数 \(\sum r_j/j^4=0\)，故这是实际 radial primitive值，无未删 pole。准确计算用
\[
K_7(x)=-\frac12+\sum_{k=1}^6(\tfrac12-\tfrac k7)x^k,
\]
它在非平凡 seventh roots等于 \(x/(1-x)\)，在1取 finite part \(-1/2\)。故(8)的系数为
\[
\sum_{j\mid12}\frac{160r_j}{j^3}
\sum_{k=1}^6(\tfrac12-\tfrac k7)
B_3(\{2jk/7\})=-1920/7.
\]

单一 endpoint不足以确定完整 polynomial。这里 \(M^2\) central且 \(\varepsilon_M=-1\)，(6)强制
\(c_R(M)|_{-2}M=c_R(M)\)。unsigned \(R_M\) 的 +1 eigenspace准确一维，由 \(Q_M\) 生成。比较 \(\tau\to i\infty\) 的最高项与(8)，完整得到
\[
\boxed{c_R(M)=-\frac{1920}{7}i\pi^3 Q_M.}
\tag{9}
\]
这保留 signed order-two eigline，未从 endpoint任意猜一次项。

## 3. 全整数唯一校正与真实 polynomial identity

定义
\[
J_n=\eta^nM\eta^{-n}
=\begin{pmatrix}24+84n&-7\\12p_n&-24-84n\end{pmatrix},
\qquad p_n=84n^2+48n+7>0 .
\tag{10}
\]
它有 determinant12、trace0，\(J_n^2=-12I\)。令 \(Q_n=Q_M|_{-2}\eta^{-n}\)，其常数项恒49，生成 unsigned \(R_{J_n}\) 的一维 +1 eigline。

实际 cocycle recurrence给所有正、负、零整数
\[
P_n:=c_L(\eta^n)/(i\pi^3)
=(44160n,\ 529920n^2,\ 2119680n^3-46080n).
\tag{11}
\]
由 \(P_0=0\)、\(P_{n+1}=P_n|_{-2}\eta+P_1\) 和逆矩阵证明负整数情形，未将有限样本外推。又
\[
\begin{aligned}
c_L(J_n)/(i\pi^3)
&=(P_n|_{-2}M+P_n)|_{-2}\eta^{-n}=\mu_nQ_n,\\
c_R(J_n)/(i\pi^3)&=-\frac{1920}{7}Q_n,\\
\mu_n&=\frac{1920}{7}(644n^3+552n^2+147n).
\end{aligned}
\tag{12}
\]
两者成比例来自 actual signed reflection的 eigline；展开(11)才计算比例。因此唯一 scalar解为
\[
\boxed{s_n=644n^3+552n^2+147n\in\mathbf Z,\quad
(h_++s_nf_R)|_{-2}J_n=-(h_++s_nf_R).}
\tag{13}
\]
\(s_0=0,s_1=1343,s_{-1}=-239\)；二次因子判别式 \(-73968<0\)，所以 \(n\ne0\) 时 \(s_n\ne0\)。

若用 endpoint规范核对，令
\(Q_{J_n}=1+(12p_n\tau-24-84n)^2/12\)，则 \(Q_n=(7/p_n)Q_{J_n}\)，实际 Tate系数为
\[
\lambda^{\rm Tate}_{L,n}=1920s_n/p_n,\qquad
\lambda^{\rm Tate}_{R,n}=-1920/p_n.
\tag{14}
\]
n=1给此前已独立核过的 \(2578560/139\)，被1343倍 \(-1920/139\) 消去；这仅是 normalization一致性，(11)–(13)已证明全尺度。

## 4. 两 embedding 的算术 primitive

对每个固定整数n，
\[
\begin{aligned}
F_n^-&=F_L+s_nR,&F_n^+&=\sigma F_L+s_nR,\\
h_n^-&=f_L+s_nf_R-\Theta,&
h_n^+&=\sigma f_L+s_nf_R+\Theta.
\end{aligned}
\tag{15}
\]
准确 identities是
\[
h_n^-|_{-2}W=-h_n^-,\quad
h_n^+|_{-2}J_n=-h_n^+,\quad
h_n^\pm|_{-2}T=h_n^\pm.
\tag{16}
\]
若反证假设 \(L(3,\chi_{12})\in\mathbf Q\)，则 \(\Theta\in K=\mathbf Q(\sqrt3)\)且 \(\sigma\Theta=-\Theta\)，所以 coefficientwise
\(\sigma h_n^-=h_n^+\)。未对未知L值使用未经授权的 Galois操作，未丢 primitive常数。

源q系数在 \(\mathcal O_K\)；整数 \(s_nR\) 不增新的固定 denominator。第k个 primitive系数仍仅新增k³分母，整数q↔t反演仍保持原 \(L_D^3\) 型整性上界。这里先固定n，再令CDT degree D增长；若n随D增长，\(\log|s_n|\) 的source height成本须另计。

## 5. 合法 full leaves 与 pole clearing

沿用
\[
t_\delta=\frac{v+\delta\sqrt3/v-1-\delta\sqrt3}{2(1-\delta\sqrt3)},
\quad \delta=\pm1,\quad t_\delta(q)=q+O(q^2).
\tag{17}
\]
\(\eta\in\Gamma\)保持v，\(Wv=\sqrt3/v\)、\(Mv=-\sqrt3/v\)，故每个 \(J_nv=-\sqrt3/v\)。令 \(A_2=E_2-12E_2(12\tau)\)，它在Γ上modular，在W、M及每个 \(J_n\) 下weight2 anti。因此
\(H_n^-=A_2h_n^-\)、\(H_n^+=A_2h_n^+\)
分别在 \(G_+=\langle T,W\rangle\)、\(G_n=\langle T,J_n\rangle\) 上真实不变。

\(J_n\) 的上半平面fixed point为
\[
\tau_n=(24+84n+i\sqrt{12})/(12p_n).
\]
令 \(\zeta=(12p_n/\sqrt{12})(\tau-\operatorname{Re}\tau_n)\)，Jn为 \(\zeta\mapsto-1/\zeta\)，T为 \(\zeta\mapsto\zeta+w_n\)，
\[
\boxed{w_n=\sqrt{12}p_n>2.}
\tag{18}
\]
沿用已证明的Hecke full-leaf拓扑，每个coarse quotient有一个cusp、一个funnel、一个order2 elliptic；填唯一cusp、使用elliptic coarse coordinate后为Riemann disk \(X_n\)。新cusp q与原q仅相差模长1的phase，不改变 conformal derivative绝对值。

H和t在upper half-plane全纯；(16)使canonical elliptic orbit真正下降，q Taylor使唯一cusp可填。t在interior不取完整cusp values，唯一filled zero简单。其它未在G_n稳定子中的involution fibers保留ordinary source的degree2 ramification，未假定其周期消失。因此 Riemann maps确实给合法 \(\phi_{-,n}\) 与固定第一支 \(\phi_+\)。

native t导数仍须清pole。沿用
\[
D_\delta=1-4(2+\delta\sqrt3)t+4t^2,\qquad g_\delta=D_\delta^2.
\]
在t critical coordinate \(t-t_0\sim z^2\)，g有order4，清二阶导数order3 pole；故
\((1,g_\delta H,g_\delta\theta_tH,g_\delta\theta_t^2H)\)
在各filled disk全纯，未声称裸Euler rows自动全纯。

每个固定n的实际rank仍为4：原 rational inhomogeneous order3 model在 \(\mathbf C(v)\) 上仅改变forcing，给order≤4；共轭源在cusp0的常数920不变，因为R在此常数0；第一支另一个∞ cusp常数 \(-132480\)也不变。非零A2 cusp常数相乘后log³延拓给四个独立monodromy translates，故order≥4。两embedding的rank不相加。

## 6. 新正接口的边界

本族保留真实纯L周期、两embedding算术germ与同一整性指数，每个n给完整校正过的reflection。n=0模型包含在内。

它不自动扩大同一个source的旧leaf：n非零时新共轭primitive在M的correction为 \(s_nc_R(M)\ne0\)，不能同时沿用旧M/旧augmented leaf。因 \(c_R(\eta)=0\)，新target的 \(c_L(\eta)\)原样保留，不能下降整个Γ。

对整数n，\(p_n-p_0=12n(7n+4)\ge0\)，仅n=0等号，所以本principal Hecke参数由n=0最小。这未分类新source的全部稳定子，未证明其它合法leaf不可能更大。

旧finite-height估计不能直接标为新的精确预算：整数校正保留 denominator profile，但新full stabilizer、背景共同延拓、actual radius/Jensen成本及任何Smith收益须对实际新source核对。本文不由合法叶存在宣布数值矛盾。

## 7. 新证书与审阅状态

同名NEW verify.py不import/执行旧文件。第一次执行保存39项fixed symbolic checks；第二次新增 independent Bernoulli normalization，保存40项全部通过。输入(7)来自实际独审冻结的完整generator-cocycle表。新证书核全n recurrence、negative inverse、signed eigline、matrix/order、完整polynomial cancellation、整数s、zero-period oldforms及(8)独立有限和。

任意n的解析叶使用既有Hecke拓扑和本文真实identities；有限checks不替代证明。

Root实际完整只读本MD与同名NEW verify.py，未执行脚本；限定独核all-n signed eigline、完整integer \(s_n\)、真实R的W周期、两embedding反证germ、T/Jn合法filled leaves及pole clearing通过。各固定n的实际rank4由unchanged nonzero cubic cusp支撑，root也实际核过。此次审阅不认证新的数值无理性、全stabilizer或改进CDT预算。本文三件据此冻结，后续实际新source/leaf或算术研究另稿。

