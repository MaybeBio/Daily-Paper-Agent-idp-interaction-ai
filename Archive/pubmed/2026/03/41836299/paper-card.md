## 01 基本信息

- **标题**：Unlocking the undruggable spliceosome: generative AI and structural dynamics in cancer therapy
- **作者与单位**：Steuer, Jakob; Kahraman, Abdullah（单位未提供）
- **期刊/预印本平台**：Frontiers in Cell and Developmental Biology
- **年份**：2026
- **论文类型**：综述（Review）
- **领域**：癌症治疗、剪接体结构动态、生成式AI、分子模拟
- **关键词**：spliceosome, SF3B1, U2AF1, SRSF2, generative AI, molecular dynamics, cryptic pockets, IDRs, neoantigens, synthetic lethality
- **DOI/arXiv 号**：10.3389/fcell.2026.1774239
- **代码**：未提供
- **数据**：未提供
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文是综述，聚焦剪接体（spliceosome）这一大型动态核糖核蛋白机器，系统论述了将物理模拟（MD、增强采样）与生成式AI结合，用于解析剪接因子突变（SF3B1、U2AF1、SRSF2）的结构动态后果、发现隐蔽变构口袋、靶向无序区（IDR），并延伸至合成致死与剪接来源新抗原的精准免疫治疗。与课题方向（IDP/IDR介导的蛋白互作 × AI/物理模拟）高度相关：剪接因子（如SRSF2、U2AF1）本身含IDR/RS结构域，且文中明确将IDR列为治疗靶点，并讨论了LLPS/核斑点的作用。

## 02 一句话总结

本文通过综述物理模拟（MD、增强采样）与生成式AI（AlphaFold3、Boltz-2、ProteinMPNN、RFDpoly等）的融合路径，论证了从静态冷冻电镜快照转向动态结构系综是解锁剪接体这一"不可成药"靶点的关键，并据此提出靶向隐蔽变构口袋、IDR、合成致死及剪接新抗原的精准治疗路线图。

## 03 研究问题

- **具体问题**：剪接体因体积巨大、高度动态、缺乏深疏水口袋而被视为"不可成药"靶点。癌症中反复出现的剪接因子突变（SF3B1、U2AF1、SRSF2）如何从结构动态层面被靶向？如何将结构动态信息转化为临床可用的治疗策略？
- **为什么重要**：剪接因子突变在血液恶性肿瘤（MDS、CLL）和实体瘤（葡萄膜黑色素瘤、乳腺癌）中高频出现，且现有药物（如E7107、H3B-480）因选择性差、毒性大而失败。理解突变如何重塑剪接体的结构动态，是开发选择性疗法的前提。
- **现有方法为何不足**：冷冻电镜仅提供静态快照，无法捕捉瞬时的中间态、呼吸运动和隐蔽口袋；经典平衡MD受限于时间尺度和系统规模，难以采样毫秒级剪接体重排；传统药物设计依赖静态结构上的深口袋，而剪接因子界面平坦、动态性强。
- **精确的"Can ... ?"研究问题**：Can the integration of enhanced sampling molecular dynamics and generative AI identify transient cryptic pockets and IDR-binding sites on mutant spliceosomal factors (SF3B1, U2AF1, SRSF2) that are invisible to static cryo-EM structures, and can these sites be exploited for selective therapeutic intervention?

## 04 背景与发展脉络

**脉络标注**：以下脉络基于本文框架，未经外部系统核验。

1. **阶段一：静态结构解析（~2015-2020）**——冷冻电镜"分辨率革命"提供了剪接体各离散状态的原子级结构（B、Bact、C等复合物）。代表：Wahl et al. (2009) 综述剪接体组装；Vorländer et al. (2022)、Tholen & Galej (2022) 的结构研究。**优点**：原子级分辨率。**局限**：仅代表深能量极小值，无法捕捉动态过渡和瞬时状态。

2. **阶段二：经典MD模拟（~2015-至今）**——对剪接体亚复合物进行原子级MD，用于精修冷冻电镜模型、探测局部柔性、合理化突变效应。代表：Pokorná et al. (2025) 综述。**优点**：提供原子级动态信息。**局限**：时间尺度差距（微秒 vs 毫秒-秒）、力场精度不足、系统规模过大。

