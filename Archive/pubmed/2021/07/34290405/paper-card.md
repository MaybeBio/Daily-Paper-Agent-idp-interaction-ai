## 01 基本信息

- **标题**：Structural basis of human separase regulation by securin and CDK1-cyclin B1
- **作者与单位**：Yu, Jun; Raia, Pierre; Ghent, Chloe M; Raisch, Tobias; Sadian, Yashar; Cavadini, Simone; Sabale, Pramod M; Barford, David; Raunser, Stefan; Morgan, David O; Boland, Andreas（单位未在摘要中提供，部分作者隶属MRC Laboratory of Molecular Biology, University of Geneva, Max Planck Institute of Molecular Physiology 等，具体以原文为准）
- **期刊/预印本平台**：Nature
- **年份**：2021-07-23
- **论文类型**：结构生物学研究论文（cryoEM 结构解析）
- **领域**：细胞周期调控、染色体分离、蛋白酶调控
- **关键词**：separase、securin、CDK1-cyclin B1、cryoEM、pseudosubstrate、有丝分裂、 cohesin
- **DOI/arXiv 号**：10.1038/s41586-021-03764-0
- **代码**：未提供
- **数据**：EMDB EMD-12368（separase-CCC）、EMD-12369（separase-securin）；PDB 7NJ0（separase-CCC）、7NJ1（separase-securin）
- **阅读日期**：2026-04-27
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**：本文核心对象是 separase 的**两个无序插入区（intrinsically disordered inserts）**在结合 securin 或 CDK1-cyclin B1 时发生**无序-有序转变（disorder-to-order transition）**，形成自抑制环（AIL1、AIL2、AIL3）来阻断底物结合。这是 IDR 介导蛋白互作与酶活性调控的经典结构生物学范例，为 IDP/IDR 互作机制研究提供了高分辨率结构模板，但本文未使用 AI/深度学习或 MD 模拟方法。

---

## 02 一句话总结

本文通过 cryoEM 解析了人源 separase 与 securin 及 CDK1-cyclin B1-Cks1 的复合物结构（2.9 Å 和 3.6 Å），发现两种抑制剂均通过**伪底物基序（pseudosubstrate motifs）**占据 separase 的活性位点和底物对接位点；其中 CDK1-cyclin B1 通过诱导 separase 自身三个无序环（AIL1-3）发生无序-有序转变来实现自抑制，揭示了 IDR 在酶调控中的多重机制。

---

## 03 研究问题

- **具体问题**：人源 separase 如何被 securin 和 CDK1-cyclin B1 抑制？其分子机制是什么？
- **为什么重要**：separase 是启动染色体分离（anaphase）的关键蛋白酶，其异常激活导致染色体分离错误和非整倍体。理解其抑制机制对细胞周期调控和癌症研究有直接意义。
- **现有方法为何不足**：此前仅有 C. elegans 和酵母的 separase-securin 结构，人源 separase 的调控机制（尤其是 CDK1-cyclin B1 的抑制方式）缺乏高分辨率结构信息；且 CDK1-cyclin B1 如何抑制 separase 的机制此前完全不清楚。
- **精确的 "Can ... ?" 研究问题**：Can cryoEM 结构解析揭示人源 separase 被 securin 和 CDK1-cyclin B1 抑制的分子机制，包括伪底物基序和自抑制环的具体作用模式？

---

## 04 背景与发展脉络

*注：以下脉络为「经外部核验」的领域发展概述，结合本文引用与领域常识。*

