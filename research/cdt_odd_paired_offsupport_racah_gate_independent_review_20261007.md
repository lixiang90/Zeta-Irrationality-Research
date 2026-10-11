# 支集外 Racah 门槛：独立全文审阅

2026-10-07，NEW，审阅者 `/root/scaled_root_finalize`。实际完整阅读 [最终候选](cdt_odd_paired_offsupport_racah_gate_20261007.md) 七节 O1–O25，物理 SHA256 `a3b89d1a210fa2a07fe55ab712e735447806d813821dcecf33810737f50c9e85`。本轮540既存冻结记录不变；本独审及审阅者本轮自身工作均无数学 producer execute/import/rerun，没有新辅助素数单位数据。只作全文纸核和原件读取。

结论：一般域秩定理及奇数维极小秩分类、实际 Racah 正规差分边界、完整 Phi radical 同构均通过。准确新结论是 r≥2 的 rank E≥ceil(r/2) 与 corank Phi^[2r]≤floor(r/2)，没有推出 E 或 D_high 非退化。

## V1. 有限 associated functional 与二类多项式

实际完整文本读 KS 报告 PDF28、29、30共3distinct页，定义、norm、monic recurrence 与 Eq1.2.5 差分式均已核；没有重复下载或宣称170页全文读完。冻结第四族 M6–M9 的正交和已证 units 作为输入，本审不重新执行其旧 producers。

O9 的 A_j/B_j 使用相同 associated recurrence，f_(n+j)=f_n A_j−b_n f_(n−1)B_j 逐项归纳正确。非零 b 阻止原相邻 f_n/f_(n−1) 共根；不需要 ordered nodes、实域 positivity 或 characteristic0。

在 K[z]/(A_R) 上，乘 z 的两相邻 entries 对 diagonal norms gamma_j=product_(h≤j)b_(n+h) 自伴随；gamma_(j+1)=b_(n+j+1)gamma_j 准确。mu(h)=〈1,h〉 由自伴随乘法给 mu(fg)=〈f,g〉，于是全部 finite leading profiles≤R 单位，mu(A_j z^k)=0 对k<j、最高 moment gamma_j非零。没有假定无限 norm 正常或 eigenvalues 可分。

O12 的 B_j=Pol(A_j C_mu) 的 B0/B1 和递推一致；额外 polynomial constant 是mu(A_j)，j≥1时为0。Laurent tail首项 gamma_j z^(−j−1) 来自准确 moment 条件。该 formal expansion不是实变量或复变量渐近。

## V2. 低秩迫 proper 的节点数与 degree 窗口

取 q=rank E、2q<R。前q+1列的关系最高指标l≤q，关联 A degree l、B degree≤l−1。gcd degree e，starred t=l−e，删g为零的节点后 M≥R−e。原相邻 pair 非零和 starred coprime 保证每行准确是非零 scalar times (B_*,-A_*)；允许某个单一 evaluation 为0，未除它。

对j≤q+1，Delta_j=A_j B_*−B_j A_* degree≤q+t=2q−e<R−e≤M。故 polynomial evaluation在此窗口单射，q+2列至少有两个恒等关系。任何关系对应 (A',B')=(hA_*,hB_*)，且 B'=Pol(A'C_mu)，所以Pol(hR_*)=0。若R_*有 polynomial part，则非零h乘它的最高 Laurent power不能取消；于是只剩零关系，与两关系矛盾。proper 是低秩和真实节点数共同逼出，未预加 Padé 假设。

R_*=0 或首非零负项晚于z^(−t−1)，都会使非零A_*与degree≤t的全部测试 moment正交，违背finite (t+1)-profile单位。故R_*=c z^(−v−1)+…，0≤v≤t，c非零。

