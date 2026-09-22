## 01 基本信息

- **标题**: Protein folding stability estimation with explicit consideration of unfolded states
- **作者**: Lee, Heechan; Cho, Yugyeong; Yun, Jeongwon; Steinegger, Martin; Kim, Ho Min; Park, Hahnbeom
- **单位**: 未提供（推测为韩国机构，基于致谢中的韩国研究基金会资助信息）
- **期刊/平台**: Nature Communications
- **年份**: 2026-01-22
- **论文类型**: 研究论文（含方法开发与实验验证）
- **领域**: 蛋白质折叠稳定性预测；深度学习；蛋白质设计
- **关键词**: ΔG预测、未折叠态、系综建模、深度学习、蛋白质工程、de novo设计
- **DOI/arXiv**: 10.1038/s41467-026-68637-4
- **代码**: github.com/HParklab/IFUM（含Colab）
- **数据**: 未提供独立数据仓库，训练数据基于Mega-scale、DisProt、CATH等公开数据库
- **阅读日期**: 2026-05-13
- **在该课题方向中的位置**: 本文虽不直接研究IDP/IDR介导的蛋白互作或相分离，但其核心创新——显式建模未折叠态（含无序蛋白）来提升ΔG预测——为IDP/IDR体系的热力学建模提供了直接可借鉴的框架。IFUM将无序蛋白（DisProt）纳入训练，并显式建模未折叠态系综，对IDP/IDR相关研究具有重要参考价值。

## 02 一句话总结

本文提出IFUM，一种联合学习ΔG与折叠/未折叠态平衡系综（以残基对距离分布表示）的深度神经网络，通过显式建模未折叠态（基于Flory无规线团模型）显著提升ΔG预测精度，并在蛋白质工程和de novo设计筛选中优于AlphaFold-based指标。

## 03 研究问题

- **具体问题**: 如何准确预测蛋白质的绝对折叠自由能（ΔG），特别是考虑未折叠态对ΔG的贡献？
- **为什么重要**: ΔG是蛋白质功能、稳定性和疾病关联的核心热力学量；现有计算方法（包括基于结构预测AI的方法）在定量复现实验ΔG值方面存在明显局限。
- **现有方法不足**: (1) AlphaFold/ESMFold的plDDT/pTM等置信度指标并非为ΔG设计，只能定性过滤；(2) ΔΔG预测方法（如ThermoFold）局限于单点突变，无法处理插入/缺失（indels）；(3) 多数深度学习方法将未折叠态视为与序列无关的"零状态"，忽略了未折叠态的序列依赖性。
- **精确研究问题**: Can a deep neural network that explicitly models the unfolded state ensemble (via Flory random coil model) achieve accurate absolute ΔG prediction across diverse protein types, including disordered proteins and complex mutations?

## 04 背景与发展脉络

*注：此脉络基于本文框架，未经外部系统核验。*

1. **实验ΔG测量时代**: 传统生物物理方法（如变性剂滴定）可测量ΔG，但耗时费力、数据异质。
2. **基于物理势能的方法**: FoldX、Rosetta等使用经验能量函数计算ΔG/ΔΔG，计算成本高，精度有限。
3. **结构预测AI的置信度指标**: AlphaFold的plDDT、pTM等被广泛用作稳定性代理指标，在de novo设计筛选中表现有效，但无法提供定量ΔG。
4. **蛋白质语言模型代理**: ESM2伪似然、ESMtherm（微调ESM2）等尝试用序列模型预测ΔG，但ESMtherm存在过拟合问题，且未考虑结构信息。
5. **ΔΔG专用模型**: ThermoFold/ThermoMPNN等基于Mega-scale数据训练，但局限于同长度序列（单点突变）。
6. **本文位置**: IFUM首次将未折叠态系综显式建模（Flory模型）引入深度学习架构，通过联合学习ΔG与平衡系综距离图，同时处理点突变、indels和 disordered proteins，填补了绝对ΔG预测的空白。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 绝对ΔG预测精度不足 | 现有方法难以定量复现实验ΔG值 | 未折叠态被忽略或简化处理，而ΔG本质是折叠态与未折叠态的自由能差 | Introduction: "computational methods...show clear limitations in reproducing quantitative experimental values" |
| 未折叠态序列依赖性被忽视 | 多数深度学习方法将未折叠态视为与序列无关的零状态 | 未折叠态构象多样，难以用单一结构表示 | Introduction: "unfolded states of poly-Leu and poly-Lys peptides cannot be equal to each other" |
| 现有ΔΔG方法局限于点突变 | ThermoMPNN等无法处理插入/缺失 | 需要序列长度匹配的输入表示 | Results: "generally limited to single point mutations" |
| 结构预测AI指标非定量 | plDDT/pTM只能定性排序，不能给出ΔG数值 | 这些指标是为结构置信度设计，非热力学量 | Introduction: "not designed to estimate ΔG and therefore show limitations in providing a quantitative estimate" |
| 输入结构质量影响预测 | 低质量结构预测导致ΔG预测偏差 | 网络假设输入结构正确代表折叠态 | Discussion: "IFUM prediction is more reliable when supplied with more confident folded structural inputs" |
| 大蛋白绝对ΔG高估 | >200氨基酸蛋白出现异常高ΔG预测 | 训练数据长度限制与Flory模型在大蛋白上的偏差 | Discussion: "predictions of absolute stability for proteins larger than 200 amino acids might be treated with caution" |

