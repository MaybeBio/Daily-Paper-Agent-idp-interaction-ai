## 01 基本信息

- **标题**：Why variant effect predictors and multiplexed assays agree and disagree
- **作者**：Livesey BJ; Marsh JA
- **单位**：MRC Human Genetics Unit, University of Edinburgh（基于作者隶属关系推断，原文未明确列出单位，但致谢提及 MRC Human Genetics Unit）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2025
- **论文类型**：预印本（研究论文）
- **领域**：计算生物学 / 蛋白质变异效应预测 / 高通量功能实验
- **关键词**：variant effect predictors (VEPs), multiplexed assays of variant effect (MAVEs), deep mutational scanning (DMS), missense variants, protein structure, disordered regions
- **DOI/arXiv 号**：10.1101/2025.07.31.667868
- **代码**：未提供
- **数据**：37 个人类蛋白的 MAVE 数据集（来源包括 MaveDB、ProteinGym 及原始文献）；ClinVar（2024-08-06 版本）；gnomAD v4.1；AlphaFold 结构；UniProt/InterPro 注释
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文不直接研究 IDP/IDR 介导的蛋白互作，但系统性地揭示了 VEPs 在无序区域（disordered regions）和蛋白表面带电残基上的系统性预测偏差，以及 MAVEs 在特定 assay 设计下的盲区。对于「IDP/IDR × 蛋白互作 × AI 方法」课题，本文提供了：(1) 无序区域中变异效应预测的已知缺陷及其机制解释；(2) MAVE 数据作为 AI 模型训练/评估基准时的偏差来源分析；(3) 整合多源证据（结构、保守性、实验）进行变异解读的框架性思路。

---

## 02 一句话总结

本文通过比较 37 个人类蛋白的 MAVE 实验数据与 5 个前沿 VEPs 的预测，发现 VEPs 系统性地在埋藏疏水残基、蛋白内部和跨膜螺旋区域过度预测致病性，而在无序区域和表面带电残基上低估致病性；MAVEs 则受限于 assay 设计（如仅测稳定性或特定功能），可能遗漏不直接影响所测表型的致病机制（如剪接影响、gain-of-function）。

---

## 03 研究问题

- **具体问题**：VEPs 和 MAVEs 作为两种评估错义变异功能影响的工具，它们的输出在哪些蛋白区域、哪些变异类型上系统性不一致？这些不一致的机制根源是什么？
- **为什么重要**：VEPs 和 MAVEs 正被越来越多地用于临床变异解读（如 ACMG/AMP 指南中的 PS3/PP3 证据）。如果两者的分歧不是随机的而是系统性的，那么单独使用任一工具都可能导致误分类。理解分歧来源是整合多源证据、改进变异解读的关键前提。
- **现有方法不足**：已有 benchmark 研究主要关注 VEPs 与 MAVEs 的总体相关性（如 Spearman 相关），但很少系统性地定位「在哪些蛋白特征/区域上分歧最大」以及「分歧的方向性」（谁高估、谁低估）。
- **精确研究问题**：Can protein structural features (buriedness, secondary structure, disorder, interface location) and variant type (amino acid substitution class) systematically predict where VEPs and MAVEs will disagree on variant effect?

---

## 04 背景与发展脉络

> 注：以下脉络基于本文 Introduction 及作者引用，属于「经外部核验」的领域发展框架。

