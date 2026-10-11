# 第234轮：有理新源的真实秩、外国原点图与基本证书容量

2026-10-08，A。实际FULL读取233规范化稿后，对同一新目标
\[
t=\frac52L(2,\chi_{-3})-\frac{\pi}{3\sqrt3}\log3
\]
及J_g(u)=H_g(4u/(4u−1))作一次有界检验。数学程序0。新增的是实际rank、合法共同图及适用于全部这些共同图的容量upper；结论只关闭当前已付安全类型的基本CDT证书，没有新数值无理性定理，也不恢复旧W优化。

## 1. 从实际积分核对方程和rank

令v=1−4u，Z(u)=4u/(4u−1)。冻结递推给L₁H_g=r，
\[
r(z)=\int_0^1\frac{ds}{1-z+(3z/4)s^2},\qquad
L_1=2(1-z)\partial_z-1.
\]
直接积分或对积分分部微分，确有
\[
r'+\frac{1-2z}{2z(1-z)}r
=\frac2{z(1-z)(4-z)}.
\tag{A1}
\]
例如乘2z(1−z)后，右侧为4/(4−z)，其z=0值与r₀=1一致。代入Z的完整积分得到
\[
r(Z(u))=vE(u),\quad
E(u)=\int_0^1\frac{ds}{1-3us^2}
=\frac{\operatorname{atanh}\sqrt{3u}}{\sqrt{3u}},
\]
\[
E'=-\frac{E}{2u}+\frac1{2u(1-3u)},\qquad
J_g'+\frac2{1-4u}J_g=-2E.
\tag{A2}
\]
均取原生0芽，E(0)=1、J_g(0)=g；未删有限头。两方程和1′=0给实际长度3有理连接。

E在u=1/3有非零log，故非有理。若J_g=qE+r₀，q,r₀∈C(u)，比较(A2)中的E及1项，必有
\[
q'+\left(-\frac1{2u}+\frac2{1-4u}\right)q=-2.
\tag{A3}
\]
括号在∞为−1/u+O(u⁻²)。有理q的∞次数d>1时，左端首项为(d−1)q_d u^{d−1}；次数≤0时趋0；次数1的常数首项相消，仍趋0。皆不能等于−2。因此对每个复常数g，
\[
\operatorname{rank}_{\mathbb C(u)}(1,E,J_g)=3.
\tag{A4}
\]
g∈Q时亦为Q(u)秩3。以uE替换E不改变函数秩。这里证明了实际线性独立，未把标量ODE阶数当作rank；与Root234的同一短证独立纸核一致。

## 2. 准确的局部叶和允许的偶阶前像

原z=4、∞、1、0分别对应u=1/3、1/4、∞、0。E在1/3的log系数是非零解析单位；任何有限阶ramification仍产生非零log。因此任何holomorphic φ:(D,0)→(C,0)，若(uE)∘φ meromorphic，都必须遗漏1/3。φ没有pole是CDT图本身的要求。

在原点附近，E的任一输运叶为
\[
E_{\rm nat}(u)+\frac c{\sqrt u},\qquad
c\in\frac{\pi i}{\sqrt3}\mathbb Z,
\tag{A5}
\]
允许sqrt分支改变c的符号。由(A2)，对应J的局部差为
\[
\sqrt{1-4u}\{A-2c\,\arcsin(2\sqrt u)\}.
\tag{A6}
\]
故外国叶c≠0遇到偶阶零点φ=w^{2k}h(w)、h(0)≠0时，E∘φ只有普通pole，J∘φ则解析；这样的前像合法。奇阶且c≠0时E的半整数pole不meromorphic。c=0的原生叶可在任意阶原点前像解析。因此全体合法图没有“0只有唯一前像”的自动条件。

在u=1/4，每个E叶都解析，J局部为解析particular solution加一个常数乘√(1−4u)。233已证明g=t恰填掉指定canonical叶，g≠t在该叶仍有非零平方根。其它叶未免费填好；偶阶mark前像也能消去平方根而不使用目标关系。这些量词须逐图核对。

## 3. 一张实际合法图，有第二个原点前像

