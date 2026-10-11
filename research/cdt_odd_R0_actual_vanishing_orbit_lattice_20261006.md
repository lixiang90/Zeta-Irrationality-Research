# R₀ 实际消失周期轨道整格、交叉矩阵与原点整数旗标

日期：2026-10-06。NEW 全尺度纸面证明，另有自有 NEW exact-matrix verifier。旧/同行数学 MD、PY、JSON、manifest 全部只读，未执行/import/rerun。实际读当前 main §§79–84，主稿 SHA
2e148742cc6e80381d5b46f434f3085954209887a934bcea19c3881ed285ccab；
delivery 只读元数据确认 earlier80+current265=345 冻结输入、93 proof/reviews、74 primary PDFs 共4399页、1124 local links。

本稿先构造真正 actual integral cycles 生成的子格，独立证明其 Gram/Smith 和所有整数单值作用；随后通过已实际核读 degree-one graph 输入补证 saturated sector 的 integral projector，得 exact index256。它不把 formal Levelt 模型当 actual geometric saturation，也不假设整个 \(H^3(X)\) rank four。没有新增奇ζ/L无理性定理。

## 1. 输入、orientation 和 actualδ所在扇区

固定 [Yukawa/scalar](cdt_odd_R0_Yukawa_scalar_interface_20261006.md) Y8–Y10 的 actual rational rank-four compact sector \(V_{\mathbf Q}\)，以及实际 normalized period form
\[
 \omega=\sqrt{x}\eta,\quad
 P=\theta^4-x(\theta+\tfrac12)^4,\quad a=2\pi i.
 \tag{O1}
\]
middle intersection convention为
\[
 \int_\gamma\alpha=Q(PD\gamma,\alpha),\quad
 \gamma\cdot\delta=Q(PD\gamma,PD\delta).
 \tag{O2}
\]
homology sector 与 cohomology sector用PD识别，均记 \(V\)。\(\delta\) 是唯一普通二次节点的 actual oriented vanishing \(S^3\)，\(\Gamma\) 是 actual compact oriented torus；它们的旧稿已证输入为
\[
 g=\int_\delta\omega=-\pi^2v(1-x),\quad
 \int_\Gamma\omega=a^3y_0/2,\quad
 \delta\cdot\Gamma=8.
 \tag{O3}
\]

这里 actualδ 完全在 \(V\)，不只是其 rational projection。理由是 \(V\) 稳定 actual \(M_1\)，Picard–Lefschetz
\[
 M_1\gamma=\gamma+(\gamma\cdot\delta)\delta
 \tag{O4}
\]
在 \(V\) 上非零（真实 half-four PF 的 conifold transvection非零）。可取 \(\gamma\in V\) 且 \(\gamma\cdot\delta\ne0\)；O4 的差在 \(V\)，故 \(\delta\in V\)。这亦是冻结Y27前的已证论证。本稿不假设δ已在 full integral lattice 中 primitive。

记实际 physical origin one-turn 为 \(M_0\)，signed transport
\[
 U=-M_0,\qquad N=\log U .
 \tag{O5}
\]
actual algebraic \(\eta\) 的 PF 为 \((\theta+1/2)^4-x(\theta+1)^4\)，origin exponents−1/2、infinity exponents1，因此 physical traces−4/+4；\(U\) 才是 single Jordan4 unipotent。真实 square-root-cover loop 是 \(M_0^2=U^2\)，不是 \(U\) 自己。这些 facts 已由 [real Betti](cdt_odd_R0_real_Betti_normalization_20261006.md) R20–R25 实际 cup/PL 证明。

## 2. 全部整数k的真实交叉数，不是四点插值

