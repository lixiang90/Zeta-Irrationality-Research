# Catalan 新论文的实数处证明：两分支 Hardy 插值、统一能量与严格差额

2026-10-07，解读者 /root/scaled_root_finalize。此文是用户新任务的只读论文解读。原 ζ/L 研究明确暂停；没有继续旧轮 map／receipt、冻结旧研究或执行任何数学 producer／Lean。本地原仓库只读，本文另存于当前 workspace。

原件：[Catalan's constant is irrational](E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)，OpenAI，2026-09-24；44页、574388 bytes，SHA4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e。

当前实际 FULL PDF1–5、18–19、25–42，共25 distinct pages；完整读取 build/sections/real-place.tex、energy.tex、certificate.tex、conclusion.tex，及README。四份章节与PDF对应式已对照。最初组合读取的energy/certificate输出发生截断，随后分别完整重读，不以截断输出冒认FULL。没有完整审计PDF6–17、20–24的全部有限处／非零证明，也没有重算证书的整数符号与50个有理区间数值；以下区分论文结论、纸面公式核对与未执行的认证。

## 1. 矛盾发生在同一个 n² 账本

Theorem1.1声称 Catalan 常数 \(G=\beta(2)=L(2,\chi_{-4})\) 无理。论证不是证明一组 rational approximants 的 quotient 收敛，而是构造大小 \(n=48N\) 的同一行列式 \(\Delta_N\)，比较
\[
 L_N=\frac{\log|\Delta_N|}{n^2}-\frac12\log2.              \tag{C1}
\]
矩阵 entries 原本含 \(1,G,\zeta(2)\)。特制整数 Chebyshev rows 的 Taylor contact消掉每一个 entry 的 \(\zeta(2)\) 项，故唯一假设 \(G\in\mathbb Q\) 使整个 \(\Delta_N\) rational。

论文 Proposition3.4的有限处 lower及Proposition4.1的prime-scale非零给
\[
 \liminf_{\substack{p\to\infty\\p\ {\rm prime}}}L_p
 \ge-\frac{8609}{4608}-\frac{2809}{4608}\log2
 >-2.29084.                                             \tag{C2}
\]
这里 odd-prime cost为 \(8609n^2/4608\)，2-adic valuation lower为 \(-505n^2/4608-o(n^2)\)；再支付C1的 \(-\tfrac12\log2\)，产生2809而非505。不能拿未规范化的实数上界与规范化后的有限处下界比较。

Proposition7.1不需rationality假设，证明
\[
 \limsup_{N\to\infty}L_N\le-2.290939875.                   \tag{C3}
\]
它与C2的保证差额大于 \(0.000099875\)；若只使用论文的粗阈值 \(-2.2909\)，保证差额为 \(0.00006\)。差额很小，端点或对角漏掉一个看似有限的费用就可能破坏证明。

非零不能从signed determinant的正性获得。本文只读了Proposition4.1的陈述和fixed-matrix接口：论文在N=p用Frobenius和palindromic bases降到三个固定48×48 rational matrices，最后得 \(v_p(\Delta_p)=-96p\)。该完整非零证书由其他章节承担；当前解读不冒认已独立重现它。

## 2. 两张分支如何进入同一真实行列式

PDF4–5给参数
\[
 a=11N,\ b=7N,\ q=g=4N,\ h=2N,\quad
 C=63N,\quad H=65N,\quad L=59N.
\]
令 \(f=\sqrt{1-t^2}\)、\(w=t/(1+f)\)，near/far involution是 \(w\leftrightarrow w^{-1}\)。真正整数 rows由
\[
 R_r=(1-t)^h t^{C-1}w^{r-g},\quad
 P_r=(R_r+R_r^*)/2,\quad
 D_r=t(R_r^*-R_r)/(2f)
\]
得到；它们是整数Chebyshev多项式，且
\[
 tP_r/f-D_r=tR_r/f=O(t^L).
\]
这既负责消 unwanted period，也为有限处 divisibility服务，不是仅为实数插值自由另选的basis。

原矩阵是 \(\mathcal M(P_r,s^{b+k}(1-s)^q)-\tfrac32\mathcal Z(D_r,s^{b+k}(1-s)^q)\)。Andréief两次和Cauchy alternant给PDF式(62)–(65)的 exact double integral。用
\[
 t_i=\frac{2x_i}{1+x_i^2},\quad
 d\mu(t_i)=\frac{4|x_i|}{(1+x_i^2)^2}\,dx_i
\]
后，mixed sheet determinant恰为
\[
 \mathcal R_n(x)
 =\det_{r,i}\{\xi_f(x_i)x_i^{g-r}
              +\xi_n(x_i)x_i^{r-g}\},
\]
其中negative interval的 \((\xi_f,\xi_n)=(1/2,1/2)\)，positive interval为 \((-1/4,5/4)\)。因此其余主 integrand是
\[
 \frac{V(t)V(s)^2}{\prod_{i,j}(1-t_i s_j)}
 \prod_j s_j^b(1-s_j)^q
 \prod_i t_i^{C-1}(1-t_i)^h.                            \tag{C4}
\]
这里准确有一个t Vandermonde、两个s Vandermondes；不是把signed rows改成一个免费的positiveGram。

## 3. 为什么节点聚集不会引入逆 Vandermonde 爆炸

设 \(D_*=n-1-2g=40N-1\)。在case2
\[
 \sum_i\frac{1-x_i^2}{1+x_i^2}\le D_*                    \tag{C5}
\]
时，Lemma5.1给一个随node list变化的holomorphic interpolant
\[
 h_*(x_i)=c_i x_i^{D_*},\quad
 c_i=1\ (x_i<0),\quad c_i=-5\ (x_i>0),\qquad
 \|h_*\|_\infty\le K_0n,\quad K_0=10e^{12}.              \tag{C6}
\]
关键是同一个上界适用于任意节点间隔，即使节点极度聚集；无需一张固定的万能h。

具体构造为Blaschke product \(B(z)=\prod_i(z-x_i)/(1-x_i z)\)、\(F=z^{D_*}/B\)。C5给imaginary diameter上的 \(|F|\le1\)（稍外延后≤e²）。在固定vertical segment上以density6F作Cauchy integral，再定义
\(h_*=c_\pm z^{D_*}-B\mathcal C\)。
左右jump6F恰取消 \(c_--c_+=6\)。端点附近只作不跨越evaluationpoint或F poles的contour deformation，给均匀O(n) norm。没有用节点分离估计，更没有在零附近要求uniform derivativebound。

Proposition5.2的第二步更值得迁移。令
\[
 Q(z)=\prod_i(1-x_i z),\qquad
 \mathcal H_Q=\{v/Q:\deg v<n\}\subset H^2.
\]
reversal \(R(v/Q)=z^{n-1}v(1/z)/Q\) 在这个真实Hilbert norm中是isometry，原因是nodes/Q coefficients均为real。Hardy kernels \(k_i=(1-x_i z)^{-1}\) 张成 \(\mathcal H_Q\)，故orthogonal projection \(\Pi_Q\)保留nodevalues。压缩乘法
\[
 J=\Pi_QM_{h_*}|_{\mathcal H_Q},\quad \mathscr L=I+JR
\]
满足 \(\|\mathscr L\|\le1+K_0n\)。

定义的是**加权评价** \(E(v/Q)=(v(x_i))_i\)，不是裸取 \((v/Q)(x_i)\)。它满足PDF式(72)
\[
 E\mathscr L R(v/Q)
   =(\widetilde v(x_i)+h_*(x_i)v(x_i))_i.
\]
在monomial/Q basis里 \(\det E=V(x)\)，所以mixed evaluations除以V(x)以后就是 \(\det\mathscr L\)，所有Q(x_i)精确取消。由
\(|\det\mathscr L|\le\|\mathscr L\|^n\) 得
\[
 |\mathcal R_n(x)|
 \le(1+K_0n)^n\,|V(1/x)|\prod_i|x_i|^g.                 \tag{C7}
\]
这里没有估计 \(E^{-1}\)。很大的K₀也只带来 \(O(n\log n)\)，在n²尺度消失。

case1为C5失败。Proposition5.3不强行用插值，而对每个near/far choice把real nodes写为tanφ，用unit-circle Vandermonde的Hadamard估计：
\[
 |\mathcal R_n(x)|\le(3/2)^n n^{n/2}2^{-\binom n2}
       \prod_i(1+x_i^2)^{(n-1)/2}|x_i|^{g-(n-1)}.       \tag{C8}
\]
\(2^{-\binom n2}\) 是主能量，不可扔到误差；sheet绝对系数和、measure mass2ⁿ、两个factorials都已另列。两case合起来才覆盖所有integration configurations。

## 4. 能量估计的难点在统一性，尤其对角与端点

PDF式(76)定义externalfields
\[
 W_\kappa=(\alpha+2\gamma)\log|x|+2\eta\log(1-x)
  -(\kappa/2+\alpha+\eta+\gamma)\log(1+x^2),\quad
 W_s=\beta\log s+\gamma\log(1-s),
\]
\(\alpha=11/48,\beta=7/48,\gamma=1/12,\eta=1/24\)。
实数坐标变换给三个**同对象**kernels：
\[
 \log|x-x'|,\quad\log(1-xx'),\quad
 -\log(1-2xs+x^2).
\]
保留跨两组变量的最后一项，才能与前两项完成负平方；逐项粗估会丢掉主要收益。

