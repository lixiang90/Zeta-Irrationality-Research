# 六个完整周期积分与五背景的 slow 像交及可计算余核

日期：2026-10-06。本文新建，不修改冻结输入。实际进展是：特征零的六个完整 Af 积分与五个已有背景独立，固定次数1,…,11的精确minor非零；因此除明确有限坏素数外，足够长的slow前缀中两像直接和。另将此前mixed S2条件化为唯一首11系数补正与一个完整tail obstruction。没有证明该obstruction为零，没有取得新的Smith收益或数值无理性定理。

## 1. 实际函数、分支与前缀规范

使用 [完整模型](cdt_odd_level20_model_20261006.md)、[q Bockstein](cdt_odd_level20_cartier_mixed_bockstein_20261006.md)、[五背景packet](cdt_odd_level20_cartier_background_slow_packet_20261006.md) 和 [真实de Rham类](cdt_odd_level20_cartier_cohomology_20261006.md) 的冻结输入。记r²=5、K=Q(r)，固定q=exp(2πiτ)，所有原点积分常数为0。

先取源减号的实际代数级数

\[
 A_-=E_2-4rF_2(4\tau),\quad
 V_-=E_4-5E_4(2\tau)+4E_4(4\tau)
 -\frac{5r}{4}\{F_4-20F_4(2\tau)+64F_4(4\tau)\},
\]
\[
 \theta_q^3 f_-=V_-,\quad f_-(0)=0,
 \quad F_-=A_-f_-,\quad
 N_-=1-(6+r)t+(1+r)t^2,
\]
\[
 C_-=1-(6-2r)t+(6-2r)t^2,
 \quad D_-=(1-t)N_-C_-.
\tag{I1}
\]

这里C₋是A₋的own-zero因子；A₋/S的分母含另一个C₊，没有将二者换用。加号级数是全部代数q系数的共轭。坐标由真实eta identity给出

\[
 h=\eta_4^2\eta_5^2/(\eta_1^2\eta_{20}^2),\qquad
 t=1/(h+1)=q-3q^2+4q^3-7q^4+\cdots.
\tag{I2}
\]

定义两个符号各自的六个完整实际primitive

\[
 \Xi_j^\delta(t)=\int_0^t \frac{v^j}{D_\delta(v)}F_\delta(v)\frac{dv}{v},
 \qquad j=0,\ldots,5,\quad\delta\in\{-,+\}.
\tag{I3}
\]

它们正是q规范中的\(\int B_j^\delta f_\delta\,dq/q\)，因为Bⱼ=QⱼAδS、dt/t=S dq/q。因此这里没有漏乘S。Fδ(0)=0，I3无需减原点残数。

五背景按已冻结定义取

\[
 \mathcal B=(T_3,R,M,Z,I_K),\quad
 T_3=L^3/6,\ R=L\operatorname{Li}_2(t),
\]
\[
 M=\operatorname{Li}_{1,2}(t),\quad Z=\operatorname{Li}_3(t),
 \quad I_K=\int_0^t K_2(v)\,dv/v,
\tag{I4}
\]

其中L=−log(1−t)，平方根(1−t)⁻¹ᐟ²在0取1。Ξ不是共同coarse G叶上的免费新函数：真实等式为Fδ=Hδ+εδΘAδ，这里εδ在δ=−时为1、δ=+时为−1，相应积分的ΘA carrier保留。本文关于它们的独立性和前缀只使用原点实际芽，不将它们加入已有同叶holonomy系统。

## 2. 特征零的实际11列独立

完整模型给三阶非齐次方程\(\mathcal L_\delta H_\delta=U_\delta\ne0\)，齐次解为Aδ、τAδ、τ²Aδ。故\(\mathcal L_\delta F_\delta=U_\delta\)也成立。Fδ−Hδ是齐次Aδ的常数倍，未消尖点处Aδ最多有log²，而Hδ有已证非零log³。因此Fδ保留log³、其实际微分闭包

\[
 W_F=\langle1,F_\delta,F_\delta',F_\delta''\rangle_{\mathbf C(t)}
\]

确为rank4。Uδ非零又使1属于此闭包。其模常数商是此前真实uniformization的不可约rank3 twisted Sym²；这一步没有把三个齐次解当成Fδ的实际函数基。

已证P10背景闭包仅含一维trivial/sign组成因子。稳定交\(W_F\cap P10\)在rank3商上的像若非零，由不可约性就是整个rank3，从而迫该因子出现P10，不可能。因此

\[
 W_F\cap P10=\mathbf C(t)\cdot1,\qquad F_\delta\notin P10.
\tag{I5}
\]

设有实际常系数关系

\[
 \sum_{j=0}^5 c_j\Xi_j^\delta+\sum_{B\in\mathcal B}d_B B=0.
\]