冻结 real Betti R30–R33 的 genuine Frobenius basis和actualconcomitant给
\[
 g=f_3+b_2f_2+b_1f_1+b_0f_0,\quad
 2b_1-b_2^2=a^2/3,\quad
 \kappa=-a^3/16.
 \tag{O6}
\]
由 \(U\) 的 genuine logshift \(L\mapsto L+a\)，对任意 \(k\in\mathbf Z\) 精确为
\[
 C(g,g_{U^k})=ka(2b_1-b_2^2)+(ka)^3/6.
 \tag{O7}
\]
actual solution/cycle dual sign 是 \(\gamma\cdot\delta=-C(h_\gamma,h_\delta)/\kappa\)。因此
\[
 \boxed{a_k:=\delta\cdot U^k\delta
   =\frac83k^3+\frac{16}3k
   =8\,\frac{k^3+2k}{3}\quad(k\in\mathbf Z).}
 \tag{O8}
\]
\(k^3+2k\equiv0\pmod3\)，所以它确为整数。特别 \(a_0=0,a_1=8,a_2=32,a_3=88\)，且 \(a_{-k}=-a_k\)。O7–O8来自所有branch的真实period/cup，不是从 \(a_1,a_2\) 猜 cubic polynomial，也不是只验证有限k。

定义 actual integral cycle lattice
\[
 e_j=U^j\delta\ (0\le j\le3),\qquad
 \boxed{\Lambda_\delta=\sum_{j=0}^3\mathbf Z e_j.}
 \tag{O9}
\]
负号补偿不破坏integrality：\(U^j\delta=(-1)^jM_0^j\delta\)。因此各 \(e_j\) 真正是 compact closed integral cycles，且全在 \(V\)。用单值保交叉，
\[
 e_i\cdot e_j=a_{j-i}.
 \tag{O10}
\]

## 3. Gram、Pfaffian、Smith 和显式整数基变换

按column-coordinate convention，Gram为
\[
 G=8\begin{pmatrix}
 0&1&4&11\\-1&0&1&4\\-4&-1&0&1\\-11&-4&-1&0
 \end{pmatrix}.
 \tag{O11}
\]
其Pfaffian
\[
 8\cdot8-32\cdot32+88\cdot8=-256,\qquad
 \boxed{\det G=65536=2^{16}.}
 \tag{O12}
\]
非零 determinant 证明四个 actual cycles独立，故它们的Qspan恰为整个rank-four \(V\)。

取actual integer basis
\[
 e_0,\ e_1,\ w_2=e_2+e_0-4e_1,\ 
 w_3=e_3+4e_0-11e_1.
 \tag{O13}
\]
基变换upper triangular、diagonal全部1。前两与后两正交，\(e_0\cdot e_1=8\)，\(w_2\cdot w_3=-32\)。因此
\[
 S^TGS=8J_2\oplus(-32J_2),\quad
 \boxed{\operatorname{SNF}(G)=\operatorname{diag}(8,8,32,32).}
 \tag{O14}
\]
这里的invariant factors是 **intersection homomorphism**
\(\Lambda_\delta\to\Lambda_\delta^\vee\) 的Smith因子；不是未经计算的包含 \(\Lambda_\delta\subset V_{\mathbf Z}\) 的Smith因子。
\[
 \Lambda_\delta^\vee/\Lambda_\delta
   \simeq(\mathbf Z/8)^2\oplus(\mathbf Z/32)^2 .
 \tag{O15}
\]

## 4. Actual M₀、M₁、real involution和全部整数单值

\((U-1)^4=0\)给实际basis中的
\[
 U=\begin{pmatrix}
 0&0&0&-1\\1&0&0&4\\0&1&0&-6\\0&0&1&4
 \end{pmatrix},\qquad M_0=-U,
 \tag{O16}
\]
\[
 \boxed{M_1=\begin{pmatrix}
 1&-8&-32&-88\\0&1&0&0\\0&0&1&0\\0&0&0&1
 \end{pmatrix}.}
 \tag{O17}
\]
O17每个column由actualPL \(e_j\mapsto e_j+(e_j\cdot e_0)e_0\)给出。二者integerdet1、inverseinteger，且preserveG，所以 \(\Lambda_\delta\) 在实际全fundamental monodromy generators下稳定。按standard looporder取 \(M_\infty=(M_0M_1)^{-1}\)，其charpoly为 \((z-1)^4\)，与physicalinfinity输入一致。换standardlooporder只给共轭，不改变指数和Gram。

