# 第224轮：真实双边周期、三奇频率与全权重投影

2026-10-08，Root。实际对象仍为222/223固定R_n三周期包。本稿给完全自含的双边period桥、精确三模态坐标和一般最高偶pole阶的投影定理。它支付真实目标投影及telescoping边界接口，**不证明目标外积无限非零、共同递推的最小阶或新的数值无理性**；本轮其他非零/递推工作须另审。

## 1. 双边实际和：有限cutoff以外只从v⁶开始

定义R_n(t)为同一有限整数乘积，对所有n≥0有R_n(t)=O(t⁻⁶)。在0≤k≤n，F_nk(v)=v⁶R_n(−k+v)，原S_n(v)=Σ_(k=0)^n(−1)^kF_nk(v)。固定n且|v|<1/2，令

\[
\mathcal B_n(v)=v^6\sum_{k\in\mathbb Z}(-1)^kR_n(-k+v).
\tag{P1}
\]

内部有限pole经v⁶消去；外部所有整数−k不是R_n极点。对足够大|k|，R及每个固定v导数在此盘为O(|k|⁻⁶)或更小，故外侧和一致绝对收敛且全纯。外侧每项含v⁶，得到

\[
\mathcal B_n(v)-S_n(v)=O(v^6).
\tag{P2}
\]

因此0、2、4次真实jets可由双边和准确恢复，未改变三个A系数或有限tail定义。这里仅替换S的低jets，**不把C_n的双重finite tail替换掉**。

223 H3的generic Gamma extension在所有整数k仍等于v⁶R_n(−k+v)：用Γ(v−k)=(-1)^kΓ(v)Γ(1−v)/Γ(k+1−v)，再用vΓ(v)=Γ(1+v)即可直接验证。这个等式与(P1)使参数shift reduction的低jets有真实边界证书，而非对cutoff之外的Gamma极点免费求Taylor。

## 2. 准确支付一种telescoping边界

记H_(n,k)(v)=(-1)^k v⁶R_n(−k+v)。若已另行证明

\[
\sum_{j=0}^{d}a_j(n)H_{n+2j,k+j}(v)
=G_{n,k+1}(v)-G_{n,k}(v),
\tag{P3}
\]

其中a_j∈Q(n)、不依赖v，且固定有效n、v小闭盘上的G两端趋零，那么对k∈Z求和精确给Σa_j(n)𝓑_(n+2j)(v)=0。平移k↦k+j对双边和合法，没有有限边界残数。再由(P2)比较低于6次的Taylor系数，得到**三个实际A序列共享同一a_j**。

一个容易核的充分条件是G=Q(n,k−v)H_(n,k)(v)，Q的无穷增长≤|k|⁵且有限整数处的乘积已正则；H在两端O(v⁶|k|⁻⁶)，故G趋零。Q=O(1)更足够。若Q增长≥|k|⁶或有限整数处有未约pole，不能免费沿用(P3)，必须另付边界。本稿没有构造a_j/Q，也没有保证其最早系数处处非零。

## 3. 精确partial-fraction周期

偶n的c_(j,k)满足c_(j,n−k)=(-1)^j c_(j,k)，于是S_(j,n)=Σ(-1)^k c_(j,k)对奇j为0。令

\[
\Phi_j(v)=\sum_{m\in\mathbb Z}\frac{(-1)^m}{(m+v)^j}
=\frac{(-1)^{j-1}}{(j-1)!}\left(\frac{d}{dv}\right)^{j-1}
  [\pi\csc(\pi v)].
\tag{P4}
\]

