# 第240轮 Root 实际读取、来源与执行域

2026-10-08。正式复盘236→240，选择新的有限ζ组合完整矩泛函作为241–244的唯一有界主窗口。目标仍active，没有新数值定理。本scope只登记Root实际操作；代理的primary读取由各自scope单独登记，不与Root合并成整篇/全仓库FULL。

## 已实际FULL的本地研究输入

本轮开始完整读取239最终报告、policy、manifest；完整读236 alternative route、228 repository mechanisms、228 target selection三稿及227 Padé stop稿。完整读本轮A/B/C路线稿（B最终补a=0后复读）及Root全泛函稿/正式复盘稿。最终数学稿的独立审核收据另外完整读取，身份由manifest固定。

最初rg --files与文件列表仅用于定位，不登记为全文读取。一次A scope还未写完时Get-Content返回missing，待其最终保存后完整读取；不是已读范围。Root正式报告初稿两处LaTeX的\\rm误转成CR，已经按原数学内容修为\\mathrm{odd}，最终稿重新读/审；没有数学内容变化。

## 新Tang primary：保存14个选定文件，全部实际FULL

官方仓库：<https://github.com/dtq1997/zeta2-zeta3-linear-independence>。官方API commit/main返回669c92bf7a3728e0de9ad80c373bc29fb5ca3d58，原件固定到此commit的raw URL；保存在root_zeta23/。commit.json/tree.json是版本收据及目录定位，不把两者的大JSON登记为全文数学审阅。目录有更多文件，本轮没有clone或审所有imports。

实际完整阅读：

- README.md、NOTICE。
- Zeta32/Family.lean、Interfaces.lean、Criterion.lean、Assembly.lean、FstarDefs.lean、PrimeObstruction.lean。
- Zeta32/Analytic/Logistic.lean、Analytic/Contour/Moments.lean、Analytic/Energy/Pointwise.lean、Analytic/Energy/Assembly.lean。
- Zeta32/PrimeEdge/LocalShape.lean、PrimeEdge/Gram.lean。

14个文件均有本轮实际Get-Content全文返回，未用导入链替代阅读。网页另外实际读Solution.lean与Challenge.lean的完整可见theorem正文；没有以challenge的sorry推实现证明有洞，也没有把implementation wrapper当成完整实现证明。README的kernel检查为作者声明；Root本轮Lean/Comparator执行0。

Root对基础logistic moments另给自含Fourier/Laplace纸证；扩展到有限odd ζ组合的L3–L13由Root/B/C纸核。Pointwise/Assembly/FstarDefs使−6的准确依赖可追溯，但其所有FstarPoints/势函数数值证书未FULL核完，−6只能条件转移。primitive全系数费用和实际关系点无限非零不能继承。

## 新文献与限定网页读取

Root fresh搜索发现并实际读：

- Tang仓库README与具体源码，来源和范围如上。
- Lai, The linear independence of 1, ζ(3), and ζ(4)，arXiv2610.06838v1（2026-10-05）。Root实际读metadata、HTML完整Introduction和§2定义/partial-fraction证明开段（页面返回到式2.12及随后代入，不称FULL§2）；A另读其§6尾段，范围在alternative scope。本轮原PDF25页按官方metadata保存，未以此宣称Root已读PDF25页。新保存root_lai2026_zeta3_zeta4_v1.pdf及HTML；byte/hash由manifest固定。
- Prellberg, arXiv2609.06895v1（2026-09-07）：只核官方metadata、abstract、补充材料目录；声明Li₂(−1/4)、Li₂(1/5)、Li₂(−1/3)无理。未下载或审28页证明，未将它作为新主源的已付数学输入。先发现的aiXiv条目号与真实arXiv不同，采用官方2609.06895。
- Brown–Zudilin arXiv2210.03391v3的fresh metadata；此轮Root没有新全文读其PDF，只沿用已证数学稿的范围。

定向novelty搜索包括3ζ₃+ζ₅、ζ₃/ζ₅线性无关及新奇值进展；只将primary实际正文/声明作为文献证据。搜索结果含旧或可疑ζ₃/π³声称、二手扫描、Wikipedia/社媒等，不采用其数学结论。没有从未命中指定组合推全球首次性或“全部文献未解”。Fischler集体维数结果仅定位，不据摘要在本輪新证明应用。

## 代理来源与fresh仓库

CDT物理29–34、175–180、190–199选页由B完整读取并保存在本目录；Root实际FULL的是B数学稿及其scope，不冒称Root新FULL读这些26页。Tosi v2新PDF及1–3、6–9页由C读取，RootFULL其原对象变换/排除证明和scope，不冒称RootFULL Tosi36页。A实际read-only检查E:/codex-build/math并保存当前七节Catalan、DD两节、README/history来源副本；RootFULL其最终报告/scope及状态收据，不登记Root重新读全外仓库源码。

外仓库本地与publicremote main/HEAD均fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status空，与236相同；本轮fetch、reset、checkout、外仓库write均0。限定仓库读域不足以认证全部odd ζ数值问题已经解决，也不证明全球不存在其它成果。

## 执行与证据分类

数学程序0，prime/参数扫描0，Lean/Comparator0，旧producer复跑0，Git mutation0。新源码下载14个固定原件、API收据2；新PDF共2（C的Tosi v2及Root的Lai v1）；CDT与Tosi文档选页提取由代理完成，不计数学程序。新的HTML保存是文档操作。

最后采用一个新的240 documentary producer固定已有文件身份、检查239main前缀并追加已审正式报告；仅文档hash/归档，不计算数学或重跑239producer。数学新证明、条件transfer、未付关及目标active由report/manifest明确分开。
