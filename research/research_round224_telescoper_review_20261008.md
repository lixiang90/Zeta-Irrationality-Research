# 第224轮共享六阶递推：Root独立全文审阅

2026-10-08。独立审阅最终稿 [共享算子](pade_centered_even_telescoper_round224_20261008.md)，14482B，SHA256 `32d41b069e688a3aa4e93c44721fe39a6f4ebe1ce646df7fe902bf660d507efd`，实际FULL七节/T1–T18。结论 **PASS，范围为显式非零共享递推、完整半直线边界与外积差分系统；不认证最小微分秩或严格CDT比较。**

## 全局有理恒等式

独立核中心移动 `(n,k)→(n+2j,k+j)` 的两组三重numerator Pochhammer以及两个九重denominator Pochhammer；所得 P_j 在 z↔n−z 下对称，两个pole家族为−i、n+i，i≤j，最高九阶。单位k移动的K=A/B与v无关，两个最高degree均12，K在无穷远趋于−1。这里对n的步长为2，不能直接称普通n-shift六阶。

正pole从i=j向1消去时，已构造 q_(j,i+1)(z+1)唯一可能贡献当前pole；其他较旧项在那里regular。除B(z−1)在当前点无零，最高九阶principal part只需0…8 normalized jets，定义实际可算。最后多出的z=n pole被A的九重零支付。随后 Y⁺(z)+Y⁺(n−z+1) 的反射身份把负pole亦全部消去，两个Y的z⁻¹首项互消，故Y=O(z⁻²)。D_nY 的degree至多10，对称多项式恰落在六个基向量 `(z−n/2)^(2a)`，a=0,…,5。未丢弃负pole、余下无穷远多项式或低pole项。

6×7余项矩阵的交错最大minor给全局Q(n)上的cofactor kernel。固定n=6的七个minor皆非零，因而λ₀、λ₆均为非零有理函数，这支付全局算子的非零性和r变量order6；不支付最小阶。有限D₀^102及D₀^612只用于明确清denominator，零点和小r以多项式前缀支付，不假设整条递推leading coefficient处处非零。

## 双边和半直线边界

从恒等式及K∞=−1，若Qcal有正degree polynomial growth，右边最高项为−2cz^d，与左边有界矛盾，所以Qcal∞=O(1)。可能的有限pole在 n+i、1−i，i≤6，阶≤9；z=0处由B(z−1)的九重零消去。对n≥6，原R的相应三重零使 H=v⁶R 与Qcal相乘在v=0 regular。双边尾部一致O(v⁶k⁻⁶)，因此整个整数区间telescoping和v-jets交换均有具体边界支持，而非免费形式求和。有限S与双边和差O(v⁶)，故0、2、4阶jets以及A₇、A₅、A₃共享λ。

T17的半直线是本次审查要点。去掉(-1)^k v⁶后，令t=−z得到

`Σ_j λ_j(-1)^j R_(n+2j)(t−j)=−Z(t−1)−Z(t)`。

独立核交错求和的有限边界为 Z′(6)−(-1)^M Z′(M)。z=−6不在有限pole表内；n≥6时R在t=6有三重零，所以Z′(6)=0。无穷远Qcal有界及其有理导数衰减支付后端0。左边j≤6，移动后的下端u≥1；遗漏u=1,…,6−j全是R_(n+2j)三重零，导数亦零。因此恢复完整I_(n+2j)，并通过已付完整身份 `I=ΣA_sζ(s)+C` 得C共享λ。此步不假设ζ值线性无关，不把完整有限尾C替换成双边period。

## 有限程序独立检查及范围

实际FULL读producer9628B、最终JSON26796B/`a47a933aca74e035b49233d1f7cbd7106d770f679f5840934cdbfcfc69e4bbd0`以及实现来源范围2886B。producer固定n=6，从已证明六维余项构造矩阵，额外节点只核已付多项式，不是序列猜递推。JSON第一次批读被输出预算截断，随后已单文件重新FULL读取；初次截断不登记FULL。

Root另外保存并执行一次 [独立Leibniz verifier](verify_pade_telescoper_minors_leibniz_round224_20261008.py)，逐minor用720项定义式求和，共七个6×6 determinant，未采用producer的Gaussian elimination，未运行或导入producer。[独审输出](pade_telescoper_leibniz_review_round224_20261008.json)实际FULL读，确认七个有符号minor全部匹配、全部非零且cofactor kernel严格为0。**只核保存的固定矩阵，不替代全局有理principal-part推导**。

由r-companion的∧³得到具体20×20差分系统，(0,1,2) coordinate分别给Δ、Ξ及固定有理g的H_g。二十一条输出row线性相关给order≤20 scalar差分算子。这里20是差分状态维数；不是生成函数的最小微分阶、CDT cyclic/micro秩或实际arithmetical holonomy上界。矩阵中的r多项式会转成θ-operator，最小微分模型仍待单独支付。

全局证明纸核及Root有限独审1次通过；A producer本轮此前1次，两者范围独立。未新增其他数学运行、CAS、order/parameter/prime扫描、PSLQ、Lean或旧证书重跑。没有实际阅读A列出的实现网页，以实际FULL来源范围为边界，不登记未读原件为Root primary FULL。只新增本审阅收据，不修改被审稿。保存后实际全文复读，身份另行登记。
