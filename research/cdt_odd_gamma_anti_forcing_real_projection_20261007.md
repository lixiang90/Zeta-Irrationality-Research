# 反不变强迫的真实共轭结构：有理完整 MUM 投影的分裂障碍

2026-10-07，NEW，作者 /root/scaled_root_finalize。本轮 authority 为 research/cdt_odd_delivery_paired_anti_modular_slopes_20261007.json，SHA47e298629fba798cc2d11a1e711219e61746c617f25f308919d9e1c6f6a7ecab；主报告 §§196–200。612 冻结记录（607 数学、5 guards）和所有旧/同行 producers、results、guards、prime 表均只读。本轮数学 producer 创建/执行/import/rerun、prime 扩表、Lean 和数学运行全部0。

主要结果是一个针对**真实有理强迫**的完整跳跃障碍。九维反不变商的八个 MUM 周期虽然写成复数，它们的虚部只沿同一个实方向；余下反射周期恰为这一实数的纯虚倍数。因此，对实系数尤其有理系数强迫，完整填掉指定 bridge 的第二个 MUM 点已经迫使扩张分裂。这个结论不是把八个复方程计作十六个独立实方程。它也把实际十行秩证明从旧的正强迫例子推广到全部实系数非分裂类，并证明杀掉该完整跳跃的有理线性微分投影只输出有理函数。较少周期条件是否有非零有理解，仍是明确的数值周期关系问题，本文不宣布新的无理性。

## 1. 原对象、实 Frobenius basis 与唯一 canonical bridge

**R1（真实固定对象）。** 本轮实际 FULL 重新读取冻结 Gamma G1–G19/七节，以及 quadratic anti-invariant 主稿 A1–A29/十节、公式 A1–A49；后者 sections1–6 与7–10分开完整读取。没有继承以前的原件页数或执行证据。固定
\[
 a=(\tfrac12^{\times5},\tfrac15,\tfrac25,\tfrac35,\tfrac45),\quad
 \Lambda=3200000,\quad c=\Lambda^{-1},\quad D=t\partial_t,
\]
\[
 L=D^9-\Lambda t\prod_{\ell=1}^9(D+a_\ell),\quad
 f_0(t)=\sum_{n\ge0}h_nt^n,\quad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbf Z.
 \tag{R1}
\]
完整 MUM basis 为 \(\phi_j=[s^j]\Phi(s,t)\)，
\[
 \Phi(s,t)=t^s\sum_{n\ge0}
 \Lambda^n\frac{\prod_\ell(a_\ell+s)_n}{(1+s)_n^9}t^n,
 \quad 0\le j\le8.
 \tag{R2}
\]
在正实 \(0<t<c\) 上取实 \(\log t\)。式R2使每个 \(\phi_j\) 都在此实值，leading term 是 \((\log t)^j/j!\)。这里使用完整 functions，包括全部 logarithms，并非 analytic-part package。

**R2（reflection 的实际规范）。** 正向 \(c\)-loop 为 \(T_c\)，
\[
 \psi=(T_c-I)f_0,\qquad
 (T_c-I)\phi_j=\kappa_j\psi,\qquad
 \kappa_j=[s^j]\frac{\Gamma(1+s)^{15}}
 {\Gamma(1+2s)^5\Gamma(1+5s)}.
 \tag{R3}
\]
\(\kappa_j\in\mathbf R,\ \kappa_0=1,\ \kappa_1=0\)，且 \(\psi\ne0,\ T_c^2=I\)。conifold exponents 为 \(0,\ldots,7,7/2\)。Green normalization 为
\[
 S_{ij}=(-1)^i\delta_{i+j,8},\quad
 d=\kappa^tS\kappa=\frac{16\pi^8}{5},\quad
 v=-\frac2dS\kappa,\quad
 \psi=v^t\phi,\quad \kappa^tv=-2.
 \tag{R4}
\]
对 homogeneous solution 的**系数列** \(h\)，reflection matrix 是
\[
 T=I+v\kappa^t.
 \tag{R5}
\]
对 basis column \(\phi\) 则是转置 \(I+\kappa v^t\)，两者不混用。

