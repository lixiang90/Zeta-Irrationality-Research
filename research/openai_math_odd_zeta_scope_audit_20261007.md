# openai/math 本地仓库的奇数 ζ 特殊值范围核查

日期：2026-10-07。核查者：`/root/source_pencil_finalize`。只读对象：`E:\codex-build\math` 的当前本地 checkout。没有运行 Lean、Lake、仓库验证脚本或任何仓库程序；没有修改外部仓库。原有 level-7 研究已按用户要求暂停，本笔记不继续该研究，也不创建旧轮 FINAL receipt。

结论：**当前仓库没有声明已经解决全部 ζ(3)、ζ(5)、ζ(7)、… 的无理性，也没有找到 ζ(7) 无理性或 3ζ(3)+ζ(5) 无理性的主定理。** 当前相关新数值特殊值结果是 Catalan 常数 G 的无理性。仓库另有 zeta 无零点半平面结果，以及每个奇数权重一个生成元的 Deligne–Drinfeld Lie 代数结果；后两者都不是奇数 ζ 数值的无理性/线性无关性定理。

## 1. 仓库自己的范围与核查方法

根 README 当前说明 collection 有 722 manuscripts、372 families，结果处于不同 verification stages，并非所有论文都已有 Lean formalization。本人实际完整读入根 README、Lean README、Comparator README；检索 CONTENTS、overview.tex、lean/docs、formalization.yaml，并对 preprints 的 `.tex/.md`、Lean `.lean/.yaml/.json` 做关键词与具体 special-value theorem 检索。

查找包括 `ζ(3),ζ(5),ζ(7)`、对应 zeta 名称、odd zeta、irrational 与 zeta 的组合、polylog、period 和 linear independence。检索出现大量无关的 `ζ` 局部变量、`ζ(3/2),ζ(5/2)` 物理常数及 Dirichlet L 分析式；它们没有被算作 odd integer special-value arithmetic results。完整 source 检索已结束，不把仍运行的 search 片段当作最终证据。

以下路径/行号均指外部仓库实文件；本笔记中“未找到”仅限定本次读到的 checkout、catalogue 和 source search，不声称未来版本绝不会有新论文。

## 2. 三个容易混淆的实际结果

| 仓库结果 | 实际主声明 | 对奇数 ζ 无理性的含义 |
|---|---|---|
| Family003，Quasi-Riemann hypothesis | ζ 及所有 Dirichlet L 在 Re(s)>7/8 无零；另有11/12证明 | 非零点位置，不是特殊值是否有理 |
| Family005，Catalan | G=β(2)=L(2,χ₋₄) 无理 | 单个导子4的 Dirichlet L 值；不自动覆盖 ζ(7) 或全部奇数 ζ |
| Family008，Deligne–Drinfeld | rational grt/Ihara Lie algebra 在奇权重3,5,7,…自由生成 | Lie 元素的独立与生成；不是实数 ζ(3),ζ(5),ζ(7),…的数值独立 |

目录证据：`E:\codex-build\math\CONTENTS.md:66`、`:75`、`:84`（zero-free），`:125`、`:132`、`:134`（Catalan），`:182`、`:191`（Deligne–Drinfeld）；overview.tex 分别第82、86及相应 family008 entry。目录没有 ζ(5) 特殊值 family。

### 2.1 无零点论文

`preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\paper.pdf` 共199页；本人实际读 physical PDF1–2、4–6。PDF4 Theorem1.1 明确是 Re(s)>7/8 无零，principal pole允许；同页还说明 RH 本身未解决。Lean `docs\003.md:9–17` 同样限定 uniform zero-free / real-zero-gap 范围。

`lean\ComparatorChallenges\QuasiRiemannHypothesis.lean:5–6` 的 target 是
`(7/8)<s.re → riemannZeta s≠0`。
它没有说 ζ(n)∉Q。在 n≥3 的正实点，非零本来也不能排除一个非零有理数；因此不应把这个名称或“所有 Dirichlet L”范围变成 special-value arithmetic 结论。

