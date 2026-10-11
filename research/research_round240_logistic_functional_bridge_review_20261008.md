# 第240轮 logistic 全泛函桥独立审核

2026-10-08，C，纸面独审 PASS；没有必要数学修正。被审稿
research/global_logistic_whole_functional_bridge_round240_20261008.md：
**9796 bytes，SHA256 a655168bbd86afbacecf29bd91d396c7ce848bd5ea418a3300b71de36a5e316c**。
实际 FULL 读六节 L1–L13及方向部分；目标稿未由审阅者修改。PASS限定本稿新纸证与明确的条件转移，不表示独立认证原仓库数值结论。

## 1. 数学核对

1. **L1–L2通过。** 高为i的矩形顶部方向反向，周期ρ(z+i)=ρ(z)，故边差确为(1−eˣ)I。i/2处ρ的主部为 −1/[2π(z−i/2)²]，留数是 ix eˣ⁄²/(2π)，乘2πi给 −xeˣ⁄²；符号正确。固定高度的竖边由指数衰减控制。Laplace交换可先用 Re(t+j)=j+1/2给绝对可积，再代入 Fourier式并展开正级数。故 k(ζ(k+1)−Hⱼ^(k+1))无遗漏；Bernoulli约定B₁⁺=1/2正确。

2. **L3–L7通过。** t/(t+j)=1−j/(t+j)；奇h=k−2次导数为 jh!/(t+j)^(h+1)，配L2得完整 j cₖ(ζ(k)−Hⱼ^(k))。ζ₂项另给 −c₂+jc₂(ζ₂−Hⱼ²)，包括全部head。多项式商部完全有理。∂ₜ=−i∂ᵧ，分部积分再付(−1)ʰ，最终系数iʰ准确；所有固定阶边界项消失。ρ导数递推的π与−2z项均正确，固定组合有 |W_c|≤C_cρ。该论证不是只在简单极点头上删周期，而是对全部商部/残数的同一泛函身份。

3. **L8–L9通过。** 矩阵是同一 h=3n完整Hankel表。Andréief因子1/h!，t差的固定i相位在绝对值中消去，指数尾支付绝对可积。C_cʰ只加O_c(n)，固定微分阶不改变同一绝对Heine envelope的n²leading外场。阅读原Pointwise与Assembly后确认：其外场只通过同一R_n、指数尾常数进入，归一化S_nʰ/F_n也相同。因此转移范围准确。**−6仍依赖FstarInput及未完整审核的数值证书；本receipt不认证它已被支付。**也不由此转移primitive内容或prime-edge非零。

4. **L10通过。** 残数展开的t⁻²系数是−Σjλ_(e,j)，多项式商不贡献该系数。R_n~t⁻ⁿ故a_e在e<n−2为0，a_(n−2)=−1。左上(n−1)块反三角，符号指数(n−1)n/2正确，rank≥n−1全尺度成立。它排除裸rank1目标系数假设；不证明rank3n、generic determinant非零或任何实际有理关系点非零。

5. **L11–L13通过。** 我从−j的留数独立推得
\[
S_n\lambda_{e,j}=(-j)^e(-1)^{j-1}j
\binom{5n}j\binom{j-1}n^4.
\]
j≤n的残数为0，S_n是整数；整数首一除法给完整商部q_e∈ℤ[t]。e≤6n−2推出deg(tq_e)≤5n−1。Bernoulli全部分母由该范围的vonStaudt–Clausen及B₁⁺例外整除d_(5n)，固定24清微分系数，Hⱼ⁵由d_(5n)⁵清。于是(24S_nd_(5n)⁵)^(3n)Q_(c,n)∈ℤ[T]确含所有determinant系数。p>5n并避开固定阶/系数分母时的p整性也成立。安全模型不等于所需净Gauss费用；F_n内容、内部primepowers及全部残数差仍须独立证明，本稿正确保留这项缺口。

6. **方向限定通过。** 主选3ζ₃+ζ₅不同于已知单独无理性，未从检索absence宣布全球新颖。所需两个准入关是同一primitive模型的费用率和每固定q∈ℚ在无界尺度上的非零；rank增长、有限头与generic非零均未被偷换成后者。241–244窗口及连续两轮核心无进展的停止规则具体；M₀,₁₀仍只是独立条件后备。新数值定理仍为0。

## 2. 本人实际primary范围

实际 FULL 读本轮已存原源码如下；这是源码纸审，不是Lean构建或所有imports审核。目录均为
literature/global_review_sources_round240_20261008/root_zeta23/Zeta32/。

| 文件 | bytes | SHA256 |
|---|---:|---|
| Family.lean | 6874 | 59d46a8462ac426bd393864d849bf4cd0f906399c4c583c9736b10835e289dbd |
| Interfaces.lean | 2788 | 6279a135507e741685a7ba5ea688ad5d5b88044160d088d76c5c23bff3493673 |
| Analytic/Logistic.lean | 10769 | 84390d945a8a9fc78d611c53abf4ee5816f28f87d082909a3d9207769b67d44c |
| Analytic/Contour/Moments.lean | 11604 | 4102b948659135c2a29e08c9a5f8ed0a2051d797f9e0c8d100d09153b5fb9ffc |
| Analytic/Energy/Pointwise.lean | 11375 | d8ff78f11196d57e9738df290215ded015be413c409b9915b24becbac9fa03a5 |
| Analytic/Energy/Assembly.lean | 16096 | 36ada384395b1406458c1e76ab48a94b045f200223cf6825247434e0b1213bc9 |
| FstarDefs.lean | 3177 | 794dd5ed22c9db1ae8ff4e10764c34d3026d4e5b09445fab63c816a0f7ad04b8 |

FstarDefs仅给FstarInput/Points的定义，不提供其数值认证；未读取其全certificate依赖、Greedy/prime-edge证明、Comparator或整个仓库。本receipt没有认证README数值主张、commit/tree的全部内容或远端freshness；Root保存的仓库版本标识只是目标稿的来源登记。采用的L1–L13扩展均另作上节纸证。

数学程序、Lean、Comparator、扫描与新source下载均0；只新增此receipt。保存后实际FULL复读本receipt，身份另报。作者自读不是对本receipt的独立审核；也未把自己的C240作者稿阅读冒充对Root稿的审阅。
