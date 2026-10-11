# 配对 primitive gcd 主率的独立实际审阅

日期：2026-10-06。NEW 独审，quarter_actual_rank。独审仅读同行数学稿、源和已经存在的首次证书，没有 execute/import/rerun。以下并非对作者程序重新执行的证明。

## J1. 实际读取、指纹与来源范围

完整实际读取 root `cdt_odd_paired_primitive_gcd_rate_20261006.md` 全文 G1–G13，当前 SHA `77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2`。初读候选 `2e957e5ed23e9761d63f6b9baeed4a02c365417697429734e1bde89351a702fa` 后，作者仅补 G10 的准确来源定位；当前终候选再次全文实际回读，输出无截断。

实际完整静态读取作者自有 NEW 源与首次 JSON：

- `cdt_odd_paired_primitive_gcd_rate_20261006_verify.py`，SHA `a7bbefb04b33cbaf38937e7595d08fbaca1263da24537147dfd2ea7e55fd67f7`。
- `cdt_odd_paired_primitive_gcd_rate_20261006_verify.json`，SHA `9ffb2bbacbddb85987ead5b938cafb488cafe798d301f141ffca3e51d9b46f43`。

实际核全部24个仿射区间、24个 digamma 系数、边界相消字段、512周期和1/513尾的算法。**未另行逐项计算512个积分，未运行程序，未将作者 first execution 改称审阅者的 independent execution。**

同轮已实际全文读冻结 lattice I1–I25、paired analytic R1–R16。审阅者本人 NEW 解析稿是作者工作，不计为独审自己的数学稿。

