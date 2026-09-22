## 01 基本信息

- **标题**：RIBEX: Predicting and Explaining RNA Binding Across Structured and Intrinsically Disordered Regions (IDR)-rich Proteins
- **作者**：Firmani S; Steinbauer F; Kasneci G; Marsico A; Horlacher M
- **单位**：未提供（bioRxiv 预印本未在提供材料中列出单位）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2026
- **论文类型**：预印本（方法学/计算生物学）
- **领域**：RNA结合蛋白预测、蛋白质语言模型、蛋白质互作网络、无序蛋白
- **关键词**：RNA-binding proteins (RBPs)、intrinsically disordered regions (IDRs)、protein language model (pLM)、protein-protein interaction network、Personalized PageRank、LoRA、interpretability
- **DOI/arXiv 号**：10.64898/2026.03.13.711639
- **代码**：未提供
- **数据**：人类 STRING PPI 网络、RNA Interactome Capture (RIC) 数据集、annotation-based benchmark
- **阅读日期**：2026-04-15（假设）
- **该文在课题方向中的位置**：本文聚焦 IDR 富集蛋白的 RNA 结合预测，将 pLM 序列嵌入与 PPI 网络拓扑（图位置编码）融合，属于「无序蛋白/相分离 × 蛋白互作 × AI 方法」交叉方向中「AI 预测蛋白互作功能」子类，其可解释性分析（计算丙氨酸扫描 + 网络消融）对 IDR 介导互作机制解析具有直接参考价值。

---

## 02 一句话总结

本文提出 RIBEX 多模态框架，将 ESM2 蛋白质语言模型嵌入与 STRING PPI 网络的 Personalized PageRank 位置编码通过 FiLM 条件化融合，并辅以 LoRA 参数高效微调，在 RNA 结合蛋白预测任务上超越现有方法，尤其在缺乏经典 RBD 和 IDR 富集蛋白子集上表现突出，同时通过序列级与网络级可解释性分析揭示已知 RNA 结合结构域和 IDR 相关贡献。

---

## 03 研究问题

- **具体问题**：如何更准确地预测 RNA 结合蛋白（RBPs），特别是那些 RNA 结合活性发生在经典 RNA 结合结构域（RBD）之外（如 IDR 内或通过蛋白复合物）的蛋白？
- **为什么重要**：RBPs 调控转录后过程，但许多尚未被发现；IDR 介导的 RNA 结合在相分离和凝聚体形成中起关键作用，与无序蛋白互作课题直接相关。
- **现有方法为何不足**：仅依赖序列特征的方法（如基于序列的 RBP 预测器）忽略了 RNA 结合常依赖细胞互作环境；现有方法未系统整合序列信息与蛋白互作上下文。
- **精确研究问题**：Can integrating protein language model embeddings with protein interactome topology improve RBP prediction accuracy and interpretability, particularly for proteins lacking canonical RBDs or enriched in IDRs?

---

## 04 背景与发展脉络

*注：以下脉络基于本文框架，标注「仅本文框架」；部分外部信息标注「经外部核验」。*

| 阶段 | 代表性方法 | 优点 | 局限 | 本文位置 |
|------|-----------|------|------|---------|
| 序列特征方法 | 基于氨基酸组成、结构域注释的 RBP 预测器 | 简单、可解释 | 忽略 IDR 内非经典结合位点；无法捕捉互作上下文 | 本文超越对象 |
| 深度序列模型 | 基于 CNN/RNN 的 RBP 预测 | 自动学习序列模式 | 仍仅用序列；泛化到非经典 RBP 有限 | 本文对比基线 |
| 蛋白质语言模型 | ESM2、ProtTrans 等 pLM 嵌入 | 捕获进化与结构信息 | 冻结嵌入缺乏任务适配；未利用互作网络 | 本文基础组件 |
| 图神经网络/网络拓扑 | STRING 等 PPI 网络上的节点嵌入 | 捕获互作上下文 | 单独使用忽略序列细节；计算成本高 | 本文创新点：PPI 拓扑 + 序列融合 |
| 多模态融合 | 序列 + 结构 + 网络联合建模 | 信息互补 | 融合策略简单；可解释性不足 | 本文：FiLM 条件化 + LoRA + 三重可解释性 |

