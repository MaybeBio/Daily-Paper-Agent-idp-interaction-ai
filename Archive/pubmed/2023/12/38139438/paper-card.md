## 01 基本信息

- **标题**: Pathogenic Variants in USH1G/SANS Alter Protein Interaction with Pre-RNA Processing Factors PRPF6 and PRPF31 of the Spliceosome
- **作者与单位**: Fritze, Jacques S; Stiehler, Felizitas F; Wolfrum, Uwe（Institute of Molecular Physiology, Johannes Gutenberg University Mainz, Germany）
- **期刊/预印本平台**: International Journal of Molecular Sciences (IJMS)
- **年份**: 2023
- **论文类型**: 原创研究论文
- **领域**: 分子生物学 / 剪接调控 / Usher综合征病理机制
- **关键词**: SANS; USH1G; PRPF31; PRPF6; pre-mRNA splicing; FRET; AlphaFold2; intrinsically disordered region
- **DOI/arXiv 号**: 10.3390/ijms242417608
- **代码**: https://github.com/LabWolfrum/Fritze_et_al.2023.git
- **数据**: 未提供（结构预测文件在GitHub）
- **阅读日期**: 2026-05-13
- **在该课题方向中的位置**: 本文以Usher综合征蛋白SANS为对象，研究其IDR（CENTn2）与剪接因子PRPF6/PRPF31的互作，核心发现为IDR在结合配体时发生无序→α-helix的构象转变，且该转变受致病突变干扰。对「IDP/IDR × 蛋白互作 × AI方法」课题的参考价值在于：(1) 展示了AlphaFold2-multimer + Metapredict + CIDER组合用于IDR互作预测的流程；(2) 提供了IDR结合诱导折叠（coupled folding and binding）的实验证据（FRET）；(3) 展示了致病突变如何通过影响IDR构象转变来破坏互作。

## 02 一句话总结

本文通过FRET实验和AlphaFold2-multimer结构预测，证明SANS蛋白的CENTn结构域通过两个不同区域（CENTn1和CENTn2）分别直接结合剪接因子PRPF31和PRPF6，其中PRPF6结合诱导CENTn2从无序区转变为α-helix，而USH1G致病突变（V132Gfs*3和S278Pfs*71）破坏这些互作。

## 03 研究问题

- **具体问题**: SANS蛋白的CENTn结构域如何与剪接因子PRPF31和PRPF6发生分子层面的互作？USH1G致病突变如何影响这些互作？
- **为什么重要**: SANS是Usher综合征1G型的致病蛋白，此前发现其参与pre-mRNA剪接调控，但互作的分子机制（直接/间接、结合位点、构象变化）未知。理解这些机制对阐明USH1G病理至关重要。
- **现有方法为何不足**: 此前仅通过体外pull-down确认了SANS与PRPF31/PRPF6的互作，但无法区分直接/间接结合，无法定位精确结合位点，也无法解释致病突变如何影响互作。
- **精确的"Can..."问题**: Can AlphaFold2-multimer predict the binding interface between an IDR-containing scaffold protein (SANS) and its spliceosomal partners (PRPF31/PRPF6), and can FRET validate these predictions in cells?

## 04 背景与发展脉络

**脉络标注**: 仅本文框架（基于本文引文与叙述）

1. **阶段一：SANS作为Usher综合征蛋白的经典功能研究**
   - 代表方法: 免疫共沉淀、免疫荧光、pull-down
   - 发现: SANS在听觉毛细胞中维持静纤毛排列，参与蛋白转运复合物
   - 局限: 未涉及剪接功能

2. **阶段二：SANS参与pre-mRNA剪接的发现**
   - 代表方法: 转录组分析、剪接报告基因、pull-down
   - 发现: SANS介导U4/U6.U5 tri-snRNP核内转运，SANS缺失改变剪接动力学
   - 局限: 互作分子机制不清

