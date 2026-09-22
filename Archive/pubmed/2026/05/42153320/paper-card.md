## 01 基本信息
- **标题**：MuFGPS: enhancing liquid–liquid phase separation protein prediction through multi-level features and ensemble learning
- **作者**：Xian, Lei; Zou, Quan; Qi, Ren; Niu, Mengting; Wang, Yansu
- **单位**：未提供（据作者贡献声明，涉及电子科技大学长三角研究院（衢州））
- **期刊/平台**：Briefings in Bioinformatics
- **年份**：2026（在线日期 2026-05-19）
- **论文类型**：方法学/预测模型开发
- **领域**：液-液相分离（LLPS）蛋白预测；生物信息学；机器学习
- **关键词**：liquid–liquid phase separation; protein prediction; graph attention network; ensemble learning; AlphaFold
- **DOI/ID**：10.1093/bib/bbag235
- **代码**：https://github.com/keepactivedayday/MuFGPS/tree/main
- **数据**：LLPSDB、PhaSepDB、PhaSePro、DrLLPS（正样本来源）；负样本从10个代表性物种中随机选取
- **阅读日期**：2026-06-02
- **在课题方向中的位置**：本文属于「IDP/IDR介导的相分离 × AI预测」方向，核心贡献是将AlphaFold预测结构转化为图表示（接触图+图注意力网络），与序列特征、二级结构特征融合，通过集成学习提升LLPS蛋白预测性能。对IDR/IDP课题的可迁移点在于：展示了如何将结构信息（即使对无序蛋白预测结构有不确定性）纳入预测框架，以及多层级特征融合+集成策略的通用性。

## 02 一句话总结
MuFGPS通过融合序列理化特征、DSSP二级结构特征和基于AlphaFold接触图的图注意力网络嵌入，结合SMOTE过采样和Stacking集成学习（RF+XGBoost+LightGBM），在LLPS蛋白预测任务上优于六种现有方法，F1达0.8356、MCC达0.7749。

## 03 研究问题
- **具体问题**：如何准确预测蛋白质是否具有液-液相分离（LLPS）能力？
- **为什么重要**：LLPS驱动无膜细胞器组装，参与转录、DNA修复、信号转导等关键过程；其失调与神经退行性疾病（阿尔茨海默病、亨廷顿病）、癌症和病毒感染相关。准确识别LLPS蛋白对理解机制和开发治疗策略至关重要。
- **现有方法不足**：现有计算方法（如catGRANULE、PScore、DeePhase、FuzDrop、Seq2Phase、MambaPhase）主要依赖序列级描述符，未显式整合结构拓扑信息，难以捕捉LLPS行为的多价弱相互作用网络所依赖的空间组织与残基级拓扑。
- **精确研究问题**：Can integrating AlphaFold-derived structural topology (via graph attention networks) with sequence-level physicochemical features and secondary structure information improve LLPS protein prediction over sequence-only approaches?

## 04 背景与发展脉络
*注：以下脉络基于本文框架，未经外部核验。*
1. **早期序列特征方法**：PLAAC（prion-like domain检测）、catGRANULE（整合无序倾向、RNA结合能力、RGG基序的加权评分）、PScore（π-π相互作用频率）——依赖特定基序或单一相互作用类型，覆盖机制有限。
2. **机器学习/深度学习方法**：DeePhase（序列理化特征+深度学习）、Seq2Phase（预训练蛋白语言模型+深度神经网络）、MambaPhase（ESM+Mamba架构）——从序列中学习非线性模式，但未显式利用三维结构。
3. **结构感知方法（本文位置）**：利用AlphaFold预测结构，通过接触图构建图神经网络（GAT）提取结构嵌入，与序列特征和二级结构特征融合。主张：结构拓扑信息提供了超越序列的判别线索，且多层级特征+集成学习可进一步提升性能。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 序列特征难以捕捉结构拓扑 | 现有方法主要依赖序列描述符，预测性能受限 | LLPS由多价弱相互作用驱动，涉及残基空间排布与接触模式，序列线性信息不足以表征 | Introduction：现有方法"largely rely on sequence-level descriptors and often fail to explicitly incorporate structural topology information" |
| LLPS蛋白序列多样性高 | 正负样本在序列层面区分度有限 | LLPS能力由多种特征共同决定（无序性、电荷分布、疏水性、π-π相互作用等），单一或少数特征不够 | Results：15个特征均显示显著分布差异，但需多特征融合 |
| 类别不平衡 | 正样本（LLPS蛋白）远少于负样本 | 已注释的LLPS蛋白数量有限 | Methods：正样本366个，负样本1302个；引入SMOTE |
| 结构预测对无序蛋白有不确定性 | AlphaFold对IDR区域预测置信度可能较低 | 无序区域缺乏稳定三级结构 | 未直接讨论；[Analysis] 作者未在文中明确处理此问题，但通过接触图+图网络的方式可能部分缓解 |

