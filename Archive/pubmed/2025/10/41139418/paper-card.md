## 01 基本信息

- **标题**: AlphaFold-Guided Discovery of an Overlapping MYC/Miz-1 Interface Enables Peptidomimetic Disruption of MYC/MAX
- **作者与单位**: Ellenbroek, Brecht D; Tirtosentono, Amardhiko S S; Pomplun, Sebastian J（荷兰莱顿大学莱顿化学研究所，Leiden Institute of Chemistry，依据致谢部分推断）
- **期刊/预印本平台**: ChemMedChem
- **年份**: 2025
- **论文类型**: 研究论文（Research Article）
- **领域**: 化学生物学、药物化学、结构生物学、无序蛋白互作
- **关键词**: AlphaFold-Multimer；MYC；Miz-1；MAX；无序蛋白（IDP）；肽模拟物（peptidomimetic）；stapled peptide；蛋白-蛋白互作（PPI）
- **DOI/arXiv 号**: 10.1002/cmdc.202500740
- **代码**: 未提供
- **数据**: 补充材料（Supporting Information）中提供，包括蛋白表达纯化数据（图 S1–S10、表 S1）、BLI 结合数据（图 S11、表 S2–S4）、CD 光谱数据（图 S12）、EMSA 数据（图 S13–S17）等
- **阅读日期**: 2026-05-13
- **在该方向中的位置**: 本文是「AlphaFold-Multimer 预测无序蛋白互作界面 → 指导多肽设计 → 干扰致癌 PPI」的典型案例。它展示了 AI 结构预测在 IDP 靶点（MYC）上发现可成药界面的能力，属于「IDP/IDR × 蛋白互作 × AI 方法」交叉方向中「AI 预测指导实验验证」的代表性工作，且聚焦于 MYC 这一经典无序致癌蛋白。

## 02 一句话总结

本文使用 AlphaFold-Multimer 预测 MYC 与 Miz-1 的互作界面，发现 Miz-1 MID2 结构域以 α-螺旋构象结合于 MYC 的 HLH 结构域疏水沟槽（与 MAX 二聚化界面重叠），据此设计并合成 stapled 肽模拟物（Mizmetic 系列），其中优化变体（Mizmetic 20）在亚微摩尔浓度下可破坏 MYC/MAX/DNA 复合物的形成。

## 03 研究问题

- **具体问题**: MYC 与 Miz-1 之间的蛋白-蛋白互作界面在结构上如何组织？该界面是否可被靶向？能否通过靶向 MYC/Miz-1 界面来干扰 MYC/MAX 的致癌功能？
- **为什么重要**: MYC 是超过 50% 人类癌症中失调的关键转录因子，属于无序蛋白（IDP），缺乏经典药物结合口袋，长期被视为"不可成药"靶点。MYC/Miz-1 互作在肿瘤发展中起重要作用（MYC 通过结合 Miz-1 抑制细胞周期负调控因子如 p21 和 p15 的表达），但该界面从未被结构解析，也从未被靶向。
- **现有方法为何不足**: MYC 的无序本质使得 X 射线晶体学和传统 NMR 结构解析极为困难；MYC/MAX 界面虽被广泛研究，但 MYC/Miz-1 界面缺乏结构信息；已有的 MYC/MAX 小分子抑制剂（如 10058-F4 等）效力有限且选择性差；尚无任何靶向 MYC/Miz-1 界面的分子工具。
- **精确的 "Can ... ?" 研究问题**: Can AlphaFold-Multimer accurately predict the binding interface between an intrinsically disordered protein (MYC) and its partner (Miz-1), and can this predicted interface be exploited to design peptidomimetic inhibitors that disrupt MYC/MAX/DNA complex formation?

## 04 背景与发展脉络

*注：以下脉络基于本文引言及参考文献，属于「经外部核验」的领域发展脉络。*

1. **阶段一：MYC 作为药物靶点的早期探索（2000s–2010s）**
   - 代表性方法：靶向 MYC/MAX 二聚化界面的小分子筛选（如 10058-F4、10074-G5）、Omomyc 等显性负性肽
   - 优点：验证了 MYC/MAX 界面可被靶向的概念
   - 局限：小分子亲和力低、细胞渗透性差；Omomyc 虽有效但为蛋白药物，递送困难；MYC 的无序性使结构辅助设计受限

