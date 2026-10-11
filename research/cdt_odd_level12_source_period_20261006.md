# Level12 pure L3χ12 的真实双lift周期 candidate

日期：2026-10-06。新建记录；不修改已冻结的candidate/mixed报告，不作parameter或prime扫描。本文在明确的四维Eisenstein source空间中完成三个线性约束，得到一个非零、整系数、pure L3χ12 source及两个真实周期。没有证明L3χ12无理性；实际t整模型、field-conjugate坐标、rank和CDT预算仍待完成。

## 1. 有限source空间与正确oldscale因子

记r=√3、K=Q(r)、χ=χ12、κ=24r。采用常数项1的E4以及

\[
 E_χ=23+\sum_{n\ge1}\frac{χ(n)n^3q^n}{1-q^n},
 \qquad F_χ=\sum_{m,n\ge1}χ(n)m^3q^{mn}.
\]

χ在mod12的units1,11取+1，5,7取−1。B2χ=4、B4χ=−184，故L(−1,χ)=−2、L(−3,χ)=46。来自[已核Fricke归一化](cdt_odd_candidates_5_8_12_20261006.md)的Eχ|W12=κFχ、Fχ|W12=Eχ/κ。

在Γ=kerχ⊂Γ0(12)上取

\[
 G_1=E_4-144E_4(12τ),\quad
 G_2=E_4(2τ)-9E_4(6τ),\quad
 G_3=E_4(3τ)-\frac{16}{9}E_4(4τ),\quad C_-=E_χ-κF_χ.
 \tag{1}
\]

三G均为trivial-character；C−为χ-character。E4(jτ)|W12=144E4(12τ/j)/j⁴，所以G3的系数必须为16/9，不能写成4。所有四source均W12-anti。Γ包含T:τ↦τ+1。

令F−=aG1+bG2+cG3+dC−。∞constant为−143a−8b−7c/9+23d，所以

\[
 23d=143a+8b+7c/9.\tag{2}
\]

正次数第三Dirichlet period的trivial部分为

\[
 ξ_U=(-110a-10b-10c/9)ζ(3),\qquad ξ_C=12rdL(3,χ),\quad ξ=ξ_U+ξ_C.
 \tag{3}
\]

这是240ζ(s)ζ(s−3)乘实际oldscale polynomial在s3取值，不是猜测的formal conjugate。ξU=0准确等价于

\[
 c=-99a-9b,\qquad d=(66a+b)/23.
 \tag{4}
\]

这些约束只限(1)的finite source空间；不声称所有目标或方法的最小level。

## 2. 共轭source与唯一指定的canonical七阶根

σ只作用于r的代数系数。Fσ=aG1+bG2+cG3+dC+，C+=Eχ+κFχ。Γ0(12)中

\[
 γ=\begin{pmatrix}7&2\\24&7\end{pmatrix},\quad χ(7)=-1,
 \quad M=γW_{12}=\begin{pmatrix}24&-7\\84&-24\end{pmatrix},\quad M^2=-12I.
 \tag{5}
\]

γ保持trivial部分、反号χ部分；C+为W-plus，因此Fσ|M=−Fσ。M正规化Γ，M∞=2/7，固定点2/7+i√3/42。对满足(2)的source，∞和2/7两端的constant均为0。令fσ=θq^-3Fσ、fσ∞=0，Bol身份及M²central给

\[
 f_σ(τ)+\frac{(84τ-24)^2}{12}f_σ(Mτ)
 =λ_σ\{1+12(7τ-2)^2\},\qquad
 λ_σ=f_σ(e^{4πi/7}).
 \tag{6}
\]

理由是左边三次导数为0，是Sym²M的+eigen quadratic，空间为一维；取τ→2/7+i0固定λ。没有额外自由的一次period。式(6)是真正的M cocycle，不能以普通W12下的L3直接替代它。

以下只计算这一canonical root，ρ=e^{2πi/7}、q=ρ²e^-ε；不搜其它endpoint或参数。

## 3. 普通Lambert kernel的精确有限Bernoulli式

记T(q)=Σn≥1 n^-3 q^n/(1−q^n)。普通T与下一节χ生成kernel不同。对h=1,…,6，减去radial pole后

