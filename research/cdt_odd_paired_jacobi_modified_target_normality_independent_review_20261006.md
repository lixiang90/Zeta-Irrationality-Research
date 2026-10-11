# 原 fixed-middle 临界目标、actual full-Q 单位与 modified Christoffel 独立审阅

2026-10-06，/root/toric_chow_completion。NEW 正式数学独审，全文回读后冻结只读；455旧数学输入及所有旧/同行producer严格只读，execute/import/rerun0。本审阅没有数学producer，没有修改同行稿或源。

## V1. 实际审阅对象和范围

实际完整读取 research/cdt_odd_paired_jacobi_modified_target_normality_20261006.md 的全部13sections、T1–T27及执行/来源说明，无截断，SHA c4dcee183239be55ab6c4e06d4b1abb1979657838f02a5c64104c45cc1fed9c4。实际完整静态读取同stem_verify.py SHA4f525b33ca7664912192daab4628db39a992ed9f3bea1df753bc6e3f253aa69b；实际完整读取JSON SHA b9f5285e3440101fa326a00c0303259262202aa428073374ec00727fa1d31a84，全部三个cases和所有字段。没有执行源码，也没有用保存的692 checks替代全尺度证明。

本人以前已全文读冻结09b9 K1–K26并正式审阅其local selfadjoint/Krylov/endpoint接口；本轮以这里明列的actual定义和独立代数推导复核，不重复运行旧source。

## V2. 原 λ2 与 norm-free rank-r middle update

通过。展开f±=T±RQ，middle plus coefficient为3、minus为λ−3，outer为3和−2；原λ2准确保留κ=1+χ、cross=5−χ。λ是diagnostic family，未被认作可免费选取的actualperiod参数。

L的首r列为middle Vandermonde，所以rankL=r，rankL^TDL=r，T7成立。T8只对已知−I块作Schur，符号(−1)^r准确，不要求M3可逆。T9的每个bordered determinant有(−1)^k；先在一般invertible A上验证再用polynomial identity延拓到singular A，合法。T10坐标(y=L(T,Q),z=Q)的basis determinant=(detVmid)^−1，故原det的[t^r]确实乘(detVmid)^2，不缺尺度。其kerL restriction仍是实际modified form，未冒认单位。

T11–14的Lagrange denominators全为unit。Z的divided difference含负号，diagonal是Z'=-sum vK²/(z-u)^2，故Loewner formula及detGλ=cG det(λI+K)均准确。固定λ2的目标是排除−2 eigenvalue，generic λ的degree-r leading unit不提供这个排除。

## V3. Actual four-Q source 的全尺度 full profile

通过。λ4第一factor的零等价18d−13=kp，k≡5(mod18)，首非负解d=5r+1=N；第二factor18d+82=kp要求k≡10(mod18)，首解10r−4≥N，包括r1等号。d0的负值绝对值<p，亦无负k遗漏。因此所有0≤d<N的真实raising coefficients为units。

四seed按d mod4、floor(d/4)取真实unequal profile，full evaluation matrix为Vandermonde乘unit triangular Δ4(N)。Actual QQ weights=κvR²皆为units，所以T17是准确full-N unit product。该同一finite realization的Hankel rank≤N、且具有已证N阶unit minor，故rank恰N。每sector的四source connections和θsector共同gcd1可由cyclic endpoint realization及full source span推出，无须simple spectrum。

这不是原3r QQ短profile或(r,3r)M5的单位定理；全空间非退化仍允许较短子空间isotropy，稿件保留该区别。

## V4. Dense connections、endpoint norms 与原 compound target

通过。θj(J)e0=Bj ej由三对角recurrence归纳，向左项恰被a_{j-1}bjθ_{j-1}消掉；所有Bj单位。故f_v=sum(vj/Bj)θj给整个dense connection，无未知norm分母。自伴关系v_j a_j=v_{j+1}b_{j+1}将endpoint norm准确变成v_j Bj²=v_start product a b，T20正确。

Actual E0/E4 Krylov columns经Q→RQ进入同一个J后，由这些已知endpoint coordinates展开；Q在minus channel取负。Cauchy–Binet给T22/T23，两边分别有Δ0(r)^2及[Δ0(r)Δ4(3r)]²尺度，channel multipliers3、−2、λ−3准确。Middle-minus最多r行，matrix degree≤r，而scalar最高λ^r唯一选全部middle rows，和T12的leading unit吻合。

