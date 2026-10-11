# 同一真实配对格的 carry、jet、镜像能量与辛缺陷：root 综合独审

2026-10-06。本稿是 NEW 审阅与兼容性证明。旧及同行数学 producers 全部只读，execute/import/rerun 为0。root 自有三个 NEW producers 的首次执行历史为2成功、1失败；失败源与失败记录保留，不称 PASS，不重跑。本文不新增数学程序。

## 1. 实际读取范围与对象固定

本轮 root 实际完整读取以下 NEW 数学稿及所列源码：

- dual carry，最终 SHA `0fb995f69cefcd4e6c92f7ffa42a8e595add4dda9a94951ed27a4693fb127047`。先全文读取073251版本，再实际复读最终三处措辞修正；数学不变。root 是作者，本文不将这部分自审冒充独审，正式独审由 quarter 的 NEW 联合 review 给出。
- large-prime jet，SHA `39a0b6f80c4020602aff6dccded6d8da71ce0288b06a4ad86890be3265deb0f5`，完整 J1–J23，完整 PY 静态，已存 JSON 全部43 cases 全字段。未执行其程序。
- mirror-choice energy，SHA `cc3821c935474ea1b87011383230b91ac04dcb147c2b09d6ce65e5f899438dd7`，完整 M1–M23及九节，完整 PY 静态；JSON 实际读取证书摘要、4096区间数量、首尾与最小794号区间。未逐条人工回读全部4096区间，不称原始 JSON 全文件独审；下界证书算法在源码中已完整核查。
- auxiliary Padé/symplectic defect，SHA `452d0271f294b304f3b8bd2a65b343ae5e8b1af128267750e7c9118862066be2`，完整 D1–D25及十节，完整 PY 静态；原始 JSON 首次组合输出截断，随后全部五个case、14个scalar与42个matrix profiles以完整compact字段实际补读。不是新的数学执行。

以上对象始终是原 B6/k3/s5、degree<3n 的实际 saturated rank2n 配对格及其原 whole-polynomial form D_A(X)。真实投影为固定有理 a,b、b≠0 的 aζ(4)+bζ(5)。没有将 degree profile 或新 ambient 对象的便宜界免费移到原对象；没有直接证明单独ζ(7)、Catalan或奇数值集合的独立性。

## 2. Jet 稿全尺度证明的独核

当 3n<p≤6n，ambient factorial units 使 Newton/monomial 转换为 GL_{3n}(Z_p)。head 的2n节点互异，primitive pair constraints 在 Z_p 上满射，因此模p weak space 可提升到真实 paired lattice；有限探针中的任意模p代表仅验证机制，不是这些 exact lifts。

对 p>4n，head stripped unit d_z/p=−A(z)，A=(t)_{6n+1-p}，P=AQ 后 primitive constraints 恰为 Q(z)=Q(2n+1−z)。degree Q<K=p−3n−1。关于中点的偶部分有 ceil(K/2) 维，奇部分必须被2n个head的偶节点多项式整除，贡献 max(0,floor((K−2n)/2))，得到文中 k。

对 3n<p<4n，H=2p−6n、J=8n+1−2p，H+J=2n+1。head z<H 的 valuation1 unit 是 −AB；z≥H 的 valuation2 unit 是 −2AB'。mixed pairs 迫使其 valuation2 端的 P 值消失。

若 H≤n，写 B=IZ、Q=ZR；overlap 的 I 有偶 degree L=2n+2−2H，I' 关于中点为奇，故 R_even 被 I 整除。degree R<D=11n−3p+1，dim=floor(D/2)+ceil((D−L)/2)=4n−p。

若 H>n，写 Q=BR，degree R<D=p−3n−1；central valuation1 的偶 degree 节点多项式迫 R_odd 被整除。维数 ceil(D/2)+max(0,floor((D−L)/2))，L=4p−14n−2，正好得到另一 max 公式。端点 p=4n 对整数n不可能为素数，无隐藏边界遗漏。

令 M=p^5 B_X。在 head，M entries 至少 p^4；unit-tail 的 derivative coefficient 至少 p，value coefficient 整体 X 至少 integral。weak polynomial 在全部unit-tail值被p整除，其他tail权重至少p^3。于是 strong/weak block被p整除，weak/weak被p²整除。M=DND 的 D 在 k 个weak坐标为p，其余为1，N integral。这直接给全部 r-minors lower bound −5r+2(r−(2n−k))_+，尤其 v_p^Gauss D_A≥−10n+2k。未声称这些 lower bounds 是完整 Smith 等式。

与冻结 raw/cap 取 max 后，paid gains仅为 11/3<x<4 的3x−11和4<x<5的5−x，总积分1/6+1/2=2/3。没有借未知 Gram units 或无限非零。

