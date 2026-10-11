# 本轮root独审：全路径障碍、非线性函数域、完整jump与新Hankel目标

日期：2026-10-06。以当前主报告§§85–93（SHA 1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c）和上一轮366份冻结数学输入为基线。旧数学producer执行/import/rerun0；本轮没有数学producer执行。本稿是项目内部纸面审阅，文件审计不代替数学证明或Lean内核认证。

## R1. 实际读稿与独立范围

root实际全文阅读本轮三个同行数学稿：

- [全word模8稿](cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md)，最终SHA a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc。
- [非线性不变量稿](cdt_odd_R0_nonlinear_projective_invariant_field_20261006.md)，最终SHA ec6ad8fedb27a1eea5fcbcdc8afed0b58a4e13cf6a393568c8274c9d16afd59b；实际完整正文N1–N12读到修改后的N26及N10a。
- [完整jump/slopes稿](cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.md)，先实际全文读候选0d4ec96a92e291a546a27cfd8b67a968ad89dcbf681411b98d06fb0566fe9a91，再实际读取终稿aeec82c8aa5a69b6e6ed8ada331ccca5846417d42c0d3a7591ac966b2f9b2d25的G3、G4及G11修订；其余论证未变，不冒称最终版又全文重读。

root自己的[混合ζ/角色Hankel稿](cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md)，SHA e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463，是作者推导，不记作root独审。quarter实际全文独审包含最终H9，另存其审阅。本稿讨论该稿的证据范围和剩余缺口，不凭自己的作者回读宣布独立验证。

## R2. 真实全word障碍通过

在真实轨道格e_j=U^jδ内逐column求和得ℓU=ℓ、ℓM₁=ℓ−8(0,1,4,11)。U、M₁及其逆都是该格的整数automorphisms；故归纳覆盖每个正负word，signed orbit的ℓ值模8为1、physical orbit为±1。这是全尺度整数证明，不是有限搜索。

实际period/cycle map等变且Pc含δline；kerN²⊂kerN³=kerℓ。于是任何γPc=P₀都会给ℓγδ=0，和上述同余矛盾。Kummer twist只改变整体sign，inverse convention也只把word换成inverse。对参考路径同时conjugate origin flag不改变结论。

primitive quotient的decomposable wedge若被even nonzero MUM-loop fixed，所张plane必须N-stable；singleJ4唯一stable2plane为kerN²。故所有transported origin branches对全部q及有限covers都不亚纯。conifold的全部branch criterion对q共同，∞已全部排除；holomorphic disk map逐puncture的有限ramification与disk small-loop生成因而使合法meromorphy自动对全部q共同。boundary regularity、所有数域embeddings和budget仍另要求。这个no-go只针对列明packet和构造。

## R3. 非线性论证通过，但保留准确field范围

N5稳定子条件MP=P、det(M|P)=1、a+Md−d∈P确实是固定实际decomposable vector的充要条件，H°维数8；实际orbit维数6而非generic9。其translation部分含P_add。

对nilpotent X，XP不稳定等价于lower symmetric block非零。已有sl₂与upper symmetric blocks，通过brackets得到全部lower Sym²，再给diagonal center和其余sp₄。由P_add非零及V的Sp₄不可约性，affine群生成是全Ga⁴⋊Sp₄。Rational ratio由两个stabilizer fixed-field处理，未误套linear evaluation kernel。

Finite roots的minimal polynomial在PV合成域中被connected H°固定，因为只能permutate有限monic factors；若local continuation固定所选root，也固定其minimal polynomial。原点fullgroup生成迫coefficients来自finite algebraic base。该结论不把algebraic root本身误认PV元素。

∞stable-plane情形的closure只有V_add⋊Q_P而非fullSp₄；fullJ5给source column不在imN，扣H内同Sp projection后产生outside-P translation，继而全V。故输出可保留homogeneous primitive periods，却失去q。这一精确分支正确。

quarter发现的未冻N26措辞已修正：常数域C本就包含每个固定q的J(q)，所以不能由N17说该固定常数不属于L_q。现稿只排除同一个q-free公式统一恢复非零斜率family；W、y₀不在L_q另由Hq作用直接证明。root实际阅读修改后的完整论证，认可这一修正。

N10a的rational-output disk共同域与rank同q由translation automorphism及逐small-loop检验成立。新ratios未自动获得finite D-finite rank或旧species；finite roots可在ordinary discriminant零点新增branching，此缺口明确保留。没有扩大为全部新period/所有非局部word/所有非代数变换的禁止定理。

## R4. 完整jump/slopes接口通过，边界修订已核

G4带cuts的Cauchy式必须保留完整jump积分。root指出仅任意rectifiable arcs不足以支持所写finite smooth exhaustion；quarter另指出cut内部仅有trace不自动给thin-cut boundary收敛。终稿补finite piecewise-C¹ embedded arcs/有限节点及bank解析延拓或明确L¹收敛，先细管后端点小圈，外圈另付L¹径向极限。α_b<1保证小圈integral趋0，ordinary poles若有则必须另付residues。修订已实际读取。

源unit ball上的完整jump operator≤C M_D exp(−σD)才给log||ev_D,n||≤logM_D+(nlogρ⁻¹−σD)^++O(1)。O(D)个独立graded位置提供正D²节省的计数正确；单个最高log取消或fixed log metric只给低阶费用，不能冒充σ>0。G8的rank-one endpoint kernel由K定义iffprojective comparison row在P(K)，是精确的必要充分条件；α₀∈K只给两vectors上的一项ratio，不能推出全row下降。

