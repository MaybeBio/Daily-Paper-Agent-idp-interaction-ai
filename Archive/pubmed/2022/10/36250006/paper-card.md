## 01 基本信息

- **标题**：Prediction of protein-protein interaction sites in intrinsically disordered proteins
- **作者**：Chen, Ranran; Li, Xinlu; Yang, Yaqing; Song, Xixi; Wang, Cheng; Qiao, Dongqing
- **单位**：山东大学（Shandong University）等（基于基金信息推断，具体单位列表未提供）
- **期刊/平台**：Frontiers in Molecular Biosciences
- **年份**：2022-10-18
- **论文类型**：综述（Review）
- **领域**：无序蛋白（IDP/IDR）蛋白-蛋白互作位点预测；计算预测方法综述
- **关键词**：intrinsically disordered proteins (IDPs)；protein-protein interaction sites (PPIS)；prediction；machine learning；scoring functions；consensus approaches
- **DOI/arXiv**：10.3389/fmolb.2022.985022
- **代码**：未提供
- **数据**：未提供（综述性论文，无新数据集）
- **阅读日期**：2026-04-27
- **在该课题方向中的位置**：本文是 IDP/IDR 蛋白互作位点（IDP-PPIS）预测方法的系统性综述，覆盖 2007–2022 年 30 个预测器，按算法类型（scoring function、machine learning、consensus）分类，系统梳理了数据库、特征和算法三个关键环节。对于本课题（IDP/IDR × 蛋白互作 × AI 方法），本文提供了该子领域的全景式地图、特征工程思路、基准数据集来源和性能对比基线，是进入该方向的重要参考综述。

## 02 一句话总结

本文收集并分类了 2007–2022 年间发表的 30 个 IDP 蛋白-蛋白互作位点（IDP-PPIS）预测器，从数据库、特征和算法三个维度系统梳理了该领域的方法学进展，指出当前方法在数据偏差、特征单一（缺乏盐桥、结构特征）等方面的不足，并展望了基于 AlphaFold2 等结构预测技术的新方向。

## 03 研究问题

- **具体问题**：IDP/IDR 中蛋白-蛋白互作位点（IDP-PPIS）的计算预测方法有哪些？它们如何构建？性能如何？存在哪些不足？
- **为什么重要**：IDP 缺乏稳定三级结构但广泛参与转录调控、细胞周期等关键生物过程，其功能主要通过蛋白互作实现。实验方法（如 NMR）昂贵耗时，计算预测是功能注释的重要补充。随着无序蛋白数据快速增长，系统梳理预测方法对方法选择和开发至关重要。
- **现有方法为何不足**：已有综述（如 Katuwawala et al., 2019a, 2019b）缺乏对影响预测器性能因素的系统描述；且该领域更新迅速（每 3 年新增 6–10 个预测器），需要及时更新。
- **精确研究问题**：Can a systematic review of 30 IDP-PPIS predictors, organized by databases, features, and algorithms, provide a comprehensive picture of the field's status quo and identify future development directions?

## 04 背景与发展脉络

> 注：以下脉络基于本文框架，标注为「仅本文框架」。

- **第一阶段（~2007–2012）：早期方法——scoring function 与简单 ML**
  - 代表方法：alpha-MoRFpred (Cheng et al., 2007) 首次用 feedforward neural network 预测 α-MoRF；ANCHOR (Dosztanyi et al., 2009) 基于能量估计的 benchmark 方法。
  - 优点：开创性，建立了基本预测框架。
  - 局限：特征较简单，性能有限（AUC 约 0.6–0.7）。

- **第二阶段（~2012–2018）：机器学习方法繁荣**
  - 代表方法：MoRFpred (SVM)、fMoRFpred、MFSPMpred、PSSMpred、MoRFCHiBi 系列、Predict-MoRFs、SPINE-D 等。
  - 优点：引入更丰富的特征（进化信息 PSSM/HMM、预测结构特征、理化性质），性能提升（AUC 可达 0.75–0.82）。
  - 局限：多数方法聚焦短 MoRF/SLiM 区域，对长无序结合区覆盖不足；特征工程依赖人工。

