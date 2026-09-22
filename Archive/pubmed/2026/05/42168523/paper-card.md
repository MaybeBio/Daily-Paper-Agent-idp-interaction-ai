## 01 基本信息

- **标题**：Deciphering the role of tubulin's C-terminal tail in kinesin binding using computational and clustering approaches
- **作者**：Shen, Ting; Li, Yuyan; Li, Yangle; Zhao, Jingjing; Ma, Jianxin; Cheng, Haojie; Zhang, Jiayi; Zhou, Meng; Zheng, Wei; Hu, Dehua; Li, Lin; Liu, Kefu; Sun, Shengjie
- **单位**：未提供（作者单位未在摘要/正文中列出）
- **期刊/平台**：Scientific Reports
- **年份**：2026-05-22
- **论文类型**：研究论文（计算模拟为主）
- **领域**：计算结构生物学、分子动力学模拟、微管-驱动蛋白互作
- **关键词**：tubulin C-terminal tail (CTT)、kinesin、intrinsically disordered region (IDR)、steered molecular dynamics (SMD)、electrostatic interactions、clustering
- **DOI/arXiv**：10.1038/s41598-026-54092-0
- **代码**：未提供
- **数据**：未提供（模拟轨迹未公开）
- **阅读日期**：2026-05-22
- **在该方向中的位置**：本文聚焦于微管蛋白（tubulin）C末端尾部（CTT，一个典型的IDR）在驱动蛋白（kinesin）结合过程中的具体分子机制，采用SMD、全原子MD、MM-PBSA、DelPhi静电计算和BSKC聚类方法。该文属于「IDR介导蛋白互作 × 物理模拟（MD）」方向，不涉及深度学习/AI方法，但为IDR在蛋白-蛋白结合中的动态角色提供了原子级证据，可作为IDP/IDR互作机制研究的参考案例。

## 02 一句话总结

本文通过SMD和全原子MD模拟，发现β-微管蛋白的CTT（IDR）通过"钩住-捕获-稳定"机制增强KIF7驱动蛋白与微管的结合：CTT在受力分离时以α-螺旋构象钩住KIF7，去除外力后促进KIF7重新结合，并通过增强静电相互作用、降低结合自由能（−25.33 vs −22.52 kcal/mol）和重塑氢键网络来稳定复合物。

## 03 研究问题

- **具体问题**：微管蛋白α/β亚基的C末端尾部（CTT，均为IDR）在驱动蛋白KIF7与微管结合过程中扮演什么具体角色？其分子机制是什么？
- **为什么重要**：CTT是微管蛋白上最突出的IDR，富含谷氨酸/天冬氨酸，带强负电荷。已有生化实验表明切除CTT会降低驱动蛋白的过程性和速度，但CTT在结合过程中的原子级动态机制尚不清楚。KIF7是一种非典型驱动蛋白（不能运动，作为信号支架），其与微管的结合机制与运动型驱动蛋白不同，且与胚胎发育密切相关。
- **现有方法为何不足**：静态结构（如冷冻电镜）无法捕捉IDR的动态构象变化；以往计算研究多关注运动型驱动蛋白（kinesin-1、KIF1A等），对非运动型KIF7的CTT结合机制缺乏研究；且多数研究未区分总静电力和结合分量。
- **精确研究问题**：Can the intrinsically disordered C-terminal tail of β-tubulin enhance KIF7 binding through a disorder-to-helix conformational transition and electrostatic tethering mechanism?

## 04 背景与发展脉络

**注：以下脉络基于本文引文和讨论，属于「经外部核验」的领域发展框架。**

1. **阶段一：生化实验揭示CTT的功能必要性**（~2000s-2010s）
   - 代表性方法：蛋白酶切除CTT、体外 motility assay
   - 发现：切除CTT降低驱动蛋白过程性和速度
   - 局限：无法提供原子级机制解释

