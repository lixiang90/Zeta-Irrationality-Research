# 实际提升L边界与调和和化简的独立核查

2026-10-07，root。实际完整读取[exact-lift-boundary主稿](cdt_odd_paired_exact_lift_boundary_20261007.md)E1–E8、全部E1–E19公式，candidate SHA256 ca43e16f8e3ae6c0c70b3adfa8e4460a877ccdb939ce96675be9e94edee68a79。核查方式为静态阅读与纸面推导，数学producer执行/import/rerun0，辅助单位素数扩表0，Lean0。

**结论：通过，未要求数学修改。** 本稿给的是actual提升边界的精确计算，不是这些明确矩阵的正常性或特殊值新定理。

实际e_z=(z)_(24r+1)/p的阶乘分拆核对：p以下乘积为(p−1)!/(z−1)!，以上乘积为v_z!·∏_(u≤v_z)(1+p/u)，v_z=6r+z−1。因此E3准确等于(p−1)!A(z)E_z，没有遗漏一个head阶乘或primitive约除单位。F_z保留原E-weighted约束，参考A-weighted gauge只在reference中使用。

E5–8的有限residue身份合法：degT<2r、degR<12r使numerator≤14r−2、denominator14r，所以infinity residue为0。所有negative/head节点及差值是p单位，反射T和S'符号把head和准确化成pair差。actual约束除p^d后给R(z)/A(z)−R(z')/A(z')=−κ_z，故boundary的正号正确。head cardinal只在各left head取补偿值，right head为0，精确取消每个F_z；degree<8r且coefficients整，得到char0 actual correction，没有扩大原局部饱和格。

E9的H_(p−1) modp²由full inverse-square sum0和pair展开自足证明：乘2置换非零域元素，1−1/4单位；full square sum为half的两倍；1/k+1/(p−k)≡−p/k²。E10反射端点公式符号均正确。

weak E12中的三项逐个复算。u=4r+z，v=u+2r−1，v'=p−1−u，j=H_v−H_u。E13的exact odd identity确为I(c−t)=−I(t−p)，其对数导数给j(z')=−j(z−p)≡−j−pj2；没有把modp反射误用到p²。三项分别H_u^(2)+j2/2、−hj+j²/2+H_u^(2)+j2/2、hj−j²/2，相加为H_u^(2)+H_v^(2)。故weak defect自动被p²整除，且其除p²后modp的值确为E14；E15真实R_Q的L边界不再含未定提升值。

strong E16保留已知reference的literal divided-p carry；E18的cardinal修正是p倍，保留指定negative reduction，确可逐pair满足参考A-weighted pairing。然后E8回到原actual E-weighted pairing。E19由h'−h≡−j得出，符号与E6一致。此参考选择不删除J4中reference N整体modp²的进位；主稿E7明确保留两者区别。

所有这些单位化与修正发生在ordinary/Newton局部GL接口内，actual最终basis与原S的变换det为p单位；没有额外source或免费全局费用变更。两个normalized derivative correction均在p²，值只在p层，经冻结S12的θ关系只贡献L边界。主稿没有以此宣称actual first pencil regular、固定source无限成功、actual determinant无限非零或strict margin。

审阅未运行有限例子，也未读取任何成功或失败producer来复算。本文只核上述全尺度纸证；最终作者FULL回读和一向来源收据另登记。
