## 01 基本信息
- **标题**: The Advantages of AI for Computational Protein Studies and Looking Ahead at the Next Challenges: Single Structures Are Not Enough
- **作者与单位**: Bk, Pradeep; Chen, Shi-Jie; Dima, Ruxandra; Hassan, Mubasher; Joachimiak, Andrzej; Kihara, Daisuke; Kloczkowski, Andrzej; Law, Jeffrey; Liwo, Adam; Meller, Jarek; Micheletti, Cristan; Minor, Wladek; Montelione, Gaetano T; Rackovsky, Shalom; Scaramozzino, Domenico; Senda, Miki; Senda, Toshiya; Skolnick, Jeffrey; Stan, George; Vakser, Ilya A; Wang, Jin; Zou, Xiaoqin; Jernigan, Robert L（单位未提供）
- **期刊/预印本平台**: Journal of Molecular Biology
- **年份**: 2026
- **论文类型**: Perspective（观点/展望文章）
- **领域**: 计算蛋白科学、AI/深度学习、结构预测、构象系综、蛋白互作
- **关键词**: 未提供
- **DOI/arXiv 号**: 10.1016/j.jmb.2026.169949
- **代码**: 未提供
- **数据**: 未提供
- **阅读日期**: 2026-07-17
- **该文在课题方向中的位置**: 本文为领域内多位专家联合撰写的展望文章，系统梳理了AI在蛋白结构预测后的下一个挑战——从单一静态结构走向构象系综、多聚体组装、无序蛋白建模等。对IDP/IDR × 蛋白互作 × AI方法方向而言，本文提供了：(1) 无序蛋白建模作为核心挑战之一的明确论述；(2) AI生成替代构象的案例（Arf6）；(3) 训练数据质量问题（含水分子、PDB误差）对AI模型的影响分析；(4) DL与CG模拟融合的路线图建议。

## 02 一句话总结
本文通过多个案例（Arf6替代构象生成、水分子预测、配体结合位点预测、无序蛋白建模、构象系综生成）论证：AI在蛋白研究中的下一个核心挑战是从单一静态结构预测转向多构象系综、动态行为和多聚体组装建模，并建议通过DL与CG模拟的协同集成来实现这一目标。

## 03 研究问题
- **具体问题**: 当前AI（特别是AlphaFold系列）在蛋白结构预测上取得了巨大成功，但单一静态结构不足以捕捉蛋白功能所需的构象多样性、动态行为、配体结合诱导的构象变化以及无序蛋白的系综行为。如何突破这一局限？
- **为什么重要**: 蛋白功能（如信号转导、酶催化、蛋白-蛋白互作、相分离）本质上依赖构象变化和多状态行为。无序蛋白/无序区（IDP/IDR）尤其如此——它们天然以系综形式存在，无法用单一结构描述。药物设计、突变效应理解、功能机制解析都需要多构象信息。
- **现有方法为何不足**: AlphaFold2/3预测单一静态结构，对IDP/IDR区域给出低pLDDT分数但无法生成代表性系综；对多聚体复合物的预测成功率有限；对配体诱导的构象变化、别构效应、过渡态等动态过程缺乏建模能力。
- **精确的"Can ... ?"问题**: Can AI methods move beyond single static structure prediction to reliably generate representative conformational ensembles, including those of disordered proteins and multi-state protein complexes, that capture functionally relevant dynamics?

## 04 背景与发展脉络
*注：以下脉络基于本文框架，未经外部系统核验。*

1. **第一阶段：序列→结构预测的突破**（2018-2021）
   - 代表方法：AlphaFold1/2、ESMFold
   - 优点：高精度单链结构预测
   - 局限：单一静态结构，无法捕捉构象多样性

2. **第二阶段：蛋白语言模型（pLM/LPLM）的兴起**（2021-至今）
   - 代表方法：ESM系列、ProtTrans等
   - 优点：从序列直接学习进化信息、可迁移到多种下游任务（同源检测、功能预测）
   - 局限：embedding直接使用易产生假阳性，需要微调或特征选择

