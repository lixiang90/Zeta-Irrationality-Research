# 恢复四重零点的平衡能量：独立全文审核

日期：2026-10-06。审阅者 conifold_arithmetic_hypothesis。NEW 独审；不修改冻结旧稿或同行稿，不执行或 import 同行 producer。

## R1. 实际读取与 pins

实际完整读取 research/cdt_odd_restored_zero_equilibrium_energy_20261006.md，E1–E35，SHA264cc3fce8d8417e04e3aea8963010b0f8804c2014692d4a64827c774454f0e6。

实际全文静态读取 NEW research/cdt_odd_restored_zero_equilibrium_energy_verify_20261006.py，SHA8aabd288de14fa1b0c72fd72a4b9568ec610b9e22af7ea205de472c8b88e7804；以及其完整 JSON，SHAef3fc4a69593411eb6ae10b680f4b406a22c823c54a5182043e45fd03b339d66。仅读源程序与已存在输出，没有执行、import 或重跑。完整读取来源收据 literature/manifest_cdt_odd_restored_zero_equilibrium_energy_20261006.json，初候选4292ba全文读后，又实际全文读取最终冻结SHA190642d5d8a5c0fc02c60942fb4937da2dc564956819588db19a8980961cdf98；proof/PY/JSON未改。本独审最终保存全文回读后正式冻结。

本轮 actual primary reading 是 Saff2010 PDF32–36，共5页，原件36页，SHAcfbeaad8cf695fc1b5528fd56295d7e3053056634c6841765a434ce9b074d862。使用 UTF-8 读取成功，特别PDF32–33 的 unbounded admissibility、mass1及(6.2)。未冒称读全36页或 Brown/Monien 原件。该PDF由root正常TLS归档；本审阅者没有下载。

冻结输入 analytic c4e8f04f0debe34cf896780424e6ceb256747eaca0d3ed3b9698802757447218、root budget644f7dbf8e01ec85f938c49435becded48533c88577f712999b6eecb0ae7c3c5均本轮实际全文读；首次组合输出中 analytic中段被截断，随后单独全文读，D1–D31完整交付。root budget R1–R9完整；其PY/JSON未执行。Lai25页只复用前轮阅读，不登记为本轮新增阅读。

## R2. 实际布局与完整正包络

四重零阶大于最高导数3，故前2n个正整数的全部 head residues 确实消失。degree R=−2h−2，在degP<2h时级数、完整右线积分和所需 Heine moments绝对收敛。a,b 的固定 kernel与D26 uniform product界都按对应layout使用。

E5的n-scaling正确：h个density各付1/n，volume各付n，两者抵消；Vandermonde付n^{h(h−1)}，没有漏n^h。h!与F_h取的是实际normalized Hankel对象。这里只用复积分绝对值取得正包络，不把任意形式X识别为实际数值关系。

E7直接求导成立：2π−6atan(2/y)+2atan(L/y)=6atan(y/2)−2atan(y/L)，再写成6-weight的[2,L]和4-weight的[L,∞]混合。E8的正混合与V₀=2LlogL−2BlogB−4log2核过；V(y)在无穷为2π|y|+2dlog|y|+O(1)，符合Saff unbounded weight w=e^{−V/(2d)}。

## R3. 显式 resolvent、support 与全域 EL

E10的apparent poles在±iu被所选sqrt branch精确抵消；slit jump等于−2πiρ，无穷O(1/z)，故是正确Cauchy transform。mass1/2(1−u/sqrt(u²+r²))来自无穷1/z coefficient。

正混合的mass为3(sqrt(4+r²)−2)−(sqrt(L²+r²)−L)，其derivative严格正。mass=d=L−6等价3sqrt(4+R²)=sqrt(L²+R²)，平方没有额外正root，故R²=(L²−36)/8。密度在cut内严格正且边缘sqrt vanishing，积分与parameter微分有合法可积支配。

由两岸resolvent和给cut内2U'=V'；cut外E14是sqrt(x²−r²)乘严格正混合，所以EL不等式成立于整实轴。R<L/2；对x≥L只保留u≥x项，导数下界>1，得到D(x)≥|x|−L。故∫e^{−D}≤2(L+1)，真正控制了无限tail。

rho≤R/(2π)(3−2/L)由每个charge的u^{−2}界直接积分；不存在把finite sup当可积包络的步骤。

