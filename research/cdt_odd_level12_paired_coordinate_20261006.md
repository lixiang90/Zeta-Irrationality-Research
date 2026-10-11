# Level12 pure L3χ12：真实共轭商坐标、全尺度整模型与实际秩4

日期：2026-10-06。这是新建记录，不修改任何已冻结输入。本文完成一个预先固定的χ12 source及其两真实周期所需的共轭模坐标，并从真实模变换证明holonomicity与实际秩4。**没有证明L(3,χ12)无理，也没有闭合CDT解析预算。** 特别是两个compact quotient的坐标配对不等于H已在所有分歧点或整个compact curve上单值全纯。

## 1. 输入、实际审阅范围与新独立周期核验

令s=√3，K=Q(s)，O_K=Z[s]，χ=χ12。χ在mod12的units1,11取+1，在5,7取−1。采用常数项1的E4以及

\[
E_χ=23+\sum_{n\ge1}\frac{χ(n)n^3q^n}{1-q^n},\qquad
F_χ=\sum_{m,n\ge1}χ(n)m^3q^{mn},\quad κ=24s.
\tag{C1}
\]

[实际source-period报告](cdt_odd_level12_source_period_20261006.md)固定

\[
\begin{split}
F_-={}&1217E_4-14082E_4(2τ)+6255E_4(3τ)-11120E_4(4τ)\\
&+126738E_4(6τ)-175248E_4(12τ)+2880E_χ-69120sF_χ,\\
B={}&E_2-12E_2(12τ),\qquad f_-=θ_q^{-3}F_-,\qquad
Θ=34560sL(3,χ),\quad H_-=B(f_--Θ).
\end{split}
\tag{C2}
\]

σ只作用于源的代数系数s↦−s，Fσ=σF−，fσ=θq^-3Fσ。记

\[
Wτ=-1/(12τ),\quad γ=\begin{pmatrix}7&2\\24&7\end{pmatrix},
\quad M=γW=\begin{pmatrix}24&-7\\84&-24\end{pmatrix},\quad M^2=-12I.
\tag{C3}
\]

采用det^(k/2)(cτ+d)^−k的slash。Eχ|4W=κFχ，Fχ|4W=Eχ/κ，χ(7)=−1。因此F−|4W=−F−、Fσ|4M=−Fσ；B|2W=B|2M=−B。Γ=kerχ⊂PSLΓ0(12)，两源在Γ上都是实际weight4 form。

本作者实际只读审阅source-period报告§§2–7，独立核对有限B3/Gauss、全部三个source constraints、ordinary-W完整Laurent项与W/M双period、仅L3∈Q下的合法σΘ及B的双anti。没有运行或审阅该稿producer；本节另用不同的E-character有限和作一次固定输入的独立证书。

### 1.1 指定ρ7²端点的独立有限和

定义B3(x)=x³−3x²/2+x/2，ρ=e^(2πi/7)。普通Lambert primitiveT(q)=Σn^-3q^n/(1−q^n)的radial finite part为

\[
\operatorname{FP}T(ρ^A)=-ζ(3)/2+iπ^3T_A,
\quad T_A=\frac1{21}\sum_{m=1}^6(7-2[A^{-1}m]_7)B_3(m/7).
\tag{C4}
\]

这个身份可由7阶根上的有限cot/Fourier polynomial直接推出。只有7|n项的1/(εn) pole被减去；减后余项统一有界，故n^-3求和的dominated limit合法。固定结果(T1,…,T6)=(12,4,0,0,−4,−12)/343。

三个trivial source

\[
G_1=E_4-144E_4(12τ),\quad G_2=E_4(2τ)-9E_4(6τ),\quad
G_3=E_4(3τ)-(16/9)E_4(4τ)
\]

的primitive依次是240T(q)−20T(q12)、30T(q2)−10T(q6)、(80/9)T(q3)−(20/3)T(q4)。在q=ρ²的iπ³系数依次是

\[
(960/343,\ 40/343,\ -80/147).
\tag{C5}
\]

独立地，在非平凡7阶根z上使用1/(1−z)=−Σk=1^6 k z^k/7。Eχ primitive的iπ³系数因此等于

\[
\mathcal E=-\frac2{21}\sum_{a=1}^{12}χ(a)\sum_{k=1}^6
 kB_3\left(\left\{\frac{2(a+12k)}7\right\}\right)=\frac{12}{343}.
\tag{C6}
\]

