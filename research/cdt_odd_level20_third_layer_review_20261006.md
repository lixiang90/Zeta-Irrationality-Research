# 自然第三 connection：Bol 恒等式、forcing 与 primitive 层的独立审核

日期：2026-10-06。本稿只读审核 [第三层新稿 §§2–6](cdt_odd_level20_third_layer_20261006.md)，不修改冻结 [Frobenius 输入](cdt_odd_level20_frobenius_20261006.md)、producer或前轮全局账。结论：第三次链式作用的模p³消除成立；消去实际 Bol 方程与 constant 方向后，target row的 content恰p²，primitive除法后该论证只提供第一层。完整 rank4的 raw forcing coefficient本身没有共同p²，必须与 target quotient分清。

## 1. 三次组合及 Euler Bol 规范

沿新稿用ϑ=t∂ₜ，a=ϑlogk、h=ϑlogg_s、ℓ=ϑlogΦ、z_S=h+ℓ、z=h+ϑlogG_p。已证 excellent比值给

\[
z\equiv z_S-pb\ell(s)\pmod{p^3},\qquad
\vartheta\log b=pbz_S(s)-z_S,
\quad\vartheta s=psb.
\tag{T1}
\]

前轮第二层 output为 p²kbg_s(s)[W₂(s)+h(s)W₁(s)]。第三 connection为ϑ−a+z，其作用于 prefactor的额外 logarithmic coefficient是

\[
\vartheta\log b+pb h(s)+z
 \equiv 2pb h(s)\pmod{p^3}.
\]

内部函数的每次ϑ derivative也带p。因此整个第三次组合确实在p³中；Euler derivative保留t^{p²}理想，没有 prefix shift错误。

operator product必须包含对z的微分，展开得

\[
(\vartheta+z)\vartheta(\vartheta-z)
 =\vartheta^3-(2\vartheta z+z^2)\vartheta
  -(\vartheta^2z+z\vartheta z)
 =\vartheta^3-V\vartheta-\tfrac12\vartheta V.
\tag{T2}
\]

[完整模型 §4](cdt_odd_level20_model_20261006.md)给√S满足Y''+t^{-1}Y'+QY=0，故ϑ²√S+t²Q√S=0。q_proj=t²Q的定义及 Riccati identity

\[
2\vartheta z_S+z_S^2+4q_{proj}=0
\tag{T3}
\]

与新稿一致。这里不能使用去掉t^{-1}Y'后另一个普通∂规范的 projective connection。其 Sym²经固定 gauge k的真实算子是

\[
\mathcal B=k[\vartheta^3+4q_{proj}\vartheta
                    +2\vartheta q_{proj}]k^{-1},
\qquad \mathcal BH=t^3U.
\tag{T4}
\]

从(T2)减(T4)，令F=V+4q_proj，得到

\[
\nabla_2\nabla_1\nabla_0-\mathcal B
 =-F\vartheta+(aF-\tfrac12\vartheta F).
\tag{T5}
\]

这是消去三阶导数后的一阶 target row，不是新的三阶独立 function。

## 2. 为什么共同恰有p²

由(T1)及ϑℓ(s)=pb(ϑℓ)(s)，直接计算

\[
F\equiv-p^2b^2\{\ell(s)^2+2h(s)\ell(s)
                    +2(\vartheta\ell)(s)\}\pmod{p^3}.
\]

对s变量用(T3)，得到

\[
F\equiv p^2b^2\mathcal T(s),\quad
\mathcal T=4q_{proj}+2\vartheta h+h^2.
\tag{T6}
\]

把模型Q₈与Δ代入，本次也独立以 exact rational simplification核得

\[
\mathcal T(t)=
\frac{-8t(18t^4-36t^3+28t^2-10t+1)}{(1-t)\Delta(t)}.
\tag{T7}
\]

s以t^p起首、b(0)=1，所以F/p² modp的t^p coefficient是−8，对每个p≥7非零。这是完整形式级数结论。对 J=(1−t)Δ、D=N(JG_p)³，清分母得到