**本文主张的位置**：首个系统整合 pLM 序列嵌入与 PPI 网络拓扑（而非仅序列或仅网络）的 RBP 预测框架，并强调在 IDR 富集蛋白上的优势。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|---------------|---------|
| 非经典 RBP 难以识别 | 许多 RBPs 缺乏已知 RBD，RNA 结合发生在 IDR 或复合物中 | 现有方法过度依赖结构域注释；IDR 缺乏保守序列模式 | Motivation 段：RNA-binding activity often occurs outside canonical RBDs |
| 序列特征不足以预测 | 仅用序列的模型在挑战性子集上性能下降 | 序列特征无法编码细胞互作环境对 RNA 结合的贡献 | Motivation 段：approaches relying solely on sequence-derived features are limited |
| 互作上下文被忽略 | 现有方法未利用 PPI 网络信息 | 缺乏将序列与网络拓扑整合的框架 | Motivation 段：no framework rigorously integrates both sequence information and protein interaction context |
| 大模型适配成本高 | 冻结大 pLM 嵌入效果有限，全量微调成本高 | 参数效率与性能之间的权衡 | Results 段：LoRA adaptation of ESM2-650M yields larger gains than simply scaling frozen backbone size |
| 预测缺乏可解释性 | 黑箱模型难以揭示 RNA 结合的结构基础 | 缺乏序列级与网络级联合解释工具 | Results 段：combine sequence-level computational alanine scanning with network-level positional-encoding ablation |

---

## 06 核心思想

### 1) 表面方法
RIBEX 是一个多模态框架：将 ESM2 pLM 的序列嵌入（池化后）与从人类 STRING PPI 网络计算的 Personalized PageRank 位置编码（经 PCA 降维）通过 FiLM（Feature-wise Linear Modulation）条件化融合，使用 LoRA 对 ESM2 进行参数高效微调，最终输出 RBP 预测。

### 2) 核心洞察
RNA 结合活性不仅由序列决定，还受蛋白在互作网络中的拓扑位置影响——PPI 网络中的邻近性可能反映 RNA 结合所需的蛋白复合物环境或功能模块。因此，将序列嵌入与网络拓扑编码融合，可以捕捉纯序列方法无法获取的互补信号，尤其对 IDR 富集蛋白（其序列信号弱但网络位置可能具有功能意义）。

### 3) 可能的普适教训 [Analysis]
对于 IDP/IDR 介导的蛋白互作预测，单一模态（序列、结构、网络）均不充分；多模态融合应基于「不同模态编码不同物理化学约束」的原则。此外，可解释性不应是事后附加，而应设计为框架的组成部分（本文通过计算丙氨酸扫描 + 网络消融 + 逆 PCA 映射实现）。

---

## 07 方法总览

- **输入**：蛋白序列（目标蛋白）+ 人类 STRING PPI 网络
- **输出**：RNA 结合概率（二分类预测）
- **模块**：
  1. 序列编码：ESM2 pLM（650M 参数）提取嵌入，池化
  2. 网络编码：STRING PPI 上计算 Personalized PageRank → 位置编码 → PCA 降维
  3. 融合：FiLM 条件化（网络 PE 调制序列特征）
  4. 适配：LoRA 微调 ESM2
  5. 预测头：分类层输出 RBP 概率
  6. 解释模块：计算丙氨酸扫描（序列级）、PE 消融（网络级）、逆 PCA 映射
