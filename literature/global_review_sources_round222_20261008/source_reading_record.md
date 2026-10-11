# 第222轮来源与实际阅读记录

2026-10-08，agent `/root/round218_dual_audit`。服务于 `research/openai_source_architecture_global_round222_20261008.md`。以下 FULL 均指本 agent 实际读完指定对象，不是只检索、不是借用其他 agent 独审，也不等于证明或形式化验证 PASS。新文件夹只存真实原件摘录、网络原始响应、文档 text locator 和本记录；既有 PDF 复用。

## 1. 只读版本核对

本地 `E:/codex-build/math`：`git status --short` 空；HEAD `adc7f1241b42e322a6451854ab7e4b4c146bf78a`；origin `https://github.com/openai/math`；提交时间 `2026-10-06T21:58:50Z`。公开 main API 同 SHA。网络保存 `openai_main_commit_20261008.json`：1155 B，SHA256 `d3ec33b8b023f6ae8b4380303198971d7619d75f3f162841242f620eaf033d4b`；实际 FULL 读短 JSON。API 地址 `https://api.github.com/repos/openai/math/commits/main`。没有 Git mutation。

实际读公开仓库 README / CONTENTS relevant family entries、Catalan preprint README/main.tex assembly/bibliography 与 `lean/docs/005.md` 范围说明。目录检索仅定位 source；未打开数学程序或 Lean proof files，未执行代码验证。仓库 verification stage 说明不能替代内核验证。

公开辅助核对：`https://github.com/openai/math`、`https://raw.githubusercontent.com/openai/math/main/CONTENTS.md`、`https://raw.githubusercontent.com/openai/math/main/lean/docs/005.md`。仅用目录定位及发布范围；不将目录标题算作数学正文阅读。

## 2. OpenAI 两个原始稿

Catalan 固定 PDF 原路径 `E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf`：574388 B，SHA256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`。与既有 `literature/openai_math_2026_special_values_20261007/openai2026_catalans_constant_irrational_20260924.pdf` 同身份，没有重复下载 PDF。

实际 FULL 读如下六个完整 TeX section；初次合并输出截断的 odd-primes 中段已另行完整补读，foundations 与 conclusion 也已另行完整读取。字节相同原件已复制至本文件夹 `catalan_sections/`。来源是上述固定 HEAD 的 `build/sections/`，公开目录 `https://github.com/openai/math/tree/main/preprints/Catalans-constant-is-irrational-September-24-2026`。

| 实际 FULL section | bytes | SHA256 |
|---|---:|---|
| introduction.tex | 11379 | c2b11e5f40084caa3430fc7bd6d6032c50db72d9bce9110def68569ca6eeedf0 |
| foundations.tex | 17469 | 21633dce32e242555dde97f82f1124f3524641bb69a2f16b7485177b667cb738 |
| odd-primes.tex | 26263 | 42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10 |
| nonvanishing.tex | 17218 | 4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f |
| real-place.tex | 17837 | 4cd88cafd703b409e581df177cb891f53beb7626b547ec9f6003920861f9a74c |
| conclusion.tex | 2580 | de12e400d16e588d873439158e495a3da00d2a4907866f4ebc9aa94d9813f1a9 |

未 FULL 读 `energy.tex` 与 `certificate.tex`，未重跑 dyadic / prime-scale / mod101 / energy finite certificates。上述六节包含实际 proof，但本轮不声明 FULL 整篇 Catalan theorem 独审或 Lean 验证。实处数值 strict gate 按 conclusion 原文报告，不冒称本轮重认证。

Deligne–Drinfeld 固定 PDF：`E:/codex-build/math/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf`，539601 B，SHA256 `5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762`。本轮没有 FULL 读 PDF；实际 FULL 读 `build/sections/01-introduction.tex`，9745 B，SHA256 `9d632ee8436f3fd986d2f784d1acc2c3024262aacb13a560e921b31963a7289a`；字节相同副本为 `deligne_drinfeld_01_introduction.tex`。其余章节只定位 filename，不记为正文阅读。实际 theorem 量词与“非零不要求数值算术独立”判断来自该完整 introduction。

## 3. Fauzan 与 Fischler：复用固定 PDF