3. **阶段三：增强采样方法（~2020-至今）**——加权系综（WE）、元动力学、副本交换（REMD）等方法用于稀有事件采样。**优点**：可访问高能中间态。**局限**：仍需合理的反应坐标定义，对超大系统仍昂贵。

4. **阶段四：生成式AI与基础模型（~2021-至今）**——AlphaFold2/3、Boltz-2、CHai-1 等结构预测模型；ProteinMPNN、RFDpoly 等逆向设计工具；RiNALMo、ERNIE-RNA、TrASPr 等RNA/剪接语言模型。**优点**：可快速生成结构假设、设计新结合物、预测剪接结果。**局限**：可能"幻觉"看似合理但物理上不可能的构象；对IDR预测不可靠；缺乏热力学校准。

5. **本文主张的位置**：主张将上述方法**融合**——用生成式AI提出结构假设，用增强采样MD验证和细化，用自由能计算（FEP）量化结合亲和力，形成"AI提出-物理验证-实验确认"的闭环，并延伸至新抗原预测和合成致死策略。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 时间尺度差距 | 常规MD仅达微秒级，而剪接体重排发生在毫秒至秒级 | 系统规模大（兆道尔顿）、自由能势垒高 | "This 3- to 6-order-of-magnitude gap means that straightforward equilibrium MD will overwhelmingly sample fluctuations near the starting structure"（Sampling gap 节） |
| 力场精度不足 | RNA磷酸骨架、Mg²⁺/K⁺配位、蛋白-RNA界面难以准确描述 | 经典非极化力场无法捕捉电荷转移和配位几何 | "standard non-polarizable models fail to capture the complex coordination geometry and charge transfer of catalytic Mg²⁺ and K⁺ ions"（Sampling gap 节） |
| 静态结构盲区 | 隐蔽变构口袋和中间态在冷冻电镜结构中不可见 | 冷冻电镜结构代表深能量极小值，瞬态构象未被捕获 | "cryo-EM structures represent deep free-energy minima, unbiased MD rarely accesses higher-energy intermediates where allosteric pathways and cryptic pockets often reside"（Sampling gap 节） |
| IDR难以建模 | 剪接因子（如SRSF2、U2AF1）的无序区无法用传统结构预测和MD处理 | IDR缺乏稳定三级结构，构象系综庞大 | "target intrinsically disordered regions"被列为前沿方向，且IDR的构象异质性对高分辨率建模构成挑战（Dynamics 节、From static structure 节） |
| AI幻觉风险 | 生成式模型可能产生物理上不可能的构象或高置信度假阳性 | 模型训练数据偏差、缺乏物理约束 | "They can 'hallucinate' plausible-looking interactions for physically impossible contacts"（Validation 节） |
| 药物选择性差 | 第一代剪接体抑制剂（E7107、H3B-8800）因靶点毒性失败 | 缺乏突变特异性靶向，治疗窗口窄 | "E7107 was discontinued due to ocular toxicity, and H3B-8800 failed to achieve objective responses... hampered by on-target dose-limiting toxicities"（Direct modulation 节） |

## 06 核心思想

### 1) 表面方法

本文是一篇综述，系统梳理了：(a) 剪接体突变（SF3B1、U2AF1、SRSF2）的结构与功能后果；(b) 增强采样MD方法（MSMD、WE、元动力学、REMD）在隐蔽口袋发现中的应用；(c) 生成式AI（AF3、Boltz-2、RFDpoly、ProteinMPNN）在结构预测和结合物设计中的角色；(d) 从结构动态到临床策略的转化路径（合成致死、新抗原、变构调节）。

### 2) 核心洞察

**洞察一：剪接体突变是"结构动态疾病"而非简单的功能丧失。** 突变（如SF3B1 K700E）不是破坏蛋白折叠，而是重塑了剪接体组装的自由能景观，改变了对剪接位点的识别偏好。因此，靶向策略必须基于动态构象系综而非单一静态结构。

