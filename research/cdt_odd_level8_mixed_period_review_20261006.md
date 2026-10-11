# χ8 共轭 source 的单位根端点与完整 cocycle：独立复核

日期：2026-10-06。本文新增，不改冻结三候选或level20输入。实际只读审阅 [level8 mixed embedding](cdt_odd_level8_mixed_embedding_20261006.md) §§2–6；另从原始divisor/Lambert sums独立计算ρ₃端点。未知ζ(3)、L(3,χ₈)始终是其通常实际数值，σ仅作用于源的代数系数。本稿确认该λ及M-cocycle正确，未取得数值无理性结论。

## 1. 固定 source 与一个新的独立证书

记r=√2、κ=16r、c₄=11/2，使用常数项1的通常E₄，以及Eχ∞=c₄、Fχ∞=0的divisor归一化。共轭源为

\[
 F_\sigma=\frac{11}{2}(E_4-64E_4(8\tau))
          +63(E_\chi+16rF_\chi).
\tag{A1}
\]

其∞constant为\((11/2)(1-64)+63(11/2)=0\)。取θq³fσ=Fσ、fσ(0)=0。新 [脚本](cdt_odd_level8_mixed_period_review_20261006_verify.py) 只作一次固定Fraction/SymPy检查；不import或执行冻结producer，不扫描素数，不用未知L值的小数。作者单次执行29checks通过，见 [JSON](cdt_odd_level8_mixed_period_review_20261006_verify.json)。

## 2. 从 divisor sums 取得真实 Lambert 表达式

置

\[
 S(q)=\sum_{n\ge1}\frac{q^n}{n^3(1-q^n)},\qquad
 F_\chi(q)=\sum_{n\ge1}\frac{\chi_8(n)q^n}{n^3(1-q^n)},
\]
\[
 E_\chi^{[-3]}(q)=\sum_{m\ge1}\frac{e_\chi(q^m)}{m^3},\qquad
 e_\chi(z)=\frac{z-z^3-z^5+z^7}{1-z^8}
          =\frac{z(1-z^2)}{1+z^4}.
\tag{A2}
\]

二者Eχ、Fχ的指标准确相反：Eχ coefficient是Σχ(d)d³，Fχ coefficient是Σχ(n)m³，不能互换。A1的实际primitive恰为

\[
 \boxed{f_\sigma(q)=1320\{S(q)-S(q^8)/8\}
             +63E_\chi^{[-3]}(q)+1008rF_\chi(q).}
\tag{A3}
\]

E₄(8τ)的64系数经θq⁻³除以8³，因此是1/8，不能误写成64或1。

## 3. 临界输入全部由有限 Bernoulli 值固定

独立有限和给

\[
 B_{2,\chi_8}=2,\quad B_{4,\chi_8}=-44,
 \quad B_{3,\chi_{-3}}=2/3,
 \quad B_{3,\chi_{-24}}=138.
\tag{A4}
\]

这里χ₋₂₄=χ₈χ₋₃，在units1,5,7,11取1，在13,17,19,23取−1。Fourier Bernoulli/primitive Gauss sum公式给

\[
 L(3,\chi_{-3})=\frac{4\pi^3}{81\sqrt3},\qquad
 L(3,\chi_{-24})=\frac{23\pi^3}{288\sqrt6},
\]
\[
 L(4,\chi_8)=\frac{11\pi^4}{768\sqrt2},
 \qquad \kappa L(4,\chi_8)=\frac{165}{8}\zeta(4).
\tag{A5}
\]

这些均为parity-compatible临界值。A5没有对困难的even-role odd值L(3,χ₈)作任何替代或有理性假设。

## 4. 真正径向极限：pole先相消，再得到λ

令ρ=exp(2πi/3)、q=ρexp(−ε)、ε↓0。对3∤n，

\[
 \frac{\rho^n}{1-\rho^n}
 =-\frac12+\frac{i}{2\sqrt3}\chi_{-3}(n).
\]

对3|n，\(q^n/(1-q^n)=1/(\varepsilon n)-1/2+o(1)\)。减去1/(εn)后绝对值≤1/2，所以乘n⁻³后由dominated convergence确定其finite part；非3倍指标的分母沿径向一致离开0，同样可用dominated convergence。因χ₈(3)=−1，两个Lambert和为

\[
 S(\rho e^{-\varepsilon})=
 \frac{\zeta(4)}{81\varepsilon}-\frac{\zeta(3)}2
 +\frac{2i\pi^3}{243}+o(1),
\]
\[
 F_\chi(\rho e^{-\varepsilon})=
 -\frac{L(4,\chi_8)}{81\varepsilon}
 -\frac{L(3,\chi_8)}2
 +\frac{i}{2\sqrt3}L(3,\chi_{-24})+o(1).
\tag{A6}
\]

S(q⁸)在ρ²处取radial parameter8ε，故其pole为ζ4/(648ε)，其虚finite part反号。Eχ的sum无需regularization：eχ(1)=0、eχ(ρ)=i√3、eχ(ρ²)=−i√3；这些三条径向上的rational kernel一致有界，m⁻³和绝对支配，得到

\[
 E_\chi^{[-3]}(\rho)=i\sqrt3 L(3,\chi_{-3})
 =4i\pi^3/81.
\tag{A7}
\]

A3全部1/ε系数是

\[
 \frac1{81\varepsilon}
 \{1320(1-1/64)\zeta(4)-63\kappa L(4,\chi_8)\}=0.
\tag{A8}
\]