**R3（quadratic cover 与路径）。** 令
\[
 t=x(1-x),\quad w=1-2x,\quad b=\tfrac14,\quad
 w^2=1-4t,\quad \sigma(x)=1-x,
\]
\[
 \delta=\frac{1-x}{1-2x}D_x,\quad
 L_{\rm pb}=\delta^9-\Lambda x(1-x)\prod_\ell(\delta+a_\ell).
 \tag{R6}
\]
MUM preimages 为 \(0,1\)，conifold preimages 为
\[
 r_\pm=(1\pm\sqrt{1-4c})/2.
\]
固定 \(\gamma\)：从 \(0\) 沿正轴，在 \(c\) 上半平面作小半圆 detour，再沿 \(c<t<b\) 的 upper boundary 到 \(b\)，最后取 detour radius 趋零。\(w(0)=+1\)，在 \(c<t<b\) 上 \(w=\sqrt{1-4t}>0\)。左 inverse \(X(t)=(1-w)/2\) 提起 \(\gamma\) 到 \(x=1/2\)；穿过该实际 analytic germ 后，用 \(1-X(t)\) 和 \(\gamma^{-1}\) 到 \(x=1\)。完整 bridge 的 \(t\)-路径是 \(\gamma\gamma^{-1}\)，所以 \(f_0(t(x))\) 在这个右端回到原 analytic MUM branch。本文所有 \(x=1\) gates 均指该 bridge；不会据此宣称任意 transported branch 或任意 analytic map 必须遗漏1。

## 2. 从实反射得到全部虚部的同一个方向

**R4（upper/lower 关系及方向）。** 在 \(c<t<b\)，令 \(\phi_j^\pm\) 为由 \(0<t<c\) 分别从 upper/lower half-plane 继续的 boundary germs。实方程与实初始 germs 给
\[
 \phi_j^-=\overline{\phi_j^+}.
 \tag{R7}
\]
从 \(c\) 左侧开始，正向小 loop 的前半段在下半平面；lower path 接 upper path 的反向组成正向 loop。因此，沿 upper path 继续 \(T_c\phi_j\)，得到 lower boundary。结合R3，
\[
 \boxed{\phi_j^--\phi_j^+=\kappa_j\psi^+,\qquad
 \psi^+=f_0^--f_0^+=-2i\,\operatorname{Im}f_0^+.}
 \tag{R8}
\]
这一步固定了符号，而不是仅引用“reflection 实系数”。于是
\[
 \boxed{\operatorname{Im}\phi_j^+(t)
   =\kappa_j\operatorname{Im}f_0^+(t),\quad c<t<b.}
 \tag{R9}
\]
before \(c\) 的 basis 全部实值；R9不适用于任意绕路后的 branch，也不将 \(\psi\) 在初始 fiber 与 upper boundary 混为同一个实值函数。

**R5（真实积分）。** 对 \(P\in t\mathbf R[t]\)，定义
\[
 I_j(P)=\int_\gamma\phi_j(t)P(t)w(t)\frac{dt}{t},
 \quad j=0,\ldots,8,\qquad
 J_c(P)=\int_c^b\psi^+(t)P(t)w(t)\frac{dt}{t}.
 \tag{R10}
\]
积分沿R3路径。0处仅有限 \(\log^j\)、\(P/t\) analytic；\(c\) 处全 solutions bounded（非整数 exponent \(7/2>0\)）；\(b\) 处 \(w=O((b-t)^{1/2})\)。这些使 improper integrals convergent，且 \(c\) 小半圆贡献趋零。因 \(P,w,t\) 在两实区间实值，可将 imaginary part 移入积分，令
\[
 \beta(P):=\operatorname{Im}I_0(P)
   =\int_c^b\operatorname{Im}f_0^+(t)P(t)w(t)\frac{dt}{t}
   \in\mathbf R.
 \tag{R11}
\]
由R8–R9，得到本轮关键的全分量身份
\[
 \boxed{\operatorname{Im}I_j(P)=\kappa_j\beta(P)
   \ (0\le j\le8),\qquad J_c(P)=-2i\beta(P).}
 \tag{R12}
\]
它对 signed real/rational \(P\) 全部成立，不依赖 positivity。\(\beta\) 是实线性 functional；不能把 \(\operatorname{Im}\) 当复线性算子，对 arbitrary complex \(P\) 无条件沿用R12。

