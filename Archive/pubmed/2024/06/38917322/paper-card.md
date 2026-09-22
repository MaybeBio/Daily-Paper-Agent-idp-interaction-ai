## 01 基本信息

- **标题**: Refining the pool of RNA-binding domains advances the classification and prediction of RNA-binding proteins
- **作者与单位**: Wassmer, Elsa; Koppany, Gergely; Hermes, Malte; Diederichs, Sven; Caudron-Herger, Maiwen（德国癌症研究中心 DKFZ）
- **期刊/预印本平台**: Nucleic Acids Research
- **年份**: 2024
- **论文类型**: 数据库/生物信息学分析
- **领域**: RNA结合蛋白（RBP）分类与预测
- **关键词**: RNA-binding proteins, RNA-binding domains, intrinsically disordered regions, RBP2GO, prediction
- **DOI/arXiv 号**: 10.1093/nar/gkae536
- **代码**: 未提供（脚本可从 RBP2GO 数据库下载）
- **数据**: RBP2GO 2.0 Beta（https://RBP2GO-2-Beta.dkfz.de），包含 176,896 个蛋白质、13 个物种、103 个数据集
- **阅读日期**: 未提供
- **在课题方向中的位置**: 该文系统分析了 RBP 中 RNA 结合结构域（RBD）与无序区（IDR）的共现关系，发现 IDR 与 RBD 强正相关，但 IDR 本身不是独立的强 RBP 预测指标。对 IDP/IDR × 蛋白互作 × AI 预测方向提供了重要的基准数据和特征工程思路。

## 02 一句话总结

通过整合 13 个物种的泛物种 RBP 数据库（RBP2GO），该研究筛选出 977 个在 RBP 中富集的 RNA 结合结构域（RBD）和 672 个 RNA 相关蛋白家族（Rfam ID），发现 IDR 与 RBD 强正相关但 IDR 本身不是独立预测因子，并据此构建了 RBP2GO 复合评分，得到 2018 个人类高置信度 RBP 列表。

## 03 研究问题

- **具体问题**: 如何利用泛物种的蛋白质组学 RBP 筛选数据来精炼 RNA 结合结构域（RBD）的列表，并基于此改进 RBP 的预测和分类？
- **为什么重要**: RBP 在转录、剪接、翻译、降解等 RNA 代谢过程中发挥核心作用，与神经退行性疾病和癌症密切相关。准确预测 RBP 对于理解疾病机制和发现新药靶点至关重要。
- **现有方法不足**: 已有 RBP 预测主要依赖序列特征（如 RBD 的存在），但 (1) 不同物种的 RBP 筛选数据覆盖度差异大；(2) 大量 RBP 缺乏已知 RBD，预测精度有限；(3) 现有 RBP2GO 评分未整合结构域信息。
- **精确的 Can 问题**: Can a refined set of RNA-binding domains, selected by enrichment analysis across 13 species, combined with IDR content, improve the prediction and classification of RNA-binding proteins?

## 04 背景与发展脉络

*注：以下脉络基于本文框架，未经外部系统核验。*

