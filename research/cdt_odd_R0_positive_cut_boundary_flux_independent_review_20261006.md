# R₀ centered positive-cut 全角点稿的独立审阅

日期：2026-10-06。NEW 独立全尺度纸面审阅。审阅对象为 [positive-cut boundary flux](cdt_odd_R0_positive_cut_boundary_flux_20261006.md) 全文 F1–F11（包括编号 F1–F21），稳定 SHA256 `3fabdbfa3f4c0fd17e50db268b86cfe8c7d752f71a462bcdf0ebaeb1faa3d150`。实际全文读取，没有执行/import任何旧、作者或同行数学producer；本文不是有限样本核验，也不声明Lean验证。

## I1. 审阅结论与准确范围

在原稿已固定的 projective regular toroidal model、positive branch 与 LEFT residue 下，接受三个新增接口：

1. 四个对数同时减去 \(a/2=\pi i\) 后，current \(R^c\) 在每个 surviving cone 都有共同因子 \(\prod_{v_i=-1}z_i\)。该因子在每个 normal ray 至少一阶消失，且 partial cuts 在所有角点有统一 angular coarea 控制。因此局部可积零延拓 \(\widetilde R^c\) 存在，并满足 total \(d\widetilde R^c=\Omega_Y\)、fibre closed。
2. 此明确 current 是指定 family \(\Xi\) 的 actual compact rational AJ lift；它与 raw \(R^+\) 的差为真实 flat open Tate class。marked scalar 为 \(-16a^3W\)，加实际 \(a^4PD(\Gamma)/8\) 后为 \(-16a^3\Psi\)。这是指定 lift 的身份，不把任意旧膜设为同一标记。
3. canonical relative class \([\omega,0]\) 的通量为0；任意 rational horizontal splitting 的通量仍可非零，raw open Tate discrepancy 本身也实际 noncompact。

以上不给 integral saturation、目标数新无理性、full-row finite-place预算、CDT contradiction。审阅没有删去任意闭周期 ambiguity。

## I2. F2 的全 cone 与 primitive orbit coordinate

旧 toroidal 模型的 local support同时包含 fixed \(-1\) 与 fixed \(0,\infty\)，character
\(\ell=(-1\text{ on poles};2\text{ on }-1)\)。因为存在一个系数−1，\(\ell\) 在 \(M_S\) primitive；若在 saturated \(M_S\cap\tau^\perp\) 中可整除，则也在整个 lattice 可整除，矛盾。因此可选 orbit coordinate \(q_0=\chi^\ell\)。

每个 nonzero surviving ray 满足
\(\sum_{S_p}n_{b,i}=2\sum_{S_-}n_{b,i}\)。其 entries非负；如果后一个和为0，前一个也为0，ray即为0。因此 \(b_b=\sum_{S_-}n_{b,i}\ge1\)。共同乘积 \(Z_-\) 在所有normal directions都消失；单一 \(-1\) coordinate 不具备这个保证。

在边界 \(\phi=c_Sq_0\) 且 \(c_S\ne0\)。故解 \(\phi=\lambda\) 的 implicit derivative统一非零，compact parameter disk、orbit annuli与有限 fan给uniform bounds。这里不替换紧化，也不另加方便的非monomial blowup。

## I3. F3 angular minor 与 coarea 独核

角点中每个 forced \(-1\) coordinate 的 positive cut都空。fixed cut rows只来自 \(S_p\)，并可能加入 free phase rows。由于至少一个 \(-1\) row未切，其 \(\ell_i=2\) 证明 \(\ell\) 不在fixed cut rows的span中。故 fixed cut rows modulo fibre phase row独立。

regular toric coordinate change是 lattice isomorphism，ambient angular rows有非零 integer minor。free cut rows提供 identity block，fibre phase \(\arg q_0+\arg c_S(v_{\rm free})\) 的free derivatives可消掉；不丢失上述rank。解q₀后，得到真正fibre angular rank，而非忘记fibre constraint的ambient rank。每个partial cut最多三条row，与fibre real dimension相容。

\(c/c_S=1+O(\max|z_i|)\)，其角导数同阶，implicit q₀ derivative有统一界。finite chart覆盖给正的统一minor下界。该结论在 \(\rho_b=\epsilon\) faces仍有效，因为固定的是径向变量，没有删掉 normal angles。

