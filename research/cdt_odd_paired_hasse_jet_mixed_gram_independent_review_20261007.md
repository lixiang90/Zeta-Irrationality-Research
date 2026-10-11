# 原行列式低阶 Hasse jets 与混合 Gram：独立全文审阅

2026-10-07，source_pencil_finalize。被审主稿为 [cdt_odd_paired_hasse_jet_mixed_gram_20261007.md](cdt_odd_paired_hasse_jet_mixed_gram_20261007.md)，SHA256 `c178bf8540ff8a0697260ff3d5d137039d92b6288affc29f432934b100704112`。本轮实际一次完整读取八节 H1–H17 后独立纸面核证；不是摘要审查。结论 PASS，无实质修改请求。

本轮另外实际全文回读冻结 partial P1–P14、supported weighted dual transfer T1–T18 及 low-price support domination L1–L18。local Gram 与 coupled Gram 在前轮已实际全文读取，本轮由 partial 的完整实际公式复核同一原 S、weights、degree 与实际轮廓；没有重新宣称执行其证书。Borodin 存档原件本轮实际完整文本读取 PDF2–7 六页，26页快照；没有称整 PDF 已读或借其具体 classical-ensemble asymptotic 代替当前对象。

## 1. 实际斜率、谱与无限非零

H1 的 X derivative 与冻结 P1 完全一致：只有 V_j(X) 的 24X 项响应，故真实斜率为 24ΣW_j v_jv_j^t。W_j 是正整数，原整数值 basis 在整数节点的 values 是整数。非零 degree<3n polynomial 不能在6n+1个不同节点全为零，故 V_n 严格正定。这不要求实际复 B_n(ξ) 正定。

以 V_n 的实正定 square root 作 congruence 后，B_n(c)+tV_n 化为一个实对称矩阵加 tI。因此 H2 的 exact degree、H3 的全部实根、H4 的 zero multiplicity=实际 corank 均成立；不能仅从非对称 rank 得到该结论。对首次非零 coefficient，用 kerB 及其 orthogonal complement 逐块展开：kernel block 贡献 t^ν det(V|ker)，complement 贡献其非零 determinant，cross terms 只进入更高阶。这确认 H5 后的准确首次 jet 公式。

冻结 P7 对同一固定有理 a,b,c 提供无限 n=4r 的 rank≥6r；m=8r，所以 ν≤2r=n/2。H6 的 k 可依 n,c 变化，但不因此损失无限非零。H7 的 squared certificate 在实 c 下无 cancellation。主稿没有提升为固定 k 或原 k=0 的无限非零。

## 2. 同一完整整模型与固定源量词

冻结 supported T13/T17 明确给同一 whole-X polynomial 的 signed Q_n，constant 与 H8 完全匹配；low-price L11/L12 确认它没有被另外零新增家族改变。这里接受冻结全尺度整模型及已审积分率作为输入，不重跑旧程序，也不把其历史12141检查数计作本轮证据。

H9 来自整数 polynomial 的 Hasse derivative：每项 multiplier 是整数 binom(i,k)，不新增 k! denominator。代入 c=u/M 后用 degree≤m−k 给 H10；随 k 改变仍被同一个 M^m 控制。固定源分母与 M 只造成 O(n) logarithmic fee，不影响 n² 主率。平方证书的 Q_n² 和 M^(2m) 亦保持正确方向。Q_n 是合法 signed scale，不是 raw minimal denominator，稿中界定准确。

## 3. 混合 measure 的 coefficientwise 解析界

H11 的离散正 measure 与 H1 的 bilinear/Hermitian Gram 都恰等于 V_n，因为节点实、basis coefficients 实。冻结轮廓等式只在 X=ξ 使用；再由 affine identity 表示 ξ+t，未假称这个 shifted source 仍是同一个 cot 轮廓周期。

独立展开 m-fold Andreief：在 ∏(dμ+t dσ) 中选择 k 个 σ variables，m! 的除数与 binom(m,k) 准确给 1/((m−k)!k!)。两个 determinants 相同，故积分为 det[g_i(w_l)]²，得到 H12。取 total variation 后是 |det|²；关于 ν+tσ 的 Hermitian Andreief 给 [t^k]det(P+tV)，确认 H13 的逐 coefficient 上界。无限轮廓的指数 tail 与有限离散 measure 保证本步所有 polynomial moments 绝对可积。

P、V 均正定，故 det(P+tV)=detP∏(1+tλ_i)，λ_i>0，所有 H_(n,k)>0。没有从一个复 determinant 的 pointwise modulus 界强行推逐 coefficient 界；稿中 mixed-integral 推导确实提供了后者。

## 4. 剪切、radius penalty 与未证门槛

H14 对与 X 独立的实 det1 congruence 同时变换 B、P、V，两个 determinant polynomials 完全相同，因此全部 Hasse/positive coefficients 都不变。复杂 basis 的 Hermitian conjugation 单独说明正确；没有在 P 新基与 V 旧基之间拼接。完整 determinant identity 也确实避免部分 compounds 的 inverse-shear norm，不能据此删去真实 discrete/head observations。

对 0<R≤1，由 positive H_k 有 R^kH_k≤det(P+RV)，再用 k≤K 得 H15。R_n=exp(−τn)、K=n/2 使 penalty 准确为 τ/2，符号与 n² scaling 正确。若 H17 被证明，其 strict gap 给所有足够大 n 上同一全部低 jets 的 uniform upper bound；H8/H10 给无限 H6 subsequence 上某 nonzero jet 的 lower bound，固定 M 的 O(n) 不能抵消 strict n² gap。这确认 H17 是一个有效 sufficient irrationality criterion。

H17 本身尚未证明。k0 衰减、positive V 或把 R 取小都不独自证明它；主稿显式保留 mixed relative-spectrum/实际支撑分析和 τ/2。本文也不把 matrix rank6r 当 CDT function rank。未取得新的 ζ/L/Catalan 数值无理性或线性无关性结论。

## 5. 审查范围

数学 producer 新建、执行、import、rerun 均0；辅助prime扩表0；没有新的数值拟合、源调整、Lean claim 或 full frozen-audit 重跑。本轮仅阅读文档、独立纸证与 SHA metadata。当前556冻结记录的全局一致性由 root audit负责，本文不冒称逐条重新核对。

本审阅通过的是稳定 c178 主稿的全部 H1–H17、源和对象接口，以及清楚限定的条件结论。正式来源收据将在双方实际最后全文回读之后建立，避免未来 review/receipt 的循环引用。
