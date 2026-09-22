## 01 基本信息

- **标题**：High-resolution protein modeling through Cryo-EM and AI: current trends and future perspectives – a review
- **作者**：Jeyaraj, Gnanaprakash; Rajendran, Anith Kumar; Sathishkumar, Kuppusamy; Almutairi, Bader O; Vadivelu, Aanand; Chokkakula, Santosh; Tu, Yanyang; Xie, Weimim
- **单位**：未提供（PubMed 记录未列出作者单位）
- **期刊/平台**：Frontiers in Molecular Biosciences
- **年份**：2025-11-10
- **论文类型**：综述（Review）
- **领域**：结构生物学、冷冻电镜（cryo-EM）、AI蛋白质结构预测
- **关键词**：cryo-EM、AlphaFold、AI、蛋白质建模、结构预测、整合方法
- **DOI/arXiv**：10.3389/fmolb.2025.1688455
- **代码**：未提供
- **数据**：未提供
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文为综述，覆盖 cryo-EM 与 AI 在蛋白质结构解析中的互补作用，明确讨论了 IDP/IDR 的挑战（如 AlphaFold 对 IDR 预测的 RMSD >5–10 Å），并列举了 IDPConformerGenerator、ALBATROSS 等 IDP 专用方法，以及 AlphaFold 与 cryo-EM 整合的案例（核孔复合物、Fanconi anemia 核心复合物等）。对 IDP/IDR × 蛋白互作 × AI 课题提供背景框架和方法论参考，但非专门针对相分离/凝聚体的研究。

## 02 一句话总结

本文系统综述了 cryo-EM 与 AI（以 AlphaFold 系列为代表）在蛋白质结构解析中的互补角色、整合策略及当前局限，指出 AI 预测在 IDP/IDR、多亚基复合物和新型折叠上仍不可靠，需与 cryo-EM 等实验手段结合，并展望了从静态结构解析走向动态、功能导向的发现型科学的趋势。

## 03 研究问题

- **具体问题**：cryo-EM 和 AI 驱动的结构预测如何互补、整合，以解决传统结构生物学难以攻克的目标（膜蛋白、大复合物、IDP/IDR）？当前技术的能力边界在哪里？
- **为什么重要**：结构生物学正从"解析结构"转向"发现驱动"的科学，理解 cryo-EM 与 AI 各自的优势和局限，对药物设计、疾病机制研究至关重要。
- **现有方法为何不足**：X 射线晶体学需要结晶（膜蛋白、柔性蛋白难以结晶）；NMR 受限于分子量（<40 kDa）；单一 AI 预测对 IDR、多亚基复合物、新型折叠的准确性不足。
- **精确的 Can 问题**：Can cryo-EM 与 AI 的整合方法实现对包括膜蛋白、IDP/IDR 和大分子复合物在内的全部蛋白质组的可靠高分辨率建模？

## 04 背景与发展脉络

**脉络标注**：以下脉络基于本文框架，未经外部系统核验。

