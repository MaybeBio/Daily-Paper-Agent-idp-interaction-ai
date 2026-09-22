## 01 基本信息

- **标题**：MedProDB: A database of Mediator proteins
- **作者**：Bhardwaj, Rohan; Thakur, Jitendra Kumar; Kumar, Shailesh
- **单位**：National Institute of Plant Genome Research（印度国家植物基因组研究所，基于致谢信息推断）
- **期刊/平台**：Computational and Structural Biotechnology Journal
- **年份**：2021（2021-09-17 在线发表）
- **论文类型**：数据库资源型论文（Database Resource）
- **领域**：转录调控、Mediator 复合物、生物信息学数据库
- **关键词**：Mediator complex；Mediator subunits；Intrinsically Disordered Regions (IDRs)；Molecular Recognition Features (MoRFs)；Post-translational modifications (PTMs)；Database
- **DOI/arXiv 号**：10.1016/j.csbj.2021.07.031
- **代码**：未提供（数据库本身为资源）
- **数据**：MedProDB 数据库，URL: www.nipgr.ac.in/MedProDB（33,971 条 Mediator 蛋白序列，涵盖 331 个后生动物、658 个真菌、123 个植物物种）
- **阅读日期**：2026-05-13（按当前日期）
- **在该课题方向中的位置**：本文是 Mediator 蛋白家族（含 IDR/MoRF 注释）的**首个专用数据库**，为 IDP/IDR 介导的蛋白互作研究提供了 Mediator 复合物这一关键转录调控节点的序列-结构-功能注释资源。其 IDR/MoRF 跨物种保守性分析、PTM 与 IDR 共定位分析，对 IDP/IDR × 蛋白互作 × AI 方法课题具有直接的数据支撑价值。

---

## 02 一句话总结

本文构建了首个 Mediator 蛋白专用数据库 MedProDB，通过 HMM 谱搜索从 1113 个物种中鉴定 33,971 条 Mediator 亚基序列，并系统注释其理化性质、IDR、MoRF、PTM 位点及疾病关联，发现 IDR 位置在跨物种间保守且富含 PTM 位点，提示无序区域是 Mediator 功能调控的核心。

---

## 03 研究问题

- **具体问题**：Mediator 复合物是转录调控的核心共调节因子，但其亚基序列信息分散于多个数据库，缺乏整合的专用资源。具体而言：(1) 哪些蛋白属于 Mediator 亚基？(2) 这些亚基的 IDR/MoRF 分布如何？(3) IDR 是否跨物种保守？(4) PTM 位点是否富集于 IDR 内？
- **为什么重要**：Mediator 调控几乎所有 Pol II 依赖的基因转录，其亚基突变与多种癌症、发育缺陷相关。理解 Mediator 亚基的无序区域特征，是揭示其"如何与众多转录因子动态互作"这一核心机制问题的关键。
- **现有方法不足**：此前无 Mediator 专用数据库；UniProt 等通用数据库缺乏针对 Mediator 的 IDR/MoRF/PTM 整合注释；植物 Mediator 亚基鉴定尤其不完整。
- **精确研究问题**：Can a comprehensive database of Mediator subunits across eukaryotes reveal conserved IDR/MoRF patterns that explain the complex's functional versatility?

---

## 04 背景与发展脉络

> 注：以下脉络为「经外部核验」的领域发展框架，结合本文引用与课题方向。

