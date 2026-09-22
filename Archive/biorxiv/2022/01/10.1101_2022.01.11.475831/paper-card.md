## 01 基本信息

- **标题**：De novo protein structure prediction by incremental inter-residue geometries prediction and model quality assessment using deep learning
- **作者与单位**：Jun Liu; Guang-Xing He; Kai-Long Zhao; Gui-Jun Zhang（浙江工业大学，zhanglab-bioinf.com）
- **期刊/预印本平台**：bioRxiv
- **年份**：2022
- **论文类型**：预印本（方法学论文）
- **领域**：蛋白质结构预测、深度学习、模型质量评估
- **关键词**：de novo protein structure prediction, deep learning, model quality assessment, inter-residue geometries, closed-loop feedback
- **DOI/arXiv 号**：10.1101/2022.01.11.475831
- **代码**：未提供（仅提供 Web 服务器：http://zhanglab-bioinf.com/RocketX）
- **数据**：训练集（DeepAccNet 数据集 7800 蛋白 + SCOPe 2.07 筛选后 8608 序列）、测试集（483 benchmark 蛋白 + CASP14 20 个 FM 靶标 + CAMEO 盲测）
- **阅读日期**：2026-05-09
- **在该方向中的位置**：本文属于「几何约束辅助折叠 + 模型质量评估反馈」路线，核心创新在于将质量评估网络（EmaNet）的输出作为动态特征反馈给几何预测网络（GeomNet），形成闭环迭代优化。与 AlphaFold2 的端到端策略不同，本文保持了两阶段可解释架构，对理解折叠机制和中间状态建模有参考价值。与 IDP/IDR 课题的直接关联有限，但其「预测-评估-反馈」闭环思想可迁移至 IDR 构象系综的迭代优化。

## 02 一句话总结

本文提出 RocketX 方法，通过 GeomNet 预测残基间几何约束、结构模拟折叠、EmaNet 评估模型质量并将距离偏差和 per-residue lDDT 反馈给 GeomNet 作为动态特征，经三轮迭代闭环优化，在 483 个 benchmark 蛋白和 CASP14 FM 靶标上优于 trRosetta（无模板）和 RaptorX，并在 CAMEO 盲测中与使用模板的方法性能相当。

## 03 研究问题

- **具体问题**：如何将模型质量评估（Model Quality Assessment, MQA）引入 de novo 蛋白质结构预测流程，形成闭环反馈以迭代提升预测精度，而非仅作为最终评估步骤？
- **为什么重要**：传统几何约束辅助折叠方法（如 trRosetta）为单轮预测，预测误差无法在后续迭代中被修正；MQA 通常只用于最终模型选择，未参与结构生成过程。若能将 MQA 信息反馈至几何预测，可望在不依赖模板的情况下持续改进模型精度，并有助于揭示折叠机制。
- **现有方法不足**：端到端方法（如 AlphaFold2）虽精度高但可解释性差，难以研究折叠中间态；传统两阶段方法缺乏反馈机制，几何预测误差在折叠后无法被系统性纠正。
- **精确研究问题**：Can a closed-loop feedback mechanism, where model quality assessment estimates (inter-residue distance deviation and per-residue lDDT) are fed back as dynamic features to the geometric constraint prediction network, significantly improve de novo protein structure prediction accuracy across multiple iterations?

## 04 背景与发展脉络

以下脉络基于本文框架及引用文献，标注「仅本文框架」或「经外部核验」。

