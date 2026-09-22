## 01 基本信息
- **标题**：A novel SXXLF motif in the FXR N-terminal domain mediates coregulator and interdomain interactions
- **作者与单位**：Villalona, Priscilla; Pulahinge, Thilini; Wenning, Jordan; Frisbie, Crawford Joseph; Magafas, Jill; Okafor, C Denise（Pulahinge 与 Okafor 所属单位未在摘要中提供；Okafor 获 NSF CAREER 与 NIH 资助，单位未提供）
- **期刊/预印本平台**：bioRxiv : the preprint server for biology
- **年份**：2026-06-04
- **论文类型**：预印本（preprint）
- **领域**：核受体生物学；无序蛋白结构-功能；蛋白-蛋白互作；分子动力学模拟
- **关键词**：FXR（NR1H4）；N-terminal domain (NTD)；SXXLF motif；coregulator；interdomain interaction；molecular dynamics；AlphaFold3
- **DOI/arXiv 号**：10.64898/2026.05.18.724725
- **代码**：未提供
- **数据**：未提供（MD 轨迹未说明是否公开）
- **阅读日期**：2026-06-10（按当前日期推断）
- **该文在课题方向中的位置**：本文以核受体 FXR 的 NTD（一个内在无序结构域）为对象，通过实验（M2H、报告基因）与计算（AlphaFold3 建模 + 微秒级 MD）结合，鉴定了一个新的 SXXLF 互作基序，证明其同时介导 NTD-LBD 互作与 NTD-coregulator 互作。对「IDP/IDR × 蛋白互作 × AI/物理模拟」课题的参考价值在于：(1) 展示了如何用 AlphaFold3 生成含 IDR 的全长模型并用于 MD 模拟；(2) 展示了如何用 M2H 实验验证 IDR 中的短线性基序（SLiM）功能；(3) 展示了 IDR 中单点突变如何通过变构耦合改变远端结构域间距离。

## 02 一句话总结
本文通过 M2H 实验与 AlphaFold3 建模驱动的微秒级 MD 模拟，鉴定出 FXR NTD 中一个新型 SXXLF（SENLF）基序，证明该基序同时介导 NTD 与 LBD 的互作及 NTD 与 SRC-1/SRC-2 共调节因子的互作，且该基序突变（SENAA）显著改变 NTD 与 LBD 间的构象距离与变构耦合。

## 03 研究问题
- **具体问题**：FXR 的 NTD（一个内在无序结构域）是否参与互作？若参与，其分子机制是什么？是否存在特定的序列基序介导这些互作？
- **为什么重要**：核受体 NTD 是药物研发中尚未充分利用的靶点，但其无序性使其难以用传统结构生物学方法研究。理解 NTD 的互作机制有助于开发针对 NTD 的调控策略，并推广到其他含 IDR 的核受体。
- **现有方法为何不足**：NTD 的无序性使其无法用 X 射线晶体学或冷冻电镜解析；传统功能研究多聚焦于 LBD 和 DBD，NTD 的功能常被忽略；已有的 NTD 互作研究（如 AR、ER、MR）未系统鉴定 FXR NTD 的互作基序。
- **精确研究问题**：Can a specific short linear motif in the intrinsically disordered N-terminal domain of FXR mediate both interdomain (NTD-LBD) and coregulator interactions, and does mutation of this motif alter conformational coupling in a way that explains reduced transcriptional activity?

