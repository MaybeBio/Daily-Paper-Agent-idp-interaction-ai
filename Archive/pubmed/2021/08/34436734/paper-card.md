## 01 基本信息
- **标题**: The (1)H, (15)N and (13)C resonance assignments of the C-terminal domain of Serpine mRNA binding protein 1 (SERBP1)
- **作者**: Baudin, Antoine; Xu, Xiaoping; Libich, David S
- **单位**: 未提供（根据基金信息推测为 University of Texas Health Science Center at San Antonio / Greehey Children's Cancer Research Institute）
- **期刊/平台**: Biomolecular NMR Assignments
- **年份**: 2021-08-27（在线发表）
- **论文类型**: 核磁共振波谱学数据报告（resonance assignments 论文）
- **领域**: 结构生物学 / NMR 波谱学 / 无序蛋白
- **关键词**: SERBP1, intrinsically disordered protein, NMR resonance assignment, RNA-binding protein, α-helix
- **DOI/arXiv**: 10.1007/s12104-021-10046-3
- **代码**: 未提供（NMRPipe 处理脚本可按合理请求提供）
- **数据**: BMRB Accession # 50953；质粒 Addgene # 172315
- **阅读日期**: 2026-05-13（按当前日期）
- **在该方向中的位置**: 本文是 IDP/IDR 结构生物学的基础数据报告，为 SERBP1 这一无经典 RNA 结合结构域、富含无序区的 mRNA 结合蛋白提供 backbone 化学位移赋值和二级结构预测。对「IDP/IDR × 蛋白互作 × AI/物理模拟」课题而言，本文提供了：(1) 一个 IDP 体系的高质量 NMR 实验数据（可用于训练/验证化学位移预测或二级结构预测模型）；(2) 一个「无序蛋白中存在稳定 α-helix」的实例，提示 IDP 的局部有序结构可能是分子识别的关键位点。

## 02 一句话总结
本文通过溶液态 NMR 三共振实验，对 SERBP1 的 C 端无序结构域（残基 189–400）完成了 93% 的 backbone 化学位移赋值，并利用化学位移数据预测出 289–298 区域存在一个稳定的 α-helix，表明该「无序」蛋白并非完全无结构。

## 03 研究问题
- **具体问题**: SERBP1 缺乏经典 RNA 结合结构域（如 RRM、锌指），其如何识别并结合 mRNA 靶标的分子机制尚不清楚。本文作为该长期研究的第一步，旨在为 SERBP1 C 端结构域提供 backbone 共振赋值，并初步评估其二级结构倾向。
- **为什么重要**: SERBP1 参与血栓形成、DNA 损伤修复、营养缺乏响应等多种生物学过程，且在多种癌症中高表达并与不良预后相关。理解其 RNA 识别机制对癌症治疗和基础 RNA 生物学均有意义。
- **现有方法为何不足**: SERBP1 被预测为 intrinsically disordered，传统晶体学难以获得其高分辨率结构；而缺乏 backbone 化学位移赋值则无法进行后续的 NMR 结构计算、动力学分析或与 RNA 互作的化学位移扰动实验。
- **精确的 Can 问题**: Can NMR backbone chemical shift assignments reveal the presence of transient secondary structure elements within the intrinsically disordered C-terminal domain of SERBP1?

## 04 背景与发展脉络
*注：此脉络为「经外部核验」的领域发展框架，结合本文引用与 IDP 领域通用知识。*

1. **阶段一：IDP 的发现与「序列-结构-功能」范式挑战（1990s–2000s）**
   - 代表方法：CD 光谱、SAXS、NMR 化学位移
   - 优点：证明许多蛋白在生理条件下无稳定三维结构但仍具功能
   - 局限：IDP 的构象异质性使高分辨率结构解析困难
   - 代表文献：Dunker et al., Wright & Dyson 系列工作

