# Θ 载体的精确秩、全素数分母与有理变基必要费用

2026-10-07。隔离新增研究稿。本文实际全文读取 `cdt_weight4_space_germ_bridge_20261007.md` 九节 S1–S40；只研究其 S37–S40 的同一个实际空间芽。没有运行旧 producer、修改 main/manifest 或把有限 prime 样本作为证明。以下结论均为纸证；没有新数值无理性或 LI 定理。

记 θ=x∂x，并固定从0正规化的实际枝

\[
 R=\log(1+x^2)-\log(1+x),\qquad
 P=\theta^2D,\quad Q=\theta D,
\]
\[
 R'=\frac{2x}{1+x^2}-\frac1{1+x},\quad
 P'=-\frac{R}{1-x^2},\quad Q'=P/x,\quad D'=Q/x,
\]
\[
 R(0)=P(0)=Q(0)=D(0)=0,\qquad
 F_u'=(D-u)/(1-x),\quad F_u(0)=0.
 \tag{T1}
\]

这里 D=A−B/2 正是 S37 的实际函数，Θ=D(1)>0；并未换成其他 particular solution。u∈Q 即保证 F_u 的有理 Taylor 系数；进一步仅 Θ=u 使其 canonical branch 完整填入1。以下秩结论对任意 u∈C 都成立，算术结论固定 u∈Q；费用不把这两件事混淆。

## 1. 五项实际空间的精确秩

取实 basepoint b∈(0,1)。选择由它出发、绕 i 一周且不绕0、−1、1、−i的 based loop α；使用一条固定 bridge 来决定 log x 在 i 附近的值。R 的 monodromy 增量是 c=2πi。原 canonical R 在1全纯且 R(1)=0，原 P,Q,D 在1也全纯。

在 α 运输后的枝，R(1)=c。写 h=x−1，则

\[
 P'=\frac{c}{2h}+O(1),\quad
 P=\frac c2\log h+\text{holomorphic},
\]

Q、D 分别只有 h log h、h² log h 起始的非解析项。令 β 为该 transported branch 上绕1的 small loop，k=πic≠0。完整局部 monodromy 满足

\[
 \Delta_\beta P=k,\qquad
 \Delta_\beta Q=k\log x,\qquad
 \Delta_\beta D=\frac k2(\log x)^2.
 \tag{T2}
\]

第一式来自实际 residue c/2；第二、三式来自 θ 导数链。积分常数由 Q、D 的 jump 在 x=1 消失而确定，因此不是只比较 leading log coefficient。β 不改变 R；log x 在1单值。沿 α 的逆 bridge 撤回，不绕0，故 T2 中的 log x 不发生平移。得到原 basepoint 上的一个 conjugate loop γ，其完整作用是

\[
 \Delta_\gamma R=0,\quad
 \Delta_\gamma P=k,\quad
 \Delta_\gamma Q=k\log x,\quad
 \Delta_\gamma D=k(\log x)^2/2.
 \tag{T3}
\]

若 a0+aR R+aP P+aQ Q+aD D=0、各 a∈C(x)，沿 γ 继续并相减，得到

\[
 a_P+a_Q\log x+\frac{a_D}{2}(\log x)^2=0.
\]

log x 对 C(x) 超越：绕0任意多次会把它平移2πiq，一个非零有限次多项式不能有这些无限多个根。因此 aD=aQ=aP=0。再沿 α，R 增加 c，迫 aR=0，最后 a0=0。于是

\[
 \boxed{\dim_{\mathbb C(x)}\langle1,R,P,Q,D\rangle=5.}
 \tag{T4}
\]

该证明同时使用1的 transported branch 和0的实际 logarithmic monodromy；不以 canonical branch 在1全纯推断整个 differential system 在1 ordinary。

## 2. 单关系下 F 仍增加一个真实方向

若 u≠Θ，canonical loop β 绕1已给 ΔF_u=2πi(u−Θ)≠0，而前五项不变，故任何 relation 中 F 的 coefficient 为0。

