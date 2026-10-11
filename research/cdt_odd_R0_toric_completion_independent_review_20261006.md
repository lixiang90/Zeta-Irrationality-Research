# 非regular toric family higher-Chow completion 的独立全尺度审核

日期：2026-10-06。quarter_actual_rank独审NEW toric completion稿 §§1–9（作者补强strict fixed-lattice、global orbit chart及明确问号的regulator候选后的版本）。本代理实际读Doran–Kerr出版PDF25–29、79–80，Abramovich–de Jong v1 PDF2–3、12，以及MVW2006所需7页。纯纸面核查，没有执行/import任何旧、root或peer数学producer。

结论：新稿构造的split SNC family model和coordinate-symbol rational higher-Chow completion成立。关键是resolution保持原lattice、所有surviving strata全局split、d1在整条stratum上vanish及actual higher differentials的target vanish；不是“field所有tame residues为零⇒完成”。没有证明所选completion的regulator等于旧R0−M0真实标记周期，亦没有新的数值无理性定理。

## 1. 实际几何设置和monomial graph

在P=(P¹)^4上，S的12个coordinate divisors在同一个factor内互不相交，different factors transverse，因此split SNC。一个support S含s≤4个fixed coordinates，stratum是U^(4-s)，U=P¹\{0,∞,−1}。固定参数v、1/v、v+1全是各相应Zariski chart的真实global coordinates。

φ=∏(1+vj)²/vj在0和∞的order均−1，在−1的order2。局部φ=c z^e准确给e_i=−1或2，且c是unit，c_S=(−1)^p∏free(1+v)²/v。∞没有被漏记。在monomial graph blowup中，unit c只将一个generator乘unit，所以ideal(z^(e+),z^(e−))不变；normalization对应按ℓ=Σe_i a_i的零hyperplane切cone。来自同一个rational map的graph闭包使这些local constructions相容，且不同charts的face restrictions正是同一个finite strict cone complex。

max(0,ℓ)给rational coherent subdivision。所有cones位于一个closed half-cone中，故normalized graph已resolve rational map到P¹的indeterminacy。进一步refinement只在这些cones内进行，不能恢复indeterminacy。

## 2. strict toroidal与fixed-lattice regularization的独立核查

Abramovich–de Jong v1 PDF3 Theorem0.4明确为strict toroidal embedding给canonical nonsingular blowup，引用KKMS II§2 Th11*；PDF12 §1.5明确将它称为pair的toroidal resolution。使用这里的toroidal/monomial modification，而不是arbitrary Hironaka blowup，完全保持原cocharacter lattice及boundary orbit描述。原embedding无self intersections；split monomial normalized graph与subdivision仍strict，所需theorem适用。

还可直接从有限cone complex证明所需fixed-lattice regular refinement，避免把KKMS ChapterIII的允许denominator theorem当成依据：

1. 用兼容star subdivisions先simplicialize。每条新ray均选原integral lattice中的primitive generator，不改变lattice；barycentric选择可在整个finite strict cone complex中同时兼容faces。star subdivision是projective toroidal modification。
2. 对一个非unimodular simplicial coneσ=〈v1,…,vr〉，在饱和span lattice中取半开fundamental parallelepiped的nonzero lattice pointw=Σa_i vi，0≤a_i<1。沿同一ray取primitive w0，仍有0≤a_i'<1。令τ是含w0的最小face，并在所有incident cones同时star-subdivide。
3. 每个受影响simplicial cone的replacement cone将一个vi换成w0，其multiplicity等于旧multiplicity乘对应a_i'，是严格较小的positive integer。未受影响cones不变；新faces的multiplicity不超过其containing cones。故选最大multiplicity的一个cone时，最大值不增，其对应cones数严格减少；有限降序终止于全部multiplicity1。

这个proof只在原lattice中加rays，未引入半整数lattice或ramified base change；star subdivisions相对于旧fan projective，并始终contained in旧half-cones。因chart normal coordinates及单位transition全部在Q且split，monomial ideals与toroidal modifications也定义于Q。结果tildeP光滑，其总boundary SNC；f为morphism且proper，Y=f^-1(Gm)为光滑四维，Y→Gm proper。

本代理没有实际读KKMS ChapterII完整证明或作者所读的ChapterIII scans，不声称读到那些原页；上面的fixed-lattice论证独立列出，Ab PDF3、12提供原始toroidal theorem接口。

## 3. global orbit chart与全部horizontal strata

