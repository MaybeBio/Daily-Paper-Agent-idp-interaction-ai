## 01 基本信息

- **标题**: Advantages and Limitations of AlphaFold in Structural Biology: Insights from Recent Studies
- **作者**: Li, Mandarina Qing Cheng; Wang, Sihan; Lin, Shi-Ruei; Ting, Li Eric Ngok; Wan, Zhi-Hong; Xie, Guodong; Zhang, Jane
- **单位**: 未提供（作者单位未在摘要中列出）
- **期刊/平台**: The Protein Journal
- **年份**: 2025（在线日期 2025-12-02）
- **论文类型**: 系统综述（Systematic Review）
- **领域**: 结构生物学、计算生物学、AI蛋白质结构预测
- **关键词**: AlphaFold, cryo-EM, cryo-ET, 蛋白质结构预测, 整合结构生物学
- **DOI/arXiv**: 10.1007/s10930-025-10310-8
- **代码**: 未提供（提及 Supplementary Code，但未公开仓库地址）
- **数据**: 32项EMDB条目（2024年沉积），见Table 1及Supplementary Data File 1
- **阅读日期**: 2026-04-26（系统日期）
- **在该课题方向中的位置**: 本文是**综述性论文**，系统评估AlphaFold在cryo-EM/cryo-ET工作流中的实际应用模式与局限。对IDP/IDR×蛋白互作×AI方向而言，本文提供了AlphaFold在**无序区、柔性区域、动态构象、多亚基组装**等场景下失效模式的实证汇总，可作为该课题中"AI预测何时不可靠、如何与实验互补"的方法论参考。

---

## 02 一句话总结

本文系统回顾了2024年沉积于EMDB的32项cryo-EM/cryo-ET研究，定量统计了AlphaFold的使用率（78.1%），归纳出三种应用模式（初始模型生成、结构域拟合/验证、功能推断），并明确指出AlphaFold在无序区、动态构象、翻译后修饰、非蛋白组分及大尺度组装等场景下的固有局限。

---

## 03 研究问题

- **具体问题**: AlphaFold在真实cryo-EM/cryo-ET研究中的使用有多普遍？它以何种方式被使用？在哪些场景下有效、哪些场景下失效？
- **为什么重要**: AlphaFold已被广泛采用，但对其"实际贡献边界"缺乏系统性、定量的评估。了解其在真实工作流中的优势与局限，对于合理使用AI预测工具、避免过度解读至关重要。
- **现有方法为何不足**: 已有综述多为定性讨论或聚焦单一案例，缺乏跨研究的系统统计；且多数讨论集中于AlphaFold对单体球状蛋白的预测能力，对其在**多亚基、柔性、无序、膜结合、翻译后修饰**等复杂场景下的表现缺乏汇总。
- **精确研究问题**: "在2024年EMDB沉积的cryo-EM/cryo-ET研究中，AlphaFold的使用模式、贡献程度及失效场景呈现怎样的分布？"

---

## 04 背景与发展脉络

> 注：以下脉络基于本文框架，标注为「仅本文框架」；部分外部信息标注「经外部核验」。

1. **冷冻电镜单颗粒分析（cryo-EM）**（本文Introduction）
   - 无需结晶，适合大分子复合物，但需要纯化样品，难以捕捉细胞内原生状态。
2. **冷冻电子断层扫描（cryo-ET）**（本文Introduction）
   - 可在近原生状态下成像，但分辨率受限，存在"missing wedge"问题。
3. **AlphaFold/AlphaFold2**（本文Introduction, Discussion）
   - 基于深度学习从序列预测结构，在CASP14达到近实验精度。
   - 局限：静态单构象、对无序区输出低置信度、无法处理配体/修饰/多聚体动态组装。
4. **整合结构生物学**（本文核心主张）
   - AI预测 + 实验密度图（cryo-EM/ET）+ 生化验证的迭代工作流，是当前主流范式。
   - 本文定位：对这一范式在2024年的实际执行情况做系统盘点。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 无序区/IDR预测不可靠 | AlphaFold对无序区返回低pLDDT（<50）的静态片段化结构 | 训练数据以有序折叠蛋白为主，无序区缺乏稳定构象模板 | Discussion: "Proteins such as α-synuclein, Tau, and the p53 transactivation domain... returned by AlphaFold as static, fragmented, low-confidence predictions (pLDDT < 50)" |