在仅用于图构造的p坐标中，置
\[
F(p)=\frac13\tanh^2\sqrt p,\qquad
G(p)=\frac{\sqrt p}{\tanh\sqrt p}.
\tag{A7}
\]
它们都是p的单值meromorphic函数，F(0)=0、F′(0)=1/3、G(0)=1。F的pole在
\[
-\pi^2(k+\tfrac12)^2\quad(k\ge0),
\]
非原点零在−k²π²、k≥1，均为二阶。F从不等于1/3。其1/4前像为
\[
b_j=(\alpha+j\pi i)^2,\quad j\in\mathbb Z,\qquad
\alpha=\log(2+\sqrt3)>0.
\tag{A8}
\]

取一个有界单连通p域Ω，包含0、b₀=α²和−π²；避免F的全部pole、全部b_j(j≠0)及其它非原点零点。存在这样的域：把[0,b₀]与一条从0到−π²、绕过−π²/4的简单弧连接成树，取足够薄的单连通邻域；所避集合离散，正区间不遇其它b_j。此为一次存在性构造，不是域参数扫描。

原生恒等式E(F(p))=G(p)延拓到Ω。令𝒥_g=J_g∘F，则
\[
\mathcal J_g'
+\frac{2F'}{1-4F}\mathcal J_g=-2F'G.
\tag{A9}
\]
在−π²处G有简单pole，但F′有简单零，所以F′G解析，(A9)为普通方程；𝒥_g在那里解析。实际算术frame的另一行也更强：
\[
(uE)(F(p))=\frac{\sqrt p}{3}\tanh\sqrt p
\]
在−π²解析。p从0沿[0,b₀]时u从0增到1/4，恰是233的canonical叶。g=t使b₀处的全部平方根消失，𝒥_t解析且值0。域中仅此一个mark，绕它的monodromy因填点为零；(A9)遂给Ω上的单值holomorphic 𝒥_t。

取Riemann map h:D→Ω、h(0)=0。再固定一个0<s<1，使h(sD)包含上述canonical路径及−π²，定义
\[
\phi(w)=F(h(sw)).
\tag{A10}
\]
此φ在closed D的某个邻域holomorphic；1、(uE)∘φ、J_t∘φ在那里均holomorphic。φ遗漏1/3，原点只有一个simple native前像，但还在h(sw)=−π²处有一个二阶前像。mark1/4只有一个simple前像，且可在连接原点与mark的contractible小邻域上取φ单射：F在[0,b₀]严格递增且导数非零，紧性给薄的单射邻域。

因此这是真实的共同图和被填叶，不是只检查径向局部式。g≠t时同图在这个simple mark上仍有平方根，非meromorphic。若t∈Q，该source的原生系数为Q，所得共同图满足所用解析条件。p是图参数，未把它免费用作新的算术坐标。

## 4. 两个限定模板容量，以及全部共同图的新upper

### 4.1 限定模板的范围

若另要求φ⁻¹(0)={0}，则3φ:D*→C∖{0,1}的原点小圈只绕0一次，可提升到modular λ的punctured-q覆盖；λ(q)=16q+⋯。lift在0有simple零，Schwarz引理给
\[
|\phi'(0)|\le16/3.
\tag{A11}
\]
CDT固定v2物理页26–27、Prop2.9.3及§2.9.5明确给这个univalence/unique-origin模板与系数16。它不自动证明λ/3是本J_t的实际共同图，也不适用于(A10)的外国零点。

对(A10)中特定的univalent h，最近的被遗漏F-pole为−π²/4。Koebe quarter theorem给|h′(0)|≤π²，因此
\[
|\phi'(0)|\le\pi^2/3.
\tag{A12}
\]
这项估计只由h的单射性支付，不能直接用于任意多值p图。Koebe常数已在McMullen作者2010课程物理页64–65、printed64的Theorem4.20核读。

### 4.2 全体合法共同图可以另行控制

Root随后提出更强入口，本文独立核如下；对应最终保存的all-map稿§1–§4/G1–G5已经实际FULL读取，精确身份见scope。任取holomorphic φ:D→C、φ(0)=0，假设(uE)∘φ meromorphic。除非φ′(0)=0使导数估计平凡，否则在原点取规定native叶。除以φ可得E∘φ meromorphic。令
\[
p=3\phi(E\circ\phi)^2.
\tag{A13}
\]
它实际上全盘holomorphic：在任何φ零点，(A5)给p/3=φE_nat²+2c√φE_nat+c²。若c≠0，meromorphy迫使零阶为偶数，故√φ是局部解析；若c=0亦解析。其它点E没有pole，因为1/3已由log排除且φ没有pole。

近原点由atanh的反函数有φ=F(p)，随后作为单值meromorphic恒等式延拓全D。F在其pole处有真正二阶pole，任何有限阶p前像仍是pole，与φ全纯矛盾。因此p遗漏−a和−9a，a=π²/4。而p(0)=0、p′(0)=3φ′(0)。置
\[
\Psi=\frac{p+a}{p+9a}:D\longrightarrow\mathbb C\setminus\{0,1\},
\quad \Psi(0)=1/9,\quad
\Psi'(0)=\frac8{81a}p'(0).
\tag{A14}
\]

为避免modulus/parameter误差，记
\[
\mathbf K(x)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-x\sin^2\theta}}
=K_{\rm DLMF}(\sqrt x).
\]
三穿孔球面在0<x<1的universal-cover conformal radius是
\[
\mathcal R(x)=\frac8\pi x(1-x)\mathbf K(x)\mathbf K(1-x).
\tag{A15}
\]
规范核查：DLMF20.9.1–2、23.15.1/6给τ=i𝐊(1−x)/𝐊(x)及λ(τ)=x。两Legendre解的Wronskian为−π/[4x(1−x)]：由微分方程得常数形式，再用𝐊(0)=π/2及
\[
\lim_{x\downarrow0}x\frac{d}{dx}\mathbf K(1-x)=-\frac12
\]
从端点积分缩放确定常数。因此
τ′=−iπ/[4x(1−x)𝐊(x)²]。disk到H的归一化cover导数模为2Imτ，相乘正好给(A15)，不是4/π或16/π。

