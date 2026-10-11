# R0 toric family completion 唯一性：原几何稿作者的独立核查

日期：2026-10-06。NEW 数学审阅；本审阅者是 toric completion 几何稿作者，不是下述唯一性主稿的作者。本次另行独推维数索引、open-curve 归纳和非零性，再实际全文读取唯一性主稿 U1–U5（含 U1–U14 全部公式）。旧稿与同行稿均只读；没有执行或 import 任何 mathematical producer。本记录不改任何已冻结文件。

**审阅结论：通过。** 在指定的四维 \(\mathbf Q\)-model \(Y\) 上，
\[
CH_0(E,4)_{\mathbf Q}=CH^3(E,4)_{\mathbf Q}=0,
\qquad
CH^4(Y,4)_{\mathbf Q}\longrightarrow CH^4(Y^*,4)_{\mathbf Q}
\quad\hbox{单射}.
\]
结合已证明的存在性，coordinate symbol 的 rational family completion \(\Xi\) 唯一；该 family class 非零。没有证明某个 fibre 上的 completion、regulator、数值周期或积分格标记的唯一性、非零性。

## 1. 实际对象和几何前提

实际全文读取的唯一性主稿是 research/cdt_odd_R0_toric_completion_uniqueness_20261006.md，6991 bytes，SHA256：

    b6baab390cd23c15b1edc717e11a3b97c42dfc4f5c16a8c87c10fe74676f66a2

只读核对其冻结几何前提 research/cdt_odd_R0_toric_completion_20261006.md，SHA256：

    abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0

采用这个具体模型：\(Y\) 光滑、维数 \(4\)，\(Y^*=U^4\)，\(U=\mathbf P^1_{\mathbf Q}\setminus\{0,\infty,-1\}\)；\(E=Y\setminus Y^*\) 是 split SNC 纯三维边界。其 codimension-\(r\) open strata \(D^{r,*}\) 是有限 disjoint union，维数 \(4-r\)。\(r=1\) 的各分支为三个 \(U\) 或 \(\mathbf G_m\) 的乘积，\(r=2\) 为 \(U\times\mathbf G_m\) 或 \(\mathbf G_m^2\)，\(r=3\) 为 \(\mathbf G_m\)，\(D^4=\varnothing\)。

这些乘积是该模型中的全局 split strata，不是仅 étale-locally 的 torus bundle。有限 SNC strata 给出闭过滤 \(D^3\subset D^2\subset D^1=E\)，各 \(D^r\) 纯维数 \(4-r\)。本次使用这一已经审过的具体几何结论，没有将一般 rational stratum 的 higher Chow groups 自动视为零。

## 2. 逐项核准 open-curve 归纳

令 \(A\) 是从 \(\mathbf P^1_{\mathbf Q}\) 删去非空有限有理点集所得曲线；实际只需要 \(A=U,\mathbf G_m\)。对光滑 \(Z/\mathbf Q\)，projective bundle 与 localization 分别给
\[
CH^p(Z\times\mathbf P^1,q)_{\mathbf Q}
\simeq CH^p(Z,q)_{\mathbf Q}\oplus CH^{p-1}(Z,q)_{\mathbf Q},
\]
\[
CH^p(Z\times\mathbf P^1,q)_{\mathbf Q}
\longrightarrow CH^p(Z\times A,q)_{\mathbf Q}
\longrightarrow \bigoplus_{\text{删去的有理点}}CH^{p-1}(Z,q-1)_{\mathbf Q}.
\]
后式两外项为零就推出中项为零，不需要 splitting 或 field-to-variety injectivity。

实际 point 输入仅为
\[
CH^2(\mathbf Q,4)_{\mathbf Q}=CH^3(\mathbf Q,4)_{\mathbf Q}
=CH^2(\mathbf Q,3)_{\mathbf Q}=0.
\]
前两项由 rational Adams decomposition 和 \(K_4(\mathbf Q)_{\mathbf Q}=0\)；第三项由 totally real field 的 weight-two \(K_3\) rational vanishing。DK 原件 PDF25–26 直接给这些输入。另对全部光滑 separated \(Z/\mathbf Q\)，整系数定理
\[
CH^1(Z,q)=0 \quad(q\ge2)
\]
来自 MVW Theorem4.1/Corollary4.2 和 Theorem19.1。这适用于完整乘积 variety，不能只用 point 版本代替。

同时归纳 \(CH^2(A_1\times\cdots\times A_m,3)_{\mathbf Q}=CH^2(A_1\times\cdots\times A_m,4)_{\mathbf Q}=0\)。初始 \(m=0\) 是 point 输入。添加一个 \(A\) 时，projective-bundle 额外项是 \(CH^1(Z,3)\) 或 \(CH^1(Z,4)\)，localization 右项是 \(CH^1(Z,2)\) 或 \(CH^1(Z,3)\)，全部为零。

随后归纳 \(CH^3(A_1\times\cdots\times A_m,4)_{\mathbf Q}=0\)：初始是 \(CH^3(\mathbf Q,4)_{\mathbf Q}=0\)，添加一个 \(A\) 时，只增加已经消失的 \(CH^2(Z,4)_{\mathbf Q}\) 和 \(CH^2(Z,3)_{\mathbf Q}\)。主稿 U7、U8 全尺度成立。整个递推只使用列明的已知 point 输入和 weight-one 定理，没有误用一般 Beilinson–Soulé 猜想。