## 3. 原九维商的准确实 comparison 和 determinant phase

**R6（实际 frozen 输入的完整范围）。** 前稿已证明并在本轮实际 FULL 重读的两个定理是
\[
 L^-=w^{-1}Lw=
 \left(D-\frac{2t}{1-4t}\right)^9
 -\Lambda t\prod_\ell\left(D-\frac{2t}{1-4t}+a_\ell\right),
\]
\[
 \mathcal H^-_K=
 tK[t]/L^-((1-4t)^9K[t]),\quad
 \dim_K\mathcal H^-_K=9,\quad [t],\ldots,[t^9]\text{ 为 basis},
 \tag{R13}
\]
其中 \(K=\mathbf Q,\mathbf R,\mathbf C\)，以及
\[
 \mathcal J(P)=(I_0(P),\ldots,I_7(P),J_c(P)),\quad
 \ker\mathcal J=L^-((1-4t)^9\mathbf C[t]),
\]
\[
 \overline{\mathcal J}:\mathcal H^-_{\mathbf C}
       \xrightarrow{\sim}\mathbf C^9.
 \tag{R14}
\]
R13中的 rational image 是原 \(L_{\rm pb}T=wP\) 的全部 rational particulars；它不是换了周期或 basis 的辅助 quotient。前稿的 pole 分析含 ordinary \(b\) 的9阶消失、0/c 的 indicial roots、全部 finite generators 和 \(\infty\) moderate growth，故R14不是仅以有限首项猜测 global fill。最高次 triangular coefficient 非零且 rational，保证 complex split 的 rational \(P\) 有 rational \(q\)。本稿使用这个已支付的完整输入，新增的是R12如何限制其有理实形式。

**R7（实比较同构）。** 定义
\[
 \mathcal J_{\mathbf R}(P)=
  (\operatorname{Re}I_0,\ldots,\operatorname{Re}I_7,\beta)(P).
 \tag{R15}
\]
split \(P\) 的R14全部零，故该 functional factor through \(\mathcal H^-_{\mathbf R}\)。反过来R15零与R12推出R14全零；R13的实系数 triangular uniqueness 使 \(P\) 在实 split image。于是实 kernel 为0，domain 与 target 都9维，故
\[
 \boxed{\overline{\mathcal J_{\mathbf R}}:
   \mathcal H^-_{\mathbf R}\xrightarrow{\sim}\mathbf R^9.}
 \tag{R16}
\]
八个复 MUM entries 的 imaginary coordinates只有一个方向，不能作十六个独立实条件计数。

**R8（matrix 的可检验 phase）。** 在 rational basis \(t^\ell,\ 1\le\ell\le9\)，令 \(N\) 的前八行是 \(\operatorname{Re}I_j(t^\ell)\), \(j=0,\ldots,7\)，末行为 \(\beta(t^\ell)\)，令 \(M\) 是R14的九行 actual complex comparison matrix。设 \(\kappa_{<8}=(\kappa_0,\ldots,\kappa_7)^t\)。则
\[
 N\in M_9(\mathbf R),\quad \det N\ne0,\qquad
 \boxed{M=
 \begin{pmatrix}I_8&i\kappa_{<8}\\0&-2i\end{pmatrix}N,\quad
 \det M=-2i\det N.}
 \tag{R17}
\]
等价地对M的第 \(j\) 行加 \(\kappa_j/2\) 倍末行，恰消掉其 imaginary part。此为实际 period matrix 的精确 determinant phase；既非 numerical determinant recognition，亦非 entries 的 Q-linear independence。

## 4. 完整填第二 MUM 已迫使所有实类分裂

