## 01 基本信息
- **标题**: Transient tertiary structure in intrinsically disordered proteins revealed by multithermal enhanced sampling
- **作者与单位**: Streit, Julian O; Invernizzi, Michele; Bottaro, Sandro; Tamiola, Kamil; Lindorff-Larsen, Kresten（单位未在摘要中提供）
- **期刊/预印本平台**: Nature Communications
- **年份**: 2026
- **论文类型**: 研究论文（方法学 + 应用）
- **领域**: 计算生物物理 / 无序蛋白构象采样
- **关键词**: IDP, enhanced sampling, OPES, multithermal, transient tertiary structure, ACTR, molecular dynamics
- **DOI/arXiv 号**: 10.1038/s41467-026-73067-3
- **代码**: 未提供（但声明"All data and analysis code are freely available"）
- **数据**: 未提供（但声明数据公开）
- **阅读日期**: 2026-05-14
- **在课题方向中的位置**: 本文属于「无序蛋白(IDP/IDR) × 物理模拟(MD)」方向，聚焦于通过增强采样方法（OPES multithermal）提高IDP构象采样的效率和收敛性，并揭示了IDP中瞬态三级结构的形成。与AI方法无直接关联，但为AI训练数据生成提供了高质量构象系综的获取途径。

## 02 一句话总结
本文通过将On-the-fly Probability Enhanced Sampling (OPES) 的multithermal变体应用于4个不同大小的无序肽段/蛋白（15-71残基），在单副本模拟中实现了比REST2和常规MD更高效的构象采样，并揭示了ACTR在无结合伴侣时能瞬态形成类似结合态的多螺旋束状三级结构。

## 03 研究问题
- **具体问题**: 如何高效生成收敛的无序蛋白（IDP）全原子构象系综，并检测IDP中是否存在瞬态三级结构？
- **为什么重要**: IDP构象系综的充分采样是理解其功能机制（如folding-upon-binding、相分离）的前提；瞬态三级结构可能代表药物靶点或功能相关构象。
- **现有方法不足**: 常规MD采样效率低；REST2等副本交换方法需要大量副本、计算成本高，且在大IDP中副本混合差；AI生成方法缺乏物理真实性。
- **精确研究问题**: Can a single-replica multithermal enhanced sampling method (OPES) efficiently generate converged atomistic ensembles for IDPs of varying sizes, and can such ensembles reveal transient tertiary structures that are functionally relevant?

## 04 背景与发展脉络
（标注：以下脉络为「经外部核验」+「仅本文框架」混合，具体标注于各阶段）

1. **常规MD模拟IDP**（早期）：直接模拟，但采样不足，构象系综不收敛。
2. **副本交换方法（REMD/REST2）**：通过多副本温度交换加速采样，但需要大量副本、计算成本高，大体系副本混合差，且高温下IDP易人工塌缩。
3. **增强采样方法（metadynamics等）**：需要选择集体变量（CV），对IDP这种高维无序体系难以预先确定有效CV。
4. **OPES方法**（本文主张的位置）：以势能为CV，无需预选反应坐标，单副本即可实现multithermal采样，避免了副本交换的通信开销和混合问题。
5. **AI构象生成方法**（外部背景）：AlphaFold等深度学习方法开始生成构象系综，但训练数据依赖高质量MD系综，本文方法可为此提供数据。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| IDP采样收敛慢 | 常规MD难以在可行时间内充分采样IDP构象空间 | IDP构象空间广阔且势能面平坦，缺乏深势阱引导 | Introduction 第2-3段 |
| REST2副本混合差 | 大IDP中高温副本易塌缩，副本交换效率低 | 高温下IDP人工塌缩，导致副本间能量重叠差 | Introduction 第3段；Results 图3g |
| 瞬态结构难以捕捉 | 低群体构象（如部分折叠态）在有限采样中被遗漏 | 常规采样偏向高概率构象，低概率但功能相关的构象难以访问 | Results 图4f-g |
| 增强采样方法参数敏感 | metadynamics等需要预选CV，对IDP不适用 | IDP缺乏明确的反应坐标，CV选择困难 | Introduction 第3段 |
| 实验数据与模拟系综整合困难 | 单一实验技术只能提供系综平均信息 | 需要计算系综与多种实验数据（NMR、SAXS）进行整合验证 | Results 图5b-c |

