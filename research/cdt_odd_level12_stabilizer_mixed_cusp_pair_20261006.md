# D12：任意真实zero separator之间的两个抛物幂不能抵消

日期：2026-10-06。新的全尺度mixed-sign结果。所有旧冻结稿保持不变；没有word、整数参数或prime扫描，没有执行/import旧或peer producer。[独立NEW符号证书](cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006_verify.py)首次、单次43项通过，[JSON](cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006_verify.json)保留formal polynomial identities。

取[完整真实周期](cdt_odd_level12_generator_cocycle_20261006.md)的纯L函数hL=fσ,L+Θ、G*=Γ⋊〈M〉、εΓ=+1、εΓM=−1。设

\[
 c(g)=h_L|_{-2}g-\epsilon(g)h_L=i\pi^3P(g),\qquad
 K=c^{-1}(0).
 \tag{Q1}
\]

K是该实际scalar B0hL的保持群，未假定它由已知H0=〈T,M,M′〉生成。本文证明

\[
 \boxed{h\in K,\ (n,m)\in\mathbf Z^2\setminus\{(0,0)\}
    \quad\Longrightarrow\quad x_4^n h x_5^m\notin K.}
 \tag{Q2}
\]

由此所有nonzero幂都有

\[
 \boxed{Kx_4^nK\ \cap\ Kx_5^mK=\varnothing
           \quad(n,m\ne0).}
 \tag{Q3}
\]

尤其任意h∈H0、任意大的正负n,m以及左右任意H0块构成的此mixed族，都不含真实zero。这个结果覆盖相反幂、odd-sign separator，不依赖先前strict-cone的sign一致条件。它仍不是全部normal forms的分类。

## 1. 实际两个周期、缩放与任意负幂

完整九表中

\[
\begin{aligned}
 x_4&=(11,3;-48,-13),&P_4&=(-2266160,-16555200,-30256320),\\
 x_5&=(25,16;-36,-23),&P_5&=(-1329040,-4311360,-3531840).
\end{aligned}
 \tag{Q4}
\]

vector表示普通basis(1,τ,τ²)，即c/(iπ³)，不混用integer lattice的thirdcoordinate/960。两矩阵在Γ、ε=+1。设

\[
 A_4=(-1,0;4,-1),\quad A_5=(-2,-1;3,1),\quad
 x_4=A_4T^{-3}A_4^{-1}\ (PSL),\quad
 x_5=A_5T^{4}A_5^{-1}.
 \tag{Q5}
\]

第一等式的SL代表是−x4，normalized weight−2 slash相同。两个fixed cusps分别为−1/4、−2/3。其scaled periods的最高系数为

\[
 \beta_4=\operatorname{coeff}_{\tau^2}(P_4|A_4)=-294080,\quad
 \beta_5=\operatorname{coeff}_{\tau^2}(P_5|A_5)=-220560.
 \tag{Q6}
\]

记Cj(n)=P(xjⁿ)。right cocycle给

\[
 C_j(n+1)=R_{x_j}C_j(n)+P_j,\qquad C_j(0)=0.
\]

由于Dj=Rxj−I满足Dj³=0，该recurrence的准确all-integer解为

\[
 C_j(n)=nP_j+\frac{n(n-1)}2D_jP_j
                +\frac{n(n-1)(n-2)}6D_j^2P_j.
 \tag{Q7}
\]

这先对nonnegative n给geometric sum，再由invertible Rxj递推到所有负n；或直接核polynomial recurrence及Cj(0)，故不是仅适用于positive powers的形式猜测。两者最高scaled系数都是nβj。

## 2. Lorentz判别式使任何两项抵消迫绝对幂相同

普通quadratic C=p0+p1τ+p2τ²的discriminant Δ(C)=p1²−4p0p2在normalized slash

\[
 R_gC=\det(g)^{-1}(c\tau+d)^2C(g\tau)
\]

下不变，乘±1也不改变它。一般P=aτ²+bτ+c、parabolic T^w的power cocycle满足

\[
 \Delta(C(n))=n^2\left(\Delta(P)
                    -\frac{a^2w^2}{3}(n^2-1)\right).
 \tag{Q8}
\]

