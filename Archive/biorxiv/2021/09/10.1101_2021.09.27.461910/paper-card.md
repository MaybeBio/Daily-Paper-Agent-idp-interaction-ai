## 01 基本信息

- **标题**：AlphaFold2: A role for disordered protein prediction?
- **作者**：Carter J. Wilson; Wing-Yiu Choy; Mikko Karttunen
- **单位**：University of Western Ontario（加拿大韦仕敦大学，据作者邮箱推断）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2021-09-27
- **论文类型**：方法评估/基准测试（Benchmarking study）
- **领域**：结构生物学 × 无序蛋白预测 × 深度学习
- **关键词**：AlphaFold2, intrinsically disordered proteins (IDPs), pLDDT, disorder prediction, DSSP, CAID benchmark
- **DOI/ID**：10.1101/2021.09.27.461910
- **代码**：未提供（仅提供数据集链接）
- **数据**：https://github.com/SoftSimu/AlphaFoldDisorderData
- **阅读日期**：2026-05-13（按当前日期）
- **在该课题方向中的位置**：本文是早期系统评估 AlphaFold2 在无序蛋白/无序区预测中适用性的关键基准工作。它直接回答了「AlphaFold2 能否用于 IDP/IDR 预测」这一核心问题，并提出了 pLDDT 作为无序性度量的可行性，为后续将 AlphaFold2 输出（pLDDT）用于 IDP 互作位点预测、相分离驱动区识别等下游任务提供了方法学基础。该文处于「深度学习结构预测 × 无序蛋白」交叉方向的早期验证阶段。

## 02 一句话总结

本文在 CAID 基准数据集（DisProt 与 DisProt-PDB）上系统评估 AlphaFold2 预测无序蛋白区域的能力，发现基于 pLDDT 的预测器（tpLD）在无序区识别上优于朴素的 DSSP 结构指派方法，但传统序列预测器（如 fIDPnn）在 DisProt 数据集上仍优于 AlphaFold2，并揭示了 pLDDT 与二级结构之间的关联可能反映 IDP 构象动力学信息。

## 03 研究问题

- **具体问题**：AlphaFold2 能否有效预测 intrinsically disordered regions（IDRs）？其预测置信度指标 pLDDT 是否可作为无序性度量的可靠替代？与传统的序列基无序预测器相比，AlphaFold2 的表现如何？
- **为什么重要**：IDP/IDR 约占真核蛋白质组的 30% 以上，在信号转导、转录调控、相分离等过程中发挥核心作用。AlphaFold2 作为结构预测的范式突破，其输出是否可用于 IDR 注释，直接关系到海量 AlphaFold2 结构库（如 AlphaFold DB）能否被 IDP 领域有效利用。
- **现有方法为何不足**：传统序列基无序预测器（如 IUPred、fIDPnn 等）仅基于序列特征，缺乏结构上下文；而 AlphaFold2 虽不专门针对无序蛋白训练，但其 pLDDT 输出可能隐含了无序性信息，此前缺乏系统评估。
- **精确的 Can 问题**：Can AlphaFold2's pLDDT score serve as a reliable predictor of protein disorder, comparable to or better than dedicated sequence-based disorder predictors?

## 04 背景与发展脉络

*注：以下脉络为「经外部核验」的领域发展主线，结合本文框架整理。*

