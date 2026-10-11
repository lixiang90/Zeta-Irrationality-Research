# R₀ Betti整扩张与conifold有效分母：独立全文审阅

日期：2026-10-06。NEW 纸面独审。全部旧/同行数学 MD/PY/JSON/manifest 只读；本独审没有执行/import/rerun任何数学 producer。

实际全文读 [Betti extension](cdt_odd_R0_regulator_Betti_extension_flag_20261006.md) 初稿
6e58db381dca549e7a60e4b69f293fb11b943eff0f2290bce1c7a6f3a005dd6d，
发现B11错误家族后通知作者及root；作者改正后再次**全文**回读
4abdcbc370b69413b07e837724867897760f493b7ee65e6d0b47a705f96292f4。
实际全文读 [denominator proof](cdt_odd_R0_conifold_effective_denominator_20261006.md)
的首次候选，数学公式逐项手核；作者补排版、sqrt同界和来源执行历史后，再次实际全文回读最终
fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8。

**当前数学结论：Betti B2–B10、修正后的B11以及B12–B13通过；分母D1–D11与FR D12通过，D13–D14的generic-radius前提保留条件性。** 本独审不把integerBetti扩张当整Taylor比较，不从有限180阶JSON推全尺度分母，不给CDT容量或数值无理性结论。

## 1. Degree-one整数投影、saturation和index

本轮实际全文回读冻结Yukawa/scalar Y8–Y10。两条图映射
\(X\leftarrow Z\to W\) 都是smoothcompactproperbirationaldegreeone；不是degree64quotient。ordinaryintegerpullback及PD定义的integerpushforward保torsion，故降到free integral middlecohomology。已证 \(qi=1_{\mathbf Q}\) 推出 \(qi=1_{\mathbf Z}\)，因为freeendomorphism张量Q单射。push/pull伴随给
\[
 Q_X(iu,iv)=Q_W(u,qiv)=Q_W(u,v).
 \tag{I1}
\]
无raw/Tate form-normalization系数进入这个topologicalcup身份。

\(\Pi=iq\)于是integerorthogonalprojector，image \(H_X\cap V_{\mathbf Q}\) saturated且cupunimodular。不需full \(H^3(X)\) rank4。有限cover上投影是actualcyclicsector唯一正交投影，deckinvariant，逐fibreintegrality保留于原base。temporaryspread删掉的ordinarysmoothpoints通过locallyconstantintegral lattice补回，非额外ramified费用。

这与本人本轮独立实际orbit稿O30–O34完全一致。actualorbitGramPf−256，det \(2^{16}\)，故在unimodularsector内index恰256。**GramSmith8,8,32,32仍不等于包含的actualSmith。**

## 2. current标记、actualcocycle和χ twist

为核B3–B5，本独审实际全文读冻结positive-cut-boundary-flux稿，核其chosen\(r_c\)和真实Γmark。实际basis的periodmap按
\[
 f_z=-\frac a{16}Q(z,\omega),\quad a=2\pi i,\quad
 R_c=\Pi r_c/a^4,\quad W=f_{R_c}.
 \tag{I2}
\]
所以归一化后的Betti平移在rational compact \(V\) 中，不能以singlepointscalar zero证明向量zero。作者用wholeperiodgerm加cyclicfourjetnondegeneracy，此injectivity严格成立。

origin \(W=\sqrt xB(x)\)给 \(W^0=-W\)、\(\chi_0=-1\)，故 \(c_0=0\)。conifold
\[
 M_1G=G-8\Delta,\quad
 h_G=a^3y_0/2,\quad
 W=\Psi+\pi^4y_0/16
\]
给 \(W^1-W=-\pi^4g/a^3=-ag/16=f_\Delta\)，故 **实际** \(c_1=\Delta\)。pathmultiplication与lefttransport按作者约定，\(c_{\gamma\eta}=c_\gamma+M_\gamma c_\eta\)。integerM和两generatorintegerc给任意wordintegerc，无wordlength增长。