**洞察二：隐蔽口袋和IDR是"不可成药"表面的可成药入口。** 剪接因子在静态结构中缺乏深口袋，但其动态呼吸和IDR的构象转换会暴露瞬时的疏水裂隙和结合位点。MSMD等增强采样方法可以系统性地发现这些位点。

**洞察三：生成式AI与物理模拟是互补而非替代关系。** AI模型擅长从数据中学习序列-结构关系，但缺乏物理约束；MD模拟提供物理真实性但受限于采样。将AI生成的结构假设作为MD的起点，再用自由能计算筛选，可以同时克服两者的局限。

**洞察四：剪接突变产生的"公共新抗原"使"现成"免疫治疗成为可能。** 由于剪接因子突变以可预测方式影响剪接位点选择，产生的异常剪接异构体在不同患者间共享，这为开发部分通用型新抗原疫苗/TCR疗法提供了基础。

### 3) 可能的普适教训 [Analysis]

- **从"靶向静态口袋"到"靶向动态系综"**：对于 intrinsically disordered 或高度动态的蛋白互作界面，传统基于静态结构的药物设计范式需要升级为基于构象系综的"动态药理学"。这一思路可直接迁移到IDP/IDR介导的相分离体系——凝聚体中的蛋白互作位点可能同样依赖瞬态构象。
- **AI与物理模拟的"双向反馈"**：不仅是AI辅助MD（如生成初始构象），MD结果也可以反过来训练和校正AI模型（如用自由能数据微调扩散模型）。这种闭环在IDP研究中尤为重要，因为IDP的实验结构数据稀缺。
- **"功能选择性"优于"结合选择性"**：剪接体抑制剂的经验表明，即使药物同时结合野生型和突变型，突变细胞因对剪接扰动更敏感而表现出选择性杀伤。这一"合成致死"逻辑可推广到其他IDR相关疾病——靶向凝聚体的药物可能不需要严格区分突变/野生型，而是利用突变细胞的脆弱性。

## 07 方法总览

本文为综述，无原始方法。但文中提出了一个**集成计算流程**（From static structure to generative design 节）：

- **输入**：剪接因子突变信息（如SF3B1 K700E）、冷冻电镜结构、序列数据、RNA-seq剪接数据
- **模块1：结构预测**——AF3、Boltz-2、CHai-1 预测突变体与RNA/蛋白复合物结构
- **模块2：增强采样MD**——MSMD（隐蔽口袋作图）、WE（稀有过渡路径）、元动力学（自由能景观）、REMD（IDR构象采样）
- **模块3：生成式设计**——RFDpoly（核酸-蛋白复合物设计）、ProteinMPNN（序列设计）、TrASPr（剪接结果预测）
- **模块4：验证与筛选**——FEP/自由能计算、MD-衍生的RMSF（肽-MHC动态稳定性）、实验验证
- **输出**：隐蔽变构口袋图谱、突变特异性结合剂、剪接新抗原候选、合成致死靶点

