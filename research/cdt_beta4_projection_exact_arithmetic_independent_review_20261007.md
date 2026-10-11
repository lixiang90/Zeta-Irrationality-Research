# 单 beta4 精确算术稿的独立全文纸审

日期：2026-10-07。审阅者：root。审阅对象为[精确算术稿](cdt_beta4_projection_exact_arithmetic_20261007.md)的12节、定理E1–E27、公式(E1)–(E37)。本记录是纸面数学审查，不是 Lean 形式化验证。root 实际全文读取该稿及直接输入单周期模型B1–B29；最终文档版本由专项 manifest 单向固定。

## V1 阶乘比与全素数投影整格

独立设d=u−k、j=u−n、h=n−1−k，检查j+h=d−1。E7中的三个二项式乘积准确恢复原B22的全部阶乘及d^(−r)；其中(d!)^r/d^r=(d−1)!^r，没有遗漏因子。故原阶乘基数逐项是整数，符号E8也由QI(k)、Bk(k)与D′(u)得到。

归一化Taylor系数的每项分母总次数为a，所有非零差≤H−1，得D_(H−1)^a h整性。基数为整数后，统一只需r−1层。该证明包含2、每个p-power及p>H；r=1的空额外块单独成立。β4的二次式/2没有再引入未付费的2层。

## V2 同一列池和有限尾消去

合流Cauchy列的第二列是对v求导，符号为正，普通差型Cauchy determinant总符号为(−1)^binom(2n,2)。按行J,I和列C,K排序，Schur补无额外置换符号。p=[I,−K_J A^(−1)]与原Hermite投影的regular-part约束一致，唯一性由detA≠0得到。

E15的所有T_(v,a),a=2,…,r，由与低周期相同的完整regular-part条件精确相消。留下的simple harmonic尾差与目标对角T_(v,r+1)正确，r3的系数为1/64。对F_k/(z−v)^r的全极点核对也成立：仅留目标r+1阶极点及simple poles，其留数总和为零。本稿未将清投影、清原A和清Schur块重复付款。

## V3 全素数幂后备模型及大prime秩

E16的第一类损失为投影2L_H加差分母3L_H加harmonic尾Lodd_(4H−3)，第二类为对角4Lodd_(4n−3)，取max再付2处固定6层正确。所用4H−3、4n−3略宽于真实最大奇数分母，因此仍为安全界。小素数的所有power没有被首层模型覆盖掉。

p>8n时p>H，T_v没有p分母，T_u只可能含单个奇数p，出现阈值是u≥ceil((p+1)/4)。p q modp的真实乘积分解给rank≤R_p。常数左右GL(Z_p)化简后至少n−R_p行的全部多项式系数可被p整除，因此det(q+TI)的每个系数估值至少−R_p，而非仅某个有理T代入后的估值。由此完整G_n Z[T]模型和leading28均成立。

## V4 p>n的Taylor余项与逐列预算

n≥13、p>n保证p²>12n。Bk(k)为p单位，未正规化Phi_k=QI/Bk²在k附近有Z_p Taylor系数，T_k也p整。若额外u≡k modp，则Phi_k(u)=0，截断余项至少p³；若u≡v∈J且k≠v，Bk(u)^3直接给p³。D′(u)的估值恰eta_(p,v)，所以全部matching分支均至少3−eta，不漏k=v。

其它余类的D′最多损失1，p≥2n时损失0。原q第v列的三类预算分别是generic 2或1、matching eta+1、对角尾4且v≥ceil((p+1)/4)，其max正是E32。这里没有把Phi的非单位常数a_k免费除掉，也没有将投影系数仅p整误当为足够的matching保护。

## V5 leading常数的独立复算

根据列变量y=v/n，交点是3−2x=x/4给x=4/3，以及3−x=x/4给x=12/5；其余分界1、3/2、3、4、8、12正确。E35八段的积分独立得到

\[
6+89/72+83/144+1089/400+273/200+11/8+4+2=771/40.
\]

ceil、floor边界只变O(1)列，prime加权总误差O(n)；p≤sqrt(12n)的全部power以O(n^(3/2)logn)=o(n²)付款。PNT的theta与partial summation足够支撑leading，未使用素数表或数值积分。有限小n保留G_n不影响渐近。

因此对同一真实E、固定beta4=a/b，有完整整数身份b^n Ghat_n detE∈Z；仅在另证detE≠0时得−(771/40)n²−o(n²)−nlogb的下界。这个结论是费用上界的改进，不是实际非零性或最终严格差额。

## V6 审阅结论与边界

E1–E37全文纸审通过，没有实质数学修正请求。原单周期矩阵、投影、有限尾和完整det多项式保持同一对象；全部prime及prime powers有明确支付。新的数值无理性定理仍缺无限尺度非零性和足以超过19.275的同对象实处衰减。本审阅不将形式monic、constraint块可逆、有限一个prime seed或旧Catalan解析常数当作缺口的证明。

本轮root未执行数学producer、prime表、guard或Lean。作者收审后应最后全文回读；最终版本统一归档于单向文档manifest，不建立额外循环回执。