2. **阶段二：计算模型提出"弱拴绳"假说**（~2010s-2020s）
   - 代表性方法：粗粒化MD（Mizuhara & Takano）、全原子MD
   - 发现：CTT产生棘轮样能量景观，偏向驱动蛋白向微管正极运动；"catch-and-guide"模型提出CTT在步进循环中短暂拴住未结合的马达头
   - 局限：多针对运动型驱动蛋白（KIF1A、kinesin-1），未覆盖非运动型KIF7；缺乏对结合过程的直接模拟

3. **阶段三：本文位置**（2026）
   - 方法：SMD + 全原子MD + MM-PBSA + DelPhi静电计算 + BSKC聚类
   - 贡献：首次对KIF7（非运动型信号驱动蛋白）与TUBA4A-TUBB8（胚胎特异微管蛋白异二聚体）的CTT结合机制进行原子级模拟；提出"钩住-捕获-稳定"两步机制；验证了结合分量静电力的预测优势

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 静态结构无法揭示IDR动态功能 | 冷冻电镜结构（如PDB: 6MLQ）只能提供单一构象，无法解释CTT如何参与结合过程 | IDR本质上是构象异质的，静态结构无法捕捉其动态行为 | Introduction：指出"little attention is paid to the specific role and mechanistic details of the CTTs on the binding process" |
| 运动型驱动蛋白研究无法推广到非运动型 | KIF7不能沿微管运动，其结合机制与kinesin-1/KIF1A不同 | KIF7的化学机械耦合缺陷使其成为研究纯结合行为的理想系统 | Introduction：KIF7 "has a defect in chemomechanical coupling that prevents it from moving in microtubules and have high binding ability to microtubules" |
| 总静电力不能准确反映结合趋势 | 总静电力包含非结合方向的分量，可能高估或低估实际结合强度 | 结合分量（F_binding = F_T·cosα）更准确反映沿结合方向的力 | Methods "Electrostatic force calculation"；Discussion引用Li & Alexov工作26,34 |
| 体细胞微管蛋白亚型无法代表胚胎系统 | 以往研究多使用体细胞微管蛋白亚型，而胚胎中TUBA4A-TUBB8是主要亚型 | CTT序列在不同亚型间有差异，可能影响结合行为 | Discussion："we model the TUBA4A–TUBB8 heterodimer, the predominant isotype in human oocytes and early embryos" |

## 06 核心思想

### 1) 表面方法
- 使用AlphaFold 3预测TUBA4A和TUBB8（含/不含CTT）的三维结构，SWISS-MODEL预测KIF7头部结构
- 基于PDB: 6MLQ（KIF7-微管复合物冷冻电镜结构）进行结构匹配
- 执行SMD（双相拉力：6.96 pN→13.92 pN）模拟KIF7从微管上分离的过程
- 执行全原子MD模拟（含/不含CTT的复合物）
- 使用BSKC聚类分析CTT的构象变化
- 使用DelPhi/DelphiForce计算静电势和静电力
- 使用MM-PBSA计算结合自由能
- 使用VMD进行氢键分析

### 2) 核心洞察
- **CTT是"动态钩子"而非静态锚点**：在无KIF7时，β-tubulin CTT从初始α-螺旋逐渐解折叠为完全无序状态；但在KIF7存在时，CTT保持稳定的α-螺旋构象。这种"上下文依赖的构象行为"是IDR功能的核心。
- **两步结合机制**：第一步，无序CTT以"钩住"方式捕获KIF7（通过特定氢键如KIF7-Asn341:TUBB8-Val443和KIF7-Arg294:TUBB8-Glu436）；第二步，CTT经历无序→α-螺旋转变，形成"棍状"稳定结构，增强结合。
- **静电增强是主要驱动力**：CTT的存在使结合界面的负电荷区域扩展，同时诱导KIF7上正电荷斑块集中化，静电结合力提升15-20%，结合自由能降低约3 kcal/mol。

