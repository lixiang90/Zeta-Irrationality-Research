# R₀ 的实际 exterior packet：秩九、完整秩十与第二端点旗标

日期：2026-10-06。NEW 全尺度纸面证明。主记录 §§73–78、root当前六秩审阅及delivery scope已实际读取；旧 MD/PY/JSON/manifest 与同行producer全部只读，没有创建或执行数学producer。本文不把actual compact scalar与analytic \(\Psi\) 的剩余三周期差置零，不声明新的数值无理性/线性无关性。

本稿证明一个真正 nine-dimensional exterior packet，加入常数1后实际完整秩十，给其有理connection和条件明确的全部prefix整化。原minor模型的安全费用为 \(D^{10}\)，实际辛配对模型可严格改进为 \(D^7\)，五个mixed rows仍为 \(D^6\)。它确实保留 \(\alpha_0\) 的非恒定周期方向，且不存在把任意参数变化解释成horizontal tensor automorphism的免费gauge。全部 transported conifold monodromy stabilizer仍对参数不敏感；raw jet poles则有额外值敏感条件，不能混同。辛配对模型填平了这些fixed-branch poles，因此其conifold填点仍对值盲。实际原点最高log旗标给一个唯一选中 \(\alpha_0\) 的第二端点关系，需与CDT费用、原Betti格另行接合。

## E1. 已核对象与完整jet坐标

取
\[
 P=\theta^4-x(\theta+\tfrac12)^4,
 \quad\theta=x\partial_x,\quad t=1-x,
 \quad\Psi=W-\frac{\pi^4}{16}y_0,
 \quad P\Psi=\frac{\sqrt{x}}{16}.
 \tag{E1}
\]
冻稿 [conifold arithmetic center](cdt_odd_conifold_arithmetic_center_20261006.md) 的三个homogeneous germs \(g_0,g_1,g_2\) 与particular \(h\) 具有有理Taylor coefficients，前三初值分别为单位向量和零，且
\[
 \Psi=h+\alpha_0g_0+\alpha_1g_1+\alpha_2g_2,
 \qquad\alpha_0=\frac{\pi^2}{16}(R_0-M_0).
 \tag{E2}
\]
令
\[
 Y_f=(f,\theta f,\theta^2f,\theta^3f,\beta\sqrt{x})^T
 \quad\text{当 }Pf=\beta\sqrt{x}/16.
 \tag{E3}
\]
对homogeneous \(g\)，记 \(Y_g\) 的最后坐标为0。全部这些向量满足同一个 \(\mathbf Q(x)\) connection
\[
 \theta Y=A Y,\qquad
 A=\begin{pmatrix}
 0&1&0&0&0\\
 0&0&1&0&0\\
 0&0&0&1&0\\
 x/(16t)&x/(2t)&3x/(2t)&2x/t&1/(16t)\\
 0&0&0&0&1/2
 \end{pmatrix}.
 \tag{E4}
\]
该rank-five extension实际非分裂，homogeneous rank-four层的connected Galois/monodromy closure为 \(\mathrm{Sp}_4\)；这是冻结 [Kummer 接口](cdt_odd_R0_kummer_period_interface_20261006.md) §4及已核P₄输入，不重跑其producer。

## E2. 一个只依赖α₀、不是常数平移的实际wedge

定义
\[
 \Phi=Y_\Psi\wedge Y_{g_1}\wedge Y_{g_2}
      \in\bigwedge^3\mathbf C^5.
 \tag{E5}
\]
线性性严格给
\[
 \boxed{\Phi=\Phi_h+\alpha_0\Phi_0,\qquad
 \Phi_h=Y_h\wedge Y_{g_1}\wedge Y_{g_2},
 \quad\Phi_0=Y_{g_0}\wedge Y_{g_1}\wedge Y_{g_2}.}
 \tag{E6}
\]
\(\alpha_1,\alpha_2\) 消去的是完整全函数，不只是端点Taylor。\(\Phi_0\ne0\)，且它不是constant function vector：它属于不可约rank-four homogeneous exterior层。

以 \(0,1,2,3,4\) 标记E3五个坐标。每个 \(\Phi_{ijk}\) 是对应三行的真实determinant。由 \(\theta f(1)=-[t]f\)、\(\theta^2f(1)=2[t^2]f-[t]f\)，
\[
 \boxed{\Phi_{012}(1)=-2\alpha_0.}
 \tag{E7}
\]
所以这个scalar仍检测实际目标端点。

