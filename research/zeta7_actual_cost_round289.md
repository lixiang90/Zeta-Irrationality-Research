# 第289轮独审 · 全阶首一公分母的判别式下界

取[本轮任务](zeta7_polynomial_content_charter_round289.md)的等斜率 \(P_m\)，写 \(b_m=[T^m]P_m\)，\(d_m^*\) 为 \(P_m/b_m\) 的系数公分母。本原化以后的实际整数满足
\[
 \liminf_{m\to\infty}{\log d_m^*\over m^2}
 \ \ge\ {\,\log1024-\log(C/4)-\log C\over3}
           +{2\over3}(1-\log2)
 =2.0523103038\ldots,\qquad C=4+1/256.                    \tag{D1}
\]
这里每一个充分大的阶数都受同一二次界约束。无理性判据要求的上界门槛仍是 \(\log 1024=6.9314718055\ldots\)。D1 的证明直接对整个实际首一多项式取判别式，适用于最高素数带出现任意深度共同整除的情形。

## 两个测度和根的单性

令 \(H=1/256\)，\(\nu\) 为[第288轮 M9](zeta7_shifted_mellin_round288.md)中 \([0,H]\) 上的正测度。令 \(\sigma\) 为 \([-4,0]\) 上的正测度，将 \([0,4]\) 上密度 \(30\tau([x,4])\) 对 \(x\mapsto -x\) 推前，其中 \(\tau\) 是 M9 后的反正弦概率测度。于是 \(\sigma\) 的 Lebesgue 密度至多 \(30\)，两个测度在各自支集内部均有稠密支撑。以 \(G_m(\eta)=(\int t^{i+j}\,d\eta)_{i,j<m}\) 记矩阵，有
\[
 P_m(\zeta(7)+z)=\det(G_m(\nu)-zG_m(\sigma)),\qquad
 |b_m|=\det G_m(\sigma),\qquad \log |b_m|=o(m^2).
\]
第二个矩阵带负号，来自 \(B_k=30(-1)^k\binom{2k}k,\ k=i+j+1\)。两矩阵均严格正定，故相对本征值 \(0<\lambda_1\le\cdots\le\lambda_m\) 都为实数；多项式的根恰为 \(\zeta(7)+\lambda_j\)。

每个本征值为单重。否则可在其至少二维的本征空间内选取非零多项式 \(q\)，次数至多 \(m-2\)。本征方程允许用 \(tq\) 作测试向量，给出
\[
 \int t q(t)^2\,d\nu(t)=\lambda\int t q(t)^2\,d\sigma(t).
\]
左侧严格正，右侧严格负。这里可取实 \(q\)，因为该广义本征问题经正定形式变换后是实对称矩阵。严格单性保证 \(d_m^*P_m/b_m\) 的判别式是非零整数。

## 对根差乘积使用混合矩

记 \(e_s\) 为 \(\lambda_1,\ldots,\lambda_m\) 的第 \(s\) 个基本对称多项式，\(V_m=\prod_{i<j}(\lambda_j-\lambda_i)>0\)。有
\[
 V_m\ \le\ \prod_{j=1}^m \lambda_j^{j-1}
 =\prod_{s=1}^{m-1}\prod_{j=m-s+1}^{m}\lambda_j
 \ \le\ \prod_{s=1}^{m-1}e_s .
\]
根的共同平移不改变根差，因而
\[
      (d_m^*)^{2m-2}V_m^2\in\mathbb Z_{\ge1},
      \qquad (m-1)\log d_m^*\ge-\sum_{s=1}^{m-1}\log e_s.    \tag{D2}
\]

对变量组写 \(\Delta(x)=\prod_{i<j}(x_j-x_i)\)。把 \(\det(G_m(\sigma)+zG_m(\nu))/\det G_m(\sigma)=\prod_{j}(1+z\lambda_j)\) 的两边取 \(z^s\) 系数。由展开两个 Vandermonde 行列式并逐项积分，若 \(t=m-s\)，则
\[
 e_s={1\over s!t!\,|b_m|}
       \int\Delta(x)^2\Delta(y)^2\prod_{i,j}|x_i-y_j|^2
                          \prod_{i=1}^s d\nu(x_i)\prod_{j=1}^t d\sigma(y_j).
\]
在 \(x_i\in[0,H],\,y_j\in[-4,0]\) 上有 \(|x_i-y_j|\le H-y_j\)。先对 \(x\) 积分得 \(\det G_s(\nu)=\mathcal D_s\)，再用 \(v_j=H-y_j\)，扩大积分区间到 \([0,C]\)，得到
\[
 e_s\le{\mathcal D_s\,30^t\over |b_m|}J_t(2s,C),\qquad
 J_t(a,C)={1\over t!}\int_{[0,C]^t}\Delta(v)^2\prod_jv_j^a\,dv_j .
                                                               \tag{D3}
\]
M9 给 \(\log\mathcal D_s=-c s^2+o(s^2),\ c=\log1024\)。相对于 \(m^2\) 的误差在全部 \(0\le s\le m\) 一致是 \(o(m^2)\)，这是将固定有限个 \(s\) 与大 \(s\) 分开即可得的结果。