1. **传统 de novo 预测（无深度学习）**：依赖物理力场（如 Rosetta）和采样算法，精度有限（Rohl et al., 2004; Xu and Zhang, 2012）。[经外部核验]
2. **深度学习用于接触图预测**：Xu 组率先将 ResNet 用于残基间接触预测（Wang et al., 2017, 2018），开启深度学习辅助折叠时代。[经外部核验]
3. **几何约束扩展**：从接触扩展到距离和取向分布（trRosetta, Yang et al., 2020），提供更丰富的几何信息用于折叠。[经外部核验]
4. **端到端预测突破**：AlphaFold2（Jumper et al., 2021）和 RoseTTAFold 通过注意力机制和结构模块直接生成原子坐标，精度大幅提升，但可解释性不足。[经外部核验]
5. **模型质量评估发展**：从传统机器学习（ProQ3D, Ornate）到深度学习（DeepAccNet, DeepUMQA），MQA 精度持续提升，但通常仅用于最终模型选择。[经外部核验]
6. **本文位置**：首次将 MQA 输出（距离偏差 + per-residue lDDT）作为动态特征反馈至几何预测网络，形成「预测-折叠-评估-再预测」闭环，属于几何约束辅助折叠路线的迭代增强版本。[仅本文框架]

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 几何预测误差无法修正 | 单轮预测的几何约束误差直接传导至最终模型，无纠错机制 | 传统方法中几何预测与折叠为单向流程，无反馈回路 | Methods 2.2-2.3 描述单轮流程；Results 3.3 消融实验显示无反馈版本（RocketX¹）精度显著低于闭环版本 |
| MQA 未参与结构生成 | MQA 仅用于最终模型选择，未利用其误差信息改进预测 | 缺乏将 MQA 输出转化为可训练特征的机制 | Introduction 第 2 段：「Model quality assessment is usually used as the last step to evaluate the quality of the model. Introducing it into the structure prediction to improve the model is worthy of attention.」 |
| 端到端方法可解释性差 | AlphaFold2 等端到端方法难以研究折叠中间态和多构象 | 端到端训练将几何预测与结构生成耦合，中间表征不可解释 | Introduction 第 1 段：「The end-to-end prediction has made a breakthrough, but the interpretability remains to be further studied」 |
| 不同几何约束的潜在特征未充分利用 | 距离、二面角等不同几何量可能具有各自特有模式，统一处理可能损失信息 | 传统网络仅在主干共享特征，未针对不同几何量分支学习 | Results 3.4 对比 GeomNet*（无分支）与 GeomNet（有分支），后者精度显著更高 |

## 06 核心思想

### 1) 表面方法

RocketX 由三个模块组成迭代闭环：(a) GeomNet——基于 MSA 特征 + 动态反馈特征预测残基间距离和取向分布；(b) 结构模拟——将预测的几何约束转换为能量势（DFIRE 范式 + Rosetta 能量项），通过 MinMover 和 FastRelax 折叠出结构模型；(c) EmaNet——从折叠模型中提取 1D/2D 特征，估计残基间距离偏差和 per-residue lDDT，并将这些估计值作为动态特征反馈给 GeomNet。整个流程迭代三轮，每轮用上一轮的结构评估结果修正几何预测。

### 2) 核心洞察

**「评估即修正」**：模型质量评估网络输出的误差信息（距离偏差、per-residue lDDT）本质上编码了当前模型与真实结构之间的系统性偏差模式。将这些偏差作为动态特征输入几何预测网络，相当于为网络提供了「当前预测哪里错了」的显式信号，使其在下一轮预测中针对性修正。这与人类专家查看模型后手动修正同源建模的思路一致，但被自动化并嵌入深度学习框架。

**「分支学习」**：不同几何约束（距离、ω、θ、φ）可能具有不同的特征模式，在主干网络后设置独立分支，让每个分支专门学习对应几何量的潜在特征，比共享输出层更有效。

### 3) 可能的普适教训 [Analysis]

- **闭环反馈是通用优化范式**：任何「预测-生成-评估」流程（包括 IDR 构象采样、蛋白-蛋白对接、相分离凝聚体预测）都可考虑将评估器的误差信号反馈至生成器，形成迭代优化。关键在于设计可微或可训练的反馈特征表示。
- **误差分解提供更丰富信号**：EmaNet 输出的是细粒度的距离偏差分布而非单一全局分数，这种「哪里错了」的空间信息比「整体多好」的标量分数更有指导价值。对 IDR 体系，可类比为输出每个残基的局部构象偏差而非整体 Rg 或 pLDDT。
- **可解释性与精度可兼得**：本文表明，保持两阶段可解释架构（几何预测→折叠）的同时，通过反馈机制也能逼近端到端方法的精度，这对需要中间态分析的研究（如 IDR 折叠路径）有方法论启示。