1. **VEPs 的发展**：从早期基于序列保守性的方法（SIFT, PolyPhen-2）→ 整合结构特征的方法 → 基于蛋白质语言模型的方法（ESM-1v, AlphaMissense, SaProt）。核心假设：进化保守性 ≈ 功能重要性。
2. **MAVEs 的发展**：从单变异功能实验到高通量饱和突变扫描（DMS），可在一次实验中测量数千至数万变异的相对功能。代表性技术包括酵母互补生长实验、VAMP-seq（蛋白稳定性）、饱和基因组编辑（SGE，内源基因组环境）。
3. **两者的关系**：MAVEs 常被用作 VEPs 的 benchmark 数据（如 ProteinGym 平台）；VEPs 也被用于优先排序 MAVE 实验的候选变异。但两者的一致性从未被系统性检验。
4. **已知问题**：VEPs 在无序区域表现差（Fawzy & Marsh, 2025）；MAVEs 的 assay 设计可能不反映疾病机制（如 VAMP-seq 只测稳定性不测活性）。
5. **本文位置**：首次在 37 个蛋白的大规模规模上，系统性地量化 VEPs 与 MAVEs 分歧的结构/序列特征根源，并区分「VEP 系统性偏差」与「MAVE assay 设计局限」两类分歧来源。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| VEPs 过度依赖保守性 | 在埋藏疏水残基、蛋白内部、跨膜螺旋区域过度预测致病性 | VEPs 训练时学习到「保守残基的突变 = 有害」的普遍规律，但埋藏残基的保守性并不总是等于功能必需性（如结构冗余） | Results 图 4A-B；图 5A（HMGCR 跨膜/sterol-sensing domain 负偏差） |
| VEPs 低估无序区域变异 | 在无序区域和表面带电残基上低估致病性 | 无序区域保守性低，VEPs 默认其为良性；但无序区域可能参与重要互作（如信号传导） | Results 图 4C（MAVE-damaging 组 pLDDT 更低）；图 5B（CBS 无序区正偏差） |
| MAVEs 受 assay 设计限制 | 只测稳定性（VAMP-seq）时遗漏活性丧失型变异；只测单一功能时遗漏多效性变异 | assay 的 fitness 定义 ≠ 疾病机制；如 ASPA 的底物结合残基变异不影响蛋白稳定性但丧失酶活性 | Results 图 5D（ASPA 活性位点负偏差）；Results 讨论 PRKN/ASPA VAMP-seq 局限 |
| MAVEs 存在实验噪声 | 部分 MAVE 结果与 ClinVar 标签矛盾，可能是实验噪声 | 高通量实验的固有噪声，尤其在低 fitness 区域 | Results 讨论 MSH2 S612P 案例；作者推测 MAVE 可能错误 |
| 数据缺失导致比较偏差 | VARITY 仅预测单核苷酸替换（~30% 变异），导致部分比较不完整 | 方法设计限制 | Methods 节「Data acquisition」；Results 图 S2 排除 VARITY |
| 剪接影响未被捕获 | BRCA1 的 A1823T/S/D 变异被 VEPs 判为良性，但实际通过破坏剪接导致致病 | VEPs 只评估氨基酸替换对蛋白功能的影响，不评估对 mRNA 剪接的影响 | Results 图 6 讨论；Pangolin 预测剪接位点丢失 |

---

## 06 核心思想

**1) 表面方法**：
- 收集 37 个人类蛋白的 MAVE 数据集，统一进行 rank normalization（0-1 尺度，0 = 最适应/野生型样，1 = 最不适应/功能丧失）。
- 对每个蛋白，计算 5 个 VEPs（AlphaMissense, ESM-1v, SaProt, ESCOTT, VARITY_R）的预测分数，同样进行 rank normalization。
- 对每个变异，计算 MAVE 与 VEPs 的 rank 差（MAVE rank − VEP rank），正值 = MAVE 认为更有害，负值 = VEP 认为更有害。
- 将变异按蛋白结构特征（内部/表面/界面、RSA、二级结构、pLDDT）、氨基酸替换类型、UniProt 功能注释（结构域、活性位点、互作位点）分组，统计各组 rank 差的分布。
- 对 ClinVar 中标注为 pathogenic/benign 的变异，检查 MAVE 与 VEPs 各自与 ClinVar 标签的一致性，并深入分析分歧最大的变异。