| 阶段 | 代表性方法 | 优点 | 局限 | 本文位置 |
|------|-----------|------|------|----------|
| 序列基无序预测（2000s-2010s） | IUPred, PONDR, ESpritz, DisoMine | 快速、无需结构、可批量注释 | 仅基于序列特征，缺乏结构上下文；对结合诱导折叠（folding-upon-binding）区域预测能力有限 | 本文将其作为对比基线 |
| 深度学习方法（2010s-2020s） | SPOT-Disorder, AUCpreD, fIDPnn, RawMSA | 利用进化信息和深度学习，精度提升 | 仍为序列基方法，未利用结构预测信息 | 本文选取 CAID 中 top 10 作为对比 |
| 结构预测范式突破（2020-2021） | AlphaFold2 (AF2) | 高精度结构预测，pLDDT 提供逐残基置信度 | 对 IDR 的预测机制不明确，pLDDT 与无序性的关系未被系统验证 | **本文填补此空白** |
| 后续发展（2022-） | AF2 在 IDR 研究中的应用扩展 | pLDDT 被广泛用于 IDR 注释、互作位点预测 | 需注意 pLDDT 对完全无序蛋白的偏差 | 本文为这一方向奠定基础 |

**本文主张的位置**：在 AF2 发布后、IDP 领域尚未系统评估其无序预测能力时，本文提供了首个基于 CAID 基准的系统比较，确立了 pLDDT 作为无序性度量的有效性边界。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 朴素 DSSP 指派导致无序含量严重高估 | 将 AF2 结构中非螺旋/非折叠区域全部视为无序，导致无序含量预测远高于实验值 | DSSP 仅基于几何/氢键模式指派二级结构，无法区分「有序环区」与「真正无序区」；AF2 对柔性区域的结构预测本身不可靠 | Results 图 3：DisProt 数据集上 DSSPp 无序含量分布峰值远高于实验值 |
| pLDDT 与无序性的关系未被验证 | AF2 发布后，pLDDT 主要被用于评估结构预测置信度，其在无序预测中的有效性未知 | AF2 训练目标为结构预测，pLDDT 与无序性的关联是间接的，需要系统验证 | 全文核心问题 |
| 传统序列预测器在含不确定残基数据集上表现差异大 | 在 DisProt（含不确定残基）上传统方法优于 AF2，但在 DisProt-PDB（无不确定残基）上 AF2 表现接近 | DisProt 中不确定残基可能包含真实无序区，而 AF2 对这些区域的 pLDDT 偏低，导致误分类 | Results 图 1、表 S1-S4 |
| 无序蛋白的构象动力学信息难以从静态结构获取 | AF2 输出单一静态结构，无法直接反映 IDP 的构象系综 | AF2 本质为静态结构预测器，不模拟构象系综 | Discussion：作者提出 pLDDT 可能间接反映构象动力学 |

## 06 核心思想

### 1) 表面方法

将 AlphaFold2 的 pLDDT 分数转化为无序性预测器（tpLD），并与 11 个传统序列基无序预测器在 CAID 基准的两个数据集（DisProt 和 DisProt-PDB）上进行系统比较。同时评估了朴素的 DSSP 二级结构指派方法（DSSPp）作为对照。

### 2) 核心洞察

- **pLDDT 是无序性的有效代理指标**：AF2 在训练过程中隐式学习了无序区域的低置信度特征，pLDDT 低分区域与实验注释的无序区域高度重合。
- **DSSP 指派不可用于无序预测**：AF2 对无序区域会生成任意但几何上合理的结构，DSSP 会将这些区域指派为环区（coil），但环区 ≠ 无序区，导致严重高估。
- **pLDDT 与二级结构的关系揭示动力学信息**：低 pLDDT 的螺旋/折叠区域可能代表瞬时结构（transient structure），高 pLDDT 的环区可能代表有序但非螺旋/折叠的稳定构象——这为从 pLDDT 提取 IDP 动力学信息提供了线索。

### 3) 可能的普适教训 [Analysis]

- **结构预测器的置信度分数可作为无序性/柔性的通用度量**：这一思路可迁移到其他深度学习结构预测器（如 ESMFold、RoseTTAFold）的置信度输出。
- **「预测结构」与「真实构象」的偏差本身携带生物学信息**：AF2 在无序区域的「低置信度」不是噪声，而是对构象熵的隐式编码。
- **基准数据集的选择决定结论边界**：DisProt 与 DisProt-PDB 的差异（是否含不确定残基）显著影响方法排名，提示 IDR 预测评估需明确标注不确定残基的处理策略。

