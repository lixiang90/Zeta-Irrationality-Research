# 实际边界 Jacobi/Krylov 算子的独立审阅

2026-10-06，NEW，/root/toric_chow_completion。实际全文审阅本轮同行新稿及完整程序/输出，仅静态读取，不执行、import或重跑任何旧或同行数学producer。本文只审所列结论；未证明 original auxiliary targets 在无穷素数上非零。

## V1. 实际读取对象与指纹

实际全文读 `research/cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.md`，SHA **09b9e74683f4767c2a69eb5a7d67893fda1c6d6bb738d2b245f8f692fc20d17f**，正文K1–K26及来源/执行史全部读完，无截断。另实际全文静态读 NEW PY SHA **ef2dd914c860485b76a29ce8566a2385c4e4bc12d285da72c6ad4a29ef1ab8fa** 和 JSON SHA **7ece9d110eb1f2580ccd549cf5250c5b3172f774e3af9501e3a63873be87a180**，三个r1/2/4案例的全部字段、characteristic polynomials、target-not-asserted字段完整核读。没有执行它们。

作为same-object校对，本轮另只读冻结 `cdt_odd_paired_auxiliary_units_structure_20261006.md` 的U1–U8、U15–U28及U29开头，核Sy、T<r/Q<3r、folded权重μ、cross权重γ=2/4/5与真正half jet。这里不称本轮新读冻结全文；先前研究轮次的读取也不再次计页。

## V2. 边界逐边自伴与 polynomial conjugacy

K2/K3与冻结实际target严格吻合。独立核相邻Sy比值：在Fp上 Sy(x)乘head polynomial A_y(x)=∏_{k=-a}^a(x−k)恰为x^p−x。因此在head点 Sy(x)A'_y(x)=−1；相邻A'_y阶乘比给Sy(x+1)/Sy(x)=−(a−x)/(a+x+1)，不把点值identity升级为rational function identity。

F_r(−x−1)=F_r(x)，所以K5forward与反向edge系数的符号恰抵消Sy^−5比值。跳边x=−r,r−1与外部端点分别被F_r和a−x因子杀掉；所有flux均已处理。由有限边求和得D0自伴并与χ通勤，不用正定性。R=Sy^4在实际support上是unit，K7系数精确是A0乘相邻R比；端点与jump同时为零。因此K8是实际节点上的共轭，K7本身仍是polynomial算子。diag(D0,D4)经(T,Q)→(T,RQ)化为diag(D0,D0)，sector-constant symmetric matrix可穿过它；K9通过。

## V3. 共同potential、全尺度leading units与critical basis

独立展开A0/B0的最高两项及共同diagonal的x8差，K10的两factor确切。将a=5r、18r=−1代入后，同一γ=−98/27恰同时给K12两factor，不是两个channel自由选gauge。K13的模18算术排除所有零：λ0第一factor的6d+1在critical range中正且小于p，第二factor首次可能root在d=8r−5；λ4两个factor首次root在d=5r+1及10r−4，全部超出相应critical ranges，r1亦包括。

因此E_i按even degree恰提升4，每条四seed链的leading product均unit；K14是原degree<r和<3r上的真正三角基，不依赖Gram–Schmidt或intermediate norm。K15 determinant-square normalization与same target相符。本变换只证明aux-local GL，作者明确保留global denominator/arch成本，没有给免费费用下降。通过。

## V4. 真实Jacobi块、continuant及八源递推

独核node0fold2、middle cut两offdiagonals为零、其余内部edge均unit，故K17块确为r和4r+1。K18的tridiagonal expansion给monic continuants；unit offdiagonal products保证相邻多项式互素、Euclidean degree每步降1，允许multiple eigenvalues。K20的prefix/suffix path products及adjugate符号正确。

Selfadjointness使K21两边幂归并，不改变真实unequal chain profile。变换后两个channel都由同一个J作用，所以八源Stieltjes entries的分母可用C=θ_mid θ_out，而非假定minimal rank减少或simple spectrum。Cayley–Hamilton/continuant直接给K24全尺度递推；order N=5r+1随r增加，作者未将它冒充固定跨素数阶数。通过。

