## 01 基本信息

- **标题**: ProteinJEPA: Latent prediction complements protein language models
- **作者**: Dan Ofer; Dafna Shahaf; Michal Linial
- **单位**: 未提供（根据作者信息推测为以色列高校，具体未提供）
- **期刊/平台**: arXiv 预印本
- **年份**: 2026
- **论文类型**: 预印本（方法学研究）
- **领域**: 蛋白质语言模型、自监督学习、表征学习
- **关键词**: JEPA, masked language modeling, protein language models, latent prediction, self-supervised learning
- **DOI/ID**: 2605.07554v1
- **代码**: https://anonymous.4open.science/r/protJepa-FF24（匿名评审用）
- **数据**: UniRef50（训练），TAPE、ProteinBERT splits、SCOPe-40 等公开基准（评测）
- **阅读日期**: 2026-05-08
- **在该课题方向中的位置**: 本文不直接研究 IDP/IDR 或相分离，但提出了一种新的预训练目标（masked-position MLM+JEPA），可迁移至 IDP/IDR 互作预测任务（如 disorder、PPI 等已在评测集中）。其核心贡献在于：在固定算力预算下，通过"仅在掩码位置做潜在空间预测 + 保留 MLM"的混合目标，提升蛋白质表征在下游任务（含 disorder、PPI、稳定性等与 IDP 相关任务）上的表现。对 IDP/IDR 课题的可迁移点在于：该方法无需额外数据或结构信息，可直接用于增强 IDP 相关预测模型的预训练表征。

---

## 02 一句话总结

本文提出 masked-position MLM+JEPA——在蛋白质语言模型的 MLM 目标基础上，仅在掩码位置附加一个对 detached 潜在目标的余弦预测损失（配 SIGReg 正则、无 EMA teacher），在相同 wall-clock 预算下，相比纯 MLM 在 16 项下游任务（含 disorder、PPI、稳定性等）中获得更多任务胜出（预训练 ESM2-35M 上 10W/3L/3T，ESM2-150M 上 11W/2L/3T），而全位置变体仅达 parity、纯 JEPA 则崩溃。

---

## 03 研究问题

- **具体问题**: 在蛋白质序列编码器中，潜在空间预测（JEPA 风格）能否在匹配的 wall-clock 预算下补充甚至超越 token 级 MLM 目标？
- **为什么重要**: 蛋白质语言模型几乎全部依赖 MLM 或 next-token 目标；JEPA 在视觉/视频领域已展示出优于重建式目标的表征质量，但蛋白质领域缺乏受控对比研究。若潜在预测有效，可提升下游任务（含 IDP 相关任务如 disorder、PPI、稳定性）的表征质量，且无需额外标注或结构信息。
- **现有方法不足**: ① 直接照搬视觉 JEPA（全位置潜在预测）在蛋白质上不 work（本文第 4.3 节显示全位置变体仅达 parity）；② 纯 JEPA（去掉 MLM）在几乎所有实验中都崩溃（第 4.3 节）；③ 已有蛋白质 JEPA 工作（如 JEPA-DNA 用于 DNA）未在蛋白质上做受控的 wall-clock 匹配对比。
- **精确研究问题 (Can...?)**: Can latent-space prediction at masked positions, when combined with MLM cross-entropy, outperform MLM-only under matched wall-clock budgets for protein sequence encoders at 35–150M scale?

---

## 04 背景与发展脉络

> 注：以下脉络基于本文框架，标注为「仅本文框架」；外部文献引用以方括号标注。

1. **蛋白质语言模型的自监督目标（仅本文框架）**:
   - 第一代：单序列 MLM（ESM-1b [31]、ProtBERT [9]）→ 依赖 MSA 或单序列
   - 第二代：规模扩展 + 数据扩展（ESM2 [12]、ProtT5 [9]）→ MLM 仍是默认目标
   - 第三代：结构/功能多模态（ESM-3 [12]、SaProt [36]）→ 仍以 token 级目标为主
   - 局限：MLM 只重建 token 身份，不显式学习全局几何/结构组织

2. **JEPA 家族（仅本文框架）**:
   - I-JEPA [1]：图像中预测潜在表征，取代重建式目标
   - V-JEPA [3]：视频中预测潜在表征
   - LLM-JEPA [14]：自然语言中的潜在预测
   - JEPA-DNA [18]：DNA 序列的潜在预测
   - 共同点：预测潜在空间而非输入空间，通常需要防坍缩机制（EMA teacher 或正则化）
   - 局限：在蛋白质上缺乏受控对比；直接迁移（全位置预测）效果不佳

