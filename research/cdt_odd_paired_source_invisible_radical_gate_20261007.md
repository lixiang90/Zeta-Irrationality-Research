# 真实源不可见radical的小门槛、相容双曲消元与更浅Smith层

2026-10-07，NEW，/root/source_pencil_finalize。此前548冻结记录（543数学文件、5旧guard）和最新audit `222765c5ecbbba1ba9bf28e19bfe68b14811bd8fe9bc999623476ecbb94ff573`只读。本轮数学producer新建/execute/import/rerun0，辅助单位素数扩表0。保留原B6/k3/s5、degree<3n、饱和rank2n配对格S、fixed rational源ξ=αζ4+βζ5及whole-X D_A。

本轮把原source斜率的radical分成一个**参考形式已确定的不可见部分**与一个更小的有Θ坐标部分。若前者unit，未知深方向至多r−dimK0；若真实cross pairing达到满rowrank，则只需这份更小的known form unit，便得到actual第一pencil regular，不再要求整个Aref|K0 unit。这些unit和rank条件尚未在实际无限序列上证明。

## 1. 实际输入与读取范围

实际读取当前authority [总报告](cdt_odd_background_progress_20261006.md)§§156–160；最新[metadata audit](cdt_odd_delivery_shallow_joint_20261007.json)header部分和完整JSONparse、物理SHA核对，不声称数千字段人工全文读或本人重新核查全部548记录。最先定位到旧reference audit7141后，进一步定位shallow_joint222765，后者才是本轮baseline。

实际完整回读冻结[source S1–S14](cdt_odd_paired_source_radical_response_20261007.md)、[pencil P1–P18](cdt_odd_paired_source_pencil_regular_20261007.md)、[reference J1–J14](cdt_odd_paired_reference_jet_completion_20261007.md)、[hyperbolic I1–I14](cdt_odd_paired_invisible_subform_arithmetic_20261007.md)。以下仅用它们已证的真实有限处身份，自证新的有限维消元。没有使用未审未来paper或generic perturbation theorem。

取n=4r、p=18r+1素数、F=Fp，避开fixed源分母与β素因子。β为F单位。原normalized8r矩阵有Nbar=6βA5；K=kerA5、k≤2r。置

\[
K_0=\ker\Theta,\quad h=\dim K_0,\quad\tau=\operatorname{rank}\Theta,
\quad k=h+\tau,\quad\mathcal P:K\to F^r.
\tag{K1}
\]

I8已证P|K0单射，故h≤r；Θ(K)维数τ≤r。冻结J7给actual常数form及真实lift boundary：

\[
A=A_{ref}+6\beta(\Theta^t\mathcal B+\mathcal B^t\Theta),
\quad\mathcal B=L\Delta,
\]
\[
\Gamma=6G_K=\Theta^t\mathcal P+\mathcal P^t\Theta,
\qquad\boxed{\overline R_\alpha=A+\lambda\bar\alpha\Gamma,
\quad\lambda=4/3.}\tag{K2}
\]

B不是自由参数：J14的literal reference modp²（包括真实carry）与已知head配对defect求和已经完成它。本文既不删除A，也不把Aref从modp leading form直接除p。

## 2. 相容cross与源不可见radical

选K=K0⊕U；Θ_U:U→F^r单射，dimU=τ。定义真实τ×h pairing

\[
C_0=\Theta_U^t\mathcal P|_{K0},\quad s=\operatorname{rank}C_0.
\tag{K3}
\]

其rank与U选择无关：更换U代表加K0不改变Θ；更换basis只左右GL。s就是Θ(K)与P(K0)在F^r标准pairing中的相容秩。

令D=radΓ=radG_K，定义D0=K0∩D。对v∈K0，K2给Γ(v,w)=P(v)^tΘ(w)，故

\[
\boxed{D_0=\ker C_0\subset K_0,\quad d_0=\dim D_0=h-s.}
\tag{K4}
\]

P(K0)有dim h，Θ(K)^⊥有dim r−τ，因而交集至多r−τ；P|K0单射给

\[
\boxed{\max(0,k-r)\le s\le\min(h,\tau),\quad
\tau-s\le r-h.}\tag{K5}
\]

这里D0完全由actual leading maps决定。它不是整个K0；也不是rad(Aref|K0)。两种radical必须分开。

选K0=D0⊕V、dimV=s，并选U=U1⊕U2，使C0在V×U1为unit、dimU1=s，而U2=ker(C0^t)⊂U是对P(K0)的annihilator、dimU2=τ−s。用V/U1的GL把这个cross block规范为I_s。按(D0,V,U1,U2)排列，Γ为

