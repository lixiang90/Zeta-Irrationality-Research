# 本轮 \(K_2\) 缺口与端点 Bloch 类：文献阅读地图

日期：2026-10-04。对应[本轮进展](../research/odd_zeta_k2_gap_progress_20261004.md)。
新增 **8 份原始来源 PDF**，其中包含已发表论文、作者教材与讲义、官方参考快照。
全部保存下载的原始字节，验证 PDF 签名、解析、页数与 SHA-256，并渲染检查首页身份。
[manifest](manifest_k2_gap_20261004.json)保留实际 URL、固定版本、首次归档时间及哈希；
[可重跑来源配置](k2_gap_sources_20261004.json)与[归档脚本](../research/archive_k2_gap_literature_20261004.py)
不会覆盖已有原件。下载和首页核对不代表全文数学证明已审定。

## 1. 积分 transfer、特化与精确挠关系

| 原件 | 版本/页数 | 本轮实际用途 |
|---|---|---|
| [Rost：Chow Groups with Coefficients](rost1996_chow_groups_coefficients.pdf) | Documenta Math.1(1996),319–393；作者 PDF 76 页 | R1c、R3b/R3d、Theorem1.4：Milnor K 的整系数 restriction–corestriction 与 residue 相容 |
| [Weibel：The K-book](weibel2013_k_book_author_20130829.pdf) | 作者完整稿 2013-08-29，576 页 | III.7.3–7.4 的特化、整数有理函数域核；VI.5 的 Bloch/K₃ 背景 |

作者原始来源：
[Rost PDF](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)，
[Weibel 版本入口](https://sites.math.rutgers.edu/~weibel/Kbook.html)。
本库使用完整 K-book：印刷 pp.246–247 对应 PDF pp.254–255，
独立章节 PDF 页码不同，不混用。
这些定理给本构造 \(4T=0\)，未证明整系数 \(T=0\)，也不自动给指定算术模型的 Quillen lift。

## 2. Bloch 端点类与全部嵌入的识别

| 原件 | 版本/页数 | 本轮实际用途 |
|---|---|---|
| [Suslin：K₃ of a field, and the Bloch group](suslin1991_k3_field_bloch_group_english.pdf) | 英文 Proc.Steklov Inst.Math.183(1991),217–239；扫描23页 | Theorem5.2 的 \(K_3^{\rm ind}\)/Bloch 关系；区别整数定义与有理化 |
| [Neumann–Yang：Rationality problems for K-theory and Chern–Simons invariants](neumann_yang1997_rationality_k_theory_v1.pdf) | arXiv math/9712225v1，1997-12-04；12页 | §2 的 Borel 总调节子核恰为挠；Proposition2.1 的有理 Galois 下降 |
| [Zagier–Gangl：Classical and elliptic polylogarithms and special values of L-series](zagier_gangl2000_classical_elliptic_polylogarithms.pdf) | MPIM2000-9，作者稿38页 | §1 Bloch–Wigner、Bloch/K₃/Borel 已证部分，与高权 polylog 猜想分开 |

原始来源：
[Suslin 英文扫描](https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf)、
[原文/译文书目](https://www.mathnet.ru/eng/tm1914)，
[Neumann–Yang v1](https://arxiv.org/pdf/math/9712225v1)，
[Zagier–Gangl 作者稿](https://people.mpim-bonn.mpg.de/zagier/files/mpim/00-9/fulltext.pdf)。

Suslin 俄文原发表年是1990，英语译文1991，不能混写。
Neumann–Yang 论文发表于1995，本次固定其1997上传稿；
该稿明确纠正发表稿的一处五项关系印刷错误。
这里使用其 §2 的无条件数域结果，没有将 Chern–Simons 猜想或一般周期无理性猜想当成定理。

本轮从实际有限链平均及四个固定 \(i\) 的嵌入，识别端点差
\(\beta=-4{\rm res}[i]\)。这一识别仅在有理 Bloch 群中。
\(D(i)=G\) 非零并不能推出 \(G\) 无理；非零 rank-one 调节子格也不提供
\(q_nG-p_n\) 的近似族。

## 3. 曲线 regulator 与正则算术模型

| 原件 | 版本/页数 | 本轮实际用途 |
|---|---|---|
| [Dokchitser–de Jeu–Zagier：Numerical verification of Beilinson's conjecture for K₂ of hyperelliptic curves](dokchitser_dejeu_zagier2005_k2_hyperelliptic_v2.pdf) | arXiv math/0405040v2，2005-05-04；39页 | §3 的 tame/closed-cycle regulator 与 Bloch–Wigner 微分；数值研究不是本曲线非零性证明 |
| [Conrad：Integer ring of prime-power cyclotomic field](conrad_cyclotomic_integer_ring_handout.pdf) | Stanford作者讲义，无日期；2页 | Theorem0.1：\(\mathcal O_{\mathbb Q(\zeta_8)}=\mathbb Z[\zeta_8]\) |
| [Stacks：Resolution of Surfaces](stacks_resolution_surfaces_snapshot_20261004.pdf) | 官方章节2026-10-04归档快照；54页，页尾显示编译于2026-07-14 | Tags0ADX/0BGP 的解消适用范围和 Lipman 定理；保留 regular locus |

原始来源：
[DDZ 固定v2](https://arxiv.org/pdf/math/0405040v2)，
[Conrad讲义](https://math.stanford.edu/~conrad/154Page/handouts/cycint.pdf)，
[Stacks0ADX](https://stacks.math.columbia.edu/tag/0ADX)、
[Lipman0BGP](https://stacks.math.columbia.edu/tag/0BGP)、
[官方章节PDF](https://stacks.math.columbia.edu/download/resolve.pdf)。

DDZ 的出版版为 Compositio Math.142(2006),339–373，页数不等于此 arXiv 稿。
本轮实际下载优先的 v2 成功，没有回退出版 PDF。
Conrad讲义没有推断出版年；Stacks 为持续维护官方参考，原始字节快照与 SHA 固定，
在线章节号、版本以后可能变动。

算术模型报告使用 resolution 的存在；没有把全 codimension 1 tame 核
擅自识别成全局 Quillen \(K_2\)。二上的全赋值 tame 通过来自精确 \(4T=0\)，
不依赖仅画出部分 wild resolution 分量。

## 4. 复用文献与新阅读顺序

[Goncharov–Levin v4](goncharov_levin1997_zagier_elliptic_k2_v4.pdf) 在上一轮已存，
本轮直接复用 §1.6 的 Bloch–Suslin 背景；没有重复下载或修改原件。
前三版撤回状态与最终v4的区别仍见[上一轮地图](next_route_reading_map_20261004.md)。

建议按以下顺序读本项目证明及原件：

1. [退化报告](../research/odd_zeta_k2_descent_20261004.md)：先用对称有理商与特化判零类；
2. [regulator 报告](../research/odd_zeta_k2_regulator_20261004.md)：核算真实开放路径及边界；
3. [端点 Bloch 报告](../research/odd_zeta_bloch_boundary_20261004.md)：有限平均、普通点值、全部嵌入识别；
4. [垂直报告](../research/odd_zeta_k2_vertical_20261004.md)：全模型整性及其范围；
5. 回到[本轮进展](../research/odd_zeta_k2_gap_progress_20261004.md)中的相对参数族与定量预算接口。

上一轮ζ(7)系统秩、分母和预算结果保持冻结；本轮没有从权二识别推出其高权无理性。

