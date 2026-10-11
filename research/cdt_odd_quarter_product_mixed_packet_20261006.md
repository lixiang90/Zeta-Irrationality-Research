# 互补 quarter 的混合全前缀包及更短的第二层关系

日期：2026-10-06。NEW 全尺度证明；实际只读 [互补稿](cdt_odd_complementary_quarter_period_product_20261006.md)、[19行接口](cdt_odd_quarter_product_rank19_interface_20261006.md)、冻结 [J 模型](cdt_odd_quarter_shift_full_model_20261006.md)、[旧 Smith 稿](cdt_odd_quarter_shift_smith_20261006.md) 和 [balanced 桥](cdt_odd_level20_balanced_smith_bridge_20261006.md)。未执行或 import 旧、同行数学 producer。

本文有一个无条件的 CDT 输入改进：实际 rank5 的 J 源第二层关系的次数从旧 3d 降到 2d，得到普通 metric 可认证费用上界 188/25。另给 Γ-free 乘积的19行原模型真实混合 relations；其 determinant/CDT 部分以19行独立为明确条件，不把 derivation-closed 上界当实际秩。没有新数值无理性定理。

## 1. 共用的 fast/slow 包：保留完整实际 forcing

沿用 A、J、F=A−1/2，shifted rows
\[
F_i=(\theta-1/4)^iF,\qquad J_i=(\theta+1/4)^iJ,
\quad S_{ij}=(F_iJ_j+F_jJ_i)/2\quad(0\le i\le j\le3).
\tag{P1}
\]
它们与常数1构成原19行有理模型。固定 odd prime p 和整个所需前缀 n<N，要求
\[
p^2>4N+1,\qquad d=(p-1)/2.\tag{P2}
\]
split p≡1(4) 时坏源是 J、好源是 F，h=(p−1)/4；inert p≡3(4) 时坏源是 F、好源是 J，h=(p+1)/4。P2 内好源全部 shifted rows p-integral，坏源用 p⁴ 清全部前缀。F 的 constant correction −1/2 在 p⁴F 模 p² 中为零，不改变坏源 packet，却没有从真实系统中删掉 forcing。

两类素数的坏带都是 h≤n mod p≤h+d。split 的准确比值已在旧稿 S2 证明；inert 由 A 的实际系数在 n₀=h+kp 直接给同一个比值
\[
\frac{a_{n_0+j}}{a_{n_0}}
=\left[\frac{(1/2+p(k+1/4))_j}{(1+p(k+1/4))_j}\right]^4,
\quad 0\le j\le d.\tag{P3}
\]
各因子 p-unit，带外 p⁴坏源的系数被 p⁴ 整除。定义
\[
T=\sum_{j=0}^{d}\left[\frac{(1/2)_j}{j!}\right]^4x^j,
\quad V=\left.\partial_\rho\sum_{j=0}^{d}
\left[\frac{(1/2+\rho)_j}{(1+\rho)_j}\right]^4x^j\right|_{\rho=0},
\]
\[
e_i=\theta^iT,\qquad d_0=V,\quad d_i=\theta^iV+i\theta^{i-1}T\ (i\ge1).
\tag{P4}
\]
T、V、eᵢ、dᵢ∈Z_(p)[x]，次数≤d；T₀=1、V₀=0，T_d 是 p-unit。

以实际带首项 w_k=p⁴j_(h+kp) 或 p⁴a_(h+kp) 定义所需 W(s)，s=xᵖ、Z=(θ_s+1/4)W。任意延拓前缀外 W 无关本结论。设 B_i 表示坏源的 shifted rows、U_i=p⁴B_i。注意两类都满足 h±1/4=p/4（split 用+，inert 用−）；对旧 scalar packet 作有限 binomial 展开，得到实际四行 packet
\[
\boxed{U_i\equiv x^h\{e_iW+p d_iZ\}\pmod{p^2,x^N},\quad0\le i\le3.}\tag{P5}
\]
确切说，shifted θ 在 x^hT(x)W(xᵖ) 上是 fast θ 加 p(θ_s+1/4)；一阶 p 项是 iθ^(i−1)TZ，正是 P4 中额外的一项。未将慢变量误当常数，也未只核一个长度 p block。