7|n的Eχ kernel在1处可去、值0，故同一有限式也覆盖这些项。这个核算不调用source-period稿的四项短polynomial。

χ的primitive even Gauss sum为√12。κ=12√12消去该根后，κFχ primitive的iπ³系数是

\[
\mathcal F=\frac{12}{21}\sum_{m=1}^6w_m\sum_{a=1}^{12}χ(a)
 B_3\left(\left\{a/12+m/7\right\}\right)=\frac{550}{1029},
\quad w=(-1,5,-3,3,-5,1).
\tag{C7}
\]

内层前三个值311/2352、383/2352、1/14，后面按反序反号；加权总和275/294。故共轭C+=Eχ+κFχ的Tate系数是586/1029，真实finite real part是−12sL3χ。

对一般aG1+bG2+cG3+dC−，∞constant0及ζ3-free分别给

\[
23d=143a+8b+7c/9,\quad c=-99a-9b,\quad d=(66a+b)/23.
\]

canonical共轭端点的剩余Tate系数恰为(28164a+2434b)/483。预先固定(a,b,c,d)=(1217,−14082,6255,2880)使它为0且d≠0。κL4χ=(115/3)ζ4，trivial pole为240Σuj/j4=(115/3)d，χ(7)=−1，完整radial poles准确抵消。所以这里得出的是实际端点

\[
f_σ(ρ^2)=-Θ,
\tag{C8}
\]

而非任意选取的regularization常数。

### 1.2 没有遗漏一次cocycle项

令z=τ−2/7。M:z↦−1/(588z)，其weight−2 slash为588z²f(Mτ)。Bol身份使fσ+fσ|−2M的三次导数为0；M²central又使这个quadratic处于Sym²M的+eigenspace。若P(z)=a+bz+cz²，条件588z²P(−1/(588z))=P(z)强迫b=0、c=588a。端点(C8)遂给

\[
f_-+12τ^2f_-(Wτ)=Θ(1+12τ^2),
\]
\[
f_σ+12(7τ-2)^2f_σ(Mτ)=-Θ\{1+12(7τ-2)^2\}.
\tag{C9}
\]

原τ坐标里展开二次式当然含固定的一次项；没有另一个可任意忽略的independent linear period。普通W下的共轭源不是anti，必须保留L2=−1920π²、W∞constant132480及

\[
f_σ-12τ^2g_σ(Wτ)=-Θ+12Θτ^2-3840iπ^3τ+\frac{3680iπ^3}{3τ}.
\tag{C10}
\]

正进展是(C9)的真实第二lift，而不是删掉(C10)的Tate项。

## 2. 从eta函数到实际character双cover

采用[已冻结level12实际模型§2](cdt_odd_level12_model_20261005.md)的literal eta输入

\[
h=\frac{η_1^3η_4η_6^2}{η_2^2η_3η_{12}^3},\qquad
x=h^{-1},\quad r_d=(3,-2,-1,1,2,-3),\ d=(1,2,3,4,6,12).
\tag{C11}
\]

权和为0，Newman两和是−24、24，∏d^rd=1/144为平方。Ligozat阶在c=1,2,3,4,6,12依次为(1,0,0,0,0,−1)。η在上半平面无零，所以h只有一个简单极点，确是X0(12)的Hauptmodul。

新证书还独立解六个固定cusps的eta阶矩阵：对每个c≠12构造divisor[c]−[∞]的eta unit hc，leadingq−1=1，检查其整数指数、权和、两模24条件及平方character。hc−h为常数，由q0=−r1读出

\[
h(0)=0,\quad h(1/2)=-6,\quad h(1/3)=-4,\quad
h(1/4)=-3,\quad h(1/6)=-2,\quad h(∞)=∞.
\tag{C12}
\]

η的S公式和指数反序=负指数给h(Wτ)=12/h(τ)。系数12的正号由正虚轴的正eta值确定。

Γ0(12)没有elliptic stabilizers：c≡0 mod4使trace0不可能，c偶使trace±1不可能。因此其open curve是六punctured sphere，六个cusp loops生成fundamental group。对1/c的parabolic stabilizer，width wc=12/gcd(c²,12)，下右项1+cwc；六个χ值是

\[
(+1,-1,+1,+1,-1,+1).
\tag{C13}
\]

恰只有h=−6与h=−2两cusps有negative character。于是定义实际analytic root

\[
v^2=\frac{h+6}{h+2},\qquad v(∞)=1.
\tag{C14}
\]