2. **阶段二：无序蛋白互作的结构预测兴起（2020s 早期）**
   - 代表性方法：AlphaFold2/AlphaFold-Multimer 应用于 IDP 复合物预测
   - 优点：无需实验结构即可获得复合物模型；对部分 IDP 互作（如 p53 与 partners）预测准确
   - 局限：对完全无序区域预测置信度仍有限；预测结果需实验验证；对瞬时/弱互作可能失效

3. **阶段三：AI 预测指导的 IDP 靶向肽设计（2023–2025）**
   - 代表性方法：AlphaFold 预测界面 → 提取关键螺旋片段 → stapled peptide 或 proteomimetic 设计
   - 优点：大幅缩短从结构信息到候选分子的周期；可发现实验结构未知的界面
   - 局限：预测误差可能传导至设计；IDP 的构象异质性使单一静态模型可能不完整

4. **本文位置**: 本文属于阶段三的代表性工作，首次将 AlphaFold-Multimer 应用于 MYC/Miz-1 界面预测，并成功转化为功能性肽抑制剂。其独特贡献在于：(a) 预测并验证了 MYC/Miz-1 与 MYC/MAX 界面重叠这一此前未知的结构特征；(b) 展示了 AI 预测在"不可成药"IDP 靶点上的实用价值。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| MYC 缺乏稳定结构 | MYC 单独存在时呈无序状态，无经典药物结合口袋 | MYC 属于 IDP，其折叠依赖于伴侣结合 | 引言："When not in complex, MYC is disordered"；图 1a |
| MYC/Miz-1 界面结构未知 | 无晶体结构、无高分辨率复合物模型 | MYC 无序性使共结晶困难；Miz-1 互作区域较大（MID2 含 84 个氨基酸） | 引言："there is no crystal structure elucidated for this complex" |
| 传统结构解析方法失效 | X 射线晶体学和 NMR 难以应用于 MYC/Miz-1 复合物 | 复合物瞬时性、构象异质性、表达纯化困难 | 引言："The MYC–Miz-1 interaction is difficult to characterize experimentally due to the intrinsically disordered nature of MYC" |
| BLI 结合曲线不理想 | 结合/解离曲线形状偏离理想 1:1 模型 | 可能由 MYC 无序区域的非特异性聚集或构象变化导致 | Results："nonideal binding behavior was observed by BLI, eventually caused by aggregation of the unstructured MYC domain" |
| 非特异性结合 | Mizmetic 16 同时抑制 MYC/MAX 和 MAX/MAX 复合物 | 机制未完全阐明，可能涉及 MAX 表面疏水区域的非特异性结合 | Results 图 4e,f："Mizmetic 16 had no preference for MYC over MAX" |

## 06 核心思想

### 1) 表面方法
使用 AlphaFold-Multimer 预测 MYC 与 Miz-1 两个结构域（MID1 和 MID2）的复合物结构，基于预测结果设计 α-螺旋 stapled 肽（Mizmetic 系列），通过 BLI 验证结合、CD 验证构象、EMSA 验证功能抑制。

### 2) 核心洞察
**无序蛋白在结合伴侣时形成瞬时但结构明确的界面，这些界面可以被 AI 结构预测捕获，并转化为可靶向的药物结合位点。** 具体而言：
- AlphaFold-Multimer 成功预测了 Miz-1 MID2 中一段 28 个氨基酸的 α-螺旋区域结合于 MYC HLH 结构域的疏水沟槽，且该界面与 MYC/MAX 二聚化界面重叠——这一预测结果与早期酵母双杂交实验的结论一致，但首次提供了结构层面的解释。
- 螺旋稳定化（stapling）可以将原本无序的肽段转化为具有预组织构象的结合分子，实现 26 倍的亲和力提升。
- 靶向 MYC/Miz-1 界面的肽可以"跨界"干扰 MYC/MAX 互作，因为两个界面在空间上重叠——这为靶向 MYC 提供了新的策略：不一定要直接阻断 MAX 结合，也可以通过占据 Miz-1 位点来变构或竞争性干扰 MYC/MAX 二聚化。

### 3) 可能的普适教训 [Analysis]
- **AI 预测可以作为 IDP 互作界面发现的"第一筛"**：对于实验结构缺失的 IDP 复合物，AlphaFold-Multimer 的预测（即使置信度中等）可以提供可检验的假说，大幅缩小实验搜索空间。
- **"界面重叠"是 IDP 靶向的潜在策略**：如果一个 IDP 与多个伙伴互作时使用相同或重叠的界面，那么靶向其中一个界面可能同时干扰多个互作——这对 MYC 这类"hub"蛋白尤为重要。
- **Stapled peptide 是 IDP 界面靶向的有效工具**：从预测的 α-螺旋界面提取序列、进行螺旋稳定化修饰，是一条从结构信息到功能分子的快速通道。

