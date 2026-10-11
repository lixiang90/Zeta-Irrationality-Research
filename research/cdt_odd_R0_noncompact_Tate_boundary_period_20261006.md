# R₀：真实非紧化 Tate 边界周期及其单位中心化修正

日期：2026-10-06。NEW 纸面证明。所有既有数学 MD/PY/JSON/manifest 与同行 producer 只读；本稿没有数学 producer，没有执行或导入旧/同行数学程序。它处理指定 toric family 的实际开放上同调，不宣称数值无理性定理。

## 1. 对象和结论

沿用冻结 [toric completion](cdt_odd_R0_toric_completion_20261006.md) §§1–5 的 smooth proper family：
\[
 \phi(v)=\prod_{j=0}^3\frac{(1+v_j)^2}{v_j}=\lambda,
 \quad U_\lambda\subset X_\lambda,
 \quad E_\lambda=X_\lambda\setminus U_\lambda.
\]
取小 disk \(D\) 围绕 \(0<\lambda_0<256\)，令 \(a=2\pi i\)。冻结 [actual positive-cut class](cdt_odd_R0_compact_positive_cut_class_20261006.md) C3 给实际 compact regulator lift \(r_\lambda\) 与正切割 current 的差
\[
 j^*r_\lambda-[R_4^+]=a^4 a_{U,\lambda},
 \qquad a_{U,\lambda}\in H^3(U_\lambda,\mathbf Q),
 \tag{N1}
\]
且 \(a_U\) 在 \(D\) 上 flat。本稿证明：

1. 存在明确 \(T^3_\epsilon\subset U_\lambda\)，它在 compact \(X_\lambda\) 中界一个真实 four-chain，而
\[
 \boxed{\int_{T^3_\epsilon}R_4^+=a^4.} \tag{N2}
\]
2. 因此对任何合法 compact lift 都有
\[
 \boxed{\langle a_U,T^3_\epsilon\rangle=-1,
 \quad a_U\notin j^*H^3(X_\lambda,\mathbf Q).} \tag{N3}
\]
按冻结 C13，Poincaré–Lefschetz 对应的 relative cycle 具有非零 \(H_2(E_\lambda,\mathbf Q)\) 边界。
3. 一个明确 rational OPEN Tate correction 消去此边界周期，并在该 chart 中消去 current 奇性。此单 chart 修正不等于完成所有角点的全局证明；全局中心化的原始 scalar 保持不变则可独立精确证明。

## 2. 必然存在的 horizontal ray 和真实局部方程

取原 grid stratum \(v_0=-1,v_1=0\)，其余坐标在 \(U\)。原 normal lattice 的 order function 为 \(\ell=2b_0-b_1\)。先以 \(\ell=0\) 切 fan 的冻结构造必含 primitive ray \((1,2)\)，regular refinement 保留该 ray。其 generic divisor 附近有 monomial chart
\[
 v_0=-1+s,\qquad v_1=s^2w,
 \quad w\in\mathbf G_m. \tag{N4}
\]
可从 unimodular cone \(((1,2),(0,1))\) 得到这个 chart；更细 refinement 不改变该 divisor 的 generic torus chart。这里没有改 lattice 或加入平方根。

写
\[
 \Phi(v_2,v_3)=\frac{(1+v_2)^2(1+v_3)^2}{v_2v_3}.
\]
实际 proper fibre 的方程为
\[
 F(s,w,v_2,v_3,\lambda)
 =\Phi(1+s^2w)^2-\lambda(-1+s)w=0. \tag{N5}
\]
在 \(s=0\) 有 \(w_0=-\Phi/\lambda\ne0\)，且 \(\partial_wF=\lambda\ne0\)。选 \(v_2,v_3\) 的闭 annuli，中心圆半径例如 \(r_2=r_3=1/2\)，避开 \(0,\infty,-1\)。缩小 \(D\) 和 \(\epsilon>0\) 后，analytic implicit function theorem 给这些 annuli 上全局一致的非零 holomorphic 解
\[
 w=w(s,v_2,v_3,\lambda),\qquad |s|\le\epsilon.
\]
局部解因规定的 \(w_0\) 与唯一性粘接。整个参数集合 compact、\(\lambda\) 与 \(\Phi\) 均有非零下界，因此可取一致 \(\epsilon\)。其 image 留在 ray divisor 的 generic chart，避开其它 boundary components；\(s\ne0\) 时全部 \(v_j\in U\)。

