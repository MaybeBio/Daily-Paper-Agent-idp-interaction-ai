## 01 基本信息
- **标题**：Asymmetric coevolution of the MEK-ERK binding interface
- **作者**：Persikov, Anton V; Marmion, Robert A; Shvartsman, Stanislav Y
- **单位**：Flatiron Institute（Simons Foundation 分部）；作者所属机构未完整提供
- **期刊/平台**：The Journal of Biological Chemistry (JBC)
- **年份**：2025（在线日期 2025-09-14）
- **论文类型**：研究论文（实验+计算整合）
- **领域**：信号转导、进化生物学、蛋白-蛋白互作、IDR/IDP、计算结构生物学
- **关键词**：MEK、ERK、D-site、D-recruitment site (DRS)、IDR、AlphaFold2、分子动力学模拟、共进化、SLiM、果蝇遗传学
- **DOI/arXiv**：10.1016/j.jbc.2025.110708
- **代码**：未提供
- **数据**：AlphaFold2 预测的人源和果蝇 MEK-ERK 复合物坐标文件已存入 Zenodo（DOI: 10.5281/zenodo.16808770 和 10.5281/zenodo.16808787）
- **阅读日期**：2026-05-13
- **在本课题方向中的位置**：本文是「IDR/IDR 介导的蛋白互作 × 进化分析 × AI 结构预测（AlphaFold2）× 物理模拟（MD）」的交叉范例。核心对象是 MEK 的 N 端无序 D-site 与 ERK 的 DRS 之间的互作，展示了 IDR 中 SLiM 基序如何在保守互作功能下发生跨物种序列分化，以及 AlphaFold2+MD 如何用于解析 IDR 介导的互作界面。对 IDP/IDR 相分离课题的可迁移点在于：IDR 内短线性基序的进化-结构-功能关系分析框架、AI 预测与 MD 验证的整合流程、以及体内功能验证的遗传学策略。

## 02 一句话总结
通过跨 300+ 物种的序列分析、AlphaFold2 结构预测和微秒级 MD 模拟，发现 MEK 的 N 端无序 D-site 在物种间序列高度分化但组内保守，五个关键残基（K3、K5、I9、L11、D16）通过与 ERK 的 DRS 形成静电/疏水接触维持互作，且该互作在果蝇体内对 ERK 信号和个体存活绝对必需。

## 03 研究问题
- **具体问题**：在 MEK-ERK 这一高度保守的信号模块中，MEK 的 N 端无序 D-site 与 ERK 的 DRS 之间的结合界面如何共进化？互作网络架构的不对称性（ERK 是 hub 蛋白、MEK 只与少数伙伴互作）是否影响两侧的进化速率？
- **为什么重要**：ERK 是调控增殖、分化等众多过程的核心激酶，其唯一上游激活激酶是 MEK。理解 MEK-ERK 互作界面的进化规律，有助于揭示信号特异性的分子基础，也为靶向该界面的药物设计提供依据。同时，D-site 是 IDR 中的 SLiM，其进化模式对理解 IDR 介导互作的普遍规律具有参考价值。
- **现有方法不足**：此前大规模进化分析（如作者前作）将 MEK 的 N 端 D-site 排除在外（因序列变异过大难以比对）；细胞实验因过表达等混杂因素无法判断 D-site 是否绝对必需。
- **Can 问题**：Can the intrinsically disordered D-site of MEK maintain conserved ERK binding function despite rapid sequence divergence across metazoan species?

## 04 背景与发展脉络
*注：以下脉络部分基于本文框架，部分经外部知识核验，具体标注如下。*

