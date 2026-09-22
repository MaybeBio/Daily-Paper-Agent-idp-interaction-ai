## 01 基本信息

- **标题**：SETH predicts nuances of residue disorder from protein embeddings
- **作者与单位**：Ilzhoefer D; Heinzinger M; Rost B（慕尼黑工业大学，Rostlab）
- **期刊/预印本平台**：bioRxiv
- **年份**：2022
- **论文类型**：预印本（方法学/基准测试论文）
- **领域**：蛋白质生物信息学、无序蛋白预测、蛋白质语言模型
- **关键词**：intrinsically disordered regions (IDRs)、protein language model、ProtT5、CheZOD、embeddings、CNN、AlphaFold2
- **DOI/arXiv 号**：10.1101/2022.06.23.497276
- **代码**：https://github.com/Rostlab/SETH
- **数据**：训练集 CheZOD1174（1174 蛋白）、测试集 CheZOD117（117 蛋白）；预测结果：https://doi.org/10.5281/zenodo.6673817
- **阅读日期**：未提供
- **在课题方向中的位置**：本文属于「IDP/IDR 预测 × 蛋白质语言模型」交叉方向，核心贡献是证明单序列 pLM embedding（ProtT5）配合浅层 CNN 即可在连续无序尺度（CheZOD）上超越依赖 MSA 的复杂方法，并展示了无序预测与 AlphaFold2 pLDDT 的互补性及无序谱系与物种进化的关联。对 IDP/IDR 介导的蛋白互作研究而言，本文提供了无需 MSA、可大规模快速预测残基级无序程度的工具，可作为互作界面中 IDR 注释的预处理步骤。

## 02 一句话总结

本文提出 SETH——一个以 ProtT5 蛋白质语言模型 embedding 为唯一输入、两层 CNN 为架构的浅层模型，在 NMR 衍生的连续无序尺度（CheZOD 分数）上预测残基级无序程度，在 CheZOD117 测试集上以 Spearman ρ≈0.75 超越 26 种既有方法（含依赖 MSA 的方法），并可在单张 RTX 3060 上约 1 小时完成人类蛋白质组的无序预测。

## 03 研究问题

- **具体问题**：能否仅用单条蛋白质序列的 pLM embedding（无需 MSA、无需手工特征）预测残基级无序程度，且在连续尺度（而非二元分类）上达到或超越现有依赖 MSA 的复杂方法？
- **为什么重要**：IDR 与多种疾病（如阿尔茨海默病）相关，且无序蛋白在相分离、信号传导等过程中发挥关键作用。现有方法依赖 MSA，而 IDR 区域本身比对困难、MSA 生成计算昂贵，限制了大规模蛋白质组层面的无序注释。
- **现有方法为何不足**：① 多数方法依赖 MSA，IDR 区域序列保守性低，MSA 质量差；② 多数方法输出二元分类（有序/无序），丢失了残基级无序程度的细微差异；③ 复杂模型（如深度残差网络）参数量大、推理慢，难以扩展到蛋白质组规模。
- **精确研究问题（Can...?）**：Can a shallow CNN trained on ProtT5 embeddings from single protein sequences predict continuous CheZOD disorder scores with accuracy comparable to or exceeding MSA-based state-of-the-art methods, while being fast enough for proteome-scale application?

## 04 背景与发展脉络

> 注：以下脉络基于本文框架，部分经外部核验标注。

