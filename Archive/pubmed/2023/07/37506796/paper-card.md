## 01 基本信息

- **标题**: Intrinsic disorder may drive the interaction of PROS1 and MERTK in uveal melanoma
- **作者与单位**: Djulbegovic, Mak; Taylor Gonzalez, David J; Antonietti, Michael; Uversky, Vladimir N; Shields, Carol L; Karp, Carol L（单位未提供）
- **期刊/预印本平台**: International Journal of Biological Macromolecules
- **年份**: 2023-07-29（在线发表）
- **论文类型**: 计算/生物信息学分析（无湿实验）
- **领域**: 无序蛋白（IDP/IDR）× 蛋白互作（PPI）× 癌症免疫微环境
- **关键词**: Intrinsic disorder; PROS1; MERTK; uveal melanoma; AlphaFold; ColabFold; IDPR; DOT
- **DOI/arXiv 号**: 10.1016/j.ijbiomac.2023.126027
- **代码**: 未提供
- **数据**: 未提供（使用公开数据库：UniProt、AlphaFoldDB、D2P2、STRING、IUPred3、PONDR 系列）
- **阅读日期**: 2026-05-13
- **在该课题方向中的位置**: 本文是「IDP/IDR × 蛋白互作 × AI 结构预测」交叉方向的代表性应用型研究——利用 AlphaFold/ColabFold 预测 PROS1-MERTK 复合物结构，结合多种无序预测工具，提出 IDR 和 DOT 区域可能驱动该 PPI 并可作为免疫治疗靶点。方法上属于「AI 结构预测 + 序列特征分析」的轻量级计算流程，未涉及 MD 模拟或深度学习模型训练。

---

## 02 一句话总结

本文利用 AlphaFold/ColabFold 预测 PROS1 与 MERTK 的复合物结构，结合多种无序预测工具，发现两者均为中度无序蛋白（PROS1 23.37%、MERTK 23.09%），PROS1 含两个半胱氨酸富集的 DOT 区域，推测内在无序可能驱动该 PPI 并可作为葡萄膜黑色素瘤免疫治疗靶点。

---

## 03 研究问题

- **具体问题**: PROS1 与 MERTK 的相互作用是否由内在无序蛋白区域（IDPR）或无序-有序转变（DOT）区域驱动？这些区域是否可作为免疫治疗靶点？
- **为什么重要**: Class 2 葡萄膜黑色素瘤（UM）中 BAP1 失活导致 PROS1 上调，PROS1 与 MERTK 结合促进免疫抑制微环境（TIME），是潜在免疫治疗靶点。理解该 PPI 的分子机制对药物设计至关重要。
- **现有方法不足**: 传统结构生物学方法（X 射线晶体学、冷冻电镜）难以解析含 IDR 的蛋白复合物；此前对该 PPI 的研究未从无序蛋白角度分析。
- **精确研究问题（Can...?）**: Can intrinsic disorder in PROS1 and MERTK drive their protein-protein interaction in uveal melanoma, and can DOT regions serve as immunotherapeutic targets?

---

## 04 背景与发展脉络

> 注：以下脉络为「经外部核验」的领域发展概述，结合本文引用与课题方向。

