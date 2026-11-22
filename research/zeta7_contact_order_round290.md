# 第290轮独审 · 外带符号、截断超几何和与零点的提升链

取素数 \(p>13,\ 2m<p<4m-1\)，设 \(N=(p-1)/2,\ h=N+1-m,\ e=m-h\)。矩阵下标从零开始。沿用实际缩放多项式 \(Q_{m,p}(Y)=p^{8m}P_m(Y/p^8)\bmod p\)，本轮关心的是其从 \(h\) 次至 \(h+\lfloor e/16\rfloor\) 次的全部系数。下面给出高端每条反对角线的统一公式，以及在 \(h,e\) 同阶时将连续消零化为一条长度随 \(m\) 增长的链。跨素数的加权比例仍待估计。[任务书](zeta7_symbol_contact_charter_round290.md) · [实际矩的 D7–D9](zeta7_actual_cost_round289.md)

## 高端反对角线与 Guillera 的有限和

在有理数域取 \(n=j+1/2\) 并定义
\[
 f_j=-{35\over n}\sum_{k=0}^{2n}(2k-n){n\choose k}^{\!4}.
\]
对于 \(0\le j<e\)，这正是末块第 \(j\) 条非零反对角线的有理提升。置 \(P(s)=820s^2+180s+13\)，则有全阶等式
\[
 \begin{split}
 U_j&=\sum_{s=0}^j(-1)^s P(s){\binom{2s}s^5\over 2^{20s}},\\
 f_j&={35\over16}\,
 {(-16)^j\over(2j+1)^2\binom{2j}j}\,U_j .                 \tag{C1}
 \end{split}
\]
无穷和为 Guillera 的 \(128/\pi^2\) 恒等式。这里用到有限上限 \(j\)，其与实际矩的等式可直接望远镜求和。[Guillera, *About a New Kind of Ramanujan-Type Series*, 公式 (1-1)](https://plouffe.fr/simon/articles/Citations/About%20a%20New%20Kind%20of%20Ramanujan-Type%20Series.pdf) · [Zudilin, *Quadratic transformations and Guillera’s formulae for \(1/\pi^2\)*, 公式 (2)](https://arxiv.org/pdf/math/0509465)

令 \(W(n,k)=(2k-n)\binom nk^4\)，并令
\[
 Z(n,k)={k^4\over n^4}(-2k^2+6nk-5n^2)\binom nk^4 .
\]
用相邻两项的二项式比值直接通分，得
\[
 nW(n,k)+2(2n-1)W(n-1,k)=Z(n,k+1)-Z(n,k).
\]
对 \(j\ge1\)，从 \(k=0\) 加至 \(2n\)。记 \(t_j=\binom n{2n}=(-1)^j\binom{2j}{j}/(2\cdot16^j)\)。端点为 \(Z(n,2n+1)=-(n^2+2n+2)t_j^4\)。左边的第二个和比 \(f_{j-1}\) 多出 \(k=2n-1,2n\) 两项，该两项之和为 \((51n-15)t_j^4\)。整理有
\[
 n^2 f_j+2(2n-1)(n-1)f_{j-1}
       =35(205n^2-160n+32)t_j^4 .                          \tag{C2}
\]
记 \(H_j=(-16)^j/[(2j+1)^2\binom{2j}j]\)。齐次方程的相邻比恰是 \(H_j/H_{j-1}\)。除以 \(n^2H_j\) 后，非齐次项为 \((35/16)(-1)^jP(j)\binom{2j}j^5/2^{20j}\)。代入 \(f_0=455/16\) 给出 C1。

所有 \(f_j/35\) 均属于 \(\mathbb Z[1/2]\)。实际上 \(k\binom nk/n=\binom{n-1}{k-1}\)，因此每项可用 \(\binom nk^4-2\binom nk^3\binom{n-1}{k-1}\) 表示，\(k=0\) 时第二项取零。半整数幂 \((1+z)^{j+1/2}\) 和 \((1+z)^{j-1/2}\) 的展开系数均属于 \(\mathbb Z[1/2]\)，这也可由平方恒等式逐项递推。因此
\[
 U_j\in (2j+1)^2\binom{2j}j\,\mathbb Z[1/2].               \tag{C3}
\]
二处的既约分母也可求准。令 \(K=2j+1\)。因 \(2k-n\) 和 \(n\) 均为奇数除以 2，两者之比是二进单位，而 \(v_2\binom nk=-k-v_2(k!)\) 对 \(k\) 严格递减。从而 \(k=K\) 是唯一最低项，\(f_j/35\) 的既约分母恰为 \(2^{8K-4s_2(K)}\)，\(s_2\) 表示二进制数位和。

## 奇素数幂处的相容性

对任意正奇数 \(K\)，取素数 \(p\ge5\)，\(r=v_p(K)\ge1\)，并记 \(j(K)=(K-1)/2\)。有
\[
 \begin{split}
 f_{j(K)}/35&\equiv f_{j(K/p)}/35\pmod{p^{3r}},\\
 U_{j(K)}&\equiv p^2U_{j(K/p)}\pmod{p^{5r}} .              \tag{C3a}
 \end{split}
\]
取 \(K=p\) 给出 \(U_{(p-1)/2}\equiv13p^2\bmod p^5\)，以及 \(f_{(p-1)/2}/35\equiv13/16\bmod p^3\)。在这个素数尺度，\(U_{p-1}\) 的额外各项也均有因子 \(p^5\)。Feng 和 Hou 的定理 1.7 式 (12) 为同一全截断和给出模 \(p\) 的消失。此处利用 C1 在半截断上直接证明 C3a，本稿未作全部文献的优先权判定。[Feng–Hou, *Finding congruences with the WZ method*](https://arxiv.org/pdf/2506.19221)

为证明第一式，置 \(x=K/2\)，则 \(f_{j(K)}/35\) 的第 \(k\) 项为 \((1-2k/x)\binom xk^4\)。由 \(k\binom xk=x\binom{x-1}{k-1}\) 和二项式的 \(p\) 进整性，有 \(v_p\binom xk\ge\max(0,r-v_p(k))\)。所以 \(p\nmid k\) 的各项均属于 \(p^{3r}\mathbb Z_p\)。若 \(k>0,\ p\mid k\)，取 \(b=\min(r,v_p(k))\)，正、负号因 \(k-k/p\) 为偶数抵消，从而
\[
 {\binom xk\over\binom{x/p}{k/p}}
  =\prod_{\substack{1\le i<k\\p\nmid i}}(1-x/i)
  \equiv1\pmod {p^{3b}}.                                    \tag{C3b}
\]
确实，配 \(i,k-i\) 后每对为 \(1-x(k-x)/[i(k-i)]\)，其改变量属于 \(p^{2b}\mathbb Z_p\)。单位指标的完全逆平方和模 \(p^b\) 为零，因为这些指标覆盖模 \(p^b\) 的每个单位相同次数，而乘 2 置换单位，\(1-2^{-2}\) 可逆。于是每对取一个代表所得的 \(\sum1/[i(k-i)]\) 也模 \(p^b\) 为零。C3b 随即成立。较低尺度第 \(k/p\) 项的权 \(1-2k/x\) 不变，整项赋值至少 \(3(r-b)\)，乘上四次幂比值所得误差仍有 \(3r\) 层。第零项相等，逐项加和即证。

再置 \(d=(K-1)/2,\ D(K)=\binom{K-1}d/(-16)^d\)，以及
\[
 A_K=\prod_{i=1}^d(1-K/(2i)),\qquad B_K=\prod_{i=1}^d(1-K/i).
\]
分别对奇数乘积和全阶乘计数，得 \(B_K=(-1)^d\binom{K-1}d=4^d A_K\)，故 \(D(K)=A_K^2/B_K\)。在 \(D(K)/D(K/p)\) 中整除 \(p\) 的指标逐一消去，剩下的乘积为
\[
 \prod_{\substack{1\le i\le d\\p\nmid i}}
        \left(1+{K^2\over4i(i-K)}\right)\equiv1\pmod{p^{3r}} .
\]
这里半段的单位逆平方和也模 \(p^r\) 为零，可将全段按 \(i,K-i\) 配对。现在 C1 给出 \(U_{j(K)}=16K^2 D(K)f_{j(K)}/35\)，\(D(K/p)\) 与 \(f_{j(K/p)}/35\) 均为 \(p\) 进整数，故得第二式。对 \(p=5,\ K=5,25,125,625\)，相邻半截断和之差 \(U_{j(K)}-25U_{j(K/5)}\) 的精确赋值依次为 \(5,10,15,20\)。外带矩阵内的实际下标满足 \(2j+1<p\)；C3a 直接控制跨尺度端点。

这给出从另一端计算同一批有理系数的公式。对 \(0\le d<N\)，
\[
 f_{N-1-d}=
 {35(-1)^d\over16(d+1)^2\binom{2d+2}{d+1}}
 \sum_{t=0}^d(-1)^t(205t^2+160t+32)\binom{2t}t^5
 \pmod p .                                                   \tag{C4}
\]
由 \(\binom{2s}s\equiv(-4)^s\binom Ns\)，\(U_j\) 的被加数模 \(p\) 是 \(P(s)2^{-10s}\binom Ns^5\)。在 \(U_N\equiv0\) 中扣掉末 \(d+1\) 项，置 \(s=N-t\)，用 \(2^{10N}=1\pmod p\) 以及 \(P(-1/2-t)=4(205t^2+160t+32)\)。最后代入 \(H_{N-1-d}=(-1)^{d+1}/[4(d+1)^2\binom{2d+2}{d+1}]\pmod p\)，即得 C4。比如从右端第一项得到 \(f_{N-1}=35\pmod p\)。独立用有理数检验了 \(0\le j\le33\) 的逐项望远镜恒等式、C1、C2，并对 \(17\le p\le167\) 的 33 个素数核实了 C4 的全部 1420 个系数。

对实际有限域矩的内部也有统一计数。在 \([0,N-1]\) 中任取连续 \(L\) 个下标。对任意 \(\lambda\in\mathbb F_p\)，
\[
      \#\{j:U_j=\lambda\}\ll 1+L^{2/3}.                     \tag{C4a}
\]
常数绝对。取 \(\lambda=0\) 时，C1 的乘数为单位，故末块长 \(e\) 的实际反对角线中至多 \(O(1+e^{2/3})\) 条消失。

令 \(T_s=(-1)^s\binom{2s}s^5/2^{20s}\)。若 \(U_j=U_{j+q}\)，\(1\le q<N,\ j+q<N\)，则将差除以单位 \(T_{j+1}\)，给出关于 \(X=j\) 的有理函数零点
\[
 P(X+1)+\sum_{i=2}^q P(X+i)
     \prod_{a=2}^{i}{-(X+a-1/2)^5\over1024(X+a)^5}=0 .
\]
以 \(\prod_{a=2}^q(X+a)^5\) 清分母，分子多项式次数至多 \(5(q-1)+2\)，在 \(X=-3/2\) 的值是 \(P(-1/2)=128\) 乘非零的公共分母。由于 \(p>13,\ 2q-3<p\)，该多项式在 \(\mathbb F_p[X]\) 非零。故固定差 \(q\) 时，此区间只有至多 \(5(q-1)+2\) 个可能的左端点。把 \(U_j=\lambda\) 的相邻下标之差分为 \(\le k\) 和 \(>k\) 两种，前者最多 \(\sum_{q=1}^k(5(q-1)+2)\)，后者最多 \(L/k\)。取 \(k=\max(1,\lfloor L^{1/3}\rfloor)\) 即得 C4a。它控制实际条目的消失；行列式仍含许多非零项之间的相加。

## 同一微分算子作用于两侧的系数

记 \(\beta_k=30(-1)^k\binom{2k}k/k\)。低端关于 \(N\) 反射后有 \(g_j=\beta_{N-j}/\beta_N=(-1/16)^j\binom{2j}j/(2j+1)\pmod p\)，\(0\le j<N\)。把全矩阵的列反转，位置 \((i,j)\) 对应 \(k=m+i-j\)，故双向 Laurent 系数以 \(z^h\) 整体平移后可写成
\[
 f(z)+Y\beta_N z^{-1}g(1/z),\qquad f(z)=\sum_{j\ge0}f_jz^j,\quad
 g(z)=\sum_{j\ge0}g_jz^j .                                  \tag{C5}
\]
在这条式子中 \(g_j\) 取给出的有理提升。有限矩阵只用到各自一侧的有限系数。

设 \(\theta=z\,d/dz,\ \mathcal H(z)=\sum_{j\ge0}\binom{2j}j^4z^j/2^{16j}\)，以及
\[
 \mathcal L=[(1+4z)\theta+1/2+4z](\theta+1/2).
\]
逐项比较 C2 和 \(j=0\) 的初值给出
\[
 \mathcal L f={35\over64}P(\theta)\mathcal H,\qquad
 \theta^4\mathcal H={z\over256}(\theta+1/2)^4\mathcal H.     \tag{C6}
\]
另一侧 \((2\theta+1)g=(1+z/4)^{-1/2}\)，因此 \(g(z)=2\operatorname{arsinh}(\sqrt z/2)/\sqrt z\)。直接微分可见 \((\theta+1/2)z^{-1}g(1/z)=-z^{-1/2}/\sqrt{1+4z}\) 选取相容的平方根分支，后者为 \(\mathcal L\) 左因子的解。故 \(z^{-1}g(1/z)\) 和 \(z^{-1/2}\) 均为 \(\mathcal L\) 的齐次解。C6 分别关于零点和无穷远的解析芽成立，C5 的有限系数解释不要求两个级数在同一环域收敛。

## 根链判据与横块的单射性

设 \(\mathcal B(t^i)=\beta_{i+1}\)。将全铅笔写为
\[
 \begin{pmatrix}YB_h & YV\\YV^{\mathsf T}&D+YB_e\end{pmatrix},\qquad
 D_{ij}=f_{i+j-e+1},\quad f_j=0\ (j<0).
\]
其中 \(D\) 可逆，因为其首条反对角线是单位 \(455/16\)。在 \(\mathbb F_p\) 选固定基将 \(B_h\) 写成 \(\operatorname{diag}(B_0,0_r)\)，\(B_0\) 可逆，\(r=\dim\ker B_h\)，并将变换后的 \(V\) 分为 \(V_0,W^{\mathsf T}\)。于是 \(W\) 是实际映射 \(V^{\mathsf T}|_{\ker B_h}\) 的 \(e\times r\) 矩阵。定义
\[
 C=B_e-V_0^{\mathsf T}B_0^{-1}V_0,\quad J=D^{-1}C,\quad U=D^{-1}W,\quad
 M_j=U^{\mathsf T}D J^j U .
\]
因 \(J\) 对 \(D\) 自伴，\(M_j\) 均对称。在 Laurent 级数域先消去 \(YB_0\)，再消去 \(D+YC\)，得
\[
 \begin{split}
 G(Y)&=W^{\mathsf T}(D+YC)^{-1}W=\sum_{j\ge0}(-Y)^j M_j,\\
 Q_{m,p}(Y)&=\kappa\,Y^{h+r}\det(D+YC)\det G(Y),
              \quad \kappa\in\mathbb F_p^\times .             \tag{C7}
 \end{split}
\]
零维行列式取 1。令 \(G\) 在 \(\mathbb F_p[[Y]]\) 的 Smith 指数为 \(\eta_1,\ldots,\eta_r\)，零因子记作 \(+\infty\)。若 \(Q\ne0\)，则
\[
 \operatorname{ord}_{Y=0}Q-h=r+\sum_{i=1}^r\eta_i .         \tag{C8}
\]
出现无穷指数等价于 \(Q\) 为零多项式。长度为 \(\ell\) 的下三角块 Toeplitz 矩阵，行列 \((i,j)\) 放 \((-1)^{i-j}M_{i-j}\)（\(i\ge j\)），其核维数恰为 \(\sum_i\min(\ell,\eta_i)\)，因为它是截断环 \(\mathbb F_p[Y]/Y^\ell\) 上乘 \(G\) 的矩阵。于是 \(\max_i\eta_i\ge\ell\) 等价于存在 \(u_0\ne0,u_1,\ldots,u_{\ell-1}\in\mathbb F_p^r\)，使下列方程同时成立
\[
 z_0=Uu_0,\qquad z_j=Uu_j-Jz_{j-1},\qquad
 W^{\mathsf T}z_j=0 \quad(0\le j<\ell).                    \tag{C9}
\]

对前 \(d\) 个输出就有长度无关的秩估计。设 \(0\le d\le e\)，\(W_{<d}\) 是 \(W\) 的前 \(d\) 行。如果其核维数 \(u\) 为正，置 \(s=\lfloor d/2\rfloor\)，则
\[
             u+s\le\sqrt{(h+s)/2}.                           \tag{C10}
\]
事实上，该核对应一空间 \(\mathcal U\) 的次数 \(<h\) 多项式 \(q\)，其矩 \(\mathcal B(t^i q)\) 在 \(0\le i<h+d\) 均为零。所有 \(t^a q\ (0\le a\le s,\ q\in\mathcal U)\) 属于 \(\ker B_{h+s}\)，因为所用最大矩指数为 \(h+2s-1\le h+d-1\)。\(\mathcal U\) 中可取 \(u\) 个首项次数互异的基向量，再把首项次数最大的一个依次乘 \(t,\ldots,t^s\)，合计取得 \(u+s\) 个线性无关的向量。[Q2–Q3 的 Cauchy 矩阵与 Wronskian 证明](zeta7_pencil_structure_round289.md) 对尺寸 \(H=h+s\) 的此纯 \(\beta\) 矩阵只需 \(2H<p\)，因为节点互异且所有非零分母不超过 \(2H-1\)。这里 \(h+s\le m,\ 2m<p\)，故 \(\dim\ker B_{h+s}\le\sqrt{(h+s)/2}\)。

特别地，只要 \(d=2s\le e,\ 2(s+1)^2>h+s\)，\(W_{<d}\) 已有满列秩。可以取 \(s=\lceil\sqrt h\rceil\)，故 \(h,e\asymp m\) 时，从前 \(O(\sqrt h)\) 行就检测到每个非零核向量，转置映射满射。在这种尺度下 C9 必有 \(z_0\ne0\)。若 \(Q\) 自 \(h\) 次至 \(h+L\) 次全部消零，\(L=\lfloor e/16\rfloor\)，则 \(r\ge1\)，而且
\[
   \max_i\eta_i\ge
       \left\lceil {L+1-r\over r}\right\rceil.               \tag{C11}
\]
在非零多项式分支这由 C8 求平均得到，零多项式分支有无穷指数。结合 \(r\le\sqrt{h/2}\)，在 \(h,e\asymp m\) 时强制至少一条长度为 \(\Omega(\sqrt m)\) 的 C9 链。这里的 \(Y\) 进链与上轮的 \(p\) 进提升对应不同系数环，尚无同方向结论。

## 一维根空间的两种情形及实际算例

若 \(r=1,\ Q\ne0\)，置 \(s=\eta_1\)，则 \(M_0,\ldots,M_{s-1}=0,\ M_s\ne0\)。向量 \(U,JU,\ldots,J^sU\) 一定线性无关。否则第一次依赖给出某个次数 \(b\le s\) 的首一关系，此关系在其后各阶继续成立，使数列 \(M_j\) 由前 \(b\) 项决定，迫使 \(M_s=0\)。由
\[
 (J^aU)^{\mathsf T}D(J^bU)=M_{a+b},\qquad
 (J^aU)^{\mathsf T}C(J^bU)=M_{a+b+1},
\]
其前 \(\lfloor s/2\rfloor\) 个向量张成的子空间同时对 \(C,D\) 全迷向。故 \(r=1\) 的非零多项式若在 \(h\) 以后再消去线性多个系数，则实际矩阵对必须含有线性维数的这种 Krylov 子空间。

若 \(r=1,\ Q=0\)，上述所有 \(M_j\) 为零。整个可达子空间 \(\mathrm{span}\{J^aU:a\ge0\}\) 对 \(C,D\) 全迷向，其维数可能很小。反过来，只须 \(U\) 为 \(J\) 的循环向量就能排除此分支。确实，令 \(K=[U,JU,\ldots,J^{e-1}U]\)，则
\[
       \det(M_{a+b})_{0\le a,b<e}=(\det K)^2\det D .
\]
因此当此行列式非零时，Markov 系数的常系数递推在 \(\mathbb F_p\) 中的最小阶数恰为 \(e\)，由 Cayley–Hamilton 给出上界。

下表直接用实际 \(D,B_m\) 计算。四例皆有 \(\dim\ker B_h=1\)，基按对应多项式首一归一化。补空间取前 \(h-1\) 个标准坐标，均非退化。

| \(p,m,h,e\) | 首批 \(M_j\bmod p\) | \(\det(M_{a+b})\bmod p\) | 最小递推阶 |
|---|---|---:|---:|
| \(29,10,5,5\) | \(17,28,26,8,15\) | 24 | 5 |
| \(103,32,20,12\) | \(40,64,40,61,1,50\) | 23 | 12 |
| \(389,150,45,105\) | \(243,145,255,208,178,238\) | 58 | 105 |
| \(389,132,63,69\) | \(329,261,96,30,274,383\) | 311 | 69 |

复算时，可用[外带矩程序](verify_zeta7_outer_symbol_round289.py)的 \(\mathrm{target\_moments}\) 和 \(\mathrm{pole\_moments}\) 得到两侧矩，解 \(B_{h-1}v=-(\beta_h,\ldots,\beta_{2h-2})^{\mathsf T}\) 取得核基 \((v^{\mathsf T},1)^{\mathsf T}\)，再按 C7 依次乘 \(J\) 并取上述 Gram 行列式。四例的 \(M_0\) 均非零，故 \(\operatorname{ord}_0Q=h+1\)。这说明低阶的 C6 与 \(Y\) 中的最小递推阶可以相差至少到 105。全阶 C1、C7 与 C10 尚未给出 \(\operatorname{ord}_0Q-h=o(e)\)，也未给出任务书要求的 \(7.5803759\ldots\%\) 加权上界。