## 06 核心思想

1. **表面方法**: 构建一个基于Transformer的深度网络IFUM，输入为ProtT5序列嵌入、ESMFold预测结构的距离图、ESM-IF1结构嵌入，联合预测ΔG、平衡系综距离图、序列恢复三个目标。

2. **核心洞察**: ΔG的定义是折叠态与未折叠态的自由能差（ΔG = –RT ln([U]/[F])），因此要准确预测ΔG，必须同时建模两个状态。作者提出用Flory无规线团模型解析计算未折叠态的残基对平均距离（仅依赖序列间隔|i−j|），用ESMFold预测结构代表折叠态，然后通过Boltzmann权重（由ΔG决定）混合两者得到"平衡系综距离图"作为训练目标。这一设计迫使网络同时学习ΔG和系综表示，形成协同约束。

3. **可能的普适教训** [Analysis]: 对于涉及构象系综的蛋白质性质预测（如IDP/IDR结合、相分离），单一结构表示本质上是不充分的。本文展示了如何用物理模型（Flory）提供解析的系综先验，再让网络学习修正——这种"物理先验+数据驱动"的混合策略可迁移到IDP/IDR体系。此外，联合学习多个热力学一致的目标（ΔG与系综）比单独学习任一目标更有效。

## 07 方法总览

- **输入**: 
  - 序列嵌入: ProtT5 (per-residue, [N, 1024])
  - 结构嵌入: ESM-IF1 (per-residue, [N, 512])
  - 折叠态距离图: ESMFold预测结构的Cα距离直方图 (one-hot, [N, N, 21], 2-42Å, bin宽2Å)
  
- **输出**: 
  - ΔG (标量，通过per-residue贡献求和)
  - 平衡系综距离图 ([N, N, 21])
  - 序列恢复 (辅助任务)

- **模块**:
  1. 嵌入投影层: 将序列和结构嵌入降维至[N, 21]
  2. 主模块: 11个修改版Evoformer块（保留三角乘法更新，移除三角注意力）
  3. 任务头: 三个MLP分别输出ΔG、系综距离图、序列恢复

- **训练**:
  - 损失函数: L = L_ΔG + 100·L_ensemble + L_seq
  - L_ΔG: 高斯负对数似然
  - L_ensemble: 交叉熵（预测系综距离图 vs 混合标签距离图）
  - L_seq: 交叉熵（序列恢复）
  - 优化器: AdamW, 学习率1e-4, 权重衰减0.01
  - 硬件: 单张A6000 48GB GPU

- **未折叠态建模**:
  - Flory模型: RMS距离 = √6 × 1.927 × |i−j|^0.598
  - 折叠态: ESMFold预测结构的Cα距离
  - 混合权重: p(F) = exp(ΔG/RT)/(1+exp(ΔG/RT)), p(U) = 1/(1+exp(ΔG/RT))
  - 混合标签距离图: 在r_F和r_U位置放置概率值，其余为0

