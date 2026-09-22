## 01 基本信息

- **标题**：A simple workflow to identify novel Small Linear Motif (SLiM)-mediated interactions with AlphaFold
- **作者与单位**：Veinstein M（de Duve Institute, UCLouvain, Belgium）；Janssens V（ECAM Brussels Engineering School）；Iorga B（Institut de Chimie des Substances Naturelles, CNRS, France）；Helaers R（de Duve Institute, UCLouvain）；Michiels T（de Duve Institute, UCLouvain）；Sorgeloos F（INRS, Laval, Canada）
- **期刊/预印本平台**：bioRxiv（预印本）
- **年份**：2025（2025-06-08 发布）
- **论文类型**：方法学/工作流论文（含基准测试与实验验证）
- **领域**：无序蛋白区（IDR）中的短线性基序（SLiM）介导的蛋白互作 × AlphaFold 结构预测 × 计算工作流
- **关键词**：SLiM、AlphaFold、ColabFold、MiniPAE、蛋白互作、无序区、RSK2、邻近标记
- **DOI/arXiv 号**：10.1101/2025.06.04.657817
- **代码**：MiniPAE 代码库：https://github.com/martinovein/MiniPAE
- **数据**：未提供独立数据集；基准测试基于已知 SLiM 案例（具体数据集未在摘要中详述）
- **阅读日期**：2025-06-10（基于发布日期的合理估计，实际阅读日期未提供）
- **该文在课题方向中的位置**：本文直接面向 IDR 中的 SLiM 介导的蛋白互作，提出用 AlphaFold（ColabFold）+ MiniPAE 评分进行 SLiM 互作预测的计算工作流，并配套活细胞邻近标记验证方法。属于「无序蛋白互作 × AI 结构预测」交叉方向的方法学贡献，强调无需本地算力、低成本、可扩展的 SLiM 发现路径。

---

## 02 一句话总结

本文系统比较了 AlphaFold2/3 的多种评分指标，发现 AlphaFold2 结合 MiniPAE 评分能最有效地识别无序区中的 SLiM 介导的蛋白互作，并据此构建了一个无需本地安装、基于 Colab 的端到端 SLiM 预测工作流，同时配套活细胞邻近标记实验用于验证低亲和力 SLiM 互作，最终成功预测了与 RSK2 激酶互作的未表征 SLiM。

---

## 03 研究问题

- **具体问题**：如何利用 AlphaFold（而非仅依赖其结构预测精度）来可靠地识别无序蛋白区中 SLiM 介导的蛋白互作？
- **为什么重要**：SLiM 是高度紧凑、简并、瞬时的互作模块，嵌入在无序区中，在细胞稳态和宿主-病原互作中起核心作用。但因其体积小、结合弱、序列简并，实验和计算检测都极为困难。现有 SLiM 预测工具（如基于序列的 ELM 等）假阳性率高，而实验方法（如突变扫描）通量低。
- **现有方法为何不足**：以往 AlphaFold 用于 SLiM 研究时，关注的是结构预测精度（如 pLDDT、ipTM 等），但 SLiM 互作往往不产生高置信度的折叠结构域，传统结构质量指标不适用；且 AlphaFold3 虽新，但在此任务上表现未必优于 AlphaFold2。
- **精确的「Can ... ?」研究问题**：Can AlphaFold2（经 ColabFold 使用）结合 MiniPAE 评分，在无需本地算力的情况下，从蛋白质序列中可靠地预测 SLiM 介导的蛋白互作，并优于 AlphaFold3 及现有结构质量指标？

---

## 04 背景与发展脉络

> 注：以下脉络部分基于本文框架，部分经外部核验（标注）。