**R9（实际 normalized particular 与完整 homogeneous defect）。** 固定
\[
 LB_P=wP,\quad B_P(0)=0,\quad
 B_P=\sum_{n\ge1}h_n
       \left(\sum_{m=1}^n\frac{[t^m](wP)}{m^9h_m}\right)t^n,
\]
\[
 C_P=\sum_{m\ge1}\frac{[t^m](wP)}{m^9h_m},\quad
 F_{P,u}=B_P-u f_0 .
 \tag{R18}
\]
对实 \(P\)，\(C_P\) 实值；\(F_{P,C_P}\) 在 \(|t|<b\) holomorphic，first conifold完整 jump 为 \((C_P-u)\psi\)。在R3的 apparent-point analytic lift，定义
\[
 H_P=B(x)+B(1-x)=\sum_{j=0}^8h_j(P)\phi_j,\quad
 h_j(P)=2(-1)^jI_{8-j}(P).
 \tag{R19}
\]
这是 actual Green concomitant 的全九项，不是只对 highest log 作投影。在 canonical \(x=1\) branch，
\[
 B^\sigma=H_P-B,\quad
 F_{P,u}^\sigma=H_P-u f_0-B .
 \tag{R20}
\]
右边 \(B,f_0\) 是原MUM0的 analytic germs。

**R10（full MUM gate）。** MUM 单Jordan块的 fixed space 为 \(\mathbf C f_0\)。R20给
\[
 \Delta^{\rm can}_{1}F_{P,u}=0
 \iff H_P\in\mathbf C f_0
 \iff h_1=\cdots=h_8=0
 \iff I_0=\cdots=I_7=0,
 \tag{R21}
\]
对每个固定 \(u\in\mathbf C\) 成立；这里 \(u f_0\) 在该右端仍 analytic。R21是完整 local germ identity，而非“最高 \(\log\) coefficient 为0”。

**R11（本轮 strengthened rational obstruction）。** 对 \(P\in t\mathbf R[t]\)，R21包含 \(I_0=0\)，故R12迫 \(\beta=0\) 与 \(J_c=0\)。结合R14，
\[
 \boxed{\Delta^{\rm can}_{1}F_{P,u}=0
 \iff P\in L^-((1-4t)^9\mathbf R[t]).}
 \tag{R22}
\]
对 \(P\in t\mathbf Q[t]\)，准确加强为
\[
 \boxed{\Delta^{\rm can}_{1}F_{P,u}=0
 \iff \exists q\in(1-4t)^9\mathbf Q[t]:\ P=L^-q.}
 \tag{R23}
\]
若右边成立，\(T(x)=wq(t)\in\mathbf Q[x]\)，\(T(0)=q(0)\)，normalized uniqueness 给
\[
 B=T-q(0)f_0,\qquad C_P=-q(0)\in\mathbf Q.
 \tag{R24}
\]
因此完整 MUM cancellation不能在这个真实有理 forcing family 中保留新的 nonsplit period。该结论比原来“九个 complete gates 全零才 split”更强；第九个 reflection gate 对实 forcing 已自动支付。它不讨论任意别的路径、任意 \(u\) 下其他 branches，或不同 base 的几何。

## 5. homogeneous comparison 的九维实形，不免费当 Betti lattice

**R12（所有 residual 的实结构）。** 定义 \(\eta=\kappa^th\)。前稿 first/second comparison 给
\[
 \eta-2C_P=-dJ_c=2id\beta.
 \tag{R25}
\]
由R4、R12、R19，
\[
 \operatorname{Im}h_j=2(-1)^j\kappa_{8-j}\beta
       =-d\beta v_j,\qquad
 \operatorname{Re}\eta=2C_P,\quad
 \operatorname{Im}\eta=2d\beta .
 \tag{R26}
\]
令 \(z=h-2C_Pe_0\)。则
\[
 \operatorname{Re}z\in\ker\kappa^t,\quad
 \operatorname{Im}z=-d\beta v,\qquad
 \boxed{z=T\overline z.}
 \tag{R27}
\]
证明最后一式：\(\kappa^t\overline z=-2id\beta\)，所以
\(T\overline z=\overline z-2id\beta v=z\)。\(T\) 的 +1 eigenspace为 \(\ker\kappa^t\)（8维），−1 eigenspace为 \(\mathbf Rv\)（1维）。R27的fixed real space因而9维，其8+1正是R16的实形式。

