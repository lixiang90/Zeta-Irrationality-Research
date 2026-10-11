# 实际 weighted constraint 的全素数 CRT 整模型、镜像块与各层容量界

2026-10-06；root，NEW 数学稿，独审后冻结。旧439数学输入与全部旧/同行 producers 仅读，无 execute/import/rerun。本稿将经典整数插值/CRT用在原真实配对对象，不声称这些一般代数工具是新的文献定理，也不声称新的特殊值无理性。

## 1. 固定输入与真正需要计算的量

本轮实际完整读取冻结 dual稿0fb995、整数格稿5b7947和主报告末节。令 M=2n、k=m−1、k'=M−1−k，

\[
d_m=(m)_{6n+1},\quad g_m=\gcd(d_m,d_{m'}),\quad
p_m=d_m/g_m,\quad q_m=d_{m'}/g_m,
\qquad m'=M+1-m.
\tag{R1}
\]

这是冻结整数格的同一 primitive pair，等价于b_m/β_m、b_{m'}/β_m；共同(6n+1)!已取消。定义实际pair map L:Z_p^M→Z_p^n：

\[
(Lv)_m=q_m v_{m-1}-p_m v_{m'-1}.
\tag{R2}
\]

每pair gcd1且supports不交，L满射。weighted matrix C! 的j列是L作用在falling polynomial t_underlined_j的连续节点值，0≤j<M。冻结精确式为

\[
\delta_p=v_p I_n(C^!),\qquad
T_p=\sum_{i=0}^{3n-1}v_p(i!)-\delta_p.
\tag{R3}
\]

本稿给任意n、任意prime p的完整 integral normal form，包含ragged degree cutoffs和所有高Smith层；随后给p²>8n的额外容量下界。这里只改变同一矩阵的局部GL列坐标，不更换global saturated paired basis，不引入更强derivative-integral子环。

## 2. 全尺度 CRT 与精确 step-Newton 评价像

对每个非空residue r∈{0,…,p−1}，令

\[
L_r=\#\{0\le k<M:k\equiv r\pmod p\},\quad
Q_r(t)=\prod_{l=0}^{L_r-1}(t-r-lp).
\tag{R4}
\]

不同r,s的resultant是其所有root differences的乘积，全部为Z_p-units。因此Q_r、Q_s在Z_p[t]中comaximal：monic Sylvester matrix determinant是unit，解Bezout的系数属Z_p。由CRT

\[
Z_p[t]/\prod_rQ_r\simeq\bigoplus_r Z_p[t]/Q_r.
\tag{R5}
\]

两边都是rank M的free Z_p modules。各quotient的degree cutoff是<L_r，左边cutoff<M，故R5是GL_M(Z_p)的真正整模型，而非仅Q_p-vector space等价。

在第r个quotient用monic basis

\[
B_{r,j}(t)=\prod_{h=0}^{j-1}(t-r-hp),\quad0\le j<L_r.
\tag{R6}
\]

它到local monomials是unitriangular。CRT唯一给degree<M、Z_p-coefficient polynomials R_{r,j}，在第r个quotient余式是B_{r,j}，在其他quotient余式是0。全部R_{r,j}构成Z_p[t]_<M完整GL基。

在实际节点r+lp精确评价，不只模p，得到

\[
R_{r,j}(s+ap)=
\mathbf1_{s=r}\,p^j j!\binom{a}{j}.
\tag{R7}
\]

同一residue的binomial evaluation E_r=(binom(l,j))是lowertriangular diag1。因此原 integer-coefficient polynomial evaluation image准确是

\[
\bigoplus_r E_r\operatorname{diag}(p^j j!)_{j<L_r}Z_p^{L_r}.
\tag{R8}
\]

等价的完整 congruence 判据是：每个residue的finite differences Δ^j v_r(0)被p^j j!整除。这里不是普通integer-valued polynomials的任意函数像；它正是原C!所用的integer-coefficient polynomial像。原falling与monomial基也unitriangular，所以将R6/R5的坐标合并确实给C!右乘GL_M(Z_p)，没有未付格指数。

有限first-only探针可用显式系数

\[
U_{j,(r,a)}=\frac1{j!}\sum_{k=0}^j(-1)^{j-k}\binom jk
\mathbf1_{k\equiv r}\,p^a a!\binom{(k-r)/p}{a}.
\tag{R9}
\]

这是R_{r,a}的global falling展开。R5证明全部U entries属Z_p，且detU为unit；它并不是未经证明的数值插值分母取消。对j<M只用前M实际值，即R9精确恢复degree<M的polynomial。

## 3. 同一C!的完整镜像块 normal form

实际reflection k↦M−1−k在residues上诱导

\[
\sigma(r)=(M-1-r)\bmod p.
\tag{R10}
\]

非空clusters在σ下封闭。若r≠s=σ(r)，reflection给两个clusters之间bijection，故L_r=L_s=L，lift indices为l↦L−1−l。这个orbit有L个actual pair rows、2L个columns。可统一把其row orientation选成r侧在前；若原row反向，只差−1的unit。相应localmatrix为

\[
K_{l,(r,j)}=q_l\binom lj p^j j!,\qquad
K_{l,(s,j)}=-p_l\binom{L-1-l}{j}p^j j!,
\quad0\le l,j<L.
\tag{R11}
\]

q_l,p_l是真实primitive coefficients，非删carry后的unweighted数据。

若r=σ(r)，L_r=L必为偶数：实际reflection没有fixed整数节点，因为M−1为奇数。这个orbit有L/2 rows、L columns，lower lift0≤l<L/2的matrix为

\[
K_{l,j}=
\left(q_l\binom lj-p_l\binom{L-1-l}{j}\right)p^j j!,
\quad0\le j<L.
\tag{R12}
\]

p=2无loop，两个residues互换。p>M时每nonempty cluster只有1site，R11仍有效。经row/column permutations，C!的同一image精确成为这些K blocks的direct sum；每block去掉diag(p^j j!)后的H也是满射，因为pair map在对应sites上满射，E_r为GL。因此各block full row rank，Smith multiset是所有block Smith multisets的并集，δ_p是其index valuations之和。

**R13（精确全层接口）。** 只需保留这些≤2residue的finite matrices即可计算全部Smith层；没有仅保留modp而丢modp² primitive units，也没有假定每residue具有完整同一jet cutoff。若p/n≥ε，每block长度至多ceil(2/ε)，而n仍任意。这把大矩阵的高层问题准确压到固定大小actual blocks。

## 4. 真高层packet及递归Schur公式

由R8，模p^e的所有degree<M polynomial values准确是

\[
v_{r,l}=\sum_{j<L_r}p^j j!\binom lj a_{r,j}\pmod{p^e},
\quad a_{r,j}\in Z_p.
\tag{R14}
\]

j+v_p(j!)≥e的terms消失；其他自由系数的precision明确为e−j−v_p(j!)。这是全部层并含ragged boundaries的精确packet。

特别p≤n时全部p个L_r≥2，模p²有独立x_r∈Z/p²、y_r∈F_p，

\[
v_{r,l}=x_r+pl y_r\pmod{p²}.
\tag{R15}
\]

degree<M没有在此丢掉derivative方向；p>n则有L_r=1的ragged clusters，不能借R15给它们补不存在的y_r。

为避免把第一层rank冒充全部Smith，设任一actual blockK有m rows，rank modp为r。选r阶unitminor，Z_p行列消元给diag(I_r,S)，S integral且全部entries被p整除。写K_next=S/p；这是实际Schur remainder，保留输入的下一层precision。

\[
\{\alpha_i(K)\}=\{0^r\}\cup\{1+\alpha_i(K_{next})\},\qquad
\delta(K)=(m-r)+\delta(K_{next}).
\tag{R16}
\]

证明unit pivot block可用integral inverses完全清除cross blocks，余块modp为0，因为r是全部modp rank。除p仅使余下nonzero invariant factors各减1。迭代的每层corank之和正是δ，不是先猜一个higher-jet matrix再加rank。

由于H满射、diag weights像包含p^{w_max}Z_p^{#cols}，其中w_max=(L−1)+v_p((L−1)!)，每block所有Smith valuations≤w_max。故R16有限步终止。R13/R16为准确计算与全尺度证明提供接口，本稿不自行算出每个window的闭式全部layers。

## 5. 全prime基准费用与真实 mixed-carry 高层容量

任何m阶minor的valuation至少为该block最便宜m个column weights之和，因为H entries integral。令w_j=j+v_p(j!)严格递增、W_u=Σ_{j<u}w_j。

offcenter L=2u时baseline=2W_u，L=2u+1时baseline=2W_u+w_u；loop L=2u时baseline=W_u。把全部orbits加和，恰是

\[
\boxed{\delta_p\ge\delta_p^0:=\sum_{i=0}^{n-1}v_p(i!).}
\tag{R17}
\]

这里的精确加和不靠样本。写M=ap+b，0≤b<p，各L是a+1（b个）或a（p−b个）。对odd p，若a=2u，则b偶、loop在length2u侧，sum=pW_u+(b/2)w_u；若a=2u+1，则b奇、loop在length2u+2侧，sum=pW_u+((p+b)/2)w_u。两式分别与n=up+b/2、n=up+(p+b)/2的first-n factorial valuations一致，因为v_p((lp+r)!)=l+v_p(l!)=w_l。若p>M，所有weights0，结论亦成立；p=2只有两lengthn clusters，其cheapest n weights正好是firstn global weights。

现在设p²>8n。令N=6n+1=hp+e，0≤e<p、τ=p−e。对sitek=r+lp，Legendre给

\[
v_p(d_{k+1})=h+c(r),\qquad c(r)=\mathbf1_{r\ge\tau}.
\tag{R18}
\]

在不同carry的offcenter orbit，一侧全部primitive coefficients为unit，另一侧全部恰带p。故强侧column weights是j，弱侧是j+1；这里j!为unit，因为L≤ceil(2n/p)<p。最便宜L个weights的和为floor(L²/4)，较原baseline floor((L−1)²/4)多floor(L/2)。无需任何更高Schur-unit假设，就得到

\[
\boxed{\delta_p\ge\delta_p^0+
\sum_{\substack{\text{offcenter orbits}\mathcal O\\c(r)\ne c(\sigma(r))}}
\left\lfloor\frac{L_{\mathcal O}}2\right\rfloor,
\qquad p²>8n.}
\tag{R19}
\]

这是已支付primitive coefficients的真实higher-column容量下界；不是exact Smith equality。

还可将其完全写成整数计数。仍写M=ap+b，则reflection在inner interval0..b−1与outer intervalb..p−1分别封闭。mixed orbit counts准确为

\[
M_{in}=\max(0,\min(\tau,b-\tau)),\quad
M_{out}=\max(0,\min(\tau-b,p-\tau)).
\tag{R20}
\]

它们来自lower endpoint<τ≤upper endpoint的计数；centerloop不可能mixed。R19的extra正是

\[
\left\lfloor\frac{a+1}2\right\rfloor M_{in}
+\left\lfloor\frac a2\right\rfloor M_{out}.
\tag{R21}
\]

对n/2<p≤n，所有lengths2,3,4，R21化为M_mixed+M_length4；p>n的length1/2情况则回到冻结第一层carry公式。R21覆盖更小large primes，但费用要继续与原whole-X Λ−2T和entry cap取max后才能兑现，不能裸记R21的积分。

## 6. 文献、机制验证与仍未完成的目标

正常verified TLS新增归档[Miller–Stanton原件](../literature/miller_stanton2017_orthogonal_polynomials_smith_author_20261006.pdf)，作者版本日期March31,2017、16页，SHA0bf017cf67796bba8d5a00fc00e398ae6fb5b252e9e6f8c98a221e5913303a45。root实际完整读PDF1–4及15–16共6页。[作者PDF](https://www-users.cse.umn.edu/~stant001/PAPERS/StantonMillerFinal.pdf)第15页Theorem7在q=1专门给等步长Vandermonde的factorial Smith；本稿用monicstepNewton独立证明该局部事实。Theorems1/8的Hankel公式先给定满足指定三项递推的monic OP functional，并不替本项目建立actual χ-corrected critical normality。真实p37首moment0已排除直接用其L(1)=1归一化的perfect scalar route。未称全文16页或被引书籍已读。

自有NEW机制探针 `cdt_odd_paired_residue_crt_integral_model_20261006_verify.py` 首次且唯一执行一次，退出码0；source SHA aa4086403985b8b9eab6bec640e538a91f73a819f651a50adaae6bd000ad3f98。独立从R1/R7/R9构造实际矩阵，检查GL局部变化、mirror directsum的全部Smith和R17/R19。覆盖n1..12的所有p≤2n共63cases，9378个精确矩阵身份entries，25个p²>8n容量cases；包含p2等高factorial layers，不扩auxiliary prime表。只验证有限机制，不证明本稿全尺度CRT。输出存在guard禁止重跑；具体一次执行历史与输出SHA在NEWreceipt准确记录，旧/同行producer执行0。

本稿尚未给全prime足够便宜费用、无限auxiliary simultaneous units、actual determinant无限nonzero、same-object strict margin或新的ζ/L/Catalan定理。下一步是利用真实小blocks求更高layer closed forms及其cap后费用；所有new source与peer review分别归档，不改旧冻结输入。
