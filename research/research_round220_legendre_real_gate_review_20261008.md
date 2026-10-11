# 第220轮 Legendre 实处与全局 gate：独立 FULL 审阅收据

日期：2026-10-08。审阅者：round218_dual_audit。目标稿作者是另一 agent；本收据不修改目标稿、旧稿、main 或 manifest。

**结论：PASS（限目标稿实际主张）。** 新零估计、enlarged cutoff 的同源有限成本、Taylor 子式分母和实处增长界，以及 univalent / 已付 multivalent 的范围，均通过有限纸面核验。目标稿没有证明新的无理性结论；固定三行没有因假设 \(G\in\mathbb Q\) 自动获得可穿越目标 cusp 的新函数。没有必要数学修正。

## 1. 确切身份与实际阅读

目标：[legendre_real_place_global_gate_round220_20261008.md](legendre_real_place_global_gate_round220_20261008.md)。实际保存文件：**17769 bytes**，SHA256：

`e34d4429485289ccb5c2ad7dc827c2353829e8d9ed9276e483e9521b89b364f2`

本 agent 对此身份进行了实际 **FULL** 读取：标题、日期、全部7节、R1–R24、表格、链接与执行账本；输出未截断。审阅覆盖全部数学结论，而非只读摘要。输入连接稿已在 round219 对最终身份 FULL 独审，整格稿在本轮策略审查中 FULL 阅读后用于本次接口核验：

|冻结输入|Bytes|SHA256|阅读角色|
|---|---:|---|---|
|eisenstein_legendre_catalan_connection_round219_20261008.md|13940|67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39|既有最终 FULL 独审；实际 branch/endpoint 接口复用|
|eisenstein_legendre_integral_flags_round219_20261008.md|15599|bc41296fb85c5548adae93d25cde5f9e4983f5d223ada8e6a39cd1b87b765730|本轮已 FULL 阅读；A17 两种满射条件与全源 fallback 核验|

未把本 agent 的高权稿作者读当作独审。目标稿提及 root 的 relation-obstruction 稿，本次不声称另对该稿 FULL 独审；目标 R9–R14 和 R24 在本收据按实际方程及冻结输入独立核验。

## 2. R5–R11：增长和完整 log 系数

R5 的正系数式与冻结公式一致。由 \(nc_n\) 的逐项比值 \(1+1/[4n(n+1)]\)，下界 \(1/4\) 与上界 \(e^{1/4}/4\) 正确。把 \(c_j\) 两侧界逐项放入 R5 得 R6；无需渐近拟合。故 \(16^nu_n\) 的指数率为16，\(\mathcal U,\mathcal V\) 的实际收敛半径为1/16。R7–R8 的正系数 Cauchy 界和 \(r_D=(1-1/D)/16\) 的 \(\log M(r_D)=O(\log D)\) 正确。

G-function 身份由具体系数指数界、全前缀公共分母 \(d_n^2\) 和有理 holonomic 系统给出；未使用 G-function classification 代替具体分母证明，也未从此身份推出数值 \(G\) 无理。

对 \(y=1-x,\ell=\log(16/y)\) 独立微分核验 R10：\(L_y(A\ell^2)\) 的 \(\ell\) 系数为 \(-4(1-y)A'+2A\)，常数项为 \(2(1-y)A/y\)；\(L_y(B_1\ell)\) 的常数项为 \(-2(1-y)B_1'+B_1\)。因此 R10 的两条非齐次式及符号准确。\(A=f/32\) 令最后一式的 \(1/y\) 项消失；指定 \(B_1(0),C(0)\) 后解析递推收敛，并与实际 U 的误差趋零。齐次局部解一项常数、一项一次 log，故差为零。这个步骤支付的是完整 \(f(y)/32\) 系数，不能降成仅 leading \(1/32\)。

