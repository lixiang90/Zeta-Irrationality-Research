# D12 真实稳定子的自由因子结构与严格锥判据

日期：2026-10-06。新的全群结构证明，旧冻结 source、period、presentation 文件均未修改。本文不搜索短字或研究参数，不执行/import旧或peer producer。新固定[Nielsen/Tietze证书](cdt_odd_level12_stabilizer_structure_20261006_verify.py)仅检验下述展示的有限变换和既定三个周期；[JSON](cdt_odd_level12_stabilizer_structure_20261006_verify.json)64项通过。第一次运行有一个SL2中央正负代表的比较错误，§7完整记录；证明使用PSL2，不改变任何输入。

本文的实质结论是

\[
 \boxed{G_* = H_0*F(x_4,x_5,x_9),\qquad
 H_0=\langle T,M,M'\rangle\simeq\mathbf Z*C_2*C_2.}
 \tag{S1}
\]

因此已经知道的真实保持群是完整模群的一个**自由因子**。这并不证明完整原点稳定子恰为该因子；本文另给一个适用于无限字族的严格锥排除判据，并明确其未覆盖的抵消。

## 1. 完整实际输入和稳定子定义

使用[已冻结Schreier表示](cdt_odd_level12_schreier_presentation_20261006.md)的真实群

\[
 \Gamma=PSL\Gamma_1(12)=F(x_1,\ldots,x_9),\quad
 G_*=\Gamma\rtimes\langle M\rangle,\quad
 M=(24,-7;84,-24),\quad M'=(-24,-7;84,24).
 \tag{S2}
\]

这里九个xj是由Bass–Serre spanning tree得到的自由基，不是仅因矩阵数量等于九而猜生成。Γ的完整表示和所有M-conjugation words均为输入。设α(g)=MgM⁻¹、T=x2；由该表示

\[
 k=M'M=x_7^{-1}x_1x_8^{-1}x_5^{-1}T^{-1},\qquad
 \alpha(k)=k^{-1}.
 \tag{S3}
\]

矩阵相等均在PSL2(R)理解：k的常用代表为(97,−28;−336,97)，而固定自由字可能给相反中央SL2代表；normalized weight−2 slash不受这一中央符号影响。

两真实函数与实际周期取[完整九表](cdt_odd_level12_generator_cocycle_20261006.md)：

\[
 h_Z=f_Z-103680\zeta(3),\quad
 h_L=f_{\sigma,L}+34560\sqrt3L(3,\chi_{12}),\quad
 c_•(g)=h_•|_{-2}g-\epsilon(g)h_•.
 \tag{S4}
\]

εΓ=+1、εΓM=−1。它们都满足c(T)=c(M)=c(M′)=0。signed right cocycle为

\[
 c(g_1g_2)=c(g_1)|_{-2}g_2+\epsilon(g_1)c(g_2),\qquad
 c(g^{-1})=-\epsilon(g)c(g)|_{-2}g^{-1}.
 \tag{S5}
\]

H=B0h的真实保持群准确是K=c⁻¹(0)，而非source的模群。完整period已证c/(iπ³)∈Q[τ]≤2，并给整数affine representation；本文只研究其真实原点稳定子，不给Taylor整格或Smith收益。

## 2. 一个实际Nielsen自由基：不是从Euler characteristic猜自由因子

设

\[
 u=\alpha(T),\quad p=\alpha(x_4),\quad
 q=\alpha(x_5),\quad v=\alpha(x_9).
 \tag{S6}
\]

原Schreier稿的两个缩写为

\[
 \mathcal U=T x_5x_8x_1^{-1}=k^{-1}x_7^{-1},\quad
 \mathcal V=\mathcal U x_7x_4^{-1}=k^{-1}x_4^{-1}.
\]

其完整α字因此给以下literal自由字恒等式：

\[
\begin{aligned}
 x_1&=x_7kT x_5x_8,\\
 u&=T x_5x_3x_6^{-1}x_4k,\\
 p&=k^{-1}x_7^{-1}k,\\
 q&=u^{-1}T x_6^{-1}x_4k,\\
 v&=k^{-1}x_7^{-1}x_8^{-1}x_5^{-1}T^{-1}u.
\end{aligned}
 \tag{S7}
\]

这些给五次明确Nielsen替换。先以k替x1：定义k中x1出现恰一次，其余字母保持。再以u替x3：在第二式中x3出现恰一次，其余均已是现有基。然后以p替x7、以q替x6、以v替x8；这三式中的被替变量均以逆元恰出现一次，其余是仍保留的基。每一步是“被替字母或其逆元左右乘不含它的字”，可由Nielsen inversion与multiplication组成，故保存自由基。所得

\[
 \boxed{\mathcal B=(T,k,u,x_4,x_5,x_9,p,q,v)
          \text{是}\Gamma\text{的自由基}.}
 \tag{S8}
\]

为完全展示反向映射，无需依赖finite matrix同值判断自由字：

\[
\begin{aligned}
 x_7&=kp^{-1}k^{-1},\\
 x_6&=x_4kq^{-1}u^{-1}T,\\
 x_8&=x_5^{-1}T^{-1}u v^{-1}p k^{-1},\\
 x_1&=kp^{-1}u v^{-1}p k^{-1},\\
 x_3&=x_5^{-1}T^{-1}u q^{-1}u^{-1}T,
\end{aligned}
 \tag{S9}
\]

且x2=T、x4/x5/x9不变。新证书逐个核两方向全部九字的composition为空/自身，不以相同PSL matrix代替自由群同字。

## 3. M扩张的Tietze消去给出完整自由积

α²=1及(S3)/(S6)在新自由基中恰为

\[
 T\leftrightarrow u,\quad k\mapsto k^{-1},\quad
 x_4\leftrightarrow p,\quad x_5\leftrightarrow q,\quad
 x_9\leftrightarrow v.
 \tag{S10}
\]

这是完整旧α表示经过(S9)后的恒等式。把Γ自由基(S8)放入已知忠实semidirect presentation，消去u,p,q,v及其由M²=1已蕴含的反向relation，准确得到

\[
 G_*=\langle T,k,M,x_4,x_5,x_9
          \mid M^2=1,\ MkM=k^{-1}\rangle.
 \tag{S11}
\]

设M′=kM；MkM=k⁻¹恰等价(M′)²=1，反向k=M′M。于是

\[
 G_*=\langle T,M,M',x_4,x_5,x_9
          \mid M^2=(M')^2=1\rangle
     =\langle T,M,M'\rangle*F(x_4,x_5,x_9).
 \tag{S12}
\]

这既证明H0无额外relation，也证明其在完整群中是自由因子，以及三个补生成元的任何非空自由字都不在H0。原来的Γ∩H0准确为F(T,u,k)，在H0中index2、rank3；Γ的其余六个基字为x4,x5,x9,p,q,v。Euler characteristic的−4与完整群signature一致，但并非本证明的依据。

## 4. 真实周期上的两个直接全群推论

首先H0⊂KZ∩KL，因为三个actualgenerators均有zero signed period、而zero集合由(S5)封闭为群。(S12)并不将该包含改成等号。

其次完整九表有cZ(x9)=0。因此

\[
 \boxed{H_Z^{\rm aug}=\langle T,M,M',x_9\rangle
       =H_0*\langle x_9\rangle
       \simeq F_2*C_2*C_2\subset K_Z,}
 \tag{S13}
\]

且该包含的左群严格大于H0。严格性来自实际自由因子(S12)，不是只从矩阵不同判断。已知η=T x9⁻¹，所以同一群也为〈T,M,M′,η〉；η的pureZ period为0早已知道，本稿新增的是它独立于H0的结构证明，不声称新ζ数值结论。

pureL的三个补生成元全有nonzero period。联合BC两项均非zero时，[联合完整模型](cdt_odd_level12_joint_full_model_20261006.md)已证其保持群准确为KZ∩KL；(S13)因x9∉KL而不能免费移植到C≠0的目标。这里也不因单个三个extra非zero而宣称KL=H0。

## 5. 一个真正all-word的strict cone排除判据

写Pj=cL(xj)/(iπ³)。实际三向量为

|j|Pj constant, τ, τ² coefficients|discriminant p1²−4p0p2|
|---|---|---:|
|4|(−2266160,−16555200,−30256320)|−188001484800|
|5|(−1329040,−4311360,−3531840)|−188001484800|
|9|(−1587840,−3617280,−2073600)|−85465497600|

三者在实轴均严格负，且最高系数<0、判别式<0。令𝒞±为正/负定real binary quadratic form的两个开锥：齐次形式p0Y²+p1XY+p2X²对所有(X,Y)≠0同号。对任何detg>0的real matrix

\[
 P|_{-2}g=\det(g)^{-1}(c\tau+d)^2P(g\tau)
 \tag{S14}
\]

来自可逆实变量替换，保持𝒞+和𝒞−；这也在cτ+d=0处由齐次多项式解释。各锥对正和封闭，故有限个严格同号项之和不能为0。

由(S5)，每个非zero integer n都有

\[
 P(x_j^n)\in
 \begin{cases}\mathcal C_-&n>0,\\\mathcal C_+&n<0,
 \end{cases}
 \quad j\in\{4,5,9\}.
 \tag{S15}
\]

正n由n项slash后的Pj相加；负n再用inverse formula和ε(xj)=+1。这证明〈xj〉∩KL={1}，包含所有幂而非一次有限check。

更一般，把一个词实际写成

\[
 g=h_0 a_1^{n_1}h_1\cdots a_r^{n_r}h_r,\quad
 h_i\in H_0,\ a_i\in\{x_4,x_5,x_9\},\ n_i\ne0,\ r\ge1.
 \tag{S16}
\]

无需假定hi只有有限长度。令gi^pre为ai块前面的实际prefix，gi^post为其后的suffix。H0各块的period为0，完整signed cocycle的展开准确为

\[
 \frac{c_L(g)}{i\pi^3}
   =\sum_{i=1}^r\epsilon(g_i^{\rm pre})
       \left(P(a_i^{n_i})|_{-2}g_i^{\rm post}\right).
 \tag{S17}
\]

若所有ε(gi^pre)sign(ni)相同，(S14)/(S15)使所有summands属于同一个严格锥，所以

\[
 \boxed{\epsilon(g_i^{\rm pre})\operatorname{sign}(n_i)
       \text{不随}i\text{变化}\quad\Longrightarrow\quad c_L(g)\ne0.}
 \tag{S18}
\]

例如所有extra幂均正、所有hi的ε=+1时必被排除；同理全部负幂。允许odd hi时，可按实际prefix符号选择ni仍得到排除。它也排除C≠0的joint stabilizer中这些字，因为其cL必须zero。这个全尺度结果基于三个明确actualquadratics，不是对短字的实验。

## 6. 完整稳定子仍缺什么

(S18)的sign条件不能删除。即便P4与P5均负定，其差

\[
 P_4-P_5=(-937120,-12243840,-26724480),\quad
 \operatorname{disc}(P_4-P_5)=49735439155200>0
 \tag{S19}
\]

已是indefinite。cL(x4x5⁻¹)=(P4−P5)|x5⁻¹·iπ³仍为indefinite，虽nonzero，但严格锥论证不适用；再插入oddM因子或相反幂，会让summands进入相反锥。实际整数affine作用具有可抵消项，不能由(S12)或三个extra均nonzero自动否定这些字。

因此下一精确任务是：对(S12)的自由积normal form，控制至少两个相反signed贡献的Lorentz/Sym² translation，或找到其严格zero。完整实period数据已固定；无需再对未知Θ施Galois，也无需再寻找Γ generators。若希望用generalized Dedekind reciprocity或affine ping-pong，仍须给出覆盖这些相反sign正常字的独立结构证明。

本文未分类KL、KZ、KZ∩KL，未证明新mixed zero subgroup、未完成其fullleaf/capacity或Smith账本；也未证明ζ/L的新数值定理。它完成的是实际完整表示上的自由因子定理和一个无限字族的真实period排除。

## 7. NEW证书和实际审阅状态

新证书64项：全部九α²自由字、双向九基变换、全部九newα、k逆元、U/V简化、literal九M-conjugation matrices、M/M′involutions、kM=M′、三个pureL extra/nonzero与负定、pureZ x9zero、差indefinite、两个旧MD的固定SHA pins。仅读冻结文件用于hash，不执行任何旧或peerproducer。

第一次运行在`k-literal`停止：该fixedword给相反中央SL2代表，原assert误用literal det1代表相等；此前自由字和M相关projective checks已经通过。只把该一条改为同PSL projective比较，第二次运行64项全部通过。新JSON如实记录两次历史。没有修改mathematicalwords、period向量或自由基公式，也没有继续反复跑通过后的producer。

有限证书不替代Nielsen原理、Tietzefaithfulness或strict-cone全词证明；这些在§§2–5逐行给出。root已实际只读全文§§1–7与新verify.py，独立重推五步Nielsen substitutions(S7–S9)、α在新freebasis上的交换/反转、忠实Tietze/freefactor、纯ζ严格性、signed prefix/suffix cone的全字scope，限定数学审阅通过；没有执行producer，也没有认领fullkernel分类。按该实际审阅仅修复(S10–S12)/(S16)缺失的LaTeX反斜杠并记录审阅状态，不重跑已通过证书。本文及三文件据此冻结；后续kernel研究另建稿。
