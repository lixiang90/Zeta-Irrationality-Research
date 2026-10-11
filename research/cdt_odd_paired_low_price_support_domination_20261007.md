# 低定价 supported 转移的精确包络与真实 partial threshold

2026-10-07，NEW，quarter_actual_rank。504 项冻结数学输入、旧/同行 producer 与所有旧收据只读，不 execute/import/rerun。原 S、B6/k3/s5、degree<3n、rank2n、sources 与 whole-X D_A(X) 不变。本轮纸证优先，不扩辅助单位素数表，不执行新数学程序。

## L1. 实际对象与两个新结论

沿用冻结 e483 的真实整数值饱和配对格及完整 S。设 p>5、p≤2n、p²>8n，写
\[
2n=ap+r_2,\quad3n=Qp+R,\quad6n=hp+r_6,
\quad V=p-r_2,\quad u=\min(r_6+1,V),\quad d=2n.
\]
unit residues U={0,…,u−1}，inner reflection σρ=V−1−ρ。令
\[
b=(2u-V)_+,\quad \ell=b\bmod2,\quad
P=(b-\ell)/2,\quad e=u-b,
\]
\[
f=a\min(u,V/2)=ae+aP+a\ell/2,\qquad
L=e+P+\ell=\left\lceil\min(u,V/2)\right\rceil.
\tag{L1}
\]
e 为 unit→nonunit 强迫 head-zero 的 residue数，P 为 unit/unit offcenter mirror pairs数，ℓ 为 fixed unit residue loop数。f 是实际 independent primitive rows 数，不能把它当作任意 selected minor 均能扣除的信用。

**新增结论一：** λ∈[0,2]、η∈[0,2] 的完整 low-price status-transfer 家族有可计算的精确候选包络，而且逐有限n被既证真实 unit-tail DND界支配；上轮 T18 及 all-a 分数gain均不产生新增paid区间。

**新增结论二：** locally forced sector 可先真实因式分解，再把 selected-row threshold从Q降为Q−a。这是任意支撑上的严格rank改进，包含r≤Q的partial观察，仍保留真实raggedtop。它在一个明确支撑给严格更小cap，但其低定价粗包络仍被DND支配。没有由此排除更强 allocation-correlated 优化。

## L2. 精确整数与固定 loop 的边界

2n=ap+r2、p odd给r2≡a mod2。V odd强迫a even，所以若ℓ1则a为至少2的偶数。特别a1必Veven，不存在a1且fixedloop的反例参数。

U∩σU是一个以reflection中心对称的interval，长b；有P个offcenter pairs和ℓ个fixed residue。其余e个unitresidues的mirror在nonunit内，每个有a条实际forced head-value relations。故L1中的f确为整数。亦可直接由冻结 e483 U16的primitive pair计数得到。

因此对所有本题实际参数都有
\[
\boxed{L=\lceil f/a\rceil\le f.}
\tag{L2}
\]
最短证明：a≥1、f是非负整数，f/a≤f，所以ceil(f/a)≤f。若要区分loop，a1时L=f；a≥2时min(u,V/2)是非负半整数，ceil它≤2倍它≤a倍它。没有把half-loop修正免费扔入O(1)。

## L3. 所选支撑的真实低定价 gap

冻结35ed P7/P10明确指定selected counts rρ及B={ρ:rρ>Q}，C=B∩U：
\[
f_B=a|C\setminus\sigma U|+(a/2)|C\cap\sigma C|,
\]
\[
v_p^{Gauss}D_A\ge-10n+\min_{\sum r=d}
\left[\sum_\rho F_\rho(r_\rho)-2\min(R,|B|)+2f_B\right],
\]
\[
F_\rho(r)=w_\rho r+4(r-2q_\rho)_++2(r-Q)_+,
\quad0\le r\le2q_\rho+2.
\tag{L3}
\]
actual node-block nonzero minors的左右counts相同，所以两侧f_B准确相同。局部ψ GL和split primitive格使此界作用于原S，不是普通coefficient替代格；derivative-only不需恢复constant。固定有理sources仍先清同一固定分母。

令0≤λ,η≤2，
\[
z=(\lambda+\eta-2)_+.
\]
unitρ有w0、qρ=h、h≥2Q，pricedminimum准确为
\[
\alpha_U=\min_r\{F_U(r)-\lambda r-\eta1_{r>Q}\}
=-\lambda Q-z.
\tag{L4}
\]
r≤Q时minimum−λQ；r>Q时先在r=Q+1取值−λQ+2−λ−η，之后直到2h slope2−λ≥0，超过2h又增加4。故notbig unitblock相对α_U至少多付z。nonunit w≥2的pricedminimum是0：r0可达；r≤Q其余≥0，r>Q有2(r−Q)−η≥0，head费用非负。

## L4. 最佳 unit-status 图信用，而非免费扣全 f

