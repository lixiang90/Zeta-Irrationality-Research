# 第225轮：实际主符号与稳定上界独立 FULL 审查

2026-10-08，C 独审。结论 **PASS**。作者已澄清两处“有理系数”术语，最终数学主式不变。审阅者未修改作者稿、冻结稿、main或manifest；本审数学程序 **0**，没有重跑或导入任何证书。

## 1. FULL最终身份与实际范围

实际 FULL 读取初版13914B / `77c429ae5e50ec1037a609147f3366bc8dd3c23d85e3a57783325807da1a08d1`全部八节；提出 S13/S14 的“rational generating functions/germ”应明确指有理系数，避免误称有理函数。作者仅改这两处后，本人再次实际 FULL 读取 [最终数学稿](pade_actual_leading_symbol_round225_20261008.md) 全八节/S1–S19及执行段：**13928 bytes**，SHA256 `ee1d70e843e53090cefc84dd750452e2ee6c954ae79bf674d0ea9f25ffede798`。PASS针对此最终身份。

下列输入全部实际 FULL 阅读，没有输出截断：

| 本地输入 | bytes | SHA256 |
|---|---:|---|
| [来源/两次执行账](../literature/pade_asymptotic_sources_round225_20261008/lambert_reading_scope.md) | 2696 | `4d74ba70edbfad73aea3e28b8d08ba59b1c7645c456986295bcac42648b8425a` |
| [最终producer](certify_pade_leading_symbol_round225_20261008.py) | 5136 | `51822e871272b0aee875042c73aa53be06792a1085bed5d4a97bf525846bdffa` |
| [完整exact JSON](pade_leading_symbol_certificate_round225_20261008.json) | 5526 | `87e412c2184de9c424831dd20e16e0b0b0f4160946a0c63cc69db49331b6f304` |
| [失败记录](pade_leading_symbol_first_run_failure_round225_20261008.txt) | 700 | `ec02cd37b1e751c159e36405cd6602d8e7ae42db3b8518b5d59cb1cde14a27cf` |

224实际operator14482B / `32d41b069e688a3aa4e93c44721fe39a6f4ebe1ce646df7fe902bf660d507efd`和222固定packet11908B / `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`是本人已实际 FULL 读取的冻结输入，本次复用其已审结构，不冒称又全文重读全部历史文件。C225三模态11160B / `37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`为本人实际 FULL 最终作者读，其 Root独审3437B / `2d9fe448e12eeff306dbd7a249c3d35ae750a69f6675fc119d091c79bfe80d35`此前亦已实际 FULL 读；作者读不充作自身独审。

## 2. h-regular连接确属原实际operator

S2–S4有限乘積极限正确：P_j→(−V9)^j，K→−(N/D)³，N+D与ND给g(u)=(1−2u−2u²)(u−1)((u+1)³−2)。这一层单独只给候选，作者没有直接冒称connection。

关键 S5–S7 通过独立纸核。缩放后的a_h、b_h和q=h^−12Y给精确identity。q的所有x-poles收缩到0、1；取固定degree的monic共同denominator后，分子degree至少低2，所以最低h系数仍在∞为O(x^−2)，不是对每个h的界免费取极限。

若r或q有负h阶，最低层确为r_s−gq_s=0。g在0、1的值均为1，故polynomial r_s迫使q_s的两个可能finite poles可去；q_s于是既为polynomial又在∞趋0，只能0，随后r_s=0，矛盾。它排除了缩放principal parts的隐藏blow-up。

真实h=0 limit的r是degree≤5的u多项式。在g六个distinct非零根上与p^j同值，因而准确等于商代数余数。u是unit，g(0)=1保证p的负u幂合法。这连接原R_j及cofactor operator，未将formal saddle roots当actual渐近。

行basis (x−1/2)^(2a)到u^a的det为−1，原各行还带n^(2a)，总指数30。因此n30λ_j→−c_j的符号与幂正确。七c_j均非零给每个λ_j的degree差−30、normalized ratio的O(1/n)，并排除充分大整数的零点；没有给最后异常整数的显式数值。r变量的实际六阶递推和所有五个scalar solutions均沿224完整边界的同一operator。

