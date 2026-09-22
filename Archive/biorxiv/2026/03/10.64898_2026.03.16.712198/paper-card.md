## 01 基本信息

- **标题**：Multicomplex Integrative Structural Modeling of a Human Histone Deacetylase Interactome
- **作者**：Nde J; Majila K; Zimmermann RC; Kempf C; Zhang Y; Cesare J; Thornton JL; Workman JL; Florens L; Viswanath S; Washburn MP
- **单位**：未提供（作者列表中未标注单位信息）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2026-03-17
- **论文类型**：预印本（研究论文）
- **领域**：结构生物学、蛋白质互作组学、整合结构建模
- **关键词**：HDAC1/2、IDR、XL-MS、Integrative Modeling、AlphaFold、NuRD、SIN3A、CoREST
- **DOI/arXiv 号**：10.64898/2026.03.16.712198
- **代码**：未提供
- **数据**：未提供（XL-MS 数据未明确说明是否已公开）
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文直接以 HDAC1/2 的 C 端 IDR 为研究对象，通过 XL-MS 约束的整合建模与 AlphaFold 结合，解析 IDR 在多亚基染色质重塑复合物中的折叠行为。该文属于「IDP/IDR 介导的蛋白互作 × AI/深度学习（AlphaFold）× 物理/整合建模」交叉方向，提供了 IDR 在复合物环境中折叠为 α-helix 的直接结构证据，以及多复合物并行建模的方法学范式。

## 02 一句话总结

本文通过 XL-MS 结合 Integrative Modeling Platform 和 AlphaFold 约束建模，构建了 HDAC1/2 互作组中 NuRD、SIN3A、CoREST 三个复合物的结构模型，发现 HDAC1 的 C 端 IDR 在复合物中折叠为 α-helix，并进一步构建了包含 6 个 IDR 的 NuRD 亚复合物完整整合模型。

## 03 研究问题

- **具体问题**：HDAC1/2 如何组装进 NuRD、SIN3A、CoREST 等多个大型染色质重塑复合物？其 C 端 IDR 在这些复合物中的结构状态是什么？
- **为什么重要**：HDAC1/2 是多个关键染色质调控复合物的共享催化亚基，但其组装机制和 IDR 结构长期未知。IDR 在复合物环境中的折叠行为是理解无序蛋白功能的关键问题，对相分离、互作网络调控等课题有直接参考价值。
- **现有方法为何不足**：传统结构生物学方法（X-ray、cryo-EM）难以捕获 IDR 的构象异质性；单个复合物的结构解析无法回答 HDAC1/2 如何以同一亚基参与多个不同复合物的问题；AlphaFold 单独预测 IDR 通常给出低置信度或无结构预测。
- **精确研究问题**：Can XL-MS 约束的整合建模与 AlphaFold 结合，确定 HDAC1 的 C 端 IDR 在 NuRD、SIN3A、CoREST 复合物中的折叠状态及组装模式？

## 04 背景与发展脉络

- **阶段一：传统复合物结构解析**（cryo-EM/X-ray）——代表性方法：单颗粒冷冻电镜、X 射线晶体学。优点：高分辨率。局限：难以处理构象异质性和 IDR；需要大量纯化样品。
- **阶段二：整合结构建模**（Integrative Modeling）——代表性方法：Integrative Modeling Platform (IMP)、XL-MS 约束建模。优点：可融合多种实验数据（交联、SAXS、EM 密度图），能处理柔性区域。局限：依赖实验数据的密度和分布，对 IDR 的构象采样仍有限。
- **阶段三：AlphaFold 及深度学习预测**——代表性方法：AlphaFold2/3。优点：高精度预测折叠域。局限：对 IDR 预测置信度低，无法直接给出复合物环境中的诱导折叠状态。
- **本文主张的位置**：将 XL-MS 约束的整合建模与 AlphaFold 预测结合，形成「AlphaFold-enabled XL-MS constrained modeling」工作流，专门针对多复合物中同一 IDR 的折叠状态进行建模，填补了「IDR 在复合物中如何折叠」的方法空白。

