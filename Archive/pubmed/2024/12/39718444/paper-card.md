## 01 基本信息
- **标题**: Searching and Using MobiDB Resource 6 to Explore Predictions and Annotations for Intrinsically Disordered Proteins
- **作者**: Aspromonte, Maria Cristina; Quaglia, Federica; Monzon, Alexander Miguel; Clemente, Damiano; Del Conte, Alessio; Piovesan, Damiano; Tosatto, Silvio C E
- **单位**: 未提供（根据致谢推测为 Università degli Studi di Padova 等）
- **期刊/平台**: Current Protocols
- **年份**: 2024
- **论文类型**: 方法学协议（Protocol）/ 数据库使用指南
- **领域**: 生物信息学、无序蛋白数据库
- **关键词**: intrinsically disordered proteins (IDPs), intrinsically disordered regions (IDRs), MobiDB, disorder prediction, AlphaFoldDB, homology transfer, REST API
- **DOI/arXiv 号**: 10.1002/cpz1.70077
- **代码**: 未提供（MobiDB 数据库本身为公开资源，https://mobidb.org/）
- **数据**: MobiDB 数据库（https://mobidb.org/），公开可用
- **阅读日期**: 2026-05-13
- **在课题方向中的位置**: 本文是 IDP/IDR 领域核心数据库 MobiDB 的 v6 版本使用协议，属于「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的**数据基础设施层**。MobiDB 整合了实验注释、预测结果（含 AlphaFoldDB）和同源转移注释，为 IDP/IDR 相关的 AI 模型训练、验证和生物学解释提供标准化的数据来源。本文不直接提出新算法，而是提供访问和解释这些数据的标准化流程，是该方向研究者必备的工具文献。

## 02 一句话总结
本文提供了一套标准化的操作协议，指导用户通过网页界面和 REST API 使用 MobiDB v6 数据库，该数据库整合了实验证据、AlphaFoldDB 预测和同源转移注释，用于查询和解释蛋白质无序区（IDR）的预测与注释信息。

## 03 研究问题
- **具体问题**: 如何有效地查询、可视化和解释 MobiDB v6 中关于 IDP/IDR 的预测与注释数据？
- **为什么重要**: IDP/IDR 约占真核蛋白质组的 30%，与神经退行性疾病、癌症和生物分子凝聚体形成密切相关。研究者需要一个可靠、全面且易于访问的数据库来获取无序注释，以支持功能研究和疾病机制探索。
- **现有方法为何不足**: 尽管 MobiDB 已存在多年，但 v6 版本引入了重大更新（AlphaFoldDB 整合、同源转移管道、界面重构），用户需要更新的指南来充分利用这些新功能。此外，不同数据来源（实验、预测、同源）的注释质量差异大，需要明确的解释框架。
- **精确的「Can ... ?」研究问题**: Can researchers efficiently retrieve and correctly interpret high-quality IDP/IDR annotations (including disorder, binding, and function) from MobiDB v6 using both web interface and REST API?

## 04 背景与发展脉络
*注：以下脉络基于本文框架及作者引用的文献，部分经外部核验。*

