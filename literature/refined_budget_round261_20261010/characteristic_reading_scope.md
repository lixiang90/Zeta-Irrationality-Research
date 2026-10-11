# 第261轮 characteristic 分支实际阅读边界

Author `/root/refined261_characteristic`，2026-10-10。

- 原始 CDT 固定 v2 PDF 仅本轮实际读物理89–96、113–120、121–124，共20页；不声称本轮读全部218页或整个物理89–124连续36页。
- 初始文档提取曾生成89–124五组文本以定位条款；未读97–104、105–112两组，随后只移除这两个本分支新建且未使用的提取文件。最终保留三组 FULL 实读文本。定页提取采用 PyMuPDF，文本保留原始数学排版字符包括PDF给出的空字节，属于忠实抽取，不用其乱码自行证明公式。
- 物理92、123页 PNG 实际视觉 FULL 查看，核实 subradii/slopes 条件、两种 correction 及严格分母。第123页 holonomic 备选条件原文含排版残余，不解释为放弃正分母。
- 两份260本地数学稿 FULL 实读；它们本轮用于固定对象和问题定位，不冒充本分支独审259全部历史资产。本分支独立纸核 t=∞ 的重复 root、F0、全部到达叶 log²及 Landau 粗界。
- Kim–Ma–Ma保存 primary 抽取的物理1–2页 FULL 实读，采用原文归一化及Landau结论；不声称读取该13页PDF全文。
- 目录全量 broad rg 定位曾发生输出截断，仅当 metadata locator，不算FULL。此前 grep 对PDF文本因空字节未输出，后用rg -a定位；FULL分类来自Get-Content完整返回及两页图像，非关键词定位。
- 无外部浏览/下载、数学/CAS/数值/Lean/图/参数/prime/Padé程序或扫描；无旧producer、archive、Git操作。Python仅文档提取、渲染、保存及hash/byte身份统计。
- 未改260原件或main/policy/manifest。本稿不完成active数值目标，不提出自动图搜索。

## 当前 primary PDF 身份（非全文阅读声明）

`literature/cdt2024_l2_chi_minus3.pdf`：4517169 bytes，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。

## FULL实读或视觉文件冻结身份

| 文件 | bytes | SHA256 | scope |
|---|---:|---|---|
| `research/global_review_mixed_analytic_round260_20261010.md` | 5716 | `0a5058ab7181b0a9ea0bc84f53866e0de6c492e7f6fd74bad85213930fe2906d` | text FULL |
| `research/global_review_architecture_round260_20261010.md` | 13020 | `d16d012f3f0c6b4a7232c6791e18ff4fdd01b684e1e0cfa7f9949a07ff0bda25` | text FULL |
| `literature/global_review_round260_20261010/analytic_kim_ma_ma_physical01_02.txt` | 5892 | `0e2b28083478dc40535ffe410585f62206aa74c476d8ec4e395282919c8a64f7` | text FULL |
| `literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical089_096.txt` | 21907 | `4fb8c07034b89ccc8fec6533e6131f52d19047d707767d7d790dfb591a5829f5` | text FULL |
| `literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical113_120.txt` | 18932 | `0701fbe82d48c45c78de12f091e84162ce3eee68341789f5422fd07672a1b05e` | text FULL |
| `literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical121_124.txt` | 11211 | `07e33ab1b4bb28fb4de0699ca66b08526503aa1b28a5012bef0bade59267f5b2` | text FULL |
| `literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical092.png` | 145773 | `a9e93a57017bd3507011ce29e96b30861a10f5be0f610bb16d9b6a3e415d8883` | visual FULL |
| `literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical123.png` | 179325 | `2ad5af2faa991e51a0a3cf1abcb599bc3474852f49790c16aa589d38ad647e29` | visual FULL |
