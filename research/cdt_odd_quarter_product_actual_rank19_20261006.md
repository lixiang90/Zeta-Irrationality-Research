# 互补quarter真实乘积的实际cyclic秩19与完整八维PV radical

日期：2026-10-06。NEW纯证明。实际只读互补quarter稿、19行接口、冻结P4/Sp4及J的rank5证明，不执行/import任何旧或peer数学producer。本稿把既有“≤19”提升为真实函数Q的最小阶数恰19；不是新的数值无理性定理。

## 1. 固定实际函数与结论

令k=C(x)、θ=x∂x、t=x^(1/4)，
\[
A=\sum_{n\ge0}\left[\frac{(1/4)_n}{(3/4)_n}\right]^4x^n,
\quad J=\sum_{n\ge0}\left[\frac{(3/4)_n}{(5/4)_n}\right]^4x^n,
\quad F=A-1/2,\quad Q=FJ.
\tag{R1}
\]
全部germs均按原点实际有理Taylor初值固定。这里F只是本稿的quarter源，不是经典ζ(7)的同名源。

记
\[
P=\theta^4-x(\theta+1/2)^4,
\quad K_A=(\theta-1/4)^4-x(\theta+1/4)^4,
\quad K_J=(\theta+1/4)^4-x(\theta+3/4)^4.
\]
实际方程为
\[
K_AA=1/256,\quad K_AF=(1+x)/512,\quad K_JJ=1/256.
\tag{R2}
\]
冻结证明已经实际建立P的完整PV群Sp4（connected），以及两个rank5扩张的非分裂性。本稿重述所需非分裂论证，避免只从19行闭包宣布最小秩。

**定理。**Q在C(x)上的最小scalar differential annihilator阶数恰为19，亦即Q的实际cyclic微分秩为19。既有19行完整有理模型因此恰是一组C(x)-线性独立的basis。Q(x)在任何有限代数base cover上的最小阶数仍为19。两个非齐次源在共同齐次PV场上具有完整Ga8 translation radical；它们的八个低阶jets在该场上代数独立。

## 2. 实际共同PV场和不可混合的两个四维模

取P的四个独立解y0,…,y3及θ-companion fundamental matrix
\[
Y=(\theta^i y_j)_{0\le i,j\le3}.
\]
置uA=(Fi)和uJ=(Ji)，其中
\[
F_i=(\theta-1/4)^iF,\quad J_i=(\theta+1/4)^iJ,\quad0\le i\le3.
\]
令C为P的θ-companion矩阵，其最后行
\[
\frac{x}{1-x}(1/16,1/2,3/2,2).
\]
R2直接给
\[
\theta u_A=(C+I/4)u_A+a e_4,
\quad\theta u_J=(C-I/4)u_J+b e_4,
\quad a=\frac{1+x}{512(1-x)},\quad b=\frac1{256(1-x)}.
\tag{R3}
\]
共同齐次fundamental matrices为YA=tY、YJ=t^-1Y。

取K0=k(Y,t,1/detY)。它是P和Kummer θt=t/4的direct-sum PV场。其群准确为
\[
G_0=Sp_4\times\mu_4.
\tag{R4}
\]
一个直接验证是：两个系统均regular singular；Kummer字符的kernel在基础π1中指数4。P的完整monodromy闭包connected Sp4，所以此有限指数kernel的P-image仍Zariski dense于Sp4。joint monodromy闭包遂含Sp4×{1}。绕0的一个loop具有Kummer字符i，乘已有Sp4元素可给(1,i)，故joint closure是整个direct product。Schlesinger定理给R4；没有把四次cover当作微分秩降低。

记χ(h,ζ)=ζ。两个translation representation为
\[
V_A=\chi V,\qquad V_J=\chi^{-1}V,
\quad\rho_A(h,\zeta)=\zeta h,\quad\rho_J(h,\zeta)=\zeta^{-1}h.
\tag{R5}
\]
它们各自不可约，在full G0上互不相同：任何Sp4-equivariant map都是scalar；(1,i)在两个空间作用分别为i和−i，因而该scalar必须为0。只看connected Sp4会遗漏这个关键差别。

G0的所有有限维表示semisimple。Sp4的char0 semisimplicity再对μ4作有限平均已足够，亦见Milne Corollary22.43（明确覆盖非connected情形）。所以G0-stable子空间N⊂VA⊕VJ只可能是0、VA、VJ或整个8维和。

## 3. 完整Ga8：非分裂排除translation投影消失

