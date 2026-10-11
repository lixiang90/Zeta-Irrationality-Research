# ζ(7) 的 level 12 实际微分模型：周期触发、模坐标与循环秩 8

日期：2026-10-05。本稿是新建的研究记录。旧报告与旧文献原件不修改。它补上具体 ζ(7) 候选从 Fricke/Eichler 恒等式到有理系数 holonomic 系统的接口，并证明实际循环秩为 8。**尚未得到 ζ(7) 的新无理性证明**；完整共同解析映射及严格 CDT 秩矛盾仍未闭合。这里的结构结果是项目内推导，未作全球新颖性声明。

## 1. 已闭合的真实周期输入

[周期触发器证明](cdt_odd_period_trigger_20261005.md)固定
\[
\begin{split}
480F={}&4E_8(\tau)-2288E_8(2\tau)+46332E_8(3\tau)\\
&-146432E_8(4\tau)+185328E_8(6\tau)-82944E_8(12\tau),\\
A={}&E_6(\tau)-1728E_6(12\tau),\qquad
f=\sum_{n\ge1}a_nq^n/n^7,\quad F=\sum a_nq^n,\\
\Theta={}&209\zeta(7)/432,\qquad H=A(f-\Theta).
\end{split}
\]
A、F 的 Fourier 系数都是整数，A 的常数项为 −1727，a_1=4。
令 Wτ=−1/(12τ)，真实变换为
\[
f(\tau)+12^3\tau^6f(W\tau)=\Theta(1+12^3\tau^6),\qquad H(W\tau)=H(\tau).
\]
此式包含 L(F,1) 的零乘极点残差；不能把它误删成零。变换来自实际收敛 Mellin 积分以及[Beukers 原文 Proposition 1.2](../literature/beukers1987_modular_irrationality.pdf)，印刷 p.273 / PDF p.4。

目标接口是：ζ(7) 假定有理，才使 H 成为有理系数芽；真实误差 H 的 Fricke 分支抵消则无条件成立。后面不能把 q 变量模形式直接当作 D-finite 函数。

## 2. 明确 Γ₀(12) Hauptmodul，避免使用错误的四尖点群

定义
\[
h(\tau)=\frac{\eta(\tau)^3\eta(4\tau)\eta(6\tau)^2}
{\eta(2\tau)^2\eta(3\tau)\eta(12\tau)^3},\qquad x=h^{-1}.
\]
按 divisors (1,2,3,4,6,12)，h 的 eta 指数为 (3,−2,−1,1,2,−3)。
其权为零，两个模性和为 −24、24，乘积 \(\prod d^{r_d}=1/144\) 是有理平方。
Newman 模性判据与 Ligozat 尖点阶公式可见
[Rouse–Webb 原始论文 §1](../literature/rouse_webb2014_eta_quotients_v3.pdf)。
六个尖点 c=1,2,3,4,6,12 的阶依次为 (1,0,0,0,0,−1)；
η 在上半平面无零，故 h 恰有一个简单极点。它给出 X₀(12) 到 P¹ 的一次映射，因此确为 Hauptmodul。

其它尖点值可精确得到，而非靠数值识别。对每个 c≠12，求唯一 eta 商 h_c，
使其 divisor 是 [c]−[∞] 且 leading q coefficient 为1。
它与 h 的差是常数；常数由 q⁰ 系数决定。结果为
\[
h(0)=0,\quad h(1/2)=-6,\quad h(1/3)=-4,\quad
h(1/4)=-3,\quad h(1/6)=-2,\quad h(\infty)=\infty.
\]
全部指数向量与模性条件在证书中记录。
η 的 S 变换直接给
\[
h(W\tau)=12/h(\tau),\qquad x(W\tau)=1/(12x(\tau)).
\]
这里没有假定 Zagier Case F 的表中参数就是 X₀(12) 的一次 Hauptmodul；
其额外对称群需另查。[Zagier 原始表](../literature/zagier2009_apery_like_recurrences.pdf)，PDF p.8，是参照而非本坐标的替代证明。

由 eta 乘积，
\[
x=q+3q^2+7q^3+15q^4+30q^5+\cdots\in q+\mathbb Z[[q]],
\]
其反演 q(x) 同样整系数。

## 3. Fricke 商与真实分支