1. **MAPK 信号模块的保守性研究**（经外部核验）：MEK-ERK 通路在真核生物中高度保守，ERK 作为 hub 蛋白与数十种底物/调节因子互作，而 MEK 的互作伙伴极少。这种网络架构不对称性此前未被用于分析互作界面的共进化模式。
2. **SLiM/IDR 进化研究**（经外部核验）：短线性基序（SLiMs）位于 IDR 中，因序列短、约束弱而进化快，但需保留关键理化特征以维持互作。本文的 D-site 是典型 SLiM 案例。
3. **AlphaFold2 用于 IDR 复合物预测**（经外部核验）：AF2 对 IDR 单独预测置信度低，但与折叠伙伴共预测时，IDR 可呈现诱导折叠构象。本文利用 AF2 Multimer 预测 MEK-ERK 复合物，pLDDT 显示 D-site 在结合态下获得有序结构。
4. **MD 模拟验证蛋白-肽互作**（经外部核验）：微秒级 MD 用于评估弱/动态互作的稳定性与接触模式，本文用 1 μs 模拟验证 AF2 预测的接触界面。
5. **果蝇遗传学功能验证**（经外部核验）：CRIMIC 系统实现内源基因敲除+转基因回补，可在体内严格检验特定残基的功能必要性。
6. **本文主张的位置**：首次将网络架构不对称性（hub vs. 非 hub）与 IDR 内 SLiM 的进化分析结合，提出「互作界面两侧进化速率不对称」假说，并用计算+实验双重验证。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| D-site 序列变异过大，难以比对 | 前作将 N 端 D-site 排除在进化分析之外 | IDR 序列约束弱，常规比对工具难以处理 | Results 节 "the D-site was excluded because of high sequence variability" |
| 细胞实验无法判断 D-site 是否绝对必需 | 过表达体系下 D-site 突变体仍可部分激活 ERK | 过表达补偿了结合亲和力下降 | Discussion 节 "confounding effects of overexpression" |
| AlphaFold2 对 IDR 单独预测置信度低 | 游离 MEK 的 D-site pLDDT 低 | IDR 无稳定三级结构 | Results 节 "pLDDT confidence score plot, showing increased ordering of MEK in the complex with ERK compared with free MEK"（图 2B） |
| 静态结构无法反映互作动态 | AF2 仅给出单一构象 | 缺乏构象系综信息 | Results 节 "MD simulations provided a clearer picture of the interaction" |
| 跨物种功能验证困难 | 无法在多个物种中逐一验证 D-site 功能 | 遗传操作在多数物种中不可行 | 作者选择果蝇作为模式生物进行体内验证 |

## 06 核心思想
1. **表面方法**：跨物种序列比对 + 聚类 → AlphaFold2 Multimer 预测复合物结构 → 1 μs MD 模拟验证接触模式 → 果蝇体内功能实验（缺失/点突变回补）。
2. **核心洞察**：MEK-ERK 互作界面呈现**不对称共进化**——ERK 侧 DRS 高度保守（因其需与众多伙伴互作，序列自由度低），而 MEK 侧 D-site 在物种间快速分化但组内保守（因其只需适配 ERK 一个伙伴，序列自由度相对高）。尽管序列分化，五个关键残基的理化性质（电荷/疏水性）被维持，形成保守的「化学补丁」识别模式。此外，D-site 不仅是结合模块，还通过变构效应稳定 MEK 活性位点构象。
3. **可能的普适教训** [Analysis]：对于 IDR 介导的互作，序列保守性评估不应仅看同一性，而应关注**理化性质保守性**（电荷、疏水性、长度）与**关键接触残基的维持**。AF2 复合物预测 + MD 验证是解析 IDR 结合构象的有效组合，但需注意 AF2 可能高估 IDR 的有序性，MD 的力场参数对 IDR 的适用性也需谨慎。网络架构（hub vs. 非 hub）可作为预测互作界面进化速率不对称性的先验线索。