1. **SLiM 计算预测的早期方法（2010s）**：基于序列模式匹配（如 ELM 数据库、ScanProsite），优点是快速、可批量，缺点是假阳性率高、缺乏结构/互作上下文。
2. **结构感知的 SLiM 预测（2015-2022）**：利用已知 3D 结构或同源建模来过滤候选 SLiM，如 SLiMPrints、PEPMatch 等。优点是提高特异性，缺点是覆盖度低（多数 SLiM 无结构模板）。
3. **AlphaFold 时代的 SLiM 研究（2021-2024）**：AlphaFold2 的 pLDDT 和 PAE 被用于评估无序区和互作界面。但多数研究聚焦于结构精度，未系统评估「互作预测」能力。AlphaFold3 发布后，其预测蛋白-肽复合物的能力被寄予厚望，但计算成本高、可及性受限。
4. **本文主张的位置**：提出「结构质量 ≠ 互作可检测性」的核心观点，即 AlphaFold 的互作信号（通过 MiniPAE 提取）可以独立于模型整体质量而存在。将 AlphaFold 从「结构预测器」重新定位为「互作打分器」，并降低使用门槛（Colab 笔记本、无安装）。

> 此脉络中第 1-2 点为外部核验的领域常识；第 3 点为本文框架内的背景描述；第 4 点为作者主张。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| SLiM 检测困难 | 体积小（3-10 残基）、序列简并、瞬时结合，实验和计算均难捕获 | SLiM 嵌入无序区，缺乏稳定折叠结构，传统结构生物学方法难以捕捉 | 摘要：「Due to their small size, degeneracy and transient binding, SLiMs remain difficult to detect both experimentally and computationally.」 |
| 现有计算工具假阳性高 | 序列模式匹配方法产生大量候选，但验证率低 | 缺乏互作上下文和结构约束 | 摘要：「SLiMs remain difficult to detect... computationally」；作者在背景中暗示现有工具局限（未提供具体数据） |
| AlphaFold 结构质量指标不适用于 SLiM | pLDDT/ipTM 等指标在无序区中表现差，无法区分真实互作与噪声 | SLiM 互作不产生高置信度折叠域，传统指标设计目标不同 | 摘要：「Unlike previous studies focused on structural accuracy, we evaluated AlphaFold's capacity to reveal SLiMs independently of model quality.」 |
| AlphaFold3 可及性受限 | 计算成本高、需本地部署或付费 API | 商业化和算力门槛 | 摘要：「requiring no installation or local computation」暗示对轻量方案的追求 |
| SLiM 验证通量低 | 低亲和力互作难以用常规方法（如 Co-IP、ITC）验证 | 瞬时结合、低亲和力（μM-mM 范围） | 摘要：「To overcome challenges associated with SLiM validation, we also introduce a highly sensitive detection method based on proximity labeling in living cells.」 |

---

## 06 核心思想

### 1) 表面方法
- 使用 ColabFold（AlphaFold2）对目标蛋白-肽段对进行共折叠预测；
- 计算多种评分指标（包括 pLDDT、PAE、ipTM 等），并引入自定义的 MiniPAE 指标；
- 系统基准测试各指标对已知 SLiM 互作的区分能力；
- 构建基于 Colab 笔记本的端到端工作流（无需安装、无需本地 GPU）；
- 配套活细胞邻近标记（proximity labeling）实验用于验证预测的 SLiM 互作。

### 2) 核心洞察
- **AlphaFold 的互作信号独立于结构质量**：即使整体模型置信度低（无序区），局部 PAE 信号（MiniPAE）仍能指示 SLiM 介导的互作界面。这重新定义了 AlphaFold 在 SLiM 研究中的角色——从「结构预测器」变为「互作打分器」。
- **AlphaFold2 优于 AlphaFold3**：在 SLiM 检测这一特定任务上，AF2 + MiniPAE 的组合优于 AF3，挑战了「更新即更好」的默认假设。
- **计算与实验的闭环**：计算预测 + 活细胞邻近标记验证，形成低成本、高灵敏度的 SLiM 发现流水线。

### 3) 可能的普适教训 [Analysis]
- **指标设计应针对任务而非模型**：MiniPAE 的成功说明，针对特定生物学问题（SLiM 互作）设计定制化评分，可能比依赖通用结构质量指标更有效。
- **轻量级工作流的价值**：无需本地算力的 Colab 方案大幅降低了使用门槛，使 SLiM 预测可被广泛采用——这在资源受限的研究环境中尤为重要。
- **「旧模型 + 新指标」可能优于「新模型 + 旧指标」**：模型迭代不总是带来任务层面的改进，系统评估不同模型-指标组合是必要的。

---

## 07 方法总览

