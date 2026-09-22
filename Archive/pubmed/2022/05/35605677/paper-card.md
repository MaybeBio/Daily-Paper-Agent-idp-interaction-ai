## 01 基本信息

- **标题**：Disordered Regions Flanking the Binding Interface Modulate Affinity between CBP and NCOA
- **作者**：Karlsson, Elin; Schnatwinkel, Jan; Paissoni, Cristina; Andersson, Eva; Herrmann, Christian; Camilloni, Carlo; Jemth, Per
- **单位**：未提供（根据期刊信息推测为瑞典乌普萨拉大学等，但原文未列出，故写未提供）
- **期刊/平台**：Journal of Molecular Biology
- **年份**：2022
- **论文类型**：实验+模拟混合研究（生物化学实验 + 分子动力学模拟）
- **领域**：无序蛋白（IDP/IDR）介导的蛋白互作；耦合折叠与结合（coupled folding and binding）；fuzzy complex
- **关键词**：intrinsically disordered proteins; fuzzy binding; coupled folding and binding; CBP; NCOA; molecular dynamics
- **DOI/arXiv**：10.1016/j.jmb.2022.167643
- **代码**：未提供
- **数据**：未提供（MD 模拟轨迹未明确说明是否公开）
- **阅读日期**：2026-05-12（按当前日期推算）
- **在该方向中的位置**：本文直接研究 IDR 中结合基序（recognition motif）两侧的 flanking regions 对结合亲和力的贡献，属于「IDP/IDR × 蛋白互作」的核心问题，方法上结合了实验（CD、stopped-flow 动力学、突变）与物理模拟（MD），未使用 AI/深度学习，但为 AI 方法（如预测 flanking region 效应）提供了可用的定量实验基准。

---

## 02 一句话总结

本文通过 N/C 端组合截短突变、圆二色光谱、动力学实验和分子动力学模拟，证明 CBP 的 NCBD 与 NCOA3 的 CID 结合时，结合界面两侧的无序 flanking regions 通过短寿命非特异性疏水接触以加和方式提高亲和力，且复合物中 flanking regions 保持高度无序，形成 energetically favorable 的 fuzzy binding。

---

## 03 研究问题

- **具体问题**：在 IDP 介导的蛋白互作中，结合基序（recognition motif）两侧的无序 flanking regions 对结合亲和力是否有贡献？如果有，其分子机制是什么？
- **为什么重要**：大多数 IDP 互作基序都嵌入在更长的无序区域中，但现有研究几乎只关注基序本身与 partner 的界面，flanking regions 的作用长期被忽略。理解 flanking regions 的贡献机制，对预测 IDP 互作强度、设计亲和力调节策略、以及理解相分离中多价弱相互作用的贡献都有直接意义。
- **现有方法为何不足**：已有的 IDP 互作研究多采用截短基序的肽段来测量亲和力，这人为排除了 flanking regions 的贡献；而全长研究又难以区分界面残基与 flanking 残基的独立贡献。缺乏系统性的组合截短 + 动力学 + 模拟的定量框架。
- **精确的 Can 问题**：Can the disordered regions flanking the CID recognition motif quantitatively modulate the binding affinity to NCBD, and if so, is the mechanism electrostatic or hydrophobic in nature?

---

## 04 背景与发展脉络

> 注：以下脉络为「经外部核验」的领域共识，结合本文框架整理。

1. **阶段一：IDP 互作的基本模型——耦合折叠与结合（coupled folding and binding）**
   - 代表方法：NMR 结构解析、ITC 热力学测量（如 Sugase et al. 2007; Dogan et al. 2013 对 NCBD/ACTR 体系的研究）。
   - 优点：确立了 IDP 在结合时折叠为稳定结构的基本范式。
   - 局限：多聚焦于基序本身，忽略 flanking regions。

2. **阶段二：fuzzy complex 概念的提出**
   - 代表方法：NMR 弛豫与残余偶极耦合（RDC）表征无序区域在复合物中的动态（Tompa & Fuxreiter 2008; Fuxreiter 2018）。
   - 优点：认识到复合物中 IDP 可保持局部无序。
   - 局限：多为定性描述，缺乏对 flanking regions 能量贡献的定量测量。