## V5. 真endpoint单位机制与target不能免费继承

起点Krylov列J^j e0支撑前j+1节点，其最末系数b1⋯bj为unit；weighted Gram的三角 determinant与逐边balance wi bi=wi−1 ai−1精确给K25。故这个**实际块的endpoint functional**在全部首profiles1≤k≤m上确有单位norm，不依赖正定性、未知Gram或distinct spectrum。

同一三角support也证明K26：last-node非零迫connection polynomial恰degree m−1。实际outer seeds u^t、Ru^t全部last-node非零，因此connection degrees全部4r。这是原critical target与endpoint perfectness之间的真实缺口，不可将endpoint首norm结论移植为G0/M5无限units。作者明确保留middle r1的zero-seed例外和χ/halfjet。通过其声明范围。

## V6. 程序与有限证据的准确范围

完整源码只import标准库，自构polynomials/actualweights/finiteJacobi/criticalbasis；guard在输出存在时拒绝执行。JSON记录作者首次1run PASS3cases/364checks，我仅静态读，未重跑。有限leading、nodalconjugacy、foldbalance、targetdeterminant-square、continuant和endpointproduct检查与纸面证明吻合；没有assert original target infinite/all-r units。有限check本身不替代V2–V5全尺度纸面核验。

## V7. Primary原件实际读域

本人本轮下载新PDF0；同行正常TLS归档的34页原件中，本人实际阅读11个distinct PDF页：

1. `literature/cdt_paired_auxiliary_jacobi_sources_20261006/costas_santos_johnson2018_tridiagonal_field_arxiv1807_08877v1.pdf`，18页，SHA **d80659f49ddc9cdd6e14cd292f033ff01ea207b9cb1e01d7c286f4fa27b5d808**；本人实际PDF1–5，含continuant、Theorem1的arbitrary-field proper-pair条件、multiple-root许可与互素不等proper的例子。不称读完18页。此来源支持精确范围；作者K18–20已自证，没有用一般properness推target normality。
2. `literature/cdt_paired_auxiliary_jacobi_sources_20261006/duran_sanchez_canales2014_matrix_orthogonal_differences.pdf`，16页，SHA **d65afa9402977d031947395585c282188a5d76a78794a21d1305eaea9d557736**；本人实际PDF1–4,8–9共6页，含Theorem1/2 quasi-definite与degree2/1、Hermitian条件，Lemma4.1的degree不增假设及proof。本项目operator升degree4且有限域target仍未quasi-definite，不能直接套这些定理；作者也没有这样套用。

本人不将同行自己的27页actual读取计入11页，不把root阅读或PDF检索snippet计入本人。该review通过K1–K26明确声明的数学范围；无限auxiliary unit、global费用、strict margin及特殊值新定理均未解决。主数学09b9没有发现需要修正之处。

## V8. 最终收据补读与冻结

先实际全文读作者候选receipt92695c1c113fa4c69f14c1b07c67b4870f50f96da3dbd66db54b1ad83288813c，再实际全文读正式冻结的 `literature/manifest_cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.json`，SHA **129070562e4df36e5e0fcfb2b93202bf9d4b015d287fb04ced89bac556a2e1b3**。主数学09b9、PYef2d、JSON7ece均保持同一字节指纹；最终receipt只登记已完成审阅状态及准确root7页/本人11页primary范围，不扩大数学结论。V3曾在独审未冻阶段将λ0的root措辞明确为第一/第二factor分别排除，作者主数学没有相关错误。

本独审新增V8后实际全文最终回读，正式冻结只读。旧/同行数学producer execute/import/rerun=0；本review没有自有数学程序。本人本轮独立Smith机制的唯一一次执行在另一NEWreceipt中记录，不混算作本review对同行代码的执行。最终收据不追写本review最终SHA，避免指纹循环，父任务根收据分别登记二者。
