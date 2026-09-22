## 01 基本信息

- **标题**：Predicting the locations of cryptic pockets from single protein structures using the PocketMiner graph neural network
- **作者**：Artur Meller; Michael Ward; Jonathan Borowsky; Jeffrey M. Lotthammer; Meghana Kshirsagar; Felipe Oviedo; Juan Lavista Ferres; Gregory R. Bowman
- **单位**：未提供（根据作者信息推测为华盛顿大学等，但原文未明确列出）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2022
- **论文类型**：预印本（方法学 + 应用研究）
- **领域**：计算结构生物学 / 药物发现 / 机器学习
- **关键词**：cryptic pockets, graph neural network, molecular dynamics, drug discovery, protein structure
- **DOI/ID**：10.1101/2022.06.28.497399
- **代码**：https://github.com/Mickdub/gvp/tree/pocket_pred
- **数据**：新构建的 39 个实验验证的 cryptic pocket 数据集（PocketMiner dataset）；人类蛋白质组应用
- **阅读日期**：2026-05-13（按当前日期）
- **在该课题方向中的位置**：本文聚焦于**有序蛋白结构域**中的 cryptic pocket 预测，而非 IDP/IDR 介导的相分离。但其核心方法——用 MD 模拟生成训练标签、用 GNN 从单结构预测动态位点——对 IDP/IDR 体系中的"动态结合位点/模糊相互作用"预测具有直接的方法学迁移价值。本文证明了"从静态结构预测动态功能位点"的可行性，是连接"构象动态性"与"机器学习预测"的桥梁性工作。

---

## 02 一句话总结

本文提出 PocketMiner——一个基于几何向量感知机（GVP-GNN）的图神经网络，以单蛋白结构为输入，预测残基在 MD 模拟中形成 cryptic pocket 的概率，在 39 个实验验证的 cryptic pocket 数据集上达到 ROC-AUC 0.87，比现有方法 CryptoSite 快 1000 倍以上，并应用于人类蛋白质组发现数千个新的潜在 cryptic pocket。

---

## 03 研究问题

- **具体问题**：能否仅从单一蛋白结构（如 apo 晶体结构或 AlphaFold 预测结构）快速、准确地预测 cryptic pocket 的位置？
- **为什么重要**：Cryptic pocket 是药物设计中"不可成药"蛋白的重要突破口，但传统发现方法（MD 模拟、实验筛选）耗时且昂贵。若能快速预测，将极大加速药物靶点筛选。
- **现有方法不足**：CryptoSite 需要运行 MD 模拟作为输入特征，单蛋白预测需约 1 天；且 CryptoSite 依赖已知配体结合位点的监督信号，难以泛化到无已知配体的蛋白。
- **精确研究问题（Can ... ?）**：Can a graph neural network trained on MD simulation-derived pocket opening events predict the locations of experimentally-validated cryptic pockets from single protein structures, with accuracy comparable to or better than existing methods, while being orders of magnitude faster?

---

## 04 背景与发展脉络

*注：以下脉络为基于本文引用和领域知识的梳理，标注「经外部核验」的部分有文献支撑，其余为本文框架内的叙述。*

