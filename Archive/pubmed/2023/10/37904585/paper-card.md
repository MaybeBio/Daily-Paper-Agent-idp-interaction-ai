## 01 基本信息

- **标题**：DisProt in 2024: improving function annotation of intrinsically disordered proteins
- **作者**：Aspromonte, Maria Cristina; Nugnes, Maria Victoria; Quaglia, Federica; Bouharoua, Adel; Tosatto, Silvio C E; Piovesan, Damiano
- **单位**：未提供（根据作者信息推测为意大利帕多瓦大学相关机构，但原文未明确列出）
- **期刊/平台**：Nucleic Acids Research
- **年份**：2023（在线发表日期 2023-10-31）
- **论文类型**：数据库资源更新报告（Database Update Article）
- **领域**：生物信息学、蛋白质科学、 intrinsically disordered proteins (IDPs)
- **关键词**：DisProt、intrinsically disordered proteins、功能注释、MIABLE、Gene Ontology、AlphaFold2
- **DOI/arXiv 号**：10.1093/nar/gkad928
- **代码**：未提供
- **数据**：DisProt 数据库（https://disprot.org），release 2023_06
- **阅读日期**：2026-05-13（按当前日期）
- **该文在课题方向中的位置**：本文是 IDP/IDR 领域核心数据库 DisProt 的更新报告，提供了大规模、人工精选的实验证据注释数据，是 IDP 功能注释的"金标准"资源。对于「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向，本文的价值在于：(1) 提供了可用于训练/验证 AI 预测模型的基准数据集；(2) 展示了如何将实验证据标准化为机器可读的注释；(3) 揭示了 AlphaFold2 pLDDT 与实验注释之间的关联与差异，为理解 AI 结构预测在 IDP 上的局限性提供了参考。

---

## 02 一句话总结

DisProt 数据库 2023_06 版本通过引入 MIABLE 标准、扩展 ECO 证据码和 Gene Ontology 功能注释，将蛋白质数量增至 2649 个（较上一版增长 30%），功能注释区域翻倍，并发现 DisProt 实验注释的 disorder 含量与 AlphaFold2 pLDDT 预测在阈值 80 处达到最大相关性（Pearson r = 0.42），但两者在 folding-upon-binding 蛋白上存在系统性偏差。

---

## 03 研究问题

**具体问题**：如何系统性地提升 intrinsically disordered proteins (IDPs) 功能注释的质量与覆盖度，并使其成为可被计算预测方法利用的标准化资源？

**为什么重要**：IDPs 在细胞调控、信号转导和疾病中发挥核心作用，但其功能难以通过传统结构生物学方法表征。缺乏标准化的实验证据注释是开发可靠 IDP 功能预测模型的主要瓶颈。同时，AlphaFold2 等 AI 结构预测工具在 IDP 上的表现需要实验数据来校准和验证。

**现有方法不足**：此前 DisProt 版本存在以下问题：(1) 功能注释覆盖度低，仅约半数蛋白有功能注释；(2) 缺乏统一的实验条件描述标准，导致不同实验间的可比性差；(3) 证据类型单一，无法捕获作者推断等非直接实验证据；(4) 与 Gene Ontology 的整合不充分，限制了与其他数据库的互操作性。

**精确研究问题**：Can systematic adoption of MIABLE standards and expanded evidence codes in DisProt improve both the quality and coverage of IDP function annotations, and can these curated annotations serve as a reliable benchmark for validating AI-based disorder predictions (e.g., AlphaFold2 pLDDT)?

---

## 04 背景与发展脉络

*注：以下脉络基于本文框架及可核验的外部知识，标注为「经外部核验」的部分基于公开文献。*

**阶段一：IDP 数据库的早期建设（2005-2015）**
- 代表性方法：DisProt 初始版本（2005）、IDEAL、MFIB 等
- 优点：首次系统收集 IDP 实验证据
- 局限：注释规模小、缺乏标准化、功能注释稀少
- 本文位置：DisProt 是该领域的开创者，本文是其持续更新

**阶段二：标准化与互操作性提升（2015-2021）**
- 代表性方法：DisProt 引入 IDPO 本体、CAID 实验基准（2019）
- 优点：建立了 disorder 注释的本体框架，推动了预测方法评测
- 局限：功能注释仍不充分，实验条件描述不统一
- 本文位置：本文延续此脉络，进一步引入 MIABLE 和 GO