## 07 方法总览

- **输入**: 
  - 蛋白序列：MYC（残基 369–454，bHLH-LZ 区域）、Miz-1 MID1（残基 269–308）、Miz-1 MID2（残基 637–718）
  - AlphaFold-Multimer 用于复合物结构预测
- **输出**: 
  - 预测的 MYC/Miz-1 复合物结构模型
  - 设计并合成的 stapled 肽（Mizmetic WT, 1, 2, 3 及 19 个丙氨酸突变体）
  - 结合亲和力数据（BLI）、构象数据（CD）、功能抑制数据（EMSA）
- **模块**:
  1. AlphaFold-Multimer 结构预测模块
  2. 肽序列设计模块（基于预测界面提取 + 丙氨酸扫描设计）
  3. 肽合成模块（SPPS + 硫醇-芳香交联 stapling）
  4. 结合验证模块（BLI）
  5. 构象表征模块（CD）
  6. 功能抑制模块（EMSA）
- **训练**: 不适用（使用预训练的 AlphaFold-Multimer 模型）
- **工具**: AlphaFold-Multimer、BLI（生物层干涉法）、CD 光谱、EMSA、SPPS
- **反馈回路**: AlphaFold 预测 → 肽设计 → 实验验证 → 丙氨酸扫描 → 优化变体 → 功能验证
- **文字流程**: 
  1. 使用 AlphaFold-Multimer 分别预测 MYC/MID1 和 MYC/MID2 复合物结构
  2. 发现 MID2 中 28 个氨基酸的 α-螺旋区域（残基 685–712）以高置信度结合于 MYC HLH 结构域
  3. 合成该 28 肽（Mizmetic WT），BLI 验证结合（Kd ≈ 4.6 µM）
  4. 通过 AlphaFold 模拟螺旋稳定化（Cys-Zn²⁺ 配位），确定 stapling 位点（Ser16, Lys20）
  5. 合成 stapled 肽 Mizmetic 1，BLI 显示亲和力提升 26 倍（Kd ≈ 176 nM）
  6. 截短优化得到 Mizmetic 2（24 肽，Kd ≈ 76–119 nM）
  7. 丙氨酸扫描（Mizmetic 4–22）鉴定关键残基
  8. EMSA 验证变体对 MYC/MAX/DNA 复合物的抑制能力

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| AlphaFold-Multimer 结构预测 | 预测 MYC/Miz-1 复合物结构 | MYC 无序、无实验结构，需要计算模型指导实验 | 输入：MYC 和 Miz-1 序列；输出：复合物结构模型及置信度分数 | 预测的 MID2 结合位点与酵母双杂交结果一致；丙氨酸扫描验证了预测的热点残基 | [预期] 移除后无法确定 Miz-1 结合位点，肽设计将缺乏结构指导，需依赖随机筛选 |
| 肽序列提取与设计 | 从预测界面提取 α-螺旋序列作为肽候选 | 需要将结构信息转化为可合成的分子 | 输入：预测复合物结构；输出：28 肽序列（Mizmetic WT） | Mizmetic WT 与 MYC 结合（Kd ≈ 4.6 µM） | [预期] 移除后无初始肽候选，整个研究无法启动 |
| Stapling 修饰 | 通过硫醇-芳香交联稳定 α-螺旋构象 | 线性肽在溶液中呈无序状态，结合亲和力低 | 输入：Mizmetic WT 序列；输出：stapled 肽 Mizmetic 1 | 亲和力从 4.6 µM 提升至 176 nM（26 倍）；CD 显示螺旋含量从 3.0% 提升至 11.6% | [实测] Mizmetic WT 结合弱（µM 级），无 stapling 则无法达到亚 µM 亲和力 |
| 截短优化 | 确定最小功能序列 | 28 肽过长，不利于后续药物开发 | 输入：Mizmetic 1；输出：Mizmetic 2（24 肽）和 Mizmetic 3（20 肽） | Mizmetic 2 保持亲和力（Kd ≈ 76–119 nM）；Mizmetic 3 亲和力大幅下降（Kd ≈ 6 µM） | [实测] 移除 C 端 4 个氨基酸（Mizmetic 3）导致亲和力下降约 50 倍，说明 C 端残基对结合至关重要 |
| 丙氨酸扫描 | 鉴定每个残基对结合的贡献 | 需要理解构效关系以指导进一步优化 | 输入：Mizmetic 2 序列；输出：19 个丙氨酸突变体的亲和力数据 | 鉴定出 3 个热点（Leu7, Ile11, Val15）和 5 个冷点（Glu3, Thr4, Glu5, Lys8, Lys13） | [预期] 移除后无法确定哪些残基可以进一步修饰或替换 |
| EMSA 功能抑制实验 | 验证肽能否干扰 MYC/MAX/DNA 复合物 | 结合 MYC 不等于功能抑制，需要功能验证 | 输入：候选肽 + MYC/MAX/DNA；输出：复合物形成/抑制的凝胶图像 | Mizmetic 13, 16, 20 抑制 MYC/MAX/DNA 形成；Mizmetic 20 IC50 ≈ 560 nM | [预期] 移除后无法确认肽的功能活性，研究停留在"结合剂"而非"抑制剂"层面 |

