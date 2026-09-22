## 01 基本信息

- **标题**：MobiDB: 10 years of intrinsically disordered proteins
- **作者**：Piovesan, Damiano; Del Conte, Alessio; Clementel, Damiano; Monzon, Alexander Miguel; Bevilacqua, Martina; Aspromonte, Maria Cristina; Iserte, Javier A; Orti, Fernando E; Marino-Buslje, Cristina; Tosatto, Silvio C E
- **单位**：未提供（根据作者信息推测为意大利帕多瓦大学等，但原文未明确列出）
- **期刊/预印本平台**：Nucleic Acids Research
- **年份**：2022
- **论文类型**：数据库资源综述/更新报告（Database Resource）
- **领域**：生物信息学、蛋白质科学、 intrinsically disordered proteins (IDPs/IDRs)
- **关键词**：intrinsically disordered proteins, database, annotation, AlphaFold, homology transfer, binding modes, liquid-liquid phase separation
- **DOI/arXiv 号**：10.1093/nar/gkac1065
- **代码**：AlphaFold-disorder 脚本：https://github.com/BioComputingUP/AlphaFold-disorder
- **数据**：https://mobidb.org/
- **阅读日期**：未提供
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**：MobiDB 是该方向的核心基础设施型数据库，聚合实验、文献、预测等多源无序蛋白注释，并整合 AlphaFold2 预测结果用于无序区识别和线性互作肽（LIP）推断。本文是数据库更新报告，本身不提出新 AI 模型，但为 IDP/IDR 互作、相分离相关研究提供标准化数据资源和可迁移的注释流程。

## 02 一句话总结

MobiDB 数据库通过"注释金字塔"框架聚合实验、文献、同源转移和预测等多层级证据，并新整合 AlphaFold2 pLDDT/RSA 衍生特征和同源转移流水线，将人工精选的无序/互作注释覆盖范围扩大两个数量级，同时提供结合模式（binding modes）和相分离相关注释。

## 03 研究问题

- **具体问题**：如何构建一个全面、标准化、可持续更新的 intrinsically disordered proteins (IDPs/IDRs) 知识库，整合多源异构数据（实验、文献、预测），并为用户提供功能相关的注释（如结合位点、结合模式、相分离）？
- **为什么重要**：IDPs/IDRs 在信号转导、转录调控、病毒劫持等过程中发挥核心作用，且与蛋白-蛋白互作和液-液相分离（LLPS）密切相关。但实验表征困难，数据分散在不同专门资源中，缺乏统一标准，阻碍了系统研究和计算建模。
- **现有方法不足**：已有数据库（如 DisProt、PDB 缺失残基）覆盖有限、更新滞后、缺乏功能注释维度；预测工具各自独立，缺乏统一整合和共识标注；缺乏从实验注释到全蛋白质组覆盖的扩展机制。
- **精确研究问题（Can...?）**：Can a multi-source annotation pyramid with homology transfer and AlphaFold-derived features expand high-quality disorder and binding annotations to the entire UniProtKB while maintaining precision?

## 04 背景与发展脉络

> 注：以下脉络基于本文框架，标注为「仅本文框架」，未经外部系统核验。

1. **早期阶段（~2012）**：MobiDB 首次发布，引入"注释金字塔"概念，将手动精选数据库（DisProt）、PDB 缺失残基和预测工具（ESpritz、IUPred）分层整合，覆盖 Swiss-Prot 约 50 万蛋白。
2. **扩展阶段（2014）**：MobiDB 2.0 扩展到整个 UniProtKB（约 8000 万序列），提供 RESTful API，实现 Web 2.0 功能。
3. **功能维度引入（2018）**：MobiDB 3.0 引入"线性互作肽"（LIP）概念，整合 PDB 复合物中互作信息（RING 软件），将功能维度加入注释金字塔；同年开发 MobiDB-lite 包封装序列预测器，并集成到 InterProScan。
4. **成熟阶段（2021-2022，本文）**：MobiDB 4.0 引入结合模式（binding modes）分类，整合 FuzDB 模糊复合物注释；2022 版（本文）整合 AlphaFold2 预测结构，开发 pLDDT/RSA 双定义无序注释和 LIP 推断流程；重新实现同源转移流水线，将精选注释扩展两个数量级；整合 PhaSePro 和 PhaSepDB 相分离数据库。