若 u=Θ，canonical β 确实平凡。先沿 T3 的 γ，再绕0 q次。原 D 在0是正规 Taylor 芽，而 γ 添加 k(log x)²/2；运输后的 D 在1仍全纯，但值变成

\[
 D_{\rm transported}(1)=\Theta+\frac k2(2\pi iq)^2.
 \tag{T5}
\]

取 q=1 即与 Θ 不同。该 branch 绕1时前五项全都单值（log x 在1普通），F 的 jump 为非零常数 −2πi·k(2πi)²/2。撤回此前 γ 和0的 loops 后，前五项回到原枝；这个 constant jump 保留，因为 analytic continuation 对常数为恒等。故有一个实际 loop 仅平移 F。对任何 C(x) relation 应用该 loop，迫其 F coefficient 为0，再用 T4。

\[
 \boxed{\dim_{\mathbb C(x)}\langle1,R,P,Q,D,F_u\rangle=6
 \quad\text{对所有 }u\in\mathbb C.}
 \tag{T6}
\]

在 Θ=u∈Q 的假设下，所有六项是 Q-Taylor 的 holonomic 芽，故其 Q(x) 秩也精确为6。T1 本身给闭合 rational first-order system；没有借抽象 period symbols 或低阶 Wronskian 数值样本。

## 3. 系数公式与全部有限素数的有效 cap

设 c_n=(-1)^n−2cos(nπ/2)∈{−1,3}。逐项展开 T1：

\[
 R_n=[x^n]R=c_n/n,\qquad
 S_n=-\sum_{\substack{1\le j<n\\j\equiv n-1\ (2)}}\frac{c_j}{j},
\]
\[
 P_n=S_n/n,\quad Q_n=S_n/n^2,\quad D_n=S_n/n^3,
 \qquad (F_u)_N=\frac{\sum_{n<N}D_n-u}{N}.
 \tag{T7}
\]

特别地，n=2m 时 S_n=Σ_{j≤2m−1,j odd}1/j；n=2m+1 时 S_n=H_{⌊m/2⌋}−3H_m/2。n=2 给 D_2=1/8，确认符号。令 \(\mathcal L_N=\operatorname{lcm}(1,\dots,N)\)、\(\mathcal L_0=1\)。固定 d>0 使 du∈Z。直接得到全部 n,N、全部 p^a 的 cap

\[
 nR_n\in\mathbb Z,\quad
 n\mathcal L_{n-1}P_n\in\mathbb Z,\quad
 n^2\mathcal L_{n-1}Q_n\in\mathbb Z,\quad
 n^3\mathcal L_{n-1}D_n\in\mathbb Z.
 \tag{T8}
\]

不需要192这一旧 pool 的共同 normalization：T7 的 colors 已是整数；仅 d 支付固定 u 的分母。

还有一个更精细的全 prime floor cap。对整数 1≤j<n≤N、s≥1，

\[
 jn^s\mid\mathcal L_N^s\mathcal L_{\lfloor N/2\rfloor}.
 \tag{T9}
\]

证明：固定任意素数 p，A=v_p(\mathcal L_N)，B=v_p(\mathcal L_{⌊N/2⌋})，a=v_p(n)，b=v_p(j)。若 b≤B，则 sa+b≤sA+B。若 b>B，则 b=A，且 p^A>N/2；N以内仅有一个 p^A 的倍数。因 j≠n，a≤B，于是 sa+b≤sB+A≤sA+B。此证明包括 p=2、小素数、任意高次 prime power，且不要求 colors 或 parity 的额外取消。

由 T7/T9，

\[
 \mathcal L_N\mathcal L_{\lfloor N/2\rfloor}P_N,
 \quad\mathcal L_N^2\mathcal L_{\lfloor N/2\rfloor}Q_N,
 \quad\mathcal L_N^3\mathcal L_{\lfloor N/2\rfloor}D_N\in\mathbb Z,
\]
\[
 \boxed{dN\mathcal L_{N-1}^3\mathcal L_{\lfloor(N-1)/2\rfloor}(F_u)_N
 \in\mathbb Z.}
 \tag{T10}
\]

