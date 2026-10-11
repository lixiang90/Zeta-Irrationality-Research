# C236 实际源码读域与运行账

2026-10-08。主稿为 research/global_catalan_weight4_review_round236_20261008.md。本轮任务只读外仓库原始 proof、对照235完整源并给 bounded gate；没有远端状态认证或数值无理性新定理。

## 1. 仓库与实际 FULL primary

E:/codex-build/math 的实际只读 HEAD：fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb。两次 git status --short 均无条目，remote -v 为 https://github.com/openai/math。未 fetch/checkout/pull 或写外仓库；不能据本地状态声称 fresh remote。适用路径的 AGENTS.md existence 检查未发现文件。

原目录为 E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026。实际 FULL 原件读取：README.md、build/main.tex 与 build/sections 内全部8个完整数学 section。先逐件读取原件，再保存相同字节的本地副本；下表身份绑定副本，不是将 locator/README当成正文或继承他人独审。

| 原件 | 本地唯一副本 | bytes | SHA256 |
|---|---|---:|---|
| README.md | dual_catalan_README.md | 533 | 197c77731d4846c84c14345185de1518c1e37b32c9a3a3218e864e3914e407de |
| build/main.tex | dual_catalan_main.tex | 1315 | 2ac21647174e4e58cb78cd680724fbe044b317f649260877dab8dc81da4b5255 |
| sections/introduction.tex | dual_catalan_introduction.tex | 11379 | c2b11e5f40084caa3430fc7bd6d6032c50db72d9bce9110def68569ca6eeedf0 |
| sections/foundations.tex | dual_catalan_foundations.tex | 17469 | 21633dce32e242555dde97f82f1124f3524641bb69a2f16b7485177b667cb738 |
| sections/odd-primes.tex | dual_catalan_odd-primes.tex | 26263 | 42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10 |
| sections/nonvanishing.tex | dual_catalan_nonvanishing.tex | 17218 | 4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f |
| sections/real-place.tex | dual_catalan_real-place.tex | 17837 | 4cd88cafd703b409e581df177cb891f53beb7626b547ec9f6003920861f9a74c |
| sections/energy.tex | dual_catalan_energy.tex | 12218 | d6c2488e86915f0b7f0af80705796eb8f2e13e03c2e3c59974b702723e5818e9 |
| sections/certificate.tex | dual_catalan_certificate.tex | 19585 | 75dbdb4a57b54327391a9f883c903d9e8a3c1eef622c93fd569c9a07e94b968c |
| sections/conclusion.tex | dual_catalan_conclusion.tex | 2580 | de12e400d16e588d873439158e495a3da00d2a4907866f4ebc9aa94d9813f1a9 |

sections 表行的原路径均相对 build。原件的 FULL 数学范围包括：完整 moment rational decomposition 与2处 smoothing；odd-prime digit reductions、central p-layer、local integral elimination、loss table/PNT；N=p 的两个 extraction shift、完整 auxiliary row、三固定 seed 及模101 pivots；两sheet Andréief/Cauchy、uniform interpolant、Hardy evaluation cancellation/Hadamard；matched damping/endpoint/diagonal；全部 barrier rational data、root brackets、log interval recipes和最终 product-formula contradiction。

本文逐段纸读 proof与recipe，但没有独立重算模101 pivots、全部 derivative numerator/root-count符号或全 rational interval values。相关 finite-certificate 数值按原论文完整陈述引用，不能把 FULL 阅读等同有限数学执行或每个数值的独立验证。没有读取/运行 Lean、Comparator、supplementary scripts；未全文读取 references.bib 或本文所引外部文献，也未对 hyperbolic-volume 外部定理重做证明。conclusion.tex 已 FULL 阅读但仅采用其 Catalan 同归一化合并论证。

## 2. 自己实际读过的冻结研究输入

- FULL research/holonomy_fine_multimap_and_period_candidate_round235_20261008.md：9563 B，SHA256 eba6a74d5b06d29462aa4223fc614578008002a866f18209b795520d41411f46。完整I1–I7及四节，不只候选locator；I2修后 γ²/m 版本。本文只采用其中实际 c4 值、rank5、involution与q连接，没有重用235的有限处fee作236费用。
- FULL research/catalan_higher_even_beta_period_projection_20261007.md：14515 B，SHA256 2a05a15737d8bedee8a99de83cef55b9a2e60f6ac5942173e5a6b7611f6113dc，完整8节/B1–B22。采用实际 inverse-binomial 起点、全有限周期递推与原contact残留作排重；它引用的旧PDF/网页未在本轮新增全文阅读。
- research/catalan_higher_even_beta_analytic_transfer_20261007.md：23944 B，SHA256 3e3d8df6181cdca82e65103687c9bfe7c5d93772245bb5cf7b4e24a85f7b5e8a。仅完整§7–10（A18–A29；保存文件第382行至末行，开头定义已补读），不是FULL整个稿。读取旧真实β4外权重、confluence范围、nonzero/local-lattice欠桥及历史author-scope，不继承其旧primary阅读账。

对四份 higher-even-beta 主稿/独审的 keyword rg 为 locator；没有FULL两份旧独审，不能把其“PASS”当本轮primary验证。首次外仓库全 preprints 文件名定位输出被截断；只作路径定位，未计为阅读其他论文。之后仅 exact Catalan 目录继续。

## 3. 新数学、协作与 ledger

主稿 C1–C4是上述原件实际证明架构的有范围复盘；C5是235已付资产；C6–C10为本轮完整 odd-projection / ∞ logarithmic-monodromy 纸面推导与准入判断。Root先给 derivative/involution核对意见，后独立核 upper∞路径、forcing常数与log障碍；本文没有把这些协作消息冒充另一份独立FULL receipt。scope仅固定有理线性背景过滤，不关闭growing mixed kernel或全部L值方法。

- 数学程序创建、执行、import、producer rerun、prime scan、参数/能量扫描：0。
- Git只读状态/HEAD/remote；全部 git mutation：0。
- 新外部文献下载0；新PDF0、PDF提取0、网页检索0。本地 exact source copies10（9 TeX＋1 README）已实际保存，非新论文下载。
- 文档创建/复制/hash/纸读属文档操作。首次新主稿apply字符串语法失败1次，未写文件且不是数学程序；随后正常保存。
- 235与更早冻结稿、外仓库、main、manifest：未修改。不存在的未来归档或同行收据不声明已读。

主稿与本scope保存后将 actual FULL 作者复读，最终bytes/hash另以消息登记；不在本文件写自引用哈希。
