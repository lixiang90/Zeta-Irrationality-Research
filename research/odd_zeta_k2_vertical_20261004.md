# Catalan 椭圆商符号的整模型、全部垂直 tame 与四阶扭退化

日期：2026-10-04。承接冻结的 [椭圆商报告](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004.md)，另立本稿，不修改旧结论。所有计算都是固定代数身份和全尺度赋值论证，无参数扫描。

本稿完成一项原先未做的检查：在明确的双覆盖整模型及其只在素数 2 上发生的正则解消上，T 的每个垂直分量 tame 都是 1。更强、也更决定研究方向的发现是

\[
\boxed{4T=0\quad\text{在 }K_2^M(K(C))\text{ 中整系数成立。}}\tag{1}
\]

因此 T 的有理类为零，不能提供非零实／有理调节子。这里没有断言整系数 T 本身等于零。已有非零 Catalan 长度二积分也没有因此消失：该路径积分尚未被证明是 T 的调节子值。独立的 [下降报告](E:/kimi-build/zeta5/research/odd_zeta_k2_descent_20261004.md) 给出同一整系数退化的另一次审查。

## 1. 固定对象与精确函数

令

\[
K=\mathbf Q(i,a)=\mathbf Q(\zeta_8),\qquad a=\sqrt2,\qquad
C:\ Y^2=Q(s)=s^8-14s^4+1.
\]

C 表示这条函数域曲线的光滑射影模型。定义

\[
A_0(s)=(s^2+1)(-s^4+4s^2-1)=-s^6+3s^4+3s^2-1,
\]
\[
B_0(s)=(s^2-1)(s^4+4s^2+1)=s^6+3s^4-3s^2-1.
\]

冻结报告两椭圆商上的函数拉回后为

\[
u_+=\frac{s^2+as+1}{s^2-as+1},\qquad
u_-=\frac{s^2-ias-1}{s^2+ias-1},
\]
\[
F_+=\frac{asY-iA_0(s)}{asY+iA_0(s)},\qquad
F_-=\frac{asY-B_0(s)}{asY+B_0(s)}.
\tag{2}
\]

本稿始终研究同一个整系数 Milnor 符号

\[
T=\{u_+,F_+\}+\{u_-,F_-\}\in K_2^M(K(C)).
\tag{3}
\]

tame 采用旧稿约定

\[
\partial_v\{f,g\}=(-1)^{v(f)v(g)}
\overline{f^{\,v(g)}/g^{\,v(f)}}.
\tag{4}
\]

Rost、Weibel 的通常约定是 (4) 的逆；下文所有 tame 等于 1、范数相容、核与扭阶结论不受这一选择影响。冻结报告已证明 T 在 C 的每个几何点 tame 等于 1，故在每个 K-闭点也等于 1；(2) 没有改变该类。

## 2. 四阶扭证明：完整 V₄ 不变性与常数特化

令

\[
\sigma(s,Y)=(-s,Y),\qquad \tau(s,Y)=(1/s,Y/s^4).
\]

它们交换并生成 V₄。精确函数动作如下：

| 函数 | σ | τ |
|---|---|---|
| u₊、F₊ | 同时取逆 | 各自固定 |
| u₋、F₋ | 同时取逆 | 同时取逆 |

因为 \(\{f^{-1},g^{-1}\}=\{f,g\}\)，两项及 T 都被整个 V₄ 固定。特别，τ 并非把正商的两个函数取逆；正确的动作表仍给完整不变性。

V₄ 的固定域由

\[
r=s^2+s^{-2},\qquad y=Y/s^2,\qquad y^2=r^2-16
\]

生成。这个 conic 在 K 上有理：设

\[
\lambda=(r+y)/4,\qquad
r=2(\lambda+\lambda^{-1}),\quad
y=2(\lambda-\lambda^{-1}).
\tag{5}
\]

由 s 满足 \(s^4-rs^2+1=0\)，固定域的次数至多 4；四个不同自同构给次数至少 4。因此

\[
K(C)^{V_4}=K(\lambda),\qquad [K(C):K(\lambda)]=4.
\]

置 \(N=\operatorname{cor}_{K(C)/K(\lambda)}T\)。范数与 tame 相容给

\[
\partial_vN
=\prod_{w\mid v}
N_{\kappa(w)/\kappa(v)}(\partial_wT)=1
\]

