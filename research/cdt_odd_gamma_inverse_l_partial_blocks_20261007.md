# 实际 inverse-L 系数的全部指标整模型、完整素数块与残余块

2026-10-07，作者 /root/source_pencil_finalize。本稿为唯一 NEW 主稿；authority 为 delivery_relative_lift_tensor_reference SHA 61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd，596 冻结记录（591 数学、5 guard）只读。已实际回读主报告当前 header、§§186–190，以及最终 dual/relative extension 与 reference gate 全文。本轮纯纸证，不创建或执行/import/rerun 数学 producer，不执行 guard，不扩展 prime 表。原 paired source 仍是 ξ=αζ(4)+βζ(5)，β≠0；本文研究已明确的 ζ(5) inverse-L 校准对象，不把它免费替换成原 source 的证明。

本稿新增三项：真实全部系数的 carry-sensitive 整模型及其准确指数率；首次包含残余块的 reciprocal 模 p 传递；在一个明确尚未证明的截断和条件下，具有固定 LCM array 的全指标成本 8 极限。逐项分母率与前缀 LCM 成本分别核算，均不宣称新数值无理性。

## 1. 保留实际系数、所有归一化与原有 cap

写 D=t∂t，保留 rank9 hypergeometric 系统

\[
L=D^9-\Lambda t\prod_{i=1}^9(D+a_i),\qquad
\Lambda=2^{10}5^5=3200000,
\quad a=(1/2^{\times5},1/5,2/5,3/5,4/5).
\]

规范齐次周期 f0=Σh_nt^n，其中

\[
h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbb Z,
\quad h_0=1,\quad h_1=3840.
\]

实际 forcing 与规范 particular coefficient 为

\[
A=-2^{20},\quad N=380928=2^{12}\cdot3\cdot31,
\quad P(X)=5532X^4-5600X^3+2275X^2-425X+30,
\]
\[
LB_5=-N^{-1}P(D)\frac{At}{1-At},\qquad B_5(0)=0,
\]
\[
\boxed{b_n:=[t^n]B_5
=-\frac{h_n}{N}\sum_{m=1}^n\frac{P(m)A^m}{m^9h_m}.}
\tag{B1}
\]

这就是冻结 dual 稿 D9/D16 与 reference 稿 H3 的系数，不引入自由 forcing。对固定有理 u，F_u=B5−u f0；关系假设 u=ζ(5) 给一个真实 conifold 填洞，而 μ=1/A 的不可去 ordinary-point 对数仍须支付。本文所有算术结论也适用于 F_u 和 D^jF_u，须额外乘 u 的固定分母。

令 D_n=lcm(1,…,n)，D_0=1。对 q=p^k 定义实际 factorial carry

\[
C_q(v)=5\lfloor2\{v/q\}\rfloor+\lfloor5\{v/q\}\rfloor\in\{0,\ldots,9\}.
\tag{B2}
\]

Legendre 公式准确给 v_p(h_v)=Σ_{k≥1}C_{p^k}(v)。冻结 H6 已证 D_n^9 h_n/(m^9h_m) 整；以下保留当时丢掉的 C_q(n)，得到更细结论。

## 2. 无条件全部 n 的 carry-sensitive 分母与准确增长率

**定理 B3（全部有限处，全部指标）。** 定义

\[
\boxed{\Gamma_n=\prod_{p^k\le n}p^{9-C_{p^k}(n)},\qquad\Gamma_0=1.}
\tag{B3}
\]

则 Γ_n 为正整数，且对所有 1≤m≤n，

\[
\Gamma_n\frac{h_n}{m^9h_m}\in\mathbb Z,
\qquad \boxed{N\Gamma_n b_n\in\mathbb Z.}
\tag{B4}
\]

证明逐 p、逐 q=p^k。ratio 的第 q 层 valuation 是

\[
C_q(n)-C_q(m)-9\mathbf1_{q\mid m}.
\]

若 q≤n、q|m，则 C_q(m)=0，该层准确为 C_q(n)−9；若 q≤n、q∤m，则 C_q(m)≤9，该层至少 C_q(n)−9。若 q>n≥m，则 q∤m，且 C_q(v)=5floor(2v/q)+floor(5v/q) 在 0≤v≤n 上单调，该层非负。故总 valuation 至少 Σ_{q≤n}(C_q(n)−9)=−v_p(Γ_n)，包括 p=2,3,5,31 在内。P(m)A^m 为整数，乘固定 N 即得 B4。固定 u 的分母 d_u 给 Nd_uΓ_n[t^n]F_u 整；D^j 只乘整数 n^j，故全 jet 也成立。

