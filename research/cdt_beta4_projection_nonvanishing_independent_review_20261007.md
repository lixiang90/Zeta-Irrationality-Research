# β(4) 实际投影素数尺度非零稿的独立全文纸审

2026-10-07。审阅者：/root/source_pencil_finalize。被审最终稿 research/cdt_beta4_projection_nonvanishing_20261007.md，SHA-256 72a6cf3df5263b9b27f726ca1bc66ca0da2456623d4bd655aef9b135b73a3996，12000 bytes。实际全文读全部八节、N1–N23；已复读奇分母上界修正及最后状态版本。结论：全部纸审通过，无进一步数学修订请求。纸审不称 Lean 或机器形式化验证。

## V1 同一对象、regular-part 与特殊化量词

直接输入为本轮 fresh FULL 读过的单周期稿 research/cdt_beta_single_period_confluent_integral_model_20261007.md，全部八节/B1–B29，物理 SHA a008a54d3307f151911ad0fc1dfa3587e05fd54eb89bd0172be364d162d64f2c、11668 bytes。N1–N4 保留其 r=3、H=3n、原 Nk/D、p_J=I 和全部一、二阶 regular-part 消去条件。没有替换成另一个正 Gram，也没有只保留目标周期而忘掉低阶 β(2)、β(3) 的完整投影。

N5 的微分式可以独立按每个 t^u 核对：(t−1)^{H−1}/(H−1)! 的系数恰为 1/D′(u)，Euler 算子多项式 Nk(δ) 再乘 Nk(u)，得原 p_{k,u}。N6 的 actual n=2 Wronskian 符号与精确系数通过；它否定直接静态 Chebyshev 捷径，未推积分 determinant 为零。N7 的 −4^{-4} 正确：行求和产生 −F/4，再将三阶分母提出 4^3。绝对收敛由 F(z)=O(1/z) 给出。

局部 theorem 对有理矩阵多项式 E(T)=q+TI 及 T∈Z_p 成立。未知实数 β(4) 不能直接当作某个 p-adic 整数。只有在假设 β(4)=a/b∈Q 且 p∤b 后，才把该局部结论用于原积分矩阵。主稿始终保留此量词。

## V2 原投影在 n=p 的完整整性和 matching 更高层

N8 的 factorial 剥离单位和符号独核通过。u=ap+i 的两段 factorial 含 p 因子数分别为 a、2−a，总数二；p≥13 使全部相关 factorial 参数小于 p²，没有漏更高层。Wilson 配对 i!(p−1−i)!≡(−1)^{i+1} 与 D′ 的符号 (−1)^{a+i} 相乘，得 (−1)^{a+1}a!(2−a)!。

N9 不只给低阶 jet：删去 QI 的两个 matching 因子以后，余下函数在 ζ=0 的分母为单位，属于 Z_p[[ζ]]；mod p 的完整 rational identity 为 U≡1。故所有正次数 U 系数被 p 整除。前三级 Taylor 的估值下界 2、1、0 正确。

off-matching 时 Bk(ap+i)/p=−a/(i−k) 的符号来自 (z^p−z)′(i)=−1。于是 Nk/D′ 的估值至少一，且 a=1、2 的 residue 分别为 −1/(i−k)、4/(i−k)，与 N12 一致。

matching 时，ζ=ap 属于 pZ_p；完整函数在该点为零。所有次数≥3 的 Taylor 系数至少一层 p，故可收敛评价的余项至少 p^4。这里必须用完整 U 的正次数整除性，而不只是 T_k≡ζ²。再除 D′ 的 p²，得到 matching p_{k,ap+k}∈p²Z_p。N11 的全部整性与两条 matching 强化因此有独立完整证明。

作为另一核对，完整约束矩阵 L_I 的 ℓ=1、2 列分别乘 p、p²，mod p 每个 residue i 的两行块为 [[1,1],[1/2,1/4]]，det=−1/4；L_J 的对应列分别至少含 p、p²。这也独立给 p_I∈pZ_p。它不单独给 matching p²，后者仍依赖上述 tail 证明，主稿没有省掉这一层。

## V3 原 A3 的端点与全四层界

N13 与直接模型 B8/B9 的有理部分一致，包括对角 −T_{v,4}；符号是 −T_{v,3}/d+T_{v,2}/d²+(T_{u,1}−T_{v,1})/d³。

首候选的“最大奇数 12p−7”已由 root 指出并由作者修成 12p−5；本审实际 FULL 读修后最后版本。最大 u=3p−1 的 T_{u,1} 含 j=2u−1，奇分母最大 2j+1=4u−1=12p−5。p≥13 时仍严格小于 p²，故此边界修正不改变 valuation 或 residue 结论。差 |u−v|<3p<p² 同样成立。

N14 的每项最坏层数分别为 3+1、2+2、1+3，故都至少 −4。extra rows 的 p 因子把其贡献提高到至少 −3。原 J 部分的四层 residue 只在对角存在：奇数 p、3p 的符号分别为 ε、−ε；其是否进入 T_{k,4} 恰由 4k>p、4k>3p 判断。p≥13 时高块 residue 的两种非零值 −ε、−ε·80/81 都为 unit；m=ceil(p/4) 的低高划分准确。

低列 4v<p 时 T_{v,a} 无 p 分母。所有列 entry 的三层付款 N16 成立；在开始 determinant 消元之前已经证明，不需要事后假设 Schur 补整性。

