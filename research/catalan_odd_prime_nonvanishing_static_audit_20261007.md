# 卡塔兰论文的奇素数整性、素数尺度非零性与 Lean 静态审计

日期：2026-10-07。原研究轮已按用户指示暂停。本文件是新的只读解读，不继续旧证明、不改旧稿、不创建旧轮 FINAL 收据。外部 `E:\codex-build\math` 全程只读；未运行其脚本、Lean、Lake、Comparator、lean4export 或 Nanoda，未安装依赖、未计算行列式或素数表。

本地 checkout 的 Git HEAD 为 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。论文为 `preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf`，44 页、574388 bytes，SHA256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`。本审计实际全文读取 PDF10–25，共16页；完整读取 `odd-primes.tex` 与 `nonvanishing.tex`，并读取 `foundations.tex` 第1–245行。没有声称本人全文读了全部44页，或重新验证了全部有限数值证书。

## 1. 可以从本轮证据得出什么

纸面奇素数论证具有完整的局部整模型：控制的是原始列池的所有满阶 minors，经可逆整列变换和整数 filter 返回原行列式，而非只估计某个归一化矩阵。非零性部分给出真正的全大素数推导：把随素数增长的矩阵化为三个固定的48阶有理矩阵，固定证书只用于证明这些种子的有理行列式非零，随后排除一个固定有限素数集合。

实际 Lean 终点是所要求的实数级数的无理性，没有额外数学假设；本地 import 闭包的静态扫描未见常见的未证占位或信任绕过标记。以上不等于本轮通过了 Lean 编译或独立内核检查。167个外部 import 的实际依赖源码不在本次本地闭包中，未重新构建；没有本轮 `#print axioms` 或 Comparator 成功输出。

## 2. 原行列式与有理性触发

论文的参数是

\[
n=48N,\quad a=11N,\quad b=7N,\quad q=g=4N,\quad h=2N,
\]
\[
L=59N,\quad C=63N,\quad H=65N,\quad A=19N.
\]

置 \(f=\sqrt{1-t^2}\)、\(w=t/(1+f)\)，则
\(t=2w/(1+w^2)\)、\(f=(1-w^2)/(1+w^2)\)。星 involution 是 \(w\mapsto w^{-1}\)，固定 \(t\)、反转 \(f\)。真实行是

\[
R_r=(1-t)^h t^{C-1}w^{r-g},\quad
P_r=(R_r+R_r^*)/2,\quad D_r=t(R_r^*-R_r)/(2f).
\]

由 Chebyshev 整系数恒等式，\(P_r,D_r\in\mathbf Z[t]\)，其低度支持和 Taylor contact 满足

\[
\operatorname{supp}P_r\subset[A,H-1],\quad
\operatorname{supp}D_r\subset[A+1,H-1],\quad
tP_r/f-D_r=tR_r/f=O(t^L).
\]

原始混合 moment 是

\[
M(i,j)=\int_{-1}^1\int_0^1\frac{|t|}{f(t)}\frac{t^i s^j}{1-ts}\,ds\,dt,
\quad Z(i,j)=\int_0^1\int_0^1\frac{t^i s^j}{1-ts}\,ds\,dt.
\]

\(M\) 同时含 \(G\) 和 \(\zeta(2)\)。contact 在所有原始列 \(b\le j<L\) 中抵消后者，得到

\[
F_j(r)=M^0(P_r,j)-\tfrac32 Z^0(D_r,j)
+4G\sum_v[t^v]P_r\,c_{(v-j)/2}\in\mathbf Q+\mathbf QG,
\quad c_l=4^{-l}\binom{2l}{l}.
\]

因此假设 \(G\in\mathbf Q\) 后，原行列式 \(\Delta_N\) 为有理数。它是原始 \(n\times(n+q)\) 列矩阵与整数 filter 的乘积；filter 来自 \(s^{b+k}(1-s)^q\)。全文的有限处估计都针对这个实际对象，不依赖把某个未知实数系数丢弃后误称原矩阵已是有理。

## 3. 奇素数的两层结构为何严格

对 \(2\sqrt H<p\le H\)，固定有理 \(G\) 的分母素数在充分大尺度已落到小素数区间。置
\(E(t)=(1-t^2)^{(p-1)/2}\)。论文逐项证明