3. **本文主张的位置（仅本文框架）**:
   - 不是"JEPA 替代 MLM"，而是"JEPA 补充 MLM"
   - 关键设计：潜在预测仅限掩码位置，而非全位置
   - 关键约束：匹配 wall-clock 而非匹配步数（更贴近实际使用场景）

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 纯 JEPA 崩溃 | 去掉 MLM 后，所有 backbone 上表征质量大幅下降（如 ESM2-35M 上 family-mean Δ = −0.250 vs. off-the-shelf） | 作者解释：JEPA 单独无法保持 token 级身份信息，导致线性探针在需要细粒度残基身份的任务上失败 | Results 4.3 节，Table 3 |
| 全位置潜在预测无效 | 全位置 MLM+JEPA 仅达 parity（|ΔΔ| ≤ 0.12 在所有 15 个 cell 内），不优于纯 MLM | 作者解释：全位置预测引入过多与 token 身份无关的噪声信号，稀释了 MLM 的强身份监督 | Results 4.3 节，Table 3 |
| 算力预算约束 | JEPA 分支每步成本约 1.8× MLM，匹配 wall-clock 时 MLM 完成更多步数（160K vs 88K steps @ 8h） | 作者解释：实际使用者按 wall-clock 分配算力，而非按步数；这使对比对 MLM+JEPA 更严苛 | Methods 3.5 节，Discussion 5 节 |
| 任务选择性 | 荧光（TAPE）和肽-HLA 结合上 MLM+JEPA 持续输给 MLM（0W/5L/0T 和 2W/3L/0T） | 作者解释：这些任务可能更依赖局部残基身份而非全局几何组织 | Results 4.2 节，Table 2 |
| 从零训练不稳定 | 随机初始化 ESM2-35M 上 masked-position MLM+JEPA 仅 6W/8L/2T（p=0.79），不如预训练 backbone 稳定 | 作者解释：架构敏感，transformer 无强归纳偏置时潜在预测收益不稳定 | Results 4.1 节，Table 1 |

---

## 06 核心思想

### 1) 表面方法

在标准 MLM 目标上叠加一个潜在空间预测损失，但**仅在掩码位置**计算该损失。具体地：
- 输入序列按标准 MLM 协议掩码 20% 位置
- 编码器对掩码序列编码，得到每个位置的隐藏状态
- MLM 头在掩码位置预测 token 身份（交叉熵）
- 同时，一个 predictor（两层 SwiGLU，expansion ratio 8/3）在掩码位置预测"干净输入"（未掩码序列）经同一编码器得到的 detached 隐藏状态
- 损失 = ℒ_MLM + λ·ℒ_JEPA^masked + α·SIGReg，其中 λ=0.45，α=1.0
- 无 EMA teacher；目标来自同一 backbone 对未掩码输入的编码，stop-gradient

### 2) 核心洞察

- **掩码位置是"信息瓶颈"**：MLM 已经在这些位置强制模型做细粒度身份预测；在此处附加潜在预测，等于要求模型同时保持"身份可恢复"和"表征可预测"两个约束，从而在不牺牲身份信息的前提下增强表征的几何组织性。
- **全位置预测是"信息冗余"**：非掩码位置的表征已经由输入直接决定，预测它们不增加有效监督信号，反而引入噪声。
- **MLM 是防坍缩的关键**：JEPA 单独训练时，模型可以退化为"预测常数表征"来最小化损失；MLM 的交叉熵强制每个位置的表征必须携带可解码的身份信息，从而天然防止坍缩。
- **detached target + SIGReg 替代 EMA teacher**：简化训练流程，降低内存开销，且效果不劣于 EMA 变体。

### 3) 可能的普适教训 [Analysis]

- **"混合目标"优于"替代目标"**：在蛋白质这类 token 身份高度重要的领域，完全抛弃 token 级监督（纯 JEPA）是危险的；更好的策略是在保留原有强监督的同时，附加一个辅助的潜在空间目标。
- **"位置选择"是设计空间的关键维度**：同样是 JEPA 损失，全位置 vs. 掩码位置效果差异巨大。这提示在迁移到其他模态/任务时，应仔细考虑"在哪些位置施加潜在预测"。
- **wall-clock 匹配是更公平的对比基准**：步数匹配会掩盖 JEPA 的额外计算成本；wall-clock 匹配更贴近实际使用场景，也更能反映方法的真实价值。

