# 第223轮 lambert holonomic 结构文献 scope

2026-10-08。round218_lambert_carrier。这里只登记本人的实际读取；Root及其他审阅者复用相同PDF时的阅读另记。对应 [数学稿](../../research/pade_holonomic_structure_round223_20261008.md)。

## 新归档的 primary

1. Doron Zeilberger，*A holonomic systems approach to special functions identities*，JCAM32(1990),321–368。来源：[作者PDF](https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1991_p321.pdf)。文件 `lambert_zeilberger1990_holonomic_author.pdf`，3514835B，48页，SHA256 `3d6f88a09982574a7c74565d286fb2cd88aa1a3c0d5f76655f4be999cd516966`。实际完整读PDF1及14–20（印刷321、334–340）：定义/有理生成函数coeff arrays，Proposition2.1，3.1–3.5及离散3.1′–3.5′，§3.2.1 diagonal/P-recursive对应；只采用数学稿列明的closure，不宣称完整读48页。实际选页TXT为page1、pages14_18、pages19_20。

2. Herbert S. Wilf、Doron Zeilberger，*An algorithmic proof theory for hypergeometric (ordinary and q) multisum/integral identities*，Invent.math.108(1992),575–633。来源：[作者PDF](https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1992_p575.pdf)。文件 `lambert_wilf_zeilberger1992_multisums_author.pdf`，2889794B，59页，SHA256 `8dc85466d9bdffad1f44f33826df31b61076654b1dbf681c3c40ee33002e57b1`。实际完整读PDF1、10–12及16–19（印刷575、584–586、590–593）：proper定义的参数/仿射阶乘条件，fundamental lemma，telescoping theorem/corollary及算法边界。未读/执行其后具体算法，没有给当前包计算operator。选页TXT为page1、pages10_12、pages16_19。

3. Wadim Zudilin，*Well-poised hypergeometric service for diophantine problems of zeta values*。来源：[作者PDF](https://www.math.ru.nl/~zudilin/PS/z234.pdf)。文件 `lambert_zudilin2003_z234_author.pdf`，317847B，SHA256 `81eeeca38692773d3760cef033d007c63da4da8747276f707aa09ef0d3de9207`。首页Date2002-03-21、LaTeX-revision2003-03-04；pdfinfo实际33页。完整读PDF1、23–25：§7全部（23–24）及§8开头（24–25），核式62与tilde F的真正差别。相近族的characteristic polynomial不移给当前包。Numdam出版扫描网页为35页，只用其locator/书目，不另下载、不冒称作者版等同出版扫描或FULL读35页。选页TXT为page1、pages23_25。Root/C随后复用此PDF，避免相同原件重复下载。

## 复用的 primary 定义

CDT固定v2 `../cdt2024_l2_chi_minus3.pdf`，4517169B，218页，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。本轮完整重读PDF189、Definition15.1.1，并保存 `lambert_cdt_fixed_v2_page189.txt`。本轮不新增整篇CDT阅读或把222选读计为223新页域。

所有全PDF locator只用于定位，不能把pdftotext全提取计为全文阅读。primary新下载PDF3份；没有下载HTML/TEX/README或第三方数学摘要。部分旧定位输出含OCR误字，不作为当前公式证明的单独依据；实际H1–H9是自足代数推导并核所用定理的假设。

数学程序、CAS、矩阵执行、参数/prime扫描、guessing/telescoping执行、数值积分、PSLQ、Lean、Git均0。工具只下载、文本提取/读写、source metadata/hash。未重跑222任何producer，没有更新旧文献manifest、旧稿或main。最终数学稿的作者FULL自读/身份另报，不冒充独审。