\[
 \operatorname{FP}T(ρ^h)=-ζ(3)/2+iπ^3\mathcal T(h),\qquad
 \mathcal T(h)=\frac1{21}\sum_{m=1}^6\{7-2[mh^{-1}]_7\}B_3(m/7).
 \tag{7}
\]

这里[·]7取1,…,6，B3(x)=x³−3x²/2+x/2。可不用浮点cot值证明(7)：在7阶roots上定义finite polynomial

\[
 K_h(x)=-\frac12+\sum_{m=1}^6\left(\frac12-\frac{[mh^{-1}]_7}{7}\right)x^m.
\]

对x=ρ^n、7∤n，它恰等于x^h/(1−x^h)；对x=1，它为−1/2，即真实radial finite part。准确的finite polynomial恒等式是(1−x^h)Kh(x)−x^h≡−Φ7(x)/7 mod(x⁷−1)，因此在primitive roots上右边为0；并未声称在x=1也作原分式除法。除constant外，其coefficients在m↦7−m下反号；Euler–Bernoulli Fourier身份Σn≥1 sin(2πnx)/n³=2π³B3(x)/3遂给(7)。仅对7|n的radial pole terms减去1/(εn)，余项绝对值≤1/2；对7∤n不作该减法，有限phase的kernel统一有界。因此n^-3求和可用dominated convergence。

所有needed phases的固定结果是

\[
 (\mathcal T(1),\ldots,\mathcal T(6))
 =(12,4,0,0,-4,-12)/343.
 \tag{8}
\]

E4(jτ) primitive为240j^-3T(q^j)。在q=ρ²处，三个trivial source的imaginary coefficients（除iπ³）分别为

\[
 A=240\{\mathcal T(2)-\mathcal T(3)/12\}=960/343,
\]
\[
 B=30\mathcal T(4)-10\mathcal T(5)=40/343,
\]
\[
 C=(80/9)\mathcal T(6)-(20/3)\mathcal T(1)=-80/147.
 \tag{9}
\]

这不是χ生成kernel在其它phase的值；把两者混用会得到错误的oldscale系数。

## 4. χ Eisenstein的两个精确Tate coefficients

Eχ去constant后的primitive是Σn≥1 n^-3 eχ(q^n)，其中

\[
 e_χ(z)=\frac{z-z^5-z^7+z^{11}}{1-z^{12}},\qquad e_χ(1)=0\quad\text{（可去）}.
\]

在canonical q=ρ²处，finite polynomial为

\[
 e_χ(ρ^{2n})=P(ρ^n),\quad P(x)=x-x^3+x^4-x^6.
 \tag{10}
\]

乘(1−x²⁴)后，等式的numerator是x²−x¹⁰−x¹⁴+x²²，按x⁷−1取余完全相等，且P(1)=0。P coefficients反号，故实部为0，由B3 Fourier身份

\[
 \mathcal E=\frac23\{B_3(1/7)-B_3(3/7)+B_3(4/7)-B_3(6/7)\}
 =12/343.
 \tag{11}
\]

Fχ primitive是Tχ(q)=Σn≥1 χ(n)n^-3 q^n/(1−q^n)。对普通finite kernel Kh的每个Fourier term，以primitive even Gauss身份χ(n)=12^-1/2Σa=1^12χ(a)cos(2πan/12)展开。乘κ=12√12，正好消掉Gauss根。canonical h2的inverse是4，得到完全有理的有限表达式

\[
 \mathcal F:=\frac{\operatorname{Im}\operatorname{FP}(κT_χ(ρ^2))}{π^3}
 =\frac{12}{3\cdot7}\sum_{m=1}^6w_m\sum_{a=1}^{12}χ(a)
 B_3\!\left(\left\{a/12+m/7\right\}\right),
 \quad w=(-1,5,-3,3,-5,1).
 \tag{12}
\]

因χ even，内层sum是m↦7−m下odd。前3项是311/2352、383/2352、1/14；总Σw·inner=275/294。因此

\[
 \mathcal F=550/1029,\qquad
 J:=\mathcal E+\mathcal F=586/1029.
 \tag{13}
\]

这里所有系数都是有限rational Bernoulli sums精确所得，没有从浮点识别rational。实部只来自κFχ finite part−κL3χ/2，所以C+的真实endpoint real part为−12rL3χ。

完整source的radial pole也必须保留再消去。T(q^j)的pole是ζ4/(7⁴jε)，Tχ(q)的pole是χ(7)L4χ/(7⁴ε)。χ(7)=−1，而