---

## 07 方法总览

- **输入**: 蛋白质氨基酸序列（单字符 tokenizer），截断/填充至 512 token
- **输出**: 训练好的蛋白质序列编码器（可冻结后用于下游线性探针）
- **训练目标**: ℒ = ℒ_MLM + λ·ℒ_JEPA^masked + α·SIGReg
  - ℒ_MLM: 标准掩码 token 交叉熵（20% 掩码率，80/10/10 mask/random/keep）
  - ℒ_JEPA^masked: 掩码位置隐藏状态与 detached 目标（干净输入经同一 backbone 编码）之间的余弦相似度损失
  - SIGReg: Sketched Isotropic Gaussian Regularizer，256 个随机投影，将 predictor 输出正则化为标准高斯
- **Predictor**: 两层 SwiGLU，expansion ratio 8/3，无 bias，输入输出均做 layer norm
- **优化器**: AdamW（lr 3e-4 从零训练，3e-5 继续预训练），1000 warmup steps，weight decay 0.01
- **有效 batch size**: 128（ProteinBERT2 为 192，AMPLIFY 为 208）
- **硬件**: 单张 NVIDIA A100-80GB，BF16 混合精度，torch.compile
- **评测**: 16 项下游任务（15 项线性探针 + SCOPe-40 零样本检索），冻结表征，线性头或余弦相似度
- **流程**:
  1. 对每个 backbone（ESM2-35M、ESM2-150M、AMPLIFY-120M、随机初始化 ESM2-35M、ProteinBERT2-35M），分别训练四种目标：MLM-only、masked-position MLM+JEPA、全位置 MLM+JEPA、JEPA-only
  2. 在相同 wall-clock 预算（1h/4h/8h）下 checkpoint
  3. 冻结表征，训练线性探针（3 seeds）或计算 SCOPe-40 检索
  4. 以 family-specific baseline（off-the-shelf 或随机初始化）为参照，计算每任务 Δ

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| MLM 头（token 预测） | 在掩码位置预测氨基酸身份 | 保留 token 级身份信息，防止表征坍缩 | 输入：编码器隐藏状态；输出：20 类 token 分布 | 纯 JEPA 崩溃（Table 3）；MLM 保留时 masked-position 变体有效 | 移除后模型坍缩（实测，Table 3） |
| Predictor（两层 SwiGLU） | 从掩码位置隐藏状态预测 detached 目标 | 将潜在预测从编码器解耦，增加模型容量 | 输入：掩码位置隐藏状态（layer-norm 后）；输出：预测的潜在向量 | 消融未单独报告，但 predictor 结构来自 sweep（Appendix A.3） | 预期：移除后 JEPA 损失无法有效传播（[Analysis] 推测） |
| Detached target（干净输入编码） | 提供预测目标，stop-gradient | 防止梯度通过目标回传导致训练不稳定 | 输入：未掩码序列；输出：同一 backbone 的隐藏状态（detached） | 方法 3.2 节；sweep 中 detached 变体优于 EMA 变体（Appendix A.3） | 预期：改为非 detached 可能导致训练不稳定（[Analysis] 推测） |
| SIGReg（256 随机投影） | 正则化 predictor 输出为标准高斯 | 防止潜在表征坍缩到低维子空间 | 输入：predictor 输出；输出：正则化损失标量 | sweep 中 SIGReg 为最佳正则化方案（Appendix A.3） | 预期：移除后可能增加坍缩风险（[Analysis] 推测） |
| 掩码位置选择 | 仅对掩码位置计算 JEPA 损失 | 在信息瓶颈处施加潜在预测，避免冗余 | 输入：掩码 mask；输出：损失掩码 | 全位置变体仅达 parity（Table 3）；masked-position 变体胜出（Table 1） | 改为全位置后增益消失（实测，Table 3） |
| 余弦损失 | 度量预测与目标的方向一致性 | 对向量尺度不敏感，适合表征学习 | 输入：预测向量、目标向量；输出：标量损失 | 方法 3.2 节；sweep 中余弦优于 MSE（Appendix A.3） | 预期：改为 MSE 可能降低性能（[Analysis] 推测） |

