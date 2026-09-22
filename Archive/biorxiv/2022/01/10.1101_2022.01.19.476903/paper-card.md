## 01 基本信息

- **标题**: Phase separation driven by interchangeable properties in the intrinsically disordered regions of protein paralogs
- **作者**: Shih-Hui Chiu; Wen-Lin Ho; Yung-Chen Sun; Jean-Cheng Kuo; Jie-rong Huang
- **单位**: 未提供（根据致谢推测为台湾阳明交通大学 NYCU 及中央研究院相关单位）
- **期刊/平台**: bioRxiv（预印本）
- **年份**: 2022
- **论文类型**: 预印本（未经同行评审）
- **领域**: 无序蛋白/无序区（IDP/IDR）、相分离（LLPS）、蛋白旁系同源物（paralogs）进化
- **关键词**: IDR、paralogs、phase separation、prion-like、α-helical propensity、Musashi
- **DOI/ID**: 10.1101/2022.01.19.476903
- **代码**: 未提供
- **数据**: BMRB 化学位移数据（accessions 51204–51208）；补充材料（序列、系统发育树等）
- **阅读日期**: 2026-05-09（按当前日期）
- **在该课题方向中的位置**: 本文属于「IDP/IDR × 蛋白互作 × 相分离」方向，核心贡献在于揭示旁系同源 IDR 可通过不同物理化学性质（prion-like vs α-helical propensity）的互换实现趋同的相分离功能。对 AI/深度学习方法的直接关联有限，但提供了 IDR 序列特征-相分离功能映射的实验基准，可作为 AI 预测模型的训练/验证数据来源。

## 02 一句话总结

以 RNA 结合蛋白 Musashi 家族为模型，通过系统发育分析、NMR、CD、显微成像和 FRAP 实验，证明旁系同源 IDR 中 prion-like 倾向与 α-helix 倾向可互换补偿，共同驱动液-液相分离（LLPS）功能。

## 03 研究问题

- **具体问题**: 旁系同源蛋白（paralogs）的 IDR 序列高度分化，但如何维持或趋同于相同的功能（如相分离）？
- **为什么重要**: 超过一半的真核蛋白含 IDR，但旁系同源 IDR 的功能进化机制几乎未被探索。理解 IDR 如何通过不同序列特征实现相同功能，对预测 IDR 功能、理解相分离的序列编码规则至关重要。
- **现有方法为何不足**: 已有研究多聚焦于单一蛋白的 IDR 序列-功能关系，缺乏对旁系同源 IDR 的系统比较；且多数研究仅关注 prion-like 或电荷模式等单一特征，未考虑多种物理化学性质的互补性。
- **精确研究问题**: Can paralogous IDRs with divergent sequences converge on the same phase separation function through interchangeable physicochemical properties (e.g., prion-likeness vs α-helical propensity)?

## 04 背景与发展脉络

*注：以下脉络为「仅本文框架」——基于本文引文和论述逻辑整理，未经外部系统核验。*

1. **基因复制与旁系同源功能分化（经典进化生物学）**: Ohno (1970) 提出基因复制产生旁系同源物，冗余拷贝可突变获得新功能（Wilson 1899）。代表：α/β-珠蛋白（Lodish et al.）。局限：主要关注折叠结构域，IDR 未纳入分析框架。
2. **IDR 与相分离的兴起（~2010s）**: IDR 占真核蛋白组 >50%（Uversky & Dunker 2010）。IDR 通过 multivalent interactions 驱动 LLPS，形成无膜细胞器（Alberti & Hyman 2021）。代表：FUS、TDP-43、hnRNPA1 等 RBPs 的 prion-like domain 研究（Kato et al. 2012; Molliex et al. 2015; Patel et al. 2015）。
3. **IDR 序列特征-相分离关系（~2015-2020）**: 芳香族残基数量/分布决定相分离行为（Martin et al. 2020）；α-helix 参与 TDP-43 自组装（Conicella et al. 2016; Li et al. 2018）。局限：多为单蛋白研究，缺乏进化视角。
4. **本文主张的位置**: 首次以旁系同源家族（Musashi）为系统，提出 IDR 的多种物理化学性质（prion-likeness、α-helicity）在进化中可互换补偿，实现趋同的 LLPS 功能。将进化生物学与相分离生物物理学连接。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 旁系同源 IDR 功能研究空白 | 旁系同源蛋白研究集中于折叠结构域，IDR 几乎未被系统比较 | IDR 无固定结构，传统序列比对/功能注释方法不适用 | Introduction 第 1-2 段 |
| IDR 序列高度分化但功能趋同 | Musashi-1 与 Musashi-2 的 IDR 氨基酸序列差异大，但都参与应激颗粒 | IDR 突变速率快，但功能约束可能通过不同物理化学特征实现 | Fig. 1A-D；Discussion 第 1 段 |
| 单一序列特征不足以解释相分离 | prion-like 倾向低的 Musashi-1 仍能形成凝聚体 | 其他特征（如 α-helical propensity）可补偿 prion-likeness 的不足 | Fig. 2C-D；Fig. 4 |
| 相分离与聚集的平衡难以控制 | Musashi-1 在 pH 6.5 下快速形成不可逆聚集体 | α-helix 促进组装的同时降低了 LLPS 与聚集态之间的能垒 | Fig. 4D-G；Discussion 第 2 段 |

