# 第224轮：固定 Padé 三行的完整 p-adic 余项与无限非零

2026-10-08。本稿证明固定222 packet 的三列(A3,A5,A7)在一个显式无界素数尺度上非退化。**不证明ζ(7)无理，不支付H_g的非有理性、最小秩、主奇点或strict holonomy费用。** 不改222/223。

**定理。** 令 Δ_r 保持222的列顺序和相邻尺度。对每个素数

`p>37，p ∤ 7763789492179875`，

有

`Δ_((p−1)/2)/p ≡ 7763789492179875/4 (mod p)`，
`v_p(Δ_((p−1)/2))=1`。                                      (I1)

故 Δ_r 有无限多个非零项。这里除去的是一个明确固定整数的有限素因子集，不是prime scan或待假设的无穷regular-prime条件。

## 1. 输入、尺度与所需层

实际输入是222数学包11908 B / `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`及有限补充3006 B / `c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f`，本agent在223已实际FULL读。223本人 [N1–N10稿](pade_infinite_nonzero_gate_round223_20261008.md)，10073 B / `f12f19984ebdcff427ac336f48869057e48d57353b28e0ea1b620252d2889931`，已实际FULL保存复读；本轮沿其N7继续同一对象，没有用新的归一化替换原Δ。

取 n=p−1,p+1,p+3。令 `κ=(3/2,15/4,189/32)`，`S_(j,n)=Σ_k(−1)^k c_(j,k,n)`，`A_(s,n)=κ_s S_(s−1,n)`。223证明 integral rows

`R0=(p A3,p−1,A5,p−1/p,A7,p−1/p³)`，
`Rm=(p³A3,pA5,A7/p)_(p+m)，m=1,3`，

满足 `det(R0,R1,R3)=pΔ_((p−1)/2)`，以及

`R0≡w=(0,−45/2,−189/16)`，
`Rm≡B_m v1`，`v1=(555/16,855/16,189/32)`。

N7的exact剩余行是 `E=(R3−βR1)/p`，`β=B3/B1`，且 `Δ=det(R0,R1,E)`。模p³的完整pair展开先给 E modp；此层仍退化。为了完成无限非零，本稿再推进一个有明确结构控制的cubic层，而不计算与det无关的全部高阶scalar。

全素数幂安全分母仍由冻结P8–P13保留。此处的p局部证明包含所有目标列h=4,2,0及完整unit jets，不删除常数尾C、固定2或其他素数费用；也不把prime-scale单个Δ估值当完整前缀source-lattice指数。

## 2. 全p-block所需同余的自足乘积证明

记 `H_b^(h)=Σ_(i=1)^b i^(−h)`，H0=0。在F_p中乘一个λ且λ^h≠1，得到

`H_(p−1)^(2)≡H_(p−1)^(3)≡0 (mod p)`，p>5。

这样的λ存在，因为多项式X^h−1至多h个根而p−1>h。再用i↦p−i配对，

`2H_(p−1)^(1)=Σ_i[1/i+1/(p−i)]≡−pH_(p−1)^(2)≡0 (mod p²)`。

故 `H_(p−1)^(1)≡0 modp²`，p>3；这是本证明实际需要的Wolstenholme harmonic层，已在这里证明，不引用未读的强版本或更高层。

对固定L=0,1,2和0≤b<p，删除p倍整数后的prefix和满足

`Σ_(1≤d≤Lp+b,p∤d) 1/d ≡ H_b^(1)−LpH_b^(2) (mod p²)`，
`Σ_(1≤d≤Lp+b,p∤d) 1/d^h ≡ H_b^(h) (mod p)，h=2,3`。           (I2)

完整每块的first reciprocal为 `H_(p−1)^(1)−lpH_(p−1)^(2)≡0 modp²`；second/third reciprocal块为0 modp。余下partial block逐个展开即可。再由

`binom(2p,p)=2∏_(i=1)^(p−1)(1+p/i)≡2 (mod p³)`，

因为first/second elementary symmetric项由上述H1/H2同余清除。没有假设模p⁴时完整块还为0；更深未知项将显式留在scalar中。

## 3. 全pairs的coarse函数与完整unit二阶

固定m=1或3、0≤a≤m，b=m−a，令

`T_a=binom(m,a)^2 binom(m+a,m)binom(2m−a,m)`，
`L_a=H_(m+a)^(1)+2H_(2m−a)^(1)−3H_(m−a)^(1)`，
`M_a=H_(m+a)^(2)+4H_(2m−a)^(2)−3H_(m−a)^(2)`，
`d_a=(9L_a²−3M_a)/2`。