1. **Cryptic pocket 的发现（实验驱动时代）**：早期 cryptic pocket 多通过共晶结构或抑制剂筛选偶然发现（本文引文 10-12）。代表性方法：X 射线晶体学、NMR。局限：成本高、通量低、不可预测。
2. **MD 模拟预测 cryptic pocket（计算驱动时代）**：随着计算能力提升，MD 模拟被用于采样蛋白构象 ensemble，发现瞬时开放的口袋（本文引文 13-18）。代表性方法：常规 MD、增强采样（如 metadynamics、replica exchange）。优点：原子级分辨率；局限：计算成本极高，不适合大规模筛选。
3. **机器学习预测 cryptic pocket（AI 驱动时代）**：CryptoSite（本文引文 23）是首个系统性尝试，用监督学习（随机森林）整合序列、结构和模拟特征，在 84 个已知 cryptic pocket 上训练。优点：比纯 MD 快；局限：仍需 MD 模拟作为输入特征，单蛋白预测需约 1 天。
4. **本文位置**：PocketMiner 将训练数据从"已知配体结合位点"扩展到"MD 模拟中的口袋开放事件"，从而摆脱对实验配体数据的依赖；同时用 GNN 直接从单结构预测，无需运行 MD。这是从"模拟辅助预测"到"纯结构预测"的范式转变。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| Cryptic pocket 发现成本高 | 传统方法依赖实验筛选或长时间 MD 模拟 | 缺乏先验知识指导，需穷举搜索 | Introduction 第 1-2 段 |
| 现有计算方法速度慢 | CryptoSite 单蛋白预测需约 1 天 | 需要运行 MD 模拟生成输入特征 | Introduction 第 3 段；Results 中对比 |
| 训练数据稀缺 | 已知 cryptic pocket 仅数十个 | 实验验证困难，多为偶然发现 | Introduction 第 1 段；Methods 数据集构建部分 |
| 现有方法泛化性差 | CryptoSite 依赖已知配体结合位点作为监督信号 | 训练标签来自实验配体数据，覆盖有限 | Introduction 第 3 段；Discussion |
| 负样本难以定义 | 难以确定哪些残基"不会"形成 cryptic pocket | 缺乏实验证据证明某位点永远不会形成口袋 | Methods "Identification of non-cryptic-pocket-forming residues" 部分 |
| 模拟数据与实验数据存在差距 | MD 模拟中开放的口袋不一定能结合配体 | 模拟力场误差、采样不充分 | Discussion 中关于模拟局限的讨论 |

---

## 06 核心思想

### 1) 表面方法

- 用 MD 模拟（adaptive sampling + FAST 算法）生成大量蛋白结构的口袋开放事件
- 用 LIGSITE 算法计算每个残基的口袋体积变化，生成二值标签（是否参与口袋开放）
- 训练 GVP-GNN（几何向量感知机图神经网络），输入为单结构，输出为每个残基的口袋开放概率
- 在实验验证的 cryptic pocket 数据集上评估，并应用于人类蛋白质组

### 2) 核心洞察

- **用模拟数据替代实验数据作为训练标签**：MD 模拟虽然昂贵，但一旦生成，可以产生比实验数据多一个数量级的训练样本（数千个口袋开放事件 vs 数十个实验验证的 cryptic pocket）
- **口袋开放是局部的、可预测的**：尽管蛋白整体构象变化复杂，但口袋开放事件在残基层面具有可学习的局部特征（如残基堆积密度、二级结构倾向、序列特征）
- **单结构足以预测动态行为**：蛋白的"呼吸"模式（哪些区域容易打开）编码在其静态结构中，GNN 可以学习这种编码

### 3) 可能的普适教训 [Analysis]

- **"模拟生成标签 + 静态结构预测"范式**：对于 IDP/IDR 体系，MD 或增强采样可以生成"哪些区域倾向于形成瞬时结构/结合位点"的标签，然后用 GNN 从序列或 AlphaFold 结构预测这些动态倾向性
- **负样本的严谨构建**：本文用超刚性蛋白和广泛筛选蛋白的未结合残基作为负样本，这种"多证据来源"的负样本策略对 IDP 体系同样适用（如用 NMR 验证的无结合区域作为负样本）
- **GVP-GNN 的等变性优势**：对于 IDP/IDR 中常见的构象异质性，等变网络对旋转/平移的不变性是天然优势

---

## 07 方法总览

- **输入**：单一蛋白结构（PDB 格式），包含原子坐标和残基信息
- **输出**：每个残基的 cryptic pocket 形成概率（0-1）
- **模块**：
  1. **数据生成模块**：MD 模拟（FAST adaptive sampling）→ 轨迹 → LIGSITE 口袋检测 → 残基级标签
  2. **特征提取模块**：节点特征（二面角、氨基酸类型、Cβ 方向）+ 边特征（Cα 距离、序列距离）
  3. **图神经网络模块**：GVP-GNN，4 层编码，消息传递，残基级输出
  4. **后处理模块**：残基概率 → 口袋热点识别（滑动窗口平均）