1. **早期阶段（~2010s 初）**: IDP 概念确立，认识到约 30% 真核蛋白含无序区。早期数据库如 DisProt 开始收集实验验证的无序注释，但覆盖度有限。
2. **MobiDB 诞生与发展（2012-2022）**: MobiDB 作为综合资源出现，整合 DisProt、PDB 等实验数据和多个预测器结果。v1-v5 逐步扩展覆盖范围，引入 consensus 预测（MobiDB-lite），并开始整合功能注释（GO、IDPO）。
3. **AlphaFold 时代（2021-至今）**: AlphaFold2 的发布改变了结构预测格局。CAID 评估显示 AlphaFold 的 pLDDT 分数与实验无序数据高度相关，使其成为无序预测的有力工具。
4. **MobiDB v6（2024）**: 本文所述版本，关键创新包括：(a) 整合 AlphaFoldDB 预测填补实验结构缺失的注释空白；(b) 新的同源转移管道，基于序列相似性和蛋白嵌入传播功能注释；(c) 界面重构，提供更直观的注释概览。
5. **本文位置**: 处于第 4 阶段，作为 v6 版本的操作指南，帮助领域内研究者（包括计算和实验科学家）有效利用这一更新后的资源。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 数据来源多样、注释质量参差 | 用户难以区分实验验证与预测的注释 | 不同来源（实验、预测、同源转移）的可靠性不同，需要标准化标注 | 文中将注释分为 Gold（人工 curated）和 Silver（衍生/预测）两个置信级别（Basic Protocol 2, Fig. 4） |
| 实验结构数据缺失 | 许多蛋白缺乏 PDB 结构，无法直接判断无序区 | 实验结构解析耗时费力，覆盖不全 | 作者指出整合 AlphaFoldDB 预测是为了「filling disorder-annotation gaps for those sequences for which experimental coordinates are lacking」（Guidelines for Understanding Results） |
| 功能注释覆盖不足 | 已知无序蛋白的功能信息分散且不完整 | 功能注释（GO、IDPO）需要人工 curation，难以大规模扩展 | 作者描述通过同源转移和蛋白嵌入传播功能注释以「expand MobiDB's coverage of functional predictions」（Background Information） |
| 界面复杂、学习曲线陡峭 | 新用户难以快速定位所需信息 | 数据库功能丰富但入口分散 | 本文专门提供 4 个 Basic Protocol 和 1 个 Support Protocol 来引导用户（Abstract） |
| 程序化访问门槛 | 批量查询和自动化分析需要编程能力 | 网页界面不适合大规模数据处理 | 作者提供 REST API 的详细端点说明（Support Protocol） |

## 06 核心思想

### 1) 表面方法
提供一套分步操作协议，涵盖：(a) 网页搜索（Basic Protocol 1-3），包括文本查询、数据集浏览和统计页面使用；(b) 程序化访问（Support Protocol），通过 REST API 进行批量查询；(c) 结果解读（Basic Protocol 4），以 GHR 为例展示如何可视化和解释注释。

### 2) 核心洞察
MobiDB v6 的核心设计理念是**多源证据整合与置信度分层**。通过将注释分为 Gold（人工 curated + 同源）和 Silver（PDB 衍生 + AlphaFold 预测）两个层级，用户可以根据研究需求选择合适的证据强度。特别重要的是，AlphaFoldDB 的 pLDDT 分数被用作无序预测的有效代理，这弥合了「结构预测」与「无序注释」之间的鸿沟。同源转移管道则利用序列相似性和蛋白嵌入（embedding）来传播功能注释，显著扩展了注释覆盖范围。

### 3) 可能的普适教训 [Analysis]
- **数据库设计应显式标注证据来源和置信度**：对于 IDP/IDR 研究，不同来源的注释可靠性差异巨大，分层设计（Gold/Silver）是良好的实践范例。
- **AlphaFold pLDDT 可作为无序预测的通用特征**：这一洞察对 IDP×AI 方向有直接启示——pLDDT 分数可作为训练无序预测模型或筛选候选 IDR 的廉价特征。
- **同源转移 + 蛋白嵌入是扩展注释覆盖的高效策略**：在实验数据稀疏的场景下，利用序列相似性和 embedding 传播注释是通用方法论，可迁移到其他功能注释任务。

## 07 方法总览

- **输入**: 用户查询（UniProt accession、蛋白名称、基因符号、物种名称或 NCBI taxonomy ID）；或通过 REST API 提交的批量 accession 列表
- **输出**: 蛋白的无序注释概览，包括：序列特征可视化（Feature viewer）、AlphaFold 结构视图、无序/结合/功能注释（按 Gold/Silver 分层）、亚细胞定位和交叉引用
- **核心模块**:
  1. **搜索模块**: 支持多种查询格式的文本搜索（Basic Protocol 1）
  2. **数据集浏览模块**: 按置信度（Gold/Silver）和物种浏览预选数据集（Basic Protocol 2）
  3. **统计模块**: 按证据类型、特征、来源查询数据库统计信息（Basic Protocol 3）
  4. **REST API 模块**: 程序化访问端点（download_page, count, statistics）（Support Protocol）
  5. **可视化模块**: 条目页面展示，含 Feature viewer、AlphaFold 结构、注释分层视图（Basic Protocol 4）