---

## 09 关键公式符号

**总损失**（Methods 3.2 节，Eq. 1）:

\[
\mathcal{L} = \mathcal{L}_{\text{MLM}} + \lambda \cdot \mathcal{L}_{\text{JEPA}}^{\text{masked}} + \alpha \cdot \mathcal{L}_{\text{reg}}
\]

- \(\mathcal{L}_{\text{MLM}}\)：标准掩码 token 交叉熵，在 20% 掩码位置上计算
- \(\mathcal{L}_{\text{JEPA}}^{\text{masked}}\)：掩码位置上的潜在预测损失
- \(\mathcal{L}_{\text{reg}}\)：SIGReg 正则化项
- \(\lambda = 0.45\)：JEPA 损失权重（sweep 选定，Appendix A.3）
- \(\alpha = 1.0\)：SIGReg 权重

**JEPA 损失**（余弦相似度，掩码位置集合 \(\mathcal{M}\)）:

\[
\mathcal{L}_{\text{JEPA}}^{\text{masked}} = \frac{1}{|\mathcal{M}|} \sum_{i \in \mathcal{M}} \left( 1 - \frac{\langle \text{predictor}(h_i^{\text{masked}}), \text{sg}(h_i^{\text{clean}}) \rangle}{\|\text{predictor}(h_i^{\text{masked}})\| \cdot \|\text{sg}(h_i^{\text{clean}})\|} \right)
\]

- \(h_i^{\text{masked}}\)：掩码输入在位置 \(i\) 的编码器隐藏状态
- \(h_i^{\text{clean}}\)：干净输入在位置 \(i\) 的编码器隐藏状态
- \(\text{sg}(\cdot)\)：stop-gradient 操作
- \(\text{predictor}(\cdot)\)：两层 SwiGLU 网络

**SIGReg**（Sketched Isotropic Gaussian Regularizer）:

\[
\mathcal{L}_{\text{reg}} = \mathbb{E}_{z \sim \mathcal{N}(0, I)} \left[ \| \hat{\Sigma}^{-1/2} (P(z) - \mu) \|^2 \right]
\]

- \(P(\cdot)\)：256 个随机投影
- \(\mu, \hat{\Sigma}\)：predictor 输出的经验均值和协方差估计
- 作用：将 predictor 输出分布正则化为标准高斯

**评测指标**：
- 线性探针：各任务原生指标（F1-Macro、AUC、Spearman ρ）
- SCOPe-40：Recall@1（主报告）、Recall@10、Recall@30（Appendix A.2）
- 每任务 Δ = 目标模型得分 − family-specific baseline 得分

---

## 10 实验设计与证据链

### 数据集/群体

- **训练数据**: UniRef50（ESM2 原始训练集），序列截断/填充至 512 token
- **评测集**: 16 项下游任务，涵盖：
  - 功能：EC 分类、酶催化效率、β-内酰胺酶适应度
  - 结构：远程同源性、SCOPe-40 折叠检索（零样本）
  - 互作：蛋白质-蛋白质相互作用（PPI）、肽-HLA 结合、金属离子结合
  - 理化：稳定性、溶解性、荧光（TAPE）
  - 定位/信号：亚细胞定位、信号肽
  - 其他：变异效应、神经肽前体、无序（CheZoD disorder）
- **规模**: 5 个 backbone × 4 种目标 × 3 个时间点（1h/4h/8h），共 60 个训练 run；评测时每个 cell 3 个探针 seed（部分 cell 仅 1 个 seed）

### 指标

- 主指标：每任务 Δ（相对 family-specific baseline）
- 汇总指标：macro-mean Δ（16 任务平均）
- 统计检验：单侧二项符号检验（masked-position vs. MLM-only，α=0.05）；配对 Wilcoxon 符号秩检验（全位置 vs. MLM-only，Holm-Bonferroni 校正）