## 07 方法总览
- **输入**：309 个后生动物 MEK 直系同源序列（来自前作数据集）；人/果蝇 MEK-ERK 蛋白序列；果蝇遗传品系。
- **输出**：D-site 进化聚类（4 组）；AF2 复合物结构；MD 接触图；果蝇存活率表型。
- **模块**：
  1. 序列分析：MUSCLE 比对（gap open 3.0, gap extend 0.5）→ Shannon entropy → 序列相似性网络（Biopython TreeConstruction，阈值 0.2）→ K-means 聚类
  2. 结构预测：AlphaFold2 Multimer（默认设置，full database search），每复合物 25 个模型，选 top-ranked
  3. MD 模拟：OpenMM CUDA，CHARMM36 力场，TIP3P 水盒子（10 Å padding），0.15 M KCl，NPT 1 μs（WT 5 重复；MEK5A 16 重复，375 K），4 fs 步长（氢质量重分配）
  4. 接触分析：自定义 Python 脚本（Biopython），非氢原子 <4 Å 为接触
  5. 体内功能：CRIMIC 系统（meK-GAL4 敲入），UAS-MEK 转基因回补，雄性存活率
- **流程**：序列收集 → D-site 区域提取与比对 → 进化聚类 → 选择代表物种（人/果蝇）→ AF2 复合物预测 → MD 模拟 → 接触图分析 → 关键残基鉴定 → 果蝇突变体构建 → 存活率/表型评估 → 整合结论。

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 序列相似性网络 + K-means 聚类 | 将 274 条 D-site 序列分为 4 个进化组 | 揭示组内保守、组间分化的模式 | 输入：274 条 D-site 序列；输出：4 个聚类组 | Results 节 "identified 201 sequences that clustered into four evolutionary subgroups" | 无法识别组间分化模式，无法指导代表物种选择 |
| Shannon entropy 分析 | 量化每个位点的保守程度 | 定位关键保守残基 | 输入：MSA；输出：每位点 entropy 值 | Results 节 "confirmed that the kinase domain is highly conserved, whereas the D-site shows the highest sequence entropy" | 无法区分功能关键位点与中性变异位点 |
| AlphaFold2 Multimer | 预测 MEK-ERK 复合物结构 | 获得 D-site-DRS 互作的原子级模型 | 输入：MEK+ERK 序列；输出：复合物结构 + pLDDT | Results 节 "the predicted complexes consistently showed the D-site binding to the same groove in ERK" | 无法获得互作界面结构模型，无法设计点突变 |
| 1 μs MD 模拟 | 验证 AF2 预测的接触模式，评估互作稳定性 | AF2 静态结构需动态验证；IDR 构象需系综采样 | 输入：AF2 结构；输出：接触频率图、RMSD 轨迹 | Results 节 "MD simulations revealed common interaction patterns"；图 2C | 无法区分真实接触与 AF2 预测伪影；无法评估突变对结合的影响 |
| 点突变 MD 模拟（MEK5A） | 测试五个关键残基同时突变后的结合行为 | 预测关键残基的功能贡献 | 输入：五突变体结构；输出：解离动力学 | Results 节 "in the MEK5A mutant, the D-site detached from the ERK groove"；图 3A | 无法判断单个残基的独立贡献 |
| 果蝇 CRIMIC 回补实验 | 体内验证 D-site 功能必要性 | 计算预测需生物学验证 | 输入：转基因果蝇品系；输出：雄性存活率 | Results 节 "MEK_ΔD-site failed to support male viability"；图 4B | 无法确认 D-site 在完整生物体中的功能重要性 |

## 09 关键公式符号
1. **Shannon entropy**（序列保守性度量）：
   \[
   H(i) = -\sum_{a=1}^{20} p_i(a) \log_2 p_i(a)
   \]
   其中 \( p_i(a) \) 为位点 i 出现氨基酸 a 的频率。用途：量化每个位点的序列变异程度。直觉：H 越高，位点越不保守。来源：Methods 节 "Shannon entropy was computed from MSA data"。

2. **解离时间定义**（MD 分析）：
   \[
   t_D(i) = \min\{t : d_i(t) > 15\,\text{Å}\}
   \]
   其中 \( d_i(t) \) 为轨迹 i 在时间 t 的 COM 距离。用途：定义 D-site 从 DRS 解离的时刻。直觉：超过 15 Å 视为解离。来源：Methods 节 "Analysis of D-site dissociation"。