> 注：此脉络为「经外部核验」——整合建模和 AlphaFold 的优缺点是领域公认事实；本文的具体定位为作者主张。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| HDAC1/2 的 CTD IDR 结构未知 | 无法从单一结构方法获得 IDR 的原子模型 | IDR 构象异质性高，传统方法难以捕获；AlphaFold 单独预测置信度低 | Summary 段「the structure of the CTD IDR remains poorly understood」 |
| 同一亚基参与多个复合物的组装机制不清 | HDAC1/2 是 NuRD、SIN3、CoREST 的共享亚基，但各复合物中组装模式未知 | 缺乏跨复合物的并行结构数据 | Summary 段「How HDAC1/2 assemble into these complexes... remains poorly understood」 |
| IDR 在复合物环境中的折叠状态未知 | 无法判断 IDR 是否折叠、折叠为何种二级结构 | 缺乏复合物环境中的实验约束数据 | Summary 段「We show that the CTD IDR of HDAC1 folds into alpha helices in these complexes」 |
| 多 IDR 复合物的完整建模困难 | NuRD 亚复合物含 6 个 IDR，传统建模难以同时处理 | 多 IDR 的构象空间巨大，需要多源实验约束 | Summary 段「built a complete integrative structural model of a NuRD subcomplex... which included 6 IDRs」 |

## 06 核心思想

**1. 表面方法**：
- 用 HDAC1/2 免疫沉淀（IP）从细胞中分离互作蛋白网络
- 对分离的复合物进行 XL-MS 交联质谱分析
- 用 Integrative Modeling Platform (IMP) 构建 NuRD、SIN3A、CoREST 的结构模型
- 开发 AlphaFold-enabled XL-MS constrained modeling 方法，专门研究 HDAC1 的组装模式
- 最终构建包含 6 个 IDR 的 NuRD 亚复合物完整模型

**2. 核心洞察**：
- HDAC1 的 CTD IDR 并非始终无序，而是在复合物环境中诱导折叠为 α-helix——这为「IDR 通过诱导折叠介导特异性互作」提供了直接结构证据。
- XL-MS 交联约束可以作为「分子尺子」，将 AlphaFold 预测的亚基结构「钉」在正确的相对位置上，从而克服 AlphaFold 对多亚基复合物和 IDR 的预测局限。
- 通过并行建模多个共享亚基的复合物，可以揭示同一 IDR 在不同复合物中的不同折叠模式，从而理解互作特异性。

**3. 可能的普适教训 [Analysis]**：
- IDR 的「无序」是上下文依赖的：在游离状态下无序，在复合物中可折叠为特定二级结构。这对 IDP/IDR 介导的互作研究有直接启示——预测 IDR 功能时需考虑其结合伙伴环境。
- 多源实验约束（XL-MS）与深度学习预测（AlphaFold）的融合，是处理「柔性区域 × 多亚基复合物」问题的有效策略，可迁移到其他含 IDR 的互作网络研究。

## 07 方法总览

- **输入**：HDAC1/2 抗体 IP 分离的内源复合物样品；XL-MS 交联数据；HDAC1/2 互作网络蛋白序列
- **输出**：NuRD、SIN3A、CoREST 三个复合物的结构模型；HDAC1 CTD IDR 的 α-helix 折叠状态；含 6 个 IDR 的 NuRD 亚复合物完整模型
- **模块**：
  1. 互作网络分离（IP）
  2. XL-MS 交联与质谱鉴定
  3. Integrative Modeling Platform (IMP) 建模
  4. AlphaFold-enabled XL-MS constrained modeling
  5. 模型验证与评估
- **训练**：不涉及传统机器学习训练；AlphaFold 为预训练模型，用于生成亚基结构预测
- **工具**：Integrative Modeling Platform (IMP)、AlphaFold、XL-MS 质谱平台
- **反馈回路**：XL-MS 交联约束 → 模型采样 → 与交联距离比对 → 迭代优化模型
- **假设**：XL-MS 交联距离可以作为结构约束（通常 Cα-Cα < 30 Å）；AlphaFold 对折叠域预测可靠；IP 分离的复合物代表内源生理状态