## E3. 实际symplectic constraint及九行有理系统

冻结Yukawa的concomitant在homogeneous jet空间为
\[
 C(f,g)=Y_f^{(4)T}B(x)Y_g^{(4)},
\quad
 B=\begin{pmatrix}
 0&x/2&x&-t\\-x/2&0&t&0\\-x&-t&0&0\\t&0&0&0
 \end{pmatrix}.
 \tag{E8}
\]
对homogeneous解它是flat symplectic form。conifold端点公式
\[
 C(f,g)(1)=f_0(2g_2-3g_1/2)-g_0(2f_2-3f_1/2)
\]
给 \(C(g_1,g_2)=0\)、\(C(g_0,g_1)=-3/2\)、\(C(g_0,g_2)=2\)。因此 \(g_1,g_2\) 是一个真正Lagrangian二平面。

最后坐标参与的六个三minor恰为
\(\Phi_{ij4}=\sqrt{x}(\theta^ig_1\theta^jg_2-\theta^jg_1\theta^ig_2)\)。由isotropy得到实际rational constraint
\[
 \boxed{\frac x2\Phi_{014}+x\Phi_{024}
             -t\Phi_{034}+t\Phi_{124}=0.}
 \tag{E9}
\]
保留四个pure triples \(012,013,023,123\)，以及五个mixed triples
\(024,034,124,134,234\)。删去的原coordinate满足
\[
 \Phi_{014}=-2\Phi_{024}+(2t/x)\Phi_{034}-(2t/x)\Phi_{124}.
 \tag{E10}
\]
新基点 \(t=0,x=1\) 上这没有除 \(t\) 的问题。

完整connection不需要猜81个matrix项：对所有递增triple \(I=(i_1,i_2,i_3)\)，精确规则为
\[
 \theta\Phi_I=\sum_{r=1}^3\sum_{k=0}^4
   A_{i_rk}\Phi_{i_1\ldots i_{r-1}k i_{r+1}\ldots i_3},
 \tag{E11}
\]
重排index用wedge符号，重复index的minor为0，再用E10消去014。这是一份明确的九行 \(\mathbf Q(x)\) 系统，等价于E4的第三exterior power在E9 kernel上的restriction。E9的derivative为其自身乘 \(1/2\)，故kernel确实horizontal。下节证明这里不是仅有abstract上界九。

## E4. 原extension的实际full translation group

令 \(G\) 为E4 monodromy的Zariski closure。homogeneous层与Kummer quotient的共同semisimple projection是
\(G_0=\mathrm{Sp}_4\times\mu_2\)：其identity component到connected \(\mathrm{Sp}_4\) 满射，有限character在identity component上为1，而绕0的平方根有负号，故得到全部两个components。

这个projection的kernel是additive homogeneous四空间中的一个 \(G_0\)-stable linear subgroup \(N\)。特征零的closed subgroup of additive vector group是linear；标准 \(\mathrm{Sp}_4\) 模不可约，所以 \(N=0\) 或 \(\mathbf G_a^4\)。若为零，\(G\simeq G_0\) reductive，其五维representation完全可约，E4 extension分裂，与实际Kummer稿的非分裂矛盾。因此
\[
 \boxed{N=\mathbf G_a^4.}
 \tag{E12}
\]
在一个complex Levi splitting中，\(G=\mathbf G_a^4\rtimes(\mathrm{Sp}_4\times\mu_2)\)，translations任意改变particular vector的homogeneous分量，固定homogeneous solutions。这个complex splitting只用于representation proof，不是integer gauge。

E4是regular singular，Fuchsian monodromy的closure给其实际differential Galois group。也可直接用此monodromy closure的complete reducibility论证E12；没有把nonzero extension的抽象Ext维数当成实际radical。

## E5. 实际orbit与coordinate functions恰九维

记homogeneous四维solution空间为 \(V\)，Kummer quotient为 \(\chi\)。完整 \(\bigwedge^3E\) 有canonical sequence
\[
 0\to\bigwedge^3V\to\bigwedge^3E
   \to\chi\otimes\bigwedge^2V\to0.
\]
E9的九维kernel \(\mathcal W\) 准确为
\[
 0\to\bigwedge^3V\ (\dim4)\to\mathcal W
   \to\chi\otimes\bigwedge^2_0V\ (\dim5)\to0.
 \tag{E13}
\]
\(\bigwedge^3V\simeq V\) 与primitive \(\bigwedge^2_0V\) 均为不可约 \(\mathrm{Sp}_4\) 模，彼此非同构。

