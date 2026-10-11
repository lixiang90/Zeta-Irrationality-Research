# 第238轮：真实填点源的全阶单缺口flag与精确费用子式

2026-10-08，Packet/B。数学程序0。本稿证明真实目标参数下，完整degree-D源的0,…,3D+3 jets全部单射，并给出actual jumps及其费用的全阶余子式选择公式。没有证明临界方阵每阶非零，也没有证明被选余子式的费用upper或新数值无理性。

## 1. 固定真实目标，不能替换成任意有理参数

沿冻结233原生canonical叶及234完整方程，使用
\[
E(u)=\int_0^1\frac{dy}{1-3uy^2}
=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
S(u)=\sqrt{1-4u},\quad
I(u)=\int_0^u\frac{E(s)}{S(s)}\,ds,
\]
\[
J_g(u)=S(u)(g-2I(u)),\qquad
g_0:=2I(1/4)
=\mathfrak t:=\frac52L(2,\chi_{-3})
-\frac{\pi\log3}{3\sqrt3}.
\tag{F1}
\]

这里g₀=𝔱的绑定采用已实际FULL读取的233、234：拉回J_g=H_g(4u/(4u−1))沿0≤u<1/4正是canonical叶；g=𝔱时J_g在1/4解析且值0。由J_g/S=g−2I且I(1/4)有限，其limit必须为0，故𝔱=2I(1/4)。下节也直接证明g=g₀时确有全部解析填点。

以下全阶moment命题固定真实实数g₀。算术source则在**真实目标关系假设g₀∈Q**下取固定正整数b_g，使b_gg₀∈Z，并使用
\[
f=(1,uE,b_gJ_{g_0}),\qquad
\mathscr L_D=\mathbb Z[u]_{\le D}^{\,3}.
\tag{F2}
\]
该假设不同于V∈Q或√3𝔱∈Q。其它参数满足J_g=J_(g₀)+(g−g₀)S，未由本稿的moment证明取得相同all-order flag。

## 2. 完整正moment表示，包含全部原生尾系数

置a₀=atanh(1/2)=(log3)/2。变量r=√(1−4s)给
\[
J_{g_0}(u)
=S(u)\int_0^{S(u)}E((1-r^2)/4)\,dr
=(1-4u)R(u),
\]
\[
R(u)=\int_0^1\!\int_0^1
\frac{dy\,dt}
{1-3y^2/4+3y^2t^2/4-3uy^2t^2}.
\tag{F3}
\]
先在0≤u<1/4取正根推导，再由解析恒等延拓原生芽。这是whole generating identity，不只渐近尾。

令a=3y²/4，x=4at²/(1−a+at²)。对固定a，
\[
t^2=\frac{x(1-a)}{a(4-x)},\qquad
\frac{dt}{1-a+at^2}
=\frac{dx}{2\sqrt{a(1-a)}\sqrt x\sqrt{4-x}},
\qquad dy=\frac{da}{\sqrt{3a}}.
\]
交换正积分，a的范围为x/4≤a≤3/4，得到
\[
R(u)=\int_0^3\frac{w_R(x)}{1-ux}\,dx,\qquad
w_R(x)=
\frac{\operatorname{atanh}\sqrt{1-x/4}-a_0}
{\sqrt3\sqrt x\sqrt{4-x}}>0.
\tag{F4}
\]
该积分在|u|<1/3解析，因此F3也证明J_(g₀)在1/4解析且值0。

定义
\[
d\mu(x)=\frac{dx}{2\sqrt{3x}},\quad 0<x<3,\qquad
v(x)=2\sqrt{4-x}\!
\left(\operatorname{atanh}\frac{\sqrt{4-x}}2-a_0\right),
\]
\[
\mu_\ell=\int_0^3x^\ell\,d\mu=\frac{3^\ell}{2\ell+1},
\qquad \nu_\ell=\int_0^3x^\ell v(x)\,d\mu.
\tag{F5}
\]
因为(4−x)w_R(x)dx=v(x)dμ，完整原生系数为
\[
[u^n](uE)=\mu_{n-1},\qquad
[u^n]J_{g_0}=-\nu_{n-1}\quad(n\ge1),\qquad
J_{g_0}(0)=g_0.
\tag{F6}
\]
v>0在(0,3)，在0仅log增长，在3趋0；这些moments全收敛。分别正性本身不保证两species square determinant非零。

## 3. 正确外cut符号只支付一个缺口

在Ω=C∖((−∞,0]∪[4,∞))上，取√(4−x)>0于(0,4)，并取atanh在此实区间的原生branch。对upper lip：
\[
\Im v_+(t)=
\begin{cases}
-\pi\sqrt{4-t},&t<0,\\
+2a_0\sqrt{t-4},&t>4.
\end{cases}
\qquad
\rho(t):=-\frac1\pi\Im v_+(t).
\tag{F7}
\]
左侧√(4−(t+i0))为正数减i0，atanh的imag为−π/2。右侧该根为−i√(t−4)，atanh(−iy)=−i atan y；乘根后imag为正。故ρ左正右负，不能将两个外cut都当正measure。

**零数lemma。** 对实多项式A、B，deg A,deg B≤m−1，非零H=A+Bv在(0,3)至多有2m个零，按multiplicity计。