### 3) 可能的普适教训 [Analysis]
- **IDR的"上下文依赖折叠"是功能实现的关键**：同一IDR序列在不同结合状态下可呈现完全不同的构象（无序↔螺旋），这种可塑性是IDR介导互作的核心优势。
- **"捕获-稳定"两步机制可能广泛存在于IDR介导的蛋白互作中**：IDR先以低亲和力、高构象熵的方式"捕获"结合伙伴，再通过诱导折叠稳定复合物——这与相分离中"多价弱相互作用→凝聚"的逻辑一致。
- **结合分量静电力比总静电力更物理**：在计算IDR介导的静电贡献时，应使用F_binding = F_T·cosα而非总力。

## 07 方法总览

- **输入**：蛋白序列（TUBA4A: P68366全长；TUBB8: Q3CMZ7全长；KIF7: Q2M1P5头部1-358）、PDB: 6MLQ复合物结构
- **结构预测**：SWISS-MODEL（KIF7头部）、AlphaFold 3（TUBA4A/TUBB8含或不含CTT）
- **系统构建**：CHARMM-GUI生成模拟体系，CHARMM36m力场，TIP3P水模型（15 Å厚度），150 mM NaCl，PME长程静电
- **模拟类型**：
  - SMD：双相拉力方案，初始6.96 pN持续500 ps，后加倍至13.92 pN直至完全分离
  - 全原子MD：含/不含CTT的复合物，用于RMSF、氢键、构象分析
- **分析工具**：
  - BSKC聚类（最大簇数10，用于CTT构象分类）
  - DelPhi（静电势，介电常数2/80，150 mM盐浓度）
  - DelphiForce（静电力，含结合分量计算）
  - MM-PBSA（结合自由能，含范德华、库仑、极性和非极性溶剂化能）
  - VMD（氢键分析，截断3.5 Å/20°）
- **输出**：CTT构象动态、结合自由能、静电力和势分布、氢键网络、RMSF
- **反馈回路**：无（非自适应模拟）
- **文字流程**：序列获取 → 结构预测 → 结构匹配（基于6MLQ）→ 体系构建 → SMD分离模拟 + 全原子MD平衡模拟 → BSKC聚类分析CTT构象 → DelPhi/DelphiForce静电分析 → MM-PBSA自由能计算 → VMD氢键分析 → 整合机制模型

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| AlphaFold 3结构预测 | 预测TUBA4A/TUBB8含/不含CTT的三维结构 | 实验结构缺乏，需获得含CTT的完整结构 | 输入：蛋白序列；输出：预测结构 | Methods "Modelling"；Fig. S1 | 无法获得含CTT的起始结构，模拟无法进行 |
| SMD双相拉力模拟 | 模拟KIF7从微管分离过程，观察CTT的"钩住"行为 | 直接观察外力下CTT如何抵抗分离 | 输入：平衡后的复合物；输出：分离轨迹、力-位移曲线 | Fig. 2a-d；Movie S1-S3 | 无法直接证明CTT的"钩住-捕获"功能 |
| 全原子MD + RMSF | 比较含/不含CTT时KIF7和tubulin的构象柔性 | 量化CTT对结合界面稳定性的影响 | 输入：复合物结构；输出：RMSF曲线 | Fig. 1d-e | 无法评估CTT对整体复合物动态的影响 |
| BSKC聚类 | 对CTT构象进行分类，识别功能相关构象态 | IDR构象异质，需识别主要构象状态 | 输入：MD轨迹；输出：聚类代表结构 | Fig. 1a-c；Table S1 | 无法系统描述CTT的构象景观 |
| DelPhi/DelphiForce静电计算 | 计算静电势和静电力（含结合分量） | 验证CTT的静电增强假说 | 输入：复合物结构；输出：静电势图、力值 | Fig. 3a-d | 无法定量评估静电贡献 |
| MM-PBSA | 计算结合自由能及其分解 | 定量比较含/不含CTT的结合强度 | 输入：MD轨迹；输出：ΔG_bind及各组分 | Fig. 3e-g | 无法定量证明CTT对结合亲和力的贡献 |
| 氢键分析 | 识别CTT-KIF7间关键氢键 | 提供原子级相互作用证据 | 输入：MD轨迹；输出：氢键占有率 | Fig. 4a-d | 无法解释CTT特异性识别KIF7的分子基础 |