coarea使用角变量。把delta phase constraints通过uniform angular graph积分后，其density和multiplicity统一有界；切相位的径向项为 \(O(z_i)d\rho_b/\rho_b\)，属原logarithmic coframe。没有多出一个未支付的 \(\rho_b^{-1}\) angular Jacobian。有限 toric character degrees和uniform local graph charts给有限sheet覆盖；本审阅接受原稿全部角点的统一估计，而非只列一项充分条件。

## I4. F4 的共同乘积及 F5 的全部 faces

near fixed \(-1\)，\(L_i^c=\operatorname{Log}(1-z_i)=O(z_i)\)，\(B_i=z_i/(z_i-1)d\log z_i\)，\(\Delta_i=0\)。令最早 forced \(-1\) index为i₀。ordered-cup中：j>i₀项为0；j=i₀项由centered log提供 \(z_{i_0}\)，其余 forced coordinates由dlogs提供；j<i₀项的全部forced factors也来自dlogs。每个surviving term因此确有全部 \(\prod_{S_-}z_i\)，并不是各项分别含一个不同因子。

与I3 coarea合并后，coefficient variation被
\(C\prod_b\rho_b^{b_b}(1+\sum_b|\log\rho_b|)\) 控制。对smooth test forms，pullback logarithmic coefficients有界；radial reference measure为 \(\prod_b d\rho_b/\rho_b\)。所有b_b≥1使局部mass有限。

在face \(\rho_b=\epsilon\)，剩余径向积分统一有限，所指定normal因子提供 \(O(\epsilon^{b_b}(1+|\log\epsilon|))\)，安全为 \(O(\epsilon(1+|\log\epsilon|))\)。codimension≥2 corners不额外贡献Stokes faces；finite atlas与partition给全局估计。因而zero extension没有divisor或higher-corner supported derivative。total与fibre test-form degree分别调整，不把三fold fibre和四fold total混同。

参数微分通过uniform angular graph把delta derivatives移到smooth test forms；implicit solution给 \(\partial_\lambda z_i=O(z_i)\)，保留共同消失因子。每个固定导数阶的积分可控，故closed current确为smooth cohomology family，可用于Cartan/Gauss–Manin。

## I5. F6 的真实 Tate class 与 compact AJ injection

CCW circle上 positive-cut coorientation \(\delta(\operatorname{Im}v)d\operatorname{Im}v\) 的积分为1，故 \([\Delta_i]=[B_i/a]=e_i\)，没有负号遗漏。F15每项closed，cohomology为
\[
 [R^c-R^+]=-\frac{a^4}{2}\sum_{j=0}^3(-1)^j
 e_0\wedge\cdots\wedge\widehat{e_j}\wedge\cdots\wedge e_3.
\]
此为total-space rational Tate class，其fibre restriction flat。四个unit同时换成−v也与 \(\{-1\}\) 的2-torsion一致，但以上identity独立给完整current比较。

本轮另外实际全文读 [regulator derivative](cdt_odd_R0_regulator_derivative_20261006.md)。其§6证明每个boundary component为smooth rational projective surface，\(H^1(E_i)=0\)，使用DeligneIII Cor8.2.8的graded Gysin exactness得到 \(H^3(X,\mathbf Q)\hookrightarrow H^3(U,\mathbf Q)\)。它没有断言整个SNC union的H³为0。

对rational injection \(A\hookrightarrow B\)，选择rational complement或tensor quotient即可得 \(A_\mathbf C\cap a^4B_\mathbf Q=a^4A_\mathbf Q\)。因此compact到open的 \(\mathbf C/\mathbf Q(4)\) AJ target也单射；这是本例Q-linear argument，不是一般商群函子保单射。degree3的 \(F^4\) 均为0。指定Xi的restricted AJ、F16和compactclosedcurrent遂给完整compact AJ equality。

别的actual rational compact lift与 \(r_c\) 只差 \(a^4q\)，q在compactH³(Q)；同一个total primitive下差flat。不存在把open Tate correction自身改称compactperiod的步骤。

## I6. F18/F19 的 scalar、orientation 与 marked lift

