# 第287轮独审 · 指定射线上的奇素数公因数

2026-11-21。取 \(d=2^s-2^{18}+9,\ s\ge19\)，并保留第286轮同一有理数 \(Z_d\)。令 \(A_d/D_d=Z_d\) 为既约表示，\(D_d>0\)，\(P_d=\prod_{2d<p<3d,\ p>127}p\)。实际丢掉第七层的素数对数之和为 \(\log\gcd(|A_d|,P_d)\)。要仅凭这个素数带和已经核准的较小奇素数排除射线，需要其除以 \(d\) 的上极限小于 \(0.8226279669\ldots\)。以下给出对每一个射线阶数适用的正积分表示，并据此检验能否直接用 \(A_d\) 的大小控制该公因数。[逐阶恒等式 W7](odd_pade_band_weight_round286.md) · [第287轮目标](odd_pade_single_ray_charter_round287.md)

## 共同有理数的正积分

置 \(m=d-1,\ N=3d-1\)，\(U=U_m\) 为 S5 的首一多项式，\(L(y)=y^mU(1/y)\)。令 \(F(y)=(1-y)^{d+1/2}L(y)\)，故 W7 中的 \(f_d^*(y^2)=(F(y)+F(-y))/2\)。定义偶多项式 \(H(y^2)=L(y)L(-y)\)。有严格等式
\[
 Z_d=2(2d-1)^2+
 \frac1{2\pi}\int_0^1 [t(1-t)]^{d-1/2}U(\sqrt t)U(-\sqrt t)\,dt.
 \tag{R1}
\]
为证此式，将 \(f_d^*(y^2)^2\) 展开。\(F(y)^2+F(-y)^2\) 是 \(u=y^2\) 的多项式，次数至多 \(2d-1<N\)，在 \(u=1\) 取 \(F(-1)^2=2^{2d+1}L(-1)^2=8(2d-1)^2\)。除以 \(1-u\) 后的 \(u^N\) 系数因此已知。交叉项则给 \((1-u)^{d-1/2}H(u)\) 的 \(u^N\) 系数。

