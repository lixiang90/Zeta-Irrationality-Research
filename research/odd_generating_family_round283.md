# 第283轮 · Koecher 母函数逐权逼近的真实分母

2026-11-20。固定任意 \(h\ge0,\ w=2h+3\)，仅以 \(\zeta(w)=u/v,\ u\in\mathbb Z,\ v>0,\ (u,v)=1\) 作反证。下面各处将 \(h\) 固定后令截断增长。整族可以逐个隔离 \(\zeta(w)\)，但其标准截断的既约分母足以抵消实侧衰减；同一 WZ 对的所有整格端点也有此障碍。

## 标准截断

记 \(C_k=\binom{2k}{k}\)，\(P_n(z)=\prod_{j=1}^{n}(1-z/j^2)\)。Koecher–Leshchiner 恒等式给
\[
\sum_{h\ge0}\zeta(2h+3)z^h
=\sum_{k\ge1}\frac{(-1)^{k-1}}{2k^3 C_k}
  \left(5+4\sum_{i\ge1}\frac{z^i}{k^{2i}}\right) P_{k-1}(z),
\qquad |z|<1 .
\tag{K1}
\]
本次取 Hessami Pilehrood 与 Hessami Pilehrood 的独立证明为一手输入，核读其式 (1)、§2 的 \(F,G\) 恒等式及求和方向。仓库已有 Borwein–Bradley、Almkvist–Granville 的四步权系数和固定 \(\zeta(7)\) 的连接值构造。K1 的系数涵盖每个奇权。本文分析这个具体截断的既约分母。[WZ 原文 v2，页 1–3](https://arxiv.org/pdf/0801.1591v2) · [既有奇权总稿](odd_zeta_global_strategy_20261004.md) · [既有 \(\zeta(7)\) 构造](odd_zeta_next_routes_progress_20261004.md)

令 \(a_{k,h}\) 为右侧第 \(k\) 项的 \(z^h\) 系数，\(r_{h,N}=\sum_{k=1}^N a_{k,h}\)。在 \(|z|\le r<1\) 上乘积绝对值由 \(\exp(r\sum j^{-2})\) 控制，系数可逐项提取。记 \(e_{j,n}=e_j(1,1/2^2,\ldots,1/n^2)\)，\(e_{0,n}=1,\ e_{j,n}=0\ (j>n)\)。固定 \(h\) 时，括号乘积的 \(h\) 阶系数趋于 \(5(-1)^h e_{h,\infty}\ne0\)，故 \(a_{k+1,h}/a_{k,h}\to-1/4\)。对连续项比作几何支配，尾除以首项趋于 \(4/5\)，从而在每个充分大的 \(N\) 非零且
\[
\lim_{N\to\infty}\frac1N\log|\zeta(w)-r_{h,N}|=-\log4.
\tag{K2}
\]

令 \(d_n=\operatorname{lcm}(1,\ldots,n)\)。Legendre 公式中 \(v_p(C_k)\) 在每一层 \(p^j\le2k\) 最多贡献 1，在 \(j\le v_p(k)\) 时贡献 0，故 \(kC_k\mid d_{2N}\) 对 \(k\le N\) 成立。其余每个系数分母由 \(k^{2+2i}\) 与 \(h-i\) 个 \(j^2\) 的乘积清整。因此 \(2 d_{2N}d_N^{w-1}r_{h,N}\in\mathbb Z\)。

设 \(p\) 为奇素数且 \(p^2>2N,\ t=\lfloor N/p\rfloor\)。若 \(p\nmid k\)，系数中 \(C_k\) 在 \(p\) 处至多占一次，各 \(e_{j,k-1}\) 的分母至多含 \(p^{2j}\)，故 \(p^wa_{k,h}\equiv0\bmod p\)。若 \(k=\ell p\)，则 \(\binom{2\ell p}{\ell p}\equiv\binom{2\ell}{\ell}\ne0\bmod p\)，并有
\[
p^{2j}e_{j,\ell p-1}\equiv e_{j,\ell-1}\pmod p .
\]
后一式由展开后只保留所有指标为 \(p\) 倍数的项得到。于是 \(p^wa_{\ell p,h}\equiv a_{\ell,h}\bmod p\)，包括 \(h=0\)，且
\[
p^wr_{h,N}\equiv r_{h,t}\pmod p.
\tag{K3}
\]
所有同余均在 \(\mathbb Z_{(p)}\) 中。对 \(t\ge1\)，起始项 \(a_{1,0}=5/4,\ a_{1,h}=1\ (h\ge1)\)。对 \(k\ge2\)，绝对系数和至多 \((5+4/3)e^2/(2k^3 C_k)\)，因 \(\sum j^{-2}<2\)。又 \(C_k\ge6\cdot3^{k-2}\)，故 \(\sum_{k\ge2}(2k^3C_k)^{-1}\le1/64\)。由 \(e^2<8\)，得 \(r_{h,t}\ge5/24>0\)。固定 \(\epsilon>0\)，对 \(\epsilon N<p\le N\) 的 \(t\) 只取有限个正值，其非零有理分子的素因子有界。故所有这些充分大的 \(p\) 对实际截断都有 \(v_p(r_{h,N})=-w\)。先用素数定理再令 \(\epsilon\downarrow0\)，若 \(c_{h,N}=\operatorname{den}(r_{h,N})\)，则
\[
w\le\liminf\frac{\log c_{h,N}}N
\le\limsup\frac{\log c_{h,N}}N\le w+1,\qquad
\liminf\frac{\log(c_{h,N}|\zeta(w)-r_{h,N}|)}N\ge w-\log4>0.
\tag{K4}
\]
对 \(\zeta(7)\)，下界为 \(7-\log4\)。这些结论已经计入所有共同约分，并覆盖每条无界子列。

## 改变截断路径

同一原文 §2 取 \(z=a^2\)，写成
\[
F(n,j;z)=(-1)^n\,\frac{j!(n!)^2}{(2n+j+1)!}\,
                  \frac{P_n(z)}{(n+j+1)^2-z}.
\]
定义 \(S_{h;n,m}=r_{h,n}+\sum_{j=0}^{m-1}[z^h]F(n,j;z)\)，\(r_{h,0}=0\)，\(n,m\ge0\)。WZ 的有限矩形求和给
\[
\zeta(w)-S_{h;n,m}=\sum_{j\ge m}[z^h]F(n,j;z).
\tag{K5}
\]
具体地，\(F(n+1,j)-F(n,j)=G(n,j+1)-G(n,j)\)，从 \(0\) 到 \(n-1\) 再沿 \(j\) 求和，\(G(i,j)\to0\)，\(G(i,0)\) 为 K1 的第 \(i+1\) 项。在紧子圆盘和每一固定 \(n\) 上可逐项提取系数。因此同一端点的单调格路径给相同有理数。

令 \(T=n+m\to\infty\)。对奇素数 \(p^2>2T+1\)，有完整的缩小指标同余
\[
p^w S_{h;n,m}\equiv S_{h;A,B}\pmod p,\qquad
A=\lfloor n/p\rfloor,\quad B=\lfloor T/p\rfloor-A .
\tag{K6}
\]
证明时写 \(n=Ap+b,\ 0\le b<p\)。在 \([z^h]F(n,j;z)\) 中，若 \(p\nmid n+j+1\)，则 \(v_p((2n+j+1)!/[j!(n!)^2])=\lfloor(2b+(j\bmod p)+1)/p\rfloor\le2\)，同时 \(e_{i,n}\) 最多引入 \(2i\) 层。乘上 \(p^w\) 后该项为零模 \(p\)。

其余指标写作 \(j=\ell p-n-1=j'p+(p-b-1)\)，\(j'=\ell-A-1\)。记 \(V=(2n+j+1)!/[j!(n!)^2]\)，则 \(v_p(V)=1\)。对 \(0\le ap+b'<p^2\) 用 \((ap+b')!/p^a\equiv(-1)^a a! b'!\bmod p\)，并用 \(b!(p-b-1)!\equiv(-1)^{b+1}\)，得
\[
V/p\equiv(-1)^b\frac{(2A+j'+1)!}{j'!(A!)^2}\pmod p.
\]
再用 \(p^{2i}e_{i,n}\equiv e_{i,A}\bmod p\) 和 \((n+j+1)/p=A+j'+1\)，便有 \(p^w[z^h]F(n,j;z)\equiv[z^h]F(A,j';z)\)。其中 \(j'\) 恰遍历 \(0,\ldots,B-1\)。加上 K3 即得 K6。

所有 \(A+B\ge1\) 的缩小端点均为正。若 \(A=0\)，则 \(S_{h;0,B}=\sum_{j=1}^B j^{-w}\)。若 \(A\ge1\)，则
\[
\sum_{j\ge B}|[z^h]F(A,j;z)|
\le\frac{e^2}{3}\sum_{j\ge0}\frac{j!}{(j+3)!}=\frac{e^2}{12}<\frac23.
\]
这里 \(\prod_{i\le A}(1+1/i^2)\le e^2\)，\((A+j+1)^2-1\ge3\)，实系数前因子 \(j!(A!)^2/(2A+j+1)!\) 随 \(A\ge1\) 减少。由 K5，\(S_{h;A,B}>1/3\)。对 \(\epsilon T<p\le T\)，缩小端点属于有限集且 \(A+B\ge1\)。再用 K6 和素数定理，得到对所有趋向无穷的端点
\[
\liminf_{n+m\to\infty}\frac{\log\operatorname{den}(S_{h;n,m})}{n+m}\ge w.
\tag{K7}
\]
所有分母亦有全素数幂上界。对 \(j<m\)，整数 \((2n+j+1)!/[j!(n!)^2]\) 的任一 \(p\) 幂层至多贡献 2，故它整除 \(d_{2n+m}^2\)。系数余下的分母整除 \(d_T^{w-1}\)。合并标准前缀后，\(2d_{2n+m}^2 d_T^{w-1}\) 清整整个 \(S_{h;n,m}\)。

实处也可对所有端点作同尺度估计。对于固定 \(h\) 及充分大的 \(n\)，在每个 \(j\ge m\) 上都有
\[
(n+j+1)^2[z^h]\frac{P_n(z)}{(n+j+1)^2-z}
=(-1)^he_{h,n}+O_h((n+j+1)^{-2}).
\]
因 \(e_{h,n}\to e_{h,\infty}>0\)，K5 右侧同号，尾的绝对值至少为首项的绝对值。写 \(x=\sqrt2-1,\ 2x+x^2=1\)，对 \((x+x+x^2)^{2n+m}\) 取 \((n,n,m)\) 项，得
\[
\frac{(2n+m)!}{(n!)^2m!}\le x^{-2(n+m)}=(3+2\sqrt2)^{n+m}.
\]
结合首项中另有的 \((2n+m+1)(n+m+1)^2\) 两个多项式因子，尾的指数下界为 \(-\log(3+2\sqrt2)\)。对其余有限多个 \(n\)，取 \(m\to\infty\) 时系数的首个非零幂由 \(e_{\min(h,n),n}>0\) 给出，故尾最终同号且第一项绝对值仅按 \(m\) 的幂衰减。综上，
\[
\boxed{\displaystyle
\liminf_{n+m\to\infty}
\frac{\log\!\big(\operatorname{den}(S_{h;n,m})\,|\zeta(w)-S_{h;n,m}|\big)}
     {n+m}\ \ge\ w-\log(3+2\sqrt2)>0.}
\tag{K8}
\]
若固定 \(m/n\to d\ge0\)，还可精确计算实率。对 \(n\ge1\)，望远镜和给 \(\sum_{j\ge m}j!/(2n+j+1)!=m!/[2n(2n+m)!]\)，故首项下界和尾上界只相差多项式因子。Stirling 公式给 \(-n^{-1}\log|\zeta(w)-S_{h;n,m}|\to(d+2)\log(d+2)-d\log d\)，取 \(0\log0=0\)。除以 \(1+d\) 后最优斜率为 \(d=\sqrt2-1\)，恰达到 K8 所用的裸速率 \(\log(3+2\sqrt2)\)。

K8 包括依权重选择的端点、随逼近阶变化的斜率及稀疏子列。K8 作用于上述一个明确 WZ 对的完整有理端点。若更换 WZ 对或将不同端点作有偿线性组合，须重新核其模 \(p^w\) 主项是否抵消，并证明同一输出的非零性与净衰减。一项不同的明确候选是 Hessami Pilehrood 二元恒等式 (7) 中 \(y=0\) 的权七截断：其公布的几何衰减率为 \(10\log2<7\)，首问题是该新系数的既约分母能否避免 K4 的权七素数层。K6 只由上述 \(F\) 推出，尚不能移用于该候选。[另一 WZ 恒等式，Theorem 2](https://arxiv.org/pdf/0801.3310)

## 交叉复核

独审者由原文和两层指标复核 K1–K8，逐式确认了 K6 的 Wilson 符号、非存活项的最高 \(p\) 次数、粗端点的正性及两端点同时趋大的 K8。本文另独审了 Markov 稿 W7–W10。正交式按列模 \(p\) 分块后，行数和列数之差至多 1。方块的首要主子式在固定 \(w,\lfloor s/p\rfloor\) 下排除有限素数即可模 \(p^w\) 求逆。每个宽块恰保留一个模 \(p^w\) 参数，带符号调和头满足 \(p^w z_{j+bp}\equiv z_b\bmod p^w\)。故只要 \(v_p(B_s)<w\)，可先判两整数的精确赋值，再除以 \(B_s\) 得 \(v_p(c_s)=w\)。余数为 \(0,p-1\) 时各只有一个宽块，本原性使该参数为单位。异常素数重量界先固定局部阶数、再取素数定理的极限，适用于稿中给定的整个既约标量。[Markov 独立推导 W7–W10](odd_markov_all_weights_round283.md)

**正平方构造 S4–S7 独审。** 取 \(m=d-1,\ \alpha=m+3/2\)。反转的完整分子为 \(V(y)^2-y^{6d-2}P(-1)^2\)，分母为 \(1+y\)。常数头在 S4 所取的次数 \(6d-2-k\ (k\ge1)\) 均无贡献。又 \(V^2/(1+y)=((1-y)^{d+1/2}U^*)^2/(1-y^2)\)，故消去的奇数 \(k\) 恰在所保证的范围 \(4d+1\le k\le6d-3\) 内，\(4d-1\) 对应下一阶。[正平方稿 S4–S7](odd_weight_square_lattice_round283.md)

独立的 Bernstein 表示为
\[
 {2m\choose m}U(x)=\sum_{k=0}^m {m+\alpha\choose k}{m-\alpha\choose m-k}
       (x+1)^k(x-1)^{m-k}.
\]
系数检验可取 \(A_\alpha(z)=\sum_{j=0}^m(-1)^j{m+\alpha\choose j}{2m-j\choose m}z^j\)。两次 Vandermonde 卷积给 \(\sum_j{\alpha\choose l-j}{m-\alpha\choose j}{2m-j\choose m}={2m-l\choose m}{m+\alpha\choose l}\ (0\le l\le2m)\)，于是 \(A_\alpha-(1-z)^\alpha A_{-\alpha}=O(z^{2m+1})\)。代入 \(z=-2y/(1-y)\) 后正得上述 \(U\) 的反转对角 Padé 解。该解首一，\(U(-1)=(2m+1)/2^m\)，\(P(-1)=(-1)^d2(2m+1)\)，\(U(1)=\prod_{j=m+1}^{2m}(2j+3)/j\)。对 \(L(y)=U^*(y),\,M(y)=L(-y)\)，微分残差 \((1-y^2)(L'M-LM')-2\alpha LM=C y^{2m}\)，且 \(C\ne0\)，因有理函数的对数导数不能具有此半整数留数。由 \(L(0)=M(0)=1\) 和该残差，\(L,M\) 互素且次数为 \(m\)。任何另一解交叉相乘给次数不超过 \(2m\) 而消失到 \(2m+1\) 阶的多项式，故只差一个标量。

在 \(0\le x\le1\)，Bernstein 各项非负。\(k=m\) 项给 \(U(x)\ge(1+x)^m\)，\(k=m-j\) 项相对于首项至多 \((3/2)_j/j!=O(\sqrt{j+1})\)，而 \({2m+3/2\choose m}/{2m\choose m}\le e^{3/2}\)。因此两边只差 \(O((m+1)^{3/2})\) 因子，由 \(x(1-x^2)\) 的内点最大值 \(2/(3\sqrt3)\) 及固定权重测度的局部正密度，得到 S6 的精确裸率 \(-\log(27/4)\)。若 \(\lambda U\) 整，则 \(\lambda\) 是整数，\(U(-1)\) 强制 \(2^m\mid\lambda\)；\(U(1)\) 强制每个 \((4m+3)/3<p\le2m\) 的奇素数整除 \(\lambda\)。素数定理给出 S7 的正平方增长下界。以上只覆盖施加全部指定奇阶精确为零的一维族。既约有理逼近会消去 \(\lambda^2\)，其分母仍须另证；其余仅需满足模 \(p^w\) 同余的整数向量也须独立研究。