1. **无序蛋白概念建立（2000s）**：Dunker、Uversky 等人提出 IDP/IDR 概念，打破「序列-结构-功能」范式。Uversky 为本文共同作者，代表该脉络的延续。
2. **无序预测工具发展（2000s-2010s）**：PONDR 系列（VLXT、VL3、VSL2）、IUPred 等基于序列特征预测无序区域，成为 IDP 研究标准工具。
3. **AlphaFold 革命（2021）**：AlphaFold2 高精度预测单体结构；ColabFold 将 MMseqs2 同源搜索与 AlphaFold2 结合，支持多聚体预测，使无实验室条件的团队也能进行结构预测。
4. **IDR 在癌症免疫中的角色（2010s-2020s）**：IDR 参与信号转导、相分离、免疫检查点调控等，成为药物设计新靶点。
5. **本文位置**：将 AlphaFold/ColabFold 多聚体预测与无序分析工具结合，首次从 IDR 视角分析 PROS1-MERTK PPI，属于「AI 结构预测 + 无序分析」的交叉应用。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| PROS1-MERTK PPI 结构未知 | 此前无该复合物的高分辨率结构模型 | 含 IDR 的膜蛋白复合物难以用传统结构生物学方法解析 | Methods 节：使用 AlphaFold/ColabFold 进行结构预测 |
| 无序区域在 PPI 中的作用被忽视 | 传统药物设计聚焦有序结合口袋 | IDR 在结合中可发生无序-有序转变，提供结合可塑性 | Discussion 节：IDR 可能驱动 PPI |
| PROS1 半胱氨酸含量异常 | PROS1 含 36 个 Cys（5.3%），远高于平均水平（1.37%） | 半胱氨酸富集可能形成二硫键网络，与 DOT 区域相关 | Results 节 Compositional Profiler 部分 |
| 靶向该 PPI 的免疫治疗缺乏分子依据 | 无明确的靶向区域建议 | 未从无序角度分析可成药位点 | Conclusion 节：建议 DOT 区域作为靶点 |
| 计算预测的置信度有限 | pLDDT = 70.68，属「Confident」但非「Very High」 | AlphaFold 对含 IDR 复合物的预测精度有限 | Results 节 Structural Assessment 部分 |

---

## 06 核心思想

### 1) 表面方法
- 从 UniProt 获取 PROS1（P07225）和 MERTK（Q12866）的 canonical 序列
- 使用 ColabFold（alphafold2_multimer_v3_model）预测 PROS1-MERTK 复合物结构，pLDDT = 70.68
- 使用 Compositional Profiler 分析氨基酸组成偏好
- 使用 PONDR VLXT/VL3/VSL2、IUPred-Long/Short 进行逐残基无序预测
- 使用 D2P2 平台整合多种预测器，识别 IDR、MoRF、PTM 位点
- 使用 IUPred3 的 redox 工具识别 DOT 区域
- 使用 STRING 构建 PPI 网络（19 节点、40 边，p < 2.0×10⁻⁶）

### 2) 核心洞察
- **PROS1 和 MERTK 均为中度无序蛋白**（ADS ≈ 23%），其互作界面可能依赖 IDR 的构象可塑性
- **PROS1 含两个 DOT 区域**（残基 48–72 和 103–261），其中 48–72 区域富含半胱氨酸，可能在氧化还原环境变化时发生无序-有序转变
- **无序区域与 PTM 位点共定位**：PROS1 的 11 个羧化位点位于 GLA 结构域（最无序区域），提示无序可能促进 PTM 介导的调控
- **PPI 网络比预期更复杂**：40 条边 vs 期望 17 条，说明 PROS1-MERTK 并非简单一对一结合

### 3) 可能的普适教训 [Analysis]
- **AlphaFold 的 pLDDT 低分区域 ≠ 无结构区域**：低置信度区域往往对应 IDR，这为「用 AlphaFold 预测 IDR」提供了反向解读思路
- **氨基酸组成偏倚可作为 IDR 的快速筛查指标**：半胱氨酸富集 + 无序预测的一致性可交叉验证
- **DOT 区域是 IDR 介导 PPI 的功能热点**：在 IDP/IDR 相关课题中，优先关注 DOT 区域而非整体无序度
- **计算流程可复制性强**：ColabFold + 开源工具链，无需高性能计算即可完成初步 IDR-PPI 分析

---

## 07 方法总览

- **输入**: PROS1（UniProt P07225）和 MERTK（UniProt Q12866）的 canonical 氨基酸序列
- **输出**: 
  - PROS1-MERTK 复合物结构模型（pLDDT = 70.68）
  - 无序程度定量（% disorder、ADS）
  - DOT 区域定位
  - PPI 网络拓扑
