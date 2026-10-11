# 第234轮补充：完整三维源的固定有理换基费用下界

2026-10-08，Packet/B。独立纸核Root提出的有限模块诊断。冻结B234主稿9529 B / SHA256 ca350ab2f584583fe0146684afb112867280d73dc92b44036037945051dc2f03不改。这里仅讨论固定g∈Q、固定u坐标及固定Q(u)换基；数学程序0，不扫描、不执行旧producer。

## 1. 精确量词与目标

沿用E=Σ3ⁿuⁿ/(2n+1)、S=√(1−4u)、J_g=S(g−2I)，

\[
I_n=\frac1n\sum_{j=0}^{n-1}
\frac{3^j}{2j+1}\binom{2(n-1-j)}{n-1-j},
\qquad
J_g'+\frac2{1-4u}J_g=-2E.
\tag{B1}
\]

令V=span_{Q(u)}{1,E,J_g}，已付实际rank3。对f∈V∩Q[[u]]，δ_f(N)表示0,…,N的最小共同正整数分母，定义下率
ν(f)=liminf_(N→∞) logδ_f(N)/N。
f=aJ_g+bE+c，a,b,c∈Q(u)固定，允许各自有有限Laurent极点，组合f在0解析。本文证明

\[
a\ne0\Longrightarrow \nu(f)\ge3,\qquad
a=0,\ b\ne0\Longrightarrow \nu(f)\ge2.
\tag{B2}
\]

一切例外素数和端点常数可依赖f、g，但不依赖N。任意固定Laurent芽也可先乘固定u幂再应用，有限移位不改这些下率。这里不允许换基随N或p改变。

## 2. p²层：最低Laurent项保留双极点

固定a≠0，写a(u)=a_αu^α+…，a_α≠0。除有限素数外，a、b、c的整个Laurent展开在Z_p，a_α和g的分母均为p单位：将每个rational函数写成u^e times两个Q[u]多项式之比，排除系数分母和分母常数项的prime即可。

对充分大p>3，记k=(p−1)/2。B1在n=p处唯一inner p极点为j=k，中心二项式binom(p−1,k)≡(−1)^k，因此

\[
p^2J_{g,p}\equiv-2(-3)^k\ne0\pmod p.
\tag{B3}
\]

全部J_ℓ、ℓ<p至多simple p极点。取f的第p+α项：a的最低项恰乘J_p；较高Laurent项只乘J_ℓ、ℓ<p，故不贡献p²主项。bE涉及的下标至多p+一个固定常数；当p充分大时2j+1<3p，故最多simple p极点；c亦p整。所以

\[
p^2[u^{p+\alpha}]f
\equiv-2a_\alpha(-3)^k\ne0\pmod p.
\tag{B4}
\]

存在固定C_f，使全部充分大p≤N−C_f在f的完整prefix强迫至少p²分母。这论证保留a的所有Laurent项，没有把a视作常数或忽略有限头。

## 3. p>N层：完整残差由固定非有理级数控制

取p>N+C_f并把C_f增大到超过a、b、c所有Laurent负阶。于是算f的0,…,N项时，所需E、J原系数全部下标<p。该范围只有一个inner p极点：

\[
pE(u)\equiv3^ku^k,\qquad
pJ_g(u)\equiv3^ku^{k+1}A(u)
\quad\text{在所需截断内}\pmod p.
\tag{B5}
\]

这里A∈Q[[u]]与p无关，由

\[
uA'+\left(\frac12+\frac{2u}{1-4u}\right)A=-2,
\qquad A(0)=-4
\tag{B6}
\]

唯一确定。证明B5：将pJ的残差写成3ᵏu^(k+1)A，在J的完整ODE中用k+1≡1/2 modp即得B6。系数递推的对角因子为j+1/2；所需j≤p−1−(k+1)=k−1，分母2j+1<p，故归约确实有定义。全部此前系数p整，初值由首次inner极点给−4。这同时支付截断边界和全部finite heads，不是仅匹配首项。

A不是Q(u)中的rational函数。除以u后其ODE为
A′+[1/(2u)+2/(1−4u)]A=−2/u，方括号在∞为O(u⁻²)。若rational A的∞ degree≥1，其导数主项为非零常数或更高幂，不能等于−2/u；若degree≤0，整个左侧为O(u⁻²)，亦不能匹配。因此

