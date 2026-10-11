# B236 联合整格独立纸审

2026-10-08，C。**PASS，无必要修正。** 本审不新增数值无理性结论，数学程序0。

实际 FULL 最终对象：

- research/global_joint_lattice_review_round236_20261008.md：11134 B，SHA256 b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70，完整七节/J1–J10及准入判断。
- literature/global_review_sources_round236_20261008/packet_reading_scope.md：4736 B，SHA256 d485ac7c21bd70c49c53c14c95c651dae9b81582d1ceebd61b572d74ab0f5b63。
- 冻结235算术稿完整七节/C1–C10：8633 B，SHA256 2ff4e12e1965d03b49df9f2b201a955aa1b8449ea051b03580087b535c424d23。
- current CDT 保存的完整选页50–54及82–88，分别为18841 B/9789168f87f5db923d6a83335f091d8385412fb64679e20628e68f29b6aaadbd、28105 B/1113969c8cd48da5b78bd6f4f2b2e39feacb71c09de21ade2b45990b93a812f4。亲自全读 Theorem3.2.8、Lemma3.2.14 的完整条件，及§6.6/Remark6.6.15/§6.7；不是220页FULL，不继承B的其他旧稿读域。

**完整 prime-jet 核。** 同一 source 为三行全部 degree≤D 多项式，输出保留0,…,N。N<p≤2N−1 时，E的唯一 inner-p 项在k=(p−1)/2；积分外分母≤N<p，S∈Z[[u]]，g项经b_g固定整化。因此整tuple至多simple-p。将 J′+2J/(1−4u)=−2E 代入，确得 pT_N=3^ku^h(b+b_gaA)，h=(p+1)/2、A₀=−4。全部有限头及g项都已支付；不存在把单元层残差当full输出之偷换。

若m=N−h>D，b清前D+1项后，倒序a的r=m−D列恰给H_r=(A_(1+i+j))。r≤D+1保证矩阵实际使用的A下标≤m，未调用截断之外的系数。Rodrigues正交、所有分部积分边界和monic norm纸核正确；缩放8与4后
\[
 \det H_r=
 \frac{2^{3r^2+r}\prod_{j=0}^{r-1}(j!)^2}
      {\prod_{i,j=0}^{r-1}(2i+2j+3)}.
\]
p>4r−1时分子、分母均unit。这以精确rational公式取得Fp结论，没有把Q正性搬到Fp。m≤D由b直接onto；于是整个窗口的最大整值源格index精确为p^(N−h+1)。N=3D+固定常数的适用不等式对充分大D成立。

**全 prime 与 metric 边界。** E的q_E=D_(2N−1)和J的q_J=D_ND_(2N−1)由实际完整系数formula清分母；固定b_g清g头。窗口外的fallback保留2、3、全部prime powers，窗口内以完整kernel替换；有限CRT给实际full-rank格Γ。固定bad primes在精确求和中须排除或取N足够大，最终稿已明示。

PNT算式为：row基线15D²，替换掉6D²，真实window index添9D²/4，故logindex为45D²/4+o(D²)，同对象enlargement为15D²/4+o(D²)。45/4是Γ的完整safe上界，不是最大联合格的全prime最优lower，也不是τ。

J10矩阵给真实rank3的derivative closure，故所读Shidlovsky原文适用，degree≤D对应参数D+1。选择C₀≥3+C(g)即可由ord≤3(D+1)+C(g)得完整jet单射；作者没有领取N=3D+2精确临界单射。这个O(1)移动不改变局部窗口或CRT主项。

§6把同一BC metric/filtered evaluation的桥列为第一门槛正确：logindex不自动控制CRT基的实处height或graded leading-coefficient预算。balanced tensor只是一种可选实现，删项可能破坏source cancellation；direct source-joint criterion可另证。拟议2κ/9=5/2只作条件诊断，不是采用中的新判据。当前精确window已饱和，未付桥主要不在再找prime。一次有界237重构、无桥则停止的范围恰当；没有新数值定理、全joint no-go或已付strict energy。

目标稿及旧文件未修改；本审没有运行CAS、probe、扫描或旧producer。没有FULL复读B引用的222/229历史稿，未把其读域算成本审。新收据保存后实际 FULL 自读，最终身份另报。