## 06 核心思想

**1) 表面方法**: 以 Musashi 旁系同源家族为模型，结合系统发育分析（MEGA X）、序列特征预测（PONDR、PLAAC）、NMR 化学位移分配与二级结构预测（δ2D）、CD 光谱、光学显微镜和 FRAP 实验，比较 Musashi-1 与 Musashi-2 的 IDR 物理化学性质及其相分离行为。

**2) 核心洞察**: 旁系同源 IDR 的序列特征（prion-likeness、α-helical propensity）在进化中可互换补偿——Musashi-1 的 IDR 虽 prion-like 倾向低，但通过更强的 α-helix 倾向实现组装；Musashi-2 则相反。两种不同的物理化学"策略"趋同于相同的 LLPS 功能。这提示 IDR 功能并非由单一序列特征决定，而是多种特征的组合优化。

**3) 可能的普适教训** [Analysis]: 对 IDR 功能预测（如 AI 模型）而言，不能仅依赖单一序列特征（如 prion-like score），需考虑多种物理化学性质的组合与权衡。旁系同源 IDR 的比较分析可作为训练/验证 AI 模型的天然实验数据集——同一功能可由不同序列特征组合实现，这为模型提供了"功能趋同"的正样本。

## 07 方法总览

- **输入**: Musashi 家族旁系同源蛋白的氨基酸序列（来自 UniProt）；重组表达的 IDR 蛋白样品
- **输出**: 系统发育树；prion-likeness 与 α-helical propensity 的定量比较；相分离/聚集行为的实验表征
- **模块**:
  1. 序列分析与系统发育（PONDR、PLAAC、MEGA X）
  2. 蛋白表达纯化（E. coli 重组表达，C4 反相 HPLC 纯化）
  3. 结构表征（CD 光谱、NMR 化学位移分配与 δ2D 预测）
  4. 相分离/聚集实验（光学显微镜、FRAP、离心聚集实验）
- **训练**: 不适用（无机器学习模型）
- **工具**: PONDR、PLAAC、MEGA X、RaptorX、δ2D、NMRPipe、NMRFAM-Sparky
- **反馈回路**: 序列特征预测 → 实验验证（CD/NMR）→ 修正对 α-helix 倾向的估计 → 突变体设计（ΔSeq1/ΔSeq2/ΔSeqA）→ 功能验证
- **假设**: (1) IDR 的物理化学性质（而非具体序列）决定其相分离功能；(2) 旁系同源 IDR 的功能趋同可通过不同性质组合实现；(3) α-helical propensity 可用 NMR 化学位移和 δ2D 可靠估计

