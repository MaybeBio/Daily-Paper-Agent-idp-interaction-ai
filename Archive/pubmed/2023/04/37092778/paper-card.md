## 01 基本信息

- **标题**：Do "Newly Born" orphan proteins resemble "Never Born" proteins? A study using three deep learning algorithms.
- **作者**：Liu, Jing; Yuan, Rongqing; Shao, Wei; Wang, Jitong; Silman, Israel; Sussman, Joel L
- **单位**：未提供（根据作者信息推测可能涉及以色列魏茨曼科学研究所及中国合作单位，但原文未明确列出）
- **期刊/平台**：Proteins
- **年份**：2023（在线日期 2023-04-24）
- **论文类型**：研究论文（应用型比较研究）
- **领域**：蛋白质结构预测、孤儿蛋白（orphan proteins）、从头蛋白（de novo proteins）、 intrinsically disordered proteins (IDPs)、深度学习结构预测
- **关键词**：orphan proteins; never born proteins; AlphaFold2; RoseTTAFold; ESMFold; intrinsically disordered proteins
- **DOI/arXiv**：10.1002/prot.26496
- **代码**：未提供
- **数据**：未提供（涉及两组"Never Born"蛋白表达实验数据及孤儿蛋白序列，但未公开数据集）
- **阅读日期**：2025-04-11
- **在该方向中的位置**：本文处于「无序蛋白/IDP × 蛋白互作 × AI 方法」交叉方向的边缘位置——它不直接研究蛋白互作或相分离，而是利用三种深度学习结构预测算法（AlphaFold2、RoseTTAFold、ESMFold）比较"孤儿蛋白"（孤儿蛋白常富含IDR/无序倾向）与"Never Born"随机多肽（其中一组实验验证为IDP）的结构特征。其核心价值在于：检验深度学习结构预测器对**无同源模板、低复杂度/无序倾向序列**的预测行为，这对IDP/IDR研究中使用AI工具的可信度评估具有直接参考意义。

## 02 一句话总结

本文用 AlphaFold2、RoseTTAFold、ESMFold 三种深度学习结构预测器，比较两组实验表征过的"Never Born"随机多肽（一组有二级结构、一组为 intrinsically disordered）及若干孤儿蛋白的预测结构，发现预测器虽整体评分低，但能正确区分紧凑折叠蛋白与 extended 无序蛋白，且对含同源家族成员的蛋白预测更可靠。

## 03 研究问题

- **具体问题**：深度学习结构预测算法能否为"Newly Born"孤儿蛋白（无同源可检测蛋白）与"Never Born"随机多肽（氨基酸组成类似天然蛋白）的结构比较提供有价值的信息？预测结果是否与实验数据一致？
- **为什么重要**：孤儿蛋白由新产生的开放阅读框（ORF）表达而来，在进化中持续出现，其结构特征（折叠 vs 无序）对理解蛋白质从头进化、新功能获得至关重要。若深度学习预测器能可靠区分折叠与无序状态，则可大规模注释孤儿蛋白的结构倾向；若不能，则需谨慎使用。
- **现有方法不足**：孤儿蛋白缺乏同源模板，传统同源建模无法适用；实验结构解析耗时费力；此前缺乏对深度学习预测器在"无同源序列"极端情况下的系统评估。
- **精确研究问题**："Can AlphaFold2, RoseTTAFold, and ESMFold reliably distinguish compact folded 'Never Born' proteins from intrinsically disordered ones, and can they produce credible structures for true orphan proteins?"

## 04 背景与发展脉络

*（注：以下脉络为「经外部核验」的领域常识，结合本文框架整理）*

1. **阶段一：孤儿蛋白与从头基因的发现（~2000s-2010s）**
   - 代表性方法：基因组比较、系统发育分析识别 taxonomically restricted genes (TRGs) / orphan genes
   - 优点：揭示了新基因产生的普遍性
   - 局限：缺乏结构信息，功能注释困难
   - 本文位置：聚焦孤儿蛋白的结构预测

2. **阶段二："Never Born"蛋白质实验研究（~2000s-2010s）**
   - 代表性方法：随机多肽文库表达、圆二色谱（CD）表征二级结构
   - 优点：提供了"无进化选择压力"的蛋白质序列-结构关系基线
   - 局限：仅能表征少数样本，无法获得高分辨率结构
   - 本文位置：直接使用此前实验表征过的两组"Never Born"蛋白（Group 1 有结构、Group 3 无序）作为基准

