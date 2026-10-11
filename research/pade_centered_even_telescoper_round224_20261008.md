# 第224轮：固定三周期包的六阶中心化telescoper

2026-10-08，A。保持222/223的实际R_n、A₃、A₅、A₇、C及外积，不搬相近文献族的四阶operator。本稿给一个**明确的有限principal-part／6×6行列式定义的有理telescoping证书**：三个实际偶A序列及完整C序列共享order6的可计算递推；其最小order只得到≤6。原Δ、Ξ及任意固定g∈Q的H_g系数共享一个明确20维外幂difference system，故共同P-recursive order≤20。没有把difference维数当成CDT所需最小微分rank。

矩阵非零性由一次预先限定的Fraction计算支付：只在n=6取centered shifts0,…,6，六维余数矩阵rank6、七个最大minor全非零。没有序列采样、递推guessing或阶数/参数扫描。首、末coefficient是非零Q(n)函数，**没有证明它们在全部大整数上不为零，也不据此证明Δ无限非零或数值无理性**。

## 1. 参数平移和真正的even centered shifts

**T1.** 固定

\[
R_n(t)=\frac{\prod_{j=1}^n[(t-j)(t+n+j)]^3}{\prod_{k=0}^n(t+k)^6},
\quad H_{n,k}(v)=(-1)^k v^6R_n(-k+v),\quad z=k-v.
\]

在支持内，H即223的(−1)^kF；其Gamma表达在所有整数k也成立。直接有限乘积或223 H3给k方向项比

\[
K_n(z)=\frac{H_{n,k+1}(v)}{H_{n,k}(v)}
=\frac{A_n(z)}{B_n(z)},\quad
A_n(z)=-(n+z+1)^3(n-z)^9,\quad
B_n(z)=(z+1)^9(2n-z)^3.
\tag{T2}
\]

v完全消失。不是在连续v方向假定Gamma holonomic。

对于j≥0，将n移2j同时将k移j，实际ratio恰为

\[
P_j(n,z)=\frac{H_{n+2j,k+j}(v)}{H_{n,k}(v)}
=(-1)^j\frac{[(n+z+1)_{3j}(2n-z+1)_{3j}]^3}
{[(z+1)_j(n-z+1)_j]^9}.
\tag{T3}
\]

P₀=1；P_j(n,n−z)=P_j(n,z)，且在z=∞为O(1)。这项k移位不是免费改有限求和端点；§5用真实双边周期完整支付它。

对Y∈Q(n,z)，定义

\[
\mathscr D_nY=A_n(z)Y(z+1)-B_n(z-1)Y(z),\quad Q=B_n(z-1)Y.
\tag{T4}
\]

于是(K_nQ(z+1)−Q(z))H_(n,k)=H_(n,k+1)Q(z+1)−H_(n,k)Q(z)。所有接下来的构造都在Q(n)(z)上，n是不定元；有限n特化仅用于证明一个minor函数非零。

## 2. 九重principal parts给完整六维余数空间

**T5：有限、无order搜索的算法。** 只取j=0,…,6。P_j的可能poles是z=−i、z=n+i，1≤i≤j，阶数≤9。对a=n+i，令PP_a为负次Laurent部分。令q_(j,j+1)=0，依次i=j,…,1定义

\[
q_{j,i}(z)=-\operatorname{PP}_{z=n+i}
\left\{\frac{P_j(n,z)}{B_n(z-1)}
-\frac{A_n(z)}{B_n(z-1)}q_{j,i+1}(z+1)\right\},
\quad Y_{j,+}=\sum_{i=1}^j q_{j,i}.
\tag{T5}
\]

每个q是Σ_(ℓ=1)^9 c_(j,i,ℓ)(n)/(z−n−i)^ℓ，完全明确：负次系数只需对(z−a)^9乘括号后的正则函数取0,…,8次normalized Taylor coefficient。若需写成导数，次数h的系数就是该正则函数的h次导数在a的值除h!。没有未知certificate ansatz或任意degree cutoff。

为什么只出现i+1项：先前q_(j,s)(z+1)只有s=i+1的pole在z=n+i，其余s>i+1在此正则；所有q_(j,s)(z)亦在此正则。因B_n(n+i−1)=(n+i)^9(n−i+1)^3是Q(n)中的unit，T5准确支付正pole的完整九阶部分。\(\mathscr D_nY_{j,+}\)的poles仅在n+1,…,n+j；最后可能在z=n的pole由A_n的九重零消去。因此P_j−𝒟Y_(j,+)已无正pole。

**T6：反射支付另一族，且实降到六维。** 置