实际 \(\Phi\) 的quotient是非零 \(g_1\wedge g_2\)，其 \(\mathrm{Sp}_4\) orbit span为全部primitive五空间。对任意translation \(a\in V\)，
\[
 u_a\Phi-\Phi=a\wedge g_1\wedge g_2.
 \tag{E14}
\]
这不是恒为零；其非零bottom方向的 \(\mathrm{Sp}_4\) span为全部不可约四空间。故实际orbit span包含bottom四空间且满射quotient五空间，恰为九维。Monodromy Zariski dense使实际continued branches的span同样九维，不是只计算possible representation dimension。

进一步，保留的九个coordinate functions在 \(\mathbf C(x)\) 上独立。若有 \(\mathbf C(x)\) row relation，Galois automorphisms固定该row，故它杀全部九维orbit；exterior fundamental matrix在E9 kernel上可逆，迫row为0。因此
\[
 \boxed{\operatorname{rank}_{\mathbf C(x)}
   (\Phi_{012},\Phi_{013},\Phi_{023},\Phi_{123},
    \Phi_{024},\Phi_{034},\Phi_{124},\Phi_{134},\Phi_{234})=9.}
 \tag{E15}
\]
对任意参数 \(q\in\mathbf C\)，\(\Phi(q)=\Phi_h+q\Phi_0\) 同样满足这结论；translation group使所有这些vectors处于同一实际Galois orbit。

scalar \(\Phi_{012}\) 的最小order也恰九。对此coordinate的solution-to-function map的kernel是G-stable。其bottom restriction非零，因为 \(\Phi_{0,012}(1)=-2\)。不可约bottom使kernel与bottom的交集为0；如果kernel的primitive quotient非零，则为全部五空间，E14的translation action迫kernel含非零bottom，矛盾。所以map injective。scalar的continued conjugates有九维span，故order≥9；九行rational system给≤9。以E11的observability rows递推、在九阶时解linear relation即可在 \(\mathbf Q(x)\) 中给一份annihilator，不需有限样本猜算子。

## E6. 常数1是实际第十行；不存在值改变的horizontal tensor automorphism

E13与dual derivative module的composition factors只是不可约4和 \(\chi\cdot5\)，无trivial factor。若常数函数1位于E15九行span，其 \(\mathbf C(x)\cdot1\) 会给trivial differential submodule，矛盾。因此
\[
 \boxed{1\text{和E15九个functions完整线性无关，实际秩十。}}
 \tag{E16}
\]
有限代数覆盖仍保留connected \(\mathbf G_a^4\rtimes\mathrm{Sp}_4\)，同一orbit和composition-factor论证保持九/十。

