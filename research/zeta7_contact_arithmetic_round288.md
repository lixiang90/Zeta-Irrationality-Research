# 第288轮独审 · 权七系数的符号和有限公式

取任务书中的有理函数，\(n,\ell\ge0\)，\(5\ell\le2n\)。写 \(a_{s,k}=[(t+k)^{-s}]R(t)\)、\(C_3=\sum_{k=0}^n a_{3,k}\)。四次求导后除以 \(24\)，在线性型中出现的 \(\zeta(7)\) 系数为 \(B=15C_3\)。改变整数求和下界只改变有理项。下面对每个容许的 \(n,\ell\) 证明
\[
  (-1)^{n+\ell}C_3\ \ge\ 2\binom{2n}{n}\binom{n+\ell}{\ell}^{5}>0.                    \tag{H1}
\]
当 \(\ell=0\) 时等号成立。[有理函数与真实系数对](zeta7_contact_charter_round288.md)

## 极点处的一阶导数

令 \(H_0=0\)、\(H_j=\sum_{i=1}^j1/i\)，并记
\[
 W(k)=\binom nk^4\binom{k+\ell}{\ell}^5\binom{n-k+\ell}{\ell}^5,
 \qquad
 T_k=5(H_{n-k+\ell}-H_{k+\ell})+9(H_k-H_{n-k}).
\]
在 \(t=-k\) 取 \((t+k)^4R(t)\) 的常数项和一次项，得到
\[
 a_{4,k}=(-1)^\ell(n-2k)W(k),\qquad
 a_{3,k}=(-1)^\ell W(k)\{2+(n-2k)T_k\}.                     \tag{H2}
\]
在 \(n=2k\) 处上式直接给 \(2(-1)^\ell W(k)\)。一般地，反射给 \(a_{s,n-k}=(-1)^{s+1}a_{s,k}\)。无穷远的衰减给 \(\sum_k a_{1,k}=0\)。故求和后只剩三阶极点贡献的周期，乘数为 \(\binom64=15\)。

