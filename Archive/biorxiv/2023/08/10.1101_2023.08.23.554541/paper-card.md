## 01 基本信息

- **标题**：PSPire: a machine learning predictor for high-performance screening of phase-separating proteins without intrinsically disordered regions
- **作者与单位**：Shuang Hou; Jiaojiao Hu; Zhaowei Yu; Cong Liu; Yong Zhang（同济大学，Zhanglab；中国科学院上海有机化学研究所等，具体单位未在摘要中提供）
- **期刊/预印本平台**：bioRxiv（预印本）
- **年份**：2023
- **论文类型**：方法学/工具开发论文（含实验验证）
- **领域**：蛋白质相分离（PS）预测；机器学习；结构生物学
- **关键词**：phase separation, intrinsically disordered regions, machine learning, XGBoost, AlphaFold, structural features
- **DOI/arXiv 号**：10.1101/2023.08.23.554541
- **代码**：https://github.com/TongjiZhanglab/PSPire
- **数据**：训练/测试数据来自 PhaSePred 数据集；额外 PSPs 来自 LLPSDB、PhaSePro、PhaSepDB、DrLLPS；Phos 位点来自 PhosphoSitePlus（均公开）
- **阅读日期**：2025-05-13（按当前日期）
- **在课题方向中的位置**：本文聚焦于**无 IDR 的相分离蛋白（noID-PSPs）**的预测，是 IDP/IDR × 相分离 × AI 预测方向的重要补充。它明确指出现有预测器（如 PSAP、PhaSePred）对 noID-PSPs 的预测能力不足，并首次系统性地引入**结构层面特征（SSUP、sticker）**来弥补序列特征的局限。对于本课题（IDP/IDR 介导的蛋白互作 × AI/物理模拟），本文提供了一个关键思路：**结构域介导的多价互作（而非仅 IDR）也可驱动相分离**，且可通过结构特征进行机器学习建模。

---

## 02 一句话总结

本文开发了机器学习预测器 PSPire，通过整合残基层面（IDR 相关）和结构层面（SSUP、sticker）特征，显著提升了对**不含 IDR 的相分离蛋白（noID-PSPs）**的预测性能（AUROC 0.84 vs 现有最佳 0.68），并通过细胞实验验证了 8 个候选蛋白中 6 个确实形成凝聚体。

---

## 03 研究问题

- **具体问题**：现有 PSP 预测器严重偏向含 IDR 的蛋白（ID-PSPs），对不含 IDR 但通过结构化结构域介导多价互作而发生相分离的蛋白（noID-PSPs）预测能力很差。如何构建一个能同时准确预测两类 PSPs 的模型？
- **为什么重要**：相分离不仅由 IDR 驱动，结构化结构域（如 SH2、coiled-coil 等）也能通过多价互作驱动 PS。忽略 noID-PSPs 会导致对相分离蛋白组的不完整认识，影响疾病机制研究和药物靶点发现。
- **现有方法不足**：现有预测器（PSAP、PhaSePred、FuzDrop 等）主要依赖序列特征（氨基酸组成、IDR 预测分数等），这些特征对 noID-PSPs 不敏感，甚至出现相反趋势（如 IDR 相关特征在 noID-PSPs 中低于非 PSPs）。
- **精确研究问题**：Can a machine learning model that integrates residue-level and structure-level features (derived from AlphaFold-predicted structures) significantly outperform existing sequence-based predictors in identifying phase-separating proteins without intrinsically disordered regions?

---

## 04 背景与发展脉络

> 注：以下脉络基于本文 Introduction 和 Results 的叙述，属于「仅本文框架」，未经外部系统核验。

