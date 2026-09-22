## 01 基本信息
- **标题**：Integrative Structural Modeling of Intrinsically Disordered Regions in a Human HDAC2 Chromatin Remodeling Complex
- **作者与单位**：Nde, Jules; Kempf, Cassandra G; Zimmermann, Rosalyn C; Cesare, Joseph; Zhang, Ying; Workman, Jerry L; Florens, Laurence; Washburn, Michael P（Stowers Institute for Medical Research，美国）
- **期刊/预印本平台**：bioRxiv (the preprint server for biology)
- **年份**：2026-04-03（预印本发布；原提交于2025-08-08）
- **论文类型**：预印本（研究论文）
- **领域**：结构生物学、蛋白质互作、无序蛋白、染色质重塑
- **关键词**：IDR/IDP、整合结构建模（ISM）、XL-MS、AlphaFold、HDAC2、MIER1、MHAP1/C16orf87
- **DOI/arXiv 号**：10.1101/2025.08.08.669391
- **代码**：未提供
- **数据**：质谱数据已存入 PeptideAtlas 和 MassIVE 数据库（具体标识符见原文 Table S5）
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文是「IDP/IDR × 蛋白互作 × AI/物理模拟」交叉方向的典型案例——直接针对含高比例IDR的HDAC2染色质重塑复合物，系统比较了AlphaFold单独预测与整合结构建模（AlphaFold + I-TASSER + HADDOCK + XL-MS约束）的差异，展示了AI方法在IDR体系中的局限及整合策略的补充价值。

## 02 一句话总结
本文通过结合XL-MS实验距离约束与I-TASSER、HADDOCK、AlphaFold等计算工具，构建了HDAC2:MIER1:MHAP1三聚体复合物的整合结构模型，发现HDAC2的C端无序结构域折叠为α-螺旋并与MIER1 ELM2结构域及MHAP1互作，而单独使用AlphaFold无法预测这些IDR介导的相互作用。

## 03 研究问题
- **具体问题**：HDAC2、MIER1和MHAP1（C16orf87）三者均含大量IDR，它们如何组装形成功能性三聚体复合物？IDR在此组装中扮演什么结构角色？
- **为什么重要**：IDR/IDP在信号传导、转录调控等过程中广泛参与蛋白互作，但传统结构生物学方法和AlphaFold均难以解析其结构。HDAC2是表观遗传调控核心酶，理解其IDR介导的复合物组装对揭示染色质重塑机制至关重要。
- **现有方法为何不足**：X射线晶体学和冷冻电镜倾向于排除或无法解析柔性IDR区域；AlphaFold对IDR的预测置信度极低（pLDDT低），且无法准确预测IDR介导的互作界面。
- **精确研究问题**：Can an integrative approach combining XL-MS distance restraints with computational modeling (I-TASSER, HADDOCK, AlphaFold) produce a structurally and biologically valid model of an IDR-rich ternary complex (HDAC2:MIER1:MHAP1) that AlphaFold alone cannot achieve?

## 04 背景与发展脉络
- **阶段一：传统结构生物学方法（X射线晶体学、NMR、冷冻电镜）**
  - 优点：高分辨率、原子级细节
  - 局限：IDR柔性导致难以结晶、NMR分子量限制、冷冻电镜常需删除柔性区域
  - 代表：HDAC2已有40个实验结构，但均不含C端IDR（最后~100个氨基酸）
- **阶段二：AlphaFold及深度学习预测方法**
  - 优点：对有序结构域预测精度高
  - 局限：对IDR预测置信度低，无法捕捉IDR折叠状态和互作界面；对复合物中IDR介导的互作预测不可靠
  - 代表：AlphaFold2/3、AlphaFold-Multimer
- **阶段三：整合结构建模（ISM）**
  - 优点：可融合多种实验约束（XL-MS、交联、SAXS等）与计算预测，捕捉动态构象
  - 局限：依赖实验数据质量，计算成本较高
  - 代表：I-TASSER + HADDOCK + XL-MS工作流
