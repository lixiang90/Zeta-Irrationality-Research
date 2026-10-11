# 原基部分 compound 与混合 Gram jets：真实全尺度解析费用

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority为main §§161–165与audit f72fe28cbb874cedbb3e1e20b840d86f2ebd9e37ff7da1632364b9e04cb6729c；556冻结记录仅读。唯一NEW主稿，数学producer新建/执行/import/rerun0，旧成功及同行执行0，辅助素数扩表0，Lean0。原B6/κ3/s5、degree<3n、rank2n饱和格及原整数basis保留。本稿不用q剪切估部分compound；mixed全阶对象的合法剪切另明确说明。

## 1. 准确对象与本轮新结论

实际全文读冻结 partial P1–P14、coupled C1–C23、lattice I1–I25、local Gram G1–G15、energy E1–E26及primitive-gcd G1–G13。组合输出截断后，local Gram与energy/gcd单独完整补读，不将截断算全文。当前总稿实际读§§161–165；audit完整JSONparse及header/current_progress/计数读取，不称全部556记录逐条人工全文读。

原basis记为
\[
g=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\quad
f_i(z)=\binom{z-1}{i},\quad G_m=(b_mL_m+b_{m'}L_{m'})/\beta_m,
\]
\[
b_j=\binom{6n+j}{j-1},\quad m'=2n+1-m,\quad
\beta_m=\gcd(b_m,b_{m'}),\quad\Gamma_n=\prod_m\beta_m.
\tag{A1}
\]
在原真实源 ξ=αζ(4)+βζ(5)、β≠0 的轮廓表示中，
\[
B_{ij}(\xi)=\int g_i(z)g_j(z)d\mu(z),\qquad
P_{ij}=\int g_i(z)\overline{g_j(z)}d\nu(z),\quad d\nu=|d\mu|.
\tag{A2}
\]
P严格正定。冻结partial P9–P10准确给
\[
\max_{I,J}|\det B_{I,J}(\xi)|\le\|C_d(B)\|_F\le e_d(P).
\tag{A3}
\]
**主定理。** 对所有 n≤d≤2n，有只依赖固定源的C使
\[
\boxed{\log e_d(P)\le
-\left(\frac{17d}{2n}-\frac{29}{3}\right)n^2-2\log\Gamma_n
+C n\log(n+2).}
\tag{A4}
\]
特别n=4r、d=6r=3n/2时，
\[
\boxed{\log e_{6r}(P)\le-\frac{37}{12}n^2-2\log\Gamma_n+O(n\log(n+2)),}
\]
\[
\boxed{\limsup n^{-2}\log\max_{I,J}|\det B_{I,J}(\xi)|
\le-\frac{37}{12}-2\gamma<-5.99,}
\quad \gamma=\lim n^{-2}\log\Gamma_n\ge1.455845.
\tag{A5}
\]
这是原basis的全部partial minors全尺度界；不借完整det衰减率、不免费省被删pair的gcd或high factorial。下半稿另给真实mixed Gram全部系数及weighted-det的付费界，仍未跨费用门槛。

## 2. 共用W、低系数与两项纸面常数

令S(z)=∏₁²ⁿ(z−j)、c_n=2n+1/2。提取common S之后，positive measure为W_n(x)dx。冻结energy给
\[
W_n(ny)\le C n^{4n+C}(1+|y|)^C e^{nQ(y)},\quad
\log L_n\le4n\log n+nM_0+O(\log(n+2)),\ L_n=\sup W_n,
\]
\[
Q(0)=12\log3-28\log2-4,\quad M_0=\sup Q,\quad M_1=\sup[Q+\log(1+y^2)].
\tag{A6}
\]
Q偶且Q(y)=−2π|y|−2log|y|+O(1)。冻结E23–E25的两个maximizers都在(0,1)，故
\[
M_0\le Q(0)+5\pi^2/102,\qquad M_1\le M_0+\log2.
\tag{A7}
\]
κtilde=β_mκ_j的准确(j−1)!² formula给，uniform于1≤j≤2n，
\[
\log|\widetilde\kappa_j|
=-(2n-1)\log n+n h(j/n)+O(\log(n+2)),
\]
\[
h(t)=(6+t)\log(6+t)-2t\log t-(2-t)\log(2-t)-6\log6+2.
\tag{A8}
\]
0log0=0；j=1或2n用0!=1，端点整数平移只损失O(logn)，无需j/n离端点正距。

所需安全常数为
\[
\boxed{M_0+2\max_{[0,2]}h<3/2,\qquad M_0+4-4\log2<-17/2.}
\tag{A9}
\]
对0<t<2，h''=1/(6+t)−2/t−1/(2−t)<−8/3：Cauchy给2/t+1/(2−t)≥(√2+1)²/2>17/6，1/(6+t)≤1/6。在t₀=3/2，h'=log(5/3)，强凹性给2maxh≤2h(3/2)+(3/8)log²(5/3)。因此
\[
M_0+2\max h\le15\log(5/4)+9\log(3/2)-9\log2
+5\pi^2/102+\frac38\log^2(5/3).
\tag{A10}
\]
log series的geometric upper给log(5/4)<9/40、log(3/2)<5/12、log(5/3)<8/15；冻结E25给log2>693/1000、π<22/7。upper小于3/2的有理余量为
\[
\frac32-\left[\frac{27}{8}+\frac{15}{4}-\frac{6237}{1000}
+\frac8{75}+\frac{1210}{2499}\right]=\frac{13207}{624750}>0.
\]
第二项由−M₀−4+4log2≥32log2−12log3−5π²/102，沿冻结log3<1099/1000，其大于17/2的余量至少1189/312375>0。均为纸证，不执行旧证书或任何数值程序。

## 3. 所有high列的原factorial费用

准确high列为S(z)h_k(z)/(2n+k)!，h_k=∏_{v=1}^k(z−2n−v)，0≤k<n。在z=c_n+iny，|h_k(z)|²≤n^(2k)(1+y²)^k。置t=k/n，A6与Stirling给
\[
\log P_{n+1+k,n+1+k}\le
n\{(1-t)M_0+tM_1-2(2+t)\log(2+t)+4+2t\}
+O(\log(n+2)).
\tag{A11}
\]
W的4nlogn、h_k的2klogn与(2n+k)!²的−(4n+2k)logn准确相消。积分尾对全部t∈[0,1]用Q+tlog(1+y²)的共同线性指数下降；dx=n dy和polynomial prefactor只付O(logn)，uniform于k。

A7放宽后的括号为M₀+tlog2−2(2+t)log(2+t)+4+2t，t导数≤−log2，最大在0。A9得到
\[
\boxed{P_{n+1+k,n+1+k}\le\exp[-(17/2)n+O(\log(n+2))].}
\tag{A12}
\]
任意h个high列的principal determinant由Hadamard不超过exp[−(17/2)hn+O(hlogn)]。未把gap-high子集当连续degrees的Vandermonde。

## 4. 部分low的Hardy系数与删除gcd的支付

取ℓ个pair的subset J，Γ_J=∏_{m∈J}β_m。原G_m/S是两真实Cauchy列之和。对这2^ℓ个选择作同一L² triangle，Loewner W≤L_n给
\[
\det P_{J,J}\le\frac{L_n^\ell}{\Gamma_J^2}
\left(\sum_{a_m\in\{m,m'\},\,m\in J}
\prod_{m\in J}|\widetilde\kappa_{a_m}|\sqrt{\mathcal H_\ell(a)}\right)^2,
\]
\[
\mathcal H_\ell=(2\pi)^\ell\prod_i(2\delta_i)^{-1}
\prod_{i<j}\left(\frac{\delta_j-\delta_i}{\delta_j+\delta_i}\right)^2,\quad
\delta_i=c_n-a_i.
\tag{A13}
\]
排序后δ_i≥i−1/2、δ_j<2n，全部a_i不同。log((1−u)/(1+u))≤−2u给
\[
\log\mathcal H_\ell\le\ell\log(2\pi)
+2\sum_{i=1}^\ell(\ell-i)\log\frac{2n-i+1/2}{2n+i-1/2}
\]
\[
\le\ell\log(2\pi)-\frac{\ell(\ell-1)(2\ell-1)}{6n}
=-\frac{\ell^3}{3n}+O(n),\quad0\le\ell\le n.
\tag{A14}
\]
离散sum Σ(ℓ−i)(i−1/2)=ℓ(ℓ−1)(2ℓ−1)/12。A6/A8使4nℓlogn相消；选择数只付O(n)，A9于是给
\[
\boxed{\log\det P_{J,J}\le\frac32\ell n-\frac{\ell^3}{3n}
-2\log\Gamma_J+O(n\log(n+2)).}
\tag{A15}
\]
ℓ=0时det=1，统一常数覆盖；ℓ=1给low diagonal界。

β_m≤b_m≤binom(7n,n)≤7^(7n)/6^(6n)。log7<2（e²前五项等于7，余项正）、6log(7/6)<1，故
\[
\boxed{\beta_m<e^{3n},\qquad
-2\log\Gamma_J\le-2\log\Gamma_n+6n(n-\ell).}
\tag{A16}
\]
这支付被删pair的真实损失，不按质量比例分摊Γ。

## 5. 全部partial minors的统一衰减

d-subset I含ℓ个low、h=d−ℓ个high。positive block Hadamard–Fischer给detP_I≤detP_low detP_high，A12/A15/A16合并为
\[
\log\det P_{I,I}\le4\ell n-\frac{17}{2}dn+6n^2-\frac{\ell^3}{3n}
-2\log\Gamma_n+O(n\log(n+2)).
\tag{A17}
\]
当n≤d≤2n，d−n≤ℓ≤n；4ℓn−ℓ³/(3n)在[0,n]严格增加，最大在ℓ=n，得A4。binom(2n,d)个principal minors的sum只再付O(n)。

γ是冻结primitive-gcd全尺度极限，本轮静态全文读其证明和保存外包。37/12+2·1.455845>599/100的差为1507/300000>0，故A3准确传回A5。冻结partial P7的fixed-source无限非零可同时使用，但当前全有限处safe upper45还未被这个已证rate跨过；更低独立费用必须另审后比较。这不构成最优费用lower或实际衰减upper。

## 6. 真实X斜率和mixed coefficientwise上界

由原local Gram G3取X系数
\[
\mathsf C_n=24\sum_{j=0}^{6n}W_jv_jv_j^{\mathsf T},\quad
v_j=(g_i(-j))_i,\quad
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3>0.
\tag{A18}
\]
C严格正定：g实系数且独立、degree<3n，6n+1个distinct real nodes的正加权平方和无非零kernel。置
\[
H_k=[t^k]\det(P+t\mathsf C)\ge0,\quad
J_k(\xi)=[t^k]\det(B_n(\xi)+t\mathsf C).
\]
mixed Andreief的k个points用positive24ΣW_jδ_(-j)，2n−k个points用原complex measure。每项取绝对值由同一positive measure的determinant平方夹住，故
\[
\boxed{|J_k(\xi)|\le H_k.}
\tag{A19}
\]
H_k≥0也来自positive generalized eigenvalues。任意实det1 q剪切使P、C同时Tᵀ-congruence，所以整个det(P+tC)及全部J_k不变；它是全阶pencil而非partial compound免费剪切。

mixed-minor展开与positive minor Cauchy–Schwarz给
\[
\boxed{H_k\le
\left(\sum_{|I|=k}\sqrt{\det P_{I^c,I^c}\det\mathsf C_{I,I}}\right)^2
\le e_{2n-k}(P)e_k(\mathsf C).}
\tag{A20}
\]
证明：系数为Σ_{I,J}(-1)^(ΣI+ΣJ)detP_(I^c,J^c)detC_(I,J)，两个minor分别夹在相应principal minors的几何平均之间；第二式再用sum层Cauchy–Schwarz。第一式保留互补low pairs。不能从t≥0的pointwise Hadamard免费推出coefficientwise inequality；这里另给准确证明。

## 7. 负整数node与source斜率的真实费用

j≤6n使
\[
W_j\le2^{12n}2^{3(2n+j)}\le2^{36n},\qquad
|f_i(-j)|=\binom{j+i}{i}\le2^{9n}\ (i<3n).
\tag{A21}
\]
Cardinal式给
\[
|L_a(-j)|=\binom{j+2n}{2n}\frac{a\binom{2n}{a}}{j+a}\le2^{10n}.
\]
b_a≤2^(8n)，故|β_mG_m(-j)|≤2^(18n+1)。因此
\[
\boxed{\mathsf C_{n+1+k,n+1+k}\le24(6n+1)2^{54n},\quad
\mathsf C_{m,m}\le96(6n+1)2^{72n}/\beta_m^2.}
\tag{A22}
\]
C principal minors按Hadamard付相应columns费用。这些source斜率的archimedean项不能继承ξ处cot指数衰减，不是免费的低阶derivative。

## 8. 保留一次Γ的全部mixed jet界

A20某k-subset I含a个C-low、b个C-high，a+b=k。P互补含ℓ=n−a个low和n−b个high。C-low gcd与P-low gcd准确相乘为Γ_n，故无需A16删除费用。A12/A15/A22和positive block Fischer给
\[
\log[\det P_{I^c,I^c}\det\mathsf C_{I,I}]
\le-7n^2-2\log\Gamma_n+\Delta_Lan+\Delta_Hbn
-\frac{(n-a)^3}{3n}+O(n\log(n+2)),
\]
\[
\Delta_L=72\log2-\frac32,\qquad \Delta_H=54\log2+\frac{17}{2}.
\tag{A23}
\]
A20的sqrt/sum/平方只付O(n)计数。Δ_L−Δ_H=18log2−10>0。对k≤n，a+b=k下A23对a的导数n(Δ_L−Δ_H)+(n−a)²/n>0，最坏a=k,b=0。因此
\[
\boxed{\log H_k\le-7n^2-2\log\Gamma_n+
(72\log2-\tfrac32)nk-\frac{(n-k)^3}{3n}
+O(n\log(n+2)),\quad0\le k\le n.}
\tag{A24}
\]
k>n最坏a=n,b=k−n，给对应线性延续。k=0的安全率比冻结q-optimized full rate弱，不冒称改善12.623；新收益是全部mixed阶数有同一真实ledger。

对固定τ∈R，t=e^(−τn)，sum全部H_k给
\[
\log\det(P+e^{-\tau n}\mathsf C)
\le-7n^2-2\log\Gamma_n+n^2F(\tau)+O(n\log(n+2)),
\]
\[
\boxed{F(\tau)=\max_{0\le u,v\le1}
\{(\Delta_L-\tau)u+(\Delta_H-\tau)v-(1-u)^3/3\}.}
\tag{A25}
\]
u,v是C-low/high比例，所有coefficients的sum只付O(n)。该max准确分离为(Δ_H−τ)_++max₀≤ᵤ≤₁[(Δ_L−τ)u−(1−u)³/3]，可按derivative全域核查，无sampling。

τ≥Δ_L+1=72log2−1/2时，两个函数都在0最大，F=−1/3，故
\[
\log\det(P+e^{-\tau n}\mathsf C)\le-\frac{22}{3}n^2
-2\log\Gamma_n+O(n\log(n+2)).
\tag{A26}
\]
使用H_k≤t^(−k)det(P+tC)仍必须付τnk。A24是更细直接系数界，不把这个fee删掉。

## 9. fixed-source低阶jet及比较范围

若假设ξ=c∈Q，冻结partial P7给无限n=4r的原B(c) rank≥3n/2。B(c) real symmetric、C SPD，使C^(-1/2)B(c)C^(-1/2) real symmetric。故det(B(c)+tC)的零阶恰nullity≤n/2，这些尺度存在一个0≤k≤n/2的非零J_k(c)。k可随n变，A19/A24仍uniform。

若signed whole-X scale q_n使D_A(X)/q_n∈Z[X]，则固定c=A/M时M^(2n)J_k(c)/q_n整数，继承同一scale只多O(n)固定分母费。whole-X real det1剪切作用整个pencil和jets；partial inverse-shear费依然不能删。当前full safe upper40.3145及其完整整模型由独立原算术来源负责，本稿不把partial45或尚未审阅的更低费用移给jets。

A24的worst k=n/2只给
\[
\limsup n^{-2}\log\max_{k\le n/2}H_k
\le36\log2-\frac{187}{24}-2\gamma.
\tag{A27}
\]
它没有给负衰减保证，所以这个明确positive mixed bound尚不足以配whole-X费用得到矛盾。A26也不能免费省τnk后宣称strict margin。A27不证明jets实际增长或方法no-go；negative-node粗binomial界、真正phase/cancellation或更精细Gram projection仍可能改善。

本轮改变解析接口为：原全部6r子式已有全尺度5.99保证衰减；真实mixed Gram coefficients有互补Γ计费及显式weighted-max界。既存full-det lower>12.62342839512558是不同对象，不继承给partial或positive jets。没有新ζ/L/Catalan无理性、LI或Lean结论。

## 10. 来源与闭合状态

新增PDF/HTML下载0，本轮原始PDF实际读页0。所有新不等式自证；原basis、Gram表示、Q/κ uniform Stirling与actual Γ率来自本轮实际全文读的六份冻结输入，不继承历史producer执行或primary页域。

本稿完整候选，待实际全文独审、收审后作者最终全文回读及一向FINAL来源收据。556旧冻结只读，不预先写审阅通过或strict margin完成。