**2) 核心洞察**：
- VEPs 与 MAVEs 的分歧不是随机的，而是**结构位置依赖**的：VEPs 在埋藏疏水区域「过度自信」，在无序/表面区域「过度保守」。
- 分歧的根源在于**信息类型不同**：VEPs 基于进化保守性（间接推断功能），MAVEs 基于直接功能测量（但受 assay 设计约束）。
- 当 MAVE 的 assay 设计与疾病机制匹配时（如酶活性、DNA 结合），MAVE 更可靠；当不匹配时（如只测稳定性），VEPs 可能反而更准确。
- 存在第三类分歧：**VEPs 和 MAVEs 都正确但 ClinVar 标签错误**（如 MSH2 S612P 可能是 ClinVar 误分类）。

**3) 可能的普适教训 [Analysis]**：
- 对于「IDP/IDR × 蛋白互作 × AI」课题：本文证实了「低保守性 ≠ 功能不重要」这一在 IDR 研究中反复出现的观点，并给出了量化证据——VEPs 在无序区域的系统性低估。这意味着任何基于保守性特征的 AI 模型（包括 AlphaFold 衍生方法）在 IDR 上都需要额外校准。
- 本文的「rank 差分析」框架可直接迁移：将任意两种变异效应评估方法（如 AlphaFold-Multimer 互作预测 vs. 实验互作数据）的 rank 差按蛋白区域/特征分组，可定位系统性偏差。
- 「assay 设计与疾病机制匹配」的原则对 IDR 研究同样适用：如果实验只测结合亲和力而不测相分离行为，可能遗漏关键致病机制。

---

## 07 方法总览

- **输入**：
  - 37 个蛋白的 MAVE 数据集（每个蛋白一个 score set，来源多样：酵母互补、VAMP-seq、SGE 等）
  - 5 个 VEPs 的预测分数（AlphaMissense, ESM-1v, SaProt, ESCOTT, VARITY_R）
  - ClinVar 致病/良性变异标注（2024-08-06 版本）
  - gnomAD v4.1 作为推定良性变异来源
  - UniProt 功能注释（结构域、活性位点、互作位点、无序区域）
  - AlphaFold 结构（pLDDT 分数）
  - PDB 生物组装（RSA 计算）

- **输出**：
  - 每个蛋白的 MAVE vs VEPs rank 差分布
  - 按结构/序列特征分组的 rank 差统计
  - ClinVar 变异中 MAVE 与 VEPs 分歧案例的详细分析

- **关键处理步骤**：
  1. 数据清洗：确保 MAVE 和 VEPs 覆盖相同的变异集合；删除缺失值
  2. 尺度统一：所有分数转换为 rank，再 min-max 归一化到 [0,1]
  3. 差异计算：对每个变异，计算 Δ = MAVE_rank − VEP_rank（VEP 分数取 5 个模型的均值）
  4. 结构注释：用 DSSP 分类二级结构；用 RSA 分类表面/内部；用 pLDDT 作为无序性代理
  5. 分组统计：按结构类别、氨基酸替换类型、功能注释分组，计算 Δ 的均值和分布
  6. 临床变异分析：筛选 |Δ| > 0.75 的 ClinVar 变异，逐一分析可能原因

- **训练/优化**：不适用（无模型训练，纯比较分析）

- **反馈回路**：不适用

