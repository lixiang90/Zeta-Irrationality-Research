# 同一配对饱和格全素数预算：独立全文审核

日期：2026-10-06。审阅者 /root/conifold_arithmetic_hypothesis。NEW 独立审核；所有旧/同行数学 producer 只读，没有执行、import 或重跑；本审核无自有数学 producer。

## R1. 实际阅读范围与精确指纹

实际完整读 research/cdt_odd_paired_all_prime_budget_20261006.md 初稿 98cf，随后完整读最终候选55278；代码、JSON和作者来源 receipt 均完整静态读取：

- MD：55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc。
- PY：research/cdt_odd_paired_all_prime_budget_verify_20261006.py，01b4970d7d634f2dc5376bce974d3755e7694c1f8a6defec68230aa86f784a95。
- JSON：research/cdt_odd_paired_all_prime_budget_verify_20261006.json，7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b。实际完整读 metadata 与全部50个有理 segment。
- 作者 receipt：literature/manifest_cdt_odd_paired_all_prime_budget_20261006.json，阅读时为候选状态、数学主稿 pin55278。不将作者来源阅读声明冒充我的独立阅读。

另外独立实际读 Lai 原件 PDF8–12 的五个完整页面：Lemma4.3 residue shift/秩/全minor证明、Lemma4.4 multilinear/Laplace 分配、PDF12 Lemma5.1 PNT test function。原件 literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf，SHA838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，URL https://arxiv.org/pdf/2610.06838v1。本审核无新下载。其他冻结数学输入作为明确的已证输入，不声称本轮又独立读了作者所列全部旧MD或全部25页Lai。

## R2. 同一格和全 finite-place 界

B2–B3 是同一 rank \(2n\) 饱和paired格、ambient degree \(<3n\)、原三重零点 \(B=6,\kappa=3,s=5\) 的 Newton determinant \(D_A\)。没有换quartic-zero或加first2n factorial normalizer。固定source分母 \(D^{2n}\) 和specialization分母 \(v^{2n}\) 都保留。

B4 的 entry valuation \(\ge-5\lfloor\log_p8n\rfloor\) 在整数值基上通过derivative lcm身份给出，size2n determinant得到 \(-10n\lfloor\log_p8n\rfloor\)，包括小p与小n。B5 对 \(p>6n\) 独立清除唯一 \(H_{2n+j}\) carry，不因pole指标6n就略过 \(6n<p\le8n\)。

large-prime 的tail entry \(i+j+w-5\)、head entry \(i+j+w-1\) 及tail rank2q给

\[
F_\rho(m)=m^2+(w_\rho-6)m+4(m-2q_\rho)^+
 +e_\rho{\bf1}_{m=1}.
\]

这是weight5的实际界，不是Lai weight4常数移植。\(e=1\) 只可能在 \(q=0,w=2\) 的type，前两个marginals同为2，所以凸性保持。将rho0 head rank弱化为2是合法较弱界。

multilinear/Laplace 给全部2n-minor共界 \(\Lambda_p\)。整数值到monomial的安全减项是

\[
2\sum_{i=n}^{3n-1}v_p(i!) ;
\]

在 \(p^2>8n\) 时用floor即可。最大2n项来自ambient degree3n，不能换成first2n。两次Cauchy–Binet与整数S保持全部形式X的Gauss valuation。B10取两个合法界的max，B11给signed common-content \(Q_n\)；positive信用保留，但不是actual primitive gcd。

## R3. 连续优化、端点与 exact certificate

B12 的资源 \(\int m=2/x\)、capacity2q+2、largest-factorial \(2\int_1^3\lfloor t/x\rfloor dt\) 与同一格匹配。integer-valued allocation在type内部可分配相邻整数，排序convex marginals给最小值，未把F任意延伸为fractional polynomial。

small x的feasible allocation满足 \(\lceil2/x\rceil\le2q_{\min}\)，且

\[
g_{\rm raw}(x)\le-4/x+2+x/4\le-223/16<-10
\quad(0<x\le1/4).
\]