| 阶段 | 代表性工作 | 优点 | 局限 |
|------|-----------|------|------|
| 早期生化鉴定 | 发现 separase 切割 Scc1/Rad21（Uhlmann et al., 1999） | 确立 separase 为 cohesin 蛋白酶 | 无结构信息 |
| 酵母/线虫结构 | C. elegans separase-securin 结构（Boland et al., 2017）；酵母 separase 结构（Luo & Tong, 2017） | 首次揭示 separase 结构域组织和 securin 的伪底物抑制 | 物种差异大，人源特异调控（CDK1-cyclin B1）未覆盖 |
| 人源结构（本文） | 人源 separase-securin 和 separase-CCC 复合物 cryoEM 结构 | 揭示人源特异的三重自抑制环机制和 cyclin B1 磷酸结合口袋 | 静态结构，缺乏动态信息 |
| 后续方向 | 单分子动力学、AI 预测（AlphaFold）辅助的构象分析 | 可补充动态和能量信息 | 尚未在 separase 体系充分应用 |

**本文主张的位置**：首次提供人源 separase 与两种关键调控因子（securin 和 CDK1-cyclin B1）的复合物结构，揭示 CDK1-cyclin B1 通过诱导 separase 自身 IDR 折叠为自抑制环来抑制其活性，这是此前未知的调控范式。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 人源 separase 结构缺失 | 无法解释人源特异调控机制 | 人源 separase 大（~230 kDa）、柔性高，难以结晶 | 作者使用 cryoEM 而非晶体学（Abstract；Methods） |
| CDK1-cyclin B1 抑制机制不明 | 已知 CDK1 磷酸化 separase 促进抑制，但机制不清 | 缺乏复合物结构 | 本文首次解析 separase-CCC 复合物结构（Abstract；Fig. 3） |
| separase 无序区功能未知 | 两个大的无序插入区（insert 1、insert 2）功能不明 | 无序区难以在结构中观察 | 作者发现这些区域在结合 CDK1-cyclin B1 后折叠为有序结构（Fig. 2；Extended Data Fig. 7） |
| 体外重组 separase-CCC 复合物困难 | 复合物不稳定、组装依赖磷酸化 | 需要 securin 融合策略和 ATP | 作者使用 securinΔ160-separaseC2029S 融合蛋白（Methods；Extended Data Fig. 1a, 2a, b） |

---

## 06 核心思想

### 1) 表面方法
- 使用 cryoEM 解析两个复合物的结构：separase-securin（2.9 Å）和 separase-CCC（3.6 Å）
- 通过 securin 融合策略稳定 separase-CCC 复合物
- 结合生化实验（切割实验、突变分析）验证结构观察

### 2) 核心洞察
- **伪底物抑制的普适性**：securin 和 CDK1-cyclin B1 都通过伪底物基序（EIExxΦ、NPLDFE、LPE 等）占据 separase 的底物结合位点
- **IDR 的自抑制功能**：CDK1-cyclin B1 结合后，separase 自身的两个无序插入区折叠为三个自抑制环（AIL1、AIL2、AIL3），其中 AIL3 同时抑制 separase 和 CDK1 的活性位点
- **磷酸化驱动的组装**：separase 的 Ser1126 磷酸化后与 cyclin B1 的磷酸结合口袋互作，是复合物组装的关键
- **协同抑制**：CDK1-cyclin B1 通过"双重打击"（同时抑制 separase 和 CDK1 活性）实现强效抑制

### 3) 可能的普适教训 [Analysis]
- **IDR 是"可编程"的调控元件**：同一段无序序列在不同结合伙伴存在时可折叠为不同结构，实现多功能调控。这对 IDP/IDR 互作研究有直接启示——IDR 的调控功能可能被严重低估。
- **伪底物基序是酶抑制的通用策略**：从病毒蛋白酶抑制剂到细胞周期调控，伪底物策略广泛存在。在 AI 辅助的抑制剂设计中，识别伪底物基序可作为起点。
- **磷酸化开关与 IDR 折叠耦合**：磷酸化修饰可触发 IDR 折叠，这一机制在相分离领域同样重要（如磷酸化调控凝聚体形成）。

---

## 07 方法总览