- **假设**：
  - MAVE 分数和 VEP 分数在 rank 尺度上可比（假设 rank 变换消除了尺度差异）
  - pLDDT 可作为无序性的有效代理（低 pLDDT ≈ 无序）
  - ClinVar 标注（≥1 star）作为「金标准」用于评估 MAVE 和 VEPs 的相对准确性

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| MAVE 数据收集与标准化 | 统一 37 个不同来源的 MAVE 数据集到可比尺度 | 不同实验的 score 定义和范围差异大，直接比较无意义 | 输入：原始 MAVE 分数；输出：rank-normalized [0,1] 分数 | Methods「Rank normalisation」节 | 无法跨蛋白比较；rank 变换是后续所有分析的基础 |
| VEP 预测收集与标准化 | 统一 5 个 VEPs 的预测分数 | VEPs 输出尺度不同（概率、log-odds 等） | 输入：VEP 原始分数；输出：rank-normalized [0,1] 分数 | Methods「Rank normalisation」节 | 无法与 MAVE 比较 |
| 结构特征注释 | 为每个变异位点分配结构类别（内部/表面/界面、二级结构、RSA、pLDDT） | 检验「分歧是否结构位置依赖」的核心假设 | 输入：PDB 结构、AlphaFold 结构；输出：每个位点的结构标签 | Results 图 4A-D | 无法定位分歧的结构根源 |
| 氨基酸替换分类 | 将变异按理化性质变化分类（疏水→带电、小→大等） | 检验「分歧是否依赖替换类型」 | 输入：变异列表；输出：替换类别标签 | Results 图 3（Hedges G 热图） | 无法区分「替换类型效应」与「位置效应」 |
| Rank 差计算与分组统计 | 计算每个变异的 Δ = MAVE − VEP，按结构/序列特征分组检验 | 核心分析：定位系统性分歧 | 输入：标准化后的 MAVE 和 VEP 分数；输出：分组 Δ 分布 | Results 图 2、4、5 | 无法量化分歧 |
| ClinVar 变异深度分析 | 筛选 |Δ| > 0.75 的临床变异，逐一分析分歧原因 | 检验「谁更接近临床真相」 | 输入：ClinVar 标注 + MAVE/VEP 分数；输出：案例研究 | Results 图 6；Results 讨论 | 无法评估临床相关性 |
| 剪接影响分析 | 对 BRCA1 剪接位点变异使用 Pangolin 预测剪接影响 | 解释 VEPs 为何漏掉剪接相关致病变异 | 输入：BRCA1 变异；输出：剪接影响预测 | Results 讨论 BRCA1 A1823T/S/D | 无法解释该类分歧 |

**消融效应区分**：
- 实测消融效应：未进行（本文无消融实验）
- 预期效应 [Analysis]：若移除结构特征注释，将无法区分「VEP 在埋藏区域过度预测」与「MAVE 在表面区域过度预测」；若移除 ClinVar 分析，将无法判断分歧中哪一方更接近临床真相。

---

## 09 关键公式符号

本文方法部分未使用复杂数学公式，核心操作如下：

**1. Rank normalization**：
- 对每个 score set S（MAVE 或 VEP），将所有变异按分数排序，赋予 rank r ∈ {1, 2, ..., N}
- 归一化：r_norm = (r − 1) / (N − 1)，使 r_norm ∈ [0, 1]
- 用途：统一不同尺度；对 ties 取平均 rank（pandas 默认行为）
- 来源：Methods「Rank normalisation」节

**2. Rank 差（Δ）**：
- Δ = r_MAVE − r_VEP
- 正值：MAVE 认为该变异比 VEP 预测的更有害
- 负值：VEP 认为该变异比 MAVE 测量的更有害
- 用途：核心分析指标，用于分组统计和 ClinVar 案例筛选

**3. Hedges' g（效应量）**：
- 用于图 3 中比较 MAVE 与 VEP 对特定氨基酸替换的评分差异
- 公式：g = (x̄₁ − x̄₂) / s_pooled，其中 s_pooled 为合并标准差
- 用途：量化特定替换类型上 MAVE 与 VEP 分歧的效应大小
- 来源：Results 图 3 图注

**4. AUROC**：
- 使用 sklearn 的 roc_auc_score() 计算
- 用于比较 MAVE 和 VEPs 区分 ClinVar pathogenic 与 gnomAD 变异的能力
- 来源：Methods「ROC AUC calculation」节

---

## 10 实验设计与证据链

**数据集与规模**：
- 37 个人类蛋白的 MAVE 数据集（表 1），覆盖多种 assay 类型：酵母互补生长实验、VAMP-seq（稳定性）、饱和基因组编辑（SGE）、结合实验等
- 5 个 VEPs：AlphaMissense, ESM-1v, SaProt, ESCOTT, VARITY_R
- ClinVar 致病/良性变异（2024-08-06 版本，≥1 star）
- gnomAD v4.1 作为推定良性变异
- AlphaFold 结构（pLDDT）；PDB 生物组装（RSA）