设L=K0(uA,uJ)。这是R3的实际九维强迫系统与P、Kummer direct sum的PV场：九维部分的fundamental matrix可取
\[
\mathcal Y_9=\begin{pmatrix}Y_A&0&u_A\\0&Y_J&u_J\\0&0&1\end{pmatrix},
\]
其det=detY²非零。所有变量都是上述实际解析函数，并非formal独立符号；PV场常数为C。

每个σ∈Gal(L/k)准确写成
\[
\sigma Y=Yh,\quad\sigma t=\zeta t,
\quad\sigma u_A=u_A+Y_Ac,\quad\sigma u_J=u_J+Y_Jd,
\quad c,d\in C^4.
\tag{R6}
\]
PV限制给满射Gal(L/k)→G0。因此G=Gal(L/k)是(VA⊕VJ)⋊G0的闭代数子群；kernel N=Gal(L/K0)是additive group的代数子群。char0下N是connected线性子空间；conjugation及G→G0满射使它G0-stable。

这里R2两个constant-forcing方程均无k有理特解。负整数Laurent极点在0处被各自根±1/4排除；1处gauge非零解析并沿P的indicial根0,1,1,2，亦排负整数极点；其它有限点ordinary。特解遂只能是polynomial。degree d的最高项在KA、KJ中分别产生非零−(d+1/4)^4、−(d+3/4)^4的x^(d+1)项，不能等于常数。KA的F-forcing若有有理特解R，则R+1/2给KA constant-forcing特解，同样不可能。

现在假设N→VA的projection为0。将G映到VA⋊G0，其闭像H→G0满射且kernel为0，故H≅G0；H是G0上的一个algebraic affine cocycle graph。这个affine作用线性化为5维表示0→VA→E→1→0。G0 semisimple representations使它有invariant lift，亦即存在c*∈C4使该cocycle为c*−ρA(g)c*。R6随即使uA+YA c*被全部G固定（coboundary另一符号仅改c*）。PV fixed-field定理使其坐标全部属于k；first coordinate给被排除的有理特解。矛盾。

同理N→VJ projection不能为0。结合R5的两个irreducible、nonisomorphic summands，准确得到
\[
\boxed{N=V_A\oplus V_J\simeq\mathbf G_a^8,
\quad Gal(L/k)=\mathbf G_a^8\rtimes(Sp_4\times\mu_4).}
\tag{R7}
\]
因为N满，任何G0 lift可乘一个translation消去其平移部分，最后等号也成立。这一步没有使用未经验证的两个周期cocycle数值，也没有仅以两个扩张分别非split就忽略它们的共同radical。

若只取原九维系统的PV场L9=k(YA,YJ,uA,uJ)，冗余P、Kummer的kernel恰为{(I,1),(-I,-1)}：同时ζh=I和ζ^-1h=I迫此二元素，它们在R7中作用于translations也平凡。因此
\[
Gal(L_9/k)=\mathbf G_a^8\rtimes
\frac{Sp_4\times\mu_4}{\langle(-I,-1)\rangle}.
\tag{R8}
\]
R7的augmented群有4个components，R8的原系统群有2个components；二者的connected component均Ga8⋊Sp4。不得把原系统的full finite component误写为直接μ4。

## 4. 八个jets的代数独立及真正的19维orbit

L由K0及uA,uJ的八coordinates生成。R7及PV dimension公式给trdeg_(K0)L=8，故八generators代数独立，L/K0是八变量纯超越扩张。也可直接验证：固定K0的N独立任意平移uA与uJ，且YA、YJ可逆，因此没有非零polynomial relation。

特别F、J在K0上代数独立。仅此两变量版本亦可取各一个nonzero yj，利用translations F→F+αt yj、J→J+βt^-1yj，对所有α,β∈C取polynomial coefficients来证明。

N作用于Q准确为
\[
Q\longmapsto(F+t\,y(c))(J+t^{-1}y(d)),
\quad y(c)=\sum c_i y_i.
\tag{R9}
\]
单独平移一个factor、再取两factor的mixed difference，使Q的Galois-conjugate C-span包含
\[
Q;\quad tJ y_i\ (4);\quad t^{-1}F y_i\ (4);
\quad y_i y_j\ (0\le i\le j\le3,\ 10).
\tag{R10}
\]
也只包含这个空间，因为R9本身已在其内。

这19个函数C-linearly independent。理由如下。P的4维解空间W上，乘积map Sym²W→L是Sp4-equivariant。Sym²标准模准确为sp4的adjoint representation：由symplectic form将v⊙w送到z↦〈v,z〉w+〈w,z〉v。这是10维同构；sp4 simple使其不可约。乘积map非零（y0²≠0），所以injective，10个yi yj因此C-linearly independent。