- **本文主张的位置**：本文处于阶段二向阶段三过渡的关键节点——系统展示了AlphaFold在IDR复合物中的失败模式，并证明整合方法可弥补这一缺陷。
- **脉络核验状态**：仅本文框架（作者在Introduction和Discussion中提供的文献脉络，未做外部系统核验）。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| AlphaFold无法预测IDR结构 | HDAC2 C端结构域（His376-Pro488）在AF模型中为无结构长环，pLDDT极低 | AlphaFold基于MSA训练，IDR缺乏进化约束 | Results "Comparison" 节、Fig. 4A-C |
| AlphaFold无法预测IDR介导的互作 | AF三聚体模型中，HDAC2 C端IDR与MIER1/MHAP1无接触；MIER1和MHAP1的IDR区域"flopping around" | AlphaFold倾向于将IDR建模为孤立无结构区域，无法捕捉诱导折叠 | Results "AlphaFold-Generated" 节、Fig. 2B-D |
| 实验结构中IDR缺失 | 40个已解析HDAC2结构均不含C端IDR | 为获得晶体或冷冻电镜样品，IDR常被删除或无法解析 | Discussion 节 |
| IDR在复合物中的功能角色不明 | MHAP1和MIER1的IDR在复合物组装中的作用此前未知 | 缺乏实验约束和结构信息 | Results "Integrative" 节 |
| 传统方法无法捕捉IDR折叠转变 | IDR从无结构到α-螺旋的转变需要实验约束引导 | IDR构象高度动态，单一方法无法捕捉 | Discussion 节 |

## 06 核心思想
1. **表面方法**：结合XL-MS实验交联数据与多种计算工具（I-TASSER、HADDOCK、AlphaFold），通过迭代优化构建三聚体复合物的整合结构模型。
2. **核心洞察**：IDR并非"无结构"的被动连接片段，而是通过折叠为α-螺旋（如HDAC2 C端结构域折叠为6个短螺旋）主动参与蛋白互作。AlphaFold的失败源于其训练数据中缺乏IDR折叠信息，而XL-MS提供的距离约束可有效引导IDR的构象预测。
3. **可能的普适教训** [Analysis]：对于IDR/IDP介导的蛋白互作体系，单一AI预测方法（如AlphaFold）存在系统性盲区；整合实验约束（尤其是交联数据）与多尺度计算建模是解析此类体系结构的必要路径。这一教训可推广至其他IDR-rich复合物研究。

## 07 方法总览
- **输入**：HDAC2、MIER1、MHAP1的氨基酸序列（UniProt）；XL-MS交联数据（DSSO交联剂）；PDB参考结构（HDAC2使用3ZZO）
- **输出**：三聚体复合物的整合结构模型（含各亚基完整结构，包括IDR区域）
- **模块**：
  1. **实验模块**：Halo标签亲和纯化、XL-MS（DSSO交联）、AP-MS、AP-FRET、去乙酰化酶活性测定
  2. **计算模块**：AlphaFold3/AF-Multimer预测复合物结构；I-TASSER单蛋白结构预测（含XL约束）；HADDOCK分子对接（CPORT预测活性残基）
  3. **验证模块**：XL得分（满足交联约束的数量）、接触图分析、赖氨酸距离热图、与实验结构比对
- **训练**：不适用（无新模型训练，使用已有工具）
- **反馈回路**：XL-MS距离约束 → I-TASSER结构预测 → 距离测量/XL得分评估 → 满足约束的模型输入HADDOCK → 对接后再次验证
- **文字流程**：首先通过AP-MS和共定位实验确认MHAP1与HDAC1/2、MIER1的互作关系；然后对纯化复合物进行XL-MS获得交联距离约束；使用AlphaFold3和AF-Multimer预测二聚体和三聚体结构作为基线；使用I-TASSER（含XL约束）预测各蛋白单体结构；通过HADDOCK（CPORT引导）进行分子对接组装三聚体；最终通过接触图、距离热图和XL得分评估模型质量，并与AlphaFold模型对比。

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| XL-MS交联实验 | 提供蛋白间和蛋白内赖氨酸残基的距离约束（≤37 Å Cα-Cα） | 为IDR构象预测提供实验锚点 | 输入：纯化复合物；输出：交联肽段列表及距离约束 | Results "Integrative" 节、Table S3 | 移除后无法引导IDR折叠预测，ISM模型将退化为无约束的对接结果 |
| AlphaFold3/AF-Multimer | 预测二聚体和三聚体复合物结构 | 提供基线模型，展示AI方法在IDR体系中的表现 | 输入：氨基酸序列；输出：复合物结构模型及pLDDT | Results "AlphaFold-Generated" 节、Fig. 2 | 移除后失去对比基线，无法量化整合方法的增益 |
| I-TASSER（含XL约束） | 单蛋白结构预测，整合交联距离约束 | 对IDR-rich蛋白进行de novo预测，XL约束改善IDR折叠 | 输入：序列+XL约束；输出：各亚基结构模型 | Methods "Protein Structure Prediction" 节、Fig. S3A | 移除后IDR区域将保持无结构状态，无法形成α-螺旋 |
| HADDOCK分子对接 | 组装三聚体复合物 | 基于预测的单体结构进行多体组装 | 输入：I-TASSER模型+CPORT活性残基；输出：复合物模型簇 | Methods "Protein Docking" 节、Fig. 3B-C | 移除后无法获得三聚体组装模型 |
| CPORT | 预测蛋白互作界面的活性残基 | 引导HADDOCK对接方向 | 输入：蛋白结构；输出：活性/被动残基列表 | Methods "Protein Docking" 节 | 移除后对接将缺乏导向，可能产生错误组装 |
| 接触图/距离热图分析 | 可视化亚基间互作界面 | 评估模型质量、比较AF与ISM模型差异 | 输入：结构模型；输出：接触图、赖氨酸距离热图 | Results "Comparison" 节、Fig. 2C-D、Fig. S4 | 移除后无法系统比较模型差异 |

