# 第259轮：CDT两log Hadamard响应的有界来源选择

2026-10-10。作者 `source259_log_products`。本稿只审查CDT原文明确的两个对数Apéry响应及其数值出口，不续旧level14、经典Li、χ−8或DD/KZ窗口。结论是：**该扩展本轮不准入；没有新的数值ζ/L或个别二重多对数定理。** 这不是所有Hadamard方法的不可行性定理。

## L1. 原文已证明的范围

固定来源为已存CDT v2，218页，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。实际完整读物理3–5、174–193；其中§14物理174–188及§15.1物理189–193首段已读完，§15.2仅物理193页，不采用其后未经阅读的模块猜想。

Theorem C / Theorem14.0.1已经证明：整数m,n不为−1或0、满足

\[
 |m/n-1|<10^{-6}
\]

时，log(1+1/m)log(1+1/n)无理；m≠n时，1、这两个单对数及其乘积在Q上线性无关。m=n时乘积是非零超越对数的平方，已经超越。m,n在这个条件下同号，1+1/m和1+1/n均正。

所以选择一个同范围的“大且接近”的新整数对，或作有理非零倍、交换、已知结论的线性重排，不能成为本项目的新数值出口。单对数的超越性及其有理线性形式已有Lindemann–Weierstrass/Baker基线；两log乘积的数值性质并不单独由这些线性对数定理推出，但近参数四项结论已由CDT覆盖。本稿没有执行全球新颖性审计，也没有把有限搜索未命中当成新颖性。

## L2. 实际unit carrier、完整坏芽与关系收益

为清楚核查机制，下面纸面推导限制a,b为不同的正奇整数、a,b>1；Theorem C的更广整数符号范围采用原定理，不声称从此限定证明推出。令

\[
 Q_a(x)=1-2ax+x^2,\quad
 A_a=Q_a^{-1/2},\quad
 H_a=A_a\int_0^x A_a(t)\,dt,
\]
\[
 \alpha_a=a-\sqrt{a^2-1}\in(0,1),\quad
 \eta_a=\frac12\log\frac{a+1}{a-1},\quad E_a=H_a-\eta_a A_a.
\]

原积分在x=αa的值是ηa。局部把Q写为(x−αa)乘一个非零解析单位：积分从αa到x有平方根因子，乘A_a的逆平方根后成为解析函数。因此E_a消去的是整个平方根坏芽，不只是一个leading系数。唯一另一个有限分支点是αa⁻¹，故E_a初始支的Taylor半径至少αa⁻¹；A_a的Taylor半径是αa。b通道相同。

定义四个实际有理Taylor载体

\[
 F_0=A_a\star A_b,\quad F_a=H_a\star A_b,\quad
 F_b=A_a\star H_b,\quad F_{ab}=H_a\star H_b.
\]

这里F₀是非平凡unit-period carrier，不是字面常函数1。直接双线性展开给

\[
 F_a-\eta_aF_0=E_a\star A_b,\quad
 F_b-\eta_bF_0=A_a\star E_b,
\]
\[
 F_{ab}-\eta_a\eta_bF_0
 =\eta_a A_a\star E_b+\eta_b E_a\star A_b+E_a\star E_b.
\tag{L2}
\]

Hadamard系数的Cauchy界表明右端三个类型的Taylor半径分别至少

\[
 \alpha_b/\alpha_a,\qquad \alpha_a/\alpha_b,
 \qquad1/(\alpha_a\alpha_b),
\]

全都严格大于αaαb。因此在最小乘积分支点αaαb，完整坏芽classes满足

\[
 [F_a]=\eta_a[F_0],\quad [F_b]=\eta_b[F_0],\quad
 [F_{ab}]=\eta_a\eta_b[F_0].
\tag{L3}
\]

若有整数关系r_aηa+r_bηb+r_abηaηb=r₀，则

\[
 P=r_aF_a+r_bF_b+r_{ab}F_{ab}-r_0F_0
\tag{L4}
\]

有有理Taylor系数，并且由(L2)实际越过最小分支点。这正满足258的完整坏芽选择判据，是明确的关系产生的解析收益。

这只自动消去最小乘积点。完整背景还须面对αa/αb、αb/αa、(αaαb)⁻¹等其它乘积分支支持；本稿不判定特定P是否另有额外取消。原文近参数条件让剩余奇点在symmetrization后聚集到有利背景外部，再用完整共同图证明矛盾。不能仅从(L3)继承最终holonomy预算。

## L3. 完整前缀整模型与原文最终秩

奇a时A_a在Z[[x]]：写a=2m+1，

\[
 A_a=(1-x)^{-1}\left(1-\frac{4mx}{(1-x)^2}\right)^{-1/2}
 =\sum_{k\ge0}\binom{2k}{k}m^kx^k(1-x)^{-2k-1}.
\]

每个系数为整数。若A_a=Σu_{a,n}xⁿ，定义积分给

\[
 [x^n]H_a=\sum_{j=0}^{n-1}
 \frac{u_{a,j}u_{a,n-1-j}}{n-j},\qquad n\ge1.
\]

所以d_N=lcm(1,…,N)清H_a的全部前缀；四个F载体及P全部前缀由d_N²清整，覆盖2与所有素数幂。固定整数关系系数不造成新Taylor增长费用。不能把这张四源表当成最终秩表。

原文接着令y=x²/(x−1)，G(y)=P(x)+P(x/(x−1))。其完整symmetrized前缀采用d_(2N)²，而不是未经支付的d_N²。原文Lemma14.3.1和§14.5加入导数、积分及七个pure函数，共17个C(y)独立函数，并使用完整17×2主类型表和附加积分向量。原文最终