## 09 关键公式符号

1. **RMSD**（Methods, 公式1）：
   \[
   RMSD(t) = \left[ \frac{1}{W N} \sum_{i=1}^{N} w_i |r_i(t) - r_i^{ref}|^2 \right]^{1/2}
   \]
   - W = Σw_i：权重因子
   - N：原子总数
   - r_i(t)：t时刻原子i的位置（最小二乘拟合后）
   - r_i^{ref}：参考结构中原子i的位置

2. **RMSF**（Methods, 公式2）：
   \[
   RMSF_i = \left[ \frac{1}{T} \sum_{t_j=1}^{T} |r_i(t_j) - r_i^{ref}|^2 \right]^{1/2}
   \]
   - i：残基编号
   - T：总模拟时间
   - r_i(t_j)：t_j时刻原子i的位置

3. **结合静电力分量**（Methods, 公式3）：
   \[
   F_{binding} = F_T \cdot \cos\alpha
   \]
   - F_T：总静电力
   - α：静电力方向与两亚基质心连线之间的夹角

4. **MM-PBSA结合自由能**（Methods, 公式4）：
   \[
   \Delta E_{total\_bind} = \Delta E_{c\_bind} + \Delta E_{v\_bind} + \Delta E_{p\_bind} + \Delta E_{np\_bind}
   \]
   - ΔE_c_bind：库仑结合能
   - ΔE_v_bind：范德华结合能
   - ΔE_p_bind：极性溶剂化结合能
   - ΔE_np_bind：非极性溶剂化结合能

## 10 实验设计与证据链

**数据集/群体**：TUBA4A（P68366）、TUBB8（Q3ZCM7）、KIF7头部（Q2M1P5, 1-358）；PDB: 6MLQ复合物结构

**规模**：SMD模拟（双相拉力，总时长未明确报告）；全原子MD模拟（含/不含CTT，时长未明确报告）；MM-PBSA采样（未明确报告帧数）

**指标**：RMSD、RMSF、结合自由能（MM-PBSA）、静电力（总力和结合分量）、静电势分布、氢键占有率、BSKC聚类构象

**基线/对比**：含CTT vs 不含CTT的复合物；有KIF7 vs 无KIF7的β-tubulin单体

**评测协议**：SMD中监测力-位移曲线和分离时间；MD中比较RMSF和氢键网络；MM-PBSA比较结合自由能

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|------------|------------------|------|
| SMD分离模拟 | CTT能抵抗KIF7分离 | 含CTT vs 不含CTT复合物，双相拉力 | 含CTT时分离延迟，CTT"钩住"KIF7（Fig. 2b-d） | CTT提供额外结合力 | 无法定量分离阻力大小 | Fig. 2；Movie S1-S3 |
| 去除外力后模拟 | CTT能促进KIF7重新结合 | 外力去除后观察 | CTT将KIF7拉回并促进重结合（Movie S2） | CTT具有"捕获"功能 | 无法确定重结合的时间尺度 | Movie S2 |
| RMSF分析 | KIF7结合降低CTT柔性 | 有KIF7 vs 无KIF7的β-tubulin | 结合后CTT RMSF显著降低（Fig. 1d-e） | 结合诱导CTT稳定化 | 无法区分诱导折叠vs构象选择 | Fig. 1d-e |
| BSKC聚类 | CTT构象在结合后趋于有序 | 单体vs复合物轨迹 | 复合物中CTT以α-螺旋为主（Fig. 1a-c） | 无序→螺旋转变是功能相关 | 无法确定转变的动力学路径 | Fig. 1a-c；Table S1 |
| 静电势/力计算 | CTT增强静电相互作用 | 含CTT vs 不含CTT | 含CTT时负电区域扩展，结合静电力提升15-20%（Fig. 3a-d） | 静电增强是CTT功能的主要机制 | 无法排除疏水/范德华贡献 | Fig. 3a-d |
| MM-PBSA | CTT降低结合自由能 | 含CTT vs 不含CTT | 含CTT时ΔG_bind更低（−25.33 vs −22.52 kcal/mol）（Fig. 3e-g） | CTT增强结合亲和力 | 无法确定熵-焓补偿细节 | Fig. 3e-g |
| 氢键分析 | CTT重塑氢键网络 | 含CTT vs 不含CTT | 关键氢键如KIF7-Arg308:TUBB8-Gln410占有率从7.92%升至76.24%（Fig. 4） | CTT选择性重塑界面氢键 | 无法确定这些氢键的功能必要性 | Fig. 4 |

