# Euler 相对链候选的独立全文纸面审查

2026-10-07，审阅者 /root。实际全文读取主稿 `cdt_odd_gamma_relative_chain_candidate_20261007.md`，E1–E23/八节，待冻结 SHA `1031f489a261e6862d7b0e895e320272751740217a61d0d3f1ce8945f245a60e`。基线588记录保持只读；本审不运行数学producer、guard或素数表。结论：**PASS，未发现需实质修订的数学问题**。这是纸面推导的审核，不是Lean形式化、全局整Betti模型或数值无理性定理。

## R1. 真实 Euler 归一与临界点

五个B(s+1,s+1)与一个Dirichlet积分严格给 Γ(1+s)15/[Γ(2+2s)5 Γ(5+5s)]。p(s)=(1+2s)5∏(5s+k)精确抵消整数Γ位移，p(0)=24与Δ4体积1/24正确，κ0=1由实际链保证。Q最大值为4^-5·5^-5，取得点唯一；parameter绝对收敛域Re s>−1足够。没有将未知period倍数略掉。

## R2. Resolvent 真正是倒数 factorial 系数

紧子圆几何展开与E4给 E(s,T)=Σκ(n+s)Tn。κ(n+s)/κ(s)=Λ^-n (1+s)n9/∏(a+s)n，在s0准确为1/h_n；T0处B_j初值和E_j未知κj明确区分。Ms的T项(D+s+1)9在第n系数作用成(n+s)9；n0剩源∏(s+a−1)，E9正确。有限参数jets有有理triangular系统，holonomic断言足够，不误作原homogeneous L的rank-nine Taylor解。

## R3. 完整 residue 与非零 branch

沿Q push-forward得到一维Cauchy resolvent，越pole q=1/T的有向差为±2πi T^-1 w(T^-1)·T^-s；主稿允许统一把orientation sign纳入ψI，未靠leading term代替完整函数identity。p(s+D)(T^-s h)=T^-s p(D)h，所以整行variation准确为T^-sΨ。

独立核Hessian x block−8I5、y block−25(I4+11ᵀ)，对应九维非退化maximum；Morse密度首指数9/2−1=7/2且正首常数。p次数9、最高系数2^5·5^4，D9下降到−11/2，九个falling factors皆非零，所以Ψ不可能恒零。后续除去Ψ有正当依据。

## R4. 相对有理链与Q Taylor 校准没有混同

E11有序Kummer simplex积分准确为(−logQ)^j/j!；添变量后的form和semialgebraic边界有理，所有边界对数可积。因此E_j确有实际relative rational-form实现。但从E_j到B_j用1/κ(s)的系数，它不是已知Q变基。E_j起点κj与B_j coefficientwise-Q可同时成立而不自动给B_j的有理Betti链；主稿正确保留这个未闭合接口。

## R5. Taylor package 的全variation、rank与正则化限制

λ0=1使 Hj(logT)degree恰j、leading(−1)^j/j!。κj或λj有理只消constant分量，不消其余log多项式，E17是完整限制。T^sB的jump变成λjΨ，却在0重新引入logj/j!；M0F=T^s∏(s+a−1)仍非齐次。λ5=−654ζ5−750ζ2ζ3的符号从exp(−logκ)独核正确。乘κ(s)得原κ行的操作也被准确记入非Q常数域。

取constant-in-log投影恰回到B_j，variation不与其交换。tangential basepoint平移及finite cover只能平移或倍乘最高log，不能变成ordinary Q Taylor germ。完整variation加logT对C(T)超越的三角论证，证明{1,B0,…,Bd}真实rank d+2，且这个linear package唯一invariant rows是rational rows。没有把此局限推广为其它relative/dual extension不可能。

## R6. 全prime cap与真实数组

Legendre层C_q(n)=5floor(2{n/q})+floor(5{n/q})在0..9，q>5n为0，故h_n|D5n9。parameter degreej项准确消耗j个分母≤5n的reciprocals，无遗落factorial，所有prime包括2/5均被E22覆盖。九个同激活width5加d个嵌套width5数组满足CDT阶梯条件；独算Σ(9+j)(2j+3)给E23以及d5=2935/49、d7=5420/81。safe费用不等于最优费用。根端本轮实际全文读CDT v2 PDF66–69，确认holonomic可放宽derivative gate、实际pullback须meromorphic及double/rearrangement分子；本审未声称这些条件已为候选满足。

## R7. 文献与交付边界

根端此次对主稿八节及上述自足积分、递推、variation、rank/cap论证实际全文独审。主稿各自记录GZ、Laporte–Walcher与BV的作者实际页域；根端没有在本审中通读这些原件，不将同行read域计为自身。normal-function数值connection及conjecturalperiod识别未作为本文无条件定理使用，此边界明确。

主稿可冻结为一个已检验的具体新候选及其准确障碍。它补全了Euler/relative-chain正实实现，但本package仍没有同时提供Q Taylor与关系依赖全填洞。root/source的新inverse-L lift是不同构造，本审的有限范围局限不排除它。当前strict holonomy余量、新ζ/L/Catalan数值结论和Lean均未获证。