## 09 关键公式符号

本文为实验驱动型研究，不涉及复杂数学模型或物理公式。以下为与数据解读直接相关的公式：

1. **解离常数（Kd）** — 用于 BLI 结合亲和力定量：
   \[
   K_d = \frac{[P][L]}{[PL]}
   \]
   其中 [P] 为蛋白浓度，[L] 为配体（肽）浓度，[PL] 为复合物浓度。文中通过 BLI 稳态分析或动力学拟合获得观测 Kd 值。

2. **半数抑制浓度（IC50）** — 用于 EMSA 竞争实验定量：
   \[
   IC_{50} = \text{抑制 50\% 复合物形成所需的抑制剂浓度}
   \]
   文中通过梯度浓度肽处理 + 凝胶条带定量获得。

3. **α-螺旋含量估算** — CD 光谱中通过 222 nm 摩尔椭圆率估算：
   \[
   \% \text{ helicity} = \frac{[\theta]_{222}}{[\theta]_{max}} \times 100\%
   \]
   其中 [θ]222 为 222 nm 处观测摩尔椭圆率，[θ]max 为理论最大椭圆率。文中使用 BestSEL 软件进行估算（Mizmetic WT: 3.0%，Mizmetic 1: 11.6%）。

4. **AlphaFold 置信度指标** — 用于评估预测可靠性：
   - **ipTM**（interface predicted Template Modeling score）：界面预测质量，文中 MYC/MID1 为 0.07（低置信度），MYC/MID2 为 0.33（中等置信度）
   - **pTM**（predicted Template Modeling score）：整体结构预测质量，文中 MYC/MID1 为 0.49，MYC/MID2 为 0.47

## 10 实验设计与证据链

### 数据集/群体/规模
- **蛋白构建体**：MYC bHLH-LZ（残基 369–454）、Miz-1 MID1（残基 269–308）、Miz-1 MID2（残基 637–718）、MAX bHLH-LZ（残基 22–103）
- **肽库**：Mizmetic WT（28 肽）、Mizmetic 1（stapled 28 肽）、Mizmetic 2（stapled 24 肽）、Mizmetic 3（stapled 20 肽）、Mizmetic 4–22（19 个丙氨酸突变体）
- **实验方法**：BLI（结合亲和力）、CD（构象）、EMSA（功能抑制）
- **指标**：Kd（BLI）、IC50（EMSA）、% helicity（CD）
- **预算/资源**：未提供具体信息
- **骨干/仪器**：BLI 生物传感器、CD 光谱仪、凝胶电泳系统
- **oracle 输入**：AlphaFold-Multimer 预测结构（作为设计指导）
- **评测协议**：BLI 梯度浓度结合实验；EMSA 竞争实验（固定 MYC/MAX/DNA 浓度，梯度肽浓度）