## 11 结论正确解读

- **任务范围**：本研究仅针对KIF7（非运动型驱动蛋白）与TUBA4A-TUBB8（胚胎特异微管蛋白）的复合物。结论不能直接推广到其他驱动蛋白家族成员或其他微管蛋白亚型。
- **Oracle/真值输入**：AlphaFold 3预测的tubulin结构（含CTT）和SWISS-MODEL预测的KIF7头部结构均为计算预测，未经实验验证。PDB: 6MLQ提供了复合物模板，但KIF7在其中的构象可能不代表溶液中的全部状态。
- **端到端状态**：本研究为纯计算模拟，无湿实验验证。所有结论均为计算预测。
- **算力成本**：未报告具体算力消耗。
- **历史数据依赖**：依赖PDB: 6MLQ冷冻电镜结构作为模板，该结构的分辨率和构象状态影响模拟起点。
- **模型依赖**：CHARMM36m力场对IDR的描述能力有限；TIP3P水模型；AlphaFold 3对IDR的预测可靠性存疑（作者在讨论中也承认"static structural prediction cannot capture the full functional repertoire of these regions"）。
- **最难情形**：CTT的完全无序状态在模拟中难以充分采样；SMD的拉力方案可能引入非生理路径。
- **群体/领域边界**：结果仅适用于KIF7-TUBA4A-TUBB8系统；对运动型驱动蛋白（kinesin-1等）的CTT机制可能不同（作者在讨论中引用了KIF1A和kinesin-2的差异）。
- **不确定性**：MM-PBSA的熵贡献计算精度有限；静电力计算基于连续介质模型，忽略分子动力学涨落。

**有边界的复述**：在CHARMM36m力场和本文模拟条件下，β-tubulin CTT通过无序→α-螺旋转变和静电增强机制，使KIF7与TUBA4A-TUBB8的结合自由能降低约2.8 kcal/mol，结合静电力提升15-20%，并在外力下通过"钩住"机制抵抗分离。这些结论限于计算模型，需实验验证。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 静态结构预测无法捕捉IDR全部功能 | AlphaFold预测的α-螺旋构象与MD模拟中观察到的无序状态不一致 | 未明确提及 | Discussion："static structural prediction cannot capture the full functional repertoire of these regions" |
| 不同tubulin CTT和核苷酸状态的作用未探索 | 未测试不同微管蛋白亚型CTT或不同核苷酸状态（ATP/ADP）对KIF7结合的影响 | "whether the different tubulin CTTs and nucleotide state have a similar role in binding kinesin still requires further investigation" | Discussion |
| 模型选择限制了对α-tubulin CTT的研究 | 复合物模型中KIF7更接近β-tubulin CTT，限制了α-tubulin CTT结合作用的研究 | 未明确提及 | Discussion："the selected complex model, in which KIF7 is closer to β-tubulin, limits discovery of α-tubulin CTT binding roles with kinesin" |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| AlphaFold 3预测的CTT为α-螺旋，但MD显示无KIF7时变为无序 | AlphaFold 3对IDR的预测可能不可靠；或模拟力场偏向无序态 | 起始结构影响整个模拟结论 | 使用实验NMR或SAXS数据约束IDR构象；或使用多力场交叉验证 | Methods "Modelling"；Fig. 1a-c |
| SMD的拉力参数（6.96→13.92 pN）未提供合理性论证 | 拉力速率和方向可能影响"钩住"现象的观察 | SMD结果高度依赖拉力协议 | 变拉力速率/方向；使用伞形采样或Metadynamics验证 | Methods "SMD"；Fig. 2 |
| MM-PBSA的ΔG差异仅2.8 kcal/mol，未报告误差范围 | 该差异可能落在计算误差内 | 结合自由能差异是核心结论之一 | 使用TI/FEP方法交叉验证；报告标准误差 | Fig. 3e-g |
| 氢键分析仅报告了占有率变化，未进行突变验证 | 关键氢键的功能必要性未证实 | "选择性重塑氢键网络"的结论需要功能验证 | 对关键残基（如KIF7-Arg308）做点突变模拟 | Fig. 4 |
| 未报告模拟的重复次数和收敛性分析 | 单次模拟可能未充分采样IDR构象空间 | IDR模拟需要充分采样才能得出可靠结论 | 多次独立模拟；检查RMSD收敛；使用增强采样方法 | Methods "MD simulation" |
| 与实验数据的对比有限 | 未与已知的CTT截短突变体实验数据直接对比 | 计算结论需要实验锚点 | 模拟CTT截短突变体，与文献实验数据对比 | Introduction引用11,12 |

