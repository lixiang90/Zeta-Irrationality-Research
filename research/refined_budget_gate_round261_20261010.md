# 第261轮：共同解析域与标准算术 type 的联合停止证书

2026-10-10。固定第259轮的真实混合关系载体
\[
H=A(a+bB_3+cC_3+dB_4),\quad a,b,c,d\in\mathbb Q,\ d\ne0,
\qquad V=\langle1,H,\theta_sH\rangle_{\mathbb Q(s)},\quad\dim V=3.
\]
目标仍是新的数值 ζ/L 无理性或线性无关性；本轮未得到该类定理。所证为一个特定函数族、坐标和已发表 holonomy 接口的停止证书。固定坐标为 r=1−2s、t=(1−r⁴)/(9−r⁴)，不得外推到全部 CDT 或全部数值目标。

## 1. 比凸性优化更早的解析障碍

在 r=±√3，z=1/t 是未分歧局部坐标，真实 forcing 为
\[
F=b+\frac c{1-t}+d\frac{(3+r^2)^3}{32r(1+r^2)},\qquad
F(0)=b\pm\frac{9\sqrt3}{16}d\ne0.
\]
最后的不等号来自关系系数有理及 d≠0，不是 generic 系数假设。
设 Q(z)=9−10z+z²，直接变换给
\[
\mathcal D_t(zY)=z\{(zQY')'+(z-3)Y\}.
\]
齐次正则解 V₀ 满足 V₀(0)=1，variation identity 是
\[
(zQV_0^2(Y/V_0)')'=V_0F/z.
\]
两次积分迫使每个到达叶都有
\[
H=\frac{F(0)}{18}zV_0(z)\log^2z+O(z\log z)+O(z).
\]
齐次解只有一次 log，有限 ramification 将最高 log 系数乘非零倍，不能修复该芽。因而合法全纯 φ:(D,0)→(C,0) 必避 s=(1±√3)/2。Kim–Ma–Ma 的 Landau 界及严格 Gamma 积分不等式给
\[
|\phi'(0)|<11/2,\qquad
\lambda=\log|\phi'(0)|<\log(11/2)<7/4.
\tag{1}
\]
这里是整个合法图类的上界。它不覆盖允许 φ 本身有极点的另一接口。若换 V 的任意可用有理函数基底，所有新基底 pullbacks 亚纯，则逆有理矩阵的 pullback 也亚纯，因此 H∘φ 亚纯，(1) 仍成立。

Root 实际全文读审两份分析终稿；两分支独立得到相同算子、常数、全叶结论和严格上界。虚两点在 b=0 时存在局部解析解，本轮没有借它们免费增加省略值。

## 2. 任意标准 literal type 的下界

此前安全两列 (0,1,1) 费用为16/9。本轮的下界不只针对这一个安全表示。
以固定 C₀ 清掉关系系数分母，令 J=C₀H，记整数系数 B,C,D，D≠0。J 与 H 生成同一个模块，解析域和渐近费用相同。对充分大的 p≥5，至次数<2p 有
\[
p^2J\equiv F_p s^pA,\qquad
p^2\theta_sJ\equiv F_p s^p\theta_sA\pmod p,
\quad F_p=B\chi_{-3}(p)+C+D\chi_{-4}(p).
\tag{2}
\]
这是完整形式幂级数的 prime obstruction，不是有限 prime 头测试。它来自真实 Lambert/dilog 系数和整数逆坐标 q(s)：q(s)^p≡s^p mod(p,s^{2p})。

取任意固定有理 Laurent 行 g=uJ+vθ_sJ+w，(u,v)≠(0,0)。在有限坏素数之外 u,v,w 的所有 Laurent 系数 p-integral；固定负阶只使(2)截断上限减少常数。已付齐次 SL₂ 不可约性保证 W=uA+vθ_sA 非有理，故存在固定正整数 k、W_k≠0。四个 prime residue classes mod12 至少一个满足 F_p≠0。Dirichlet 给该类无穷大 p，排除有限分子分母 prime 后
\[
v_p(g_{p+k})=-2,\qquad p\nmid(p+k).
\tag{3}
\]
全过程直接在 Laurent ring 中核算，没有先乘有理分母并免费继承 n^e 的卷积错误。

因此任何清该行系数的 CDT 标准 literal 分母
\[
n^e\prod_{h=1}^r d_{\lfloor b_hn+c_h\rfloor},
\qquad e\in\mathbb N,\ b_h\ge0,
\]
必须至少有两项 b_h≥1：在 n=p+k 时 n^e 不含 p，每个固定有限 b_h 因子至多给一次 p；b_h<1 最终完全不给 p。固定整数 shift c_h 不改变这一必要条件；若 b_h=1 而 k+c_h<0，只会减少贡献并强化障碍。

V 的任意 rank3 有理基底至少有两条非有理行。Definition8 的 Den_N 只依赖每条 row 的 factor multiset；各 row 独立排列 factor columns 不改变计数。两条非有理行各自有两项≥1，故 rowwise count 支配两列 (0,1,1) 的 baseline。对每个 balanced(i,n) 先逐点比较，再取 max、limsup，得到
\[
\tau^{\flat\flat}(b)\ge16/9.
\tag{4}
\]
固定 shifts 按原文 Remark6.0.12 通过非零 b 增 ε 及有限初始串处理；极限中的(4)不减少。Theorem6.0.2 的 e∈N^m 且 τsharp(e)≥0，所以
\[
\boxed{\tau^{\flat\flat}(b)+\tau^\sharp(e)\ge16/9.}
\tag{5}
\]
Root 及 punctures 分支另作独立纸核。这里的 scope 是同一 s、同一实际 rank3 模块的标准有限 lcm-factor type，包括可用有理 rebasing 和固定 shifts；不包括按 prime residue 分组的非 literal 分母、新函数族、新坐标或未证明的新 holonomy 定理。

## 3. 联合结论与另一种真实算术资产

合并(1)与(5)，同对象的全部上述标准 type 满足
\[
\lambda-\tau<-1/36<0.
\tag{6}
\]
CDT §7–8 已选择的精化只改 numerator，明文先要求正 denominator。因此改有理基底、配置 n^e、调整标准 lcm 参数以及继续优化凸性项，都不能使该固定入口成立。**结束这个实现窗口的默认投入。** 本轮不优化地图、半径、prime、参数或 Padé，也不将这一停止结论冒充数值四项线性无关的否定。

还可给下一候选作更早的预算检验。记 T(r)=原文 Bost–Charles characteristic，J_BC=T(1)。对固定外圆 z，以内变量 w 作 Jensen，再对 φ(z)=z·g(z) 作 Jensen，得到
\[
T(r)\ge\int_{\mathbb T}\log|\phi(z)|\,d\mu(z)\ge\lambda.
\]
由 Lemma7.1.4 的单调凸性及合法 a_l≤m，0≤a_k≤m。于是所选第一修正
\[
C_1=\frac1m\sum a_k^2\Delta_k\le\sum a_k\Delta_k=J_{BC}-T(r_0),
\quad J_{BC}-C_1\ge\lambda.
\]
第二修正的原文合法 s* 非负且和为1，因此
\[
J_{BC}-C_2=\sum_h s_h^*T(r_h)\ge\lambda.
\tag{7}
\]
这次(7)有独立结构证明，没有将 J_BC≥λ 直接套到扣除修正后的分子。故未精化及这两种合法凸性精化若要产生 rank3 严格矛盾，均必要 λ>3τ/2。结合(1)，更必要 τ<7/6。该分子下界只用于这两种修正及未精化式，不扩给 binomial、多图或未陈述的其它 metric 接口。

算术分支另有 AP-filtered 的完整前缀资产：按 χ−3(p)、χ−4(p) 分类，首个 surviving index k_r∈{1,2,3}，大的 prime p 只需保留至 N/k_r；小 prime 的全部幂仍保留。特定系数组合可以把前缀最小分母的 leading rate 从2降至7/4、3/2或4/3。generic 关系四类均活跃时仍为2。这是实际分母改进，**不是**已发表 CDT 的 τ 值，也不是全四项反证空间的共同降费；不能免费乘原16/9比例或声称已经获得 strict rank 矛盾。

## 4. 全局决策与下一方向

260已做正式全局复盘；261完成后 last260、count1、next264、latest268，不 reset。用户每4–8轮的要求保持默认4，最多8；连续两轮核心准入或同对象净可行性未改善则提前。稿件数量、归档和局部引理不抵消停滞。

下一262先作一个有界的**数值出口选择**，同时比较两个不同的缺口：AP-filtered 分母是否需要且值得一个新的 balanced-height holonomy 定理；真正不同的 period carrier 是否让反证关系消掉完整坏芽并产生足够净域增益。前者必须先指出新的数值目标和覆盖的完整反证系数范围，后者必须先有完整真实投影、全部关系跳变及同对象费用。仅有“分母更小”或“新载体可能有效”均不进入实现。不因改坐标、加 jets 或改名重开已停止的 χ8/RV/χ7/level14 等窗口。

AP方向优先核查的具体候选是 ζ(2)±2G 的无理性，先查已知结果与新颖性，不预称其尚未证明。真实period为 a+bL(2,χ−3)/2+cζ(2)/4+dG/2；b=0、c=d 对应 a+(d/4)(ζ(2)+2G)=0，c=−d 对应 a−(d/4)(ζ(2)−2G)=0。这两个目标各自的完整反证类恰在leading4/3的特殊范围内；因此可以缩小数值出口，无须冒称证明全部四项线性无关。

但正分母仍不充分。由(7)，例如**若**未来新费用只能付到32/27，则未精化和这两种凸性精化仍要求 λ>16/9，与(1)冲突；32/27−7/6=1/54>0。32/27在本轮不是已证新τ；这只是事前预算检验。必须先有可望使真实费用低于7/6的机制，或明确不同接口改变严格净可行性的证据，再决定是否值得补新定理，不能先写定理再希望它产生结果。

优先比较能否改变关键数值缺口和机会成本，再选择至多一个第一证书；若两者都不能给出明确的新机制，报告未准入而不硬开参数搜索。原成功标准仍是新的数值定理，goal active。
