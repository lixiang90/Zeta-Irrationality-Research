# D12 完整解析叶：真实分支反例、合法ramified maps与全部尖点

日期：2026-10-06。新proof note，不修改冻结source，不执行旧或peer producer。基于[真实pure周期source](cdt_odd_level12_source_period_20261006.md)与[配对几何](cdt_odd_level12_paired_coordinate_20261006.md)。本稿先决定目标函数的CDT解析输入；未求实际conformal radius、完整辅助数组成本或新的无理性结论。

## 1. 几何输入与branch标签

记r=√3、b=3^(1/4)，Γ=kerχ12⊂Γ0(12)，

\[
 h=\frac{η_1^3η_4η_6^2}{η_2^2η_3η_{12}^3},\qquad
 v^2=\frac{h+6}{h+2},\quad v=1+2q+O(q^2).
\]

v是Γ compact curve的一次参数；Γ0(12)的deck χ−coset作用为v↦−v。W=W12作用v↦r/v，M=(24,−7;84,−24)作用v↦−r/v。以下δ=+1对应原H−/W；δ=−1对应共轭Hσ/M。配对参数为

\[
 t_δ=\frac{v+δr/v-1-δr}{2(1-δr)},\qquad t_δ=q+O(q^2).
 \tag{1}
\]

原支branch values来自v=±b：

\[
 α=\frac{b-1}{2(b+1)},\quad β=\frac{b+1}{2(b-1)},\quad αβ=1/4.
\]

τ=i/√12处h>0、v由正q连续保持正，所以实际canonical W-fixed point对应v=+b和α；不用数值sample识别此标签。另一个W branch为v=−b。

共轭branch values来自v=±ib：

\[
 γ_\pm=\frac{r-1\pm2ib}{2(1+r)},\qquad |γ_\pm|=1/2.
\]

无需猜定M的fixed point究竟给哪一个γ标签：实q coefficients保证反射τ↦−\bar τ将它变为另一点。下面将两个actual representatives都处理。

## 2. 直接Γ商下降需要逐fiber真实cocycle

取A=E2−12E2(12τ)、Θ=34560rL(3,χ12)，H−=A(f−−Θ)、Hσ=A(fσ+Θ)。在L3∈Q假设下，这两个q germs是实际代数系数共轭；以下解析身份本身不依赖该假设。

若J=(a,b0;c,−a)是对应W或M在Γ中的trace-zero conjugate，detJ=12，且source F|J=−F，∞constant0，则

\[
 f+R_Jf=λ_JQ_J,\quad R_Jf=(cτ-a)^2f(Jτ)/12,
 \quad Q_J=1+(cτ-a)^2/12,
 \quad λ_J=f(e^{2πia/c}).
 \tag{2}
\]

同样由Bol加一维Sym² eigenline及两端constant0证明。A|J=−A。因此A(f−s)在该actual fixedpoint的coarse quadratic quotient上可去，准确当且仅当λJ=s。

更具体，Cayley w取J:w↦−w，QJ=−4w/(1−w)²，e=(1−w)²(f−s)，则

\[
 \frac{e(w)-e(-w)}2=-2(λ_J-s)w.
 \tag{3}
\]

若A=(1−w)²a(w²)，H的odd carrier为−2(λJ−s)w a(w²)。A的有限zeros只推迟首个odd项，不能删去非零carrier。不能用一个branch value的canonical period来替代它在所有Γ translates上的period。

## 3. 第一嵌入另一个branch确实不可填

取一个明确χ−deck representative

\[
 g_5=\begin{pmatrix}5&2\\12&5\end{pmatrix},\quad χ(5)=-1,\qquad
 J_β=g_5Wg_5^{-1}=\begin{pmatrix}180&-73\\444&-180\end{pmatrix}.
 \tag{4}
\]

其fixed point是15/37+i√3/222，v=−b，所以属于β。因JβW^-1∈Γ，F−|Jβ=−F−。这个actual period来自唯一指定endpoint q=e^(2πi15/37)，其完整值为

\[
 \boxed{λ_{J_β}=Θ+\frac{498240}{37}iπ^3.}\tag{5}
\]

下面给可复算的有限sum，不从浮点识别系数。对k与12互素、h coprime k，定义

\[
 \mathcal T_k(h)=\frac1{3k}\sum_{m=1}^{k-1}(k-2[mh^{-1}]_k)B_3(m/k),
\]
\[
 \mathcal F_{k,h}=\frac{12}{3k}\sum_{m=1}^{k-1}(k-2[mh^{-1}]_k)
 \sum_{a=1}^{12}χ(a)B_3(\{a/12+m/k\}).
 \tag{6}
\]

