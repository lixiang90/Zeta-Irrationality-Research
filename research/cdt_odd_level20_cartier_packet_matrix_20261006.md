# level20 六个正规积分的最高 packet 与完整 Hecke 矩阵

日期：2026-10-06。本稿新建，不改冻结稿。正结论是六个实际积分的深度一统一身份：它们的最高 packet 由固定六维模形式空间上的完整 Hecke 矩阵控制。没有扫描素数，没有假设 nonordinary 密度，没有 modp²/³ 提升或新的数值无理性定理。

## 1. 固定真实积分与局部窗口

沿用 [核稿](cdt_odd_level20_cartier_kernel_20261006.md)、[实际 cohomology 稿](cdt_odd_level20_cartier_cohomology_20261006.md) 和 [全素数 Hecke 空间](cdt_odd_level20_hecke_space_20261006.md)。本稿 δ=−1,+1 表示原 A₋、A₊，其 Fricke eigenvalue 是 δ；δ 不等于 χ(p)。定义

\[
 D_\delta=(1-t)N_\delta C_\delta,\quad
 Q_j^\delta=t^j/D_\delta,\quad
 B_j^\delta=Q_j^\delta A_\delta S,\quad0\le j\le5.
\tag{P1}
\]

Bⱼ 是对应 Fricke eigenspace 的完整六维 holomorphic weight4、characterχ₅基，且5Bⱼ从−qʲ开始，全部 q coefficients 在 O_K。本文真实源固定 δ=−1，六个正规积分为

\[
 I_j=\int_0^t\{Q_j^-(v)H_-(v)-Q_j^-(0)H_-(0)\}\,dv/v,
 \qquad I_j(0)=0.
\tag{P2}
\]

先按原反证路线假设 L(3,χ₅)∈Q，使所有 H 原点系数属于 K。固定一个好 place 𝔭|p，p∤20且不除固定周期分母。以下 integral prefix 在 n<p²；若另记长度 N，则为 p<N≤p²、按 t^N 截断。n=N−1 是最后一个 coefficient。原点 residue 已完整减去。

令 ε=χ(p)、target δ′=−ε。原 f₋ 在最高 packet 后变为 f^{(ε)}：ε=1 取 f₋，ε=−1 取 f₊。以

\[
 f_{p,\varepsilon}=f^{(\varepsilon)}\pmod{t^p}
\]

表示这个**实际** Taylor 芽的 degree<p 截断，其 constant 为0。它在该 slow-variable 前缀 p-integral。原真实 packet 给

\[
 p^3H_-\equiv A_-\,f_{p,\varepsilon}(t^p)
 \pmod{\mathfrak p,t^{p^2}}.
\tag{P3}
\]

没有把 genuine Frobenius lift 错换成整个 characteristic-zero q(t)^p；P3 是已经证明的最高层、modp 的 coordinate-compatible 身份。

## 2. 对六个积分逐系数抽取

取 Yⱼ=p³Qⱼ⁻H₋、Zⱼ=p⁴Iⱼ。Qⱼ⁻ 的全部 t coefficients integral，故两者在上述 prefix integral。P3 给

\[
 \overline Y_j=Q_j^-A_-\,f_{p,\varepsilon}(t^p)
 \quad\bmod t^{p^2}.
\tag{P4}
\]

对 n>0，正规积分精确满足 [tⁿ]Zⱼ=(p/n)[tⁿ]Yⱼ。若 p∤n，此 coefficient mod𝔭为0；若 n=pm、1≤m<p，则为 [t^(pm)]Yⱼ/m。constant 取0。因此有唯一 Jₚ,ⱼ∈tk[t]/tᵖ，使

\[
 \overline Z_j=J_{p,j}(t^p)\bmod t^{p^2},
 \qquad \vartheta J_{p,j}
 =\mathfrak C_t(Q_j^-A_-)\,f_{p,\varepsilon}\bmod t^p,
\tag{P5}
\]

其中 ϑ=t∂t，𝔠 是 k-linear relative Cartier extraction。抽取乘积规则

\[
 \mathfrak C_t(g(t)h(t^p))=\mathfrak C_t(g(t))h(t)
\]

在本识别下直接由 coefficients 成立。inert residue k=Fₚ²时，也不在该式额外施加一次 coefficient Frobenius：absolute Cartier 的 p-root 已由 relative/twisted linearization 处理。q(t)、t(q)、S 的 Fₚ coefficients 保证坐标相容。

## 3. 全六矩阵公式与真实 period carrier

用 columns 表示源 basis images：

