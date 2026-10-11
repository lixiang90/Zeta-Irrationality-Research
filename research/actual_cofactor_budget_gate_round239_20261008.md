# 第239轮：实际余子式费用的紧全图门槛与同BC校准

2026-10-08，Alternative/A。数学程序0。本轮的全尺度算术改进有效，但
\(\kappa_{\rm safe}=21/2-\log12\)仍不能给当前源的同一固定BC证书类带来严格矛盾。
关键是重新利用234留下的精确覆盖式，而不是把旧的粗导数upper当成可达到的图。
以下结论是投入停止门槛；没有证明实际费用等于这个safe upper，更没有新的数值无理性定理。

## 1. 保持同一actual flag和费用

仅在真实目标
\[
g_0=\mathfrak t=\frac52L(2,\chi_{-3})
-\frac{\pi\log3}{3\sqrt3}\in\mathbb Q
\]
的反证假设下，固定正整数\(b_g\)使\(b_gg_0\in\mathbb Z\)。完整源为
\[
f=(1,F,b_gJ_{g_0}),\quad F=uE,\quad
E=\frac{\operatorname{atanh}\sqrt{3u}}{\sqrt{3u}},\quad
J_g=\sqrt{1-4u}\,(g-2I),\quad I'=E/\sqrt{1-4u}.
\]
它的实际\(\mathbb Q(u)\)-rank为3。令\(m=D+1\)。238支付的完整原生jet
\(0,\ldots,3m\)单射，以及
\[
V_D=\{0,\ldots,3m\}\setminus\{m+h_*\},\qquad
h_*=\max\{h:\delta_h\ne0\},\quad m\le h_*\le2m.
\]
因而同一标准多项式源格的精确有限处费用为
\[
\mathcal A_D=-\log|\det T_{V_D}|
=-m\log b_g-\log|\delta_{h_*}|.                 \tag{B1}
\]
不能将\(\delta_{h_*}\)改成绝对值最大的余子式、平方和或generic目标的minor。
238的非零和Chebyshev实处小量分别支付评价单射和费用lower，均不提供费用upper。

239独立算术稿对全部候选hole和全部prime powers证明
\[
\limsup_{D\to\infty}\mathcal A_D/D^2
\le\kappa_{\rm safe}:=\frac{21}{2}-\log12.       \tag{B2}
\]
这里已实际FULL读其冻结11139B版本的A1–A25；本稿采用它的同对象算术输入，
不以本稿的解析比较代替该稿的局部证明或另一份独审。
一般可用的整数证书是
\(Q_m b_g^m\delta_h\in C_m\mathbb Z\)，其中\(Q_m,C_m>0\)且包括全部prime、
幂、固定\(g\)头；若对所有候选h成立，则actual非零给
\(\mathcal A_D\le\log Q_m-\log C_m\)。只清某一tail或只取得某几个prime的content不够。

## 2. 固定共同BC度量的rank-one校准

