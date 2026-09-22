## 01 基本信息

- **标题**：Membrane Interactions of the Peroxisomal Proteins PEX5 and PEX14
- **作者与单位**：Gaussmann, Stefan; Gopalswamy, Mohanraj; Eberhardt, Maike; Reuter, Maren; Zou, Peijian; Schliebs, Wolfgang; Erdmann, Ralf; Sattler, Michael（Institute of Structural Biology, Helmholtz Zentrum München; 等）
- **期刊/预印本平台**：Frontiers in Cell and Developmental Biology
- **年份**：2021
- **论文类型**：实验研究（in vitro 生物物理与结构生物学）
- **领域**：过氧化物酶体蛋白转运；膜蛋白互作；IDP 构象与膜结合
- **关键词**：PEX5, PEX14, intrinsically disordered protein, membrane interaction, NMR spectroscopy, bicelles, nanodiscs, peroxisome translocon
- **DOI/arXiv 号**：10.3389/fcell.2021.651449
- **代码**：未提供
- **数据**：原始数据可向作者索取（Data Availability Statement）
- **阅读日期**：2026-05-12
- **在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**：本文是 IDP（PEX5 NTD）与膜表面及膜蛋白（PEX14 NTD）互作的实验表征工作，不涉及 AI 或计算方法，但提供了 IDP 膜结合与蛋白互作竞争关系的定量热力学数据，可作为 AI/物理模拟方法（如 MD 膜结合模拟、IDP 构象预测）的验证基准与训练数据来源。

## 02 一句话总结

本文通过 NMR 和 ITC 实验表征了过氧化物酶体转运受体 PEX5 的无序 N 端结构域（NTD）与膜模拟物（bicelles）及膜蛋白 PEX14 NTD 的相互作用，发现 PEX5 NTD 中多个两亲性 α-螺旋区域（含 WF 基序）介导弱微摩尔级膜结合，且膜的存在不显著改变 PEX5-PEX14 的结合亲和力（KD 从 147 nM 变为 260 nM），表明二者互作在膜表面可正常进行。

## 03 研究问题

- **具体问题**：PEX5 的无序 N 端结构域（NTD）如何与过氧化物酶体膜相互作用？PEX5 NTD 与 PEX14 NTD 的互作在膜存在时是否受影响？
- **为什么重要**：PEX5-PEX14 互作是过氧化物酶体蛋白转运（translocon）的起始步骤，但 PEX5 无跨膜结构域，其如何被招募到膜上并完成 cargo 释放的机制尚不清楚。
- **现有方法为何不足**：此前研究主要关注 PEX5-PEX14 在溶液中的互作（晶体结构、ITC），缺乏对膜环境影响的系统表征；PEX5 的膜结合能力及其与 PEX14 结合的竞争关系未被定量研究。
- **精确的「Can ... ?」研究问题**：Can the intrinsically disordered N-terminal domain of PEX5 directly interact with lipid membranes, and does this membrane interaction modulate its binding to PEX14?

## 04 背景与发展脉络

**脉络标注**：仅本文框架（基于本文引言的叙述，未经外部系统核验）