这可写成 Γ_n=D_n^9/∏_{p^k≤n}p^{C_{p^k}(n)}。不能把分母除数改成 gcd(D_n^9,h_n)：h_n 还有 q>n 的 carries，那部分在 ratio 证明中只支付了两个 factorial 的相互比较，不能再重复领取。

**定理 B5（逐项上界的精确指数率）。** 自然对数下，

\[
\boxed{\lim_{n\to\infty}\frac{\log\Gamma_n}{n}
=\gamma=\frac{245}{12}-10\log2-5\log5\simeq5.4380.}
\tag{B5}
\]

证明从准确等式

\[
\log\Gamma_n=9\log D_n-\log h_n
+\sum_{p^k>n}C_{p^k}(n)\log p
\tag{B6}
\]

出发。只有 n<p^k≤5n 可能在末项出现。k≥2 的项总数与权重粗估为 O(√n(log n)^2)=o(n)。k=1 的部分准确为

\[
5(\vartheta(2n)-\vartheta(n))
+\sum_{j=1}^4(\vartheta(5n/j)-\vartheta(n)),
\tag{B7}
\]

其中 θ(x)=Σ_{p≤x}log p。素数定理给其主项
5+Σ_{j=1}^4(5/j−1)=137/12；同理 log D_n=n+o(n)。Stirling 给 log h_n=n log Λ−(9/2)log n+O(1)。代入 B6 得 9−logΛ+137/12=245/12−logΛ，正是 B5。这是已证明的显式上界 Γ_n 的率，尚不是实际系数最小分母的率。

**定理 B8（前缀包络恰好恢复旧 cap）。** 对每个 n≥1，

\[
\boxed{\operatorname{lcm}(\Gamma_1,\ldots,\Gamma_n)=D_n^9.}
\tag{B8}
\]

一向由 Γ_k|D_k^9|D_n^9。反向固定 p≤n，取 e=floor(log_p n)、k=p^e≤n。所有 p^j≤k 都整除 k，故 C_{p^j}(k)=0，v_p(Γ_k)=9e，恰为 v_p(D_n^9)。逐 prime 合并即得等式。这个 envelope 提示由 root 提出，本文实际独核其两向证明。

B8 是本显式上界序列的精确 LCM，不证明真实 b_1,…,b_n 的最小公共分母一定是 D_n^9。它明确排除“把 γ 直接填进 CDT row sum”的步骤；多项式辅助函数会混合不同指标，窗口 LCM 仍要单独证明。当前 Γ_n 的真实改进可用于单指标或另外支付的窗口算术，不能越过该接口。

## 3. 只含一个 p 层时的准确 unit 与反转

以下 p>31，n=q p+r，0≤r<p，且 **5n<p²**。置 d=floor(p/5)，

\[
\delta=\lfloor2r/p\rfloor\in\{0,1\},\quad
e=\lfloor5r/p\rfloor\in\{0,\ldots,4\},\quad C=5\delta+e.
\]

此时 5q+e<p、q≤d，所有 h_n factorial 只含第一 p 层。因此 v_p(h_n)=C；记其 unit 为 \(\bar h_n=p^{-C}h_n\bmod p\in\mathbb F_p^\times\)。下列 factorial 计算完全保留该 unit，不能把 h_n 直接当作 p 单位。

**引理 B9（stripped factorial）。** 对 0≤a,b<p，

\[
p^{-a}(ap+b)!\equiv(-1)^a a!b!\pmod p.
\tag{B9}
\]

证明 p-multiples 给 p^aa!；其余 a 个完整块各给 (p−1)!≡−1，剩余尾部给 b!。利用 B9，分离 q 部分与 r 部分，准确得到

\[
\boxed{\bar h_{q p+r}
=h_q(2q+1)^{5\delta}\binom{5q+e}{e}\bar h_r\pmod p.}
\tag{B10}
\]