\[
p^2M^0(i,j)\equiv E_dM^0(i',j'),\qquad
p^2Z^0(i,j)\equiv
\begin{cases}Z^0(\lfloor i/p\rfloor,j'),&i\equiv j\pmod p,\\0,&\text{其他},\end{cases}
\]

其中 \(i'\ge-1\)，边界 \(M^0(-1,j')=k^+_{j'+1}\) 被明确保留。这些同余包含局部整性声明。\(H<p^2/4\) 保证只有一层 factorial carry；偶数起始 moment 的存活项由完整的 \(mp-\lambda\) block 组成，再用
\(\sum_{j=0}^{(p-1)/2}c_j^2\equiv(-1)^{(p-1)/2}\pmod p\)。证明没有把残余 block 当成完整 block。奇数、偶数、\(i<j\) 和 \(i'=-1\) 分支均有对应公式。

按列余数抽取后，\(X_j=p^2F_j\bmod p\)，在规定支持范围内

\[
X_\ell=V_\ell,\qquad X_{p+\ell}=U_\ell-V_\ell,
\quad U_\ell=0\ (\ell\le A).
\]

这首先使一些配对和 \(F_\ell+F_{p+\ell}\) 真正属于 \(p^{-1}\mathbf Z_p^n\)。若可配对数为

\[
d_0=[\min(p,L-p,A)-\max(b,H-2p)]_+,
\]

任意满阶 minor 最少使用 \([d_0-q]_+\) 个改善后的列，于是
\(v_p\Delta_N\ge-2n+[d_0-q]_+\)。这里减去 \(q\) 正是额外列池带来的最坏选择成本。

对 \(p>H/2\)，中央列已有 \(pF_j\) 局部整性，而且

\[
pF_j\equiv-\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell},
\quad J=H-p,\quad K=L-p.
\]

保留的非中央列 \(Y_\ell\) 提供 \(p^2Y_\ell\equiv\pm V_\ell\)。把中央列加上相应的 \(p\) 倍 \(Y_\ell\) 是可逆整 shear。关键是

\[
Y_\ell=p^{-2}y_0+p^{-1}y_1+y_2
\Longrightarrow pY_\ell=p^{-1}y_0+y_1+py_2.
\]

因此未知的下一层 \(y_1\) 已是整数；无需假定它为零，也无需丢掉保留列。剩下中央列的 \(p\)-scaled residues 只落在例外 \(e\) 个向量的 span 中，故可通过提升模 \(p\) 核基的 \(\mathrm{GL}(\mathbf Z_p)\) 变换使多数中央列真正整化。最后列池包含 \(R\) 个可能 \(p^{-2}\) 列、最多 \(S\) 个可能 \(p^{-1}\) 列，其余整数列：

\[
R=K_++(K-A)_++[J-\max(b,K)]_+,
\]
\[
S=[\min(A,K)-b]_++[\min(b,J)-\max(0,K)]_+.
\]

对任意原满阶 minor 的损失是

\[
v_p\Delta_N\ge-\min(2n,n+R,2R+S).
\]

所有列变换及逆变换均整，再对整数 filter 使用 Cauchy–Binet，故这确是原对象的界。特别没有从第一层的低秩，直接推出原 \(p^{-2}\) 列已经减少分母。\(K\le0\)、\(J\le b\)、可选边界配对 \(\ell=A\) 和 \(p=H\) 的计数在证明中均有交代。

## 4. 全部有限处并没有遗漏

取 \(x=p/N\)，两层列计数给连续分段损失 \(d(x)\)，其值为

| 区间 | \(d(x)\) |
|---|---|
| \([0,25]\) | \(96\) |
| \([25,29]\) | \(146-2x\) |
| \([29,65/2]\) | \(88\) |
| \([65/2,69/2]\) | \(153-2x\) |
| \([69/2,40]\) | \(222-4x\) |
| \([40,58]\) | \(182-3x\) |
| \([58,59]\) | \(124-2x\) |
| \([59,65]\) | \(65-x\) |

面积为 \(8609/2\)。普通 PNT 的 step-function 上下逼近将此转为奇素数总损失 \(-8609n^2/4608-o(n^2)\)。小素数不是免费忽略：原始 entry 的 factorial-floor 界给
\(O(n\sqrt H\log H+n\log\operatorname{den}G)=o(n^2)\)。\(p>H\) 在充分大 \(N\) 时没有负贡献；\(p=2\) 独立支付 \(-505n^2/4608-o(n^2)\)。

由非零有理数的精确 product formula，论文得到

\[
\liminf\left(\frac{\log|\Delta_N|}{n^2}-\tfrac12\log2\right)
\ge-\frac{8609}{4608}-\left(\tfrac12+\frac{505}{4608}\right)\log2
>-2.29084.
\]

这条下界仅用于非零尺度，不能由有限处界本身推出 \(\Delta_N\ne0\)。下一节另付这一点。这里审计的是奇素数论证及其接口；实处最终证书的逐项独立计算不属于本文件范围。

## 5. 从一个固定证书到所有充分大素数

取 \(N=p\)，维数 \(n=48p\)。论文在 \(\mathbf F_p[w]\) 的回文空间中构造两组真正的基

\[
U_\ell=(2w)^\ell(1+w^2)^{p-1-\ell},\quad
Q_i=w^i\sum_{j=0}^{p-i-1}w^{2j}.
\]

按最低次项的三角性，过渡矩阵 \(\mathbf a\) 的对角元为 \(2^{-i}\)，其行列式为 \(2^{-p(p-1)/2}\)，在每个奇素数上为单位。另有 \(\mathbf b=\mathbf a\Pi\)，\(\Pi e_0=0\)、\(\Pi e_i=e_{p-i}\)。恒等式

\[
E(t)w^i=\sum_\ell t^\ell(a_{\ell i}+b_{\ell i}w^p)
\]

配合真实 \(R_{pr_0+i}\) 的 Frobenius 分解，只产生基行 \(r_0\) 与其 successor \(r_0+1\)。星对称分解进一步同时给 \(P\) 和 \(D\) 的正确抽取；\(P\) 的 \(u+1\) 位移被前面的 \(t^p\) 精确消耗，\(D\) 不带此位移。

最后的 auxiliary 行48不能删掉其 \(P\) 的 degree18 项和 \(D\) 的 degree19 项。论文证明该项在增长矩阵中从 \(20p-i\) 开始，与原始行的最低度完全一致；并不是把低度超出原接触范围的基行免费塞回去。整数 filter 的 \((1-s)^{4p}\) 先在已整的 \(p^2F_j\) 上约化，再变为固定第四阶差分。

令 \(\mathcal B_0,\mathcal B_1\) 是 \(N=1\) 的49行种子矩阵取相邻48行得到的两个固定有理矩阵。约化后的整个 \(48p\) 阶矩阵确为

\[
\mathcal L_p=\mathbf a^T\otimes\mathcal B_0+
\mathbf b^T\otimes\mathcal B_1,
\]
\[
\mathcal L_p((\mathbf a^T)^{-1}\otimes I)=
I_p\otimes\mathcal B_0+\Pi^T\otimes\mathcal B_1.
\]

\(\Pi\) 的 \(0,+1,-1\) 特征值重数分别为 \(1,(p-1)/2,(p-1)/2\)，所以

\[
\det\mathcal L_p=(\det\mathbf a)^{48}\det\mathcal B_0
\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}
\det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}.
\]

