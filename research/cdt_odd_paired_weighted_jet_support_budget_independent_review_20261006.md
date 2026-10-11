# 实际 weighted jet 支撑预算的正式独立审阅

2026-10-06；审阅者 quarter_actual_rank。NEW 独审文书。全部旧/同行 mathematical producer 仅读，本审阅无执行、import 或 rerun。一般线性代数与局部格证明独立纸核，不以作者有限证书替代全尺度定理。

## I1. 实际版本、读取范围与执行区别

实际完整读取 [root NEW weighted稿](cdt_odd_paired_weighted_jet_support_budget_20261006.md) sections W1–W10、equations W1–W14，无截断。初读物理SHA为 d8f6724c50d80e398aa59ecc4f9e2470033ac1bab46bc23117dc40e4f9810dc6；作者随后仅将W10计划语句改成实际首次PASS及有限case范围，本人已实际完整补读最终W10。最终稿 SHA：

b9535b241ef67af5d5ce82aaa8bd5073e844dd5a9b5701f12669b1cc9a5211cb。

完整静态读作者NEW PY，SHA36112ffcb950479e89a1744ee35721770f8216cd96b7352d7c9b785ad5e40932；实际完整读NEW JSON，SHAbb3ceac4bb22ac030fbf8ed43337738b70b0af3fdf7f687147862e5f1b7a4eba，包括所有三case、全部allocations及全部selected actual jet-row labels，输出未截断。未手工重算全部矩阵entries/1425assertions。

审阅者本轮另一项自有 support-correlated 程序首次1PASS，与这里 peer程序执行0分别计；不会把root自有FIRST1写成自己的run。root所归档 Grinberg–Petrov PDF 本人没有实读，不将其12页来源scope记为本人scope，也没有新PDF/外部源码下载。W1–W14的证明无需它。

同对象定义已在本轮实际完整读冻结 mixed arithmetic A1–A14、budget B1–B22、credit-cap S1–S10、old actual analytic R1–R6、CRT sections1–6/R1–R21。相关合并输出曾全局截断的analytic/CRT已分别补读无截断。审阅本文不执行它们的program。

## I2. actual integer-valued坐标和指定支撑rank通过

W2的ψ=(t^p−t)/p、b_i=binom(t,i0)binom(ψ,i1)与原f_i=binom(t−1,i)的变换是实际GL_{3n}(Z_p)：integer values给finite-difference系数整，leading比的valuation是floor(i/p)−i1=0。degree i的triangular cutoff、最后R维ragged层保留，不能以ordinary coefficient CRT的自由函数像替代。

p-scaled导数关系由pψ'≡−1和低digit degree<p的p倍导数≡0给出，评价和导数均为实际格的整映射。对选定jet-row subset，每个residue的local polynomial degree≤Q，前Q个coefficients自由，top coefficient受同一个degree<R低digit空间约束。

W3的small-row处理正确：先把r_ρ≤Q的全部rows贡献上界r_ρ，然后删掉这些rows。剩下big residues的底层rank至多每块Q，top在每块最多一条列方向，总rank≤min(R,K)。所以总cap是Σmin(r_ρ,Q)+min(R,K)，没有给small residues额外免费top credit，也没有假定evaluation/derivative各自都独立。

任意指定Y_I是整d×d矩阵，modp rank≤cap就给det valuation≥d−cap。把ambient cap限制到actual paired L只会进一步降低rank；该步骤未换格、未使用target Gram unit。

## I3. block minor左右匹配与whole-X联合估值通过