| 动态构象/多状态无法捕捉 | 无法预测肌球蛋白头部在收缩过程中的状态转换 | AlphaFold输出单一静态构象，不包含时间维度 | Result 3, Fig. 5A: 心肌粗丝中三种肌球蛋白头状态需cryo-ET实验解析 |
| 大尺度组装/原位环境超出预测范围 | CRP-C1复合物、LRRK2-微管纤维、染色质高级结构无法从序列预测 | 组装依赖膜表面、拥挤环境、细胞力学等多因素 | Result 3, Fig. 4A-D: 这些结构仅能通过cryo-ET在原位解析 |
| 非蛋白组分不可预测 | 脂质、聚糖、RNA等无法由AlphaFold建模 | AlphaFold仅以氨基酸序列为输入 | Result 3, Discussion: "cannot predict the structures of nucleic acids, lipids, or other non-protein macromolecules" |
| 弱/瞬时互作界面预测困难 | Hsp90-共伴侣、泛素-E2等弱互作复合物中伙伴取向常被错配 | 弱互作界面在进化中保守信号弱，训练数据中代表性不足 | Discussion: "AlphaFold-Multimer often misassigns partner orientation or fails to model the flexible linker regions" |
| 翻译后修饰/配体诱导构象变化无法预测 | 免疫逃逸中MHC-I的动态调控、PROTAC三元复合物 | 序列输入不含修饰信息，构象变化依赖上下文能量学 | Discussion: "ligand-induced transitions and ternary PROTAC complexes remain beyond the system's resolution" |
| 膜蛋白跨膜区精度不足 | 螺旋取向、loop拓扑、脂质偶联常被错误预测 | 训练数据中膜蛋白代表性不足，缺少脂质环境约束 | Discussion: "helical bundle orientation, loop topology, and dynamic coupling to lipid bilayers are often mispredicted" |

---

## 06 核心思想

### 1) 表面方法
对2024年EMDB沉积的cryo-EM/cryo-ET研究进行系统检索、筛选（32项纳入），提取每项研究中AlphaFold的使用情况（是否使用、使用模式、置信度报告），进行定量统计（使用率、卡方检验、Spearman相关）和定性归纳（三种应用模式、失效场景分类）。

### 2) 核心洞察
AlphaFold在cryo-EM/cryo-ET工作流中的角色是**"假设生成器"而非"答案提供者"**。其最大价值在于为中等分辨率密度图提供可拟合的原子模型起点，但其预测的可靠性高度依赖目标区域的**有序性、构象稳定性、互作强度**。在无序区、动态构象、原位组装等场景中，AlphaFold的预测不仅无益，反而可能误导——必须由实验数据（cryo-ET、SAXS、NMR、交联质谱等）提供约束。

### 3) 可能的普适教训 [Analysis]
- **AI工具的适用边界应由"目标区域的物理化学性质"而非"整体任务类型"决定**。对IDP/IDR研究而言，这意味着不能因AlphaFold在折叠域上的成功而期望其对无序区同样有效。
- **置信度指标（pLDDT）本身就是信息**：低pLDDT区域不应被视为"预测失败"，而应被解读为"该区域可能 intrinsically disordered 或构象异质"——这恰好是IDP研究的核心对象。
- **整合工作流是双向的**：不仅AI辅助实验（提供初始模型），实验也辅助AI（提供构象约束、验证/修正预测）。对IDP/IDR系统，后者可能更为关键。

---

## 07 方法总览

- **输入**: EMDB数据库2024年1月1日至12月31日期间沉积的cryo-EM/cryo-ET条目
- **筛选**: 纳入标准——(i) 有2024年同行评审论文；(ii) 以cryo-EM/cryo-ET为主要结构解析手段；(iii) 方法学信息足以判断AlphaFold使用情况。排除纯计算论文、无实验图谱的预印本
- **编码**: 双人独立全文筛查 + 关键词搜索（"AlphaFold", "AlphaFold2", "AF2", "Multimer", "ColabFold", "predicted model", "fitted AF2 domain"），Cohen's κ报告一致性
- **提取变量**: 生物体系、技术类型、标称/局部分辨率、EMDB/PDB编号、AlphaFold版本（单体vs Multimer）、pLDDT/PAE报告情况、使用模式分类
- **分析**: 描述性统计（比例、95%CI）、关联检验（χ²/Fisher精确检验、Spearman's ρ）
- **可视化**: UCSF ChimeraX/Chimera，EMDB推荐contour level ±10-20%调整，模型-密度匹配度（CC_mask/CC_box）
- **输出**: 使用率统计、三种使用模式分类、代表性案例（Fig. 1-7）、局限性归纳