**本文主张的位置**：MobiDB 已从单纯的无序注释聚合器演变为包含结构预测、功能注释（结合模式、相分离）和标准化词汇表的综合性 IDP 知识库，是该领域的参考资源。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 数据分散 | IDP 相关数据散落在 DisProt、PDB、UniProtKB 等多个资源，缺乏统一入口 | 不同资源聚焦不同方面（实验验证、结构、序列），缺乏整合框架 | Introduction 第 2 段："Available data is scattered across different specialized resources" |
| 实验表征困难 | IDP 难以通过传统结构生物学方法表征，实验数据稀少 | IDP 表达、纯化、结晶困难，构象动态异质 | Introduction 第 1 段："difficulties in IDP expression, purification and structural characterization hamper experimental characterization" |
| 覆盖不足 | 手动精选注释仅覆盖少量蛋白，无法扩展到全蛋白质组 | 人工精选成本高、速度慢 | Homology transfer 节：同源转移将精选注释扩展"两个数量级" |
| 功能注释缺失 | 传统无序注释只标注"无序/有序"，缺乏结合位点、结合模式等功能维度 | IDP 功能多样（互作、相分离、修饰位点），单一注释维度不足 | Introduction 第 3 段：2018 年引入 LIP 概念，"adding the function dimension to the annotation pyramid" |
| 预测结果不一致 | 不同预测工具输出差异大，用户难以判断可信度 | 各工具基于不同原理（物理化学性质、进化信息、深度学习），无统一标准 | 注释金字塔设计：分层证据、共识注释（Table 1） |
| 同源转移假阳性风险 | 盲目同源转移可能产生错误注释 | 序列相似性不等于功能/无序特征保守 | Homology transfer 节：严格过滤条件（90% 覆盖、80% 同一性、20% gap 限制） |

## 06 核心思想

### 1) 表面方法

MobiDB 是一个聚合型数据库，通过"注释金字塔"（annotation pyramid）将四层证据整合：① 手动精选实验注释（DisProt、PDB 等）；② 从 PDB 结构衍生的注释（缺失残基、温度系数等）；③ 同源转移注释（基于序列相似性从精选注释推断）；④ 序列预测注释（MobiDB-lite 封装的多种预测器）。新版本增加 AlphaFold2 衍生注释和结合模式分类。

### 2) 核心洞察

**洞察一：证据分层而非单一来源。** 不同来源的注释具有不同可信度，金字塔模型让用户根据需求选择证据层级，同时通过共识规则组合互补信息。

**洞察二：AlphaFold2 的"失败模式"即无序信号。** AlphaFold2 对无序区域给出低 pLDDT 分数，这并非缺陷而是可用的无序预测特征。结合 pLDDT 和相对溶剂可及性（RSA）可识别"条件折叠"区域——即那些在结合时可能折叠的无序区，这直接关联到 IDP 互作机制。

**洞察三：同源转移的"精确扩展"策略。** 通过极严格的序列相似性阈值（90% 覆盖、80% 同一性），将人工精选注释安全地扩展到全蛋白质组，实现"质"与"量"的平衡。

**洞察四：功能注释是 IDP 数据库的核心价值。** 仅标注"无序"不够，需要标注无序区的功能角色（结合、相分离、修饰），这通过 LIP、结合模式和相分离数据库整合实现。

### 3) 可能的普适教训 [Analysis]

- **对 IDP/IDR 互作研究**：AlphaFold2 低置信度区域 + 高溶剂可及性的组合可作为"条件折叠/结合位点"的候选特征，这一思路可迁移到其他蛋白互作预测任务。
- **对 AI 方法开发**：多源证据分层整合（实验 > 同源 > 预测）是处理生物数据噪声的有效策略，可作为训练集构建和标签融合的参考框架。
- **对相分离研究**：将 PhaSePro/PhaSepDB 的相分离驱动区域注释与无序注释整合，为相分离序列特征分析提供数据基础。

## 07 方法总览

- **输入**：UniProtKB 全部蛋白序列（约 2.5 亿条）；DisProt、PDB、FuzDB、PhaSePro、PhaSepDB 等外部数据库注释；AlphaFoldDB 结构预测（1,121,068 个 Swiss-Prot 和模式生物蛋白）。
- **输出**：每个蛋白的多层级无序注释、LIP/结合模式注释、相分离相关注释，通过网页和 RESTful API 提供访问。
- **模块**：
  1. **注释金字塔**：四层证据（精选/衍生/同源/预测）的分层整合与共识计算
  2. **同源转移流水线**：BLAST 搜索 → 严格过滤（90% 覆盖、80% 同一性、20% gap）→ 贪心去重叠
  3. **AlphaFold 处理模块**：pLDDT < 70% 定义为无序；RSA 滑动窗口（25 残基，阈值 0.58）定义第二类无序；两者组合推断条件折叠和 LIP
  4. **MobiDB-lite**：封装多种序列预测器的集成包，集成到 InterProScan
  5. **受控词汇表（CV）**：evidence/feature/source 三命名空间，标准化注释描述
  6. **数据存储**：gold collection（精选+衍生+同源+AlphaFold，约 150 万蛋白）与预测 collection 分离