- **训练**：在 annotation-based benchmark 上训练/验证，在 RIC 数据集上独立评测
- **工具**：未提供具体实现细节（如框架、硬件）
- **反馈回路**：解释模块的输出可用于识别关键残基和网络社区，指导后续实验验证
- **文字流程**：输入蛋白序列 → ESM2 嵌入池化 → 同时从 STRING 计算该蛋白的 Personalized PageRank 向量 → PCA 降维得到 PE → FiLM 层用 PE 调制序列特征 → LoRA 微调后的 ESM2 输出融合特征 → 分类头预测 RBP 概率 → 解释模块分别通过丙氨酸扫描、PE 消融和逆 PCA 映射定位关键序列位点、网络位置和功能社区。

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|---------|---------|---------|----------------------|
| ESM2 序列嵌入 | 提取蛋白序列的进化/结构/功能特征 | 序列是 RNA 结合的基础决定因素 | 输入：氨基酸序列；输出：嵌入向量 | Results 段：pLM embeddings 作为基础特征 | 预期：性能大幅下降（未做消融实验，[Analysis] 推测） |
| Personalized PageRank PE | 编码蛋白在 PPI 网络中的拓扑位置 | 捕捉互作上下文对 RNA 结合的贡献 | 输入：STRING 网络 + 目标蛋白；输出：低维 PE 向量 | Results 段：PE consistently improves predictive performance | 实测：在 annotation benchmark 和 RIC 上均降低性能（作者明确报告 PE 消融实验） |
| PCA 降维 | 降低 PE 维度，去冗余 | 高维 PPR 向量含噪声，降维利于融合 | 输入：PPR 向量；输出：主成分 | Methods 节（未提供细节） | 预期：维度灾难或过拟合（[Analysis] 推测） |
| FiLM 条件化 | 用网络 PE 调制序列特征 | 实现序列与网络信息的非线性交互 | 输入：序列特征 + PE；输出：调制后特征 | Results 段：fusion through FiLM conditioning | 预期：若替换为简单拼接，融合效果可能下降（[Analysis] 推测） |
| LoRA 适配 | 参数高效微调 ESM2 | 冻结大模型嵌入不足以适应任务 | 输入：ESM2 权重；输出：低秩适配权重 | Results 段：LoRA yields larger gains than scaling frozen backbone | 实测：LoRA 优于增大冻结 backbone 规模 |
| 计算丙氨酸扫描 | 逐残基突变评估对预测的影响 | 定位关键 RNA 结合残基 | 输入：蛋白序列；输出：残基重要性分数 | Results 段：recovering known RNA-binding domains | 预期：移除后丧失序列级可解释性 |
| PE 消融 + 逆 PCA | 评估网络位置贡献并映射回网络空间 | 识别功能互作社区 | 输入：PE 向量；输出：网络社区归属 | Results 段：functional interactome communities linked to RBP predictions | 预期：移除后丧失网络级可解释性 |

---

## 09 关键公式符号

| 公式 | 符号含义 | 用途 | 直觉 | 来源 |
|------|---------|------|------|------|
| Personalized PageRank: `PPR = (1-α)·(I - α·D⁻¹A)⁻¹·eᵢ` | α：阻尼因子；A：邻接矩阵；D：度矩阵；eᵢ：目标节点指示向量 | 计算蛋白 i 在网络中的个性化 PageRank 向量 | 衡量从目标蛋白出发随机游走到达各节点的概率，编码网络邻近性 | Methods 节（作者描述，公式为 [Analysis] 标准形式） |
| PCA: `Z = X·W` | X：PPR 矩阵；W：主成分载荷矩阵；Z：降维后 PE | 降维 PPR 向量 | 保留最大方差方向，去相关 | Methods 节（作者描述，公式为 [Analysis] 标准形式） |
| FiLM: `h' = γ(PE) ⊙ h + β(PE)` | h：序列特征；γ, β：由 PE 生成的比例/偏移参数；⊙：逐元素乘 | 用网络信息调制序列特征 | 网络拓扑决定序列特征如何被强调或抑制 | Methods 节（作者描述，公式为 [Analysis] 标准形式） |
| LoRA: `W' = W + ΔW = W + BA` | W：原权重；B, A：低秩分解矩阵 | 参数高效微调 | 用低秩更新近似全量微调 | Methods 节（作者描述，公式为 [Analysis] 标准形式） |

*注：作者未在提供的材料中给出具体公式，以上为基于标准方法的 [Analysis] 重建。*

---

## 10 实验设计与证据链

- **数据集**：
  - 训练/验证：annotation-based benchmark（具体规模未提供）
  - 独立测试：RNA Interactome Capture (RIC) 实验数据集（具体规模未提供）