取
\[
t=\frac1{h+12/h+8}=\frac{x}{1+8x+12x^2}.
\]
它满足 t(Wτ)=t(τ)，且
\[
t=q-5q^2+11q^3-21q^4+46q^5+\cdots,\qquad
q=t+5t^2+39t^3+371t^4+3922t^5+\cdots
\]
均为整系数。此商在 q=0 未分歧，不能套用 CDT 另一种 x² 对称迹的分母翻倍公式。

尖点分成三对：
\[
(\infty,0)\mapsto0,\quad (1/2,1/6)\mapsto\infty,\quad
(1/3,1/4)\mapsto1.
\]
两分支值为
\[
\alpha=\frac{2-\sqrt3}{4},\qquad \beta=\frac{2+\sqrt3}{4},\qquad
\Delta(t)=1-16t+16t^2.
\]
正虚轴上的实际固定点 τ=i/√12 对应 α。H 的局部 w 展开在 W:w→−w 下为偶函数，
故 H(t) 真正穿过 α。β 对应共轭的 Fricke 路径，额外 Eichler 周期多项式没有被上述恒等式消除，仍保留。
H 也不是整个 Γ₀(12) 上的单值模函数。

## 4. 二阶 Picard–Fuchs 系统：先证极点界，再认证有限系数

令
\[
S=q\frac{d\log x}{dq},\qquad Y=\sqrt{S(q(x))},\qquad Y(0)=1.
\]
S 是权2模形式；Hauptmodul 无内部临界点，所以 S 在上半平面非零。
在 H 上可固定平方根。Y 与 τY 在解析延拓下张成二维系统，Wronskian 为
\[
Y^2\frac{d\tau}{dx}=\frac1{2\pi ix}.
\]
因此其方程是
\[
Y_{xx}+\frac1xY_x+Q_x(x)Y=0.
\]
模性保证 Q_x 是有理函数。四个其它有限尖点 x=−1/2,−1/3,−1/4,−1/6 处，
Y 的局部形状是 \(\sqrt{x-x_c}(a+b\log(x-x_c))\)，故 Q_x 的双极主部为1/4。
在0它至多有简单极；在∞有 \(Y\sim a+b\log x\)，所以 \(Q_x=O(x^{-3})\)。
写
\[
D(x)=(1+2x)(1+3x)(1+4x)(1+6x)
\]
便得到 \(Q_x=N_Q(x)/(xD(x)^2)\)，deg N_Q≤6。
此先验界使7个精确系数足以认证；额外展开到更高阶是冗余核验。
证书中的显式结果是
\[
Q_x=-\frac{(36x^2+20x+3)(288x^4+324x^3+140x^2+27x+2)}
{4xD(x)^2}.
\]

令 R=A/S³、T=F/S⁴。它们是权零模函数；S 在其它四尖点各有一个简单零，
故 R 的极点阶≤3、T≤4。在∞，R 有界、T=O(x⁻¹)，所以
\[
R=N_R/D^3,\quad\deg N_R\le12;\qquad T=N_T/D^4,\quad\deg N_T\le15.
\]
同样，有限认证的依据是已证的全局极点界。R(1/(12x))=R(x)，T(1/(12x))=−T(x)。

在 Fricke 商 t 上，同一 Y 满足明确二阶方程
\[
Y_{tt}+P(t)Y_t+Q(t)Y=0,
\]
\[
P=\frac{32t^2-24t+1}{t\Delta},\qquad
Q=\frac{(4t-3)(4t^2-5t+2)}{4t(t-1)^2\Delta}.
\]
可直接核对 \(Q(t(x))(dt/dx)^2=Q_x(x)\) 与 P 的变量变换，不依赖小数拟合。
其 Wronskian 是 \(1/(2\pi it\sqrt\Delta)\)。
这一半整数局部结构保留了两 Fricke 分支，而非把它们先验删除。

## 5. 完全明确的有理七阶非齐次算子