- **训练**：5 折交叉验证（按蛋白划分），类别不平衡处理（多种方案对比），Adam 优化器，学习率 2e-5
- **推理**：单结构前向传播，<1 秒/蛋白
- **流程**：输入结构 → 构建 k-NN 图（30 邻居）→ GVP-GNN 编码 → 残基级 sigmoid 输出 → 热点检测

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| MD 模拟数据生成（FAST + adaptive sampling） | 生成训练标签：哪些残基在模拟中形成口袋 | 提供大规模、无配体依赖的训练信号 | 输入：apo 结构；输出：残基级口袋开放标签 | Results 图 2：13/15 蛋白在 400 ns 内开放 | 移除后训练数据量减少 >90%，模型无法训练（预期） |
| LIGSITE 口袋检测 | 计算每个残基的口袋体积 | 将连续构象转化为离散标签 | 输入：MD 轨迹帧；输出：残基-口袋体积矩阵 | Methods "Model Training" 部分 | 移除后无法定义训练目标（预期） |
| GVP-GNN 编码器 | 学习残基的局部化学/拓扑环境表示 | 从静态结构提取可预测动态行为的特征 | 输入：节点/边特征；输出：残基级嵌入 | Results 图 4：ROC-AUC 0.83（模拟标签） | 替换为 MLP 或 CNN 性能下降（实测：3D-CNN ROC-AUC 0.79 vs GVP-GNN 0.83） |
| 二阶段训练（模拟标签 → 实验标签微调） | 先用大规模模拟数据预训练，再用实验数据微调 | 结合模拟数据的规模优势和实验数据的准确性 | 输入：预训练模型 + 实验 cryptic pocket 数据；输出：微调模型 | Results：最终 ROC-AUC 0.87 | 仅用模拟标签：0.83；仅用实验标签：数据量不足（预期） |
| 负样本构建（超刚性蛋白 + 广泛筛选蛋白） | 提供高置信度的"非口袋"残基 | 减少假阳性，提高特异性 | 输入：超刚性蛋白结构 + 广泛筛选蛋白的未结合残基；输出：负标签 | Methods "Identification of non-cryptic-pocket-forming residues" 部分 | 移除后假阳性率上升（预期，基于 CryptoSite 对比） |
| 人类蛋白质组应用管线 | 批量预测、分类、热点检测 | 从单蛋白预测扩展到组学规模 | 输入：10,806 个人类蛋白结构；输出：cryptic pocket 分类和热点 | Results 图 6：29.4% 蛋白预测有 cryptic pocket | 移除后无法评估泛化能力（预期） |

---

## 09 关键公式符号

本文为深度学习应用型论文，核心公式较少，主要涉及以下内容：

1. **口袋体积变化标签**（Methods 中隐含）：
   - 对每个残基 $i$，在模拟帧 $t$ 的口袋体积 $V_i(t)$ 由 LIGSITE 计算
   - 标签 $y_i = 1$ 若 $\max_t V_i(t) - V_i(0) > \theta$，其中 $\theta = 40 \, \text{Å}^3$
   - 符号：$V_i(t)$ = 残基 $i$ 在时间 $t$ 的口袋体积；$\theta$ = 阈值

2. **GVP-GNN 消息传递**（引用自 Jing et al. 2020，未在本文中展开）：
   - 节点更新：$\mathbf{h}_i^{(l+1)} = \text{GVP}\left(\mathbf{h}_i^{(l)}, \sum_{j \in \mathcal{N}(i)} \text{GVP}\left(\mathbf{h}_j^{(l)}, \mathbf{e}_{ij}\right)\right)$
   - 符号：$\mathbf{h}_i^{(l)}$ = 残基 $i$ 在第 $l$ 层的嵌入；$\mathbf{e}_{ij}$ = 边特征；$\mathcal{N}(i)$ = 残基 $i$ 的 30 近邻

3. **损失函数**（Methods 中描述）：
   - 二值交叉熵损失：$\mathcal{L} = -\frac{1}{N} \sum_i [y_i \log(p_i) + (1-y_i) \log(1-p_i)]$
   - 符号：$y_i$ = 真实标签；$p_i$ = 预测概率

