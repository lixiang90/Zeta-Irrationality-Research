# D12：任意mixed元素的幂、root-closed Γ部分与精确odd-axis例外

日期：2026-10-06。新纯Markdown全尺度结构引理。不改冻结稿、不运行producer，不扫描words、整数参数或primes。使用[完整群](cdt_odd_level12_schreier_presentation_20261006.md)与[真实signed cocycle](cdt_odd_level12_generator_cocycle_20261006.md)，而非weight2 scalar kernel定理。

设G*=Γ⋊〈M〉、Γ=PSLΓ1(12)、εΓ=+1、εΓM=−1，c(g)=h|−2g−ε(g)h。结论适用于已证纯L、纯ζ各自actualcocycle及其合法joint组合；不是把nogauge primitive作为holonomic species。K=c⁻¹(0)。

## 1. 幂的准确signed polynomial与谱

令R=Rg为normalized weight−2 quadratic slash。对positive integer n，right cocycle准确给

\[
 c(g^n)=S_n^{\epsilon}(R)c(g),\quad
 S_n^{\epsilon}(R)=\sum_{j=0}^{n-1}\epsilon^jR^{n-1-j}.
 \tag{V1}
\]

negative powers用

\[
 c(g^{-n})=-\epsilon^nR^{-n}c(g^n)
 \tag{V2}
\]

得到同一zero判据，不能把positive-n recurrence直接忘记inverse sign后外推。

若g∈Γ非identity，则其为hyperbolic或parabolic，因为Γ离散、torsionfree。hyperbolic的R可对角化，谱为λ²,1,λ⁻²，其中λ>1；parabolic的R为nonidentity unipotent。ε=+1时，Sn的hyperbolic各eigenvalue均为positive实geometric sum，不能为0；parabolic时Sn(R)=nI+nilpotent，亦invertible。因此

\[
 \boxed{g\in\Gamma, n\ne0:\quad
       c(g^n)=0\ \Longleftrightarrow\ c(g)=0.}
 \tag{V3}
\]

g=1情况也成立。K∩Γ因而是root-closed subgroup：某nonzero power属于K∩Γ，primitive root本身也属于它。此结论覆盖任意长度、任意signed pattern的Γword。

## 2. ΓM的精确axis例外，不能误用scalar root argument

每个odd g可用integer matrix γM代表，det=12。若其parabolic，integer trace必须满足tr²=4det=48，矛盾。因此ΓM没有parabolics。若odd g为finite order，则g²∈Γ、torsionfree迫g²=1；否则g为hyperbolic。

对infinite odd g，R有正谱λ²,1,λ⁻²，所以R+I可逆，且

\[
 S_n^{-}(R)=(R^n-(-1)^nI)(R+I)^{-1}.
 \tag{V4}
\]

odd n时Rⁿ+I可逆；even n时ker(Rⁿ−I)=ker(R−I)。故对所有nonzero integer n

\[
 \boxed{\begin{array}{ll}
 n\text{ odd}:&c(g^n)=0\iff c(g)=0,\\
 n\text{ even}:&c(g^n)=0\iff(R_g-I)c(g)=0.
 \end{array}}
 \tag{V5}
\]

这里g已知infinite order，不把even幂的group identity混入新zero情况。

对any代表g=(a,b;c,d) normalized detD，固定line为

\[
 \ker(R_g-I)=\mathbf R\,Q_g,\quad
 Q_g(\tau)=c\tau^2+(d-a)\tau-b,\quad
 \Delta(Q_g)=(a+d)^2-4D>0.
 \tag{V6}
\]

直接代入Rg便有RgQg=Qg；hyperbolic谱的1-eigenspace为dimension1，给全部kernel。Qg的两个real roots是g的fixed points，所以该line严格indefinite。这是具体Lorentz固定空间，而不是未知L-value条件。

若c(g)=非zero scalar·Qg，则g不保持原点、而g²及其全部powers保持原点。确实c(g²)=(Rg−I)c(g)=0。这指出一种可能的真正新zero cyclic subgroup接口，但本文**没有证明任何额外actualg满足它**，也不因存在一个formal line就认领新的leaf。

对odd finiteorder involution，c(g²)=0是group relation；它迫c(g)∈ker(Rg−I)，此时Qg判别式<0、fixedline为严格定型。该情形须与infinite hyperbolic(V5–V6)分开。

## 3. 严格定translation的整个cyclic subgroup及本引理范围

如果actualc(g)/(iπ³)严格正定或负定，则

\[
 \boxed{\langle g\rangle\cap K=\{1\}.}
 \tag{V7}
\]

ε=+1时由(V3)；ε=−1且g无限order时，strictly definite vector不属于(V6)的indefinite line，所以(V5)的所有nonzero powers均nonzero；odd involution则只有identity和g，而g的translation非zero。于是先前[严格锥整族](cdt_odd_level12_stabilizer_structure_20261006.md)(S18)产生的每个actualelement，不论其中有多少odd H0 separators，其整个cyclic subgroup都被排除。这额外覆盖那些power word本身不再满足(S18)sign条件的mixed族。

更一般(V3–V6)把任意candidate power的zero问题准确降至原word的period或其明确axis line，不允许把“even power zero”统一误称“原word zero”。本引理既不分类所有primitive mixed words，也不求出fullK；对joint source的line条件必须仍作用于完整实际cocycle，不能删掉其中某一个periodcarrier。

## 4. 实际审阅状态

root已实际阅读全文§§1–4，独立核对right cocycle、Γ root-closed、odd infinite fixed-axis与finite involution区别，通过。按该actual范围冻结。本稿没有fixed numerical实例、没有producer；全proof由actualG*结构、right cocycle和三维Sym²谱给出。后续寻找真实axis-line实例或完整mixed kernel另建稿。