## 04 背景与发展脉络
- **阶段一：核受体 NTD 功能研究（AR/ER/MR 等）**。代表性工作：AR 的 FXXLF/WXXLF 基序介导 NTD-LBD 互作（作者引用文献 15-16, 20, 28-29, 33-34）；ER 的 AF-1 与 GRIP1/SRC1α 互作（文献 10）；MR NTD 与 p300 互作（文献 13）。优点：确立了 NTD 具有功能性互作基序的先例。局限：这些基序在不同受体间不保守，FXR 的 NTD 基序未知。
- **阶段二：FXR 结构-功能研究**。已有大量 FXR LBD 与 DBD 的结构与功能研究（文献 7-8），但 NTD 因无序性被排除在结构研究之外。
- **阶段三：IDR 与 SLiM 研究**。短线性基序（SLiMs）在无序区域中介导蛋白互作已成为共识，但核受体 NTD 中的 SLiM 鉴定仍不系统。
- **本文主张的位置**：首次在 FXR NTD 中鉴定 SXXLF 基序，证明其同时介导 NTD-LBD 与 NTD-coregulator 互作，并利用 AlphaFold3 + MD 模拟揭示突变导致的构象与变构变化。
- **脉络核验状态**：仅本文框架（作者在 Introduction 中引用的 AR/ER/MR 研究为外部文献，但「FXR NTD 功能未知」的判断基于作者综述，未独立核验）。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| NTD 无序性阻碍结构研究 | 无实验结构解析 NTD | NTD 高度无序，难以结晶或冷冻电镜 | Introduction：「the NTD is highly disordered, making it challenging to use in structural studies」 |
| NTD 功能在 FXR 中未被探索 | 缺乏 FXR NTD 的互作与功能数据 | 研究焦点集中在 LBD/DBD | Introduction：「The role of the NTD in FXR has not been fully explored」 |
| 已知核受体 NTD 基序不保守 | AR 的 FXXLF/WXXLF 不能直接推广到 FXR | NTD 序列保守性低 | Introduction：「few NTD functions are conserved between nuclear receptors」 |
| 传统互作实验难以定位 IDR 中的功能基序 | 需要系统突变扫描才能定位关键残基 | IDR 缺乏稳定三级结构，功能依赖短线性基序 | Results 图 3A：序列分析定位 SENLF |
| 单点突变的功能影响难以从结构上解释 | 突变导致转录活性下降但机制不明 | 缺乏全长动态结构信息 | Results 图 4D-H：MD 模拟揭示构象与变构变化 |

## 06 核心思想
1. **表面方法**：用 M2H 实验系统检测 FXR NTD 与 LBD 及 coregulator 的互作；用序列分析寻找已知核受体互作基序的同源序列；用定点突变验证基序功能；用 AlphaFold3 生成全长模型，再用微秒级 MD 模拟比较 WT 与突变体的构象动态与变构耦合。
2. **核心洞察**：FXR NTD 中的 SENLF 基序是一个双功能 SLiM——它既介导 NTD 与 LBD 的分子内互作（类似 AR 的 FXXLF 介导 NTD-LBD 互作），又介导 NTD 与 SRC-1/SRC-2 的分子间互作。突变该基序不仅破坏直接互作，还通过改变 NTD 的构象位置，远程影响 NTD 与 LBD 其他区域（如 H3、H4）的距离，从而改变变构耦合网络。
3. **可能的普适教训** [Analysis]：IDR 中的 SLiM 可能具有「双功能」属性——同一基序既参与分子内（intramolecular）又参与分子间（intermolecular）互作。这意味着在研究 IDR 功能时，不能仅关注其与某一伙伴的互作，而应考虑其在分子内与分子间互作之间的竞争或协同。此外，AlphaFold3 虽然对 IDR 的构象预测不可靠，但可用于生成含 IDR 的全长模型，再通过 MD 模拟探索 IDR 的动态行为——这种「AF3 建模 + MD 采样」的流程对 IDP/IDR 研究具有方法论参考价值。

