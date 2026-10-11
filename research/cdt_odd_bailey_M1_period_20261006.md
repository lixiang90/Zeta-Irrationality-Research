# 一阶连接矩的 Bailey 合流与精确临界周期

日期：2026-10-06。本文是新的纯证明笔记。没有执行或导入旧的、已冻结的或同行的数学生产脚本；没有使用数值识别。

## 1. 精确结论与适用范围

令
\[
 a_n=\left(\frac{(1/2)_n}{n!}\right)^4,
 \quad h_n=H_{2n}-H_n,
 \quad \Phi(t)=\left(\frac{\Gamma(t)}{\Gamma(t+1/2)}\right)^4,
\]
并采用已冻结连接矩笔记的定义
\[
 T(\varepsilon)=\sum_{n\ge0}\Phi(n+1/2+\varepsilon),
 \qquad M_1=-T'(0).
\]
对规范化新形式
\[
 f_8(\tau)=\eta(2\tau)^4\eta(4\tau)^4
\]
有精确恒等式
\[
 \boxed{M_1=64L(f_8,3).}\tag{1}
\]
这补齐的是本项目连接常数与已知模形式周期之间的精确比较。它本身不证明任何新的数值无理性；也没有给完整整 Betti 基底、\(M_4\) 的临界 L 值表达式或免费周期降秩。

## 2. 原始文献输入与实际核读

