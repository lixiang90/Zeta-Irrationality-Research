# inverse-L lift 与同叶对数参考门槛：独立全文审查

2026-10-07，审阅者 `/root/masked_racah_finalize`。实际 FULL 读最终 `cdt_odd_gamma_lift_holonomy_reference_gate_20261007.md`，H1–H20/全部七节，物理 SHA `78eb5777b649336c7906174878f1b5504e34dd012409fdcbb96e13d1390710c7`。此前 H1–H17 的 0f42 候选也实际读过，但本正式审稿只 pin 最终 78eb。结论 **PASS：没有发现需实质修订的数学问题**。以下是纸面独立核查，不是 Lean 或新数值无理性结论。

实际 FULL 的直接数学输入还包括冻结 Gamma G1–G19、其正式独审 R1–R7，以及本轮 source `cdt_odd_gamma_dual_relation_extension_20261007.md` D1–D30/七节（最终 SHA `f8e36b1bf0b605d73574e556bc9cc382a944a07523b74dc5d12a5b64446208ab`）、tensor 主稿 T1–T28/十节（SHA `0a9eb062f5ca02f3337a9532457a01b6b8904e064b2ff1ebf187b302388adc9e`）。source此前c5候选亦实际全文读；其后仅修正共享文献下载owner，本审实际全文重读最终f8稿后更新此输入hash，数学核查不变。本审不把同行原件页数或 root 的588物理基线核查计为自身工作。

## V1. 原坐标、forcing、初值和 complete c-fill

原 L、h_n、整数 Λ 与 Γ 稿一致。Au v4 PDF19 Example X 的 hypergeometric coefficient 为 Λ^m/h_m，special parameter −2^10/5^5 乘 Λ 恰为 A=−2^20；polynomial P 的 degree 四、五个系数、N=380928 的归一全部匹配原件。该式经原文 WZ 评价证明，不把 Guillera 的正向高 rank 猜想代替它，也没有执行其 WZ notebook。

LB=R 的第 n 项是 n^9b_n−Λ∏(n−1+a_i)b_(n−1)=R_n。h_n 的对应齐次 recurrence 给 b_n=h_nΣ_(m≤n)R_m/(m^9h_m)，b_0=0 固定唯一 particular。R5 的 Taylor coefficient 为 −P(m)A^m/N，所以 H3、H4 的 ζ5 恒等式与 source D9/D15–D17 相同。

Stirling h_n∼HΛ^n n^−9/2，加上 P(m)degree4，尾和乘 h_n 的 coefficient 至多 |A|^n 乘一个固定 polynomial 因子，故 ζ5 f0−B5 的 Taylor radius 至少 |A|^−1=|μ|>c。这个真实 holomorphic 差证明 Δ_cB5=ζ5ψ 是完整 germ identity，而非 endpoint value 或 leading branch 配平。Fu 在 u=ζ5∈Q 的假设下同时保有 Q Taylor 和该 c 分支填洞；没有把整个多叶面上所有 transported c generators 当作已消去。

## V2. 全 prime 的 ratio cap 不重复扣 carry

对 q=p^k，C_q(v)=5floor(2{v/q})+floor(5{v/q}) 在0..9。ratio h_n/(m^9h_m) 的单层 deficit 是 C_q(n)−C_q(m)−9·1_(q|m)。q≤n 且 q|m 时 C_q(m)=0，因此该层最低−9；q不整除m时也最低−9。q>n≥m 时 floor(v/q)=0，剩下的 floor(2v/q)、floor(5v/q) 随 v 单调，且 q不整除m，所以该层非负。

因此 v_p ratio≥−9floor(log_p n)，精确由 D_n^9 支付；包括2、5等全部 finite places，不能把 m^9 与 h_m carries 两个最差预算叠为18。P(m)、A^m 为整数，所以固定 N 乘数支付 B5；固定 rational u 的分母也明确支付。D^j 只乘整数 n^j，统一 cap9 的全 jet 数组合法，但它是 safe upper，不是 minimal cap 或实际 content。

## V3. μ 的各分支都有非零 log，所有 admissible maps 因而 omit μ

geo=At/(1−At)=−1−μ/y，y=t−μ；P(D) 的 degree 四首项在 forcing 中准确为 (24·5532μ^5/N)y^−5。L 的 ordinary-coordinate 首系数为 (1−Λμ)μ^9≠0。九次普通导数 ∂_y^9(y^4log y)=24^2y^−5；因此 H9 的 λμ=5532/[24N(1−Λμ)μ^4] 正确且非零。

ordinary variation of constants 给 analytic part 加 analytic homogeneous coefficient乘 log。任何 negative Laurent 首项在 L 后产生至少10阶 pole，不能匹配 forcing 的五阶 pole；任何低于 y^4 的首 log 项亦产生高于五阶 pole。因此首项 y^4log y 不能被其它项抵消。任意分支之差是 L 的 analytic homogeneous solution，λμ 不变；χμ=ΔμFu 是非零 L-solution，且不依赖 u。

若 holomorphic φ 达到 μ，局部有限 ramification order h 使该项成为非零 (z−z0)^(4h)·hlog(z−z0)，仍非 meromorphic。故每个 target-admissible φ 都 omit μ。于是1−Aφ零点不存在，在 simply connected disk 上有唯一规范 holomorphic log lift；所有 ℓ^j∘φ 一同合法。该推理不要求 φ univalent，亦没有把 omit一点误用为一般 conformal derivative 上界。

## V4. 完整函数 rank10，未用 module 秩冒充 function 秩

