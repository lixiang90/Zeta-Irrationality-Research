# 互补 quarter 实际秩19的只读独立审查

日期：2026-10-06。审查者 quarter_mixed_arithmetic。实际全文读 [实际秩稿](cdt_odd_quarter_product_actual_rank19_20261006.md) §§1–6、[来源收据](../literature/manifest_cdt_odd_quarter_actual_rank19_20261006.json)、[19行接口](cdt_odd_quarter_product_rank19_interface_20261006.md)、[互补稿](cdt_odd_complementary_quarter_period_product_20261006.md)、冻结 [spin主稿](cdt_odd_classical_spin_pullback_20261006.md) §§1–7、[Sp4证书说明](cdt_odd_classical_spin_monodromy_20261006.md) 及 [J模型](cdt_odd_quarter_shift_full_model_20261006.md) §§1–2。未运行或 import 数学 producer；未以本审查冒认任何有限检查次数。

**结论：通过。** 实际 quarter 乘积 Q=(A−1/2)J 的 scalar cyclic 秩恰19，19行原有理模型独立，完整共同 translation radical 为 Ga8；这些功能性结论在有限代数base cover后保持。它们没有证明端点的数值无理性。本审查不对本人所写 mixed Smith 稿作“独立审查”；其 local/cost proof 由root另审。

## 1. 固定系统与共同齐次群

重新展开 P=θ⁴−x(θ+1/2)⁴，并以 F_i=(θ−1/4)^iF、J_i=(θ+1/4)^iJ，确得实际稿R3和19接口T3的同一 rational companion 及forcing：a=(1+x)/[512(1−x)]、b=1/[256(1−x)]。t=x^(1/4) 给 Y_A=tY、Y_J=t^(−1)Y，gauge方向正确。

冻结spin主稿P13–P14及精确Lie闭包的书面证明给P的完整monodromy/PV群Sp4；本审查读其论证，不重跑其证书计算。实际稿R4的 joint closure论证成立：Kummer字符kernel是基础π1的index4子群，P-image的Zariski closure若小于Sp4，则Sp4会成为有限个较低维coset的并，违背connected群的不可约性。因此该kernel的P-image仍dense于Sp4。joint closure先含Sp4×{1}，再用一个Kummer字符i的loop消掉其Sp4分量，得到(1,i)，遂为Sp4×μ4。两个齐次系统regular singular，所以Schlesinger可用。

translation模V_A=χV、V_J=χ^(−1)V在**完整**G0上不可约且非同构。Sp4标准模的Hom只有scalar；(1,i)分别作用i和−i，迫intertwiner为0。只看connected Sp4会错误遗漏此区分。

## 2. 两个非分裂扩张确实迫完整Ga8

R2的两个constant-forcing方程没有k=C(x)有理特解：各有限点的negative Laurent root排除poles，余下polynomial的最高x^(d+1)项非零，不能等于constant。F-forcing通过加1/2准确转成A的constant-forcing。这与冻结单源非分裂证明一致。

R6不是预设符号独立，而是从σu−u满足真实齐次系统推出的PV action。由restriction onto共同齐次PV场可得G→G0满射，N是Ga8中的closed algebraic subgroup。char0下它是linear vector subgroup，且满射使它G0-stable。完整G0的finite-dimensional representations semisimple，所以其在两个nonisomorphic simple summands内的subspace只能选零、一个summand或全部。

审查了“projection不能为0”的必要步骤：若N→V_A为0，将G映到V_A⋊G0后的closed image H→G0仍满射且kernel为0；char0群同态/closed image定理使H≅G0。其affine cocycle给5维representation extension。semisimplicity使cocycle是c*−ρ(g)c*，故u_A+Y_Ac*被所有PV automorphisms固定；fixed-field theorem使其first coordinate属于k，形成已排除的rational particular。V_J同理。因此N投影到两方都非零，结合非同构性准确迫N=V_A⊕V_J=Ga8；不是仅凭“两扩张各自非split”就跳过共同radical问题。