T8 与 T10 有不同用途，不能把各自最便宜的局部因子未证明地混在一起。一个有效 CDT fixed-type 阵列是

\[
 \sigma=(0,0,1,1,1,7/2),\qquad
 e=(0,1,1,2,3,1),\qquad
 \tau^{\flat}=119/72.
 \tag{T11}
\]

在实际输入中把 T8/T10 的 N−1 上标增加至 N，全部 columns 可取零 offset。三个 width-one columns 中，一个从 P 行开始、另两个只在 F 行出现；一个 width-half column 只在 F 行出现，故各列符合阶梯条件。完整 τ 还须加 CDT 的 τsharp(e)，T11 不删掉它。若要求 e=0 的无需 minimization 输入，则吸收各 n^s，并使用 T10 得有效

\[
 \sigma=(0,1,3/2,5/2,7/2,9/2),\quad e=0,\quad
 \tau_{\rm safe}=109/36.
 \tag{T12}
\]

例如 width-half column 从 P 行开始，四个 width-one columns 依次从 R,Q,D,F 行开始。T12 比旧 (0,1,2,3,4,5) 的125/36更便宜，但二者都只是有效上界；不称最小必要费用。

## 4. 2p 附近的四层全素数 response

从现在起固定任意实际 row

\[
 W=a_0+a_RR+a_PP+a_QQ+a_DD+a_FF_u\in\mathbb Q[[x]],
 \quad a_\bullet\in\mathbb Q(x).
 \tag{T13}
\]

各 a 可在0有有限 Laurent pole，组合只须正规。除固定有限 primes 后，各 a 的整个无限 Laurent tail 均 p-integral：把它写成 x^h A/B，B(0)≠0，用 formal inverse 的整数递推即可。下述 witness 的偏移全固定，再令 p 增长。

对足够大的 odd prime p，2p 的内和中唯一 p-divisible term 是 j=p，c_p=−1，所以

\[
 p^4D_{2p}\equiv1/8\pmod p,\qquad v_p(D_{2p})=-4.
 \tag{T14}
\]

P_{2p},Q_{2p} 分别最深为−2、−3。对于固定 k>0，D_{2p+k} 最深为−1；n=p 可至−3，仍不到−4。F_{2p} 至少具有 valuation≥−4，记 C_p=p^4(F_u)_{2p}∈Z_(p)。F_{2p+k} 在−4层只来自 D_{2p}/(2p+k)，故

\[
 p^4(F_u)_{2p+k}\equiv\frac1{8k}\pmod p.
 \tag{T15}
\]

允许完整 rational tails，且取 p 大到3p之外的索引不能进入固定-offset convolution。于是对固定 t≠0，

\[
 p^4W_{2p+t}\equiv
 \frac18[x^t](a_D+a_FL)+C_p[x^t]a_F\pmod p,
 \quad L=-\log(1-x).
 \tag{T16}
\]

负 Laurent shifts 仅改变一个固定 lower bound。若 aF≠0，则 aD+aF L 不可能等于 κaF 加一个常数（κ∈Q），否则 L 是 rational。故在非零 t 的 coefficient space 中，两向量 aD+aFL、aF 不会依赖；若 aF 在该 coefficient space 为0，则前向量自身非零。可取一组有限非零 offsets 及固定 rational linear functional λ，使 λ(aF)=0、λ(aD+aFL)≠0。除有限 primes 后 λ 及其非零值是 p-units，因此 T16 迫使每个 sufficiently large odd prime p 至少有其中一个 t 满足

\[
 \boxed{v_p(W_{2p+t})=-4\quad(a_F\ne0).}
 \tag{T17}
\]

这是全 prime 的有限集合 witness；不假设同一个 t 对所有 p 有效，不需要预测 C_p 或 Fermat quotient。

若 W 具有任何 fixed type

\[
 W_N=\frac{z_N}{N^e\prod_\ell\mathcal L_{\lfloor b_\ell N+c_\ell\rfloor}},
 \quad z_N\in\mathbb Z,
 \quad e,b_\ell,c_\ell\text{固定},\quad b_\ell\ge0,
 \tag{T18}
\]

