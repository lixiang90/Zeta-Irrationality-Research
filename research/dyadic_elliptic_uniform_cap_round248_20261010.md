# 第248轮：原五行源的全部合法图有统一导数上界

2026-10-10，Root，全部纸证。结论限定原坐标 x=u/(1+7u)、完整五行(1,Z,Z²,H,δH)和已付 d_N² 安全模型的基本单实处CDT入口：**任意共同合法图均有|φ′(0)|<20，不能跨越所需log|φ′(0)|>16/5。** 这包括multivalent图，不靠坏叶存在或地图扫描。它不关闭不同坐标、Fricke商源、多place或增长矩阵方法，也不证明任何新数值无理性。

## 1. 正确分母数组与能量必要门槛

247已付实际field F=Q(u,Z)=Q(X₀(14))，其对Q(x)degree3；1,Z,Z²在x的全部Taylor系数整数，对Q(x)独立。共同合法φ使这些三个实际native芽的拉回单值亚纯。

CDT Theorem2.5.1 (2.5.2)的τ为
\[
\tau=\frac1{m^2}\sum_{i=1}^m(2i-1)\sigma_i
=\sigma_m-\frac1{m^2}\sum_j u_j^2 b_j.
\tag{1}
\]
对三行整数field，τ=0。若λ=log|φ′(0)|>0，其Bost–Charles能量J满足 **J≥3λ**。

完整五行的 d_N² 应写成 **5×2** array，两列均为(0,0,0,1,1)；σ行和是(0,0,0,2,2)。每列u_j=3、b_j=1，故τ=2−18/25=32/25。247 C稿D14的“单列”记法在此明确澄清：不能以d_(2N)替d_N·d_N。旧稿保持冻结，数值τ及此前秩/jump结论不变。

若该五行基本入口想得到 J/(λ−32/25)<5，则J≥3λ迫
\[
3\lambda<5(\lambda-32/25),\qquad \lambda>16/5.
\tag{2}
\]
下面给所有共同图λ<3，不需要其余行的monodromy分析。若图不延伸到边界，CDT条件按其允许的缩盘/边界能量解释；导数上界本身仅用开圆盘内合法性。

## 2. 实际微分、商坐标和完整quartic

为避免数据库浮点period及未付Manin归一化，重新自含构造。写
\[
f_{14}=\eta(\tau)\eta(2\tau)\eta(7\tau)\eta(14\tau),\qquad
t=\left(\frac{\eta(\tau)\eta(14\tau)}{\eta(2\tau)\eta(7\tau)}\right)^4.
\]
采用Savitt官方Theorem1.1完整statement及Remark1.2（所用读域另存）。f₁₄指数(1,1,1,1)，weight2，两个加权和24，product196平方，故Γ₀(14)字符trivial；四cusps∞、0、1/2、1/7的实际orders全为1。H中eta无零。Γ₀(14)无elliptic points：order2的trace0在mod7要求−1为平方，order3在mod2要求z²+z+1有根，均不可能。于是
\[
\omega=f_{14}\,dq/q
\]
在紧X₀(14)上处处全纯且无零，故其genus为1；nativeω=(1+O(q))dq。

t的指数(4,−4,−4,4)，weight0，两个加权和24，product1。实际divisor为
\[
(t)=[\infty]+[0]-[1/2]-[1/7].
\]
η的完整S变换给t(W₁₄τ)=t(τ)、f₁₄(W₁₄τ)=−14τ²f₁₄(τ)。t在E=X₀(14)的degree2等于W商degree2，因此t是实际商的degree-one坐标。此处无需把另一个two-pole表达式猜作Hauptmodul。

令Θ=q∂q、y=Θt/f₁₄，则y(W₁₄τ)=−y(τ)，且ω=dt/y。y仅在两个t-pole的cusps有order2 pole；在另两cusps有限，H中无pole。故y²在P¹_t上为degree≤4 polynomial。这先付完整degree bound。

有限乘积逐项给
\[
t=q-4q^2+6q^3-8q^4+17q^5+O(q^6),
\]
\[
f_{14}=q-q^2-2q^3+q^4+0q^5+O(q^6),\quad
y=1-7q+13q^2-34q^3+84q^4+O(q^5).
\]
由于t首项q，五系数唯一确定已付空间，得到整个函数身份
\[
\boxed{y^2=E(t)=t^4-14t^3+19t^2-14t+1.}
\tag{3}
\]
y非W-invariant，故C(t,y)=C(E)。它也是Q-defined完整函数域模型。这不是从有限头外推未经界定的恒等式。

## 3. 自含Weierstrass桥，含准确微分规范

令
\[
U=(y+1-7t)/t^2,\quad X=(U+3)/2,
\]
\[
V=2(U^2-1)t+14U+14,\quad Y=V/4.
\]
由(3)直接相消得
\[
(U^2-1)t^2+14(U+1)t+30-2U=0,
\]
\[
V^2=8U^3+76U^2+384U+316,
\quad\boxed{Y^2=(X-1)(4X^2+5X+23).}
\tag{4}
\]
也就是Y²=4X³+X²+18X−23；若Y=2Y₀+X+1，则Y₀²+XY₀+Y₀=X³+4X−6。公式给rational inverse t=(4Y−14U−14)/(2(U²−1))，故是birational桥而非未定degree的isogeny。

隐式式对U的偏导为2y，对t的偏导为V，故
\[
\boxed{\omega=dt/y=-dX/Y.}
\tag{5}
\]
native(t,y)=(0,1)到Weierstrass∞，ω的leading coefficient仍1。无需数据库Manin constant来领取准确归一化。

## 4. 两个真实closed cycles与严格period界