**R13（不偷换 rational structure）。** 原方程可有 motivic/Betti rational structure，但完整 logarithmic Frobenius basis 的 reflection entries \(\kappa_j,v_j\) 含实际 Gamma/zeta/π常数。R27是指定 paths 下的 real structure；它不说 \(z\) 的九个坐标 rational，也不说 \(N^{-1}\) 将 rational vector 送到 rational \(P\)。把 fixed real space 直接标成一个 Q-lattice 会遗漏 deRham/Betti comparison。本文所有 rational statements只由R13的 rational operator和R23的 uniqueness获得，没有借未证的 period conjecture。

## 6. 所有实非分裂类的真实十行秩与线性微分投影障碍

**R14（实际拉回仍不可约）。** 在 \(\mathbf P^1_t\setminus\{0,c,b,\infty\}\) 上 quadratic cover unramified，fundamental-group subgroup \(H\) index2；parity来自 ordinary \(b\)-loop与∞。homogeneous monodromy around \(b\) 为I。对任意 odd loop \(g\)，乘一个 \(b\)-loop变成 \(H\) 中的 loop且原 monodromy matrix不变。因此 \(\rho(H)=\rho(\pi_1)\)。原L的GM不可约条件是 \(D^9\) 的 roots0 与第二 polynomial 的 roots \(-a_\ell\) 无共同 modZ class，故 \(L_{\rm pb}\) 的实际9维solution representation也不可约。这里不无偿沿用一般 finite-cover irreducibility。

**R15（signed real family 的 rank theorem）。** 若 \(P\in t\mathbf R[t]\) 非分裂，R22使 \(\chi_1=\Delta^{\rm can}_1F_{P,u}\ne0\)。forcing single-valued给 \(L_{\rm pb}\chi_1=0\)，R14使其 monodromy orbit张成全部9维homogeneous space。若
\[
 r_*+\sum_{j=0}^8r_j(x)\delta^jF_{P,u}=0,\quad
 r_*,r_j\in\mathbf C(x),
\]
continuation差给 order≤8 operator annihilating \(\chi_1\) 及其完整 orbit。它不可能杀九个独立 ordinary solutions，故所有 \(r_j=0\)，再 \(r_*=0\)。于是
\[
 \boxed{\operatorname{rank}_{\mathbf C(x)}
 \{1,F_{P,u},\delta F_{P,u},\ldots,\delta^8F_{P,u}\}=10.}
 \tag{R28}
\]
这覆盖所有 signed real nonsplit P，旧稿只对正强迫 \(P=t\) 给过该 rank。R28不表示每个P的最高log必为8；许多高阶项可以消失，但一个非零完整 homogeneous jump就足以给实际 orbit rank。

**R16（minimal scalar order）。** 若 \(P\ne0\)，\(R=wP\ne0\)，
\[
 (\delta-\delta R/R)L_{\rm pb}F_{P,u}=0
\]
给 \(\mathbf R(x)\)-coefficient order10 annihilator（Q-P时为 \(\mathbf Q(x)\)-coefficients）。任何 annihilator 的 continuation差杀 \(\chi_1\)，Ore division 迫它右含 \(L_{\rm pb}\)；order9时只能为 nonzero rational scalar times \(L_{\rm pb}\)，却把 \(F_{P,u}\) 送到 nonzero \(R\)。order≤8同R15不可能。所以非分裂实P的 minimal scalar order恰10，不能仅以“存在order10方程”来代替rank证明。

**R17（所有有理线性 differential projections）。** 设 \(P\in t\mathbf Q[t]\) 非分裂，\(A\in\mathbf Q(x)\langle\delta\rangle\) 满足
\[
 A\chi_1=0.
 \tag{R29}
\]
沿所有loops继续，rational coefficients不变，故A杀整个homogeneous space。用 \(L_{\rm pb}\) 的 rational leading coefficient作Ore division，
\[
 A=U L_{\rm pb}+V,\quad \operatorname{ord}V<9,\quad
 U,V\in\mathbf Q(x)\langle\delta\rangle .
 \tag{R30}
\]
V杀九维空间，因而V=0；包括A=0的情况。因此
\[
 \boxed{A=U L_{\rm pb},\qquad
 A F_{P,u}=U(wP)\in\mathbf Q(x).}
 \tag{R31}
\]
这对每个 \(u\in\mathbf C\) 成立；\(L_{\rm pb}f_0=0\)。若A仅有 \(\mathbf C(x)\) coefficients，同理输出 \(\mathbf C(x)\) rational function。为了填该指定完整 MUM jump而施行有理线性微分投影，不能保留非分裂数值 period。此处未排除 nonlinear tensor constructions、不同 base、不同 allowed leaf 或有理 forcing假设外的目标。