3. **阶段三：深度学习结构预测革命（2018-2022）**
   - 代表性方法：AlphaFold2 (2021)、RoseTTAFold (2021)、ESMFold (2022)
   - 优点：高精度预测单体结构，尤其对有同源信息的蛋白
   - 局限：对孤儿蛋白/无同源序列蛋白的预测置信度低，对IDP的预测行为尚未充分表征
   - 本文位置：首次系统比较三种预测器在"Never Born"蛋白和孤儿蛋白上的表现

4. **阶段四：IDP/IDR与相分离的AI研究（2022-至今）**
   - 代表性方法：AlphaFold2 pLDDT 作为无序倾向预测器、IUPred/ESLpred 等专用工具
   - 优点：pLDDT 低值区域与实验无序区域有相关性
   - 局限：AF2 对全长IDP的预测结构不可靠，需谨慎解读
   - 本文位置：为这一方向提供了"预测器对实验验证IDP的行为"的直接证据

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 孤儿蛋白缺乏同源信息 | 无法用传统同源建模预测结构；BLAST 无显著匹配 | 孤儿蛋白是新进化产生的，无祖先同源序列 | 摘要："devoid of detectable homology to any other proteins" |
| 深度学习预测器对无同源序列蛋白的可靠性未知 | 预测模型整体评分低（pLDDT 等指标低） | 预测器依赖进化共变异信息，孤儿蛋白缺乏 MSA 深度 | 摘要："the models generated were scored as being of low quality" |
| 预测器能否区分折叠 vs 无序 | 需验证预测的 compact/extended 状态是否与实验一致 | 若预测器对无序蛋白也预测为紧凑结构，则无法用于孤儿蛋白筛选 | 摘要：Group 1 预测为 compact、Group 3 预测为 extended，与实验一致 |
| 孤儿蛋白中 novel fold 的预测困难 | 两个 novel fold 孤儿蛋白的预测结构与晶体结构不一致 | 无同源模板时，预测器无法推断全新折叠 | 摘要："only for the protein which did not have a novel fold... did all three algorithms predict very similar, high-quality structures" |
| 预测器对含同源家族成员的孤儿蛋白预测更可靠 | HCO_11565 被三种算法一致预测为高质量结构 | 该蛋白属于 taxonomically restricted family，有多个同源物；Dali 发现非相关蛋白有相似折叠 | 摘要："remarkably similar and high-quality predictions for one large protein, HCO_11565" |

## 06 核心思想

### 1) 表面方法
用三种深度学习结构预测器（AlphaFold2、RoseTTAFold、ESMFold）对两组"Never Born"蛋白（Group 1: 实验验证有二级结构；Group 3: 实验验证为 intrinsically disordered）及若干孤儿蛋白（含已知晶体结构的3个、功能已知但结构未知的7个）进行结构预测，比较预测结构的 compactness（通过 accessible surface area 量化）与实验数据的一致性。

### 2) 核心洞察
- 尽管预测器对这类"无同源序列"蛋白的整体置信度低，但**预测的全局形状（compact vs extended）仍能反映真实的折叠/无序状态**——Group 1 被预测为紧凑、Group 3 被预测为 extended，与实验 CD 数据一致。
- 预测质量的关键决定因素不是"是否孤儿"，而是**是否有同源家族成员**（MSA 深度）以及**是否采用已知折叠**（fold 是否在 PDB 中出现过）。HCO_11565 因有家族同源物和相似折叠的无关蛋白，预测质量高；novel fold 孤儿蛋白则预测失败。
- [Analysis] 这暗示：深度学习预测器对孤儿蛋白的"结构预测"应被理解为"形状/无序倾向预测"而非"精确原子结构预测"，其输出可作为低分辨率结构倾向指标使用。

### 3) 可能的普适教训 [Analysis]
- 对 IDP/IDR 研究：AF2 等预测器的 pLDDT 低值区域和 extended 预测形状可作为无序倾向的辅助证据，但需结合实验验证。
- 对孤儿蛋白/新基因研究：预测器的 compact/extended 区分能力可用于大规模筛选候选折叠蛋白 vs 无序蛋白，但 novel fold 预测不可靠。
- 对蛋白互作研究：若互作伙伴之一是孤儿蛋白/IDP，预测器给出的结构不可直接用于对接或互作建模，需谨慎。