直接实际阅读 NIST 官方原页面中的 [5.7.6 差级数](https://dlmf.nist.gov/5.7.E6)、[5.4.19 Gauss 公式及0<p<q条件](https://dlmf.nist.gov/5.4.E19)、[27.12.4–5 素数定理](https://dlmf.nist.gov/27.12)。其中27.12给 π(x) 的 PNT；partial summation
θ(x)=π(x)logx−∫₂ˣπ(u)du/u 给稿中 θ(x)∼x。没有称这些网页提供本 gcd 极限的新定理或已全文阅读其引用书籍。

作者已归档对应三个原始HTML，仅读其指纹以定位相同版本：5.7 SHA `e414ff91e957a27eb06cdb7d4e0a8ce72f7359f8dc4d877a4a1c17572d405029`；5.4 SHA `8527350b609826de362b1c2e5818b0a8dc7152cd59a92a2c2788bde153f968fd`；27.12 SHA `12ddbf9698be9a9c6876d728a79c59df8a679ba8ccb4d7a89f7ad5f0ad706a93`。本审阅者没有新增下载、没有 TLS 例外，没有新增 PDF 原页阅读。

## J2. 一般 B 的全尺度极限通过

准确的 binomial factorial denominator 为 (Bn+1)!(m-1)!。核对 G5 两式后，每层 carry确为0/1；min 对两实际整数的 valuation 操作，而非把两个平均值取min。

小prime≤√((B+2)n) 时，valuation层数乘 logp 至多log((B+2)n)，总贡献 ≤nπ(√((B+2)n))log((B+2)n)=o(n²)。对固定δ、p≥δn，去掉 ±1 仅改变 O_B(1+δ^{-1}) 个节点；共同 floor(Bn+1)/p 的例外素数来自 Bn+1，累积误差 ≤nlog(Bn+1)。这两个误差均 o(n²)，不能把 exceptional primes 未付费用。

g_B 在[δ,B+2]由有限仿射区间长度组成，有有限跳点，所以 θ 的加权弱极限可用。√((B+2)n)<p<δn 的 normalized贡献 limsup≤δ，且积分尾≤δ。两尾同时令δ→0给 G3 极限，既无数值拟合也未隐含 uniform in δ 的错误交换。

x>B+1 时 threshold x−B>1，两个 t、2−t 不可能同时越过，故支持上限成立。x>2的 k 区间 (B/k,(B+1)/k)，k1..floor(B/2)，每段三角积分1/(2k)准确，B6给11/12。

## J3. 周期折叠、原函数及24-cell证书通过

u={t/x}、a={6d}、b={2d}、c1−a。第一 carry要求u≥c；若u≤b，第二 fractional remainder b−u≥c，得[c,b−c]。若u>b，则1+b−u≥c，得[max(c,b),min(1,b+a)]。这直接证明 G7 对所有参数而非24个测试点。

t/x 的 q 个完整周期和最后长度d给 g=x(qL+K)。x=1/(q+d) 的 Jacobian使 gdx=(qL+K)/(q+d)³ dd，q0对应x1..2，x>2另为11/12。尾 q>Q 对应0<x<1/(Q+1)，其≤1/(Q+1)是已证全参数尾。

G10 的导数独算：令 u=q+d，N=dL−K，则
F'_q=(l0+k1)/(2u²)+N'/(2u²)−N/u³=L/u²−(dL−K)/u³=(qL+K)/u³。
源的 exact Fraction 原函数、端点差及 outward millionth rounding 与该式一致。24-cell各段由 G7 的 min/max breakpoints 分裂，静态检查源码所有交点枚举、merge及截断K的方向；既有 JSON 的全表与纸面函数一致。512项计算输出只用于主率积分的认证，有限folding cases不代替G7。

## J4. Digamma 闭式通过

每段二阶端点项 (dL−K)/(2(q+d)²) 在普通连续端点相消。d=j/6 reset左L1,Kd，右L=K=0，故两边 dL−K=0；d0、1亦0。因此没有遗漏 trigamma。

每个端点的 ψ(1+d)系数由相邻 (l0+k1)/2 的跳变确定，核 JSON 全部24项后可分四组：

- odd/14 的(1/2,3/2,5/2)及各反射负系数；
- j/7 的 j−7/2，j1..6；
- eighths j/8、(j+4)/8 的 −j，j1..3；
- sixths j/6、(j+3)/6 的4−j，j1..3。

这正是 G12；总系数0，Euler常数消去。用5.7.6绝对收敛差级数接合，其符号正确。q0与x>2的有理项算法为 ∫K(d)/d³+11/12，对应416821/360360；审阅未冒称重新执行512项。Gauss5.4.19与ψ平移可进一步闭式化，但这种继续化简不是G11区间或G3极限成立的前提。

## J5. 与同一格解析率接合，数值范围严格受限

实际 κ_j 分母必须含 (j−1)!²。β_m 对同一mirror pair两项相同，所以 low multilinear term共含Γ_n^{-1}、squared positive envelope共含Γ_n^{-2}。这与审阅者 NEW same-basis解析稿 E2 完全一致，不是从raw basis另除 (6n+1)!。

G3–G11提供γ∈[1.455845,1.457795]，其与 E2 的合法接合为

\[
\limsup_{n\to\infty}n^{-2}\log|D_{A,n}(\xi)|
\le-\beta_H-2\gamma,
\quad\beta_H>8.59403839512558,
\]
\[
\beta_H+2\gamma>11.50572839512558.
\]

只证明这个实际构造的解析上界。没有把同一 primitive gcd算两次，或解释成实际finite-place denominator成本下界、restricted target的非零、严格算术/解析margin、特殊值无理性或Lean定理。

## J6. 审阅结论与执行审计

G1–G13全尺度数学与 source/certificate静态接口通过。数学producer审阅执行0、旧/同行execute/import/rerun0、外部Lean0。本审阅者自己的另外一个常数项目发生failed1+NEW-v2-success1共2次数学执行，原失败源保持并披露；这两次均不执行本 gcd 源，不能混成gcd independent rerun。

当前审阅文件待作者终稿pin确认后冻结，不修改任何旧冻结稿。无限unit、实际全素数预算和新的特殊值结论各自仍有缺口。