1. **实验方法时代（~2012-2018）**：通过 UV 交联 + oligo-dT 纯化 + 质谱（如 mRNA 互作组捕获）鉴定 RBP。代表方法包括 mRNA interactome capture（7-12）、有机相分离（16-18）、蔗糖梯度分离（19-21）。局限：不同实验室、不同细胞类型的结果重叠度低。
2. **数据库整合时代（2018-2022）**：RBP2GO 数据库（22）整合了 103 个数据集、22,554 个 RBP 候选，提供 RBP2GO 评分。局限：评分仅基于实验检测次数和蛋白互作网络，未整合结构域信息。
3. **序列特征预测时代（当前）**：利用 RBD 列表（8,13,29）和 InterPro 数据库进行序列特征预测。局限：RBD 列表来源不一，未经过系统筛选；IDR 的作用未被系统评估。
4. **本文位置**：在数据库整合的基础上，通过富集分析精炼 RBD 列表，系统评估 IDR 与 RBD 的关系，构建复合评分，实现跨物种的 RBP 预测。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| RBP 候选列表可靠性低 | 不同研究间重叠度差，许多候选未被重复验证 | 实验方法差异、细胞类型差异、质谱检测灵敏度限制 | 引言部分；图 2A 显示不同物种 RBD 分布差异大 |
| RBD 列表来源混杂 | 不同文献和数据库的 RBD 定义不一致，包含大量非特异性结构域 | 缺乏统一的筛选标准 | 方法部分：整合 3 个文献来源 + InterPro 数据库，初始 2712 个 ID |
| 大量 RBP 缺乏已知 RBD | 人类中 70% 的 RBP 不含已知 RBD | RBD 定义不完整，或存在非经典 RNA 结合模式 | 图 2C；Supplementary Figure S4B |
| IDR 的作用不明确 | IDR 在 RBP 中富集，但能否作为独立预测因子未知 | IDR 与 RBD 共现，难以区分独立贡献 | 图 5A；Supplementary Figure S6-S7 |
| 低表达蛋白难以检测 | 非 RBP 组表达量显著低于 RBP 组 | 质谱检测存在灵敏度下限 | 图 2E；Supplementary Figure S2 |
| 跨物种预测困难 | 少研究物种的 RBP 鉴定率极低 | 实验数据覆盖不足 | 图 2A-B；图 6A |

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| RBP 候选列表可靠性低 | 不同研究间重叠度差，许多候选未被重复验证 | 实验方法差异、细胞类型差异、质谱检测灵敏度限制 | 引言部分；图 2A 显示不同物种 RBD 分布差异大 |
| RBD 列表来源混杂 | 不同文献和数据库的 RBD 定义不一致，包含大量非特异性结构域 | 缺乏统一的筛选标准 | 方法部分：整合 3 个文献来源 + InterPro 数据库，初始 2712 个 ID |
| 大量 RBP 缺乏已知 RBD | 人类中 70% 的 RBP 不含已知 RBD | RBD 定义不完整，或存在非经典 RNA 结合模式 | 图 2C；Supplementary Figure S4B |
| IDR 的作用不明确 | IDR 在 RBP 中富集，但能否作为独立预测因子未知 | IDR 与 RBD 共现，难以区分独立贡献 | 图 5A；Supplementary Figure S6-S7 |
| 低表达蛋白难以检测 | 非 RBP 组表达量显著低于 RBP 组 | 质谱检测存在灵敏度下限 | 图 2E；Supplementary Figure S2 |
| 跨物种预测困难 | 少研究物种的 RBP 鉴定率极低 | 实验数据覆盖不足 | 图 2A-B；图 6A |

## 06 核心思想

1. **表面方法**：整合 13 个物种的 RBP 筛选数据，通过三步富集分析（以人类为主，逐步扩展到小鼠、酵母、果蝇及其他物种）筛选出 977 个 RBD 和 672 个 Rfam ID；分析 IDR 含量与 RBD 的关系；构建包含 RBD/Rfam 信息的复合评分。

2. **核心洞察**：
   - RBD 的存在是 RBP 的强预测因子，但 IDR 本身不是独立的强预测因子——IDR 的富集主要源于与 RBD 的共现。
   - 通过富集分析可以系统性地精炼 RBD 列表，并发现新的候选 RBD（如 Armadillo repeat）。
   - 复合评分（整合实验检测、互作网络、结构域信息）比单一指标更能有效区分 RBP 与非 RBP。

3. **可能的普适教训** [Analysis]：
   - 在无序蛋白/相分离研究中，IDR 的"存在"不等于"功能"——需要区分 IDR 的独立贡献与共现效应。这对 IDP 介导的蛋白互作研究有直接启示：不能仅凭 IDR 含量预测互作能力，需结合具体序列特征（如 RGG 重复、电荷分布）。
   - 跨物种的富集分析策略可迁移到 IDP/IDR 功能结构域的鉴定中：通过比较不同物种中已知功能蛋白的序列特征，可以精炼功能相关序列模式。

## 07 方法总览

