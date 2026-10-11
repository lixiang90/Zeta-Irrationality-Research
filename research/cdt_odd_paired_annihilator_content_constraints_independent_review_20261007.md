# Actual annihilator 内容定理的正式独立纸面审阅

2026-10-07，NEW，审阅者 /root/scaled_root_finalize。实际审阅最终主稿 research/cdt_odd_paired_annihilator_content_constraints_20261007.md，SHA bf341f2e7f1205c92f41403f822621099dbc7079ac5fbe85afda71a8ae967beb，15827 bytes，A1–A24含A21a/all8节。先actual FULL读14798-byte旧候选，作者补入A21a后再actual FULL读最终15827-byte全文；正式final pin只取bf341f，不取未冻结e05c候选。结论PASS，没有正文修改请求。这里的PASS限纸面定理、对象及计费范围，不代表特殊值无理性或Lean验证。

## V1. 本轮实际读域与独立范围

审阅者本轮actual FULL读以下直接冻结输入：content Q1–Q22/all8节92a962、primitive-kernel K1–K18/all8节996e26、original lattice I1–I25/all10节5b7947、actual-local G1–G15/all正文2856a4、Hasse arithmetic J1–J18/all7节8676d1、relative-spectrum R1–R29/all9节41b309。主报告实际 §§176–180；audit完整JSONparse/header/current_progress/准确580计数与物理SHA，不称逐条人工全文读或逐一物理审计全部580。直接新稿最后一次全文输出完整，无截断；未继承作者或旧稿的程序/PDF阅读证据。

无producer创建、执行、import、rerun，无数学数值结果读取、prime实验或扩表，原始PDF/HTML新读0、下载0、Lean0。一项误写不存在lattice filename的只读请求返回missing path，随后用rg找到真实lattice并actual FULL读；这不是数学失败、producer启动或许可重跑。旧580冻结记录只读。以下恒等式和局部valuation逐式独立纸核。

## V2. Literal leading layer的系数、节点与β单位条件

A1与本轮FULL读local G3及jet J1逐项一致。5n<p≤6n给p>3n、p>5、p²>8n，原Newton i<3n的i!全为unit，原g monomial及ordinary derivatives均Z_p。全节点只能有unit head/tail、weight2单head、weight5单head；u=6n−p+1及T=p−2n>3n保留+1，不漏j0。

tail j=p+ρ只包含一个p harmonic倍数：pC≡5−3=2，p⁴U≡−6β。T中C·U给−12β，−24βH_j^(5)给−24β，故p⁵T≡−36β。αH^(3)、αH^(4)均多一个p，c项多五个p；tail derivative p⁵U消失。所有head U整，T≥−1，故p⁵缩放后head全消失。W_tail是unit，且βunit与p>5使−36βunit。A7–A8准确，不借旧normalized模型或把β非零误当所有prime βunit。

## V3. Evaluation满射与实际kernel reduction

A9–A10的u×u矩阵 Y_ρk=binom(2n+k+ρ,ρ)，去掉(-1)^(2n+k)列sign后由Vandermonde作 lower A、upper B，二者diagonal1，因此detY=1。u≤n使这些列均是原high列；这是source evaluation unit，不是actual B highblock unit。

由此E_u满射、E_u^t注入，diagonal Δ单位。A12中E_u^tΔE_u的radical准确为kerE_u：若该乘积杀x，injective E_u^t和invertible Δ迫E_ux=0，反向显然成立。即使Δ的quadratic form有isotropic向量也不改变这个operator核。由BK=0取modp后，全部cheap head rows与tail同余rows均为p倍数，A14成立。这里真正用了全部annihilator，不能以单个自配对零代替。

## V4. 内容共同lower与达到2ν的系数

A3系数为distinct node subsets的单项，24^ν ∏W_j det(R_K,J)²，原source变量独立。因此选r个cheap rows时det至少p^r，其余ν−r个节点至少weight2，逐单项共同lower2ν，没有项间相消。

