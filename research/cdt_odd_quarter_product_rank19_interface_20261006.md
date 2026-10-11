# Γ-free quarter 乘积的19行全有理模型与 homogeneous 双log障碍

日期：2026-10-06。NEW纯证明；沿用本轮 root 互补quarter稿的实际 A、J 及 endpoint identity。只读冻结 P4/Sp4/Frobenius 输入，不执行/import旧数学 producer。safe19是 derivation-closed 上界，未证明实际最小秩19，也未构造 CDT Smith certificate。

## 1. 同一个 P4 forcing 与19行模型

写 \(F=A-1/2\)、\(Q=FJ\)，θ=x∂x。
\[
f=x^{-1/4}F,\quad g=x^{1/4}J,\quad
Pf=\frac{x^{-1/4}(1+x)}{512},
\quad Pg=\frac{x^{1/4}}{256}.
\tag{T1}
\]
T1 直接来自 \(K_AA=1/256\)、\(K_A(1/2)=(1-x)/512\) 及既有 J equation；没有以特殊纤维身份替代全函数。

令
\[
F_i=(\theta-1/4)^iF=x^{1/4}\theta^if,
\quad J_i=(\theta+1/4)^iJ=x^{-1/4}\theta^ig,
\qquad 0\le i\le3,
\]
\[
S_{ij}=\frac{F_iJ_j+F_jJ_i}{2},\quad0\le i\le j\le3.
\tag{T2}
\]
全部19行 \(1,F_i,J_i,S_{ij}\) 都有真正 rational Taylor germs，native x中无需Kummer初值。Q=S00。

置
\[
(c_0,c_1,c_2,c_3)=
\frac{x}{1-x}(1/16,1/2,3/2,2),
\quad a=\frac{1+x}{512(1-x)},\quad b=\frac1{256(1-x)}.
\]
四阶 P 精确展开给
\[
\begin{aligned}
\theta F_i&=F_{i+1}+F_i/4&&(i<3),\\
\theta J_i&=J_{i+1}-J_i/4&&(i<3),\\
\theta F_3&=F_3/4+\sum_{k=0}^3c_kF_k+a,\\
\theta J_3&=-J_3/4+\sum_{k=0}^3c_kJ_k+b.
\end{aligned}
\tag{T3}
\]
Leibniz rule中 ±1/4 项成对取消，因此
\[
\begin{aligned}
\theta S_{ij}&=S_{i+1,j}+S_{i,j+1}&&(i,j<3),\\
\theta S_{3j}&=\sum_kc_kS_{kj}+S_{3,j+1}+(aJ_j+bF_j)/2&&(j<3),\\
\theta S_{33}&=2\sum_kc_kS_{k3}+aJ_3+bF_3.
\end{aligned}
\tag{T4}
\]
所有系数均在 Q(x)，故这是完整的19行 differential generating model，Q的最小阶数≤19。它把25行tensor的 homogeneous antisymmetric 六维 kernel 从输出中准确删去，但没有据此证明剩余19行独立或 complete joint PV radical。

## 2. 完整 Taylor 算术上界

root的全部 prime-power证明给 A、J 的 prefix minimal denominators DA(N)、DJ(N)。T2的 shifted Euler derivatives至多产生固定 powers4分母；19行统一可用
\[
\boxed{2^{14}D_A(N)D_J(N)}
\tag{T5}
\]
清 n≤N 的全部 Taylor coefficients。单 F 行的 A−1/2 只有固定2，最高 shifted derivative order3给4³；Sij最高i+j=6，再乘symmetrization2与Fconstant2，用2²·4⁶=2¹⁴足够。有限卷积每个index≤N，DA DJ清每一项后也清总和。

T5 的 log 主率≤16N+o(N)。whole-prefix p²>4N+1 时，一方首层为p-integral、另一方亏损≤4，故全部19行在odd p处可用p⁴清前缀；shifted derivatives的固定2分母无odd-prime影响。此为真实矩阵列的可用上界，不能自动记成 tensor cosmall/Smith 信用；model19也不能不经独立性核验直接设 CDT 的 m=19。

## 3. 真实 conifold 及全 homogeneous analytic 背景的限制

