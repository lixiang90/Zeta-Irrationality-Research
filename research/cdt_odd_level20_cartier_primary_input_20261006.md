# Cartier / Hecke / Fricke 的正规化原始输入

日期：2026-10-06。本稿只核小而精确的文献输入及直接一般矩阵推导，不改既有冻结稿、不搜索参数。不宣称新增Smith方向、周期无理性或rank预算成功。新原始PDF见[独立清单](../literature/manifest_cdt_odd_cartier_primary_20261006.json)。

## 1. 三个原始定位与一份复用原件

1. Andreea Mocanu，*Atkin–Lehner Theory of Γ₁(N)-Modular Forms*，[作者原PDF](https://andreeamocanu.github.io/atkin-lehner-theory.pdf)，10页。PDF/印刷第2页给Mk(Γ,χ)的定义和扩展slash；第5页Definition4.2给Tp double-coset representatives；第6页Proposition4.1明确double coset保持全部holomorphic Mk；第7页Proposition4.2证明中明确给全部Mk(Γ₀(N),χ)的Fourier公式，并定位到Diamond–Shurman Proposition5.2.2(ii)。本稿不把只在cuspidal space定义的Petersson adjoint当成一般Mk交换式的证明。
2. Jared Weinstein，*Lecture Notes: An Invitation to Modular Forms*，[波士顿大学官方原PDF](https://math.bu.edu/people/jsweinst/Teaching/MA843/ModFormsIntro.pdf)，15页，首页日期2011-10-03。PDF/印刷第15页§4.4给Fricke作用及非平凡角色的新形式eigenvalue转为χ(p)^−1 a_p。这只作正规化交叉证据；下面全部Mk版本是直接推导，而非把newform陈述扩大适用范围。
3. William A. Stein，*Explicitly Computing Modular Forms*，[作者官方原快照](https://wstein.org/msri06/refs/stein-book-on-modular-forms.pdf)，278页，PDF metadata creation2006-07-30。当前实际标题是*Explicitly Computing Modular Forms*，不能误标成另一个较新的PDF版本。PDF第171–172页/印刷157–158页§9.1给Mk的diamond角色分解；PDF第175页/印刷161页Proposition9.10证明中给角色Tp的系数公式。该页在解释cusp空间，故全Mk适用还由上面的double-coset公式保障。
4. 复用 Nicholas Katz，*p-adic Properties of Modular Schemes and Modular Forms*，已存[katz1973_padic_modular_forms.pdf](../literature/katz1973_padic_modular_forms.pdf)。PDF第47页/原书印刷115页Ka-47，Lemma3.6.1证明给relative Cartier局部提取公式，目标是Ω^(p)。新清单只记录复用，不覆盖原文件。

## 2. 固定标准，Hecke 的整性与 U_p 比较

固定det^(k/2) slash，χ(-1)=(-1)^k，N≥1，p∤N。置

\[
 (W_N f)(\tau)=N^{-k/2}\tau^{-k}f(-1/(N\tau)),
\tag{C1}
\]

\[
 (T_p^\chi f)(\tau)=\chi(p)p^{k-1}f(p\tau)
                 +\frac1p\sum_{a=0}^{p-1}f((\tau+a)/p).
\tag{C2}
\]

这是与上述primary Fourier公式一致的integral Hecke正规化。Mocanu的GL+ slash使用det^(k−1)；其double-coset sum已经给(C2)，不能在其Tp上额外乘p^(k/2−1)。采用本稿det^(k/2) slash书写double coset时，才需对应的Hecke normalization factor。将W_N乘任意固定非零scalar不改变后面的交换公式。W_N²=(-1)^k；本项目k=4时是1。

若f=∑a_nq^n，则(C2)逐系数给

\[
 T_p^\chi f=\sum_{n\ge0}
       [a_{pn}+\chi(p)p^{k-1}a_{n/p}]q^n,
 \qquad a_{n/p}=0\ (p\nmid n).
\tag{C3}
\]

因此Tp保持任何含角色值的系数ring的integral q-expansion；这里不需要从Hecke eigenforms的代数整数性间接推。double-coset定义保证结果仍为同level/weight/character的holomorphic form。令U_p f=∑a_pn q^n、V_p f=f(q^p)，则

\[
 T_p^\chi=U_p+\chi(p)p^{k-1}V_p.
\tag{C4}
\]

本项目k=4时，U_p f≡Tp f mod𝔭³作为完整q级数，特别mod𝔭；但U_p f在characteristic zero并非据此自动是level N form。holomorphic fixed-level输入应使用Tp f，再用(C4)取同余。

## 3. 一般 Mk 的 Fricke 交换式：直接矩阵证明

W_N把χ变为χ^−1：对γ∈Γ₀(N)，w_Nγw_N^−1的lower-right entry是γ的upper-left entry，χ(a)=χ(d)^−1。对所有Mk(Γ₀(N),χ)，不是仅newform，有

\[
 \boxed{T_p^{\chi^{-1}}W_N
       =\chi(p)^{-1}W_NT_p^\chi,\qquad
 W_NT_p^\chi=\chi(p)T_p^{\chi^{-1}}W_N.}
\tag{C5}
\]

推导如下。展开(C2)作用到(C1)。a=0项与f(pτ)项分别直接对应。对a∈{1,…,p−1}，选唯一b∈{1,…,p−1}使Nab≡−1modp，取

\[
 \gamma_a=\begin{pmatrix}
 p&-b\\-Na&(1+Nab)/p
 \end{pmatrix}\in\Gamma_0(N).
\tag{C6}
\]

其det=1，lower-right d≡p^−1modN。令z_b=(−1/(Nτ)+b)/p，则

\[
 \gamma_a z_b=-p/[N(\tau+a)],\qquad
 c z_b+d=(\tau+a)/(p\tau).
\]

模形式转化律给

\[
 f(-p/[N(\tau+a)])
   =\chi(p)^{-1}((\tau+a)/(p\tau))^k f(z_b).
\]

代入p^−1 N^−k/2((τ+a)/p)^−k的prefactor，恰成为χ(p)^−1 p^−1 N^−k/2 τ^−k f(z_b)。a↔b是bijection，故得到(C5)。此证明只用转化律与primary(C2)，无需cuspidality、newness、diagonalizability或Petersson adjoint。

特别N=20、χ=χ₅二次时χ^−1=χ，得到root需要的W₂₀Tp=χ₅(p)TpW₂₀。k=4的(C1)与加入i^k的另一常用Fricke规范相同。

## 4. 固定除子商的下降：必须匹配 Fricke 符号

设F∈Mk(Γ₀(N),χ)，W_NF=λF。由(C5)，

\[
 W_N(T_pF)=\chi(p)\lambda\,T_pF.
\tag{C7}
\]

本项目已有同weight/character、对应两种Fricke eigenvalue的固定denominator forms；若选D_ε满足W_ND_ε=χ₅(p)λD_ε，则(T_pF)/D_ε是Γ₀(N)与Fricke都不变的meromorphic function。只有在χ₅(p)=1时可不加检查就用原F作denominator；χ₅(p)=−1时(T_pF)/F反不变，不能称K(t)。当前conjugate构造选择A_εS以匹配这一符号。

在项目已证X₀(20)/W₂₀ genus0、t为其Hauptmodul的前提下，上述不变商属于C(t)。TpF在全部cusps与内部holomorphic，故商的poles仅来自固定D_ε的zeros、pole orders受其固定zero divisor控制，与p无关。两个ε的固定divisor可并成一个公共bound。这是固定除子输入；不是从有限q前缀推出全局无其它poles。

域与整性可用项目的显式固定clearing divisor处理，避免未经核实的field Galois作用。若固定h_ε(t)∈K[t]清商的finite poles并给固定degree M，则h_ε(t)(TpF)/D_ε为degree≤M的polynomial。TpF及D_ε的q展式在K，t=q+…在K且局部可逆，故有限t-jet直接恢复这些polynomial coefficients∈K。若q-expansions p-integral且D_ε leading coefficient在好place为unit，固定q-jet matrix的非零det只增加有限坏primes；其inverse保证这些coefficients在其余places integral。这个最后步骤必须给实际h_ε/M/nonzerojetdet，不能只由holomorphic或genus0推出O_K[t]。root已另独推实际固定divisor/jetdet接口；本稿只说明所需条件。

## 5. Cartier 的两种记法不能混用

Katz Lemma3.6.1 的relative Cartier写作

\[
 C_{\rm rel}(a_nX^n dX)=
 \begin{cases}
 0,&p\nmid n+1,\\
 a_n(X^{(n+1)/p-1}dX)^{(p)},&p\mid n+1.
 \end{cases}
\tag{C8}
\]

目标为Frobenius-twisted differential module。以q作local parameter，relative系数提取可写

\[
 C_{\rm rel}\bigl(\sum_n a_nq^n dq/q\bigr)
   =\sum_n a_{pn}(q^n dq/q)^{(p)}.
\tag{C9}
\]

如果把目标与原curve over a perfect field识别为absolute Cartier，则是p^−1-semilinear，右边系数为a_pn^(1/p)。k=O_K/𝔭不是总等于F_p；本项目K=Q(√5)的inert primes有k=F_p²，必须保留coefficients Frobenius（√5会变号）。线性的U_p extraction可以用relative target，或明确另作coefficient Frobenius linearization，不能把两种C无说明地混同。

项目S满足dt/t=S dq/q，故formal source A dt/t=AS dq/q。如果AS确已是holomorphic weight4 χ₅且q-integral，(C3)–(C5)给其Cartier提取的固定weight、符号转换和完整mod𝔭³的Hecke lift。A、S的实际身份、Cartier坐标change、混合primitive row与new Smith阈值仍由新actual Cartier报告负责，本稿不代证明。

## 6. 本次归档核验

三份新PDF分别15、278、10页，合303页，均从作者官方/大学教学网址取得，检查%PDF签名、页面数、首页文本身份与上述页码；来源快照、SHA256、角色及适用边界写入新manifest。Katz原122页PDF只读复用。作者另执行11项归档count/signature/page/SHA检查，全部通过。Weinstein官方URL下载时Python证书链不足，改用Windows Invoke-WebRequest验证证书后取得；Stein主www URL返回522，改用上述作者msri06官方路径取得并按实际旧标题和metadata固定版本记录。没有以metadata时间冒充正式出版日期，也没有替换旧原件或重跑任何冻结producer。

conjugate_projection已对实际§3作限定只读独审：γ的det、lower-right角色、z_b的变换、prefactor与a↔b配对，以及两项diagonal/zero互换均通过；其审阅不另覆盖本稿下载清单、其它原页定位或任何生产器。
