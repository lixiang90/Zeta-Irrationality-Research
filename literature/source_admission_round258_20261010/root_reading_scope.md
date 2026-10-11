# 第258轮 Root：实际读域与独立数学复核

2026-10-10。只记录Root实际调用与读取，不继承作者的FULL或独审标签。257 manifest在本轮开始实际解析，117/117文件及new_main/new_policy bytes/hash逐项核；这是文档连续性，不是数学正确性认证。

## 1. Root新primary与实际范围

新保存Pérez-Marco `Local monodromy formula of Hadamard products`，https://arxiv.org/pdf/2011.10497v1，18页PDF：225072 bytes / e16fb9aa52ef0e825e7fc63523d3bb206b27b72e30f1bed7fa7cfafe42afa03c。仅实际完整读保存提取的物理1–6页，10303 bytes / b52766a6af52bea50097aafa176bede242f331df092be4a33769884425ba1896，包含Theorem1.1、§2证明、Prop3.1和polylog例子。没有声称整篇FULL。下载收据当时写“尚未读取”是历史事实；之后确实两次无截断完整读上述选段。

Root两次web检索共6queries，两个open调用共5URLs：用于定位CDT、DD、Catalan及Hadamard primary，采用arXiv metadata、CDT作者站首页/目录所显示范围与Pérez-Marco。初次256global+web合并输出截断，不记FULL；作者站CDT是当前220页，而本轮CDT作者校准的是库中固定v2 218页，两者不混作同一版本。Rootprimary PDF新下载1，无整篇primary阅读声明。团队其它下载按各自scope记。

## 2. 旧项目记录的Root完整读取

这些是项目笔记，不继承其内部所称primary全文审计。以下均在本轮实际无截断全文显示：

| 文件 | bytes | SHA256 |
|---|---:|---|
| research/period_holonomy_cdt_mechanism_20261005.md | 16857 | 27483fbfe9d54e0e2bbe982d6959da4586bd9e7490bbb2b64c5c6301e3478299 |
| research/research_holonomy_architecture_round255_20261010.md | 13378 | 0f0d5651d857ac07a137defe629286658ea151a81e8ca52fe940383dd6c60324 |
| research/research_global_review_round248_20261010.md | 7851 | 0efe88842e82a1b6cec326a9d753ace0187ebc53a6b049b399e42879b9a825c1 |
| research/research_catalan_architecture_round255_20261010.md | 14434 | 4f4d47ae4ca25aa7317d42ed15a0032e1d56bbb7dbe66ab368ab6740a3efa8bd |
| research/research_candidate_budget_review_round252_20261010.md | 13388 | 2db9191981654ba5307e915184d9790e783f890eeb78e6ef5c0481e3dfea1f2a |
| research/research_native_chi8_progress_round257_20261010.md | 6272 | 03f510d7cee51b40807afd1f3950ffbecc4719ae25e9196248c95dea827cd27e |

248旧完整field、背景成本与all-map cap引起本轮去重纠偏，Root随即让CDT作者精确对照247源，未在未经检查时领取新坐标费用或复活窗口。252旧magnetic与Question15.2.2讨论只作既有资产，不当新准入。Root广域rg搜索的294命中输出截断，只记定位/显示片段；一次regex定位因非法escape失败，不计读取。初次256global输出截断，未补成FULL。

Root亦实际全文读archive257的源代码用于新archive设计，没有运行旧producer。

## 3. 本轮新数学稿：自审与独核分开

Root自己的 `source_admission_shared_jump_round258_20261010.md` 最终10071 bytes / 01e19f162645e4cde1b2d058dc073b9be3ee7953eebe0c9e174b7d7916d58d18 已实际无截断全文复读。最高log例子按独审修为F₀=log²、F₁=Θ₁log²+log；Hadamard闭包旋转限定μ12群内。Root自读不称独立审。

