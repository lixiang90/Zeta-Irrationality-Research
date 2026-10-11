# R0 相对周期与 mirror 商：限定范围独立审阅

日期：2026-10-06。实际全文阅读新稿 `cdt_odd_R0_relative_cycle_mirror_20261006.md`，纸面独立核算其 §§2–9，并检查 §§4、9–12 的结论边界。没有执行、导入或修改任何数学 producer；以下不是 Lean 验证，也没有数值无理性结论。

## 1. 相对 pair 与真正的闭链

设 \(F=1-x\prod(1-u_j^2)\)、\(U=\mathbb A^4\setminus\{F=0\}\)，边界 \(D=\bigcup_j\{u_j=\pm1\}\)。在 \(D\) 上 \(F=1\)，故这个边界确实与 divisor 分离。八个 faces 的非空交集都是 affine spaces，交集 nerve 是四个 \(S^0\) 的 join，即 \(S^3\)。相应 Mayer–Vietoris / MHS 计算给 \(H^3(D)=\mathbb Q(0)\)、\(H^4(D)=0\)。

平滑 \(U\) 的 \(H^3(U)\) weights 至少为 3，因此 strictness 令 \(H^3(U)\to H^3(D)\) 为零；localization 于 affine ambient 给 \(H^4(U)=H^3(V)(-1)\)。所以作者的

\[
0\to\mathbb Q(0)\to H^4(U,D)\to H^3(V)(-1)\to0
\]

通过。这里无需假设 \(H^3(U)=0\) 或 \(H^2(V)=0\)，也不把完整 \(H^3(V)\) 预设为四维。全 cube \(C=[-1,1]^4\) 的十六个 octants 按字符加权恢复 ambient positive orientation；内部零 faces 相消，而真正边界落在 \(D\)。它给实际 integral relative chain，非 absolute closed chain。

## 2. 三个 contour、留数与 tube 的完整常数

对固定 \(0<x<1\)，三个 ccw 椭圆可取得足够靠近线段 \([-1,1]\)，使 \(x|\prod_{j<3}(1-u_j^2)|<1\)。各 \(\sqrt{1-u_j^2}\) 围绕两个零点后单值；选 upper shore 为正，则 lower shore 为负。ccw upper shore 的方向是 \(1\to-1\)，因此

\[
\oint_\gamma\frac{(1-u^2)^n\,du}{\sqrt{1-u^2}}
=-2\int_{-1}^1(1-u^2)^{n-1/2}\,du
=-2\pi\frac{(1/2)_n}{n!}.
\]

端点 contribution 可积且趋零。所给 graph

\[
u_3=\frac{i\sqrt{1-xT}}{\sqrt{x}\prod_{j<3}\sqrt{1-u_j^2}},\qquad T=\prod_{j<3}(1-u_j^2)
\]

是 divisor 上实际 compact closed three-torus；坐标全有限且 \(u_3\ne0\)。以 \(\Omega=dF/F\wedge\eta\) 为约定，\(F_{u_3}=2xu_3T\) 与 \(du_3\wedge du_0du_1du_2=-du_0du_1du_2du_3\) 给

\[
\eta=-\frac{du_0du_1du_2}{2xu_3T}
=\frac{i\,du_0du_1du_2}{2\sqrt{x}\prod_{j<3}\sqrt{1-u_j^2}\sqrt{1-xT}}.
\]

一致收敛 binomial series 可逐项积分，故 \(\int_\Gamma\eta=-4i\pi^3y_0/\sqrt{x}\)。将 normal \(F\)-circle 的 ccw 方向放在三环面前面，Leray tube 给 \(2\pi i\int_\Gamma\eta\)，因而准确为

\[
\sqrt{x}\int_{T\Gamma}\Omega=+8\pi^4y_0.
\]

与 \(\int_C\Omega=16B\) 合并：\(8C-T\Gamma\) 是 integral relative cycle，其周期是 \(128(W-\pi^4y_0/16)\)，conifold limit 是 \(8\pi^2(R_0-M_0)\)。三个 contour 的负号、留数的负号和 tube 的 \(2\pi i\) 均保留，C1–C3 通过。

## 3. Mirror function field、raw residue 与 Euler quotient

