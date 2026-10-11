# 第228轮新数值目标：√3 倍实二重对数的完整投影与秩一停止门槛

2026-10-08，B。只新建本轮记录；数学程序0。本稿没有证明新的数值无理性，也不把目录声明、微分秩或文献检索未命中当作证明。主目标仍值得保留，但下面完整支付的普通 Gram 模型不能通过严格 N² 预算。

## 1. 三个候选及实际已知范围

记 L=L(2,χ_{−3})，V=(3√3/4)L。最新下载的 [CDT 作者版](../literature/global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf) 为220页；本轮实际完整选读物理第3–5页。Theorem A 明确给出 1、π²、L 在 Q 上线性无关。第4页给 V 的理想四面体/Gieseking 体积身份，并称其定理没有直接解决所述体积的有理关系问题；同页对 canonical Mahler heights 也明确说明没有直接结论。[作者原文入口](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)。

| 候选 | 本轮能够核定的已有结论 | 新目标所需区别 |
|---|---|---|
| 主选 V=(3√3/4)L 无理 | CDT 的 Q-LI 给 L 无理 | 非有理代数倍 √3 不能免费加入 Q-LI；需要处理 Q(√3) 的两个实际嵌入 |
| 次选 L(2,χ_{−8}) 无理 | 此稿已支付下文的真实函数与全部系数分母；所读 growing-weight 文献摘要不给这个指定权2单值定理 | 它是新 character，不是 Catalan 的升权，也没有继承 Catalan 的投影/有限处 flags |
| 保留 m(1+x+y)=V/π 无理 | CDT 第4页给该身份，并与已证的非 canonical 修改目标区别 | 除以π不能由 V 或 L 的 Q-无理直接推出；本轮不展开第二套源 |

表中的“候选”只表示**本轮实际核定资料没有闭合相应命题**。CDT 原文并没有逐字单列“单个 V 无理仍未解”；不能从它讨论的更大体积问题，或从搜索未命中，冒称本稿证明了全球 novelty。

Q-LI 不足的形式例子很直接：1、π²、√3 在 Q 上线性无关，但 √3·√3=3∈Q。前一项由π²超越和√3无理取得；这个例子不是对真实 L 数值的断言。CDT 第3页的 matching-parity π 幂及实二次 weight1 对数属于经典 Lindemann 范围；当前 opposite-parity weight2 实二重对数不因 Baker 的线性对数定理而自动得到结论。旧研究的 ψ₁(n/6) 分类和近单位两对数乘积，则已经是 CDT A/C 的转移，不能再次列作新的主命题。

本轮当前官方 math 仓库 commit 为 fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb；Root 的 [状态收据](../literature/global_review_sources_round228_20261008/root_repository_state.json) 明确其 FF 更新过程。本人实际读当前 history 全文及 catalogue 005 完整内容：005仍发布 Catalan 无理的声明。这里不重新认证该稿/Lean，也不由未匹配到其它名称宣称全仓库或整个文献没有定理。

## 2. 主目标的完整实矩投影：不遗漏 off-diagonal

χ=χ_{−3}，χ(1)=1、χ(2)=−1、χ(0)=0。令

L=∫₀¹ (−log x)/(1+x+x²) dx>0，
h_m=Σ_{n=1}^m χ(n)/n²∈Q。

对每个 N≥1、0≤r,s<N，定义完整 N×N 矩阵

M_N(r,s)=∫₀¹ x^{3(r+s)}(−log x)/(1+x+x²) dx
         =L−h_{3(r+s)}。                                      (S1)

证明：核为 Σ_{n≥1}χ(n)x^{n−1}；积分后的绝对值级数收敛，允许交换积分。χ(n+3m)=χ(n)，所以移位完整尾项恰为 L−h_{3m}。因此真实 period-coefficient stack 是

M_N=L·11ᵀ−H_N，H_N(r,s)=h_{3(r+s)}∈Q。                    (S2)

这里所有行列都用同一源 x^{3r}，不是只计算对角线，也没有免费引入 π² 或忽略其系数。对任意非零实向量 q，

qᵀM_Nq=∫₀¹(Σ_r q_r x^{3r})²(−log x)/(1+x+x²)dx>0。

故 D_N=det M_N>0 对**每个** N 成立。所有尺度的非零性已付，不需要固定素数证书。

由于 (S2) 的 L 系数秩一，

det(X·11ᵀ−H_N)=P_N X−Q_N，P_N,Q_N∈Q，
K_N=1ᵀM_N^−1 1，
P_N=D_N K_N>0，Q_N/P_N=L−1/K_N。                          (S3)

这些等式来自 det(M+t11ᵀ)=D_N(1+tK_N)。它支付实际单目标的线性投影，而不是用函数源的形式秩替代数值关系。

## 3. 完整两嵌入、全部素数整模型

反证假设 V=g∈Q，置 c=4g/3=√3L∈Q；K₀=Q(√3)，O_{K₀}=Z[√3]。完整的形式矩阵/行列式是

