# 对称周期完整塔在全部共同映射下的 CDT 门槛

2026-10-07。本稿将前轮 Θ=Θ₃ 的必要费用推广到全部 Θₛ，s≥2，并将解析限制从某个 slit 或 injective arctan lift 推广到任意 CDT 共同 holomorphic map。结果是这个特定完整函数塔的 rank comparison 无法推出无理性；它迫后续研究改变真实载体或引入其它有效输入，而不是只增加同一塔的阶数、更换有理基或扩大单叶。这个限制不涉及所有 Θₛ 无理性证明方法，更不涉及 ζ/L 的全局不可能性。

## 1. 固定实际对象和单关系

定义 R=log(1+x²)−log(1+x)，θ=x∂ₓ，令从0正规化的 Dⱼ满足

\[
D_1'=-R/(1-x^2),\qquad D_j'=D_{j-1}/x\ (j\ge2),
\quad D_j(0)=0.
\tag{W1}
\]

这是 [对合投影稿](cdt_theta_involution_period_projection_20261007.md) I1的同一函数族；Θⱼ=Dⱼ(1)>0，Θ₁=ζ(2)/8，Θ₃是原 A−B/2。所有 Dⱼ的 canonical germs 在1完整全纯。令

\[
F_{s,u}'=(D_s-u)/(1-x),\quad F_{s,u}(0)=0,
\quad \mathscr V_{s,u}=\langle1,R,D_1,\ldots,D_s,F_{s,u}\rangle_{\mathbb C(x)}.
\tag{W2}
\]

u∈Q 保证 Q-Taylor；仅 Θₛ=u 给 F 的原枝完整填1。以下 rank对任何complex u成立，算术固定rational u，共同map的条件则在目标relation下判断，不把三个条件相互代替。

## 2. 全阶精确函数秩

绕 i 运输 R，增量 c=2πi；随后绕1并逆向撤回i的路径（均不绕0）。D₁' 在该 transported branch 的1处有 residue c/2，故这个 conjugate loop γ准确给

\[
\Delta_\gamma R=0,\qquad
\Delta_\gamma D_j=\frac{k}{(j-1)!}(\log x)^{j-1},\quad k=\pi ic\ne0.
\tag{W3}
\]

每次 Euler 积分的常数由 jump 在1消失决定（j≥2）。对一个 rational-function relation作用γ，log x 的最高次项逐级强迫全部 Dⱼ系数为0；再绕i迫R系数0，故前s+2项独立。log x 的超越性由绕0反复平移2πi证明。

若u≠Θₛ，直接绕1仅平移F，故F独立。若u=Θₛ且s≥2，沿γ后绕0一次，Dₛ在1的值变成 Θₛ+k(2πi)ˢ⁻¹/(s−1)!≠Θₛ。这些transported Dⱼ在1仍全纯；再绕1仅给F非零constant translation，撤回前述路径后constant保留。于是

\[
\boxed{\dim_{\mathbb C(x)}\mathscr V_{s,u}=m=s+3\quad(s\ge2).}
\tag{W4}
\]

闭合rational ODE由W1–W2显式给出，所有成员holonomic；relation下Q(x)秩也为m。W4没有借数值周期独立性。

## 3. 全有限处有效输入

写 cₙ=(−1)ⁿ−2cos(nπ/2)∈{−1,3}，

\[
R_n=c_n/n,\quad S_n=-\sum_{1\le l<n,\ n-l\text{ odd}}c_l/l,
\quad (D_j)_n=S_n/n^j,
\]
\[
(F_{s,u})_N=(\sum_{n<N}(D_s)_n-u)/N.
\tag{W5}
\]

令 ℓ_N=lcm(1,…,N)，d固定使du∈Z。对所有N、全部finite primes与prime powers，N R_N∈Z、Nʲℓ_N(Dⱼ)_N∈Z、dNℓ_Nˢ⁺¹(Fₛ,u)_N∈Z。吸收N幂给一个有效e0阶梯 σ=(0,1,2,…,s+1,s+2)。这些粗cap只证明实际输入存在；下面必要费用允许任意更佳fixed type和任意 full Q(x)基，不以粗cap作为最优费。

