# 第255轮：从Catalan全模型到导子8的完整参数两叶载体

2026-10-10。跨架构数值出口比较，独立子任务。只读核当前仓库HEAD为fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status --short空。实际FULL读Catalan的foundations、nonvanishing、real-place、odd-primes、energy、certificate、conclusion七份当前源；完整复制和实际读域见alternative_reading_scope.md。不重新运行作者的模101枢轴或实能量表，不声称本人Lean认证或全仓库数学认证。

**没有新的数值无理性定理。** 本轮给出一个不同于232/233截区模板的新完整周期身份：在完整区间的Cauchy核中引入参数，用其两条解析叶的3∶1组合，同时消除πlog(1+√2)与π通道，保留纯L(2,χ−8)及可由完整整数接触消掉的ζ(2)。这是实际全数组恒等式，不是有限头、参数扫描或把新导子贴到旧正Gram。

## 1. 成功证明的可移植接口与真实限制

当前Catalan稿先给每个raw列的完整M/Z周期分解，再用整数行P_r,D_r的tP_r/f−D_r=O(t^L)消掉ζ(2)，故G有理假设确使整个增长det有理。实处不是一个正Gram：原积分的两叶系数在正半区为−1/4、5/4；统一插值处理任意聚集nodes，Hilbert压缩代数地消掉evaluation determinant。Hadamard另付一整case；能量用匹配damping保留negative squares，最后才取统一suprema。

有限处也不是只算leading residue rank。odd-primes的digit lemma包含全部p²清整，完整边界约定M⁰(−1,j)及两种不同extraction shifts；central p层的shear保留noncentral列，不能把其未知次层依赖当清整。整个raw pool上的Z_p可逆变换和Cauchy–Binet支付整数filter。非零另用N=p的Frobenius及两个palindromic基，把实际48p矩阵归约到B₀、B₀±B₁三个固定48矩阵；successor行48的低阶系数必须保留。模101表是作者的一份完整有限certificate，本文读过全部配方与枢轴，但未重跑。

作者最终比较的是同一det：有限处normalized lower >−2.29084，实处upper ≤−2.290939875<−2.2909。其间距很小；换参数、导子、数域或sheet后不能借这两个数字。本文FULL读所有能量与certificate步骤，但未重新计算全部rational表，不把阅读替代独立程序认证。

| 架构 | 真实结论 | 下一项可移植全模型定理 |
|---|---|---|
| Catalan当前增长mixed矩阵 | 全列接触、完整finite flags、prime sequence非零与uniform energy共同成功 | 新目标必须在同一完整载体支付这些接口 |
| 252朴素χ−8正Gram | period matrix为rank-one bbᵀ；完整scalar整化后actual值≥[256(D+1)²64^D]⁻¹，D=O(m)时严格负m²预算被真正下界排除 | 必须改变period matrix结构，不再优化同一rank-one Gram |
| 232/233与252χ−8截区 | 完整period投影有用；低区对每个X均可用数值row-add消掉，没有关系专属支撑收益；实际谱点非零和净预算未付 | 新的完整载体/谱点证书，不能改名续查旧截区 |
| 下文完整参数两叶 | 纯χ−8周期的全数组、native Q接触与全n目标系数秩已推；hypothesis使实际条目落Q | 首先匹配同一完整生成载体、全前缀整数模型及其成本，继而独立非零/能量 |

前三行依据实际FULL读的232、233及252冻结稿。第二行是该具体类的数学下界，第三行是准入停止，不能互换成所有χ−8方法不可能。

## 2. 完整区间、参数与三个强制边界

令 f(t)=√(1−t²)取实正支，dμ(t)=|t|dt/f(t)，并令

\[
 m_i=\int_{-1}^1 t^i\,d\mu(t),\quad
 m_{2l}=\frac{2}{(2l+1)c_l},\quad m_{2l+1}=0,\quad
 c_l=4^{-l}\binom{2l}{l},\quad m_{-1}=0.
 \tag{C1}
\]

这是原Catalan的完整rational moment序列；没有截掉|t|<1/√2。对|u|<1设

\[
 M_u(i,j)=\int_{-1}^1\int_0^1
 \frac{t^is^j}{1-uts}\,ds\,d\mu(t)
 =\sum_{k\ge0}\frac{u^km_{i+k}}{j+k+1},
 \quad S_i(u)=\sum_{k\ge0}u^km_{i+k}.
 \tag{C2}
\]

初始域内积分、级数和参数微分绝对一致。置K⁻_d=M_u(d,0)、K⁺_d=M_u(0,d)，φ=arcsin u、v=√(1−u²)取0<u<1上的实正支。直接积分或C1给

