# Actual vanishing orbit 格独立审阅

日期：2026-10-06。NEW 独立全文审阅。旧稿、同行 PY/JSON/manifest 只读，未执行或 import 任何数学 producer。

## V1. 实际审阅对象

实际全文读 `research/cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md`，冻结 SHA256
\[
\texttt{baf29ee041a0ea48c4b64c517cf0712f24c52c4c98893e4c74a98698c7e05586}.
\]
O1–O38 全文及 §10–11 均已实际阅读。同行的 verifier 与 certificate 没有执行，不以其“38 checks”替代审阅。其是否执行成功是作者自有登记，本审阅只接受纸面全尺度证明。

本轮实际全文重读 frozen Yukawa，SHA \(\texttt{172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15}\)，重点 degree-one graph 的 Y8–Y10 与 actualδ 的 Y27。real Betti 稿 \(\texttt{dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f}\) 上一轮已全文独审；本轮 use 的一般 logshift 与 PL 标度与该输入一致。另本轮复读 frozen exterior E1–E3/E10，核同一 origin spectral projector 的定义。

## V2. 一般 k 交叉式与 actual 格

O7 的 \(C(g,g_{U^k})=ka(2b_1-b_2^2)+(ka)^3/6\) 对任意整数 \(k\) 来自 Frobenius 真 logshift。代入 \(2b_1-b_2^2=a^2/3\)、\(\kappa=-a^3/16\) 及 intersection \(=-C/\kappa\)，确得
\[
\delta\cdot U^k\delta=\tfrac83(k^3+2k).
\]
负 k 的 sign、k1 的 8 及 physical \(M_0=-U\) 均正确。每个 \(U^k\delta=(-1)^kM_0^k\delta\) 为 actual integral compact cycle；没有将 formal Levelt vector 当 actual cycle。

O11 的 Gram、Pfaffian \(-256\)、determinant \(2^{16}\) 正确。O13 的整数基变换给 \(8J_2\oplus(-32J_2)\)，故 intersection Smith \(8,8,32,32\)。作者明确这些不是包含 \(\Lambda_\delta\subset L\) 的 Smith factors，此区别正确。

## V3. 全 monodromy、real involution 与 N³

O16 的 companion \(U\) 来自 \((U-1)^4=0\)，O17 的每列由 \(e_j+(e_j\cdot e_0)e_0\) 给出，sign 正确。它们及 inverse 为整数，preserve Gram，因而全群稳定 orbit 格。physical infinity eigenvalue \(+1\) 与 square-root scalar twist 的 \(-1\) 不能混同；作者未混同。

O18 的 real homology involution列为 \(U^{-j}\delta\)，其 square 为 1、Gram 变号与 cohomology PD 对应的额外负号正确。O19 的 \(N^2=A^2-A^3\)、\(N^3=A^3\)，O21 的
\[
N^3=(-1,3,-3,1)^T(1,1,1,1)
\]
是实际 orbit basis 中的完整 rank-one operator。最高 log coefficient 与 \(C(y_0,h_z)=-\ell(z)\) 相符。真实 double loop logarithm 为 \(2N\)，cube 的 8 不能省去；O23 正确。

## V4. Γ、remaining cycle、有限 index

O24–O25 使用 period-germ injectivity（cyclic span 与 nondegenerate V），不是仅凭一个点的 period。故
\[
2\Gamma_V=-e_0+3e_1-3e_2+e_3.
\]
代入 companion 的 \(U^{-1}\delta=4e_0-6e_1+4e_2-e_3\)，得到 O26 actual integral \(\alpha=-3e_0+4e_1-e_2\)，正确。未据此声称 whole \(\Gamma=\Gamma_V\)。

O28 的 \(m\mid256\) 来自整数 alternating lattice 的 Pfaffian determinant；O29 的 projected full lattice 嵌入 orbit dual 来自 self-adjoint pairing，dual exponent32 正确。这是先于整 projector 升级的安全界，逻辑顺序没有倒置。

## V5. 核心 degree-one integral 升级

O30–O33 的两个地图是真正同维 smooth proper degree-one 共同 resolution；degree64 quotient 不在此图中。pullback 与 PD pushforward 在 free integral H³ 上均有定义；\(q i=1_{\mathbf Q}\) 强迫 \(q i=1_{\mathbf Z}\) 因 free endomorphism 张量 Q 单射。伴随性给 \(Q(iu,iv)=Q(u,v)\)。因此 image 为 split saturated 整格且 isometric 于 compact mirror 的 free H³，unimodular；\(\Pi=iq\) 为 actual integral orthogonal projector。

unique rational orthogonal projector 的 deck descent 与逐 fibre integrality 不要求整 correspondences 自身在原始 base 上先下降。原始 smooth integral local system 平行传输该 integer operator，即给全 base integrality。没有要求 full H³ rank4。于是 \(m=256\) exact，而 inclusion Smith factors仍未给出；O34 的范围正确。

## V6. Γ even 与 charge

O35 的
\[
N^3z=(z\cdot\Gamma_V)\Gamma_V/4
\]
由 O21/O25 全向量成立。若 \(\Gamma_V=d\gamma\) primitive in unimodular L，选择 \(z\cdot\gamma=1\) 并用 \(N^3\) 整数，得 \(d^2/4\) 整数；结合 \(d\mid8\)，只有 \(2,4,8\)。故 sector \(\Gamma/8\) charge ≤4，与 orbit coordinates \(v/16\) 的 exact16 不矛盾。O38 的 \(\ell(L)=d/8\,\mathbf Z\) 正确。作者不报 exact primitive MUM cycle。

## V7. scope 与结论

全文纸面 claims 通过。actual saturation/unimodularity、exact index256 与 Γeven 是本輪新正结果。它们没有建立 complete integral mirror basis、canonical conifold germs 的 arithmetic Betti coordinates、whole-prefix bad-prime bound、或 CDT 的足够 capacity。作者最后仍将 extension source/spectral projector charge 留给独立 NEW 证明，符合当时 scope。

本轮 actual primary read 为 KLM published PDF12–14（SHA \(\texttt{8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9}\)），用于本人 Betti extension 新稿的 AJ 整/有理与 torsion 说明；这些页不是 degree-one map 输入。BK PDF6–7、12、19 与 Movasati93–95 在以前轮已实际读，当前通过 frozen Yukawa 全尺度 proof 使用，未冒认本轮重读。没有新增 primary PDF，没有数值、PSLQ、Lean 或新的特殊值无理性结论。

