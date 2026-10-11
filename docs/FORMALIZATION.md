# 形式化资产与证明状态

本仓库同时保存上游证明、本地论文镜像和未完成的推广工程。**Lean 能编译带 `sorry` 的文件；编译成功与目标定理不依赖 `sorryAx` 是两项检查。** 本次仓库整理核对了源码及锁定配置，没有重新全量构建所有 Lean 依赖。

## 三个工程的职责

| 工程 | 保留内容 | 可以作出的结论 |
| --- | --- | --- |
| 根目录 [Zeta5Irrational](../Zeta5Irrational/) | Fauzan 论文的陈述镜像、局部证明、精确数值引理，以及上游桥接 | `zeta5_irrational_absolute` 直接采用上游完整证明；镜像中仍有待证输入 |
| [Zeta5-mo271](../Zeta5-mo271/) | mo271/Zeta5 的源码参考快照、证书表及生成脚本 | 上游声明 `Apery.irrational_five` 的形式化完整；实际根工程依赖由 Lake 按固定提交获取 |
| [Zeta7Formal](../Zeta7Formal/) | 保留原上游 `Apery`，并加入 b=8 的定义、局部引理及旧装配链 | ζ(7) 的推广尚未完成，当前全局参数并未统一 |

根目录 [Main.lean](../Zeta5Irrational/Main.lean) 中的绝对版先证明 `(riemannZeta 5).re = Apery.zeta5`，再调用 `Apery.irrational_zeta5`。它与本地 `zeta5_irrational` 是不同轨道：后者的归约已经写出，但依赖镜像中尚未证明的估计。不能把绝对版的完成状态转移到每条镜像陈述。

根镜像 [Propositions.lean](../Zeta5Irrational/Propositions.lean) 目前保留 20 处证明占位；装配链和许多数值、次数、赋值引理已真证。先前把 x 世界的 τ 恒等式移植到 t 世界的 μ 后产生的错误陈述已改写，源码还保留反例 `eq_3_3_false`；这是翻译错误，不能笼统归为原论文错误。

## 上游与原论文的差别

[上游 README](../Zeta5-mo271/README.md) 明确记录：使用 M=400、局部秩损失 r 代替 min(r,z)，并通过逐类部分分式处理赋值，而非逐字实现 Tate 代数路线。所需的是严格负净指数，未承诺复现论文的全部衰减常数。其记录的目标公理为 `propext`、`Classical.choice`、`Quot.sound`；依赖中存在的无关 `sorry` 不自动污染目标，应检查目标的实际公理依赖。

ζ(7) 的 [重启审计](../research/restart_analysis.md) 优先于旧工程中的乐观注释：Construction 使用 (40n,n,39n)，部分算术模块仍使用 37n；旧 Aeff=1.98 不能与新实侧 U=−2.15 合用。因此“只剩一个 sorry”不能解释为已闭合证明。已认证局部结果值得保留，但参数、完整整数预算和真实衰减必须在同一构造中重新闭合。

## 如何核验与扩展

构建与目标公理检查见 [复现指南](REPRODUCIBILITY.md)。后续研究报告中的周期投影、整模型、秩、停止证书及 Python 精确核验，除非明确指向具体 Lean 定理，否则属于书面或计算成果，尚未 Lean 形式化。

新增形式化时应写清目标定理、依赖链、参数和归一化，分别报告编译结果与 `#print axioms` 输出；不要以源码的占位数量代替数学可行性。保留已有反例、证书与上游说明，避免修复一条局部链时掩盖全局预算仍未闭合的事实。

上游源码的 Apache-2.0 许可保留于 [Zeta5-mo271/LICENSE](../Zeta5-mo271/LICENSE) 和 [Zeta7Formal/LICENSE](../Zeta7Formal/LICENSE)。论文、网页和文献原件遵循各自来源的权利与许可，不能仅凭代码许可推定其可自由再授权。
