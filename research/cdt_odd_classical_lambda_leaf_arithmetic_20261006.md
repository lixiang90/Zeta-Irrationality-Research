# Classic spin/ζ(7)：真实共同 λ 叶、Jensen 与完整坐标成本接口

日期：2026-10-06。NEW 纯证明稿，不运行、import 或改动任何旧/同行 producer，不扫描参数、degree、word 或素数。输入为[实际 spin](cdt_odd_classical_spin_pullback_20261006.md)、[forcing spin](cdt_odd_classical_zeta7_forcing_spin_20261006.md)、[完整目标 rank10](cdt_odd_classical_zeta7_full_rank_20261006.md)与[经典投影算术](cdt_odd_classical_derivative_projection_20261006.md)。本文作者实际只读新 rank10 稿 §§2–5并独审核其 Laurent-log、reciprocity 与 actual quotient 链；不执行它的有限证书。

本文得到同一实际函数包的合法共同盘、avoid1/unique0 地图类的 sharp capacity16、一个可精确计算 ordinary Jensen 的固定窗口，以及 source/graded lattice 的坐标转化公式。另给 forcing 全阶安全分母、primitive A 的 dyadic 必要成本和 Levelt 原格的 saturated primitive5/index8。它们没有拼成完整 F2 的最优算术费，没有新的无理性定理，也没有对所有 transported conifold branches 或完整解析叶作分类。

## 1. 同一 actual 包与三奇点范围

令 x=256z、θ=x∂x=z∂z，实际 germ 为
\[
\begin{aligned}
y_0(x)&={}_4F_3(\tfrac12,\tfrac12,\tfrac12,\tfrac12;1,1,1;x),\\
A^x(x)&=\sum_{n\ge0}A_n(x/256)^n,\\
H(x)&=\sum_{n\ge1}\frac{(n-1)!^4}{(1/2)_{n+1}^4}x^n,\\
F_2^x(x)&=\sum_{n\ge0}[C_{n,2}+91440\zeta(7)A_n](x/256)^n .
\end{aligned}
\tag{L1}
\]
输入已实际证明 P4=θ4−x(θ+1/2)4 的齐次rank4、L5的 primitive exterior rank5，以及 KH=16x，K=(θ+1/2)4−xθ4。完整 F2 不是齐次 L5 解：
\[
L_5F_2^x=G=960x-\tfrac32x\theta^2
(48\theta^3+80\theta^2+40\theta+5)H.
\tag{L2}
\]
新实际 rank10 证明给一组真正函数基
\[
\mathcal B_{10}=\{1,H,\theta H,\theta^2H,\theta^3H,
F_2^x,\theta F_2^x,\ldots,\theta^4F_2^x\}.
\tag{L3}
\]
这里 W_G=W_H、forcing rank5及完整非split目标rank10均有实际证明；不能把这组函数删成rank5或把spin入口当rank4目标。ζ(7)∈Q的反证假设使相应 z/x-germs属于 Q[[z]]/Q[[x]]，不改变 actual rank 或函数的数值。

P4、L5、K及其上述实际系统仅在0、1、∞有奇点；全部 L1 的指定 germs 在0真正 Taylor-regular。各 Euler derivatives也在0 regular。任意附加背景只有在它本身的实际 rational differential system 仍无其它奇点、且所选 germ 在0 regular时才由下节共用叶；不能从composition factor相似自动赠送这个性质。de-log Frobenius regular parts可经其实际 triangular variational equations核此条件，但它们的独立秩不在本稿免费追加。

## 2. 真实 cyclic 共同叶与 sharp16：不是降低微分秩