## 07 方法总览

- **输入**：蛋白质氨基酸序列（两组"Never Born"蛋白序列、3个有晶体结构的孤儿蛋白序列、7个功能已知但结构未知的孤儿蛋白序列）
- **输出**：每个蛋白的预测三维结构模型（PDB 格式）、每个残基的置信度分数（pLDDT 等）、预测结构的 accessible surface area (ASA)
- **模块**：
  1. 序列输入与 MSA 构建（AlphaFold2/RoseTTAFold 需 MSA；ESMFold 为单序列模型）
  2. 深度学习结构预测（三种算法独立运行）
  3. 结构质量评估（预测置信度分数）
  4. 结构比较分析（计算 ASA、比较 compact vs extended）
  5. 与实验数据对照（CD 数据、晶体结构）
- **训练**：三种算法均为预训练模型，本文未进行微调
- **工具**：AlphaFold2、RoseTTAFold、ESMFold（具体版本未提供）
- **反馈回路**：无（一次性预测，无迭代优化）
- **假设**：预测结构的 ASA 可作为蛋白 compactness 的量化指标；实验 CD 数据（Group 1 有结构、Group 3 无序）可作为 ground truth

**文字流程**：
1. 收集两组"Never Born"蛋白序列（来自此前表达实验）和孤儿蛋白序列
2. 分别用 AlphaFold2、RoseTTAFold、ESMFold 预测每个蛋白的结构
3. 计算每个预测结构的 ASA，比较 Group 1 vs Group 3 的 ASA 分布
4. 对3个有晶体结构的孤儿蛋白，比较预测结构与实验结构的相似度
5. 对7个功能已知的孤儿蛋白，分析预测结构的形状（compact/extended）与序列预测的无序倾向是否一致
6. 统计检验 ASA 差异的显著性

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| MSA 构建（AF2/RoseTTAFold） | 为预测器提供进化共变异信息 | 预测器依赖 MSA 推断残基间接触；孤儿蛋白 MSA 极浅 | 输入：序列；输出：MSA | 摘要指出 HCO_11565 因有家族同源物而预测质量高 | [预期] 移除后预测质量进一步下降，但 ESMFold 无需 MSA 仍能区分 Group 1/3，说明形状区分不依赖 MSA |
| 深度学习结构预测模块 | 生成三维结构模型 | 核心预测引擎 | 输入：序列（+MSA）；输出：结构模型+置信度分数 | 三种算法均成功生成模型 | 无法移除（核心模块） |
| ASA 计算 | 量化预测结构的 compactness | 用于比较 Group 1 vs Group 3 的全局形状差异 | 输入：预测结构；输出：ASA 数值 | 摘要："statistically significant by comparing their accessible surface areas" | [预期] 无 ASA 则无法量化比较，只能定性观察 |
| 与实验数据对照模块 | 验证预测可靠性 | 建立预测与实验的对应关系 | 输入：预测结构+实验数据（CD、晶体结构）；输出：一致性判断 | Group 1 compact、Group 3 extended 与实验一致 | [预期] 无实验对照则无法判断预测可靠性 |
| 统计检验 | 确认 Group 1/3 的 ASA 差异非随机 | 支撑"预测器能区分折叠/无序"的结论 | 输入：两组 ASA 值；输出：p 值 | 摘要明确提到"statistically significant" | [预期] 无统计检验则结论缺乏严谨性 |

## 09 关键公式符号

本文未提供明确的数学公式。核心量化指标为 **accessible surface area (ASA)**，其计算基于预测结构模型，使用标准算法（如 Shrake-Rupley 算法）计算溶剂可及表面积。文中未给出具体公式或参数。

## 10 实验设计与证据链

- **数据集/群体**：
  - "Never Born"蛋白：Group 1（4个成员，实验验证有实质二级结构）、Group 3（成员数未明确，实验验证为 intrinsically disordered）
  - 孤儿蛋白：3个有晶体结构（其中2个为 novel fold，1个为 taxonomically restricted 而非 true orphan）、7个功能已知但结构未知