- **第三阶段（~2018–2022）：深度学习和 consensus 方法**
  - 代表方法：SPOT-Disorder/SPOT-Disorder2 (LSTM)、DeepDISOBind (multi-task deep neural network)、flDPnn (deep feedforward + random forest)、DEPICTER、HybridPBRpred。
  - 优点：深度学习自动特征提取，multi-task 学习同时预测 DNA/RNA/蛋白结合；consensus 方法整合多个预测器提升鲁棒性（AUC 可达 0.87–0.90）。
  - 局限：数据偏差问题（如 MoRF 数据集含大量免疫相关蛋白）；高维特征空间导致计算效率下降。

- **本文主张的位置**：作为截至 2022 年 1 月的系统性综述，本文填补了已有综述在「影响预测器性能因素」方面的空白，并首次系统讨论盐桥特征缺失、AlphaFold2 结构特征等未来方向。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 数据偏差 | 现有 MoRF 数据集含大量免疫相关蛋白，训练出的预测器可能偏向免疫相关位点 | 数据集主要来自 DisProt 和 PDB，尤其是 Disfani 等人的数据集 | Discussion 节："Since this dataset contains a large number of immune-related proteins, the trained predictors might suffer from bias problems" |
| 特征覆盖不全 | 所有预测器均未考虑盐桥（salt bridge）特征 | 盐桥在 IDP 互作中贡献局部刚性结构并触发 disorder-to-order 转变，但尚未被纳入特征工程 | Discussion 节："Salt bridges involved in disordered proteins have not yet been considered as a feature in all the predictors summarized" |
| 短区域偏重 | 多数方法聚焦 MoRF/SLiM 等短结合区域，对长无序结合区覆盖不足 | 现有基准数据集和特征设计主要针对短 motif | Discussion 节："The existing predictors mainly focus on short binding regions such as MoRF and SLiMs, but there are still non-MoRF and non-SLiMs binding regions" |
| 高维特征与效率 | 整合多种特征导致高维特征空间，增加算法复杂度、降低计算效率 | 多特征融合策略缺乏特征选择/降维 | Discussion 节："this approach easily causes high-dimensional feature space and the algorithm complexity and also reduce the computing efficiency" |
| 结构信息利用不足 | 多数方法仅基于序列信息，未充分利用结构预测信息 | 结构预测技术（如 AlphaFold2）刚兴起，尚未被整合进 IDP-PPIS 预测 | Discussion 节："disorder predictors constructed based on AlphaFold2 structures were found to have potentials to identify disordered regions" |

## 06 核心思想

### 1) 表面方法

对 30 个 IDP-PPIS 预测器进行系统性综述，按算法类型分为三类：
- **Scoring function based**：如 ANCHOR/ANCHOR2，基于能量估计（intra-chain interaction energy 与 hypothetical globular protein 结合能量）计算残基级得分。
- **Machine learning based**：SVM（MoRFpred、MFSPMpred、PSSMpred、MoRFCHiBi）、神经网络（alpha-MoRFpred、SPINE-D、SPOT-Disorder/2、DeepDISOBind）、random forest（flDPnn）、logistic regression（DisoRDPbind）等。
- **Consensus approaches**：如 DEPICTER、HybridPBRpred，整合多个预测器的输出作为新特征，用 meta-learner 生成最终预测。

### 2) 核心洞察

- **特征工程是 IDP-PPIS 预测的核心驱动力**：从氨基酸组成、理化性质到进化信息（PSSM/HMM）、预测结构特征（二级结构、溶剂可及性、disorder score），特征的丰富程度直接决定预测性能上限。
- **三类算法各有优劣**：scoring function 可解释性强但性能有限；ML 方法性能高但依赖训练数据质量；consensus 方法通过整合互补信息提升鲁棒性，但增加计算开销。
- **数据质量与覆盖度是瓶颈**：现有基准数据集来源单一（DisProt/PDB），存在免疫相关蛋白偏差，且对非 MoRF/SLiM 的长无序结合区覆盖不足。
- **结构信息是未来突破口**：AlphaFold2 等结构预测技术可提供 IDP 结合构象的线索，有望弥补纯序列方法的不足。

### 3) 可能的普适教训 [Analysis]