3. **累积解离分数**：
   \[
   F(t) = \frac{1}{N}\sum_{i=1}^{N} \eta_i(t), \quad \eta_i(t) = \begin{cases} 0, & t < t_D(i) \\ 1, & t \geq t_D(i) \end{cases}
   \]
   用途：汇总多条轨迹的解离动力学。直觉：F(t) 单调递增，表示到时间 t 为止已解离的轨迹比例。来源：Methods 节。

4. **RMSD**（结构偏差度量）：
   \[
   \text{RMSD}_i(t) = \sqrt{\frac{1}{M}\sum_{m=1}^{M} \| \mathbf{r}_m(t) - \mathbf{r}_m(0) \|^2}
   \]
   其中 \( \mathbf{r}_m(t) \) 为原子 m 在时间 t 的坐标，M 为子域原子数。用途：追踪 D-site 和活性位点的构象变化。来源：Methods 节。

## 10 实验设计与证据链
- **数据集/群体**：309 个后生动物 MEK 序列（274 个含完整 D-site）；人（H. sapiens）、斑马鱼（D. rerio）、线虫（C. elegans）、果蝇（D. melanogaster）为代表物种；果蝇遗传实验使用 mek-GAL4 敲入品系（BDSC #78914）。
- **规模**：MD 模拟 WT 5 条 1 μs 轨迹；MEK5A 16 条 1 μs 轨迹（375 K）；果蝇回交实验每组 n 见图 4。
- **指标**：Shannon entropy、序列聚类、pLDDT、接触频率、COM 距离、解离时间、雄性存活率、蛹长度。
- **基线/对照**：WT MEK 回补作为阳性对照；UAS-GFP 作为阴性对照（无法回补）；同胞兄弟（携带 WT X 染色体）作为内部对照。
- **预算/资源**：未提供具体计算资源信息。
- **骨干/仪器**：AlphaFold2 Multimer（计算集群）；OpenMM CUDA（GPU）；果蝇培养标准条件。
- **oracle 输入**：AF2 预测结构作为 MD 起始构象。
- **评测协议**：雄性存活率（回补成功与否）；蛹长度（gain-of-function 表型）。

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|----------------|------|
| 跨物种 D-site 序列聚类 | D-site 在组内保守、组间分化 | 274 条序列，阈值 0.2 相似性网络 | 4 个聚类组，组内保守 | D-site 存在系统发育信号，非完全随机漂变 | 无法确定组间功能差异 | Results 节；图 1C |
| AF2 复合物预测（人 vs 果蝇） | D-site 结合同一 DRS 沟槽 | 人/果蝇 MEK-ERK 复合物 | 两物种均结合 DRS，接触模式相似 | 互作模式跨物种保守 | AF2 可能高估 IDR 有序性 | Results 节；图 2A |
| MD 接触图（人 vs 果蝇） | 关键接触残基在 MD 中稳定 | 1 μs 轨迹，接触频率 >50% | 五残基（K3/K5/I9/L11/D16）接触模式保守 | 关键残基功能保守 | MD 力场对 IDR 的适用性有限 | Results 节；图 2C |
| MEK5A 突变 MD | 五残基同时突变导致解离 | WT vs MEK5A，16 条轨迹 | MEK5A 在 600 ns 内解离 | 五残基对结合必需 | 单残基贡献未单独测试 | Results 节；图 3A |
| 果蝇 ΔD-site 回补 | D-site 缺失导致功能丧失 | ΔD-site vs WT 回补 | ΔD-site 无法回补雄性存活 | D-site 对体内 ERK 信号绝对必需 | 无法区分结合缺陷与折叠缺陷 | Results 节；图 4B |
| 果蝇 4A 突变 + Q56P | D-site 突变抑制组成性激活表型 | Q56P vs Q56P+4A | 4A 突变消除缩短蛹表型 | D-site 对组成性激活也必需 | 机制（结合 vs 变构）未完全解析 | Results 节；图 4C |

