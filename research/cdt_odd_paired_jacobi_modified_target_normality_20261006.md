# 原临界目标的 modified moment 公式、middle 特征多项式与实际源全阶单位

2026-10-06，/root/conifold_arithmetic_hypothesis。NEW 研究稿，待实际独审。455冻结数学输入及所有旧/同行producer全部只读，无执行/import/rerun。冻结09b9 Jacobi稿及129070 receipt不改。本稿未证明原G0/M5在无穷辅助素数上同时为单位，也没有新的ζ/L数值定理。

本轮直接针对原目标，给出不用未知norm作分母的实际connection/compound Christoffel公式、固定middle值2的精确Loewner/bordered判据；另证明实际Q四源的全阶unequal-profile Hankel单位，而非仅derived endpoint单位。最后在同一χ-preserving诊断族中给两个真正退化实例，严格证明这些结构不能自动下传为原临界normality。

## 1. Same object 与 middle 参数的含义

取p=18r+1为素数，r≥1，a=5r，N=a+1，F=Fp。所有量来自实际冻结K1–K26：

\[
u_k=k^2,\quad S(u)=\prod_{k=a+1}^{9r}(u-k^2),\quad
R_k=S(u_k)^4,\qquad 0\le k\le a.
\tag{T1}
\]

点u_k彼此不同，S(u_k)和R_k皆unit。定义**基础folded权重**

\[
v_0=\tfrac12S(0)^{-5},\quad
v_k=S(u_k)^{-5}\quad(k>0).
\tag{T2}
\]

Middle是k<r，outer是k≥r，χ完全保留。设λ是一个**诊断代数参数**，并定义

\[
G_\lambda(T,V)=
\lambda\sum_{k<r}v_kT(u_k)V(u_k)
+\sum_{k\ge r}v_kT(u_k)V(u_k),
\quad \deg T,V<r.
\tag{T3}
\]

矩阵目标在deg T<r、deg Q<3r上定义为

\[
M_\lambda((T,Q),(V,Z))
=\sum_{k<r}v_k\{\lambda(TV+R^2QZ)+(6-\lambda)R(TZ+QV)\}
\]
\[
\hspace{20mm}+\sum_{k\ge r}v_k\{TV+R^2QZ+5R(TZ+QV)\}.
\tag{T4}
\]

**真正原目标固定λ=2：G_2就是冻结G0，M_2就是冻结M5。** 这里下标2表示诊断middle值，不改变旧稿0/5的命名或特殊值weight。λ不是可免费选择的真实period参数；没有为其他λ构造全球整数模型或数值目标。

在unfolded点上，middle κ=λ、cross numerator=6−λ，outer κ=1、cross5；λ2恰为原κ=1+χ、cross5−χ。因此真实half jet没有被改成toy或删掉。

## 2. 精确 plus/minus 化与 rank-r middle 更新

令f_+=T+RQ、f_-=T−RQ，g相同。逐点展开T4得

\[
\boxed{M_\lambda
=3\sum_{k=0}^av_k f_+(u_k)g_+(u_k)
+(\lambda-3)\sum_{k<r}v_k f_-(u_k)g_-(u_k)
-2\sum_{k\ge r}v_k f_-(u_k)g_-(u_k).}
\tag{T5}
\]

特别plus部分没有χ，但minus部分有完整middle/outer差；不能因plus简单就丢minus。原λ2的middle minus系数−1、outer−2，是actual half jet的准确代数结果。

令L为middle difference evaluation，列顺序T的r个monomials、Q的3r个monomials：

\[
L_{k,d}=u_k^d\ (d<r),\qquad
L_{k,r+d}=-R_ku_k^d\ (d<3r).
\tag{T6}
\]

其首r列是middle Vandermonde，故L满row rank r。D=diag(v_k)_{k<r}为unit matrix。若A为原同一profile上的M_3矩阵，则

\[
\boxed{M_\lambda=A+(\lambda-3)L^{\mathsf T}DL.}
\tag{T7}
\]

Slope矩阵rank恰r：L满射、L^T单射、D可逆。于是detMλ是degree≤r的多项式；**不自动是degree r或非零多项式**，因为顶层restriction仍可能退化。

## 3. 不除M3/G0的 bordered 目标判据