2. **阶段二：IDP 的 NMR 表征方法学成熟（2000s–2010s）**
   - 代表方法：三共振实验（HNCO, HNCACO, CBCACONH, HNCACB）、NUS 采样、SMILE 重建
   - 优点：可在近生理条件下获得残基级分辨率的结构和动力学信息
   - 局限：需要高表达、高稳定性样品；谱峰重叠严重时赋值困难
   - 代表文献：Grzesiek & Bax 1992; Yamazaki et al. 1994; Delaglio et al. 2017

3. **阶段三：IDP 中局部有序结构的识别与功能关联（2010s–至今）**
   - 代表方法：化学位移-based 二级结构预测（如 SSP, δ2D）、MD 模拟、AI 预测（AlphaFold 对 IDP 的局限与改进）
   - 优点：揭示 IDP 中 transient helix / pre-structured motifs 可能是分子识别的成核位点
   - 局限：化学位移预测的准确性依赖经验数据库；局部有序结构的生物学意义需功能实验验证
   - 代表文献：Marsh et al. 2006; Kjaergaard & Poulsen 2011

4. **本文位置**: 处于阶段二向阶段三过渡——提供 SERBP1 C 端结构域的 NMR 赋值数据，并用两种独立方法（secondary chemical shift 和 SSP）识别出一个稳定的 α-helix（289–298），为后续研究该 helix 是否参与 RNA 识别奠定基础。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| SERBP1 缺乏经典 RNA 结合结构域 | 无法用已知 RNA 结合 motif 预测其靶标识别机制 | 作者指出 SERBP1 不含 RRM 或锌指，其识别机制可能非常规 | Abstract; Biological context 节 |
| 蛋白稳定性差 | 初始 189–408 构建体 C 端 8 个残基系统性降解 | 作者通过质谱和初始 NMR 谱发现降解，推测为蛋白酶敏感区 | Assignment and data deposition 节 |
| IDP 的 NMR 谱峰重叠 | 15 个残基无法唯一赋值，其中 13 个位于 RGG 重复区 | RGG 重复序列高度简并，导致化学位移简并和谱峰重叠 | Assignment and data deposition 节 |
| 弱峰/低强度峰 | 4 个峰强度低于其他峰的 10%，无法从 3D 谱中找到对应自旋系统 | 可能来自克隆 scar 或慢构象交换过程 | Assignment and data deposition 节 |

## 06 核心思想
1. **表面方法**: 表达纯化 SERBP1 189–400 构建体，采集 2D ¹H-¹⁵N HSQC 和 3D 三共振谱（HNCO, HNCACO, CBCACONH, HNCACB, HNHA），完成 backbone 化学位移赋值，并用两种独立方法预测二级结构。

2. **核心洞察**: 一个被预测为 intrinsically disordered 的蛋白，其 C 端结构域并非完全无结构——化学位移数据明确显示 289–298 区域存在稳定的 α-helix。这一「无序中的有序」可能是 SERBP1 识别 RNA 的结构基础。

3. **可能的普适教训** [Analysis]: 对 IDP/IDR 研究而言，NMR 化学位移赋值不仅是结构解析的「前奏」，其本身就能提供重要的结构信息——即使无法获得完整三维结构，残基级的二级结构倾向数据已足以识别功能相关的局部有序元件。对于 AI/深度学习方向，这类高质量 NMR 赋值数据是训练化学位移预测模型（如 SPARTA+, ShiftX2）和验证 IDP 构象系综预测的宝贵实验基准。