**文字流程**: EMDB检索 → 筛选32项 → 双人编码AlphaFold使用情况 → 统计检验 → 按使用模式分类 → 选取代表性案例进行模型-密度拟合评估 → 归纳优势与局限 → 提出整合工作流建议

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| EMDB系统检索与筛选 | 建立代表性研究样本 | 提供定量统计的基础数据集 | 输入：EMDB 2024年条目；输出：32项纳入研究 | Methods节；Table 1 | 无此模块则综述沦为轶事汇编，缺乏系统性 |
| AlphaFold使用情况编码 | 判断每项研究是否/如何使用AlphaFold | 量化采用率与使用模式 | 输入：全文文本；输出：二元标签+三分类使用模式 | Methods节；Cohen's κ报告 | 编码不一致将导致统计偏差 |
| 统计检验（χ²/Fisher/Spearman） | 检验分辨率与使用率之间的关联 | 判断"何时用AlphaFold"是否有规律 | 输入：编码数据+分辨率；输出：p值、ρ值 | Results: "χ²=0.20, p=0.656; ρ=-0.163, p=0.373" | 无统计检验则无法区分随机波动与真实趋势 |
| 代表性案例深度分析 | 展示AlphaFold成功与失败的具体场景 | 提供定性、可操作的洞见 | 输入：选定的cryo-EM/ET图谱+AlphaFold模型；输出：拟合评估、机制解释 | Fig. 1-7；Result 2, 3 | 仅靠统计无法传达"何时该信、何时不该信"的实操判断 |
| 局限性归纳与未来方向 | 提炼AlphaFold的边界条件 | 指导社区合理使用 | 输入：全部案例的综合；输出：局限性清单+未来方向 | Discussion; Future Perspectives | 无此模块则综述缺乏实用价值 |

---

## 09 关键公式符号

本文为综述性论文，**不涉及新的数学公式或算法推导**。核心定量工具为：

- **χ²检验**（卡方检验）：用于检验AlphaFold使用与分辨率分组之间的关联。χ² = 0.20, p = 0.656（不显著）
- **Fisher精确检验**：p = 0.640（不显著）
- **Spearman秩相关系数**：ρ = -0.163, p = 0.373（不显著）
- **Cohen's κ**：用于评估两位评审者编码一致性（具体值在Supplementary Table S1中，摘要未提供）

**符号含义**：
- pLDDT: predicted Local Distance Difference Test，AlphaFold的逐残基置信度分数（0-100）
- pTM: predicted Template Modeling score，整体结构置信度
- PAE: Predicted Aligned Error，残基对间相对位置误差
- CC_mask/CC_box: 模型与密度图之间的相关系数（掩膜内/盒内）

**用途**：这些统计量用于支持"AlphaFold使用与分辨率无显著关联"的结论，以及"使用率在各类体系中普遍较高"的描述。

---

## 10 实验设计与证据链

### 数据集与规模
- **来源**: EMDB 2024年1月1日-12月31日沉积条目
- **纳入**: 32项研究（Table 1）
- **分辨率范围**: 3.0 Å至~31.7 Å（后者为原位cryo-ET）
- **高分辨率子集**: 3.0-4.0 Å，9项
- **生物体系**: 人类、猪、多种细菌/真核复合物、痘苗病毒等病毒组装体

### 指标
- AlphaFold使用率（二元）
- 使用模式（三分类：初始模型生成/结构域拟合验证/功能推断）
- 标称分辨率与使用率的关联

### 关键结果

