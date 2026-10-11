# D12 共轭额外真实symmetry的解析盘与严格半径界

日期：2026-10-06。新proof note；只处理预先固定的Gaug=〈T,M,M′〉，不扫描生成元或研究参数，不运行任何旧或peer producer。[真实M/M′周期](cdt_odd_level12_full_leaf_20261006.md)已经分别给λM=λM′=−Θ，所以Hσ保持这两个变换。本稿证明增加这个真实symmetry仍不足以达到当前固定log账本的容量门槛；不排其它source或进一步实际period symmetries。

## 1. 两个相离圆的准确标准化

用ζ=√588τ、w=√588=14√3、u=4√3，则

\[
 T:ζ\mapsto ζ+w,\qquad
 S_\pm:ζ\mapsto \pm u-\frac1{ζ\mp u}.
 \tag{A1}
\]

M对应S+、M′对应S−。两矩阵为

\[
 S_a=\begin{pmatrix}a&-a^2-1\\1&-a\end{pmatrix},
 \quad\det S_a=1,\ S_a^2=-I.
\]

它们的isometric circles是center±u、radius1。所有translated circles的centers是±u+nw；任何两不同centers距离至少

\[
 d=6\sqrt3>2.
 \tag{A2}
\]

同sign相差14n√3，n≠0；异sign相差(14n±8)√3，其最小绝对非zero integer factor为6。因此这些closed semicircles严格相离，且基础两个圆都在strip |Reζ|<w/2内部。

## 2. 不靠猜测signature：fundamental domain与填后盘

定义

\[
 \mathcal F=\{ζ\in H:|\Re ζ|<w/2,
          |ζ-u|>1,\ |ζ+u|>1\}.
 \tag{A3}
\]

每个S_a将circle外部送入内部。reduced word的相邻两inversions若中间translation为0，必须选择异sign；若中间translation不为0，同sign也允许。相应的translated circles总严格相离。由右到左应用word，最后inversion将F送入其circle，下一个inversion将这个相离circle再送入自己的circle；左端translation只平移最终circle。因此任何含inversion的reduced word都把F送入某个translated circle，与F的interior相离；纯nonzero translation则把F送入相离strip。这证明free-product normal form没有额外relation、interiors不重叠与group离散。

还需证明F覆盖。对任意ζ∈H先translate到strip；若位于其中一个circle内，施加相应S_a再translate回strip。假若这一步后仍位于另一translated circle，则其center与上一center相距≥d。因S_a inverse就是自身，上一点到center的距离≤1/(d−1)；因此该次inversion将height乘至少(d−1)²>1。连续未终止的inversions要求height始终≤1，但上述uniform增长不能无限发生。算法有限终止，故F确是完整fundamental domain；seams按T、S±准确glue。

这给Gaug≅Z*C2*C2。domain只有∞一个ideal/parabolic vertex，两个圆tip为order2 elliptic points。其real boundary共有三个interval。两圆各将自己的左、右endpoint识别，T将strip左右endpoint识别；三个interval的endpoint graph恰是一个cycle，所以有且仅有一个funnel boundary circle。两个圆分别coarse化、∞cusp填充后，underlying surface的fundamental group由T,S+,S−分别kill，故simply connected；有这个single analytic boundary的填充surface是Riemann diskXaug。

这段论证没有从自由积的Euler characteristic独自推signature：实际fundamental domain、唯一cusp和boundary cycle都已验证。还可明确核该唯一boundary的side holonomy（up to inversion/cyclic conjugacy）：它是T_w^-1 S+S−，trace142。直接在原τ坐标中