本轮另实际全文读 [positive-cut period comparison](cdt_odd_R0_positive_cut_period_comparison_20261006.md)。其normal-first triple-cut orientation为正，LEFT residue给两sheet \(\omega_-=-\omega_+\)；每个sheet的absolute integral finite。centering差中前三terms含holomorphic dlog，与(3,0)ω wedge为0；末term贡献 \(a^4/2\int_{T_0T_1T_2}\omega\)。两sheet按相同normal orientation积分相消，此项严格为0。

I4使compactcurrentpairing实际定义，故
\[
 Q(r_c,\omega)=-16a^3W.
\]
total derivative \(d\widetilde R^c=\Omega_Y\) 与LEFT尺度给 \(\nabla_\theta r_c=16\sqrt x\omega\)，holomorphic scalar可解析延拓；forcing是 \(-a^3\sqrt x\)，没有新Tate因子。

真实 \(\int_\Gamma\omega=-4i\pi^3y_0\) 与 \(a^4/8=2\pi^4\) 给cycle补偿 \(-8i\pi^7y_0\)。另一方面 \(-16a^3W=128i\pi^3W\)。相加恰为
\[
 Q(r_c+a^4PD(\Gamma)/8,\omega)
 =-16a^3(W-\pi^4y_0/16)=-16a^3\Psi.
\]
这是具体centeredcurrent+具体rationalcycle选定的真实标记。没有靠conifoldholomorphy推出任意lift的三个homogeneouscoefficients为0。

## I7. F8 relative fine complex、Hadamard product 与通量

对SNC coordinate union，所有divisor restrictions都为0的smooth forms构成fine complex。boundary stalk上的radial contraction保持每个coordinate hyperplane，终点pullback在kernel为0，所以stalk cohomology全零；interior是ordinary Poincaré lemma。因此该complex resolves \(j_!\mathbf C_U\)，计算relativecohomology，严格适用于reducibleE。

commuting coordinate projections的inclusion–exclusion公式确实extension相容intersectionforms，验证mappingcone接口。regularneighborhoodN retractsE只用于topologicalvanishing，再经finecomplex得smoothrelativeprimitiveη；不把nonsmoothretraction pullback当formconstruct。

η限制每个divisor为0的条件给logarithmic coefficients \(O(\prod_b\rho_b)\)：若一个standard basis component含normaldt_b或dbar_t_b，则改logframe提供ρ_b；否则该componentrestrictionzero，realHadamardlemma给 \(t_b g+\bar t_bh\)。独立normalvariables迭代给乘积，而非minρ_b。face restriction保持这些因子。

rawR⁺虽只有loggrowth，乘此η后同样满足I4 faceestimate；degree3 Stokes使用此前核准的正flux符号，通量极限为0。因此canonicalrelative \([\omega,0]\) trace等于rawcut scalar。一般rationalhorizontal splitting的primitive不满足η|E=0，故此证明不扩大为任意Bσ=0。

## I8. F21 的 noncompact boundary 与限制

在mandatorysupport(v₀−1,v₁zero)=(1,2)chart，\(v_0=-1+s,v_1=s^2w\)、w无零holomorphic。normalcircle×两个freecircles bounds \(D_s^2\times T^2\) incompactX。raw log near−1常数a/2，normalresidue为2(a/2)=a，乘normal积分a及两free积分a²得rawperioda⁴。compactclosedclass在boundingtorus的period为0，因此un-centeredopenTatediscrepancy有period−1，actualnoncompact。

centering把log改为Log(1−s)，normalresidue为0。I4负责所有cones/corners同时cancel，不只这个局部例子。该noncompact结论与canonicaltop-Hodge trace零不矛盾；它们测试的周期方向不同。

## I9. 实际阅读、独立性与冻结边界

本轮实际全文读取被审稿F1–F11、冻结regulator_derivative全文与positive_cut_period_comparison全文；这些读数全部只读。之前本审阅者已实际全文核toric/center/Yukawa/Kummer与boundarycomparison，原KLM、DeligneIII、FR primary的实际阅读范围已记录在自己的冻结arithmetichypotheses与boundaryindependentreview中；本轮不冒认新增PDFpage阅读。

I2–I8为这次实际对象的独立纸面手核。没有新网络下载、TLS例外、数学producer、有限samples、PSLQ或Leanclaim。接受的是explicitrationalcurrentmarking、全角点延拓和canonicalflux；整数格、finite-placeholonomy与具体数值定理仍未完成。