## 06 核心思想
1. **表面方法**：多层级特征融合（序列理化特征 + DSSP二级结构特征 + GAT图嵌入）+ SMOTE过采样 + Stacking集成学习（RF/XGBoost/LightGBM + 逻辑回归元学习器）。
2. **核心洞察**：LLPS蛋白的判别信息分布在多个层级——序列组成（无序性、电荷、疏水性）、局部构象（二级结构倾向）、全局拓扑（残基接触模式）。单一层级特征不足以充分刻画LLPS的多价弱相互作用本质；结构拓扑信息（即使来自预测结构）提供了序列之外的互补判别信号。
3. **可能的普适教训** [Analysis]：对于IDP/IDR相关预测任务，即使目标蛋白区域缺乏稳定结构，将AlphaFold预测结构转化为图/接触表示仍可提取有用特征——因为相分离相关相互作用往往涉及局部的、瞬时的结构倾向（如短螺旋、β-turn），而非全局折叠。此外，多层级特征融合+集成策略可有效缓解单一特征/模型的偏差。

## 07 方法总览
- **输入**：蛋白质氨基酸序列
- **特征提取**：
  - 序列特征：无序倾向（ESpritz）、低复杂度区域（SEG）、电荷分布/模式（LocalCIDER）、prion-like domain（PLAAC）、π-π相互作用（PScore）、溶解度（Protein-sol）等15个特征
  - 二级结构特征：从AlphaFold PDB结构文件经DSSP注释，提取α-helix、β-sheet、β-turn比例
  - 图结构特征：基于AlphaFold PDB结构构建接触图（Cα距离<8Å定义边），节点初始特征为SeqVec嵌入（1024维），经3层多头GAT（前两层3头，第三层1头）提取128维图嵌入
- **类别平衡**：SMOTE过采样（仅在训练集内）
- **分类器**：Stacking集成——第一层RF、XGBoost、LightGBM，第二层逻辑回归
- **训练细节**：GAT先以对比学习（NT-Xent损失）自监督预训练（随机边丢弃p=0.2、节点特征掩蔽p=0.1；AdamW，lr=1e-3，weight decay=1e-4，200 epochs，dropout=0.5），然后冻结GAT参数生成图嵌入
- **输出**：二分类概率（LLPS vs 非LLPS）
- **流程**：序列 → 多层级特征提取 → 特征拼接 → SMOTE → Stacking集成分类 → 预测

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 序列特征提取（15个特征） | 捕获无序性、电荷、疏水性、π-π等序列层面LLPS驱动因素 | LLPS的序列决定因素已被广泛验证 | 输入：序列；输出：15维特征向量 | Results图2：多数特征在正负样本间显著差异（P<0.001） | 预期显著降低性能（尤其Recall）；[Analysis] 未单独消融，但No-Struct仍保留序列特征，性能下降23.2% MCC说明序列特征单独不够 |
| DSSP二级结构特征 | 提供局部构象倾向信息 | 二级结构倾向（如β-turn富集）与LLPS相关 | 输入：AlphaFold PDB文件；输出：α-helix/β-sheet/β-turn比例 | Results图2：α-helix含量显著降低，β-sheet/β-turn略增 | 消融实验（No-DSSP）：Recall降至0.730，MCC降至0.676（实测消融效应） |
| GAT图嵌入 | 提取残基接触拓扑的高阶结构表示 | 接触图编码空间邻近性，GAT可学习注意力加权的邻域聚合 | 输入：接触图+SeqVec节点特征；输出：128维图嵌入 | 消融实验（No-GAT）：Recall降至0.716，MCC降至0.673（实测消融效应） | 移除后性能下降，但略小于No-DSSP；两者联合移除（No-Struct）MCC降至0.595 |
| SMOTE过采样 | 缓解类别不平衡 | 正样本仅366个，负样本1302个 | 输入：训练集特征；输出：过采样后的平衡训练集 | Results图4：SMOTE后Recall从0.586提升至0.793，假阴性从12降至6 | 预期降低对正类的召回；[Analysis] 作者未报告移除SMOTE的完整消融 |
| Stacking集成（RF+XGB+LGBM→LR） | 融合多个异构模型的预测信号 | 不同树模型在特征空间中的决策边界互补 | 输入：三个基学习器的预测概率；输出：最终二分类概率 | 消融实验（No-Struct-No-Ensemble vs RF vs MLP vs Full）：Full模型MCC最高（0.775），优于单模型RF（0.698）和MLP（0.670）（实测消融效应） | 移除后MCC下降约10-14%相对值 |