\[
Y_j(z)=Y_{j,+}(z)+Y_{j,+}(n-z+1),\qquad
R_j(n,z)=P_j(n,z)-\mathscr D_nY_j(z).
\tag{T6}
\]

因为A_n(n−z)=−B_n(z−1)、B_n(n−z−1)=−A_n(z)，精确有
(𝒟Y)(n−z)=𝒟[Y(n−z+1)](z)。反射后的𝒟Y_(j,+)因此准确取消P_j的负poles−1,…,−j，不引入正pole。R_j无任何有限pole，故为多项式，并且R_j(n,n−z)=R_j(n,z)。

每个Y_(j,+)=O(z⁻¹)，两个反射项的z⁻¹首项相消，故Y_j=O(z⁻²)。A、B均degree12，因而R_j的degree≤10。置w=z−n/2，得到完全有理的固定六维basis

\[
R_j(n,n/2+w)=\sum_{a=0}^5 m_{a,j}(n)w^{2a},\qquad m_{a,j}\in\mathbb Q(n).
\tag{T7}
\]

这不是把generic projection当作免费rank下降：两个pole族均已消除，反射的certificate符号、∞首项与实际求和移位都另付。R₀=1。degree与对称性是纸面身份，不从有限插值点推断。

## 3. 有限非零minor支付一个明确的operator

**T8.** 令M(n)=(m_(a,j)(n))，行a=0,…,5、列j=0,…,6；令M̂_j删去第j列。定义

\[
\lambda_j(n)=(-1)^j\det\widehat M_j(n),\quad
L_n=\sum_{j=0}^6\lambda_j(n)E_n^{2j},\quad
\mathcal Q(n,z)=B_n(z-1)\sum_{j=0}^6\lambda_j(n)Y_j(n,z).
\tag{T8}
\]

这已是一条有限可核的symbolic定义：至多六组九阶principal parts、六维系数提取、七个6×6行列式；不需要将大系数全部展开。L_n按步长2的E_n²计order6，按通常E_n计order12；在r=n/2变量上是order6。cofactor恒等式Σλ_jR_j=0直接给

\[
\sum_{j=0}^6\lambda_j(n)P_j(n,z)
=K_n(z)\mathcal Q(n,z+1)-\mathcal Q(n,z).
\tag{T9}
\]

还必须支付λ非恒零。本次唯一数学执行固定n=6，由T5直接Fraction计算Laurent系数，再用**已纸证**的T7在六个w=q/13、q=0,…,5处准确重建degree≤5的w²多项式，另在未参与重建的w=7/13核恒等值。并核反射及cofactor kernel。结果M(6)rank6，七个signed maximal minors全部非零；其中

\[
\lambda_6(6)=
-\frac{89211651547364448048475293682221949275162682610460756007447365406937695243032669943582098909177053440342998708821071219361654960793949}
{779800861152894554968423761497409327436004560241907401597312440214710596403200000000000000}\ne0.
\tag{T10}
\]

全部矩阵、principal parts及七个exact fractions存于[唯一运行输出](pade_telescoper_residual_rank_certificate_round224_20261008.json)。所以M在Q(n)上rank6，λ₀和λ₆均是非零有理函数，T8给order6的非零operator。这里的rank6是**所构造余数矩阵**的rank；未证明这是所有rational certificates的商空间最小rank，更未证明实际A源的最小order等于6。

## 4. 参数整数异常与可明写的全局多项式版本

**T11.** T5在n≥6的每个整数均有意义。regular Taylor系数的n分母只来自n+i、n−i+1、n+i+1+r（r=0,…,j−1）及固定非零整数。置

\[
D_0(n)=\prod_{c=-5}^{12}(n+c).
\]

每个P_j/B在正pole处的normalized jet、以及A/B的0,…,8次jet均由D₀¹⁷清除n分母：原因是原分母单个线性因子的幂≤9，再求至多8次Taylor系数。T5至多六层乘法，故D₀¹⁰²清除Y的全部n分母。对z作polynomial part只需除首项±1的线性因子，不添n分母；置w后只添固定2幂。因此D₀¹⁰²m_(a,j)∈Q[n]，进而

\[
D_0(n)^{612}\lambda_j(n)\in\mathbb Q[n].
\tag{T11}
\]

这个粗612是operator的符号分母上界，不是源系数的LCM费用，不替代223的safe12/26或最优整模型。n≥6时D₀(n)无零。λ₀或λ₆仍可能在该区间有限多个整数上为零；T10只核定n=6，尚未计算它们的完整整数零点集合。

**T12.** 对三个偶序列f_r=A_(s,2r)，本稿递推先在r≥3成立。以下明确polynomial operator将所有有限初始异常一起支付：

