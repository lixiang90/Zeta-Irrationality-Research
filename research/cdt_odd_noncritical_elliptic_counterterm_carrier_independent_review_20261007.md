# 非 CM 椭圆反项积分载体：独立全文审阅

2026-10-07。Reviewer：/root/scaled_root_finalize；作者：/root/masked_racah_finalize。本轮唯一指定正式对象为 research/cdt_odd_noncritical_elliptic_counterterm_carrier_20261007.md，SHA **32e8352c28c394d95470f393cb3408d3de42ed2aa1a8c32ac2ca8584595e58bb**，18217 bytes。本人 actual FULL 八节、正文 N1–N21／公式 N1–N27，核 physical fingerprint，并独立纸面逐式复核。

结论：**PASS，无正文修改请求。** 核准同一数值 ratio 的真实新 counterterm primitive、全 n/all powers half-width 整模型、matching prefix leading5/2、whole-array safe费用21/10、actualrank5及完整 native/transported跳跃。没有核准新的数值无理性；21/10是该已证模型的安全上界，不是任意新basis/model的最小费用。

## 1. V1：同一数值 normalization、kernel 与起点

本轮 fresh FULL Koutschan–Zudilin v1 PDF1–6，实际 PDF5给
\(\lambda(1/16)=30L(E,2)/\pi\)、\(\rho_1(1/16)=L(E,\chi_{-4},1)/2\)；
PDF2–3给 \(\lambda=2\pi\,{}_3F_2\)、\(\rho_1=\pi\,{}_2F_1\)。
所以 \(\lambda/(2\rho_1)=Y/F=30L(E,2)/(\pi L(E,\chi_{-4},1))\)，主稿 N3 的 factors准确。没有把 elliptic period或π降到Q；作者原件 PDF3–4的分母实验数组没有用于本文全素数证明。当前没有重新读LMFDB网页，nonCM标记只作为已冻结对象范围，不冒认新status检索或穷尽未知性证明。

整数坐标z=16t同时给 \(\mu=1/256,\sigma=1/16\)、\(b_j=\binom{2j}{j}^2\)。直接合并两个partialfractions：
\[
 (t-\mu)^{-1}-16(t-\sigma)^{-1}
 =-15t/((t-\mu)(t-\sigma)).
\]
原点constant恰消失，K的Taylorcoefficients为 \(-[256^{\ell+1}-16\cdot16^{\ell+1}]\)，全整数。积分后第n coefficient只用j≤n−2，N7成立；z₀=z₁=0，z₂=−256·240(1−u)/2=−30720(1−u)。这些固定初值没有自由选particular。

## 2. V2：native与transported的完整跳跃

ordinaryµ处 \(H_u=Y-uF\) analytic，K residue1，primitive精确为
\(H_u(\mu)\log(t-\mu)+\text{analytic}\)。所以N9是完整constant germ jump；r=u假设消去整个native logarithm和全部jets。反项在µ的analytic部分不改变此机制。便宜KH本来meromorphic，作者没有为其polefill重复领取relation-dependent leaf收益。

N10在普通基点以“相同值、相同derivative”独核成立：Πℓ是continuation过程中真正integral，余项导数为 \(K(H^\ell-H)\)。任意access g到ordinaryµ，µ小圆对原H无monodromy，所以共轭loop的primitive增量精确为constant \(2\pi iH^g(\mu)\)。它并不强迫所有µlifts同时filled。