## 06 核心思想
1. **表面方法**: 使用OPES multithermal增强采样，以势能为CV，在单副本中实现多温度系综采样，通过reweighting获得目标温度下的构象系综。
2. **核心洞察**: IDP虽然整体无序，但其构象空间并非完全均匀——存在低群体的、部分折叠的、具有三级结构的亚态，这些亚态可能代表folding-upon-binding的中间态或功能相关构象。OPES通过增强势能涨落，能有效访问这些低概率但功能重要的构象。
3. **[Analysis] 普适教训**: 对于IDP/IDR研究，采样方法的选择比力场精度更可能成为瓶颈；单副本增强采样方法（如OPES）避免了副本交换的扩展性问题，为更大IDP体系（乃至多分子相分离体系）提供了可扩展的采样框架。此外，将模拟系综与多种实验数据（NMR、SAXS）整合验证是建立可信IDP构象系综的必要步骤。

## 07 方法总览
- **输入**: 4个无序肽段/蛋白的初始结构（(AAQAA)3、ACTR20−60、ACTR全长、HTTex1 16Q），力场参数（a03ws/TIP4P/2005或a99SB-disp），溶剂环境（含盐浓度）
- **输出**: 各体系在目标温度（300K或310K）下的reweighted构象系综，包括Rg分布、螺旋度分布、自由能景观、瞬态三级结构
- **模块**:
  1. OPES bias构建（势能为CV，multithermal目标分布）
  2. 偏置模拟（单副本，温度范围290-450K）
  3. Reweighting（权重计算，目标温度系综重建）
  4. 构象分析（Rg、螺旋度、Q值、自由能景观）
  5. 实验数据整合（NMR CS、PRE、RDC、SAXS的Bayesian/maximum entropy reweighting）
- **训练**: 无监督（无训练过程，为物理模拟）
- **反馈回路**: 模拟系综 → 计算实验可观测量 → 与实验数据比较 → 通过BME reweighting调整系综权重
- **文字流程**: 初始结构 → 10次短试运行估计温度步数 → 构建OPES bias → 单副本multithermal生产模拟 → 监测bias收敛（c(t)）和采样分数 → 多副本合并 → Reweighting获得目标温度系综 → 构象分析 + 实验数据整合验证

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| OPES bias构建 | 以势能为CV构建自适应偏置势 | 无需预选反应坐标，适用于IDP | 输入：势能轨迹；输出：偏置势 | Methods "OPES multithermal simulations" | 预期影响：无法实现multithermal采样，退化为常规MD |
| 温度步数估计 | 确定multithermal目标分布的温度范围 | 确保温度空间覆盖充分 | 输入：短试运行；输出：温度步数 | Methods 步骤1；Supplementary Table 2 | 预期影响：温度范围过窄则采样不足，过宽则效率降低 |
| Bias收敛监测 | 通过c(t)和采样分数判断bias是否收敛 | 确保偏置势达到准静态极限 | 输入：bias轨迹；输出：收敛判断 | Methods 步骤2；Supplementary Fig. 1 | 预期影响：bias未收敛时reweighting结果不可靠 |
| Reweighting | 将multithermal系综权重转换到目标温度 | 获得目标温度下的构象系综 | 输入：偏置模拟轨迹；输出：目标温度权重 | Methods 公式(3) | 预期影响：无法获得目标温度系综 |
| BME实验数据整合 | 使用NMR/SAXS数据对系综进行reweighting | 验证并修正模拟系综 | 输入：模拟系综+实验数据；输出：修正后系综 | Results 图5b-c；Methods "Bayesian/maximum entropy reweighting" | 预期影响：系综与实验数据一致性降低 |
| ELViM降维分析 | 将高维构象投影到2D空间 | 可视化构象空间覆盖和亚态分布 | 输入：构象系综；输出：2D投影 | Results 图3g | 预期影响：难以直观比较不同方法的构象空间覆盖 |

## 09 关键公式符号
1. **OPES multithermal目标分布**（Methods 公式1）:
   $$p^{tg}(x) = \frac{1}{N_\beta} \sum_k \exp[-\beta_k U(x)]/Z_k$$
   其中 $\beta = (k_B T)^{-1}$，$U(x)$为势能，$Z_k$为配分函数，$N_\beta$为温度步数。

