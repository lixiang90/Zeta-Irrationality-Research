# Level8 混合目标：两个真实嵌入、完整非cuspidal周期与共轭叶障碍

日期：2026-10-06。新建报告，不修改已冻结的三候选稿。本稿目标是审计实际数域输入，不证明新的数值无理性，不将未知周期作形式Galois共轭。所有ζ3和L3均为通常的真实正数。

## 1. 原件、符号及唯一数值假设

实际输入是[三候选稿§4](cdt_odd_candidates_5_8_12_20261006.md)的明确source，以及[Beukers1987原件](../literature/beukers1987_modular_irrationality.pdf)印刷p273的Proposition1.2和pp280–281的Theorem4证明。原件p281在第二embedding直接给原始函数的较小收敛半径，对任意复数θ均成立，然后取θ为已假定代数数的共轭；它没有将真实L值的共轭作为第二Fricke正则化输入。

记r=√2、K=Q(r)、D=8、c=11/2、k=63、κ=16r；E4是常数项1的通常Eisenstein级数，Eχ、Fχ采用三候选稿的归一化。令

\[
 U=c(E_4-64E_4(8τ)),\qquad V_-=k(E_χ-κF_χ),\qquad V_+=k(E_χ+κF_χ),\qquad F_-=U+V_-,\quad F_σ=U+V_+.
 \tag{1}
\]

Γ=kerχ8在Γ0(8)中的PSL像，包含T:τ↦τ+1。U为trivial-character，V±为χ8-character；全source在Γ上为weight4。以determinant-normalized slash记W=W8。U和V−为W-anti，V+为W-plus。

定义各q primitive在∞为0：u=θq^-3(U−U∞)、v±=θq^-3(V±−V±∞)、f−=u+v−、fσ=u+v+。F−与Fσ的∞constant都是0。系数共轭σr=−r确实给σf−=fσ；它只作用于代数系数。

唯一待反证的数值假设可以是

\[
 ξ=-\frac{1155}{2}ζ(3)+504rL(3,χ_8)\in K
 \quad\text{（或更强地ξ∈Q）}.\tag{2}
\]

这不定义一个作用于ζ3、L3或π³的σ。若ξ=a+br∈K，则σξ=a−br是已假定代数数的共轭；不允许将其设为下一节的真实ψ。

## 2. 完整L1/2/3与实际W分解

χ8的even functional equation及Bernoulli值给

\[
 L(-1,χ_8)=-1,\quad L(0,χ_8)=L(-2,χ_8)=0,
 \quad L'_χ(-2)=-\frac{32r}{π^2}L(3,χ_8),
 \quad κL(2,χ_8)=2π^2.
 \tag{3}
\]

正次数Dirichlet级数为

\[
 L(F_σ,s)=1320(1-64\,8^{-s})ζ(s)ζ(s-3)
 +63ζ(s)L_χ(s-3)+1008rζ(s-3)L_χ(s).
 \tag{4}
\]

ζ(s)在1的pole与ζ(s−3)、Lχ(s−3)的simple zero必须先取极限，不能擅自写成0。令

\[
 ξ_U=-1155ζ(3)/2,\qquad ξ_V=504rL(3,χ_8),\qquad ξ=ξ_U+ξ_V,\quad ψ=ξ_U-ξ_V.
 \tag{5}
\]

完整有限值是

|source|L1|L2|L3|∞constant|W∞constant|
|---|---|---|---|---:|---:|
|U|−4ξU/π²|0|ξU|−693/2|+693/2|
|V−|−4ξV/π²|0|ξV|+693/2|−693/2|
|V+|−4ξV/π²|−21π²|−ξV|+693/2|+693/2|
|F−|−4ξ/π²|0|ξ|0|0|
|Fσ|−4ξ/π²|−21π²|ψ|0|693|

特别是σ源的L1仍含真实ξ，L3是ψ，L2是非零Tate周期。它不是W-eigen，而且W后的非零constant693使其不满足Proposition1.2的cuspidal-at-both-ends假设。

## 3. 非cuspidal配对的完整Laurent周期

下面保留constant-term corrections。一般设weight4 source F与G=F|W_N，constant分别为a、b；f、g是去constant后的q primitive。Bol身份是

\[
 θ_q^3\{Nτ^2 g(W_Nτ)\}=(G-b)|W_N.
\]

完整primitive f+a(2πiτ)³/6与g+b(2πiτ)³/6有三次导数F、G。因此Mellin–Hecke轮廓给