## 07 方法总览

- **输入**：蛋白质氨基酸序列（来自 DisProt/DisProt-PDB 数据集，共 475 个靶标）
- **输出**：每个残基的无序/有序二分类预测
- **核心模块**：
  1. **AF2 结构获取**：从 EMBL AlphaFold 数据库下载预计算结构
  2. **DSSP 指派**：对 AF2 结构运行 DSSP 进行二级结构指派
  3. **pLDDT 提取**：从 AF2 输出中提取每个残基的 pLDDT 分数
  4. **tpLD 转换**：按 Tunyasuvunakool et al. 的公式将 pLDDT 转换为无序概率
  5. **pLD_n 二值化**：基于 MCC 最大化选择阈值（DisProt: 76, DisProt-PDB: 68，合并使用 72）
  6. **对比预测器**：11 个 CAID top 预测器（fIDPnn, SPOT-Disorder2, RawMSA, fIDPln, Predisorder, AUCpreD, SPOT-Disorder1, SPOT-Disorder-S, DisoMine, AUCpreD-np, ESpritz-D）
- **评估指标**：ROC-AUC, Precision-Recall (F_max), Matthews Correlation Coefficient (MCC), RMSD
- **工具**：scikit-learn（统计）、seaborn（KDE 可视化）
- **反馈回路**：无（静态基准测试，无迭代训练）
- **文字流程**：从 CAID 数据集获取序列 → 从 AlphaFold DB 下载 AF2 结构 → 对结构运行 DSSP 得到 DSSPp 预测 → 提取 pLDDT 并转换为 tpLD → 基于 MCC 选择阈值得到 pLD_n → 运行 11 个序列预测器 → 在两种数据集上计算所有指标 → 比较分析

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| AF2 结构获取 | 获取每个靶标的预测结构 | AF2 是本文评估的核心对象 | 输入：UniProt ID；输出：PDB 结构 + pLDDT | Methods "Dataset generation" | 无法进行任何 AF2 相关评估 |
| DSSP 指派（DSSPp） | 将 AF2 结构转为二级结构指派，coil 视为无序 | 作为「朴素基线」，模拟用户直接使用 AF2 结构注释无序区的做法 | 输入：AF2 PDB；输出：每个残基 H/E/T/C 指派 | Results 图 1-3 | 失去对照基线，无法展示 pLDDT 的增量价值 |
| pLDDT 提取与转换（tpLD） | 将 pLDDT 分数转换为无序概率 | pLDDT 是 AF2 输出的置信度指标，需转换为无序性度量 | 输入：pLDDT 分数（0-100）；输出：无序概率（0-1） | Methods Eq. 1, 引用 Tunyasuvunakool et al. | 无法将 AF2 用于无序预测 |
| 阈值选择（pLD_n） | 基于 MCC 最大化选择二值化阈值 | 将连续 pLDDT 转换为二值无序/有序标签 | 输入：tpLD 分数 + 真实标签；输出：最优阈值（76/68/72） | Results, 表 S3-S4 | 阈值选择不当会显著影响 MCC 和 F1 |
| 序列预测器对比 | 运行 11 个 CAID top 预测器 | 提供传统方法的性能基准 | 输入：序列；输出：无序概率/标签 | Results 图 1, 表 S1-S4 | 无法判断 AF2 相对传统方法的优劣 |
| 统计评估 | 计算 AUC, F_max, MCC, RMSD | 量化各方法性能 | 输入：预测 + 真实标签；输出：指标值 | Methods "Statistical analysis" | 无法进行方法间比较 |

## 09 关键公式符号

**tpLD 转换公式（Eq. 1）**：

$$p(\text{disorder}) = 1 - \frac{\text{pLDDT}}{100}$$

- pLDDT：AlphaFold2 输出的每个残基的预测局部距离差异测试分数（0-100）
- p(disorder)：该残基为无序的概率（0-1），1 表示完全无序