1. **奠基期（1950s–2000s）**：X 射线晶体学（肌红蛋白、核糖体）、NMR（溶液态小蛋白）、传统 EM（负染色，10–20 Å 分辨率）。局限：结晶瓶颈、分子量限制、低分辨率。
2. **分辨率革命（2013–2020）**：直接电子探测器（direct electron detectors）引入，cryo-EM 突破近原子分辨率（TRPV1 离子通道为里程碑）。同时，计算方法的进步使单颗粒分析（SPA）成为主流。
3. **AI 爆发期（2021–至今）**：AlphaFold2 在 CASP14 达到近实验精度；AlphaFold3 扩展至蛋白-核酸-配体复合物；RoseTTAFold 等工具涌现。AI 预测数据库（AlphaFold DB）覆盖近乎全蛋白质组。
4. **整合与挑战期（当前）**：AI 与 cryo-EM 的整合（如模型引导的建模、cryo-EM 密度图辅助的 AI 精修）；IDP/IDR 的构象系综方法（IDPConformerGenerator、ALBATROSS）；时间分辨技术（TR-cryo-EM、TR-SFX）与 AI 结合探索动态结构。
5. **本文主张的位置**：cryo-EM 与 AI 不是替代关系而是互补关系；整合方法（integrative/hybrid）是未来方向；IDP/IDR 和动态构象是下一个前沿。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 膜蛋白难以结晶 | X 射线晶体学对膜蛋白成功率低 | 膜蛋白疏水性强，难以形成有序晶体；需要去垢剂或脂质环境稳定 | Introduction 节；"membrane proteins...notoriously resistant to crystallization" |
| IDP/IDR 预测不可靠 | AlphaFold 对 IDR 的 RMSD 常超过 5–10 Å | IDR 缺乏稳定三级结构，进化约束弱，MSA 信号不足 | Introduction 节；"for IDRs and flexible linkers, RMSD often exceeds 5–10 Å" |
| 大复合物建模困难 | 多亚基复合物中 AI 预测常遗漏动态构象 | 复合物构象空间大，单一静态结构不足以描述功能状态 | Introduction 节；"multi-subunit complexes may omit relevant dynamic conformers" |
| AI 预测缺乏实验验证 | 高置信度预测不一定对应生物学真实构象 | 训练数据偏差、过拟合、置信度指标（pLDDT）可能误导 | "AI 模型标准"节；"high scores do not always correlate with biological accuracy" |
| cryo-EM 设备门槛高 | 设备昂贵、需专业操作、数据处理计算量大 | 高成本、高维护、需专门人才 | "Cryo-EM 标准"节；"high capital and maintenance costs" |
| 时间分辨能力有限 | TR-cryo-EM 仅达毫秒级，TR-SFX 受限于微晶 | 反应引发速度、样品制备、剂量控制等瓶颈 | "时间分辨结构生物学"节；"reaction initiation speed, reproducible grid manufacture, dose control" |

## 06 核心思想

**1) 表面方法**：
- 系统回顾 cryo-EM 的技术进步（直接电子探测器、SPA、cryo-ET）和 AI 预测工具（AlphaFold2/3、RoseTTAFold）的发展
- 分类讨论整合方法：AI 辅助 cryo-EM 建模（如 DeepTracer、ModelAngelo）、cryo-EM 约束的 AI 精修、多技术数据融合（cryo-EM + NMR + SAXS + MS）
- 列举应用案例：膜蛋白、IDP/IDR、病毒复合物、核孔复合物等

**2) 核心洞察**：
- cryo-EM 提供实验约束和构象多样性，AI 提供序列到结构的快速映射，二者互补而非竞争
- IDP/IDR 需要从"单一结构"范式转向"构象系综"范式，AI 预测需与 NMR/SAXS/FRET 等实验约束结合
- 结构生物学的未来是"发现驱动"的：从静态结构到动态功能，从纯化样品到原位（in situ）结构

**3) 可能的普适教训 [Analysis]**：
- 对 IDP/IDR × 蛋白互作 × AI 课题：单一 AI 模型（如 AlphaFold）不足以描述无序蛋白的互作机制，需要结合构象系综生成器（如 IDPConformerGenerator）和实验约束（NMR 化学位移、SAXS 轮廓、FRET 距离）来构建功能相关的构象集合
- 相分离/凝聚体研究可借鉴"整合建模"思路：将 cryo-EM 的低分辨率密度、NMR 的残基级动态信息、AI 预测的域结构整合，构建多价互作网络模型
- 对 AI 方法开发者：需要针对 IDR 开发专门的评估指标和训练策略，而非直接套用折叠蛋白的基准

## 07 方法总览

本文为综述，无原始方法。但综述中描述的技术流程可归纳为：

