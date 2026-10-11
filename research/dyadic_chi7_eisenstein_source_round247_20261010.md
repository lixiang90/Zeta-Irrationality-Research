# 第247轮 χ−7 dyadic 源：实际五行模型与一叶完整 jump

2026-10-10，C。全部数学为纸证。本稿对固定
\[
Y=L(2,\chi_{-7}),\quad
F=E_{3,\chi_{-7},1},\quad
\mathcal E(q)=\sum_{n\ge1}e_nq^n/n^2
\]
支付一个真实 level14 源、全 prefix 整模型、实际五行独立秩和 canonical cusp 的完整关系 jump。其填点必须使用实际二重 cusp 参数；同一 base 值的另一叶仍有 log²。没有合法全图或 strict holonomy 预算，没有新数值无理性定理。

## 1. 实际函数、微分驱动与有界去重

(D1) 固定 χ=χ−7，χ(2)=1，q=e^{2πiτ}。定义
\[
R(q)=\mathcal E(q)-2\mathcal E(q^2)
=\sum_{m\ge1}\frac{\chi(m)}{m^2}\frac{q^m}{1+q^m},
\quad
H(\tau)=F(\tau)-8F(2\tau).
\tag{1}
\]
恒等式使用 z/(1−z)−2z²/(1−z²)=z/(1+z)，所有重排在 |q|<1 绝对收敛。D_q=q∂q 给 D_q²R=H，系数8包括两次链式微分，不能替成2或4。径向实极限直接由 |q^m/(1+q^m)|≤1 和 ∑m⁻² 支配给
\[
R(e^{-a})\longrightarrow Y/2\qquad(a\downarrow0).
\tag{2}
\]
这一步单独没有支付整个局部 jump。

本人实际完整选读旧218 §§1–5、219 symmetric-power §§1–3及 Catalan gauge §3、220 §§2–4。旧218的原始 Lambert finite part 与 raw-q natural boundary 不等于新式(1)的完整 modular-base 模型；219说明驱动 oldform 必须保留参数和 period powers；220明确 direct CDT 不以 Betti/Hodge 实现为先决条件，但完整关系补点与同对象整模型必须实际给出。246 E13 只关闭 level7 指定全纯两源 family，不能外推到当前 level14 的 H。本稿不重命名这些既有资产。

## 2. 同一 degree-three 代数曲线上的真实 forcing

(D2) 沿用246已核的实际函数
\[
u=u_7(\tau)=(\eta(7\tau)/\eta(\tau))^4,\quad
u_2=u_7(2\tau),\quad
f=\eta(\tau)^3\eta(7\tau)^3,\quad P=1+13u+49u^2,
\]
\[
F=f(1+8u),\qquad
\mathscr L=P^2\delta^2-2u(1+16u+49u^2),\quad \delta=u\partial_u,
\quad \mathscr LA=0 .
\tag{3}
\]
这里 A 是固定 Yang weight-one period，native A(0)=1。