- **训练**：不适用（数据库项目，无模型训练）
- **反馈回路**：外部数据库更新触发 gold collection 重新生成；用户通过 API 和网站访问数据
- **假设**：① 序列相似性可传递无序/功能注释（同源转移）；② AlphaFold2 低 pLDDT 与实验无序高度相关；③ 高 RSA 的无序区域可能参与条件折叠/结合

**文字流程**：从 UniProtKB 获取全部蛋白序列 → 对每个蛋白执行 MobiDB-lite 预测 → 对 gold collection 蛋白执行 BLAST 同源搜索 → 匹配精选注释并过滤 → 从 AlphaFoldDB 下载结构 → 计算 pLDDT/RSA 衍生注释 → 整合所有来源到统一 schema → 通过网站/API 发布。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 注释金字塔 | 分层整合多源无序注释，提供共识视图 | 不同来源注释可信度不同，需要统一框架 | 输入：各来源注释；输出：分层+共识注释 | Figure 1、Table 1 | 预期影响：用户无法判断注释可信度，数据使用困难 |
| 同源转移流水线 | 将精选注释扩展到同源蛋白 | 人工注释覆盖有限，需要自动化扩展 | 输入：精选注释+UniProtKB 序列；输出：同源转移注释 | "expands manually curated annotations by two orders of magnitude" | 预期影响：高质量注释覆盖大幅缩减，回到仅数千蛋白 |
| AlphaFold 处理 | 从 pLDDT/RSA 提取无序和 LIP 注释 | AlphaFold2 预测覆盖广，可补充实验数据 | 输入：AlphaFoldDB 结构；输出：pLDDT 无序、RSA 无序、条件折叠 LIP | Figure 2（Paxillin 例）、CAID 评估引用 | 预期影响：失去结构层面的无序证据，条件折叠注释缺失 |
| MobiDB-lite | 封装多种序列预测器，提供统一预测接口 | 不同预测器各有优劣，需要集成和标准化 | 输入：蛋白序列；输出：共识预测 | 集成到 InterProScan | 预期影响：预测层注释消失，仅剩实验/同源注释 |
| 受控词汇表（CV） | 标准化注释术语 | 多源数据术语不统一，影响机器可读性 | 输入：注释类型；输出：标准 CV 三元组 | "available in a controlled vocabulary" | 预期影响：注释描述混乱，难以自动化处理 |
| 结合模式分类 | 区分不同 IDP 互作模式（折叠结合、模糊复合物等） | IDP 互作机制多样，需要功能分类 | 输入：LIP 注释+结构信息；输出：结合模式标签 | Table 3、FuzDB 整合 | 预期影响：失去 IDP 互作功能维度，仅剩位置注释 |
| 相分离数据库整合 | 提供 LLPS 驱动区域注释 | 相分离是 IDP 核心功能之一 | 输入：PhaSePro/PhaSepDB 注释；输出：LLPS 注释 | "integrates two databases of LLPS protein drivers" | 预期影响：相分离相关查询无法支持 |

## 09 关键公式符号

不适用。本文为数据库资源报告，未提出新的数学模型或算法公式。核心"规则"为同源转移的过滤条件（阈值），以文字描述而非公式形式给出：

- 同源转移过滤条件：比对片段覆盖查询注释区域 ≥ 90%；序列同一性 ≥ 80%；gap 比例 ≤ 20%
- AlphaFold 无序定义：pLDDT < 70（阈值）
- AlphaFold RSA 无序定义：平均 RSA > 0.58（25 残基滑动窗口）

## 10 实验设计与证据链

### 数据集/群体/规模/指标