## 07 方法总览

- **输入**：查询蛋白序列 → MSA（HHblits 搜索 UniRef30 + BFD 数据库，逐步放宽 e-value 阈值 1e⁻³⁰ → 1e⁻¹⁰ → 1e⁻⁶ → 1e⁻³）
- **输出**：最终全原子结构模型（三轮迭代后）
- **模块**：
  1. **GeomNet**（几何约束预测）：输入 MSA 特征（逆协方差矩阵 441 维、PSSM 21 维、位置熵 1 维、one-hot 20 维，共 526 维/残基对）+ 动态反馈特征（距离偏差 15 维 + per-residue lDDT 1 维，共 543 维/残基对）。主干为 61 个残差块（空洞卷积，dilation 循环 1,2,4,8），后接 4 个独立分支（各 5 个残差块），分别预测距离分布（37 bins：2-20Å，0.5Å 步长 + 1 个无接触 bin）、ω（25 bins）、θ（25 bins）、φ（13 bins）。
  2. **结构模拟**：将预测的几何分布转换为平滑能量势（DFIRE 范式），结合 Rosetta 四个基础能量项，用 MinMover 搜索粗粒度结构，再 FastRelax 精修为全原子模型。
  3. **EmaNet**（质量评估）：输入从折叠模型提取的 1D 特征（73 维：per-residue USR、氨基酸性质、二级结构、键长键角、主链二面角、Rosetta 单体能项）和 2D 特征（33 维：残基间多距离、取向、氢键图、残基对欧拉角、序列距离）。主干为 20 个残差块，分支输出距离偏差（15 bins）和接触图（阈值 15Å）。
- **训练**：GeomNet 和 EmaNet 分别训练。GeomNet 用交叉熵损失，EmaNet 用交叉熵（距离偏差）+ MSE（per-residue lDDT）。AdamW 优化器（GeomNet，triangular 循环学习率 base_lr=1e⁻⁴, max_lr=5e⁻⁴），Adam（EmaNet，lr=5e⁻⁴，decay 0.98/epoch）。各 200 epochs，5 模型平均。
- **反馈流程**：第 1 轮仅用 MSA 特征预测几何→折叠→EmaNet 评估；第 2、3 轮将 EmaNet 输出的距离偏差和 per-residue lDDT 作为动态特征拼接到 GeomNet 输入，重新预测几何→折叠→再评估。共 3 轮迭代。
- **推理成本**：单轮约数分钟（GPU），三轮迭代总计约 10-15 分钟/蛋白（未提供精确计时）。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| **GeomNet 主干**（61 残差块） | 从 MSA 特征学习残基对几何约束的共享表征 | 捕获共进化信号与几何约束间的复杂映射 | 输入：L×L×526（第 1 轮）或 L×L×543（后续轮）；输出：共享特征张量 | Results 3.1 表 1：接触精度和距离 MAE 优于 trRosetta | [预期] 移除后无法预测几何约束，整个流程失效 |
| **GeomNet 分支**（4 独立分支） | 分别预测距离、ω、θ、φ 分布 | 不同几何量可能有各自特有模式，共享输出层可能互相干扰 | 输入：主干特征；输出：4 个概率分布张量 | Results 3.4 表 4：GeomNet（分支）优于 GeomNet*（无分支），所有指标显著提升 | [实测消融] GeomNet* 的 TM-score 显著低于 GeomNet，证明分支结构有效 |
| **结构模拟**（MinMover + FastRelax） | 将几何约束转化为 3D 坐标 | 几何分布需转换为可评估的原子模型 | 输入：几何分布；输出：全原子结构 | Results 3.2 表 2：整体 TM-score 优于 trRosetta 和 RaptorX | [预期] 移除后无结构可评估，反馈闭环断裂 |
| **EmaNet 特征提取**（1D+2D） | 从模型中提取多尺度几何和能量特征 | 需要丰富特征以准确估计模型误差 | 输入：折叠模型；输出：73 维 1D + 33 维 2D 特征 | Methods 2.4 特征列表（补充表 S1） | [预期] 特征不足会降低误差估计精度，削弱反馈效果 |
| **EmaNet 评估**（20 残差块 + 双分支） | 估计距离偏差和 per-residue lDDT | 提供细粒度误差信号作为反馈 | 输入：特征张量；输出：距离偏差分布 + per-residue lDDT | Results 3.3 表 3：反馈使 TM-score 从 0.758 提升至 0.774 | [实测消融] RocketX¹（无反馈）TM-score 0.758 vs RocketX（两轮反馈）0.774，差异显著 |
| **反馈拼接**（动态特征） | 将 EmaNet 输出拼接到 GeomNet 输入 | 为几何预测提供「当前误差在哪」的显式信号 | 输入：EmaNet 输出；输出：L×L×543 输入张量 | Results 3.3 图 4：TM-score≥0.95 的模型从 1 个增至 12 个 | [实测消融] 无反馈版本高精度模型数量大幅减少 |