\[
P_1=-DF,\qquad P_0=D(aF-\tfrac12\vartheta F).
\]

由于D(0)是p-adic unit，formal到polynomial的整性检测无损：P₀、P₁所有coefficients都在p²中，而P₁/p²的t^p coefficient是8modp。故 target row共同 content恰p²，而不只是“至少p²”。D同时清forcing，degree≤9p+17；P₀、P₁也有这一安全界。

primitive除法只保证

\[
(P_0/p^2)Y+(P_1/p^2)\vartheta Y\equiv0\pmod p,
\qquad Y=p^3H.
\tag{T8}
\]

模p，ϑlog(F/p²)=−2z_S，所以 normalized row满足

\[
\bar P_0+\bar P_1\vartheta\log A=0,
\qquad\vartheta\log A=a+z_S.
\]

它属于已有 Hasse一阶 rational annihilator模。本文没有证明其在另一个输入下绝不可能有第二层；它只指出此模p³链条约去共同p²后本身保证的层数是1。

## 3. 完整 rank4的forcing不能免费忽略

在 unscaled coefficient module O_{K,𝔭}[t]_{≤D}^{⊕4}、actual tuple(1,H,ϑH,ϑ²H)上，消去ϑ³H的完整 physical coefficient row为

\[
(Dt^3U,\ P_0,\ P_1,\ 0).
\tag{T9}
\]

第一coefficient不能说也含共同p²。模型式(4)给t³U的t coefficient为

\[
-\frac15+\frac r4=\frac{5r-4}{20},\qquad
\operatorname{Norm}_{K/\mathbf Q}= -\frac{109}{400}.
\tag{T10}
\]

因为D(0)=G_p(0)³≡1modp³，这也是Dt³U的t coefficient。对p≠109的好素数它在各𝔭处是unit；p=109不影响“raw full row没有普遍共同p²”这一结论。不能以(T6)的target quotient信息改写整个raw row。

raw scaled evaluation是p³eval，所以任何integral constant polynomial Q₀已满足p³Q₀∈p³F。减去(T9)中的 pure constant direction后，target row才共同p²，且modp reduction为零。因此(T9)在第三层的非零modp image至多来自已有constant directions，不能算作新的target第三层image。

## 4. CDT原格坐标中的同一结论

上一节的raw basis与CDT原source的unit basis不同。在已证明的p>√N、p≤D窗口，bare rank4 source constant block是ℓ_D^{-3}O_{K,𝔭}[t]，rank7 constant block是(ℓ_Dℓ_{2D}ℓ_{4D})^{-1}O_{K,𝔭}[t]；二者的 denominator valuation都恰3。

所以同一physical constant polynomial Dt³U在**原 integral source坐标**中表示为p³u·Dt³U，其中u是unit。该坐标在p³中，而target coordinates在p²中：完整source向量的content因而恰p²。除掉p²后constant coordinate仍在p中、target至少一个coordinate是unit；其Ψimage只由现有论证保证在p中，仍只是S₁。

这不是与(T10)矛盾：一个说physical coefficient，另一个说带LCM缩放的 integral source coordinate。不能把raw pure constant的S₃ image当作CDT原格的免费新维数，也不能只看target coefficient就说raw整行共同p²。

若使用已清pole的实际tuple(1,Δ²H,Δ²ϑH,Δ²ϑ²H)，target row的output共同乘Δ²；forcing physical coefficient成为Δ²Dt³U。其degree可能额外增加固定8，故在有限degree模板中应保留此fixed offset；它不改变任何D²主项。target content和primitive阈值保持不变。

## 5. 审阅边界

第三层新稿§§2–6的限定结论通过独立审核，以上额外解释是raw module与CDT原格之间的接口澄清。本文没有重跑作者的54checkproducer；本次独立执行只核exact rational curvature identity(T7)及forcing norm(T10)，其全素数依据是(T1)–(T8)的代数推导。

没有新增 primitive第三层Smith方向，没有修改已得到的两层全局收益，没有排除不同 connection、进一步square lifts、primitive saturation或tensor方法。冻结Frobenius、第三层producer和既有bridge均保持原样。