## 3. 镜像能量稿独核

先固定 k 个 left choices，q=k/n。最小 κ损失是末 k 个 mirror ratios 的和，给 n²P(q)+O(nlogn)。sorted low nodes 的两组逐项范围给 LL/LH/HH 的 Hardy kernel ratio 上界。root分别用三角区、方形区和矩形区积分，独立复原稿中 c_LL、c_LH、c_HH 的 f、f' 公式；κ项的积分亦与 P(q) 一致。

所有 q，包括0与1，log端点以 uniform O(nlogn) 支付；2^n selections 只给 O(n)。NEW exact log interval 源码使用正尾界、负scale时交换端点、f/f' 的有界区间/单调区间、P 的单调下界。4096个closed cells完整覆盖[0,1]；global lower取cell lower最小，global upper仅取一个midpoint候选。故

\[
0.840144459\le c_*\le0.845115370,
\qquad \beta_{\rm mirror}>9.09188285412558.
\]

同一个 primitive Γ^{-2} 因子沿用冻结 gcd 下界，故

\[
\beta_{\rm mirror}+2\gamma>12.00357285412558.
\]

严格凹变分式也核查通过：K(x,y)=log|x−y|/(x+y)在 u=log x 后展开为负的奇数阶指数核；每个核都有平方积分表示，非零signed density至少ell=1严格正，因此唯一 maximizer。log-tail控制与网格rounding recovery足以证明正镜像包络的精确能量极限。它不是实际复数 determinant 的非零/下界。

## 4. 辛缺陷稿独核

对 scalar及对称matrix graph modules，初始basis determinants分别 P、P²；critical bounds总和分别 N、2N。同 leading position 的 monomial 消元使整数 measure严格下降，得到 weak-Popov；distinct positions 保证 predictable degree。leading matrix 的三角结构证明 sumδ=0，Hilbert function证明 δ multiset intrinsic。

初始 B_0 J B_0^T=PJ，故 graph 上 β(v,w)=vJw^T/P 是 polynomial unimodular alternating form。互补 bound 和等于degP=N，给 degβ_ij≤δ_i+δ_j。form determinant 的一个非零 permutation term迫各δ_i+δ_σ(i)≥0；总和0，故每项都0。这是实际对称配对证明，不是把非退化环境误当截断非退化。

于是 scalar=(-d,d)，matrix=(-d2,-d1,d1,d2)，实际coranks分别 d、d1+d2。strict negative shifted part恰等于冻结稿全部 bounded remainder kernels，不多出只在后半坐标的伪kernel。PSC式的头 P block monic三角、g rows reversal和Laurent unit变换给精确符号。完整ambient两det的Wilson乘积及Jacobi complementary minor亦正确；unknown complementary minor被保留。

真实p37,r2的首 moment148=0而下一moment12，使 size1 Hankel singular、原size2 det=−12²=4。这个反例排除依赖每个 intermediate profile正常的perfect-path证明，但不排除临界目标在无限辅助素数正常。此稿没有证明 d=d1=d2=0的无限族。

## 5. 两个费用改善可相加：同对象、异素数窗口

Dual-carry的paid收益仅支持1<p/n<2；jet收益仅支持11/3<p/n<5。两者均是同一 actual D_A(X) 的 whole-X Gauss lower bound，固定a,b的例外分母只需 O(n)。因此在各自窗口用其较强界，在其余素数用原全n安全界即可，既不double count，也不丢small prime/端点。

同一个 signed common scalar Q_n可满足 D_A/Q_n∈Z[X]，安全费用主率是

\[
A_{\rm combined}
=\frac{1085983123}{24190320}-\frac{1718}{15015}-\frac23
=\frac{4624049789}{104824720}
\in(44.112,44.113).
\]

以上有理数等式与decimal窗口由纸面公分母及整数交叉乘积核查；本文无新增producer。它是安全费用上界，不是实际费用下界。当前解析与分母估计仍不足以推出所需strict positive margin；不能以两者差值证明本方法永不可能成功。

## 6. 准确完成情况

本轮得到三类新结构/估计定理：实际weighted Plücker的全prime对偶与 p>n Smith0/1；large-prime unit-tail exact weak rank及whole-X minor polygon；更强mirror-choice energy和真实临界辛缺陷。对应有限程序只各做首次机制/有理区间核验，不替代全尺度纸面证明。

仍未完成：p≤n高层Smith费用；两个actual auxiliary determinants的无穷同时unit；actual determinant无穷非零；same-object strict margin；任何新的特殊值无理性或线性无关性定理；Lean认证。下一轮优先研究 p≤n 的higher-layer graph及真实 χ 所致的critical balancing，保留singular intermediate profiles。
