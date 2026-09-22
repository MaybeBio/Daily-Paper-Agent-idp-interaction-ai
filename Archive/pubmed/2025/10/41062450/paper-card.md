## 01 基本信息

- **标题**：PhaSepDB 3.0: a comprehensive knowledgebase of phase separation-related proteins from AI-assisted curation
- **作者与单位**：You, Kaiqiang; Li, Runyu; Lian, Ruixin; Li, Yuxuan; Yang, Hongzhining; Zhou, Yiran; Chen, Yangsheng; Wang, Likun; Fan, Zhaoqing; Ma, Liwei; Li, Tingting（单位未在摘要中提供）
- **期刊/预印本平台**：Nucleic Acids Research
- **年份**：2025
- **论文类型**：数据库资源（Database Resource）
- **领域**：生物信息学 / 相分离 / 知识库构建 / AI辅助文献挖掘
- **关键词**：phase separation, membraneless organelles, biomolecular condensates, knowledgebase, large language model, AI-assisted curation
- **DOI/arXiv 号**：10.1093/nar/gkaf973
- **代码**：https://doi.org/10.5281/zenodo.17052250（AI辅助策展工作流性能评估的代码与数据）
- **数据**：https://db.phasep.pro/（PhaSepDB 3.0 数据库）
- **阅读日期**：2025-04-26（基于DOI在线日期推断，实际阅读日期以读者为准）
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**：本文是该方向中「知识库/数据资源」类的重要更新，首次将LLM智能体系统引入相分离文献策展流程，为IDP/IDR相分离研究提供了大规模、深度注释的数据基础设施，是连接实验文献与AI预测模型的关键桥梁资源。

## 02 一句话总结

本文开发了一个LLM智能体系统与专家验证相结合的人机协同策展工作流，将PhaSepDB从2.1版扩展至3,484条实验验证条目（覆盖1,849个蛋白），并新增蛋白级汇总页面、功能关联注释和内在/外在调控信息，为相分离研究提供更全面、更深度的知识库资源。

## 03 研究问题

- **具体问题**：如何在大规模、快速增长的科学文献中，高效且准确地策展相分离相关蛋白的实验证据和深度注释？
- **为什么重要**：相分离领域文献量指数增长，传统纯人工策展不可持续；同时研究焦点从「哪些蛋白发生相分离」转向「相分离的生物学功能、调控机制和治疗意义」，需要更深度的注释框架。
- **现有方法为何不足**：传统人工策展速度慢、难以跟上文献增长；已有数据库（如PhaSepDB 2.1、LLPSDB等）注释深度有限，缺乏功能关联和调控信息的系统化捕获。
- **精确的「Can ... ?」研究问题**：Can an LLM-based agentic system, combined with expert verification, achieve sufficient accuracy and efficiency to enable large-scale, in-depth curation of phase separation-related proteins from scientific literature?

## 04 背景与发展脉络

**注：以下脉络基于本文引用和领域常识，标记为「经外部核验」部分基于公开领域知识，其余为「仅本文框架」。**

1. **早期阶段（~2018-2020）**：相分离概念兴起，首批数据库出现。代表性方法：PhaSepDB 1.0/2.x、LLPSDB等，主要收录「哪些蛋白发生相分离」的基础信息。优点：建立了领域数据基础；局限：注释深度有限，更新速度慢。
2. **中期阶段（~2020-2023）**：相分离功能研究深化，连接疾病和调控机制。代表性方法：PhaSepDB 2.1扩展、MloDisDB等。优点：增加了疾病关联和部分功能注释；局限：仍依赖纯人工策展，难以应对文献爆炸。
3. **AI辅助策展阶段（~2023-至今）**：LLM技术成熟，开始应用于科学文献挖掘。代表性方法：本文的LLM agentic system + 专家验证工作流。优点：大幅提升策展效率，支持更深度的注释框架；局限：AI输出仍需专家验证，初始提示工程需要标注数据集。
4. **本文主张的位置**：首次将LLM智能体系统系统性地应用于相分离知识库策展，实现「效率+深度」的双重突破，并建立可扩展的人机协同策展范式。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 文献量指数增长 | 2022.4-2025.4间新增2,386篇候选文献 | 相分离领域快速扩张，研究焦点从基础识别转向功能与调控 | Methods "Literature collection"节 |
| 传统人工策展不可持续 | 纯人工策展难以应对大规模文献 | 每篇文献需深度阅读和结构化提取，人力成本高 | Introduction "the exponentially increasing volume of literature makes traditional manual curation by experts unsustainable" |
| 注释深度不足 | 已有数据库缺乏功能关联、调控信息 | 研究焦点已从「哪些蛋白」转向「功能与调控机制」 | Introduction "The focus of research in this field has significantly evolved" |
| 数据异质性 | 文献中材料状态、功能域等报告缺乏标准化 | 领域缺乏统一实验报告标准 | Discussion "The lack of standardized experimental reporting in information such as material states and functional domain" |
| 知识碎片化 | 同一蛋白的多篇文献信息分散 | 缺乏蛋白级整合视图 | Results "protein-wise summary pages consolidate data from all relevant publications" |

