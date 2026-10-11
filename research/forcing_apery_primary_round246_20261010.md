# 第246轮：Yang level7的实际forcing、非恢复与全纯筛选

2026-10-10，A。本稿的主要新筛选结论是：固定Yang例2的t、A，任何在0全纯且R(0)=0的有理forcing，若其variation核在H全纯，则R只能是c·t(1−t)。因此该全纯Fricke模板不能通过换forcing产生新的Dirichlet L(2,χ₋₇)或log出口。已知κ=L(2,η³η₇³)只作校准，不当新数值目标。另付完整函数级证书：B−gA不能有理微分恢复A，与245的JF forcing确有结构区别。未付新数值无理性、全部叶或费用。数学程序0。

## 1. 实际primary数值身份与精确方程

Yang论文正式标题为[Apéry limits and special values of L-functions](https://arxiv.org/abs/0709.1968)，官方唯一v1；不是以“modular forms”为题的另一篇论文。复用原PDF264199 B / SHA256691258e04fb3f9f9fa6a4cc144c8be99d587d0af47f96cbf138ac797a1025109。实际完整选读physical PDF5–11、15–16、18–20：variation Lemma1–2、elliptic方法及完整Lemma3–4证明、例2与完整Theorem2、例4/Theorem4及例5。不将第一次被截断的24页抽取算FULL。

例2定义q=e^{2πiτ}、θ=t∂_t，
\[
 f(\tau)=\eta(\tau)^3\eta(7\tau)^3,\qquad
 t=\left({\eta(\tau)^4\over\eta(7\tau)^4}+14+
 49{\eta(7\tau)^4\over\eta(\tau)^4}\right)^{-1},
\]
\[
 A=1+2\sum_{n\ge1}\chi_{-7}(n){q^n\over1-q^n},\quad
 \mathcal L=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2).
 \tag{Y1}
\]
实际恒等式为
\[
 \mathcal LA=0,\quad \mathcal LB=t(1-t),\quad
 B(0)=0,\quad B=t+45t^2/4+\cdots .
 \tag{Y2}
\]
其中B=A E、E=Σ_{n≥1}c_n q^n/n²、f=Σc_nq^n。Yang Theorem2的数值出口是
\[
 \kappa=L(2,f),\qquad b_n/a_n-\kappa=O(28^{-n}).
 \tag{Y3}
\]
这是权3 CM尖点形式的Hecke L值，不是Dirichlet L(2,χ₋₇)。例如其Dirichlet级数的c₂=−3，而χ₋₇(2)=1；这区分级数身份，不证明两个特殊值之间不存在其它恒等式。本项目旧level7记录已处理κ与第三类周期类，本稿不把它或仅改名后的目标作为新的数值出口。所读Yang的Dirichlet实例分别为χ₋₃与χ₋₄，不能由例2免费得到χ₋₈或χ₋₇。

## 2. 数值关系真正补点：完整Fricke核验