- **输入**：蛋白质氨基酸序列（AI 预测）；冷冻样品电子显微图像（cryo-EM）；溶液态 NMR 谱；SAXS 散射曲线；MS 交联数据
- **处理模块**：
  - cryo-EM 流程：样品制备（玻璃化）→ 数据采集（直接电子探测器）→ 运动校正/CTF 估计 → 粒子挑选（AI 辅助，如 Topaz、crYOLO）→ 2D/3D 分类 → 三维重构 → 模型构建与精修
  - AI 预测流程：序列 → MSA 构建 → 注意力网络（Evoformer）→ 结构模块 → 3D 坐标 + 置信度（pLDDT, PAE）
  - 整合流程：AI 预测模型作为初始模板 → 拟合到 cryo-EM 密度图 → 实验约束（交联、FRET、SAXS）精修 → 构象系综生成
- **输出**：高分辨率原子模型、构象系综、蛋白-配体/蛋白-蛋白复合物模型、功能注释
- **反馈回路**：AI 预测可指导 cryo-EM 数据解释（如模型引导的粒子分类），cryo-EM 实验结构可反馈改进 AI 训练数据
- **假设**：序列决定结构（折叠蛋白）；cryo-EM 密度图反映构象系综的平均；AI 置信度指标与实验准确性相关（但作者指出此假设在 IDR 上不成立）

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 直接电子探测器 | 提高信噪比、实现单电子计数 | 传统探测器噪声大、帧率低，无法校正束致漂移 | 输入：电子散射信号；输出：高质量显微图像 | "X. Li et al., 2013" 引用；"resolution revolution" 标志 | 无此模块则 cryo-EM 分辨率仍停留在 10–20 Å 水平 |
| 单颗粒分析（SPA） | 从大量粒子投影中重构 3D 密度 | 无需结晶，可处理构象异质性 | 输入：粒子图像；输出：3D 密度图 | TRPV1 结构（Liao et al., 2013） | 无法解析无晶体的大复合物和膜蛋白 |
| AI 粒子挑选（Topaz, crYOLO, CryoTransformer） | 自动、准确识别显微图中的粒子 | 手动挑选耗时且主观，是 cryo-EM 流程瓶颈 | 输入：显微图；输出：粒子坐标 | CryoTransformer 在 CryoPPP 上 F1 0.65–0.85（Dhakal et al., 2024） | 高通量 cryo-EM 流程不可行 |
| AlphaFold2/3 | 从序列预测 3D 结构 | 提供无实验条件下的快速结构预测 | 输入：序列 + MSA；输出：3D 坐标 + pLDDT/PAE | CASP14 近实验精度（Jumper et al., 2021） | 失去大规模结构预测能力，但 IDR 预测本身不可靠 |
| 构象系综生成器（IDPConformerGenerator） | 生成 IDP 的构象系综 | IDP 无单一结构，需系综描述 | 输入：序列 + 实验约束；输出：构象系综 | Teixeira et al., 2022 引用 | IDP 研究缺乏计算工具 |
| 序列-系综预测器（ALBATROSS） | 从序列直接预测 IDP 系综维度 | 无需昂贵实验即可估计 IDP 尺寸 | 输入：序列；输出：Rg、端到端距离等 | Lotthammer et al., 2024 引用 | IDP 高通量表征受限 |
| 整合建模框架 | 融合多源数据构建统一模型 | 单一技术不足以覆盖复杂系统 | 输入：cryo-EM + NMR + SAXS + MS + AI 预测；输出：综合模型 | 核孔复合物重建（Schotte et al., 2003 引用） | 复杂系统（如 NPC）无法完整解析 |

**消融效应区分**：本文为综述，未做消融实验。上述"移除后影响"为基于作者论述的预期效应，非实测。

## 09 关键公式符号

本文为综述，未包含原始数学公式。涉及的技术指标包括：

- **Fourier Shell Correlation (FSC)**：用于估计 cryo-EM 分辨率，采用 gold-standard half-map FSC 的 0.143 判据。公式未给出，但为 cryo-EM 领域标准指标。
- **pLDDT (predicted Local Distance Difference Test)**：AlphaFold 的逐残基置信度分数，范围 0–100，>90 表示高置信度。
- **PAE (Predicted Aligned Error)**：预测的残基对/域间相对位置误差矩阵。
- **RMSD (Root Mean Square Deviation)**：用于量化预测结构与实验结构的偏差。文中给出 IDR 的 RMSD 常 >5–10 Å。
- **F1-score**：粒子挑选模型的评估指标，CryoTransformer 在 CryoPPP 上达到 0.65–0.85。

