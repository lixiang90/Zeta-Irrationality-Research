# Hasse 关系进入固定原格：level20 的一变量全局秩界改进

日期：2026-10-06。本文把 [Hasse 最高分母层关系](cdt_odd_level20_hasse_20261006.md) 接入 CDT 的原始一变量 Taylor 评价格。结果是两个限定、实际系统的全局算术秩界改进；没有证明 L(3,χ₅) 无理，也没有把一变量常数代入 balanced tensor 定理。

核心区别是：改变源格所产生的指数与高度改进相抵消；在**固定原格**上发现原评价矩阵的 Smith 整除性，则能够改进原来的粗高度上界。独立局部证明见 [桥梁稿](cdt_odd_level20_hasse_smith_bridge_20261006.md)。本文补齐其 leading-order 覆盖与完整 D² 记账。

## 1. 实际闭合系统与统一消失阶界

令 K=Q(r)、r²=5、c=L(3,χ₅)。反证假设 c∈Q。使用 [完整模型 §§5–8](cdt_odd_level20_model_20261006.md) 的实际函数 H=H₋，并令 g=Δ²、ϑ=t∂ₜ。以下每个原点芽均为实际解析函数，其系数在 K 中；不对未知周期自行施加 Galois 共轭。

第一个元组是
\[
\mathcal F_4=(1,gH,g\vartheta H,g\vartheta^2H).
\tag{1}
\]
它在 K(t) 上独立且导数闭合。原稿给实际最小齐次阶4与三阶非齐次式
\[
H'''+a_2H''+a_1H'+a_0H=U\ne0,\qquad a_i,U\in K(t).
\]
这将 H''' 写成前三个导数与1的有理组合；ϑ 与 ∂ 的三角转换，以及同时乘固定非零 g，均保持上述性质。特别不能把 raw companion 矩阵误称为简单极点的 Fuchsian gauge。

第二个元组是
\[
\mathcal F_7=(1,L,T_2,K_2,gH,g\vartheta H,g\vartheta^2H),
\quad L=-\log(1-t),\quad T_2=L^2/2.
\tag{2}
\]
K₂ 取已审阅的完整 LCM² 规范。其一阶式是
\[
K_2'=\frac{K_2}{2(1-t)}+\frac{L}{t(1-t)}.
\]
L'=1/(1-t)、T₂'=L/(1-t)，因此(2)导数闭合。背景只含 trivial/sign 因子，目标的实际商是不可约 rank3；[算术稿](cdt_odd_level20_arithmetic_20261006.md)的交空间论证证明实际 rank 恰7。

CDT 固定 v2 第52页 Theorem3.2.8 对独立、导数闭合的 rank m 系统给出：degree≤D 的多项式评价空间共有 R=m(D+1) 个消失阶跳点，且
\[
V_D\subset\{0,\ldots,m(D+1)+C_m\},\qquad \#V_D=R.
\tag{3}
\]
定理的 Shidlovsky 证明在特征零常数域上成立，故对 K(t) 同样适用；数域归一化按 CDT Remark8.2.42 及原算术稿的限定闭合系统接口处理。这里 C_m 为固定常数，无须求出它的数值。源格的非零有理缩放不改变 K-线性消失旗标。

取 N_D=m(D+1)+C_m+1。于是所有跳点严格小于 N_D，且
\[
\sum_{n\in V_D}n=\frac{m^2}{2}D^2+O(D).
\tag{4}
\]
这比只知道某个固定 jet 满秩更强：它覆盖所有 D 的整个实际 primitive Taylor 旗标。

## 2. 固定原格上的 Smith 余量

对好素理想 𝔭∣p，取 p>√N_D；固定规范与 c 的分母只排除有限个 p。原 Hasse 稿证明，对所有指数 n<N_D<p²，p³H 的最高 packet 等于 A(t)F(tᵖ)，且三目标行有两个 k[t]-独立关系 v₀、v₁，系数次数
\[
\delta_p\le(3p+9)/2.
\]
三行同时乘 g 不改变关系的系数次数。D≥δ_p 时，其次数≤D−δ_p 的多项式倍数给至少
\[
s_{p,D}=2(D-\delta_p+1)
\tag{5}
\]
个独立模𝔭核方向。核方向只占三目标 source blocks，其余 blocks 取0。

使用下面第3节所列的**原 CDT 源格**，并只在 √N_D<p≤D 的窗口取上述改进。在此窗口，p³eval_{<N_D} 在整个源格上积分，原逐项粗 bound 恰为每个跳点3log Norm(𝔭)。若 mod𝔭 rank≤R−s，primitive saturated Taylor 旗标可取 GL_R(O_{K,𝔭}) 中的适配基。由全部 leading jets 选出的矩阵为三角矩阵、对角非零；Smith 标准形给其 determinant valuation≥s。因此
\[
\sum_{n\in V_D}h_{\mathfrak p}(\psi_D^{(n)})
\le(3R-s_{p,D})\log\operatorname{Norm}(\mathfrak p).
\tag{6}
\]
该计算保持 source lattice、source degree 与 archimedean metrics 不变。局部适配基仅用于评价行列式，不用于建立新的全局 polynomial basis；因此没有遗漏 CRT representatives 的系数高度。

归一化求和时，对未分歧的每个好 p 有
\([K:Q]^{-1}\sum_{\mathfrak p\mid p}\log\operatorname{Norm}(\mathfrak p)=\log p\)。
保守收益是
\[
G_D=\sum_{p>\sqrt{N_D},\ p\ {\rm good}}
(2D-3p-7)_+\log p
=\left(\frac23+o(1)\right)D^2.
\tag{7}
\]
最后一步来自 PNT：θ(X)=X+o(X)、Σ_{p≤X}p logp=X²/2+o(X²)，取 X=2D/3。去掉 p≤√N_D 的损失为 O(D^{3/2})，固定坏 p 与常数7的损失均为 o(D²)。这是收益项的损失；原有限高度估计中的小素数、高幂及坏素数全部保留。

## 3. 两个原源格与全部素数的高度账本

记 ℓ_x=lcm(1,…,⌊x⌋)。按照 CDT (7.3.6)，将 Laurent sections 乘 tᴰ识别为 degree≤D polynomials，同时携带原 O(1)_φ 的 L² metric。

对(1)，原系数格为
\[
E_{4,D}=\ell_D^{-3}O_K[t]_{\le D}\oplus
O_K[t]_{\le D}^{\oplus3}.
\tag{8}
\]
对(2)，三个单位尺度列从第2、第3、第5行开启，u=(1,2,4)、y=u；原系数格为
\[
\begin{split}
E_{7,D}={}&(\ell_D\ell_{2D}\ell_{4D})^{-1}O_K[t]_{\le D}
\oplus(\ell_{2D}\ell_{4D})^{-1}O_K[t]_{\le D}\\
&\oplus\ell_{4D}^{-1}O_K[t]_{\le D}^{\oplus2}
\oplus O_K[t]_{\le D}^{\oplus3}.
\end{split}
\tag{9}
\]
没有引入新格Λ。背景安全型分别为1、ℓ_n、ℓ_n²、ℓ_n²，三个目标的安全型是固定 D_c ℓ_n³；Euler 导数与整数系数的 g 保持该型。固定 D_c 在累计高度中贡献 O(D)，高幂素数仍由全部 LCM 估计处理。

在窗口 √N_D<p≤D，(8)的常数 block 有 valuation−3；(9)的四背景 blocks 的 source valuations依次为−3、−2、−1、−1，配合函数的安全型均使完整 p³ jet 积分。这正是(6)所需的同一原格，不能用另一张分母表的 source 替代。

对全部 p，CDT (7.3.10)的粗估计经 PNT 与(3)给
\[
\begin{array}{c|c|c}
 &\text{原有限高度和的 }D^2\text{ 系数}&\text{扣除(7)后}\hline
m=4&3\int_0^4\max(s,1)ds=51/2&149/6\\
m=7&\sum_{u=1,2,4}\int_0^7\max(s,u)ds=84&250/3.
\end{array}
\tag{10}
\]
这些是**累计评价高度**上界。未声称每个 n 都改进，也未清掉尚未控制的第二、第三分母层。p>D、p≤√N_D 及有限坏 p 均保留原完整上界，只有已经证明的窗口扣除 G_D。

## 4. 数域平均的解析侧与源 degree

对两个 embedding 分别取实际共同叶上的合法 φ_σ，圆盘内拉回函数亚纯且 φ_σ(0)=0、φ_σ'(0)≠0。固定有限 poles 可按 CDT 第103页脚注29先径向缩小并清除，最后取极限。令
\[
\bar\rho=\frac1{[K:Q]}\sum_\sigma\log|\varphi_\sigma'(0)|,
\qquad
\bar J=\frac1{[K:Q]}\sum_\sigma
\iint_{\mathbb T^2}\log|\varphi_\sigma(z)-\varphi_\sigma(w)|\,d\mu(z)d\mu(w).
\tag{11}
\]
先在边界正则的径向限制上使用公式；其极限按原 CDT 处理。固定原 metrics 与 Hilbert–Samuel 给
\[
\widehat{\deg}E_{4,D}=(2\bar J+3)D^2+o(D^2),
\quad
\widehat{\deg}E_{7,D}=(7\bar J/2+21)D^2+o(D^2).
\tag{12}
\]
CDT (7.3.9)及(4)给
\[
\sum_{n\in V_D}h_\infty(\psi_D^{(n)})
\le\left(-\frac{m^2}{2}\bar\rho+m\bar J\right)D^2+o(D^2).
\tag{13}
\]
这里的函数已知 holonomic 且实际导数闭合，所以直接使用 Theorem3.2.8；无需把原文用来先推出 holonomicity 的条件 log|φ'(0)|>σ_m 当作已满足。所用评价/HS/斜率证明本身仍成立。

## 5. 已闭合的特殊秩界

将(10)、(12)、(13)代入 Bost 斜率不等式后取 D² 主项，得到
\[
\boxed{4\bar\rho-\bar J\le131/12}
\quad\Longleftrightarrow\quad
\boxed{4(\bar\rho-131/48)\le\bar J},
\tag{14}
\]
以及
\[
\boxed{7\bar\rho-\bar J\le374/21}
\quad\Longleftrightarrow\quad
\boxed{7(\bar\rho-374/147)\le\bar J}.
\tag{15}
\]
这是针对(1)、(2)及其固定原 source 的特殊全局界。相应有效成本从45/16降到131/48（下降1/12），从18/7降到374/147（下降4/147）。它们不是任意 denominator array 的新通用 τ 公式。

若括号中分母为正，可写成熟悉的 m≤J/(ρ−τ) 形式；(14)–(15)的线性形式无须这一附加条件。它们依赖反证假设 c∈Q，但实际 rank 与 closed-system 输入均已由真实周期模型证明。

## 6. 为什么仍无数值矛盾，以及下一项实质工作

普通 Bost–Charles numerator 满足 J≥ρ（Jensen）；当前真实共同叶的原点唯一原像并省略 cusp1 给 ρ≤log16。因此(14)若要产生矛盾，必要条件是ρ>131/36；(15)的必要条件是ρ>187/63。这两个数都严格大于 log16。对应已审阅的凸性方案也有自身 floor，不能只把普通 J 的新成本换进其它未核的公式。

这一比较明确表明：最高分母层已经提供了真实的一变量收益，但仍需更多收益。下面6.1已把 Beukers 原证明推广到本模型零阶3的规范，补齐有界次数的 modp³ 商与第二层整除性；第三层与 balanced tensor 兼容性仍是下一步。固定换基保留三层的旧结论不排除随 p 变化的局部输入，但局部输入必须像本文一样接到实际 source 与全局高度。

### 6.1. 已补齐的 excellent lift 与第二层收益

后续 [Frobenius 稿 §§1–4](cdt_odd_level20_frobenius_20261006.md) 已重证所需比值输入，并经独立复核。它不直接套用 Beukers r≤1 的定理：采用实际 eta-product Φ=B/[t(1−t)]，唯一零轨道的阶是3；保留完整 characteristic-polynomial 系数 G_p(t)，得到
\[
\Phi(t)/\Phi(t_p^{Fr}(t))\equiv G_p(t)\pmod{p^3},
\qquad\deg G_p\le3p.
\]
关键是 eta norm 使多项式 monic，根之和中的 p² 权重与完整 Fourier trace 的 p 因子相乘给模p³；Gp是完整系数，不是 degree<p 截断。

该稿结合真实 θ_q/t 链式法则，给 (H,ϑH,ϑ²H) 上的一个二阶 polynomial row L₂，其次数≤6p+13，且前 N_D<p² 项满足
\[
p^3L_2H\in p^2O_{K,\mathfrak p}[[t]]/(t^{N_D}).
\]
其最高坐标为 D₁D₀²，mod𝔭非零。因此 degree≤D 的原 source 中，L₂ 的多项式倍数提供至少
\[
k_{2,p,D}=(D-6p-12)_+
\]
个 mod𝔭 独立整向量，其 Ψ=p³eval 的像被p²整除。旧 Hasse 两行仍提供 k₁≥(2D−3p−7)_+ 个向量，其像被p整除。

两组不要求彼此独立。对原 leading minor 的 Smith exponents a_i≥0，向量条件分别给
\[
\#\{a_i\ge1\}\ge k_1,\qquad
\#\{a_i\ge2\}\ge k_2,
\quad\sum_i a_i\ge k_1+k_2.
\tag{16}
\]
这按两个不同阈值计量；第二组已经落在第一层核中，只额外扣一层，不重复扣2k₂。

同一素数窗口的额外主项是
\[
\sum_{p>\sqrt{N_D}}(D-6p-12)_+\log p
=\left(\frac1{12}+o(1)\right)D^2.
\]
所以总收益从2D²/3提升到3D²/4。保持(8)–(13)的原 source、所有小/坏素数上界和 arch metrics 后，得到更强的限定全局界
\[
\boxed{4(\bar\rho-87/32)\le\bar J},\qquad
\boxed{7(\bar\rho-249/98)\le\bar J}.
\tag{17}
\]
其有限高度主项分别为99/4与333/4。这将两个元组的有效成本进一步降到87/32、249/98。

结合 J≥ρ，必要尺度分别是ρ>29/8、ρ>83/28；二者仍大于 log16。因此(17)也没有产生数值矛盾。尚未获得第三层或 balanced tensor 版收益；不将新算子的特征p关系计作额外特征零函数。

### 6.2. 曲率保证的平方提升降低第二层次数

[平方提升稿](cdt_odd_level20_square_lift_20261006.md)及[独立审阅](cdt_odd_level20_squarelift_review_20261006.md)给出新的全素数输入。对完整 G_p，曲率恒等式在全有理函数意义下给
\[
2G_p\vartheta^2G_p-(\vartheta G_p)^2
+2hG_p\vartheta G_p+\mathcal T G_p^2\equiv0\pmod{p^2}.
\]
其中 h=ϑlog((1−t)√Δ)，𝒯 的分母在 generic Hasse 根处为 unit。写 G_p modp=B_p F_p²，F_p 是 squarefree double-root 部分，b=degB_p≤4、2degF_p+b=3(p−1)。取整数 lifts 后，曲率的 linearization 与 monic p-saturation 推出误差除p后被F_p整除。于是存在 p-integral polynomials β_p、η_p，满足
\[
G_p\equiv\beta_p\eta_p^2\pmod{p^2},\qquad
\deg\eta_p=\deg F_p,\quad\deg\beta_p\le b+3\le7.
\]
本段 F_p 是多项式因子，不是 source packet；不要求 β_p 在模p²下仍整除 Δ。

用 ϑlog(Rβ_pη_p²) 替换原 a₀=ϑlog(RG_p)，二者模p²一致，故完整 integral prefix 上的第二层消除保持。清分母改用 D₀,new=NCβ_pη_p；其二阶 row 的次数不超过3p+20，而最高坐标 D₁D₀,new² 模p非零。故同一原 source 中的第二层方向至少为
\[
k_{2,new,p,D}=(D-3p-19)_+.
\]
相对于(16)只替换 k₂；k₁不变，两个 Smith 阈值的计数允许重叠。新第二层主项为
\[
\sum_{p>\sqrt{N_D}}(D-3p-19)_+\log p
=\left(\frac16+o(1)\right)D^2.
\]
所以总收益为5D²/6。所有 p>D、小素数、固定坏素数、高幂、原 source degree 和 arch metrics 仍按(8)–(13)保留。原累计有限高度主项分别降为
\[
51/2-5/6=74/3,\qquad84-5/6=499/6.
\]
同一斜率不等式给更强的限定全局界
\[
\boxed{4(\bar\rho-65/24)\le\bar J},\qquad
\boxed{7(\bar\rho-373/147)\le\bar J}.\tag{18}
\]
结合 J≥ρ，所需必要尺度仍为ρ>65/18、ρ>373/126，均超过log16。因此次数下降提供了真实收益，但仍未证明L(3,χ₅)无理。

[自然第三层审查](cdt_odd_level20_third_layer_20261006.md)及[其审阅](cdt_odd_level20_third_layer_review_20261006.md)说明：第三次 connection 组合约掉原 Bol 方程和既有 constant 方向后，target coefficients 共同含恰好p²。primitive 除p²后只保证第一层，不能当作新的第三层 Smith 方向。这个限定结果没有排除其它构造；[固定原源格的收益上限](cdt_odd_level20_fixed_source_ceiling_20261006.md)也不能从当前账本推出绝对排除。

未证明新的 ζ/L 奇数值无理性、未新增 Lean 形式化。下面6.3已补齐第八节near-balanced、列明e=0数组的Smith兼容；它不自动覆盖第六节exact-balanced或任意新filter。目标保持active。本稿的全尺度证据是各节数学论证与原始定理，固定素数执行证书仅用于各自明确的代数和截断核查。

### 6.3. 第八节近似均衡张量接口已闭合

[独立张量桥](cdt_odd_level20_balanced_smith_bridge_20261006.md)回到CDT第129页实际整数source，而不是将本稿分母缩放source直接张量。令R=m(D+1)，p³评价矩阵的certified floors为b_i≤3，E是full tensor内codimension c的primitive近似均衡子模。对其实际leading minor，有

\[
 v(\det B)\ge dR^{d-1}\sum_i b_i-3dc.
\]

这是逐Smith阈值与saturated intersection的全尺度结论；局部SNF不需要保持species。full tensor leading set为V_D^d，故实际balanced leading rows适用该引理。epsilon-thick species的比例趋于1，codimension损失在d→∞消失；exact-balanced species没有这一性质。

在p≤(1−δ)D的严格内窗，原flat transport的cap与pure source背景floors完全接合。累计finite高度的归一收益是γ/m，而最终有效成本下降2γ/m²。因此(18)的65/24、373/147现也可进入第八节原Bost–Charles与列明convexity numerator。新metric情形保留它自己的HS degree，不沿用J/2。一般e=0 fractional数组需要存在零行并核theta-matching窗口，不能无条件替换τ。

[积分型接口](cdt_odd_level20_integrated_tensor_bridge_20261006.md)另给必须先固定cutoffξ的ei>0扩展，正文审阅后再作为其限定范围内的证据；不把已经minimized的τsharp与另一ξ的收益拼接。[既定三族的乐观门槛](cdt_odd_level20_post_smith_budget_20261006.md)说明，即使信用全部γ，原13/14/15维背景族的普通Jensen必要尺度仍≥14/5>log16。

[通用二阶次数障碍](cdt_odd_level20_universal_s2_20261006.md)与[同一Gp的modp³平方提升障碍](cdt_odd_level20_squarelift_modp3_obstruction_20261006.md)进一步限定可继续使用的构造范围，但不排特殊packet、原flag或其它真正primitive高层输入。[大素数净收益稿](cdt_odd_level20_large_prime_net_20261006.md)证明末端三层成本已等于原基线；[四个完整Taylor矩阵](cdt_odd_level20_large_prime_smith_probe_20261006.md)的唯一有限收益只是固定宽度边界，未给新D²主项。

## 7. 原始来源与复核

CDT [固定 v2 原件](../literature/cdt2024_l2_chi_minus3.pdf)：第52页 Theorem3.2.8，第94–103页 primitive quotient metrics、source (7.3.6)、HS 与 heights，第94页 §7.2 的数域说明及第143页 Remark8.2.42。Hasse 局部输入的原始 Katz/Beukers 文献见 [Hasse稿](cdt_odd_level20_hasse_20261006.md)。

helper_tensor_budget 与 low_period_closure 已分别独立核对原格/换格区别、Shidlovsky入口、数域归一及 D² 常数；[独立审阅](cdt_odd_level20_hasse_smith_audit_20261006.md) 覆盖本稿 §§1–5 的实际正文。[Frobenius 与两层 Smith 审阅](cdt_odd_level20_frobenius_review_20261006.md)另独立核对6.1的 weighted Smith 阈值、次数与全局主项。Frobenius稿的全形式一阶障碍不参与本稿(17)的证明。