**R18（constant Euler polynomial 特例）。** 非零 \(Q(\delta)\)，\(Q\in\mathbf C[z]\)，不能满足R29。否则它杀全部 original homogeneous solutions，尤其 \(f_0\)。在 \(r_-\)，\(\delta=a(x)\partial_x\) 的 \(a(r_-)\ne0\)，所以 \(Q(\delta)\) 是 ordinary scalar equation，局部 solutions analytic；而 \(f_0\) 有R3非零reflection jump，矛盾。这一步不限于 \(\deg Q<9\)，也不把 \(x=1/2\) 的 apparent point 当 ordinary。

## 7. 部分 gates 的真实有理条件与一个最低-log target line

**R19（部分完整 entries 的准确实 codimension）。** 对 \(S\subset\{0,\ldots,7\}\)，设 \(k=|S|\)。R16使八个 \(\operatorname{Re}I_j\) 与 \(\beta\) 独立。若至少一个 \(i\in S\) 有 \(\kappa_i\ne0\)，则
\[
 I_i(P)=0\ \forall i\in S
 \iff \beta(P)=0,\qquad
 \operatorname{Re}I_i(P)=0\ \forall i\in S.
 \tag{R32}
\]
在实九维商上这是 \(k+1\) 个独立实条件，kernel维数 \(8-k\)。若所有所选 \(\kappa_i=0\)，则只有k个条件，维数 \(9-k\)。特别含0的subset总在前一情形；\(I_1\) 总是实数。这里无需声称未知的每个odd \(\kappa_i\) 都非零，也没有把复维数当有理解。

**R20（精确 Q-coefficient 矩阵接口）。** 把 \(P\) 按R13降到 \(P_q=\sum_{\ell=1}^9q_\ell t^\ell\)，\(q\in\mathbf Q^9\)。对含0的S，真实 rational forcing candidates恰为
\[
 \boxed{q\in\mathbf Q^9,\quad
 N_{S,\bullet}q=0,\quad N_{8,\bullet}q=0,}
 \tag{R33}
\]
其中行indices \(0,\ldots,7,8\) 依R15。split项不会改变这些 equations。N在 \(\mathbf R\) invertible不保证这个 real kernel含非零 rational vector。证明某个这样的Q-vector存在，或证明不存在，需要实际 scalar period relations；本轮没有以complexinverse或rational approximation构造假的Q-Taylor载体。

**R21（full reflected-conifold fill 与限定 low-log space）。** first conifold用 \(u=C_P\) 填掉以后，canonical second conifold residual恰
\[
 (\eta-2C_P)\psi=2id\beta\,\psi .
 \tag{R34}
\]
故它完整消失 iff \(\beta=0\)。在此 real slice，\(h,z\) 为实、\(\kappa^tz=0\)。若再要求 canonical \(x=1\) 的log degree≤j，\(0\le j\le8\)，准确 homogeneous defect具有
\[
 z=\sum_{\ell=1}^j a_\ell(e_\ell-\kappa_\ell e_0),
 \quad a_\ell\in\mathbf R .
 \tag{R35}
\]
因为 \(\phi_\ell\) 的最高log degree恰ℓ，低项不能取消更高项；R35的real dimension恰j。j=0就是R22的split。j≥1的非零类仍有完整 MUM jump，仍由R28给rank10。R35不是一个有效的 rational period projection construction，直到其在原 rational deRham lattice中的非零交点被证实。

