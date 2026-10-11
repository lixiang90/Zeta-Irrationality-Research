# 真实 high 压缩的第四 Racah、Christoffel 门槛与短 Whipple 矩

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。529既存冻结记录全部只读。本文纯纸面研究；新增数学程序执行0，旧或同行 producer execute/import/rerun 0，不扩辅助素数单位表。保留原固定 λ2、degree profiles、middle、halfjet 和第五幂种子，不把未证压缩正常性改写成无理性结论。

## 1. 实际目标与两次 mask 必须区分

本轮实际全文回读冻结 [restricted-H 稿 H1–H27](cdt_odd_paired_restricted_H_normality_20261007.md)。以下仍是 p=18r+1 素数、F=Fp、u=k²、a=5r，
\[
S(u)=\prod_{j=5r+1}^{9r}(u-j^2),\qquad
m(u)=\prod_{j=0}^{r-1}(u-j^2),\qquad
D(f)=\tfrac12\sum_{k=-5r}^{5r}S(k^2)^3f(k^2).
\tag{M1}
\]
实际 H=D+VEVt，原点 e0=S(0)³/2，真实 middle 保留。冻结 H18 的 high kernel basis 为
\[
q_j=m\widetilde P_{r+j},\quad0\le j<r,
\quad D_{\rm high}=[D(q_iq_j)]_{i,j<r}.
\tag{M2}
\]
P̃_n 是冻结 H8 的第三、masked-cross Racah 多项式。q_j 在 middle 消失，所以 M2 同时是实际 H 在这 r 个方向的压缩；这不是把整个 ker C 或原 H 的 middle 删除。

定义两个不同的新函数
\[
\mathcal L(f)=D(mf),\qquad \Phi(f)=D(m^2f)=\mathcal L(mf).
\tag{M3}
\]
本文证明 L 的完整正常性，Phi 是目标的实际权重。它们不相同；D_high=[Phi(P̃_(r+i)P̃_(r+j))]。

## 2. 单次 cubic mask 是第四个完整 Racah 族

剩余节点 k=r+x，0≤x≤4r，lambda=x(x+2r)=u−r²。冻结 H4/H5 的准确因子给
\[
\mathcal L(f)=\lambda_*\sum_{x=0}^{4r}w_x f(r^2+\lambda(x)),
\quad \lambda_*=-\frac{r(2r-1)!}{(4r)!^3(6r)!^3},
\]
\[
w_x=\frac{(-4r)_x^3(2r)_x(r+1)_x}
{(6r+1)_x^3(r)_x x!}.
\tag{M4}
\]
这是 KS Eq1.2.2 在
\[
(\alpha,\beta,\gamma,\delta)
=(-4r-1,-10r-1,-4r-1,6r),\quad g=2r
\tag{M5}
\]
的权重：三个上终止因子为−4r，三个下因子为6r+1，另外为 g 与 well-poised pair。定义
\[
R_n^{\mathcal L}(u)={}_4F_3
\left(\begin{matrix}-n,n-14r-1,-x,x+2r\\-4r,-4r,-4r\end{matrix};1\right),
\quad 0\le n\le4r,
\quad\kappa_n=\frac{(n-14r-1)_n}{(-4r)_n^3}.
\tag{M6}
\]
其 norm 为 L((R_n^L)²)=lambda_* h_n，准确
\[
h_0=\frac{(10r+1)_{4r}(2r+1)_{4r}}{(6r+1)_{4r}^2},
\qquad
\frac{h_n}{h_0}
=\frac{(n-14r-1)_n n!(-10r)_n^3}
{(-14r)_{2n}(-4r)_n^3}.
\tag{M7}
\]

**Theorem M8。** 对每个实际辅助素数，lambda_*、所有 n≤4r 的 h_n、κ_n 都是 F 单位。因此 L 的每个 leading profile d≤4r+1 都非退化。

证明：M7 所有非空负积的绝对值≤14r且不含0，正积最大指标14r，严格小于 p。n0空积单独处理。M6 最高项由冻结 H9 同一 Newton product 得出；三角正交 congruence 给
\[
\det\mathcal L^{[d]}=\prod_{n<d}\omega_n\in F^\times,
\quad p_n=R_n^{\mathcal L}/\kappa_n,
\quad \omega_n=\lambda_*h_n/\kappa_n^2.
\tag{M9}
\]
KS有限有理正交身份在全部终止范围内分母无零，先作有理特化后约化到 F；不含有限域 positivity。该第四族的正常性是真实新全尺度定理，未升级为 Phi 或 D_high 正常性。