## 09 关键公式符号

本文方法以网络架构和损失函数为主，无显式数学公式。以下为隐含的关键定义：

1. **per-residue lDDT 计算**（Methods 2.4）：
   \[
   p_{i,k} = \frac{1}{L} \sum_{j \neq i} \left[ c_{i,j} \cdot \mathbb{1}(d_{i,j} \leq k) \right]
   \]
   其中 \( p_{i,k} \) 为残基 i 在阈值 k 下的 lDDT 预测值；\( d_{i,j} \) 为残基 i 和 j 的预测距离偏差；\( c_{i,j} \) 为残基 i 和 j 接触（<15Å）的预测概率；\( L \) 为序列长度。最终 lDDT 为 k ∈ {0.5, 1, 2, 4}Å 的平均。

2. **总损失函数**（Methods 2.2, 2.4）：
   \[
   \mathcal{L}_{GeomNet} = \sum_{g \in \{dist, \omega, \theta, \phi\}} \text{CE}(p_g, \hat{p}_g)
   \]
   \[
   \mathcal{L}_{EmaNet} = \text{CE}(p_{dev}, \hat{p}_{dev}) + 0.25 \cdot \text{CE}(p_{contact}, \hat{p}_{contact}) + 10 \cdot \text{MSE}(p_{lDDT}, \hat{p}_{lDDT})
   \]
   其中 CE 为交叉熵，MSE 为均方误差；权重 0.25 和 10 为手动调节（Methods 2.4：「The weights are tuned to allows the deviation to dominate」）。

3. **能量势转换**（Methods 2.3）：预测的几何分布通过 DFIRE 范式转换为能量势：
   \[
   E(d) = -k_B T \ln \frac{P_{pred}(d)}{P_{ref}(d)}
   \]
   其中 \( P_{pred}(d) \) 为预测的距离分布，\( P_{ref}(d) \) 为参考态分布（DFIRE 背景分布）。

## 10 实验设计与证据链

### 数据集与评测协议

| 数据集 | 规模 | 用途 | 来源 |
|--------|------|------|------|
| DeepAccNet 数据集 | 7800 蛋白（95% 训练，5% 验证） | 训练 EmaNet | Methods 2.1 |
| SCOPe 2.07 筛选集 | 8608 训练 + 483 测试 | 训练 GeomNet + 整体 benchmark | Methods 2.1 |
| CASP14 FM 靶标 | 20 个 | 外部测试 | Results 3.5 |
| CAMEO 盲测 | 16 hard + 29 medium（2021-12-04 至 12-25） | 盲测 | Results 3.6 |

**指标**：接触精度（top-L 长/中长程）、距离 MAE/RMSE、Cβ-lDDT、TM-score、RMSD。