- **输入**：RBP2GO 数据库（13 个物种、103 个数据集、176,896 个蛋白质）；InterPro 数据库（结构域注释）；MobiDB 数据库（IDR 预测）；UniProt（蛋白质序列和注释）
- **输出**：977 个精选 RBD；672 个精选 Rfam ID；15 个新预测 RBD；2018 个人类高置信度 RBP 列表；更新版 RBP2GO 数据库
- **模块**：
  1. RBD 候选收集与整合（文献 + InterPro）
  2. 三步富集筛选（人类 → 模式物种 → 其他物种）
  3. IDR 含量分析（MobiDB-lite）
  4. LCR 频率和氨基酸组成分析
  5. 新 RBD 预测（基于高评分 RBP 中富集的结构域）
  6. 复合评分构建（随机森林加权）
- **训练**：随机森林算法用于确定三个评分组件的权重（基于三个独立 RBP 数据集）
- **反馈回路**：新 RBD 预测结果通过 RNA 结合肽段数据验证
- **假设**：在多个物种中一致富集于 RBP 的结构域更可能是真正的 RBD；IDR 与 RBD 的共现反映协同功能

**文字流程**：从 RBP2GO 数据库获取 13 个物种的 RBP/非 RBP 分类 → 整合文献和 InterPro 的 RBD 候选列表 → 在人类中筛选富集的结构域 → 扩展到其他物种验证 → 分析 IDR 含量与 RBD 的关系 → 在无 RBD 的高评分 RBP 中预测新 RBD → 用 RNA 结合肽段验证 → 构建复合评分 → 生成高置信度 RBP 列表 → 整合到数据库。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| RBD 候选整合 | 合并文献和 InterPro 的 RBD 列表 | 单一来源不完整 | 输入：3 个文献列表 + InterPro 查询；输出：2712 个唯一 ID | 方法部分 | 预期：遗漏非经典 RBD |
| 三步富集筛选 | 按物种研究深度分层筛选 RBD | 不同物种数据量差异大 | 输入：RBP/非 RBP 分类 + RBD 注释；输出：977 个精选 RBD | 图 1A-B；方法部分 | 预期：保留更多假阳性 RBD |
| IDR 含量分析 | 比较 RBP 与非 RBP 的 IDR 含量 | 评估 IDR 作为预测因子的价值 | 输入：MobiDB-lite 预测；输出：IDR 分数分布 | 图 5A；Supplementary Figure S6-S7 | 预期：无法评估 IDR 与 RBD 的共现关系 |
| LCR 分析 | 分析低复杂度区域的氨基酸组成 | 识别特定序列模式 | 输入：UniProt 序列；输出：LCR 频率和组成 | 图 5B；Supplementary Figure S8 | 预期：无法区分特定 LCR 类型（如 RGG）的贡献 |
| 新 RBD 预测 | 在无 RBD 的高评分 RBP 中寻找富集结构域 | 发现非经典 RBD | 输入：935 个高评分无 RBD RBP；输出：15 个候选 RBD | 图 7A-E；Supplementary Table S8 | 预期：无法扩展 RBD 库 |
| 肽段验证 | 用 RNA 结合肽段数据验证新 RBD | 提供实验证据 | 输入：RNA 结合肽段数据集；输出：验证统计 | 图 7F-G | 预期：新 RBD 缺乏实验支持 |
| 复合评分 | 整合多源信息评估 RBP 可能性 | 单一指标不够准确 | 输入：RBP2GO 评分、RBD/Rfam 信息；输出：0-100 复合评分 | 图 8A-B；Supplementary Figure S9-S12 | 预期：预测精度下降 |

## 09 关键公式符号

**复合评分（Composite Score）**：

Composite Score = w₁ × Component₁ + w₂ × Component₂ + w₃ × Component₃

- Component₁：基于 Listing Count 的标准化评分（0-50 分）
- Component₂：基于 STRING 互作网络 top-10 伙伴平均 Listing Count 的评分（0-25 分）
- Component₃：基于 RBD/Rfam 质量因子的评分（0-25 分）
- w₁, w₂, w₃：由随机森林算法确定的权重

**富集筛选标准**：
- 人类（Selection 1）：RBP 中 hits > 非 RBP 中 hits
- 模式物种（Selection 2）：在 ≥50% 的物种中富集
- 其他物种（Selection 3）：在 ≥50% 的剩余物种中富集

**肽段重叠计算**：
- 重叠比例 = 与 RBD 重叠的肽段数 / 该结构域相关蛋白的总肽段数
- 归一化：除以结构域在蛋白序列中的覆盖比例