把 \(W(k)\) 由 Gamma 倒数和多项式延伸到复变量 \(k\)。在 \(0\le k\le n\) 的整数处，其对数导数为 \(-T_k\)。其余整数处，\(\binom nk^4\) 至少四阶为零。写 \(x=k-n/2\)，\(\Lambda(f)=\sum_{x\in\mathbb Z+n/2}(xf(x))'\)，则 H2 给
\[
 C_3=2(-1)^\ell\Lambda(W(n/2+x)).
\]
以下各个格点导数之和只有有限项。

## 零接触的直接计算

固定 \(n\ge1\) 并用 Rogers–Dougall 的终止 \({}_5F_4(1)\) 求和，取三个上参数同为 \(-n\)，先约去很适定参数之比再求导。得到有理函数恒等式
\[
 S(a)=\sum_{k=0}^n(a+2k)
  \frac{(a)_k(-n)_k^3}{k!(1+a+n)_k^3}
 =a\frac{(1+a)_n(1+a+2n)_n}{(1+a+n)_n^2}.
\]
在 \(a=-n\) 求导。右端只须对含零因子的 \((1+a)_n\) 求导，得 \((-1)^n\binom{2n}{n}\)。左端导数为
\[
 \sum_{k=0}^n\binom nk^4[1+(2k-n)(H_{n-k}-H_n-3H_k)].
\]
用 \(k\leftrightarrow n-k\) 对称化，在 \(\ell=0\) 时这等于 H2 的 \(C_3/2\)。\(n=0\) 可由 \(R=2/t^3\) 直接核对。因此 \(B=30(-1)^n\binom{2n}{n}\)。[NIST DLMF 16.4.9 及其终止条件](https://dlmf.nist.gov/16.4.E9)

## 四个不同宽度的求和

置 \(G_m(x)=1/[\Gamma(1+m+x)\Gamma(1+m-x)]\)。让四个 \(m_i\) 同为整数或同为半奇整数，\(m_i\ge-1/2\)，\(\sum_i m_i\ge0\)。格点取 \(\mathbb Z+m_1\)。在 \((-1)!\) 出现在分母时将其倒数解释为零。则
\[
 \Lambda\!\left(\prod_{i=1}^4G_{m_i}\right)
 =(-1)^{2m_1}\frac{(\sum_i m_i)!}{\prod_{i<j}(m_i+m_j)!}.       \tag{H3}
\]

先设 \(m_1=\min_i m_i\ge0\)。记 \(N=2m_1\)、\(d_i=m_i-m_1\)、\(D=d_2+d_3+d_4\)、\(x=k-N/2\)，并令 \(w(k)=\prod_iG_{m_i}(k-N/2)\)。有 \(w(0)=1/[N!\prod_{i=2}^4 d_i!(N+d_i)!]\)。用上参数 \(b_i=-N-d_i\ (2\le i\le4)\) 构造
\[
 S_*(a)=\sum_{k=0}^{N+\min_{i\ge2}d_i}
 (a+2k)\frac{(a)_k}{k!}
               \prod_{i=2}^4\frac{(b_i)_k}{(1+a-b_i)_k}.
\]
对 \(0\le k\le N\)，导数在 \(a=-N\) 处乘 \(w(0)\) 给
\[
 w(k)\left[1+(2k-N)\left(H_{N-k}-H_N-
                  \sum_{i=2}^4(H_{k+d_i}-H_{d_i})\right)\right].
\]
因 \(w(k)=w(N-k)\)，且
\(w'(k)/w(k)=\sum_{i=1}^4(H_{N-k+d_i}-H_{k+d_i})\)，这些项之和恰是 \(\sum_{k=0}^N[w(k)+(k-N/2)w'(k)]\)。

对外侧 \(k=N+h\)、\(1\le h\le\min_{i\ge2}d_i\)，此处 \(w(k)=0\)。首因子给 \(\partial_a(a)_k|_{a=-N}=(-1)^NN!(h-1)!\)，而
\[
 \left.\frac{d}{dk}\frac1{\Gamma(k+1)\Gamma(N-k+1)}\right|_{k=N+h}
 =\frac{(-1)^h(h-1)!}{(N+h)!}.
\]
三项 \((b_i)_k\) 的总符号为 \((-1)^k\)。所以外侧的导数乘 \(w(0)\) 为 \((2k-N)w'(k)\)，恰好把反射的 \(k\) 和 \(N-k\) 两项都计入。再向外有至少两个倒 Gamma 因子同时为零，导数也为零。于是 \(w(0)S_*'(-N)=\Lambda(\prod G_{m_i})\)。

同一 Rogers–Dougall 公式的右端为
\[
 a\frac{\prod_{i=2}^4\Gamma(1+a+N+d_i)\,
          \Gamma(1+a+3N+D)}
         {\Gamma(1+a)\prod_{2\le i<j\le4}\Gamma(1+a+2N+d_i+d_j)} .
\]
在 \(a=-N\) 时 \(a/\Gamma(1+a)\) 的导数为 \((-1)^N N!\)，\(N=0\) 时也成立。乘 \(w(0)\) 后即为 H3。

若恰有一个 \(m_i=-1/2\)，重排至第一位。此时 \(G_{-1/2}(x)=\cos(\pi x)/\pi\)。写 \(x=k+1/2\)、\(d_i=m_i+1/2\ge1\ (2\le i\le4)\)。反射后只需 \(k\ge0\)，两侧导数之和为
\[
 -\sum_{k\ge0}(2k+1)(-1)^k
       \prod_{i=2}^4\frac1{(d_i+k)!(d_i-1-k)!}.
\]
此和在 \(k>\min(d_i-1)\) 时终止。同一求和公式直接取 \(a=1\)、\(b_i=1-d_i\)，得其值
\[
 -\frac{(d_2+d_3+d_4-2)!}
        {\prod_{i=2}^4(d_i-1)!\prod_{2\le i<j\le4}(d_i+d_j-1)!}.
\]
这也是 H3。若有至少两个这样的 \(m_i\)，格点处余弦平方已有二重零点，而 H3 分母含 \((-1)!\)，两侧同为零。

## 正接触的有限公式

在四个初始的 \(G_{n/2}\) 上分配 \(5\ell\) 个因子 \((n/2+i)^2-x^2\)，其中每个 \(1\le i\le\ell\) 出现五次。可循环分配使每个位置收到至多 \(\lceil n/2\rceil\) 个，因 \(5\ell\le2n\)。在单一位置反复用 Gamma 递推
\[
 ((n/2+i)^2-x^2)G_m
 =((n/2+i)^2-m^2)G_m+G_{m-1}.
\]
若该位置已降 \(j\) 次，当前 \(m=n/2-j\)，保留项的系数为 \((i+j)(n+i-j)>0\)，下移项的系数为 1。以 \(A_{\mathbf j}\) 为选出四个下移次数 \(j_1,\ldots,j_4\) 的展开系数，\(J=\sum_i j_i\)。这些系数是非负整数，且 \(m_i=n/2-j_i\ge-1/2\)、\(\sum m_i=2n-J\ge0\)。由 H3 得
\[
 \frac{(-1)^{n+\ell}C_3}{2}
 =\frac{(n!)^4}{(\ell!)^{10}}
    \sum_{\mathbf j}A_{\mathbf j}
       \frac{(2n-J)!}{\prod_{i<v}(n-j_i-j_v)!}.                 \tag{H4}
\]
所有非零项均为正。只取 \(\mathbf j=0\)，其展开系数为 \(\prod_{i=1}^\ell[i(n+i)]^5\)，即得 H1。

对每项可选择对边 \((1,2),(3,4)\) 将阶乘改写为
\[
 (n!)^4\frac{(2n-J)!}{\prod_{i<v}(n-j_i-j_v)!}
 =\binom{2n-J}{n-j_1-j_2}
     \prod_{i=1,2\,;\,v=3,4}\frac{n!}{(n-j_i-j_v)!}
 \in\mathbb Z
\]
（任一底端阶乘为负时该项取零）。同时 H2 直接给 \(\operatorname{den}(C_3)\mid\operatorname{lcm}(1,\ldots,n+\ell)\)。因此 \(\operatorname{den}(C_3)\mid\gcd((\ell!)^{10},\operatorname{lcm}(1,\ldots,n+\ell))\)。特别对 \(\ell=0,1\) 目标系数总为整数。对 \(\ell=0\)，每个素数处的目标系数阶数严格等于
\[
 v_p(B)=v_p(30)+\sum_{r\ge1}
 \left(\left\lfloor\frac{2n}{p^r}\right\rfloor
       -2\left\lfloor\frac{n}{p^r}\right\rfloor\right).
\]
一般 \(\ell\) 的素分母只在 \(p\le\ell\) 出现。记 \(\vartheta(y)=\sum_{p\le y}\log p\)，则
\(\log\operatorname{den}(C_3)\le\vartheta(\ell)+O(\sqrt n\log(n+2))\)，因为二次及以上的素数幂只涉及 \(p\le\sqrt{n+\ell}\)，每个素数的总贡献至多 \(\log(n+\ell)\)。因此若 \(\ell/n\to\alpha\)，目标系数分母的对数上率至多为 \(\alpha\)。同一系数对的本原费用还涉及有理项 \(A\) 的分母以及两整数的共同因子。

## 零接触实际有理项的素数递降

取 \(\ell=0\)，\(b\ge0\)，记
\[
 L_{n,b}=\frac1{24}\sum_{t>b}R_n^{(4)}(t)=A_{n,b}+B_n\zeta(7).
\]
取素数 \(p\ge5\)，\(p^2>2(n+b+1)\)，写 \(n=up+r,\ b=vp+s,\ 0\le r,s<p\)。当 \(r+s<p\) 时有
\[
 p^7A_{n,b}\in\mathbb Z_{(p)},\qquad
 p^7A_{n,b}\equiv(-1)^r\binom{2r}{r} A_{u,v}\pmod p.       \tag{H5}
\]
右侧的 \(A_{u,v}\) 在 \(p\) 处整。这个公式同样包括 \(\binom{2r}r\equiv0\bmod p\) 的情形。

写 \(h_j=\binom{j+3}{4}\)、\(H_m^{(e)}=\sum_{h=1}^m h^{-e}\)，并给原 Laurent 系数加上阶数上标 \(a^{(n)}_{j,k}\)。部分分式给
\[
 A_{n,b}=-\sum_{k=0}^n\sum_{j=1}^4 h_j a^{(n)}_{j,k}H_{b+k}^{(j+4)} .
\]
在形式变量 \(X\) 中写
\[
 V_{n,k}(X)=(n-2k+2pX)\binom nk^4
       \prod_{h=1}^k(1-pX/h)^{-4}
       \prod_{h=1}^{n-k}(1+pX/h)^{-4}.
\]
这就是 \((pX)^4R_n(-k+pX)\)，所以 \([X^{4-j}]V_{n,k}=p^{4-j}a^{(n)}_{j,k}\)。所有因子在 \(\mathbb Z_{(p)}[[X]]\) 可展开，因为 \(n<p^2\)。写 \(k=ip+c\)，其中 \(0\le c<p\)。若 \(c>r\)，则 \(p\mid\binom nk\)，整项 \(V_{n,k}\) 模 \(p^4\) 消失。

若 \(c\le r\)，分开 \(p\) 的倍数和其余因子，令
\[
 W_i(X)=\binom ui^4\prod_{h=1}^i(1-X/h)^{-4}
                   \prod_{h=1}^{u-i}(1+X/h)^{-4},\quad
 w_c=\binom rc^4 .
\]
在每个完整长度 \(p\) 的区块，非倍数的逆元和模 \(p\) 为零。因此
\[
 \binom{up+r}{ip+c}\equiv\binom ui\binom rc
       [1+p\{uH_r-iH_c-(u-i)H_{r-c}\}]\pmod{p^2}.
\]
这里 \(\binom{up}{ip}\equiv\binom ui\bmod p^2\)，可从
\(\prod_{h=1}^{p-1}(ap+h)\equiv(p-1)!\bmod p^2\) 逐块相除。重新组装 \(V\) 给
\[
 V_{n,ip+c}\equiv W_i(X)w_c
 [r-2c+p(u-2i+2X)]
 [1+4p\{uH_r-iH_c-(u-i)H_{r-c}+X(H_c-H_{r-c})\}]
 \pmod{p^2}.
\]
在 \(c=0,\ldots,r\) 求和，\(\sum_c(r-2c)w_c=0\)。以
\(S=\sum_c(r-2c)w_c H_c\) 记剩下的调和和，反射 \(c\leftrightarrow r-c\) 后有
\[
 \sum_{c=0}^r V_{n,ip+c}(X)\equiv
 p\,(\sum_c w_c+4S)(u-2i+2X)W_i(X)\pmod{p^2}.
\]
零接触的 H2 和 Dougall 闭式给 \(\sum_c w_c+4S=(-1)^r\binom{2r}{r}\)。
\((u-2i+2X)W_i(X)=X^4R_u(-i+X)\)，其前三次及常数系数正是小阶数的原 Laurent 系数。

由 \(n+b+1<p^2/2\)，有 \(u+v+1<p\)。对每个 \(e=j+4\) 均可用
\[
 p^e H_{b+k}^{(e)}\equiv H_{\lfloor(b+k)/p\rfloor}^{(e)}\pmod{p^e}.
\]
计算 \(p^8A_{n,b}\) 时，将左边同 \([X^{4-j}]V_{n,k}\) 相乘。无进位且 \(c\le r\) 时，右边是与 \(c\) 无关的 \(H_{v+i}^{(e)}\)。合并上面的区块求和，模 \(p^2\) 计算后除去一个 \(p\)，即得 H5。

有进位 \(r+s\ge p\) 时也能得到最高一层的实际判别。置
\[
 U_{r,s}=\sum_{c=p-s}^r(r-2c)\binom rc^4,\qquad
 P_u(t)=\frac{(u!)^4}{\prod_{i=0}^u(t+i)^4}.
\]
则
\[
 p^8A_{n,b}\equiv-U_{r,s}\frac{P_u^{(4)}(v+1)}{24}\pmod p .   \tag{H6}
\]
确实，模 \(p\) 各区块的低位总和为零。只有 \(c\ge p-s\) 时多出一个调和项 \((v+i+1)^{-j-4}\)，其乘数是 \(U_{r,s}[X^{4-j}]W_i(X)\)。后者的系数来自 \(W_i=X^4P_u(-i+X)\)，对全部 \(i,j\) 代回 \(P_u\) 的四阶导数即得 H6。实数中 \(U_{r,s}<0\)，因为上半截各项负，若截点在中心左边则其互补的下半截总和为正。对每个固定 \(u,v\)，\(P_u^{(4)}(v+1)>0\) 可由分母各因子分别求导看出。有进位的八层由 H6 右端模 \(p\) 的非零性决定。

小阶数的有理项也可完全判零。把 \(R_u=(2t+u)P_u\) 拆为 \(tP_u+(t+u)P_u\)。两项各是 \(4u+3\) 个正倒数因子的积乘常数。四次导数除以 \(24\) 的相对因子是这组倒数的四次完全齐次多项式，从而
\[
 0<R_u^{(4)}(t)/24\le\binom{4u+6}{4}\frac{R_u(t)}{t^4}
 \quad(t\ge1).
\]
因此 \(L_{u,v}>0\)，奇数 \(u\) 时 \(B_u<0\)，故 \(A_{u,v}>0\)。若 \(u\ge2\) 为偶数，利用 \(R_u(t)=(2t+u)/[t\binom{t+u}{u}]^4\)、\(\binom{t+u}{u}\ge u+1\)、\(\zeta(8)<\zeta(7)<7/6\)，得到
\[
 L_{u,v}\le L_{u,0}\le
 \frac{\binom{4u+6}{4}(2\zeta(7)+u\zeta(8))}{(u+1)^4}
 \le\frac{625}{24}\frac76(u+2)<30u(u+1)
 \le30\binom{2u}{u}<B_u\zeta(7).
\]
这里 \(\binom{2u}{u}\ge\binom{2u}{2}\ge u(u+1)\)。因此偶数 \(u\ge2\) 时 \(A_{u,v}<0\)。最后 \(A_{0,v}=-30H_v^{(7)}\)。全部非负整数对中，只有 \(A_{0,0}=0\)。

特别在 \(b=n\) 时，固定 \(u\ge1\)，区间 \(n/(u+1/2)<p\le n/u\) 上的素数满足 \(2r<p\)。当 \(n\) 充分大时，\(p\) 整除固定非零有理数 \(A_{u,u}\) 的分子或分母的可能性消失，故 H5 给 \(v_p(A_{n,n})=-7\)，且 \(p\nmid B_n\)。对任意有限组这样的不交区间用素数定理，再把 \(u\) 的上限送至无穷，即得
\[
 \liminf_{n\to\infty} \frac{\log\operatorname{den}(A_{n,n})}{n}
 \ge7\sum_{u\ge1}\left(\frac{1}{u}-\frac{1}{u+1/2}\right)
 =7(2-2\log2).                                                   \tag{H7}
\]
有限和化为 \(2H_m-2H_{2m+1}+2\)，给出最后的常数。H7 的每个带内素数在本原整数对中保留七层，其他素数处的共同因子还须另计。

对任意固定偶数 \(a\ge2\)，用 \(R_n^{(a)}/a!\) 求和时，反射和总留数只留下 \(\zeta(a+3)\)，其系数为 \(2\binom{a+2}{a}(-1)^n\binom{2n}{n}\)。记有理项为 \(A^{(a)}_{n,b}\)。H5 的区块恒等式不依赖 \(a\)，调和指数 \(j+a\ge3\) 保证同样的模 \(p^2\) 精度。因此在同一无进位条件下，
\[
 p^{a+3}A^{(a)}_{n,b}\equiv(-1)^r\binom{2r}{r}A^{(a)}_{u,v}\pmod p .
\]
在进位条件下，H6 的两边分别换为 \(p^{a+4}A^{(a)}_{n,b}\) 与 \(-U_{r,s}P_u^{(a)}(v+1)/a!\)。这给出适用于全部奇权 \(5,7,\ldots\) 的系数递降。每一权的本原公因数与实处误差仍需在同一无界子列配合。
