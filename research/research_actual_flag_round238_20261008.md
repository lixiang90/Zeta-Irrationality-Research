# 第238轮：真实源的全阶过滤已确定，下一关限定为算术费用

2026-10-08。238是结构性进展；目标保持active，**尚未得到新的ζ/L值无理性或线性无关性定理**。本轮完成236–237指定的实际过滤行列式接口，足够保留路线到239，但不因此延长参数或格扫描。用户本轮再次要求每4–8轮全局俯瞰，已保存[复盘规则](research_global_review_policy.md)：默认6轮，上一236、下一242，窗口240–244；240另有明确继续/停止检查。

## 1. 保留真实数值目标

源仍为
\[
f=(1,F,b_gJ_g),\quad F=uE,\quad
E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
S=\sqrt{1-4u},\quad I'=E/S,\ I(0)=0,\quad
J_g=S(g-2I).
\]
233–234已付的canonical连接值将真实填点参数绑定为
\[
g_0=2I(1/4)=t
=\frac52L(2,\chi_{-3})-\frac{\pi\log3}{3\sqrt3}.
\tag{1}
\]
本轮沿用该真实身份，没有替换为任意generic参数或另一个Clausen值。以下实解析证明固定这个实数g₀；算术应用在假设g₀∈Q下，取固定正整数b_g使b_gg₀∈Z。正moment结论未外推到所有g∈Q或全部transported叶。

## 2. 全尺度单射：正moment与正确的外cut

令a=atanh(1/2)，可由正双积分换元得到
\[
\frac{J_{g_0}(u)}{1-4u}
=\int_0^3\frac{w_R(x)}{1-ux}\,dx,\qquad
w_R(x)=\frac{\operatorname{atanh}(\sqrt{4-x}/2)-a}
{\sqrt3\sqrt x\sqrt{4-x}}>0.
\tag{2}
\]
它是整个原生芽恒等式，故包含全部系数，且直接证明u=1/4解析填点。置
\[
d\mu=\frac{dx}{2\sqrt{3x}},\quad
v=2\sqrt{4-x}\{\operatorname{atanh}(\sqrt{4-x}/2)-a\},\quad
\mu_k=\frac{3^k}{2k+1},\quad \nu_k=\int_0^3x^kv\,d\mu.
\]
于是F的第n≥1项为μₙ₋₁，J_(g₀)的第n≥1项为−νₙ₋₁，而J_(g₀)(0)=g₀。两种measure均正，但不能仅据此断言mixed square determinant非零。

在C∖((−∞,0]∪[4,∞))选原生branch，upper lip满足
\[
\Im v_+(x)=-\pi\sqrt{4-x}\ (x<0),\qquad
\Im v_+(x)=+2a\sqrt{x-4}\ (x>4).
\tag{3}
\]
Root起初把右cut的根号符号取反；两条独立审阅发现并纠正，撤回“临界方阵必非零”的更强提案。实际ρ=−Im(v₊)/π左正右负，标准恒号Nikishin perfectness不能直接套用。

保留正确符号后有自足零数引理：非零H=A+Bv，deg A,deg B≤m−1，在(0,3)最多2m个零，按重数计。若有2m+1个，令Z为这些零的monic奇次多项式。H/Z去掉内点极点，沿两外cut的contour给
\[
\int_{(-\infty,0)\cup(4,\infty)}
\frac{x^kB(x)\rho(x)}{Z(x)}dx=0\quad(0\le k<m).
\]
∞处H/Z=O(z⁻ᵐ⁻³ᐟ²)，0处仅log、4处至多sqrt，全部大弧、小弧及尾积分受控。取多项式B的线性组合得到∫B²ρ/Z=0；但奇次Z在左负右正，使ρ/Z两侧均严格负，矛盾。B=0则用多项式零数。这只付2m上界，没有付2m−1。

现在m=D+1，消去常数函数的前m行并分别反序F/J的列后，完整tail矩阵为
\[
K_m[r,j]=\mu_{r+j},\quad
K_m[r,m+j]=-\nu_{r+j},\qquad
0\le r\le2m,\quad0\le j<m.
\tag{4}
\]
若其2m列相关，就有非零H与x⁰,…,x²ᵐ在正μ下全正交；标准变号点多项式论证迫使至少2m+1个内变号，违反零数引理。因此
\[
\boxed{\operatorname{rank}K_m=2m,\qquad
\operatorname{rank}T_{3D+3}=3(D+1)\quad\text{对全部 }D\ge0.}
\tag{5}
\]
完整source的所有实际vanishing jumps都不超过3D+3。此处是全阶证明，不是有限头测试或未知O(1)常数。