- **规模**：总计约14个蛋白序列（4+4+3+7，具体数字未完全明确）
- **指标**：预测结构 ASA、预测置信度分数、预测结构与晶体结构的相似度（定性描述）
- **基线**：无显式基线（未与随机多肽预测或传统方法对比）
- **预算**：未提供
- **骨干/仪器**：AlphaFold2、RoseTTAFold、ESMFold（版本未提供）
- **oracle 输入**：实验 CD 数据（Group 1/3 分类）、晶体结构（3个孤儿蛋白）
- **评测协议**：比较 Group 1 vs Group 3 的 ASA 分布；比较预测结构与晶体结构的相似性；对7个未知结构孤儿蛋白进行形状分类

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| Group 1 vs Group 3 的预测结构比较 | 预测器能区分折叠与无序蛋白 | 三种算法分别预测两组蛋白，比较 ASA | Group 1 预测为 compact，Group 3 预测为 extended，ASA 差异显著 | 预测器的全局形状输出与实验分类一致 | 不能证明预测器能精确预测 IDP 的原子结构 | 摘要 |
| 3个有晶体结构孤儿蛋白的预测 vs 实验 | 预测器对孤儿蛋白的预测可靠性 | 预测结构与晶体结构对比 | 仅非 novel fold 蛋白（taxonomically restricted）预测质量高且与晶体结构一致；2个 novel fold 蛋白预测失败 | 预测质量取决于是否有同源家族/已知折叠 | 不能推广到所有孤儿蛋白 | 摘要 |
| 7个未知结构孤儿蛋白的预测 | 预测器能否提供结构线索 | 三种算法预测，观察形状一致性 | 2个预测为 extended（与序列无序预测一致），5个预测为 compact（其中 HCO_11565 三种算法高度一致） | 预测器可为孤儿蛋白提供形状/无序倾向线索 | 不能确认 compact 预测的精确结构正确性 | 摘要 |

## 11 结论正确解读

- **任务范围**：本文仅评估三种预测器对"无同源序列蛋白"的**全局形状预测**（compact vs extended），而非精确原子结构预测。
- **oracle/真值输入**：Group 1/3 的分类基于实验 CD 数据（非高分辨率结构）；3个孤儿蛋白有晶体结构作为真值。
- **端到端状态**：非端到端——预测器输出结构后，需人工计算 ASA 并进行统计比较。
- **算力成本**：未提供（但三种预测器均为标准工具，成本可预估）。
- **历史数据依赖**：预测器训练数据包含 PDB 中已知折叠，对 novel fold 预测能力有限。
- **模型依赖**：结论基于三种特定算法（AF2、RF、ESMFold），不保证其他预测器（如 ESM-2 微调版、OmegaFold）有相同行为。
- **最难情形**：novel fold 孤儿蛋白（无同源、无相似折叠）是预测失败的重灾区。
- **群体/领域边界**：样本量小（~14个蛋白），统计功效有限；"Never Born"蛋白是人工随机序列，与天然孤儿蛋白的序列特征可能有差异。
- **不确定性**：ASA 差异的显著性已报告，但未提供效应量或置信区间；预测结构与晶体结构的相似度未量化（如 TM-score 未报告）。

**有边界的复述**：在约14个样本的小规模测试中，AlphaFold2、RoseTTAFold、ESMFold 对"Never Born"蛋白的全局形状预测（compact vs extended）与实验分类一致，且对含同源家族成员的孤儿蛋白（HCO_11565）能产生高质量一致预测；但对 novel fold 孤儿蛋白的预测不可靠。这些结论不能外推到所有孤儿蛋白或 IDP 的精确结构预测。

## 12 作者自认局限

在提供的摘要中，作者未明确列出局限性。以下为作者提及的相关约束（非正式局限）：

