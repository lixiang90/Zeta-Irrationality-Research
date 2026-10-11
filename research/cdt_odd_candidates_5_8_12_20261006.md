# 三个非临界 L3 目标：明确周期 source、level32 全尖点模型与 level48 几何障碍

日期：2026-10-06。新建记录，不修改冻结报告。定向比较正基本判别式D=5、8、12的偶实角色χD及困难值L(3,χD)。本稿没有证明新的无理性或数值线性无关性，不运行下载源码，不作参数或素数扫描。新证书只核三个固定角色、有限Bernoulli恒等式、完整eta尖点表和genus公式。

主要结果是：标准三oldscale的真实周期构造可以同时用于三个D；D8的level32确有一个明确、整系数、Fricke invariant的genus0坐标，但相同全填充叶方案的几何上限比level20更紧；D12的level48 Fricke商genus1，不能直接照搬genus0微分模型。另给低level混合ζ3/L3的确切周期，作为不同目标的候选，而非已经成立的无理性结论。

## 1. 原始文献与检索范围

实际原件：

- [Beukers, Irrationality proofs using modular forms, 1987](../literature/beukers1987_modular_irrationality.pdf)：印刷p273的Proposition1.2给完整Eichler–Fricke周期；pp280–281的Theorem4证明8ζ3−5√5L(3,χ5)不属于Q(√5)。这是混合目标，不是单个L3χ5无理。
- [Yang, Apéry limits and special values of L-functions, arXiv:0709.1968v1](../literature/yang2007_apery_limits_v1_20261006.pdf)：本轮保存原始24页PDF；对应JMAA343(2008),492–513。pp4–6的Lemmas1–2给genus0模参数下的非齐次微分方程/Eichler积分方法；具体例子包含ζ3、L2χ−3、Catalan及模形式L值。有限的本文例子没有提供已证纯L3χ8/L3χ12无理性触发器。
- [Ogg, Hyperelliptic modular curves, BSMF102(1974),449–462](../literature/ogg1974_hyperelliptic_modular_curves_20261006.pdf)：本轮保存15页原始PDF；Theorem2、印刷p451明确N48的hyperelliptic involution不是Atkin–Lehner型；p460给它的实际矩阵。
- [Rouse–Webb, On spaces of modular forms spanned by eta-quotients, 固定v3](../literature/rouse_webb2014_eta_quotients_v3.pdf)：§1的Newman模性条件及Ligozat尖点阶用于第5节全局eta模型。
- [Zagier, Integral solutions of Apéry-like recurrence equations](../literature/zagier2009_apery_like_recurrences.pdf)：§5的表格是weight1、二阶Apéry方程；同一个level标签不能自动识别成偶角色L3目标。

