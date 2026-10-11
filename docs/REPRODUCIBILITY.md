# 复现指南

先阅读 [形式化状态](FORMALIZATION.md)，再选择要复核的具体命题。仓库中既有精确有理计算，也有浮点探索和有限扫描；有限样本通过不等于全尺度证明。本次整理没有重新全量构建 Lean，也没有将所有历史实验重新运行。

## 固定的 Lean 环境

三个工程均使用 [lean-toolchain](../lean-toolchain) 中的 `leanprover/lean4:v4.33.1`。根工程的 [lakefile.toml](../lakefile.toml) 与 [lake-manifest.json](../lake-manifest.json) 固定：

| 依赖 | 版本或提交 |
| --- | --- |
| mathlib | v4.33.1，`0df444a360eaa60ab8c11dca51a86af692955474` |
| Apery（mo271/Zeta5） | `00c55bdad2d9ce3870f1d5d73202297218d157b5` |
| PrimeNumberTheoremAnd | `04d81b2a68ea3548b9990813fdc463c78511f412` |

首次构建需要 Elan/Lake、网络和足够内存。保持清单，避免用 `lake update` 或上游最新分支改变复核对象。在仓库根目录执行：

```powershell
lake --version
lake exe cache get
lake build +Zeta5Irrational.Main
```

指定一个模块仍会构建其全部缺失依赖；首次运行可能很重。完整根工程用 `lake build`。`Zeta5-mo271/` 是参考快照，根构建实际使用 `.lake/packages/Apery/` 的锁定依赖；不要把两个目录的构建缓存混用。

构建后核验目标公理：

```powershell
@'
import Zeta5Irrational.Main
#print axioms Apery.irrational_five
#print axioms Zeta5Irrational.zeta5_irrational_absolute
#print axioms Zeta5Irrational.zeta5_irrational
'@ | lake env lean --stdin
```

前两个目标预期仅依赖 `propext`、`Classical.choice`、`Quot.sound`；本地镜像目标可能出现 `sorryAx`。该预期来自保留的源码及历史记录，需由当前环境输出实际确认。ζ(7) 工程可在其目录执行同类构建，但其待证输入和参数问题仍存在。

## 计算资产的恢复与最小复核

部分大 JSON 以原路径加 `.gz` 可逆压缩。当前原路径、原始字节数与 SHA-256 见 [资产清单](../archives/asset-manifest.json)。旧脚本通常仍读取 `.json`，运行前先恢复所需文件：

```powershell
python scripts/restore_assets.py --path research/需要复核的文件.json
# 或一次恢复全部压缩资产
python scripts/restore_assets.py --all
```

不要将示例占位文件名直接执行；从清单选择真实路径。恢复后原件应与清单中的原始摘要一致。文献原件保持原路径与原字节。累计日志、旧规则全文和一次性归档运行器保存在 [history.zip](../archives/history.zip)，可解压到独立目录追溯；请勿覆盖当前仓库或重跑旧归档程序。历史 manifest 的摘要不能认证本次新导航文本。

Python 的历史实验没有统一版本锁；脚本按需使用标准库、SymPy、mpmath、python-flint 等。应记录 `python --version` 和实际依赖版本，再判断输出差异；不要假装所有脚本都在一个已锁定环境中复现过。

标准库入门复核可运行：

```powershell
python Zeta5-mo271/scripts/appendixB.py
```

它重算论文 Table 3/4 及有理积分，同时含有限抽样诊断；应分别阅读这些输出的证明强度。更多上游脚本见 [脚本说明](../Zeta5-mo271/scripts/README.md)。

SymPy 证书脚本常会重写邻近 JSON。要保留冻结输出，可复制报告与脚本到临时目录，再运行：

```powershell
$runRoot = Join-Path $env:TEMP ("zeta-repro-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $runRoot | Out-Null
Copy-Item -LiteralPath research/period_holonomy_integral_models_20261005.md,research/period_holonomy_integral_models_20261005_verify.py -Destination $runRoot
python (Join-Path $runRoot 'period_holonomy_integral_models_20261005_verify.py')
```

预期 `all_checks_passed` 为 true。它核验固定代数恒等式及有限系数诊断；全尺度分母结论需要配套报告中的证明。复现报告应记录输入摘要、软件版本、命令与输出，以及未覆盖的假设。归档完整、脚本成功和数值无理性证明完成是不同结论。