对任意t=λ−3，包括t=0，−I_r为已知unit块，给

\[
\boxed{\det M_\lambda=(-1)^r
\det\begin{pmatrix}A&tL^{\mathsf T}D\\L&-I_r\end{pmatrix}.}
\tag{T8}
\]

证明只用−I的Schur determinant；没有除A、原G0、原M5或任何intermediate moment。Actualλ2即t=−1。该5r阶bordered矩阵与原4r阶目标非零严格等价；它是一条合法目标identity，不是已证nonzero。

进一步设I⊂{0,…,r−1}，L_I取这些middle rows，则

\[
\det M_\lambda
=\sum_{k=0}^r t^k(-1)^k
\sum_{|I|=k}\det D_I
\det\begin{pmatrix}A&L_I^{\mathsf T}\\L_I&0_k\end{pmatrix}.
\tag{T9}
\]

这是multilinear determinant update：先在一般可逆A上用det(I+tDL A^-1L^T)和Cauchy–Binet，bordered determinant吸收A^-1；清分母后为所有A的polynomial identity。故A奇异也成立，不需要实际目标可逆来合法化T9。

顶层系数还有准确归属。取变量y=L(T,Q)、z=Q的3r个coefficients，则T由middle interpolation唯一恢复，basis-change determinant是(det V_mid)^−1。在该坐标下t只加到y块D。因此

\[
[t^r]\det M_\lambda
=(\det V_{\rm mid})^2\det D
\det(A|_{\ker L}).
\tag{T10}
\]

右边3r维restriction是明确的实际modified form，可能退化。它保留T=middle interpolation(RQ)、actual outer及middle plus项，不能改成自由QQ全迹或免费较低profile。

## 4. 原标量目标的 norm-free middle 特征多项式

令