1. **早期序列/组成特征预测器**（~2015-2018）：PLAAC、catGRANULE、PScore、PSPer 等。基于氨基酸组成、疏水性、电荷分布等简单序列特征。局限：训练数据小、特征单一、对 noID-PSPs 无区分能力。
2. **机器学习/深度学习预测器**（~2019-2022）：FuzDrop、PSAP、PSPredictor、PhaSePred 等。使用更大训练集和更复杂模型（随机森林、SVM、神经网络等）。进步：整体预测性能提升。局限：仍以序列特征为主，对 noID-PSPs 预测性能差（本文 Fig. 1a 显示最佳 AUROC 仅 0.68）。
3. **结构信息引入的契机**（~2021-2023）：AlphaFold 的出现使得全蛋白质组高质量结构预测成为可能。本文首次系统性地将**结构层面特征**（SSUP 残基组成、sticker 数量/配对）引入 PSP 预测，专门针对 noID-PSPs。
4. **本文位置**：在「序列特征 → 结构特征」的演进中，本文是首个明确以 noID-PSPs 为核心目标、并利用 AlphaFold 结构特征构建专用预测器的工作。它同时提供了可解释性分析（SHAP）和实验验证，是该方向的重要里程碑。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 现有预测器对 noID-PSPs 预测能力差 | 最佳 AUROC 仅 0.68，AUPRC 仅 0.08 | 现有特征（IDR 相关、序列组成）在 noID-PSPs 上呈现与 ID-PSPs 相反的趋势，无法有效区分 | Results 节 Fig. 1a, Supplementary Fig. 1a |
| 序列特征对 noID-PSPs 不敏感甚至误导 | 如 "IDR_50" 特征在 noID-PSPs 中低于非 PSPs，与 ID-PSPs 趋势相反 | noID-PSPs 缺乏 IDR，IDR 相关特征自然失效；部分序列特征（如疏水性）在两类 PSPs 中表现不同 | Results 节 Fig. 1b, Supplementary Fig. 1b |
| 缺乏结构层面特征 | 现有预测器完全忽略蛋白三维结构信息 | 此前缺乏高质量结构数据；AlphaFold 的出现才使全蛋白质组结构特征计算成为可能 | Introduction 节 |
| noID-PSPs 的识别标准不明确 | 现有数据库和训练集以 IDR 含量高的 PSPs 为主 | 相分离研究早期聚焦于 IDR 驱动的 PS，结构化结构域驱动的 PS 被忽视 | Introduction 节, Methods 节 Datasets |

---

## 06 核心思想

### 1) 表面方法
构建 XGBoost 分类器 PSPire，输入特征包括：
- **IDR 相关特征**：在 IDR 区域上计算的氨基酸组成、疏水性等（来自 PSAP/PhaSePred 的重要特征）
- **SSUP 相关特征**：在结构表面暴露区域（SSUP）上计算的相同特征
- **Sticker 相关特征**：基于 SSUP 上带电残基聚类识别的 sticker 数量、sticker 配对数量等
- **Phos 频率特征**：磷酸化位点频率（来自 PhosphoSitePlus）

### 2) 核心洞察
**结构化结构域的表面残基（SSUP）是 noID-PSPs 相分离的关键驱动因素**。作者发现，将原本在 full-length 蛋白上计算的序列特征改为在 SSUP 上计算后，这些特征对 noID-PSPs 的区分能力显著提升。特别是带电残基形成的 "sticker" 簇（类似 IDR 中的 sticker-and-spacer 模型）在 SSUP 上同样存在，且能有效预测 noID-PSPs。这提示：**多价互作不仅可由 IDR 中的短线性基序介导，也可由结构化结构域表面的带电 patch 介导**。

### 3) 可能的普适教训 [Analysis]
- **特征计算区域比特征本身更重要**：同样的氨基酸组成特征，在 full-length 上计算 vs. 在 SSUP 上计算，预测能力截然不同。这提示在蛋白功能预测中，**功能相关区域（而非全蛋白）的特征计算**可能更有效。
- **AlphaFold 结构不仅是预测工具，更是特征提取器**：本文展示了 AlphaFold 结构可用于提取超越序列的特征（如 SSUP、sticker），这为其他蛋白功能预测任务提供了可迁移的范式。
- **针对亚群优化而非追求通用模型**：作者没有试图构建一个对所有 PSPs 都最优的模型，而是专门针对 noID-PSPs 优化特征和模型，取得了显著提升。这种「分而治之」的策略值得借鉴。

---

## 07 方法总览

- **输入**：蛋白质氨基酸序列 + AlphaFold 预测的 3D 结构（PDB 格式）
- **输出**：PS 概率分数（0-1），用于判断蛋白是否为 PSP
- **特征计算流程**：
  1. 从 AlphaFold PDB 文件中提取序列、pLDDT 分数、原子坐标
  2. 使用 DSSP 计算每个残基的二级结构状态
  3. 基于 pLDDT < 50 和二级结构状态定义 IDR 和 SSUP 区域
  4. 在 IDR 和 SSUP 上分别计算 PSAP/PhaSePred 的特征（氨基酸组成、疏水性等）
  5. 在 SSUP 上识别带电 sticker 簇，计算 sticker 数量和配对数量
  6. 计算 Phos 频率特征