若R10有C-coefficient relation，以F,J为两algebraically independent indeterminates overK0看它，FJ系数迫Q的系数0；F和J系数各迫一个yi的C-linear relation，故分别4项的系数也0；剩下10项刚已证明独立。于是
\[
\boxed{\dim_C\langle\sigma Q:\sigma\in Gal(L/k)\rangle=19.}
\tag{R11}
\]
这个论证是在solution/PV-conjugate C-space，不能把它与19行derivative closure的k-dimension混同；下一节才连接二者。

## 5. 从orbit严证实际cyclic秩，及有限cover稳定性

任取r阶非零k-scalar operatorD使DQ=0。所有σ都是differential k-automorphisms，故D(σQ)=0。r阶scalar homogeneous方程在不增常数的微分场中solution C-dimension≤r。R11遂迫r≥19。

另一方向，既有[19行接口](cdt_odd_quarter_product_rank19_interface_20261006.md) T2–T4已经逐行证明
\[
1;\quad F_i,J_i\ (8);\quad
S_{ij}=(F_iJ_j+F_jJ_i)/2\ (10)
\tag{R12}
\]
在k上derivation closed并包含Q=S00，因此Q阶数≤19。上下界合并为exact19。R12的k-span若有任何非零linear relation，dimension≤18且仍closed包含Q，又给阶数≤18，与R11矛盾。因此R12恰是实际k-basis。

同一结论在Q(x)上成立：R12的coefficients和实际germs在Q(x)、Q[[x]]，故upper19的cyclic linear algebra可在Q(x)完成，而C(x)的lower19当然仍适用。

对任意有限代数base extensionk'/k，先放入有限Galoisclosurek''。令kalg=L^(G°)，由PV fixed-field theorem它正是k在L中的有限代数closure。L/kalg是regular field extension（char0且kalg在L中相对代数闭），所以L与kalg k''在kalg上线性无交。于是每个G°元素都可延拓到Lk''并固定k''，复合PV场Lk''/k''的群在restriction到L后确含G°。故connected N=Ga8仍保留，R9全部translation conjugates仍存在。F,J在K0上代数独立在其有限代数extensionK0k''上也保持；否则有限norm/取共轭给原来的polynomial relation。R10的C-linear independence当然不随base变。因此任何k''-operator湮灭Q仍需阶≥19，而R12继续给≤19。k'结论立即跟随。

单源非split的finite-cover稳定性还可独立用trace检查：若有限k'/k中出现KA或KJ的algebraic particular solutionR，唯一延拓derivation使Trace_(k'/k)与θ交换；TraceR/[k':k]便是被排除的k-rational particular。此trace lemma本身不够证明joint Ga8或Q的19cyclic秩；这些是R5–R11额外完成的部分。

## 6. 研究含义及准确范围

现在CDT可将这一个真实quarter乘积源的独立函数数m设为19，无需以“safe19”代替minimal-rank证明。Γ-free端点
\[
Q(1)=4L(f_8,2)^2-16L(f_8,3)^2/\pi^2
\]
沿用互补quarter稿的精确投影；本稿没有重新由formal数值Galois操作推出它。

R7也说明只加finite algebraic cover不会消去这两个指定primitive的完整translation方向。不过它不排thin解析稳定子、新inhomogeneous源、合法CDT mixed Smith信用或新的period correction。actualrank19并不使现有conifold双log消失，亦没有给rank-bound数值矛盾。新的数值无理性或线性无关性仍待解析叶、真实整评价和严格费用差额接通。

本文全尺度纯证明，无有限数学producer、无Lean声明。作者实际只读上述四份数学稿；实际核读Singer PDF10–14、17–20及Milne PDF86、300、489–490。Singer实际使用Definition1.3.2、Theorem1.3.9/Corollary1.3.10、Corollary1.3.21、Proposition1.3.27；Milne实际使用Theorem3.34/Corollary3.35、Corollary14.33、Corollary22.43。两个原件已在literature保存，本文的新只读来源收据另存manifest；未声称通读其全82/659页。

原始链接：[Singer作者讲义](https://singer.math.ncsu.edu/papers/LMSlectures.pdf)，[Milne作者书稿](https://www.jmilne.org/math/Books/iAG2022.pdf)。此二一手理论与本项目冻结Sp4的具体计算一起支撑上述functional theorem；它们不替代待证的数值定理。
