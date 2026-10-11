# R 校正族的多反射、全 Γ 周期接口与实际增强解析叶

日期：2026-10-06。本文只读[冻结整数校正族](cdt_odd_level12_zero_period_corrector_family_20261006.md)作为输入，不执行/import其producer，不作研究参数、短word或素数扫描。新的全尺度结论是：同一个scalar不能使两个不同J_n为zero，但每个实际校正源自动有一个不同的mirror zero reflection，从而确有双反射augmented full leaf。其它det12反射给完整、可验证的rational period条件；尚未分类全部稳定子。

## 1. 两个 J_n 不能共用同一校正

沿用 \(\eta=(1,0;12,1)\)、\(J_n=\eta^nM\eta^{-n}\)，
\[
s_n=644n^3+552n^2+147n,\quad
p_n=84n^2+48n+7,\quad
a_n=24+84n,\ c_n=12p_n.
\]
冻结的完整polynomialidentity给
\[
c_{L+sR}(J_n)=\frac{1920}{7}(s_n-s)i\pi^3Q_n,\qquad Q_n\ne0.
\tag{1}
\]
因此同一source同时kill \(J_n,J_m\) 的准确条件是 \(s=s_n=s_m\)。对所有整数
\[
s_{n+1}-s_n=1932n^2+3036n+1343\ge239.
\tag{2}
\]
n≥0时显然≥1343；写n=-k-1、k≥0时右式为 \(1932k^2+828k+239\)。故整数族strictly increasing，只有n=m可能。没有从real derivative的符号推integer单调。

另一个直接all-pair核：令u=n+m、v=n-m，v非零，则
\[
\frac{s_n-s_m}{n-m}
=483(u+92/161)^2+161v^2-1725/161
\ge24196/161>0 .
\]
这个整数差限制不排其它reflection orbit。

## 2. Real q结构给第二个实际 zero reflection

对任意固定real s，目标
\[
h_s^+=\sigma f_L+s f_R+\Theta
\]
在upper half-plane满足 \(\mathfrak r\tau=-\bar\tau\) 下
\(h_s^+(\mathfrak r\tau)=\overline{h_s^+(\tau)}\)：q系数与实际Θ全为real。这是ordinary complex conjugation，不是对未知L值作number-field σ。

