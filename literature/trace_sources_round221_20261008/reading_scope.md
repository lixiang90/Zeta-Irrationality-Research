# 第221轮 trace primary 读取范围

2026-10-08。本文件夹用于NEW文献阅读材料；未改旧manifest。仅一项primary，未增加其余external论文，没有重复下载CDT。

源文件：`../cdt2024_l2_chi_minus3.pdf`，CDT arXiv2408.15403v2（2024-09-16），218页，4517169 bytes，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。公网身份链接：[fixed v2](https://arxiv.org/pdf/2408.15403v2)。复用workspace已有PDF。

Actual read：printed页码与PDF one-based页码相同，**146–174全部页、67–68全部页、203–205全部页**。页码通过PDF提取文本form-feed分段定位；不是按搜索摘要推断阅读。

- 146–153：§9完整，Lemma9.0.3代数/分母proof，Definitions9.0.8/10/12，Lemma9.0.13 actual analytic descent，Corollary9.0.19与BasicRemark9.0.20（末尾在153）。
- 153–158：§10 pure functions、B5/Catalan标记、Lemma10.2.2、Remark10.1.8/10.2.3、plus/minus integrated类型差别与17/14比较。
- 159–164：§11 actual Zagier/Eichler relation、overconvergence、Proposition11.1.8、Definition11.2.1、Lemma11.2.2；Remark11.1.17只限制其中两种Catalan approximant families，不能升级为所有Catalan源no-go。
- 164–171：§12 complete function-rank proof；169–170作者finite-linear-algebra proof实读，未重跑软件；171还含一个多加积分产生关系的反例。
- 171–174：§13完整actualχ−3 proof和费用，尾页跨入Theorem C开头；未读其全部proof，未把17行的Theorem C包混为χ−3的14行包。
- 67–68：fine theorem输入与fixed index-shift Remark6.0.12完整内容。
- 203–205：DefinitionA.4.2、LemmaA.4.4实际前像排除、A.5 strict预算；作者数值证明未在本轮重跑。

保存文件：`cdt_fixed_v2_locator.txt` 为全PDF documentary提取，只作定位；各 `cdt_fixed_v2_pages*.txt` 是确实读取的页段。所有页段全文实读；**不声称FULL218页**。MiKTeX pdftotext在环境中打印legacy-Windows提示但成功输出文件；仅文献处理，不是数学程序。

数学程序/矩阵/CAS/prime grid/PSLQ/Lean/数值积分/Git全部0。新研究稿为 `research/cdt_actual_trace_transfer_round221_20261008.md`；其作者读不能当独审。
