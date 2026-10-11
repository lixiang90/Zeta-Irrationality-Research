# D12：真实纯L稳定子沿两个抛物幂的严格malnormal性

日期：2026-10-06。这是新的全尺度self-pair定理，使用完整actual cocycle，不把已知H0当作完整稳定子。所有旧冻结稿不修改、不执行。没有words、参数或素数扫描。

沿用[两个不同尖点的分离](cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006.md)的Q1、Q4–Q13：Γ=PSLΓ1(12)，G*=Γ⋊〈M〉，纯L actual cocycle为c(g)=iπ³P(g)，K=c⁻¹(0)。这里K是未知的完整原点稳定子。固定

\[
 x_4=(11,3;-48,-13),\quad x_5=(25,16;-36,-23),
\]

以及det1 cusp scalings A4=(-1,0;4,-1)、A5=(-2,-1;3,1)。它们给x4=A4 T⁻³ A4⁻¹、x5=A5 T⁴ A5⁻¹（PSL）。

## 1. 新定理与它的精确范围

对j=4或5、h∈K、n,m为nonzero integers，有

\[
 \boxed{x_j^n h x_j^m\in K
       \quad\Longleftrightarrow\quad h=1,\ m=-n.}
 \tag{N1}
\]

因此对每个n≠0，

\[
 \boxed{K\cap x_j^nKx_j^{-n}=\{1\}.}
 \tag{N2}
\]

所有不同integer幂的doublecosets KxjⁿK也互不相同，包括identity幂。更一般，xjⁿKxj⁻ⁿ这整个conjugate family两两只交identity。这里结论作用于完整未知K，增强先前仅在严格定translation条件下处理gH0g⁻¹的结论。

它不证明K*〈xj〉嵌入G*，也不分类三块以上的normal form。联合关系C≠0的稳定子是KL的子群，故同一(N1–N2)适用于该实际子群；不把pureζ的不同period表替换成这里的纯L数据。

## 2. 两项抵消的必要root orbit

记Cj(n)=P(xjⁿ)。前稿已全整数证明

\[
 \Delta C_j(n)=-307200n^2(844561n^2-232577),
 \tag{N3}
\]

且判别式在|n|≥1随|n|严格变化。若xjⁿ h xjᵐ∈K，actual signed right cocycle给

\[
 R_{x_j^m}R_h C_j(n)+\epsilon(h)C_j(m)=0.
\]

于是|n|=|m|。以zj(n)为Cj(n)的唯一upper-half-plane root，抵消准确迫

\[
 gz_j(n)=z_j(m),\qquad g=x_j^{-m}h^{-1}\in G_*.
 \tag{N4}
\]

negative幂不能猜root方向；inverse cocycle准确给

\[
 C_j(-n)=-R_{x_j^{-n}}C_j(n),\qquad
 z_j(-n)=x_j^n z_j(n).
 \tag{N5}
\]

令ζj(n)=Aj⁻¹zj(n)，yj(n)=Imζj(n)，r=|n|。前稿的all-integer height公式给

\[
 y_4(n)^2=\frac34\left(r^2-\frac{232577}{844561}\right),\quad
 y_5(n)^2=\frac43\left(r^2-\frac{232577}{844561}\right).
 \tag{N6}
\]

这些heights对n,m的正负不变。两点都在同一j的scaled coordinate中，所以det1 Möbius matrix的lower-left非零时必须满足yj(n)²≤1/C²。

## 3. 任意Γ与ΓM元素的同尖点lower-left下界

取γ=(a,b;c,d)∈Γ的SL representative，c≡0 mod12，a≡d≡κ mod12，κ=±1。直接矩阵相乘给

\[
\begin{array}{c|c|c}
 j&\operatorname{lowerleft}(A_j^{-1}\gamma A_j)
   &\operatorname{lowerleft}(A_j^{-1}\gamma M A_j)/\sqrt{12}\\\hline
 4&4a-16b+c-4d
   &4(52a+180b+13c+45d)/\sqrt{12}\\
 5&6a-9b+4c-6d
   &3(69a+240b+46c+160d)/\sqrt{12}.
\end{array}
 \tag{N7}
\]