3. **阶段三：结构预测与IDR分析（本文位置）**
   - 代表方法: AlphaFold2-multimer、Metapredict、CIDER、FRET
   - 发现: CENTn1结合PRPF31，CENTn2（IDR）结合PRPF6，结合诱导IDR→α-helix转变
   - 局限: AlphaFold2对IDR复合物预测置信度有限，需实验验证

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 互作直接性不明 | 无法判断SANS与PRPF31/PRPF6是直接结合还是通过其他蛋白介导 | 此前仅用pull-down，可能捕获间接互作 | Results 2.1: "positive FRET signals are only achieved at a distance of 8–10 nm or less" |
| 结合位点未定位 | CENTn结构域含~120个氨基酸，具体结合区域未知 | 缺乏高分辨率结构或突变扫描 | Results 2.2: AlphaFold2预测定位到CENTn1 (aa 128-173) 和CENTn2 (aa 174-243) |
| IDR构象动态不明 | SANS CENTn2为预测IDR，其构象变化机制未知 | IDR难以用传统结构生物学方法研究 | Results 2.3: Metapredict + CIDER预测IDR特性；FRET显示结合诱导折叠 |
| 致病突变机制不清 | V132Gfs*3和S278Pfs*71如何导致病理表型未知 | 突变可能影响蛋白稳定性、定位或互作 | Results 2.4: 突变体FRET效率显著降低 |
| AlphaFold2对IDR复合物预测置信度低 | 全长蛋白复合物预测失败，仅短片段预测成功 | AlphaFold2训练数据以折叠蛋白为主 | Results 2.2: "low confidence (PAEmean ≥ 25.66 Å)" for full-length predictions |

## 06 核心思想

### 1) 表面方法
- 在HEK293T细胞中过表达荧光标记的SANS（野生型或致病突变体）与PRPF31/PRPF6，通过FRET acceptor photobleaching检测直接互作
- 使用AlphaFold2-multimer预测SANS与PRPF31/PRPF6的结合界面
- 使用Metapredict和CIDER预测SANS的IDR区域及理化性质
- 将预测的SANS-PRPF复合物结构拟合到已发表的tri-snRNP冷冻电镜结构（PDB: 6QW6）中

### 2) 核心洞察
- **SANS通过两个独立且不重叠的区域结合两个不同的剪接因子**：CENTn1（aa 128-173，结构化α-helix）结合PRPF31，CENTn2（aa 174-243，IDR）结合PRPF6
- **IDR结合诱导折叠**：PRPF6结合诱导CENTn2从无序状态转变为短α-helix（aa 183-198），这是典型的 coupled binding and folding 机制
- **结合顺序性**：PRPF31结合不依赖PRPF6，但PRPF31的存在会干扰SANS-PRPF6互作，提示顺序性结合或竞争性结合
- **致病突变通过破坏IDR构象转变来致病**：S278Pfs*71突变导致CENTn2 IDR特性改变，破坏PRPF6结合

### 3) 可能的普适教训 [Analysis]
- **IDR介导的互作可以通过"区域分工"实现多特异性**：一个IDR-containing scaffold蛋白可以通过不同区域（一个结构化、一个无序）结合不同配体，实现功能整合
- **AlphaFold2-multimer对IDR复合物的预测需要"分而治之"策略**：全长预测失败时，截短到互作界面区域可显著提高预测置信度
- **FRET acceptor photobleaching是验证IDR互作的良好实验手段**：因为IDR互作通常亲和力较低，FRET可在活细胞中检测直接互作
- **IDR的进化保守性可能暗示功能重要性**：本文发现CENTn2 IDR在哺乳动物中高度保守，挑战了"IDR不保守"的普遍认知

## 07 方法总览

- **输入**: 
  - SANS全长及截短突变体cDNA（野生型、V132Gfs*3、S278Pfs*71）
  - PRPF31、PRPF6全长cDNA
  - 蛋白序列（UniProt: SANS/Q495M9, PRPF31/Q8WWY3, PRPF6/O94906, harmonin/Q9Y6N9）

- **输出**:
  - FRET效率值（定量互作强度）
  - AlphaFold2预测的蛋白复合物结构（PDB格式）
  - IDR预测图谱（Metapredict/CIDER输出）
  - 进化保守性分析结果