real cycle involution \(B_H=c_*\)满足 \(B_H\delta=\delta\)、
\(B_HUB_H=U^{-1}\)。因此actualinteger矩阵为
\[
 B_H=\begin{pmatrix}
 1&4&10&20\\0&-6&-20&-45\\0&4&15&36\\0&-1&-4&-10
 \end{pmatrix},
 \tag{O18}
\]
且 \(B_H^2=1,\ B_H^TGB_H=-G\)。它是homologylinear involution；cohomology的\(c^*\)经PD对应 **\(-B_H\)**，不能混同前轮PDplus/minus。O18也直接证明各integercycletransport的conjugation，而非从某个period值猜real sign。

## 5. N³的primitiveintegerrow与真实double-cover费用

令 \(A=U-I\)。因为 \(A^4=0\)，
\[
 N=A-A^2/2+A^3/3,\quad N^2=A^2-A^3,\quad N^3=A^3.
 \tag{O19}
\]
虽然 \(N\) 本身目前只有 denominator6，\(N^2,N^3\)都是integeroperators。明确
\[
 6N=\begin{pmatrix}
 -11&-2&1&-2\\18&-3&-6&9\\-9&6&3&-18\\2&-1&2&11
 \end{pmatrix},
 \tag{O20}
\]
\[
 \boxed{N^3=v\ell,\quad
 v=(-1,3,-3,1)^T,\quad\ell=(1,1,1,1).}
 \tag{O21}
\]
\(v\) 与 \(\ell\)都primitiveinteger；image \(N^3\Lambda_\delta=\mathbf Zv\)，kernel \(\ell=0\) 是 saturatedrank3子格。不是只有zero/nonzeroflag，没有比较尺度。

令 \(h_z=\int_z\omega\)，\(z=\sum z_je_j\)。O6每个 \(U^jg\) 的\(f_3\) coefficient是1，所以
\[
 [(\log x)^3]h_z=\frac{\ell(z)}6y_0,\qquad
 C(y_0,h_z)=-\ell(z).
 \tag{O22}
\]
这是原点最高log³所用的actualintegercovector。π和Tate factors仍在actualperiod比较内；不能把任意conifoldanalyticbasis的coordinates免费当 \(\Lambda_\delta\) coordinates。

真实sqrt-coverdoubleloop \(M_0^2=U^2\)的logarithm是 \(2N\)，其cube为 \(8N^3\)。也有
\[
 (M_0^2-I)^3=8v\ell .
 \tag{O23}
\]
因此cover不会使primitive originrow消失，也不能把factor8免费忽略。

## 6. ΓV的真实rational表达和实际integral remaining cycle

由 highest-log和 O3，
\[
 \int_{N^3\delta}\omega=a^3y_0
     =2\int_{\Gamma_V}\omega,\qquad\Gamma_V=\Pi_H\Gamma.
 \tag{O24}
\]
actualperiod map从\(V\)到solution space单射：若cycle的period identicallyzero，其与所有\(\theta^j\omega\)配对为零，而这些forms生成nondegenerateV。故
\[
 \boxed{2\Gamma_V=v
 =-e_0+3e_1-3e_2+e_3,\quad
 \Gamma_V=v/2,\quad
 \Gamma_V\cdot z=-8\ell(z).}
 \tag{O25}
\]
这不等于声明 wholecompact \(\Gamma=\Gamma_V\)。其sector表达有exact denominator2 relative to \(\Lambda_\delta\)，因为v primitive。

之前real remainingactualcycle
\(\gamma_L=(U-U^{-1})\delta-2\Gamma\) 的projection nowexact为
\[
 \boxed{(\gamma_L)_V=-3e_0+4e_1-e_2=:\alpha.}
 \tag{O26}
\]
右边本身是 **actual integral cycle**，无需假设 \(\Pi\) integral也成立。其 \(B_H\alpha=-\alpha\)，\(\delta\cdot\alpha=0\)，且其normalizedperiod就是前轮正端点成本 \(p_L\)。\(\alpha\) primitive in \(\Lambda_\delta\)，但在complete saturatedsector是否primitive须另算。其divisibility在本格为16，因为
\[
 G\alpha=(0,16,64,144)^T.
 \tag{O27}
\]
ordinarycoefficientprimitive与cupdivisibility须分开。

## 7. 不用degree-one图升级时已有的有限index界

