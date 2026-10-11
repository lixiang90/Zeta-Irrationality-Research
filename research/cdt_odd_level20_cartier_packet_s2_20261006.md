# level20 六积分最高 packet 的第二层：精确提升条件与常系数障碍

日期：2026-10-06。本稿新建，不改已经冻结的 packet_matrix 稿。研究的是六个实际正规积分的 native、constant-coefficient、完整前缀评价；不是原 CDT 全整格的免费收益。结论包括：一般的 Bockstein 充要条件；保留 genuine Frobenius lift 的两种第二层缺陷；以及一个实际源的精确分类——除固定坏素数外，N>p+5 时纯六列中没有 primitive constant-coefficient S2 行。这个障碍不排 polynomial coefficients 或与旧 H 行混合，没有排除所有第二层方法，也没有新的数值无理性定理。

## 1. 固定 integral prefix 和 native source

沿用 [packet matrix](cdt_odd_level20_cartier_packet_matrix_20261006.md) 的符号。源固定为 A₋、H₋，

\[
 Q_j=t^j/D_-,\quad D_-=(1-t)N_-C_-,\quad
 I_j=\int_0^t\{Q_jH_--Q_j(0)H_-(0)\}\,dt/t,
 \quad0\le j\le5.
\tag{S1}
\]

反证假设 L(3,χ₅)∈Q，只排其固定分母与规范坏素数。令 O=O_{K,𝔭}、k=O/𝔭，p在K未分歧，故可用p记录层。取p≥7、p<N≤p²，并在t^N截断，最后 coefficient是n=N−1。使用

\[
 Y_j=p^3Q_jH_-,\quad Z_j=p^4I_j,
 \quad E_N(c)=\sum_jc_jZ_j\in O[t]/t^N.
\tag{S2}
\]

这些都是完整 integral prefixes。这里 source coefficient向量 c∈O⁶ 是常系数；primitive 指 cmod𝔭非零。对所有n>0，精确 coefficient身份是

\[
 [t^n]Z_c=\frac p n[t^n]Y_c,
 \quad Y_c=p^3\frac{P_c(t)}{D_-(t)}H_-,
 \quad P_c=\sum_{j=0}^5c_jt^j,
\tag{S3}
\]

且 Zc(0)=0。正规化的 constant只出现在 Euler身份

\[
 \vartheta Z_c=pY_c-p^4Q_c(0)H_-(0),
\tag{S4}
\]

其 constant项与Yc(0)精确相消；modp²时这两个constant各自为零。

## 2. 任意深度一关系的提升充要条件

给定 \(\bar c_0\in\ker\overline E_N\)，任取 integral lift \(\hat c_0\)。由于 E_N(ĉ₀)∈p·target lattice，可定义

\[
 d_N(\bar c_0)=E_N(\hat c_0)/p\pmod p.
\tag{S5}
\]

更换 lift ĉ₀→ĉ₀+p h使d增加\(\overline E_Nh\)。因此 obstruction class

\[
 [d_N(\bar c_0)]\in\operatorname{coker}\overline E_N
\tag{S6}
\]

与lift选择无关，并给严格充要条件

\[
 \boxed{\exists c_1\in O^6:
 E_N(\hat c_0+pc_1)\equiv0\pmod{p^2}
 \iff[d_N(\bar c_0)]=0.}
\tag{S7}
\]

这是实际 finite-prefix evaluation 的线性提升，不假设任何更高 Frobenius 定理。c₀≠0时成功的行是source primitive；若c₀=0，只是原source行已有共同p-content，不能把这种行重新数成免费primitive S2方向。

深度一矩阵稿给\(\overline E_N=V_{p,N}\overline M_p\)，所以kerMₚ包含于kerEₙ，但可能严格更小。S7必须用于整个kerEₙ；不能将一个有限前缀核自动当成完整formal矩阵核。

## 3. 第二层为何不是把 M_p 简单再提升一次

置ε=χ(p)，target为 A₋、f₋（ε=1）或 A₊、f₊（ε=−1）。令 fε(z)是实际target芽的degree<p integral截断。真实 [Frobenius source身份](cdt_odd_level20_frobenius_20261006.md) §3给