同时 \(\operatorname{End}_G(\mathcal W)=\mathbf C\)。任一endomorphism在不可约bottom和quotient上为两个scalars \(a,b\)，非零translation map迫 \(a=b\)；余下可能的off-diagonal map属于 \(\operatorname{Hom}_G(5,4)=0\)。于是endomorphism只是scalar。因为每个 \(\Phi(q)\) 的quotient相同且非零，能把它变为 \(\Phi(q')\) 的horizontal module automorphism只能为identity，迫 \(q=q'\)。有限cover同样成立。

这与E15的Galois translation不矛盾：\(u_a\) 是differential-field automorphism，会共轭G-stabilizer；它不是commute整个monodromy/G的 \(\mathbf Q(x)\) horizontal tensor automorphism。因此不能用一个真实arithmetic gauge把不同目标值全等同；下一节说明某些具体local填点数据仍盲。

## E7. 条件α₀∈K下、保留全部tensor费用的prefix模型

按冻结FR原件Thm1–2，\(h\) 用order5给 \(D_{n+b_h}^4C_h^{n+1}\)，三个homogeneous \(g_j\) 用order4给 \(D_{n+b_g}^3C_g^{n+1}\)。conifold exponents均整数，\(b=1\)。这些germs的G-function/local normalization已在冻结中心稿及本代理上一稿实际核准；有限坏素数的 \(C\) 指数保留。

取 \(b_0=\max(b_h,b_g)\)、正整数 \(C\) 为 \(4,C_h,C_g\) 的共同倍数；若 \(\alpha_0\in K\)，选正整数 \(d_0\) 整化 \(\alpha_0\)。用E6表达actual \(\Phi\)，不需要 \(\alpha_1,\alpha_2\) 代数。

pure triple系数是 \(h\) 的一个jet乘 \(g_1,g_2\) 两个jets，再加 \(\alpha_0\) 乘三个homogeneous jets。前者pay \(D^{4+3+3}=D^{10}\)，后者 \(D^9\)。\(\theta^j\)、\(j\le3\)，在t坐标为integer-coefficient polynomial times derivatives，只读到 \(n+3\)，factorial ratios为整数。三项convolution的exponential factors相乘是 \(C^{n+12}\)，不是错误地把三个独立prefix费用再记成 \(C^{3n}\)。因此四个pure rows有安全prefix
\[
 \boxed{\Delta_N^{\rm pure}
 =16d_0D_{N+b_0+3}^{10}C^{N+12}.}
 \tag{E17}
\]
五个mixed rows是 \(\sqrt{1-t}\) 乘两个homogeneous jets，有
\[
 \boxed{\Delta_N^{\rm mixed}
 =16D_{N+b_0+3}^{6}C^{N+12}.}
 \tag{E18}
\]
algebraic twist的 \(4^n\) 已由 \(4\mid C\) 支付。E17共同覆盖全部九行及常数1，主率≤\(10+\log C\)。每一条是全部 \(0\le n\le N\) 的prefix命题；没有运行小样本作为证明。

这些不是effective最小denominators或CDT optimum；mixed/pure split仅说明一份真实species array。E9 elimination保留原minor坐标，E10的 \(1/x\) 只在connection中；没有改用超越period gauge。若需要actual Betti integer matrix、finite-place Smith和matching improvements，必须另核，不能从rank9/10免费继承旧原点预算。

## E7a. 实际辛配对模型：四行费用从D十严格降为D七

E17是原三minor格的安全证明；以下改进另给全尺度整化证明，不把rational gauge当成免费整数comparison。对四个pure minors施加E8的点态symplectic contraction，定义四分量向量
\[
 Z=C(\Psi,g_1)Y_{g_2}^{(4)}-C(\Psi,g_2)Y_{g_1}^{(4)}.
 \tag{E18.1}
\]
这里 \(C(g_1,g_2)=0\)，故正是四空间的
\(c_B(Y_\Psi^{(4)}\wedge Y_{g_1}^{(4)}\wedge Y_{g_2}^{(4)})\)。相对于E15的pure顺序，其matrix准确为
\[
 c_B=\begin{pmatrix}
 t&0&0&0\\-x&t&0&0\\x/2&0&t&0\\0&x/2&x&t
 \end{pmatrix}.
\]
这不引入任何period constant。因为 \(\operatorname{Pf}B=-t^2\)、\(\det c_B=t^4\)，它在 \(t\ne0\) 可逆；其inverse含 \(t^{-1},t^{-2}\) 极点（第三阶项相消）。因而这改变了conifold的holomorphic lattice，不声称preserve原integer格。

concomitant identity \(\theta C(f,g)=(Pf)g-f(Pg)\) 与E8端点值给
\[
 \begin{split}
 C(\Psi,g_1)&=-\tfrac32\alpha_0+F_1,\qquad
 C(\Psi,g_2)=2\alpha_0+F_2,\\
 F_j(t)&=-\frac1{16}\int_0^t
             \frac{g_j(u)}{\sqrt{1-u}}\,du\in\mathbf Q[[t]].
 \end{split}
 \tag{E18.2}
\]
所以 \(Z\) 的第 \(j\) 行、\(0\le j\le3\)，准确为
\[
 Z_j=F_1\theta^jg_2-F_2\theta^jg_1-2\alpha_0\theta^jv,
 \qquad v=g_1+\tfrac34g_2.
 \tag{E18.3}
\]
\(Z\) 全函数只依赖 \(\alpha_0\)；没有要求另外两jet代数，也没有除以 \(\pi^2\)。

给出所需denominator证明。\((1-t)^{-1/2}\) 的第k项分母整除 \(4^k\)。\(F_j\) 的第n项（n≥1）是n−1次convolution再除 \(16n\)。令 \(D=D_{N+b_0+3}\)，各 \(g_j\) 项由 \(D^3\) 整化，\(n\mid D\)，故 \(F_j\) 全部prefix由 \(16D^4 C^{N+2}\) 安全整化。乘 \(\theta^jg\) 再付 \(D^3\)；convolution indices之和不超过N，jet只增加固定不超过3的位移，指数费用仍是 \(C^{N+12}\)。\(\alpha_0\theta^jv\) 项的 \(D^3\) 费用也被覆盖。因此四个Z行有严格全prefix模型
\[
 \boxed{\Delta_N^{Z}
    =16d_0D_{N+b_0+3}^{7}C^{N+12}.}
 \tag{E18.4}
\]
这里需按每个coefficient的convolution sum使用指数费用；若只机械相乘两个统一prefix的 \(C^{N+2}\)、\(C^{N+4}\)，会错误产生 \(C^{2N}\)。上述all-coefficient证明避免这个损失。五个mixed rows仍保留E18的 \(D^6\)；两组加常数1的共同主率安全为 \(7+\log C\)。可去掉 \(C_h\) 而取新的 \(4,C_g\) 共同倍数；为便于与E17比较，本稿保留原更大的C。这不是effective最优或finite-place Smith结论。

定义新的九行packet为四个Z行和E15的五个mixed rows。令 \(T=\operatorname{diag}(c_B,I_5)\)，其完整rational connection明确为
\[
 A_Z=(\theta T)T^{-1}+TA_9T^{-1},
 \tag{E18.5}
\]
其中 \(A_9\) 由E11指定。E15–E16与invertible rational map给实际rank9、含1rank10，全部有限cover同样；End与origin旗标结论也保持。scalar \(Z_0\) 的最小order也是9：其solution evaluation在bottom上为非零函数 \(-2v\)，E5的同一kernel/translation argument适用。

canonical conifold上 \(F_1(0)=F_2(0)=0\)，且
\(\theta v(1)=-1\)、\(\theta^2v(1)=1/2\)、\(\theta^3v(1)=-1/8\)。于是目标数据准确为
\[
 \boxed{(Z_0,Z_1,Z_2,Z_3)(1)
       =(0,2\alpha_0,-\alpha_0,\alpha_0/4).}
 \tag{E18.6}
\]
这份更低费用的真实共模仍检测原period \(\alpha_0\)。其conifold全纯性与原raw minor格不同，下一节分别记录。

## E8. Conifold稳定子对值盲；raw jet全纯还要检查极点

在conifold，E4 localmonodromy为一个rank-one unipotent
\[
 T_1=I+v\otimes\ell.
 \tag{E19}
\]
其中 \(v=g_1+3g_2/4\)（非零actual vanishing period的constant倍数），\(\ell|_V\) 是非零multiple的 \(C(v,\cdot)\)。\(h,g_0,g_1,g_2\) 全纯，故均在 \(\ker\ell\)；只有第四homogeneous log方向非零。source quotient在1为平凡。该description由真实rank-onePL与canonicalholomorphicspace给出，没有猜affinetranslation常数。

任一continued branch \(\gamma\Phi(q)\) 为decomposable wedge，张成三平面
\[
 L_q=\operatorname{span}(Y_{\gamma(h+qg_0)},
                         Y_{\gamma g_1},Y_{\gamma g_2}).
\]
第一向量的quotient非零；后两向量张成homogeneous Lagrangian plane \(P_\gamma\subset V\)。因此 \(L_q\cap V=P_\gamma\)，不随q变化。

对rank-one transvection，decomposable三wedge被fixed iff三plane invariant，等价于 \(v\in L_q\) 或 \(\ell|_{L_q}=0\)。前者等价于 \(v\in P_\gamma\)。后者蕴含 \(P_\gamma\subset v^\perp\)；因 \(P_\gamma\) Lagrangian且 \(P_\gamma=P_\gamma^\perp\)，同样迫 \(v\in P_\gamma\)。反过来若 \(v\in P_\gamma\)，isotropy使 \(\ell(P_\gamma)=0\)，且对第一向量的translation落在Pγ，T₁确实fixes整wedge。所以
\[
 \boxed{T_1\gamma\Phi(q)=\gamma\Phi(q)
      \iff v\in P_\gamma,\qquad\text{对全部q相同。}}
 \tag{E20}
\]
这不能直接称为raw九行的holomorphic填点：jet坐标是derivatives，log cancellation后的wedge仍可能有apparent poles。若E20成立，Pγ由两个holomorphic homogeneous solutions生成，其中可取一个为v，另一个为k。第一列若 \(\ell(\gamma(h+qg_0))\ne0\)，则含非零 \(v\log t\) 系数。把 \(k\) 的v分量除去：若 \(k(1)\ne0\)，\(012\) determinant有非零 \(t^{-1}\) leading term；若 \(k(1)=0\)，independence使 \(k=c_2t^2+O(t^3)\)、\(c_2\ne0\)，\(123\) determinant有非零 \(t^{-2}\) leading term。可在D-jet上直接算
\[
 \det D^{0,1,2}(t\log t,t,k_0)\sim-k_0/t,
 \qquad
 \det D^{1,2,3}(t\log t,t,c_2t^2)\sim-2c_2/t^2.
\]
换成Euler jets是regular invertible triangular row change，不能删去这些whole-packet poles。反之若第一列也holomorphic，全部minors当然holomorphic。因此完整raw tuple的真正条件是
\[
 \boxed{\gamma\Phi(q)\text{ 全部九行在1全纯}
   \iff v\in P_\gamma\ \text{且}\ 
       \ell\bigl(\gamma(h+qg_0)\bigr)=0.}
 \tag{E20.1}
\]
最后一个条件是 \(a_\gamma+q b_\gamma=0\)。要宣称某个实际transported conifold branch对q敏感，必须实际找到word满足第一条件且 \(b_\gamma\ne0\)；目前未构造这样的word。canonical word全部 \(h,g_0,g_1,g_2\) 全纯，故对全部q都填平。单scalar012与完整tuple还可能有不同pole条件，不能用其monodromy evaluation injectivity偷换holomorphy。

还有一个可严格实现的regularization。E4在conifold只有一个log direction \(v\log t\)；其三阶Euler jet极点至多 \(t^{-2}\)，其余四个canonical解的jets均holomorphic。任一第三wedge最多含一列这个bad方向，所以全部branches的minors极点至多二阶。令
\[
 \widehat\Phi=t^2\Phi.
 \tag{E20.2}
\]
则 \(\widehat\Phi\) 的transported branch holomorphic iff E20成立：fixed branch的所有poles已删，非fixed branch的log不能由nonzero polynomial删除。因此这个regularized tuple的全部conifold filled branches才真正对q盲。它仍实际rank9/with1rank10；固定integer polynomial multiplication不会增加E17–E18的prefix主率，但其完整analytic/CDT normalization仍应记录。其目标值改为 \([t^2]\widehat\Phi_{012}=-2\alpha_0\)，没有丢掉该jet数据。

辛配对模型E18.1还有更直接的analytic advantage。若E20成立，则 \(P_\gamma\subset v^\perp\)，所以两个transported homogeneous columns均全纯；对第一列f，\(\theta C(f,\gamma g_j)=(Pf)\gamma g_j\) 也全纯。因 \(\theta\) 在1为非零unit times derivative，两个C值都全纯，即使f自身含 \(v\log t\)。E18.1的全部Z行因此全纯，五个mixed rows也全纯。反之若新tuple全纯则monodromy必fixed，离开t=0时T可逆又迫E20。因此
\[
 \boxed{\gamma(Z,\Phi_{\rm mixed})\text{ 在1全纯}
         \iff v\in P_\gamma,\quad\text{任意q相同。}}
 \tag{E20.3}
\]
这正说明 \(c_B\) 在t=0的退化会取消raw-minor poles；它的有理inverse有极点，不能把两份holomorphic格混为一谈。较优D七packet具有真实数值敏感方向和origin旗标，却仍不能靠conifold填点数区分q。

本节在独立回读时明确区分了fixed monodromy、raw jet全纯、regularized与辛配对模型全纯；没有把scalar exponents的非负性错误地赋给全部derivative coordinates。

## E9. 真正Stieltjes积分证明∞为full Jordan五

本节给一个不依赖resonant hypergeometric Levelt猜测的local∞证据。沿negative real \(x=-R\)、\(R\to\infty\)，实际积分
\[
 B(-R)=\int_{\mathbf R^4}
       \frac{dz_0\cdots dz_3}
        {\prod_j(2+2\cosh z_j)+256R},\quad v_j=e^{z_j},
\]
由冻结真实Stieltjes恒等式直接成立。令 \(L=\log(256R)\)，写
\[
 \log\phi(e^z)=\sum|z_j|+b(z),
 \quad b(z)=2\sum\log(1+e^{-|z_j|})\in[0,\log256].
\]
缩放 \(z=Lw\) 得
\[
 B(-R)=e^{-L}L^4\int_{\mathbf R^4}
  \frac{dw}{1+\exp(L(\|w\|_1-1)+b(Lw))}.
\]
integrand a.e.趋于 \(\mathbf1_{\|w\|_1<1}\)。对 \(L\ge1\)，它被
\(\mathbf1_{\|w\|_1\le1}+\mathbf1_{\|w\|_1>1}e^{1-\|w\|_1}\)
这个integrable function控制。Dominated convergence与four-dimensionalcrosspolytope体积 \(2^4/4!=2/3\) 给
\[
 \boxed{B(-R)\sim\frac{\log(256R)^4}{384R},
 \qquad W(-R)\sim\frac{i}{384}R^{-1/2}\log(256R)^4.}
 \tag{E21}
\]
取 \(\sqrt{-R}=i\sqrt R\)。E4 scalarL在∞regular singular、全部五个exponents为1/2（以1/x为坐标）。真实非零log⁴迫localE5 monodromy为 \(J_5(-1)\)，不是 \(J_4\oplus J_1\)。

任何decomposable \(\gamma\Phi(q)\) 的三plane含非零source quotient。绕∞奇数次时exterior三wedge的semisimple sign为−1，不能fixed；偶数次的logarithm为regular nilpotentJ₅，其唯一invariant三plane是最初三维Jordanflag，完全位于homogeneous四planeV内。故这种Lq不能invariant。因此
\[
 \boxed{\text{∞的全部transported branches都不能填平，任意q、有限cover均同。}}
 \tag{E22}
\]
这对fillability是新actual证据，未给CDT capacity数值。

## E10. 原点的实际第二endpoint：最高log³旗标唯一选α₀

原E5在0准确为 \(J_4(1)\oplus(-1)\)。\(W=\sqrt{x}B\) 是无log的canonical half-power particular，homogeneousMUM空间为V。由于eigenvalues不同，local0 semisimple projector \(p_+\) 到 \(\bigwedge^3V\) canonical存在；它可由localmonodromy的polynomial spectralprojector描述，不能未经Betti格比较记成arithmetic \(\mathbf Q(x)\) gauge。

对 \(\Phi(q)=Y_{h+qg_0}\wedge g_1\wedge g_2\)，令
\(H_q=h+qg_0-W\in\ker P\)。实际有
\[
 p_+\Phi(q)=Y_{H_q}\wedge Y_{g_1}\wedge Y_{g_2}.
 \tag{E23}
\]
真实q=α₀时，由E2和E1，
\[
 \boxed{p_+\Phi(\alpha_0)
 =-\frac{\pi^4}{16}Y_{y_0}\wedge Y_{g_1}\wedge Y_{g_2}.}
 \tag{E24}
\]
未知 \(\alpha_1,\alpha_2\) 仍完全消去。这是实际original W的local0 marking，不是任选toy参数的extra条件。

定义flat symplectic contraction
\[
 c(a\wedge b\wedge d)=C(a,b)d-C(a,d)b+C(b,d)a.
 \tag{E25}
\]
它给 \(\bigwedge^3V\simeq V\)。E8端点配对给
\[
 c(\Phi_0)=-\tfrac32Y_{g_2}-2Y_{g_1}=-2Y_v.
 \tag{E26}
\]
冻结实际node/Γ/Yukawa证明给
\(C(y_0,g_\delta)=-1\)、\(g_\delta=-\pi^2v\)，所以
\[
 \boxed{C(y_0,v)=1/\pi^2\ne0.}
 \tag{E27}
\]
令 \(N_0=\log T_0|_V\)。这是regular symplectic nilpotentJ₄，\(\ker N_0=\mathbf C y_0\)。symplectic invariance使 \(\ker N_0^3=y_0^\perp\)：\(N_0^3\) 秩1，唯一相关nonzero covector为 \(C(y_0,\cdot)\)。另一方面
\[
 C\bigl(y_0,c(Y_{y_0}\wedge a\wedge b)\bigr)=0
\]
直接由E25交叉两项相消。因此E24–E27给
\[
 \boxed{N_0^3 p_+\Phi(q)=0\iff q=\alpha_0.}
 \tag{E28}
\]
这里 \(N_0\) 在exterior三空间按c识别作用。actualq使 \(+\)-sector最高log³槽消失；任意别的q都保留非零槽。对 \(q-\alpha_0\) 的系数非零，正由E27证明，而非数值猜测。

可以把该actualsecondendpoint写成conifold canonical连接常数的精确linear关系：令 \(Z_0=c(p_+\Phi_h)\in V\)，则
\[
 \boxed{C(y_0,Z_0)-\frac{2\alpha_0}{\pi^2}=0,
 \qquad \alpha_0=\frac{\pi^2}{2}C(y_0,Z_0).}
 \tag{E29}
\]
这是两个实际端点（conifold有理初值与originMUM标记）的关系。尚未给 \(Z_0\) 的connection coefficients或整数comparison；也未证明该relation连同假设α₀代数能触发CDT不等式。

## E11. 填平与最高log旗标不是同一数据

对canonicalbranch在0，homogeneousLagrangian plane \(P=\langle g_1,g_2\rangle\) 包含v。regularJ₄唯一invariant Lagrangian二plane为 \(P_0=\ker N_0^2\)，它位于 \(y_0^\perp\)。E27说明 \(v\notin P_0\)，所以 \(P\ne P_0\)。混合quotient已经不能fixed，故canonicalbranch绕0任意有限cover仍不填平，任意q一样。

对任意transportedbranch \(\gamma\)，必须先区分cover parity：原T₀的source character是−1，mixed quotient非零，任何奇数次loop的wedge都不能fixed。以下准确的潜在填点criterion是在偶数cover杀掉Kummer character后使用 \(T_0^2\) 的unipotent作用。先必须 \(P_\gamma=P_0\)；随后在local splitting \(E=V\oplus\mathbf CW\) 中写第一向量为nonzero multiple W加 \(H_{\gamma,q}\)。其三plane invariant iff \(N_0H_{\gamma,q}\in P_0\)，此时unipotent在plane上的determinant为1，故确实fixes wedge；该条件等价于
\[
 C(y_0,H_{\gamma,q})=0.
 \tag{E30}
\]
这里只是实际monodromy标记给的条件；当前未证明有某个word使 \(P_\gamma=P_0\)，不能把它当成已有新增fillable sheet或capacity提升。若存在，第二项可能依赖q；若variation coefficient零，则不依赖q，均须逐word实际比较。对∞和conifold则E20、E22已经完整分类。

E28的唯一参数检测是最高log³旗标，不是已构造的值敏感conifold填点，也不是canonical0填点。因此它确实保留了此前 \(S=F+q\) 抹掉的一项实际endpoint信息，同时尚未解决CDT所需容量与费用缺口。

## E12. 数值目标与下一步

若仅假设 \(R_0-M_0\in\mathbf Q\)，\(\alpha_0=\pi^2(R_0-M_0)/16\) 仍不必代数，E17不适用。适用单初值假设的直接目标仍为 \(\pi^2(R_0-M_0)\)，或更大period向量关系；Tate normalization不能免费改变。

本稿已给可实际推进的三项数据：真实rank9/含1rank10、原minor D十与辛配对D七（mixed D六）的全部prefix array、唯一actualorigin highest-log relationE28/E29。应在真实Betti/de Rham格上计算p₊、N₀与primitive quotient的comparison，核这种flag constraint怎样进入CDTholonomy秩界；不能继续只优化对q全盲的conifold填点数。

另外actual open Tateboundary已经由root独立路线研究。若存在真实noncompact relativecycle，必须以rationalopencounterterm改动trace并计整数成本；本稿没假定raw R⁺ discrepancy compact，也没把新tensor的numeric endpoint视为指定Xi的全部marked regulator评价。

尚未给任何新ζ/L/Catalan数值无理性；完整目标仍active。需要effective \(C_h,C_g\)、Smith与all-place费用、actual integral lattice/saturation及适用的endpoint-sensitive analytic capacity。

## E13. 实际阅读与执行边界

本轮实际读主记录 §§73–78、[root review](cdt_odd_R0_current_cycle_arithmetic_root_review_20261006.md)全文和delivery末尾全部current scope。原center/Kummer/Yukawa/positive-cut稿在上一轮本代理已实际全文核读，本轮关键concomitant、local0/非分裂和Stieltjes输入按冻结原文使用；没有重跑数学脚本。原source是既存 [FR published](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)、实际node/cup稿所核primary；本轮不声称新增primary阅读页或PDF归档。

E4–E30均为上述对象上的新全尺度纸面证明。九秩不是abstractdimension猜测，∞J₅不是有限numericalasymptotic，整化不是有限samples，E28不是PSLQ。没有数学producer、没有Lean claim；自己的回读不冒认独立审阅，同行/root独审另记录。
