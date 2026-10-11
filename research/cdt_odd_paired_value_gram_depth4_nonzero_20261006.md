# 真实取值 Gram 的 p⁵ 精度与四层非零性门槛

2026-10-06，root，NEW。保留原 B6/k3/s5、degree<3n、原饱和整数值配对格 S 及 whole-X 行列式。487 项既存数学文件、所有旧或同行数学 producer 及其结果保持只读；本文不运行或 import 它们。这里推进的是同一对象的条件非零性判据，尚未证明新的特殊值无理性定理。

## V1. 实际对象与本轮改进

令 M=⊕_{i<3n} Z binom(t−1,i)，U=A_{n,Z}⊗Z_p 为原 rank2n 配对直和因子，D_A(X) 为原完整整数基 S 上的双线性型行列式。取 p>5、p²>8n、p≤6n；固定有理 sources 先用同一固定分母清整，费用仍是 O(n)，不要求 a、b 是 p-units。原 form 中 X 的系数准确为

\[
\partial_X B_X(P,Q)=24\sum_{j=0}^{6n}W_jP(-j)Q(-j),\qquad
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3.
\tag{V1}
\]

令 k 为真实 unit-tail map (P(−j),pP′(−j)) 的模 p 核维数。把其核基在原 S 坐标 lift 成 exact characteristic-zero 配对多项式，并补成 U 的 Z_p 基；最后 k 列称 weak。已有真实整模型接口给

\[
p^5B_X=D_pN(X)D_p,
\qquad D_p=\operatorname{diag}(1^{2n-k},p^k),
\qquad N(X)\in\operatorname{Mat}_{2n}(Z_p[X]).
\tag{V2}
\]

本轮证明更强的实际精度，而不是只按两次除 p 估算损失：

\[
\boxed{N(X)-N(c)\in24p^5(X-c)\operatorname{Mat}_{2n}(Z_p),\qquad c\in Z_p.}
\tag{V3}
\]

因此最大 Smith 指数 ≤4 的 anchor 已足以保证 whole-X 非零。冻结 single-bordered B11 的 p³/指数≤2 仍是正确的保守结论；本文增强它，不改旧稿。

## V2. 所有 unit-W 节点上的真实弱取值

写 2n=ap+r_2、3n=Qp+R、6n=hp+r_6，余数均在 [0,p)。此处允许 a=0、Q=0。由于全部 factorial endpoints≤8n<p²，Legendre 公式逐 j=ρ+lp 给

\[
v_p(W_j)=2\mathbf1_{\rho>r_6}+3\mathbf1_{\rho\ge V},\qquad V=p-r_2.
\tag{V4}
\]

故 unit residues 恰为 0≤ρ<u，u=min(r_6+1,V)，包含 ρ=0 和余数端点；其余 weights valuation 至少2。

真正整数值 ψ(t)=(t^p−t)/p 的 GL 基为 binom(t,i_0)binom(ψ(t),i_1)，i_0+pi_1<3n。其 Newton 变换最高系数比 i!/(i_0!i_1!p^{i_1}) 是 unit，其余系数由整数值有限差分在 Z_p 内；再用 t→t−1 的整 unitriangular 变换，准确回到原 M。每个 residue 上的 reduction 是 degree≤Q 的 local polynomial Φ_r(Y)，Y=ψ(t)；底 Q 层自由而最高层保留 degree<R 的全局约束，绝不添加自由 top layer。此处仅使用 degree 上界，不需要 ambient coefficient map 的满射。

对每个 unit ρ，全部 unit-tail sites 是 j=ρ+lp，1≤l≤h。p²>8n 保证 h<p；它们的 ψ(−j) mod p 两两不同。又 h=floor(6n/p)≥2Q；若 Q≥1，2Q≥Q+1，若 Q=0，则 p≤6n 保证 h≥1=Q+1。因此 weak P 的尾部取值为零迫使

\[
\Phi_{-\rho}(Y)\equiv0.
\tag{V5}
\]

这同时给出 scaled derivative 为零，并给出同 residue 的 j<p 头部取值也为零。结论是对原 S 的 exact 配对 weak lift：