- **对 IDP/IDR × 蛋白互作 × AI 方法课题的启示**：特征设计应超越传统序列特征，纳入互作特异性信息（如盐桥、疏水补丁、线性 motif 保守性）；数据构建应关注偏差控制（如免疫蛋白富集问题），并考虑多源数据融合（DisProt + PDB + ELM + DIBS + MFIB）。
- **方法选择应匹配预测目标**：短 motif（MoRF/SLiM）与长无序结合区可能需要不同的特征和模型架构；multi-task 学习（同时预测 DNA/RNA/蛋白结合）是提高泛化能力的有效策略。
- **结构预测与序列预测的融合是趋势**：AlphaFold2 的 pLDDT 等置信度指标可作为 IDP 结合位点预测的新特征，值得在本课题中探索。

## 07 方法总览

本文为综述，无新方法。但综述梳理的预测器构建流程可概括为：

- **输入**：蛋白质序列（或序列 + 已知结构信息）
- **特征提取**：
  - 氨基酸组成（AAC）
  - 理化性质（疏水性、极性、电荷等，来自 AAindex）
  - 进化信息（PSSM、HMM profile）
  - 预测结构特征（二级结构、溶剂可及性、接触数、B-factor）
  - Disorder score（IUPred、ESpritz 等）
- **模型训练**：
  - Scoring function：能量估计（ANCHOR）
  - ML：SVM、logistic regression、random forest、feedforward/RNN/LSTM 神经网络、multi-task deep learning
  - Consensus：整合多个预测器输出，用 meta-learner（如 extreme gradient boosting）生成最终预测
- **输出**：每个残基的 binding propensity score 或 binary classification（是否结合位点）
- **评测**：AUC、MCC、sensitivity、specificity 等

**文字流程**：序列输入 → 特征提取（多源特征融合）→ 模型训练/预测 → 残基级得分 → 阈值判定结合位点 → 性能评估。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 数据库/基准数据集（DisProt, PDB, ELM, DIBS, MFIB） | 提供训练和测试数据 | IDP-PPIS 预测需要标注了结合位点的无序蛋白数据 | 输入：蛋白序列 + 实验标注；输出：训练/测试集 | Section 2.1 详细列出各数据库 | 数据质量差或偏差大会导致预测器泛化能力下降（作者指出免疫蛋白偏差问题） |
| 特征提取模块 | 将序列转换为数值特征 | ML 模型需要数值输入 | 输入：序列；输出：特征向量 | Section 2.2 详述六类特征 | 特征不足会限制预测性能上限；高维特征会降低计算效率 |
| 预测算法模块（scoring function / ML / consensus） | 从特征学习结合位点模式 | 核心预测能力 | 输入：特征向量；输出：残基级得分/分类 | Section 2.3 分类详述 30 个预测器 | 算法选择决定性能上限和可解释性 |
| 性能评估模块 | 量化预测精度 | 方法比较和选择 | 输入：预测结果 + 真实标注；输出：AUC/MCC 等 | 各预测器原文报告的性能指标 | 缺乏统一评测基准会导致方法间不可比 |

**消融效应说明**：本文为综述，未做消融实验。上述「移除后影响」为基于作者讨论的预期效应，非实测。

## 09 关键公式符号

本文为综述，核心公式来自 ANCHOR 系列：

**ANCHOR 评分函数**（Section 2.3.1.2）：
$$I_k = p_1 S_k + p_2 E_{int,k} + p_3 E_{gain,k}$$

- $I_k$：残基 k 的最终预测得分
- $S_k$：残基 k 邻域窗口内 IUPred 平均 disorder score（对应标准 1）
- $E_{int,k}$：残基 k 通过形成链内接触的可能相互作用能
- $E_{gain,k}$：残基 k 通过与假想球状蛋白互作可能获得的能量
- $p_1, p_2, p_3$：权重参数

**ANCHOR2 改进评分**（Section 2.3.1.2）：
$$S_k = (E_{gain,k}(w_1) - E_{gain,0})(I_k(w_2) - I_0)$$

- $S_k$：残基 k 的得分
- $E_{gain,k}(w_1) = E_{loc,k}(w_1) - E_{int,k}$：仅通过与有序蛋白结合计算的能量
- $I_k(w_2)$：残基 k 在 $w_2$ 半窗口连续邻域内的平均 IUPred 得分
- $E_{gain,0}$ 和 $I_0$：使残基成为 IDP-PPIS 的最小能量增益和最小平均 disorder 倾向参数