**基线**：trRosetta（无模板模式）、RaptorX。

**消融版本**：RocketX¹（无反馈，仅 MSA 特征）、RocketX²（一轮反馈）、RocketX（两轮反馈）。

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 几何约束精度对比 | RocketX 的几何预测优于 trRosetta | 483 benchmark 蛋白，同 MSA 输入 | 接触精度：RocketX 0.764（中长程）/0.667（长程）vs trRosetta 0.744/0.641；MAE 1.08Å vs 1.14Å；Cβ-lDDT 0.677 vs 0.623 | RocketX 的 GeomNet 架构（分支设计）优于 trRosetta 的共享输出 | 未与 AlphaFold2 等端到端方法对比几何预测精度 | Results 3.1 表 1 |
| 整体结构精度对比 | RocketX 优于 trRosetta 和 RaptorX | 483 benchmark 蛋白 | 平均 TM-score：RocketX 0.774 vs trRosetta 0.751 vs RaptorX 0.714；平均 RMSD：4.92 vs 5.17 vs 5.88 | RocketX 整体预测精度显著优于两个基线 | 未与 AlphaFold2 直接对比 | Results 3.2 表 2 |
| 反馈消融实验 | 反馈机制显著提升精度 | RocketX¹（无反馈）vs RocketX²（1 轮）vs RocketX（2 轮） | TM-score：0.758 → 0.766 → 0.774；TM-score≥0.9 数量：55 → 73 → 81；TM-score≥0.95 数量：1 → 5 → 12 | 每轮反馈均带来显著提升，且高精度模型数量增长尤为明显 | 未测试 3 轮以上迭代是否继续提升 | Results 3.3 表 3、图 4 |
| 网络架构对比 | 分支设计优于无分支 | GeomNet*（无分支）vs GeomNet（有分支） | GeomNet 在所有几何指标上优于 GeomNet*，显著性检验 p<0.05 | 分支结构能更好学习不同几何量的特有特征 | 未测试其他分支设计变体 | Results 3.4 表 4 |
| CASP14 FM 靶标 | RocketX 在盲测靶标上具有竞争力 | 20 个 FM 靶标 vs 4 个 CASP14 服务器组 | 平均 TM-score：RocketX 0.474 vs RaptorX 0.415 vs BAKER-ROSETTASERVER 0.410 vs MULTICOM-CLUSTER 0.460 vs Yang_FM 0.470 | RocketX 优于 RaptorX 和 BAKER，与 MULTICOM 和 Yang_FM 相当 | 样本量小（20 靶标），未做显著性检验 | Results 3.5 图 5 |
| CAMEO 盲测 | 无模板预测在盲测中表现 | 16 hard + 29 medium，11 个服务器 | Hard：TM-score 0.45，lDDT 43.58，排名 4/11；Medium：TM-score 0.73，排名 3/11 | 无模板方法可与使用模板的方法竞争 | 仅 1 个月数据，时间窗口有限 | Results 3.6 图 6 |

## 11 结论正确解读