\[
\boxed{P(-j)\in pZ_p\quad\text{对全部 }0\le j\le6n\text{ 且 }v_p(W_j)=0.}
\tag{V6}
\]

没有把单个零取值当成多项式恒零；使用的是 h≥Q+1 个互异实际节点。没有只证明尾部而遗漏头部，也没有改用普通 coefficient 格。

## V3. 节点逐项整除，保留精度 p⁵

令 P_i 为上述 actual adapted basis，δ_i=0/1 分别对应 strong/weak。在 unit-W 节点，V6 使 W_jP_i(−j)P_l(−j) 被 p^{δ_i+δ_l} 整除。在 nonunit-W 节点，weight 至少被 p² 整除，而 δ_i+δ_l≤2，所有取值均整。因此逐节点有

\[
H_{il}=\sum_{j=0}^{6n}
\frac{W_jP_i(-j)P_l(-j)}{p^{\delta_i+\delta_l}}\in Z_p.
\tag{V7}
\]

这是真实 normalized value-Gram，而非假设未归一化值 Gram 的 weak blocks 都是任意整数。将 V1 两侧除 D_p 后，准确得到

\[
\partial_X N=24p^5H,
\tag{V8}
\]

证明 V3。这里不除未知强块、restricted Gram 或 M5；不要求任何 leading gate 非零。V2 的 p⁵B 整性和 V7 的 value-Gram 整性是不同的两步，不能相互替代。

## V4. 指数≤4 的 whole-X 条件判据

固定 c∈Z_p，假设 N(c) 在 Q_p 上可逆，Smith 指数为 0≤ν_1≤⋯≤ν_d，d=2n。若 ν_d≤4，则 p⁵N(c)^{-1}∈p Mat_d(Z_p)。由 V8，

\[
N(X)=N(c)\{I+24p^5(X-c)N(c)^{-1}H\},
\]
\[
\boxed{\det N(X)/\det N(c)\in1+p(X-c)Z_p[X].}
\tag{V9}
\]

所以每个 X∈Z_p 都非零且 valuation 相同，整个多项式除以 p^{t}、t=v_p detN(c)，其模 p 为非零常数。设 adapted basis 相对原 S 的行列式为 τ∈Z_p^×，由 V2 有

\[
\boxed{p^{5d-2k-t}D_A(X)\bmod p\text{ 为非零常数。}}
\tag{V10}
\]

指数可为负；这是一处 signed rational 归一化，不声称最小整数分母。对于 fixed rational target，须避开其固定分母及 sources 的有限例外素数。要取得无限非零子列，仍需证明无限 n 有适用的 prime 与 ν_d≤4；本文没有证明这一步。

阈值4对于只知道 p⁵ 扰动的一般矩阵类严格：N(c)=diag(p⁵,1)，H=−diag(1,0)/24 给 N(c+1) 奇异，而 N_X∈24p⁵Mat。这个 toy 只说明不能由 V3 单独免费允许 ν_d=5，并不是本题原 M5 或实际 higher layers 的反例。

## V5. 无未知逆的四层 obstruction ladder

以下仅处理 integral symmetric anchor N(c)，并只除实际已识别的 unit blocks。令 N^{(0)}=N(c)、k_0=d。在 stage j=0,…,4，取其 mod p rank r_j。因为 p≠2，有限域对称形式可分解成一个非退化 r_j 子空间及其 radical；lift 成 Z_p-GL 后写

\[
N^{(j)}\sim
\begin{pmatrix}A_j&B_j\\ B_j^t&C_j\end{pmatrix},
\qquad A_j\in GL_{r_j}(Z_p).
\tag{V11}
\]

仅用已知 unit A_j 求逆，整 congruence 消掉 B_j。Schur residual mod p 为零，因此

\[
N^{(j+1)}=(C_j-B_j^tA_j^{-1}B_j)/p\in\operatorname{Mat}_{k_{j+1}}(Z_p),
\qquad k_{j+1}=k_j-r_j.
\tag{V12}
\]