- **模块**:
  1. 分子克隆模块（Gateway系统构建表达载体）
  2. 细胞实验模块（HEK293T培养、转染、固定）
  3. 显微成像模块（共聚焦显微镜、FRET acceptor photobleaching）
  4. 结构预测模块（AlphaFold2-multimer via ColabFold）
  5. 生物信息学模块（Metapredict、CIDER、多序列比对）
  6. 结构拟合模块（预测复合物拟合到tri-snRNP冷冻电镜结构）

- **训练**: 不适用（无模型训练）

- **工具**: 
  - ColabFold (AlphaFold2-multimer_v2, 24 recycling)
  - Metapredict (Python library)
  - CIDER (在线平台)
  - Fiji/ImageJ (Coloc 2插件, Plot Profile)
  - PyMOL / UCSF Chimera
  - Jalview (多序列比对)
  - R-Studio (统计分析)

- **反馈回路**: 无（非迭代方法）

- **文字流程**:
  1. 克隆SANS野生型、突变体及PRPF31/PRPF6表达载体
  2. 共转染HEK293T细胞，固定后共聚焦成像
  3. 进行FRET acceptor photobleaching，计算FRET效率
  4. 用AlphaFold2-multimer预测SANS-PRPF复合物结构
  5. 用Metapredict/CIDER分析SANS IDR特性
  6. 多序列比对分析进化保守性
  7. 将预测复合物拟合到tri-snRNP冷冻电镜结构
  8. 统计分析FRET数据

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| FRET acceptor photobleaching | 检测活细胞中蛋白直接互作 | 区分直接/间接结合，定量互作强度 | 输入：共表达荧光蛋白的细胞；输出：FRET效率值 | Results 2.1, 图3: 阳性FRET信号证实直接互作 | 无法区分直接/间接互作，无法验证AlphaFold2预测 |
| AlphaFold2-multimer | 预测蛋白复合物结构 | 定位精确结合位点 | 输入：蛋白序列；输出：预测复合物结构+PAE分数 | Results 2.2, 图4: 预测CENTn1-PRPF31和CENTn2-PRPF6界面 | 无法获得结合位点信息，无法设计突变验证实验 |
| Metapredict | 预测IDR区域 | 识别无序区域 | 输入：蛋白序列；输出：每个残基的无序分数 | Results 2.3, 图5A: 预测CENTn2为IDR | 无法解释CENTn2的构象可塑性 |
| CIDER | 分析IDR理化性质 | 预测IDR行为类型（如Janus序列） | 输入：蛋白序列；输出：电荷分布、Janus预测 | Results 2.3, 图5C: 预测CENTn2为Janus序列 | 无法解释IDR的构象转变能力 |
| 进化保守性分析 | 评估功能重要性 | IDR保守性暗示功能 | 输入：多物种SANS序列；输出：保守性分数 | Results 2.3, 图5B: IDR区域保守 | 无法判断IDR功能重要性 |
| 结构拟合到tri-snRNP | 评估SANS在剪接体中的空间位置 | 理解互作的时空顺序 | 输入：预测复合物+PDB: 6QW6；输出：拟合模型 | Results 2.2, 图4D,E: SANS与PRPF3空间分离 | 无法评估SANS在tri-snRNP中的整合方式 |

**消融效应区分**: 本文未做模块消融实验。上述"移除后影响"为[Analysis]基于方法学逻辑的预期推断，非实测数据。

## 09 关键公式符号

本文涉及的唯一公式为FRET效率计算：

**FRET效率公式**:
$$FRET_{eff} = \frac{D_{post} - D_{pre}}{D_{post}}$$

- $D_{pre}$: 光漂白前供体（donor, eCFP）荧光强度
- $D_{post}$: 光漂白后供体荧光强度
- $FRET_{eff}$: FRET效率，反映供体-受体间能量转移效率，与两蛋白间距离（<10 nm）相关

**漂白效率公式**:
$$Bleach_{eff} = \left(1 - \frac{A_{post}}{A_{pre}}\right) \times 100$$

- $A_{pre}$: 光漂白前受体（acceptor, eYFP）荧光强度
- $A_{post}$: 光漂白后受体荧光强度
- $Bleach_{eff}$: 漂白效率，用于质量控制（仅>60%的数据纳入分析）

**用途**: 前者定量蛋白互作强度，后者确保FRET数据可靠性。

**来源**: Methods 4.5节

## 10 实验设计与证据链