积分 \(J_t\) 是 Cauchy 行列式，
\[
 J_t(a,C)=C^{t^2+at}\,\frac{\prod_{0\le i<j<t}(j-i)^2}
                                {\prod_{0\le i,j<t}(a+i+j+1)} .
\]
特别 \(\log J_t(0,C)=t^2\log(C/4)+o(t^2)\)，由区间 \([0,C]\) 的首一 Legendre 平方范数也可直接验证。因此
\[
 \log e_s\le
 -cs^2+t^2\log(C/4)+2st\log C
 -\sum_{0\le i,j<t}\log\left(1+{2s\over i+j+1}\right)+o(m^2),           \tag{D4}
\]
误差对 \(s\) 一致。

## 二次常数

把 D4 代回 D2。最后一项的归一化和的极限为
\[
 I=\int_0^1\int_0^{1-x}\int_0^{1-x}
          \log\left(1+{2x\over u+v}\right)\,du\,dv\,dx
   ={2\over3}(1-\log2).
\]
可先排除 \(u+v\le\epsilon\) 后取普通 Riemann 和。遗漏部分在每个 \(s\) 的离散和中至多为
\(\sum_{h\le\epsilon m+1}h\log(1+2m/h)\)；除以 \(m^2\) 的上极限是 \(O(\epsilon^2(1+|\log\epsilon|))\)。连续积分的同一部分满足相同界。
为核积分常数，置 \(F(u)=u^2\log u/2-3u^2/4,\ F(0)=0\)。双重积分展开后，对 \(x\) 的积分化为
\(F(2)-2\int_1^2 F(u)\,du+2\int_0^1F(u)\,du\)，即为上值。其余三个二次项分别使用 \(\int x^2dx=\int(1-x)^2dx=\int2x(1-x)dx=1/3\)，区间均为 \([0,1]\)。由此得 D1。

D1 可与 M12 的全带条件下界逐阶取较大值。直接相加会对同一个 \(d_m^*\) 重复计入。下段则通过判别式本身同时保留实处和有限处的贡献。

## 可与实处合并的实际分母深度

记 \(F_m=d_m^*P_m/b_m\in\mathbb Z[T]\)，其正领系数为 \(d_m^*\)。对最高素数带 \(2m<p<4m-1,\ p>13\)，令 \(u_p=v_p(d_m^*)-v_p(b_m)=v_p(\kappa_m)\)，并置
\[
                         a_p=\lfloor\max(u_p,0)/8\rfloor .
\]
M11 的逐行上界给 \(a_p\le e=2m-(p+1)/2\)。对 \(0\le j\le m\)，\(P_m\) 的 \(T^{m-j}\) 系数中的每个排列表项恰从 \(j\) 个条目取有理常数，其余条目取 \(p\)-整的目标系数。每个有理常数的负赋值至多 8，故
\[
 v_p([T^{m-j}]F_m)\ \ge\ \max(0,u_p-8j)\ \ge\ 8(a_p-j)_+ .
\]
于是实际的整数判别式满足
\[
                  v_p(\operatorname{Disc} F_m)\ge8a_p(a_p-1).               \tag{D5}
\]
这里用到一个一般的判别式整除。对次数 \(m\) 的整系数多项式取倒数多项式；其判别式不变。若倒数多项式的第 \(j\) 个系数被 \(p^{8(a-j)_+}\) 整除，将通用多项式写成 \(\sum_{j=0}^m U_j z^{(a-j)_+}X^j\)。对于代数独立的 \(U_j\)，令 \(z\to0\)，恰有 \(a\) 个根是 \(z\) 阶，其首项系数为 \(\sum_{j=0}^a U_jY^j\) 的互异非零根；其余根趋向 \(\sum_{j=a}^m U_jX^{j-a}\) 的互异非零根。这可由两个方程在简单根处的隐函数定理得到。因此通用的整数判别式多项式被 \(z^{a(a-1)}\) 整除。令 \(z=p^8\) 并专门化 \(U_j\)，就得 D5。\(a=0,1\) 时直接由判别式整性成立。

在 D2 中使用 D5 的整数因子，得实际可加的界
\[
 {\log d_m^*\over m^2}
 \ \ge\ 2.0523103038\ldots+
 {4\over m^2(m-1)}
 \sum_{\substack{2m<p<4m-1\\p>13}}a_p(a_p-1)\log p+o(1),                \tag{D6}
\]
其中常数取 D1 的精确值。若 M11 中较小多项式的内容赋值 \(t_p<8\)，则 \(u_p=8e-t_p\)，所以该项 \(a_p\ge e-1\)。即使 \(t_p\ge8\)，D6 仍按实际剩余的 \(u_p\) 计入。该合并对准一个非零整数判别式，避免重复使用同一首一公分母。D1、D6 均尚未达到 \(\log1024\) 的严格指数门槛。

## 有限域缩放铅笔的反射和截断核