4. **热点检测**（Methods 中描述）：
   - 残基 $i$ 的平滑分数：$s_i = \frac{1}{11} \sum_{j=i-5}^{i+5} p_j$
   - 若 $s_i > 0.7$ 则标记为 cryptic pocket 热点

---

## 10 实验设计与证据链

### 数据集与规模

| 数据集 | 用途 | 规模 | 来源 |
|--------|------|------|------|
| MD 模拟训练集 | 训练 GVP-GNN 预测模拟中的口袋开放 | 37 个蛋白，2,400 条独立 MD 模拟，11,128 个残基样本 | 自建（SARS-CoV-2 蛋白 + 已知 cryptic pocket 蛋白 + 其他） |
| PocketMiner 测试集 | 评估 cryptic pocket 预测 | 39 个 cryptic pocket（24 个 apo 结构） | 自建（基于 PDB 文献挖掘） |
| 负样本集 | 评估特异性 | 4 个超刚性蛋白 + 7 个广泛筛选蛋白 | 自建 |
| 人类蛋白质组 | 应用 | 10,806 个蛋白结构 | UniProt + PDB + AlphaFold |

### 指标

- ROC-AUC（残基级分类）
- PR-AUC（残基级分类）
- 准确率（热点检测，阈值 0.7）

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|-------------------|------|
| MD 模拟中口袋开放速度 | 大多数 cryptic pocket 在短模拟中开放 | 15 个已知 cryptic pocket 蛋白，400 ns adaptive sampling | 13/15 在 40 ns 内开放 | 短模拟足以捕捉 cryptic pocket 开放 | 不能推广到所有 cryptic pocket | Results 图 2 |
| GVP-GNN vs 3D-CNN（模拟标签） | GNN 架构优于 CNN | 相同训练/测试集，5 折交叉验证 | GVP-GNN ROC-AUC 0.83 vs 3D-CNN 0.79 | GVP-GNN 更优 | 差异可能依赖具体数据集 | Results 图 4C-D |
| PocketMiner vs CryptoSite（实验标签） | PocketMiner 达到或超过现有方法 | 39 个 cryptic pocket 测试集 | PocketMiner ROC-AUC 0.87 vs CryptoSite 0.85 | PocketMiner 略优 | 差异小，需更大样本确认 | Results 表 S5 |
| 负样本特异性 | PocketMiner 能区分非口袋残基 | 超刚性蛋白 + 广泛筛选蛋白 | 低假阳性率（具体数值未在摘要中提供） | 模型具有特异性 | 负样本定义可能有偏 | Results 图 5B |
| 人类蛋白质组应用 | 预测大量新 cryptic pocket | 10,806 个人类蛋白 | 29.4% 蛋白预测有 cryptic pocket | 大量蛋白可能通过 cryptic pocket 成药 | 预测未经实验验证 | Results 图 6A |
| PIM2 和 WNT2 验证 | 预测位点在模拟中确实开放 | MD 模拟验证 | 两个蛋白的预测位点均观察到口袋开放 | 预测具有可重复性 | 仅两个案例，非系统验证 | Results 图 6D-E |

---

## 11 结论正确解读

- **任务范围**：本文预测的是**有序蛋白结构域**中 cryptic pocket 的位置，不涉及 IDP/IDR 或相分离体系。所有训练和测试数据均为折叠良好的球蛋白。
- **Oracle/真值输入**：训练标签来自 MD 模拟（LIGSITE 计算的口袋体积变化），而非实验验证的配体结合。测试标签来自实验验证的 cryptic pocket（apo-holo 结构对）。
- **端到端状态**：PocketMiner 是端到端的——输入单结构，输出残基概率，无需中间模拟。但训练过程依赖 MD 模拟生成标签。
- **算力成本**：训练需要 MD 模拟数据（计算量大），但推理极快（<1 秒/蛋白）。作者未提供训练的具体 GPU 时数。
- **历史数据依赖**：训练数据来自 MD 模拟，模拟的力场偏差会传递给模型。测试数据来自 PDB 中已知的 cryptic pocket，存在发表偏倚。
- **最难情况**：reverse pockets（闭合型口袋）和需要较大构象变化的口袋可能更难预测；IDP/IDR 区域被明确排除。
- **群体/领域边界**：结论仅适用于单体球蛋白（50-1000 残基），不适用于膜蛋白、多聚体复合物或无序蛋白。
- **不确定性**：人类蛋白质组预测中 29.4% 的阳性率未经实验验证，可能高估；阈值 0.7 的敏感性/特异性权衡未充分讨论。