Scaled block W5正是(p⁵V,p⁴U)作用在(P,pP')上。large-prime时tail entries≥w_ρ、head≥w_ρ+4；w取0/2/3/5，source的额外divisibility不会使界变坏，X系数也在同一Gauss估值内。

一个block-diagonal node矩阵的非零minor必须在每个实际node左右取相同数量l_j。否则任何det permutation都无法匹配。故左右的residue counts都是同一个r_ρ；这正是相关估值所需的支撑条件，不可分成两次独立allocation。

每个residue至多2q_ρ个tail rows，超出部分必来自head，得到W6的weight成本。两侧Y-minor都按同一r_ρ付rank费用，于是两次Cauchy–Binet准确给W7/W8。整体X polynomial所有系数同时受控，D_A=0时也合法，不假设某个specialization非零。

共享credit−2min(R,K)不是convex independent marginal。作者DP以(used rows,used credits)记录全局R预算，每个r>Q的residue最多取credit1，准确实现W7；没有将它改成未经证明的greedy。其最后rank费用非负，因为Σ(r−Q)_+≥K≥min(R,K)，Ω_p≥0。因此W8合法地包含旧entrycap。

## I4. 明确window的全尺度dual bound通过

在31n/42<p<3n/4，Q4、h8、a2，unit/mixed/large类型的精确数目

u=6n−8p+1，v=11p−8n−1，z=2n−2p

分别对应(w,q)=(0,8),(2,7),(5,7)。由于整数c<t，u≤t，计数没有遗漏一条rho端点。

W11三不等式可在其breakpoints0/4/14/16和容量端点逐段手核：unit型r≤16时difference≥32−2r，r≥16时difference≥2r−32；w2型在4≤r≤14准确饱和；w5型已有5r≥4r。credit放宽为R仅削弱下界。独算

\[
8n-40u-8v-2R=240p-174n-32
\]

故原determinant的valuation≥240p−184n−32。−32是实际整数边界，未免费抹去。

此处u=2R+1，unit-tail一层cap为4u+R，实际kernel lower=36p−25n−4，正部确实为正：p≤n及p²>8n蕴含p>8；W9给36p−25n>11n/7，n≥11足以超过4。因此W13的72p−60n−8是原actual basis上的合法全X下界。

## I5. 相对已付费用的1/84准确通过

W9处旧first-Smith模型为38x−36，新的同对象一层DND为72x−60。两者差34x−24在整个window为正，故weighted必须与新DND比较，不能重复扣已付Smith/cap信用。

Weighted主率240x−184超出DND的差168x−124在x=31/42为0、x=3/4为2，window宽1/84，因此其面积是1/84。作者只在这个明确区间兑现Ω的dual lower，没有将整个未解Ω优化积分冒认为已证。

uniform有限整数误差−32、−8不影响固定window的PNT n²主率。若与审阅者p≤n的新proof合并，须在这个window逐prime取max；在其费用之外可再减少至少1/84，不能将重叠区间所有候选裸gain相加。

## I6. source/certificate范围准确，不替代proof

完整static source的paired_newton构造实际primitive G_m与mandatory high vectors；cardinal Newton系数(−1)^{i−m+1}binom(i,m−1)和modp pD的shift by lp式与真实定义一致。所选rows是实际负nodes上的evaluation或p-scaled derivative，degree仍<3n；没有扩大为自由Hermite矩阵。

JSON三个case的Ω为66/98/238，dual lower46/94/238，一层credit66/98/194。前两个有限case不比一层更强，第三多44；这与全尺度−32边界完全兼容，不构成或替代无限收益证明。对应观测rank16/22/40≤cap21/29/53，指定det最低divisibility为25/33/57。作者没有计算实际Gram determinant。

源码exact Fraction面积1/84、共有1425检查/3cases，FIRST1成功；本审阅无运行/import/rerun，没有用有限rank表推W3的全尺度断言。最终W10准确区分了作者只读rowlabels首尾与本审阅实际读全部labels，两者readscope不混淆。

## I7. 审阅结论与边界

W1–W14在同一个original B6/k3/s5 paired saturated rank2n、degree<3n、whole-X对象上全部通过，未发现需要数学修订的项。新结果是实际支撑相关weighted finite-place theorem、精确dual window和在一层DND之外再付1/84的主率信用。

它不证明最优actual content或cost lower，不证明actual restricted determinant无限nonzero，也未跨过strict arithmetic/analytic margin。没有新的ζ/L/Catalan数值无理性或线性无关性定理，没有外部Lean验证。

本NEW独审全文自读后冻结；所有旧/同行producer执行/import/rerun0，PDF实读与下载0。
