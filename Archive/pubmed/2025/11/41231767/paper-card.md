## 01 基本信息

- **标题**：DynaRepo: the repository of macromolecular conformational dynamics
- **作者**：Mokhtari, Omid; Bignon, Emmanuelle; Khakzad, Hamed; Karami, Yasaman
- **单位**：Inria Center at the University of Lorraine（法国洛林大学Inria中心）
- **期刊/平台**：Nucleic Acids Research
- **年份**：2025
- **论文类型**：数据库/资源类论文（Database/Resource Article）
- **领域**：结构生物学、分子动力学模拟、生物信息学数据库
- **关键词**：分子动力学模拟、构象动力学、蛋白质复合物、蛋白质-核酸复合物、MD数据库、FAIR原则
- **DOI/ID**：10.1093/nar/gkaf1130
- **代码**：MDDB workflow: https://github.com/mmb-irb/MDDB-workflow
- **数据**：https://dynarepo.inria.fr/
- **阅读日期**：2025-11-13
- **该文在课题方向中的位置**：本文是面向「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向的重要数据基础设施。它提供了大规模、标准化、FAIR合规的蛋白-蛋白和蛋白-核酸复合物MD轨迹数据，可直接用于训练动力学感知的深度学习模型（如结合位点预测、结合亲和力估计）。值得注意的是，作者在数据筛选时**明确排除了含有IDP/IDR的复合物**（见Methods），这既是本课题可利用数据的局限，也提示了该方向的数据空白。

---

## 02 一句话总结

本文构建了DynaRepo数据库——一个包含约450个蛋白-蛋白复合物、约270个单链蛋白和7个核小体变体的MD模拟轨迹（每个体系3次重复×500 ns，总计>1100 μs）的开放资源库，通过统一的MD流程和预计算分析（RMSD、RMSF、PCA、氢键、能量、口袋检测等），为动力学感知的深度学习框架提供训练数据基础。

---

## 03 研究问题

- **具体问题**：如何构建一个大规模、标准化、FAIR合规的分子动力学模拟数据库，以弥补深度学习模型训练中「动态构象数据」的稀缺？
- **为什么重要**：AlphaFold2/3等静态结构预测方法无法捕捉蛋白的构象异质性和动态行为，而动态行为对理解抗体-抗原识别、无序蛋白功能、蛋白-核酸结合等关键生物学过程至关重要。现有MD数据库要么规模小、要么缺乏标准化协议、要么不聚焦于复合物。
- **现有方法不足**：MDRepo、MDDB等已有平台缺乏针对大分子复合物的系统化MD数据；不同实验室的MD协议差异大，难以直接用于训练统一模型；缺乏预计算分析结果，用户需自行处理原始轨迹。
- **精确研究问题**：Can a standardized, FAIR-compliant MD repository focused on macromolecular complexes (protein–protein and protein–nucleic acid) provide sufficient dynamics data to train deep learning models for binding site prediction and affinity estimation?

---

## 04 背景与发展脉络

> 注：以下脉络基于本文引用和讨论，属于「经外部核验」的领域发展框架。