\[
 S_0(u)=\frac{2\phi}{uv},\quad
 K^+_1(u)=\frac{\phi^2}{u^2},\quad
 K^-_0(u)=K^+_0(u)=\frac{J(u)}u,
 \tag{C3}
\]
\[
 J(u)=\int_0^{\pi/2}\log\frac{1+u\sin\theta}{1-u\sin\theta}\,d\theta,
 \qquad J'(u)=\frac{2\phi}{uv}.
 \tag{C4}
\]

S₀来自令y=cosθ后的有理积分。K⁺₁可用(arcsin u)²的Taylor式，其系数恰m_(2l)/(2l+2)；也可积分其微分方程，初值0唯一。C4在紧子域微分后令y=cosθ即得。J不是一个任意形式周期；J/u是当前完整二重积分的实际start。

为写清全部有限头，对u≠0有

\[
 S_i=u^{-i}\left(S_0-\sum_{k=0}^{i-1}u^km_k\right),\quad
 M_u(i,j)=u^{-1}\left(M_u(i-1,j-1)-\frac{m_{i-1}}j\right)
 \ (i,j\ge1),
 \tag{C5}
\]
\[
 K^-_1=(u-u^{-1})S_0+2/u,\quad
 dK^-_d=(d-1)K^-_{d-2}+S_{d-2}-S_d\quad(d\ge2),
 \tag{C6}
\]
\[
 (d-1)u^2K^+_d=(d-2)K^+_{d-2}+(u^2-1)S_0+\frac2{d-1}
 \quad(d\ge2).
 \tag{C7}
\]

C5是几何核身份。C6由C1的moment recurrence逐项得到；d=1用m_(−1)=0。C7把u²K⁺_d的级数移两位，k≥2项成为u^k(m_(k−2)−m_k)，另付k=0的boundary。它明确解释Catalan的特殊性：u=1时额外S₀通道消失；u≠1时不可沿用原两start配方。

## 3. 在参数1处的完整解析两叶

固定ρ=1/√2、E=1+√2。初始叶从0<u<1到ρ，称old。新叶是从ρ沿实区到1附近，绕u=1一次而不绕0、−1，再沿原路径返回ρ的解析延拓，称new。小圈大小可变，同一同伦类的结果相同。此monodromy是参数u的叶，不是把t的star当免费新值。

绕1后φ_new=π−φ、v_new=−v。因此S₀的新叶在ρ等于−3π，旧叶等于π；K⁺₁的新叶为9π²/8，旧叶为π²/8。J的常数也必须确定。由C4，

\[
 J'_{\rm new}-J'_{\rm old}=-\frac{2\pi}{uv},\qquad
 \frac d{du}\log\frac{u}{1+v}=\frac1{uv}.
\]

在u=1附近用局部参数v：dJ=−2φ/(1−v²)dv，而φ=π/2−arcsin v。这在v=0全纯，故两叶J在分歧点匹配，积分常数为0。于是

\[
 J_{\rm new}-J_{\rm old}=-2\pi\log\frac{u}{1+v}.
 \tag{C8}
\]

没有丢掉额外π²或任意integration constant。

由φ变量分部积分，及Clausen的绝对收敛Fourier定义，

\[
 J(u)=2\phi\log\tan(\phi/2)
      +2\operatorname{Cl}_2(\phi)+2\operatorname{Cl}_2(\pi-\phi).
\]

其导数使用∫log tan(φ/2)=−Cl₂(φ)−Cl₂(π−φ)；端点0取可积极限，Fourier导数可先作Abel正则化。对φ=π/4，逐项有限character identity给

\[
 \operatorname{Cl}_2(\pi/4)+\operatorname{Cl}_2(3\pi/4)=\sqrt2Y,
 \quad Y=L(2,\chi_{-8}).
\]

所以全部实际start为

\[
 \begin{array}{c|cc}
 &\mathrm{old}&\mathrm{new}\\\hline
 M_\rho(0,0)&4Y-(\pi/\sqrt2)\log E&4Y+(3\pi/\sqrt2)\log E\\
 S_0&\pi&-3\pi\\
 M_\rho(0,1)&\pi^2/8&9\pi^2/8
 \end{array}.
 \tag{C9}
\]

定义同一完整数组的sheet组合

\[
 \overline M=3M_{\rho,\rm old}+M_{\rho,\rm new},\qquad
 \overline S=3S_{\rm old}+S_{\rm new}.
 \tag{C10}
\]