不能把empirical diagonals代入undamped logarithm展开。论文先固定ε，选择matched damping（式83）
\[
 \tau=1-\varepsilon,\quad
 \rho(x)=1-\varepsilon(1-x),\quad
 \sigma(s)=1-\varepsilon\sqrt{1-s}.
\]
near(1,1)的尺度来自
\(|1-xe^{i\arccos s}|^2=(1-x)^2+2x(1-s)\)。
同样的damped moments
\[
 A_k=\langle\tau^kT_k(x)\rangle,\quad
 B_k=\langle\rho(x)^kx^k\rangle,\quad
 C_k=\langle\sigma(s)^kT_k(s)\rangle
\]
同时出现在pure与cross项，给exact squares（式86–87）
\[
 -\kappa\sum_k A_k^2/k,\qquad
 -\frac12\sum_k(B_k-2C_k)^2/k.                           \tag{C9}
\]
若pure、cross各自选一个“有利”的regularization，C9未必还成立。

漏掉diagonal后的upward corrections准确包含
\[
 O_\varepsilon(1/n)
  -\frac1{2n}\langle\log(1-x)\rangle
  -\frac1n\langle\log(1-s)\rangle.                       \tag{C10}
\]
它们不能在取sup以前笼统写成uniform O(1/n)，因为nodes能靠近1任意快。论文把它们吸收到externalfield，使端点系数变成
\[
 1/12-1/(2n),\qquad1/12-1/n.
\]
n≥24时都仍有positive下界。另一个重要身份是
\((C-1)+g-(n-1)=a+2g\)，所以x=0处没有额外singular finite-size loss。