χE kernel的finite polynomialEk,h在x^k=1上满足

\[
 (1-x^{12h})E_{k,h}(x)=\sum_{a=1}^{12}χ(a)x^{ha},
 \quad E_{k,h}(1)=0,
\]

并令\(\mathcal E_{k,h}=(2/3)\sum_m [x^m]E_{k,h}\,B_3(m/k)\)。coefficients由cyclic recurrence c_m−c_(m−12h)=H_m与c0=0准确确定。此处χeven令kernel纯imaginary、coefficients odd，故normalization自洽。普通Lambert finite part和Gauss/B3证明已在source稿完成，(6)是同一恒等式的fixed group-derived endpoint应用。

trivial coefficients为u1=1217,u2=−14082,u3=6255,u4=−11120,u6=126738,u12=−175248。对(k,h)=(37,15)，各imaginary coefficients（除iπ³）为

|部分|准确值|
|---|---:|
|240Σu_j j^-3 T37(hj)|683326080/50653|
|E37,15|7004/50653|
|κF37,15|7433/50653|
|完整source，triv+2880(E−κF)|498240/37|

实部仍为Θ，因为全部trivial ζ3系数为0。χ(37)=+1，使原C−与trivial radial poles准确相消。式(5)与(3)证明H−不直接下降到整个Γ/W商的所有upper-half-plane branch fibers。

## 4. 第二嵌入两个canonical branch可填，但Γ translates仍有反例

取

\[
 M'=\begin{pmatrix}-24&-7\\84&24\end{pmatrix},\qquad
 M'M^{-1}=\begin{pmatrix}97&-28\\-336&97\end{pmatrix}\in Γ.
\]

M′的endpoint为−2/7，fixed point为−2/7+i√3/42。实coefficients与已经证明的canonical λM=−Θ给λM′=−Θ；两actual points的v互为complex conjugate，因此覆盖v=+ib、−ib。这两个canonical paths的Hσ branch都可填。

但不能由此推所有fibers可填。取明确parabolic

\[
 η=\begin{pmatrix}1&0\\12&1\end{pmatrix}\in Γ,\qquad
 J_σ=ηMη^{-1}=\begin{pmatrix}108&-7\\1668&-108\end{pmatrix}.
 \tag{7}
\]

其fixed point是9/139+i√3/834。η保持v，所以它处在同一个γ branch的另一个Γ translate；它的真实endpoint期望值却为

\[
 \boxed{λ_{J_σ}=-Θ+\frac{2578560}{139}iπ^3.}\tag{8}
\]

同一有限式(6)对(k,h)=(139,9)给

|部分|准确值|
|---|---:|
|trivial|25179461760/2685619|
|E139,9|−156120/2685619|
|κF139,9|26135960/8056857|
|完整σsource，triv+2880(E+κF)|2578560/139|

χ(139)=−1，与真实σsource的C+ radial pole相消；不是把原source C−和σsource混用。由(3)，Hσ在该actual point不可直接下降。

一个固定sanity check是ηWT^-1关系：η=WT^-1W^-1，η本就在原G−；J0=ηWη^-1=(12,−1;156,−12)，endpoint1/13的Tate coefficient确为0。因此这里没有将所有Γ translate都误判成坏fiber，也没有尝试扫描或分类所有cocycles。

## 5. 全部10 cusp、zero fibers与不能填的cubic carriers

h的完整六cusp值给v的全部10 cusp values：

|Γ0 cusp denominator|h|Γ上的v values|
|---:|---:|---|
|12，∞|∞|+1,−1|
|1，0|0|+r,−r|
|2|−6|0|
|6|−2|∞|
|3|−4|+i,−i|
|4|−3|+ir,−ir|

在(1)的quotient中，令aδ=2+δr，完整五cusp images是

\[
 \boxed{0,\ a_δ,\ \infty,\ (a_δ+i)/2,\ (a_δ-i)/2.}\tag{9}
\]

其中zero fibers恰为v=1、v=δr，pole fibers恰为v=0、∞；它们全是cusps，没有任何interior zeros/poles。Jδ交换两个zero cusp，且tδ=q+O(q²)，所以选定Gδ的唯一q-filled cusp给一个simple zero。

所有其它cusps有实际非零cubic obstruction。对c|12，trivial source和A的slash constants是

