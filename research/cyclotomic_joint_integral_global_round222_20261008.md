# 第222轮：同源双悬挂的联合整格与最高层窗口

2026-10-08。NEW 有限纸面进展。支付一个实际完整源的联合top flag、全素数安全整子格及精确指数比较。完整五行在可单射的连续jet矩形上没有这一窗口的联合收益；实际三行子源仍有小的真实联合收益，但尚未付清可进入holonomy的费用。本稿不把row分母当最优source-lattice下界，不否定不同函数源或精细能量方案。数学程序0。

## 1. 实际源及被冻结的门槛

本轮实际FULL读取221最终算术稿全部七节/P1–P17：13880 B，SHA256 `ec00ff4c6dd4d76b61d1093234e0525a4d164ffdc66d34ac37c4fcda1e56c28e`；FULL读取221最终全图稿全部七节/Q1–Q13：7527 B，SHA256 `41916916956130d288497d90793d3cdbd5648dfa6fe750e2f5999bddb368783d`。

沿同一初始芽，令G=g∈Q为拟反证假设，c_g>0固定整数且c_gg∈Z，

\[
a_n=\frac{(-1)^n}{2n+1},\quad b_n=\frac{(-1)^n}{(2n+1)^2},\quad
H_n=\sum_{j<n}\frac{(-1)^j}{(2j+1)^2},
\]
\[
f_e=2c_ge,\quad (f_e)_0=0,\quad (f_e)_n=c_g(H_n-g)/n\ (n\ge1),
\quad f_o=c_go,\quad(f_o)_n=c_g(H_n-g)/(2n+1).
\tag{J1}
\]

完整五行F=(1,a,b,f_e,f_o)有已付Q(t)连接与实际函数秩5；实际e/o初始t=1补点保留G目标。共用H_n给(2n+1)o_n=2ne_n（n≥1），但这不是删行的Q(t)关系。

写L_D=Z[t]≤D^5、m=5(D+1)，T_N(P)为sum_i P_iF_i的完整0,...,N Taylor向量。q_M是不超过M的正奇整数lcm。全部素数幂的安全fallback是

\[
M_N=q_{2N+1}^2d_N,\qquad M_N T_N(L_D)\subset Z^{N+1}.
\tag{J2}
\]

221全图稿给任何实际e或o共同亚纯图的ell=log|psi'(0)|<7/2；普通差值能量J≥ell。含1,e,o的子列表也继承此界，这是解析恢复a,b，不是免费增行。

## 2. 精确最高层联合残数lemma

设odd prime p满足N/2<p≤N、p²>2N+1、p不除6c_g。置

\[
h=(p-1)/2,\qquad\kappa=(3p-1)/2=p+h.
\]

**Lemma.** 对完整Z_p源L_D⊗Z_p，p³T_N已整，且其mod p映射恰为

\[
\Phi_p(P)=c_g\chi_4(p)
\left(t^pP_e+\tfrac13t^\kappa P_o\right)\pmod{(p,t^{N+1})}.
\tag{J3}
\]

证明：全部内层奇指标k≤2N−1小于4p，且p²>2N+1，故H_n最多有p深度二。a、b最高深度一、二，p³后均为零。e的外层n只能在n=p含p；H_p内唯一奇p倍数是p，故p³(f_e)_p≡c_gχ4(p)。其余e系数至多深度二。o的外层2n+1可能是p或3p；前者内层还没有p，不能有深度三；后者内层只有p、不含3p，故p³(f_o)_kappa≡c_gχ4(p)/3。其余o系数至多深度二。固定g在这些top残数中消失，p不除6c_g保证两个常数是unit。乘P_i只将全部实际系数移位，没有删输出列。这支付J3。

## 3. 完整源kernel、局部剪切与未付的下一层

令I_p=[p,p+D]∩[0,N]、J_p=[kappa,kappa+D]∩[0,N]，空区间的长度为0。J3的像是对应单项式位置的完整span，因此

\[
r_p=|I_p\cup J_p|,\quad K_p=\ker\Phi_p,\quad
[L_D\otimes Z_p:K_p]=p^{r_p}.
\tag{J4}
\]

分行top约束K_p^sep要求两项分别为零，其index为p^(|I_p|+|J_p|)。所以真正联合收益是

\[
[K_p:K_p^{sep}]=p^{\lambda_p},\qquad
\lambda_p=|I_p\cap J_p|
=\max\{0,\min(D-h,N-\kappa)+1\}.
\tag{J5}
\]

这也有实际整剪切：对每个0≤l≤min(D−h,N−kappa)，将o列t^lf_o替换成

\[
3t^lf_o-t^{h+l}f_e.
\tag{J6}
\]

两个源次数都≤D；该完整源变换的det是3^lambda_p，为p-unit。J3给p²乘J6的全部0,...,N jets在Z_p中。每个重叠方向确实降低一层p分母，不是形式Hasse kernel、单行抵消或离散拟合。

最优整源Lambda_p={P:T_N(P)∈Z_p^(N+1)}仍包含更多问题。精确三层过滤为L→K_p={p²T_N整}→{pT_N整}→Lambda_p。后两步分别在当前整域上取p²T_N、pT_N的mod p kernel，因此v_p[L:Lambda_p]=r_p+r_mid+r_low。J4只付r_p，未求r_mid/r_low；不能将它或J1的逐行Den当完整最优index。