## 07 方法总览
- **输入**：FXR 全长序列（UniProt Q96RI1-1）；FXR 已知结构信息（LBD、DBD）；coregulator 序列（SRC1 基序、SRC1-3M 片段）；FXRE DNA 序列（IR1、PLTP）。
- **输出**：NTD 与 LBD 互作的实验证据；SENLF 基序的功能验证；WT 与 SENAA 突变体的构象差异与变构耦合变化。
- **模块**：
  1. 报告基因实验（ΔNTD vs WT，4 种配体）
  2. M2H 互作实验（NTD 与 LBD；NTD 与 coregulator 基序）
  3. 序列分析（寻找已知基序同源序列）
  4. 定点突变（SENAA）
  5. AlphaFold3 建模（单体 FXR；FXR-RXR 异二聚体 + DNA）
  6. MD 模拟（单体：6 个 5μs 重复；异二聚体：4 个 1.5-3.5μs 重复）
  7. 接触图分析、Cα-Cα 距离分析、相关性矩阵分析
- **训练**：不适用（无机器学习训练）
- **工具**：AlphaFold3；Amber18/20/22（ff14SB 力场）；Anton 3 超级计算机；CPPTRAJ
- **反馈回路**：实验（M2H/报告基因）→ 序列分析 → 突变验证 → 计算建模 → MD 模拟 → 构象/变构解释 → 回到实验假设
- **假设**：NTD 的互作功能由短线性基序介导；AlphaFold3 生成的 NTD 构象虽不唯一，但可用于 MD 模拟的初始构象；MD 模拟的微秒时间尺度足以捕捉 NTD 的构象重排。

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| ΔNTD 报告基因实验 | 评估 NTD 对转录活性的贡献 | 建立 NTD 功能重要性的初步证据 | 输入：WT/ΔNTD 质粒 + 4 种配体；输出：荧光素酶活性 fold change | Results 图 1B：ΔNTD 显著降低所有配体下的转录活性 | 若移除，无法建立 NTD 功能重要性的前提 |
| M2H（NTD-LBD） | 检测 NTD 与 LBD 的分子内互作 | 验证 NTD 是否参与分子内互作 | 输入：VP16-NTD 系列 + GAL4-LBD；输出：互作 fold change | Results 图 1D：NTD 与 LBD 互作，且受配体影响 | 若移除，无法证明 NTD-LBD 互作的存在 |
| M2H（NTD-coregulator） | 检测 NTD 与 coregulator 的分子间互作 | 验证 NTD 是否直接结合 coregulator | 输入：VP16-NTD 系列 + GAL4-SRC1-2/3M；输出：互作 fold change | Results 图 2：NTD-DBD 与 SRC1 基序互作 | 若移除，无法证明 NTD 的 coregulator 识别功能 |
| 序列分析 | 定位候选互作基序 | 无序区中功能基序需序列比对发现 | 输入：NTD 序列；输出：SENLF 候选基序 | Results 图 3A：SENLF 与 AR FQNLF 相似 | 若移除，无法指导突变设计 |
| SENAA 突变体 | 验证 SENLF 基序功能 | 通过功能丧失验证基序必要性 | 输入：SENAA 突变质粒；输出：活性/互作变化 | Results 图 3D-F：SENAA 降低转录活性与互作 | 若移除，无法将表型归因于该基序 |
| AlphaFold3 建模 | 生成全长 FXR 结构模型 | 无实验结构，需计算模型作为 MD 起点 | 输入：序列；输出：全长单体/异二聚体模型 | Results 图 3B-C：NTD 无序但 SENLF 形成 helix 并靠近 LBD AF-2 | 若移除，无法进行 MD 模拟 |
| MD 模拟 | 比较 WT 与 SENAA 的构象动态 | 解释突变如何影响构象与变构 | 输入：AF3 模型；输出：轨迹、接触图、距离、相关性 | Results 图 4A-H：SENAA 改变 NTD-LBD 距离与相关性 | 若移除，无法提供构象层面的机制解释 |

