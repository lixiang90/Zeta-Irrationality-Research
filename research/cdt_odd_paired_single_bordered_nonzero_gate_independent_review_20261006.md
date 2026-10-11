# 原配对形式 single-bordered 门槛：独立全文核验

2026-10-06，NEW，quarter_actual_rank。旧471数学输入及所有旧/同行 producer 仅读，未执行/import/rerun。本稿记录真实阅读与纸面核验；本文不扩大 root 的无限非零或数值结论。

## V1. 实际阅读与当前 pins

实际完整阅读 root NEW `cdt_odd_paired_single_bordered_nonzero_gate_20261006.md` B1–B8/公式B1–B11：初读为数学正文与pending执行状态；第二次完整回读包括FIRST1 PASS142及primary准确归档说明，snapshot SHA f07051bb398fbf06c75d1299e688a506521e270b740263b740dc9915664b30c0。随后作者修 B4 的一个TeX反斜杠，数学不变；我再实际完整回读最终冻结正文，核实际 SHA a60d8116c88581028669d9a91aaaf1b848761fcfc4a37b089ca6e5b490b590f8。三次全文输出均无截断；最终数学通过。

另外 actual 完整重读冻结 auxiliary 原稿 A1–A13/公式A1–A32，SHA4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b；它给实际 paired constraints、negative evaluation、η=1/2 shared lift与全误差费用。不能将当轮旧PDF阅读算成本轮新读。

root NEW source 完整静态读，SHA84e3c06bb135ec57235880fa1490afe4a9c17e07fef62541219ce99e329e1cb3；NEW JSON实际完整读取所有字段，另实际全文syntax parse，SHA0273fdab538337a3a617aaed658db0e9a2e6559c91de65fc20448942a493b3ba，包括3actual cases、19条depth2记录及toy/depth3边界。其source只import stdlib、不读取旧/同行数据；exclusive-create first guard与failure保留路径明确。我没有执行或import它。

本独审没有实际新读 Caruso 或 Elsheikh–Giesbrecht 的PDF，因此只记录root正文报告的有限read scopes，不冒称peer已经读过。以下证明不使用其generic-density定理，也不依赖Smith/eigenvalue等价。

## V2. 实际 weak lifts 与完整 N

aux A18–A23 给 P_Q=AQ+(p/2)(A/I)I′Q+O(p²)，修正保留原 degree<6m、actual primitive paired kernel，并在shared nodes给 P_Q(a)/p=η A′Q、P_Q′(a)=A′Q，η=χ/2。不能换成裸AQ。Strong image维e=5m/2、weak kernel维q=3m/2，与rank4m格完全匹配；由actual reduction image/kernel基lift得到τ为p-unit，不需Gram非退化。

tail处弱value进一步为 p(η−1)A′Q。s5原leading harmonic给 p4U=−u、p5V=−6u，u=6b。故strong/strong为−6uD；strong/weak除p后是u(5−6η)DJ；weak/weak除p²为u(−6η²+10η−4)DJ⊗J。

令k=5−6η，则 −6η²+10η−4=(1−k²)/6=d。head p4、W非leading误差、a-source高一层、X-source p5共同给N∈Mat(Zp[X])及正文B4，其whole-X leading常数独立a、X。这准确继承aux A7的全部误差，没有在弱weak除p²后漏一层。

## V3. 无 G0 逆的 constrained determinant/corank 恒等式

L满rowrankt，Z基kerL，F右逆，U=[Z,F]为GL(V)。给Ψ作block-diag(U,Iq,It) congruence后，ambient坐标拆为(E,F)，并同步重排为(E,Q,F,T)。后2t块为[[B,It],[It,0]]，det=(−1)^t，inverse左上角0。因此顶层Schur仍是原Ncal，而非额外修正。这给

\[
\det\mathcal N=(-1)^t(\det U)^2\det\Psi,
\qquad\operatorname{corank}\mathcal N=\operatorname{corank}\Psi.
\]

同一个known-unit hyperbolic Schur证明corank，不需对未知Ncal或G0求逆。Congruence重排同时作用于行列，没有额外permutation sign。

只除 known-unit ambient−6D，Schur项为

\[
\frac16\begin{pmatrix}J^tDJ&J^tKL^t\\LKJ&LD^{-1}L^t\end{pmatrix}
=\frac16\begin{pmatrix}\kappa H_0&C_5^t\\C_5&\kappa^{-1}G_0\end{pmatrix}.
\]

