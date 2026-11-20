# 第283轮 · 每个奇权的 Markov 余项、分母与素数降阶

2026-11-20。对任意固定的奇数 \(w\ge3\)，只假设 \(\zeta(w)=u/v\)，其中 \((u,v)=1,\ v>0\)。取 \(\tau_w=\eta(w)=(1-2^{1-w})\zeta(w)\)。若 \(r_s=a_s/c_s\) 既约，\(E_s=\tau_w-r_s>0\)，则反证下 \(2^{w-1}vc_s E_s\) 为正整数。本文的 \(s\) 是逼近阶，所有极限先固定 \(w\)。[本轮任务](odd_weight_family_scope_round283.md)

## 每个权重的真实逼近

令
\[
d\mu_w(x)=\frac{(-\log x)^{w-1}}{(w-1)!}\,dx,\quad
\mu_j=\int_0^1 x^j\,d\mu_w=(j+1)^{-w},\quad
\tau_w=\int_0^1\frac{d\mu_w(x)}{1+x}.
\]
矩公式由 \(x=e^{-t}\) 得到。最后一式将 \((1+x)^{-1}\) 按几何部分和积分，得到交错级数。质量为 1。取首一正交多项式 \(P_s\)，以及
\[
b_i=\mu_i,\quad K_{ij}=\mu_{i+j}+\mu_{i+j+1}\ (0\le i,j<s),\qquad r_s=b^tK^{-1}b .
\]
正密度使 \(K\) 正定。写 \(W=(1-P_s/P_s(-1))/(1+x)\)，正交性给 \(K\,\mathrm{coeff}(W)=b\)。在 \(d\sigma=d\mu_w/(1+x)\) 下将平方展开，得到
\[
E_s=\frac{\int P_s^2\,d\sigma}{P_s(-1)^2}
=\min_{\deg P\le s,\ P(-1)=1}\int P^2d\sigma>0 .
\tag{W1}
\]
设 \(\rho=3+2\sqrt2\)。取 \(P=T_s(2x-1)/T_s(-3)\)，得 \(E_s\le4\rho^{-2s}\)。反向固定 \(I=[\epsilon,1-\epsilon]\)、\(\ell=1-2\epsilon\)，其上 \(d\sigma/dx\ge c_{w,\epsilon}>0\)。该区间的正交 Legendre 基在 \(-1\) 处点值平方和至多 \((s+1)^2\rho_\epsilon^{2s}/\ell\)，\(\rho_\epsilon=(3+\sqrt{9-\ell^2})/\ell\)。这是由 \(|\mathsf P_j(y)|\le(|y|+\sqrt{y^2-1})^j\)（\(|y|\ge1\)）在 \(y=-3/\ell\) 处得到。由 Cauchy–Schwarz 下界并令 \(\epsilon\downarrow0\)，有
\[
\lim_{s\to\infty}\frac{\log E_s}{s}=-2\log\rho .
\tag{W2}
\]
因此每个权重的严格负线性判据都是在同一无界子列取得 \(\log c_s\le(2\log\rho-\delta_w)s\)，其中 \(\delta_w>0\)。此前已有单测度的正性、余项与权七的 Schur 公式。[旧 Markov 稿 §1–4](markov_source_review_round275.md) · [Legendre 夹逼的详细证明](full_net_gate_round281.md)

## 全部子式的共同整除

写 \(l_n=\operatorname{lcm}(1,\ldots,n)\)，\(\Lambda=l_{2s}^w\)。令 \(d_k\) 为 \((\Lambda/(i+j+1)^w)_{0\le i<s,\,0\le j\le s}\) 删去第 \(k\) 列的最大子式。因 \(d_s>0\)，有
\[
P_s(t)=d_s^{-1}\sum_{k=0}^s(-1)^{s-k}d_k t^k .
\]
该首一多项式的正交性是矩阵的余子式关系。正测度使它有 \(s\) 个互异的 \((0,1)\) 内零点，否则乘上所有内部变号零点的一次因子之积会得到定号且积分非零的函数，违反正交。故各 \(d_k>0\)。定义
\[
g_s=\gcd_{0\le k\le s} d_k,\quad e_{s,k}=d_k/g_s,\quad B_s=\sum_k e_{s,k},\qquad
z_k=\sum_{j=1}^k\frac{(-1)^{j-1}}{j^w},\quad z_0=0 .
\]
由 \(P_s(t)/P_s(-1)=\sum e_{s,k}(-t)^k/B_s\) 并对 \(W\) 积分，可得 \(r_s=\sum z_k e_{s,k}/B_s\)。相邻列合并给 \(\det(\Lambda K)=\sum d_k\)，因此同一整数对为
\[
H=\Lambda\sum d_k=\Lambda^{s+1}\det K,\qquad N=\sum(\Lambda z_k)d_k,\quad c_s=H/\gcd(H,N).
\tag{W3}
\]