微分后得到\(Q_cF_\delta/t\in P10\)，其中\(Q_c=\sum_jc_jt^j/D_\delta\)。若有cⱼ非零，则Q_c非零，并迫Fδ属于P10，与I5矛盾。故全部cⱼ=0。五背景由已证首五系数unit minor独立，随后全部d_B=0。因此

\[
 \boxed{\Xi_0^\delta,\ldots,\Xi_5^\delta,T_3,R,M,Z,I_K
 \text{在特征零实际原点芽上常系数独立。}}
\tag{I6}
\]

I6不依赖L(3,χ₅)的有理性假设。它也未宣称这11个局部芽本身满足同一完整解析叶条件。

## 3. 固定首11minor：从明确eta与E/F公式独立实现

本次新 [producer](cdt_odd_level20_cartier_slow_intersection_20261006_verify.py) 不import或执行任何旧冻结脚本。它只使用如下精确输入：

\[
 E_{k,n}=\sum_{d\mid n}\chi_5(d)d^{k-1},\quad
 F_{k,n}=\sum_{d\mid n}\chi_5(n/d)d^{k-1},
\]
\[
 E_{2,0}=-1/5,\quad E_{4,0}=1,\quad F_{k,0}=0,
\]

及I1–I2的eta整数积。先预先固定工作order12和minor行次数1,…,11，未尝试第二个前缀、未扫描素数。q(t)由首项1的形式递归取得，Ξⱼ系数由\([t^n]\Xi_j=[t^{n-j}](A f/D)/n\)精确取得。五背景由其卷积/谐和数公式和K₂递推取得。所有运算在Fraction的K=Q(r)二元表示中进行，没有浮点L值。

以列顺序(Ξ₀⁻,…,Ξ₅⁻,T₃,R,M,Z,I_K)、行次数1,…,11记矩阵J₋。完整矩阵和det在新 [JSON](cdt_odd_level20_cartier_slow_intersection_20261006_verify.json) 中保存。单次20项固定检查通过，得到

\[
 \det J_- = a+br\ne0,
\]
\[
 a=\frac{-6282200735810370608941961682373767659469928540257185663705210264094823111}
 {21849778258362324777508772451489525288948203520000000000000000000000000000},
\]
\[
 b=\frac{29849283075167303685051102467708749781350698386842761928658784516293555129}
 {237919807702167536466206633360663719812991549440000000000000000000000000000}.
\tag{I7}
\]

其非零norm已约分，分子为正整数

\[
 \mathfrak n=
 18185128059402095125798657293885020814441811560723828110102552030003090751962161123632363437598689225859892984380857405446711841549680952353121065279.
\tag{I8}
\]

J₊=σ(J₋)，所以detJ₊=σ(detJ₋)，二者norm相同。完整源系数通过I1定义，20项检查另核所有六Ξ的真实系数共轭，未对未知实际周期赋予σ。行列式的非零也独立证明这11个常系数芽独立；I6给其结构原因。

首11系数的分母素因子均≤11：E/F只含固定1/5与1/4，eta双向坐标和D⁻¹整数，f的n³与一次积分的n在此仅有n≤11；五背景同理。故对任意p>11，除p∣\(\mathfrak n\)外，这个minor在K的所有p-place都为unit，无须将大整数完全因式分解才获得一个明确有限排除集。

## 4. 全好剩余域中的两个slow像直接和

取p>11、p∤\(\mathfrak n\)，并保留原mixed primitive/packet所需固定好约化条件。若用于该primitive，仍排29、1049与原有假设period分母等固定坏素数；这里只证明函数minor，p>11已排2、5、7、11。k可为Fₚ²，采用此前relative coefficient extraction/目标twist规范，不能把绝对Cartier的p-root重复加到这里。

令slow保留次数0,…,r，其中

\[
 r=\left\lfloor\frac{N-1}{p}\right\rfloor,
 \qquad 11\le r<p
 \quad(11p+1\le N\le p^2).
\tag{I9}
\]

相应Ξ与背景在degree<p的系数均p-integral。实际target符号可随χ₅(p)改变，两个符号的unit minor保证统一结论。在k[t]/t^(r+1)中

\[
 \dim\langle\bar\Xi_0,\ldots,\bar\Xi_5\rangle=6,
 \quad\dim\langle\bar T_3,\bar R,\bar M,\bar Z,\bar I_K\rangle=5,
\]
\[
 \boxed{\langle\bar\Xi_i\rangle\cap
 \langle\bar T_3,\bar R,\bar M,\bar Z,\bar I_K\rangle=0.}
\tag{I10}
\]

于是此前补正像\(\operatorname{image}(\bar M_p\bar\Xi)+\langle\bar{\mathcal B}\rangle\)的维数在此范围恰为rank\(\bar M_p\)+5，而不是一个未证的上界。此维数指actual slow常系数像，不是新函数rank或已产生的Smith kernel rank。