- **模型**：XGBoost 分类器，默认参数，样本加权（按 ID-PSPs/noID-PSPs/non-PSPs 频率倒数）
- **训练策略**：10 轮训练，每轮从负样本中随机采样（负样本数为正样本 2 倍），最终分数为 10 个模型平均
- **评测**：独立测试集（258 PSPs, 1961 non-PSPs），AUROC 和 AUPRC 指标
- **实验验证**：HeLa 细胞免疫荧光 + 体外纯化蛋白 + PEG 诱导相分离 + DIC 成像

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| IDR 区域定义 | 基于 pLDDT < 50 和二级结构过滤，识别长无序区域 | 区分 ID-PSPs 和 noID-PSPs，为 IDR 特征计算提供区域 | 输入：AlphaFold PDB；输出：IDR 残基集合 | Methods 节 IDRs calculation | 预期影响：ID-PSPs 预测性能下降（IDR 特征无法计算） |
| SSUP 区域定义 | 基于 RSA > 25% 和排除 IDR，识别结构表面暴露区域 | 捕获结构化结构域表面的互作残基 | 输入：AlphaFold PDB + IDR 集合；输出：SSUP 残基集合 | Results 节 Fig. 2a-b | 预期影响：noID-PSPs 预测性能显著下降（核心创新模块） |
| Sticker 识别 | 在 SSUP 上聚类带电残基，识别正/负 sticker 簇 | 量化结构化表面的多价互作能力 | 输入：SSUP 残基坐标；输出：sticker 数量、配对数量 | Results 节 Fig. 2c-e, Supplementary Fig. 2 | 预期影响：noID-PSPs 预测性能下降（sticker 是 noID-PSPs 的关键特征） |
| XGBoost 分类器 | 整合所有特征进行二分类 | 核心预测模型 | 输入：特征向量；输出：PS 概率 | Results 节 Fig. 4 | 预期影响：模型无法工作（核心模块） |
| Phos 频率特征 | 计算磷酸化位点频率 | 磷酸化已知可调控相分离 | 输入：PhosphoSitePlus 数据；输出：频率值 | Results 节 Supplementary Fig. 3 | 预期影响：整体性能轻微下降（SHAP 显示其为重要特征） |

---

## 09 关键公式符号

本文未提供显式数学公式。核心计算步骤包括：

1. **RSA（相对溶剂可及表面积）**：
   - RSA = SASA / SASA_standard（每个残基类型有标准值）
   - 阈值：RSA > 25% 判定为暴露残基

2. **净电荷指数（net charge index）**：
   - 对 SSUP 中每个残基 i，计算距离 d 内（d 从 10 Å 到 20 Å 测试，选 14 Å）正电荷残基数减去负电荷残基数
   - |净电荷指数| > 3 的残基被选为 sticker 候选

3. **Sticker 聚类**：
   - 基于 Cα 3D 坐标，使用层次聚类（hierarchical clustering）
   - 参数：t=15, criterion=distance, metric=Euclidean, method=centroid
   - 聚类结果按电荷分类为正/负 sticker

4. **Sticker 频率** = sticker 总数 / SSUP 残基数
5. **Sticker 配对频率** = min(正 sticker 数, 负 sticker 数) / SSUP 残基数

---

## 10 实验设计与证据链