## 07 方法总览
- **输入**: 重组表达的 ¹⁵N 或 ¹³C/¹⁵N 双标记 SERBP1 189–400 蛋白样品（80–100 μM，20 mM Na₂HPO₄ pH 7.0, 60 mM NaCl, 1 mM PMSF, 0.2 mM EDTA, 10% D₂O）
- **输出**: ¹H, ¹⁵N, ¹³Cα, ¹³Cβ, ¹³C' backbone 化学位移赋值（BMRB # 50953）；二级结构预测（Fig. 2）
- **模块**:
  1. 基因构建与蛋白表达（大肠杆菌 BL21(DE3) Star，M9 培养基，¹⁵NH₄Cl / ¹³C₆-glucose 标记）
  2. 蛋白纯化（HisTrap HP 亲和层析 + TEV 酶切 + 反相 Ni 柱 + Superdex 75 16/60 凝胶过滤）
  3. NMR 数据采集（Bruker NEO 700 MHz，TCI 低温探头，NUS 采样 15%）
  4. 数据处理与赋值（NMRPipe + SMILE 重建，CCPNMR Analysis 2.5）
  5. 二级结构预测（secondary chemical shift 法 + SSP 程序）
- **反馈回路**: 初始 189–408 构建体不稳定 → 缩短为 189–400 → 稳定性显著提高
- **假设**: 蛋白在 NMR 实验条件下（278 K, pH 7.0）保持天然构象状态；化学位移赋值可反映蛋白的构象倾向

**文字流程**: 基因合成 → 克隆至表达载体 → 大肠杆菌表达（同位素标记）→ 两步亲和纯化 + 凝胶过滤 → NMR 样品制备 → 采集 HSQC 及 5 个 3D 三共振谱 → 谱图处理（NMRPipe/SMILE）→ 顺序赋值 → 化学位移分析 → 二级结构预测 → 数据存入 BMRB

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 构建体设计（189–400） | 截短 C 端结构域，去除不稳定区域 | 189–408 构建体 C 端 8 残基降解，影响样品稳定性 | 输入：序列比对结果；输出：稳定表达的截短构建体 | Assignment and data deposition 节 | 预期影响：若保留 189–408，蛋白降解导致 NMR 谱质量差，无法完成赋值 |
| 同位素标记表达 | 获得 ¹⁵N/¹³C 标记蛋白 | 三共振实验需要同位素标记 | 输入：M9 培养基 + 标记底物；输出：双标记蛋白 | Methods: Protein expression 节 | 预期影响：无法进行异核多维 NMR 实验 |
| 三共振 NMR 实验套件 | 获得 backbone 化学位移 | 顺序赋值需要多个实验的关联信息 | 输入：标记蛋白样品；输出：HNCO, HNCACO, CBCACONH, HNCACB, HNHA 谱 | Methods: NMR experiments 节 | 预期影响：缺少任一实验将降低赋值确定性，尤其 HNCA 类实验对 proline 前残基的赋值至关重要 |
| NUS + SMILE 重建 | 缩短采集时间同时保持分辨率 | 3D 实验全采样时间过长 | 输入：15% NUS 数据；输出：重建后的完整谱 | Methods: NMR experiments 节 | 预期影响：全采样时间增加 6-7 倍，或分辨率下降导致简并峰无法分辨 |
| 二级结构预测（Δδ + SSP） | 从化学位移推断二级结构倾向 | 化学位移对局部构象敏感 | 输入：¹³Cα, ¹³Cβ 化学位移；输出：Δδ 图和 SSP score | Results: Fig. 2 | 预期影响：无法识别 289–298 的 α-helix，结论变为「完全无序」 |

## 09 关键公式符号
**不适用** — 本文为 NMR 赋值数据报告，无数学公式。核心分析基于以下经验关系：

- **Secondary chemical shift**: Δδ¹³Cα = δ¹³Cα(observed) − δ¹³Cα(random coil)，正值 > 1 ppm 指示 α-helix 倾向
- **SSP score**: 基于化学位移加权组合的二级结构评分，范围 −1（β-strand）到 +1（α-helix），|score| > 0.5 表示显著倾向