**阶段三：AI 结构预测时代（2021-至今）**
- 代表性方法：AlphaFold2（2021）、AlphaFold DB、CAID 2.0
- 优点：提供全蛋白质组的结构预测，pLDDT 可作为 disorder 的代理指标
- 局限：对 IDP 的预测存在系统性偏差，folding-upon-binding 区域常被误预测为结构化
- 本文位置：本文首次系统比较 DisProt 实验注释与 AlphaFold2 pLDDT 的相关性，为理解 AI 预测在 IDP 上的可靠性提供了基准

**阶段四：功能注释的深化（本文）**
- 代表性方法：MIABLE 标准、ECO 扩展、GO 整合、主题数据集
- 优点：功能注释翻倍，证据类型更丰富，与其他数据库（UniProtKB）实现自动传播
- 局限：仍依赖人工文献挖掘，存在注释偏差
- 本文位置：本文是此阶段的代表性工作

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 功能注释覆盖不足 | 仅约半数 DisProt 蛋白有功能注释 | 人工文献挖掘耗时，功能实验数据本身稀缺 | 本文提到功能注释区域从 2021_08 到 2023_06 翻倍，暗示此前覆盖不足 |
| 实验条件描述不统一 | 不同实验间的 disorder 结论难以直接比较 | 缺乏统一的实验条件报告标准 | 引入 MIABLE 标准以系统化记录实验条件 |
| 证据类型单一 | 仅捕获直接实验证据，忽略作者推断 | 此前 ECO 术语范围有限 | 新增 ECO:0006218（组合实验与作者推断）、ECO:0000305（策展人推断）、ECO:0000302（作者陈述） |
| 与外部数据库互操作性差 | 功能注释无法自动传播到 UniProtKB 等核心资源 | 未采用 GO 本体 | 加入 GO 联盟，实现注释自动传播 |
| AlphaFold2 预测与实验注释存在偏差 | 部分实验验证的 disorder 区域被 AlphaFold2 预测为高置信度结构化 | AlphaFold2 偏向预测折叠构象，folding-upon-binding 区域被误判 | 图 1B 显示对角线以上的蛋白（实验 disorder 高但 pLDDT 高）对应 folding-upon-binding 案例 |
| 注释偏差（under-annotation） | 部分蛋白在 DisProt 中 disorder 注释不足，但 AlphaFold2 预测为低置信度 | 文献研究通常聚焦单一区域而非全长蛋白，策展人难以评估全长状态 | 图 1B 对角线以下的案例，如 Nuclear fragile X mental retardation-interacting protein 1 (DP03731) 和胶原蛋白家族 |

---

## 06 核心思想

### 1) 表面方法

DisProt 2023_06 版本的系统性更新，包括：(a) 扩大数据库规模（2649 个蛋白，+30%）；(b) 引入 MIABLE 标准记录实验条件；(c) 扩展 ECO 证据码以捕获更多证据类型；(d) 全面采用 Gene Ontology 进行功能注释；(e) 新增 5 个主题数据集；(f) 改进 FeatureViewer 可视化界面，整合 InterPro、MobiDB-lite 和 AlphaFold2 pLDDT 轨道。

### 2) 核心洞察

**数据标准化是 AI 方法发展的前提**：DisProt 的核心价值不在于数据量本身，而在于将散落的实验文献转化为机器可读、标准化的注释。MIABLE 和 ECO 的引入使得不同实验间的可比性增强，为训练和验证 IDP 预测模型提供了更可靠的基准。

**实验注释与 AI 预测的互补性**：通过系统比较 DisProt 注释与 AlphaFold2 pLDDT，本文揭示了 AI 预测在 IDP 上的系统性偏差——folding-upon-binding 区域常被误预测为结构化。这一发现不仅说明了 AI 方法的局限，也反过来证明了实验注释数据库的必要性。

**功能注释是 IDP 研究的下一前沿**：结构注释（disorder 区域定位）已相对成熟，但功能注释（这些区域做什么）是更大的挑战。GO 的引入使功能注释从"定性描述"走向"标准化分类"，为未来功能预测方法提供了训练数据。

### 3) 可能的普适教训 [Analysis]

