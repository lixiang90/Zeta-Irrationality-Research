# 完整 F 新分母与 whole-prefix recurrence：独立纸面核查

日期：2026-10-06。审稿对象为新文件 [complete F high filtration](cdt_odd_complete_F_high_filtration_20261006.md)。独审者为 current_r0。全文实际阅读，严格核查范围为 §§2–3，并额外核对 §4 的 Ore identity、fast/slow derivative 与 primitive rank count。没有执行/import 原稿、冻结稿或任何数学 producer；没有宣称 finite certificate 或 Lean verification。

## 1. All odd p-powers 的安全界通过

固定 odd p，a=floor(log_p n)、b=floor(log_p(2n))，b−a只能是0或1。每个 Taylor monomial 对 A_n^4 删除 u 因子、B_n,k^4 作 l 阶 expansion、线性项取 v=0/1，u+l+v=j=4−i。连续长度 n、step 2 的 half-integer progression 对 odd p 每层至少 floor(n/p^s) 命中；因此 A 的低层亏损最多 ua。B 的 constant 是整数 binomial 的四次方，additional inverse-power denominator 仅用 ≤n 的非零整数距离，亏损最多 la。于是 r 的低层界 −ja 是针对同一个 monomial 的合法逐层计数，不是把已求和系数的多个独立估值不合法相加。

最容易遗漏的 q=p^b>n 命中也核查通过：2ℓ−1=q 是唯一可能，k≥(q+1)/2。在 A_n(−k+u) 内 m=k−(q+1)/2 属于0,…,n−1，因子恰为 −q/2。四份 A 中四次出现该因子；删除 u≤4−i 份后，至少 i 份保留。q 层在 n! 和 B-distance denominators 内均不出现。故新高层 gain ≥i，最终 harmonic product 的界为 −8a−4。若 b=a，界为 −8a。两者统一为

\[
 v_p(C_{n,2})\ge-4\lfloor\log_p n\rfloor
                    -4\lfloor\log_p(2n)\rfloor.
\]

这核实了 §2 F5，不依赖“只看 n<p 的大素数首层”。乘 (i)_4 只增加 valuation；求和不会降低共同下界。对 fixed rational c，整数 A_n 与 fixed initial denominator D0 被计入后，同一界适用于实际 F 的四个 Euler derivatives。仅声明 odd part Δ_n^4Δ_2n^4 是安全表，未证明最小分母。

## 2. 实际 forcing 与完整 prefix block 通过

实际 source 的 forcing 是 960x−(3/2)xθ²P3H，不是960/x。p²>2N+1 在整个 n<N prefix 保证 p^8F 与 p^4H integral；因此 p^8 forcing 至少含 p^4。这给 L5(p^8F)=0 mod(p^4,x^N)，并未改为齐次 rank5 模型。

recurrence 的 n 行系数依次为 n^5、−(2n−1)Q(n−1)/8、(n−1)^5；代 n=kp+j 精确得到 F7 的 ρ=kp。j=1 时前一 block 项系数是 (kp)^5；其 valuation 至少5，故 mod p² 被杀，无需假设该项实际 coefficient 为零。对1≤j<p，kp+j为unit，逐次 recurrence 确定当前 block，其自由 initial coefficient w_k=U_kp 完整保留。

Frobenius rational t_j(ρ) 的 denominators 在0≤j<p、ρ=0为p-units，值和一阶导数 p-integral；ρ=kp 的 first-order Taylor remainder 属 p²。归纳得到全部 blocks

\[
 U_{kp+j}=w_k\{t_j(0)+kp\,t'_j(0)\}\pmod{p^2}.
\]

没有除 w_k，没有跨 j=p 的 nonunit boundary 除数；最后 partial block 的 truncation 有效。它正是 F10 的 whole-prefix identity，慢导数 bias 为0。

## 3. 附加核对 §4 的关系与 primitive ranks

令 B=TθV−VθT、Q_T=T²+B。F10 直接给

\[
 (\theta-\theta T/T)U
 =p(Q_T/T)\theta_sW\pmod{p^2}.
\]

第二算子取 θ−θ(Q_T/T)/(Q_T/T)，只剩 p² 级慢导数。清分母后的三系数正是 F11：P2=Q_TT、P1=−(θQ_T)T、P0=(θQ_T)(θT)−Q_Tθ²T。独立使用 Ore relation θa=aθ+θ(a)，核实

\[
 \mathcal M_2=(Q_T\theta-\theta Q_T)\mathcal M_1.
\]

T(0)=Q_T(0)=1，故最高 derivative coefficients 非零 modp。四个 order1–4 families 与三个 order2–4 families 分别给 4(D−p+2)_+、3(D−3p+4)_+。第二层 multiplier degree≤2(p−1)，保证它的 modp span 位于第一层而非额外七个 ordinary kernels。这个两层区分与原 derivative supports 一致。

## 4. 审核结论与范围限制

§§2–3 新 all-p-power denominator、准确 forcing、全 prefix recurrence 通过独立纸面核查；§4 的 polynomial Ore relation 和 rank/nesting count 亦通过。本次没有独立重审旧 H 源的 Smith proof、archimedean geometry、HS transport、balanced tensor、最终 τ/κ，不能把这个报告当作对 §5 的最终 CDT cost 验收。

实际 source 仍是完整 rank10；dyadic native-x coordinate 主成本仍须保留。没有新数值无理性结果。