\[
\widetilde L_r=
\sum_{j=0}^6 r(r-1)(r-2)D_0(2r)^{612}\lambda_j(2r)E_r^j.
\tag{T12}
\]

它在Q[r][E_r]中非零，order6，且对所有r≥0有效：r≥3使用§5的实际身份；r=0,1,2时所有系数为0。该有限prefix处理没有证明这些初值由递推决定，也不能用它从Δ₀向后排除零尾。T12的首末coefficient均非零多项式，但含显式prefix零点及尚未定位的minor整数零点。

## 5. 实际bilateral和完全支付certificate边界

**T13.** 定义真实period

\[
\mathcal B_n(v)=\sum_{k\in\mathbb Z}H_{n,k}(v).
\]

对固定n、|v|<1/2，支持外整数点不是R_n的poles，且两端R_n(−k+v)=O(|k|⁻⁶)一致。因此𝓑全纯，𝓑_n−S_n=O(v⁶)，S_n仍是原有限cutoff。所需0、2、4次jets准确保留。伴随[Root双边period稿](pade_bilateral_period_model_round224_20261008.md)P1–P3给同一接口；本稿在下文为自己的具体certificate支付其条件。未将C的双重finite tail替换为双边和。

**T14：∞边界。** 每个P_j=O(1)。T9的𝒬是rational function；若其∞ polynomial首项是cz^d、d>0，则K_n(z)→−1使右端首项恰为−2cz^d，不能等于左端的O(1)。所以最终**组合后**𝒬=O(1)。不能把individual certificates的O(z¹⁰)免费视作已满足边界；其高次项正是由ΣλR=0取消。

**T15：有限integer poles。** Y_j的poles只有z=n+i及z=1−i，1≤i≤6，阶≤9。𝒬中z=0的pole由B_n(z−1)的z⁹消去。其他pole分别对应foreign integers k=n+i，及k=1−i≤−1；n≥6时R_n在t=−n−i、t=i−1都有三阶零。故H_(n,k)(v)=O(v⁹)，准确取消𝒬在v=0的至多九阶pole。内部k=0,…,n的F本来正则，其他位置亦无未付pole。因而G_(n,k)=𝒬(n,k−v)H_(n,k)在v的小盘全纯，且两端一致为O(v⁶|k|⁻⁶)，特别趋零。

将T9乘H得到实际telescoping identity

\[
\sum_{j=0}^6\lambda_j(n)H_{n+2j,k+j}(v)
=G_{n,k+1}(v)-G_{n,k}(v).
\tag{T16}
\]

对全部整数k求和，两端为0，每个k↦k+j平移合法。因此Σλ_j(n)𝓑_(n+2j)(v)=0，n≥6。取低于6次Taylor系数，再用T13，得同一个operator同时湮灭原S_n的0、2、4次系数。223 H6的固定κ_s=(s−1)(1−2^(1−s))仅为非零有理乘子，所以**原A₃、A₅、A₇的实际偶序列全部满足T12**。没有用foreign Gamma项的裸Taylor或未付cutoff。

## 6. 实际半线I/C边界及二十维完整外幂系统

**T17：同一个operator也支付完整C。** Root在本稿draft期间提出用半线交错和恢复I的边界桥，作者另作如下完整纸核。将T16除去(−1)^kv⁶并置t=−k+v，作为rational identity得到

\[
\sum_{j=0}^6\lambda_j(n)(-1)^jR_{n+2j}(t-j)
=-Z_n(t-1)-Z_n(t),\quad Z_n(t)=\mathcal Q(n,-t)R_n(t).
\]

先对t微分，再对整数t=7,…,M乘(−1)^t求和，右侧准确望远镜为Z_n′(6)−(−1)^MZ_n′(M)。T15列出的最左pole是z=−5，因此𝒬(n,−t)在t=6处正则；n≥6时R_n(6)三阶零，故Z_n′(6)=0。∞处𝒬=O(1)、其t导数O(t⁻²)，R=O(t⁻⁶)、R′=O(t⁻⁷)，故Z_n′(M)→0。

左侧对每个j置u=t−j，(−1)^t(−1)^j=(−1)^u，且j≤6确保u≥1。恢复完整I_(n+2j)时遗漏的正整数最多为1,…,6，全部为R_(n+2j)的三阶零，其一阶导数为0。所有求和绝对收敛。因此对偶n≥6实际有Σλ_j(n)I_(n+2j)=0。结合原exact period分解及T16已证三A共同递推，相减给Σλ_j(n)C_(n+2j)=0；不假定ζ(3)、ζ(5)、ζ(7)独立或任何目标有理性。完整finite tail没有删去，T12因此也湮灭第四个实际有理序列C_(2r)。

