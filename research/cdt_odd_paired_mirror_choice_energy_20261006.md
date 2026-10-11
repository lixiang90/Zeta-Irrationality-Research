# 同一配对饱和格的镜像选择能量：严格解析改进与准确变分极限

日期：2026-10-06。NEW 数学稿，quarter_actual_rank，待实际独审后冻结。所有旧/同行数学 MD、PY、JSON、manifest 保持只读，不执行、import或重跑。本文只运行自己的 NEW 有理区间证书首次一次。结论为同一实际构造的内部全尺度界，不是新的特殊值无理性定理。

## M1. 实际输入、固定对象与新的主定理

本轮实际全文回读冻结 energy `cdt_odd_paired_plucker_energy_rate_20261006.md` E1–E8、公式E1–E26，SHA `01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a`；root gcd `cdt_odd_paired_primitive_gcd_rate_20261006.md` G1–G10、全部G1–G13公式，SHA `77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2`；同格全素数预算 `cdt_odd_paired_all_prime_budget_20261006.md` B1–B22，SHA `55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc`。均完整输出，无截断；它们的 producer 均未执行/import。

沿用原三重零点R_n、rank2n、实际整数值饱和基 G_1,…,G_n,f_{2n},…,f_{3n−1}、原右线 c_n=2n+1/2。固定a,b∈Z、b≠0，ξ=aζ(4)+bζ(5)，D_{A,n}(ξ)完全不变。记 m'=2n+1−m、b_j=binom(6n+j,j−1)、β_m=gcd(b_m,b_m')、Γ_n=∏β_m，以及

\[
\widetilde\kappa_j=\frac{(6n+j)!}{(6n+1)!(j-1)!^2(2n-j)!},
\quad h(t)=(6+t)\log(6+t)-2t\log t-(2-t)\log(2-t)-6\log6+2.
\tag{M1}
\]

两个(j−1)!始终保留。没有改变基、form scaling、finite-place规范或目标。

**主定理。** 存在C_{a,b}使每个n≥1满足

\[
\log|D_{A,n}(\xi)|\le-\beta_{\rm mirror}n^2-2\log\Gamma_n
+C_{a,b}n\log(n+2),
\quad \beta_{\rm mirror}=\beta_0+\tfrac12\log2+c_*.
\tag{M2}
\]

β0是冻结E3/E4的原常数，已有首次证书β0∈[7.90523839512558,7.90523839512559]，本轮没有重跑。c_*在本稿M5的公式M15明确为一变量全区间最小值；新的严格有理证书给

\[
0.840144459\le c_*\le0.845115370,
\quad \beta_{\rm mirror}>9.09188285412558.
\tag{M3}
\]

使用冻结gcd全尺度γ∈[1.455845,1.457795]，得到相同D_A的

\[
\limsup n^{-2}\log|D_{A,n}(\xi)|
\le-\beta_{\rm mirror}-2\gamma<-12.00357285412558.
\tag{M4}
\]

此前同对象β_H用c_H=9log3−8log2−4；新界用镜像选择的系数损失与Hardy能量共同取代c_H，严格改善。非零与算术margin仍未成立，M4不单独证明任何数值无理性。

## M2. 先计准确镜像系数损失

冻结E12/E14中低块实际选择a_m∈{m,m'}；设选择左节点m的pairs共k个，q=k/n。左节点对应较大的δ=c_n−a；右节点对应较小的δ。对同一pair，|S'(m)|=|S'(m')|，所以

\[
\frac{\widetilde\kappa_m}{\widetilde\kappa_{m'}}=\frac{b_m}{b_{m'}}.
\tag{M5}
\]