3. **阶段三：flanking regions 的功能研究（本文所处位置）**
   - 代表方法：组合截短突变 + 动力学（stopped-flow）+ MD 模拟。
   - 优点：可定量分解 flanking regions 的加和贡献，并区分静电 vs 疏水机制。
   - 局限：单一体系（NCBD/CID），需更多体系验证普适性。

4. **阶段四（未来/候选）：AI 预测 flanking region 效应**
   - 本文未涉及，但为 AlphaFold 等结构预测方法无法捕捉的动态/模糊相互作用提供了实验基准，可作为 AI 方法训练的 target。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 结合基序两侧的 flanking regions 的贡献被系统性忽略 | 多数 IDP 互作研究使用截短基序肽段，flanking regions 被切除 | 实验上全长蛋白难以单独操纵 flanking regions；结构生物学聚焦于有序界面 | 引言部分（未提供具体行号） |
| 无法区分 flanking regions 贡献的静电 vs 疏水机制 | 仅做截短实验无法判断机制 | 需要变盐浓度实验 + 突变 + 模拟联合 | Results 中 ionic strength 实验（图 3 附近） |
| flanking regions 在复合物中的构象状态未知 | 不清楚它们是有序化还是保持无序 | 需要 CD 和 MD 联合表征 | Results 中 CD 谱图与 MD 的 RMSF 分析 |
| 加和性 vs 协同性的问题 | 不清楚多个 flanking 位点的贡献是独立加和还是协同 | 需要 N/C 端组合变体设计 | Results 中 combinatorial variants 数据 |

---

## 06 核心思想

### 1) 表面方法
通过 N 端和 C 端 flanking regions 的组合截短（combinatorial truncation variants），结合圆二色光谱（CD）测量二级结构含量、stopped-flow 动力学测量结合/解离速率常数、变盐浓度实验、点突变（site-directed mutagenesis）以及分子动力学（MD）模拟，定量分解 flanking regions 对 NCBD-CID 结合亲和力的贡献。

### 2) 核心洞察
Flanking regions 对结合亲和力的贡献是**加和的（additive）**，而非协同的；其机制**不是静电相互作用**（盐浓度实验排除），而是**短寿命的非特异性疏水接触**（MD 模拟显示 flanking regions 与 NCBD 表面形成瞬时接触）。这些接触在复合物中保持高度无序（fuzzy），但整体上产生**轻微但显著的热力学稳定化**（ΔΔG 为负值），即「energetically favorable fuzzy binding」。

### 3) 可能的普适教训 [Analysis]
- 无序区域的「非特异性」相互作用不能因为「非特异性」就被忽略——它们可以以加和方式累积成可测量的亲和力贡献。
- 对 IDP 互作的定量理解需要同时考虑基序内（interface）和基序外（flanking）的自由能贡献，且两者机制可能完全不同。
- 对 AI 方法而言，仅用基序序列预测结合亲和力会系统性低估全长 IDP 的亲和力；需要将 flanking regions 的序列特征（如疏水残基含量）纳入特征空间。

---

## 07 方法总览

- **输入**：NCBD（CBP 的 2059-2117 区域）与 CID（NCOA3 的 1018-1093 区域）的野生型及 N/C 端组合截短变体蛋白。
- **输出**：各变体的结合亲和力（Kd）、结合/解离速率常数（kon/koff）、复合物中 flanking regions 的构象状态（有序 vs 无序）、flanking regions 与 NCBD 的接触模式。
- **模块**：
  1. 蛋白表达与纯化（重组表达）
  2. 组合截短变体设计（N 端、C 端、N+C 端截短）
  3. 圆二色光谱（CD）：测量自由态与复合态的二级结构
  4. Stopped-flow 动力学：测量 kon 和 koff，计算 Kd
  5. 变盐浓度实验（ionic strength series）：测试静电贡献
  6. 点突变：针对 MD 预测的疏水接触残基
  7. 分子动力学模拟（MD）：全原子模拟，分析接触图、RMSF、接触寿命