### 数据集与评测设置
- **训练集**：259 PSPs（195 ID-PSPs + 64 noID-PSPs），8,323 non-PSPs
- **测试集**：258 PSPs（194 ID-PSPs + 64 noID-PSPs），1,961 non-PSPs
- **外部评测集**：4 个人类 MLO 数据集（G3BP1 proximity labelling, RNAgranuleDB Tier1, PhaSepDB MLO, DrLLPS MLO）
- **指标**：AUROC, AUPRC
- **基线**：PSAP, PhaSePred, PSPredictor, FuzDrop, PSPer, PScore, catGRANULE, PLAAC
- **实验验证**：HeLa 细胞免疫荧光（内源蛋白）、体外纯化蛋白 + PEG 诱导 + DIC 成像

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 现有预测器在 noID-PSPs 上的表现 | 现有预测器对 noID-PSPs 预测能力差 | 8 个预测器在测试集上分别评估 ID-PSPs 和 noID-PSPs | 最佳 AUROC = 0.68（noID-PSPs），最佳 AUROC = 0.84（ID-PSPs） | 现有预测器确实对 noID-PSPs 预测能力差 | 未比较所有预测器在相同训练集上的重训效果 | Results 节 Fig. 1a |
| 特征在 full-length vs. SSUP 上的对比 | SSUP 特征对 noID-PSPs 更有效 | 同一特征在 full-length 和 SSUP 上分别计算，比较分布差异 | SSUP 特征能同时区分 ID-PSPs 和 noID-PSPs 与 non-PSPs | SSUP 是 noID-PSPs 的关键特征区域 | 未做统计检验量化的效应量 | Results 节 Fig. 2b |
| Sticker 特征分析 | noID-PSPs 的 SSUP 上存在更多 sticker | 比较 ID-PSPs、noID-PSPs、non-PSPs 的 sticker 频率和配对频率 | noID-PSPs 的 sticker 频率和配对频率显著高于 non-PSPs | 结构化表面的多价电荷互作是 noID-PSPs 相分离的驱动因素 | 未直接证明 sticker 互作导致相分离（仅相关性） | Results 节 Fig. 2e, Supplementary Fig. 2 |
| PSPire 整体性能 | PSPire 优于现有预测器 | 在测试集上对比 PSPire 与 8 个现有预测器 | PSPire noID-PSPs AUROC = 0.84, AUPRC = 0.19；ID-PSPs AUROC = 0.85, AUPRC = 0.47 | PSPire 显著提升 noID-PSPs 预测性能，同时保持 ID-PSPs 性能 | 未在独立外部数据集上与其他预测器对比 | Results 节 Fig. 4a-b |
| MLO 数据集评测 | PSPire 在 MLO 蛋白上表现良好 | 4 个人类 MLO 数据集 | PSPire 在 noID-PSPs 预测上显著优于现有预测器 | PSPire 的预测具有生物学相关性 | MLO 数据集可能包含非 PSP 蛋白，标签噪声 | Results 节 Fig. 4c |
| 细胞实验验证 | PSPire 预测的候选蛋白确实形成凝聚体 | 8 个候选蛋白（3 个高置信 noID-PSPs + 3 个中置信 noID-PSPs + 2 个 ID-PSPs）在 HeLa 细胞中免疫荧光 | 6/8 形成凝聚体（PGM1, TXNL4B, SerpinB4, VPS26B, S100A7, Rab31） | PSPire 预测具有实验可验证性 | 未做定量凝聚体形成效率比较；未验证凝聚体是否为液相 | Results 节 Fig. 5a-b |
| 体外相分离验证 | 候选蛋白可在体外发生相分离 | 纯化蛋白 + PEG 诱导 + DIC 成像 | PGM1, SerpinB4, S100A7, Rab31 形成液滴 | 候选蛋白具有内在相分离能力 | 仅验证 4 个蛋白；未做突变对照 | Results 节 Fig. 5c |

---

## 11 结论正确解读