## 10 实验设计与证据链

**数据集与资源**：
- RBP2GO 数据库：13 个物种、103 个数据集、176,896 个蛋白质
- 人类数据集：43 个 RBP 数据集（最大覆盖）
- 验证数据集：RNA 结合肽段数据（来自 4 个独立研究）
- 比较基准：HydRA 分类（49）、RBPbase superset（3）

**指标**：
- 富集倍数（fold enrichment）
- Fisher 精确检验 + FDR 校正
- 复合评分分布比较
- 与 HydRA/RBPbase 的重叠率

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|-----------------|------|
| RBD 富集筛选 | 精选 RBD 在 RBP 中富集 | 977 精选 RBD vs 未精选 RBD；RBP vs 非 RBP | 精选 RBD 蛋白的 RBP2GO 评分显著更高 | RBD 富集筛选有效 | 不能证明因果关系 | 图 1B；图 3A |
| IDR 含量比较 | RBP 比非 RBP 含更多 IDR | RBP vs 非 RBP；有/无 RBD 分层 | RBP 的 IDR 分数显著更高；但有 RBD 的蛋白 IDR 更高 | IDR 与 RBD 共现 | IDR 独立预测能力有限 | 图 5A；Supplementary Figure S6 |
| 新 RBD 预测 | 15 个候选结构域是真正的 RBD | 935 高评分无 RBD RBP vs 参考集 | 15 个结构域显著富集 | 存在非经典 RBD | 需要实验验证 | 图 7A-E |
| 肽段验证 | 新 RBD 确实结合 RNA | 新 RBD vs 非选择结构域；肽段重叠 | 新 RBD 的肽段重叠显著更高 | 新 RBD 有实验支持 | 样本量有限 | 图 7F-G |
| 复合评分验证 | 复合评分优于单一评分 | 复合评分 vs RBP2GO 评分；与 HydRA/RBPbase 比较 | 2018 个高置信度 RBP，89% 与 HydRA/RBPbase 重叠 | 复合评分有效 | 不能证明优于所有现有方法 | 图 8；Supplementary Figure S13 |
| 表达水平分析 | 非 RBP 检测不到与低表达有关 | 四组蛋白表达水平比较 | 非 RBP 组表达显著更低 | 表达水平影响检测 | 不能排除其他因素 | 图 2E |

## 11 结论正确解读

- **任务范围**：该研究是生物信息学/数据库层面的分析，不涉及湿实验验证。所有结论基于已有数据的重分析。
- **oracle/真值输入**：RBP/非 RBP 分类基于实验检测（Listing Count ≥ 1 为 RBP），这是操作定义而非生物学真值。非 RBP 可能只是未被检测到。
- **端到端状态**：从数据整合到预测模型是端到端的，但预测的 RBP 候选（特别是新 RBD）未经系统实验验证。
- **算力成本**：未报告具体算力需求，但主要为数据库查询和统计检验，计算成本低。
- **历史数据依赖**：高度依赖 RBP2GO 数据库的覆盖度和质量。少研究物种（如疟原虫、利什曼原虫）的数据可能严重不完整。
- **模型依赖**：复合评分的权重由随机森林确定，依赖训练数据集的代表性。不同物种的适用性可能不同。
- **最难情形**：无 RBD 且无已知互作伙伴的 RBP 最难预测；低表达蛋白容易被误分类为非 RBP。
- **群体/领域边界**：结论适用于原核和真核生物，但主要验证集中在人类、小鼠、酵母、果蝇。IDR 预测基于 MobiDB-lite，不同预测器可能给出不同结果。
- **不确定性**：新 RBD 的验证仅基于肽段重叠统计，未进行定向突变或结构验证。IDR 与 RBD 的因果关系未建立。