**RMSD 公式**：

$$\text{RMSD}(v, w) = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (v_i - w_i)^2}$$

- v, w：两个二进制向量（预测与真实标签）
- m：向量长度（蛋白质残基数）
- 随机预测器在均匀数据集上的 RMSD ≈ 0.7

**MCC（Matthews Correlation Coefficient）**：标准二分类评估指标，用于选择 pLD_n 的最优阈值。

## 10 实验设计与证据链

**数据集**：
- DisProt：475 个靶标，基于 DisProt 数据库注释（2018 年 11 月版），所有非无序残基标记为有序
- DisProt-PDB：同一 475 个靶标，但仅有无 PDB 结构覆盖的残基才可标记为无序，无注释残基被掩码
- 数据来源：CAID 基准数据集（少于 CAID 的 646 个靶标，因 AF2 结构缺失）

**指标**：ROC-AUC, Precision-Recall F_max, MCC, RMSD

**基线/对比**：11 个 CAID top 序列预测器（fIDPnn, SPOT-Disorder2, RawMSA, fIDPln, Predisorder, AUCpreD, SPOT-Disorder1, SPOT-Disorder-S, DisoMine, AUCpreD-np, ESpritz-D）

| 实验 | 检验的 Claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|------------------|------|
| DSSP vs pLDDT 无序预测 | 朴素 DSSP 指派导致无序高估 | DSSPp vs tpLD/pLD_n，两个数据集 | tpLD AUC 0.905 (DisProt-PDB), DSSPp 显著更低；无序含量分布 DSSPp 高估 | pLDDT 优于朴素 DSSP 指派 | 不能说明 pLDDT 优于所有传统方法 | Results 图 1-3, 表 S1-S2 |
| AF2 vs 传统预测器 | AF2 能否超越专用无序预测器 | tpLD/pLD_n vs 11 个 CAID top 预测器 | DisProt-PDB 上 tpLD F_max 0.784 最高；DisProt 上 fIDPnn 最优 (F_max 0.457 vs tpLD 0.429) | AF2 在无不确定残基数据集上表现优异；在含不确定残基数据集上不如专用方法 | 不能断言 AF2 全面优于传统方法 | Results 图 1, 表 S1-S4 |
| pLDDT 与二级结构关系 | pLDDT 分布与二级结构类型相关 | KDE 分析所有残基的 pLDDT 分布按 DSSP 类别分层 | Coil 呈双峰分布（峰值约 94 和 35）；螺旋/折叠呈左偏分布 | pLDDT 可区分「有序环区」与「真正无序区」 | 不能直接推断 pLDDT 与动力学的关系 | Results 图 4, 图 S8-S11 |
| SSC 分析 | 局部二级结构上下文影响 pLDDT | 引入 secondary structure codon (SSC) 三连体分析 | 螺旋末端（HHC/CHH 等）可低至 <50；折叠末端（EEC/CEE 等）未观察到 <50 | 螺旋比折叠更可能具有瞬时性 | 样本量有限，需更大规模验证 | Results 图 S8-S11 |

## 11 结论正确解读

- **任务范围**：仅评估 AF2 对**全局无序含量**和**残基级无序/有序二分类**的预测能力，不涉及无序区域的具体构象系综、结合机制或功能注释。
- **Oracle/真值输入**：使用 DisProt 实验注释作为无序金标准；DisProt-PDB 中 PDB 结构覆盖区域视为有序。AF2 结构为预计算（非针对本数据集重新运行），pLDDT 为 AF2 原始输出。
- **端到端状态**：非端到端——AF2 本身不输出无序预测，需通过 pLDDT 转换和后处理（阈值选择）才能得到无序标签。
- **算力成本**：未报告 AF2 推理成本；但使用预计算结构，实际计算成本仅为 DSSP 运行和 pLDDT 转换，极低。
- **历史数据依赖**：AF2 训练集（PDB）天然偏向有序蛋白，对完全无序蛋白的预测可能系统性偏差。
- **模型依赖**：结论基于 AlphaFold2 v2.0 预计算结构；后续版本（如 AF3）或 ESMFold 等可能表现不同。
- **最难情形**：完全无序蛋白（>95% 无序）和含不确定残基的蛋白（DisProt 数据集）是 AF2 表现最差的场景。
- **群体/领域边界**：结论适用于球状蛋白为主的蛋白质组；对膜蛋白、RNA 结合蛋白等特殊类别未单独验证。
- **不确定性**：pLDDT 与无序性的关系是相关性而非因果性；pLDDT 低分也可能反映同源二聚体界面、配体结合位点等非无序因素。