## 06 核心思想

**1) 表面方法**：
构建一个三智能体（Data Extraction Agent → Data Formatting Agent → Protein-wise Summary Agent）的LLM智能体系统，以全文文献为输入，自动提取相分离相关蛋白及其注释信息，经两轮专家验证后入库。

**2) 核心洞察**：
- 将LLM从「信息提取工具」提升为「策展工作流中的协作者」，通过分工明确的智能体设计，实现从原始文本到结构化知识的自动化流水线。
- 「人机协同」而非「全自动」是关键：AI负责效率和广度，专家负责准确性和深度判断，两者互补。
- 蛋白级汇总页面解决了「同一蛋白多篇文献信息碎片化」的问题，将条目级数据整合为蛋白级知识。

**3) 可能的普适教训 [Analysis]**：
- 对于IDP/IDR相分离这类跨学科、文献量大、注释维度多的领域，LLM辅助策展是构建可持续知识库的有效范式。
- 智能体分工（提取→格式化→汇总）的设计模式可迁移至其他生物医学知识库的构建。
- 将「条目级」数据与「蛋白级」知识分层组织，是处理复杂生物现象数据的好架构。

## 07 方法总览

- **输入**：PubMed检索得到的2,386篇候选文献全文（检索式：'(phase transition[Title/Abstract] OR phase separation[Title/Abstract] OR membraneless organelles[Title/Abstract] OR biomolecular condensates[Title/Abstract]) AND protein AND cell'，时间范围2022.4.1-2025.4.20）+ PhaSepDB 2.1已有数据
- **输出**：PhaSepDB 3.0数据库（3,484条条目，1,849个蛋白），包含蛋白级汇总页面
- **核心模块**：
  1. **Data Extraction Agent**：从全文提取实验验证的相分离蛋白及属性
  2. **Data Formatting Agent**：将提取信息转换为预定义JSON格式
  3. **Protein-wise Summary Agent**：整合多文献信息生成蛋白级汇总
  4. **两轮专家验证**：每条目由两位不同专家独立审核
- **工具**：DeepSeek-V2 LLM（官方API）、CrewAI框架（智能体编排）、自定义Web策展工具
- **训练/验证**：PhaSepDB 2.1作为标注数据集；50篇文献作为提示工程验证集，382篇作为测试集
- **反馈回路**：专家审核意见记录在数据库，用于质量控制和追溯
- **假设**：LLM能从全文文献中准确提取相分离相关信息；专家验证能保证最终数据质量