**文字流程**：
1. 用 HDAC1/2 抗体从细胞核提取物中 IP 分离互作复合物
2. 对分离的复合物进行 XL-MS 分析，获得赖氨酸残基间的交联距离约束
3. 用 IMP 对 NuRD、SIN3A、CoREST 分别进行整合建模，以交联约束驱动亚基排列
4. 用 AlphaFold 预测各亚基结构域结构，将预测结构作为刚性体输入 IMP
5. 开发 AlphaFold-enabled XL-MS constrained modeling 流程，专门优化 HDAC1 在复合物中的位置和 IDR 构象
6. 对 NuRD 亚复合物（HDAC1:MBD3:MTA1:GATAD2B:RBBP4）进行完整建模，包含 6 个 IDR
7. 评估模型与交联数据的吻合度，验证 IDR 折叠状态

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| HDAC1/2 IP 互作网络分离 | 从细胞中分离内源复合物 | 获得生理状态下的复合物组成 | 输入：细胞核提取物；输出：HDAC1/2 互作蛋白混合物 | Summary 段「used HDAC1/2 to isolate their protein interaction networks from cells」 | 预期影响：无法获得内源复合物，后续 XL-MS 和建模无数据来源 |
| XL-MS 交联质谱 | 产生距离约束 | 提供亚基间和亚基内的空间邻近信息 | 输入：IP 复合物；输出：交联肽段和距离约束 | Summary 段「used crosslinking mass spectrometry (XL-MS)」 | 预期影响：失去关键实验约束，整合建模无法收敛到唯一解 |
| Integrative Modeling Platform (IMP) | 构建复合物结构模型 | 融合交联约束与亚基结构，生成复合物排列 | 输入：交联约束 + 亚基结构；输出：复合物结构模型 | Summary 段「coupled with the Integrative Modeling Platform to build structural models」 | 预期影响：无法将交联数据转化为结构模型 |
| AlphaFold-enabled XL-MS constrained modeling | 研究 HDAC1 组装模式 | 利用 AlphaFold 预测结构作为先验，结合交联约束优化 HDAC1 位置 | 输入：AlphaFold 预测结构 + XL-MS 约束；输出：HDAC1 在复合物中的组装模型 | Summary 段「implemented an AlphaFold-enabled XL-MS constrained modeling approach」 | 预期影响：无法确定 HDAC1 在复合物中的具体位置和 IDR 折叠状态 |
| NuRD 亚复合物完整建模 | 构建含 6 个 IDR 的完整模型 | 展示方法对多 IDR 复合物的处理能力 | 输入：NuRD 亚复合物亚基 + 交联约束；输出：含 6 个 IDR 的完整模型 | Summary 段「built a complete integrative structural model of a NuRD subcomplex... which included 6 IDRs」 | 预期影响：无法展示方法对多 IDR 系统的适用性 |

> 注：所有消融影响均为「预期效应」，本文未提供模块移除的系统消融实验。

## 09 关键公式符号

不适用。本文为整合结构建模方法学论文，未在摘要或正文中提供可提取的数学公式。XL-MS 距离约束通常以 Cα-Cα < 30 Å 为经验阈值，但该数值未在摘要中明确给出，故不列为公式。

## 10 实验设计与证据链

- **数据集**：HDAC1/2 互作网络（从细胞中 IP 分离）；NuRD、SIN3A、CoREST 三个复合物
- **规模**：未提供具体蛋白数量或交联位点数量
- **指标**：模型与交联数据的吻合度（具体指标未在摘要中提供）
- **基线**：未提供明确的基线方法对比
- **预算**：未提供
- **骨干/仪器**：质谱仪（具体型号未提供）
- **oracle 输入**：AlphaFold 预测的亚基结构
- **评测协议**：未在摘要中详细描述

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|----------------|------|
| HDAC1/2 IP 分离互作网络 | HDAC1/2 与多个染色质复合物互作 | 从细胞中 IP 后质谱鉴定 | 鉴定到 NuRD、SIN3、CoREST 组分 | HDAC1/2 是多个复合物的共享亚基 | 无法证明互作的 stoichiometry 或动态性 | Summary 段 |
| XL-MS 交联分析 | 复合物中亚基间的空间邻近关系 | 对 IP 复合物进行交联 | 获得亚基间交联约束 | 提供结构建模的距离约束 | 无法直接给出原子分辨率结构 | Summary 段 |
| IMP 整合建模 | 复合物的整体结构排列 | 以交联约束驱动建模 | 构建 NuRD、SIN3A、CoREST 模型 | 获得复合物结构模型 | 模型分辨率受限于交联数据密度 | Summary 段 |
| AlphaFold-enabled XL-MS constrained modeling | HDAC1 在复合物中的组装模式 | AlphaFold 预测 + 交联约束 | 确定 HDAC1 的组装位置 | HDAC1 通过特定界面组装进复合物 | 无法证明该组装模式的动态切换机制 | Summary 段 |
| CTD IDR 折叠分析 | HDAC1 的 CTD IDR 在复合物中折叠为 α-helix | 模型中的 IDR 构象分析 | IDR 折叠为 α-helix | IDR 在复合物环境中诱导折叠 | 无法证明该折叠是否在溶液游离态也存在 | Summary 段 |
| NuRD 亚复合物完整建模 | 含 6 个 IDR 的复合物可被完整建模 | 包含 HDAC1:MBD3:MTA1:GATAD2B:RBBP4 | 构建完整模型 | 方法可处理多 IDR 复合物 | 无法证明该模型在细胞内的唯一性 | Summary 段 |