### 实验表格

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| AlphaFold-Multimer 预测 MYC/MID1 和 MYC/MID2 | MID2 而非 MID1 与 MYC 形成高置信度复合物 | MID1 vs MID2 预测对比 | MID1: ipTM=0.07；MID2: ipTM=0.33，预测 28 残基 α-螺旋结合于 MYC HLH 疏水沟槽 | MID2 是 MYC 的主要结合区域，与酵母双杂交结果一致 | 预测置信度中等（ipTM=0.33），不能排除其他结合模式 | Results 图 1c–f |
| BLI 验证 Mizmetic WT 与 MYC 结合 | 预测的肽序列确实结合 MYC | Mizmetic WT vs 空白对照 | 观测 Kd ≈ 4.6 ± 1.3 µM | 预测的 α-螺旋区域确实介导 MYC 结合 | BLI 曲线不理想，Kd 为观测值而非精确值 | Results 图 S11、表 S2 |
| Stapling 对结合亲和力的影响 | 螺旋稳定化增强结合 | Mizmetic WT vs Mizmetic 1 | Kd 从 4.6 µM 提升至 176 nM（26 倍） | Stapling 通过预组织螺旋构象显著增强结合 | 未直接证明亲和力提升完全归因于螺旋含量增加 | Results 图 2c、表 S2 |
| 截短优化 | 24 肽保持结合活性 | Mizmetic 1 vs 2 vs 3 | Mizmetic 2: Kd ≈ 76–119 nM；Mizmetic 3: Kd ≈ 6 µM | N 端 4 个残基非必需，C 端 4 个残基对结合至关重要 | 未系统扫描所有截短组合 | Results 图 2f、表 S3 |
| 丙氨酸扫描 | 鉴定关键结合残基 | 19 个丙氨酸突变体 vs Mizmetic 2 | Leu7, Ile11, Val15 突变显著降低结合；Glu3, Thr4, Glu5, Lys8, Lys13 突变增强结合 | 疏水残基 Leu7/Ile11/Val15 是结合热点，与 AlphaFold 预测一致 | 丙氨酸扫描仅反映单点突变效应，未测试组合突变 | Results 图 3a、表 S4 |
| EMSA 竞争实验 | 优化的 Mizmetic 变体抑制 MYC/MAX/DNA 复合物 | Mizmetic WT/1/2/13/16/19/20/21 vs 对照 | Mizmetic 13, 16, 20 完全消除 MYC/MAX/DNA 条带；Mizmetic 20 IC50 ≈ 560 nM | 靶向 MYC/Miz-1 界面的肽可干扰 MYC/MAX/DNA 形成 | Mizmetic 16 也抑制 MAX/MAX/DNA，存在非特异性；未在细胞水平验证 | Results 图 4c–f、图 S14–S17 |

## 11 结论正确解读

- **任务范围**：本文仅涉及体外生化实验（BLI、CD、EMSA），未进行细胞实验或动物实验。结论限于"体外条件下，特定肽序列可结合 MYC 并干扰 MYC/MAX/DNA 复合物形成"。
- **oracle/真值输入**：AlphaFold-Multimer 预测结构作为设计指导，但预测本身并非实验真值。实验验证（BLI 结合、丙氨酸扫描一致性）为预测提供了部分验证，但未通过共结晶或突变-结合-功能三联实验完全确认预测界面的精确原子接触。
- **端到端状态**：从 AI 预测到功能性肽抑制剂的完整流程已在体外验证，但尚未达到"药物开发"阶段。作者明确标注为"proof-of-concept"。
- **算力成本**：未提供 AlphaFold-Multimer 预测的计算资源信息。
- **历史数据依赖**：AlphaFold-Multimer 的训练数据包含大量已知蛋白复合物结构，对 MYC 相关预测的准确性可能受训练数据中 MYC 同源蛋白（如其他 bHLH-LZ 家族成员）结构的影响。
- **模型依赖**：结果依赖于 AlphaFold-Multimer 的预测准确性。ipTM=0.33 属于中等置信度，预测的精确界面可能不完全准确。
- **最难情形**：MYC 的无序性意味着其结合构象可能具有多个亚稳态，AlphaFold 预测的单一构象可能无法完全代表溶液中的构象系综。
- **群体/领域边界**：结论仅适用于 MYC/Miz-1/Max 这一特定系统，不能推广至所有 IDP 互作。方法学（AI 预测 → 肽设计）可能具有可迁移性，但需逐案验证。
- **不确定性**：BLI 曲线不理想导致 Kd 值精度有限；Mizmetic 16 的非特异性抑制机制未阐明；未检测肽对 MYC 单独结合 Miz-1 的抑制效果（仅检测了对 MYC/MAX/DNA 的影响）。

**有边界的复述**：在体外条件下，AlphaFold-Multimer 预测的 Miz-1 MID2 α-螺旋区域（残基 685–712）确实能以微摩尔亲和力结合 MYC bHLH-LZ 区域；通过 stapling 和截短优化，可获得纳摩尔级结合剂；其中部分变体（特别是 Mizmetic 20）能在亚微摩尔浓度下干扰 MYC/MAX/DNA 复合物的形成，但存在一定的非特异性效应。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| BLI 结合曲线不理想 | 无法获得精确的 Kd 值，只能报告"观测 Kd" | 未明确提及改进方案 | Results："limiting us in finding the true affinity value toward MYC" |
| 非特异性结合 | Mizmetic 16 同时抑制 MYC/MAX 和 MAX/MAX DNA 复合物 | 未明确提及 | Results："potentially indicating some degree of unspecific binding" |
| 仍处于概念验证阶段 | 未进行细胞或体内实验 | 未明确提及，但暗示需要进一步优化 | Conclusion："While still at a proof-of-concept stage" |
| 需要进一步优化 | 部分变体存在非特异性，需要提高选择性 | "there is need for further optimization of these compounds" | Conclusion |

