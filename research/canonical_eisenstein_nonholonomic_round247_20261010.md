# 第247轮：canonical去常数Eisenstein源的实际非holonomic障碍

2026-10-10，B。全部数学为纸证，数学程序/CAS/Lean、素数、参数、map扫描均为0。本稿只核同一Γ₀(7)、同一u坐标的另一Eisenstein源。结论：去常数给出的native有理Taylor源确实存在且有完整安全分母，但不是D-finite；任何固定非零有理微分过滤亦不能使它D-finite。没有新数值无理性或LI定理。

## 1. 固定输入与准确字符

实际FULL读冻结246源、报告及独审收据；亲自完整读已存Yang物理PDF5–11、15–16文本载体及Stein Definition(4)/Theorems5.8–5.9选段。采用246已明示的eta模单位输入：u为X₀(7)的degree-one坐标，两个cusps对应0、∞。本稿不声称重新认证该判据的全部上游证明。记
\[
q=e^{2\pi i\tau},\quad \chi=\chi_{-7},\quad
u=(\eta(7\tau)/\eta(\tau))^4,\quad
t=\frac{u}{(1+7u)^2},\quad P=1+13u+49u^2,
\]
\[
f=\eta(\tau)^3\eta(7\tau)^3,\quad
A=1+2\sum_{n\ge1}\chi(n)\frac{q^n}{1-q^n},\quad
\delta=u\partial_u,\quad D_q=q\partial_q,
\]
\[
\mathscr L=P^2\delta^2-2u(1+16u+49u^2),\qquad
\mathscr LA=0. \tag{N1}
\]
这里A与u取native q→0的芽；A=1+O(q)，u=q+O(q²)。A在H全纯；其零点离散。u在H全纯且非零，u′的零点也离散。

Yang例2实际给
\[
A=G_1^2g_0/f,\qquad G_1=D_qt/t,\qquad
g_0=\frac{t}{(1-t)(1-28t)},
\]
并在Theorem2给f的weight3与字符χ(d)。由于t在Γ₀(7)不变，链式法则给G₁的weight2及平凡字符。因此对
\(\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma_0(7)\)，
\[
A(\gamma\tau)=\chi(d)^{-1}(c\tau+d)A(\tau)
=\chi(d)(c\tau+d)A(\tau). \tag{N2}
\]
这由实际函数身份得出，不由形式“weight1”命名领取。χ为实二次字符；中心−I的字符−1与weight1因子相消。

## 2. Wronskian与去常数的完整forcing

齐次实际basis A、τA由Yang变化常数式给出；也可直接由N2中
\(U=\left(\begin{smallmatrix}1&0\\7&1\end{smallmatrix}\right)\)
得到：沿u不变的实际延拓，A(Uτ)=(7τ+1)A仍满足N1，故τA是齐次解。将N1除以P²后没有δ一次项，δ-Wronskian恒定：
\[
A\delta(\tau A)-\tau A\delta A=A^2\delta\tau.
\]
native q→0的极限给该常数1/(2πi)，于是
\[
\delta\log q=A^{-2}. \tag{N3}
\]
对任意局部二次可微q函数ℰ，直接展开而非忽略交叉项：
\[
\delta\mathcal E=A^{-2}D_q\mathcal E,\qquad
\delta^2\mathcal E=-2A^{-3}(\delta A)D_q\mathcal E
                  +A^{-4}D_q^2\mathcal E.
\]
利用\(\mathscr LA=0\)后交叉项精确抵消，得
\[
\boxed{\mathscr L(A\mathcal E)=P^2A^{-3}D_q^2\mathcal E.} \tag{N4}
\]
另由Yang的A身份、N3及t(u)，
\[
D_qt/t=\frac{1-7u}{1+7u}A^2,\qquad
f=\frac{uA^3}{P}. \tag{N5}
\]
这些恒等式初在非零分母的native域证明，再以亚纯身份延拓。

Stein的定义和奇偶条件χ(−1)=−1给实际全纯模形式
\[
e_1=E_{3,1,\chi}
=-\frac87+\sum_{n\ge1}b_nq^n,\qquad
b_n=\sum_{d\mid n}\chi(d)d^2\in\mathbb Z. \tag{N6}
\]
常数可独立核：\(B_{3,\chi}=7^2\sum_{a=1}^7\chi(a)B_3(a/7)=48/7\)，
故\(c_0=-B_{3,\chi}/6=-8/7\)。例如
\(\sum\chi(a)a=-7,\ \sum\chi(a)a^2=-49,\ \sum\chi(a)a^3=-295\)，
代入\(B_3(x)=x^3-\frac32x^2+\frac12x\)得到48/7。

canonical native源明确为
\[
\widehat{\mathcal E}_1=\sum_{n\ge1}\frac{b_n}{n^2}q^n,\qquad
\widehat B(u)=A(q(u))\widehat{\mathcal E}_1(q(u)). \tag{N7}
\]
u(q)及其inverse整系数、A整系数，故
\[
\widehat B\in u\mathbb Q[[u]],\qquad
d_N^2[u^j]\delta^r\widehat B\in\mathbb Z
\quad(0\le j\le N,\ r\ge0\text{固定}). \tag{N8}
\]
这里覆盖全部素数与素数幂，不是最小LCD声明；canonical非constant coefficients本身整数，不因c₀而额外加入7。固定g∈Q时，清其固定分母后同样清\(\widehat B-gA\)。

