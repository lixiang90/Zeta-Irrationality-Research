# 第223轮：固定 Padé packet 的无界素数尺度残差与非零门槛

2026-10-08。本文给两个显式无界素数尺度的完整首残差定理和局部整性改进，**尚未证明 Δ_r 无限非零**。首残差恰为秩2或秩1，堵住的是相应首层直接取非零行列式的捷径；不是整个 packet、所有深层或所有素数尺度的 no-go。没有素数/参数扫描或辅助数学程序。

## 1. 实际 FULL 输入与不变的全素数幂基线

实际 FULL 读 [222数学包](relation_source_architecture_global_round222_20261008.md)，11908 B，SHA256 `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`，全部七节/P1–P15；以及 [222有限补充](pade_target_head_nonzero_round222_20261008.md)，3006 B，SHA256 `c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f`，全部两节、表格及量词。未重跑其 producer/verifier。Δ0>0 是已付有限事实，不代替本轮目标。

沿用偶 n 的 R_n、c_(j,k,n)，记

`S_(j,n)=Σ_(k=0)^n (−1)^k c_(j,k,n)`，
`A_(s,n)=κ_s S_(s−1,n)`，`(κ3,κ5,κ7)=(3/2,15/4,189/32)`。

Δ_r 的三行依次为 n=2r,2r+2,2r+4，三列为 A3,A5,A7。全素数幂基线仍是 P7–P9 的 `d_(2n)^(6−j)c_j∈Z` 及 P13 的 Δ/Ξ/H 分母。本稿只证明以下特定 n 的局部估值；不把它当作整个前缀源整格指数或 CDT τ。常数尾 C_n、固定2幂及其余素数的费用均未删除。Root另推导的 d_n sharpening 不作为本稿未读证明的输入。

所有局部计算取大奇素数 p。用 `H_b=Σ_(i=1)^b 1/i,H_0=0`；出现的小 b<p，因此这些数在 Z_p 中。完整正则化乘积是222 P7，系数次数 h=6−j≤5；下文支付 numerator 与 denominator 中所有 p 倍距离，非只取 c6。

## 2. n=p−1：最高系数的 carries 与完整下一层

最高系数为 `c6,k=[binom(n,k)^2 binom(n+k,n)binom(2n−k,n)]^3`。n=p−1 时，两端 k=0,p−1 的估值为3，内点为6。内点正则因子的 h 次系数估值至少 −h，故全部 j≥1 的 c_j 内点在 pZ_p；端点只有一个 numerator p 距离，且其幂为3，denominator 没有 p 距离，所以全部 c_j 端点也整。这与 n<p 时 p-unit 分母相容，不使用 d_(2n) 的 phantom 深度。

在 k=0 端点，唯一 p 因子是 `(1+v/p)^3`。去掉它的 unit 乘积记 Q(v)，其一次系数为

`Q'(0)≡−3H_(p−1)+3H_(p−2)−6H_(p−1)≡3 (mod p)`。

又 `binom(2p−2,p−1)/p≡−1 (mod p)`，可由 `binom(2p−1,p−1)=∏_(i=1)^(p−1)(1+p/i)` 与前一二项式的比例 p/(2p−1) 直接得到。因此

`c6,0/p³≡−1`，`c4,0/p≡−3`，`c2,0≡−3 (mod p)`。

镜像端点的 even j 系数相同、alternating 权也相同。内点不贡献这些残差，故

`A3,p−1≡−9`，`A5,p−1/p≡−45/2`，`A7,p−1/p³≡−189/16 (mod p)`。       (N1)

这些是逐系数完整分层计算；特别 A3 的主项使用端点的第三个 p^-1 numerator 次数乘 unit 一次系数，不能从最高 c6 一项替代。

## 3. n=p+m，m=1,3：两个 p-separated pole 的首层取消和次层

令0≤a≤m，并定义固定有理数

`T_a=binom(m,a)^2 binom(m+a,m)binom(2m−a,m)`，
`L_a=H_(m+a)+2H_(2m−a)−3H_(m−a)`，
`q_a=3[H_(2m−a)−H_(m+a)+3H_a−3H_(m−a)]`。

