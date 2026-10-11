# 真实核的双曲单射、源响应亏秩界与极大核分支的 regularity

2026-10-07，NEW，/root/source_pencil_finalize。此前540冻结记录及最新审计7141ac2383dee7e1f2bf0828c993a17de4c0738b4f8a90dd6a627f9d97a43be3只读。本轮纯纸证：数学producer执行/import/rerun0，辅助单位素数扩表0。保留原B6/k3/s5、degree<3n、原饱和rank2n格S、fixed rational source ξ=αζ4+βζ5（β≠0）与whole-X D_A。本文没有新特殊值无理性或线性无关性结论。

本轮证明新的实际rank bound：令k=dim ker A5≤2r，真实源斜率G_K的corank至多min(k,2r−k)。特别在k=2r的分支，G_K必为unit，actual first source pencil自动regular。这不是将未知first form generic化；它来自原middle和两份实际moment之间的关系。

## I1. 已经实际完整读取的来源和尺度

本轮完整读取冻结[source S1–S14](cdt_odd_paired_source_radical_response_20261007.md)、[完整cubic/middle R1–R30](cdt_odd_paired_fixed_middle_racah_border_20261006.md)、[restricted-H H1–H27](cdt_odd_paired_restricted_H_normality_20261007.md)、[第四Racah M1–M24](cdt_odd_paired_masked_high_compression_20261007.md)及[reference completion J1–J14](cdt_odd_paired_reference_jet_completion_20261007.md)。后一稿实际完整读取包括J6文献范围；本轮本人PDF实读0，未借其generic论文来证明本family。

取n=4r、p=18r+1素数、F=F_p，避开fixed source分母及β素因子。physical模型有

\[
\mathcal K=\ker\mathcal A_5,\quad k=\dim\mathcal K\le2r,
\quad \Theta:\mathcal K\to F^r,
\quad \mathcal P(v)=F_*q_v\in F^r.
\tag{I1}
\]

冻结S12给v=(z,q)的完整重建，冻结S14给actual G_K：

\[
G_*\Theta(v)=C_*q_v,\quad H_*q_v=C_*^t\Theta(v),
\quad\mathcal E v=-(Jq_v+D_{phys}^{-1}L^t\Theta(v))/6,
\]
\[
\boxed{G_K(v,w)=\{\Theta(v)^t\mathcal P(w)
+\Theta(w)^t\mathcal P(v)\}/6.} \tag{I2}
\]

没有除未知G_*或H_*；q0且Θ0通过原Z满columnrank立即给v0。原first residual为A_act+8αG_K，A_act保留原β源及真实lift，已由前轮exact-lift-boundary与J14完成literal参考计算，本稿不删除它。

## I2. 物理 complete cross 与真实 middle 的关系

fold为u=y²、a=5r，令

\[
S_f(u)=\prod_{j=5r+1}^{9r}(u-j^2),\qquad
\mathscr J(f)=\tfrac12\sum_{y=-5r}^{5r}S_f(y^2)^{-1}f(y^2),
\]
\[
\mathscr J_{mid}(f)=\tfrac12\sum_{y=-(r-1)}^{r-1}
S_f(y^2)^{-1}f(y^2),\quad
C(T,q)=5\mathscr J(Tq)-\mathscr J_{mid}(Tq). \tag{I3}
\]

T degree<r，q degree<3r。physical F_* exactly就是complete J的r×3r matrix，原点半权重保留（S13）。physical C_*正是I3的actual C；physical H_*只和以下actual folded H差一个已知unit κ，故它们的kernel相同。若用其他T/Q基，仅作GL变换；本文可选T_i(u)=u^i来明确middle Vandermonde。

complete cubic为

\[
\mathscr D(f)=\tfrac12\sum_{y=-5r}^{5r}S_f(y^2)^3 f(y^2),
\quad D_{cub}=\mathscr D^{[3r]},\quad
H=D_{cub}+VE_HV^t. \tag{I4}
\]

R10–R16已证明D_cub unit：全部complete Racah norm/leading coefficients的factor指标≤15r<p。V_(i,b)=b^{2i}（0≤b<r），E_H的原点entry为S_f(0)^3/2，其余为S_f(b²)^3；全部unit。E_H是actual middle update，不把它删掉。

置K0=kerΘ。I2的两kernel equations给精确同构

\[
\boxed{K_0\simeq\ker H\cap\ker C,\quad v\mapsto q_v.} \tag{I5}
\]

反向：Hq=Cq=0使K5Jq/6属于kerL=imZ，唯一求出z，遂重建Θ0的v。这里ker H是完整3r空间内的kernel；它不同于restricted form H|ker C的kernel，后者允许Hq落在im C^t而不为0。

## I3. P 在 source-invisible K0 上单射

设ev_mid(q)=(q(b²))_(0≤b<r)。若q∈ker H且ev_mid(q)=0，则I4给D_cub q=0，已知D_cub unit给q0。因此ev_mid在ker H上单射；这是使用完整cubic unit，而非未证actual H正常性。

令V_mid=(b^(2i))_(0≤i,b<r)，并设

\[
E_J=\operatorname{diag}(f_b),\quad
f_0=S_f(0)^{-1}/2,\quad f_b=S_f(b^2)^{-1}\ (b>0).
\tag{I6}
\]

middle的distinct squares给V_mid unit，E_J也是已知unit。对v∈K0，Cq=0和I3准确给

\[
\boxed{5\mathcal P(v)=
V_{mid}E_J\operatorname{ev}_{mid}(q_v).} \tag{I7}
\]

因为P=J的低T矩，等式中没有误加factor2，也没有删除原点half。5为unit。若P(v)=0，I7给q_v middle values0；q_v∈ker H，故q_v0，再I2给v0。得到

