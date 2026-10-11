# 独立全文审查：Level 7 rational-pole Stieltjes 周期族

日期：2026-10-07。审阅者：`/root/source_pencil_finalize`。唯一受审主稿：`research/cdt_odd_level7_rational_pole_stieltjes_family_20261007.md`，SHA256 **`c7782adfca5d00fb6c53bcccc903240caa9baf2e006e8656a4415b2ec3b9f5de`**，**14378 bytes**。已实际全文读完 P1–P24、全部8节；以下是独立纸面复核，不是读取作者结论后重复 PASS，也没有数学 producer／prime／guard／Lean 执行。

结论：**PASS，无修改请求**。主稿给出真实全素数 cap、全部 ordinary-jump 分支、实际函数 rank 和正矩递推；没有把它们冒充新的数值 LI 或把 Taylor cap 移给递推系数。

## V1. 输入与 same-object normalization

本轮 fresh FULL 读入冻结 `cdt_odd_level7_polynomial_extension_classes_20261007.md` E1–E29/8节（fc585a055e3b577a862f58202e24eda099394ae1b62e5f33393fb2b868690e7c），其正式独审 a1aebf1f810e933147d5ce964e5177402146f2954dfd35aa8e4caf51b624db77，及冻结 `cdt_odd_level7_kummer_relative_classification_20261007.md` K1–K27/8节（bec6b922b3fabd9e424c88329c8111bf3656f4da2c23faff9fadbfb197dd1148）。authority 7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a 的 current progress、620/615/5 与物理 SHA 已核；mutable main 仅 header 和 §§201–205，本 review 不 pin 它。

与 Yang fixed v1 PDF5–6/15–16 本轮 actual FULL 读域对照，受审 `L,r_B,A,f,t,S` 恰为同一模型。P4 中 `R_aS²/(pA)=f/(1+at)` 的 p 因子确实保留，不误把 L 当 monic。P7 的 Fricke affine correction使用冻结稿同一 cusp-primitive normalization；这里只有轴及邻域无 pole，不假称 f_a 全球 holomorphic。

## V2. 全素数 cap 与完整 σ 连接

对整数 a≥1，`1+at(q)`、p(t(q))、A(q) 都是整数 Taylor units；因此 f_a 是整数 q-series。B_a 的 q-coefficient来自整数乘法和 `1/j²`，composition q(t) 的每个 index n 只使用 j≤n，遂 D_n² 消掉所有分母；乘 n^j 的 fixed θ-jet不增加分母。此处为 all n/all primes/powers，没有“辅助 unit-prime”假设。

Fricke交换两个 cusp，固定 t；归一化 E_a、E_a′在∞为零，P6 的常数正是 affine correction常数。P7给 `B_a−C_aA` 在 order-2 fixed point invariant，所以它下降为 σ 附近完整 analytic t-germ。该结论沿已指定正轴 access；主稿保留所有 transported accesses 的额外要求。若改成复杂 u，函数 rank 的结论仍成立，但 Q-Taylor及同 cap 的条件只有 u∈Q、固定 rational multiplier 已支付时成立；主稿没有据 complex u 付算术费。

CDT 固定原件本轮实际 FULL PDF66–69：两 identical width-1、slope-1列，首行0，后面 row sum2；u_j=1，e=0。公式6.0.4直接给 `τ=2−2/m²`，m=2k+1，单解 m=3 为16/9。不是仅拿 slope2 重写而漏掉 row-array 形状，也没有声称已具备 strict geometric margin。

## V3. 每个新增 ordinary 点的所有 branches

独算 µ=−1/a：`Res R_a=−(a+1)/a³`，`p₂(µ)=(a+1)²(a+28)/a⁵`，其比值恰为 `γ_a=−a²/((a+1)(a+28))`。令 v_µ(µ)=0、v_µ′(µ)=1，则 P10 的交换子式逐项正确：二阶导贡献 `2p₂v′/s−p₂v/s²`，一阶导贡献 `p₁v/s`；残留 simple-pole 系数是 p₂(µ)，其余 holomorphic。

因此减去 γ_av_µlog s 后是 ordinary analytic particular，且任何其它 branch只差 analytic homogeneous solution。P11 的 coefficient与 full jump不能因 branch改变或减 uA 改变。有限 cover得到 s^klog s，仍不是 meromorphic。原1/∞的 forcing分别 analytic、`z³R_a=O(z²)`，不会触发新增∞0-exponent resonance；这与 B₃的原 infinity log形成真正区别。

ordinary rational T 若有 pole order k，其 LT最高 pole order k+2不能降为 simple pole；若无 pole則LT analytic。因此 P12 对 C(t) 也成立，足以应用 frozen K1 的旧域分类（包括 a=28 与旧 Kummer同 µ 的情形）。没有把 ordinary jump的 rational 2πi 标量误认为任意 complex period。