对每个素数幂 \(q=p^a\le2s\)，令 \(r=s\bmod q,\ h_q=\min(r,q-1-r)\)。在行列式的一个排列项中，免付该层 \(p^w\) 的位置恰有 \(j\equiv-1-i\bmod q\)。写 \(s=tq+r\)，行的额外 \(r\) 个副本需要列余类 \([q-r,q-1]\)，全部 \(s+1\) 个列的额外副本只在 \([0,r]\)。有 \(h_q\) 个需求落在后一区间外，故任何删列、任何排列至少出现 \(h_q\) 次缺失。该层的最佳位置匹配数由各余类人数的逐类最小值给出。把每个排列的各个素数幂层相加，得到
\[
J_{w,s}=\prod_{p^a\le2s}p^{w h_{p^a}}\ \bigm|\ d_k\quad (0\le k\le s).
\tag{W4}
\]
写 \(\|y\|\) 为到最近整数的距离。\(h_p=p\|s/p\|+O(1)\)，高幂 \(a\ge2\) 合计至多 \(O_w(s^{3/2}\log^2s)\)。在 \([\epsilon s,2s]\) 按素数定理分部求和，剩余 \(p<\epsilon s\) 部分由 \(h_p\le p\) 给出 \(O_w(\epsilon^2s^2)\) 的上界。于是
\[
\lim\frac{\log J_{w,s}}{s^2}
=w\int_0^2 x\|1/x\|\,dx=2w(1-\log2).
\]
第二式令 \(y=1/x\) 后按半整数分段积分，得到 \(1+\sum_{k\ge1}(-1)^k(1/k-1/(k+1))=2-2\log2\)。在 \((1+x)d\mu_w\) 的单项式 Gram 矩阵 \(K\) 上，移位首一 Chebyshev 上界及任一紧内区间的首一 Legendre 下界给 \(\log\det K/s^2\to-\log4\)。分母 \(\log\Lambda/s\to2w\)，故
\[
\boxed{\lim_{s\to\infty}\frac1{s^2}\log\frac{H}{J_{w,s}}=2(w-1)\log2,\qquad c_s\le H/J_{w,s}.}
\tag{W5}
\]
权七的显式剩余分母二次系数为 \(12\log2\)。此单余类计数覆盖全部素数幂，与导子为八时的两类匹配不同。[两余类的旧证书](chi8_markov_minors_round282.md) · [实处 Gram 范数夹逼](chi8_markov_content_round282.md)

## 除尽余子式公因子之后的线性障碍

