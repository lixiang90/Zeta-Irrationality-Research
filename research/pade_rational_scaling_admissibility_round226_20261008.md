# 第226轮：原三行与目标行的有理缩放准入

2026-10-08。固定第225轮原包，考察 \(z=x/N\)，其中 \(N\in\mathbf Z_{>0}\)。本稿支付完整系数表的必要条件、实际完整 polynomial-jet 格的缩放公式，以及一个明确的全部小尺度排除区间；**没有证明所有 \(N\) 的最优整模型都失败**。数学程序0次，旧稿、main、manifest未改。

## 1. 冻结输入与定理对象

本轮实际完整阅读225报告9050B／`9daacd63563f862e2459fee9146b9a31152a4f55e397e3f119d1ca47021ed7af`及目标径向稿5015B／`8d46532cde29b6133687e926e4af02f82e1cf3a7dfbb9f9eaf26a45ff9835afa`。225 manifest49255B／`f2f89ce01ca7e9e56aca9a98185c0ced3c2594c60fe44f26af1fb9d535f79a42`只选读导航、运行账、剩余接口、相关pins等必要字段，不冒称全部旧附件已重读。自己的225 leading稿13928B／`ee1d70e843e53090cefc84dd750452e2ee6c954ae79bf674d0ea9f25ffede798`及B225完整模式稿14444B／`7752b5bfeb3b2090d913b999600695c5a12ffc1c731dd36649d4d89104b5b255`复用已有FULL及独审。

设

\[
 \mathcal D(z)=\sum_{r\ge0}\Delta_rz^r,\qquad
 \mathcal H_g(z)=\sum_{r\ge0}(g\Delta_r+\Xi_r)z^r.
 \tag{V1}
\]

在反证假设 \(\zeta(7)=g\in\mathbf Q\) 下，\(\mathcal H_g=\mathcal J\in\mathbf Q[[z]]\)。已有实际结果是

\[
 \dim_{\mathbf Q(z)}\langle1,\mathcal D,\mathcal H_g\rangle=3,
 \quad \mathcal H_g\notin\mathbf C(z),
 \quad \dim_{\mathbf Q(z)}\langle1,\mathcal H_g\rangle=2.
 \tag{V2}
\]

这些是指定行的函数域秩。六阶离散递推或更高标量微分阶数不会自动增加这些秩。

令 \(L_1=\alpha^9,L_2=(3+2\sqrt3)^9,L_3=3^9\)，其中 \(8<\alpha<9\) 是 \(v^3-9v^2+3v-3\) 的唯一实根。225已付原始分支的两个尺度

\[
 M=L_1L_2L_3,\qquad T_*=L_1L_2q_*,\quad
 q_*\in\{(3/\alpha)^{9/2},(2\sqrt3-3)^9\}.
 \tag{V3}
\]

保留 \(\mathcal D\) 的 raw univalent common map 导数至多 \(4/M\)；即使仅保留目标 \(\mathcal H_g\)，其 raw univalent map 导数仍至多 \(4/T_*\)。这里依靠实际径向非亚纯分支，并非仅比较两个 radius lower bounds。

本轮实际读CDT2025短稿物理pp.3–4的完整Theorem2.1及Remark2.2，并完整读既存选文中的原Theorem2.5.1、Theorem2.7.1和BasicRemark2.11.1。定理所要求的完整合法表是有限列数的嵌套数组

\[
 f_i(x)=\sum_{n\ge0}\frac{a_{i,n}x^n}
 {\prod_{j=1}^{s}d_{\lfloor b_{i,j}n\rfloor}},\quad a_{i,n}\in\mathbf Z,
 \qquad
 \tau=\frac1{m^2}\sum_{i=1}^m(2i-1)\sum_j b_{i,j}\ge0.
 \tag{V4}
\]

