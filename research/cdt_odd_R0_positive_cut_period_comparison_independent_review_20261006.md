# R₀ positive-cut current / relative-period 比较的独立复核

日期：2026-10-06。Reviewer：quarter_actual_rank。本文是新的独审记录；被审稿及所有旧/同行 mathematical producers 均只读，未执行、import 或重跑。

实际全文回读的 final 稿：
[positive-cut comparison](cdt_odd_R0_positive_cut_period_comparison_20261006.md)，
SHA256 **fb44cacdd85484887a51c90c7547432eff5ceb0516b356a3fbc26a5f97f65dc8**。
已核的旧实际 mirror/residue/tube 输入 SHA256 为
**43009e569bba25b6f819f0e5f1de0b96fa2db57e1a73817e8b087d294a059912**。

审阅结论：§§1–7 在声明的 **raw open current scalar integral / actual relative period** 范围内通过。具体 compact Chow regulator 的 Betti lift 仍未识别；不能由以下身份自动删除该缺口。

## 1. 正实 logarithm 与 normal-first orientation

\(\arg v\in(0,2\pi)\) 的 lower-to-upper jump 是 \(-2\pi i\)，所以
\[
 d[\log^+v]=d\log v-2\pi i\,\delta(b)\,db
\]
确实按稿中的 coorientation 成立。Reviewer 独立重排 normal forms：
\[
 db_0\,db_1\,db_2\,da_0\,da_1\,da_2
\]
到三个 complex coordinate 的正向 order，permutation
\([1,3,5,0,2,4]\) 的 inversion count 是 \(1+2+3=6\)，符号为正。
两张 sheet 的投影是 holomorphic local chart，因此都有相同 complex orientation；无需再给 lower sheet 加一个猜测的负号。

稿中 \(R_4^+\) 的前三项包含至少一个 holomorphic \(d\log v_j\)，与 holomorphic three-form wedge 为零；最后一项保留
\(-(2\pi i)^3\)。四个 positive cuts 的共同 fibre intersection 空，因为
\(\phi\ge256>256x\)。这个判断只用于 \(0<x<1\)，不将 \(x=1\) 的 node 当成已满足 cut-transversality 的光滑 fibre。

还可直接检查开放模型的 current differential：按稿中将 delta factors 放在前的 order，逐项 telescoping 给
\[
 dR_4^+=d\log v_0\wedge\cdots\wedge d\log v_3
       -(2\pi i)^4\delta_{T_0\cap\cdots\cap T_3}.
\]
在所选 smooth fibre 上两项都为0，故 \(R_4^+\) 是 closed **open current**。这不是对 compact boundary/Bloch faces 的 completion 证明。

## 2. LEFT residue 与两张 sheet

固定 \(\Phi=\prod_{j<3}(v_j+2+v_j^{-1})\)，独立核得
\[
 \Phi(v_3+2+v_3^{-1})=256x,\quad
 v_3=e^{\pm i\alpha},\quad
 \Phi\sin\alpha=16\sqrt{x}\sqrt{\Phi-64x}.
\]
\(0<a=256x/\Phi<4\) 保证两根不同且没有 positive-real root。

LEFT residue 的负号来自 \(d\log v_3\) 经过前三个 coordinate：
\[
 \eta=-\frac{16\,d\log^3v}{\Phi(v_3-v_3^{-1})}.
\]
因此 \(\omega_\pm=\pm i\,d\log^3v/[2\sqrt{\Phi-64x}]\)。
分支值 \(i\alpha\)、\(i(2\pi-\alpha)\) 给
\[
 \log^+v_{3,+}\omega_+
 +\log^+v_{3,-}\omega_-
 =\frac{(\pi-\alpha)d\log^3v}{\sqrt{\Phi-64x}}.
\]
这里 lower log 的 \(2\pi i\) 是产生真实值的必要部分，不能丢掉。

## 3. Factor16 和真正绝对收敛

第四个 positive coordinate 的积分是
\[
 \frac1\Phi\int_0^\infty
     \frac{dv}{(v-\cos\alpha)^2+\sin^2\alpha}
 =\frac{\pi-\alpha}{\Phi\sin\alpha}.
\]
Reviewer 独立核对 arctan branch：
\(\arctan(-\cot\alpha)=\alpha-\pi/2\)，\(0<\alpha<\pi\)。
乘 \(\sqrt{x}\) 后正好得到稿中 \(W\) 的 \(1/16\) 倍 sheet density。
所以
\[
 \boxed{\nu_{\rm cut}=-16(2\pi i)^3W.}
\]

初稿只有 combined nonnegative-integrand 的 Tonelli argument；它本身不足以证明每张 sheet 的 absolute convergence。Reviewer 提出以下补强，作者已实际补入当前 final §4：
\[
 |\log^+v_{3,+}\omega_+|+|\log^+v_{3,-}\omega_-|
 =\frac{\pi\,d\log^3v}{\sqrt{\Phi-64x}}
 \le\frac{\pi}{\sqrt{1-x}}
       \frac{d\log^3v}{\sqrt\Phi}.
\]
三个 separated integrals 均为
\[
 \int_0^\infty\frac{dv}{\sqrt v(1+v)}=\pi .
\]
故 total absolute norm \(\le\pi^4/\sqrt{1-x}\)，而不依赖 sheets 之间的 cancellation。Exhaustion 顺序因此合法。