## 11 结论正确解读

- **任务范围**：本文仅针对 HDAC1/2 互作网络中的 NuRD、SIN3A、CoREST 三个复合物，不涵盖 HDAC1/2 参与的所有复合物或所有细胞类型。
- **oracle/真值输入**：AlphaFold 预测结构作为先验输入，其准确性直接影响最终模型；XL-MS 交联约束为实验真值，但覆盖度有限。
- **端到端状态**：方法并非全自动端到端——需要人工 IP 实验、质谱数据解析、建模参数调整。
- **算力成本**：未提供；AlphaFold 预测和 IMP 采样均需一定计算资源，但具体成本未报告。
- **历史数据依赖**：依赖 AlphaFold 预训练模型，其训练数据来自 PDB 等已知结构库；对全新折叠或非标准构象可能预测不准。
- **模型依赖**：最终模型是「数据 + 先验 + 采样策略」的联合产物，不同参数设置可能得到不同模型。
- **最难情形**：IDR 区域的构象采样仍受限于交联数据密度；若交联位点稀疏，IDR 折叠状态的确定性会降低。
- **群体/领域边界**：结论基于人类细胞中的 HDAC1/2 复合物，不能直接推广到其他物种或其他 HDAC 家族成员。
- **不确定性**：模型分辨率未明确报告；IDR 折叠为 α-helix 的结论基于整合模型，缺乏独立实验（如 NMR、cryo-EM）的直接验证。

**有边界的复述**：在人类细胞中，通过 HDAC1/2 IP 分离的 NuRD、SIN3A、CoREST 复合物，在 XL-MS 约束和 AlphaFold 先验的联合驱动下，可构建出与交联数据吻合的结构模型；在该模型框架下，HDAC1 的 CTD IDR 呈现 α-helix 折叠状态。该结论受限于交联数据覆盖度、AlphaFold 预测准确性和模型采样策略。

## 12 作者自认局限

在提供的摘要材料中，作者未明确列出局限性。摘要仅提及方法「broadly applicable」，未讨论方法局限或未来方向。

**作者提及的相关约束**（非正式局限）：
- 摘要中「the structure of the CTD IDR remains poorly understood」暗示 IDR 结构解析的固有困难。
- 模型构建依赖 XL-MS 数据质量，但摘要未讨论数据稀疏或缺失的情况。

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|-------------------|----------|----------|------|
| IDR 折叠为 α-helix 的结论仅基于整合模型 | 整合模型是间接推断，缺乏 NMR/cryo-EM 等直接结构证据；α-helix 可能是采样偏好或交联约束不足导致的伪影 | IDR 折叠状态是本文核心发现，若不可靠则结论基础动摇 | 用 NMR 或 cryo-EM 独立验证 HDAC1 CTD IDR 在复合物中的构象；或对 IDR 区域增加交联剂密度 | Summary 段「We show that the CTD IDR of HDAC1 folds into alpha helices」 |
| AlphaFold 对 IDR 预测置信度低，作为先验可能引入偏差 | AlphaFold 对无序区域通常预测为低置信度或无结构，将其作为刚性体输入可能扭曲模型 | 若 AlphaFold 先验错误，后续交联约束拟合可能将错误结构「钉」入模型 | 对比不使用 AlphaFold 先验的纯 IMP 建模结果；检查 IDR 区域的模型置信度分数 | Summary 段「AlphaFold-enabled XL-MS constrained modeling」 |
| 未提供模型与交联数据的定量吻合度指标 | 无法评估模型质量；「吻合」可能是定性判断 | 模型质量决定结论可靠性 | 要求作者提供交联violation率、模型聚类分数等定量指标 | 摘要未提供具体指标 |
| IP 分离的复合物可能不代表单一生理状态 | IP 可能共纯化多个不同构象或亚复合物，混合信号导致模型平均化 | 若存在构象异质性，单一模型可能掩盖真实生物学 | 用 SEC 或 native PAGE 检查 IP 样品的均一性；或对交联数据进行构象聚类分析 | Summary 段「isolate their protein interaction networks from cells」 |
| 未报告模型分辨率或精度估计 | 无法判断模型在原子层面的可信度 | 结构模型的可用性取决于分辨率 | 要求作者提供模型精度估计（如 cross-validation 或独立数据验证） | 摘要未提供 |