作者的 degree-64 计算可直接核对：\(r_j^2=(1+u_j)/(1-u_j)\) 给 16 个初选；closure 的未平方条件 \(\prod(r_j+r_j^{-1})=(2\psi)^4\) 保留恰 8 个；在 \(Y_0=1\) 的 patch 内其余三个 \(Y_j\) 的平方根再给 8 个。generic nonzero-coordinate 点的 projective stabilizer 只有已商去的 diagonal。于是 actual function-field quotient 的 degree 是 64，cube parameter 为 \(x=\psi^8\)，primary 的 native normalized parameter 是 \(1/x\)。

raw residue 的 Jacobian 与符号独立核算如下。在作者指定 ambient order 中

\[
\mu_7=-\frac{dr_0dr_1dr_2dr_3db_1db_2db_3}{8r_1r_2r_3},
\quad \det\frac{\partial(P_0,P_1,P_2)}{\partial(b_1,b_2,b_3)}=(-c)^3,
\quad P_3=r_0(S-c^4)/c^3.
\]

两处负号抵消，给 raw \(\omega_M=\operatorname{Res}_{Q=0}(dr_0\cdots dr_3/[8\prod r_jQ])\)。又 \(p^*\Omega=256dr_0\cdots dr_3/[\prod r_jQ(S+c^4)]\)，在 \(Q=0\) 上 \(S+c^4=2c^4\)。尺度故为 \(1024/c^4=64/\psi^4\)，乘 \(\sqrt{x}=\psi^4\) 后为 64。没有把 primary 另乘 \((2\psi)^4\) 的 form normalization 混进这个 raw 计算。

even-sign subgroup quotient 的 degree 8 与 \(w^2=t_0t_1t_2\prod_{i=0}^2(1-t_i)(1-xT)\) 通过。其留数 \(dt_0dt_1dt_2/(16xz)=-dt_0dt_1dt_2/(16\kappa w)\)、\(\kappa^2=-x\) 与前述 convention 一致。

## 4. Toric symbol 与准确的缺口

代换 \(v_j=(1+u_j)/(1-u_j)\) 给 \(A=256/\phi\)、\(\Omega=16\,d\log v_0\cdots d\log v_3/(\phi-256x)\)。正 orthant 积分和 \(B(0)=1\) 的归一化准确。

任一 boundary divisorial valuation 的 center 上，compact equation 强制至少一个不同 coordinate 满足 \(a_k+b_k=0\)，故 \(v_k\) 为 unit 且 residue 是 \(-1\)。将这个 unit 移至 Milnor symbol 首位，tame residue 含有 \(\{-1\}\) 因子；其 2-torsion 在 rational coefficients 下消失。center 在 torus 时所有 coordinates 为 units，同样无 residue。因此作者的全部 divisorial unramified \(K_4^M\otimes\mathbb Q\) 命题通过。

每个 facet polynomial 含 repeated factor \((v_j+1)^2\)，所以不 Δ-regular。这个严格障碍与强 tame vanishing 同时成立；不能由后一项直接套用需要 regularity 的 n=4 motivic completion 定理。unramified Milnor class 也不能直接代替 global higher-Chow lift 或消灭其 \(d_2\)。

认可作者明确保留的限制：period 全纯不证明 full relative Betti class monodromy invariant；affine quotient 不给 compact integral saturation；实际 cube/tube 也不自动识别一个 \(CH^4(X,4)\) regulator。compact pure-sector 的标记与 relative extension 全整格仍是下一项工作。

## 5. 实际 primary 阅读范围

本审阅另实际提取并阅读 BKΣZ 本地原件 PDF **16–17、19**，确认 family、group、generic nodes、quotient resolution、native parameter 与 Eq. (2.40) 的 normalization。实际提取并阅读 Doran–Kerr published 本地原件 PDF **48–50、53、55–56**：Definition 3.1–3.2、Theorem 3.1 的 n=4 条件，以及 completion spectral sequence 的 \(\ker d_1\cap\ker d_2\) 和 totally-real \(K_3^{\rm ind}\otimes\mathbb Q\) 使用范围，均与作者的限定相符。

不认领其余 primary 页码或 Deligne 原件的实际阅读；relative MHS 部分按上述独立数学计算及标准 smooth-variety weight / strictness 输入审核。以上为纸面限定独审，不以全文读 Markdown 代替全部 primary source 阅读。