\[
K(u)=\prod_{i=0}^{r-1}(u-u_i),\quad
X_{k,i}=\frac{K(u_k)}{(u_k-u_i)K'(u_i)}
\quad(k\ge r,\ 0\le i<r).
\tag{T11}
\]

全部分母是unit。X是middle Lagrange cardinal polynomials在真实outer点的evaluation，无未知Gram inverse。令D_out=diag(v_k)_{k≥r}及

\[
\mathcal K=D^{-1}X^{\mathsf T}D_{\rm out}X,\qquad
c_G=(\det V_{\rm mid})^2\det D\in F^\times .
\]

则原monomial basis中的准确identity为

\[
\boxed{\det G_\lambda=c_G\det(\lambda I_r+\mathcal K).}
\tag{T12}
\]

证明：middle values y=V_mid c，outer values=Xy；因此Gram=V_mid^T(λD+X^TD_outX)V_mid。只除已知middle diagonal weights，原Gλ可奇异。

故detGλ恰degree r、leading cG为显式unit；每个p最多r个坏λ。但这只是诊断族statement，**不能把λ2换成一个generic好值后声称原目标完成**。

还有一个可以继续攻固定2的scalar rational function：

\[
Z(z)=\sum_{k\ge r}\frac{v_kK(u_k)^2}{z-u_k}.
\tag{T13}
\]

Offdiagonal及diagonal统一为

\[
(X^{\mathsf T}D_{\rm out}X)_{ij}
=-\frac{Z[u_i,u_j]}{K'(u_i)K'(u_j)},
\tag{T14}
\]

其中Z[u_i,u_j]=(Z(u_i)−Z(u_j))/(u_i−u_j)，相同点取Z'(u_i)。负号由Z'=-ΣvK²/(z-u_k)²给出；所有evaluation poles都在outer，middle处安全。原G0非零现在准确等价于**−2不是这个明确weighted Loewner矩阵的eigenvalue**。自伴和controllability本身未证明此固定值排除。

## 5. 原Q源的全尺度 full-profile 单位

冻结共同E4的highest raising coefficient为

\[
\lambda_4(d)=-(2d-\tfrac{13}{9})(2d+\tfrac{82}{9}).
\]

**Theorem T15。对全部0≤d<N=5r+1，λ4(d)均非零。**

证明：第一factor等价18d−13；d0时−13绝对值<p，正值首次kp要求k≡5(mod18)，最早d=5r+1=N。第二factor18d+82要求k≡10(mod18)，最早d=10r−4≥5r+1=N，r1也是等号。均在full source cutoff外。这里不是generic polynomial nonzero，包含每个实际辅助p。

所以

\[
q_d=E_4^{\lfloor d/4\rfloor}u^{d\bmod4},
\quad0\le d<N
\tag{T16}
\]

是原全node polynomial空间degree<N的真实basis，det变换Δ4(N)=Π_{d<N}Π_{h<floor(d/4)}λ4(dmod4+4h)为显式unit。它恰是四seed的真实unequal chain lengths，不是uniform矩阵块。

在actualλ2上，QQ form为

\[
B_Q(Q,Z)=\sum_{k=0}^a \kappa_kv_kR_k^2Q(u_k)Z(u_k),
\quad\kappa_k=2\ (k<r),\ 1\ (k\ge r).
\]

全部weights=κ_fold S³为unit。因此四Q源Stieltjes block Hankel在T16的**full source N阶profile**上

\[
\boxed{\det H^{Q}_{\rm full}
=\Delta_4(N)^2
\prod_{0\le i<j\le a}(u_j-u_i)^2
\prod_{k=0}^a\kappa_kv_kR_k^2\in F^\times .}
\tag{T17}
\]

这是真actual source的normal profile，非derived endpoint functional。不能从它推出原3r QQ前profile或原(r,3r) M5 profile正常。

## 6. 实际四Q源的 visibility 与何处仍可能失败

E4自伴；把q_d按d排序，H_full由〈E4^j u^s,E4^k u^t〉=〈u^s,E4^(j+k)u^t〉得到，真行/列chain cutoff同T16。它是无限四源block Hankel的一个N阶unit minor。Node realization dimensionN又给rank≤N，故**实际QQ四源block Hankel rank恰N**，其finite rational realization不能少于N维。

这不要求θ_mid、θ_out互素，不要求simple spectrum；即使相同scalar poles有不同matrix residue方向，state degree仍由该Hankel rank说明。每个sector中四个RQ seed的endpoint connection polynomials与θ_sector共同gcd1：否则其F[z]/θ生成像位于一个真ideal，不能覆盖该sector，而full Q Krylov evaluation已覆盖全部node函数。这个gcd只排除共同隐藏模式，不排除临界Gram isotropy。

于是gate比“是否丢了某个spectral mode”精确：原未知是短的实际unequal-profile minor；full realization和一个actual full normal profile都已严证。

## 7. 所有dense connections的闭式，而非只报degree4r

对任一真实J_B块，m=r或4r+1，取local super a_j、sub b_j、prefix continuantsθ_j如冻结K18；B_j=b_1⋯b_j，B_0=1，全为units。直接TTRR归纳给

\[
\boxed{\theta_j(J_B)e_0=B_je_j\quad(0\le j<m).}
\tag{T18}
\]

证明：j1由J e0−d0e0=b1e1；归纳时a_{j-1}b_jθ_{j-1}恰消去向左项，剩下B_{j+1}e_{j+1}。没有Gram除法。

故任一实际node vector v的完整connection polynomial为

\[
\boxed{f_v(z)=\sum_{j=0}^{m-1}\frac{v_j}{B_j}\theta_j(z),
\qquad f_v(J_B)e_0=v.}
\tag{T19}
\]

它给出K26高degree连接的全部coefficients。Dense seed v_j=u_k^s或R_ku_k^s，最后node非零依旧迫degree4r；没有把高degree费用消掉。

基础endpoint functional取L_B(h)=v_start[h(J_B)]00。其orthogonal monicθ_j norm

\[
h_{B,j}=v_{{\rm start}+j}B_j^2
=v_{\rm start}\prod_{\ell=1}^ja_{\ell-1}b_\ell\in F^\times.
\tag{T20}
\]

这次用基础v而非actual middle2v，后者将在目标compound coefficients准确计入。

## 8. 真unequal四/八源的 compound Christoffel 目标公式

保留冻结source seed s=0,1,2,3及**d=s+4j<r/3r**的实际chain lengths。对每sector，用T19求T种子的f_Ts、Q种子的f_Qs；变换(T,Q)→(T,RQ)后，这些目标columns是

\[
z^jf_{T,s}\bmod\theta_B,\qquad
z^jf_{Q,s}\bmod\theta_B.
\tag{T21}
\]

每个remainder再在θ0,…,θ_{m−1}的unitriangular basis中展开。Scalar将middle/outer的coefficient rows合并为C_G；matrix将middle+/middle−/outer+/outer−的rows合并为C_M，Qcolumns在minus rows有负号。所有这些系数由已知unit products、polynomial division决定，无目标norm inverse。

令h_i按真实sector/local index取T20，则

\[
\boxed{\Delta_0(r)^2\det G_\lambda
=\sum_{|I|=r}\det(C_G)_I^2
\prod_{i\in I}h_i\,
\lambda^{\,\#(I\cap{\rm mid})}.}
\tag{T22}
\]

Matrix对全部4r个真实columns为

\[
\boxed{[\Delta_0(r)\Delta_4(3r)]^2\det M_\lambda
=\sum_{|I|=4r}\det(C_M)_I^2
\prod_{i\in I}h_i\,
3^{\#I_+}(-2)^{\#(I\cap{\rm out}-)}
(\lambda-3)^{\#(I\cap{\rm mid}-)}.}
\tag{T23}
\]

证明：T18–T20将基础endpoint form对角化，T5给四channel的准确scalar multipliers，然后用Cauchy–Binet。T22/T23保留原criticalΔ单位因子及true unequal profile；没有换成某个single-source consecutive Hankel。

Middle minus最多r rows，故T23又证明degree≤r。T22最高λ^r唯一选择所有r个middle rows，其unit leading coefficient与T12一致。λ2时所有diagonal multipliers也unit，但这些squares会在有限域相消；**不能据每个term单位报sum单位**。

## 9. 可以合法使用的有限support Christoffel公式

Primary Krattenthaler2021 Theorem1 as printed假设characteristic0及所有OP norms非零，不能直接照搬本有限域/有限support目标。本节另自证一个足够的有限模板。

取T20的L_B，p_j=θ_j对0≤j≤m，j>m取p_j=z^(j−m)θ_m。θ_m(J_B)=0，而j<m时T18及J^i e0的support给L_B(p_j z^i)=0(i<j)。故所有p_j monic且对degree<j orthogonal，**j≥m的norm允许为0**。

对n≤m，D_n=det(L_B(z^(i+j)))_{i,j<n}是已知endpoint unit；对h(z)=Π_{t=1}^d(z−x_t)：

\[
\boxed{\det(L_B(h(z)z^{i+j}))_{i,j<n}
=(-1)^{nd}D_n
\frac{\det(p_{n+i}(x_j))_{0\le i<d,\,1\le j\le d}}
{\prod_{i<j}(x_j-x_i)}.}
\tag{T24}
\]

证明以formal tensor L而非实正measure：V(z_1,…,z_n,x_1,…,x_d)=V(z)V(x)Π(x_j−z_i)。把大Vandermonde按monic p_j重写，expand x rows，再对z rows乘V(z)并施L_z1⋯L_zn。所有包含degree≥n的z-column因上述orthogonality消失；唯一低degree组给n! D_n，h那侧给n! det modified moments，符号来自Π(x_j−z_i)。n≤m<p，所以n!为unit。公式是polynomial identity，Vandermonde除法为整除；root重复时取Hasse confluent columns，不免费除p-divisible factorial。

该模板不假定modified target或其intermediate profiles正常。可给每个single seed链h=f_seed²的确切modified determinant；高degreef仍保留。**原四/八seed unequal profile需要T22/T23，不能把T24的single chain公式当whole target。** Matrix primary Theorem2还明确要求detΠ_{k,N}非零；那正是不能循环使用的门槛。

## 10. 同一结构中两个真正退化实例

下面是χ-preserving λ族的数学反例，**不是原固定λ2反例**。取旧已考察p19,r1，u=(0,1,4,9,16,6)。手算

\[
S(u_k)=(9,2,7,14,18,2),\quad
v=(3,3,7,2,18,3),\quad
R=(6,16,7,17,1,16).
\]

因此

\[
G_\lambda=3\lambda+14.
\tag{T25}
\]

λ8给G=0，而λ2给1。λ8既非0又非3，scalar/matrix ambient均非退化，common selfadjoint operators、leading单位、endpoint properness和actual full QQ visibility均保留。

在Tbasis1、Qbasis1,u,u²上，准确实际halfjet family矩阵是

\[
M_\lambda=
\begin{pmatrix}
3\lambda+14&\lambda+10&6&1\\
\lambda+10&13\lambda+5&2&1\\
6&2&1&2\\1&1&2&16
\end{pmatrix}\pmod{19}.
\tag{T26}
\]

右下2×2det=12为unit，其inverse为[[14,3],[3,8]]。合法Schur消去得到左上
[[3λ−2,λ],[λ,13λ+5]]，det=8λ+9，乘12恰

\[
\boxed{\det M_\lambda=\lambda+13.}
\tag{T27}
\]

λ6给M=0而G6=13unit；λ8给M8=2unit。λ6也非0/3，两ambient forms及上述全部结构非退化。故两种critical失败都能在同一个节点、χ、halfjet保持的族中发生。即使全QQ actual-source Hankel可控且一个full profile正常，也不能自动排除较短critical isotropy。

Actualλ2仍G=1、M=15；无以改变λ冒充原目标完成。T25–27为明确手算，不依赖finite probe；其目的严格定位需要新增的固定参数算术。

## 11. 本轮已推进到哪里，下一条实际定理要证明什么

已证直接actual-source的全N阶normal profile/minimal realization；已把原target写成显式connection compound公式，并将G0固定值问题精确变为T12的−2 eigenvalue排除，M5变为T8或T9在t=−1的bordered/compound非零。所有unknown intermediate profiles允许奇异，两个结构反例排除“selfadjoint+raising+endpointproper⇒target”的错误捷径。

下一实质门槛是从真实S、K、Z的Fermat/finite-field算术证明T14的特征值排除，或给T23在λ2的防相消身份；M还不能假定T10的3r维restriction为unit。若使用Christoffel/Jordan-chain theorem，必须直接证明其非零interpolation matrix，不能把该hypothesis换名字。

本轮没有证明无穷原critical simultaneous units、没有global Krylov整模型/arch费用改善、没有strict margin或特殊值新定理。Aux-local unit basis与诊断λ不免费给CDT arithmetic germs。真正目标仍是原ζ/L比较定理，未缩成derived endpoint结果。

## 12. NEW primary 原件与准确读域

正常verified TLS新增两份独立原件，无证书bypass：

- [Krattenthaler2021原件](https://arxiv.org/pdf/2101.04225v1)，24页，SHA6ee728bafe1ac1467050df139da6e86c9395f7fb7f7c77b769d0bb5388120fff。实际PDF1–5、7–17，共16distinct页。PDF2 Theorem1的char0/allnorm输入、PDF7–10 condensation、PDF13–14 confluence、PDF14–17 polynomial变换scope实际读。未称读PDF6、18–24；其印刷定理未直接升级有限域T24，后者自证。
- [Álvarez-Fernández等2015原件](https://arxiv.org/pdf/1511.04771v1)，34页，SHA082d479245929dc979f510fe5f082468de37d003623c6989c01def7c99759ded。实际PDF1–5、8–10、14–16，共11distinct页。PDF8–9定义nondegenerate为所有leading block非奇异、Gauss factorization输入，PDF15–16 Theorem2显式detΠ非零和逆实际读。未称读其余23页，不套real uniform-block OP normality到原有限域unequal profile。

总新archive58页，author实际27distinct页，URL/hash/执行史在独立NEWreceipt。未把摘要、peer阅读或页数元数据当实际全文阅读。

## 13. FIRST-ONLY结构验证与边界

NEW同stem verify.py保存后完整静态读，guard输出已存在即拒绝。恰首次1次运行，exit0 PASS3cases/692checks，r只选旧已考察1/2/4；未扩aux prime表。源码仅stdlib，不读取/import/执行旧或peer producer；输出保持first-only不改不重跑。

验证full QQ实际profile单位/Δ4(N)变换、λ-family整个F_p的target归一化及degree界、T12 middle公式、T8 border、endpoint connection、single-factor及重复factor有限Christoffel模板；p19反例按手算字段独核。原G2/M2仅比较identity，不assert为units；所有有限cases不替代正文allscale证明或无穷原target门槛。

本稿数学待root/toric实际全文独核，旧455数学pins不变。producer一次执行已完成，不允许重复。
