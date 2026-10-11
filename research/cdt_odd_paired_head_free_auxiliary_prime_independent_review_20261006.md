# 配对消头空间辅助素数证明：独立全文审阅

日期：2026-10-06。审阅者 `/root/toric_chow_completion`。本文件 NEW，不修改同行证明或冻结旧稿。本次独审没有执行、import、重跑任何旧/同行数学 producer。

**审阅结论：在明确的两 determinant-unit 条件下，全文纸面推导通过。** 真实 mod p² paired lift、负评价 rank、weak Schur factorization 与 conditional Smith/Gauss结论均成立。五个辅助素数上的十次 finite probes 只作为有限证据；未证明 infinite-unit 条件，也未获得新的数值无理性/线性无关性结论。

## V1. 实际读取的版本与范围

实际全文读取 [辅助素数稿](cdt_odd_paired_head_free_auxiliary_prime_20261006.md) A1–A13，初读SHA bb4eeb14d876bdffb0ae1d0c88bb0d4421a3945ef7be5a1c67f7433e61a8e73a，随后全文复读作者补充固定 source 费用及 probe 参数的最终版本，SHA

`4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b`。

实际全文静态读取作者自有 NEW [probe源码](cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.py)，SHA `256f5f32efa8755a6c3c234d25ed2d5395fbf7e45d9402af569c476bb6c94e42`，及全部 [现有输出](cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.json)，SHA `f8b0f099507d284850fb66ff5236b8e4d5e5d46025ad798c97bca467274ab30a`。全部读取输出完整、未截断；源码只静态审阅，未运行或 import。

本轮未重新读 Lai 的完整25页，不以作者 source scope 冒称审阅者 scope。审阅者前轮实际 primary scope 仅 Lai PDF1–7、17–25共16页，已登记于冻结解析/独审记录。此处模 p lifting、有限域 residue、Schur 和误差费用均直接纸面独核，不从十个 probes 推成一般 m 定理。

## V2. 完整格、negative evaluation 及有限域 annihilator

纸面独核 A2–A5：n=2m、p=9m+1 prime、p>s+1，迫 m为偶数。全部4m个 positive 节点与3m个negative节点分别 distinct，head evaluation split surjective；e_z=d_z/p为unit，2m actual pair constraints满射。因此 actual paired kernel 是 rank4m direct summand，Newton/monomial比较在该 p 因6m<p而unit，未省略 raw-row gcd 或 saturation。

若negative evaluation为0，P=AQ，degQ<3m；positive constraints使Q reflection-even。由4m个节点超过degree得多项式身份，kernel维3m/2、image E维5m/2。并非全ambient的3m，因此 full-space Hermite blocks 不能直接限制。

head Vandermonde annihilator 的μ_z=T(z)/S'(z)与pair antisymmetry给 T reflection-even、degT<m，维m/2。有限域 rational function TP/(AS)次数给 infinity residue为0，negative residues得 A10 的准确 annihilator。独核 W=K S(a)³/A'(a)²、v_T=T A'/(K S⁴)及其 Gram=K⁻¹G₀；ambient D非退化，所以 D|E非退化恰等于 detG₀ unit。没有使用实数正性代替 finite-field unit。

## V3. mod p² lift 与 η=1/2 的必要性

逐项核 e_z 的 factorial product，将其除以 (p−1)!，得到 A16 的实际 modulo p² harmonic correction。反射 z'=4m+1−z 给 H_{7m−z}≡H_{2m+z}，差恰为 I'(z)/I(z)，其中 I roots为 shared negative nodes2m+1..3m−1，I reflection-odd modulo p。

因此

\[
\widehat P_Q=AQ+\frac p2(A/I)I'Q
\]