- **输入**：重组表达的人源 separase、securin、CDK1-cyclin B1-Cks1 蛋白
- **输出**：两个复合物的原子模型（PDB 7NJ0, 7NJ1）
- **模块**：
  1. 蛋白表达与纯化（昆虫细胞/大肠杆菌系统）
  2. 复合物组装（securin 融合策略 + ATP 依赖的磷酸化）
  3. cryoEM 数据采集（Titan Krios + K3 相机）
  4. 图像处理（MotionCorr2, CTFFIND4, crYOLO, RELION, CryoSPARC）
  5. 模型构建与精修（PHENIX, Coot, Flex-EM）
  6. 生化验证（切割实验、突变分析）
- **训练**：不适用（无机器学习训练）
- **工具**：cryoEM 相关软件套件（详见 Methods）
- **反馈回路**：结构观察 → 设计突变 → 生化验证 → 修正模型
- **文字流程**：表达纯化 separase-securin 复合物 → cryoEM 数据采集与处理 → 获得 2.9 Å 结构 → 用 securin 融合策略组装 separase-CCC 复合物 → 获得 3.6 Å 结构 → 分析互作界面和伪底物基序 → 设计突变体验证功能 → 提出抑制机制模型

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| securin 融合策略 | 稳定 separase-CCC 复合物 | separase 与 CDK1-cyclin B1 亲和力低，复合物不稳定 | 输入：securin 片段（160-202）+ separase 融合蛋白；输出：稳定的复合物 | Extended Data Fig. 1a；Methods | 预期影响：无法获得复合物结构（作者明确说明该策略是必需的） |
| cryoEM 单颗粒分析 | 获得复合物三维结构 | separase 大且柔性高，不适合晶体学 | 输入：冷冻电镜图像；输出：3D 密度图 | Abstract；Methods | 预期影响：无法获得高分辨率结构信息 |
| 聚焦精修（focused refinement） | 提高 TPR 和蛋白酶结构域分辨率 | 整体结构分辨率受柔性 N 端限制 | 输入：整体精修后的粒子；输出：局部优化密度图 | Methods（"focused 3D refinement"） | 预期影响：关键互作界面分辨率不足 |
| 伪底物基序分析 | 识别抑制性互作的关键序列 | 理解抑制机制的核心 | 输入：结构模型；输出：基序序列和互作残基 | Fig. 2a-e；Extended Data Fig. 7 | 预期影响：无法解释抑制机制 |
| 切割实验 | 验证结构观察的功能意义 | 结构需要功能验证 | 输入：野生型/突变体 separase + 底物；输出：切割效率 | Fig. 2f, g；Extended Data Fig. 9, 10 | 预期影响：结构结论缺乏功能支持 |
| 磷酸化位点分析 | 确认 Ser1126 磷酸化在复合物组装中的作用 | 磷酸化是复合物组装的先决条件 | 输入：质谱数据 + 结构；输出：磷酸化位点定位 | Extended Data Fig. 2c, d；Fig. 3a | 预期影响：无法解释 ATP 依赖性 |

---

## 09 关键公式符号

**不适用**。本文为结构生物学研究，未使用定量公式或数学模型。核心"符号"为结构基序命名：

- **EIExxΦ**：securin 中的伪底物基序（E=Glu, I=Ile, Φ=疏水残基），结合 separase 活性位点
- **NPLDFE**：securin 中的 NxLxΦE 基序（残基 121-126），结合 separase 的 TPR-蛋白酶结构域间 cleft
- **NxLxΦE**：保守的 α-螺旋基序，存在于 securin（NPLDFE）、separase AIL1（NDLNYE）和底物 Scc1（NHLEYE）
- **APxxxxR**：CDK 抑制基序，位于 separase AIL3 中，模拟 CDK 底物
- **AIL1/AIL2/AIL3**：separase 的三个自抑制环（autoinhibitory loops）

---

## 10 实验设计与证据链

**数据集/群体**：
- 人源 separase（全长 1-2120）
- 人源 securin（全长 1-202 及截短体）
- CDK1-cyclin B1-Cks1 复合物
- 底物 Scc1（人源，残基 142-300 及全长）