- **指标**：未提供具体指标（推测为 AUROC/AUPRC，[Analysis]）
- **基线**：RBP-TSTL、HydRA（state-of-the-art 方法）
- **评测协议**：在 annotation benchmark 上训练，在 RIC 上独立评测；另设挑战性子集（缺乏 RBD 的蛋白、IDR 富集蛋白）
- **oracle 输入**：不适用（监督学习，无 oracle）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|-----------|----------------|------|
| 主 benchmark 预测 | RIBEX 优于现有方法 | vs RBP-TSTL、HydRA | RIBEX outperforms（具体数值未提供） | 多模态融合有效 | 无法确定是否统计显著（未提供 p 值/置信区间） | Results 段 |
| PE 消融 | 网络拓扑提供互补信息 | 有 PE vs 无 PE | PE consistently improves performance | 互作网络信息对 RBP 预测有增量贡献 | 无法确定 PE 贡献是否独立于序列特征 | Results 段 |
| LoRA vs 冻结 backbone | 参数高效微调优于增大模型 | LoRA-ESM2-650M vs 更大冻结模型 | LoRA yields larger gains | 任务适配比模型规模更重要 | 未比较 LoRA vs 全量微调 | Results 段 |
| 挑战性子集（无 RBD/IDR 富集） | 在非经典 RBP 上表现优异 | 标准子集 vs 挑战子集 | 表现突出（具体数值未提供） | 多模态方法对 IDR 介导结合有优势 | 无法确定是否因网络信息或序列嵌入 | Results 段 |
| 可解释性分析 | 恢复已知 RBD 和 IDR 贡献 | 计算丙氨酸扫描 vs 已知注释 | recovering known RNA-binding domains | 解释模块有效 | 未与实验验证（如突变体功能实验）对照 | Results 段 |

---

## 11 结论正确解读

- **任务范围**：本文解决的是 RBP 二分类预测问题，而非 RNA 结合位点/残基级预测（尽管可解释性分析提供残基级信息）。
- **oracle/真值输入**：训练标签来自 annotation-based benchmark（可能基于 GO 注释或已知 RBP 数据库），RIC 数据集为实验验证集。标签质量依赖注释完整性，可能遗漏未注释的 RBP。
- **端到端状态**：非端到端——序列嵌入来自预训练 ESM2（冻结+LoRA），网络 PE 来自预计算 STRING，融合后仅分类头为任务训练。
- **算力成本**：未提供。ESM2-650M + LoRA 训练成本中等，但 STRING 上 PPR 计算需预处理。
- **历史数据依赖**：依赖 STRING 网络（版本未提供）和 ESM2 预训练数据；网络更新或领域偏移可能影响性能。
- **模型依赖**：结果依赖 ESM2 和 STRING 的选择；其他 pLM 或网络可能产生不同结果。
- **最难情形**：缺乏 PPI 网络覆盖的蛋白（如新发现蛋白）、非人类物种（模型仅用人类 STRING）、RNA 结合依赖动态构象变化的 IDR 场景。
- **群体/领域边界**：仅人类蛋白；仅 RNA 结合预测，不覆盖 DNA 结合或其他互作类型。
- **不确定性**：未提供置信区间、错误分析或失败案例讨论。

**有边界的复述**：RIBEX 在人类蛋白上，通过融合 ESM2 序列嵌入与 STRING 网络拓扑，在 RBP 预测任务上优于现有方法，且该优势在缺乏经典 RBD 和 IDR 富集蛋白子集上更为明显；其可解释性分析可恢复已知 RNA 结合结构域和网络功能社区，但结论限于人类蛋白和当前数据版本。

---

## 12 作者自认局限

在提供的材料（摘要）中，作者未明确列出局限性。以下为作者提及的相关约束（非正式局限）：

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|---------|-------------------|------|
| 未提供 | 未提供 | 未提供 | 未提供 |