- **任务范围**：本文仅针对单域球状蛋白的 de novo 结构预测，测试集蛋白长度 50-500 残基，不涉及多域蛋白、膜蛋白、蛋白复合物或 IDP/IDR。
- **Oracle/真值输入**：MSA 搜索依赖 UniRef30 和 BFD 数据库，对孤儿序列或浅 MSA 的蛋白性能可能显著下降。EmaNet 训练依赖 DeepAccNet 数据集的 decoy 结构，decoy 质量分布影响评估精度。
- **端到端状态**：RocketX 为「几何预测→折叠→评估→再预测」的迭代流程，非端到端可微训练。GeomNet 和 EmaNet 分别训练，反馈特征为离散拼接而非梯度回传。
- **算力成本**：GeomNet 训练约 10 天/GPU（TITAN RTX），EmaNet 约 8 天/GPU。推理需三轮迭代，每轮含结构折叠和评估，总耗时显著高于单轮方法。
- **历史数据依赖**：训练数据截至 2018 年（DeepAccNet 数据集），测试集为 2020-2021 年（CASP14、CAMEO），存在时间跨度。MSA 数据库版本影响共进化特征质量。
- **模型依赖**：结构折叠依赖 PyRosetta 的 MinMover 和 FastRelax，折叠成功率受几何约束质量影响。EmaNet 的 lDDT 估计依赖阈值参数（0.5-4Å）。
- **最难情形**：从 CASP14 FM 结果看，RocketX 在部分靶标上 TM-score 低于 0.4，表明对新型折叠或浅 MSA 靶标仍有困难。CAMEO hard 靶标平均 TM-score 仅 0.45，远低于 benchmark 测试集。
- **有边界的复述**：RocketX 在 483 个 benchmark 蛋白和 CASP14 FM 靶标上，通过三轮「预测-评估-反馈」闭环迭代，显著优于无反馈版本和 trRosetta、RaptorX 基线，并在 CAMEO 盲测中达到与使用模板方法相当的水平。该结论仅适用于长度 50-500 残基、MSA 质量良好的球状蛋白。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 未与 AlphaFold2 直接对比 | 仅在 benchmark 和 CASP14 上与 trRosetta、RaptorX 比较，未提及 AlphaFold2 结果 | 未明确说明 | Results 3.2（未提及 AlphaFold2） |
| 迭代轮数有限 | 仅测试三轮迭代，未探索更多轮次的效果 | 未明确说明 | Methods 2「The final model is generated after three iterations」 |
| 计算成本较高 | 三轮迭代含多次折叠和评估，推理时间较长 | 未明确说明 | Methods 2.3-2.4（未提供时间数据） |
| 依赖 MSA 质量 | 共进化特征依赖 MSA 深度，对浅 MSA 蛋白可能失效 | 未明确说明 | Methods 2.2（未讨论 MSA 深度影响） |
| 可解释性仍有限 | 虽为两阶段架构，但反馈机制的具体修正逻辑未深入分析 | 作者在 Conclusion 提到未来将研究折叠路径和多状态 | Conclusion 第 2 段 |

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 未与 AlphaFold2 直接对比 | 仅在 benchmark 和 CASP14 上与 trRosetta、RaptorX 比较，未提及 AlphaFold2 结果 | 未明确说明 | Results 3.2（未提及 AlphaFold2） |
| 迭代轮数有限 | 仅测试三轮迭代，未探索更多轮次的效果 | 未明确说明 | Methods 2「The final model is generated after three iterations」 |
| 计算成本较高 | 三轮迭代含多次折叠和评估，推理时间较长 | 未明确说明 | Methods 2.3-2.4（未提供时间数据） |
| 依赖 MSA 质量 | 共进化特征依赖 MSA 深度，对浅 MSA 蛋白可能失效 | 未明确说明 | Methods 2.2（未讨论 MSA 深度影响） |
| 可解释性仍有限 | 虽为两阶段架构，但反馈机制的具体修正逻辑未深入分析 | 作者在 Conclusion 提到未来将研究折叠路径和多状态 | Conclusion 第 2 段 |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 反馈提升幅度有限 | TM-score 从 0.758 提升至 0.774（+2.1%），虽显著但幅度不大；高精度模型（≥0.95）从 1 增至 12 是主要亮点 | 需判断闭环反馈是否值得额外计算成本 | 在更大测试集上报告每轮迭代的增量收益和耗时 | Results 3.3 表 3 |
| 与 trRosetta 的对比公平性存疑 | trRosetta 使用官方服务器预测，而 RocketX 使用相同 MSA 但可能不同的搜索参数；RaptorX 为旧版服务器 | 对比公平性影响结论可信度 | 统一 MSA 生成流程，使用相同搜索参数重跑基线 | Methods 2.1-2.2 |
| EmaNet 反馈特征的信息量未量化 | 距离偏差（15 bins）和 per-residue lDDT（1 维）是否是最优反馈表示？其他误差特征（如局部二面角误差）可能更有效 | 反馈特征设计是闭环机制的核心，需系统比较 | 消融不同反馈特征组合，测量对最终 TM-score 的影响 | Methods 2.4（未提供特征消融实验） |
| 分支网络增益的机制解释不足 | 作者推测「不同几何约束有各自特征」，但未提供证据（如特征可视化或梯度分析） | 理解分支为何有效有助于推广到其他预测任务 | 对分支中间特征做可视化或探针分析 | Results 3.4（仅提供性能对比） |
| CAMEO 对比窗口过短 | 仅 1 个月（4 周）数据，hard 靶标仅 16 个，统计功效有限 | 盲测结论需更长时间窗口验证 | 延长 CAMEO 参与时间，积累更多靶标 | Results 3.6 |
| 未报告失败案例 | 未分析 RocketX 在哪些靶标上表现差（如 TM-score<0.5），以及失败模式 | 失败分析有助于理解方法边界 | 对低分靶标做分类分析（长度、二级结构组成、MSA 深度） | Results 3.5-3.6（未提供失败案例） |

