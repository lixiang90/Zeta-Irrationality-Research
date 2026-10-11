# 纯端点 type-I 改造的严格对偶、整数节点过滤与最高 log 权基线

日期：2026-10-05。本稿只新增本文件与固定精确证书，不修改已冻结的五份对数矩报告、审阅记录或论文原件。

本轮得到一个全尺度的明确结论：对原七个 log 权施加纯端点约束后，type-I 余项严格等于旧 type-II 余项除以目标系数，规范本原整数形式完全相同。因而这一具体改造没有改善实际指数或 gcd。另构造真正改变权输入的普通 Padé 基线：只用最高 log 权，实际余项对全部尺度严格为正，有限目标系数明显较小；但其整数化与完整共同因子增长尚未证明，不能称新的 ζ(7) 无理性方法。

## 1. 原始文献接口与需要保留的差别

令
\[
w_j(u)=\frac{(-\log u)^{j-1}}{(j-1)!},\qquad 0<u<1.
\]
Smet–Van Assche 2008 作者稿的 Theorem 2.3（印刷页 5）确实处理这些合流权的 type-I 组合，Mellin transform 的 pole orders 与整数矩零点被互换。本文的端点约束改变了该问题的矩数量，不能直接声称仍是标准首一 type-I。[固定原件](E:/kimi-build/zeta5/literature/smet_vanassche2008_mellin_author.pdf)。

同文 §3 的 Apéry 接口以两项 log 密度同时进入两个余项；§§4–5 则同时约束 0、∞ 和 1，借真实反演对称消掉偶数权，得到多个奇 ζ 的线性形式。这里的多点是函数插值条件，不能替换成若干任意整数端点的数值求和；已证的“多个奇值中至少一个”也不是指定 ζ(7)。

Sorokin 的 1994 两页原始短文另给实际 mixed Nikishin 系统，含显式 Rodrigues/三变量积分及渐近结论，处理 ζ(3)。它说明真正改系统可以改变余项，而不是仅将同一矩系统转置；其定理没有覆盖这里的 ζ(7)。[出版原件](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=1187&what=fullteng)／[本地归档](E:/kimi-build/zeta5/literature/sorokin1994_nikishin_zeta3_english.pdf)，Russian Math. Surveys 49:2,176–177，DOI `10.1070/RM1994v049n02ABEH002229`。

Wolfs `2401.08312v2` 的数值独立定理使用严格 `p<q` 的 factorial 余裕；其 §5.2 的 `p=q` polylog 边界不能免费继承该证明。本轮没有通过转置消除此缺口。[固定原件](E:/kimi-build/zeta5/literature/wolfs2024_multiple_orthogonal_hypergeometric_v2.pdf)。

## 2. 一个全尺度可计算、纯端点的 type-I 族

固定整数 `q≥1,n≥2` 与实数 `a>0`。记
\[
s=n-1,\qquad d=qs,\qquad
E=\operatorname{span}\{u^r w_j(u):0\le r<s,1\le j\le q\}.
\]
寻求密度
\[
F(u)=w_q(u)+(u+a)G(u),\qquad
G(u)=\sum_{j=1}^q\sum_{r=0}^{s-1}b_{jr}u^r w_j(u), \tag{1}
\]
满足 `∫u^mF(u)du=0`，`0≤m<d`。这相当于
\[
F=\sum_{j=1}^q A_j(u)w_j(u),\quad
\deg A_j\le n-1,\quad A_j(-a)=\delta_{jq}. \tag{2}
\]
实际系数由一个完全明确的矩矩阵给出：
\[
C(a)_{m,(j,r)}=\frac a{(m+r+1)^j}+\frac1{(m+r+2)^j},
\qquad v_m=\frac1{(m+1)^q},
\qquad b=-C(a)^{-1}v. \tag{3}
\]
当 `a∈Q` 时所有系数为有理数。没有使用非显式 Siegel 存在论证。

**可逆性证明。** 在 `t=-logu` 下 E 为指数多项式 `e^{-rt}t^{j-1}` 的空间，实指数的总重数为 d，非零函数最多有 `d−1` 个零点，计重数。这一扩展 Chebyshev 事实也可由逐次乘指数与 Rolle 归纳证明。

若 `C(a)` 有非零核，则 `(u+a)G` 的前 d 个普通矩为零。若其符号变化点不足 d 个，将这些点的线性因子相乘，所得 degree 至多 `d−1` 的 polynomial 与 `(u+a)G` 之积在 `(0,1)` 固定号且非零，积分不可能为零。故它至少有 d 个符号变化。`u+a>0` 不改变 G 的符号，与 E 的零点上界矛盾。两端 log 奇性可积。证毕。

