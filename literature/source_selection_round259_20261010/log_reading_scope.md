# 第259轮两log来源选择：实际阅读与执行范围

2026-10-10，作者 `source259_log_products`。所有FULL指实际完整读到文本的指定文件/页段，不代表整篇独立数学认证；下载、保存、hash和关键词命中均不等于FULL。本文不继承其它作者的阅读范围。

## 1. 适用规则与旧记录

实际FULL读取PDF技能 `C:/Users/A/.codex/plugins/cache/openai-primary-runtime/pdf/26.1007.11041/skills/pdf/SKILL.md`。本次只读PDF、提取与渲染，不创建/修改PDF，不适用PDF作者marker。适用路径E:/、E:/kimi-build/、cwd、research/、literature/及本轮来源目录的AGENTS.md均实际检查不存在。

以下旧稿实际FULL读；只使用其冻结判断及重复来源纪律，没有修改旧文件：

| 文件 | bytes | SHA256 |
|---|---:|---|
| research/research_source_admission_progress_round258_20261010.md | 6972 | 7dec44c0b57fec181fa39482f1f20c2096c5d0721343621cd2a434aa5d64ae70 |
| research/research_global_review_round252_20261010.md | 7740 | 5a7f813d82a615067de5697aa5939ee38f5174f3d8adf67f1359ee493736c832 |
| research/research_candidate_budget_review_round252_20261010.md | 13388 | 2db9191981654ba5307e915184d9790e783f890eeb78e6ef5c0481e3dfea1f2a |

初次rg对PowerShell通配路径失败，未得到该部分内容。随后针对research的有界rg输出截断，只作PARTIAL定位，未冒称所有252/258稿FULL。以上三个FULL分别来自明确Get-Content整文件读取。

## 2. 固定CDT原件与选段

原件 `literature/cdt2024_l2_chi_minus3.pdf`，218物理页，4517169 bytes，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。本轮没有重新下载或将作者当前网页版本混同为此冻结身份；也未修改原件。

实际FULL所选物理页3–5、174–193。其中§14物理174–188、§15.1物理189–193首段已经跨页读完；§15.2仅物理193页是PARTIAL section。其它原件页没有本轮FULL阅读声明。只采用§14的已有Theorem C及其明确成功接口，未独立重证全文。

六份文本摘录均从该原件以PyMuPDF提取，全部实际FULL读。初次175–186输出在中间截断，随后明确分175–180与181–186补读，最终覆盖整个文件。未把首次截断输出算FULL。

| 新选段 | bytes | SHA256 |
|---|---:|---|
| log_cdt_fixed_v2_pdf03_05.txt | 8274 | 2eb41277fc8d91dc9ef15a91d91e6ced086f3cc083409b55936cb0ab0c51393e |
| log_cdt_fixed_v2_pdf174.txt | 2677 | 025f5f0764a404f2147a0b62f2d8205412ade3a59a24f355b503657feeb64f95 |
| log_cdt_fixed_v2_pdf175_186.txt | 28402 | 90d560e2ba4c76579361cdb65e591f37f927a4c626f8429ace3ac3151d3da9af |
| log_cdt_fixed_v2_pdf187_188.txt | 4103 | 9b4f2f5a225c49768320fe0b523b3f55be7e32a114dc05c1c84a75c5046a0e8c |
| log_cdt_fixed_v2_pdf189_192.txt | 13413 | dfdb224701b905eb71f4948aae59323db49aea17917a61e71e280f3fc48fc484 |
| log_cdt_fixed_v2_pdf193.txt | 3640 | fdfbf89d7ddc73c7e87023934243c7df82284e8ac74175c048b1bf894efd9b72 |

三份整页PNG以1.5倍渲染且实际看图，核查Ha初始项、P关系常数项符号及第二singlelog参数；这些不是数学数值实验：

| 视觉原件 | bytes | SHA256 |
|---|---:|---|
| log_cdt_fixed_v2_pdf175.png | 147851 | 10eba13c5c4470f4bdc3104c261717acc284351df9e0a31a6a440bbc5731821c |
| log_cdt_fixed_v2_pdf178.png | 155732 | 10befe8194c210ed37f442b9cc922b759cd74a5b023236347d12d98eebc39bfc |
| log_cdt_fixed_v2_pdf187.png | 151593 | 3eb4b3c693879f84c235dfbfa7a07ac0a19ed647ff7090e33af0419b9a9f7f2c |

图上确实存在稿中所述显示笔误，纸面按积分定义/前一行关系纠正。没有把这项纠正冒充原定理失败，也没有执行原文高次polynomial/resultant的独立CAS认证。§14.5最终17与16.2及Appendix A.6是原文接口，不是本轮完整独审或新候选的可借证书。

## 3. 网络范围

一次web搜索，共两queries，domain限制arxiv.org/math.uchicago.edu。返回的作者原文URL `https://math.uchicago.edu/~fcale/papers/L2chi.pdf` 只读PARTIAL结果片段，没有打开/下载或确定远端PDF当前字节身份。第二query没有可采用结果，不作globalnovelty或文献不存在判断。

准确query与计数保存于 `log_web_search_receipt.json`，841 bytes，SHA256 `f9ee1210d7ed4303954ab1e580e1eba1dcf91a4d3db8097e688d3159582e054a`。网络PDF下载0、web.open0。实质证明与来源范围采用固定本地原件。

## 4. 本稿及独核边界

数学稿 `research/source_selection_log_products_round259_20261010.md`，9137 bytes，SHA256 `c12d4e25b661f42b76165a2de4af2b2e442a32dd63fff61485b1f279d1bcb206`。

作者纸面重新推导：两响应完整消芽(L2–L4)、全prefix整性、三处显示纠错、绝对收敛depth-two拆和(L5)、有限张量响应展开及半径/整性界(L6)。报告中的这些推导尚待root/独立作者审核；本scope不把作者自核当独审。

对原文完整17函数rank、十行polynomial determinant与高次resultant、Appendix A.6的全图预算没有本轮独立认证。对一般ζ/L或depth-two全球状态、全仓库或Lean没有认证声明。外仓库未读取/写入；root独立的本轮mixed modular来源不在本scope里。

## 5. 执行结算

本作者数学程序0、CAS0、finite-n/interval实验0、参数/prime/map/word扫描0、Padé生产0、Lean0、外Git写0、旧producer0、归档0。Python仅文献页定位/提取/渲染与文件hash/规则存在性；它没有执行数学系数、参数或矩阵计算。仅创建本作者 `log_*`来源文件与一份指定新数学稿，没有修改main、policy、manifest、其它作者稿或旧归档。

拒绝的是本轮两log扩展：已证明近参数目标重复，其它数值改写没有独立新目标加完整收益证书。没有给一般Hadamard/三log/depth-two方法的全类no-go；没有新数值定理。整个root目标和正式复盘clock不由本作者改变。