| 实验/分析 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|-----------|------------|-----------|------|------------|-------------------|------|
| 使用率统计 | AlphaFold在cryo-EM/ET研究中被广泛采用 | 32项中25项使用 | 78.1%使用率 | AlphaFold已成为cryo-EM工作流的标准组件 | 样本量小（n=32），可能不代表全部2024年EMDB沉积 | Results; Table 1 |
| 分辨率-使用率关联 | 高分辨率研究是否更少依赖AlphaFold | ≤4.0Å vs >4.0Å | χ²=0.20, p=0.656; ρ=-0.163, p=0.373 | 无显著关联；使用率在各分辨率区间普遍较高 | 统计功效有限（n=32），无法排除弱关联 | Results; Supplementary Fig. S1 |
| 痘苗病毒核心蛋白案例 | AlphaFold可预测中等分辨率密度图中的有序结构域 | 7.7-13.4 Å cryo-EM图 + AF2模型 | 5个核心蛋白（A3, A4, A10, L4, F17）pLDDT>90，成功对接 | AlphaFold在中等分辨率下可提供可靠初始模型 | 仅适用于有序折叠结构域，不涉及无序区 | Result 2; Fig. 2 |
| E3泛素连接酶-底物复合物 | AlphaFold可揭示弱/瞬时互作界面 | 12.0 Å cryo-EM + AF2预测 | 疏水-静电界面被识别并经突变验证 | AlphaFold可生成可检验的互作假说 | 界面预测需实验验证，不能单独作为证据 | Result 2; Fig. 1A |
| 染色质重塑复合物 | AlphaFold可辅助亚基分配与结构域定位 | 9.7 Å cryo-EM + AF2亚基模型 | 远端结构域间的别构偶联被揭示 | AlphaFold可补充中等分辨率图中的结构信息 | 别构机制仍需生化实验支持 | Result 2; Fig. 1B |
| 心肌粗丝（cryo-ET） | AlphaFold无法预测动态构象状态 | 原位cryo-ET + AF2 | 三种肌球蛋白头状态仅实验可分辨 | 静态预测无法覆盖构象景观 | — | Result 3; Fig. 5A |
| 染色质/核小体 | AlphaFold无法预测高级别组装 | 原位cryo-ET | 高阶结构依赖细胞环境 | 序列到结构预测存在尺度上限 | — | Result 3; Fig. 4C-D |
| ZBTB20/MYPT3/SNO-GSTO1 | AlphaFold作为补充工具而非独立解法 | cryo-EM/SAXS/晶体学 + AF2 | AF2提供初始模型，但需多轮实验修正 | 整合工作流是当前最佳实践 | AF2不能替代实验定相 | Result 3; Fig. 6 |

---

## 11 核心结论

1. **AlphaFold在cryo-EM/cryo-ET研究中已被广泛采用**（78.1%），且使用率与分辨率无显著关联——无论高分辨率还是低分辨率研究，研究者都倾向于使用AlphaFold。
2. **三种主导应用模式**：(i) 为未解析或低质量密度区域生成初始原子模型；(ii) 结构域/亚基在密度图中的拟合与验证；(iii) 基于结构的功能假说生成（如突变靶点预测）。
3. **AlphaFold的核心局限**集中在：无序区/IDP（输出低置信度静态片段）、动态构象转换、翻译后修饰、非蛋白组分（脂质/聚糖/RNA）、大尺度原位组装、弱/瞬时互作界面。
4. **整合工作流是当前范式**：AI预测 + 实验密度图 + 生化验证的迭代循环，而非AI替代实验。

---

## 12 关键图表