**指标**：cryoEM 分辨率（2.9 Å / 3.6 Å）、切割效率（放射性标记底物）

**基线/对照**：野生型 vs 突变体；有/无 CDK1-cyclin B1

**预算**：未提供

**骨干/仪器**：Titan Krios（Thermo Fisher Scientific），K3 相机（Gatan）

**oracle 输入**：不适用

**评测协议**：体外切割实验、pull-down 结合实验

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|-----------------|------|
| cryoEM 结构解析（separase-securin） | securin 通过伪底物基序抑制 separase | 无对照（结构解析） | 2.9 Å 结构显示 EIExxΦ 和 NPLDFE 基序占据活性位点和 cleft | securin 的伪底物抑制机制 | 无法直接证明动态过程 | Abstract；Fig. 2 |
| cryoEM 结构解析（separase-CCC） | CDK1-cyclin B1 诱导 separase 自抑制环折叠 | 无对照（结构解析） | 3.6 Å 结构显示 AIL1-3 折叠并阻断底物结合 | CDK1-cyclin B1 通过诱导 IDR 折叠抑制 separase | 静态结构无法证明折叠动力学 | Abstract；Fig. 2, 3 |
| Scc1 切割实验（NHLEYE 突变） | NHLEYE 基序对底物识别重要 | 野生型 vs ΔNHLEYE | 删除 NHLEYE 后切割效率显著降低 | NHLEYE 是底物对接基序 | 未测试所有残基贡献 | Fig. 2f；Extended Data Fig. 9a |
| Scc1 切割实验（linker 删除） | linker 长度对底物切割重要 | 野生型 vs linker 删除/替换 | linker 删除或随机替换后切割消失 | linker 提供必需的柔性连接 | 未系统扫描 linker 长度 | Extended Data Fig. 9c |
| separase AIL 删除突变 | AIL 在自抑制中起作用 | 野生型 vs ΔAIL1/ΔAIL3 | 删除 AIL 后切割活性升高，对 CDK1-cyclin B1 抑制的抵抗增强 | AIL 介导自抑制 | 未测试 AIL2 单独效应 | Fig. 2g；Extended Data Fig. 10 |
| pull-down 实验 | securin 疏水段介导高亲和结合 | 全长 securin vs 截短体 | 删除疏水段（136-146）后结合减弱 | 疏水段对高亲和结合必需 | 未做定量结合常数 | Extended Data Fig. 11 |
| 磷酸化位点分析 | Ser1126 磷酸化驱动复合物组装 | 质谱检测 | 检测到 Ser1126 磷酸化 | Ser1126 是复合物组装的关键磷酸化位点 | 未做磷酸化位点突变的功能实验 | Extended Data Fig. 2c, d |

---

## 11 结论正确解读

- **任务范围**：本文仅解析了 separase 与 securin 和 CDK1-cyclin B1 的复合物结构，未涉及 separase 与其他调控因子（如 Sgo2-Mad2）的复合物结构。
- **oracle/真值输入**：结构模型基于 cryoEM 密度图构建，分辨率 2.9-3.6 Å，侧链密度在核心区域清晰，但 N 端结构域和部分无序区密度较弱。
- **端到端状态**：从蛋白表达、复合物组装到结构解析和功能验证是完整的，但未进行体内功能实验（如细胞实验验证突变体的表型）。
- **算力成本**：未提供。
- **历史数据依赖**：结构建模参考了 C. elegans separase-securin 结构（PDB 5MZ6）和 CDK2-cyclin A 结构（PDB 2CCI, 4YC3）。
- **模型依赖**：结构模型依赖 cryoEM 数据处理软件（RELION, CryoSPARC）和建模软件（PHENIX, Coot），不同软件版本可能影响细节。
- **最难情形**：separase 的 N 端 HEAT 重复结构域柔性高，密度模糊；AIL3 的部分区域在复合物中仍为无序。
- **群体/领域边界**：结论基于体外重组蛋白，未在细胞或体内验证；物种特异性（人源 vs 其他物种）未系统比较。
- **不确定性**：Ser1126 磷酸化与 cyclin B1 结合的精确贡献未通过突变实验直接验证；CDK1 活性位点被 AIL3 抑制的机制基于结构推断，未做激酶活性实验。