1. **静态结构预测时代（2018-2023）**：AlphaFold2 [1]、AlphaFold3 [2]、RoseTTAFoldNA [3] 等深度学习方法在静态结构预测上取得突破性进展。局限：无法捕捉构象异质性、内在无序区、动态结合过程。
2. **MD模拟数据库早期探索（2010s-2020s）**：MoDEL [11]、Dynameomics [12]、ATLAS [13] 等提供蛋白MD轨迹，但多为单链蛋白、规模有限、协议不统一。MemProtMD [8]、GPCRmd [9] 等聚焦特定蛋白类别。
3. **开放科学MD平台兴起（2020s）**：MDRepo（开放仓库）、MDDB（欧洲联邦式分布式数据库）等推动MD数据共享标准化。MDDB采用MDPosit软件栈和REST API实现联邦式互操作。
4. **动力学感知AI的萌芽（2023-至今）**：DynamicGT [16]（动力学感知结合位点预测）、Boltz-2 [17]（结合亲和力预测）、BioEmu [18]（构象集合生成）等开始利用MD轨迹训练模型，但受限于数据规模。
5. **DynaRepo的位置**：作为MDDB首个法国节点，填补「大分子复合物MD数据」空白，提供标准化协议+预计算分析+API访问的一站式资源，直接服务于动力学感知AI模型的训练。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 动态数据稀缺 | 深度学习模型主要依赖静态结构，无法捕捉构象异质性 | 缺乏大规模、高质量的MD轨迹数据集 | Introduction: "the scarcity of openly available, high-quality dynamic datasets" |
| 数据协议不统一 | 不同实验室的MD模拟条件差异大，难以直接比较或合并训练 | 缺乏标准化流程和统一的质量控制 | Introduction: "comparative analyses across simulations from different research groups remain challenging due to variations in system preparation, MD protocols, software packages, and force fields" |
| 复合物数据缺失 | 现有MD数据库多为单链蛋白，缺乏蛋白-蛋白和蛋白-核酸复合物 | 复合物体系大、模拟成本高、分析复杂 | Introduction: "DynaRepo focuses on macromolecular complexes, including protein–nucleic acid assemblies rather than isolated proteins or small molecules" |
| 数据可访问性差 | 原始轨迹文件大，用户难以快速获取预计算结果 | 缺乏预计算分析和API接口 | Results: 每个条目附带RMSD、RMSF、PCA等预计算分析，支持API访问 |
| 蛋白-核酸动态数据空白 | 蛋白-DNA/RNA复合物的MD数据尤其稀缺 | 核酸力场参数复杂、模拟难度大 | Discussion: "the shortage of dynamic datasets for protein–nucleic acid complexes, which currently limits broad generalization across molecular interaction types" |

---

## 06 核心思想

### 1) 表面方法
构建一个基于MDDB联邦架构的MD轨迹数据库节点，对来自PDBbind、SAbDab、Testing Transient和核小体数据集的结构进行统一的MD模拟（3×500 ns），并通过MDPosit软件栈提供预计算分析和可视化。

### 2) 核心洞察
**「数据标准化+预计算分析+开放API」三位一体**是推动动力学感知AI落地的关键。仅提供原始轨迹不足以服务社区——需要统一的模拟协议保证数据可比性，预计算分析降低使用门槛，API接口支持程序化访问和大规模训练数据获取。

### 3) 可能的普适教训 [Analysis]
- 对无序蛋白/相分离课题：DynaRepo的架构模式（标准化MD+预计算+API）可直接迁移到IDP/IDR的MD数据收集与共享，但目前IDP/IDR数据在该库中被系统性排除，提示该方向需要专门的数据库建设。
- 对AI方法开发：动力学感知模型（如DynamicGT）需要大规模、多样化的MD轨迹，DynaRepo的模式可作为IDP/IDR动力学数据基础设施的模板。

---

## 07 方法总览

- **输入**：来自4个数据源的三维结构——PDBbind v2020蛋白-蛋白复合物（经筛选）、SAbDab抗原、Testing Transient数据集（53个单链蛋白及其复合物）、核小体结构变体
- **筛选流程**（以PDBbind为例）：(i) 排除NMR结构；(ii) 分辨率<3.5 Å；(iii) 结构缺口<4个；(iv) 基于MM-align的MM-score进行层次聚类去冗余（距离阈值0.55）；(v) 人工检查排除问题条目
- **MD模拟协议**（蛋白体系）：GROMACS 2024.2 + CHARMM36m力场；缺口残基用MODELLER（≤5残基）或AlphaFold3（>5残基）补齐；150 mM NaCl生理盐浓度；TIP3P水模型；12 Å缓冲距离；5000步最陡下降能量最小化；6步逐步释放约束的NPT平衡（310 K，共0.375 ns）；3次重复×500 ns生产模拟；2 fs时间步长；每100 ps输出坐标
- **MD模拟协议**（核小体体系）：Amber20或NAMD3；ff14SB+BSC1+CUFIX+TIP3P力场组合；20 Å截断八面体水盒；150 mM NaCl；10000-40000步最小化；40-100 ns NPT平衡；2-6次重复×2-4 μs生产模拟；存储时1 frame = 1 ns
- **后处理分析**：RMSD（对首帧和平均结构，可选原子类型）、RMSF、TM-score、回旋半径、PCA（协方差矩阵，2000帧）、聚类、溶剂可及表面积、残基间距离、静电势表面、氢键（供体-受体距离<3 Å，角度>135°）、能量（静电+范德华）、口袋检测（MDpocket）
- **数据库架构**：MDPosit软件栈 + REST API + OPTIMADE接口；支持外部贡献（标准化提交流程）
- **输出**：交互式可视化页面（Overview/Trajectory/Analyses/Download）、可下载的PDB/xtc/tpr文件、API访问接口