## 2. 纯坏源的更短第二层及真实嵌套阈值

用 εᵢ 表示四行坐标向量，定义三个 first vectors
\[
m_i=T\varepsilon_i-e_i\varepsilon_0,\quad i=1,2,3.
\tag{P6}
\]
mᵢ·U=0 mod(p,xᴺ)，每个 source coefficient 次数≤d。

置
\[
Q_T=T d_1-e_1V=T^2+T\theta V-V\theta T,
\quad C_i=e_i d_1-d_i e_1,
\quad D_i=T d_i-Ve_i\quad(i=2,3),
\]
\[
r_i=Q_T\varepsilon_i-C_i\varepsilon_0-D_i\varepsilon_1.
\tag{P7}
\]
直接相消给 rᵢ·e=rᵢ·d=0，因而
\[
\boxed{r_i\cdot U\equiv0\pmod{p^2,x^N},\quad i=2,3.}\tag{P8}
\]
所有 coefficients 次数≤2d，较旧稿 second operator 的3d少一整份 d。最高 x^(2d) 项为 Q_T 的 T_d²；B=TθV−VθT 的最高项相消。故 deg Q_T=2d，top 是 p-unit，且 Q_T(0)=1。

在 polynomial source degree≤D 内，乘 degree≤D−d 的任意整多项式，三个 mᵢ 按最高 row index 3、2、1 依次比较，modp primitive rank 为
\[
k_1^{B}=3(D-d+1)_+.
\]
同理 r₂、r₃ 乘 degree≤D−2d 的多项式，最高 row 2、3 coefficient Q_T 给 modp primitive rank
\[
\boxed{k_2^{B}=2(D-2d+1)_+.}\tag{P9}
\]
这里 primitive 是原有限 coefficient 格在 DVR 上的 primitive submodule：模 p 的向量独立意味着 span 是 direct summand，并非对 polynomial ring 作未经证实的可逆换基。

阈值的嵌套应在真实评价格中解释。对整 evaluation matrix A_D，令
\[
\mathcal K_\ell=\{v:A_Dv\in p^\ell O^R\},\qquad
L_\ell=\operatorname{image}(\mathcal K_\ell\longrightarrow E_D/pE_D).
\tag{P10}
\]
L₂⊂L₁，SNF 给 dim L_ℓ=#{a_j≥ℓ}。P6、P8 的 primitive span 分别包含于 L₁、L₂；因此可以累加两个不同阈值的 lower bounds。**没有**把两个 second families 当成 first kernel 之外的两个新独立普通 kernel。虽有 T rᵢ=Q_Tmᵢ−Dᵢm₁，本文也不据此声称有限 degree 内可除掉 T；实际 L_ℓ 的嵌套不依赖这种除法。

对实际 rank5 J 的原格 {1,J,θJ,θ²J,θ³J}，P1 的 shifted basis 到 Euler basis 是固定 upper triangular、diagonal1 的变换，在所有 odd places 整且可逆。因此这些 relations 和 primitive counts 直接属于**同一原格**。实际 leading rows V_D⊂[0,5(D+1)+O(1))；取 p⁴eval_(V_D)。constant 的 D+1 directions image⊂p⁴，其它 four rows 用安全 p⁴。cap4 Smith floors满足
\[
\boxed{\sum_j\beta_j\ge4(D+1)+3(D-d+1)_++2(D-2d+1)_+.}\tag{P11}
\]
三四层只有原 constant baseline，未认证更高 crédito。

## 3. 无条件接入实际 rank5 的 CDT 费用

全部地方仍使用旧稿 §§4–5 的完整 denominator 表：split 四列 restricted Δ⁺_(⌊bn⌋)，b=4+ε；inert 高幂、split 高幂仅 O(√N log²N) 的统一 prefix log，给 o(D²)；native J 全部 Taylor coefficients 在2处是 units。本证明始终可把 shifted relations 转回原 Euler 行，不新增2处分母主项。如果改用 shifted global source，固定4^(−i)所带 index/norm 也仅 O(D)，归一后为小项。