## 4. 2p附近的全prime必要深层

固定一个正规row

\[
Y=a_0+a_RR+\sum_{j=1}^s a_jD_j+a_FF_{s,u},\qquad a_\bullet\in\mathbb Q(x).
\tag{W6}
\]

各a可有0处有限Laurent pole，完整infinite tails在除有限primes外p-integral。对充分大oddprime p，2p内和唯一p-divisible项为l=p，cₚ=−1，故

\[
p^{s+1}(D_s)_{2p}\equiv2^{-s}\pmod p.
\tag{W7}
\]

较低Dⱼ最深为−j−1>−s−1。固定k>0时 Dₛ,2p+k最深仅−1，F₂p+k在最低层只来自Dₛ,2p/(2p+k)，故其pˢ⁺¹倍为2⁻ˢ/k modp。令Cₚ=pˢ⁺¹F₂p，Cₚ为p-integral（所有n<2p输入最深来自n=p的−s，再付outerp）。对固定t≠0，完整convolution给

\[
p^{s+1}Y_{2p+t}\equiv
2^{-s}[x^t](a_s+a_FL)+C_p[x^t]a_F\pmod p,
\quad L=-\log(1-x).
\tag{W8}
\]

aF≠0时，aₛ+aFL在非zero-offset coefficient space中不可能是aF的constant倍；否则L成为rational。可取有限nonzero offsets上的固定rational functional，annihilate aF但不annihilate aₛ+aFL；若aF在该space为0，后者自身非零。除有限primes后，这迫每个p有某个所选t使vₚY₂p+t=−s−1。p∤2p+t，fixed Nᵉ不支付此层。

对任何合法fixed type NᵉΠℓ_floor(bN+c)，每个factor在此至多付一层p，b<1/2不能付p。因此

\[
\boxed{a_F\ne0\Longrightarrow\text{至少s+1个LCM columns有width}\ b\ge1/2.}
\tag{W9}
\]

有限offset集合可随固定row选择，不要求某个单offset适用于全部primes。

## 5. p附近的必要width-one层

令 Oⱼ=Σₖ≥1,k odd xᵏ/kʲ，Bₛ'=Oₛ/(1−x)、Bₛ(0)=0。真实monodromy给

\[
1,O_1,\ldots,O_s\text{ 独立};\qquad
B_s\notin\langle1,O_1,\ldots,O_s,L\rangle_{\mathbb C(x)}.
\tag{W10}
\]

第一式由绕−1的jump πi(logx−iπ)ʲ⁻¹/(j−1)!及logx超越性证明。第二式用绕−1与绕1的commutator：两个loops在Oⱼ及L上commute，因为它们的increments是logx多项式或constant且都不绕0。绕−1的 Oₛ jump在1值为πi(−iπ)ˢ⁻¹/(s−1)!≠0，所以该branch Bₛ绕1产生非零constant。反向的绕1jump的primitive在−1 ordinary，故无相应increment。这只给Bₛ一个非零constant translation，迫其独立。该论证不假设Oₛ(1)有理。

对固定k>0，fresh Rₚ=−1/p给

\[
p(D_j)_{p+k}\equiv [x^k]O_j\pmod p.
\tag{W11}
\]

不能假设p(Dⱼ)ₚ p-integral；这些数准确保留为unknown constants Cⱼ,p。有限positive-offset窗口中，p-scaledY有完整分解

\[
\sum_{j<s}C_{j,p}a_j+C_{s,p}(a_s+a_FL_p)
+C_{F,p}a_F+Z_p,
\quad L_p=\sum_{k\ge1}\frac{x^k}{p+k},
\]
\[
Z_p\equiv Z=-a_R+\sum_j a_jO_j+a_FB_s\pmod p.
\tag{W12}
\]

这里Zₚ p-integral，未知constants可以非integral；只在固定窗口使用Lₚ。具体 Cⱼ,p=p(Dⱼ)ₚ，而 C_F,p=p(Fₛ,u)ₚ=Σₙ<p(Dₛ)ₙ−u∈Z_(p)。对k>0准确有

