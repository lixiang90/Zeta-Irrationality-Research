# 原九阶系统无新增 ordinary jump 的拆分定理：独立全文审阅

2026-10-07，审阅者 /root/source_pencil_finalize，作者 /root/scaled_root_finalize。结论 **PASS，限于明示的 operator、forcing 与完整 jump 条件**。本报告是固定候选的独立纸证审阅，不是 Lean 验证，也不宣称新的数值无理性。

## V1. 实际全文对象、输入与一个已处理的域条件

已实际 FULL 读取最终主稿 research/cdt_odd_gamma_unramified_forcing_split_20261007.md 的全部十节及 U1–U34，最终 SHA256 611485070e8364a2b2905ea60654eac12770b8bb76d3b8d2c6f929b356de37ac，22304 bytes。先读初候选 c433ab12… 后，请作者将 R∈tQ(t) 澄清为 R∈Q(t)∩tQ[[t]]，作者已在中间 e3545018… 及最终正文与 U22 中处理；本文实际 FULL 回读该中间稿，随后在 root 建议加入 U34 后，再实际 FULL 回读当前最终稿。Q(t) 是域，tQ(t) 本身不能表达 R(0)=0，而该条件是 U3/U17 所需，现已准确保留。没有其他修订请求。

authority 为 delivery_relative_lift_tensor_reference SHA 61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd，596 记录只读。本轮本人已实际 FULL 回读冻结 Gamma G1–G19、dual D1–D30 七节与 reference gate 全文；对 tensor 仅新读 T28 附近 Apéry 校准段，不把该 partial reading 记作当前全文读。authority header/§§186–190 已读，JSON parse/当前进展及物理 SHA 已核，不宣称本人人工全文重审596历史记录。

本审阅 fresh primary 为 Golyshev–Mellit0902.2003v1 PDF1–3 全文，尤其 PDF2 irreducibility criterion、finite pseudoreflection 和∞的 eigenvalues。该三页计入本人本轮 primary 合计10 distinct 页（另有本轮自己主稿 CDT66–69 与 Guillera3–4、17 共七页）；不继承作者三页或旧轮页数。数学 producer创建/执行/import/rerun、guard执行、prime扩表和 Lean 均0。

## V2. 任意 ordinary pole 的全部 Laurent 极部与九个完整条件

U6 的 ordinary companion system variation of constants 给有限 Laurent、analytic 项与 analytic homogeneous Hμ log(t−μ)，故完整 jump 恰为2πiHμ。不同 particular branches 的差为 ordinary-point analytic homogeneous solution，所以负 Laurent 部与 Hμ 不随 branch 变化；送回基点的坐标可能变换，但零条件保持。

U7 的首项准确为 \(-\ell_9(\mu)m(m+1)\cdots(m+8)q_{-m}x^{-m-9}\)；Hμlog 的 L-image 最多 pole9。因此 poles≥10 的所有负部由 orders p,…,10 的 triangular equations 唯一确定，coefficients 在 Qbar，不只是 leading coefficient。低阶 poles≤9 负部为空。U9 的两个方向都成立：残余 forcing analytic 与 particular meromorphic 在 ordinary ODE 中等价。

实际 L 关于 dt/t skew-adjoint，可从 a 参数在 a↦1−a 下配对直接复核；冻结 Green identity 因而适用。U10 的小正向 loop 因 local homogeneous v_i 单值，准确给2πi residue，不遗漏 \(t^{-1}\) 因子。非退化 pairing 与 canonical ordinary basis 把完整 jump vanishing 等价为九个有限、代数 residue 条件 U11。只杀最高 log coefficient 没有被当成九个条件。

U12 的 \(\partial_x^9(x^k\log x)=(-1)^{p-1}k!(p-1)!x^{-p}\)，k=9−p，系数与符号通过独核。非零 ordinary homogeneous Hμ 的首阶≤8，故 pole≤9 时显示的首项确非零，冻结 pole5/\(x^4\log x\) 为其特例。

## V3. Galois 下降、polynomial remainder 与完整 splitting

U13 对 unique triangular equations 使用 Galois，而没有对未知 comparison constants 使用 Galois。proper partial-fraction sum 的 pole 集共轭稳定，故 Q∈Q(t)；它在0,c analytic。若所有 ordinary jumps为零，R−LQ 无 finite poles，仍允许∞的 polynomial growth，准确属于 Q[t]。R0=0 与 (LQ)0=0 进一步给 tQ[t]。

U18 的有限截断身份直接来自本 L 的一步 coefficient recurrence：polynomial forcing particular 为 C_S f0−Q_S，C_S∈Q。B_R−Q−B_S 在0 analytic，只能是 −Q(0)f0，故 U19–U20 的符号 C=C_S−Q(0)=−T(0) 正确。T在c analytic，完整 conifold jump于是 Cψ；ψ≠0给 C_R=C∈Q。这证明完整 splitting，而非把所有 B_R 称为有理。

U21 的反向在当前 R 条件下成立。若 rational T在0有 pole，D9 的负整数 indicial term 非零；若在c有 pole，负整数 exponent 不在0,…,7,7/2的 indicial roots 中，均与 analytic R 冲突。其他 ordinary poles由 U7处理。无 rational homogeneous solution 使T唯一。number-field版本保留所有coefficients在同一域，范围正确。

U22 的 pole10 无log例子正确，说明“R有pole便有jump”并非本定理。U23额外要求∞完整jump为零才迫C=0；还可用本轮 GM PDF2 独立核其∞monodromy没有 eigenvalue1（roots为−a_i、全非整数），从而非零 f0不可能被任一∞local monodromy固定。这也避免把∞的base branch误当ordinary-pole条件。