3. **第三阶段：多构象与动态建模的探索**（2023-至今）
   - 代表方法：AlphaFold-alt、AF-cluster、SPEECH_AF、AF-sample、AF-sample2、AF-RAVE、BioEmu
   - 优点：通过MSA操作、网络dropout、迭代重训等方式生成替代构象
   - 局限：对训练数据中过表达的构象态有偏置（如BioEmu偏向closed-holo态）；对大型复合物支持有限

4. **第四阶段（展望）：DL+CG协同集成**
   - 本文主张：DL生成构象 + CG物理模拟提供时间序列和物理真实性 + 实验数据约束
   - 优势互补：DL加速采样，CG提供可解释性和物理规律，实验数据锚定真实状态

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 单一结构不足以描述蛋白功能 | AlphaFold预测单一静态结构，无法捕捉构象变化、多状态行为 | 蛋白功能依赖构象多样性，单一结构信息不完整 | 摘要："Single Structures Are Not Enough"；"useful representations of proteins usually require 'dynamic' ensembles with multiple states" |
| 训练数据本身有误差 | PDB中实验结构模型存在解释偏差和错误 | 实验数据是人为解释的结果，非绝对真实 | "The experiment-based structure models in the PDB are interpretations of experimental data and are not themselves free of interpretation bias and errors" |
| 水分子缺失/错误 | 约800个高分辨率（≤2.5Å）晶体结构不含任何水分子；部分水分子占据率异常 | 实验限制和建模简化 | "around 800 such structures determined to 2.5 Å resolution or better without any water molecule" |
| AI对训练数据中过表达的构象态有偏置 | BioEmu在RBP和SERCA上偏向closed-holo态，且产生无实验支持的partial unfolding | 模型可能是在"记忆"训练数据而非学习物理原理 | "the resulting ensembles displayed a strong bias toward the closed-holo states, which are over-represented in the PDB"; "might result from AI memorization, rather than its inherent 'learning' of protein physical structure principles" |
| 无序蛋白建模困难 | AlphaFold不适合IDP/IDR，无法生成代表性系综 | IDP/IDR天然以动态系综存在，单一结构预测范式不适用 | "AlphaFold is not suitable for intrinsically disordered proteins (IDPs) or proteins with intrinsically disordered regions (IDRs) that exist as dynamic ensembles of conformations" |
| 多聚体复合物预测成功率低 | AlphaFold-multimer标准应用效果有限 | 复合物构象空间更大，MSA信息有限 | "the standard application of AlphaFold-multimer for modeling protein-protein co-structures has had limited success" |
| DL生成构象缺乏时间序列和物理真实性 | 当前DL方法生成构象但无法排序、无法给出时间顺序 | DL缺乏物理规律约束 | "current DL attempts tend to bridge the gap in conformational space by performing extensive MD sampling from end-state conformers and reconstructing the sequence of transition steps ex post facto" |

## 06 核心思想

### 1) 表面方法
本文是一篇Perspective文章，通过多个案例和领域综述，论证AI蛋白研究的下一步方向：从单一结构走向构象系综、动态建模、多聚体组装，并提出了DL与CG模拟融合的路线图。

### 2) 核心洞察
- **单一结构范式已到极限**：AlphaFold等工具在静态结构预测上已接近饱和，但蛋白功能本质上是动态的、多状态的。下一个突破点在于构象系综的生成与验证。
- **训练数据质量是隐藏瓶颈**：PDB中的误差（特别是水分子缺失）和构象态偏置（如closed-holo过表达）会直接影响AI模型的输出质量，需要系统性清洗和重训练。
- **DL与CG的互补性**：DL擅长从数据中学习模式、快速生成候选构象；CG模拟提供物理真实性、时间序列和可解释性。两者结合可以互相弥补短板。
- **无序蛋白是AI建模的"试金石"**：IDP/IDR天然以系综形式存在，无法用单一结构描述，是检验多构象建模方法的最佳测试平台。