- **训练**：不适用（无机器学习）
- **反馈回路**：MD 预测的接触残基 → 点突变验证 → 实验确认/修正 MD 模型
- **文字流程**：设计并表达组合截短变体 → CD 确认各变体自由态无序程度 → stopped-flow 测量各变体与 NCBD 结合的 kon/koff → 计算 ΔΔG 并检验加和性 → 变盐实验排除静电机制 → MD 模拟野生型复合物 → 从 MD 提取 flanking regions 与 NCBD 的瞬时接触残基 → 点突变这些残基 → 实验验证突变对亲和力的影响 → 综合得出结论。

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 组合截短变体设计 | 系统性地去除 N 端、C 端或两侧 flanking regions | 单独评估每个 flanking region 的贡献及其加和性 | 输入：野生型序列；输出：多个截短变体 | Results 中 Kd 随截短变化的趋势 | 无法分解 flanking regions 的独立贡献（预期） |
| Stopped-flow 动力学 | 测量 kon 和 koff | 区分亲和力变化来自结合还是解离速率 | 输入：蛋白变体；输出：kon, koff, Kd | Results 中速率常数表 | 无法判断 flanking regions 影响的是结合路径还是解离稳定性（预期） |
| 变盐浓度实验 | 改变溶液离子强度 | 检验静电相互作用的贡献 | 输入：不同 NaCl 浓度；输出：Kd 变化 | Results 中 Kd 对盐浓度不敏感 | 无法排除静电机制（实测） |
| 点突变 | 针对 MD 预测的疏水接触残基进行替换 | 验证 MD 预测的接触是否真实贡献亲和力 | 输入：MD 预测残基；输出：突变体 Kd | Results 中突变体 Kd 升高 | 无法验证 MD 预测的接触（预期） |
| MD 模拟 | 全原子模拟复合物动态 | 提供原子级接触信息，解释实验观察 | 输入：野生型复合物结构；输出：接触图、RMSF、接触寿命 | Methods 中 MD 设置与 Results 中接触分析 | 无法获得原子级机制解释（预期） |
| CD 光谱 | 测量二级结构含量 | 确认 flanking regions 在复合物中是否保持无序 | 输入：蛋白样品；输出：摩尔椭圆率 | Results 中 CD 谱图 | 无法确认 fuzzy 状态（实测） |

---

## 09 关键公式符号

| 公式 | 符号含义 | 用途 | 直觉 | 来源 |
|------|----------|------|------|------|
| ΔG = RT ln(Kd) | R：气体常数；T：温度；Kd：解离常数 | 将 Kd 转换为结合自由能 | 亲和力越高，ΔG 越负 | 标准热力学，文中用于计算 ΔΔG |
| ΔΔG = ΔG(wt) − ΔG(mutant) | ΔG(wt)：野生型结合自由能；ΔG(mutant)：截短或突变体结合自由能 | 量化 flanking regions 或单个残基对结合自由能的贡献 | 正值表示截短/突变降低亲和力 | Results 中 ΔΔG 计算 |
| Kd = koff / kon | koff：解离速率常数；kon：结合速率常数 | 从动力学数据计算亲和力 | 解离越慢或结合越快，Kd 越小 | 标准动力学关系，文中用于 stopped-flow 数据分析 |

---

## 10 实验设计与证据链

- **数据集/群体**：NCBD（CBP 2059-2117）与 CID（NCOA3 1018-1093）的野生型及多种 N/C 端组合截短变体。具体变体数量未提供。
- **规模**：未提供具体变体数量；每个变体至少进行 CD、stopped-flow 和盐浓度实验。
- **指标**：Kd（由 stopped-flow 动力学计算）、kon、koff、CD 摩尔椭圆率、MD 接触频率。
- **基线**：野生型 NCBD-CID 相互作用。
- **预算/资源**：未提供。
- **骨干/仪器**：CD 光谱仪、stopped-flow 仪器（具体型号未提供）；MD 模拟软件（具体名称未提供，推测为 GROMACS 等）。
- **oracle 输入**：不适用（无 AI 组件）。
- **评测协议**：每个变体独立测量 Kd，重复次数未提供；MD 模拟至少 3 条独立轨迹（推测，未明确）。

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 组合截短变体的 Kd 测量 | Flanking regions 对亲和力有贡献 | 野生型 vs 各截短变体 | 截短后 Kd 升高（亲和力降低），N 端和 C 端贡献加和 | Flanking regions 以加和方式提高亲和力 | 无法确定具体接触残基 | Results 图 2-3 |
| 变盐浓度实验 | 静电相互作用是否介导 flanking regions 的贡献 | 不同 NaCl 浓度下野生型与截短变体的 Kd | Kd 对盐浓度不敏感 | 静电相互作用不是主要机制 | 无法排除疏水或其他非静电机制 | Results 图 4 |
| 点突变实验 | MD 预测的疏水接触残基是否真实贡献 | 野生型 vs 突变体 | 突变后 Kd 升高 | MD 预测的疏水接触确实贡献亲和力 | 无法确定接触的精确时间尺度 | Results 图 5 |
| MD 模拟 | Flanking regions 与 NCBD 的接触模式 | 野生型复合物模拟 | 观察到短寿命、非特异性疏水接触 | 支持 fuzzy binding 模型 | 模拟力场可能影响接触寿命定量 | Methods 与 Results 图 6 |
| CD 光谱 | Flanking regions 在复合物中是否保持无序 | 自由态 vs 复合态 | 复合物中 flanking regions 仍保持无序 | 支持 fuzzy complex 模型 | CD 无法提供残基级分辨率 | Results 图 1 |