## 10 实验设计与证据链

本文为综述，无原始实验。综述中引用的关键证据：

- **数据集/群体**：CryoPPP（9,893 张显微图，>400,000 个标注粒子，34 个蛋白数据集）；CASP14/CASP15 基准；AlphaFold DB（全蛋白质组预测）；EMDB/EMPIAR 数据库
- **指标**：FSC（0.143 判据）、RMSD、pLDDT、PAE、F1-score
- **评测协议**：CASP 系列盲测；EMDataResource Model Challenge（2019）；EM Ligand Modeling Challenge（2024）

| 实验/案例 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|-----------|-------------|-----------|------|------------|----------------|------|
| TRPV1 离子通道 cryo-EM 结构 | 新探测器可实现近原子分辨率 | 对比传统探测器 | 首次近原子分辨率膜蛋白结构 | cryo-EM 可解析难结晶膜蛋白 | 不能推广到所有膜蛋白 | Introduction 节；Liao et al., 2013 |
| AlphaFold2 CASP14 表现 | AI 可达到实验级预测精度 | 与实验结构对比 | 多数球状蛋白 RMSD <1.5 Å | AI 预测对折叠蛋白高度准确 | 不适用于 IDR/IDR | Introduction 节；Jumper et al., 2021 |
| AlphaFold 对 IDR 预测 | AI 对无序区域的能力 | 与 NMR/实验对比 | RMSD 常 >5–10 Å | IDR 预测不可靠 | 不能推断所有 IDR 均失败 | Introduction 节；Tunyasuvunakool et al., 2021 |
| CryoTransformer 粒子挑选 | Transformer 可提升挑选精度 | 对比 Topaz、crYOLO | F1 0.65–0.85，3D 重构 4–6 Å | AI 可自动化 cryo-EM 前处理 | 依赖训练数据多样性 | "Cryo-EM"节；Dhakal et al., 2024 |
| Fanconi anemia 核心复合物 | AI 预测辅助 cryo-EM 建模 | 无 AI 辅助 vs 有 AI 辅助 | 4.6 Å 密度图中可 de novo 建模 | AI 可解析原本不可解释的密度图 | 需要实验数据引导 | "整合方法"节；Farrell et al., 2020 |
| 核孔复合物整合建模 | 多技术融合可解析超大复合物 | cryo-EM + AI + 生化数据 | 近完整 ~120 MDa 复合物重构 | 整合方法可攻克超大系统 | 依赖多源数据可用性 | "整合方法"节 |
| 细胞色素 P450 构象探索 | AlphaFold + cryo-EM 揭示构象多样性 | 单一结构 vs 多构象 | 发现替代构象状态 | AI 可补充实验构象采样 | 构象状态的功能意义需验证 | "应用"节；Urban and Pompon, 2022 |

## 11 结论正确解读

- **任务范围**：本文是综述，覆盖 cryo-EM 技术进展、AI 结构预测、整合方法、应用案例和未来方向。不包含新实验或新算法。
- **oracle/真值输入**：综述中引用的实验结构（X 射线、cryo-EM、NMR）作为 AI 预测的基准真值。
- **端到端状态**：cryo-EM 管线（样品→密度图→模型）已较成熟；AI 预测（序列→结构）对折叠蛋白成熟，对 IDR/复合物不成熟；整合方法仍在发展中。
- **算力成本**：文中提及 cryo-EM 需要"substantial computational infrastructure"，但未给出具体数字。
- **历史数据依赖**：AlphaFold 依赖 PDB 中已知结构训练，对新型折叠和未表征蛋白家族预测能力有限。
- **模型依赖**：综述讨论的 AI 工具（AlphaFold2/3、RoseTTAFold、DeepTracer、ModelAngelo、CryoDRGN 等）各有适用范围和局限。
- **最难情形**：IDP/IDR 的构象系综、膜蛋白的构象动态、超大复合物的异质性、新型折叠蛋白。
- **群体/领域边界**：结论主要适用于可纯化的生物大分子；对翻译后修饰、突变效应、环境依赖性构象的预测能力有限。
- **不确定性**：作者明确指出 AI 置信度指标（pLDDT）在 IDR 上可能误导，高置信度不等于生物学准确性。