**文字流程**：结构筛选 → 缺口补齐 → 力场参数化 → 溶剂化 → 能量最小化 → 逐步平衡 → 3×500 ns生产模拟 → 后处理分析 → 元数据标注 → 上传至DynaRepo → 用户通过Web界面或API访问

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 数据筛选管道 | 从PDBbind等来源选择高质量、非冗余结构 | 保证数据质量、避免冗余偏差 | 输入：PDBbind 2852条目；输出：405个复合物 | Methods "Data selection" 节 | 移除后数据质量下降，模型训练受噪声结构影响 |
| 统一MD模拟协议 | 所有体系使用相同力场、溶剂条件、模拟时长 | 保证数据可比性和一致性 | 输入：筛选后结构；输出：3×500 ns轨迹 | Methods "Protocol for proteins" 节 | 移除后不同体系间无法直接比较，无法用于统一模型训练 |
| 缺口补齐模块 | MODELLER/AlphaFold3补齐缺失残基 | 完整结构是MD模拟的前提 | 输入：有缺口结构；输出：完整结构 | Methods: "missing residues were added using MODELLER v10.4... or with AlphaFold3" | 移除后大量结构无法模拟，数据量大幅减少 |
| 预计算分析管道 | 自动计算RMSD、RMSF、PCA等20+种分析 | 降低用户使用门槛，提供即用型数据 | 输入：MD轨迹；输出：预计算分析结果 | Results 节及图2 | 移除后用户需自行处理原始轨迹，使用门槛大幅提高 |
| MDPosit+API架构 | 提供Web可视化和程序化数据访问 | 支持大规模数据获取和联邦互操作 | 输入：分析结果+元数据；输出：Web界面+API响应 | Methods "Database implementation" 节 | 移除后数据可发现性和可访问性下降，违背FAIR原则 |
| 外部贡献机制 | 允许研究者提交新模拟数据 | 保证数据库持续增长 | 输入：外部MD数据；输出：标准化入库 | Methods "DynaRepo accepts external contributions" | 移除后数据库规模停滞，无法覆盖更多体系 |

---

## 09 关键公式符号

本文为数据库描述论文，核心公式较少，但以下概念在数据筛选中起关键作用：

1. **MM-score（MM-align）**：
   - 用途：结构相似性度量，用于层次聚类去冗余
   - 定义：基于TM-score的改进版本，用于多聚体结构比对
   - 聚类距离：$d = 1 - \text{MM-score}$
   - 阈值：$d < 0.55$ 视为同一簇
   - 来源：Methods "Data selection" 节

2. **RMSD（Root Mean Square Deviation）**：
   - $\text{RMSD} = \sqrt{\frac{1}{N}\sum_{i=1}^{N} \delta_i^2}$
   - 其中 $\delta_i$ 为第 $i$ 个原子（或残基）的坐标偏差，$N$ 为原子/残基总数
   - 用途：衡量模拟轨迹相对参考结构的偏差，用于质量控制
   - 来源：Methods "Post-simulation and meta-analysis" 节