\[
 T_pB_j^- =\sum_{i=0}^5 M_{p,ij}B_i^{\delta'},
 \qquad M_p\in M_6(O_K),\quad\delta'=-\varepsilon.
\tag{P6}
\]

这个 integral matrix 由完整 holomorphic空间和三角 q基定义，对全部 p∤20存在；不是由几个 p 的数值拟合定义。weight4 的算术 Fourier 身份给 UₚBⱼ≡TₚBⱼmod𝔭，额外项含χ(p)p³。对一形式 QⱼA₋dt/t= Bⱼ⁻dq/q 的 Cartier 坐标相容性给

\[
 \mathfrak C_t(Q_j^-A_-)S
 =\mathfrak C_q(B_j^-)
 \equiv T_pB_j^-\pmod{\mathfrak p}.
\]

S(0)=1，故相除并代入 P6，得到**完整 formal modp 身份**

\[
 \boxed{\mathfrak C_t(Q_j^-A_-)
   =\sum_i\overline M_{p,ij}Q_i^{\delta'}A_{\delta'}\pmod{\mathfrak p}.}
\tag{P7}
\]

定义 target 的完整实际 primitive

\[
 \Xi_i^{Af,\delta'}=\int_0^t Q_i^{\delta'}(v)A_{\delta'}(v)
                   f^{(\varepsilon)}(v)\,dv/v,\qquad\Xi_i(0)=0.
\tag{P8}
\]

其 degree<p 前缀 integral；因为 f(0)=0不含 logt。ϑ 在 tk[t]/tᵖ 上 invertible，因此 P5–P8 给唯一解

\[
 \boxed{J_{p,j}=\sum_i\overline M_{p,ij}
                 \overline\Xi_i^{Af,\delta'}\pmod{t^p},}
\tag{P9}
\]

即最高 fast-variable packet

\[
 \boxed{p^4 I_j(t)\equiv
     \sum_i\overline M_{p,ij}
          \overline\Xi_i^{Af,\delta'}(t^p)
       \pmod{\mathfrak p,t^{p^2}}.}
\tag{P10}
\]

零积分常数是 P9 的必要规范；仅比导数而漏常数不够。

target primitive 的真实分解仍是

\[
 \boxed{\Xi_i^{Af,\delta'}
 =J_{Q_i^{\delta'},H_{\delta'}}
  +\varepsilon\Theta J_{Q_i^{\delta'},A_{\delta'}}.}
\tag{P11}
\]

Hδ′=Aδ′(f^{(ε)}−εΘ)。P11 未删 carrier；第二项不能下降到此前 coarse G叶。P9 是 actual Taylor 前缀的算术身份，并没有把 Ξ 本身重新声明成共同 full-disk 函数。

P9/P10覆盖整个六维 basis；源 B₀⁻,…,B₅⁻ 的完整 Hecke orbit一般不是只有原单个 F₋的三个方向。不能将“单个 F₋核空间每sign至多3维”误套为整个 Mₚ 的 rank≤3。

## 4. 深度一 constant 核与 primitive 的准确范围

对显式 local integral-prefix evaluation

\[
 E_{p,N}:O_{K,\mathfrak p}^6\longrightarrow
          O_{K,\mathfrak p}[t]/(t^N),
 \quad c\longmapsto p^4\sum_jc_jI_j,
 \quad p<N\le p^2,
\tag{P12}
\]

P10显示：若 \(\bar c\in\ker\bar M_p\)，则 Eₚ,N(c)∈𝔭·target lattice。选择 kerMₚ 的 k-basis并任取 integral lifts，有 degree0、source primitive 的 S1 rows；每行至少一个 coefficient是 unit，不是除去共同p-content以前的零行。它们在 source residue space 独立，数目为 dimₖkerMₚ。

这是 **P12 的明确本地六列 evaluation** 的深度一结论。该核未必等于 evaluation 的全核：slow-prefix target Ξ 可有额外 finite-jet关系；P9不排除这些。也没有无条件把这 dimkerM个数加进原 CDT 完整整格的 Smith预算：e=1积分 species、整格坐标、其它 blocks 已有 baselines、p-dependent coefficient heights、degree windows与determinantal counting仍须同一接口核准。

已证 actual cohomology 独立性保证 I₀,…,I₅不是 characteristic-zero 假独立或 rational exact 类；同 source closed模块rank10，加入P10实际rank19。它不保证每个有限N、每个𝔭的 packet columns独立，不能由实际秩直接推出模p²或模p³提升。

### 4.1 仅由完整前缀长度产生的大素数核

P5 给 Zⱼmod𝔭只有 t^(pm)项，1≤m≤rₚ,N:=floor((N−1)/p)。因此 P12 的 residue map \(\overline E_{p,N}\) 有

\[
 \operatorname{rank}\overline E_{p,N}\le\min(6,r_{p,N}),\qquad
 \dim\ker\overline E_{p,N}\ge(6-r_{p,N})_+.
\tag{P12a}
\]

这是 full chosen prefix 的 constant-coefficient 核，不要求 nonordinary。设 Vₚ,N 是取 target Ξ 前rₚ,N个positive coefficients的矩阵，则

\[
 \overline E_{p,N}=V_{p,N}\overline M_p,\qquad
 \dim\ker\overline E_{p,N}
 =\dim\ker\overline M_p+
   \operatorname{rank}\overline M_p-
   \operatorname{rank}(V_{p,N}\overline M_p).
\tag{P12b}
\]

所以两种核可能重叠；不能把 dimkerM 与 (6−r)直接相加。仅由维数可安全得下界 max(dimkerM,6−r)。

取同一 full prefix N、同一个 constant residue kernel 的 basis。对每个 d=0,…,D，将其source coefficient vectors同时乘 tᵈ，仍给 mod𝔭为零的 degree≤D行；source polynomial-coordinate中这些(D+1)份独立，因为它们构成 kernel basis与monomial basis的tensor product。这只是这个完整本地 evaluation 的 shift lemma，没有对既有selected-row格或global Smith收益做认领。

P12a强迫非零核的窗口为 p>(N−1)/6，属于大素数窗口。例如若为rank19系统选N≥19(D+1)，该输入通常从p约19D/6才出现，不能不经新接口就算进当前较小的 prime-cutoff预算。本文不据此给 asymptotic γ、density或免费第三层。

## 5. 三个 Hecke 块怎样约束深度一核

全素数 Hecke 稿的 decomposition 是 E（每sign3维）、O（每sign2维）、N（每sign1维）。固定 T₃² eigenvalues 分别676、−4、−76，projectors有固定分母。为单纯以这些固定 projectors 与 T₃-isomorphisms 在 residue上读 block ranks，可先省略有限集合

\[
 p\in\{2,3,5,13,17,19,47\},
\tag{P13}
\]

以及实际规范的固定坏素数。这里13与19只是保证选定 T₃ 在 E/N 间的 isomorphism为unit；projector denominators包含2、3、5、17、47。P6–P10本身不因P13而失去其它好p，只是那些p不能免费采用此 residue直和账本。

在该 fixed-good范围，χ(p)=1时各块为 scalar×I；χ(p)=−1时各块为 scalar×T₃。Eisenstein块的系数明确是

\[
 a_E(p)=1+p^3\quad(\varepsilon=1),\qquad
 b_E(p)=(p^3-1)/26\quad(\varepsilon=-1).
\tag{P14}
\]

均 mod𝔭非零，因此 E 的三维 block是unit。定义 αO(p)、αN(p) 为该规范下 old/new块的 scalar（I或T₃前的系数）；从完整 integral matrix及 fixed unit block bases，它们在好place integral。此时

\[
 \boxed{\dim\ker\overline M_p
 =2\,\mathbf1_{\alpha_O(p)\equiv0}
    +\mathbf1_{\alpha_N(p)\equiv0}.}
\tag{P15}
\]

因此若相应块在该p退化，可给P12中2个或1个 primitive degree0 S1方向；E块不会产生这样的核。P15是条件结论。本稿不称这些p有正密度、无穷多个或某个固定valuation，不用几个 prime值证明任何全p nonordinary断言。

depth1只说明某些完整 packet受whole Hecke matrix控制。下一需要真正证明的输入是与完整 CDT source匹配的 higher-prefix或 higher-modulus elimination；目前仍未给出这样的提升。

## 6. 核验范围

本稿没有新 numerical producer、prime扫描或重跑旧证书。P5的逐系数积分、P7的relative Cartier坐标相容性、P9的zero-constant uniqueness与P12的primitive kernel均由正文给出。依赖的最高packet、完整holomorphic基、全pHecke分解、共同leaf及actualrank分别引用已冻结/已审前稿，不把其固定57check数据当作本稿全p逻辑的替代。

low_period_closure 实际只读独审 §§1–4.1通过：逐 coefficient抽取、inert relative Cartier、P7坐标相容性、zero-constant primitive、整个 n<p²前缀、native六列的primitive S1、完整前缀support维数、V M分解与monomial shifts均重推成立；同时认可§5在固定unitprojectors与已证whole Hecke分解输入下的条件核数及不推密度的范围。未运行producer，也未在该次审阅重复证明whole Hecke谱分解。其指出的P1两处排版已修正，数学主体保持同版。