在外带取 \(T_0=(p+1)/2,\ n_0=T_0-1,\ h=T_0-m,\ e=m-h\)。将 \(Y=p^8T\) 代入并清每行的八层，模 \(p\) 的矩阵为
\[
       \begin{pmatrix}Y B_h&YV\\YV^{\mathsf T}&D+YB_e\end{pmatrix}.
\]
末块 \(D_{ij}=f_{i+j-e+1}\)（负下标取零），\(f_0=455/16\ne0\)。设 \(r=\operatorname{corank}B_h\)。在零点的形式幂级数环消去末块，再分离 \(B_h\) 的非退化部分，剩余核上的首项是 \(-Y VD^{-1}V^{\mathsf T}|_{\ker B_h}\)。若此形式非退化，则全部行列式关于 \(Y\) 在零点恰有 \(h+r\) 阶零，给 \(v_p(d_m^*)\ge8(e-r)\)，与较小 \(P_h\) 自己的八层内容无关。

以下公式给这个有限域形式一个独立检验。记 \(\beta_k=30(-1)^k\binom{2k}k/k\)。在可用的区间内有
\[
 {\beta_{n_0-j}\over\beta_{n_0}}
 =\frac{(-1/16)^j}{2j+1}\binom{2j}{j}\pmod p\qquad(0\le j<n_0).
                                                               \tag{D7}
\]
事实上 \(\binom{2k}k\equiv(-4)^k\binom{n_0}k\)，在 \(k=n_0-j\) 处再用二项式反射及 \(n_0\equiv-1/2\pmod p\) 即得。另一方面 M5 在 \(k=T_0+j\) 的首个高区块仅有 \(2j+2\) 项，给
\[
 f_j=-{35\over j+1/2}\sum_{k=0}^{2j+1}
               (2k-j-1/2){j+1/2\choose k}^{\!4}\pmod p,\qquad 0\le j<e .
                                                               \tag{D8}
\]
两式右侧均为与 \(p\) 无关的有理系数序列，分母在各自使用的区间内为单位。

以 \(\mathcal B(t^i)=\beta_{i+1}\) 定义矩泛函。设 \(d<h<D'\) 是包住奇异阶 \(h\) 的相邻正常阶，以 \(q_d\) 为首一的第 \(d\) 阶正交多项式。记 \(\delta=D'-1-h,\ c_i=\mathcal B(t^{h+i}q_d)\)，则首个非零 \(c_i\) 的下标为 \(\delta\)。据正常阶的核描述，\(r=\min(h-d,D'-h)\)，且 \(q_d,tq_d,\ldots,t^{r-1}q_d\) 为核基。若需超出所给数据定义 \(D'\)，可延拓矩序列；下面的有限个矩阵系数只使用原前缀。[正常阶与核](zeta7_pencil_structure_round289.md)

写 \(c(z)=\sum_{i\ge0}c_i z^i,\ f(z)=\sum_{j=0}^{e-1}f_j z^j\)。反转 Hankel 矩阵的行后即为三角 Toeplitz 矩阵，故向量 \(v,w\) 的配对满足 \(v^{\mathsf T}D^{-1}w=[z^{e-1}]v(z)w(z)/f(z)\)。又因 \(\delta\ge r-1\)，上述第 \(a\) 个核向量给 \(z^{-a}c(z)\) 的前 \(e\) 项。因此在该核基中，限制形式的整个矩阵为
\[
 \left([z^{e-1+a+b}]{c(z)^2\over f(z)}\right)_{0\le a,b<r}.              \tag{D9}
\]
若 \(e+r-2<2\delta\)，首行全零，故会退化。若 \(e+r-2=2\delta\)，矩阵沿一条反对角线首现共同的非零数 \(c_\delta^2/f_0\)，故非退化。这是关于正常阶位置的条件判据，未断言外带确实出现该退化位置。

对 \(13<p\le18000\) 的每个素数、每个 \(1\le h\le\lfloor(p-1)/4\rfloor\)，独立按 D9 检查。共有 494 个 \(B_h\) 奇异的外带对，其中 121 个满足 \(p\le3500\)。每一个都满足 \(d=h-1\)，故 \(r=1\)；494 个标量均非零。以首一基计，\((m,p,h,e)=(10,29,5,5)\) 时余数是 17，\((32,103,20,12)\) 时余数是 40。

可按以下步骤复算这段有限检验。用模 \(p\) 中的 \(\beta_1,\ldots,\beta_{n_0}\) 及[现有程序](verify_zeta7_polynomial_content_round289.py)的 \(\texttt{normal_indices}\) 取出奇异 \(h\)。在 \(\sum_{j=0}^{n_0-1}\beta_{j+1}z^{-j-1}\) 的 Laurent 连分数中取次数 \(d\) 的首一分母 \(q_d=\sum u_jt^j\)。逐项置 \(c_i=\sum_{j=0}^du_j\beta_{h+i+j+1}\ (0\le i<e)\)，用 D8 求 \(f\)，以截断多项式逆算 \([z^{e-1}]c^2/f\)。计算还核了 \(\sum_j u_j\beta_{i+j+1}=0\ (0\le i<h)\)。超出可用上端的 \(\beta_k\) 在 \(n_0<k<p\) 均为零。这里的有限范围没有给出无界加权坏比例。