**有边界的复述**：在 CAID 基准的 475 个蛋白上，AF2 的 pLDDT 分数经简单线性转换后，可作为无序区预测的有效指标，在无不确定残基的 DisProt-PDB 数据集上达到与顶尖序列预测器相当的性能；但在含不确定残基的 DisProt 数据集上，传统序列预测器（如 fIDPnn）仍具优势。pLDDT 不能替代专用无序预测器，但可作为补充工具，且其与二级结构的关联可能为 IDP 动力学研究提供新视角。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据集规模有限 | 仅 475 个靶标（少于 CAID 的 646 个），因 AF2 结构缺失 | 未明确提及 | Methods "Dataset generation" |
| AF2 对完全无序蛋白的预测可能不可靠 | 高度无序蛋白（>95%）的 pLDDT 分布与实验注释偏差较大 | 未明确提及 | Results 图 2 |
| pLDDT 与无序性的关系为间接推断 | AF2 训练目标非无序预测，pLDDT 低分可能有其他原因 | 建议进一步研究 pLDDT 与 IDP 动力学的关系 | Discussion |
| 未进行多序列比对（MSA）深度分析 | AF2 的 MSA 深度可能影响 pLDDT 可靠性 | 未明确提及 | 未提供 |
| 阈值选择依赖数据集 | pLD_76/pLD_68 基于 MCC 最大化，可能过拟合 | 未明确提及 | Results |

**作者提及的相关约束**（非正式局限）：
- AF2 结构为静态快照，无法反映 IDP 的构象系综（Discussion）
- 训练集对无序蛋白的覆盖不足，可能影响 pLDDT 在 IDP 上的校准（Discussion）

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| pLDDT 与无序性的关系可能受训练集偏差驱动 | AF2 训练集（PDB）中柔性区域天然低 pLDDT，但这可能反映「晶体堆积/表达偏好」而非「生理无序性」 | 若 pLDDT 低分仅反映「不可结晶性」，则其在 IDP 功能研究中的价值有限 | 比较 AF2 在 NMR 验证的无序区域与晶体结构缺失区域上的 pLDDT 分布 | Discussion 中作者承认训练集偏差 |
| DisProt 与 DisProt-PDB 的性能差异被归因于「不确定残基」，但未深入分析 | 不确定残基可能包含真实无序区，也可能包含实验噪声；两种解释对结论影响不同 | 决定 AF2 在真实 IDP 注释中的可用性 | 对不确定残基进行亚分类（如 NMR 化学位移 vs 有限蛋白水解）后重新评估 | Results 图 1 vs 图 S1 |
| SSC 分析仅描述相关性，未建立因果机制 | pLDDT 与二级结构的关联可能由 AF2 架构（如 Evoformer 注意力模式）而非物理真实性驱动 | 若为架构伪影，则 pLDDT 对 IDP 动力学的推断不可靠 | 比较 AF2 与 ESMFold/RoseTTAFold 的 pLDDT-SSC 关联是否一致 | Results 图 4, 图 S8-S11 |
| 未报告 AF2 运行参数和版本细节 | 不同 AF2 版本（v2.0 vs v2.1 vs v2.2）的 pLDDT 校准可能不同 | 影响结果可复现性和跨版本泛化 | 在多个 AF2 版本上重复实验 | Methods 仅提及 "downloaded from EMBL database" |
| 比较基准仅限 CAID top 预测器，未包含更简单的基线（如氨基酸组成） | 简单基线（如 Q/C 含量）可能已能解释大部分无序性方差 | 若简单特征即可达到相近性能，pLDDT 的增量价值存疑 | 增加氨基酸组成、疏水性等简单特征作为对照 | 未提供 |