## 14 Agent 提炼的知识候选

**标题：Agent 提炼的知识候选**

1. **「预测-评估-反馈」闭环范式**：将质量评估器的误差信号（而非仅分数）反馈至生成器，是提升迭代预测精度的通用策略。对 IDP/IDR 研究，可类比设计「构象采样→系综评估→误差反馈→再采样」闭环，其中评估器输出每个残基的局部构象偏差（类似 per-residue lDDT）而非单一全局分数。

2. **误差的空间分解优于标量分数**：EmaNet 输出距离偏差分布（15 bins）而非单一 lDDT 分数，提供了「哪里错了、错多少」的空间信息。对 IDR 相分离预测，可输出每个残基/区域的局部聚集倾向偏差，指导下一轮模拟或预测。

3. **分支网络设计**：在共享主干后设置独立分支预测不同几何量，优于共享输出层。对 IDR 多属性预测（如同时预测柔性、疏水性、电荷分布），可借鉴此设计。

4. **迭代轮数的边际收益递减**：三轮迭代中每轮均有提升，但增量递减（TM-score：+0.008 → +0.008）。对计算密集型 IDR 模拟，需权衡迭代轮数与计算成本。

5. **无模板预测的竞争力**：RocketX 在 CAMEO 上不使用模板即可与使用模板的方法竞争，提示对缺乏模板的 IDR 体系，纯共进化 + 深度学习策略仍有潜力。

6. **可解释架构的保留价值**：两阶段架构（几何预测→折叠）虽精度略低于端到端方法，但保留了中间产物（几何约束、结构模型），便于分析折叠路径和中间态——这对研究 IDR 的构象转变和凝聚体形成机制尤为重要。

## 15 与已有知识连接

- **trRosetta（Yang et al., 2020）**：本文的几何约束定义（距离、ω、θ、φ）和能量势转换直接继承自 trRosetta，可视为 trRosetta 的迭代增强版本。对 IDR 研究，trRosetta 的几何约束框架已被用于预测 IDR 的瞬态结构。
- **AlphaFold2（Jumper et al., 2021）**：本文明确将自身定位为与端到端方法互补的「可解释」路线。AlphaFold2 的 pLDDT 与本文的 per-residue lDDT 功能类似，但 AlphaFold2 未将其反馈至输入。对 IDR 研究，AlphaFold2 的 pLDDT 已被广泛用于预测 IDR 区域，但本文的反馈思想可改进 IDR 构象的迭代优化。
- **DeepAccNet（Hiranuma et al., 2021）**：本文 EmaNet 的训练数据直接采用 DeepAccNet 数据集，且 EmaNet 的架构和特征设计（1D/2D 混合）与 DeepAccNet 有相似之处。
- **DeepUMQA（Guo et al., 2021）**：本文作者团队前期工作，提出 per-residue USR 特征用于模型质量评估，该特征被直接用于 EmaNet 的 1D 输入。
- **CASP14/CAMEO 评测体系**：本文使用 CASP14 FM 靶标和 CAMEO 盲测作为外部验证，与领域内主流评测标准一致。
- **[Analysis] 与 IDP/IDR 课题的潜在连接**：本文的闭环反馈思想可迁移至 IDR 构象系综的迭代优化——用评估器（如预测 IDR 区域局部构象偏差的模型）的输出反馈至采样器（如 MD 或生成模型），逐步改进 IDR 的构象系综。此外，per-residue lDDT 的空间分解思想可类比为 IDR 中每个残基的局部有序度预测。