## 14 Agent 提炼的知识候选

**面向课题方向（IDP/IDR × 蛋白互作 × AI/物理模拟）的可迁移知识：**

1. **"上下文依赖折叠"作为IDR功能标志**：本文核心发现——同一IDR（β-tubulin CTT）在无结合伙伴时趋于无序，在结合KIF7时稳定为α-螺旋——提示在IDR介导的互作研究中，应同时模拟"自由态"和"结合态"，比较构象差异。可迁移到其他IDR介导的互作体系（如转录因子、信号蛋白）。

2. **"捕获-稳定"两步机制**：IDR先以低亲和力"捕获"结合伙伴（通过少数关键氢键），再通过诱导折叠稳定复合物。这一机制与相分离中的"多价弱相互作用→凝聚"逻辑高度一致，可作为IDR介导凝聚体形成的分子机制假设。

3. **结合分量静电力（F_binding = F_T·cosα）优于总静电力**：在计算IDR（富含电荷）介导的静电贡献时，应使用沿结合方向的力分量，而非总力。这一方法学改进可直接迁移到其他带电IDR互作体系。

4. **BSKC聚类用于IDR构象分析**：使用改进的RMSD度量（强调蛋白间接触和IDR区域）进行k-means聚类，可有效识别IDR的主要构象状态。该方法可迁移到其他IDR的MD轨迹分析。

5. **AlphaFold 3预测IDR结构的局限性警示**：本文明确展示AlphaFold预测的IDR构象（α-螺旋）与MD模拟结果（无序）不一致，提示在IDR研究中不能依赖静态结构预测，需结合MD或实验构象系综。

6. **IDR的"棍状化"（rod-like stabilization）作为结合增强机制**：IDR从柔性无序态转变为刚性螺旋态，既减少熵代价又提供结构化结合界面。这一概念可迁移到设计IDR介导的互作调控策略。

7. **微管蛋白CTT作为"静电钩子"的模型**：强负电IDR通过长程静电作用"预组织"正电结合伙伴，再通过构象转变稳定结合。这一"静电预组织→构象锁定"模型可推广到其他带相反电荷的IDR-蛋白互作对。

## 15 与已有知识的连接

- **Mizuhara & Takano（粗粒化MD）**：本文引用的"棘轮样能量景观"模型，与本文的"钩住-捕获"机制一致，但本文提供了全原子水平的直接证据。可连接至相分离中IDR介导的定向运输/富集机制。
- **Nguyen et al. "catch-and-guide"模型**：本文SMD结果直接支持该模型，并提供了原子级结构基础。该模型与相分离中IDR"招募"结合伙伴的机制高度相关。
- **Xie & Li（DelPhiForce分析）**：本文引用的β-tubulin E-hook对kinesin吸引力更强的发现，与本文静电增强结论一致。可连接至IDR电荷模式（charge pattern）与结合特异性的关系。
- **AlphaFold 3 / AlphaFold 2对IDR的预测局限**：已有文献广泛报道AF对IDR预测不可靠，本文提供了具体案例。可连接至"AI预测结构 + MD精修"的混合策略在IDR研究中的应用。
- **微管蛋白翻译后修饰（PTM）对CTT的调控**：CTT上的酪氨酸化/去酪氨酸化、多聚谷氨酰化等PTM已知调控驱动蛋白结合，本文的静电机制为理解PTM如何通过改变CTT电荷影响结合提供了框架。
- **相分离中的IDR静电相互作用**：本文的"静电增强结合"机制与相分离中"电荷互补驱动凝聚"的机制一致，可连接至IDR介导凝聚体的计算模拟方法。