令 \(D=l_s^w\)。它是所有 \(z_0,\ldots,z_s\) 的最小共同分母，因为 \(z_k-z_{k-1}=(-1)^{k-1}/k^w\)。以本原的 \(e_{s,k}\) 构造整数
\[
H'=D B_s,\qquad N'=D\sum_k z_k e_{s,k},\qquad
c_s=H'/\gcd(H',N').
\]
令 \(m_w=(\log2)^{w-1}/(w-1)!\) 及 \(h_s=\int P_s^2d\mu_w\)。在 \([0,1/2]\) 密度至少为 \(m_w\)，此区间上 Legendre 基在 0 处点值平方和等于 \(2(s+1)^2\)。所以 \(|P_s(0)|\le\sqrt{2/m_w}(s+1)\sqrt{h_s}\)。W1 给 \(|P_s(-1)|\ge\sqrt{h_s/(2E_s)}\)，而 \(e_{s,0}\ge1\)。故
\[
B_s\ge\frac{B_s}{e_{s,0}}=\frac{|P_s(-1)|}{|P_s(0)|}
\ge \frac{\sqrt{m_w}\,\rho^s}{4(s+1)} .
\tag{W6}
\]
即便已除尽所有最大子式的共同内容（包括节点 Vandermonde），这个完整清头规范的分母仍满足 \(\liminf s^{-1}\log H'\ge w+\log\rho\)。要达到 W2 的严格判据，两最终坐标之间的 \(\gcd(H',N')\) 必须在同一子列取得至少 \(w-\log\rho+\delta_w\) 的线性对数率。

## 大素数把最终标量降到一个固定小阶

对固定 \(w,h\ge1\)，取 \(h=\lfloor s/p\rfloor\) 的大奇素数 \(p\)。以下有限例外仅依赖 \(w,h\)。写 \(s=hp+r,\ 0\le r<p\)。对每个余类 \(0\le j<p\)，在正交式中取行 \(i=p-1-j+ap\)，乘 \(p^w\) 并按 \(p^w\) 在 \(\mathbb Z_{(p)}\) 中化简。唯有列 \(k=j+bp\) 的项留下，从而
\[
\sum_{b}\frac{(-1)^b e_{s,j+bp}}{(a+b+1)^w}\equiv0\pmod{p^w}.
\tag{W7}
\]
此处 \((-1)^j\) 已约去。行数为 \(h+\mathbf1_{j\ge p-r}\)，列数为 \(h+\mathbf1_{j\le r}\)，各从 \(a,b=0\) 起。取 \(p>2h+2\)，所有显示的小分母皆为单位。当列数不大于行数时，前面的方块是阶 \(h\) 或 \(h+1\) 的正定矩 Gram 矩阵乘交错列符号。除其非零有理行列式的有限坏素数后，该块向量为零模 \(p^w\)。当列比行多一时，矩阵是同一 \(w\) 的阶 \(h\) 矩阵。前 \(h\) 列可逆，其核由本原余子式向量生成。故存在 \(t_j\in\mathbb Z_{(p)}\) 使
\[
e_{s,j+bp}\equiv t_j e_{h,b}\pmod{p^w}\quad(0\le b\le h).
\]
后一种余类称为有自由参数的类。取 \(t=\sum t_j\)，求和得 \(B_s\equiv tB_h\bmod p^w\)。又因 \(p\) 为奇数，前缀中恰有 \(p,2p,\ldots,bp\) 可保留，故 \(p^w z_{j+bp}\equiv z_b\bmod p^w\)。在固定正数 \(r_h\) 的分子、分母与固定 \(B_h\) 所涉的有限素数之外，得到
\[
p^w\sum_k z_k e_{s,k}\equiv t\sum_{b=0}^h z_b e_{h,b}
\equiv r_h B_s\pmod{p^w},\qquad v_p(r_h)=0.
\tag{W8}
\]
特别地，若 \(v_p(B_s)<w\)，两边赋值同为 \(v_p(B_s)\)，除以 \(B_s\) 给出对实际既约分母的等式
\[
\boxed{p^w\nmid B_s\quad\Longrightarrow\quad v_p(c_s)=w.}
\tag{W9}
\]
有自由参数的 \(j\) 恰满足 \(j\le r,\ j<p-r\)。在 \(s=hp\) 或 \(s=(h+1)p-1\) 时只剩 \(j=0\)。本原性 \(\gcd_k e_{s,k}=1\) 迫使 \(t_0\) 为单位，故这两类无限尺度无条件有 \(v_p(c_s)=w\)。每次只给 \(w\log p\) 的对数费用。第275轮研究了 \(s<p<2s\) 的另一极层和可逆残块，在 \(s=p-1\) 可得到 \(p\)-整。W7 的整数商则满足 \(h\ge1\)。

设 \(\Theta_{w,s}=\sum_{p\le s,\ p^w\mid B_s}\log p\)。固定 \(K\ge1\) 后，W9 覆盖 \(s/(K+1)<p\le s\) 中的所有充分大素数。于是
\[
\log c_s+w\Theta_{w,s}\ \ge\
w\!\!\sum_{s/(K+1)<p\le s}\log p
=w\bigl(K/(K+1)+o_K(1)\bigr)s .
\]
先 \(s\to\infty\)，再 \(K\to\infty\)，得 \(\liminf_s(\log c_s+w\Theta_{w,s})/s\ge w\)。因此 W2 的任何成功子列必须满足
\[
\liminf\frac{\Theta_{w,s}}s\ \ge\
1-\frac{2\log\rho-\delta_w}{w}.
\tag{W10}
\]
在 \(w=7\)，必须有超过 \(49.63\%\) 的素数对数重量来自 \(p^7\mid B_s\)。这是本原整数 \(B_s\) 的可证伪条件。满足该条件后，还需核这些素数处的实际消去、其余素数和全部线性预算。权七的具体停止条件是证明 \(\limsup_s\Theta_{7,s}/s\le1-2\log\rho/7\)。若该式成立，W10 将排除本族的严格线性判据。

## 权一校准及证据范围

\(w=1\) 时 \(\tau_1=\log2\)。对 Lebesgue 测度作 \(s\) 次分部积分，移位 Rodrigues 多项式 \((d/dx)^s[x^s(1-x)^s]/s!\) 给出 \(e_{s,k}=\binom sk\binom{s+k}{k}\)，其常数系数为 1，故已本原。于是
\[
B_s=[y^s](1+y)^s(2+y)^s\le
\left(\frac{(1+\sqrt2)(2+\sqrt2)}{\sqrt2}\right)^s=\rho^s .
\]
这时 \(\log H'/s\le1+\log\rho+o(1)<2\log\rho\)，确实能复得已知的 \(\log2\) 无理性。这也说明 W5 在 \(w=1\) 的零二次系数和真正的线性证明之间还需要哪些信息。对 \(w\ge3\)，W6 给出的另一方向的界使单靠约去余子式公因子的办法在该清头规范中达不到所需线性率。本文新核的是单余类全权匹配、W6 的原始整数下界和 W7–10 的标量局部结论。没有对所有奇权得到新的无理性定理，也未审查这些结构结果的全球首创性。[Rodrigues 公式](https://dlmf.nist.gov/18.5#ii) · [项目旧纯值与单测度来源](markov_source_review_round275.md)

Koecher 稿作者另从本原核向量独立复核了本文 W7–W10 的模数、两端余类与素数定理极限。本文作者独立复核 Koecher 稿 K1–K8。特别在 K6 中，若 \(j=j'p+p-b-1,\ n=Ap+b\)，则 \(2n+j+1=(2A+j'+1)p+b\)，所需阶乘比恰含一个 \(p\)，去掉该 \(p\) 后的 Wilson 符号是 \((-1)^b\)，抵消 \((-1)^n\) 中的低位符号。未命中该类时分母赋值至多 \(2+2h=w-1\)。小阶端点正性、无界 \(n\) 和有界 \(n\) 的同号尾以及多项式损失分别核过，K8 适用于原 WZ 对的全部格端点。[Koecher 稿 K1–K8](odd_generating_family_round283.md) · [一手公式 (1) 及 §2](https://arxiv.org/pdf/0801.1591v2#page=2)

## 全格双线性整性的锐成本

保持上述 \(d\mu_w\)。对 \(\mathbb Z[x]_{<d}\) 定义有理对称双线性形
\[
\mathcal B(P,Q)=\int_0^1
\frac{P(x)Q(x)-P(-1)Q(-1)}{1+x}\,d\mu_w.
\]
令 \(I(d,w)\) 为满足 \(\mathcal B(L,L)\subset\mathbb Z\) 的满格的最小指数。它存在，因为足够大的整倍数格满足条件。对任意固定整数 \(w\ge1\)，有
\[
\boxed{\lim_{d\to\infty}\frac{\log I(d,w)}{d^2}=w\log2.}
\tag{W11}
\]

单项式基的矩阵是 \(\mathcal B_{ij}=(-1)^{i+j-1}z_{i+j}\)（\(z_0=0\)）。以对角符号共轭后为 \(-z_{i+j}\)。先看 \(d<p\le2d-2\) 的奇素数。乘 \(p^w\) 后按 \(p^w\) 化简，唯一可能贡献的是前缀项 \(1/p^w\)。尾部索引 \(p-d+1,\ldots,d-1\) 给阶 \(2d-1-p\) 的单位反三角块，其余全零。尾块的阶为偶数。

以下同时处理所有增长素数。固定 \(\epsilon>0\)，取 \(\epsilon d<p\le2d-2\)，\(d\) 充分大时 \(p^2>2d\)。在 \(R=\mathbb Z/p^w\mathbb Z\) 对整的 \(C=p^w\mathcal B\)（在 \(p\) 处取整）作上述符号共轭并将相邻行相减，保留一行恢复原矩阵。所得 \(s=d-1\) 行的矩阵再乘行列符号，恰为 \(p^w/(i+j+1)^w\) 模 \(p^w\)。它按 \(j\equiv-1-i\bmod p\) 分成不相交矩形块。各块是 \(((a+b+1)^{-w})\) 从 \(a=b=0\) 起的连续行列。大小只依赖 \(1/\epsilon\) 的上界，每块含满秩方形首子式，其行列式是固定非零有理数，所以对所有充分大 \(p\) 为单位。按 W4 的逐类人数，在 \(R\) 上有两侧可逆变换把这 \(s\) 行化成 \(t_p\) 个单位及零，
\[
t_p=s-\min(s\bmod p,\ p-1-(s\bmod p)).
\tag{W12}
\]
补回最后一行后，原对称形有至少 \(t_p\) 个单位 Smith 因子，除这批之外至多再有一个非零因子（把该行的前 \(t_p\) 个系数消去，余下仅一行）。

对 \(V=R^d\) 及完全各向同性子群 \(U\)，令 \(K_0=\{v\in V:C(v,V)=0\}\)。由 \(V/K_0\) 上的完美有限配对，\(|U|^2\le |V||K_0|\)，而 \(|K_0|\le p^{w(d-t_p)}\)。故 \(\mathcal B(L,L)\subset\mathbb Z\) 强制 \(v_p([\mathbb Z^d:L])\ge wt_p/2\)。

反向也有局部指数至多 \(p^{wt_p/2+O_w(1)}\) 的全各向同性子群。以下给出存在证明。奇 \(p\) 处可用同余变换令对称形对角化。取一个赋值最小的系数，若它在非对角而所有对角的赋值更大，则取这两个基向量之和，借 \(2\) 为单位得到同赋值的对角主元。以此消去主元所在行、列，归纳完成。由 W12，单位对角部分的秩至多 \(t_p+1\)，其余至多一个非零坐标。每个单位对角部分在去除双曲平面后最多留下两维。为证此点，在维数至少三时，非零模 \(p\) 对角元 \(a,b,c\) 给方程 \(a x^2+b y^2=-c\)，两个平方值集各有 \((p+1)/2\) 个元素，故有解。向量 \((x,y,1)\) 在第三坐标的一阶导数 \(2c\) 为单位，可逐次调整该坐标升至模 \(p^w\) 的原始零向量。配上与其内积为 1 的向量，从后者减去其自配对的一半乘前者，得到双曲平面，直和分出并归纳。每个双曲平面保留一条轴的指数为 \(p^w\)。剩余的至多三维分别取 \(p^{\lceil w/2\rceil}\) 倍数，零坐标可全部保留，得所述上界。

重量计算用 W4 的同一积分，
\[
\lim_{d\to\infty}d^{-2}\sum_{\epsilon d<p\le2d-2}t_p\log p
=\int_\epsilon^2 (1-x\|1/x\|)\,dx .
\]
右侧在 \(\epsilon\downarrow0\) 时为 \(2\log2\)。对 \(p\le\epsilon d\)，令 \(a_p=\lfloor\log_p(2d-2)\rfloor\)，直接将每个坐标乘 \(p^{\lceil w a_p/2\rceil}\) 即使该处整性成立。这批局部指数对数之和至多 \(O_w(\epsilon d^2)+o_w(d^2)\)，因为 \(a_p\ge2\) 的额外层总素数重量为 \(O(\sqrt d\log^2d)\)。对大 \(p\) 的 \(O_w(1)\log p\) 误差之和为 \(O_w(d)\)。各有限模数互素，用中国剩余定理取局部格原像之交，所得全局指数为局部指数的乘积。上下界先令 \(d\to\infty\)，再令 \(\epsilon\downarrow0\)，即得 W11。

实椭球范数 \(\|P\|_\sigma^2=\int P^2\,d\mu_w/(1+x)\) 的 Gram 行列式对数率为 \(-\log4\)，由 W5 使用的首一范数夹逼得到。Minkowski 凸体定理对满格给出的平方最短向量上界为 \(4\,\mathrm{vol}(\mathbb B^d)^{-2/d}[\mathbb Z^d:L]^{2/d}(\det \mathrm{Gram})^{1/d}\)。在指数最小的全整格上，该上界的对数除以 \(d\) 趋于 \(2(w-1)\log2\)。对 \(w\ge3\) 它不足以逼出趋零的整数。这项结论约束全格整性和平均体积界，仍容许超出平均保证的短向量和单个满足自配对条件的多项式。

## 单个多项式能同时消去一整段大素数

取 \(P_i=x^d(1-x)^d x^i\)（\(0\le i<d\)）并令 \(P=x^d(1-x)^d U,\ U=\sum_{i<d}u_i x^i,\ u_{d-1}=1\)。当 \(5d-1\le p\le6d-2\) 为素数，清理 \(\mathcal B(P,P)\) 中的 \(p^w\) 只需其被积多项式的 \(x^{p-1}\) 系数模 \(p^w\) 为零，因所涉各矩分母底数都不超过 \(6d-2<2p\)。两项 \(P_i,P_j\) 的对应系数在 \(4d+i+j<p\) 时为零，等号时为 1（被积多项式的次数为 \(4d+i+j-1\)，首项系数为 1）。置 \(j_p=p-5d+1\)。此索引非负且严格小于 \(d-1\)，因为 \(6d-2\) 是合数。所求同余中恰有 \(2u_{j_p}u_{d-1}=2u_{j_p}\)，余项全属更高指标。不同素数给互异索引。其他坐标先置零，逐 \(p\) 从大到小取代表解，一个坐标只解一个模 \(p^w\) 的线性式。

可以同时保证 \(u_0\ne0,\ U(-1)\) 为奇数，且 \(\max|u_i|\le2(6d)^w\)。当 \(d\ge2\) 时，每个需解同余的坐标都选绝对值不超过 \(p^w\) 的偶数代表，模数为奇数故可行。若此规则给出 \(u_0=0\)，取同余的 \(2p^w\)。若 \(u_0\) 无约束，取 2。其余未用坐标为零，最高次系数为 1，故 \(U(-1)\) 为奇数。当 \(d=1\) 时直接取 \(U=1\)。由此得到同一整系数线性形式
\[
\Lambda'_d \|P\|_\sigma^2
=\Lambda'_d P(-1)^2\tau_w+\Lambda'_d\mathcal B(P,P),\qquad
\Lambda'_d=l_{6d-2}^w\Big/\!\!\prod_{5d-1\le p\le6d-2}p^w ,
\tag{W13}
\]
其中两有理系数均为整数，目标系数非零。

上述规范还有精确实率。上界由 \(|x(1-x)|\le1/4\)、\(\sup_{|z|\le1}|U(z)|=:M\le2d(6d)^w\) 立得。下界取任意 \(x_0<1/2\) 接近 \(1/2\)，在 \((0,1/2)\) 中取以 \(x_0\) 为中心的非退化闭区间 \(I\)。以它的端点为焦点，选半长轴介于 \(x_0\) 与 \(1-x_0\) 之间的椭圆，这使椭圆包含 0 且整体在单位圆内。记 Bernstein 椭圆参数为 \(R>1\)，点 0 的外点参数为 \(1<R_0<R\)。\(U\) 在 \(I\) 的 Chebyshev 系数同时受 \(2\sup_I|U|\) 和 \(2M R^{-k}\) 控制，分别由余弦正交和 Joukowski 代换后的圆周 Laurent 系数界得到。在点 0 求和，因第 \(k\) 项的基函数不超过 \(R_0^k\)，从 \(n=C_I\log(2M)\) 之后的尾绝对值至多 \(1/2\)（常数取得充分大，\(n\) 取整）。\(|U(0)|\ge1\) 于是给 \(\sup_I|U|\ge c_I(2M)^{-C'_I}\)。区间点值的 Legendre 范数估计进一步给 \(\int_I U^2 dx\ge |I|\,(\sup_I|U|)^2/d^2\)。对固定 \(w,I\) 这些损失仅为多项式，且密度在 \(I\) 上有正下界。让 \(I\) 从左侧趋近 \(1/2\) 即得
\[
\lim_{d\to\infty}\frac{\log\|P\|_\sigma^2}{d}=-\log16,\qquad
\boxed{\lim_{d\to\infty}\frac{\log(\Lambda'_d\|P\|_\sigma^2)}d=5w-\log16.}
\tag{W14}
\]
后式用素数定理计整段信用 \(w d+o_w(d)\)。这是 W13 指定输出的真实净率。其两整数系数若还有巨大的共同因子，既约后可能有不同净率。该选择在原全段费用上确有节省，同时较低次数的单项式 \(x^d(1-x)^d\) 已有 \(l_{4d}^w\) 的安全清整。这项发现支付的是同一高次数向量的一整段大素数，尚未给足本原分母的严格衰减。
