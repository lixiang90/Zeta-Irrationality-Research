# 高偶数 beta 值解析迁移的正式独立审查

日期：2026-10-07。审查者：/root/source_pencil_finalize。结论：**纸面证明 PASS**，没有进一步数学修改请求。实际 FULL 读取 catalan_higher_even_beta_analytic_transfer_20261007.md 全十节、A1–A29及公式A1–A37；最终审查输入 SHA256 3e3d8df6181cdca82e65103687c9bfe7c5d93772245bb5cf7b4e24a85f7b5e8a，23944bytes。没有用文件 SHA 或数学程序替代证明。

独立核对的正面结论是：固定有限的非负测度权重保留真实两分支 Hardy/Cauchy 实处二次界；对称 t-log 权重使实际起始周期准确成为 \(4\beta(2m)\)。完整周期投影、可比较的有限处预算和无穷尺度非零性仍未证明，故没有新的数值无理性结论。

## V1. 原行、核与两个积分测度确为同一对象

原 Catalan foundations.tex 与 real-place.tex 的参数、star、P/D的Chebyshev多项式、接触阶、整数列filter均与A1一致。R本身是代数曲线上的行，最终稿已正确区分R与实际多项式P、D。由

\[
fD/t=(R^*-R)/2
\]

可直接得到负半轴\((R+R^*)/2\)、正半轴\((5R-R^*)/4\)，所以两分支系数恰是\((1/2,1/2)\)、\((-1/4,5/4)\)。新增 \(\rho(t),v(s)\) 同时乘M与Z；它们不改变这些系数、原Cauchy核或原列filter。若只加权M则此证明不适用，主稿已明确限制。

行在0连续，因为D最低阶大于1；在两端有连续有限值。对N固定，行有界是足以做Fubini的真实条件；没有要求其界独立于N。

## V2. 绝对可积性、双 Andréief 与有限测度付款

独立核得
\[
(1-ts)^{-1}\le(1-s)^{-1},\qquad
|\psi_k(s)|/(1-ts)\le(1-s)^{q-1}\le1.
\]
每个置换展开项中，一个 \(s_j\) 只承受一个Cauchy核，并携带一个 \(s_j^{b+k}(1-s_j)^q\)；因此所有项均由有界行乘有限测度质量控制。即使 \(\rho,v\) 无界，Fubini与两次Andréief仍成立。绝对连续权重下节点重合和端点为零测度集合，原原始表达式提供积分定义，不需要新增节点分离。

双Cauchy/Vandermonde代数完全不变。real-place.tex 的两个majorant先是点态界，再对原测度取上确界；新测度只把总质量 \(2^n\) 换为 \(K_t^nK_s^n\)。原Hardy压缩及后备界、两个 \(1/n!\) 的付款仍在。因此A11成立，新增费用为 \(n\log(K_tK_s)\)，没有新增 \(n^2\) 常数。固定权重、固定m的量词不可改成随N增长。

## V3. 定量阻尼与实处二次证书

对原 energy.tex 的全部显式比较逐项核查：核比较余量为 \(O(\varepsilon)\)；x-cosine、负x-power对角的底分别以常数倍 \(\varepsilon\) 控制；s-cosine对角底为 \(\varepsilon\sqrt{1-s}\)。先保留
\[
-\langle\log(1-x)\rangle/(2n),\qquad
-\langle\log(1-s)\rangle/n
\]
后，其余对角费用仅 \(O((1+|\log\varepsilon|)/n)\)。指数衰减试验系数使三个阻尼切线的统一差为 \(O(\varepsilon)\)，与节点无关。

两个一元外场在0的正系数不变，弱化后的端点系数在 \(n\ge24\) 时至少 \(1/24\)，其余切线均统一有界；固定比较点给最大值的共同下界。故 maximizers 位于共同紧集（x的常规端点−1包含在其中）。在此集合上的 \(O(1/n)\) 系数误差统一，严格允许选 \(\varepsilon=1/n\)。A13–A14的 \(O(n\log n)\) 于是成立，不是直接在非一致Fourier级数里交换极限。

数值常数 \(-2.290939875\) 与原 certificate.tex 的两case结论一致。此次审查FULL阅读该章的试验函数、根括区、对数余量付款与结论陈述，但**没有重算**四个分子、全部sign variations、模101或50个有理对数值，也不声称产生了一份新数值证书。A15正确引用原证书；独立于该数值证书的A14则对每对合法试验序列成立。新密度没有改变所调用试验函数的任何自变量或domain。

## V4. 高s阶梯的符号、周期系统与完整形式整格

由 \((v+1)m_v=vm_{v-2}\)，直接核对A22的三条递推。

第一条的分子是 \((u+1)(m_{a+u-2}-m_{a+u})\)，所以lower阶差的次序为 \(K_{d-1}^-(a-2)-K_{d-1}^-(a)\)。plus递推向后移两位，剩余分子是 \((a+u-1)(m_{u-2}-m_u)\)；u=0项不可删，最终常数为 \(+2/(a-1)^d\)。a=1用 \(m_{-1}=0\) 得 \(K_d^-(1)=U_{d-1}-K_{d-1}^-(1)\)。d≥2所有参与系列都单独收敛；d=1确须原有限telescoping版本。