**文字流程**：
PubMed文献检索 → 全文获取 → Data Extraction Agent提取蛋白及属性 → Data Formatting Agent结构化JSON → 专家两轮验证（Web工具）→ 入库 → Protein-wise Summary Agent生成蛋白级汇总 → 专家审核 → 发布至网站

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| Data Extraction Agent | 从全文提取实验验证的相分离蛋白及属性 | 自动化处理大规模文献，提取结构化信息 | 输入：全文文献；输出：Markdown格式提取结果 | Results "successfully extracted 91.5% of the entries in the validation set" | 策展效率大幅下降，无法应对文献量增长 |
| Data Formatting Agent | 将Markdown转换为预定义JSON格式 | 标准化数据，便于入库和后续处理 | 输入：Markdown提取结果；输出：JSON对象 | Methods "processes the information into a formatted JSON object" | 数据格式不统一，入库和查询困难 |
| Protein-wise Summary Agent | 整合多文献信息生成蛋白级汇总 | 解决知识碎片化，提供蛋白级全景视图 | 输入：某蛋白所有已批准条目；输出：蛋白级汇总文本 | Results "synthesizes findings from multiple publications" | 用户需自行整合多篇文献信息，效率低 |
| 两轮专家验证 | 审核AI输出，确保准确性和完整性 | AI输出需人工把关，保证数据库质量 | 输入：AI生成条目；输出：批准/修改/拒绝 | Results "experts approved over 80.0% of the entries" | 数据质量无法保证，错误信息可能入库 |
| 自定义Web策展工具 | 支持专家高效审核和编辑 | 提供并排比较界面，加速审核流程 | 输入：AI生成条目+原文；输出：审核后条目 | Supplementary Fig. S1 | 专家审核效率降低，人机协同流程受阻 |

**注**：消融实验未在摘要中提供，上述「移除后的影响」为基于模块功能的预期分析 [Analysis]。

## 09 关键公式符号

**不适用**。本文为数据库资源论文，未涉及数学模型或算法公式。核心「公式」是工作流设计而非数学表达。

## 10 实验设计与证据链

**数据集/群体**：
- 2,386篇候选文献（2022.4.1-2025.4.20 PubMed检索）
- 50篇验证集（提示工程优化）
- 382篇测试集（最终性能评估）
- PhaSepDB 2.1数据作为标注数据集

**指标**：
- 提取率（91.5%的验证集条目被成功提取）
- 关键注释准确率（organism, subcellular location, MLOs, PS-class, material state平均>70%）
- 专家批准率（>80.0%的AI生成条目获专家批准）

**基线**：PhaSepDB 2.1（数据量对比）

**评测协议**：AI提取结果与专家审核结果对比，计算一致性和准确率

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|------------|-----------|------|------------|------------------|------|
| 验证集提取测试 | LLM智能体能有效提取相分离条目 | 50篇文献，提示工程优化后 | 91.5%条目被成功提取 | 智能体系统具有高提取率 | 未报告精确率/召回率，91.5%可能包含部分提取 | Results "successfully extracted 91.5% of the entries" |
| 关键注释准确率评估 | 提取的注释信息准确 | 5类关键注释与专家判断对比 | 平均准确率>70% | 注释质量可接受 | 各类别准确率差异未报告，>70%对某些应用可能不够高 | Results "exceeded an average of 70%" |
| 专家批准率 | AI输出与专家判断高度一致 | 全部AI生成条目经两轮专家审核 | >80.0%条目获批准 | 人机协同工作流有效 | 20%被拒条目的错误类型和原因未分析 | Results "experts approved over 80.0% of the entries" |
| 数据量对比 | 数据库内容显著扩展 | PhaSepDB 3.0 vs 2.1 | 3,484条目/1,849蛋白，超2倍增长 | AI辅助策展显著提升产出 | 未报告精确的2.1版数据量 | Results "more than doubling the database's content" |

## 11 结论正确解读

- **任务范围**：本文的AI系统仅用于文献策展（信息提取和结构化），不涉及相分离预测、机制建模或实验验证。
- **Oracle/真值输入**：专家审核是最终真值来源，AI输出需经两轮人工验证；PhaSepDB 2.1作为训练/验证的标注数据。
- **端到端状态**：工作流已投入实际生产（数据库已发布），但AI系统本身不是端到端全自动——人类专家是流程中不可缺的环节。
- **算力成本**：未报告具体算力消耗，仅提及使用DeepSeek-V2 API和CrewAI框架。
- **历史数据依赖**：AI系统依赖PhaSepDB 2.1作为标注数据，其质量影响提示工程效果。
- **模型依赖**：使用DeepSeek-V2，未测试其他LLM的迁移性。
- **最难情况**：AI在提取准确率>70%的注释类别上仍有改进空间；20%被专家拒绝的条目说明AI输出存在系统性或随机性错误。
- **群体/领域边界**：检索策略限定特定关键词，可能遗漏未使用这些术语的相分离文献；数据库偏向实验验证的蛋白，计算预测的候选未纳入。
- **不确定性**：未报告AI提取错误的类型学分析、不同文献类型的表现差异、以及专家间一致性（inter-annotator agreement）。