Fauzan：`literature/fauzan_zeta5.pdf`，476337 B，SHA256 `a42c05ccc46b9a7c36428913453c4617202c59109713ba20f464ab9ec640d0da`；与 `literature/ZETA5_IS_IRRATIONAL.pdf` 相同。32 physical PDF pages。实际 FULL 连续读第1–13页，包括 §1–§4 全部及 §5 首个归一化定义段；第14–32页不在本轮实际读域。其 pole-class allocation / polynomial correction 判断来自完整 §3–§4。必要修订时另完整复读第3–5页，Prop2.2 明确 `f=(e^(2πy)−1)^(-1)`、`w5=y^5 f^(4)/12`；第四阶导数不是 f 的幂。新抽取 `fauzan_zeta5_locator.txt` 为118010 B，SHA256 `2654c2dfacb6cfa53cf5adcb45ffe3d98ec8dd8fcb666d0a202a7cb2dd5cbffc`；抽出全文不等于实际读完全文。

原始网页 `https://zenodo.org/records/22826419`：实际读 title/author/date/v1/file/version notice；发布日期2026-09-17，版本v1。`https://github.com/danromik/zeta5-irrationality` 实际读 README 发布范围（作者宣称 Lean4 形式化及外部 PNT axiom 范围）；没有读完其 Lean source 或执行 build / axioms。不以这些发布说明替代 proof 全文审计。

Fischler：`literature/fischler2020_dirichlet_irrationality.pdf`，243833 B，SHA256 `8faaf867a2d2b5ef608f53190cd5cef01e6ca79eabf97d397f009e8672e768e7`。**实际首页版本 arXiv:1904.02402v1，2019-04-05，不能按文件名冒称2020或作者后来修订版。**本轮实际 FULL 连续读 physical/printed 第1–15页：完整 introduction、§1.1 Prop.1、§1.2、§1.3 Thm.3、§1.4 Lemma2 三步 proof 及 Remark3、§1.5 前部 Lemma3/4 statement。第16页以后未读；没有完成整篇论文独审。原始固定版本 `https://arxiv.org/abs/1904.02402v1`。新 text locator `fischler2020_locator.txt`：86536 B，SHA256 `b21f7375f4b18618b3a8830178dbdb3851d5f3c5d65835f1a68f2626ceb357d7`。

公开作者 PDF `https://www.imo.universite-paris-saclay.fr/~stephane.fischler/Lschi.pdf` 只定位到后来版本，不把其整篇内容计为 actual read；正文判据使用的是上面实际固定 v1。目标选择性二维系数平面和 `αβ^v<1` 是本轮给出的不缩放整数线性形式绝对趋零充分条件及余子式消元论证，未把它写成原作者已证明的指定值结论，亦非 CDT 必要门槛。`β/α` 只是两个 radius 形式下界的比，不能推出 actual strict overconvergence；实际 dominant growth / singularity、fixed-rational scaling / 分母 / 导数均另付。

## 4. 三条实际新保存的 primary 公式

实际打开 DLMF 页面并保存/read FULL 以下原始短 TeX equation；仅 selected equations，不声称 FULL chapter。

| 文件 | 原始地址 | bytes | SHA256 |
|---|---|---:|---|
| dlmf25_11E29.tex | https://dlmf.nist.gov/25.11.E29 | 197 | f8011fba03fe90d7f186ab415c5adfa8d5c27972acfcc6a2a22576158e3c4165 |
| dlmf25_6E2.tex | https://dlmf.nist.gov/25.6.E2 | 71 | 2d4b53f0647918badaf7b95ff659a542614ebcef55cde82d20c326c150ff94aa |
| dlmf25_11E4.tex | https://dlmf.nist.gov/25.11.E4 | 88 | 3393307bcceb9742bcf421c5e048e92ef9ed2ed88d565e4d4b43b4d14f4fe5c2 |

用它们核基础 Hermite/Hurwitz/Bernoulli 结构，没有用新 µ7 名称冒充新 carrier，亦未将 ζ5 pole exponents/费用转给 ζ7。正确 ζ7 权为 `w7=y^7 f^(6)/360`，是六阶导数；正性由 `f^(2m)=(2π)^(2m)Σℓ^(2m)e^(-2πℓy)>0`，零矩5/12与7/12与 Bernoulli 矩匹配。主稿初版将两项导数误成幂，属于正测度本体的数学错误，已按原文修正，不能解释为等价排版。

## 5. 实际 FULL 旧记录和第221轮范围输入

以下十个文件均在本轮实际 FULL 阅读；合并输出截断的 odd-global 已单独 FULL 复读。其数值/Lean/扫描声称用于确认历史投入和限定已知框架，不是本轮重跑认证。数学程序未打开或执行。