- **模块**:
  1. 结构预测：ColabFold（MMseqs2 + AlphaFold2 multimer）
  2. 氨基酸组成分析：Compositional Profiler
  3. 逐残基无序预测：PONDR VLXT/VL3/VSL2、IUPred-Long/Short
  4. 功能注释：D2P2（整合预测器 + MoRF + PTM）
  5. DOT 识别：IUPred3 redox 工具
  6. PPI 网络：STRING（最高置信度 0.900）
- **训练**: 无（使用预训练模型 AlphaFold2）
- **工具**: UCSF ChimeraX-1.6.1（可视化）、Google Colaboratory（计算环境）、NVIDIA A100-SXM4-40GB GPU
- **反馈回路**: 无（单轮分析，无迭代优化）
- **文字流程**: 获取序列 → AlphaFold 单体结构可视化 → ColabFold 多聚体预测 → 氨基酸组成分析 → 多种无序预测器交叉验证 → D2P2 功能注释 → IUPred3 识别 DOT → STRING 构建 PPI 网络 → 综合解读

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| ColabFold 多聚体预测 | 预测 PROS1-MERTK 复合物结构 | 该 PPI 无实验结构，需计算模型 | 输入：两条序列；输出：复合物结构 + pLDDT | Results 节：pLDDT = 70.68 | 无法获得互作界面信息（预期影响，未做消融） |
| Compositional Profiler | 分析氨基酸组成偏倚 | 识别 IDR 相关的组成特征 | 输入：序列；输出：各氨基酸富集/耗竭 | Results 节：PROS1 富集 Cys（p<0.05） | 无法发现 Cys 异常富集（预期影响） |
| PONDR 系列 + IUPred | 逐残基无序预测 | 定量无序程度和位置 | 输入：序列；输出：无序分数谱 | Results 节：PROS1 23.37%、MERTK 23.09% 无序 | 无法定位 IDR 具体区域（预期影响） |
| D2P2 平台 | 整合多种预测器 + 功能注释 | 交叉验证无序预测，识别 MoRF/PTM | 输入：序列；输出：IDR/MoRF/PTM 图谱 | Results 节：PROS1 无 MoRF，MERTK 含 2 个 MoRF | 无法关联无序与 PTM 功能（预期影响） |
| IUPred3 redox 工具 | 识别 DOT 区域 | 定位氧化还原敏感的无序-有序转变区域 | 输入：序列；输出：DOT 区域坐标 | Results 节：PROS1 含 2 个 DOT（48–72、103–261） | 无法提出 DOT 作为靶点的核心发现（预期影响） |
| STRING PPI 网络 | 构建互作网络 | 评估 PPI 的复杂性和额外伙伴 | 输入：PROS1/MERTK 序列；输出：19 节点 40 边网络 | Results 节：p < 2.0×10⁻⁶ | 无法发现网络复杂性（预期影响） |

> 注：本文未做模块消融实验，所有「移除影响」均为 [Analysis] 预期推断。

---

## 09 关键公式符号

本文为生物信息学分析，无核心数学公式。涉及的关键计算概念：

- **归一化氨基酸富集/耗竭**：Cx − C_order / C_order，其中 Cx 为查询蛋白中某氨基酸含量，C_order 为 PDB Select 25 中该氨基酸含量。正值表示富集，负值表示耗竭。
- **无序百分比（PPDR）**：预测为无序的残基数 / 总残基数 × 100%
- **平均无序分数（ADS）**：所有残基无序预测分数的平均值
- **pLDDT（predicted Local Distance Difference Test）**：AlphaFold 输出的每个残基的预测置信度分数，范围 0–100。>90 为 Very High，70–90 为 Confident，50–70 为 Low，<50 为 Very Low
- **STRING 网络富集 p 值**：观察到的边数 vs 随机期望边数的超几何检验，p < 2.0×10⁻⁶

---

## 10 实验设计与证据链

### 数据集/群体/规模
- **蛋白质序列**: PROS1（676 aa，UniProt P07225）、MERTK（999 aa，UniProt Q12866）
- **复合物**: PROS1-MERTK 共 1,675 残基
- **PPI 网络**: 19 个节点（第一层互作伙伴），40 条边
- **物种**: 人类（human variants）
- **比较物种（仅 PROS1）**: 猴、猪、大鼠、小鼠、兔（用于 MSA 保守性分析）