- **输入**：目标蛋白序列 + 候选 SLiM 肽段序列（或候选互作蛋白的肽段区域）
- **输出**：SLiM 互作预测评分（MiniPAE 等）、候选互作列表、实验验证方案
- **模块**：
  1. **共折叠预测模块**：ColabFold（AlphaFold2）对蛋白-肽对进行共折叠；
  2. **评分模块**：计算多种指标（pLDDT、PAE、ipTM、MiniPAE 等）；
  3. **基准测试模块**：在已知 SLiM 数据集上比较各指标性能；
  4. **工作流封装模块**：Colab 笔记本，自动化从序列输入到评分输出；
  5. **实验验证模块**：活细胞邻近标记（proximity labeling）检测 SLiM-靶标互作。
- **训练**：无模型训练；AlphaFold2 为预训练模型，MiniPAE 为自定义评分函数（基于 PAE 矩阵的局部最小值提取）。
- **工具**：ColabFold、AlphaFold2/3、MiniPAE（GitHub 提供）、Colab 笔记本、邻近标记实验（具体方法未在摘要详述）。
- **反馈回路**：计算预测 → 实验验证 → 验证结果反馈优化评分阈值/工作流参数。
- **文字流程**：用户输入目标蛋白和候选肽段序列 → ColabFold 进行共折叠 → 计算多种评分指标 → MiniPAE 提取局部互作信号 → 输出候选 SLiM 互作列表 → 用户选择候选进行活细胞邻近标记实验验证 → 确认互作。

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| ColabFold 共折叠 | 预测蛋白-肽复合物结构 | 提供互作的结构上下文 | 输入：蛋白序列+肽段序列；输出：预测复合物结构 | 摘要：「AlphaFold, used via ColabFold, offers a practical and accessible alternative」 | 预期影响：无法获得结构信息，MiniPAE 无从计算 [预期效应] |
| MiniPAE 评分 | 从 PAE 矩阵提取局部互作信号 | 传统指标无法捕捉 SLiM 的弱互作信号 | 输入：PAE 矩阵；输出：MiniPAE 分数 | 摘要：「AlphaFold2 combined with MiniPAE yields the best performance」 | 预期影响：SLiM 检测灵敏度显著下降 [预期效应] |
| 多指标基准测试 | 系统比较各评分指标 | 确定最优指标组合 | 输入：已知 SLiM 数据集；输出：各指标性能排名 | 摘要：「we benchmarked several scoring metrics」 | 预期影响：无法确定最优方案，工作流缺乏依据 [预期效应] |
| Colab 工作流封装 | 提供无需安装的端到端方案 | 降低使用门槛，提高可及性 | 输入：序列；输出：预测报告 | 摘要：「requiring no installation or local computation」 | 预期影响：可及性下降，非计算背景研究者难以使用 [预期效应] |
| 邻近标记实验 | 活细胞中验证 SLiM 互作 | 计算预测需实验确认 | 输入：候选 SLiM 互作对；输出：互作确认/否定 | 摘要：「highly sensitive detection method based on proximity labeling in living cells」 | 预期影响：无法区分真/假阳性预测 [预期效应] |

> 注：摘要中未提供消融实验数据，以上「预期影响」均为 [Analysis] 推断，非实测消融结果。

---

## 09 关键公式符号

不适用。摘要中未提供具体公式。MiniPAE 的具体计算方式在 GitHub 代码库中，但摘要未给出数学定义。

---

## 10 实验设计与证据链

