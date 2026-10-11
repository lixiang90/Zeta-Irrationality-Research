# 第227轮：同源全处缩放不变性与 Taylor-paid 总预算

2026-10-08，B。固定225–226的实际 \(\Delta/\Xi/J\)，只新增本稿及227来源记录。数学程序 **0**。新纸面结果是全部有限处同时参与的乘积公式半径界，以及两行、三行安全数组在明确图类中的严格负总margin；另支付任意同源 scalar/unit normalization 的全处协变。没有证明全部 primitive 模型、真实p-adic亚纯延拓或 ramified arch 图都失败。

## 1. 同一个实际源与所用接口

假设 \(\zeta(7)=g\in\mathbf Q\)。记
\[
 D(z)=\sum_{n\ge0}\Delta_nz^n,\qquad
 H(z)=gD(z)+X(z)=\sum_{n\ge0}J_nz^n.
\]
225完整basis稿P2、P11–P14及目标径向稿R1–R5已支付：
\[
 \limsup|J_n|^{1/n}=T,\quad H\notin\mathbf C(z),\quad
 \operatorname{rank}_{\mathbf Q(z)}(1,H)=2,\quad
 \operatorname{rank}_{\mathbf Q(z)}(1,D,H)=3.
 \tag{B1}
\]
其中 \(M=L_1L_2L_3\)，\(T=L_1L_2q_*\)，\(q_*\in\{\kappa,s\}\)，\(M>T>24^9\)。目标单叶图导数至多 \(4/T\)；保留D的共同单叶图至多 \(4/M\)。这是实际原径向分支的结果，不是形式leading products的猜测。

原系数整性为
\[
 64^3d_{2n+4}^{\,6}\Delta_n\in\mathbf Z,\qquad
 64^3c_gd_{2n+4}^{\,13}J_n\in\mathbf Z.
 \tag{B2}
\]
固定 \(c_g\) 清g的分母，所有素数幂及2均保留。由固定p上 \(v_p(d_{2n+4})=O(\log(n+2))\)，H的每个p-adic Taylor radius \(R_p\ge1\)。不能把这个下界变成半径的上界。

对完整合法数组与全部place图定义
\[
 L=\sum_v\ell_v,\quad \ell_v=\log|\phi_v'(0)|_v,\qquad
 E=\sum_{v\mid\infty}E_v+\sum_{v\nmid\infty}e_v,\quad
 e_v=\sup_{z\in T_v}\log|\phi_v(z)|_v,
\]
\[
 \mathcal M_m=m(L-\tau)-E.
 \tag{B3}
\]
正CDT strict入口需要 \(L>\tau\) 且 \(\mathcal M_m>0\)。本文只上界这个同一对象的margin；不把ICM Theorem2.6含近似参数的式子直接设空指标、制造 \(0/0\) 应用。全处 \(L/E\) 是完整§2.3 slopes计算中的实际两项。绝对值按field degree归一，不另加一遍local weights。

## 2. 所有固定素数的 Taylor 内容不能独立累加

**B4（乘积公式半径预算）。** 设 \(a_n\in\mathbf Q\) 有无限非零项，
\[
 \limsup|a_n|^{1/n}=T\in(0,\infty),\quad
 Q_na_n\in\mathbf Z,\quad Q_n\in\mathbf Z_{>0},\quad
 \limsup_{n\to\infty}\frac{\log Q_n}{n}\le\sigma.
\]
若各p的Taylor radius \(R_p\ge1\)，则
\[
 \boxed{\quad B_{\rm Tay}:=\sup_{P\ {\rm finite}}\sum_{p\in P}\log R_p
       \le\log T+\sigma.\quad}
 \tag{B4}
\]
这里半径按 \(|p|_p=p^{-1}\) 取值。无需选一个素数尺度或扫描。

证明：对有限P及任意 \(\epsilon>0\)，半径公式保证充分大的全部非零 \(a_n\) 满足
\[
 \sum_{p\in P}v_p(a_n)\log p
 \ge n\sum_{p\in P}\log R_p-\epsilon n.
\]
同时 \(\log|a_n|\le n(\log T+\epsilon)\)、\(\log Q_n\le n(\sigma+\epsilon)\)。非零整数 \(Q_na_n\) 的绝对值至少为其P部分，所以
\[
 n\sum_{p\in P}\log R_p-\epsilon n
 \le\sum_{p\in P}v_p(Q_na_n)\log p
 \le\log|Q_na_n|\le n(\log T+\sigma+2\epsilon).
\]
沿无限非零指标取极限再令epsilon趋0。若某 \(R_p=\infty\)，先用任意有限候选半径即得矛盾，故上述证明也排除这种情形。各 \(\log R_p\ge0\)，有限子集sup已包含所有处的可能正贡献。

应用B2与 \(\log d_N=N+o(N)\) 的PNT成本，H可取 \(\sigma=26\)。更一般，下节合法宽度 \(2+\epsilon\) 的13列给 \(\sigma_H=26+13\epsilon\)。固定前缀常数不改指数。这是一个**已知安全清分母上界**用于控制全部正内容之和，不是最优联合格必要费用。

