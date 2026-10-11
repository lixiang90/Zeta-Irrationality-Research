# 第246轮：χ−7的真实Eisenstein双覆盖源、有限部分与固定投影障碍

2026-10-10，Root。全部数学为纸证。目标Y=L(2,χ−7)没有被替换成CM尖点形式L(f,2)或未命名第三类周期。本稿取得一个明确Y响应、完整整数模型及实际非恢复源；同时证明其单一常数补偿与固定有理微分过滤不足。没有新数值无理性结论，也没有合法大图或strict预算。

## 1. 保留两个尖点的实际坐标

取q=e^{2πiτ}、χ=χ−7，令
\[
 u=(\eta(7\tau)/\eta(\tau))^4
 =q\prod_{n\ge1}(1-q^{7n})^4/(1-q^n)^4
 =q+4q^2+14q^3+\cdots,
\]
\[
 t={u\over(1+7u)^2},\quad P(u)=1+13u+49u^2,
 \quad f=\eta(\tau)^3\eta(7\tau)^3.
 \tag{E1}
\]
u是X₀(7)的degree-one坐标：eta模单位判据的指数(−4,4)满足和0、乘积7⁴为平方；其cusp矩阵[[7,1],[1,7]]乘指数得(−24,24)。故u在∞为simple zero、在0为simple pole，H内无零极点。Γ₀(7)的两个cusp之外没有divisor；唯一simple pole使它给X₀(7)→P¹的degree1同构。所用模单位判据按Darmon–Daub–Lichtenstein–Rotger作者draft物理PDF14的Definition4.3.1及紧邻Newman–Ligozat statement输入，不声称重证全部上游判据。原件和完整所用页已保存。

Yang的固定A为
\[
 A(q)=1+2\sum_{n\ge1}\chi(n){q^n\over1-q^n},
 \quad L_tA=0,
\]
\[
 L_t=(1-t)^2(1-28t)\theta_t^2
 -14t(1-t)^2\theta_t-(2t+4t^2).
 \tag{E2}
\]
实际所用Yang PDF5–11、15–16完整选段支付变化常数公式、同一A与t、f的weight3/χ及原方程。A与f的字符相同；f在H无零，在两个cusps各vanishing order1。

## 2. 精确Eisenstein身份，不以有限系数猜测

官方Stein书的Definition(4)/Theorem5.8给
\[
 F_\chi(q)=E_{3,\chi,1}(q)
 =\sum_{n\ge1}e_nq^n,
 \quad e_n=\sum_{d\mid n}\chi(n/d)d^2\in\mathbb Z.
 \tag{E3}
\]
它是M₃(Γ₀(7),χ)的全纯形式，∞常数0，头为q+5q²+8q³+⋯。这是所用标准模性输入；书中将一般证明指向Miyake，本文没有认证Miyake全书。

Fχ/f是Γ₀(7)-invariant meromorphic函数。f在H无零，所以这个商无H pole；两个cusps至多simple pole。在∞，Fχ与f均vanish至少order1，商实际上有限。u为degree1坐标，于是商必为α+βu。f=q−3q²+O(q³)，所以商=1+8q+O(q²)。u=q+O(q²)唯一确定α=1、β=8，得到完整函数恒等式
\[
 \boxed{F_\chi=f(1+8u).}\tag{E4}
\]
这里两个系数只在先付的degree bound内确定身份，绝非从有限头宣称无限q-series相等。

Fχ/f不是Fricke-invariant，因为u在W₇下变成1/(49u)。它因而避开同一t/A全纯源刚性定理的hypothesis。u→t是degree2，不能把E4偷偷当成原t上的rational forcing。

## 3. 实际rational forcing与全prefix整模型

定义真实holomorphic native源
\[
 \mathcal E_\chi(q)=\sum_{n\ge1}{e_n\over n^2}q^n,
 \quad B_\chi(u)=A(q(u))\mathcal E_\chi(q(u)).\tag{E5}
\]
由Yang变化常数式和E4，原t算子作用为
\[
 L_tB_\chi=t(1-t)(1+8u).
\]
令δ=u∂u、a=(1+7u)/(1−7u)，则θ_t=aδ。两条精确式为
\[
 p(t)a^2=P^2/(1+7u)^4,
\]
\[
 p(t)a\,\delta a-14t(1-t)^2a=0.
\]
因此乘(1+7u)^4后得到同一个实际scalar方程
\[
 \boxed{\mathscr L=P(u)^2\delta^2-2u(1+16u+49u^2),
 \quad\mathscr LA=0,
 \quad\mathscr LB_\chi=uP(u)(1+8u).}\tag{E6}
\]
u=1/7的原Fricke branch point现在是ordinary点，不再免费提供目标关系敏感补点。