**有边界的复述**：本文通过 cryoEM 结构解析，证明人源 separase 被 securin 和 CDK1-cyclin B1 抑制的分子基础是伪底物基序占据底物结合位点，其中 CDK1-cyclin B1 通过诱导 separase 自身无序区折叠为自抑制环来实现抑制。该结论基于体外重组蛋白的结构和生化实验，未在体内验证。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| N 端结构域分辨率有限 | HEAT 重复结构域密度模糊，无法构建完整原子模型 | 未明确提及 | Methods（"less well-defined due to its inherent flexibility"） |
| AIL3 部分区域仍无序 | 在 separase-CCC 复合物中 AIL3 的某些残基无清晰密度 | 未明确提及 | Fig. 2；Extended Data Fig. 7 |
| 未直接验证 Ser1126 磷酸化的功能贡献 | 结构显示磷酸化位点，但未做磷酸化位点突变的功能实验 | 未明确提及 | Extended Data Fig. 2c, d |
| 未研究 Sgo2-Mad2 复合物的抑制机制 | 仅讨论 securin 和 CDK1-cyclin B1 | 提出需要详细结构分析 | Discussion（"detailed structural analysis will be required"） |
| 体外重组系统 | 未在细胞或体内验证 | 未明确提及 | Methods |

**作者提及的相关约束**（非正式局限）：
- CDK1-cyclin B1 对 separase 的抑制需要 ATP 和磷酸化，体外重组系统可能无法完全模拟体内磷酸化状态。
- securin 融合策略可能影响 separase 的天然构象。

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 复合物组装依赖 securin 融合策略 | 融合蛋白可能引入人为构象，不代表天然状态下 separase 与 CDK1-cyclin B1 的互作方式 | 如果融合策略改变了互作界面，结构结论可能不适用于天然状态 | 使用非融合策略（如化学交联或纳米抗体辅助）验证复合物结构 | Methods（"required the fusion of a short C-terminal segment of securin"） |
| Ser1126 磷酸化位点的功能贡献未直接验证 | 结构显示磷酸化与 cyclin B1 口袋互作，但未做 S1126A 突变的功能实验 | 如果磷酸化不是复合物组装的必要条件，模型需要修正 | 构建 S1126A 突变体，检测复合物组装和 separase 活性 | Extended Data Fig. 2c, d；Fig. 3a |
| 静态结构无法证明 IDR 折叠的动态过程 | 作者提出"无序-有序转变"是抑制机制，但 cryoEM 只提供终态结构 | IDR 的动态行为可能是调控的关键，静态结构可能高估或低估某些互作的贡献 | 使用 NMR、HDX-MS 或 MD 模拟研究 IDR 折叠动力学 | Fig. 2；Discussion |
| 体外切割实验条件可能不反映体内环境 | 使用重组蛋白和人工底物，缺乏细胞环境中的辅助因子 | 体内可能有其他因子增强或减弱 separase 活性 | 在细胞中敲低/过表达 separase 突变体，检测染色体分离表型 | Fig. 2f, g；Methods |
| 物种特异性未系统讨论 | 作者指出 AIL 保守性仅限脊椎动物，但未深入分析 | 如果 CDK1-cyclin B1 调控是脊椎动物特异的，模式生物研究可能不适用 | 比较不同物种的 separase 序列和结构 | Discussion（"conserved only in vertebrates"） |

---

## 14 Agent 提炼的知识候选

**面向课题方向（IDP/IDR × 蛋白互作 × AI/物理模拟）的可迁移知识：**