- **任务范围**：本文解决的是**蛋白质序列 + 结构 → 相分离倾向**的二分类预测问题，特别针对 noID-PSPs。它不预测相分离的机制、条件或凝聚体性质。
- **Oracle/真值输入**：训练标签来自 PhaSePred 数据集（文献验证的 PSPs）和额外数据库（LLPSDB、PhaSePro 等），这些标签本身可能存在偏差（如实验条件不同、假阴性）。
- **端到端状态**：PSPire 是端到端可用的预测工具，输入蛋白序列即可输出 PS 分数（自动调用 AlphaFold 结构）。但**不是**端到端的相分离机制模型。
- **算力成本**：主要成本在 AlphaFold 结构预测（对每个蛋白需数分钟至数小时 GPU 时间）；XGBoost 训练本身轻量。
- **历史数据依赖**：训练数据来自已发表的 PSP 数据库，存在发表偏倚（已研究的 PSPs 更可能被收录）。
- **模型依赖**：依赖 AlphaFold 预测结构的准确性；对 AlphaFold 预测质量差的蛋白（如某些膜蛋白、多结构域蛋白），SSUP 特征可能不可靠。
- **最难情形**：无 IDR 且结构域表面缺乏明显带电 patch 的蛋白；结构域间互作依赖非电荷相互作用（如疏水、芳香族）的蛋白。
- **群体/领域边界**：训练和测试主要基于人类蛋白；跨物种泛化能力未验证。MLO 数据集评测仅针对人类。
- **有边界的复述**：PSPire 在人类蛋白质组范围内，通过整合 AlphaFold 结构衍生的 SSUP 和 sticker 特征，能够以 AUROC 0.84 的准确度识别不含 IDR 的相分离蛋白，显著优于现有序列-based 预测器（AUROC 0.68），且该预测能力在 4 个 MLO 数据集和 8 个候选蛋白的湿实验验证中得到支持。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| AlphaFold 预测结构与天然结构可能存在差异 | 影响 SSUP 和 sticker 计算的准确性 | 期待更精确的结构预测工具出现 | Discussion 节 |
| ID-PSPs 与 noID-PSPs 的二分法过于简化 | 某些蛋白可能同时具有 IDR 和结构域介导的相分离机制 | 未来可考虑更细粒度的分类 | Discussion 节 |
| 训练数据依赖已发表的 PSP 数据库 | 存在发表偏倚，可能遗漏未研究的 PSPs | 随着 PSP 数据库扩充，模型可进一步改进 | Discussion 节 |
| 物种泛化性未验证 | 模型主要针对人类蛋白训练 | 未明确提及 | Discussion 节（隐含） |
| 对 noID-PSPs 的预测仍非完美 | AUPRC 仅 0.19，精度有限 | 未来可引入更多结构特征或实验数据 | Results 节 Fig. 4b |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| noID-PSPs 的标签定义依赖 IDR 预测工具 | 不同 IDR 预测工具（IUPred、ESpritz 等）结果差异大，可能影响 noID-PSPs 的划分 | 标签噪声直接影响模型评估的可靠性 | 使用多种 IDR 预测工具重复划分，检验模型性能稳定性 | Methods 节 IDRs calculation |
| SSUP 定义依赖 RSA 阈值（25%） | 该阈值是否最优未做敏感性分析 | 不同阈值可能改变特征分布和模型性能 | 对 RSA 阈值做网格搜索，报告性能变化 | Methods 节 SSUP determination |
| Sticker 识别距离阈值（14 Å）的选择依据 | 作者测试了 10-20 Å 但未展示完整结果 | 阈值选择可能过拟合训练集 | 在独立测试集上验证不同距离阈值的泛化性能 | Methods 节 Sticker-related features |
| 与现有预测器的对比可能不公平 | 现有预测器未在相同训练集上重训，可能低估其性能 | 公平对比是方法学贡献的关键 | 在相同训练/测试集上重训所有基线模型 | Results 节 Fig. 4a-b |
| 湿实验验证样本量小（8 个蛋白） | 6/8 的验证成功率可能受选择偏倚影响 | 小样本验证不足以确立普适性 | 扩大验证集，特别是阴性对照 | Results 节 Fig. 5 |
| 未与 AlphaFold 结构质量关联分析 | 低质量预测结构的蛋白可能影响 SSUP 特征可靠性 | 结构质量可能是模型误差的重要来源 | 按 pLDDT 分数分层分析模型性能 | [Analysis] 基于 Methods 推断 |
| 未讨论非人类蛋白的适用性 | 模型特征（如磷酸化频率）可能具有物种特异性 | 跨物种应用是实际需求 | 在模式生物（小鼠、酵母）蛋白上评测 | [Analysis] 基于 Discussion 推断 |

---

## 13 批判性分析（续）

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 特征计算依赖 AlphaFold 结构，但未与实验结构对比 | AlphaFold 预测的 SSUP 可能与晶体结构/冷冻电镜结构中的实际表面暴露区域不同 | 结构预测误差可能系统性影响特征质量 | 对具有实验结构的蛋白，比较 AlphaFold 与实验结构计算的 SSUP 特征差异 | Methods 节 SSUP determination |
| 模型输出为二分类概率，未提供相分离机制解释 | 即使预测准确，也无法区分 IDR 驱动 vs 结构域驱动的相分离 | 机制理解是课题方向的核心需求 | 分析 SHAP 值在不同蛋白类别上的差异模式 | Results 节 Supplementary Fig. 3 |
| 训练集正负样本比例严重不平衡（259:8323） | 虽然使用样本加权，但极端不平衡可能影响模型校准 | 概率分数可能无法直接解释为相分离倾向 | 检查模型校准曲线，考虑使用平衡采样或集成方法 | Methods 节 Model training |