- **基准数据的质量比数量更重要**：对于 IDP 预测方法的开发，一个经过严格策展、带有实验条件元数据的小规模数据集，可能比大规模但注释粗糙的数据集更有价值。这提示本课题在构建 AI 训练集时应优先考虑数据质量。
- **AI 预测与实验数据的系统性偏差需要显式建模**：AlphaFold2 在 IDP 上的偏差不是随机噪声，而是有生物学根源的（folding-upon-binding）。本课题若使用 AlphaFold2 作为工具，应意识到其对 IDP 的预测需要实验数据校准。
- **本体论驱动的注释是跨数据库互操作的关键**：采用 GO 等标准本体使 DisProt 的注释能自动传播到 UniProtKB，极大提升了数据的可发现性和可用性。本课题若构建新的 IDP 互作数据集，应考虑采用标准本体。

---

## 07 方法总览

**输入**：
- 科学文献（PubMed 收录的实验论文）
- 实验数据（NMR、X-ray、SAXS、CD 等）

**输出**：
- 标准化的 disorder 结构注释（区域定位）
- 标准化的功能注释（GO 术语 + IDPO 术语）
- 带 MIABLE 元数据的实验条件记录
- 主题数据集（按生物学主题组织的蛋白集合）

**核心模块**：
1. **文献挖掘与策展流程**：由专业策展团队（biocurators）从文献中提取 disorder 证据，经培训和质量控制后录入数据库
2. **MIABLE 标准化模块**：记录实验条件（construct 定义、实验参数、缓冲液条件等）
3. **本体注释模块**：使用 IDPO（结构）和 GO（功能）双本体进行注释
4. **证据编码模块**：使用 ECO 术语标记证据类型（实验、作者推断、策展人推断等）
5. **验证与质量控制模块**：资深策展人验证（43% 区域标记为 validated）
6. **数据传播模块**：通过 GO 联盟将功能注释自动传播到 UniProtKB
7. **可视化模块**：FeatureViewer 整合多源信息（InterPro、MobiDB-lite、AlphaFold2 pLDDT）

**训练**：不适用（数据库建设，非预测模型）

**反馈回路**：CAID 实验使用 DisProt 作为基准数据集，预测方法的评测结果反过来指导数据库的改进方向

**假设**：
- 文献中的实验证据可以被标准化为机器可读的注释
- disorder 是一个可被实验定义和验证的生物学属性
- 功能注释（GO）能充分捕获 IDP 的功能多样性

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 文献策展流程 | 从文献中提取 disorder 证据并标准化 | 实验数据散落在大量文献中，需要人工判断和标准化 | 输入：PubMed 文献；输出：标准化的 disorder 注释 | 数据库从 2005 年持续运行至今，规模持续增长 | 数据库将无法更新，失去"金标准"地位 |
| MIABLE 标准化 | 记录实验条件元数据 | 不同实验条件下的 disorder 结论可能不同，需要上下文信息 | 输入：实验方法部分；输出：标准化的实验条件描述 | 本文明确说明"systematically applying MIABLE principles" | 注释的可比性和可解释性下降，用户无法判断注释的适用条件 |
| IDPO + GO 双本体注释 | 分别注释结构状态和功能 | 结构注释（哪里 disorder）和功能注释（disorder 区域做什么）是不同维度 | 输入：策展判断；输出：IDPO 和 GO 术语 | 表 3 显示 GO 术语使用量大幅增加 | 功能注释将退化为定性描述，无法支持计算预测 |
| ECO 证据编码 | 标记证据类型和强度 | 不同证据类型的可靠性不同，用户需要过滤 | 输入：证据来源判断；输出：ECO 术语 | 新增 3 种 ECO 术语（ECO:0006218, ECO:0000305, ECO:0000302） | 用户无法区分直接实验证据和推断证据，可能误用注释 |
| 验证流程 | 资深策展人复核注释 | 保证注释质量 | 输入：初级策展注释；输出：validated 注释 | 43% 区域标记为 validated | 注释错误率上升，数据库可信度下降 |
| FeatureViewer 可视化 | 整合多源信息展示 | 用户需要同时查看实验注释和预测结果 | 输入：DisProt 注释 + InterPro + MobiFold + AlphaFold2 pLDDT；输出：集成可视化 | 本文描述新增 AlphaFold2 pLDDT 轨道 | 用户需要手动整合多数据库信息，效率降低 |
| 数据传播到 UniProtKB | 通过 GO 注释自动传播 | 扩大数据影响力，惠及更广泛用户 | 输入：DisProt GO 注释；输出：UniProtKB 功能注释 | 本文明确说明"automatically propagated to UniProtKB" | 数据影响力受限，IDP 功能注释在 UniProtKB 中缺失 |