- **训练**: 不适用（本文为数据库使用协议，非模型训练）
- **工具**: MobiDB-lite（consensus 预测器）、FLIPPER（LIP 预测）、RING（残基相互作用网络）、AlphaFoldDB
- **反馈回路**: 不适用
- **假设**: 用户具备基本的分子生物学知识；对 REST API 用户，假设具备基础的编程能力

**文字流程**:
1. 用户通过网页搜索框输入查询（accession/名称/基因符号等）→ 2. 系统返回匹配的蛋白条目 → 3. 条目页面展示综合注释视图（序列特征、AlphaFold 结构、无序/结合/功能注释）→ 4. 用户可通过「Selected datasets」或「Statistics」页面进一步筛选特定置信度或物种的数据 → 5. 对于批量或自动化需求，用户可通过 REST API 调用 download_page/count/statistics 端点获取结构化数据

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 搜索模块（Basic Protocol 1） | 支持多种查询格式的文本搜索 | 用户可能持有不同类型的标识符（accession、名称、基因符号） | 输入：查询字符串；输出：匹配蛋白列表 | Fig. 1 展示搜索界面 | 预期影响：降低可用性，用户需手动转换标识符格式 [Analysis] |
| 数据集浏览模块（Basic Protocol 2） | 按 Gold/Silver 置信度浏览预选数据集 | 用户需要快速访问高质量注释或全量预测数据 | 输入：数据集选择（Gold/Silver）；输出：数据集详情（蛋白数、注释残基百分比） | Fig. 4 展示 Gold/Silver 数据集 | 预期影响：用户难以快速筛选合适置信度的数据 [Analysis] |
| 统计模块（Basic Protocol 3） | 查询数据库整体统计信息 | 用户需要了解特定物种或证据类型的覆盖情况 | 输入：证据类型/特征/物种筛选；输出：统计表格 | Basic Protocol 3 描述 | 预期影响：用户无法评估数据覆盖度，影响研究设计 [Analysis] |
| REST API 模块（Support Protocol） | 程序化访问数据库 | 批量查询和自动化分析需要编程接口 | 输入：HTTP 请求（含参数）；输出：JSON/结构化数据 | Support Protocol 提供端点说明 | 预期影响：无法进行大规模筛选或集成到分析管道 [Analysis] |
| 可视化模块（Basic Protocol 4） | 展示蛋白条目的综合注释视图 | 用户需要直观理解无序/结合/功能注释的空间分布 | 输入：蛋白条目选择；输出：Feature viewer、AlphaFold 结构、注释分层视图 | Fig. 8 展示条目页面结构 | 预期影响：用户难以直观解读注释的空间关系 [Analysis] |

*注：由于本文为协议类文献，未提供消融实验数据。上述「移除后的影响」均为基于模块功能的预期推断，标注为 [Analysis]。*

## 09 关键公式符号

**不适用**。本文为数据库使用协议，不涉及数学模型或算法公式。相关的方法学概念包括：
- **pLDDT**（predicted Local Distance Difference Test）：AlphaFold 输出的每个残基的预测置信度分数，范围 0-100，低 pLDDT 与无序区高度相关（文中引用 CAID 评估结果）
- **Gold/Silver 注释分层**：基于证据来源的置信度分类体系

## 10 实验设计与证据链

**数据集/群体**: 本文为协议类文献，无传统实验设计。使用的示例数据为：
- 人类生长激素受体（GHR, UniProt: P10912）作为案例研究

**指标**: 不适用（无定量评估指标）

**基线**: 不适用

**预算**: 不适用