## 09 关键公式符号
- **Cα-Cα 距离**：d(i,j) = ||r_Cα(i) - r_Cα(j)||，用于量化残基 i 与 j 之间的空间距离。文中用于比较 WT 与 SENAA 中 NTD 残基（如 G27、V43）与 LBD 残基（如 Q313、F282）的距离变化（Results 图 4D）。
- **相关性矩阵（correlation matrix）**：C(i,j) = ⟨Δr_i · Δr_j⟩ / (⟨|Δr_i|²⟩⟨|Δr_j|²⟩)^(1/2)，其中 Δr_i 为残基 i 相对其平均位置的位移。用于衡量 NTD 与 LBD 之间的变构耦合（Results 图 4I）。
- **接触图（contact map）**：二值矩阵，若残基 i 与 j 的重原子距离 < 阈值（通常 4.5-6 Å）则为 1，否则为 0。用于比较 WT 与 SENAA 的接触差异（Results 图 4A-C）。
- **fold change**：报告基因实验中 Firefly/Renilla 比值，归一化到 DMSO 处理的空载体对照。用于量化转录活性与互作强度。

## 10 实验设计与证据链
- **数据集/群体**：HeLa 细胞系（ATCC）；FXR 配体：CDCA、OCA、GW4064、LCA、fexaramine；coregulator 片段：SRC1-2（单 LXXLL 基序）、SRC1-3M（3 个 LXXLL 基序，残基 620-759）。
- **规模**：报告基因实验每组至少 3 个生物学重复（Methods 未明确说明具体 n，但提到「three biological replicates」）；M2H 实验每组 3 个生物学重复；MD 模拟：单体 6×5μs，异二聚体 4×1.5-3.5μs。
- **指标**：荧光素酶 fold change；M2H 互作 fold change；MD 中 Cα-Cα 距离、接触图差异、相关性矩阵。
- **基线/对照**：空 VP16/空 GAL4 载体；WT FXR；DMSO 处理。
- **评测协议**：双荧光素酶报告基因（Firefly/Renilla 归一化）；M2H 按 Promega CheckMate 系统操作；MD 分析用 CPPTRAJ。
- **预算/仪器**：未提供（预印本未说明）。
- **oracle 输入**：AlphaFold3 生成的 FXR 全长模型（含 NTD）。

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| ΔNTD 报告基因 | NTD 对 FXR 转录活性有贡献 | WT vs ΔNTD，4 种配体 | ΔNTD 显著降低活性（>50%） | NTD 是 FXR 转录活性的重要贡献者 | 不能区分 NTD 是直接参与转录机制还是通过构象影响其他结构域 | Results 图 1B |
| M2H NTD-LBD | NTD 与 LBD 存在分子内互作 | VP16-NTD + GAL4-LBD vs 对照 | 显著互作信号，配体增强 | NTD 与 LBD 直接互作 | 不能确定互作是否在完整受体中发生（M2H 为片段水平） | Results 图 1D |
| M2H NTD-coregulator | NTD 与 SRC1 基序互作 | VP16-NTD-DBD + GAL4-SRC1-2/3M | 显著互作信号 | NTD 直接识别 coregulator 基序 | 不能确定互作是否依赖 LBD 协同 | Results 图 2 |
| SENAA 突变报告基因 | SENLF 基序对转录活性必要 | WT vs SENAA，报告基因 | SENAA 降低活性 | SENLF 是功能必需基序 | 不能排除其他 NTD 区域也参与 | Results 图 3D |
| SENAA 突变 M2H | SENLF 介导 NTD-LBD 与 NTD-coregulator 互作 | WT vs SENAA，M2H | SENAA 降低互作 | SENLF 是互作介导基序 | 不能确定 SENLF 是否直接接触伙伴或通过构象间接影响 | Results 图 3E-F |
| MD 接触图/距离 | SENAA 改变 NTD-LBD 构象 | WT vs SENAA 轨迹 | 接触差异、距离变化（G27-Q313: 18.7→37.2 Å；V43-F282: 40.8→19.8 Å） | 突变导致 NTD 相对 LBD 的构象重排 | MD 为计算预测，需实验验证 | Results 图 4A-H |
| MD 相关性矩阵 | SENAA 改变 NTD-LBD 变构耦合 | WT vs SENAA 相关性 | WT 中 NTD 与 LBD 正相关，SENAA 中变为负相关 | 突变改变变构耦合模式 | 相关性不等于因果，需功能实验验证 | Results 图 4I |