1. **Mediator 发现与亚基鉴定阶段（1990s-2000s）**：1994 年酵母中首次纯化 Mediator（Kim et al.）；随后在人类、果蝇等后生动物中鉴定同源复合物。代表性方法：生化纯化 + 质谱。局限：不同物种亚基组成差异大，植物亚基鉴定滞后。
2. **生物信息学鉴定阶段（2010s）**：利用序列同源搜索（BLAST、HMM）跨物种鉴定 Mediator 亚基。代表：Bourbon 2008 年对后生动物 Mediator 的系统分析。局限：缺乏整合数据库，IDR 等特征未系统注释。
3. **IDR 功能认识深化阶段（2010s-至今）**：认识到 Mediator 亚基富含 IDR（如 Med15 的激活子互作域），IDR 介导相分离参与转录凝聚体形成（Boija et al. 2018, Science；Sabari et al. 2018, Science）。本文作者前期工作（Thakur 实验室）已报道植物 Mediator 亚基 IDR 保守性。
4. **本文位置**：在上述脉络中，本文是**首个将 Mediator 亚基序列、IDR、MoRF、PTM、疾病注释整合为专用数据库**的工作，填补了 Mediator 研究中的资源空白，为后续 AI/深度学习分析 Mediator 无序互作网络提供了数据基础。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| Mediator 亚基信息分散 | 序列、功能、互作、疾病数据分散于 UniProt、IntAct、PubMed 等多个数据库 | 无 Mediator 专用整合资源 | Introduction 末段："surprisingly, to the best of our knowledge, there is no database of Mediator subunits available in the public domain" |
| 植物 Mediator 亚基鉴定不完整 | 植物 Mediator 亚基数目和组成存在争议 | 不同实验研究结论不一致 | Results："There have been few discrepancies in the Mediator complex composition, and different experimental studies have concluded different results" |
| 亚基命名混乱 | 同一亚基在不同物种中名称不同（如 Med2/29/32 为同源组） | 进化过程中亚基分化与融合 | Results 中多处使用斜线命名（Med2/29/32, Med3/27） |
| IDR/MoRF 注释缺乏系统性 | 各亚基 IDR 位置、MoRF 数量、保守性无统一资源 | 未对 Mediator 全家族进行系统无序性分析 | Methods 2.2 节 IDR/MoRF 计算流程 |
| PTM 与无序区域关系不明 | PTM 位点是否富集于 IDR 内缺乏系统统计 | 未进行跨物种 PTM-IDR 共定位分析 | Results 2.4 节 PTM 分析（图 3） |

---

## 06 核心思想

### 1) 表面方法
构建一个三层架构的数据库：(a) 以已知 Mediator 亚基为种子序列，分 kingdom 构建 HMM 谱，搜索 UniProt 数据库鉴定新亚基；(b) 对每条序列计算理化性质（长度、分子量、芳香性、GRAVY、不稳定指数、pI）、IDR（IUPred）、MoRF（MoRF-CHiBi）、PTM 位点；(c) 整合 UniProt/IntAct/PubMed 的注释信息（功能、互作、疾病），通过 Web 界面提供多级检索（Global/Simple/Advanced Search）和内置工具（BLAST、IUPred、MoRF-CHiBi）。

### 2) 核心洞察
- **IDR 位置保守性**：尽管 Mediator 亚基序列在远缘物种间相似性低，但 IDR 的位置（N端/中间/C端）在 kingdom 内高度保守，提示无序性本身是功能约束的进化特征。
- **PTM 富集于 IDR**：磷酸化、乙酰化、甲基化、糖基化位点大量富集于 IDR 内部，且部分 PTM 位点与 MoRF 重叠，提示无序区域通过 PTM 调控互作。
- **Med15/Med19 为全局无序枢纽**：Med15（尾模块）和 Med19（头模块）在所有 kingdom 中平均无序度 >0.5，与其已知的多互作伴侣功能一致。

### 3) 可能的普适教训 [Analysis]
- **"序列不保守，但无序模式保守"** 这一发现对 IDP/IDR 研究具有方法论启示：在跨物种比较 IDR 功能时，应比较无序倾向谱（disorder propensity profile）而非序列同源性。
- **数据库设计模式**：以 HMM 谱 + 多特征注释 + 内置分析工具的架构，可迁移至其他 IDR 富集的蛋白家族（如转录因子、RNA 结合蛋白）数据库构建。
- **PTM-IDR-MoRF 三者的共定位分析框架**，为研究"无序区域如何通过翻译后修饰动态调控互作"提供了可复用的计算流程。

---

## 07 方法总览