1. **早期无序预测（~2000-2010）**：基于氨基酸组成、疏水性等手工特征，如 PONDR、IUPred、DISOPRED2。优点：可解释、快速；局限：精度有限，多为二元分类。
2. **基于 MSA 与进化信息的预测（~2010-2020）**：如 SPOT-Disorder、PrDOS、AUCpreD。利用 MSA 中的进化信息提升精度。优点：精度显著提升；局限：IDR 区域 MSA 质量差、计算开销大、推理慢。
3. **深度学习方法（~2015-2021）**：如 flDPnn、ODiNPred，使用更复杂的网络架构和更多特征。优点：精度进一步提升；局限：仍依赖 MSA 或大量手工特征，模型复杂、推理慢。
4. **蛋白质语言模型（~2019-2022）**：如 SeqVec、ESM-1b、ProtBERT、ProtT5，通过自监督学习从海量序列中捕获蛋白质序列的隐式进化与结构信息。优点：单序列即可生成信息丰富的 embedding，无需 MSA；局限：直接用于下游任务时需适配。
5. **本文位置**：首次系统比较 5 种 pLM embedding 用于无序预测，证明 ProtT5 embedding + 浅层 CNN（SETH）在连续 CheZOD 尺度上超越 26 种既有方法（含 MSA 依赖方法），并展示其蛋白质组级推理速度与 AlphaFold2 预筛潜力。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| MSA 依赖限制可扩展性 | 现有 SOTA 方法需先生成 MSA，IDR 区域比对困难且计算昂贵 | IDR 序列保守性低，MSA 质量差；MSA 生成是计算瓶颈 | Methods 2.1；Results 3.4（SETH 速度对比） |
| 二元分类丢失无序细微差异 | 多数方法仅输出有序/无序，无法区分短无序、长无序、部分无序 | 训练标签为二元，模型未学习连续尺度 | Results 3.3（SETH 对短/长无序的区分分析） |
| 复杂模型推理慢 | 深度模型参数量大，蛋白质组规模预测耗时 | 模型复杂度与推理速度的权衡 | Results 3.4（人类蛋白质组约 1 小时） |
| IDR 区域 MSA 质量差 | 无序区域序列保守性低，MSA 比对不可靠 | IDR 进化压力不同于有序区域 | Introduction（IDR 比对困难） |
| 训练-测试分布偏移 | 训练集有序残基占 72%，测试集仅 31% | 数据来源不同（NMR 实验 vs 其他） | Methods 2.1；Results 3.2（分布差异分析） |

## 06 核心思想

1. **表面方法**：用 ProtT5 蛋白质语言模型对单条序列生成逐残基 embedding（1024 维），输入一个两层 CNN（SETH）回归预测连续 CheZOD 分数；同时训练了 LogReg（二元分类）、LinReg（线性回归）、ANN（两层全连接）作为对比模型。

2. **核心洞察**：pLM embedding 在自监督预训练中已隐式捕获了序列-结构-功能关系，包括无序相关信息。因此，一个极浅的 CNN 就足以在连续无序尺度上超越依赖 MSA 的复杂方法——这挑战了「无序预测必须依赖 MSA 进化信息」的假设。作者进一步发现，ProtT5 的 1024 维 embedding 中，单一维度（第 295 维）就携带了 86%-96% 的预测信号，说明无序信息在 pLM 表征中高度集中。

3. **可能的普适教训** [Analysis]：① 预训练 pLM embedding 的「零样本」信息密度可能远超预期，下游任务中应首先尝试简单模型而非复杂架构；② 连续尺度标签（如 CheZOD）比二元标签能捕获更多生物学细微差异，且与进化信号（物种聚类）关联更强；③ 模型速度与精度的权衡可通过「预训练 embedding + 浅层头」实现，而非必须依赖复杂模型。

## 07 方法总览

- **输入**：单条蛋白质氨基酸序列（无 MSA、无手工特征）
- **输出**：逐残基 CheZOD 分数（连续值，越高越无序）
- **模块**：
  1. **Embedding 生成**：5 种 pLM（SeqVec、ProtBERT、ESM-1b、ProtT5、ProSE）生成逐残基 embedding；ProtT5 为最终选择（1024 维/残基）
  2. **预测头**：SETH = 两层 CNN（Conv2d，kernel size (5,1)，28 个输出通道，Tanh 激活，weight decay 0.001，Adam 优化器，MSELoss）；对比模型：LogReg、LinReg、LinReg1D（仅第 295 维）、ANN
  3. **AlphaFold2 对比**：对 CheZOD117 运行 ColabFold，提取 pLDDT、实验可溶性（experimentally resolved）、RSA 作为无序预测的替代指标
  4. **进化分析**：将 37 个物种的 CheZOD 分数分布转换为 8 维向量，PCA 降维后观察物种聚类