1. **IDR 伪底物基序作为抑制性互作模块**：本文展示了 IDR 中的短线性基序（如 EIExxΦ、NPLDFE）如何通过模拟底物来竞争性抑制酶活性。在 IDP/IDR 互作研究中，可系统搜索这类"伪底物基序"作为候选互作位点。**可迁移方法**：使用 AI 工具（如 ELM、MoRFpred）扫描 IDR 中的潜在伪底物基序，结合结构信息预测抑制性互作。

2. **无序-有序转变作为互作开关**：separase 的 AIL1-3 在无 CDK1-cyclin B1 时无序，结合后折叠为有序结构。这提示 IDR 的折叠转变是互作调控的普遍机制。**可迁移方法**：在相分离研究中，可关注 IDR 折叠转变如何驱动凝聚体形成或解散；在 AI 预测中，可使用 AlphaFold 或 MD 模拟预测 IDR 结合后的构象。

3. **磷酸化与 IDR 折叠的耦合**：Ser1126 磷酸化是复合物组装的先决条件，磷酸化位点位于 IDR 中。**可迁移方法**：在 IDP/IDR 互作预测中，将磷酸化状态作为关键特征输入；在 MD 模拟中，模拟磷酸化修饰对 IDR 构象的影响。

4. **多价互作与协同抑制**：securin 通过多个基序同时占据 separase 的多个位点，CDK1-cyclin B1 也通过多个界面协同抑制。**可迁移方法**：在相分离研究中，多价互作是凝聚体形成的关键驱动力；可借鉴本文的多位点互作分析框架。

5. **cryoEM 解析 IDR 复合物的策略**：本文展示了如何通过融合策略和聚焦精修处理含大段 IDR 的复合物。**可迁移方法**：对 IDP/IDR 复合物的结构研究，可参考其样品制备和数据处理策略。

6. **结构-功能验证闭环**：结构观察 → 突变设计 → 功能验证的闭环是研究 IDR 功能的有效范式。**可迁移方法**：在 AI 预测的 IDR 互作位点验证中，采用类似的突变-功能验证策略。

---

## 15 与已有知识连接

- **C. elegans separase-securin 结构**（Boland et al., 2017, Nature）：本文直接对比了人源和线虫的 separase 抑制机制，发现伪底物基序策略保守，但具体基序序列和位置有差异。
- **酵母 separase 结构**（Luo & Tong, 2017, Nature）：酵母 separase 的 N 端结构域更紧凑，人源有更大的无序插入区，提示调控复杂性增加。
- **CDK-cyclin 底物识别**（Brown et al., 1999; 综述见 Malumbres, 2014）：本文发现的 APxxxxR 伪底物基序与 CDK 底物识别的共识基序一致，扩展了 CDK 抑制机制的理解。
- **IDR 在细胞周期调控中的作用**（综述见 Wright & Dyson, 2015）：本文为 IDR 在酶活性调控中的直接作用提供了结构证据。
- **伪底物抑制策略**（如 p27 抑制 CDK2，Russo et al., 1996）：本文的发现与 p27 抑制 CDK 的机制类似，但作用于相反方向（CDK1-cyclin B1 抑制 separase，而非被抑制）。
- **无序蛋白与相分离**（综述见 Banani et al., 2017）：本文的 IDR 折叠转变机制与相分离中的 IDR 构象变化有潜在联系，但本文未涉及相分离。

---

## 16 Agent 生成的研究候选

### 候选 1：IDR 伪底物基序的 AI 预测工具
- **来源局限/观察**：本文发现 separase 的 IDR 中多个短线性基序（AIL1-3）介导抑制性互作，但现有基序预测工具（如 ELM）未针对"伪底物"场景优化。
- **核心假设**：IDR 中的伪底物基序具有可识别的序列特征（如与已知底物基序的相似性、疏水模式、磷酸化位点邻近性），可通过机器学习从已知伪底物基序中学习。
- **相对本文的增量**：将本文的结构-功能数据转化为训练集，开发专门预测 IDR 伪底物基序的工具。
- **初步方法**：收集已知伪底物基序（separase-securin、p27-CDK2 等），提取序列和结构特征，训练分类器（如随机森林或深度学习），在 proteome-wide 扫描候选伪底物基序。
- **验证方式**：用实验验证预测的伪底物基序是否具有抑制功能（如体外结合和酶活实验）。
- **可能的失败模式**：伪底物基序可能过于多样化，序列特征不足以泛化；需要结构信息辅助。

