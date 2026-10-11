## 213. 混合周期四维投影、联合整格与显式 Jacobi 两端接触行

2026-10-07。本轮归类 progress：得到四份新的数学稿、一个有限精确整格 producer 及有范围的 primary 文献核读；尚未得到新的 ζ/L 数值无理性或线性无关性定理。此前用户要求的原仓库同步已经完成，本地 main、origin/main 与已核云端 HEAD 同为 adc7f1241b42e322a6451854ab7e4b4c146bf78a，tracked 缺失0、工作区干净。本轮继续只读原仓库，不重复同步，也不把 Git 完整性检查算作数学验证。完整 goal 保持 active。

**一、固定混合目标有真实的四维投影。** [几何稿](cdt_mixed_catalan_pi2_geometry_20261007.md)取 A=arctan x、B=Σχ₄(n)xⁿ/n²、Ψ=aB+16bA²、F′=(Ψ−u)/(1−x)。因为 Ψ′=A(a/x+32b/(1+x²))，实际闭合空间为 {1,A,Ψ,F}，秩恰为4；同时保留 B、A² 的较大空间秩为5。这是固定周期方向的不可逆投影，而非有理换基。仅假设 aG+bπ²=u∈Q 就使 F 的原始1分支完整可填。

任意 transported 1 分支的值可写 A=π/4+πk、B=G+iπ²c，其中 c≡k/2 mod Z。混合 b≠0 时，完整填入条件强迫 k=c=0；b=0 则只迫 c=0、k偶，已分别处理。arctan lift g 的实际范围须省略所有非零 kπ/2；g=0 处允许 B 有非零运输常数。全部分支条件与 holonomy 的真实函数秩均由实际 monodromy 和 conjugate-loop 证明。

**二、共同映射确实能够超过 π，但固定算术费用仍封住该载体。** 显式 slit map φρ=tan(πρz/(1+ρ²z²)) 给出每个有限ρ的完整共同 pullbacks，并证明 Lρ≤Jρ≤π−log2。将 slit surface 与 D(3π/4,ε) 只沿上半盘粘合，得到实际承载 B、F 原函数 continuation 的 simply connected 多叶曲面。严格 Schwarz 证明其正规尺度 r_R>π；限制正规 uniformizer 后得到 |φ′(0)|>π 的共同 map，且给出精确有限 Jensen 公式与有限 fiber 界。未求 r_R 的数值或更优的 quantitative J，不能仅由尺度增加宣称秩矛盾。

[独立算术稿](cdt_mixed_catalan_pi2_arithmetic_independent_20261007.md)完整支付全部素数和任意素数幂，给 e=0、σ=(0,1,2,5/2) 的安全 cap。p、2p 的固定偏移响应允许完整 rational Laurent tails；任意完整 Q(x) 基通过非零 determinant matching、e 截断及八种精确费用，得到

\[
\boxed{a\ne0, b\ne0:\quad\tau_{\mathrm{fixed\ type}}^{\min}=61/32.}
\]

该最小值在自然模型达到，不只是一个自然基上界。任何共同 map 仍有 L≤log C<3/2，所以这种 CDT 固定 N^e 与有限 LCM 类型不能给出反证。此结论仅限制这个完整混合载体及上述费用接口，不限制更一般联合整数格或其他真实投影。

**三、有限联合 Taylor 格确认分母节省，也揭示高度缺口。** [联合格稿](cdt_mixed_joint_taylor_lattice_20261007.md)及[新 producer](cdt_mixed_taylor_lattice_20261007.py)对 toy a=b=1、u=0，计算12个一维与25个多维整数接触核，D≤6；没有假定 G+π²=0，也没有数值周期或 PSLQ。转置带变换 HNF 保留完整像格，δ=lcmden(B₀⁻¹e_last) 严格给最小竖直格点，首项理想为 (δ/L)Z。“饱和”只指完整整数接触核，不扩大像格。

四维 D6、N23 的一维核，首项分母相对末行逐项 lcm 节省104093970750倍，但本原向量高度有95位。四维 D6、N18 的更宽核首项理想为 (512/164190889863)Z，节省2250倍，返回见证却有520位；它不代表最小高度。独立 reviewer 只额外重算 D2/N6 的36个最大子式，确认 δ16 和理想 (8/675)Z；没有虚称独立重复全部37项。所有结果都是有限范围，不是渐近费用下降；u 改变还会加入 u log(1−x)，故 toy 理想不能直接迁移到未知关系。

