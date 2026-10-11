# 第232轮：关系敏感的CDT解析入口与χ₋₈原生载体的限制

2026-10-08，Root。正式全局复盘中的具体纸面产出。下面证明的是指定模板的准入限制；没有证明χ₋₈或全部ζ/L研究不可能，没有新的数值无理性定理。数学程序0。

## 1. CDT允许meromorphic，普通pole的消失不是自动的解析收益

实际完整阅读保存的CDT Theorem2.5.1、2.7.1、Basic Remark2.11.1选段。定理要求φ:(D,0)→(C,0) holomorphic，而每个f_i∘φ只要求meromorphic。应区分这两种要求。原文来源见[作者版](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)；本轮重读的是已有固定选段，不称重新读完220页。

**引理M。** 设F是原点解析芽，a∈Q且a≠0，c∈Q，

\[
H_c(z)=\frac{F(z)-c}{z-a}.
\]

则span_{Q(z)}{1,H_c}=span_{Q(z)}{1,F}。对任意非恒定holomorphic φ、φ(0)=0，F∘φ具有全盘meromorphic延拓，当且仅当H_c∘φ具有这样的延拓。

证明：F=(z−a)H_c+c，反向公式亦为有理线性变换。φ−a不是零函数，其零点孤立，乘除这个holomorphic函数只增减有限阶pole；两个公式在原点相符，故由延拓唯一性在盘内相符。这也涵盖φ到达a的其它叶，并非只看原生实段。常数1必须保留，a≠0保证H_c仍为原点解析芽。

更一般地，完整tuple的可逆Q(z)矩阵变换保留Q(z)-rank和共同meromorphic图类（两套tuple须在原点定义为解析芽）。系数的孤立零点/pole不会构成新的branch障碍。**这不是算术费用不变定理。** 例如1/(1−z/2)的第n项为2^{−n}；任何固定有限lcm-slope数组在p=2只给O(log n)估值，故不能把任意有理gauge当成免费同type。

如果真实关系取消的是对数、分数幂或其它非meromorphic局部行为，引理M不适用：例如Apéry的B−cA可以在正确c下取消平方根branch，且保留A会重新带回原branch。新的有效CDT投影必须检查**保留的整个tuple**，而不是只看一个改善的分量。

## 2. 一个与原目标直接相连的全尺度例子

取χ=χ₋₈，χ(1,3,5,7 mod8)=(1,1,−1,−1)，偶数处0。令

\[
A(z)=\sum_{n\ge1}\frac{\chi(n)z^n}{n},\qquad
B(z)=\sum_{n\ge1}\frac{\chi(n)z^n}{n^2},\qquad L_8=B(1).
\]

角色生成函数直接给

\[
A'(z)=\frac{1+z^2}{1+z^4},\qquad B'(z)=\frac{A(z)}z.
\tag{1}
\]

B在1处原生解析。所谓关系载体H_c=(B−c)/(1−z)，在c=L₈时填1处pole；在假设L₈∈Q时确为Q系数芽。然而引理M已说明这一个pole的消失不扩大CDT的meromorphic图类。

还能直接支付全部强迫branch。对ξ⁴=−1，记

\[
r_\xi=\operatorname{Res}_{z=\xi}A'(z)
=\frac{1+\xi^2}{4\xi^3}\ne0.
\]

在ξ附近的任一transported branch，A=r_ξ log(z−ξ)+analytic。取local ℓ(z)=log(z/ξ)、ℓ(ξ)=0。由(1)分部积分可得

\[
B(z)=r_\xi\ell(z)\log(z-\xi)+\text{analytic},
\quad
\ell(z)=\frac{z-\xi}{\xi}+O((z-\xi)^2).
\tag{2}
\]

确切地，右侧导数多出的r_ξℓ(z)/(z−ξ)是analytic，可放入analytic余项；A的余项除以z亦analytic。不同transported A branches只相差常数，B的差因而在ξ附近analytic，(2)的非零log系数不变。

