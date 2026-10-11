# 多根势能稿的独立纸面审阅

2026-10-07，/root/source_pencil_finalize。实际两次完整读取[最终主稿](cdt_odd_paired_multiroot_potential_improvement_20261007.md)P1–P5（含P4a），最终字节SHA256 b0092b32bc7efefa80945c5e494ce11ed68ddc38fa0075964aaea4b82415029c；并实际完整读取冻结[coupled-Gram稿](cdt_odd_paired_coupled_gram_decay_20261007.md)C1–C10。本人不execute/import/rerun旧、同行或NEW数学producer；没有辅助素数扩表或Lean检查。本审阅是独立全尺度纸证核查。

结论：**PASS，未发现需修正的数学步骤。**

1. **同一模型与全n转移。** 原C3/C4剪切degree≤n−1，det1，确实保留whole-X D_A；不需要将新列当整数basis。P7逐mirror choice采用较小真实距离m−1/2，未误用镜像q值相等。沿竖线q的n^(4N)平方与head的n^(4Nn)平方准确抵消；P8新增项为−2Nn ε(ρ_n)，odd n差仅O(n)。固定根/正权重使所有maximizers统一避开根和无穷尾；舍入权重带来的V误差O(1/n)成立。初始N=0/N_i=0的有限例外由常数覆盖。Γ下率只用于liminf，未引入未证明的O(nlog n)误差。P9/P10不证明目标行列式非零。
2. **有限active peaks与严格改进。** F'(0+)=π/2，根附近各自log pole主导导数，尾部导数趋−2π；因此critical points位于有限个避根紧区间。每段导数实解析且非恒零，故全局maxima有限。将新根放在全部maxima上，使Fσ−Fρ在其共同邻域≤−1；补集通过上半连续性与coercive尾部得到严格gap η。P12混合估计同时覆盖邻域、补集及旧/新根的−∞值，确为全实轴严格改进，而非采样结论。
3. **有理参数。** 保持有限support数量、位置有界且严格正、权重有正下界时，最大点统一紧致；联合log上半连续及I连续足以得到limsup V≤V。因已有严格gap，足够近的正有理根/权重保持改进，权重和1及位置互异可以同时满足。不需要证明一般无限测度空间的连续性或最优measure存在。
4. **粗dual上界P4a。** 0<s≤1的积分公式及h≥−2−log2成立；s≥1时逐点ratio随s增加，h(s)≥h(1)=log2−π/2。有限log奇点可积，所以直接平均合法。Q''的上下界−7/2≤Q''≤−51/20和Q'(0+)=π/2给M0−∫Q<40/51−1/6；加2+log2<3得到123/34。该界仅限制本文特定保守V的信用，主稿明确没有把它当actual decay上界、算术cost下界或所有方法的no-go。

标准weighted Chebyshev的monic normalization与本题随ρ变化的J(ρ)不同；主稿未免费套用其equilibrium定理，也未交换未经验证的singular minimax。本人本轮PDF实读0，PDF下载/hash/页数及root实读范围由其来源收据承担；本审阅不把主稿所记PDF范围冒称本人已核查。

数学程序执行0、失败0、重跑0、旧/同行execute/import0、new auxiliary prime0、Lean0。审阅证明范围是上述全尺度转移、有限根严格改进、rational stability和粗dual bound；无新的特殊值无理性/线性无关性结论。最终来源receipt会pin本review与最终主稿；成功后本文只读。