\[
 B_c=\sum_j u_j\{\gcd(c,j)/j\}^4,
 \qquad A_c=1-c^2/12.
\]

|c|Bc|Ac|
|---:|---:|---:|
|1|460|11/12|
|2|−36160/3|2/3|
|3|13785|1/4|
|4|−73520/3|−1/3|
|6|108480|−2|
|12|−66240|−11|

χE constant只能在c12非零、χF只能在c1非零：从E/F lattice sum的zero denominator条件即可证明（primitive χ要求分别12|c及gcd(c,12)=1）。所以c2,3,4,6的full source constants就是上表Bc，四者全非零。

若z=σc^-1τ是cusp的标准upper-half-plane coordinate，Bol的leading term给

\[
 H(σ_c z)=\frac{A_cB_c(2πi)^3}{6}z^3+O(z^2).
 \tag{10}
\]

若q_c=e^(2πiz/wc)，换成logq_c时系数是Ac Bc wc³/6；不能省略width后混淆规范。ΘA只贡献degree≤2，删不掉这个cube。非zero coefficient意味着该cusp不能作为H全纯的interior填充点，有限ramification也不能消掉log³。

剩下c1/c12的两sheet中，canonical zero pair由真实W/M周期正则；另外一对v=−1、−δr的source constants非零（c12为−132480；c1以det1的S规范为920）。它们给aδ cusp的非zero cubic。故(9)的全部nonzero finite cusp images在这些目标函数的合法fullleaf地图中保持遗漏；∞ cusp pair也不能被当成全纯填充点。

## 6. 完整合法CDT目标地图确实存在

采用实际generated groups，而不要求整个Γ quotient下降：

\[
 G_+=\langle T,W\rangle,\qquad G_-=\langle T,M\rangle.
 \tag{11}
\]

这里G+对应H−，G−对应Hσ。原支ζ=√12τ将G+变成Hecke group〈ζ↦ζ+√12,ζ↦−1/ζ〉；共轭支先z=τ−2/7，再ζ=√588z，将G−变成同类型、参数√588的group。二者参数>2。

实际原件[Soares2020 pp1–2](../literature/soares2020_hecke_triangle_transfer_v1.pdf)给fundamental domain |Reζ|<w/2、|ζ|>1及one cusp/one funnel/one order2 elliptic的拓扑。coarse quotient是genus0 punctured bordered disk；填充唯一cusp并用elliptic coarse coordinate后，interior是Riemann disk Xδ。

Hδ的T不变性和真正W/M周期使其全局Gδ不变。在upper-half-plane，Hδ及tδ全纯；canonical elliptic orbit由真实identity下降，唯一cusp由原q Taylor填充。tδ全部interior不取(9)的cusp values，且唯一filled pointPδ给simple zero。取Riemann maps Fδ:(D,0)→(Xδ,Pδ)，则

\[
 \boxed{Φ_δ=t_δ\circ F_δ:D\to C,
 \quad Φ_δ^{-1}(0)=\{0\},
 \quad H_δ\circ F_δ\text{全纯}.}\tag{12}
\]

这是真正的全纤维判据：在Gδ stabilizer的canonical orbit，tδ coarse degree1且H下降；在其余involution fixedpoint，若stabilizer不在Gδ，source是普通point而tδ有degree2，故Φδ自动偶数分歧，原始H在source仍全纯。式(5)/(8)的坏fibers因此合法，而不是错误地删除了其周期。

M′不变性允许考虑更大的生成群〈T,M,M′〉，但本稿不依赖尚未独立证明的更大group conformal topology/capacity。已经给出的Gδ full maps足够证明目标系统的合法cover存在。

不能直接说裸Euler导数行在这个disk上全纯。这里有一个明确的统一gauge。令

\[
 \mathscr D_δ(t)=1-4a_δt+4t^2,\qquad
 g_δ(t)=\mathscr D_δ(t)^2\in O_K[t],\quad g_δ(0)=1.
 \tag{12a}
\]

它是v↦tδ双cover的discriminant归一；两个simple roots正是该支的branch values。若一个ordinary source point满足t−t0∼w²而H全纯，则∂tH至多有w^-1、∂t²H至多有w^-3；gδ有w^4，所以这两个poles全被清掉。canonical elliptic orbit的coarse source coordinate中t为simple local parameter，H已下降，那里原本没有这类pole。t=∞只对应未填cusps，在disk interior不出现。因此

\[
 \boxed{1,\ g_δH_δ,\ g_δ\theta_tH_δ,
       \ g_δ\theta_t^2H_δ\text{ 在 }X_δ\text{ 上全部全纯}.}
 \tag{12b}
\]

