# 第290轮独审 · 外带两条反射序列的共同递推

对[本轮缩放铅笔](zeta7_symbol_contact_charter_round290.md)，令 \(p>13,\ 2m<p<4m-1,\ N=(p-1)/2,\ h=N+1-m,\ e=m-h\)。上一轮的低侧反射系数为 \(b_j=(-1/16)^j\binom{2j}j/(2j+1)\)，高侧系数为
\[
 f_j=-{35\over r}\sum_{i=0}^{2j+1}(2i-r){r\choose i}^4,\qquad r=j+1/2.
\]
此处先取有理数，再在合法下标取模。记 \(\beta_k=30(-1)^k\binom{2k}k/k\)，则缩放矩阵的第 \(i,j\) 项是 \(M_\ell,\ \ell=i+j+1-(N+1)\)。\(\ell\ge0\) 时 \(M_\ell=f_\ell\)，\(\ell=-j-1<0\) 时 \(M_\ell=Y\beta_N b_j\)。下文写 \(y=Y\beta_N\)，这个单位因子保持关于 \(Y\) 的零点阶数。[原序列 D7–D9](zeta7_actual_cost_round289.md)

## 实际高侧是 Guillera 级数的截断

置 \(G_j=(\binom{2j}j/16^j)^4,\ P(s)=820s^2+180s+13\)。对 \(j\ge0\) 有
\[
\begin{split}
 &(2j+1)^2 f_j+4(2j-1)(2j)f_{j-1}={35\over16}P(j)G_j,\\
 & f_j={35\over16}{(-1)^j16^j\over (2j+1)^2\binom{2j}j}
      \sum_{k=0}^j(-1)^kP(k){\binom{2k}k^5\over 2^{20k}}.       \tag{S1}
\end{split}
\]
第一式在 \(j=0\) 的第二项取零，给 \(f_0=455/16\)。部分和的无穷极限 \(128/\pi^2\) 是 Guillera 的已证恒等式；这里确定了外带给出的每一个有理系数。[Guillera 原作者给出的等式](https://sites.math.rutgers.edu/~zeilberg/expmath/GuilleraSlides.pdf)

给一个有限差分证书。写 \(F(r,i)=(2i-r)\binom ri^4\)，
\[
 W(r,i)={i^4[-2i^2+6(r+1)i-5(r+1)^2]\over(r+1)^4}\binom{r+1}{i}^4 .
\]
以 \(\Delta_i W=W(r,i+1)-W(r,i)\) 为约定，通分得到
\((r+1)F(r+1,i)+2(2r+1)F(r,i)=\Delta_i W\)。
在 \(0\le i\le2r\) 上求和，给移位的和补足 \(2r+1,2r+2\) 两项。其结果为
\[
 (r+1)^2f_{j+1}+2r(2r+1)f_j
   ={35\over16}(205r^2+250r+77)\binom r{2r+1}^4 .
\]
用 \(\binom r{2r+1}=(-1)^{j+1}\binom{2j+2}{j+1}/16^{j+1}\) 即得 S1 的第一式；乘齐次解的倒数再求和得第二式。

从有限和还可读出既约分母。对 \(i>0\)，
\((2i-r)\binom ri^4/r=2\binom{r-1}{i-1}\binom ri^3-\binom ri^4\)。
半整数二项式是二分有理数，这由 \((1+z)^j(1+z)^{1/2}\) 的系数或广义 Lucas 整性得到。每项的二进阶为 \(-8i+4s_2(i)\)，因为 \(v_2(\binom ri)=-2i+s_2(i)\) 而 \((2i-r)/r\) 是二进单位。这些阶数严格下降，故
\[
                 f_j\in\mathbb Z[1/2],\qquad v_2(f_j)=-16j-4+4s_2(j). \tag{S2}
\]

## 一支正矩的两段支撑

取 \(X=\prod x_i,\ Z=\prod x_i(1-x_i)\)。高侧的精确实表示是
\[
 f_j={280\over\pi^2}\,\frac{(-1)^j16^j}{(2j+1)^2\binom{2j}j}
       +{35\over\pi^4}\int_{(0,1)^4}Z^{j+1/2}
                  {1+x_4\over(1-x_4)(1-X)}\,d^4x.                    \tag{S3}
\]
第一项是 \([-4,0]\) 上的正测度矩，因为
\[
 \frac{1}{(2j+1)^2\binom{2j}j}
   =\int_0^1\int_0^1 [u(1-u)v^2]^j\,du\,dv .
\]
第二项是 \([0,1/256]\) 上的正测度矩。第一项乘低侧的 \(b_j\) 恰得 \(280/[\pi^2(2j+1)^3]\)。

用非终止 Rogers–Dougall 求和，取四个自由参数均为 \(-r\)，得到
\[
 \sum_{i=0}^{\infty}(2i-r)\binom ri^4
  =-{\sin(\pi r)\over\pi}\,\frac{\Gamma(1+2r)}{\Gamma(1+r)^2}.
\]
收敛条件为 \(-2r<1\)。在被截去的 \(i=2r+1+t,\ t\ge0\) 段，有 \(|\binom ri|=\mathrm B(r+1+t,r+1)/\pi\)。令 \(s=r+1+t\)，在四个 Beta 积分之一使用
\((2s+r)\mathrm B(s,r+1)=r[\mathrm B(s+1,r)+\mathrm B(s,r)]\)。
其余三个因子照常展开，对 \(t\) 的正项几何级数求和即得 S3。[Rogers–Dougall 公式及收敛范围](https://dlmf.nist.gov/16.4.E9)

## 半素数端点和全下标 Frobenius 递降

写 \(S_j=\sum_{k=0}^j(-1)^kP(k)\binom{2k}k^5/2^{20k}\)。对素数 \(p\ge5\)，S1 在 \(j=N\) 给
\[
                                S_N\equiv13p^2\pmod {p^5}.               \tag{S4}
\]
事实上 \(f_N/35\) 的原有限和中 \(r=p/2\)。对 \(0<i<p\) 的二项式含一因子 \(p\)，除去 \(r\) 后每项仍含 \(p^3\)。首尾余项给
\(f_N/35\equiv1-3\binom{p/2}p^4\equiv13/16\bmod p^3\)。
这里 \(\binom{p/2}p=\frac12\prod_{i=1}^{p-1}(1-p/(2i))\equiv1/2\bmod p^3\)，可用倒数的一、二阶和分别为 \(0\bmod p^2,\ 0\bmod p\)。
再用 Morley 同余 \((-1)^N\binom{p-1}N\equiv4^{p-1}=16^N\bmod p^3\)，从 S1 解出 \(S_N\) 即成。补足至 \(p-1\) 的各项含 \(p^5\)。这恢复了 Zudilin 列出的第 (26) 条式子；未作该超同余证明的首创性断言。[Zudilin 原文，第 (26) 式与其原文证明范围](https://arxiv.org/abs/0805.2788)

同一有理边界还在全部素数幂层稳定。取 \(p\ge5\)，\(u\) 为任意与 \(p\) 互素的正奇数，\(n_s=(up^s-1)/2\)。对 \(s\ge1\) 有
\[
 \frac{f_{n_s}}{35}\equiv\frac{f_{n_{s-1}}}{35}\pmod {p^{3s}},
 \qquad S_{n_s}\equiv p^2S_{n_{s-1}}\pmod {p^{5s}}.                   \tag{S4a}
\]
在 \(f_{n_s}/35\) 的有限和中设 \(x=up^{s-1}/2\)，二项式上参数是 \(px\)。当 \(p\nmid i\) 时，
\(\binom{px}i=(px/i)\binom{px-1}{i-1}\) 含 \(p^s\)，乘 \((px-2i)/(px)\) 后仍含 \(p^{3s}\)。对 \(i=pt,\ t>0\)，有精确的积
\[
 \binom{px}{pt}\big/\binom xt
 =\prod_{\substack{1\le k<pt\\p\nmid k}}(1-px/k).
\]
当 \(j=v_p(t)\) 时，完整约化剩余类的倒数平方和是 \(0\bmod p^{j+1}\)，由乘一个平方非 1 的单位即可证。配对 \(k,pt-k\) 给倒数和是 \(0\bmod p^{2(j+1)}\)。故上积的一次项含 \(p^{s+2j+2}\)，二次项含 \(p^{2s+j+1}\)，其余含 \(p^{3s}\)。若 \(j<s-1\)，低层的项 \((x-2t)\binom xt^4/x\) 已含 \(p^{3(s-1-j)}\)，乘积误差至少含 \(p^{4s-1-j}\)，从而含 \(p^{3s}\)。若 \(j\ge s-1\)，上积本身即为 \(1\bmod p^{3s}\)，低层因子是 \(p\)-整的。求和并计入 \(t=0\) 得第一式。
由于
\[
 S_{n_s}=\frac{32}{35}(up^s)^2\binom{up^s/2}{up^s} f_{n_s},
\]
再对该端点二项式取 \(t=up^{s-1}\) 用刚才的积，即得第二式。这同时给出一个不依赖 Morley 同余的 S4 证明。它约束 \(2n+1\) 有大素数幂因子的边界；实际单个外带矩阵中的 \(0\le j<e<N\) 仍须使用各自的截断值。

对所有 \(a\ge0,\ 0\le b<p\)，高侧矩的整个下标满足
\[
 f_{ap+b}\equiv
 \begin{cases}
       G_a f_b,& b<N,\\
       f_a,& b=N,\\
       0,& b>N
 \end{cases}\pmod p,\qquad G_{ap+b}\equiv G_aG_b\pmod p.               \tag{S5}
\]
为证第一式，先假设 \(b\ne N\)。设 \(ap+b+1/2=r_0+pr_1,\ 0<r_0<p\)。在 \(i=dp+c,\ 0\le c<p\) 处，广义二项式模 \(p\) 为 \(\binom{r_0}c\binom{r_1}d\)。这是普通 Lucas 定理对 \(p\) 进整数参数取连续极限，也可从 \((1+z)^{r_0}(1+z^p)^{r_1}\) 直接取系数。每个完整低位块都有 \(\sum_c(r_0-2c)\binom{r_0}c^4=0\)。当 \(b>N\) 时 \(r_0=b-N,\ 2r_0<p\)，最后的部分块也覆盖 \(0\le c\le r_0\)，故相消。当 \(b<N\) 时 \(r_0=b+N+1,\ r_1=a-1/2\)，唯一的末块上 \(d=2a,\ c\le2b+1\)；它是 \(f_b\) 乘以 \(\binom{a-1/2}{2a}^4=G_a\)。
当 \(b=N\) 时使用 S2 前的无除法恒等式；\(i\not\equiv0\bmod p\) 的项消失，而 \(i=dp\) 的两种二项式分别化为 \(\binom{a+1/2}d,\ \binom{a-1/2}{d-1}\)。由此得到 \(f_a\)，包括 \(p\mid 2a+1\) 的情形。\(G\) 的式子由中心二项式的 Lucas 定理即得，低位进位时 \(G_b\equiv0\)。

记 \(\mathcal F=\sum f_jz^j,\ \mathcal G=\sum G_jz^j,\ \mathcal F_{<N}=\sum_{j<N}f_jz^j\)。S5 在 \(\mathbb F_p[[z]]\) 中等价于
\[
    \mathcal G=\mathcal G_{\le N}\mathcal G^p,\qquad
    \mathcal F=\mathcal F_{<N}\mathcal G^p+z^N\mathcal F^p .
\]
因而 \(\sqrt z\,\mathcal F\) 的 Artin–Schreier 差为 \(\sqrt z\,\mathcal F_{<N}\mathcal G^p\)。把 S4 模 \(p\) 的截断从上端反射，还给出[上一轮 M6](zeta7_shifted_mellin_round288.md)的整数
\[
 J_j=\frac{(-1)^j}{32(2j+1)\binom{2j}j}
        \sum_{i=0}^j(-1)^i(205i^2+160i+32)\binom{2i}i^5 .              \tag{S6}
\]
对固定 \(j\) 及任意充分大的 \(p\)，用
\(\binom{2(N-i)}{N-i}/16^{N-i}\equiv(-1)^N\binom{2i}i\) 与
\(P(N-i)\equiv4(205i^2+160i+32)\)。由 S4 得 \(S_{N-1-j}\equiv-\sum_{k=N-j}^N(-1)^kP(k)\binom{2k}k^5/2^{20k}\)，将它代入 S1，再用 M6 的 \(f_{N-1-j}\equiv35J_j/(j+1)\) 即得 S6 模 \(p\)。对无穷多个素数成立便给出有理数恒等式。

## 两侧共同的矩递推及空间变量的零点界

令 \(G_k=0\ (k<0)\)。在整个双向下标上有
\[
 (2k+1)^2 M_k+4(2k-1)(2k)M_{k-1}=(35/16)P(k)G_k .                   \tag{S7}
\]
在左半边这是 \(b_{j+1}/b_j=-(2j+1)^2/[8(j+1)(2j+3)]\)。在接缝 \(k=0\) 处左半边系数乘以 \(0\)，不必选择 \(y\)。若 \(\theta=z\,d/dz\)，对应算子可写为
\[
 \mathcal L=[(2\theta+1)+8z(\theta+1)](2\theta+1),\qquad
 [256\theta^4-z(\theta+1/2)^4]\mathcal G=0 .
\]
这给 \((M,\theta M,\mathcal G,\theta\mathcal G,\theta^2\mathcal G,\theta^3\mathcal G)\) 的六维微分系统。取双向系数时 S7 是逐个下标的恒等式；不需要将两支无穷级数放在同一收敛环域。

在整个实际半带 \(0\le j<N\)，\(G_j\) 均为模 \(p\) 单位。故一对相邻的 \(f_{j-1},f_j\) 若同零，则 \(P(j)=0\bmod p\)，这样的起点至多两个。四项不可能同时为零。三项同零需 \(P(j)=P(j+1)=0\)。两者的整系数 resultant 的绝对值为 \(2^8 5^3 7\cdot23\cdot41^2\cdot53\)。对 \(p=23,41,53\) 用 S1 在合法前缀递推，各自的零项下标集合是 \(\{1,4,5,6\},\varnothing,\{16\}\)。因此 \(p>13\) 时，原高侧的三连零恰在 \(p=23\) 的 \(4,5,6\) 处。

一个有限域推论是，对 \(p>41\) 和任意 \(y\in\overline{\mathbb F}_p\)，反射后的整个多项式
\[
 U_{p,y}(z)=z^N\left(\mathcal F_{<N}(z)
                  +y\sum_{j=0}^{N-1} b_j z^{-j-1}\right)
\]
在任何非零普通点 \(z_0\ne256\bmod p\) 的零点重数至多 9。若 \(y=0\)，可降为 7。在 \(z_0=256\) 的界分别为 8 和 6。

为证明统一的 9，S7 给
\[
 \mathcal L(z^{-N}U_{p,y})=(35/16)P(\theta)\mathcal G_{\le N}
                       +y(1-2N)^2b_{N-1} z^{-N}.
\]
上端成立是因为 \(2N+1=0\) 在剩余域中成立，这也消去未列入 \(\mathcal F_{<N}\) 的项。施加 \(\theta+N\) 后仅保留
\(W=S(\theta)\mathcal G_{\le N}\)，略去单位 \(35/16\)，其中
\(S(x)=(x+N)P(x)\)。这是非零次数小于 \(p\) 的多项式，其常数项为 \(13N\ne0\)。
写 \(d=\deg S=3\)，由 \(G_j\) 的相邻项比得
\[
 [256\theta^4 S(\theta-1)-z(\theta+1/2)^4 S(\theta+1)]\,W=0 .
\]
在非零且异于 256 的点，最高 \(4+d=7\) 阶导数系数是单位。若 \(W\) 消失阶为 \(s\ge7\)，最低项的导数系数含 \(s(s-1)\cdots(s-6)\ne0\)，矛盾。故 \(W\) 重数至多 6。作用于原 Laurent 多项式的三个导数至多降低重数 3，得 9。
在 \(z=256\) 写 \(t=z/256-1,\ n=4+d\)。最高两个 \(\theta\) 系数分别为 \(-t\) 和在 \(t=0\) 时的 \(-2d-2\)（先将 \(S\) 首一化并除以 256）。代入 \(t^s\) 的首项给指标因子
\[
        s(s-1)\cdots(s-n+2)(s+d-1).
\]
故 \(s=0,\ldots,n-2\)，或 \(s\equiv1-d\bmod p\)；后者因 \(\deg W\le N\) 排除。得 \(s\le 5\)，原函数的上界为 8。\(y=0\) 时直接取 \(S=P,\ d=2\) 而省去 \(\theta+N\)；同一证明给普通点 7、奇点 6。

该结论也控制完整循环矩阵。在 \(\overline{\mathbb F}_p[z]/(z^p-z_0^p)\) 上以 \(U_{p,y}(z)\) 相乘的核维数等于 \(\min(p,\operatorname{ord}_{z_0}U_{p,y})\)。所以每个非零 \(z_0\) 及每个 \(y\) 的维数都至多 9。原任务取这个系数序列的一块主 Hankel 行列式，所测变量是 \(Y\)。支撑多项式在 \(z\) 中的重数界不能换作该主子式在 \(Y\) 中的重数界。

## 在 \(e\) 与 \(m\) 同阶时完整提取低端核

以 \(V_a\) 为次数小于 \(a\) 的多项式空间，\(B\) 表示全部领系数双线性型。高侧常数型在 \(V_h\) 上对整个 \(V_m\) 为零，在 \(V_m/V_h\) 上给可逆的 \(e\) 阶型 \(D\)。小矩阵 \(B_h\) 的核 \(K\) 的维数为 \(r\)。

当 \(e>\sqrt{2m}+2\) 时，\(B\) 将 \(K\) 与高端 \(V_m/V_h\) 配对成满秩 \(r\)。若 \(r=0\) 结论直接成立。否则记 \(d<h\) 为前一正常阶。若下一正常阶超过 \(m\)，所有 \(d<j\le m\) 都落在同一缺陷区间，在中点的秩亏至少是 \((m-d)/2-1\)。第289轮的 Cauchy–Wronskian 界对所有 \(2j<p\) 都有 \(\operatorname{corank} B_j\le\sqrt{j/2}\)，所以这会给 \(m-d\le\sqrt{2m}+2\)，与 \(m-d>e\) 矛盾。存在 \(h<D'\le m\) 的正常阶后，\(B|_{V_{D'}}\) 非退化，\(K\) 的各向量已经能在该空间上给出线性无关的泛函。[正常阶与核维界 Q1–Q3](zeta7_pencil_structure_round289.md)

在 \(V_h\) 内选 \(B\) 非退化的 \(h-r\) 维补空间。以它作合同消元，提出 \(h-r\) 个 \(Y\) 因子，常数型不受影响。在剩余的高端选 \(r\) 个方向与 \(K\) 完全配对，并取其余 \(e-r\) 个方向为 \(K\) 的 \(B\) 泛函共同消去的空间 \(W\)；此处 \(W\) 指选定高端补空间中的核。沿 \(K\) 的行与列展开，有精确的**线性铅笔恒等式**
\[
              Q_{m,p}(Y)=cY^{h+r}\det(D_W+YB_W),\qquad
              c\in\mathbb F_p^\times,\quad \dim W=e-r.                  \tag{S8}
\]
其中 \(D_W,B_W\) 是两型在 \(W\) 上的限制。因为 \(D\) 在 \(e\) 维高端非退化而 \(W\) 余维 \(r\)，所以
\(\operatorname{corank}D_W\le r\)。剥离的 \(B\) 非退化部分由低端的 \(h-r\) 个方向和 \(r\) 对完全配对的方向组成，故
\(\operatorname{corank}B_W=\operatorname{corank}B_m\le\sqrt{m/2}\)。
具体地，配对块形如 \(\left(\begin{smallmatrix}0&C\\ C^{\mathsf T}&*\end{smallmatrix}\right)\) 且 \(C\) 可逆，\(W\) 只同第二组有交叉项，配对块逆矩阵的右下块是零。这证明了最后的秩等式，也说明 S8 保留了原多项式的所有项。

最高次系数也有一项不涉及有理部分 \(A\) 的反射。\(B_N\) 在 \(i+j=N-1\) 的反对角线上全为单位 \(\beta_N\)，在其后全为零。用反三角 Toeplitz 逆和 Jacobi 主子式公式，可得
\[
 \det B_m\ne0\bmod p\quad\Longleftrightarrow\quad
 \det\big([z^{e+2+i+j}]\,b(z)^{-1}\big)_{0\le i,j<h-1}\ne0\bmod p ,
 \qquad b(z)=\sum_{j\ge0}b_j z^j.                                     \tag{S9}
\]
确实 \((B_N^{-1})_{ij}=\beta_N^{-1}[z^{i+j-(N-1)}]\,b(z)^{-1}\)，而补块从 \(i=j=m\) 开始，\(N-m=h-1\)。涉及的系数至多 \(N-1\)，不触及 \(b_N\) 的素分母。在 \(13<p\le4000\) 的所有合法 \(h\) 中，用正常指标检查得到 142 个奇异 \(B_h\)，其中 142 个对应的 \(B_m\) 均非奇异。这个核对仅用于区别两端的判定。

S8 对任务指定的正比例部分一致适用。令 \(\ell=\lfloor e/16\rfloor\)。当原铅笔从 \(h\) 至 \(h+\ell\) 都消零且 \(\ell\ge r\) 时，必须有 \(\det(D_W+YB_W)\) 在 \(Y=0\) 消失至至少 \(\ell-r+1\) 阶，或恒等于零。两端秩亏均小仍允许某个零特征值有长 Jordan 链。S1–S9 已约束了条目、完整循环矩阵和这个剩余铅笔；尚未证明该主子式的加权坏比例上极限低于 \(1-2\log1024/15\)。