3. **RMSF（Root Mean Square Fluctuation）**：
   - $\text{RMSF}_i = \sqrt{\frac{1}{T}\sum_{t=1}^{T} (\mathbf{r}_i(t) - \bar{\mathbf{r}}_i)^2}$
   - 其中 $\mathbf{r}_i(t)$ 为残基 $i$ 在时间 $t$ 的坐标，$\bar{\mathbf{r}}_i$ 为时间平均坐标
   - 用途：衡量每个残基的柔性，对IDP/IDR研究尤其重要
   - 来源：Methods "Post-simulation and meta-analysis" 节

4. **回旋半径（Radius of Gyration）**：
   - $R_g = \sqrt{\frac{\sum_i m_i (\mathbf{r}_i - \mathbf{r}_{\text{com}})^2}{\sum_i m_i}}$
   - 其中 $m_i$ 为原子 $i$ 的质量，$\mathbf{r}_{\text{com}}$ 为质心坐标
   - 用途：衡量蛋白紧凑度，对无序蛋白构象分析有直接参考价值
   - 来源：Methods "Post-simulation and meta-analysis" 节

---

## 10 实验设计与证据链

### 数据集与规模
- **PDBbind v2020**：初始2852个蛋白-蛋白复合物 → 筛选后405个
- **SAbDab抗原**：220个单链抗原
- **Testing Transient**：53个单链蛋白（同时模拟单体与复合物形式）
- **核小体**：7个结构变体（含不同翻译后修饰）
- **总计**：约450个复合物 + 约270个单链蛋白，>1100 μs MD数据，约1500条蛋白链

### 模拟参数
- 力场：CHARMM36m（蛋白体系）；ff14SB+BSC1+CUFIX+TIP3P（核小体体系）
- 模拟时长：3×500 ns/体系（蛋白）；2-4 μs/体系（核小体）
- 温度：310 K（蛋白）；300 K（核小体）
- 盐浓度：150 mM NaCl
- 软件：GROMACS 2024.2（蛋白）；Amber20/NAMD3（核小体）

### 评测指标
- 轨迹稳定性：RMSD、RMSF
- 结构紧凑性：回旋半径
- 构象采样：PCA、聚类分析
- 相互作用：氢键、残基间距离、静电势表面、能量（静电+范德华）
- 功能位点：口袋检测（MDpocket）

### 实验表格

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|-----------|-----------------|------|
| PDBbind筛选管道 | 去冗余后保留代表性复合物 | 2852→405，基于MM-score聚类 | 405个复合物进入模拟 | 数据覆盖多样化的蛋白-蛋白相互作用界面 | 未报告聚类后各簇的大小分布 | Methods "Data selection" |
| 3×500 ns重复模拟 | 重复采样可捕获构象异质性 | 不同初始速度 | 轨迹稳定（RMSD/RMSF监控） | 数据质量可靠，适合下游AI训练 | 未报告各体系收敛性定量指标 | Methods "Protocol for proteins" |
| 预计算分析管道 | 标准化分析可覆盖多种动力学特征 | 20+种分析类型 | 所有条目附带完整分析 | 用户可直接使用预计算结果 | 未报告分析结果与实验数据的一致性验证 | Results 节 |
| 核小体变体模拟 | 可模拟蛋白-DNA复合物的动态行为 | 7个变体，2-4 μs | 81 μs MD数据 | 覆盖蛋白-核酸相互作用的构象空间 | 仅7个体系，泛化性有限 | Methods "Nucleosomes" |
| 外部贡献机制 | 数据库可持续增长 | 标准化提交流程 | 接受外部数据 | 社区可共同扩展数据规模 | 尚未报告外部贡献的实际案例 | Methods "Database implementation" |

---

## 11 结论正确解读