u(q)∈qZ[[q]]首项1，故其inverse q(u)∈uZ[[u]]。A(q)整数，e_n整数，复合和乘积前N项只用原级数前N项。因此令d_N=lcm(1,…,N)，全部N、0≤m≤N和固定r≥0满足
\[
 [u^m]\delta^rA\in\mathbb Z,
 \quad d_N^2[u^m]\delta^rB_\chi\in\mathbb Z.
 \tag{E7}
\]
对g∈Q，bg∈Z时，S_g=Bχ−gA的所有prefix用bd_N²清除。固定常数行1也包括在内。没有仅检查有限素数或猜最小LCD，尚未优化整格。

## 4. 明确Dirichlet数值出口：收敛的有限部分

重排绝对收敛的|q|<1级数，得
\[
 \mathcal E_\chi(q)
 =\sum_{m\ge1}{\chi(m)\over m^2}{q^m\over1-q^m}.
\]
对a>0，设ρ(x)=1/(eˣ−1)−1/x。它在x>0满足−1≤ρ(x)≤0，且ρ(0+)=-1/2。因此
\[
 \mathcal E_\chi(e^{-a})-{L(3,\chi)\over a}
 =\sum_{m\ge1}{\chi(m)\over m^2}\rho(am).
\]
右侧被∑m⁻²支配，故dominated convergence直接给
\[
 \boxed{\lim_{a\downarrow0}
 \left(\mathcal E_\chi(e^{-a})
       -{L(3,\chi)\over a}\right)
 =-{1\over2}L(2,\chi).}\tag{E8}
\]
E5在A非零的局部给Bχ/A=ℰχ，ℰχ本身在H内全纯；E8直接使用这个primitive，不需要额外证明沿imaginary axis的A非零。实际数值响应是Y而非L(f,2)。E8是对已有holomorphic源的真实cusp有限部分，不是把形式Laurent系数命名为新数，也不假装它已成为CDT所需的完整jump投影。

## 5. 不恢复A的实际证书

\mathscr L的有限奇点为0及P的两个根；0指数(0,0)，P根指数(1/3,2/3)，∞指数(0,0)。P根处t=1且t′(u)≠0，故这两组指数也可从Yang E2直接拉回核；∞则由E6的δ²−O(1/u)直接得。

\mathscr L在C(u)[∂u]不可约。若有order1右因子，它的hyperexponential解有有理log-derivative。regular singularity排除高阶pole与∞的exponential polynomial part；ordinary点的residue只能是非负整数zero multiplicity，有限singular点的residue为相应非负指数。两个P根各贡献至少1/3，所以finite residues总和>0；但∞指数0要求它等于0，矛盾。

也不存在y∈C(u)使\mathscr Ly=uP(1+8u)。ordinary点pole的最高导数项不能消；finite singular点的负整数指数均非indicial root，亦排除pole。故y为polynomial。若degree d≥1，左侧最高degree d+4的系数2401d²[y]_d非零，而右侧degree4。若y为constant，左侧至多degree3，也不能匹配。证毕。

实际M=span_C(u){∂^jS_g}含1（因\mathscr LS_g为非零rational function），dim≤3。若A∈M，不可约的rank2模块V=span{A,A′}与K=C(u)相交0，便迫M=V⊕K。这两个微分子模的直和投影与K[∂u]作用交换。分解S_g=v+y并投影\mathscr LS_g=uP(1+8u)，于是\mathscr Lv=0及\mathscr Ly=uP(1+8u)，与上段矛盾；这里没有假定\mathscr L杀死V的所有元素。因此
\[
 \boxed{A\notin C(u)+C(u)[\partial_u]S_g
 \quad(g\in C).}\tag{E9}
\]
同时M/K非零、为不可约order2方程的cyclic quotient，故actual rank3，basis为1,S_g,δS_g。这是本源的实际nonrecovery，不从一句rational RHS领取答案。它通过245的恢复前置检查，但仍不保证目标补点或大图。

## 6. 固定log²与有理微分过滤的精确限制

