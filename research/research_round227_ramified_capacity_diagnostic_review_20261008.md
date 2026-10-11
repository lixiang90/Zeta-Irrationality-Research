# 第227轮 C 分歧叶与容量诊断：独立完整审查

2026-10-08。独审者 A；不是 C 的作者自读，也不以 Root 的审查替代本次纸面核验。结论：**PASS，未发现必要数学修正。** 通过的是文中限定的量词反例、指定图的能量与分母计算、两条 conditional 几何界；没有通过原 Padé 包的全图失败或正收益准入。

## 1. 最终身份与实际阅读

| 实际完整读取对象 | bytes | SHA256 |
|---|---:|---|
| research/pade_ramified_leaf_capacity_diagnostic_round227_20261008.md | 11815 | 458f934a825ac213cafbd47943f8825119f973876759929497ad3b61405ee15b |
| literature/pade_ramified_capacity_sources_round227_20261008/dual_reading_scope.md | 6691 | 496cd0e08080a25120618895d8ae6d17175628e3f1274b0f1d4e7ceb066ce613 |

本次实际 FULL 阅读主稿六节 N1–N15、全部公式与 scope 四节。另实际完整读取三份 selected primary 文本：

- McMullen 作者书 PDF182–188（印刷177–183），TXT 14412 B，SHA256 f3db898a9003f862fb829a250b8532890339fc1af334bd7affa3cf16fe982e8c；全部 §A.1、§A.2、Theorem A.1/A.2/A.3 及相关定义、证明、曲率归一，末页 §A.3 开头亦已读取。
- 冻结 CDT PDF23–25，TXT 11736 B，SHA256 e1b6c1ff784f0caa4940d04b7e9570a18e246b346f4e5558e54c0c7a98c51683；完整三页，包括 §2.8 的唯一零点、omit 1 和界16条件。
- 冻结 CDT PDF26–27，TXT 8259 B，SHA256 e15f6f9849a746c2cb5dcbdc44843a5c7ba4dab2ae16e72ec5599fde528fc87b；完整两页，包括 Proposition 2.9.3、Remark 2.9.4 和 §2.9.5。它们给一类充分的共同图设计条件，不给所有合法图的唯一原点必要性。

没有 FULL 阅读 McMullen 219页或 CDT 218页原件，没有读取 Carathéodory 1954 原书页198。界16的证据是实际读到的 CDT primary 准确引述；scope 对此没有越界。N1 的旧包输入复用冻结证明及本人的既有226独审，不把本次诊断改称重新完整审查全部历史 packet。

## 2. 独立数学核验

**局部分支与全叶量词。** R²=ηR 且 η 为非整数半整数，给 Π=R/η、M=I−2Π。rank-one reflection 有固定空间；沿具体路径到达的 tuple 可以落入该空间。非零 fractional 项在局部次数 e 的拉回中，指数 e(31/2+k) 的奇偶性正是 N4 所述。原径向一条路径的非零系数不能推出全部前像到达叶的非零系数，H_g 单行还可能发生线性抵消。

**实际 cubic。** w³−3w=z 的 rational root 若有有限极点，左边最高极点阶无法与右边相消；故 root 必为 polynomial，再由 degree 排除。于是 {1,w,w²} 的函数域秩为3。独立代入 w′=1/[3(w²−1)] 和 w″=−2w/[9(w²−1)³]，核得完整二阶方程 (4−z²)w″−zw′+w/9=0。在 −2 的原生叶 w=1 有 square-root，而 w=−2 是 ordinary 叶；+2 同理。两 transpositions 生成 S3，在根之和为零的二维解空间给标准不可约表示；这里没有把含常数行的秩三 tuple 冒称不可约三维表示。

Φ_K=K³ζ³−3Kζ 满足 native pullback w∘Φ_K=Kζ，故三行都在全平面延拓。两个 branch values 的 simple preimages −2/K、2/K 到达正则第三叶；±√3/K 是 foreign 原点前像。故这个同一模型同时支付了“大导数”和量词反例，但没有支付当前 D/X/H_g 的类似图。

**能量与固定3费用。** 差分因子和 Haar 保持变换 u=z/w 后，对 w² 应用 Jensen，核得

E(Φ_K)=3log K+∫ log max(|1+u+u²|,3/K²)dμ(u)。

二次因子的 Mahler measure 为0；其对数奇点可积，截断负部可用可积支配函数，所以积分非负且趋于0。因此 m=3 时 3log|Φ_K′(0)|−E≤3log3，导数无界没有给此指定图族的解析 margin 无界。没有把这里的 τ 当成当前包或所有整模型的必要下界。

由 formal Lagrange/residue 公式，奇系数是 −binom(3n,n)/[(2n+1)3^(3n+1)]，n=0 为 −1/3，全部符号为负而非交错。Legendre carry 项及 v₃(2n+1) 都是 O(log(n+2))，所以实际 valuation 为 −3n−1+O(log n)，Taylor 半径确为 3^(−3/2)。有限固定 LCM 数组仅有固定3深度 O(log n)，不能整化该线性负深度。此处只论 Taylor/完整固定数组，没有偷换为所有数域亚纯入口失败。

**conditional 界。** 两值 cosh 图的 a、b 非零保证 sinh h₀≠0，两个差值各为 square，故全 even fibers 而导数任意大。三值 even fibers 按实际读到的 orbifold degree-divisibility 条件给 signature (2,2,2,∞)、Euler characteristic −1/2；curvature −1 下 disc 原点密度为2，故 bound 是 2/λ_O(0)，未支付其数值小于 exp τ。唯一 native0 加一值 even fibers 时，global square root s 存在、s omit −1，g=(1−s)/2 唯一零点为0且 omit1；g′(0)=φ′(0)/(4a)，所以 CDT 界16给 **64|a|**。当前源没有付这些全图条件；226指定小图具有它们，仍不能反推所有图。

## 3. 范围与运行

N13 的停止判断只表示本接口尚无同源 positive map、energy 和完整整模型准入对象，可把固定包降为结构工具供228比较；它没有证明全部 ramified maps 不可能，没有否定既有递推、无限非零及渐近资产，没有给新 ζ/L 数值定理。

本次数学程序 **0**，数学失败运行 **0**；旧 producer 重跑、CAS、参数/素数扫描、数值积分均0。读取、hash 和保存为文档操作；第一次默认 shell 因 ACL helper 启动失败，随后授权只读调用成功，不是数学运行。没有下载新原件，没有修改目标、旧稿、main 或 manifest。本收据保存后 actual FULL 自读并另报 bytes/SHA256；自读不改上述独立审查身份。