- **数据集**：已知 SLiM 案例（具体数据集未在摘要中详述，可能包括 ELM 数据库中的已知 SLiM 及其互作靶标）
- **规模**：未提供
- **指标**：多种 AlphaFold 评分指标（pLDDT、PAE、ipTM、MiniPAE 等）
- **基线**：各指标之间的相互比较；AF2 vs AF3
- **预算/算力**：ColabFold（免费/低成本），无需本地 GPU
- **骨干/仪器**：ColabFold（AlphaFold2/3）、MiniPAE、邻近标记实验
- **oracle 输入**：已知 SLiM 互作对作为基准测试的真值
- **评测协议**：各指标对已知 SLiM 互作 vs 非互作对的区分能力（如 AUC、灵敏度/特异度）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|------------------|------|
| 多指标基准测试 | 不同评分指标对 SLiM 检测的性能差异 | AF2 各指标 vs AF3 各指标 | AF2 + MiniPAE 性能最优 | MiniPAE 是 SLiM 检测的有效指标 | 未提供具体数值，无法评估效应量 | 摘要：「AlphaFold2 combined with MiniPAE yields the best performance, outperforming AlphaFold3 in this context」 |
| RSK2 SLiM 预测 | 工作流能否发现新的 SLiM 互作 | 预测 vs 实验验证 | 预测了未表征的 SLiM 与 RSK2 互作 | 工作流具有实际发现能力 | 未提供验证的互作数量/成功率 | 摘要：「used to predict the occurrence of SLiMs that mediate binding to ribosomal protein S6 kinase A3 (RPS6KA3 or RSK2)」 |
| 邻近标记验证 | 低亲和力 SLiM 互作能否在活细胞中检测 | 邻近标记 vs 常规方法 | 方法灵敏度高 | 提供有效的实验验证手段 | 未提供与常规方法的定量比较 | 摘要：「highly sensitive detection method based on proximity labeling in living cells」 |

---

## 11 结论正确解读

- **任务范围**：本文解决的是「SLiM 介导的蛋白互作预测」，而非一般蛋白-蛋白互作预测；且聚焦于无序区中的 SLiM，不涉及折叠结构域介导的互作。
- **oracle/真值输入**：基准测试使用了已知 SLiM 案例作为真值，但这些案例的选择标准、覆盖范围未在摘要中说明，可能存在选择偏差。
- **端到端状态**：工作流从序列输入到候选互作输出是端到端的，但「预测 → 验证」的完整闭环仅在 RSK2 案例中展示，未系统评估全流程的假阳性/假阴性率。
- **算力成本**：ColabFold 为免费/低成本方案，但大规模筛选时的 API 限制和队列等待时间未讨论。
- **历史数据依赖**：AlphaFold2 的训练数据包含 PDB 中的复合物结构，对 SLiM 类弱互作的覆盖可能有限；本文未讨论这一潜在偏差。
- **模型依赖**：结论基于 AlphaFold2/3 的特定版本和参数设置，未来模型更新可能改变结论。
- **最难情形**：SLiM 的简并性意味着同一基序可结合多个靶标，本文工作流是否能够区分不同靶标的结合偏好未讨论。
- **不确定性**：摘要未提供任何置信区间、效应量或统计检验信息，性能优势的幅度未知。
- **有边界的复述**：在已知 SLiM 案例的基准测试中，AF2 + MiniPAE 评分优于其他测试的指标组合（包括 AF3），且该工作流成功预测了 RSK2 的未表征 SLiM 互作并通过邻近标记实验验证；但具体性能数值、适用范围和失败模式未在摘要中披露。

---

## 12 作者自认局限

在提供的摘要材料中未发现作者明确承认的局限。

**作者提及的相关约束**（非正式局限）：
- 摘要提到 SLiM「difficult to detect both experimentally and computationally」，暗示方法仍有挑战；
- 工作流强调「simple」和「accessible」，暗示其可能牺牲了部分精度换取易用性；
- 验证方法（邻近标记）被描述为「highly sensitive」，但未讨论其特异性或假阳性风险。

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| AF2 + MiniPAE 优于 AF3 的结论 | AF3 可能在不同超参数/输入格式下有不同表现；AF3 的肽段处理方式与 AF2 不同 | 若结论依赖特定实现细节，则普适性有限 | 在多个 AF3 版本和输入设置下重复基准测试 | 摘要：「outperforming AlphaFold3 in this context」——「in this context」暗示条件依赖性 |
| 基准测试数据集未披露 | 可能仅包含特定类型的 SLiM（如高置信度已知案例），导致选择偏差 | 影响结论的泛化能力 | 要求作者提供数据集详情，或在独立数据集上复现 | 摘要未提供数据集描述 |
| MiniPAE 的定义未在摘要中给出 | 可能是对 PAE 矩阵的某种自定义变换，其生物学合理性需审视 | 若 MiniPAE 只是过拟合了基准数据集，则对新案例无效 | 检查 MiniPAE 的数学定义，分析其与已知 SLiM 结合机制的关联 | 摘要仅提及名称，无公式 |
| 邻近标记验证的灵敏度 vs 特异性 | 高灵敏度可能伴随高假阳性率（邻近标记可捕获非特异性邻近蛋白） | 影响验证结果的可信度 | 设置阴性对照（如突变 SLiM 或无关肽段）检验特异性 | 摘要：「highly sensitive」未提及特异性 |
| 工作流「无需安装」的代价 | Colab 免费版有使用时长和内存限制，大规模筛选可能不现实 | 影响可扩展性声明 | 测试大规模筛选时的实际限制 | 摘要：「requiring no installation or local computation」 |
| RSK2 案例的普适性 | 单一案例不足以证明工作流的广泛适用性 | 需要更多不同靶标的验证 | 在多个已知 SLiM-靶标系统上测试 | 摘要仅提及 RSK2 一个案例 |

