# R₀：positive-cut 的真实 open regulator 类与 compact trace 的剩余界面

日期：2026-10-06。NEW 全尺度纸面证明。旧数学 MD/PY/JSON/manifest 与同行 producer 全部只读；没有执行、导入或修改其中任何文件。先实际读主报告 §§68–72、delivery 的全部 R₀ 新状态和冻结 positive-cut 稿，再推导这里的新接口。本文不把 ordinary open cohomology 与未经 compact-support 校准的积分泛函混同。

## 1. 对象、范围与新结论

使用冻结的 smooth proper toric family \(f:Y\to\mathbf G_m\)，smooth 四维 total space \(Y\)、horizontal SNC boundary \(E\)、open \(Y^*=Y\setminus E\)，以及唯一存在的
\[
 \Xi\in CH^4(Y,4)_{\mathbf Q},\qquad
 \Xi|_{Y^*}=\xi=\{v_0,v_1,v_2,v_3\}.
\]
令 \(\phi=\prod_{j=0}^3(v_j+2+v_j^{-1})\)，\(\Omega=d\log v_0\wedge\cdots\wedge d\log v_3\)。取 sufficiently small simply connected disk \(D\) 围绕 \(0<\lambda_0<256\)，满足
\[
 D\subset\mathbf C^*,\qquad \sup_{\lambda\in D}|\lambda|<256.
 \tag{C1}
\]
在此 disk 中 \(Y_D\to D\) 是 smooth proper family，所有 surviving boundary strata 亦 smooth。记 \(U_\lambda=Y_\lambda^*\)、\(X_\lambda=Y_\lambda\)、\(j_\lambda:U_\lambda\hookrightarrow X_\lambda\)。固定 LEFT residue 和 \(x=\lambda/256\) 的实际 square-root branch。

本稿的新正结论是：

1. 正实切割 current \(R_4^+\) 在每个 \(U_\lambda\) 上真正代表 \(\xi_\lambda\) 的 Deligne regulator：
\[
 \boxed{
 j_\lambda^*AJ(\Xi_\lambda)
 =[R_4^+|_{U_\lambda}]
 \quad\text{in }H^3(U_\lambda,\mathbf C)/H^3(U_\lambda,\mathbf Q(4)).
 }
 \tag{C2}
\]
证明用 intrinsic unit Deligne triples 的 exterior product，再利用实际 positive-cut transversality 拉回；不宣称 compact raw graph 已满足 cubical multi-face admissibility。
2. 对冻结 compact derivative 稿构造的 actual lift \(R_\lambda=[S|_{X_\lambda}]\)，存在 flat rational **open** class \(a_\lambda\in H^3(U_\lambda,\mathbf Q)\)，使
\[
 \boxed{
 j_\lambda^*R_\lambda-[R_4^+|_{U_\lambda}]
 =(2\pi i)^4a_\lambda
 \quad\text{in ordinary }H^3(U_\lambda,\mathbf C).
 }
 \tag{C3}
\]
Flat 来自 total-space closed current。
3. 对 \(0<x<1\) 的冻结 absolutely convergent raw scalar \(\nu_{\rm cut}=\int_{U_x}R_4^+\wedge\omega_x\)，有精确 remaining-comparison：
\[
 \boxed{
 \nu_{\rm compact}-\nu_{\rm cut}
 =(2\pi i)^4\langle a_x,\omega_{{\rm rel},x}\rangle+B_x .
 }
 \tag{C4}
\]
\(\omega_{\rm rel}\in H^3(X_x,E_x;\mathbf C)\simeq H_c^3(U_x,\mathbf C)\) 是实际 \((\omega_x,0)\) relative class；\(B_x\) 是 §6 定义的 boundary flux。第一项是 rational **relative** Tate period，未证明来自 closed compact cycle；第二项未证明为零。

C2/C3 补上 actual open regulator class 的识别，C4 精确限定剩余 functional comparison。本文不宣称 \(\nu_{\rm compact}=\nu_{\rm cut}\)，不宣称其差已是四个 rational compact periods 的组合，也没有新的数值无理性。

## 2. Positive partial cuts 的实际横截性