- **训练**：CheZOD1174（1174 蛋白，132,545 残基），90% 训练 / 10% 验证；测试集 CheZOD117（117 蛋白，13,069 残基）
- **评测**：Spearman ρ（连续）和 AUC（二元化，阈值 8）
- **流程**：序列 → ProtT5 embedding（1024 维/残基）→ CNN 卷积 → 逐残基 CheZOD 预测分数

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| ProtT5 embedding | 将序列编码为信息丰富的逐残基向量 | 捕获序列中隐式的结构/功能/无序信息，替代 MSA | 输入：氨基酸序列；输出：L×1024 矩阵 | Results 3.1（ProtT5 优于其他 4 种 pLM）；Fig. 1 | 预期显著性能下降（其他 pLM 均不如 ProtT5）；若替换为 one-hot，性能大幅下降（Fig. 1） |
| 两层 CNN（SETH） | 从 embedding 中提取局部上下文特征并回归 CheZOD | 捕获相邻残基对无序程度的协同影响 | 输入：L×1024；输出：L×1 | Results 3.2（SETH ρ 最高）；Fig. 3 | 预期性能下降（SETH 优于 ANN 和 LinReg，但差异未达统计显著） |
| 第 295 维（LinReg1D） | 单维度线性回归 | 验证无序信息在 embedding 中的集中程度 | 输入：L×1；输出：L×1 | Results 3.5（ρ=0.61，达 LinReg 的 89%） | 预期大幅性能下降（但仍优于多数非 pLM 方法） |
| AlphaFold2 衍生指标 | pLDDT、experimentally resolved、RSA 作为无序替代 | 对比 SOTA 结构预测器的无序判别能力 | 输入：序列；输出：逐残基分数 | Results 3.6（ρ=0.56-0.64，低于 SETH） | 不适用（对比基线） |
| 8 维 CheZOD 谱向量 + PCA | 物种级无序谱系比较 | 验证无序预测的进化生物学意义 | 输入：物种全部蛋白的 CheZOD 预测；输出：2D PCA 图 | Results 3.7（Fig. 6，物种按进化关系聚类） | 不适用（分析工具） |

## 09 关键公式符号

1. **Spearman 相关系数**：
   ρ = cov(u, v) / (σ_u · σ_v)
   其中 u、v 分别为真实和预测 CheZOD 分数的秩次。用于评估连续预测精度。

2. **AUC（ROC 曲线下面积）**：
   AUC = ∫₀¹ TPR(FPR⁻¹(x)) dx
   其中 TPR 为真阳性率，FPR 为假阳性率。用于评估二元分类性能（阈值 CheZOD ≤ 8 为无序）。

3. **CheZOD 分数**（来自 Nielsen & Mulder）：
   CheZOD = (δ_obs - δ_random) / σ_random
   基于 NMR 化学位移观测值与随机卷曲预测值的标准化差异，正值表示有序，负值表示无序。

4. **CNN 卷积操作**（SETH 核心）：
   y_i = f(Σ_j Σ_k W_jk · x_{i+j,k} + b)
   其中 W 为卷积核（5×1），x 为 embedding 矩阵，f 为 Tanh 激活函数。

5. **MSA 序列同一性**：
   PIDE = (相同残基数 / 比对长度) × 100%
   用于冗余去除（阈值 20%）。

## 10 实验设计与证据链

**数据集**：
- 训练集：CheZOD1174（1174 蛋白，132,545 残基），由 ODiNpred 的 CheZOD1325 经冗余去除（PIDE<20%）得到
- 测试集：CheZOD117（117 蛋白，13,069 残基），与 26 种方法比较的公共基准
- 17-ORGANISM 集：105,881 蛋白，47M 残基（用于 SETH vs AlphaFold2 比较）
- 37 个 Swiss-Prot 物种（≥1500 蛋白）用于进化分析

**指标**：Spearman ρ（连续）、AUC（二元）

