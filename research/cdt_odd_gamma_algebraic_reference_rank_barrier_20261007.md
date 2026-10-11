# 新增对数奇点的整代数参考族：超出分母改进的 CDT 秩比较

2026-10-07，作者 /root，唯一 NEW 纸面主稿。Authority 为总记录 §§186–190 和 delivery_relative_lift_tensor_reference SHA `61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd`。596 冻结记录（591 数学、5 guards）物理 SHA/bytes 本轮全部重核不变；未执行/import/rerun旧或同行数学producer、guard或素数表，未建立新数学producer。原 paired source ξ=αζ(4)+βζ(5)、β≠0 保持。本文只证明同一 inverse-L 校准及其明确有限放大的新比较，不宣称数值无理性或 Lean。

本轮实际 FULL 重读冻结 [reference 主稿](cdt_odd_gamma_lift_holonomy_reference_gate_20261007.md) H1–H20/七节，以及总记录 §§186–190。实际 FULL 读取 CDT 固定v2原件 PDF66–69，特别核对 Definition6.0.1、Theorem6.0.2、Cor6.0.14 的非负费用、holonomic 条件、holomorphic maps、same-partition 多map分子及固定倍数/limiting条件。新的整代数参考族在下面自足纸证，不依赖另一分支待审的新结论。

## 1. 保留实际极点、所有分支和允许 maps 的范围

**A1.** 冻结 inverse-L 校准给

\[
 A=-2^{20},\quad \mu=A^{-1},\quad
 F_u=B_5-u f_0,\quad u\in\mathbb Q,
\]
\[
 LF_u=r_5,\qquad
 F_u=\lambda_\mu(t-\mu)^4\log(t-\mu)
 +\text{analytic and higher-order log terms},
 \quad\lambda_\mu\ne0.
 \tag{A1}
\]

每个 transported branch 的同一首系数非零；齐次差在μ ordinary point analytic。任意 holomorphic nonconstant φ:(D,0)→(C_t,0) 若 F_u∘φ 是指定germ的全盘meromorphic延拓，便不能达到μ：有限ramification h仍留下非零(z−z0)^(4h)h log(z−z0)。因此所有这一族的 target-admissible maps 都 omit μ。这里没有将φ假设为univalent，也没有限制到某一预先选定的slit plane。

以下更一般比较只要求：给定 target-admissible maps 已经有上述 omission 证据。若某个投影删除F_u，且其它rows可能消去完整μ跳跃，不能继承该证据；本文不对这种不同family作无条件排除。

## 2. 指定整数坐标下有高秩、零分母费用的代数函数

**A2（完整族及真实rank）。** 对 s≥1、q=2^s，取规范 Taylor germs

\[
 G_k(t)=(1-At)^{k/q},\qquad 0\le k<q,
 \qquad G_k(0)=1.
 \tag{A2}
\]

这q个函数在 C(t)、从而Q(t)上线性无关。若 Σ r_k(t)G_k=0，绕μ正向loop的j次给 Σ r_k(t)e^(2πijk/q)G_k=0，j0..q−1；有理coefficients单值，Fourier矩阵可逆，故每个r_kG_k=0。该证明检查实际scalar函数，不把形式algebraic degree或某个module rank当作结论。

每行阶1 holonomic：

\[
 (1-At)G_k'(t)=-(kA/q)G_k(t).
 \tag{A3}
\]

**A3（所有有限处的准确整性）。** 若1≤s≤19，则

\[
 \boxed{G_k(t)\in\mathbb Z[[t]]\quad(0\le k<2^s).}
 \tag{A4}
\]

证明 [t^n]G_k=binom(k/2^s,n)(−A)^n。k0给常数；其它k将分数约分为k'/2^s'，k' odd、s'≤s。每个k'−2^s'j为odd，所以对n≥1精确