**数据集/群体**:
- 细胞系: HEK293T (ATCC: CRL-3216)
- 蛋白构建: SANS全长、SANS-Nterm (aa 1-243)、SANSV132Gfs*3、SANSS278Pfs*71、PRPF31、PRPF6、harmonin
- 荧光标记: eCFP (供体), eYFP (受体), mRFP/mCherry (竞争/共定位)

**指标**: FRET效率、Pearson共定位系数、PAE分数

**基线/对照**:
- 阳性对照: eCFP-c-eYFP串联构建（已知强FRET）
- 阴性对照: 不相关蛋白对、单独表达供体/受体
- 已知互作对照: SANS-harmonin（已知互作）

**预算/仪器**: 未提供具体经费信息；共聚焦显微镜为Leica TCS SP5/SP8

**评测协议**: 至少3次独立实验，每次≥6个ROI，漂白效率>60%才纳入分析

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| FRET: SANS-PRPF31 | SANS直接结合PRPF31 | eCFP-PRPF31 + eYFP-SANS vs 阴性对照 | 显著FRET信号 | SANS与PRPF31直接互作 | 无法定位精确结合位点 | Results 2.1, 图3B |
| FRET: SANS-PRPF6 | SANS直接结合PRPF6 | PRPF6-eCFP + eYFP-SANS vs 阴性对照 | 显著FRET信号 | SANS与PRPF6直接互作 | 无法定位精确结合位点 | Results 2.1, 图3B |
| FRET: SANS-PRPF3 | PRPF3为阴性对照 | eCFP-PRPF3 + eYFP-SANS | 无显著FRET信号 | SANS不结合PRPF3 | 无法排除低亲和力互作 | Results 2.1, 图3C |
| AlphaFold2: SANS CENTn1-PRPF31 | CENTn1 (aa 128-173) 为PRPF31结合位点 | 截短片段预测 vs 全长预测 | 高置信度预测 (PAEmean ≤ 11.83 Å) | CENTn1介导PRPF31结合 | 预测需实验验证 | Results 2.2, 图4A |
| AlphaFold2: SANS CENTn2-PRPF6 | CENTn2 (aa 174-243) 为PRPF6结合位点 | 截短片段预测 vs 全长预测 | 高置信度预测 (PAEmean ≤ 10.21 Å) | CENTn2介导PRPF6结合 | 预测需实验验证 | Results 2.2, 图4B |
| FRET: SANSV132Gfs*3-PRPF6 | 致病突变破坏PRPF6结合 | 突变体 vs 野生型 | FRET效率显著降低 | V132Gfs*3破坏PRPF6互作 | 无法区分直接/间接效应 | Results 2.4, 图6C |
| FRET: SANSV132Gfs*3-PRPF31 | V132Gfs*3不影响PRPF31结合 | 突变体 vs 野生型 | FRET效率无显著变化 | PRPF31存在替代结合位点（N端锚蛋白重复区） | 无法定位替代位点 | Results 2.4, 图6D |
| FRET: SANSS278Pfs*71-PRPF31/PRPF6 | 致病突变破坏两种互作 | 突变体 vs 野生型 | 两种FRET效率均显著降低 | S278Pfs*71破坏SANS与两种PRPFs的互作 | 无法区分蛋白稳定性vs互作缺陷 | Results 2.4, 图6A,B |
| Metapredict/CIDER: SANS IDR分析 | CENTn2为IDR且具有Janus特性 | 预测工具输出 | CENTn2预测为IDR，Janus序列 | CENTn2具有构象可塑性 | 预测需实验验证 | Results 2.3, 图5A,C |

## 11 结论正确解读