纸面模101证书包含三个矩阵的非零 pivots；所有种子分母的素数因子 \(\le65\)，故101是合法模数。本轮没有重新计算144个 pivots。其数学作用只是证明三个固定有理行列式非零，绝不是对增长矩阵做素数采样后外推。

排除 \(2\)、有理 \(G\) 的分母素数、种子分母及三个固定行列式的分子/分母素数，得到固定有限例外集合。对 \(p>260\) 且不在该集合，\(p^2\mathcal F_p\) 局部整且约化行列式非零，所以

\[
p^{2n}\Delta_p\in\mathbf Z_{(p)}^\times,
\qquad v_p\Delta_p=-2n=-96p.
\]

这一全大素数结论确实强于有限数值证据，也完全独立于 \(G\) 的具体有理值：其贡献在 \(p^2\) 层已消失。

## 6. Lean 的真实终点、证书和信任边界

实际终点在 `lean/OAI/NumberTheory/Catalan/Results/Conclusions.lean:11`：

```lean
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2) := by
  change Irrational catalan
  rintro ⟨z, hz⟩
  ...
```

`Estimates/Contract.lean:10` 中 `catalan` 的定义就是这一实 `tsum`，且有 `mainClaim_unfold := rfl`。`Results/Catalan.lean` 导入 `Results/Conclusions`；`Main.lean` 再导入前者及精度/算术文件。并非只证明了另一个叫 catalan 的符号、也并非通过给终点添加非零性假设来规避主张。真实终点先假设一个有理代表 \(z\)，从素数尺度非零性获得无限序列，再把有限处下界与实处上界组合成矛盾。

`Arithmetic/PrimeNonvanishing.lean` 实际接入 `fixedMatrix_zero_det_ne_zero`、`fixedMatrix_one_det_ne_zero`、`fixedMatrix_neg_one_det_ne_zero`，给 `determinantRat_prime_valuation = -96*p`，并从素数无穷性选取趋于无穷的非零尺度。`PalindromicResidueDeterminant.lean` 证明约化的是 \(p^2\) 倍原 filtered rational matrix，行列式尺度为 \(p^{2n}\)，并用 entry 分母不被 \(p\) 整除来支付约化。

