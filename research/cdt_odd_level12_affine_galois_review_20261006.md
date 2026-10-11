# D12 双周期实际 affine/PV 结论的限定只读独审

日期：2026-10-06。本稿仅记录对 [实际主稿](cdt_odd_level12_affine_galois_20261006.md) §§1–8 的独立只读审核。未修改主稿，未执行或导入任何 producer，未以有限 checks 替代全尺度证明。审核时主稿尚待根任务冻结；本记录不复制主稿作为第二份定理版本。

## 1. 实际对象与两个 period classes

实际读取了已冻结的 generator_cocycle、gamma_cocycle 和 joint_full_model 全文。hL 是共轭源的实际 primitive，hZ 与 hL 都用相同 \(\mathcal B\) 及 weight \(-2\) slash，故在 \(\Gamma\) 的 compact Hauptmodul \(v\) 上确有同一个 homogeneous Bol module。

独立重算了两个 coboundary witnesses：\(\eta\) 的 \(P_L(\eta)(0)=44160\)、\(P_Z(\eta)=0\)，以及 \(x_8\) 的有限 fixed point \(-1/2\) 上 \(P_Z=138240\)、\(P_L=72320\)。任何 quadratic coboundary 在相应 parabolic fixed point 必为零，因此两 cohomology classes 在 \(\mathbf C\) 上独立。另核整数 affine \(\eta\) 的 \((A-I)^3=13248E_{34}\)，但主稿采用 fixed-point witnesses 已足够。

§3 的 algebraic-group 论证通过：translation kernel 是 \(G\)-stable 线性子空间；若不是完整 \(V\oplus V\)，Schur/semisimplicity 给 \(aZ+bL\) quotient；kernel-zero algebraic graph 在 reductive \(G=PSL_2\) 上必须为 coboundary。此步骤用的是 reductive algebraic group representation 的 splitting，没有错误地令 discrete \(H^1(\Gamma,V)=0\)。右作用先以逆元转为左作用的约定与实际表相容。

## 2. 同一 Bol 系统、七维矩阵与 regular singular

独立用 \(\theta_q=k_v\partial_v\) 展开三次导数，得到主稿 (A8)；两个强迫项 \(\mathcal B F_j/k_v^3\) 都是 weight0 的 \(\Gamma\)-invariant meromorphic functions，故属于同一个 \(\mathbf C(v)\)。减数值常数只改 homogeneous \(\mathcal B\) 方向，不改 forcing。

主稿 (A10) 的两个 homogeneous blocks 是字面相同的实际 matrix \(Y\)，七维 fundamental matrix 与 companion equation 精确匹配。对列 \(\mathcal B,\mathcal B\tau,12\mathcal B\tau^2\)，Wronskian 是 \(24\mathcal B^3(\tau')^3\ne0\)，七维 determinant 为其平方。

每个 cusp 的 SL₂ scaling 中，\(\mathcal B\) 的 weight2 因子与 \(h_j\) 的 weight \(-2\) 因子准确相消。真正 \(h_j|_{-2}A\) 是 source constant 给出的 cubic polynomial 加 lower period polynomial 与 positive cusp series，因此 \(H_j\) 为 finite Laurent factor 乘有限 log polynomial。homogeneous 三列也有同样的 degree≤2 log 形式。有限阶 \(v\)-导数仍 moderate；\(\mathcal B\)-zeros 只给 apparent meromorphic poles。detY 在 cusp scaling 中是 \(\mathcal B_c^3 q_c^{-3}\) 乘一个 meromorphic unit，亦可据此核 inverse matrix 为 moderate。regular-singular 接口通过。

## 3. 实际 PV 群与六个 jets

实际回读 [Singer 作者原件](../literature/singer2009_differential_galois_lms_author_20261006.pdf) 的 Theorem1.3.9（PDF13）、Corollary1.3.21（PDF17）、regular growth 和 Proposition1.3.27/Schlesinger（PDF20），并回读 PDF26 的 regular-singular equivalent criteria；来源 URL 为 https://singer.math.ncsu.edu/papers/LMSlectures.pdf。没有声称通读82页。

七维系统 regular singular，因此实际 monodromy closure 与 differential Galois group 相同。主稿 (A12) 中，任何 automorphism 对两 homogeneous blocks 必用同一个 \(g\)，而每个 actual inhomogeneous vector 的 difference 为 \(Y a_j\)。据实际双 affine closure，\(\operatorname{Gal}(L/K_0)=\mathbf G_a^6\) 的接口通过。

L 恰由 K0 及六个 actual jet coordinates 生成，高阶导数由共同三阶 forcing 消去。PV transcendence-degree 公式给六个 generators 在 K0 上代数独立，故是六变量纯超越扩张。translation-invariant rational expressions 只属于 K0；若进一步对全部 \(\Gamma\) continuation 不变，则由密性与 PV fixed-field theorem 精确属于 \(\mathbf C(v)\)。

有限代数 gauge-field 扩大不产生新的六 jet relation；有限 base cover 对实际 monodromy只取 finite-index subgroup，connected affine closure 保持。因此主稿 §7 在它明确规定的 rational differential constructions、finite algebraic gauges/covers 范围内通过。

## 4. 范围与非结论

本审核通过实际正文 §§1–8 的上述数学链；不重核新下载文件的 acquisition utility，不运行任何证书，不替代完整 discrete zero stabilizer 的分类。

唯一发现的文字问题是审核时 (A1) 的 `H_j=B h_j,quad B=` 缺少 LaTeX 反斜线；已报根任务修复，不影响数学。主稿 C 常数域包含所有数值周期，故上述 functional algebraic independence 不能直接推出 \(\zeta(3)\) 与 \(L(3,\chi_{12})\) 的数值独立。它也不排 thin scalar leaves、全新的源、非代数扩张、成功 mixed Taylor 格或另证的 bundle holonomy 定理。