对齐次纯端点解，最高端点值若为零，则所有 `A_j` 均被 `u+a` 整除，重复核论证便得全零。因此 (1) 是唯一的归一化解，未归一化问题一维，最高目标系数确实非零。这个论证只用 ECT 与正因子，没有将 ECT 等同 Nikishin 系统。

标准平衡 type-I 有 `qn−1` 个矩零点；这里纯端点消去 `q−1` 个非目标系数后保留的是 `q(n−1)` 个矩零点。不能宣称这些额外约束没有成本。

## 3. 实际函数、纯目标身份与 Mellin 零点

对 `z∉[0,1]` 定义实际 Cauchy 函数
\[
\mathcal F(z)=\int_0^1\frac{F(u)}{z-u}\,du.
\]
若 `A_j(u)=Σ_r a_{jr}u^r`，则逐单项积分给
\[
\mathcal F(z)=\sum_{j=1}^q A_j(z)\operatorname{Li}_j(1/z)-T(z),
\quad
T(z)=\sum_{j=1}^q\sum_{r\ge1}a_{jr}
 \sum_{\ell=1}^r\frac{z^{r-\ell}}{\ell^j}. \tag{4}
\]
因此 `𝔽(z)=O(z^{-d-1})`，在 `z=-a` 精确只有最高 polylog 系数。

直接由 (1) 得更简洁的实际积分
\[
\mathcal I_a:=\int_0^1\frac{F(u)}{u+a}\,du
=-\operatorname{Li}_q(-1/a)+
 \sum_{j,r}\frac{b_{jr}}{(r+1)^j}. \tag{5}
\]
`a=1` 时为 `η(q)+rational`；对 `q≥2`，`η(q)=(1−2^{1−q})ζ(q)`，`q=1` 则为 `log2`。一般有理 `a>0` 的目标是 `Li_q(-1/a)`，并非 ζ(q)。

实际 Mellin 函数也完全明确：
\[
\widehat F(w)=\frac1{w^q}+
 \sum_{j,r}b_{jr}\left(\frac a{(w+r)^j}+
 \frac1{(w+r+1)^j}\right). \tag{6}
\]
它有 `w=1,…,d` 的零点。统一 denominator 可取 `∏_{r=0}^{n-1}(w+r)^q`，故 numerator 为这 d 个线性零因子乘 degree 至多 `q−1` 的 polynomial。(3) 给这有限自由 numerator 的全部端点约束，不需要再扫描首一解。

截至这里只证明了目标系数非零与真实矩消元；实际积分非零不能由这些结论单独推出。

## 4. 严格对偶：它就是旧 type-II 逼近的目标归一化

令旧候选
\[
R(u)=R_{s,q}(u)=\sum_{r=0}^{qs}(-1)^r
 \binom{qs}{r}\binom{s+r}{s}^q u^r,
\quad s=n-1. \tag{7}
\]
它对 E 正交；`R(-a)>0`，因为 (7) 在负实轴上是严格正项和。

**对偶恒等式。** 对所有 `n≥2,q≥1,a>0`，
\[
\boxed{\mathcal I_a=
 \frac1{R(-a)}\int_0^1\frac{R(u)w_q(u)}{u+a}\,du.} \tag{8}
\]
证明只需将同一个积分展开两次。由 `G∈E`、`R⊥E`，
\[
\int\frac{RF}{u+a}=\int\frac{Rw_q}{u+a}+\int RG
=\int\frac{Rw_q}{u+a}.
\]
另一方面 `(R(u)−R(-a))/(u+a)` 的 degree 为 `d−1`，而 F 消去全部这些普通矩，所以
\[
\int\frac{RF}{u+a}=R(-a)\int\frac F{u+a}.
\]
得到 (8)。没有调用任何目标值的无理性。

若 `a∈Q`，两边都是同一个目标周期的有理仿射形式，差一个非零有理倍，因此化成互素整数系数后完全相同。尤其 `a=1,q=7` 时，规范本原 `cζ(7)+e` 与旧尺度 `s=n−1` 的形式逐项一致。新 n 不能与旧 n 直接同标比较。

于是原型的实际复 saddle、相位抵消和完整 gcd 缺口全部保留。type-I 归一化使裸误差看起来小了 `R(-1)` 的指数，但该系数必须在本原化时付回；这不是新的丢番图节省。非零子序列也与旧族完全相同。

