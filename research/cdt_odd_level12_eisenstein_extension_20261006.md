# D12 完整 Eisenstein 扩展的辅助审计：odd–odd、真实周期与零 residue

日期：2026-10-06。本文是本轮辅助记录；正向主结果是已经root实际全文审阅冻结的[零周期整数校正族](cdt_odd_level12_zero_period_corrector_family_20261006.md)。本文不并入该主结果，不宣称新的无理性或已获得更大leaf。它保留完整真实primitive常数，不将未知L或π³任意作Galois共轭。

## 1. 实际 source空间与新方向

已证 \(\Gamma=\mathrm{PSL}\Gamma_1(12)\) 无torsion、genus0、10cusps。Riemann–Roch给
\(\dim M_4(\Gamma)=17,\dim S_4(\Gamma)=7,\dim E_4(\Gamma)=10\)。
这里17是完整modular source维数，不是17个已构造的Apéry targets。

\(\Gamma_0(12)/\Gamma=C_2\)只有even characters1、χ12。标准primitive-pair basis给Eisenstein的完整十方向：
六个 \(E_4(j\tau),j\mid12\)，\(E_\chi=E_4(1,\chi_{12})\)、\(F_\chi=E_4(\chi_{12},1)\)，以及此前未使用的
\[
A=E_4(\chi_{-3},\chi_{-4}),\qquad
B=E_4(\chi_{-4},\chi_{-3}).
\tag{1}
\]
采用q规范
\[
E_4(\alpha,\beta)=\sum_{n\ge1}\sum_{d\mid n}
\alpha(n/d)\beta(d)d^3q^n,\quad
L(E,s)=L(s,\alpha)L(s-3,\beta).
\tag{2}
\]
A、B的constant为0。两conductor乘积12，因此没有额外oldscale。primitive-pair/oldscale完备性与Fricke交换可核于[Young原论文](https://arxiv.org/pdf/1710.03624v2)，实际定向读取PDF pp3–6、27–28；本轮原件已保存literature。不能把Young的nonholomorphic规范直接当(2)的q-normalized规范。

odd characters的Gauss sums \(i\sqrt3,2i\)，结合q-normalization给
\[
A|_4W=\kappa B,\quad B|_4W=\kappa^{-1}A,\qquad
\boxed{\kappa=-8\sqrt3/9.}
\tag{3}
\]
也可由交换身份及 \(L(A,3),L(B,1)\) 的Mellin FE独立核：
\(\kappa=(6/\pi^2)L(A,3)/L(B,1)\)。W在十方向上有五个exchange pairs，所以scalar anti sector准确为5维；新anti方向为
\[
V_o^-=A+8\sqrt3B/9,\qquad V_o^+=\sigma V_o^-=A-8\sqrt3B/9.
\tag{4}
\]

## 2. 新方向是实际实π³周期，不能误删

真实critical值是
\[
\begin{array}{c|cc}
&L(1)&L(3)\\ \hline
A&-\pi/(6\sqrt3)&2\pi^3/(81\sqrt3)\\
B&-\pi/18&\pi^3/96 .
\end{array}
\]
两者L2均为0。因此
\[
\Theta_o:=L(V_o^-,3)=17\sqrt3\pi^3/972,\quad
L(V_o^-,1)=-6\Theta_o/\pi^2,
\]
\[
L(V_o^+,3)=-\sqrt3\pi^3/972,\quad
L(V_o^+,1)=6L(V_o^+,3)/\pi^2 .
\tag{5}
\]
这是real critical π³，不是纯虚π³加realL的平凡无理性。若某个实际实组合
\(L(3,\chi_{12})+\nu\pi^3\) 被假定有理，则相应primitive减去其假代数常数仍可能成为算术germ；π³已知超越并不自动使这个模型非法。单个这样的组合无理，也不能推出纯L无理或完整三项线性无关。

## 3. canonical M的真实carrier，与formal σ不同

写
\[
f_A=\sum_{m\ge1}\frac{\chi_{-3}(m)}{m^3}\frac{q^m}{1+q^{2m}},
\quad
f_B=\sum_{m\ge1}\frac{\chi_{-4}(m)}{m^3}\frac{q^m}{1+q^m+q^{2m}}.
\tag{6}
\]
在canonical \(\rho_7^2=e^{4\pi i/7}\)，两kernels没有pole，有限phase统一有界，\(m^{-3}\)支配保证actual radial limit。取K4、K3分别为 \(x/(1+x^2)\)、\(x/(1+x+x^2)\)在 \(\mathbf Q[x]/(x^7-1)\) 中的代表；它们reciprocal系数对称。有限Gauss/B3 Fourier给
\[
f_A(\rho_7^2)/(\sqrt3\pi^3)=-478/11907,\quad
f_B(\rho_7^2)/\pi^3=269/4704.
\]
所以
\[
\boxed{f_{V_o^+}(\rho_7^2)=-619\sqrt3\pi^3/6804.}
\tag{7}
\]
\(\sigma\)只作用source系数，故(7)是actualσsource的值，不是未知period的Galois共轭。其formal \(\sigma\Theta_o=-119\sqrt3\pi^3/6804\)，差为
\(-125\sqrt3\pi^3/1701\)。\(V_o^+\) 是M-anti，\(M=\gamma W,\gamma=(7,2;24,7)\)，χ12(7)=-1；同一点的原source值 \(509\sqrt3\pi^3/47628\) 不能冒称原source的M周期。

对完整W-anti旧源 \(aG_1+bG_2+cG_3+dC^-\)，∞正则与ζ3-free给
\[
c=-99a-9b,\qquad d=(66a+b)/23.
\tag{8}
\]
加入 \(eV_o^-\)，其中 \(a,b,e\in K=\mathbf Q(\sqrt3)\subset\mathbf R\)。canonicalσsource的imaginary Tate项为
\((28164\sigma a+2434\sigma b)i\pi^3/483\)；odd方向不贡献imaginary Tate。
若实际original carrier ξ在K，且进一步要求canonical M实际carrier准确等于σξ，则imaginary part强制旧方向为 \(uF_L\)，u在K。于是
\[
\xi=u\Theta+17e\sqrt3\pi^3/972,\quad
\lambda=-\sigma u\,\Theta-619\sigma e\,\sqrt3\pi^3/6804.
\]
若u非零且 \(\lambda=\sigma\xi\)，消掉actualL给一个algebraic数等于
\[
\frac{\sqrt3\pi^3}{6804}
[119(\sigma u/u)e-619\sigma e].
\]
π³超越迫括号为0；若e非零，令z=e/u，则 \(\sigma z/z=119/619\)，再作σ迫 \((119/619)^2=1\)，矛盾。所以e=0。u=0时非零ξ是known critical π³，已非代数。

准确结论：这个canonical paired scalar carrier接口不能容纳nonzero odd–odd方向。它没有证明real mixed value无理，也没有排除第二embedding采用较小或ramified map。q-disk上的σarithmetical germ仍是合法基础输入，缺的是足够强的共同解析/算术矛盾。

## 4. 十cusp constants与extra-zero必要条件

odd-pair的support准确为 gcd(c,12)=4或3。若actualscaling第一列(a,c)，先将a/c写成正分母，令 \(a^\flat=a\operatorname{sgn}c\)。于是
\[
\operatorname{const}(A|_4S_{a/c})=
\begin{cases}23i\sqrt3\,\chi_{-4}(a^\flat)/81&(c,12)=4\\0&\text{其它},\end{cases}
\]
\[
\operatorname{const}(B|_4S_{a/c})=
\begin{cases}23i\,\chi_{-3}(a^\flat)/128&(c,12)=3\\0&\text{其它}.\end{cases}
\tag{9}
\]
负denominator不能漏掉odd-character sign。本新证书用实际十scalings核完整十方向的constant matrix rank10；不是从几个cusp样例推所有slots。

(9)可直接由primitive kernel residue核：在q接近四阶根，A primitive的pole为
\(i\chi_{-4}(a^\flat)L(4,\chi_{12})/(2\epsilon)\)；三阶根B的pole为
\(i\chi_{-3}(a^\flat)L(4,\chi_{12})/(\sqrt3\epsilon)\)。
再用θ³及det1scaling得(9)，\(L(4,\chi_{12})=23\pi^4/(1296\sqrt3)\)。

旧ζ-free real family在c2、c4的常数为
\[
B_2=\frac{16}{9}(6a+b),\quad
B_4=(1566a+151b)/9,\quad
B_6=-9B_2,\quad B_3=-9B_4/16.
\tag{10}
\]
旧常数real，新odd常数imaginary；realK系数无法让它们互相取消。故odd方向并未自动多给一个可填cusp。

两份actual pure-L residue-zero source是
\[
(a,b,c,d)=(23,-138,-1035,60),\quad
(3473,-36018,-19665,8400).
\tag{11}
\]
第一份杀c2/c6，第二份杀c3/c4。但Bol residue为0仅使parabolicaffine作用有fixedline，不使真实原点位于该line。

第一份在q=-1的实际primitiveendpoint为Θ，θprimitive值为
\[
\theta_q f(-1)=3180\zeta(2)\ne0 .
\]
这是wholefamily有限式 \((7362a+697b)\zeta(2)/23\)。在cusp -1/2的width6规范，相应constant paraboliccorrection为 \(-6360i\pi^3\)，仍非零。第二份在q=i的actualendpoint为
\[
f(i)=\Theta+10330i\pi^3\ne\Theta,
\]
来自wholefamily系数 \((17274a+1349b)/1104\)。所以(11)没有产生新的filled leaf。本文未从standard representative非zero排除zero-residue类的所有conjugates。

## 5. 正向接口：零周期corrector与剩余cuspidal条件

(8)中d=0准确给新的zero-period rational
\(R=G_1-66G_2+495G_3\)。它不引入未知critical cusp-period；已在独立主稿闭合全整数source/reflection族，保留pureL目标与两embedding实际算术germ。主稿的完整 signed eigline证明优先于本辅助维数讨论。

七个cuspidal方向的boundary全部为0。因此加cuspidal source不能修已有非零cusp constant，但可以改变(11)在zero-residue cusps的lower-degree correction。要保留原pureL实际period，至少还要实际核 \(L(C,3)=0\) 及相应Fricke pairing；要杀第一份的paraboliccorrection，还需实际critical additive值 \(f_C(-1)=0\)、\(\theta_qf_C(-1)=-3180\zeta(2)\)。它们不是仅对q系数的rational线性约束。本文没有构造算术cuspidal corrector，也没有将任意complex解算作K系数source或新oddL结论。

全Γ下降更不由加cuspidalforms自动实现。若nonzero holomorphicweight4源的q-regularEichlerprimitive在全Γ有zero correction，则所有cuspscalings的polynomial部分被parabolicperiodicity迫成constant，primitive为全部cusps全纯的weight−2 modularform，必为0，与源非零矛盾。这个negative-weight事实不排thin stabilizer或只填部分cusps的leaf。

## 6. 新证书、文献与准确review scope

同名NEW verify.py执行记录为三次：第一21checks通过，但未assert的odd-character负denominator槽方向修正；第二保存修正后的21checks；第三加入完整boundary rank与两个新residue-zero/corrector接口，40checks通过。未执行/import旧producer，无研究参数扫描。

conjugate_projection实际只读当前NEW PY/JSON，独立核odd-pair κ、L1/L2/L3、ρ7² endpoint及finitephase支配limit通过；未运行证书，未审本文全部cusp slots、boundary rank、correctorfamily或本MD全文。本文仅记录该实际范围，不登记成全稿已独审。主correctorfamily已另外获得root实际全文MD/PY审阅并冻结。

Young v2原件37页、SHA与actual定向阅读页记于本轮独立manifest。本文仍为auxiliary，未把17维source讨论并入核心无理性输出。