---

## 09 关键公式符号

本文为数据库资源报告，不涉及数学公式或算法模型。核心的定量指标为 Pearson 相关系数，用于衡量 DisProt 实验注释的 disorder 含量与 AlphaFold2 pLDDT 预测之间的相关性：

**Pearson 相关系数**：
r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² · Σ(yᵢ - ȳ)²]

其中：
- xᵢ：DisProt 中蛋白 i 的实验注释 disorder 含量（disorder 残基比例）
- yᵢ：AlphaFold2 对蛋白 i 的预测 disorder 含量（pLDDT < 阈值 的残基比例）
- 本文报告在 pLDDT = 80 阈值处达到最大相关：r = 0.42，P-value = 6.26e−101

**pLDDT 阈值**：本文使用 pLDDT < 70 作为 disorder 预测的阈值（与 AlphaFold DB 的"low confidence"分类一致）

---

## 10 实验设计与证据链

**数据集/群体**：
- DisProt release 2023_06：2649 个蛋白，10822 条实验证据，覆盖 407 个物种
- 与上一版本（2021_08）对比：蛋白数增长 30%，功能注释区域翻倍
- 文献来源：3468 篇独立文献

**指标**：
- 数据库规模（蛋白数、证据数、物种数）
- 功能注释覆盖度（GO 术语数量、注释区域数）
- 与 AlphaFold2 的一致性（Pearson 相关系数）

**基线/对比**：
- 与 DisProt 2021_08 版本对比增长情况
- 与 AlphaFold2 pLDDT 预测对比（图 1A、1B）

**评测协议**：
- 无标准 benchmark 协议（数据库报告）
- 相关性分析使用全部 DisProt 蛋白的 disorder 含量 vs AlphaFold2 预测

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|-------------------|------|
| 数据库规模统计 | DisProt 持续增长 | 2021_08 vs 2023_06 | 蛋白 +30%，功能注释翻倍 | 数据库在持续扩展 | 增长是否代表领域整体进展而非选择性策展 | Results "Database growth" |
| 新增 ECO 术语 | 能捕获更多证据类型 | 新增 3 种 ECO 术语 | 部分蛋白 disorder 含量显著提升（如 DP02376 从 0.7% 到 63.6%） | 扩展证据类型能提高注释覆盖 | 作者推断证据的可靠性未单独验证 | Results "Disorder content" |
| DisProt vs AlphaFold2 相关性 | 实验注释与 AI 预测一致 | 不同 pLDDT 阈值（70-90） | 最大相关在 pLDDT=80：r=0.42，P=6.26e−101 | 两者在整体水平上一致 | 相关性中等（r=0.42），不能支持个体蛋白水平的一致性 | Results "Disorder content" 图 1A |
| 对角线以上案例分析 | folding-upon-binding 导致 AlphaFold2 高估结构 | 实验 disorder 高但 pLDDT 高的蛋白 | 对应 Antitoxin YefM、Calsequestrin-1、eIF4E-BP2 等已知 folding-upon-binding 蛋白 | AlphaFold2 对 folding-upon-binding 蛋白存在系统性偏差 | 未提供系统性的偏差量化分析 | Results "Disorder content" 图 1B |
| 对角线以下案例分析 | 存在 under-annotation | 实验 disorder 低但 pLDDT 低的蛋白 | 包括 Nuclear fragile X protein、胶原蛋白等 | 部分蛋白在 DisProt 中注释不足 | 未验证这些蛋白是否确实 disorder | Results "Disorder content" 图 1B |

---

## 11 结论正确解读

**任务范围**：本文是数据库资源报告，不涉及端到端的预测模型开发。其核心贡献是数据资源的更新与标准化。

**oracle/真值输入**：DisProt 的注释基于人工文献策展，以实验证据为"真值"。但需要注意：(1) 实验证据本身可能有条件依赖性（不同 pH、温度、结合状态下的 disorder 状态可能不同）；(2) 作者推断类证据（ECO:0000302）的可靠性低于直接实验证据。

**端到端状态**：不适用（非预测模型）。

**算力成本**：不适用。

**历史数据依赖**：DisProt 依赖已发表的文献，存在发表偏倚——研究热点区域的蛋白注释更充分，而"非热点"蛋白可能被低估。

**模型依赖**：本文不依赖特定预测模型，但展示了与 AlphaFold2 的比较结果。