- **任务范围**: 本文仅研究SANS与PRPF31/PRPF6的二元互作，不涉及SANS在完整剪接体中的动态行为或与其他剪接因子的互作。
- **oracle/真值输入**: AlphaFold2预测使用了UniProt序列，无实验结构作为模板；FRET实验使用了过表达系统，非内源水平。
- **端到端状态**: 非端到端。结构预测与实验验证是分离的，预测结果仅用于指导实验设计，未形成闭环优化。
- **算力成本**: 未提供具体算力信息。ColabFold为云端免费服务，计算成本较低。
- **历史数据依赖**: AlphaFold2训练数据包含PDB中已知蛋白复合物结构，对IDR复合物的预测能力有限；本文通过截短策略部分规避了此问题。
- **模型依赖**: 结论高度依赖AlphaFold2-multimer的预测准确性，作者承认对IDR复合物预测置信度有限。
- **最难情形**: IDR（CENTn2）与PRPF6的互作预测是本文最困难的部分，因为AlphaFold2对无序区域的建模能力有限。
- **群体/领域边界**: 结论仅限于SANS-PRPF31/PRPF6互作，不能推广到其他USH1G互作网络或一般IDR互作机制。
- **不确定性**: FRET效率降低可能反映结合亲和力下降、结合构象改变或蛋白稳定性降低，本文无法区分这些可能性。

**有边界的复述**: 在HEK293T过表达系统中，SANS通过CENTn1（aa 128-173）直接结合PRPF31，通过CENTn2（aa 174-243，IDR）直接结合PRPF6；PRPF6结合诱导CENTn2形成α-helix；USH1G致病突变V132Gfs*3破坏PRPF6互作但不影响PRPF31互作，S278Pfs*71破坏两种互作。这些结论基于FRET实验和AlphaFold2预测，未在体内或内源水平验证。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| AlphaFold2对IDR复合物预测置信度有限 | 全长SANS与PRPF31/PRPF6复合物预测失败，仅截短片段预测成功 | 未明确提及 | Discussion: "low confidence...probably since AlphaFold2-multimer is trained on structured protein data" |
| 无法解释S278Pfs*71突变导致互作破坏的机制 | 突变体仍包含PRPF31/PRPF6结合位点，但互作被破坏 | 作者推测可能是脯氨酸含量变化导致空间位阻 | Discussion: "content of proline residues in the frameshift sequence changes from 2 to 9" |
| 未验证SANS与PRPF31/PRPF6互作的动态时序 | 无法确定SANS是同时还是顺序性结合两种PRPFs | 作者提出顺序性结合假说 | Discussion: "SANS molecules bind to both PRPFs separately, either sequentially...or independently" |
| 未在体内验证互作 | 所有实验均在HEK293T过表达系统进行 | 未明确提及 | 未提供 |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|---------------------|----------|----------|------|
| AlphaFold2预测的"高置信度"仅基于截短片段 | 截短可能改变蛋白天然构象，预测的界面可能不代表全长蛋白中的真实互作 | 如果预测界面不准确，后续实验设计将基于错误假设 | 使用交联质谱（cross-linking MS）或NMR验证全长蛋白中的互作界面 | Results 2.2: 全长预测失败，截短后成功 |
| FRET效率降低可能反映蛋白稳定性下降而非互作破坏 | 突变体可能表达水平低、折叠错误或快速降解，导致FRET信号降低 | 如果突变体不稳定，结论"突变破坏互作"可能不成立 | 检测突变体蛋白表达水平和稳定性（如放线菌酮追踪实验） | Results 2.4: 未提供突变体表达水平数据 |
| 未检测内源SANS与PRPF31/PRPF6的互作 | 过表达可能导致非生理性互作或错误定位 | 过表达系统的假阳性/假阴性风险 | 使用内源免疫沉淀（endogenous IP）或PLA（proximity ligation assay）验证 | Methods: 所有实验均为过表达 |
| "顺序性结合"假说缺乏直接证据 | FRET竞争实验只能说明PRPF31干扰SANS-PRPF6互作，不能证明顺序性 | 如果SANS同时结合两种PRPF，则剪接调控模型需要修正 | 使用三色FRET或单分子实验检测三元复合物 | Results 2.1, 图3F: PRPF31降低SANS-PRPF6 FRET约16% |
| IDR→α-helix构象转变仅由AlphaFold2预测，无实验验证 | AlphaFold2可能错误预测IDR的折叠倾向 | 如果构象转变是核心机制，需要实验证据支持 | 使用CD光谱、NMR或HDX-MS检测CENTn2在PRPF6结合前后的构象变化 | Results 2.2: 构象转变仅来自计算预测 |
| 进化保守性分析未区分功能约束与结构约束 | IDR保守可能反映其他功能（如蛋白稳定性）而非PRPF结合 | 保守性不能直接证明互作的功能重要性 | 进行饱和突变扫描，比较PRPF结合与保守性的相关性 | Results 2.3, 图5B: 仅展示保守性，未做功能关联 |