## 11 结论正确解读
- **任务范围**：本文仅研究了 FXR（NR1H4）的 NTD，未涉及其他核受体。结论不能推广到所有核受体 NTD。
- **oracle/真值输入**：AlphaFold3 模型作为 MD 模拟的起点，但 AF3 对 IDR 的预测不可靠，MD 结果依赖初始模型的选择。作者未说明是否测试了不同初始构象的鲁棒性。
- **端到端状态**：实验（M2H/报告基因）与计算（MD）是分开的，未在同一体系中进行「计算预测→实验验证」的闭环。MD 预测的构象变化未通过实验（如 FRET、HDX）验证。
- **算力成本**：未提供。MD 总模拟时间约 30μs（单体）+ 约 10μs（异二聚体），需要 GPU 集群或 Anton 3 级算力。
- **历史数据依赖**：依赖 AlphaFold3 的预测能力；依赖已知核受体基序（FXXLF/WXXLF）作为序列比对参考。
- **模型依赖**：MD 结果依赖力场（ff14SB）、水模型（TIP3P）、离子浓度（150 mM NaCl）和模拟时间尺度。更长模拟可能发现不同构象。
- **最难情形**：NTD 的高度无序性意味着其构象系综极为复杂，MD 模拟可能未充分采样。SENLF 基序在 AF3 模型中形成 helix，但 IDR 中的 helix 可能只是瞬态结构。
- **群体/领域边界**：结论仅适用于 FXR 及其直系同源物；SXXLF 基序在其他蛋白中的存在与功能未探索。
- **有边界的复述**：在 HeLa 细胞报告基因和 M2H 实验中，FXR NTD 的 SENLF 基序对转录活性和 NTD-LBD、NTD-coregulator 互作是必要的；AlphaFold3 建模 + MD 模拟预测该基序突变会改变 NTD 相对 LBD 的位置和变构耦合，但这些计算预测尚未经实验验证。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| NTD 无序性限制结构解析 | 无法获得 NTD 的实验结构 | 使用 CD/NMR 等生物物理实验验证 NTD 结构变化 | Discussion：「Biophysical experiments such as CD or NMR will be used in future experiments to test the hypothesis that additional domains increase the secondary structure of the NTD」 |
| SENLF 基序未完全解释 NTD 功能 | SENAA 突变未完全消除活性，ΔNTD 效果更强 | 需鉴定 NTD 中其他功能基序 | Results 图 3D：「the activity levels of the SENAA mutant are not decreased to the same extent as ΔNTD, indicating that other parts of the NTD may facilitate the receptor’s normal function」 |
| coregulator 选择性机制未明 | P300 对 SENAA 不敏感，但 ΔNTD 敏感 | 需鉴定 P300 识别的其他 NTD 区域 | Results 图 3F：「P300 only shows a decrease in the ΔNTD mutant, suggesting that mechanisms other than SENLF are preferentially used for P300 recognition」 |
| MD 预测未实验验证 | 构象变化和变构耦合为计算预测 | 需实验验证（如交联质谱、FRET） | Discussion 未明确说明，但 MD 结果未与实验对照 |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|----------------------|----------|----------|------|
| M2H 实验使用片段而非全长蛋白 | NTD 与 LBD 的互作可能在完整受体中受其他结构域影响 | M2H 结果可能高估或低估真实互作强度 | 在完整受体背景下进行共免疫沉淀或 BRET 实验 | Methods：M2H 使用 VP16-NTD 系列片段 |
| AlphaFold3 对 IDR 的预测不可靠 | AF3 预测的 SENLF helix 可能只是计算伪影 | MD 结果依赖初始构象，若 helix 不存在则结论不成立 | 用 CD 或 NMR 验证 SENLF 是否形成 helix | Results 图 3B-C：AF3 预测 helix 结构 |
| MD 模拟时间尺度可能不足 | 5μs 可能不足以采样 IDR 的完整构象空间 | 可能遗漏重要的构象状态 | 增加模拟时间或使用增强采样方法（如 Replica Exchange） | Methods：单体 6×5μs |
| 相关性矩阵的因果解释不明确 | 相关性变化可能是间接效应而非直接变构 | 变构耦合的结论可能过度解读 | 进行突变扫描或使用变构网络分析工具 | Results 图 4I |
| 未测试 SXXLF 基序在其他核受体中的保守性 | 该基序可能仅存在于 FXR | 若基序不保守，其普遍意义有限 | 对核受体家族进行序列比对 | Results 图 3A：仅展示 FXR 序列 |
| 报告基因实验未区分 NTD 对基础转录 vs 配体诱导转录的贡献 | ΔNTD 和 SENAA 的效果可能主要影响基础活性 | 对配体调控机制的结论可能不准确 | 分别分析基础与配体诱导的活性 | Results 图 1B：未区分基础 vs 诱导活性 |