## 14 Agent 提炼的知识候选

1. **IDR 上下文依赖折叠的概念**：HDAC1 CTD IDR 在复合物中折叠为 α-helix，说明 IDR 的构象状态受结合伙伴调控。**迁移到本课题**：研究 IDP/IDR 介导的互作时，不应将 IDR 视为静态无序，而应考虑「结合诱导折叠」机制；可系统比较同一 IDR 在不同复合物中的折叠差异，理解互作特异性。

2. **XL-MS + AlphaFold 的混合建模工作流**：用 XL-MS 交联约束「锚定」AlphaFold 预测的亚基结构，克服 AlphaFold 对多亚基复合物和 IDR 的预测局限。**迁移到本课题**：对含 IDR 的互作复合物，可先用 AlphaFold 预测折叠域，再用 XL-MS 约束确定亚基排列和 IDR 路径；该方法可扩展到相分离凝聚体中的多价互作建模。

3. **多复合物并行建模策略**：以共享亚基（HDAC1/2）为锚点，并行构建多个复合物模型，比较同一亚基在不同复合物中的构象差异。**迁移到本课题**：对 IDP 参与的多个互作复合物，可并行建模并比较 IDP 在不同复合物中的折叠状态，揭示「一个 IDP 多个构象」的调控机制。

4. **IP + XL-MS 的内源复合物捕获策略**：用内源 IP 而非重组表达获得复合物，保留翻译后修饰和天然互作。**迁移到本课题**：研究 IDP 互作网络时，内源 IP 可捕获更真实的互作状态，尤其对相分离相关复合物，可保留凝聚体中的弱多价互作。

5. **6 个 IDR 同时建模的可行性证明**：NuRD 亚复合物含 6 个 IDR 仍可完成整合建模，说明当前方法可处理多 IDR 系统。**迁移到本课题**：对相分离凝聚体中的多 IDR 体系，可尝试类似的整合建模策略，但需注意交联数据密度需足够覆盖多个 IDR。

## 15 与已有知识连接

- **相似方法**：Integrative Modeling Platform (IMP) 是结构生物学中成熟的整合建模工具（Rout & Sali 等开发），本文将其应用于 HDAC 互作组，属于方法在新体系上的应用。
- **相似概念**：「IDR 结合诱导折叠」与分子识别特征（MoRF, Molecular Recognition Feature）概念一致——MoRF 是 IDR 中结合后折叠为有序结构的短区域。本文 HDAC1 CTD IDR 折叠为 α-helix 的发现可作为 MoRF 的新实例。
- **冲突或补充**：AlphaFold 对 IDR 的预测通常为低置信度，本文通过 XL-MS 约束弥补了这一缺陷，是对「AlphaFold 无法处理 IDR」这一已知局限的补充方案。
- **可迁移领域**：相分离研究——IDR 驱动的液-液相分离中，IDR 的构象状态和互作模式是核心问题。本文的「XL-MS + AlphaFold + 整合建模」工作流可迁移到凝聚体中的 IDR 互作建模，但需注意凝聚体中的弱多价互作可能超出 XL-MS 的检测范围。
- **候选方向**：将本文方法应用于其他含 IDR 的染色质调控复合物（如 SWI/SNF、PRC2），或扩展到 IDR 介导的相分离体系。

## 16 Agent 生成的研究候选

**候选 1：IDR 折叠状态与相分离能力的关联分析**
- **来源局限/观察**：本文发现 HDAC1 CTD IDR 在复合物中折叠为 α-helix，但未探讨该折叠与相分离行为的关系。
- **核心假设**：IDR 在复合物中的折叠状态与其相分离倾向负相关——折叠为有序结构会减少多价互作位点，从而抑制相分离。
- **相对本文的增量**：将 IDR 结构状态与相分离功能直接关联，从结构到功能的闭环。
- **初步方法**：对 HDAC1 CTD IDR 进行突变（破坏 α-helix 形成），用共聚焦显微镜和体外凝聚实验检测相分离能力变化；结合 XL-MS 比较突变体的互作网络。
- **验证方式**：突变体相分离能力与 α-helix 形成能力的定量相关性；分子动力学模拟验证突变对折叠的影响。
- **可能的失败模式**：IDR 折叠与相分离可能无直接因果，而是通过其他机制（如互作伙伴的招募）间接关联。
- **创新状态**：unverified