\[
 T^{-1}\frac{MM'}{12}
 =\begin{pmatrix}239&69\\-336&-97\end{pmatrix},
 \quad\det=1,\quad\operatorname{tr}=142>2.
 \tag{A3a}
\]

所以该boundary是hyperbolic funnel，不是第二parabolic cusp。若使用orbifold记号，其signature为genus0、one cusp、one funnel、two order2；χorb=−1，与free product一致。

## 3. 目标函数、导数和原点在该盘上合法

Hσ和t−（这里指fullleaf稿的δ=−，即paired-coordinate稿的t+）真实保持T、M、M′。M′周期来自real coefficients反射canonical endpoint−2/7，已证明为−Θ；不是额外假定Galois period。

两个elliptic orbits分别有真实even Cayley germ，所以目标函数在两个coarse points都regular。其余Γ-involution fibers若没有Gaug stabilizer，继续作为ordinary points保留t的ram2，不错误删除其period。唯一cusp由q Taylor填充；t=q+O(q²)在那里有simple zero。全部interior无t-zero/pole，全部nonzero cuspimages保持遗漏。因此Xaug给另一张真实合法conjugate map，而不是未经认证的compact Γ/M下降。

同一个g=(1−4(2−√3)t+4t²)²仍在全部ordinary critical点清native θ/θ² poles；两个coarse elliptic处已无pole。相应1,gHσ,gθHσ,gθ²Hσ在整个Xaug全纯。q=e^(2πiζ/w)就是原q，不涉及phase shift。

## 4. 全尺度double words与正级数界

每个非identity double coset G∞\Gaug/G∞的唯一word可写

\[
 g=S_{a_0}T_w^{n_1}S_{a_1}\cdots T_w^{n_k}S_{a_k},
 \quad a_j\in\{u,-u\},
 \quad n_j=0\Longrightarrow a_j\ne a_{j-1}.
 \tag{A4}
\]

空transition k0有两个choicesS±。用Sa=T_a S T_-a展开，inner word是S T^{b1}S⋯T^{bk}S，其中

\[
 b_j=n_jw+a_j-a_{j-1},\qquad |b_j|\ge d.
\]

外侧translations不改变lower-left c。其continuant满足c−1=0、c0=1、c1=b1、cj=bj c(j−1)−c(j−2)，且lower-right ratio为

\[
 d_g/c_g=-a_k-c_{k-1}/c_k.
 \tag{A5}
\]

对Λ=(d+√(d²−4))/2，前一Hecke稿相同ratio归纳给|c(k−1)/ck|≤Λ^-1。令θ=1−1/(dΛ)=Λ/d，则

\[
 |c_k|\ge θ^k\prod_j|b_j|.
 \tag{A6}
\]

它不要求center choices交替，也处理所有signed translations。

transition平方倒数的2×2矩阵有diagonal和offdiagonal

\[
 A=\sum_{n\ne0}(nw)^{-2}=\frac{π²}{3w²},
 \quad
 B=\sum_{n\in Z}(nw+2u)^{-2}
   =\frac{π²}{w²\sin²(4π/7)}.
 \tag{A7}
\]

两offdiagonals相同。每行sum=A+B，所以逐wordlength对(A6)求和，精确species计数给

\[
 \mathcal C_{\rm aug}=\sum_{G∞\backslash G/G∞,c\ne0}c^{-2}
   \le\frac2{1-β},\quad β=θ^{-2}(A+B).
 \tag{A8}
\]

因为3π/7∈(π/3,π/2)，sin²(4π/7)=sin²(3π/7)>3/4，所以B<4A。Λ²+Λ^-2=d²−2=106、Λ>1给Λ²>105；于是

\[
 θ^{-2}<36/35,\quad
 \boxed{β<\frac{π²}{343}<1.}
 \tag{A9}
\]

这是真正全word majorant，没有将同一个row的多个baseline或两canonical ellipse误计成重复长度。

## 5. Green归一仍成立，且真实容量依然太小

定义Eaug=ΣG∞\G Im(gζ)。按double cosets及rightT求和，仍是

\[
 E_{\rm aug}=y+\sum_g c_g^{-2}P_w(x+d_g/c_g,y).
\]

(A8)给compact正常收敛；它是正harmonic、group invariant，在两个coarse ellipse均regular。由(A5)，每个pole orbit位于translated centers±u附近Λ^-1的bands。fundamental real intervals全在unit circles之外，与这些bands统一分离至少1−Λ^-1；故periodic Poisson kernel→0 uniformly且funnelboundary为0。cusp constant仍为(π/w)Caug。前一稿的Green唯一性证明因此逐项适用，给

\[
 \log R_{\rm aug}=\frac{2π²}{w²}\mathcal C_{\rm aug}
 <\boxed{\frac{π²}{147(1-π²/343)}}.
 \tag{A10}
\]

这里只是upper，不是actualradius的等式。它的量级约0.069；positive空words也给lower≥π²/147。

取P0=484/49>π²。结合原支已经证明的有理upper U+=290884/123333，准确Fraction比较给

\[
 \boxed{\frac{\log R_++\log R_{\rm aug}}2
 <\frac12\left[\frac{290884}{123333}
 +\frac{P_0}{147(1-P_0/343)}\right]<\frac54.}
 \tag{A11}
\]

因此这个已知额外真实symmetry也不能使当前固定k2/k3原log数组达到其lower-cost Jensen门槛29/13和539/253。所有映入Xaug的盘map由Schwarz lemma受同一radius控制；新增背景限制地图不会提升它。没有给这些数组任何待证Smith信用，也没有排其它source、其它完整period group或更精细算术包。

## 6. NEW固定证书与边界

同名NEW producer仅核固定M/M′标准化、两circle位置和integer-center差、symbolic lower-row、(A9)/(A11)有理比较；不运行旧或peerproducer，不扫描参数。作者首次、单次执行，37项全通过；有理平均upper是2443691800/2013164559<5/4。normal-form、fundamental coverage、boundary cycle及Green唯一性由正文承担，不能从有限矩阵样本推全group结论。

本稿证明了预先指定aug surface合法且半径小。它不是D12全部可能解析叶的分类；进一步真实变换可能需要另一个fundamental polygon和新的Green级数。

实际限定只读审核：Root完整阅读修正纯translation case后的本MD§§1–6与NEW源码，通过fundamental coverage的连续height增长、最小circle距离、unique doublecoset、continuant与2×2全尺度majorant、Green边界与q-radius归一、当前预算scope；没有运行37项producer。conjugate_projection实际只读§§1–3，核完整F覆盖、单boundary cycle、T/M/M′真实下降及ram2/gauge保留；没有运行producer，没有将scope扩展为全部真实stabilizer分类。唯一boundary的trace142按Root要求补入(A3a)，是展示的固定det1矩阵的直接恒等式，不改37项脚本或冒称已重跑。

本文三件在上述实际限定审阅状态冻结；以后再加symmetry或算术折扣另建稿。文献交付采用Root的合并uniformization manifest，不将同一MIT扫描PDF的重复hash算成两份独立文献；扫描讲义仍不是新Green证明的输入。