**反馈回路**：MD模拟结果反馈给AI模型进行微调（如用自由能数据训练更好的打分函数）；实验验证结果反馈给计算流程进行迭代优化。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 增强采样MD（MSMD） | 发现隐蔽变构口袋 | 静态结构无法显示瞬时空腔，MSMD用小分子探针映射可成药热点 | 输入：蛋白结构/系综；输出：探针富集位点、候选口袋 | "Mixed-solvent molecular dynamics (MSMD) simulations... identify and map these cryptic binding sites"（Cryptic pockets 节）；Koseki et al. (2025) 结合拓扑数据分析提升预测精度 | 预期影响：丧失发现隐蔽口袋的能力，回到静态结构盲区（预期效应，未消融验证） |
| 生成式结构预测（AF3/Boltz-2） | 预测突变体复合物结构 | 剪接因子突变体的实验结构难以获得，需快速生成结构假设 | 输入：序列、突变信息、配体/核酸；输出：3D复合物结构 | "AlphaFold3... unified diffusion-based architecture capable of modeling protein-protein, protein-ligand, and protein-nucleic acid complexes"（Foundation models 节）；Boltz-2 在混合模态复合物预测中达到与AF3相当或更优精度 | 预期影响：失去快速生成结构假设的能力，MD模拟缺乏起点（预期效应） |
| 生成式结合物设计（RFDpoly/ProteinMPNN） | 设计靶向RNA-蛋白界面的结合物 | 传统小分子难以靶向剪接体平坦界面，需要设计大分子结合物 | 输入：目标结构/口袋；输出：候选蛋白/肽/核酸序列 | "RFDpoly... enables the simultaneous hallucination of nucleic acid backbones and protein binders"（Inverse design 节）；ProteinMPNN 为固定骨架设计高亲和序列 | 预期影响：丧失设计新型结合物的能力，只能依赖现有小分子库（预期效应） |
| 自由能计算（FEP） | 量化结合亲和力和突变效应 | 预测结合强度，筛选候选分子 | 输入：结合复合物结构；输出：相对结合自由能 | "alchemical methods such as Free Energy Perturbation (FEP)... calculate relative binding free energies with high accuracy"（Cryptic pockets 节） | 预期影响：无法区分候选分子的结合强弱，筛选效率大幅下降（预期效应） |
| 剪接新抗原预测流程 | 从RNA-seq识别异常剪接来源的新抗原 | 剪接因子突变产生共享新抗原，可作为免疫治疗靶点 | 输入：RNA-seq、突变信息、HLA分型；输出：新抗原候选列表 | "splicing-derived neoantigens demonstrate substantially higher immunogenicity than SNV-derived peptides"（Neoantigens 节）；SNAF 整合剪接位点检测与深度学习免疫原性预测 | 预期影响：丧失系统性发现新抗原的能力，回到单基因手工分析（预期效应） |
| 结构免疫信息学（pMHC建模） | 评估新抗原-MHC复合物的动态稳定性 | 静态结合亲和力不足以预测免疫原性，需要动态稳定性指标 | 输入：肽序列、HLA类型；输出：RMSF、复合物稳定性评分 | "peptide–MHC complex stability can often be a better predictor of T-cell responses"（Structural immunoinformatics 节）；MD模拟的RMSF与TCR识别相关 | 预期影响：丧失区分高/低免疫原性新抗原的能力（预期效应） |

## 09 关键公式符号

本文为综述，未给出具体公式。文中提及但未展开的方法学概念包括：

- **自由能微扰（FEP）**：ΔΔG = ΔG_mutant − ΔG_wildtype，用于量化突变对结合亲和力的影响（文中提及"alchemical methods"但未给出公式）
- **RMSF（Root Mean Square Fluctuation）**：RMSF = √(⟨(r_i − ⟨r_i⟩)²⟩)，用于量化肽段残基在MD模拟中的位置波动，文中用于评估肽-MHC复合物动态稳定性（Structural immunoinformatics 节）
- **加权系综（WE）**：通过复制和合并轨迹来加速稀有事件采样，文中提及但未给出数学形式

**结论**：不适用（综述无原始公式）。

## 10 实验设计与证据链

本文为综述，无原始实验。文中引用的关键证据来源如下：