### 候选 2：磷酸化触发的 IDR 折叠转变的 MD 模拟
- **来源局限/观察**：本文提出 Ser1126 磷酸化驱动 insert 1 折叠并包裹 cyclin B1，但未提供动态证据。
- **核心假设**：磷酸化修饰显著改变 IDR 的构象 ensemble，促进折叠和结合。
- **相对本文的增量**：用 MD 模拟补充结构的动态信息，揭示磷酸化如何改变 IDR 的自由能景观。
- **初步方法**：对 separase insert 1（残基 1065-1152）进行增强采样 MD（如 replica exchange），比较未磷酸化/磷酸化状态的构象 ensemble；用 Markov state model 分析折叠路径。
- **验证方式**：模拟预测的磷酸化依赖构象变化可用 NMR 或 HDX-MS 验证。
- **可能的失败模式**：IDR 模拟的力场准确性有限；磷酸化参数化可能引入偏差。

### 候选 3：IDR 介导的多价互作与相分离的关联分析
- **来源局限/观察**：本文展示了 separase 通过多个 IDR 基序与不同伙伴互作，这种多价互作是相分离的典型特征。
- **核心假设**：细胞周期调控中的 IDR 介导多价互作可能形成瞬时凝聚体，协调下游事件。
- **相对本文的增量**：将 separase 的调控机制与相分离框架连接，提出可检验的预测。
- **初步方法**：分析 separase 及其互作伙伴（securin、CDK1-cyclin B1）的 IDR 序列特征（如电荷模式、疏水簇），预测相分离倾向；在细胞中检测 separase 是否形成凝聚体。
- **验证方式**：体外相分离实验（浊度、FRAP）+ 细胞成像。
- **可能的失败模式**：separase 可能不形成凝聚体，多价互作仅用于增强亲和力而非相分离。

### 候选 4：基于 AlphaFold 的 IDR 复合物构象预测
- **来源局限/观察**：本文的 cryoEM 结构显示 IDR 折叠后的构象，但 AlphaFold 对 IDR 的预测通常不可靠。
- **核心假设**：结合实验约束（如交联质谱、突变数据）可显著改善 AlphaFold 对 IDR 复合物的预测。
- **相对本文的增量**：开发将实验约束整合到 AlphaFold 预测的流程，用于 IDR 复合物结构预测。
- **初步方法**：使用 AlphaFold-Metainference 或 AF2 的约束模式，输入本文的交联/突变数据，预测 separase-CCC 复合物构象。
- **验证方式**：与 cryoEM 结构对比，评估预测精度。
- **可能的失败模式**：IDR 的构象多样性可能超出 AlphaFold 的表示能力；约束不足时预测不可靠。

### 候选 5：伪底物基序在蛋白酶抑制剂设计中的应用
- **来源局限/观察**：本文揭示了伪底物基序如何高效抑制 separase，这种策略可推广到其他蛋白酶。
- **核心假设**：从天然伪底物基序出发，通过序列优化可设计高亲和力的肽类抑制剂。
- **相对本文的增量**：将结构信息转化为抑制剂设计原则。
- **初步方法**：基于 separase-securin 结构，设计伪底物肽库，用噬菌体展示或 mRNA display 筛选高亲和力变体。
- **验证方式**：体外抑制实验 + 细胞实验。
- **可能的失败模式**：肽类抑制剂的细胞通透性差；伪底物基序的优化空间有限。