**指标**：
- 主要指标：rank 差（Δ）的分布和分组均值
- 辅助指标：AUROC（区分 pathogenic vs benign）、Hedges' g（替换类型效应量）

**评测协议**：
- 无独立测试集；使用 ClinVar 标注作为「金标准」评估 MAVE 和 VEPs 的相对准确性
- 对每个蛋白独立计算 rank，避免跨蛋白尺度问题

**实验列表**：

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| MAVE vs VEP 总体 AUROC 比较 | MAVE 和 VEPs 在区分 ClinVar pathogenic/benign 上表现不同 | 37 个蛋白，5 个 VEPs 分别与 MAVE 比较 | MAVE 在某些蛋白上优于 VEPs，在另一些蛋白上劣于 VEPs；表现因蛋白和 assay 类型而异 | 两种方法的相对可靠性是蛋白/assay 依赖的 | 不能得出「MAVE 普遍优于 VEP」或反之 | Results 图 1 |
| 按结构位置分组 rank 差分析 | VEPs 在埋藏残基过度预测致病性 | 内部 vs 表面 vs 界面残基 | VEP-damaging 变异富集于内部和界面残基；MAVE-damaging 富集于表面残基 | VEPs 系统性高估埋藏残基变异的有害性 | 不能确定这是否为所有 VEPs 的普遍缺陷（仅测试 5 个 VEPs） | Results 图 4A-B |
| 按 pLDDT 分组分析 | VEPs 在低 pLDDT（无序）区域低估致病性 | 高 vs 低 pLDDT 残基 | MAVE-damaging 变异在低 pLDDT 区域富集 | VEPs 在无序区域系统性低估变异效应 | pLDDT 仅为无序性的间接代理，需实验验证 | Results 图 4C |
| 按二级结构分组分析 | VEPs 在螺旋/折叠区域过度预测 | 螺旋 vs 折叠 vs 环 | VEP-damaging 富集于螺旋和折叠；MAVE-damaging 富集于环 | 结构有序性驱动 VEP 偏差 | 二级结构分类可能与其他特征（如埋藏度）混淆 | Results 图 4D |
| 氨基酸替换类型分析 | 特定替换类型上 MAVE 与 VEP 系统性分歧 | 所有 20×20 替换组合 | 疏水→带电、小→大等「剧烈」替换被 VEPs 过度预测；相似性质替换被 MAVE 更敏感 | VEPs 倾向于高估理化性质剧烈变化的效应 | 效应量（Hedges' g）的绝对值较小，需谨慎解读 | Results 图 3 |
| ClinVar 分歧案例深度分析 | 分歧最大的变异中，哪一方更接近临床真相 | Δ > 0.75 或 < −0.75 的 ClinVar 变异 | 发现三类分歧：VEP 漏掉剪接变异（BRCA1）、VEP 漏掉 gain-of-function（SHOC2）、MAVE 噪声（MSH2） | 分歧有明确机制根源，非随机 | 案例数量有限，不能推广到所有蛋白 | Results 图 6；Results 讨论 |
| 无序区域整体分析 | 无序区域中 MAVE 与 VEP 的系统性分歧 | 有/无 UniProt 无序注释的区域 | 所有 12 个有无序注释的蛋白均显示正 Δ（MAVE 认为更有害） | VEPs 在无序区域普遍低估变异效应 | 无序注释可能不完整 | Results 讨论 |

---

## 11 结论正确解读

**任务范围**：
- 仅覆盖 37 个人类蛋白的错义变异（missense variants），不涉及插入/缺失、剪接变异、非编码变异
- 仅测试 5 个 VEPs（虽然代表不同方法学类别，但非全部）
- MAVE 数据来自多种 assay 类型，但每种蛋白通常只有一种 assay