- **数据规模**：UniProtKB 全部序列（约 2.5 亿）；gold collection 约 150 万蛋白；AlphaFoldDB 处理 1,121,068 个 Swiss-Prot 和模式生物蛋白
- **外部数据源**：DisProt、PDB、FusDB、PhaSePro、PhaSepDB、UniProtKB、InterPro、PDBe-KB
- **评测指标**：未提供定量评测指标（如 precision/recall）；以覆盖规模（蛋白数、注释数）和外部评估引用（CAID）作为质量依据
- **基准/对照**：CAID 评估（Critical Assessment of protein Intrinsic Disorder prediction）作为外部基准被引用

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 同源转移流水线 | 可将精选注释扩展两个数量级 | 对比旧版流水线 | 精选注释扩展 2 个数量级 | 新流水线显著提升覆盖 | 未提供精度/假阳性率定量评估 | "expands manually curated annotations by two orders of magnitude" |
| AlphaFold 无序定义 | pLDDT < 70 可定义无序 | 与 CAID 评估结果对比 | 与实验无序和现有预测器相关性好 | AlphaFold 可作为无序预测器 | 未提供具体相关系数 | "correlate very well with experimental disorder and with state-of-the art disorder predictors according to CAID assessment" |
| Paxillin 案例 | AlphaFold 衍生 LIP 可识别条件折叠区域 | Paxillin 蛋白（P49023） | 预测 LIP 匹配 5 个保守 LD 基序及额外互作区域 | 方法可识别已知功能互作位点 | 单案例，非系统验证 | Figure 2 |
| 受控词汇表 | CV 可标准化注释描述 | 无对比 | 4 evidence / 39 feature / 37 source 术语 | 提供标准化框架 | 未评估用户采用率 | "Controlled vocabularies" 节 |

## 11 结论正确解读

- **任务范围**：本文是数据库资源更新报告，非方法学验证论文。核心贡献是数据整合、标准化和覆盖扩展，而非新算法或新生物学发现。
- **Oracle/真值输入**：同源转移以人工精选注释（DisProt 等）为 oracle；AlphaFold 衍生注释以实验无序数据为隐式真值（通过 CAID 评估间接验证）。
- **端到端状态**：数据库已上线运行，数据可公开访问；但"端到端"验证（如用户使用数据库产生新发现的案例）未在本文中系统评估。
- **算力成本**：未提供具体算力数据；仅提及 gold collection 重新生成需"数周计算时间"。
- **历史数据依赖**：依赖 UniProtKB 版本和外部数据库更新频率；成员数据库未同步更新时注释可能过期。
- **模型依赖**：AlphaFold 注释依赖 AlphaFoldDB 覆盖范围（目前仅 Swiss-Prot 和模式生物）；同源转移依赖 BLAST 搜索质量。
- **最难情形**：低复杂度区域（low complexity regions）被 BLAST 默认屏蔽，同源转移无法覆盖；孤儿蛋白（无同源序列）无法获得同源注释。
- **群体/领域边界**：注释质量受限于来源数据库的偏差（如 DisProt 偏向研究充分的蛋白）；预测注释对特定蛋白类型（如膜蛋白）可能不准确。
- **不确定性**：未提供注释的置信度区间或不确定性量化；共识注释规则未在本文中详细验证。

**有边界的复述**：MobiDB 通过分层整合多源证据，将无序注释覆盖扩展到全蛋白质组，并新增 AlphaFold 衍生和结合模式注释，但注释质量依赖来源数据库和同源转移的严格性，且未提供系统性的精度评估。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 低复杂度区域同源转移受限 | BLAST 默认屏蔽低复杂度区域，导致此类注释无法通过同源转移扩展 | 未明确提及 | "the homology transfer for low complexity regions is limited as they are masked by BLAST by default" |
| 相分离数据库覆盖有限 | 仅整合 PhaSePro 和 PhaSepDB 两个数据库 | 与 IDP Community 合作扩展 | "collaboration with the IDP Community of ELIXIR" |
| 数据格式标准化不足 | 需要与 BMRB、SASDB、PCDDB、PED 等数据库建立标准交换格式 | 确定标准交换格式以支持无序证据 | "identify a standard exchange format to support disorder evidence" |
| 成员数据库更新不同步 | 外部数据库未更新时注释可能不一致 | 通过自动工作流和 sanity checks 缓解 | "All annotations integrated from member databases undergo stringent sanity checks" |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 同源转移"两个数量级"扩展缺乏精度评估 | 严格阈值（80% 同一性）可能降低假阳性，但也可能遗漏真实同源注释；未报告 precision/recall | 用户需知道扩展注释的可靠性 | 在独立测试集上比较同源转移注释与实验验证 | "expands manually curated annotations by two orders of magnitude" |
| AlphaFold 无序定义仅依赖 pLDT 阈值 | pLDDT < 70 是启发式阈值，不同蛋白类型可能最优阈值不同；RSA 阈值 0.58 同样缺乏系统优化 | 阈值选择直接影响注释准确性 | 在不同蛋白家族上系统扫描阈值，与实验无序数据对比 | "residues with a pLDDT lower than 70% are considered disordered" |
| 共识注释规则未详细说明 | 不同层级证据如何组合为共识注释？冲突时如何处理？ | 用户无法判断共识注释的生成逻辑 | 查阅文档或代码库 | "consensus annotations which are combined according to different sets of rules" |
| 案例验证仅 Paxillin 单蛋白 | 单案例不足以证明 AlphaFold 衍生 LIP 的普适性 | 需多蛋白系统验证 | 在多个已知 IDP 互作体系上测试 | Figure 2 |
| 数据库更新周期和版本管理未说明 | 用户无法追踪注释版本变化 | 可重复性要求版本控制 | 检查数据库版本历史 | 未提供 |
| 未与其他 IDP 数据库（如 D2P2、IDEAL）进行系统比较 | 用户无法判断 MobiDB 的增量优势 | 数据库竞争格局需要明确差异化 | 系统比较各数据库的覆盖、精度、功能 | 未提供 |