σ处 \((2\theta+1)Y=F\) 的积分使Y的order0 log系数为0，F的order0 log系数非零；于是N12的q₀=−u a_F(0)准确。K=−16/s+analytic。对N13直接求导，log系数为
\(-16q_0/s+\beta'=Kq\)，constant项的pole由β(0)=−16h₀消去。这独立验证完整analyticβ、γ的存在以及全跳跃
\[
 \Delta_\sigma Z=-2\pi i\,16q_0\log s
                 +2\pi^2\,16q_0+2\pi i\beta(s).
\]
u≠0时非零log²，u0时Y(σ)>0给非零log。真实r∈(0,1)属于前者。此新反项未增加puncture，却确实增强了原σ分支，scope准确。

## 3. V3：实际rank和rationaloperator

本轮实际 FULL 回读旧2ee738主稿与旧3a8dd独审，重新核其monodromy证明。Gauss两处非零unipotents的fixedlines不同，F的orbit differences张成二维space；Wronskian排除RF+SG+T=0。∞Euler integral的非零 \(t^{-1/2}\log t\) leading给Y的唯一 \(t^{-1/2}A_\infty(0)\log^2t/4\) term；其它j≥1只给一次log。故1,Y,F,G实际rank4。

对S=T∞²，两次loop恢复half-power符号，logt改变±4πi。二次差分消去每个一次log，留下完整identity
\[
 (S-I)^2H_u=2(\pm4\pi i)^2A_\infty(0)t^{-1/2}/4
           =-8\pi^2A_\infty(0)t^{-1/2}.
\]
它沿ordinarypaths搬回µ仍非零，故三个实际branchvalues不能全零。至少一条primitivebranch在µ有nonzero whole log；rational combination of1,Y,F,G在µ每条branch只能meromorphic。于是加入Z使actualrank5。

手展开R_u determinant得
\[
 \frac14-\frac u2(1+a)+u^2(\frac14+\frac a2-b)
 =\frac{(1-u)^2-16t}{4(1-16t)}\ne0.
\]
θZ=tKH的三角jet变换对角均tK≠0，所以主稿N18五行实际rank正确。N19的operator以明列R_u、matrix和rationalinverse确定，K⁻¹∂Z=H；这只证明functionfield身份，未将rationalgauge免费当整basis。scalaroperator的apparentpoints没有成为真实新puncture，未冒称已构造motiviccycle。

## 4. V4：全 N、全 prime powers 的一层真实消去

旧粗模型 \(MnD_{2n-3}z_n\in\mathbb Z\) 由N7的奇数innerdenominators直接给出。独立核N21如下：

N0/1系数为零；N2的z₂已为M分母内integer。N≥3，oddp置e=v_pD_N、e'=v_pD_floor(N/2)、f=v_pD_(2N−3)≥e。区间(N/2,N]至多一个p-power，所以e'=e或e−1。前者由旧粗模型支付。

后者q=pᵉ∈(N/2,N]。n≠q时，任何n≤N若含pᵉ必为q的倍数，但2q>N，所以v_pn≤e−1；全部innerdenominators由f支付。n=q时，inneroddnumbers≤2q−3，唯一含pᵉ的是q，对应j=(q−1)/2；其余valuation≤e−1。最高term的bracket是
\[
 A^{(q+1)/2}-16B^{(q+1)/2}\equiv A-16B=0\pmod p,
\]
因为A=2⁸、B=2⁴为squares，q−1被p−1整除。故只节省一层p：全部项valuation至少−(2e−1)，而e−1+f≥2e−1。MuF部分无innerdenominator，也被同预算支付。作者没有把pᵉ全部删去。

p2时innerdenominators全odd，M z_n valuation≥−v₂n≥−e；N≥3给f≥1、e'≥e−1，故e'+f≥e。N2不错误套这个不等式，而已经独立支付。inputM一开始清掉u，故inputprimes也包含在证明中。N21是所有N、所有n≤N、全部powers的actualprefix模型，而非PNTleading或first-prime实验。

取N=n给N23；正θjets的integerindex消去primitive n分母，继续使用D_(2n−3)。本人未运行任何coefficients或primes。

## 5. V5：matching lower 两个 indices，保留3p项

对p>5、p∤M，n=2p时innerdenominators≤4p−3<p²，含p的恰p与3p。分别j₁=(p−1)/2、j₃=(3p−1)/2，Lucas给b_j₁≡1、b_j₃≡4。第一个bracket指数(3p+1)/2，因A/B均squares而化为A²−16B²=A(A−B)；第二指数(p+1)/2化为A−16B=0。因此第二term不能漏列，但确在该p层消失，得到
\[
 p^2z_{2p}\equiv-\tfrac12A(A-B)\pmod p.
\]
uF及所有其它terms在乘p²后消失，leftside的p-adicintegrality先由N7保证。

n=(p+3)/2时唯一innerp term为j₁=n−2，bracket指数2；n≡3/2 modp，遂
\[
 pz_{(p+3)/2}\equiv-\tfrac23 A(A-B)\pmod p.
\]
A(A−B)=256·240仅含2、3、5，故goodprimes上两式全unit，valuation准确−2、−1，与u无关。

在prefix≤N，p≤N/2使用2p，p≤2N−3使用(p+3)/2。所以lower为 \(\vartheta(N/2)+\vartheta(2N-3)-O(\log N)\)，固定finiteexceptions无碍；N21 upper为 \(\log M+\log D_{\lfloor N/2\rfloor}+\log D_{2N-3}\)。两者均5N/2+o(N)，主稿N25是matchingactualprefixleading，不声称每个power都sharp。

## 6. V6：真正标准 whole-array 与21/10

本人本轮fresh FULL CDT fixedv2 PDF66–69：b列允许realwidth，fixedintegerindexshifts由Remark6.0.12在原limit机制支付；holonomic可放松conformal门槛，但meromorphicpullbacks不可省。

N20/N23给排序(1,θZ,θ²Z,θ³Z,Z)的两个标准列
\((0,2,2,2,2)\)、\((0,0,0,0,1/2)\)，全部e=0。独立计算flat费用：
\[
 2(1-1/25)+\tfrac12(1-16/25)
 =48/25+9/50=21/10.
\]
这比旧选定safeupper57/25低9/50；没有把旧upper当最小值，也没有仅从leading5/2倒推出新CDTtype。fixedM不带新n指数，θjets用同coordinate，预算完整。

nativeµ在relation假设下真正填掉；nativeσ仍log²，transportedµ至少一条仍bad。rounddisc限制只用于nativebranch，不移给任意leaf、多map或uniformization。作者没有宣称严格holonomyquotient、新irrationality、数值LI或Lean。

## 7. V7：查证范围与文献状态

作者§8的primary搜索是locator/status范围；本人没有扩展搜索或将未搜到无理性当定理。KZ PDF5的k>4源确含originlog(z/16)，作者确说新recurrence未带来可认领irrationality；这些没有被免费移给本稿原点Q-Taylor。对Brunault／Rogers–Zudilin的metadata仅按作者范围解释，不冒称当前review全文读过那些原件。

本review mathematicaljudgment来自实际完整正文、旧直接输入与primary，未继承作者或旧review的运行/读页证据。没有下载或新数学支线。

## 8. V8：本轮实际 read domains 与闭合

actual FULL本轮：目标32e835八节/N1–N21；冻结2ee738八节/E1–E25；冻结3a8dd独审V1–V8。对authority完整JSONparse、current_progress printed读取与physicalhash核验，mutable总稿§§201–205本轮已FULL读用于定位，不作receiptpin，也不冒认620数学全文审查。

primary实际FULL（text可见、render0）：

- KZ arXiv2111.08796v1，既有literature/cdt_gamma_noncritical_elliptic_sources_20261007/koutschan_zudilin2021_apery_elliptic_l_values_arxiv2111_08796v1.pdf，PDF1–6；126817bytes、6archivepages、SHA8f55e4b6b8bd772ee83b5d4638af06e8af17b75e8907c49fa307434d9a515ad7。
- CDT fixedv2，literature/cdt2024_l2_chi_minus3.pdf，PDF66–69；4517169bytes、218archivepages、SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。与ownmain当前同页复用，不重复计数。

review域10distinctPDF页，只有KZ6为本轮ownmain22页以外新增；个人本轮union28distinct，未继承上一轮13页。数学producer创建/执行/import/rerun、prime、guard、Lean均0。documentaryread/hash/metadata不算数学执行。

本review最后actualFULL自读后送作者收审；作者收审后最后FULL回读主稿，再一次生成其单向FINALreceipt。当前review不pin未来audit、mutable总稿或同行receipt；旧620 frozen字节不改。