- **任务范围**：本文是数据库资源论文，不涉及具体生物学发现或方法性能benchmark。其核心贡献是数据基础设施。
- **Oracle/真值输入**：模拟起始结构来自实验解析的晶体结构（PDB），但作者未报告对模拟结果与实验数据（如NMR、SAXS）的系统性验证。
- **端到端状态**：数据库已上线可访问（https://dynarepo.inria.fr/），但属于「持续增长」状态，非最终版本。
- **算力成本**：未报告总CPU/GPU小时数。仅提及核小体体系单系统约需数天（基于2-4 μs模拟时长推断），但具体硬件配置未说明。
- **历史数据依赖**：数据来源为PDBbind v2020、SAbDab等既有数据库，存在结构数据库本身的偏差（如晶体结构偏好稳定构象）。
- **模型依赖**：缺口补齐依赖MODELLER和AlphaFold3，后者预测的构象可能引入偏差。
- **最难情况**：核小体体系（约30万-40万原子）是计算量最大的体系，分析流程耗时约60小时/重复。
- **群体/领域边界**：数据覆盖蛋白-蛋白复合物、抗体-抗原、单链蛋白和核小体，但**明确排除了IDP/IDR体系**（见Methods筛选标准），也缺乏膜蛋白、RNA-only体系。
- **不确定性**：作者未报告模拟的系综收敛性分析，也未与实验系综（如NMR ensembles）进行系统比较。

**有边界的复述**：DynaRepo提供了约450个蛋白-蛋白复合物和约270个单链蛋白的标准化MD轨迹（3×500 ns），附带预计算分析，可作为训练动力学感知深度学习模型（如结合位点预测、亲和力估计）的数据源，但其数据范围明确排除了IDP/IDR体系，且未验证模拟系综与实验数据的一致性。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 蛋白-核酸复合物数据不足 | 目前仅包含核小体体系，缺乏多样化的蛋白-DNA/RNA复合物 | 未明确说明，但Discussion中承认这是限制泛化性的瓶颈 | Discussion: "the shortage of dynamic datasets for protein–nucleic acid complexes" |
| 500 ns模拟时长有限 | 不足以完全采样大蛋白复合物的构象空间 | 未明确说明 | Discussion: "the 500 ns trajectories in triplicate are not intended to exhaustively enumerate the conformational landscape" |
| 数据库持续增长中 | 当前规模有限，需社区贡献扩展 | 接受外部贡献，开发自动化提交流程 | Methods "DynaRepo accepts external contributions" |
| 核小体模拟使用不同力场 | 蛋白与核小体体系力场不统一 | 未明确说明 | Methods 中蛋白用CHARMM36m，核小体用ff14SB+BSC1+CUFIX |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 明确排除IDP/IDR体系 | 作者在PDBbind筛选中排除了「含有内在无序蛋白的复合物」，但未说明具体判定标准 | 对IDP/IDR研究群体而言，该数据库无法直接用于训练无序蛋白相关模型 | 检查筛选代码或补充材料中的IDP判定方法 | Methods "Data selection" 节 |
| 未报告模拟系综收敛性 | 500 ns×3重复可能不足以达到系综收敛，尤其对大型复合物 | 若轨迹未收敛，预计算分析可能误导下游模型训练 | 对代表性体系计算前后半段轨迹的构象分布重叠度 | Methods 中未提及收敛性分析 |
| 未与实验数据系统验证 | 未将模拟系综与NMR、SAXS、FRET等实验数据对比 | 模拟力场偏差可能系统性地影响所有轨迹 | 选取若干体系与实验系综数据对比RMSF、Rg分布 | 全文未提及实验验证 |
| 缺口补齐依赖AlphaFold3 | 对长缺口（>5残基）使用AF3预测，可能引入预测偏差 | AF3预测的构象可能不代表天然构象，影响后续模拟 | 对比AF3补齐区域在模拟中的构象与实验结构 | Methods "Protocol for proteins" |
| 数据筛选偏向稳定复合物 | PDBbind本身偏向可结晶的稳定复合物，动态/弱结合复合物代表性不足 | 弱相互作用（如相分离相关互作）在该数据集中可能系统性缺失 | 分析数据集中结合亲和力分布 | Methods "Data selection" |
| 未报告用户使用案例 | 未展示任何基于DynaRepo数据训练的模型或下游分析 | 数据库的实际效用未经验证 | 等待后续引用或使用案例 | 全文未提及 |

