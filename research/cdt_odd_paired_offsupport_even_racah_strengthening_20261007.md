# 偶数支集外 Racah 门槛：排除半秩等号

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。本轮548既存冻结记录只读，权威进展为总稿 §§156–160 和 `cdt_odd_delivery_shallow_joint_20261007.json`，SHA `222765c5ecbbba1ba9bf28e19bfe68b14811bd8fe9bc999623476ecbb94ff573`。实际已读这些进展段落，完整 JSONparse 审计并读取头部；不宣称逐条人工全文读全部548记录。实际 FULL 回读 [offsupport O1–O25](cdt_odd_paired_offsupport_racah_gate_20261007.md)、[第四族 M1–M24](cdt_odd_paired_masked_high_compression_20261007.md)和 [invisible I1–I14](cdt_odd_paired_invisible_subform_arithmetic_20261007.md)。本稿纯纸证，数学 producer execute/import/rerun0，新增辅助素数数据或单位扩表0，原对象、degree、middle、halfjet 和已付费用保留。

新的全尺度结论：实际 even r≥4 时，旧 rank≥r/2 提高为 rank≥r/2+1。证明关键是严格处理旧 proper 论证的边界 2q=R，而非把旧 2q<R 假设无偿移到中间秩。

## 1. 实际门槛与精确加强范围

仍取 p=18r+1 素数，F=Fp，
\[
S(u)=\prod_{j=5r+1}^{9r}(u-j^2),\quad
m(u)=\prod_{i=0}^{r-1}(u-i^2),\quad
D(f)=\tfrac12\sum_{k=-5r}^{5r}S(k^2)^3f(k^2),
\]
\[
\mathcal L(f)=D(mf),\qquad \Phi(f)=D(m^2f)=\mathcal L(mf).
\tag{E1}
\]
冻结第四族正常性给全部 n≤4r 的 monic p_n、leading coefficient κ_n 和 norm ω_n 单位：
\[
p_n(u)=\kappa_n^{-1}
{}_4F_3\left(\begin{matrix}-n,n-14r-1,-x,x+2r\\-4r,-4r,-4r\end{matrix};1\right),
\qquad u=r^2+x(x+2r).
\tag{E2}
\]
同一个实际 off-support matrix 为
\[
\mathcal E=[p_{2r+j}(i^2)]_{i,j=0}^{r-1}.
\tag{E3}
\]

**Theorem E4。** 每个实际辅助素数，若 r为偶数且 r≥4，则
\[
\boxed{\operatorname{rank}\mathcal E\ge r/2+1,\qquad
\operatorname{corank}\Phi^{[2r]}\le r/2-1.}
\tag{E4}
\]
连同旧 O4，r≥3 统一得到 rank E≥floor(r/2)+1、corank Phi^[2r]≤ceil(r/2)−1。r=2保留旧 rank≥1；本稿既不补该单个素数的单位实验，也不把 r=2纳入 E4。r=1亦未加强。没有推出满秩或真实 D_high 同样的界。

## 2. 一般偶数窗口的极小秩必要机制

取任意域 K，monic recurrence
\[
f_{j+1}=(z-a_j)f_j-b_jf_{j-1},\qquad f_0=1,\ f_{-1}=0,
\tag{E5}
\]
所用 b_j均非零。取 n≥1、R=2s≥4、R个不同节点 z_i。原 recurrence 和已知非零系数覆盖本有限 associated construction 至下一项 f_(n+R)。设
\[
E=[f_{n+j}(z_i)]_{i,j=0}^{R-1}.
\tag{E6}
\]
旧一般定理 O7 给 rank E≥s。

**Lemma E7（半秩等号的必要替代）。** 若 rank E=s，则至少一个替代成立：

1. 存在 c∈K，全部 R节点均为 f_(n+s)+c f_(n+s−1) 的零点；
2. 至少 R−1个节点为 f_(n+s−1) 的零点。

这里只宣称由 rank=s 推出的必要替代，不把第二个替代单独宣称为充分条件。下面覆盖 gcd 的全部分支；不要求节点有实数次序或正权重。

### 2.1. Associated 资料与 coefficient relations