1. **过氧化物酶体蛋白转运模型建立阶段**（~1990s-2000s）：鉴定 PEX5 为可溶性 cargo 受体，PEX14 为膜对接蛋白；提出「受体循环」模型（Dodt & Gould, 1996; Dammai & Subramani, 2001）。
2. **PEX5-PEX14 互作结构解析阶段**（~2009-2016）：晶体/NMR 结构揭示 PEX5 NTD 的 WF 基序（WxxxF/Y）插入 PEX14 NTD 的疏水沟槽（Neufeld et al., 2009; Neuhaus et al., 2014）；ITC 显示纳摩尔级亲和力。
3. **IDP 构象与膜结合研究阶段**（~2016-2021）：PEX5 NTD 被确认为 intrinsically disordered（Emmanouilidis et al., 2016），但其膜结合能力未被系统研究。
4. **本文位置**：首次系统表征 PEX5 NTD 与 PEX14 NTD 的膜结合特性，提出「弱膜结合 + 强蛋白互作」的协同模型，填补了从溶液互作到膜表面互作之间的空白。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| PEX5 无跨膜结构域却需在膜上工作 | PEX5 是 soluble receptor，但需在膜表面完成 cargo 释放 | PEX5 NTD 含有多个两亲性 α-螺旋区域，可弱结合膜表面 | Results 节「PEX5 NTD Interacts With Membranes」；图 1D-E |
| PEX5 NTD 的 IDP 特性导致构象异质 | NMR 谱峰重叠严重，难以进行残基级分析 | IDP 的构象 ensemble 导致化学位移分散差 | Results 节「Conformational Analysis of the PEX5 NTD by NMR Spectroscopy」；图 1A |
| 膜模拟物选择困难 | 传统脂质体不适合溶液 NMR；bicelles 尺寸小但曲率高 | 使用 DMPC/D7PC bicelles（q=0.2）兼顾 NMR 分辨率和膜环境代表性 | Methods 节「Bicelles and Nanodiscs Preparation」 |
| PEX14 NTD 膜结合位点与 PEX5 结合位点重叠 | PEX14 NTD 的膜结合表面与 WF 基序结合沟槽部分重叠 | 膜结合与蛋白互作存在潜在竞争 | Results 节「PEX14 NTD Interaction With Membranes」；图 4C-G |
| 膜结合亲和力弱，难以定量 | 微摩尔级 KD 需要高浓度蛋白和脂质 | 使用 NMR 滴定和 ITC 联合定量 | Results 节；表 1、表 2 |

## 06 核心思想

### 1) 表面方法
用 NMR（化学位移扰动、二级化学位移、hetNOE）和 ITC 表征 PEX5 NTD 三个亚片段（1-113、110-230、228-315）及 PEX14 NTD（1-104、16-80）在有无 bicelles 时的构象变化和结合亲和力；用 nanodiscs 验证 PEX14 跨膜构象下的 NTD 膜结合。

### 2) 核心洞察
PEX5 NTD 的膜结合主要由 C 端区域（228-315，含 W5/W6/W7）介导，该区域在溶液中已有部分 α-螺旋倾向，膜结合进一步稳定螺旋构象。PEX14 NTD 的膜结合表面与 PEX5 结合位点部分重叠，但 PEX5 的 WF 基序结合亲和力远强于膜结合，因此膜的存在不显著削弱 PEX5-PEX14 互作。**膜的作用是「定位」而非「变构调节」**——将 PEX5 富集在膜表面，但不改变其与 PEX14 的结合模式。

### 3) 可能的普适教训 [Analysis]
- IDP 的膜结合往往由多个弱亲和力位点协同贡献，单个位点突变不足以完全消除膜结合——这对设计膜结合抑制剂有启示。
- 弱互作（μM 级膜结合）与强互作（nM 级蛋白互作）的共存可通过「熵补偿」实现：膜结合预组织螺旋构象，降低蛋白互作时的熵代价。
- 对 IDP-膜互作的定量研究，bicelles + NMR 滴定是有效组合，但需注意 bicelles 的高曲率可能高估或低估真实膜亲和力。

## 07 方法总览

- **输入**：重组表达的人源 PEX5 NTD 亚片段（1-113、110-230、228-315、1-315）和 PEX14 NTD 片段（1-104、16-80、1-137），以及 DMPC/D7PC bicelles、DMPC/DMPG nanodiscs。
- **输出**：残基级化学位移归属、二级结构倾向、膜结合位点图谱、结合亲和力（KD、KDapp）、热力学参数（ΔH、ΔS、ΔG）。
- **模块**：
  1. 蛋白表达与纯化（大肠杆菌体系，含同位素标记）
  2. 膜模拟物制备（bicelles、nanodiscs）
  3. NMR 波谱学（主链归属、CSP 分析、hetNOE、二级化学位移）
  4. ITC 热力学测量
  5. 浮选实验（liposome binding 验证）
  6. CD 光谱（构象稳定性验证）