则\(\overline M(0,0)=16Y\)、\(\overline S_0=0\)、\(\overline M(0,1)=3\pi^2/2=9\zeta(2)\)。这是3+T作用的准确含义：消掉此实际源的πlog E和π，保留Y；没有断言全部monodromy或所有奇数ζ被统一消掉。

## 4. 所有数组指标的period模块与接触

令K=Q(√2)。C5–C7在两叶上均为实际解析恒等式，故相加后全部moment头乘4：

\[
 \overline S_i=-4\rho^{-i}\sum_{k<i}\rho^km_k\in K,
\quad \overline K^-_1=8/\rho,
\]
\[
 d\overline K^-_d=(d-1)\overline K^-_{d-2}
          +\overline S_{d-2}-\overline S_d,
\]
\[
 (d-1)\rho^2\overline K^+_d
  =(d-2)\overline K^+_{d-2}+\frac8{d-1},
\quad
 \overline M(i,j)=\rho^{-1}
       (\overline M(i-1,j-1)-4m_{i-1}/j).
 \tag{C11}
\]

这些初值与递推完整定义每个i,j≥0的头，不能省finite heads。按C11传播三个start，得到

\[
 \boxed{\ \overline M(i,j)=H(i,j)
     +16Y\rho^{-j}c_{(i-j)/2}
     +9\zeta(2)\rho^{1-j}c_{(j-i-1)/2},
       \quad H(i,j)\in K.\ }
 \tag{C12}
\]

约定c_z=0除非z为非负整数。H由C11把两个period starts设0、保留所有rational inhomogeneous terms所得；无需假设Y、ζ(2)独立，因而这是指定的形式递推分解。minus even边界的homogeneous kernel为c_l，plus odd边界为ρ^(−2l)c_l；diagonal传播乘ρ^(−1)，正好给C12两个系数。

现在可保留原Catalan的整数P_r,D_r和完整接触范围j<L；不改其比例或扫新参数。普通Z满足Z(i,j)=Z⁰(i,j)+[i=j]ζ(2)，因此同一真实raw列

\[
 \mathscr F_j(r)=\overline M(P_r,j)
          -9\rho^{1-j}Z(D_r,j)
 =\mathscr H_j(r)
        +16Y\rho^{-j}\sum_i[t^i]P_r c_{(i-j)/2},
 \quad\mathscr H_j(r)\in K
 \tag{C13}
\]

在j<L精确成立：ζ(2)系数是9ρ^(1−j)[t^j](tP_r/f−D_r)=0。故若Y∈Q，整个raw pool与整数filter后的det都落K，而非未经支付的Q。

本period coefficient是有限Toeplitz型c_((i−j)/2)，不是252正Gram的bbᵀ；在单一even sector的monomial表示中(c_(r−k))是单位下三角，故这个核本身允许随维度增长的秩。此观察不证明当前固定P_r/filter实际目标矩阵满秩，也不支付关系点det非零。

## 5. 两个嵌入的比较与优先有理归一化

σ(√2)=−√2使ρ变成−ρ。C11的所有rational coefficients随ρ同样共轭，period starts16Y、9ζ(2)固定。在负参数处选old实叶φ=−π/4，再用映射u↦−u把绕1的路径搬为绕−1；new叶φ=−π−φ、v变号。S₀的两值仍π、−3π，M₀₀与M₀₁的两个值仍为C9。所以C12/C13在两个嵌入下由这对镜像canonical paths表示一致。若Y∈Q且ζ(2)已消，σ确作用于同一个K矩阵，而不擅自指定σ(Y)=−Y。

这**不是正测度载体**。new是完整参数积分的解析延拓，可能需要变形contour；不能把它换回old正区积分、从正核领取非零或套Catalan real-place bound。C13中ρ^(1−j)还改变了Z companion的column尺度：把Z的s变为ρs可见其对应support不再与M的原列区间一致，不能免费沿用原双Andréief integrand。

原生二变量生成函数在初始域是

\[
 \mathcal G_u(z,w)=\sum_{i,j\ge0}M_u(i,j)z^iw^j
 =\int\!\int\frac{d\mu(t)\,ds}
 {(1-zt)(1-ws)(1-uts)}.
 \tag{C14}
\]

逐系数monodromy已由C5–C12全部确定；把3+T在一个共同生成芽和合法contour上统一实现、证明其全系数边界及清整类型，还需要完整匹配证明。保存C14不等于支付CDT的全纯map、arithmetical holonomy秩或其strict条件。尤其ordinary Z的ρ^(−j)必须包含在同一生成载体里。

经B提出、Root与本文分别纸核的更好规范化是

\[
 \mathcal N(i,j)=\rho^i\overline M(i,j),\quad
 \mu_i=\rho^i m_i\in\mathbb Q,\quad
 U_i=\rho^i\overline S_i\in\mathbb Q.
 \tag{C15}
\]