## V4. actual joint rank 及量词

µ_i loop在其它 affine systems都是 ordinary local identity；所有 branches差 homogeneous，在 µ_i同样 analytic，所以 conjugating该 based loop仍只平移第 i 解。对第 i 的 nonzero translation取 homogeneous monodromy conjugates，irreducibility使其 span等于完整 V。

若 P13 存在 C(t)-relation，取这些 loop differences得 `c_i v+d_i θv=0` 对全部 v∈V。两个 homogeneous solutions的 Wronskian非零，故 c_i=d_i=0，再 c₀=0。P14的 m=2k+1因此是实际 scalar-function rank；不是 matrix rank或数值 period rank。取 k=1、减 uA 时同 ordinary loop证 rank3，不能从“假设 C_a rational 填 σ”错误降到 rank2。

## V5. 正测度、前两 moments 与校准点

ν是固定正 measure 的真正 pushforward；f(iy)>0、0<t≤σ给 finite massκ，内部interval正质量、无 endpoint atoms。P16–17 dominated differentiation与严格 inequalities均正确。给出 `M_n∈Q+Qκ+QC₃` 的方法是 polynomialforcing exact quotient及 normalized connection coefficient `bκ+cC₃−T(0)`，包括实际 T(0)；不是从数值拟合得到。

独核：

- `t²−t³=−r_B/3−t³+L(−1/6)`，所以 M₁=1/6−κ/3−C₃。
- `t³−t⁴=−(8/21)r_B−(13/14)t³+L(t/42−5/28)`，四个 monomial coefficients逐项一致，给 M₂=5/28−8κ/21−13C₃/14。
- `t=(2/3)r_B+L(−1/6)`，normalized solution必须加 A/6，因此 C(−1)=2κ/3+1/6。

这些均为实际 full connection常数，没有把 cohomological exact项的 endpoint漏掉。

## V6. exact J-recurrence、局部密度与非退化

直接纸面展开
`L(tⁿ)=n²tⁿ−(30n²+14n+2)tⁿ⁺¹+(57n²+28n−4)tⁿ⁺²−14n(2n+1)tⁿ⁺³`。
除 r_B 后各 Mellin项恰为 J_n,…,J_{n+3}；n≥1 的 polynomial solution T=tⁿ有 T(0)=0、零 σ coefficient，遂 P22 all n恒等。J₁/J₂/J₃ 与 M_n=J_{n+1}−J_{n+2} 的 index也一致。P22的 n=1 还独立恢复 M₂公式。

P23的 endpoint exponent经过单独核验：σ的真实 elliptic order为2，τ_c=i/√7，t的 local ramification恰为2而非更高；imaginary axis的 t有严格最大σ。故 `σ−t(iy)=c(y−y_c)²+O((y−y_c)³)`、c>0。原 measure density `4π²y f(iy)` 在 y_c严格正且 analytic，两个 local inverse branches的 `|dy/dx|` 均贡献 positive `(σ−x)^−1/2`；合计常数非零。离此 endpoint的部分指数更小。令 u=(σ−x)/σ 作局部 Laplace代换，得 `J_n∼c_*σ^(n−1)n^−1/2`，c_*>0；未声称该常数 algebraic。

由实 polynomial不可能在 support的所有 openinterval vanish，`∫P²dν>0`，所以全阶 moment Hankel positive definite。此为真实 Hermite–Padé nondegeneracy；不等于 1,κ,C₃的数值 Q-LI。

## V7. 通过范围及本轮证据

主稿严格留下了 recurrence coefficient的全素数 lattice、增长与非零性下界，以及新增 µ 全jump对可用 maps的真实费用。其 D_n²为 B_a Taylor rows 的 cap，未移给 P22 的 rational recurrence division；故没有根据 analytic recessive solution和正 Hankel就宣布 irrationality。本文同样不证明任何新 period数值 theorem。

本审阅者本轮 primary 实际页域：Yang5–6、15–16共4页；CDT66–69共4页（此四页为本 review新增读域）；本人主稿另读 GZ9–10与 BF13、15–17、26、29–30、33–39。合并个人本轮为 **24 distinct PDF页**。本人已渲染目读BF13/34/36/39，但不是 root本稿所需新增原件；没有新下载。没有继承作者或同行的 primary reading，不把过去一轮读域算作本轮。

此 review已 actual FULL 作者自读后才能给最终 SHA。后续单向 receipt可以 pin上述 stable主稿、本review与 frozen inputs/primary，不能 pin mutable进展总稿、同行receipt或未来audit。