所有 displayed factorial 与 h_q 都为单位，因为 5q+e<p。具体比值的高位 factorial 是 ((2q+δ)!)^5(5q+e)!/(q!)^{15}，而 r 的高位是 (δ!)^5e!；共有符号 (−1)^C 相消，即得 B10。C=0 时退化为 h_qh_r，其他 C 时不能省略 unit 因子。

**引理 B11（准确最高-carry 反转）。** 若 1≤l≤d、1≤k≤d，m=lp−k，则 5m<p²、v_p(h_m)=9，且

\[
\boxed{p^{-9}h_{lp-k}\equiv
-\frac{h_l l^9}{h_k k^9}\pmod p,\qquad
\frac{p^9}{(lp-k)^9h_{lp-k}}
\equiv\frac{h_k}{l^9h_l}\pmod p.}
\tag{B11}
\]

证明 B9 的高位 factorial 比值是
((2l−1)!)^5(5l−1)!/((l−1)!)^{15}=h_l l^9/160。
低位 Wilson 比值为

\[
\frac{((p-2k)!)^5(p-5k)!}{((p-k)!)^{15}}
\equiv160/(h_k k^9)\pmod p.
\]

这里 (p−a)!≡(−1)^a/(a−1)!，低位比值的符号为 (−1)^{10k+5k−15k}=1；stripped factorial 的总高位符号为 (−1)^9=−1。因此第一等式准确有负号。再用 (lp−k)^9≡−k^9 得第二等式。另 h_{lp}≡h_l，由 B10 的 r=0 case，故 p^9/((lp)^9h_{lp})≡1/(l^9h_l)。本引理只要求所列有限范围；未推成 p² 或所有 prime-power 反转。

## 4. 完整 reciprocal 块与残余块的精确传递

定义实际正向截断和

\[
S_p=\sum_{k=0}^{d}P(-k)h_kA^{-k}\in\mathbb F_p,
\quad U_q=\sum_{l=1}^{q}\frac{A^l}{l^9h_l},\quad U_0=0.
\tag{B12}
\]

U_q 是**无 P(l) 权重**的 reciprocal sum，不等于实际 B5 的 q-th coefficient 除 h_q。这个区别来自 P(lp−k)≡P(−k)，在完整反转后 P 全部留在 S_p，不能误把 U_q 变成 b_q。

**定理 B13（完整块）。** 对 1≤l≤q，

\[
\boxed{p^9\sum_{m=(l-1)p+1}^{lp}
\frac{P(m)A^m}{m^9h_m}
\equiv\frac{A^l}{l^9h_l}S_p\pmod p.}
\tag{B13}
\]

证明 m=lp 贡献 30A^l/(l^9h_l)。其余 surviving terms 恰是 m=lp−k，1≤k≤d；其他 p∤m 的 C_p(m)≤8，乘 p9 后为零。用 B11、P(lp−k)≡P(−k)、A^{lp−k}≡A^{l-k}，并合并 k0 即得。

残余 q-th 块的和不能默认消失。置

\[
T_{p,r}=\sum_{k=\max(1,p-r)}^{d}P(-k)h_kA^{-k},
\quad\text{空区间的和为 }0,
\]
\[
V_{q,r}=\begin{cases}
0,&r<p-d,\\
\displaystyle\frac{A^{q+1}}{(q+1)^9h_{q+1}}T_{p,r},&r\ge p-d.
\end{cases}
\tag{B14}
\]

非空时 e=4、δ=1、C=9，且 5q+e<p 强制 q+1≤d，所以 h_{q+1} 与 (q+1) 是单位。空时不取 h_{d+1} 的 inverse，避免在 q=d 的允许边界引入不存在的单位。

**定理 B15（实际完整加残余块）。** 对每个 p>31、5n<p²，准确

\[
\boxed{N p^{9-C}b_{q p+r}
\equiv-\bar h_n\big(S_p U_q+V_{q,r}\big)\pmod p.}
\tag{B15}
\]

证明完整块由 B13 合计 S_p U_q；残余块只有 m=(q+1)p−k、p−r≤k≤d surviving，恰给 V。再乘 B1 的 −h_n，p^{9-C}h_n=p^9\bar h_n，得到准确身份。所有待约化的项 p9/(m9h_m) 为 p整，因为第一层的亏损至多9。

特别 C≤8 时 V=0。故

\[
\boxed{S_p=0\Longrightarrow
v_p(b_n)\ge\min(0,C-8),\qquad 5n<p^2.}
\tag{B16}
\]

