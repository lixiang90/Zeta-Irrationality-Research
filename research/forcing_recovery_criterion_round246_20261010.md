# 第246轮：实际forcing恢复、非分裂有理扩张与目标敏感源

2026-10-10，C。本文给完整的两向准入判据，并在现有Yang level-7实际L值源上核对非恢复及whole-jump校准，另证固定holomorphic-source的rigidity。旧level-7非分裂、rank3/5、多项式forcing两class与Mellin常数均已有冻结证明，不重命名为第246轮新成果。本轮新增范围是一般实际恢复/非恢复准入、完整局部取消条件与第8节的固定全纯源限制；不是新的ζ/L数值无理性或线性无关性结论。只创建本稿及dual_reading_scope.md；数学程序/CAS/扫描/旧producer/Lean/外Git写入均0。

## 1. 实际函数空间与一般恢复定理

(G1) 令K=C(z)，∂=d/dz，R=K[∂]。所有函数均为同一连通延拓面的指定实际germ；定义
\[
 M_f=\operatorname{span}_K\{\partial^jf:j\ge0\}.
\]
“恢复”指存在一个固定的R∈K[∂]给实际函数身份f=Rh，允许其有理系数有pole，不表示Taylor/算术费用免费。微分模是实际函数子空间，不能以形式算子阶数代替其维数。

若f的最小monic算子L阶数m且不可约，则映射R→M_f、Q↦Qf的kernel为左理想RL，故M_f≃R/RL简单。证明只需Ore除法：任何含RL的左理想对应L的右因子；不可约性排除中间理想。

(G2) **实际非零forcing恢复定理。** 若M_f简单，J∈R且w=Jf≠0，则M_w是M_f的非零微分子模，所以M_w=M_f；存在P∈R使
\[
 \boxed{f=P(Jf).}
\]
特别若L_0s=Jf，便有f=P L_0s。J算子非零不足以领取此结论：J可能在Ann(f)中，必须核实际Jf≠0。

此桥可作有限、精确的审查。把∂^kJ按L右余式展开
\[
 \partial^kJ\equiv\sum_{j=0}^{m-1}O_{kj}(z)\partial^j
 \pmod{RL},\qquad0\le k<m.
\]
则O∈Mat_m(K)可逆。若前m个w-导数有依赖，最早依赖会使较早导数的span对∂封闭，产生维数<m的非零子模，与简单性矛盾。因此
\[
 f=e_0^{\mathsf T}O^{-1}(w,\partial w,\ldots,\partial^{m-1}w)^{\mathsf T}.
\]
这给一般的实际observability矩阵，不依赖finite Taylor猜测。若L、J的系数在Q(z)，则上述余式、O与O⁻¹也在Q(z)，恢复身份自动保留该系数域；没有另添任意复常数。245的P正是同一机制的一个具体证书。