### 指标
- pLDDT（结构预测置信度）
- PPDR（无序残基百分比）
- ADS（平均无序分数）
- 氨基酸富集/耗竭 p 值（< 0.05）
- STRING 网络富集 p 值（< 2.0×10⁻⁶）

### 基线/对比
- 无显式基线模型；无序预测使用多种工具交叉验证（PONDR VLXT/VL3/VSL2、IUPred-Long/Short）
- 氨基酸组成对比基线为 PDB Select 25（高有序蛋白集合）

### 评测协议
- 无标准评测协议；采用多工具一致性 + 结构可视化 + 保守性分析的综合判断

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|-----------------|------|
| AlphaFold 单体结构预测 | PROS1/MERTK 含 IDR | 无对比，仅可视化 | 两蛋白均含低置信度区域（黄/橙色） | 存在 IDR | 无法确定 IDR 的功能角色 | Results 节 Figure 2 |
| ColabFold 多聚体预测 | PROS1-MERTK 可形成复合物 | 无对比 | pLDDT = 70.68（Confident） | 成功建模复合物 | 无法验证体内真实结合 | Results 节 Figure 3 |
| Compositional Profiler | PROS1 富集 Cys | 对比 PDB Select 25 | PROS1 含 36 Cys（5.3%），显著富集（p<0.05） | Cys 富集可能参与二硫键网络 | 无法证明 Cys 与 DOT 的因果关系 | Results 节 Figure 4 |
| PONDR/IUPred 无序预测 | 两蛋白为中度无序 | 多工具交叉验证 | PROS1 23.37%、MERTK 23.09% 无序 | 均为中度无序蛋白 | 无法确定无序区域的具体功能 | Results 节 Figure 5 |
| IUPred3 redox 分析 | PROS1 含 DOT 区域 | 无对比 | 两个 DOT 区域（48–72、103–261） | DOT 可能驱动 PPI | 无法验证 DOT 在体内的转变 | Results 节 Figure 7 |
| STRING PPI 网络 | PPI 网络复杂 | 随机期望 17 边 vs 实际 40 边 | p < 2.0×10⁻⁶ | 网络显著富集 | 无法确定哪些边是直接物理结合 | Results 节 Figure 9 |
| MSA 保守性分析 | 无序区域保守 | 5 个物种对比 | 部分区域保守 | 保守区域可能功能重要 | 无法确定保守性与 PPI 的关联 | Results 节 Figure 5B/5D |

---

## 11 结论正确解读