\[
 p^3H_-\equiv A_-(t)f_\varepsilon(s(t))
 \pmod{p^3,t^{p^2}},\quad
 s(t)=t(q(t)^p),\quad s(t)\equiv t^p\pmod p.
\tag{S8}
\]

s在characteristic zero的首阶恰为p。模p²不能把s换成tᵖ。令 gⱼ=QⱼA₋；记 Cₜ⁰为characteristic-zero coefficient extraction Σaₙtⁿ↦Σaₚₙtⁿ，用于integral prefix。

由modp Cartier兼容性，以下slow degree<p的缺陷合法p-integral：

\[
 \mathcal D_{p,j}(t)=\frac{
 C_t^0(g_j(t)f_\varepsilon(s(t)))
 -(T_pB_j^-/S)(t)f_\varepsilon(t)}{p}\pmod{t^p}.
\tag{S9}
\]

分子divp的证明正是深度一P7加Cartier乘积规则；不假设charzero extraction在换坐标后仍相容modp²。其constant为0，故唯一\(\Upsilon_{p,j}(0)=0\)满足

\[
 \vartheta\Upsilon_{p,j}=\mathcal D_{p,j}\pmod{t^p}.
\tag{S10}
\]

在k[t]/tᵖ²中定义另一个确定缺陷

\[
 \mathcal O_{p,j}(t)=
 \sum_{\substack{1\le n<p^2\\p\nmid n}}
 \frac{[t^n](\bar g_j(t)\bar f_\varepsilon(t^p))}{n}t^n.
\tag{S11}
\]

它只有非p倍的positive次数。逐系数S3、S8与完整矩阵\(T_pB_j^-=\sum_i M_{p,ij}B_i^{target}\)给严格第二层分解

\[
 \boxed{Z_j(t)\equiv
 \left[\sum_i M_{p,ij}\Xi_i^{Af,target}(u)
       +p\Upsilon_{p,j}(u)\right]_{u^{<p},\ u=t^p}
       +p\mathcal O_{p,j}(t)
 \pmod{p^2,t^{p^2}}.}
\tag{S12}
\]

S12的两个缺陷角色不同：Υ校正p倍次数上的genuine-lift／坐标Cartier误差；O是非p倍次数的第二层项。后者不在单纯fast-variable矩阵像中。

weight4算术Hecke精确尾项是

\[
 T_pB_j^-=U_pB_j^-+\varepsilon p^3B_j^-(q^p).
\tag{S13}
\]

因而Uₚ≡Tₚmodp³；在S9除p后此尾项只出现p²，不能消掉S12的第一p层 O或Υ。不能从“尾项有p³”推断深度一Cartier矩阵自然提升到modp²或modp³。

Ξ仍是完整真实primitive

\[
 \Xi_i^{Af,target}=J_{Q_i,H^{target}}
                     +\varepsilon\Theta J_{Q_i,A^{target}}.
\tag{S14}
\]

Υ、O是本p、本prefix的算术缺陷，不声明成独立于p的共同解析叶函数，更不能以它们当作免费CDT species。

## 4. 完整前缀的非p倍项给出精确常系数分类

令κ=5√5/4。实际target的第一Taylor coefficient为

\[
 \eta_\varepsilon=[t]f_\varepsilon=1-\varepsilon\kappa,
 \quad\operatorname{Norm}(\eta_\varepsilon)=-109/16.
\tag{S15}
\]

以下另排p=109，使ηε在每个好place均为unit。A₋(0)=−1/5、D₋(0)=1也为unit。

若\(E_N(c)\in p^2\,target\)，S4迫\(\overline Y_c=0\bmod t^N\)。S8的modp reduction则是

\[
 \overline Y_c=(A_-/D_-)\,\overline P_c(t)\,
                 \bar f_\varepsilon(t^p)
 \quad\bmod t^N.
\tag{S16}
\]

\(\bar f_\varepsilon(t^p)=\eta_\varepsilon t^p\cdot unit\)。因此