由small factorial segments及§2的central binomial乘积，

`c6,a,p+m=8T_a³[1+3pL_a+p²d_a+p³e_a(p)]`，`e_a(p)∈Z_p`。     (I3)

这是模p³展开后定义的exact integral余项；没有令e_a为0。最高值mirror为 `c6,p+a,p+m=c6,b,p+m`。

写 t=pz−a。唯一p倍 numerator距离是−p、2p，denominator poles是0、−p；因此完整coarse函数恰为

`𝓡(z)=R_(n=1)(z)=(z−1)^3(z+2)^3/[z^6(z+1)^6]`，
`p⁶ R_(p+m)(pz−a)=−T_a³ 𝓡(z) U_a(z;p)`。                    (I4)

𝓡是coarse有理函数，与n=p+1的normalized row R1区分。

U_a由(I3)的normalizing scalar乘全部unit距离因子组成。负 numerator unit距离为a+j，正 numerator unit距离为p+m+j−a，denominator unit距离为r−a，分别在原P7的范围j=1..p+m、r=0..p+m中删除p倍距离；signed denominator保留。每因子是 `(1+pz/d)^e`，d为p-unit、e为3或−6（负numerator的符号在d中保留）。它们在z=0、−1处及全部所需jets均正则。

令λ、ρ、ν为unit log的signed first、second、third reciprocal sums，权分别是(e/d),(e/d²),(e/d³)。由(I2)，

`λ=q_a+pℓ_a+p²α_a(p)`，`ρ=ρ_a+pη_a(p)`，`ν≡ν_a modp`，

其中余项α、η在Z_p，且

`q_a=3[H_(2m−a)^(1)−H_(m+a)^(1)+3H_a^(1)−3H_(m−a)^(1)]`，
`ℓ_a=3[H_(m+a)^(2)−2H_(2m−a)^(2)+3H_(m−a)^(2)]`，
`ρ_a=3[H_(m+a)^(2)+H_(2m−a)^(2)−3H_a^(2)−3H_(m−a)^(2)]`，
`ν_a=3[H_(2m−a)^(3)−H_(m+a)^(3)+3H_a^(3)−3H_(m−a)^(3)]`。     (I5)

正、负距离的square signs与cube signs均计入。这支付完整unit二阶与所有完整块；α、η容纳其更高层，没有把它们免费清零。

由 `log Q=pzλ−p²z²ρ/2+p³z³ν/3+O(p⁴)`，乘(I3)可写

`U_a=1+p(3L_a+q_a z)+p²(d_a+γ_a z+δ_a z²)`
`       +p³(e_a+u_a(p)z+v_a(p)z²+t_a z³)+O(p⁴)`，             (I6)

`γ_a=ℓ_a+3L_a q_a`，`δ_a=(q_a²−ρ_a)/2`，
`t_a=q_a³/6−q_aρ_a/2+ν_a/3`。

例如exact第三层linear/quadratic余项是 `u=α+3Lℓ+dq`、`v=qℓ−η/2+3Lδ`，均保留。O(p⁴)表示在两个coarse poles的regular germs中各系数都在p⁴Z_p；因为每个unit factor的degree h系数含p^h，截到degree3及p³后，z↦−1+w也保持此整性。乘固定𝓡并取pole系数h≤5不会丢失任何denominator深度。

其余partial clusters的c6估值≥6，正则h层至多损失h，所以 `p^h c_(6−h)∈p⁶Z_p`；在normalized row Rm再除p之后仍至少在p⁵Z_p。它们在所用模p³/p⁴中不贡献，但没有被假设为exact零。

## 4. Reflection filtration：二阶退化与下一层的两个方向

令y=z+1/2。𝓡关于z↦−1−z对称。对j=2,4,6，定义Λ_j(P)为𝓡P在pole0的j阶系数，减去在pole−1的j阶系数。reflection-even P给Λ_j(P)=0。因此degree≤q多项式只通过

`P_odd=y Q(y²)，dim≤floor((q+1)/2)`

影响三个目标列。这个是image dimension上界，不是任意actual unit packet都达到该rank的断言。

特别q=1,2只一个方向。定义

`v_d=−(κ3Λ2(y^d),κ5Λ4(y^d),κ7Λ6(y^d))/8`，d=1,3。

由223的ψ系数或直接有限乘法，

`v1=(555/16,855/16,189/32)`，
`v3=(−297/64,−225/64,189/128)`，
`det(w,v1,v3)=1148175/4096≠0`。                              (I7)

这明确说明第三层能有第二个pair方向，且它与n=p−1行可组成rank3；仍须支付actual cubic amplitude，不能只靠dimension上界。