**T18.** 在Q(r)上令l_j(r)=λ_j(2r)。l₀、l₆都非零。设𝒞(r)为6×6 companion matrix：前五行是右移的单位向量，末行是(−l₀/l₆,…,−l₅/l₆)。对实际四个列序列a=A₃,₂ᵣ、b=A₅,₂ᵣ、c=A₇,₂ᵣ、q=C₂ᵣ，在足够大的非异常r处，六项state都满足v_(r+1)=𝒞(r)v_r。rational coefficients只可能有有限整数异常；未定位这些点，不能声称每个整数处都invertible。

令W_r=v_(a,r)∧v_(b,r)∧v_(c,r)。则

\[
W_{r+1}=(\wedge^3\mathcal C(r))W_r,\qquad
(\wedge^3\mathcal C)_{I,J}=\det\mathcal C_{I,J},\quad |I|=|J|=3.
\tag{T18}
\]

这是显式20×20 rational matrix system。其(0,1,2)分量恰是原连续三行Δ_r，没有换det对象或去掉某列。分别以第三个state换成v_q及g v_c+v_q，便得同一system的另两个solution，其相同分量分别是Ξ_r与gΔ_r+Ξ_r。对观测行e_(0,1,2)及其20个前移的20维线性依赖，得到**与solution无关**的共同scalar operator，order≤20；这不是把三个不同solution加成免费rank3。有限异常和有限prefix不破坏P-recursiveness，可乘相应有限prefix polynomial支付。这里没有展开该scalar operator、给它的最小order或最早coefficient整数零点；也不据此证明Δ无限非零。

本轮从“仅存在性”前进一步：固定A/C-block有明确非零cofactor定义的order6 telescoper，完整有限、双边与半线边界已付；Δ、Ξ、任意固定有理g的H_g系数有实际共同20维difference system。尚未由此获得实际CDT connection的微分rank、generic主奇点、目标relation的strict overconvergence或费用门槛。G-functions性质及同源分母沿用223已证版本；新operator归一化不改变实际源系数费用。Δ₀≠0与T10也不支付无界尺度的目标非退化。

## 7. 实际primary／运行与保存身份

先核official实现入口：[SymPy Concrete的Gosper条目](https://docs.sympy.org/latest/modules/concrete.html)、[RISC HolonomicFunctions](https://www1.risc.jku.at/sw/holonomicfunctions/)、[Zeilberger A=B packages](https://sites.math.rutgers.edu/~zeilberg/programsAB.html)。它们用于比较路线，本稿数学T1–T18由上述自含纸证，不调用其未执行的软件。没有安装或执行Maple/Mathematica/SymPy，也未搬异族四阶算式。新实际选读scope另存[实现来源记录](../literature/pade_operator_sources_round224_20261008/lambert_implementation_reading_scope.md)；223原论文选页不重复下载，未冒称本轮FULL原论文。

本任务数学程序准确**1次**，exit0：

- [producer](certify_pade_telescoper_residual_rank_round224_20261008.py)，9628B，SHA256 `b01275768fe9700cc7c3b21befa91bfd5ca1a97676d34f459112f3d3f8e2fd8f`。
- [完整exact输出](pade_telescoper_residual_rank_certificate_round224_20261008.json)，26796B，SHA256 `a47a933aca74e035b49233d1f7cbd7106d770f679f5840934cdbfcfc69e4bbd0`。

实际FULL读producer与全部输出。输入仅n=6、j=0,…,6；既有degree proof下的准确插值只是恢复系数，不是guessing recurrence。数学执行包含Fraction principal parts、一个6×7矩阵的rank/七minor、反射/kernel与一额外点检查；无序列计算、prime/order/grid扫描、numericalintegration、PSLQ或Lean。未运行222任何producer，未重跑本程序。文档/web/metadata操作另计，不冒充数学执行。

本轮实际FULL复读223 holonomic11517B／`54eb60ab2835832855cd268c5dfb4318f2c25019a4589cf713483460fa00866a`，并实际FULL读Root双边稿当时7816B／`7761ce036a9b31d6a6bdfd4e3cac6d0e4feba840e6b2dca23f4db7ff0d7996a4`全部P1–P11，本稿只采用P1–P3并为自己的certificate再付条件，不冒称已独审其三频率常数或全权重投影。若伴随稿后来变更需另登记身份。旧稿/main/manifest保持不动。本文与来源记录保存后需实际FULL作者复读，最终bytes/hash另报；作者自读不代替独审。