## 10 实验设计与证据链
- **数据集/群体**: 单个蛋白构建体（SERBP1 189–400），两种同位素标记样品（¹⁵N 单标记用于 HNHA；¹³C/¹⁵N 双标记用于三共振实验）
- **规模**: 203 个预期 backbone 峰（189–400 含 9 个 proline），成功赋值 188 个（93%）
- **指标**: 赋值完成率（93% ¹H-¹⁵N, 93% ¹³Cα, 96% ¹³Cβ, 93% ¹³C', 80% ¹Hα）；SSP score
- **基线**: 无（赋值论文通常无对照实验）
- **预算/资源**: 单台 Bruker NEO 700 MHz 谱仪，配备 TCI 低温探头
- **oracle 输入**: 不适用
- **评测协议**: 无标准 benchmark；赋值可靠性通过 3D 实验间交叉验证

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|----------------|------|
| 2D ¹H-¹⁵N HSQC | 蛋白是否可溶、是否折叠 | 80 μM, 278 K, pH 7.0 | 观察到 203 个预期峰中的 188 个，谱峰分散度低 | 蛋白主要为无序构象 | 无法排除部分区域存在有序结构 | Fig. 1 |
| 3D 三共振实验套件 | 能否完成顺序赋值 | HNCO, HNCACO, CBCACONH, HNCACB, HNHA | 188/203 残基完成赋值 | 蛋白适合 NMR 研究 | 15 个残基（主要为 RGG 区）无法赋值 | Assignment and data deposition 节 |
| Secondary chemical shift 分析 | 是否存在二级结构倾向 | Δδ¹³Cα − Δδ¹³Cβ vs. random coil | 289–299 区域 Δδ > 3 ppm | 该区域形成稳定 α-helix | 无法确定 helix 的精确边界和稳定性 | Fig. 2A |
| SSP 分析 | 交叉验证 helix 预测 | SSP score vs. 化学位移 | 289–298 区域 score > 0.7 | 独立方法确认 α-helix 存在 | 无法确定 helix 是否在 RNA 结合时构象改变 | Fig. 2B |

## 11 结论正确解读
- **任务范围**: 本文仅报告 backbone 化学位移赋值和二级结构预测，不涉及功能实验、RNA 结合实验或完整结构解析。
- **oracle/真值输入**: 化学位移赋值基于 NMR 实验数据，无外部真值；二级结构预测基于经验化学位移数据库。
- **端到端状态**: 非端到端——本文是长期结构生物学研究的第一步，后续需进行 RNA 滴定实验、动力学测量和结构计算。
- **算力成本**: 低（NMR 数据处理和 SSP 分析计算量小）。
- **历史数据依赖**: 二级结构预测依赖 random coil 化学位移数据库（Kjaergaard & Poulsen 2011）和 SSP 训练数据。
- **模型依赖**: SSP 程序基于经验化学位移-结构关系；不同预测程序可能给出略有差异的结果。
- **最难情形**: RGG 重复区（369–381）因序列简并和谱峰重叠无法赋值，该区域恰好是可能的 RNA 结合位点。
- **群体/领域边界**: 结论仅适用于 SERBP1 189–400 在 278 K、pH 7.0 条件下的构象状态；不能外推至全长蛋白或其他条件。
- **不确定性**: 15 个未赋值残基的构象状态未知；α-helix 的群体比例（population）未定量；helix 的生物学意义未验证。
- **有边界的复述**: 在 278 K、pH 7.0 条件下，SERBP1 189–400 的 backbone 化学位移赋值完成 93%，化学位移分析表明 289–298 区域存在稳定的 α-helix，其余区域主要为无序构象；该 helix 是否参与 RNA 识别尚待功能实验验证。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 部分残基无法赋值 | 15 个峰未赋值，其中 13 个位于 RGG 重复区（369–381） | 作者提出可考虑突变策略（"We consider mutagenesis as a possible strategy"）来解决 RGG 区的赋值问题 | Assignment and data deposition 节 |
| 初始构建体不稳定 | 189–408 构建体 C 端 8 残基降解 | 设计更短的 189–400 构建体 | Assignment and data deposition 节 |
| 未涉及功能验证 | 未进行 RNA 结合实验 | 本文定位为「第一步」（"first step toward understanding the structural basis"） | Abstract |

