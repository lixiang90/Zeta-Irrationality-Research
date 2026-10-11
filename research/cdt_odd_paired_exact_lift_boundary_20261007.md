# 实际配对提升的精确 L 边界与二阶调和和公式

2026-10-07，NEW，/root/source_pencil_finalize。上一轮529冻结记录只读，包括前轮数学源、输出、guard和审计；不execute/import/rerun旧或同行数学程序，不扩辅助单位素数表。本文纯纸面推导，保留原B6/k3/s5、degree<3n、原饱和rank2n整数值配对格S及fixed rational source αζ4+βζ5。没有新的特殊值无理性/线性无关性结论。

## E1. 实际输入和记号

本轮实际完整读取[原auxiliary稿](cdt_odd_paired_head_free_auxiliary_prime_20261006.md)A1–A13、[完整整数格稿](cdt_odd_paired_head_free_integral_lattice_20261006.md)I1–I10、[源响应稿](cdt_odd_paired_source_radical_response_20261007.md)S1–S14及[第一residual精度稿](cdt_odd_paired_source_pencil_regular_20261007.md)P1–P7。以下补出后者保留的真正第二阶提升边界，不把halfjet代表直接当exact paired polynomial。

取n=4r、p=18r+1素数、F=F_p，故p≥19。设

\[
c=8r+1,\quad z'=c-z,\quad 1\le z\le4r,
\quad a_l=-l\ (0\le l<6r),
\]
\[
A(t)=\prod_{l=0}^{6r-1}(t+l),\quad
S(t)=\prod_{z=1}^{8r}(t-z),\quad
I(t)=\prod_{l=4r+1}^{6r-1}(t+l),\quad B(t)=(A/I)I'. \tag{E1}
\]

这里S是head节点多项式，与完整整数基矩阵S按上下文区分。T-space为reflection-even、degree<2r的多项式，维r；选其exact Z_p reflection-even lifts T_i。Q-space为reflection-even、degree<6r的多项式，维3r，同样用exact even lifts。negative annihilator是

\[
L_{i,l}=\frac{T_i(a_l)}{A'(a_l)S(a_l)}\in F,
\quad S(c-t)=S(t),\quad S'(z')=-S'(z). \tag{E2}
\]

A(z)、I(z)、S'(z)、A'(a)、S(a)均为p-units：所用不同节点及factorial差值的绝对值最多14r−1<p。ambient degree<12r<p使ordinary coefficient和原Newton整数值基的局部变换为GL(Z_p)。

## E2. 原 primitive constraints 的准确归一化

原head数d_z=(z)_(24r+1)恰含一层p。e_z=d_z/p是unit；原primitive gcd约除只将各pair行乘unit，kernel仍准确由e_z'P(z)−e_zP(z')=0决定。不是未经约除的raw行index。

置v_z=6r+z−1，则实际factorial乘积给**精确char0身份**

\[
e_z=(p-1)!A(z)E_z,\qquad
E_z=\prod_{u=1}^{v_z}(1+p/u)\in1+p\mathbf Z_p. \tag{E3}
\]

所有v_z≤14r−1<p，故没有未移去的p极点。定义归一化pair functional