**R22（可审查的 log1 目标）。** 特别令
\[
 I_0=\cdots=I_6=0,\quad I_7=1,\quad\beta=0.
 \tag{R36}
\]
R16唯一给一个 real degree≤9 class，由 \(q^{(1)}=N^{-1}e_7\) 表示。由于 \(\kappa_1=0\)，实际完整 defect为
\[
 H_P=2C_P f_0-2\phi_1,\quad
 F_{P,C_P}^\sigma=-2\phi_1-F_{P,C_P},\quad
 \Delta^{\rm can}_1F_{P,C_P}=-4\pi i f_0 .
 \tag{R37}
\]
两conifolds的 canonical full jumps为0，apparent点仍analytic，却留下一个真实log1。存在非零 **rational** forcing实现同一 line，当且仅当
\[
 \mathbf R q^{(1)}\cap\mathbf Q^9\ne\{0\},
 \tag{R38}
\]
等价于 \(q^{(1)}\) 的全部非零coordinate ratios rational。本文证明了目标line和其完整germ，而没有证明R38；以real vector直接当Q-forcing不合法。即便R38被证明，\(C_P\) 的数值评价、相应leaf以及更小费用仍须支付，R28的fulljet rank不会因log1而降至2。

**R23（最低次数的 double-conifold moment test）。** 冻结Euler representation在本轮FULL读取的真实参数下给 \(\operatorname{Im}f_0^+(t)>0\) on \((c,b)\)。于是R11的weight
\[
 d\omega(t)=\operatorname{Im}f_0^+(t)\frac{w(t)}t\,dt
\]
strictly positive且可积。非零 real P若 \(\beta(P)=0\)，必须在 \((c,b)\) 变号；正锥不能实现R34。degree1的 \(P=at\ne0\) 不可能。degree2 candidate \(P=a\,t(t-r),\ a\ne0\)，满足
\[
 \beta(P)=0\iff
 r=\frac{\beta(t^2)}{\beta(t)},\qquad c<r<b.
 \tag{R39}
\]
strict bounds来自positiveweight对t的weightedaverage。degree2非零 **rational** P可填canonical second conifold，当且仅当此真实moment ratio rational。它不是猜识数值，也不保证填MUM；比泛泛“找signedcoefficients”给出了一个具体的低次数 arithmetic period gate。该比值的有理性本轮未知。

## 8. Same-object Taylor、完整费用与未达成的数值目标

**R24（全有限处 cap 没有改善）。** 记 \(D_n=\operatorname{lcm}(1,\ldots,n)\)，\(D_0=1\)。对 rational P，\(w=1-2\sum_{m\ge1}\mathrm{Cat}_{m-1}t^m\in\mathbf Z[[t]]\)，fixed M使 \(M[t^m](wP)\in\mathbf Z\)。对每个prime power \(q=p^k\)，
\[
 C_q(s)=5\lfloor2\{s/q\}\rfloor+\lfloor5\{s/q\}\rfloor\in[0,9]
\]
给 \(h_n/(m^9h_m)\) 的q-layer
\(C_q(n)-C_q(m)-9\,1_{q\mid m}\)。若q≤n至少−9（q|m时 \(C_q(m)=0\)）；q>n≥m时 factorial floor随index monotone且q∤m，至少0。因此
\[
 D_n^9\frac{h_n}{m^9h_m}\in\mathbf Z,\quad
 MD_n^9[t^n]B_P\in\mathbf Z.
 \tag{R40}
\]
integer composition \(t=x(1-x)\) 与 \(D_m\mid D_n\) 给same x-cap。δ的multiplier \((1-x)/(1-2x)\) 有integer Taylor coefficients，fixed iterations不新增width；对每个 fixed \(u\in\mathbf Q\)，
\[
 M_uD_n^9[x^n]\delta^jF_{P,u}\in\mathbf Z,\quad 0\le j\le8.
 \tag{R41}
\]
这里所有primes同时支付，无prime表扩展，也不把实 \(C_P\) 自动当 rational Taylor shift。

