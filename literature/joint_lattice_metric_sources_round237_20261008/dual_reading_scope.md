# 第237轮 Dual/C 实际读域与运行账

2026-10-08。配套独立稿 research/joint_lattice_metric_independent_round237_20261008.md。先独立推导，再与 Packet/B 当前稿交叉审；本记录初次保存时尚未读 B237，后续交叉审另存收据，不回填成独立推导输入。

## 1. 原文身份及实际完整选页

复用当前220页作者 PDF：
literature/global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf，
3628820 B，SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c。
未下载新PDF，未FULL读220页，不把其他代理的阅读范围当本人范围。PDF物理页与所选页页眉编号一致；本轮采用TXT完整读，没有新增PNG视觉阅读声称。

本轮实际 FULL 阅读：

- 复用235目录 PDF1、2：定位§3/§6/§7/§8，目录不充当证明。
- 复用236完整PDF50–54：Corollary3.1.11、Theorem3.2.8/3.2.10/3.2.13、Lemma3.2.14及条件/边界。最后一次工具输出完整；早一次与其他输出合并时有少量截断，未将其计作FULL。本源采用derivative-closed的固定O(1) jump cutoff，没有重证Shidlovsky或宣称N=3D+2单射。
- NEW完整PDF71–77：§6.1 horizontal low discrepancy、§6.2 balanced species、Lemma6.2.6完整主陈述及§6.3完整box proof、§6.4开头所在页。用于明确原辅助多项式的整数coefficients小高度/支持要求；未宣称完整读§6.4后续。
- NEW完整PDF95–100：§7.1末尾、§7.2 Euclidean degree/local heights/filtered slopes完整陈述、§7.3 BC metric与Hilbert–Samuel、(7.3.7) source degree及evaluation map。
- NEW完整PDF101–105：vanishing quotient、target Z、(7.3.9) arch height、finite leading heights、(7.3.14)–(7.3.16)、meromorphic pole-clearing脚注完整范围。
- NEW完整PDF106–110：Lemma7.4.1完整pole-clearing/Poisson–Jensen proof、Lemma7.4.5完整intersection proof、piecewise convexity saving、§7.5开头所在页。没有完整读§7.5后续或把它的binomial metric改名成已付新判据。

精确选页身份：

| 文件 | bytes | SHA256 |
|---|---:|---|
| 235/dual_cdt_current_pdf01_toc.txt | 4051 | fd727da05823ea93450723750fbe31db9f8df40ebf1efd3ed0845ba32baf27d7 |
| 235/dual_cdt_current_pdf02_toc.txt | 4142 | 17153ed8c6300bf7f39276a7d066b1a9898382dcd6119dd41f86ab7507ce92c1 |
| 236/packet_cdt_current_pdf50_54.txt | 18841 | 9789168f87f5db923d6a83335f091d8385412fb64679e20628e68f29b6aaadbd |
| dual_cdt_current_pdf71_77.txt | 26412 | e7d824fbcd81bf860c9a29c35a9596c688afe338079d43b84cb3186d3f13dfd6 |
| dual_cdt_current_pdf95_100.txt | 23396 | 119dcec1ef42d89a24d2f53423d40f4d4e9286308acfd6a2bc482eb64f1243a6 |
| dual_cdt_current_pdf101_105.txt | 22804 | 7271d80c7c7f026e68b6c1a0535e7f4ee802a67dc8eb9c5485233c3ed6575adb |
| dual_cdt_current_pdf106_110.txt | 19691 | 6aac081322ab54a8afadcf50b80fa794b13678deec4f9b673d63940f3ef1a56f |

表中235文件实际位于 literature/holonomy_interfaces_sources_round235_20261008/；236文件位于 literature/global_review_sources_round236_20261008/；无前缀的NEW文件位于本237目录。

早期定位误取PDF57–65保存为 dual_cdt_current_pdf57_65.txt，35985 B / 429879148c9d74d5c75db30eb86bc15901aed1524c64d7b01880881380d50b50；**未读、不采用**。它是实际文档提取事实，不隐藏为未发生，也不把提取等同读过。共同目录其他 packet/root/alternative 前缀文件只在身份列举时见到，本人没有因此声称读取。

## 2. 实际FULL读取的冻结稿

- research/global_joint_lattice_review_round236_20261008.md：
11134 B / b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70。
本轮再次实际FULL读全部七节，采用同一f、完整Γ、κ45/4安全upper、O(1)跳跃范围。没有改236稿。
- literature/global_review_sources_round236_20261008/packet_reading_scope.md：
4736 B / d485ac7c21bd70c49c53c14c95c651dae9b81582d1ceebd61b572d74ab0f5b63。
本轮实际FULL读。其222/229等旧稿的作者FULL范围不转成本人此次FULL范围。
- 固定basis费用7/3、合法共同图cap C*作为235/236冻结输入；本轮不重读全235数学与全图证明，不重核当前外仓库/HEAD/remote或numerical novelty。

## 3. 独立纸证、协调及程序账

独立纸证：正多项式与O(D[0])的Laurent整数基反序、完整Taylor leading整性、逐层primitive quotient、BC degree及local height桥，得到2κ/m²上界；同一flag的各graded index乘积、source degree/finite heights精确抵消，以及实际jump Taylor square determinant的算术defect。有限半径凸refinement按已读Lemma7.4.1/7.4.5推导，不扩大基本Jensen cap到所有metric/多图。

Root在独立阅读全文过程中提示 exact graded cancellation lemma；本人另给自足三角基证明与 pivot determinant表达，而非把Root提示当既成证明。未借Packet237草稿先行推导；交叉审阅另存记录。

数学程序 **0**，数值/prime/参数扫描0，旧producer执行0，Git命令0，新PDF下载0，旧数学稿/main/manifest修改0。文档 pdftotext 提取调用5次（含未采用57–65），均exit0，MiKTeX附Win10提示不影响文本输出。哈希/读写均为文档操作：一条PowerShell哈希汇总管道初次ParserError后纠正；一次apply_patch初稿因缺少行前缀验证失败后正确保存，失败均未写目标文件。这些不是数学执行。

独立稿初版10655 B / 2b2e939642b540c308a2067abda91a0dbca5ca00f476e8dd0de8e158736fdf40 已实际FULL自读后交叉审。仅补明确φ在闭盘邻域holomorphic，并采用B/Root提示的最短证明衔接：固定原Lφ metric，G5用J(1)、G6用mixed J(ρ)，直接采用已读7.4.1的mixed-limit，不另领取shrunk self-energy连续性定理。最终数学稿10822 B / 4af1493bec05bd98ce370ebbfca6c502566779ca05f789700b36b0c5b794dc9c 又已实际FULL保存复读；G7以后判据和exact invariant未改变。

完成独立主稿后另实际FULL读B237最终稿9821 B / cf2550e55910f6feceff0652aa38b5a102749aed7479c67540a4a80bc7e190a8与scope4527 B / 5137be32687a0a8ddf78b2936f767ee9c911404ce1ba8e865f34ad4f237ea87e，交叉纸审另存短收据。B scope里的90–94原文和两页PNG不转成本人已读；本人原文完整范围仍为上列。没有新primary或数学运行。

数学稿和本scope保存后均实际FULL自读，最终scope bytes/SHA另报；本scope不自包含它自己的SHA。没有以辅助lemma重定义主goal成功，没有已付strict energy或新数值ζ/L结论。

