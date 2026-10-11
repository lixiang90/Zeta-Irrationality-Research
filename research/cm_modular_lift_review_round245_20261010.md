# 第245轮：CM源的模函数提升与原坐标全图界

2026-10-10，A，独立纸面证明。固定244的F、S_g=G+gF、H_g及原坐标z；不改冻结秩稿。本稿证明：任何非恒定全纯图φ:(D,0)→(C,0)，若所选native F∘φ在整个D亚纯，则φ=Z∘q，其中q:D→D全纯、q(0)=0，故|φ′(0)|≤1。显式有理微分恢复式使S_g-only和H_g-only的同类亚纯图也满足此界。这里没有unique-origin、univalence或只有有限个前像的假设。此结论限制同坐标的基本正余量入口，不是所有新周期商、有限处图或更强CDT方法的排除。数学程序0。

## 1. 精确同源参数与F的恒等式

令w∈H、q=e^{πiw}，并取
\[
 \lambda(w)={\theta_2(0|w)^4\over\theta_3(0|w)^4},\qquad
 Z(q)={\lambda(w)(1-\lambda(w))\over16}.
 \tag{M1}
\]
这是q=e^{2πiτ}、w=2τ的原坐标，没有额外缩放。DLMF的theta产品和变换式给λ(w+2)=λ(w)、λ=16q+O(q²)，以及θ₃在H无零。故Z在整个q圆盘全纯，Z(0)=0、Z′(0)=1。