q慢坐标也成立：t(q)=q+O(q²)使前11行只左乘unit triangular矩阵。整坐标在modp又满足t(q)^p=t(q^p)，故完整fast前缀中的Bockstein身份转坐标后不改变I10。

## 5. 精确且可计算的唯一候选与tail obstruction

在I9范围写11函数列为\(\mathcal U=(\bar\Xi_0,\ldots,\bar\Xi_5,\bar{\mathcal B})\)，令\(\mathcal J\)为实际target符号的首11unit matrix。以下可统一使用slow t坐标；若用slow q坐标，必须同时把全部函数列、ψ及其首11matrix转为q，不能只转换ψ。给任何已计算且ψ(0)=0的slow余项ψ（实际ψc由Ξ(0)=f(0)=0自动满足），定义

\[
 z(\psi)=(\lambda(\psi),\mu(\psi))
 =\mathcal J^{-1}([s^1]\psi,\ldots,[s^{11}]\psi)^T,
\]
\[
 \mathcal T\psi=\psi-\sum_{i=0}^5\lambda_i(\psi)\bar\Xi_i
                  -\sum_{B\in\mathcal B}\mu_B(\psi)\bar B.
\tag{I11}
\]

这里限定ψ(0)=0，与实际ψ_c的规范一致；若输入有非零constant，I12还须另加ψ(0)=0这一必要条件。这不是可任选的补正：首11系数已迫所有11个常系数唯一。\(\mathcal T\psi\)的前11系数恰为0，但更高次数尚未保证消失。由I10，此前constant-c₁+五背景family的mixed S2充要条件严格等价于

\[
 \boxed{\lambda(\psi)\in\operatorname{image}\bar M_p
 \quad\text{且}\quad
 \mathcal T\psi=0\pmod{s^{r+1}}.}
\tag{I12}
\]

因此得到一个canonical obstruction

\[
 \left([\lambda(\psi)]\in\operatorname{coker}\bar M_p,
       \mathcal T\psi\in s^{12}k[s]/s^{r+1}\right).
\tag{I13}
\]

若r=11，tail空间为空，只有有限维coker测试；若r>11，必须完整核所有更高slow系数。首11minor不能把这些tail条件自动删除。

更贴近真实source的q表达是已证

\[
 \psi_c=\sum_i\bar m_{1,i}\bar\Xi_i-\eta_c\bar f,
 \qquad \eta_c=\mathcal U_p(uA),\quad
 m_1=M_p\hat c/p.
\tag{I14}
\]

本稿仍未证明ηc是rational、属于固定允许space或为0。记κ=ηc f并在同一slow q坐标对κ应用I11，则I12等价于

\[
 \boxed{\mathcal T\kappa=0,
 \quad\bar m_1-\lambda(\kappa)\in\operatorname{image}\bar M_p.}
\tag{I15}
\]

κ的背景坐标由唯一μ(κ)提供补正。I15将横向抽取项的完整function obstruction与Hecke的线性coker obstruction分开，但未解决任何一个。此接口允许下一步直接针对ηc f证明或反驳固定span身份，而不是猜测两个像可能有不明交。

## 6. 原source与不重复信用的边界

I12/I15仅分类此前明确family：ĉ→ĉ+pc₁，及五已有background的unit原source坐标gβ，g=Δ²。新I投影g c₀保证原始行primitive，但是否S2仍由I12完整判断。旧三H用已经证的CRT Vr补off-p部分；本稿未扩大其额外horizontal允许像。

背景五列早已在rank19原system内，不再增加actualrank。I10也不允许直接将rankMp+5作为新的Smith收益：baseline1、native kerM、polynomial shifts、source degree及saturation仍须在同一原整格中计。r<11或p∣\(\mathfrak n\)时，本稿不称两像有交，也不称无交；只是此固定minor不能给结论。

本稿未扫描nonordinary素数，不猜CM或密度，不证明ηc f通过I15，不改任何旧冻结报告。特征零的完整carrier与已有coarse叶限制始终保留。

## 7. 固定证书与独立审阅范围

20项检查由作者在本轮新producer单次执行，精确核：eta坐标首项与双向递归、整数性、实际E/F常数/V首项、两个embedding的完整Ξ系数共轭、五背景minor、固定11minor非零及其norm。完整matrix、两个有理det分量及norm在JSON保存。该固定计算不是素数扫描、不是以finite jets证明新holonomy定理。

root本轮实际只读审核全文及producer：实际F保留log³给rank4、rank3不可约商，P10只有一维factor，微分constant关系迫F属于P10而矛盾；审查了eta/E/F、双向坐标、积分系数、有限minor的好素数范围与I12/I15完整tail条件。helper_tensor_budget实际只读审核§§2、4–5及producer规范，限定通过；其提出的ψ(0)=0规范已在§5明示。没有重跑此producer，审阅记录不将有限minor当作S2存在证明或新的算术信用。