固定证书在 Lean 中以另一种严格可检验形式保存：canonical 有理矩阵先乘固定整数，逐行接到模101 literal base，再接三种 literal 矩阵的显式 right inverse。相应逐行有限等式使用 `decide +kernel`；`fixedLiteralModZero_rightInverse` 等汇总后，从 \(MM^{-1}=I\) 推出模101行列式非零，最终再传回固定有理矩阵。没有以“表格 pivots 均非零”这个未证命题直接作为假设。这里只核读了证书桥与代表性逐行证明，没有编译这些计算证明或逐项人工核算全部矩阵 entries。

静态 import 元数据从 `OAI.NumberTheory.Catalan.Main` 递归遍历，发现本地闭包988文件：981个 Catalan 模块，加7个 ZetaFive 辅助模块，分别是 `LargePrimeWeighted`、`LargePrimeIntegral`、`LargePrimeTable`、`Endpoints`、`RiemannSqueeze`、`WeightedOrder`、`WeightedPNT`。这是 PNT/加权求和辅助，闭包没有导入 \(\zeta(5)\) 无理性终点。

对这988份本地源码逐文本扫描，未见 `sorry/admit/axiom/unsafe/native_decide/implemented_by/extern/sorryAx/ofReduceBool/unchecked`，亦未见自定义 `run_cmd/run_meta/initialize/elab/macro/syntax/#eval/#print` 标记。扫描是元数据检查，不能当成988份数学证明的逐式全文人工审阅，也不证明代码已经成功 elaboration。

另有167个实际源码未在本次本地闭包的 import，包括 Lean、Mathlib 和 `PrimeNumberTheoremAnd.Catalan.Consequences`。`lakefile.lean` 指定 Lean4.34.1、mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`、PrimeNumberTheoremAnd commit `c39a751132c88b6e8080b74c74023fd95b3d8be0`，并有依赖 compatibility patches；未运行它的自动下载/打补丁配置。对保存的 PNT patch 新增行作关键词扫描未见上述信任标记，但没有完整审计或构建该外部库。配置文件中的编译期 `unsafe env.evalConstCheck` 不在数学源码闭包内；不能把配置代码中的 `unsafe` 自动等同于主定理依赖了额外数学公理，也不能据此免去实际构建审计。

比较题面 `ComparatorChallenges/Catalan.lean` 包含一个 `sorry`，但该文件就是只陈述挑战的模板。实际解决模块是 JSON 指定的 `OAI.NumberTheory.Catalan.Main`，同名 theorem 的字面命题吻合。JSON 的 `permitted_axioms` 仅列 `propext`、`Quot.sound`、`Classical.choice`，且 `enable_nanoda=false`。这是允许集合和配置，不是本轮 `#print axioms` 的实际输出；关闭可选 Nanoda 本身也不是错误证明证据。

`docs/005.md` 保存了“主标题结论已形式化”的范围声明；Comparator README 保存了运行方法，而非本次验证日志。当前 `formalization.yaml` 完整关键词扫描没有 Catalan 条目，不能拿该 catalog 为本题额外背书，也不能因目录遗漏就反推 Lean 终点必然失败。本轮未找到并核验对应当前指纹的编译/Comparator成功记录，最终状态应写为“源代码级静态审计未发现上述漏洞，实际复现验证尚未进行”。

## 7. 对本项目缺口的可迁移性，及不可自动迁移的对象

本轮为比较实际全文读取了冻结 `cdt_odd_paired_head_free_integral_lattice_20261006.md` I1–I25 和 `cdt_odd_paired_actual_local_gram_layers_20261006.md` G1–G15，仅作解读，不重新执行或推进它们的证明。两者研究的是 rank2n 饱和 Newton 整数值格中的实际 signed Hermite Gram：

\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\quad W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,
\]

并保留 \(P(m)/d_m=P(2n+1-m)/d_{2n+1-m}\) 的真实饱和约束。它与 Catalan 的混合双积分行列式不同：权重、局部基、度数、filter、弱层、原周期消去关系皆不同。原 paired 格的局部 \(\psi=(t^p-t)/p\) 层还有 ragged top degree，不能把 Catalan 的48阶种子直接代入。此前 \(\xi\) 或局部 restricted blocks 的名称相似，也不建立原 determinant 的等式。