## 5. 矩阵 determinant 正好含同一个目标系数

写 `C(a)=aC_0+C_1`，令 `P=R/lc(R)` 为 degree d 的首一 polynomial。`C_1` 的前 `d−1` 行为 `C_0` 的后一行；最后一行由 `P⊥E` 给出。因而
\[
C_1=TC_0,
\]
其中 T 是 characteristic polynomial 为 P 的 row companion matrix。故
\[
\boxed{\frac{\det C(a)}{\det C_0}=\det(aI+T)
=(-1)^dP(-a)
=\frac{R(-a)}{\binom{(q+1)s}{s}^{q}}.} \tag{9}
\]
这既重证可逆，也精确识别目标归一化系数。右边不能当作免费公因子。

按列 `(r,j)` 排序，confluent Cauchy determinant 还给
\[
\det C_0=(-1)^{s q(q-1)/2}
\frac{\prod_{0\le m<m'<d}(m'-m)
 \prod_{0\le r<r'<s}(r'-r)^{q^2}}
 {\prod_{m=0}^{d-1}\prod_{r=0}^{s-1}(m+r+1)^q}. \tag{10}
\]
它可由普通 Cauchy determinant 合并重复列节点得到；列用导数除阶乘表示，产生显示的符号，没有遗漏 factorial。固定证书同时核了 (9)、(10) 与 companion relation。

## 6. a=1,2 多整数节点：完整函数过滤会约掉新增核

对任意 `R∈Q[u]` 写 `R=(u+a)Q_a+B_a`。实际身份为
\[
J_{q,a}(R):=\int_0^1\frac{R(u)w_q(u)}{u+a}\,du
=-R(-a)\operatorname{Li}_q(-1/a)
 +\sum_r\frac{[u^r]Q_a}{(r+1)^q}. \tag{11}
\]
加入 `a=2` 后，新的非有理输入为 `Li_q(-1/2)`。若采用**明确消去全部非目标 polylog 系数**的纯目标规则，则非零新核系数要求 `R(-2)=0`，因而 `R=(u+2)P`，新核被约掉，只剩 polynomial rational moments。

具体地
\[
J_{q,2}((u+2)P)=\int Pw_q,
\quad J_{q,1}((u+2)P)=J_{q,1}(P)+\int Pw_q,
\]
所以
\[
\boxed{J_{q,1}((u+2)P)-J_{q,2}((u+2)P)=J_{q,1}(P).} \tag{12}
\]
这一个最直接的双节点纯目标改造完全退回原核。若不用相减，新增项仍只是已有可计算 rational boundary；没有引入新的目标周期信息。

这些论断是系数层的严格过滤障碍，不是数值独立定理。不能宣称已经证明 `1,ζ(7),Li_7(-1/2)` 数值独立。函数层不同节点 `Li_j(-x/a)` 则可由各自 `x=-a` 的 monodromy 与 log 的超越性证明在 `C(x)` 上独立，说明此污染是真实不同函数块，不是免费 functional identity。

对旧 (7)，`R(-2)>0` 对全部尺度成立。因此不加因子或额外周期关系，非零 `a=2` 核不能按上述纯系数规则保留纯 ζ(q)。本结论不排除利用另行严格证明的数值周期关系或真正不同 mixed 系统。

## 7. 真正改变输入：只用最高 log 权的普通 Padé 基线

对 ζ(7)，另一明确输入是只保留正测度
\[
d\mu(u)=w_7(u)du,\qquad
\mu_m=\int u^m d\mu=\frac1{(m+1)^7}.
\]
令 `P_s` 为其首一普通 orthogonal polynomial，`degP_s=s`。系数从正定 Hankel 矩阵
\[
H_{mr}=\frac1{(m+r+1)^7},\quad
v_m=\frac1{(m+s+1)^7},\quad
P_s(u)=u^s-\sum_{r=0}^{s-1}(H^{-1}v)_r u^r \tag{13}
\]
精确得到。它有 s 个单纯 `(0,1)` 零点，`P_s(-1)≠0`。

将 §2 的 E 换成 `span{u^r w_7:0≤r<s}`，同一对偶证明给一个纯端点 type-I 密度
`F=w_7+(u+1)G`，其归一化积分为 `J_{7,1}(P_s)/P_s(-1)`。这时 corresponding type-II polynomial 已改变，不是 (7)。