| 实验/研究 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|-----------|------------|-----------|------|-----------|------------------|------|
| SF3B1 K700E 结构-功能研究 | K700E突变改变分支点识别 | 突变型 vs 野生型 | 突变导致分支点选择偏移，产生异常剪接 | 剪接因子突变是"改变功能"而非"丧失功能" | 未提供具体结构数据 | "SF3B1: the gatekeeper of branch point fidelity" 节；Cretu et al. (2016) |
| U2AF1 S34F/Y 突变分析 | S34突变改变3'剪接位点AG二核苷酸识别 | S34F/S34Y vs 野生型 | 突变体对-3位嘧啶（C vs U）产生严格偏好 | 突变通过空间位阻重塑RNA结合口袋 | 未提供MD模拟数据 | "U2AF1: altering zinc finger specificity" 节；Yoshida et al. (2020) |
| MSMD + 拓扑数据分析 | 拓扑方法提升隐蔽口袋预测精度 | MSMD+拓扑 vs 传统MSMD | 隐蔽口袋预测精度显著提升 | 拓扑数据分析可增强MSMD的口袋发现能力 | 未在剪接体上验证 | "Cryptic pockets" 节；Koseki et al. (2025) |
| 剪接新抗原免疫原性分析 | 剪接来源新抗原比SNV新抗原免疫原性更强 | 剪接新抗原 vs SNV新抗原 | 剪接新抗原诱导更强T细胞反应 | 剪接新抗原是免疫治疗的富矿 | 样本量有限 | "Neoantigens" 节；Li et al. (2024)；Kwok et al. (2025) |
| SF3B1 K700E 新抗原验证 | K700E突变本身产生可靶向新抗原 | K700E肽 vs 野生型肽 | 验证为CD8+ T细胞靶点，纳摩尔级亲和力 | 突变本身可作为免疫治疗靶点 | 仅限特定HLA类型 | "Neoantigens" 节；Biernacki et al. (2025) |
| 分子胶降解剂（如RBM39） | 分子胶可靶向剪接相关蛋白 | 分子胶处理 vs 对照 | 诱导RBM39降解，抑制剪接 | 分子胶策略可扩展剪接体靶向范围 | 耐药性机制未明 | "Direct modulation" 节；Han et al. (2017) |

## 11 结论正确解读

- **任务范围**：本文是**综述**，不提出新方法或新数据。其"结论"是**观点性主张**，基于对现有文献的整合与推断，而非实验验证。
- **oracle/真值输入**：不适用（无计算实验）。
- **端到端状态**：文中提出的"AI+MD"集成流程是**概念框架**，尚未在剪接体上实现端到端验证。各模块（AF3预测、MSMD口袋发现、FEP计算）分别在各自领域有验证，但**整合流程**未经过完整实验检验。
- **算力成本**：文中承认全原子MD对剪接体这样的大系统"极其昂贵"，但未给出具体数字。
- **历史数据依赖**：新抗原预测依赖RNA-seq数据和HLA分型数据库，文中未讨论数据偏差问题。
- **模型依赖**：文中明确指出AI模型可能"幻觉"不可靠结构，需要物理模拟和实验验证作为"安全网"。
- **最难情形**：IDR的构象采样、RNA-蛋白界面的力场精度、突变诱导的远程别构效应。
- **群体/领域边界**：结论主要针对血液恶性肿瘤（MDS、CLL）和部分实体瘤（葡萄膜黑色素瘤、乳腺癌），不适用于所有癌症类型。
- **不确定性**：文中多处使用"potential"、"may"、"could"等限定词，表明这些策略尚处于概念阶段。