## 16 Agent 生成的研究候选

**标题：Agent 生成的研究候选**

1. **候选名称**：IDR-ConformerRefine——基于闭环反馈的 IDR 构象系综迭代优化
   - **来源局限/观察**：本文的「预测-评估-反馈」闭环显著提升球状蛋白预测精度，但 IDR 的构象系综优化缺乏类似机制；现有 IDR 采样方法（MD、蒙特卡洛）无系统性误差反馈。
   - **核心假设**：将 IDR 构象评估器（预测每个残基局部构象偏差）的输出反馈至采样器，可迭代改善 IDR 系综与实验数据（SAXS、NMR 化学位移）的吻合度。
   - **初步方法**：训练一个 IDR 专用评估网络（类似 EmaNet，但输出残基级 Rg 偏差或二级结构倾向偏差），将其输出作为偏置势加入 MD 模拟或作为生成模型的条件输入，迭代 3-5 轮。
   - **验证方式**：在已知 IDR 体系（如 α-synuclein）上比较迭代前后系综与实验数据的 χ² 吻合度。
   - **创新状态**：unverified

2. **候选名称**：IDR-GeomNet——面向 IDR 的几何约束预测网络
   - **来源局限/观察**：本文 GeomNet 的共进化特征对 IDR 可能失效（IDR 缺乏稳定共进化信号），但 IDR 的瞬态结构仍有几何偏好（如 polyproline II 螺旋）。
   - **核心假设**：结合序列理化性质（电荷分布、疏水性、柔性）和语言模型嵌入，可预测 IDR 残基间的瞬态几何偏好。
   - **初步方法**：将 GeomNet 的输入从共进化特征扩展为 ESM-2 嵌入 + 理化性质，训练数据使用 IDR 的 MD 模拟系综而非静态结构。
   - **验证方式**：在 IDR 测试集上比较预测几何分布与 MD 模拟的吻合度。
   - **创新状态**：unverified

3. **候选名称**：PhaseSep-Feedback——相分离驱动蛋白的凝聚体形成倾向迭代预测
   - **来源局限/观察**：本文的闭环反馈思想可推广至相分离预测——现有相分离预测器（如 catGRANULUS、PhaSepPred）为单轮预测，未利用预测误差修正。
   - **核心假设**：将相分离预测器的误差（如漏检的驱动残基）反馈至特征提取，可提升 IDR 相分离驱动区域的识别精度。
   - **初步方法**：在相分离蛋白数据集上训练评估器，输出每个残基的「驱动贡献偏差」，反馈至预测器重新训练或迭代推理。
   - **验证方式**：在已知相分离蛋白（如 FUS、TDP-43）上比较迭代前后的 AUC。
   - **创新状态**：unverified

4. **候选名称**：IDR-MQA——面向 IDR 构象系综的质量评估指标
   - **来源局限/观察**：本文 EmaNet 的 per-residue lDDT 针对球状蛋白设计，IDR 的构象评估缺乏类似的空间分解指标。
   - **核心假设**：将 lDDT 推广为「局部系综吻合度」（local ensemble agreement score），可量化 IDR 每个残基的构象系综与参考系综的偏差。
   - **初步方法**：定义残基级系综距离分布偏差指标，训练评估网络预测该指标，用于 IDR 构象系综的筛选和反馈。
   - **验证方式**：在 IDR 基准集上比较该指标与现有指标（如 Rg、SASA）对系综质量的判别力。
   - **创新状态**：unverified