每列先为0，随后各行是同一个正数；函数须 \(\mathbf Q(x)\)-独立、holonomic并有同盘实际meromorphic pullback。入口要求 \(\ell=\log|\phi'(0)|>\tau\)。对univalent图，原Theorem2.7.1给 \(E(\phi)=\ell\)，从而严格反证所需的是 \(m(\ell-\tau)>E(\phi)\)。固定有理常数的行归一化可先清除 \(g\) 等固定分母，但不会清除随 \(n\) 增长的 \(N^n\)。

## 2. 全系数的固定素数必要条件

定义 \(f_{i,N}(x)=f_i(x/N)\)。设 \(f_i(z)=\sum_n f_{i,n}z^n\)，固定素数 \(p\mid N\)，\(e=v_p(N)>0\)。则

\[
 [x^n]f_{i,N}=N^{-n}f_{i,n},\qquad
 v_p([x^n]f_{i,N})=v_p(f_{i,n})-en.
 \tag{V5}
\]

任何有限固定表(V4)在此固定素数提供的深度都是

\[
 v_p\!\left(\prod_jd_{\lfloor b_{i,j}n\rfloor}\right)
 =\sum_{j:b_{i,j}>0}
 \left\lfloor\log_p\max\{1,\lfloor b_{i,j}n\rfloor\}\right\rfloor
 =O_{p,\mathbf b}(\log(n+2)).
 \tag{V6}
\]

空LCM取 \(d_0=1\)，不足 \(p\) 的项深度为0。故合法的scaled row必满足，对全部非零系数

\[
 \boxed{\ v_p(f_{i,n})\ge en-O(\log(n+2))\quad(p\mid N).\ }
 \tag{V7}
\]

乘一个固定整数只改变 \(O(1)\)。若存在无穷多个系数使 \(v_p(f_{i,n})=o(n)\)，则此行的任何有限LCM表都不能支付 \(x/N\)。这是必要条件，不是已经为本包所有固定 \(p\) 证明的内容定理；满足(V7)也不自动给出全素数、全行、嵌套的合法数组。

223的 \(d_{2r+4}^{6}\Delta_r\) 与 \(d_{2r+4}^{13}(g\Delta_r+\Xi_r)\) 安全清分母只给 \(v_p(f_{i,r})\ge-O(\log r)\)，没有给排除正线性内容的反向界。224无穷素数引理在 \(r=(p-1)/2\) 给可变素数 \(p\) 的 \(v_p(\Delta_r)=1\)；它不是某一个固定 \(p\mid N\) 上随 \(r\to\infty\) 的内容结论。因此不能把原安全表 \((0,12,26)\) 沿用到scaled rows，也不能宣称“增加几列LCM即可吸收 \(N^n\)”而不核(V7)。

## 3. 实际图的协变与一个已证排除区间

若 \(\phi_N\) 是scaled rows的合法common map，令 \(\psi=\phi_N/N\)。则逐行有

\[
 f_{i,N}(\phi_N)=f_i(\psi),\quad
 \ell_N=\ell_\psi+\log N,\quad
 E(\phi_N)=E(\psi)+\log N.
 \tag{V8}
\]

后一式由双积分的被积函数逐点增加 \(\log N\) 得到；univalence和同盘亚纯性也完全对应。于是实际raw cap转成

\[
 |\phi_N'(0)|\le4N/M\quad(\mathcal D\text{保留}),\qquad
 |\phi_N'(0)|\le4N/T_*\quad(\mathcal H_g\text{保留}).
 \tag{V9}
\]

scaled rows的函数域秩和D-finiteness保持，但它们的整数数组必须重新支付。

由 \((3+2\sqrt3)(2\sqrt3-3)=3\)、225的 \(\kappa>s\) 和 \(\alpha>8\)，得

\[
 T_*\ge L_1L_2s=(3\alpha)^9>24^9,
 \qquad M>144^9.
 \tag{V10}
\]

因此，**全部整数 \(1\le N\le24^9/4\)** 的目标raw-univalent入口均有 \(|\phi_N'(0)|<1\)，在任何合法非负成本表下都失败。保留 \(\mathcal D\) 时可扩大为 **\(1\le N\le144^9/4\)**。这是一次纸面整区间结论，没有参数扫描。对于更大的 \(N\)，(V9)本身不再足以排除入口；不能把原始导数小于1直接说成所有缩放都小于1。

## 4. 完整联合 integer-valued jet 格的必要成本

以下引理不依赖row-wise安全上界。选定全部实际 \(m\) 行，取完整次数 \(0\le j\le D\) 的多项式源；记 \(q=m(D+1)\)。给完整cutoff \(0\le k\le K\)，令

\[
 E_{k,(i,j)}=[z^k](z^jf_i(z)),\qquad
 (E_N)_{k,(i,j)}=[x^k](x^jf_i(x/N)).
\]

所有行与全部源列保留，负指标系数取0。直接得到精确矩阵恒等式

\[
 \boxed{\ E_N=\operatorname{diag}_{0\le k\le K}(N^{-k})\,
 E\,\operatorname{diag}_{(i,j)}(N^j).\ }
 \tag{V11}
\]

定义实际整值格，而非某个足够的小子格：

\[
 \Lambda_N(D,K)=\{a\in\mathbf Z^q:E_Na\in\mathbf Z^{K+1}\}.
 \tag{V12}
\]

它是有限指数全格，因为有限有理矩阵有共同分母。完整交集表达式是

\[
 \Lambda_N=\operatorname{diag}(N^{-j})
 \{b\in\operatorname{diag}(N^j)\mathbf Z^q:
 Eb\in\operatorname{diag}(N^k)\mathbf Z^{K+1}\}.
 \tag{V13}
\]

特别不能只保留原source格，并忽略新的jet同余条件。

若 \(I\) 是 \(q\) 个不同jet行且 \(\det E_I\ne0\)，则

\[
 \det(E_N)_I=N^{-\beta_I}\det E_I,\qquad
 \beta_I=\sum_{k\in I}k-\frac{mD(D+1)}2
 \ge\frac{m(m-1)(D+1)^2}{2}.
 \tag{V14}
\]

最后一步使用 \(\sum_{k\in I}k\ge q(q-1)/2\)。令 \(C\) 为 \(\Lambda_N\) 的整数基矩阵，\(|\det C|=[\mathbf Z^q:\Lambda_N]\)；\((E_N)_IC\) 是整数矩阵，故对每个 \(p\mid N\)

\[
 \boxed{\ v_p[\mathbf Z^q:\Lambda_N]\ge
 \max\{0,\,v_p(N)\beta_I-v_p(\det E_I)\}.\ }
 \tag{V15}
\]

这是真正的联合格必要下界。它自动包括全部prime powers、完整背景行、固定 \(g\) 分母和全部 \(N\)-powers；不假定源列独立余数可免费删去。

由于指定 \(m\) 行 \(\mathbf Q(z)\)-独立，对于每个固定 \(D\)，总有某个有限 \(K(D)\) 使完整jet map满列秩：递减的有限维核若永不消失，最终稳定的非零核就给零形式级数的多项式关系。**这里没有证明 \(K(D)=3D\) 或其它线性cutoff，也没有证明最早 \(q\) 行的minor非零。** 六阶scalar operator不能替代这个零估计。

## 5. 已运输模型的中性，及尚欠的primitive界

若同一个nonzero minor使用最早 \(q\) 个jet行，则(V14)的缩放指数正好

\[
 \beta_0=\frac{m(m-1)(D+1)^2}{2}.
 \tag{V16}
\]

即使不满足这一normality假设，完整图(V11)仍说明：同时把source格运输为 \(\operatorname{diag}(N^{-j})S\)，把jet格运输为 \(\operatorname{diag}(N^{-k})T\)，两边的线性映射精确同构，Smith数据没有新收益。**以下(V17)/(V18)的具体费用限于(V16)模型，或另行已付 \(\beta_I=\beta_0+o(D^2)\) 的asymptotic normality。** 对一般不同 \(I\)，该minor的精确metric费用是 \(2\beta_I\log N/[m^2(D+1)^2]\)，不能免费取成下式。满足所述normality条件并改回标准coordinate metrics时，二次尺度 \(m^2(D+1)^2/2\) 下的费用为

\[
 c_m(N)=(1-1/m)\log N.
 \tag{V17}
\]

这是**指定完整transported determinant模型**的metric换算，不是一个已构造的scaled LCM数组，也不是所有primitive \(\Lambda_N\) 的最优成本定理。其精确中性恒等式为

\[
 m\bigl((\ell+\log N)-(\tau+c_m(N))\bigr)
 -(E+\log N)=m(\ell-\tau)-E.
 \tag{V18}
\]

所以，如果某项算术holonomy证明真正使用这个已经运输并付足的模型，缩放没有增加其严格margin。原三行 \(m=3\) 的shift为 \((2/3)\log N\)；指定子源 \((1,\mathcal H_g)\) 的 \(m=2\) shift为 \((1/2)\log N\)。这些常数不是凭安全表猜出的必要最优值。

要把(V18)提升成“所有 \(N\)、所有联合模型均无收益”，必须控制(V15)中的**原minor正素数内容**。例如 \(v_p\det E_I=o(D^2)\) 会保留相应 \(p\) 上的二次缩放费用，但本包尚没有这种same-cutoff、same-source结论；即使支付了它，也须与同一算术holonomy对象的全部其它费用一起比较。把原安全 \(\tau=166/9\) 当必要下界，再叠加(V17)，是不合法的。原LCM表是充分清分母上界；它不排除固定素数的指数内容或多行joint cancellation。

## 6. 去重、停止范围与下一项准入

历史dyadic number-field supplement已证明其指定clearing class的全place运输及解析metric协变，并明确未证明primitive最优性；221的 \(t=\kappa v\) 条目也已提醒必须改完整source-column/jet基。本稿没有把这些旧结论当新全归一化定理。旧“scaled-root optimum”是monic辅助多项式根位置的优化，与此处 \(z=x/N\) 不同。

当前最强已证结论是(V7)、(V11)–(V15)、指定运输模型的(V18)，以及(V10)所给明确全整数区间的入口排除。更大 \(N\) 的literal CDT数组尚欠实际固定素数内容；其primitive联合jet成本尚欠原minor内容与有效nonzero cutoff。未付这两项前，本稿既不宣称全部有理缩放失败，也不认证一个新合法入口。若继续固定包，优先支付一个真实可用的scaled完整数组或一个primitive内容下界；仅调整已有安全LCM表不会解决此准入问题。

实际primary阅读及运行账见 [A226 scope](../literature/pade_rational_scale_sources_round226_20261008/lambert_reading_scope.md)。作者保存后须完整复读本稿与scope，再报告最终bytes/SHA256；该作者自读不冒充独审。