因此x0、x1、s0、s1附近统一趋−∞，maximizers落在不依赖n和smallε的compactsets。正确次序是先n→∞（ε fixed），再ε↓0；不是交换sup和逐点极限。case1还通过 \(\langle2\gamma-2x^2/(1+x^2)\rangle>-1/n\) 加入一个λ≥0 multiplier，仅付λ/n。

## 5. 由负平方到两个可完整认证的一维 barrier

任取exponentiallydecaying realtrialsequencesp,v，定义
\(\|u\|_*^2=\sum u_k^2/k\)、\(T(u,x)=\sum u_kT_k(x)/k\)、\(S(u,x)=\sum u_kx^k/k\)。
用 \(-a^2\le b^2-2ab\) 切线化C9，Proposition6.1／式(78)得
\[
 (-1+\alpha+\gamma)\log2+
 \kappa\|p\|_*^2+\tfrac12\|v\|_*^2
 +\sup X_\kappa+\sup Y_\kappa,                          \tag{C11}
\]
\[
 X_\kappa=W_\kappa+\lambda D-2\kappa T(p,x)-S(v,x),\quad
 Y_\kappa=W_s+2T(v,s).
\]
任意admissibletrials均给真upperbound；不必先证明找到了global equilibrium。certificate只需给一组成功的rationaltrial，而不是证明该组“最优”。