**文字流程**: 从 UniProt 获取 Musashi 同源序列 → 以折叠结构域（RRM）构建系统发育树 → 预测 IDR 边界与 prion-likeness → 比较旁系同源 IDR 的氨基酸组成与 prion 倾向 → 重组表达并纯化 IDR → CD 光谱确认无序性 → NMR 化学位移分配 → δ2D 预测残基级 α-helix 倾向 → 设计 ΔSeq1/ΔSeq2/ΔSeqA 突变体 → 显微镜观察凝聚体形态 → FRAP 测量动力学 → 离心聚集实验比较稳定性 → 综合序列进化与实验数据得出结论。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 系统发育分析（MEGA X） | 确定旁系同源关系与进化分支 | 确认 Musashi-1/2 为旁系同源物，追溯 IDR 分化时间 | 输入：全长序列；输出：系统发育树 | Fig. 1A | 无法确认旁系同源关系，后续比较失去进化框架 |
| prion-likeness 预测（PLAAC） | 量化 IDR 的 prion-like 倾向 | 识别 Musashi-2 与 Musashi-1 在 prion 倾向上的差异 | 输入：IDR 序列；输出：prion-like score | Fig. 1A-D | 无法发现旁系同源 IDR 在 prion 倾向上的分化 |
| NMR 化学位移分配与 δ2D | 残基级二级结构倾向预测 | 定量比较 Musashi-1/2 的 α-helix 倾向差异 | 输入：NMR 化学位移；输出：α-helix 倾向值 | Fig. 2C-D | 无法证明 α-helix 倾向的差异是序列特异性的 |
| 突变体设计（ΔSeq1/ΔSeq2/ΔSeqA） | 验证非保守序列对 α-helix 倾向和组装的影响 | 确定哪些序列区域调控 α-helix 倾向 | 输入：野生型 IDR 序列；输出：突变体蛋白 | Fig. 3B-G | 无法将 α-helix 倾向差异定位到具体序列区域 |
| 相分离/聚集实验（显微镜+FRAP+离心） | 表征凝聚体形成和动力学 | 验证 α-helix 倾向差异是否影响 LLPS 和聚集行为 | 输入：纯化蛋白；输出：凝聚体图像、FRAP 曲线、聚集时间曲线 | Fig. 4D-F | 无法将序列特征与相分离功能直接关联 |
| 蛋白质组范围 α-helix 倾向扫描 | 评估 α-helix 倾向在 RBPs 中的普遍性 | 将 Musashi 案例推广到更广泛的 RBPs | 输入：人类蛋白质组序列；输出：RBPs 中 α-helix 倾向的统计分布 | Fig. 5C | 无法支持 α-helix 倾向是 RBPs 相分离的普遍机制 |

## 09 关键公式符号

本文为实验生物学论文，无核心数学公式。以下为隐含的定量关系：

- **二级化学位移 (Secondary Chemical Shift)**:
  \[
  \Delta\delta = \delta_{\text{measured}} - \delta_{\text{random coil}}
  \]
  其中 \(\delta_{\text{measured}}\) 为实测化学位移，\(\delta_{\text{random coil}}\) 为随机卷曲参考值。正值（Cα、C'）与负值（Cβ）指示 α-helix 倾向。来源：Fig. 2C。