### 关键实验

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|------------------|------|
| 主对比：masked-position MLM+JEPA vs. MLM-only（预训练 ESM2-35M） | 潜在预测补充 MLM | 相同 backbone、相同 wall-clock（8h）、相同评测协议 | 10W/3L/3T，p=0.046（拒绝 H₀） | masked-position 变体在多数任务上优于纯 MLM | 未报告效应量大小；未做多 seed 预训练 | Results 4.1 节，Table 1 |
| 主对比：masked-position MLM+JEPA vs. MLM-only（预训练 ESM2-150M） | 结论可扩展至更大模型 | 同上 | 11W/2L/3T，p=0.011（拒绝 H₀） | 150M 上收益更明显 | 未报告 150M 的绝对得分 | Results 4.1 节，Table 1 |
| 从零训练：随机初始化 ESM2-35M | 潜在预测对随机初始化有效 | 相同架构、相同 wall-clock | 6W/8L/2T，p=0.79（不拒绝 H₀） | 从零训练时收益不稳定 | 不能排除架构依赖 | Results 4.1 节，Table 1 |
| 从零训练：ProteinBERT2-35M | 架构设计可改善从零训练 | 自定义架构（卷积 stem + 交替注意力） | 11W/4L/1T，p=0.059 | 强归纳偏置可提升从零训练效果 | p 值未达 0.05 阈值 | Results 4.1 节，Table 1 |
| 全位置 MLM+JEPA vs. MLM-only（15 个 cell） | 全位置预测是否有效 | 5 backbone × 3 时间点 | 11/15 cell 不拒绝 parity；Rand-Init-35M 显著更差（p_H=0.002 at 4h） | 全位置预测不优于 MLM-only | 不能排除特定架构/规模下有效 | Results 4.3 节，Table 3 |
| 纯 JEPA（无 MLM） | JEPA 单独是否可行 | 所有 backbone | 所有 backbone 上 family-mean Δ 为负（−0.250 至 −0.131） | 纯 JEPA 在蛋白质上不可行 | 未测试更大规模或更长训练 | Results 4.3 节，Table 3 |
| 任务子集分析 | 收益集中在哪些任务 | 按任务类型分组 | 收益集中在回归、适应度、结构检索；荧光和肽-HLA 持续输 | 潜在预测改善全局几何组织 | 未做任务间相关性分析 | Results 4.2 节，Table 2 |
| L2 归一化鲁棒性 | 结论是否依赖后处理 | 7 任务子集，有/无 L2 归一化 | 所有 group |Δ| ≤ 0.002，排序不变 | 结论对 L2 选择鲁棒 | Appendix A.8，Table 18-19 |
| KNN 探针 | 结论是否依赖线性探针 | 11 任务子集，k=20 KNN | KNN 整体低于线性探针（mean −0.123），但未反转主结论 | 主结论对探针类型鲁棒 | KNN 仅作次要验证 | Appendix A.9 |

### 消融与对照

- **位置消融**：全位置 vs. 掩码位置（Table 3）——掩码位置是关键设计
- **目标消融**：保留 vs. 去除 MLM（Table 3）——MLM 是防坍缩关键
- **优化器对照**：AdamW vs. SGDm（Table 1）——AdamW 更优
- **EMA 对照**：LeWM 风格 detached target vs. EMA teacher（Appendix A.3）——detached 更优且更省内存

---

## 11 核心结论

1. **掩码位置潜在预测 + MLM 是有效组合**：在预训练 ESM2-35M 和 ESM2-150M 上，masked-position MLM+JEPA 在 16 项任务中分别以 10W/3L/3T 和 11W/2L/3T 胜过纯 MLM（p<0.05）。
2. **全位置预测无效**：全位置 MLM+JEPA 仅达 parity，不优于纯 MLM。
3. **纯 JEPA 崩溃**：去掉 MLM 后，所有 backbone 上表征质量大幅下降，说明 token 级身份监督对蛋白质表征至关重要。
4. **收益集中在特定任务类型**：回归、适应度、结构检索（含 disorder、PPI、稳定性）受益最大；荧光和肽-HLA 结合持续受损。
5. **从零训练效果依赖架构**：ProteinBERT2（强归纳偏置）上从零训练有效（11W/4L/1T），随机初始化 ESM2 上不稳定（6W/8L/2T）。
6. **方法即插即用**：无需 EMA teacher、无需额外数据、无需结构信息，可直接叠加到现有 MLM 训练流程中。

---

## 12 局限与未解问题

### 作者明确承认的局限（Discussion 5 节）