有限域中unit diagonal和minor squares的和可以相消。稿件没有将compound formula当作未知critical sum的非零证明，也没有把局部GL基的实处费用免费移入全球解析bound。

## V5. Singular later profiles 的 finite-support Christoffel 自证

通过其明确scope。对j<m，θj的endpoint orthogonality来自θj(J)e0=Bj ej及J^i e0支持i≤j−1；θm(J)=0，所以延伸pj=z^(j−m)θm对j≥m的全部norm可为0。n≤m<p保证仅所用n!可逆。大Vandermonde乘小Vandermonde的formal tensor functional expansion中，含degree≥n的z列由上述orthogonality消失，仅低degree组给n!Dn；h(z)=product(z-x)使sign为(−1)^{nd}。这证明T24而不要求later profiles正常。

Vandermonde quotient是polynomial identity；重复根用Hasse confluent columns，不能免费除p-divisible factorial。该single-chain identity不等于原四/八source unequal compound identity，稿件正确使用T22/T23承担whole target。

## V6. 两个 χ-preserving 反例的准确含义

通过。p19/r1的实际表给Gλ=3λ+14，Mλ的右下2×2 determinant12和inverse[[14,3],[3,8]]皆准确；Schur后的det8λ+9乘12等于λ+13。故λ8 scalar singular而M8=2，λ6 matrix singular而G6=13，且λ6/8都非0、3，相应ambient forms不退化。Actualλ2仍G2=1、M2=15。

这些是同节点/χ/halfjet结构中关于逻辑推出关系的反例；它们不是原固定λ2目标反例，亦没有改变数值目标。由此严证“selfadjoint+raising+fullvisibility+endpointproper”单独不足以给原critical normality；还需固定参数的算术防相消信息。

## V7. 本人实际 primary 阅读与视觉核验

没有新增下载；使用本轮作者已归档的正常TLS原件。本人的actual阅读不是作者/根阅读的复制记账：

- Krattenthaler《Hankel determinants of linear combinations of moments of orthogonal polynomials, II》，PDF1–3、13–14，共5distinct页；SHA6ee728bafe1ac1467050df139da6e86c9395f7fb7f7c77b769d0bb5388120fff。实际PDF2 Theorem1写char0及all norms非零；PDF13–14 confluence明确ordinary derivatives/factorial。这里只核印刷scope，稿件有限域T24另自证。PDF2已render/view完整页核符号。
- Álvarez-Fernández等2015《Christoffel transformations for matrix orthogonal polynomials in the real line and the non-Abelian 2D Toda lattice hierarchy》，PDF8–9、15–16，共4distinct页；SHA082d479245929dc979f510fe5f082468de37d003623c6989c01def7c99759ded。Definition9和Proposition9要求全部leading blocks nonsingular；Theorem2实际写detΠk,N≠0，proof明确用其inverse，另分支要Πk+1,N。未以换名字方式使用这个未知hypothesis。PDF15已render/view完整页。

本审阅实际9distinct primary页，未读其他49归档页，不称全文两PDF。只读提取与两页render属于primary阅读，不是数学producer执行。

## V8. 收据、最终结论和保留缺口

先实际完整读作者候选来源receipt literature/manifest_cdt_odd_paired_jacobi_modified_target_normality_20261006.json，snapshot SHA d1d6716bebff24ae45a70cb4ce3678088ac1eb68d879441f905d126fa5c8a414。作者先one-way冻结finalreceipt后，本人实际完整补读最终SHA fa77214875c2beb909739791013054c8dbff87cbf9c587768e1ad2be8295fd4d，核其final state、三个数学pins、准确9页本人阅读及formalreview只记path的非循环归属。然后本审仅作这一次V8/状态补全并全文回读冻结，数学正文V1–V7未改。

本审阅按T1–T27声称scope数学通过，没有提出正文数学修订。已证actual full-Q normal profile和exact norm-free target identities；无限original λ2 simultaneous units、actual D_A无限nonzero、global fees和strict margin仍未证。作者有限3cases/692checks只支持实现，与这些缺口没有混用；本人数学执行0，旧或同行数学execute/import/rerun0，external Lean0。