可迁移的是一个具体、可审的证明策略。若以后恢复研究，面对“需要无限多个局部单位”的缺口，可先尝试在**原矩阵和原整数格**的一个素数索引尺度上证明：

1. 已支付的 \(p^e\) 倍原矩阵逐 entry 局部整；
2. 完整 residue matrix 经已付费的 row/column 变换确为有限个固定有理 seeds 的 Frobenius block，例如 \(A_p^T\otimes B_0+B_p^T\otimes B_1\)；
3. \(B_p=A_p\Pi_p\)、\(\det A_p\) 对全部大素数为单位，\(\Pi_p\) 有已证的固定有限特征类型；
4. 每个所需 seed 非零，用一个合法固定模数的 exact certificate 证明，再排除其固定有限分子/分母素数。

这四项若全部付出，就能得到真正全大素数非零性，而不依赖 prime sampling。第2项通常是实质难点；在本项目 \(p=9r+1\) 或其他分数尺度、实际饱和 paired 约束和 shifted Hermite jets 下，它目前不是已证明的输入。本审计没有建立新的 seed 分解，也没有恢复暂停的数学探索。

此外，冻结 Gamma/\(S_p\) 接口在本輪仅检索了其定义与状态段落，未称全文重审。其缺口是特定 weighted Cartier image **为零**，而 Catalan 这里是固定 residue matrix **非零**。已证 Lucas/Cartier 完整 block 传递没有把 \(S_p=0\) 化成三个固定有理矩阵的非零性；模101种子证书无法迁移成全 prime 的 supercongruence。若要借 Frobenius finite seed 思路处理该零性，必须另证该特定 weighted row 的统一 exact comparison 或 kernel identity，并支付 higher/partial reciprocal blocks，不能把抽象 Frobenius 分解或一个 Tate factor 当作结论。

## 8. 本轮读取与指纹边界

完整人工读域：论文 PDF10–25；`odd-primes.tex`672行；`nonvanishing.tex`413行；真实 `Main.lean`、`Results/Catalan.lean`、`Results/Conclusions.lean`、`Estimates/Contract.lean`、`Arithmetic/PrimeNonvanishing.lean`、`Determinants/PalindromicResidueDeterminant.lean`、`FiniteMatrices/FixedDeterminantsNonzero.lean`、Comparator题面/JSON/README、`docs/005.md`、Lean README、论文README、toolchain、lakefile。`foundations.tex`只读1–245行；`FinitePlaceAssembly.lean`及其匹配桥、固定 inverse/canonical逐行源为指定段落/声明审阅。一次大输出发生截断，随后对需用的纸面奇素数全部672行和关键 Lean bridge 单独分段读取；不把截断部分写成完整人工读域。

本地988文件闭包与外部167 import、完整 catalog 和 PNT patch新增行均只是纯文本扫描/元数据核查。没有运行原仓库程序或执行数学验证；没有外部目录写操作、没有修改旧研究稿或本轮暂停前的候选。

关键文件指纹：

| 文件（相对外部checkout） | SHA256 |
|---|---|
| `lean/OAI/NumberTheory/Catalan/Main.lean` | `b49f7377c833a8a688858832d2f347eff499b71d1d035f00c32b5ed56caef52a` |
| `lean/OAI/NumberTheory/Catalan/Results/Conclusions.lean` | `96fb1e6b2839ea70dd574cffb5ae4e83dc67cd3cdbff916e77f8f9edf331c50c` |
| `lean/ComparatorChallenges/Catalan.lean` | `532c6393186873a9137fd87412df8cdee51ad9bb2704fec8bbbfdf483b956a83` |
| `lean/ComparatorChallenges/Catalan.json` | `2b3bce6fda567c1cdfe18d341682c26986fe534b3a5d2172bf73350afbefe773` |
| `lean/docs/005.md` | `81e93bf39eeabe2264a6bb6ac6ee5adfd8a41e4dacdab6db780117312364a899` |
| `lean/formalization.yaml` | `20739b2378f60b059069c098a94222151462671c3eab20d4129ef6a85672d5d8` |
| `build/sections/odd-primes.tex`（论文目录下） | `42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10` |
| `build/sections/nonvanishing.tex`（论文目录下） | `4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f` |

结论范围：本轮纸面接口与源代码审计支持“存在具体、完整的 Catalan 算术与非零性证明链”，尚未提供“本轮已成功复现 Lean 验证”的证据。其最有价值的可迁移点是 **完整整列池的第二层消元** 与 **Frobenius 将无限单位问题降成固定有限种子**；数值结论或种子非零性不能在不同原格/原周期之间自动继承。