在 \((\mathbf C^*)^4\) 上以 \(v_i=a_i+ib_i\) 写
\[
 T_i^+=\{b_i=0,\ a_i>0\},\qquad
 \delta_{T_i^+}=\delta(b_i)\,db_i.
\]
在 total open \(Y_D^*=\phi^{-1}(D)\) 中，coordinate-cut normals独立。还须核所有 fibre pullbacks，而不只核 full \(T_4\)。

四个 coordinates若全部 positive，各 \(v_i+2+v_i^{-1}\ge4\)，故 \(\phi\ge256\)。C1 给
\[
 T_0^+\cap T_1^+\cap T_2^+\cap T_3^+\cap U_\lambda=\varnothing .
 \tag{C5}
\]
对 proper subset \(I\subsetneq\{0,1,2,3\}\)，在 partial positive cut 上若某个 free coordinate \(v_j\), \(j\notin I\)，有 \(\partial\phi/\partial v_j\ne0\)，则该 free complex direction使 fibre normal与cut normals独立，得到 transverse pullback。

如果所有 free-coordinate derivatives都为零，由 \(\phi\ne0\) 得 free \(v_j=\pm1\)；\(v_j=-1\) 会令 \(\phi=0\)，故全为1。Cut coordinates positive，于是仍有 \(\phi\ge256\)，与 C1 矛盾。因此所有 nonempty partial positive cuts 与fibre均 transverse，real codimension准确为 \(|I|\)。

小相位邻域内也有实际稳定性：对 \(v=re^{i\alpha}\)，
\[
 |v+2+v^{-1}|=2(\cosh(\log r)+\cos\alpha)
 \ge4\cos^2(\alpha/2).
\]
取 \(\epsilon>0\) 使 \(256\cos^8(\epsilon/2)>\sup_D|\lambda|\)。在 \(|\alpha_i|<\epsilon\) 的 full cuts上仍不可能有 \(\phi=\lambda\)；proper partial-cut free derivatives全零也与同一 lower bound矛盾。因此可以对正 cuts作该邻域内的实际 regularization/prescribed-fibre pullback。这不是扩大 Li 的小扰动定理到所有相位。

## 3. Intrinsic unit phase homotopy 与四重乘积

先在单个 \(\mathbf C^*\) 上工作。令 \(L^-\) 是 principal log，\(\operatorname{Arg}\in(-\pi,\pi)\)；\(L^+\) 是 \(\operatorname{Arg}\in(0,2\pi)\)。Locally integrable functions满足
\[
 L^+-L^-=2\pi i\,\chi_-,\qquad
 \chi_-=\mathbf 1_{\{\operatorname{Im}v<0\}} .
 \tag{C6}
\]
Oriented cut currents满足
\[
 dL^\pm=d\log v-2\pi i\,\delta_{T^\pm},\qquad
 d\chi_-=\delta_{T^-}-\delta_{T^+}.
 \tag{C7}
\]
Negative ray在 \(a<0\) 的 normal current为 \(-\delta(b)db\)，positive ray为 \(+\delta(b)db\)；这与 C6 分布导数一致。

在 cohomological current cone写
\[
 D(A,B,C)=(-dA,-dB,dC-B+A).
\]
Unit triples为 \(\mathcal U^\pm=(2\pi i\,\delta_{T^\pm},d\log v,L^\pm)\)。令 \(\mathcal H=(2\pi i\,\chi_-,0,0)\)，直接得
\[
 \boxed{D\mathcal H=\mathcal U^+-\mathcal U^-.}
 \tag{C8}
\]
这是 integral-multiplicity angular-sector chain，尚未用 rational moving。它与 Li PDF8 的 sector identity同型；这里直接核分布公式，不把其 Theorem6.1 的小-\(\epsilon\) 条件扩大。