- **数据**:
  - 训练: Mega-scale数据集（约65万条，30-80氨基酸）+ DisProt（3219条无序蛋白，≤70氨基酸）
  - 测试: Mega-scale测试集、CATH（6007条）、文献ΔG数据集（57条）、工程蛋白Tm数据集（26条）、de novo设计数据集（413条）

- **流程**: 输入序列→ProtT5/ESM-IF1/ESMFold生成嵌入和结构→主模块联合更新→三个任务头输出→加权损失训练

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| ProtT5序列嵌入 | 提供序列语义表示 | 捕获序列-稳定性关系 | 输入: 氨基酸序列; 输出: [N, 1024]嵌入 | 消融实验显示移除后性能下降 (Supplementary Table 3) | 预期显著降低ΔG预测精度（实测消融） |
| ESM-IF1结构嵌入 | 提供结构语义表示 | 捕获折叠态结构特征 | 输入: ESMFold预测结构; 输出: [N, 512]嵌入 | 消融实验显示移除后性能下降 (Supplementary Table 3) | 预期降低对结构敏感突变（如核心残基）的预测精度（实测消融） |
| 折叠态距离图输入 | 提供折叠态空间约束 | 网络需知道折叠态具体构象 | 输入: ESMFold结构Cα距离; 输出: [N, N, 21] one-hot | 核心输入，不可移除 | 移除后网络无法区分折叠态与未折叠态（预期） |
| 主模块（11×Evoformer变体） | 联合更新序列/结构/成对表示 | 捕获长程残基相互作用 | 输入: 拼接嵌入+距离图; 输出: 更新后的[N,21]和[N,N,21]表示 | 三角乘法更新保留、三角注意力移除（Methods） | 移除三角乘法更新预期显著降低精度（预期，基于AlphaFold2经验） |
| ΔG预测头 | 输出per-residue ΔG贡献 | 提供残基级稳定性分解 | 输入: 主模块嵌入; 输出: [N] per-residue ΔG | 用于指导残基级设计 (Discussion) | 移除后无法进行残基级稳定性分析（预期） |
| 系综距离图预测头 | 预测平衡态距离分布 | 核心创新：显式学习折叠/未折叠混合 | 输入: 主模块成对表示; 输出: [N, N, 21] | 消融实验显示移除后ΔG精度下降 (Supplementary Table 3) | 移除后ΔG预测精度显著下降（实测消融），证明联合学习有效 |
| 序列恢复头 | 辅助任务，增强序列表示 | 正则化，防止过拟合 | 输入: 主模块嵌入; 输出: [N, 20]氨基酸概率 | 消融实验显示移除后性能下降 (Supplementary Table 3) | 预期轻微降低泛化能力（实测消融） |
| Flory模型未折叠态计算 | 解析计算未折叠态距离 | 提供未折叠态先验，无需额外数据 | 输入: 序列长度N; 输出: [N, N] RMS距离矩阵 | Methods Eq.2 | 移除后网络需从数据隐式学习未折叠态，预期精度下降（预期） |

## 09 关键公式符号

1. **Flory无规线团模型** (Methods Eq. 2):
   D = R₀N^ν
   √⟨⟨r²ᵤᵢⱼ⟩⟩ = √6 × 1.927 × |i−j|^0.598
   - D: 均方根末端距
   - R₀: 特征比例常数 (1.927)
   - N: 链段数（此处为|i−j|，残基间隔）
   - ν: Flory指数 (0.598)
   - rᵤᵢⱼ: 未折叠态中残基i和j之间的Cα距离

2. **ΔG定义** (Introduction):
   ΔG = –RT ln([U]/[F])
   - R: 气体常数
   - T: 温度
   - [U], [F]: 未折叠态和折叠态的浓度

3. **Boltzmann权重** (Methods Eq. 3-5):
   [F]:[U] = exp(ΔG/RT):1
   p(rᶠᵢⱼ) = exp(ΔG/RT)/(1+exp(ΔG/RT))
   p(rᵘᵢⱼ) = 1/(1+exp(ΔG/RT))
   - p(rᶠᵢⱼ): 残基对(i,j)处于折叠态距离的概率
   - p(rᵘᵢⱼ): 残基对(i,j)处于未折叠态距离的概率