\[
 \tau=1032659/242760
\]

配合Appendix A.6图得到秩上界≤16.2，与实际17冲突。本稿完整阅读§14的该接口，**没有复跑其高次resultant、十行行列式、全17行rank证明或Appendix图的完整独立认证**；不能向不同载体借用17、16.2或τ。

## L4. 两个可直接纠正的符号笔误及一个初始项笔误

固定v2物理178页(14.1.8)把(L4)的最后一项印为+r₀F₀，但同式上一行P=r_aP_a+r_bP_b+r_abP_ab以及(14.1.7)给出−r₀F₀。本文使用由定义逐项得到的负号；无需新的假设。物理187页§14.5的第二个singlelog分母印为m，按b=2n+1及(14.1.7)应为n。均已用整页PNG视觉核查，不归因于OCR。

物理175页(14.0.8)的显示初始项为x+ax²/2+(3a²−1)x³/6；它与同页积分定义、非齐次ODE不一致。由上节卷积公式正确初始项是

\[
 H_a=x+\frac{3a}{2}x^2+\frac{15a^2-4}{6}x^3+O(x^4).
\]

例如直接代入Q_aH′+(x−a)H=1即给x²系数3a/2。本文以后只采用积分定义及ODE。这些是可确定纠正的显示笔误，不据此宣布CDT Theorem C失效，也不把纠错计作新数值结果。

## L5. 为什么改写成二重polylog不能自动得到新个别值

固定绝对收敛域|u|,|v|<1，采用明确约定

\[
 D(u,v)=\sum_{r>s\ge1}\frac{u^r v^s}{rs}.
\]

将双和按r>s、s>r、r=s拆开，自含地得到

\[
 \log(1-u)\log(1-v)=D(u,v)+D(v,u)+\operatorname{Li}_2(uv).
\tag{L5}
\]

取u=−1/m、v=−1/n，m,n≥2且在CDT近参数范围，右边整个组合的无理性已由Theorem C给出。这不是独立的新数值目标；尤其不能据其和无理，推出D(u,v)、D(v,u)或Li₂(1/(mn))中指定某一个无理，也不能推出它们与ζ/L的全组线性无关。要隔离一个未知depth-two数值，须有新的真实载体或已付独立周期消去，不是给同一和换名称。

同理，这两个固定log响应的四个坏芽只承载Q-span{1,ηa,ηb,ηaηb}。常系数重排、重新规范化已知周期不会让某个ζ(7)或非临界L(2,χ)无条件加入此行。CDT一般Hadamard几何可以承载别的period；那需要新的实际响应，不能由本固定两log载体自动领取。

## L6. 可迁移的张量恒等式不代替准入

保留一条确定的工具：有限个实际A_i,H_i∈Q[[x]]，且E_i=H_i−η_iA_i的Taylor半径R_i严格大于A_i的半径ρ_i>0。对S⊂{1,…,r}定义F_S为各i选择H_i（i∈S）或A_i的Hadamard积，η_S=∏_(i∈S)η_i。则

\[
 F_S-\eta_SF_\varnothing
 =\sum_{\varnothing\ne T\subset S}
 \left(\prod_{i\in S\setminus T}\eta_i\right)
 \mathop{\star}_{i=1}^r
 \begin{cases}E_i&i\in T,\\A_i&i\notin T.\end{cases}
\tag{L6}
\]

每项半径至少(∏ρ_i)∏_(i∈T)(R_i/ρ_i)，故整个差的半径严格大于∏ρ_i。整数关系Σ_S c_Sη_S=0自动令Σ_S c_SF_S越过该最小乘积点。若A_i整数、非负整数w_i给d_N^(w_i)清H_i前缀，则该组合由d_N^(max_(c_S≠0)Σ_(i∈S)w_i)清整。有理关系先乘固定整数清c_S的分母。证明为有限双线性展开、系数Cauchy界及逐系数整性，无数学程序。

这只是§14响应恒等式的有限因子书写，不声称首次提出。2^r是载体标签数，不是其C(x)函数秩；还须证明实际完整最小族、所有叶与外国周期、共同图及严格净预算。原文§15.1.10指出其当前三log费用e³>16已经不利，建议多对两log的simultaneous Hermite–Padé来源，但没有给出新的数值定理。本稿不把这个建议当已完成的新候选，也不据此证明所有高阶张量方法失败。

## 决定与下一证书

本轮唯一所选两log扩展拒绝实现准入：它已给完整关系收益，但其近参数数值结论属于原文baseline；换成一个未覆盖整数对缺少同对象严格共同图/费用证书，换成个别depth-two或ζ/L值又缺少真实周期投影。没有获准的新numerical target，不开展参数、地图、素数或Padé扫描。

将来重开须先交付固定实际新响应与明确未由baseline直接涵盖的数值目标，证明同一潜在关系确实消掉完整坏芽或产生另一个已支付的算术收益，随后核完整prefix、实际rank、全域与strict预算。本结算不关闭root本轮独立的mixed modular来源，也不重置全局复盘clock。

所有来源选段、视觉核查和实际FULL/PARTIAL身份另见 `literature/source_selection_round259_20261010/log_reading_scope.md`。数学程序、CAS、参数/prime/map/word扫描、interval、Lean、外仓库Git写、旧producer、归档均0；仅文献定位、提取、渲染、文件记录及纸面数学。