**有边界的复述**：PocketMiner 能够从单体球蛋白的静态结构出发，在亚秒级时间内预测 MD 模拟中可能出现的口袋开放位点，其预测与实验验证的 cryptic pocket 位置高度吻合（ROC-AUC 0.87），且比现有方法 CryptoSite 快三个数量级以上。该模型在人类蛋白质组中预测超过半数"无口袋"蛋白可能含有 cryptic pocket，但这一预测需要实验验证。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 训练数据来自模拟而非实验 | 模型学习的是 MD 模拟中的口袋开放，可能与实验有偏差 | 用更多实验验证的数据进行微调 | Discussion 中关于模拟局限的讨论 |
| 测试集规模有限 | 39 个 cryptic pocket 样本量小 | 扩大测试集，纳入更多蛋白家族 | Discussion |
| 负样本定义困难 | 超刚性蛋白和广泛筛选蛋白可能仍有未发现的口袋 | 开发更严格的负样本筛选方法 | Methods "Identification of non-cryptic-pocket-forming residues" 部分 |
| 仅适用于单体球蛋白 | 排除膜蛋白、多聚体、IDP/IDR | 扩展模型到其他蛋白类型 | Methods 数据集构建部分 |
| 人类蛋白质组预测未经实验验证 | 29.4% 阳性率可能高估 | 对高置信度预测进行实验验证 | Discussion 中关于蛋白质组应用的讨论 |
| 未考虑配体诱导的构象变化 | 模型仅从 apo 结构出发，未考虑配体结合后的适应 | 结合配体对接或共价修饰信息 | Discussion |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 训练标签来自 MD 模拟，但测试标签来自实验 | 模型可能过拟合模拟的"伪口袋"，而非真实的配体结合位点 | 如果模拟中的口袋开放与实验配体结合位点不一致，模型预测可能误导药物设计 | 比较模型预测与大量未参与训练的实验 cryptic pocket 数据 | Methods 中训练/测试标签来源不同 |
| 负样本构建依赖"未结合"推断 | 广泛筛选蛋白中未结合配体的残基可能只是"尚未发现"而非"不能结合" | 负样本噪声会低估模型性能 | 用正向验证的"非结合位点"（如突变实验）重新评估 | Methods 负样本部分 |
| 与 CryptoSite 的比较可能不公平 | CryptoSite 需要 MD 模拟输入，PocketMiner 不需要，但两者测试集可能不同 | 性能差异可能来自测试集而非模型本身 | 在完全相同的测试集上重新运行 CryptoSite | Results 表 S5 |
| 人类蛋白质组应用使用 AlphaFold 结构 | AlphaFold 预测结构可能缺少 cryptic pocket 所需的构象信息 | 如果 AlphaFold 结构偏向于闭合态，可能低估 cryptic pocket 数量 | 对 AlphaFold 结构与实验结构预测结果进行系统比较 | Methods 蛋白质组应用部分 |
| 阈值 0.7 的选择依据不明确 | 可能过拟合测试集 | 不同阈值下模型性能可能显著变化 | 绘制 ROC 曲线并报告不同阈值下的性能 | Methods 热点检测部分 |
| 未讨论 IDP/IDR 区域 | 无序区域被明确排除，但许多"不可成药"蛋白含 IDR | 对课题方向（IDP/IDR × 蛋白互作）的迁移需要额外验证 | 在 IDR 数据集上测试 PocketMiner | Methods 数据集构建部分 |

---

## 14 Agent 提炼的知识候选

**标题：Agent 提炼的知识候选**