则 p∤(2p+t)，N^e 不支付这些 p 层；每个固定 LCM factor 最终至多贡献一层。b<1/2 的 column 最终不含 p。因此至少四个 columns 满足 b≥1/2，初步给 σ(W)=Σb≥2。下一节补一个独立的 width-one 必要条件。

## 5. p 附近的 response：避开 Wieferich 未知性

不能直接从 D_p 推断 p^-3 witness：其 S_p mod p 涉及 Fermat quotient。改用实际 fresh input R_p=−1/p 及 p+固定offset 的整段 response。定义正规实际函数

\[
 H(x)=\sum_{k\ge1,\ k\ \text{odd}}x^k/k=\operatorname{artanh}x,
 \quad J(x)=\sum_{k\ge1,\ k\ \text{odd}}x^k/k^2,
\]
\[
 K(x)=\sum_{k\ge1,\ k\ \text{odd}}x^k/k^3,
 \quad B(x)=\int_0^x K(t)/(1-t)\,dt.
 \tag{T19}
\]

这里 B 是此节临时响应函数，与原 S32 的 B(x) 不同；本文仅在本节使用它。θJ=H、θK=J。

需要的独立性是

\[
 1,H,J,K\text{ 在 }\mathbb C(x)\text{ 上独立};\qquad
 B\notin\langle1,H,J,K,L\rangle_{\mathbb C(x)}.
 \tag{T20}
\]

第一式绕1后给 jump 的常数、log x、(log x)²，证明同 T4。为第二式，绕−1的 loop α_- 给

\[
 \Delta H=\pi i,\quad
 \Delta J=\pi i(\log x-\log(-1)),\quad
 \Delta K=\frac{\pi i}{2}(\log x-\log(-1))^2.
\]

bridge 固定 log(-1)=iπ；该 ΔK 在1取非零值。绕1的 loop β_+ 的 H/J/K jumps 亦为 log x 多项式，所以 α_- 与 β_+ 在这三项上 commute，L 的 constant translation 也 commute。Δα_-B 的导数是 Δα_-K/(1-x)，在1有非零 residue；因此 β_+ 使它增加非零 constant。反过来 Δβ_+B 的导数是 Δβ_+K/(1-x)，在−1普通，故 α_- 不改变它。其 commutator 只给 B 一个非零常数平移，而前五项1,H,J,K,L不变，证明 T20。此论证使用完整 primitive branches；不把 endpoint K(1) 的未知有理性当假设。

固定有限 positive offsets k。R_{p+k} 在 k>0 时 p-integral，T7 给

\[
 pP_{p+k}\equiv\begin{cases}1/k&k\ \text{odd},\\0&k\ \text{even},\end{cases}
\quad
 pQ_{p+k}\equiv\begin{cases}1/k^2&k\ \text{odd},\\0&k\ \text{even},\end{cases}
\]
\[
 pD_{p+k}\equiv\begin{cases}1/k^3&k\ \text{odd},\\0&k\ \text{even},\end{cases}\pmod p.
 \tag{T21}
\]

不对 pP_p、pQ_p、pD_p 的 integrality 作假设。这三个值及 pF_p 都作为未知 scalar constants 保留。记有限 coefficient window 中

\[
 L_p(x)=\sum_{k\ge1}\frac{x^k}{p+k}.
\]

F_{p+k} 的 direct coefficient formula 显示，未知 D_p 的贡献准确是 pD_p/(p+k)；其余在 p^-1层来自 Σ_{1≤l<k}D_{p+l}/(p+k)。窗口内的 p-scaled W vector 可写成

\[
 Y_p=C_{P,p}\,a_P+C_{Q,p}\,a_Q+C_{D,p}(a_D+a_FL_p)
       +C_{F,p}\,a_F+Z_p,
 \tag{T22}
\]

这里 C_{P,p}=pP_p、C_{Q,p}=pQ_p、C_{D,p}=pD_p、C_{F,p}=p(F_u)_p。各 C 可以非 p-integral，但全部先于 index p 的函数 coefficients 是 p-integral；除掉 constants 后的 Z_p 是 p-integral，且