右边在H内无零/极点，故可在simply connected H上取root。绕上述两cusps的continuation反号、绕其余cusps不变；(C13)与生成性证明v(γτ)=χ(γ)v(τ)。这是实际monodromy证明，不是从q-series猜测一个character。

v不属于C(h)，并已在Γ上单值，因此Γ的function field是C(h,v)，degree2恰好等于[Γ0:Γ]。由

\[
h=\frac{6-2v^2}{v^2-1}
\tag{C15}
\]

看出它就是C(v)。相同方程给一个明确Q-model P1v；v=1是q-germ指向的Q-rational cusp。这里的Q-model来自(C14)的实际rational-q函数field及明确参数，没有未经说明地使用standard X1(12) moduli-model的∞cusp定义域。十个cusps也直接由四个unbranchedcusps各两点、两个branchedcusps各一点得到。

## 3. W/M是实际Galois配对的involutions

设δ∈Γ0(12)/Γ为nontrivial diamond，则δv=−v。W正规化Γ，(C11)–(C14)给

\[
v(Wτ)^2=3/v(τ)^2.
\]

这个square身份尚不能定sign。在τ=i/√12处，h=2√3>0。沿τ=iy，h>0且选定v>0，所以fixedpoint处v=3^(1/4)。只有正号与v(Wτ)=v(τ)相容。故实际地

\[
Wv=s/v,\qquad Mv=-s/v.
\tag{C16}
\]

第二式来自χ(γ)=−1及M=γW。两者与δ生成V4；σ固定v,h的rational-q定义，只把s送−s。因此作为K-model上的actual automorphisms，σ(W)=M；没有对未知L值施σ。

## 4. 明确的共轭Hauptmoduls与全尺度整数反演

令u=(v−1)/2。由(C14)准确得到

\[
x=\frac{u(1+u)}{1-2u-2u^2},\quad
u+u^2=x-2xu-2xu^2.
\tag{C17}
\]

x=q+Z[[q]]，因为它是leading q的literal integer eta product。对(C17)逐阶求u，每个新系数的系数都是1，右边只用此前整数系数，所以u(x)∈x+Z[[x]]。x(u)的分母constant1，故同样整系数；leading1 formal inverse一般也不需除法。因此u(q)、q(u)在q+Z[[q]]中。这个全n结论来自递归，不从十二项样本推出。

定义

\[
\boxed{
t_-=\frac{u[1-(1+s)u]}{1+2u}
 =\frac{v+s/v-1-s}{2(1-s)},\qquad
t_+=σt_-=\frac{u[1-(1-s)u]}{1+2u}.
}
\tag{C18}
\]

t−在W下不变，t+在M下不变。两者都是P1v上degree2的rational map，恰等于各order2group的degree；故是各actual quotient的Hauptmodul，不是仅有W-invariance的更高degree function。

u-formula的分母constant1证明

\[
t_\pm(q),\ q(t_\pm)\in q+O_K[[q]]
\tag{C19}
\]

（逆式的formal变量按相应t理解），两方向全尺度成立；σ配对保持leading1。首项仅作核验：

\[
t_-=q-(3+s)q^2+(5+2s)q^3-(7+2s)q^4+\cdots,
\]
\[
q=t_-+(3+s)t_-^2+(19+10s)t_-^3+(172+97s)t_-^4+\cdots.
\tag{C20}
\]

## 5. 全compact cusp/branch数据与实际叶的限定

由(C12)/(C14)，Γ的十个cusps在v上是

|base h|v cusps|W-pairing|
|---|---|---|
|∞、0|±1、±s|1↔s，−1↔−s|
|−6、−2|0、∞|0↔∞|
|−4、−3|±i、±is|i↔−is，−i↔is|

所以t−的五个cusp values为

\[
0,\quad∞,\quad 2+s,\quad(2+s+i)/2,\quad(2+s-i)/2.
\tag{C21}
\]

t+的值由s↦−s获得。具体t−(i)=(2+s+i)/2、t−(−i)=(2+s−i)/2；只列无序±集合时不需该标签。

令a=3^(1/4)>1。W固定v=±a，t−的两个branch values为

\[
α=\frac{a-1}{2(a+1)},\qquad β=\frac{a+1}{2(a-1)},\qquad αβ=1/4.
\tag{C22}
\]

正虚轴canonical W固定点对应v=a，故准确对应α。M固定v=±ia，t+两个branch values是

\[
γ_\pm=\frac{s-1\pm2ia}{2(1+s)},\qquad |γ_\pm|=1/2.
\tag{C23}
\]

