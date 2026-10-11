# 偶数支集外 Racah 加强稿：实际全文独立审阅

2026-10-07。审阅者 `/root/scaled_root_finalize`，作者 `/root/masked_racah_finalize`。本轮548既存冻结记录只读；原实际对象、degree、格和费用保持。数学 producer execute/import/rerun0，旧成功及同行运行0，辅助素数扩表0。

## 1. 真实输入及阅读范围

实际完整读取 `research/cdt_odd_paired_offsupport_even_racah_strengthening_20261007.md` 的七节 E1–E24，候选物理 SHA `63bf66f49c2b37a905afd9ef93cbbe0dbca9c5fa8fe8b8cab9e33f706a4cc366`。实际完整回读冻结 `research/cdt_odd_paired_offsupport_racah_gate_20261007.md` 的七节 O1–O25，SHA `a3b89d1a210fa2a07fe55ab712e735447806d813821dcecf33810737f50c9e85`，包含本稿直接使用的有限 associated functional 和 Phi-kernel 双向同构。不冒称本轮重新全文读所有更早 fourth-normality、restricted-H 或其 producer；正常性沿已冻结 O2 使用，未重新执行验证。

实际完整文本读 Koekoek–Swarttouw 原件 PDF28、29、30 共3 distinct页：28含 Racah定义1.2.1，29含 norm及 recurrence1.2.2–1.2.4，30含完整差分方程1.2.5和本页其余公式。原件位于 `literature/cdt_paired_pearson_rankone_sources_20261006/koekoek_swarttouw1998_askey_scheme_report98_17.pdf`，SHA `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`。未新下载、未render，不把170归档页称为全文读取。审阅建立在实际读到的文本及纸面推导上。

## 2. 等号边界的 proper 证明通过

旧 O15 的严格 proper 条件只在2q<R推出；本稿没有直接沿用该结论。在新边界 R=2s≥4、q=s，对前q+2个 Delta有 degree≤R−e≤M，因此不同M节点上的求值kernel至多1维。它们属于原R列，因为q+2≤R。evaluated rank≤q使 polynomial span≤q+1，所以这些q+2个系数向量确实至少有一份非零 polynomial 恒等关系。这里没有错误使用 degree<M 的单射。

associated A_j 为 monic不同degree，故非零 coefficient relation 给非零 A'。starred pair coprime使关系准确为(A',B')=(hA*,hB*)、h非零。Pol(hR*)=0与R*存在非零 polynomial part矛盾，因此仍可推出严格 proper。正常profile排除R*=0，并给v≤t。此步骤未声称一般q>s也可用。

全部R列的关系空间E12准确：degree h≤R−1−t，且 Pol(hR*)=0当且仅当degree h≤v。反向展开 hA* 于A-basis后，其B部分因线性和proper条件准确等于hB*；nullity是min(v,R−1−t)+1，没有只证明一向包含。

## 3. gcd 分支计数与必要替代通过

E13的独立degree区间与冻结O19一致。在proper已另证后，e≥1迫l=s；e≥2、v≥1则迫rank≥s+1，所以e≥2只能v=0、t=s−e。

e=0时全部Delta degree≤R−2，R节点求值单射；关系维数为s，故 t=s−1时v=t，正常性给中央 A_(s−1)/B_(s−1)。t=s时v≥s−1，A*只在 A_s、A_(s−1)两项中，B由同一linear polynomial-part map确定。于是准确得到一份中央相邻两阶组合在全部节点为0。

e=1时删至多一个节点，M≥R−1；degree≤R−2仍严格小于M。全polynomial block rank≤s和E12迫v=t=s−1，因此至多漏一个中央多项式零点。

e≥2时v=0使全polynomial Delta-image degree≤R−2且dimension恰R−1。其剩余M节点求值kernel至多max(0,R−1−M)≤e−1，故evaluated rank≥R−e。rank=s迫e≥s；同时e≤l=s，得到e=l=s。因为l=s≥2，B准确degree s−1且非零，g degree s不能整除B，排除此分支。这没有把删除节点后的rank错误视为原rank相等：只需其不超过原rank。

E7因此是完整的必要替代。第二替代并未被作者宣称为独立充分条件；本审阅也不加强这一范围。R=4时q+2=R合法，最小窗口仍有效；R=2因前提失败已明确留在旧界。

## 4. 原 Racah 差分排除通过

实际取n=2r、R=r=2s、r≥4偶数，最高涉及degree至3r，完整处于已证fourth-normality窗口≤4r。不同i²节点在F_p互异。

从实读KS1.2.5代入第四族参数和k=x+r，E18的B、D及 eigenvalue全部匹配。在1≤k≤r−1，B的分子(k−5r)^3(k+r)和分母2k(2k+1)都为单位，D分母也正常；没有在k=0使用有理算子或丢掉jet。一个 eigenpoly若在相邻 omitted indices为0，可从后一正规index逐步向右传播到k=r，违背p_N(r²)=κ_N^−1≠0。

第二必要替代的r−1个零点必含相邻indices，r≥4时ceil(r/2)<r−1，故传播适用。第一替代若c=0同样直接排除；c≠0时只在interior1..r−2应用三个相邻值为0的组合。两个真实eigenvalue之差准确为−9r−2，绝对值小于p且不为0，所以中央低一阶在所有这些interior为0。r≥4给至少相邻1、2，继续传播矛盾。没有将单一eigenfunction法错用到整个组合，也没有在有限域引用实数正性。

## 5. 结论及限制

审阅结果 **PASS，无需数学修正**：每个实际辅助素数的 even r≥4 确得 rank E≥r/2+1；沿实际完整 Phi radical与gate-kernel的双向同构，corank Phi^[2r]≤r/2−1。与冻结odd界合并，r≥3时corank≤ceil(r/2)−1。

E24只下界完整Phi秩，不传给不同r维D_high压缩，不证明gate unit、K0=0、fixed rational source无限成功、whole-X无限非零或新的n²算术信用。相容式k+dPhi≤2r不能把dPhi的upper改充lower；作者已准确写出。没有新特殊值无理性、LI或Lean定理。本正式独审已实际全文回读并冻结，不pin未来receipt或可变总稿。