---

## 14 学到什么

> Agent 提炼的知识候选

1. **标准化MD协议的可迁移性**：DynaRepo的「统一力场+统一时长+统一分析」模式可直接迁移到IDP/IDR MD数据集的构建。对无序蛋白，建议采用CHARMM36m（对IDP有较好表现）并增加重复次数以增强系综采样。

2. **预计算分析降低AI训练门槛**：将RMSF、PCA、氢键等预计算结果与原始轨迹一同发布，可显著降低动力学感知模型的特征工程成本。对IDP/相分离研究，建议额外预计算：链内接触图、Rg时间序列、残基级溶剂可及性、凝聚体形成相关序参数。

3. **数据筛选策略的借鉴与修正**：DynaRepo的MM-score聚类去冗余策略可迁移到IDP数据集构建，但需注意IDP的构象异质性使得单一结构聚类不充分——建议基于MD系综而非单一结构进行去冗余。

4. **IDP/IDR数据空白即机会**：作者明确排除IDP/IDR体系，说明该方向缺乏大规模MD数据。这提示：构建IDP/IDR专用MD数据库（类似DynaRepo但针对无序蛋白）是推动该领域AI方法发展的关键瓶颈。

5. **动力学感知AI的可行性验证**：DynamicGT等模型已在DynaRepo数据上展示改进，说明「MD轨迹→AI模型」的技术路线可行。对IDP/相分离，可类比开发「构象系综→相分离预测」的模型。

6. **API+联邦架构的生态价值**：DynaRepo作为MDDB节点，通过标准化API实现跨库互操作。对IDP/IDR数据库建设，建议从一开始就采用类似架构，避免数据孤岛。

---

## 15 与已有知识连接

1. **AlphaFold2/3 [1,2]**：DynaRepo使用AF3进行缺口补齐，同时其存在本身回应了AF系列「静态结构预测」的局限——动力学数据是下一代模型的关键。对IDP/相分离，AF3对无序区域预测置信度低，MD数据可补充这一空白。

2. **DynamicGT [16]**：作者团队此前工作，利用MD轨迹训练动力学感知的结合位点预测模型。DynaRepo是其数据基础。该技术路线可迁移到IDP介导的互作位点预测。

3. **Boltz-2 [17]**：基于MD数据训练的结合亲和力预测模型。对IDP/相分离，类似方法可用于预测IDP介导的弱相互作用亲和力。

4. **BioEmu [18]**：基于MD数据训练的构象集合生成模型。对IDP研究，此类方法可用于从序列直接生成无序蛋白构象系综。

5. **MDDB联盟**：欧洲分布式MD数据库倡议，DynaRepo是其法国节点。该联盟的标准化协议（MDPosit、OPTIMADE接口）可作为IDP/IDR MD数据共享的参考架构。

6. **PDBbind [19]**：经典蛋白-配体结合数据库，DynaRepo从中筛选蛋白-蛋白复合物。对IDP/相分离，类似可构建「IDP-伴侣」结合数据库。

7. **SAbDab [20]**：抗体结构数据库，DynaRepo的抗原来源。抗体-抗原识别中的CDR环区动态与IDP的「folding-upon-binding」机制有相似性，可交叉借鉴。

8. **MDpocket [51]**：口袋检测工具，DynaRepo用于预计算。对IDP/相分离，可类比开发「动态口袋/结合热点」检测工具，识别IDP上的瞬时结合位点。

9. **无序蛋白数据库（如DisProt、IDEAL）**：与DynaRepo互补——前者提供无序注释，后者提供动态轨迹。两者结合可构建「无序蛋白动态图谱」。

10. **相分离数据库（如LLPSDB、PhaSepDB）**：DynaRepo目前不含相分离相关体系，但核小体模拟（含翻译后修饰）与染色质相分离研究直接相关，可作为连接点。

---

## 16 研究想法

> Agent 生成的研究候选

