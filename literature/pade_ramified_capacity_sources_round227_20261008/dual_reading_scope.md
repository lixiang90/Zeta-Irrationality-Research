# C227：ramified leaf/capacity 实际阅读与运行范围

2026-10-08。数学程序0；这里只记录本人实际阅读、NEW来源与纸证明边界。旧/main/manifest未改，未执行任何旧producer或archive。此scope随新数学稿完整保存复读；作者自读不冒充独审。

## 1. NEW primary及本人真正读域

| 保存对象 | bytes | SHA256 | 实际范围 |
|---|---:|---|---|
| `dual_mcmullen_complex_dynamics_orbifolds_author.pdf` | 1211489 | `aee144d8363fec9f134883cfe39af684eb12adc306ac0ecbc3405be9fdf90423` | 下载归档219页原件；不是FULL219页 |
| `dual_mcmullen_pdf182_188_orbifolds.txt` | 14412 | `f3db898a9003f862fb829a250b8532890339fc1af334bd7affa3cf16fe982e8c` | 实际 FULL 完整PDF182–188（印刷177–183）全部文字 |
| `dual_cdt_fixed_v2_pdf23_25_caratheodory.txt` | 11736 | `e1b6c1ff784f0caa4940d04b7e9570a18e246b346f4e5558e54c0c7a98c51683` | 实际 FULL 冻结CDT完整PDF23–25 |
| `dual_cdt_fixed_v2_pdf26_27_leaf.txt` | 8259 | `e15f6f9849a746c2cb5dcbdc44843a5c7ba4dab2ae16e72ec5599fde528fc87b` | 实际 FULL 冻结CDT完整PDF26–27 |

McMullen来源是作者[Harvard原件](https://people.math.harvard.edu/~ctm/papers/home/text/papers/real/book.pdf)，题名 *Complex Dynamics and Renormalization*；pdfinfo确认219页、book.dvi、Ghostscript8.71与PDF大小。实际七页selectedTXT覆盖完整§A.1、§A.2：chart/multiplicity、∞表示omit、holomorphic orbifold map的全部degree-divisibility条件、covering区别、Euler characteristic、完整TheoremA.1/A.2及证明、curvature归一、完整TheoremA.3。末页§A.3开头亦输出并读到，但不应用rational dynamics分类。本稿只借orbifold holomorphic map及uniformization/Schwarz lemma，不借未读的Thurston原件或全部书。作者PDF开篇误引“uniformization A.4”不继承为实际定位；真正statement为A.2。

McMullen下载前搜索既存文件名，只有另一个 *complex analysis course* PDF；其不是本书，不作为同件缓存。本轮仅下载这一个新PDF；Beardon–Minda academic mirror和author Eremenko等web搜索/定位不承担数学证明，没有归档或应用其未完整读的定理。搜索结果摘要、一次宽find输出截断都不登记FULL阅读。

CDT复用固定 `../cdt2024_l2_chi_minus3.pdf`：4517169 B，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`，218页，不再下载。完整实际PDF23–27五页两份TXT，包含§2.8所引Carathéodory|φ′(0)|≤16的完整唯一zero/omit1条件和相邻解释，及完整§2.9/Proposition2.9.3/Remark2.9.4/§2.9.5。顺带读到§2.7末和§2.10开头、Conjecture2.8.1/Question2.8.3/Th2.8.4等，不应用这些statement或旧Li2数值状态，不把它们当当前novelty核验。Carathéodory1954书(412.8)页198本人未读；界16依据CDT的明确primary引述，没有声称已审原书证明或FULL218页。局部univalent-leaf proposition是设计充分条件，不把它的唯一0前像升为所有maps的必要条件。

本轮新增primary **PDF1、selectedTXT3、HTML0、TEX0**。PDF到TXT两类提取均系统pdftotext，MiKTeX平台提示仍exit0且完整输出；文档提取不是数学程序或数学失败。没有渲染/截图，故不声称视觉逐页审核。

## 2. 冻结输入与历史排重范围

复用本人226实际 FULL 作者稿13212 / `2bbe912ac345d5afa5c6a999c1ba05b8b79de83d27b58e0a44921490a3ed1772`、Root最终外幂9351 / `a981d3fa323ee30fd1408c280614cae10f0ef52797083673cd92cdeddab2ceae`的本人实际 FULL 独审，及226报告8332 / `f0d977e7cde11c6247c675356bdddc20f7065e967c1ed09560ce217198734c68`的本人实际 FULL 独审。225 actual modes/powers与target branch cap也是本人既有FULL最终输入；本轮不声称又重读全部历史文件、archive脚本或manifest，亦不重跑leading certificate。

227实际选读 `research/cdt_odd_level20_leaf_20261006.md` 当前16644 B，SHA256 `8660d6cd6993bcc1fd76e5c381fa5c03fa450dc11eacd78d5747574a1e1a9719` 的完整§§4–7；输出还含§3末与§8开头。相关内容为CDT精确共同叶/全部foreign前像、native0、even ramification、Carathéodory条件、三elliptic genus1提升和未付capacity。没有FULL整篇，不重新审其j式或level20数学证明，也不把不同载体的非零log障碍转到当前packet。

宽rg只导航“orbifold、Schottky、Picard–Lefschetz、even/all-preimage、cosh”等历史条目；其输出不等于读每个命中文件。另对既存trace locator读取Carathéodory附近完整段作页码导航，随后以上实际PDF选页承担完整primary条件。较宽find/rg组合有一次总体tool预算截断，不登记FULL；后续单一TXT输出完整。

## 3. 本轮证明及真实准入范围

新稿自含证明实际local coefficient决定odd/even前像；cubic inverse的rank3/两维不可约monodromy、两处native分支/第三regular叶、large polynomial共同图、同图energy、Lagrange精确系数与固定3估值；无需mathematical producer。

该cubic是**量词反例**，不是当前Padé源，不能推出其大图存在或所有图不可能。原cubic芽的fixed3-adic线性负深度不能由finite固定LCM数组支付，unbounded derivative也没有给unbounded rank3 margin。两值all-even的cosh construction只否定两值几何假设自动给有限derivative cap；没有付当前source所有foreign叶。三值orbifold bound与唯一native0的64|a|cap均标作conditional。当前D/X/H_g尚未付所有reachable叶的fractional coefficient非零或原点唯一必要性；global irreducibility也不足以替代它。

因此227没有取得原packet positive map+energy+完整整模型，亦没有证明全部ramified源失败；按停止准入规则将其作为结构工具供228比较，不把补上conditional uniformization当新主线希望。正式全局cadence222→228、窗口226–230未重置，数值目标active，无新ζ/L数值无理性/线性无关定理。

## 4. 操作与运行账

数学程序 **0**，失败数学运行 **0**。全部counterexample、ODE、torus/Jensen energy、Lagrange/formal residue及Legendre floor估值、conditional bound均纸推；没有CAS、roots/矩阵执行、prime/parameter/energy扫描、数值积分、PSLQ、Lean、旧producer/import/rerun或Git mutation。网络下载、pdfinfo/pdftotext、rg、文件hash/Markdown保存只为文档操作。

本轮一次新PDF请求成功、三份selectedTXT成功；没有为失败请求制造成功记录。没有修改226及更早冻结稿、main、manifest。最终新数学稿与本scope保存后 actual FULL 自读登记身份，并交同行独审；不把Root协调消息或自己作者读当独立审查。