**消融效应区分**：作者未进行系统性消融实验（如移除XL约束后重新建模），因此上述"移除后影响"多为预期效应 [Analysis]，而非实测消融结果。

## 09 关键公式符号
- **XL得分（XL Score）**：统计满足距离阈值的交联约束数量。文中使用Cα-Cα距离≤37 Å作为DSSO交联的满足标准（依据参考文献25）。公式未明确给出，但逻辑为：XL Score = 满足约束的交联对数 / 总交联对数。
- **FRET效率**：E_FRET = 1 − (I_prebleach / I_postbleach) × 100%，其中I为供体通道荧光强度（Methods "Acceptor Photobleaching" 节）。
- **欧几里得距离（Euclidean Distance, ED）**：用于测量交联赖氨酸Cα原子间的三维空间距离，在Chimera中计算。
- **溶剂可及表面积距离（Solvent Accessible Surface Distance, SASD）**：在xWalk中计算的替代距离度量，用于交叉验证ED结果。
- **pLDDT（predicted Local Distance Difference Test）**：AlphaFold输出的每个残基的预测置信度分数，范围0-100，文中用于识别低置信度IDR区域。

## 10 实验设计与证据链
- **数据集/群体**：HEK293T细胞（瞬时转染和Flp-In稳定细胞系）；HeLa细胞（早期AP-MS筛选）
- **规模**：53次MudPIT质谱运行；3次生物学重复XL-MS（HDAC1-Halo和HDAC2-Halo各3次）
- **指标**：dNSAF（定量质谱）、log2FC > 2且FDR < 0.05（互作筛选）、XL得分、FRET效率、去乙酰化酶活性
- **基线/对照**：Halo标签单独表达（阴性对照）；AlphaFold模型作为计算基线
- **预算/资源**：未提供具体预算信息
- **骨干/仪器**：LTQ线性离子阱质谱仪（MudPIT）；Orbitrap Fusion Lumos（XL-MS）；UltraVIEW VoX转盘共聚焦显微镜（FRET）
- **oracle输入**：XL-MS交联距离约束作为结构预测的"oracle"信息
- **评测协议**：XL得分评估模型满足实验约束的程度；接触图比较AF与ISM模型的互作界面差异；与实验解析的HDAC2结构（3ZZO）比对验证HDAC结构域准确性

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|------------|----------------|------|
| AP-MS（Halo-MHAP1为诱饵） | MHAP1与HDAC1/2及MIER家族成员互作 | 与Halo标签对照比较 | MHAP1富集HDAC1/2、MIER1/3 | MHAP1是MIER复合物成员 | 不能确定直接vs间接互作 | Results 节、Fig. 1B、Table S1 |
| 共定位/AP-FRET | MHAP1与HDAC1/2在细胞内直接互作 | FRET效率与阴性对照比较 | 显著FRET信号 | MHAP1与HDAC1/2距离<10 nm | 不能确定具体互作界面 | Results 节、Fig. 1C |
| 去乙酰化酶活性测定 | MHAP1相关复合物具有HDAC活性 | 有无SAHA抑制剂对比 | 活性可被SAHA抑制 | 复合物含活性HDAC | 不能确定MHAP1是否直接调控活性 | Results 节、Fig. 1D |
| AlphaFold预测二聚体/三聚体 | AF能否准确预测IDR-rich复合物结构 | AF3 vs AFM；二聚体 vs 三聚体 | IDR区域pLDDT极低，C端结构域无结构 | AF无法捕捉IDR折叠和互作 | 不能排除AF在其他IDR体系中的有效性 | Results "AlphaFold-Generated" 节、Fig. 2 |
| ISM建模（I-TASSER + XL约束 + HADDOCK） | 整合方法能否产生更完整的复合物模型 | ISM模型 vs AF模型 | ISM模型包含完整IDR折叠为α-螺旋，满足XL约束 | 整合方法优于AF单独预测 | 模型未经实验验证（如突变验证） | Results "Integrative" 节、Fig. 3 |
| 接触图/距离热图比较 | AF与ISM模型的互作界面差异 | AF vs ISM接触图 | ISM显示HDAC2 C端IDR与MIER1 ELMH2/MHAP1互作 | IDR介导的互作在ISM中被捕捉 | 接触图基于模型而非实验 | Results "Comparison" 节、Fig. 4 |