A_N(C)=C·11ᵀ−√3H_N，
F_N(C)=det A_N(C)=(√3)^{N−1}(P_N C−√3Q_N)。              (S4)

第一嵌入在 C=c 的值为 √3M_N；第二嵌入的实际值为

A_N^−(c)=−√3M_N+2c11ᵀ。

第二处没有错误地“再次令 L=c/√3”，而是对完整代数系数作共轭。其 determinant 为

det A_N^−(c)=(−√3)^N D_N(1−2LK_N)。                       (S5)

常数多项式的评价给 K_N≥1/L，故此因子≤−1。两个嵌入都非零。

记 d_m=lcm(1,…,m)，固定正整数 c_g 清除 c 分母。由于所有 H_N 条目只涉及 n≤6N−6，

c_g d_{6N}² A_N(c)∈Mat_N(O_{K₀})，
(c_g d_{6N}²)^{2N} Norm_{K₀/Q} F_N(c)∈Z\{0}。           (S6)

这是一套完整安全模型，包含2、3及全部 prime powers；√3是代数整数，没有坐标缩放的漏账。由 log d_m=m+o(m)，其安全范数清分母的 N² 率为24。这不是 primitive 联合指标的最优下界，也不是 CDT 的 τ；本稿的 N 行 Gram 族尚未被声称是可直接输入 CDT 的固定实际独立函数族。

## 4. 内在评价范数与实际 N² 衰减

用 t=x³，实际测度变为

dμ(t)=(−log t)t^{−2/3}/[9(1+t^{1/3}+t^{2/3})]dt
      ≥(1−t)dt/27。                                       (S7)

K_N 是次数<N多项式在1的评价范数平方：sup |p(1)|²/∫|p|²dμ。下面的界可以自含纸付。置

R_j(t)=(-1)^j/[j!(1−t)] · ∂^j[t^j(1−t)^{j+1}]。

它次数j、首系数 B_j=binom(2j+1,j)、R_j(1)=j+1。j次分部积分的全部边界为零，所以它们对权重1−t正交，且

∫₀¹(1−t)R_j²dt
=B_j·j!(j+1)!/(2j+2)!
=1/[2(j+1)]。

在这个正交基上作有限维 Cauchy 不等式，得到准确的评价范数 Σ_{j<N}2(j+1)³=N²(N+1)²/2。因此

1/L≤K_N≤(27/2)N²(N+1)²。                                (S8)

用首一 shifted Chebyshev 多项式换基，j≥1的 sup 为2^{1−2j}；变基 determinant=1，Hadamard 给

D_N≤L^N 2^{−2(N−1)²}。

反向用 M_N≥J_N/27，J_N 是权重1−t的完整 Gram。首一 R_j/B_j 的平方范数为1/[2(j+1)B_j²]，且 B_j≤2^{2j+1}，故

D_N≥27^{−N}∏_{j<N}[2(j+1)B_j²]^{−1}
    ≥27^{−N}8^{−N}(N!)^{−1}16^{−N(N−1)/2}。

两侧给出确切的实际 rate

log D_N/N²→−log4，log P_N/N²→−log4。                    (S9)

它们不是两个半径下界的比较。由 (S5)、(S8)，实际目标范数的 rate 为

log|Norm F_N(c)|/N²→−2log4。                              (S10)

## 5. 完整 coefficient content 的严格停止门槛

令 a_N=(√3)^{N−1}P_N 为 F_N(C) 的非零 C 系数。精确身份为

Norm F_N(c)/Norm a_N
=c²−3(Q_N/P_N)²
=6L/K_N−3/K_N²。                                         (S11)

由 (S8) 得

2L/[9N²(N+1)²]≤6L/K_N−3/K_N²≤6L²。                    (S12)

现在允许任意 u_N∈K₀×，只要求**完整多项式** u_NF_N(C)∈O_{K₀}[C]，包括最优 scalar content 约分和代数单位重分配。其最高系数 u_Na_N 是非零代数整数，故 |Norm(u_Na_N)|≥1。因此

|Norm(u_NF_N(c))|≥2L/[9N²(N+1)²]，
liminf N^{−2}log|Norm(u_NF_N(c))|≥0。                     (S13)

同时 (S9) 强迫 liminf log|Norm u_N|/N²≥2log4。故“把安全24算低到严格小于2log4”与此完整多项式不相容：问题不是尚未挑中某个素数窗口，而是同一源必须一起整化的目标系数本身已经支付这一率。

Root 的 [一般秩一 Gram cap](global_rank_one_period_gram_cap_round228_20261008.md) 把此论证推广到任意包含1、degree至多多项式增长的有理多项式空间；本稿已独立 FULL 纸核其主链。不能凭改 rational basis 或换成普通 Catalan/χ_{−8} 周期移位矩而获得不存在的严格 N² 余量。