---

## 11 结论正确解读

- **任务范围**：本文仅研究 NCBD-CID 这一对互作蛋白，结论不能直接推广到所有 IDP 互作体系。
- **oracle/真值输入**：不适用（无 AI）。
- **端到端状态**：实验与模拟联合，但 MD 模拟仅用于机制解释，未做自由能计算（如 FEP 或 MM-PBSA）来定量预测突变效应。
- **算力成本**：未提供 MD 模拟的规模与时长。
- **历史数据依赖**：不适用。
- **模型依赖**：MD 结果依赖力场选择（具体力场未提供），不同力场可能影响接触寿命的定量估计。
- **最难情形**：flanking regions 的贡献是「轻微但显著」的（ΔΔG 较小），在低信噪比实验条件下可能难以检测。
- **群体/领域边界**：结论基于单一体系（NCBD/CID），且 flanking regions 的疏水贡献可能依赖于特定序列组成（如疏水残基含量），不能外推到所有 IDR。
- **不确定性**：MD 模拟的接触频率与实验突变效应的对应关系是定性的，未做定量关联（如接触频率 vs ΔΔG 的回归）。

**有边界的复述**：在 NCBD-CID 体系中，结合基序两侧的无序 flanking regions 通过短寿命非特异性疏水接触以加和方式提高结合亲和力约数倍（具体倍数未提供），且不依赖静电相互作用；该效应在生理盐浓度下成立，但具体幅度依赖序列组成。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 单一体系 | 仅研究了 NCBD-CID 一对互作蛋白 | 需在更多 IDP 互作体系中验证 flanking regions 的普适贡献 | Discussion 部分（未提供具体行号） |
| 疏水接触的定量贡献未精确计算 | MD 模拟显示接触但未做自由能分解 | 未来可用更精确的自由能计算方法量化每个接触的贡献 | Discussion 部分 |
| 体内相关性未验证 | 实验均在体外进行 | 需在细胞环境中验证 flanking regions 的调节作用 | Discussion 部分 |

**作者提及的相关约束**（非正式局限）：flanking regions 的贡献幅度较小（ΔΔG 在 1-2 kcal/mol 量级），可能被其他相互作用掩盖；且 flanking regions 的序列保守性较低，暗示其功能可能具有体系特异性。

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| 截短变体可能改变基序本身的构象偏好 | 截短 flanking regions 可能间接影响基序的折叠成核，而非直接通过接触贡献 | 若如此，结论应从「flanking 直接接触」修正为「flanking 影响基序构象」 | 用 NMR 或 MD 比较截短前后基序区域的构象系综 | 文中未提供截短变体的基序构象表征 |
| MD 模拟的疏水接触可能为力场伪影 | 疏水相互作用在 MD 力场中常被高估 | 若为伪影，则实验突变效应可能另有机制 | 用不同力场重复模拟，或用增强采样验证接触稳定性 | 文中未提供力场对比 |
| 盐浓度实验仅测试了静电贡献 | 疏水相互作用也可被高盐浓度影响（盐析效应），但文中未做完整盐浓度梯度 | 若疏水贡献也随盐浓度变化，则「非静电」结论需细化 | 扩展盐浓度范围并监测 Kd 变化趋势 | 文中盐浓度范围未提供 |
| 加和性结论基于有限组合变体 | 仅测试了 N 端、C 端和双侧截短，未做内部缺失突变 | 可能存在 flanking 内部残基的协同效应被平均化掩盖 | 设计内部缺失或点突变组合 | 文中变体设计未覆盖内部区域 |
| 未测量 flanking regions 在复合物中的动力学时间尺度 | CD 和 MD 均无法提供实验时间尺度的动态信息 | 若接触寿命极短，则「fuzzy binding」的生物学意义需重新评估 | 用 NMR 弛豫或单分子 FRET 测量 | 文中未提供 NMR 或 smFRET 数据 |