even栏分别是4和3的整数倍，故若非零，其absolute values至少4和3。odd栏两个括号均≡κ mod12，不能为零；对应absolute values至少4/√12和3/√12。M的正det12只通过除√12归一，不能把source sign ε=-1当作matrix determinant。

设θ0=232577/844561。已有严格有理不等式1−θ0>1/12。因此(N6)对所有r≥1给y4²>1/16、y5²>1/9。若(N4)的g在Γ，(N7)和height inequality迫同尖点lower-left为零。于是g保持该cusp。完整Γ的cusp widths在这两点分别为3和4，且xj恰为对应primitive generator，所以

\[
 g\in\Gamma\quad\Longrightarrow\quad g=x_j^k
 \text{ for some }k\in\mathbf Z.
 \tag{N8}
\]

这使用完整torsion-free cusp stabilizer，不仅是检查有限生成元。

若g∈ΓM，r≥2时r²−θ0>1；(N6)给y4²>3/4、y5²>4/3，与odd栏的1/C² upper bounds矛盾。只剩r=1，需要下一节的exact arithmetic argument，不能丢掉这个小幂边界。

## 4. r=1的odd例外由二次根域严格排除

因为m=±n，(N5)说明(N4)的odd g或者自身固定zj(n)，或者xj⁻ⁿg固定zj(n)。这仍是ΓM中的元素。任何ΓM元素若固定upper-half-plane point就是elliptic；G*是Γ的有限index extension且离散，故该elliptic有finite order。其square在torsion-free Γ中，因此其projective order只能2。用integer det12代表，它的trace为0，fixed-point quadratic判别式为−48，所以该upper point属于Q(√−3)。

然而r=1时，Cj(n)的判别式与−48之比为

\[
 \frac{-188001484800}{-48}
       =6400\cdot611984\equiv2\pmod3.
 \tag{N9}
\]

该positive integer不能是Q-square：integer若是rational square则已经是integer square，而integer square mod3只有0、1。Cj(n)的二次域因此不是Q(√−3)。这同时排除j=4和5、n=±1的odd固定点。没有枚举elliptic words或CM参数。

## 5. Γ剩余情况仅有平凡抵消

由§§3–4，g必须在Γ且g=xjᵏ。若m=n，(N4)迫xjᵏ固定upper-half-plane point，parabolic power只能k=0。于是h=xj⁻ᵐ；但m≠0且(N3)严格负，h不在K，矛盾。

若m=-n，由(N5)知g z(n)=xjⁿz(n)。于是xjᵏ⁻ⁿ固定upper-half-plane point，迫k=n，(N4)的g=xjⁿh⁻¹进而迫h=1。反向h=1,m=-n时product是identity，确在K。证明(N1)。

取m=-n立即得(N2)。两个不同conjugates的intersection经xj幂conjugation化为(N2)，故同样只有identity。若两个doublecosets相等，将交点等式整理成xjⁿ h xj⁻ᵐ∈K，其中h∈K；nonzero幂用(N1)迫n=m，某一幂为0时非zero Cj不能被zero左右因子消去。于是全部doublecosets不同。

## 6. NEW固定证书与实际审阅状态

[NEW producer](cdt_odd_level12_stabilizer_parabolic_malnormal_20261006_verify.py)首次、单次24项通过，无错误或修复；[JSON](cdt_odd_level12_stabilizer_parabolic_malnormal_20261006_verify.json)保存formal identities与两个冻结输入pins。它仅检查预定两个scalings的det/幂、formal γ的四lower-left identities、固定同余、height严格有理数和唯一r=1的quadratic-field square obstruction；不扫描parameters或words。有限符号checks不替代wholeΓ cusp-stabilizer、all-integer recurrence、root direction或unknownK argument。

root已实际阅读全文§§1–6及NEW producer源码，独立复核allΓ cusp-stabilizer、negative根方向、odd r=1 elliptic finiteorder及root-field非square、全部N1证明，通过；未执行producer。按该actual范围冻结正文及单次证书。没有声称完整kernel已解，没有新增合法group generator，也没有给CDT Taylor Smith或数值定理信用。