2. **OPES偏置势**（Methods 公式2）:
   $$V_n(x) = -\frac{1}{\beta_0} \ln\left[\frac{1}{N_\beta} \sum_k \exp(-(\beta_k - \beta_0)U(x) + \beta_0 \Delta F_n(\beta_k))\right]$$
   其中 $\Delta F_n(\beta_k)$为第n次迭代时各温度态的相对自由能估计。

3. **Reweighting权重**（Methods 公式3）:
   $$w_i(\beta^*) = \exp[-(\beta^* - \beta_0)U_i + \beta_0 V(x_i)]$$
   用于将偏置模拟的帧权重转换到目标温度 $\beta^*$。

4. **有效样本量**（Methods 公式4）:
   $$N_{eff}(\beta^*) = \frac{(\sum_i w_i(\beta^*))^2}{\sum_i w_i(\beta^*)^2}$$
   衡量reweighting后系综的统计可靠性。

5. **Q值（native contacts分数）**（Methods 公式8）:
   $$q(r_{ij}) = \frac{1}{1 + \exp[\beta(r_{ij} - \lambda r_0)]}$$
   其中 $r_0$为参考结构中的接触距离，$\lambda = 1.8$，$\beta = 50$ nm⁻¹。

6. **SAXS reduced χ²**（Methods 公式15）:
   $$\chi^2_{red} = \frac{1}{N} \sum_{i=1}^N \frac{[I_i^{exp} - (\alpha \langle I_i^{gen} \rangle + \beta)]^2}{\sigma_i^2}$$
   用于量化模拟系综与SAXS实验数据的拟合质量。

## 10 实验设计与证据链
- **数据集/群体**: 4个无序体系：(AAQAA)3（15残基，a03ws/TIP4P/2005力场）、ACTR20−60（40残基，a99SB-disp）、ACTR全长（71残基，a99SB-disp）、HTTex1 16Q（66残基，a03ws）
- **规模**: 模拟体系原子数29,730-174,602；OPES模拟总时长未明确给出，但bias收敛时间100-600 ns
- **指标**: Rg分布、螺旋度、Q值、自由能景观、有效样本量（Neff）、相关时间（τint）、加速因子
- **基线**: REST2模拟（相同力场和体系）、15 μs无偏MD（(AAQAA)3）、30 μs无偏MD（ACTR，来自DE Shaw Research）
- **预算**: 未提供具体计算资源
- **评测协议**: 多指标交叉验证（Rg、螺旋度、Q值）+ 实验数据整合验证（NMR CS、PRE、RDC、SAXS）

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|------------|------|------------|----------------|------|
| (AAQAA)3 OPES vs REST2 vs 无偏MD | OPES与REST2产生一致系综且加速收敛 | 相同力场，300K | Rg和螺旋度分布一致；OPES加速2-3×（误差条）和13-16×（相关时间） | OPES产生与REST2一致的系综，且采样效率更高 | 加速因子因指标而异，不能给出单一加速倍数 | Results 图2 |
| HTTex1 16Q OPES vs REST2 | 大IDP中OPES系综与REST2一致 | 相同力场，293K | Rg分布和螺旋度分布一致；OPES探索更广构象空间 | OPES适用于较大IDP | 未验证与实验数据的一致性 | Results 图3 |
| ACTR20−60 OPES vs REST2 | 片段中OPES采样更高效 | 相同力场，300K | OPES加速4.4-6.5×（相关时间）；OPES采样到高螺旋态 | OPES在片段中采样效率更高 | 加速因子基于相关时间，可能受初始条件影响 | Results 图4d-e |
| ACTR全长 OPES vs REST2 vs 无偏MD | OPES发现REST2和无偏MD未采到的瞬态三级结构 | 相同力场，300K/310K | OPES采样到Q~0.6-0.7的高螺旋、紧凑态；REST2和无偏MD未采到 | OPES能发现低群体但功能相关的瞬态结构 | 瞬态结构的生物学相关性需进一步验证 | Results 图4f-g |
| ACTR系综与NMR/SAXS数据整合 | OPES系综与实验数据一致 | BME reweighting，CS+PRE或CS+SAXS | Reweighting后系综与实验数据一致；OPES系综比REST2系综与实验数据一致性更好 | OPES系综包含实验支持的构象 | 实验数据不能唯一确定系综 | Results 图5b-c |
| 从结合态出发的无偏MD | 结合态在无伴侣时是否稳定 | 10×5 μs无偏MD，300K | 螺旋结构保持但三级结构丢失；形成类似OPES采到的瞬态结构 | 瞬态三级结构是真实的亚稳态 | 模拟时间仍可能不足以完全松弛 | Results 图5h-i |