逐项相加P(τ+jw)的1/τ/τ²系数即可证明；该identity仍是all-integer polynomial，因而适用于negative n。这里

\[
 \Delta(P_4)=\Delta(P_5)=-188001484800,\quad
 (-3\beta_4)^2=(4\beta_5)^2=882240^2,
\]

所以准确共同公式为

\[
 \boxed{\Delta(C_4(n))=\Delta(C_5(n))
       =-307200n^2(844561n^2-232577).}
 \tag{Q9}
\]

每个nonzero integer n的discriminant严格负。函数r²(844561r²−232577)在r≥1严格增加，故Δ(C4(n))=Δ(C5(m))迫|n|=|m|。

若h∈K，则不论h是否在H0，完整signed right cocycle都准确给

\[
 P(x_4^n h x_5^m)=R_{x_5^m}R_h C_4(n)+\epsilon(h)C_5(m).
 \tag{Q10}
\]

当n,m均nonzero且(Q10)为0时，判别式不变立即给|n|=|m|；此处没有丢掉odd h的sign。若仅一幂nonzero，其period已经由(Q9)nonzero，invertible slash与zero separator不能消掉，证明(Q2)的单幂边界情况。

## 3. 周期的二次根与两个尖点的高度

对Δ(Cj(n))<0，在上半平面取唯一root zj(n)。这只是一个real rational quadratic的upper-half-plane root，不使用任何未知CM/L-value identity。令

\[
 \zeta_j(n)=A_j^{-1}z_j(n),\qquad y_j(n)=\operatorname{Im}\zeta_j(n)>0.
\]

由scaled最高系数nβj与(Q9)，

\[
 y_j(n)=\frac{\sqrt{-\Delta(C_j(n))}}{2|n\beta_j|},\quad
 \frac{y_4(n)}3=\frac{y_5(n)}4
    =\sqrt{\frac{n^2-232577/844561}{12}}.
 \tag{Q11}
\]

符号n<0改变period的正/负定方向，不改变这一rootheight的absolute-coefficient公式。若|n|=|m|=r≥1，则

\[
 \boxed{y_4(n)y_5(m)=r^2-\frac{232577}{844561}
       \ge\frac{611984}{844561}>\frac1{12}.}
 \tag{Q12}
\]

源归一的exact cancellation用4|β4β5|=307200·844561；不以rounded heights得出此严格不等式。

若(Q10)为0，则

\[
 R_h C_4(n)=-\epsilon(h)R_{x_5^{-m}}C_5(m).
\]

根在Möbius变换下的方向必须保留：左边的upper root为h⁻¹z4(n)，右边为x5ᵐz5(m)，所以

\[
 g z_4(n)=z_5(m),\qquad g=x_5^{-m}h^{-1}\in G_*.
 \tag{Q13}
\]

相乘的−ε(h)对根没有影响。因而实际抵消要求两个points在完整G*的同一orbit，不能仅用slit/局部leaf上的图形直觉排除。

## 4. 完整Γ与signed M coset的lower-left全尺度下界

令γ=(a,b;c,d)∈Γ的SL representative，c≡0 mod12且a≡d≡κ mod12、κ=±1。两scalings均det1。

对g=γ有

\[
 L_0=A_5^{-1}\gamma A_4\in SL_2(\mathbf Z),\quad
 C_0=3a-12b+2c-8d\equiv-5\kappa\pmod{12}.
 \tag{Q14}
\]

所以C0≠0且|C0|≥5，适用于整个Γ而非只有限生成元。

对g=γM，integer matrix A5⁻¹γMA4有det12；取正square-root normalized det1代表

\[
 L_1=\frac{A_5^{-1}\gamma M A_4}{\sqrt{12}},\quad
 C_1=\frac{156a+540b+104c+360d}{\sqrt{12}}.
 \tag{Q15}
\]

因c divisible12，numerator为

\[
 12\left(13a+45b+104\frac c{12}+30d\right).
 \tag{Q16}
\]