\[
 \boxed{E_N(c)\equiv0\pmod{p^2}
 \Longrightarrow t^{N-p}\mid\overline P_c(t).}
\tag{S17}
\]

反向也成立为**lift存在性**：给定degree≤5的P₀∈t^(N−p)k[t]，选择其低于N−p的coefficients为exactzero的integral polynomial lift P。S8中的\((A_-/D_-)P f_\varepsilon(s)\)首阶至少N，所以Yc的完整n<N前缀divp²；由S3，p∤n时还多一层，n=pm时乘1/m，仍divp²。这个lift满足S2，且P₀≠0时source primitive。

结合两向得到实际的精确分类

\[
 \boxed{\operatorname{image}\bigl(
 \{c\in O^6:E_N(c)\in p^2target\}\to k^6\bigr)
 =\{c_0:t^{N-p}\mid P_{c_0}\}.}
\tag{S18}
\]

其dimension为\((6-(N-p))_+\)。尤其

\[
 \boxed{p+5<N\le p^2
 \Longrightarrow\text{纯六列native source不存在primitive常系数S2行。}}
\tag{S19}
\]

这不是只排某一个Mₚ-kernel lift，而是该完整窗口中所有constant-coefficient primitive行。它不依赖ordinary密度，也不需要全素数谱分解。

对原完整\(c_0\in\ker\bar M_p\setminus0\)还可显式看到第一次失败。matrix第一constant项给P₀(0)=0，故m=ordP₀∈{1,…,5}。由S16，n=p+m不是p倍，S11中对应coefficient为

\[
 [t^{p+m}]\mathcal O_{p,c_0}
 =-\eta_\varepsilon[t^m]P_0/(5m)\ne0.
\tag{S20}
\]

changing lift c→c+p c₁仅增加p·barE(c₁)，后者只有p倍support。因此不能纠正这项；所谓把c₀ lift成c₀+p c₁的自由度不能移去这个Bockstein obstruction。

短窗口p<N≤p+5则有S18所列lift，来自原点高阶vanishing；不把这种极短prefix结论认领成当前小素数窗口的净CDT收益。

### 4.1 原 native 六列的 Smith 指数因此精确受控

仍取S15的unit条件及N>p+5，令E_N的六个Smith指数为a₁,…,a₆（rank不足的方向记∞）。若有aᵢ≥2或∞，unimodular source变换中的对应unit向量给primitive S2行，与S19矛盾。因此

\[
 \boxed{\operatorname{rank}_{K_\mathfrak p}E_N=6,
 \qquad a_i\in\{0,1\}.}
\tag{S20a}
\]

这一column-fullrank由本地no-S2推出，不是把characteristic-zero actualrank误当成所有有限N的rank。于是\(\sum a_i=\dim_k\ker\bar E_N\)。

target Ξ_i 的首阶i+1，first6 coefficients矩阵triangular，diagonal为\(-\eta_\varepsilon/[5(i+1)]\)（i=0,…,5），在p≥7与ηunit时全部是unit。因此N≥6p+1时slow前缀含六个positive coefficients，Vₚ,N有rank6，且

\[
 \boxed{N\ge6p+1\Longrightarrow
 \ker\bar E_N=\ker\bar M_p,\quad
 \sum_{i=1}^6a_i=\dim_k\ker\bar M_p.}
\tag{S20b}
\]

若再满足packet_matrix稿的fixed-good谱投影条件，右边恰为old退化的2与new退化的1之条件和；这里不追加密度假设。S20a/b仅涉及同一个native常系数六列source与整个t^N前缀，未转移到CDT changed metric或混合整格。

## 5. 允许混合旧 H 行时：可检验的充要接口

S19仅是纯六列常系数结论。若允许加上原p³H的old native columns，例如

\[
 T=(Y,\vartheta Y,\vartheta^2Y),\qquad Y=p^3H_-,
\]

并以**p倍source coefficients**补正，即

\[
 E_N(\hat c_0+pc_1)+p\sum_{r=0}^2\beta_rT_r,
\tag{S21}
\]

其深度一c₀保持原先的kerE条件；深度二lift存在的充要条件变为

