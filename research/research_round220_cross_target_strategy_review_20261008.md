# 第220轮跨目标策略稿：独立 FULL 审阅收据

2026-10-08。审阅者：round218_lambert_carrier。作者：round218_dual_audit。本收据只审下述已冻结最终身份，不修改被审稿、旧研究文件、main 或 manifest。

## 1. 最终身份与独立结论

实际 FULL 阅读 [cross_target_strategy_global_round220_20261008.md](cross_target_strategy_global_round220_20261008.md) 的全部8节，身份为18626 bytes，SHA-256：

`93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42`。

**PASS，限于该稿实际声称的范围。** 新的 Catalan ordinary-point suspension 确实将假设 G=g∈Q 变成一个 Q-Taylor germ，并在指定 ν=3/4 的同一圆盘图下全纯。四行秩、三种已经计费的分母表、literal n 的额外费用、统一 conformal-radius 必要上界及严格费用比较均通过独立纸面核对。没有发现必须修改冻结稿的数学问题。

这个 PASS 不包含新的 Catalan 无理性、其他普通值的 novelty、所有 cyclotomic 方法失败、最优共同 admissible 图或最优全源费用。作者保存稿 FULL 阅读和本审阅者的独立 FULL 审阅是两项不同事实。

## 2. 实际目标关系与指定同盘延拓

被审稿的 A=arctan x、B=Ti_2(x) 采用实际奇数交替 character χ_4(n)，故 B(1)=Σχ_4(n)/n²=G；级数在1绝对收敛，且初始分支可沿正实轴全纯延拓经过1。这保持的是实际 Catalan 目标，没有用任意普通点取代它。

独立按

\[
A'=1/(1+x^2),\quad B'=A/x,\quad
S_g'=\frac{B-g}{1-x},\quad S_g(0)=0
\]

核对系数：

\[
[x^N]S_g=\frac1N\left(\sum_{k=1}^{N-1}\frac{\chi_4(k)}{k^2}-g\right).
\tag{C1}
\]

因此 g∈Q 给实际 Q[[x]] germ；B(1)=g 则在初始1 leaf 去掉 S_g 导数的简单极点。此局部事实本身不足以断言任意全局图有效；被审稿补付的指定图确实完成了全盘核验。

设 a=3π/8，φ(z)=tan(az)。最近的极点为 z=±4/3；零点为8k/3，圆盘中只有0；1的前像为2/3+8k/3，圆盘中只有2/3。tan 不取±i，可用其指数表达式直接核对。上述性质在某个半径大于1的圆盘仍成立。

初始 germ 的 A(φ(z)) 导数恒为a，所以全盘为az。B 的拉回导数是