*作者提及的相关约束（非正式局限）*: 实验在单一温度（278 K）和单一 pH（7.0）条件下进行；未进行 ¹⁵N 弛豫或 RDC 等动力学/取向测量。

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| α-helix 的判定仅基于化学位移 | 化学位移预测的 helix 可能是 transient 而非稳定折叠；不同预测方法（Δδ vs. SSP）虽一致，但均基于同一套化学位移数据，非独立验证 | 若 helix 是 transient 的，其功能意义可能与稳定 helix 完全不同 | 进行 ¹⁵N 弛豫实验（R₁, R₂, NOE）或 CPMG 弛豫弥散实验测量 helix 区域的构象动力学；或进行 MD 模拟验证 helix 的稳定性 | Fig. 2; Methods |
| 未赋值残基集中在 RGG 区 | RGG 区恰是可能的 RNA 结合位点，无法赋值意味着关键功能区域的结构信息缺失 | 若 RGG 区参与 RNA 识别，则本文提供的结构信息不足以支撑功能机制研究 | 尝试不同 pH/温度条件改善谱峰分离；或采用 ¹³C 直接检测实验；或对 RGG 区进行选择性标记 | Assignment and data deposition 节 |
| 构建体截短可能改变构象 | 189–400 截短体缺少 C 端 8 个残基和 N 端 188 个残基，可能影响 helix 的稳定性或构象 | 全长蛋白中 helix 可能更稳定或更不稳定 | 对全长蛋白进行初步 NMR 表征（即使无法完全赋值）或 SAXS 比较截短体与全长蛋白的构象 | Assignment and data deposition 节 |
| 单一浓度（80–100 μM） | 未测试浓度依赖性，无法排除寡聚或浓度依赖的构象变化 | SERBP1 在核糖体环境中可能以高浓度存在，可能发生相分离或寡聚 | 进行浓度梯度的 NMR 滴定或 DLS 测量 | Methods: NMR experiments 节 |

## 14 Agent 提炼的知识候选
**标题: Agent 提炼的知识候选**

1. **「无序中的有序」作为 IDR 功能位点的识别策略**
   - 本文显示，即使整体为 IDP 的蛋白，其化学位移数据也能可靠地识别局部稳定二级结构。对 IDP/IDR × 蛋白互作研究，可迁移的方法论是：在开展昂贵的全长结构解析或 MD 模拟之前，先用 NMR 化学位移（或 AI 预测的化学位移）快速扫描 IDR 中的「有序岛」（ordered islands），这些区域往往是分子识别的热点。
   - 迁移方式：对目标 IDP/IDR，先获取或预测 backbone 化学位移，用 SSP 或 δ2D 识别 transient helix/strand，再针对这些区域设计突变或截短实验验证功能。

2. **RGG 重复区的 NMR 挑战与应对策略**
   - 本文明确报告 RGG 重复区（369–381）因序列简并导致谱峰重叠而无法赋值。这对 IDP/IDR 研究有普适意义：富含重复序列的 IDR（RGG、poly-Q、poly-S 等）是 NMR 赋值的「重灾区」。
   - 迁移方式：对含重复序列的 IDR，可考虑 (a) 分段表达；(b) 选择性氨基酸标记；(c) 点突变打破简并；(d) 结合 MD 模拟或 AI 结构预测补充实验盲区。

3. **构建体稳定性筛选的实用策略**
   - 作者通过质谱发现 C 端降解后，果断缩短构建体（189–408 → 189–400），大幅提升稳定性。这一「先验证完整性，再优化边界」的策略对 IDP 表达纯化具有普适性。
   - 迁移方式：对 IDP 表达构建体，建议常规进行质谱完整性检查；若发现降解，优先尝试截短而非改变标签或条件。