1. McCrorie，*Moments in Pearson's Four-Step Uniform Random Walk Problem and Other Applications of Very Well-Poised Generalized Hypergeometric Series*，DOI [10.1007/s13571-020-00230-1](https://doi.org/10.1007/s13571-020-00230-1)。出版 PDF 共 38 页，标题页为 2021 Volume 83-B, Supplement 2，S244–S281，版权 2020。实际核读 PDF 32–34 页（印刷 S275–S277），尤其 Bailey 分解 (A.1)，并与出版网页核对；不是全篇核读。[本地论文](../literature/mccrorie2020_pearson_vwp_bailey_published_20261006.pdf)。
2. Rogers–Wan–Zucker，arXiv [1303.2259v2](https://arxiv.org/abs/1303.2259v2)，实际重读 PDF 13–14 页。其 (31) 精确给出
\[
 L(f_8,3)=\frac{\pi^4}{128}\mathcal W(0),\tag{2}
\]
其中
\[
 \mathcal W(\varepsilon)=W(1/2+\varepsilon;1/2,1/2,1/2,1/2,1/2),
\]
\[
 W(a;c,d,e,f,g)={}_7F_6\!\left(
 \begin{matrix}a,1+a/2,c,d,e,f,g\\
 a/2,1+a-c,1+a-d,1+a-e,1+a-f,1+a-g\end{matrix};1\right).
\]
参数顺序可置换；\(\mathcal W(0)\) 正是 (31) 中 \((5/4,(1/2)^6;1/4,1^5)\) 的级数。[本地论文](../literature/rogers_wan_zucker2013_moments_elliptic_critical_l_values_v2.pdf)。

## 3. 合流公式与两边的极点

将 (A.1) 中 \(a=1/2+\varepsilon\)、其余五个参数均取 \(1/2\)。对足够小且非零的 \(\varepsilon\)，逐项代入得到
\[
 \mathcal W(\varepsilon)=A(\varepsilon)F_+(\varepsilon)
                      +B(\varepsilon)F_-(\varepsilon),\tag{3}
\]
\[
 F_+(\varepsilon)={}_4F_3\!\left(
 \begin{matrix}1/2+\varepsilon,1/2,1/2,1/2\\
 1+\varepsilon,1+\varepsilon,1-\varepsilon\end{matrix};1\right),
\]
\[
 F_-(\varepsilon)={}_4F_3\!\left(
 \begin{matrix}1/2+2\varepsilon,1/2+\varepsilon,1/2+\varepsilon,1/2+\varepsilon\\
 1+\varepsilon,1+2\varepsilon,1+2\varepsilon\end{matrix};1\right),
\]
\[
 A(\varepsilon)=
 \frac{\Gamma(1+\varepsilon)^3\Gamma(\varepsilon)}
 {\Gamma(3/2+\varepsilon)\Gamma(1/2+\varepsilon)^3},
\]
\[
 B(\varepsilon)=
 \frac{\Gamma(1+\varepsilon)^5\Gamma(-\varepsilon)\Gamma(1/2+2\varepsilon)}
 {\Gamma(3/2+\varepsilon)\Gamma(1/2+\varepsilon)\Gamma(1/2)^3\Gamma(1+2\varepsilon)^2}.
\]
注意 \(A,B\) 各有极点。不能把 \(\varepsilon=0\) 直接代入两个分项。

使用
\(\psi(1)=-\gamma\)、\(\psi(1/2)=-\gamma-2\log2\)、
\(\psi(3/2)=-\gamma-2\log2+2\)，去掉 \(\Gamma(\pm\varepsilon)\) 的两个正则因子在零点都等于 \(2/\pi^2\)，其对数导数分别为
\[
 \gamma+8\log2-2,\qquad -\gamma-2.
\]
所以
\[
 A(\varepsilon)=\frac2{\pi^2}
 \left(\frac1\varepsilon+8\log2-2+O(\varepsilon)\right),
\]
\[
 B(\varepsilon)=\frac2{\pi^2}
 \left(-\frac1\varepsilon+2+O(\varepsilon)\right).\tag{4}
\]

## 4. 级数微分与极限交换

两条 \({}_4F_3\) 的下参数和减上参数和恒等于 1。足够小的复圆盘中参数避开极点，Gamma 比值的统一渐近给出级数项 \(O((n+1)^{-2})\)；可在更大的紧圆盘上使用 Cauchy 估计得到导数的同阶控制。因而级数及其一阶导数在零点邻域一致收敛，可逐项微分。

记 \(F_0=\sum a_n\)。上参数在 \(1/2\) 的 Pochhammer 对数导数为 \(2H_{2n}-H_n\)，下参数在 1 的导数为 \(H_n\)。参数位移的总权重分别为 1 和 5，因此
\[
 F_+(0)=F_-(0)=F_0,
\quad F_+'(0)=2\sum a_nh_n,
\quad F_-'(0)=10\sum a_nh_n.\tag{5}
\]
\({}_7F_6\) 的收敛余量为 \(1+4\varepsilon\)，在小圆盘内实部保持正值，左侧也解析。因此 (3) 可在两边极点相消后取合流极限。由 (4)–(5)，
\[
 \mathcal W(0)=\frac2{\pi^2}
 \left[8\log2 F_0+F_+'(0)-F_-'(0)\right]
 =\frac{16}{\pi^2}\sum_{n\ge0}a_n(\log2-h_n).\tag{6}
\]

另一方面，
\[
 \Phi(n+1/2)=\pi^2a_n,
 \quad \Phi'(n+1/2)=8\pi^2a_n(h_n-\log2),
\]
故
\[
 M_1=8\pi^2\sum_{n\ge0}a_n(\log2-h_n),
 \qquad \mathcal W(0)=\frac{2M_1}{\pi^4}.\tag{7}
\]
结合 (2) 即得 (1)。此外 \(h_n<\log2\)，故正性与已知 \(M_1>0\) 一致；这只是符号核对，不代替证明。

## 5. 对项目连接极限的改进

沿用冻结笔记中已证明的真实极限，现可精确写成
\[
 \lim_{n\to\infty}\frac{F_n^{[r]}}{A_n}
   =\frac{\pi^4M_{2r}}{64L(f_8,3)},
\]
\[
 \lim_{n\to\infty}\frac{C_n^{[r]}}{A_n}
   =-(2r+2)!(2^{2r+3}-1)\zeta(2r+3)
      +\frac{\pi^4M_{2r}}{64L(f_8,3)}.
\]
特别是 \(r=2\) 的修正周期为 \(\pi^4M_4/(64L(f_8,3))\)。这使分母成为明确的模形式临界周期，却仍须处理分子的扩张周期。

旧 CY 文献中的 Frobenius 坐标 \(w_+=4M_1\) 因而等于 \(256L(f_8,3)\)。这里只使用已明确的 Frobenius 坐标定义，不能由此宣称一个整 Betti 周期已校准。

## 6. 审核与归档状态

这是经典 Bailey 分解与既有临界 L 值公式的严格推论。项目中的新贡献是关闭先前尚未确定的 \(M_1\) 精确比较接口；不主张这条恒等式是文献中未出现过的新定理。根代理已经逐项读原始 PDF 公式并独立推导；同行实际阅读的结论另记于交付审核。