**有边界的复述**：本文主张，通过将增强采样MD与生成式AI结合，有可能在剪接因子突变体中发现静态结构不可见的隐蔽可成药位点（包括IDR区域），并据此设计选择性更高的治疗策略（变构调节剂、分子胶、新抗原疫苗），但这一流程的端到端可行性尚未在剪接体系统中得到实验验证。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 计算成本高 | 全原子MD对剪接体大系统"极其昂贵"，难以常规应用 | 发展更高效的增强采样方法和粗粒化模型 | "The most fundamental constraint is the disparity between accessible simulation times and biological timescales"（Sampling gap 节） |
| AI模型幻觉风险 | 生成式模型可能产生物理上不可能的构象或高置信度假阳性 | 用物理模拟和实验验证作为"安全网"；发展更好的打分函数 | "They can 'hallucinate' plausible-looking interactions for physically impossible contacts"（Validation 节） |
| 预测-实验差距 | 计算预测的新抗原和结合剂需要实验验证，但验证通量低 | 发展高通量验证平台；整合免疫肽组学数据 | "computational predictions remain imperfect: mass spectrometry validation studies demonstrate that only a subset of predicted neoantigens are actually presented"（Neoantigens 节） |
| IDR建模困难 | 剪接因子的IDR区域构象异质性大，传统方法难以处理 | 发展IDR专用采样方法和AI模型 | "their conformational heterogeneity poses significant challenges for high-resolution modeling"（Dynamics 节） |
| 耐药性未明 | 分子胶等策略的耐药机制不清楚 | 需要更多机制研究和联合用药策略 | "the lack of thermodynamic selectivity resulted in a narrow therapeutic index"（Direct modulation 节） |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 综述高度依赖"AI+MD融合"的乐观叙事 | 文中未讨论AI预测结构（如AF3）在剪接体这类大型动态复合物上的实际精度；AF3对IDR的预测已被广泛认为不可靠 | 如果AI结构假设本身有偏，后续MD和药物设计将建立在错误基础上 | 在已知剪接体复合物上系统比较AF3/Boltz-2预测与实验结构的差异，特别关注IDR区域 | "They can 'hallucinate' plausible-looking interactions"（Validation 节）——作者承认但未量化 |
| "隐蔽口袋"策略缺乏实验验证案例 | 文中引用的MSMD发现隐蔽口袋的案例多来自可溶性蛋白，剪接体上尚无成功案例 | 剪接体的动态性和复合物界面可能使隐蔽口袋策略失效 | 在SF3B1或U2AF1上开展MSMD+实验验证的案例研究 | "MSMD simulations... identify and map these cryptic binding sites"（Cryptic pockets 节）——均为方法学引用，无剪接体实例 |
| 新抗原"公共性"可能被高估 | 文中引用"90%黑色素瘤患者共享新抗原"的数据，但未讨论HLA限制性和肿瘤异质性 | 如果新抗原共享率在真实患者群体中较低，"现成"免疫治疗策略将受限 | 在更大患者队列中验证共享新抗原的频率和HLA覆盖度 | "shared splicing neoantigens in up to 90% of melanoma patients"（Neoantigens 节）——单一研究引用 |
| 合成致死逻辑的因果链不完整 | 文中提出剪接因子突变导致"剪接压力"从而产生合成致死脆弱性，但未讨论正常细胞如何耐受 | 如果正常细胞也依赖剪接因子功能，治疗窗口可能很窄 | 在正常组织与肿瘤组织中比较剪接因子抑制的差异敏感性 | "functional selectivity"概念（Direct modulation 节）——作者承认治疗窗口窄 |
| 未讨论IDR相分离在剪接调控中的具体机制 | 文中提及LLPS和核斑点，但未深入讨论剪接因子IDR如何通过相分离调控剪接位点选择 | 相分离可能是剪接因子突变致病的核心机制，也是潜在治疗靶点 | 在剪接因子突变细胞中检测凝聚体形成和组成的变化 | "fluid segments drive liquid-liquid phase separation (LLPS) and the formation of nuclear speckles"（Dynamics 节）——仅提及未展开 |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **"动态系综药理学"范式**：对于IDP/IDR介导的互作，靶向静态结构可能无效。应构建蛋白的构象系综（通过增强采样MD或生成式AI），在系综中寻找瞬时可成药的"隐秘口袋"。**可迁移到**：IDP介导的相分离体系——凝聚体中的互作位点可能仅在特定构象或聚集状态下暴露。

2. **MSMD作为IDR可成药性筛查工具**：混合溶剂MD（MSMD）用小分子探针（苯、异丙醇）系统扫描蛋白表面，识别热力学上有利的结合热点。**可迁移到**：对IDR或相分离驱动蛋白进行MSMD，预测哪些区域可能被小分子或肽段结合，即使这些区域在静态结构中看似"无口袋"。

3. **"功能选择性"优于"结合选择性"**：剪接体抑制剂的经验表明，即使药物同时结合野生型和突变型，突变细胞因对额外剪接压力更敏感而表现出选择性杀伤。**可迁移到**：靶向相分离的药物可能不需要严格区分突变/野生型IDR，而是利用突变细胞对凝聚体稳态扰动更脆弱的特点。

4. **AI预测+MD验证的闭环流程**：用AF3/Boltz-2快速生成突变体结构假设，用增强采样MD验证其动态可行性，用FEP量化结合自由能。**可迁移到**：IDP互作研究——AF3对IDP预测不可靠，但可以生成"候选折叠态"作为MD采样的起点，而非最终答案。