设s=|U\B|。对固定z∈[0,2]，只放松total row-resource与其它node细节，unit big/notbig状态的精确minimum是
\[
\boxed{\min_{C\subset U}\{z|U\setminus C|+2f_B(C)\}=zL.}
\tag{L5}
\]
逐实际graph component证明：forced单residue，small付z、big付2a，minimumz；offcenter unitpair，bothsmall付2z、onebig付z、bothbig付2a，minimumz；fixedloop，small付z、big付a，minimumz，因为a even≥2。不同components不交，分别取最小即zL。这只是status relaxation的exactminimum，不声称这些最小状态同时满足Σr=d或实际Gram正常。

令K=|B|，−2min(R,K)+ηK≥−(2−η)R。因此L3–L5给全尺度whole-X候选
\[
\boxed{v_p^{Gauss}D_A(X)\ge C_{\lambda,\eta}:=
-10n+\lambda(d-Qu)-(2-\eta)R-z(u-L).}
\tag{L6}
\]
它保留真实source degree cutoff、raggedtop和匹配side；只是对allocation更弱的lowerbound。

尤其λ2η2时z2，
\[
C_{2,2}=-6n-2(Q+1)u+2L.
\tag{L7}
\]
这严格包括all-a合法收益2f/a=2min(u,V/2)，且补清fixedloop的有限整数ceiling。a1时L=f，正是上轮T18的合法候选。

## L5. 整个 λ0/1/2 家族的闭包络与零新增覆盖

记
\[
k_*=d-Qu-\min(R,u)+f,
\quad A_0=d-Qu-R,\quad A_1=d-Qu-u+L.
\]
若λ>0且η≤2−λ，则z0，L6至多−10n+λA0。若η≥2−λ，令β=z/λ∈[0,1]，则
\[
C_{\lambda,\eta}=-10n+
\lambda\{(1-\beta)A_0+\beta A_1\}.
\tag{L8}
\]
λ0的candidate≤−10n。由u−L=P得精确候选包络
\[
\boxed{\sup_{0\le\lambda,\eta\le2}C_{\lambda,\eta}
=-10n+2[d-Qu-\min(R,P)]_+.}
\tag{L9}
\]
最值由λ0η2，或λ2η0/λ2η2之一给出，故并未只检查整数λ/η的有限表。

实际e483 U6已证明
\[
G_{DND}=-10n+2[k_*]_+\le v_p^{Gauss}D_A(X).
\tag{L10}
\]
A0≤k*，因为min(R,u)≤R；A1≤k*，因为min(R,u)≤u且L≤f。故
\[
\boxed{C_{\lambda,\eta}\le G_{DND}
\quad\text{对每个本题有限n,p和全部 }0\le\lambda,\eta\le2.}
\tag{L11}
\]
不必只说O(1)主率被覆盖：有限整数参数与fixedloop均已精确比较。k*若负，candidate仍≤−10n，正部保持正确。

504预算逐prime保留了这份实际DND与上轮所有合法界，再共同max新的27个λ≥3supported candidates。因此L11给本家族**所有places零新增**，当然n² paidgain亦为0。无须重算旧producer或建立一份“零面积”finitecertificate。当前安全费用仍为冻结T17的
\[
800671681093752110193539327219/19860629178118281482813083200.
\tag{L12}
\]
这是明确限制，非actual方法no-go，也不把safe费用说成actual最小整数分母下界。

## L6. 更早可见的 actual forced-sector 因式分解

令E=U\σU，|E|=e。每个ρ∈E的actual localΦρ在a个真实positivehead ψ-values处为0；它们互异，unit/nonunit primitive carry方向已在冻结e483 U13–U16严证。令
\[
H_\rho(Y)=\prod_{m\in\mathrm{head}(\rho)}(Y-\psi(m)),
\quad\deg H_\rho=a\quad\text{且monic}.
\]
则模p实际系数必满足
\[
\boxed{\Phi_\rho=H_\rho\Psi_\rho,\qquad\deg\Psi_\rho\le Q-a.}
\tag{L13}
\]
把local ordinary monomial最高系数记τρ。Hmonic使Ψ最高系数仍是**同一个**τρ，不是另加自由top；τρ仍来自原degree<R low-digit polynomial的restriction。固定top后forcedρ底Q−a系数自由，unforcedρ底Q系数自由。这里描述的是含actualA像的明确ambient constrained coefficient source，未声称actual全局pair数据在任意支撑都可延拓。