复述已证 O9–O12 的有限资料。A0=1、A1=z−a_n，B0=0、B1=1，两序列对 j≥1满足相同 associated recurrence
\[
A_{j+1}=(z-a_{n+j})A_j-b_{n+j}A_{j-1},
\quad B_{j+1}=(z-a_{n+j})B_j-b_{n+j}B_{j-1},
\]
\[
f_{n+j}=f_nA_j-b_nf_{n-1}B_j.
\tag{E8}
\]
A_j monic degree j；B_j 在 j≥1时也 monic degree j−1。有限 Jacobi 商 K[z]/(A_R) 的 diagonal pairing γ_j=product_(h=1)^j b_(n+h)给 functional μ；全部 leading profiles 至 R阶非退化。其 formal Laurent series C_μ 满足
\[
B_j=\operatorname{Pol}(A_jC_\mu),\quad
A_jC_\mu-B_j=\gamma_jz^{-j-1}+O(z^{-j-2}),\qquad j<R.
\tag{E9}
\]
Pol为 polynomial part。有限 normality 的构造只用上述非零 b，不假设无限 functional 正常。

令 q=rank E=s。前 q+1列的一个非零关系最高指标 l≤q，得到 A=Σc_j A_j、B=Σc_j B_j。deg A=l；若 l≥1，B也准确 degree l−1，leading coefficient c_l≠0。取 g=gcd(A,B)，e=deg g，t=l−e，A_*=A/g、B_*=B/g。删去 g为0的节点，剩余 M≥R−e。

相邻 f_n/f_(n−1) coprime，且 starred pair coprime，故剩余 rows 经非零 scaling 后为
\[
\Delta_j(z_i),\qquad
\Delta_j=A_jB_*-B_jA_*.
\tag{E10}
\]
这没有除一个可能为0的单独 evaluation。

### 2.2. 边界 2q=R 仍迫 strictly proper

对 j≤q+1，
\[
\deg\Delta_j\le q+t\le2q-e=R-e\le M.
\]
在 M个不同节点上，degree≤M 的 polynomial evaluation kernel 至多1维；这是 factor theorem，而非 degree<M 的单射。因 q+2≤R（s≥2），这些 q+2个 Δ 均属于原 block，evaluated rank≤q，故其 polynomial span dimension≤q+1。于是仍至少有一个非零 polynomial 恒等 coefficient relation。

置 R_*=A_*C_μ−B_*。任一恒等关系给 (A',B')=(hA_*,hB_*)，因为 starred pair coprime；E9 给 B'=Pol(A'C_μ)，所以 Pol(hR_*)=0。非零 coefficient relation 对应 h≠0，因为 A_j 形成 monic basis。若 R_*有非零 polynomial part，任一非零 h乘它的最高 nonnegative Laurent power 不可能消失。这与该关系矛盾。因此 R_*严格 proper。

有限 (t+1)阶 normality 又给
\[
R_*=c_*z^{-v-1}+O(z^{-v-2}),\qquad
c_*\ne0,\quad0\le v\le t.
\tag{E11}
\]
R_*=0或v>t均使非零 A_*与所有 degree≤t 测试正交，违背该 profile。证明只在 q=s、2q=R 的边界使用；没有据此声称更一般中间秩也 proper。

全部 R列的 polynomial 恒等关系，准确对应
\[
\deg h\le R-1-t,\qquad\operatorname{Pol}(hR_*)=0
\quad\Longleftrightarrow\quad\deg h\le v.
\tag{E12}
\]
反向也成立：将 hA_*在 A0,…,A_(R−1)中展开，E9和 proper 条件保证对应 B'=hB_*。因此 polynomial Δ-map 的 kernel dimension准确 min(v,R−1−t)+1。

### 2.3. 精确计数先约束 gcd

对 j≥t，E9给 Δ_j=−Pol(A_jR_*)；j≥t+1时其 degree准确 j−v−1。取 t+1≤j≤min(R−1,R−e+v)，各 degree不同且<M，得到与旧 O19 同一准确计数：
\[
q\ge R-t-1-\max(0,e-v-1).
\tag{E13}
\]
这里新补齐的是 proper 在等号边界确实已证，后续计数未改变。

若 e=0，E13给 l=t≥s−1，因此 t=s−1或s。若 e≥1，则 max(0,e−v−1)≤e−1，给 q≥R−l，迫 l=s。若 e≥2而v≥1，更强 max≤e−2会给 q≥R−l+1≥s+1，矛盾。因此
\[
e\ge2\quad\Longrightarrow\quad l=s,\ v=0.
\tag{E14}
\]

## 3. 三个 gcd 分支与必要替代的完成