**最难情形**：folding-upon-binding 蛋白是实验注释与 AI 预测差异最大的类别。这类蛋白在游离状态下无序，但结合后折叠，AlphaFold2 倾向于预测折叠构象。

**群体/领域边界**：DisProt 覆盖 407 个物种，但以真核生物为主；病毒蛋白也有一定覆盖。原核生物的 IDP 注释相对较少。

**不确定性**：DisProt 与 AlphaFold2 的相关性为中等（r=0.42），说明两者在个体蛋白水平上存在显著差异。这种差异既可能来自 AlphaFold2 的预测误差，也可能来自 DisProt 的注释不足。

**有边界的复述**：DisProt 2023_06 版本通过标准化改进，提供了更大规模、更高质量的 IDP 功能注释数据；该数据与 AlphaFold2 pLDDT 在整体水平上中等相关，但 folding-upon-binding 蛋白是系统性偏差的主要来源。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 注释覆盖仍不完整 | 部分蛋白（如胶原蛋白家族）在 DisProt 中 disorder 注释不足 | 鼓励社区提交新注释，开放外部贡献者提交表单 | Results "Disorder content" |
| 功能注释存在偏倚 | 统计反映的是数据库当前内容，可能受主题数据集和策展优先级影响 | 未明确提及 | Results "Disorder function" |
| 与 AlphaFold2 相关性中等 | r=0.42，个体蛋白水平差异大 | 未明确提及 | Results "Disorder content" |
| 依赖人工策展 | 策展速度受限于人力资源 | 通过培训材料和 APICURON 激励机制扩大策展团队 | Introduction, Training material |

*注：作者在本文中未系统性地列出局限性，以上为从文中可推断的约束。*

**作者提及的相关约束**（非正式局限）：
- 功能注释的统计"does not provide a complete overview of the functions of disordered proteins but rather reflects the information available in the database and could be biased by the specific thematic datasets and organisms currently available"（Results "Disorder function"）
- 低 pLDDT 并不总是 disorder 的可靠指标，可能受 MSA 质量影响（Results "Disorder content" 中对图 1B 的解释）

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 新增 ECO 术语大幅提升 disorder 含量 | 作者推断类证据（ECO:0000302）可能引入主观偏差，不同策展人的判断标准可能不一致 | 如果推断证据质量参差，数据库的"金标准"地位可能受损 | 比较仅含实验证据的子集与含推断证据的完整集的注释一致性；评估策展人间一致性 | Results "Disorder content" 中 DP02376 案例 |
| 与 AlphaFold2 相关性分析使用全部蛋白 | 不同蛋白家族的 disorder 特征差异大，全局相关性可能掩盖亚组差异 | 对特定蛋白家族（如含 PRM 的蛋白）的预测可靠性可能不同 | 按蛋白家族/功能类别分层计算相关性 | Results "Disorder content" 图 1A |
| 对角线以下案例被解释为 under-annotation | 也可能是 AlphaFold2 的假阳性预测（MSA 质量差导致低 pLDDT） | 如果大量"under-annotation"实为 AlphaFold2 误差，则数据库的完整性可能被高估 | 对候选 under-annotation 蛋白进行定向实验验证 | Results "Disorder content" 图 1B |
| 功能注释使用 GO 术语 | GO 术语可能无法充分捕获 IDP 特有的功能模式（如相分离、分子伴侣功能） | 如果 GO 覆盖不足，功能注释的实用性受限 | 检查 IDP 相关 GO 术语的覆盖度，与 IDPO 术语的互补性 | Results "Disorder function" |
| 主题数据集的引入 | 主题数据集可能引入选择偏倚，使数据库内容偏向特定生物学主题 | 影响下游统计分析和预测模型训练的公平性 | 比较主题数据集内外的蛋白特征分布 | Results "Database growth" 表 1 |
| 与 UniProtKB 的自动传播 | 传播机制可能放大注释错误，且用户难以追溯原始证据 | 错误注释可能被下游用户误用 | 评估传播后注释的可追溯性和错误率 | Results "Disorder function" |

---

## 14 Agent 提炼的知识候选

**面向课题方向（IDP/IDR × 蛋白互作 × AI/物理模拟）的可迁移知识：**

1. **基准数据的标准化框架**：DisProt 的 MIABLE + ECO + GO 三层注释框架可直接借鉴。本课题若构建 IDP 互作数据集，应采用类似的三层结构：实验条件（MIABLE 风格）、证据类型（ECO 风格）、功能类别（GO 风格），以支持跨数据库互操作和 AI 模型训练。