## 11 结论正确解读
- **任务范围**: 本文仅针对4个特定无序体系（15-71残基），使用特定力场（a03ws、a99SB-disp）和特定增强采样方法（OPES multithermal）。结论不能直接推广到所有IDP/IDR。
- **Oracle/真值输入**: 无外部oracle；真值来自实验数据（NMR CS、PRE、RDC、SAXS）的间接验证。
- **端到端状态**: 方法端到端可用（从初始结构到实验整合系综），但bias收敛需要人工监控，且成功率随体系增大而降低（10-50%）。
- **算力成本**: OPES比REST2计算成本低（单副本 vs 多副本），但比无偏MD高30-40%；bias收敛需100-600 ns。
- **历史数据依赖**: 无历史数据依赖（纯物理模拟）。
- **模型依赖**: 结果依赖力场选择（a03ws vs a99SB-disp）；不同力场可能产生不同系综。
- **最难情形**: 大IDP（如ACTR全长）中bias收敛成功率低（10%），且瞬态结构群体极低（~2.6%），需要长模拟和多次重复才能可靠检测。
- **群体/领域边界**: 结论仅适用于单链IDP在稀溶液中的构象系综；不涉及相分离/凝聚体、多分子体系、翻译后修饰等复杂条件。
- **不确定性**: 瞬态三级结构的群体估计（~2.6%）依赖于reweighting和实验数据整合，存在模型不确定性；不同实验数据组合可能给出不同结果。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 系统大小限制 | 最大体系仅71残基（ACTR），更大IDP或多分子体系需要更多计算资源 | 扩展到更大IDP或多蛋白组装体 | Discussion 第3段 |
| Bias收敛成功率低 | ACTR全长仅10%的试运行达到收敛标准 | 可能需要更高效的bias构建策略或多walker方案 | Methods "OPES multithermal simulations"；Supplementary Table 2 |
| 采样仍可能不充分 | 承认"unlikely to have exhaustively sampled all relevant low-population states" | 更长模拟、更宽温度范围或结合其他增强采样方法 | Discussion 第3段 |
| 实验数据不能唯一确定系综 | 不同实验数据组合可能支持不同系综 | 整合更多正交实验数据 | Results 图5 |
| 力场依赖性 | 结果依赖力场选择 | 使用多个力场交叉验证 | Methods 表1 |
| 瞬态结构的功能相关性未验证 | 检测到的瞬态三级结构是否具有生物学功能尚不清楚 | 需要功能实验验证 | Discussion 第2段 |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| 瞬态三级结构的检测依赖于Q值定义和参考结构选择 | 使用结合态结构作为参考可能偏向检测结合态类似构象；不同参考结构可能给出不同结果 | 核心结论（瞬态三级结构）可能受分析选择影响 | 使用多种参考结构（如无偏MD聚类中心）重复分析 | Results 图5e-h |
| OPES与REST2的系综一致性仅在(AAQAA)3中严格验证 | 更大体系中两者系综差异可能更大 | 方法有效性随体系增大可能降低 | 在HTTex1和ACTR中更严格比较系综分布 | Results 图3-4 |
| 加速因子估计方法不一致 | 不同指标（误差条、相关时间）给出不同加速因子（2-3× vs 13-16×） | 加速因子的实际意义不明确 | 使用统一指标（如有效样本量/计算时间）重新评估 | Results 图2d |
| BME reweighting可能过度拟合实验数据 | 大量权重调整可能掩盖模拟系综的不足 | 实验整合可能高估系综质量 | 使用交叉验证（训练/测试集分离）评估reweighting | Methods "Bayesian/maximum entropy reweighting" |
| 未与AI方法（如AlphaFold、生成模型）比较 | 当前AI方法也能生成IDP构象系综 | 方法定位不清晰 | 与AI生成系综进行基准比较 | Introduction 第1段 |
| 瞬态结构的生物学意义缺乏实验验证 | 检测到的结构可能只是模拟伪影或与功能无关 | 核心生物学结论需要实验支持 | 设计突变实验或小分子结合实验验证 | Discussion 第2段 |