4. **总损失** (Methods Eq. 6):
   L = L_ΔG + 100·L_ensemble + L_seq
   - L_ΔG: 高斯负对数似然损失
   - L_ensemble: 系综距离图交叉熵
   - L_seq: 序列恢复交叉熵

5. **ESM2伪对数似然** (Methods Eq. 7):
   ESM2 pseudo loglikelihood = Σᵢ₌₁ᴺ log P_ESM2(rᵢ)
   - P_ESM2(rᵢ): ESM2预测第i个残基的概率

## 10 实验设计与证据链

**数据集与规模**:
- Mega-scale训练集: 约65万条序列（30-80 aa），含野生型和突变体
- Dispora训练集: 3219条无序蛋白（≤70 aa）
- Mega-scale测试集: 86条（野生型+de novo）
- CATH测试集: 6007条（≤869 aa）
- 文献ΔG数据集: 57条野生型蛋白（33-375 aa）
- 工程蛋白Tm数据集: 26条（12 IFN-λ, 8 IL-10, 6 UGT76G1）
- de novo设计数据集: 413条（5种折叠类型）

**指标**: RMSE, PCC, AUROC

**基线方法**: ESMtherm, ESM2伪似然, FoldX, Rosetta (FastRelax + Cartesian ddg), ThermoMPNN/ThermoMPNN-D

**评测协议**: 序列同一性<0.30过滤确保无泄漏；ΔG值clamp到[-1,5] kcal/mol（Mega-scale动态范围）

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|------------|-------------------|------|
| Mega-scale测试集ΔG预测 | IFUM能准确预测小蛋白ΔG | IFUM vs ESMtherm, ESM2, 长度基线 | PCC=0.78, RMSE=1.16 kcal/mol | IFUM优于所有基线 | 未与所有现有方法全面比较 | Fig. 2a |
| Mega-scale Common对比 | 公平比较IFUM与ESMtherm | 27个重叠域，5356条序列 | IFUM PCC=0.91, RMSE=0.78; ESMtherm PCC=0.86, RMSE=1.40 | IFUM显著优于ESMtherm | 样本量有限 | Fig. 2b |
| 消融实验 | 验证各组件贡献 | 移除未折叠态建模/三角更新/差分注意力/ProtT5 | 未折叠态建模移除后PCC从0.78降至0.70, RMSE从1.16升至1.39 | 未折叠态建模是关键创新 | 未报告所有消融组合的完整统计 | Fig. 2c, Supp. Table 3 |
| 稳定vs不稳定判别 | IFUM能区分稳定/不稳定蛋白 | Mega-scale测试集稳定(ΔG≥5) vs 不稳定(ΔG≤-1) | Welch's t-test p«0.001 | 判别力强 | 未报告AUC等判别指标 | Fig. 2e |
| CATH vs Dispora判别 | IFUM能区分折叠蛋白与无序蛋白 | 6007 CATH vs 685 Dispora | Welch's t-test p«0.001 | 能区分有序/无序 | 未报告具体PCC或AUC | Fig. 2g |
| 文献ΔG数据集 | 对较大天然蛋白的泛化能力 | 57条野生型蛋白(33-375 aa) | PCC=0.53 (全部), 随plDDT阈值提高而提升至0.97 | 结构质量影响预测精度 | 样本量小，需更多验证 | Fig. 2f, Supp. Fig. 5 |
| 工程蛋白Tm相关性 | 实际工程应用价值 | 26条工程序列(IFN-λ, IL-10, UGT76G1) | PCC=0.75, 0.62, 0.87 (分别) | 与实验Tm正相关 | 样本量极小，需谨慎解读 | Fig. 4a |
| de novo设计筛选 | 优于AlphaFold-based指标 | 413条de novo序列，5种折叠 | IFUM AUROC优于ESMfold/plDDT和AF3/plDDT | IFUM可作为设计筛选工具 | 仅二分类（表达/不表达），非稳定性直接测量 | Fig. 4b, c |
| FEP对比 | 与物理方法比较 | 76个非冗余FEP数据点 | IFUM RMSE=1.44 vs FEP+ RMSE=1.06 kcal/mol | FEP精度更高但计算成本高 | IFUM速度优势明显（30s vs 数小时） | Supp. Fig. 8 |