当 k_j=0 时以后为空。逐步整 Smith 关系给出：r_j 正是原 anchor 的指数 j 的重数；剩余 N^{(j+1)} 的指数需加 j+1。故

\[
\boxed{k_5=0\ \Longleftrightarrow\ N(c)\text{可逆且}\nu_{\max}\le4.}
\tag{V13}
\]
\[
\boxed{t=\sum_{j=0}^4j r_j=\sum_{j=1}^4 k_j\quad(k_5=0).}
\tag{V14}
\]

这些 ranks 与已知 unit 块的选择无关，因为它们就是 Smith 指数重数；可从 N(c) mod p⁵ 决定，stage j 保留 p^{5−j} 精度。条件不要求每个中间 Gram 非退化。尚未证明实际 ladder 终止；这里只把条件准确降成四个更高 residual tests，而不是把 algorithm 当作已完成非零性证明。

对于冻结 auxiliary p=18r+1、n=4r、m=2r，已有 bordered identity 说明 k_1=corank M5，即全部后续障碍只需在真正 leading radical 上处理。leading M5 奇异不再自动停止研究；但实际 residual forms 仍须算术证明。这里没有由 Jacobi/full-Q unit 免费推出它们。

## V6. 费用和实际 lift 的边界

所有 basis 与 Schur transformations 仅在 Z_p 上，原 S 的实处范数与解析 bound 保持原费用。单个 p≈n 的辅助判据只产生 O(n log n) 量级定标，不降低 n² safe A；本稿不把精度增益加到同轮 weighted paid 积分中。原 degree cutoff、primitive gcd、真实 half jet 均保留。实际 X 系数为 V1，故这份证明不必另算或假设 higher-source jets；higher sources 仍决定 anchor 的未知 residual forms。

## V7. 来源和有限验证

本轮实际全文读取冻结 actual-local-Gram G1–G15/G1–G13、actual-unit-sector U1–U10/U1–U21、single-bordered B1–B8/B1–B11，以及 auxiliary head-free A1–A13/A1–A32。其定义和既证 DND 是输入；V2–V5 在本文给出新的全尺度证明。未新增下载、未声称已完整重读任何 primary PDF，未用 generic eigenvalue 等同 Smith 指数。

NEW [自有源](cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.py)先完整静态读取，再首次且唯一运行1次，exit0 PASS66037checks。它从 factorial gcd 与原 S literal 定义重建旧 r=1,2,4 的 actual 配对基，按真实 unit-tail evaluation 选核并 lift，核 V6/V7 的全部节点和 blocks；不扩 auxiliary-prime unit 表，不计算 actual higher-layer Smith。三个 cases 的 unit-tail 像秩为5/10/20，weak 维数3/6/12；实际 normalized value-Gram modp 的秩恰8/16/32。这最后一项只是原 X 系数的有限取值 Gram，不是 anchor N(c) 或无限 nonzero 证据。

另以 mixed congruence 的一般矩阵验证 ladder 的指数0/1/2/3/4和 p⁵ 阈值，toy 与本题模型严格区别。guard 在数学执行前 exclusive-create 输出；失败会保留记录且不 rerun。实际成功1、失败0、rerun0、旧同行 execute/import0、Lean0；成功 source 与 [JSON](cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.json)保持只读。source SHA256 bc3a54157f1d36c892ecbbf1f4209737244ecdfe5533bec49da95e52b4e24785。root 已完整读取全部保存 JSON 字段；最终文件指纹另登记于来源收据。

## V8. 当前结论与缺口

已证：全部所列 large primes 的真实 normalized value-Gram 整性；actual N_X 的 p⁵ 精度；允许最大 Smith 指数4的条件 whole-X 常数非零；无未知 Gram 逆的有限 obstruction ladder。仍缺：实际 higher-layer 最大指数≤4在无限子列上的算术证明、无限 original D_A 非零以及足够的解析—算术严格余量。没有新增 ζ/L/Catalan 无理性或线性无关性定理，也没有新 Lean 证明。本文待独审，尚未冻结。
