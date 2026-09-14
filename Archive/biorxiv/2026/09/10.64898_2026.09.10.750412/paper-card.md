## 01 基本信息

- **标题**：Agentic-AI-ready genome-wide poxvirus-host interaction screen refined by a protein language model
- **作者**：Jacob Anter; Jason Mercer; Artur Yakimovich
- **单位**：未提供（bioRxiv 预印本未在提供材料中列出单位）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2026（预印本日期 2026-09-13）
- **论文类型**：预印本（方法学 + 资源型论文）
- **领域**：病毒-宿主互作、功能基因组筛选、蛋白质语言模型、正-未标记学习
- **关键词**：poxvirus、vaccinia virus、RNA interference screen、protein language model、positive-unlabelled learning、host factors、agentic AI
- **DOI/arXiv**：10.64898/2026.09.10.750412
- **代码**：未提供
- **数据**：基因组规模痘病毒宿主因子筛选的原始与精炼 read-out，作为 agentic-AI-ready 社区资源提供
- **阅读日期**：2026-09-14（按预印本日期推算，实际阅读日期未提供）
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**：本文不直接研究 IDP/IDR 或相分离，但其核心方法——用蛋白质语言模型（pLM）提取的蛋白-蛋白互作（PPI）信息来精炼功能筛选的 hit 优先级——对 IDP/IDR 介导的互作研究具有直接的方法学迁移价值。pLM 嵌入可捕捉由 IDR 介导的弱/瞬时互作信号，而 positive-unlabelled（PU）学习框架可推广到任何以「表型筛选 + PPI 先验」为结构的场景，包括相分离凝聚体的功能筛选。

---

## 02 一句话总结

本文提出 ICARus——一个将蛋白质语言模型衍生的 PPI 信息整合进 positive-unlabelled 学习框架的 read-out 精炼方法，用于从全基因组 RNAi 筛选中更可靠地识别痘病毒宿主因子（尤其是抗病毒功能基因），并发布 agentic-AI-ready 的筛选数据资源。

---

## 03 研究问题

- **具体问题**：在全基因组 RNAi 筛选中，脱靶效应（off-target effects）和检测噪声掩盖了真实的基因-表型关系，导致病毒-宿主互作因子的发现受阻。如何从噪声密集的筛选 read-out 中稳健地优先排序真正的宿主因子？
- **为什么重要**：近期 mpox 疫情凸显了理解痘病毒-人类宿主互作的必要性；系统性地发现参与感染的宿主基因是发现治疗靶点的关键路径。
- **现有方法为何不足**：传统筛选分析仅依赖 read-out 本身的统计显著性，未利用独立的生物学先验（如 PPI 网络信息）来区分真实信号与噪声/脱靶效应。
- **精确研究问题**：Can integrating protein language model-derived PPI information into a positive-unlabelled learning framework refine genome-wide RNAi screen read-outs to better identify true poxvirus host factors?

---

## 04 背景与发展脉络

> 注：以下脉络基于本文框架重建，标注「仅本文框架」；外部核验部分单独标注。

1. **阶段一：全基因组 RNAi 筛选（经典方法）**
   - 代表性方法：单细胞水平 RNAi 筛选，通过敲低每个宿主基因后检测病毒感染表型。
   - 优点：无偏、基因组规模、可直接发现功能相关基因。
   - 局限：脱靶效应、assay 噪声、批次效应导致假阳性/假阴性率高。
   - 来源：本文引言所述背景。

2. **阶段二：统计精炼与多组学整合**
   - 代表性方法：基于统计阈值的 hit 选择、多重复一致性过滤、与已知互作数据库（如 BioGRID、STRING）交叉验证。
   - 优点：一定程度降低假阳性。
   - 局限：依赖人工设定的阈值和外部数据库的覆盖度；未充分利用连续型 PPI 信号。
   - 来源：本文框架推断。

3. **阶段三：蛋白质语言模型（pLM）时代**
   - 代表性方法：用 ESM 等 pLM 的嵌入表示蛋白质，通过嵌入相似性或下游模型预测 PPI。
   - 优点：无需实验 PPI 数据即可生成全基因组规模的互作先验；可捕捉序列-结构-功能关系。
   - 局限：pLM 预测的 PPI 本身有噪声，直接作为硬过滤条件会丢失真实信号。
   - 来源：本文方法部分所述。