因此cap后 \(g=-10\)，tail integral精确 \(-5/2\)。这是同一个D_A entry bound提供的合法cap，不把raw发散形状升级成actual cost下界。

静态核PY：base breaks \(1/j,2/j,3/j,6/j,8/j\) 覆盖floor变化和两个residue阈值交叉；type length affine且integer marginals排序固定；cumulative resource=2的根及cap-crossing显式加入。每段积分为有理精确式，47 base breaks/50 final segments/291 checks与程序逻辑一致。抽点assertion只核分支，全覆盖由break枚举证明。

末几段 [3,4]、[4,5]、[5,6] 的g分别 \(-2x-2\)、\(2x-18\)、\(12x-68\)，积分 \(-9,-9,-2\)，与所读JSON相符。完整segment表与声明

\[
\int_0^6g=-1085983123/24190320
\]

相容。审核没有运行脚本重算该和：纸面coverage和静态代码结构通过，作者首次exact certificate提供有理求和证据。

## R4. PNT接口与费用方向

在 \(x\in[1/4,6]\)，有限type、marginal和capacity uniform bounded。实际residue数与scaled length差O(1)，整数resource rounding只影响有界个cutoff marginals，给 \(\ell_p\ge n g(p/n)-O(1)\)。n>128保证该区间属于large-prime域；小n已由B4–11完整支付。

小素数费用o(n²)，中小区间entry cap付 \(5n^2/2+o(n^2)\)。PNT bounded piecewise continuous test-function normalization与独立所读Lai Lemma5.1吻合。O(1) valuation误差乘prime log sum仅O(n)，不改主率。作者新增coarse60依据正确：第一层 \(\theta(6n)\sim6n\)，更高层O(sqrt(n)log n)。

故B16的方向为

\[
\liminf n^{-2}\log Q_n\ge-A_{\rm pair}^{safe},\quad
A_{\rm pair}^{safe}=1085983123/24190320<44.894.
\]

这是同一对象安全费用上界；未压过解析估计不构成actual cost下界或no-go。

## R5. Plücker真实分母与局部GL

非零support必须含高层2n..3n-1，再选n个低层。每个Cauchy–Binet项确切factorial费 \(e_I+e_J\)，带actual \(v_p(u_I)+v_p(u_J)\)，所以

\[
v_p^{Gauss}D_A\ge\Lambda_p-2T_p,\quad
T_p=\max_{u_I\ne0}(e_I-v_p(u_I)).
\]

饱和性给每个p至少一个unit Plücker minor，配合support得到B19上下界。falling numerator整数GL保持full wedge的min valuation，故T_p有限位denominator解释正确。尚未优化的T_p率没有塞进B1，也没有重复扣root的primitive-pair \(-2\gamma\) 信用。

B20的 \(b_i=\binom t{i_0}\binom{(t^p-t)/p}{i_1}\)，\(i=i_0+pi_1<p^2\)，确为integer-valued。有限差分係数属Zp，leading比值

\[
i!/(i_0!\,i_1!\,p^{i_1})
\]

是unit，故为真GL3n(Zp)改基；转到原shift Newton基同样integer GL。B21的 \(\psi_p(a+pY)\equiv\psi_p(a)-Y\)、\(p\psi_p'\equiv-1\) 直接展开正确。degree只许完整layers加一个ragged layer，paired S须同步改基；限制均保留，没有从leading i1方向宣称未知全Smith费用。

## R6. 审核结论与未证项

最终55278全文纸面范围通过：全n、全素数、whole-coefficient signed content；capped continuous exact安全率；actual Plücker denominator refinement；真局部GL和leading范围。纸面证明、作者首次证书与审核静态检查各有准确范围。

仍未证T_p优化主率、完整局部Smith、无限辅助unit、同一D_A strict margin、新特殊值结果。审核没有拼接不同family。本审核保存后实际全文回读并冻结；作者只更新候选/冻结状态且主稿SHA不变时，对数学内容的审核精确有效。作者receipt状态另报；本审核不修改任何同行文件。