\[
 v_2([t^n]G_k)=(20-s')n-v_2(n!)
 =(19-s')n+s_2(n)\ge0,
 \tag{A5}
\]

其中s2(n)是二进制数位和，Legendre身份 v2(n!)=n−s2(n)可逐floor层直接相加。k/q本来整数时binomial整且更直接。

对 odd prime p，k/2^s∈Z_p。自足说明binomial的p整性：固定n，取非负整数a_h趋近k/2^s于p-adic topology；falling-factorial polynomial的差可被任意高p幂整除，除去固定n!后仍趋近。所有binom(a_h,n)都是整数，故其极限binom(k/2^s,n)∈Z_p。于是所有odd primes亦整。本文没有把在2处的Eisenstein scaling当成只检查一个prime的完整整模型。

所以q=2^19给实际rank524288的整Taylor族；当前rank10只需q16/s4，并从中取任意十个不同k即可。参考族自己的真实rank不自动加入target的rank。

**A4（同一maps的真实pullback）。** 若φ omit μ，1−Aφ全盘无零。单连通disk上有规范global holomorphic log，其起点0，于是

\[
 G_k(\varphi(z))=
 \exp\{(k/q)\log(1-A\varphi(z))\}
 \tag{A6}
\]

是全盘holomorphic，恰为指定Taylor germ的pullback。额外target奇点只缩小允许maps，不能使这个参考族失效。

## 3. 同map零费用比较排除当前rank10的任何非负算术账本

**A5（任意相同m的参考数据）。** 给定2≤m≤2^19，选q=2^s≥m且s≤19，从A2中只取k0..m−1。它们实际Q(t)独立、holonomic、Z[[t]]，因此 CDT可使用一个全零column、e=0，准确τflat=τsharp=0；全零column对应u_j=m，没有未支付的正宽度或finite-place幂。所有maps沿A4合法。

记ρ=log|φ'(0)|。若ρ>0且满足原CDT boundary/integrability或limiting条件，Cor6.0.14给

\[
 \boxed{J(\varphi)\ge m\rho.}
 \tag{A7}
\]

现在任何同maps的m个target函数若有已支付的CDT费用τ_T≥0、ρ>τ_T，必有

\[
 \boxed{\frac{J(\varphi)}{\rho-\tau_T}
 \ge m\frac{\rho}{\rho-\tau_T}\ge m.}
 \tag{A8}
\]

因此不能得到strict rank contradiction。即使τ_T被改进成0，最后仍只有≥m；若J=+∞，则strict contradiction本就无从成立。未满足原CDT解析条件的map不在比较范围。

**A6（完整多map版本）。** 保持同一个m、同一个分割0=γ0<…<γl+1=m。记

\[
 \mathcal N_{\varphi,\gamma}=
 \iint\max(g_{\varphi,\gamma}(a),g_{\varphi,\gamma}(b))\,da\,db
 +\frac1m\sum_{k=1}^l\gamma_k^2
 \log\frac{|\varphi_k'(0)|}{|\varphi_{k-1}'(0)|}.
 \tag{A9}
\]

参考族以同m和same-partition应用Theorem6.0.2，给 Nφγ≥mρ_l；target同一个完整分子除以ρ_l−τ_T亦≥m。没有更改rank时偷换partition、丢弃derivative-gap terms或只看largest derivative。

**A7（对现有lift的实际收益）。** frozen H11给{1,F_u,DF_u,…,D8F_u}实际rank10且每个admissible map因包含F_u而omit μ。选q16、first ten algebraic roots，A8–A9于是排除其任意非负CDT算术费用，不只旧uniform cap9。

上轮s<205/33是较弱log-power reference的必要条件，逻辑上仍成立；现在它已不是可以指导此固定rank10 family获得余量的充分路线。即便未来有真实Dn5、Dn1或zero denominator cap，保持这组functions、同一forced omission及这套CDT分子也不会闭合数值矛盾。

## 4. 更高rank参考可以用精确坐标缩放支付

**A8（任意q的完整整模型）。** 对s≥1令

\[
 q=2^s,\quad B=2^{\max(0,s-19)},\quad x=t/B,
 \quad \widetilde G_k(x)=(1-ABx)^{k/q}.
 \tag{A10}
\]

v2(AB)≥s+1，A5原证明给所有k行在Z[[x]]；odd prime证明不变。选任意m≤q行真实rankm，全部费用0。这里是显式改坐标，未将原G_k(t)在s>19时谎称整Taylor，也未把指数有限prime分母误写成CDT Definition6.0.1的n^e：后者e是积分的指标分母，不是指数型bad-prime费用。

对原φ定义ψ=φ/B，则ψ holomorphic、ψ'(0)=φ'(0)/B，且

\[
 \widetilde G_k(\psi)=G_k(\varphi),\quad
 \rho_\psi=\rho_\varphi-\log B,
 \quad J(\psi)=J(\varphi)-\log B.
 \tag{A11}
\]

每个等式保留同一germ、pole位置、完整Jensen分子和derivative；没有只改arithmetic coordinate而保留archimedean scale。

**A9（任意rank的已支付比较）。** 对m≤q、ρ>logB，零费用参考族在x坐标给

\[
 \boxed{J(\varphi)\ge m\rho-(m-1)\log B.}
 \tag{A12}
\]

多map情形将全部φ_k一同除以B，原same-partition patched g整体减logB，所有derivative ratios不变。因此准确

\[
 \boxed{\mathcal N_{\varphi,\gamma}
 \ge m\rho_l-(m-1)\log B.}
 \tag{A13}
\]

若target的已支付费用满足τ_T≥logB、ρ_l>τ_T，则Nφγ≥m(ρ_l−τ_T)，仍不能产生strict rank contradiction。这个充分排除条件没有被称为最优必要条件；当τ_T<logB或失去forced omission时须重新分析。

## 5. 当前九个jet的有限polynomial放大仍被精确比较封住

**A10（量词与真实rank upper）。** 固定u∈Q、d≥1。仅考虑由

\[
 X=(F_u,DF_u,\ldots,D^8F_u)
\]

的degree≤d polynomials形成的finite family，coefficients在Q[t]；要求family包含1和F_u，选择m个真实Q(t)独立rows。多项式t coefficients不增加overQ(t)的span。因此

\[
 2\le m\le\binom{d+9}{9}\le(d+1)^9\le2^{9d}.
 \tag{A14}
\]

这里只是实际rank upper，不声明这些monomials全都独立、未知differential Galois extension已算出、或formal symmetric power自动给函数rank。保留F_u是forced omission的已支付来源；删除它后的其它projections不在本命题中。

**A11（当前uniform整模型）。** frozen H7每个X_j由一个fixed rational multiplier和Dn9支付；乘积中每个index≤n，所以D_{n_i}|D_n，degree≤d的convolution准确由fixed multiplier及Dn^(9d)支付。Q[t] multiplication只有非负index shifts，亦由Dn支付。所有rows holonomic，由finite-dimensional rational differential modules的tensor closure直接得出。

使用first row1、其余m−1行9d的nested width1 arrays、e=0，合法safe费用是

\[
 \tau_T=9d(1-m^{-2}).
 \tag{A15}
\]

本文只检查这个已证明uniform账本，未把它当minimal cap；未来更细mixed数据须另证明。

**A12（全部d都不能仅靠该放大逃出）。** 取s=ceil(log2m)、q=2^s，A10的B满足B≤m，故logB≤logm。又log2<3/4（严格凸的1/x在[1,2]的trapezoid upper为3/4），于是由A14

\[
 \log B\le\log m\le9d\log2
 <\frac{27}{4}d\le9d(1-m^{-2})=\tau_T.
 \tag{A16}
\]

故A13对这个degree任意大但finite的family都适用：即使其真实rank超过524288，精确坐标缩放后的代数参考族仍排除同maps/current uniform账本的CDT严格余量。这是对一种具体rank放大方案的证明，不是对所有tensor、all arithmetic arrays或一切ζ无理性方法的no-go。

## 6. 当前进展、结构出路与证据边界

**A13.** 本轮收益是找到同一forced-omission leaf上的高秩整代数参考，而不是添加未证明的target rank。现有rank10的障碍从“uniform cap9太贵”收紧为“任意非负CDT费用仍不能在这个leaf/interface产生rank矛盾”；保留F_u的当前polynomial amplification也被精确scale comparison封住。

**A14.** 真正改变该结论须改变一个明确假设：构造能完全去掉ordinary μ jump的新period、使用新的base/多conifold结构、给出删除F_u后仍有非有理真实独立rows且允许穿μ的projection，或采用原CDT rearrangement theorem以外的已证明更强工具。不能单凭一句“更深数学”或一次prime抵消宣布这些接口已经存在。上轮explicit inverse-L lift仍是构造进展；原ξ双项及κ5/κ7另一forcing identity仍未支付。

**A15（实际阅读和闭合）。** 本稿直接primary只有CDT固定v2原件PDF66–69，4 distinct页，actual FULL text读，未新下载或render。新根端数学输入为全文回读的旧reference H1–H20；authority§§186–190实际读，596旧记录物理核不冒称人工全文重审。所有5 guards实际全文读、状态bytes不变、不执行。全部新结论为纸证，尚待正式独立全文审查、作者收审后最终全文回读及单向FINAL来源收据；本稿不pin未来audit或收据。数学producer、prime扩表、Lean均0；未得新的ζ/L/Catalan数值定理，goal保持active。
