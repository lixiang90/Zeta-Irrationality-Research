# Root 第227轮文献与读取范围

2026-10-08。本文是读取证据，不把下载、网页定位或作者自读等同于完整论文独立验证。

## 新保存原始文献

- Fischler–Rivoal，*On the values of G-functions*，作者 PDF：<https://rivoal.perso.math.cnrs.fr/articles/gvalues.pdf>。保存为 `root_fischler_rivoal_values_author.pdf`，213981字节，SHA256 `3d966f8edf1d6640173d8cb3bdf8957f2673e5fe6659636c9e902d4381819572`。共27物理页。
- Dreyfus–Rivoal，*Representability of G-functions as rational functions in hypergeometric series*，作者 PDF：<https://rivoal.perso.math.cnrs.fr/articles/repgfn.pdf>。保存为 `root_dreyfus_rivoal_representability_author.pdf`，430421字节，SHA256 `b882519d9860a9316b9af55acd5ed1e6c9df881d96ee576fdb646f40f3bd6946`。共20物理页。

网页检索仅用于寻找原作者文献。采用的结论均来自上述原文，未以非 primary 的搜索摘要代替定理。

## 实际完整读取的选段

1. `root_fischler_rivoal_values_pdf1_6.txt`：20558字节，MiKTeX pdftotext 使用 `-layout -enc UTF-8 -f 1 -l 6` 生成；Root 分两段完整读取所有内容。包含 G-function 定义、定理1–5完整陈述、论文对分母过快的限制、ζ/MZV/Catalan 属于 G 的例子。
2. `root_fischler_rivoal_values_pdf19_20.txt`：9191字节，选物理页19–20；Root 一次实际完整读取。包含定理4证明的末段及完整§6.1部分和逼近构造，§6.2只读到该选段末尾，不称完整。
3. `root_dreyfus_rivoal_representability_pdf1_6.txt`：21085字节，选物理页1–6；Root 分两段实际完整读取。包含问题1–3、Proposition1、定理1及推论1–3完整陈述、用途说明和§2.1开头。

网页还定位并阅读第二篇物理页15–16中局部指数与 connection 的相关文字，但该段未保存为本轮 TXT、未完整独审其证明。路线决定只依赖已完整读取的主结论陈述，不依赖该段的 NumGfun 近似常数。

**没有**完整读取两篇全部证明、生成页面截图或认证原作者数值计算。PDF原件和选段 TXT 保存供后续准确复核；SHA/链接核查不扩张数学读取范围。

## 同项目实际读取

Root 在本輪起始实际完整读226报告，完整读226 archive 脚本和C的227最终诊断全部六节。冻结226的数学资产沿用此前实际完整独审；没有重新运行任何旧 proof producer。之后的 A/B 最终稿及独审回执在227总报告中逐一登记，不在本文预先声称已经读过。

## 本轮执行范围

Root 新下载作者 PDF 2个、selected TXT 3个；HTML/TEX0。MiKTeX 文本提取退出0，出现系统旧版提示，不属于数学失败。全部数学由纸面推导与独审完成；无序列取样、根求解、参数/素数扫描、数值积分、CAS、PSLQ、Lean 构建、Git mutation。尚未重新检查 `E:/codex-build/math` 的当前云端状态；不能称本轮验证最新仓库或其形式化结论。

本轮决定见[路线收束稿](../../research/pade_route_stop_and_global_inputs_round227_20261008.md)。作者复读与独立审读分别记录，不能相互替代。