case2用finite10terms加complex-conjugate exponentialtails，case1用finite8terms和λ=2.47405979。所有decimals为exactrationals；tails的norm与potentials化成finite principal-log formulas（式90），并明确complexbranch。

四个barrierderivatives为rationalfunctions，清denominator后真实degrees为36、24、13、9。Descartes变换给各interval的完整root uppercounts，43个disjoint rational brackets的endpoint signchanges达到这些counts，于是每bracket唯一simple root，没有遗漏stationarypoints。再单列7个finite divisionpoints，共50个candidatepointvalues。singular endpoints趋−∞；regular endpointx=−1实际evaluated。故不是网格扫描或靠“图上最大值”。

每个rootbracket宽 \(2/10^{10}\)，所有wholebrackets上 \(|X'|,|Y'|<120000\)，从左endpoint到真stationarypoint每个sup最多加0.000024。两sup总付0.000048。对数以finite rationalseries和显式tail remainder计算，signed complexweights保留intervaldirection；这不依赖浮点log。

paper的coarsecutoffs最终给
\[
 \kappa2:\quad -\tfrac{11}{16}(0.693146)
  +0.77844-0.98399-1.60890+0.000048=-2.290939875,
\]
\[
 \kappa1:\quad -\tfrac{11}{16}(0.693146)
  +0.9321-1.3244-1.4280+0.000048=-2.296789875.
\]
取较大的第一项，即C3。当前只读核查了recipe、每项预算及最终代数拼接，没有运行supplementarycertificate或独立重算每个整数count/tablevalue。

## 6. 哪些思想能迁移到 odd ζ，哪些还没有

与之前paired/determinant路线最直接的对应是：

| Catalan 论文真实机制 | 对 odd ζ 路线可借鉴的层面 | 仍需另证的实际输入 |
|---|---|---|
| 同一整数Chebyshevrows兼顾contact和divisibility | 先设计算术row family，再处理其真实near/far评价 | 完整ζ-period投影；不能遗留其它oddvalues或π/log项 |
| Hardycompression精确抵消evaluationdet | 把mixedrow估计做成operatornorm，避开逆Vandermonde | 实际基的isometricreversal、reproducingkernels与subexponentialinterpolant；一般kernel维数不提供这些 |
| 两case覆盖全configuration | 用可验证nodeconstraint换不同estimate及λdualcredit | fallbackprincipalenergy必须与原整模型一致 |
| matchedkernels形成(B−2C)² | 保留continuous/discrete或mirrorcrosscorrelation | 原ζintegrand的exactcrosskernel及统一regularization；不能各取一个新basis的最佳bound |
| all-configdiag/endpoints先付、后sup | n²率须有uniformfinite-n推导 | 全boundaryescape与collision；旧conservativeenvelope的改善不等于actualdet率 |
| all-prime productformula+prime-scale非零 | 同一saturatedlattice里比较whole determinant | 完整finite-place费用和无限尺度nonzero；signedintegral不自动positive |
| rationaltrial＋全rootcertificate | 搜索可提出trial，证据需成为finiteexactglobalcertificate | 新问题必须有足够strictmargin，不能把“可认证”本身当margin |

最关键的改变是，论文同时保住了**同一对象**的算术cancellation与实数crossinteraction。Hardy和potentialtheory不是单独解决所有特殊值的通用黑箱。我们此前的positive-envelope上界、relativeGram或kernelprojection若没有这些actualidentities，不能免费认领C7或C9；也不能把Catalan证书的数字直接用于ζ(7)。

更高阶oddζ可能需要多于两张sheet、不同contactsystem或更高ranklocalperiods。即使能构造analogousH²model，仍需target-onlyrationality、integerlattice、全primes、nonzero和strictenergygap五项同时闭合。此处仅解读和对照，不因用户暂停而启动旧研究的新计算。

## 7. 阅读与执行边界

freshPDF页域为1–5、18–19、25–42（25页）；README与四份章节source全文。没有修改E:/codex-build/math任何文件，没有执行repositoryPython、certificate、Lean、building或tests。PDF指纹、页数和text extraction仅为documentary。

本读后稿保存数学proof架构和最重要的uniformity接口。它不代表44页论文和所有formalization的完整独立认证，不代表已证明新的oddζ结果；原项目仍暂停。