网页原件入口：[Beukers](https://www.numdam.org/article/AST_1987__147-148__271_0.pdf)、[Yang固定v1](https://arxiv.org/pdf/0709.1968v1)、[Ogg](https://www.numdam.org/article/BSMF_1974__102__449_0.pdf)。新文件与已有原件复用记录见[本轮manifest](../literature/manifest_cdt_candidates_5_8_12_20261006.json)。这里没有用2026年的level8/domb争议draft；也没有把未搜索到某个表达式写成全球不存在定理。

## 2. 统一且不混淆常数项的 Eisenstein 归一化

记q=exp(2πiτ)，k=2或4，采用

\[
 E_{k,D}=\frac12L(1-k,\chi_D)
 +\sum_{n\ge1}\frac{\chi_D(n)n^{k-1}q^n}{1-q^n},\qquad
 F_{k,D}=\sum_{m,n\ge1}\chi_D(n)m^{k-1}q^{mn}.
 \tag{1}
\]

其正次数Dirichlet级数分别是ζ(s)L(s−k+1,χD)、ζ(s−k+1)L(s,χD)。D=5的E4常数恰好等于1；不能将这个常数擅自复制给D8/12。

|D|K|E2常数|E4常数|κ=D√D|
|---|---|---:|---:|---:|
|5|Q(√5)|−1/5|1|5√5|
|8|Q(√2)|−1/2|11/2|16√2|
|12|Q(√3)|−1|23|24√3|

表格由B_{j,χ}=D^{j−1}Σ_{a=1}^Dχ(a)B_j(a/D)、L(1−j,χ)=−B_{j,χ}/j精确得到；角色均为正基本判别式所定义的primitive even角色。

为固定Fricke因子，可直接用两种Eisenstein lattice sums：Σ'χ(n)/(Dmτ+n)^k与Σ'χ(m)/(mτ+n)^k。前者的Fourier正次数归一化因子是2(−2πi)^k√D/[D^k(k−1)!]，后者是2(−2πi)^k/(k−1)!。换元τ→−1/(Dτ)交换两种sum。以determinant-normalized slash记W_D，得到

\[
 E_{k,D}|_kW_D=D^{(k-1)/2}F_{k,D},\quad
 F_{k,D}|_kW_D=D^{-(k-1)/2}E_{k,D}.
 \tag{2}
\]

k4时格点sum绝对收敛；k2采用标准Hecke/Eisenstein求和，非主角色消除准模修正，同样的换元给(2)。因此weight4的交换因子是κ，weight2的是√D。D5的式(2)与Beukers原件归一化一致。

在N=Dℓ、j|ℓ下，(2)给

\[
 E_{k,D}(j\tau)|_kW_{D\ell}
 =D^{(k-1)/2}\frac{\ell^{k/2}}{j^k}
 F_{k,D}(\ell\tau/j).
 \tag{3}
\]

该式来自直接替换z=ℓτ/j；并不要求auxiliary prime与D互素。

## 3. 三个真实纯 L3 周期 source

取N=4D，以下省略D下标：

\[
 \begin{aligned}
 V_-={}&E_4(\tau)-5E_4(2\tau)+4E_4(4\tau)\\
 &-\frac\kappa4\{F_4(\tau)-20F_4(2\tau)+64F_4(4\tau)\},\\
 V_+={}&\sigma(V_-),\\
 A_-={}&E_2(\tau)-4\sqrt D F_2(4\tau),\quad A_+=\sigma(A_-).
 \end{aligned}\tag{4}
\]

σ是K的非平凡embedding。由(3)，V−/A−的normalized Fricke sign为−，V+/A+为+。V±的∞常数是c4(1−5+4)=0；W sign又保证它们在0也无常数，故第三q原函数f±=ΣV±,n q^n/n³是实际holomorphic芽，不能用删除非零Eisenstein常数的方式代替这一步。

置

\[
 P_E(s)=(1-2^{-s})(1-2^{2-s}),\quad
 P_F(s)=(1-2^{2-s})(1-2^{4-s}).
\]

真实Dirichlet级数为

\[
 L(V_-,s)=P_E(s)\zeta(s)L(s-3,\chi_D)
 -\frac\kappa4P_F(s)\zeta(s-3)L(s,\chi_D).
 \tag{5}
\]

两个polynomials在s2都为零，所以两embedding的L(V±,2)均为0。even角色的L(0,χ)=0，ζ(0)=−1/2，P_F(3)=−1/2，故

\[
 \Theta=-\frac\kappa{16}L(3,\chi_D),\qquad
 L(V_-,3)=\Theta,\quad L(V_+,3)=-\Theta.
 \tag{6}
\]

此外P_E(1)=−1/2，L′(−2,χ)=−D²√D L(3,χ)/(4π²)，而ζ(−2)=0，得到两边共同的L(V±,1)=−NΘ/(2π²)。代入Beukers Proposition1.2的完整period polynomial，严格得到

\[
 \begin{aligned}
 f_-(\tau)+N\tau^2 f_-(W_N\tau)&=\Theta(1+N\tau^2),\\
 f_+(\tau)-N\tau^2 f_+(W_N\tau)&=-\Theta(1-N\tau^2).
 \end{aligned}\tag{7}
\]

因此H−=A−(f−−Θ)、H+=A+(f++Θ)都真实W_N-invariant。假设L3χD∈Q时，两者是K[[q]]中实际互为共轭的芽；Θ没有被删掉。该假设仅为构造算术触发器，未得到holonomy矛盾。

|D|N|Θ|
|---|---:|---|
|5|20|−5√5L3χ5/16|
|8|32|−√2L3χ8|
|12|48|−3√3L3χ12/2|

q系数的完整安全型仍是C0·LCM(1,…,n)³。D8有2A±∈OK[[q]]、V±∈OK[[q]]；D12两者已为OK系数。固定规范分母改善不是随n增长的D²收益。q级数本身不能自动称为holonomic；还须选择真实modular coordinate并证明下降系统和actual rank。

### 3.1 两oldscale为什么尚未解除两个embedding的周期障碍

在N=2D同一E/F ansatz中，唯一∞常数取消组合是E(τ)−E(2τ)，配成anti-Fricke所需的F部分是κ\{F(τ)−16F(2τ)\}/4。原embedding的L2为0；其系数共轭的L2为

\[
 L(V_+^{(2)},2)=\frac{\pi^2}{4}L(-1,\chi_D)\ne0.
 \tag{8}
\]

值L(−1,χD)依次为−2/5、−1、−2。该非零Tate中项阻止相同W叶上的两个pure quadratic period同时成立。要在同一three-oldscale polynomial中同时满足∞ constant0与两个E/F的s2零点，E polynomial须包含(1−x)(1−4x)，degree至少2。这只是该unmixed anti/同时pure quadratic ansatz的最少三个scales；不是所有目标、所有projection或所有modular方法的最低level定理。不同embedding用不同analytic maps、额外真实period projection、混合source都不被此论证排除。

## 4. 低level混合目标可以改变目标，而非直接继承纯目标结论

令c4=L(−3,χD)/2，取

\[
 F_D^{mix}=c_4\{E_4^{triv}(\tau)-D^2E_4^{triv}(D\tau)\}
 +(D^2-1)\{E_{4,D}(\tau)-\kappa F_{4,D}(\tau)\}.
 \tag{9}
\]

E4triv=1+240Σσ3(n)q^n。该source在levelD、character kernel kerχD上是weight4，∞ constant0，W_D sign−、L2=0；其真实第三period为

\[
 -120c_4\frac{D-1}{D}\zeta(3)
 +\frac{(D^2-1)\kappa}{2}L(3,\chi_D).
 \tag{10}
\]

分别等于

\[
 -12\{8\zeta(3)-5\sqrt5L3\chi5\},\quad
 -\frac{21}{2}\{55\zeta(3)-48\sqrt2L3\chi8\},\quad
 -22\{115\zeta(3)-78\sqrt3L3\chi12\}.
 \tag{11}
\]

首项正是Beukers既有定理的模型。后两项是本文由真实Eisenstein source得到的明确候选period，尚无数值无理性结论。不能由ζ3已无理推断这两个组合或单个L3无理。

低level确有genus0几何：Γ0(8)、Γ0(12)的character kernel均为Γ1(D)在PSL意义下的像。它们对genus0的X0(D)给degree2 cover，character在cusp stabilizer上只在denominators(2,4)或(2,6)为−1；每处只有一个cusp。两基曲线均无elliptic points，所以恰有两branch points，Riemann–Hurwitz给kernel curve genus0。这分别是6 cusp和10 cusp的genus0曲线，不能与Γ0(D)自身的4或6 cusp混淆。

这些混合目标允许在level8/12重新研究不同source；仍须构造具体Hauptmodul、匹配所有embedding真实period与leaf、重证actual independence与完整t分母。这里只闭合了source和period，不声称继承BeukersD5的收敛/范数估计，也不声称它们已比level20预算便宜。

## 5. D8 / level32：真正的Fricke quotient坐标

记ηδ=η(δτ)，取

\[
 h_{32}=\frac{\eta_2^3\eta_{16}^3}
 {\eta_1^2\eta_4\eta_8\eta_{32}^2},\qquad
 B_{32}=\eta_4^2\eta_8^2,\qquad t_{32}=1/h_{32}.
 \tag{12}
\]

h exponents为(−2,3,−1,−1,3,−2)，δ=(1,2,4,8,16,32)。weight0、两Newman congruences均为−24，∏δ^{rδ}=1，故h是Γ0(32)的trivial-character modular function。exponents在δ↔32/δ下对称，η变换prefactor∏(32/δ)^{rδ/2}=1，故h|W32=h；这不是仅检查前几个q系数。

使用完整Ligozat公式

\[
 \operatorname{ord}_{a/c}\prod\eta_\delta^{r_\delta}
 =\frac{32}{24\gcd(c^2,32)}
 \sum_\delta r_\delta\frac{\gcd(c,\delta)^2}{\delta},
 \tag{13}
\]

以及每个denominator c的cusp数φ(gcd(c,32/c))，得到全部8 cusp：

|c|完整代表|cusp数|ord h|ord B|h值（order0时）|
|---:|---|---:|---:|---:|---|
|1|0|1|−1|1|∞|
|2|1/2|1|1|1|0|
|4|1/4,3/4|2|0|1|1−i,1+i|
|8|1/8,3/8|2|0|1|1+i,1−i|
|16|1/16|1|1|1|0|
|32|∞（等价1/32）|1|−1|1|∞|

η在upper half-plane没有zeros，所以这个表包括所有zeros/poles。h的total pole degree恰为2。W32交换∞/0，1/2和1/16，以及其余两对cusps；h非恒定且W invariant。因此degree2 map已经恰好是W quotient：X0(32)/W32为P1，h是其Hauptmodul，不是一个degree2的Hauptmodul有理函数。

B32的weight为2、character trivial、各8 cusp全为order1、interior无zeros。其Fricke prefactor是−(8·4)/32=−1，故B32|W32=−B32。它是可用于后续实际微分系统的明确weight2 gauge，并未计算新的Q/U或actual rank。

h=q^(−1)+2+O(q)，t32=q−2q²+O(q³)。所有eta产品的整数指数提供t32∈qZ[[q]]；首项1又给q(t32)∈t32Z[[t32]]，这是formal recursion的全尺度整数性，不由少数Taylor coefficients推断。于是第3节q安全型转到此t仍为C0·LCM(1,…,n)³。

### 5.1 全部order0 cusp的精确phase

取τ=a/c+iy，δa/c约成a′/c′，d′为a′modc′的inverse（c′=1取d′=0）。由标准η变换和η(z)在∞的首项，order0 eta quotient的cusp constant是

\[
 \Bigl\{\prod_\delta(\delta/\gcd(c,\delta))^{-r_\delta/2}\Bigr\}
 \exp\!\left(\pi i\left[
 \frac{a}{12c}\sum_\delta\delta r_\delta
 -\sum_\delta r_\delta s(d',c')\right]\right),
 \tag{14}
\]

s是有限Dedekind sum。共同y-power因weight0取消，exponential divergence因cusp order0取消；因此该式没有略掉可能改变符号的η multiplier。

|cusp|phase/π|modulus²|完整constant|
|---|---:|---:|---|
|1/4|−1/4|2|1−i|
|3/4|−7/4|2|1+i|
|1/8|1/4|2|1+i|
|3/8|−1/4|2|1−i|

这逐项覆盖了全部四个order0 cusp；不是从1/4的值猜测其它cusps。其余四个cusp由非零order已经精确为0或∞。因此Fricke quotient的四个cusp值准确为

\[
 t=0,\quad\infty,\quad\frac{1+i}{2},\quad\frac{1-i}{2}.
 \tag{15}
\]

### 5.2 同一全填充叶方案的条件性上限

对(4)的N32 source，H±在真实<T,W32>下同时invariant且在唯一q-cusp正则。若采用之前level20型的fullfilled leaf构造，G=<T,W32>的coarse填充面具有唯一simple-zero point P；eta unit t在interior无zeros/poles，且其非零cusp值(15)的所有fibers不在interior。任何相应holomorphic disk map Φ=t∘u因而满足Φ^−1(0)={0}、省略a=(1±i)/2。

CDT固定原件§2.8、p24的Carathéodory界按a缩放给

\[
 |\Phi'(0)|\le16|a|=8\sqrt2,
 \qquad\log|\Phi'(0)|\le\log(8\sqrt2)<\log16.
 \tag{16}
\]

这里只断言满足上述fullfilled、unique-zero及omission standing条件的这个几何族上限；没有从eta table自动重证所有fullleaf拓扑，也没有计算实际conformal radius。其它coordinate、restricted leaf、不同embedding maps或其它source都未被排除。把坐标代成1/(h−1)虽然能将complex cusp values移到±i，却在interior h=1引入pole；它不能无条件保留这里的full holomorphic leaf。

## 6. D12 / level48：Fricke quotient恰为genus1

标准genus formula给Γ0(48) index96、12 cusp、没有elliptic points，所以g(X0(48))=1+96/12−12/2=3。Ogg原Theorem2和p460证明其唯一hyperelliptic involution是

\[
 v=\begin{pmatrix}-6&1\\-48&6\end{pmatrix},\quad\det v=12,
 \tag{17}
\]

并且它不属于Atkin–Lehner型。因此W48不是hyperelliptic involution；其degree2 quotient不能genus0，故gquot≥1。另一方面W48在τ=i/√48有interior固定点，所以Riemann–Hurwitz

\[
 2g(X)-2=2(2g_{quot}-2)+r,\qquad r>0
\]

给4=4gquot−4+r，故gquot<2。两者合并严格得到

\[
 \boxed{g(X_0(48)/W_{48})=1.}\tag{18}
\]

genus3加“有固定点”单独不够；必须加Ogg的非hyperelliptic证明才能排除gquot0。v的商确为genus0，但(7)仅证明W48周期，尚未证明同一actual H±在v下正则。把v当成W48或把它的genus0结论直接代进pure χ12模型是不合法的。

可考察第4节level12混合source，或为(17)重新计算真正period cocycle；二者都要保留可能的π³/log载体并核两embedding。这是具体的新接口，不是已经找到的低cost替代系统。

## 7. 模型选择与剩余工作

|目标/ansatz|已闭合最低level（限定此构造）|真实genus0坐标状态|关键限制|
|---|---:|---|---|
|Beukers混合8ζ3−5√5L3χ5|5|原件已给|既有定理，不能推出单L3χ5|
|pure L3χ5，两个same-W quadratic periods|20|此前已完整核|当前算术/解析预算仍失败|
|pure L3χ8，同一three-oldscale ansatz|32|本稿h32全局证明|四 cusp，条件性导数cap8√2更紧|
|pure L3χ12，同一three-oldscale ansatz|48|W quotient genus1|genus0需新v cocycle，不能直接复用|
|55ζ3−48√2L3χ8 mixed period|8|character kernel genus0；尚未给完整quotient参数|共轭period、leaf、rank、完整t成本未闭合|
|115ζ3−78√3L3χ12 mixed period|12|character kernel genus0；同上|更多cusps；未继承Beukers收敛/范数估计|

可验证优先级是：pure D8可直接开始真实h32/B32微分系统，而不是重新找q参数；它提供对level20方法的严格几何压力测试，不是自动改善预算。若希望改变预算结构，level8混合目标比盲升level48更值得先核，但应先闭合不同embedding的actual正则叶及共同整模型。此优先级是本轮模型比较的推断，不是新的无理性主张。

## 8. 证书与scope

[新脚本](cdt_odd_candidates_5_8_12_20261006_verify.py)和[JSON](cdt_odd_candidates_5_8_12_20261006_verify.json)包含71项固定精确核验，作者本轮执行通过：三角色Bernoulli constants、E/F polynomials及period系数、8个固定level的genus公式、level32完整8 cusp的orders/counts、全部4个finite eta constants的Dedekind phase、weight/character/W prefactor，以及D8/12 character-cover branch表。

global modularity、Eichler period、degree2 quotient和条件性leaf界由正文证明及标明的原始输入承担；有限checks不代替它们。不运行旧producer、没有random primes/parameters，未验证新的actual rank、完整p-adic content或数值无理性。

## 9. 本轮实际独立审阅记录

- conjugate_projection实际只读§§2–3及§3.1，重推determinant-normalized Fricke与oldscale因子、even functional equation给出的L′(−2,χ)、L1/2/3及两个embedding的pure quadratic periods，独核three-old/two-old限定ansatz结论。审阅通过；没有执行producer，没有审阅§5尖点phase。
- root实际完整只读§§1–8及71项check的JSON，限定独审通过§§2–6的周期source、mixed period规范、character-kernel的两个branch cusp/genus、h32完整8 cusp与4个finite phase、B32和t双向整性、level48非hyperelliptic加fixed-point的Riemann–Hurwitz论证，以及standing leaf/omission条件下的cap。未独立重证Yang/Beukers已经发表的数值定理原出处，未主张mixed两embedding叶已闭合或这些候选具有首次性。

这些审阅不扩大正文的范围；不存在从有限证书、genus0或period恒等式直接得到新的数值无理性结论。