**有边界的复述**：cryo-EM 与 AI 的整合已在膜蛋白、大复合物和部分 IDP 系统上展示了可行性，但 AI 预测对 IDR/IDR 的可靠性仍有限，需要实验约束和构象系综方法补充；未来方向是动态、原位和功能导向的结构生物学。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| IDP/IDR 预测不可靠 | AlphaFold 对 IDR 的 RMSD 常超过 5–10 Å，结构预测可能误导 | 需要 ensemble-based 方法 + 实验验证（NMR、SAXS、HDX-MS） | Introduction 节 |
| 多亚基复合物预测不足 | 可能遗漏相关动态构象 | 整合 cryo-EM 密度约束与 AI 预测 | Introduction 节 |
| AI 模型忽略环境条件 | 不考虑 pH、离子强度、氧化还原、配体、PTM 等 | 未来 AI 需显式条件化环境参数 | "AI 局限"节 |
| 训练数据偏差 | 对未充分代表的蛋白家族、新型折叠预测不可靠 | 扩大训练数据多样性、持续基准测试 | "AI 模型标准"节 |
| 置信度指标可能误导 | pLDDT 高值不一定对应生物学准确性 | 谨慎解读置信度，结合实验验证 | "AI 模型标准"节 |
| cryo-EM 设备门槛高 | 高成本、需专业操作、计算资源大 | 自动化、AI 辅助流程降低门槛 | "Cryo-EM 标准"节 |
| 时间分辨技术受限 | TR-cryo-EM 仅毫秒级，TR-SFX 需微晶 | 改进微流控、数据采集策略 | "时间分辨"节 |
| 原位结构解析仍困难 | 细胞内近原子分辨率尚未实现 | 开发 cryo-ET 和原位验证方法 | "未来方向"节 |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| 综述对 AlphaFold 的 IDR 局限描述较笼统 | 未区分不同 IDR 类型（如弱疏水、聚电解质、富含重复序列）的预测差异 | IDP/IDR 异质性大，统一论断可能掩盖可预测的子类 | 按 IDR 序列特征分层评估 AlphaFold 准确性 | 文中仅给出 RMSD >5–10 Å 的总体范围 |
| 对相分离/凝聚体的讨论缺失 | 文中提到 IDP 但未讨论液-液相分离（LLPS）或多价互作介导的凝聚体形成 | 相分离是 IDP 功能的重要机制，cryo-EM/AI 在此领域的应用是前沿 | 检索文中是否出现 "phase separation"、"condensate"、"LLPS" 关键词 | 全文未出现相关术语 |
| 整合方法案例选择偏重"成功故事" | 未讨论整合建模失败的案例或方法失效的条件 | 了解失败模式对方法选择至关重要 | 对比其他综述中整合建模的失败案例 | 文中 NPC、Fanconi 等均为成功案例 |
| 对 AI 预测的"生物学验证"标准不明确 | 未定义什么构成充分的实验验证 | 不同验证标准（结构重叠 vs 功能验证）结论可能不同 | 检查文中是否给出具体验证协议 | 仅提及"cross-validation with experimental methods" |
| 综述时间范围有限 | 未覆盖 2024 年后最新进展（如 AF3 的全面评估、新 IDP 预测器） | 快速发展的领域需要及时更新 | 检查引用文献的最新年份 | 引用集中在 2021–2024 |
| 对 cryo-EM 分辨率"原子级"的表述需谨慎 | 近原子分辨率（~3 Å）与真正原子分辨率（<1.2 Å）有本质区别 | 影响对模型精度的预期 | 检查文中分辨率表述是否区分 | 文中使用"near-atomic"和"atomic"混用 |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **IDP/IDR 需要"系综思维"而非"单结构思维"**：AlphaFold 对 IDR 的预测不可靠（RMSD >5–10 Å），这提示在 IDP/IDR 介导的蛋白互作研究中，不应将 AI 预测的单一结构作为互作模型的基础，而应使用构象系综（如 IDPConformerGenerator 生成）来描述无序区域。可迁移：在相分离研究中，多价互作网络需要系综描述而非单一复合物结构。