- **输入**：已知 Mediator 亚基种子序列（来自 SwissProt 已注释亚基）、UniProt 蛋白数据库、TAIR/Oryzabase 植物序列数据库
- **输出**：MedProDB 数据库（33,971 条序列 + 注释），Web 界面
- **模块**：
  1. **序列鉴定模块**：ClustalO 多序列比对 → HMMER 构建 kingdom 特异 HMM 谱 → HMMSearch 搜索（E-value ≤ 0.01）→ 去冗余
  2. **特征计算模块**：Bio.SeqUtils.ProtParam（理化性质）、IUPred（IDR，阈值 0.5，最小长度 30 aa）、MoRF-CHiBi（MoRF，阈值 0.72，最小长度 5 aa）、NetPhos/NetOGlyc/GPS-MSP/PAIL（PTM）
  3. **注释整合模块**：从 UniProt/IntAct/PubMed 提取功能、互作、疾病注释；人工整理人类疾病数据（基于 8525 篇文献）
  4. **Web 展示模块**：HTML/CSS/PHP/MySQL/JavaScript，提供 Global/Simple/Advanced Search、Browse（按名称/kingdom/模块）、PTM 工具链接、内置 BLAST/IUPred/MoRF-CHiBi
- **训练**：不适用（无监督学习/无模型训练）
- **反馈回路**：数据库设计为可扩展架构，未来可添加新序列和新注释（Future extensions 节）
- **文字流程**：从 SwissProt 下载已注释 Mediator 亚基序列 → 分 kingdom 构建 HMM 谱 → 搜索 UniProt 全库 → 去冗余获得最终序列集 → 对每条序列计算理化性质、IDR、MoRF、PTM → 整合功能/互作/疾病注释 → 存入 MySQL → 通过 Web 界面提供检索与分析工具

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| HMM 谱构建与搜索 | 跨物种鉴定 Mediator 亚基同源序列 | 序列相似性低，BLAST 不足以识别远缘同源物 | 输入：种子序列；输出：候选亚基序列列表 | Methods 2.1 节；结果获得 33,971 条序列 | 预期影响：无法鉴定远缘物种亚基，数据库规模大幅缩水 [预期效应] |
| 去冗余处理 | 去除重复/高度相似序列 | 避免数据库冗余影响统计 | 输入：HMM 搜索原始命中；输出：非冗余序列集 | Methods 2.1 节 | 预期影响：数据库条目膨胀，统计结果偏差 [预期效应] |
| IUPred IDR 预测 | 计算每条序列的无序倾向 | IDR 是 Mediator 功能的核心特征 | 输入：蛋白序列；输出：每个残基无序分数 + IDR 区间 | Methods 2.2 节；图 1 展示各亚基平均无序度 | 实测影响：无法生成图 1 的跨 kingdom 无序度比较 [实测消融效应] |
| MoRF-CHiBi 预测 | 识别 IDR 内的分子识别特征 | MoRF 是 IDR 介导互作的关键位点 | 输入：蛋白序列；输出：MoRF 位置 | Methods 2.2 节；图 4 展示 MoRF 分数 | 预期影响：丢失 IDR-互作关系的关键注释 [预期效应] |
| PTM 预测与 IDR 共定位 | 预测 4 类 PTM 位点并统计与 IDR/MoRF 重叠 | PTM 调控 IDR 介导的互作 | 输入：8 个模式物种序列；输出：PTM 位点及共定位统计 | Results 2.4 节；图 3 | 预期影响：无法揭示 PTM-IDR 共定位规律 [预期效应] |
| 疾病注释模块 | 人工整理 Mediator 亚基相关人类疾病 | 连接基础研究与临床 | 输入：8525 篇文献；输出：疾病-亚基关联 | Methods 2.1 节；Case study II | 预期影响：数据库临床转化价值降低 [预期效应] |
| Web 检索界面 | 提供多级检索与浏览 | 数据库可用性核心 | 输入：用户查询；输出：结果表格 + 详情页 | Results 3 节 | 预期影响：数据库无法使用 [预期效应] |
| 内置分析工具 | BLAST/IUPred/MoRF-CHiBi 在线分析 | 用户可分析自有序列 | 输入：用户序列；输出：比对/无序/MoRF 结果 | Results 3 节 Tools 部分 | 预期影响：降低数据库实用性 [预期效应] |

---

## 09 关键公式符号

本文为数据库资源型论文，**无核心数学公式**。涉及的关键计算工具与参数如下：