对j≥t，A_*(A_j C_mu−B_j)无 polynomial part，因此Delta_j=−Pol(A_jR_*)。j≥t+1的准确degree为j−v−1。选择j≤min(R−1,R−e+v)使degree<M；各degree不同故单射后独立。数量准确为 R−t−1−max(0,e−v−1)，给O19，进而2q≥R−1。当前2q<R、l≤q的条件保证计数所需窗口存在；一般q≥R/2时无需这套proper论证。

## V3. 奇数维极小秩的双向分类

R=2s+1、q=s时，精确计数若e≥1则q≥R−l≥s+1，矛盾；e0时t=l<s同样矛盾。因此e0、t=l=s。所有Delta columns degree≤2s−1<R，完整evaluation单射，polynomial nullity准确s+1。

全部关系的h degree≤s；Pol(hR_*)=0 iff degree h≤v。反向每个此h都给真实关系：A'=hA_*在degree≤2s的A-basis内，Pol(A'C_mu)=hB_*。故关系空间为v+1，迫v=s。associated正交的唯一性给A_*/B_*为A_s/B_s同一常数倍，节点原关系遂为f_(n+s)(z_i)=0。

反向中央零点时，A_s/B_s coprime由相邻Casoratian恒为非零b乘积证明；R_*=gamma_s z^(−s−1)+… 。j<s时用另一余项的polynomial part得degree Delta≤s−j−1；j≥s时degree≤j−s−1。全部≤s−1，给rank≤s；j=s+1,…,2s的degree准确0,…,s−1又给rank≥s。故O8确为双向分类，非单向必要条件。一般域上极小秩可出现，作者没有用准定性免费推满秩。

## V4. 真实 Racah 差分边界与完整 radical

KS Eq1.2.5 代入 alpha=gamma=−4r−1、beta=−10r−1、delta=6r，B(x)的三个因子均x−4r，另为x+2r；D(x)为x(x+6r)^3。置k=x+r即准确O22。lambda=x(x+2r)=k²−r²，degree eigenvalue n(n−14r−1)，符合O2。

在k=r−1≥1，B0=−(4r+1)^3/[2(r−1)]为单位；D0的分母2(r−1)(2r−3)亦为单位，r2时仍正规。若omitted i²节点全部为零，y(r−2)=y(r−1)=0，实际差分式迫y(r)=0；而R_n^L(r²)=1，矛盾。负x=−1使用的是同一 polynomial/rational身份，分母正规后约化合法。未在k0的singular combination代入，未忽略halfjet或用支集外real positivity。

实际n=2r、R=r的associated窗口至p_(3r)，完全在已证degree≤4r的normality范围。even r由一般floor bound，odd r≥3再排除中央零点机制，准确得到ceil(r/2)。r1不在新增加强范围，未添加有限素数unit实验。

O24独立核：f=mW degree<3r，Phi(WT)=L(fT)=0对degree T<2r，完整L正交norm单位使f恰在span p_(2r),…,p_(3r−1)。同时f vanishes on全部omitted roots，即coefficients在kerE。反向distinct roots factor theorem给m整除f，商degree<2r，恢复实际Phi radical。整个同构不除未知E、Phi norm或principal block。因此corank Phi^[2r]=r−rankE，rank Phi^[2r]≥2r−floor(r/2)。

## V5. 通过范围与剩余问题

a3b89 O1–O25通过实际全文独审和上述primary公式核查。实际进展是全辅助域支集外门槛至少半秩、奇数维极小秩严格排除、complete Phi的准确缺陷同构；并非重复既有determinant identity。

仍未证明rankE=r、Phi^[2r] unit、真实D_high同样rank下界或unit、restricted-H unit、原固定M5无限unit、fixed rational source无限成功、whole-X无限非零或足够strict margin。restricted subspace可另生radical，不能把complete Phi corank控制直接传给r维high compression。2rankE<r时逼出的proper条件也不能无偿移到当前可能的中间秩kernel。无新ζ/L/Catalan无理性或LI、无Lean、无数学producer执行。

作者实际全文读本审与最终主稿回读后，可另作一向FINAL来源收据；本审不预先声明未来读取已完成。