\[
 κL(4,χ)=\frac{115}{3}ζ(4).
\]

若trivial展开coefficients为u_j，W-anti和(2)给Σu_j/j⁴=23d/144，所以240Σu_j/j⁴=115d/3。trivial和χ pole准确抵消；real/imag finite parts确为实际fσ radial limit，不是任意regularization。

## 5. 三个线性约束闭合：非零的pure目标与Tate消去

由(3)、(9)、(13)，完整canonical period是

\[
 λ_σ=ξ_U-12rdL(3,χ)
 +iπ^3\left(\frac{960a}{343}+\frac{40b}{343}-\frac{80c}{147}+\frac{586d}{1029}\right).
 \tag{14}
\]

在ζ3-free约束(4)下，Tate linear form恰为

\[
 \frac{28164a+2434b}{483}.
 \tag{15}
\]

三个constraints（∞zero、ζ3-free、Tate-free）在有限四维source空间中rank3。取唯一nonzero方向的integer代表

\[
 (a,b,c,d)=(1217,-14082,6255,2880).
 \tag{16}
\]

关键是d≠0，目标没有被消掉。G3的rational factor也被6255整除，source可写成完整integer model

\[
 \boxed{F_-=1217E_4-14082E_4(2τ)+6255E_4(3τ)-11120E_4(4τ)
 +126738E_4(6τ)-175248E_4(12τ)+2880E_χ-69120rF_χ.}
 \tag{17}
\]

其∞constant为0，positive q coefficients在O_K=Z[r]；无需从几项sample推出整性。真正原支和共轭lift period是

\[
 \boxed{Θ=34560rL(3,χ_{12}),\qquad λ_σ=-Θ.}\tag{18}
\]

式(18)是无条件的两个实际period身份；“−Θ等于σΘ”只有在以下正确数值假设中才成立。

## 6. 保留完整L1/2/3与constant corrections

F−在W12下anti且两端constant0。其positive Dirichlet series的trivial factor在s1和s3都为0；χeven functional equation给L′χ(−2)=−72rL3χ/π²。所以

|source|L1|L2|L3|∞constant|W∞constant|
|---|---|---|---|---:|---:|
|F−|−6Θ/π²|0|Θ|0|0|
|Fσ|−6Θ/π²|−1920π²|−Θ|0|132480|

对f−=θq^-3F−和fσ=θq^-3Fσ，两个实际eigen identities为

\[
 f_-+12τ^2f_-(W_{12}τ)=Θ(1+12τ^2),
 \tag{19}
\]
\[
 f_σ+12(7τ-2)^2f_σ(Mτ)=-Θ\{1+12(7τ-2)^2\}.
 \tag{20}
\]

但是Fσ在普通W12下仍不是eigen。令Gσ=Fσ|W12、gσ=θq^-3(Gσ−132480)，完整pair Laurent identity是

\[
 f_σ-12τ^2g_σ(W_{12}τ)
 =-Θ+12Θτ^2-3840iπ^3τ+\frac{3680iπ^3}{3τ}.
 \tag{21}
\]

式(21)由[完整非cuspidal Mellin identity](cdt_odd_level8_mixed_embedding_20261006.md)及上表得到；没有删去中间L2、reciprocal constant或把M误当W。新positive机制是换成真正的共轭lift M并在其endpoint精确消去Tate，而非σsource的普通L2变成0。

## 7. Irrationality假设下真实双embedding正则化

为尝试证明L(3,χ12)∉Q，只假设L(3,χ12)∈Q。这时Θ=34560r·rational∈K且σΘ=−Θ，是实际已假代数数的共轭；不需要对未知真实L值定义σ。取真实modular weight2

\[
 A=E_2-12E_2(12τ).
\]

E2的quasimodular correction消掉，A为Γ0(12)的trivial-character form，A|W12=−A。γ∈Γ0(12)，故A|M=−A。由(19)、(20)，两个实际q germs

\[
 H_-=A(f_--Θ),\qquad σH_-=H_σ=A(f_σ+Θ)
 \tag{22}
\]

分别在W12和M的canonical quadratic quotient上全纯下降。它们分别对T和对应involution不变，因而下降到生成群〈T,W12〉与〈T,M〉的实际叶；∞处由q=0填充、相应canonical elliptic point由已证identity填充。upper-half-plane内A和f均全纯，局部coarse holomorphic下降不依赖guess endpoint。分歧点处的所有odd carrier已由相容的真实period消去。