2. **AI 与实验的整合是 IDP 研究的可行路径**：文中列举的整合方法（AI 预测 + cryo-EM 密度 + NMR/SAXS 约束）为 IDP 系统提供了建模框架。可迁移：对 IDP 介导的互作，可先用 AlphaFold 预测折叠域结构，再用 NMR/SAXS/FRET 约束无序区域的系综分布，最后构建全长的整合模型。

3. **构象异质性分析是 cryo-EM 对 IDP 研究的关键贡献**：cryo-EM 的 3D 分类和 CryoDRGN 等工具可揭示构象连续体，这对 IDP 的"构象景观"研究有直接借鉴意义。可迁移：相分离中的多价互作可能产生多种亚稳态构象，cryo-EM 异质性分析可用于表征这些状态。

4. **AI 置信度指标在 IDP 上不可靠**：pLDDT 高值不一定对应生物学准确性，这对使用 AlphaFold 预测 IDP 互作界面的研究是重要警示。可迁移：在 IDP/IDR 互作预测中，应结合实验验证或交叉验证，而非仅依赖置信度分数。

5. **环境条件对 IDP 构象的影响被 AI 忽略**：pH、离子强度、PTM 等对 IDP 构象和相分离行为有重大影响，但当前 AI 工具不考虑这些因素。可迁移：在 IDP/相分离研究中，需将环境参数作为显式变量纳入建模。

6. **标准化数据集是 AI 方法发展的关键**：CryoPPP 的建立推动了粒子挑选算法的进步。可迁移：IDP/相分离领域需要类似的标准化数据集（如带注释的凝聚体图像、IDP 构象系综基准）来推动 AI 方法发展。

## 15 与已有知识连接

- **AlphaFold2/3 与 IDP 预测**：文中引用的 Jumper et al. (2021) 和 Tunyasuvunakool et al. (2021) 是 AlphaFold 系列的核心文献。已知 AlphaFold 对 IDR 的预测不可靠，这与 CASP15 中 IDP 目标的评估结果一致（外部知识）。可连接：Ruff & Pappu (2021) 对 AlphaFold 在 IDP 上应用的系统讨论。

- **Cryo-EM 分辨率革命**：文中引用的 X. Li et al. (2013) 是直接电子探测器的里程碑工作。Kühlbrandt (2014) 综述了分辨率革命。可连接：Cheng et al. (2015) 对 cryo-EM 技术发展的综述。

- **IDP 构象系综方法**：文中提到的 IDPConformerGenerator (Teixeira et al., 2022) 和 ALBATROSS (Lotthammer et al., 2024) 是 IDP 计算方法的代表。可连接：METADOCK、IDP-SP 等 IDP 对接方法（外部知识），以及用于相分离预测的 catGRANULATOR、PSPredictor 等工具。

- **整合建模**：文中引用的核孔复合物研究（Schotte et al., 2003 等）是整合建模的经典案例。可连接：Integrative Modeling Platform (IMP) 和 I-TASSER 等工具（外部知识）。

- **Cryo-EM 与 AI 的端到端整合**：文中提到的 DeepTracer、ModelAngelo、CryoDRGN 等工具代表了 AI 在 cryo-EM 各环节的应用。可连接：2024 年 Nature 发表的 AI 辅助 cryo-EM 自动建模工作（外部知识）。

- **相分离与结构生物学**：文中未讨论相分离，但 IDP 的构象系综方法可直接迁移到相分离研究。可连接：Banani et al. (2017) 对相分离的综述，以及针对凝聚体的粗粒化模拟方法（如 MARTINI 3）。

## 16 研究想法

**Agent 生成的研究候选**：