## V4 低块反对称 gate 与完整倍数列表

低块对角的 extra matching 行至少有 p²，所以即使 A 最坏四层，p³ 后仍消失。off-matching 且 u不与v同余的行，d 为 unit；与 p_{k,u} 至少一层相乘后最多只剩两层，也不进入三层 residue。

真正贡献只来自 u=v+p、v+2p。这时 N13 的前两项分别最多一、二层；最后一项有 d³ 的 p³，T_{u,1}−T_{v,1} 的 p^{-1} 才到四层。对 v∈L，第一段完整 odd-p 倍数是 p、3p；第二段完整倍数是 p、3p、5p、7p。没有遗漏 partial block 边界，因为 4v<p。

因此两条 p⁴ A residues 分别为 ε/96、19ε/13440。再乘 N12 的原 projection residue，常数准确为

\[
-\frac1{96}+4\frac{19}{13440}
=-\frac1{210}.
\]

N18 的 −ε/[210(v−k)] 符号和 factor 均通过。p≥13 排除了所有显示的小整数分母。该 gate 是完整实际 E 的局部层，不能把它改成经典 Schur 的 (x_i−x_j)/(x_i+x_j) 核。

## V5 已付款的三角消元和 determinant residue

N19 先对真实 E(T) 的全部低列乘 p³、高列乘 p⁴。N14、N16 保证所得 entire matrix 为 p-integral；T∈Z_p 的目标对角在此层全部消失。其 reduction 确为 [[S,0],[B,D]]，D 为上述单位高对角。

在 F_p 上右乘 [[I,0],[−D^{-1}B,I]] 后，完整 reduction 成为 diag(S,D)。该 column operation 的 determinant 为 1，可以提升为 local unit 操作；不需要知道 B 的 entries，也没有对 unscaled E 作免费的有理 Schur 消元。

故 rank=p−m+rankS，scaled determinant 的 residue=detS detD，与 T 无关。因为 scaled matrix 本身属于 Z_p[T] 且正次数 T 系数含 p，其 determinant 也属于 Z_p[T]，所有正次数系数被 p 整除。这证明 N21 的 polynomial 版本，而非仅在有限个 T 值的 pointwise 拟合。

如果 detS 为 unit，估值恰为 −3m−4(p−m)，而不是只给不等式。detS 不为 unit 时，只能说第一层秩缺损，不能声称 unscaled determinant 为零。主稿对两个情形准确分开。

## V6 有限正证书、失败例与没有闭合的无限量词

m 为奇数，反对称矩阵在奇特征下 determinant 为零；p≡1、3 mod8 确实给 m 奇数。偶数 m 不自动非退化。

p=13、m=4 时，Pf=1−1/4+1/3=13/12，mod13 失效。一个二阶主子式非零，四阶 determinant 为零且反对称 rank 为偶数，故 rankS=2，完整 scaled rank=9+2=11。此为第一层失败，未证明实际 E13 奇异。

p=23、m=6 的五项 Pfaffian 独立逐项核对：

\[
\frac{13}{12},\quad-\frac7{24},\quad
\frac{73}{216},\quad-\frac7{48},\quad\frac{13}{60}.
\]

第二和第四项的四阶 Pf 均为 7/12，中间 Pf 为 73/72，末项 Pf 为 13/12；第一行系数和交错符号相乘后得到所列五项。其共同分母 2160 上的分子为 2340−630+730−315+468=2593。mod23 为 17/21，且210为单位，故 N23 的正证书成立。

因此对所有 T∈Z23，n=23 的 determinant 估值准确为 −18−68=−86。有理根的既约分母必须被23整除，是这一局部定理的正确推论。若真实 β4 有理且分母不被23整除，则真实 E23 非零；不排除分母有23的有理假设，也不无条件证明未知实 β4 的 E23 非零。

未证明无限多个 successful primes，未证明 fixed23 的任何 p-power 传递，未证明失败 prime 的更高层结论。末节将这些明确保留为缺口，没有从有限证书推出新的数值无理性。

## V7 完整读取、证据与结论

本审本人 actual FULL：最终72a6稿全部八节/N1–N23；直接单周期a008全部八节/B1–B29；此前修后9d1候选亦全文读，并将12p−5边界修正与最终状态核对。初始a86也全文读取，但它不是最终被审输入。

这一正式审阅的证明自足，不另读取或下载 PDF；本人同轮另一项 Padé来源作者工作确实读35个distinct primary PDF页，记录在其主稿中，不能把该域冒认成这份审阅新产生的阅读，更不继承同行页数。未运行或重算 prime 表、旧 producer、guards、原官方seed、Lean 或任何数学程序。有限Pfaffian与residue均由逐式纸核完成。

N1–N23 正式独立全文纸审通过，无进一步正文修改请求。actual p-integral projection、matching 高层、三层反对称 gate、paid triangular rank及23单尺度证书均成立；max odd endpoint修订已闭合。仍缺无限非零、同一对象的全有限处预算和足够实处衰减，未证明 β4 或其它数值的无理性。

本正式审稿由审阅者在保存后最后全文自读。只保存这一份新的独审，不改被审主稿、620冻结记录、旧审计或官方仓库；统一最终manifest由root处理，不另作循环receipt。