refined coneτ维r，其最小原support是s-cone且relative interior有所有s坐标正的vector。τ surviving于Y当且仅当τ⊂kerℓ；否则某正/负order ray使stratum落入f=0/∞而被删去。nonzero horizontal cone必同时含positive与negative original exponents，故至少一个fixed coordinate为−1，另一个为0或∞；s≥2且r≤s−1≤3。

global split是实质核点。对该固定support，把全部fixed factors取上述各自global z_i chart，free factors取U；这是A^s×U^(4-s)的explicit open，fixed因子各只删一个nonzero z值（±1）。原support最小使每个z_i在associated orbit上恒0：原coordinate character在某个τ-ray上strictly positive。因此这个open限制完全不删掉associated orbit的任何point，而一个同一product chart已经覆盖整个stratum。fixed点的normal lines沿U^(4-s)确为trivial，不需在多个twisted bundles间粘接。

所以所有family strata准确为U^(4-s)×Gm^(s-r)。primitive ℓ在quotient lattice也primitive：一个原negative coordinate vector的pairing是−1，而Nτ⊂kerℓ，故其quotient image仍给−1。GL_Z basischange加一个torus coordinate乘unit c_S，使f准确成为最后Gm_λ projection。这个变换既不取square root也不改function field。

codim2 r=2只能s=3或4，target strata全部是U×Gm或Gm²，exhaustive；codim3只可能s=4，strata是Gm；不存在codim4 horizontal strata。其dim均是family dimension4减r，并非先pass到Q(x)的fibre后借totally real vanishing。

新增smooth-fibre范围也通过：在U⁴内部∂vj logφ=(vj−1)/(vj(1+vj))，故唯一critical point是所有vj=1，其φ=256；boundary每个stratum已有λ-coordinate使df不为0。因此整个proper fibre在λ∈Gm\{256}光滑。这里没有将λ=256奇异fibre的pullback、nearby cycles或marking偷偷纳入。

§3.1的two-variable sanity chart同样成立：rays(1,0),(2,1),(1,1),(0,1)相邻det1；horizontal(2,1)给q=z/w²和λ=−φ23/q，boundary open为U²×Gm。这里strict原lattice及global product assertion实际可见。

## 4. d1在全stratum higher-Chow group中为零

coordinate-symbol ξ来自U⁴上四个真实unit CH¹(−,1)的product，DK PDF27给graph-symbol class与generic Milnor symbol的准确区别。每个horizontal boundary divisorEα映入一个含vj=−1的原center，该固定coordinate在整个Eα均为−1，非只generic point；并且vj在b^-1(vj≠0,∞)上为regular unit，包含整个Eα。

移到symbol首项后，用higher-Chow localization与products兼容，在完整Eα°上residue是{-1}乘剩余三个units的boundary class（可能的graded sign不影响vanishing）。CH¹(Eα°,1)=ΓO*，{-1}有order2，⊗Q后为0。因此d1ξ在CH³(Eα°,3)_Q准确为0。没有经过field restriction再将可能kernel当0。

## 5. actual d_r target及CH² vanishing lemma

DK出版PDF26/印刷422给CH²(Q,3)_Q=0；这里是totally real number field本身，而非rational function field。对任意smooth separated Z/Q，CH¹(Z,q)=0(q≥2)还实际核准了新的官方一手原件：Mazza–Voevodsky–Weibel2006 PDF40–42的Theorem4.1/Corollary4.2给Z(1)≈O*[-1]及weight-one非degree1,2的vanishing；PDF174、176–178的Theorem19.1和proof给CH¹(Z,q)=H^(2−q,1)(Z,Z)。q≥2对应2−q≤0，所以整系数group已经为0；无需只在field或只在Q coefficients声称。这也给CH¹(Z,1)=O*(Z)所需的全stratum单位解释。

若CH²(Z,3)_Q=0，则projective bundle给CH²(Z×P¹,3)_Q=CH²(Z,3)_Q⊕CH¹(Z,3)_Q=0。删finite nonempty rational sections的localization相邻项为
\[
0\to CH^2(Z\times A,3)_Q\to\bigoplus CH^1(Z,2)_Q=0.
\]
这里左端的0表示前一CH²(ZP¹,3)为0，只用exactness；于是目标group确0。由SpecQ出发两次应用，准确得CH²(U×Gm,3)_Q=CH²(Gm²,3)_Q=0。根本不用某种Künneth假设或function-field Borel vanishing。