## 4. 真正全素数的有限整模型

取S_N为§2全部好素数，定义整数源的CRT交Gamma_joint={P∈L_D:每个p∈S_N的Phi_p(P)=0}，分行版Gamma_sep同理。各mod p条件独立，CRT给

\[
[L_D:\Gamma_{joint}]=\prod_{p\in S_N}p^{r_p},\quad
[\Gamma_{joint}:\Gamma_{sep}]=\prod_{p\in S_N}p^{\lambda_p}.
\]

令B_N=M_N/prod_(p∈S_N)p。好素数在M_N中恰有深度3；Gamma_joint使其输出深度至多2。其余素数及全部高幂保留J2，特别2、3与p|c_g没有被漏掉。因此

\[
\Lambda_{paid}=B_N\Gamma_{joint}\subset L_D,
\quad T_N(\Lambda_{paid})\subset Z^{N+1},
\]
\[
\log[L_D:\Lambda_{paid}]
=m\log B_N+\sum_{p\in S_N}r_p\log p.
\tag{J7}
\]

这是保留全部函数方向和全部输出的真正有限整子格。相同B_N下，相比分行模型的精确source-index节省是sum lambda_p log p。最优Lambda_int可能更大；J7是安全上界，不是最优下界。local unit剪切也不自动支付全局CRT基的实处高度或CDT balanced determinant估计，故不把J7的指数直接称为tau。

## 5. 完整五行没有此窗口收益；三行是明确未排除的对象

若完整五行连续jet映射要单射，行数至少为m，即N≥5D+4；这是必要维数条件，不声称该N已经充分。此时p>N/2给h>D，两个窗口不重叠：

\[
N\ge5D+4\quad\Longrightarrow\quad\lambda_p=0\ (p\in S_N).
\tag{J8}
\]

所以本highest-layer联合lemma不能改善完整五行的这个大素数窗口。N=3D的短矩形确有sum lambda_p log p=(1/16+o(1))D²：p∈(3D/2,2D]时lambda_p=D−p/2+O(1)，PNT给积分∫_(3/2)^2(1−x/2)dx=1/16。但该矩形只有3D+1输出，少于5(D+1)列，不能借它声称完整五行determinant非零或降低holonomy费用。

不同的实际direct-CDT子源F_3=(1,f_e,f_o)有函数秩3，三个函数各自holonomic；它不是rank5微分connection的免费降秩，其微分闭包恢复a,b，秩仍5。取完整Z[t]≤D^3时，J3–J7原样成立而m=3(D+1)。对N=3D+c、固定c≥2，同一真实top-layer节省仍为1/16 D²；outputcount的必要条件N≥3D+2成立，但实际zero estimate/非零jet证书仍未付。没有声称0,...,N jet单射，更没有将这有限节省转成无限CDT slopes。

该三行现有arbitrary-array是(0,0,0)、(2,2,1)、(2,2,2/3)。前两width2列都可同时达到16/9，第三列非负，故这张已付表tau_flatflat≥32/9>7/2，仍没有正gate。**此下界仅属该array，不是F_3最优联合格下界。** 新J7给可研究的更大整数源，但后续层、所有prime-power总体成本及实处接口尚未支付，不能把1/16直接从32/9减掉。

## 6. Holonomy接口与当前应停止的事项

同源新模型首先须给合法CDT类型或重证完整算术determinant estimate，取得tau_joint<7/2才可能有正费用差。对于普通J商，本源m=5还必须tau_joint<14/5，三行m=3必须tau_joint<7/3，四行必须tau_joint<21/8，因为J≥ell且ell<7/2，strict quotient<m强制tau<(m−1)ell/m。原x四行的普通rho cap同理要求tau<9/8。当前已付表均不满足这些条件。

最小下一步lemma现在具体为：对实际F_3的完整多项式源，支付r_mid/r_low及p≤N/2多极点窗口和全部高幂的总index；证明所用Taylor矩形单射，连同CRT/源基实处高度，将其转成上述门槛内的有效holonomy成本。只证明某row分母变小、某有限prime flag或某短矩形节省，均不能替代它。

J8停止的是完整五行此最高层窗口；它没有否定更小实际函数源、低素数联合层或别的合法整模型。CDT更精细能量/多图版本的分子还需另付，普通J的必要阈值未被挪给它们。普通同源导数调参应停止；结构性全源arith与实际branch改变仍可研究。没有新数值结论。

## 7. 实际阅读与执行范围

除§1两份冻结稿的FULL阅读，本轮实际重读fixed v2 printed/PDF pp122–123完整Theorem8.0.1、arbitrary-array定义及Remark8.0.6；不是FULL读218页。源PDF为4517169 B、SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。复用冻结221实际函数秩/全幂fallback及全图证明，不假定新的numerical theorem。J1–J8全部为独立有限纸笔推导；PNT仅用于§5标明的leading term。

数学程序/CAS/矩阵执行/泛搜/prime或parameter扫描/PSLQ/数值积分/Lean/Git均0。工具仅FULL文档读取、PDF选页文本、metadata/hash及本NEW文件保存；未改旧稿、main或manifest，未重复archive。保存后将实际FULL作者复读最终稿，外部登记bytes/hash；作者复读不替代独审。