4. **NMR 化学位移数据作为 AI 预测模型的 benchmark**
   - 本文提供了 188 个残基的实验化学位移（BMRB # 50953），可作为 IDP 化学位移预测工具（如 SPARTA+, ShiftX2, UCBShift）的验证数据。对 AI × IDP 方向，这类高质量实验数据是训练和验证模型的重要资源。
   - 迁移方式：收集类似 IDP 的 NMR 赋值数据构建 benchmark 数据集，评估现有化学位移预测器在 IDP 上的表现，针对性改进。

5. **「无经典结构域」蛋白的 RNA 识别可能依赖 IDR 中的 helix**
   - SERBP1 无 RRM/锌指，但 C 端 IDR 含稳定 helix。这提示 IDR 中的 helix 可能替代经典结构域介导 RNA 识别。对 IDP × RNA 互作研究，这是一个可检验的假设。
   - 迁移方式：对无经典 RNA 结合结构域的蛋白，用 NMR 或 AI 预测扫描 IDR 中的 helix 区域，设计突变体进行 RNA 结合实验（EMSA、ITC、NMR 滴定）验证。

## 15 与已有知识连接
1. **IDP 中 transient helix 与分子识别（经外部核验）**
   - Wright & Dyson (2015) Nat Rev Mol Cell Biol 综述指出，IDP 中的 transient secondary structure 常作为分子识别的成核位点。本文发现的 289–298 helix 与此概念一致，可作为该领域的又一实例。

2. **RGG 重复与 RNA 结合（经外部核验）**
   - Thandapani et al. (2013) Mol Cell 综述了 RGG/RG motif 在 RNA 结合和相分离中的作用。本文中 RGG 区无法赋值，但作者暗示其重要性，与文献中 RGG 介导 RNA 识别的观点吻合。

3. **SERBP1 在核糖体中的功能（经外部核验）**
   - Anger et al. (2013) Science 和 Brown et al. (2018) EMBO J 的 cryo-EM 结构显示 SERBP1 以延伸构象占据核糖体 mRNA 通道。本文的 NMR 数据为理解该延伸构象中的局部有序结构提供了溶液态证据。

4. **化学位移预测工具（经外部核验）**
   - 本文使用的 SSP (Marsh et al. 2006) 和 random coil 化学位移 (Kjaergaard & Poulsen 2011) 是 IDP 二级结构预测的常用工具。这些工具与 AI 化学位移预测器（如 ShiftX2, SPARTA+）可互为验证。

5. **IDP 的 NMR 赋值挑战（经外部核验）**
   - IDP 因谱峰重叠和构象交换导致赋值困难是领域共识（Dyson & Wright 2004 Chem Rev）。本文报告的 93% 赋值率在 IDP 中属于较好水平，其策略（NUS + 多实验交叉验证）可参考。

## 16 研究想法
**标题: Agent 生成的研究候选**

1. **候选名称**: IDR 局部有序结构预测的 AI 辅助管线
   - **来源局限/观察**: 本文用 NMR 化学位移识别 helix，但 NMR 实验耗时且需要同位素标记；对无法表达或标记的 IDP 缺乏可扩展的预测工具。
   - **核心假设**: 基于序列的深度学习模型（如 AlphaFold3 的 pLDDT 或专门训练的 IDP 二级结构预测器）能准确预测 IDR 中的 transient helix 位置，与 NMR 化学位移预测结果一致。
   - **初步方法**: 收集已发表的 IDP NMR 赋值数据（如 BMRB），提取实验确定的二级结构倾向，训练/微调序列-结构预测模型；用本文 SERBP1 数据作为独立验证集。
   - **验证方式**: 比较模型预测的 helix 区域与 NMR 实验确定的 helix 区域的重叠率（如 Matthews correlation coefficient）。
   - **创新状态**: partially checked（已有 IDP 二级结构预测工具如 IUPred, DISOPRED3，但对 transient helix 的预测精度有限）

