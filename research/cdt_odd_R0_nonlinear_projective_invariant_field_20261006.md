# R₀ 的非线性与射影函数域：实际稳定子、全部原点分支及奇点分类

日期：2026-10-06。NEW 全尺度纸面证明。本轮权威主报告 SHA256 为 1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c，实际读取 §§85–93；delivery SHA 为 720729da5652eddff514b331c177b1fde7749af4fa38ce3e9cf65d60708b66a3，基线366份冻结数学输入。旧/同行数学文件及 receipts 只读；数学 producer 执行、import、重跑均为0，本稿没有数学 producer。

本稿将旧九行线性 no-go 真正推进到其**有理微分函数域及有限代数操作**。不能用线性 evaluation kernel 直接证明 ratio 的结论；这里另算实际 decomposable vector 的稳定子，并证明它与局部单值变换生成的群。结果是：原点任何实际 transported branch 上，可亚纯的这类输出只能来自有限代数基底；同一无外加目标系数的有理公式必对所有 q 同值。Conifold 不产生 q 特有的亚纯条件；无穷远可亚纯输出亦对 q 盲。这里没有把它扩大成“全部新周期、全部非线性分析或任意非局部word”的 no-go。

## N1. 实际对象、函数域与“同一个公式”的含义

采用冻结 [exterior 稿](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md) E1–E6：
\[
 P=\theta^4-x(\theta+\tfrac12)^4,\quad t=1-x,\quad
 \Phi(q)=Y_{h+qg_0}\wedge Y_{g_1}\wedge Y_{g_2},\quad
 q_{\rm actual}=\alpha_0=\pi^2(R_0-M_0)/16 .
 \tag{N1}
\]
使用E7a的四个Z行与五个mixed行，记九行向量 \(F(q)\)。原minor与它由可逆 \(\mathbf C(x)\) gauge联系；它们生成同一个微分函数域。实际含1的线性秩是10。有限阶导数不增函数域，因为九行connection有理。

令 \(k=\mathbf C(x)\)，\(\mathcal E/k\) 是实际rank-five方程的Picard–Vessiot(PV)域，不是把全部九行误认为一个PV基本矩阵。其群及表示为
\[
 G=\mathbf G_a^4\rtimes(\operatorname{Sp}(V)\times\mu_2),\quad
 G^\circ=\mathbf G_a^4\rtimes\operatorname{Sp}(V),\quad\dim V=4,
\]
\[
 0\longrightarrow\wedge^3V\longrightarrow\mathcal W
 \longrightarrow\chi\wedge^2_0V\longrightarrow0,\quad \dim\mathcal W=9.
 \tag{N2}
\]
实际full translation radical与Sp4是冻结E4–E5的输入；regular singular使monodromy closure等于PV群。一个complex Levi splitting只用于群论，不是算术gauge。