**氨基酸组成**（Section 2.2.1）：
$$composition(i) = \frac{n_i}{N}$$

- $i$：特定氨基酸
- $n_i$：该氨基酸在序列中的数量
- $N$：序列总氨基酸数

## 10 实验设计与证据链

本文为综述，无原始实验。其「证据」来自对 30 个预测器原文的汇总比较。

- **数据集/群体**：30 个 IDP-PPIS 预测器（2007–2022 年 1 月发表）
- **指标**：AUC、MCC、sensitivity、specificity、accuracy 等（各预测器原文报告）
- **评测协议**：各预测器原文的独立评测协议，无统一基准

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|------------------|------|
| 预测器分类（scoring function / ML / consensus） | 三类方法构成该领域主要技术路线 | 按算法类型分类 30 个预测器 | 约 2/3 为 ML-based | 该领域以 ML 方法为主导 | 无法比较三类方法的相对优劣（无统一基准） | Section 2.3, Table 2 |
| 特征类型汇总 | 特征工程是预测性能的关键 | 汇总六类特征（AAC、理化、进化、结构、disorder、其他） | 多数预测器整合多种特征 | 多特征融合是主流策略 | 无法确定哪些特征贡献最大 | Section 2.2, Table 1 |
| 性能趋势分析 | 预测性能随时间提升 | 比较不同年份预测器的 AUC | AUC 从 ~0.6 提升至 ~0.9 | 该领域持续进步 | 性能提升可能部分来自数据集变化而非算法改进 | Section 3 |
| 数据偏差分析 | 现有数据集存在免疫蛋白偏差 | 分析 Disfani 等人数据集的组成 | 含大量免疫相关蛋白 | 预测器可能偏向免疫相关位点 | 偏差对性能的具体影响未量化 | Discussion 节 |
| 盐桥特征缺失分析 | 盐桥是潜在的重要特征 | 检查 30 个预测器的特征列表 | 均未包含盐桥特征 | 盐桥特征未被利用 | 加入盐桥特征能否提升性能未验证 | Discussion 节 |
| AlphaFold2 潜力讨论 | 结构预测可辅助 IDP-PPIS 预测 | 讨论 AlphaFold2 在无序蛋白中的应用 | pLDDT 可识别无序区域 | 结构信息有望提升预测性能 | 具体实现和效果未验证 | Discussion 节 |

## 11 结论正确解读

- **任务范围**：本文仅覆盖 IDP-PPIS 预测，即无序蛋白中参与蛋白-蛋白互作的残基/区域预测。不涉及 DNA/RNA 结合位点（虽提及 DeepDISOBind 的 multi-task 框架）、不涉及互作亲和力/动力学预测、不涉及相分离驱动序列预测。
- **oracle/真值输入**：综述中所有预测器的训练数据均来自实验验证的结合位点（如 DisProt、PDB 中的复合物结构），属于实验标注，非预测值。
- **端到端状态**：本文是综述，非端到端预测工具。其描述的预测器均为序列输入 → 残基级得分输出，但各预测器独立开发，无统一 pipeline。
- **算力成本**：未讨论。综述中部分方法（如 DeepDISOBind）需要 GPU 训练，但具体成本未报告。
- **历史数据依赖**：所有预测器依赖历史实验数据训练，对新发现的 IDP 类型（如新病毒蛋白）的泛化能力未验证。
- **模型依赖**：综述结论（如「ML 方法占主导」「盐桥特征缺失」）基于 30 个预测器的汇总，不依赖单一模型。
- **最难情形**：作者指出长无序结合区（非 MoRF/SLiM）的预测是难点；含免疫相关蛋白偏差的数据集训练的模型在非免疫蛋白上可能失效。
- **群体/领域边界**：结论仅适用于 IDP-PPIS 预测领域，不直接推广到有序蛋白的 PPI 位点预测或 IDP 的其他功能预测。
- **不确定性**：综述中报告的 AUC/MCC 来自各预测器独立评测，数据集不同，不可直接横向比较。