2. **候选名称**: RGG 重复区 NMR 赋值的同位素标记策略优化
   - **来源局限/观察**: 本文 RGG 区（369–381）因序列简并无法赋值，这是 IDP 中重复序列的共性问题。
   - **核心假设**: 选择性 ¹⁵N-精氨酸/¹⁵N-甘氨酸标记（利用精氨酸胍基和甘氨酸 α-氨基的代谢差异）可打破 RGG 重复区的化学位移简并。
   - **初步方法**: 在 E. coli 中使用精氨酸/甘氨酸营养缺陷型菌株，分别添加 ¹⁵N-Arg 和 ¹⁴N-Gly（或反之），比较 HSQC 谱峰分辨率的改善。
   - **验证方式**: 对比选择性标记与全标记样品的 HSQC 谱峰数量、线宽和赋值成功率。
   - **创新状态**: unverified（类似策略已用于其他重复序列蛋白，但未在 SERBP1 上验证）

3. **候选名称**: SERBP1 C 端 helix 的 RNA 结合功能验证
   - **来源局限/观察**: 本文发现 289–298 存在稳定 helix，但未验证其功能。SERBP1 无经典 RNA 结合结构域，该 helix 可能是 RNA 识别的关键。
   - **核心假设**: 289–298 helix 是 SERBP1 结合 mRNA 靶标（如 PAI-1 3'UTR 的 CRS 序列）的结构元件；突变破坏 helix 将降低 RNA 结合亲和力。
   - **初步方法**: 表达 189–400 野生型和 helix 区突变体（如引入脯氨酸破坏 helix），用 EMSA、ITC 或 NMR 滴定比较 RNA 结合亲和力；结合 RNA 的化学位移扰动实验定位结合界面。
   - **验证方式**: 突变体与野生型的 Kd 差异 > 5 倍，且化学位移扰动集中在 helix 区域。
   - **创新状态**: unverified（本文未提供任何 RNA 结合实验数据）

4. **候选名称**: IDP 化学位移赋值数据的 AI 补全方法
   - **来源局限/观察**: 本文 15 个残基（7%）无法赋值，其中 RGG 区因简并和重叠导致。IDP 中未赋值残基常位于功能重要区域。
   - **核心假设**: 利用图神经网络或 transformer 架构，结合已赋值残基的化学位移和序列上下文，可预测未赋值残基的化学位移，置信度可量化。
   - **初步方法**: 以 BMRB 中 IDP 赋值数据为训练集，构建残基级化学位移预测模型；对本文未赋值残基进行预测，并用预测值进行二级结构推断。
   - **验证方式**: 对已知赋值但故意掩蔽的残基进行交叉验证，比较预测与实验化学位移的 RMSD。
   - **创新状态**: unverified（已有化学位移预测工具如 SPARTA+ 但非专门针对 IDP 未赋值残基的补全场景）

5. **候选名称**: IDR 构象系综的 NMR 化学位移约束 MD 模拟
   - **来源局限/观察**: 本文仅提供化学位移赋值和二级结构预测，未进行构象系综分析。IDP 的功能依赖其构象系综，而非单一结构。
   - **核心假设**: 将本文的化学位移作为约束（如 CAMELOT 或 PPM 驱动的restraints），进行 IDP 的增强采样 MD 模拟，可获得比无约束模拟更准确的构象系综，揭示 helix 的群体比例和构象动态。
   - **初步方法**: 使用本文 BMRB 化学位移数据，结合 Amber 或 GROMACS 的 IDP 力场（如 ff99SBws, a99SB-disp），进行 replica exchange MD 或 metadynamics 模拟。
   - **验证方式**: 模拟系综的回算化学位移与实验值吻合（RMSD < 0.5 ppm for ¹³Cα）；helix 群体比例与 SSP score 一致。
   - **创新状态**: partially checked（化学位移约束 MD 已有先例，但未应用于 SERBP1）