正实积分身份在整段 \(0<x<1\) 成立；\(W\) 在 \(|x|<1\) 的既有 analytic continuation 给这个 scalar 的唯一 analytic continuation。也可在 compact subinterval 上连续选两根和 log branch，通过同一 domination 核参数微分。于是
\[
 P_4\nu_{\rm cut}=-(2\pi i)^3\sqrt{x}.
\]

另一个可独立使用的小 lemma 是：两张 sheet 的 absolute integral 在 \(x\uparrow1\) 仍有 integrable majorant。写 \(v_j=e^{z_j}\)，则
\[
 \Phi=64\prod_{j<3}\cosh^2(z_j/2),\qquad
 \Phi-64=16|z|^2+O(|z|^4).
\]
因此中心附近 \(1/\sqrt{\Phi-64}=O(1/|z|)\) 在三实维可积；离开中心的尾部由 \(1/\sqrt\Phi\) 控制，integral 有限。
对 \(0<x\le1\)，\(\Phi-64x\ge\Phi-64\)，故 dominated convergence 还证明 analytic current integrals 的 finite boundary limit。**这不构造 singular-fibre current/cohomology class 或 regulator**。

## 4. 真实 tube 修正和 Tate factor

冻结实际 \(\Gamma\) period 是 \(-4i\pi^3y_0\)，tube period 是
\(8\pi^4y_0/\sqrt{x}\)。Reviewer 独立算得
\[
 \frac{(2\pi i)^4}{8}\int_\Gamma\omega
 =-8i\pi^7y_0,\qquad
 -16(2\pi i)^3W=128i\pi^3W.
\]
故
\[
 \nu_{\rm cut}+\frac{(2\pi i)^4}{8}\int_\Gamma\omega
 =-16(2\pi i)^3(W-\pi^4y_0/16)
 =-\frac{(2\pi i)^3}{8}\sqrt{x}
          \int_{8C-T\Gamma}\Omega_x.
\]
所有方向与 raw factors 相容。\(1/8\) 是 rational membrane coefficient；不能把它登记为一个未核实的 integral primitive lift。
采用冻结 conifold holomorphic identity，端点恰为
\[
 -(2\pi i)^3\pi^2(R_0-M_0).
\]
它是已定义 analytic period 的边界值，不是数值非零性或无理性结论。

## 5. KLM primary 的作用域与 compact gap

Reviewer 实际读 published KLM2006 的 PDF10–14、18–19：
[23页 primary](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，
SHA256 **8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9**，
397166 bytes。没有声称全文已读。

PDF10 §5.3 给 logarithmic current 与 delta terms；PDF11 §5.4 要求实际 multi-face / real good-position 条件。PDF12–13 §5.5–5.6 的普通 cohomology normalization 为
\((-2\pi i)^{p-n}\)，而 membrane term 为 \((2\pi i)^n\delta_\zeta\)（此处 \(n=4\) 为正号）。所以 \(p=n=4\) 时没有额外的 \(2\pi i\) 前因子，allowed rational-period change 是
\((2\pi i)^4\int_\gamma\omega\)。

PDF18–19 的实际 extension 和 comparison theorem 都要求已给 higher-Chow cycle / class；不能只凭一个 raw graph 当前式就认领满足这些条件。本稿 final §6 精确保留这一缺口。

尤其，family Chow **class** 唯一并不能确定 chosen precycle、Bloch homotopy、membrane 或一个普通 cohomology lift。Boundary pushforward 的 immediate type-vanishing 不消除 membrane 的 closed-period contribution。当前 proof 只解决 root 定义的 raw open current scalar 积分和旧 cube/tube 的相对周期身份。

## 6. 与独立 Yukawa 计算的兼容边界

本 reviewer 的独立 [Yukawa/scalar 稿](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)
从真实 node 的 PL intersection 计算 \(\kappa_{\rm raw}=-(2\pi i)^3/16\)，没有用这里的 current identity 反求该常数。
如果另一个 actual compact-current proof 给
\(\nabla_\theta r=+16\sqrt{x}\omega\)，则 scalarization 给
\[
 P_4Q_{\rm raw}(r,\omega)=-(2\pi i)^3\sqrt{x},
\]
与当前 (10) 完全一致。但相同 forcing 仍只消除到 homogeneous PF difference；本独审没有证明 compact lift 等于 \(\nu_{\rm cut}\) 或 \(\nu_{\rm corr}\)。

最终限定独审通过。本文无数学 producer、数值搜索、PSLQ 或 Lean 执行；被审 final 稿及本独审可在 root 回读后冻结。