1. **掩码位置 vs. 全位置的混淆**：主对比同时改变了位置集合（掩码 vs. 全）和损失形式（余弦 vs. MSE），无法单独归因于位置选择。
2. **未做全位置余弦消融**：未运行"全位置 + 余弦"的 cell，无法完全排除损失形式的影响。
3. **从零训练结论不稳定**：随机初始化 ESM2-35M 上结果混合，不能断言 masked-position MLM+JEPA 对任意架构从零训练都有效。
4. **未测试微调（fine-tuning）**：仅评测了冻结线性探针，未验证在微调场景下的表现。
5. **未测试更大规模**：最大模型 150M，未验证在 650M+ 或更大模型上的可扩展性。
6. **未测试多模态模型**：SaProt、ESM-3、PTM-Mamba 等结构/功能多模态模型未纳入对比。

### 未解问题（[Analysis] 补充）

- 掩码位置潜在预测为何在荧光和肽-HLA 上持续失败？是否与任务对局部残基身份的极端依赖有关？
- 收益是否随训练时间增加而累积，还是仅在短训练窗口内有效？
- 潜在预测的表征是否在结构层面（而非仅任务层面）有可验证的改进（如二级结构一致性、接触图质量）？

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 主对比存在混淆变量 | 掩码位置 vs. 全位置同时改变了位置集合和损失形式（余弦 vs. MSE），无法归因 | 若增益来自余弦损失而非位置选择，则"掩码位置"这一核心 claim 不成立 | 增加"全位置 + 余弦"和"掩码位置 + MSE"两个 cell | Methods 3.3 节明确承认此混淆 |
| 预训练 backbone 已高度优化 | ESM2 的 off-the-shelf 权重可能已接近该规模的上限，MLM+JEPA 的增益可能只是"欠训练"的补偿 | 若增益来自"更多训练"而非"更好目标"，则方法价值有限 | 对比相同步数下 MLM-only 的更长训练 | Results 4.1 节显示 1h/4h checkpoint 也有增益 |
| 任务选择偏差 | 16 项任务中多数为回归/适应度类，可能偏向 JEPA 的全局几何优势 | 若任务集偏向某一类，结论不可泛化 | 增加更多分类任务、token 级任务（如二级结构 per-residue） | Table 2 显示荧光和肽-HLA 持续失败 |
| 未报告效应量 | 仅报告胜/负/平计数和 p 值，未报告平均效应量（如平均 Δ 或 Cohen's d） | 无法判断增益的实际大小是否值得额外计算成本（1.8×/step） | 补充效应量分析和成本-收益分析 | Results 4.1 节仅报告计数 |
| 单 seed 预训练 | 除 3 个 masked-position 主 run 外，多数 cell 仅 1 个预训练 seed | 无法区分训练随机性与方法效应 | 对关键对比增加多 seed 预训练 | Appendix A.6 说明部分 cell 仅 1 seed |
| 未与更强基线对比 | 未对比其他自监督目标（如对比学习、next-token prediction、结构辅助目标） | 无法判断 masked-position MLM+JEPA 是否是最优补充目标 | 增加 SimCSE、InfoNCE、ESM-3 风格目标作为对照 | Related Work 未提及此类对比 |

---

## 14 术语表

| 术语 | 含义 | 在本文中指 |
|------|------|-----------|
| MLM (Masked Language Modeling) | 掩码语言建模，预测被掩码 token 的身份 | 标准蛋白质预训练目标，20% 掩码率 |
| JEPA (Joint Embedding Predictive Architecture) | 联合嵌入预测架构，预测潜在表征而非输入 token | 本文的核心研究对象，具体为"掩码位置潜在预测" |
| Masked-position MLM+JEPA | 仅在掩码位置附加潜在预测损失的混合目标 | 本文提出的主要方法 |
| All-position MLM+JEPA | 在所有位置附加潜在预测损失的变体 | 作为对照的变体，效果不如掩码位置版本 |
| JEPA-only | 仅使用潜在预测损失，无 MLM | 作为对照的变体，几乎全部崩溃 |
| SIGReg (Sketched Isotropic Gaussian Regularizer) | 一种正则化方法，将输出分布推向标准高斯 | 用于防止 predictor 输出坍缩 |
| Detached target | 停止梯度的目标向量 | 来自干净输入经同一 backbone 编码的隐藏状态，不参与梯度回传 |
| EMA teacher (Exponential Moving Average teacher) | 指数移动平均教师网络 | 经典 JEPA 中用于生成目标的机制，本文用 detached target 替代 |
| Predictor | 预测器网络 | 两层 SwiGLU，将掩码位置隐藏状态映射到潜在目标空间 |
| Wall-clock budget | 墙钟时间预算 | 本文对比的基准，匹配实际算力使用场景 |
| Linear probe | 线性探针 | 在冻结表征上训练线性分类器/回归器，评测表征质量 |
| SCOPe-40 | 结构分类数据库的 40% 相似性聚类版本 | 用于零样本折叠检索的基准 |
| CheZoD | 蛋白质无序区域数据集 | 评测任务之一，与 IDP 直接相关 |
| TAPE | Tasks Assessing Protein Embeddings | 蛋白质嵌入评测基准，包含荧光等任务 |

