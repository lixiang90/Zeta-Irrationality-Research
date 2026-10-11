# A228 实际阅读与执行范围

日期2026-10-08；作者 A=/root/round218_lambert_carrier。仅本目录和 NEW 第228轮主稿新增文件；未改 OpenAI math、mo271 仓库、冻结研究稿、main 或 manifest。数学程序成功0、失败0；全部新数学为纸面证明。下载、抽取、文件读取和哈希属于文献操作，不计数学程序。

## 当前仓库身份

Root 实际 fetch/检查/FF 后 OpenAI math 的 HEAD=origin/main=fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，工作树干净；本人未执行更新。Root 定向 diff 表明本轮 Catalan、DD、Zeta/Holonomy 路径没有改变。更新前已读的不变正文按下面最终哈希登记，更新后另外实际复读 current README/history、Catalan foundations 和 DD 最后小节。

- README.md：4241 B，b0cc9fed82ea436c974d0d86fc30c8791a433b407254455c6e43c036b2dd5768，FULL。
- history.md：2312 B，ff26d9214a6c29c6bb7faf99b0d55e72ba26a547b4e53485809e95f4de7f3374，FULL。
- CONTENTS.md：647869 B，f2d4a0b512bc366b82c8a7219680547ed9b5f667da5f508aa9fb9c4ee569f0b0，仅关键词定位及相关族003/005/008等摘要片段；不是目录全文或全部论文读取。
- 官方 GitHub、raw README/history/CONTENTS、Catalan foundations/形式化说明、DD intro/holonomy 本轮实际 web open。没有用网页缓存代替 Root 实际 Git HEAD。

## Catalan 原文

来源 https://github.com/openai/math/tree/main/preprints/Catalans-constant-is-irrational-September-24-2026 。paper.pdf 本地574388 B，4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e；PDF本身只核文件身份，不称 FULL 渲染阅读。实际阅读的是对应 TeX：

- introduction.tex：11379 B，c2b11e5f40084caa3430fc7bd6d6032c50db72d9bce9110def68569ca6eeedf0，FULL。
- foundations.tex：17469 B，21633dce32e242555dde97f82f1124f3524641bb69a2f16b7485177b667cb738，FULL；本目录另存同一当前文件 lambert_catalan_foundations_current.tex，并实际 FULL 复读。
- odd-primes.tex：26263 B，42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10。实际完整选读原文件行328–653，包括 central-layer/integral column elimination、全列池组合及素数损失汇总；另读末28行精确 log2 界及严格数值比较。不是整文件 FULL。
- nonvanishing.tex：17218 B，4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f，FULL，包括固定模101的三个48阶矩阵消元表。未复算144个枢轴。
- real-place.tex：17837 B，4cd88cafd703b409e581df177cb891f53beb7626b547ec9f6003920861f9a74c，FULL 联合读取：首次输出中间截断后，明确补读181–320行，覆盖缺失部分。
- energy.tex：12218 B，d6c2488e86915f0b7f0af80705796eb8f2e13e03c2e3c59974b702723e5818e9，FULL。
- certificate.tex：19585 B，75dbdb4a57b54327391a9f883c903d9e8a3c1eef622c93fd569c9a07e94b968c，只读1–17行与419行至结尾。读目标上界和最终 supremum 装配；未完整核所有 trial 系数、根计数与区间证书。
- conclusion.tex：2580 B，de12e400d16e588d873439158e495a3da00d2a4907866f4ebc9aa94d9813f1a9，FULL。
- family README、main.tex 和 lean/docs/005.md FULL；lean/ComparatorChallenges/Catalan.lean 的完整13行挑战声明 FULL；lean/README.md FULL；formalization.yaml 仅首36行与关键词定位。未以 yaml 定位结果断言形式化缺失。

因此本轮不是 Catalan 论文全部细节的独立 PASS，不是所有计算证书复算，也不是 Lean 内核验证。主稿引用已公布结论，核其相关完整机制和投影身份。

## 独立 ζ(5) 原文与形式化来源

作者 Aabir Fauzan 的 Zenodo https://zenodo.org/records/22826419 本轮实际读取。当前记录为v1，2026-09-17发布，记录修订日期2026-09-30。既有 literature/ZETA5_IS_IRRATIONAL.pdf 和 literature/fauzan_zeta5.pdf 均476337 B，SHA256 a42c05ccc46b9a7c36428913453c4617202c59109713ba20f464ab9ec640d0da；MD5=30dafe4adbb13a79f202e94a046c8c8d，匹配官方文件元数据。

没有新下载 PDF。实际用 pdftotext 从既有32页 PDF 抽取并 FULL 阅读以下物理页选段：