对 \(K(\lambda)\) 的每个水平闭点成立。这里 w 正是 C 的闭点赋值，所用赋值环的有限正规化条件满足。Rost 的整系数规则 R1c、R3b 与 Theorem 1.4 分别给基变换、范数／残差相容及 Milnor K 理论的适用性；见 [Rost 作者原稿，印刷 pp.329–331](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)。因此不是先有理化后再作下降。

有理函数域的 Bass–Tate／Milnor 正合列给

\[
\ker\!\left(K_2^M(K(\lambda))
\longrightarrow\bigoplus_{v\in\mathbf A^1_K{}^{(1)}}\kappa(v)^\times\right)
=K_2^M(K).
\]

所以存在唯一常数 \(\alpha\in K_2^M(K)\)，使 \(N=\operatorname{res}\alpha\)。Galois 基变换再给

\[
\operatorname{res}N=\sum_{\gamma\in V_4}\gamma T=4T
\quad\text{在 }K_2^M(K(C))\text{ 中。}\tag{6}
\]

这也可由 \(K(C)\otimes_{K(\lambda)}K(C)\cong\prod_{\gamma\in V_4}K(C)\) 与 transfer 的可加性理解。

现在在 K-有理点 \(P_0=(s,Y)=(0,1)\) 特化。s 是局部参数，(2) 的四个分子、分母都在此处为单位，并且

\[
u_+(P_0)=u_-(P_0)=1,\qquad
F_+(P_0)=F_-(P_0)=-1.
\]

离散赋值的 Milnor 特化同态把单位符号送到残域中的单位符号，把常数送回自身。因此由 (6)

\[
\alpha=s_{P_0}(\operatorname{res}\alpha)
=4s_{P_0}(T)
=4\bigl(\{1,-1\}+\{1,-1\}\bigr)=0.
\]

得到 (1)。不是把等式任意代表中的函数逐项代值，而是先使用整个 Milnor 群上的特化同态。上述有理函数域核及特化的整系数表述见 [Weibel 作者稿，III.7.3–7.4](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf)。

## 3. 明确整数环与 proper 双覆盖模型

取 \(R=\mathcal O_K=\mathbf Z[\zeta_8]\)，其中

\[
\zeta_8=(1+i)/a,\qquad i=\zeta_8^2,\qquad
a=\zeta_8+\zeta_8^{-1}.
\]