在 \((\mathbf C^*)^4\) 上，各 unit是不同坐标的 exterior pullback，products和Leibniz rule定义良好。采用 Deligne product
\[
 (A,B,C)\cup(A',B',C')
 =(A\wedge A',B\wedge B',
 C\wedge B'+(-1)^{\deg A}A\wedge C').
\]
四重 positive product的 third component恰为
\[
\begin{aligned}
 R_4^+={}&L_0^+d\log v_1\wedge d\log v_2\wedge d\log v_3\\
 &-2\pi i\,\delta_{T_0^+}L_1^+d\log v_2\wedge d\log v_3\\
 &+(2\pi i)^2\delta_{T_0^+}\wedge\delta_{T_1^+}L_2^+d\log v_3\\
 &-(2\pi i)^3\delta_{T_0^+}\wedge\delta_{T_1^+}
                 \wedge\delta_{T_2^+}L_3^+ .
\end{aligned}
 \tag{C9}
\]
Delta factors在前的符号与冻结 positive-cut 积分相同。

Telescoping homotopy
\[
 \mathcal H_4=\sum_{j=0}^3(-1)^j
 \mathcal U_0^+\cup\cdots\cup\mathcal U_{j-1}^+
 \cup\mathcal H_j\cup
 \mathcal U_{j+1}^-\cup\cdots\cup\mathcal U_3^-
\]
给全尺度 identity
\[
 D\mathcal H_4=
 \mathcal U_0^+\cup\cdots\cup\mathcal U_3^+
 -\mathcal U_0^-\cup\cdots\cup\mathcal U_3^- .
 \tag{C10}
\]
Coordinates不同，所以这是合法 universal exterior product，没有 face terms。Principal unit triple代表对应unit的 Deligne class；C8/C10证明 positive product代表同一个 four-unit regulator。

这里区分 intrinsic unit与literal cubical graph：positive ray经过被cubical coordinates删除的值1，不能未经说明就把其chains认作原negative-cut Bloch complex的chains。我们在整个 \(\mathbf C^*\) 上用unit cone和regulator ring homomorphism。Unit在值1的Deligne class为零；C8在此没有新 divisor。

## 4. 实际 fibre/total open regulator 的识别

Regular units \(v_i:U_\lambda\to\mathbf C^*\) 的 motivic cup product就是指定 \(\xi_\lambda\)。KLM regulator是 ring homomorphism并与restriction/pullback相容。先在universal torus证明C10，再取cohomological pullback，不要求homotopy中所有negative cuts在本fibre有transverse representative。

Positive representative自身的全部cut strata已由§2实际证明transverse。Normal/intersection current model的pullback因此给exactly C9，而不是未知derived representative；这与KLII PDF59 prescribed-pullback interface相容。C5使first component为空，second component是holomorphic4-form的fibre restriction、因dimension3为零，third component是closed \(R_4^+|_{U_\lambda}\)。

因为 fibre dimension3、\(p=n=4\)，\(F^4\) terms均不进入相关Deligne complex。KLM PDF17 §5.9(iv)给
\[
 H_D^4(U_\lambda,\mathbf Q(4))
 \simeq H^3(U_\lambda,\mathbf C)/H^3(U_\lambda,\mathbf Q(4)),
\]
且可在open直接用 \(R\)。真正Chow restriction \(\Xi|_{Y^*}=\xi\) 与AJ functoriality于是给C2。

同理 analytic total open \(Y_D^*\) 上，positive product代表 restricted \(AJ(\Xi)\)，triple为
\[
 (0,\Omega,R_4^+),\qquad dR_4^+=\Omega .
 \tag{C11}
\]
指定 \(\Xi\) 已由真实higher-Chow theorem存在；这里识别的是它的实际restriction，并非把任意open类当作另一个候选completion。

## 5. Flat rational open Tate discrepancy

冻结compact derivative稿在 \(Y_D\) 给smooth three-form \(S\)，\(dS=\Omega_Y\)，其fibre classes是真正AJ lifts；membrane已在该证明中处理。Deligne representative为 \((0,\Omega_Y,S)\)。限制到 \(Y_D^*\) 后，与C11代表同一个total Deligne class。

因此
\[
 (0,0,S-R_4^+)=D(A,B,K).
\]
这里 \(B\in F^4D^3(Y_D^*)=0\)，first component给 \(dA=0\)，third component给
\[
 S-R_4^+=A+dK,\qquad
 [A]\in H^3(Y_D^*,\mathbf Q(4)).
 \tag{C12}
\]
这直接给 rational ordinary total class，不只是从每个fibre的quotient equality猜测。

Smooth proper pair \((Y_D,E_D)\to D\) 各strata submersive，可选保护boundary的局部horizontal trivialization。Total closed class的fibre restrictions因而flat；直接Cartan也给同样结论，因为 \(d(S-R_4^+)=0\)，Lie derivative限制只剩exact项。设 \(a_\lambda=(2\pi i)^{-4}[A|_{U_\lambda}]\)，即得C3。更换compact lift只改变 \(j^*\) 的flat rational compact Tate class。

尚未证明 \(a_\lambda\in j^*H^3(X_\lambda,\mathbf Q)\)。Poincaré–Lefschetz duality给
\[
 H^3(U_\lambda,\mathbf Q)\simeq H_3(X_\lambda,E_\lambda;\mathbf Q).
\]
记 \(A_\lambda^{\rm rel}\) 为 \(a_\lambda\) 对应的 rational relative three-cycle。Long exact sequence给
\[
 \boxed{
 a_\lambda\in j^*H^3(X_\lambda,\mathbf Q)
 \Longleftrightarrow \partial A_\lambda^{\rm rel}=0
 \quad\text{in }H_2(E_\lambda,\mathbf Q).
 }
 \tag{C13}
\]
因此C3缩小的是flat rational OPEN ambiguity；还没有证明该relative boundary为零。

## 6. Compact-support trace 与 boundary flux

冻结derivative theorem的compact \(H^3\to\)open \(H^3\) rational injection经duality给 \(H_c^3(U_\lambda,\mathbf Q)\to H^3(X_\lambda,\mathbf Q)\) surjective。实际holomorphic three-form \(\omega_\lambda\) 在每个boundary surface与更低intersection上restriction为零。SNC simplicial de Rham model中
\[
 \omega_{{\rm rel},\lambda}:=(\omega_\lambda,0)
 \in H^3(X_\lambda,E_\lambda;\mathbf C)\simeq H_c^3(U_\lambda,\mathbf C)
 \tag{C14}
\]
是一个明确relative lift。我们采用这一actual class，不任选支持lift。

取compactly supported smooth closed \(\omega_c\) 代表C14。其compact-cohomological image是 \([\omega_\lambda]\)，所以在compact \(X_\lambda\) 有一个smooth two-form \(\beta\)，使
\[
 \omega_\lambda-\omega_c=d\beta .
 \tag{C15}
\]
这只是ordinary de Rham exactness，未要求 \(\beta\) holomorphic、boundary值为零或具有未经证明的growth。Near boundary \(\omega_c=0\)，故 \(d\beta=\omega_\lambda\)。这种global primitive避免了从SNC neighbourhood deformation retract跳步宣称一个特定holomorphic collar primitive存在。

Canonical open-class trace
\[
 \nu_c^+:=\langle [R_4^+],\omega_{\rm rel}\rangle
 =\int_{U_\lambda}R_4^+\wedge\omega_c
 \tag{C16}
\]
确实只依赖ordinary class。Projection formula与C3给
\[
 \nu_{\rm compact}-\nu_c^+
 =(2\pi i)^4\langle a_\lambda,\omega_{\rm rel}\rangle
 =(2\pi i)^4\int_{A_\lambda^{\rm rel}}\omega_\lambda .
 \tag{C17}
\]
这是rational relative Tate-period statement。若C13 boundary为零，才可改成 rational closed compact period；actual rational projector随后才把其scalar contribution放入rank4 sector。

对 \(0<x<1\)，冻结positive-cut theorem已证明raw pairing逐sheet绝对收敛。取smooth compact exhaustion \(M_\epsilon\Subset U_x\)，boundaries横截有限个smooth positive-cut strata（可选其restrictions的common regular values）。Normal-current Stokes合法。由degree3，
\[
 \int_{M_\epsilon}R_4^+\wedge d\beta
 =-\int_{\partial M_\epsilon}R_4^+\wedge\beta .
\]
定义
\[
 B_x:=\lim_{\epsilon\to0}
      \int_{\partial M_\epsilon}R_4^+\wedge\beta .
 \tag{C18}
\]
Limit存在：左边是已收敛raw integral减compactly supported integral。于是
\[
 \boxed{\nu_{\rm cut}-\nu_c^+=-B_x,}
 \tag{C19}
\]
并由C17得到C4。由于C14固定，该flux不取决于为C15选择的smooth primitive；若primitive改变closed two-form，Stokes给对应boundary项恒为零。

剩余至少是实际求 \(\partial A^{\rm rel}\) 与实际证明/计算 \(B\)。另证 \(\partial A^{\rm rel}=0\) 且 \(B=0\) 时，才能说compact-minus-raw scalar是rational compact Tate periods；仅证 \(B=0\) 得到的仍可能是rational relative periods。

## 7. 为什么绝对收敛和 ordinary class equality 不足

这是一个逻辑检验，不是对本例flux的反例断言。取compact elliptic curve \(X\)、point \(p\)、\(U=X\setminus\{p\}\)、local coordinate \(z\)，以及global holomorphic one-form
\[
 \omega=f(z)\,dz,\qquad f(0)\ne0 .
\]
令 \(\chi\) supported在coordinate disk且near \(p\)为1，\(F=\chi/z\) 在 \(U\) smooth。Current \(\alpha=dF\) 在ordinary \(H^1(U,\mathbf C)\)中exact。

Near \(p\)，\(\alpha=-dz/z^2\)，所以 \(\alpha\wedge\omega=0\)；实际wedge只支撑在cutoff annulus，raw integral绝对收敛。删去 \(|z|<\epsilon\)，Stokes与inner clockwise orientation给
\[
 \int_U\alpha\wedge\omega
 =\lim_{\epsilon\to0}\int_{\partial(X\setminus\{|z|<\epsilon\})}F\omega
 =-2\pi i f(0)\ne0 .
 \tag{C20}
\]
但任意compactly supported closed \(\omega_c\) 都有 \(\int_UdF\wedge\omega_c=0\)。

所以“ordinary类相同”和“raw wedge积分绝对收敛”仍不自动给raw积分cohomological invariance。需actual boundary-growth/flux theorem；C18准确定位此缺口。这不宣称本项目logarithmic current有nonzero flux。

## 8. 局部 vanishing normalization 与研究边界

在 \(v\approx1\) 的principal-cut-free neighbourhood，unit product的third component为
\[
 R_{\rm loc}=\log v_0\,d\log v_1\wedge d\log v_2\wedge d\log v_3.
\]
它代表specified symbol的局部Deligne restriction，评价actual vanishing sphere只差 \((2\pi i)^4\mathbf Q\) 常数；这不需要compact raw graph的multi-face验证。塌缩real four-ball的Stokes可选择零极限标记。一项局部normalization不消除其它compact homogeneous coefficients，也不代替C4的global functional comparison。

本轮打通：positive intrinsic unit product的actual Deligne类 → 指定 \(\Xi\) 的open restriction → total closed difference的flat rational open Tate class。此前仅由forcing吻合给未知complex homogeneous discrepancy；现在class层面多了rational open Betti约束，functional升级还需C13/C18。

直接下一任务是本例monomial boundary charts中 \(R_4^+\) 与C15的 \(\beta\) 的actual pairing bounds，或real-oriented blow-up上的compatible relative current模型，计算boundary flux与relative boundary class。Boundary components rational和direct boundary pushforward的type pairing为零，都不替代这两项。

## 9. 实际来源与执行记录

实际来源页、版本、SHA与NEW稿pin见[新receipt](../literature/manifest_cdt_odd_R0_compact_positive_cut_class_20261006.json)。本次实际primary reads：

* KLM published PDF7–12、17：unit triple/Prop4.2、ring product、current cone、quasiprojective \(p=n>m\) 的direct \(R\) interface；7/17本次另完整回读，前序任务也实际逐页读过其它页。
* Li2018 published PDF8–10：sector cochain、exterior-product telescoping；PDF4–7本次背景读。只用具体cone identities，不将Theorem6.1的small-\(\epsilon\)条件扩大。
* KLII fixed arXiv v1 PDF59：intersection-current pullback与prescribed fibre；PDF50–54/57–59前序实际完整页读，59本次另完整回读。
* Deligne HodgeIII PDF35–41前序实际完整页读；本稿C13/C14明确采用relative long exact sequence、Poincaré–Lefschetz与SNC relative de Rham，不从OCR上下标推full-open rank或integral saturation。

本次没有新增PDF。Python fitz仅抽取primary页与读取元数据；旧/同行数学producer执行/import数0，没有PSLQ、Lean或数值无理性claim。第一次保存patch因一行缺少add-file前缀而被工具拒绝，未改变任何文件；随后使用自动逐行前缀保存NEW稿。本文当前不冒认同行已审。后续独审重点是intrinsic unit/cube值1的区别、derived-to-actual transverse pullback、C12 rational total class以及relative trace和boundary符号。