使用主文献[Long–Tu作者讲义 Theorem1.20，PDF16–17](../literature/long_tu2021_hypergeometric_lectures_lambda_20261006.pdf)识别
\[
\lambda:\mathbb H\longrightarrow
Y=\mathbf P^1\setminus\{0,1,\infty\}
\]
为Γ(2) uniformizing cover。归一 q=exp(πiτ)，cusp deck T0:τ↦τ+2。NIST给
\[
\Lambda(q):=\lambda(\tau)=16q\,U(q),\quad
U(q)=\prod_{n\ge1}\left(\frac{1+q^{2n}}{1+q^{2n-1}}\right)^8,
\quad U(0)=1.
\tag{L4}
\]
公式和nome定义见 [23.17.4、23.17.7](https://dlmf.nist.gov/23.17)、[23.15](https://dlmf.nist.gov/23.15)。原件与实际读取范围存[独立文献清单](../literature/manifest_cdt_odd_classical_lambda_leaf_20261006.json)。不把这个 rank2 Legendre uniformizer当作rank4 spin方程的解或其模块降阶。

H/〈T0〉是 punctured q-disk D*。L1–L3每个实际 germ 的0-loop monodromy固定其自身，因为它们在0 Taylor-regular；因此在 universal cover的解析延拓对 T0 不变，真正在同一个D*上下降，并在q=0按原germ填充。得到一个共同 simply connected leaf D。Λ在D全纯，Λ−1(0)={0}且零点simple，Λ不取1、没有pole；λ的 covering 性也给 q≠0的derivative不为0。故所有 native x/z derivatives在该盘上全纯，不需因假想额外critical点另清pole。

这是一个已经完整认证的共同叶，未声称它是全部 zero-period subgroup的最大叶。原K(x)-线性独立性在 Λ pullback后（仍以K(Λ)为系数域）保留，因为 Λ 有open image；计CDT时仍是原 rational-variable rank10。将q直接当 coefficient variable，转到K(q)则不免费保留有限Dfinite秩。有限 **代数** cover保留输入的connected Sp4/irreducible ranks；这里的 infinite analytic leaf也不授权原K(x) rank降低。

更强的地图类结论可以单独严格证明。若 φ:D→C 全纯，φ(0)=0且simple，φ−1(0)={0}、φ不取1，则φ|D*的 fundamental-group image正好是Y的0-loop cyclic subgroup（至basepath conjugacy），因为原点winding为1。cover lifting因此给 f:D*→D*、φ=Λ∘f。f有界，填0后全纯；f非constant，maximum principle给|f(0)|<1，再由φ→0及 Λ 的唯一zero迫 f(0)=0。Schwarz lemma于是给
\[
\boxed{|\phi'(0)|=16|f'(0)|\le16.}
\tag{L5}
\]
Λ本身达到16。这个 sharp bound仅是 **omit1与unique simple0** 类；如果实际另一branch能填某个1-slot，必须另核其完整period identity，不能从这里宣布allbranches cap。root已证 canonical F2 branch在1不可去，仍不代替其它 transported slots的分析。

## 3. 合法闭圆盘 maps 与一个 exact ordinary Jensen窗口

对任意预先固定0<r<1，取 φr,x(u)=Λ(ru)。它在闭单位圆盘的邻域全纯，所有共同函数pullbacks也如此，因为rD紧含实际共同叶。这里r是符号全区间，不作数值参数优化。准确有
\[
\rho_{r,x}=\log|\phi_{r,x}'(0)|=\log16+\log r,
\quad \phi_{r,z}=\phi_{r,x}/256,\quad
\rho_{r,z}=\log r-\log16.
\tag{L6}
\]
注意原整数A源的 coefficient variable是z，不是x。

定义ordinary双Jensen指标（normalized Haar measureμ）
\[
J_{r,x}=\int_{\mathbb T^2}
\log|\phi_{r,x}(u)-\phi_{r,x}(v)|\,d\mu(u)d\mu(v).
\tag{L7}
\]
因为map在闭盘邻域analytic且unramified，log的diagonal及其它isolated correspondence零点可积。对固定v按u作Jensen，再平均v，严格给
\[
\begin{aligned}
J_{r,x}&=\rho_{r,x}+E_r,\\
E_r&=\int_{\mathbb T}\sum_{\substack{a\in D\,:
\phi_{r,x}(a)=\phi_{r,x}(v)}}
\operatorname{mult}(a)\log\frac1{|a|}\,d\mu(v)\ge0.
\end{aligned}
\tag{L8}
\]
finite zero-count在每个v按闭盘解析性理解，boundary零点的weight0；μ_v log|φr,x(v)|=ρr,x由 L4 的unit U直接给出。于是不是假定J的lower floor可达到，而是列出此map的exact额外项。

Λ在|q|<r0=exp(−π/2)上准确univalent。若Λ(q1)=Λ(q2)，取 τ2=γτ1、γ=(a,b;c,d)∈Γ(2)。c=0时q1=q2；c≠0时|c|≥2且
\[
(\Im\tau_1)(\Im\tau_2)
=\frac{(\Im\tau_1)^2}{|c\tau_1+d|^2}\le\frac1{c^2}\le\frac14.
\tag{L9}
\]
两个q均在|q|<r0时，两height均>1/2，与此矛盾。反之γ=(1,0;2,1)发送τ1=−1/2+i/2到τ2=1/2+i/2，给q1=−ir0、q2=ir0的两个不同preimages。故r>r0时Λ在rD不单射；本稿不从此单独猜E_r的精确值。

对0<r≤r0，内部没有其它preimages，故 L8 真正达到floor：
\[
\boxed{J_{r,x}=\rho_{r,x},\qquad
\rho_{r,x}\le\log16-\pi/2.}
\tag{L10}
\]
在原z坐标，Jr,z=Jr,x−log256，且ρr,z=ρr,x−log256，所以
\[
J_{r,z}-\rho_{r,z}=E_r\ge0.
\tag{L11}
\]
Jensen额外项在这种常数坐标缩放下不变，但 capacity的绝对值变了，必须与下节source/grade一起核。

对任何原z、omit conifold z=1/256与unique simple0类，L5等价给 |φz′(0)|≤1/16。因此ρz≤−log16<0。若使用现有标准componentwise非负costτ及ordinaryJ≥ρ，则plain holonomy矛盾需要m(ρ−τ)>J，必要(m−1)ρ>mτ≥0，不能成立。这只排 **这个坐标、这类maps、普通J与非负componentwise账本**；不排已证明mixed determinant收益产生的新指标或其它真实叶。

## 4. x=256z：source与graded determinant的精确账本

令α=256。给任意已独立证明的actual scalar tuple fi,z(z)，设 fi,x(x)=fi,z(x/α)。degree≤D source unit bases为 z^jfi,z 与x^jfi,x（0≤j≤D）。选完整leading square evaluation minor，roworders n∈V_D，columnorders j重复每species；其矩阵准确满足
\[
M_x=\operatorname{diag}(\alpha^{-n})\,M_z\,
\operatorname{diag}(\alpha^j),
\qquad
\det M_x=\alpha^{\sum_jj-\sum_nn}\det M_z.
\tag{L12}
\]
这只是actual coefficient substitution恒等式，无需假设所有Smith向量独立。

尤其在p=2，v2α=8，固定prime造成
\[
v_2(\det M_x)-v_2(\det M_z)
=8\left(\sum_jj-\sum_nn\right).
\tag{L13}
\]
若使用同一 closed rank m系统的 Shidlovsky leadingflag范围N=m(D+1)+O(1)，删去O(1)行，
\[
\sum_jj=\tfrac m2D^2+O(D),\quad
\sum_nn=\tfrac{m^2}{2}D^2+O(D),
\]
因此该determinant差的主项为−4m(m−1)D²。这里需原系统有效multiplicity估计给这条N；本稿不只据dimension猜全部leadingorders。实际rank10可用既有 closed-system Shidlovsky条件核接，但 L12–L13 的精确公式本身不依赖此渐近。**固定素数2可以贡献D²主项，不能以“坏素数有限”忽略。**

更直接的same-lattice版本是：原source格转为⊕Z·α−j x^jfi,x，原grade z^n转为Z·α−n x^n。使用这些转移基，evaluation仍就是Mz；换成两端unit-x基才出现 L12 的factor。所有arch/nonarch norm及degree也必须按这两个格变换；product formula Σv log|α|v=0给常数缩放的完整adelic平衡。不能只保留 L6 的arch解析增益，再把finite-place和source/graded degree留作原值，也不能从 L13 单独宣布新的τ。

L4还有一个严格的全n formal arithmetic接口：设t=q/16，则
\[
z(t)=\frac{\Lambda(16t)}{256}=tU(16t)\in\mathbb Z[[t]],
\quad z(t)=t+O(t^2),\quad t(z)\in\mathbb Z[[z]].
\tag{L14}
\]
最后式由unit-leading reversion递推直接得；并不是在 q-variable免费用leading1/16的反演。两个方向的prefix substitution matrices均为integer unitriangular，所以每个实际function的最小公共prefix分母在z与这个formal t中准确相同。但 L14 的自然analytic域只有 |t|<1/16，并且t是transcendental uniformizer，不能由此声称 fi,z(z(t))仍有相同Q(t)-Dfinite rank。它可作参数与prefix整性接口，不作未经证明的新 rational-variable CDT tuple。

## 5. 两个实际source方向的全尺度算术，不拼成F2最优费

### 5.1 强制非齐次carrier的安全LCM4与完整odd band

写 a_n=(n−1)!4/(1/2)_(n+1)4，n≥1，ΔN=lcm(1,…,N)。对odd u=p^a，n=ku+r，0≤r<u，有
\[
\#\{1,3,\ldots,2n+1:u\mid\cdot\}
-\left\lfloor\frac{n-1}{u}\right\rfloor
={\bf1}_{r\ge(u-1)/2}+{\bf1}_{r=0}\le1.
\tag{L15}
\]
u≥3使两条件互斥。高于2n+1的层两者均0。因此所有 n≤N 的 a_n和 h_n=256^n a_n满足
\[
\boxed{\Delta_{2N+1}^4a_n,\ \Delta_{2N+1}^4h_n\in\mathbb Z.}
\tag{L16}
\]
p=2没有遗漏：denominator odd product是2-unit，准确v2a_n=8n−4s2(n−1)≥0，s2是binary digit sum；乘256^n只增整性。

对任何odd prime p，n=(p−1)/2时odd product恰含一次p、factorial p-unit，故v_p(a_n)=v_p(h_n)=−4。N<p≤2N+1整带进入prefix，所以该carrier最小prefix denominator M_N有
\[
4N+o(N)\le\log M_N\le8N+o(N).
\tag{L17}
\]
这不是exact8，也不是complete F2的成本。为接原CDT固定LCM类型，可先固定任何ε>0：N足够大时Δ_floor((2+ε)N)^4覆盖 L16，其有限initial项用一个固定整数清掉，然后再ε↓0。Euler derivatives不增分母。没有把2N+1偷偷替换成2N的逐项整性。

### 5.2 spin regular period的坏prime2不能免费删除

y0,x第n系数为 binom(2n,n)^4/256^n。由v2 binom(2n,n)=s2(n)，准确有
\[
v_2([x^n]y_0)=4s_2(n)-8n.
\tag{L18}
\]
所以采用这个真实CY4周期作为x数组背景，prefix至少需2^(8N−O(logN))。原z period y0(256z)全系数integer。L18只给这个实际source方向的必要row成本，不给整个mixed evaluation determinant的exact值。

### 5.3 实际primitive A的dyadic系数同样有不可忽略成本

从已证Wronskian P9，取c_n=binom(2n,n)^4、b_n=8c_n(H2n−Hn)，c0=1、b0=0。这里b_n是rational，并未假定全integer。对n≥1，完整coefficient identity为（n=0则直接A0=1）
\[
A_n=2c_n+n b_n+
\sum_{\substack{i+j=n\\i,j>0}}c_ic_j+
\sum_{\substack{i+j=n\\i,j>0}}(j-i)c_ib_j.
\tag{L19}
\]
令n=2^k。k=0时两interior sums为空，c1=16、b1=64，因此A1=96、v2A1=5。对k≥1，v2c_n=4；nharmonic difference中ℓ=2n唯一给n/ℓ=1/2，其余ℓ=n+1,…,2n−1的2-adic valuation至少1，故v2[n(H2n−Hn)]=−1，v2(n b_n)=6。

对positive i+j=2^k，设a=v2j。binary complement gives s2i+s2j=k−a+1≥2，所以第一interior sum每项v2≥8。第二sum在j=i时weight0；否则v2(j−i)=a+1，而仅使用安全harmonic bound v2(H2j−Hj)≥−floor(log2(2j))≥−k，给
\[
v_2((j-i)c_i b_j)
\ge4(k-a+1)+3+(a+1)-k
=3(k-a)+8\ge11.
\tag{L20}
\]
于是除2c_n以外全部mod64消失，而2c_n赋值5。得到全k精确结论
\[
\boxed{v_2(A_{2^k})=5.}\tag{L21}
\]
因此x-variable A^x的prefix在N=2^k需2^(8N−5)。这是一个全尺度指定子序列证明，没有采样k或执行producer；它不等于声称所有N的精确growth，也没有排 F2=C2+91440ζ7A 在反证假设中的2-adic cancellation。

### 5.4 完整actualrank10的一个明确安全表

原z中的 C2与假ζ7∈Q下的F2有冻结的全prefix表 D0 ΔN³Δ2N⁸。L16给h_z=H(256z)较廉价的四列b≈2表，全部Euler rows不增分母。故先固定ε>0，给 L3 中forcing四行rate≤8+4ε、target五行rate≤19+8ε、constant0的明确arbitrary-matrix安全输入；或者将九条非constant统一inflate到三列b1和八列b2+ε，得到原nested类型安全表。D0清掉目标rational假设与有限initial项。

这些只是安全upper；没有用 L17、L18、L21拼成complete F2的exact必要cost或声称target的2-adic主部。由于本map类原z capacity负，现有非negativecomponentwise普通CDT门槛仍打不开。若改用x，必须实际重新证明所有rows的完整2-adic模型并带入 L12–L13；不能只把odd bands与archlog16挑出来使用。

## 6. Levelt J给真正饱和primitive5格，但尚无Taylor信用

使用冻结Levelt Λ=Z4与交替form J（spin P14），其Pfaffian为−4、detJ=16。entries gcd1，故polarization elementary divisors为(1,4)。它不是已证明的CY integral principal symplectic period basis。

在Λ²的ordered basis(e12,e13,e14,e23,e24,e34)，J-contraction为
\[
c_J=(1,0,-5,1,0,1).
\tag{L22}
\]
因为cJ(e12)=1，W=ker cJ是primitive saturated rank5 sublattice，明确basis
\[
e_{13},\quad e_{14}+5e_{12},\quad e_{23}-e_{12},\quad
e_{24},\quad e_{34}-e_{12}.
\tag{L23}
\]
Levelt generators保持J，所以保持W。primitive invariant bivector为\(\Omega=4J^{-1}\)，按这个basis是(1,0,1,−5,0,1)，cJ(Ω)=−8；Ω的entries gcd1，所以Q=Λ²/ZΩ也free rank5。W映Q注入且
\[
\boxed{[Q:\operatorname{image}W]=8.}\tag{L24}
\]
证明：Λ²/W=Z由cJ给出，而Ω映−8；或在(e12,Wbasis)中Ω=−8e12+(e14+5e12)−5(e23−e12)+(e34−e12)。因此W与quotient primitive5在odd p上integrally一致，p=2有明确固定index，不可误写成unimodular外平方分裂。

若保持这个J，任何unimodular-overlattice的index必要为4，因为detJ′=16/index²；本稿没有证明有Levelt-invariant这样的overlattice，更未把它识别成几何Betti格。指数8只是一份固定topological comparison：若此fixed comparison真正在CDT sources/grades的整模型中给每source-column bounded fixed denominators，则总O(rankE_D)成本对D²主项是小项；但 **没有该Taylor/deRham comparison时，不能推finite-place evaluation heights**。L18/L21正示范“单值matrix整数”与“coefficients整数”不同。

新的净信用需一个实际comparison：同一 L3函数、source polynomial lattice、全部graded evaluations在各p的完整包含关系，说明哪些p-dependent filtration获得多少determinant收益，以及比较的arch norm/degree。只有Levelt detJ=16或GL4(Z)不提供这一步。本稿得到真实饱和格和explicit index，却不认领一个尚未证明的τ折扣。

## 7. 范围、实际读取与待审

本稿正接口是共同λ叶与exactJensen小窗口、完整coordinate/grade恒等式、forcing安全four-layer和primitive A的指定dyadic必要成本、Levelt saturated5/index8。rank10、两non-split输入来自实际full-rank/forcing证明，本文不重建Sp4或CY resolution。

所有当前source在canonical0 Taylor-regular，使 L3合法共用叶。其它branch可填1、其它source有额外真实零周期、p-dependent mixed格或新的bundle指标须另证；不能把本稿avoid1/unique0范围扩大为全部解析方法失败。尤其数值irrationality仍未得到。

NEW文献原件三份及manifest保存literature；实际读Long–Tu title与PDF15–17，NIST23.15 nome/lambda定义、23.17.4/7。作者实际只读冻结spin/forcing/classicalprojection正文，新fullrank§§2–5；没有执行/import任何旧或同行producer。本文纯MD，没有为可直接证明的符号恒等式增加镜像测试。

根任务实际只读全文§§1–7并独审通过，覆盖真实cyclic叶/Schwarz sharp16、Jensen univalence cutoff、L12–13同格坐标主项、L15 odd全层、L19–21完整dyadic A与饱和primitive/index8；未执行producer。

conjugate_projection 随后实际只读§§2–6限定独审通过：cyclic Γ2 cusp quotient与fill0/Schwarz16、Jensen全部preimage项及精确univalence cutoff、source/grade α^(j−n)与fixed p2主项、formal整数双向反演的Dfinite限制、forcing全prime LCM4/band、完整A convolution与全k dyadic valuation、J饱和primitive/index8。它未执行producer、未重证upstream Sp4或最优算术费，未把结论扩大为所有transported分支或新mixed净信用。root仅在数学正文不变的前提下追加此实际审阅记录，本文与文献清单现冻结；后续新模型另稿。