## 3. 明确的全部有限处图类与严格总cap

**B5（Taylor-paid图类）。** 所有arch图单叶，且拉回同一完整源亚纯；所有finite图在closed unit disc邻域解析、取0为0、导数非零，并除有限处外为identity。每个finite图的Gauss/image半径满足
\[
 r_v:=\sup_{T_v}|\phi_v|_v\le R_{H,v}.
 \tag{B5}
\]
右侧是H的Taylor radius，采用相同normalized绝对值。此条件支付H的open-disc全纯pullback；三行模型还要求D同盘亚纯，不能免费删D。允许任意满足B5的nonlinear finite图，并不限于affine图。

非arch最大值原理给 \(|\phi_v'(0)|_v\le r_v\)，所以
\[
 e_v\ge\ell_v,\qquad m\ell_v-e_v
 \le(m-1)e_v\le(m-1)\log R_{H,v}.
 \tag{B6}
\]
univalent arch图由完整CDT Theorem2.7.1的证明给 \(E_v=\ell_v\)。设其原变量cap为 \(4/C\)，则按全部arch embeddings归一
\[
 \boxed{\quad
 \mathcal M_m\le(m-1)\bigl(\log4-\log C+B_{\rm Tay}\bigr)-m\tau
 \le(m-1)\bigl(\log4-\log(C/T)+\sigma_H\bigr)-m\tau.
 \quad}
 \tag{B7}
\]
B4使任何有限正处集合的预算同时受控。数域扩张不会复制该预算：原有理H在每个 \(v\mid p\) 是同一芽，normalized weights之和为1，故 \(\sum_{v\mid p}\log R_{H,v}=\log R_p\)；arch同理。这里没有省掉坏素数。

**B8（目标两行）。** 对每个固定 \(\epsilon>0\)，将B2中的 \(2n+4\) 吸收为 \(\lfloor(2+\epsilon)n\rfloor\)，有限不足指标以一个固定整数清除。两行 \((1,H)\) 的13列为第一行0、第二行 \(2+\epsilon\)，全coeff合法且nested：
\[
 \sigma_H=26+13\epsilon,\qquad
 \tau_2=\frac34\sigma_H.
\]
B7取 \(m=2,C=T\)，得到
\[
 \boxed{\quad\mathcal M_2\le\log4-\frac{\sigma_H}{2}
       =\log4-13-\frac{13}{2}\epsilon<0.\quad}
 \tag{B8}
\]
这排除该实际安全数组、所有arch单叶图及所有Taylor-paid finite图的正入口，不只排除3处某一个map。

**B9（原完整三行）。** 同一个宽度 \(2+\epsilon\) 的表：6列同时支付D/H，另7列只支付H，常数行全0。故
\[
 \sigma_D=12+6\epsilon,\quad \sigma_H=26+13\epsilon,\quad
 \tau_3=\frac{3\sigma_D+5\sigma_H}{9}
       =\frac{166}{9}+\frac{83}{9}\epsilon.
\]
取 \(m=3,C=M\)，B7给
\[
 \boxed{\quad
 \mathcal M_3\le2\log4-\frac{10}{3}-\frac53\epsilon
                    -2\log(M/T)<0.
 \quad}
 \tag{B9}
\]
即使放松成 \(M\ge T\)，仍严格负：\(e^3>16\) 由其0至5次正Taylor和直接可见，故 \(2\log4=\log16<3<10/3\)。B8/B9没有把极限安全表假装成省去有限prefix的literal数组。

## 4. 任意同源scalar/unit的全处协变范围

**B10（全family运输，超出226指定linear例）。** 固定一个完整K系数源 \(f_i\) 及合法 \(S'\)-integer LCM数组，令 \(f_{i,c}(x)=f_i(x/c)\)，\(c\in K^\times\)。保留全部行、target relation与denominator表。扩大 \(S'\) 到包含c的非unit处，scaled coefficients仍是同一 \(S''\)-integer数组，\(\tau\)不变；此处不宣称literal \(\mathcal O_K\) 的最优数组不变。

给任意合法scaled family \(\phi_{c,v}\)，置
\[
 \psi_v=\phi_{c,v}/c,\qquad
 f_{i,c}(\phi_{c,v})=f_i(\psi_v).
\]
各source pullback、近似条件的domain radii \(\rho_u\)、meromorphy、函数域rank及holonomicity保持。局部精确有
\[
 \ell_v(\phi_c)=\ell_v(\psi)+\log|c|_v,\qquad
 E_v(\phi_c)=E_v(\psi)+\log|c|_v
 \tag{B10}
\]
（finite用 \(e_v\)，arch用双积分）。乘积公式因此给
\[
 L(\phi_c)=L(\psi),\quad E(\phi_c)=E(\psi),\quad
 \mathcal M_m(\phi_c)=\mathcal M_m(\psi).
 \tag{B11}
\]
这不要求arch单叶，也不要求finite affine。

须处理“almost all maps为identity”而非漏掉无限多unit处：在原family的有限例外集、\(S'\)及c非unit处之外，\(\phi_{c,v}=z\)、\(|c|_v=1\)，故 \(\psi_v=z/c\) 的局部L/E都0。原LCM型系数在这些处有Taylor radius至少1，可把 \(\psi_v\) 改为identity，原source仍全纯，0局部项不变。在包含近似目标的有限S中不作此替换。反向从原family构造scaled family并同样rectify即可。因此在这种 \(S'\)-integer对象中，**全部合法families的可达 \(L,E,\rho,\mathcal M\) 集合相同**，而不只是某个选定transport无收益。

代数unit只重分配arch模长；全处相同margin不变。扩域时，若原源仍是同一rational packet、local map类别不随conjugate改变，normalized local权重合为原权重，独立选各embedding图亦不复制最优预算。新的projector、不同conjugate源或新的primitive/literal数组不满足这里“同一完整对象、同一数组”的量词，须另付。

B8/B9在scaled对象中的正确表述是：先由B10拉回原坐标，再要求该原family满足B5及arch单叶。不能因scaled Taylor radius可能小于1而硬把另一套identity maps塞进B8。

## 5. 真正可能跨过此gate的最小新条件

Taylor radius与**meromorphic continuation radius**不同。H可在Taylor圆上有poles，允许亚纯图越过它；B4不控制这种更大圆，也不控制有限处ramification消branch。B8/B9不能替代真正的p-adic延拓证明。同行A的native A7在3处半径结论也不自动继承到D/H，本文不作该移植。

一个具体可审的新入口是只在3处付过圆延拓。令 \(R^{\rm mer}_3(H)\) 为原canonical H在centered p-adic disc上的真实亚纯半径。arch取affine图 \(az\)，\(|a|<1/T\)，3处取 \(bz\)，此处明确要求 \(b\in\mathbf Q_3^\times\)、\(|b|_3<R^{\rm mer}_3\)，其它finite处identity。此family有 \(E=L\)，而rank2的positive strict条件是
\[
 L=\log|a|+\log|b|_3>2\tau_2.
 \tag{B12}
\]
一个精确可选择的充分条件是实际存在 \(b\in\mathbf Q_3^\times\) 使
\[
 T e^{39}<|b|_3<R^{\rm mer}_3(H).
\]
简单的纸面充分界为 \(R^{\rm mer}_3(H)>3T e^{39}\)：取严格超过 \(Te^{39}\) 的最小 \(3^k\)，它至多为 \(3Te^{39}\)，然后选择足够小的epsilon和足够接近 \(1/T\) 的arch半径使B12成立。仅 \(R^{\rm mer}_3>Te^{39}\) 是连续sup门槛，不保证这个离散值群中有可选b。这里不借未付的扩域补足离散缺口。这是**明确conditional图及费用门槛**，不是已支付的延拓或新数值结论。反之，若仅允许3处positive增益、该处仍限affine图或映像半径不超过这个centered meromorphic radius、arch仍任意单叶，正入口必要
\[
 \log R^{\rm mer}_3>\log(T/4)+2\tau_2.
\]
连暂时放松 \(\tau_2=0\) 都需
\[
 \frac{\log R^{\rm mer}_3}{\log3}>
 \frac{9\log24-\log4}{\log3}=9+\frac{25\log2}{\log3}.
\]
226自然scale的3深度12或21/2不是这种实际半径的upper，也不是足够的positive预算。

因此本轮parking证据明确：继续用原safe数组、arch单叶及finite Taylor映像，纵使全部places同时贡献、再作任意同源scalar/unit运输，均无法通过。下一步须先支付原target过Taylor圆的实际meromorphy、真正改进的joint/primitive数组与对应费用，或C正在研究的有费ramified arch图。本文不排除这些新对象。

## 6. 实际来源、保存与程序账

实际FULL重读225完整basis稿14444B、目标cap5015B、226全处稿13193B及历史dyadic数域稿7862B；只核B1/B2等必要输入，不重复226的delta/norm证明。实际FULL读官方当前CDT ICM PDF3–8的既存完整TXT25090B，及fixed-v2完整Theorem2.5.1/2.7.1/Remark2.11.1选段10820B；没有声称FULL20页或218页、视觉页面阅读或新nilpotence/Frobenius theorem。

这些实际选段精确复制进NEW227来源目录，未修改旧来源，也没有新web/PDF下载。副本与本稿/scope保存后实际FULL复读；精确身份和选读范围见 [227 scope](../literature/pade_all_place_budget_sources_round227_20261008/packet_reading_scope.md)。数学程序、CAS、prime/parameter扫描、PSLQ、recurrence guessing、旧producer复跑均0；文件复制、rg、阅读与hash是文档操作。没有新ζ/L无理性定理，旧稿/main/manifest不改。