C≤8 时 B15 给 ≥C−8；C9 时只给 ≥0，因为 V 可能不为零。不能把 B16 写成所有 C 都 ≥C−8：那会在 C9 错领一层。

当 n=p+r、C≤8，q=1、h1=3840，B10–B15 化为

\[
\boxed{Np^{9-C}b_{p+r}
\equiv-A\,3^{5\delta}\binom{5+e}{e}\bar h_r S_p\pmod p.}
\tag{B17}
\]

其 prefactor 在 p>31 时均为单位。因此在这些实际首块指标上，S_p=0 **等价于** v_p(b_{p+r})≥C−8；S_p≠0 时准确 v_p(b_{p+r})=C−9。r=0 就是冻结 H18–H19，而本式覆盖首块所有非最高-carry 指标。

## 5. 在抵消假设下仍然 surviving 的明确边界

**定理 B18（残余块可以是实际 p-unit）。** 对 p>31、1≤l≤d，令 n=lp−1；此时 C=9、T_{p,p−1}=S_p−30。B11 给 \(\bar h_n=-h_l l^9/h_1\)，故 B15 准确为

\[
\boxed{N b_{lp-1}\equiv
\frac{h_l l^9U_{l-1}+A^l}{h_1}S_p
-\frac{A^l}{128}\pmod p.}
\tag{B18}
\]

特别若 S_p=0，则

\[
\boxed{N b_{lp-1}\equiv-A^l/128\not\equiv0\pmod p.}
\tag{B19}
\]

尤其 n=2p−1 给 −A²/128。这里 h1=30·128，所有 denominator 与 A,N 都为 p单位。B19 为实际系数的身份，不是任取 forcing 的例子。它不反对 cap8：该指标原来就 p整；它准确否定“完整块抵消后残余块也为零，连 C9 的最后一层也可领取”。

固定有理 u 的 homogeneous subtraction 在该指标有 v_p(u h_n)≥9（除有限分母 prime），所以 B18–B19 的 modulo p 身份也保留在 F_u 上。一般 B15 的 leading normalized residue 亦不受该 subtraction 影响：p^{9-C}u h_n 为 p9 的 p整倍数。D^jF_u 只增加 p-integrality，不能强迫原 B5 的残余块消失。

## 6. 明确尚未证明的条件如何支付为全 n、固定 array 的成本 8

假设

\[
\mathcal H:\quad\exists p_0\ge31\quad
S_p\equiv0\pmod p\text{ 对所有 prime }p>p_0.
\tag{B20}
\]

本稿不证明 H；Guillera 表5的同参数猜想不能当作已证 input。下面是 H 的严格全指标后果，说明不是仅把 b_p 局部结论重新命名。

**定理 B21（小 prime 与高层完整支付）。** 若 H 成立，则存在固定整数 M>0，使所有 n≥1 满足

\[
\boxed{M D_n^8 D_{\lfloor\sqrt{5n}\rfloor}^{3}b_n\in\mathbb Z.}
\tag{B21}
\]

证明置 K=floor√(5n)。对 p>K 且 p≤n，p²>5n，第一层 B16 给 v_p(b_n)≥−8（p>p0），同时 v_p(D_n)=1。对 p≤K，保留无条件 N D_n9 cap；若 a=floor(log_p n)=1，则 v_p(D_K)≥1；若 a≥2，则 p^{floor(a/2)}≤√n≤K，故 3v_p(D_K)≥3floor(a/2)≥a。因此 D_K3 支付从 D_n9 到 D_n8 所差的一个完整 D_n，不遗漏 p²,p³ 等层。

剩余 p≤p0 且 p>K 只出现在 n<p0²/5 的有限初始区间。譬如 M=N D_{ceil(p0²)}^9 已充分支付它们与 N 的 prime，不需对这些 small primes 另作 S_p 假设。这也覆盖 n<p≤5n 的 factorial primes：无条件 ratio 证明在 p>n 时本来 p整。

由于 log D_K=O(√n)，B21 给一个普通非前缀 LCM 格式的 exponential upper rate ≤8。然而 √n-column 不是 CDT6.0.9 的固定 width，下一步另行转换。

**定理 B22（真正固定 LCM array）。** 若 H 成立，则对每个固定 ε>0，有一个固定整数 Mε>0，所有 n≥1 满足