下面的\(s\)表示函数源rank，避免与余子式尺寸\(m=D+1\)混淆。固定一个
single-variable rank-\(s\)源、标准完整多项式系数格和目标graded格\(\mathbb Z\)；
假设已付其评价单射及实际jumps覆盖\(sD+O(1)\)。固定有限个合法共同图
\(\phi_j\)，\(\phi_j(0)=0,\ \phi_j'(0)\ne0\)，所有species pullback在整盘亚纯。
固定一个所有species共用的半正BC line metric \(\mathcal L\)；
允许已付CDT §7.6的固定非负凸组合，但度量、图和权重均不随D变化。

记
\[
\lambda_j=\log|\phi_j'(0)|,\quad
\lambda_*=\max_j\lambda_j,\quad
J=\mathcal L^2,\quad K_j=\mathcal L\cdot\mathcal L_j.
\]
这里要求同一度量的arithmetic Hilbert–Samuel式及uniform evaluation heights确实适用：
\[
\widehat{\deg}L_D=\frac{s}{2}JD^2+o(D^2),\qquad
h_\infty^{(\nu)}\le-\nu\lambda_j+DK_j+o(D),    \tag{B3}
\]
后一误差对\(\nu=O(D)\)一致。CDT Lemma7.4.1及其§7.6线性推广提供这个接口；
它不是对任意新度量的无条件断言。开放盘图先作固定径向缩图、清有限pole，
应用闭盘/邻域估计，再在D极限后取径向极限。未以任意点态边界值代替可适用的BC度量。

定义
\[
B(t)=\min_j\{K_j+t(\lambda_*-\lambda_j)\},\qquad
Q_s=\frac2s\int_0^sB(t)\,dt-J.                \tag{B4}
\]
每个斜率非负，故B非减。对actual jumps取B3的最佳upper，使用其全密度
Riemann sum；一个缺行只贡献\(O(D)\)。237精确finite-height抵消给
\[
\liminf_{D\to\infty}\mathcal A_D/D^2
\ge\frac{s^2}{2}\lambda_*-\frac{s}{2}Q_s.     \tag{B5}
\]
例如当前\(s=3\)，jump总和为\(9D^2/2+O(D)\)，B5直接由
\(sJD^2/2\le\mathcal A_D+\sum_{\nu\in V_D}h_\infty^{(\nu)}\)得到。
这一步没有把raw index或一个denominator table的\(\tau\)当成精确费用。

用常数源1校准同一组图和同一度量：其多项式格的实际jumps为\(0,\ldots,D\)，
首项行列式1，有限处费用0。B3–B5适用，故
\[
Q_1=2\int_0^1B(t)\,dt-J\ge\lambda_*.
\]
B非减使区间平均非减；对每个整数\(s\ge1\)，
\[
\boxed{Q_s\ge Q_1\ge\lambda_*}.              \tag{B6}
\]
这是公开degree/height式的校准，并未把真实目标源换成常数源。
它不需要§7.1.6的最后一个secant slope恰不超过s；固定有限radii的真正凸envelope
已经包含在B中。若\(\kappa\)是同actual费用的已证upper，严格rank矛盾要求
\[
s\lambda_*>Q_s+2\kappa/s,\qquad
\boxed{\kappa<\frac{s(s-1)}2\lambda_*}.       \tag{B7}
\]
当前\(s=3\)仍必要\(\kappa<3\lambda_*\)。因此单图Jensen门槛不是仅靠固定
共同BC metric的多图或凸修正便可消掉的障碍。

B6–B7的范围仅是B3已支付的同源、同ordinary graded目标、固定共同metric类。
不同species metric、随D变化的权重或图、balanced tensor、新source/target格、
有限处解析图及一般更强CDT方法都须另付公式，本文未将其关闭。

## 3. 无需新primary的紧全图上界

实际FULL复读234冻结all-map稿G1–G4：若\(\phi:\mathbb D\to\mathbb C\)
holomorphic且\(F\circ\phi\)亚纯，则\(E\circ\phi\)亚纯；
\[
p=3\phi(E\circ\phi)^2
\]
在包括foreign原点前像的全盘holomorphic，且
\(\phi=\tfrac13\tanh^2\sqrt p\)。因此p遗漏\(-a,-9a\)，\(a=\pi^2/4\)。
用\(h=(p+a)/(p+9a)\)、\(h(0)=1/9\)，
\(h'(0)=8p'(0)/(81a)\)、\(p'(0)=3\phi'(0)\)，该稿的三穿孔覆盖半径
\[
R(x)=\frac{8x(1-x)}{\pi}K(x)K(1-x),\quad
K(x)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-x\sin^2\theta}}
\]
给精确仍未数值求值的all-map upper
\[
|\phi'(0)|\le C_E=\frac{2\pi}{3}K(1/9)K(8/9). \tag{B8}
\]
没有unique-origin或univalent-p假设；J的共同延拓要求只会进一步缩小图类。

Cauchy–Schwarz及\(y=\tan\theta\)给
\[
K(x)^2\le\frac\pi2
\int_0^{\pi/2}\frac{d\theta}{1-x\sin^2\theta}
=\frac\pi2\int_0^\infty\frac{dy}{1+(1-x)y^2}
=\frac{\pi^2}{4\sqrt{1-x}}.
\]
在\(x=1/9\)有\(x(1-x)=8/81\)。代回B8，所有因子保留后得到
\[
\boxed{|\phi'(0)|\le C_\dagger
=\frac{\pi^3}{2^{7/4}}}.                     \tag{B9}
\]
这里K采用parameter x而非modulus。该提升只收紧234原有全图证明，
不新增图的量词或新的uniformization假设。

## 4. 当前safe upper不能跨过校准后的门槛

完全不使用浮点计算即可比较。由\(\pi<22/7\)得\(\pi^3<32\)，且
\(2^{7/4}>16/5\)（四次方比较\(128>65536/625\)），所以\(C_\dagger<10\)。
有限正项级数给
\[
e^{5/2}>
\sum_{k=0}^7\frac{(5/2)^k}{k!}
=\frac{7825795}{645120}>12.
\]
于是\(\log12<5/2\)，
\[
\boxed{\kappa_{\rm safe}>8
>15/2>3\log C_\dagger}.                      \tag{B10}
\]
中间\(15/2>3\log C_\dagger\)也因\(C_\dagger<10<12\)直接成立。
结合B7–B9，**仅以B2作为算术输入，任何本稿B3类的合法共同图及固定共同BC
凸修正，都不能得到严格rank矛盾**。改善跨过旧松cap的必要window是正确但无足够收益的描述。