## 14 学到什么

**Agent 提炼的知识候选**

1. **IDR"区域分工"策略**: SANS的CENTn结构域包含一个结构化亚区（CENTn1）和一个IDR亚区（CENTn2），分别结合不同配体。这提示IDR-containing scaffold蛋白可以通过结构域内区域分工实现多特异性互作，而不需要多个独立结构域。**可迁移到本课题**: 在研究IDP/IDR介导的互作网络时，不应将IDR视为均质区域，而应细分功能亚区。

2. **IDR结合诱导折叠的预测-验证闭环**: 本文展示了AlphaFold2预测IDR结合诱导折叠，再用FRET验证互作的流程。**可迁移到本课题**: 对于IDR介导的互作，AlphaFold2-multimer预测的构象转变需要实验验证，FRET acceptor photobleaching是验证IDR互作的良好手段，因为IDR互作通常亲和力低，FRET可在活细胞中检测直接互作。

3. **"分而治之"策略处理IDR复合物预测**: 全长蛋白的AlphaFold2预测失败后，截短到互作界面区域可显著提高预测置信度。**可迁移到本课题**: 对IDR-containing蛋白复合物进行结构预测时，应优先预测结构化区域与IDR中较短片段的互作，而非全长复合物。

4. **致病突变作为互作功能探针**: 本文使用致病突变来验证预测的结合位点，突变导致的互作破坏支持了预测的生物学相关性。**可迁移到本课题**: 在IDR互作研究中，天然存在的致病突变可作为"实验探针"来验证预测的互作界面。

5. **IDR的进化保守性分析**: 本文发现CENTn2 IDR在哺乳动物中高度保守，挑战了"IDR不保守"的普遍认知。**可迁移到本课题**: 在研究IDR功能时，应进行跨物种保守性分析，保守的IDR区域更可能具有功能重要性。

6. **多方法交叉验证**: 本文结合了FRET（活细胞互作）、AlphaFold2（结构预测）、Metapredict/CIDER（IDR预测）、进化分析（功能重要性）四种方法。**可迁移到本课题**: IDR互作研究需要多方法交叉验证，单一方法（尤其仅计算预测）不足以支撑结论。

## 15 与已有知识连接

- **SANS与剪接调控**: 本文是作者团队此前发现SANS参与pre-mRNA剪接调控（参考文献[3]）的延续，将互作从体外pull-down推进到活细胞FRET验证和结构预测层面。**与本课题关联**: 展示了从"发现互作"到"解析互作机制"的研究路径。

- **Usher综合征蛋白网络**: SANS与harmonin、USH2A、whirlin形成三元复合物（参考文献[9,20,26]），本文进一步扩展了SANS的互作网络至剪接因子。**与本课题关联**: IDR-containing scaffold蛋白常参与多个功能模块的整合，本文是典型案例。

- **AlphaFold2在IDR研究中的局限**: 已有文献广泛报道AlphaFold2对IDR预测置信度低（如Ruff & Pappu, 2021; Chakrabarti et al., 2023），本文的"分而治之"策略是对此局限的实用应对。**与本课题关联**: 使用AlphaFold2研究IDR互作时，需注意其训练数据偏差。

- **coupled folding and binding机制**: IDR结合配体时发生无序→有序转变是IDP领域的经典机制（如p27-KID/Cdk2体系），本文为这一机制提供了新的实例。**与本课题关联**: 支持IDR构象可塑性在互作中的普遍重要性。

- **剪接因子与视网膜疾病**: PRPF31（RP11）和PRPF6（RP60）是已知的视网膜色素变性致病基因（参考文献[4,46,47]），本文将其与USH1G/SANS联系起来。**与本课题关联**: IDR介导的互作缺陷可能是多种遗传性视网膜疾病的共同机制。

- **候选方向（未经本文验证）**: 本文未使用分子动力学（MD）模拟验证IDR构象转变的动态过程，也未使用AlphaFold3或RoseTTAFold等更新工具。这些可作为本课题的延伸方向。