\[
\boxed{M_\epsilon D_n^8D_{\lfloor\epsilon n\rfloor}^{2}b_n\in\mathbb Z.}
\tag{B22}
\]

证明 large n 可要求 εn≥max(√(5n),n^{2/3})。若 p≤√(5n) 且 a=floor(log_p n)=1，D_{floor εn} 至少含 p；若 a=2 同样一层的平方足够。若 a≥3，
p^{ceil(a/2)}≤n^{ceil(a/2)/a}≤n^{2/3}≤εn，因此 2v_p(D_{floor εn})≥2ceil(a/2)≥a。于是其平方支付一个完整 D_n 在所有 small-prime 部分的缺口。其余 prime 与有限 bad prime 用 B21 同样处理；有限 initial n 再乘一个固定 Mε 即可。这里 ε 固定后取 n→∞，不令 ε 随 n 变化。

若 u∈Q，乘其固定分母后 B21–B22 同时覆盖 {1,F_u,DF_u,…,D8F_u}。该真实函数包的 Q(t)-rank10 与 holonomic 性来自冻结 reference H11；取其中常数及任意 m−1 个 distinct jet，2≤m≤10，仍独立。将整个包按 Mε 固定缩放，CDT Theorem6.0.2 的 admissible array 是八列 width1、两列 widthε，第一行0、其余行全部激活，e_i=0。

\[
\boxed{\sigma=(0,8+2\epsilon,\ldots,8+2\epsilon),
\qquad\tau^\flat=(8+2\epsilon)(1-m^{-2}).}
\tag{B23}
\]

每个 ε 的 fixed scale 不改变 Q(t)-rank或 meromorphic pullback 条件；所得 bound 对 ε 连续，故允许取 ε↓0 的极限成本 \(8(1-m^{-2})\)，对应 CDT Remark6.0.12 的 finite-initial scaling 与 continuity 手段。必须先有 H、先有对所有 n 的 B22，才能领取该费用；不能从 S_p 的有限测试、或几个 b_p，直接填写 B23。

## 7. 尚未闭合的实际问题与本轮证据

Guillera1908.05123v1 PDF17 Table5第三项的参数正是五个1/2、1/5,…,4/5，z0=−5^5/2^10，权重 P(−k)=5532k4+5600k3+2275k2+425k+30。本人本轮重新全文读 PDF3–4、17，并目读已存的 PDF17 rendered image，核查指数与列。PDF3–4将对应 supercongruence pattern 作为猜想，不能据表中 χ0=ε0=1 断言这组已证。只在模 p 中，d<k<p 的 h_k 有正 valuation，所以 S_p 可等价写成长度 p 的正向 finite sum；这没有给 p² 或 p9 的 reciprocal 反转。

本稿因此把缺口分成确切对象：无条件 B4–B8 是已付费全部 n 的新整模型；B15–B19 是第一 p 层全部完整及残余块的实际响应；H/B20 是当前 cap8 接口的未证输入。即使另证正向模p9猜想，higher p^k reciprocal 反转仍须包含 stripped factorial 的高阶 harmonic 项和每个 partial block，不可直接领取 cap5。反过来，若在无穷多个大 prime 上证明 S_p≠0，B17会直接证明实际 b_p 需要 p9，这也尚未取得。

逐项 Γ_n 的率 γ<旧 log-reference 的必要门槛并不自动改善 CDT array：B8精确展示 prefix envelope 丢失全部 gain。此外旧 H17 的205/33只是其特定 log reference 比较的必要条件，绝不是存在新余量的充分条件。本稿不借 γ或条件8声称摆脱 μ 的共同参考族；root本轮另研究更强的 algebraic-reference gate，须以其独立最终稿为准。新的数值无理性、完整去 μ jump 或更高层 supercongruence 均未证明。

本轮个人实际阅读：固定 CDT v2 PDF66–69全文四页，核 Definition6.0.1、Theorem6.0.2、Cor6.0.14、Remark6.0.12与69页 window-denominator提示；Guillera1908.05123v1 PDF3–4、17全文三页，并目读既存 PDF17 rendering。distinct primary PDF共7页；无新下载，不把团队页域或上一轮37页计入个人本轮。本稿未使用 Guillera机器数据、WZ程序或其他数学 producer。当前基线596记录只读；本文不冒称人工全文重读所有历史证明。
