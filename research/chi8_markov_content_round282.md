# 第282轮 · 带边整数对的精确二进赋值与奇素数公因子

2026-11-20。沿用[本轮章程](chi8_markov_border_charter_round282.md)的 \(\Lambda=\Lambda_s,A,w,H,N\)，\(s\ge1\)。反证取任意既约 \(L(2,\chi_{-8})=u/v\)，\(v>0\)。对原 \(r_s=N/H\)，以下给出全尺度公因子，证明 \(c_s=H/\gcd(H,N)\) 恒为奇数，并算出这批约分之后仍需消除的二次项。

## 1. 差分的二进赋值

令 \(\Delta f(k)=f(k+1)-f(k)\)。对正奇数 \(b\)、整数 \(m\ge0\)，对一次倒数的有限差分恒等式关于 \(b\) 微分，得到
\[
\Delta^m(4k+b)^{-2}\big|_{k=0}
=(-4)^m m!(m+1)F_m(b),\qquad
F_m(b)=\frac1{\prod_{r=0}^{m}(b+4r)}
  \frac1{m+1}\sum_{r=0}^m\frac1{b+4r}.
\tag{C1}
\]
一次倒数式的右边为 \((-4)^mm!/\prod_{r=0}^m(b+4r)\)，由相邻两项作差归纳。需要控制的是上式中除以 \(m+1\) 后的赋值。

写 \(n=m+1,\ a=v_2(n)\)。若 \(a\ge1\)，对任意 \(j\ge1\)，\(\sum_{r<n}r^j\) 可被 \(2^{a-1}\) 整除。将前后半块对应项按模 \(2^{a-1}\) 配对，归纳得每个长度 \(2^a\) 的块均满足此式，而 \(n\) 是块长的整数倍。因此 \(n^{-1}\sum_{r<n}r^j\in 2^{-1}\mathbb Z_2\)，对奇 \(n\) 亦成立。展开 \((b+4r)^{-1}\) 的二进几何级数可得
\[
\frac1n\sum_{r<n}(b+4r)^{-1}
\equiv b^{-1}-2m b^{-2}\pmod 4.
\]
这里 \(j=1\) 用 \(\sum r/n=m/2\)，\(j\ge2\) 的每项均在 \(8\mathbb Z_2\)。于是 \(F_m(b)\) 是二进单位，其模 4 的值只依赖于 \(b\bmod4\)。若 \(m\) 为偶数，则 \(n\) 为奇数，进一步按模 8 展开乘积得
\[
F_m(b)\equiv b^{-(m+2)}
 \bigl(1-2m(m+2)b^{-1}\bigr)\equiv1\pmod8 .
\]
确实，乘积倒数第一阶为 \(b^{-n}(1-4b^{-1}\sum_{r<n}r)\)，乘以上述均值且保留模 8 即得第一式。由此
\[
U_m=\tfrac14\!\!\sum_{b=1,3,5,7}F_m(b)\in\mathbb Z_2,\qquad
V_m=\tfrac12(F_m(1)+F_m(3))\in\mathbb Z_2,\qquad
U_{2k}\equiv1\pmod2 .
\tag{C2}
\]
四项和模 4 等于 \(2(F_m(1)+F_m(3))\)，两项各为奇单位。

## 2. 同时约去分母的全部 2 因子

取整数矩阵 \(P_{ij}=(-1)^{i-j}\binom ij\)（\(j>i\) 时为零），它将首 \(s\) 项变为各阶差分，\(\det P=1\)。令
\[
d_i=2^{1+2i+v_2(i!)},\qquad e_i=d_i\,2^{v_2(i+1)},\qquad
D=\operatorname{diag}(d_i),\quad E=\operatorname{diag}(e_i).
\]
由 C1–C2，\(PAP^t\) 的 \(ij\) 项为
\(\Lambda(-4)^{i+j}(i+j)!(i+j+1)4U_{i+j}\)，\(Pw\) 的 \(i\) 项为 \(\Lambda(-4)^ii!(i+1)2V_i\)。恒等式
\[
\frac{(i+j+1)!}{(i+1)!\,j!}=\binom{i+j+1}{j}
\]
说明 \(M=E^{-1}PAP^tD^{-1},\ x=E^{-1}Pw,\ y=D^{-1}Pw\) 均为整数数组。于是原整数对满足
\[
(H,N)=2^{T_s}\bigl(\Lambda\det M,\ y^t\operatorname{adj}(M)x\bigr),
\qquad T_s=\sum_{i=0}^{s-1}\log_2(d_i e_i).
\tag{C3}
\]