- **δ2D 预测的 α-helix 群体 (Helical Population)**:
  \[
  P_{\alpha} = f(\Delta\delta C\alpha, \Delta\delta C\beta, \Delta\delta C')
  \]
  由 δ2D 程序（Camilloni et al. 2012）基于化学位移组合预测残基级 α-helix 群体。来源：Fig. 2D。

- **prion-like score**: 由 PLAAC 算法（Lancaster et al. 2014）基于氨基酸组成计算的 prion 倾向得分。来源：Fig. 1A。

## 10 实验设计与证据链

**数据集/群体**: Musashi 家族旁系同源序列（人类、小鼠、鸡、斑马鱼、果蝇、线虫、文昌鱼等）；人类蛋白质组（UniProtKB 2021_01，20396 条序列）
**规模**: 系统发育分析覆盖多个物种；实验表征聚焦人类 Musashi-1/2 的 IDR（Msi-1C: 残基 237–362；Msi-2C: 残基 235–328）
**指标**: prion-like score（PLAAC）、α-helix 群体（δ2D）、CD 摩尔椭圆率、FRAP 恢复率、可溶性蛋白比例（聚集实验）
**基线**: 无明确基线，以野生型 Msi-1C 为参照比较突变体
**预算**: 未提供
**骨干/仪器**: Bruker AVIII 600 MHz NMR 光谱仪（低温探头）、AVIV model 410 圆二色光谱仪、Olympus BX51 光学显微镜、iLas 多模态 TIRF/转盘共聚焦显微镜
**oracle 输入**: 不适用（无 AI 模型）
**评测协议**: 每个实验重复三次；NMR 化学位移分配使用标准三共振实验；FRAP 在凝聚体上进行多点测量

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 系统发育分析 | Musashi-1/2 为旁系同源，IDR 序列分化 | 多物种序列比对，邻接法建树 | 脊椎动物有两个旁系同源，IDR 序列差异大 | 旁系同源 IDR 序列高度分化 | 无法确定分化速率或选择压力 | Fig. 1A |
| PLAAC 预测 | Musashi-2 比 Musashi-1 更 prion-like | 人类 Musashi-1/2 IDR 的 PLAAC score | Musashi-2 的 prion-like score 显著高于 Musashi-1 | 旁系同源 IDR 的 prion 倾向不同 | 未验证 prion-like 与相分离的因果关系 | Fig. 1A-D |
| NMR 化学位移 + δ2D | Msi-1C 的 α-helix 倾向高于 Msi-2C | 比较 Msi-1C 与 Msi-2C 的残基级 α-helix 群体 | Msi-1C 的 α-helix 群体最高达 ~50%，Msi-2C 仅 ~20% | α-helix 倾向差异是序列特异的 | 未直接证明 α-helix 驱动相分离 | Fig. 2C-D |
| 突变体（ΔSeq1/ΔSeq2） | 非保守序列调控 α-helix 倾向 | 比较野生型与突变体的 δ2D 预测 | ΔSeq1 的 α-helix 倾向比野生型高 ~6%，ΔSeq2 低 ~5% | 侧翼序列微调 α-helix 倾向 | 未检测突变体的相分离行为 | Fig. 3F-G |
| 显微镜 + FRAP | 所有构建体均形成动态凝聚体 | pH 5.5 和 6.5 条件下观察 | 所有构建体形成球形凝聚体，FRAP 显示动态恢复 | IDR 具备相分离能力 | FRAP 恢复率变异大，未定量比较 | Fig. 4D-E |
| 聚集实验 | Msi-1C 的 α-helix 促进聚集 | pH 6.5 下比较野生型与 ΔSeqA 的可溶性 | Msi-1C 在 1 小时内几乎完全聚集，ΔSeqA 保持可溶更久 | α-helix 区域促进组装和聚集 | 未区分 LLPS 与不可逆聚集的贡献 | Fig. 4F |
| 蛋白质组扫描 | α-helix 倾向在 RBPs 中富集 | 人类蛋白质组中 RBPs vs 非 RBPs 的 α-helix score 分布 | RBPs 中高 α-helix score 的 IDR 比例更高 | α-helix 倾向可能是 RBPs 相分离的普遍特征 | 仅为统计关联，未实验验证 | Fig. 5C |

## 11 结论正确解读

- **任务范围**: 本文仅研究 Musashi 家族两个旁系同源 IDR 的物理化学性质与相分离行为，未覆盖其他旁系同源家族。
- **oracle/真值输入**: 无 AI 模型，实验数据为直接测量（NMR、CD、显微镜）。
- **端到端状态**: 非端到端——序列特征预测（PLAAC、δ2D）与实验验证分离进行，未建立定量预测模型。
- **算力成本**: 不适用。
- **历史数据依赖**: 依赖 UniProt 序列数据库和已有 RBP 注释（Gerstberger et al. 2014），未使用时间序列数据。
- **模型依赖**: 不适用。
- **最难情形**: pH 6.5 下 Msi-1C 的快速不可逆聚集使 FRAP 测量不可靠（作者明确说明）；凝聚体大小和形态的定量比较未系统进行。
- **群体/领域边界**: 结论限于 Musashi 家族及 RBPs 的 IDR；是否适用于其他 IDP 家族未知。
- **不确定性**: 作者未提供统计显著性检验（如 p 值）或效应量；δ2D 预测的 α-helix 群体为间接推断，未用分子动力学模拟或晶体结构验证。

**有边界的复述**: 在 Musashi 旁系同源家族中，IDR 的 prion-likeness 与 α-helical propensity 呈负相关补偿关系，两种性质均可独立驱动 LLPS 组装；该模式在 RBPs 中可能普遍存在，但需更多家族验证。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 未直接证明 α-helix 驱动相分离的分子机制 | 仅通过突变体间接推断 α-helix 的作用 | 未明确提及 | Discussion 第 2 段（隐含） |
| 未定量比较不同构建体的相分离能力 | FRAP 恢复率变异大，未给出定量比较 | 未明确提及 | Fig. 4E 图注（隐含） |
| 蛋白质组扫描仅为统计关联 | 未实验验证 RBPs 中 α-helix 倾向与相分离的因果关系 | 未明确提及 | Fig. 5C 相关讨论 |
| 未研究全长蛋白的相分离行为 | 实验使用分离的 IDR 构建体，未包含 RRM 结构域 | 未明确提及 | Methods（隐含） |

*注：作者在 Discussion 中未以"limitations"形式系统列出局限，以上为从文中推断的隐含局限。*

**作者提及的相关约束**（非正式局限）:
- Msi-1C 在 pH 6.5 下快速聚集，限制了 FRAP 测量的可靠性（Fig. 4E 图注）
- 实验条件（pH 5.5/6.5）为体外优化条件，与细胞内环境（如分子拥挤、其他互作蛋白）有差异

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| α-helix 倾向差异仅基于 NMR 化学位移和 δ2D 预测 | δ2D 为统计预测工具，可能高估短 IDR 的 α-helix 群体；未用 CD 定量或 MD 模拟验证 | 核心结论依赖 α-helix 倾向的准确估计 | 使用 CD 光谱定量 α-helix 含量；或进行增强采样 MD 模拟验证 | Fig. 2C-D；Methods |
| 突变体实验仅改变侧翼序列，未直接突变 α-helix 核心残基 | 观察到的相分离差异可能由其他因素（如疏水性、电荷）而非 α-helix 变化引起 | 无法排除混杂变量 | 设计点突变直接破坏 α-helix 核心（如脯氨酸插入） | Fig. 3B-G |
| 相分离实验仅使用分离的 IDR，未包含 RRM 或全长蛋白 | 全长蛋白中 RRM 可能通过 RNA 结合影响相分离，IDR 单独行为不能代表生理状态 | 结论可能过度简化 | 重复实验使用全长 Musashi-1/2 或包含 RRM 的构建体 | Methods |
| 蛋白质组扫描的 α-helix score 阈值（1.5/2.0/2.5）为任意选择 | 不同阈值可能改变 RBPs 富集结论 | 统计稳健性存疑 | 进行敏感性分析，测试不同阈值 | Fig. 5C |
| 未检测 RNA 对相分离的影响 | Musashi 为 RNA 结合蛋白，RNA 可能显著调节 LLPS | 生理条件下 RNA 是重要调控因子 | 在相分离实验中添加 RNA 并比较 | Introduction（RBP 背景） |
| 系统发育分析未包含足够古老物种 | 文昌鱼为最古老样本，无法确定旁系同源分化的精确时间 | 进化时间线不完整 | 扩展至更广泛的无脊椎动物物种 | Fig. 1A；Fig. 6A-C |

## 14 Agent 提炼的知识候选

**可迁移概念**:

1. **IDR 功能趋同的"性质互换"原则**: 旁系同源 IDR 可通过不同物理化学性质（prion-likeness vs α-helical propensity）实现相同功能。对本课题（IDP/IDR × 蛋白互作 × AI）的启示: AI 模型预测 IDR 功能时，不应仅依赖单一序列特征，而应学习多种特征的组合空间。可设计多任务学习框架，同时预测 prion-likeness、α-helical propensity、电荷模式等多个物理化学性质，再综合判断相分离能力。

2. **α-helical propensity 作为相分离的独立预测因子**: 本文证明 α-helix 倾向可独立于 prion-likeness 驱动组装。对本课题的启示: 现有相分离预测工具（如 catGRANULE、PhaSepDB）多基于电荷/疏水性/prion-like 特征，可考虑将 α-helical propensity（可用 SPIDER3、PSSpred 等工具预测）作为新增特征维度。

3. **旁系同源 IDR 作为天然"功能趋同"数据集**: Musashi-1/2 的 IDR 序列差异大但功能相同，这类旁系同源对可作为 AI 模型的正样本对，用于训练"序列-功能"映射的鲁棒性——模型应能从不同序列中识别相同功能。

**可迁移方法**:

1. **NMR 化学位移 + δ2D 的残基级 α-helix 倾向定量**: 该方法可推广到其他 IDR 的相分离研究，为 AI 模型提供高分辨率的实验标签（残基级 α-helix 群体），优于仅使用整体 CD 光谱。

2. **突变体设计策略（ΔSeq1/ΔSeq2/ΔSeqA）**: 通过删除非保守侧翼序列来微调 α-helix 倾向，这种"序列微扰-功能响应"的实验设计可用于生成 AI 模型的训练数据（序列变异 → 相分离行为变化）。

3. **系统发育 + 生物物理联合分析框架**: 将进化树与物理化学性质比较结合，可推广到其他旁系同源家族的 IDR 功能研究，为 AI 模型提供进化背景特征。

**可迁移公式/评分函数**:

1. **α-helix 倾向评分函数**（Fig. 5A 的简化版）: 基于氨基酸 α-helix 倾向值（Levitt 1978; Pace & Scholtz 1998）的滑动窗口聚合评分。可迁移为 AI 模型的特征工程——将序列编码为 α-helix 倾向谱，作为相分离预测的输入特征。

2. **二级化学位移组合**（ΔδCα - ΔδCβ）: 该组合最小化化学位移参考误差，可作为 IDR 局部结构倾向的实验标签，用于训练残基级结构预测模型。

## 15 与已有知识连接

- **相似研究**: 
  - Martin et al. (2020) 关于芳香族残基模式决定相分离行为的研究——本文补充了 α-helix 作为另一独立特征维度。
  - Conicella et al. (2016) 和 Li et al. (2018) 关于 TDP-43 α-helix 介导自组装的研究——本文将其推广到旁系同源进化框架。
  - Molliex et al. (2015) 和 Patel et al. (2015) 关于 prion-like domain 驱动 LLPS 的研究——本文显示 prion-likeness 并非唯一途径。

- **冲突/补充**: 
  - 与"prion-like domain 是相分离主要驱动因素"的主流观点形成补充——本文显示 α-helix 可独立驱动组装，提示相分离的序列编码具有多重冗余性。

- **可连接的外部资源**:
  - PLAAG 算法（Lancaster et al. 2014）: 本文使用的 prion-likeness 预测工具，可迁移到其他 IDR 分析。
  - PONDR（Obradovic et al. 2005）: 无序区预测工具，与 AI 方法（如 AlphaFold 的 pLDDT）可互补。
  - BMRB accessions 51204–51208: 本文沉积的化学位移数据，可用于训练 IDR 结构预测模型。
  - UniProtKB 人类蛋白质组: 本文的 α-helix 倾向扫描数据集，可复用于其他分析。

- **候选方向** [Analysis]: 
  - 将本文的"性质互换"原则形式化为 AI 可学习的约束——例如，在相分离预测模型中引入"多特征冗余"正则化，使模型不依赖单一特征。
  - 利用旁系同源 IDR 对作为数据增强策略——将已知相分离蛋白的旁系同源 IDR 作为正样本，扩大训练集。

## 16 Agent 生成的研究候选

**候选 1: 基于多物理化学特征融合的 IDR 相分离预测模型**
- **来源局限/观察**: 本文证明 prion-likeness 与 α-helical propensity 可互换补偿，现有预测工具多依赖单一特征。
- **核心假设**: 融合 prion-likeness、α-helical propensity、电荷模式、疏水性等多特征的深度学习模型，可更准确预测 IDR 相分离能力。
- **初步方法**: 使用本文的 Musashi 数据 + 已知相分离蛋白数据库（PhaSepDB、LLPSDB）作为训练集；特征编码采用滑动窗口聚合 + 残基级预测（如 SPIDER3 的 α-helix 概率）；模型架构可采用注意力机制捕捉长程序列依赖。
- **验证方式**: 在留出测试集上比较与 catGRANULE、PhaSepPred 的 AUC；用本文的突变体数据（ΔSeq1/ΔSeq2/ΔSeqA）作为外部验证。
- **可能的失败模式**: 训练数据不足导致过拟合；α-helix 预测误差传播；相分离的多因素决定论使单一模型难以泛化。
- **创新状态**: unverified

**候选 2: 旁系同源 IDR 功能趋同的对比学习框架**
- **来源局限/观察**: 本文提供旁系同源 IDR 功能趋同的实验证据，但未利用此结构进行预测。
- **核心假设**: 旁系同源 IDR 对（功能相同、序列不同）可作为对比学习的正样本对，学习"功能等价"的序列嵌入。
- **初步方法**: 收集旁系同源 IDR 对（从 OrthoMCL 或 Ensembl Compara 获取）；使用对比学习（如 SimCLR 风格）训练序列编码器，使功能趋同的 IDR 对在嵌入空间中接近；下游任务为相分离能力预测。
- **验证方式**: 在已知相分离蛋白上测试嵌入的判别能力；与基于序列相似性的基线比较。
- **可能的失败模式**: 旁系同源 IDR 对数量有限；功能趋同的定义模糊（如何确定"相同功能"）；对比学习需要大量数据。
- **创新状态**: unverified

**候选 3: α-helix 介导的 IDR 组装机制的粗粒化 MD 模拟**
- **来源局限/观察**: 本文实验表明 α-helix 促进组装，但未提供分子机制。
- **核心假设**: α-helix 通过增强链内/链间疏水接触驱动 LLPS，而非仅通过螺旋-螺旋相互作用。
- **初步方法**: 使用粗粒化模型（如 MARTINI 或 HPS 模型）模拟 Musashi-1/2 IDR 的相分离；参数化 α-helix 倾向作为偏置势；比较野生型与突变体的相图。
- **验证方式**: 模拟预测的相分离温度/浓度与实验观察（Fig. 4）对比；突变体模拟重现实验差异。
- **可能的失败模式**: 粗粒化模型对 α-helix 的描述精度不足；IDR 的构象系综采样困难；计算成本高。
- **创新状态**: unverified

**候选 4: 基于 AlphaFold 的 IDR 结构预测与相分离倾向的关联分析**
- **来源局限/观察**: 本文使用 NMR 实验测定 α-helix 倾向，但 AlphaFold 对 IDR 的预测置信度低，尚未系统评估其与相分离的关系。
- **核心假设**: AlphaFold 的 pLDDT 和 PAE 可提供 IDR 的残余结构信息，与实验测定的 α-helix 倾向相关，可用于相分离预测。
- **初步方法**: 对 Musashi 家族及已知相分离蛋白运行 AlphaFold；提取 IDR 区域的 pLDDT 分布、预测的二级结构；与实验 α-helix 倾向（本文 NMR 数据）和相分离行为关联。
- **验证方式**: 统计 pLDDT 与 δ2D 预测的 α-helix 群体的相关性；在独立数据集上测试预测能力。
- **可能的失败模式**: AlphaFold 对 IDR 的预测不可靠；pLDDT 与 α-helix 倾向无直接对应；样本量不足。
- **创新状态**: unverified

**候选 5: IDR 旁系同源进化的序列-功能映射数据库**
- **来源局限/观察**: 本文仅研究一个家族，但提出"性质互换"可能普遍存在。
- **核心假设**: 多个旁系同源 IDR 家族中均存在 prion-likeness 与 α-helical propensity 的负相关补偿。
- **初步方法**: 从 OrthoMCL 获取旁系同源家族；对 IDR 区域计算 prion-likeness（PLAAC）、α-helix 倾向（δ2D 或 SPIDER3）、电荷模式等特征；统计家族内特征补偿模式。
- **验证方式**: 在多个家族中检验负相关显著性；选择代表性家族进行实验验证（如显微镜观察）。
- **可能的失败模式**: 旁系同源 IDR 注释不完整；特征计算误差；补偿模式可能仅存在于特定家族。
- **创新状态**: unverified