---

## 14 学到什么

> **Agent 提炼的知识候选**

1. **结构域表面特征可预测相分离**：本文证明，结构化结构域的表面暴露残基（SSUP）上的氨基酸组成和电荷分布，能有效预测 noID-PSPs。这提示在 IDP/IDR 研究中，**不应忽视结构化结构域对相分离的贡献**。可迁移到本课题：在分析 IDR 介导的互作时，同时考虑互作伙伴的结构域表面特征。

2. **特征计算区域的选择是关键创新点**：同样的特征，在 full-length 上计算 vs. 在功能相关区域（如 SSUP）上计算，预测能力差异巨大。可迁移到本课题：在预测 IDR 介导的互作时，**在 IDR 内识别功能相关子区域**（如 MoRF、SLiM）可能比全 IDR 特征更有效。

3. **Sticker-and-spacer 模型可推广到结构化结构域**：本文将原本用于 IDR 的 sticker 概念扩展到 SSUP 上的带电残基簇，并验证了其预测能力。可迁移到本课题：**将 IDR 中的 sticker 概念与结构化结构域中的相互作用热点统一**，建立更全面的多价互作模型。

4. **AlphaFold 结构作为特征提取器的范式**：本文展示了 AlphaFold 结构不仅可用于折叠预测，还可作为下游预测任务的特征来源。可迁移到本课题：**利用 AlphaFold 结构提取 IDR 的构象系综特征**（如 pLDDT 分布、接触图）来预测互作模式。

5. **分而治之的建模策略**：针对 noID-PSPs 这一被忽视的子类专门优化模型，比追求通用模型更有效。可迁移到本课题：**针对特定类型的 IDR 介导互作**（如 RGG 基序介导、酸性 IDR 介导）分别建模，可能优于通用预测器。

6. **湿实验验证的闭环设计**：从预测到细胞验证（免疫荧光）再到体外验证（纯化蛋白 + PEG + DIC），形成了完整的验证链条。可迁移到本课题：**AI 预测结果应配套标准化的湿实验验证流程**，包括细胞定位、凝聚体形成、突变扰动等。

---

## 15 与已有知识连接

1. **Brangwynne et al. (2009)**：首次发现 P granules 的液滴性质，奠定相分离研究基础。本文延续了这一框架，但将研究对象扩展到无 IDR 的蛋白。

2. **Sticker-and-spacer 模型（Choi, Hyman & Pappu, 2020 等）**：本文将该模型从 IDR 扩展到 SSUP，是概念上的重要延伸。

3. **PSAP (Chen et al., 2022)** 和 **PhaSePred (Chen et al., 2023)**：本文直接对比的 SOTA 预测器。PSAP 基于序列特征 + 随机森林，PhaSePred 整合多特征 + 机器学习。本文的贡献在于引入结构特征并专门优化 noID-PSPs。

4. **AlphaFold (Jumper et al., 2021)** 和 **AlphaFold DB (Varadi et al., 2022)**：本文依赖 AlphaFold 预测结构作为特征来源，是 AlphaFold 在蛋白功能预测中的典型应用。

5. **DeepPhase (Yu et al., 2023)**：基于免疫荧光图像的 PSP 预测器。本文将其作为外部验证资源，说明两种方法互补。

6. **LLPSDB (Li et al., 2020)**、**PhaSepDB (You et al., 2020)**、**DrLLPS (Ning et al., 2020)**：本文使用的 PSP 数据库来源，是相分离领域的重要数据资源。

7. **MoRF/SLiM 预测**：本文的 SSUP 特征与 IDR 中的 MoRF（分子识别特征）预测有概念上的相似性，可考虑将两者结合。

8. **分子动力学模拟**：本文的 sticker 识别方法（基于距离的电荷聚类）与 MD 模拟中识别互作热点的方法类似，可迁移到 MD 模拟的初始构象选择。

---

## 16 研究想法

> **Agent 生成的研究候选**