---

## 15 对 IDP/IDR × 蛋白互作 × AI 课题的启示

### 直接相关任务（本文已覆盖）

1. **无序预测（CheZoD disorder）**：本文评测集中包含 CheZoD 无序数据集，masked-position MLM+JEPA 在该任务上有增益。对 IDP 课题的直接意义：**潜在空间预测可能改善无序区域的表征质量**，因为无序区域往往缺乏稳定的局部结构，全局几何组织信号可能比局部残基身份更有信息量。

2. **蛋白质-蛋白质相互作用（PPI）**：本文评测集中包含 PPI 任务。IDP 介导的互作（如分子识别特征 MoRF、短线性基序 SLiM）往往依赖全局构象而非单一残基，潜在空间预测可能捕捉这类非局部信号。

### 可迁移的方法论

3. **"掩码位置 + 潜在预测"的混合目标**：对于 IDP/IDR 互作预测，可尝试在现有模型（如 ESM2、ProtTrans）上继续训练时附加 masked-position JEPA 损失，**无需额外标注或结构信息**，直接增强表征。特别适合 IDP 相关任务（无序预测、MoRF 预测、相分离驱动蛋白识别）。

4. **位置选择的设计原则**：本文的核心发现是"在信息瓶颈处施加潜在预测"有效。对 IDP 课题，可类比思考：**在哪些位置施加潜在预测最有信息量？** 例如，在预测相分离时，可能在已知的 IDR 区域或预测的无序区域施加潜在预测，而非全序列。

5. **wall-clock 匹配的对比框架**：IDP 相关模型评测常忽视算力成本。本文的对比框架（匹配 wall-clock 而非步数）值得借鉴，尤其当比较不同架构（如 transformer vs. Mamba）时。

### 对 IDP 互作机制的潜在理解

6. **全局几何 vs. 局部身份的权衡**：本文的结论（潜在预测改善全局几何组织、但可能损害局部身份任务）对 IDP 有直接启示：**IDP 介导的互作可能更依赖全局构象而非局部序列**。这提示在 IDP 互作预测中，应优先使用能捕捉全局几何的表征（如 JEPA 增强的），而非纯 token-level 表征。

7. **从零训练 vs. 继续训练的架构依赖**：本文发现从零训练效果依赖架构（ProteinBERT2 好、ESM2 差）。对 IDP 课题，若需从零训练专门针对 IDP 的模型，**架构选择（如卷积 stem、交替注意力）可能比目标函数更重要**。

### 具体可迁移的评测设计

8. **任务矩阵设计**：本文的 16 任务矩阵覆盖功能、结构、互作、定位、理化等多维度。IDP 课题可借鉴此设计，构建包含无序预测、MoRF 识别、相分离驱动蛋白分类、IDP 结合亲和力回归等多任务的评测矩阵，避免单一任务过拟合。

9. **零样本检索评测**：SCOPe-40 零样本折叠检索是本文的亮点之一。IDP 课题可类比设计**零样本 IDP 相关检索**（如给定一个已知的相分离驱动蛋白，检索其同源或功能相似的蛋白），检验表征是否捕捉了 IDP 相关的功能几何。

---

## 16 研究想法

### 候选 1: IDP-JEPA——面向无序蛋白互作的掩码位置潜在预测

- **来源局限/观察**: 本文发现 masked-position MLM+JEPA 在 disorder 和 PPI 任务上有增益，但未专门针对 IDP 优化；且未测试 per-residue 任务（IDP 互作常需残基级预测）。
- **核心假设**: 在 IDR 区域施加潜在预测损失，能比全序列均匀施加更有效地增强 IDP 互作相关表征。
- **初步方法**: 在 ESM2 继续训练时，用预测的 IDR 区域（如 IUPred 输出）作为掩码概率权重，IDR 区域更高概率被掩码并施加 JEPA 损失；评测 MoRF 预测、SLiM 识别、相分离驱动蛋白分类。
- **验证方式**: 与均匀掩码的 masked-position MLM+JEPA 对比，在 IDP 相关任务上比较 Δ。
- **创新状态**: unverified