| 工具/概念 | 符号/参数 | 含义 | 用途 | 来源 |
|-----------|-----------|------|------|------|
| HMMER 搜索 | E-value ≤ 0.01 | 期望值阈值，控制假阳性率 | 序列同源鉴定 | Methods 2.1 节 |
| IUPred 无序阈值 | 分数 > 0.5 | 残基被判定为无序的分数阈值 | IDR 定义 | Methods 2.2 节 |
| IDR 最小长度 | ≥ 30 aa | 连续无序残基的最小长度 | IDR 区间定义 | Methods 2.2 节 |
| MoRF-CHiBi 阈值 | 分数 ≥ 0.72 | MoRF 预测分数阈值 | MoRF 定义 | Methods 2.2 节 |
| MoRF 最小长度 | ≥ 5 aa | 连续 MoRF 残基最小长度 | MoRF 区间定义 | Methods 2.2 节 |
| IQR 离群值检测 | Q1 - 1.5×IQR, Q3 + 1.5×IQR | 四分位距法识别异常序列长度 | 排除极端长度序列 | Methods 2.2 节 |

---

## 10 实验设计与证据链

### 数据集/群体/规模/指标/基线/预算/评测协议

- **数据集**：UniProtKB/SwissProt 已注释 Mediator 亚基序列（种子）；UniProt 全库（搜索目标）；TAIR（拟南芥）、Oryzabase（水稻）植物序列
- **规模**：最终数据库含 33,971 条序列（12,531 后生动物 / 9,593 真菌 / 11,545 植物），覆盖 1,113 个物种（331 后生动物 / 658 真菌 / 123 植物）
- **指标**：无定量评测指标（数据库构建）；验证方式为 Case study 展示
- **基线**：无（首个 Mediator 专用数据库）
- **预算/计算资源**：未提供
- **评测协议**：通过两个 Case study 展示数据库功能：(1) "ATP binding" 功能检索；(2) 癌症相关亚基检索

### 实验表格

| 实验 | 检验的 Claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|-----------|-----------------|------|
| HMM 谱跨 kingdom 搜索 | HMM 方法可鉴定远缘物种 Mediator 亚基 | 3 个 kingdom 分别建谱，E-value ≤ 0.01 | 获得 33,971 条序列，覆盖 1,113 物种 | HMM 方法有效扩展了 Mediator 亚基鉴定范围 | 未与 BLAST 等方法做系统对比，无法证明 HMM 优于其他方法 | Results 2.1 节 |
| IDR 跨 kingdom 保守性分析 | Mediator 亚基 IDR 位置在进化中保守 | 计算各亚基平均无序度，按 kingdom 分组比较 | Med15、Med19 在所有 kingdom 中无序度 >0.5；多个亚基 IDR 位置保守 | IDR 位置是 Mediator 的功能约束特征 | 未做统计显著性检验；保守性判断基于目视比较 | Results 2.2 节；图 1-2 |
| PTM-IDR 共定位分析 | PTM 位点富集于 IDR 内 | 8 个模式物种，4 类 PTM 预测 | 甲基化位点 >90% 位于 IDR（C. elegans, D. melanogaster）；植物中 85-98% | PTM 主要通过修饰 IDR 调控 Mediator 功能 | 预测工具未实验验证；仅 8 个物种 | Results 2.4 节；图 3 |
| Case study I: "ATP binding" 检索 | 数据库可按功能检索亚基 | Global Search 输入 "ATP binding" | 返回相关亚基列表；CDK8 和 Med15 为三 kingdom 共有 | 数据库支持跨 kingdom 功能比较 | 检索结果未与文献系统验证 | Results 3.1 节；图 4 |
| Case study II: 癌症关联检索 | 数据库可关联疾病与亚基 | 检索 5 种癌症类型 | CDK8 与全部 5 种癌症相关；Med12 与 4 种 | 数据库支持疾病-亚基关联分析 | 疾病关联来自文献人工整理，可能存在偏倚 | Results 3.2 节；图 5 |

---

## 11 结论正确解读