full pole pair 是 k=a,p+a。其余 k 的 c6 估值至少6：binom(n,k) 至少产生一次 carry，已在其平方后立方贡献6；其他因子不产生负估值。即使所有正则距离的 h 层损失都计入，仍有 `v_p(c_j)≥6−h`，不贡献下面目标列的残差。

对 full pair，写 v=pw。下端 p 距离的完整正则乘积为

`ψ(w)=(1−w)^3(1+w/2)^3(1+w)^−6`；

上端为 ψ(−w)。负 numerator p、正 numerator 2p 和另一 denominator p 全部保留。其余 unit 距离乘积两端均满足

`Q_a^±(pw)≡1+p q_a w (mod p²)`。                              (N2)

这是逐因子的一次展开；unit reciprocal sums 分别为 `H_(m+a)−H_a`、`H_(2m−a)−H_(m−a)` 与 `H_(m−a)−H_a`，带权 −3,3,−6 即得 q_a。完整块 `H_(p−1)≡0`，并未假设更高层 harmonic 为零。

最高值 `E_a^−=c6,a,n` 满足

`E_a^−≡8T_a³(1+3pL_a) (mod p²)`，`E_a^+=E_(m−a)^−`，
`(E_a^−−E_a^+)/p≡8T_a³ q_a (mod p)`。                         (N3)

证明只用小段阶乘展开：`binom(p+m,a)/binom(m,a)≡1+p(H_m−H_(m−a))`；另一个小 a 二项式给 `H_(m+a)−H_m`；`binom(2p+u,p+m)/(2binom(u,m))≡1+p(2H_u−H_m−H_(u−m))`，u=2m−a。最后一式用 `binom(2p,p)≡2 mod p²`，其乘积证明仍只需 `H_(p−1)≡0`。合并三因子再立方得到(N3)。

因 p 奇，两端 alternating 权相反。目标列的 h=0,2,4 为偶数，ψ_h 两端相同，所以 p^-h 的首层严格取消。支付(N2)–(N3)后，令

`B_m=Σ_(a=0)^m (−1)^a 8T_a³ q_a`。

对 h=0,2,4（ψ_(−1)=0）得到完整下一层

`p^(h−1) S_(6−h,p+m)≡B_m(ψ_h+2ψ_(h−1)) (mod p)`。             (N4)

ψ 的0–4次系数为 `1,−15/2,117/4,−653/8,1491/8`，故

`(p³A3,pA5,A7/p)_(p+m)≡B_m (555/16,855/16,189/32) (mod p)`。    (N5)

尤其 B1=−960。奇深度 ψ1、ψ3 已计入；将首层取消直接写成三列主项为零而不付这层，会漏掉实际次层。

## 4. r=(p−1)/2 的完整首 residual 恰为秩2

令 M_p 的第一行为

`(p A3,p−1, A5,p−1/p, A7,p−1/p³)`，

后两行为 n=p+1,p+3 的 `(p³A3,pA5,A7/p)`。全部条目在 Z_p，且 **exactly** `det M_p=p Δ_((p−1)/2)`：这是对原三列乘 p³,p,p^-1，再将第一行除以 p²。

由(N1),(N5)，p>37 时

```
M_p mod p =
[ 0       −45/2       −189/16 ]
[ B1·555/16 B1·855/16 B1·189/32 ]
[ B3·555/16 B3·855/16 B3·189/32 ].
```

第一行与第二行独立：第一项为0与非零，且第一行不零。第三行与第二行比例，故 rank **恰2**。因此 `pΔ≡0 mod p`，得到

`Δ_((p−1)/2)∈Z_p`，对所有素数 p>37。                          (N6)

这是无界素数尺度的严格整性命题，不是非零命题。令 β=B3/B1∈Q，其分母在这里为 p-unit；固定 row shear 得第三行 `R3−βR1∈pZ_p³`。定义 `E_p=(R3−βR1)/p`，则

`Δ_((p−1)/2)=det(R0,R1,E_p)`。                                (N7)

最小下一待证 lemma 是：支付这些 exact E_p 的剩余完整层，并证明该 determinant 对所有充分大 p 非零（例如证明 mod p 的三行独立）。求 E_p mod p 要将 full-pair 展开推进到模 p³，不能复用模 p² 的(N2)–(N3)。本稿没有证明该新 residual 为秩3，也没有假设 p-dependent harmonic/Bernoulli 项自动非零。