**全尺度实际正性。** 普通正交给
\[
\boxed{\frac{J_{7,1}(P_s)}{P_s(-1)}=
\frac1{P_s(-1)^2}\int_0^1
\frac{P_s(u)^2w_7(u)}{1+u}\,du>0.} \tag{14}
\]
因为 `(P_s(u)−P_s(-1))/(u+1)` degree `s−1`，其与 `P_s w_7` 的积分为零。这是实际余项对所有尺度非零的证明，没有把 ζ(7) 无理当作前提。

同时 `P_s(z)Li_7(1/z)−S_7(z)=O(z^{-s-1})`，除以 degree s 的 P 后是普通 Padé 的 `2s+1` 阶无穷远接触。它是经典 Stieltjes/Markov Padé 接口，不作全球新颖性主张。

这里实际最高 Cauchy 函数的最小齐次微分阶数仍为 8：`P_s(1)≠0`，冻结[结构报告 §3](E:/kimi-build/zeta5/research/odd_zeta_log_structure_20261005.md)的 simple-pole cyclic 证明原样适用。它没有降低标准 Li connection 的秩或扩大解析域。

这一输入有较少 polynomial 系数与真实正余项，值得作为比较基线；但每个 moment 仍付第七次幂分母。不能仅用 degree s 推断整系数归一化很小。把 (13) 乘 `L_{2s}^7` 后用 Cramer 可给一个安全 determinant 倍数，其粗高度为 `exp(O(s²))`；这只是上界，不是实际高度下界或失败定理。

### 7.1 每个尺度的完整本原接口

取最小正整数 `D_s` 使 `Q_s=D_sP_s∈Z[u]`；Q 的 polynomial 系数 gcd 为 1。写
\[
Q_s=(u+1)T_s+B_s,\quad B_s=Q_s(-1)\ne0,
\qquad S_s=\int T_sw_7=\frac{t_s}{M_s},\quad
\gcd(t_s,M_s)=1,\ M_s>0.
\]
`M_s|L_s^7` 是安全整系数 polynomial 除法上界，尚未证明接近等号。由 (11)，
\[
J_{7,1}(Q_s)=\frac{63B_s}{64}\zeta(7)+\frac{t_s}{M_s}.
\]
定义完整 content 与规范形式
\[
g_s=\gcd(|63M_sB_s|,|64t_s|),\qquad
\boxed{\ell_s=\operatorname{sgn}(B_s)\frac{64M_s}{g_s}J_{7,1}(Q_s)
=\frac{64M_s|B_s|}{g_s}\mathcal I_s>0.} \tag{15}
\]
其中 `𝓘_s=J(P_s)/P_s(-1)`。这是互素整数目标系数，没有遗漏 `D_s` 或 rational boundary 的 gcd。

逐素数精确为
\[
v_p(g_s)=\min\{v_p(63)+v_p(M_s)+v_p(B_s),
v_p(64)+v_p(t_s)\}. \tag{16}
\]
对奇 p，可化为 `g_{s,odd}=gcd(63B_s,t_s)_{odd}`；任何实际 denominator 奇素数 `p|M_s` 不会再被 content 约掉。对 2，若 `2|M_s`，估值为 `min(v_2(M_s)+v_2(B_s),6)`；否则为 `min(v_2(B_s),6+v_2(t_s))`。尤其
\[
g_s\le64\cdot63|B_s|,\qquad
\ell_s\ge \frac{M_s}{63}\mathcal I_s. \tag{17}
\]
这些是每个尺度的精确／有限不等式，不假定 denominator 或 content 的渐近。s=1 的 `(D_s,B_s,M_s,g_s)` 为 `(128,-129,1,1)`；s=2 为 `(3974251392,4553325433,1,9)`。`M_s=1` 目前只在这两个固定例中认证，不能外推。

### 7.2 可实际移植的普通正交 logarithmic asymptotics

这次只有一个正生成测度，支持恰为 `[0,1]`，密度在内部严格为正；无额外负轴支持。可直接应用 [Fidalgo Prieto–López Lagomasino 固定稿](E:/kimi-build/zeta5/literature/fidalgo_lopez2010_nikishin_perfect_v1.pdf) 印刷页 33 的 Lemma 5.3，而不需将七 log AT-system 套成多测度 Nikishin theorem。取该 lemma 的 `σ=w_7du`、连续正乘子 `φ_s≡1`、外场 `φ=0`；支持 `[0,1]` 是 regular compact set，当然 quasi-regular。下面明确核 `σ∈Reg`。