| 路径（相对 research/） | bytes | SHA256 |
|---|---:|---|
| cdt_cyclotomic_symmetry_gate_round221_20261008.md | 6873 | 3be37acfd427ad802d85f5399b992708712aaaa5811edb6888d61e498ecee7db |
| cyclotomic_quotient_global_map_obstruction_round221_20261008.md | 7527 | 41916916956130d288497d90793d3cdbd5648dfa6fe750e2f5999bddb368783d |
| research_global_review_round214_20261007.md | 6979 | 51f8cd458ac4d8b405363ff73e45d3657d01fc237c92871996b3e68163f8b20e |
| research_global_review_round216_20261007.md | 8957 | 60119f1598fa41ff07a23223a181735d34c23f9611e796df9ae885b2f9431450 |
| zeta7_research_report.md | 9310 | 2ede12582ad7b1d57011e6d7c920ac2ce178d44c88be77df339a37b36de23840 |
| odd_zeta_global_strategy_20261004.md | 11981 | 4ebed2eb12751b191fe2304472dfed709257736051dbe021c308cd3e87ff35a1 |
| zeta7_joint_lattice_20261004.md | 12248 | 5460579240854f86880c0baf34cbde4e64eb8bafd8e193a77bf5ee5cd1ffb4d2 |
| b8_arithmetic.md | 26141 | 4e5080534e86506ec45de8d1168226d876a580b2145aa6cdd4d33a8b316f63e6 |
| b8_verdict.md | 7996 | 45a3c4ec6dd49ee7f733c37e788c8e4b68de4f7b6b1f3015bf9c3f69807711f0 |
| b8_phaseB_gate.md | 9843 | 7c9d98a6959bb44d79ee9dffefd93b1223bc7b2b7e454f7dc50e23a8db78d261 |

必要修订时又选择读取以下旧文件，**不记 FULL 整篇**：

| 文件 | 实际 selected scope | bytes / SHA256 |
|---|---|---|
| zeta7_confluent_lower_kernel_analysis_20261004.md | 开头38行，含完整 µ5/µ7 导数核定义及其后降阶公式段；未 FULL 其余 proof | 8314 / 75285be79a62131b68e9ca353fa4a647c31c8e4f8b12dbdf2d13accb048a6e3a |
| cyclotomic_symmetry_arithmetic_round221_20261008.md | P16–P17 的完整 arbitrary-array 定义、前两列下界和第三列 upper proof 段，实际行211–244；未 FULL 13880-byte 整稿 | 13880 / ec00ff4c6dd4d76b61d1093234e0525a4d164ffdc66d34ac37c4fcda1e56c28e |
| NOTES.md | 开头32行，仅历史 ζ7 pole identity 与 Hermite paragraph；不沿用其首行一般 weight 表达式或程序验证声称 | 54524 / 6ce73206a986420f5fe17fd2515843a01ffaa8220d27516a83d0d679d3bd780f |

主稿 §2 的 FULL 对象是6873-byte 第221轮**汇总稿**；13880-byte 算术稿仅上述选段。五行源具有三列，`18/5` 是 arbitrary-array 前两列给出的总费用下界，实际已证区间 `18/5≤τ≤21/5`，不冒称总费用等于18/5。Fischler 的 n 沿 N 正整数倍增长、空间稳定仅充分大 n，亦已明示；生成芽可对其他 n 置0。

## 6. 运行与结论边界

数学程序运行0：无数值/参数 grid、CAS、PSLQ、能量优化、有限矩阵 proof producer 或 Lean。执行仅为 read-only Git、网络原始来源核对、documentary PDF text extraction/页段读取、rg 定位、原件复制和 bytes/SHA。没有 Git mutation；只写本轮新主稿与本文件夹，旧稿/main/manifest 未改。

本轮没有 FULL 验证一个新的指定 ζ7/β4 theorem，也没有定位到可以直接迁移并已通过 strict gate 的新 carrier。源稿 architecture 与作者发布的证明/形式化状态均按上述真实范围登记。

修订历史：初版主稿14995 B / `e3e9c4c7bbddf0e6dd622ecb7a7e277dec5dd3e2a23ffe6c64d211fd955bd75d` 和阅读记录9082 B / `b41d263c8d7ad9501e524cec4b71d71220264ca0364e2618ab8fd6a67f10f41f` 已被 Root 与独审指出必要导数核、221对象标签及费用下界范围错误，不能作为最终审定版本。修订只影响本轮两个新文档；旧来源文件不改。