令 \(H=H_3(X,\mathbf Z)/{\rm tors}\)，
\(L=H\cap V_{\mathbf Q}\)。它是实际 saturation，不是formallevelt格。由O12，\(m=[L:\Lambda_\delta]\)有限且
\[
 \det G=m^2\det Q_L,\qquad
 \boxed{m\mid256.}
 \tag{O28}
\]
因为integeralternatingmatrix的det是integerPfaffian的平方。故 \(m\)只有2-primary因子；全oddprimes已无index。对任意 actualh，\(\Pi_Hh\)与全部 \(\Lambda_\delta\)cycles交叉为整数，所以
\[
 \Lambda_\delta\subset L\subset\Pi_HH\subset
 \Lambda_\delta^\vee\subset\tfrac1{32}\Lambda_\delta.
 \tag{O29}
\]
这证明 \(32\Pi_HH\subset\Lambda_\delta\)，投影在每个oddprime处integral。只靠O28不能确定m，也不能把 \(\Gamma_V\in\Pi_HH\)免费放入L。下节提供真正几何补证。

## 8. Degree-one共同resolution实际补证 integralΠ和exact index256

本轮实际全文回读冻结Yukawa，尤其明确图
\[
 X\xleftarrow{a}Z\xrightarrow{b}\mathcal W
 \tag{O30}
\]
的两个 smoothproperbirational degree-one maps；degree64的finitecover \(M_\psi\to\mathcal W\)不出现在这里。冻结Y9通过实际holomorphicform及cyclicspan证明
\[
 i_{\mathbf Q}=a_*b^*,\quad q_{\mathbf Q}=b_*a^*,\quad
 q_{\mathbf Q}i_{\mathbf Q}=1,\quad\Pi=i_{\mathbf Q}q_{\mathbf Q}.
 \tag{O31}
\]

NEW整数升级如下。对orientedcompact sixmanifolds，ordinarypullback及
PD-defined properpushforward都在 torsion-free integral middlecohomology上定义，degreeoneprojectionformula同样成立。故同一图有integer maps \(i_{\mathbf Z},q_{\mathbf Z}\)；O31的rationalidentity推出integeridentity \(q_{\mathbf Z}i_{\mathbf Z}=1\)，因为free abelian endomorphism tensorQ单射。这不要求先知道maps的integer矩阵。

push/pull在middlecup下互为adjoint，故
\[
 Q_X(iu,iv)=Q_{\mathcal W}(u,qiv)=Q_{\mathcal W}(u,v).
 \tag{O32}
\]
因此 \(i\)是integral isometric splitembedding，\(\Pi=iq\)是integerorthogonalprojector。finitecover上的actualimage就是已证V；uniqueorthogonalprojector的deckinvariance使它下降回原base，integrality是逐fibre事实。由此
\[
 \boxed{L=iH^3(\mathcal W,\mathbf Z)/{\rm tors}
 \text{ saturated、rank4、unimodular；}\quad \Pi\text{ integral}.}
 \tag{O33}
\]
这里 \(\mathcal W\) actualH³rank4是冻结BKcompactmirror输入。闭orientedmanifold的middlefreecupunimodular给 \(\det Q_L=1\)，所以
\[
 \boxed{[L:\Lambda_\delta]=256,\quad
 L/\Lambda_\delta\text{ 是O15中order256的isotropic subgroup}.}
 \tag{O34}
\]
这是真正geometry补证，强于formalLevelt saturation。同行亦正在独立从同一degree-one输入建立该整数升级，随后双方另稿互审。旧稿“尚未证明integralΠ”的历史范围保持只读，没有改写成旧稿已经证明。

包含 \(\Lambda_\delta\subset L\) 的具体Smith factors仍未唯一确定。现在已知其order256、exponent≤32、全部2-primary；Gram的8,8,32,32不等于这些包含因子。要给其actualfullmatrix/primitiveδ，仍需actual integralmirrorbasis或几何divisibility计算。

## 9. ΓV实际必须even、Γ/8费用及nativeintegerflag范围