*注：作者在提供的全文/摘要中未系统列出"Limitations"章节，以上为从正文中提取的明确承认的局限。*

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| AlphaFold-Multimer 预测的 ipTM=0.33 属于中等置信度 | 预测的界面可能不完全准确；可能只是 MYC 表面多个弱结合位点之一 | 如果预测界面不准确，后续肽设计的"合理性"论证将被削弱 | 通过共结晶或 HDX-MS 等实验方法验证预测界面的精确原子接触 | Results 图 1d：ipTM=0.33 |
| Mizmetic 16 抑制 MAX/MAX/DNA 复合物 | 可能不是通过与 MYC 结合来发挥抑制作用的，而是直接结合 DNA 或 MAX | 如果存在非特异性 DNA 结合，则"靶向 MYC/Miz-1 界面"的机制叙述需要修正 | 进行无 MYC 的对照实验（肽 + MAX + DNA），检测是否直接干扰 MAX/DNA 互作；或使用表面等离子共振检测肽与 DNA 的直接结合 | Results 图 4e,f |
| 未进行细胞实验 | 体外结合和抑制活性不一定转化为细胞内活性 | 对于"治疗干预"的最终目标，缺乏细胞水平证据是一个显著缺口 | 在 MYC 驱动的癌细胞系中测试 Mizmetic 的活性（如增殖抑制、MYC 靶基因表达变化） | Conclusion："proof-of-concept stage" |
| 未检测 Mizmetic 对 MYC/Miz-1 互作的直接抑制 | 实验检测的是 MYC/MAX/DNA 复合物的减少，而非 MYC/Miz-1 互作的直接竞争 | 如果 Mizmetic 是通过其他机制（如诱导 MYC 构象变化）来抑制 MYC/MAX，则"靶向 MYC/Miz-1 界面"的叙述需要调整 | 进行 MYC/Miz-1 的直接结合竞争实验（如 BLI 竞争或 pull-down） | Results 图 4c–f |
| 丙氨酸扫描仅检测了单点突变 | 组合突变可能揭示协同效应；热点残基的鉴定可能不完整 | 对于进一步优化肽序列，需要更全面的构效关系数据 | 对热点残基进行组合突变，或进行饱和突变扫描 | Results 图 3a |
| 未与已知 MYC/MAX 抑制剂进行直接比较 | 无法评估 Mizmetic 相对于已有工具分子的优劣 | 对于实际应用价值评估，需要基准比较 | 在相同实验条件下测试已知 MYC/MAX 抑制剂（如 10058-F4）作为阳性对照 | 未提供 |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **AI 预测可作为 IDP 互作界面发现的低成本筛选工具**：本文展示了 AlphaFold-Multimer 在无实验结构的情况下预测 IDP 结合界面的实用性。对于本课题（IDP/IDR × 蛋白互作 × AI），可迁移的方法论是：对目标 IDP 与其伙伴蛋白进行 AlphaFold-Multimer 预测 → 提取高置信度界面区域 → 设计肽或小分子候选。关键注意点是 ipTM 阈值的选择——本文中 ipTM=0.33 即被采用，说明中等置信度预测也可能具有实验指导价值。

2. **"界面重叠"策略：靶向一个 IDP 的多个互作界面**：本文发现 MYC/Miz-1 与 MYC/MAX 界面重叠，因此靶向 Miz-1 结合位点的肽也能干扰 MYC/MAX 互作。对于相分离研究，这一策略可能更广泛适用：许多相分离驱动蛋白（如 FUS、TDP-43、TAF15）通过多个弱相互作用界面与不同伙伴互作，如果这些界面重叠，一个分子工具可能同时干扰多个互作和相分离行为。

3. **Stapled peptide 是靶向 IDP 瞬时螺旋界面的有效策略**：从无序 IDP 序列中提取结合螺旋片段、通过 stapling 预组织构象，可实现 26 倍亲和力提升。对于相分离研究，这一策略可用于设计干扰凝聚体形成的肽工具——特别是当凝聚体由螺旋-螺旋相互作用驱动时。