actualBettiextension的sourcecharacter为1；scalarPF系统额外twist整扩张 byχ，才得到
\[
 T_0=\operatorname{diag}(U,-1),\quad
 T_1=\begin{pmatrix}M_1&\Delta\\0&1\end{pmatrix}.
 \tag{I3}
\]
physical \(M_0=-U\)与scalar \(T_0|_V=U\)严分，未偷把signedloop当physicalone-turn。矩阵作用與cocycle的raw/Tate factors一致。

## 3. Γeven、corrected成本以及新primitive限制

actual \(N^3=(U-I)^3\) integral、\(N^3\Delta=2G\)、\(\Delta G=8\)给
\[
 N^3z=(z\cdot G)G/4.
 \tag{I4}
\]
在unimodularsector写 \(G=d\gamma_{\rm prim}\)，选整数dualvector，则 \(d^2/4\)必integer。又 \(d\mid8\)，所以 \(d\in\{2,4,8\}\)。sign也与本人orbitO35一致。\(G/8\)sourcecochain成本≤4；correctedcocycles
\[
 c_0^{\rm corr}=-G/4,\quad c_1^{\rm corr}=0
 \tag{I5}
\]
成本≤2，稳定格可取 \(\Lambda+\mathbf Z(4e_c+G/2)\)。均是安全界，不声称最小。

本独审先独立推出并通信，作者已在未冻B7.7完整写出：

* \(\Delta=d_\delta\delta_{\rm prim}\)且Uintegerautomorphism，使 \(d_\delta^2\mid\Delta U\Delta=8\)，故 \(d_\delta=1\)或2；若2，则 \(d_G\ne8\)。
* 在perfectsymplectic \(\Lambda/2\Lambda\) 上，整个Uorbit的互交点为8倍，spanisotropicdim≤2。其Ustable且unipotent，所以 \((U-I)^2\Delta=0\bmod2\)。
* actual \(\alpha=(-3+4U-U^2)\Delta=2A\Delta-A^2\Delta\)于是even；\(\alpha U\alpha=-64\)给 \(\operatorname{div}\alpha\in\{2,4,8\}\)。

这些是paperlemmas，不是finiteprimitiveguess。旧冻结orbit稿O27的安全界未改写。

## 4. CRT多项式与actualoperator：完整系数核查

rank5：minpoly \((z-1)^4(z+1)\)给
\[
 p_{5,+}=1-(T-1)^4/16,\quad
 N^3p_{5,+}=(T-1)^3(T+1)/2.
 \tag{I6}
\]
用 \(A^4(A+2)=0\) 核 \(A^7=-8A^4\)，得作者公式。约化最高系数分别−1/16、1/2，所以universalrationalpolynomial费用16、2不能缩小；monic最小多项式的integerdivision不会隐藏降低最高系数。actualcenteredsplitting给相应integerblockoperators；这不声称integerpolynomial表示，也不是globalflatgauge。

rank9：primitiveexteriorkernel是unimodularpairing的surjectiveintegralmap的kernel，因此saturated。原点分块 \(\wedge^3\Lambda\)与 \(e_c\wedge\wedge^2_0\Lambda\) 具有 \(J_4(+1),J_5(-1)\)。Jordan手核
\[
 N^4(e_3\wedge e_2)=2e_1\wedge e_0\ne0,\quad N^5=0.
 \tag{I7}
\]
primitive五空间确含size5block；另一trivialquotient不能承载 \(N^4\)。

展开 \((u-2)^{-4}\) 前五项确为
\[
 (16+32u+40u^2+40u^3+35u^4)/256.
 \tag{I8}
\]
rank9minpoly \((z-1)^4(z+1)^5\)给author \(p_{9,+}\)；
\((T-1)^3(T+1)^5/32\)在negativeblock0、positiveblock等于 \((T-1)^3\)。
highestcoeff分别−35/256、1/32，通用费用256、32准确。
actualsplitinteger格上的operators费用1，symplecticcontraction用 **topologicalunimodularcup** 是integerisomorphism。analyticperiodconcomitant \(C\) 与这个topologicalcup的Tate scale仍属于comparison；不能由此宣布analyticZ行整数。