除去奇单位，\(M_{ij}\bmod2\) 等于 \(\binom{i+j+1}{j}U_{i+j}\)。对行列按指标奇偶排序，偶行奇列块为零，因为上标偶而下标奇。另两个对角块是 \(\binom{a+b}{b}\) 和 \(\binom{a+b+1}{b}\) 模 2，这来自 C2 及 \((1+X)^2\equiv1+X^2\bmod2\)。对 \(h=0,1\)，首 \(t\) 行列组成的 \((\binom{a+b+h}{b})_{0\le a,b<t}\) 行列式恰等于 1。第 \(b\) 列是关于 \(a\) 次数为 \(b\)、首项系数为 \(1/b!\) 的多项式，节点 \(0,\ldots,t-1\) 的 Vandermonde 为 \(\prod_{b<t}b!\)。空块按 1 计。因此 \(\det M\) 为奇数。写 \(s_2(k)\) 表示二进数字和，由 \(v_2(i!)=i-s_2(i)\) 得
\[
\boxed{v_2(\gcd(H,N))=v_2(H)=
T_s=3s^2-2\sum_{0\le i<s}s_2(i)-s_2(s),\qquad v_2(c_s)=0.}
\tag{C4}
\]
二进公因子的对数为 \(3(\log2)s^2+O(s\log s)\)。式 C4 确定了原整数对在该素数的全部共同内容。

## 3. 一个可与 C4 相乘的奇公因子

记 \(\lambda_i\) 为 \([4i+1,4(i+s)+3]\) 内奇整数的最小公倍数之平方，\(\lambda_*=\operatorname{lcm}(1,3,\ldots,4s-1)^2\)。每个 \(\lambda_i\) 清掉 \(K\) 第 \(i\) 行和 \(b_i\)，\(\lambda_*\) 清掉整个 \(b\)。从 \(A,w\) 的各行取出 \(q_i=\Lambda/\lambda_i\)，从带边矩阵
\(\left(\begin{smallmatrix}A&w\\w^t&0\end{smallmatrix}\right)\) 的末行取出 \(q_*=\Lambda/\lambda_*\)。带边行列式等于 \(-N\)，同一个 \(q_*\) 也整除 \(H\) 在 \(\det A\) 之外的 \(\Lambda\)。故
\[
G_s=q_*\prod_{i<s}q_i\ \bigm|\ \gcd(H,N),\qquad (G_s,2)=1 .
\tag{C5}
\]

下面给出这个显式因子本身的渐近。\(q_*\) 的对数是 \(O(s)\)。对奇素数每一层 \(q=p^j\le 2s+2\)，行区间包含 \(2s+2\) 个连续奇数，必有 \(q\) 的倍数，该层不贡献。高幂 \(j\ge2\) 的全部贡献至多 \(2s\sum_{p^j\le8s,\,j\ge2}\log p=o(s^2)\)。对 \(2s<p\le8s\) 置 \(t=p/s\)。在第 \(i\) 行，候选奇倍数只有 \(p,3p\)。缺失行数等于 \(s f(t)+O(1)\)，取整误差统一有界，其中
\[
f(t)=
\begin{cases}
t/2-1,&2\le t\le 8/3,\\
1-t/4,&8/3\le t\le4,\\
t/4-1,&4\le t\le8 .
\end{cases}
\]
第一段中，\(i/s\) 在 \(t/4\) 与 \(3t/4-1\) 之间时两个倍数都不出现。后两段中仅 \(p\) 可出现，含 \(p\) 的行指标满足 \(t/4-1\le i/s\le t/4\)，再截到 \([0,1]\)。由素数定理与分部求和，
\[
\lim_{s\to\infty}\frac{\log G_s}{s^2}
=2\int_2^8 f(t)\,dt=\frac{14}{3}.
\tag{C6}
\]

## 4. 约分后的费用

在测度 \(d\nu=(1+u)d\mu\) 下，\(\det K_s\) 是前 \(s\) 个首一正交多项式平方范数之积。移位 Chebyshev 给第 \(j\ge1\) 个极小平方范数上界 \(4\,\nu([0,1])\,4^{-2j}\)。在长度 \(\ell=1-2\epsilon\) 的内区间上，密度有下界 \(c_\epsilon>0\)，移位首一 Legendre 的极小平方范数给下界 \(c_\epsilon\ell^{2j+1}/((2j+1)\binom{2j}{j}^2)\)。先取乘积并令 \(s\to\infty\)，再令 \(\epsilon\downarrow0\)，得到 \(\log\det K_s/s^2\to-\log4\)。由 \(\log\Lambda/s\to16\) 及 \(H=\Lambda^{s+1}\det K_s\)，原分母除以 C4、C5 给出的公因子后仍有
\[
\lim_{s\to\infty}\frac1{s^2}\log\frac{H}{2^{T_s}G_s}
=\frac{34}{3}-5\log2>0 .
\tag{C7}
\]
因此 C7 同时给实际 \(\log c_s/s^2\) 的上极限上界。当前分子、分母若要达到 \(\log c_s\le(\eta-\delta)s\)，剩余共同内容 \(\gcd(H,N)/(2^{T_s}G_s)\) 必须在同一子列取得 C7 全部二次率，并进一步满足线性门槛。C3–C6 给出全尺度算术改善。未知的奇素数共同内容仍使这个指定值的无理性悬而未决。