在真实 pair constraints 上模 p²为0。A/I 是实际整数 factor，因此此式是 Z_p coefficient 的 polynomial、degree<6m；选择 reflection-even Z_p lift Q合法。constraint map 的 Z_p right inverse 将剩余 p² error 修掉，取得真实 paired P_Q。其负节点 evaluation为 pηj modulo p²，derivative为j modulo p；η在shared节点恰1/2，其他为0。该项不能通过任选bare AQ或全空间gauge删去。

## V4. 全误差、Schur 与 conditional Smith/Gauss

独推 tail a−p evaluation=p(η−1)j+O(p²)，derivative=j+O(p)。b-source的主项 p^{s−1}U=−u、p^sV=−(s+1)u。a-source高一层，X-source乘p^s；weak/weak两evaluation有p、derivative-product有p，因此误差至少p³。head j<p的V至少−1阶，乘p^s后至少p^{s−1}，s≥4亦在p² weak-leading之外。strong/weak误差至少p²。这证明A7确实控制了所需所有误差。

由 k_s=s−(s+1)η、d_s=(1−k_s²)/(s+1)独立完成强块消元：

\[
\text{weak Schur leading}
=\frac{uK}{s+1}(H_0-C_sG_0^{-1}C_s^T).
\]

这是原强块−(s+1)uD|E带来正确的加号后，再用 E⊕E⊥分解得到的式子。v_T Gram=K⁻¹G₀、cross=C_s、j Gram=KH₀的 K factors 都匹配。若 detG₀及 detM_s均unit，actual p^s restricted form 的Smith恰0^(5m/2),2^(3m/2)；原form为 (−s)^(5m/2), (−(s−2))^(3m/2)。实际局部basis变换unit，没有未付的p指数。

其det valuation为3m−4ms=−m(4s−3)。scaled whole polynomial的 reduction是非零常数，a、X的相关误差已经被排除，故结论同时覆盖Gauss valuation及X∈Z_p的每个specialization。s5的−17m降低的是指定auxprime上的指数；单个p随n变化只付O(nlogn)，不能改称 all-prime n²收益。若两unit条件在无限辅助p上成立，才可接Dirichlet及固定分母避让推出 infinite nonzero；这项仍未证。

A30–A31 的reflection union有5m+1节点、overlap m−1节点，shared correction保留。two-small-Gram判据不等于一个无条件非退化结论。

## V5. 费用接口与有限 probe 的准确范围

两次Cauchy–Binet可把actual saturated paired determinant接ambient全部2n-minors的共同 valuation下界。向Newton转换须付最大的2n个 factorial，2Σ_{i=n}^{3n−1}v_p(i!)；不是first2n normalizer。大prime范围 sqrt8n<p≤6n，p>6n integrality另述；固定 rational a,b source 分母以D^(2n)统一支付O(n)，不会改变n²率，也没有作为免费gauge删去。此接口未计算matched all-prime主率。

静态核probe：actual d_z/p constraints在modp⁸上以unit pivots求kernel；其Gram由准确scaled harmonic moments构造；逐步unit Schur与p-power division检测Smith。r=0、1的source准确对应a=−r,b=1、X0、s5。m=2,4,8,12,14的现有十cases与文中表一致；全部detected exponents低于precision8，G₀ rank=m/2。未执行这些cases，未称独立运行认证；静态读取只能核代码与输出声明的匹配。

scope无扩大：有限cases不证明全部m、两个unit条件在无限p上成立、all-prime预算或strict margin。本文独审只确认纸面conditional theorem及作者有限probe的准确记录。

实际全文读取作者冻结 [来源收据](../literature/manifest_cdt_odd_paired_head_free_auxiliary_prime_20261006.json)，SHA `1c35ae09a7260786373840ff288f7dec09f210994aa1ca3908edfd5ed048c419`，终稿/首次probe/source参数与实际读取版本匹配。作者的 previous-round Lai25页范围是作者 receipt，未被转写成本文审阅者的PDF阅读范围。本文保存后实际全文回读并冻结，独审没有新增数学producer或PDF下载。