这不是\(\liminf\mathcal A_D/D^2\ge\kappa_{\rm safe}\)，也不是实际最优费用no-go。
若将来证明更低的actual费用，并付同一合法图及真实\(Q_3\)，仍可重新检验
\[
\kappa<\frac92\lambda_*-\frac32Q_3
\le3\log C_\dagger.                          \tag{B11}
\]
239至此应停止仅凭现有safe upper继续优化的投资推断，在240作提前正式全局复盘；
本数学稿不重置policy中的正式轮次。更强的证书若改B3，须具体写出其新增负项及适用条件。

精确费用界只须在一个**已证明无界**的degree子族成立也可以：沿该子族取
\(\limsup\mathcal A_D/D^2\)和B5的极限，严格B11仍矛盾。
因此停止条件不能因“尚无全D最优界”排除一个真正已支付的无界子族；有限头不提供这种接口。
每个该degree的全部finite-place账和actual selector仍须保持。

## 5. 更高价值的后备首证书：一次D3约束清三个禁通道

237已证明固定\(M_{0,10}\)原配置、原\(F,\omega\)的全n周期有11通道motivic ambient。
要求的六通道projection尚缺五个坐标恒零；238的换形counterexample仅排除
“一般Gauss–Manin或同F会免费给该projection”，没有否定原\(\omega\)。

一个可核的首证书不必先猜全rank4。写既有motivic分解中四个相关坐标为
\[
c_3\zeta_3^{\mathfrak m}
+c_{23}\zeta_2^{\mathfrak m}\zeta_3^{\mathfrak m}
+c_{33}(\zeta_3^{\mathfrak m})^2
+c_{223}(\zeta_2^{\mathfrak m})^2\zeta_3^{\mathfrak m}.
\]
Brown的primitive odd-zeta coaction及derivation式精确给
\[
D_3 I_n^{\mathfrak m}
=\zeta_3^\ell\otimes
\big[c_3(n)+c_{23}(n)\zeta_2^{\mathfrak m}
+2c_{33}(n)\zeta_3^{\mathfrak m}
+c_{223}(n)(\zeta_2^{\mathfrak m})^2\big].     \tag{B12}
\]
其它七个ambient坐标的D3为0。motivic独立性（不是数值period map injectivity）遂给
\[
\boxed{D_3 I_n^{\mathfrak m}\in
\mathbb Q\,\zeta_3^\ell\otimes\zeta_2^{\mathfrak m}
\iff c_3(n)=c_{33}(n)=c_{223}(n)=0}.          \tag{B13}
\]
因此一次真正uniform的relative-cut证书可以同时清三禁通道；
仍剩\(\zeta_2^2,\zeta_2^3\)两个Tate坐标单独支付。

这是具体的下一首关，尚未证明原\(\omega\)满足B13。
所需证书须将原有高pole/relative-boundary reduction写为全部n有效的标准
iterated-integral words，再按Brown(3.4)的长度3 cuts证明右因子weight0、3、4
部分恒零，只保留weight2部分。weight至多7时每个word至多五个这种cut；
这并不免费提供原高pole family的uniform word reduction或消去boundary。
有限头、dimension计数和ordinary生成函数的holonomic存在性都不能代替该证书。
即使五坐标最终清完，专门\(\zeta_7\)隔离（或\(1,\zeta_5,\zeta_7\)更强LI）的
无限非零、完整费用及目标选择性仍另付；“\(\zeta_5,\zeta_7\)至少一个无理”在项目采用的
\(\zeta_5\)baseline下不是新目标。本轮未选择更多参数或新的文献搜寻序列。

## 6. 实际验证范围

239实际FULL读取238报告、policy/current manifest，237两份metric桥、235两份
multimap稿、234 all-map稿及239独立算术冻结稿；manifest只作为当前状态输入，
没有历史目录审计。当前CDT220页作者PDF实际完整选读物理90–95、101–118；
Brown2012本轮新增完整选读物理8–11（Theorem2.4、Definition3.1、(3.3)–(3.4)、
Lemma3.2），支撑B12–B13。没有声称FULL整部CDT或实际数值period独立性。
精确身份见
[本人scope](../literature/actual_cofactor_arithmetic_sources_round239_20261008/alternative_reading_scope.md)。
数学程序、参数/prime扫描、旧producer、Git和Lean执行均0；只新增本稿和本轮来源记录。
保存后作者实际FULL复读最终全文，身份另报；此作者核对不冒充独立审阅。