### 3.1. e=0：中央相邻两阶的一个组合

没有删节点。j<t时 degree Δ_j≤j+t−1≤2t−2≤R−2；j≥t时 proper 给 degree≤j−v−1≤R−2。故全部 Δ的求值在 R节点上单射，polynomial Δ-map 的 nullity为 R−q=s。由 E12，
\[
\min(v,R-1-t)+1=s.
\tag{E15}
\]
若 t=s−1，得到 v=t。有限 normality 的唯一性迫 A_*为 A_(s−1)的常数倍，B_*为 B_(s−1)的同一倍。E8节点关系即 f_(n+s−1)(z_i)=0，符合 E7第二替代。

若 t=s，得到 v≥s−1。A_*degree s且其 Laurent tail首非零至少 z^(−s)，说明 μ(z^k A_*)=0对 k=0,…,s−2。因此在 normal A-basis 中准确
\[
(A_*,B_*)=c_0\bigl(A_s+cA_{s-1},\ B_s+cB_{s-1}\bigr),
\quad c_0\ne0.
\tag{E16}
\]
B部分由 E9的 linearity确定。v=s时c=0；v=s−1时c非零。E8遂给全部节点上的 f_(n+s)+c f_(n+s−1)=0，即第一替代。

### 3.2. e=1：一个中央多项式只许漏至多一节点

E14之前的计数已给 l=s、t=s−1，删至多1节点，M≥R−1。同样所有 Δ degree≤R−2<M，故剩余 evaluations 对其 polynomial span 单射。其 rank≤q=s，E12给 R−(v+1)≤s，因 v≤t=s−1而准确 v=t。有限 normality 迫 starred pair为 (A_(s−1),B_(s−1))同一常数倍。因此至少 R−1个原节点为 f_(n+s−1)零点，给第二替代。

### 3.3. e≥2：利用整个 polynomial block 排除

E14给 v=0、t=s−e≤s−2。j<t时 degree Δ_j≤2t−2≤R−2；j≥t时 degree≤j−1≤R−2。所以 polynomial Δ-image 在 degree≤R−2内。E12给其 kernel准确1维，image dimension为 R−1。

在剩余 M≥R−e节点上，这个 polynomial space 的 evaluation kernel维数至多 max(0,R−1−M)≤e−1。因此 evaluated rank至少
\[
(R-1)-(e-1)=R-e.
\tag{E17}
\]
原 rank=q=s，迫 e≥s。但 e≤l=s，遂 e=s、t=0。这不可能：l=s≥2使 B准确 degree s−1，非零；g degree e=s不可能整除该 B。故 e≥2分支不存在。

E15–E17覆盖所有 gcd情形，完成 Lemma E7。R=4、s=2时 q+2=R，边界论证完全合法，e≥2分支仍按同一 degree矛盾排除。R=2不具 q+2≤R，本稿没有套用该 lemma。

## 4. 实际正规差分传播排除两种替代

在实际族取 n=2r、R=r=2s≥4。所有关联 polynomials 至3r以及 norms、recurrence coefficients都在已证 degree≤4r正常窗口内。KS Eq1.2.5 的实际算子记为 T：对 y(k)=p_N(k²)，
\[
(Ty)(k)=B(k)(y(k+1)-y(k))
\mathbin{+}D_0(k)(y(k-1)-y(k))
=\lambda_Ny(k),\quad \lambda_N=N(N-14r-1),
\]
\[
B(k)=\frac{(k-5r)^3(k+r)}{2k(2k+1)},\qquad
D_0(k)=\frac{(k-r)(k+5r)^3}{2k(2k-1)}.
\tag{E18}
\]
每个1≤k≤r−1都是正规位置，B(k)单位：其全部分子因子非零，分母2k、2k+1均非零；因子绝对值/正指标均小于 p。D0的分母2k、2k−1也单位。

**传播事实 E19。** 若一个实际 eigenpoly在相邻 omitted indices a、a+1处为0，0≤a<a+1≤r−1，则在正规 k=a+1处由 E18迫下一点为0。如此向右传播至k=r，矛盾于
\[
p_N(r^2)=\kappa_N^{-1}\ne0.
\tag{E19}
\]
初始 pair可以是0、1：首次应用在k=1而非k=0。也可以是r−2、r−1：仅一步便抵达规范点。原点 rational combination和jet从未代入。