\[
\boxed{\mathcal P|_{K0}\text{ 单射},\quad
\dim K0\le r.} \tag{I8}
\]

dim K0≤r本身已可由旧corank H≤r得到；本轮更强的新内容是complete cross map P在该实际子核上单射。它依赖C=5J−J_mid和D_cub unit的相容性，不是泛泛完整cross满rowrank。

## I4. 真实 joint map 的双曲单射和新的亏秩界

定义

\[
\mathcal M:\mathcal K\to F^r\oplus F^r,
\quad\mathcal M(v)=(\Theta(v),\mathcal P(v)),
\quad\Omega=\begin{pmatrix}0&I_r\\I_r&0\end{pmatrix}. \tag{I9}
\]

M(v)=0先给v∈K0，再I8给v0，故M满columnrank k。I2变成

\[
\boxed{G_K=\tfrac16\mathcal M^t\Omega\mathcal M.} \tag{I10}
\]

Ω是已知unit metric，ambient维数**2r**；这比以前的6r physical质量map单射更小。不能只凭M单射断言restricted metric unit；现在合法利用codimension：W=imM有dim k，Ω非退化给dim W^⊥=2r−k，rad(Ω|W)=W∩W^⊥，因此

\[
\boxed{\operatorname{corank}G_K\le\min(k,2r-k),
\quad\operatorname{rank}G_K\ge\max(0,2k-2r).} \tag{I11}
\]

以前S14只有rank G_K≤2rankΘ。现在两者可共同使用：若τ=rankΘ，

\[
\max(0,2k-2r)\le\operatorname{rank}G_K\le\min(k,2\tau).
\]

这是真实source斜率的全尺度算术rank bound，不更换source、free parameter、lattice或degree cutoff。k≤r时本界允许G_K完全退化；k>r时则强制至少2(k−r)个响应方向。对于一般k，尚未证明W∩W^⊥=0。

## I5. 极大leading核的actual regularity分支

**推论I12。** 若某实际辅助素数的leading核维数k=2r，则M方阵unit，因而G_K unit；精确det身份为

\[
\boxed{\det G_K=6^{-2r}(-1)^r(\det\mathcal M)^2\in F^\times.} \tag{I12}
\]

于是对actual完成后的任意A_act，det(A_act+8αG_K)是degree恰2r的非零多项式。该prime至多2r个α residue失败；其余residue给实际first Schur residual unit，原N的Smith型

\[
0^{6r},\quad1^{2r},
\]

以及

\[
\boxed{v_pD_A(X)=-32r,\qquad
p^{32r}D_A(X)\bmod p\in F^\times\quad(X\in\mathbf Z_p).} \tag{I13}
\]

这是在**已明确的k=2r分支**消除了原先另需G_K unit的门槛，不需要求A_act的det。未断言这个分支出现或无限出现；未新增任何unit-prime实例。whole-X常数来自旧X的normalized perturbation至少p³，first residual不受X影响；返回原S的变换det为unit。固定β的有限denominator另按旧接口避开。

若k<2r，I11只能把源斜率的未知radical维数限制到2r−k；完整actual affine pencil仍需前轮staircase或新的真实配对非退化证明，不能由partial rank自动宣称regular。每prime多数α成功也不证明某个fixed rational α无限成功。

## I6. source-invisible子form的第四Racah定位与degree门槛

为继续研究J9中H0=Aref|K0，第四M8提供一个具体候选空间。令m(u)=∏_(b<r)(u−b²)，L4(f)=D(mf)，其全部leading profiles由第四Racah已知unit。若q∈ker actual H，则对R=mW、degW<2r有

\[
0=H(q,mW)=D(qmW)=L_4(qW).
\]

所以在L4的完整正交basis R_n^L中，q degree<3r迫

\[
q\in\langle R_{2r}^{L},\ldots,R_{3r-1}^{L}\rangle. \tag{I14}
\]

这r维space不同于M2的m·third-Racah high directions。K0进一步由这里的actual H(q,u^i)=0和C(u^i,q)=0（i<r）确定，给2r×r明确stack。所有测试R都在原degree<3r；不能使用L4(q²)的known norm来直接判q0，因为它对应H(q,mq)，而任何非零q在I14中的degree至少2r，deg(mq)至少3r，超出原Q cutoff。这个精确degree门槛说明为什么complete第四norm本身还没有证明actual K0=0或Aref|K0 unit。

I8/I11已经绕开这个门槛取得source秩界；Aref|K0正常性仍待通过真实first jets或上述stack进一步研究。原first form的完整modp² carry仍必须保留。

## I7. 核查范围与剩余目标

本人新增数学producer执行0、失败0、rerun0，旧/同行execute/import0，辅助单位素数扩表0、Lean0。本文新的I7–I13由实际middle moment和正文有限维线性代数自证，不需要generic matrix perturbation或未核文献theorem。本轮新增文献下载0、PDF实读0。一次定位rg的glob组合匹配过宽且输出截断，只作定位，之后所列指定MD均完整读取；未把截断输出作为proof阅读证据。

新进展是P|K0单射、2r-dimensional actual joint hyperbolic embedding、严格codimension source-rank界，以及k=2r分支的actual source pencil regularity。没有证明一般actual Aref|K0 unit、一般actual first pencil regular、fixed source无限成功、whole determinant无限非零或同一对象strict解析–算术余量。单个p≈n的source响应不提供n²费用改善；safe费用上界也不当actual费用下界。

正文candidate待root实际完整独立review及作者最终自读，随后另存FINAL immutable来源receipt；此前540记录不改。