- 预测模型整体被评分为低质量（"the models generated were scored as being of low quality"）——暗示预测器对这类蛋白的置信度有限。
- 对 novel fold 孤儿蛋白，预测与晶体结构不一致（隐含在"only for the protein which did not have a novel fold... did all three algorithms predict very similar, high-quality structures"中）。
- 对 HCO_11565 高质量预测的解释归因于同源家族和 Dali 发现的相似折叠——暗示无这些条件时预测不可靠。

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 样本量极小（~14个蛋白） | 统计显著性可能由个别样本驱动；Group 1 仅4个成员 | 小样本结论难以推广到整个孤儿蛋白/IDP 类别 | 在更大规模（>100）的孤儿蛋白/IDP 数据集上重复实验 | 摘要中样本数描述 |
| "Never Born"蛋白是人工随机序列 | 其序列特征（氨基酸组成、长度）可能与天然孤儿蛋白差异显著，预测器行为可能不同 | 若序列分布不同，则"Never Born"结果不能直接外推到天然孤儿蛋白 | 用天然孤儿蛋白（如人类/酵母中已验证的 de novo genes）重复比较 | 摘要中"random polypeptides with amino acid content similar to that of native proteins" |
| ASA 作为 compactness 指标可能过于粗糙 | 两个结构可能 ASA 相似但拓扑完全不同；IDP 的 extended 状态在预测器中可能只是"低置信度折叠"的伪影 | 若 ASA 差异反映的是预测器的不确定性而非真实结构差异，则结论需重新解释 | 比较预测结构的残基级 pLDDT 分布与实验无序区域（如 NMR 化学位移） | 摘要仅提到 ASA 比较 |
| 未报告预测器内部置信度分数与实验数据的关系 | pLDDT 低值可能直接指示无序，而非结构预测"失败" | 若 pLDDT 与实验无序有定量关系，则预测器可作为 IDP 预测工具 | 分析 pLDDT 与 CD/NMR 无序评分的相关性 | 摘要未提及 pLDDT 分析 |
| 对 novel fold 蛋白的"失败"可能反映训练数据偏差 | PDB 中 novel fold 极少，预测器从未见过类似拓扑，失败是预期行为而非算法缺陷 | 这提示对孤儿蛋白预测应设定合理预期，而非归咎于算法 | 用结构预测领域的标准指标（TM-score, lDDT）量化失败程度 | 摘要中"only for the protein which did not have a novel fold" |

## 14 Agent 提炼的知识候选

**面向课题方向（IDP/IDR × 蛋白互作 × AI/物理模拟）的可迁移知识：**

1. **预测器全局形状可作为 IDP 筛选的辅助工具**：本文证明 AF2/RF/ESMFold 对实验验证的 IDP（Group 3）预测为 extended 结构，对折叠蛋白预测为 compact。在 IDP/IDR 互作研究中，可用预测结构的 ASA 或 radius of gyration 作为无序倾向的快速预筛指标，再结合 IUPred 等专用工具交叉验证。

2. **pLDDT 低值区域的解读需谨慎**：本文未分析 pLDDT，但预测器对 IDP 的"低质量"评分可能恰恰指示无序区域。在 IDR 介导互作研究中，可将 AF2 的 pLDDT 低值区域与实验无序数据（NMR、CD）对照，建立预测器置信度与无序程度的映射关系。

3. **同源信息对预测质量的决定性作用**：HCO_11565 因有家族同源物而预测成功，提示在 IDR 互作研究中，若互作伙伴有同源物（即使是 taxonomically restricted family），AF2 预测的互作界面更可信；对孤儿 IDP，预测结果仅作参考。

4. **多算法一致性作为置信度指标**：本文用三种算法交叉验证，当多算法对同一蛋白预测出相似形状时，结论更可靠。在 IDP 互作研究中，可对 IDP-伙伴复合物用多种预测器（AF2-multimer、RoseTTAFold2、ESMFold）预测，一致性高的区域更可能是真实互作界面。

5. **"Never Born"蛋白作为 IDP 研究的模型系统**：人工随机多肽（氨基酸组成类似天然蛋白）可作为 IDP 序列-结构关系的可控实验系统，结合深度学习预测可探索"序列组成→无序倾向→互作能力"的映射。

6. **对 IDP 复合物预测的启示**：本文对单体 IDP 的预测表明 extended 结构可被正确预测，这提示对 IDP 参与的复合物，预测器可能正确捕捉"结合后折叠"或"fuzzy complex"的整体形状，但需实验验证。

## 15 与已有知识连接