**基线/对比方法**：26 种既有无序预测方法（含 SPOT-Disorder、flDPnn、ODiNPred、AUCpreD 等，来自 Nielsen & Mulder 2019 基准）；AlphaFold2 衍生指标（pLDDT、experimentally resolved、RSA）

**硬件**：单张 NVIDIA RTX A6000（48GB）或 RTX 3060（12GB）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 5 种 pLM embedding 比较 | 不同 pLM 对无序预测的适用性 | 线性回归 + 5 种 pLM embedding vs one-hot | ProtT5 最优（ρ 最高）；所有 pLM 均优于 one-hot | pLM embedding 携带无序信息 | 无法确定最优 pLM 是否在更大数据集上仍最优 | Results 3.1；Fig. 1 |
| SETH vs 26 种方法 | 单序列 pLM 方法能否超越 MSA 方法 | SETH vs 26 种方法（CheZOD117） | SETH ρ 最高（≈0.75），AUC 最高 | 单序列 pLM 方法可超越 MSA 方法 | 统计显著性仅对部分方法成立 | Results 3.2；Fig. 3 |
| 模型复杂度比较 | 更复杂模型是否更好 | SETH (CNN) vs ANN vs LinReg vs LogReg | SETH 数值最优，但与 ANN/LinReg 差异不显著 | 浅层模型足够；回归优于分类 | 无法排除更大模型在更多数据上更优 | Results 3.2；Fig. 3 |
| 短 vs 长无序分析 | SETH 能否区分无序细微差异 | SETH 对短（<30 残基）和长（≥30 残基）无序的预测 | 短无序 ρ=0.41±0.04，长无序更高 | SETH 对长无序更准确，短无序仍有挑战 | 短无序预测误差的具体来源未完全阐明 | Results 3.3；Fig. 4 |
| SETH vs AlphaFold2 指标 | pLM 方法 vs 结构预测器作为无序预测器 | SETH vs pLDDT、experimentally resolved、RSA | SETH ρ 显著更高（0.75 vs 0.56-0.64） | SETH 优于 AlphaFold2 衍生无序指标 | AlphaFold2 在特定蛋白子集上可能更优 | Results 3.6；Fig. 3 |
| 速度基准 | SETH 是否足够快 | SETH vs AlphaFold2 推理时间 | SETH 快约 170 倍 | SETH 适合大规模预筛 | 未与其他 pLM 方法（如 ADOPT）直接对比速度 | Results 3.4 |
| 物种 CheZOD 谱 PCA | 无序谱系是否反映进化关系 | 37 物种 8 维 CheZOD 谱 PCA | 真核/原核分离，门级聚类可见 | 无序组成与进化相关 | 样本量有限，不能推广到所有物种 | Results 3.7；Fig. 6 |

## 11 结论正确解读

- **任务范围**：本文仅针对 CheZOD 分数定义的无序程度预测，未直接评估二元无序/有序分类的 SOTA 对比（但 AUC 指标覆盖了二元视角）。
- **Oracle/真值输入**：训练和测试标签均为 NMR 衍生的 CheZOD 分数，非实验验证的无序区域注释（如 X 射线缺失残基）。CheZOD 本身是间接测量。
- **端到端状态**：SETH 是「pLM embedding + 浅层 CNN」的端到端流程，但 pLM（ProtT5）本身是预训练模型，未针对无序任务微调。
- **算力成本**：推理极快（人类蛋白质组约 1 小时/RTX 3060），但 ProtT5 embedding 生成需 GPU；训练成本低（浅层模型）。
- **历史数据依赖**：训练数据来自 ODiNpred 的 CheZOD1325，经冗余去除后仅 1174 蛋白，规模有限；测试集仅 117 蛋白。
- **模型依赖**：性能高度依赖 ProtT5 的预训练质量；第 295 维的发现表明 pLM 内部表征可能高度偏向特定氨基酸属性。
- **最难情形**：短无序片段（<30 残基）预测精度显著下降；SETH 倾向于高估有序。
- **群体/领域边界**：训练数据以球状蛋白为主，对膜蛋白、重复蛋白等特殊类别的泛化能力未验证。
- **不确定性**：SETH 与 ANN/LinReg 的差异未达统计显著，说明 embedding 质量比模型架构更重要；但这一结论仅在当前数据规模下成立。