j≥2时绝对且局部一致收敛；j=1为对称求和。依据[NIST DLMF4.22.E5](https://dlmf.nist.gov/4.22.E5)的成对csc展开，移位有限整数不改变对称极限，逐次微分在避开Z的紧集合法。R的有限partial fractions可逐项求和，偶n所有奇S_j消去，得到准确身份

\[
\mathcal B_n(v)=v^6[S_{2,n}\Phi_2(v)+S_{4,n}\Phi_4(v)+S_{6,n}\Phi_6(v)].
\tag{P5}
\]

该式不含近似或saddle选择，n=0亦成立。原双边和本来绝对收敛；仅为分解其中可能的j=1单项，临时用对称极限，消去后不留条件求和依赖。

## 4. 三个实际奇频率与固定可逆矩阵

定义实际整个period

\[
\mathcal T_n(v)=\left(\frac{\sin\pi v}{\pi v}\right)^6\mathcal B_n(v).
\tag{P6}
\]

sin消去所有integer pole。置x=πv、c=cosx，直接三次/五次微分csc给

\[
\mathcal T_n(v)=c\left[
\frac{S_{6,n}(61+58c^2+c^4)}{120}
+\frac{S_{4,n}(1-c^2)(5+c^2)}{6\pi^2}
+\frac{S_{2,n}(1-c^2)^2}{\pi^4}\right].
\tag{P7}
\]

故精确有𝓣_n(v)=B_(1,n)cos(πv)+B_(3,n)cos(3πv)+B_(5,n)cos(5πv)，其中

\[
\begin{aligned}
B_{1,n}&=\frac{S_{2,n}}{8\pi^4}+\frac{11S_{4,n}}{48\pi^2}+\frac{841S_{6,n}}{960},\\
B_{3,n}&=-\frac{3S_{2,n}}{16\pi^4}-\frac{7S_{4,n}}{32\pi^2}+\frac{79S_{6,n}}{640},\\
B_{5,n}&=\frac{S_{2,n}}{16\pi^4}-\frac{S_{4,n}}{96\pi^2}+\frac{S_{6,n}}{1920}.
\end{aligned}
\tag{P8}
\]

纸核：cos³x=(3cosx+cos3x)/4，cos⁵x=(10cosx+5cos3x+cos5x)/16；代入(P7)即得全部常数。矩阵从(S2/π⁴,S4/π²,S6)到(B1,B3,B5)，乘1920后的行依次是(240,440,1682)、(−360,−420,237)、(120,−20,1)，其det=110592000，故原det=1/64。此处是固定纸面有理运算，未执行矩阵程序。

对于实际三行n=2r,2r+2,2r+4及κ3κ5κ7=8505/256，得到

\[
\Delta_r=\frac{8505\pi^6}{4}
\det[B_{q,2r+2i}]_{0\le i\le2,\,q=1,3,5}.
\tag{P9}
\]

因此原目标非退化恰等价于这三个**完整实际模态**的连续三行非退化。单个主saddle或单个cos方向只给rank≤1；不能由某一幅度非零替代(P9)。矩阵含π⁻²、π⁻⁴，所以这里是C上的精确坐标等价，**不是Q上的免费shear或一个新的有理G源**。CDT整模型继续用原A/Δ，不能从三频率个数声称n方向rank=3。

## 5. 一般最高偶pole阶：同一真实投影有m个奇频率

进一步设G(t)是整数pole的proper有理函数，最高pole阶≤2m、在∞为O(t⁻²)，并且其alternating partial-fraction sums所有奇阶为0。令s_j=Σ(-1)^k c_(j,k)，则

\[
\mathcal T(v)=\left(\frac{\sin\pi v}{\pi}\right)^{2m}
\sum_{k\in\mathbb Z}(-1)^kG(k+v)
=\sum_{j=1}^m s_{2j}\left(\frac{\sin\pi v}{\pi}\right)^{2m}\Phi_{2j}(v).
\tag{P10}
\]

对csc的2j−1次导数，乘sin^(2m)后是cosx乘cos²x的次数≤m−1多项式。可以归纳验证：每个奇导数均为cosx乘cos²多项式/ sin^(2j)x，再乘(1−cos²x)^(m−j)。因此𝓣是cos[(2ℓ−1)πv]、ℓ=1,…,m的准确线性组合。

其固定矩阵从ascending变量(s2/π^(2m−2),s4/π^(2m−4),…,s_(2m))到ascending奇频率幅度的det为

\[
2^{-m(m-1)}\ne0.
\tag{P11}
\]

证明：Φ_(2j)=v^(−2j)+正则部分。低于2m阶的jets因此恰由s_(2m)、s_(2m−2)、…构成；乘sinc^(2m)的jet矩阵下三角且对角1。频率ℓ的v^(2a)/π^(2a)系数为(−1)^a(2ℓ−1)^(2a)/(2a)!。Vandermonde的绝对det为

∏_(i<ℓ)[(2ℓ−1)²−(2i−1)²]/∏_(a=0)^(m−1)(2a)!
=4^[m(m−1)/2]=2^[m(m−1)]，

其中每个固定ℓ的∏_(i<ℓ)(ℓ−i)(ℓ+i−1)=(2ℓ−2)!。jet符号与ascending s列的反序符号抵消，得到(P11)。m=3恢复(P8)的1/64。

这使“真实period投影”成为适用于全部此类最高偶pole阶的一般接口，可用于奇ζ候选。它不凭有限频率维数解决所有奇ζ，也不声称Dirichlet字符的不同pole类免费合并；类似L目标仍须支付各个字符/共轭类的完整实际period及整模型。

## 6. 原文、执行与结论边界

Root本轮实际完整复读223 holonomic稿11517B及无限非零稿10073B，核223manifest固定SHA `2b1b22375774410a6c7dec49579e651d1987af45057347184e204e87de8b377b`与main长度524758B；上一轮属于实质progress。只用冻结R、A、Δ身份，不重跑222有限程序。

Root实际web完整读取DLMF4.22的csc公式及排除integer pole条件，下载并FULL读[4.22.E5 TEX](../literature/pade_nonvanishing_sources_round224_20261008/root_dlmf_4_22E5.tex)。没有完整读其引用的Hobson等书籍，未将一个标准partial-fraction公式当成完整primary研究论文审定。其余(P1)–(P3)、(P5)–(P11)为本文自含纸面推导。

本稿数学程序0：无CAS、矩阵执行、numericalintegration、telescoping执行、guessing、PSLQ、Lean、素数/参数扫描或Git操作。公式常数为上述纸核，需独审；本稿不代替其他224作者稿的运行账。保存后Root实际FULL复读，最终身份外部登记，作者自读不冒充独审。独审见[收据](research_round224_bilateral_period_review_20261008.md)。

本轮这份稿单独支付双边边界与全权重投影，未证明Δ无限非零、具体operator的边缘系数、generic主奇点或关系的strict增益。原数值目标继续active；其他224结果若成立，另有严格证明与独审。