\[
p(F_{s,u})_{p+k}=
\frac{pC_{F,p}+C_{s,p}+\sum_{1\le r<k}p(D_s)_{p+r}}{p+k}.
\]

所以constants columns之外的pC_F,p a_FLₚ确实并入Zₚ，并在modp为0；这里没有将可能非integral的Cⱼ,p误并入residual。index<p的输入均p-integral，index=p的值只进入所列constants，index>p的固定窗口由W11闭合，因此finiteLaurent poles只扩大一个固定窗口，不产生新的constants。

aF≠0时，aₛ+aFL不在其余rational columns的constant span；又W10迫Z不在rational-functions加rational-multiple-of-L的span。选一个finite coefficient minor，将L改成L_y=Σxᵏ/(y+k)，该minor在y0非零；代y=p后除有限primes外为p-unit。Cramer elimination于是给p-integral窗口functional，精确annihilate全部unknown-constant columns并对Z取值1。由Zₚ≡Z，若所选全部Yₚ+t都p-integral，则p-scaledvector属pZ_(p)，与functional输出p-unit矛盾。aF0但某aⱼ非zero时，constants仅为rational columns，Z非rational由W10第一式直接得到，同理成立。

因此每个充分大oddprime在某个有限positive-offset集合中有vₚYₚ+t<0。fixed Nᵉ不付p，所有width b<1的LCM factors也不付p。得到

\[
\boxed{Y\notin\langle1,R\rangle\Longrightarrow\text{至少一个column }b\ge1.}
\tag{W13}
\]

W12的矩阵是在辅助符号y0取值，不是让primes作为realnumbers趋于0。没有使用Wieferich primes或Fermatquotient的density。

## 6. 任意full basis的必要费用

W9与W13合并：aF≠0的row须有s+1个width≥1/2，且至少一个width≥1，故σ≥(s+2)/2。V0=⟨1,R⟩维数2，任意fullm维basis至少s+1行在V0外，各σ≥1，至少一行含F。合法staircase使row sums非降，于是

\[
\sigma\ge(0,0,\underbrace{1,\ldots,1}_{s\ \text{rows}},(s+2)/2),
\]
\[
\boxed{\tau\ge\tau^{\flat}\ge
t_s:=\frac{4s^2+17s+10}{2(s+3)^2}.}
\tag{W14}
\]

允许所有full Q(x)gauges、固定Nᵉ与normalization；τsharp≥0不能削弱W14。s3准确复得97/72，s2为6/5。这是必要界，不是最小τ的等式。

## 7. 所有共同maps的普遍尺度上界

fullbasis共同meromorphic意味着其rational inverse gauge重建的R共同meromorphic。若φ命中±i，R(φ)有nonzero-orderlogarithm，不可能meromorphic；finite ramification仍留log。因此任意合法holomorphicφ: D→C，φ0=0，都omit±i，而不必落在任何旧slit。

曲率−4的twice-punctured-plane metric及Schwarz–Pick给

\[
|\varphi'(0)|\le R_*:=\frac4\pi\mathcal K(1/\sqrt2)^2,
\tag{W15}
\]

