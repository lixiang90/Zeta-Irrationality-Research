# 曲率保证的平方提升与低次数二阶行

日期：2026-10-06。新输入是全素数的 modp² square lift：完整 excellent quotient G_p 的 generic double-root 部分可以提升为平方。它将已有两层算子的安全次数从6p+13降至3p+20。本文只证明该具体输入及原格可用性；不声明新的数值无理性定理，不要求 branch factor在提升后仍整除Δ，也不修改此前冻结稿。

## 1. 已证对象与全 polynomial 曲率关系

沿用 [Frobenius 稿](cdt_odd_level20_frobenius_20261006.md)、[Hasse 稿](cdt_odd_level20_hasse_20261006.md) 和 [第三层审查](cdt_odd_level20_third_layer_20261006.md)。p≥7、p∤20。Φ 是真实 eta gauge，其完整 norm coefficient满足

\[
G=G_p\in Z[t],\qquad\deg G\le3p,\qquad
\Phi(t)/\Phi(s(t))\equiv G\pmod{p^3},\quad s=t(q(t)^p).
\]

设 ϑ=t d/dt、g_s=(1−t)√Δ、h=ϑlogg_s、q_proj=t²Q。第三层推导已证明，若 z=h+ϑlogG，则 F=2ϑz+z²+4q_proj≡0modp²。置

\[
J=(1-t)\Delta,\quad h=H_J/J,\qquad
\mathcal T=4q_{proj}+2\vartheta h+h^2
=\frac{-8t(18t^4-36t^3+28t^2-10t+1)}J.
\]

将 F 乘G²，得

\[
\boxed{\mathscr R(G)=
2G\vartheta^2G-(\vartheta G)^2+2hG\vartheta G+
\mathcal T G^2\equiv0\pmod{p^2}.} \tag{1}
\]

清分母J后的 numerator 是完整 polynomial，所有 coefficients被p²整除。依据是全形式级数 Frobenius 比值和 Riccati identity，非任何有限 jet 的猜测：J(0)=G(0)modp=1使 rational-to-formal 映射在原点 injective modulo p²。

## 2. Hasse 除子与 double roots

令 P=Gmodp=P_p。Hasse simple-zero 输入给 degree P=3(p−1)，其非分歧根重数2、分歧根重数1；无 cusp 根。取