## 5. r=p：完整粗细块分离，首 residual 恰为秩1

取 n=2p+m，m=0,2,4，p>11。full clusters 为 `k=a+ℓp`，0≤a≤m，ℓ=0,1,2。由 `(1+X)^p≡1+X^p mod p` 比较系数（即此处所需 Lucas 形式），

`c6,a+ℓp,n≡c6,a,m · c6,ℓ,2 (mod p)`。                          (N8)

v=pw 的全部 p 距离正则乘积恰是 R2 在其 pole −ℓ 的 P7 正则乘积：两组 numerator 各两个 p 倍距离、其余两个 denominator p 倍距离全部保留。于是对 h=0,2,4

`p^h c_(6−h,a+ℓp,n)≡c6,a,m · c_(6−h,ℓ,2) (mod p)`。

其余 partial clusters 的 binom(n,k) carry 已令 c6 估值≥6；即使 denominator p 层全部计算，`v_p(c_j)≥6−h`，故不贡献首残差。因为 `(−1)^(a+ℓp)=(−1)^(a+ℓ)`，令 `U_m=Σ_a(−1)^a c6,a,m∈Z`，便得

`(p⁴A3,p²A5,A7)_(2p+m)≡U_m (A3,2,A5,2,A7,2) (mod p)`。        (N9)

U0=1。222有限证书中的固定向量为 `(-6951213/16,−2983095/4,−546021/2)`；前两 numerator 的 gcd 为9，所以该向量对 p>11 不零。三行 residual **恰秩1**，不是3。

记这三个 integral rows 为 V0,V2,V4，作固定整数 shear `V_m−U_m V0`，m=2,4。后二行均属 pZ_p³，因此

`p⁴ Δ_p∈Z_p`，对所有素数 p>11。                              (N10)

更精确地 `p⁴Δ_p=det(V0,(V2−U2V0)/p,(V4−U4V0)/p)`。该新 determinant 的非零仍未付。只知道首矩阵 rank1，不能将其取成某个固定 rank3 证书；更不能把未计算的后二行除 p 后 residual 当成0或当成独立。

## 6. 递推/零尾替代接口及严格量词

纸面补充一个真正足够的递推条件：若给 Δ 本身的 exact recurrence

`Σ_(j=0)^q a_j(r) Δ_(r+j)=0`，

且 `a0(r)≠0` 对所有整数 r≥0，便可从 Δ0≠0 推出 Δ 不是 eventually zero，从而有无限多个非零项。证明是从假设的零尾逐项向后递推。若 a0 只在 r≥r0 不零，则必须另付至少一个 r≥r0 的非零项；Δ0 不能免费越过早期奇异点。一般 P-recursive 序列允许有限支撑，例如仅第0项为1的序列满足 `rΔ_r=0`，恰在起点有奇异最早系数。

若 A3,A5,A7 真是同一个无奇异三阶 recurrence 的独立三个解，则 Casoratian 满足 `Δ_(r+1)=−a0(r)/a3(r)·Δ_r`；必须先证明 common order3、两端系数及跨奇异点的非零，不能从一般 holonomicity 推出这一式。单列 A7 的非零或负实根性质也不能替代三列外积非零。

目前(N6),(N10)对每个指定大素数都成立，却同样兼容 Δ 最终为零。它们不为目标关系的非退化、非有理性、真实奇点或 strict holonomy gate 提供替代证书。下一步只能付(N7)/(N10)的新剩余矩阵，或完整 recurrence 的 nonvanishing-edge/finite-bridge 条件；本轮不扩展 prime/parameter 搜索。

## 7. 实际 scope、保存与运行账

本轮新数学来自同一 P6/P7 整数乘积、局部 Taylor 层和固定小常数的纸面运算，未新增 primary 引用或下载，未冒称重新 FULL 审222文献原论文。新文献归档目录无需建立空包。使用222有限表作为已认证输入，但未读取/重跑其数学程序。

数学程序0：没有 CAS、prime/parameter scan、PSLQ、矩阵执行或一次性辅助计算；没有调用允许的额外 exact computation。实际工具仅 rg 定位、全文读写与 bytes/hash。只写本 NEW 数学稿，不改222、旧稿、main或manifest。最终保存后作者实际 FULL 复读七节及N1–N10；身份另向 Root 登记，不冒充独审。