\[
\begin{pmatrix}
0&0&0&0\\
0&0&I&0\\
0&I&M&E\\
0&0&E^t&\Gamma_2
\end{pmatrix}. \tag{K6}
\]

其中M对称，E为s×(τ−s)。把U2的basis改成U2'=U2−V E，恰消去E；Γ(U2',U2')仍是Γ2，因为Γ(V,U2)=Γ(V,V)=0。这是常数GL，Θ_U2'仍等于Θ_U2，保持其单射。准确得到

\[
\boxed{\Gamma\simeq0_{d0}\oplus
\begin{pmatrix}0&I_s\\I_s&M\end{pmatrix}\oplus\Gamma_2.}
\tag{K7}
\]

已知2s块det=(-1)^s，不除任何未知actual form。若D2=radΓ2在U2'内的lift，则

\[
\boxed{D=D_0\oplus D_2,\quad
d_2=\dim D_2=\operatorname{corank}\Gamma_2,
\quad\operatorname{rank}\Theta|_D=d_2,}
\]
\[
\boxed{g=\operatorname{rank}G_K=2s+\operatorname{rank}\Gamma_2,
\quad d_2\le\tau-s\le r-h.}\tag{K8}
\]

D2中的Θ单射来自U2'的Θ单射；不是说D0中的Θ单射。K7–K8将原双曲亏秩界细化为actual cross相容分解，而非笼统从M单射推metric unit。

## 3. 只消去较小的known form

记

\[
H_{00}=A_{ref}|_{D0\times D0}=A|_{D0\times D0}.
\tag{K9}
\]

第二个等号因D0⊂kerΘ；H00可直接从真实reference完成计算，独立于α与lift边界。**仅在H00已证或明确假设unit时**，选K=D0⊕Y并作常数Schur：