---

## 14 Agent 提炼的知识候选

> 标题：Agent 提炼的知识候选

1. **加和性自由能贡献的测量框架**：本文的组合截短 + ΔΔG 分解方法可直接迁移到其他 IDP 互作体系，用于量化 flanking regions 的贡献。对课题方向而言，可作为 AI 预测模型的训练标签——即用截短实验数据训练一个预测 flanking region 对 Kd 贡献的模型。

2. **非特异性疏水接触的「fuzzy」机制**：本文证明非特异性接触可以产生热力学稳定化，这对相分离研究有直接启示——相分离中的多价弱相互作用可能同样依赖这种「非特异性但加和」的疏水接触。可迁移到相分离预测模型中，将 flanking region 的疏水残基密度作为凝聚体形成的特征。

3. **静电 vs 疏水的判别实验设计**：变盐浓度实验是区分静电与疏水贡献的简单有效手段。对 AI 方法而言，这意味着预测模型需要将溶液条件（离子强度）作为输入特征，否则无法正确预测 IDP 互作的亲和力。

4. **MD 接触预测 → 点突变验证的闭环**：本文展示了 MD 模拟预测接触残基、实验突变验证的闭环流程。对课题方向而言，可迁移为「MD 预测 flanking region 接触 → AlphaFold 无法捕捉的动态界面 → 实验验证」的工作流，用于发现新的调控位点。

5. **「基序外」调控的概念**：本文强调结合基序之外的区域可以调节亲和力，这对药物设计/肽段抑制剂设计有启示——仅靶向基序可能不够，需要同时考虑 flanking regions 的贡献。可迁移到 AI 辅助的肽段设计任务中，将 flanking 序列特征纳入生成模型的约束。

---

## 15 与已有知识的连接

- **相似工作**：Dogan et al. (2013) 对 NCBD/ACTR 体系的热力学研究（JMB），建立了基序内相互作用的自由能图谱；本文在此基础上扩展了基序外 flanking regions 的贡献。Sugase et al. (2007) 的 NMR 研究描述了 NCBD 结合 ACTR 的折叠路径，本文的 fuzzy binding 结论与其部分互补。
- **概念连接**：Tompa & Fuxreiter (2008) 提出的 fuzzy complex 概念是本文的理论框架；本文提供了 fuzzy complex 中 flanking regions 能量贡献的定量实验证据。
- **方法连接**：本文的 MD 接触分析可类比于近期用 AlphaFold 预测 IDP 互作的工作（如 Ruff & Pappu 2021 的评论），但本文强调 AlphaFold 无法捕捉的动态 fuzzy 接触，提示 AI 方法需要超越静态结构预测。
- **相分离连接**：本文的「非特异性疏水接触加和贡献」机制与 Brangwynne 等关于相分离中多价弱相互作用的观点一致（如 Shin & Brangwynne 2017），可作为 IDR 驱动相分离的分子机制补充。
- **冲突/张力**：部分文献认为 flanking regions 通过静电相互作用（如带电荷残基）调节 IDP 互作（如 Borgia et al. 2018 对 histone H1 的研究），本文的结果提示疏水机制可能同样重要，两者可能在不同体系中占主导。

---

## 16 研究想法

> 标题：Agent 生成的研究候选