**有边界的复述**：PhaSepDB 3.0通过LLM智能体+专家验证的工作流，在2022.4-2025.4的文献范围内，成功将数据库扩展至3,484条实验验证条目（1,849个蛋白），AI提取的条目中>80%获专家批准，关键注释平均准确率>70%。该数据库为相分离研究提供了深度注释资源，但其覆盖范围受检索策略和文献类型限制，数据质量依赖专家审核环节。

## 12 作者自认局限

在提供的材料（摘要）中，作者明确承认的局限如下：

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 数据异质性 | 文献中材料状态、功能域等信息缺乏标准化报告，影响数据统一性 | 利用AI能力促进标准化基准数据集的创建 | Discussion "The lack of standardized reporting...hinder the development of robust predictive models" |
| 数据统一性不足 | 数据异质性阻碍了稳健预测模型的开发 | 创建标准化基准数据集，用于训练和验证下一代预测算法 | Discussion "a promising future direction would be to leverage AI's capabilities to facilitate the creation of standardized benchmark datasets" |

**作者提及的相关约束**（非正式局限）：
- 检索策略限定特定关键词（Methods "Literature collection"节）
- 高计算资源依赖（Acknowledgements "supported by High-performance Computing Platform of Peking University"）

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 提取率91.5%但注释准确率仅>70% | 提取「条目」成功不等于提取「内容」准确；高提取率可能掩盖了部分条目的信息缺失或错误 | 用户依赖数据库注释做研究，注释错误会传导至下游分析和预测模型 | 按注释类别分层报告精确率/召回率；对错误条目做错误类型学分析 | Results "91.5% of the entries" vs "accuracy...exceeded an average of 70%" |
| 专家批准率>80%但未报告专家间一致性 | 不同专家可能有不同判断标准，>80%批准率可能反映的是AI与「某一位」专家的一致性 | 知识库质量取决于审核的可靠性，专家间分歧未量化则无法评估审核环节本身的可重复性 | 计算Cohen's kappa或Fleiss' kappa；报告分歧解决流程 | Results "experts approved over 80.0% of the entries" |
| 未报告AI系统在「负面案例」上的表现 | 系统可能漏报（false negative）了应纳入的蛋白，或误报（false positive）了无充分证据的蛋白 | 漏报影响数据库完整性，误报影响数据可靠性 | 在测试集上计算精确率和召回率；对未提取的蛋白做人工复核 | Methods "LLM-based Agentic System"节未提及负面案例评估 |
| 仅使用单一LLM（DeepSeek-V2） | 结果可能依赖特定模型能力，不同LLM的迁移性未知 | 若模型更新或替换，工作流的可重复性和输出一致性受影响 | 用多个LLM（GPT-4、Claude、Llama等）在相同测试集上对比 | Methods "employed the DeepSeek-V2 LLM" |
| 数据库覆盖偏向「热门」蛋白 | 高频研究的蛋白（如FUS、G3BP1）被多篇文献覆盖，而低频研究的蛋白可能仅1-2条记录 | 用户可能误将「文献数量」等同于「生物学重要性」 | 在网站提供文献覆盖度提示；区分「充分验证」与「初步证据」条目 | Results "proteins that are frequently studied and central to the field are extensively annotated" |
| 未报告AI策展与纯人工策展的「成本-收益」定量对比 | 虽然声称效率提升，但未量化节省的人力时间或增加的吞吐量 | 其他数据库项目需要评估是否值得采用类似工作流 | 对比AI+专家 vs 纯专家策展相同文献集的时间、成本和错误率 | Results "automated extraction by agents required less than five minutes per publication"（仅报告AI时间，未报告专家审核时间） |

## 14 学到什么

**Agent 提炼的知识候选**：

1. **LLM智能体工作流设计模式**：三智能体分工（提取→格式化→汇总）是可复制的架构。对于IDP/IDR相分离研究，可借鉴此模式构建「文献→结构化知识」的自动化pipeline，用于追踪特定蛋白家族的相分离证据。