实际读DK PDF28–29/印刷424–425的general pure-codimension localization spectral sequence。对E_r^(0,−4)，d_r target为CH^(4-r)(D^(r,*),3)的subquotient。d1已在全strata groups证明0；d2的group本身因上段及§3 exhaustive strata为0；d3的CH¹(−,3)为0；D4空故无更高targets。source不存在a<0的incoming differentials，DK明确给E∞^(0,−4)=image(CH⁴(Y,4)→CH⁴(Y*,4))。因此ξ确有rational higher-Chow lift Ξ。

这个证明没有把d2替换成iterated tame residue，也没有直接套DK n=4 regular-hypersurface completion theorem。原repeated face roots和nonregular问题是在split toroidal family的全strata上另行处理。

## 6. 正面结论和未审成的regulator接口

完成的是一个定义于Q的proper smooth toroidal family model上的实际CH⁴(Y,4)_Q completion，并可pullback至smooth fibres。最终主稿没有先假定completion nonunique，而将family restriction kernel明确列为待算；该kernel的正面vanishing另由本轮NEW[唯一性稿](cdt_odd_R0_toric_completion_uniqueness_20261006.md)与独立记录登记，不能将这个Chow-class问题和Betti/regulator-current lift ambiguity混同。

本审核未建立KLM current与旧8C−TΓ的marking/Tate比例、π²(R0−M0)/16的regulator identity、整Betti/deRham饱和或新的CDT all-place严格差额。positive motivic lift不能被改写成一个新数值ζ/L定理。稿§7的这四项局限正确且实质。

新增§8也实际读了：DK原件PDF79–80的Lemma4.1明确只陈述ell=2,3及所列smooth compactification hypotheses，不会直接覆盖本例ell4/nonregular boundary。作者保留问号而未作为主定理使用，范围正确。其假设中的first candidate若成立，λ=256x且ω=√x ResΩx、Ωx=16 dlogv⁴/(φ−256x)，则θx转换的scalar factor确为−256x/(16√x)=−16√x；这个比例换算不证明ell4 current identity、sign/Tate convention或compact-sector projection。本审核没有将这个待证候选升级为regulator theorem。

## 7. 阅读、版本与冻结范围

实际全文回读作者已冻结最终稿 §§1–9，SHA256 `abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0`。最终新增MVW exact source、Levine范围、§7 conditional family-kernel而不先假定nonuniqueness，以及保留问号的§8 candidate均已实际核查；inline TeX修复不改变display数学。作者新来源收据亦实际全文读，SHA256 `509b0b5205e21b38dd8383f14a95a3fcae173e24aad1a6addbcb21f2f9e298b6`。

实际primary范围：DK PDF25–29、79–80（7页），Ab-deJong v1 PDF2–3、12（3页），MVW2006 PDF40–42、174、176–178（7页），Levine1994 PDF79–85（7页）；没有冒认DK全部204页、Ab全部12页、MVW全部234页、Levine全部87页或KKMS完整书稿。网页目录只确认institutional KKMS来源实际只有ChapterIII，不以该目录或二手搜索结果支撑数学定理。

本次保存MVW官方原件，SHA256 `fb20ff2f30cefe0b67b359de275491e3716d509d891cc72afa95460f57ed0180`，234页；上述weight-one读取的来源/read_scope见[NEW来源收据](../literature/manifest_cdt_odd_weight_one_higher_chow_20261006.json)。同轮另实际补读PDF151 Properties17.4，明确higher-Chow localization对任意scheme的open complement适用，不需singular boundary smooth。URL路径2022/03是上传目录，不将它称为2022新论文。正常Schannel验证curl成功；没有TLS bypass。

实际primary bytes SHA256：DK出版原件`1911f2f4a805e1a3d218ca247665209f3fe9505aa9bc0ae949b1163d7271ede4`；Ab-deJong v1原件`c9265d149f37a8a9d254ca8f0eb40262009006a660b827b7e80a3c2a6d1b0397`；Levine原件`5f4de92e51f03dfb9a4708f70ed9a8f58d2c2a51e310eeb4d597be84c7450984`；MVW新来源manifest`a82c6465281cfe036854180709cfa73bd13113005c055dbdea7609f8608f7500`。

本稿纯独立纸面审核，没有数学producer或有限checks，无Lean声明。已核对上述作者final版本；本稿按明确scope冻结，本稿SHA由交付工具登记。
