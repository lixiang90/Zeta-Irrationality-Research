# 单周期 beta 合流整模型的独立全文纸审

2026-10-07。审阅者 masked_racah_finalize。实际全文读取 `research/cdt_beta_single_period_confluent_integral_model_20261007.md` 全8节/B1–B29，并在作者仅更新末段收审记录后再次实际全文复读最终稿；其最终 SHA256 `a008a54d3307f151911ad0fc1dfa3587e05fd54eb89bd0172be364d162d64f2c`，11668 bytes。没有编辑作者主稿，没有运行数学程序、素数表、旧 producer/guard、Lean 或原外部仓库脚本。本审稿是独立纸面验证，不是形式化编译 PASS。

## V1. 真实周期身份与 beta(1) 消去

B1 的积分绝对几何展开以 k^(-r-1) 收敛，r=1也足够；B2 因此有逐项积分的合法支配。指数采用4u和4v，使两条 odd-denominator 尾均平移偶数个交错项，B4没有遗漏 (-1) 的 prefactor。

独核 B6 的部分分式：最高极点1/z^r系数1/d，递推各层系数 (-1)^(r-a)/d^(r-a+1)，末项 (-1)^r/(d^r(z+d))；两条 beta(1) 的系数精确为相反数。它们逐条条件收敛也允许先取共同有限截断再极限。B8 的 order1 有理尾符号为 (-1)^(r-1)(T_{u,1}-T_{v,1})/d^r，正确；d<0时原z+d仍为正。r=1的空和与s=4实例B9均一致。对角的 B5 确是单个 beta(s) 与有限有理尾，无inverse-binomial污染。

## V2. Hermite numerator、次数及完整 regular part

独核 B11 的 numerator degree 上界：B_k^r 为r(n-1)次，截断Taylor为至多r-1次，总计rn-1=H-1，故 B12 的 partial fraction 没有 polynomial part。

在z=k，未截断函数满足 B_k^r·(Q_I/B_k^(r-1))=B_k Q_I=D/(z-k)。截断误差 O((z-k)^r)，除以D给 B13 的 regular part O((z-k)^(r-1))。所以正是次数0,…,r-2的全部 regular Taylor coefficients 消失，不只是留数条件。在其它v∈J，numerator至少r阶零、denominator一阶零，亦得到r-1阶零；regular coefficient ell-1等于负的 sum p/(u-v)^ell。因此 B14 包括每个所需ell，低beta残数全被消去。

u∈J的p子矩阵恰I_n，故投影行独立；B16 E=q+beta(s)I_n为实际全部entries身份。它不等价于投影配对矩阵可逆，作者已正确区分。

## V3. 所有素数行分母 d_H^(3r-2)

B18 的整数性经纸面 factorial 参数核对通过：分母参数和为H-r-k，增加(r-1)!之后恰H-1-k。因此a_k的绝对值等于(r-1)!乘整数multinomial，所有k端点包括k=n-1与n=1成立。

对B19的正规级数，每个线性因子的分母是非零node差，绝对值≤H；负整数次方展开系数为整数。次数a的单项分母总次数a，故 d_H^a h_{k,a}∈Z，不依赖奇素数或p>r等额外条件。

B22是B_k(u)=u!/((u-n)!(u-k))、D'(u)=±u!(H-1-u)!的直接代入，指数与符号省略范围正确。其factorial numerator有r个因子，denominator有3r个；参数总和差恰r。令q=p^e，每层floor差等于r/q减去r个分子fractional parts、再加3r个分母fractional parts，严格大于-r，所以整数至少-(r-1)。所有factorial参数≤H，q>H时floor为零。因此该ratio v_p≥-(r-1)L，其中L=floor(log_p H)。另有(u-k)^r付rL，得到B23的-(2r-1)L；有限jet factor最多再付(r-1)L。合计为-(3r-2)L，恰由d_H^(3r-2)支付。

这证明B17涵盖p=2、小素数、所有powers及p>H；不是只验证第一层residue。u∈J的系数0或1另行整数，r=1的p=delta无需用此粗预算。没有把有理投影冒充unimodular变换。

## V4. 有理部分、假设输入分母与粗费用

T_{u,a}的odd denominators≤4H，|4(u-v)|≤4H。B8每项分母总幂数a+(r-a+1)=r+1，order1项为1+r；对角有限尾也为r+1。因此B25的d_{4H}^s全素数整数声明成立。先有integer投影p_hat，再与A_r相乘，顺序正确。

若beta(s)=a/b，matrix乘bd_{4H}^s后逐entry整数，故B26。只有在det E≠0时该整数的绝对值≥1，作者并未免费假定这一点。记m_n=d_H^(3r-2)，det E=m_n^(-n)det E_hat；普通PNT给leading成本4sr+(3r-2)r=7r²+2r。s4/r3时69正确。固定b输入损失n logb仅O(n)，并未漏掉。B27是safe denominator upper，不是不可改善的费用lower。

## V5. 系数高度

B19正规乘积的绝对系数可被(1-z)^(-E)控制：正一次因子也逐系数被(1-z)^(-1)控制；E=|I|+(r-1)|J\{k}|≤2(r-1)n。对固定a≤r-1，h=O_r(H^a)，再乘(u-k)^a≤H^a，有限jet的总高度O_r(H^(2r-2))。

B22每个factorial参数≤H。统一Stirling展开的logH系数恰为参数差r，而不是O(n)；所有 jlog(j/H) 项只有O_r(H)，其余固定个数error为O_r(logH)。所以factorial比与整个p的logheight为O_r(n)，没有n logn leading。u∈J系数0/1与n=1也无例外。增加m_n仍为exp(O_r(n))。这只是高度上界，不能当作小线性型或determinant的衰减证明。

## V6. 非零性与解析结论范围

独核原H×n矩阵的符号正则性：在两次Andreief中，两组ordered positive-node monomial generalized Vandermonde均为正；kernel 1/(1+x_i² y_j²)的Cauchy determinant符号为(-1)^(n(n-1)/2)，denominator全正。log weight在内部严格正，积分绝对可积，故所有按递增rowindices取的raw full minors严格同符号。

目前没有p投影full minors的相容符号证明，故不能经Cauchy–Binet把这个结论移给E。det(q+TI) monic证明形式多项式不恒零，却可能在真实beta(s)上有零；假设目标有理时更不能免费排除该情况。作者保留无限非零尺度、实际行族解析衰减、同一对象有限处改费三个缺口，准确。

## V7. 文献、读取和最终判断

本轮审查输入为作者主稿8节全文，以及本轮本人已完整读取的Catalan foundations.tex434行、自己的高权重周期稿全文。实际复用Lai–Zhou本地PDF11–14四页，确认Theorem6.1仅证明五个偶beta值中至少一个无理；这不能因beta2已满足便自动推出其它四个。没有继承别人阅读页域，没有新增下载，没有运行论文附带MATLAB/Lean。

数学判断：B1–B29及相关nonzero/height/费用范围纸核PASS，未发现需要作者数学修订的错误。这是一个明确的单目标真实carrier与全部素数整模型；尚非beta4或其它高偶beta无理性证明。审阅者应在任何最终指纹更新后实际全文回读本审稿；不将本纸审写作已通过Lean或已复现原仓库编译。