这个整数环的等式可用 [Conrad，prime-power cyclotomic integer ring，Theorem 0.1](https://math.stanford.edu/~conrad/154Page/handouts/cycint.pdf)。本稿另外精确计算

\[
\operatorname{disc}(K)=\operatorname{disc}(X^4+1)=2^8,\qquad
\operatorname{disc}_sQ=2^{40}3^4.
\tag{7}
\]

因此 3 在 K 中不分歧；2 是唯一数域分歧素数，并且全分歧。模 3，

\[
X^4+1=(X^2+X-1)(X^2-X-1)
\]

的两因子各不可约，故 R 有两个 3 上素理想，残域均为 \(\mathbf F_9\)。在其局部环中 3 是 uniformizer，a、i 都是单位。

定义 \(\mathcal X\to\mathbf P^1_R\) 为下面两张图的粘合：

\[
\mathcal X_s=\operatorname{Spec}R[s,Y]/(Y^2-Q(s)),\qquad
\mathcal X_t=\operatorname{Spec}R[t,Z]/(Z^2-Q(t)),
\tag{8}
\]

\[
t=s^{-1},\qquad Z=Y/s^4.
\]

因为 \(s^8Q(1/s)=Q(s)\)，粘合成立。两张图上的代数作为底部坐标环模都有基 \(1,Y\) 或 \(1,Z\)，故 \(\mathcal X\) 是 \(\mathbf P^1_R\) 上次数二的 finite flat 双覆盖，因而 proper 且对 R flat。其泛纤维就是 C。它是整概形：坐标环嵌入无零因子的泛纤维函数域，且 R-模无扭。

(7) 是所写多项式的判别式，不冒充任何未算出的最小模型判别式。它使 (8) 的待检查残特征只剩 2、3。

## 4. 每个残特征 p>3：smooth 单分量与实际单位

令 \(\mathfrak p\subset R\) 的残特征 p>3。2 与 (7) 在 \(R_{\mathfrak p}\) 中都为单位，所以 \(Q\bmod\mathfrak p\) 无重根，(8) 是 smooth proper model。

其几何纤维不可约：squarefree 的八次多项式在代数闭包的有理函数域中不是平方，故双覆盖不是两分量。每个 \(\mathfrak p\) 的垂直纤维只有一个 generic component。

在该分量的函数域中，u± 的分子、分母都是首项系数为 1 的非零二次式。F± 的每个分子、分母都是形如

\[
\overline{a}s\overline Y\ \pm\ \overline i\,\overline{A_0}
\quad\text{或}\quad
\overline{a}s\overline Y\ \pm\ \overline{B_0}.
\]

其中 \(\overline Y\notin\kappa(\mathfrak p)(s)\)，而 \(\overline a\ne0\)。所以每一个表达式都非零。于是四个有理函数的垂直赋值全为 0：

\[
v_{\mathfrak p}(u_\pm)=v_{\mathfrak p}(F_\pm)=0.
\]

两个符号分别 tame 为 1。这是对所有 p>3 的一次性证明，并非有限素数样本。

## 5. 残特征 3：所选模型已有全部分量，无遗漏解消除子

在每个 \(R_{\mathfrak p}\)，\(\mathfrak p\mid3\)，有精确身份

\[
Q(s)=(s^4-1)^2-12s^4.
\tag{9}
\]

特殊纤维是两条 multiplicity 1 的 \(\mathbf P^1\)：

\[
\Gamma_+:\ Y=s^4-1,\qquad
\Gamma_-:\ Y=-(s^4-1).
\]

它们在 \(s^4=1,\ Y=0\) 的四点相交；这些点均在残域 \(\mathbf F_9\) 中，因为 ±1、±i 皆存在。四根各简单。

不能只从纤维有节点推出 arithmetic surface regular。此处可作完整局部核验。定义

\[
u=Y-s^4+7,\qquad v=Y+s^4-7.
\]

利用曲线方程得

\[
\boxed{uv=-48=-16\cdot3},\qquad
s^4=(v-u+14)/2,\quad Y=(u+v)/2.
\tag{10}
\]

在四个节点，u、v 都在 maximal ideal 中；s 是单位，且 \(4s^3\) 是单位。因此在各节点附近，从 s 到 s⁴ 是 étale，(10) 给局部 étale 模型 \(uv=-48\)。右端是 3 的一次幂乘单位，所以最大理想由 u、v 两个元素生成，Krull 维数为 2：该局部环 regular。它还是 thickness 1 的 semistable node。

非节点处，特殊纤维 smooth，所以总空间 regular。两张无穷远图在 t=0 有 Z=±1，导数 2Z 为单位，亦 regular。因此 \(\mathcal X_{R[1/2]}\) 本身是 regular proper model；素数 3 上没有需要加入的 exceptional component。

对两个 generic components，模 3 有

\[
A_0=-s^6-1,\qquad B_0=s^6-1.
\]

代入 \(\overline Y=\pm(s^4-1)\) 后，\(\overline a s\overline Y\) 为五次多项式，而 \(\overline i\,\overline{A_0}\)、\(\overline{B_0}\) 为六次、首项系数为单位。因此 F± 的四个分子、分母都非零。u± 的首项同样为 1，亦非零。每个 \(\Gamma_\pm\) 上四个函数的垂直赋值全部为 0，两个符号分别 tame 为 1。

这里检查的是所选 regular model 的两个完整分量。没有把这两项检查直接推广成任意奇素数 blowup 或任意 regular model 上全部赋值的断言；后者需要另一个适用的延伸／纯性论证。

## 6. 残特征 2：任意垂直 divisorial valuation 的 tame 都为 1

(8) 在残特征 2 上的朴素纤维为

\[
\overline{Y^2-Q(s)}
=\bigl(Y-(s+1)^4\bigr)^2.
\tag{11}
\]

因此它不能充当正则模型所有分量的清单；本稿不作这种替代，也没有声称已经列出 wild resolution graph。

可用一个更强的赋值引理完成全部检查。

**引理。** 设 E 是一个域，\(x\in K_2^M(E)\) 满足 \(2^e x=0\)。若 v 是任意离散赋值且 \(\operatorname{char}\kappa(v)=2\)，则 \(\partial_vx=1\)。

**证明。** tame 是群同态，故 \((\partial_vx)^{2^e}=1\)。在特征 2 的域中，\(X^{2^e}-1=(X-1)^{2^e}\)，所以 \(\kappa(v)^\times\) 没有非平凡的 2-primary torsion，\(\partial_vx=1\)。证明不要求残域有限、v 无分歧或模型 semistable。□

将 e=2、x=T 代入 (1)，得到

\[
\boxed{\partial_vT=1
\quad\text{对 }K(C)\text{ 每个残特征 2 的离散赋值成立。}}\tag{12}
\]

特别，任何正则解消上的原分量和全部 exceptional components 均覆盖；其 multiplicity、intersection graph、2-adic ramification 不影响 (12)。这里只需检查 T 总和，未断言两个单符号分别满足 (12)。

为把全素数结果放在一个 proper regular model 上，先有限正规化 (8)，再取在 regular locus 上为同构的 proper 正则解消

\[
\widetilde{\mathcal X}\longrightarrow\mathcal X.
\]

R 是 excellent 的 Dedekind 整数环；此处二维整概形的 finite normalization 与 surface resolution 存在，见 [Stacks，54.1 的适用范围](https://stacks.math.columbia.edu/tag/0ADX) 和 [Lipman 定理 54.14.5，0BGP](https://stacks.math.columbia.edu/tag/0BGP)。解消中心可只放在 2 上，因为 §4–5 已证明其余部分 regular。所得模型仍 proper，整且支配 R，故对 Dedekind 底部 flat，泛纤维为 C。

在这一个选定模型上，奇素数全部分量就是 §4–5 所检；素数 2 的每个分量都由 (12) 处理。于是

\[
\boxed{\partial_D T=1
\quad\text{对 }\widetilde{\mathcal X}\text{ 每个垂直 prime divisor }D.}
\tag{13}
\]

水平 prime divisors 沿用旧稿 tame=1。故完整 codimension 1 检验通过。更精确地，它给

\[
T\in K_{2,\mathrm{nr}}^M(\widetilde{\mathcal X})
:=\ker\!\left[
K_2^M(K(C))\xrightarrow{\oplus\partial_D}
\bigoplus_{D\in\widetilde{\mathcal X}^{(1)}}\kappa(D)^\times
\right],\qquad 4T=0.
\tag{14}
\]

(14) 是以全部 codimension 1 residues 定义的无分歧 Milnor 群结论。未额外调用 mixed-characteristic Gersten 去把它识别成一个指定全局 Quillen K₂ 群的像；本轮垂直检验不需要该识别。

## 7. 对研究路线的实际含义

该 T 通过全部水平与所选 arithmetic model 的全部垂直 tame，仍在有理化后为零。因此“垂直整性成立”没有修复它的非零性。任何从该类出发、取值于实或有理向量空间的群同态调节子都把它送到零；这不排除有限系数中的 torsion 信息，也没有证明整系数 T=0。

冻结稿的实际 Catalan 表达式是沿指定 open path 的长度二积分

\[
G=\frac i4(I_++I_-).
\]

它使用单值分支、基点和端点；tame 符号类 (3) 忘记了部分路径与对数分支资料。此前没有证明这一路径表达式是 (14) 的 regulator，所以 (1) 不是非零积分的矛盾。今后若继续几何路线，应明确改选不被这次 V₄ 平均杀掉的类，或保留 open／relative motivic extension 和路径资料，再证明与目标常数的真实配对关系。不能再把本 T 作为已有非零有理 K₂ 输入。

本轮也没有从固定整模型推出近似线性形式的分母或 content。整数近似的无限尺度预算仍须独立建立。

## 8. 精确证书与审阅范围

[脚本](E:/kimi-build/zeta5/research/odd_zeta_k2_vertical_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_k2_vertical_20261004_verify.json) 已运行通过。它们核对 (2) 的拉回函数、σ／τ 精确动作、quotient conic 与参数化、两种判别式、3 的分解、两图 reciprocal 粘合、(9)–(11)、3 上 generic nonzero 的次数证据及 P₀ 单位特化值。

SymPy 证书不替代 Milnor transfer 正合列、surface resolution 或 (12) 的全赋值证明。这三处由上文理论推导承担。整系数下降已由根任务与几何分支独立核查；几何分支另对 §§5–6 作只读复审，确认 3 上 exact étale node chart、无穷远 regularity、2 上任意赋值引理、Stacks 解消适用范围，以及 (14) 不冒充全局 Quillen lifting，均通过，无必要纠错。本稿及证书在该审阅后冻结。