\[
\mathscr F_z(P)=E_{z'}\frac{P(z)}{A(z)}-E_z\frac{P(z')}{A(z')}.
\tag{E4}
\]

真实paired约束恰为F_z(P)=0；归一化因子(p−1)!A(z)A(z')是已知unit。所有choice仅依赖原配对geometry，不依赖source α、β。

## E3. 任意阶提升的边界定理

**定理E5。** 设d≥1，参考多项式P_hat∈Z_p[t]_<12r满足F_z(P_hat)∈p^dZ_p。取任意actual exact paired lift

\[
P=P_{hat}+p^dR,\quad R\in\mathbf Z_p[t]_{<12r},
\quad\kappa_z(P_{hat},d)=\mathscr F_z(P_{hat})/p^d\bmod p. \tag{E5}
\]

则未知R的negative-node值虽然可不唯一，其r维L边界**完全确定**：

\[
\boxed{(L\,R(a))_i=\sum_{z=1}^{4r}\frac{T_i(z)}{S'(z)}\kappa_z(P_{hat},d)\quad\text{in }F.} \tag{E6}
\]

证明：F_z(P)=0除p^d后modp，利用E_z≡1，得

\[
R(z)/A(z)-R(z')/A(z')=-\kappa_z. \tag{E7}
\]

有限residue身份适用于T_iR/(AS)：numerator degree<14r−1、denominator degree14r，无infinity residue。因此在Z_p以及modp有

\[
L R(a)=-\sum_{z=1}^{8r}\frac{T_i(z)R(z)}{A(z)S'(z)}.
\]

T_i exact reflection-even且S'(z')=−S'(z)，逐pair合并并代入E7给E6。若两个exact corrections不同，其差modp属于原paired reduction，negative image在kerL；所以boundary不受choice影响。

**actual lift存在且可明确构造。** 令head cardinal

\[
\mathcal L_z(t)=S(t)/[(t-z)S'(z)]\in\mathbf Z_p[t],\quad\deg\mathcal L_z=8r-1.
\]

取

\[
R(t)=-\sum_{z=1}^{4r}
\frac{A(z)\mathscr F_z(P_{hat})}{p^dE_{z'}}\mathcal L_z(t). \tag{E8}
\]

它系数整、degree<8r<12r；left head值为−A(z)F_z(P_hat)/(p^dE_z')，right head值为0，故P_hat+p^dR逐pair满足原E-weighted约束，**在char0中准确成立**。E8不扩大原格：通过原primitive/saturated接口，此P属于原局部U_Z⊗Z_p。本文没有把参考P_hat自身当actual paired列。

## E4. elementary harmonic congruences

定义H_v=Σ_(u=1)^v1/u、H_v^(2)=Σ1/u²，H_0=H_0^(2)=0。先在F中证明H_(p−1)^(2)=0：乘2置换F^×，该sum等于自身的1/4倍，而p>3。再按k,p−k配对，half-square sum也为0；于是

\[
H_{p-1}=\sum_{k=1}^{(p-1)/2}\left(\frac1k+\frac1{p-k}\right)
\equiv-p\sum_{k=1}^{(p-1)/2}\frac1{k^2}\equiv0\pmod{p^2}. \tag{E9}
\]

因此对0≤u<p−1，直接移去末u项有

\[
H_{p-1-u}\equiv H_u+pH_u^{(2)}\pmod{p^2},
\quad H_{p-1-u}^{(2)}\equiv-H_u^{(2)}\pmod p. \tag{E10}
\]

这一步在这里完整证明，不将命名同余或generic p-adic theorem当免费输入。

## E5. weak 的实际第二阶 defect

对Q exact reflection-even，原halfjet参考是

\[
P_{hat,Q}=AQ+(p/2)BQ,\quad d=2. \tag{E11}
\]

置

\[
h_z=H_{v_z},\quad b_z=(H_{v_z}^2-H_{v_z}^{(2)})/2,
\quad j_z=I'(z)/I(z),\quad j_{2,z}=\sum_{l=4r+1}^{6r-1}(z+l)^{-2}.
\]

E_z≡1+ph_z+p²b_z (modp³)，而P_hat,Q(z)/A(z)=Q(z)(1+pj_z/2)。故

\[
\kappa_z(P_{hat,Q},2)
=Q(z)\left\{
\frac{h_{z'}-h_z+(j_z-j_{z'})/2}{p}
+b_{z'}-b_z+(h_{z'}j_z-h_zj_{z'})/2\right\}\bmod p. \tag{E12}
\]

分子被p整除，下面自证，不对尚未整除的表达式除p。令u=4r+z，则v_z=u+2r−1，v_z'=p−1−u，并有exact j_z=H_v−H_u、j2=H_v^(2)−H_u^(2)。整多项式I还满足关键char0身份

\[
I(c-t)=-I(t-p),\qquad j_{z'}=-I'(z-p)/I(z-p)
\equiv-j_z-pj_{2,z}\pmod{p^2}. \tag{E13}
\]

第一式来自index反射l↔10r−l和degI=2r−1为奇数；不能只用模p的odd性而漏掉p层。E10给h_z'≡H_u+pH_u^(2)，因此E12的三个部分分别为

\[
\frac{h_{z'}-h_z+(j_z-j_{z'})/2}{p}
\equiv H_u^{(2)}+j_{2,z}/2,
\]
\[
b_{z'}-b_z\equiv-h_zj_z+j_z^2/2+H_u^{(2)}+j_{2,z}/2,
\]
\[
(h_{z'}j_z-h_zj_{z'})/2\equiv h_zj_z-j_z^2/2\pmod p.
\]

不仅证明F_z(P_hat,Q)∈p²，而且彻底化去first-order harmonic和divided-p项，得到

\[
\boxed{\kappa_z(P_{hat,Q},2)
=Q(z)\{H_{4r+z}^{(2)}+H_{6r+z-1}^{(2)}\}\quad\text{in }F.} \tag{E14}
\]

故任意actual P_Q=P_hat,Q+p²R_Q满足

\[
\boxed{(L R_Q(a))_i=
\sum_{z=1}^{4r}\frac{T_i(z)Q(z)}{S'(z)}
\{H_{4r+z}^{(2)}+H_{6r+z-1}^{(2)}\}.} \tag{E15}
\]

这填补真正weak第二阶提升的L边界；没有声称全部6r个R_Q(a)分别唯一或已求出。

## E6. strong 边界及可实现的参考选择

对任意P0 whose reduction属于真实paired U/p，令f_z=P0(z)/A(z)。f_z−f_z'∈pZ_p，d=1，E3直接给

\[
\boxed{\kappa_z(P_0,1)=
(f_z-f_{z'})/p+h_{z'}f_z-h_zf_{z'}\bmod p.} \tag{E16}
\]

这里第一项是已知P0的literal carry，不是未知actual提升。仍由E6确定任何actual P=P0+pR的L R边界。

可以选择更简单的参考P0，使

\[
P_0(z)/A(z)=P_0(z')/A(z')\quad\text{exactly over }\mathbf Z_p. \tag{E17}
\]

这是**参考约束**，不代替原E-weighted actual约束。它的each pair系数是unit、head evaluation split surjective，且modp与原约束相同，故每个所需strong reduction均可这样lift。更明确：先取任意ordinary integral lift P_bar of该reduction，δ_z=P_bar(z)/A(z)−P_bar(z')/A(z')∈pZ_p，置

\[
P_0=P_{bar}-\sum_{z=1}^{4r}A(z)\delta_z\mathcal L_z.
\tag{E18}
\]

新增项的系数被p整除，保留negative reduction Z；degree仍<12r；head ratio差准确为0。然后使用E8、d1修正到原actual U。E17使E16的carry为0，且h_z'−h_z≡−j_z，得到

\[
\boxed{\kappa_z(P_0,1)=-j_z\frac{P_0(z)}{A(z)},\qquad
(L R(a))_i=-\sum_{z=1}^{4r}\frac{T_i(z)j_zP_0(z)}{S'(z)A(z)}.} \tag{E19}
\]

实际strong basis所需5r个negative Z列可全部采用此参考选择；weak3r列采用E11。完成actual correction之后，其modp列仍是原image加kernel的basis，故与原完整S局部变换det为unit。没有新增source、格index或算术费用。

## E7. 与第一 residual 的接口和剩余数学

strong列设ε=0、weak列ε=1，参考到actual修正统一为p^(ε+1)R。其normalized values增加p R(a) (modp²)，normalized derivatives增加p²R'(a−p)，所以在first residual精度不变。对leading K=kerA5的v，用冻结S12的y_v+6x_v=−D^-1L^tθ_v，value修正只通过L R(a)进入restricted form。E15/E19遂为整个r×8r lift-boundary matrix的明确head公式；不需要任选unknown R_Q或P1。

完整actual第一form仍必须包括reference N modp²的leading carry：先算T^tN_refT再除p，不能把模p的零form先删除。若在K0=kerθ上形式上取x0=−y0/6，则leading term仍含β y0^tD0 y0'，一般只modp为0，其除p的carry不能无证省去。本稿不单独给无carry的K0公式；root的新reference-jet completion将使用E6/E15/E19接回完整literal first residual。

本轮具体新结果是：任意阶actual lift的L-boundary唯一且显式；weak实际第二阶边界化为二阶harmonic head sum；strong参考可选取明确A-weighted gauge，使其boundary亦为显式first-harmonic sum。它们消除了前轮first-form接口中的自由提升边界，不证明actual残余pencil regular或这些明确矩阵为unit。

尚缺：实际leading kernel和完成后的first residual在无限辅助素数上的正常性；fixed rational source无限成功；whole determinant无限非零；同一对象解析–算术strict margin；新的ζ/L/Catalan无理性/线性无关性结论。单个p≈n的提升控制仍不直接给n²费用节省。

## E8. 证据与执行范围

数学producer执行0、失败0、rerun0，旧/同行execute/import0，辅助单位素数扩表0，Lean0。全文是从实际原primitive约束、有限residue身份及正文自证的harmonic congruences推导，不使用未经验证的generic arithmetic或文献定理。本轮新增primary下载0、PDF实读0；旧文献存档未重下载。

一次带Windows路径glob的定位rg失败；随后正确rg glob搜索结果截断，只用于定位整数格稿，不当全文阅读证据。之后上述四份指定MD均以Get-Content -Raw完整读回。此类定位输出不是数学producer失败或已执行旧程序。最终独立review、全稿自读与immutable来源receipt另存；当前candidate尚未冻结。