1. **名称**：IDP-AI 互作预测基准（IDP-PPI-Bench）
   - **来源局限/观察**：本文指出 AlphaFold 对 IDR 预测不可靠，但缺乏系统量化 IDP 互作预测能力的基准
   - **核心假设**：现有 AI 互作预测工具（AlphaFold-Multimer、RoseTTAFold 等）在 IDP 参与的互作上准确率显著低于折叠蛋白互作
   - **初步方法**：构建包含实验验证的 IDP 互作数据集（从 PDB、BioGRID、IntAct 收集），按 IDR 长度、无序程度、互作类型分层，评估现有工具
   - **验证方式**：与实验结构/交联数据对比，计算 DockQ、LRMSD 等指标
   - **可能的失败模式**：IDP 互作实验数据稀缺，数据集规模不足
   - **创新状态**：unverified

2. **名称**：Cryo-EM 密度引导的 IDP 构象系综生成（CryoIDP-Ensemble）
   - **来源局限/观察**：文中提到 cryo-EM 可捕获构象异质性（CryoDRGN），但未与 IDP 系综生成器结合
   - **核心假设**：cryo-EM 的低分辨率密度图可作为约束，引导 IDP 构象系综生成，提高系综与实验数据的一致性
   - **初步方法**：将 CryoDRGN 学习的构象景观与 IDPConformerGenerator 的采样结合，用 cryo-EM 密度作为评分函数约束
   - **验证方式**：对已知 IDP 系统（如 p53、α-synuclein）比较生成系综与 NMR/SAXS 实验数据的吻合度
   - **可能的失败模式**：cryo-EM 密度分辨率不足以约束 IDP 的局部构象
   - **创新状态**：unverified

3. **名称**：相分离蛋白的 AlphaFold 置信度与凝聚体倾向性关联分析
   - **来源局限/观察**：文中指出 pLDDT 在 IDR 上可能误导，但未探讨 pLDDT 与相分离行为的关系
   - **核心假设**：相分离蛋白的 IDR 区域 pLDDT 分布模式（如低 pLDDT 的连续片段长度）与凝聚体形成倾向相关
   - **初步方法**：收集已知相分离蛋白（PhosphoSitePlus、LLPSDB），提取 AlphaFold pLDDT 特征，与相分离能力评分（如 catGRANULATOR）关联
   - **验证方式**：统计检验 + 独立验证集
   - **可能的失败模式**：pLDDT 与相分离行为无直接关联，需引入更多特征
   - **创新状态**：unverified

4. **名称**：整合 cryo-EM 与 AI 预测的 IDP 介导凝聚体多价互作建模
   - **来源局限/观察**：文中提到整合方法可解析大复合物（NPC），但未延伸到凝聚体尺度
   - **核心假设**：将 cryo-EM 亚基结构、AI 预测的 IDR 构象、交联质谱约束整合，可构建凝聚体中多价互作网络模型
   - **初步方法**：以已知形成凝聚体的信号复合物（如 T-cell 信号复合物）为模型系统，整合 cryo-EM 密度、AlphaFold 预测、XL-MS 数据，用分子模拟（粗粒化）生成凝聚体模型
   - **验证方式**：与体外凝聚体实验（浊度、FRAP）对比
   - **可能的失败模式**：计算成本过高，凝聚体尺度超出当前模拟能力
   - **创新状态**：unverified

5. **名称**：环境条件感知的 IDP 构象预测模型（EnvIDP）
   - **来源局限/观察**：文中指出 AI 预测忽略 pH、离子强度等环境因素，这对 IDP 尤其关键
   - **核心假设**：将环境参数（pH、盐浓度、温度）作为显式输入，可显著提高 IDP 构象系综预测的准确性
   - **初步方法**：在现有 IDP 预测器（如 ALBATROSS）基础上，增加环境条件编码器，用实验数据（NMR、SAXS 在不同条件下的测量）训练
   - **验证方式**：对未见过的环境条件进行预测，与实验对比
   - **可能的失败模式**：实验数据覆盖不足，环境参数与构象关系复杂
   - **创新状态**：unverified