- **任务范围**：本文是**数据库构建**工作，而非机制研究。其核心产出是 Mediator 亚基序列的整合资源，附带描述性统计分析。
- **oracle/真值输入**：种子序列来自 SwissProt 已注释亚基（人工验证）；疾病注释来自人工文献整理（8525 篇）。
- **端到端状态**：数据库已完成并上线（www.nipgr.ac.in/MedProDB），但**未提供**数据库使用统计、用户反馈或第三方验证数据。
- **算力成本**：未提供。
- **历史数据依赖**：依赖 UniProt 数据库版本（具体版本号未提供）；HMM 谱基于当前已知亚基构建，新亚基发现需更新。
- **模型依赖**：IDR 预测依赖 IUPred 的算法假设（基于能量模型）；MoRF 预测依赖 MoRF-CHiBi 的训练数据。
- **最难情形**：植物 Mediator 亚基鉴定（亚基组成争议大）；远缘物种同源物识别（序列相似性极低）。
- **群体/领域边界**：结论仅适用于 Mediator 蛋白家族；IDR 保守性规律是否适用于其他复合物未验证。
- **不确定性**：IDR/MoRF 预测均为计算预测，缺乏实验验证；PTM 预测未与实验数据交叉验证。

**有边界的复述**：本文构建了覆盖 1,113 个物种的 Mediator 蛋白序列数据库，计算预测显示 Med15/Med19 为全局高无序亚基，IDR 位置在 kingdom 内保守，且 PTM 位点富集于 IDR 内——这些结论基于计算预测，需实验验证，且仅适用于 Mediator 家族。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据库需持续更新 | 新序列不断上传至公共数据库 | "We will keep on identifying putative Mediator subunits, generate all the necessary information, and upload them at MedProDB" | Future extensions 节 |
| 注释需持续人工维护 | 基于文献的疾病/功能注释可能过时 | "We will continuously curate Mediator protein information based on published literature" | Future extensions 节 |
| 分析工具需扩展 | 当前仅提供 BLAST/IUPred/MoRF-CHiBi | "We will incorporate visualization and analysis tools to the MedProDB" | Future extensions 节 |
| 植物 Mediator 亚基鉴定存在争议 | 不同实验研究对亚基组成结论不同 | 未明确提及（隐含通过数据库整合解决） | Results 2.1 节 |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|-------------------|----------|----------|------|
| IDR 保守性分析基于 IUPred 单一工具 | IUPred 的算法偏差可能影响结论；不同 IDR 预测器结果差异大 | IDR 保守性是本文核心发现之一，工具选择直接影响结论可靠性 | 使用 2-3 种独立 IDR 预测器（如 ESpritz、DISOPRED3）交叉验证 | Methods 2.2 节仅提及 IUPred |
| "保守 IDR"定义模糊 | 仅基于"≥70% 物种在同一区域有 IDR"，未考虑 IDR 边界偏移 | 保守性结论的稳健性存疑 | 定义更严格的保守性指标（如位置偏移容忍度、长度重叠比例） | Results 2.2 节 |
| PTM 预测未实验验证 | 计算预测的 PTM 位点假阳性率高；未与 PhosphoSitePlus 等实验数据库交叉验证 | PTM-IDR 共定位结论可能被高估 | 与实验验证的 PTM 数据库比对，或对关键位点进行突变验证 | Results 2.4 节 |
| 疾病注释仅限人类 | Mediator 亚基在模式生物中的疾病关联未覆盖 | 限制了数据库在非人类疾病模型研究中的价值 | 扩展至小鼠、斑马鱼等模式生物疾病注释 | Methods 2.1 节 |
| 未提供数据库使用统计 | 无法评估数据库实际使用情况和影响力 | 资源型论文的价值需使用数据支撑 | 提供访问量、下载量、引用情况 | 全文未提及 |
| 与 AlphaFold 结构预测未整合 | 未提供 Mediator 亚基的预测结构或结构相关注释 | 结构信息对理解 IDR 介导互作至关重要 | 整合 AlphaFold 预测结构或实验结构 | 全文未提及 |
| 未提供 IDR 序列本体数据下载 | 用户无法直接获取 IDR 区间序列进行下游分析 | 降低数据可重用性 | 提供 FASTA 格式的 IDR 序列下载 | Results 3 节未提及 |

---

## 14 学到什么

> **Agent 提炼的知识候选**

1. **无序模式保守性分析框架**：本文展示了"序列不保守但无序倾向谱保守"的分析方法——将蛋白按 kingdom 分组，计算各亚基平均无序度，比较 IDR 位置分布。此方法可直接迁移至其他 IDP/IDR 富集蛋白家族（如转录因子、剪接因子）的跨物种无序性分析。

