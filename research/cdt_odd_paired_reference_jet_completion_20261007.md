# 原配对格的参考jets完成、source-invisible核与二次小门槛

2026-10-07，NEW，root。此前529冻结记录和delivery75205快照只读。本文不执行/import/rerun任何数学producer，不扩辅助单位素数表。原B6/κ3/s5、degree<3n、饱和S、fixed source ξ=αζ4+βζ5（β≠0）和whole-X D_A不变。参考多项式只用来计算原模型的局部剩余项，不重选全局整数格。本文纯纸证；正式独审及来源收据后存。

## J1. 已证实际输入和可选参考多项式

令n=4r、p=18r+1素数、F=Fp，避开fixed source分母和β素因子。沿用[source稿](cdt_odd_paired_source_radical_response_20261007.md)S1–S14与[pencil稿](cdt_odd_paired_source_pencil_regular_20261007.md)P1–P18：在实际局部strong/weak基中

\[
p^5B_{\alpha,\beta,X}=D_pN_{\alpha,\beta}(X)D_p,
\quad D_p=\operatorname{diag}(1^{5r},p^{3r}),
\quad\overline N=6\bar\beta\mathcal A_5.
\tag{J1}
\]

物理negative nodes a_l=−l（0≤l<6r），A(t)=∏(t+l)，I为共同节点因子，B_node=(A/I)I'。选择strong参考多项式 P̂_z=P0,z、weak参考 P̂_Q=AQ+(p/2)B_node Q；actual exact lifts可写

\[
P_z=P̂_z+pR_z,\qquad P_Q=P̂_Q+p^2R_Q,
\tag{J2}
\]

均在Zp[t]_<12r中；p单位的Newton factorial允许普通系数与整数值坐标互换。J2只要求参考准确至指定层，不要求参考本身是char0 exact paired polynomial。存在这些exact actual lifts来自原primitive约束的已证满射；所有R仍受该约束，不是自由源。

用同一个literal harmonic form计算参考 N̂_0,β(0)，两侧同样除D_p。tail处weak参考值被p整除，普通derivatives整；head在normalized矩阵至少p²。因此N̂为整矩阵，且其modp与actual N相同。参考不满足exact pairing不影响这些局部整性，但不能据此把其det当原全局D_A。

令K=ker A5，dimK=k≤2r，T为K基的整lift。actual first residual为

\[
\overline R_\alpha=A_{\rm act}+8\bar\alpha G_K,
\quad A_{\rm act}=(T^tN_{0,\beta}(0)T/p)\bmod p.
\tag{J3}
\]

leading矩阵杀T，已知unit补空间的Schur交叉乘积除p后modp消失。定义

\[
A_{\rm ref}=(T^tN̂_{0,\beta}(0)T/p)\bmod p.
\tag{J4}
\]

分子也被p整除。必须保留完整modp²计算再除p：leading form只在modp为0，可能有真实进位。J4没有删除这个进位。

## J2. 未知值修正只经过同一个θ边界

对normalized局部jets，strong取x=P(a−p)、y=pP'(a−p)，weak取x=P(a−p)/p、y=P'(a−p)。J2给

\[
x_{\rm act}-x_{\rm ref}=p\Delta\pmod{p^2},
\quad y_{\rm act}-y_{\rm ref}=0\pmod{p^2},
\tag{J5}
\]

其中每列Δ是相应R(a_l)modp。strong的derivative差是p·pR'=p²R'；weak的差亦为p²R'。tail的literal coefficients为u≡−6β、v≡−36β−6pβc_l (modp²)，head不进入first residual。

在K上记leading jets为x,y，物理质量D=diag(W_(p+l)modp)。source S12给唯一线性映射Θ:K→F^r，使

\[
y+6x=-D^{-1}L^t\Theta,
\quad G_K=\tfrac16(\Theta^t\mathcal P+\mathcal P^t\Theta),
\quad\mathcal P(v)=F_*q_v.
\tag{J6}
\]

这里只用已证L,Z,J等；D^{-1}是已知单位，不除actual未知Gram。由真实tail形式−6β(xyᵀ+yxᵀ)−36βxxᵀ，值的一阶变化准确为

\[
\frac{N_{\rm act}-N̂}{p}
=-6\bar\beta\,[\Delta^tD(y+6x)+(y+6x)^tD\Delta]
\pmod p
\]

在K上的restricted form。v的p层c_l项乘值变化后成为p²，不遗漏；derivative变化J5及head也不贡献。置

\[
\mathcal B=L\Delta:K\to F^r.
\]

得到新的实际完成恒等式

\[
\boxed{A_{\rm act}=A_{\rm ref}
+6\bar\beta(\Theta^t\mathcal B+\mathcal B^t\Theta),}
\tag{J7}
\]
\[
\boxed{\overline R_\alpha=A_{\rm ref}
+\Theta^t\mathcal Z_\alpha+\mathcal Z_\alpha^t\Theta,
\quad\mathcal Z_\alpha=6\bar\beta\mathcal B
+\tfrac43\bar\alpha\mathcal P.}
\tag{J8}
\]

原ζ4的source响应与真正提升修正共享Θ边界，未引入新自由参数。B由原约束确定；配对defect求B的接口由[exact-lift-boundary稿](cdt_odd_paired_exact_lift_boundary_20261007.md)独立完成，J7本身不依赖任何未证正常性。

## J3. source-invisible子核的actual配对已经确定

设τ=rankΘ，K0=kerΘ，dimK0=h=k−τ。J7/J8给

\[
\boxed{A_{\rm act}|_{K0\times K0}
=A_{\rm ref}|_{K0\times K0},\qquad
G_K|_{K0\times K0}=0.}
\tag{J9}
\]