它不能为0。给出一个不依赖cusp table猜测的精确证明：MA4的firstcolumn为4(−13,−45)。γ把primitive column(−13,−45)送至primitive(u,v)。若(Q15)numerator为0，A5⁻¹的lowerrow(−3,−2)迫

\[
 (u,v)=s(-2,3),\quad s=\pm1.
\]

但v=−13c−45d≡−9κ mod12；v=3s迫κ=s。另一方面u=−13a−45b≡−κ mod3，而目标u=−2s≡s mod3，迫−s≡s mod3，矛盾。因此

\[
 \boxed{C_1\ne0,\quad |C_1|\ge 12/\sqrt{12}=\sqrt{12}.}
 \tag{Q17}
\]

这也从全矩阵同余证明两个cusp在G*中不同类。尤其没有把signed source sign ε=−1误放进det normalization；M的matrix determinant仍为正12。

## 5. 高度矛盾与完整zero separator定理

由(Q13)，在scaled coordinates有

\[
 \zeta_5(m)=(A_5^{-1}gA_4)\zeta_4(n).
\]

对任意det1 real Möbius matrix L=(A,B;C,D)、C≠0，若ζ′=Lζ则

\[
 \operatorname{Im}\zeta'=
 \frac{\operatorname{Im}\zeta}{|C\zeta+D|^2},\qquad
 (\operatorname{Im}\zeta)(\operatorname{Im}\zeta')\le\frac1{C^2}.
 \tag{Q18}
\]

因为|Cζ+D|²≥C²(Imζ)²。若g∈Γ，(Q14)给y4y5≤1/25；若g∈ΓM，(Q17)给y4y5≤1/12。二者均与(Q12)矛盾。于是(Q10)不能为0，证明(Q2)，包括任意nonzero正负幂及整个未知K中的zero separator。

对左右任意k0,k1∈K，

\[
 P(k_0 x_4^n h x_5^m k_1)
 =\epsilon(k_0)R_{k_1}P(x_4^n h x_5^m)\ne0.
 \tag{Q19}
\]

若(Q3)两个doublecosets相交，k0 x4ⁿ h x5⁻ᵐ=1可由交点等式得到，其中k0,h∈K；与(Q19)矛盾。因此(Q3)也已证。没有用“未知K=H0”作为前提。

## 6. 已解决的mixed范围与未解决事项

冻结strict-cone稿只处理signed幂方向一致的summands。本定理额外排除所有x4/x5两块、任意zero separator、任意left/rightzero因子的相反符号抵消。这是全群同余/period-root height的结果，非短word试验。它给完整K的实际doublecoset separation，即使K以后严格大于H0也仍成立。

联合关系模型C≠0的保持群是KL或KZ∩KL的相应子群，所以同一排除适用于其实际zero separators；本文不把纯ζ的更大保持群当作该目标的免费输入。

未排除的是至少三个非zero period blocks的求和，以及涉及x9或不同extra pairing的mixed forms。多项二次型相加的root不等于某一个summand的root，故(Q13)不能自动延伸到任意长normal form。本文没有求全K、没有发现新的zero subgroup、没有改变合法analytic leaf或CDT成本，也没有宣布新的ζ/L数值无理性。

## 7. 固定证书和实际审阅状态

NEW43项首次、单次通过，无修复或重复执行：两个A的det/scaling、Mdet12、两Sym² nilpotence、formal n recurrence及0/1、共同discriminant与scaledβ、generic translationdiscriminant、height exactconstant/strictbound、generic γ两个cosetlowerleftidentities、primitivecolumn与两个±congruence choices、两个旧MD的SHA pins。n一直是formal integer变量；没有枚举任何n,m、任何word或prime。± loops只是Γ定义中的两个residue signs，不是研究参数搜索。

有限checks不替代(SL congruence)任意γ的nonzero proof、negative-n recurrence、right root direction或wholeK separator论证；这些在§§1–5明确给出。root已实际阅读全文§§1–7及NEW producer源码，独立复核全部Γ/ΓM代表、right root direction与wholeK证明，通过；未执行producer。按此实际范围冻结本稿，旧冻结文件保持原状。