二阶多项式的reflection-odd coefficient为γ−δ。由(I5)，

`q_a=3(L_a−L_b)`，`γ_a−δ_a=d_a−d_b`。

定义固定有理数

`B_m=Σ_a(−1)^a 8T_a³ q_a`，
`D_m=Σ_a(−1)^a 8T_a³(d_a−d_b)`，
`F_m=Σ_a(−1)^a 8T_a³ t_a`。

第三层polynomial的reflection-odd部分为某个integral scalar乘y，加上t_a y³；全部e,u,v等余项只进入第一个scalar。这些项因coarse反射结构而受控，不是被忽略。由alternating pair权(+,-)和(I4)–(I6)，得到

`Rm=(B_m+pD_m+p²K_m(p))v1+p²F_m v3+O(p³)`，`K_m(p)∈Z_p`。     (I8)

这里K_m(p)是exact未知的linear方向scalar。它可含更深完整块/最高系数的信息，不能移去后当作零；下节将用determinant结构消掉它。

## 5. 固定常数、E modp与actual cubic residual

有限有理数表为

| m | B_m | D_m | F_m |
|---|---:|---:|---:|
| 1 | −960 | −6048 | −10448 |
| 3 | 2909459200 | 23729805120 | 660203246512/27 |

于是

`β=−9092060/3`，
`d=D3−βD1=5400212160`，
`f=F3−βF1=−194741339408/27≠0`。

(I8)首先给用户要求的modp³ pair展开与N7剩余行

`E≡d v1 (mod p)`。

所以该层的det仍零，新增Δ∈pZ_p；这是二阶结构退化，不是整体no-go。第三层进一步给

`E=dv1+p[(K3(p)−βK1(p))v1+f v3]+O(p²)`。                     (I9)

取fixed rational row shear

`F_p=(E−(d/B1)R1)/p∈Z_p³`。

保留未知scalar k_p∈Z_p后，

`F_p≡k_p v1+f v3 (mod p)`。

具体 `k_p≡K3(p)−βK1(p)−(d/B1)D1 (mod p)`。β、d/B1及全部有限常数的分母在p>37时为units，K1,K3在Z_p，所以该shear确实integral；没有假设unknown scalar消失。

exact determinant身份为 `Δ/p=det(R0,R1,F_p)`。现在未知linear项由重复v1的det严格消去，得到

`Δ/p≡B1 f det(w,v1,v3)`
`     =7763789492179875/4 (mod p)`。                           (I10)

从p-divisible Rm到E、再到F的每次除p都有(I8)的整性保证，不把modp rank当全部next layers。对(I1)指定的p，右边是p-unit，故valuation exact1。固定整数只有有限素因子，素数集无界，遂证明无限Δ非零。证明没有使用recurrence边缘系数或有限Δ0来替代无界命题。

## 6. 有限cert的作用与还没有证明的事实

所有全p乘积展开、error bounds、reflection filtration及exact row shear都是上述纸面证明。为核固定大常数，本任务预先设计并保存一个 [Fraction producer](certify_pade_residual_constants_round224_20261008.py)，只对m=1,3、a=0..m、harmonic orders1..3和Taylor degrees0..4作有限有理运算；没有prime输入。唯一运行退出0，保存 [完整JSON](pade_residual_constants_round224_20261008.json)，并实际FULL读producer/输出。程序核I7的固定3×3矩阵及B/D/F/β/d/f/I10常数，不负责证明(I1)的全p量词。

运行与原件身份单存 [ledger](pade_residual_constants_ledger_round224_20261008.md)。数学程序实际1次；未运行第二verifier或扫描，未重跑222/223。独审仍须实际检查全p证明，有限PASS不能代替它。

本轮支付的是目标系数Δ的无限非零及指定素数尺度actual rank3。它使Δ生成级数非多项式；**不推出非有理、最小微分秩、J_r或H_g的无限非零，更不推出ζ7无理**。actual G-function存在性由223另付，本稿不进口相近Zudilin族operator或新数值定理。没有给full prefix最优分母、共同图能量或strict CDT费用。

## 7. 实际读域与最终保存

本稿是223同一P7 source的继续。所需finite-field/谐和/central-binomial同余已自足证明；未新增primary阅读或下载，不冒称FULL重审222/223原论文。没有新文献空目录或重复archive工作。

只写本NEW224数学稿、预设计producer/结果/ledger；旧稿、main、manifest不改。全文含七节/I1–I10；作者保存后实际FULL复读并核metadata，身份另向Root登记。作者自读、有限常数PASS与独审各有独立scope。