**候选1：IDP-DynaRepo——面向内在无序蛋白/无序区的MD轨迹数据库**
- **来源局限/观察**：DynaRepo明确排除了IDP/IDR体系，导致该方向缺乏大规模标准化MD数据
- **核心假设**：针对IDP/IDR的MD数据库（含游离态与结合态）可显著提升无序蛋白互作位点预测和相分离倾向预测的准确性
- **初步方法**：从DisProt/IDEAL收集IDP/IDR序列，对游离态和结合态分别进行3×500 ns MD模拟（CHARMM36m），预计算Rg、RMSF、链内接触图、瞬时二级结构等IDP相关特征，采用DynaRepo的MDPosit+API架构发布
- **验证方式**：训练IDP结合位点预测模型，与基于静态结构的基线（如AlphaFold置信度特征）对比
- **创新状态**：unverified

**候选2：基于MD轨迹的相分离驱动残基识别**
- **来源局限/观察**：DynaRepo提供残基级RMSF、氢键、能量等预计算数据，但未针对相分离相关特征（如多价弱相互作用、疏水补丁动态暴露）进行专门分析
- **核心假设**：MD轨迹中的残基级动态特征（RMSF、溶剂可及性波动、瞬时接触网络）可预测相分离驱动残基（π-π、阳离子-π、疏水相互作用热点）
- **初步方法**：利用DynaRepo中蛋白-蛋白复合物轨迹，计算界面残基的动态特征；与已知相分离蛋白（FUS、TDP-43等）的驱动残基注释对比；训练分类器识别「相分离驱动残基」特征模式
- **验证方式**：在已知相分离蛋白上交叉验证，并通过突变模拟（in silico mutagenesis）验证预测残基对凝聚倾向的影响
- **创新状态**：unverified

**候选3：动态感知的IDP-伴侣结合位点预测模型**
- **来源局限/观察**：DynaRepo数据可用于训练结合位点预测模型（如DynamicGT），但IDP-伴侣互作具有「folding-upon-binding」特性，与稳定复合物不同
- **核心假设**：IDP在结合伴侣前的构象系综（而非单一静态结构）包含结合位点信息，MD轨迹可捕获这些瞬时结合模式
- **初步方法**：对IDP-伴侣复合物进行MD模拟，提取IDP在游离态和结合态的构象系综；训练几何深度学习模型，输入为IDP构象系综（而非单一结构），输出为结合位点概率
- **验证方式**：在已知IDP-伴侣复合物benchmark上测试，与AlphaFold3、DynamicGT对比
- **创新状态**：unverified

**候选4：核小体翻译后修饰对染色质动态的MD-深度学习联合分析**
- **来源局限/观察**：DynaRepo包含7个核小体变体（含不同翻译后修饰），但未深入分析修饰对核小体动态的影响
- **核心假设**：组蛋白翻译后修饰（如乙酰化、磷酸化）通过改变核小体动态（而非静态结构）调控染色质可及性，MD轨迹可捕获这些动态差异
- **初步方法**：利用DynaRepo核小体轨迹，比较不同修饰状态的RMSF、接触图、DNA-组蛋白相互作用能量差异；训练图神经网络预测修饰状态对核小体动态的影响
- **验证方式**：与实验数据（MNase-seq、ATAC-seq）对比，验证预测的动态差异与染色质可及性相关性
- **创新状态**：unverified

**候选5：MD轨迹增强的蛋白-核酸结合亲和力预测**
- **来源局限/观察**：DynaRepo包含蛋白-DNA复合物（核小体），但蛋白-RNA复合物数据缺失；现有亲和力预测模型（如Boltz-2）主要基于静态结构
- **核心假设**：MD轨迹中的界面动态特征（界面残基RMSF、氢键占有率、水介导相互作用）可提升蛋白-核酸结合亲和力预测精度
- **初步方法**：对已知蛋白-RNA复合物进行MD模拟，提取界面动态特征；将这些特征作为补充输入加入现有亲和力预测模型（如Boltz-2微调）
- **验证方式**：在蛋白-RNA结合亲和力benchmark（如Protein-RNA Interface Database）上测试
- **创新状态**：unverified