原 split 最大 transport 为 M_b(t)=4min(4/5,(1−t/b)_+)，density1/2 后 τ=48b/25。P11 的 first 支持 p≤2D+O(1)、second 支持 p≤D+O(1)，均在原 all-active matching 内。该窗口原 cap 是16/5，pure p⁴ matrix baseline 4−4/5也为16/5；因此与原费用兼容，可扣真实 determinant credit。

冻结 balanced 桥的 saturated restriction 引理采用同一 cap4，restriction 损失≤4dc，near-balanced leading rows仍来自 V_D^d。严格内窗、固定 ε/tensor dimension 后 D→∞，再取 tensor/tolerance极限和 margin↓0。小素数 p²≤4N_D+1删掉的信用是 o(D²)。AP-PNT 给
\[
\gamma_J=\tfrac12\left[3\int_0^2(1-t/2)dt+
2\int_0^1(1-t)dt\right]=2.
\]
有限高度归一信用是 γ_J/5，CDT HS/arch 原归一的费用信用为2γ_J/5²=4/25。因此
\[
\boxed{\kappa_{J,\varepsilon}=\frac{48(4+\varepsilon)}{25}-\frac4{25},
\qquad\lim_{\varepsilon\downarrow0}\kappa_{J,\varepsilon}=\frac{188}{25}.}\tag{P12}
\]
这是本轮无条件、同一实际 rank5 输入的改进上界，未修改冻结旧113/15稿，也不声称最优。已有合法 omit1/unique0 native λ-leaf 容量≤log16，故 P12 仍不能产生 CDT 数值矛盾。

## 4. 19行的真实混合第一、第二层

令 G_i 为好源 shifted rows，\(\mathscr S_{ij}=p^4S_{ij}=(G_iU_j+G_jU_i)/2\)。P5 给
\[
\mathscr S\equiv \tfrac{x^h}{2}
\{W(Ge^t+eG^t)+pZ(Gd^t+dG^t)\}\pmod{p^2,x^N}.
\tag{P13}
\]
G 全 prefix integral；没有假设它是常数或 fast polynomial。对任何 i,j∈{1,2,3}，
\[
m_i^t\mathscr S m_j\equiv0\pmod{p,x^N}.
\tag{P14}
\]
展开是 T²𝒮ᵢⱼ−Teⱼ𝒮ᵢ₀−Teᵢ𝒮₀ⱼ+eᵢeⱼ𝒮₀₀，source degree≤2d。六个 i≤j families 的独有最高 target coordinates Sᵢⱼ (i,j≥1) 系数T²给 primitive rank
\[
k_1^{S}=6(D-2d+1)_+.
\]
同理 i,j∈{2,3} 时
\[
\boxed{r_i^t\mathscr S r_j\equiv0\pmod{p^2,x^N},}\tag{P15}
\]
所有 coefficients degree≤4d，三个 i≤j families 的独有 Sᵢⱼ (i,j≥2) 系数Q_T² 给 primitive rank
\[
k_2^{S}=3(D-4d+1)_+.
\]
pure bad、Sym、constant/good三种 supports 分开，故各阈值的 primitive ranks 可相加。P10 的 actual L₂⊂L₁仍保证嵌套；没有把两层各自在同一个 modp kernel 中相加。对于原19列源的任何可逆 leading square evaluation，p⁴ scaling 的 certified cap4 floors 因而满足
\[
\boxed{\sum_j\beta_j\ge20(D+1)+
3(D-d+1)_++8(D-2d+1)_++3(D-4d+1)_+.}\tag{P16}
\]
baseline20=4×5来自常数与四 good rows；其 image⊂p⁴。这里 formal19源的 primitive relations 无条件成立，P16 的可逆19(D+1)评价及接下来的 m=19 CDT 结论明确要求19个实际函数独立。若实际秩较低，须选真正独立格并重新转移 counts，不能沿用19作结论。