本测度的 regularity 可以直接核：单一 Chebyshev polynomial 给 monic norm 的上界；任意紧区间 `[ε,1−ε]` 上 `w_7` 有正下界，用该区间 monic Legendre norm 给下界，再令 `ε↓0`。因此
\[
h_s:=\int P_s^2w_7,\qquad h_s^{1/s}\longrightarrow\frac1{16}.
\]
该 lemma 给归一化零点计数测度 `ν_s` 弱收敛到 `[0,1]` 的零外场 equilibrium，即 arcsine measure。因为全部零点均在 `(0,1)`，而 `log(1+u)` 在闭区间连续，
\[
\frac1s\log|P_s(-1)|=\int\log(1+u)d\nu_s(u)
\longrightarrow\int_0^1\frac{\log(1+u)}{\pi\sqrt{u(1-u)}}du
=\log\frac{3+2\sqrt2}{4}.
\]
最后一个积分可对一般 `log(a+u)` 对 a 求导，再由无穷远常数确定。因此
\[
|P_s(-1)|^{1/s}\longrightarrow\frac{3+2\sqrt2}{4}.
\]
在 (14) 中分子介于 `h_s/2` 与 `h_s`，故实际全尺度误差有
\[
\boxed{\lim_{s\to\infty}\frac1s\log\mathcal I_s
=-2\log(3+2\sqrt2).} \tag{18}
\]
这是经典普通 Padé 输入的真实解析指数，不是新强 saddle 定理，也没有支付 (15) 的整数乘子。由 (17)，若实际分母后来被证明满足
\[
\liminf_s\frac1s\log M_s>2\log(3+2\sqrt2),
\]
则这一基线的本原形式指数增长；目前没有证明该前提。反之，小 M 也不能忽略 `|B_s|/g_s`。后续必须研究 (15) 的全部成本，不能把单独的正余项或固定较少 bits 当作净指数优势。

### 7.3 Catalan 的同一实际 Markov 接口

Catalan 的实际积分经 `u=t²` 变为
\[
G=\int_0^1\frac{-\log t}{1+t^2}dt
=\int_0^1\frac{d\mu_G(u)}{1+u},\qquad
d\mu_G(u)=\frac{-\log u}{4\sqrt u}\,du,
\quad (\mu_G)_m=\frac1{(2m+1)^2}. \tag{19}
\]
这是实际正测度及收敛积分，非形式周期投影。令 `P_s^G` 为它的首一普通 orthogonal polynomial；Hankel 矩阵与 (13) 相同构造，只将 moments 换为 `(2m+1)^{-2}`。平方身份精确给
\[
\mathcal I_s^G=
\frac{\int P_s^G(u)/(1+u)\,d\mu_G}{P_s^G(-1)}
=\frac{\int (P_s^G)^2/(1+u)\,d\mu_G}{P_s^G(-1)^2}>0. \tag{20}
\]
密度内部正、有限且在每个紧内部区间有正下界；Chebyshev/Legendre regularity 证明同样适用。取同一 Lemma 5.3 的 `σ=μ_G、φ_s≡1、φ=0`，全部假设再满足。其零点弱收敛与 (20) 给
\[
\lim_s\frac1s\log\mathcal I_s^G=-2\log(3+2\sqrt2). \tag{21}
\]
两目标共享这个单区间 Markov 几何，不意味着它们共享已闭合的整数预算。

每尺度取最小整系数归一化 `Q_s^G=D_s^GP_s^G`，写
\[
Q_s^G=(u+1)T_s^G+B_s^G,\qquad
S_s^G=\int T_s^Gd\mu_G=t_s^G/M_s^G
\]
为约分分数。实际身份与完整 content 是
\[
J_G(Q_s^G)=B_s^G G+t_s^G/M_s^G,
\quad g_s^G=\gcd(M_s^G|B_s^G|,|t_s^G|)
=\gcd(|B_s^G|,|t_s^G|).
\]
故规范本原值
\[
\boxed{\ell_s^G=\operatorname{sgn}(B_s^G)
\frac{M_s^G}{g_s^G}J_G(Q_s^G)
=\frac{M_s^G|B_s^G|}{g_s^G}\mathcal I_s^G
\ge M_s^G\mathcal I_s^G>0.} \tag{22}
\]
安全 boundary denominator 仅保证
`M_s^G|(lcm(1,3,…,2s−1))²`；`D_s^G`、目标系数与 content 的实际增长仍须单独研究。没有将该上界当作实际下界。

