# conifold算术中心接口的独立全文审核

日期：2026-10-06。quarter_actual_rank独审。只读root NEW稿 §§C1–C7、NEW符号PY和其JSON，不执行/import root、同行或旧数学producer；实际读Fischler–Rivoal出版PDF2–5、9。结论：在文中明确的三个实际jet均属于number field的条件下，完整geometric G-function整模型及其费用上界成立；未发现实质数学缺口。这个审核不证明三个jet代数，也不证明新的数值无理性。

## 1. 实际输入与没有重建的范围

实际全文审阅[conifold稿](cdt_odd_conifold_arithmetic_center_20261006.md)。Ψ=W−π⁴y0/16、PΨ=√x/16及标记实支在1全纯，采用已单列的真实相对周期输入；本次没有重新建构整相对链8C−TΓ、mirror resolution、MHS或higher-Chow lift。本次正面审核的是这个实际全纯germ在新算术中心的完整接口。

初值α0、α1、α2是Ψ(1−t)真正的前三Taylor coefficients；α1的负号和α2的1/2来自t=1−x。W、y0原先有log，不能各自直接取未正则化端点导数。仅α0的算术假设不足以使整个germ有代数系数，文中正确保留其它两个实际jet。

## 2. C2–C3的全尺度独推

手工展开θ=−(1−t)D：
\[
\begin{aligned}
\theta^2&=(1-t)^2D^2-(1-t)D,\\
\theta^3&=-(1-t)^3D^3+3(1-t)^2D^2-(1-t)D,\\
\theta^4&=(1-t)^4D^4-6(1-t)^3D^3+7(1-t)^2D^2-(1-t)D.
\end{aligned}
\]
将P=tθ⁴−(1−t)(2θ³+3θ²/2+θ/2+1/16)逐项合并，准确得C2.1全部五项。最小项tD⁴+2D³在t^ρ上给ρ(ρ−1)²(ρ−2)t^(ρ−3)；左乘(θ−1/2)=−(1−t)D−1/2再给−(ρ−3)，所以C2.2两个indicial均正确。LΨ=0来自(θ−1/2)√x=0；没有把相乘顺序倒置。

设(n)_j为falling factorial。由C2.1提取c_(n+offset)五个非零offset得到：
\[
\begin{array}{c|l}
3&(n+3)(n+2)^2(n+1)\\
2&-(n+2)(n+1)(8n^2+20n+15)/2\\
1&(n+1)(12n^3+24n^2+23n+8)/2\\
0&-(64n^4+32n^3+40n^2+8n+1)/16\\
-1&(n-1/2)^4.
\end{array}
\]
例如offset2为−4(n+2)_4−14(n+2)_3−(15/2)(n+2)_2；offset−1为(n−1)_4+8(n−1)_3+(29/2)(n−1)_2+5(n−1)+1/16=(n−1/2)^4。这是一切n的代数恒等式，不是有限Taylor样本。无offset4，因为最高D⁴系数无constant；所有系数degree≤derivative order+1，因此无更低offset。

A_n对n≥0均非零，c_(−1)=0使n=0同样合法。n=0准确给12c3=β/16+15c2−4c1+c0/16，即C3.2。

给定(c0,c1,c2,β)因此唯一确定形式解。收敛也可不借后续G-function结论：递推各ratio B_n/A_n、C_n/A_n、E_n/A_n及(n−1/2)^4/A_n在n≥0有统一有限界，h_n也有指数界；有限记忆majorant遂给c_n指数界及正收敛半径。故四组标准初值确是实际holomorphic germs。任一L-holomorphic解满足(θ−1/2)Pf=0，局部√(1−t)非零，必有Pf=β√(1−t)/16；holomorphic solution空间恰四维，初值map(c0,c1,c2,β)为同构。

## 3. local Nilsson–G basis到canonical germs的完整论证

FR PDF4/印刷290的André–Chudnovsky–Katz陈述适用于geometric G-operator在代数singular point：local basis由G-functions乘有理powers和log polynomials构成，coefficients可取Qbar。L在新点的exponents0,1,1,2,3全部整数，所以这里的power classes均为整数。