G6/G11在当前R₀模型尚未证明，也没有完整vector-valued算术holonomy theorem。此稿给的是需要补的可检验局部接口。

## R5. 正面Hankel转向的已证与未证

root新稿H2–H7把待研究ξ_s,r=ζ(s)−rζ(s−1)直接送入Q[X]矩与degree≤h的det。Fixed s,r的higher-logistic derivatives只改变positive-envelope upper bound的O(h)项；complex signed kernel不提供positivity或nonvanishing。Q系数的primitive整化存在，但其全素数费用未知。χ trace有真实Hurwitz身份及rq系数，同时明确多轮廓Vandermonde不能免费套单轮廓energy。

H9另从Lai的double-pole simultaneous approximation出发。relation aζ(s−1)+bζ(s)=c使ΣA₁=0消去较低ζ，得到完整有理U_j/V_j。Auxprimep=9m+1、n=2m及Hermite basis上，缩放form p^{s−4}给universal blocks
\[
 (s-2)!bW_{p+l}\begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix},
\]
det为−((s−2)!bW)²。H9证明固定s≥4的无穷非零子序列；不把此结果归给H4的另一个simple-pole布局。quarter已手核最终H9，正式独审另外登记。

真正剩余的是double-pole高weight布局的全素数minor/content费用和匹配解析衰减。Lai weight4的30.83、Tang weight3的283/50都不能直接继承。若费用超过收益须改布局；不以有限n数据推全n，不将该内部lemma冒称已经发表的新特殊值定理。

## R6. 文献、执行与当前轮进展

本轮正常TLS新PDF为Bost–Chambert-Loir55页、André95页、Lai25页，共175归档页；归档页数不是root实际阅读页数。BCL/André由toric读取列明30页；root实际读Lai1–7、20–23共11页。既存Singer/Bost/CDT selected阅读另列于作者receipts，不算新下载。

本轮另保存两作者repository的22份immutable README/Lean文件、116874 bytes，root全文读14份、partial1份、只归档7份；外部Lean编译/执行0，完整外部数值proof/kernel独立重验未完成。新来源收据保留版本、SHA、实际读取和这种限制。

内部纸面推导和多方独审取得实质进展：关闭旧九行全路径/非线性local填点路线，写出完整jump/slopes精确接口，建立高weight混合ζ的明确新目标与无穷非零double-pole机制。仍无新的经典奇ζ/L/Catalan数值无理性、线性无关性或Lean结论。下一轮优先计算s=5新double-pole布局的全素数费用，再判断是否有真正strict margin；χ及jump-theorem路线保留但不虚报完成。

## R7. 最终同行独审及来源metadata历史

root本轮另实际全文读取以下五份最终独审，均输出无截断：

- [模8算术独审](cdt_odd_R0_origin_orbit_mod8_arithmetic_independent_review_20261006.md)，SHA 615a30cfed0d6696fd36c3b132ae62b23fcdb867e488e58af7273dc995da9338。
- [模8几何独审](cdt_odd_R0_origin_orbit_mod8_independent_review_20261006.md)，SHA 14766f8cb92e52dd180a5668d2b7d78c0f49963580b60768c3bf9c53cd0edd7c。
- [非线性toric独审](cdt_odd_R0_nonlinear_projective_invariant_field_independent_review_20261006.md)，SHA f50624fe3f2fd10bde8aead5ef1687a2f98baa5c0ea6bc88ec185f16cd2f6926。
- [非线性与flag合并独审](cdt_odd_R0_nonlinear_flag_slopes_independent_review_20261006.md)，SHA 5c2215864e27153a0ee37398681062c148b2271d164814eedf7ad8db4916012f。
- [mixed/H9独审](cdt_odd_mixed_zeta_character_hankel_independent_review_20261006.md)，SHA dfa064d0ddf9361ae48da4fd95e7b8c7816f3d459b4ccb861a679ac53291fe79。

两份quarter最终review均已由作者全文回读冻结。Mixed独审J3自身排版曾漏一个加号，冻结前恢复，实际数学主稿e6未改；root实际读的是已经恢复的最终dfa版本。

来源指纹有一个明确的metadata-only历史，不修改已冻结review：quarter的mixed J1实际阅读时，Lai收据SHA为0b1cfbd3713c18ebb234b74079e4a95cceaa2fc83a874d74b4bbf2f3fa2d1634，polylog收据为68d48519b01704d10e8aa025fd969e7e646bdf21f3b3d405082885cfc7ac6333。root之后只给这两份自己NEW收据添加ownproof e6 fingerprint/status metadata，源码22项bytes/SHA、PDF及actual-reading范围均未变。

Current最终[Lai收据](../literature/manifest_cdt_odd_lai2026_mixed_zeta_20261006.json)SHA为9763dff18ed5b23001220a6081e158570aeff766075177082acd35f2f7a50609；[polylog收据](../literature/manifest_cdt_odd_2026_polylog_primary_sources_20261006.json)SHA为8c82166ffd46ada438f5726bf34cb575a3edef49e5da3c7165f54cc7fced4c86。最终audit将核current指纹，历史review旧pin仍准确反映其实际阅读时刻，不冒记它已读root后加的metadata。

其余两份current来源收据已实际读/核：非线性b76e6d36b85f3e93c12c92cf0856a46b49a89270e304803f1d3561b5de47d17d；flag/slopes f55d8f15ce967f864cf85b5b6fa1971dc98369aada6829cbf7f9e4ceb8e060ac。数学终稿、独审、来源各自固定，不用自引用hash或旧producer重跑代替证明。本NEW综合审阅到此冻结只读，后续只修改mutable main/audit。