写P(X)=(X−1)(4X²+5X+23)，只有实root1。取其正实branch，真实real oval给period
\[
a=2\int_1^\infty\frac{dX}{\sqrt{P(X)}}
=4\int_0^\infty\frac{ds}{\sqrt{4s^4+13s^2+32}}.
\]
沿X从−∞到1取Y=i√(−P)，再从1到∞取正Y。两端均到同一个Weierstrass∞，在branch1的local参数Y下是连续piecewise smooth的closed cycle；其period为a/2−ib，其中
\[
b=\int_{-\infty}^1\frac{dX}{\sqrt{-P(X)}}
=2\int_0^\infty\frac{ds}{\sqrt{4s^4-13s^2+32}}>0.
\tag{6}
\]
ω的负号只改变period符号。因此完整Abel latticeΛ包含a及a/2+ib（取共轭/反向cycles）。不必证明此二者primitive：包含的sublattice已经足够给covering radius上界。

先用4s⁴+13s²+32≥(2s²+13/4)²，有
\[
a\le4\pi/\sqrt{26},\qquad a^2<80/13,
\]
其中π²<10。令κ=1/2−13√2/64∈(0,1)。直接恒等式
\[
4s^4-13s^2+32
=\kappa(2s^2+4\sqrt2)^2+(1-\kappa)(2s^2-4\sqrt2)^2
\]
给
\[
b\le\frac{\pi}{\sqrt{4\sqrt2-13/4}},\qquad b^2<200/47,
\]
后者用√2>7/5、π²<10。对sublattice aZ+(a/2+ib)Z，先选最近的imaginary row，再选该row最近real lattice node，距离不超过
\[
R=\frac12\sqrt{a^2+b^2},\quad
R^2<1590/611<25/9,\quad R<5/3.
\tag{7}
\]
完整Λ只会更密；任一translate亦有此covering radius。全部界为有理/根式不等式及实积分纸证，不是近似数据库period或数值quadrature。

## 5. Elementary Bloch界，适用所有multivalent图

自含引理：若holomorphic z:D→C的像遗漏任一Λ-coset，而该coset covering radius≤R，则|z′(0)|≤12R。

证明：取r<1，选|ζ₀|<r使M=(r−|ζ₀|)|z′(ζ₀)|在closed |ζ|≤r最大；M≥r|z′(0)|。令d=r−|ζ₀|、h(w)=z(ζ₀+dw/2)−z(ζ₀)，α=h′(0)。在|w|<1有|h′|≤2|α|，故由Schwarz lemma有|h′−α|≤3|α||w|。积分给|h−αw|≤(3/2)|α||w|²。于|w|=1/3，Rouché使h的像包含center0、radius|α|/6=M/12的open disk。遗漏coset使M/12≤R。令r↑1得引理。α=0/constant情况平凡；没有假设z或φ单射。

## 6. 当前完整field强制这一cap；基本窗口立即停止

共同单值亚纯拉回Z与x产生compact curve normalization的holomorphic lift ψ:D→E，nativeψ(0)=cusp∞；这由实际degree3 field及一维normalization延拓完成，细证亦见B248。原x=u/(1+7u)的pole divisor恰u=−1/7的degree3 fiber。φ=x∘ψ holomorphic且finite，故ψ必须遗漏此fiber每个point；finite ramification不能把非零pole变成普通点。

通过Abel universal cover lift ψ为z:D→C，选z(0)=0、dz=ψ*ω。nativex=q+O(q²)、ω=(1+O(q))dq，故z′(0)=φ′(0)。至少一个遗漏point P的Abel lifts为z_P+Λ，z的像遗漏整个coset。由(7)及§5，
\[
\boxed{|\phi'(0)|\le12R<20.}\tag{8}
\]
e³>20可用exp级数前九项严格证明，因此λ<log20<3<16/5，与(2)矛盾。故当前全五行、原x、已付τ32/25的基本single-archimedean CDT严格入口，**所有共同合法图均失败**。

这个停止证明只用完整field与pole geometry、其整数秩能量lower、period上界，不用H坏cusp存在替代all-maps量词。它是已付安全模型/选用判据的结构失配；未证明任何更优joint arithmetic类型仍失败，不移植到另一坐标或不同完整源，亦不关闭多place、integral-refined或增长矩阵定理。停止该窗口不停止新数值研究。

## 7. 来源与运行边界

Root本轮实际全文读247进展、244全局报告，以及CDT所存固定v2物理PDF16–20完整五页（18249 B / SHA256 ade72b61da52b4e7297e13d594af11b58025285a780aab796490497c9c6a07ae），含完整Theorem2.5.1与2.7.1及邻接条件。未声称完整218/220页原著或最新全proof审计。Savitt完整所用statement及ηS/T为官方web载体读域，直接PDF下载403记录另存；没有把旧weight0 eta criterion偷当weight2定理。

以上eta orders、quartic degree及系数、exactbirational/differential、closedperiod cycles、全部严格bounds与Bloch引理均本稿纸证。Root实际全文读B248最终8082 B field-lift与energy稿、A248最终12413 B商源稿，并独立重推本稿所用共同部分；不是以消息代替正文。另全文读A所存官方MSP论文物理PDF11页的完整Theorems2.4/2.5，独立核对weight2字符与cusp-order条件。本稿不领取A尚未付的全Eichler周期系数或Galois投影。B另对本稿全部七节作独立数学审查，终稿pin与具体审查范围另存。

数学/CAS/interval/prime/parameter/map/Lean执行0，外Git mutation0；文档GET/提取与hash另记，不是数学实验。正式248复盘将据此停止原basic入口，保留已付真实period/rank/整模型；目标active，数值定理未得。