- **训练**：不适用（无机器学习/统计模型）
- **反馈回路**：NMR 滴定结果指导 ITC 实验设计（选择饱和浓度）；浮选实验验证 NMR 膜结合结论。
- **文字流程**：表达纯化各 PEX 片段 → 在无膜条件下进行 NMR 主链归属和构象分析 → 逐步加入 bicelles 记录 CSP 和 hetNOE 变化 → 拟合 KD → 对 PEX14 进行同样滴定 → 在 bicelles 存在下进行 PEX5-PEX14 ITC 滴定 → 用 nanodiscs 验证 PEX14 跨膜构象下的行为 → 浮选实验确认脂质结合特异性。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| PEX5 NTD 亚片段设计 | 将 315 残基 IDP 分为 3 个可操作片段 | 全长 IDP 的 NMR 谱重叠严重，无法进行残基级分析 | 输入：全长序列；输出：1-113、110-230、228-315 | Results 图 1A；Methods「Molecular Cloning」 | 预期影响：无法获得残基级膜结合位点信息 [预期效应] |
| Bicelles 膜模拟系统 | 提供可溶、NMR 友好的膜环境 | 脂质体太大导致 NMR 谱线过宽；bicelles 各向同性旋转 | 输入：DMPC/D7PC 脂质；输出：q=0.2 的 bicelles 溶液 | Methods「Bicelles and Nanodiscs Preparation」 | 预期影响：无法在溶液 NMR 中研究膜结合 [预期效应] |
| NMR CSP 分析 | 鉴定膜结合残基 | 化学位移变化反映局部环境改变 | 输入：有无 bicelles 的 2D 谱；输出：Δδavg 图谱 | Results 图 1E、2A-B、4C | 实测影响：C 端区域（228-315）CSP 最大，被鉴定为主要膜结合区 [实测消融效应] |
| hetNOE 实验 | 评估主链柔性 | 区分刚性螺旋与柔性 loop | 输入：饱和/非饱和实验谱；输出：残基级 NOE 值 | Results 图 1B | 预期影响：无法区分构象稳定性差异 [预期效应] |
| ITC 结合实验 | 定量 PEX5-PEX14 亲和力及热力学 | 提供 KD、ΔH、ΔS 等热力学参数 | 输入：PEX5 1-315 与 PEX14 1-104；输出：结合等温线 | Results 图 5；表 2 | 实测影响：bicelles 存在时 KD 从 147 nM 变为 260 nM，但仍在同一数量级 [实测消融效应] |
| Nanodiscs 验证 | 检验 PEX14 跨膜构象下的 NTD 行为 | PEX14 是膜蛋白，bicelles 不能完全模拟跨膜环境 | 输入：PEX14 1-137 + MSP1D1Δ5；输出：nanodisc 重构蛋白的 NMR 谱 | Results 图 4B；Methods「Nanodiscs」 | 预期影响：无法确认 NTD 在真实膜环境中的行为 [预期效应] |
| 浮选实验 | 验证脂质结合特异性 | 排除非特异性聚集 | 输入：PEX5 全长 + 脂质体；输出：浮选分级 | Results 补充图 2A-B | 预期影响：无法区分特异与非特异结合 [预期效应] |

## 09 关键公式符号

1. **化学位移扰动（CSP）**：
   Δδavg = [(ΔδH)² + (ΔδN/6.3)²]^0.5
   - ΔδH：¹H 化学位移变化（ppm）
   - ΔδN：¹⁵N 化学位移变化（ppm）
   - 6.3：¹⁵N 与 ¹H 化学位移尺度的归一化因子
   - 用途：鉴定膜结合残基；来源：Results 节

2. **NMR 滴定结合等温线拟合**：
   Δδ = Δδmax/(2[Pt]) × {[L] + [Pt] + KD − (([L] + [Pt] + KD)² − 4[Pt][L])^0.5}
   - Δδ：观测化学位移变化
   - Δδmax：最大化学位移变化
   - [Pt]：总蛋白浓度
   - [L]：配体（DMPC）浓度
   - KD：解离常数
   - 用途：拟合膜结合亲和力；来源：Methods 节「NMR Spectroscopy」