## 09 关键公式符号
1. **接触图定义**：C = (c_ij)，L×L对称邻接矩阵；c_ij = 1 当 d(Cα_i, Cα_j) < 8Å，否则 c_ij = 0。其中L为序列长度，d为欧氏距离。
2. **GAT节点更新**：h_i^(l+1) = σ( Σ_{j∈N_i} α_ij^(k) W^(k) h_j^(l) )，其中N_i为节点i的邻居集，W^(k)∈R^(d×d')为第k个注意力头的可训练线性变换矩阵，α_ij^(k)为注意力权重（经LeakyReLU和softmax归一化），σ为激活函数。
3. **Stacking预测**：ŷ = σ(w^T [p_RF, p_XGB, p_LGBM] + b)，其中p_*为三个基学习器的预测概率，w和b为逻辑回归元学习器的权重和偏置，σ为sigmoid函数。
4. **NT-Xent对比损失**（GAT预训练）：最大化同一蛋白两个增强视图的图嵌入相似度，同时分离不同蛋白的嵌入（具体公式未在文中给出）。

## 10 实验设计与证据链
- **数据集**：
  - 正样本：366个LLPS蛋白（来自LLPSDB、PhaSepDB、PhaSePro、DrLLPS四个数据库，经CD-HIT去冗余，阈值0.8）
  - 负样本：1302个非LLPS蛋白（从10个代表性物种中随机选取，经相同预处理）
  - 额外测试集：29个正样本 + 124个负样本
- **指标**：Accuracy、Precision、Recall、F1-score、MCC、AUROC、AUPRC
- **基线**：catGRANULE、PScore、DeePhase、FuzDrop、Seq2Phase、MambaPhase（六种代表性方法）
- **评测协议**：交叉验证（fold-level），额外独立测试集验证；统计显著性用配对单侧Wilcoxon符号秩检验

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|------------|------------------|------|
| 特征分布分析 | 15个特征在正负样本间有显著差异 | Mann-Whitney U检验 | 多数特征P<0.001 | 所选特征具有判别力 | 单特征判别力有限，需多特征融合 | Results图2 |
| 与六种基线方法对比 | MuFGPS优于现有方法 | 同一基准数据集，5个指标 | Accuracy>91%，F1=0.8356，MCC=0.7749，全面最优 | MuFGPS在LLPS预测上优于现有方法 | 未报告各方法在独立测试集上的逐项数值对比 | Results表1 |
| SMOTE效果 | SMOTE提升正类召回 | 有/无SMOTE对比 | Recall从0.586→0.793，假阴性12→6 | SMOTE有效缓解类别不平衡 | 未报告AUROC/AUPRC的完整对比 | Results图4 |
| 消融-结构特征 | 结构特征贡献 | Full vs No-Struct vs No-DSSP vs No-GAT | No-Struct：MCC 0.775→0.595（-23.2%）；No-DSSP：Recall 0.824→0.730，MCC 0.775→0.676；No-GAT：Recall 0.824→0.716，MCC 0.775→0.673 | 结构特征（DSSP+GAT）贡献显著且互补 | 无法区分DSSP与GAT各自独立贡献的统计显著性 | Results图5A |
| 消融-集成策略 | Stacking优于单模型 | Full vs RF vs MLP vs No-Struct-No-Ensemble | Full MCC=0.775 > RF=0.698 > MLP=0.670 > No-Struct-No-Ensemble=0.562 | 结构特征与集成学习均有独立贡献 | 未报告各配置的完整指标矩阵 | Results图5C |
| 嵌入模型鲁棒性 | 框架不依赖特定PLM | SeqVec vs ProtBERT | MCC 0.775 vs 0.756，差异<3% | 框架对PLM选择不敏感 | 未报告其他PLM（如ESM-2） | Results图5B |

## 11 结论正确解读
- **任务范围**：二分类预测（LLPS vs 非LLPS），基于序列+AlphaFold预测结构。仅针对蛋白是否具有相分离能力，不预测相分离的驱动区域、条件或机制类型。
- **Oracle/真值输入**：正样本来自已注释数据库（实验验证或文献报道），负样本为"未报道相分离倾向"的蛋白——后者是弱标签，可能包含未发现的LLPS蛋白。
- **端到端状态**：非端到端。需要AlphaFold预测结构作为输入，GAT预训练后冻结，特征提取和分类是流水线式的。
- **算力成本**：GAT预训练需要GPU，但模型规模小（128维嵌入），推理成本低。未报告具体训练时间。
- **历史数据依赖**：训练数据来自截至构建时的数据库注释，新发现的LLPS蛋白可能改变决策边界。
- **模型依赖**：对PLM选择不敏感（SeqVec vs ProtBERT差异<3%），但未测试ESM-2等更现代模型。
- **最难情况**：序列特征不典型但结构拓扑关键的蛋白；高度无序、AlphaFold预测置信度低的蛋白。
- **群体/领域边界**：训练集以真核蛋白为主（10个物种），对原核生物或病毒蛋白的泛化能力未验证。
- **不确定性**：未报告置信度校准或预测不确定性的量化。
- **有边界的复述**：MuFGPS在包含366个正样本和1302个负样本的基准数据集上，通过融合序列、二级结构和AlphaFold接触图特征，以Stacking集成方式实现了优于六种现有方法的LLPS蛋白分类性能（Accuracy>91%，MCC=0.7749），但该性能边界受限于训练数据的注释质量、物种覆盖和AlphaFold预测结构的准确性。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据规模有限 | 正样本仅366个 | 在更大LLPS数据集可用时评估更严格的冗余阈值 | Discussion/Conclusion |
| 缺乏动态结构信息 | 仅使用静态AlphaFold预测结构 | 纳入动态结构或无序-结构转变特征 | Conclusion |
| 缺乏相互作用背景 | 未整合蛋白-RNA关联等相互作用上下文 | 整合相互作用背景信息（如蛋白-RNA关联） | Conclusion |
| 缺乏实验验证 | 预测结果未经湿实验验证 | 对高置信度预测进行实验验证 | Conclusion |

*注：作者在Conclusion中提及以上方向，但未以"limitation"形式系统列出。*

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 负样本为"未报道"而非"实验验证非LLPS" | 负样本可能包含未发现的LLPS蛋白，导致模型学习到有偏决策边界 | 影响模型泛化性和实际应用可靠性 | 用实验验证的非LLPS蛋白子集重新评估；或检查模型在已知假阴性上的行为 | Methods：负样本为"Proteins not recorded or reported to exhibit phase separation tendencies" |
| AlphaFold对IDR区域预测可靠性未讨论 | IDR是LLPS关键驱动区域，但AlphaFold对这些区域预测置信度低；接触图可能编码噪声而非真实生物学 | 若结构特征主要来自IDR区域的不可靠预测，则模型可能过拟合预测误差 | 按AlphaFold pLDDT分层分析特征贡献；比较仅用高置信度区域构建接触图的性能 | Introduction强调IDR重要性；Methods未提及pLDDT过滤 |
| 消融实验未报告统计显著性 | 图5显示数值差异，但未给出置信区间或显著性检验 | 无法判断DSSP与GAT贡献差异是否真实 | 重复多次交叉验证，报告均值±标准差及统计检验 | Results图5 |
| 与基线方法比较的公平性 | 基线方法（如catGRANULE、PScore）可能未经过重新训练或超参数调优 | 若基线未充分优化，性能优势可能被夸大 | 报告基线方法的调优细节；使用相同交叉验证划分 | Results表1，未提供基线调优细节 |
| 未报告独立测试集上的完整指标 | 仅提及额外测试集（29正/124负），但未给出该集上的详细结果 | 独立测试集是评估泛化能力的关键 | 补充独立测试集上的全部指标 | Methods：额外测试集描述；Results未报告其详细结果 |
| 未与其他结构感知方法比较 | 仅与序列方法比较，未与同样利用结构的预测器比较 | 无法判断结构特征融合策略是否优于现有结构感知方法 | 与PrionScan、PLAAC等结构感知变体或其他图方法比较 | Results表1 |

## 14 Agent 提炼的知识候选
**Agent 提炼的知识候选**（面向IDP/IDR × 蛋白互作 × AI/物理模拟课题）：

1. **AlphaFold结构→接触图→GAT的迁移路径**：即使目标蛋白（如IDP）缺乏稳定全局结构，将AlphaFold预测结构转化为接触图（Cα距离<8Å）并用GAT提取拓扑嵌入，仍可提供超越序列的判别特征。迁移到IDR互作预测时，可考虑：(a) 按pLDDT分层加权接触图，降低低置信度区域噪声；(b) 将接触图与MD模拟的瞬态接触集合对比，验证结构特征的生物学意义。

2. **多层级特征融合框架**：序列特征（无序性、电荷模式、疏水性）+ 局部构象（二级结构倾向）+ 全局拓扑（图嵌入）的三层融合策略，可迁移到IDR介导互作预测——例如预测IDR是否介导相分离时，可融合序列组成、预测的IDR长度/位置、AlphaFold接触图、以及互作伙伴特征。

3. **SMOTE在生物序列不平衡问题中的应用**：正样本稀少是IDP/IDR注释数据的常态。SMOTE在特征空间合成少数类样本，且作者在独立测试集上验证了泛化性（非过拟合），说明该策略在特征维度适中时有效。迁移时注意：SMOTE应在特征拼接后、交叉验证的训练fold内应用，避免数据泄漏。

4. **Stacking集成作为决策层**：RF/XGBoost/LGBM三个异构树模型+逻辑回归元学习器，优于单模型和MLP决策层。对IDR预测任务，可尝试不同基学习器组合（如SVM+树模型+图神经网络），元学习器用逻辑回归保持可解释性。

5. **对比基线选择策略**：本文选择了覆盖不同机制的代表性方法（prion-like、π-π、无序性、深度学习），而非仅选最新方法。这种"机制覆盖式"基线选择有助于定位新方法的增量贡献。

6. **消融实验设计模板**：按特征层级（序列/二级结构/图嵌入）和决策模块（单模型/MLP/集成）两个维度消融，清晰分离各组件贡献。对IDR课题，可增加"IDR区域特征 vs 全局特征"的消融维度。

7. **特征可解释性分析**：15个手工特征均通过Mann-Whitney U检验验证判别力，且与已知LLPS机制一致（IDR富集、电荷模式、π-π）。这种"机制-特征"对应分析可迁移到IDR互作预测，帮助建立模型预测与分子机制的联系。

## 15 与已有知识连接
- **LLPS预测方法谱系**：本文与PLAAC（prion-like domain）、catGRANULE（多特征加权）、PScore（π-π）、DeePhase（深度学习）、FuzDrop（物理模型）、Seq2Phase/MambaPhase（蛋白语言模型）形成对比。本文的增量在于显式引入AlphaFold结构拓扑，而非仅序列特征。
- **AlphaFold在功能预测中的应用**：本文属于"AlphaFold结构→下游功能预测"的范式，与AlphaFold在结合位点预测、突变效应预测等应用一致。对IDR课题，需注意AlphaFold对无序区域的预测可靠性问题（pLDDT低），可参考AlphaFold2原始论文及后续关于IDR预测不确定性的讨论。
- **图神经网络在蛋白质功能预测中的应用**：GAT用于蛋白质接触图/结构图建模，与GNN在蛋白质-配体结合、酶功能预测等工作一致。本文的接触图构建（Cα距离<8Å）是蛋白质残基接触图的常用定义。
- **集成学习在生物信息学中的应用**：Stacking集成在蛋白质预测任务中已有广泛应用（如二级结构预测、亚细胞定位），本文将其用于LLPS预测。
- **SMOTE在不平衡生物数据集中的应用**：SMOTE是处理生物医学不平衡分类的经典方法，本文在特征空间而非序列空间应用，避免了生成不真实序列的问题。
- **IDR/相分离机制知识**：本文特征选择与已知LLPS机制一致——IDR富集（ESpritz）、低复杂度区域（SEG）、电荷模式（LocalCIDER Omega）、π-π（PScore）、溶解度（Protein-sol）。这些特征与Brangwynne、Fuxreiter等关于相分离驱动力的综述一致。
- **[Analysis] 候选连接**：本文未使用分子动力学（MD）模拟，但其接触图特征可视为静态结构近似。可连接MD模拟文献，探讨瞬态接触与AlphaFold静态接触的互补性；也可连接AlphaFold3等新工具，探讨其对IDR-蛋白复合物预测的改进是否可进一步提升此类框架性能。

## 16 Agent 生成的研究候选
**Agent 生成的研究候选**（面向IDP/IDR × 蛋白互作 × AI/物理模拟）：

1. **候选名称**：IDR-Aware Contact Graph Weighting for Phase Separation Prediction
   - **来源局限/观察**：MuFGPS未按pLDDT或IDR注释加权接触图，而IDR区域是相分离关键驱动区域但AlphaFold预测置信度低。
   - **核心假设**：对IDR区域接触赋予更高权重（或单独建模IDR-IDR接触子图），可提升LLPS预测性能。
   - **初步方法**：在MuFGPS框架基础上，将AlphaFold pLDDT值作为节点/边权重，或构建IDR-接触子图与有序域-接触子图的双通道GAT。
   - **验证方式**：在相同基准数据集上对比加权/未加权版本；按蛋白IDR含量分层分析性能差异。
   - **创新状态**：unverified

2. **候选名称**：MD-Ensemble Contact Maps as Dynamic Features for LLPS Prediction
   - **来源局限/观察**：MuFGPS仅使用AlphaFold静态结构，未捕捉IDR的构象系综和瞬态接触。
   - **核心假设**：MD模拟产生的接触系综（如接触概率矩阵）比单一静态接触图更能编码IDR介导的多价弱相互作用。
   - **初步方法**：对正负样本子集运行粗粒化MD（如MARTINI）或增强采样，提取接触概率矩阵作为额外图特征，与AlphaFold接触图融合。
   - **验证方式**：对比静态图、MD系综图、两者融合的性能；分析MD接触概率与已知相分离驱动残基的对应关系。
   - **创新状态**：unverified

3. **候选名称**：Cross-Species Transfer Learning for IDR-Mediated Interaction Prediction
   - **来源局限/观察**：MuFGPS训练数据以真核蛋白为主，IDR介导互作的物种特异性可能限制泛化。
   - **核心假设**：IDR介导互作的序列-结构特征在物种间存在保守模式，可通过跨物种预训练+微调提升泛化。
   - **初步方法**：在多个物种的蛋白互作数据上预训练特征提取器，在LLPS/IDR互作数据集上微调。
   - **验证方式**：留一物种交叉验证；对比直接训练与迁移学习性能。
   - **创新状态**：unverified

4. **候选名称**：Interpretable IDR Motif Discovery via Attention Weights
   - **来源局限/观察**：MuFGPS的GAT注意力权重未被用于解释预测，而IDR中的特定短线性基序（SLiMs）可能驱动相分离。
   - **核心假设**：GAT注意力权重可识别对LLPS预测贡献最大的残基/接触，这些残基富集已知相分离驱动基序。
   - **初步方法**：提取GAT注意力权重，映射回残基级别，与已知SLiM数据库（如ELM）比对；用SHAP或LIME验证。
   - **验证方式**：注意力权重高值残基是否富集已知相分离相关基序；与突变实验数据对比。
   - **创新状态**：unverified

5. **候选名称**：Uncertainty-Aware LLPS Prediction with Ensemble Calibration
   - **来源局限/观察**：MuFGPS未报告预测置信度，而LLPS预测的假阳性可能影响湿实验验证优先级。
   - **核心假设**：通过集成模型的预测方差或MC-Dropout可量化预测不确定性，高置信度预测更可能被实验验证。
   - **初步方法**：在MuFGPS的Stacking框架中加入不确定性估计（如集成方差、温度缩放校准），输出预测概率+置信区间。
   - **验证方式**：在独立测试集上评估校准误差（ECE）；与湿实验验证结果对比。
   - **创新状态**：unverified