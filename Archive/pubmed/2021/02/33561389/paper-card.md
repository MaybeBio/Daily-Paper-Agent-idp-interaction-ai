## 01 基本信息

- **标题**: An intrinsically disordered region-mediated confinement state contributes to the dynamics and function of transcription factors
- **作者**: Garcia, David A; Johnson, Thomas A; Presman, Diego M; Fettweis, Gregory; Wagh, Kaustubh; Rinaldi, Lorenzo; Stavreva, Diana A; Paakinaho, Ville; Jensen, Rikke A M; Mandrup, Susanne; Upadhyaya, Arpita; Hager, Gordon L
- **单位**: National Cancer Institute, NIH (Hager实验室为主); 其他作者来自 University of Maryland, University of Southern Denmark 等
- **期刊/平台**: Molecular Cell
- **年份**: 2021
- **论文类型**: 研究论文（实验 + 机器学习数据分析）
- **领域**: 转录因子动力学、单分子追踪、无序蛋白区域、相分离、基因调控
- **关键词**: intrinsically disordered region (IDR), single-molecule tracking (SMT), glucocorticoid receptor (GR), confinement state, machine learning, pEM, power-law, liquid-liquid phase separation
- **DOI/arXiv**: 10.1016/j.molcel.2021.01.013
- **代码**: pEMv2 (https://github.com/p-koo/pEMv2)；SMT追踪代码为定制MATLAB脚本（未公开）
- **数据**: ChIP-seq (GEO: GSE154771, GSE108634)；SMT原始数据样本 (Mendeley Data: https://doi.org/10.17632/k6g3xtr5k3.1)
- **阅读日期**: 2026-05-13（按当前日期）
- **在该课题方向中的位置**: 本文是IDR介导的转录因子凝聚/限域行为与单分子动力学结合的代表性工作，首次将ML分类方法（pEM）应用于TF单分子轨迹，区分出IDR依赖的"confinement"状态，为IDP/IDR介导的蛋白互作与相分离研究提供了单分子水平的动态证据和数据分析范式。

## 02 一句话总结

本文通过单分子追踪（SMT）结合机器学习分类方法（pEM），发现糖皮质激素受体（GR）在细胞核内存在四种扩散状态，其中一种新的"confinement"状态由GR的 intrinsically disordered region (IDR) 介导，与特异性染色质结合状态在动力学上可区分，且该状态通过增加TF局部浓度来调节转录输出。

## 03 研究问题

- **具体问题**: 转录因子（TF）在细胞核内搜索并结合靶位点的过程中，除了已知的特异性染色质结合和非特异性扩散外，是否存在由IDR介导的、功能上可区分的动力学状态？该状态如何影响TF的驻留时间和转录功能？
- **为什么重要**: TF如何在复杂的核环境中高效找到靶位点一直是基因调控的核心问题。IDR介导的相分离/凝聚体被认为是转录调控的重要机制，但缺乏单分子水平的直接动力学证据。如果IDR介导的confinement状态确实存在，它将为"凝聚体如何促进TF搜索靶位点"提供定量解释。
- **现有方法不足**: 传统SMT分析通常将TF动力学简化为"结合"与"自由扩散"两类，无法区分不同亚型的受限运动；且多数研究未将IDR的贡献纳入动力学模型。此外，传统双指数拟合无法捕捉幂律分布的尾部行为。
- **精确研究问题**: Can single-molecule tracking combined with unsupervised machine learning distinguish an IDR-mediated confinement state from specific chromatin binding in living cells, and does this state contribute to transcriptional output?

## 04 背景与发展脉络

*注：此脉络基于本文引用和讨论，属于「经外部核验」的领域发展框架。*

1. **TF动力学研究的早期阶段（~2000s）**: FRAP和FLIP技术揭示TF与染色质相互作用是瞬态的（秒级），提出"hit-and-run"模型。代表：McNally et al., 2000; Hager et al., 2009。
2. **单分子追踪（SMT）兴起（~2010s）**: 光激活定位显微镜（PALM）和HiLO技术使单TF分子追踪成为可能，揭示TF扩散的异质性。代表：Izeddin et al., 2014; Gebhardt et al., 2013。
3. **动力学状态分类的统计方法（~2015-2020）**: 隐马尔可夫模型（HMM）和pEM等无监督学习方法被引入SMT数据分析，用于区分不同扩散状态。代表：Koo et al., 2015; Persson et al., 2013。
4. **IDR与相分离在转录中的作用（~2017-2020）**: 体外和细胞实验表明TF的IDR可驱动液-液相分离（LLPS），形成转录凝聚体。代表：Boija et al., 2018; Sabari et al., 2018; Cho et al., 2018。
5. **本文位置（2021）**: 首次将ML分类的SMT分析与IDR功能直接关联，在活细胞中区分出IDR介导的confinement状态，并证明其与染色质结合在动力学上独立、在功能上协同。该工作为后续IDR/相分离与TF搜索机制研究提供了单分子动力学框架。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| TF动力学状态分类过于简化 | 传统分析仅区分"结合"与"扩散"，无法捕捉IDR介导的受限运动 | 缺乏能自动识别多扩散状态的无监督分类方法；IDR介导的confinement与染色质结合在MSD上部分重叠 | Results 图1B-C：pEM识别出4个状态，而传统方法仅能区分2-3个 |
| IDR对TF动力学的影响缺乏直接证据 | 虽有体外凝聚体实验，但活细胞中IDR如何改变TF运动未知 | 缺乏将IDR操作与单分子动力学结合的系统方法 | Results 图3B：GR407C（去IDR）完全丧失confinement状态 |
| 幂律分布的生物学来源不明 | TF驻留时间呈幂律分布，但无法归因于特定分子机制 | 幂律可能来自染色质异质性或IDR介导的蛋白互作网络，需分离各贡献 | Results 图5G：confinement和chromatin binding各自均呈幂律，但来源不同 |
| 凝聚体/相分离的功能验证困难 | 凝聚体与转录活性的因果关系难以在活细胞中直接证明 | 缺乏将动力学状态与转录输出定量关联的方法 | Results 图5I：GRdim（低转录活性）的chromatin binding驻留时间显著短于GRwt |
| SMT数据分析的主观性 | 传统阈值法依赖人为设定参数 | 需要无偏的、数据驱动的分类方法 | Methods：pEM使用贝叶斯信息准则自动确定状态数 |

## 05 核心思想

### 1) 表面方法

- 对HaloTag融合的GR（野生型及多种突变体）进行活细胞单分子追踪（SMT），使用HiLO照明和PA-JF549光激活荧光团
- 使用pEM（perturbation expectation-maximization）无监督机器学习方法对单分子轨迹进行分类，基于MSD特征自动识别不同扩散状态
- 结合ChIP-seq、转录活性测定和共聚焦成像，将动力学状态与功能关联

### 2) 核心洞察

- **TF的"结合"并非单一状态**：pEM识别出两种可区分的低迁移率状态——"chromatin binding"（最受限）和"confinement"（中等受限），前者依赖DNA结合域（DBD），后者依赖IDR。
- **IDR介导的confinement独立于DNA结合**：DBD突变体（GR-C428G）丧失chromatin binding但保留confinement；IDR缺失突变体（GR407C）丧失confinement但保留chromatin binding。两者在动力学上正交。
- **Confinement通过增加局部浓度促进转录**：IDR介导的confinement将TF限制在特定核区域，提高局部浓度，从而增加kon（结合速率），而非延长koff（驻留时间）。GRdim（转录缺陷突变体）的confinement正常但chromatin binding驻留时间缩短，说明两者协同。
- **幂律分布的双重来源**：chromatin binding的幂律来自靶位点异质性（motif强度差异），confinement的幂律来自IDR介导的蛋白互作网络异质性。

### 3) 可能的普适教训 [Analysis]

- **动力学状态的正交分解**：将"结合"分解为DNA介导和蛋白互作介导的两个正交维度，这一思路可推广到其他TF/IDP系统——任何TF的"结合"都可能包含IDR介导的confinement贡献。
- **ML分类+遗传操作的组合策略**：pEM无监督分类与系列突变体（DBD突变、IDR缺失、转录缺陷）结合，可系统性地将动力学状态映射到分子功能域，这一范式适用于其他IDP/IDR互作研究。
- **幂律分布作为异质性指标**：幂律而非指数分布提示系统存在广泛的亲和力/互作强度分布，这对IDP介导的多价互作研究具有方法论启示。

## 07 方法总览

**输入**：
- 活细胞中单分子SMT时间序列（12ms/200ms/500ms采集间隔）
- HaloTag融合蛋白：GRwt、GR-C428G（DBD突变）、GRmon（单体化）、GR407C（IDR缺失）、GRdim（A465T）、PPARα（天然短IDR）、H2B（对照）

**输出**：
- 每个轨迹的扩散状态分类（4种状态）
- 每种状态的MSD曲线、扩散系数、驻留时间分布
- 各突变体的状态比例和动力学参数对比

**模块**：
1. **SMT数据采集模块**：HiLO显微镜，PA-JF549光激活，连续成像
2. **轨迹追踪模块**：TrackRecord软件（MATLAB），最近邻算法
3. **pEM分类模块**：无监督ML，基于MSD特征自动确定状态数并分类
4. **MSD分析模块**：计算各状态的ensemble MSD和扩散系数
5. **驻留时间分析模块**：Kaplan-Meier生存分析，幂律vs指数模型拟合
6. **功能验证模块**：ChIP-seq（染色质结合位点）、转录活性报告基因、共聚焦成像（凝聚体观察）

**流程**：
1. 细胞培养并转染HaloTag融合蛋白，标记PA-JF549
2. 激素激活（Dex/Cort）后，HiLO成像采集单分子轨迹
3. TrackRecord追踪粒子，生成轨迹集
4. pEM对轨迹分类，确定最优状态数
5. 对每个状态计算MSD、扩散系数、状态比例
6. 对每个状态计算驻留时间分布，拟合幂律/指数模型
7. 对突变体重复上述流程，比较状态差异
8. ChIP-seq验证chromatin binding状态对应基因组结合位点
9. 转录活性测定关联confinement比例与功能输出

**反馈回路**：pEM分类结果指导突变体设计（如GR407C验证IDR假说），突变体数据反过来验证分类的生物学意义。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| pEM分类模块 | 无监督识别扩散状态 | 传统阈值法无法区分confinement与chromatin binding | 输入：轨迹集；输出：状态数K和每个轨迹的状态归属 | Results 图1B-C：BIC确定K=4；图2A：两种低迁移率状态MSD可区分 | 预期影响：无法区分confinement与chromatin binding，IDR功能将被掩盖（[Analysis] 基于pEM是核心创新点） |
| 突变体系列 | 遗传学验证状态的功能归属 | 需要将动力学状态映射到分子功能域 | 输入：GRwt/GR-C428G/GR407C/GRmon/GRdim；输出：各状态比例和动力学参数 | Results 图2B：GR-C428G丧失状态1；图3B：GR407C丧失状态2 | 实测影响：无突变体则无法证明confinement的IDR依赖性（作者通过系列突变体系统验证） |
| 驻留时间分析 | 区分幂律vs指数分布 | 幂律提示异质性互作网络，指数提示单一亲和力 | 输入：各状态的轨迹；输出：生存曲线、幂律指数 | Results 图5A-E：GRwt呈幂律，GR407C/PPARα呈双指数 | 预期影响：无法揭示IDR介导的异质性互作（[Analysis] 幂律是confinement功能的重要证据） |
| ChIP-seq验证 | 确认chromatin binding状态的基因组定位 | 需要将单分子动力学与基因组结合位点关联 | 输入：GRwt/GR407C/GR-C428G细胞；输出：全基因组结合峰 | Results 图3C：GR407C结合峰数从4410降至898 | 实测影响：无ChIP-seq则无法确认状态1的染色质结合属性 |
| 转录活性测定 | 关联confinement与功能输出 | 需要证明confinement的生物学意义 | 输入：各突变体细胞；输出：内源靶基因表达水平 | Results 图5I：GRdim的chromatin binding驻留时间短，转录活性低 | 预期影响：无法建立动力学-功能因果链（[Analysis] 转录活性是最终功能验证） |

## 09 关键公式符号

**1. 均方位移（MSD）**：
MSD(τ) = ⟨|r(t+τ) - r(t)|²⟩ = 2nDτ + c

- τ: 时间间隔
- r(t): t时刻粒子位置
- n: 空间维度（此处n=2）
- D: 扩散系数
- c: 定位噪声常数

**用途**：判断扩散类型（线性=布朗运动，亚线性=受限扩散）

**2. 扩散系数估计**：
⟨v²⟩ = 4D/Δt

- v: 瞬时速度向量
- Δt: 采集间隔

**用途**：从瞬时速度方差估计扩散系数

**3. 幂律分布**：
S(t) ∝ t^(-α)

- S(t): 生存函数（驻留时间>t的概率）
- α: 幂律指数

**用途**：描述confinement和chromatin binding的驻留时间分布

**4. 贝叶斯信息准则（BIC）**：
BIC(M) = k·ln(n) - 2·ln(P(D|θ̂, M))

- k: 模型参数数量
- n: 观测数量
- P(D|θ̂, M): 模型M下数据的似然

**用途**：确定pEM最优状态数和模型选择（幂律vs双指数vs三指数）

**5. 光漂白校正**：
S(t) = e^(γt) · S_E(t)

- γ: 光漂白速率
- S_E(t): 实验观测的生存函数

**用途**：从H2B数据估计γ，校正TF驻留时间

## 10 实验设计与证据链

**数据集/群体**：
- 细胞系：3617小鼠乳腺腺癌细胞及其衍生系（GRKO背景）
- 蛋白：GRwt、GR-C428G、GRmon、GR407C、GRdim、PPARα、H2B（均为HaloTag融合）
- 激素：地塞米松（Dex，合成激动剂）、皮质酮（Cort，天然激素）
- SMT数据量：每种条件至少20个细胞（慢采集）或60-100个细胞（快采集），3次以上生物学重复

**指标**：
- 扩散状态数及比例
- 各状态扩散系数
- 驻留时间分布（幂律指数α）
- ChIP-seq峰数
- 转录活性（内源靶基因mRNA水平）

**评测协议**：
- pEM分类后，用BIC确定最优状态数
- 驻留时间用Kaplan-Meier估计，BIC比较幂律vs指数模型
- 突变体与野生型逐一对比

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|-------------|-------------------|------|
| pEM分类GRwt（12ms） | GR存在多种扩散状态 | GRwt+Dex vs 固定细胞 | 4种状态，2种高迁移率+2种低迁移率 | GR动力学高度异质 | 未直接证明4种状态的生物学功能 | Results 图1B-C |
| GR-C428G（DBD突变） | 状态1=特异性染色质结合 | GRwt vs GR-C428G，均+Dex | 状态1消失，状态2保留 | 状态1依赖DNA结合 | 不能排除其他DBD功能贡献 | Results 图2B |
| GR407C（IDR缺失） | 状态2=IDR介导的confinement | GRwt vs GR407C，均+Dex | 状态2消失，状态1保留 | 状态2依赖IDR | 不能排除IDR影响蛋白折叠 | Results 图3B |
| PPARα（天然短IDR） | 短IDR不足以产生confinement | GRwt vs PPARα，各自配体激活 | PPARα无confinement状态 | IDR长度/性质决定confinement | 不能排除PPARα特异性因素 | Results 图3H |
| 驻留时间分布（500ms） | confinement和binding均呈幂律 | GRwt各状态分别拟合 | 两者均幂律，指数不同 | 两种状态均有异质性互作 | 幂律来源（亲和力谱vs几何限制）未直接证明 | Results 图5A-E |
| GRdim（转录缺陷） | confinement与转录活性相关 | GRwt vs GRdim | confinement相似，binding驻留时间缩短 | 转录活性需要长驻留时间 | 因果关系未直接证明 | Results 图5I |
| 阵列实验（MMTV） | confinement在靶位点富集 | 阵列区域vs核质 | 阵列区域confinement比例升高 | confinement促进局部浓度增加 | 未直接测量局部浓度 | Results 图2F-H |

## 11 结论正确解读

- **任务范围**: 本研究仅针对糖皮质激素受体（GR）及其突变体在3617小鼠细胞系中的动力学行为。结论不直接推广到所有TF或所有细胞类型。
- **Oracle/真值输入**: 无外部oracle。pEM分类是无监督的，状态数由BIC决定；"chromatin binding"和"confinement"的生物学注释是通过突变体表型推断的，而非直接测量分子互作。
- **端到端状态**: 从SMT数据到功能结论的链条完整，但中间环节（如confinement的分子组成、物理性质）未直接验证。
- **算力成本**: pEM计算在常规工作站可完成，无特殊算力需求。
- **历史数据依赖**: 依赖先前发表的GR ChIP-seq和ATAC-seq数据（GSE108634）进行对比分析。
- **模型依赖**: 结论依赖pEM分类的准确性；pEM假设轨迹可分割为离散扩散状态，可能忽略连续状态转换。
- **最难情形**: 快速扩散分子（高迁移率状态）难以精确追踪，可能低估扩散比例；长驻留时间尾部受光漂白影响，需H2B校正。
- **群体/领域边界**: 结论基于细胞系实验，未在组织或体内验证；GR是配体激活的TF，其他TF可能不依赖配体。
- **不确定性**: 幂律分布的精确指数未报告置信区间；confinement与凝聚体的直接对应关系（如是否共定位）未直接证明。

**有边界的复述**: 在3617小鼠细胞中，GR的IDR介导一种可检测的confinement扩散状态，该状态独立于DNA结合、依赖IDR、呈幂律驻留时间分布，且与转录活性相关。该结论适用于GR系统，其普适性需在其他TF中验证。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 快速扩散群体无法完全解析 | HiLO技术仅能追踪低迁移率分子，高迁移率状态可能被低估 | 需要更高时间分辨率的3D追踪技术 | Limitations of study |
| 未考虑状态间转换 | 轨迹被分割为固定长度片段，可能遗漏单轨迹内的状态转换 | 使用贝叶斯非参数方法识别状态转换 | Limitations of study |
| confinement与凝聚体的直接联系未建立 | 未直接观察confinement状态下的分子是否位于凝聚体中 | 需要结合超分辨成像与SMT | Discussion |
| 光漂白限制长驻留时间测量 | 荧光团寿命限制了对长驻留时间尾部的精确量化 | 使用更稳定的荧光团或降低激发功率 | Limitations of study |
| 仅研究了GR一个系统 | 结论可能不适用于其他TF | 需要在其他TF中验证confinement的普遍性 | Discussion |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|-------------------|----------|----------|------|
| pEM分类的"confinement"可能包含多种物理过程 | 除IDR介导的蛋白互作外，可能与核骨架、RNA、染色质非特异互作有关 | 若confinement是多种机制的混合，则IDR特异性结论被削弱 | 使用IDR点突变（而非完全删除）结合交联质谱鉴定互作伙伴 | Results 图3B仅用完全删除突变体 |
| GR407C的转录缺陷可能不完全归因于confinement缺失 | IDR删除可能影响蛋白折叠、稳定性或核定位 | 若存在混杂因素，则confinement-转录因果链不成立 | 检测GR407C的蛋白表达水平、核质分布和配体结合能力 | Results 图3C显示ChIP-seq峰减少，但未报告蛋白水平 |
| 幂律分布拟合的稳健性未充分讨论 | 有限时间窗口内，幂律和重尾指数分布可能难以区分 | 若实际为指数分布，则"异质性互作"解释不成立 | 报告拟合优度、置信区间，使用更长时间窗口验证 | Results 图5A-E未报告拟合参数的不确定性 |
| 阵列实验的confinement富集可能反映染色质密度而非IDR互作 | 阵列区域染色质高度浓缩，可能非特异限制所有蛋白运动 | 若为染色质密度效应，则confinement的IDR特异性被高估 | 使用不结合DNA的IDR融合蛋白在阵列区域检测confinement | Results 图2F-H未设置此对照 |
| 转录活性与confinement的相关性不等于因果性 | 可能通过其他IDR功能（如直接激活转录机器）实现 | 若为间接关联，则"局部浓度增加"模型不成立 | 使用光遗传学工具人为诱导confinement并检测转录 | Results 图5I仅显示相关性 |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **pEM无监督分类范式**：将pEM（或类似ML聚类方法）应用于SMT轨迹分析，可自动识别传统方法无法区分的扩散亚状态。本课题可迁移：对IDP/IDR介导的互作体系，使用pEM区分"特异性结合"与"IDR介导的confinement"两种低迁移率状态，避免人为设定阈值。

2. **正交遗传学验证策略**：通过系列突变体（DBD突变 vs IDR删除）将动力学状态正交分解，证明两个状态在分子机制上独立。本课题可迁移：研究任意IDP/IDR介导的互作时，可设计"互作界面突变"与"IDR删除"两组突变体，系统性地将动力学状态映射到分子功能域。

3. **幂律分布作为异质性指标**：驻留时间呈幂律而非指数分布，提示系统存在广泛的亲和力谱。本课题可迁移：在IDP介导的相分离体系中，测量单个分子的驻留时间分布，若呈幂律则提示多价互作的异质性，可进一步分析幂律指数与凝聚体性质的关系。

4. **confinement与binding的动力学解耦**：IDR介导的confinement不直接延长驻留时间，而是通过增加局部浓度提高kon。本课题可迁移：在相分离/凝聚体研究中，区分"凝聚体内的受限扩散"与"凝聚体上的特异性结合"两种机制，分别测量kon和koff的贡献。

5. **H2O作为光漂白校正参照**：使用H2B（染色质结合蛋白）作为光漂白校正参照，可分离光漂白与真实解离的贡献。本课题可迁移：在IDP凝聚体研究中，使用已知驻留时间的对照蛋白校正光漂白，提高长驻留时间测量的准确性。

6. **ChIP-seq与SMT的互补验证**：ChIP-seq提供群体水平的结合位点信息，SMT提供单分子水平的动力学信息，两者结合可建立"结合位点-动力学状态"的对应关系。本课题可迁移：对IDP/IDR互作体系，结合ChIP-seq（或CUT&Tag）与SMT，验证confinement状态是否对应特定基因组区域。

## 15 与已有知识连接

- **相似工作**: Garcia et al., 2020 (bioRxiv, 同一团队前期工作) 报道了GR驻留时间的幂律分布，本文在此基础上进一步区分了confinement和binding两种状态。连接：本文是前者的机制深化。
- **相似工作**: Koo et al., 2015 (pEM方法原始论文) 在体外系统验证了pEM的聚类能力。连接：本文首次将pEM应用于哺乳动物TF的核内SMT数据。
- **相似工作**: Sabari et al., 2018 (Science) 和 Boija et al., 2018 (Science) 展示了TF IDR介导的相分离凝聚体在转录调控中的作用。连接：本文为这些凝聚体假说提供了单分子动力学证据，但未直接观察凝聚体。
- **相似工作**: Cho et al., 2018 (Science) 和 Chong et al., 2018 (Science) 展示了RNA Pol II IDR的相分离行为。连接：本文的confinement状态可能对应这些凝聚体内部的受限扩散。
- **相似工作**: Hansen et al., 2020 (Nature Cell Biology) 报道了TF的"transient confinement"现象，但未归因于IDR。连接：本文通过突变体实验将confinement明确归因于IDR。
- **冲突/差异**: 部分研究认为TF的亚扩散行为主要来自染色质拓扑限制（如Bénichou et al., 2011），本文的confinement状态可能被这些模型解释为染色质密度效应。连接：本文通过IDR删除突变体排除了纯几何解释。
- **可迁移领域**: 本文的pEM+SMT+突变体策略可直接迁移到其他IDP/IDR介导的互作研究，如FUS、TDP-43、α-synuclein等神经退行性疾病相关蛋白的凝聚体动力学研究。

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**: IDR介导的confinement在人工凝聚体中的单分子验证
   - **来源局限/观察**: 本文未直接观察confinement状态下的分子是否位于凝聚体中，仅通过IDR删除间接推断
   - **核心假设**: 人工诱导的IDR凝聚体可产生与GR confinement相同的单分子动力学特征
   - **初步方法**: 使用光遗传学工具（如CRY2/CIB1）在活细胞中诱导IDR凝聚体形成，同时进行SMT追踪，比较凝聚体形成前后的扩散状态变化
   - **验证方式**: 若凝聚体形成后出现confinement状态且与IDR长度相关，则支持confinement=凝聚体内部受限扩散的假说
   - **创新状态**: unverified

2. **候选名称**: AlphaFold预测的IDR互作网络与confinement动力学的关联
   - **来源局限/观察**: 本文提出confinement源于IDR介导的蛋白互作网络，但未预测具体互作伙伴
   - **核心假设**: AlphaFold/AlphaFold-Multimer预测的IDR互作强度与confinement状态的驻留时间呈正相关
   - **初步方法**: 对GR的IDR进行AlphaFold-Multimer预测，筛选高置信度互作伙伴；构建IDR突变体破坏预测互作界面，检测confinement状态的变化
   - **验证方式**: 若破坏预测互作界面后confinement消失或减弱，则支持计算预测与实验动力学的一致性
   - **创新状态**: unverified

3. **候选名称**: 无序区长度与confinement状态的定量关系
   - **来源局限/观察**: 本文仅比较了GR（长IDR）和PPARα（短IDR），未系统扫描IDR长度
   - **核心假设**: IDR长度与confinement状态的驻留时间呈幂律关系
   - **初步方法**: 构建GR IDR系列截短突变体（如保留25%、50%、75%），SMT测量各突变体的confinement驻留时间，拟合长度-驻留时间关系
   - **验证方式**: 若存在明确的标度关系，可为IDR介导的互作网络模型提供定量约束
   - **创新状态**: unverified

4. **候选名称**: MD模拟与SMT数据的多尺度整合
   - **来源局限/观察**: 本文的confinement状态缺乏分子层面的结构解释
   - **核心假设**: 粗粒化MD模拟可重现confinement状态的扩散特征，并揭示IDR互作的分子机制
   - **初步方法**: 使用粗粒化MD（如MARTINI或HPS模型）模拟GR IDR在核环境中的扩散，计算MSD并与SMT数据对比；调整IDR互作参数以匹配实验驻留时间分布
   - **验证方式**: 若模拟能定量重现confinement状态的MSD和驻留时间，则提供机制解释
   - **创新状态**: unverified

5. **候选名称**: 凝聚体内部与外部TF的差异化转录输出
   - **来源局限/观察**: 本文提出confinement通过增加局部浓度提高kon，但未直接测量凝聚体内部TF的转录活性
   - **核心假设**: 凝聚体内部TF的转录输出高于外部，且差异源于kon而非koff
   - **初步方法**: 使用双色荧光标记（凝聚体标记+TF标记），结合单分子RNA荧光原位杂交（smFISH）检测凝聚体内部和外部TF的靶基因转录活性
   - **验证方式**: 若凝聚体内部TF的转录活性显著更高，则支持confinement-转录功能模型
   - **创新状态**: unverified