b_j严格随j增长，故log(b_m'/b_m)随m递减。对于所有包含k个左节点的选择，真实平方系数损失至少

\[
2\sum_{m=n-k+1}^n\log\frac{b_{m'}}{b_m}.
\tag{M6}
\]

这是一条每个n的准确不等式，没有从独立最大κ与独立最小Hardy值拼出假收益。

令B(t)=(6+t)log(6+t)−tlogt−6log6。S'的对称阶乘相消给h(2−t)−h(t)=B(2−t)−B(t)=:Δ(t)。B'(t)=log((6+t)/t)>0于0<t≤2，Δ递减且Δ(1)=0。Stirling对全部0!端点一致地给

\[
2\sum_{m=n-k+1}^n\log\frac{b_{m'}}{b_m}
=n^2P(q)+O(n\log(n+2)),
\quad P(q)=2\int_{1-q}^{1}\Delta(t)dt.
\tag{M7}
\]

误差uniform in k：B在[0,2]连续，导数只有可积log端点；全部阶乘的Stirling误差O(logn)按n项支付。因此P≥0、P'=2Δ(1−q)≥0。

## M3. Hardy节点两个半区的真实排序界

小δ节点准确为m−1/2，大δ节点为2n−(m−1/2)，m1..n。设d=n−k，将选定δ排序δ_1<⋯<δ_n。选择结构严格给

\[
\begin{array}{ll}
i\le d:&i-\tfrac12\le\delta_i\le k+i-\tfrac12,\\
i>d:&k+i-\tfrac12\le\delta_i\le n+i-\tfrac12.
\end{array}
\tag{M8}
\]

分别来自n个半整数中选d个或k个。不是假定所有左节点连续或所有右节点相同。

Hardy determinant准确为

\[
\mathcal H_n=(2\pi)^n\prod_i(2\delta_i)^{-1}
\prod_{i<j}\left(\frac{\delta_j-\delta_i}{\delta_j+\delta_i}\right)^2.
\tag{M9}
\]

对j>i，ratio随δ_j增、δ_i减而增；M8因而给三种上界：

\[
\frac{\delta_j-\delta_i}{\delta_j+\delta_i}\le
\begin{cases}
\frac{k+j-i}{k+j+i-1},&i<j\le d,\\
\frac{n+j-i}{n+j+i-1},&i\le d<j,\\
\frac{n+j-k-i}{n+j+k+i-1},&d<i<j.
\end{cases}
\tag{M10}
\]

各分子至少1，∏(2δ_i)^{-1}≤1。与旧E15只用δ_j<2n相比，这里支付了k对全部低/高节点的位置约束。

## M4. 三块全尺度能量及其闭式

令L=1−q，定义

\[
\begin{aligned}
c(q)=2\!\int_0^L\!\int_t^L\log\frac{q+u+t}{q+u-t}\,du\,dt
&+2\!\int_0^L\!\int_L^1\log\frac{1+u+t}{1+u-t}\,du\,dt\\
&+2\!\int_L^1\!\int_t^1\log\frac{1+u+q+t}{1+u-q-t}\,du\,dt.
\end{aligned}
\tag{M11}
\]

q0、1的对角log奇点按可积极限处理。M10的三角/矩形Riemann sums统一给

\[
\log\mathcal H_n\le-c(q)n^2+O(n\log(n+2)),\qquad0\le k\le n.
\tag{M12}
\]

uniform误差可直接按affine log的等值strips证：每个strip至多O(n)个grid pairs，值为log(r/n)；改变一个grid unit的总误差由∑_{r=1}^{O(n)}1/r付O(nlogn)。可能为零的边界strip含O(n)个cells，∫_0^{1/n}|logv|dv=(logn+1)/n给同一量级。domain的moving edge位于k/n grid，boundary cells亦O(n)个。所有分子/分母为M10的integer affine forms，系数只为±1，故常数不依赖k。这样没有以某个固定q的渐近冒认uniform in k。

令f(z)=z²logz/2−3z²/4、f(0)=0，f'(z)=zlogz−z、f'(0)=0。因为f''=logz，逐项积分M11得

\[
\begin{aligned}
c_{LL}(q)&=f(2-q)-4f(1)+3f(q)+2(1-q)f'(q),\\
c_{HH}(q)&=f(3+q)-2f(3)+f(3-q)-2f(1)
+2f(1-q)+2qf'(1-q),\\
c_{LH}(q)&=2\{f(3-q)-2f(2)-f(3-2q)
+2f(2-q)+f(1+q)-f(1)\},\\
c(q)&=c_{LL}+c_{HH}+c_{LH}.
\end{aligned}
\tag{M13}
\]

例如q0给c(0)=2log2；q1给f(4)−2f(3)+f(2)−2f(1)，均与实际单半区Hardy能量一致。M7同样积分得

\[
P(q)=2\{f(7+q)+f(7-q)-2f(7)
-f(1+q)-f(1-q)+2f(1)\}.
\tag{M14}
\]

该闭式没有额外阶乘信用：它只是同一κ product的准确相对损失。

## M5. 匹配而非分开极值，并返回实际D_A

设

\[
c_*:=\min_{0\le q\le1}\{c(q)+P(q)\}.
\tag{M15}
\]

连续性保证min存在。M6–M12给每个选择

\[
\log\left\{\prod_m\widetilde\kappa_{a_m}^{\,2}\mathcal H_n(a)\right\}
\le2\sum_{j=n+1}^{2n}\log\widetilde\kappa_j
-c_*n^2+O(n\log(n+2)).
\tag{M16}
\]

所有2^n个正项的sum再平方只付2nlog2，故冻结E12–E14给

\[
|D_A(\xi)|\le\exp\{-c_*n^2+O_{a,b}(n\log(n+2))\}
\frac{Z_{H,n}L_n^n}{F_n^2\Gamma_n^2}
\prod_{j=n+1}^{2n}\widetilde\kappa_j^{\,2}.
\tag{M17}
\]

Z_H,L_n,F_n完全沿用冻结E18–E22，high Vandermonde已用准确平方恒等式去掉factor2。其n²logn取消不变。因此旧c_H被M15合法取代，得M2。没有把选择数2^n写成n²费，也没有把κ loss独立double扣一次。

## M6. 4096闭区间的严格证书，不以采样充当全q证明

NEW源 `cdt_odd_paired_mirror_choice_energy_20261006_verify.py` 只import stdlib Fraction、functools、pathlib、json，不读取旧/同行文件。首次且唯一执行1次成功，生成同名JSON；没有failed新run。本轮执行1，不合并或抹掉上一轮failed-v1+distinct-v2的2次历史。

区间公式为logx=2∑_{j=0}^{23}z^{2j+1}/(2j+1)+positive remainder，z=(x−1)/(x+1)，先reduce x到[1,2]，余项≤2z^49/[49(1−z²)]。负power-of-two在interval操作中交换端点。全计算为exact Fraction，输出仅作向外10^−9舍入。

将[0,1]分4096个闭区间[l,h]，每个interval真正覆盖全部q：

- f在[0,1]递减，f'亦递减，使用两端的exact log intervals，包括0的连续值。
- 在[1,4]，f'从−1增长至4(log4−1)<2，故|f'|≤2；用midpoint的exact f interval加减2×halfwidth包住整个输入区间。log4<3/2另由同一log certificate核实。
- 所有signed linear combinations与products用完整interval arithmetic。P单调，因此其整个cell的下界是P(l)的interval lower端与0取max。

全部cells下界的minimum≥840144459/10^9；一个midpoint的upper给c_*≤84511537/10^8。JSON保存4096个closed cell bounds及min cell794。midpoint只用于global upper，不用于证明lower；interval覆盖及上述导数/单调法才证明M3的所有q。

M2/M12/actualdet nonzero并非程序认证范围。程序只认证M13–M15的一变量数值界；所有n的桥为正文纸面证明。

β0的既有lower加log2>0.693（原E7纯纸面前三项series）和c_*的NEW lower，给β_mirror>9.09188285412558。γ的既有lower再加2×1.455845，得M4严格下界。旧证书/source从未重跑或修改。

## M7. E26正选择和的准确约束变分极限

令x_i=δ_i/n。小节点为(m−1/2)/n，大节点为2−(m−1/2)/n，镜像准确，phase没有被免费忽略。设

\[
\mathcal C=\{p(x)dx:0\le p\le1,\ p(x)+p(2-x)=1\text{ a.e.},\ 0\le x\le2\},
\]
\[
K(x,y)=\log\left|\frac{x-y}{x+y}\right|,
\quad \mathcal F(p)=2\int_0^2h(2-x)p(x)dx
+\iint_{[0,2]^2}K(x,y)p(x)p(y)dxdy.
\tag{M18}
\]

边界x=y以及(0,0)的值不影响density integral。定义冻结E26的实际正和

\[
T_n=\left(\sum_{a_m\in\{m,m'\}}\prod_m\widetilde\kappa_{a_m}
\sqrt{\mathcal H_n(a)}\right)^2.
\]

则准确极限存在且

\[
\boxed{\lim_{n\to\infty}\{n^{-2}\log T_n+4\log n\}
=\max_{pdx\in\mathcal C}\mathcal F(p).}
\tag{M19}
\]

这是unweighted Hardy选择正和的极限，不是原complex determinant equality，也不是把真实weighted低Gram的L_n upper称equality。

**compactness。** 任一selection empirical λ_n=n^−1∑δ_{x_i}包含每个1/n-grid site至多一次，且λ_n+reflectionλ_n是全2n中点grid measure。任一weak极限有density≤1并满足mirror关系；C因此weak compact。h连续至0、2，uniform Stirling给每个selection的external cost为2∫h(2−x)dλ_n−4logn+o(1)，误差uniform。j/n与2−x的1/(2n)相位只付O(nlogn)。Hardy前因子nlog(2π)−∑log(2δ_i)=O(nlogn)。

**log奇点。** K≤0且−K≤log4+log(1/|x−y|)当|x−y|<1。每个grid site的η近邻至多2ηn+2个，逐spacing k/n求和给discrete off-diagonal tail

\[
\frac1{n^2}\sum_{i\ne j,\ |x_i-x_j|<\eta}|K(x_i,x_j)|
\le C\eta(1+|\log\eta|)+C\frac{\log(n+2)}n.
\tag{M20}
\]

continuous density≤1有相同Cη(1+|logη|) bound。K<-M只可能|x−y|<4e^−M。先truncate max(K,−M)，再避开原点[0,ε]^2（mass≤ε²且bounded truncation），得到continuous kernel；weak convergence适用。full diagonal的truncated离散项只付M/n。依次n→∞、ε→0、M→∞，M20保证K能量在C上连续，并给全部selection weak subsequences的准确limit。不存在以未控制diagonal log代替有限原始能量的缺口。

**recovery。** 给任意p∈C，在低半区定义
b_m= floor(n∫_0^{m/n}p)-floor(n∫_0^{(m−1)/n}p)∈{0,1}。
选择小节点当b_m1，否则其大mirror。每个prefix low mass误差≤1/n，故这些binary selections weak趋p；M20又给energy收敛。compactness给max upper、recovery给lower，最后2^n正项的logsum与最大log项仅差O(n)，证明M19。

这里recovery的b_m是局部0/1指标，仅本段使用；不是M1的binomial b_j或新的整数basis。

## M8. 变分最大值唯一与可执行的精确优化接口

K严格负定，以下直接证明而不依赖未读potential theory文献。置u=logx、v=logy，则

\[
K(x,y)=-2\sum_{\ell\ge1\text{ odd}}\frac{e^{-\ell|u-v|}}\ell,
\]
\[
e^{-\ell|u-v|}=\int_{-\infty}^{\min(u,v)}2\ell
e^{-\ell(u-s)}e^{-\ell(v-s)}ds.
\tag{M21}
\]

对任意两个C中densities的非零signed差ν，M20保证绝对积分；M21展开得K-energy是若干非正square integrals之和。若为0，则ell1的
∫_[s,∞)e^−u dν(u)=0对a.e.s成立；该weighted tail连续，遂对全部finite s为0，区间差分给ν=0，矛盾。因此F严格concave。M19的compactness/continuity给唯一maximizer p_*。

其准确first-variation接口：对0<x<1记

\[
g_*(x)=h(2-x)-h(x)+\int_0^2
\{K(x,y)-K(2-x,y)\}p_*(y)dy.
\tag{M22}
\]

bounded perturbation δp在低半区和反射半区取相反号，使δF=2∫_0^1g_*δp。故a.e.：p_*=0处g_*≤0，p_*=1处g_*≥0，0<p_*<1处g_*=0。严格concavity使这些feasible first-variation条件亦充分；可以用这条实际mirror-constrained integral equation继续求p_*、给更强certified upper，而不是另换norm。

当前没有解出p_*或max F的闭式/最优数值。已证M16还给可验证的严格upper

\[
\max_{p\in\mathcal C}\mathcal F(p)
\le2\int_1^2h(t)dt-c_*.
\tag{M23}
\]

所以M19并非只有待解定义：M3/M23已经给同一actual格的新严格解析改进。未知max F的进一步求解可继续加强它。

## M9. 进展与仍缺的数值结论门槛

本轮已证：全n同格解析率提高；镜像κ与Hardy匹配的一变量严格uniform界；E26正和的准确受约束变分极限；该变分问题唯一max与完整first-variation接口。自身NEWproducer1次PASS、旧/同行execute/import/rerun0、Lean0。没有新增外部PDF/代码/HTML归档；本稿关键数学全部在正文直接推导，没有冒认同行primary页为本人本轮阅读。

同一格all-prime safeA=1085983123/24190320约44.893是上界；新已证解析率>12.00357仍不提供strict margin。不能从两个安全bound不足推出actualcost下界或no-go。两个辅助finite-field matrix的无限unit仍未证，因此D_A(有理目标)的无限nonzero也未被本稿消除。没有新的ζ/L/Catalan无理性、线性无关性或外部Lean结论。旧420项冻结输入保持只读；本文和NEW来源收据待实际独审后冻结。