**有边界的复述**：在 RBP2GO 数据库覆盖的 13 个物种中，通过富集分析筛选出的 977 个 RBD 和 672 个 Rfam ID 能有效区分已知 RBP 与非 RBP；IDR 在 RBP 中富集但主要与 RBD 共现；基于复合评分的 2018 个人类高置信度 RBP 列表与现有数据库高度重叠，但包含约 10% 的新候选。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 非 RBP 定义不完善 | 非 RBP 可能只是未被检测到，而非真正不结合 RNA | 需要更多实验验证 | 讨论部分 |
| IDR 预测的局限性 | MobiDB-lite 预测可能不准确，且 IDR 亚型（如 RGG、RS 重复）未细分 | 未来可纳入更详细的 IDR 亚型分析 | 讨论部分 |
| 新 RBD 验证不足 | 仅通过肽段重叠统计验证，缺乏功能实验 | 需要湿实验验证 | 讨论部分 |
| 物种覆盖不均 | 少研究物种的数据可能不完整 | 需要更多物种的 RBP 筛选数据 | 讨论部分 |
| 复合评分依赖训练数据 | 权重由随机森林确定，可能偏向数据丰富的物种 | 需要更多独立验证 | 方法部分 |

## 13 与已有知识的联系

- **相似工作**：与 Caudron-Herger et al. (2019) 的 RBP2GO 原始版本（22）一脉相承，但新增了结构域层面的分析。与 Hentze 团队的 mRNA interactome capture 系列工作（7-12）互补。
- **直接相关**：与 Castello et al. (2016) 关于非经典 RBP 的综述（30）直接相关——本文为"非经典 RBP 如何结合 RNA"提供了结构域层面的线索。
- **方法可迁移**：三步富集筛选策略可迁移到 IDP/IDR 功能结构域的鉴定。对于无序蛋白研究，可借鉴其"在已知功能蛋白中富集序列特征"的思路。
- **冲突/张力**：本文发现 IDR 不是独立预测因子，与部分文献强调 IDR 在 RBP 中的重要性（如 74,82,83）存在张力。但作者指出 IDR 与 RBD 的共现可能反映协同功能，而非 IDR 独立驱动 RNA 结合。
- **对 IDP/IDR × 蛋白互作 × AI 的启示**：
  1. 特征工程：IDR 含量单独作为预测特征可能不够，需与结构域信息组合。
  2. 数据资源：RBP2GO 2.0 可作为 IDP/IDR 相关 RBP 预测的训练/验证数据。
  3. 方法学：跨物种富集分析可迁移到 IDP 功能序列模式的发现。

## 14 学到什么

**Agent 提炼的知识候选**：

1. **跨物种富集筛选策略**：在 IDP/IDR 研究中，可借鉴三步筛选法（先在高覆盖物种中筛选，再跨物种验证），用于鉴定与相分离相关的序列模式或结构域。

2. **IDR 与结构域的共现分析**：本文的方法提示，在研究 IDR 介导的蛋白互作时，应区分 IDR 的独立贡献与共现效应。可迁移到相分离预测：IDR 的相分离能力可能依赖于邻近的 RNA 结合结构域。

3. **复合评分的构建思路**：将实验检测、互作网络、序列特征三个维度整合为复合评分，可迁移到 IDP/IDR 介导互作的打分函数设计。

4. **"RBP aspirant"概念**：将"有结构域证据但未被实验检测到"的蛋白定义为候选，这一思路可迁移到相分离蛋白的预测——将"有 IDR 且互作网络支持"的蛋白列为相分离候选。

5. **负样本的重要性**：本文强调非 RBP 的定义影响预测性能。在 IDP/IDR 相分离预测中，负样本（非相分离蛋白）的定义同样关键。

6. **肽段重叠验证方法**：用 RNA 结合肽段数据验证新 RBD 的方法，可迁移到 IDR 介导互作区域的验证——用交联肽段数据验证预测的互作区域。

## 15 研究想法

**Agent 生成的研究候选**：

1. **候选名称**: IDR-RBD 共现网络分析用于相分离蛋白预测
   - **来源局限/观察**: 本文发现 IDR 与 RBD 强共现，但未分析共现的拓扑模式（如 IDR 在 RBD 侧翼 vs 远端）
   - **核心假设**: IDR 与 RBD 的相对位置（侧翼、间隔、重叠）影响 RNA 结合的亲和力和特异性，进而影响相分离能力
   - **初步方法**: 从 RBP2GO 2.0 提取含 RBD+IDR 的蛋白，计算 IDR-RBD 距离分布，聚类分析共现模式，与已知相分离蛋白数据库（如 PhaSepDB）交叉验证
   - **验证方式**: 比较不同共现模式的蛋白在相分离数据库中的富集程度；用 AlphaFold 预测代表性蛋白的结构，检查 IDR-RBD 空间关系
   - **创新状态**: unverified