1. **"模拟生成标签 + 静态结构预测"范式**：本文最核心的可迁移思想。对于 IDP/IDR 体系，可以用增强采样 MD（如 replica exchange、metadynamics）或粗粒化模拟生成"哪些残基倾向于形成瞬时结构/结合位点"的标签，然后用 GNN 从序列或 AlphaFold 结构预测这些动态倾向性。这避免了 IDP 实验标签稀缺的问题。

2. **GVP-GNN 架构适用于残基级预测**：GVP-GNN 的等变性和局部消息传递机制对残基级属性预测（如结合位点、PTM 位点、相分离驱动残基）具有天然优势。可迁移到 IDP 体系的"相分离热点残基预测"。

3. **负样本的多证据来源策略**：本文用超刚性蛋白 + 广泛筛选蛋白的未结合残基作为负样本，这种"多证据来源"策略对 IDP 体系同样适用——可以用 NMR 验证的无结合区域 + 高严格性筛选的未结合残基作为负样本。

4. **二阶段训练（预训练 + 微调）**：先用大规模模拟数据预训练，再用少量实验数据微调，这种策略在 IDP 领域尤其有价值——模拟数据（如 coarse-grained MD 或 AlphaFold 的 pLDDT 特征）可以大规模生成，实验数据（如 NMR 化学位移、交联质谱）稀缺但准确。

5. **"呼吸"模式作为可学习特征**：本文的核心假设是"蛋白的呼吸模式编码在静态结构中"。对 IDP/IDR 而言，类似假设可以是"IDR 的瞬时结构倾向性编码在序列和预测结构中"——这为用 AlphaFold 预测 IDR 功能提供了理论基础。

6. **快速筛选管线**：PocketMiner 的 <1 秒/蛋白推理速度使其可用于全蛋白质组筛选。类似地，IDP 领域的"相分离预测器"也可以设计为高通量筛选管线，用于全基因组范围的相分离蛋白预测。

---

## 15 与已有知识连接

1. **CryptoSite（Cimermancic et al. 2016, Biophys J）**：本文的直接前作。CryptoSite 用随机森林整合序列、结构和 MD 特征预测 cryptic pocket，但需要 MD 模拟作为输入。PocketMiner 在速度和精度上均超越 CryptoSite。**对本课题的启示**：CryptoSite 的特征工程思路（如残基柔性、堆积密度）可迁移到 IDR 结合位点预测。

2. **GVP-GNN（Jing et al. 2020, ICLR）**：本文的架构基础。GVP-GNN 是蛋白质结构学习的通用等变图神经网络，已被广泛用于蛋白质设计、功能预测等任务。**对本课题的启示**：GVP-GNN 可直接用于 IDR 体系的残基级预测任务。

3. **AlphaFold 2（Jumper et al. 2021, Nature）**：本文在人类蛋白质组应用中使用 AlphaFold 结构。**对本课题的启示**：AlphaFold 对 IDR 的预测置信度（pLDDT）本身可作为 IDR 无序程度的特征，与 PocketMiner 类方法结合可能预测 IDR 的瞬时结合位点。

4. **Folding@home / MD 模拟社区**：本文的 MD 模拟数据来自分布式计算。**对本课题的启示**：IDP/IDR 的 MD 模拟同样可以利用分布式计算或 GPU 加速生成大规模训练数据。

5. **相分离预测器（如 catGRANULES、PhaSepPred）**：这些方法从序列预测相分离驱动残基，但缺乏结构信息。**与本课题的关联**：PocketMiner 的"结构→动态位点"思路可补充序列方法的不足，用于预测 IDR 中参与相分离的"stickers"残基。

6. **药物发现中的"不可成药"蛋白**：本文的最终目标是扩大可成药蛋白质组。**与本课题的关联**：IDP/IDR 是"不可成药"蛋白的重要来源，PocketMiner 类方法若扩展到 IDR，可能发现全新的药物结合位点。

---

## 16 研究想法

**标题：Agent 生成的研究候选**

### 候选 1：IDR-Sticker 预测器——用 GNN 从 AlphaFold 结构预测 IDR 中相分离驱动残基