奇moment为0、ρ²=1/2，故μ_i有理；U₀=0、U_i−U_(i+1)=4μ_i使全部U_i有理。完整native递推为

\[
 \mathcal N(i,j)-\mathcal N(i+1,j+1)=4\mu_i/(j+1),
\]
\[
 d\mathcal N(d,0)=(d-1)\rho^2\mathcal N(d-2,0)
                 +\rho^2U_{d-2}-U_d,
 \quad\mathcal N(1,0)=8,
\]
\[
 (d-1)\rho^2\mathcal N(0,d)
       =(d-2)\mathcal N(0,d-2)+8/(d-1).
\]

因此不仅period系数，整个head也实际在Q：

\[
 \mathcal N(i,j)=R(i,j)
  +16Y\rho^{i-j}c_{(i-j)/2}
  +9\zeta(2)\rho^{i+1-j}c_{(j-i-1)/2},\quad R(i,j)\in\mathbb Q.
 \tag{C16}
\]

两个非零period系数的ρ指数都为偶数。这是全n形式递推身份，仍不要求未知period已经独立。

对应native接触与真实raw列是

\[
 \frac{xP(x)}{\sqrt{1-2x^2}}-D(x)=O(x^L),\qquad
 \mathcal F_j(P,D)=\mathcal N(P,j)-9Z(D,j)\in\mathbb Q+\mathbb QY
 \quad(j<L).
 \tag{C17}
\]

因为ζ(2)系数恰9[x^j](xP/√(1−2x²)−D)。这消掉了K-Norm费用；C13的旧行K版本仅作为推导比较，不另开候选。原Catalan整数行不自动满足新conic接触。

一个确定的、无需有限n扫描的完整prototype由Root/B给出并经本文纸核：n≥1、r=0,…,n−1，

\[
 P_r(x)=2^n x^{2r},\qquad
 D_r(x)=\sum_{l=0}^{n-r-1}2^{n-l}\binom{2l}{l}x^{2r+1+2l}.
 \tag{C18}
\]

P_r,D_r为整数多项式，D_r恰是xP_r/√(1−2x²)的<2n jet，故所有raw j<2n满足C17。在选列j=2s、s=0,…,n−1的实际Y系数矩阵中，s>r为0、s=r为16·2^n，因此

\[
 \det\bigl([Y]\mathcal F_{2s}(P_r,D_r)\bigr)=(16\cdot2^n)^n\ne0
 \quad\text{对所有 }n\ge1.
 \tag{C19}
\]

这是同一完整两叶源的实际目标系数秩，故det作为形式Y多项式最高次数n且leading非零；不是实际Y处或任意固定有理关系点的非零证明。

native原始积分把x=ρt，t完整区间变为x∈[−ρ,ρ]，其conic为√(1−2x²)。ordinary Z的x support到1，超过branch点ρ；还要保留参数new contour及行尺度ρ^i。系数有理不证明这些同对象能量费用消失。

**建议唯一256 first gate**：固定ρ、3∶1参数两叶、native N及C18/C19 prototype，证明完整生成芽/contour与全部raw C17真正匹配；给所有规模、所有头、2和所有odd primepowers的全degree-prefix Z整数模型，成本须为exp(O(degree))，并记完整行尺度。仅有通用factorial的exp(O(degree log degree))上界，不作为进入quadratic费用比较的准入证书。若不能给这份全尺度匹配及费用证书，停止候选；不启动参数/prime/sheet-word扫描。通过也只允许另审关系点非零与同一实际能量，不继承原Catalan三fixed matrices、finite loss table或strict能量。

该候选与停放的截区源不同：区间完整、extra boundary channels来自参数monodromy并被实际3+T消去；其全period module不靠对任意X都成立的数值row-add制造收益。但这种差异只支付新接口，不证明它的最终预算更优。本文不提出其它导子、更多sheet组合或长期自动窗口。

## 6. 当前进展与限制

本轮新资产是C1–C19的完整纯χ−8period投影、额外π/log通道的实际消去、native Q全数组及prototype的全尺度目标秩。尚无完整优化整数费用、growing relation-point非零、合法统一contour能量或数值无理性；亦未证明新目标全球未解。使用作者公布Catalan结论作为baseline，所有迁移条件另外列明。

数学程序、有限n/参数/prime扫描、CAS、Lean、外Git写与旧producer均0。只做当前源读取/复制与纸面推导；未修改任何旧稿、main、policy或manifest。全局比较不以新增引理数量自动延长旧路线。