为详细核准正文的“以初值规范化”步骤：将一个完整五维Nilsson–G basis的任意C-linear组合写出。要求所有正次log系数为0，并要求无负次t主部，是其五个线性组合系数的一组Qbar-linear方程。即使写成无限方程，row span维数至多5，可取有限个独立方程定义同一空间。因此四维holomorphic子空间在Qbar上定义，可选Qbar-coefficient basis。取消log和有限负次主部后，每个basis函数是finite Qbar-linear组合的G-series及整数shift，故仍为G-function；G class对这些操作闭合。

该basis的(c0,c1,c2,β)矩阵在Qbar：β=16Pf(0)=192c3−240c2+64c1−c0，也是有限Taylor jet的Q-linear函数。§2已证这个map可逆，故其inverse也在Qbar。以四个标准initial tuples归一后，得到正文的g0,g1,g2,h；都是G-functions。C3.1再表明其coefficients实际上在Q，而不是必须使用可能超越的全局connection constants。

因此此处能直接对原L所消去的四个holomorphic germs用μ=5；没有将一般去log parts（通常只能安全用μ²−1）误说成原L解。FR PDF4的一般μ²警告在本文的明确holomorphic子空间归一化后不构成缺口。

## 4. geometric条件、分母定理及全部地方

FR PDF2/印刷288明确将geometric differential operator定义为Picard–Fuchs operators的factors之products；PDF3/印刷289 Thm2明确给无条件版本。P是冻结识别的four-quadrics CY PF因子；θ−1/2是有限double cover u²=x的rank-one finite-character因子（H0的sign summand可见这个代数解）。故按原文定义L=(θ−1/2)P是geometric，平移x=1−t也保留。这个operator-class判定不需要先有某一relative chain的higher-Chow regulator lift。

FR Thm1不要求给定annihilator minimal；μ=5合法。其b可取local exponent分母的LCM，C2.2给b=1。对四个finite rational G-germs统一选b0、C即可得到C4.1的D_(n+b0)^4 C^(n+1)整化。虽然原定理说algebraic integer，此处系数为Q，所以实际是Z。

三个αi∈K时，取固定d0整化它们，C3.3准确给C4.2。反过来Taylor系数全代数必使前三项代数。因此缺口是这三个实际initial data，而非一个formal rational forcing或只有endpoint α0。正文不声称这些初值已经代数。

FR PDF9/印刷295 §3.4显式用C^(n+1)承担有限坏素数的线性n valuation亏损。有限prime support不能删除这个指数项。prefix采用D_(N+b0+3)^4 C^(N+4)准确涵盖D^jΨ（j≤3）的c_(n+j)；derivative factorial ratio是整数。加大C还可整化√(1−t)全部binomial coefficients。六行model在K(t)上derivation closed，t=0的regular singular companion仍保留实际初值，正文没有以除t私自丢掉它们。

PNT给logprefix≤(4+logC)N+o(N)；fixed b0,d0不改主率，C改主率。正文没有把这个row-wise denominator bound叫作已优化的CDT transport，也没有未经核证将六行数目设成actual independent rank。上述界在这些范围内通过。

## 5. 只读符号证书与结论范围

实际读NEW PY：它独立构造θ powers、operator coefficients、两个indicial、all-symbolic-n五个coefficient identity及首项；没有import任何旧或同行producer。实际读JSON passed及stored coefficient formulas，与§2独推一致。本独审没有执行脚本，所以JSON是root实际运行的记录，不冒认本代理的新增checks。

读到的固定bytes SHA256：

- root MD：`10c1e882a7cc75b2f8b6be82ed6c241ec3900db07109ff144c041cc734f3e7b0`；本次读完整C1–C7。
- root PY：`f2f0e3e9ffb785abb5f5a315590f0885f0f5964846975d1101c98b170f6236d1`。
- root JSON：`7bc10a6760d84c69f879b0c1dbee77a00b3bc3c647edb27d91aee2ee734fa911`；实际只读。
- FR出版PDF：`c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68`，12页；本次实际read5页（2–5、9），非通读12页。
- root FR来源manifest：`eba2c4f8ea07f150c673a6190afe6c3a86c8815e858e8174981c5ca999f47b84`；只读，不执行下载工具。

通过的是真实全纯period germ在三个jet属于number field的条件下的完整geometric arithmetic-center接口。初值算术、实际C的有效最小值、holonomy leaf capacity、完整Smith/transport、数值ζ/L/Catalan结论均未被此次审阅证明。