**四、原矩方法获得一个显式整数混合行构造。** [两端接触稿](catalan_mixed_two_end_contact_support_lemma_20261007.md)从当前 Catalan 原文的真实矩分解得到 period part

\[
4C_j(P)G+\frac{\pi^2}{4}(H_j(P)-D_j),
\qquad H_j-D_j=\mu C_j,\quad\mu=16b/a.
\]

C_j 是 P(t)/√(1−t⁻²) 在∞的非负 Laurent 系数，H_j 是 tP(t)/√(1−t²) 在0的 Taylor 系数。新关系确实连接两个端点。保持原 P≥t^(19N)、D≥t^(19N+1)、deg<65N、共同因子(1−t)^(2N)，混合 raw kernel 维数恰36N−1，filtered-only kernel 恰40N−1；原纯 G 接触空间则恰48N，原 Chebyshev pairs 是其完整基。于是直接保留48N行的混合行列式必为零。“只调整 D”会产生禁止的低次数系数；r=g 的原行有 C_(19N)<0 的全N显式见证。

这一障碍同时给出积极构造。filtered 的低端条件是 Q 对权 (1−x)^(6N)/(π√(1−x²)) 的0至8N矩正交。取

\[
Q_d=P_d^{(6N-1/2,-1/2)},\qquad 8N+1\le d\le44N-1.
\]

Jacobi 正交性给全部低端矩条件；半整数 binomial 展开证明 8^dQ_d∈Z[x]、l1 norm≤2^(5d+6N)。固定 d_μ2^(58N−2) 清掉原有限列块 b≤j<L 中 H/C 的 dyadic 分母，filter 和端点的逆三角递推仍为整数，且系数高度 exp(O_μ(N))。这是实际全秩整数子格；未证明它是完整本原格或支付其指数。

同时把过滤列数降为 n′=44N−1，L′=55N−1，保留原支持与端点因子，合规行池恰44N维，可以显式选择44N−1个独立整数 pairs 组成自洽的方阵候选。不同于在旧48N个条件下只减少行数，这里行、列共同重配。独立 polynomial pairs 不等于实际 moment determinant 非零；后者及全部 finite-prime/real-place 比较须重新证明，原 Chebyshev 估值 lemma 不能借用。

**五、新文献的可用输入与阅读范围。** primary 检索未在实际核读来源中找到1,G,π²的新无条件线性无关性定理；这是有范围的检索结论。EMN 的三维联合 period 包和 DD 的形式 Lie 自由性不提供数值 period injectivity。新保存 Viola–Zudilin 的 dilogarithmic LI 论文及 Brown 非线性几何、Brown–Schnetz wheel 论文；后者的正确 wheel 定理给所有奇数 n 的单 ζ(n) 实积分表示，未给无理性结论。两篇 nonlinear 来源实际共新增10页 root 节选阅读；公式层面的支持/索引问题记录为局部 caution，不据此否定其 main theorem。两份 NIST DLMF HTML 与有限公式 TeX 已归档，实际只读 Jacobi 对应表项。详见[核读范围](../literature/cdt_mixed_new_sources_20261007/reading_scope.md)、[novelty scope](../literature/catalan_pi2_mixed_novelty_source_scope_20261007.md)、[Jacobi scope](../literature/catalan_mixed_contact_jacobi_source_scope_20261007.md)。

**验证与下一步。** 四稿收到实际全文数学纸审；新增 matching 与 Jacobi/reduced-size 段另外全文核读。root 全文读取最终正文及本节；有限 producer 有实际断言，审阅范围与单个独立子式例已分开记录，没有 Lean 形式化验证。CDT v2 本轮 root 新读物理66–69页，不能计为整篇全文验证；原 foundations child 读1–434全文，root 读1–263。没有旧 producer、guards 或 prime 表扩跑。此前 manifest 与主稿旧字节前缀保持不变；本輪指纹及审阅范围见[新归档](../literature/manifest_cdt_mixed_projection_joint_lattice_20261007.json)。

**本轮完成后的当前进展：获得了真实四维混合载体、严格更大的共同解析映射、精确固定费用下界，以及全N显式整数 Jacobi 两端接触行与可行方阵规模；尚未得到新的数值无理性或线性无关性结论。下一轮优先在这同一个矩对象上证明非零性、完整整数格指数/素数估值和实处严格差距。完整 goal 保持 active。**