对 γ=(a b;c d)∈Γ₀(14)，矩阵 (a,2b;c/2,d)∈Γ₀(7)，因此 F(2τ) 变换为同一 weight3、χ(d)；holomorphic cusp 条件也由这个 degeneracy 拉回保留。H 是 M₃(Γ₀(14),χ) 中 native∞消失的实际形式。官方 [Stein degeneracy 定义](https://wstein.org/books/modform/modform/newforms.html#atkin-lehner-li-theory)用于核参数约定；Eisenstein 的 character 与 cusp 拉回在上述矩阵上直接检查，没有把只述 cusp forms 的定义误当附加证明。

(D3) 取真实模单位
\[
Z=\frac{f(2\tau)}{f(\tau)}
=q\prod_{n\ge1}(1+q^n)^3(1+q^{7n})^3\in q\mathbb Z[[q]].
\tag{4}
\]
在 level14，eta 指数按 δ=1,2,7,14 为(−3,3,−3,3)；加权和为24、反向加权和为−24，乘积为64且 weight0。因此246已亲读的 Newman–Ligozat 模单位 statement 给 Z 在 X₀(14) 上 meromorphic、H 中无零极点、字符 trivial。定义
\[
h=H/f=1+8u-8Z(1+8u_2).
\tag{5}
\]
三个函数 u₂、Z、h 均属于 X₀(14) 的实际函数域；f 的无 H 零保证没有额外 interior poles。它不是原 t 的 rational forcing 猜测。

(D4) Γ₀(7) 在 mod2 的像为 SL₂(F₂)：T 和 U₇=(1 0;7 1) 的像给上下 elementary generators。Γ₀(14) 正是其中 c=0 的 subgroup 的逆像；故
\[
[\Gamma_0(7):\Gamma_0(14)]=3.
\tag{6}
\]
由已核的 u 是 X₀(7) 的 degree-one 坐标，X₀(14)→P¹_u 的 degree 正是3。紧化曲线、degree 与函数域的标准对应采用 [Loeffler 作者讲义](https://warwick.ac.uk/fac/sci/maths/people/staff/david_loeffler/teaching/modularcurves/lecture_notes.pdf) PDF3–5、8–10的完整所用页；不用假设 X₀(14) 为 genus0。

在下节 cusp0 参数 w 中，u 有 pole2 而 Z 有 pole1。因此 Z∉C(u)；prime degree3 迫
\[
C(X_0(14))=C(u,Z),\quad [C(u,Z):C(u)]=3.
\]
它也有 Q 定义：u(q)、Z(q) 的 Laurent/Taylor 系数均 rational。给任一有限 degree bound 的代数关系，所有 q 系数等式是有限未知量上的 Q 线性方程；无限方程的 row rank 由某有限子集实现。因此已存在的 C 系数 degree3 关系可取 Q 系数。又 Z 不在 C(u)，故其最小式在 Q(u) 上仍 degree3。u₂、h 在 C(u,Z) 的有界 rational expression 同理下降到 Q(u,Z)。这里使用先付的函数域 degree，而不是有限头拟合来证明代数性。记
\[
\mathcal F=\mathbb Q(u,Z)=\mathbb Q(X_0(14)),\quad
\Phi(u,Z)=0,\quad \deg_Z\Phi=3.
\tag{7}
\]

## 3. 实际 connection 与全 prefix 整模型

(D5) 取真正的补偿函数
\[
S_g=A(q(u))(R(q(u))-g),\quad T_g=\delta S_g.
\]
同一 Yang 变化常数公式适用于实际 primitive (1)，给
\[
\boxed{\mathscr LS_g=uP h,\qquad
\delta T_g=\frac{2u(1+16u+49u^2)}{P^2}S_g+\frac{u h}{P}.}
\tag{8}
\]
驱动是式(5)的 actual H/f；g 不改变 forcing。

基于最小式(7)，
\[
\delta Z=-u\Phi_u/\Phi_Z\in\mathcal F,\qquad
\delta Z^2=2Z\,\delta Z.
\]
将它们和 u h/P 按 basis 1,Z,Z² 唯一展开，便给出明确规则定义的 rational 5×5 connection，frame 为
\[
\boxed{(1,Z,Z^2,S_g,T_g).}\tag{9}
\]
矩阵在 Q(u)，只有有限个 pole。未展开 Φ 或猜出一个 scalar operator，不妨碍有限 derivative span 的严格证明；每行均 holonomic。此时先得 rank≤5，确切独立性在§6支付，不能仅由矩阵尺寸领取。

(D6) 使用有限整坐标
\[
x=\frac{u}{1+7u},\quad u=\frac{x}{1-7x}\in x\mathbb Z[[x]],
\quad \delta=x(1-7x)\partial_x.
\tag{10}
\]
u(q)∈qZ[[q]]首项1，故 q(u) 为整数逆级数；复合 q(u(x)) 仍整数。由(1)，R 的 qⁿ系数为
\[
\frac{e_n-8\,1_{2\mid n}e_{n/2}}{n^2}.
\]
于是对每个 N、0≤k≤N，固定 b∈Z_{>0}、bg∈Z 时，
\[
[x^k](1,Z,Z^2)\in\mathbb Z,\qquad
b\,d_N^2[x^k]S_g,\ b\,d_N^2[x^k]T_g\in\mathbb Z.
\tag{11}
\]
δ 是整数 polynomial operator，不调用 N+r 之外的原系数；任意固定 δ-jet 也用同一 full prefix bound。普通 ∂x-jet 若从完整函数取系数则需相应 shifted prefix，不能混淆。式(11)保留所有素数及 prime powers，未声称最小 LCD、joint index 或 free coordinate-energy transport。

## 4. canonical cusp0 的完整收敛 jump

(D7) 固定到达叶：τ=iy，y↓0；置
\[
z=-1/(14\tau),\qquad w=e^{2\pi iz}=e^{-\pi/(7y)}.
\]
这是 Γ₀(14) cusp0 的 local uniformizer。Eta S 的完整函数变换及246已核的 Fricke 规范给
\[
u=\frac1{49u_7(w^2)},\quad
u_2=\frac1{49u_7(w)},\quad
Z=\frac{f(w)}{8f(w^2)},\quad
A(\tau)=-\frac{\sqrt7}{\pi}\log w\,A(w^2).
\tag{12}
\]
其中 f(w)=w−3w²+O(w³)、u₇(w)=w+4w²+O(w³)，来自收敛 native 级数。因而式(5)给
\[
h(w)=\frac1{7w}+O(1).
\tag{13}
\]
w⁻² 系数实际相消；w⁻¹ 系数为1/7。这个相消是 modular transformed driver 的全函数结论，不能只从数值极限或 leading Tate 名称领取。

(D8) 令 U=u₇(w²)、ϑ=w∂w。由 u=1/(49U) 得
\[
\delta=k(w)\vartheta,\quad k=-U/(wU'),\quad k(0)=-1/2,
\quad \frac uP=\frac{U}{1+13U+49U^2}.
\]
k 为 analytic even unit。将(8)除 P²，再除 k²，得到
\[
[\vartheta^2+a(w)\vartheta+b(w)]S_g=c(w),
\quad a,b\in w^2\mathbb C[[w^2]],\quad
c(w)=\frac47w+O(w^2).
\tag{14}
\]
所以 forcing constant 为0，indicial polynomial 为 λ²。

这里可以直接付收敛。选 analytic particular p(0)=0；n≥1 的 Taylor pivot 是 n²。若 a_j、b_j、c_j 有 C R⁻ʲ 的 Cauchy 界，取 ρ<R 使相关 Σ_{j≥1}2C(ρ/R)^j<1/2，递推的 (n−j)/n²、1/n² 均≤1，归纳得 |p_n|≤Mρ⁻ⁿ。故 p 收敛且 p₁=4/7。相同递推给 normalized homogeneous v₀(0)=1。式(12)的精确 period identity 表明 v₀=A(w²) 且 v₀log w 也是 homogeneous 解，两者构成完整 basis；它不是只指定 leading exponent。因此任意 actual S_g 在该叶唯一写为
\[
S_g=p(w)+\alpha_gv_0(w)+\beta_gv_0(w)\log w .
\]

(D9) 由 S_g/A=R−g、式(2)和(12)，沿正实 w↓0 有
\[
\beta_g=-\frac{\sqrt7}{\pi}(Y/2-g).
\]
逆时针 w-loop 给完整函数身份
\[
\boxed{\Delta_0 S_g=-2i\sqrt7(Y/2-g)\,A(w^2).}\tag{15}
\]
因此 g=Y/2 时 S_g、T_g 在本 cusp uniformizer 上全纯；1,Z,Z² 在此亚纯。反向若 S_g 在此亚纯，其 finite-power/log 增长和非零 v₀ 要求 β_g=0。这个关系敏感比较保留明确 Dirichlet 数值 Y。

(D10) 式(10)、(12)还给
\[
x-1/7=-w^2+O(w^4),\qquad
S_{Y/2}(w)=\alpha v_0(w)+(4/7)w+O(w^2).
\tag{16}
\]
所以 native base x 上仍有非零 half-power；Z∼1/(8w)亦有 half-power pole。支付的是实际 e=2 cusp-cover 上的填点，不是 base x 的普通解析点。不得把 ordinary scalar zero 或径向极限改名为未经 ramification 的 complete branchfill。

## 5. 同一 base 值的另一实际叶仍有 log²

(D11) 从 native q-disk 先旋转再沿 q=−e⁻ᵃ 到达 cusp1/2。偶 m 项有界；奇 m 项给
\[
aR(-e^{-a})\longrightarrow
-\sum_{m\ {\rm odd}}\frac{\chi(m)}{m^3}
=-\frac78L(3,\chi)\ne0.
\tag{17}
\]
支配由 a/(e^{am}−1)≤1/m 给出，L(3,χ) 的绝对收敛 Euler product 为正。

取 γ=(4 1;7 2)∈Γ₀(7)，χ(2)=1。τ=1/2+ia/(2π) 时 τ'=γ⁻¹τ∼2ia/π；A 的 Fricke 变换与 native A(0)=1 给
\[
A(\tau)\sim\frac{\pi}{\sqrt7\,a}.
\]
因此对每个固定 g∈C，
\[
S_g\sim-\frac{7\pi}{8\sqrt7}L(3,\chi)a^{-2}.
\tag{18}
\]
cusp scaling σ=(1 0;2 1)、width7 给 local w₁=e^{2πiσ^{-1}\tau/7}，
\[
\log w_1=-\frac{\pi^2}{7a}-\frac{\pi i}{7}.
\]
其非零最高 log² 系数为
\[
-\frac{343}{8\sqrt7\pi^3}L(3,\chi).
\]
这不是以 asymptotic 代替 full germ：H 在该 cusp 全纯、f 的 pulled-back vanishing order为1，故 h 至多 pole1；u 也 pole1，式(8)归一化后的 forcing analytic。其 regular-singular indicial double zero 的收敛 log²/log/analytic 三层递推，与§4的 n² majorant 同样闭合。式(18)确定完整最高层非零。齐次 A 只有一级 log，任何 g 及有限 ramification 均不能删除该 log²。

(D12) cusp0 对 u∞ 的 ramification 为2，而 cusp1/2为1：后者 Γ₀(14) 和 Γ₀(7) 的 cusp width 均为7。其总和等于 cover degree3，故这就是 u∞ 的全部 fiber，也同投 x=1/7。本稿既给一条 actual 填叶，也给同值另一条 actual 未填叶。没有从后一叶推出每个合法 φ 都必到它：全图的 chosen lift、return monodromy、所有实际 preimages 尚待检查，不能把 existence-of-bad-leaf 换成 all-maps no-go。

## 6. 确切五行独立秩与可用的 literal type

(D13) 由(18)及收敛局部展开，S_g 不属于 meromorphic 函数域 F_C=C(u,Z)，所以也不属于其三维 C(u) 向量块。令
\[
V=F_C+C(u)S_g+C(u)\delta S_g .
\]
F_C 在 δ 下稳定，(8)使 V 稳定；V/F_C 是非零 cyclic quotient，被原二阶 \mathscr L 杀。246已自含核过 \mathscr L 在 C(u)[∂u] 不可约，故这个 quotient 恰为rank2。于是(9)的五个实际函数对 C(u)、也对 Q(x)独立，**actual full-frame rank=5**。不需先证明 forcing 的 derivative closure 本身生成全部 F；也没有用“矩阵有五行”代替独立性。

(D14) 在 g∈Q 的假设下，固定 b 清除 g 后，整型(11)给合法单列 literal array
\[
(0,0,0,2,2),\qquad
\tau=\frac{2(7+9)}{25}=\frac{32}{25}.
\tag{19}
\]
这是全五行同 x-coordinate、同 all-prefix 来源的 coefficient type，不是 raw covolume 或未证最优联合费用。因全行 holonomic，若另付同一 holomorphic φ:(D,0)→(C_x,0)，所有实际拉回单值亚纯，且
\[
\log|\phi'(0)|>32/25,\qquad
\frac{J(\phi)}{\log|\phi'(0)|-32/25}<5,
\]
才有直接 CDT contradiction。这里没有计算、声称或继承任何 capacity、energy、derivative gain。

## 7. 首关结论与读域/运行账

新付资产是 level14 actual driving field、finite-coordinate全prefix、actual m5，以及明确 Y 的 canonical ramified whole jump。与246单level7 log²障碍相比，driver constant 在指定 cusp 相消，确实改变了局部源结构；但另一同值叶还留 log²，完整合法图仍未付。下一项必须是这五行的实际共同 lifted 图及目标敏感 whole-leaf 条件，不能直接启动 prime/parameter/map 预算优化或宣称无理性。

本轮没有采用 Root 尚待单独审计的 Mellin/Fricke 跨 R/T 公式；§4 jump 为独立 Frobenius 纸证。完整实际 source identity/全图费用与∞非零未相互借用。主 goal 仍为新的 ζ/L 数值结论，当前未 complete。

primary 新保存2件：Loeffler 官方21页 PDF及 Stein 官方 HTML；仅读前者物理PDF3–5、8–10完整六页，后者完整 degeneracy 定义选段；未声称全部原著 FULL。具体版本、旧稿完整 section 范围及历史 Fricke 输入见同目录 dual_reading_scope.md。数学程序/CAS/样本/扫描/Lean：0；外 Git mutation：0；旧稿/246冻结档/主进展/政策/manifest写入：0。最终保存后实际 FULL 作者自读并登记 bytes/SHA。

