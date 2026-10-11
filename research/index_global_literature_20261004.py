"""Build the reading map from checked PDFs; keep historical index entries."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / 'literature'
manifest = json.loads((LIBRARY / 'manifest_global_20261004.json').read_text(encoding='utf-8'))
groups = [
    ('holonomy', '算术 holonomy、模形式及 p-adic 对照'),
    ('motives', '动机、周期与调节子'),
    ('approximation', '单目标判据、几何积分与最新维数界'),
    ('modular', '模变换与奇数 ζ'),
    ('dirichlet', 'Catalan 与 Dirichlet L 值'),
    ('functions', 'G 函数：可用范围与反例'),
    ('disputed', '证明声称及批评稿：配对阅读'),
]
intro = '''# 全部奇数 ζ 与 Catalan：文献阅读地图

核对日：2026-10-04。本轮新增 **28份原始PDF**，复用两份已有PDF；以下30条均已保存且可解析。PDF原件保留原字节，未翻译、改写或去除出版方信息。文件名只帮助识别；固定版本、实际下载URL、检索时间、页数与SHA-256以 [归档清单](manifest_global_20261004.json) 为准。

建议先读 [总体研究判断](../research/odd_zeta_global_strategy_20261004.md)，再按以下顺序进入原文：

1. **统一对象**：Brown2014周期综述、Deligne2010 level4；区分已证结构与比较点泛型猜想。
2. **已成功的新证明机制**：CDT2025框架稿，再读CDT2024的L(2,χ₋₃)长文；先理解函数秩、分母与解析容量。
3. **纯目标的几何实例**：Dupont奇ζ动机、Eskandari–Murty–Nemoto Catalan动机最新v3；检查真实投影和整模型。
4. **逼近判据**：Zudilin2017；然后比较ζ(5)论文已有输入与跨权构造的缺口。
5. **防止误用通用定理**：Huber–Wüstholz的1-period范围、Rivoal的G函数特化反例。
6. **最新文献审计**：Lai2026正文Theorem/Claim区别，以及Sun/Wachs声称与批评的配对阅读。

“已证结果”表示原文定理的文献状态，不表示本项目已形式化复核整篇证明。动机结构、p-adic无理性、无理值个数、线性空间维数、指定实值无理性分别标记，不能互相替换。

'''
lines = [intro]
for category, label in groups:
    lines += [f'## {label}\n', '| 原件 | 版本 / 出版 | 页数 | 状态与阅读目的 |', '| --- | --- | ---: | --- |']
    for item in manifest['sources']:
        if item['category'] != category:
            continue
        if item['archive_status'] == 'failed':
            raise RuntimeError(f"Cannot index missing original: {item['file']}")
        path = LIBRARY / item['file']
        if not path.is_file():
            raise FileNotFoundError(path)
        text = f"[{item['title']}]({item['file']}) · [来源]({item['page_url']})"
        note = item['status'] + '。' + item['notes']
        lines.append(f"| {text} | {item['version']} | {item['pages']} | {note} |")
    lines.append('')
lines += ['''## 版本与验证注意

- Brown2012 Annals原件可直接打开；PDF含空打开密码的出版方加密标记。验证时仅在内存读取，保存字节完全不变。
- Borel1980为两页归档PDF，含NUMDAM封面；不要把PDF页数与文章的单页出版页码混同。
- Brown2014本地为arXiv v1。动机专题中另引作者v3的页码，不能直接套到本地v1；这是不同版本来源。
- Brown–Zudilin已有文件是2210.03391v3；本轮保留原件。Fischler已有文件标2109.10136v3、正文日期2025-12-01，而当前HTML正文日期不同；未覆盖文件，也未因版本号相同宣称字节相同。
- Calegari2004归档固定arXiv v1，但PDF正文内部日期为2018-10-28；两个日期都保留。
- 六篇代表原件的首页已渲染抽查，见 [验证图](../research/archive_validation_20261004.png)。PDF签名/解析/页数/SHA检查只确认归档完整性，不确认数学证明正确。

已有经典论文、ζ(5)形式化对象及p-adic资料继续保留在 [原有索引](README.md)。新增PDF来源配置为 [global_sources_20261004.json](global_sources_20261004.json)；下载与索引脚本位于research，均不覆盖已有PDF。
''']
(LIBRARY / 'reading_map_20261004.md').write_text('\n'.join(lines), encoding='utf-8')

index = LIBRARY / 'README.md'
old = index.read_text(encoding='utf-8')
old = old.replace('围绕 ζ(5)/ζ(7) 无理性的核心文献。按主题分组。', '''当前入口：[全部奇数ζ与Catalan的阅读地图](reading_map_20261004.md)与[总体研究报告](../research/odd_zeta_global_strategy_20261004.md)。2026-10-04新增28份开放原始PDF，补充动机/周期、算术holonomy、模形式、Catalan及G函数适用边界；本轮30条归档记录包含两份复用文件。

[完整归档清单](manifest_global_20261004.json)记录作者、固定版本、来源、页数与SHA-256。证明声称和批评稿成对保存；归档检查不等同于数学证明审定。下列经典资料和项目原件继续保留。''')
old = old.replace('| `ball_rivoal2001.pdf` | ⚠ 占位（付费墙未获取）；Ball–Rivoal, Invent. Math. 146 (2001) |', '| Ball–Rivoal 2001原文未取得 | Invent. Math.146(2001)；本库没有名为ball_rivoal2001.pdf的原件，不能引用占位文件。 |')
old = old.replace('≥ 2^{(1−ε)log(s/log s)/log log s} 个无理', '对每个ε>0及充分大的s，≥ 2^{(1−ε)log s/log log s} 个无理')
old = old.replace('Li Lai：ζ(5),…,ζ(35) 中至少两个无理（arXiv 2103.00904）', 'Li Lai–Li Zhou：ζ(5),…,ζ(35)中至少两个无理；同文β(2),…,β(10)中至少一个无理（arXiv2103.00904v2；发表于2022）。均不能指定ζ(7)或Catalan。')
old = old.replace('Li Lai：≥ 1.284·√(s/log s) 个无理（当前计数纪录，arXiv 2501.05321）', 'Li Lai：正文Theorem1.1给≥1.284579·√(s/log s)个无理，摘要取较粗1.284（arXiv2501.05321v2）；是个数，不是维数。')
old = old.replace('Fischler：Siegel 引理与奇数 zeta 值线性无关（JLMS 113, 2026）', 'Fischler：dim_Q Span{1,ζ(3),…,ζ(s)}≥0.21√(s/log s)，充分大的奇s（JLMS113,2026）；本地v3与网页正文日期差异见新清单。')
index.write_text(old, encoding='utf-8')
print('Indexed 30 validated PDF records; retained and corrected the historical index.')