\[
\frac d{dz}B(\phi(z))
=az\frac{\phi'(z)}{\phi(z)}.
\tag{C2}
\]

唯一可能的分母零点在0，因φ(z)=az+O(z³)而可去。故实际 B 拉回全盘全纯。到 z=2/3 的实路径对应 x 从0到1，确实到达 B(1)=G 的初始 leaf。最后

\[
\frac d{dz}S_g(\phi(z))
=\frac{B(\phi(z))-g}{1-\phi(z)}\phi'(z).
\tag{C3}
\]

唯一可能的1点在2/3；φ'(2/3)=2a≠0，在 G=g 假设下分子同时为零，所以C3可去。其余各点没有奇点。由圆盘单连通性和0处初始常数，C3给出该 germ 的实际全盘全纯延拓，而不是另选一个同方程解。

被审稿明确保留了其他0/1前像的 branch 风险；没有把局部填点自动升级为全 universal covering 的共同 source 定理。这项限制正确而必要。

## 3. 四行实际秩与 holonomic 身份

独立核对实际绕 i 的单值变换：A 在i的对数系数为1/(2i)，逆时针一周给 ΔA=π。由 B'=A/x，得到 ΔB=πlog x+C，C 是所选路径的常数。

若 r_0+r_1A+r_2B=0，r_i∈C(x)，作用单值变换后有 πr_1+r_2(πlog x+C)=0。r_2非零会使log x成为有理函数，矛盾；因此r_2=r_1=r_0=0。这是实际函数独立性，不依赖未证明的数值独立性。

若 S_g=r_0+r_1A+r_2B，微分后比较这三个已独立函数的 B 系数，强迫 r_2'=1/(1-x)。有理函数导数在任何点的简单极点残数为零，而右端在1的残数为−1，矛盾。故1,A,B,S_g对C(x)线性独立，对Q(x)也独立。

四行满足被审稿S6的完整有理微分系统；包括常数1后，这是真正齐次的 rank4 系统，g∈Q时矩阵在Q(x)上。分量消元给有理系数标量微分方程，因此四个实际 germs 的 a priori holonomic 性已经付清。这里不要求先有 Betti/Hodge 实现。

## 4. 三种分母类型与 literal n 费用

取固定c_g使c_gg∈Z，对最后一行使用c_gS_g。C1逐项证明其分母可用n d_n²清除。按(1,A,B,c_gS_g)排序，第一张表的两列是(0,1,1,1)^t、(0,0,1,1)^t，各列宽度1；所以σ=(0,1,2,2)，e=(0,0,0,1)，flat费用为27/16。

本审阅者重新读取固定 CDT v2 的 Definition6.0.1、Theorem6.0.2 费用定义及 Example6.0.20。单个e_i=1的m=4费用只依赖Σe_i=max e_i=1，因此不因其出现在第三行还是第四行而变；Example给τ_sharp=7/16、minimizers含[2,3]。于是该表总费用17/8，确认没有漏掉literal n。

第二张安全表也通过独立逐prime-power检查。对p≤N设h=floor(log_p N)。若N≥2p^h，d_floor(N/2)含p^h，三个layers有3h足以清除Nk²。若N<2p^h，则d_floor(N/2)至少含p^(h−1)；N及k<N不能同时为p^h的正倍数，故v_p(N)+2v_p(k)≤3h−1。g/N项的分母也被包住。p>N没有费用，N=1直接由c_gg∈Z处理。证明包括p=2，不依赖character删去偶数项。因multiplier随N整除后续multiplier，亦可清除完整系数jet。

所以d_N²d_floor(N/2)的表是合法的；其三列宽度为1、1、1/2，σ=(0,1,2,5/2)，e=0，flat费用确为61/32。

第三张literal表σ=(0,0,0,2)、e=(0,1,2,1)也是逐项合法类型。独立代入Definition6.0.1：

\[
\tau_\sharp=\frac14\min_{0\le\xi\le4}
\{2\xi+I_\xi^4(\xi)\}.
\tag{C4}
\]

若0≤ξ≤1，中间harmonic integral在[2,3)、[3,4)的被积函数分别至少为1、3/2，故I≥5/2。若1≤ξ≤2，该integral至少为从ξ+1到4的长度3−ξ，故2ξ+I≥ξ+3≥4。若ξ≥2，则2ξ≥4，其余项非负。因此τ_sharp≥5/8，连同flat7/8得到总τ≥3/2。这是充分lower bound，没有冒充完整minimum。

以上表是已经证明的全系数CDT类型；不是声称它们等于真正最优全源费用。被审稿正是按这一范围下结论。literal n对单系数只有多项式增长，仍须按定理的全源费用计入；此区分正确。

## 5. 统一容量上界及严格比较

任何共同admissible图都必须避开±i：若φ(z_0)=i且局部阶k≥1，则 A(φ) 的导数有非零残数k/(2i)，故A拉回有不可meromorphic的对数。同理处理−i。有限分歧不能消除这个必要条件。

冻结Legendre坐标给standard λ 的已付归一化

\[
\partial_\tau\lambda(\tau)=\pi i\lambda(1-\lambda)F(\lambda)^2.
\]

这是standard τ，而不是λ(2τ)的导数；被审稿没有丢factor2。令t(z)=i(1+z)/(1-z)，则t'(0)=2i，λ(i)=1/2。实际cover

\[
\Psi(z)=i(2\lambda(t(z))-1)
\]

满足Ψ(0)=0、|Ψ'(0)|=πF(1/2)²。Γ(2)的已付Hauptmodul描述使λ:H→C\{0,1}为universal covering；所以上述Ψ是C\{±i}的universal cover。任一避开±i的圆盘图可提升到此cover，提升在0可归一为0；Schwarz lemma遂给|φ'(0)|≤ρ=πF(1/2)²。

**这只给所有实际共同图的必要导数上界。** 它没有证明Ψ自身对B、S_g的所有其他0/1前像都适配；被审稿没有作这一不合法推断。实际已付共同图仍是§2的ν=3/4 tan图。

纸面严格数值比较也通过。c_n递减，c_1=1/4、c_2=9/64、c_3=25/256，所以

\[
F(1/2)\le1+1/8+9/256+(25/256)(1/4)=1213/1024.
\]

用π<22/7得到ρ<32370118/7340032。若需完全初等核π界，可由正积分∫_0^1 x^4(1-x)^4/(1+x²)dx=22/7−π获得。纸面交叉相乘显示

\[
32370118/7340032<5711/1280,
\]

两个交叉乘积的正差为485171712。指数级数从j=0到5之和恰为5711/1280，余项严格正，因此ρ<e^(3/2)。三个已计费的τ依次17/8、61/32、至少3/2，均严格大于logρ。故即便已知holonomic，也不能满足普通single-map Theorem7.0.1的正分母条件。

这里没有比较未支付的energy quotient，没有把27/16单独充作第一表总成本，没有从这一必要条件失败升级为所有新source/trace/坐标或所有CDT变体的no-go。即便未来降低费用产生正分母，strict quotient<4仍是独立义务。被审稿对此范围的表述准确。

## 6. 策略与 primary 引用范围核对

被审稿S2–S3的Legendre比较与冻结实际reciprocity一致：假设G有理只消去规范化的一次log系数，强迫log²仍存在。其对低权33/4、高权480·7!d_N^7及旧Jacobi预算的对象限制也没有发生拼接。本审阅者对旧数值标签作了定位核对：global216实际L_arith=−27323/4和U_mix区间、round218实际条件性−7799.5与b0的−2675.5/5124差距，均与引用本地正文一致；高权safe系数包的480·7!也与冻结稿一致。本次没有重新FULL审全部旧Jacobi证明。

对五项primary的引用，另实际选读核对如下：

- CDT固定218页v2：本轮重新读取Definition6.0.1、Theorem6.0.2费用及输入、Example6.0.20、Theorem7.0.1及其holonomic放宽条件。源是本地固定PDF，未混用220页作者快照的页码。[固定主文](https://arxiv.org/pdf/2408.15403v2)
- Brown Annals：实际web选读Theorem1.1/Corollary1.2及§2.2 Definition2.1/Remark2.2。它给motivic basis及数值spanning，而不自动给数值独立性；被审稿限制正确。[原文](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf)
- Deligne–Goncharov：核91页作者稿§5.1–5.2的cyclotomic paths与canonical de Rham path描述。它不替本构造支付数值分裂。[作者稿](https://www.math.ias.edu/files/deligne/Tate.pdf)
- Brown–Hain：核intro Theorem1.2/比较同构与Proposition2.2的Bol身份，其对象是level1。被审稿没有免证Γ_0(4)接口。[作者稿](https://arxiv.org/pdf/1708.00652)
- MMV49页作者稿：核§7.3 Lemma7.1及(7.3)，确有odd-zeta coboundary，除Tate scale后cohomology class有理；实际cocycle不因此有理。[作者稿](https://www.ihes.fr/~brown/MMVarchiveV1.pdf)

本审阅者不把作者自报的各次阅读行为再认证成自己的FULL文献阅读，也不把所读选目提升为whole-paper review。上述逐项引用没有越过所述数学用途。§7的Ti_2(1/2)等储备明确没有novelty或无理性结论；非主real Dirichlet入口的B_0在1可去，可由周期character和为0直接核对。odd Li_s在1仍有log branch，不能只减去目标值就直接复用Catalan补点，这项限制也正确。

## 7. 保存审阅范围与实际执行账本

被审稿最终8节FULL阅读及其18626-byte/SHA身份由本审阅者实际完成；正文、所有新公式S4–S15、三张表与策略范围均已核对。所列8份旧输入的bytes/SHA重新查验，与被审稿表格相符；未冒称本次FULL重审它们。冻结低权连接与整格的本轮FULL输入核验是另一个委托中已完成的事实。

数学程序、CAS、矩阵执行、数值积分、prime/parameter grids、PSLQ、Lean、Git与旧producer执行均为零。上面的branch、rank、逐prime-power、费用lower bound与rational严格比较全是独立纸面推导。工具仅作冻结Markdown FULL读取与hash、旧数值文字定位、PDF指定页段文本提取、primary web选目浏览、本NEW收据保存与复读。无新HTML/PDF下载。

未改被审稿、旧文件、main或manifest。本收据的作者实际FULL保存稿复读与最终hash另在handoff报告；这不冒充第三位审阅者对本收据的独审。