**有边界的复述**：SETH 在 CheZOD117 测试集上以 ρ≈0.75 超越 26 种既有方法，但这一优势在统计上仅对部分方法显著；其核心贡献在于证明了「单序列 pLM embedding + 浅层模型」足以达到 SOTA 水平，且速度快 170 倍，适合蛋白质组规模应用。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 短无序预测精度不足 | 短无序片段（<30 残基）ρ 仅 0.41±0.04 | 未明确提及 | Results 3.3；Fig. 4 |
| 训练/测试分布偏移 | 训练集 72% 有序 vs 测试集 31% 有序 | 未明确提及 | Methods 2.1；Results 3.2 |
| 冗余去除不彻底 | 仍有 3 个测试蛋白与训练蛋白在 10% 覆盖率下 PIDE>20% | 未明确提及 | Methods 2.1；Table S5 |
| 统计显著性有限 | SETH 与 ANN/LinReg 差异不显著 | 未明确提及 | Results 3.2 |
| 无法获取 SPOT-Disorder2 结果 | 服务器无响应，未能纳入对比 | 未明确提及 | Methods 2.5 |
| 模型未针对 pLM 微调 | pLM 为预训练模型，未针对无序任务优化 | 未明确提及 | 全文隐含 |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 训练集规模小（1174 蛋白） | 性能优势可能在小规模数据上过拟合；更大训练集上 MSA 方法可能反超 | 影响结论的泛化性 | 在更大训练集（如 DisProt 全量）上重训对比 | Methods 2.1 |
| 测试集仅 117 蛋白 | 统计功效有限，ρ 的置信区间可能较宽 | 影响 SOTA 对比的可靠性 | 使用更大独立测试集（如 CAID 基准） | Methods 2.5 |
| 第 295 维贡献 89% 性能 | 可能反映 ProtT5 中某一特定氨基酸属性（如疏水性）的编码，而非真正的「无序」概念 | 影响对 pLM 机制的理解 | 分析第 295 维与已知无序相关特征（如电荷、疏水性）的相关性 | Results 3.5 |
| SETH 与简单线性模型差异不显著 | 可能说明 CNN 的局部上下文建模对 CheZOD 预测增益有限 | 影响架构选择的合理性 | 在更长序列、更多数据上比较 CNN vs 线性模型 | Results 3.2 |
| AlphaFold2 对比中未控制同源效应 | 高 ρ 可能部分来自训练集与测试集的同源蛋白 | 影响 SETH vs AlphaFold2 结论的公平性 | 在严格非冗余测试集上重新对比 | Results 3.6 |
| 进化分析仅用 37 个物种 | 物种选择偏差可能影响 PCA 聚类结论 | 影响「无序谱系反映进化」的推广性 | 扩展到更多物种（如 GTDB 全基因组） | Results 3.7 |

## 14 Agent 提炼的知识候选

> 面向「无序蛋白/无序区(IDP/IDR)介导的蛋白互作（含相分离/凝聚体）× AI/深度学习 或 物理模拟」课题方向：

1. **pLM embedding 可作为 IDR 互作界面的高效特征**：SETH 证明 ProtT5 embedding 无需 MSA 即可捕获无序信息。在 IDR 介导的蛋白互作预测中，可直接用 ProtT5 embedding 作为残基级特征输入互作预测模型（如 PPI 预测、结合位点预测），避免 IDR 区域 MSA 质量差的瓶颈。

2. **连续尺度标签优于二元分类**：CheZOD 连续分数比二元无序/有序标签捕获更多细微差异，且与进化信号关联更强。在相分离相关预测中，可考虑用连续尺度（如凝聚体形成倾向分数、疏水/电荷模式强度）替代二元标签，以捕获 IDR 介导互作的梯度效应。