3. **ITC 热力学关系**：
   ΔG = ΔH − TΔS
   - ΔG：吉布斯自由能变化（-9.3 kcal/mol 无膜；-8.9 kcal/mol 有膜）
   - ΔH：结合焓变（-147.0 kcal/mol 无膜；-92.0 kcal/mol 有膜）
   - TΔS：熵贡献（137.7 kcal/mol 无膜；83.0 kcal/mol 有膜）
   - 用途：解析结合驱动力；来源：Results 节「PEX5 PEX14 Interaction in the Presence of Lipids」；表 2

4. **Bicelles 尺寸计算**（用于浓度换算）：
   未提供具体公式，但 bicelles 浓度基于 DMPC 分子数/盘计算（每盘约 46 个 DMPC 分子）
   - 来源：Methods 节「Bicelles and Nanodiscs Preparation」

## 10 实验设计与证据链

**数据集/群体**：
- PEX5 NTD 亚片段：1-113、110-230、228-315、1-315（人源，重组表达）
- PEX14 NTD 片段：1-104、16-80（含 C 端 Trp 突变体 16-80W）、1-137（含跨膜区）
- 膜模拟物：DMPC/D7PC bicelles（q=0.2）、DMPC/DMPC nanodiscs（6-8 nm）、DMPC/DOPC 脂质体

**指标**：CSP（Δδavg）、hetNOE 值、二级化学位移、KD、KDapp、ΔH、ΔS、ΔG、浮选百分比

**基线/对照**：
- 无关 RNA 结合结构域作为膜结合阴性对照（补充图 3E）
- 无 bicelles 条件下的 PEX5-PEX14 ITC 作为基线

**预算/资源**：未提供（学术实验室常规经费）

**骨干/仪器**：Bruker Avance III NMR 谱仪（500-950 MHz）、MicroCal PEAQ-ITC 量热仪、Jasco J-810 圆二色谱仪

**Oracle 输入**：不适用（无计算方法）

**评测协议**：NMR 滴定逐步增加 bicelles 浓度至饱和；ITC 为 triplicate 测量；浮选实验为 3 次独立重复

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|------------------|------|
| PEX5 NTD 亚片段 NMR 归属 | IDP 构象异质性可被亚片段化克服 | 3 个亚片段 vs 全长 | 亚片段谱图分散良好，可进行残基级分析 | 亚片段忠实反映全长构象 | 亚片段间可能的相互作用被忽略 | Results 图 1A |
| Bicelles 滴定 PEX5 亚片段 | PEX5 NTD 与膜直接互作 | 0→0.9 mM bicelles | C 端片段（228-315）CSP 最大，KDapp=20±7 μM | PEX5 NTD 的 C 端区域是主要膜结合区 | 膜结合是否具有脂质组成特异性 | Results 图 1D-E、2A-D；表 1 |
| HetNOE 比较 | 膜结合稳定螺旋构象 | 无膜 vs 有膜 | W5/W6 区域 hetNOE 值升高 | 膜结合诱导/稳定 α-螺旋 | 螺旋稳定化的功能意义 | Results 图 1B |
| PEX14 NTD bicelles 滴定 | PEX14 NTD 有内在膜亲和力 | 16-80W + bicelles | 弱 CSP，KDapp 为 μM 级 | PEX14 NTD 弱结合膜 | 膜结合是否依赖特定脂质头基 | Results 图 4A；补充图 3 |
| PEX14 1-137 nanodiscs | 跨膜锚定影响 NTD 膜结合 | 1-137 + nanodiscs vs 1-104 + bicelles | 相似 CSP 模式 | NTD 膜结合不依赖跨膜区 | 跨膜区对 NTD 取向的影响 | Results 图 4B-C |
| ITC 无膜 vs 有膜 | 膜不显著改变 PEX5-PEX14 亲和力 | 无 bicelles vs 44 μM bicelles | KD: 147→260 nM；ΔH: -147→-92 kcal/mol | 膜结合与蛋白互作部分竞争但总体亲和力保持 | 膜上 PEX5-PEX14 复合物的化学计量 | Results 图 5；表 2 |
| 浮选实验 | PEX5 全长蛋白结合脂质体 | DMPC vs DOPE/DOPC 脂质体 | 两种脂质组成均观察到浮选共迁移 | PEX5 膜结合不依赖特定脂质组成 | 体内膜结合是否由蛋白辅助 | 补充图 2A-B |
| CD 热稳定性 | 膜结合不破坏 PEX14 结构 | 无膜 vs 有膜 | Tm 相似 | 膜结合不改变 PEX14 NTD 折叠稳定性 | 膜结合对 PEX14 构象动态的影响 | 补充图 3C-D |