这些两起始加对角递推按d归纳给A23的完整生成系统。A24的partial fractions符号可由d=1起步逐次分母分解核得；两个1阶发散项抵消，非对角留下ζ2,…,ζd，对角则是ζ(d+1)减有限harmonic。没有把这些真实低阶周期免费消掉。

形式分母方面，在 \(i,j<H\) 上 \(H!m_i\in\mathbb Z\)。一次boundary递推链逐个除的整数积整除H!，每升一阶添加一个H!足够；对角付款亦由 \(H!^{d+1}\) 覆盖。Z系数中partial-fraction分母指数与harmonic指数相加至多d+1，所以 \(D_H^{d+1}\) 更已足够。主稿据此给完整但粗的全有限处**形式**整模型，未使用生成周期独立性。

唯一审查修订已落实：清分母后的整数多项式总次数是**至多n**；把常数1保留作形式变量时可齐次化到n次，但不能在未证非零时强称实际次数恰n。该模型的付款可达 \(O_d(n^2\log n)\)，且未使目标有理假设下的矩阵变成有理，主稿限制正确。

## V5. 真正的2-adic平滑与不能移用的determinant费用

原factorial bound给
\[
v_2(m_{i+u}/(j+u+1)^d)
\ge i+u+1-(d+1)\log_2(H+u).
\]
右边趋 \(+\infty\)，所以新平滑系列在 \(\mathbb Q_2\) 收敛。利用 \(H+u\le H(1+u)\) 得A28的uniform界，有限常数 \(C_d\) 的定义也一致。

真实Chebyshev coefficient的 \(v_2(p_{r,u})\ge u-1\) 与卷积后degree \(C-1-u+v\) 相加，u抵消；整数卷积不会添valuation损失，得A29。它是原实际行的高valuation通道。

高阶boundary会耦合lower阶discrepancies，A29不能自动恢复原S/E/B三column alternation。主稿没有将原 \(-505/4608\) quadratic fee transplant到新array，这是必要限制。

## V6. beta起始的准确修复与全端点

s-log权重质量为1，但其起始 \(T_d\) 对d≥3严格小于9/4，而 \(4\beta(2m)>9/4\)（m≥2），因此该起始不等于目标。用 \(m_{2k}\le2\) 和递减函数的积分上界即可独立核A20，不需数值。

t-log权重A30则不同：其偶性、非负性和质量有限成立；0处为 \(O(|t|^{2m-1})dt\)，±1处是可积的半阶奇性乘固定log幂。未滤波M/Z在s积分后至多多一个log，仍绝对可积。

准确配对t与−t后，M00为
\[
\int_0^1\rho_m(t)\Lambda(t)(1-t^2)^{-1/2}dt.
\]
以 \(u=\sqrt{(1-t)/(1+t)}\) 代入，\(\Lambda=-2\log u\)、\(dt/f=-2du/(1+u^2)\)，A30的 \(2^{2m-2}(2m-1)!\) 与这些factors恰给
\[
\frac4{(2m-1)!}\int_0^1\frac{(-\log u)^{2m-1}}{1+u^2}du
=4\beta(2m).
\]
有限几何展开或绝对积分级数都合法。因此A32与A33同时成立，是真实解析carrier；没有仅改首moment而忽略其他entries。

## V7. 多变量、confluence和prime-layer范围

uniform变量乘积的推前密度是 \((-\log s)^{d-1}/(d-1)!\)，A34的卷积与Jacobian正确。先合并每列的一组独立变量为S_j，保留原Cauchy核及V(S)，不新增interaction。

独立列参数的每列ℓ阶导数由行列式多线性给A35；共同参数的ℓn阶导数会混入其它分配，不能代替。原Cauchy界只在这些导数恢复共同密度以后使用。对核本身求导的A36改变Cauchy结构，主稿未移用旧energy。

fresh FULL nonvanishing.tex 确认原seed的三矩阵只处理d=1 rational array及其两个不同extraction shifts；原integer Frobenius多项式身份不足以推出新矩的prime-layer。A37的 \(v_p(-H_p^{(d+1)})=-(d+1)\) 因唯一p项具有最低valuation而成立；该入口例子不被误报为最终mixed determinant费用下界。

## V8. 最终范围与个人读取记录

已实际FULL读取主稿3e3最终版本全部十节及本地官方primary六章，目录为 E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/，文件分别为 foundations.tex、real-place.tex、energy.tex、certificate.tex、nonvanishing.tex、conclusion.tex。

六章均分开无截断读取。此次**review域新增PDF读页0、render0、新下载0、数学producer创建/执行/import/rerun0、prime/guard/Lean0**。本审查者另项level7主稿的个人14页primary域与这里的tex域分别记录，不冒认同行的Lai或其他PDF页。没有FULL读取odd-primes章节，也没有核证所有外部证书计算或Lean依赖。

最终主稿对三条未证桥的区分准确：仅目标值有理时的完整周期投影；同一有理整模型的可比较全有限处预算；无穷尺度非零性。没有把正测度变成Gram正定性，没有把原seed变成普适seed，也没有从一个beta起始值声称高偶beta已无理。所有被要求的范围修订已完成，审查结论为PASS。