此处K的argument是modulus，不是parameter。Primary [ASVV 0805.1501v1 §1](https://arxiv.org/html/0805.1501v1#S1)明确ρ_D(0)=1、metric contraction及λ₀₁(−1)=π/(8K²)。Möbius z/(z−1)将1/2映到−1、derivative绝对值4，因此λ₀₁(1/2)=π/(2K²)；affine x↦(x+i)/(2i)将±i映到0/1、0映到1/2，derivative1/2，故λ_pair(0)=π/(4K²)，即W15。不能用曲率−1的1/λ而漏disk density的factor2。

一个纯rational证书足够严格比较，不需求Γ值。binomial积分给

\[
\mathcal K(1/\sqrt2)=\frac\pi2 S,
\quad S=\sum_{n\ge0}b_n^2 2^{-n},
\quad b_n=4^{-n}\binom{2n}{n}.
\]

bₙ递减，n≥3时≤5/16。所以S≤1188/1024+25/1024=1213/1024<19/16，得

\[
\boxed{R_*<\frac{3971}{896}
<\sum_{j=0}^5\frac{(3/2)^j}{j!}<e^{3/2},
\quad L=\log|\varphi'(0)|<3/2.}
\tag{W16}
\]

K标准值约1.854只作背景，不参与W16。W15包括所有noninjective maps和任意更深cover；没有使用g=arctanφ injective假设。

## 8. 全s、全部map的rank门槛比较

任意CDT map两次Jensen给J≥L。其实际rankm的反证需要m>J/(L−τ)且L−τ>0，即

\[
\tau<L-J/m\le\frac{m-1}{m}L.
\]

由W14，必需

\[
L>g(s):=\frac{4s^2+17s+10}{2(s+3)(s+2)}.
\tag{W17}
\]

g(2)=3/2，且

\[
g'(s)=\frac{3s^2+28s+52}{2(s+3)^2(s+2)^2}>0.
\]

W16与W17矛盾。因此

\[
\boxed{\text{对每个整数s≥2，此完整实际塔及任意full Q(x)basis，}
\text{均不能通过上述CDT fixed-type rank comparison给Θₛ反证。}}
\tag{W18}
\]

W18不是Θₛ有理、不是其实际行列式不收缩，也不是其它carrier的否证。加入不属于此塔的真实函数、采用不同周期carrier、利用额外有效关系或其它定理都不在其范围内；它只消除了在同一完整塔上单靠更深cover或提高weight的继续搜寻。

同一universal bound亦能加强 [原β空间稿](cdt_weight4_space_germ_bridge_20261007.md) S22：其完整{1,T₁,…,Tₛ,F}秩mβ=s+2，任意fullbasis必要τ≥s(2s+3)/(s+2)²。共同T₁=arctanφ的meromorphic条件迫φ omit±i；其derivative在这些点的residue非零，finite ramification仍不能消去。rank comparison必要

\[
L>f(s)=\frac{s(2s+3)}{(s+1)(s+2)}.
\tag{W19}
\]

f递增且f(5)=65/42>3/2；W16于是排除这一个完整βₛ carrier在 **所有s≥5、全部共同maps** 下的同类rank contradiction。s2、s3、s4不由此universal bound排除；不能将它外推为β4或G的所有map否证，更不能将方法的限制说成β值有理。

## 9. 与真实目标的关系及证据

I8仍给Θₛ=(1/2−2⁻ˢ⁻¹)η(s+1)−Hₛ(1)/2，因此s偶涉及奇ζ值，s奇涉及偶ζ值。W18同样作用这些具体新组合的此carrier；没有证明其数值关系、ζ/L统一无理性或线性无关性。

root实际全文读T1–T27、N1–N15、G1–G26及独立universal稿U1–U26；W1–W19全部s版本逐项重新纸面推导。ASVV网页本轮打开并实际核§1 curvature、disk、Schwarz–Pick、负realaxis公式及K定义，§2初部hypergeometricseries；其余§3–4不称全文阅读。W15–W16又与独立geometry agent的universal-bound稿互核。CDT实际接口来自本轮已打开§2.1与Remark2.5。root本人没有新PDF阅读、旧producer、PSLQ或Lean执行；独立geometry agent另有准确节选PDF阅读与归档，见universal稿第9节，不把其阅读计为root全文阅读。

1次全新inline Fraction证书：重建r0–6、n1–8全部J递推/I15/I16形式η系数与其cap；复核s2–9、oddprimes3–31的2p最低层与有限比较值；纯有理核Sbound=1213/1024、Rbound=3971/896、exp下界5711/1280及严格差267/8960。有限全weight样本不替代W3–W14的全s全prime纸证；W15来自已核primary度量而非浮点。

写后独立全文纸审：theta_analytic_geometry实际FULL读九节W1–W19，独立从全部s≥2重推rank、两prime窗口、W12精确矩阵消元、权重和、universal比较及W19 β corollary，数学PASS；其universal_normalization子审实际FULL读W1–W18并独立全s重推PASS，没有将该子审范围外推到W19。二者共同建议显写C_F,p的integrality及上面的完整pF_(p+k)式，已补入；属于证明展开而非结论修改。root随后全文回读最终九节。这些是纸面数学复核，未称Lean形式化验证。