5. **剪接来源新抗原的"公共性"**：剪接因子突变以可预测方式产生共享异常剪接事件，这些事件编码公共新抗原。**可迁移到**：IDR突变（如癌症中的频繁IDR突变）可能同样产生共享异常剪接或翻译后修饰改变，可作为新抗原来源。

6. **RMSF作为免疫原性预测指标**：肽-MHC复合物的动态稳定性（RMSF）比静态结合亲和力更能预测T细胞反应。**可迁移到**：评估IDR来源的肽段-MHC复合物动态行为，筛选更可能引发免疫反应的候选新抗原。

7. **多模态验证的必要性**：计算预测（无论AI还是MD）必须经过正交实验验证（免疫肽组学、T细胞功能实验等）。**可迁移到**：IDP/相分离研究中的计算预测应配套体外凝聚体实验、交联质谱或NMR验证。

## 15 与已有知识连接

1. **AlphaFold2/3 对IDP的已知局限**：AF2对IDR预测为低置信度或无规卷曲，本文承认AI模型可能"幻觉"结构。这与已知文献一致（如 Ruff & Pappu, 2021; Chakravarty et al., 2023 关于AF2在IDP上的表现）。本文的应对策略——用MD补充AI预测——与领域共识一致。

2. **相分离与剪接的关联**：本文提及SR蛋白的RS结构域通过LLPS形成核斑点，这与已知文献一致（如 Gueroussov et al., 2015; Greig et al., 2020 关于SR蛋白相分离调控剪接）。本文未深入展开，但为课题提供了连接点：剪接因子IDR的相分离行为可能是突变致病的核心机制。

3. **分子胶与"不可成药"靶点**：本文讨论的RBM39/DCAF15分子胶机制与已知文献一致（Han et al., 2017; Bussiere et al., 2020）。这为IDP/IDR靶向提供了范例——通过诱导蛋白-蛋白互作而非阻断活性位点。

4. **增强采样方法在RNA-蛋白体系的应用**：本文引用的MSMD、WE等方法在RNA-蛋白互作研究中的应用与领域前沿一致（如 Borišek et al., 2020 对U2AF2的MD研究）。可进一步连接：粗粒化模型（Martini）在剪接体大尺度构象变化中的应用。

5. **新抗原预测的计算流程**：本文提出的"剪接新抗原发现流程"与现有工具（如SNAF、NeoSplice）一致，但增加了结构动态验证层。这与课题方向相关：IDR突变产生的异常剪接事件可能编码新抗原，而结构动态分析可以预测其MHC呈递和TCR识别。

6. **候选连接方向**：本文未讨论但可探索的——剪接因子突变是否影响其IDR的相分离行为？这种改变是否产生"相分离新抗原"或改变凝聚体中的蛋白互作网络？这为课题提供了新的研究假设。

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**：剪接因子IDR的相分离驱动隐蔽口袋的MSMD筛查
   - **来源局限/观察**：本文提出MSMD可发现剪接因子的隐蔽口袋，但未具体到IDR/相分离区域。IDR在凝聚体中的构象系综可能暴露独特的可成药位点。
   - **核心假设**：SF3B1 K700E或SRSF2 P95突变通过改变IDR的构象系综，暴露野生型中不存在的隐蔽口袋，这些口袋可被小分子选择性靶向。
   - **初步方法**：对野生型和突变型剪接因子IDR进行增强采样MD（REMD或WE），结合MSMD探针映射，比较隐蔽口袋的差异；用AF3/ Boltz-2生成初始结构假设作为MD起点。
   - **验证方式**：在凝聚体条件下（高浓度、多价互作）验证候选口袋的可及性；用NMR或交联质谱验证小分子结合。
   - **可能的失败模式**：IDR的构象系综过于宽泛，隐蔽口袋在生理条件下不稳定；MSMD探针在IDR上的结合位点可能缺乏特异性。
   - **创新状态**：unverified