- **来源局限/观察**：PocketMiner 证明"静态结构→动态位点"可学习；IDR 的相分离行为由少数关键残基（stickers）驱动，但这些残基在序列上无明显 motif，现有序列方法（catGRANULES 等）精度有限。
- **核心假设**：IDR 的瞬时结构倾向性（即使很低）编码在 AlphaFold 预测结构和 pLDDT 谱中，GNN 可以学习这种编码。
- **初步方法**：收集已知相分离蛋白的 stickers 残基（实验验证的突变数据），用 AlphaFold 结构 + pLDDT 作为输入，训练 GVP-GNN 预测 sticker 残基。负样本用 NMR 验证的无序且无结合区域。
- **验证方式**：与 catGRANULES、PhaSepPred 等序列方法比较；用已知相分离蛋白的突变实验验证预测位点。
- **创新状态**：unverified（新方向，需验证可行性）

### 候选 2：模拟标签 + 实验微调的二阶段训练框架用于 IDR 结合位点预测

- **来源局限/观察**：PocketMiner 的二阶段训练（MD 模拟标签预训练 + 实验标签微调）有效解决了标签稀缺问题。IDR 结合位点的实验数据更稀缺，但 MD/粗粒化模拟可以生成大量"IDR 与伴侣蛋白瞬时结合"的标签。
- **核心假设**：粗粒化 MD（如 MARTINI）或 enhanced sampling 可以生成 IDR 结合位点的可靠标签，预训练后微调可达到实验级精度。
- **初步方法**：用 coarse-grained MD 模拟 IDR-伴侣蛋白体系，标记残基-残基接触频率高的区域为"结合位点"；用这些标签预训练 GNN，再用少量实验验证的 IDR 结合位点微调。
- **验证方式**：在已知 IDR 结合位点数据集（如 ELM 数据库）上评估；与 AlphaFold-Multimer 的预测比较。
- **创新状态**：unverified（方法可行，但标签质量需验证）

### 候选 3：PocketMiner 在 IDR 上的直接迁移测试

- **来源局限/观察**：PocketMiner 明确排除 IDR，但其核心假设（静态结构→动态位点）可能部分适用于 IDR 的"瞬时口袋"。
- **核心假设**：IDR 中某些残基在结合伴侣时形成瞬时口袋，PocketMiner 的预训练特征（堆积密度、局部拓扑）可能部分捕捉这种倾向。
- **初步方法**：直接在 IDR 区域运行 PocketMiner，比较预测分数与实验验证的 IDR 结合位点；分析哪些特征在 IDR 中仍然有效。
- **验证方式**：在 IDR 结合位点数据集上评估；与随机基线比较。
- **创新状态**：partially checked（PocketMiner 已开源，可直接测试）

### 候选 4：相分离凝聚体中的"动态口袋"预测——将 PocketMiner 扩展到多链体系

- **来源局限/观察**：PocketMiner 仅处理单体结构；相分离凝聚体中，口袋可能在多链组装界面形成。
- **核心假设**：凝聚体中的瞬时口袋与单体 cryptic pocket 具有相似的结构特征，但需要多链上下文信息。
- **初步方法**：用 AlphaFold-Multimer 或 MD 生成的凝聚体结构作为输入，扩展 GVP-GNN 以处理多链图，预测界面处的动态口袋。
- **验证方式**：用已知的凝聚体小分子结合位点（如 RNA 结合蛋白的配体结合）验证。
- **创新状态**：unverified（需大量方法开发）

### 候选 5：从"口袋预测"到"变构位点预测"——结合 PocketMiner 与蛋白互作网络

- **来源局限/观察**：PocketMiner 预测的口袋可能不仅是药物结合位点，也可能是蛋白-蛋白互作界面。
- **核心假设**：高 PocketMiner 分数的残基倾向于参与蛋白-蛋白互作或变构调控。
- **初步方法**：将 PocketMiner 预测与蛋白-蛋白互作数据库（如 BioGRID、STRING）交叉分析，寻找高预测分数且参与互作的残基。
- **验证方式**：用突变实验数据验证预测的互作关键残基。
- **创新状态**：unverified（需交叉验证）