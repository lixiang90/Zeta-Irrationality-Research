# Level12 完整尖点校正窗口：真实周期、整模型与额外零反射条件

日期：2026-10-06。本文在冻结的 pure-\(L(3,\chi_{12})\) 源 \(F_L\)、零周期源 \(R\)、完整 \(\Gamma=\ker\chi_{12}\) 群及实际 \(v\)-坐标基础上，构造完整七维尖点形式空间及其反 Fricke 三维部分。它给出可用于下一步的实际整系数校正源和完整周期条件，没有构造出同一源的第三个独立零周期生成元，也不把未知关键周期关系当作已经成立。

只读既有 MD/PY/JSON，没有执行或 import 冻结、同行 producer；本文新固定证书另建。全部基、Fricke 分解与二段反射恒等式为固定空间/全尺度符号计算，不是参数或 word 搜索。

## 1. 十个尖点给完整、显式的尖点源基

沿用真实坐标
\[
v^2=\frac{h+6}{h+2},\qquad v(\infty)=1,\qquad
v(\gamma\tau)=\chi_{12}(\gamma)v(\tau),\qquad Wv=\frac{\sqrt3}{v}.
\]
\(\Gamma\) 无 torsion、genus0，函数域为 \(\mathbf C(v)\)。十个尖点恰为
\[
v=0,\infty,\ \pm1,\ \pm\sqrt3,\ \pm i,\ \pm i\sqrt3.
\]
令
\[
r=\sqrt3,\quad
P(v)=v(v^2-1)(v^2-3)(v^2+1)(v^2+3),\qquad
\boxed{C_k=\frac{(\theta_qv)^2v^k}{P(v)},\quad 0\le k\le6.}
\tag{1}
\]

