# Actual residue CRT 整模型的独立全文审阅

2026-10-06，quarter_actual_rank。NEW 独审；旧及同行数学 MD/PY/JSON/manifests 全部只读，没有 execute/import/rerun。自有 cap-transfer 项目首次1 run 与本独审执行0分开登记。

## I1. 实际最终输入与读取范围

实际完整无截断读 root `cdt_odd_paired_residue_crt_integral_model_20261006.md`，全部sections1–6、R1–R21，当前 SHA3265da7c600ef8c1624f4208448ec35d75e32d71d92d78f4576b2cfdd5cfbd33。纸面数学逐项独核通过。

NEW source `cdt_odd_paired_residue_crt_integral_model_20261006_verify.py` 完整静态读，SHAaa4086403985b8b9eab6bec640e538a91f73a819f651a50adaae6bd000ad3f98；不运行。其 JSON SHA b88deee25e9ee0eef09c64fdd380f48b83062ffc28a2a4213b014ca14e1d640d。最初组合raw JSON输出截断，不能称完成；随后 JSON parser 只读并紧凑显示全部63 cases、全部actual Smith arrays、全部orbit records的residues/length/rows/Smith/baseline/mixed/credit，显示无截断并实际读完。没有手工重算所有9378 matrix identities。

本輪源输出计数63 cases、25 capacity cases、9378 identity checks与代码循环和JSON结构对应；root自有first-only成功1由作者历史登记，本审阅数学执行0。

## I2. 全 p 真 GL 与 step-Newton evaluation image

不同residue的全部root differences都是Z_p-units，monic resultants亦为unit。Sylvester inverse给Z_p[t] Bezout，故comaximal并成立CRT。左module rank M、右各rank L_r相加恰 M；monicdivision保留degree<M和degree<L_r。这是整free modules的isomorphism，基变换属于GL_M(Z_p)，无有理gauge或未知torsionfree假设。

local B_{r,j} monic且到local monomials unitriangular。CRT lift余式正确，在实际site r+lp的值精确为p^j j! binom(l,j)，其他residue值0；不是Taylor截断。各 E_r binomial matrix lowertriangular diag1，故R8确为准确image。Δ^j条件来自E_r^{-1}，不会把 integer-coefficient polynomial像偷换成任意integer-valued functions。

原falling与monomial两基unitriangular。R9的Δ^j/j!是global falling coefficient；CRT已保证R_{r,a}具有Z_p-coefficients，所以该表面分母的取消有先行整证明，不从有限U矩阵的det0估值反推。degree<M时前M连续values确定polynomial，恢复公式正确。

## I3. reflection block 与 ragged degree cutoff

head mirror k→M−1−k 在residue clusters上是实际bijection；offcenter L_r=L_s，lift index为L−1−l。这些实际pairs正好给L rows、2L columns，R11的primitive coefficients及负号匹配原pair map；orientation change只乘−1。

loop固定residue内reflection无fixed整数site，故L偶、row数L/2，R12正确。p=2不存在loop，p>M非空clusters长度1；均不遗漏。

CRT rows/columns按orbitpermutation后成为真正direct sum，不仅mod-p block diagonal。去掉column weights后的matrix是primitive pair map乘各 E_r；前者每pair至少一个unit且supports不交，后者GL，所以每block满射/full-row-rank。准确Smith multisets可以逐block取union，actual δ是其和。

R14准确保留每个j<L_r及precision e−j−v_p(j!)。p≤n时L_r≥2故modp²有全部x_r、y_r方向；p>n的length1 ragged clusters没有y_r，主稿没有免费补维。

## I4. Schur recursion 与 finite termination

选完整modp rank的unit pivot block后，integral row/column elimination得到I_r与S；余block modp为0，不需要猜测next jet权重。S/p使剩余非zero invariant valuations各减1，R16准确。

去column weights后的H满射，weights像包含p^{w_max}整domain，故blockimage包含p^{w_max}Z_p^{rows}。全部Smith exponent≤w_max，递归有限终止；没有拿第一层rank替代全部层。

## I5. R17 的全 p 奇偶计数实际等于 δ0