\[
 f(τ)-Nτ^2g(W_Nτ)=L(F,3)+2πiτL(F,2)-2π^2τ^2L(F,1)
 -\frac{a(2πi)^3τ^3}{6}-\frac{b(2πi)^3}{6N^2τ}.
 \tag{6}
\]

这里的解析延拓可明确固定，避免以发散的0端积分定义L值。取Y=1/√N，令ΛF(s)=(2π)^−sΓ(s)L(F,s)，则

\[
 Λ_F(s)=\int_0^Y\left(F(iy)-\frac{b}{N^2y^4}\right)y^{s-1}dy
 +\int_Y^\infty(F(iy)-a)y^{s-1}dy
 +\frac{bY^{s-4}}{N^2(s-4)}-\frac{aY^s}{s}.
 \tag{6a}
\]

两个积分均entire，直接换元给ΛF(s)=N^(2−s)ΛG(4−s)。可直接核对轮廓的全部residues：θ^-3的Mellin积分使用Γ(s)L(F,s+3)(−2πiτ)^−s；s=0,−1,−2给三个L值。由(6a)，L(F,s)在4的residue为b(2π)⁴/(6N²)，故s=1给式(6)的−b(2πi)³/(6N²τ)。L(F,0)=−a给s=−3的cubic term；更低negative integers的Γ poles由trivial L-zeros抵消。函数方程将剩余轮廓换成Nτ²g(W_Nτ)。这同时固定sign，且没有删去非cuspidal source的τ^-1项。

令Gσ=Fσ|W=−U+V+，gσ=−u+v+。式(6)成为

\[
 \boxed{f_σ(τ)-8τ^2g_σ(Wτ)
 =ψ+8ξτ^2-42iπ^3τ+\frac{231iπ^3}{16τ}.}\tag{7}
\]

注意左边不是fσ与其自身的普通Fricke二项式。各W-eigen部分的完整身份是

\[
 u+8τ^2u(Wτ)=ξ_U(1+8τ^2)-462iπ^3τ^3+\frac{231iπ^3}{32τ},
 \tag{8a}
\]
\[
 v_-+8τ^2v_-(Wτ)=ξ_V(1+8τ^2)+462iπ^3τ^3-\frac{231iπ^3}{32τ},
 \tag{8b}
\]
\[
 v_+-8τ^2v_+(Wτ)=-ξ_V(1-8τ^2)-42iπ^3τ
 +462iπ^3τ^3+\frac{231iπ^3}{32τ}.
 \tag{8c}
\]

只有原支(8a)+(8b)同时消去cubic和reciprocal污染，得到f−+8τ²f−W=ξ(1+8τ²)。共轭q source并未继承这种实际消去。

若完成全Eichler primitive并按真正周期正则化，可拆成一个weight−2 W-anti函数和一个W-plus函数；它们分别必须使用ξU、−ξV与π³τ。二者的sum是fσ−ψ+21iπ³τ。这里ξU、ξV各自不由(2)控制，而τ/logq项也不属于∞处全纯的K[[q]] germ。不能将此拆分当成合法的免费算术projection。

## 4. 共轭lift的真实α与另一完整周期

系数共轭可能改变Fricke lift，而不只是改变同一个W的周期。取

\[
 γ=\begin{pmatrix}3&1\\8&3\end{pmatrix},\quad χ_8(3)=-1,
 \quad M=γW=\begin{pmatrix}8&-3\\24&-8\end{pmatrix},\quad M^2=-8I.
 \tag{9}
\]

因为γ保持U并反号V+，Fσ|M=−Fσ。M正规化Γ，固定点是

\[
 α_M=\frac13+\frac{i\sqrt2}{12},\qquad
 q_M(τ)=1+\frac{(24τ-8)^2}{8}=1+8(3τ-1)^2.
 \tag{10}
\]

Fσ在∞及M∞=1/3的constant为0。Bol身份因此给fσ+R_Mfσ为degree≤2 polynomial，R_Mh=(24τ−8)²h(Mτ)/8。由M²=−8I，它必须在Sym²表示的+eigenspace中；此空间为一维、生成元qM。取τ→1/3+i0，R_Mfσ→0，所以

\[
 f_σ+R_Mf_σ=λ_M q_M,
 \qquad λ_M=f_σ(e^{2πi/3}).\tag{11}
\]

这个真实endpoint可完整求出。写ρ=e^{2πi/3}，并对3|n处的Lambert pole取实际radial limit，不任意指定正则值：