- **任务范围**: 本文仅做计算预测，无任何湿实验验证。所有结论均为「预测」或「建议」，非实验证实。
- **Oracle/真值输入**: 使用 UniProt canonical 序列作为输入，未考虑异构体、突变或翻译后修饰对结构的影响。
- **端到端状态**: 非端到端。结构预测（ColabFold）与无序分析（PONDR/IUPred）是独立流程，未整合为统一模型。
- **算力成本**: 使用 Google Colaboratory 免费/低成本环境 + 单张 A100 GPU，成本较低，可复现性强。
- **历史数据依赖**: 依赖 AlphaFold2 训练数据（PDB 等），对 IDR 的预测能力有限，因为训练集富含有序蛋白结构。
- **模型依赖**: 结果高度依赖 AlphaFold2/ColabFold 的预测精度；pLDDT = 70.68 仅属「Confident」，非高置信度。
- **最难情形**: 含 IDR 的膜蛋白复合物预测是 AlphaFold 的已知难点；PROS1-MERTK 的互作界面可能涉及无序-有序转变，AlphaFold 难以准确捕捉。
- **群体/领域边界**: 结论仅针对葡萄膜黑色素瘤中 PROS1-MERTK 互作，不可推广至其他肿瘤或 PPI。
- **不确定性**: 作者未提供置信区间或误差分析；DOT 区域的 redox 敏感性为预测，未经验证。
- **有边界的复述**: 本文通过计算分析预测 PROS1 和 MERTK 均为中度无序蛋白，PROS1 含两个半胱氨酸富集的 DOT 区域，这些区域可能驱动 PPI 并可作为免疫治疗靶点；但所有结论均为计算预测，需实验验证。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| AlphaFold 不模拟物理折叠过程 | 无法捕捉无序-有序转变的动态过程 | 建议进行分子动力学模拟 | Discussion 节 |
| 计算预测需实验验证 | 所有发现为理论推测 | 建议结合体外药物发现实验 | Discussion 节 |
| ColabFold 多聚体预测精度有限 | 相比本地 AlphaFold 安装可能有精度损失 | 建议使用本地 AlphaFold 安装提高精度 | Discussion 节 |
| 未使用 IDP 专用力场 | 未进行 MD 模拟 | 建议使用 ff14IDPSFF、ESFF1、ff03CMAP 等 IDP 专用力场 | Discussion 节 |
| PPI 网络复杂可能限制靶向治疗 | PROS1 和 MERTK 有 promiscuous binding | 需考虑网络复杂性 | Discussion 节 |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| pLDDT = 70.68 被解读为「成功建模」 | 70.68 仅属「Confident」，对含 IDR 的复合物可能不可靠；AlphaFold 对 IDR 区域常给出低置信度，但低置信度 ≠ 正确预测无序 | 核心结论（IDR 驱动 PPI）依赖该模型的可靠性 | 与实验结构（如交联质谱、SAXS）对比；或使用多个独立预测器交叉验证 | Results 节 Figure 3 |
| PROS1 的 Cys 富集被赋予功能意义 | Cys 富集可能仅是序列进化痕迹，不必然与 DOT 或 PPI 相关；36 个 Cys 中多数可能形成结构二硫键而非参与 redox 调控 | 若 Cys 富集与 DOT 无因果关系，则 DOT 作为靶点的建议缺乏基础 | 定点突变 Cys 后检测 DOT 转变；或检测氧化还原条件下的构象变化 | Results 节 Figure 4 |
| 「中度无序」分类依赖任意阈值 | 23.37% 和 23.09% 的 ADS 分类为「中度无序」依赖文献阈值，不同工具可能给出不同结果 | 分类影响后续所有解读 | 使用多种无序预测器（如 IUPred3、ESPritz、PrDOS）比较一致性 | Results 节 Figure 5 |
| STRING 网络富集被过度解读 | p < 2.0×10⁻⁶ 仅说明网络非随机，不证明 PROS1-MERTK 的直接物理结合或功能关联 | 网络复杂性可能被用作「靶向困难」的论据，但网络分析不能替代直接互作实验 | 使用 co-IP、pull-down 或表面等离子共振验证直接结合 | Results 节 Figure 9 |
| 未讨论 PROS1 的 GLA 结构域功能 | GLA 结构域是维生素 K 依赖性羧化位点，其无序性可能仅是羧化修饰的底物需求，而非 PPI 驱动因素 | 若 GLA 结构域的无序是 PTM 需求而非 PPI 需求，则 DOT 作为 PPI 靶点的逻辑需修正 | 比较 GLA 结构域在其他维生素 K 依赖性蛋白中的无序程度 | Results 节 Figure 6A |
| 无阴性对照 | 未分析已知有序蛋白作为对照，无法证明 PROS1/MERTK 的无序程度具有特异性 | 缺乏对照削弱「无序驱动 PPI」的论证强度 | 加入已知有序互作蛋白对作为对照分析 | 全文未提供 |

---

## 14 Agent 提炼的知识候选

> 标题：Agent 提炼的知识候选

1. **AlphaFold 低置信度区域可作为 IDR 的代理指标**：本文展示了如何将 AlphaFold 的 pLDDT 低分区域（黄/橙色）解读为潜在 IDR。在 IDP/IDR × 蛋白互作课题中，可先用 AlphaFold 快速筛查 IDR 候选区域，再用专用无序预测器验证。**迁移方式**：对目标 IDP/IDR 蛋白运行 AlphaFold，提取 pLDDT < 50 的连续区域作为 IDR 候选。