### 3) 可能的普适教训 [Analysis]
- **"预测"不等于"理解"**：AI模型即使预测准确，也可能是在记忆训练数据而非学习物理原理（如BioEmu案例）。验证模型是否真正"理解"蛋白物理，需要看其在未见过的构象态上的表现。
- **数据质量决定模型上限**：在AI时代，训练数据的系统性误差（如PDB中水分子缺失）会被模型放大。清洗和增强训练数据可能比改进模型架构带来更大的收益。
- **多尺度融合是复杂生物系统建模的必然路径**：单一方法（纯DL或纯物理模拟）都有局限，跨尺度、跨范式的集成是处理蛋白复合物、无序蛋白等复杂系统的可行策略。

## 07 方法总览
本文为Perspective文章，无具体方法实现。但文中提出了以下方法学框架：

- **输入**：蛋白序列、PDB实验结构、MSA、实验约束数据（NMR、cryo-EM）、LPLM embeddings
- **输出**：构象系综、替代构象、多聚体组装模型、配体结合位点预测、水分子位置预测
- **核心模块**：
  1. LPLM embeddings用于同源检测和功能预测
  2. AlphaFold变体（AF-sample、AF-cluster、SPEECH_AF等）用于生成替代构象
  3. DL生成构象 + CG模拟（ENM、MD）验证和扩展
  4. 实验数据（NMR、cryo-EM）约束和验证
- **反馈回路**：DL生成构象 → CG模拟验证/扩展 → 实验数据锚定 → 重新训练/优化DL模型
- **假设**：DL与CG的集成可以克服各自局限；实验数据可以提供锚定真实状态的约束

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| LPLM embeddings | 数值化表示蛋白序列，用于同源检测、功能预测 | 直接从序列学习进化信息，无需结构 | 输入：序列；输出：embedding向量 | "The embeddings provide numerical representations of any given sequence. The differences between embedding values can be used to identify the most homologous pairs" | 预期影响：失去序列-功能映射的快速通道；但直接使用会产生假阳性，需微调 |
| AlphaFold变体（AF-sample、AF-cluster等） | 生成替代构象 | 标准AlphaFold只给单一结构，无法捕捉多状态 | 输入：序列+MSA（操作后）；输出：多个候选构象 | "stochastic sampling methods and customized MSAs"在CASP中表现提升 | 预期影响：失去多构象生成能力，回到单一结构范式 |
| 水分子预测模块（GALAXYWater-CNN、HydraProt、SuperWater） | 预测蛋白周围水分子位置 | 水分子对结构稳定性和功能至关重要，但PDB中大量缺失 | 输入：蛋白结构；输出：水分子位置/概率图 | "GALAXYWater-CNN uses a 3D CNN...HydraProt employs a 3D U-net...SuperWater integrates score-based diffusion model with equivariant GNNs" | 预期影响：无法处理水介导的相互作用和构象稳定性 |
| CG模拟（ENM等） | 生成大尺度构象变化的物理可行路径 | DL缺乏物理约束和时间序列 | 输入：起始构象（可来自DL）；输出：构象轨迹/过渡路径 | "ENM path-sampling methods...achieve scalability to larger protein sizes, enabling the generation of transition pathways for large proteins and protein complexes up to the megadalton scale" | 预期影响：失去物理真实性和时间序列信息 |
| DL+CG集成框架 | 结合DL的快速采样和CG的物理真实性 | 两者互补：DL加速、CG提供物理约束 | 输入：DL生成构象+CG模拟；输出：验证后的构象系综 | "a synergistic integration of data-driven DL approaches for ensemble generation with physics-based and data-assisted CG simulations could overcome many of the current limitations" | 预期影响：回到单一方法的局限（DL无物理、CG采样不足） |

*注：以上"预期影响"均为[Analysis]推断，文中未提供消融实验。*