为给出可复现模型，定义两个有理函数
\[
R(t)=\frac{1664t^6-9024t^5+32016t^4-60752t^3+
54552t^2-20220t+1727}{(t-1)^3},
\]
\[
I(t)=\frac{4t^2(7616t^6-27808t^5+19552t^4-18096t^3+
12908t^2-446t+1)}{(t-1)^4}.
\]
它们满足
\[
A=RY^6,\qquad T=(1/x-12x)I(t).
\]
以下有限递推是七阶算子的精确指定，不需要打印冗长的展开系数。
对 j=0,…,6，置 \(v_j=Y^{6-j}Y_t^j\)。由二阶方程，
\[
(v_j)'=(6-j)v_{j+1}-jP v_j-jQv_{j-1}.
\]
令 M 是这个三对角矩阵；将 v 乘 R 后，矩阵变成
\(M_R=M+(R'/R)\mathbf1\)。递推行
\[
c_0=(1,0,\ldots,0),\qquad c_{n+1}=c_n'+c_nM_R.
\]
前7行 c₀,…,c₆ 的三角主元为 \((6)_n=6!/(6-n)!\)，都非零。
解唯一有理关系 \(c_7=\sum_{i=0}^6\ell_i c_i\)，定义
\[
\mathcal L_A=\partial_t^7-\sum_{i=0}^6\ell_i(t)\partial_t^i.
\]
其齐次解空间恰为 \(A\tau^j,\ j=0,\ldots,6\)。

Bol 变换或直接最高阶系数给
\[
\mathcal L_{6,x}(S^3f)=T/x^7.
\]
转到 t 后 \(x t'(x)=t^2(1/x-12x)\)，再作 R gauge，得到
\[
\boxed{\mathcal L_AH=\mathcal L_A(Af)=
U(t):=\frac{R(t)I(t)}{t^8\Delta(t)^3}\in\mathbb Q(t).}
\]
这一步也可不借二阶显式式而独立检查下降：
W 将 \(A\tau^j\) 送到 \((-1)^{j+1}12^{3-j}A\tau^{6-j}\)，
所以唯一 monic 七阶齐次算子对 W 固定；
\(t'(1/(12x))=-12x^2t'(x)\)、R 的偶性与 T 的奇性使强迫项严格固定。
故它是七阶有理商系统，不是盲目二次 pushforward 得到十六阶。

U 非零，所以
\[
(\partial_t-U'/U)\mathcal L_A H=0
\]
给出有理八阶齐次上界。R 的零以及将方程齐次化时 U 的零可能引入表观奇点，
它们不等于函数本身的新奇点；原几何真正标记仍须按0、1、α、β、∞逐一处理。

## 6. 未消去尖点给实际秩下界：恰为8

对 cusp 1/2，取 γ=(1 0;2 1)，width=3，局部变量
\(q_c=\exp(2\pi i\tau_c/3)\)。精确常数为
\[
(A|_6\gamma)_0=26/27,\qquad (F|_8\gamma)_0=-476/81.
\]
Bol 恒等式说明 \(f|_{-6}\gamma\) 含非零七次多项式项，
其最高系数是 \( (F|_8\gamma)_0(2\pi i)^7/7!\)；
其余 Fourier 积分是周期函数，加上至多六次多项式。
减去 ΘA 只修改六次以下项。于是 H 的局部最高对数项是
\[
-\frac{1547}{630}(\log q_c)^7,
\]
非零。由于 t 在该 cusp 有简单极，改用 t 时最高项为
\[
\frac{1547}{630}(\log t)^7.
\]
这与明确 forcing 的
\(\lim_{t\to\infty}t^7U(t)=12376=7!\cdot1547/630\)
精确相符。

八个 monodromy translates 首先是在 **C 常数系数意义**下独立：
若一个次数≤7的平移多项式使它们相消，其作用到最高的七次对数多项式
要求在特征值1处有八重零，因此该多项式只能为零。
它们都是任何有理齐次 annihilator 的解，故此算子阶至少8。
结合上一节的八阶上界，H 的最小有理齐次算子阶 **恰为8**；
也就是实际 C(t) 循环导数秩8。若 ζ(7) 假定有理，同一 Q(t) 系统也恰为8。

因此自然评估行可取
\[
1,\ H,\ \theta_tH,\ldots,\theta_t^6H.
\]
这里的秩不是形式周期数量，不靠重复同一低阶系统免费增加。

## 7. 完整算术成本：原点未分歧，没有免费降层

[触发器 §7](cdt_odd_period_trigger_20261005.md)证明：f、Af 的完整前缀分母
在除固定素数外精确支付 \(L_N^7\)。因为 t(q)、q(t) 是双向整数三角变换，
前缀共同分母不变；假定 Θ有理只增加固定分母。

更强的是所有充分大素数 p：
\[
v_p([t^{p+1}]H)=-7,\qquad
p^7[t^{p+1}]H\equiv-2016\pmod p.
\]
这是 A₁a_p 的唯一最高层；整数反演造成的其它 p 项至少多一个 p。
任意固定 \(n^e\) 在 n=p+1 都是 p-unit，不能清掉这七层。
一般 fixed rational differential image 的最高 residue packet 是
\(4\,P(A)\)；目标保留且非有理的行仍有七层。
Sym⁶ 的 SL₂ monodromy 不可约，保证其非零元素不能成为有理函数。
完整论证与范围见[预算报告](cdt_odd_holonomy_budget_20261005.md)。

对自然秩8系统，七个目标行安全型为 \(L_{n+O(1)}^7\)，一行1无分母。
它的主成本为
\[
\tau^\flat=\frac{7(3+5+\cdots+15)}{8^2}=\frac{441}{64}=6.890625.
\]
这也是此 target-preserving fixed-basis 接口的必要主成本；
不外推到所有新增背景、不同周期构造或新 holonomy 定理。
同一行的 e 指数不能把最高七层替换为廉价的 n⁷ 型。

不能把 A 的整数系数导数直接作免费背景使用：A 单独仍在 α 的商路径上
有权因子导致的分支，不能与已经穿过 α 的 H 共用原先期望的未分歧解析叶。
新增背景须重新检查独立性、每行分母与同一映射下的全部叶。

## 8. 一个完整的具体覆盖／背景组合排除

预算分支进一步证明：在自然八行后加入任意有限数量
\(T_j=(-\log(1-t))^j/j!\)，实际秩为8+r；允许自然各行的全部固定
\(n^e\)/LCM类型及排序，其成本仅 flat 部分就满足
\[
\tau^\flat>43/10\qquad(r\ge0).
\]
这是全r的有理不等式证明，不是检查一些小r后猜测；完整界见
[预算报告 §5.4](cdt_odd_holonomy_budget_20261005.md)。
范围是这些自然行，不声称任意混合基或所有其它背景的最小成本。

CDT 固定原文 Appendix A 的函数
\[
h_2(q)=-256q\prod_{n\ge1}(1+q^n)^{24}
\]
有 \(|h_2'(0)|=256\)，标记的阶2分支值为4。
因此对具体试验族
\[
\varphi(z)=(\beta/4)\,h_2(\psi(z)),\qquad
\psi:\mathbb D\to\mathbb D,\quad\psi(0)=0,
\]
即使所有所需叶条件都能满足，Schwarz lemma 仍给
\[
\log|\varphi'(0)|\le\log(64\beta)
=\log(16(2+\sqrt3))<41/10<43/10<\tau.
\]
精确上界可由 \(16(2+\sqrt3)<60<\exp(41/10)\) 证明。
故**此覆盖族加任意数量连续纯对数幂**连 CDT 的正分母门槛也不能通过。
不能把它改写成所有 admissible 映射或所有 arithmetic holonomy 方法的不可能结论；
它使下一步选择更具体：改覆盖、改背景，或改完整整数周期模型。

## 9. 证书、未闭合要求与下一项数学任务

[精确脚本](cdt_odd_level12_model_20261005_verify.py)与
[JSON](cdt_odd_level12_model_20261005_verify.json)记录：
六尖点 eta 阶与单极点单位、整数反演、Q/R/T 的先验度数认证、
商坐标二阶方程和所有有理恒等式、35阶安全系数、预先固定七个素数的最高 packet、
cusp 常数及 log⁷／forcing 常数的精确相符。
脚本还实际执行七阶算子的 Laurent 递推，在指数 −7 至14逐项核对
\(\mathcal L_AA=0\)、\(\mathcal L_A(Af)=U\)。固定素数与有限 jet 检查说明脚本执行，
不代替正文的全素数、极点界和 Bol 证明。

已经闭合的是：
真实 ζ(7) 周期触发器 → 整数模坐标 → 合法七阶非齐次／八阶齐次系统
→ 实际循环秩8 → 完整七层算术接口。

仍欠的目标条件是：
(1) 明确 admissible φ，检查 α 的所选叶、β 的分歧、0/1/∞的全部返回路径；
(2) 在这同一 φ 下加入确实独立且成本划算的背景；
(3) 证明严格 \(m>J(\varphi)/(\log|\varphi'(0)|-\tau)\)。
当前没有这个严格余量，不能宣称 ζ(7) 无理，也没有 Lean 新数值定理。

下一项工作应在已给出的有理 t 系统上进行共同叶与背景函数的解析／算术优化，
而非重新扫描 F₈ 的系数或把其临界值消失重新包装成无理性结论。

