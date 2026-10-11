# 配对整数格真实 gcd 的主率：全尺度极限、闭式与同对象解析信用

日期：2026-10-06。NEW 数学稿，root。本稿不修改冻结输入，不执行、import 或重跑旧/同行数学 producer。只运行自己本轮 NEW 精确有理程序一次。本文给模型内部的全尺度命题；不是新的 ζ/L 值无理性定理，也不是 Lean 验证。

## G1. 实际对象及待填项

全文重读冻结 paired integral-lattice 稿 I1–I25 与 paired analytic 稿 R1–R16。取

\[
b_j=\binom{6n+j}{j-1},\quad j'=2n+1-j,\quad
\beta_m=\gcd(b_m,b_{m'}),\qquad 1\le m\le n.
\]

实际饱和格基为 \(G_m=(b_m/\beta_m)L_m+(b_{m'}/\beta_m)L_{m'}\)，加高 Newton 基 \(f_{2n},\ldots,f_{3n-1}\)。共同因子 \((6n+1)!\) 已从 \(d_j=(6n+1)!b_j\) 消去，不能再次算作 gcd 信用。

cardinal 恒等式给

\[
G_m(z)=S_{2n}(z)\sum_{j=m,m'}\frac{\kappa_j}{z-j},\quad
\kappa_j=\frac{b_j}{\beta_m S_{2n}'(j)}
=\frac{(-1)^j(6n+j)!}
{(6n+1)!\,\beta_m\,(j-1)!^2(2n-j)!}.
\tag{G1}
\]

特别两个 \((j-1)!\) 都保留。任一对 n 个 G 的多线性 Cauchy 展开项恰含共同系数 \((\prod_m\beta_m)^{-1}\)。与另一高块拼成整个 size-2n determinant 并平方后，所有项共同含 \((\prod_m\beta_m)^{-2}\)。这是同一实际整数基的准确分解，不是换格或免付分母。

本稿计算
\[
\gamma=\lim_{n\to\infty}\frac1{n^2}\sum_{m=1}^n\log\beta_m.
\]

## G2. 更一般的整数参数定理

对任意固定整数 \(B\ge1\)，令

\[
b_{B,j}=\binom{Bn+j}{j-1},\qquad
\beta_{B,m}=\gcd(b_{B,m},b_{B,2n+1-m}).
\]

记
\[
e_B(x,t)=\left\lfloor\frac{B+t}{x}\right\rfloor
-\left\lfloor\frac Bx\right\rfloor-\left\lfloor\frac tx\right\rfloor\in\{0,1\},
\]
\[
g_B(x)=\int_0^1\min\{e_B(x,t),e_B(x,2-t)\}\,dt.
\tag{G2}
\]

则全尺度极限存在且
\[
\boxed{\gamma_B=\lim_{n\to\infty}n^{-2}\sum_m\log\beta_{B,m}
=\int_0^{B+2}g_B(x)\,dx.}
\tag{G3}
\]

实际 \(g_B=0\) 于 \(x>B+1\)，因此上限也可改 \(B+1\)。非负性及 \(g_B\le1\) 立即给所有 \(\delta>0\) 的尾界 \(0\le\int_0^\delta g_B\le\delta\)。这里的共同 gcd 来自两整数的实际 valuation 最小值，不将各自 carry 单独平均后再取最小值。

## G3. G3 的证明：小素数与整数平移

Legendre 的阶乘 valuation 给每个 \(b_{B,j}\) 的每一层 \(p^k\) 一个 0/1 carry。若 \(p\le\sqrt{(B+2)n}\)，总 valuation 不超过 \(\lfloor\log_p((B+2)n)\rfloor\)。其在 \(\sum_m\log\beta_{B,m}\) 的总贡献至多

\[
n\,\pi(\sqrt{(B+2)n})\log((B+2)n)=O_B(n^{3/2}\log n)=o(n^2).
\tag{G4}
\]

对较大 p 只有一次 carry。准确公式分别是
\[
v_p(b_{B,m})=\left\lfloor\frac{Bn+m}{p}\right\rfloor
-\left\lfloor\frac{Bn+1}{p}\right\rfloor-\left\lfloor\frac{m-1}{p}\right\rfloor,
\]
\[
v_p(b_{B,m'})=\left\lfloor\frac{(B+2)n+1-m}{p}\right\rfloor
-\left\lfloor\frac{Bn+1}{p}\right\rfloor-\left\lfloor\frac{2n-m}{p}\right\rfloor.
\tag{G5}
\]

固定 \(\delta>0\)，对 \(\delta n\le p\le(B+2)n\)，除了 \(p\mid Bn+1\) 外，去掉 G5 的各处 ±1 仅在 \(m\equiv0\) 或相关单一剩余类模 p 时改变值，每 prime 影响 \(O_B(1+\delta^{-1})\) 个 m。对共同的基项 \(\lfloor(Bn+1)/p\rfloor\)，例外 prime 只能来自 \(Bn+1\) 的素因子；所有这些 prime 的贡献总误差至多 \(n\log(Bn+1)=O_B(n\log n)\)。最小值是 Lipschitz，误差界保持。

对非例外 prime，两个 carry 在 t=m/n 上的交集是有限区间并，其端点来自有限个 \(kx-B\)、\(kx\) 及反射端点。因此 Riemann sum 与 \(n g_B(p/n)\) 之差为 \(O_B(1+\delta^{-1})\)。利用 \(\sum_{p\le(B+2)n}\log p=O_B(n)\)，总误差仍为 \(o(n^2)\)。

## G4. G3 的证明：PNT 与小 x 尾

素数定理 \(\theta(u)=\sum_{p\le u}\log p\sim u\) 说明 \(n^{-1}\sum_p\log p\,\delta_{p/n}\) 在紧区间弱收敛于 dx。\(g_B\) 在 \([\delta,B+2]\) 有有限个分段线性部分及有限跳点，故可用于这个弱收敛。由 G5 和 G3 的固定-δ Riemann 估计，得到 \([\delta,B+2]\) 的积分极限。

剩余 \(\sqrt{(B+2)n}<p<\delta n\) 每个共同 valuation≤1，总贡献≤\(n\theta(\delta n)\)，其归一化 limsup≤δ。再与 G4 及积分尾≤δ合并，令δ→0，证明 G3。此步骤没有把有限 n 的 gcd 拟合外推。

## G5. x>2 的准确贡献

对 x>2，\(\lfloor t/x\rfloor=\lfloor(2-t)/x\rfloor=0\)。设 \(k=\lfloor B/x\rfloor+1\)，则共同 carry=1 当且仅当
\(kx-B\le t\le2-(kx-B)\)。在 t∈[0,1] 上其长度为 \((B+1-kx)^+\)，但只在 \(B/k<x\) 的相应 k 区间使用。

非零区间准确是 \((B/k,(B+1)/k)\)，\(1\le k\le\lfloor B/2\rfloor\)。各自积分为1/(2k)，于是
\[
\boxed{\int_2^{B+2}g_B(x)dx=\frac12 H_{\lfloor B/2\rfloor}.}
\tag{G6}
\]

对 B=6，为 \(1/2+1/4+1/6=11/12\)。具体区间 \((6,7),(3,7/2),(2,7/3)\) 已包括所有 x>2 贡献。

## G6. B=6 的周期折叠公式

令 \(q=\lfloor1/x\rfloor\)、\(d=\{1/x\}\)，以及 \(a=\{6d\}\)、\(b=\{2d\}\)、\(c=1-a\)。对于 u={t/x}，两个 carry 同时1的集合准确为

\[
E_d=[c,b-c]\ \cup\ [\max(c,b),\min(1,b+a)],
\tag{G7}
\]

空的或倒向区间按空集；端点无测度影响。两个区间各在 u≤b 和 u>b，不重叠。令 \(L(d)=|E_d|\)、\(K(d)=|E_d\cap[0,d]|\)。将 t/x∈[0,q+d] 分成 q 个完整周期及最后一段，得
\[
\boxed{g_6(x)=x\{qL(d)+K(d)\}.}
\tag{G8}
\]

由 G7，L、K 为有限分段仿射函数。它们的精确表达式由 max/min 直接确定，不需要有限测试作为证明。a 在 j/6 重置时，左极限 L=1、K=d，右极限 L=K=0。

## G7. 收敛级数与严格有理区间

代换 \(x=1/(q+d)\)，得到
\[
\gamma=\frac{11}{12}+\int_{1/2}^1\frac{K(d)}{d^3}\,dd
+\sum_{q=1}^{\infty}\int_0^1\frac{qL(d)+K(d)}{(q+d)^3}\,dd.
\tag{G9}
\]

所有项非负。取 q=1,…,Q 时，未计部分正是 x∈(0,1/(Q+1))，故严格可用的误差上界为1/(Q+1)。分段仿射区间中的原函数为
\[
F_q(d)=-\frac{l_1}{2}-\frac{l_0+k_1}{2(q+d)}
+\frac{dL(d)-K(d)}{2(q+d)^2},
\quad L=l_1d+l_0,\ K=k_1d+k_0.
\tag{G10}
\]

直接微分检查 \(F'_q=(qL+K)/(q+d)^3\)。NEW 精确程序以 Fraction 构造 G7 的24个仿射区间，逐段积分512个完整周期，并保留尾1/513，认证
\[
\boxed{1.455845\le\gamma\le1.457795.}
\tag{G11}
\]

这是 G3 已证明的主率积分的有理包围，不是有限 n 的主率猜测。证书同时核24个非边界参数的折叠一致性；全参数恒等式仍来自 G7–G8 的纸面证明。

## G8. 有限 digamma 闭式

记 \(\Psi(d)=\psi(1+d)\)，ψ 为 digamma。G10 的二阶分母项在所有区间端点相消：通常端点 L、K 连续；a 重置时两侧的 dL−K 都为0；d0、1 的端点值也为0。因此不剩 trigamma 常数。用绝对收敛的 digamma 差级数，逐段求和得

\[
\begin{aligned}
\gamma={416821\over360360}
&+\frac12\sum_{j=1}^{3}(2j-1)
 \{\Psi((2j-1)/14)-\Psi(1-(2j-1)/14)\}\\
&+\sum_{j=1}^{6}(j-7/2)\Psi(j/7)\\
&-\sum_{j=1}^{3}j\{\Psi(j/8)+\Psi((j+4)/8)\}\\
&+\sum_{j=1}^{3}(4-j)\{\Psi(j/6)+\Psi((j+3)/6)\}.
\end{aligned}
\tag{G12}
\]

有理项是 G9 的 x≥1 部分。各 ψ 系数之和为0，Euler 常数消去；用 ψ(z+1)=ψ(z)+1/z 与 Gauss 有理点公式，可进一步写成有理数、π乘实代数数及实代数数的 log 的有限组合。本文不需要这项进一步化简证明 G11。公式及有限区间表另由同行静态全文审阅，不重跑 producer。

## G9. 对同一个配对行列式的真实用途

G1 每个 Cauchy 展开项都保留相同 \((\prod\beta_m)^{-1}\)，故正平方包络内准确付
\[
-2\sum_m\log\beta_m=-2\gamma n^2+o(n^2).
\tag{G13}
\]

相对于在这个相同展开中把 β_m 统一粗略成1，G11给主率信用至少2.911690。这个差别不是把 gcd 当作额外格指数：格早已饱和，β已经同时影响 κ_j 及其有限素数数据。不能对原 form 再免费除 gcd，也不能把 G13 直接当实际 arithmetic cost 下界、restricted determinant 非零或无理性结论。

新的实际解析稿可写 \(\limsup n^{-2}\log|D_A(\xi)|\le-\beta_0-2\gamma\)，其中 β0 必须由同一 Cauchy/high-block 分解证明；G13不能与别的 layout、full3n det 或不同范数拼接。全素数 budget与无限 nonzero仍各有独立门槛。

## G10. 验证与来源范围

新程序 [verify](cdt_odd_paired_primitive_gcd_rate_20261006_verify.py) 及 [首次证书](cdt_odd_paired_primitive_gcd_rate_20261006_verify.json) 只用 Python 标准库，输出存在时拒绝第二次执行。本轮 root 数学 producer 首次运行1次；旧/同行 execute/import/rerun0，外部Lean0。程序认证分段公式、有限精确积分及由 G3/G7–G9 接入的严格尾界；不证明素数定理，不把 finite folding cases 替代所有参数证明。

参考一手公式：[NIST DLMF 5.4(ii)](https://dlmf.nist.gov/5.4.ii)，特别 Gauss 有理点公式5.4.19；[DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) 给本文使用的 digamma 差级数，[DLMF 27.12](https://dlmf.nist.gov/27.12) 列素数定理。PNT用于G4的准确归一化，paper G2–G4说明实际适用范围。三个原始HTML分别归档在 literature，来源与实际读取范围另保存在本轮来源收据。未宣称全文读未列出的外部论文。

已证的是完整 primitive gcd 主率及准确同对象信用。目标特殊值无理性/线性无关性、两有限域矩阵的无限unit、最终严格算术/解析margin仍未完成。此前goal保持active；本稿补实际费用，不把研究终点改成此内部lemma。