- **Table 1**: 32项EMDB条目汇总——条目编号、分辨率、AlphaFold使用与否、DOI链接。核心统计表。
- **Fig. 1**: E3泛素连接酶-底物复合物（A, 12.0 Å）和染色质重塑复合物（B, 9.7 Å）的cryo-EM重建。展示AlphaFold辅助中等分辨率结构解析的典型案例。
- **Fig. 2**: 痘苗病毒核心蛋白（A-D）和未成熟核心（E）的cryo-EM重建。展示AlphaFold在7.7-13.4 Å分辨率下的成功应用。
- **Fig. 3**: 核孔复合物（A）、狂犬病病毒基质蛋白（B）的cryo-EM重建。展示AlphaFold在宿主-病原互作研究中的应用。
- **Fig. 4**: CRP-C1复合物（A）、LRRK2-微管（B）、染色质（C-D）的原位cryo-ET重建。展示超出AlphaFold预测能力的复杂组装。
- **Fig. 5**: 心肌粗丝（A）的cryo-ET重建。展示动态构象状态需实验解析。
- **Fig. 6**: ZBTB20（A-E）、MYPT3（F）、SNO-GSTO1的cryo-EM重建。展示AlphaFold作为补充工具而非独立解法的案例。
- **Fig. 7**: 工程化荧光蛋白（A）和免疫逃逸复合物（B）的cryo-EM重建。展示AlphaFold在工程与疾病场景中的边界。
- **Supplementary Fig. S1**: AlphaFold使用率的统计分布图。

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|-------------------|----------|----------|------|
| 样本量仅32项，且为2024年单一年份 | 可能无法代表AlphaFold使用的整体趋势；2024年可能受特定技术事件影响 | 统计结论（如"使用率与分辨率无关联"）的普适性存疑 | 扩展至多年份、更大样本量（如100+项）重新分析 | Methods节：明确限定2024年 |
| "AlphaFold贡献"分类依赖原文作者自述 | 可能存在报告偏差——未使用AlphaFold的研究可能未提及原因；使用的研究可能夸大贡献 | 分类的主观性影响所有统计结论 | 建立更客观的贡献评估标准（如模型-密度匹配度量化） | Methods节：双人编码+Cohen's κ，但κ值未在摘要中报告 |
| 综述偏向cryo-EM/ET领域 | AlphaFold在X射线晶体学、NMR、SAXS等领域的应用与局限未覆盖 | 结论可能不适用于其他结构生物学分支 | 扩展至多技术平台的比较综述 | 标题明确限定"Structural Biology"，但实际语料仅覆盖cryo-EM/ET |
| 对IDP/IDR的讨论停留在已知结论层面 | 未提供新的量化分析（如pLDDT分布与实验无序区注释的系统比较） | 对IDP研究者而言，缺乏可操作的新洞见 | 对32项研究中的低pLDDT区域与实验无序注释做系统比对 | Discussion: 仅定性提及α-synuclein, Tau, p53 |
| 未讨论AlphaFold3的潜在改进 | 综述聚焦AlphaFold2，但AlphaFold3已发布并声称改进配体/修饰预测 | 结论可能已部分过时 | 纳入AlphaFold3的对比分析 | 全文仅提及AlphaFold2/Multimer/ColabFold |
| "整合工作流"建议缺乏具体操作指南 | 未给出如何选择"何时信AI、何时信实验"的决策框架 | 对实践者帮助有限 | 提出基于pLDDT/PAE/局部分辨率的决策树或流程图 | Discussion; Future Perspectives |

---

## 14 对IDP/IDR×蛋白互作×AI课题的启示

### 直接相关结论
1. **AlphaFold对无序区的处理是公认短板**：本文明确将IDP/IDR列为AlphaFold的核心失效场景之一（pLDDT<50，输出静态片段化结构）。对IDP/IDR介导的互作研究，**不能将AlphaFold输出作为结构依据**，而应将其低置信度区域本身视为"无序或构象异质"的证据。
2. **弱/瞬时互作界面预测困难**：本文指出AlphaFold-Multimer在Hsp90-共伴侣、泛素-E2等弱互作复合物中常错配伙伴取向。IDP介导的互作多为弱亲和力、瞬时结合，**直接使用AlphaFold-Multimer预测IDP互作界面风险极高**。
3. **中等分辨率cryo-EM + AlphaFold的整合模式可迁移**：对于IDP/IDR系统，若能在cryo-EM/ET中捕获结合态构象（即使分辨率有限），AlphaFold可为有序区域提供起点模型，而密度图可约束无序区的空间分布——这种"部分有序+部分无序"的混合建模策略值得借鉴。

### 可迁移的方法论
4. **pLDDT作为无序区注释工具**：本文反复强调pLDDT<50对应无序/柔性区域。在IDP研究中，可将AlphaFold的pLDDT分布作为**计算预测器**，与实验无序注释（NMR化学位移、SAXS Kratky图等）交叉验证。
5. **"假设生成器"定位**：本文的核心主张——AlphaFold是假设生成器而非答案提供者——对IDP研究尤为重要。可将AlphaFold-Multimer对IDP互作的预测（即使低置信度）作为**候选界面假说**，再用交联质谱、突变分析、NMR滴定等实验验证。
6. **整合工作流设计**：本文展示的"AI预测 + 实验密度 + 生化验证"循环，可扩展为"AlphaFold预测 + cryo-EM/SAXS约束 + MD采样 + 实验验证"的IDP专用流程。

### 对物理模拟的启示 [Analysis]
7. 本文指出AlphaFold无法捕捉构象状态转换（如心肌粗丝中肌球蛋白头的三种状态），这为**MD模拟**提供了明确的应用空间：MD可以采样AlphaFold无法输出的构象 ensemble，而AlphaFold可以为MD提供初始结构或验证MD采样的合理性。对IDP/IDR系统，**MD（或增强采样方法）几乎是必需的补充**，因为AlphaFold无法提供无序区的构象分布。

---

## 15 与已有知识连接

