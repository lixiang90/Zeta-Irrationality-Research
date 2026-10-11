# 第224轮：固定目标外积无限非零的第二份独立审阅

2026-10-08，A。对B最终稿作实际FULL读取及独立纸面核验，结论：**PASS，无必要数学修正**。这次检查不采用Root的PASS代替自己的证明检查，也没有执行有限常数producer。未修改任何被审输入、旧稿、main或manifest。

## 1. FULL身份和检查范围

| 本次实际全文读的输入 | bytes | SHA256 |
|---|---:|---|
| `pade_infinite_nonzero_residual_round224_20261008.md`，七节/I1–I10 | 10833 | `0c9fc5eece684d709e0d4a3ad787968b97af80b10f99e7b4b9f14d33fd7d039b` |
| `certify_pade_residual_constants_round224_20261008.py`，全部producer | 4698 | `b6cd01f1c99f63d6123b725efc01fbef78f48c1ae924aee7f4f3828d3b4ffac6` |
| `pade_residual_constants_round224_20261008.json`，全部local及global输出 | 2994 | `59b76b4e0678d1c4c265c05c5310e55a0f804feddd84024c0c6eba9e25034beb` |
| `pade_residual_constants_ledger_round224_20261008.md`，完整运行账 | 1664 | `96bc45b181877f10b6b984002d79de8a2f755f734cc03cc2e13bc23317e7ecdc` |
| 223输入 `pade_infinite_nonzero_gate_round223_20261008.md`，七节/N1–N10 | 10073 | `f12f19984ebdcff427ac336f48869057e48d57353b28e0ea1b620252d2889931` |

路径均在`research/`。222原分式11908B／`35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`与有限校准3006B／`c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f`为本人既有实际FULL读身份，本次复用。有限Δ₀和任何递推存在性均不参与本次无界量词的证明。

## 2. 全p展开、完整errors及signed unit block

在F_p中用乘法重排证明H_(p−1)^(2)、H_(p−1)^(3)为0；逐项1/(p−i)=−1/i−p/i² modp²再给H1=0 modp²。这些层足够支付全部完整blocks及binom(2p,p)=2 modp³；没有偷偷使用modp⁴消失。L=0,1,2的partial block直接展开，I2准确。

最高系数的small factorial log层依次为L_a及−M_a/2，立方后p²项恰为d_a=(9L_a²−3M_a)/2。更高层e_a(p)留在Z_p，T_a对所取大p为unit，故其定义不添非法分母。coarse R₁在pole0的六阶系数为−8，I4前−T_a³因此与actual c₆的8T_a³精确相容。

独立重组unit距离：负numerator范围为a+1,…,p+m+a；正numerator为p+b+1,…,2p+2m−a；denominator为−a,…,p+b，全部删除p倍距离。first、square、cube分别保留负距离的负、正、负符号。得到

\[
\lambda=-3P_{p+m+a}^{(1)}+3P_{2p+2m-a}^{(1)}-9P_{p+b}^{(1)}+9H_a^{(1)},
\]

其中P为deleted-multiple prefix；代入I2正好给q_a与ℓ_a。square和cube同样准确给ρ_a、ν_a。特别denominator负距离的cube符号没有遗漏；α、η及第三层linear/quadratic未知数都保留。

I6的p⁴error在两个coarse poles的regular germs均有效：每个unit因子的normalized次数h系数含p^h；z=−1+w时常数1−p/d仍为unit，且改写后的w因子仍含p。高degree尾在p-adic意义逐系数收敛、全部落在p⁴Z_p。固定coarse R₁的Laurent系数分母仅固定2幂，取h≤5不损失该p⁴精度；normalized R_m再除p，error准确为O(p³)。

其余partial clusters因binom(p+m,k)的一次carry，最高c₆估值至少6；这里全部非零距离绝对值<p²，故h层至多损失h。于是p^h c_(6−h)∈p⁶Z_p，normalized R_m除p后仍≥p⁵。没有将这些项当exact零，也没有因只看最高pole漏掉目标h=4、2、0。

## 3. Reflection、固定常数及两次exact shear

coarse反射z↦−1−z支付偶j的Λ_j只看polynomial的odd part。二阶的odd coefficient为γ−δ=d_a−d_b；三阶的odd part为未知integral scalar乘y，加t_a y³。q=3(L_a−L_b)及γ−δ identity均独立纸核。故I8中的K_m(p)确实容纳所有未计算深层，cubic方向F_m没有被unknown scalar污染。

用ψ=(1−z)³(1+z/2)³(1+z)⁻⁶直接展开，独立核ψ₀,…,ψ₄、v₁、v₃及det(w,v₁,v₃)=1148175/4096。有限常数表亦另用mirror pairs手算，未运行程序。例如m=3的两个weights为64000、373248000，得到

\[
B_3=2909459200,\quad D_3=23729805120,\quad
F_3=24522953472-1916497232/27=660203246512/27.
\]

m=1给B₁=−960、D₁=−6048、F₁=−10448。因此β、d、f与I9一致，且

\[
B_1f\det(w,v_1,v_3)
=637875\cdot12171333713/4
=7763789492179875/4.
\]

FULL producer/JSON只认证这些有限常数，与此纸核一致；其有限PASS不负责全p量词。

exact行缩放给det(R₀,R₁,R₃)=pΔ。I8支付R₃−βR₁∈pZ_p³，故E定义合法且Δ=det(R₀,R₁,E)。接着E−(d/B₁)R₁∈pZ_p³，F_p为integral行，并有

\[
F_p\equiv[K_3-\beta K_1-(d/B_1)D_1]v_1+fv_3\pmod p.
\]

所有fixed rational shear分母对p>37为units。再次exact取det得Δ/p=det(R₀,R₁,F_p)。unknown K₁、K₃由重复v₁的det**严格消去**，没有假设它们为0；只需R₀≡w、R₁≡B₁v₁，便给I10。各次除p都有完整上一层整性支持，不由modp rank免费推出。

## 4. 量词、结果边界和本审运行账

因此对**每个**p>37且p不整除固定整数7763789492179875，Δ_((p−1)/2)/p为p-unit，valuation恰1。固定非零整数只有有限素因子，被排除的小p亦有限，故留下无界、无限的素数集合与不同r，确证无限Δ非零。这个结论不是有限常数实验的外推，不需要recurrence首系数处处非零或finite bridge。

量词仅用于原三列/相邻三行的Δ；并未认证Ξ、J或H_g的无限非零、非有理性、最小rank、真实主奇点、strict CDT门槛或ζ(7)无理性。nonpolynomial的Δ生成级数也不自动非有理。这里的指定prime-scale valuation不是full prefix最优整格指数；固定2和其他素数费用没有被删除。

本次第二独审新增数学程序运行数**0**：未运行B producer、自己的224producer或任何verifier，没有prime/parameter/order扫描、CAS、数值积分、矩阵程序、PSLQ或Lean。常数和全p证明均为纸面复核。本人224主构造此前独立run1的账保持不变，不把它计作本审验证B。工具只做全文读取、metadata/hash及此NEW收据写入；无新primary阅读或下载，未冒称FULL原论文。

本收据保存后实际全文作者复读并另报bytes/hash；它是被审数学稿的第二独审，收据自己的作者自读不冒充第三独审。