## 3. Phi 的完整 leading Gram 精确压到 r 个 off-support evaluations

设 b_i=i²、0≤i<r，V_b=product_(i<j)(b_j−b_i) 为单位。Christoffel determinant identity 给对 0≤d≤3r+1，
\[
\boxed{\det\Phi^{[d]}=(-1)^{rd}
\left(\prod_{n<d}\omega_n\right)
\frac{\det[p_{d+j}(b_i)]_{i,j<r}}{V_b}.}
\tag{M10}
\]
所用最高 degree d+r−1≤4r，全部旧 norm/leading coefficient 已由 M8 证明单位。该有限 identity 是正交和 Vandermonde 的代数身份，Krattenthaler Theorem1 的有限窗口只用上述已知 polynomials；其 characteristic-zero 书面身份经已证单位分母约化到 F。也可从有限 Heine 展开直接证明，相关 d! 与 (d+r)! 均小于 p。没有假设 Phi 的任何 norm 非零。

特别完整 Phi 在 W-degree<2r 上正常，当且仅当
\[
\det[p_{2r+j}(i^2)]_{i,j<r}\ne0.
\tag{M11}
\]
这是 r×r 的具体 off-support gate。节点 x=i−r 为负，M6 的两个相应上参数为 r−i、r+i：各 evaluation 是完整已知4F3，不能据“在实支集外”在 F 中给它正号或非零。M11 控制完整2r Phi Gram，**并不直接控制**只有 r 个第三-Racah high 方向的 D_high；这第二个压缩步骤必须另算。

## 4. 目标 Phi 是 very-well-poised7F6 权重，普通 Racah 捷径失败

准确的节点权重为
\[
\Phi(f)=\phi_*\sum_{x=0}^{4r}t_x f(r^2+\lambda(x)),\quad
\phi_*=-\frac{r^2((2r-1)!)^2}{(4r)!^3(6r)!^3},
\]
\[
t_x=\frac{(-4r)_x^3(r+1)_x^2(2r)_x^2}
{(6r+1)_x^3(r)_x^2(x!)^2}.
\tag{M12}
\]
它是终止 very-well-poised7F6 的 summand，上参数
\[
(2r,r+1,-4r,-4r,-4r,r+1,2r),
\quad\text{下参数 }(r,6r+1,6r+1,6r+1,r,1).
\tag{M13}
\]

**Theorem M14（限定普通族的严格障碍）。** 对 r≥4，Phi 在全部实际 nodes0,…,4r 上的权重，不可能是同一 quadratic grid lambda=x(x+2r) 上一个常数倍的普通 KS Racah 权重，若后者终止以内的所有节点质量/相邻比均正常定义且非零。

证明：真实相邻比是
\[
\frac{t_{x+1}}{t_x}
=\frac{(x-4r)^3(x+r+1)^2(x+2r)^2}
{(x+6r+1)^3(x+r)^2(x+1)^2}.
\tag{M15}
\]
对 r≥2，上下各三个 linear factors 的常数在 F 中全不同，表示元可取14r+1,r+1,2r和6r+1,r,1，故其负数所给的根位置也全不同，约分后分子/分母次数均7。普通 Racah 相邻比至多5/5。假如在全部4r条真实边 x=0,…,4r−1 上相等，交叉相乘的多项式次数至多12，却有4r>12个不同零点，因而必须恒等。这和 reduced7/7不能等于5/5矛盾。原终止边 x=4r 不在检查内，未把终止0当分母异常。

M14只否定这个指定普通Racah shortcut；没有断言 r1/2/3 的所有有限拟合不可能，没有否定其他更高超几何公式、Christoffel 正常性或 actual M5。这也解释为什么必须区分 M4 的一次 mask 和 M12 的两次 mask。

## 5. 全部 Newton 矩的准确短 Whipple 变换