## 13 学到什么
**Agent 提炼的知识候选**：
1. **单副本增强采样框架**: OPES multithermal避免了副本交换的扩展性问题，为更大IDP体系（乃至相分离体系）提供了可扩展的采样方案。可迁移到IDP/IDR相分离模拟中，用于高效采样多分子凝聚体构象。
2. **势能作为CV的普适性**: 对于缺乏明确反应坐标的IDP体系，以势能为CV的增强采样方法具有普适性，无需预先知道功能相关构象。可迁移到IDP-配体结合、IDP-伴侣互作模拟中。
3. **瞬态三级结构检测策略**: 通过Q值（native contacts）和自由能景观分析，可以系统检测IDP中的低群体部分折叠态。可迁移到IDP/IDR互作研究中，用于识别folding-upon-binding的预折叠态。
4. **多实验数据整合验证**: BME reweighting框架可整合NMR、SAXS等多种实验数据，为IDP构象系综提供交叉验证。可迁移到IDP-蛋白互作复合物的构象系综验证中。
5. **收敛性评估方法**: 使用累积平均、相关时间、有效样本量等多指标评估采样收敛性，而非单一指标。可迁移到任何IDP模拟研究中。
6. **片段-全长策略**: 先模拟片段（ACTR20−60）再模拟全长，可系统探索IDP的区域性结构倾向。可迁移到IDR功能域分析中。

## 14 与已有知识连接
- **OPES方法**: 由Invernizzi等人开发（参考文献47,48），本文将其应用于IDP体系，扩展了其应用范围。
- **REST2方法**: Wang等人开发（参考文献19,37-40），本文将其作为基准比较方法。
- **IDP力场**: a03ws（参考文献13）和a99SB-disp（参考文献14）是当前IDP模拟的主流力场，本文验证了它们在增强采样下的表现。
- **ACTR-NCBD体系**: 已有大量实验和计算研究（参考文献56-58），本文提供了新的构象系综视角。
- **BME reweighting**: 由Bottaro等人开发（参考文献64），本文将其应用于IDP系综的实验数据整合。
- **folding-upon-binding**: 经典概念（参考文献68-70），本文提供了apo态预折叠的直接计算证据。
- **与AI方法的关系**: 本文方法可为AI构象生成模型提供高质量训练数据（Discussion 最后一段），与AlphaFold等深度学习方法互补。

## 15 研究想法
**Agent 生成的研究候选**：

1. **候选名称**: OPES-multiT驱动的IDP-配体结合构象系综生成
   - **来源局限/观察**: 本文仅模拟了apo态IDP，未涉及配体结合；但瞬态三级结构可能代表配体结合口袋
   - **核心假设**: OPES-multiT能高效采样IDP-配体结合过程中的构象变化，包括induced fit和conformational selection路径
   - **初步方法**: 对ACTR-小分子体系进行OPES-multiT模拟，结合BME reweighting整合NMR化学位移扰动数据
   - **验证方式**: 与已知结合亲和力实验数据比较，检测结合态构象群体
   - **创新状态**: unverified

2. **候选名称**: 基于OPES-multiT构象系综的IDP相分离驱动残基识别
   - **来源局限/观察**: 本文方法限于单链IDP，未涉及多分子相分离；但瞬态三级结构可能介导多价互作
   - **核心假设**: IDP中瞬态三级结构区域是相分离的关键驱动残基
   - **初步方法**: 对ACTR或其它相分离相关IDR进行OPES-multiT模拟，分析瞬态结构区域，与相分离突变实验数据比较
   - **验证方式**: 预测的驱动残基突变后相分离行为变化
   - **创新状态**: unverified

3. **候选名称**: OPES-multiT构象系综作为AI构象生成模型的训练数据
   - **来源局限/观察**: 本文方法计算成本仍较高，难以覆盖所有IDP序列；AI模型可快速生成构象
   - **核心假设**: 用OPES-multiT生成的高质量构象系综训练AI模型，可提高AI生成IDP构象的物理真实性
   - **初步方法**: 用本文4个体系的OPES-multiT系综训练生成模型（如扩散模型），评估生成构象的Rg、螺旋度分布与OPES系综的一致性
   - **验证方式**: 生成系综与实验数据（NMR、SAXS）的一致性
   - **创新状态**: unverified