root已证
\(Q(1)=4L(f_8,2)^2-16L(f_8,3)^2/\pi^2\)，并有非零 \(t^2\log^2t/256\)，t=1−x。进一步，首 tlogt 的系数由真实 endpoint公式直接给
\[
C_{1/4}J(1)+C_{3/4}F(1)
=M_0/64=L(f_8,2)/4>0.
\tag{T6}
\]
两份 log费用都不能由减去 Q1 常数消去。

现在明确一类更大的 homogeneous correction。令 normalized Frobenius family
\[
Y(\rho,x)=x^\rho\sum_{n\ge0}
\left[\frac{(1/2+\rho)_n}{(1+\rho)_n}\right]^4x^n,
\quad y_j=[\rho^j]Y\ (0\le j\le3).
\]
记 de-log parts bj，b0=y0，则
\(y_1=y_0\log x+b_1\)、
\(y_2=y_0(\log x)^2/2+b_1\log x+b_2\)。
全部 bj∈Q[[x]]，b1,b2常数为0。两份 Sym²P 的真实 homogeneous analytic germs 为
\[
V_0=y_0^2,\qquad V_2=y_0y_2-y_1^2/2=y_0b_2-b_1^2/2.
\tag{T7}
\]
V2=x/8+O(x²)，因此两者独立。

它们准确覆盖这个 homogeneous module 在0的全部 single-valued germs。P 的 local0为J4；在Frobenius基中N yj=y(j−1)、N y0=0。在10个对称单项式中用N的Leibniz作用逐项解N v=0，只剩自由系数c00、c02，且c11=−c02/2，其余系数均0。所以fixed space准确由y0²、y0y2−y1²/2生成，维2；最大nilpotent链长7，余链长3，即J7⊕J3。Sym²标准Sp4表示绝对不可约（维10），products输出非零，所以 map 到 scalar solution functions 没有kernel；T7 的两个fixed germs即全空间。任何 number-field-initial homogeneous analytic germ都是 V0,V2的代数常数线性组合，由它们常数1及首项x/8确定系数。这里不包括别的 inhomogeneous source 或 rational differential projections。

conifold处 Y 的首 tlogt系数为
\[
C(\rho)=\left[\frac{\Gamma(1+\rho)}{\Gamma(1/2+\rho)}\right]^4.
\]
它的 normalized rho coefficients对 j≤3给 yj 的全部 rank1 log方向。NIST DLMF的psi/trigamma special values给
\[
C(0)=1/\pi^2,\quad(\log C)'(0)=8\log2,
\quad(\log C)''(0)=-4\pi^2/3.
\]
因此 T7 的首 t²log² coefficients精确为
\[
\operatorname{log}^2(V_0)=1/\pi^4,
\qquad \operatorname{log}^2(V_2)
=C(0)C''(0)/2-C'(0)^2/2=-2/(3\pi^2).
\tag{T8}
\]

**命题。** 不存在 α,β∈Qbar，使 \(Q-\alpha V_0-\beta V_2\) 在conifold全纯。否则仅看最高log²即迫
\[
1/256=\alpha/\pi^4-2\beta/(3\pi^2),
\quad\pi^4/256=\alpha-(2\beta/3)\pi^2,
\]
与π²对Qbar超越矛盾。于是补入**全部** arithmetic-initial Sym² homogeneous analytic背景仍不能填本conifold。这不排新的 inhomogeneous tensor source、非线性/有理operator组合或其它解析叶。

## 4. 验证与文献范围

本文是全尺度纯证明，未创建、执行有限数学 verifier，不冒认实际最小秩19。root互补quarter稿 §§1–4已实际全文独审，A2移位、Gammafree endpoint、A primepower witness、wholeprefix窗口与log²通过；没有执行root producer。新的T1–T8及上述两个范围命题待root独审。

Gamma/trigamma公式实际核 NIST DLMF §§5.4、5.15，尤其5.15.1–3；版本1.2.8，2026-09-15。EHMM III/Rosen2026的实际原件阅读另见新manifest，与这些新纯证明不相互替代。没有数值无理性或线性无关性主结论。