## 09 关键公式符号
本文为Perspective文章，未提供具体公式。文中涉及的定量信息包括：
- 水分子预测精度：SuperWater达到0.3 ± 0.06 Å（相对于实验验证位置）
- 同源检测：使用LPLM embeddings，可在低至10%序列同一性下发现新同源物

## 10 实验设计与证据链
本文为Perspective文章，无系统实验设计。文中案例包括：

| 实验/案例 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|-----------|------------|------------|------|------------|-------------------|------|
| Arf6替代构象生成 | ESMFold可预测未提供的替代构象 | 两个实验结构：PDB 1E0S（未结合）和2J5X（GTPγS结合）；ESMFold仅输入序列 | ESMFold生成结构与两个实验结构均一致，且覆盖从未结合到结合的构象连续体 | AI可从序列直接生成构象系综，无需提供替代构象信息 | 仅单一蛋白案例，不能推广到所有蛋白 | Figure 1 |
| BioEmu测试（RBP和SERCA） | AI生成构象系综的可靠性 | 与PDB中已知构象比较 | 偏向closed-holo态（PDB中过表达），产生无实验支持的partial unfolding | 模型可能在记忆训练数据而非学习物理原理 | 仅两个蛋白案例，不能推广 | "Scaramozzino et al. recently tested BioEmu on ribose-binding protein (RBP) and the sarcoplasmic/endoplasmic reticulum Ca2+ ATPase1 (SERCA)" |
| 水分子预测方法比较 | DL方法优于能量方法 | GALAXYWater-CNN vs 之前能量方法；HydraProt vs SOTA；SuperWater vs SOTA | 各方法均声称超越之前方法 | DL方法在水分子预测上持续进步 | 各方法独立开发，无统一基准比较 | "showed higher performance when compared with previous energy-based methods"; "was shown to surpass than existing state-of-the-art approaches"; "accuracy of 0.3 ± 0.06 Å" |
| CASP16 RNA预测 | AlphaFold3在RNA上的表现 | 与物理方法比较 | 物理方法优于AlphaFold3 | RNA结构预测仍具挑战性 | 单次实验，样本有限 | "the AlphaFold3 server's predictions of 3D RNA structures were outperformed by physics-based models" |

## 11 结论正确解读
- **任务范围**: 本文是Perspective文章，非实验研究。结论为领域展望和建议，非已验证的实证结果。
- **Oracle/真值输入**: 文中案例使用PDB实验结构作为参考/真值，但未系统讨论实验误差。
- **端到端状态**: 文中提出的DL+CG集成框架为建议方向，尚未实现为完整工作流。
- **算力成本**: 未讨论。
- **历史数据依赖**: 明确指出AI模型受训练数据偏置影响（如BioEmu偏向closed-holo态），但未量化。
- **模型依赖**: 结论基于AlphaFold系列、ESMFold、BioEmu等特定模型的表现，可能不适用于其他架构。
- **最难情形**: 文中指出IDP/IDR、大型多聚体复合物、RNA-蛋白复合物是当前最具挑战性的目标。
- **群体/领域边界**: 结论主要针对计算蛋白科学领域，对实验生物学的适用性未讨论。
- **不确定性**: 文中多处使用"likely"、"potential"等词，表明结论为推测性展望。