2. **IDR-MoRF-PTM 三位一体注释流程**：本文建立了"IDR 预测（IUPred）→ MoRF 预测（MoRF-CHiBi）→ PTM 预测与共定位统计"的整合分析流水线。该流程可复用于构建其他 IDR 介导互作蛋白的数据库或特征分析。

3. **HMM 谱分 kingdom 构建策略**：本文按后生动物/真菌/植物分别构建 HMM 谱，而非统一建谱，有效提高了远缘物种同源物识别的灵敏度。此策略可迁移至其他保守蛋白复合物的跨物种鉴定。

4. **数据库功能设计模式**：Global/Simple/Advanced 三级检索 + Browse 分类 + 内置分析工具（BLAST/IUPred/MoRF-CHiBi）的架构，是 IDR 相关蛋白数据库的可用模板。

5. **Med15/Med19 作为无序枢纽的验证**：本文独立验证了 Med15（尾模块）和 Med19（头模块）在所有 kingdom 中平均无序度 >0.5，与已知的"Med15 为多互作伴侣"功能一致。这为以 Med15/Med19 为靶点的 IDR 介导互作研究提供了序列基础。

6. **PTM 富集于 IDR 的定量证据**：本文提供了 Mediator 亚基中 PTM 位点与 IDR 共定位的定量数据（如植物中 85-98% 甲基化位点位于 IDR），为"无序区域是 PTM 调控互作的热点"这一假说提供了家族水平的证据。

7. **跨 kingdom 保守 IDR 列表**：本文鉴定的 8 个具有保守 IDR 的 Mediator 亚基（Med4、Med6、Med8、Med9、Med15、Med19、Med31、CDK8）可作为 IDR 介导互作研究的候选靶标。

---

## 15 与已有知识连接

1. **Boija et al. 2018, Science**：证明转录凝聚体（transcriptional condensates）由激活因子 IDR 与 Mediator 共定位形成。本文提供的 Mediator 亚基 IDR 注释为该模型提供了系统序列证据——Med15 等亚基的保守 IDR 正是凝聚体形成的结构基础。

2. **Sabari et al. 2018, Science**：证明超级增强子区域 Mediator 与 BRD4 共凝聚。本文的 Mediator IDR 数据可支撑"Mediator 通过 IDR 介导相分离参与增强子-启动子互作"的机制研究。

3. **Bourbon 2008, Nucleic Acids Research**：后生动物 Mediator 亚基的系统鉴定。本文在此基础上扩展至真菌和植物，并新增 IDR/MoRF/PTM 注释。

4. **Dosztányi 等 IUPred 系列工作**：本文使用 IUPred 进行 IDR 预测，与 IDP 领域标准工具链一致。

5. **Mészáros et al. 2018, Nucleic Acids Research（MoRF-CHiBi）**：本文使用 MoRF-CHiBi 预测 MoRF，该工具是 IDR 内互作位点预测的代表性方法。

6. **Guruprasad et al. 1990, Protein Engineering**：本文使用其不稳定指数算法，为蛋白稳定性预测的经典方法。

7. **与 AlphaFold 的关联 [Analysis]**：本文未整合结构预测，但 Mediator 亚基的 IDR 注释可作为 AlphaFold 预测的验证集——IDR 区域应表现为低 pLDDT 分数。未来可将 MedProDB 的 IDR 注释与 AlphaFold 结构数据库（AlphaFold DB）交叉验证。

8. **与相分离预测工具的关联 [Analysis]**：本文的 IDR 序列数据可直接输入 catGRANULE、PSPredictor 等相分离预测工具，用于评估 Mediator 亚基的相分离倾向。

---

## 16 研究想法

> **Agent 生成的研究候选**

### 候选 1：基于 MedProDB 的 Mediator 亚基相分离倾向系统预测
- **来源**：本文提供 33,971 条 Mediator 序列及 IDR 注释，但未进行相分离预测
- **假设**：Mediator 亚基中，已知参与转录凝聚体的亚基（Med15、Med19 等）应具有显著高于其他亚基的相分离倾向分数
- **方法**：对 MedProDB 全部序列运行 catGRANULE、PSPredictor、FuzDrop 等相分离预测工具，比较各亚基、各模块的相分离倾向分布；与已知凝聚体蛋白数据库（如 PhaSepDB）交叉比对
- **验证**：选取高相分离倾向的 Mediator 亚基 IDR，进行体外相分离实验（如液滴形成显微镜观察）或细胞成像验证
- **创新点**：首次系统评估 Mediator 全家族的相分离倾向，建立"Mediator 亚基相分离图谱"

