# D12 真实Hecke填充盘的半径：Green函数、可计算级数与严格强上界

日期：2026-10-06。新proof note；不修改冻结source，不运行任何旧或peer producer。不做参数或prime扫描。本稿只研究[已证明合法的两张真实Hecke filled leaves](cdt_odd_level12_full_leaf_20261006.md)，参数分别w+=√12、w−=√588。给出精确conformal-radius表达和严格上界，不声称排除其它source、其它continuation surface或任意CDT方法。

## 1. 半径的准确含义与本轮结论

令G_w=〈T_w:z↦z+w,S:z↦−1/z〉、w>2。实际主源[Soares2020 pp1–2](../literature/soares2020_hecke_triangle_transfer_v1.pdf)给fundamental domain

\[
 \mathcal F_w=\{z\in\mathbb H:|\Re z|<w/2,\ |z|>1\},
\]

及one cusp、one funnel、one order2 elliptic。将唯一cusp填充、elliptic取coarse coordinate后，得到有解析circle边界的Riemann disk X_w。记其filled cusp为P，局部nome q_w=e^(2πiz/w)。对任意Riemann map F:(D,0)→(X_w,P)，定义

\[
 R(w)=\left|\frac{d(q_w\circ F)}{dz}(0)\right|.
 \tag{R1}
\]

q_w在P附近是合法local coordinate；不要求它在整个X_w单值。D12的tδ=q+O(q²)，所以本稿的R(w)正是目标map的|d(tδ∘F)/dz(0)|。第二支标准化z=√588(τ−2/7)只将q乘unit complex phase，因此其绝对值半径不变。

下文独立证明

\[
 \boxed{\log R(w)=\frac{2π^2}{w^2}
  \sum_{k\ge0}\ \sum_{n_1,\ldots,n_k\in\mathbb Z\setminus\{0\}}
      \frac1{c_k(n_1,\ldots,n_k;w)^2},}
 \tag{R2}
\]

其中空word的c0=1，c1=n1w，ck=nkw c(k−1)−c(k−2)。对λ=(w+√(w²−4))/2且π²/(3λ²)<1，正级数有严格可计算的geometric tail。实际两支因此满足

\[
 \boxed{\frac{\log R(\sqrt{12})+\log R(\sqrt{588})}{2}
       <\frac65=1.2<\frac{573}{253}.}
 \tag{R3}
\]

这个结论是指定真实盘的容量上界，不是数值实验；更接近的实数bound约1.1770715只作读者参考。它不把遗漏cap写成等式，也不计算实际J。

## 2. 唯一double coset words与continuant的全尺度控制

由fundamental domain和side-pairing，G_w=〈T_w〉*〈S〉≅Z*C2。G∞=〈T_w〉。每个非trivial double coset G∞\G_w/G∞有唯一reduced representative

\[
 g_k=S T_w^{n_1}S\cdots T_w^{n_k}S,
 \quad n_j\ne0,\quad k\ge0.
 \tag{R4}
\]

唯一性是free-product normal form：丢掉两端的T powers后仍由S起终；没有额外factor2，PSL中的central sign不改变这个normal form。c=0仅identity double coset。每个(R4)的全部left cosets是gk T_w^n、n∈Z，互不重复。

取determinant1矩阵。直接矩阵乘法给其lower row

\[
 (c_k,d_k)=(c_k,-c_{k-1})\ (k\ge1),\qquad
 (c_0,d_0)=(1,0),
\]

其中c0=1、c1=n1w，及(R2)中的递推。设λ>1，则λ+λ^-1=w。归纳证明

\[
 \left|\frac{c_{k-1}}{c_k}\right|\le\lambda^{-1},\qquad
 |c_k|\ge w\lambda^{k-1}\prod_{j=1}^k|n_j|\quad(k\ge1).
 \tag{R5}
\]

base case来自|n1|w≥w>λ。若上一ratio≤λ^-1，则

\[
 |c_k/c_{k-1}|\ge |n_k|w-\lambda^{-1}
 \ge |n_k|(w-\lambda^{-1})=|n_k|\lambda,
\]

给出下一ratio及product lower bound。这个论证处理任意sign pattern，不需要假设nj同号。特别所有ck非零，且|dk/ck|≤λ^-1。

令Z=2ζ(2)=π²/3。逐长度求和得到

