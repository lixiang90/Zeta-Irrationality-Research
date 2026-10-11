# 同一配对格对偶 carry 与大素数 jet 费用的独立联合审阅

日期：2026-10-06。NEW 独审，quarter_actual_rank。全部数学源与已有JSON均只读；本人没有 execute/import/rerun任何旧或同行数学producer。两份论文的全尺度结论以纸面核验为主，不以有限样本推成无限结论。

## Q1. 实际全文读取与最终输入定位

root `cdt_odd_paired_dual_plucker_carry_rate_20261006.md` 实际全文读初稿0732514ee6276a1b6be8b5dd0a0f1b9bce9fe190b5588d7909d45a987c9333a6，随后再次完整无截断读终稿 **0fb995f69cefcd4e6c92f7ffa42a8e595add4dda9a94951ed27a4693fb127047**，全部D1–D10和公式D1–D21。三处最终clarity修订通过：L_{m'}避免导数歧义，p|N处用(h_x+1)x−6，费用明确为安全上界。

toric `cdt_odd_paired_large_prime_jet_rank_20261006.md` 实际全文无截断读J1–J23，SHA **39a0b6f80c4020602aff6dccded6d8da71ce0288b06a4ad86890be3265deb0f5**；作者确认以此指纹定稿，源码/JSON亦不改。

完整静态读取下列NEW数学源，全部execute/import/rerun0：

- root probe `cdt_odd_paired_dual_plucker_layers_20261006_probe.py`，SHA `4b020bc73c49a08a19f49f489bc719bc368d150ce830e3237cd032fd88c9aa1d`；JSON `53b243b65a9a3c7a1a07279b52debabd33bb2c5188ebcf943f3ff82bf60e72d3`。第一次合并raw输出JSON截断，随后compact重新显示全部105案例和全部Smith arrays成功，不将最初截断称已完成。
- root carry失败v1 `cdt_odd_paired_dual_plucker_carry_rate_20261006_verify.py`，SHA `ade489f98225ce61a9f58333464ce4d5e91ebfffe149358eb0e4df4b9321c3d5`；只读确认没有v1 JSON。
- distinct carry-v2源 `cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.py`，SHA `75dda9e61e2a6446e66d1b09502b860294e32e7532e0918f2d346c002e6fa1cf`；JSON `964137827f95314fe269bce3de6a4ddd631f3036b7398ef8507accd04b7bc725`，全部42formula comparisons、三tent、cap、exact费字段实际完整读。
- toric jet源 `cdt_odd_paired_large_prime_jet_rank_20261006_verify.py`，SHA `5c1df7cf287e6865561d22871f8f8ff61a03f1f090a25b9d04b0ad1c1516a17e`；JSON `190e0aea7a126438037709328576e779b8454c79c815067dc88d6c1b3ac5a99e`，全部43cases完整实际读。初次定位源码文件名错误仅产生只读FileNotFound，按rg正确路径补读，没有启动任何数学执行。

另本轮实际全文读冻结budget B1–B22（55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc）及已有JSON（7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b）的全部50 affine rows，用来直接核各gain窗口与entry cap，而不是借作者未显示的表。

## Q2. 全prime primitive complementary-minor与Smith层通过

Newton系数到1,…,2n evaluation的矩阵lowertriangular、diag1。每pair primitive(p_m,q_m)的gcd1，所以约束C是Z满射；它的kernel由完整饱和低块A给出。column wedge A及star(row wedge C)各自primitive、在同一有理一维空间，比例±1。因此D5没有隐藏格指数或Euclidean norm，确实对所有complementary minors成立。

所有非零S-minors必须包含high indices2n,…,3n−1；将low I与complement J相加，独立得到

\[
T_p=\sum_{i=0}^{3n-1}v_p(i!)-\min_{|J|=n}
\{v_p\det C_J+\sum_{j\in J}v_p(j!)\}.
\]

这正是D7，并非选一个方便basis去替代真实Plücker支持。

falling products j≥p在所有integer sites模p为0；首p列在完整residue sites上的evaluation矩阵可逆。p>2n时改用2n个distinct sites仍可逆，故D9的actual带权residue图rank成立。p>n时diag(j!) image包含pZ_p^{2n}，满射C给pZ_p^n⊂image(C^!)⊂Z_p^n；所有Smith层确为0/1，δ=n−rank图。p≤n只有第一层rank下界，稿件没有冒认全层。

## Q3. carry图的完整整数公式通过

n<p≤2n、p>8保证p²>8n。对k=lp+r，(k+N)!/k!的Wilson去p单位独算为

\[
(-1)^{h+c(r)}\frac{(l+h+c(r))!}{l!}
\frac{(r+e-c(r)p)!}{r!},\quad c(r)=1_{r+e\ge p}.
\]

所有阶乘指标<p；U1=(h+c+1)U0正确。h+c及(h+c+1)²−1为units，域p≥11不能省略。

H=2n−p−1为偶数。r0..H有两lifts，lower r<s=H−r各给两实际pairs；同carry的2×2块det为[(h+c+1)²−1]U0(r)U0(s)，different carry经primitive约除后都仅保留carry较大节点，rank1。centerloop的差为(h+c)U0(r)，rank1。外侧single pairs primitive保证rank1，互不干扰。

因此亏秩准确是r0..H/2−1中r<τ≤H−r的个数，即max(0,min(τ,H+1−τ,H/2))。这不是105有限例子的猜测。e0或H0边界也通过。

D18的floor例外亦准确：h变化当且仅当p|6n+1，actualδ0，此时(h_x+1)x−6=1/n，continuum d≤1/n；不能把此项错误换成h_x x−6。

## Q4. 两个paid tents和第三个隐藏cap通过

三tent的a=6/(h+1)、z=14/(2h+3)、b=8/(h+2)独算正确；第三条1−x/2只在峰点touch。原50行JSON明确在其支撑上raw依次是4x−12、−10、−2x−8。

前两段gain全为2d，面积分别6/91、8/165；h3时raw+2d≤−3x−6<−10，被cap完全遮住，gain必须0。故1718/15015是已付收益，不可以加未付第三面积1/45。

uniform O(1)的δ、LP与factorial误差按Σlogp付O(n)；原全prime界在其他window保持。实际形式系数signed ratio下界由PNT给D21，范围完整，包括小n原bound。费用是安全upper，未变成actual content equality。

## Q5. 大素数负节点核的实际carry1/2与parity通过

3n<p≤6n下degree<3n<p，Newton到monomial是GL(Z_p)，head interpolation满射，primitive pairs给actual A_Z⊗Z_p rank2n直和项。核的reduction与原characteristic-zero格相容。

p>4n时R0=6n+1−p，A=(t)R0在head上unit，d_z/p≡−A(z)直接由Wilson得出。P=AQ使条件成为Q(z)=Q(c−z)。head-root polynomial reflection-even，故odd Q必须被其整除，维数ceil(K/2)+max(0,floor((K−2n)/2))与J9相同。

3n<p<4n时H=2p−6n、J=c−H、A=(t)_{p−2n}、B=∏_{H}^{2n}(t−z)。独核leading factors：low val1为−AB，high val2为−2AB'；A(z)B'(z)≡−(z−H)!/(z−1)!的负号来自Wilson互补阶乘，不能略去。

H≤n时mixed high点J+1..2n先迫Q=ZR；overlap I的I'反射变号，条件为R odd modulo I，dim floor(D/2)+ceil((D−L)/2)=4n−p。H>n时high全mixed，Q=BR；central低点要求R even modulo其root polynomial，dim ceil(D/2)+max(0,floor((D−L)/2))。全部degree和可能空central set保留，得J14的两个max公式。没有把reduction unit权重偷换成unweighted evaluation。

## Q6. actual lifts、whole-X与jet polygon通过

reduction kernel basis可提升到actual paired Z_p basis，因为原格是直和项。weak值在unit-tail实际−p−ρ点带p，所有系数与导数integral。p^5U带p、p^5V integral；head全项≥p4、非unit-tail W带p3。故strong×weak≥p、weak×weak≥p²，对全部形式X系数成立。

M=diag(1^R,p^k)Ndiag(1^R,p^k)的N integral，所以r-minors≥2(r−R)^+，full determinant得到−10n+2k。它是polygon lower，不是exact Smith 0^R,2^k；mixed block可能给1,1。稿件明确没有用未知N unit去证nonzero。

finite verifier中的weak representatives只满足modp constraints；它们不是exact paired lifts。源码/正文都将这层差别写明，纸面lifting而非finite代码完成actual basis桥。p^4U的a项−8apH^(3)与p^5V的−24apH^(4)及target p^5X消失范围亦独核准确。

J18与原最后三段表逐段比较给gain=(3x−11)于11/3..4、(5−x)于4..5、其余0；面积1/6+1/2=2/3，无第三额外信用。PNT域和小prime/largeprime bound完整保留。

## Q7. 两个不相交window可以严格相加

两份稿使用同一S、same D_A(X)、same original B6/k3/s5和whole-X Gauss规范。root在n<p≤2n,p>8改进，toric在3n<p≤6n改进；window不交。逐prime分别取已证较强合法bound，其他prime保持冻结bound，得到一个实际signed ratio Q_n^{joint}，全n有D_A/Q_n^{joint}∈Z[X]。

两个paid PNT积分相加，精确安全fee为

\[
A_{joint}^{safe}=
\frac{1085983123}{24190320}-\frac{1718}{15015}-\frac23
=\frac{4624049789}{104824720}\in(44.112,44.113).
\]

这个接合只加两个已证明的不相交finite-place信用，没有再次约除Γ。它是安全费用upper，不能解读actual denominator lower或方法no-go。与另NEW镜像解析paper的>12.003572已证率相比，仍无strict margin。

## Q8. 一手来源和真实执行历史

本人实际完整读取本轮root新归档Bhargava2009 PDF1–4、7–11，共9页：`literature/bhargava2009_p_orderings_integer_valued_ultrametric_20261006.pdf`，SHA `cf66a3058ad9612019dcd9eda8bc1f26f9951c876b3e699d16bdd6b199c93f2e`，31归档页。本人数新下载0，未称全文31页。原件[AMS](https://www.ams.org/journals/jams/2009-22-04/S0894-0347-09-00638-9/S0894-0347-09-00638-9.pdf)。Theorem7是r-removed local divided-difference整值basis；PDF11的Theorem10需要全部factorial ideals非零principal才有global regular basis。这些条件准确支持D8的scope提醒，不替代D4–D21的实际Smith证明。

第一次文档extract显示用GBK而失败，随后`-X utf8`完整显示9页成功；这是PDF文本parser，不是数学producer。没有冒认同行额外primary页为本人已读。

root自有数学执行本轮3：probe成功1、carry-v1失败1（错误猜decimalwindow，已过formula/tent assertions但无JSON）、distinct-v2成功1。source保留、无重跑。toric自有1次成功43cases/15383 finitechecks。这些均为作者执行；审阅者数学执行0、旧/同行execute/import/rerun0、外部Lean0。

本审阅者另有自有镜像能量项目首次1次成功，与此同行独审执行0分开登记；上一轮failed-v1+distinct-v2两次仍在旧冻结收据，不重新计成本轮run。

## Q9. 审阅结论与未补范围

两份全尺度纸面命题及static source/certificate接口通过。已核重点包括真实格primitive complement、全部p>n Smith0/1、exact carry图亏秩、actual负节点核、paired exact lifts与whole-X p²、真实cap后的收益及不相交接合。没有重新计算全部作者105矩阵或运行其程序。

无限辅助Padé/unit、actual rational-target infinite nonzero及严格算术/解析margin仍未证明。没有新的ζ/L/Catalan无理性、线性无关性或Lean结论。本NEW联合独审完成全文自读后交root；旧冻结输入不修改。
