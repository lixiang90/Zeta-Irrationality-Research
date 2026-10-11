# 同秩整代数参照对 CDT 第七、八节更强斜率界的约束

2026-10-07，作者 /root。本轮唯一 NEW 纸面主稿。起点为总记录 §195 与 delivery_carry_cartier_split_algebraic（SHA256 `44521a432fd71bdfef7e10a0d3ac63d636878b32aabfad5b293d8276a9fdf4a7`）。604 个冻结记录只读；未创建或运行数学 producer，未 import、重跑旧数学程序、guard、素数表或 Lean。本稿将已证整代数参照从第六节推广到原文已证的第七、八节；不是新的数值无理性定理。

本轮实际 FULL 读取固定 CDT v2 原件 PDF66–69、89–93、105–106、113–116、122–124，共18页；特别核查 7.1.6 的斜率限制、7.6.4 的线性系统唯一性及非负性、8.0.1 的任意非负分母矩阵。原件是 [218页本地稿](../literature/cdt2024_l2_chi_minus3.pdf)，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`；不混同20页 ICM 综述。FULL 回读冻结 [代数参照 A1–A15](cdt_odd_gamma_algebraic_reference_rank_barrier_20261007.md)、[Cartier F1–F24及全文](cdt_odd_gamma_ramanujan_frobenius_bridge_20261007.md)，并读取当前总记录 §§191–195。以下是新证明范围。

## 1. 准确固定比较对象

**H1.** 仍取

\[
A=-2^{20},\quad\mu=A^{-1},\quad F_u=B_5-u f_0,\quad u\in\mathbf Q.
\]

已证每个 transported branch 的普通点 μ 有非零完整 logarithmic jump；任何使 \(F_u\circ\varphi\) 在全盘亚纯的非恒定 holomorphic \(\varphi:(\mathbb D,0)\to(\mathbb C,0)\) 都 omit μ，包含任意有限 ramification。本文只使用这个已支付的 omission，不假设任意别的 projection 都同样 omit μ。

对整数 \(2\le m\le2^{19}\)，选 \(q=2^s\ge m\)、\(s\le19\)，取

\[
G_k(t)=(1-At)^{k/q},\qquad k=0,\ldots,m-1.
\tag{H1}
\]

它们实际 \(\mathbf Q(t)\)-独立、holonomic、属于 \(\mathbf Z[[t]]\)。独立性由 μ loop 的不同 q次单位根特征及 Fourier 矩阵给出。\(k=0\) 是常数1，所有正阶系数为0；下面2处的精确赋值公式针对 \(k>0\)：

\[
v_2([t^n]G_k)=(19-s')n+s_2(n)\ge0
\]

（约分后的指数分母 \(2^{s'}\)）；odd primes 由 p-adic integral binomial coefficients。每个 omit μ 的 disk map 都让 H1 的规范 logarithm 存在，故全部参考 pullbacks 是 holomorphic。这些是相同 m 的另一组实际函数，不是把参考 rank 加进目标。

它们取全零 \(b\)、全零 \(e\) 后有准确费用0。对第八节新费用也如此：在 (8.0.2) 的定义中，\(k>0\) 不可能满足 \(k\le b_{i_j,h}n_j=0\)，所以每项计数0，直接得

\[
\tau^{\flat\flat}(0)=0,\qquad\tau^\sharp(0)=0.
\tag{H2}
\]

任意实际 target 的非负 \(b,e\) 则由原定义有 \(\tau^{\flat\flat}(b)+\tau^\sharp(e)\ge0\)；这里不把该费用说成目标最小分母或原文所有方法的最优值。

## 2. Bost–Charles 与离散、连续凸性改进

写 \(\rho=\log|\varphi'(0)|\)，以及

\[
I_{hk}=\iint_{\mathbb T^2}\log|\varphi(r_hz)-\varphi(r_kw)|\,d\mu(z)d\mu(w),\quad
C=I_{ll},\quad r_l=1,
\]
\[
\widehat T(r)=\iint\log|\varphi(z)-\varphi(rw)|\,d\mu(z)d\mu(w).
\tag{H3}
\]

只对满足原文边界及有限积分条件的 maps 使用以下式子；若某个必要积分无穷，则相应有限严格矛盾不能由这些公式取得。\(\rho>0\) 时，将 H1 的 rank m、zero-fee tuple 代入 Theorem7.0.1 即得

\[
\boxed{C\ge m\rho.}
\tag{H4}
\]

令

\[
\alpha_k=\frac{\widehat T(r_k)-\widehat T(r_{k-1})}{\log r_k-\log r_{k-1}},
\quad S=\sum_{k=1}^l
\frac{(\widehat T(r_k)-\widehat T(r_{k-1}))^2}{\log r_k-\log r_{k-1}}.
\tag{H5}
\]

**H2（离散与连续 convexity）。** 当原文要求的 \(\alpha_l\le m\) 成立，Theorem7.1.6 对同一 m 参考 tuple 给

\[
\boxed{C-S/m\ge m\rho.}
\tag{H6}
\]

原文 continuous version 额外要求 \(\widehat A(1)\le m\)；满足这个条件时，以 \(S=\int_0^1\widehat A(r)^2dr/r\) 得同一 H6。不能为了增大 saving 略掉这些实际 slope 假设。

对 same-rank target，若已支付费用 \(\tau_T\ge0\)、\(\rho>\tau_T\)，则对应更强 bound 的整个右侧仍有

\[
\frac{C-S/m}{\rho-\tau_T}
\ge\frac{m\rho}{\rho-\tau_T}\ge m.
\tag{H7}
\]

这不是用较弱 rearrangement integral 替代 Bost–Charles integral；是直接将真正较强的 theorem 应用于同一 geometry 和同一 m 的已构造整 tuple。

## 3. 加权 Hermitian metrics 与第八节任意分母数组

**H3（原文 Theorem7.6.4）。** 固定上述 radii，若原文 (7.6.5) 的 \((l+1)\)-variable linear system 有唯一 solution \(s^*\in[0,1]^{l+1}\)，定义准确的 improved numerator

\[
C_m^*=\sum_{h=0}^l s_h^*I_{hl}
=C-\sum_{h=0}^{l-1}s_h^*(C-I_{hl}).
\tag{H8}
\]

这个系统只含 m、radii 及 H3 的 intersection numbers，不含目标函数的 connection constants、\(b\) 或 \(e\)。同 m 的参考 tuple 因而满足完全相同的系统条件；7.6.4 给

\[
\boxed{C_m^*\ge m\rho.}
\tag{H9}
\]

不能以“原文 heuristic 认为通常成立”代替唯一性或非负性的核对。若该条件失败，这个 theorem 本身不能用于相应 target，不能从失败的权重取得改进。

**H4（第八节完整 strengthening）。** 原文 Theorem8.0.1 不再要求 nested equal-nonzero columns，允许任意 nonnegative denominator matrix。其 (8.0.3)、(8.0.4)、(8.0.5) 的 archimedean numerators 分别恰为 \(C,C-S/m,C_m^*\)，分母费用改为

\[
\tau_T=\tau^{\flat\flat}(b)+\tau^\sharp(e)\ge0.
\tag{H10}
\]

H2 支付 reference 的这个费用恰0；H4、H6、H9 遂逐项给

\[
\boxed{\frac{\mathcal C_m(\varphi,r)}{\rho-\tau_T}\ge m}
\tag{H11}
\]

（每种 numerator 都连同其原文全部附加条件）。因此 arbitrary mixed rows、较精确第八节 finite-place fee 与较强 convexity numerator 均不能在这一 fixed-omission family 产生 strict contradiction。原文 8.0.7 的 \([0,1,2]^t\) savings 是真实的，但不会推翻 zero-fee calibration。

## 4. binomial metrics 亦需要同一初始收敛半径

**H5.** 原文 Theorem7.1.13 又允许一个 initial radius R 及参数 \(r>1,\lambda>0,\nu\in\mathbf R\)（此处将原文的 metric 参数 μ 改记 ν，避免混同已固定的 ordinary point μ）。其 numerator记为 \(\mathcal B_m(\varphi,R;r,\lambda,\nu)\)，保持原文的全部 terms、\(\chi_0\)、\(\chi_1\) 及 inequalities。

若 target tuple 含 \(F_u\)，其 Taylor series 有 μ 的非零 log singularity，所以共同初始收敛半径不能超过 \(|\mu|\)。参考 H1 的全部 Taylor series 都在 \(|t|<|\mu|\) 收敛，因而同一 R 也适用。其他参数条件只依赖 geometry、R、m 和 metric parameters。参考 theorem 费用0遂给

\[
\boxed{\mathcal B_m\ge m\rho,}
\tag{H12}
\]

target 费用非负时也不能 strict contradiction。这项比较不覆盖不同 projection 已真正去掉 μ 的情形，亦不把普通点首项被杀当成全 log singularity 消失。

## 5. 任意 finite rank 的缩放仍保持所有 convexity saving

**H6.** 对任意 m≥2，取 \(q=2^s\ge m\)，\(B=2^{\max(0,s-19)}\)、\(x=t/B\)，参考变为 \(\widetilde G_k(x)=(1-ABx)^{k/q}\in\mathbf Z[[x]]\)。所有 maps 同时缩放 \(\psi=\varphi/B\)，有

\[
\rho_\psi=\rho_\varphi-\log B,\qquad
I_{hk}(\psi)=I_{hk}(\varphi)-\log B.
\tag{H13}
\]

所以 \(\widehat T\) 的 differences、\(\alpha\)、\(\widehat A\)、S 均不变，原文 weight system 及其唯一性、非负性也不变，而 \(C,C-S/m,C_m^*\) 全部准确减 \(\log B\)。binomial formula 亦如此：取 \(R_\psi=R/B\)、\(\nu_\psi=\nu-\log B\) 时，Γ、\(\chi_0\)、\(\chi_1\) 及 correction terms 不变，\(2T_{r,\lambda,\nu}\) 减 \(\log B\)，故整体 numerator 减 \(\log B\)。这是逐项同时改 arithmetic coordinate、archimedean scale，未只改其中一侧。

若 \(\rho>\log B\)，这些 references 给对各自合法几何 numerator 的同一 bound

\[
\boxed{\mathcal C_m\ \text{或}\ \mathcal B_m
\ \ge m\rho-(m-1)\log B.}
\tag{H14}
\]

因此 \(\tau_T\ge\log B\)、\(\rho>\tau_T\) 是充分排除条件，准确有

\[
\mathcal C_m-m(\rho-\tau_T)
\ge m\tau_T-(m-1)\log B\ge0.
\tag{H15}
\]

对已证的 degree≤d、包含1和 \(F_u\)、由九个 jet polynomial 构成的 finite family，在本项应用中明确选 \(s=\lceil\log_2m\rceil\)。现有实际模型给 \(m\le2^{9d}\) 以及 uniform safe fee \(9d(1-m^{-2})>\log B\)。因此冻结 A10–A12 的 finite-amplification 排除同样延伸到这里列出的第七、八节 bounds。这只支付现有 uniform账本；其他更细 arithmetic arrays、删除 \(F_u\) 的 projections、不同 base 或真实 negative nonarchimedean收益不由此无条件排除。

## 6. 对研究路线的新增判断

**H7.** 当前实际 rank10 inverse-L tuple 的结构障碍不是仅第六节 rearrangement bound 的估计损失：包括原文已证明的 Bost–Charles、离散/连续 convexity、最优加权方案（满足其显式假设时）、任意 nonnegative matrix 的第八节界及同R binomial metrics，都受同秩 integral algebraic tuple 的约束。不能据此声称所有 Arakelov 或所有 irrationality methods 无效；所排除的是这些已明确列出的 formulas 与这一已证 forced omission 的接口。

**H8.** 实际下一步必须改变已具体指出的输入：真实相对周期 projection 完整消掉 μ translation；新的多奇点 carrier 要证明所消 relation 对全部 transported branches 的效果；或建立不同 geometry 的 integral model 和实际 rank。仅求 \(S_p=0\) 虽是有价值的算术信息，并不会独自救活这一固定 rank10 tuple。同行本轮正在推进 paired genuine extensions 和 quadratic anti-invariant source，其最终结果须独立 review，不能预先把新 carrier 的未证 constants 当成 ζ/L evaluation。

本轮 primary web search另核最新作者仓库 [Tang zeta2-zeta3](https://github.com/dtq1997/zeta2-zeta3-linear-independence) 与 [CDT ICM primary](https://arxiv.org/abs/2510.04156)。这两者在本项目已归档，未重复下载；前者只读取既有README及作者当前声明，本轮未本地重建 Lean，不作为本轮新定理。精确 Ramanujan polynomial 的 web queries 只用于寻找新原件线索，没有据 secondary snippets 增添数学 claim。

## 7. 本轮实际证据与待审状态

本稿是 paper proof，数学 producer0、素数扩表0、Lean0。实际 FULL 数学旧输入与18页 primary范围列首段；旧604记录的物理 rehash是文档 audit，不能代替人工重审全部历史proof。未新归档PDF，没有把封面metadata、检索片段或既有页数计作本轮FULL阅读。

本稿尚待正式全文独审及作者收审后最终 FULL 回读；未来 receipt/audit 不写进本稿依赖，避免双向pin。没有证明新的 ζ(7)、Catalan或其它数值无理性/线性无关性；goal继续active。原 \(\xi=\alpha\zeta(4)+\beta\zeta(5),\beta\ne0\) source、endpoint、fees 均不改动。