2. **多工具交叉验证的无序分析流程**：本文使用了 PONDR VLXT/VL3/VSL2、IUPred-Long/Short、D2P2 等多种工具，通过一致性判断无序区域。**迁移方式**：在 IDR 分析中，不依赖单一预测器，至少使用 3 种以上工具交叉验证，并报告一致性区域。

3. **DOT 区域作为 IDR 介导 PPI 的功能热点**：本文识别了 PROS1 中两个 DOT 区域，并建议将其作为药物靶点。**迁移方式**：在 IDP/IDR 互作研究中，优先分析 DOT 区域（无序→有序转变），而非整体无序度，因为 DOT 区域更可能直接参与结合。

4. **氨基酸组成偏倚与无序预测的交叉验证**：PROS1 的 Cys 富集与 DOT 区域共定位，提示组成偏倚可作为无序功能的补充证据。**迁移方式**：对目标 IDR 进行氨基酸组成分析，特别关注 Cys、Pro、Gly、Ser 等无序相关残基的富集/耗竭。

5. **ColabFold 多聚体预测的轻量级流程**：本文展示了在 Google Colaboratory 上运行 ColabFold 预测蛋白复合物的可行性，成本低、可复现。**迁移方式**：对 IDP/IDR 介导的 PPI 复合物，先用 ColabFold 预测结构，再结合无序分析解读互作界面。

6. **STRING 网络分析揭示 PPI 复杂性**：本文用 STRING 展示了 PROS1-MERTK 网络比预期更复杂（40 边 vs 17 期望边）。**迁移方式**：在研究 IDP/IDR 介导的 PPI 时，用 STRING 评估目标蛋白的互作网络复杂度，避免过度简化为一对一模型。

7. **IDR 与 PTM 共定位分析**：PROS1 的 11 个羧化位点位于最无序的 GLA 结构域，提示无序区域可能促进 PTM 介导的调控。**迁移方式**：在 IDR 分析中，将无序预测与 PTM 数据库（如 PhosphoSitePlus）交叉比对，识别无序-PTM 共定位的功能候选区域。

8. **计算预测的边界意识**：本文明确承认所有发现为理论预测，需实验验证。**迁移方式**：在 IDP/IDR 计算研究中，明确区分「预测」与「验证」，避免过度解读计算结果的生物学意义。

---

## 15 与已有知识连接

1. **Uversky 课题组的工作**：本文共同作者 Uversky 是无序蛋白领域的奠基人之一，其早期工作建立了 IDP 的序列-功能关系框架（如 charge-hydropathy 分析）。本文是该框架在葡萄膜黑色素瘤中的延伸应用。

2. **AlphaFold2 与 IDR 预测的张力**：AlphaFold2 训练数据富含有序蛋白，对 IDR 的预测能力有限。本文的「低置信度区域 = IDR」解读与已知文献一致（如 Tunyasuvunakool et al. 2021, Nature 指出 pLDDT < 50 对应无序区域）。

3. **PROS1-MERTK 信号轴**：Kaler et al. 2022 首次报道 BAP1 缺失导致 PROS1 上调并激活 MERTK 通路，本文在此基础上从无序角度深化了分子机制理解。

4. **IDR 作为药物靶点**：已知 IDR 在癌症信号通路中广泛参与（如 p53、MYC 等），本文建议将 DOT 区域作为免疫治疗靶点，与「无序蛋白靶向」领域（如 PROTAC、分子胶）的趋势一致。

5. **葡萄膜黑色素瘤免疫治疗**：UM 对免疫检查点抑制剂反应差，本文提出的靶向 PROS1-MERTK PPI 的免疫治疗策略是对该领域的新贡献。

6. **ColabFold 的广泛应用**：Mirdita et al. 2022 开发 ColabFold 后，已被广泛用于无 GPU 资源的课题组进行蛋白复合物预测。本文是该工具在 IDR-PPI 研究中的典型案例。

7. **D2P2 平台**：Oates et al. 2013 开发 D2P2 整合多种无序预测器，本文使用该平台进行功能注释，代表 IDR 分析的标准流程。