实际F(z)=₃F₂(1/2,1/2,1/2;1,1;64z)。[DLMF16.12.2](https://dlmf.nist.gov/16.12.E2)的Clausen式取a=b=1/4，给F(z)=f(64z)²，f(t)=₂F₁(1/4,1/4;1;t)。为支付quadratic而非借有限系数比较，令t=4λ(1−λ)、y(λ)=f(t)，直接链式计算得
\[
 \lambda(1-\lambda)y''+(1-2\lambda)y'-y/4
 =4\{t(1-t)f''+(1-3t/2)f'-f/16\}=0.
\]
y(0)=1且是全纯解，所以y=₂F₁(1/2,1/2;1;λ)。由椭圆积分的二项式积分展开和[DLMF20.9.1–2](https://dlmf.nist.gov/20.9)，它等于(2/π)K(√λ)=θ₃(0|w)²。因此从q=0的实际芽出发，解析延拓给
\[
 \widehat F(w):=F(Z(e^{\pi iw}))=\theta_3(0|w)^4.
 \tag{M2}
\]
theta₃无零用[DLMF20.5.3](https://dlmf.nist.gov/20.5.E3)在变量0的产品：每个因子(1−q^{2n})(1+q^{2n−1})²非零，且产品在|q|<1局部正规收敛。λ的比值规范用[DLMF23.15.6](https://dlmf.nist.gov/23.15.E6)。

## 2. 覆盖证据与讲义中必须修正的两处

实际FULL读Chiang作者讲义物理PDF208–219的完整第6章选段，尤其Thm6.3.1的证明和Thm6.3.2；不声称读完整224页。其(6.8)印出的域与随后三条边不一致，§6.3的T变换分母也有符号错，不能逐字套用。正确基本ideal triangle是
\[
 \Delta=\{0<\Re w<1,\ \Im w>0,\ |w-1/2|>1/2\},
 \quad \lambda(Sw)=1-\lambda(w),\quad
 \lambda(Tw)={\lambda(w)\over\lambda(w)-1},
 \tag{M3}
\]
S:w↦−1/w、T:w↦w+1。讲义§6.1已经给正确的两条变换；这里修补其后证明而非接纳误印域。

简述完整修补。写t=λ(iy)。theta实值、λ不取0或1及cusp渐近给0<t<1。DLMF20.9.2给y=K(√(1−t))/K(√t)；分子严格递减、分母严格递增，故t随y严格递减，从y=∞时0到y=0时1。Δ三边的像于是分别为
\[
 \lambda(iy)=t\in(0,1),\quad
 \lambda(1+iy)=t/(t-1)\in(-\infty,0),\quad
 \lambda(1-1/(1+iy))=1/t\in(1,\infty).
\]
第三条是上半圆|w−1/2|=1/2，绝非误印的圆。用λ=16e^{πiw}(1+o(1))在∞截角，并以S、TS在0、1截角：前两cusp的像分别绕0、1作消失小弧，cusp1的像作上半平面的大半圆。正向边界像对每个上半平面点绕数1、对每个下半平面点绕数0。λ在Δ无极点，argument principle给每个上半平面值恰一个原像且重数1。因此λ:Δ→H双全纯。沿三条实值边Schwarz反射，理想三角形的反射镶嵌覆盖H；其保向群由T²及w↦w/(2w+1)生成，正是Γ(2)（在PSL₂中）。这给λ:H→C\{0,1}的无分歧通用覆盖，fibres恰Γ(2)轨道。域和符号修正后，这是讲义原argument-principle/反射证明的实际结论。

所以Z=λ(1−λ)/16的fibres由
\[
 \Gamma_\theta=\langle\Gamma(2),S\rangle=\langle T^2,S\rangle
 \tag{M4}
\]
给出，唯一有限critical值是z_*=1/64，原像λ=1/2。生成式也可用even Euclid核：Γθ模2为I或S；其primitive第一列两整数奇偶相反，反复用T^{2k}把首项绝对值严格缩到次项之下，再用S交换，最终到c=0及±T^{2k}。删去所有elliptic原像后，Z:H\Z^{-1}(z_*)→C\{0,z_*}是regular covering，不能称这个删点域为普通universal cover；不删点时为(∞,2,∞) orbifold cover。

## 3. 函数芽稳定子，及局部分支核查

[DLMF20.7.28、29、32](https://dlmf.nist.gov/20.7)在theta变量0给
\[
 \widehat F(w+2)=\widehat F(w),\qquad
 \widehat F(-1/w)=-w^2\widehat F(w).
\]
按M4生成元合成，对γ=(a,b;c,d)∈Γθ有
\[
 \widehat F(\gamma w)=\epsilon_\gamma(cw+d)^2\widehat F(w),
 \qquad \epsilon_\gamma\in\{1,-1\}.
 \tag{M5}
\]
稳定的是完整函数芽。如果右边与\widehat F在某开集相等，由其无零性，εγ(cw+d)²≡1。于是c=0、d=±1，而模2条件使b为偶数；反过来±T^{2k}确实稳定。因此
\[
 \operatorname{Stab}_{\Gamma_\theta}(\widehat F\text{ germ})
 =\langle T^2\rangle \quad(\text{在PSL}_2).
 \tag{M6}
\]
不能用单个点的函数值相等代替M6。

局部检查与此一致。S变换求导在w=i给\widehat F′(i)=i\widehat F(i)。任何分支M5在i的导数为
\[
 \epsilon_\gamma(ci+d)(c+id)\widehat F(i)\ne0.
 \tag{M7}
\]
λ′(i)≠0且z−z_* =−(λ−1/2)²/16，故所有z_*分支都具有非零sqrt项；有限ramification使其亚纯必须为偶阶。native z=0的γ分支若c≠0，则M5含非零(log z)²首项，任何有限阶零点ramification都不能把它变成亚纯。c=0恰M6的native cusp叶。下一节不把这些局部检查当额外图假设，而统一证明提升。

## 4. 任意合法图的删点提升与Schwarz界

设φ:D→C全纯、φ(0)=0，且所选native F∘φ延成单值亚纯函数h于整个D。若φ恒为0，结论平凡。否则集合E=φ^{-1}({0,z_*})在D局部有限，Ω=D\E连通。由Z′(0)=1，在足够小的native邻域有逆芽q，q(0)=0，并在穿孔部分提升到H。沿Ω路径，上一节的regular covering使w可继续，故q=e^{πiw}也可继续。

任一闭路的w提升相差γ∈Γθ。h是全局亚纯函数，所以继续后返回同一个F函数芽；在选取的普通基点附近φ是非恒定开映射，芽相等强迫M6。于是γ是T^{2k}，q不变。故q成为Ω上的单值全纯函数，且0<|q|<1。

q有界，E的每一个点均为可去奇点，延成全D全纯函数。无论E有多少点，这都是局部可去性；没有把无穷前像替换为有限前像。延拓后|q|≤1，最大值原理和native q(0)=0排除盘内取单位模，所以q:D→D。φ=Z(q)在Ω成立，按全纯恒等式延至整个D。由M1及Schwarz lemma，
\[
 \boxed{\phi=Z\circ q,\quad q:D\to D,\quad q(0)=0,
 \quad |\phi'(0)|=|q'(0)|\le1.}
 \tag{M8}
\]
证明没有要求φ单叶、q单叶、φ^{-1}(0)唯一，亦未预设z_*前像的偶ramification。后者自动由M8的分歧结构得出。F-alone的界是sharp：φ=Z(u)给全盘全纯F拉回及φ′(0)=1；这不表示H或S也对该图全盘亚纯。

## 5. 显式恢复F：H-only和S-only也受同一个界

记θ=z∂_z、L=θ³−8z(2θ+1)³、J=8z(2θ+1)−θ/46，取W=JF、b=16z−1/46、D₀=1−64z。由LF=0直接微分得到
\[
 \begin{pmatrix}W\\\theta W\\\theta^2W\end{pmatrix}
 =P(z)\begin{pmatrix}F\\\theta F\\\theta^2F\end{pmatrix},
 \quad P=
 \begin{pmatrix}
 8z&b&0\\
 8z&24z&b\\
 8z+8zb/D_0&32z+48zb/D_0&40z+96zb/D_0
 \end{pmatrix}.
 \tag{M9}
\]
其行式逐项为W=8zF+bθF，θW=8zF+24zθF+bθ²F，以及θ²W=8zF+32zθF+40zθ²F+bθ³F后用LF=0消去θ³F。唯一一次z首阶行列式项为b(0)²·8z(1+b(0))，故
\[
 \det P={45\over23^3}z+O(z^2)\ne0.
 \tag{M10}
\]
P^{-1}第一行就是恢复F的明确Q(z)微分证书。244的精确恒等式给
\[
 W=LS_g=L[(1-4096z)\partial_z]H_g.
 \tag{M11}
\]
这不依赖g，不借七阶formal闭包或不可约性猜cyclic恢复。

若H_g∘φ（或S_g∘φ）是单值亚纯函数，沿φ拉回M9–M11：θ变为(φ/φ′)∂_u，任意有理系数变为r(φ)。φ非恒定时这些均亚纯；φ′的零点只产生允许的有限阶pole，而亚纯函数对微分封闭。初始芽恒等式于是恢复F∘φ为全D亚纯函数。M8随即适用。因此M8同样涵盖H-only、S-only及显式包含它们的完整源。系数证书在0出现pole也无问题，初始实际F芽的可去性已由恒等式给定。

## 6. 已付关闭范围与执行账

实际FULL复读244源6783 B / SHA256187cbbd9bda470a07691dc2c962dd5054144e6c65a6542491498bb9342456d9c，以及245秩稿7188 B / fd02e917049de96221007fe6a6edb62615a55b785785b201979cf14338d18cec。后者已付C7 actual rank7、加1 rank8；本稿M9–M11使提升界不需要再援引该秩证明。

原坐标全部合法全纯共同图的log|φ′(0)|≤0。故凡以log|φ′(0)|−τ>0为基本入口、算术成本τ≥0的同源证书，都不能在这里领取正余量；即使先放弃正算术费也没有严格正解析增益。此判断包括同坐标H_g-only和S_g-only的这个基本入口，不能再以删掉F背景逃过M9。目标g=g*的native CM补点不改变提升约束。

本稿不把此界扩为任意数域有限处图、其它目标period quotient、非线性新源、D-dependent整模型或所有更强CDT的no-go；也不证明数值X无理或全叶CM评价。没有把τ的安全upper当必要lower。它给当前基本分支的结构停止理由，取代继续246图参数试探。来源准确选读、讲义修补、保存身份见alternative_modular_lift_review_scope.md。数学程序、CAS、素数/参数扫描、Lean、git均0；保存后实际FULL作者复读全文。