2. **人机协同的「验证环节」设计**：两轮独立专家审核+Web工具并排比较，是保证AI输出质量的有效方案。在构建IDP/IDR相分离数据库或训练数据集时，应设计明确的「AI生成→人工验证」流程，而非完全自动化。

3. **蛋白级汇总页面的信息架构**：将「条目级」证据整合为「蛋白级」知识视图，解决了多文献信息碎片化问题。对于IDP/IDR研究，这种「从证据到综合」的呈现方式有助于快速获取某蛋白的相分离全貌。

4. **注释框架的深度分层**：本文的注释框架涵盖功能关联、内在决定因素（如IDR、PTM、突变）、外在调控（如伴侣、RNA、化学物质）等多维度。这为IDP/IDR相分离研究提供了「应该收集哪些信息」的参考模板。

5. **AI策展的「效率-准确率」权衡**：AI提取的注释准确率>70%但未达完美，提示在依赖AI生成的数据时需设置「置信度阈值」或「人工复核优先级」。对于IDP/IDR相分离预测模型的训练数据构建，建议对AI提取的数据做严格过滤。

6. **标准化数据报告的呼吁**：作者指出文献中材料状态、功能域等报告缺乏标准化，阻碍了预测模型开发。这提示IDP/IDR相分离领域需要社区层面的数据报告标准（如MIAPE-like标准），以支持AI模型的训练和验证。

## 15 与已有知识连接

- **PhaSepDB 2.1/1.0**（本文前序版本）：本文直接扩展了该数据库，新增AI辅助策展工作流和蛋白级汇总页面。用户可对比新旧版本的数据量和注释深度变化。
- **LLPSDB**（相分离数据库）：与PhaSepDB互补，LLPSDB侧重体外相分离实验数据，PhaSepDB侧重细胞/体内证据。两者结合可提供更全面的相分离证据链。
- **MloDisDB**（膜less细胞器疾病关联数据库）：与PhaSepDB 3.0的功能关联注释互补，可交叉验证疾病-相分离关联。
- **DeepSeek-V2**（LLM）：本文使用的AI模型，其能力边界直接影响提取质量。可关注后续版本或替代模型在生物医学文本挖掘中的表现。
- **CrewAI框架**（智能体编排）：本文使用的多智能体框架，可迁移至其他生物医学知识库构建场景。
- **AlphaFold/AlphaFold3**（结构预测）：PhaSepDB 3.0的蛋白注释（如IDR区域、突变）可与AlphaFold预测的结构结合，用于分析相分离热点区域的结构基础。
- **LLPS预测工具**（如catGRANUS、PhaSepPred等）：PhaSepDB 3.0的实验验证数据可作为这些预测工具的训练集或验证集，提升预测准确性。
- **[Analysis] 候选连接**：本文的「AI辅助策展」模式与「AI辅助科学发现」的宏观趋势一致，可参考材料科学、基因组学领域的类似工作（如LLM用于文献挖掘的其他案例）进行横向对比。

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**：IDR-PS-Bench：基于PhaSepDB 3.0的IDR相分离预测基准测试集
   - **来源局限/观察**：PhaSepDB 3.0提供了大量实验验证的相分离蛋白，但未提供统一的基准测试集用于评估IDR相分离预测工具。
   - **核心假设**：利用PhaSepDB 3.0的实验验证数据，可构建一个覆盖多物种、多MLO类型、含正负样本的IDR相分离预测基准，系统评估现有预测工具（如catGRANUS、PhaSepPred、FuzDrop等）的性能。
   - **相对本文的增量**：将数据库从「查询资源」转化为「评估平台」，填补IDR相分离预测领域缺乏标准化基准的空白。
   - **初步方法**：从PhaSepDB 3.0提取PS-self蛋白作为正样本，从人类蛋白组中选取无相分离证据的蛋白作为负样本；按物种、MLO类型、序列特征分层；评估各预测工具的AUC、Precision-Recall等指标。
   - **验证方式**：交叉验证、独立测试集验证、与已有benchmark（如CAID）对比。
   - **可能的失败模式**：负样本选择偏差（无证据≠不相分离）；数据库覆盖偏向热门蛋白导致样本不平衡。