**作者提及的相关约束**（非正式局限）：
- 方法依赖 STRING 网络，可能不覆盖所有蛋白（Motivation 段暗示网络上下文的重要性，但未讨论覆盖度问题）
- 仅针对人类蛋白（从「human STRING PPI network」推断，[Analysis]）
- 未讨论 IDR 构象动态性对 RNA 结合的影响（[Analysis] 推测，摘要未涉及）

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| PE 提升可能来自网络度/中心性而非特异性拓扑 | 高连接度蛋白（hub）可能更易被注释为 RBP，PE 可能只是编码了注释偏差 | 若 PE 仅编码度信息，则「互作上下文」的解释不成立 | 控制网络度后重新评估 PE 增量；使用度作为替代特征对比 | Results 段：PE improves performance，但未控制混淆变量 |
| 挑战性子集优势可能因基准标签偏差 | 无 RBD 蛋白的 RBP 标签可能来自低通量实验，与网络位置相关 | 若标签偏差存在，挑战子集优势可能是人为产物 | 使用独立实验验证集（如 eCLIP）重新评估挑战子集 | Results 段：challenging subsets 表现突出 |
| 可解释性分析缺乏定量验证 | 「recovering known RNA-binding domains」可能是定性观察，无量化指标 | 无法判断解释质量是否达到实用水平 | 计算残基级 AUC（预测重要性 vs 实验注释） | Results 段：recovering known domains，未提供量化指标 |
| 未与全量微调比较 | LoRA 优于冻结 backbone，但未与全量微调 ESM2 比较 | 无法判断 LoRA 是否是最优适配策略 | 增加全量微调基线 | Results 段：LoRA vs frozen backbone，未提全量微调 |
| 仅用 STRING 一种网络 | 其他网络（如 BioGRID、HIPPIE）可能提供不同拓扑信息 | 结果可能依赖特定网络选择 | 多网络对比实验 | Methods 节：仅提及 STRING |
| 未讨论 IDR 构象/相分离机制 | RNA 结合在 IDR 中常伴随构象变化或相分离，本文未建模 | 对 IDP/IDR 课题读者，机制层面解释不足 | 结合 MD 模拟或相分离实验数据验证预测 | 摘要全文未涉及构象或相分离 |

---

## 14 Agent 提炼的知识候选

| 知识候选 | 可迁移性 | 如何迁移到本课题（IDP/IDR × 蛋白互作 × AI/物理模拟） |
|---------|---------|---------------------------------------------------|
| **多模态融合框架**：pLM 嵌入 + 网络拓扑 + FiLM 条件化 | 高 | 对 IDP/IDR 介导互作预测，可类似融合序列嵌入（如 ESM2/ProtTrans）与互作网络（如 STRING/BioGRID）或共表达网络，FiLM 条件化可让网络信息动态调制序列特征 |
| **LoRA 参数高效适配** | 高 | 对 IDP 相关任务微调大 pLM 时，LoRA 可在有限数据下获得优于增大冻结模型的效果，适合 IDP 数据集规模较小的场景 |
| **计算丙氨酸扫描用于 IDR 功能残基定位** | 高 | 对 IDR 中 RNA/DNA/蛋白结合关键残基预测，可类似逐残基突变评估预测变化，识别 IDR 内功能热点 |
| **网络级可解释性（PE 消融 + 逆 PCA）** | 中 | 对 IDP 互作预测，可识别蛋白在互作网络中的功能社区，推断 IDP 可能参与的凝聚体/复合物模块 |
| **挑战性子集评估策略** | 高 | 对 IDP/IDR 富集蛋白，应单独评估模型在「无经典结构域」子集上的表现，避免被结构域信号掩盖 |
| **PPR 位置编码作为互作上下文特征** | 中 | 对相分离相关蛋白，PPR 编码可能捕捉凝聚体网络中的 hub 特性，可尝试用于相分离蛋白预测 |
| **多模态互补性验证思路** | 高 | 通过消融实验证明「序列 + 网络」互补性，类似思路可用于「序列 + 结构 + 网络」或「序列 + MD 特征」融合 |

---

## 15 与已有知识连接

- **相似方法**：RBP-TSTL 和 HydRA（本文对比基线）代表现有 RBP 预测方法；本文的 FiLM 条件化融合思路与多模态学习中的特征调制方法一致（如 FiLM 在视觉问答中的应用，[Analysis] 外部知识）。
- **pLM 应用**：ESM2 作为蛋白质语言模型的代表，已被广泛用于功能预测；本文将其与网络拓扑结合，与 ProtST、ProteinBERT 等模型的多模态扩展方向一致（[Analysis] 外部知识）。
- **IDR 与 RNA 结合**：已知 IDR 在 RNA 结合和相分离中起重要作用（如 FUS、TDP-43 等），本文对 IDR 富集蛋白的专门评估与此领域直接相关（[Analysis] 外部知识，如 Calabretta & Richard, 2015; 未在本文引用）。
- **网络拓扑用于功能预测**：PPI 网络上的节点嵌入（如 Node2Vec、GNN）已被用于蛋白功能注释，本文的 PPR 编码是其中一种轻量级方案（[Analysis] 外部知识）。
- **可解释性方法**：计算丙氨酸扫描在蛋白质工程中常用，本文将其用于深度学习模型解释，与 in silico mutagenesis 方向一致（[Analysis] 外部知识）。
- **冲突/差异**：本文强调网络拓扑的增量价值，但未与纯 GNN 方法（直接在图上游走）比较，无法判断 PPR 编码是否最优网络特征化方式（[Analysis]）。