- **AlphaFold2 对 IDP 的预测行为**：已有文献（如 Ruff & Pappu, 2021; Akdel et al., 2022）表明 AF2 对 IDP 的 pLDDT 低值区域与实验无序区域相关。本文为这一观点提供了"Never Born"蛋白的额外证据，且扩展了 RoseTTAFold 和 ESMFold 的比较。
- **孤儿蛋白/从头基因的结构特征**：Bungard et al. (2020) 等研究表明从头蛋白常富含无序区域。本文通过预测器比较支持这一观点（Group 3 的 IDP 被预测为 extended）。
- **"Never Born"蛋白实验**：本文使用的 Group 1/3 蛋白来自此前表达实验（可能为 Keefe & Szostak 或类似随机多肽文库工作），本文将其作为深度学习预测的基准数据集。
- **ESMFold 的单序列预测能力**：ESMFold 无需 MSA 即可预测，本文中 ESMFold 也能区分 Group 1/3，支持"单序列模型对无同源蛋白的适用性"这一观点。
- **可迁移领域**：IDP 介导的相分离研究中，AF2 等预测器常被用于预测凝聚体形成蛋白的结构倾向。本文提示：对无同源序列的 IDP，预测器的 extended 预测可作为相分离倾向的间接证据，但需结合序列组成（如电荷模式、疏水模式）分析。

## 16 Agent 生成的研究候选

**候选 1：基于多预测器一致性的 IDP 互作界面预测框架**
- **来源局限/观察**：本文仅比较单体预测，未涉及 IDP-伙伴复合物；但多算法一致性在单体上有效。
- **核心假设**：对 IDP-伙伴复合物，多预测器（AF2-multimer、RoseTTAFold2、ESMFold）预测的互作界面一致性高的区域，更可能是真实结合位点。
- **初步方法**：收集已知 IDP-伙伴复合物（如 PDB 中带无序区域的复合物），用三种预测器预测，计算界面残基的预测一致性分数，与实验界面比较。
- **验证方式**：在独立测试集上计算 precision/recall；与 AlphaFold3 预测结果对比。
- **创新状态**：unverified

**候选 2：孤儿蛋白的"预测无序度"与实验无序度的系统比较**
- **来源局限/观察**：本文样本量小（~14），且未定量比较预测器输出与实验无序评分。
- **核心假设**：AF2 pLDDT、ESMFold pLDDT 与实验无序评分（如 CD 的 R值、NMR 的化学位移指数）在孤儿蛋白上存在定量相关。
- **初步方法**：收集更多实验表征的孤儿蛋白（如酵母 de novo genes 的 CD/NMR 数据），计算预测器 pLDDT 与实验无序评分的 Spearman 相关。
- **验证方式**：交叉验证；与 IUPred3 等专用无序预测器比较。
- **创新状态**：unverified

**候选 3：利用"Never Born"蛋白库训练 IDP 互作预测模型**
- **来源局限/观察**：本文的"Never Born"蛋白是可控的序列-结构系统，但未用于训练。
- **核心假设**：在"Never Born"蛋白库上训练的序列-结构（或序列-无序）映射模型，可迁移到天然孤儿蛋白的 IDP 预测。
- **初步方法**：用大规模随机多肽序列（氨基酸组成匹配天然蛋白）生成训练集，用实验 CD 或预测器输出作为标签，训练轻量模型预测无序倾向。
- **验证方式**：在天然孤儿蛋白上测试；与现有无序预测器比较 AUC。
- **创新状态**：unverified

**候选 4：IDP 介导相分离的"预测形状"与实验凝聚体性质的关联**
- **来源局限/观察**：本文证明预测器能区分 compact/extended 单体，但未延伸到相分离。
- **核心假设**：对已知相分离蛋白，预测结构的 extended 程度（如 ASA、Rg）与实验凝聚体形成倾向（如饱和浓度）相关。
- **初步方法**：收集已知相分离蛋白（如 FUS、TDP-43、hnRNPA1），用三种预测器预测，计算全局形状指标，与实验相分离数据（如 LLPS 饱和浓度）回归。
- **验证方式**：留一法交叉验证；与序列组成特征（如 prion-like domain 分数）比较。
- **创新状态**：unverified

**候选 5：novel fold 孤儿蛋白的"预测失败"模式分析**
- **来源局限/观察**：本文发现 novel fold 孤儿蛋白预测失败，但未分析失败模式。
- **核心假设**：预测失败（低 pLDDT、多构象预测）可能指示蛋白质的构象异质性或内在无序，而非单纯算法局限。
- **初步方法**：对 novel fold 孤儿蛋白的预测结构进行聚类分析，检查是否出现多构象分布；与实验无序数据对照。
- **验证方式**：若多构象预测与实验无序一致，则"失败"可重新解释为"无序信号"。
- **创新状态**：unverified