## V4. Rational differential projection 的范围

U24 的χμ非零且属于原不可约 rank9 homogeneous system，其 monodromy orbit张成全部 solution space。rational operator annihilateχ便 annihilate全部orbit。Ore right division的余项order<9，不可能杀九维ordinary solution space，故 A=UL，U∈Q(t)〈D〉。U25因此输出 UR∈Q(t)，对 B_R−u f0也成立；没有把“映到另一系统”误作 annihilation。

constant Euler polynomial Q(D)在c≠0是 ordinary operator，全部解在c analytic，而irreducibility会迫它杀有非零cjump的f0，矛盾。这个论证对任意degree成立，不依靠order<9。χ=0的边界例子与非 rational projectors 均被明确排除，条件没有遗漏。

## V5. 二次拉回的真实 operator、nonsplitting、Taylor 与全部有限处

U26 的δ=(1−x)/(1−2x)D_x是正确 chain rule，δ9不按 commuting coefficients错误展开。0、1、r±、1/2和∞的支集全部保留，critical point不是新增ordinary pole的免费版本。

U29在0的实际 operator expansion 与 n9 diagonal给唯一 Q-Taylor particular，b1=1。U30在x1的δ=u∂u+O(u²)使 rational pole被δ9首项保留；T若analytic则L_pbT(1)=0，与 forcingx=1冲突。因此x确不属于L_pb(C(x))，B非rational，{1,B}实际 Q(x)-rank2。没有把 scalar operator阶数当多行函数秩。

U31的 inverse branch X(t)=ΣCat(m−1)t^m 使该问题化成明确的 algebraic forcing，而非原 rational theorem的免费延用。radius1/4>c，tail argument给第一r−的完整 jump C_Xψ，C_X是显示的正、绝对收敛和。第二conifold的comparison和数值evaluation仍未证，正文准确保留。

Catalan整数、原 ratio cap以及composition x(1−x) 的整数coefficients给 U32。参与 x^n coefficient 的 t-indices≤n，D_m|D_n足够支付；δ multiplier自身整数Taylor coefficients，fixed δ^j依旧只混合较早indices，所以same cap亦成立。这不证明相应 whole-jet rank，正文没有领取该rank。

## V6. 必须保留的局部 jump 与尚未闭合的数值接口

x1的另一 inverse forcing为1−X(t)=1+O(t)。冻结 G3给 \(L[s^9]\Phi=1\)；其最高 \((\log t)^9/9!\) 在constant t项上为1。无constant forcing部分有analytic particular，homogeneous MUM最高log degree仅8，故 U33的 log9不能由路径变化或−u f0删除。它是新增base MUM的真实障碍。

x1/2对应L的ordinary t=1/4。forcing的 fractional部分为 \(z^{1/2}\) 乘analytic，九次ordinary inverse给 \(z^{19/2}\) 乘analytic，无log；z=−(x−1/2)²使该部分analytic。所有homogeneous ordinary solutions亦analytic，因而 apparent point确实可填。这里只填该点，没有把x1与第二conifold也算作已填。

新增 U34 已独立纸核，且本人已在本轮实际读 CDT PDF66–69。x1非零最高log9迫所有 target-admissible φ omit1；reference \(g(z)=\sqrt{1-4z}=1-2\sum_{n\ge1}\mathrm{Cat}_{n-1}z^n\) 为整数Taylor、algebraic holonomic，并与1在Q(z)上线性无关。ψ=φ/4使该 reference pullback在单连通disc holomorphic，全部finite-place费用0。准确 \(J_\psi=J_\varphi-\log4\)、\(\rho_\psi=\rho_\varphi-\log4\)；reference rank2定理于是给 \(J_\varphi\ge2\rho_\varphi-\log4\)。target rank2/cap9为τ=27/4，若derivative gate开启便有ρ>log4；target严格矛盾要求 \(J_\varphi<2\rho_\varphi-2\tau\)，与显示reference lower bound冲突。B的holonomic annihilator \((D_x-1)L_{\mathrm{pb}}\) 正确，因为forcing是x。

multimap同时除4，patched logarithm与double rearrangement均只减log4，全部derivative-gap ratios保持，所以完整numerator K也只减log4。同一个分割、同一组map的比较仍成立，没有只检查largest derivative而遗漏gap项。U34因此严格关闭当前两行/cap9接口，未把它夸成所有新base路线的no-go；scaling已支付，亦未把 \(\mu=-2^{-20}\) 的旧零费用root族移植到此处。

最后 harmonic示例的 ΔμR_H=−2πi/(1−At) 非零，故 particular jump不是原L齐次χ，U25 hypothesis确失效；这只是范围说明，没有隐含新rank或cap宣称。Apéry旁支按冻结T28核为 L_A B_A=6t，其两finite singularities说明一步recurrence split的特殊性，不移植其irrationality。

## V7. 最终判定

**PASS，无进一步修改请求。** 最终 61148507… 的 ordinary全pole/jump兼容、Galois下降、完整C_R有理 splitting、rational projection、actual quadratic-pullback nonsplit校准，以及 U34 current rank2的single/multimap参考门槛均通过独立纸核。§1的R0条件在正式判定前已精确处理。

这个结论只约束指定原L的 rational forcing/projection类，不排除所有周期或normal-function路线。二次模型尚缺 C_X 的ζ/L评价、第二conifold完整comparison、新base MUM处理、有效geometry与另一个实际接口的strict holonomy余量；当前两行/cap9接口的余量则已被U34排除。原ξ=αζ4+βζ5没有被替换；ζ(7)、Catalan或新的数值LI、Lean均未取得。本审阅不引用未来audit、mutable main或任何未来receipt，固定最终候选单向记录。