2. **候选名称**：基于结构动态的剪接新抗原免疫原性预测框架
   - **来源局限/观察**：本文提出用MD评估肽-MHC复合物动态稳定性（RMSF）来预测免疫原性，但未将其整合到剪接新抗原发现流程中。
   - **核心假设**：剪接因子突变产生的异常剪接肽段，其与MHC的复合物动态稳定性（而非静态亲和力）能更好预测T细胞反应。
   - **初步方法**：从RNA-seq数据中识别剪接因子突变样本的异常剪接事件，生成候选新抗原肽段；用AF3/AlphaFold-Multimer预测肽-MHC复合物结构；用MD模拟计算RMSF和复合物稳定性；整合序列特征（疏水性、芳香族残基含量）与动态特征训练免疫原性预测模型。
   - **验证方式**：在已发表的免疫肽组学数据集上验证预测精度；用T细胞功能实验验证高评分候选。
   - **可能的失败模式**：计算成本高（每个肽-MHC复合物需独立MD）；动态稳定性与免疫原性的相关性可能受HLA型别影响。
   - **创新状态**：unverified

3. **候选名称**：剪接因子IDR突变对相分离行为的影响及其作为治疗靶点的评估
   - **来源局限/观察**：本文提及SR蛋白IDR驱动LLPS，但未讨论剪接因子突变如何影响相分离行为，也未将相分离作为治疗靶点。
   - **核心假设**：SF3B1、U2AF1、SRSF2的癌症相关突变通过改变IDR的电荷分布或疏水性，改变其相分离行为（如凝聚体形成温度、粘度、组成），从而影响剪接位点选择。
   - **初步方法**：对野生型和突变型IDR进行粗粒化MD（Martini）或晶格模型模拟，预测相分离行为差异；用实验（体外凝聚体实验、荧光恢复FRAP）验证；筛选调节相分离的小分子或肽段。
   - **验证方式**：比较野生型和突变型IDR的相图（温度-浓度相图）；检测突变细胞中核斑点的形态和动力学变化。
   - **可能的失败模式**：IDR相分离行为在体外与体内的相关性有限；突变对相分离的影响可能被其他因素（如RNA结合）掩盖。
   - **创新状态**：unverified

4. **候选名称**：AI生成IDR构象系综与MD验证的集成工作流
   - **来源局限/观察**：本文提出AI与MD互补，但未给出具体集成方案。IDR的构象系综生成是当前计算挑战。
   - **核心假设**：用生成式AI（如扩散模型）快速生成IDR构象系综，再用增强采样MD进行物理筛选和权重校正，可以比纯MD或纯AI更高效地获得热力学可靠的IDR构象系综。
   - **初步方法**：用AF3/扩散模型生成IDR候选构象；用REMD或WE-MD对候选构象进行重加权和验证；比较AI生成系综与MD采样系综的差异；用实验数据（SAXS、FRET）验证。
   - **验证方式**：在已知IDR体系（如SRSF2 RS结构域）上验证系综的准确性；比较计算效率与纯MD。
   - **可能的失败模式**：AI生成构象可能偏向训练数据中的折叠蛋白，对IDR的"无序性"建模不足；MD重加权可能无法完全校正AI偏差。
   - **创新状态**：unverified

5. **候选名称**：剪接因子突变-相分离-新抗原三联体的系统图谱
   - **来源局限/观察**：本文分别讨论了剪接因子突变的结构后果、IDR的相分离行为、以及剪接新抗原的免疫治疗潜力，但未将三者系统整合。
   - **核心假设**：剪接因子突变通过改变IDR相分离行为，系统性改变剪接位点选择，产生可预测的异常剪接事件库，其中一部分编码共享新抗原，可作为免疫治疗靶点。
   - **初步方法**：整合TCGA等癌症基因组数据（剪接因子突变）、RNA-seq剪接数据、蛋白质结构/IDR预测，构建"突变→相分离改变→剪接异常→新抗原"的因果链模型；用MD/AI验证关键节点的结构基础。
   - **验证方式**：在独立数据集中验证突变-剪接异常关联的预测精度；用免疫肽组学数据验证新抗原预测。
   - **可能的失败模式**：因果链过长，每个环节都有不确定性；相分离行为难以在临床样本中直接测量。
   - **创新状态**：unverified