定义新的bottom维数
\[
t_\rho=Q-a1_{\rho\in E},\quad
B'=\{\rho:r_\rho>t_\rho\},\quad
C'=B'\cap(U\cap\sigma U),\quad
j_{B'}=(a/2)|C'\cap\sigma C'|.
\]
discard小blocks后，big系数源维数Σ_(B')tρ+min(R,|B'|)。余下unit/unit内部primitivepairs仍独立：它们在unforcedresidues，底Q≥a能在a个headsites任意插值，固定真实top；forcedsector的headzeros已经通过L13付过，不再重复扣除。因此
\[
\boxed{\operatorname{rank}_{\mathbf F_p}Y_I|_A
\le\sum_\rho\min(r_\rho,t_\rho)+\min(R,|B'|)-j_{B'}.}
\tag{L14}
\]
这是新的all-scale partial-threshold lemma。它允许selected rows r≤Q也真实看见forced loss，不假设selectedjets injective，也没有局部GL的实处费用免费。

L14 pointwise不弱于旧35ed P7。旧B中的forcedresidue对应“Q减a”与旧扣a完全相抵；内部pair big条件没改。新增加的big forcedresidues只可能tρ<rρ≤Q。令此集合N，则newcap−oldcap准确为
\[
-\sum_{\rho\in N}(r_\rho-t_\rho)
+\min(R,|B'|)-\min(R,|B|)
\le-\sum_{\rho\in N}(r_\rho-t_\rho-1)\le0.
\tag{L15}
\]
所以没有把sharedtop重复扣掉。真实有限示例：n33、p19满足domain，a3/Q5/R4/V10/u9，E={0}。取actual value rows j0,…,65，residuecounts r0..8=4、r9..18=3。旧P7 cap66；新t0=2、B'={0}、jB'0，L14给cap65。这里是严格cap改进，未声明实际rank恰65或whole-X费用新增。

同一matchednodecounts接口使L14可进入whole-X模型：将L3中的2(r−Q)+改为2(r−tρ)+，最后big count用B'、配对信用用jB'。这是新的合法support model，未解其exactallocationminimum，也未把上述单支撑cap改进直接积分当预算收益。

## L7. 新 partial threshold 的低定价仍被覆盖

对L14的新model，低price minimum在forcedunit上是−λ(Q−a)−z，在其它unit上是−λQ−z；nonunit为0。forcedhead约束已因式分解，不再计graph信用；内部P个pairs与ℓ个loops仍各有minimumz，给z(P+ℓ)。候选成为
\[
\widetilde C_{\lambda,\eta}
=-10n+\lambda(d-Qu+ae)-(2-\eta)R-z(e+P).
\tag{L16}
\]
和L5同样取连续λ/η包络得
\[
\sup\widetilde C_{\lambda,\eta}
=-10n+2[d-Qu+ae-\min(R,e+P)]_+.
\tag{L17}
\]
其方括号不超过k*：相差
\[
aP+a\ell/2+\min(R,e+P)-\min(R,u)
\ge(a-1)P+(a/2-1)\ell\ge0,
\tag{L18}
\]
用u=e+2P+ℓ；loop存在时a even≥2。因此新的partialsource确实改善selectedcap，但完整**低定价粗转移**仍没有任何有限place新增，也没有whole-X paidgain。λ≥3只用coarse minima时forcedfactor贡献2ae，与上轮已经支付的full forced credit相同；本文不据此声称更强allocationcorrelation也无收益。

## L8. 能推进什么、不能排除什么

已证：完整低price status家族的精确graph收益、连续λ/η包络、finite-n DND支配、actual forcedfactor/更早threshold/raggedtop/pair信用及严格selectedcap示例。没有选择新的n-dependent格或增source。

尚未排除：保留Σr=d与真实rowtypes的allocation相关优化；多个threshold的sharedtop费用与mirrorgraph同时求解；partial观察functionals同实际pairrowspace的交；真实node0/更高jet层。L11/L18只排除已经写出的coarse低price转移家族，不是全Ωsupport、所有λ2构造或actual方法的no-go。要新增费用必须超过当前**whole-X共同max**，而非只比旧ambientcap强。

无限original target非零和strictmargin仍缺，没有新ζ/L/Catalan无理性、线性无关性或Lean定理。没有新的辅助单位素数表。

## L9. 实际只读范围和执行史

本轮actual FULLread：e483 unitsector U1–U10/equationsU1–U21；35ed selectedsupport P1–P8/P1–P15；3a4b supportedtransfer T1–T9/T1–T18，输出无截断。实际SHA分别为

- `e4830013ad948599c4e1bb76113aeed3a8b6df23b32a9d575052cd97d7f6fac8`；
- `35ed9d8e9b3f1f5ea70c4e742d1e26c262d6d529823987bdc0478128fdd35880`；
- `3a4b58d6d0fbad83e13268e4b30d73030caf8461c99a4db0acb5681ba1625334`。

冻结上轮successful JSON `cdt_odd_paired_supported_weighted_dual_transfer_20261006_verify.json`，SHAa37ce3e552a6ded9efaa48f07ca268ec207000d4a165cc4e072ba52dc31f1694：本轮全syntaxparse，全部metadata、98条saved affine records所有字段按49/49 compact两批实际读，均无截断。它仅作字面504预算基线；没有重算213arrangementcells或旧27candidate/producer。L11逐整数参数直接证明零新增，不靠finitefit或端点数值表。

本轮own mathematical producer0；旧/同行execute/import/rerun0；externalLean0；新PDF/HTML/外部源码下载0、新primaryPDF阅读页0。该证明是实际factor/interpolation、finitegraph、piecewiseprice与精确整数比较，自足无需泛套外部文献。本文NEW候选尚未冻结，待root/peer独审；暂不写finalreceipt，不修改504任何旧文件。