2. **AlphaFold2 pLDDT 作为 disorder 代理指标的校准方法**：本文展示了如何系统比较实验注释与 pLDDT 预测。本课题在使用 AlphaFold2 预测 IDP 结构或互作时，应意识到：(a) pLDDT < 70 可作为 disorder 的粗略指标；(b) folding-upon-binding 区域是系统性误判的高发区；(c) 最佳阈值（本文为 80）可能因蛋白家族而异，需要针对特定体系校准。

3. **folding-upon-binding 作为 IDP 互作的核心机制**：本文揭示的 AlphaFold2 偏差实际上指向了一个重要的生物学现象——folding-upon-binding 是 IDP 参与蛋白互作的主要模式之一。本课题在研究 IDP 介导的互作时，应将 folding-upon-binding 视为核心机制，而非异常情况。

4. **主题数据集的组织方式**：DisProt 的"thematic datasets"按生物学主题组织蛋白集合，便于用户快速获取特定领域的注释数据。本课题可借鉴此方式，按互作类型（如相分离、信号传导、转录调控）组织 IDP 互作数据。

5. **注释偏倚的识别与处理**：本文揭示的 under-annotation 问题提示，任何基于文献挖掘的数据集都存在偏倚。本课题在使用 DisProt 或其他数据库训练模型时，应检查注释偏倚对模型性能的影响。

6. **策展质量控制流程**：DisProt 的验证流程（43% 区域由资深策展人复核）和 APICURON 激励机制，为社区驱动的数据建设提供了可复制的模式。本课题若涉及大规模数据标注，可借鉴此质量控制思路。

7. **跨数据库传播机制**：DisProt 通过 GO 联盟实现注释自动传播到 UniProtKB，极大提升了数据影响力。本课题的成果若涉及功能注释，应考虑与 GO 等标准本体的兼容性。

---

## 15 与已有知识连接

**可核验的外部文献/资源：**

1. **DisProt 早期版本**：Hatos et al. (2022) "DisProt: intrinsic protein disorder annotation in 2020" 描述了此前版本的功能和数据结构。本文是这一系列的持续更新。

2. **AlphaFold2**：Jumper et al. (2021) "Highly accurate protein structure prediction with AlphaFold" (Nature) 是 pLDDT 指标的原始来源。本文将其应用于 IDP 比较。

3. **CAID 实验**：Nezhady et al. (2021) "Critical Assessment of protein Intrinsic Disorder prediction (CAID)" 使用 DisProt 作为基准数据集。本文提到的 CAID 和 CAID4 是 IDP 预测方法评测的权威平台。

4. **MIABLE 标准**：Quaglia et al. (2022) "MIABLE: Minimum Information About Disorder Experiments" 是本文采用的实验标准。

5. **IDPO 本体**：本文使用的 IDP 本体，与 Gene Ontology 互补。

6. **MobiDB**：Piovesan et al. (2021) "MobiDB: intrinsically disordered proteins in 2021" 是 DisProt 的姊妹数据库，提供自动预测的 disorder 注释。

7. **FuzDB**：Mészáros et al. (2021) "FuzDB: database of fuzzy complexes" 关注 IDP 互作中的模糊复合物，与本课题的 IDP 互作方向直接相关。

8. **PED 数据库**：Lazar et al. (2021) "PED in 2021: a major update of the protein ensemble database" 提供 IDP 构象系综数据。

**与本课题的关联**：
- 本课题若使用 AI 方法预测 IDP 互作，DisProt 的功能注释可作为训练/验证数据
- 本课题若使用物理模拟（MD）研究 IDP 互作，DisProt 的实验条件元数据（MIABLE）可帮助设置模拟条件
- 本文揭示的 AlphaFold2 在 folding-upon-binding 上的偏差，提示本课题在使用 AlphaFold2 预测 IDP 互作界面时应谨慎

---

## 16 Agent 生成的研究候选