## 11 结论正确解读
- **任务范围**：本文仅针对HDAC2:MIER1:MHAP1这一个三聚体复合物，不能推广至所有IDR体系。
- **oracle/真值输入**：XL-MS交联约束是模型构建的核心实验输入，模型质量高度依赖交联数据质量。
- **端到端状态**：本文并非端到端自动流程——需要人工选择模型、评估XL得分、迭代优化。
- **算力成本**：未报告具体算力消耗。
- **历史数据依赖**：AlphaFold预测依赖MSA数据库；I-TASSER依赖PDB结构模板。
- **模型依赖**：结果依赖AlphaFold3/AFM、I-TASSER、HADDOCK的具体版本和参数设置。
- **最难情形**：IDR-rich蛋白复合物，尤其是IDR介导的互作界面。
- **群体/领域边界**：结论限于HDAC2相关复合物；对其他IDP体系需独立验证。
- **不确定性**：ISM模型未经突变实验或高分辨率结构验证，模型精度未知。
- **有边界的复述**：本文证明，在HDAC2:MIER1:MHAP1体系中，结合XL-MS约束的整合建模可产生比AlphaFold单独预测更完整、更符合实验数据的结构模型，特别是捕捉了HDAC2 C端IDR折叠为α-螺旋并介导互作这一关键特征。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| AlphaFold对IDR预测的固有局限 | AF模型无法预测IDR折叠和互作 | 需开发专门针对IDR的预测方法 | Discussion 节 |
| 模型未经高分辨率实验验证 | ISM模型为计算预测，缺乏晶体或冷冻电镜结构确认 | 未来可通过冷冻电镜或NMR验证 | Discussion 节 |
| XL-MS覆盖度有限 | 仅检测赖氨酸交联，未覆盖所有互作残基 | 结合其他交联剂或互补技术 | Discussion 节 |
| MHAP1功能未知 | MHAP1是新命名的蛋白，其生物学功能尚待阐明 | 需要功能实验（如敲除/敲低） | Discussion 节 |
| 单一复合物体系 | 结论基于HDAC2:MIER1:MHAP1一个体系 | 需在更多IDR复合物中验证整合方法 | Discussion 节 |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|---------------------|----------|----------|------|
| ISM模型将IDR折叠为α-螺旋，但缺乏独立验证 | 可能是计算伪影而非真实构象；IDR在溶液中可能保持多种构象 | 模型的核心创新点若不可靠，则整个方法的价值存疑 | 通过圆二色谱、NMR或分子动力学模拟验证IDR螺旋倾向 | Results "Integrative" 节 |
| XL-MS交联数据量有限（仅4个MHAP1赖氨酸被交联） | 约束稀疏可能导致模型过度拟合或欠约束 | 模型质量取决于约束密度 | 增加生物学重复或使用多种交联剂 | Results 节、Table S3 |
| AlphaFold与ISM模型的比较可能不公平 | AF使用默认设置，未尝试优化或使用AF3更新版本 | 可能低估AF在IDR体系中的表现 | 使用多种AF配置和版本进行系统比较 | Methods "AlphaFold" 节 |
| MHAP1的命名和功能推断基于有限的互作数据 | 可能只是共纯化而非直接互作 | 功能注释影响后续实验设计 | 进行体外直接互作实验（如ITC、SPR） | Results 节 |
| 未报告模型评估的定量指标（如RMSD、MolProbity分数） | 无法客观评估模型质量 | 模型质量评估是结构生物学的基本要求 | 补充模型质量指标 | Results "Integrative" 节 |
| 整合方法的工作流程依赖多步骤人工干预 | 可重复性和自动化程度存疑 | 方法推广需要标准化流程 | 提供完整流程代码和参数设置 | Methods 节 |