Ga8全满后，可用translation消掉每个G0 lift的translation部分，故增广群为Ga8⋊(Sp4×μ4)。原九维系统只含Y_A、Y_J、u_A、u_J时，restriction kernel需同时ζh=ζ^(−1)h=I且c=d=0，因此恰{(I,1),(−I,−1)}。该中心在两translation模上作用平凡，R8的finite quotient正确。原系统的2 components与增广的4 components被准确区分。

## 3. 八个jets与19维scalar orbit

L/K0以八个真实jets生成，Gal(L/K0)=Ga8。PV dimension公式给trdeg=8，故八generators代数独立；将“八个generators”和“八维transcendence degree”结合，没有只从group dimension声称单个周期值超越。特别F、J在K0上代数独立。

真实N action为Q↦(F+t y(c))(J+t^(−1)y(d))。单factor difference及mixed difference给Q、tJy_i、t^(−1)Fy_i、y_iy_j的19维candidate C-space，所有conjugates也在该空间内。Sym²标准Sp4为10维adjoint不可约模；产品map Sym²W→L是equivariant且非零，因此injective，十个products C-linearly independent。其余九项的独立性随后由F、J在K0上代数独立逐个比对FJ、F、J、constant polynomial coefficients严格推出。

因此conjugate **C-span**恰19。任意r阶k-scalar annihilator同样湮灭全部conjugates，而r阶homogeneous equation的solution C-dimension≤r，所以r≥19。19接口T2–T4给derivation-closed k-space包含Q，给r≤19。上下界相合，且一旦19行存在k-linear relation，closed span≤18又与lower bound冲突，故它们确为实际basis。这里没有把C-orbit dimension和k-derivative-space dimension未经论证地混同。

## 4. 有限代数cover不会消去这项实际秩

实际稿用k_alg=L^(G°)与finite Galoisclosure k''处理任意finite k'/k。fixed-field theorem给k_alg为k在L内的relative algebraic closure；char0中L/k_alg regular，故与finite algebraic field k_alg k''线性无交。每个G° automorphism因此可延拓至Lk''并固定k''。特别全部connected Ga8 translations仍存在，R9–R11的lower bound保持；19行upper bound也保持。

这一步避开了一个真实潜在陷阱：四次cover后V_A、V_J作为connected Sp4模会变同构；不能重新只用“单方non-split”推出joint Ga8。本稿从已建立的完整PV场及connected subgroup保存Ga8，因此论证有效。F、J的代数独立在finite algebraic enlargement的K0上保持，也可由finite norm polynomial反证。

R12的rational coefficients与Q[[x]] germs同时保证Q(x)上的upper19；C(x)上的lower19当然覆盖Q(x)。finite cover中的derivation唯一延拓，换用cover parameter只将derivation乘非零algebraic因子，不改变scalar order。

## 5. 原始理论实际核读及来源收据

本审查实际提取并阅读本地Singer PDF10–14、17–20：PV construction、Theorem1.3.9/Corollary1.3.10的fixed field和relative algebraic closure、Corollary1.3.21的group dimension/trdeg、Proposition1.3.27的Schlesinger条件。另实际提取阅读Milne PDF86、300、489–490：Theorem3.34/Corollary3.35的group homomorphism closed image/zero kernel，Corollary14.33的additive vector groups，以及Corollary22.43明确覆盖nonconnected G0的semisimplicity。未认领通读其82/659页；未另下载或编辑这两份冻结原件。

只读复核收据中的bytes、pages、SHA256，全部一致：Singer 537902 bytes/82页/c805d45ed54e0e6734b4d7f125c197364b9eccab2a7e09a8c26c3bf63cf5db96；Milne 4838013 bytes/659页/f2ddd8fa4d263085f173934664b246007a2c0bd539739b7c82de39bfb5d21f40。实际秩稿SHA256为55adb223c226956a47a082eace77190ef7fe2d153f932494c68db8414ae72189；来源收据为49936b70d2f17daafb7e9b871e2ec2559d1eaf40262c44b4416b3a2e4738c1f4。

此独审使 [mixed稿](cdt_odd_quarter_product_mixed_packet_20261006.md) P16/P19中“19行实际独立”的条件获得已验证的功能性依据，可以实际取m=19；其packet、费用及52项有限记录仍须由root分别审查，不能以本rank审查替代。未给数值无理性、线性无关性或Lean声明。