## 14 Agent 提炼的知识候选

> 标题：Agent 提炼的知识候选

1. **AlphaFold2 低置信度区域作为无序/条件折叠特征**：MobiDB 将 pLDDT < 70 定义为无序，并结合 RSA > 0.58 识别"高溶剂暴露的无序区域"作为条件折叠候选。**可迁移到本课题**：在 IDP/IDR 介导的蛋白互作预测中，可将 AlphaFold2 pLDDT 和 RSA 作为输入特征，用于识别可能参与结合诱导折叠的区域。

2. **注释金字塔作为多源证据整合框架**：将实验、同源、预测分层整合，每层有明确可信度。**可迁移到本课题**：在构建 IDP 互作训练集时，可设计类似的分层标签体系（实验验证 > 同源推断 > 预测），并分别评估模型在不同证据层级的性能。

3. **同源转移的严格过滤策略**：90% 覆盖、80% 同一性、20% gap 限制。**可迁移到本课题**：在将已知 IDP 互作注释扩展到其他物种/同源蛋白时，采用类似严格阈值可控制假阳性。

4. **结合模式（binding modes）分类体系**：MobiDB 区分不同 IDP 结合模式（折叠结合、模糊复合物等）。**可迁移到本课题**：在 IDP 互作预测中，不仅预测"是否互作"，还可预测"互作模式"（如诱导折叠 vs 模糊结合），这需要不同的序列/结构特征。

5. **受控词汇表（CV）设计**：evidence/feature/source 三命名空间标准化注释。**可迁移到本课题**：在构建 IDP 互作数据库或训练集时，采用类似的三元组标注（证据类型、特征类型、来源），提高数据可复用性。

6. **相分离数据库整合策略**：将 PhaSePro 和 PhaSepDB 的驱动区域注释整合到主数据库。**可迁移到本课题**：相分离驱动区域与 IDP 互作区域高度重叠，可交叉利用这两类注释进行特征工程。

## 15 与已有知识连接

- **DisProt**（参考文献中作为主要实验注释来源）：MobiDB 金字塔顶层的核心数据源，提供人工精选的无序注释。本课题中 DisProt 也是 IDP 互作训练集的重要来源。
- **PDB 缺失残基**：MobiDB 从 PDB 结构中提取缺失残基作为实验无序证据。这与本课题中利用晶体结构缺失区域识别 IDR 的方法一致。
- **CAID 评估**（Critical Assessment of protein Intrinsic Disorder prediction）：MobiDB 引用 CAID 验证 AlphaFold 无序预测能力。本课题中 CAID 可作为 IDP 预测模型的基准评估框架。
- **AlphaFoldDB**：MobiDB 整合 AlphaFold2 预测结构。本课题中 AlphaFold2 结构预测是 IDP 互作建模的重要工具，其 pLDDT 分数已被广泛用于无序区识别。
- **FuzDB**：MobiDB 整合模糊复合物注释。模糊复合物是 IDP 互作的特殊模式，本课题中可参考 FuzDB 的注释体系。
- **ELM 数据库**：MobiDB 提及 ELM 的短线性基序（SLiMs）注释。SLiMs 是 IDP 互作的重要功能位点，本课题中可结合 SLiM 注释进行互作位点预测。
- **PhaSePro / PhaSepDB**：相分离驱动区域数据库。本课题中相分离与 IDP 互作密切相关，这两个数据库提供实验验证的相分离区域注释。
- **IUPred / ESpritz**：MobiDB 早期使用的预测工具。本课题中这些经典无序预测器可作为基线或特征。
- **RING 软件**：MobiDB 用于检测 PDB 复合物中分子间相互作用。本课题中 RING 可用于从结构数据中提取 IDP 互作残基对。