## R4. 全 n 正则化，不省 self-energy

Kε−logε的Laplace/Fourier身份核过；mass0杀常数项，cos双积分给|sigma-hat|²，负号正确。first absolute moment在0端给O(t²)/t，指数因子控制∞端，截断后Fubini再dominated convergence合法。应用的sigma是empirical减compact有界密度，假设满足。

Uε−U≤πMε来自一维kernel积分2πε；Iε(μ,μ)≥I(μ,μ)。取ν=n⁻¹Σδ，mass=d，扣除h个diagonal logε，逐项得到E22的n²E_B−nΣD+2dπMεn²−hlogε。

ε=1/n与n≥1给全部n的Z_n≤[2(L+1)]^h e^{n²E_B+2dπMn}n^h。代回实际Heine后是E24的n^{h²}/(h!F_h)。Stirling求和主项h²logh−3h²/2，故beta=−E_B+d²logd−3d²/2。fixed kernel、diagonal和tail均只留明付的O(nlogn)，没有从形式平衡点直接猜全n结果。

## R5. 闭式 beta 的独立手核

E26由实际angular density的Fourier coefficients (−t²)^k与log|r cosθ|的coefficients核过；得到(1−u/A_u)log(r/2)+log(2u/(u+A_u))，质量因子1/2没有遗漏。

E27尾积分的integration by parts成立；E28的ell'确为2m'log(r/2)。对可微mass family，energy derivative为ell m'；固定角坐标后density、parameter derivative及log singularity均可积。因此E29保留mass derivative的积分项是必要而正确的。

E30由m=3sqrt(4+r²)−sqrt(L²+r²)+d逐项平方得出。E31的primitive可直接求导验证；在0端扣掉2Llogt后有限常数正确。实际endpoint C=3A，S(T)=3(L²−4)/8，两个ratio分别为2(L−2)/(L+2)及(L²−4)(L+6)²/(128L²)。

独立代入可见E28与6dJ₂−2dJ_L中的sqrt logarithms完全抵消，剩

\[
\beta=dV_0+d^2\log(2d/R)-3d^2/2-5T+6J_{2,L}(T).
\]

把6J展开，polynomial部分
3S(T)−6L−5T−3d²/2=−d²；
log(2d/R)=1/2log(32d/(d+12))，因此精确复原E32。符号、factor2与h=d n normalization通过。

## R6. 严格 interval code 的准确范围

静态核N=80的atanh-log算法。t∈[0,1/3]，截断powers1,…,159，余项上界2t^161/[161(1−t²)]正确；任意正有理数按2的整幂缩放，负integer或负coefficients反转endpoints，代码逐项如此处理。thousand窗口由精确floor/ceil而非float给出，严格assert排除了endpoint equality。

三组log coefficients/arguments逐项吻合E32。mass square与E31两个ratio共有9个代数checks；三组strict window、gain、safe-cost方向共有9个checks，JSON登记18与源码一致。读取的JSON完整，producer SHA与现存源hash相符。作者唯一首次运行的已存输出支持所报严格窗口；本审阅者没有再次执行。

证书只证明B5/6/8的闭式常数包围，不能证明general-n theorem；general-n已经在R2–R4核纸面步骤。gain严格>0.465、>0.799、>3.376与冻结root R8窗口方向一致；safe arithmetic A只是上界，不能解释成实际费用下界。

## R7. 正包络精确门槛与结论

μ/d有compact有界density，square-root endpoints令entropy与log energy有限。将Z_n限制到cut并以p^h改写，log integrable，Jensen给h(h−1)I(p)−nh∫Vp−hH(p)。h=d n代入就是E34；与全n上界夹出E35。

因此beta_eq是指定固定右直线正包络的精确n²系数；它不是actual complex determinant的lower bound，也不否定phase cancellation、不同contour或另一个整格的改进。三组beta均仍低于已给safe A，未证明strict margin或新数值无理性/线性无关性。

E1–E35及NEW code/JSON的上述scope独核通过。本文自身producer新建/执行为0；所有旧/同行producer执行、import、rerun为0；只有源读取/PDF文本提取/hash。本agent另一篇自有auxiliary probe的首次运行另有独立收据，不混入本审计的执行数。最终冻结源收据已实际全文读并 pin，本独审最后全文回读后冻结，准确 hash 另交 root 与作者。