证明：若有2m+1个零，选其monic零多项式Z，deg Z=2m+1；H/Z在这些点可去。v的非零cut jump也保证H不可能恒零，除非A=B=0。令k=0,…,m−1，沿两外cut作Cauchy contour：
\[
\int_{(-\infty,0)\cup(4,\infty)}
\frac{t^k B(t)\rho(t)}{Z(t)}\,dt=0.
\tag{F8}
\]
所有边界费用可直接控制：v=O(log z)在0，v=O(√(4−z))在4，故小弧分别为O(ε|log ε|)、O(ε)；在∞，v=O(|z|^(1/2))，大弧为O(R^(k−m−1/2))→0。cut integrand在∞为O(|t|^(k−m−3/2))，端点亦可积。lower lip为upper lip的共轭，jump恰给F8，未忽略额外pole或finite head。

取F8中t^k的线性组合B(t)，得∫B²ρ/Z=0。但奇次数Z在t<0为负，在t>4为正，故ρ/Z在两个外cut**均严格负**。若B≠0，积分严格负；若B=0，非零A不可能有2m+1个零。矛盾，lemma得证。

此证明不能把上界2m减成2m−1：偶次数Z在两cut同正，使ρ/Z异号。它没有支付critical square perfectness，也没有证明该更强命题为假。

## 4. 全D完整jet单射，明确C₀=3

令D≥0、m=D+1。T_N是F2全部3m个monomial tuple列的原生Taylor评价，行0≤n≤N。先取N=3m=3D+3。常数函数的m列在前m行形成identity，在余下全部行均为0。

将uE与J两组monomial列各逆序：j=D−s，s=0,…,m−1。余下行n=m+r，r=0,…,2m，由F6恰为
\[
K_m(r,s,E)=\mu_{r+s},\qquad
K_m(r,s,J)=-\nu_{r+s}.
\tag{F9}
\]
K_m是(2m+1)×2m矩阵；native第三组另乘b_g。此处n−j≥1覆盖全部tail，没有遗漏n=0头或移动jet坐标。

若K_m列相关，便存在非零A+Bv，deg A,deg B≤m−1，满足∫x^r(A+Bv)dμ=0，r=0,…,2m。零数lemma给至多2m个sign changes。以全部sign-change位置构造实多项式q，deg q≤2m，使q(A+Bv)同号且非恒零。μ严格正且端点可积，故该积分非零，与正交矛盾。因此
\[
\boxed{\operatorname{rank}K_m=2m,\qquad
\operatorname{rank}T_{3D+3}=3(D+1)\quad(D\ge0).}
\tag{F10}
\]
这也逐D证明填点源在实系数有理函数域上的实际rank3。g₀∈Q时全部源系数为Q，F10同时是Q上的complete-jet单射。没有把有限D证据或Shidlovsky未知常数当作此全阶证明。

## 5. actual jumps由最大非零下标精确选择

定义δ_h为K_m删去第h行后的2m阶det，0≤h≤2m。F10保证至少一个δ_h非零；left kernel是一维，cofactor vector为((−1)^hδ_h)_h。置
\[
h_*=\max\{h:\delta_h\ne0\}.
\tag{F11}
\]
这是**最大非零下标**，不是最大绝对值余子式。前h_*行独立：否则存在left relation支持于h_*之前，与唯一关系的最后非零坐标h_*矛盾。该关系使第h_*行依赖之前行。以后每行继续增加rank，因为完整matrix仅有这一维left kernel。

前m个tail rows已经独立：其μ-block是正定m×m Hankel，∫p(x)²dμ>0。因此h_*≥m。结合常数列消去，greedy native row flag恰略过一行：
\[
\boxed{V_D=\{0,1,\ldots,3m\}\setminus\{m+h_*\}.}
\tag{F12}
\]
在原生source全部3m列上，前m行constant block为identity，剩余block为K_m删h_*行；列逆序只改变符号。因此
\[
\boxed{\det T_{V_D}=\pm b_g^m\delta_{h_*},\qquad
\mathcal A_D=-m\log b_g-\log|\delta_{h_*}|.}
\tag{F13}
\]
最后一个恒等式正是冻结237同metric、rank1 ordinary graded target下的intrinsic finite fee。b_g固定，其项只有O(D)。

δ_(2m)≠0时critical prefix 0,…,3D+2已经单射；否则actual flag包含最后一行3D+3而缺较早一行。本稿只证明F12，未证明δ_(2m)在全部m上非零。

## 6. 数值接口仍是selected cofactor，不能换成Gram总和

Cauchy–Binet确给
\[
\det(K_m^{\mathsf T}K_m)=\sum_{h=0}^{2m}\delta_h^2>0.
\tag{F14}
\]
它认证all-order rank，却不提供δ_(h*)的下界；最大绝对值minor也不一定是actual flag所选minor。即使取得所有cofactor的实处upper，也只给𝓐_D的lower，不能替代证明严格收益所需的费用upper。

当前实质推进是：真实关系源的zero estimate常数明确为3，actual jumps及其完整原生子式均有全阶公式。未付量收窄为g₀∈Q假设下F11所选δ的全部finite-place/content与leading费用控制，以及与同一合法图真实metric的严格比较。没有从F10、δ平方和、正moment或safe整格index推出数值矛盾，也不扩大为其它目标/源的no-go。

实际读取与执行范围见 literature/actual_flag_sources_round238_20261008/packet_reading_scope.md。只新增本238稿和scope；数学程序0、prime/parameter scans0、旧producer0、新primary检索0；没有改237、旧稿、main或manifest。保存后实际FULL作者复读，身份另报。