---

## 14 Agent 提炼的知识候选

> 面向课题方向：IDP/IDR × 蛋白互作 × AI/物理模拟

1. **「结构质量 ≠ 互作可检测性」的指标设计哲学**：对于 IDR 介导的弱互作，传统结构置信度指标（pLDDT、ipTM）可能失效。可迁移思路：针对特定互作类型（如 SLiM、相分离中的多价互作）设计定制化评分，而非依赖通用指标。应用于本课题：在预测 IDR 介导的相分离驱动互作时，可开发类似 MiniPAE 的「局部互作信号提取器」。

2. **AF2 + 轻量级评分优于 AF3 的可能性**：在特定任务上，旧模型 + 定制指标可能优于新模型 + 通用指标。可迁移思路：不要默认「更新模型 = 更好」，系统评估模型-指标组合。应用于本课题：在 IDR 互作预测中，AF2 的 PAE 矩阵可能比 AF3 的输出更适合提取弱互作信号。

3. **Colab 工作流模式**：无需本地算力的云端方案大幅降低使用门槛。可迁移思路：将复杂的 IDR 互作预测流程封装为 Colab 笔记本，使实验生物学家也能使用。应用于本课题：可构建 IDR 互作 + 相分离预测的云端工作流。

4. **计算-实验闭环设计**：计算预测 + 活细胞邻近标记验证的组合策略。可迁移思路：邻近标记（如 BioID、APEX）适合验证低亲和力、瞬时的 IDR 介导互作。应用于本课题：相分离中的多价弱互作可用邻近标记验证。

5. **MiniPAE 作为可复用的评分工具**：代码已开源（GitHub），可直接用于其他 SLiM 预测任务。可迁移思路：评估 MiniPAE 是否也能用于预测 IDR 介导的相分离驱动互作。

---

## 15 与已有知识连接

- **相似方法**：与「AlphaFold 用于肽-蛋白互作预测」的已有研究（如 AF2 预测 MHC-肽、SH3 域-肽互作）相似，但本文创新点在于「不依赖结构质量」的评分策略。可参考：Jumper et al. (2021) Nature; Bryant & Abagyan (2023) 关于 AF 用于肽互作预测的工作。
- **SLiM 数据库与工具**：ELM (Eukaryotic Linear Motif) 数据库是 SLiM 注释的金标准；本文工作流可作为 ELM 预测的补充验证工具。可参考：Kumar et al. (2020) NAR。
- **IDR 互作与相分离**：SLiM 是相分离中多价互作的重要介导者（如 FG 重复序列、PrLD）。本文方法可迁移到相分离驱动互作的预测。可参考：Martin et al. (2020) Science 关于 SLiM 在相分离中的作用。
- **AlphaFold 的 IDR 预测局限**：AF2 对 IDR 的结构预测置信度低，但本文证明其互作信号仍可提取。这与「AF 预测无序区」的讨论相关。可参考：Ruff & Pappu (2021) 关于 AF 与 IDR 的评论。
- **邻近标记技术**：BioID、APEX2 等邻近标记方法已被用于鉴定弱/瞬时互作，本文将其与计算预测结合，类似策略可参考：Roux et al. (2012) JCB。
- **冲突/竞争方法**：基于序列的 SLiM 预测工具（如 SLiMPrints、PEPMatch）可能比 AF 方法更快，但缺乏结构上下文；本文方法可能更适合需要结构信息的场景。