2. **候选名称**：PS-Interactome：从PhaSepDB 3.0提取相分离蛋白互作网络
   - **来源局限/观察**：PhaSepDB 3.0记录了蛋白的「PS partner」信息（2,304条条目含蛋白伴侣），但未系统构建蛋白-蛋白互作网络。
   - **核心假设**：从PhaSepDB 3.0的partner信息可构建相分离蛋白互作网络，通过网络分析（hub、模块、motif）发现新的相分离调控机制和功能模块。
   - **相对本文的增量**：将「条目级」的partner信息升级为「网络级」的系统知识，揭示相分离蛋白的协同作用模式。
   - **初步方法**：从PhaSepDB 3.0提取所有PS-self和PS-other的partner关系；与STRING、BioGRID等互作数据库交叉验证；计算网络拓扑属性；识别与特定MLO或疾病相关的功能模块。
   - **验证方式**：网络鲁棒性分析、模块富集分析、与已知相分离调控通路对比。
   - **可能的失败模式**：partner信息来自不同实验条件，异质性高；网络稀疏性限制分析深度。

3. **候选名称**：AI-PS-Curator：面向IDP/IDR相分离文献的自动化策展工具
   - **来源局限/观察**：PhaSepDB 3.0的AI策展工作流需要专家验证，且仅针对相分离领域。IDP/IDR研究（如分子伴侣、翻译后修饰、突变效应）的文献策展仍依赖人工。
   - **核心假设**：将PhaSepDB 3.0的LLM智能体工作流泛化至IDP/IDR功能注释领域，可构建更广泛的IDP知识库。
   - **相对本文的增量**：将「相分离专用」的策展工具扩展为「IDP/IDR通用」的策展框架，覆盖更多功能维度。
   - **初步方法**：复用三智能体架构，扩展注释schema（如IDR长度、电荷分布、相互作用伙伴类型）；在IDP/IDR相关文献子集上微调提示；设计领域专家验证流程。
   - **验证方式**：与人工策展结果对比准确率和召回率；在独立文献集上测试泛化性。
   - **可能的失败模式**：IDP/IDR文献的术语多样性高于相分离领域，提取难度更大；专家验证成本可能成为瓶颈。

4. **候选名称**：PS-Mutation-Atlas：PhaSepDB 3.0驱动的相分离相关突变效应数据库
   - **来源局限/观察**：PhaSepDB 3.0注释了突变对相分离的影响，但未系统化整理为可查询的突变效应数据库。
   - **核心假设**：从PhaSepDB 3.0提取的突变-相分离效应数据，结合AlphaFold结构预测，可揭示突变影响相分离的结构机制，并用于训练突变效应预测模型。
   - **相对本文的增量**：将「定性注释」升级为「定量预测」的训练资源，连接数据库与AI预测。
   - **初步方法**：从PhaSepDB 3.0提取突变相关条目；注释突变类型、位置、效应方向（促进/抑制相分离）；结合AlphaFold预测的IDR区域和结构特征；训练突变效应分类器。
   - **验证方式**：与ClinVar、COSMIC等疾病突变数据库交叉验证；在已知相分离相关疾病突变上测试。
   - **可能的失败模式**：突变效应注释的粒度不一致；IDR区域的结构预测可靠性有限。

5. **候选名称**：PhaSep-Embed：基于PhaSepDB 3.0的蛋白相分离表示学习
   - **来源局限/观察**：PhaSepDB 3.0提供了丰富的相分离蛋白注释，但未利用这些数据训练蛋白序列的相分离专用表示。
   - **核心假设**：在PhaSepDB 3.0的蛋白序列和注释上微调蛋白质语言模型（如ESM-2、ProtTrans），可学习到相分离相关的序列特征，提升下游预测任务性能。
   - **相对本文的增量**：将数据库从「查询资源」转化为「预训练数据」，为IDP/IDR相分离预测提供专用表示。
   - **初步方法**：收集PhaSepDB 3.0的蛋白序列和相分离标签；在ESM-2等模型上做对比学习微调；在下游任务（相分离预测、IDR注释）上评估。
   - **验证方式**：与通用蛋白质语言模型对比下游任务性能；消融实验验证数据规模影响。
   - **可能的失败模式**：相分离标签的噪声（实验条件差异）影响表示质量；数据量不足以支持大规模预训练。