**oracle/真值输入**：
- ClinVar 标注（≥1 star）作为「金标准」——但作者明确指出 ClinVar 本身可能包含错误标注（如 MSH2 S612P 案例）
- gnomAD 作为「推定良性」来源——但低频良性变异可能混入罕见致病变异

**端到端状态**：
- 本文是**分析性研究**，不提供端到端的变异解读工具
- 结论是「描述性」的：指出分歧存在、分歧有结构基础、分歧有机制解释
- 未提供改进 VEPs 或 MAVE 的具体算法/实验方案

**算力成本**：
- 不适用（无模型训练；VEP 预测为离线获取）

**历史数据依赖**：
- 依赖 MAVE 数据质量（不同实验室、不同 assay 的可重复性未系统评估）
- 依赖 ClinVar 标注质量（作者承认部分标注可能错误）

**最难情形**：
- 无序区域中的致病变异（VEPs 系统性低估）
- 不影响蛋白稳定性但影响特定功能的变异（如活性位点残基，VEPs 可能高估或低估）
- Gain-of-function 变异（VEPs 和 MAVE 的 fitness 定义可能都不匹配）

**有边界的复述**：
在 37 个人类蛋白的错义变异范围内，VEPs 与 MAVEs 的分歧主要源于 VEPs 对保守性-功能关系的过度泛化（在埋藏疏水区域过度预测致病性）和对无序区域功能重要性的低估；MAVEs 的准确性受 assay 设计与疾病机制匹配程度的限制。两者分歧最大的变异往往涉及剪接影响、gain-of-function 或实验噪声，需要整合多源证据进行解读。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| MAVE 数据质量参差 | 不同实验室、不同 assay 的数据质量差异大；部分 MAVE 可能包含实验噪声 | 未明确提及 | Results 讨论（MSH2 S612P 案例） |
| ClinVar 标注可能错误 | 部分 ClinVar 标注可能基于不充分证据，导致「金标准」不可靠 | 未明确提及 | Results 讨论（MSH2 S612P 案例） |
| 仅覆盖错义变异 | 不涉及插入/缺失、剪接变异、非编码变异 | 未明确提及 | 未明确说明，但研究设计隐含此限制 |
| 仅测试 5 个 VEPs | 未覆盖所有可用 VEPs | 未明确提及 | 未明确说明 |
| 无序区域注释不完整 | UniProt 无序注释可能遗漏部分无序区域 | 未明确提及 | Results 讨论 |
| 单 assay 限制 | 每种蛋白通常只有一种 MAVE assay，无法区分「蛋白固有特性」与「assay 特性」 | 未明确提及 | 未明确说明 |