4. **本文主张的位置**：将 pLM 衍生的 PPI 信息作为 soft prior 整合进 PU 学习框架，而非硬过滤——即在「无偏筛选」与「先验知识」之间取平衡，实现 read-out 的稳健精炼。
   - 来源：本文摘要与框架。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 脱靶效应 | RNAi 筛选中的假阳性 hit 被误认为真实宿主因子 | RNAi 试剂可非特异性地沉默多个基因，导致表型与目标基因无关 | 摘要：「off-target effects and assay noise obscure true gene-phenotype relationships」 |
| 检测噪声 | 同一基因在不同重复/条件下 read-out 波动大 | 单细胞 assay 的生物学变异 + 技术噪声 | 摘要：「assay noise」 |
| 真实信号被掩盖 | 真阳性宿主因子因噪声/脱靶干扰而排名不高 | 传统统计方法未利用独立生物学先验来区分信号与噪声 | 摘要：「hampering the discovery of therapeutically relevant targets」 |
| 先验知识利用不足 | 已知 PPI 信息未被系统整合进筛选分析 | 现有方法多为硬过滤或事后验证，未在模型层面融合 | 本文方法设计（ICARus 的提出动机） |

---

## 06 核心思想

### 1) 表面方法
ICARus 是一个 positive-unlabelled（PU）学习框架：将筛选 read-out 中高置信度的 hit 视为 positive，其余视为 unlabelled，用蛋白质语言模型衍生的 PPI 特征作为辅助信息，训练分类器来重新评估每个基因属于真实宿主因子的概率，从而精炼原始 read-out 的排名。

### 2) 核心洞察
pLM 衍生的 PPI 信息可以作为独立于表型 read-out 的生物学先验，在 PU 框架中充当「校准信号」——即使 pLM 预测本身有噪声，其与真实 PPI 的弱相关性也足以在 aggregate 层面提升 hit 优先排序的精度，而非依赖单条预测的准确性。

### 3) 可能的普适教训 [Analysis]
- 将「弱但独立的先验」以 soft 方式整合进学习框架，比硬过滤更鲁棒——这一原则可迁移到 IDP/IDR 研究：pLM 对 IDR 介导互作的预测虽不精确，但可作为先验特征融入功能筛选或凝聚体表型的分析。
- PU 学习天然适配「正例少、未标记多」的生物学场景（如已知互作少、未知互作多），与 IDP/IDR 互作网络的不完整现状高度契合。

---

## 07 方法总览

- **输入**：
  1. 全基因组 RNAi 筛选的原始 read-out（每个基因的感染表型得分）
  2. 蛋白质语言模型（pLM）衍生的全基因组 PPI 特征（如嵌入相似度或预测互作概率）
- **输出**：精炼后的基因排名（每个基因作为真实宿主因子的概率/得分）
- **模块**：
  1. Positive 集合构建：从原始 read-out 中选取高置信度 hit 作为 positive
  2. 特征工程：将 pLM 衍生的 PPI 信息编码为每个基因的特征向量
  3. PU 学习分类器：在 positive + unlabelled 上训练，输出每个基因的「真实宿主因子概率」
  4. Read-out 精炼：将原始 read-out 与 PU 概率融合，生成最终排名
- **训练**：PU 学习框架（具体算法细节未在摘要中提供）
- **工具**：蛋白质语言模型（具体模型未在摘要中指定）
- **反馈回路**：未明确描述（可能通过迭代优化 positive 集合）
- **假设**：pLM 衍生的 PPI 信息与真实宿主因子身份存在弱但可利用的相关性；PU 学习能有效利用未标记数据中的信息
- **文字流程**：原始 read-out → 选取 positive → 提取 pLM-PPI 特征 → PU 分类器训练 → 输出精炼概率 → 与原始 read-out 融合 → 最终 hit 排名

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| Positive 集合构建 | 从原始 read-out 中识别高置信度 hit 作为正例 | PU 学习需要正例；原始 read-out 中高置信度 hit 相对可靠 | 输入：原始 read-out；输出：positive 基因集合 | 摘要：「positive-unlabelled read-out refinement framework」 | 预期影响：positive 集合质量下降会直接降低 PU 分类器精度 [Analysis] |
| pLM-PPI 特征提取 | 将 pLM 衍生的 PPI 信息编码为基因特征 | 提供独立于表型的生物学先验 | 输入：蛋白质序列；输出：PPI 特征向量 | 摘要：「integrating protein-protein interaction information derived from a protein language model」 | 预期影响：移除后 ICARus 退化为纯统计方法，失去先验校准能力 [Analysis] |
| PU 学习分类器 | 在 positive + unlabelled 上学习真实宿主因子概率 | 利用未标记数据中的信息，避免仅依赖 positive | 输入：positive 特征 + unlabelled 特征；输出：每个基因的概率得分 | 摘要：「ICARus - a positive-unlabelled read-out refinement framework」 | 预期影响：移除后无法生成精炼概率，仅剩原始 read-out [Analysis] |
| Read-out 融合 | 将原始 read-out 与 PU 概率结合生成最终排名 | 保留原始表型信息的同时引入先验校准 | 输入：原始 read-out + PU 概率；输出：精炼排名 | 摘要：「enhances the identification of human genes with potential antiviral function」 | 预期影响：移除融合步骤则 PU 输出与原始 read-out 脱节 [Analysis] |