## 11 结论正确解读

- **任务范围**：本文仅研究 PEX5 和 PEX14 的 NTD 片段与人工膜模拟物（bicelles、nanodiscs）的体外互作，不涉及全长蛋白、完整过氧化物酶体膜或其他 peroxin 蛋白。
- **Oracle/真值输入**：无计算方法，所有结论基于实验数据。
- **端到端状态**：非端到端——本文是机制研究的中间环节，未构建完整的 translocon 组装模型。
- **算力成本**：不适用。
- **历史数据依赖**：依赖此前 PEX5-PEX14 晶体结构（Neufeld et al., 2009）和 ITC 数据（Neuhaus et al., 2014）作为互作界面参考。
- **模型依赖**：不适用。
- **最难情形**：PEX5 NTD 的 W3/W4 区域因谱峰重叠无法归属，膜结合贡献无法定量；bicelles 高曲率可能高估膜亲和力。
- **群体/领域边界**：结论限于过氧化物酶体转运系统；对其它 IDP-膜系统仅提供方法学参考。
- **不确定性**：KDapp 拟合基于单一位点模型，实际膜结合可能涉及多位点协同；ITC 中 bicelles 浓度（44 μM）可能未完全饱和 PEX5 膜结合位点。

**有边界的复述**：在体外条件下，PEX5 NTD 的 C 端区域（约残基 228-315）通过两亲性 α-螺旋以微摩尔级亲和力结合 DMPC 膜表面，该结合稳定螺旋构象但不改变 PEX5-PEX14 的纳摩尔级互作亲和力（仅从 147 nM 轻微降至 260 nM），提示膜的主要功能是富集 PEX5 而非变构调节其与 PEX14 的结合。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 膜模拟物不能完全代表天然膜 | bicelles 高曲率、单一脂质组成（DMPC），不含胆固醇/磷脂酰肌醇等 | 使用更接近天然组成的膜系统验证 | Discussion 节 |
| W3/W4 区域无法归属 | 谱峰重叠导致无法定量这些区域的膜结合贡献 | 需要更高场强 NMR 或选择性标记策略 | Results 节「PEX5 NTD Interacts With Membranes」 |
| 未研究全长 PEX5 在膜上的行为 | 亚片段可能丢失长程相互作用 | 全长蛋白的 NMR 研究（需优化表达和标记方案） | Discussion 节 |
| 未直接观察膜上的 PEX5-PEX14 复合物 | ITC 反映的是溶液中的竞争关系，非膜上复合物结构 | 需要固态 NMR 或 cryo-EM 研究膜结合复合物 | Discussion 节 |
| 未研究其它 peroxin 蛋白（如 PEX13）的影响 | 体内 translocon 组装涉及多个蛋白 | 未来需纳入 PEX13 等蛋白进行多组分研究 | Discussion 节 |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 亚片段策略可能丢失长程相互作用 | PEX5 NTD 的膜结合可能依赖片段间的协同，亚片段实验高估或低估真实亲和力 | 全长 IDR 的构象 ensemble 可能不同于片段之和 | 用全长 PEX5 NTD 进行单分子 FRET 或 smFRET 膜结合实验 | Results 图 1A 中亚片段设计 |
| Bicelles 的 DMPC 为饱和脂质，缺乏电荷 | 天然过氧化物酶体膜含负电脂质（如 PI），PEX5 膜结合可能依赖静电相互作用 | 若膜结合依赖静电，则 DMPC 实验会低估真实亲和力 | 使用含 PI/PS 的 bicelles 或 nanodiscs 重复滴定 | Methods「Bicelles」；引言引用 Hardeman 脂质组成 |
| ITC 中 bicelles 浓度（44 μM）可能未饱和 | 若 PEX5 膜结合位点未饱和，KD 变化可能反映的是膜结合竞争的不完全 | 影响「膜不改变互作」结论的强度 | 在更高 bicelles 浓度下重复 ITC | Results 图 5B |
| 浮选实验未定量 | 仅定性显示共迁移，未给出结合百分比或亲和力 | 无法与 NMR 滴定结果交叉验证 | 使用定量浮选或表面等离子共振（SPR） | 补充图 2A-B |
| 未检测 PEX5 膜结合对 cargo 释放的影响 | 膜结合可能促进 PEX5 构象变化从而释放 cargo，但本文未测 | 膜结合的生物学功能可能不仅是定位 | 在脂质体存在下检测 PEX5-cargo 复合物的解离 | Discussion 中未提及 |
| 未讨论 PEX5 膜结合与 PEX14 竞争的时间尺度 | 弱膜结合（μM）与强蛋白互作（nM）的动力学关系未研究 | 体内 translocon 组装可能依赖动力学而非热力学 | 使用 stopped-flow 或 NMR 弛豫弥散测量交换速率 | 表 1、表 2 数据 |

