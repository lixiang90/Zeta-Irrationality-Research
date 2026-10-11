# split四二次曲面family coordinate-symbol completion 的有理唯一性

日期：2026-10-06。NEW全尺度纯证明；全部旧及同行MD/PY/JSON/manifest只读，不执行/import mathematical producers。本稿在新[toric completion](cdt_odd_R0_toric_completion_20261006.md)的真实全局split strata基础上，证明family higher-Chow completion作为有理class唯一。不是regulator-current、integral marking或数值周期定理。

## U1. 明确对象和结论

沿toric稿固定光滑四维Y/Q、Y*=U⁴、split SNC边界E=Y\Y*、U=P¹\{0,∞,−1}。记D¹=E，D²为Y-codim至少2的boundary strata闭包，D³为codim至少3的闭包；D⁴=∅。各闭集取reduced structure。

其实际global strata满足
\[
\begin{array}{c|c|c}
r&\dim D^{r,*}&D^{r,*}\text{ 的component类型}\\\hline
1&3&U^{4-s}\times\mathbf G_m^{s-1},\quad 2\le s\le4\\
2&2&U\times\mathbf G_m\ \text{或}\ \mathbf G_m^2\\
3&1&\mathbf G_m.
\end{array}
\tag{U1}
\]
这里是在family overQ上的strata，而非先pass到Q(x)或复杂数fibre。

**定理。**
\[
\boxed{CH^3(E,4)_Q=0,\qquad
CH^4(Y,4)_Q\longrightarrow CH^4(Y^*,4)_Q
\text{ injective}.}
\tag{U2}
\]
因toric稿已证明coordinate-symbol ξ={v0,v1,v2,v3}存在lift，故它在CH⁴(Y,4)_Q中的family lift Ξ准确唯一。此结论将“family completion choice ambiguity”补平，不消除Abel–Jacobi lift的closed-period/Betti marking ambiguity。

## U2. 只用真实higher-Chow groups的open-curve归纳

令A为从P¹/Q删去非empty finite rational points得到的smooth curve。对smooth Z/Q，projective bundle formula和localization给
\[
CH^p(Z\times P^1,q)_Q
=CH^p(Z,q)_Q\oplus CH^{p-1}(Z,q)_Q,
\tag{U3}
\]
\[
CH^p(Z\times P^1,q)_Q\to CH^p(Z\times A,q)_Q
\to\bigoplus_{a\ \rm removed}CH^{p-1}(Z,q-1)_Q.
\tag{U4}
\]
因此两外项为0就严格迫中项为0；不需要motivic Künneth、short exact sequence splitting或把generic field zero当成full variety zero。

所用point输入均已在Doran–Kerr原件PDF25–26实际读到：rational higher-Chow的Adams decomposition与K_even(Q)_Q=0给
\[
CH^2(Q,4)_Q=CH^3(Q,4)_Q=0,
\quad CH^2(Q,3)_Q=0.
\tag{U5}
\]
第二个是totally-real数域的K3/weight2 vanishing。对全部smooth separated Z/Q，
\[
CH^1(Z,q)=0\quad(q\ge2)
\tag{U6}
\]
是整系数定理：MVW2006 Theorem4.1/Corollary4.2和Theorem19.1给CH¹(Z,q)=H^(2−q,1)(Z,Z)，weight one在degree≤0消失。其实际读页与本次保存的官方原件见[weight-one来源收据](../literature/manifest_cdt_odd_weight_one_higher_chow_20261006.json)。

首先对任意finite product Z=A1×…×Am归纳
\[
CH^2(Z,3)_Q=CH^2(Z,4)_Q=0.
\tag{U7}
\]
m=0由U5。若对Z成立，U3在(p,q)=(2,3),(2,4)的额外项CH¹(Z,q)都由U6为0，U4的右项CH¹(Z,q−1)亦为0，故对Z×A继续成立。

其次归纳
\[
CH^3(Z,4)_Q=0\quad\text{对全部这种finite product }Z.
\tag{U8}
\]
m=0同样由U5；U3额外项CH²(Z,4)及U4右项CH²(Z,3)已由U7为0，故递推完成。

U1的r1components都是三个rational open curves的product，U8给CH³(D¹*,4)_Q=0；r2components是两个的product，U7给CH²(D²*,4)_Q=0；r3components=Gm，U6给CH¹(D³*,4)=0。

## U3. singular boundary严格使用dimension indexing