\[
 \mathcal C(w):=\sum_k\sum_{n_j\ne0}c_k^{-2}
 \le1+\frac{Z/w^2}{1-Z/\lambda^2}.
 \tag{R6}
\]

不用第一步w而只用λ可得稍粗的1/(1−Z/λ²)。任意截掉全部length≤K后，余项至多

\[
 \frac{Z}{w^2}\frac{(Z/\lambda^2)^K}{1-Z/\lambda^2}.
 \tag{R7}
\]

每个固定length内的integer尾也由(R5)及Σn>L n^-2≤1/L严格控制。因此(R2)不仅给界，也给任意精度的计算算法。本文没有为逼近它而扫描words；只使用全尺度majorant。

## 3. 正harmonic级数、normal convergence与funnel边界

定义未缩放的cusp Eisenstein函数

\[
 E_w(z)=\sum_{G_\infty\backslash G_w}\Im(gz).
 \tag{R8}
\]

每项为正harmonic函数。按double cosets准确分组：若z=x+iy，a_g=d_g/c_g，则

\[
 E_w(z)=y+\sum_g\frac1{c_g^2}\,P_w(x+a_g,y),
\]
\[
 P_w(X,y)=\sum_{n\in Z}\frac{y}{(X+nw)^2+y^2}
 =\fracπw\frac{\sinh(2πy/w)}{\cosh(2πy/w)-\cos(2πX/w)}.
 \tag{R9}
\]

最后身份是标准periodic Poisson kernel，可直接用partial fractions或对每个Fourier mode积分证明。对任意compact K⊂H，y≥ε>0，故P_w≤(π/w)coth(πε/w)。结合(R6)，(R8)在所有compact上uniform正常收敛，和为harmonic。没有在s=1偷用只对Re(s)>1的有限面积Eisenstein结论；收敛已由(R5)直接证明。

left-coset绝对收敛允许重排，故E_w真正G_w不变。有限elliptic orbit上，在Cayley coordinate u中S:u↦−u；E_w是harmonic且even。写E_w=Re h(u)，其odd holomorphic part为0，因此h是u²的holomorphic函数。它在coarse elliptic coordinate u²中是regular harmonic函数，没有隐藏cone singularity。

还必须证明funnel边界为0。标准fundamental domain的real boundary代表是

\[
 J_w=[1,w/2]\cup[-w/2,-1].
\]

由(R5)，|ag|≤λ^-1<1。这些闭interval与所有poles −ag−nw统一分离：n=0和相邻n项的距离至少1−λ^-1>0，其余项随|n|线性增大。因此在x∈Jw、y↓0，P_w(x+ag,y)≤C_w y，Cw可取统一有限常数。结合Σcg^-2<∞，得到E_w→0 uniformly。这包括real interval两端的side identifications；Möbius gluing给真实funnel的解析circle边界。因此E_w在X_w的整个boundary连续为0。

## 4. Green函数与radius的准确归一

Poisson kernel的Fourier展开给

\[
 P_w(X,y)=\fracπw\left(1+2\sum_{m\ge1}
           e^{-2πmy/w}\cos(2πmX/w)\right).
\]

所有g系数由(R6)控制，故cusp处实际展开是

\[
 E_w(z)=y+\fracπw\mathcal C(w)+O(e^{-2πy/w}),
 \tag{R10}
\]

而且E_w−y−(π/w)C是q_w的convergent real harmonic Taylor series。

因此

\[
 G_w(z,P)=\frac{2π}{w}E_w(z)
 =-\log|q_w|+\frac{2π^2}{w^2}\mathcal C(w)+O(q_w)
 \tag{R11}
\]

为positive harmonic、boundary0、唯一P处的logarithmic pole；它在coarse elliptic point regular。唯一性由max principle：与Riemann disk的Green函数之差延拓过P且boundary0，所以为0。

若Riemann map的disk coordinate为ξ，则G=−log|ξ|；q_w=R(w)e^(iθ)ξ+O(ξ²)，所以

\[
 G=-\log|q_w|+\log R(w)+O(q_w).
\]

比较(R11)给(R2)。这里的常数是logR，不是R；没有额外cusp-width或order2因子。这也说明半径只依赖真实G_w surface及normalized q germ，不依赖另一个leading1的formal t坐标。

## 5. 两个固定参数的纯有理严格证书