4. **丙氨酸扫描是验证 AI 预测界面的高效实验手段**：本文通过 19 个丙氨酸突变体验证了 AlphaFold 预测的热点残基。对于本课题，这一方法可推广为"AI 预测 → 丙氨酸扫描验证 → 界面确认"的标准流程，尤其适用于缺乏高分辨率实验结构的 IDP 互作系统。

5. **体外功能实验（EMSA）作为 AI 预测的"功能验证"层**：本文不仅验证了结合，还验证了功能抑制（干扰 MYC/MAX/DNA）。对于相分离研究，类似的功能验证可以是：肽处理后检测凝聚体形成/解离的变化（如浊度、FRAP、共定位等）。

6. **BLI 是适合 IDP 互作的低样品消耗筛选平台**：本文使用 BLI 进行结合验证和丙氨酸扫描，该方法对无序蛋白的聚集倾向有一定耐受性（通过条件优化）。对于本课题中大量 IDP 候选互作的筛选，BLI 可作为中等通量的结合验证平台。

## 15 与已有知识连接

1. **MYC 无序性与相分离的关联**：MYC 的转录激活域（TAD）已知为无序区域，且 MYC 在转录凝聚体（transcriptional condensates）中富集。本文聚焦于 MYC 的 bHLH-LZ 结构域（相对有序），但 MYC 的 TAD 与相分离的关系是当前研究热点。本文的肽工具可作为干扰 MYC 凝聚体行为的候选分子。

2. **AlphaFold 在 IDP 互作预测中的已知局限**：已有文献（如 Ruff & Pappu, 2021; Chakravarty et al., 2023）指出 AlphaFold 对完全无序区域（无结合伴侣时）预测置信度低，但对"偶联折叠结合"（coupled folding-binding）界面可能给出有用预测。本文结果与这一观点一致——AlphaFold 对 MYC/MID2 的预测置信度中等但实验可验证。

3. **Miz-1 在相分离中的潜在角色**：Miz-1 含锌指结构域，已知参与 MYC 介导的转录抑制。虽然本文未涉及相分离，但 MYC/Miz-1 互作在转录调控凝聚体中的角色值得探索——本文的 Mizmetic 肽可作为扰动工具。

4. **Stapled peptide 靶向 IDP 互作的前例**：类似策略已用于靶向 p53/MDM2（如 Nutlin 类小分子和 stapled peptide）、Bcl-2 家族等。本文将其扩展到 MYC/Miz-1 这一此前未靶向的界面，验证了"AI 预测 → stapled peptide"这一组合策略的可行性。

5. **与 AlphaFold 蛋白质-配体预测的衔接**：本文使用 AlphaFold-Multimer 预测蛋白-蛋白互作，而本课题中涉及的"AI 方法"还可延伸至 AlphaFold3 等支持小分子/离子配体的新工具。本文中 Cys-Zn²⁺ 模拟 stapling 的策略，可视为利用 AlphaFold 预测非天然修饰蛋白的早期尝试。

6. **MYC 抑制剂领域的背景**：已有多种 MYC/MAX 小分子抑制剂（如 10058-F4、MYCi975）和肽类抑制剂（Omomyc）报道。本文的 Mizmetic 系列提供了一种新机制——通过靶向 MYC/Miz-1 界面而非 MYC/MAX 界面来干扰 MYC 功能，这为 MYC 靶向策略提供了新思路。

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**: MYC/Miz-1 界面肽对 MYC 相分离行为的调控研究
   - **来源局限/观察**: 本文仅验证了 Mizmetic 对 MYC/MAX/DNA 复合物的体外抑制，未涉及其对 MYC 在转录凝聚体中行为的调控。MYC 的 TAD 已知驱动相分离，但 bHLH-LZ 区域是否参与凝聚体形成尚不清楚。
   - **核心假设**: Mizmetic 肽通过占据 MYC 的 HLH 结构域，可能改变 MYC 在凝聚体中的富集/分配行为，从而影响转录凝聚体的形成或性质。
   - **初步方法**: 在体外相分离体系中（如 MYC TAD + 转录共激活因子），加入 Mizmetic 2/20，通过浊度、荧光显微镜、FRAP 检测凝聚体形成/性质变化；在细胞中通过光遗传或药物诱导的凝聚体报告系统验证。
   - **验证方式**: 凝聚体形成/解离的定量比较；Mizmetic 处理前后 MYC 靶基因表达变化。
   - **可能的失败模式**: MYC 的 HLH 结构域可能不直接参与相分离，Mizmetic 对凝聚体无影响；或 Mizmetic 的非特异性效应干扰结果解读。
   - **创新状态**: unverified