## 16 研究想法

**Agent 生成的研究候选：**

1. **候选名称**：IDR介导凝聚体中"捕获-稳定"机制的粗粒化验证
   - **来源局限/观察**：本文在单分子水平提出"捕获-稳定"两步机制，但未在凝聚体（多分子）水平验证
   - **核心假设**：在相分离条件下，IDR的"捕获-稳定"机制通过多价效应被放大，驱动凝聚体形成
   - **初步方法**：使用粗粒化MD（如MARTINI或HPS模型）模拟多个KIF7-微管蛋白复合物，观察CTT介导的聚集行为
   - **验证方式**：比较含/不含CTT的体系在相同条件下的凝聚倾向（cluster size、density）
   - **创新状态**：unverified

2. **候选名称**：基于AlphaFold 3 + MD的IDR结合构象系综预测流程
   - **来源局限/观察**：本文发现AF3预测的IDR构象与MD结果不一致，但未提出改进策略
   - **核心假设**：AF3预测的IDR构象可作为MD模拟的"种子"，通过多起始点MD采样获得更可靠的IDR结合构象系综
   - **初步方法**：对同一IDR-蛋白对，使用AF3预测多个构象作为MD起始点，比较各轨迹的收敛性和结合自由能
   - **验证方式**：与实验（NMR化学位移扰动、H/D交换）数据对比
   - **创新状态**：unverified

3. **候选名称**：微管蛋白CTT电荷模式与驱动蛋白结合特异性的机器学习预测
   - **来源局限/观察**：本文仅研究TUBA4A-TUBB8一种亚型，但人类有多个微管蛋白亚型，CTT序列差异大
   - **核心假设**：CTT的电荷模式（如负电残基分布、PTM位点）可预测其与不同驱动蛋白的结合亲和力
   - **初步方法**：收集已知微管蛋白亚型CTT序列和对应驱动蛋白结合数据，训练序列-结合亲和力预测模型（如CNN或Transformer）
   - **验证方式**：留一亚型交叉验证；对预测的高/低亲和力对进行MD验证
   - **创新状态**：unverified

4. **候选名称**：IDR介导互作中"静电预组织"的通用物理模型
   - **来源局限/观察**：本文提出"静电增强"机制，但未给出定量物理模型
   - **核心假设**：IDR的净电荷、电荷分布和长度可参数化为一个"静电捕获半径"，预测其对结合伙伴的捕获效率
   - **初步方法**：基于Poisson-Boltzmann理论建立IDR-蛋白静电相互作用的解析模型，用本文的MD数据拟合参数
   - **验证方式**：预测其他IDR-蛋白对的结合速率常数，与实验（停流或表面等离子共振）对比
   - **创新状态**：unverified

5. **候选名称**：IDR的"上下文依赖折叠"作为相分离驱动力的热力学分析
   - **来源局限/观察**：本文发现IDR在结合时从无序→螺旋转变，但未分析该转变对相分离自由能的贡献
   - **核心假设**：IDR的结合诱导折叠（coupled folding and binding）通过减少构象熵代价，降低相分离的临界浓度
   - **初步方法**：使用伞形采样或Metadynamics计算IDR在自由态和结合态的构象自由能差，结合Flory-Huggins理论预测相分离相图
   - **验证方式**：与体外凝聚实验（浊度、FRAP）对比
   - **创新状态**：unverified