(G3) 对任意非恒定全纯盘图φ，s∘φ亚纯且f=Ps，则
\[
 \partial_z\mapsto(\phi')^{-1}\partial_w
\]
给f∘φ亚纯。φ′的孤立零点及有理系数的拉回只产生允许的亚纯pole。于是已证的背景合法图cap可以转移给实际forcing源。这里不推算术分母、basis高度或新坐标费用；复杂代数/非线性商也未由本命题覆盖。

## 2. 有理forcing下真正的非恢复证书

(G4) 假设L∈K[∂]不可约、阶数m≥2，A≠0满足LA=0，B是指定实际解
\[
 LB=r,\qquad r\in K^\times,\qquad S_g=B+gA,\quad g\in C.
\]
再付一个可检验命题：
\[
 \boxed{\nexists c\in K:\ Lc=r.}\tag{NR}
\]
则对每个固定g，M=M_{S_g}含r、因而含整个K。方程LS_g=r把dim_K M限制为≤m+1。M/K非零，否则S_g∈K与(NR)矛盾；其生成元S_g modK被L消去，因此是简单R/RL的非零quotient，必与之同构。得到实际exact sequence
\[
 \boxed{0\longrightarrow K\longrightarrow M_{S_g}
       \longrightarrow R/RL\longrightarrow0,\qquad
       \dim_KM_{S_g}=m+1.}\tag{1}
\]

(G5) (1)不分裂。若有补模U，写S_g=v+c、v∈U、c∈K。Lv=r−Lc同时属于U和K，故为0，给Lc=r，矛盾。因此
\[
 \boxed{A\notin M_{S_g},\qquad
 \nexists P\in K[\partial]:\ P S_g=A.}\tag{2}
\]
事实上M_A简单且维数m，与K相交0；若它嵌入M，投影到M/K便为同维数同构，强制分裂。这是实际函数非恢复证明，既没有把形式quotient当作实际源，也没有从rationalforcing的一条方程直接推(2)。

此证明给一个必要诊断：在这些假设下，实际恢复A必然要求r有rational particular。(NR)是充分非恢复条件；存在particular不自动证明恢复某个指定A，还要核实际函数身份。

(G6) 单凭“LB有理”会误判。选任一非零c∈K使r=Lc≠0，令B=A+c；则
\[
 LS_g=r,\quad S_g=c+(1+g)A,\quad
 A=\frac{S_g-c}{1+g}\quad(g\ne-1).
\]
又1=r^{-1}LS_g，所以右式确为固定有理微分作用于S_g，背景恢复真实存在。g=−1时源只剩c，此特例也说明不能把generic g代替每个固定g。

(G7) 在(NR)下，M仅有子模0、K、M。若N∩K=0且N向M/K投影非零，会给分裂；若N含K且投影非零，则N=M。故任何固定P∈K[∂]的非有理输出C_g=P S_g都仍生成完整m+1维M，且仍不能恢复A。一个形式rank-m quotient不能借此变成较小的实际标量函数；反之，此结果没有禁止另构新的相对周期、非线性对象或degree-growing整投影。

非恢复只排除这一类固定有理线性微分身份，**不保证某个大图合法**，不自动给strict CDT收益，更不是所有解析约束都消失。

## 3. 一个明确L值源：Yang的level-7实际对象

(G8) 复用Yang固定v1的实际参数，q=e^(2πiτ)、θ=t∂_t：
\[
 f(\tau)=\eta(\tau)^3\eta(7\tau)^3,\qquad \kappa=L(f,2),
\]
\[
 t=\left(\eta(\tau)^4/\eta(7\tau)^4+14+
             49\eta(7\tau)^4/\eta(\tau)^4\right)^{-1},
\quad A=1+2\sum_{j\ge1}(j/7)\frac{q^j}{1-q^j},
\]
\[
 L=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),
\quad LB=t(1-t),\quad B(0)=0,\ [t]B=1.
\tag{3}
\]
Lemma1及其完整variation proof给实际齐次basisA、τA、B=AΣc_jq^j/j²；Example2明确给
\[
 \boxed{B-\kappa A\text{ 在 }\sigma=1/28
        \text{ 可延拓为完整单值全纯germ}.}\tag{4}
\]
这是原文声明，不是由系数比limit推fill。本次亲读原PDF5–6、15–16全部文本。旧完整source/独审记录也全文读取，但不继承其余primary页域。[Yang固定原件](https://arxiv.org/abs/0709.1968v1)。

## 4. 该例的不可约与非恢复自含纸证

(G9) 普通导数形式为
\[
 p_2=t^2(1-t)^2(1-28t),\quad
 p_1=t(1-t)^2(1-42t),\quad p_0=-2t-4t^2.
\]
四点均regular singular，local exponents为
\[
 0:(0,0),\quad\sigma:(0,1/2),\quad
 1:(1/3,2/3),\quad\infty\ (v=1/t):(0,1/2).
\tag{5}
\]
例如1处indicial为−27α(α−1)−6；∞令y=t^d时最高系数−14d(2d+1)，故d=0或−1/2。

若二阶L在C(t)有一阶右因子，其非零解y有rational log-derivativey′/y。Regular-singular性排除该log-derivative的高阶finite poles及polynomial part，否则y有指数型不规则增长。ordinary点的residue只能为非负整数zero order；三个finite奇点的residue各为(5)中的一个非负exponent，且1处必≥1/3。因此全部finite residues之和>0。另一方面，在∞有y=t^{-β} times非零analytic series、β∈{0,1/2}，所以y′/y的1/t系数为−β≤0；rational部分分式的同一系数正是finite residues之和，矛盾。故L在C(t)不可约。这里没有将formal二阶或一般container当不可约证明。

若有rational c满足Lc=t(1−t)，ordinary finite pole的最高二阶导数不可抵消；三个finite singular点的negative integer pole exponent均不在(5)，也不可能。故c为polynomial。degree d≥1的最高t^(d+3)项
\[
 -14d(2d+1)[t^d]c
\]
非零，不可能等于degree2的forcing。constant c则需−2c=1与−4c=−1同时成立，矛盾。这支付(NR)。

于是(1)–(2)给**全部g∈C**的实际rank3及固定有理微分非恢复。对g∈Q，真实tuple可取(1,S_g,θS_g)，不是generic g证书；在g=−κ的关系假设也继续成立。该结论补强旧实际rank论证的准入解释，不声称重获新L值定理。

## 5. 该例确有完整目标响应，不只是非恢复

(G10) 还需确认(4)不是一个没有背景jump的普通值身份。令Wτ=−1/(7τ)，τ₀=i/√7。Yang的Hauptmodul给t(Wτ)=t(τ)、t(τ₀)=σ及这里的order2 elliptic uniformizer。

记G₁=(qdt/dq)/t，g₀(t)=t/((1−t)(1−28t))；原文A=G₁²g₀/f。Eta的principal-root变换
\(\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau)\)
由[DLMF23.18.5–7](https://dlmf.nist.gov/23.18)取(a,b,c,d)=(0,−1,1,0)给出。因此
\[
 f(W\tau)=(-i\sqrt7\,\tau)^3f(\tau),\quad
 G_1(W\tau)=7\tau^2G_1(\tau),\quad
 A(W\tau)=-i\sqrt7\,\tau A(\tau).
\tag{6}
\]
最后等式先在分母非零处成立，再全纯续接至τ₀。

q₀=e^(−2π/√7)<1/8（2π/√7>9/4，exp(9/4)>8），故Lambert式给
\[
 |A(\tau_0)-1|\le2q_0/(1-q_0)^2<16/49<1.
\]
所以A(τ₀)≠0；在(6)微分，W′(τ₀)=−1，得
\[
 A'_\tau(\tau_0)=i\sqrt7\,A(\tau_0)/2\ne0.
\]
t−σ是τ−τ₀的二阶uniformizer，故A(t)的half-power项非零，
\[
 \Delta_\sigma A=(t-\sigma)^{1/2}a(t-\sigma),\quad a(0)\ne0.
\]
与(4)合并，对S_g=B+gA有实际whole-germ身份
\[
 \boxed{\Delta_\sigma S_g=(\kappa+g)\Delta_\sigma A.}\tag{7}
\]
这是真正的目标关系敏感局部源；它不强制恢复A。然而只填所指定nativeσ叶，其他reachable叶和全图margin没有因此支付。

若固定P使C_g=P S_g非有理，则PΔA≠0：否则ΔA是不可约L的非零解，P在RL中，PS_g有理，矛盾。因此这类非有理输出仍保留(7)的完整目标jump，同时按(G7)保留rank3；不能借固定微分过滤免费降秩。

## 6. 新数值门槛与止损条件

(G11) Level-7的κ并非本轮新数值目标；旧冻结文献核验已将其作为已知超越值处理，本轮不重认证RWZ/Schneider原文。它是“rationalforcing、实际非恢复、完整关系补点”的校准，不能因通过本关自动恢复该旧标量路线。

一个明确但尚未支付的跨权重目标仍是1、κ、log2的关系。旧试验
\[
 B-(u+v\log(1+28t))A
\]
在κ=u+vlog2时仍有jump
\[
 -14v\,a(0)(t-\sigma)^{3/2}
       +O((t-\sigma)^{5/2}),\quad v\ne0.
\]
因为log′(1+28t)|σ=14；这只是延迟branch，未消除。其L-forcing还含非零A/A′，按(G2)会恢复背景；不能把旧log模板当新的有理forcing源。

真正待构造对象C须指定实际Q-Taylor germ、LC=r_C∈Q(t)、完整费用，并满足
\[
 \Delta_\sigma C=\log2\,\Delta_\sigma A
\]
的完整germ比较，才使B−uA−vC在所假关系下fill。没有这样的实际C或其它明确新ζ/L源时，不进入地图/分母优化。对任何新源，先付：实际最小模与forcing身份；可检验(NR)/恢复测试；完整目标jump；同对象全前缀整模型和合法全图余量。没有要求先取得额外motivic实现才能应用直接CDT，但指定几何周期若被调用必须有实际comparison，不能靠名称替代。

(G12) 本轮停止范围仅为 fixed rational-linear differential recovery/quotient 的偷换与旧log-product复活。未证明新source存在，未证明新的数值LI，也未关闭degree-growing mixed periods、多place判据或所有normal functions。正式全局复盘仍248；结构资产不能重定义总goal完成。

## 7. 两个实际forcing源的完整局部取消及既有第二class

(G13) 令B、C满足同一L的rational forcing，固定同一到达叶和局部正向loop T。必须核的是完整函数身份
\[
 (T-I)B=\kappa_B v,\qquad (T-I)C=\kappa_C v,\qquad
 v\ne0,\quad\kappa_C\ne0.                                  \tag{8}
\]
κ为常数，v是同一个完整homogeneous germ，不是只把leading coefficient、点值或不同normalization作比。若B、C的增广方程在此regular singular（或已独立付有限power/log增长），则
\[
 \boxed{B-gC\text{ 局部亚纯}\quad\Longleftrightarrow\quad
        g=\kappa_B/\kappa_C.}                               \tag{9}
\]
证明：取消全部jump等于T(B−gC)=B−gC；局部基本群由此loop生成，所以实际germ单值。单值且有限power/log增长者乘足够大的整数幂局部有界，可去，故亚纯；反向亚纯必有零jump。若还需要全纯，必须另排掉负整幂pole。式(9)仅是这一到达叶的条件，不能复制到所有reachable叶。

普通点上L及forcing均analytic时所有解原本analytic，故没有新的关系补点。若forcing有pole，ordinary点也可能出现primitive-log jump；其向量必须实际计算，不能因homogeneous T=I便删除。对regular-singular点，homogeneous T−I秩1也不自动保证两条affine jumps都在其image：共振forcing可能附加fixed homogeneous方向的log。式(8)是需要支付的完整输入。

(G14) 一个直接可审的充分局部模型是：homogeneous basis为m−1条meromorphic germs和一条s^αa(s)、α非整数，且两forcing各有meromorphic particular。将实际B、C分解到这个basis，唯一非亚纯分量的常数为κ_B、κ_C；在共同jump规范v=(e^(2πiα)−1)s^αa(s)下(8)随之成立。不能只比两个quotient的端点值。

在当前level-7的σ处，p₂=s a(s)、p₁=b(s)、b(0)=a(0)/2≠0。任意在σ analytic的forcing都有analytic particular：任给y₀，Taylor递推对n≥1的最高系数为a(0)n(n−1/2)≠0；解析系数的Cauchy界和选足够小ρ使Σ_{k≥1}C(ρ/R)^k<1/2给|y_n|≤Mρ^{-n}的归纳majorant，故级数收敛。homogeneous basis是analytic germ和s^{1/2}a(s)，没有共振log。因此两条polynomial forcing的跳跃确共用唯一完整half-power通道；其κ仍须由完整connection formula确定。

(G15) 此处已有第二源，不能当新发现。本人实际完整选读旧
cdt_odd_level7_polynomial_extension_classes_20261007.md §§2–7：
\[
 t\mathbb Q[t]/L(\mathbb Q[t])
   =\mathbb Q[r_B]\oplus\mathbb Q[t^3],\quad LB_3=t^3,
\]
\[
 \Delta_\sigma B_3=C_3\Delta_\sigma A,\quad
 C_3=4\pi^2\int_0^\infty y f(iy)
              \frac{t(iy)^2}{1-t(iy)}\,dy.
\]
它已有全D_n²模型、actual joint rank5及whole-germ比较。旧
cdt_level7_explicit_third_kind_split_20261007.md §§1–2、6–7又给
\[
 \rho=-ft,\quad
 C_3=\mathcal I(\rho)+1/6-\kappa/3,\quad
 \Delta_\sigma B_\rho=\mathcal I(\rho)\Delta_\sigma A.
\]
这些精确周期名和有理常数保留，但未将C₃或I(ρ)识别为所需ζ/Dirichlet/Hecke L值。普通Σ[q^n]ρ/n^s甚至没有右收敛半平面，不能凭Mellin记号领取L(ρ,2)。式(9)可应用于B、B₃的κ/C₃，但不会凭它自动给新的ζ/L目标。本轮没有重审旧pole/residue全部proof或把其既有PV逃逸当新数值收益。

## 8. 固定全纯模源的严格一维限制

(G16) **Holomorphic-source rigidity。** 对当前原参数t，设R∈C(t)在t=0 regular、R(0)=0，并定义同一实际weight3源
\[
 h_R=f\,\frac{R(t)}{t(1-t)}.
\]
若h_R在整个H全纯，则
\[
 \boxed{R=c\,t(1-t),\quad h_R=c f.}                         \tag{10}
\]
若R∈Q(t)，则c=R'(0)∈Q。

证明：eta的收敛非零Euler product使f=η³η7³在H无零，故v=h_R/f=R(t)/(t(1−t))在H无pole。t为Γ₀(7)与Fricke invariant，v是weight0 modular function。Γ₀(7)的两个cusps为∞、0；在∞有t=q+O(q²)，Fricke把0送∞且保持t，所以两cusps均t→0。R的指定条件使v的t0极点可去。于是v延至compact X₀(7)的全纯函数，最大原则给v=c；t非constant，得到(10)。同时f在两个cusps的local order各1，h_R也vanish；这不是借未经核验的dimension公式。

该限制排除本family中新造独立holomorphic Eisenstein/cusp integrand的捷径，却不关闭meromorphic R的新CM poles、其它坐标、level、character/marking、源的full relative comparison或其它CDT metric。旧B₃、ρ恰有interior poles，所以不与(10)矛盾。它只是固定family的精确方向gate，不是所有rationalforcing的no-go。

实际读域及运行账见literature/forcing_recovery_sources_round246_20261010/dual_reading_scope.md；最终保存后全文自读并报bytes/SHA。