## 16 Agent 生成的研究候选

> 标题：Agent 生成的研究候选

### 候选 1：基于 AlphaFold2 pLDDT/RSA 的 IDP 互作位点预测模型
- **来源局限/观察**：MobiDB 证明 pLDDT + RSA 可识别条件折叠区域（如 Paxillin 案例），但未系统验证这些特征对互作位点预测的贡献。
- **核心假设**：AlphaFold2 低 pLDDT + 高 RSA 的区域富集 IDP 互作位点，且结合模式（折叠结合 vs 模糊结合）可通过 pLDDT/RSA 组合特征区分。
- **相对本文增量**：从数据库注释到预测模型，系统评估 AlphaFold 衍生特征在互作位点预测中的增量价值。
- **初步方法**：以 DisProt/FuzDB 互作注释为标签，提取 pLDDT、RSA、序列组成、进化保守性等特征，训练分类模型（如 gradient boosting 或 GNN），与仅用序列特征的基线对比。
- **验证方式**：在 CAID 基准和独立 IDP 互作数据集上评估；分结合模式（折叠 vs 模糊）进行分层评估。
- **可能失败模式**：pLDDT/RSA 特征与互作位点相关性不足；不同蛋白家族间特征分布差异大导致泛化差。
- **创新状态**：unverified

### 候选 2：利用 MobiDB 注释金字塔构建 IDP 互作训练集的多源标签融合策略
- **来源局限/观察**：MobiDB 的分层注释（实验/同源/预测）为训练集构建提供天然的分层标签，但未提供标签融合的定量评估。
- **核心假设**：在训练 IDP 互作预测模型时，将不同证据层级的标签按可信度加权（而非二值化）可提升模型性能。
- **相对本文增量**：将数据库设计原则转化为机器学习训练策略。
- **初步方法**：从 MobiDB API 获取分层注释，构建多级标签（如 0=无证据, 1=仅预测, 2=同源, 3=实验），设计加权损失函数训练模型，与二值标签基线对比。
- **验证方式**：在保留的实验注释子集上评估；比较不同加权策略的 precision-recall。
- **可能失败模式**：分层标签噪声传播；加权策略过拟合特定数据库偏差。
- **创新状态**：unverified

### 候选 3：结合 AlphaFold2 结构和 MobiDB 注释的 IDP 介导相分离驱动区域预测
- **来源局限/观察**：MobiDB 整合了 PhaSePro/PhaSepDB 相分离注释，但未提供基于结构的相分离驱动区域分析。
- **核心假设**：相分离驱动区域具有独特的 AlphaFold2 结构特征（如低 pLDDT 但特定模式的多域布局），可与其他 IDP 区域区分。
- **相对本文增量**：将结构预测特征引入相分离区域预测，超越纯序列方法。
- **初步方法**：提取相分离驱动区域的 pLDDT 分布、预测接触图、RSA 谱等特征，与 IDP 互作区域和非功能无序区对比，训练分类器。
- **验证方式**：在 PhaSePro 实验验证区域上交叉验证；与已知序列特征方法（如 catGRANULE）对比。
- **可能失败模式**：相分离驱动区域与普通 IDR 结构特征差异不显著；训练数据量有限。
- **创新状态**：unverified

### 候选 4：基于同源转移注释的跨物种 IDP 互作保守性分析
- **来源局限/观察**：MobiDB 的同源转移 pipeline 扩展了注释覆盖，但未分析互作位点的进化保守性。
- **核心假设**：实验验证的 IDP 互作位点在同源蛋白中高度保守，且保守程度与结合模式相关。
- **相对本文增量**：利用 MobiDB 同源转移注释进行进化分析，为互作位点预测提供保守性特征。
- **初步方法**：从 MobiDB 获取同源转移注释，计算互作位点的序列保守性（如 ConSurf 分数），分析不同结合模式的保守性差异。
- **验证方式**：与实验验证的互作位点对比；评估保守性特征对互作位点预测的增量贡献。
- **可能失败模式**：同源转移注释的假阳性影响保守性分析；IDP 互作位点保守性普遍较低。
- **创新状态**：unverified