## 14 与已有知识连接

- **PEX5-PEX14 互作结构基础**：Neufeld et al. (2009) 和 Neuhaus et al. (2014) 的晶体/NMR 结构确定了 WF 基序与 PEX14 NTD 疏水沟槽的结合模式。本文的 ITC 数据（KD=147 nM）与此前报道一致，验证了实验体系可靠性。
- **IDP 膜结合的两亲性螺旋机制**：与其它 IDP 膜结合研究（如 α-synuclein、MARCKS 肽段）一致，两亲性螺旋插入膜界面是常见模式。本文发现的「预形成螺旋 + 膜诱导稳定化」机制与 α-synuclein 的膜结合模型相似。
- **过氧化物酶体 translocon 组装模型**：本文支持「PEX5 先膜结合后 PEX14 对接」的模型，与 Szymanska et al. (2020) 提出的「PEX5 膜扫描」假说一致（本文未引用，[Analysis] 推测）。
- **熵补偿机制**：本文观察到的「膜结合预组织螺旋降低蛋白互作熵代价」与经典 coupled folding and binding 理论（Dyson & Wright, 2002）一致。
- **方法学连接**：bicelles + NMR 滴定表征 IDP-膜互作的方法可迁移至其它 IDP-膜系统研究。

## 15 与已有知识连接

- **相似工作**：Emmanouilidis et al. (2016) 对 PEX5 NTD 的 NMR 表征（本文引用），确认了其 intrinsically disordered 特性；本文在此基础上增加了膜结合维度。
- **方法学先例**：Hagn et al. (2018) 的 nanodisc 制备方法（本文 Methods 引用），用于膜蛋白 NMR 研究。
- **潜在冲突**：Barros-Barbosa et al. (2019) 提出 PEX14 NTD 位于过氧化物酶体腔内侧，若如此，PEX5 在胞质侧如何接触 PEX14 NTD 需要重新解释。本文未直接回应此争议，但膜结合数据支持 PEX5 可独立于 PEX14 结合膜。
- **可迁移领域**：本文的「弱膜结合 + 强蛋白互作」双亲和力模型可推广至其它 IDP 介导的膜相关蛋白互作系统（如突触蛋白、病毒基质蛋白）。

## 16 研究想法

**Agent 生成的研究候选**