## 11 结论正确解读
- **任务范围**：本文仅针对 MEK-ERK 这一对互作蛋白，不涉及其他 MAPK 模块或更广泛的 IDR 互作网络。
- **oracle/真值输入**：AF2 预测结构作为 MD 起点，未用实验结构（如晶体结构）验证；MD 力场为 CHARMM36，对 IDR 的构象采样可能不充分。
- **端到端状态**：计算预测（AF2+MD）与体内功能验证（果蝇）整合，但未做体外结合实验（如 ITC、SPR）直接量化突变对亲和力的影响。
- **算力成本**：未报告具体 GPU 时数或集群规模。
- **历史数据依赖**：序列分析依赖前作数据集（Ref. 11），该数据集可能包含注释错误或物种采样偏差。
- **模型依赖**：AF2 对 IDR 复合物的预测能力有限，pLDDT 60-80 属于中等置信度；MD 的力场参数对 IDR 的适用性未做系统验证。
- **最难情形**：果蝇与人类 D-site 长度差异（果蝇 IDR 更长）可能影响直接序列比对的可比性；作者未讨论 IDR 长度变异对结合动力学的影响。
- **群体/领域边界**：结论限于后生动物；植物、真菌等物种的 MEK-ERK 同源系统未纳入。
- **不确定性**：作者未报告 MD 模拟的系综收敛性分析；解离时间阈值（15 Å）为任意选择，未做敏感性测试。
- **有边界的复述**：在分析的 274 个后生动物物种中，MEK 的 D-site 序列在系统发育组内保守、组间分化，五个关键残基（K3、K5、I9、L11、D16）通过静电/疏水接触与 ERK 的 DRS 互作；果蝇体内实验表明该 D-site 对 ERK 信号和个体存活绝对必需，且 D-site 突变可抑制组成性激活 MEK 的过度信号表型。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 变构机制的推测性 | D-site 对活性位点稳定性的影响基于 RMSD 间接推断，未直接测量催化活性 | 未明确提及 | Discussion 节 "suggesting a potential allosteric mechanism"（作者用 "potential" 限定） |
| 跨物种功能验证有限 | 仅在果蝇中验证，未在脊椎动物中测试 | 未明确提及 | Results 节（仅果蝇实验） |
| 临床变异分析为观察性 | 人类 D-site 变异极罕见，但未做功能验证 | 未明确提及 | Discussion 节 "no variation in key residues... was found in large-scale human variant datasets" |
| 链接长度变异的推测性 | 果蝇 IDR 更长可能影响结合动力学，但未实验验证 | "this hypothesis merits future investigation" | Discussion 节 |

**作者提及的相关约束**（非正式局限）：作者在 Discussion 中提到 D-site 的进化分析依赖序列比对质量，而 IDR 区域的比对本身具有不确定性；此外，MD 模拟虽为 1 μs，但 IDR 的构象空间可能未充分采样。

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| AF2 预测的 D-site 结合构象可能不代表真实溶液构象 | AF2 对 IDR 复合物的预测偏向稳定构象，可能高估结合亲和力；MD 从 AF2 结构出发可能陷入局部能量最小值 | IDR 互作本质是动态的，静态结构可能误导功能推断 | 用增强采样方法（如 replica exchange MD、metadynamics）从游离态 IDR 开始模拟结合过程；或与实验 SAXS/FRET 数据对比 | Results 节 "pLDDT 60-80" 属于中等置信度；Methods 节 MD 从 AF2 结构开始 |
| 五残基同时突变（MEK5A）无法区分各残基贡献 | 可能只有其中 1-2 个残基是关键，其余为冗余；4A 突变（不含 D16）在体内也完全丧失功能，说明 D16 可能非必需 | 药物设计需要明确热点残基 | 逐点突变 + 丙氨酸扫描 + 结合实验 | Results 节 "MEK4A failed to rescue" 与 "MEK5A" 结果对比 |
| 果蝇存活率作为读数过于粗粒度 | 存活率无法区分部分功能保留；可能 D-site 突变体在特定组织/发育阶段仍有残余功能 | 信号通路的功能冗余可能掩盖精细表型 | 组织特异性表达、温度敏感型等位基因、下游报告基因检测 | Results 节仅报告存活率 |
| 进化分析仅用 MEK 单侧序列 | ERK 侧 DRS 的保守性分析未系统量化（仅定性描述） | 不对称共进化的核心 claim 需要双侧量化比较 | 对 ERK DRS 区域计算同样的 entropy 和聚类分析 | Results 节对 ERK 的描述为 "highly conserved"，但未给出 entropy 数据 |
| MD 模拟温度（375 K）仅用于 MEK5A | 高温可能加速解离，但 WT 未在相同条件下比较 | 解离动力学差异可能部分由温度效应而非突变效应导致 | 在相同温度下运行 WT 模拟作为对照 | Methods 节 "16 replicates at 375 K for the MEK5A mutant" |
| 未报告 MD 模拟的力场验证 | CHARMM36 对 IDR 的适用性有文献争议 | 力场选择可能影响接触图结论 | 用不同力场（如 AMBER ff19SB、CHARMM36m）重复关键模拟 | Methods 节仅提及 CHARMM36 |

