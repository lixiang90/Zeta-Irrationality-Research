# 第222轮：公开源版本、实际证明架构与跨目标入口

2026-10-08。结论是：当前公开 OpenAI math 与本地只读 HEAD 一致；Catalan 源稿确实提供了与第221轮普通 cyclotomic source 不同的行列式架构，但这已是本项目冻结的来源，不能算本轮发现的新载体。Fauzan 的 ζ(5) 原文补清了完整 pole-class / polynomial-correction 接口，未改变旧 ζ(7) 的费用、能量或非零缺口。本轮仅保留一个有明确验收条件的 Padé 入口，不将它升级为主路线；没有取得新的数值无理性定理。

## 1. 当前公开状态与核查边界

只读仓库 `E:/codex-build/math` 的 `git status --short` 为空；HEAD 为 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，origin 为 `https://github.com/openai/math`。GitHub main 的原始 commit API 返回同一 SHA；提交日期为 2026-10-06T21:58:50Z。本轮没有 fetch、checkout、pull 或其他 Git mutation。[公开仓库](https://github.com/openai/math)、[固定提交](https://github.com/openai/math/commit/adc7f1241b42e322a6451854ab7e4b4c146bf78a)。

仓库目录和 README 只用于定位。实际数学阅读来自下面指定的正文；README 的 verification stage 和 `lean/docs/005.md` 的形式化范围是作者发布的状态说明，本轮没有执行 Lean、审查内核输出或复查所有依赖，不能据此宣布本轮完成形式验证。

| 原始来源 | 实际读到的结论与架构 | 本轮状态措辞 |
|---|---|---|
| OpenAI《Catalan's constant is irrational》，2026-09-24 | `introduction/foundations/odd-primes/nonvanishing/real-place/conclusion` 六个完整 TeX section；源稿以完整混合矩阵、局部格、素数尺度非零和能量比较证明 G 无理 | 有实际证明正文；本轮是架构审查，未 FULL 读 energy/certificate 两节或重跑证书，不冒称独立验证整篇 theorem |
| Fauzan《ζ(5) is irrational》，Zenodo v1，2026-09-17 | 固定 PDF 全部第1–13页：泛函、正 Gram、多项式归一化定义及全部 §3–§4 局部格；没有读完其全32页能量/结论/附录 | 原始预印本声称 ζ5 无理；公开 Lean 仓库声称完成形式化，本轮仅核发布范围，未验证 Lean 或全 proof |
| OpenAI《The Deligne–Drinfeld conjecture》，2026-09-23 | 完整 `01-introduction.tex`：有理分次 Lie 代数自由生成，奇权 holonomy 系数以收敛积分非零 | 不是各个奇 ζ 值的数值无理性/独立性 theorem；正文明确该非零不要求数值算术独立 |
| Fischler，arXiv:1904.02402v1，2019-04-05 | 固定 PDF 全部第1–15页，含 Prop.1、Thm.3、Lemma2 的完整三步 rank proof 与 Remark3；止于 §1.5 前部 | 周期序列 L 值的维数/个数结果及 Padé 系数空间接口；不指定 ζ7 或 β4 |

ζ5 发布状态核对使用了 [Zenodo 原始 v1](https://zenodo.org/records/22826419) 和[作者的形式化仓库](https://github.com/danromik/zeta5-irrationality)。本轮没有定位并全文核过一个比该 v1 更新的证明版本。OpenAI 目录中定位到的相关奇权结果是 Deligne–Drinfeld；未定位到指定 ζ7 或 β4 的数值证明，**这不是全球不存在此类新论文的证明**。[OpenAI 原始目录](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md)、[Deligne–Drinfeld 实际读的正文](https://raw.githubusercontent.com/openai/math/main/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/build/sections/01-introduction.tex)。

追加纠正旧 `zeta7_research_report.md` 的历史误述：Apéry 定理证明的是 ζ(3) 无理，不能将本次 ζ(5) 来源的结论归于 Apéry。旧稿的 Lean/零 sorry/扫描叙述均保留为历史记录，未作为本轮新验证事实。

## 2. 第221轮 cap 排除了什么

本轮先实际 FULL 读 [第221轮汇总稿](cdt_cyclotomic_symmetry_gate_round221_20261008.md) 和[共同图几何稿](cyclotomic_quotient_global_map_obstruction_round221_20261008.md)。它们限定在实际 `a(t)=atan(sqrt(t))/sqrt(t)`、`b(t)=Ti2(sqrt(t))/sqrt(t)`、相应奇偶 source 与给定 LCM / literal-power 类型；不是所有 cyclotomic、所有 trace 或所有 CDT 定理的 no-go。

对其中允许的同一共同图，实际分支的 -1 对数和无穷远 `t^(-1/2)log t` 项给出 `log ψ'(0)<7/2`。已付 odd 类型费用为 `11/3`，even 为 `61/16`；五行源 arbitrary-array 的前两列给费用下界 `18/5`（实际三列总费用仅已证 `18/5≤τ≤21/5`，不是等于 `18/5`），均不能形成正余量。对给定三行 `(1,a,o)`，ordinary Jensen 中 `J≥log ψ'(0)` 与费用 `88/27` 也不能满足所需严格比较。不能通过 t/x 坐标双倍账本或不计 literal n 因子宣称突破。

这项结论没有涉及下面两种不同对象：以全部系数 content 为核心的高次数数值多项式；以同时 Padé 余项及其整数消元为核心的多条线性形式。它也没有排除同一 rank 更强的联合整格。CDT 的 direct holonomy theorem 本身不要求先完成 Betti/Hodge 实现；必要桥仍是目标关系能否产生该定理所需的实际有理系数亚纯 overconvergent 芽，以及同一 source 的 strict gate。

## 3. 原始架构真正支付的收益

### 3.1 Catalan：两层局部信息、无界非零、实际混合外积

源稿固定 `n=48N,a=11N,b=7N,q=g=4N,h=2N,L=59N,C=63N,H=65N`。Chebyshev/Pell 接触身份先在完整 raw column pool 中消去 ζ2，随后整数滤波才定义实际 `Δ_N`。不能在另一组 Jacobi 限制或 tail projection 上沿用此身份的常数。[实际 foundations](https://raw.githubusercontent.com/openai/math/main/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex)。

奇素数格同时处理 `p^-2` 与 `p^-1` 层。列变换及逆都在 `GL(Z_p)`；先控制 raw pool 的全部最大子式，再用 Cauchy–Binet 转移到整数滤波矩阵。大素数区域中的 central column 扣除只使未知次层项乘 p 后变成整项，并没有把未知 residue 当作零。首层 rank 上界单独不能免除下一层。

非零性是反证关系点的无界序列命题：取 `N=p`，Frobenius 将 `48p` 阶矩阵约化为三个固定48阶有理矩阵，再用文中有限 mod101 证书得到对所有充分大素数 p 的非零。读到这些精确 proof 与证书表不等于本轮重跑了证书。

实处 proof 保留 near/far 两 sheet 的完整配置与 signed row determinant；Hardy 插值分支和 Hadamard 分支共同覆盖实际 Andreief 被积式。自由正 Cauchy 外积或 compact beta Gram 并不能代替这个混合矩阵的上下界。结论节报告的比较作用于同一

`log|Δ_p|/(48p)^2 − (1/2)log 2`：有限处下界 `>−2.29084`，实处上界 `<−2.2909`。本轮没有 FULL 审其 energy/certificate，故这些数值记为**原文比较结论**，不记成本轮重新认证常数。

可迁移的结构是“所有层的整格 + 实际关系点非零 + 同一完整外积”的组合。它已经存在于第218轮来源，不能因本轮重读就变成新 source，更不能给当前不同归一化的矩阵免费付清 fixedcarrier gate。

### 3.2 ζ5：whole-functional pole allocation 与外区 Qp-rank

Fauzan 使用 `K=40n,N=3n,h=37n` 及

`G_K(X)_{ij}=μ_X(D_N^6 t^(i+j)/D_K)`，

其中 `μ_X(t^e)=(-1)^e B_(2e+2)(2e+3)(2e+4)(2e+5)/24`，

`μ_X(1/(t+j^2))=j^4(X−H_j^(5))−1/4+1/(2j)`。

这定义了多项式部分与每个简单极点值，完整矩阵是 X 的 affine matrix。在 `X=ζ5`，令 `f(y)=(e^(2πy)−1)^(-1)`，正权是 `w5(y)=y^5 f^(4)(y)/12`，其中 `f^(4)` 是四阶导数，绝不是 `f^4`。原文 Prop2.2 的正性来自 `f^(4)(y)=(2π)^4 Σ_(ℓ≥1) ℓ^4 e^(-2πℓy)>0`，给实际 Gram 正性；原文 Thm2.1 声称相应整数多项式值以负 n² 指数衰减。

§3–§4 的关键是整个泛函的 distribution，而非孤立 residue：三阶导数/Bernoulli 部分与极点一起变换，缩放是 `p^-4`；inner 区用整 CRT pole-class basis，并同时比较包括0类的所有来源。outer 区写为 `A+p^-1 L`，需要的是 `rank_(Qp)L` 的界，随后整余子式 lemma 支付剩余损失，不能只看 `rank mod p`。这些估值保留全部 X 系数，包括常数项与 polynomial correction；只核一个 X 数值不构成 polynomial content。

这是与第221轮芽的秩—容量比较不同的算术接口，但本轮只读到归一化定义及局部格，没有重新证明其最终能量及严格比较。[Fauzan 固定原始 v1](https://zenodo.org/records/22826419)。

## 4. 为什么不把 μ7 重新升级为主路线

本轮实际 FULL 对照 `b8_arithmetic.md`、`b8_verdict.md`、`b8_phaseB_gate.md`、`zeta7_research_report.md`、`odd_zeta_global_strategy_20261004.md`、`zeta7_joint_lattice_20261004.md` 和第214/216轮 global。旧记录已经包含

`μ_7,X(1/(t+j^2))=j^6(X−H_j^(7))−1/6+1/(2j)`，

相应 Bernoulli polynomial part、`p^-6` distribution、正 Hermite/Gram、pole classes、polynomial-correction rank 费用，以及完整双参数 content 与 Schur 正性。由 Hermite 公式和六次分部积分得到 `w7(y)=y^7 f^(6)(y)/360`，f 同上，`f^(6)` 是六阶导数；一般 `f^(2m)(y)=(2π)^(2m) Σ_(ℓ≥1) ℓ^(2m)e^(-2πℓy)>0`。零矩分别是 `∫w5=5/12`、`∫w7=7/12`，与相应 Bernoulli 矩一致。这是导数核，不是 Bose 核的幂；这里只重新确认已知接口。[Hermite 原始公式](https://dlmf.nist.gov/25.11.E29)、[偶 ζ/Bernoulli 公式](https://dlmf.nist.gov/25.6.E2)。

| 旧对象 | 已记录的决定性缺口 | 这次 ζ5 primary 阅读是否改变它 |
|---|---|---|
| 早期 b8 `(40:1:39)` | 校正后的 `A_eff≈3.424178395`，已证书族能量约 `−2.1546`；finite scan 不能推出全参数 no-go | 否；ζ5 的 `p^-4`、四次核和原始常数不能转移为 ζ7 的 `p^-6`、六次核收益 |
| 第214轮非交错 Hermite ζ7 | 安全费用 cap `15949/840≈18.987`，实际实处上界约 `+6.696`，无限非零未付 | 否；这是另一归一化/模型，不能与早期 b8 数字拼接 |
| 第10/4双矩修正 | 既有完整系数联合抵消和 Schur 界；最佳修改本原值仍比原基准大约122.04；无一般尺度整除收益 | 否；“允许联合格”本身不是新发现，需新增跨尺度而非有限代表结论 |

因此 μ7/pole-class 路线登记为**既有 framework，降级保持**。本轮未给出新的完整局部格常数、同一对象的 n² 实处改进或关系点无限非零，不安排回转主线。旧报告9/28审计已收回“自由测度即已可行”等历史推断；有限测度族/扫描范围的失败不能升级为所有参数、所有核的不可能性。也没有重新确认旧 Lean 全链。

## 5. 唯一保留的条件入口：目标选择性 Padé 余空间

Fischler Prop.1 对固定周期 N、整数 `1≤r<a/(3N)` 给有限条整数线性形式，n 沿 N 的正整数倍增长，稳定系数空间仅对充分大 n 成立；系数高度 `≤β^(n+o(n))`，余项 `≤α^(n+o(n))`，其中

`α=(4e)^((a+1)/N)(2N)^(2r+2) r^(−(a+1)/N+4(r+1))`，

`β=(2e)^((a+1)/N)(r+1)^(2r+2)N^(2r+2)`。

同一实际周期 Fourier/奇偶投影及有理背景合并后，记整数系数行的 Q-span 为 `S_n`。原文 Lemma2 的稳定空间来自 `M P`，M 是与 n 无关的实际投影矩阵；Thm3 给未投影 P 在奇点 `z0` 处的 rank 下界 `q−#J_z0`（该 evaluation point 与上面的衰减 α 无关）。**不能把 P 的满秩移给 M P**：Remark3 明示某些 parity/period 参数有零行，且原文维数/计数定理不指定单个目标。[固定原始 v1](https://arxiv.org/abs/1904.02402v1)。

可审查入口是选择一个此前未付的新目标，例如指定 ζ7，先固定有限 `(a,r,N)` 或一个具证明的参数族，证明 `S_n` 与目标系数平面 `T=Q e_0⊕Q e_ζ7` 相交为整个二维平面。若用 χ4/偶 β，同样必须保留其他偶 L 值，不能因 Catalan 来源已有结论就直接删除它。这里的“平面”指系数坐标，不预设数值1、ζ7独立。

还必须付出消元高度。设 nuisance projection 的秩为 v，且 `dim S_n=v+2`。选择 v 个 nuisance 坐标及 v+2 个独立整数系数行，以 v 阶余子式构造两条独立、只支持 `(1,目标)` 的整数形式。固定 v 时乘子高度 `≤β^(vn+o(n))`，故其数值仅得到

`|Λ_n|≤(αβ^v)^(n+o(n))`。

若目标有理，这两条目标系数向量独立保证至少一条数值非零；固定目标分母给整数下界。因此 `αβ^v<1` 是上述**不缩放整数线性形式绝对趋零反证的充分条件**。它不是 CDT overconvergence 的必要条件，也不是所有投影方法的门槛。证明只用余子式消元与固定行数的三角不等式，不用程序，也不把逐次导数/消元视为无费用。

若把这些实际线性形式作为生成芽的系数，对其余 n 置0，上界给关系芽的 radius **下界** `(αβ^v)^(-1)`，目标系数生成芽的一般高度界给 radius 下界 `β^(-v-1)`；两个形式下界的比为 `β/α`。因此即使 `αβ^v≥1`，`α<β` 仍可提供相对 bound 的潜在收益，不能据此否定 holonomy-source 桥。**两个 radius 下界之间的严格比较不能推出实际 `R_关系>R_一般`**：β 若只是 coefficient upper，而未证 generic 实际增长率或不可去 dominant singularity，该解析收益尚未付。将它实现为 CDT 输入另需固定有理缩放、相应全分母与导数费用、实际共同亚纯图及目标关系保留；这些下界不是 actual radius 等式或已付新 domain。

这个直接线性形式接口确实区别于第221轮 common-map cap：它不要求普通 source 在共同图上 overconvergent，也不用正 Gram。但是一般多值 Padé 方法早已在旧 global 中登记；本轮新明确的是上述目标系数空间和完整消元高度验收口，**不是新 carrier 或新定理**。若仅有较大的 ambient rank，消掉许多 nuisance 的 `β^v` 可能完全吃掉绝对趋零收益；相对解析 gap 则需另外核查。下一窗口应分别审实际目标投影及完整高度、或保留较大 packet 后的真实 holonomy source 与相对解析 gap。未付相应桥前，不扩大参数搜索，不宣称比旧 Legendre 三行更可行。

## 6. 实际读域、归档与运行账

精确 bytes/SHA、各原件/摘录路径、公共版本及实际读域单存于 [新来源阅读记录](../literature/global_review_sources_round222_20261008/source_reading_record.md)。Catalan 六个完整实际读的 TeX section 与 Deligne–Drinfeld introduction 已从固定 HEAD 逐字复制到该新文件夹；既有 PDF 没有重复下载。新网络保存只有 commit API JSON 与三条 DLMF 原始公式，另保存已有 PDF 的 documentary text locator。

Catalan 未读的 energy/certificate、Fauzan 未读的第14–32页、Fischler 未读的第16页以后和全部 Lean/程序均明确排除 FULL 声明。Fischler 文件名含2020，但实际是 arXiv v1 2019-04-05，不能冒称后来作者修订版。初次合并读取曾截断的段落已另行补读；FULL 指本 agent 实际完整阅读，不替代任何独审。

数学程序运行 **0**；没有 grid、CAS、能量优化、PSLQ、有限矩阵证书重跑或 Lean build。只进行了只读 Git/原始发布核查、文本抽取/搜索、哈希与新文档保存。旧稿、main、manifest 均未修改。最终数值目标仍未完成；第221轮 ordinary source 的失败范围不扩大，固定载体的未付 gate 也没有被本次文献比较通过。