**有边界的复述**：截至 2022 年 1 月，IDP-PPIS 预测领域以 ML 方法为主流，特征工程（尤其是进化信息和预测结构特征）是性能关键，但现有方法存在数据偏差、盐桥特征缺失、长结合区覆盖不足等问题，基于 AlphaFold2 的结构信息整合是值得探索的方向。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据偏差 | 现有 MoRF 数据集含大量免疫相关蛋白，预测器可能偏向免疫相关位点 | 构建更全面的基准数据集，纳入更多来源（如 D2P2、MFIB） | Discussion 节 |
| 短区域偏重 | 现有方法主要聚焦 MoRF/SLiM 等短结合区域，非 MoRF/SLiM 的长无序结合区预测不足 | 开发针对长无序结合区的预测方法 | Discussion 节 |
| 盐桥特征缺失 | 所有 30 个预测器均未考虑盐桥特征 | 将盐桥特征纳入预测器 | Discussion 节 |
| 结构信息利用不足 | 多数方法仅基于序列信息 | 利用 AlphaFold2 等结构预测技术构建结构基预测器 | Discussion 节 |
| 高维特征效率问题 | 多特征融合导致高维特征空间和计算效率下降 | 特征选择/降维策略 | Discussion 节 |

**作者提及的相关约束**（非正式局限）：
- 综述仅覆盖截至 2022 年 1 月发表的预测器，后续新方法未纳入。
- 各预测器使用不同数据集和评测协议，性能不可直接比较。

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 综述未提供统一的性能比较基准 | 各预测器在不同数据集上报告 AUC/MCC，无法判断哪个方法真正最优 | 用户无法基于综述选择最佳工具 | 在统一基准（如 DisProt 最新版 + 独立测试集）上重新评测所有 30 个预测器 | Section 2.3, Table 2 中各预测器独立报告 |
| 「盐桥特征缺失」的论断缺乏定量证据 | 作者未展示加入盐桥特征后性能提升的实验数据 | 该论断是未来方向的核心论据，若无定量支持则说服力有限 | 在现有预测器（如 flDPnn）中加入盐桥特征，对比 AUC/MCC 变化 | Discussion 节 |
| AlphaFold2 在 IDP 上的适用性存疑 | AlphaFold2 对无序区域预测置信度低（pLDDT 低），直接用于 IDP 结合位点预测可能效果有限 | 作者将其作为主要未来方向，但未讨论其局限性 | 在 IDP 测试集上比较 AlphaFold2 结构特征与传统序列特征的预测性能 | Discussion 节 |
| 综述未讨论相分离/凝聚体相关预测 | IDP 介导的相分离是重要功能模式，但综述未涉及 LLPS 驱动序列预测 | 本课题关注相分离，该综述覆盖范围有限 | 补充 LLPS 预测方法（如 catGRANULE、PSPredictor）的综述 | 全文未提及相分离 |
| 分类框架可能过于简化 | 将预测器分为三类（scoring/ML/consensus）忽略了混合方法的细节差异 | 分类有助于概览，但可能掩盖方法间的关键差异 | 对每个预测器做更细粒度的特征-算法矩阵分析 | Section 2.3 |
| 未讨论训练集冗余/同源性偏差 | 训练集与测试集可能存在序列同源性，导致性能高估 | 这是计算预测领域的常见问题，影响泛化性评估 | 检查各预测器的训练/测试集划分是否做了去冗余处理 | 全文未提及 |

## 14 学到什么

> Agent 提炼的知识候选

1. **特征分层策略**：IDP-PPIS 预测的特征可系统分为六层——氨基酸组成、理化性质、进化信息（PSSM/HMM）、预测结构特征（二级结构、ASA、接触数）、disorder score、序列复杂度。本课题（IDP/IDR × 蛋白互作 × AI）在设计新模型时，可参考此分层框架，优先整合 disorder score + 进化信息 + 预测结构特征，这三类在综述中被反复证明有效。

2. **Multi-task 学习框架**：DeepDISOBind 的 multi-task 架构（共享层 + 任务特定层）同时预测 DNA/RNA/蛋白结合位点，且性能优于单任务模型。本课题可迁移此思路：同时预测蛋白结合位点、相分离驱动区域、翻译后修饰位点等多任务，利用任务间相关性提升泛化。