### 候选 2: 相分离驱动蛋白的零样本检索

- **来源局限/观察**: 本文的 SCOPe-40 零样本检索展示了 JEPA 增强表征在结构检索上的优势；相分离驱动蛋白缺乏类似的结构基准。
- **核心假设**: JEPA 增强的表征能比纯 MLM 表征更好地在零样本设置下检索功能相似的相分离驱动蛋白（如已知的 FUS、TDP-43、HNRNPA1 等）。
- **初步方法**: 构建相分离蛋白基准集（如 PhaSepDB、LLPSDB），用本文的 masked-position MLM+JEPA 模型提取表征，计算余弦相似度检索，对比 MLM-only 表征。
- **验证方式**: Recall@k 对比；与序列同一性匹配的基线对比。
- **创新状态**: unverified

### 候选 3: 潜在预测损失作为 IDP 互作模型的辅助目标

- **来源局限/观察**: 本文的 JEPA 损失是自监督的，无需标注。IDP 互作预测常受限于少量标注数据（如有限的 MoRF 标注、相分离实验数据）。
- **核心假设**: 在 IDP 互作预测模型（如基于 ESM2 的微调模型）训练时，附加 masked-position JEPA 损失作为辅助目标，能利用无标注序列改善表征，提升标注数据有限时的泛化。
- **初步方法**: 在 MoRF 预测任务上，对比"仅微调"与"微调 + JEPA 辅助损失"的模型，在少量标注（如 10%/25%/50% 训练数据）下比较性能。
- **验证方式**: 学习曲线对比；低数据 regime 下的 F1/AUC 差异。
- **创新状态**: unverified

### 候选 4: 无序区域的"信息瓶颈"分析

- **来源局限/观察**: 本文的核心洞察是"掩码位置是信息瓶颈"。IDR 区域在序列上往往缺乏保守性，但功能重要。
- **核心假设**: IDR 区域的潜在预测难度（JEPA 损失值）可以作为无序程度或功能重要性的代理指标。
- **初步方法**: 用训练好的 masked-position MLM+JEPA 模型，计算每个位置的 JEPA 损失（预测与目标的余弦距离），分析其在已知 IDR、MoRF、SLiM 区域是否系统性偏高或偏低。
- **验证方式**: 与 IUPred、DISOPRED 等无序预测器的输出做相关性分析。
- **创新状态**: unverified

### 候选 5: 物理模拟与 JEPA 表征的交叉验证

- **来源局限/观察**: 本文仅用序列信息，未涉及结构或物理模拟。IDP 的构象 ensemble 是理解其互作的关键。
- **核心假设**: JEPA 增强的表征能预测 IDP 的构象 ensemble 特性（如回旋半径、链内接触概率），因为潜在预测迫使表征编码全局几何组织。
- **初步方法**: 对一组 IDP 序列，用本文模型提取表征，与分子动力学（MD）模拟或粗粒化模拟（如 CABS、AWSEM）得到的 ensemble 特性做回归预测。
- **验证方式**: 与 MLM-only 表征的预测精度对比；与序列组成特征（如电荷分布、疏水性）的基线对比。
- **创新状态**: unverified

### 候选 6: AlphaFold 结构特征与 JEPA 潜在预测的融合

- **来源局限/观察**: 本文未使用结构信息；AlphaFold 对 IDP 区域常给出低置信度预测，但 pLDDT 等置信度指标本身可能携带信息。
- **核心假设**: 将 AlphaFold 的 pLDDT 或预测对齐误差（PAE）作为辅助特征，与 JEPA 增强的序列表征融合，能改善 IDP 互作位点预测。
- **初步方法**: 在 MoRF 或 SLiM 预测任务上，对比"仅序列表征"与"序列表征 + AlphaFold 置信度特征"的模型，其中序列表征分别用 MLM-only 和 masked-position MLM+JEPA。
- **验证方式**: 消融实验；在 IDP 富集的测试集上比较 F1/AUC。
- **创新状态**: unverified