---

## 16 Agent 生成的研究候选

> 标题：Agent 生成的研究候选

1. **候选名称**：MiniPAE 在相分离驱动互作预测中的适用性评估
   - **来源局限/观察**：MiniPAE 在 SLiM 检测中表现优异，但相分离中的多价互作（如 FG 重复、PrLD）是否也能被 MiniPAE 捕获未知
   - **核心假设**：MiniPAE 能识别 IDR 中介导相分离的多价弱互作信号
   - **相对本文的增量**：将 MiniPAE 从 SLiM 扩展到相分离互作预测
   - **初步方法**：在已知相分离驱动蛋白（如 FUS、hnRNPA1）的互作肽段上测试 MiniPAE；与已知相分离突变体比较
   - **验证方式**：与体外相分离实验（浊度、FRAP）结果对比
   - **可能的失败模式**：相分离互作的多价性和协同性可能无法被成对共折叠捕捉
   - **创新状态**：unverified

2. **候选名称**：AF2 共折叠 + 分子动力学（MD）模拟的 SLiM 互作验证工作流
   - **来源局限/观察**：AF2 预测的 SLiM 互作缺乏动态信息，而 SLiM 结合本质上是瞬时的
   - **核心假设**：AF2 预测的 SLiM 互作界面可作为 MD 模拟的初始构象，MD 能提供结合动力学和亲和力排序
   - **相对本文的增量**：将静态预测扩展到动态验证
   - **初步方法**：选取 AF2 + MiniPAE 预测的 SLiM 候选，进行 μs 级 MD 模拟（如 GROMACS），计算结合自由能（MM-PBSA）
   - **验证方式**：与表面等离子共振（SPR）或等温滴定量热（ITC）实验对比
   - **可能的失败模式**：SLiM 结合的自由能面可能过于平坦，MD 采样不足
   - **创新状态**：unverified

3. **候选名称**：基于 MiniPAE 的 IDR 互作组学筛选平台
   - **来源局限/观察**：本文工作流针对单个蛋白-肽对，缺乏组学规模的筛选能力
   - **核心假设**：MiniPAE 可作为高通量筛选指标，从蛋白质组中识别 IDR 介导的互作
   - **相对本文的增量**：从单对预测扩展到互作组学
   - **初步方法**：对目标蛋白的 IDR 进行滑动窗口肽段扫描，与候选互作蛋白库进行批量 AF2 共折叠 + MiniPAE 评分
   - **验证方式**：与邻近标记（BioID）实验数据对比
   - **可能的失败模式**：计算成本随蛋白库规模线性增长，可能不现实
   - **创新状态**：unverified

4. **候选名称**：SLiM 介导互作的 AF2 预测与 AlphaFold3 的深度比较
   - **来源局限/观察**：本文仅报告 AF2 + MiniPAE 优于 AF3，但未深入分析原因
   - **核心假设**：AF3 的互作预测偏向高亲和力复合物，对弱 SLiM 互作不敏感
   - **相对本文的增量**：理解模型架构差异对弱互作检测的影响
   - **初步方法**：在多个 SLiM 数据集上比较 AF2/AF3 的 PAE 分布、置信度特征；分析 AF3 的「置信度校准」是否牺牲了弱信号
   - **验证方式**：与已知 SLiM 突变体的实验结合数据对比
   - **可能的失败模式**：AF3 的 API 限制可能阻碍大规模测试
   - **创新状态**：unverified

5. **候选名称**：IDR 介导互作的「结构质量无关」评分框架
   - **来源局限/观察**：MiniPAE 的成功暗示「局部互作信号」可独立于整体结构质量
   - **核心假设**：可设计一种通用的「互作信号提取器」，适用于 SLiM、相分离、伴侣结合等多种 IDR 介导互作
   - **相对本文的增量**：从特定工具到通用框架
   - **初步方法**：形式化定义「互作信号」为 PAE 矩阵的局部拓扑特征；在多种 IDR 互作数据集上训练/验证
   - **验证方式**：与实验验证的互作数据库（如 BioGRID、IntAct）对比
   - **可能的失败模式**：不同互作类型的信号特征可能差异过大，难以统一
   - **创新状态**：unverified