## 14 Agent 提炼的知识候选
1. **「化学补丁」保守性分析框架**：对于 IDR 内的 SLiM 基序，跨物种比较不应仅看序列同一性，而应关注关键残基的理化性质（电荷、疏水性、体积）是否维持。可迁移到 IDP/IDR 相分离研究：对驱动相分离的 IDR 区域进行跨物种分析时，可识别「化学补丁」而非序列基序，以预测保守的相分离行为。
2. **AF2 + MD 的 IDR 复合物验证流程**：先用 AF2 Multimer 预测 IDR-折叠蛋白复合物，再用长时程 MD 验证接触稳定性。此流程可迁移到 IDP/IDR 互作研究：当 AF2 对 IDR 单独预测置信度低时，与折叠伙伴共预测可提高置信度；MD 可提供接触频率和动力学信息。
3. **网络架构不对称性作为进化速率预测因子**：hub 蛋白（多伙伴）的互作界面趋于保守，非 hub 蛋白（少伙伴）的互作界面趋于分化。此原则可迁移到相分离研究：评估凝聚体组分蛋白的互作界面进化速率时，可先判断其在互作网络中的 hub 属性，以预测保守程度。
4. **变构耦合的 RMSD 检测方法**：通过比较 D-site 结合/解离状态下活性位点的 RMSD 变化，推断变构效应。可迁移到 IDP/IDR 研究：当 IDR 结合伙伴后，可监测远端功能域（如催化位点、其他互作界面）的构象变化，以识别变构调控。
5. **CRIMIC 系统用于 IDR 功能验证**：利用内源基因敲入 GAL4 + UAS-转基因回补，在体内严格检验 IDR 突变体的功能。可迁移到相分离研究：在果蝇等模式生物中验证 IDR 突变对凝聚体形成和生理功能的影响。
6. **多重复 MD 的解离动力学分析**：用多条独立轨迹的累积解离曲线（F(t)）量化结合稳定性。可迁移到 IDP/IDR 互作研究：对弱/动态互作，单条轨迹不足以表征结合稳定性，需多条轨迹的统计描述。