## 11 结论正确解读

- **可安全得出的结论**: IFUM通过显式建模未折叠态（Flory模型）联合学习ΔG与平衡系综，在小蛋白（≤80 aa）上实现了优于现有深度学习方法（ESMtherm、ESM2）的ΔG预测精度；在de novo设计筛选中优于plDDT指标；能处理点突变和indels。
- **不可过度推广的结论**: (1) 对>200 aa蛋白的绝对ΔG预测不可靠（存在系统性高估）；(2) 对高loop含量蛋白和IDPs存在预测偏差（倾向于预测过低稳定性）；(3) 与FEP相比精度仍有差距，不能替代精确物理方法；(4) 工程应用中的Tm相关性基于极小样本（n=6-12），需更大规模验证。
- **关键边界条件**: 训练数据以≤80 aa小蛋白为主；ΔG标签来自Mega-scale的推断值而非直接实验测量；未折叠态用Flory模型近似，可能不适用于所有序列。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 大蛋白绝对ΔG高估 | >200 aa蛋白出现>25 kcal/mol的异常预测 | 需扩展训练数据至更大蛋白 | Discussion: "predictions of absolute stability for proteins larger than 200 amino acids might be treated with caution" |
| 高loop含量蛋白系统性低估 | 对loop-rich蛋白预测稳定性偏低 | 可能需更精细的未折叠态模型 | Discussion: "systematic tendency to predict lower stability for high loop content proteins" |
| Flory模型近似局限 | 未折叠态可能偏离理想无规线团 | 探索更直接的未折叠态表示（如CALVADOS） | Discussion: "denatured state structural ensemble is different from the Flory model" |
| 不适用于膜蛋白和寡聚体 | 训练数据仅含可溶单体蛋白 | 未来扩展至膜蛋白和寡聚体 | Discussion: "does not apply to membrane proteins and obligate oligomers" |
| 对输入结构质量敏感 | 低质量折叠态结构导致预测偏差 | 建议使用高质量结构或AF3模型 | Discussion: "IFUM prediction is more reliable when supplied with more confident folded structural inputs" |
| 训练数据动态范围有限 | ΔG标签限于[-1,5] kcal/mol | 需更多极端稳定性数据 | Discussion: "restricted range inherent to the proteolysis-based experimental methodology" |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 训练数据ΔG标签来自Mega-scale的推断值 | 推断值可能包含系统误差，模型可能学习到推断方法的偏差而非真实热力学 | 影响所有下游预测的可信度 | 与独立实验测量的ΔG子集对比验证 | Methods: "deltaG values inferred from cDNA display proteolysis" |
| 消融实验中未折叠态建模的增益可能部分来自模型容量增加 | IFUM_baseline参数更少，性能差异可能源于容量而非概念创新 | 需区分架构创新与概念创新 | 控制参数量的消融实验 | Supp. Table 3 |
| 工程蛋白Tm相关性样本量极小（n=6-12） | 高PCC可能由个别离群点驱动 | 实际应用价值需更大规模验证 | 扩展至更多蛋白家族和突变体 | Fig. 4a |
| de novo筛选的"表达"标签是粗糙的二分类 | 表达成功≠折叠稳定，可能混淆稳定性和可表达性 | 筛选工具的实用性需更精细的标签 | 使用更精细的稳定性测量（如熔解温度） | Fig. 4b, c |
| 与FEP比较中未报告计算时间细节 | "30s vs 数小时"可能未包含结构预测和预处理时间 | 实际工作流总成本可能更高 | 端到端时间对比 | Supp. Fig. 8 |
| 未与最新的ΔΔG预测方法（如RaSP、DDMut）全面比较 | 对比基准可能不完整 | 无法确定IFUM在领域中的相对位置 | 扩展基准测试集 | 未提供 |
| 对IDP/IDR的"无序"处理过于简化 | 仅用Flory模型和低ΔG标签表示无序，未考虑结合诱导折叠等IDP特性 | 对IDP/IDR互作研究的可迁移性受限 | 在IDP/IDR结合体系上测试 | Discussion |