σg+ = g−，它的fixed degree4与全整数coefficients不增加LCM denominator exponent；乘同一非零rational gauge也不改变derivative-closure rank。新增背景函数仍须另核其branch/omission及算术分母，不能从(12)宣称整套未来CDT数组自动合法。为closed-disk-neighborhood要求可使用Φδ(sz)、0<s<1，然后取极限。

## 7. 原点导数的严格上界与coordinate normalization

令ρδ=|Φδ′(0)|；因tδ=q+O(q²)，它也是q-coordinate conformal derivative。对遗漏nonzero a，CDT原件§2.8 p24的Carathéodory唯一零点定理给ρδ≤16|a|。利用aδ²+1=4aδ，(9)给

\[
 \boxed{ρ_+\le16\sqrt{2+r},\qquad ρ_-\le16(2-r).}\tag{13}
\]

第一embedding最近nonzero cusp是complex pair、模长√(2+r)；第二embedding最近的是a−=2−r，其complex cusp modulus√(2−r)更大。数域degree2的标准archimedean权重各1/2，所以

\[
 \boxed{\frac{\logρ_++\logρ_-}{2}
 \le\log16-\frac14\log(2+r).}\tag{14}
\]

这不是已知实际radius的等式，也不宣称某个CDT预算已失败；它适用于给出的actual坐标/period surfaces/unique-zero和cusp omissions，不排不同source或不满足这些standing conditions的方案。

一个容易误计的变换是xδ=tδ/(1−tδ/aδ)。aδ为O_K unit，故它保持q leading1、两embedding配对及全n整性；它将另一个cusp改为∞，其余三个nonzero finite cusp modulus都变成aδ。但dx/dt在0等于1，所以同一filled source的ρ根本不变。原t同时保持全纯（x=−aδ只是未填irregular旧∞ cusp），因此更强的(13)/(14)仍能应用。不能把这个unit Möbius的较弱“平均cap16”算成新增解析收益。

## 8. 固定证书、范围及下一步

新同名verify只核三个明确group-derived endpoints1/13、15/37、9/139，全部matrix与finite Bernoulli kernels、十cusp几何及branch-clearing degree4 gauge；它不搜索endpoint或参数。旧source/paired-coordinate producer都不执行。作者本轮首次、单次运行这个NEW producer，77项全部通过；有限证书不替代下面注明的fullleaf拓扑与解析证明。

本稿已经给出：两embedding不在整个Γ quotient上单值下降的实际反例、哪些chosen fibers可填的cocycle判据、其余fibers的合法even ramification、全部cusp/zero fibers和真实Gδ full maps。仍未分类所有Γ period cocycles、未算实际conformal size、未完成背景数组/holonomy预算；不由fullmap存在宣布无理性。

## 9. 实际只读审阅记录

helper_tensor_budget实际只读§§5–7，限定审核通过：全部10cusps、两个zero fibers与非zero cubic排填；参数√12/√588的Hecke一cusp一funnel/order2拓扑及填后盘；t无interior zeros/poles与唯一simple filledzero；坏Γ fibers保留ordinary source上的ram2；degree4 gauge清native导数；两embedding最小遗漏值与(14)的平均cap。审阅者没有运行77项NEW producer，没有独立重算§§3–4的37/139 Bernoulli endpoint，不认领实际radius/J或未来全部背景函数。

本文作者另实际只读配对坐标稿§§2–4与§6，核对actual character cover/C(v)、W正号与σ(W)=M、全n整数反演、rational非齐次阶3及cusp actualrank4链；没有运行peer producer。这是对所用几何输入的审阅，不冒充他人对本新稿的审核。

conjugate_projection实际只读§§2–4和NEW源码，并用独立E倒数Fourier double-sum核三个固定13/37/139端点；其ordinary/E/κF/Tate值、radial character与source sign全吻合。generalBol一维period、Cayley odd carrier及M′反射的两actual路径审核通过。审阅者没有运行本文producer，没有将这次审核扩展为§§5–7全文或全部stabilizer分类。

Root实际全文阅读本MD与NEW源码，限定§§2–7的数学链通过：真实branch反例与cocycle、全部cusp carriers、合法Gδ填充盘、native degree4清pole因子及平均cap。Root没有重新执行77项producer。这些审阅不认证任何新的无理性定理、实际radius/J或完整未来背景数组。本文三件在上述实际限定审阅状态冻结，后续capacity输入另建稿。