**有边界的复述**: 基于当前AI结构预测工具的已知局限（单一结构、训练数据偏置）和若干案例（Arf6、BioEmu、水分子预测），本文建议：AI蛋白研究的下一阶段应聚焦于构象系综生成、多聚体组装建模和IDP/IDR表征，并通过DL与CG模拟的集成来实现。这些建议基于领域专家的共识性判断，但尚未经过大规模实证验证。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 训练数据误差 | PDB中实验结构模型存在解释偏差和错误；约800个高分辨率结构无水分子 | 使用验证报告和密度图排除低质量结构；用PDB-REDO等工具优化；考虑用过滤后的数据库重训练AI | "These validation reports and the data needed to visualize the density maps can enable independent structure evaluation that could be used to exclude models" |
| 水分子建模不足 | 许多结构缺少水分子或水分子位置错误 | 开发更先进的DL水分子预测方法；需要更多高分辨率晶体结构 | "This problem will be solved with more high resolution crystal structures solved with the higher energy beam lines coming online now" |
| AI对训练数据构象偏置 | BioEmu偏向closed-holo态，产生无实验支持的partial unfolding | 需要开发去偏置方法；结合物理模拟验证 | "Bias from specific conformational states present in the training data can prevent sampling of alternative conformational states" |
| DL方法规模限制 | 多数DL构象采样方法限于单体蛋白或小复合物 | 开发可处理大型多聚体复合物的方法 | "most available DL methods are still limited to monomeric proteins, or small complexes" |
| DL构象缺乏时间序列 | 生成的构象无法排序、无时间顺序 | 结合CG模拟提供时间序列 | "current DL attempts tend to bridge the gap in conformational space by performing extensive MD sampling from end-state conformers and reconstructing the sequence of transition steps ex post facto" |
| RNA结构预测仍具挑战 | AlphaFold3在RNA上被物理方法超越 | 需要更多RNA实验数据和专门方法 | "predicting RNA structure with AI remains more challenging than predicting protein structure" |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| Arf6案例仅展示单一蛋白 | ESMFold的成功可能依赖Arf6的特殊性（小G蛋白、构象变化有限） | 若仅少数蛋白适用，则"AI生成构象系综"的普适性存疑 | 在多种蛋白类型（激酶、通道、IDP等）上系统测试ESMFold的构象生成能力 | Figure 1 |
| BioEmu的失败被归因于"记忆"而非"学习" | 也可能是模型架构或训练目标不适合构象采样，而非记忆问题 | 归因错误会导致错误的方法改进方向 | 设计实验区分记忆与学习：在训练集中删除目标构象态后重新测试 | "might result from AI memorization" |
| DL+CG集成建议缺乏具体实现方案 | 集成方式（串行、并行、迭代？）、接口设计、计算成本分配均未讨论 | 从建议到可执行方案之间存在巨大鸿沟 | 在1-2个具体系统上实现原型并比较与纯DL/纯CG的优劣 | "We suggest that a synergistic integration..." |
| 水分子问题被简化为"需要更多高分辨率数据" | 即使有高分辨率数据，DL方法对水分子的物理建模（氢键网络、动态交换）仍不成熟 | 数据量增加不等于建模能力提升 | 在现有高分辨率数据集上测试当前DL水分子预测方法的上限 | "This problem will be solved with more high resolution crystal structures" |
| 对IDP/IDR的讨论停留在"AlphaFold不适合"层面 | 未讨论IDP/IDR系综生成的具体方法学挑战（如如何验证系综准确性、如何与实验SAXS/NMR数据整合） | IDP/IDR是本文课题的核心对象，但本文未提供可操作的建模路线 | 系统综述现有IDP系综生成方法（如MES、AF-MD集成）的进展与瓶颈 | "AlphaFold is not suitable for intrinsically disordered proteins" |
| 未讨论AI方法的计算成本与可及性 | AlphaFold3等工具对算力要求高，可能限制其在资源有限实验室的应用 | 方法建议需考虑实际可部署性 | 分析各方法在标准GPU上的运行时间和内存需求 | 全文未提及计算成本 |

## 14 学到什么
*Agent 提炼的知识候选*

1. **概念：单一结构范式的局限**。AlphaFold等工具预测的单一静态结构不足以描述蛋白功能，尤其对IDP/IDR和构象变化驱动的互作。可迁移到本课题：研究IDP/IDR介导的互作时，应明确采用"系综思维"而非"单结构思维"。

2. **方法：AI生成替代构象的多种策略**。包括：(1) 状态注释的构象模板；(2) 浅MSA（随机选择或聚类选择）；(3) 极浅MSA甚至单序列；(4) 多位点MSA掩码（SPEECH_AF、AF-sample2）；(5) 网络dropout（AF-sample）。可迁移到本课题：这些策略可用于生成IDP/IDR的构象系综，作为MD模拟的起始点或约束。

