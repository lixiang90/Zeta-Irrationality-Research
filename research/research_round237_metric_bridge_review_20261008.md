# 第237轮联合整格 BC 桥：独立交叉审阅

2026-10-08，Dual/C。**PASS；被审稿无需数学修订。** 数学程序0，未改作者稿、236冻结稿、main或manifest。

实际 FULL 读取最终两文件：

- research/joint_lattice_metric_bridge_round237_20261008.md，9821 B，SHA256 cf2550e55910f6feceff0652aa38b5a102749aed7479c67540a4a80bc7e190a8；全部六节B1–B14。
- literature/joint_lattice_metric_sources_round237_20261008/packet_reading_scope.md，4527 B，SHA256 5137be32687a0a8ddf78b2936f767ee9c911404ce1ba8e865f34ad4f237ea87e；全部四节。

本人先独立完成同轮数学稿，再读上述对象。本人实际完整原文为当前220页CDT的50–54、71–77、95–110及235复用目录1–2；采用§7.2 degree/slopes、§7.3 Hilbert–Samuel/source/evaluation、Lemma7.4.1完整pole-clearing与mixed-limit、Lemma7.4.5完整intersection。PDF身份3628820 B / 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c。没有把作者读90–94或两页PNG的事实转成本人的读取；未FULL读220页、BC原著或重证Shidlovsky。

直接纸核如下。P↦u⁻ᴰP为整数基反序；section的graded order为原Taylor指数n，leading不变。Γ∩有理vanishing子空间是primitive，rank1商无扭；完整Taylor jets覆盖全部jumps才给每个hp≤0。BC real metric不变，degree恰减logindex；arch quotient只依同real flag，故不要求低height CRT基。固定ρ清除有限poles，hρ(0)=1保留leading；先D→∞再ρ→1，mixed Iρ→J的已读原文极限完整支付，未交换不统一误差。

由source degree与Σn=m²D²/2+O(D)，判据确为
m²λ≤mJ+2κ，费用upper2κ/m²成立。它是重作filtered slopes，不是把旧LCM theorem改名，亦不要求原balanced tensor支持保持。

第二lemma的精确式也通过：同一Q flag/普通Z target下，各graded index为s_n，递归exact sequence给∏s_n=[L:Γ]；hp减少v_p(s_n)logp，arch不变。故
A_D=logindex+Σhfin(Γ)=Σhfin(L)=−log|det T_actual-jumps|。
适配primitive Z基的unimodular变换与triangular leading matrix完整说明最后一步；nonstandard flags、skipped jumps、D-dependent Γ均不破坏它。

范围结论准确：45/4仅安全upper，5/2未优于7/3；raw enlargement改善可证明upper，不改变该exact invariant。单BC、r=1的a<3logC*门槛没有扩大到convexity、多图、其他metric或新target。全尺度pivot费用、同对象strict energy和新数值目标仍未付，不能用有限minor/局部rank替代。

交叉审对本人稿发现的补丁另已实施：仅明确闭盘邻域图，并将source固定为原Lφ、arch使用mixed J(ρ)，避免未证明的shrunk self-energy连续衔接。被审B稿原来已经采用该正确处理。没有新增primary或数学执行。

本收据保存后实际FULL自读，最终bytes/SHA另报。