## 12 学到什么

**Agent 提炼的知识候选**:

1. **未折叠态显式建模（核心可迁移概念）**: 对于涉及构象系综的蛋白质性质预测，单一结构表示本质上不充分。IFUM展示了用物理模型（Flory无规线团）提供解析的未折叠态先验，再让网络学习修正的策略。**迁移到IDP/IDR互作**: 可将IDP的未折叠态/结合态平衡类似地参数化，用Flory模型或更精细的IDP系综模型（如CALVADOS）提供先验，让网络学习序列如何改变系综分布。

2. **联合学习热力学一致目标**: 同时预测ΔG和平衡系综距离图，形成协同约束，比单独学习任一目标更有效（消融实验证实）。**迁移**: 在IDP/IDR相分离预测中，可联合学习多组分化学势、饱和浓度和凝聚体内部结构，利用热力学一致性作为正则化。

3. **物理先验+数据驱动的混合策略**: 不抛弃物理模型，而是将其作为可微分的先验组件嵌入深度学习架构。**迁移**: 对IDP/IDR体系，可用SAXS/SANS或FRET实验导出的系综约束作为先验，与深度学习预测结合。

4. **残基级ΔG分解**: IFUM预测per-residue ΔG贡献，可用于指导残基级稳定性优化。**迁移**: 在IDP/IDR互作中，可类似地预测per-residue结合贡献或相分离驱动残基，指导突变设计。

5. **处理indels的能力**: 通过序列-结构联合建模，IFUM能处理插入/缺失突变，这是传统ΔΔG方法无法做到的。**迁移**: IDP/IDR区域经常发生插入/缺失（如重复序列扩增），此能力对IDP/IDR突变效应预测尤为重要。

6. **输入结构质量感知**: 作者发现输入结构质量直接影响预测精度，并建议使用高质量结构。**迁移**: 对IDP/IDR体系，结构预测本身不可靠，需开发"结构质量感知"的预测策略，或直接以系综表示替代单一结构输入。

7. **训练数据设计**: 将无序蛋白（DisProt）纳入训练并赋予低ΔG标签，帮助模型学习"无序"概念。**迁移**: 构建IDP/IDR互作训练集时，应包含正例（结合）和负例（不结合）以及不同无序程度的蛋白。

## 15 与已有知识连接

- **AlphaFold2 Evoformer架构**: IFUM的主模块是AlphaFold2 Evoformer的修改版（移除三角注意力，保留三角乘法更新）。这与Jumper et al. (2021) Nature的AlphaFold2架构直接相关，可参考原始Evoformer设计。
- **Flory无规线团模型**: 源自Flory (1953) 高分子物理经典理论，在IDP研究中被广泛用于描述无序态。本文用拟合参数（1.927, 0.598）来自Bernadó et al.或类似IDP系综研究。
- **Mega-scale数据集**: Tsuboyama et al. (2023) eLife的蛋白酶解稳定性数据集，包含约80万条小蛋白稳定性数据，是当前ΔG预测的主要训练资源。
- **ESMtherm**: 本文主要对比的深度学习方法，见Li et al. (2023)或相关预印本，是ESM2微调用于ΔG预测的代表。
- **ThermoMPNN**: 本文对比的ΔΔG预测方法，见Dieckhaus et al. (2024)或相关论文，是ProteinMPNN的稳定性预测变体。
- **IDP/IDR相分离连接** [Analysis]: 本文的未折叠态建模思想与IDP/IDR相分离研究中的"系综编码"概念高度一致。Brangwynne、Mittag、Pappu等团队的工作表明，IDP/IDR的相分离行为由序列编码的系综特性决定。IFUM的"物理先验+深度学习"框架可直接迁移到相分离预测，如用Flory-Huggins理论或随机相图模型作为先验，结合深度学习预测序列的相分离倾向。
- **无序蛋白稳定性**: 本文对IDP的ΔG处理（<0.5 kcal/mol标签）与IDP研究中的"边缘稳定性"概念一致，可连接Sanchez-Burgos et al.关于IDP稳定性的工作。