3. **「预训练 embedding + 浅层头」范式**：SETH 用两层 CNN 即达 SOTA，说明复杂模型并非必需。在 IDR 互作预测中，可先尝试「ProtT5/ESM-2 embedding + 浅层 MLP/CNN」的简单架构，再逐步增加复杂度，避免过度工程化。

4. **单维度可解释性分析**：第 295 维贡献 86%-96% 信号，提示 pLM embedding 中存在高度集中的生物学信号维度。在 IDR 互作分析中，可对 embedding 维度进行贡献度排序，识别关键维度并映射回生物学属性（如疏水性、电荷），增强模型可解释性。

5. **无序预测作为 AlphaFold2 预筛工具**：SETH 与 AlphaFold2 pLDDT 的相关性可用于优先选择需要昂贵 MD 模拟或实验验证的蛋白/区域——低 SETH 分数（预测有序）且低 pLDDT 的区域可能是错误折叠或互作诱导折叠区域，值得深入分析。

6. **无序谱系作为进化/功能标记**：CheZOD 分数分布的 PCA 可区分物种进化关系。在 IDR 介导互作研究中，可比较不同物种同源 IDR 的无序谱差异，识别功能关键的无序区域（保守无序 vs 物种特异无序）。

7. **冗余去除阈值对性能评估的影响**：作者使用 PIDE<20% 去冗余，但指出阈值选择会影响性能估计。在 IDR 互作数据集中，应明确冗余去除策略，避免同源蛋白导致的性能高估。

## 15 与已有知识连接

1. **Nielsen & Mulder (2016, 2019)**：CheZOD 分数的原始提出者，本文直接使用其数据集和基准。CheZOD 分数基于 NMR 化学位移，是少数提供连续无序测量的实验衍生标签。

2. **Elnaggar et al. (2021)**：ProtT5 蛋白质语言模型的原始论文。本文使用其 embedding 且未微调，证明预训练表征的迁移能力。

3. **Rives et al. (2021, ESM-1b)**：另一种 pLM，本文比较了 ESM-1b 与 ProtT5，后者略优。

4. **Jumper et al. (2021, AlphaFold2)**：本文系统比较了 AlphaFold2 衍生指标（pLDDT、experimentally resolved、RSA）与 SETH 在 CheZOD 预测上的表现，发现 AlphaFold2 指标不如专门的无序预测器。

5. **Dunker et al. (2013)**：IDP/IDR 领域的奠基性综述，本文引用其关于 IDR 功能重要性的论述。

6. **CAID (Necci et al., 2021)**：无序预测的社区基准评估，本文提到 SETH 在 CAID 第二轮中的初步表现。

7. **Marot-Lassauzaie et al. (2021)**：亚细胞定位谱系与进化的关联分析，本文借鉴其方法学思路用于无序谱系分析。

8. **[Analysis] 与相分离研究的潜在连接**：SETH 预测的连续无序分数可作为 LLPS 预测的输入特征。已知相分离驱动区域通常具有低复杂度序列、高电荷/疏水模式，CheZOD 分数可能捕获这些特征。但本文未直接验证 SETH 分数与相分离行为的相关性，需进一步实验验证。

## 16 Agent 生成的研究候选

1. **候选名称**：IDR-LLPS 互作界面预测器（IDR-LLPS-Interactor）
   - **来源局限/观察**：SETH 证明 pLM embedding 可高效预测无序程度，但未涉及 IDR 介导的互作或相分离。已知相分离由多价弱互作驱动，IDR 在其中起核心作用。
   - **核心假设**：ProtT5 embedding 中捕获的无序信息可迁移至 IDR 介导的互作/相分离预测，且连续无序分数比二元标签更有效。
   - **初步方法**：以 ProtT5 embedding 为输入，训练残基级互作位点预测器（如 attention-based 模型），输出互作概率和相分离倾向分数；在已知相分离蛋白数据集（如 PhaSepDB、LLPSDB）上验证。
   - **验证方式**：与现有 LLPS 预测器（如 catGRANULE、PLAAC）对比 AUC/ρ；在 CRISPR 突变体上验证预测的相分离关键残基。
   - **失败模式**：pLM embedding 可能主要捕获序列组成特征而非互作特异性，导致对相分离的预测退化为疏水性/电荷组成的代理指标。