每minor至少付所选最便宜column weights。w_j=j+v_p(j!)严格递增。L=2u offcenter费用2W_u；L=2u+1费用2W_u+w_u；loop L=2u费用W_u。

设M=ap+b。odd p下，a=2u使b偶、loop在outer length2u侧。inner b/2 pairs与outer (p−b−1)/2 pairs加loop，准确sum为pW_u+(b/2)w_u。a=2u+1使b奇、loop在inner length2u+2侧；准确sum为pW_u+((p+b)/2)w_u。两式与n商余展开一致。

独核 v_p((lp+r)!)=l+v_p(l!)=w_l 对全部l成立，不只index<p²。因而上述sum恰Σ_{i<n}v_p(i!)，未漏高factorial层。p=2两lengthn clusters，最便宜n项是w_0,w_0,w_1,w_1,…，恰同first-n factorial费用；p>M所有weights0亦正确。

## I6. primitive mixed-carry高层容量和完整整数计数

在p²>8n，全部actual d-site factorial指标≤8n，Legendre给R18。Mixed orbit的真实primitive coefficients在一侧全unit、另一侧恰p；不是未约除row的虚假p信用。

L≤ceil(2n/p)<p，所以所有j!都是units。shifted weights为0,1,2,…和1,2,3,…。最便宜L项sum=floor(L²/4)，原两份0,1,2,…的sum=floor((L−1)²/4)，差floor(L/2)。全部block费用相加给R19，不要求任何Schur unit或exact Smith等式。

inner0..b−1和outerb..p−1各自reflection封闭。阈值τ将区间切分，mixed pairs准确计数max0min(τ,b−τ)、max0min(τ−b,p−τ)，fixed point不mixed。b=0、e=0边界均正确。R21与本审自证first-layer S8完全相容；当长度2,3,4，extra是M+M4。

因此 R19–R21可以作为另NEW cap-transfer稿的已证same-object输入。其费用须先与whole-X common-minor bound/entry cap匹配；更强整格下界并不自动产生相同面积的paid gain。

## I7. 完整静态 source 与有限证书范围

source未读取旧/同行producer或certificate，用实际d/g primitive rows独立构造original matrix；localW、global U来自R7/R9，有限检查U integrality及unit det，精确验证original·U=K。Orbit分解保留全部actual pairs和columns，比较独立original/orbit DVR invariant lists。

minimum-valuation pivot的row/column multipliers属于Z_p，清pivot row时已清bottom pivot column所以bottom-right不受影响；accumulated pivot valuations给完整DVR Smith。finite表含p2高层，正好检验R17中不可省的j!费用。已读全部cases/orbits，不重新计算矩阵。

代码没有证明CRT、全n公式、paid fee、无限非零或数值定理；这些界线在paper和JSON均准确。只读原JSON截断后补齐不算数学run；本审没有execute/import同行source。

## I8. primary实际页与结论边界

本轮实际完整抽读 Miller–Stanton author PDF1–4、15–16，共6页；归档总16页，不称全文。`literature/miller_stanton2017_orthogonal_polynomials_smith_author_20261006.pdf`，SHA0bf017cf67796bba8d5a00fc00e398ae6fb5b252e9e6f8c98a221e5913303a45，原[作者PDF](https://www-users.cse.umn.edu/~stant001/PAPERS/StantonMillerFinal.pdf)。本人数新下载0；pypdf报告少量xref pointing warnings，六页文本均完整显示，无读取失败或数学执行。

PDF15 Theorem7(a)的q=1、step a=p确给Vandermonde factorial factors，integer translation由unitriangular polynomial换基处理。PDF2–3的Theorem1及PDF15 Theorem8首先给定三项递推的monic OP和L(1)=1，并非本项目actual χ-corrected functional的无限normality。主稿正确定义其文献范围，不借一般OP定理填补未知auxiliary unit。

R1–R21纸面数学通过；全p真GL模型、全部ragged precision、baselineδ0、mixed高层容量、精确integercount均严核。没有宣称全窗口exact Smith、无限auxiliary simultaneous units、actual determinant无限非零、严格margin或新的ζ/L/Catalan定理。本NEWreview最终自读后交root固定；旧数学稿不修改。