## 16 研究想法

**Agent 生成的研究候选**

1. **候选名称**: IDR介导的SANS-PRPF6互作动态构象转变的MD模拟研究
   - **来源局限/观察**: 本文仅用AlphaFold2静态预测了CENTn2的α-helix构象，未揭示IDR从无序到有序转变的动态路径和热力学驱动
   - **核心假设**: SANS CENTn2的IDR→α-helix转变遵循特定的折叠路径，PRPF6结合通过熵-焓补偿驱动该转变
   - **初步方法**: 使用增强采样MD（如REMD、metadynamics）模拟CENTn2在自由态和PRPF6结合态下的构象系综；计算结合自由能分解
   - **验证方式**: 与本文FRET数据对比；预测致病突变对构象转变自由能的影响
   - **可能的失败模式**: IDR采样不足导致自由能计算不可靠；力场对IDR描述不准确
   - **创新状态**: unverified

2. **候选名称**: 基于AlphaFold2-multiverse的SANS-IDR互作伴侣全局预测
   - **来源局限/观察**: 本文仅研究了PRPF31和PRPF6两个剪接因子，但SANS的CENTn结构域已知可结合50种以上蛋白（参考文献[3,9,14,17,20]）
   - **核心假设**: SANS的CENTn1和CENTn2亚区分别识别特定类型的互作基序，可通过序列特征预测未知互作伴侣
   - **初步方法**: 使用AlphaFold2-multiverse或批量AlphaFold2-multimer筛选SANS CENTn与候选蛋白库的互作；结合共免疫沉淀验证
   - **验证方式**: 对预测的高置信度互作进行FRET或pull-down验证
   - **可能的失败模式**: IDR互作的预测准确率低；候选库选择偏差
   - **创新状态**: unverified

3. **候选名称**: 致病突变对IDR相分离行为影响的生物物理研究
   - **来源局限/观察**: 本文发现SANS CENTn2是IDR且具有Janus序列特征，但未研究其相分离行为；SANS已知参与多种细胞凝聚体（如Cajal body）定位
   - **核心假设**: SANS CENTn2的IDR特性赋予其相分离能力，致病突变通过改变IDR电荷分布或疏水性影响相分离
   - **初步方法**: 体外纯化SANS CENTn2，使用浊度测定、荧光恢复（FRAP）和液滴融合实验检测相分离；比较野生型与突变体的相图
   - **验证方式**: 在细胞中检测SANS凝聚体的动态和组成
   - **可能的失败模式**: CENTn2单独不足以驱动相分离，需要多结构域协同
   - **创新状态**: unverified

4. **候选名称**: SANS-IDR互作界面的深度学习预测与突变效应评分
   - **来源局限/观察**: 本文手工分析了AlphaFold2预测的互作界面，但未系统评估所有已知致病突变对互作的影响
   - **核心假设**: 基于结构的深度学习模型（如ESM-IF、ProteinMPNN）可准确预测SANS CENTn突变对PRPF31/PRPF6结合的影响
   - **初步方法**: 收集USH1G所有已知致病突变，使用结构感知的突变效应预测工具评分；与本文FRET数据对比
   - **验证方式**: 对预测为"破坏性"的突变进行实验验证
   - **可能的失败模式**: 训练数据中IDR互作样本不足；突变效应预测工具对IDR界面不敏感
   - **创新状态**: unverified

5. **候选名称**: SANS-PRPF31/PRPF6互作的进化深度扫描（deep mutational scanning）
   - **来源局限/观察**: 本文仅测试了两个致病突变，未系统探索CENTn结构域的序列-功能关系
   - **核心假设**: CENTn1和CENTn2的序列约束不同，CENTn2（IDR）可能具有更高的突变耐受性但关键残基对结合至关重要
   - **初步方法**: 构建SANS CENTn饱和突变文库，使用报告基因系统（如剪接报告子）进行深度扫描
   - **验证方式**: 与本文AlphaFold2预测的界面残基对比
   - **可能的失败模式**: 高通量功能检测灵敏度不足；IDR突变可能通过非结合机制影响功能
   - **创新状态**: unverified