\[
 T(ρ):=\operatorname{FP}\sum_{n\ge1}\frac{ρ^n}{n^3(1-ρ^n)}
 =-\frac{ζ(3)}2+\frac{2iπ^3}{243},
 \tag{12a}
\]
\[
 T_χ(ρ):=\operatorname{FP}\sum_{n\ge1}\frac{χ_8(n)ρ^n}{n^3(1-ρ^n)}
 =-\frac{L(3,χ_8)}2+\frac{i\sqrt3}{6}L(3,χ_{-24}).
 \tag{12b}
\]

对3∤n，ρ^n/(1−ρ^n)=−1/2+i√3χ−3(n)/6；对3|n，radial expansion为1/(εn)−1/2+O(εn)。减去1/(εn)后绝对值≤1/2，所以n^-3求和的finite parts由dominated convergence严格确定。

Eχ的primitive使用eχ(z)=(z−z³−z⁵+z⁷)/(1−z⁸)：eχ(1)=0（可去），eχ(ρ)=i√3，eχ(ρ²)=−i√3。因此

\[
 (E_χ-c)^{[-3]}(ρ)=i\sqrt3 L(3,χ_{-3}).
 \tag{12c}
\]

准确临界值是

\[
 L(3,χ_{-3})=\frac{4π^3}{81\sqrt3},\qquad
 B_{3,χ_{-24}}=138,\qquad L(3,χ_{-24})=\frac{23π^3}{288\sqrt6},
 \quad κL(4,χ_8)=\frac{165}{8}ζ(4).
 \tag{13}
\]

χ−24在units1,5,7,11取+1，在13,17,19,23取−1，故B3由有限Bernoulli sum直接得到；(13)全部是parity-compatible临界公式，不含未知odd-even target。

u=1320[T(q)−T(q⁸)/8]。在q=ρe^-ε处，u的1/ε residue为1320(1−1/64)ζ4/81，v+的residue为−63κL4χ8/81；两者由(13)准确抵消。finite imaginary coefficients分别为110/9（U）、28/9（63Eχ）及161/12（1008rFχ）。所以实际radial limit，而非猜测的形式共轭，是

\[
 \boxed{λ_M=ψ+\frac{115}{4}iπ^3.}\tag{14}
\]

这保留了额外真实periodψ及不可删除的Tate载体。由于K为实域，(2)下σξ是实数，式(14)的非零虚部无条件证明λM≠σξ。它不提供ψ的无理性。

## 5. Scalar modular prefactor不能免费解除共轭α

令a∈R（特别a=σξ），假设某个非零、Γ上weight2 modular form B使B(fσ−a)在M二次商的αM附近下降。局部下降由解析延拓给H(Mτ)=H(τ)的整体身份。记B^M=B|2M，由(11)

\[
 (B+B^M)(f_σ-a)=(λ_M-a)B^M q_M.
 \tag{15}
\]

若B+B^M=0，右边非零，立即矛盾。否则M正规化Γ，所以B^M/(B+B^M)是Γ上的meromorphic weight0函数，特别为T-periodic；fσ−a也是T-periodic。式(15)在τ与τ+1的差给

\[
 (λ_M-a)\frac{B^M}{B+B^M}\{q_M(τ+1)-q_M(τ)\}=0,
\]

但三个因子皆非零，矛盾。故整个这种scalar modular prefactor族都不能使a=σξ的共轭germ在αM可去；不只排除某一个选定的W-eigen gauge。

局部carrier也可以直接看见。令z=τ−1/3、w=(z−i√2/12)/(z+i√2/12)，则M作用为w↦−w，qM=−4w/(1−w)²。若e(w)=(1−w)²(fσ−a)，式(11)给

\[
 \frac{e(w)-e(-w)}2=-2(λ_M-a)w.
 \tag{15a}
\]

对M-anti gauge B=(1−w)²b(w²)，H的odd部分精确为−2(λM−a)w b(w²)。增加finite zero只将首个odd项推到更高奇数阶，不能使它消失。

一般prefactor的证明同样允许B有有限zeros/poles。它不排除加入其它独立Eichler functions、真正的额外period projection、ramified pullback或不同analytic map。标准W下也有较简单的限定障碍：Fσ+Fσ|W=2V+≠0、Fσ−Fσ|W=2U≠0，因此任何W-eigen weight2 scalar gauge加一个constant均不能让fσ自动取得所需W-eigensign。

## 6. 真正rational trace有何所得、没有何所得

以γ′=(3,−1;−8,3)给M′=(−8,−3;24,8)，固定点−1/3+i√2/12。实q coefficients给

