# 第231轮 C 来源与实际读域

2026-10-08。本记录只登记本人实际阅读，不继承Root/B/A的primary或数学稿FULL声明。数学程序0。

## 1. 新保存primary及完整选段

1. Faribault–Tschirhart–Muller, *Determinant representation of the domain-wall boundary condition partition function of a Richardson–Gaudin model containing one arbitrary spin*, J. Phys. A49 (2016)185202。机构原件 URL：<https://orbilu.uni.lu/bitstream/10993/33488/1/faribault2016.pdf>。

   - `dual_faribault2016_institutional.pdf`：391654 B，SHA256 `ee9be05bb56298cda3494d06d0aeb93c551c26e99ed62406393072f49e70fa8e`。
   - 本人实际完整读PDF1–3：IOP cover及printed1–2。选段 `dual_faribault2016_pdf01_03.txt`：8390 B，SHA256 `77e8844b1fc75f9afeb9444776d479354a15fa45f80bd8fda762edcb69ca1cd5`。完整选段包含abstract、Cauchy节点distinct假设、公式(1)–(4)及其全部周围文字。
   - 使用的是任意两组distinct节点的永久和/Gaudin身份(1)–(3)；没有FULL读printed3–15或原文引用[1]的递归证明。正文另给有限域自含推导，不把Bethe应用条件当定理假设。

2. A.M.Kamenetsky, *Determinants and permanents of an arbitrary the Hadamard degree of a Cauchy matrix and proof of a generalization of a conjecture of R.F.Scott(1881)*, arXiv0907.2860v1。原件 URL：<https://arxiv.org/pdf/0907.2860v1>。

   - `dual_kamenetsky2009_arxiv0907.2860v1.pdf`：248092 B，SHA256 `3d5e2bd3a8364518920f1d6cc3ed5f0822c876d763bed4257ceaf9eacdb5a61a`。
   - 本人实际完整读PDF1–3（printed1–3）。选段 `dual_kamenetsky2009_pdf01_03.txt`：14113 B，SHA256 `0f30f17b0f63d53fb93b18c471ab5389caf7c26d7013f2fcce5cce66b637e22e`。完整包含abstract、Introduction、Theorem1的characteristic0假设和完整证明、Lemma1的完整声明及证明。
   - 仅用来核简积式的binomial根集假设并排除搬用；没有声称FULL读后续20页或采用未读结果。

## 2. 实际旧稿阅读及搜索边界

本轮实际FULL复读本人冻结230稿 `research/q2_residue_saturation_interface_round230_20261008.md`：5391 B，SHA256 `cd9003d7c29d1154543ed3e241464a6bb12c3076675723e58c999423aa32b35f`。未改此稿。B的231块分解由消息获知，仅作为未独审的平行接口；不登记其稿FULL。

定向web搜索围绕Cauchy永久和、Gaudin表示、Hilbert/Toeplitz半单位偏移及有限域congruence。搜索命中Sun等multiplicative/root-of-unity永久和结果、Hilbert序列、论文摘要和二手页面，均未用于证明，也未声称其全文或原定理已读。没有从“未搜索到”推出文献不存在或条件未解决的普遍断言。

较早web直接打开机构PDF返回502，后来PowerShell机构原件下载成功；尝试arXiv1511.03127v2返回“no document”，未产生PDF，该失败不登记为成功下载。最终仅有上述两个真实新PDF；未保存失败HTML为数学来源。

## 3. 运行与写入账

数学运行0。没有probe、CAS、参数扫描、旧producer或数学计算脚本。PowerShell用于新目录/下载、pdftotext完整选页抽取、文件读取和文档hash；均为文档操作。本轮手算反例及全部矩阵/插值证明为纸面核。

仅新写C231数学稿及本scope，保存后分别实际FULL作者复读。未修改旧稿、他人稿、main、manifest或git。保存整篇PDF与实际FULL读所选文本严格区分；本scope不代表完整PDF阅读全文或独立审稿。