3. **Consensus 方法的鲁棒性增益**：DEPICTER 和 HybridPBRpred 证明，整合多个异构预测器的输出（而非仅用单一模型）可显著提升预测稳定性。本课题可构建「多预测器集成 + meta-learner」框架，将现有 IDP-PPIS 预测器（如 ANCHOR2、MoRFCHiBi、flPNN）作为基础特征，训练集成模型。

4. **数据偏差意识**：Disfani 数据集的免疫蛋白富集问题提醒我们，训练数据来源的偏差会直接影响模型泛化。本课题构建相分离相关数据集时，应主动检查蛋白功能类别分布，避免单一功能类主导。

5. **盐桥特征的价值**：作者指出盐桥在 IDP 互作中贡献局部刚性并触发 disorder-to-order 转变，但所有预测器均未使用。本课题可探索将盐桥预测（如从序列预测离子键）作为新特征，尤其对相分离体系（电荷互补是 LLPS 的重要驱动）。

6. **AlphaFold2 的 IDP 应用边界**：综述建议用 AlphaFold2 结构信息辅助 IDP-PPIS 预测，但需注意 AF2 对无序区域置信度低。本课题可尝试将 pLDDT 作为 disorder 置信度特征，而非直接使用 AF2 预测的结构坐标。

7. **基准数据集来源**：综述列出了该领域的核心数据库——DisProt（实验验证无序蛋白）、PDB（结构）、ELM（线性 motif）、DIBS（无序蛋白复合物）、MFIB（无序-无序复合物）、D2P2（大规模预测注释）。本课题构建训练集时，应优先从这些数据库交叉筛选。

8. **性能指标选择**：综述中各预测器主要报告 AUC 和 MCC。本课题在评估相分离预测模型时，建议同时报告 AUC、MCC、Precision-Recall AUC（正负样本不平衡时更可靠），并注意与现有 IDP-PPIS 预测器做公平对比。

## 15 与已有连接

- **相似综述**：Katuwawala et al. (2019a, 2019b) 是本文直接的前序综述，本文在其基础上更新了 2019–2022 年的新预测器，并补充了「影响性能因素」的系统分析。本课题读者可对比阅读，追踪该领域的时间演化。
- **方法基础**：ANCHOR/ANCHOR2 的能量估计方法源自 IUPred 的氨基酸对相互作用能量矩阵（Dosztányi et al., 2005），是 IDP 研究领域的经典方法。本课题若涉及物理模拟（如粗粒化 MD），可参考 ANCHOR 的能量框架设计 IDP-伴侣结合的自由能特征。
- **深度学习应用**：DeepDISOBind (Zhang et al., 2021) 的 multi-task 深度网络架构与 AlphaFold2 的 Evoformer 架构同属深度学习在蛋白领域的应用。本课题可参考其「共享表示 + 任务特定头」的设计模式。
- **数据库连接**：DisProt、PDB、ELM、DIBS、MFIB 是 IDP 研究的基础设施。本课题若构建相分离相关数据集，应优先从这些数据库提取训练/测试数据，确保与领域标准兼容。
- **冲突/补充**：本文强调序列特征的重要性，但未讨论物理模拟（MD/对接）方法在 IDP-PPIS 预测中的作用。本课题可补充这一视角：将 MD 模拟的构象系综特征（如结合自由能、接触图谱）与序列特征结合，可能超越纯序列方法的性能上限。
- **AlphaFold2 连接**：综述提及 AF2 在 IDP 预测中的潜力，但未深入。本课题可连接 AF2 的最新进展（如 AF2 的 pLDDT 与 disorder 的相关性研究），探索结构预测与无序预测的交叉。
- **相分离连接**：本文未涉及 LLPS，但 IDP-PPIS 与相分离驱动区域高度重叠（许多相分离驱动蛋白通过 IDR 互作介导凝聚）。本课题可将 IDP-PPIS 预测器作为相分离预测的基线或特征来源。

## 16 研究想法

> Agent 生成的研究候选