## 14 Agent 提炼的知识候选

**面向 IDP/IDR × 蛋白互作 × AI/物理模拟方向的可迁移知识：**

1. **pLDDT 作为无序性代理指标的校准方法**：本文的 tpLD 转换（1 - pLDDT/100）和阈值选择策略（基于 MCC 最大化）可直接迁移到 IDR 注释任务。在相分离研究中，可将 pLDDT 低分区域与已知相分离驱动区（如 PrLD、RGG 基序）进行重叠分析，验证 pLDDT 是否能富集凝聚体驱动残基。

2. **「预测器置信度」作为构象熵的隐式编码**：核心洞察——AF2 的低置信度区域可能反映构象多样性。可迁移到 MD 模拟：将 pLDDT 分布与 MD 模拟的 RMSF（均方根波动）进行对比，检验 pLDDT 是否能作为 MD 采样充分性的先验指导，或用于选择 MD 起始构象。

3. **DSSP 不可用于 IDR 注释的警示**：对使用 AF2 结构进行 IDR 注释的研究者，本文提供了明确的方法学警告——直接使用 DSSP 环区作为无序区会导致严重高估。在相分离研究中，若使用 AF2 结构预测凝聚体形成区域，应优先使用 pLDDT 而非二级结构指派。

4. **基准数据集构建策略**：DisProt vs DisProt-PDB 的对比揭示了「不确定残基」处理对评估结果的影响。在 IDR 互作预测中，构建训练/测试集时需明确标注无结构覆盖区域的处理方式，否则可能导致性能评估偏差。

5. **SSC（二级结构密码子）分析框架**：引入三连体局部二级结构上下文分析 pLDDT 分布的方法，可迁移到 IDR 功能基序分析——例如检验特定 SSC 模式是否富集在已知互作位点或相分离驱动区。

6. **多预测器集成思路**：本文对比了 AF2 与 11 个序列预测器，发现不同数据集上各有优劣。在 IDR 互作位点预测中，可考虑将 pLDDT 与序列预测器输出作为多视图特征进行集成学习。

## 15 与已有知识连接

- **Tunyasuvunakool et al. (2021)**：本文的 tpLD 转换公式直接引用自此工作，该文首次提出 pLDDT 可用于识别无序区域。本文在此基础上进行了系统基准测试。
- **CAID 基准 (Necci et al., 2021)**：本文使用的数据集和对比预测器均来自 CAID 工作，该基准是 IDR 预测领域的标准评估平台。
- **DisProt 数据库 (Hatos et al., 2020)**：无序蛋白注释的金标准数据库，本文的标签来源。
- **AlphaFold2 原论文 (Jumper et al., 2021)**：AF2 的 pLDDT 被定义为预测 lDDT 的期望值，本文将其重新解释为无序性度量。
- **与相分离研究的连接 [Analysis]**：pLDDT 低分区域与相分离驱动区（如低复杂度结构域 LCD）的重叠尚未被系统验证，这是本文结论可直接延伸的方向。后续研究（如 2022-2024 年多篇工作）已开始使用 pLDDT 注释相分离相关区域。
- **与 MD 模拟的连接 [Analysis]**：本文提出的 pLDDT-动力学关联假说，与 MD 模拟中 IDP 的构象系综采样形成互补——pLDDT 可提供全蛋白质组的无序性先验，MD 可提供原子级动力学细节。

## 16 Agent 生成的研究候选