若 r_*+Q(D)Fu=0，order Q≤8，绕 μ 后 Qχμ=0。冻结 Γ 输入已支付 L 的 C(t)-irreducibility；非零 χμ 的 minimal rational annihilator 因此为 L。低于九阶 Q 必为0，然后 r_*=0。这准确证明 {1,Fu,DFu,…,D^8Fu} 的真实 function rank10。

LFu=r5 给这个十维 span 的 D 闭合及十阶 homogeneous annihilator (D−Dr5/r5)L。任何九阶以下 annihilator 取 μ variation 后必须 annihilate χμ；九阶候选只能是 v(t)L，作用 Fu 为 vr5≠0。故最小 scalar order 确为10。均匀 nine width1 columns 激活除1外全部 rows，给 τ_T(m)=9(m²−1)/m²；m2的27/4不能直接作为 m10费用，m10准确为891/100。

## V5. 同一 maps 的严格 reference 比较

ℓ=log(1−At) 对 C(t) 超越由重复绕 μ 获无穷 ℓ+2πiN 证明；所以1,ℓ,…,ℓ^(m−1)真实独立，各行 holonomic。每个 ℓ^j Taylor composition 项恰j个整数分母≤n，D_n^j 支付，嵌套 width1 array给

τ_R(m)=Σ_(j1..m−1)(2j+1)j/m²=(m−1)(4m+1)/(6m)。

本轮实际 FULL 读 CDT v2 PDF66–69，核对 staircase arrays、e0、holonomic derivative relaxation、φ本身 holomorphic 及各 pullback meromorphic 条件。由于上述参考族沿每个 target-admissible map也合法，ρ>τ_T>τ_R 时，reference theorem使同一 J≥m(ρ−τ_R)>0。τ_T≥τ_R 导致 target quotient J/(ρ−τ_T)≥m，不可能获得严格 contradiction。若ρ≤τ_T，则 target derivative gate本来不成立。

多 map 版本保持相同 m、maps、分割 γ 与整个 rearrangement 分子；γ² log derivative-gap 项与函数数组无关，故同一分子比较完全相同。比较不依赖 largest derivative 的单独估计。2≤m≤10 时差的符号等价 4m²−53m−54<0，凸性和两个负端点足够。m10的 τ_R=123/20，均匀新 cap s 要逃开当前比较，必要 s·99/100<123/20，即 s<205/33；这只是必要账本条件。

## V6. p9 反转、符号及准确首层 scope

独立手核 H18。p>31 时 N,A 为p单位，h_p≡3840。m=p 项给−P(p)A^p≡−30A。其余1≤m<p仅 C_p(m)=9 的 m>4p/5 存活；令 m=p−k，1≤k≤floor(p/5)。Wilson 分别给

(2p−2k)!/p≡−1/(2k−1)!，

(5p−5k)!/p^4≡24(−1)^k/(5k−1)!，

(p−k)!≡(−1)^k/(k−1)!。

合并五个 first factor 和十五个 denominator 得 h_(p−k)/p^9≡−24 (k−1)!^15/[(2k−1)!^5(5k−1)!]。再用 (p−k)^9≡−k^9 及 h_k=160 k^−9(2k−1)!^5(5k−1)!/(k−1)!^15，准确得 p^9h_p/[(p−k)^9h_(p−k)]≡h_k。所有 factorial argument<p，符号和k0补项均支付，所以 Np9b_p≡−AΣP(−k)h_kA^−k。

H19 双向是 p^9b_p 的准确 residue：S_p非零即 valuation−9，S_p为0即 valuation≥−8。固定 rational u 的 p-integral例外之外，−u h_p 不改变该首层。对 floor(p/5)<k<p，C_p(k)≥1，故 H20 延长成 full p−1 截断合法。这里不包含其它n、p² layers或四阶免费改善。

实际 FULL 读 Guillera1908.05123v1 PDF1–4、17：Table5#3与本参数、P(−k)、z0=−5^5/2^10匹配；该未截断正向级数绝对 ratio>1，原件PDF2明确按 analytic continuation 理解。首页说明高rank公式未证，PDF3–4的 general supercongruence 是猜想。另实际 FULL 读1910.01961v1 PDF1–2，所谈 p-adic expansions 明确是 heuristic/conjectural。作者未把这些作为无条件 all-prime theorem，限制准确。

## V7. 正式交付与实际读域

本审支持：一条实际 inverse-L Taylor/完整关系填洞接口、全 finite-place cap9、不可去 μ jump、全 jet rank10、同叶参考族的全 admissible-map账本阻碍，以及一个可检验的具体 top p-layer反转入口。它没有证明新 ζ5/ζ7/Catalan 无理性、最优 cap、prime-power supercongruence、全 integral Betti lattice或 Lean。

本人本轮用于 root reference 独审的额外原件实际读域为 Au v4 PDF19、25–26 共3页（PDF26乱码段另 actual render/view），Guillera1908 v1 PDF1–4、17 共5页，Guillera1910 v1 PDF1–2 共2页；加自己 Euler 主稿直接输入的 GZ7、Laporte10、BV6、CDT4，共 **37 distinct primary PDF页**。render不重复计页。Guillera由 root 共享归档，未重复下载；本分支自行新增两份 Euler 文献共31归档页，不当个人全文页数。

588 frozen只读；当前 audit 仅完整JSON syntax parse、header/schema/count与其物理SHA，不称588条人工FULL或本审独立逐物理核查。旧/同行数学producer、guards及素数表未读取执行或导入重跑；文献提取、render、文件hash不计数学producer。正式审稿保存后须实际FULL审阅者自读，再把最终SHA交作者；本审不pin自己、mutable总稿、未来audit或任何同行FINAL receipt。