**停止的是这个完整 polynomial scalar-clearing 模型的严格 N² 入口。** 不包括仅在特定关系值的另付 cancellation、不同完整源、真正非秩一 period stack 或次主阶判据。尤其 (S11) 仍有多项式误差；若要在它上面工作，必须先证明 primitive 最高系数的次主阶高度控制。本轮没有给这一定理，不能扩大成此族永远不能证明无理。

## 6. 下一项具体对象与分支准入

同一主目标若采用新的 mixed projection，应先提供完整 coefficient stack：每个保留 moment/column 都有实际身份 R_j+√3L·S_j+Σ_νΠ_νT_{νj}；给整个列区间的显式投影，消掉全部非目标 Π_ν，不能只消一个 leading term。然后在 c=√3L∈Q 下形成 K₀ 中实际有理化的完整矩阵，并实际计算另一嵌入的矩阵、非零性和误差。**若主张严格 N² determinant 预算**，其非零 coefficient 范数与关系点范数之间须有已证的额外指数误差，(S11) 的 polynomial gap 不足；其它 Diophantine/能量判据必须另付各自的明确接口。

若新源确实取得 N² extra error，一项充分准入证书可以写成：在同一完整投影源上，存在无界尺度的 F_N(C)，其中 deg_C F_N=O(N)，以及非零 coefficient b_N 与完整 scalar clearing u_N，证明 u_NF_N(C)∈O_{K₀}[C]、F_N(c)≠0，且

limsup N^{−2}log|Norm(u_NF_N(c))|<0。                    (S14)

固定 c 分母 c_g 按 deg_C F_N 另付：c_g^{deg_C F_N}u_NF_N(c) 是代数整数，其范数清分母只增加 O(N) 对数费用，所以与 (S14) 矛盾。若 degree 超过此范围，应把该费用显式写入准入不等式。这是 N² 分支的充分证书，**不是所有下次研究的统一必要门槛**；次主阶 Diophantine 判据或 CDT 能量路线仍可另付。若改用 CDT fixed-rank functions/能量方法，则须另外支付实际函数独立、合法共同 meromorphic 图、完整 all-place array 及其**真正**的严格秩界；不能把 (S6) 的24或 Gram determinant rate直接称为 τ。当前尚无通过该接口的新对象；不为朴素 Gram 源继续安排 Smith/素数扫描。

次选 χ_{−8} 已有一个可以独立核的原生入口：

Σ_{n≥1}χ_{−8}(n)z^n=z(1+z²)/(1+z⁴)，
A′(z)=(1+z²)/(1+z⁴)，
A(z)=atan(√2z/(1−z²))/√2，
B′(z)=A(z)/z，B(1)=L(2,χ_{−8})。                          (S15)

角色在1、3、5、7模8的值为1、1、−1、−1；约掉1−z⁴即得首式。对 atan 直接微分给 A′，原点值0固定 branch。对应 A、B 的完整 Taylor 系数分别为 χ(n)/n、χ(n)/n²，d_N² 同时清除所有前缀分母；在0到1原生实段上可积分，没有从 Catalan 借来的 flags 或 free scaling。由于角色奇、权2偶，它不在 matching-parity 的经典π幂情形。

一个更具体且已完成准入检验的对象是 [χ−8对数矩完整接口](chi_minus8_logarithmic_moment_interface_round228_20261008.md)：J_{8j}=∫₀¹x^{8j−1}B(x)dx=L₈/(8j)−a_{8j}/(8j)²，a_m=Σ_{n≤m}χ_{−8}(n)/n。整个 N×N J_{8(r+s+1)} 的目标 coefficient是满秩 C=(1/8)Hilbert_N，A(1)项在所有列精确消去。短稿支付全矩非零、完整 d_{16N}³安全模型及 e^{−N/4}≤det M/det C≤2^N。更重要的是，对每个 p∈(8N,16N)，完整 determinant 的指定 coefficient valuation恰−q，q=2N−ceil(p/8)，强制完整scalar clearing的leading整数content至少 exp(4N²+o(N²))。**这个普通 integrated Gram 也立即停止，不能把次主阶高度假说继续排成229项目。**

因此229若选χ−8，应先交付真正改变此完整系数池的 mixed contact/whole-functional projection及其全部nuisance cancellation；若没有具体新对象，则不以它启动多轮Smith预算研究。V亦保持候选而非已准入路线。可以使用次主阶或真正CDT能量判据，但必须有新源的已付接口；不把(S14)设成普遍必要条件，也不以更换conductor继承Catalan结论。

实际 source/read scope 与文件身份见 [本轮 B 阅读记录](../literature/global_review_sources_round228_20261008/packet_reading_scope.md)。新证明为 (S1)–(S13)、(S15) 的纸面数学；(S14) 是明确待证准入命题，未声称已经满足。数学执行0；文献下载/提取、rg、文件读写/hash 不计数学执行。