这是完整实际 source，非仅形式上的有理函数。\(v\) 为 \(\Gamma\)-模函数，\(\theta_qv\) 为 weight2 模形式，故 \(C_k\) 为 weight4。在 \(H\) 中 \(P(v)\) 无零；\(v'\) 无零，因为 torsionfree 曲线到其 Hauptmodul 的 degree1 坐标没有内点分歧。故内点没有 pole。

在任何有限尖点，局部 \(v-v_c\sim q_c\)，导数经该 cusp scaling 后阶1；\((\theta v)^2/P(v)\) 阶1。因此每个 \(C_k\) 都是 cusp form。\(v=\infty\) 的尖点处，\(v\sim q_c^{-1}\)、导数阶−1，故 \(C_k\) 阶为 \(7-k\ge1\)。完整七个形式线性无关，因为公因子非零且 \(1,v,\ldots,v^6\) 线性无关。

另一方面，weight4 cusp form 对应 genus0 曲线上允许十个 cusp 各 simple pole 的 quadratic differential，即
\[
H^0(\mathbf P^1,K_{\mathbf P^1}^{\otimes2}+D_{\rm cusp})
\simeq H^0(\mathbf P^1,\mathcal O(6)),
\]
维数7。所以 (1) 是完整 \(S_4(\Gamma)\) 基，不是七个未证完备的样例。

## 2. 完整 Fricke 分解及三份整系数 anti sources

Diamond \(v\mapsto-v\) 给
\[
C_k|_4\gamma=(-1)^{k+1}C_k
\quad(\chi_{12}(\gamma)=-1).
\tag{2}
\]
故平凡字符 cusp space 是 \(C_1,C_3,C_5\) 三维；字符 \(\chi_{12}\) cusp space 是 \(C_0,C_2,C_4,C_6\) 四维。

准确 Fricke 因子来自
\[
(\theta v)|_2W=-\frac r{v^2}\theta v,\qquad
P(r/v)=\frac{9r}{v^{10}}P(v).
\]
所以
\[
\boxed{C_k|_4W=r^{\,k-3}C_{6-k}.}
\tag{3}
\]
平凡字符的 W-minus 部分恰一维，字符 \(\chi_{12}\) 的 W-minus 部分恰二维。整个 \(S_4(\Gamma)\) 的 W-minus 部分准确三维。

这三维有如下实际整系数基：
\[
\begin{aligned}
U&=f_6(\tau)-4f_6(2\tau),\\
f_6&=\eta_1^2\eta_2^2\eta_3^2\eta_6^2,\\
X_0&=16(C_6-3rC_0),\\
X_2&=16(C_4-rC_2).
\end{aligned}
\tag{4}
\]
准确规范为
\[
C_1-\frac13C_5=-\frac1{24}U.
\tag{5}
\]
两边都是已证明的 holomorphic weight4 \(\Gamma_0(12)\) cusp forms；固定 q 系数1至8一致，Sturm bound8给完整身份。新证书还额外核 q9至q11，但不是用额外样例代替 Sturm。
这里 eta form 的 level6 规范也可直接核：四个 exponent均为2，权为4，两项 Newman 和均24，\(\prod d^{r_d}=36^2\) 为平方；正 exponent给所有尖点严格正阶。eta 的 S 变换给 \(f_6|_4W_6=f_6\)，不依赖数据库代码执行。因此 oldform 公式给
\[
f_6|_4W_{12}=4f_6(2\tau),\quad
f_6(2\tau)|_4W_{12}=f_6/4,
\]
与 \(U|_4W_{12}=-U\) 相容。

这里的整性是全 n 证明。写 \(u=(v-1)/2\in q\mathbf Z[[q]]\)，真实整数反演已证。直接因式分解给
\[
16C_k=-\frac{(\theta u)^2}{u}\,
\frac{(1+2u)^{k-1}}
{(1+u)(1-2u-2u^2)(1+2u+2u^2)(1+u+u^2)}.
\tag{6}
\]
全部 denominator 在 \(u=0\) 为1，\(k=0\) 的 \((1+2u)^{-1}\) 也为整系数 unit；\((\theta u)^2/u\in q\mathbf Z[[q]]\)。因此
\[
16C_k\in q\mathbf Z[[q]],\qquad
U\in q\mathbf Z[[q]],\quad X_0,X_2\in q\mathcal O_K[[q]].
\]
\(X_0\) 与 \(X_2\) 的首项分别为 \((3r-1)q,(r-1)q\)。\(\sigma C_k=C_k\)，所以 \(\sigma X_j\) 在 W-plus 部分，而不是 \(\sigma X_j=-X_j\)。不得对未知关键 L 值使用该系数共轭替代真实积分。

## 3. oldspace 的实际周期限制，与 newspace 的区别

\(\chi_{12}\) 本原、导子为12。任何 lower-level oldform 的 Nebentypus 导子须整除其原 level，因此 level12 的四维 \(S_4(12,\chi_{12})\) 全部是 newspace；这里没有同一 lower-level primitive form 的两个 oldscales，可免费共享并取消同一 \(L(3)\) carrier。

平凡字符 oldspace 则由 \(f_6,f_6(2\tau)\) 生成，唯一 W-minus 方向为 \(U\)，其真实周期
\[
\boxed{\Omega_U=L(U,3)=\tfrac12L(f_6,3)>0.}
\tag{7}
\]
严格正性可由 \(f_6(iy)>0\) 的 eta product Mellin integral直接证明。因而 \(U\) 单独不是零真实周期 corrector。平凡字符 level12 的剩余 new cusp 方向是 W-plus，由 (3) 的完整三维分解也可看出，不能加入本 W-minus scalar source ansatz。

本轮实际读取 [LMFDB 6.4.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/6/4/a/a/)、[12.4.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/12/4/a/) 与 [12.4.b.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/12/4/b/a/) 的原数据页作独立交叉核对。它们分别记载上述 eta form、平凡字符 cusp 总维3/old2/new1与 W-minus1，以及字符 \(\chi(5)=\chi(7)=-1\) 的四维单一 newform orbit，系数域 \(\mathbf Q(\sqrt3,\sqrt{-5})\) 并有四个 inner twists。本文的完整 basis、整性和 W 分解不依赖数据库猜测。inner twists 不自动证明本文关键周期的 K 比值，也不能直接被记作可用 zero-period corrector。

## 4. 两个 new anti carriers 的严格非零与比例界

令
\[
\Omega_0=L(X_0,3),\qquad \Omega_2=L(X_2,3).
\]
以下是严格解析界，非浮点实验。

取 \(\tau=iy\)、\(y_0=1/\sqrt{12}\)。真实 eta 坐标 \(h(iy)>0\)；其 derivative 在 H 不为0，且从 \(h(iy)\sim e^{2\pi y}\) 得沿正虚轴随 y 严格增加。\(h(iy_0)=2r\)。所以 \(y>y_0\) 时
\[
1<v(iy)^2<r,\qquad \theta_qv=-\frac1{2\pi}\frac{dv}{dy}>0.
\tag{8}
\]
这里明确保留 q/τ orientation：v 随 y 减少，因此 \(\theta_qv\) 为正。

在此区间 \(P(v)<0\)，故
\[
X_0=16C_0(v^6-3r)>0,\qquad
X_2=16C_2(v^2-r)>0.
\]
对任一 W-minus cusp form \(X\)，det-normalized Fricke 给
\(X(iy)=-X(i/(12y))/(144y^4)\)。Mellin变换、把 \(0<y<y_0\) 换元到 \(y>y_0\)，得
\[
L(X,3)=\frac{(2\pi)^3}{2}
\int_{y_0}^{\infty}X(iy)(y^2-1/12)\,dy .
\tag{9}
\]
(9) 对 \(X_0,X_2\) 有处处严格正权，故 \(\Omega_0,\Omega_2>0\)。

实际 source 比为
\[
\frac{X_0}{X_2}
=\frac{v^6-3r}{v^2(v^2-r)}
=v^2+r+\frac3{v^2}.
\]
令 \(x=v^2\in(1,r)\)，\(x+r+3/x\) 随 x 严格下降，其端点为 \(4+r\) 和 \(3r\)。对 (9) 的严格正权取 weighted mean，得到
\[
\boxed{3\sqrt3<\frac{\Omega_0}{\Omega_2}<4+\sqrt3.}
\tag{10}
\]
因此单独的 \(X_0,X_2\) 都不是 zero-period corrector，也不存在 \(X_0-kX_2\)（k整数）这种校正。但 K 在实数中稠密，(10) 没有证明两周期在 K 上线性无关；更未排 \(\Omega_U,\Omega_0,\Omega_2\) 的 K 关系。

## 5. 实际 pure-L 校正和第三零反射的完整条件

完整 W-minus modular source空间有 Eisenstein5加 cusp3，共8维。Eisenstein部分在 infinity regular、分别删其显式 \(\zeta(3)\) 与 critical \(\pi^3\) carrier 的组件条件下，剩余恰为 \(F_L,R\) 两方向。因此这个组件条件下的完整 source 窗口准确为
\[
F=F_L+sR+tU+uX_0+wX_2,\qquad s,t,u,w\in K.
\tag{11}
\]
此句没有把“cusp period可能与ζ3/π3之间存在未知关系”的全部数学可能性排除。若取消组件条件，完整8维空间的实际 pure-L约束必须把那些未知关系也保留。

要使 (11) 第一支真实 period 仍准确为
\(\Theta=34560rL(3,\chi_{12})\)，必须且充分有
\[
\boxed{t\Omega_U+u\Omega_0+w\Omega_2=0.}
\tag{12}
\]
因为这些 source W-minus 且cuspidal，FE还给
\(L(C,2)=0,\ L(C,1)=-6L(C,3)/\pi^2\)。所以 (12) 正确取消完整三项 W period，而不是仅以 central root number声称零周期。

三个 \(\Omega\) 全非零，复系数零 \(L(3)\) 核为二维；K系数核的维度可能为0、1或2，本文没有证明存在非零 K 向量。把复二维核直接视为可用于算术germ的两个 K 正确器是不合法的。

对任意 eligible \(\chi_{12}=-1\) reflection \(J=\gamma W\)，取冻结稿的
\[
Q_J=1+(12d\tau-12b)^2/12,\quad
c_L(J)=i\pi^3\ell_JQ_J,\quad c_R(J)=i\pi^3\mathcal R_JQ_J .
\]
定义实际 additive critical endpoint
\[
\Lambda_U(J)=f_U(b/d+i0),\quad
\Lambda_0(J)=f_{\sigma X_0}(b/d+i0),\quad
\Lambda_2(J)=f_{\sigma X_2}(b/d+i0).
\tag{13}
\]
它们来自 coefficientwise共轭的真实source，不是 \(\sigma\Omega_j\)。cusp form 的系数增长保证 \(\theta^{-3}\) 在 rational roots这里绝对收敛；亦可用cusp Mellin继续。J-anti源与 \(J^2\) central保证完整 polynomial在unsigned +1的一维 eigline。故同一第二embedding原点的实际zero条件准确为
\[
\boxed{
i\pi^3(\ell_J+\sigma(s)\mathcal R_J)
+\sigma(t)\Lambda_U(J)+\sigma(u)\Lambda_0(J)+\sigma(w)\Lambda_2(J)=0 .
}
\tag{14}
\]
第三个指定、独立 reflection \(J'\) 要求另加同样一条 (14)。这是复等式，不能只删 imaginary 部分。

若 (12)、(14) 均闭合，则 \(L(3,\chi_{12})\in\mathbf Q\) 的反证假设使
\(f_F-\Theta\) 与 \(\sigma f_F+\Theta\) 真正为 K-conjugate arithmetic germs，且两个第二embedding反射由完整 signed eigline zero，而不是 endpoint单点guess。源 q整性只需固定清 \(s,t,u,w\) 的代数分母，primitive指数仍是3。real q结构自动保留 mirror。本文没有以未计算的 \(\Lambda_j\) 宣布实际第三零生成元或更大leaf。

这是具体的下一步接口：完整三份 cusp basis已给出、critical-period条件和两额外反射的真线性方程已写明；欠缺的是可证明的 K 周期关系及对应 additive endpoint，不是缺少q系数或自由维数。

## 6. 原两源窗口的一个真正全尺度补充

这里给一个有限字长但全整数参数的完整身份，不能扩大为 full kernel 分类。

令 \(g_{n,m}=\eta^nT^m\)、\(K_{n,m}=g_{n,m}Mg_{n,m}^{-1}\)。R在 \(\eta,T\) 上完整zero，所以对所有整数n,m有 \(c_R(g_{n,m})=0\)。冻结的
\[
P_n=c_L(\eta^n)/(i\pi^3)
=(44160n,529920n^2,2119680n^3-46080n)
\]
给 \(c_L(g_{n,m})=i\pi^3 P_n|T^m\)。

signed reflection eigline将其 +1 projection 化为
\[
\mu(n,m)
=P_{n,0}+(m+2/7)P_{n,1}
+(m^2+4m/7+1/12)P_{n,2}.
\]
不是仅据endpoint猜period。完整cochain cancellation强制唯一
\[
\begin{aligned}
s(n,m)&=\frac7{1920}\mu(n,m)\\
&=s_n+12nm\left[14(46n^2-1)m+368n^2+161n-8\right].
\end{aligned}
\tag{15}
\]
对固定 n非零，同一 \(s_n\) kill \(K_{n,m}\) 若m非零则要求
\[
m=-\frac{368n^2+161n-8}{14(46n^2-1)} .
\]
对 \(n=\pm(k+1),k\ge0\)，分子和“分母减分子”均有严格正的多项式系数，故此根严格在 \((-1,0)\)，没有整数解。n=0只给原T-conjugates of M。因此这个二段 family没有在已有 \(s_n\) 源上构造出独立第三反射。

(15) 不排 \(n'\ne n\) 的所有跨族相等、不排更深 words、general reflections或完整 origin stabilizer；它仅证明精确指定 family 的全尺度限制。

## 7. 新证书、文献与审核状态

同名 NEW producer不执行或 import旧/同行producer。首次执行47项通过；第二次仅把两个dimension记账checks替换为实际 Fricke eigenspace rank checks，仍47项全部通过，执行历史如实保存于JSON。固定证书核完整 cusp polynomial与W因子、diamond、全部七个整数 q模型、基独立jet、eta anti Sturm规范、ratio身份、两段完整s与extra root的全整数不等式。有限checks不替代正文genus0/divisor/Mellin/正权证明。

本轮 primary网页事实另保存 literature/cdt_odd_level12_cusp_space_primary_20261006.json；没有把数据库代码下载执行，也没有将新form字段/inner twists当作未知criticalperiod的现成关系。

root实际完整只读本文§§1–7、同名NEW PY与JSON，独核genus0 quadratic differentials的O6完备性、Fricke因子、16C全n q整性、eta/Sturm规范、Mellin正权、(14)真实leading端点规范与§6二段全整数限制通过。root还实际读取三个LMFDB原页核数据，没有执行producer，也不把§6扩大为full stabilizer。

conjugate_projection实际只读本文§§1–5与NEW PY/JSON，独核完整七维quadratic differential基、W-minus三维、全n整式/eta Sturm8、Mellin正权与严格ratio、(14)完整periodline身份通过；特别核了\(dJ\tau-b=-1/[12(d\tau-b)]\)、\(Q_J|_{-2}J=Q_J\)、\(Q_J(b/d)=1\)与\(\sigma X_j\)的实际J-anti/character匹配。它未执行producer、未审§6二段族、未把interval推为K线性无关，也未认领新的数据库关键周期事实。

本MD、同名PY/JSON与上述primary事实记录据此冻结；后续所有新模型和周期关系另稿。当前尚无新的数值无理性结论。