## 3. 实际过滤恰漏一行，费用子式不能任选

定义δₕ=det(K_m删去第h行)，0≤h≤2m，并取
\[
h_* =\max\{h:\delta_h\ne0\}.
\]
其signed cofactor vector是唯一left relation。最后非零位置h_*就是greedy row flag唯一依赖行；此前各行独立，此后各行增加秩。前m行的μ Hankel block正定，故m≤h_*≤2m。得到
\[
\boxed{V_D=\{0,\ldots,3m\}\setminus\{m+h_*\},\qquad
\det T_{V_D}=\pm b_g^m\delta_{h_*}.}
\tag{6}
\]
由237的同格、同度量、普通rank-one graded target精确传递公式，
\[
\boxed{\mathcal A_D=-m\log b_g-\log|\delta_{h_*}|.}
\tag{7}
\]
h_*按最大非零**下标**选择，不能换成最大绝对值cofactor。Cauchy–Binet的Σδₕ²>0也不能为这个选中项提供所需下界。未证明δ₂ₘ全阶非零，因此未领取临界0,…,3D+2方阵的perfectness。

独审另给真实费用的小下界：在[0,3]取monic shifted Chebyshev，分别变换两组columns，并变换所选rows。缺失行h_*是此前rows的组合，所以该实际minor在monic row变换下不变。行列degrees总和3m²−h_*，Hadamard给
\[
|\delta_{h_*}|\le(3/4)^{3m^2-h_*}\exp(O(m\log m)),\quad
\mathcal A_D\ge3\log(4/3)D^2-O_{g_0}(D\log D).
\tag{8}
\]
它是费用lower，远未排除严格预算，也不是所需upper。

## 4. 大局判断与有界下一步

238解决的是“使用哪个真实完整行列式”；仍未解决“有理假设下该行列式的完整算术费用是否足够小”。236的安全CRT upper为45/4，237证明仅换同源整数格不能改变精确内在费用。故继续盲目放大格或增加有限样本不缩小剩余缺口。

239只攻一个命题：为实际δ_(h*)构造完整有限处证书；若不知道h_*，则统一覆盖h∈[m,2m]。例如给正整数Q_m、C_m，使
\[
Q_m b_g^m\delta_h\in C_m\mathbb Z,
\qquad
\kappa_\delta=\limsup\frac{\log Q_m-\log C_m}{D^2}
\]
得到选中非零项的费用upper。证书必须包含全部素数幂与固定b_g例外；C_m须是真实同一余子式的整数content，不能借另一格或另选minor的节省。只控制实处大小、generic多项式非零或局部一批素数不够。

基本BC矛盾最终需要同一合法图上的3λ>J+2a/3，其中a为实际费用的limsup upper。既有共同图cap C*=3π³√2/8、J≥λ，只给必要窗口a<3log C*；这不是任意新度量的通用no-go。239不同时重开图、能量或参数搜索。

240执行继续/停止检查，必要时提前正式复盘：若仍只有秩、局部节省或不足的safe upper，未打开上述必要窗口，就停止此源的继续优化。只有明确费用改进跨过必要门槛并提供合法图能量接口，才有界继续到242。安全upper不足只决定投入取舍，不被宣传为费用lower或不可能定理。

后备固定M₀,₁₀路线本轮也作准入检查：标准对偶同余看不见全部五个禁止坐标；同F的另一个收敛边界形式可精确积分为ζ₃，说明一般Gauss–Manin存在性本身不保证六通道投影。它不反驳指定ω；原族仍欠一份含边界与motivic坐标的具体relative reduction/全n投影证书。换到更深几何也必须先付这个接口，不能以理论名称代替数值出口。详见[后备审阅](cellular_uniform_projection_gate_round238_20261008.md)。

## 5. 验证边界

Root完整读取238 Packet、独审、后备稿，并逐式纸核(2)–(8)的换元、cut符号、contour衰减、变号论证、pivot及Chebyshev实际缺行变换。另两名代理独立建立核心证明；最终报告再作全文审阅。独审的所有g安全截止不是本报告核心依赖。原canonical数值身份沿用233–234，未重新认证全部特殊值或全球新颖性。

本轮数学程序、素数/参数扫描、新保存PDF、Git修改和Lean构建均0；来源查阅和文档归档不是数值验证。完整证明见[Packet稿](actual_flag_determinant_round238_20261008.md)与[独审稿](actual_flag_independent_round238_20261008.md)，实际读域另存literature/actual_flag_sources_round238_20261008。本轮不是正式全局复盘，不重置236的计数。