E7第二替代给 r−1个 omitted zeros。r≥4时从 r个连续 indices删至多一个，剩余必含相邻 pair：没有相邻 pair的 subset至多 ceil(r/2)<r−1。无论漏掉边界还是中间点，E19都排除该替代。

对第一替代，置 N=n+s=2r+s，
\[
h(k)=p_N(k^2)+c p_{N-1}(k^2),\qquad
h(k)=0\ (0\le k<r).
\tag{E20}
\]
c=0时由 E19直接排除。若 c≠0，在所有正规 interior k=1,…,r−2处，h的三个相邻值都为0，所以 Th(k)=0。利用两个 eigenvalue和 h(k)=0，准确得到
\[
0=c(\lambda_{N-1}-\lambda_N)p_{N-1}(k^2).
\tag{E21}
\]
这里
\[
\lambda_N-\lambda_{N-1}=2N-14r-2=-9r-2\in F^\times.
\tag{E22}
\]
因 r≥4且9r+2<p，差值确非零。于是 p_(N−1)在k=1,…,r−2全零；r≥4使此集合至少含1、2这一相邻 pair，再由 E19矛盾。N及N−1仍在第四正常窗口，未使用更高degree。

两种必要替代均不可能，因此 rank E不等于s。结合旧一般 rank≥s，得 rank E≥s+1，完成 E4第一条。此证明对线性组合使用真实两个 eigenvalue，不将单一 eigenfunction传播规则错误施加给任意 high kernel。

## 5. 完整 Phi 的新缺陷界与真实 K0 接口

冻结 O24 的双向同构仍为同一个实际对象：
\[
\operatorname{rad}\Phi^{[2r]}\simeq\ker\mathcal E,
\qquad W\longmapsto mW.
\tag{E23}
\]
不除未知 norm或未知 gate，故 even r≥4时缺陷≤r/2−1，完整 rank Phi^[2r]≥3r/2+1。连同旧 odd界，可准确记为
\[
r\ge3:\quad
\boxed{\operatorname{corank}\Phi^{[2r]}\le\lceil r/2\rceil-1,\qquad
\operatorname{rank}\Phi^{[2r]}\ge2r-\lceil r/2\rceil+1.}
\tag{E24}
\]

本轮权威 §157 的真实相容界 k+dPhi≤2r仍成立。它联系同一个完整 Phi radical与 source-invisible K0，但 E24是 dPhi的上界；不能把它代成 dPhi的下界来无偿改善 k的上界。也不能把完整 Phi的界传给另一个 r维 D_high压缩。新结果准确作用是进一步限制实际 Christoffel门槛可能的缺陷，未证明 K0=0、actual source pencil常规分支非退化或固定源无限成功。

## 6. 已证与未证的界线

本稿新收益是 even r≥4的额外一个秩方向、等号边界2q=R的合法 proper证明、完整 gcd分支的必要机制和原差分传播排除。未证明一般 q>s的中间秩核也 proper；剩余 kernel需要新的机制，不能重复使用本稿的半秩等号分类。odd维本稿没有比旧 ceil(r/2)再提高。

没有证明 off-support determinant或完整 Phi unit，D_high、restricted-H、原 fixed M5无限单位、actual深Smith方向、fixed rational source无限避开例外、whole-X无限非零和足够same-object解析–算术余量仍缺。没有新ζ/L/Catalan无理性、LI或Lean结果。费用未调整，本证明不提供n²算术收益或新的解析数值。

## 7. 原件、实际读取与闭合状态

复用 Koekoek–Swarttouw 作者报告 [primary URL](https://tudelft.roelofkoekoek.nl/documents/as98.pdf)、[本地冻结PDF](../literature/cdt_paired_pearson_rankone_sources_20261006/koekoek_swarttouw1998_askey_scheme_report98_17.pdf)，SHA `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`，737178bytes，170归档页。本轮作者实际完整文本读取 PDF28、29、30，共3 distinct页；定义、norm/monic recurrence与Eq1.2.5差分式均已读。没有将170归档页当作全文读完，没有新下载或TLS绕过。

E7–E17为有限代数自足纸证，使用冻结 O9–O12的已证 associated构造；E18实际回核KS原式。此次仅新增这份研究主稿，不建或运行数学 producer，不扩prime单位表。状态为完整NEW候选，待实际FULL独审、作者最终回读后另存一向FINAL来源收据；此前548记录保持只读。