## 14 学到什么
**Agent 提炼的知识候选**：
1. **SLiM 双功能假说**：同一短线性基序可同时介导分子内（intramolecular）与分子间（intermolecular）互作。对 IDP/IDR 研究的方法论启示：在鉴定 IDR 中的功能基序时，应同时测试其与同一蛋白其他结构域及外部伙伴的互作，避免只关注单一互作模式。
2. **AF3 + MD 的 IDR 研究流程**：AlphaFold3 虽对 IDR 构象预测不可靠，但可生成含 IDR 的全长模型作为 MD 模拟起点。对 IDP/IDR × AI × 物理模拟课题的启示：可建立「AF3 生成初始模型 → MD 采样构象系综 → 比较突变体」的流程，但需注意初始构象依赖性和采样充分性。
3. **M2H 用于 IDR 互作验证**：M2H 系统可检测 IDR 与折叠结构域之间的互作，且可通过片段化（NTD、NTD-DBD、NTD-DBD-hinge）定位互作所需的最小区域。对 IDP/IDR 互作研究的方法论参考：可用类似策略系统定位 IDR 中的功能基序。
4. **变构耦合的 MD 分析方法**：通过 Cα-Cα 距离和相关性矩阵比较 WT 与突变体的构象差异，可揭示 IDR 突变如何远程影响其他结构域。对 IDP/IDR × 蛋白互作课题的启示：IDR 中的突变可能通过改变 IDR 的构象偏好来远程调控折叠结构域的功能，这种「IDR 介导的变构调控」可能是普遍机制。
5. **coregulator 选择性**：不同 coregulator 可能识别 IDR 中不同的基序（SENLF 对 SRC-1/2 重要，但对 P300 不重要）。对 IDP/IDR 互作课题的启示：IDR 可能包含多个互作基序，分别识别不同伙伴，形成「多价互作」网络。

## 15 与已有知识连接
- **核受体 NTD 互作基序**：本文与 AR 的 FXXLF/WXXLF 基序研究（He et al., 2000; He & Wilson, 2003）直接相关。作者将 SXXLF 定位为新的核受体互作基序家族成员。可进一步检查其他核受体（如 PPAR、LXR、RXR）NTD 中是否存在 SXXLF 同源基序。
- **IDR 中的 SLiM 功能**：本文与 SLiM 领域的一般认识一致——无序区域通过短线性基序介导互作（Davey et al., 2012; Van Roey et al., 2014）。本文的特殊贡献在于证明同一 SLiM 同时参与分子内与分子间互作。
- **AF3 在 IDR 研究中的应用**：本文使用 AF3 生成全长模型，与近期将 AF3 用于 IDR 研究的趋势一致（如 Ruff & Pappu, 2021 对 AF 在 IDR 中局限性的讨论）。本文未讨论 AF3 对 IDR 预测的不确定性，这是可改进之处。
- **核受体变构调控**：本文的变构耦合分析可与核受体变构调控的已有研究（如 NVR 的变构网络）连接。IDR 介导的变构调控在核受体中尚少报道，本文提供了新视角。
- **候选方向**：可探索 SXXLF 基序是否存在于其他含 IDR 的转录因子中；可测试 SXXLF 基序是否参与液-液相分离（因 IDR 与 SLiM 常参与凝聚体形成）。