因此这份actual子form完全独立于全部未知值提升和α。它可以从已知参考polynomials、literal binomial weights modp²、literal harmonic coefficients和T的lift直接算出，不需解6r个R(a)值。特别不可把J9简写成只含D的modp表达再除p；J4的leading carry仍真实存在。

若更换参考P̂而actual基不变，只要仍满足J2精度，则J7表明Aref的变化同样经Θ，J9不变。若更换T的整lift为T+pU，leading N̂杀K，所以J4作为K上form不变。这些独立性不允许任意改变K的坐标后不作congruence。

提升差的整个restricted修正rank≤2τ；source斜率rank同样≤2τ。J9不是非退化定理：finite-field form在子空间上仍可相消。新目标是确定这份已知h阶form的正常性，而不是继续将所有值修正作为未知。

## J4. 已知子form非退化时的τ阶二次gate

仅在已证或明确假设H=Aref|K0非退化时，选K=K0⊕U、dimU=τ，Θ_U:U→F^r单射。以下不能在H未知unit时擅自求逆。写

\[
A_{\rm ref}=\begin{pmatrix}H&E\\E^t&A_U\end{pmatrix},
\quad Z_\alpha=\Theta_U^t\mathcal Z_\alpha
=[Z_{0,\alpha},Z_{1,\alpha}],
\]

其中Z0为τ×h，Z1为τ×τ。J8准确成为

\[
\overline R_\alpha=
\begin{pmatrix}
H&E+Z_{0,\alpha}^t\\
E^t+Z_{0,\alpha}&A_U+Z_{1,\alpha}+Z_{1,\alpha}^t
\end{pmatrix}.
\tag{J10}
\]

只消去这个known H，得到

\[
\boxed{\det\overline R_\alpha=\det H\det\mathcal C_\alpha,}
\]
\[
\mathcal C_\alpha=A_U+Z_{1,\alpha}+Z_{1,\alpha}^t
-(E^t+Z_{0,\alpha})H^{-1}(E+Z_{0,\alpha}^t).
\tag{J11}
\]

τ阶C的entries最多二次α。此处二次项是对source-invisible块的合法Schur结果，与上轮一般affine staircase的不产生二次项并不矛盾；两个消元对象不同。h=0时空det=1，C退为affine；τ=0时全部source和提升修正均消失，仅剩Aref。

置 P0=Θ_UᵀP|K0（τ×h）。C的二次系数为

\[
\boxed{C_2=-\tfrac{16}{9}P_0H^{-1}P_0^t.}
\tag{J12}
\]

这项不含B或actual提升选择。故有严格的鲁棒充分条件：若H与P0H^{-1}P0ᵀ均为单位，则actual det Rbarα为degree恰2τ的非零多项式，无论J7的值边界修正是什么。leading coefficient为

\[
\det H\,(-16/9)^\tau\det(P_0H^{-1}P_0^t)\ne0.
\tag{J13}
\]

该条件必要求h≥τ，即k≥2τ；τ0按空矩阵处理。至多2τ个source residues失败，接原Smith/whole-X推论时仍用leading radical维数k，不能用2τ代替。实际H与压缩是否单位仍未证；本稿不将一般充分条件当作actual infinite regularity。

## J5. 核查边界与下一问题

J7–J9是实际first residual的新无条件结构结果，J11–J13是明确known-subform条件下的较小门槛。J4准确保留modp²进位，避免从modp leading Gram直接除p的错误。全文没有actual higher Smith或新prime数据，也没有全局费用改进。

**推论J14（actual first form的完整参考计算）。** 实际全文读取exact-lift-boundary候选ca43e16f的E5–E19后，可将其已自证的E6代入J7：每个strong/weak reference correction的B列为Σ_(z≤4r)T_i(z)κ_z/S'(z)，κ是原E-weighted head配对defect除指定p层。其weak闭式E14、strong reference gauge E19都是已知调和和与head值；head cardinal E8给degree<8r的exact actual correction。因此actual A完全由reference N的literal modp²（保留进位）和已知有限head求和完成，不需解任意6r个第二阶negative值。这是对原actual剩余form的计算身份，不是另一个自由参考form的正常性结论。

下一步应证明这些明确矩阵或H/P0压缩的正常性。即使得到per-prime regularity，fixed rational source无限成功仍需真实统一算术，不能用坏residue密度替代。whole determinant无限非零和足够解析–算术strict margin也独立未证。

本轮root数学producer执行0、失败0、重跑0、旧/同行execute-import0、辅助单位素数扩表0、Lean0。尚无新的ζ/L/Catalan无理性或线性无关性定理；独立实际全文核查和最后来源收据另存，不提前声称已完成。

## J6. primary文献与不可跨越的generic条件

正常verified TLS新增归档 De Terán–Mehl–Mehrmann, *Low rank perturbation of regular matrix pencils with symmetry structures*, [arXiv:1902.00444v1](https://arxiv.org/abs/1902.00444v1)/[本地原件](../literature/cdt_paired_reference_jet_sources_20261007/de_teran_mehl_mehrmann2019_low_rank_symmetry_arxiv1902_00444v1.pdf)，37页、521780bytes，SHA256 4a97d0fac414073aec97b3f534d1359b3abf37cfcf307880e91720f69ce23f94。root实际完整文本读PDF1–6共6distinct页，未称全文验证，无重复下载/TLS绕过。

PDF2的generic参数空间、PDF3–4的normal rank与regular/singular定义、PDF5–6的structured paired rank-one项提示用ΘᵀZ+ZᵀΘ保留结构。该文研究复数域上的generic perturbation，且其目标pencils起始regular；本题的有限域actual边界、固定调和和参数及无限素数序列未被该假设覆盖。所以未用generic结果证明本family regular，也未套Hermitian符号正性。J7–J14全部由本稿和实际lift约束直接自证。
