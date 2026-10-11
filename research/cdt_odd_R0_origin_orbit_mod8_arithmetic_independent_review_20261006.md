# 全路径模8障碍的独立审阅：周期符号、轨道与共同CDT域

日期：2026-10-06。NEW 独立纸面审阅。对象是 [NEW模8主稿](cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md)，实际全文读取M1–M17及scope，最终SHA a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc。没有执行/import/rerun旧或同行数学producer，也没有创建数学producer。

审阅结论：指定对象和范围全部通过。特别，全部实际路径与origin二维MUM旗标不相交；完整paired九行的CDT盘上亚纯条件自动对参数共同适用。它不是任意新ratio或额外period的共用域定理。

## I1. 整数矩阵与全部word，而不是有限搜索

实际轨道格的交叉式 \((8/3)(k^3+2k)\) 在k=0,1,2,3分别为0、8、32、88，因此主稿给定orientation下PL第一行是 \((1,-8,-32,-88)\)。逐column求和得 \(\ell U=\ell\)；\(M_1-I\)平方为0，inverse的第一行为 \((1,8,32,88)\)。故 \(\ell M_1^{\pm1}\equiv\ell\pmod8\)，physical \(M_0^{\pm1}=-U^{\pm1}\)只改变符号。

从actual \(\ell(\delta)=1\)逐letter应用得到每个正负physical word的 \(\ell(\gamma\delta)\equiv\pm1\pmod8\)。Signed群得到1。此证明涵盖任意长度，不涉及枚举；两generator及inverse都保持actual轨道格。用 \(z\cdot\Gamma_V=8\ell(z)\)重写为交叉数模64等于±8，尺度一致。

## I2. Physical、signed与period map方向实际核验

本轮实际另读冻结 [轨道格稿](cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md) O24–O25及周边：period若恒零，则与四个cyclic de Rham forms配对为零，扇区非退化迫cycle为零；所以actual period map是四维同构。\(2\Gamma_V=(-1,3,-3,1)\)、\(\Gamma_V\cdot z=-8\ell(z)\)及\(N^3=w\ell\)归一化一致。

实际另核 [real Betti稿](cdt_odd_R0_real_Betti_normalization_20261006.md) physical/signed段，及本轮主报告对应记录：\(\eta=\omega/\sqrt x\) single-valued，actual cycles origin transport为M0，P-period continuation为 \(\chi(\gamma)h_{\gamma z}\)。因此P的origin matrix是U=−M0，actual sqrt-cover是M0²=U²。Plane整体乘χ不改变plane；采用inverse-action convention时inverse仍在同一群，且flag须同步转换。主稿M11没有把scalar transport与cycle transport误认。

\(h_\delta=-\pi^2v\)、\(v\in P_c\)给actual cycle line在Pc内；这是冻结node归一化，不需要g2的Betti coordinates为代数。M14符号由
\(C(y_0,h_z)=-\ell(z)\)及 \(v=-h_\delta/\pi^2\)得
\(C(y_0,\operatorname{cont}_\gamma v)=\chi(\gamma)\ell(\gamma\delta)/\pi^2\)。

## I3. 全部路径、cover及线性输出

SingleJ4唯一N-stable二维plane是 \(\ker N^2\subset\ker N^3=\ker\ell\)。若γPc等于该plane，其含有的γδ line将使 \(\ell(\gamma\delta)=0\)，与I1矛盾。改参考路径的η只将word换为η⁻¹γ；有限algebraic cover只限制fundamental-group subgroup，origin logarithm乘非零ramification index不改kernel。Ordinary ramification不引入新的period monodromy。M13因而真正涵盖全部实际路径及finite covers。

已冻结exterior E20.3、E22、E30本轮实际再读。Origin odd local loop的χ quotient eigenvalue−1，even loop固定decomposable wedge则其plane稳定；M13使两种都不能fixed，并保证jump有非零primitive quotient。冻结holonomy H2–H4的connected evaluation-kernel lemma于是覆盖所有transported origin上的非零algebraic linear row。没有把它免费推广到非线性。

## I4. 定理3的disk-loop证明与all-place费用

假设一个q*的完整paired tuple经holomorphic φ拉回为meromorphic。φ的origin-value preimage即t=1处有有限positive ramification，上一项立即排除。所以φ避免1；holomorphic φ无∞preimage，若改为meromorphic maps则E22排除其poles。

Closed-disk neighborhood上的nonconstant φ，其conifold preimages在闭盘中有限。到每个preimage的arrival word由φ路径决定，与q无关。q*的local fixed tuple强制 \(v\in\gamma P_c\)；E20.3遂给每个q实际holomorphic extension。Punctured disk的fundamental group由这些small loops生成，全部q在每个generator fixed，于是整盘single-valued。Open-disk版本逐compact exhaustion，每个loop落入某个finite-puncture subdisk，同样成立。Boundary integral及radial limits不由此自动产生，主稿保持其独立条件，准确。

每个embedding逐一应用，选定map即使依赖actualq，也已经是q=0可用的同一个map。费用只是复用已冻结完整模型：same actual \(L=K(\sqrt2)\)、所有σ及normalized weights、scale \(\rho=(7/2)\log2\)、rank10、\(\tau=329/50\)、小p多项式与fixed εspecies均不变化。因此M17由真实q=0 reference强制，不是toy常数例。

## I5. 阅读、来源与边界

本轮实际全文读取模8主稿final a510；实际补读轨道O24–O25、real Betti physical/signed关键段、exterior E8–E13全段与holonomy H1–H4；主报告 §§85–93及delivery metadata已实际读。旧轨道/real Betti其它段的先前独审不冒认本轮又全文读。没有新增primary PDF下载；本轮Singer关键页阅读属于另行非线性研究，不是本审阅赖以新增的几何输入。

同余仅属于实际word群，不属于完整Sp4(Z)或所有non-flat比較矩阵；它与Sp4 Zariski density不矛盾。结论只对指定当前packet建立共同解析域；没有新的特殊值无理性、超越性或Lean定理。审阅为纸面全尺度核验，不是数学producer、finite sampling或作者自审。