\[
\boxed{\det\overline R_\alpha=
\det H_{00}\det(A'+\lambda\bar\alpha\Gamma_Y),
\quad A'=A_{YY}-A_{Y0}H_{00}^{-1}A_{0Y}.}\tag{K10}
\]

等式按这一basis计算；相对先前basis另有已知GL determinant平方的非零因子。因为Γ(D0,K)=0，cross A0Y不含源α，Schur没有α²；Γ_Y就是K7的剩余斜率，radical恰D2，维数d2≤r−h。更换D0的actual basis只作congruence，不使H00unit成为新的自由选择。

完整regularity仍准确等价于K10余下actual affine pencil的P3 staircase成功，但其第一radical已从d0+d2减少到d2。H00未知或singular时不能执行这个消元，也不能据此断言原pencil失败。

**条件浅层推论。** 假设H00unit，选Γ_Y的已知g阶非退化补空间，g=rankΓ。该block的det源多项式degree恰g，最高系数λ^g detΓ_unit非零（g0空det=1）。因此至多g个α residues例外；其余所有p整α与每个X∈Zp满足

\[
\operatorname{rank}\overline R_\alpha\ge d_0+g=k-d_2,
\]
\[
\boxed{\#\{N\text{ 的Smith指数}\ge2\text{或}\infty\}
\le d_2\le r-h,
\quad\#\{\text{指数}\le1\}\ge7r+h.}\tag{K11}
\]

证明只沿原局部整消元：N的0层恰8r−k，1层恰rankRbar。normalized X项至少p³，不进入以上源例外集合。令I_d(N)为全部d×d minors的理想，则首d个Smith指数求和，在d=7r+h给准确条件估值

\[
\boxed{v_p I_{7r+h}(N)=\max(0,k+h-r).}\tag{K12}
\]

若d≤8r−k首d项全0；否则已证有足够1层，恰需d−(8r−k)=k+h−r个1。这里7r+h≤8r；h0及空H00均包含。K12只关于normalized N，不给原B相同的免费费用或解析衰减率。

## 4. 实际最高degree的d2阶门槛

在K7之后，进一步仅按Γ2分出已知非退化补空间。按(D0,D2,S)取常数GL basis Q，S维数g、Γ_Sunit，Γ在D0⊕D2上零。多线性det展开准确给

\[
\deg_\alpha\det\overline R_\alpha\le g,
\]
\[
\boxed{[\alpha^g]\det(Q^t\overline R_\alpha Q)
=\lambda^g\det\Gamma_S\det(A|_D).}\tag{K13}
\]

选择g个源项时它们必须全部来自S的rows/columns，余下项恰是A|D；不存在带source cross的漏项。原basis中的系数再除(detQ)²，故最高系数非零/degree不依basis。K13不要求A|Dunit来成立；它证明达到最大可能degree g**当且仅当**A|Dunit，未声称degree低于g必恒零。

若H00unit，设置Aref在D0×D2的块E02、在D2上的块Aref22；并令Θ2=Θ|D2、B0=B|D0、B2=B|D2。真实d2阶Schur form为

\[
\boxed{\begin{aligned}
\mathcal L_{deep}={}&A_{ref,22}
+6\beta(\Theta_2^tB_2+B_2^t\Theta_2)\\
&-(E_{02}^t+6\beta\Theta_2^tB_0)
H_{00}^{-1}(E_{02}+6\beta B_0^t\Theta_2).
\end{aligned}}\tag{K14}
\]

则det(A|D)=detH00 detLdeep。K14大小d2≤r−h，独立于α；真实已完成B被保留而非设为0。因此在H00unit条件下，Ldeepunit等价于原det达到degree g，足以推出actual regularity。若Ldeep singular，仅证明最高项消失；低degree regularity仍可能经真实staircase成立，不能当作singularity判据。

## 5. full-row相容分支不再需要整个K0form unit

**定理K15。** 假设真实s=τ，即C0满rowrank。则U2空、D2空，

\[
D=D_0,\quad g=2\tau,\quad\dim D_0=h-\tau.
\]

取K=(D0,V,U)，V维数τ，C=C0|V为unit。未必把C规范成I。该basis的source块为[[0,C^t],[C,M]]，det=(-1)^τ(detC)²；K13给无需任何H00逆的准确最高项

\[
\boxed{[\alpha^{2\tau}]\det(Q^t\overline R_\alpha Q)
=(-1)^\tau(4/3)^{2\tau}
(\det C)^2\det H_{00}.}\tag{K15}
\]

因此，在这一实际rank分支内，degree恰2τ当且仅当**较小的H00unit**。若H00unit，original actual源pencil regular，至多2τ个residues使first residual失败；其余给原N的Smith型0^(8r−k),1^k和whole-X估值−34r+k及非零归一化常数。H00即使singular也可能有较低degree regular；本文未反向排除。

这个最高项独立于B，因为D0⊂kerΘ；wholeAref|K0可以singular。特别若真实h=r，则P(K0)=F^r，Θ(K)的τ个坐标在其上独立，**自动s=τ**；所以仅需一个(r−τ)=2r−k阶known H00unit便可证明regular，而不要求此前极大k=2r。没有断言h=r或这个unit条件在实际序列中发生或无限发生。

与冻结J13的关系可以精确核查。若额外H0=Aref|K0unit，则在(D0,V)basis中C0=[0,C]，Jacobi complementary principal-minor identity给

\[
\boxed{\det H_0\det(C_0H_0^{-1}C_0^t)
=(\det C)^2\det H_{00}.}\tag{K16}
\]

旧J13的两个unit条件于是推出K15；新K15删掉整个H0unit的要求。这个扩展可由明确一般线性代数例子证明，并非原actual family的新增prime实例：在任意char≠2,3的域取r=2、K=(d,v,u)，Θ(d)=Θ(v)=0、Θ(u)=e1，P(d)=e2、P(v)=e1、P(u)=0，Aref=diag(1,0,0)、B=0。M=(Θ;P)单射，h=2、τ=s=1，H0=diag(1,0)singular，而D0=span d、H00=1，detRα=−(4/3)²α²非零。没有执行程序，也不声称这些toy数据由原primitive约束产生。

## 6. 量词、边界与下一问题

H00unit下K11–K12也适用于α、X的p-Gauss形式变量域：residue field F(α,X)中非零源多项式为unit。形式源自动非零不证明同一fixed rational α无限避开例外。K15也只在每个满足s=τ及H00unit的实际prime上给residue结论；可随p选好residue不能换成一个新特殊值定理。

若τ0，则s0、D0=K=K0，H00unit是整个constant Aunit条件，源多项式degree0。若h0，D0空、K10是原pencil，K11退回此前7r界。若s0或Γ2unit，相应空pair/空radical的det按1处理。所用4/3、6、β在当前p≥19均unit。

新进展是actual cross-compatible源分解、只在D0上检查的known constant gate、条件deep方向数≤r−h、d2阶真实最高degree门槛，以及s=τ分支中严格弱于旧J13的regularity充分条件。一般H00unit、s=τ、Ldeepunit、实际完整pencil regular和fixed源无限有效性仍未知。未证明原whole determinant无限非零、n²算术费用改善、same-object strict解析–算术余量或任何新ζ/L/Catalan无理性/线性无关性。

本人新增数学producer/source0、execute0、failure0、rerun0、旧/同行execute-import0、辅助素数扩表0、新prime实验0、Lean0；新文献下载0、PDF实读0。仅有MD创建/读取、metadata JSONparse和SHA查询。候选待实际全文独立review及作者最终全文自读；最后一向来源收据另存，不覆盖此前548记录。