另一方面lattice I7–I8确使S是ambient Newton格的direct summand，完整primitive K也是原Z^m的direct summand，组合SK仍primitive。前N=3n连续负节点矩阵binom(−j−1,i)是整数unimodular：leading coefficient1/i!与Vandermonde绝对值∏i!准确抵消。故任一p有一个unit νminor；它不可能使用cheap rows，因为那些rows全部被p整除。前3n余节点u≤j<3n满足j<p、2n+j<p、j>e，W valuation恰2。所选系数恰2ν，证明A5/A18 equality，不仅安全upper或lower。ν0用空minor，所有式子仍成立。

## V5. 原free high校准的精确边界

A19只用cheap rows modulo p最多u个不同残差。对选r个cheap rows，GL_r(Z_p) row operations把至少(r−u)^+行变p倍数，因而det有相应次幂，不能只记一层p。加其余节点weight2，所有νminors至少付2(ν−u)^+。

K_free取前ν个high列（0≤ν≤n），前ν个负点evaluation仍是A9截断unit；其中min(ν,u)个cheap、其余weight2，恰达到2(ν−u)^+。A20为同原格中自由primitive子格的准确值，但它不满足BK=0；非空时cheap evaluation unit与A14矛盾。作者明确将其限定为对比校准，没有把它当实际核或原问题反例。

## V6. Smith第一层、数值a_V lower及局部归一化

modp rank u使p⁵B的非零Smith entries恰u个valuation0、余d−u个≥1，并有ν个零entries。它不给完整Smith profile。A21从coefficient共同divisibility推出a_V specialization至少2ν，内容exact2ν并不给数值specialization upper。

最终新增A21a独立核对通过：a_V为原整数V在完整整数K上的strictly positive整数det。每个good prime均p^(2ν)|a_V，故Π_n^(2ν)|a_V，正实绝对值至少该乘积。固定例外为DM(Dβ)的prime divisors，PNT θ(6n)−θ(5n)=n+o(n)并去有限例外O(1)。乘2ν的误差uniform为o(n²)，因0≤ν≤2n。准确得到log a_V≥2(ν/n)n²−o(n²)；ν0为空det1。这里是实际离散det lower，与continuous a_P lower或relative a_V/a_P upper方向不同，作者没有混用。

A22 cheap rows先除p、noncheap weights先除p²，确使原kernel source Gram总除p²，det总除p^(2ν)。weight5变p³整，weight2变unit；A18保证normalized coefficient content unit，z全1数值却未必unit。局部归一化没有更换原P或免费传q/jet整性。

## V7. 全处费用、原模型限制与实际进展

固定sources/input bad primes均保留旧完整模型、(DM)^d。A5精确化的是前轮Q12内容扣2ν，A23同窗口q可保证的lower未改变；与旧rank lower取max、原curve A_q=32λ−1−13λ²/4及λ1.5费用635/16仍合法。这里没有把a_V lower除掉后沿用whole-jet40.3145，也没有宣布safe费用最优。

本轮实质新数学是原annihilator cheap-node排除、exact source coefficient content、准确free high校准及actual a_V全尺度lower。它关闭同source polynomial内“降低2ν内容扣费”这个具体方向，未排除更高p-adic coefficient lower、其他prime或phase/continuous几何。没有从p整除反推continuous P-normalized compression upper或免费Plücker高度信用。尚无strict margin或新ζ/L/Catalan无理性、LI、Lean。

## V8. 审阅闭合

上述最终bf341f完整主稿及全部必要直接冻结MD实际全文读取；对应physical SHA与bytes已检查。没有改作者稿、旧输入或580冻结文件。正式review完成后审阅者将actual FULL自读本review，再通知作者/root；作者收审后的最终全文回读和自身单向receipt由作者独立完成。不pin对方将来receipt或将来总audit。本review的PASS是实际纸面阅读后的结论，不冒称执行任何数学producer。