## 3. 固定商代数算法及谱核验

FULL源码的操作限于degree6 quotient、u逆元、固定9次幂、j0…6幂矩阵及七maximal cofactors；Fraction Gaussian determinant的pivot/换行符号与cofactor kernel检查正确。没有actual sequence输入、n采样或猜递推。完整JSON所列g、u逆元、V、powers、matrix、cofactors、χ、因子及所有checks与源码定义一致。

独立纸核quadratic trace的Lucas recurrence s0=2、s1=6、s_j=6s_(j−1)+3s_(j−2)，得s8=3048354、s9=19704870；q-pair product=−19683，故二次因子准确。cubic V根的symmetric sums为9、3、3，其九次power sum为283965993；三组pair-product的九次power sum为3308931，q-product给常数19683，与三次因子一致。χ常数−3^27及q5系数303690546也独立核过。有限程序支付完整大cofactors，没有被扩成全局h-regular证明。

唯一cubic实根8<α<9、另两根modulus sqrt(3/α)通过其两个critical点值−16V及root product3核实。六个q=−V9分为三个unstable大模与三个stable小模；κ=(3/α)^(9/2)是最大stable模，η=19683是最小unstable模。χ squarefree使limiting companion可对角化，所用sup norm和外幂norm存在。谱norm迭代只给source/wedge的upper，未假设某actual solution有非零top connection。

## 4. weighted Volterra稳定界

实际I的既有θ²<1衰减保证six-state属于B_σ，max(κ,θ²)<σ<1。未来迭代的terminal乘D_u逆后趋0，因为σ/η<1；因此S14的unstable未来和是原actual解的identity，绝对收敛，没有任意抛掉large modes。

在B_ρ，κ<ρ<σ，stable过去和的几何系数和为1/(ρ−κ)，unstable未来和为1/(η−ρ)。按两组向量的max norm得到S15的max，常数无漏因子；B_σ同样成立。取充分大R使两个空间均收缩，stable forcing属于B_ρ，存在唯一B_ρ解且包含于B_σ。实际解已有B_σ bound、同一x_R及相同integral equations，由B_σ唯一性与该解相等。令ρ↓κ确得actual I six-state及scalar的limsup root≤κ。

因此two-A wedge upper与actual I upper给J的S17；finite ordinary/θ derivatives不改变该radius。此证明不支付I exact rate、prefactor、非零small connection或J非多项式。作者限制准确。

结合独立三模态的actual Δ/Ξ主项和不可去点，S19的严格相对radius ratio正确；若只剩S13/S17两个upper则不能如此比较。差分order6、外幂20维没有被混成最小微分/CDT rank，safe12/26与完整背景费用没有免费取消。最小微分模型、共同图、H非有理及strict算术gate仍未付。

## 5. Primary和运行边界

本人此次实际 web 读取 [DLMF2.9](https://dlmf.nist.gov/2.9) §i lines44–159的E1–E8及其完整条件，另读§iii line279的arbitrary-order参考句。该节的实际渐近statement针对second-order，不能当六阶完整basis theorem；作者的norm/Volterra证明自含，未借未读Wimp/Olver/Wong–Li作品。没有下载新原件，亦不登记作者失败的E5/E8 TEX请求为已读文件。

执行账确为 **2=失败1+成功1**。第1次错误19704582在factor assert终止，无JSON；第2次通过固定Lucas九次trace修复后成功。记录明确成功后只改scope metadata、数学数据不变，未第三次运行。本审只静态读取程序与结果，不独立重算全部大cofactors，不隐藏失败、也不将两次算作一次。

本审新增数学程序0：无导入/重跑、CAS、根求解、积分、扫描、PSLQ、Lean或Git。只纸面推导与文档/网页读取、hash及NEW收据写入。最终术语修复已由作者完成，本审不把“有理系数芽”当有理函数。原ζ/L数值目标仍开放；保存后实际 FULL 自读本收据并另登记身份。