定义 product-oriented chain
\[
 B^4_\epsilon=\{|s|\le\epsilon\}\times
 \{|v_2|=r_2\}\times\{|v_3|=r_3\},
 \qquad T^3_\epsilon=\partial B^4_\epsilon.
 \tag{N6}
\]
盘取 complex orientation，两圆各取逆时针，boundary orientation 正是三个逆时针圆的顺序 \((s,v_2,v_3)\)。这是 \(X_\lambda\) 中真实光滑 four-chain，而 \(T^3_\epsilon\subset U_\lambda\)。故任意 compact closed three-class 在它上的周期为零。

## 3. 正切割 current 的精确非零周期

\(v_0\) 始终在 \(-1\) 的小邻域，未碰正实 cut。因此 \(R_4^+\) 中含 \(\delta_{T_0^+}\) 的后三项全部为空，留下普通光滑 closed three-form
\[
 R_4^+=L_0^+\,d\log v_1\wedge d\log v_2\wedge d\log v_3,
 \quad L_0^+=a/2+\log(1-s). \tag{N7}
\]
这里 \(\log(1-s)\) 是 \(s=0\) 附近值为零的 holomorphic branch，且
\[
 d\log v_1=2\,ds/s+d\log w.
\]
\(d\log w\) 在整个 normal disk holomorphic；其 free-coordinate 分量与后面两个 free \(d\log\) wedge 为零，normal 分量也无 residue。唯一 normal residue 是 \(2(a/2)\,ds/s=a\,ds/s\)。所以
\[
 \oint_{|s|=\epsilon}L_0^+d\log v_1=a^2,
 \qquad \oint_{|v_j|=r_j}d\log v_j=a,
\]
给 N2，精确且与 sufficiently small \(\epsilon\) 无关。此处不是含 cut 的分布周期：在 cycle 邻域后三项本来为零。

将 N1 在 \(T^3_\epsilon\) 上评价，compact 项因 N6 为零，即得 \(-a^4=a^4\langle a_U,T^3_\epsilon\rangle\)。这证明 N3。更换 compact rational Tate lift 不改变结论，因为其 restriction 也在此 cycle 上评价为零。因此原 \(a_U\) 的 relative boundary 为零，已经被本例否定；不能继续把它作为一个待证假设。

## 4. 明确 rational OPEN counterterm

令
\[
 \beta_0=\frac a2\,d\log v_1\wedge d\log v_2\wedge d\log v_3.
 \tag{N8}
\]
各 \(d\log v_j/a\) 是 unit 给出的 integral degree-one cohomology class，故
\[
 [\beta_0]/a^4=\tfrac12
 [d\log v_1/a]\cup[d\log v_2/a]\cup[d\log v_3/a]
 \in H^3(U_\lambda,\mathbf Q). \tag{N9}
\]
它同样在 \(T^3_\epsilon\) 上给 \(a^4\)，不是 compact Tate class。在 N4 chart 中
\[
 R_4^+-\beta_0
 =\log(1-s)(2\,ds/s+d\log w)
       \wedge d\log v_2\wedge d\log v_3. \tag{N10}
\]
由于 \(\log(1-s)/s\) holomorphic，N10 延伸为整个 chart 上 holomorphic three-form。故该 counterterm 真正消去所算边界周期与 local normal pole。

其 motivic 含义是将首项 unit \(v_0\) 换成 \(-v_0\)：\(\{-1\}\) 是 2-torsion，故 rational four-unit Chow symbol 不变。\(-v_0\) 的 principal unit triple 有相同 \(a\delta_{T_0^+}\)、\(d\log v_0\)，而对数为 \(L_0^+-a/2\)，四重 product 的 third component 精确改变 \(-\beta_0\)。这里只使用 rational motivic equality，不声称 integral symbol 不变。