令 \(\mathcal L_q=k(F(q))\subset\mathcal E\)。本稿的有理操作是
\[
 f_q=R(x,F(q),\theta F(q),\ldots),\qquad R\text{ 固定且不另外输入 }q.
 \tag{N3}
\]
其系数可在一个固定有限代数扩张 \(k'/k\) 中；它们须被所用PV群固定。允许coefficients为任意固定complex constants，但不能把未知目标q直接写成一个外加coefficient，然后称“提取了q”。“对q盲”指同一个公式所给的整个函数 \(f_q\) 对全部q精确相同，不只是导数相同或局部阶数相同。

本轮实际全文读 [NEW模8稿](cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md)，最终SHA a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc；它证明全部实际路径的 \(\gamma P_c\ne\ker N_0^2\)，不假定 \(P_c=\langle g_1,g_2\rangle\) 已有有理Betti坐标。本稿§N7明确调用这项新输入。

## N2. 实际轨道不是一般九空间；其稳定子恰八维

在上述Levi splitting写 \(E=V\oplus\mathbf Ce\)。每个actual solution vector形如
\[
 w=(e+d)\wedge p,\quad p=b_1\wedge b_2\ne0,\quad
 P_c=\langle b_1,b_2\rangle\text{ Lagrangian}.
 \tag{N4}
\]
一般transported branch把 \(P_c\) 换成 \(P_\gamma\)，仍有此形式。\(G^\circ\) 中 \((a,M)\) 在E上作用为 \(e\mapsto e+a,\ z\mapsto Mz\)。因而 \(w\) 的connected稳定子条件准确为
\[
 MP=P,\quad\det(M|_P)=1,\quad a+Md-d\in P.
 \tag{N5}
\]
对d作一次constant translation conjugation后，得到
\[
 H_P=P_{\rm add}\rtimes Q_P,\qquad
 Q_P=\{M\in\operatorname{Sp}(V):MP=P,\ \det(M|_P)=1\}.
 \tag{N6}
\]
取symplectic basis \(V=P\oplus P^*\)，
\[
 \operatorname{Lie}Q_P=
 \left\{\begin{pmatrix}A&B\\0&-A^T\end{pmatrix}:
          \operatorname{tr}A=0,\ B=B^T\right\}.
 \tag{N7}
\]
群本身为 \(\operatorname{SL}_2\ltimes\operatorname{Sym}^2P\)，连通、维数6。因此actual \(H_q^\circ\) 连通、维数8；轨道维数 \(14-8=6\)。特别它不是九空间上的generic orbit。Translation部分始终含完整二维 \(P_{\rm add}\)，并不随d改变。

PV基本矩阵可逆使“固定全部九行函数”等价于“固定w”。PV对应故给
\[
 \mathcal L_q=\mathcal E^{H_q},
 \tag{N8}
\]
其中 \(H_q\) 是完整G稳定子。此式不是声称 \(\mathcal L_q/k\) 本身PV；\(H_q\)一般非normal。

完整 \(H_q\) 还有一个 \(\chi=-1\) component：选 \(MP=P,\det(M|P)=-1\)，再选a使 \(-e+Md+a\) 与 \(-e-d\) modulo P相同，就固定w。于是
\[
 \mathcal L_q^{G^\circ}
 =\mathcal L_q\cap\mathcal E^{G^\circ}=k.
 \tag{N9}
\]
理由是 \(\mathcal E^{G^\circ}=k(\sqrt x)\)：component quotient恰\(\mu_2\)，而\(\sqrt x\)已在PV域内；上述H的negative component不固定它。有限base extension后，若sqrt已进入base则PV群连通，否则相同component论证仍适用。

## N3. 完整ambient invariant field与actual null orbit

在constant splitting把 \(\mathcal W\) 写为 \(\wedge^3V\oplus\wedge^2_0V\)，坐标记 \((b,p)\)。translation作用为
\[
 (b,p)\longmapsto(b+a\wedge p,p).
 \tag{N10}
\]
令 \({\rm vol}\) 为symplectic volume，定义非退化quadratic form
\[
 p\wedge p=Q(p)\,{\rm vol}.
 \tag{N11}
\]
若 \(Q(p)\ne0\)，线性映射 \(a\mapsto a\wedge p:V\to\wedge^3V\) 可逆：将nondegenerate bivector化成 \(u_1\wedge u_2+u_3\wedge u_4\) 即逐basis验证。所以一个generic rational translation invariant与b无关。

Sp4在primitive五空间的像为SO5。给出所需elementary验证：它保持N11；Lie作用的kernel若杀primitive \(\wedge^2_0V\)，也杀trivial symplectic bivector，因而杀全部\(\wedge^2V\)。逐basis检查 \(\wedge^2\) 的Lie作用在 \(\mathfrak{gl}_4\) 上kernel为0。故10维 \(\mathfrak{sp}_4\) 注入同为10维的 \(\mathfrak{so}_5\)，connected像为全部SO5。SO5在每个非零Q-level上传递，含determinant1的Witt isometry；在一条nonisotropicline上的r与−r亦共轭。因此rational invariant在这条line上是r²的rational function，得到
\[
 \boxed{\mathbf C(\mathcal W)^{G^\circ}
       =\mathbf C(Q),\qquad
       \mathbf C[\mathcal W]^{G^\circ}=\mathbf C[Q].}
 \tag{N12}
\]
Polynomial版本也由同一line上的even polynomial及 \(Q\ne0\) 的dense open成立。完整\(\mu_2\)只是p的符号，不改变Q，因此G的两种invariant field/ring相同。

然而actual \(\Phi(q)\) 的p是decomposable，**Q(p)=0**。其b又属于二维image \(V\wedge p\)。在这类非零p上，Sp4对oriented Lagrangian bivectors传递，translations对b的完整二维fibre传递。因此actual orbit
\[
 \mathcal O=\{(b,p):p\ne0,\ Q(p)=0,\ b\in V\wedge p\}
 \quad\text{为单个六维 }G^\circ\text{ orbit},\qquad
 \boxed{\mathbf C(\mathcal O)^{G^\circ}=\mathbf C.}
 \tag{N13}
\]
这解释了常见quadratic invariant的失败：唯一ambient invariant Q在actual数据上恒零，不能检测α0。Q=0上的0/0不能视为一个已定义有理输出；若在actual function field有合法rational extension，仍由N13分类。相同vector的finite tensor、symmetric/exterior powers及rational contractions的coordinate都是原 \(\mathcal L_q\) 元素，不因此产生独立period。

## N4. 群生成lemma：SL2稳定子加一个不稳定plane的nilpotent足够

**Lemma。** 在Sp4中，令Q_P为N6，X为nilpotent且 \(XP\not\subset P\)。则Q_P与 \(\exp(sX)\) 生成群的Zariski closure是Sp4。

证明：相对于 \(P\oplus P^*\)，
\[
 X=\begin{pmatrix}A&B\\C&-A^T\end{pmatrix},\quad B=B^T,\ C=C^T,
 \qquad XP\not\subset P\iff C\ne0.
 \tag{N14}
\]
从Lie algebra中减去N7已有的upper B与traceless A，留下 \(cZ+C_{\rm lower}\)，\(Z=\operatorname{diag}(I_2,-I_2)\)。在block-diagonal \(\mathfrak{sl}_2\) 的adjoint作用下，Z是trivial，lower symmetric C是不可约三维 \(\operatorname{Sym}^2P^*\)。对 \(cZ+C_{\rm lower}\) 作这些brackets及其线性span，得到完整pure lower三空间（非平凡不可约模上的 \(\mathfrak{sl}_2\)-span为全模）。与已有upper symmetric B的brackets给diag(BC,−CB)。取B=C=I即得到Z，其他BC连同已有sl2给全部diagonal四空间。至此upper3、diagonal4、lower3齐全，Lie algebra为sp4。Sp4连通，lemma成立。

**Affine结论。** 令u为 \(G^\circ\) 的unipotent元素，其Sp projection为 \(\exp X\)，且 \(XP\not\subset P\)。则
\[
 \boxed{\overline{\langle H_q^\circ,u\rangle}^{\,{\rm Zar}}=G^\circ.}
 \tag{N15}
\]
循环unipotent powers的closure含完整one-parameter subgroup，因而其Lie投影含X。Lemma给满Sp4投影；该closure与translation V的交集是Sp4-stable linear subspace，已含 \(P_{\rm add}\ne0\)。标准V不可约，交集必为全V，遂得N15。此论证与d的constant conjugation、u可能有affine source column无关。

## N5. Rational函数的真正local criterion与q同值

在有限algebraic cover的base \(k'\) 上，可先加入sqrt(x)。PV合成域的connected群仍是 \(G^\circ\)：有限base extension不能改变identity component。若一个fixed rational expression f属于 \(k'(F(q))\) 且某个transported endpoint branch在更深finite local cover上meromorphic，局部monodromy的某个even正power u便固定f。同时f被 \(H_q^\circ\) 固定。若该endpoint满足N15，则f被全部 \(G^\circ\) 固定。

因此f属于finite algebraic base；未先加入sqrt时，§N2 negative component进一步给
\[
 \boxed{f\in k'.}
 \tag{N16}
\]
这是fixed-field证明，不把rational ratio误作linear row。它不依赖f是否D-finite、也不依赖任何denominator estimate。

更关键的是同一formula的参数结论。一个translation \(a=(q'-q)g_0\) 将actual vector \(\Phi(q)\) 送到 \(\Phi(q')\)，固定g1、g2、source及base coefficients。Transported branch上使用对应 \(\gamma g_0\)。若N15成立，f已被这个translation固定，故
\[
 \boxed{R(x,F(q'))=R(x,F(q))\quad\text{每个 }q'\in\mathbf C.}
 \tag{N17}
\]
分母在q处为非零PV元素时，其translation像在每个q'仍非零，不存在把identically-zero denominator解释成另一个参数的函数。输出可为一个nonconstant algebraic function of x，但其中没有从q提取的信息；若R原已输入q，N17的hypothesis不成立。

## N6. 有限代数操作：minimal polynomial只给finite base branches

不能直接将一个algebraic root冒认PV元素。令z由有限次algebraic operations从 \(k'(F(q))\) 构成；等价地z对该field algebraic。在PV合成域 \(\mathcal E'\) 上，令
\[
 m_z(T)=T^d+c_{d-1}T^{d-1}+\cdots+c_0\in\mathcal E'[T]
 \tag{N18}
\]
为其monic minimal polynomial。

每个c_j被 \(H_q^\circ\) 固定。证明：z满足一个coefficients在 \(k'(F(q))\) 的polynomial P(T)；H固定P。m_z是P在 \(\mathcal E'[T]\) 中的monic irreducible factor，H只能将它送往有限个这样的factors。一个connected algebraic group对这有限set的动作必trivial：coefficient的rational orbit map像有限，故在dense open恒定，再由group law全体恒定。于是H固定m_z，而没有要求H先固定所选root。

若z在该endpoint经过有限cover为meromorphic，analytic continuation给一个固定z的local automorphism τ，其在 \(\mathcal E'\) 上restriction是某个even正power u。τ将N18送往另一个monic irreducible polynomial且仍有同一root z，故 \(\tau m_z=m_z\)，即u固定各c_j。N15使这些c_j全部属于finite algebraic base。因此
\[
 \boxed{z\text{ algebraic over }k'\ ;\
 \text{有限root操作不能产生一个新的目标敏感亚纯period函数。}}
 \tag{N19}
\]
若未kill sqrt，先取 \(k'(\sqrt x)\) 得同样“algebraic over k'”结论。这里没有声称z为rational，更没有把finite branch choice当作新增rank。

Uniform q-free algebraic constructions的准确定义是：选择同一个defining algebraic extension/germ，并以相同continuation规则比较不同q。Minimal polynomial在上述meromorphic情形的coefficients已固定translations；所能输出的finite algebraic branches因而对q独立。选定simple branch在q的connected analytic family上不变，multiple roots用irreducible separable polynomial后亦同。任意另行按q选择不同finite roots，是外加branch-selection数据；它不是连续的目标period抽取，也不由本稿提供算术/解析hypothesis。

## N7. 全部实际origin branches的nonlinear no-go

Origin的Sp投影为 \(\exp N_0\)，N0 regular nilpotent singleJ4。它唯一稳定二维plane为 \(P_0=\ker N_0^2\)。NEW模8稿用真实cycles
\[
 e_j=U^j\delta,\quad\ell=(1,1,1,1),\quad
 \ell U=\ell,\quad\ell M_1^{\pm1}\equiv\ell\pmod8
\]
证明physical words \(\ell(\gamma\delta)\equiv\pm1\pmod8\)；period map等变并计Kummer sign后，
\[
 \boxed{P_\gamma=\gamma P_c\ne P_0
        \quad\text{每个实际continuation word }\gamma.}
 \tag{N20}
\]
本轮实际全文核该稿M1–M17及实际轨道格O24–O25、real Betti的physical/signed解释；同余不是完整Sp4(Z)的不变量，不能与Zariski closure混淆。

于是 \(N_0P_\gamma\not\subset P_\gamma\)。任何有限local cover给 \(\exp(2eN_0)\)，e正整数，§N4同样成立。由N16–N19：

**定理1。** 原点任一实际transported branch上，现有九行生成的有理微分field中的meromorphic finite-cover输出，必来自所用finite algebraic base。Fixed q-free rational expression一旦有此性质，便对所有q整个函数同值。Finite algebraic operations的meromorphic输出只给base的finite algebraic branches。特别一个真正q-sensitive ratio、quadratic polynomial、projective affine coordinate或finite tensor coordinate，不能新增任何origin filled point。

Projective map只要在一个affine chart单值，其coordinates是N3的ratios；故同样成立。把multivaluedvector送往weighted projective space仍须逐chart核rational functions，并不绕过N15。一个identically-undefined chart或actual nullcone的0/0不是合法projective coordinate。

## N8. Conifold的所有非线性亚纯条件仍对q盲

Conifold投影是transvection \(T_V=I+v\otimes C(v,\cdot)\)。对Lagrangian P，
\[
 T_VP\subset P\quad\Longleftrightarrow\quad v\in P.
 \tag{N21}
\]
若v不在P，则covector在P上非零并送一vector到outside P，故N14的lower C非零；反之v在P时isotropy立即给T_V|P=I。

对每个transported \(P_\gamma\)：

- 若 \(v\notin P_\gamma\)，N15成立；meromorphic rational output只能base，并由N17对q同值。有限代数输出由N19分类。
- 若 \(v\in P_\gamma\)，冻结E20/E20.3证明完整paired九行F(q)对**每个q**在该branch holomorphic；raw jet minors虽可有apparent poles，却对全部q meromorphic。所有定义良好的fixed rational expressions因此对全部q meromorphic，允许其poles。

所以target-sensitive rational operations不能获得一个“仅actual q才亚纯”的conifold branch。这里是CDT所需**meromorphic**条件，不能将ratio的零点、pole order或holomorphic-lattice费用混为filled-meromorphic条件。代数roots在第二种情形可有有限Puiseux ramification；存在有限cover使之meromorphic也对全部q成立，所需ramification度由fixed defining polynomial有限控制。

## N9. 无穷远：full J5强制可亚纯输出失去q

冻结E21实际Stieltjes渐近证明E5在∞是 \(J_5(-1)\)。Even local power的logarithmD在E上为regular nilpotentJ5，\(D|V=N_\infty\) 为regularJ4，quotient为0。取e的source coefficient非零，
\[
 De=b,\qquad b\notin N_\infty V.
 \tag{N22}
\]
否则将e减去一个V-vector使De=0，会有J4⊕J1，矛盾。改Levi splitting只将b改变一个 \(N_\infty V\) 元素。

若 \(N_\infty P_\gamma\not\subset P_\gamma\)，§N4给full \(G^\circ\)，可亚纯输出为base、q同值。若稳定，则singleJ4使
\[
 P_\gamma=P_\infty=\ker N_\infty^2
                  \subset N_\infty V.
 \tag{N23}
\]
在把H写成N6的translation-conjugate坐标中，D减去H内具有同一Sp projection \(N_\infty\) 的Lie元素，得到pure translation \(b+N_\infty d\)。由N22它不在 \(N_\infty V\)，特别不在P∞。Generated closure的translation intersection已含P∞；该intersection为Q_P-stable，且在不可约SL2模 \(V/P_\infty\) 上像非零。因此它含全部V。准确地，
\[
 \boxed{\overline{\langle H_q^\circ,\exp(2eD)\rangle}
       =V_{\rm add}\rtimes Q_{P_\infty}.}
 \tag{N24}
\]
Projection不能超过Q，因为两项都在Q；反向已含全translations和Q。这个closure不是Sp4全群，不能错误地由fullJ5直接声称N15。

其fixed field在kill sqrt后的base为
\[
 \mathcal E'^{\,V_{\rm add}\rtimes Q_{P_\infty}}
       =k'(J_1,\ldots,J_5),
 \tag{N25}
\]
其中J是F的primitive五维mixed quotient。理由是该closed subgroup恰为J的stabilizer，且J满足closed五维rational connection，应用PV对应。J不依赖q。

**定理2。** 在任何actual transported infinity branch上，可meromorphic的rational output均固定全translation radical，所以固定formula对所有q同值。Nonstable-plane情形甚至只来自base；stable-plane情形可以留下homogeneous primitive-period functions，但完全失去q。Finite algebraic outputs的minimal-polynomial coefficients同样固定translations；选择相同finite branch时也不能连续地保留q。

## N10. 精确范围与一个真实的“新增独立period”边界

N12–N25涵盖同一个F(q)的finite tensor powers、products、ratios、algebraic gauges、fixed finite-order differential operations及finite algebraic roots，允许finite algebraic base covers。它没有涵盖：

1. 加入一个不在 \(\mathcal L_q\) 中的独立period、另一normal function或另一个marked affine column；
2. 非代数Nilsson/logarithmic gauge、Hadamard product、非代数积分变换；
3. 一个新含jump项的vector-valued local-height定理；
4. 任意非局部word所定义的scalar Riemann-surface quotient的全部global stabilizers。

第四项需特别保留：这里分类的是实际三个punctures的local cyclic monodromy及global G-invariant field。一般word g的closure \(\langle H_q,g\rangle\) 未逐个分类；不能仅由local结果宣称任何scalar map的global capacity自动共同。下面§N10a另对列明的holomorphic disk maps给disk-loop证明，范围不包括所有algebraic root的新增branchpoints。

一个真实的额外-reference例说明第一项不是空洞免责。另加入actual origin particular W和MUM period y0，令 \(d_q=h+qg_0-W\) 为homogeneous。则
\[
 \mathcal J(q)=
 C\!\left(y_0,\,
 C(d_q,g_1)g_2-C(d_q,g_2)g_1\right)
       =-\frac{2(q-\alpha_0)}{\pi^2}
 \tag{N26}
\]
为全函数常数。证明：q=α0时d为 \(-\pi^4y_0/16\) 加g1/g2项，辛交叉两项相消；q-variation由
\(c(g_0\wedge g_1\wedge g_2)=-2v\) 与 \(C(y_0,v)=1/\pi^2\) 给右边。全部homogeneous concomitants flat，所以这是真实global invariant而非toy函数。

必须区分fixed-q field membership与uniform recovery：对每个固定q，N26右边是complex constant，当然属于 \(k\subset\mathcal L_q\)。正确结论是**没有一个固定且不外加q/α0的新reference-independent有理公式 \(R(x,F(q))\)，能对全q表示这个非零斜率family**；否则它在origin meromorphic，N17迫全family同值，矛盾。

另可直接证明实际W、y0各不在 \(\mathcal L_q\)，不从上述常数family猜field membership。Hq含全部 \(P_{\rm add}\)；任一非零a∈P将W变成W+a，nonzero homogeneous scalar不能恒零，故W不被Hq固定。对于y0，Hq的Sp projection Q_P在V上的fixed subspace为0：其SL2在P和V/P上都没有fixed vector，exact sequence便排除V内fixed vector。因此非零y0亦不被Hq固定，PV对应N8给二者不在 \(\mathcal L_q\)。

这仍未给新CDTpacket：W、y0与canonical conifold g1/g2的**共同arithmetical germ**并未由单一假设α0∈Qbar提供，加入它们不能免费继承当前九行的all-place coefficients、species或rank。W和y0各自在origin有良好arithmetical normalization，不推出这一共同conifold comparison。N26只是严格指出：新增independent reference可以改变translation稳定子；它是一项target-sensitive constant relation，不能作为一个已获得新meromorphic period函数或新数值定理登记。初始未冻候选曾把uniform recovery写成fixed-q field membership，quarter独审指出后于冻结前作此明确修正。

## N10a. Rational outputs的holomorphic disk共同域；root操作的剩余边界

**定理3。** 取有限个fixed q-free rational expressions \(f_i(q)=R_i(x,F(q))\)，此处coefficients在 \(k=\mathbf C(x)\)，denominators为非零PV元素。令φ为nonconstant holomorphic disk map，target variable为t，φ(0)=0，沿canonical germs解释pullback，允许germ有finite pole。如果某个q*的全部 \(f_i(q_*)\circ\phi\) 在盘上single-valued meromorphic，则同一φ对每个q的全部outputs都有此性质。φ若只在open disk全纯，亦成立；boundary estimates仍另核。

证明：如果每个output的whole function都对q盲，结论直接来自相同函数。否则选一个target-sensitive output f。若有 \(\phi(z)=1\)，其arrival branch在origin有positive local winding；定理1迫f对全部q同值，矛盾。因此φ避免target origin。Holomorphic φ没有∞preimage；若允许meromorphic φ，其pole由定理2同样与f的sensitivity矛盾。

在每个conifold preimage \(\phi(z)=0\)，arrival planePγ若不包含v，§N8第一种情形再迫f q同值，矛盾。故每个arrival branch都有 \(v\in P_\gamma\)。§N8第二种情形使完整F(q)在这里对每个q holomorphic，且local loop固定全部F(q)。从punctured disk沿路径继续germs，其fundamental group由这些small loops生成，因此所有F(q)单值并填回preimages；然后全部R_i(F(q))是meromorphic。每个q的denominator仍非零，因为它是原nonzero PV元素的translation像。Closed-neighborhood版本conifold preimages有限，open-disk版本每个compact subdisk有限，每个loop属于某个subdisk，遂得全盘。证毕。

这是由local分类加disk topology另证的共同域，不需要逐个分类任意nonlocalword。它也涵盖选定后依赖actualq的φ：选定φ即对reference q=0可用。凡使用finite algebraic coefficients的扩充，须另列其fixed cover及pullback branch；这里不省略这项手续。

此外同一个rational construction的**实际线性微分秩**（有限或无限）对q相同：
\[
 \dim_k\langle1,\theta^j f_i(q):j\ge0\rangle
 =\dim_k\langle1,\theta^j f_i(q'):j\ge0\rangle .
 \tag{N27}
\]
Translation是fix k且commutes θ的field automorphism，直接把两侧spaces同构。此式不声称该秩等于9或10，也不声称必有限。

若一个proposed rational packet已经**分别完整核准**q与q=0的同一all-place coefficients/species预算，并具备finite actual rank及所列CDT boundary条件，则定理3使其q=0 reference强制同一个CDT不等式，不能仅通过q特有的disk-meromorphy反证。旧F的 \(\tau,\rho\) 不能免费赋给新ratios：reciprocal Taylor denominator、basepoint finite poles及G-function/D-finite条件仍须独立证明。

有限algebraic roots不在定理3范围内。即使其coefficients在ordinary points全纯，一个defining polynomial的discriminant零点也可产生**新的ordinary branchpoints**；这些零点可随q改变。N19及定理1–2只排除了它们在原三个punctures保留q的特有meromorphic收益，没有排除在新ordinary discriminant locus上的目标敏感ramification。是否能由真实α0关系使这种ramification消失，且使root具有finite D-finite rank、完整arithmetical germ与all-place费用，仍是一个具体未解决问题；本稿没有构造这样的positive packet。

## N11. 对研究路线和算术holonomy的实际后果

本轮并没有一个合法的新target-sensitive meromorphic packet，因而不报告未经证明的actual rank或免费的tensor denominator。如果一个nonlinear候选仍只在 \(\mathcal L_q\) 内，则定理1–2先排除它在origin/∞保留q的fillable收益；conifold亚纯条件也共同。无需再对这一不可能的local收益优化其费用。

一个新ratio还可能不是D-finite/G-function；即便绕开这里未分类的非局部word，它亦须另证明CDT需要的全部coefficients整模型、actual finite linear rank及所有embeddings。当前已冻结十行预算
\(\tau=329/50,\ L=K(\sqrt2),a=8\sqrt2,\rho=(7/2)\log2\)
只属于原F packet，不是任意rational ratio的自动预算。

因此具体的新研究入口是：寻找带**独立reference且所有source coefficients受控**的共模，以改变H而保留实际target identity；或建立允许nonzero jump/最高log flag的完整arithmetical local-height理论。这里“改变共模”须实付canonical Taylor/Betti comparison，不能仅改坐标名称。α0代数与R0−M0有理/代数不等价，仍不作免费Tate division。

没有新的ζ、L、Catalan或α0无理性/超越性结论，没有Lean验证。新增已证的是actual six-dimensional orbit、ambient/actual invariant fields、connected stabilizer generation、finite-root minimal-polynomial lemma及三个punctures的nonlinear精确分类。

## N12. 原件与执行范围

本轮实际阅读 [Singer作者原件](../literature/singer2009_differential_galois_lms_author_20261006.pdf) PDF1、13–14、17、20、26：Theorem1.3.9、Corollary1.3.10、Proposition1.3.20/Corollary1.3.21、Schlesinger Proposition1.3.27与regular-singular local group。82页原件 SHA c805d45ed54e0e6734b4d7f125c197364b9eccab2a7e09a8c26c3bf63cf5db96；没有声称全文82页阅读。原件既存，正常TLS来源由既存receipt固定，本轮无PDF下载。PV对应按原件引用；N4、N6及具体representation invariant计算是本文新纸面证明，不冒称原文已有R0定理。

Source URL为 https://singer.math.ncsu.edu/papers/LMSlectures.pdf ，本轮通过官方author search核对。旧exterior实际E1–E7a组合读取，E8–E13另完整补读；holonomy实际H1–H4及其余正文已读，先前组合输出预算截断登记并按段补读；NEW模8稿实际完整读取。轨道格O24–O25与real Betti physical/signed关键段本轮另回读，其余冻结输入的既有审阅范围不冒认本轮又全读。

首次Singer source text抽取在GBK stdout编码时报错，随后显式UTF-8实际读取上述全部页；失败输出不算阅读。PDF抽取与hash只读，不是数学producer。本稿全尺度推导没有有限word搜索、PSLQ、symbolic/numerical producer；旧/peer producer execution/import/rerun=0，自己NEW mathematical producer=0。同行独审另存，作者回读不记为独立审阅。来源收据另保存，精确pin最终稿与read scope。