这一步说明λ是真实有限径向极限，而不是独立给各divergent sum指定一个“正则值”。三个部分的finite contribution为

|部分|实部|iπ³系数|
|---|---|---:|
|1320[S−S(q⁸)/8]|−1155ζ3/2|110/9|
|63Eχ^[−3]|0|28/9|
|1008√2Fχ|−504√2L3χ8|161/12|

所以

\[
 \boxed{\lambda=f_\sigma(\rho)
 =-\frac{1155}{2}\zeta(3)-504\sqrt2L(3,\chi_8)
        +\frac{115}{4}i\pi^3.}
\tag{A9}
\]

110/9+28/9+161/12=115/4已精确核。实虚三项均与被审稿相同。

## 5. M的完整 period：不存在另一个独立的一次项

取

\[
 \gamma=\begin{pmatrix}3&1\\8&3\end{pmatrix},\qquad
 M=\gamma W_8=\begin{pmatrix}8&-3\\24&-8\end{pmatrix},\quad M^2=-8I.
\]

trivial-character的U在W₈下anti；χ₈-character的V₊在W₈下plus，但χ₈(3)=−1使γ作用反号。故整个Fσ在M下是anti：\(F_\sigma|_4M=-F_\sigma\)。这是使用真正Γ₀(8)变换与角色得到的身份，未对数值周期施σ。

定义weight−2 action

\[
 (J_Mf)(\tau)=\frac{(24\tau-8)^2}{8}f(M\tau)
             =8(3\tau-1)^2f(M\tau).
\]

Bol covariance给\(P=f_\sigma+J_Mf_\sigma\)的第三导数为0，故P是degree≤2 polynomial。M²central使J_M²=1，因而J_MP=P。在h=1/3、z=τ−h坐标，

\[
 M(h+z)=h-1/(72z),\qquad J_M=72z^2\text{ times pullback}.
\]

若P=a+bz+cz²，则J_MP=c/72−bz+72az²。J_MP=P迫b=0、c=72a。因此其+1 eigenspace严格一维，生成元1+72z²；没有可独立增加的一次项。τ→h+i0时J_Mfσ→0，由A9又得a=λ。完整cocycle因此为

\[
 \boxed{f_\sigma(\tau)+8(3\tau-1)^2f_\sigma(M\tau)
  =\lambda\{1+8(3\tau-1)^2\}.}
\tag{A10}
\]

展开后的polynomial当然含\(-48\lambda\tau\)，这是同一固定quadratic generator的一部分；“无独立一次项”不能误说成以原τ展开时一次系数为零。

## 6. 对被审正文其余周期与障碍的限定核对

实际只读§§2–3的L1/L2/L3及非cuspidal pair。对一般F、G=F|W_N，constant为a、b，completed primitives加入a(2πiτ)³/6、b(2πiτ)³/6。其Bol差是degree≤2 polynomial。Mellin residues0,−1,−2给L3+2πiτL2−2π²τ²L1；s=1与−3的constant residues分别为−b(2πi)³/(6N²τ)、−a(2πi)³τ³/6。此处被审稿保留了全Laurent terms，四个显示(7)/(8a–c)的sign和系数重推吻合。随后实际复读新增(6a)：两个指数衰减的regularized积分均entire，补出的bY^(s−4)/[N²(s−4)]与−aY^s/s使Y依赖取消，换元y→1/(Ny)给ΛF(s)=N^(2−s)ΛG(4−s)，0及4的residues与上述sign一致。

具体Fσ在普通W₈下不是eigen，其W∞constant为693，因此不能套两端constant0的简单Fricke polynomial。被审稿(7)的实际余项−42iπ³τ+231iπ³/(16τ)正确；新M叶的A10与此结论并不冲突。

实际只读§5的scalar-prefactor论证亦通过，限定B是Γ=kerχ₈上的weight2 meromorphic modular form。M正规化Γ，B^M/(B+B^M)为T-periodic；若B(fσ−a)在M二次商下降而a实，A9的λ−a≠0与q_M(τ+1)−q_M(τ)=144τ+24≠0相矛盾。此结论不排ramified pullback、不同embedding maps或增加别的真实Eichler周期。

实际只读§6的另一endpoint与complete trace：λ′=ψ−(115/4)iπ³，q_M′=1+8(3τ+1)²。其endpoint average为ψ，但完整polynomial average严格为

\[
 \frac{\lambda q_M+\lambda' q_{M'}}2
 =9\psi(1+8\tau^2)-1380i\pi^3\tau.
\tag{A11}
\]

所以endpoint imaginary cancellation不等于同一完整cycle无Tate项。A11的linear coefficient已独立精确核对。

## 7. 审阅范围与边界

本作者独立从A2的原始Lambert和、有限Bernoulli值、真实γ角色与Bol action重推A9–A11；另实际只读被审稿§§2–6，其L-value、Laurent residues、scalar-prefactor与trace的上述范围通过。未运行其producer，没有复核其全部76项实现，也未独立重证Γ的完整群几何或第7节尚未构造的analytic map。

新29check证书仅支持固定Bernoulli、finite kernels、matrix/Sym²、residue cancellation与有理系数。径向limit、Bol covariance和T-periodic矛盾由本稿证明承担，不由有限checks替代。不存在对未知ζ3、L3、π³的“Galois共轭”假设。此审阅确认真实period输入，不能作为已有无理性定理或共同number-field holonomy预算成功。
