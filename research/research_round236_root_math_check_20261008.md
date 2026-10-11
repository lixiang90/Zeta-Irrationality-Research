# 第236轮 Root 独立数学检查

2026-10-08。纸面检查，不是 Lean 或全仓库认证；没有新数值无理性定理。

## 1. 权4源的完整奇部检查

已实际 FULL 读冻结的 global_catalan_weight4_review_round236_20261008.md（13797 B，cf93376bf4add588566fc577a3cf3bf682b5164dc9b1e02036e1e588cbfbb6a0）。独立从235的有理连接重导：

z=(2−x)/x，q=4/(1−z²)，r=−4z/(1−z²)，L=ell+J，ell=±iπ，J=2atanh z。

S_z=zS/(1−z²)+2(ell+J)³/(1−z²)。令 Y=Odd S，则

Y sqrt(1−z²)=2∫_0^z (ell³+3ell J(t)²)/sqrt(1−t²) dt。

初值 S(0)=−192c4 只进入 even homogeneous solution，故完整 Y 不依赖 c4。背景的奇部依次是0、ell r、2ell J、r(ell³+3ell J²)。这不是把f(−z)换成另一native star叶。

从0沿上半平面避开±1到∞，J=iπ+2/z+O(z^−3)，sqrt(1−z²)=−iz(1+O(z^−2))。因此

(Y sqrt(1−z²))'=−8iπ²ell/z+O(z^−2)，Y=8π²ell log z/z+O(z^−1)。

背景和C(q)系数在这一∞叶均为收敛Laurent级数；非零有理倍只能改变非零log项的有限幂次，不能使它变成meromorphic。若在q4完成meromorphic下降，z局部完整奇Laurent jet须零，延拓至∞矛盾。C6–C10的范围与证明均 PASS。

该结论涵盖这个固定空间内任意次数的有理线性过滤；不排除更大mixed-period矩阵、非线性determinant或新源。图的偶ramification也不是关系敏感填点的证书。

## 2. Jacobi尾块行列式的独立证明

235的A满足 u(1−4u)A'+A/2=−2+8u，A0=−4。故A1=16/3，A_n/A_(n−1)=8(n−1)/(2n+1)，即

A_(1+i+j)=8·4^(i+j) B(i+j+1,3/2)。

以下给全部r的精确值，不仅核r=1,2。取w(t)=(1−t)^(1/2)，monic Jacobi多项式由

R_j(t)=w(t)^−1 (d/dt)^j[t^j(1−t)^(j+1/2)]

除以leading coefficient (−1)^j λ_j得到，其中λ_j=Γ(2j+3/2)/Γ(j+3/2)。j次分部积分的全部边界项为零；这同时给次数<j的正交性。其monic norm为

h_j=(j!)² Γ(j+3/2)²/[Γ(2j+3/2)Γ(2j+5/2)]。

Gram determinant等于∏_(j<r) h_j（monic变基det=1）。记

C_r=∏_(j<r)(j!)² / ∏_(i,j<r)(i+j+3/2)。

直接计算C_r/C_(r−1)=h_(r−1)，C0=1，故beta moment determinant=C_r。再提取每行每列的4幂与8幂，得到

det[A_(1+i+j)]_(0≤i,j<r)
=2^(3r²+r) ∏_(j<r)(j!)² / ∏_(i,j<r)(2i+2j+3)。

r=0取1。若p>4r−1，全部分母及阶乘都是p单位（p为奇素数），所以此det为p单位。此证明不依赖Selberg公式或素数猜想。

## 3. 有限jet窗口的逻辑边界

对h=(p+1)/2、M=N−h+1，residue模型u^h(aA+b)的M个输出，a,b次数≤D。若M≤D+1，b即满射；否则先以b处理0至D，再令r=M−D−1，从a_D,a_(D−1),…选择尾块A_(1+i+j)。上节在p>4r−1时给全部M输出满射。

N=3D+2仅是3(D+1)个系数与N+1个jet数目的匹配，不证明该方形jet矩阵可逆。已实际 FULL 核当前CDT物理50–54页：Theorem3.2.8对derivative-closed实际rank3源给ord≤3(D+1)+C，因此N=3D+C0的完整jet注入可以采用一个固定C0。Lemma3.2.14的tensor版本也明确允许epsilon=0。这里采用已发表零估计，不冒称新零估计。

任何窗口rank/index都须另外支付真实residue身份、没有p²层及完整native support。单独的M维满射不是函数rank，也不是源的实际高阶Padé normality。

已 actual FULL 独审B236最终11134 B，SHA256 b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70及4736 B scope。J1–J10 PASS：I'=E/S给J'=−2J/(1−4u)−2E，移位uE的残差起于h，使两行恰同起点；n≤N<p没有外积分p，也没有内奇分母p²。bg gS项p整；p∤bg时缩放可吸收。m=N−h≤(p−3)/2，所用A各项的奇分母全为p单位。

全部M=m+1输出的onto给完整Z_p系数域kernel指数p^M，不把局部非零minor当完整rank结论。r=m−D时p>4r−1等价3p>4N−4D−3，N=3D+O(1)大D自动满足。Shidlovsky常数固定依g，无需uniform g，不领取临界N=3D+2单射。

CRT模型窗口外保留qE=d_(2N−1)、qJ=d_N d_(2N−1)的安全行格，故全部小prime、高幂及finite heads包含。窗口中的两个尺度各恰给一个p，指数由2(D+1)替换为N−h+1。PNT给window成本N²/4，raw row成本5N(D+1)，改后成本3N(D+1)+N²/4=(45/4)D²+o(D²)，gain15D²/4+o(D²)。bg固定坏prime只须在small N精确和式排除，最终稿已注明。

这些是完整有限jet格的实际模型与上界，不是费用τ。§6将直接BC filtered bridge列第一接口、tensor作为可选实现；条件算量2κ/9=5/2明确未当作已证新判据，范围正确。

## 4. 定量holonomy不能免费绕过已有定性障碍

实际 FULL 读已存CDT ICM版物理3–8页，并实际视觉核物理4页。Proposition2.4的分母为

log|phi'(0)|−tau−(1−gamma)(2/mu−(1−gamma)/mu²)log(1/rho)。

其额外项对mu≥2、0<gamma≤1、0<rho≤1非负，故只减小分母；gamma=1时为零。原文明确在mu→∞恢复定性界。因此不能单靠改用irrationality-measure名称，使235的固定源获得新的定性严格余量。新有限处输入或新关系敏感source仍是另外的任务。

## 5. 检查范围

另已 actual FULL 读 A236 最终11218 B/b99bcb2616a6a2c2fa2640a728464ce209650bce8b3a26e61ca4d3b025b3fe57及其4511 B scope，并完整读 Brown–Zudilin PDF4–5、27–30。独立纠正χ(1/192)=−76799/1769472，核其余试值与三个不交根区间，确认A3–A5符号及投影指数判断。A8的目标系数差54033、常数−8037855/8均正确。最终A10已区分有核整值域与单射cutoff的离散格，不领取normality。

上述为Root独立纸核；C1–C4的原Catalan有限算术证书由代理实际完整阅读，没有在本轮执行。Root只实际完整读Catalan foundations和conclusion，不把代理八节FULL范围归到Root。所有数值/全格结论仍须以本轮正式稿及独审scope的具体条件为准。