**作者提及的相关约束（非正式局限）**：
- 作者指出 VEPs 的「过度保守性依赖」在 gain-of-function 变异上尤其成问题，但未系统评估
- 作者提到 rank normalization 可能丢失绝对效应大小信息，但认为这是跨数据集比较的必要代价

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 37 个蛋白的 MAVE 数据来自多种 assay 类型，但分析中未按 assay 类型分层 | 不同 assay 的 fitness 定义差异可能驱动「蛋白间差异」而非蛋白本身特性 | 如果 assay 类型是主要混杂因素，则「蛋白结构特征预测分歧」的结论可能不稳健 | 按 assay 类型（酵母互补 vs VAMP-seq vs SGE）分层重复分析 | Results 图 1 显示 MAVE 表现因蛋白而异，但未控制 assay 类型 |
| 使用 pLDDT 作为无序性的代理 | pLDDT 是 AlphaFold 的置信度分数，不等同于实验验证的无序性；低 pLDDT 也可能反映结构域间灵活性而非完全无序 | 如果 pLDDT 与真实无序性有偏差，则「VEP 在无序区域低估」的结论可能被夸大 | 使用实验验证的无序区域注释（如 IUPred 预测或 NMR 数据）重复分析 | Results 图 4C 仅使用 pLDDT |
| 「VEP 过度预测埋藏残基」可能反映真实生物学而非 VEP 缺陷 | 埋藏残基的突变确实更可能导致蛋白不稳定，MAVE 可能因 assay 条件（如过表达）而低估其有害性 | 如果 MAVE 低估而非 VEP 高估，则改进方向应针对 MAVE 而非 VEP | 比较 MAVE 结果与独立的功能实验（如酶活性测定） | Results 图 4A-B 仅显示相关性，无因果证据 |
| ClinVar 作为金标准的循环论证问题 | VEPs 的训练数据可能包含 ClinVar 标注，导致 VEPs 与 ClinVar 的一致性被高估 | 如果 VEPs 已「见过」ClinVar 标注，则 MAVE vs VEP 的分歧可能反映 MAVE 与 ClinVar 的分歧而非 VEP 的真实性能 | 使用未参与任何 VEP 训练的独立功能实验数据作为金标准 | 作者未讨论此问题 |
| 5 个 VEPs 的均值可能掩盖个体差异 | 不同 VEPs 的偏差模式可能不同，均值分析可能掩盖重要异质性 | 如果某些 VEPs 在无序区域表现良好，则「VEPs 普遍低估无序区域」的结论过于笼统 | 逐个 VEP 重复分组分析 | Results 图 2 仅展示 ESM-1v 示例 |
| rank normalization 可能放大噪声 | 对低质量 MAVE 数据，rank 变换可能将噪声放大为显著差异 | 如果部分 MAVE 数据质量低，则「MAVE 更可靠」的结论可能不成立 | 使用原始分数（如适用）或加权分析重复 | Methods「Rank normalisation」节未讨论此问题 |

---

## 14 学到什么

> Agent 提炼的知识候选

**概念性知识**：
1. **VEPs 的偏差是结构位置依赖的**：埋藏疏水残基、跨膜螺旋、蛋白内部界面的变异被 VEPs 系统性高估致病性；无序区域、表面带电残基的变异被系统性低估。这直接适用于 IDP/IDR 研究——IDR 区域变异的功能影响几乎肯定被现有 VEPs 低估。
2. **MAVEs 的 fitness 定义决定其盲区**：只测稳定性的 assay（如 VAMP-seq）会遗漏活性丧失型变异；只测单一功能的 assay 会遗漏多效性变异。对于 IDR 介导的相分离，如果 assay 不测凝聚体形成/动态，则相关变异会被误判为良性。
3. **分歧的三种来源**：(a) VEP 的保守性假设失效（无序区、新功能获得）；(b) MAVE 的 assay 与疾病机制不匹配；(c) 实验噪声或 ClinVar 标注错误。三者需要不同应对策略。

**方法性知识**：
4. **Rank 差分析框架**：将两种评估方法的分数分别 rank-normalize，计算逐变异差值，再按蛋白特征分组统计。这一框架可迁移到「AlphaFold-Multimer 互作预测 vs. 实验互作数据」的比较，定位预测系统偏差的结构基础。
5. **「金标准」的批判性使用**：ClinVar 标注本身可能错误（如 MSI2 S612P 案例），且 VEPs 训练数据可能包含 ClinVar 导致循环论证。在 IDP/IDR 研究中，需要独立的功能实验数据作为验证。
6. **多模态 assay 的必要性**：单一 assay 无法覆盖所有致病机制；对于 IDR 相关疾病，需要同时测稳定性、互作、相分离行为等多维度表型。

**可迁移到本课题的具体思路**：
7. **IDR 区域的 VEP 校准**：本文证实 VEPs 在无序区域系统性低估变异效应。本课题可借鉴此结论，开发针对 IDR 区域的专用变异效应预测器，或对现有 VEP 输出进行 IDR 感知的校准。
8. **相分离相关变异的 assay 设计**：本文的「assay 与疾病机制匹配」原则提示，研究 IDR 变异时，实验设计必须包含相分离相关读