O33使 \(\Gamma_V\in L\)。O25/O21给所有 \(z\in V\)
\[
 \boxed{N^3z=-\frac14(\Gamma_V\cdot z)\Gamma_V
 =\frac14(z\cdot\Gamma_V)\Gamma_V.}
 \tag{O35}
\]
令 \(\Gamma_V=d\gamma\)，\(\gamma\) primitive in unimodular L。O3使d正整数且 \(d\mid8\)。选 \(z\in L\)使 \(z\cdot\gamma=1\)；O35和 \(N^3=(U-I)^3\) integral给
\[
 (d^2/4)\gamma\in L\quad\Longrightarrow\quad d\text{ even}.
 \tag{O36}
\]
因此
\[
 \boxed{d_\Gamma\in\{2,4,8\},\quad
 \Gamma_V/2=v/4\in L,\quad
 \Gamma_V/8\in\tfrac14 L.}
 \tag{O37}
\]
canonical sector \(\Gamma/8\) marking的安全integercharge≤4，而不是默认必须8；它在orbitbasis中仍为v/16，exactdenominator16。二者使用不同actual lattices。未证明exact \(d_\Gamma=8\) 或primitiveMUMcycle。

nativeflag covector \(\ell\) 在L上的valuegroup由O25是
\[
 \boxed{\ell(L)=\tfrac{d_\Gamma}{8}\mathbf Z
 \in\{\tfrac14\mathbf Z,\tfrac12\mathbf Z,\mathbf Z\}.}
 \tag{O38}
\]
这说明在actualsaturatedgrid与orbitgrid的最高log比较只有有限2-primary uncertainty。O26的actualremainingcycle若写 \(\alpha=d_\alpha\alpha_{\rm prim}\)，O27给 \(d_\alpha\mid16\)，所以remainingrealnormalization的primitivecharge也有finitebound。没有将其中任意case默认实际case。

## 10. Endpoint-sensitive packet的接合与范围

本轮实际读取 [exterior packet](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md) E10–E11。其 \(p_+\) 是rank-five原点Kummer **spectral** projector，不是本稿realinvolution projector；其 \(N_0\) 在homogeneousperiods中对应O5的signedU。symplecticcontraction识别 \(\bigwedge^3V\) 后，实际origin最高log条件确可由本稿primitiveintegerrow \(\ell\)检测。

本稿没有把这个detection直接变成CDTcapacity。exterior/conifoldanalyticbasis到actualBetti格的comparison、rank-fiveextension的source格、\(p_+\) 在该extension格中的charge、wholeprefix有效badprimeC、以及真实fillableword仍需另证。同行本轮主攻实际extension与spectralcharge，不由本稿claim完成。

与上轮相比，新的integer输出是actualorbitΛ、全部integerM₀/M₁、Gram/Smith、actualsaturationindex256、integralΠ、Γeven的safecharge、primitiveoriginrow及doubleloopfactor8。chosen centered compact scalar等于 \(\nu_{\rm corr}\) 已由前轮另稿证明，不再列为本稿的比较缺口。没有新增 ζ(7)、Catalan 或类似特殊值的无理性、线性无关性或Lean。

## 11. 独立验证、来源和执行登记

纸面论证O7–O10、O30–O38是真正geometry/cup证明；exactmatrixcertificate不能验证几何hypotheses。
自有 [NEW verifier](cdt_odd_R0_actual_vanishing_orbit_lattice_20261006_verify.py)
与 [NEW certificate](cdt_odd_R0_actual_vanishing_orbit_lattice_20261006_verify.json)
仅核矩阵、symbolic整数k恒等式、SNF、basischange、flags及Γ/α坐标。它以自身和本稿hash固定来源；首次执行一次，未import旧/同行producer，未数值搜索。若有修订或失败，须在NEW记录明示，不能冒称单次成功。

本轮实际全文回读冻结real Betti和Yukawa/scalar两稿；main79–84完整读；exterior E10–E11实际读；delivery只读selectedmetadata、不执行audit。

* real Betti SHA dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f；
* Yukawa/scalar SHA 172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15；
* 新数学producer执行范围只限本稿自有 verifier，脚本不读/import旧数学程序；本轮旧/同行数学producer执行/import/rerun数0。

没有新增PDF，不冒认本轮又全文读取BK、Movasati或其他primary。其compactmirror/PL输入由此前实际独审冻结稿提供；本轮新增整数Gysin/PD argument完整写在O30–O36。