\[
 λ_{M'}=f_σ(ρ^{-1})=ψ-\frac{115}{4}iπ^3,
 \quad\frac{λ_M+λ_{M'}}2=ψ.
 \tag{16}
\]

这是新的真实endpoint projection接口；Tate虚部确实在两个endpoint的平均中消失。它没有成为同一个α叶上的正则投影：两complete period的qM分别中心±1/3，所以平均的完整polynomial仍为

\[
 \frac{λ_Mq_M+λ_{M'}q_{M'}}2
 =9ψ(1+8τ^2)-1380iπ^3τ.
 \tag{17}
\]

式(17)明确说明“endpoint trace纯实”不蕴涵“complete cycle没有Tate项”。coefficient trace f−+fσ=2u+2(Eχ−c)^[−3]也不是W-eigen；它不能由单一ξ∈Q或K假设消去另一个真实周期ψ。若另行构造additive twists的modular source与共同cycle，需要重证其level、constant terms、除子、integer t模型及period，而不是将(16)当成已完成的CDT输入。

还有一个不依赖Tate项的算术区别。实际身份ψ+ξ=−1155ζ3；若假ξ∈K且进一步误设ψ=σξ，则Trace_K/Q ξ=−1155ζ3∈Q，与ζ3已知无理矛盾。因此即使在endpoint trace中删去iπ³，ψ也不能成为所假代数ξ的共轭。若假ξ∈Q，则ψ∉Q是相同身份的条件性推论；这里没有无条件声称ψ无理。λM本身的超越性由其非零代数倍π³虚部与π已知超越直接推出，这是已知Tate事实的推论，不是新的odd-L目标结果。

## 7. 合法的number-field holonomy下一步及范围

在(2)下，K[[q]]函数H=B0(f−−ξ)，例如B0=E2−8E2(8τ)，其第二embedding是实际q germ B0(fσ−σξ)。第一embedding在W的canonical α可去；第二embedding不能删除式(7)/(14)中的ψ与π³，也不能免费解除M的canonical α。

CDT数域版本仍允许不同embedding使用不同analytic maps。第二embedding可在未解除branch前选避开αM的域，或者令该branch的所有interior fibers具有偶数ramification；它保留真实K系数germ而无需额外数值假设。若要选择更大fullfilled leaf，必须实际证明该cover上所有branch、cusp与q=0的延拓及unique-zero条件，并把第二embedding的derivative/边界增长成本完整计入数域平均。把q芽搬运到有已证有限阶微分方程的实际t模型也仍需完成；q modularity本身不替代CDT要求的holonomicity。我们未在本稿构造该map、求其capacity或证明其预算足够。

若目标是无需ramification的共同大叶，则现有source至少还需要一个实际处理ψ与π³载体的机制。使用λM作为shift会引入不在K中的constant和错误算术germ；使用formal σξ=ψ会虚增一个未经证明的真实数值关系。Beukers p281的合法替代是对第二embedding原始函数给较小radius，然后做product/norm，不是给两个embedding同样的Fricke消去。

本稿闭合的结果是：完整真实周期、对偶lift的正确α、精确Tate项，以及所述scalar prefactor族的全尺度障碍。没有证明所有mixed方法失败，也没有证明新的ζ3/L3数值结论。

## 8. 新固定证书

同名[verify脚本](cdt_odd_level8_mixed_embedding_20261006_verify.py)及[JSON](cdt_odd_level8_mixed_embedding_20261006_verify.json)含76项本轮固定精确核验，作者一次执行全部通过：矩阵与Sym² period、critical Bernoulli sums、root-of-unity finite kernels、residue cancellation和各有理系数。完整Mellin/解析延拓/T-periodic prefactor论证由正文承担；有限checks不替代这些证明。不执行旧或下载producer。

## 9. 实际独立审阅与冻结范围

- root实际完整只读本稿主段落§§1–8，限定认可完整周期/finite parts/任意scalar modular prefactor的证明链，并另提供§6的conditional algebraic-trace区别。未将prefactor-family障碍外推全CDT；第二embedding小域/ramified map保持正接口。
- conjugate_projection实际只读§§2–6，含新增(6a)的全文，独立从原始Lambert求三个finite imaginary coefficients及1/ε抵消、重推M/Bol的一维period、Laurent signs、entire Mellin/functional equation、prefactor的T-periodic矛盾和完整trace残项，限定审阅通过。没有运行本稿producer，也没有审阅全部76项实现；没有构造§7的map或认领任何新算术收益。其独立[审阅稿](cdt_odd_level8_mixed_period_review_20261006.md)及同名证书由该分支单次执行29项固定checks，正文审阅范围与本稿作者证书相互区别。

本稿冻结不涉及原三候选稿和其它旧报告。不由这些核验宣布新的无理性、最优level或全CDT不可能性。