3. **方法：LPLM embeddings的正确使用方式**。直接使用原始embedding会产生大量假阳性；需要通过微调或特征选择来优化。可迁移到本课题：用LPLM embeddings预测IDP/IDR互作位点时，必须设计验证集和微调流程。

4. **方法：DL+CG集成框架**。DL生成候选构象 + CG模拟（ENM/MD）提供物理验证和时间序列 + 实验数据锚定。可迁移到本课题：对IDP/IDR介导的相分离，可用DL生成多种构象，用CG模拟评估其相分离倾向，用实验（如SAXS、NMR）验证。

5. **概念：训练数据质量对AI模型的深远影响**。PDB中水分子缺失和构象态偏置会直接影响AI输出。可迁移到本课题：构建IDP/IDR相关训练集时，需特别注意实验数据的质量和构象覆盖度。

6. **方法：实验数据与AI建模的整合**。AF-NMR框架用NMR NOESY数据评分AlphaFold生成的构象，可发现动态平衡中的多构象态。可迁移到本课题：对IDP/IDR互作，可用NMR或SAXS数据约束和验证AI生成的构象系综。

7. **概念：AI"记忆"与"学习"的区分**。模型在训练数据过表达的构象态上表现好，不意味着学到了物理原理。可迁移到本课题：评估AI模型对IDP/IDR的建模能力时，需在训练集覆盖不足的构象态上测试。

8. **方法：基于LPLM embeddings的同源检测**。通过embedding距离发现低序列同一性（~10%）的同源物。可迁移到本课题：可用于发现IDP/IDR的功能同源物，即使序列差异大但功能相似。

## 15 与已有知识连接
- **AlphaFold系列**：本文多处引用AlphaFold1/2/3的进展与局限，与已知文献一致（Jumper et al., Nature 2021; Abramson et al., Nature 2024）。本文指出AlphaFold3仍无法预测功能性构象（如ATP水解循环中的不同状态），与已知评估一致。
- **蛋白语言模型**：ESM系列（Lin et al., Science 2023）等LPLM的embedding用于同源检测，本文提供了具体案例（10%序列同一性发现新同源物）。
- **构象系综生成方法**：AF-cluster（Wayment-Steele et al., bioRxiv 2023）、AF-sample（Wallner et al.）、SPEECH_AF（Stein & Mchaourab, 2024）等，均为已知方法，本文将其归入"AI生成替代构象"的策略谱系。
- **无序蛋白建模**：本文明确指出AlphaFold不适合IDP/IDR，与已知文献一致（Ruff & Pappu, JMB 2021; 等）。本文建议用系综生成方法应对，与IDP领域的主流观点一致。
- **水分子预测**：GALAXYWater-CNN（Ko et al., NAR 2022）、HydraProt、SuperWater等为已知方法，本文将其作为AI在蛋白研究中应用的一个方向。
- **DL+CG集成**：AF-RAVE（Wang et al., 2024）、BioEmu（Lewis et al., 2024）等为已知的DL+MD集成方法，本文将其作为未来方向。
- **RNA结构预测**：本文引用CASP16结果（AlphaFold3被物理方法超越），与已知评估一致（Das et al., Science 2024 等）。

## 16 研究想法
*Agent 生成的研究候选*

1. **名称**：IDP/IDR构象系综生成的DL+CG集成框架
   - **来源局限/观察**：本文指出AlphaFold不适合IDP/IDR，且DL+CG集成是未来方向，但未给出具体实现。
   - **核心假设**：用AF-sample/AF-cluster生成IDP/IDR的多样构象，再用CG/MD模拟（如ABSINTH、MPI）筛选物理可行的系综，可得到比单一方法更准确的IDP/IDR构象系综。
   - **初步方法**：以已知IDP/IDR（如p53 N端、α-synuclein）为测试集，比较纯DL、纯MD、DL+CG集成三种策略生成的系综与实验（SAXS、NMR Rg、J-coupling）的吻合度。
   - **验证方式**：计算系综平均Rg、残基接触概率与实验数据对比；用留一法验证泛化性。
   - **创新状态**：unverified