这只针对rationality of L3χ12。若仅假Θ∈K，σΘ=−Θ不一定成立；等价条件正是Θ的trace0，即L3χ12∈Q。不能将(22)提升为L3χ12不属于K的假设触发器。

source integer q coefficients及θ^-3给L_n³ f_n∈O_K，A也有integer q coefficients。rationality假设的固定分母D0清掉Θ后，D0L_n³(H−)_n与其真实共轭均在O_K；卷积通过j|LCM(1,…,n)的整除性保证全尺度成立。这是q整模型，不自动等于CDT的t整模型或G-function论证。

## 8. 精确正进展及尚未闭合的几何/预算

这是level12 genuine pure L3χ12的双lift period candidate，跳出了旧pure χ的unmixed three-oldscale ansatz（该旧ansatz给level48）。并未违反旧最少scales结论，因为(17)引入了trivial-character weight4 Eisenstein oldscales。

Γ=kerχ12的compact curve是genus0（Γ0(12) genus0，character cover只有denominators2与6的两个branch cusp，Γ的10 cusps及index48也直接给genus0）。W和M正规化Γ，它们在该compact genus0曲线上的非trivial involution quotient也为genus0。然而这些复解析quotient并未在本稿被识别为带K结构的相互Galois共轭Hauptmodul；不能仅凭genus0和(22)代用一个未给出的t。

明确下一步是：给实际t−∈qK[[q]]及σt−、证明其quotient分别匹配W和M；全尖点/branch divisor及完整逆q整性；实际finite rational ODE与rank；两filled leaf上的t全纯、全部interior branch fibers、omissions及unique-zero；最后重算完整数组的denominator和number-field analytic平均。

M的固定点中心2/7可以移到0；在z=τ−2/7中，M作用为z↦−1/(588z)。所以生成群〈T,M〉等价于这一个Hecke参数为√588的解析群。这个数只标明实际第二叶的几何，不代表其代数模型level升到了588，也不能由它推断budget失败；尚需上述actual t/metric和capacity计算。

本文没有求capacity、没有证明arithmetic holonomy界小于actual rank，也没有给无理性或新的数值linear independence结论。与此前Tate始终不能删除的固定mixed模型相比，这里确实得到一个可以继续完成模型与预算的真实positive输入。

## 9. 新一次固定证书

[新verify脚本](cdt_odd_level12_source_period_20261006_verify.py)及[JSON](cdt_odd_level12_source_period_20261006_verify.json)含68项固定精确核验，作者本轮仅一次执行全部通过：Bernoulli inner sums/finite kernels、三个oldscale因子、M与Sym² quadratic、完整三个linear constraints、integer展开、critical L2/L4及ordinaryW Laurent coefficients。没有parameter/prime扫描，不运行旧或下载producer。

有限checks不替代(6)的global modular/Bol proof、(7)/(12)的Fourier identities与dominated limit、(22)的实际解析下降。尚未验证本节列出的t/rank/fullleaf/CDT输入。

## 10. 实际独立审阅范围

- helper_tensor_budget实际只读§§2–5及新脚本（未执行），独立有限Fourier/B3重算普通Lambert phases、三个trivial Tate coefficients、χE kernel、scaledχF=550/1029、charplus总586/1029、Tate linear constraint与integer witness，限定通过。其关于radial pole减法只限7|n、Kh的cyclotomic remainder的scope澄清已在§3补齐，见[独立有限审阅](cdt_odd_level12_source_period_finite_review_20261006.md)。没有审阅§§6–8的几何/整模型，也没有执行作者68项checks。
- conjugate_projection实际全文阅读，限定独审通过§§2–7：有限B3/Gauss与λσ、全部constraints、ordinaryW的完整Laurent身份、真实W/M双period、仅L3∈Q假设下的合法σΘ=−Θ、A双anti及canonical germ下降。没有运行或审阅本稿producer，也没有补§8的fullleaf/cost。其不同paired-coordinate模型若另行闭合，由独立新稿承担，不能自动计为本稿已经完成的输入。

这些审阅不扩大positive candidate的范围，不提供无理性主结论，也不把canonical branch可去当成全部fullfilled leaf判据。