逆时针绕1给 \(\ell\mapsto\ell-2\pi i\)，从而 \(\Delta^2U=-\pi^2B/4\)。对 \(aU+b\theta U+c/(1-x)\) 的 R11 也正确。\(B'/B\notin\mathbb C(x)\) 的证书成立：实际 \(xB'/B\to0\)，但 \(B'/B\) 无界；有理函数在0若有极点，前一极限不可能为零，否则它在0有界。

## 3. R12–R14：零估计不存在秩循环

R12 从 \(\delta=(1-16u)\theta_u\) 与实际 inhomogeneous Legendre 方程得到；三行分别为 \((1-16u)\mathcal V\)、\(4u\mathcal U+16u\mathcal V+u\mathcal W\)、\(16u\mathcal W\)。矩阵和次数均正确。

若 \(r_0,r_1,r_2\) 相关：当 \(r_0,r_1\) 已相关时，其一维 span 在连接作用下稳定；否则 \(r_2\) 在前二行 span 中，该二维 span 同样稳定。因此先得到的是 row module 秩至多2及 R 的阶数至多2标量方程，**没有先假定目标 Taylor 矩阵已有秩3**。有理系数在局部绕1单值，故 \(R,\Delta R,\Delta^2R\) 都是该方程的解。R11 的非零系数给三者分别具有二、一、零的最高 log 次数，故 C-独立，与二阶方程矛盾。这证明 \(\det S\ne0\)，不依赖 \(G\) 是否无理。

\(\deg r_j\le D+j\) 给 \(\deg\det S\le3D+3\)。\(Q\) 在0有简单零，所以 \(\delta^jR\) 的零阶不低于 R。adjugate 的系数为多项式，加上 \(\mathcal W(0)=1\)，得到 \(\operatorname{ord}_0R\le\operatorname{ord}_0\det S\le3D+3\)。纯第三行的界为D。R14 对完整复多项式源成立。

因此 E3D 的核维数介于2与3：尺寸给下界；R14 使其核单射到最后三个 coefficients，给上界。原 cutoff 的秩只被限定在3D至3D+1，未夸成完整列秩。新 \(N^*=3D+3\) 的全系数 jet 单射，确有非零 \((3D+3)\) 阶子式；它是 Taylor 子式，尚不是目标周期的数值非零证书。

## 4. R15–R20：全部 p、一次 index 分母及同源实处

在 \(N^*/2<p\le N^*\) 的新奇素数窗口：\(p\ge2D+3\) 给 \(D\ge N^*-p\)，满足冻结 A17 的第一分支；否则奇数 p 至多2D+1，\(h\le D\)，而 \(p>(3D+3)/2\ge(4D+7)/3\)（D≥6）给 \(N^*-p\le D+h\)，满足第二分支的全部条件。因窗口内 \(p^2>N^*\)，exact local exponent 为 \(2(N^*-p+1)\)。

fallback 并未漏掉窗口外：两个非整行的每列可用 \(d_{N^*}^2\)，所有小素数与高素数幂仍被其 valuations 控制；2仍整；\(p>N^*\) 整。fallback 主项12，窗口相对节省 \(2p-2D-4\)，加权 PNT 的主项为15/4，故新完整 cutoff 的成本仍为33/4。没有从旧 N statement 未经核验直接改 cutoff。

若 J 为全源 integral-jet lattice 的整数基，\(|\det J|=I\) 而 E J 整：Jacobi complement identity 使 \(J^{-1}\) 的任意阶子式分母整除 I；Cauchy–Binet 给 E 的任意子式属于 \(I^{-1}\mathbb Z\)。故 R16 只支付 I **一次**。此证明无需 E 先有完整秩；R14 单独支付新最大子式非零，二者没有互相循环。

R17 的 row/column grading 与 Hadamard 正确。旧 s=3D+1 的精确 exponent 为 \(3D^2+k_1+k_2\)；s=3D 仍为 \(3D^2+O(D)\)。新 cutoff 使用所有3D+3列、删第j行，精确为 \(3D^2+9D+6-j\)。取 \(r_D\) 得实处 **正增长** \(3\log16\,D^2+O(D\log D)\)，与有限处下界 \(-33D^2/4-o(D^2)\) 没有矛盾，也不构成严格小量。

R20 的 \(16^{n-k}\) scaling 对三行皆成立。改 x/u 坐标必须同时改变 source basis、jet basis 和有限格；保留 u 的2整性、借 x 的16导数会混对象。指数33/4不是 CDT 系数类型参数 \(\tau=16/9\)，目标稿明确区分了它们。

## 5. R21–R24：admissible 范围和目标状态

排序 \((\mathcal W,\mathcal U,\mathcal V)\) 后两列 staircase 均为 \((0,1,1)\)，合法类型给 \(\tau=16/9\)。R11 也支付 C(u)-独立性。有理 Betti/Hodge 包没有被误写为 direct theorem 先决条件。

R22 的缩放 Koebe map 对应 \(\mathbb C\setminus[1/16,\infty)\)，导数1/4正确；rescaled closed-disc 图导数s/4，univalent 的两重对数能量确为 \(\log(s/4)\)。对所有 **univalent** actual admissible maps，Koebe disk inclusion 与不可 meromorphic 的目标 cusp 给导数≤1/4；这是该范围的上限。

R23 已付 theta/Lambert 图是不同的 multivalent 家族。其 \(\psi_s'(0)=s\)，\(\mathcal U\) 拉回为 \(FK\)；\(\mathcal V\) 拉回可写为 \(\Theta(FK)/[(1-\Lambda)F^2]\)，分母在 q-disk 非零，0点可去；第三行也全纯。s<1 使各对象在闭圆盘邻域有定义。但 \(\log s<0\) 不过 \(16/9\) 阈值。目标稿未把1宣称为所有 multivalent maps 的最优上限，未为未知图借用能量，因此范围诚实。

R24 的 \(G=g\) 只取消一次 log；完整二次 log 系数仍为 \(f/32\)。三行 C(x)-span 在1单值 meromorphic 的部分恰为第三有理行：\(\Delta^2=0\) 强迫 \(aB+bxB'=0\)，再用 \(B'/B\) 非有理得 a=b=0。有限 ramification 只把 log monodromy 乘k、二次差分乘 \(k^2\)，不能消去这项。此结论只约束当前三行，不排除新 companion、载体或其他数值方法。

## 6. 引文核验、执行账本与最终范围

本次实际 primary 选读：既已完整读取的 CDT fixed v2 Theorem2.5.1 / fine-type 输入及完整 Theorem7.0.1；另打开并读取 [arXiv2510.04156v1 Theorem2.1、Remark2.2](https://arxiv.org/html/2510.04156v1#S2.SS1)，核 holonomic/meromorphic/positive denominator 假设；[Fischler–Rivoal 1606.00706](https://arxiv.org/pdf/1606.00706) 第1页定义(i)–(iii)；[McMullen 官方课程笔记](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/10/html/home/course/course.pdf) printed page64（工具 zero-based P64）的完整 Theorem4.20 及证明。均为必要选目，不声称 FULL 全文。引用与目标稿陈述一致。

数学程序0；CAS/symbolic0；矩阵执行0；prime/parameter grid0；PSLQ0；Lean0；数值积分0；Git0。实际工具仅 documentary FULL 读取、metadata/SHA256、既引用 primary 选目网页读取及本 NEW 收据保存/作者复读。全部 R1–R24 的本次核验为有限纸面推导。

PASS 的界限：R14/R15 是可复用的非零 Taylor / 有限格技术资产，R18 是增长界；没有目标数值小量、完整目标评价 certificate 或新的无理性 theorem。独审不把“当前三行不能穿 cusp”扩大成所有 Legendre/modular/cyclotomic 载体的 no-go。目标稿无必要修正；本收据 final saved 作者 FULL 阅读及 hash 外部登记，目标身份再次核对后 handoff。