> 注：以上「预期影响」均为 [Analysis] 推断，原文未提供消融实验数据。

---

## 09 关键公式符号

不适用。摘要中未提供具体数学公式或符号定义。

---

## 10 实验设计与证据链

- **数据集**：全基因组 RNAi 筛选（痘病毒-宿主互作），具体细胞系、文库规模未在摘要中提供
- **指标**：hit 识别精度/优先排序质量（具体指标未在摘要中提供）
- **基线**：未在摘要中明确列出（推测为传统统计阈值方法）
- **评测协议**：未在摘要中提供
- **oracle 输入**：pLM 衍生的 PPI 信息（具体模型与版本未提供）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|----------------|------|
| ICARus 精炼 vs 原始 read-out | pLM-PPI 整合能提升宿主因子识别 | ICARus 精炼排名 vs 原始 read-out 排名 | 摘要：「boosts the discovery of vaccinia virus-host interactions」 | pLM-PPI 整合可提升 hit 优先排序 | 未提供量化指标，无法评估提升幅度 | 摘要 |
| 抗病毒功能基因识别 | ICARus 能增强抗病毒基因的识别 | 精炼后排名中抗病毒基因的富集 | 摘要：「enhances the identification of human genes with potential antiviral function」 | ICARus 对抗病毒基因有偏好性提升 | 未提供具体基因列表或富集分析 | 摘要 |

> 注：摘要中未提供详细实验数据、消融实验或统计检验，以上仅基于摘要可获取信息。

---

## 11 结论正确解读

- **任务范围**：本文聚焦于痘病毒（vaccinia virus）宿主因子的全基因组 RNAi 筛选 read-out 精炼，不涉及其他病毒或表型筛选的验证。
- **oracle/真值输入**：pLM 衍生的 PPI 信息作为先验输入，其质量直接影响结果；但 pLM 预测的 PPI 本身有噪声，ICARus 的价值在于「弱先验也能提升 aggregate 精度」。
- **端到端状态**：ICARus 是分析流程而非湿实验流程；其输出是精炼排名，需后续实验验证。
- **算力成本**：未提供。
- **历史数据依赖**：依赖全基因组 RNAi 筛选数据的质量；脱靶效应和噪声虽被缓解但未消除。
- **模型依赖**：依赖 pLM 的嵌入质量；不同 pLM 可能产生不同结果。
- **最难情形**：对于 pLM 预测 PPI 信号极弱的基因（如 IDR 介导的瞬时互作），ICARus 的增益可能有限 [Analysis]。
- **群体/领域边界**：结论限于痘病毒-宿主互作筛选；「generalisable strategy」是作者主张，尚未在跨领域验证。
- **不确定性**：摘要未提供置信区间、效应量或统计检验，无法评估精炼提升的稳健性。

**有边界的复述**：在痘病毒全基因组 RNAi 筛选中，将 pLM 衍生的 PPI 信息以 PU 学习方式整合，可提升宿主因子（尤其抗病毒基因）的识别精度；该策略的跨领域普适性尚待验证。

---

## 12 作者自认局限

在提供的材料（摘要）中未发现作者明确承认的局限。