**评测协议**: 不适用

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|-------------------|------|
| GHR 案例展示（Basic Protocol 4） | MobiDB v6 条目页面能综合展示无序/结合/功能注释 | 使用 GHR 作为示例蛋白 | 展示了 Feature viewer、AlphaFold 结构、注释分层视图 | 条目页面设计支持直观的注释解读 | 未证明该设计优于其他数据库的展示方式 | Basic Protocol 4, Fig. 8 |
| AlphaFoldDB 整合说明 | AlphaFold 预测可填补实验结构缺失的注释空白 | 引用 CAID 评估结果 | 声称 AlphaFold pLDDT 与实验无序数据高度相关 | AlphaFold 预测是有效的无序注释来源 | 未提供具体相关性数值 | Background Information |
| 同源转移管道说明 | 同源转移可扩展功能注释覆盖 | 描述管道设计（序列相似性 + 蛋白嵌入） | 声称显著增加高质量注释条目数 | 同源转移是有效的注释扩展策略 | 未提供具体扩展数量 | Background Information |

## 11 结论正确解读

- **任务范围**: 本文结论仅限于「如何使用 MobiDB v6 数据库」，不涉及任何生物学发现或算法性能声明。
- **oracle/真值输入**: 数据库中的 Gold 注释来源于人工 curated 数据库（如 DisProt），Silver 注释来源于 PDB 衍生和 AlphaFold 预测。用户应理解 Gold 注释的可靠性高于 Silver。
- **端到端状态**: 本文是完整可用的操作指南，所有协议步骤均可在公开网站上执行。
- **算力成本**: 网页界面无需本地计算资源；REST API 调用需要网络连接，但计算在服务器端完成。
- **历史数据依赖**: 数据库内容随版本更新而变化，v6 于 2024 年 7 月发布，包含截至该时间点的注释数据。
- **模型依赖**: AlphaFoldDB 预测基于 AlphaFold2 模型；MobiDB-lite 为 consensus 预测器，整合多个无序预测算法。
- **最难情形**: 对于缺乏实验数据且无同源蛋白的非模式物种蛋白，注释可能仅依赖预测，可靠性较低。
- **群体/领域边界**: 本文适用于所有研究 IDP/IDR 的科研人员，包括计算生物学家、实验生物学家和临床研究者。不适用于非蛋白序列的注释查询。
- **有边界的复述**: 本文提供了一套经过验证的操作流程，使研究者能够通过网页或 API 从 MobiDB v6 获取分层（Gold/Silver）的 IDP/IDR 注释数据，包括无序预测、结合位点、功能注释和 AlphaFold 结构信息，但本文不评估这些注释的生物学准确性。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据库覆盖依赖外部数据源 | 注释质量受限于 DisProt、PDB 等上游数据库的 curation 进度 | 未明确提及（隐含：持续更新和扩展 curation） | Background Information |
| AlphaFold 预测的适用性 | AlphaFold pLDDT 与实验无序数据相关，但并非所有场景均适用 | 未明确提及 | Background Information |
| 同源转移的准确性 | 基于序列相似性和 embedding 的注释传播可能引入错误 | 未明确提及 | Background Information |

*注：本文为协议类文献，作者未系统性地列出局限性。上述内容为文中隐含提及的约束条件，非正式局限声明。*

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| Gold/Silver 分层可能过度简化证据质量 | 同源转移的 Gold 注释（curated + homologs）与直接实验验证的 Gold 注释可靠性不同，但被归为同一层级 | 用户可能高估同源转移注释的可靠性 | 比较同源转移注释与直接实验注释在独立测试集上的一致性 | Basic Protocol 2 描述 Gold 包含「manually curated annotations and their homologs」 |
| AlphaFold pLDDT 作为无序预测的代理存在边界 | pLDDT 低可能反映结构域间灵活性而非完全无序；pLDDT 高也可能存在隐蔽无序 | 影响依赖 AlphaFold 预测进行无序判断的研究结论 | 在已知无序/有序的基准集上系统评估 pLDDT 阈值 | Background Information 引用 CAID 评估 |
| 协议未提供批量查询的最佳实践 | REST API 的速率限制、错误处理、大数据量下载策略未详细说明 | 影响需要大规模筛选的研究效率 | 测试 API 在不同请求频率和批量大小下的表现 | Support Protocol 仅提供端点描述 |
| 数据库更新频率和版本管理策略不明确 | 用户可能基于旧版本数据进行分析，影响可重复性 | 科学可重复性要求明确的数据版本引用 | 检查 MobiDB 是否提供版本快照或 DOI 引用机制 | 文中未提及版本管理细节 |
| 案例研究仅使用 GHR 一个蛋白 | 单一案例可能无法覆盖所有功能场景（如多结构域蛋白、膜蛋白等） | 影响协议对不同类型蛋白的适用性评估 | 使用多个不同特征的蛋白测试协议步骤 | Basic Protocol 4 仅展示 GHR |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **多源证据整合与置信度分层设计**：MobiDB 将注释分为 Gold（人工 curated + 同源）和 Silver（PDB 衍生 + AlphaFold 预测）两层。**可迁移性**：在 IDP/IDR×AI 研究中，训练数据应显式标注证据来源和置信度，避免混合不同质量的数据导致模型偏差。