对real matrix g、det>0，令 \(g^\mathfrak r=\mathfrak r g\mathfrak r\)，直接代入det-normalized weight−2 slash给
\[
(h|_{-2}g)(\mathfrak r\tau)
=\overline{(h|_{-2}g^\mathfrak r)(\tau)} .
\tag{3}
\]
因此若 \(h|_{-2}g=-h\)，也有 \(h|_{-2}g^\mathfrak r=-h\)。对s=s_n，
\[
\boxed{\widetilde J_n=
\begin{pmatrix}-a_n&-7\\c_n&a_n\end{pmatrix}
=\eta^{-n}M'\eta^n,\qquad
h_{s_n}^+|_{-2}\widetilde J_n=-h_{s_n}^+.}
\tag{4}
\]
这里 \(M'=(-24,-7;84,24)\)。\(\widetilde J_n\)不是任意整数m的J_m：第一行相等要求m=-n-4/7。两个fixed centers不同，因为a_n≠0。所以(2)和(4)相容。

(3)证明完整function identity，不是用endpoint单点补一次项。源q系数的real性和primitive常数Θ都被保留。第一embedding仍用 \(h_{s_n}^-=f_L+s_nf_R-\Theta\) 的W对称；反证假设L∈Q时这两支正是K-arithmetic conjugate germs。

## 3. 全 n 双反射 augmented full disk

令 \(\zeta=(c_n/\sqrt{12})\tau\)，
\[
w_n=c_n/\sqrt{12}=2\sqrt3p_n,\quad
u_n=a_n/\sqrt{12}=(14n+4)\sqrt3.
\tag{5}
\]
T是translation by w_n，两反射是
\[
S_{\pm u_n}(\zeta)=\pm u_n-\frac1{\zeta\mp u_n}.
\]
isometric circles为center±u_n、radius1。取A=|a_n|≥24；由 \(a_n^2+12=7c_n\)，native circles位于width1 strip内且相离：
\[
|a_n|>\sqrt{12},\qquad
2(A+\sqrt{12})<c_n.
\tag{6}
\]
后一式乘7化为 \(A^2-14A+12-14\sqrt{12}>0\)；A≥24和√12<4给strict positive lower196。这样保证每个translated circle都与其它circle严格相离。

准确center间距是
\[
d_n=\min(2|u_n|,w_n-2|u_n|)>2.
\tag{7}
\]
n=0时d=6√3；n非零时 \(p_n>2|14n+4|\)，故 \(d_n=2\sqrt3|14n+4|\ge20\sqrt3\)。这两个分支由integer正、负的二次式直接证明，不作n样例扫描。

对
\[
\mathcal F_n=\{\zeta\in H:|\Re\zeta|<w_n/2,\ 
|\zeta-u_n|>1,\ |\zeta+u_n|>1\}
\tag{8}
\]
有完整fundamental-domain证明。reduced free-product word含最后一个inversion时，把F送入对应translated circle；下一inversion将相离circle送入自己的circle，最终interior与F相离，纯translation则落相离strip。这给discreteness和无额外relations。

覆盖也不能省略：先translate回strip，若在一个circle内则invert再translate。若下一步仍落另一个circle，两center距离≥d_n；上一点距center≤1/(d_n−1)，该次inversion把height乘至少 \((d_n-1)^2>1\)。未终止时height≤1，不能无限增长，所以算法有限终止。故(8)确覆盖。

因此
\[
G_n^{\rm aug}=\langle T,J_n,\widetilde J_n\rangle
\cong\mathbf Z*C_2*C_2.
\]
三个real boundaryinterval的端点按两involutions与translationglue后恰是一cycle，只有一个boundary。其唯一cusp是∞，两tip为order2 ellipses。将a_n必要时改正号、相应swap generators，该boundary holonomy为 \(T^{-1}J_AJ_{-A}/12\)，
\[
\operatorname{tr}
=\frac{(A-7)c_n-A^2}{6}
=\frac{A^3-14A^2+12A-84}{42}\ge142>2.
\tag{9}
\]
函数在A≥24严格增加，A=24给142。因此这是funnel，不是第二cusp。填∞、coarse化两个ellipses后，三个free factors都kill，underlying surface simply connected；有唯一analytic funnel boundary，所以是Riemann disk \(X_n^{\rm aug}\)。

真实函数
\(H_n^+=A_2h_{s_n}^+\)，\(A_2=E_2-12E_2(12\tau)\)，由(4)和modularweight2 anti真实保持两个reflections。t−也保持它们：η固定v，M、M′均发送v到−√3/v。两个canonical elliptic orbits均有实际even germ；其它Γ-fibers仍保留ordinary source ram2，不错误删除period。q Taylor填唯一cusp，t=q+…给唯一simple zero；interior无t零/pole。于是这个augmented disk确给合法第二embedding map。

同一 \(g_-=[1-4(2-\sqrt3)t+4t^2]^2\) 清全部ordinary critical点的native一、二阶derivative poles；已下降的两个coarse ellipses原本regular。因此完整四行仍holomorphic。q=e^(2πiζ/w_n)正是原q。新增盘是同一actual source的合法extension，而非借用别的source的zero group。

这里不计算actual radius，也不由domain外观假定容量改善；helper的Green/transport研究须引用这个实际leaf输入后另证。

## 4. 整个 Γ 的 R cocycle有 exact有限公式

记 \(r_j=(1,-66,495,-880,594,-144)\)，对reduced rational x=b/d、d>0定义
\[
G_{d,h}=\begin{cases}-1/2&h=0\\1/2-h/d&1\le h<d,\end{cases}
\]
\[
\mathcal R(b,d)
=160\sum_{j\mid12}\frac{r_j}{j^3}
\sum_{h=0}^{d-1}G_{d,h}B_3(\{bjh/d\}).
\tag{10}
\]
这里所有sum有限且值rational；不把它标成研究参数扫描。普通root kernel经pole finite-part归一后，Fourier的
\(\operatorname{Im}\operatorname{Li}_3(e^{2\pi ix})=(2\pi^3/3)B_3(\{x\})\)
给 \(f_R(b/d+i0)/(i\pi^3)=\mathcal R(b,d)\)，前提是该cusp source常数为0。Γ0∞及Γ00两cusp classes满足此前提；∞取0。

对任何 \(g=(a,b;c,d)\in\Gamma_0(12)\)，c_R(g)是Bol保证的degree≤2 polynomial。取固定 \(\tau_k=1/(12k),k=1,2,3\)，它和gτ_k均在Γ0∞ orbit，有真正finite limits；若gτ_k=∞，其slash term取真实limit0。于是
\[
\frac{c_R(g)(\tau_k)}{i\pi^3}
=(c\tau_k+d)^2\mathcal R(g\tau_k)-\mathcal R(\tau_k).
\tag{11}
\]
三个distinct points唯一确定完整polynomial。这是对整个Γ0，特别完整Γ=F9的确切决定接口；不是仅给一个endpoint或有限几个word的guess。其完整cocycle law仍由actualf_R的slash成立。

用固定完整Schreier九基、新有限公式及第四个independent seed \(1/48\)，得到完整实际 \(c_R/(i\pi^3)\) 表。这里只读冻结群/PL JSON数据，不执行旧producer。

|generator|R period vector in \((1,\tau,\tau^2)\)|同一 \(h_L+sf_R\) 的zero条件|
|---|---|---|
|x1|(-566400,-2674560,-3156480)|无scalar：与PL不成比例|
|x2|(0,0,0)|所有s，实际T|
|x3|(351520,898560,574080)|无scalar|
|x4|(-36400,-258240,-461760)|无scalar|
|x5|(-182480,-578880,-459840)|无scalar|
|x6|(-214880,-528000,-324480)|无scalar|
|x7|(-38480,-258240,-436800)|无scalar|
|x8|(27040,120960,136320)|无scalar|
|x9|(0,0,0)|无scalar：PL非zero|

Γ是这些矩阵生成的F9，因此表连同actualcocyclelaw确定整个Γ上的R，而不是仅有九个不知是否生成的样例。它不把“没有新增zero basis generator”当成“没有新增zero word”；多word相消仍须实际证明。

表还给准确的整数origin接口：所有 \(P_R(x_j)/80\) 属于
\(\Lambda=\mathbf Z+\mathbf Z\tau+12\mathbf Z\tau^2\)；
\(c_R(M)/(80i\pi^3)=(-168,1152,-2016)\) 在ordinarybasis中，也属于Λ。冻结的signed slash矩阵保持Λ，故R在整个 \(\Gamma\rtimes C_2\) 的translation都有该整模型。对 \(s=A/B\)，actualperiod条件可在同一整数affine状态中写成 \(B P_L(g)+A P_R(g)=0\)，无需浮点period判零。本文没有由整数接口推fullkernel生成性。

sourceconstant也给全scale限制：十Γcusps中，R在两∞/两0 slots均为0；其余六slots按c2,c3,c4,c6为
\[
B_2=-320/3,\quad B_3=525,\quad B_4=-2800/3,\quad B_6=960.
\tag{12}
\]
由Bol residue \(\beta=-4wB\)，这些非zero classes的任意nonzero parabolicpower、任意affineconjugate都没有fixedpoint，因此不能在R的origin stabilizer中。四个zero slots仅给fixedline必要条件；(10)–(11)仍须保留actualq-origin，不能声称R全kernel已经由T、W生成。

## 5. 所有 det12 χ− reflections的完整条件

任意这样的reflection可写成
\[
J(b,d)=\gamma W=
\begin{pmatrix}12b&-a\\12d&-12b\end{pmatrix},
\quad ad=12b^2+1,\ d>0,\ \chi_{12}(d)=-1.
\tag{13}
\]
其unsigned+1 eigline准确由
\(Q_J=1+(12d\tau-12b)^2/12\)生成。对actualconjugate primitiveh+和fR，source均J-anti，signed order2迫
\[
c_L(J)=i\pi^3\ell(b,d)Q_J,\quad
c_R(J)=i\pi^3\mathcal R(b,d)Q_J .
\tag{14}
\]
actualendpoint的realpart准确为−Θ；h+中的+Θ将其消去。ℓ是实际有限Bernoulli/Gauss coefficient，不是未知L的σ。例如完整source旧ordinary系数u_j给
\[
\ell=\sum_{j\mid12}\frac{160u_j}{j^3}
\sum_hG_{d,h}B_3(\{bjh/d\})
+2880\,\mathcal E(b,d)+2880\,\mathcal F(b,d),
\tag{15}
\]
其中
\[
\mathcal E=\frac23\sum_hK_{\chi,d,h}B_3(\{bh/d\}),\quad
K_{\chi,d}(x)\equiv
P_\chi(x)\Bigl[1+\sum_hG_{d,h}x^{12h}\Bigr]\pmod{x^d-1},
\]
\(P_\chi=x-x^5-x^7+x^{11}\)，取degree<d代表；d与12coprime，Pχ(1)=0保证kernel归一在1也正确。
\[
\mathcal F=8\sum_hG_{d,h}\sum_{z=1}^{12}
\chi_{12}(z)B_3(\{bh/d+z/12\}).
\]
factor8包含κχ=24√3与τχ=2√3，采用actualσsource的PLUSχF。全sourcepole residue由J-anti及∞zero取消；这个finitepart因此是实际primitive limit。

故若 \(\mathcal R\ne0\)，唯一合法corrector为 \(s(J)=-\ell/\mathcal R\in\mathbf Q\)；若R=0，必须ℓ也0才可kill。两different generalreflections能被同一sourcekill的确切条件为
\[
\ell_1\mathcal R_2-\ell_2\mathcal R_1=0
\tag{16}
\]
并分别处理R=0情况。这是完整polynomial/eigline条件，不仅endpoint假定。

这也覆盖完整K系数的two-source空间，而不只预先选rational s：若originalsource为 \(uF_L+vR\)、u非零、u,v∈K，在L∈Q假设下其conjugateprimitive除以σu后是 \(h_++\sigma(v/u)f_R\)。当 \(\mathcal R\ne0\)，反射zero强制 \(\sigma(v/u)=-\ell/\mathcal R\in\mathbf Q\)，故 \(v/u\) 本身就是这个rational scalar。u=0仅是零真实L-period的R方向，不能当作纯L目标触发器。

Jacobi symbol还严格限制位置：由12b²≡−1modd、(b,d)=1得
\((-12/d)=1\)。χ12(d)=-1于是 \((-1/d)=-1\)，所以d≡7mod12，d≥7。最小d=7时b≡±2mod7；全部这些reflections只是T-conjugates of M或M′，其校正只s=0。所有其它d≥19，principal single-reflectionwidth至少19√12。这不排多个reflection共同生成更大leaf，亦不把singlecirclewidth当augmentedradius。

两个下一层的明确source来自固定等式 \(12\cdot7^2+1=19\cdot31\)，不是参数search：
\[
\begin{array}{c|c|c|c}
(a,b,d)&\ell&\mathcal R&s=-\ell/\mathcal R\\ \hline
(31,7,19)&298560/19&5760/19&-311/6\\
(19,7,31)&402240/31&5760/31&-419/6 .
\end{array}
\tag{17}
\]
分别给 \(F_L-(311/6)R\)、\(F_L-(419/6)R\) 的真实pureL source；每个都保持第一W、使第二支完整reflectionzero，并由real结构保持mirror。它们不能被同一s同时kill。事实上 \(R\in240q\mathbf Z[[q]]\)，所以这里的fraction6在source q系数中完全取消；两新源仍有 \(\mathcal O_K\) q系数，不新增固定q分母，也不改变primitive的k³分母指数。L∈Q的反证假设使两支germs真正是K-conjugates，沿用actualprimitive常数±Θ。

更一般地，对任何(13)且R非zero的reflection，rational \(s(J)\) 都得到合法两embeddingmodel；geometry也不是条件式猜想。先用T-conjugation把b取centered residue \(0<|b_0|<d/2\)。必须 \(|b_0|\ge2\)，否则d|13与χ(d)=-1矛盾；也必须 \(d-2|b_0|\ge3\)，否则d|4。standardizedcenters为±√12b0、width√12d，所以translatedcircle最小间距
\[
\sqrt{12}\min(2|b_0|,d-2|b_0|)\ge6\sqrt3>2.
\]
同§3的完整覆盖、singleboundarycycle与actualprimitive下降给augmentedfilleddisk；boundarytrace为
\[
24|b_0|(d-2|b_0|)-2\ge142>2.
\tag{18}
\]
这提供所有eligibleχ−reflections的实际source/leaf接口，但没有证明这些两circle盘容量超过旧n0，亦未把其最大group误当fullstabilizer。

## 6. 旧源加sR的全部residue-zero与lower-degree缺口

在actualsource \(F_L+sR\) 或σsource，c2/c4常数准确为
\[
B_2(s)=-\frac{320}{3}(s+113),\qquad
B_4(s)=-\frac{2800}{3}(s+919/35),
\]
\(B_6=-9B_2,B_3=-9B_4/16\)。其它noncanonical∞/0slots仍为−132480、920。因s_n的整数strictgrowth，s_n从不等于−113或−919/35。因此整个integerfamily的四个forbiddenG* peripheral classes仍由非zeroBol residue排除所有conjugate nonzero powers。

对任意rational s，唯一可能额外zero-residueclasses只有上述两值。即便那里，standard actualprimitive也未zero：s=-113时
\[
\theta_qf^-(-1)=152640\zeta(2),\qquad
\theta_qf^+(-1)=118080\zeta(2).
\]
相应cusp−1/2、width6的constant period分别为−305280iπ³和−236160iπ³。s=-919/35时，q=i endpoint减掉各实际Θ后分别为
\(24792i\pi^3/7\)、\(51672i\pi^3/7\)，亦非zero。它们来自wholefamily finite kernel公式，并保留σsourceχF的相反符号。

这些lowerdegree值不排zero-residueclass的所有conjugates：β=0时affinefixedline存在，是否origin位于某个conjugatefixedline仍是actualorbit问题。不能从这两representatives推全kernelno-go。

## 7. 范围与审阅

新的可用正接口是每个fixedinteger实际source的双反射full disk。R的完整Γ周期有(10)–(11)的exact接口，generalχ−reflection有(14)–(16)的可验证完整条件；本文没有声称完整origin stabilizer已分类，也没有新的数值无理性或预算改进。

新同名NEW producer第一次、单次执行50项checks全部通过；输入冻结periodJSON pin SHA=b8dfb80d30a4fc276d225d148c76ead7032de51523896664f5c743eb0af966ef，仅作为数据读取。新实现独立重算完整九基R表、第四点检查、指定canonical/n1及(17)的有限Bernoulli normalization，并核全integergeometry、sourceexception/lowerdegree系数。没有word/prime/研究参数扫描，未执行/import冻结producer。有限cert不替代正文wholeΓ、signedeigline与fundamental-domain证明。

conjugate_projection独立理论核(1)的all-integer差factorpositivity通过；未将此记录成实际全文审核。helper_tensor_budget实际只读本文§§1–3，限定数学链通过：real-slashmirror、a²+12=7c与all-n circles、height-growth覆盖/freeproduct、singleboundarycycle/trace≥142、真实H/t descent、cusp/gauge及保留其它ram2。helper另实际只读更新§5中其Green推导所使用的matrix/Jacobi/centered circles与合法zero pair；未认领全部有限Bernoulli值、§4完整table或§6，未执行任何producer。

root实际完整读取最终本文§§1–7及同名verify.py全文，通过完整period finite-Bernoulli、三点决定全polynomial、signed eigline、多反射full leaf、§4table/Λ、§5完整K-span rationalratio与source q整性/general circle geometry的数学链。root未执行producer，本次不认领重新构建此前全部source cusp模型；JSON直接数据核对另由root外部记录。此审阅不把pair leaf扩大为full origin stabilizer，不把新真实source扩大为新数值无理性结论。本文与同名PY/JSON现冻结，任何后续扩充另建文件。