### 2.2 Catalan 论文

`preprints\Catalans-constant-is-irrational-September-24-2026\paper.pdf` 共44页；本人实际完整读 physical PDF1–2。PDF1 Theorem1.1 **只有 Catalan’s constant is irrational**。主 source `build\sections\introduction.tex:16–18` 给同一声明。

PDF1中的 Apéry ζ(2)、ζ(3) 是历史比较（source introduction.tex:44–45），PDF2中的 ζ(2) 是需要消去的额外列（source :99–113）；不是另证明 ζ(5)/ζ(7)。核心阵列条目含 1,G,ζ(2)，Taylor contact 消去 ζ(2)，所以只假设 G∈Q 后 determinants rational。它不把不同 weight 的每个 zeta 值同时纳入 theorem。

`lean\docs\005.md:9` 明确 formalization scope 为这个 individual G。论文还提到其它 even β family 的历史结果，不能据此说所有 β(2k) 都在这篇论文中被证明无理。

### 2.3 Deligne–Drinfeld 的奇权重不等于奇 ζ 数值

`preprints\The-Deligne-Drinfeld-conjecture-September-23-2026\paper.pdf` 共41页；本人实际读 physical PDF1–2、38，另完整读 introduction source 与 holonomy source 中具体 coefficient 段。

PDF2 Theorem1.1、`build\sections\01-introduction.tex:49–62` 是

\[
\operatorname{Lie}_{\mathbb Q}\langle e_3,e_5,e_7,\ldots\rangle
\simeq (W,\{\ ,\ \}),
\]

其中 W 是满足 antisymmetry、three-term、four-strand pentagon 的 Lie polynomial solution space。主定理说明生成元存在、无 Lie relations、穷尽全部 solution space；其生成元并非 canonical。

holonomy coefficient确实含真正 ζ：source `build\sections\07-holonomy.tex:517–527` 计算 `[x^(n−1)y]Φ=−λ^nζ(n)`；`:540–543` 对奇n给非零 `2λ^nζ(n)`。但是 **PDF38、source :545–546 字面明确**：

> This only uses positivity of the real series, with no arithmetic independence assertion.

这句短引文直接排除了把该计算解释成 irrationality/LI 证明。证明由非零复 solution 的 rational-defined finite data 得到某个非零 rational Lie solution；不需要 ζ(n)本身有理或无理。motivic/Lie 自由性与 numerical period evaluation 的 injectivity是不同命题，论文没有补上后者。

Lean `docs\008.md:9–11` 进一步限定 formalization为 rational Lie solution space及weight completion，**regularized-transport proposition和graph-complex consequences不包含在 formalization中**。实际 final `lean\OAI\Algebra\Drinfeld\Completion.lean:559` 为 `main : MainStatement`，MainStatement中是 graded equivalence、Ihara bracket与continuous completion等；没有 numerical `Irrational ζ(n)` target。

## 3. ζ(3)、ζ(5)文件名与没有找到的命题

外部依赖 `Zeta3Irrational` 明确固定于 `lean\lakefile.lean:12–13`：
`https://github.com/ahhwuhu/zeta_3_irrational.git`，commit `e8785315a01c8fbcddaa0fc03b3c8b29a61bc1f1`。formalization.yaml:866–867 把它列为 builds-on。它是已有 Apéry ζ(3)形式化依赖，不是这次仓库声称新解决全部odd ζ的 theorem。

确有 `lean\OAI\NumberTheory\ZetaFive` 目录，但当前只包含7个 auxiliary modules：

- Identities/WeightedPNT、WeightedOrder、RiemannSqueeze、Endpoints。
- Arithmetic/LargePrimeWeighted、LargePrimeTable、LargePrimeIntegral。