唯一预先指定 Catalan 例 `s=1` 为
\[
P_1^G=u-\frac19,\quad Q_1^G=9u-1,
\quad B_1^G=-10,\ S_1^G=9,
\quad \ell_1^G=10G-9.
\]
完全有理 Euler 界认证 `1/8<10G−9<1/4`。这个单项已是正的小整数型，但没有证明其后全部本原值趋零；一项小值不能给无理性。

### 7.4 原项目固定组合 `3ζ(3)+ζ(5)` 的同一入口

令 `Θ=3ζ(3)+ζ(5)`。实际线性身份为
\[
\boxed{\Theta=\int_0^1\frac{d\mu_\Theta(u)}{1+u},\qquad
d\mu_\Theta=(4w_3+\tfrac{16}{15}w_5)du,\qquad
(\mu_\Theta)_m=\frac4{(m+1)^3}+\frac{16}{15(m+1)^5}.} \tag{23}
\]
因为 `4η(3)=3ζ(3)`、`(16/15)η(5)=ζ(5)`，这个身份未引入其他周期。密度内部严格为正，质量有限，moments 全有理；同一 Hankel 构造、Gram 平方正性、Chebyshev/Legendre regularity 与 Lemma 5.3 给全部尺度的真实正余项及 `−2log(3+2√2)` 裸误差指数。整系数 `Q=(u+1)T+B` 给 `J=BΘ+t/M`，规范 content 仍为 `gcd(M|B|,|t|)`；目标根分母与完整整数系数增长没有闭合。这里证明的是对指定组合的实际接口，尚不是它的无理性。

同理，任意非零有限**正有理系数**的奇 ζ(k)（`k≥3`）及 Dirichlet beta(k)（整数 `k≥1`）组合可得到内部正、同一支持 `[0,1]` 的 rational-moment 测度：ζ(k) 使用 `w_k/(1−2^{1−k})`，而 β(k) 在 `u=t²` 后使用
`(-logu)^{k−1}/(2^k(k−1)!√u)`，其 moments 为 `(2m+1)^{-k}`。这仅统一 Markov 正性和裸解析指数；它不统一已经支付的整数预算，也不自动适用于负系数组合。

## 8. 固定证书与本轮结论的量词

固定[脚本](E:/kimi-build/zeta5/research/odd_zeta_mixed_pade_20261005_verify.py)／[JSON](E:/kimi-build/zeta5/research/odd_zeta_mixed_pade_20261005_verify.json) 已通过四个指定对偶输入：`(n,q,a)=(2,3,1),(2,7,1),(3,7,1),(2,7,2)`。证书核全部矩、端点多项式、Mellin 零点、Cauchy determinant、companion determinant、目标 rational part 和本原系数。

| 输入 | 对应旧尺度 | 目标本原系数 bits | 完全有理认证 |
|---|---:|---:|---|
| 七 log 纯 type-I `n=2` | 旧 `s=1` | 81 | 与旧形式逐系数相同；负值，绝对值至少 `2^48` |
| 七 log 纯 type-I `n=3` | 旧 `s=2` | 180 | 与旧形式逐系数相同；负值，绝对值至少 `2^117` |
| 最高 log 普通 Padé `s=1` | 不同权输入 | 13 | 规范形式 `8127ζ(7)−8192`，正值且大于 1 |
| 最高 log 普通 Padé `s=2` | 不同权输入 | 35 | 规范形式 `31873278031ζ(7)−32139312192`，正值且至少 `2^16` |

前两行的有限大值不是新的全尺度本原失败证明；全尺度结论是 (8) 的严格同一性，原族未闭合的 content 问题仍在。普通最高 log 的两行也只是固定基线，不能把较少 bits 外推为全尺度预算改善。

证书的 period 区间来自 η(7) 或 Catalan 交错 moment 的正项 Euler 展开与有理尾界，不调用 ζ/G 的数值小数。另核 `P=R_{1,7},R=(u+2)P` 的 (12) 精确身份及唯一 Catalan `s=1` 的正小值。无参数扫描。

目前应继续的具体接口是改变真实权/矩空间后同时控制 `D_sP_s(-1)` 与 rational boundary 的完整 content，或使用文献中额外端点/反演条件构造真正不同 mixed 系统。单纯将旧七 log 系统转置，或用一个额外整数节点再系数过滤，没有新增丢番图预算能力。