---

## 16 Agent 生成的研究候选

| 候选名称 | 来源局限/观察 | 核心假设 | 相对本文的增量 | 初步方法 | 验证方式 | 可能的失败模式 | 创新状态 |
|---------|-------------|---------|--------------|---------|---------|--------------|---------|
| **IDR-aware 多模态 RBP 预测器** | 本文虽评估 IDR 富集蛋白，但未显式建模 IDR 序列特性（如低复杂度、电荷分布） | 将 IDR 特异性特征（如电荷模式、疏水模式、预测无序分数）作为额外模态，可进一步提升 IDR 富集蛋白的 RBP 预测 | 在 RIBEX 基础上增加 IDR 特征通道 | 用 IUPred/AUCpred 预测无序分数，计算 IDR 序列物化特征，与 ESM2 嵌入和 PE 融合 | 在 RIC 和独立 IDR 相关 RBP 数据集上对比 RIBEX | IDR 特征与 ESM2 嵌入高度冗余，无增量 | unverified |
| **相分离蛋白互作网络嵌入** | 本文用 STRING 通用 PPI 网络，未针对相分离/凝聚体相关互作优化 | 使用相分离相关蛋白互作子网络（如 LLPS 数据库）计算 PE，可更好捕捉凝聚体介导的 RNA 结合上下文 | 网络选择从通用到功能特异 | 构建 LLPS 相关 PPI 子网络，计算 PPR，与通用网络对比 | 在已知相分离 RBP 集上评估预测和可解释性 | 相分离网络覆盖度低，丢失关键互作信息 | unverified |
| **动态 IDR 构象感知预测** | 本文为静态预测，未考虑 IDR 构象动态性对 RNA 结合的影响 | 结合 MD 模拟或 AlphaFold 预测的 IDR 构象系综特征，可提升对构象依赖型 RNA 结合的预测 | 从静态序列+网络到动态构象特征 | 对 IDR 区段进行粗粒化 MD 模拟，提取构象特征（如端到端距离、接触图），与序列嵌入融合 | 在构象依赖型 RBP 子集上对比静态模型 | MD 模拟成本高，构象特征噪声大 | unverified |
| **跨物种互作网络迁移** | 本文仅用人类 STRING，未验证跨物种泛化 | 网络拓扑编码的互作上下文具有跨物种保守性，可迁移到非人类 RBP 预测 | 从人类到多物种泛化 | 用人类训练的模型直接测试小鼠/果蝇 RBP，或构建多物种联合网络 | 跨物种 benchmark 评估 | 物种间网络结构差异大，迁移失败 | unverified |
| **凝聚体相关功能社区发现** | 本文可解释性识别功能社区，但未与相分离凝聚体组成直接关联 | 网络 PE 识别出的功能社区可能对应已知凝聚体组成模块 | 从预测到机制发现 | 将 PE 消融识别的高贡献社区与已知凝聚体蛋白组（如 PhaSepDB）比对 | 富集分析验证社区与凝聚体组成的重叠 | 社区与凝聚体组成无显著重叠 | unverified |
| **RNA 结合位点级 IDR 预测扩展** | 本文为蛋白级二分类，未到残基级 | 计算丙氨酸扫描的重要性分数可扩展为残基级 RNA 结合位点预测器 | 从蛋白级到残基级 | 用重要性分数作为弱监督信号，训练残基级预测头 | 与 eCLIP 或 RBPmap 实验数据对比 | 重要性分数噪声大，无法精确定位 | unverified |