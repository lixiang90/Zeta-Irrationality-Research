# 第234轮Root：允许额外原点前像的全部共同图上界

2026-10-08。纸证，数学程序0。此处固定实际源
E(u)=atanh√(3u)/√(3u)、J_g(u)=√(1−4u)[g−2∫E/√(1−4u)]。
它关闭这个源的基本CDT证书的一个全局几何缺口；不是所有CDT判据或所有ζ/L源的no-go。

## 1. 从meromorphic原点前像得到真正holomorphic的参数

设φ:D→C为holomorphic、φ(0)=0、φ'(0)≠0，并假设(uE)∘φ在全盘meromorphic。
除以φ后e=E∘φ仍为meromorphic。由于E在u=1/3有不可消掉的log，φ必遗漏1/3：有限阶ramification只把log系数乘一个非零整数，不能使其meromorphic。

定义
\[
p(z)=3\phi(z)e(z)^2.
\tag{G1}
\]
在φ≠0处，E的ODE为ordinary，故e无pole，p holomorphic。
在任一φ零点的局部，E的延拓为
\[
E_{\rm native}(\phi)+A/\sqrt{3\phi}
\]
（选择局部平方根，A为常数）。若A≠0，e meromorphic迫使φ零点阶数为偶数；于是
\[
p=A^2+2A\sqrt{3\phi}\,E_{\rm native}(\phi)
+3\phi E_{\rm native}(\phi)^2
\]
仍holomorphic。A=0时也holomorphic，允许额外的奇阶native零点。
因此G1在整个D holomorphic。没有假设φ^(-1)(0)={0}，也没有把φ所有零点都要求偶阶。

在原点p(0)=0、p'(0)=3φ'(0)，原生身份给
\[
\phi(z)=\frac13\tanh^2\sqrt{p(z)}.
\tag{G2}
\]
右侧是p的单值meromorphic函数，因为tanh²√p是偶函数的复合。
G2在邻域成立后由meromorphic identity theorem延拓到全盘。右侧在
\[
p=-\pi^2(k+1/2)^2,\quad k=0,1,\ldots
\]
有真正pole；φ holomorphic故p遗漏全部这些值。只用前两个值就足够。

## 2. 两个被遗漏值给全盘导数上界

令a=π²/4，前两个值是−a与−9a。Möbius函数
\[
h(z)=\frac{p(z)+a}{p(z)+9a}
\]
holomorphic映D到C∖{0,1}，h(0)=1/9，且
\[
h'(0)=\frac8{81a}p'(0).
\tag{G3}
\]
这里h的pole值已由p遗漏；h=1需要p无限，而p为holomorphic有限值函数。

以下统一用**参数**而非modulus记完整椭圆积分：
\[
\mathcal K(x)=\int_0^{\pi/2}(1-x\sin^2\theta)^{-1/2}d\theta.
\]
标准modularλ覆盖在实点0<x<1的逆参数为
\(\tau(x)=i\mathcal K(1-x)/\mathcal K(x)\)。
从完整积分导数及Legendre关系，
\[
\tau'(x)=-\frac{i\pi}{4x(1-x)\mathcal K(x)^2}.
\]
单位盘到上半平面的最大导数为2Imτ。故C∖{0,1}在基点x的通用覆盖半径为
\[
R(x)=\frac{8x(1-x)}{\pi}\mathcal K(x)\mathcal K(1-x).
\tag{G4}
\]
任何h:D→C∖{0,1}、h(0)=x可提举到该覆盖，再用Schwarz，因此|h'(0)|≤R(x)。这不要求h univalent。

积分直接给\(\mathcal K(x)\le\pi/(2\sqrt{1-x})\)，所以
\[
R(1/9)\le 2\pi\sqrt{(1/9)(8/9)}
=\frac{4\pi\sqrt2}{9}.
\]
合G1、G3得真正覆盖全部允许原点前像的上界
\[
\boxed{|\phi'(0)|\le\frac{3\pi^3\sqrt2}{8}<18.}
\tag{G5}
\]
严格比较可用π<22/7、√2<3/2；不需要数值程序。
这是只由E meromorphic得到的upper。加入J_g的全盘延拓、标记点条件只会进一步限制图，不会扩大G5。

## 3. 它怎样限制算术holonomy证书

同源真实Q(u)-rank为3；已付基本LCD数组τ=7/3。
基本CDT界的双积分能量至少是log|φ'(0)|。
欲使rank upper<3，必须有log|φ'(0)|>3τ/2=7/2。
然而G5给|φ'(0)|<18<exp(7/2)。故**这个数组下，没有任何合法共同φ能用基本Theorem2.5.1给出所需矛盾**。

不能靠更好的图、额外原点前像或更准确的双积分upper消除这个必要门槛。
这不是从univalent-p模板的Koebe界外推；G1–G5已重新支付所有额外原点前像的量词。
若另外证明任何固定有理基都强迫τ≥7/3，则同一个结论可扩展到此三维函数空间的全部固定基基本证书；该算术不变性须另证明，本文不预领。
更强的CDT判据、随尺度的联合整格、新函数空间及新目标均不受本结论自动约束。

## 4. 依据和读取界限

G1–G5由Root自证，A独立消息逐项纸核通过；最终文件的独立FULL读取须另登记。
modularλ是CDT的通用三穿孔覆盖，完整积分的导数和Legendre关系可见
[DLMF19.4](https://dlmf.nist.gov/19.4)和[19.7](https://dlmf.nist.gov/19.7)。
DLMF用modulus k，本文用x=k²，已经显式转换，避免少一个2。
Root本轮实际FULL读当前作者版CDT16–17页的Theorem2.5.1与固定233相关源。
没有认证CDT完整证明或全部更强判据，也没有得到新的数值无理性定理。旧档不改。