E本身是equidimensional3的SNC union，可singular。写higher-Chow dimension notation CH_j，避免误将Y-codim与E-codim混同：对于equidimensionald的variety，CH^p(X,q)=CH_(d−p)(X,q)。因此
\[
CH^3(E,4)=CH_0(E,4),
\quad CH^{4-r}(D^{r,*},4)=CH_0(D^{r,*},4).
\tag{U9}
\]
在closed/open localization中dimension index j=0不变；不需要ambient smoothness或将E视作smooth。

D³=D³*是disjoint Gm，因此CH0(D³,4)_Q=CH¹(D³,4)_Q=0。对closed D³⊂D²及open D²*，localization exactness给
\[
CH_0(D^3,4)_Q\to CH_0(D^2,4)_Q\to CH_0(D^{2,*},4)_Q.
\tag{U10}
\]
两外项刚已证明0，故CH0(D²,4)_Q=0。再对D²⊂E及openD¹*：
\[
CH_0(D^2,4)_Q\to CH_0(E,4)_Q\to CH_0(D^{1,*},4)_Q,
\tag{U11}
\]
同理得CH0(E,4)_Q=0。这是U2第一个等号，直接closed filtration证明，不依赖一个未核验的singular-boundary spectral sequence或仅field residue。

最后对E⊂Y的localization，在同一dimension indexj=0中为
\[
CH_0(E,4)_Q\to CH_0(Y,4)_Q\to CH_0(Y^*,4)_Q.
\tag{U12}
\]
Y,Y*dim4，所以中、右项就是CH⁴(−,4)_Q。左项为0迫restriction injective，完成唯一性证明。

## U4. 唯一family class也确实非零

generic point restriction将ξ送到
\[
\{v_0,v_1,v_2,v_3\}\in
K_4^M(Q(v_0,v_1,v_2,v_3))_Q
\simeq CH^4(Q(v_0,v_1,v_2,v_3),4)_Q.
\tag{U13}
\]
DK PDF27给此field Milnor/higher-Chow isomorphism和graph-symbol restriction。现在依次取vj=0的discrete valuations及Milnor tame residue（每次其余variables为units）：
\[
\{v_0,v_1,v_2,v_3\}\longmapsto
\pm\{v_1,v_2,v_3\}\longmapsto
\pm\{v_2,v_3\}\longmapsto
\pm\{v_3\}\longmapsto\pm1\in K_0^M(Q)=Z.
\tag{U14}
\]
⊗Q后最后仍非零，故generic class、ξ和其唯一Ξ皆非零。这只用field restriction的一个非零image推出原class非零，不以field restriction injectivity来证明global completion。

这些vj=0 valuations对应φ的pole/vertical λ=∞方向，在Y=f^-1(Gm)之外；不是toric稿d1所处理的surviving horizontal boundary。故此nonvanishing不与后者因unit{-1}消失矛盾。没有由U14推出任何individual fibre regulator非零或数值独立。

## U5. 对后续周期研究的准确作用

现在family coordinate-symbol在该Q-model中的rational completion class已非零且无choice ambiguity，可固定其functorial regulator class研究。然而下列并未证明：

* integral higher-Chow唯一性；上述torsion及Borel只在Q coefficients使用。
* base change到C、Q(x)、一般number field或其它model后仍有相同vanishing；不能把Q的totally-real输入无依据移到function field。
* 任意individual fibre completion、nearby-cycle class或conifold singular-fibreclass的唯一性；本文定理只在明确family overQ上。
* regulator作为current、其Betti lift、closed-cycle ambiguity、Tate factors与旧relative-chain marking的唯一性或比较；这些不是同一个higher-Chow class是否唯一的问题。
* 任何新的R0、ζ或L-value数值无理性/线性无关性。

因此toric主稿原先列出的“completion可能不同”的第一类缺口，现可在这个特定rational family class层面精确移除；其它解析/整格/marking接口仍须真正计算。没有改写冻结旧稿，新的定理单独保存。

本文是全尺度纸面证明，无producer、无有限checks、无Lean声明。实际primary输入页：DK25–29（vanishing/Adams/field-symbol与localization）；MVW40–42、151、174、176–178（weight one、对任意scheme的localization和higher-Chow comparison）；Levine1994 PDF79–85（products/projection、Corollary5.4 rational projective bundle）。冻结toric输入SHA256为`abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0`。独立review由另NEW记录登记，不以此稿声称已完成数值goal。