## 16 研究想法
**Agent 生成的研究候选**：

1. **候选名称**：SXXLF 基序在核受体家族中的保守性与功能泛化分析
   - **来源局限/观察**：本文仅验证了 FXR 中的 SXXLF，未检查其他核受体。
   - **核心假设**：SXXLF 基序可能存在于其他核受体 NTD 中，并介导类似的 NTD-LBD 与 NTD-coregulator 互作。
   - **初步方法**：对核受体家族 NTD 进行序列比对，寻找 SXXLF 同源基序；对阳性受体进行 M2H 验证。
   - **验证方式**：M2H 实验 + 报告基因实验。
   - **可能的失败模式**：基序在其他受体中不保守或功能不同。
   - **创新状态**：unverified

2. **候选名称**：SXXLF 基序与液-液相分离的关联研究
   - **来源局限/观察**：IDR 与 SLiM 常参与相分离，但本文未探讨 SXXLF 是否参与 FXR 凝聚体形成。
   - **核心假设**：SXXLF 基序可能通过介导多价互作促进 FXR 的相分离，且 SENAA 突变会破坏相分离。
   - **初步方法**：体外相分离实验（浊度、荧光显微镜）+ 细胞内凝聚体成像。
   - **验证方式**：比较 WT 与 SENAA 的相分离能力。
   - **可能的失败模式**：SXXLF 不参与相分离，或相分离主要由其他区域驱动。
   - **创新状态**：unverified

3. **候选名称**：IDR 介导的核受体变构调控的通用机制研究
   - **来源局限/观察**：本文发现 NTD 突变改变 LBD 构象与变构耦合，但机制不清。
   - **核心假设**：IDR 通过动态构象系综的变化来调控折叠结构域的功能，这种「IDR 介导的变构」是核受体的通用机制。
   - **初步方法**：对多个核受体（FXR、AR、ER、PPAR）进行 MD 模拟，比较 IDR 突变对 LBD 构象的影响。
   - **验证方式**：MD 预测 + 实验验证（HDX-MS、FRET）。
   - **可能的失败模式**：不同受体的 IDR 变构机制差异大，难以归纳通用规律。
   - **创新状态**：unverified

4. **候选名称**：AF3 模型不确定性对 IDR-MD 模拟结果的影响评估
   - **来源局限/观察**：本文未讨论 AF3 对 IDR 预测的不确定性对 MD 结果的影响。
   - **核心假设**：AF3 生成的 IDR 初始构象不同会导致 MD 模拟结果显著不同。
   - **初步方法**：用 AF3 生成多个 IDR 构象，分别作为 MD 起点，比较构象系综的收敛性。
   - **验证方式**：比较不同初始构象的 MD 轨迹是否收敛到相似系综。
   - **可能的失败模式**：MD 结果对初始构象高度敏感，需要更长的模拟或增强采样。
   - **创新状态**：unverified

5. **候选名称**：coregulator 对 IDR 基序的选择性识别机制
   - **来源局限/观察**：本文发现 SRC-1/SRC-2 对 SENLF 敏感，但 P300 不敏感。
   - **核心假设**：不同 coregulator 通过不同的结构机制识别 NTD 中的不同基序，形成选择性互作网络。
   - **初步方法**：对 SRC-1/SRC-2/P300 与 FXR NTD 的互作进行分子对接或共结晶尝试。
   - **验证方式**：突变分析 + 结合亲和力测定。
   - **可能的失败模式**：IDR 的构象异质性使共结晶或对接困难。
   - **创新状态**：unverified