2. **AlphaFold pLDDT 作为无序预测的廉价特征**：MobiDB v6 整合 AlphaFoldDB 预测，利用 pLDDT 与实验无序数据的高相关性填补注释空白。**可迁移性**：在缺乏实验无序数据的蛋白上，pLDDT 分数可作为特征或标签用于训练轻量级无序预测器，或作为多模态模型的输入特征。

3. **同源转移 + 蛋白嵌入的注释传播策略**：MobiDB 通过序列相似性和蛋白 embedding 将 curated 功能注释传播到同源蛋白。**可迁移性**：在 IDP/IDR 功能注释稀疏的场景下，可利用预训练蛋白语言模型的 embedding 进行标签传播，扩展训练集覆盖。

4. **REST API 设计模式**：MobiDB 提供 download_page/count/statistics 三类端点，分别支持数据检索、计数查询和统计信息获取。**可迁移性**：构建 IDP/IDR 相关数据库或工具时，应提供程序化访问接口，支持批量查询和统计汇总，便于集成到自动化分析管道。

5. **可视化设计原则**：条目页面将序列特征、结构视图和功能注释整合在同一界面，支持分层查看。**可迁移性**：在 IDP/IDR 预测工具中，应提供直观的序列-结构-功能联合可视化，帮助用户理解无序区与功能位点的空间关系。

6. **与相分离研究的连接**：MobiDB 注释包含 LIP（线性互作肽段）和结合模式（DD/DO），这些信息与相分离凝聚体中的多价互作直接相关。**可迁移性**：在相分离研究中，可利用 MobiDB 的 LIP 和结合模式注释筛选候选的相分离驱动区域（IDR 中的重复互作基序）。

## 15 与已有知识连接

- **DisProt 数据库**（本文引用）：MobiDB 的核心数据来源之一，提供人工 curated 的无序注释。MobiDB 将其作为 Gold 注释的基础。
- **AlphaFoldDB / AlphaFold2**（Jumper et al., 2021，本文引用）：MobiDB v6 整合其预测结果，pLDDT 分数作为无序预测的代理。
- **CAID 评估**（Del Conte et al., 2023，本文引用）：无序预测方法的社区评估，验证了 AlphaFold pLDDT 与实验无序数据的相关性。
- **MobiDB-lite**（Necci et al., 2017, 2021，本文引用）：MobiDB 的 consensus 预测器，整合多个无序预测算法。
- **FLIPPER**（Monzon et al., 2021，本文引用）：用于预测和表征 LIP 的软件，集成于 MobiDB 管道。
- **RING**（Del Conte et al., 2024，本文引用）：残基相互作用网络生成器，用于分析蛋白结构中的非共价相互作用。
- **IDP/IDR 与相分离**（Martin et al., 2020，本文引用）：IDP/IDR 在液-液相分离中的关键作用，MobiDB 的注释数据可支持相分离相关研究。
- **IDP Central Consortium / ELIXIR IDP Community**（Davey et al., 2019，本文引用）：MobiDB 所属的社区基础设施，提供 IDP 相关资源和标准。

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**: IDR-PLM-Bench：基于 MobiDB 注释的无序区蛋白语言模型基准测试
   - **来源局限/观察**: MobiDB v6 提供了大规模、分层置信度的无序注释，但缺乏系统性的基准测试框架来评估蛋白语言模型（如 ESM-2, ProtTrans）在无序预测任务上的表现。
   - **核心假设**: 在 MobiDB Gold 注释上微调的蛋白语言模型可超越传统无序预测器（如 IUPred, ESpritz），尤其在缺乏同源信息的蛋白上。
   - **初步方法**: 构建基于 MobiDB Gold/Silver 注释的训练/验证/测试集；评估多种 PLM 的零样本和微调性能；与现有无序预测器对比。
   - **验证方式**: 在 CAID 基准上独立评估；分析不同物种、不同无序类型（全长无序 vs 部分无序）的亚组性能。
   - **创新状态**: partially checked（PLM 用于无序预测已有先例，但基于 MobiDB v6 的系统性基准尚缺）