e₁/f的weight与字符相消。在H无pole，两个cusps至多simple pole，故degree-one u坐标给
\[
e_1/f=\alpha_{-1}/u+\alpha_0+\alpha_1u\in\mathbb Q(u).
\]
系数的有理性来自native Laurent展开的有理系数，不以未付无限身份作有限拟合。令\(R_1=uP(e_1/f)\)。N4–N7给
\[
\boxed{\mathscr L\widehat B
=R_1+\frac87P^2A^{-3},\qquad R_1\in\mathbb Q(u).} \tag{N9}
\]
正号来自减去c₀=−8/7。完整e₁的二重primitive应另含
\(c_0(\log q)^2/2\)，它不是native holomorphic Taylor芽。去掉该项改变forcing，不能仍沿用246的有理forcing模板。

## 3. 无限分支是实际u闭路延拓

令F=A⁻³，native F(0)=1。对k≥0取
\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\gamma_k=UT^k=\begin{pmatrix}1&k\\7&7k+1\end{pmatrix}.
\]
它们确属Γ₀(7)，det=1，χ(7k+1)=1，且u(γₖτ)=u(τ)。N2因此给
\[
F(\gamma_k\tau)=(7\tau+7k+1)^{-3}F(\tau). \tag{N10}
\]

为避免把模变换形式等式偷换成实际monodromy，假设F有一个非零C(u)系数齐次ODE。取其全部有限系数pole和leading coefficient zero组成有限集S；选高处native τ₀，使u₀=u(τ₀)为ordinary点、A(τ₀)≠0、u′(τ₀)≠0。H中删去A零点、u′零点及u⁻¹(S)。这些集合局部有限离散，且因模变换而使所有γₖτ₀仍为未删点。H减去离散集仍路径连通：取紧的分段路径，只需绕开其邻域中的有限多个删点。

故每个k均有实际路径τ₀→γₖτ₀，沿途u′≠0。其u投影是基于u₀、避开S的闭路；逐个局部inverse接续给F的实际解析延拓。终点的inverse正是γₖτ(u)，因为u∘γₖ=u且终点值匹配。于是这些实际返回芽包括
\[
F_k(u)=(7\tau(u)+7k+1)^{-3}F_0(u). \tag{N11}
\]
不需要宣称H是整个u平面的普通universal cover，也不忽略椭圆点或新增ODE apparent singularities。

任意有限线性关系\(\sum_{k\in I}c_kF_k=0\)，除以局部非零F₀后并用τ为局部变量，给
\[
\sum_{k\in I}\frac{c_k}{(7\tau+7k+1)^3}=0.
\]
这是在一个开集成立的有理函数身份。其极点−k−1/7彼此不同，逐个比较三阶principal part迫全部cₖ=0。极点在实轴而不在H不影响此有理身份论证；不声称这些点是H内实际pole。因此N11中任意有限多个芽都C-linearly independent。

有理ODE在ordinary u₀的齐次解空间维数有限，所有避开S的闭路继续芽都仍在这个空间；与上述无限线性独立矛盾。于是
\[
\boxed{A^{-3}\text{ 不是C(u)上的D-finite芽。}} \tag{N12}
\]
order0亦不可能，因为F非零。证明只用实际闭路与有限维解空间，不用猜测递推、growth或参数样本。

## 4. canonical源与全部固定非零有理微分过滤

D-finite芽等价于其所有导数的C(u)-span有限维；从齐次ODE可递推更高导数，反向有限依赖给ODE。因此它们对加法、有理乘法及固定有理微分算子封闭。若\(\widehat B\) D-finite，N9便迫
\[
A^{-3}=\frac7{8P^2}\bigl(\mathscr L\widehat B-R_1\bigr)
\]
D-finite，与N12矛盾。由于A本身D-finite，对每个固定g∈C，
\[
\boxed{\widehat B-gA\text{ 不是D-finite。}} \tag{N13}
\]

还可排除“先用一个非零固定operator再要求有限闭包”。设
\(Q\in\mathbb C(u)[\partial_u]\setminus\{0\}\)。
若Qy为D-finite，取其非零annihilator H；则(HQ)y=0。该Ore环无零因子，leading derivative coefficient的乘积非零，所以HQ≠0，y亦D-finite。若Qy=0，Q本身即annihilator，结论相同。因此
\[
\boxed{Q(\widehat B-gA)\text{ 对所有这样的Q都不是D-finite。}} \tag{N14}
\]
若输入再加固定D-finite函数或输出再加固定D-finite函数，闭包性给同样结论。这里Q固定、系数有理、输入只此一个非D-finite方向；不涵盖两个相关非D-finite源之间的抵消。

## 5. 本关结论与停止边界

N8的native有理Taylor与全部prefix安全整模型成立，但planned有限holonomic scalar/cyclic源入口在N9–N14处失败。对这一canonical e₁源，不投入下一项fixed-basis、prime或map费用优化来补一个不存在的有限holonomic闭包。

这是实际单源holonomicity gate，不是“所有CDT都要求D-finite”的断言；直接算术holonomy定理有它自己明示的函数、分母和图条件。本稿不排除另行支付这些条件的非D-finite入口，不排除多源相关抵消、增长周期投影、其他level/坐标或新整格，也没有证明Y=L(2,χ−7)的有理性或无理性。完整period stack/全leaf投影、同对象无限非零和strict能量均未从本证明取得。

246冻结稿、主日志、policy、manifest不改。详细实际阅读身份另记本轮packet_reading_scope.md；数学执行数0。保存后本文实际FULL自读，最终bytes/SHA另报。