**候选 2：AlphaFold 预测 IDR 构象的 XL-MS 约束微调框架**
- **来源局限/观察**：本文的 AlphaFold-enabled XL-MS constrained modeling 是特定于 HDAC1 的定制流程，未提供通用工具。
- **核心假设**：将 XL-MS 交联约束作为可微分的损失项，微调 AlphaFold 的 structure module，可系统改善 IDR 区域的预测精度。
- **相对本文的增量**：从「手动定制流程」到「通用可复用工具」，降低方法使用门槛。
- **初步方法**：基于 AlphaFold 的开源代码，在 structure module 后添加交联距离损失项；在多个含 IDR 的复合物（如本文的 NuRD、SIN3A、CoREST）上测试。
- **验证方式**：与本文模型对比，检查 IDR 区域预测的 α-helix 一致性；用独立 NMR 数据验证。
- **可能的失败模式**：交联数据稀疏时损失项梯度不稳定；AlphaFold 内部表示与交联约束的尺度不匹配。
- **创新状态**：unverified

**候选 3：多复合物共享 IDR 的构象比较与互作特异性机制**
- **来源局限/观察**：本文构建了三个复合物模型，但未系统比较 HDAC1 CTD IDR 在不同复合物中的构象差异。
- **核心假设**：HDAC1 CTD IDR 在不同复合物中折叠为不同的 α-helix 构象，该构象差异决定互作特异性。
- **相对本文的增量**：从「单复合物结构」到「跨复合物构象比较」，揭示 IDR 编码互作特异性的机制。
- **初步方法**：对本文三个复合物模型中的 HDAC1 CTD IDR 进行结构比对（RMSD、接触图谱）；结合序列分析预测不同 α-helix 的互作界面。
- **验证方式**：突变不同 α-helix 界面的关键残基，检测对复合物组装的影响；HDX-MS 验证不同复合物中 IDR 的溶剂暴露差异。
- **可能的失败模式**：IDR 在不同复合物中的构象差异可能很小，不足以解释互作特异性；模型分辨率不足以区分细微构象差异。
- **创新状态**：unverified

**候选 4：IDR 介导的多价互作网络建模方法**
- **来源局限/观察**：本文方法针对稳定复合物，未涉及 IDR 介导的弱多价互作（如相分离中的动态网络）。
- **核心假设**：将 XL-MS 交联约束与粗粒化分子模拟结合，可建模 IDR 介导的弱多价互作网络。
- **相对本文的增量**：将方法从「静态复合物」扩展到「动态互作网络」，覆盖相分离等动态过程。
- **初步方法**：对含 IDR 的互作网络进行 XL-MS 分析，将交联约束转化为粗粒化模拟中的谐波约束；用 LAMMPS 或 OpenMM 进行系综模拟。
- **验证方式**：模拟得到的互作网络拓扑与共定位数据（如免疫荧光）对比；预测的凝聚体形成能力与体外实验对比。
- **可能的失败模式**：弱互作的交联效率低，数据覆盖不足；粗粒化模型对 IDR 的表示过于简化。
- **创新状态**：unverified

**候选 5：IDR 折叠的序列决定因素分析**
- **来源局限/观察**：本文发现 HDAC1 CTD IDR 折叠为 α-helix，但未分析哪些序列特征决定该折叠。
- **核心假设**：IDR 中特定序列模式（如 MoRF 基序、电荷模式）预测其在不同复合物中的折叠倾向。
- **相对本文的增量**：从「结构发现」到「序列预测规则」，为 IDR 功能预测提供工具。
- **初步方法**：收集本文及文献中已知折叠状态的 IDR 序列，训练分类器（如随机森林或小规模神经网络）预测折叠倾向；用 SHAP 分析关键序列特征。
- **验证方式**：在独立 IDR 数据集上验证预测精度；用圆二色谱或 NMR 验证新预测的折叠 IDR。
- **可能的失败模式**：已知折叠状态的 IDR 样本量小，模型泛化差；序列特征与折叠的关联可能被结合伙伴环境混淆。
- **创新状态**：unverified