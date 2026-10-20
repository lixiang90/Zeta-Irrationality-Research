# 第276轮独立有限处证书：按实际次数收紧完整有理头

2026-10-20。只写本文件。先核本子代理的实际 goal（返回 null）、初始 `git status --short`（干净），运行 `python scripts/research_state.py show`，读取 AGENTS、STATE、长期目标、[276任务](growing_pole_primitive_charter_round276_20261020.md)、[275完整行别证书](rational_kernel_review_round275.md)、[275结算](global_source_review_round275.md)、[269 G4–G7](global_source_review_round269.md)、270的[显式逆](growing_pole_euler_inverse_round270.md)、[算术](growing_pole_arithmetic_round270.md)与[实处](growing_pole_gram_bounds_round270.md)。没有运行 m、prime、参数或 Padé 扫描。其他代理后来生成的文件不在本稿写入范围。

**结论：同一原 Q 的新完整内容满足一个额外的全尺度整除，信用率为 2。** 它来自每行实际次数，不是275已领的 \(1+18\log2\)。令 \(r_i=N-i\)、\(D_i=2\,4^{r_i}d_{r_i}\)，并置

\[
h_i=16m-3-2i,\qquad E_i=D_i d_{h_i},\qquad
\Lambda_m^{\#}=\prod_{i<m}E_i^2.
\tag{C1}
\]

则全系数整数多项式及其内容满足

\[
F_m^{\#}=\Lambda_m^{\#}Q_m\in\mathbb Z[Z],\qquad
F_m^{\rm row}=L_m^{\#}F_m^{\#},\qquad
c_m^{\rm row}=L_m^{\#}c_m^{\#},
\tag{C2}
\]
\[
L_m^{\#}=\prod_{i<m}\left(\frac{d_{16m}}{d_{h_i}}\right)^2
\in\mathbb Z_{>0},\qquad
\frac{\log L_m^{\#}}{m^2}\longrightarrow2.
\tag{C3}
\]

只合并270旧实处证书时，完整本原 upper 是

\[
45+55\log2+32\mathfrak h(1/4)>0.
\tag{C4}
\]

随后独立核查本轮新实处证书，合并后的更紧完整 upper 为 \(46+46\log2+32\mathfrak h(1/4)>0\)，见§6。因此本证书没有给严格负净率，也没有给最优 \(\lambda_m\) 的足够 lower。它改善全对象安全预算，但不能自动延长276的一轮期限。

## 1. 固定对象、反证范围与本稿首命题

始终固定 \(X=\zeta(2)+2G\)、\(n=8m\)、\(N=8m-1\)、269 G5的唯一基

\[
p_i(z)=z^i+z^{4m}v_i(z),\quad 0\le i<m,
\]

以及实际正 Gram

\[
M_m=R_m+XI_m>0,\qquad Q_m(Z)=\det(R_m+ZI_m).
\]

\(Q_m\) 首一，\(\lambda_m\) 是其全部系数的最小共同分母。全部实际反证为 \(X=u/v\)、\(u\in\mathbb Z\)、\(v>0\)、\(\gcd(u,v)=1\)，此时 \(v^m\lambda_mQ_m(X)\) 为正整数。所需数值出口是在同一预定无界子列上

\[
\limsup m^{-2}\log|\lambda_mQ_m(X)|<0.
\tag{C5}
\]

本稿的首命题是：能否利用实际各行次数，把275的统一普通矩头费收紧为全部系数、全部素数幂均合法的较小清整？目标是C2–C3；不把某个主部、某个 minor 或一组有限 gcd 当完整内容。停止条件仍是276任务的一轮期限；若所得信用和真实实处未合成C5，本窗口到期结束。

## 2. 全部有理头的最大索引可从 \(2a\) 降到 \(2a-3\)

对任意整数 \(a\ge2\)、\(P\in\mathbb Z[T]\)、\(\deg P\le2a-2\)，原五周期分解中的**全部有理栏**都由

\[
B_a^{\#}=2^{2a}d_{2a-3}^{\,2}
\tag{C6}
\]

清整。这里仍是原积分与原 G2 的有理栏，未替换周期归一化。

先作完整带商分解

\[
\frac{P(T)}{(1+T)^a}=A(T)+\sum_{j=1}^{a}\frac{a_j}{(1+T)^j}.
\]

整系数首一除法给 \(A\in\mathbb Z[T]\)、\(a_j\in\mathbb Z\)、\(\deg A\le a-2\)。普通矩为

\[
\mu_k=\frac2{(k+1)^2}+\frac2{(2k+1)^2}.
\]

其中所有索引均不超过 \(2(a-2)+1=2a-3\)，故 \(d_{2a-3}^2\) 清全部多项式商部。

对 proper 部分，沿270 A4–A5重新核每一素数幂。令 \(s=j-1\)；\(j=1\) 时 \(U_1=0\)。对 \(j\ge2\)，原公式为

\[
U_j'(1)=-\frac1s\sum_{q=1}^{s-1}2^{-q}
                         \sum_{h=q+1}^{s}\frac1{h-1},
\tag{C7}
\]
\[
\frac{U_j'(1/2)}2
=-\sum_{q=1}^{s-1}2^{-q}\frac{A_{q,s}}q
                    \sum_{h=q+1}^{s}\frac1{2h-1},\qquad
A_{q,s}=\prod_{h=q+1}^{s}\frac{2h-1}{2h}.
\tag{C8}
\]

在C7中两个有理分母索引都不超过 \(s\)，而 \(q\le s-1\)。所以 \(2^{2a}d_{2a-3}^2\) 同时支付全部2幂与其余分母；因 \(s\le a-1\le2a-3\)，没有边缘索引遗漏。

对C8的任意奇素数幂 \(P_0=p^e\)，\(A_{q,s}/q\) 的分母计数来自 \(q,q+1,\ldots,s\) 中的0残基，分子计数来自 \(q+1,\ldots,s\) 中的 \((P_0+1)/2\) 残基。两者之差至多1。可直接比较同长度区间的两个残基；若区间首项 \(q\) 恰为后一残基，删去该首项前，该残基计数不小于0残基计数，删去后仍至多亏1。若 \(P_0>s\)，分母计数为0，不能产生亏损。因此

\[
v_p(A_{q,s}/q)\ge-e_p(s),\qquad
e_p(t)=\max\{e\ge0:p^e\le t\}.
\tag{C9}
\]

奇数调和和的全部分母索引至多 \(2s-1\le2a-3\)。故奇素数部分由 \(d_s d_{2s-1}\mid d_{2a-3}^2\) 清整，覆盖每个高次幂。2处单独按原精确计算：

\[
-v_2(2^{-q}A_{q,s}/q)
=s+v_2\!\left(\frac{s!}{(q-1)!}\right)<2s<2a.
\tag{C10}
\]

奇数调和和没有2处分母，所以 \(2^{2a}\) 支付这一处。C7–C10包含原有理栏的 \(2U_j'(1)+U_j'(1/2)/2\)，包括全部有限和头；不是只清 proper 的某个系数。这就证明C6。

## 3. 实际次数使逐行头费进一步下降

由原 G5 的 \(B_1\) 方程，最高 \(m\) 个系数恰为半个单位矩阵：

\[
[z^{N-j}]p_i=\frac12\delta_{ij},\quad0\le j<m.
\]

因此真实次数与首项为

\[
\deg v_i=4m-1-i,\qquad \operatorname{lc}(v_i)=1/2.
\tag{C11}
\]

这只是识别同一唯一基的实际次数，未作换基。275已由原 Hermite 数据证明 \(D_iv_i,D_ip_i\in\mathbb Z[z]\)，以下继续采用该已付来源分母。

在原实际积分中，完整恒等式仍是

\[
\frac{p_i(z)p_j(z)}{z^{8m}}
=z^{i+j-8m}+z^{i-4m}v_j(z)
 +z^{j-4m}v_i(z)+v_i(z)v_j(z),\quad z=1+T.
\tag{C12}
\]

令 \(E=\operatorname{diag}(E_i)\)。下面对三类项证明 \(E_iE_j\) 清除其全部有理栏。

* **高高项。** \(D_iD_jv_iv_j\) 为整系数多项式，实际次数至多 \(8m-2-i-j\)。平移到T坐标不新增分母，其普通矩最大索引为
  \[
  t_{ij}=16m-3-2i-2j.
  \]
  因 \(t_{ij}\le h_i,h_j\)，逐个素数幂有 \(d_{t_{ij}}^2\mid d_{h_i}d_{h_j}\)。因此 \(E_iE_j\) 清全部高高项，不让每一行都支付最大 \(d_{16m}^2\)。
* **低高项。** 写 \(a_i=4m-i\)，\(3m+1\le a_i\le4m\)。\(z^{-a_i}v_j(z)\) 先由 \(D_j\) 清来源，且 \(\deg v_j\le4m-1\le2a_i-2\)，所以C6适用。\(h_i,h_j\ge14m-1>8m-3\ge2a_i-3\)，故两行的头因子分别供一份 \(d_{2a_i-3}\)。此外
  \[
  v_2(D_i)\ge2r_i+1\ge2a_i,
  \]
  所需 \(2^{2a_i}\) 已包含在剩余的 \(D_i\) 中。因此 \(B_{a_i}^{\#}\mid D_i d_{h_i}d_{h_j}\)，整项由 \(E_iE_j\) 清整；交换i、j同理。
* **低低项。** 令 \(a=8m-i-j\)，此项为整系数来源的 \(z^{-a}\)，适用C6。\(2a-3=t_{ij}\le h_i,h_j\)，而
  \[
  (2r_i+1)+(2r_j+1)-2a=16m-2\ge0.
  \]
  所以 \(B_a^{\#}\mid D_iD_jd_{h_i}d_{h_j}=E_iE_j\)，包括完整有限头和2处。

这里没有逐项声称纯X。逐项只结算原形式分解的完整有理栏，最后仍由原 G6 消去其他周期。于是严格得到

\[
J_m^{\#}:=ER_mE\in M_m(\mathbb Z),\qquad
E^2\in M_m(\mathbb Z).
\tag{C13}
\]

它对全部 \(m\ge1\) 成立；本节所有整除均包含小素数和任意高次幂。

## 4. 全系数内容桥、全部赋值与预算

C13给完整整数多项式

\[
F_m^{\#}(Z)=\det(J_m^{\#}+ZE^2)
=\left(\prod_{i<m}E_i^2\right)Q_m(Z).
\tag{C14}
\]

对每个素数p，其安全费用及新增内容因子的完整赋值分别为

\[
v_p(\Lambda_m^{\#})
=30m^2\mathbf1_{p=2}
 +2\sum_{i<m}\{e_p(r_i)+e_p(h_i)\},
\tag{C15}
\]
\[
v_p(L_m^{\#})=2m e_p(16m)-2\sum_{i<m}e_p(h_i)\ge0.
\tag{C16}
\]

特别 \(p>16m\) 没有费用。C16非负来自每个 \(d_{h_i}\mid d_{16m}\)，不靠忽略高次幂或近似整除。C14与固定的 \(F_m^{\rm row}=\Lambda_m^{\rm row}Q_m\) 精确给C2–C3。取全系数内容，不能出现只在一个评价值或某一 minor 中成立的约分。

因Q首一，\(c_m^{\#}\mid\Lambda_m^{\#}\)，且同一个最小清整恰为

\[
\lambda_m=\frac{\Lambda_m^{\#}}{c_m^{\#}}
=\frac{\Lambda_m^{\rm row}}{c_m^{\rm row}},\qquad
\log|\lambda_mQ_m(X)|
=\log\Lambda_m^{\#}+\log\det M_m-\log c_m^{\#}.
\tag{C17}
\]

没有改变实际评价或最终整数 \(v^m\lambda_mQ_m(X)\)。275旧信用只用于定义已经固定的row规范，没有再扣一次。

使用与275相同的标准 \(\psi(t)=\log d_t=t+o(t)\)，因所有 \(r_i\in[7m,8m]\)、\(h_i\in[14m-1,16m-3]\)，误差在这些区间上一致为 \(o(m)\)。由

\[
\sum_{i<m}r_i=\frac{15m^2-m}{2},\qquad
\sum_{i<m}h_i=15m^2-2m
\]

得到

\[
\log\Lambda_m^{\#}=(45+30\log2+o(1))m^2,
\qquad \log L_m^{\#}=(2+o(1))m^2.
\tag{C18}
\]

原同一实际Gram的已付upper为

\[
\limsup m^{-2}\log\det M_m
\le25\log2+32\mathfrak h(1/4).
\]

结合C17、\(c_m^{\#}\ge1\)，证明C4。它将row完整upper再严格降低2，但仍是正的upper，不是实际增长率。

原实际Gram lower同时给新安全族的全序列lower

\[
\liminf m^{-2}\log(\Lambda_m^{\#}\det M_m)
\ge\kappa_{\#}:=45+16\log2-8\log(3+2\sqrt2)>0.
\tag{C19}
\]

这是 \(\kappa_{\rm row}-2\)，也只描述未经剩余内容约分的安全族。若在同一子列上C5的负余量至少为 \(\delta>0\)，则必要有

\[
\liminf m^{-2}\log c_m^{\#}\ge\kappa_{\#}+\delta.
\tag{C20}
\]

等价地，原row内容的必要门槛仍为 \(\kappa_{\rm row}+\delta\)；已付的率2不能改变该必要条件。若单用当前Gram upper给充分预算，剩余内容则须严格超过C4，或配合同一实际Gram的真实实处改善。C20不是充分条件。

还应明确当前upper本身的限制：\(c_m^{\#}\mid\Lambda_m^{\#}\)，所以即使假设全部安全费用都被内容除尽，用这个Gram upper仍只得到 \(25\log2+32\mathfrak h(1/4)>0\)。因此“继续付足内容”不能单独使**这一现有upper的计算**变成负数；实际裸Q的新的负upper仍是必需的实处证据。这不表示实际裸Q具有非负率，也不是最小λ或全部本原方法的no-go。

## 5. 短结算

新增的是C6、C13–C18的完整有理头及全系数内容证书，所有 \(p^e\) 已计入，完整安全净upper下降2。没有取得新的指定数值无理性定理、足够的最优λ lower，或完整负本原率。必要 \(\kappa\) 与充分upper信用没有混用，正upper也未当实际growth。

本稿依授权只提交这一文件，不修改 program、STATE、其他数学源、文献或形式化资产。单凭本稿成果，276一轮窗口仍应依既定停止条件到期结束；这个新完整预算改善可进入后续宏观机会成本比较，但不自动换名或续期。作者对C6–C20的推导不计作自身独立复核。

## 6. 对本轮新实处证书的独立审读及最终合并

本稿完成后，按根要求全文读取[本轮实际实处稿](growing_pole_real_rate_round276.md)，独立复核其R4–R12，而不继承作者的审阅标签。R5中 \((\binom{m-1}{i}+1)/2\le\binom{m-1}{i}\) 覆盖两个实际value栏；导数栏仍由原270的统一调和界支付。R6覆盖Newton恢复实际使用的每一个整数 \(1\le2t+1\le N\)。R7保留逐阶 \(2^r\)，再由实际 \(1\le z\le2\) 上的 \(2^rz^{M-r}\le2^M\) 得R8；没有换成辅助多项式。R9是原同一Gram的Hadamard。

独立代入Stirling并保留全部行有

\[
\log A_{m,i}=8m\log2+16m\mathfrak h(1/4)
 +\log\binom{m-1}{i}+O(\log m),
\]

误差对所有i一致。再由

\[
\sum_{i<m}\log\binom{m-1}{i}
=\tfrac12m^2+O(m\log m)
\]

得到该稿的新真实实处upper

\[
\limsup m^{-2}\log\det M_m
\le1+16\log2+32\mathfrak h(1/4).
\]

没有发现这条证明链的遗漏。将其与本稿全素数幂的C17–C18合并，最终可付的完整本原包络为

\[
\boxed{\limsup m^{-2}\log|\lambda_mQ_m(X)|
\le46+46\log2+32\mathfrak h(1/4)>0.}
\tag{C21}
\]

相对275下降 \(1+9\log2\)，分别来自本稿新增完整内容率2和新实处upper下降 \(9\log2-1\)，两项没有重复记账。C19–C20的必要lower门槛不受实处upper改进影响。C21仍不能排除或证明任何负二次子列，也不支付新的指定数值无理性结论；实际全序列非负liminf与严格负本原率均未付。

对同轮提出的二进有限差分分级机制，本稿只完成局部整除核查，未将其高高普通矩与全部有理头合成为新的完整共同内容，故没有在C18或C21中领取任何额外信用，也未把该局部结构用作自动续期证据。

## 7. 主结算与277章程的只读交叉审查

按根要求全文只读[276主结算](growing_pole_primitive_round276.md)与[277宏观章程](source_gate_charter_round277_20261020.md)，随后仅在本文件追加审读范围，没有修改两稿、账或其他源，没有新探索或执行诊断脚本。

重点逐式核276.1–276.5：完整新安全倍数与全系数内容关系吻合C14–C18；新增信用为率2，275旧L没有在row规范中再次扣除；新实处率与同对象清整合并确为 \(46+46\log2+32\mathfrak h(1/4)\)，对275的净upper下降恰为 \(1+9\log2\)。必要门槛 \(\kappa_{\#}+\delta\) 来自实际安全族lower，不能代替充分负upper；主稿已明确这一点。

全文的量词及资源结算没有越界：正的裸upper在 \(\lambda=1\) 下仍不闭合，仅说明保留当前绝对值/Hadamard包络的证书不足；主稿与277第2项均没有由此推出实际裸率非负、排除全部负子列或最优本原方法失败。原X窗口按一完成轮期限关闭，本轮预算改善使停滞计数为0；下一轮主动宏观比较因窗口到期，而非错误宣称两轮停滞。277没有重复领取本轮内容或实处信用，也没有自动重开旧来源。

对主稿§4，核其有限样本、signed尾域及有限部纠错的使用范围；未把只读主稿计作本人重建该脚本、JSON或独审稿的全文PASS。其有限部反例的常数项为 \(-1+6-1=4\)，与所示等式相容。没有发现主稿或277章程中应修正的错漏。本稿原创C6–C20仍不计作本人对自身证明的独立复核。