Root对cyclotomic作者做独立数学复核：最终稿12289 bytes / f80b2e0263ff3c1283fc863b38f4a5cf9865f16e72287940f69b43c3bc63c349；scope4978 bytes / 70ee41ab36c0d1fcf8345a61e455da5a3f74e6be957afa157f68df035e5b204e。正文/scope实际两次完整读，无截断。C1–C18 PASS：Fourier endpoint实虚系数、局部t=log(αz)的全部log项、异support隔离、jump全纯与原函数非亚纯区别、消跳系数组分类、known endpoint零但全jump非零反例、log超越和函数rank/minimality分别核。E/U/V/W在s=2的rank5/6/9/10没有混用；foreign log不是0处Taylor行。未从函数独立推出数值独立，没有全圆分no-go。

Root对alternative作者做独立数学复核：最终稿14291 bytes / 440e32429698408b7f7720f875ac2954630bb14c2f1c9e3934a6fa7fc13f617f；scope4150 bytes / 2dec1f54995ab9f3a10e8abc7289111527ad552ba71a8dc52b4f26f016de5d13。两者实际完整读；A1–A11 PASS。真实λ⁷ζ7的非零不等于同数值有理descent；nilpotent exp/log及有限ramification、convergent normal form、Li₇−r jump、14维独立与极小性逐项核。lcm(720,d_H⁷)精确prefix和全部prime powers通过，universal安全7!d_H⁷亦另以积分递推核：固定weight w系数z^m L^j/j!的分母项∏n_i^{k_i}满足n_i≤m且Σk_i+j=w；正次幂积分产生m^{−h−1}，零次幂提高log degree。因此所有weight≤7均由7!d_H⁷覆盖。该模型仍不是普通Q[[u]]入口。原Catalan两处strict数字仅采用其scope所述primary接口，没有Root重跑能量表/非零certificate或继承全文认证。

Root现已实际完整读CDT终稿19153 bytes / d6209fecb3bdbb343288f1dee71d7128d07cb402f0b3b0d89fb40287d9c09e14及scope9725 bytes / 8ed3066b3da7f772a1f0b6f1843e780473b5ef92fa3fa2c4088dfa91c95dd20a，无截断。scope原存research，Root只复制相同bytes到本目录cdt_reading_scope.md，不改作者原稿。全部(2.1)–(7.2)纸面独核PASS：trigamma矩阵det1/288；两完整积分由compact支配给全坏芽消去；HG归一化及局部log jump给Jδ=−i√3(1−3x)^−1 F(1−z)，δ值非零；假设关系剩forcing非零；symmetrization的integer recurrence和真实截断2N；14tuple/τ/strict采用作者实际原文读域，不声称Root重新证明该218页论文或重跑Appendix energy。

χ7部分另逐项核all-prefix整数逆和乘法、B的n^−2/2支配、F7非负有界与C的绝对重排、真实Abel和trigamma投影。显式E模型上的Q/P/O局部展开给T divisor2Q+O−3P；消元与critical numerator2y−x³+3x−2、R=(8,49)由eta-S constants、整个δ7 fiber分别核。去重B7/C7同旧primitive，A7/A0为同角色同weight quotient，故源在完整field有理gauge。T非Q(u)与Z非Q(T)的fiber pole证明、degree3恢复完整field和三整数行通过；原生dq归一化使旧Abel cap可移交，但新cyclic rank/τ不能贴旧值。数学PASS只是有限来源拒绝，不准入新χ7实现。初次读作者保存中的稿后又实际FULL读取上述最终版本；不继承其更早FULL标签。

## 4. 执行边界

Root数学程序、finite-n数值/interval、CAS、参数/prime/map/word扫描、Lean、外Git写和旧producer均0。JSON/hash核、文档提取/下载与新archive的文档核验不计数学程序。团队CDT作者精确有理CAS实际3次进程，固定HG拉回/T消元/F7恒等式，按其scope和保存JSON收据记录；不能把Root的0扩张成团队0。没有新numeric或全球novelty结论。

clock last256，258完成后count2，next260/latest264，不重置；goal保持active。新四稿、report/scopes和唯一独审齐全才单次archive，旧116非policy pins与main/policy旧bytes前缀保留。
