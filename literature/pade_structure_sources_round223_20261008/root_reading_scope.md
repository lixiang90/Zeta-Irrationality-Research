# 第223轮合并阅读与执行范围

2026-10-08。Root记录实际最终读域；本轮主报告为[research_pade_structure_round223_20261008.md](../../research/research_pade_structure_round223_20261008.md)。原数值目标active，无新数值无理性/线性无关性定理。存在性、增长上界、有限非零与无限非零分开登记。

## 数学稿、独审与历史输入

Root本轮实际FULL读四份最终数学稿的所有章节及量词，无截断：

| 稿件 | 最终bytes | SHA256 | Root的核验及独审 |
|---|---:|---|---|
| [全幂整模型](../../research/pade_integer_valued_denominators_round223_20261008.md) | 6110 | cea842775409706034017f9f1dbc7cbcde39ed6d331691dfa3d80588ab79c648 | Root自证D1–D7、保存后FULL复读；C独立FULL审阅 |
| [holonomic/G结构](../../research/pade_holonomic_structure_round223_20261008.md) | 11517 | 54eb60ab2835832855cd268c5dfb4318f2c25019a4589cf713483460fa00866a | Root全文、纸核关键参数/Taylor/closure；B独立全文并读必要primary选页 |
| [实际增长](../../research/pade_actual_growth_structure_round223_20261008.md) | 11630 | abc734b21846a221e76daf0941dff3f6e5dba47d723ad420f87d78ce9b60922f | Root全文、纸核轮廓与全部有限头、积分界、Stirling常数；A独立全文核验 |
| [无限非零接口](../../research/pade_infinite_nonzero_gate_round223_20261008.md) | 10073 | f12f19984ebdcff427ac336f48869057e48d57353b28e0ea1b620252d2889931 | Root全文、独立纸核两尺度全部pole分类与低jet/归一化det；不认证剩余层满秩 |

Root实际FULL读四份最终独审收据：

- [C审整模型](../../research/research_round223_integer_denominator_review_20261008.md)，2284B / `1a7789ff131bf8613dc6c27ce20a3307667871b2ef2e41cab3aa834bc1e31154`。
- [B审holonomic](../../research/research_round223_holonomic_structure_review_20261008.md)，4025B / `944315b055b2e6800c23ab9b945b530aa8158eebbe0e419b179008e306d2bcdb`。
- [A审growth](../../research/research_round223_actual_growth_review_20261008.md)，6094B / `9b8797bcb7e7852c880f71918985887360b65431046611451f96222f7e1eb1f7`。
- [Root审两尺度](../../research/research_round223_infinite_gate_review_20261008.md)，保存后实际FULL复读；最终身份由归档清单外部登记。

222原三周期包11908B / `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`及222全局报告9258B / `a29a0253b047859a035d8098aafb37cc1773177594548f9429185a239ffb6f32`，Root本轮实际FULL读取。222有限Δ₀补充3006B / `c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f`为上一轮已FULL核读身份，本轮复用其有限结论，未重跑producer/verifier。本轮新d_n整性更新旧安全费用，旧稿与旧manifest保持历史身份。

## Primary的实际读域

三份新PDF只有一份共享副本；下载不等于完整阅读。A与B的读域详见[lambert记录](lambert_reading_scope.md)和B收据；C与A的读域详见[dual记录](dual_source_reading_record_round223_20261008.md)和A收据。Root已实际FULL读两份作者阅读记录，但不将作者读域转记为Root自己的阅读。

Root从已下载Zudilin作者33页版本实际提取并FULL读[PDF第6、7、23、24页TXT](root_zudilin2003_author_pdf6_7_23_24.txt)，7135B / `75f74b067304997fa16673a8374890dcbf30676f864316cc509c72faa0409882`，并实际查看[第6页PNG](root_zudilin2003_pdf6.png)及[第23页PNG](root_zudilin2003_pdf23.png)。§7位于23–24页；Root未FULL读33页全文，也未借阅域外的§8条件。第6页式(17)最后求和漏掉a_l，前一行含a_l；实际像素确认，n=1,k=0即校准其局部符号/残数。Root新D3含该整数残数乘子，自含的全幂证明不依赖排印式。此观察仅针对冻结作者版本，不声称所有出版版相同，也不否定整篇文章。

Root实际FULL读保存的[DLMF E1 TEX](dual_dlmf_5_11E1.tex)及[E7 TEX](dual_dlmf_5_11E7.tex)两条公式。Root本轮未额外读其完整网页条件；C与A已实际读固定a,b/扇形条件并登记，growth独审只用正实轴固定参数。Root没有实际读Zeilberger/WZ全部primary或CDT第189页；后者由A/B明确登记，不由Root扩称已FULL原文。

一次宽泛rg误命中巨大整数JSON而截断，未作为FULL源读取或任何数学证据。随后按精确路径/扩展名读取所需最终文本。hash、文件库存和PDF提取仅为文档身份操作。

## 执行、归档与导航

本轮所有参与者数学程序总数**0**。没有CAS、递推猜测、creative-telescoping执行、矩阵程序、素数/参数扫描、数值积分、PSLQ或Lean；222两次有限精确程序属于222，未计入223。本轮新增PDF下载3份，DLMF短公式2份；PDF文字提取/两个PNG渲染、hash与文档归档不计数学程序。没有Git修改，本轮没有重新核云端仓库；222的公开SHA只作为已冻结历史输入。

四稿独审和报告独审的通过范围均有限：G定义存在性、完整安全整模型、真实余项上界、首残差局部整性；不覆盖具体operator、最小秩、无限非零、generic主奇点、strict比较或最终数值结论。Root保存主报告后实际FULL复读，随后FULL读独审收据；这些身份由[223manifest](../manifest_cdt_pade_structure_round223_20261008.json)登记。main只追加报告，严格保留222最终516292-byte前缀及其SHA `65918c974ba750a38b51f9507c1579819f5d36ffdf7a6c09250d5b293ddc01cb`。

正常下一次全局复盘228，允许226–230，结构性反例或连续两个完成轮次无核心进展即提前。本轮支付核心结构接口，未改复盘起点222。下一步优先实际operator/非零桥或剩余行精确非退化，不恢复旧模板或扫描为默认路线。原目标仍active。