---

## 16 Agent 生成的研究候选

> 标题：Agent 生成的研究候选

### 候选 1：基于 AlphaFold pLDDT 的 IDR 介导 PPI 界面预测框架
- **来源局限/观察**：本文仅用 ColabFold 预测了一个复合物，未系统评估 pLDDT 低分区域与 PPI 界面的关联
- **核心假设**：在 IDP/IDR 介导的 PPI 中，互作界面残基的 pLDDT 显著低于蛋白整体平均水平，且 DOT 区域残基的 pLDDT 变化可预测结合亲和力
- **初步方法**：收集已知 IDR 介导的 PPI 复合物（如 PROS1-MERTK、p53-MDM2 等），运行 ColabFold 预测，提取界面残基 pLDDT，与实验结合亲和力数据回归分析
- **验证方式**：与实验结构（PDB）或交联质谱数据对比；ROC 曲线评估 pLDDT 作为界面预测指标的灵敏度/特异度
- **创新状态**：unverified

### 候选 2：DOT 区域作为免疫治疗靶点的系统筛选
- **来源局限/观察**：本文仅识别了 PROS1 中两个 DOT 区域，未系统筛选其他肿瘤相关 PPI 中的 DOT
- **核心假设**：在肿瘤免疫相关 PPI 网络中，DOT 区域富集的蛋白更可能是可成药靶点
- **初步方法**：从 STRING/BioGRID 获取肿瘤免疫相关 PPI 网络，对每个蛋白运行 IUPred3 redox 分析，识别 DOT 区域；与已知药物靶点数据库（DrugBank）交叉比对
- **验证方式**：统计 DOT 富集蛋白与已知药物靶点的重叠显著性；选择 top 候选进行分子动力学模拟验证
- **创新状态**：unverified

### 候选 3：IDR 介导 PPI 的 MD 模拟力场评估
- **来源局限/观察**：本文作者建议进行 MD 模拟但未执行，且未讨论 IDP 专用力场的选择
- **核心假设**：IDP 专用力场（如 ff14IDPSFF、ESFF1）比通用力场（如 AMBER ff14SB）更准确描述 PROS1-MERTK 的 IDR 介导结合
- **初步方法**：用 ColabFold 预测的复合物结构作为起点，分别用通用力场和 IDP 专用力场进行 MD 模拟，比较结合自由能、界面残基构象系综
- **验证方式**：与实验结合亲和力数据对比；检查 IDR 区域的构象采样是否与 NMR/SAXS 实验一致
- **创新状态**：unverified

### 候选 4：PROS1-MERTK 的 redox 依赖性结合机制
- **来源局限/观察**：本文识别了 PROS1 的 DOT 区域富含 Cys，但未深入探讨 redox 调控机制
- **核心假设**：PROS1 的 Cys 残基在氧化条件下形成二硫键，改变 DOT 区域构象，从而调控 MERTK 结合
- **初步方法**：对 PROS1 的 Cys 进行氧化还原敏感性分析（如 Cys 氧化状态预测工具），结合 MD 模拟比较氧化/还原状态下的构象差异
- **验证方式**：体外实验（如氧化还原条件下的 pull-down）；或与已知 redox 调控蛋白（如 p53）的机制对比
- **创新状态**：unverified

### 候选 5：IDR 介导 PPI 的深度学习结合位点预测
- **来源局限/观察**：本文使用 AlphaFold 预测结构但未利用深度学习预测结合位点
- **核心假设**：现有结合位点预测工具（如 P2Rank、DeepSite）在 IDR 介导的 PPI 上表现不佳，需要针对 IDR 特征（无序分数、组成偏倚）进行微调
- **初步方法**：收集 IDR 介导的 PPI 数据集，提取序列特征（无序分数、氨基酸组成、PTM 位点）+ 结构特征（pLDDT、溶剂可及性），训练结合位点预测模型
- **验证方式**：与 P2Rank 等基线工具对比；在 PROS1-MERTK 等案例上进行外部验证
- **创新状态**：unverified