## 5. 全部高幂与条件费用的精确接合

互补稿给精确 D_A(N)、D_J(N)。事实上其乘积恰为
\[
\boxed{D_A(N)D_J(N)=\operatorname{odd}(\operatorname{lcm}(1,\ldots,4N+1))^4.}\tag{P17}
\]
N=0单独为空积。split p 的 A 无分母、J exponent4⌊log_p(4N+1)⌋。inert 令 b⁻=⌊log_p(4N−1)⌋、b⁺=⌊log_p(4N+1)⌋，其和为4[⌈b⁻/2⌉+⌊b⁺/2⌋]。两 b 相等时和为4b⁺；若相差1，唯一跨过的 odd p-power 必为4N+1≡1(4)，所以该 power 的指数 b⁺是偶数，仍得到4b⁺。无其它情况。

因此 Sym10行的 shifted/sym 固定 dyadic 因子之外，只要四个 full-density LCM columns，毋须八列。各 prime class 的主要 denominator 数组都是：constant加四个 good rows 五 species费用0；bad4加Sym10十四 species各四个 b=4+ε columns。其它地方：A/J非该class的高幂亏损、所有 j≥2 层、有限初值和固定2-power均按完整 prefix计为 o(D²)，不删除 inert 高幂。对于 symmetric rows，P17 已逐素数清全部高幂。

条件 m=19 下，per-class 最大 transport 是
\[
M_b(t)=4\min(14/19,(1-t/b)_+),
\quad\tau=2\int_0^bM_b(t)dt=\frac{1344b}{361}.\tag{P18}
\]
两 class各密度1/2且同一个最大值，故总leading值仍为P18。各class可各自采取其允许的 transport maximum；没有以一个 comonotone 下界替代 maximum。split/inert零费species不同并不妨碍逐place的上界。

每class有五零行，all-active匹配窗口至少 p≤5bD；更小 p≤2D 已覆盖P16全部 credit。此时原 cap=56/19，而原 p⁴ scaling baseline 4−20/19=56/19完全一致。cap4 near-balanced restriction和严格内窗接合沿原桥不变；使用每class实际 packet，AP prime sums和密度相加为
\[
\gamma_{19}=3\int_0^2(1-t/2)dt+
8\int_0^1(1-t)dt+
3\int_0^{1/2}(1-2t)dt=\frac{31}{4}.
\]
故在19行实际独立、full leading flag N_D=19(D+1)+O(1)及已有合法共同叶条件下，普通metric的可认证 finite cost 为
\[
\boxed{\kappa_{19,\varepsilon}=\frac{1344(4+\varepsilon)}{361}-\frac{31}{722},
\qquad\lim\kappa_{19,\varepsilon}=\frac{10721}{722}.}\tag{P19}
\]
P19 仍大于14，没有 CDT 数值矛盾，也不是实际19秩的证明。本文的目标增益是完整 mixed source 的 primitive Smith interfaces 及无条件 P12；真实 Γ-free 临界值的无理性仍未证明。

## 6. 新有限核验和范围

新 [verify.py](cdt_odd_quarter_product_mixed_packet_20261006_verify.py) 只用 Python 标准库，第一次单次执行通过52项精确 checks。实际 p,N pairs为 (5,5),(13,40),(17,70),(3,1),(7,11),(11,29),(19,89)，全满足P2；包括多block真实A/J coefficients、四 shifted rows P5、exact second annihilators、pure first/second、六个 mixed first和三个 mixed second identities，以及N=0..64实际最小分母乘积P17。新 [JSON](cdt_odd_quarter_product_mixed_packet_20261006_verify.json)记录此首次通过执行历史。未执行旧或peer producer，未核数值L值或实际rank19，有限check不能代替本稿全prime证明。

本文待root实际独审；冻结旧数据不变。本稿没有Lean形式化声明，也没有数值无理性或线性无关性主定理。
