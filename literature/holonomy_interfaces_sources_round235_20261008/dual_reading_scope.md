# C235 实际来源与阅读范围

2026-10-08。对应新稿 `research/holonomy_fine_multimap_and_period_candidate_round235_20261008.md`。数学程序0；没有数值扫描、CAS、旧producer/归档执行或git mutation。新PDF0；当前CDT复用1原件；新TXT11、TEX1。文档提取共12次：11次保存下表选段，另一次PDF66–71 stdout作定位，后者工具输出截断，不注册为完整阅读。

## 1. 固定当前原件

`literature/global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf`，220页，3628820 B，SHA256 `9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c`。源URL：<https://www.math.uchicago.edu/~fcale/papers/L2chi.pdf>。234已对官方HTTP字节与此缓存作严格同件比较；235只核本地身份，没有重复下载PDF。它不是233使用的218页固定v2。

实际完整读取以下每个保存TXT的全部内容；只对选段登记FULL，不扩大为全部§6–8/§10或220页全文。主陈述和相关remark完整；长证明大多未读，不能以目录定位替代证明。

| 文件 | 实际PDF页 | B | SHA256 |
|---|---:|---:|---|
| dual_cdt_current_pdf01_toc.txt | 1 | 4051 | fd727da05823ea93450723750fbe31db9f8df40ebf1efd3ed0845ba32baf27d7 |
| dual_cdt_current_pdf02_toc.txt | 2 | 4142 | 17153ed8c6300bf7f39276a7d066b1a9898382dcd6119dd41f86ab7507ce92c1 |
| dual_cdt_current_pdf67_70.txt | 67–70 | 15873 | 6dd54a2f75f8a5ed6cf95290092bde47f60665be1430a60b006544047f2fbae5 |
| dual_cdt_current_pdf71.txt | 71 | 3581 | d41c2c53b09552c2e83877d2d7428881f6ea38b3e14148bc5454bccaa9797d28 |
| dual_cdt_current_pdf90.txt | 90 | 3932 | 0451877725325e8c197146a022866e152217769f80f808a487e6d2fdfb325f08 |
| dual_cdt_current_pdf91.txt | 91 | 3739 | c89af1b7cdb10c7ec147ae48c3eecad7d8aef6244d0804d99fbe33c4b9b28e67 |
| dual_cdt_current_pdf92_95.txt | 92–95 | 16464 | 0eb8a3f4974534ab9197deba6d209b4a7de4de311ebf0bc9bd62a0697dfe39b8 |
| dual_cdt_current_pdf114_116.txt | 114–116 | 11475 | 5fb3236a2f9077f006bb58eecbd6628410087c85b6dcabc05bf679561a00f5d8 |
| dual_cdt_current_pdf117.txt | 117 | 3709 | abcc260d830df9a1e3ab41779f2cfe893f04f8cfb68fb39b483e9259bfdb4b18 |
| dual_cdt_current_pdf123_126.txt | 123–126 | 18054 | c8ddb8196a9575156ee78a1504adb11a15328ba3bbfff3f39cd36ae0189aaabc |
| dual_cdt_current_pdf154_159.txt | 154–159 | 23093 | 7dfb5c57c8c61de903224d847805c04b3d608b04038181760f576f98bdd5fb92 |

PDF1 TXT与234同一页提取同字节，勿算成第二份primary。90包含Example6.8.6未经认证数值例及7.0.1起始，91包含完整结尾；114–117包含7.6.4权重系统的完整主陈述。123–126包含8.0.1、8.0.6的完整相关证明及后续能源principle起始；没有采用未读的8.1完整比较证明。154–159完整包含10.1.8的偶数J族声明、10.2.2及10.3；一般J族整性没有在此选段给出完整证明，本人也未复证或运行计算。

234已FULL读并保存的当前CDT29–34是数值覆盖背景；235回读工具输出部分截断，不增加235全文读取宣称。234结论范围保持不变：未认证全球新颖性；current2.11.17三项，不沿用旧v2四项为当前结果。

**I2 单项更正。** 初稿9565 B / SHA256 `f7d8cab8d192abef441fba67b17a667a78eb82fae9bccdd437fd08287c4231f1` 把(6.0.10)切换项误读为γ²/m²。Root指出并与A/B从当前PDF68 PNG独立视觉核定为γ²/m；本人随后实际视觉完整读取共享图 `literature/refined_arithmetic_sources_round235_20261008/packet_cdt_current-068.png`，245987 B / SHA256 `c3f639cb1ffe487b6a74df9da7de06f260ebe27d0efaa4b9cac06d443df06bbc`，确认两条等价分子均为1/m。只修I2这一分母，其余数学正文不改；本记录补记此次视觉核对与更正。复用PNG1、新PNG0；这不冒称本人FULL读同行235稿或其scope。更正后主稿与本记录再作实际FULL保存自读，数学程序仍0。

## 2. 唯一额外公式与仓库定位

web实际读 <https://dlmf.nist.gov/24.8> 的24.8.1、24.8.2及其条件：正整数n、0≤x≤1；24.8.2另含n0的补充条件但本文只用n1。以Bernoulli多项式B3(1/4)=3/64给β(3)=π³/32，同页even式给ζ(4)=π⁴/90。不是整章24的FULL阅读。新保存原公式 `dual_dlmf_24_8_E2.tex`（<https://dlmf.nist.gov/24.8.E2.tex>）实际FULL读；仅一次TEX HTTP下载、一次HTML webopen，无新PDF。

只读 `E:/codex-build/math`：`git status --short`无条目，HEAD `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`，origin `https://github.com/openai/math`。题目/README及Catalan TeX关键词输出只作locator，不采用其数学断言，不冒称全文/Lean认证或最新remote HEAD。另对研究目录做q2目标身份、J4候选历史关键词的定点定位；输出未命中精确公式不证明新颖。没有读旧W成本证明或重启旧任务。

## 3. 本稿新增纸面范围

源级条件模板(I1)、多图/凸性适用边界来自上述主陈述；K4在canonical x2的路径积分、五行完整源、居中antiderivative involution、q下降连接是本文自含纸推。Root独立纸核了K4连接值并提供involution方向，本人随后独立付清居中常数和完整q连接；这不是peer FULL审核收据。一般偶数J族全prime整性只采用原文声明，新的q联合整格、canonical填点、多图实际energy、global leaf和数值无理性均未付。

新稿及本记录保存后须实际FULL自读再报身份；不改234、main、manifest或旧冻结稿。