## 16 研究想法

**Agent 生成的研究候选**:

1. **IDP/IDR结合亲和力预测器（IDP-Bind）**
   - **来源局限/观察**: IFUM显式建模未折叠态提升了ΔG预测，但仅针对单域折叠蛋白。IDP/IDR介导的互作中，未折叠态是功能必需，结合常伴随折叠转变（coupled folding and binding）。
   - **核心假设**: 将IDP/IDR的结合态和自由态系综同时建模（类似IFUM的折叠/未折叠平衡），可提升IDP-蛋白结合亲和力预测精度。
   - **初步方法**: 扩展IFUM架构，输入为IDP序列+结合伴侣结构，输出为结合ΔG和结合态/自由态系综距离图。用Flory模型表示自由态，用伴侣结构约束表示结合态。
   - **验证方式**: 在已知IDP-蛋白互作数据集（如DIBS、BioGRID IDP子集）上测试，与AlphaFold-Multimer的pDockQ和现有亲和力预测器比较。
   - **创新状态**: unverified

2. **相分离驱动残基预测器（PS-Driver）**
   - **来源局限/观察**: IFUM的per-residue ΔG分解可用于指导稳定性工程。类似地，相分离由特定残基/短线性基序驱动，但目前缺乏残基级相分离贡献预测工具。
   - **核心假设**: 通过联合学习序列-相分离行为（饱和浓度、液滴性质）和残基级贡献，可识别驱动相分离的关键残基。
   - **初步方法**: 在IFUM架构基础上，将ΔG头替换为相分离相关输出（如饱和浓度、临界温度），增加per-residue贡献头。训练数据可用PhaSepDB、LLPSDB等。
   - **验证方式**: 预测的驱动残基与已知相分离突变（如ALS相关FUS突变）对比，实验验证选定位点的相分离行为变化。
   - **创新状态**: unverified

3. **IDR介导互作的系综感知对接（Ensemble-Dock-IDR）**
   - **来源局限/观察**: IFUM用Flory模型提供未折叠态先验，但IDP/IDR的未折叠态并非理想无规线团，存在瞬态结构（如pre-structured motifs）。
   - **核心假设**: 用分子模拟（如CALVADOS、ABSINTH）生成的IDR系综替代Flory模型，作为深度学习的未折叠态先验，可提升IDR-蛋白互作预测精度。
   - **初步方法**: 对训练集中的IDR序列运行粗粒化模拟生成系综距离图，替代Flory解析解；网络结构类似IFUM，但输入包含模拟系综特征。
   - **验证方式**: 在IDR-蛋白复合物结构预测任务上测试，与AlphaFold-Multimer和原始IFUM比较。
   - **创新状态**: unverified

4. **突变对IDR相分离影响的预测（Mut-PS）**
   - **来源局限/观察**: IFUM能预测indels的ΔG效应，但IDR/相分离中的突变效应（如磷酸化模拟突变、重复序列扩增）更为复杂。
   - **核心假设**: 将IFUM的系综建模扩展到相分离体系，可预测突变对相分离倾向的影响。
   - **初步方法**: 训练IFUM变体，输入为野生型和突变型序列，输出为相分离倾向差异（ΔΔG_PS）。训练数据来自文献中已知影响相分离的突变。
   - **验证方式**: 在独立突变数据集上测试，与实验相分离行为对比。
   - **创新状态**: unverified

5. **IDP/IDR结合诱导折叠的结构预测增强**
   - **来源局限/观察**: IFUM依赖ESMFold预测结构作为折叠态代理，但IDP/IDR在结合伴侣存在时才折叠，apo结构不可用。
   - **核心假设**: 将IFUM的系综建模与AlphaFold-Multimer结合，在预测IDP-伴侣复合物结构时显式考虑IDP的未折叠态贡献，可提升复合物结构预测精度。
   - **初步方法**: 在AlphaFold-Multimer的pairwise表示中注入IFUM的系综距离图特征，或在多序列比对中引入IDP系综约束。
   - **验证方式**: 在IDP-蛋白复合物基准集上测试，与AlphaFold-Multimer原始版本比较TM-score和界面残基精度。
   - **创新状态**: unverified