\[
H=\gcd(P,P')\ \text{monic},\qquad B=P/H^2.
\]

H 为 generic double roots 的 squarefree polynomial，B 的根是 supersingular Fricke branch，B squarefree且 B|Δ。令 degH=h₀、degB=b。则

\[
2h_0+b=3(p-1),\quad b\le4,
\quad\gcd(H,BJt)=\gcd(H,H')=1. \tag{2}
\]

这里H是 polynomial，与真实函数H_±区别明确。以下 square lift完全是有理整数 gauge Φ 的性质；只在随后应用 source packet 时需要假定未知周期有理。

## 3. 曲率排除 generic double roots 的一阶分裂

取任意 coefficientwise integer lifts B₀、H₀，H₀monic，degrees为b、h₀。P₀=B₀H₀²与G reduction相同，因而

\[
G=P_0+pE,\qquad E\in Z[t],\quad\deg E\le3p.
\]

所有 \(\mathscr R(P_0)\) 的项都含 H₀²。清J后记完整integer numerator为\(\mathscr R_J\)。因为G≡P₀modp且\(\mathscr R_J(G)\in p^2Z[t]\)，还得到\(\mathscr R_J(P_0)\in pZ[t]\)。monic H₀保证其divisibility是p-saturated：若\(pW=H_0^2V\)，reduction在F_p[t]整域中使V∈pZ[t]，于是W仍被H₀²整除。因此\(\mathscr R_J(P_0)/p\) reduction被H²整除。现在将 \(\mathscr R(P_0+pE)\) 展开、除p并在H的根上取 residue才得到合法的一阶约束：P₀和ϑP₀为零，而

\[
\vartheta^2P_0\equiv2B(\vartheta H)^2\pmod H.
\]

因此(1)给

\[
\boxed{4B(\vartheta H)^2\overline E\equiv0\pmod H.} \tag{3}
\]

若统一清分母J，左边多一个J；由(2)它仍是unit。ϑH=tH′，而H squarefree且没有t=0根，所以4B(ϑH)²在 F_p[t]/(H) 中可逆。得到真正的全 polynomial 结论

\[
\boxed{H\mid\overline E.} \tag{4}
\]

该 residue 步骤合法地在全 polynomial equation 上进行。它不把仅 n<p² 的 target packet方程外推到 generic roots。

## 4. 有界 branch 部分的显式 square lift

写 \(\overline E=H E_1\)。取

\[
H_1\equiv E_1/(2B)\pmod H,\quad\deg H_1<h_0,
\qquad B_1=(E_1-2BH_1)/H.
\]

两条均属于 F_p[t]。因 degE≤3p，

\[
\deg B_1\le3p-2h_0=b+3\le7.
\]

将H₁、B₁任意lift到整数，并置

\[
\eta=H_0+pH_1,\qquad\beta=B_0+pB_1.
\]

直接展开得到

\[
\boxed{G\equiv\beta\eta^2\pmod{p^2},
\quad\deg\eta=h_0,\quad\deg\beta\le b+3\le7.} \tag{5}
\]

P(0)=1保证β、η在原点均为p-adic units。没有要求β在modp²下仍为Δ的因子；也没有要求Gmodp²保持degree3p−3。原来的安全degree3p已经足够。

## 5. 将二阶行次数降至3p+20

暂省略目标±，令 R=N√C、C_o为另一个C，k=R/g_s。旧 connection为

\[
a_0=\vartheta\log(RG),\quad
a_1=\vartheta\log k
=\vartheta N/N+t/(1-t)-\tfrac12\vartheta C_o/C_o.
\]

以(5)定义

\[
a_{0,new}=\vartheta N/N+\tfrac12\vartheta C/C+
              \vartheta\beta/\beta+2\vartheta\eta/\eta.
\]

所有原点分母为unit，故 \(a_{0,new}\equiv a_0\pmod{p^2}\)。在 n<p² 的真实完整前缀，Y=p³H是integral；因此用new替换∇₀只改变p²项，ϑ和∇₁都保持它。旧二层关系遂给

\[
(\vartheta-a_1)(\vartheta-a_{0,new})Y\equiv0
\pmod{p^2,t^{p^2}}. \tag{6}
\]

取

\[
D_{0,new}=NC\beta\eta,\quad
M_{0,new}=D_{0,new}a_{0,new},\quad
D_1=N(1-t)C_o,\quad M_1=D_1a_1.
\]

它们是p-integral polynomial coefficients；degrees≤h₀+b+7和5。与冻结两层稿相同的 operator identity给

\[
L_{2,new}=(D_1D_{0,new}\vartheta-D_1\vartheta D_{0,new}-D_{0,new}M_1)
                 (D_{0,new}\vartheta-M_{0,new}).
\]

该行等于 \(D_1D_{0,new}^2(\vartheta-a_1)(\vartheta-a_{0,new})\)，所以在完整前缀输出属于p²。三个 polynomial coefficients的次数安全界为

\[
\boxed{\delta_{2,new}\le2h_0+2b+19
       =3p+b+16\le3p+20.} \tag{7}
\]

最高 coordinate是D₁D₀,new²；modp非零，原点常数为unit。故其 polynomial multiples在原 **target source blocks** 中 reduction-independent，constant block取0。它是原格可用的第二层方向；无需更换源格或把raw constant方向记成免费收益。

## 6. Smith 输入及限定范围

在前次的相同D-degree原格、prime window √N<p和同一完整leading cutoff中，新行给

\[
k_{2,new}\ge(D-3p-19)_+.
\]

旧第一层两方向保持原样。加权Smith仍按 \(#a_i\ge1\) 与 \(#a_i\ge2\) 分别计数，允许方向重叠；第二层的新增主项从D²/12提升到D²/6，总相应原格 determinant 主项为5D²/6。这个具体degree改进仍须在主任务的完整source/height账本上使用，不能改写成适用于任意balanced tensor的通用成本。

本稿不补第三层 primitive direction。此前第三层稿已明确 raw coefficients与实际Econstant block的差别；平方提升是利用其曲率关系降低已有二层行的degree，具有不同的算术作用。

## 7. 精确证书与审阅范围

[新脚本](cdt_odd_level20_square_lift_20261006_verify.py)、[新证书](cdt_odd_level20_square_lift_20261006_verify.json)读取冻结107check certificate中的完整Gmodp³。对固定 p=7,11,13，以完整 polynomial coefficients（不作有限jet猜测）核验：曲率numerator modp²、linearization residue、乘子modH为unit、H|E、βη² lift、全 polynomial logderivative cross关系及degree/unit界。

共51项精确检查，包括上述p-saturated divisibility。该脚本不重新生成源packet，也不将三个有限素数当作全素数证明；全素数依据是 §§1–5。有限样本的βdegree实际仍为b，二阶行degree界为31、47、53；本稿不用此现象改善统一3p+20界。