\[
 Z_p\equiv Z:=-a_R+a_PH+a_QJ+a_DK+a_FB\pmod p.
 \tag{T23}
\]

上述等式在任何选定有限窗口中准确成立；Zp 的其余项都可并入 p-integral residual。rational multipliers 的完整 tails 不会增加未知 constants：index<p 的函数值 p-integral，index>p 的固定窗口由 T21 闭合。固定 Laurent pole 只扩大窗口一个固定数目。

为避免把“constants 可能非 integral”藏进 mod p，使用一个有限矩阵消元。只取 positive offsets，从 rational functions aP,aQ,aF 中取其 coefficient vectors 的一个基；它们的 constant linear relations 对所有 p 完全相同。若 aF≠0，向量 aD+aF L 不在这个 rational span，即使允许差一个有限 Laurent polynomial。因此可选足够大的有限窗口，使这些 rational columns 加 aD+aF L 的秩为 r+1；同一非零 minor 在 p→0 的 reduction 中是 rational nonzero。将 L 换成 Lp，所选 minor 的 entries 是 p 的 rational functions，且 denominator 在 p=0 非零，所以除有限 primes 后该 minor 是 p-unit。

这里 p→0 只表示辅助符号参数 y 的 rational matrix 在 y=0 评价：先用 L_y=Σx^k/(y+k)，再代 y=p；不是令 primes 在实数意义趋向0。mod p 的 unit 结论来自固定 integer numerator 在 y=p 与 y=0 同余。

由 T20，Z 不在该 span（甚至不在 C(x)+C(x)L）。具体地，若 aF≠0 而 Z 落在 rational+rational·L，则用 T23 解出 B，迫使 B 落在 ⟨1,H,J,K,L⟩_{C(x)}，直接违反 T20；不需要先证明前五项的 full rank。加入 Z 后再选一个 nonzero minor，构造窗口上的 p-integral functional λp。具体在选定的 square submatrix (independent constants columns, Z) 上指定 λp 的输出为 (0,…,0,1)；其 determinant 在 p=0 是固定 nonzero rational，除有限 primes 后是 p-unit。故 Cramer elimination 给 p-integral λp，准确 annihilate T22 的四个 unknown-constant columns，且 λp(Z)=1。由 Zp≡Z 得 λp(Zp)≡1 mod p。这只是有限 rational matrix 的消元；各 entries 是固定 offsets 下的1/(p+k)，没有 asymptotic 或 prime-density 假设。若所有所选 W_{p+t} 都 p-integral，则 Yp 的所有 entries 属于 pZ_(p)，与 λp(Yp)=λp(Zp) 为 p-unit 矛盾。

若 aF=0、但 aP,aQ,aD 不全为0，则 constants columns 全是 rational。若 Z 也是 rational，T23 便给出1,H,J,K的非平凡 C(x) relation，直接违反 T20 第一式；故同一有限消元更简单，完全不用 Lp。于是对每个 sufficiently large odd prime p，

\[
 \boxed{W\notin\langle1,R\rangle_{\mathbb Q(x)}
 \Longrightarrow\text{某个固定有限集合的 }t>0\text{ 满足 }v_p(W_{p+t})<0.}
 \tag{T24}
\]

T24 不声称 valuation 必为−3，恰好只证明所需的 width-one 必要条件。p∤(p+t)，所以任何 fixed N^e 都不能支付。若所有 b<1，则 T18 的全部 LCM factors 最终也不能支付。因此

\[
 W\notin\langle1,R\rangle\Longrightarrow\text{至少一个 column }b\ge1.
 \tag{T25}
\]

合并 T17 与 T25：任何 aF≠0 的 row，至少四个 columns 有 b≥1/2，且至少一个有 b≥1，故

\[
 \boxed{a_F\ne0\Longrightarrow\sigma(W)\ge5/2.}
 \tag{T26}
\]

这一费用来自每个充分大 prime 的必要响应，而非只统计已知 non-Wieferich primes；不需要其 infinitude、density 或 abc conjecture。