## 14 Agent 提炼的知识候选
1. **XL-MS约束引导IDR折叠预测**：本文展示了将交联距离约束（≤37 Å Cα-Cα）整合到I-TASSER预测流程中，可显著改善IDR区域的折叠预测。**可迁移至本课题**：对IDP/IDR介导的互作体系，可设计XL-MS实验获取距离约束，用于引导AlphaFold或I-TASSER的IDR构象预测。
2. **AlphaFold在IDR体系中的系统性失败模式**：AF对IDR-rich蛋白的预测存在"无结构长环"偏差，且无法预测IDR介导的互作界面。**可迁移至本课题**：在使用AlphaFold预测IDP/IDR相关复合物时，应警惕其低置信度区域，并考虑补充实验约束。
3. **"折叠-结合"（folding-upon-binding）机制的结构证据**：本文ISM模型显示HDAC2 C端IDR折叠为6个α-螺旋并与MIER1 ELM2结构域互作，为IDR介导的诱导折叠提供了结构模型。**可迁移至本课题**：在研究IDP/IDR介导的相分离或互作时，可关注IDR是否通过折叠为特定二级结构来驱动互作。
4. **多工具整合工作流**：AlphaFold（初始预测）→ I-TASSER（含约束优化）→ HADDOCK（对接组装）→ XL得分评估的流程，为IDR复合物建模提供了可复用的框架。**可迁移至本课题**：可建立类似的整合流程用于其他IDP/IDR复合物或凝聚体体系。
5. **接触图和赖氨酸距离热图作为模型比较工具**：通过2D接触图和赖氨酸距离热图系统比较不同模型的互作界面差异。**可迁移至本课题**：在比较不同预测方法或不同实验条件下的IDR构象时，可借鉴这种可视化比较策略。
6. **IDR在复合物中的"支架"角色**：MHAP1虽小且高度无序，但通过其IDR和SAH结构域在复合物中发挥结构支撑作用。**可迁移至本课题**：在相分离体系中，小分子量IDP可能通过类似机制作为"支架"分子驱动凝聚体形成。

## 15 与已有知识连接
- **相似工作**：作者引用了此前对HDAC1/2复合物的XL-MS研究（参考文献16,17,25），以及RCOR1 ELM2结构域与HDAC1 C端互作的研究（参考文献35）。这些工作共同构成了HDAC复合物中IDR介导互作的证据链。
- **方法学连接**：整合结构建模（ISM）方法可追溯至Sali实验室的Integrative Modeling Platform（IMP）框架（参考文献40-42），本文是该框架在IDR-rich复合物中的具体应用。
- **AlphaFold局限性的已知讨论**：已有文献系统评估了AlphaFold对IDR预测的局限性（如pLDDT与无序程度的关联），本文提供了具体案例支持。
- **IDR折叠-结合机制**：本文观察到的IDR折叠为α-螺旋的现象与已知的MoRF（Molecular Recognition Feature）概念一致——短线性基序在结合时折叠为二级结构。
- **与相分离的潜在连接** [Analysis]：HDAC2 C端IDR折叠为α-螺旋并介导多价互作的特征，与相分离中多价IDR互作驱动凝聚体形成的机制有相似性。本文虽未研究相分离，但其结构模型可为理解IDR介导的凝聚体形成提供参考。
- **冲突或补充** [Analysis]：本文结果与"IDR完全无结构"的传统观点形成对比，支持IDR在结合伙伴存在时可诱导折叠的观点。这与NMR研究显示的IDR构象多样性并不矛盾，而是强调了环境依赖的折叠行为。