cross的正号来自subtract负逆。d+k²/6=1/6准确，所以不残留未知G0项。同步重排为(T,Q)后，对M5左乘diag(κ⁻¹It,Iq)、右乘diag(It,κIq)得到这个矩阵；det因子κ^(q−t)=κ^m，corank保持。这一解释无需κ平方根。

ambientdet=(-6)^(3m)detD，Schur缩放6^(−2m)；m偶数消掉(−1)^(3m)，故总因子6^mκ^m。与上述congruence合成准确B8。所有外部因子为unit，故leading whole normalization的非零门槛只剩detM5；detG0是旧strong Schur方便性条件，不是whole leading的额外必要条件。

## V4. 原 determinant 缩放与实际 Smith 型

τ^2将原D_A换到actual局部基，p5缩放rank4m共p20m；Dp的det平方为p^(2q)=p3m。因而p17m D_A modp=τ⁻²u4m detNcal，正是B9，没有额外factorial、raw gcd或局部index。对于b为unit且候选rational X的denominator不被p整除，这个constant reduction若非零则Gauss与specialization估值都为−17m。

在M5 unit条件下，Nleading完整unit，strong block corank g=corankG0：nondegenerate ambient D把rad(D|E)与rad(D|E⊥)识别，E⊥由D⁻¹L^t给Gramκ⁻¹G0。先消掉e−g个strong unit方向后，剩g strong/q weak；Nleading的cross C满rowrankg，否则强rad向量仍是完整N的rad。

剩M被p整除，除p的modp矩阵[[A,C],[Ct,0]]，不论A为何，kernel为(0,kerC)，rank2g。因此Smith首e−g个0、随后2g个1、余q−g个至少2。已知vdetM=2q，迫使余项都等2。这给B10，适用于每个X∈Zp。不能继续在g>0时称旧0/2分布；root已准确纠正为0/1/2。

## V5. p³扰动阈值

原X项是24p5X times原value-Gram；两侧除Dp最多损失p²，所以N的affine X系数在p³Mat(Zp)。若N(c)可逆且νmax≤2，则p³N(c)⁻¹∈pMat(Zp)。因N在X中affine，写成N(c)[I+(X−c)N(c)⁻¹N_X]的第二因子在Zp[X]中模p恒I。归一化det的所有非constant coefficients被p整除，constant为unit；所有X∈Zp nonzero且估值固定。这是whole-X结论，不是只检查有限specializations。

νmax=3时diag(p³,1)加−p³(X−c)diag(1,0)在c+1精确奇异，阈值不能放宽。真实N(c)的νmax≤2仍未证明；其higher层可能含a-source。本文没有由finite-fieldM5 rank或density条件推出该higher-layer命题。

## V6. 静态证书核验与结论界线

完整source中r1,2,4 literal定义的center y=a+5r是正确reflection坐标：c/2=4r+1/2≡−5r(mod18r+1)。A′的factorial sign、Lucas W、LZ=0/LF=I、known unit complements、B6/B8因子与corank均对应纸面式。记录whole-normalized det6/10/18、M5det15/16/38、unitratio8/33/12；三项比例直接核对正确。它验证142checks，不是新auxprime无限搜索。

一般F19 toy G0=0与full form unit准确说明逻辑可能性，不能称真实λ2 family的退化例子。19个depth2整数扰动以及depth3反例只校验一般阈值，也不是actual higher-layer数据。第一且唯一成功执行归root；本独审旧/同行producer执行/import0，自有新数学producer额外执行0。

通过范围：actual-halfjet输入、B4完整归一化、B6/B8 determinant/corank、B9单一leading gate、B10退化强块Smith、B11合法扰动阈值。未完成：无穷M5 units、真实higher-layerνmax≤2、无限D_A非零、strict margin或任何新ζ/L/Catalan数值定理。单个auxprime的O(nlogn)不改变n²安全预算。

B4初稿TeX逗号后缺反斜杠已由作者在未冻结NEW稿中修复，最终a60d全文实读通过。数学无需修改。本文完整作者回读后冻结只读；root来源收据若随后仅增状态/审阅指纹，不冒称我已读尚未生成的元数据。本独审不替root登记未实际读到的最终receipt。