因为ξ≠1，每个c的H_c在此仍有leading term

\[
\frac{r_\xi}{\xi(1-\xi)}(z-\xi)\log(z-\xi).
\tag{3}
\]

任意非恒定holomorphic φ若在z₀命中ξ，写φ−ξ=u(z−z₀)^e+…，u≠0、e≥1，则(3)留下非零(z−z₀)^e log(z−z₀)，不是meromorphic。故所有合法共同图均omit这四个ξ，且此必要条件对每个c完全相同。没有声称omit四点就是充分条件；全部到达叶和全盘单值性仍须核。

## 3. 同一原生族的完整算术与函数秩也不依赖c的真值

置D_odd(N)=∏_{p≤N,p odd}p^{⌊log_p N⌋}（N=0时1），δ_f(N)为含0到N系数的最小共同分母。逐项有

\[
\delta_B(N)=D_{\rm odd}(N)^2.
\]

上界明显；对每个p^k≤N，χ(p^k)=±1，第p^k项的估值精确−2k，给下界。H_c的系数为h₀=−c、h_n=Σ_{j≤n}χ(j)/j²−c。整的前缀和/差分双向变换于是给**精确**公式

\[
\delta_{H_c}(N)=\operatorname{lcm}\bigl(D_{\rm odd}(N)^2,\operatorname{den}(c)\bigr).
\tag{4}
\]

它不遗漏常数项和prime powers。PNT给log δ=2N+o(N)，固定c只改变有限费用。固定整数清den(c)后，{1,H_c}可用literal数组两列(0,1)，σ=(0,2)、e=0、τ=3/2。这是一个共同安全type，**不是所有primitive/all-place格的最优费用**。

(2)亦证明B不是有理函数，故{1,H_c}的Q(z)-rank恰2，对每个c都成立。两函数holonomic由(1)的有限微分系统直接得到。

所以这套原生模板的实际rank、合法共同meromorphic图类及上述完整safe type在所有c∈Q下相同。若仅依这些数据构造严格CDT秩矛盾，该矛盾对任意c∈Q都会成立，与实际存在的这些芽冲突。**c=L₈带来的普通pole取消没有提供依赖目标有理假设的额外CDT输入。** 不能把holomorphic子类中填1的观感当作CDT已经利用的条件改进。

这不排除关系点特有的联合整格收益：若要使用它，必须在同一源上独立证明新的joint lattice费用，不能从(4)推断；也不排除新的χ₋₈混合源，因其可以有不同branch系数和周期栈。

## 4. 对下一窗口的准入要求

新载体先给实际Q/K系数芽、全部真实周期关系及源函数秩。在目标关系下，必须明确支付至少一项真正改变判据的事实：保留tuple的非meromorphic branch被消去；新增有理芽带来真实函数秩而不继承旧branch；或同一联合整格产生已证净费用改进。只改普通pole、扩大形式motivic空间、保留可逆恢复的旧完整tuple，不足以启动新的参数窗口。

229–231的真实Θ投影与固定minor仍是有价值的结构资产；它们是否闭合W的无限非零和严格费用是另外的问题。不能因本引理否定一个原生χ₋₈ quotient，就宣称应该返回旧μ₇/固定Padé扫描。

## 5. 阅读与验证边界

本轮Root完整读CDT保存选段、228正式报告及231报告；CDT原文网页本轮作来源核对。OpenAI Deligne–Drinfeld保存源07-holonomy.tex仅实际读末尾499–553附近：作者明确指出奇ζ系数非零只用正性，没有数值算术独立性断言。全仓库认证和Lean构建均未进行。

本引理M的共同meromorphic/费用区分与(1)–(4)由本稿自含纸证承担。历史228已有可逆代数gauge不能制造GB的结论和Catalan有限Euler过滤的LCD；本轮不把它们冒称新结果。新增是CDT允许类下的关系敏感准入诊断及χ₋₈具体原生模型的全叶/LCD/rank联证。独立审阅另存新收据。