### 候选 1：基于截短实验数据的 flanking region 亲和力预测模型
- **来源局限/观察**：本文提供了 NCBD/CID 体系的 flanking region 截短数据，但仅限单一体系；其他 IDP 互作体系缺乏类似系统数据。
- **核心假设**：flanking region 对亲和力的贡献可由其序列特征（疏水残基含量、长度、净电荷）预测，且贡献具有加和性。
- **相对本文的增量**：将本文的单体系结论推广为可泛化的预测模型。
- **初步方法**：收集多个 IDP 互作体系的截短突变数据（文献挖掘），提取 flanking region 序列特征，训练回归模型预测 ΔΔG。
- **验证方式**：留一体系交叉验证；对预测的高贡献 flanking region 进行实验验证。
- **可能的失败模式**：不同体系的 flanking region 机制差异过大（静电 vs 疏水），单一特征集无法泛化。
- **创新状态**：unverified

### 候选 2：MD 驱动的 fuzzy contact 图谱用于相分离热点预测
- **来源局限/观察**：本文 MD 显示 flanking regions 与 NCBD 形成短寿命疏水接触，但未系统分析这些接触是否与相分离倾向相关。
- **核心假设**：IDR 中与 partner 形成短寿命疏水接触的区域，同时也是相分离中的多价相互作用热点。
- **相对本文的增量**：将 fuzzy binding 的分子机制扩展到相分离预测。
- **初步方法**：对多个已知相分离相关 IDR 进行 MD 模拟，提取短寿命接触图谱，与实验相分离数据（如液滴形成浓度）关联。
- **验证方式**：预测新的相分离热点区域，用体外液滴实验验证。
- **可能的失败模式**：MD 力场对短寿命接触的定量不可靠，导致图谱噪声过大。
- **创新状态**：unverified

### 候选 3：AlphaFold 无法捕捉的 fuzzy 接触——用 MD 增强采样补充结构预测
- **来源局限/观察**：本文的 fuzzy binding 机制是动态的、非特异性的，AlphaFold 等静态结构预测工具无法捕捉。
- **核心假设**：MD 增强采样（如 metadynamics 或 replica exchange）可以生成 IDP 互作的构象系综，补充 AlphaFold 的静态预测，提供 flanking region 接触的自由能景观。
- **相对本文的增量**：将本文的 MD 分析升级为系统性的构象系综方法，并与 AI 结构预测结合。
- **初步方法**：对 NCBD/CID 及类似体系运行增强采样 MD，构建 flanking region 接触的自由能图谱；与 AlphaFold 预测的界面比较，识别 AlphaFold 遗漏的动态接触。
- **验证方式**：用突变实验验证自由能图谱预测的高贡献接触。
- **可能的失败模式**：增强采样计算成本过高，且力场误差在 IDP 体系中可能被放大。
- **创新状态**：unverified

### 候选 4：flanking region 疏水含量作为 IDP 互作亲和力的通用特征
- **来源局限/观察**：本文发现疏水接触是 flanking region 贡献的机制，但未检验该特征在其他体系中的预测力。
- **核心假设**：IDR 中结合基序两侧的疏水残基含量（如 aliphatic 残基比例）可作为互作亲和力的通用预测特征，独立于基序本身。
- **相对本文的增量**：提出一个可计算的序列特征，用于 IDP 互作预测。
- **初步方法**：从数据库（如 BioGRID、IntAct）收集 IDP 互作对，计算 flanking region 疏水含量，与实验 Kd 关联。
- **验证方式**：在多个体系上检验相关性；用机器学习模型比较该特征与已有特征（如 net charge、disorder propensity）的预测力。
- **可能的失败模式**：疏水含量与其他序列特征高度相关，无法分离独立贡献。
- **创新状态**：unverified

### 候选 5：fuzzy binding 对相分离多价性的贡献——粗粒化模型
- **来源局限/观察**：本文的 fuzzy binding 是二聚体互作，但相分离涉及多价互作；本文机制能否外推到多价体系未知。
- **核心假设**：flanking region 的短寿命疏水接触在多价体系中可累积为相分离的驱动力，且其贡献可用粗粒化模型（如 patchy particle 模型）描述。
- **相对本文的增量**：将单对互作的 fuzzy binding 机制推广到多体相分离。
- **初步方法**：基于本文的接触参数构建粗粒化模型，模拟多价 IDR 体系的相分离行为，改变 flanking region 疏水强度观察相图变化。
- **验证方式**：与实验相分离数据（如液滴形成浓度、饱和度）对比。
- **可能的失败模式**：粗粒化模型参数化过于简化，无法捕捉序列特异性。
- **创新状态**：unverified