**作者提及的相关约束**（非正式局限）：
- 摘要中「off-target effects and assay noise obscure true gene-phenotype relationships」暗示筛选数据本身的噪声是 ICARus 试图缓解但无法完全消除的约束。
- 「generalisable strategy」的表述暗示当前验证范围限于痘病毒系统，跨系统推广尚属展望。

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| pLM-PPI 先验可能引入系统性偏差 | pLM 训练数据偏向研究充分的蛋白家族，IDP/IDR 富集的蛋白可能表征不足，导致先验对这类基因不利 | 若目标基因富集 IDP/IDR，ICARus 可能系统性低估其排名 | 比较 ICARus 精炼前后 IDP/IDR 富集基因的排名变化 | 摘要未提供 pLM 类型与训练数据细节 |
| PU 学习的 positive 集合构建依赖原始 read-out 阈值 | 阈值选择可能引入主观性，不同阈值下 ICARus 表现可能不稳定 | 影响方法可复现性和跨数据集迁移 | 对阈值进行敏感性分析 | 摘要未提供 positive 选择标准 |
| 「boosts discovery」缺乏量化支撑 | 摘要未提供效应量、precision/recall 或与基线的统计比较 | 无法评估提升幅度和实际应用价值 | 要求提供与基线方法的量化对比 | 摘要仅定性描述 |
| 抗病毒基因的「增强识别」可能反映先验偏差而非真实信号 | pLM 可能对已知抗病毒基因（研究充分）有更好的表征，导致先验偏好 | 若如此，ICARus 的增益是「已知知识回响」而非新发现 | 检查精炼后新命中的基因是否在 pLM 训练数据中表征充分 | 摘要未提供新命中基因列表 |
| Agentic-AI-ready 资源缺乏明确接口定义 | 「agentic-AI-ready」是新兴概念，摘要未说明数据格式、API 或 agent 交互协议 | 影响资源实际可用性和社区采纳 | 要求提供数据 schema 与使用文档 | 摘要仅提及「community resource」 |

---

## 14 Agent 提炼的知识候选

> 面向课题方向：IDP/IDR × 蛋白互作 × AI/物理模拟

1. **pLM-PPI 作为 soft prior 的通用框架**：ICARus 的核心思想——用 pLM 衍生的 PPI 信息作为 PU 学习中的辅助特征——可直接迁移到 IDP/IDR 研究。例如，在 IDR 介导的相分离候选蛋白筛选中，可将 pLM 预测的互作特征与凝聚体表型 read-out 结合，提升 hit 优先排序。

2. **PU 学习适配 IDR 互作网络的不完整性**：IDP/IDR 互作网络已知高度不完整（正例少、未标记多），PU 学习天然适配这一场景。可将已知的 IDR 介导互作作为 positive，其余作为 unlabelled，用 pLM 特征训练分类器预测新的 IDR 互作。

3. **弱先验的 aggregate 价值**：pLM 对 IDR 介导的弱/瞬时互作预测可能不精确，但 ICARus 的逻辑表明「弱但独立」的先验在 aggregate 层面仍有校准价值——这为「用 pLM 预测 IDR 互作虽不准但有用」提供了方法论辩护。

4. **read-out 精炼作为通用分析层**：任何「表型筛选 + 互作先验」的结构（如凝聚体突变筛选 + AlphaFold 互作预测）都可套用 ICARus 的 read-out 精炼思路，作为湿实验前的计算预筛层。

5. **Agentic-AI-ready 数据资源范式**：将筛选数据以 agent 可交互的格式发布，是未来功能基因组数据共享的方向；IDR/相分离领域可借鉴此范式，发布凝聚体筛选的标准化数据资源。

---

## 15 与已有知识连接

- **pLM 用于 PPI 预测**：ESM 等 pLM 已被广泛用于 PPI 预测（如 ESM-1v、ESM2 嵌入 + 下游分类器）。本文将其用于筛选 read-out 精炼而非直接 PPI 预测，是应用场景的迁移。相关文献：Lin et al., Science 2023 (ESM2)；Chowdhury et al., 2022 (ESM-fold)。
- **PU 学习在生物医学的应用**：PU 学习已用于药物-靶点预测、基因-疾病关联发现等场景。本文将其引入功能筛选分析，属于方法迁移。相关方向：Yang et al., Briefings in Bioinformatics 2012 (PU learning for gene-disease)。
- **RNAi 筛选的噪声问题**：RNAi 脱靶效应是已知难题，已有多种计算校正方法（如 seed-based off-target prediction）。ICARus 的贡献在于引入独立先验而非改进脱靶预测本身。
- **与 IDP/IDR 研究的连接 [Analysis]**：IDR 介导的互作通常为弱亲和力、瞬时互作，实验检测难度高，pLM 对此类互作的预测能力尚不明确。ICARus 的「弱先验可用」逻辑为这一困境提供了潜在出路，但需在 IDR 数据集上验证。
- **与相分离研究的连接 [Analysis]**：相分离凝聚体的功能筛选（如以凝聚体形成/解离为表型）可类比 RNAi 筛选，ICARus 的 read-out 精炼框架可直接迁移。