1. **候选名称**：IDR-LLPS-MultiTask——基于 multi-task 深度学习的 IDR 蛋白互作位点与相分离驱动区域联合预测
   - **来源局限/观察**：本文指出 IDP-PPIS 预测器聚焦短 motif，未覆盖长无序结合区；且未涉及相分离。而相分离驱动区域与 IDP 互作位点高度重叠。
   - **核心假设**：蛋白互作位点与相分离驱动区域共享序列特征（如电荷分布、疏水补丁、低复杂度区域），multi-task 学习可互相增强。
   - **初步方法**：以 DeepDISOBind 的 multi-task 架构为基础，增加 LLPS 驱动区域预测头；特征层整合 disorder score、PSSM、理化性质、盐桥预测特征；训练数据从 DisProt + ELM + 相分离数据库（如 PhaSepDB）交叉构建。
   - **验证方式**：在独立测试集上比较单任务 vs multi-task 的 AUC/MCC；与现有 IDP-PPIS 预测器（ANCHOR2、flPNN）和 LLPS 预测器（catGRANULE）对比。
   - **创新状态**：unverified

2. **候选名称**：SaltBridge-IDR——盐桥特征增强的 IDR 互作位点预测
   - **来源局限/观察**：作者明确指出所有 30 个预测器均未使用盐桥特征，而盐桥在 IDP 互作和 disorder-to-order 转变中起关键作用。
   - **核心假设**：盐桥预测特征可显著提升 IDP-PPIS 预测性能，尤其在电荷互补驱动的互作中。
   - **初步方法**：从序列预测盐桥（如基于共进化或结构预测），将盐桥概率作为新特征加入现有预测器（如 flPNN 或 DeepDISOBind）；对比有无盐桥特征的性能差异。
   - **验证方式**：在 DisProt 标注的 IDP-PPIS 数据集上做消融实验；分析盐桥特征在正负样本中的分布差异。
   - **创新状态**：unverified

3. **候选名称**：AF2-Disorder-Fusion——AlphaFold2 pLDDT 与序列特征融合的 IDR 互作位点预测
   - **来源局限/观察**：综述建议利用 AlphaFold2 结构信息，但未讨论 pLDDT 作为 disorder 置信度特征的潜力。
   - **核心假设**：AF2 的 pLDDT 低值区域与 IDP 互作位点相关，pLDDT 可作为有效特征提升预测性能。
   - **初步方法**：对训练集蛋白运行 AF2，提取每个残基的 pLDDT 值作为特征；与序列特征（PSSM、disorder score）融合，训练 ML 模型（如 gradient boosting 或深度网络）。
   - **验证方式**：比较有/无 pLDDT 特征的 AUC/MCC；分析 pLDDT 特征在已知 IDP-PPIS 残基上的分布。
   - **创新状态**：unverified

4. **候选名称**：Consensus-IDR-Ensemble——基于多预测器集成的 IDR 互作位点鲁棒预测框架
   - **来源局限/观察**：综述显示 consensus 方法（如 DEPICTER、HybridPBRpred）性能优于单一预测器，但现有集成方法仅整合 2-3 个基础预测器。
   - **核心假设**：整合更多异构预测器（ANCHOR2、MoRFCHiBi、flPNN、DeepDISOBind、SPOT-Disorder）可进一步提升预测鲁棒性和泛化性。
   - **初步方法**：将 5+ 个现有预测器的输出作为特征，训练 meta-learner（如 XGBoost 或逻辑回归）；在多个独立数据集上评估集成增益。
   - **验证方式**：比较单一预测器 vs 集成的 AUC/MCC/PR-AUC；分析集成在不同蛋白功能类别上的表现差异。
   - **创新状态**：unverified

5. **候选名称**：IDR-PPI-Physics——结合粗粒化 MD 模拟的 IDR 互作位点预测
   - **来源局限/观察**：综述仅覆盖序列基方法，未涉及物理模拟。而 IDP 互作涉及 disorder-to-order 转变，MD 模拟可提供构象系综信息。
   - **核心假设**：MD 模拟得到的结合自由能、接触图谱、构象熵等物理特征可补充序列特征的不足，提升 IDP-PPIS 预测精度。
   - **初步方法**：对已知 IDP-伴侣复合物做粗粒化 MD 模拟，提取每个残基的接触概率、结合自由能分解等特征；与序列特征融合训练预测模型。
   - **验证方式**：在实验验证的 IDP-PPIS 数据集上比较序列特征 vs 序列+MD 特征的性能；分析 MD 特征对长无序结合区的预测增益。
   - **创新状态**：unverified