## 15 与已有知识连接
- **MEK-ERK 互作的结构基础**：本文确认了此前生化研究（如 Ref. 21, 22, 30）提出的 D-site-DRS 互作模型，并提供了原子级结构预测和动态验证。与经典 MAPK  docking 基序研究（如 KIM 基序）一致。
- **SLiM 进化理论**：本文与 Davey et al. 等关于 SLiM 快速进化的研究一致，但补充了「网络架构不对称性」作为进化速率差异的解释变量。
- **AlphaFold2 在 IDR 研究中的应用**：本文与近期文献（如 Ruff & Pappu 2021, 关于 AF2 对 IDR 预测的局限性）一致，但展示了 AF2 在 IDR-折叠蛋白复合物预测中的可用性。
- **MD 模拟在 IDR 互作中的应用**：本文与 IDP 结合机制研究（如 fuzzy complex 模型）相关，MD 揭示的多种结合模式支持 IDR 互作的构象多样性。
- **果蝇 MAPK 信号研究**：本文使用的 CRIMIC 系统与果蝇遗传学工具（如 Gabay et al. 1997 的 MAPK 通路研究）一脉相承。
- **与相分离研究的潜在连接** [Analysis]：MEK 的 D-site 是 IDR，ERK 的 DRS 是折叠域上的浅沟槽。这种「IDR-折叠域」互作模式与相分离中「IDR-折叠域」相互作用（如 SPOP-MATH 与 DAXX IDR）具有相似性。本文的进化分析框架可迁移到相分离组分蛋白的进化研究。

## 16 Agent 生成的研究候选
1. **候选名称**：IDR 介导互作的「化学补丁」进化分析工具
   - **来源局限/观察**：本文对 MEK D-site 的理化性质保守性分析是手动进行的，缺乏自动化工具
   - **核心假设**：IDR 内驱动互作的关键残基可通过理化性质保守性（而非序列保守性）自动识别
   - **初步方法**：开发基于氨基酸理化性质（电荷、疏水性、体积）的保守性打分，应用于大规模 IDR 互作组学数据
   - **验证方式**：与已知 SLiM 数据库（ELM）比较，并在相分离相关 IDR 上测试
   - **创新状态**：unverified

2. **候选名称**：AF2-MD 联合流程用于 IDR 互作界面预测的基准测试
   - **来源局限/观察**：本文用 AF2+MD 研究单一体系，未系统评估该方法在多种 IDR 互作中的适用性
   - **核心假设**：AF2+MD 对 IDR-折叠域互作的预测准确率与 IDR 长度、结合亲和力、构象异质性相关
   - **初步方法**：收集已知 IDR-折叠域复合物数据集，运行 AF2 预测 + 短 MD 验证，与实验结构/亲和力数据比较
   - **验证方式**：与实验结合数据（ITC、NMR）对比，建立适用性预测规则
   - **创新状态**：unverified

3. **候选名称**：MAPK 家族 docking 基序的跨物种共进化网络分析
   - **来源局限/观察**：本文仅分析 MEK-ERK 一对互作，MAPK 家族其他成员（如 p38、JNK）的 docking 基序进化模式未知
   - **核心假设**：MAPK 家族各成员的 docking 基序进化速率与其互作网络规模成反比
   - **初步方法**：对 MAPK 家族所有成员的 docking 基序进行跨物种分析，结合互作组数据（BioGRID）量化网络规模
   - **验证方式**：统计检验网络规模与进化速率的相关性
   - **创新状态**：unverified

4. **候选名称**：IDR 变构效应的 MD 检测标准
   - **来源局限/观察**：本文用 RMSD 推断变构效应，但缺乏系统标准
   - **核心假设**：IDR 结合/解离导致的远端域 RMSD 变化可作为变构效应的可靠指标
   - **初步方法**：在多个已知变构体系（含 IDR 参与）中测试 RMSD、动态网络分析、自由能景观等方法
   - **验证方式**：与实验变构数据（如氢氘交换、NMR）对比
   - **创新状态**：unverified

5. **候选名称**：相分离驱动 IDR 的进化保守性分析
   - **来源局限/观察**：本文的进化分析框架可迁移到相分离相关 IDR
   - **核心假设**：驱动相分离的 IDR 区域在物种间表现出「化学补丁」保守性，而非序列保守性
   - **初步方法**：收集已知相分离相关 IDR（如 FUS、hnRNPA1、DDX4），进行跨物种理化性质保守性分析
   - **验证方式**：与实验相分离行为数据（体外凝聚实验）关联
   - **创新状态**：unverified