### 候选 1：基于 DisProt 功能注释的 IDP 互作预测模型
- **名称**：IDP-FuncNet：利用 DisProt 功能注释预测 IDP 互作伙伴
- **来源局限/观察**：DisProt 功能注释显示 IDP 主要参与结合和调控功能，但缺乏系统性的互作伙伴预测工具
- **核心假设**：IDP 的功能注释（GO 术语）与互作伙伴类型之间存在可学习的关联模式
- **相对本文的增量**：本文仅提供数据，未开发预测模型；本候选将数据转化为预测工具
- **初步方法**：将 DisProt 功能注释编码为特征向量，结合序列特征（如 MoRF 预测、电荷分布），训练分类器预测互作伙伴类型（蛋白/核酸/小分子）
- **验证方式**：在 DisProt 留出集上交叉验证，与 UniProtKB 注释对比
- **可能的失败模式**：功能注释偏倚导致预测偏差；GO 术语粒度不足
- **创新状态**：unverified

### 候选 2：AlphaFold2 pLDDT 与实验 disorder 注释的系统性偏差分析
- **名称**：AF2-DisorderGap：量化 AlphaFold2 在 IDP 上的预测偏差及其生物学根源
- **来源局限/观察**：本文报告 r=0.42 的中等相关性，但未系统分析偏差的蛋白家族分布
- **核心假设**：AlphaFold2 的 disorder 预测偏差与蛋白的互作模式（如 folding-upon-binding vs. 组成型 disorder）相关
- **相对本文的增量**：本文仅展示相关性；本候选将深入分析偏差的结构与功能决定因素
- **初步方法**：对 DisProt 全部蛋白计算 pLDDT 与实验注释的逐残基差异，聚类分析偏差模式，关联蛋白功能注释和互作伙伴类型
- **验证方式**：在独立数据集（如 CAID benchmark）上验证偏差模式的泛化性
- **可能的失败模式**：偏差模式过于异质，难以形成统一解释
- **创新状态**：unverified

### 候选 3：利用 DisProt 实验条件元数据改进 MD 模拟的 IDP 构象采样
- **名称**：MD-DisProt：基于 MIABLE 元数据的 IDP 模拟条件优化
- **来源局限/观察**：MIABLE 记录了实验条件（pH、温度、buffer），但未用于指导模拟
- **核心假设**：在 MIABLE 记录的实验条件下进行 MD 模拟，能更好地重现实验观测的 disorder 状态
- **相对本文的增量**：本文仅记录条件；本候选将条件转化为模拟参数
- **初步方法**：从 DisProt 提取 MIABLE 字段，映射为 MD 模拟参数（离子强度、pH 对应的质子化状态），对代表性 IDP 进行增强采样模拟
- **验证方式**：模拟生成的构象系综与实验观测（如 SAXS、NMR 化学位移）对比
- **可能的失败模式**：MIABLE 字段覆盖不全；实验条件与模拟条件的映射不精确
- **创新状态**：unverified

### 候选 4：基于 DisProt 的 IDP 相分离功能注释扩展
- **名称**：DisProt-LLPS：从现有注释推断 IDP 的相分离倾向
- **来源局限/观察**：DisProt 功能注释包含"localization"等 GO 术语，但未显式标注相分离相关功能
- **核心假设**：DisProt 中部分功能注释（如"localization"、"protein binding"）与相分离倾向相关
- **相对本文的增量**：本文未涉及相分离；本候选将现有注释映射到相分离功能空间
- **初步方法**：利用 DisProt 注释 + 序列特征（如 R/Y 比例、电荷模式）训练相分离倾向预测器，与已知 LLPS 数据库（如 PhaSepDB）对比
- **验证方式**：在 PhaSepDB 和 LLPS 实验文献上验证
- **可能的失败模式**：注释与相分离的关联过于间接；训练数据不足
- **创新状态**：unverified

### 候选 5：DisProt 注释驱动的 IDP 互作 motif 发现
- **名称**：IDP-MotifMiner：从 DisProt 功能注释中挖掘互作相关序列模式
- **来源局限/观察**：DisProt 注释了大量具有 binding 功能的 IDR，但未系统提取其中的互作 motif
- **核心假设**：DisProt 中注释为"molecular recognition display site"的区域富含可泛化的互作 motif
- **相对本文的增量**：本文提供注释；本候选从注释中提取可迁移的序列模式
- **初步方法**：从 DisProt 提取 IDPO 注释为 recognition display site 的区域，进行 motif 富集分析，与 ELM 数据库对比
- **验证方式**：在 ELM 和 3D 结构数据库（如 PDB 中的 folding-upon-binding 复合物）上验证 motif 的互作能力
- **可能的失败模式**：motif 过于简并；注释区域长度不均一
- **创新状态**：unverified