---

## 16 Agent 生成的研究候选

> 标题：Agent 生成的研究候选

1. **候选名称**：IDR-PU：基于 pLM 与 PU 学习的 IDR 介导互作功能筛选精炼
   - **来源局限/观察**：ICARus 在痘病毒筛选中有效，但 IDR 介导互作具有弱/瞬时特性，pLM 先验可能更弱，需验证「弱先验」逻辑在 IDR 场景是否成立。
   - **核心假设**：pLM 衍生的 PPI 特征即使对 IDR 介导互作预测不精确，也能在 PU 框架中提升功能筛选的 hit 优先排序。
   - **初步方法**：选取一个 IDR 富集的功能筛选数据集（如应激颗粒/相分离相关 RNAi 筛选），用 ESM2 嵌入提取 PPI 特征，套用 ICARus 的 PU 框架，比较精炼前后 hit 精度。
   - **验证方式**：用已知的 IDR 介导互作数据库（如 ELM、IUPred 注释）作为 ground truth，计算 precision@k 和 AUPRC。
   - **可能的失败模式**：pLM 对 IDR 介导互作的特征区分度过低，PU 分类器无法学到有效信号；或 IDR 相关表型筛选的噪声结构不同于病毒筛选，PU 假设不成立。
   - **创新状态**：unverified

2. **候选名称**：凝聚体筛选的 agentic-AI-ready 数据资源
   - **来源局限/观察**：ICARus 发布了痘病毒筛选的 agentic-ready 数据，但相分离/凝聚体领域缺乏类似标准化资源。
   - **核心假设**：将凝聚体相关筛选数据以标准化、agent 可交互格式发布，可加速领域内 AI 方法的开发与验证。
   - **初步方法**：整合现有凝聚体筛选数据集（如 stress granule、P-body 相关 RNAi/CRISPR 筛选），定义统一 schema，提供 API 接口。
   - **验证方式**：邀请领域内研究者试用，评估数据可发现性和可交互性。
   - **可能的失败模式**：数据异质性过高，标准化成本大于收益；社区采纳率低。
   - **创新状态**：unverified

3. **候选名称**：pLM 先验 vs AlphaFold 先验在筛选精炼中的对比
   - **来源局限/观察**：ICARus 用 pLM 衍生的 PPI 信息，但 AlphaFold-Multimer 等结构预测工具也提供互作先验，两者在筛选精炼中的相对价值未知。
   - **核心假设**：AlphaFold 先验对高置信度结构互作更精确，但覆盖度低；pLM 先验覆盖广但噪声高——两者在 PU 框架中可能互补。
   - **初步方法**：在同一筛选数据集上分别用 pLM 特征和 AlphaFold 特征训练 PU 分类器，比较精炼效果；再尝试特征融合。
   - **验证方式**：交叉验证 + 独立验证集上的 hit 精度比较。
   - **可能的失败模式**：AlphaFold 先验覆盖度过低，无法提供有效信号；或两种先验高度相关，融合无增益。
   - **创新状态**：unverified

4. **候选名称**：IDR 介导互作的「弱先验」理论边界
   - **来源局限/观察**：ICARus 的成功依赖「弱先验在 aggregate 层面有用」这一假设，但该假设的适用边界（先验多弱才失效？）未探索。
   - **核心假设**：存在一个先验-噪声比阈值，低于该阈值时 PU 精炼不再优于纯统计方法。
   - **初步方法**：在模拟数据上系统变化先验强度（信噪比），绘制 ICARus 性能曲线，确定失效边界；再用真实 IDR 数据验证。
   - **验证方式**：模拟实验 + 真实数据对照。
   - **可能的失败模式**：真实数据的先验强度难以精确控制，模拟与真实结果不一致。
   - **创新状态**：unverified