令
\[
F_l(u)=\prod_{i=0}^{l-1}(u-r^2-i(i+2r)),\quad0\le l\le4r.
\tag{M16}
\]
M13 的 general Whipple 变换应使用 Chu1998 Eq4.12 的完整参数。将乘 F_l 后的 summand 平移 x=l+j，very-well-poised 主参数 a_l=2r+2l；另外五参数为 (−4r+l) 三次、r+1+l、2r+l。准确得到
\[
\Phi(F_l)=\phi_*\sigma_l g_l T_l,
\tag{M17}
\]
\[
\sigma_l=(2r)_{2l}\frac{2r+2l}{2r}
\frac{(-4r)_l^3(r+1)_l(2r)_l}
{(6r+1)_l^3(r)_l l!},
\quad
g_l=\frac{(6r+l)!^3(14r-l)!}{(2r+2l)!(10r)!^3},
\]
\[
\boxed{T_l={}_4F_3
\left(\begin{matrix}-4r+l,-4r+l,-4r+l,-r\\
-14r+l,r+l,1+l\end{matrix};1\right).}
\tag{M18}
\]
最大求和指标≤min(r,4r−l)，故项数≤r+1；所有 sigma_l、g_l 因子都是单位，最大 factorial 指标14r。T_l 的下终止参数−14r+l 在本次实际求和范围内不触及0，另外两下参数也为单位。T4r=1 与只剩末节点的 F4r 求和相符，但其他 T_l 的值可以相消，本稿不声称其全为单位。

推导：(-x)_l(x+2r)_l=(-1)^lF_l，取消 factorial 后平移 x=l+j，准确产生 sigma_l（两个(−1)^l抵消）。Chu4.12 取 n=4r−l，b=c=−4r+l，d=r+1+l，e=2r+l。其 fourth upper parameter
\[
1+a_l-d-e=-r
\tag{M19}
\]
不可误写成 a_l。其 prefactor (1+a_l)_n(1+a_l−b−c)_n/[(1+a_l−b)_n(1+a_l−c)_n] 准确为 g_l。

本轮也实际阅读 Li–Long–Tu PDF18 Eq26及其后明确 c+d=1 的研究特殊化。应准确区别：印刷 Eq26 自称在双方终止时给一般公式，但把相应 fourth upper 印成 a；一般正确参数是1+a−c−d，只在该文后续 c+d=1 的特殊化才等于a。一个无程序的正常终止手核即可检出这处印式问题：取a=2、c=d=1、e=f=1/2、g=−1，左7F6=99/100，Gamma prefactor=24/25；印upper a的4F3=17/16给51/50，正确upper1的4F3=33/32给99/100。右下参数−2在upper−1终止以前没有pole。这个手核只是原件公式范围审计，不是本题actual辅助素数实验，也不否定其后满足c+d=1的特殊化结论。当前参数 d+e=3r+1+2l不为1，不能沿用该upper a印式；本稿从 Chu 完整公式直接导出 M19，未改动任何冻结原件或旧稿。

T_l 的上下参数和之差为1，是 balanced4F3；balanced本身不提供 norm 正常性或闭式单位。Chu4.13 的 Dougall 条件 1+2a_l+n=b+c+d+e 在这里差为13r−l>0，且模p也不为0（0≤l≤4r时9r≤13r−l≤13r<p）。因此不能把 M17 的7F6免费替换为 Dougall factorial product。

## 6. actual D_high 的完整矩表示和已知连接

在同一 shifted Newton basis F_l 中，第四 L 族和冻结第三 cross 族准确分别为
\[
R_n^{\mathcal L}=\sum_{l\le n}\binom nl
\frac{(n-14r-1)_l}{(-4r)_l^3}F_l,
\quad
\widetilde P_n=\sum_{l\le n}\binom nl
\frac{(n+6r+1)_l}{(-4r)_l(6r+1)_l^2}F_l.
\tag{M20}
\]
全部 n≤4r 的 diagonal coefficients 为已证 units。故用逐 degree 下降消元直接求三角 connection，所有分母只有 κ_n，不除任何 Phi 或 high 压缩 norm。

将每个产品 P̃_(r+i)P̃_(r+j) 在 F_l 中作唯一展开，记明确系数为 c_ij,l。其最高 degree ≤4r−2，准确
\[
\boxed{(D_{\rm high})_{ij}
=\phi_*\sum_{l=0}^{4r-2}c_{ij,l}\sigma_lg_lT_l.}
\tag{M21}
\]
这是原 high 压缩的 short balanced4F3 moment expression；所有矩都在同一个真实 Phi 中，不能把不同权重的 norms拼成这个 determinant。它把每个原4r+1-node和改成至多r+1项的4F3及 known-unit prefactors，没有新增数学执行或第五幂自由种子。

## 7. 完整 reciprocal metric 把压缩精确接回第五幂