\[
D_f(u):=a(u)uA(u)+b(u)\ne0
\quad(a\ne0).
\tag{B7}
\]

取它的首个非零Laurent项d_0u^{j_0}，d_0∈Q×。排除d_0分子分母的有限prime，B5给完整f残差

\[
pf(u)\equiv3^ku^kD_f(u),\qquad
p[u^{k+j_0}]f\equiv3^kd_0\ne0\pmod p.
\tag{B8}
\]

再次增大固定C_f，可同时保证N+C_f<p≤2N−C_f时0≤k+j_0≤N，以及全部Laurent卷积所需原系数<p。于是该整个窗口强迫至少p分母。所有模p式仅在这些明确截断内断言；不将B5声称为无截断的Fp全级数恒等式。

结合B4和B8，PNT给

\[
\log\delta_f(N)\ge
2\vartheta(N-C_f)+
\vartheta(2N-C_f)-\vartheta(N+C_f)-O_f(1)
=3N+o(N).
\tag{B9}
\]

固定端点损失及有限badprime不改主率，证明B2第一式。

## 4. 纯E行与完整basis的basic CDT下界

若a=0、b≠0，写b=b_βu^β+…，对充分大p其首项为p单位。E的首次p极点在k=(p−1)/2，此前E系数p整；故
p[u^(k+β)]f≡b_β3ᵏ≠0 modp。
所有充分大p≤2N−C_f均出现于完整prefix。PNT即给ν(f)≥2，完成B2。

V中的rational子空间维数1，span{1,E}维数2。因此任意固定Q(u)-basis f₁,f₂,f₃⊂Q[[u]]的三项下率排序后至少(0,2,3)：至少两项不rational，至少一项含非零J分量。

现仅考虑CDT Theorem2.5.1的**basic数组**，即各列为leading zeros后接一个共同非负常数，完整nth系数由这些LCM乘积清整；固定整数清分母允许先乘，每项下率不变。设其有序row sums为σ₁≤σ₂≤σ₃。完整prefix的分母整除对应截断LCM乘积，所以logδ_(f_i)(N)≤σ_iN+o(N)。B2及上述维数强迫σ₂≥2、σ₃≥3，从而

\[
\tau(b)=\frac{\sigma_1+3\sigma_2+5\sigma_3}{9}
\ge\frac73.
\tag{B10}
\]

冻结B234数组(0,2,2)、(0,0,1)达到7/3。故这是完整V的固定rational basis、固定u坐标、basic数组范围内的sharp费用，不只是某一safe表的upper。它不是随D/N改变的多项式source lattice下界，也不覆盖CDT更精细literal/integral types、algebraic换源、其它变量、删掉部分源或新载体。

## 5. 从费用到关系敏感准入的准确范围

对同一完整V的共同holomorphic φ，c=|φ′(0)|。任一固定rational basis的meromorphic pullbacks与原basis等价；rational系数复合只引入允许的极点。CDT能量有普遍下界J(φ)≥log c，故要由其rank3 bound得到矛盾，必须

\[
3(\log c-\tau)>J(\phi)\ge\log c,
\qquad
\log c>\frac32\tau\ge\frac72.
\tag{B11}
\]

e^(7/2)是rank矛盾的必要大小；不要把它误写成Theorem2.5.1本身的holonomic门槛e^τ。若另有针对所有共同φ的实际容量cap c≤3π³√2/8<18<e^(7/2)，则B11排除这里全部固定basic换基入口。本文没有重新证明该cover容量cap或代替其独审；该结论按另一个已付cap的范围合并。仅ν≥3自身不能排除更精细共同整模型或另一个数值源。

实际scope：本轮已实际FULL读取冻结B234全文及已存CDT primary物理PDF16–20完整选页文本，含Theorem2.5.1全部条件/数组和2.7.1的J≥log c论证；未冒称全文220页。Root先提出B3/B5接口，本人独立纸核上述Laurent、finiteprefix、非rational性和所有量词。仅NEW234补充，数学程序0；保存后实际FULL作者复读并另报bytes/SHA。