Schwarz lift给|Ψ′(0)|≤𝓡(1/9)。积分直接给
𝐊(x)≤π/(2√(1−x))、𝐊(1−x)≤π/(2√x)，故
\[
\mathcal R(1/9)\le\frac{4\pi\sqrt2}{9},\qquad
\boxed{|\phi'(0)|\le\frac{3\pi^3\sqrt2}{8}.}
\tag{A16}
\]
这无需unique-origin或univalent p条件，确覆盖保留该实际frame的全部合法共同图。J的mark条件只进一步缩小图类，没有被免费取消。

## 5. 单次gate的结果与严格停止范围

Root234已支付的函数组(1,uE,b_gJ_g)使用安全数组σ=(0,2,3)、τ=7/3。基本CDT界若要严格小于实际rank3，Jensen 𝓔(φ)≥log|φ′(0)|给必要条件
\[
\log|\phi'(0)|>3\tau/2=7/2.
\tag{A17}
\]
这里使用的是同一已付数组，不是最优联合格费用。由π³<32、√2<3/2，(A16)小于18；而e^{7/2}>1+7/2+49/8+343/48+2401/384>24。所以(A16)确达不到(A17)。即使采用理想最低能量也不够。

因此本轮既支付一张含外国even-origin的真实共同图，也支付不依赖该单射构造的全图upper；当前安全表的基本证书失败。它不排除更低的真实联合τ、改变源的算术结构、其它CDT证书或其它目标。没有证明t的新颖性或无理性；不把T∈Q、t∈Q、V∈Q混同，不从标量LCD精确主率推出最优联合费用。此次gate收束，不启动域/参数扫描或新的自动六轮优化。

来源与执行：规范化233全文、最终Root234 exact-LCD/rank稿及all-map稿实际FULL读取；CDT218页固定v2只新增FULL选页26–27，McMullen106页只新增FULL选页64–65，两组均抽取并渲染核读；DLMF仅读所用定义与theta/period规范。精确身份和浏览范围见literature/truncated_analytic_sources_round234_20261008/lambert_reading_scope.md。数学程序0、参数扫描0、旧producer重跑0；PDF工具仅文档操作。本文最终保存后作者完整复读，不作为他人独审。