**候选 1：pLDDT 引导的相分离驱动区识别**
- **名称**：PhaseSep-pLDDT：基于 AlphaFold2 pLDDT 的相分离驱动区全蛋白质组扫描
- **来源局限/观察**：本文证明 pLDDT 可有效识别无序区，但未验证其与相分离驱动区（如 LCD、PrLD）的关联
- **核心假设**：pLDDT 低分且序列复杂度低的区域富集相分离驱动残基
- **增量**：将 pLDDT 与序列复杂度、电荷分布等相分离特征结合，构建相分离驱动区预测器
- **初步方法**：在 CAID 数据集上训练 pLDDT + 序列特征的分类器，用已知相分离蛋白（如 FUS、TDP-43）验证
- **验证方式**：与实验验证的相分离区域（LLPS 数据库）进行重叠率比较
- **创新状态**：unverified

**候选 2：pLDDT 与 MD 模拟的协同采样策略**
- **名称**：pLDDT-guided MD：利用 AlphaFold2 置信度指导 IDP 构象系综的增强采样
- **来源局限/观察**：本文提出 pLDDT 可能反映 IDP 动力学，但未与 MD 模拟结合验证
- **核心假设**：pLDDT 低分区域的构象熵高于高分区域，可用 pLDDT 作为副本交换 MD（REMD）的温度/偏置势先验
- **增量**：将静态预测置信度转化为 MD 采样偏置，加速 IDP 系综收敛
- **初步方法**：选取 10 个 IDP，比较 pLDDT 引导的 REMD 与标准 REMD 的构象采样效率
- **验证方式**：与实验 SAXS/NMR 数据对比系综平均性质
- **创新状态**：unverified

**候选 3：多预测器集成的 IDR 互作位点预测**
- **名称**：Ensemble-IDR：融合 pLDDT 与序列预测器的 IDR 互作位点预测框架
- **来源局限/观察**：本文发现 AF2 与序列预测器在不同数据集上各有优势，提示互补性
- **核心假设**：pLDDT 与序列预测器捕捉无序性的不同方面，集成可提升互作位点预测精度
- **增量**：首个将 AF2 结构置信度与序列无序预测融合的互作位点预测器
- **初步方法**：以 pLDDT、fIDPnn、IUPred 等为特征，在 IDR 互作位点数据集（如 MFIB）上训练分类器
- **验证方式**：与单一特征预测器比较 AUC/PR
- **创新状态**：unverified

**候选 4：SSC 模式与 IDP 结合诱导折叠的关联分析**
- **名称**：SSC-Dynamics：二级结构密码子模式作为 IDP 结合诱导折叠的预测因子
- **来源局限/观察**：本文的 SSC 分析显示 pLDDT 与局部二级结构上下文相关，但未探索其功能意义
- **核心假设**：特定 SSC 模式（如 HHC/CHH）富集的区域更可能经历 disorder-to-order 转变
- **增量**：将静态结构预测转化为结合诱导折叠倾向性预测
- **初步方法**：分析已知结合诱导折叠区域（来自 DIBS 数据库）的 SSC 分布，与随机 IDR 区域比较
- **验证方式**：留一交叉验证预测结合区域
- **创新状态**：unverified

**候选 5：pLDDT 校准的跨物种迁移性**
- **名称**：Cross-species pLDDT：AlphaFold2 无序预测在不同物种蛋白质组中的一致性验证
- **来源局限/观察**：本文仅使用人类相关蛋白（DisProt 为主），未验证跨物种泛化
- **核心假设**：pLDDT 的无序预测能力在细菌、植物、哺乳动物中一致
- **增量**：为全蛋白质组 IDR 注释提供适用性边界
- **初步方法**：从 UniProt 选取 5 个物种各 100 个蛋白，比较 pLDDT 与实验无序注释的一致性
- **验证方式**：跨物种 AUC 一致性分析
- **创新状态**：unverified