2. **候选名称**: MobiDB-Phase：从无序注释到相分离驱动区域的预测管道
   - **来源局限/观察**: MobiDB 提供 LIP 和结合模式（DD/DO）注释，但未直接提供相分离相关注释。相分离驱动区域通常富含重复互作基序和多价相互作用。
   - **核心假设**: 从 MobiDB 的 LIP 注释和结合模式可提取特征，训练分类器预测相分离驱动区域。
   - **初步方法**: 从 MobiDB 提取 LIP 密度、DD/DO 结合模式分布、序列组成等特征；使用已知相分离蛋白（如 FUS, TDP-43）作为正例；训练梯度提升或深度学习分类器。
   - **验证方式**: 在独立相分离数据库（如 PhaSepDB, LLPSDB）上验证；与现有相分离预测器（如 catGRANULE, PLAAC）对比。
   - **创新状态**: unverified

3. **候选名称**: AlphaFold-pLDDT-Phase：利用结构预测置信度图谱识别相分离区域
   - **来源局限/观察**: MobiDB v6 整合 AlphaFoldDB 预测，pLDDT 低分区域与无序区高度相关。相分离驱动区域通常包含多个低 pLDDT 的互作基序。
   - **核心假设**: pLDDT 图谱的空间分布模式（而非简单的低分阈值）可区分相分离驱动区域和普通无序区。
   - **初步方法**: 从 AlphaFoldDB 获取蛋白的 pLDDT 图谱；提取低分区域的长度分布、间距、周期性等特征；结合序列组成特征训练分类器。
   - **验证方式**: 在已知相分离蛋白上评估；与基于序列的方法对比；分析预测区域是否富集已知的相分离相关基序（如 RGG, FG 重复）。
   - **创新状态**: unverified

4. **候选名称**: MobiDB-Embedding-Transfer：基于蛋白 embedding 的无序功能注释迁移学习
   - **来源局限/观察**: MobiDB v6 的同源转移管道基于序列相似性，但未利用现代蛋白 embedding 的语义信息。蛋白语言模型的 embedding 可捕获远同源的功能相似性。
   - **核心假设**: 基于蛋白 embedding 的标签传播可超越传统序列相似性方法，将功能注释（如 GO, IDPO）更准确地传播到远同源蛋白。
   - **初步方法**: 使用 ESM-2 等模型提取蛋白 embedding；在 embedding 空间中构建相似性图；用标签传播算法（如 Label Spreading）传播 MobiDB 中的功能注释；与现有同源转移管道对比。
   - **验证方式**: 在保留的 curated 注释上评估传播准确性；分析传播注释的置信度分布。
   - **创新状态**: unverified

5. **候选名称**: IDR-Binding-Mode-Predictor：基于 MobiDB 注释的 IDR 结合模式预测
   - **来源局限/观察**: MobiDB 提供 DD（disorder-to-disorder）和 DO（disorder-to-order）结合模式注释，这些模式与 IDR 介导的蛋白互作机制直接相关，但缺乏专门的预测工具。
   - **核心假设**: 从序列特征（组成、疏水性、电荷分布）和预测结构特征（pLDDT 图谱）可预测 IDR 的结合模式（DD vs DO）。
   - **初步方法**: 从 MobiDB 提取带 DD/DO 注释的 IDR 区域；提取序列和结构特征；训练二分类器；分析不同结合模式的特征重要性。
   - **验证方式**: 交叉验证性能；在独立实验数据上验证；分析预测的 DD 区域是否富集于相分离相关蛋白。
   - **创新状态**: unverified