- **AlphaFold原始文献**: Jumper et al. (2021) Nature, "Highly accurate protein structure prediction with AlphaFold"——本文的出发点，其局限（无序区、多聚体、配体）在本文中被系统验证。
- **AlphaFold-Multimer**: Evans et al. (2022) bioRxiv——本文讨论的复合物预测模式，其弱互作界面预测缺陷与IDP互作研究直接相关。
- **AlphaFold数据库**: Varadi et al. (2022) NAR——本文引用的"约三分之一残基未达原子精度"的出处。
- **cryo-ET原位结构**: 本文强调cryo-ET可捕捉原生状态下的组装，这与Beck & Baumeister (2016) 的cryo-ET综述一致。
- **IDP预测工具**: 本文未讨论IUPred、SPOT-Disorder等专用无序预测器，但pLDDT<50与无序区的对应关系可与此类工具交叉验证。
- **整合结构生物学**: 本文的"AI+实验"工作流主张与Rout & Sali (2019) 的整合建模框架一致。
- **MD模拟补充**: 本文建议MD用于构象采样，与Lindorff-Larsen et al. (2016) 对IDP的MD模拟研究形成互补。

---

## 16 研究想法

### 候选1: IDP互作界面的AlphaFold-Multimer系统性基准测试
- **来源**: 本文指出AlphaFold-Multimer在弱/瞬时互作中表现不佳（Discussion），但未提供量化数据
- **假设**: AlphaFold-Multimer对IDP介导的互作界面预测精度显著低于有序-有序互作，且pLDDT/IPA（ipTM）可作为预测可靠性的判别指标
- **方法**: 收集已知IDP互作复合物（如p53-MDM2、c-Myc-Max等），运行AlphaFold-Multimer，与实验结构/交联数据对比，建立"置信度-可靠性"映射
- **验证**: 与实验结合自由能数据、突变热点对比
- **创新状态**: unverified

### 候选2: pLDDT分布作为IDP/IDR的计算注释工具
- **来源**: 本文反复使用pLDDT<50作为无序区标志（Discussion）
- **假设**: AlphaFold的pLDDT逐残基分布与实验无序注释（NMR CS、SAXS）高度相关，可作为基因组规模的IDP注释工具
- **方法**: 在DisProt/IDEAL数据库上系统比较pLDDT与实验无序注释的ROC-AUC，与IUPred等专用工具对比
- **验证**: 独立测试集上的泛化性能
- **创新状态**: partially checked（已有零星报道，但缺乏系统比较）

### 候选3: 整合AlphaFold与增强采样MD的IDP构象ensemble生成
- **来源**: 本文指出AlphaFold无法捕捉构象状态转换（Fig. 5A），建议MD作为补充
- **假设**: 以AlphaFold预测的有序结构域为约束，对IDP区域进行增强采样MD（如REMD、GaMD），可生成与SAXS/FRET实验一致的构象ensemble
- **方法**: 对已知IDP系统（如α-synuclein、Tau），用AlphaFold预测+MD采样生成ensemble，与SAXS/FRET数据对比
- **验证**: ensemble平均SAXS曲线与实验的χ²拟合
- **创新状态**: unverified

### 候选4: 相分离驱动蛋白的AlphaFold预测与实验验证
- **来源**: 本文未直接讨论相分离，但其"无序区预测不可靠"的结论与相分离研究直接相关
- **假设**: 相分离驱动蛋白（含长IDR）的AlphaFold预测中，低pLD TT区域的空间分布与实验鉴定的互作基序（SLiMs）相关，可用于预测相分离热点
- **方法**: 对已知相分离蛋白（如FUS、TDP-43、hnRNPA1），分析AlphaFold pLDDT分布与已知SLiMs/修饰位点的共定位
- **验证**: 与体外相分离实验（浊度、FRAP）对比
- **创新状态**: unverified

### 候选5: cryo-ET + AlphaFold整合工作流在IDP复合物中的应用
- **来源**: 本文的核心主张——AI预测与cryo-ET密度图整合
- **假设**: 对于IDP介导的复合物，cryo-ET可在原生状态下捕获结合态构象，AlphaFold可为有序区域提供模型，两者整合可解析IDP在复合物中的空间分布
- **方法**: 选择代表性IDP复合物，收集cryo-ET数据，用AlphaFold预测亚基结构，进行柔性拟合
- **验证**: 与交联质谱、突变分析交叉验证
- **创新状态**: unverified