这些都是 prime-weighted arithmetic/analytic辅助证明，没有 ζ(5) irrational final theorem。Catalan 的 `PrimeLimits\ContinuousWeightedPNT.lean:11` 实际 import上述 LargePrimeWeighted，保留了 `Zeta5` namespace。**目录名与 reused namespace不能当作已存在的 ζ(5) theorem。**

完整目标检索没有找到 numerical ζ(7) irrationality、all odd zeta irrationality、3ζ(3)+ζ(5) irrationality或 1/ζ3/ζ5/ζ7 全数值 LI 的 repository主声明。当前项目旧 ζ(5)论文不在这次仓库 catalogue的 special-value family中；本笔记不撤销也不替它作 proof audit。

## 4. Catalan 最末 Lean theorem 与 axioms 初步核对

真正 solution final proof在
`E:\codex-build\math\lean\OAI\NumberTheory\Catalan\Results\Conclusions.lean:11–23`：

```lean
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2) := by
  ...
```

该 proof 读入 FinitePlaceAssembly、PrimeNonvanishing、RealDeterminantUpper，假设 G rational后取足够大的非零 prime-scale determinant，再比较有限处 lower、实处 upper及严格 threshold gap得到矛盾。`Main.lean` import这一 result及各具体估计 proof；`IrrationalityAlias.lean` 仅给相同 theorem的alias。

Comparator `Catalan.json:2–5` 指定 challenge module、真正 solution module `OAI.NumberTheory.Catalan.Main`、theorem `OAI.InternalCatalan.catalan_irrational`。`:9–12` 只允许 `propext`、`Quot.sound`、`Classical.choice`，`:8` 的 `enable_nanoda=false` 意味不能说 nanoda 已启用检查。

`ComparatorChallenges\Catalan.lean:7–9` 中的 `sorry` 是**待 solution匹配的 challenge statement 占位**；不应当将它与 `Conclusions.lean` 的真正 proof混同。QuasiRiemann、DeligneDrinfeld challenge同样采用占位设计，solution模块另列。

本人用只读文本遍历，从 Catalan Main 递归读取本地 OAI import closure，共 **988个模块**，未发现显式 `axiom`、`sorry`、`admit` 或 `sorryAx` 标记。此为 static source audit，不是读完988个proof的独立数学验证，也不是运行 Lean kernel 的 transitive `#print axioms`。

此外还有外部 `PrimeNumberTheoremAnd.Catalan.Consequences`；其仓库依赖固定在 lakefile.lean:73–74，commit `c39a751132c88b6e8080b74c74023fd95b3d8be0`。Mathlib/Lean与这个外部依赖在本笔记没有重新编译/审计。所以准确表述是：**末 theorem类型与纸面主声明相符，local source没有静态显式未证占位，comparator配置仅允许标准axioms；本次没有重新完成机器验证。**

当前 formalization.yaml中没有查到 Catalan title/target条目，而 `docs\005.md`、Comparator和solution proof都有内容。这是该checkout的 catalogue覆盖差异，不足以反推proof无效；也不能只凭目录页就冒称本次重新验证成功。

## 5. 已读页域、范围与最终回答依据

本只读任务个人 actual PDF 页：Catalan1–2（2页）、Deligne–Drinfeld1–2/38（3页）、Quasi-Riemann1–2/4–6（5页），合计10 distinct页。Lean final declarations、配置、scope docs和具体source theorem段另实际读入；未把上轮研究的20/24页并入这个任务。

可以据此明确回答：**Catalan论文没有一劳永逸解决全部奇数 ζ。openai/math当前所列成果中也没有这样的 numerical theorem。** 若从它们的方法继续研究 ζ(7)，仍须为 ζ(7)本身或所需线性组合构造和证明相应 moment/projected determinant、whole integer model、nonvanishing与analytic/arithmetic margin；Catalan与odd-weight Lie结果不能直接替代这些步骤。这里仅解释逻辑范围，不恢复已暂停的原研究。