**R25（rank 与费用接口）。** R28的实际10行是 \(\mathbf C(x)\)-independent，故对Q-P/uQ也 \(\mathbf Q(x)\)-independent。它们holonomic，same cap9的保守whole-array为九个width1 columns \((0,1,\ldots,1)^t\)，e=0。本人本轮实际CDTv2 PDF66–69核Definition6.0.1/Theorem6.0.2/Cor6.0.14，得
\[
 \sigma=(0,9,\ldots,9),\qquad
 \tau^\flat=9(1-10^{-2})=\frac{891}{100}.
 \tag{R42}
\]
这是safe upper预算，不是最小费用，更不是strict-margin证明。每个meromorphic pullback与其全部branch/fulljump仍需实际核对。R22–R39不会免费删掉一行或降低整化cap，R31的rational输出虽小却已丢失非分裂目标。

**R26（本轮推进的准确边界）。** 新内容是actualrealcomparisonR12/R16/R17、canonicalfullMUM已迫 rational split的R23、全signedrealfamily的rank10与linear differential projection分类R28/R31，以及有理partial-gate的准确矩阵/low-log/moment接口R33/R38/R39。它给一个具体否证：在此real/rationalanti-forcingfamily内，“先完整填MUM1而保留新period”不可行；highlog取消可行的real空间仍不等于Q载体。它没有给 \(\zeta(7)\)、Catalan、\(C_P\) 或任何新常数的无理性/线性无关性。

## 9. 原件范围、输入指纹与最终审查界限

**R27（本轮 actual primary read）。** 没有下载新原件、重复归档、TLS改动或render。实际FULL text读取：

- Golyshev–Mellit，[Gamma Structures and Gauss's Contiguity, arXiv0902.2003v1](https://arxiv.org/pdf/0902.2003v1)，literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf，SHA239c64b8bab41b12bc2a41d8eb3630d2935e04365bf6a3b9919193793551fc20，171695bytes、10归档页；本人本轮actualFULL text PDF1–3，3distinct页。PDF2的原irreducibility/pseudoreflection/Jordan-blockhypotheses准确适用；pullbackR14自证。PDF1的motiviccomparison说明不当作scalarperiodrelations证明。
- 固定CDTv2，literature/cdt2024_l2_chi_minus3.pdf，SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771，4517169bytes、218归档页；本人本轮actualFULL text PDF66–69，4distinct页，只用于R42与whole-array/holonomic/meromorphichypotheses。

总计本轮个人7distinct PDF页，不继承上轮36、同行读域或整份页数。一次documentary lookup误选20页的 literature/cdt2025_arithmetic_holonomy.pdf，metadata SHA5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1、751610bytes；请求PDF66越界，未读取任何该PDF正文页，随后依冻结来源表选正确CDTv2。该lookup不创建producer或数学结果，不作为支持证据。

**R28（本轮 frozen 直接输入）。** 下列正文均实际全文重新读；不冒称读取其所有producer/原件或612历史稿：

- research/cdt_odd_gamma_quadratic_antiinvariant_extension_20261007.md，SHAc0a492603f559ed92b08fb685f79284ab3daf5feb9e10c52daf2ae1ea101ba27，26211bytes，全十节/所有A1–A49。本稿用其actual split classification、full Green/bridge/involution、finite generators/∞growth、comparisonkernel、Eulerpositivity、allprimecarry；authoring时另精读sections1–3及section4 Green规范，并重读sections7–10，不继承其primary页数。
- research/cdt_odd_gamma_connection_projection_20261007.md，SHA0bb53d928dbc925dadce1e7dd2c4a1bdd148af0e7c81be4659070aeb893fff44，18401bytes，全七节/G1–G19。用于actual Frobenius/reflection normalization与Gammaκ，不冒称本轮独立重读Bloch–Vlasenko公式页。
- authority audit完整JSONparse、physicalSHA/bytes核验及current_progress/full主报告§§196–200实际读取；本稿FINAL收据只pinimmutableauthority，不pin会继续append的background主报告。

**R29（闭合流程）。** 本稿所有新数学为纸证；旧/同行数学producer/result/guard不执行、不import、不rerun，数学producer创建0、运行0、prime扩表0、Lean0。候选必须作者实际FULL回读、指定reviewer正式实际FULL独审、收审后作者最后FULL回读，才一次生成单向FINAL来源收据。收据不pinmutablemain、futureaudit或peerreceipt；正文与review最终字节核验后不再编辑。当前只完成数学候选，不把structuralprogress当作数值irrationality目标达成。