令 N=4r+1、E_eval=[P̃_j((r+x)²)]_(x,j=0,…,4r)。因所有 third leading coefficients 及 distinct-square Vandermonde 单位，E_eval是单位。置
\[
v_x=S((r+x)^2)^{-1}m((r+x)^2),\quad
z_x=S((r+x)^2)^3m((r+x)^2)^2,
\]
\[
\mathcal J=E_{\rm eval}^t\operatorname{diag}(v_x)E_{\rm eval}
=\operatorname{diag}(\eta_j),
\quad \mathcal P=E_{\rm eval}^t\operatorname{diag}(z_x)E_{\rm eval}.
\tag{M22}
\]
全部完整 N×N metrics单位，理由是 complete node evaluation；它不宣称任何中间 principal compression单位。逐节点 v_x²/z_x=S((r+x)²)^−5。因此
\[
\boxed{\mathcal P^{-1}=\mathcal J^{-1}\mathcal G_5\mathcal J^{-1},
\quad \mathcal G_5=E_{\rm eval}^t
\operatorname{diag}(S((r+x)^2)^{-5})E_{\rm eval}.}
\tag{M23}
\]

令 I={r,…,2r−1}、Iᶜ={0,…,r−1,2r,…,4r}。D_high就是 P的I主块；Jacobi principal complementary-minor identity给
\[
\boxed{\det D_{\rm high}=
\det\mathcal P\left(\prod_{j\in I^c}\eta_j^{-2}\right)
\det(\mathcal G_5)_{I^c,I^c}.}
\tag{M24}
\]
prefactors全为单位。恒等式在 D_high奇异时同样成立，不除该 block；可由一般 invertible full matrix 的 Jacobi identity直接自证。因此目标压缩正常性也等价为一个具体3r+1维 outer第五幂 spectral-complement Gram的正常性。

M24不是原 M5 的第五幂左上r-block，也不允许扩大原globaldegree cutoff或免费变换原S；它只在当前有限处证明了准确 dual关系。新第四完整normality并没有自动绕过第五幂相消，完整P单位也不推出其I主块单位。

## 8. 当前实际进展与剩余问题

全尺度已证：一次 cubic mask 的第四Racah全部leading profiles单位；真实Phi完整leading Gram的r-node Christoffel determinant；r≥4普通Racah直接识别的严格障碍；所有Newton矩的合法短Whipple balanced4F3公式及完整known-unit connection；actual D_high与第五幂spectral补块的准确 determinant duality。

仍未证明 M11 的off-support determinant非零、M21/M24 的目标 determinant非零、H|kerC正常或actual固定第五幂M5无限单位。即使 M11 成立，D_high也需要额外压缩防相消；即使 D_high成立，H21剩余低块和middle还须另证。没有 actualhigherSmith替代、固定 rational source 无限成功、same-object strict margin、新ζ/L/Catalan无理性或LI、没有Lean。

下一有效问题是M11 off-support Racah determinant的确切因子，或M21 balanced4F3 moment的structured-minor正常性；M24还允许将相同缺口与真实第五幂 arithmetic种子联系起来。不能用第四族的完整正交或印刷Dougall条件跳过这些门槛。

## 9. 新文献、复用文献和实际读域

正常TLS新增publisher原件 Chu Wenchang, *Partial-fraction expansions and well-poised bilateral series*, Acta Sci.Math.(Szeged)64(1998),495–513，[原件](https://www.acta.hu/download.phtml?id=2471)，本地 [PDF](../literature/cdt_paired_masked_high_sources_20261007/chu1998_partial_fraction_well_poised_acta64_495_513.pdf)。19归档页，168085bytes，SHA256 `0a7e92173e94fab43ba04ee351cbc04eafeb0009948cc63404b3c20b8fe76dd5`；本轮实际完整文本PDF1,10–12，共4distinct页。Eq4.12的完整Whipple upper参数与Eq4.13的明确Dougallbalance实际已读，不称全文19页读完。

复用三份原件，无重复下载：KS报告PDF28–29，2页；Li–Long–Tu arXiv2103.08858v2 PDF1–5,18–19，7页（其中PDF18 Eq26只按其研究特殊化和Chu完整式核对）；Krattenthaler arXiv2101.04225v1 PDF1–4，4页（Theorem1的char0条件和formal/nonpositive范围已读，当前有限单位约化明确在M10）。本轮实际17distinct原件页，其中新增原件读4页、复用读13页。归档不等于全文阅读；没有关闭TLS检查，没有执行外部源码或数学 producer。

状态：完整候选纸证，待root与同行实际全文独审、作者最终回读后另作FINAL一向来源收据；本稿不预先声明已审通过。