1. **候选名称**：IDP 膜结合位点的深度学习预测器
   - **来源局限/观察**：本文实验表征了 PEX5 NTD 的膜结合位点，但实验方法耗时且需要同位素标记；目前缺乏从序列预测 IDP 膜结合位点的工具。
   - **核心假设**：两亲性螺旋 + 芳香族残基（W/F）富集 + 净正电荷的组合特征可预测 IDP 膜结合区域。
   - **相对本文的增量**：将本文的实验数据（CSP 图谱、KD 值）作为训练/验证集，开发生物学可解释的预测模型。
   - **初步方法**：收集已发表的 IDP 膜结合实验数据（NMR CSP、突变扫描），提取序列特征（螺旋倾向、疏水性、芳香族残基分布），训练梯度提升或 CNN 分类器。
   - **验证方式**：留一法交叉验证；对 PEX5 同源蛋白（PEX5L/PEX5S）进行预测并实验验证。
   - **可能的失败模式**：IDP 膜结合位点可能依赖三级结构上下文而非线性序列特征，导致预测精度不足。
   - **创新状态**：unverified

2. **候选名称**：膜存在下 IDP-蛋白互作的粗粒化 MD 模拟
   - **来源局限/观察**：本文 ITC 显示膜存在时 PEX5-PEX14 亲和力轻微下降，但无法解释分子机制；原子级 MD 模拟 IDP-膜-蛋白三组分体系计算成本过高。
   - **核心假设**：膜表面通过排除体积效应和静电筛选降低 PEX5-PEX14 的结合能垒，但通过预组织螺旋构象补偿熵损失。
   - **相对本文的增量**：提供膜调节 IDP-蛋白互作的分子级机制解释，补充实验无法获得的结构动态信息。
   - **初步方法**：使用 MARTINI 粗粒化力场，构建 PEX5 NTD（从 AlphaFold 预测结构提取）+ PEX14 NTD + DMPC 双层膜体系；模拟不同膜结合状态下的 PEX5-PEX14 结合自由能（伞形采样）。
   - **验证方式**：模拟预测的 KD 变化与本文 ITC 数据（147→260 nM）对比；预测关键残基突变效应。
   - **可能的失败模式**：粗粒化力场对 IDP 构象 ensemble 的描述不准确，导致结合自由能计算偏差。
   - **创新状态**：unverified

3. **候选名称**：PEX5-PEX14 互作界面的 AI 辅助突变设计
   - **来源局限/观察**：本文确认 WF 基序是膜结合和 PEX14 结合的共同界面，但未系统探索如何设计选择性突变来区分两种功能。
   - **核心假设**：通过深度学习（如 ProteinMPNN）设计保留 PEX14 结合但减弱膜结合的 PEX5 突变体，可验证膜结合在 translocon 组装中的独立功能。
   - **相对本文的增量**：将本文的双功能界面发现转化为可操作的突变设计工具。
   - **初步方法**：以 PEX5-PEX14 复合物结构为模板，用 ProteinMPNN 生成序列变体；用 Rosetta 或 AlphaFold 评估结合亲和力变化；筛选候选突变体进行实验验证（ITC + 浮选）。
   - **验证方式**：实验测定设计突变体的 PEX14 结合 KD 和膜结合 KDapp，与预测对比。
   - **可能的失败模式**：WF 基序的膜结合和蛋白结合可能由相同残基介导，无法完全解耦。
   - **创新状态**：unverified

4. **候选名称**：IDP 膜结合与蛋白互作竞争的热力学数据库
   - **来源局限/观察**：本文提供了 PEX5-PEX14 在膜存在/不存在时的完整热力学参数（ΔH、ΔS、ΔG），但此类数据在文献中极为稀缺。
   - **核心假设**：系统收集 IDP-膜-蛋白三组分热力学数据可揭示「熵-焓补偿」的普适规律。
   - **相对本文的增量**：将本文的单点数据扩展为领域资源，为 AI 模型训练提供特征。
   - **初步方法**：文献挖掘 + 数据库构建（类似 BioGRID 但聚焦热力学参数）；标注膜组成、蛋白片段、实验方法。
   - **验证方式**：数据库覆盖度评估；用收集的数据训练热力学参数预测模型。
   - **可能的失败模式**：文献数据异质性大（不同膜组成、缓冲条件），难以直接比较。
   - **创新状态**：unverified