\[
 \boxed{d_N(c_0)\in
       \operatorname{image}\bar E_N+
       \langle\bar T_0,\bar T_1,\bar T_2\rangle_k.}
\tag{S22}
\]

旧 columns 的modp packet是

\[
 \bar T_r=(\vartheta^rA_-)\bar f_\varepsilon(t^p),
 \quad r=0,1,2,
\tag{S23}
\]

因为ϑ\(f(t^p)\)=0modp。它们有非p倍support，可能纠正S20，所以不能将纯六列的no-S2外推到S21。若使用旧CDTspecies的Δ² clearing，须相应替换T并核source整格与coefficients，不能直接照抄native列的净预算。

具体地，令g=Δ²，旧实际species是gH₋、gϑH₋、gϑ²H₋。它们在**共同p⁴ evaluation**中的列是p·(gY,gϑY,gϑ²Y)，本来已有baseline1。因此S21的显式p是在p³-normalized old columns坐标中写出的；换成共同p⁴ source时，old coefficientsβ本身不需再人为含p。正确first-layer补正空间是\(\langle(gA_-)f(t^p),g(\vartheta A_-)f(t^p),g(\vartheta^2A_-)f(t^p)\rangle\)，并须按实际允许的polynomial shifts扩张。这个坐标区别不能用于免费增加一份baseline。

对c₀∈kerM，还可在本地看到一个明确的建设接口：\(\vartheta(E_N(\hat c_0)/p)=(Q_{c_0}A_-)f(t^p)\bmod p\)。若能在**modp、指定完整前缀**找到rational且integral-at-origin的u满足\(\vartheta(uA_-)=Q_{c_0}A_-\)，并证明uA₋f(tᵖ)属于实际允许的old first-layer空间，便可消去off-p residue项；两者差的Euler derivative为零，仍可能留下slow-variable p倍项，须另用S22的coker条件。本文没有构造这样的bounded-degree u，没有把它误称为characteristic-zero actual exactness，也没有忽略剩余slow obstruction。

S22也允许扩充一组**明确指定且integral**的old correction columns（如polynomial shifts）：将其modp images加入右边即可。这是一个完整finite-prefix矩阵的可验证条件，不是已经构造出的成功关系。若改用p³-normalized old columns并允许它们的source coefficients不含前置p，从而离开共同p⁴ baseline1约定，就必须从整个混合evaluation的ker出发再用S5–S7，不能沿用纯六c₀的Bockstein账本。共同p⁴坐标中的old coefficientsβ可以是unit，这已经由S21/S22覆盖。

本稿没有分析带t-dependent coefficients的六积分S2行。对\(\sum c_j(t)Z_j\)微分还产生\(\sum(\vartheta c_j)Z_j\)，所以S17的简单必要条件不再成立；不能把constant分类改写成polynomial-degree任意的no-go。没有宣称S22成功，也没有宣称任意mixed Smith rank的升高。

## 6. 范围和核验

本稿没有素数扫描、没有运行旧producer，也没有新numerical producer。S7是一般DVR线性lift身份；S12逐coefficient使用已有真实modp³源与genuine s；S18是对这个具体actual degree5源的完整prefix分类。Norm−109/16直接来自κ²=125/16。原complete rank与共同leaf由冻结前稿给出，不由这些modp²身份重证。

尚待实质闭合的是S22中实际mixed correction的构造、primitive saturation、degree/height、整格坐标与Smith独立性，以及和完整CDT成本相容的窗口。S19说明纯常系数六矩阵kernel correction本身没有第二层捷径，而不是排除这一统一框架或所有新算术输入。

root 实际只读独审 §§1–6通过，独推invariant Bockstein、S9积分性、S12两缺陷与p³tail阶数、S17/S18两向、Smith0/1和S22 mixed source坐标。low_period_closure 实际只读独审 §§2–4及§5共同p⁴坐标通过，逐项重推pm/nonp系数、genuine lift、c₀+pc₁ correction、completeprefix分类、unit triangle与旧baseline1；未运行producer，未在本次重证完整Hecke谱。审阅范围没有扩大为polynomial no-S2或metric净Smith收益。