## 16 研究想法
1. **候选名称**：IDR介导的HDAC2复合物相分离行为研究
   - **来源局限/观察**：本文ISM模型显示HDAC2 C端IDR折叠为α-螺旋并介导多价互作，但未研究该复合物是否形成相分离凝聚体。
   - **核心假设**：HDAC2:MIER1:MHAP1复合物通过IDR介导的多价互作在特定条件下形成相分离凝聚体，且该过程受HDAC2 C端IDR的螺旋折叠调控。
   - **初步方法**：体外纯化重组蛋白，使用共聚焦显微镜和浊度实验检测相分离；突变HDAC2 C端IDR关键残基（破坏螺旋形成）观察对相分离的影响；结合本文ISM模型设计突变位点。
   - **验证方式**：FRAP实验验证凝聚体动态性；突变体对比实验验证IDR螺旋的关键作用。
   - **可能的失败模式**：该复合物可能不形成相分离凝聚体，或相分离由其他结构域驱动而非IDR。
   - **创新状态**：unverified

2. **候选名称**：AlphaFold-IDR约束微调策略（AF-IDR-FT）
   - **来源局限/观察**：本文展示了AlphaFold在IDR预测中的系统性失败，但未尝试改进AlphaFold本身。
   - **核心假设**：通过在AlphaFold训练或微调阶段引入XL-MS距离约束作为辅助损失，可提升其对IDR-rich复合物的预测能力。
   - **初步方法**：收集包含XL-MS数据的IDR复合物数据集；在AlphaFold架构基础上增加距离约束损失项；微调模型并评估IDR区域预测精度。
   - **验证方式**：在本文HDAC2:MIER1:MHAP1体系及独立测试集上比较微调前后模型的IDR预测精度和互作界面预测能力。
   - **可能的失败模式**：XL-MS数据稀疏且噪声大，可能不足以驱动模型改进；IDR的构象多样性可能超出监督学习可捕捉的范围。
   - **创新状态**：unverified

3. **候选名称**：IDR介导互作的分子动力学（MD）模拟验证
   - **来源局限/观察**：本文ISM模型为静态结构，未探索IDR构象动态和结合路径。
   - **核心假设**：HDAC2 C端IDR与MIER1 ELM2结构域的结合遵循"构象选择+诱导折叠"混合机制，MD模拟可揭示结合路径和中间态。
   - **初步方法**：以ISM模型为起点，使用粗粒化MD（如MARTINI）或增强采样方法（如REMD）模拟IDR结合过程；分析结合自由能面和关键中间态。
   - **验证方式**：模拟预测的结合关键残基与XL-MS数据交叉验证；突变模拟预测结合亲和力变化。
   - **可能的失败模式**：IDR体系采样困难，模拟时间尺度不足；力场对IDR的描述可能不准确。
   - **创新状态**：unverified

4. **候选名称**：基于图神经网络的IDR互作界面预测器（IDR-InterfaceGNN）
   - **来源局限/观察**：本文依赖实验XL-MS获取距离约束，成本高且耗时；需要计算方法来预测IDR互作界面。
   - **核心假设**：图神经网络可学习IDR序列特征与互作界面的关联，在无实验数据条件下预测IDR介导的互作热点。
   - **初步方法**：收集已知IDR互作数据（如来自XL-MS、NMR、突变实验）；构建以IDR序列和预测结构为输入的图神经网络；训练分类器预测互作残基。
   - **验证方式**：在本文HDAC2:MIER1:MHAP1体系上测试预测精度；与AlphaFold和随机基线比较。
   - **可能的失败模式**：IDR互作数据稀缺，训练数据不足；IDR互作的序列-结构关系可能过于复杂。
   - **创新状态**：unverified

5. **候选名称**：IDR折叠-结合与相分离的序列决定因素分析
   - **来源局限/观察**：本文发现HDAC2 C端IDR折叠为α-螺旋，MHAP1含SAH结构域，但未系统分析何种序列特征决定IDR的折叠倾向。
   - **核心假设**：IDR中螺旋倾向性残基（如谷氨酸、赖氨酸、丙氨酸）的周期性分布决定其折叠-结合能力，进而影响相分离行为。
   - **初步方法**：对本文三个蛋白的IDR进行序列分析（如使用IUPred、PONDR、AGGRESCAN）；比较折叠区与非折叠区的序列特征；在已知相分离蛋白数据库中验证序列特征与相分离能力的关联。
   - **验证方式**：设计嵌合蛋白（替换IDR序列）检测折叠和互作能力变化；统计分析序列特征与实验相分离数据的相关性。
   - **可能的失败模式**：序列特征与折叠能力的关联可能被其他因素（如翻译后修饰）掩盖；体外实验与体内行为可能不一致。
   - **创新状态**：unverified