2. **候选名称**：无序感知的 AlphaFold2 结构置信度校正（Disorder-Aware AF2 Confidence Calibration）
   - **来源局限/观察**：本文发现 AlphaFold2 pLDDT 与 CheZOD 分数相关性有限，且 SETH 可预测 AlphaFold2 高置信但实际无序的区域。
   - **核心假设**：将 SETH 无序分数与 AlphaFold2 pLDDT 联合，可更准确识别「假高置信」区域（即 AlphaFold2 预测有序但实验为无序的区域），从而改进结构模型的可靠性评估。
   - **初步方法**：在 AlphaFold2 数据库（AFDB）上运行 SETH，比较 pLDDT 与 SETH 分数不一致的区域；分析这些区域是否富集已知互作界面或相分离相关序列模式。
   - **验证方式**：在 PDB 中验证不一致区域是否有实验证据支持无序或互作诱导折叠；与 MD 模拟结果对比。
   - **失败模式**：不一致区域可能主要是 AlphaFold2 训练数据偏差所致，而非真实生物学信号。

3. **候选名称**：IDR 介导互作的进化保守性分析（Evolutionary Conservation of IDR-Mediated Interactions）
   - **来源局限/观察**：本文证明 CheZOD 分数分布可反映物种进化关系。IDR 介导的互作在进化中的保守性尚不清楚。
   - **核心假设**：功能重要的 IDR 互作区域在进化中保持无序程度相似（尽管序列可能快速演化），即「无序保守性」可作为互作功能重要性的标志。
   - **初步方法**：对同源蛋白家族计算 SETH 预测的 CheZOD 分数谱，比较直系同源物中无序模式的保守性；将保守无序区域与已知互作界面（如从 PPI 数据库）交叉验证。
   - **验证方式**：统计保守无序区域是否富集已知互作位点；在模式生物（酵母、线虫、人类）中比较互作网络的保守性。
   - **失败模式**：无序区域的序列快速演化可能导致 pLM embedding 无法捕获同源性，需要开发对齐无关的比较方法。

4. **候选名称**：pLM embedding 引导的 IDR 粗粒化 MD 模拟（PLM-Guided Coarse-Grained MD for IDRs）
   - **来源局限/观察**：SETH 证明 pLM embedding 包含残基级无序信息。IDR 的 MD 模拟面临力场参数化困难，尤其是无序区域。
   - **核心假设**：pLM embedding 可辅助生成 IDR 的粗粒化模型参数（如每个残基的疏水性、电荷、柔韧性），从而改进 MD 模拟的准确性。
   - **初步方法**：将 ProtT5 embedding 降维映射到粗粒化力场参数空间（如 MARTINI 的 bead 类型选择），对已知相分离蛋白进行 MD 模拟，比较相分离行为与实验数据。
   - **验证方式**：模拟预测的凝聚体形成浓度、液滴粘度等与实验对比；与标准 MARTINI 模拟对比精度。
   - **失败模式**：pLM embedding 与物理化学参数之间的映射可能不直接，需要大量训练数据且可能过拟合。

5. **候选名称**：无序介导互作的零样本预测（Zero-Shot Prediction of Disorder-Mediated Interactions）
   - **来源局限/观察**：SETH 的线性回归在未微调 pLM embedding 上即表现良好，提示 pLM 可能已隐式编码互作信息。
   - **核心假设**：ProtT5 embedding 的互作相关信号可通过零样本/少样本方式直接用于预测 IDR 介导的互作，无需大规模标注数据。
   - **初步方法**：对已知互作 IDR 对和非互作 IDR 对计算 embedding 相似性（如余弦相似度、注意力模式），训练简单分类器；在互作数据集（如 BioGRID、IntAct）上验证。
   - **验证方式**：与监督学习方法对比；在全新蛋白（无同源标注）上测试零样本泛化能力。
   - **失败模式**：pLM embedding 可能主要捕获序列相似性而非功能互作，导致预测退化为同源检测。