2. **候选名称**: AlphaFold-Multimer 预测 IDP 互作界面的系统评估——以 MYC 互作组为例
   - **来源局限/观察**: 本文仅对 MYC/Miz-1 一个互作对进行了预测-验证。MYC 作为 hub 蛋白，与数十个伙伴互作，其中多数互作界面未知。系统评估 AlphaFold 在 MYC 互作组中的预测能力，可确定该方法论的适用范围和置信度阈值。
   - **核心假设**: AlphaFold-Multimer 对 MYC 与其伙伴蛋白的互作预测准确性与伙伴蛋白的结构特征（有序 vs 无序）相关；对偶联折叠结合界面的预测准确率高于完全无序互作。
   - **初步方法**: 对 MYC 互作组中已知互作对进行 AlphaFold-Multimer 预测，与已有实验数据（突变、交联、NMR 等）比对；建立预测置信度与实验验证率的关联曲线。
   - **验证方式**: 选取预测高置信度但实验未表征的互作对，通过 BLI/ITC 验证。
   - **可能的失败模式**: AlphaFold 对 IDP 互作的预测准确率整体偏低，无法建立有效筛选流程。
   - **创新状态**: unverified

3. **候选名称**: 基于 AlphaFold 预测界面的 MYC 凝聚体调控肽设计
   - **来源局限/观察**: 本文的 Mizmetic 设计仅针对 MYC/Miz-1 界面。MYC 的 TAD 已知含多个低复杂度区域（LCD），可能驱动相分离。若 AlphaFold 能预测 TAD 与共激活因子（如 TRRAP、P-TEFb）的互作界面，则可设计针对这些界面的肽工具来调控 MYC 凝聚体。
   - **核心假设**: MYC TAD 与转录共激活因子的互作界面可被 AlphaFold-Multimer 预测，且这些界面驱动 MYC 在凝聚体中的富集。
   - **初步方法**: AlphaFold-Multimer 预测 MYC TAD 与候选伙伴的复合物结构 → 提取界面螺旋/线性基序 → 设计 stapled 肽 → 体外相分离实验验证。
   - **验证方式**: 肽处理后凝聚体形成/解离的定量变化；共定位分析。
   - **可能的失败模式**: TAD 的构象异质性过高，AlphaFold 预测不可靠；或 TAD 互作界面不驱动相分离。
   - **创新状态**: unverified

4. **候选名称**: Mizmetic 肽的细胞穿透性与胞内靶向效率优化
   - **来源局限/观察**: 本文所有实验均为体外生化实验，未验证 Mizmetic 的细胞穿透性、稳定性和胞内活性。这是从"体外工具"到"细胞工具"的关键一步。
   - **核心假设**: 通过细胞穿透肽（CPP）修饰或脂质偶联，Mizmetic 可被递送入细胞并在胞内浓度下有效干扰 MYC/Miz-1 和 MYC/MAX 互作。
   - **初步方法**: 在 Mizmetic 2/20 的 N 端或 C 端偶联 CPP（如 TAT、penetratin）或脂肪酸链；检测细胞摄取（荧光标记 + 共聚焦）；检测 MYC 靶基因表达和细胞增殖。
   - **验证方式**: 胞内 MYC/Miz-1 互作的邻近连接实验（PLA）或共免疫沉淀；MYC 靶基因表达变化。
   - **可能的失败模式**: 肽在细胞内被降解；或 CPP 修饰影响肽与 MYC 的结合。
   - **创新状态**: unverified

5. **候选名称**: MYC/Miz-1 界面作为相分离调控靶点的计算筛选
   - **来源局限/观察**: 本文仅针对 MYC/Miz-1 一个界面。若将方法扩展到其他 IDP 互作系统，可建立"AI 预测界面 → 肽设计 → 相分离调控"的通用流程。
   - **核心假设**: 许多相分离驱动蛋白的互作界面可被 AlphaFold-Multimer 预测，且这些界面可作为相分离调控的靶点。
   - **初步方法**: 选择 5-10 个已知参与相分离的 IDP 互作对 → AlphaFold-Multimer 预测 → 提取界面肽 → 设计 stapled 肽 → 体外相分离实验验证。
   - **验证方式**: 肽处理后凝聚体形成/解离的定量比较；与已知相分离调控因子的功能比较。
   - **可能的失败模式**: 多数 IDP 互作界面的预测置信度不足；或界面肽无法有效干扰相分离。
   - **创新状态**: unverified