因为 \(\beta_0\) 是 holomorphic three-form，\(\beta_0\wedge\omega_\lambda=0\)，所以 raw scalar 未改变。对于冻结指定的 canonical relative lift \(\omega_{\rm rel}=(\omega,0)\)，配对同样为零：\([\beta_0]\in F^3H^3(U)\)、\(\omega_{\rm rel}\in F^3H_c^3(U)\)，filtered cup 给 \(F^6H_c^6(U)=0\)，因 smooth complex threefold 的 top compact-support class 为 \(\mathbf Q(-3)\)。这是 relative filtered cone 的 cup compatibility，不能用于任意非 Hodge 的 rational horizontal splitting。此点核对 Deligne HodgeIII PDF37 的 8.2.10/11 与 PDF40–41 的 8.3.8/9；relative cone 的 product 延续同一 filtered wedge。并未从 ordinary absolute convergence 猜 cohomological pairing。

## 5. 全部单位中心化保持目标积分：已证与待证分开

将四个 units 同时换成 \(-v_j\)，即令 \(L_j^c=L_j^+-a/2\)，保持 unit triples 的 first/second components。得到
\[
 R_4^c=\sum_{j=0}^3(-a)^j
 \delta_{T_0^+}\wedge\cdots\wedge\delta_{T_{j-1}^+}
 (L_j^+-a/2)
 d\log v_{j+1}\wedge\cdots\wedge d\log v_3.
 \tag{N11}
\]
它代表相同 rational open regulator，且在 total open 上 \(dR_4^c=\Omega\)、在每个 fibre closed。对 \(0<x<1\)，冻结 raw period proof 给首三个 terms 与 holomorphic \(\omega\) 的 type pairing 为零。最后一项的常数修正给 \(\int_{T_{012}^+}\omega\)，其两实际 sheets 为
\[
 \omega_\pm=\pm\frac{i\,d\log v_0d\log v_1d\log v_2}
                         {2\sqrt{\Phi_{012}-64x}}.
\]
共同 oriented normal-current pullback 下两者正好相消；逐 sheet 绝对可积已有冻结证明。因此
\[
 \boxed{\int_{U_x}R_4^c\wedge\omega_x
       =\int_{U_x}R_4^+\wedge\omega_x
       =-16a^3 W(x).} \tag{N12}
\]

N11/N12 已是严格 open-class/raw-scalar identity。尚须另证所有 surviving toric corners 上 centered current 的局部质量、cut angular transversality 和 zero-extension 的 boundary differential 全为零，才可将 N12 提升为 actual compact AJ scalar。同行正在单独建立此全 corner theorem；本稿没有从单 chart N10 推全局。

## 6. 阅读、独审与研究边界

本轮实际完整读取冻结 positive-cut class 全文；实际读取 toric completion §§1–5 及 §6 的开头，未执行旧程序。实际 extract Deligne PDF37–41，首次 GBK 终端编码失败后以 Python UTF-8 重读成功，均无文件修改。网页另核 KLM primary [作者/论文元数据](https://arxiv.org/abs/math/0409116) 与 [published paper](https://www.cambridge.org/core/journals/compositio-mathematica/article/abeljacobi-map-for-higher-chow-groups/96E7B429B8B0E96C08890BE3BAC41724)，未新增 PDF。

本稿新结论是实际开放 Tate 障碍非零与 explicit centered correction；它不产生新数值无理性、线性无关性、Lean 证明或 integral saturation。下一步是全 corner compact-extension proof 与 endpoint-sensitive packet 的 CDT 预算。独审应检查 normal-ray chart、period orientation、noncompact conclusion、relative Hodge pairing 及 N12 的 sheet sign。

冻结前修订记录：同行完整回读依次发现 N8 和 §5 sheet display 的 TeX 间距被保存为逗号，以及 N9 的 \tfrac 被保存为 TAB；已在本稿正式纳入冻结审计之前全部修复。此前 fb91af… 是独审初读 snapshot，终稿另取 SHA 并请独审回读最终文本。无数学内容变化、无数学程序执行。全角点结论若获另稿证明，须以该稿及其独审为准，本稿的局部论证仍独立成立。