记W₇τ=−1/(7τ)。由[DLMF23.18.5–6](https://dlmf.nist.gov/23.18)的eta S变换，在H的既定平方根上
\[
 t(W_7\tau)=t(\tau),\quad
 f(W_7\tau)=i(\sqrt7\tau)^3f(\tau),\quad
 A(W_7\tau)=-i\sqrt7\tau A(\tau).
 \tag{Y4}
\]
最后一式也从Yang完整variation输入直接得：
\[
 A=\left({D_qt\over t}\right)^2{t\over(1-t)(1-28t)f},\quad
 {D_qt(W_7\tau)\over t(W_7\tau)}=7\tau^2{D_qt(\tau)\over t(\tau)}.
\]
因此符号不是猜测或有限q系数拟合。

给Y3所用补点的独立精确核查。设α=2π/√7、E₀(x)=E(ix/√7)，完成L函数α^{−s}Γ(s)L(s,f)在s↔3−s下不变，由Yang Lemma4或Y4的Mellin积分证明。E₀的Mellin式中把Re s=2移至−7/2：只有s=0、−1留残差；s≤−2的Gamma poles由cusp L函数的trivial zeros取消。有限宽水平尾由Gamma指数衰减及L的垂直多项式界消失；此为固定contour，不是数值近似。由完成函数在s=1、2的关系，αL(1,f)=κ。再代s↦−1−s，得
\[
 E_0(1/x)=\kappa-\kappa/x+E_0(x)/x,
\]
先对x>0成立，再在H解析延拓，所以
\[
 E(W_7\tau)-\kappa={i\over\sqrt7\tau}(E(\tau)-\kappa),\qquad
 (B-\kappa A)(W_7\tau)=B-\kappa A.
 \tag{Y5}
\]
W₇固定i/√7，对应t=1/28的二阶elliptic商。B−κA在τ的普通邻域全纯且W₇不变，故其实际native t芽在此全纯，支付真实补点。Y5不说所有其它叶都同时补点，也不以作者的Apéry收敛率代替整数模型或CDT费用。

## 3. Rational forcing确实不允许245式背景恢复

先证明没有R∈C(t)满足𝓛R=t(1−t)。有限ordinary点的pole在最高二阶导数产生不可消去的最高pole阶。其余有限点0、1/28、1的齐次indicial根分别为
\[
 (0,0),\qquad(0,1/2),\qquad(1/3,2/3).
 \tag{Y6}
\]
直接核验：写普通导数系数a=t²(1−t)²(1−28t)、b=t(1−t)²(1−42t)，在1/28有b/a′=1/2；在1有a=−27(t−1)²+…、zeroth=−6+…，给r(r−1)+2/9=0。每个负整数r都不使indicial首项消失，而右端全纯，故这些点也不能有rational pole。于是R为polynomial。若deg R=d≥1，𝓛R的最高项是−14d(2d+1)R_d t^{d+3}，不能等于二次forcing；若R=c，则−2c=1与−4c=−1矛盾。故
\[
 \mathcal LR=t(1-t)\quad\hbox{没有有理解。}
 \tag{Y7}
\]

齐次局部系统由A、τA生成，且不可约：T:τ↦τ+1有唯一不变线C·A，Y4的W₇却把它送到C·τA。两者是实际t monodromy，故没有共同不变线。由此A、θA在C(t)上实际独立，且其rank2微分模块不含常数函数1。

取任意常数g，S=B−gA。𝓛S=t(1−t)使1属于S的cyclic模块；该模块rank≤3，其模常数的商被不可约𝓛杀死。商非零，否则S为有理函数，违反Y7。因此它实际rank3，构成rank2齐次模块与常数模块的扩张。

若某P∈C(t)[∂_t]满足PS=A，则不可约性使整个A模块包含在这个rank3模块中，并与常数线交为0；两者直和等于全部模块。于是S可写为r(t)+u(t)A+v(t)θA。应用𝓛，常数模块与A模块独立，强迫𝓛r=t(1−t)，违反Y7。因此
\[
 \boxed{A\notin\mathbb C(t)[\partial_t](B-gA)\quad
 \text{对任意常数}g.}
 \tag{Y8}
\]
固定g∈Q及假设κ∈Q时取g=κ均包括在内。这证明245的背景恢复机制不适用于此rational forcing；但它本身不是合格新目标、合法大图或严格预算。旧κ/ρ类的存在也不等于新的Dirichlet出口。

## 4. 主筛选定理：同一全纯Fricke模板只剩原forcing

令R(t)∈C(t)在0全纯、R(0)=0，考虑𝓛B_R=R。Yang normalized variation的最高θ²系数为h₀=(1−t)²(1−28t)，其权3核准确等于
\[
 h_R=\left({D_qt\over t}\right)^2{R\over A h_0}
 = f\,{R(t)\over t(1-t)}.
 \tag{Y9}
\]
假设h_R在H全纯。由于t Fricke不变，h_R与f具有同一Γ₀(7)角色和Y4的Fricke乘子。t=q+…、f=q+…，R在0的阶至少1，故h_R在∞ cusp至少一次消失；Fricke把∞换成0 cusp，故在0 cusp也至少一次消失。

Γ₀(7)只有这两个cusps。eta在H无零，所以f在H无零；Y4与其q首项又给f在两个cusps各恰order1。因此h_R/f是X₀(7)上的weight0全纯函数：H内无pole，两个cusps处商有界，在elliptic点的角色也相消。紧性使它为常数。于是
\[
 \boxed{h_R\in\mathcal O(H),\ R(0)=0
 \quad\Longrightarrow\quad R=c\,t(1-t),\ h_R=c f.}
 \tag{Y10}
\]
反向当然成立。R可在别处形式上有pole，本证明没有偷偷要求它是polynomial；条件是实际h_R在H全纯。对R∈Q(t)，c∈Q。这个定理严格关闭“同t/A，仅更换全纯 rational forcing以取得新period”的提案。允许H内meromorphic核、第三类残差、新coordinate/module或不同乘子时，不在Y10范围；旧t³/ρ类属于这些例外，不能把它们当成Y10的新holomorphic出口。

## 5. 为什么Eisenstein χ₋₇提案必须改变上述假设

[Stein作者教材](https://wstein.org/books/modform/modform/eisenstein.html)式(4)、Theorems5.8–5.9给权3、level7、角色χ₋₇的Eisenstein基
\[
 e_0=E_{3,\chi,1}=\sum_{n\ge1}\sum_{d|n}\chi(n/d)d^2q^n,
\quad e_1=E_{3,1,\chi}=-8/7+\sum_{n\ge1}\sum_{d|n}\chi(d)d^2q^n.
 \tag{Y11}
\]
常数−8/7由B_{3,χ}=48/7直接得：χ在1,2,4为+1、3,5,6为−1，三个幂和为−7、−49、−295；代7²Σχ(a)B₃(a/7)。两者的Dirichlet级数分别为ζ(s−2)L(s,χ)和ζ(s)L(s−2,χ)（先在绝对收敛半平面）。因此e₀在s=2的继续值确为−L(2,χ₋₇)/2，给出真正数值身份，而不是f的κ。

但e₀不能同时满足Y9的Fricke乘子及native∞ vanishing：若满足，Fricke会使它在0也消失，成为cusp form，与Stein的Eisenstein/cusp直和及e₀非零矛盾。任意e₀/e₁线性组合若在∞消失，e₁系数须0；因此没有非零Eisenstein组合同时满足这两个条件。加入f也不能拯救非零Eisenstein部分。若直接保留e₁的常数，则二重q积分产生非零(log q)²项，无法由常数gA消去；也不再是R(0)=0的原点全纯B_R。

改用Γ₀(7)而不取Fricke商确实改变前提：其Hauptmodul可取s=(η₇/η)⁴，而t=s/(1+7s)²，Fricke作用s↦1/(49s)。e₀可单独在∞消失，不再要求另一个cusp同时消失。但本稿没有支付该双覆盖上一个B_E/A的whole jump恰为纯L(2,χ₋₇)、π²或log2的完整身份，也没有支付两叶的共同亚纯图及整预算；ζ(s−2)L(s,χ)的Mellin继续值本身不等于elliptic点的Eichler值。Y10不能外推关闭这个新模块，反过来也不能把它当已通过的候选。

## 6. 路线判断与读取账

本轮真正改变行动的是Y10：当前Yang t/A的全纯rationalforcing小改应停止，唯一核重复既有κ。Y8保留一个重要接口，说明rational forcing可能解除背景恢复式，但这不单独提供新数值目标。下一项若准入，必须先给不同模块或meromorphic核的明确新Dirichlet/ζ whole-period jump，而非先投资map或LCM。没有在本稿找到并认证χ₋₈或χ₋₇的新完整数值入口，不以搜索未命中宣称全球未知。

实际范围见本轮alternative_reading_scope.md。数学程序/CAS/素数或参数扫描/Lean/git均0；只有既存PDF选段抽取与NEW文档保存，未重跑旧producer、未变更外部仓库。保存后实际FULL作者复读全文；作者自读不冒充同行独审。