用Archimedes严格boundπ<22/7，记P0=484/49>π²。对w+²=12，

\[
 \lambda_+^2=5+2\sqrt6>9.
\]

对w−²=588，λ−²+λ−^-2=586且λ−>1，所以λ−²>585。故(R6)给下列完全有理upper bounds：

\[
 U_+=\frac{P_0}{6}\left(1+
       \frac{P_0/36}{1-P_0/27}\right),
\]
\[
 U_-=\frac{P_0}{294}\left(1+
       \frac{P_0/1764}{1-P_0/1755}\right).
 \tag{R12}
\]

所有denominators严格为正。精确Fraction比较得到

\[
 \boxed{\log R(\sqrt{12})<U_+,
 \quad\log R(\sqrt{588})<U_-,
 \quad (U_++U_-)/2<6/5.}\tag{R13}
\]

这些常数的浮点值不是严格证明的一部分；严格性来自π的有理bound、根式lower及有理交叉相乘。相反，空word给unconditional lower boundlogR(w)≥2π²/w²，所以不是把真实radius假定为0或只得到模糊的上界。

## 6. 对当前地图族与cheap three-log账本的意义

任何holomorphic map f:(D,0)→(X_w,P)都满足其q derivative≤R(w)：先用Riemannmapinverse将其变成D的self-map，再用Schwarz lemma。因此(R3)也控制非单射、预先ramified或closed-disk缩小的maps，只要它们确实映到这两张Xδ并从唯一filled cusp起步。

[当前三个log packet稿](cdt_odd_level12_cheap_log_packet_20261006.md)的固定m23 safe成本upper是1146/529。使用该指定safe估计的plain CDT rank矛盾，Jensen必要平均logρ门槛是573/253。本稿严格证明这两张真实Hecke filled disks连这个必要条件也达不到。限制背景使domain变小不能改善radius；给t乘leading1的unit Möbius也不能改变它。

实际结论还不依赖采用哪个joint transport upper：同一原数组已证lower τ3≥1078/529，所以其最乐观Jensen门槛仍≥539/253>6/5。k2同样有τ2≥348/169，门槛≥29/13>6/5。故这两个指定原数组在这些真实Xδ上的plain rank矛盾失败，即使完成联合matching也不能弥补这个解析差距；这不涉及新增Smith折扣或其它数组。

这里要谨慎区分safe upper账本与全方法lower bound：本稿没有证明该账本τ是最优，也没有排除prime-dependent混合格、别的背景、额外真实symmetry或不同continuation surface。它不证明L3χ12无理或有理。特别追加已证M′ symmetry的更大group可能给另一surface，必须重新证明拓扑及半径，不能从(R13)直接排除；下一步将另核该固定更大group。

## 7. NEW固定证书与审阅状态

同名NEW producer只核symbolic矩阵递推、两个固定参数的根式事实、Poisson kernel的固定归一及(R12)的Fraction严格比较；不import任何旧producer，不枚举prime或research参数。作者首次、单次执行，35项全部通过；有理平均upper准确为30288738869708/25321733919363<6/5。有限checks不替代§§2–4的normal convergence、actual boundary0与Green唯一性证明。

主源使用已保存[Soares2020原件](https://arxiv.org/pdf/2005.11808v1)。本轮检索另将[Dyatlov MIT lecture24](https://math.mit.edu/~dyatlov/18.156/lecture24.pdf)保存为单独背景文献；该扫描讲义不是本稿数学证明的输入，不将文本抽取为空写成全文核对。本稿的s=1收敛与radius identity由正文独立证明，没有从finite-area scattering结果移用。

实际限定只读独审：Root全文阅读本MD和NEW源码，§§1–6通过unique doublecosets、first-w continuant、Poisson归一、normal convergence、real boundary与pole bands距离、coarse harmonic regular、Green唯一与logR归一、有理R12及factor-to-X scope；未运行35项producer。conjugate_projection实际阅读本稿，限定§§2–4独审同一关键链通过，确认没有额外width/order2因子；未运行producer。helper_tensor_budget实际只读§§2/5/6，核all-sign continuant、geometric sum与有理λ lower、budgetlower及仅这些Xδ的scope；未运行producer，其审核不替代§§3–4的全文读取。本文三件在此实际审阅状态冻结，不将base结论直接扩展到augmented群。