2. **候选名称**: 基于 RBP2GO 复合评分的相分离蛋白预测器
   - **来源局限/观察**: 本文的复合评分仅用于 RBP 分类，但相分离蛋白与 RBP 高度重叠
   - **核心假设**: RBP2GO 复合评分与相分离能力正相关，可作为相分离蛋白预测的辅助特征
   - **初步方法**: 将 RBP2GO 复合评分与已知相分离特征（IDR 长度、电荷分布、RGG 重复数）结合，训练分类器区分相分离/非相分离蛋白
   - **验证方式**: 在独立数据集上评估 AUC；对高评分但未报道的相分离候选进行文献验证
   - **创新状态**: unverified

3. **候选名称**: 无序区 RNA 结合基序的从头预测
   - **来源局限/观察**: 本文预测的新 RBD 中，部分位于 IDR 内，但未系统分析 IDR 内的 RNA 结合基序
   - **核心假设**: IDR 内存在短线性 RNA 结合基序（类似 SLiM），可通过序列模式挖掘发现
   - **初步方法**: 从 RNA 结合肽段数据中提取 IDR 内的结合肽段，进行 motif 发现（如 MEME），构建基序数据库，用深度学习（如 CNN）预测 IDR 内的 RNA 结合位点
   - **验证方式**: 交叉验证；对预测的基序进行突变分析（文献验证）
   - **创新状态**: unverified

4. **候选名称**: 相分离驱动的 RNA 结合特异性：IDR 介导的 multi-valent 互作模型
   - **来源局限/观察**: 本文发现 RBD 数量与 RBP2GO 评分正相关，但未分析 IDR 介导的多价互作
   - **核心假设**: IDR 通过多价弱相互作用增强 RBD 的 RNA 结合特异性，尤其在相分离凝聚体中
   - **初步方法**: 构建含 RBD+IDR 的蛋白序列数据集，用分子模拟（粗粒化 MD）模拟 IDR-RNA 相互作用，分析 IDR 对 RBD-RNA 结合自由能的贡献
   - **验证方式**: 模拟预测与实验数据（如 SMARTER 或 eCLIP）对比
   - **创新状态**: unverified

5. **候选名称**: 低表达 RBP 的检测偏差校正模型
   - **来源局限/观察**: 本文指出非 RBP 可能只是低表达未被检测，但未建立校正模型
   - **核心假设**: 结合表达量数据可以校正 RBP 检测偏差，提高预测准确性
   - **初步方法**: 整合 RBP2GO 与人类蛋白表达图谱（如 Human Protein Atlas），建立考虑表达量的贝叶斯模型预测 RBP 概率
   - **验证方式**: 在独立数据集上比较校正前后的预测性能
   - **创新状态**: unverified

## 16 关键引用

1. **Caudron-Herger M, et al. (2019)** RBP2GO: a comprehensive pan-species database on RNA-binding proteins, their interactions and functions. Nucleic Acids Research.（本文的前身数据库）

2. **Castello A, et al. (2016)** Comprehensive identification of RNA-binding domains in human cells. Molecular Cell.（RBD 列表来源之一）

3. **Hentze MW, et al. (2018)** A brave new world of RNA-binding proteins. Nature Reviews Molecular Cell Biology.（非经典 RBP 综述）

4. **Queiroz RML, et al. (2019)** Comprehensive identification of RNA-protein interactions in any organism using orthogonal organic phase separation (OOPS). Nature Biotechnology.（RBP 筛选方法）

5. **Perez-Perri JI, et al. (2021)** The "protein-mediated" RNA world: a new era of RNA-binding protein research. Trends in Biochemical Sciences.（RBP 研究展望）

6. **Piovesan D, et al. (2021)** MobiDB: intrinsically disordered proteins in 2021. Nucleic Acids Research.（IDR 数据库来源）

7. **Blum M, et al. (2021)** InterPro in 2022. Nucleic Acids Research.（结构域数据库来源）

8. **Szklarczyk D, et al. (2021)** STRING database in 2021. Nucleic Acids Research.（互作网络来源）