对 \(n\ge d\)，半整数二项式系数满足
\[
 [u^n](1-u)^{d-1/2}
 =\frac{(-1)^d}{\pi}\int_0^1 t^{n-d-1/2}(1-t)^{d-1/2}\,dt .
\]
可由半整数阶乘公式或 Euler 的 Beta 积分直接核算。对 \([u^j]H(u)\) 逐项取 \(n=N-j\)，均有 \(n\ge2d\)。利用 \(H(1/t)=(-1)^m t^{-m}U(\sqrt t)U(-\sqrt t)\)，符号是 \((-1)^{d+m}=-1\)，积分中 \(t\) 的指数是 \(N-d-1/2-m=d-1/2\)。代回系数，得到 R1。[原多项式和端点 S5](odd_weight_square_lattice_round283.md) · [Euler 的 Beta 积分](https://dlmf.nist.gov/5.12.E1)

## 分子高度的障碍

写 \(\varepsilon_d=Z_d-2(2d-1)^2\)。对全部 \(d\to\infty\)，从而在指定射线上也有
\[
 \varepsilon_d>0,\qquad
 \lim_{d\to\infty}\frac{\log\varepsilon_d}{d}=-\log4,\qquad
 \liminf_{d\to\infty}\frac{\log D_d}{d}\ge\log4,\qquad
 \liminf_{d\to\infty}\frac{\log|A_d|}{d}\ge\log4 .
 \tag{R2}
\]
用 S5 的积分式 \(U(x)=J_m^{-1}\int_0^1 v^{1/2}\phi_x(v)^m\,dv\)，其中 \(J_m=\int_0^1 v^{1/2}(1-v)^{2m}\,dv\)，\(J_m^{-1}=O((m+1)^{3/2})\)，
\[
\phi_x(v)=(1-v)\{2v+(1-v)(1+x)\}
           =1+x-2xv-(1-x)v^2.
\]
在 \(0\le x\le1\)，\(\max\phi_x=1+x\)。在 \(x=-r,\ 0<r<1\)，最大值是 \(1/(1+r)\)，取在 \(v=r/(1+r)\)。因而 \(0<U(r)U(-r)\ll(m+1)^3\) 对 \(0\le r\le1\) 一致成立，给出 R2 的指数上界。

对下界，在 \(1/3\le t\le2/3\) 令 \(r=\sqrt t\)。S5 的首项给 \(U(r)\ge(1+r)^m\)。计算 \(U(-r)\) 时只取 \(v=r/(1+r)\) 附近宽度 \(1/\sqrt m\) 的区间。区间在 \((0,1)\) 的紧子集中，\(\phi_{-r}\ge(1+r)^{-1}(1-O(1/m))\)，故 \(U(-r)\gg (1+r)^{-m}/\sqrt m\)。在 \(t=1/2\) 的任意固定小邻域代回 R1，再收缩邻域，得下指数 \(-\log4\)。最后 \(\varepsilon_d D_d=A_d-2(2d-1)^2D_d\) 是正整数，故 \(D_d\ge1/\varepsilon_d\)，从而得到分子与分母的高度下界。

## 能先剥掉的一整段素数

对充分大的 \(d\)，另一个不相交的素数积
\[
 Q_d=\prod_{3d<p<4d}p
\]
总是整除 \(A_d\)。确实，在这段仍有 C1 的 \(L(y)=(1-y)^K E_0(y^2)\bmod p\)，\(K=(p-2d-1)/2\)。于是 \(F(y)\equiv(1-y^p)^{1/2}E_0(y^2)\)。由于 \(N=3d-1<p\)，取偶部至 \(u^N\) 得 \(f_d^*(u)\equiv E_0(u)\)。又 \(\deg E_0^2\le m-K<N\)，故 \(R_N\equiv E_0(1)^2\)。在 \(y=-1\) 求值，
\[
 E_0(1)^2=2^{-2K}L(-1)^2
 \equiv (2d-1)^2\,2^{-(p-3)}
 \equiv4(2d-1)^2\pmod p .
\]
这就给 \(Z_d\equiv0\bmod p\)，相关系数由 \(F\) 的形式平方根及 \(p\)-整的原始 \(L\) 在 \(p\) 处取模。由 \(\gcd(P_d,Q_d)=1\)，逐阶有
\[
  \gcd(|A_d|,P_d)=\gcd(|A_d|/Q_d,P_d),\qquad
  \log Q_d=(1+o(1))d. \tag{R3}
\]
对 \(p\mid\gcd(A_d,P_d)\)，R1 的小余项在 \(\mathbb F_p\) 中恰等于 \(-2(2d-1)^2\ne0\)，它的分子与该 \(p\) 互素。要在剥除 \(Q_d\) 之后判断高度法是否够用，还可精确求 \(D_d\) 在 2 处的阶。[第284轮首层带](odd_pade_prime_cost_round284.md)

## 共同有理数的二进分母

记 \(s_2(n)\) 为二进数字和，\(\nu=\nu_2\)。主稿的奇部恒等式给
\[
 O_d(z)={}_2F_1(-1/4,1/4;d+1/2;z),\quad
 H_d=[z^d]\frac{O_d(z)^2}{1-z},\quad
 Z_d=K_d^2H_d,\qquad \nu(K_d)=1-2d .
\]
最后一式也可直接由 \(|K_d|=(2d+1)2^{-d}\prod_{j=d}^{2d-2}(2j+3)/j\) 求出。以下对每个 \(d\ge1\) 证明
\[
 \boxed{\ \nu(H_d)=-2d+s_2(3d)-2,\qquad \nu(D_d)=6d-s_2(3d).\ } \tag{R4}
\]
[奇部恒等式及 \(K_d\)](odd_pade_single_ray_round287.md)

令 \(A(w)={}_2F_1(-1/2,-d;d+1/2;w)\)。Gauss 二次变换给
\[
 O_d\!\left(\frac{4w}{(1+w)^2}\right)=\frac{A(w)}{\sqrt{1+w}} .
\]
置 \(x=w/(1+w)^2\)。因 \(dx/x=(1-w)\,dw/(w(1+w))\) 及 \(1-4x=(1-w)^2/(1+w)^2\)，对系数的形式留数换元得
\[
 4^dH_d=[w^d]\frac{(1+w)^{2d}A(w)^2}{1-w}.
\]
Pfaff 变换再给
\[
 A(w)=\sum_{k=0}^d h_k w^k(1-w)^{d-k},\qquad
 h_k=\frac{2^k\,d^{\underline k}\binom{d+k}{k}}
                {\prod_{i=0}^{k-1}(2d+1+2i)} .
\]
这里 \(a^{\underline k}=a(a-1)\cdots(a-k+1)\)。[Gauss 二次变换 15.8.15](https://dlmf.nist.gov/15.8.E15) · [Pfaff 变换 15.8.1](https://dlmf.nist.gov/15.8.E1)

写 \(b=\lfloor d/2\rfloor\)，\(M=2d-1\)。展开 \(A(w)^2\) 后，\(k=l=0\) 的项是
\[
 [w^d]\frac{(1-w^2)^{2d}}{1-w}
 =\sum_{j=0}^b(-1)^j\binom{2d}{j}=(-1)^b\binom M b.
\]
由 \(\nu\binom M b=s_2(b)+s_2(M-b)-s_2(M)\)，分别代 \(d=2b,2b+1\)，得到 \(\nu\binom M b=s_2(3d)-2\)。

其余项按对称性设 \(k\ge l,\ 1\le t=k+l\le d\)。需乘 \(h_k h_l\) 的系数为
\[
 [w^{d-t}](1-w^2)^{M-t}(1+w)^{t+1}.
\]
对 \((1+w)^{t+1}\) 取 \(w^j\)。若该项非零，则 \(0\le j\le t+1\)，\(d-t-j\) 为非负偶数。置
\[
 u=b-(d-t-j)/2=\bigl(t+j-(d\bmod2)\bigr)/2,\qquad 0\le u\le t.
\]
相对于 \(\binom M b\)，来自第一个因子的二项式的绝对值之比为
\[
 \frac{\binom{M-t}{b-u}}{\binom M b}
 =\frac{b^{\underline u}(M-b)^{\underline{t-u}}}{M^{\underline t}}.
\]
分母 \(M^{\underline t}=\prod_{j=1}^t(2d-j)\) 的偶因子乘积是
\(2^a(d-1)^{\underline a}\)，\(a=\lfloor t/2\rfloor\)。若 \(k>l\)，则 \(k\ge a+1\)，\(d^{\underline k}\) 已含 \((d-1)^{\underline a}\) 的全部因子。\(h_kh_l\) 另有因子 \(2^t\)，所以与基准项之比的二阶至少为 \(t-a\ge1\)。

若 \(k=l\ge1\)，则 \(a=k\)，\(d^{\underline k}\) 只需补 \((d-1)^{\underline k}\) 的末因子 \(d-k\)。当 \(d-k\) 为奇数时，比值的二阶至少为 \(k\)。当 \(d-k\) 为偶数时，由 \(t=2k\) 和 \(j\equiv d\bmod2\) 得 \(u\ge k\)，故 \(b^{\underline u}\) 含 \(b-\lfloor k/2\rfloor=(d-k)/2\)。此时比值的二阶至少为 \(k-1\)，对 \(k\ge2\) 已为正。余下的 \(k=1,\ d\) 奇时，\(h_1^2\) 还有偶因子 \(\binom{d+1}{1}^2\)，比值二阶同样为正。每个展开项所乘的 \(\binom{t+1}{j}\) 是整数，因此 \(k=l=0\) 项独占最低二阶。这证明 R4。

由 R1，\(Z_d>2(2d-1)^2\)。R3 与 R4 于是给出
\[
 \liminf_{d\to\infty}\frac{\log(|A_d|/Q_d)}{d}
 \ \ge\ 6\log2-1=3.158883\ldots .
\]
即使剥去 \(Q_d\)，整个剩余分子的大小仍超过 \(0.8226279669\ldots d\) 的对数门槛。实际 \(\gcd(|A_d|/Q_d,P_d)\) 可以小得多。现有稀疏计数允许每个 \(2^s-2^{18}+9\) 都落在例外集中，该射线上跨过门槛的七层重量下界仍待逐阶带内算术控制。[第286轮例外计数](odd_pade_band_sparse_round286.md)