### 候选 2：Mediator 亚基 IDR 的跨 kingdom 共进化分析
- **来源**：本文发现 IDR 位置保守但序列不保守
- **假设**：Mediator 亚基 IDR 的保守位置对应功能关键区域，其序列快速进化可能驱动物种特异的转录调控
- **方法**：提取 MedProDB 中保守 IDR 区域，进行序列熵分析、共进化分析（EVcouplings）；将保守 IDR 与已知互作界面（来自 PDB 或 AlphaFold 多聚体预测）比对
- **验证**：对高序列变异但位置保守的 IDR 进行功能实验（如嵌合体替换实验）
- **创新点**：将"无序区域位置保守性"与"序列快速进化"结合，提出 Mediator 功能多样性的进化机制

### 候选 3：基于深度学习的 Mediator-IDR 互作伴侣预测模型
- **来源**：本文提供 Mediator 亚基 IDR/MoRF 注释，但未涉及互作预测
- **假设**：Mediator 亚基的 MoRF 序列特征可用于预测其互作伴侣（转录因子、染色质修饰因子等）
- **方法**：以 MedProDB 的 MoRF 注释为训练数据，结合已知 Mediator 互作网络（BioGRID、IntAct），训练图神经网络或 Transformer 模型预测 Mediator-IDR 介导的互作；与 AlphaFold-Multimer 预测结果对比
- **验证**：对预测的新互作对进行 Co-IP 或 MST 实验验证
- **创新点**：首个针对 Mediator 复合物的 IDR 互作预测模型，整合序列特征与互作网络

### 候选 4：Mediator 亚基 IDR 的 PTM 调控互作动态模型
- **来源**：本文发现 PTM 位点富集于 IDR/MoRF 内
- **假设**：Mediator 亚基 IDR 内的 PTM 通过改变无序区域构象动态，调控其与转录因子的互作亲和力
- **方法**：选取 Med15 或 Med19 的 IDR，进行分子动力学（MD）模拟（如 CAMPARI、ABSINTH 等 IDP 专用力场），比较磷酸化/乙酰化修饰前后的构象系综差异；结合 NMR 或 SAXS 实验验证
- **验证**：对关键 PTM 位点进行突变，检测与已知互作伴侣的结合变化
- **创新点**：将 MedProDB 的静态 PTM 注释与动态构象模拟结合，建立"PTM-IDR 构象-互作"的机制模型

### 候选 5：植物 Mediator 亚基 IDR 与免疫信号互作网络
- **来源**：本文包含植物 Mediator 亚基，但未深入分析植物特异 IDR
- **假设**：植物特有 Mediator 亚基（如 Med34-37）的 IDR 可能介导植物免疫信号通路的特异互作
- **方法**：提取植物特异 Mediator 亚基的 IDR，与植物免疫相关蛋白（NLR、MAPK 等）进行互作预测；结合植物互作组数据（如 BioGRID 植物数据）
- **验证**：对候选互作对进行酵母双杂交或 BiFC 验证
- **创新点**：将 MedProDB 资源拓展至植物免疫研究，填补植物 Mediator-IDR 互作研究空白

### 候选 6：MedProDB 与 AlphaFold 结构注释的整合数据库升级
- **来源**：本文未整合结构信息
- **假设**：将 AlphaFold 预测结构与 MedProDB 的 IDR/MoRF 注释整合，可提供更全面的 Mediator 结构-无序-互作图谱
- **方法**：对 MedProDB 全部序列运行 AlphaFold2/3 预测，计算 pLDDT 与 IDR 注释的一致性；标注 MoRF 区域在预测结构中的位置；开发可视化界面展示结构-无序-互作信息
- **验证**：与已知实验结构（PDB 中 Mediator 亚基结构）比对，评估预测质量
- **创新点**：首个整合 Mediator 序列-无序-结构-互作的多维数据库，为 AI 驱动的 Mediator 研究提供基础设施