## 5. B11发现、纠正和目标保留

初稿6e58的family写成 \(\Phi_\Psi-q\,y_0\wedge g_1\wedge g_2\)。
由冻结E24，所有这种变化都被最高log旗标杀掉，因此其“iffq=α₀”错误。本独审实际回读exteriorE1–E2/E10–E11，向作者/root说明；root独审也独立发现同项。

作者修正后的4abd全文回读确认：
\[
 \Phi(q)=Y_{h+qg_0}\wedge Y_{g_1}\wedge Y_{g_2}
 =\Phi_h+q\Phi_0,\quad
 \Phi(\alpha_0)=\Phi_\Psi.
 \tag{I9}
\]
\(g_0\)不是vanishing \(v=g_1+3g_2/4\)。冻结E27的 \(C(y_0,v)\ne0\)于是确给唯一q=α₀。作者保留修订history，未改旧冻稿。

B12原件KLM明确topologicalclassatworsttorsion；rationalcompletion不推出integralcompletion成本2。B13constantnormalfunction反例及合法periodshift也正确：integercocycle不保证代数initialjet。既有chosenΨ身份保留，不把它撤回为unknownhomogeneouserror。

## 6. 有效二进制分母：直接解向量递推

作者实际P与jetgauge
\[
 y=(f,f',f''+tf''',t^2f''')^T
\]
的D3全部entries独立手核。第四阶forcing是
\(\beta/(16t(1-t)^{7/2})\)，第三/第四source分别
\(\beta t/(16w^{7/2}),\beta t^2/(16w^{7/2})\)，没有forcing误号或额外w。
令u=w−7/2添第五行，再 \(t=4z\)、\(S=\operatorname{diag}(1,2,4,1,1)\)，D5所有25entries核准；分子integer、分母只 \((1-4z)^k\)。

residueR仅 \(R_{1,3}=-2,R_{2,3}=-6\)，所以 \(R^2=0,R\in2M_5(\mathbf Z_2)\)。规范化fourinitialvectors为作者所列，全部kerR中。regularsource向量没有被换成日志fundamentalmatrix。

系数递推
\[
 (nI-R)d_n=\sum_{j=1}^nH_jd_{n-j},\qquad
 (nI-R)^{-1}=I/n+R/n^2
 \tag{I10}
\]
是exact，非adR基本矩阵递推。逆矩阵2-adic费用
\(e(v_2n)=0\)（odd）或 \(2v_2n-1\)（even）。
累计 \(E_n=2v_2(n!)-\lfloor n/2\rfloor\)非减，完整归纳得到
\[
 2^{E_n}d_n\in\mathbf Z_2^5,\quad
 \boxed{2^{b(n)}c_n\in\mathbf Z_2,\quad
 b(n)=2n+2v_2(n!)-\lfloor n/2\rfloor .}
 \tag{I11}
\]
Legendre给 \(b(n)/n\to7/2\)，\(b(n)\le7n/2\)。没有用180阶数据完成归纳。

## 7. Products、integrals与derivative成本

手核D10：
\[
 b(a)+b(b)-b(a+b)
 =-2v_2\binom{a+b}a+
 \lfloor(a+b)/2\rfloor-\lfloor a/2\rfloor-\lfloor b/2\rfloor\le1.
 \tag{I12}
\]
足够作者全部safecharges。实际上可≤0：后一项只有a,b都odd时为1，而此时binomialvaluation≥1；此fixedconstant微改进不改变主率，不要求作者重写安全界。

\(w^{-1/2}\)coeffbinaryfee≤2k≤b(k)；最终稿亦明确 \(\sqrt w=w\,w^{-1/2}\)，乘整数多项式只涉及前项，沿同一b界控制。积分系数再付4+v₂(m)，与
\[
 b(m)-b(m-1)=2+e(v_2m)\ge2+v_2m
 \tag{I13}
\]
给 \(F_j\)fee≤b(m)+3，\(F_1g_2-F_2g_1\)fee≤b(n)+4。Eulerderivatives是整数polynomial组合的ordinaryderivatives，最多两组thirdjets的总indexshift≤6，故整prefix可用 \(2^{b(N+6)+O(1)}\)。
\(q\)为代数时须固定数域和initialintegerfactor，未把单一realembedding的分母当all-placegerm。

## 8. FR原件、oddprime条件及有限数据范围

本轮实际FR publishedPDF6–8全部读。Theorem3有四条前提：unitdisknopoles、nilpotentresidue、Gaussnorm≤1、generic-pointfundamentalmatrix在openunitdisk收敛。D3直接证明前三条于所有oddprimes；第四条不能由前三条推出。

当第四条成立，μ4的FR指数为
\[
 3+v_p(3!)+\min(3,v_p(4\cdot6\cdot4\cdot1)).
 \tag{I14}
\]
所以p≥5为3，p3为5，准确保留两项extra3-fees。regularinitialvectorsinteger并kerG0，故holomorphicsolutions是 \(U(t)c\) 而非额外logbranch，无Laurentshift；D13/D14按genericradius条件成立。sourceh的oddbound未从μ4定理免费推，相关Fi是sourceintegration，付额外LCM一次。pure收缩D七、mixedD六与此前packet范围一致。

本独审实际完整只读rootNEWprobePY、symbolicPY/JSON。巨大probeJSON的首个Get-Content output被截断；随后只读parsedselectedmetadata和每条sequence summary，**没有**冒认独立重算全部181系数。JSON的scope与作者两producer首次各1次登记一致；13symbolicchecks不是全尺度定理。本人未运行它们。probe数据hash与symboliccertificatepin匹配。

本独审没有实际阅读本轮新增Katz全文，也不替另稿的所有oddprimes几何好约化检查作证。D14在作者此稿明确第四条件下通过；如另稿补证该条件，应对另稿另实际阅读/独审。

## 9. Actualread、hash与最终版本记录

* 本独审此前实际main79–84全读；delivery只读metadata。
* 旧Yukawa和real Betti两稿本轮实际全文回读；positive-cut-boundary-flux本独审实际全文读；exteriorE1–E2、E10–E11实际读。
* Betti初读6e58→改正后final4abd再次实际全文读；修正仅在作者未冻NEW稿，旧稿不改。
* denominator首次候选实际全文读；D1–D14按以上范围手核；最终 fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8 再次实际全文回读，核排版修复、sqrt同界及Katz locfree前提保留。Katz新PDF仍未由本人实际阅读，未扩大source claim。
* [FR primary](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf) actualPDF6–8；SHA c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68。
* [KLM primary](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf) actualPDF12–14；SHA 8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9。
* root symbolic PY SHA 7ac54b6094f4346673c1a931ced683fbf7143fe162af6b5caa200f01e48c1c01，JSON SHA305eb28b0d38bef698b02ae7871dc54e65b359742d310f7909022d1a0abfbc34；probe PY SHA6bae4c3b34b3bb006fa6a6b697251d8a9ff4543c797693ec4414eb66f1a27c6f，JSON SHA b275f2481c3f02b571ccadd447d5a776d58842eaa2614bde5c67ecb0bb801ebf。全部只读不执行。

没有新增PDF或本独审数学producer；本轮本人另有自有orbitverifier首次1run38checks，和本独审严格分开，不在此代root/peer重跑。没有新奇ζ/L/Catalan无理性、线性无关性、CDT反证或Lean结论。