| NEW 选段文件 | 页码 | bytes | SHA256 |
|---|---|---:|---|
| lambert_fauzan_pdf1_5.txt | 1–5 | 17652 | 91dc96a0d2e4b643c6a1dbac8c217d5f067f438c495e9e5e4143b82497551570 |
| lambert_fauzan_pdf13_17.txt | 13–17 | 17950 | 845ae936274bfef93d89894adcbb1eb432ad8907335e34400e00abb10744ef68 |
| lambert_fauzan_pdf18_21.txt | 18–21 | 15933 | 00fa3e5923f620142ff6fe90f5524a4817a74cb3627adbd7f540c1fad7ade7d2 |
| lambert_fauzan_pdf28_31.txt | 28–31 | 13733 | 0eb6dacb7172d9c5e4a90836c7005ddd2b4b46dad935ed8a950e885ebd899bde |

覆盖定理/构造、全部归一化命题及整数性证明、质量零能量与目标行列式完成、附录C的稳定邻域/指数260及末尾 future-work 段。没有 FULL 32页，没有全部局部分类推导或所有附录数值证书的完整独审。

research/zeta5_paper_future_directions.md 本轮 FULL 读取，作为项目历史排重而非 primary 证明。已有 μ₇/外场方向不是本轮首次提出。

本地 Zeta5-mo271/README.md 17551 B 只读前140行，明确是旧本地快照；未更新该仓库。官方当前 https://github.com/mo271/Zeta5 与 raw main README 实际 web 读取，另成功下载 NEW lambert_mo271_readme_current.md，18005 B，69047fa5181ebe835862047d5f9bdb8f4ed60b0ff203d7026d023687880225e5，实际 FULL。当前说明列 toolchain4.34.0-rc1，并说明 M=400 等数学调整。没有执行其 Lean/Lake/CI/Comparator/#print axioms。README 的完成声明与本轮独立内核验收严格分开。

## DD 选段及数值范围

来源 https://github.com/openai/math/tree/main/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026 。

- build/sections/intro.tex：9745 B，9d632ee8436f3fd986d2f784d1acc2c3024262aacb13a560e921b31963a7289a，单独输出实际 FULL。
- build/sections/07-holonomy.tex：27594 B，aec06f4767cf810e421c4a394f543b1d7ce128c4a31f02cec5c32e3ecb2a8c44。完整读最后 A nonzero depth-one value 小节，并读前32行的连接规范；不称整个27kB文件 FULL。
- NEW lambert_dd_odd_depth_one_current.txt 为最后小节的完整原文，6032 B，a6b797333d66f20b1e87403892e0501086c5e41850c91646a944e91e1b95f53a，保存后 FULL 复读。

核 R6 以及 rational-descent 非零性与实数算术性质的区别。没有独立复核整个 DD 定理、所有特征2整格步骤或其形式化。相关 Dirichlet L 零点条目仅目录定位，不假称正文证明阅读。

## 输出与执行账

另实际 FULL 读取本轮 Root 新稿 research/global_rank_one_period_gram_cap_round228_20261008.md，检查其模型条件供架构比较；未把这次读取登记为独立 PASS，未修改该稿。

1. 首次过宽 rg --files 命中大量生成文件并截断：只算无效导航，不算 FULL 仓库盘点。
2. 早期组合读取的 foundations 中段截断已由其完整 NEW copy 实际 FULL 阅读补齐；real-place 缺段已明确补读。DD 组合输出也曾截断，故只登记后来单独 FULL 的 intro 与最后小节，不扩大为07全读。
3. 更新前 guessed history 路径不存在；更新后实际 FULL 当前 history。
4. PDF抽取的首次 PowerShell 数组路径表达式失败；部分命令默认产生此前不存在的 literature/ZETA5_IS_IRRATIONAL.txt。核创建时间及文本页首后，用 native Move-Item 把该新文本移到上述 NEW pdf28_31 文件；目标绝对路径均在工作区，没有覆盖或移动旧文件。其余三选段用显式路径成功抽取。此为1次文献命令失败，不是数学程序。
5. web 直接打开 Zenodo PDF 返回 Internal Error，没有成功下载或内容读取；故复用官方 MD5 对得上的既有 PDF。
6. 本轮成功网络保存1个 raw README；NEW PDF下载0；NEW TeX同文件复制1；NEW选段TXT5（PDF4、DD1）。全部选段实际阅读范围如上。
7. 数学执行总数0，数学失败0。没有CAS、有限系数生产器、参数/素数扫描、数值积分或Lean编译。主稿新数学 R2–R5 纸面推导，未认新起始周期为任何尚未证明目标值。

作者将保存后完整复读 NEW 主稿与本范围并报告各自bytes/SHA256。该作者复读不是第二人独审。旧稿及全历史 manifest 不重审、不修改。