本稿不额外识别canonical M固定点在(C23)的±标签；(C9)已经对actual M证明该点的局部正则化，branch set和坐标配对不依赖这个标签。

若L3χ∈Q，则σΘ=−Θ合法，Hσ=B(fσ+Θ)=σH−。两个actual germs分别对〈T,W〉、〈T,M〉不变，canonical fixedpoint的Cayley coordinate下为偶函数，故在相应coarse local quotient全纯。这没有证明它们对整个Γ单值：一般Γ Eichler cocycle仍可能非零；也没有证明β或另一个γ的路径具有同一消除period。后面使用的rational ODE容许H的这种monodromy，不能把compact algebraic quotient误作完整全纯叶。

## 6. 从真实变换证明rational ODE，实际秩恰4

先证明上界，不从q-modularity直接断言D-finite。取t=t−，k=θq t，r_t=k′/k，其中′=d/dt。τ′=(2πi k)^−1，故

\[
\mathcal L_0=\partial_t^3+3r_t\partial_t^2+(r_t'+2r_t^2)\partial_t,
\quad \mathcal L_B=B\mathcal L_0B^{-1}.
\tag{C24}
\]

局部solutions是B、τB、τ²B，它们Wronskian非零。Γ的weight2变换及W-anti使这个三维solution space在Γ、W下由constant matrix变换；因此唯一monic scalar operator的coefficients在actual quotient上不变。它们在H内只可能有B-zero及t-critical的有限阶pole。在cusps，换到cusp coordinate，basis是holomorphic finite-order factor乘1、logq_c、(logq_c)²；Wronskian quotient translation-invariant，log项消除，留下finite Laurent poles。在order2 quotient points用local square coordinate也只有有限pole。因此这些coefficients延拓为compact quotient P1上的meromorphic functions，属于C(t)。

它们的Laurent expansions在K：τ′中的2πi常数在r_t消掉，B、q(t)、k都具有K系数。一个C(t) rational function若formal Laurent coefficients在K，有限Padé linear algebra把它下降到K(t)。所以(C24)的三个coefficients确实在K(t)，并非猜测ODE。

chain rule给(θq)^3=k³L0。θq³f−=F−、L0constant=0，于是

\[
\mathcal L_BH_-=\frac{BF_-}{k^3}
 =\frac{BF_-}{t^3 S_t^3}\in K(t),\qquad S_t=θ_q\log t.
\tag{C25}
\]

右边非零。它确实下降：B、F−分别W-anti，k是weight2 W-plus，weight6相消；在Γ上同样weight相消。两端有限pole性质与上面一致，其K下降也可由formal series得出。故(∂−R′/R)LB给一个真实homogeneous order4 annihilator，实际derivative closure rank≤4。第二坐标t+与M下完全相同；所有operator coefficients及forcing由s↦−s共轭，因为B、F、t、q的algebraic coefficients都实际配对。σ作用于Θ只在L3Q假设中使用。

### 6.1 一个实际cusp给rank4下界

取cusp1/2，scaling γc=(1,0;2,1)，Γ0-width3的stabilizer下右项7、χ(7)=−1。因此Eχ|4γc、Fχ|4γc在τc↦τc+3时反号，constant0；Γ-width6使它们有ordinary holomorphic cusp expansion。

trivial E4(jτ)的normalized cusp constant为(gcd(2,j)/j)^4。因此一般finite source的constant为

\[
(F_-|_4γ_c)_0=\frac8{81}(9a+9b-c)
 =-\frac{36160}{3},\qquad (B|_2γ_c)_0=1-12(2/12)^2=\frac23.
\tag{C26}
\]

quasimodular E2 correction在B中相消；χ部分constant0的理由是irregular-cusp character，并未把regular-cusp formula错误代入。

Bol identity作用于f|−2γc，使其third θτc derivative等于F|4γc。因此包含

\[
(f|_{-2}γ_c)(τ_c)=
-\frac{36160}{3}\frac{(2πiτ_c)^3}{6}
+\text{degree≤2 polynomial}+\text{holomorphic positive cusp terms}.
\tag{C27}
\]

乘上B|2γc后，H−以(2πiτc)³计的cubic leading coefficient准确为

\[
\frac{(2/3)(-36160/3)}6=-\frac{36160}{27}\ne0.
\tag{C28}
\]

Γ-width6的真正local cusp parameter是q_c=exp(2πiτc/6)，所以以(logq_c)³计的系数是6³乘(C28)，即−289280；新有限证书所记录−36160/27采用(C28)的(2πiτc)³规范。ΘB项在该coordinate最多degree2，不能消除它。这里h=−6、v=0，v是Γ-width6的simple cusp parameter，t−在v=0有simple pole；换到actual t∞ local coordinate不会消除log³。一个common unipotent monodromy幂对H有Jordan chain长4；任何homogeneous scalar ODE必须order≥4。结合(C25)的上界得到

\[
\boxed{\operatorname{rank}_{\mathbf C(t_-)}\langle H_-,H_-',H_-''\ldots\rangle=4.}
\tag{C29}
\]

forcing使常数1位于closure；若这个trivial factor与rank3 homogeneous quotient分裂，则local unipotent chain最多长3，矛盾(C28)。所以这个实际extension不分裂。Fσ在该irregular cusp有相同trivial constant，t+也在那里有simple pole，第二actual rank同样4。这个论证仅用真实cusp输入，不从formal积分增加阶数推秩。

## 7. 全n、两embedding的safe算术模型

F± positive q coefficients在O_K：C2的全部ordinary oldscale coefficients是整数，character coefficient是整数乘s。B有integer q coefficients。f的nth coefficient是Fn/n³，故令Dn=LCM(1,…,n)，全n有Dn³fn∈O_K。

若用于irrationality反证而假L3χ=A0/B0∈Q，固定正整数B0清Θ分母（这里B0仅是数值分母，勿与gauge B混淆）。卷积只用indices≤n，Dj|Dn，因此

\[
B_0D_n^3[H_-(q)]_n,\quad B_0D_n^3[H_σ(q)]_n\in O_K
\quad\text{for every }n.
\tag{C30}
\]

由(C19)的all-order integral composition，换到各actual t仍只使用indices≤n；同一Dn³清分母。所以

\[
B_0D_n^3[H_-(q(t_-))]_n,\quad
B_0D_n^3[H_σ(q(t_+))]_n\in O_K
\quad\text{for every }n,
\tag{C31}
\]

而且它们是实际embedding conjugates。两反演leading1，不发生额外n↦2n denominator翻倍。这里给的是完整safe coefficient model；没有优化三导数数组、所有prime Smith layers或arithmetic holonomy成本。无理性结论需要这些算术费用与完整解析map一起进入定理。

## 8. 新固定证书、核验记录与剩余边界

[NEW producer](cdt_odd_level12_paired_coordinate_20261006_verify.py)不import旧producer，也不运行任何冻结脚本。[固定JSON](cdt_odd_level12_paired_coordinate_20261006_verify.json)的76项全部通过：独立E-character double Bernoulli sum、Gauss sums、canonical唯一source、M centered cocycle、六cusps eta阶与character、coordinate rational identities及order12双整数反演、cusp log³ coefficient。没有prime或parameter扫描。

执行记录如实区分：第一次执行在两个complex cusp的±标签断言处停下，改正标签；第二次在SymPy等价表达式的结构比较处停下，改为精确代数相等；第三次完成76项。没有改变source、endpoint或任何研究参数，没有调用旧证书。这些有限checks不能替代§§2–4的actual monodromy、sign、全n递归，或§6的compact meromorphic ODE与cusp rank证明。

本稿已完成真实共轭quotient坐标、实际rank4、full formal integer change of variable及safe denominator family。仍未证明两filled leaves上t的全局行为、全部interior fibers、unique zero和omissions，没有计算两embedding的capacity，没有把complete derivative lattice与CDT算术费用闭合。因此没有新的数值无理性/线性无关性定理，也没有Lean认证。

独立审阅：helper_tensor_budget实际只读§§2–4与§6，限定数学链通过：actual character双cover/Q(v)、W正号与σ(W)=M、degree2商和全n整数反演、rational order3非齐次系统及actual rank4。其建议已明确(C28)与width6 logq_c的规范区别。审阅者没有运行producer，也没有审fullleaf或CDT预算。上面的source-period核验是本文作者的实际只读审阅，不能替代他人对本新稿其它部分的审阅。

Root另实际全文阅读本稿及NEW producer后审核通过：真实character cover及sign、全n整反演、rational ODE与rank4链闭合；C28的width6规范已明确。Root未重新执行producer。以上审阅均不覆盖仍open的fullleaf、capacity或CDT预算。本文及对应producer/JSON于这个实际审阅状态冻结；后续输入另建稿，不以新增结论回写本文。