4. **候选名称**: IDP瞬态三级结构的序列决定因素分析
   - **来源局限/观察**: 本文仅研究了4个体系，瞬态三级结构的序列基础尚不清楚
   - **核心假设**: 特定序列模式（如疏水残基分布、电荷模式）决定IDP瞬态三级结构的倾向
   - **初步方法**: 对多个IDP进行OPES-multiT模拟，建立瞬态结构倾向与序列特征的关联模型
   - **验证方式**: 预测的序列特征与实验检测的瞬态结构（如NMR PRE）比较
   - **创新状态**: unverified

5. **候选名称**: OPES-multiT与AI增强采样结合的双层采样框架
   - **来源局限/观察**: OPES-multiT的bias收敛在大体系中成功率低（10%）
   - **核心假设**: AI模型可预测OPES bias的初始猜测，加速收敛
   - **初步方法**: 用AI模型预测势能面特征，初始化OPES bias，再进行multithermal模拟
   - **验证方式**: 比较AI初始化与随机初始化的bias收敛时间和系综质量
   - **创新状态**: unverified

## 16 研究想法
（注：此节与15节重复，按指令要求保留，但内容与15节相同）

**Agent 生成的研究候选**：

1. **候选名称**: OPES-multiT驱动的IDP-配体结合构象系综生成
   - **来源局限/观察**: 本文仅模拟了apo态IDP，未涉及配体结合；但瞬态三级结构可能代表配体结合口袋
   - **核心假设**: OPES-multiT能高效采样IDP-配体结合过程中的构象变化，包括induced fit和conformational selection路径
   - **初步方法**: 对ACTR-小分子体系进行OPES-multiT模拟，结合BME reweighting整合NMR化学位移扰动数据
   - **验证方式**: 与已知结合亲和力实验数据比较，检测结合态构象群体
   - **创新状态**: unverified

2. **候选名称**: 基于OPES-multiT构象系综的IDP相分离驱动残基识别
   - **来源局限/观察**: 本文方法限于单链IDP，未涉及多分子相分离；但瞬态三级结构可能介导多价互作
   - **核心假设**: IDP中瞬态三级结构区域是相分离的关键驱动残基
   - **初步方法**: 对ACTR或其它相分离相关IDR进行OPES-multiT模拟，分析瞬态结构区域，与相分离突变实验数据比较
   - **验证方式**: 预测的驱动残基突变后相分离行为变化
   - **创新状态**: unverified

3. **候选名称**: OPES-multiT构象系综作为AI构象生成模型的训练数据
   - **来源局限/观察**: 本文方法计算成本仍较高，难以覆盖所有IDP序列；AI模型可快速生成构象
   - **核心假设**: 用OPES-multiT生成的高质量构象系综训练AI模型，可提高AI生成IDP构象的物理真实性
   - **初步方法**: 用本文4个体系的OPES-multiT系综训练生成模型（如扩散模型），评估生成构象的Rg、螺旋度分布与OPES系综的一致性
   - **验证方式**: 生成系综与实验数据（NMR、SAXS）的一致性
   - **创新状态**: unverified

4. **候选名称**: IDP瞬态三级结构的序列决定因素分析
   - **来源局限/观察**: 本文仅研究了4个体系，瞬态三级结构的序列基础尚不清楚
   - **核心假设**: 特定序列模式（如疏水残基分布、电荷模式）决定IDP瞬态三级结构的倾向
   - **初步方法**: 对多个IDP进行OPES-multiT模拟，建立瞬态结构倾向与序列特征的关联模型
   - **验证方式**: 预测的序列特征与实验检测的瞬态结构（如NMR PRE）比较
   - **创新状态**: unverified

5. **候选名称**: OPES-multiT与AI增强采样结合的双层采样框架
   - **来源局限/观察**: OPES-multiT的bias收敛在大体系中成功率低（10%）
   - **核心假设**: AI模型可预测OPES bias的初始猜测，加速收敛
   - **初步方法**: 用AI模型预测势能面特征，初始化OPES bias，再进行multithermal模拟
   - **验证方式**: 比较AI初始化与随机初始化的bias收敛时间和系综质量
   - **创新状态**: unverified