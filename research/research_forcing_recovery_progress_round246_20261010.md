# 第246轮进展：真实χ−7数值源与同类投影的限制

2026-10-10。本轮分类progress，总目标保持active。上一正式全局复盘244，下一次固定248；当前相隔两个完成轮次，本轮战术转向不重置计数。成功标准仍是新的数值无理性或线性无关性定理；本轮尚无这类结论。

## 本轮实际缩小的缺口

245原CM标量源被有理微分恢复强制拉回受限背景，原坐标基本入口已关闭。本轮先分析成功方法的实际源，而后构造不同的Dirichlet响应，没有继续旧图、prime或basis优化。

CDT χ−3的LB=1、LC=1/(1−x)给两个明确数值响应η/2、π²/24，真实关系组合在β=1/9取消同一个完整jump行。单个filled组合不恢复有实际对数jump的HA；三数LI仍需要作者完整14函数和算术能量，不能从一行jump直接领取。Catalan标量源反而恢复反三角背景，其成功投影发生在整个增长列池：整数contact对全部使用列消除ζ₂并保留G，说明非恢复不是所有矩阵方法的必要条件。

对新直接源的前置检查，C给一般实际简单模forcing恢复定理：实际Jf非零且背景模简单时，Jf的导数闭包恢复f。另一方面，不可约LA=0、LB=r∈Q(x)且无有理particular，给实际非分裂rank(m+1)源；任意常数补偿均不恢复A。两方向要求实际函数身份，不从形式阶数或“RHS有理”判断。

固定Yang原t/A的H全纯rational forcing还有严格刚性：驱动h=fR/[t(1−t)]只能cf，因此换此family内的forcing不会给新数值响应。这促使本轮保留Γ₀(7)的两个尖点，使用双覆盖坐标
\[
u=(\eta(7\tau)/\eta(\tau))^4,\quad
t=u/(1+7u)^2,\quad P=1+13u+49u^2.
\]

χ=χ−7、Y=L(2,χ)。divisor论证先付degree≤1，再确定两个系数，得到完整Eisenstein身份
\[
F_\chi=E_{3,\chi,1}=f(1+8u).
\]
其真实二重primitive ℰχ=Σe_nq^n/n²、Bχ=Aℰχ满足
\[
\mathscr L=P^2\delta^2-2u(1+16u+49u^2),\qquad
\mathscr LB_\chi=uP(1+8u),\qquad\delta=u\partial_u.
\]
新源不是旧Hecke κ=L(f,2)。Lambert重排和支配收敛给真实数值出口
\[
\lim_{a\downarrow0}\left(\mathcal E_\chi(e^{-a})-
 L(3,\chi)/a\right)=-Y/2.
\]
u(q)及其inverse整数、A整数、e_n整数，因此d_N²清除Bχ全部prefix和固定δ-jets的分母。纸证算子不可约且没有有理particular，实际(1,Bχ−gA,δ(Bχ−gA)) rank3并对全部常数g不恢复A。这解除245那类恢复前置障碍，但有限部分尚不是完整filled周期投影。

## 使下一步必须改变的障碍

在v=1/u的另一个尖点，新源的完整收敛展开有
\[
B_\chi=(4/49)v_0(v)(\log v)^2+v_1(v)\log v+v_2(v),
\quad v_0(0)=1.
\]
任意gA至多一级log，不能取消它。若固定有理微分Q消除完整log²，则Qv₀=0，不可约性迫Q=T𝓛，输出仅为有理函数。因此单源固定微分过滤同时删除目标通道。

更大的同类全纯池也已分类：任意h∈M₃(Γ₀(7),χ)，native∞消失，必h=f(a+bu)，故只有f与Fχ两个方向。B_h=(a−b/8)B_f+(b/8)Bχ，最高log²系数b/98，有限部分为(a−b/8)κ−bY/16。任何常数线性混合消掉log²时有效b=0，Y函数方向也消失。该整个两源线性逃逸分支停止，不投入247继续微调它。

以上只是明确family、固定微分和常数线性投影的限制；不是所有周期矩阵、所有合法盘图、所有CDT或所有L值方法的不可能定理。尤其∞非亚纯不能直接当成所有有限值盘图的容量cap。

## 接口状态与唯一下一关

|接口|本轮状态|
|---|---|
|明确数值响应|已证Y的真实尖点有限部分|
|实际最小源与不恢复|已证rank3、无有理particular及全g非恢复|
|完整安全整模型|已证全prefix d_N²；未优化|
|关系假设下完整周期投影/补点|未证|
|同对象无限非零|未证|
|全leaf合法图与strict预算|未证|
|新数值无理性/LI定理|未得|

247只给一个有界前置关：对另一Eisenstein e₁=E_{3,1,χ}（常数−8/7）作明确的canonical constant-term处理，写完整双cusp period-polynomial/局部log stack，判定是否存在同时保持native有理Taylor源、取消全部Tate项且保留非零Y方向的实际投影。去常数会改变modularity/forcing，必须重新审实际holonomicity和恢复，不以形式减去log²免费领取。若这固定stack失败，不扩大同类参数，248正式复盘优先比较增长混合矩阵、真正相对周期及其他已识别数值源。

在过关前不扫描maps、primes或LCD，不以更多文档或辅助对象算进展。两个连续轮次不缩小核心缺口即提前查方向；正式248仍比较全部路线与剩余成本，防止局部最优。原ζ奇值总目标没有被Y源或结构引理替换。

## 核验和文献归档

本轮Yang实际选页、Stein官方Eisenstein statement、eta模单位判据等保存于literature/forcing_recovery_sources_round246_20261010；各reader scope区分全载体与实际读域。Root新源final、一般判据及成功源比较经独立纸审；没有Lean认证、数学程序、参数/prime扫描或外部仓库修改。245冻结档不变。本轮一次性producer只做hash、追加本报告及manifest，不执行数学。