写v=1/u、ϑ=v∂v。乘v⁴的局部方程为
\[
 [(v^2+13v+49)^2\vartheta^2
      -2v(v^2+16v+49)]B_\chi
 =(v^2+13v+49)(v+8).
 \tag{E10}
\]
右端constant392，indicial operator为2401ϑ²。所以regular-singular收敛Frobenius展开含不可取消的最高项
\[
 B_\chi={4\over49}v_0(v)(\log v)^2
         +v_1(v)\log v+v_2(v),
 \quad v_0(0)=1,
 \quad v_j\text{ 在0全纯},
 \quad\mathscr Lv_0=0.
 \tag{E11}
\]
这里可直接支付收敛而不只写形式首项。令a(v)=(v²+13v+49)²、b(v)=−2v(v²+16v+49)、R(v)=(v²+13v+49)(v+8)，记\widetilde L=aϑ²+b，c=4/49。先取\widetilde Lv₀=0、v₀(0)=1，再递推
\[
 \widetilde Lv_1=-4c\,a\vartheta v_0,\qquad
 \widetilde Lv_2=R-2c\,av_0-2a\vartheta v_1.
\]
两个右端的constant term都为0；后者用392−2c·2401=0。n≥1的Taylor pivot为2401n²，解析系数的局部majorant给三个级数收敛。另加任意齐次解只改变低层log项。因而4/49是完整最高log系数，来自392/(2·2401)，不是仅拟合leading asymptotic。齐次A至多一级log，因此任何g都不能使S_g在∞meromorphic；有限ramification仍留下非零log²。E8的Y有限部分可改变低层响应，却不能改变这项。

还有一个固定投影限制。若Q∈C(u)[∂u]使QS_g的完整log²系数消失，则最高log系数正是(4/49)Qv₀，故Qv₀=0。不可约的order2算子\mathscr L是v₀的minimal annihilator；Ore右除得Q=T\mathscr L。于是
\[
 \boxed{QS_g=T[uP(1+8u)]\in C(u).}\tag{E12}
\]
因此任何这样的固定有理微分过滤同时杀掉整个homogeneous目标通道，不能仅去除log²而留下Y响应。对Q∈Q(u)[∂u]，右侧为Q(u)。没有从此排除growing integer period projectors、多源混合矩阵、所有finite-u合法图或其他判据；尤其所有盘图的值本来有限，∞的局部障碍不能直接外推为全部图的no-go。

## 7. 两源全纯family不能作线性逃逸

还有一个先于扩大pool的精确筛选。任取h∈M₃(Γ₀(7),χ)，在H与两个cusps全纯、native∞消失。与E4同一divisor论证给h/f=a+bu；因此这个完整family恰为span{f,Fχ}，不需要维数公式。

令ℰ_f为Yang的二重q primitive，B_f=Aℰ_f；normalized h源满足
\[
 B_h=(a-b/8)B_f+(b/8)B_\chi.
 \tag{E13}
\]
其∞完整log²系数为(b/98)v₀，因为B_f的forcing uP没有E10右端constant term，故至多一级log。对于此family任意常数线性混合，消去完整log²必须使有效b=0，于是实际驱动源只剩f，目标Eisenstein方向完全消失。

具体地，Yang完整Fricke比较给ℰ_f(q→1)=κ=L(f,2)，E8给h primitive的有限部分为(a−b/8)κ−bY/16；b=0同时删除Y项。这里是明确函数方向的消失，不需要假设κ、Y之间不存在数值关系。故仅增加同一family的第二个全纯驱动源不能逃出障碍。此结论只涵盖上述weight/character/native条件下的常数线性投影，不否定增长的混合矩阵、不同level、meromorphic核或完整相对周期。

## 8. 下一项真正未付的接口

E1–E9给出了明确Y源、rational forcing、全部prefix整模型及实际nonrecovery；不是新的Y无理性定理。原t的全纯Fricke刚性没有关闭这条double-cover源，因为E4不Fricke invariant；代价是原u=1/7处对所有g均ordinary，且新∞有E11。

若继续，必须给一个真正的多源或增长的整数周期投影，消掉完整的固定Tate/log²通道并保留E8的Y通道；只减gA、改固定derivative basis或只减leading asymptotic不足。或者证明另一条完整数值jump及不同合法解析入口。全投影/全leaf准入、同对象无限非零、strict holonomy预算均未付；未过这些接口不做参数/prime/map扫描。

本轮主稿及primary读域另记root_reading_scope.md。官方书/文档只调用明示标准statement；没有从保存全HTML/PDF声称已认证全部原著。没有Lean或外Git mutation，245冻结档未改。
