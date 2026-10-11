# 实际配对格的对偶 Plücker 内容与镜像 carry 秩亏

日期：2026-10-06。NEW 数学稿，root，尚待独审。所有旧及同行程序只读，不 execute/import/rerun。本文给同一 actual rank2n 配对格的有限位定理及安全费用改善；不证明无限辅助非零或新的特殊值无理性。

## D1. 同一对象与主结果

实际读取冻结 [整数格稿](cdt_odd_paired_head_free_integral_lattice_20261006.md) 全部 I1–I10（公式 I1–I25），SHA `5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b`；冻结 [全素数稿](cdt_odd_paired_all_prime_budget_20261006.md) 全部 B2–B22，SHA `55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc`；原50段 JSON只读，不执行其来源。

保持 f_i(t)=binom(t−1,i)、ambient degree<3n、B6/k3/s5、actual saturated rank2n基。令

\[
b_j=\binom{6n+j}{j-1},\quad m'=2n+1-m,\quad
\beta_m=\gcd(b_m,b_{m'}),\quad
p_m=b_m/\beta_m,\quad q_m=b_{m'}/\beta_m.
\tag{D1}
\]

取 G_m=p_m L_m+q_m L_{m'}、m1..n，以及 f_i、2n≤i<3n；S为其Newton系数矩阵。对真正非零 maximal minors u_I=detS_I，冻结B17的实际分母是

\[
T_p=\max_{u_I\ne0}\left\{\sum_{i\in I}v_p(i!)-v_p(u_I)\right\}.
\tag{D2}
\]

本文证明任意n、任意prime p的准确对偶式；在 n<p≤2n、p>8 的窗口完全算出其 Smith 层和T_p，从而把同一D_A全素数安全费用改善为

\[
\boxed{A_{\rm dual}^{safe}
=\frac{1085983123}{24190320}-\frac{1718}{15015}
=\frac{14081798807}{314474160}\in(44.778,44.779).}
\tag{D3}
\]

改善1718/15015是主率真收益，不是单个辅助素数的O(nlogn)信用；仍不足以匹配解析界。D3只应用本稿的Plücker改善，不预先借另一同行尚待独审的weak-block改善。

## D2. Complementary minors给准确对偶内容

令 A 为 S 的低2n×n块；高n×n块是identity，其他交块为0。primitive满射约束 C:Z^{2n}→Z^n 的第m行是

\[
C_{m,j}=q_m\binom{m-1}{j}-p_m\binom{m'-1}{j},
\quad0\le j<2n.
\tag{D4}
\]

连续节点evaluation的unimodularity及每pair gcd1，说明C满射、kernel A完整饱和。把A加一个整数complement成为GL_{2n}(Z)，或直接取primitive exterior Hodge star，得任意n-subset I⊂{0,…,2n−1}的

\[
\det A_I=\pm\det C_{I^c}.
\tag{D5}
\]

理由不依赖Euclidean范数：row wedge C和star(column wedge A)位于同一一维有理空间，二者全部坐标gcd均1，因此比例只能±1。具体subset的orientation符号不影响valuation。

定义整数矩阵

\[
C^!=C\operatorname{diag}(j!)_{j=0}^{2n-1},\qquad
\delta_p=v_p(I_n(C^!))
=\min_{|J|=n}\left\{\sum_{j\in J}v_p(j!)+v_p\det C_J\right\},
\tag{D6}
\]

I_n为全部n-minors生成的非零整数理想。实际非零S-minors必须含全部high indices2n..3n−1，所以D5直接给全prime exact identity

\[
\boxed{T_p=\sum_{i=0}^{3n-1}v_p(i!)-\delta_p.}
\tag{D7}
\]

这准确计算了冻结B17中的同一个weighted wedge。没有把Γ再次除入finite content，没有改变格，也没有让unimodular real norm免费成为1。

## D3. 第一Smith层的真实residue图

C^!的第m行第j项是

\[
q_m(m-1)_{\underline j}-p_m(m'-1)_{\underline j}.
\tag{D8}
\]

模p时j≥p的falling产品在每个整数点皆为0；j0..p−1的falling基与monomial基为unitriangular，全部p节点上的评价矩阵可逆。若p>2n，只需distinct节点0..2n−1的degree<2n插值，仍可逆。

因此任意prime p有准确的rank identity

\[
\operatorname{rank}_{\mathbf F_p}(C^!\bmod p)
=\operatorname{rank}_{\mathbf F_p}\mathcal R_p,
\qquad (\mathcal R_p)_m=q_m e_{m-1\bmod p}-p_m e_{m'-1\bmod p},
\tag{D9}
\]

e_r是p节点function坐标。这是primitive带权镜像图，不是忽略carry的unweighted graph。第一层给δ_p≥n−rankR_p，不能一般把它升级成全部Smith层。

当p>n，0≤v_p(j!)≤1、j<2n。因为C满射，

\[
p\mathbf Z_p^n\subseteq C^!\mathbf Z_p^{2n}\subseteq\mathbf Z_p^n.
\tag{D10}
\]

第一包含来自diag(j!)Z_p^{2n}⊃pZ_p^{2n}。所以C^!的所有n个Smith valuations确为0或1，且

\[
\boxed{\delta_p=n-\operatorname{rank}\mathcal R_p\quad(p>n).}
\tag{D11}
\]

这是全部层的精确结论。p≤n时可能有valuation2及以上，D11不在那里使用。

## D4. n<p≤2n窗口的carry权重精确归一化

再设p>8。p为奇数，p²>8n；取N=6n+1、N=hp+e、0≤e<p。写实际节点j=k+1、k=lp+r、l∈{0,1}、0≤r<p。Legendre/Wilson给

\[
v_p(d_j)=h+c(r),\quad
c(r)=\mathbf1_{r+e\ge p},\quad d_j=(j)_N,
\]
\[
U_l(r):=p^{-h-c(r)}d_{lp+r+1}\bmod p
=(-1)^{h+c(r)}\frac{(l+h+c(r))!}{l!}
\frac{(r+e-c(r)p)!}{r!},
\tag{D12}
\]

所有阶乘指标<p，故units；这里用vp(A!)=floor(A/p)，其去p单位部分为(−1)^q q! R!，A=qp+R<p²。

从d_j除共同N!得到b_j，不改变pair的relative primitive条件。特别

\[
U_1(r)=(h+c(r)+1)U_0(r).
\tag{D13}
\]

在该窗口h∈{3,4,5}；粗界h≤6也足够，因为h+c+1≤8<p−1，对p≥11成立。故h+c与(h+c+1)²−1均为p-unit。

## D5. 双边块、中心loop与准确秩亏

令H=2n−p−1≥0。H为偶数且H<n−1。实际k0..2n−1的镜像是k'=p+H−k，residue反射r↦H−r modp。

- r0..H有两个lifts r、r+p。对r<s=H−r，有两条actual pair约束，forming一个两节点、两row块。
- r>H仅有一个lift；residue pair不同，只有一row，primitive gcd确保rank1。
- r=H/2为一个中心loop，actual sites r与r+p。

两row块中，若c(r)≠c(s)，primitive约除后两row都仅在carry较大一侧有一个unit coefficient，rank为1。若c(r)=c(s)=c，row-unit缩放及D13给块

\[
\begin{pmatrix}
(h+c+1)U_0(s)&-U_0(r)\\
-U_0(s)&(h+c+1)U_0(r)
\end{pmatrix},
\tag{D14}
\]

det=[(h+c+1)²−1]U_0(r)U_0(s)为unit，rank2。中心loop是(h+c)U_0(r)的unit倍，rank1。不同residue blocks互不相交，所以总rank亏只来自carry不同的双row块。

阈值τ=p−e。r<s=H−r的lower r范围0..H/2−1，carry不同恰r<τ≤H−r。精确计数及D11给

\[
\boxed{\delta_p=
\max\{0,\min(\tau,H+1-\tau,H/2)\},
\quad n<p\le2n,\ p>8.}
\tag{D15}
\]

H=0时只有中心loop，公式仍给0。e=0时τ=p>H，亦给0。无任何无穷unit、OP normality或实际form非零假设。

## D6. 同一Gauss模型中的真实改进

冻结B18给v_p^{Gauss}D_A≥Λ_p−2T_p，并可与全entry界−10n取max。n<p≤2n时，Σ_{i=0}^{n−1}vp(i!)=0，故D7精确给

\[
T_p=T_p^{safe}-\delta_p,
\qquad T_p^{safe}=\sum_{i=n}^{3n-1}v_p(i!).
\tag{D16}
\]

因此可定义新的全prime bound：在D15窗口用

\[
\ell_p^{dual}=\max\{-10n,\Lambda_p-2T_p^{safe}+2\delta_p\},
\tag{D17}
\]

其余prime用冻结B10/小prime/largeprime界。所有n、全部形式X系数都有D_A(X)/Q_n^{dual}∈Z[X]，Q_n^{dual}=∏p p^{ℓ_p^{dual}}。此处只把D15证明的actual weighted minor整除算入费用，不把它称实际D_A content equality。

## D7. 三个tent的全尺度极限与cap兑现

令x=p/n∈(1,2)、h_x=floor(6/x)。D15直接给

\[
\delta_p=n d(p/n)+O(1),\qquad
d(x)=\max\{0,\min((h_x+1)x-6,8-(h_x+2)x,1-x/2)\}.
\tag{D18}
\]

误差uniform：h=floor((6n+1)/p)=h_x时三项只差−1、+1、−1/2；max/min为1-Lipschitz。唯一h变化发生p|6n+1，此时δ=0，h_x=h−1，而d≤(h_x+1)x−6=1/n，误差仍≤1。无需丢一个未付的大例外prime。

三个nonzero tents为h=5,4,3，端点、共同交点与高度是

\[
a_h=6/(h+1),\quad z_h=14/(2h+3),\quad b_h=8/(h+2),
\quad d(z_h)=2(h-2)/(2h+3).
\tag{D19}
\]

第三项1−x/2只在峰点与两条直线相交；tent内部d是上升(h+1)x−6或下降8−(h+2)x。冻结B14真实50段表在这些支撑上的old raw为：h5时4x−12>−10；h4时−10；h3时−2x−8。故前两个真实gain恰2d；第三个即使加2d，仍≤−3x−6<−10，**被entry cap全部遮蔽，不计收益**。

三角面积给已付主率改善

\[
\int_1^2(g_{dual}-g_{old})dx
=2\int_{a_5}^{b_5}d+2\int_{a_4}^{b_4}d
=\frac6{91}+\frac8{165}
=\frac{1718}{15015}.
\tag{D20}
\]

原continuous LP到真实Λ、factorial的uniform O(1)误差由冻结B15支付；加入D18仍只增加O(1)。bounded piecewise affine gain的PNT测试函数论证给

\[
\liminf n^{-2}\log Q_n^{dual}\ge-A_{dual}^{safe}.
\tag{D21}
\]

窗口外费用保持原合法界，small n或small primes不被D15覆盖时亦用原全n界。因此D21没有仅prime-window的遗漏。D3和D21只证明更便宜的安全费用，未证明det的无限非零或strict margin。

## D8. 一手来源与更高层整模型的适用界线

正常TLS新归档 [Bhargava2009原件](../literature/bhargava2009_p_orderings_integer_valued_ultrametric_20261006.pdf)，31页408017bytes，SHA `cf66a3058ad9612019dcd9eda8bc1f26f9951c876b3e699d16bdd6b199c93f2e`，原始 [AMS PDF](https://www.ams.org/journals/jams/2009-22-04/S0894-0347-09-00638-9/S0894-0347-09-00638-9.pdf)。实际读PDF1–4及7–11，共9完整页面，UTF-8输出无截断；不是全文31页。

所读Theorem7及3.1.2区分普通integer-valued、divided-difference-integral子环与global regular basis的条件。它提供开展更高jet整格的框架；不直接计算我们的paired constraint Smith。D4–D21已独立由primitive满射、Wilson、整数图和PNT证明，不借Bhargava替代。换成导数整性更强的子环可能更便宜地表示jet，但同时改变实际格，须支付global index和解析基增长；不能只保留局部好处。

## D9. 自有首次程序及有限证据范围

1. NEW `cdt_odd_paired_dual_plucker_layers_20261006_probe.py` 首次仅一次，成功。n1..18、每个√8n<p≤3n，共105案例；exact Fraction DVR消元独立计算primal与dual maximal-minor理想，静态JSON同时保存所有Smith valuations与graph rank。其minimum-valuation pivot的row/column clear系数属Z_p，所以累计pivot valuations确为determinantal ideal。未import旧/同行源。
2. NEW `cdt_odd_paired_dual_plucker_carry_rate_20261006_verify.py` 首次一次，失败：42有限formula comparisons及三tent exact integrals assertions已过，但最后猜测小数窗口(44.779,44.780)错误。实际值低于44.779，**无JSON，不记PASS**；原源码保留不改、不重跑。
3. 单独 NEW `cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.py` 首次一次成功。只纠正最终窗口为(44.778,44.779)并准确登记失败历史；相同42有限接口和exact tent/cap算法未改。它仅读已存probe JSON为data，不execute/import其source，输出exact D3与D20。

root数学执行合计3、成功2失败1；旧/同行execute/import/rerun0、Lean0。所有输出存在guard。有限probe和certificate不是全尺度D5/D9/D10/D15/PNT证明；纸面证明分别在本稿中。程序与已有JSON实际静态回读，不重跑。

## D10. 未补的实际目标

已完成：actual weighted Plücker的全prime对偶内容；第一层residue graph；p>n全Smith层0/1；n<p≤2n,p>8的精确carry秩亏和主率1718/15015收益。剩余p≤n更高Smith层仍可从相同满射的weighted columns及jet图入手，但不能假定D11在那里成立。

当前安全费用界位于(44.778,44.779)，而已证解析率仍远低于这个界；未形成strict margin，不是actual费用下界。无限辅助Padé normality也未证。新的ζ/L/Catalan无理性/线性无关性结论仍未取得。下一步应推进更多prime windows真实层和same-object相容收益，避免将有限低n表、普通OP perfectness或仅换基当成无限结论。