2. **名称**：基于LPLM embeddings的IDP/IDR互作位点预测
   - **来源局限/观察**：本文指出LPLM embeddings可用于同源检测，但直接使用有假阳性；IDP/IDR的互作位点预测是未解决问题。
   - **核心假设**：对LPLM embeddings进行微调（fine-tuning）后，可准确预测IDP/IDR中的短线性基序（SLiMs）和分子识别特征（MoRFs）。
   - **初步方法**：用ELM数据库中的SLiM标注训练集，对ESM-2 embeddings进行微调；与现有方法（如IUPred、Anchor）比较。
   - **验证方式**：独立测试集上的AUC、精确率-召回率；在已知相分离蛋白（如FUS、TDP-43）上验证预测位点是否富集于互作界面。
   - **创新状态**：unverified

3. **名称**：训练数据构象偏置对IDP/IDR建模影响的系统评估
   - **来源局限/观察**：本文指出BioEmu偏向closed-holo态，提示AI模型对训练数据中过表达构象的偏置问题。IDP/IDR在PDB中天然欠表达，偏置问题可能更严重。
   - **核心假设**：在IDP/IDR建模中，训练数据的构象偏置会导致系统性的系综失真，且这种失真无法通过增加数据量解决。
   - **初步方法**：构建一个IDP/IDR测试集，其构象覆盖度已知；用不同构象覆盖度的训练集训练同一模型，比较输出系综的偏差。
   - **验证方式**：计算输出系综与实验数据的KL散度；分析偏置与训练集构象覆盖度的相关性。
   - **创新状态**：unverified

4. **名称**：水分子介导的IDP/IDR互作界面预测
   - **来源局限/观察**：本文强调水分子在蛋白结构中的重要性，但IDP/IDR互作中水分子的角色尚未被系统研究。
   - **核心假设**：IDP/IDR互作界面上的水分子位置可通过DL方法（如SuperWater）预测，且这些水分子对互作自由能贡献显著。
   - **初步方法**：用SuperWater预测IDP/IDR复合物界面水分子；用MD模拟验证这些水分子的驻留时间和自由能贡献。
   - **验证方式**：预测水分子位置与MD模拟水密度图对比；突变界面水分子相关残基后测量结合亲和力变化。
   - **创新状态**：unverified

5. **名称**：IDP/IDR介导相分离的构象系综-相图关联模型
   - **来源局限/观察**：本文指出IDP/IDR的系综建模是核心挑战，而相分离行为与IDP/IDR的构象系综直接相关。
   - **核心假设**：IDP/IDR的构象系综特征（如链内接触概率、Rg分布）可预测其相分离倾向和相图位置。
   - **初步方法**：用DL+CG集成生成多个IDP/IDR的构象系综，计算系综特征；用实验相图数据（饱和浓度、临界温度）建立关联模型。
   - **验证方式**：在已知相分离蛋白（FUS、hnRNPA1、DDX4）上验证预测准确性；在未知蛋白上做前瞻性预测。
   - **创新状态**：unverified

6. **名称**：AF-NMR框架在IDP/IDR互作研究中的扩展
   - **来源局限/观察**：本文介绍AF-NMR用NMR数据评分AlphaFold构象，但仅应用于有序蛋白。IDP/IDR的NMR数据（化学位移、NOE、PRE）包含丰富的系综信息。
   - **核心假设**：将AF-NMR框架扩展到IDP/IDR，用NMR化学位移和PRE数据评分DL生成的构象系综，可显著提高系综准确性。
   - **初步方法**：以α-synuclein为测试系统，用AF-sample生成构象池，用SPARTA+或ShiftX2预测化学位移，与实验化学位移对比评分。
   - **验证方式**：评分最高的系综与实验Rg、残基接触概率对比；与现有IDP系综方法（如ENSEMBLE、MES）比较。
   - **创新状态**：unverified