## 6. 任意 full Q(x) basis 的必要 CDT 费用

固定真正六维空间 V=⟨1,R,P,Q,D,F_u⟩。子空间 V0=⟨1,R⟩ 的维数恰为2。任一 full basis 至少四行在 V0 外，由 T25 各有 σ≥1；至少一行 aF≠0，由 T26 有 σ≥5/2。CDT column-step condition 使 row sums 非降，因此任意这类有效 fixed-type array 至少满足

\[
 \sigma\ \ge\ (0,0,1,1,1,5/2)
\]

按逐项必要比较，

\[
 \boxed{\tau\ge\tau^{\flat}
 \ge\frac{5+7+9+11\cdot(5/2)}{36}
 =\frac{97}{72}.}
 \tag{T27}
\]

允许所有 rational gauge、0处有限 poles、完整 infinite Taylor tails、不同 integer e 和固定 normalization；τsharp≥0 不降低此界。T27 是必要费用，T11–T12 是可行 cap，二者保留间隙。没有声称找到精确最小 τ。

原 S39/S40 canonical leaf Dmix 包含于 Dβ=C\(i[1,∞)∪−i[1,∞))，到 Dmix 的0固定 holomorphic map 满足 |φ′(0)|≤2。因此 T27 已有97/72>1>log2，连 CDT positive denominator 都不成立。在这个 leaf 上，任何此 full six-dimensional carrier 的 Q(x) basis 都不能给新无理性结论。该结论不排除 root 正在构造的不同周期 carrier、不同函数子空间或更大 monodromy-compatible map；也不把函数秩6当作 Θ 的数值无理性。

## 7. 实际审计范围

root随后实际 FULL 读取本文七节 T1–T27，并独立纸核 T2/T3 的完整 log 初值、T5/T6 的 pure F constant translation、T9 的全部 prime powers、T16/T17 的四层响应、T22–T24 的 finite p-dependent exact annihilation 及 T27 的97/72必要界，数学 PASS。仅要求统一 T19/T21 奇偶条件的 \text{odd/even} 渲染，并把 T24 直接调用 T20 的逻辑显写；作者已完成这两项文字补强，并最后再次 FULL 回读本文。此收据是明确写后数学审阅，不把文件 hash 或有限样本当证明。

本轮输入 FULL 阅读：桥接稿九节 S1–S40，工具返回的完整6848-token source（含最后审计段）；没有将仅搜索摘要计为全文。本文 T1–T27 均独立纸面推导；T9 覆盖全部 finite primes 和 prime powers，T17/T24 是每个 sufficiently large odd prime 的必要 witness，排除的 finite exceptions 只来自固定 rational coefficients/minors。必要下界不依赖这些被排除 primes；不声称任意 rational gauge 在 bad primes 的整个无限 tail 都能由一次 scaling 清除。实际有效阵列 T8–T12 已自行支付所有有限处。

执行范围：读取源稿；新增本文；随后全文回读本文。旧 producer、PSLQ、prime 样本扩表、浮点 quadrature、Lean、外部数学代码全部未运行。未浏览新的网页、未下载新PDF，故没有新增 literature 引用；CDT fixed-type 与 τflat 的定义使用已全文读的桥接稿所明确记录的 primary §2.1–2.2 接口。本文不声称本轮独立全文读取 CDT 或 Panzer 原论文。

随后另实际 FULL 阅读并独立审阅并行稿 `cdt_theta_involution_period_projection_20261007.md` 十一节 I1–I20。逐式重推 source 对合、两个不同积分核、dilog derivative/0初值、全 s 的2^(−s−1)系数、I11严格尾界、I14递推及端点、I15的路径分母次数和 c_nj∈2^jZ 对所有 dyadic terminal 的清理、I16/I17全 prime cap、I19 residue/Legendre 系数及 I20指数增长，数学 PASS。只指出一处“围绕t−1”应明确写为“围绕t=−1”的文字问题；未把 hash、样本或未经读取的文献算作数学审阅。这个并行稿没有被本轮修改。