### 候选 1：IDR-SSUP 协同互作预测模型
- **来源局限/观察**：PSPire 将 IDR 和 SSUP 特征分开计算，但未建模两者的协同效应。许多蛋白同时具有 IDR 和结构化结构域，两者可能协同驱动相分离。
- **核心假设**：IDR 中的 sticker 与 SSUP 上的 sticker 之间的**跨区域互作**是相分离的重要驱动因素，且这种协同效应可被机器学习捕获。
- **初步方法**：构建图神经网络（GNN），将蛋白表示为 IDR-SSUP 双区域图，节点为残基/区域，边为空间邻近或序列邻近关系，预测相分离倾向。
- **验证方式**：在 PSPire 数据集上对比 GNN 与 PSPire 的性能；对预测为 PSP 的蛋白进行突变分析（破坏 IDR-SSUP 互作）。
- **创新状态**：unverified

### 候选 2：基于 AlphaFold 构象系综的 IDR 互作预测
- **来源局限/观察**：PSPire 使用 AlphaFold 的单一预测结构，但 IDR 本质上是构象异质的，单一结构无法捕捉其互作模式。
- **核心假设**：IDR 的构象系综特征（而非单一结构）能更好地预测其介导的互作和相分离行为。
- **初步方法**：使用 AlphaFold 的 pLDDT 和 PAE 信息生成 IDR 的构象系综（如通过 AF-Cluster 或 MD 模拟），提取系综特征（如 Rg 分布、接触概率），训练预测器。
- **验证方式**：在已知 IDR 介导互作的蛋白集上评测；与 PSPire 和 MD 模拟结果对比。
- **创新状态**：unverified

### 候选 3：物理模拟与机器学习融合的 sticker 预测
- **来源局限/观察**：PSPire 的 sticker 识别基于简单的距离阈值和电荷数，未考虑残基互作的热力学性质。
- **核心假设**：结合 MD 模拟或粗粒化模拟计算的残基互作自由能，能更准确地识别功能性 sticker。
- **初步方法**：对候选 PSPs 进行粗粒化 MD 模拟（如 MARTINI），计算残基互作能量矩阵，识别高能量互作热点作为 sticker；将这些物理特征输入 PSPire 框架。
- **验证方式**：对比物理特征 vs. 几何特征的 sticker 预测准确性；在已知相分离蛋白上验证。
- **创新状态**：unverified

### 候选 4：跨物种相分离蛋白预测与进化分析
- **来源局限/观察**：PSPire 主要针对人类蛋白，跨物种泛化性未验证。
- **核心假设**：相分离相关的结构特征（SSUP、sticker）在进化上保守，可用于跨物种预测。
- **初步方法**：收集多物种 PSP 数据集，训练跨物种模型；分析 SSUP/sticker 特征的进化保守性。
- **验证方式**：在非人类物种（酵母、果蝇、小鼠）的已知 PSPs 上评测；与人类模型对比。
- **创新状态**：unverified

### 候选 5：IDR 介导互作的残基级解释工具
- **来源局限/观察**：PSPire 提供蛋白级预测，但无法定位到具体残基/区域，限制了机制研究和实验验证。
- **核心假设**：通过可解释 AI（如 SHAP 值在残基级别的分解），可以识别驱动相分离预测的关键残基，这些残基可能是真实的互作位点。
- **初步方法**：在 PSPire 框架上增加残基级特征归因模块，输出每个残基对预测的贡献分数；与已知互作位点数据库（如 BioGRID、IntAct）对比验证。
- **验证方式**：在已知互作位点的蛋白上评测残基级归因的准确性；设计突变实验验证预测的关键残基。
- **创新状态**：unverified

### 候选 6：IDR 磷酸化调控相分离的预测模型
- **来源局限/观察**：PSPire 将 Phos 频率作为单一特征，但未建模磷酸化位点的位置效应和动态调控。
- **核心假设**：IDR 中特定位置的磷酸化事件可增强或抑制相分离，且这种效应可通过序列-结构上下文预测。
- **初步方法**：收集已知磷酸化调控相分离的蛋白数据，构建序列-结构上下文特征（如磷酸化位点附近的电荷变化、二级结构偏好），训练预测器。
- **验证方式**：在已知磷酸化调控相分离的蛋白上评测；与 PSPire 对比。
- **创新状态**：unverified