代入全部实际 open strata，得到
\[
CH^{4-r}(D^{r,*},4)_{\mathbf Q}=0 \quad(r=1,2,3).
\]

## 3. singular boundary 的维数索引和 exactness

\(E\) 可以 singular，使用 higher Chow dimension notation \(CH_j(-,q)\)。纯维数 \(d\) 的 scheme 满足 \(CH^p(X,q)=CH_{d-p}(X,q)\)，所以这里统一有
\[
CH^{4-r}(D^{r,*},4)=CH_0(D^{r,*},4),
\qquad CH^3(E,4)=CH_0(E,4).
\]
闭/open localization 在 homological notation 中保持 \(j=0\) 和 \(q=4\)。因 \(D^4=\varnothing\)，\(D^3=D^{3,*}\) 的相关群为零；依次应用
\[
CH_0(D^3,4)_{\mathbf Q}\longrightarrow CH_0(D^2,4)_{\mathbf Q}
\longrightarrow CH_0(D^{2,*},4)_{\mathbf Q},
\]
\[
CH_0(D^2,4)_{\mathbf Q}\longrightarrow CH_0(E,4)_{\mathbf Q}
\longrightarrow CH_0(D^{1,*},4)_{\mathbf Q},
\]
两外项为零，严格推出 \(CH_0(E,4)_{\mathbf Q}=0\)。再对 \(E\subset Y\) 应用
\[
CH_0(E,4)_{\mathbf Q}\longrightarrow CH_0(Y,4)_{\mathbf Q}
\longrightarrow CH_0(Y^*,4)_{\mathbf Q}.
\]
\(Y,Y^*\) 均纯四维，中、右项就是 \(CH^4(-,4)_{\mathbf Q}\)，故 restriction 单射。无需任何关于 singular-boundary spectral sequence 的附加断言。

本次额外实际核读 MVW PDF150–152（printed135–137）：PDF151 Properties17.4(2) 的 localization 对任意 scheme 的 open complement 成立；纯 codimension 的 closed complement 给 long exact sequence。上述每一步满足该前提。任意 scheme 的 localization 与 smooth-only motivic comparison 是不同输入，主稿没有混同。

## 4. family 非零性和准确作用域

具体 \(Y\) 与 \((\mathbf P^1)^4\) birational，其 \(\mathbf Q\)-function field 是 \(\mathbf Q(v_0,v_1,v_2,v_3)\)。泛点 restriction 将 \(\xi\) 送到 Milnor symbol \(\{v_0,v_1,v_2,v_3\}\)；依次取四个 coordinate-zero field valuations 的 tame residue，得到 \(\pm1\in K^M_0(\mathbf Q)=\mathbf Z\)。Tensor \(\mathbf Q\) 后仍非零，故泛点 image、原 \(\xi\) 和唯一 \(\Xi\) 皆非零。

这只从非零 image 反推 source 非零，不要求泛点 restriction 单射。四个 valuations 是 \(\varphi\) 的 vertical pole 方向，在 \(Y=f^{-1}(\mathbf G_m)\) 之外，与 horizontal boundary 的 \(\{-1\}\)-torsion residue vanishing 相容。

审阅通过的结论仅在指定模型的 \(\mathbf Q\)-family、rational coefficients 层面。没有推广到 \(\mathbf Q(x)\) 或 \(\mathbf C\) 的同型消失，没有证明 individual fibre、Abel–Jacobi Betti lift、conifold current、integral marking、regulator 的非零性或任何数值无理性。

## 5. 实际来源阅读和冻结记录

本次使用的已保存原件均只读：

* DK2011 published PDF literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf，SHA256 1911f2f4a805e1a3d218ca247665209f3fe9505aa9bc0ae949b1163d7271ede4。实际读 PDF25–29：Adams/number-field inputs、field Milnor symbol comparison 和 localization；这些页已在本轮 toric 完成研究实际阅读。
* Levine1994 literature/levine1994_higher_chow_revisited_20261006.pdf，SHA256 5f4de92e51f03dfb9a4708f70ed9a8f58d2c2a51e310eeb4d597be84c7450984。实际读 PDF79–85，特别是 PDF84–85 Corollary5.4 projective bundle formula；已在本轮 toric 完成研究实际阅读。
* MVW2006 官方原件 literature/mazza_voevodsky_weibel2006_motivic_cohomology_clay_20261006.pdf，SHA256 fb20ff2f30cefe0b67b359de275491e3716d509d891cc72afa95460f57ed0180。实际读 PDF40–42、174、176–178；本次新增实际全文页读 PDF150–152，专核任意 scheme 的 localization。同行来源收据 literature/manifest_cdt_odd_weight_one_higher_chow_20261006.json 的 SHA256 是 a82c6465281cfe036854180709cfa73bd13113005c055dbdea7609f8608f7500。

本审阅没有新增 PDF，没有修改 source receipts，没有使用 producer 输出为数学证明。结论由公开定理输入和上述明确 finite closed filtration 得出；没有 Lean 验证声明。
