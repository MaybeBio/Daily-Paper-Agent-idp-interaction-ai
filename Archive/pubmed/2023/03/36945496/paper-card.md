## 01 基本信息
- **标题**: Exploring the evolution and function of Canoe's intrinsically disordered region in linking cell-cell junctions to the cytoskeleton during embryonic morphogenesis
- **作者**: Gurley, Noah J; Szymanski, Rachel A; Dowen, Robert H; Butcher, T Amber; Ishiyama, Noboru; Peifer, Mark
- **单位**: 未提供（推测为 University of North Carolina at Chapel Hill，基于作者 Peifer, Mark 的已知 affiliation，但原文未明确）
- **期刊/平台**: bioRxiv (preprint server for biology)
- **年份**: 2023
- **论文类型**: 预印本（未经同行评审）
- **领域**: 发育生物学、细胞生物学、蛋白进化
- **关键词**: 无序蛋白区域 (IDR)、黏附连接 (adherens junctions)、细胞骨架、形态发生、进化、Canoe/Afadin
- **DOI/arXiv**: 10.1101/2023.03.06.531372
- **代码**: 未提供
- **数据**: 全基因组测序数据（未提供 accession 号）；AlphaFold 结构预测（来自 AlphaFold DB）
- **阅读日期**: 2026-05-13（当前日期）
- **在课题方向中的位置**: 本文以果蝇 Canoe（Afadin 同源物）为模型，系统研究了 IDR 的进化保守性、序列特征与功能关联，属于「IDP/IDR 介导的蛋白互作」方向，但未涉及相分离/凝聚体，也未使用 AI 方法（仅用 AlphaFold 预测结构作为辅助工具）。对本课题的可迁移价值在于：提供了 IDR 进化分析的方法框架、IDR 内保守基序与已知结合位点的对应关系，以及 IDR 截短突变体的表型分析策略。

## 02 一句话总结
本文通过生物信息学分析和一系列携带早熟终止密码子的 canoe 突变体，揭示了 Canoe/Afadin 的 C 端 IDR 在序列和组成上快速进化，但其中包含多个保守基序（部分被 AlphaFold 预测为 α-螺旋），这些基序对应已知的 α-catenin 和 F-actin 结合位点，且 IDR 的完整性对胚胎形态发生中细胞连接-细胞骨架的稳固连接至关重要。

## 03 研究问题
- **具体问题**: Canoe/Afadin 的 C 端 IDR 在进化中如何变化？IDR 内的哪些序列特征/基序是保守的？这些保守基序是否对应已知功能（如蛋白结合）？IDR 的不同区域对 Canoe 在胚胎形态发生中的功能贡献如何？
- **为什么重要**: IDR 在信号蛋白和支架蛋白中普遍存在，但对其进化约束和功能意义的理解远不如折叠结构域。Canoe/Afadin 是连接黏附连接到肌动蛋白细胞骨架的关键蛋白，其 IDR 占蛋白近一半长度，理解 IDR 的进化与功能关系对揭示这类「复杂多功能蛋白」的作用机制至关重要。
- **现有方法不足**: 传统结构域分析（如 CDD）无法注释 IDR 内的功能元素；简单的序列比对在长进化距离下无法检测 IDR 的保守性；已有的 IDR 功能研究多集中在体外生化实验，缺乏体内功能验证。
- **精确研究问题 (Can...?)**: Can 进化上保守的 IDR 内基序（特别是 AlphaFold 预测的 α-螺旋区域）被用作蛋白-蛋白相互作用位点，并且这些位点的完整性对胚胎形态发生中 Canoe 的功能是必需的？

## 04 背景与发展脉络
- **阶段一：IDR 的发现与基本特征描述**（约 2000-2010）
  - 代表性工作：Dunker, Uversky 等建立 IDP/IDR 概念，指出其缺乏稳定三级结构但具有重要功能
  - 优点：建立了 IDR 的序列-功能关系框架
  - 局限：多为生物信息学预测，缺乏系统体内功能验证
- **阶段二：IDR 在信号复合物组装中的作用**（约 2010-2020）
  - 代表性工作：对 Src 家族激酶、TCR 信号复合物等的研究，揭示 IDR 通过多价弱相互作用介导凝聚体形成
  - 优点：建立了 IDR 介导多价互作和相分离的概念
  - 局限：多集中在体外重构系统，体内证据有限
- **阶段三：IDR 的进化分析与功能基序鉴定**（约 2015-至今）
  - 代表性工作：对酵母、果蝇等模式生物的 IDR 进化分析，发现 IDR 快速进化但保留特定理化性质
  - 优点：将进化约束作为功能重要性的指标
  - 局限：多数研究停留在序列层面，缺乏与体内功能的直接关联
- **本文位置**: 本文属于阶段三的延伸，将 IDR 进化分析与经典遗传学（突变体表型）结合，首次系统地将 Canoe IDR 的进化保守基序与已知/预测的结合位点对应，并用体内功能数据支持 IDR 的功能重要性。该方法框架可直接迁移到其他 IDR 介导的蛋白互作研究。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| IDR 序列快速进化导致难以检测保守性 | 果蝇与人类 Canoe/Afadin 的 IDR 无显著序列相似性 | IDR 通常不受折叠约束，序列可快速漂移 | Results 节 "The IDRs of Drosophila Cno and human Afadin have diverged..."；Blast 搜索无显著匹配 |
| 传统结构域注释无法覆盖 IDR 功能元素 | CDD 数据库仅注释折叠结构域，IDR 内无已知结构域 | IDR 缺乏稳定结构，难以用传统方法定义功能单元 | Results 节 "In some cases, the folded domain predictions included additional structural elements not contained in the CDD domain definition" |
| IDR 内结合位点的实验定位困难 | 不同研究组对 F-actin 结合位点的定位不一致 | 缺乏高分辨率结构，生化实验受限于蛋白片段设计 | Discussion 节 "The initial mapping of the F-actin binding region of Afadin used radioactively-labeled F-actin in a blot overlay assay"；不同研究组结果不一致 |
| 早熟终止密码子突变体的功能解释复杂 | 截短蛋白可能触发无义介导的 mRNA 降解，导致功能缺失而非结构域特异性效应 | 无法区分「蛋白缺失」与「特定区域功能缺失」 | Discussion 节 "Many early stop codons trigger nonsense-mediated mRNA decay" |
| 母源与合子贡献的区分困难 | 母源提供的 Canoe 蛋白掩盖合子突变体的早期表型 | 母源 mRNA/蛋白在胚胎早期持续存在 | Results 节 "Maternally contributed Cno persists until late in embryonic morphogenesis" |

## 06 核心思想
1. **表面方法**: 结合生物信息学（序列比对、AlphaFold 结构预测）与经典遗传学（18 个 canoe 突变体的表型分析），系统研究 IDR 的进化与功能。
2. **核心洞察**: IDR 虽然在整体序列上快速进化，但其中嵌入了多个短保守基序，这些基序被 AlphaFold 预测为 α-螺旋，且与已知的蛋白结合位点（α-catenin、F-actin）精确对应。IDR 的 N 端部分（含 α-catenin 结合位点）对功能至关重要，而 C 端 FAB 区域虽非必需但起支持作用。
3. **可能的普适教训 [Analysis]**: IDR 的功能可能通过「短线性基序 + 局部结构倾向」实现，而非整体序列保守。AlphaFold 预测的 IDR 内螺旋区域可作为功能候选位点的高效筛选工具。进化分析（短进化距离）与结构预测的结合是 IDR 功能研究的有效策略。

## 07 方法总览
- **输入**: 
  - 蛋白序列：果蝇 Canoe、人类 Afadin 及多种昆虫/脊椎动物同源物
  - 突变体：18 个 canoe 等位基因（含早熟终止密码子）
  - 结构预测：AlphaFold DB 中 Canoe/Afadin 的预测结构
- **输出**: 
  - IDR 进化速率、序列组成差异的定量描述
  - 保守基序的定位与功能注释
  - 各突变体的表型严重程度分级
- **模块**:
  1. 序列比对与进化分析（Clustal Omega）
  2. 无序性预测（D2P2 数据库）
  3. 结构预测（AlphaFold DB）
  4. 突变体鉴定（全基因组测序 + Sanger 验证）
  5. 表型分析（胚胎角质层、形态发生）
  6. 蛋白定位分析（免疫荧光）
- **训练**: 不适用（无机器学习模型训练）
- **工具**: Clustal Omega, D2P2, AlphaFold DB, AlphaFold-Multimer (ColabFold), BWA/FreeBayes/GATK/snpEff（突变鉴定）
- **反馈回路**: 表型严重程度与突变位置（IDR 内 vs 外）的关联分析
- **假设**: 
  - 保守基序（特别是 AlphaFold 预测的螺旋）具有功能重要性
  - 早熟终止密码子导致的截短蛋白（若未被降解）可反映缺失区域的功能
  - 角质层表型可反映形态发生中细胞连接-细胞骨架耦联的完整性

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| IDR 进化分析 | 比较果蝇与人类 IDR 的序列、组成、电荷差异 | 确定 IDR 的进化约束程度 | 输入：同源蛋白序列；输出：序列一致性、组成偏好、电荷分布 | Results 节 "The IDRs of Drosophila Cno and human Afadin have diverged..." | 无法量化 IDR 的进化动态，无法识别保守基序 |
| 保守基序鉴定 | 在短进化距离内识别 IDR 中的保守序列块 | 定位潜在功能位点 | 输入：多种昆虫/脊椎动物 IDR 序列；输出：保守基序列表 | Results 节 "Comparisons of IDRs reveals strong sequence conservation over shorter evolutionary distances" | 无法将 IDR 功能与特定序列元素关联 |
| AlphaFold 结构预测 | 预测 IDR 内局部结构倾向（α-螺旋） | 将保守基序与结构特征关联 | 输入：Canoe/Afadin 全长序列；输出：预测结构及 pLDDT 分数 | Results 节 "In both cases, the full set of known domains... were clearly included in the predictions" | 无法识别 IDR 内可能的功能性结构元素 |
| AlphaFold-Multimer 对接 | 预测 α-catenin 与 Afadin 的结合界面 | 验证保守基序是否为结合位点 | 输入：Afadin 肽段 + α-catenin M3 结构域；输出：预测复合物结构 | Results 节 "We used AlphaFold-Multimer... to predict heterodimeric structures" | 无法从结构层面支持保守基序的功能注释 |
| 突变体鉴定与表型分析 | 将 IDR 内突变与功能缺失关联 | 提供 IDR 功能的体内证据 | 输入：18 个 canoe 等位基因；输出：角质层表型评分 | Results 节 "The zygotic phenotype of the original cno mutant..." | 无法评估 IDR 的体内功能贡献 |
| 母源/合子突变体区分 | 分离母源与合子贡献 | 准确评估合子突变体的表型 | 输入：遗传杂交方案；输出：母源/合子突变体胚胎 | Results 节 "Maternally contributed Cno persists until late in embryonic morphogenesis" | 无法区分母源与合子效应，表型解释可能偏差 |

## 09 关键公式符号
不适用。本文无数学公式或统计模型。所有分析为描述性统计（序列一致性百分比、表型评分分布）和结构预测（pLDDT、pTM、ipTM 分数），无需要推导的公式。

## 10 实验设计与证据链
- **数据集/群体**: 
  - 序列数据：果蝇 Canoe、人类 Afadin、多种昆虫（果蝇近缘种、家蝇、蕈蚊、蝴蝶）和脊椎动物（斑马鱼、非洲爪蟾、鸡、小鼠、人等）同源物
  - 突变体：18 个 canoe 等位基因（来自 Nüsslein-Volhard/Wieschaus 筛选和 Gaul/van Aelst 实验室）
  - 胚胎：果蝇胚胎（角质层制备、免疫荧光）
- **规模**: 18 个等位基因，每个至少 100 个胚胎的角质层评分；免疫荧光每组 5-6 个胚胎
- **指标**: 
  - 序列一致性（% identity）
  - 氨基酸组成偏好（% 特定残基）
  - 电荷（% charged residues）
  - 角质层表型评分（0-5 级）
  - 蛋白定位（连接处富集程度）
- **基线**: 野生型胚胎（角质层完整、头包内陷正常）；cnoR2（蛋白 null）作为完全功能缺失对照
- **预算**: 未提供
- **骨干/仪器**: 共聚焦显微镜（Zeiss LSM 880）；全基因组测序（BGI DNBseq）
- **oracle 输入**: 不适用（无机器学习）
- **评测协议**: 角质层表型盲评（n≥100/基因型）；免疫荧光定量（连接处 vs 细胞质强度比）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| IDR 序列比对（果蝇 vs 人类） | IDR 序列不保守 | 全长蛋白比对，聚焦 IDR 区域 | 无显著相似性；IDR 长度差异 132 aa；组成差异大 | IDR 整体序列快速进化 | 不能排除 IDR 内存在短保守基序 | Results 节 "The IDRs of Drosophila Cno and human Aficano have diverged..." |
| 短进化距离比对（昆虫/脊椎动物） | IDR 内存在保守基序 | 果蝇属内、双翅目内、昆虫纲内、脊椎动物内分别比对 | 鉴定出多个保守基序，部分与已知结合位点重叠 | IDR 内存在进化约束的短序列元素 | 保守基序不一定都有功能 | Results 节 "Comparisons of IDRs reveals strong sequence conservation..." |
| AlphaFold 结构预测 | IDR 内存在 α-螺旋 | 检查 Canoe/Afadin 全长预测结构 | 多个预测螺旋，其中 2-3 个位于 FAB 区域 | 保守基序可能形成局部结构 | 预测结构需实验验证 | Results 节 "In both cases, the full set of known domains..." |
| AlphaFold-Multimer 预测 α-catenin 结合 | 保守螺旋是 α-catenin 结合位点 | Afadin 1400-1460 + α-catenin M3 | 高置信度复合物模型，界面与已知结合位点一致 | 该保守螺旋介导 α-catenin 结合 | 预测需生化验证 | Results 节 "We used AlphaFold-Multimer..." |
| 18 个等位基因角质层表型 | IDR 突变影响形态发生 | 各等位基因 vs 野生型 vs cnoR2 null | 表型严重程度与突变位置相关；IDR 早期截短表型最强 | IDR 对 Canoe 功能至关重要 | 无法区分蛋白稳定性 vs 功能缺失 | Results 节 "The zygotic phenotype of the original cno mutant..." |
| 母源/合子突变体比较 | 母源 Canoe 掩盖合子表型 | cnoR2 合子突变 vs 母源/合子突变 | 母源/合子突变表型更严重 | 母源 Canoe 持续至晚期形态发生 | 母源蛋白的精确功能域未定义 | Results 节 "Maternally contributed Cno persists until late in embryonic morphogenesis" |
| sdk 遗传互作 | 背景基因影响表型 | cnoR2 vs sdk;cnoR2 | sdk 缺失增强 cno 表型 | 遗传背景可修饰 cno 表型 | 互作机制未阐明 | Results 节 "Loss of Sdk enhances the cno null zygotic phenotype..." |

## 11 结论正确解读
- **任务范围**: 本文仅研究果蝇胚胎形态发生中 Canoe 的功能，未涉及成体组织、其他物种或体外生化活性。
- **oracle/真值输入**: 无机器学习，无 oracle。突变体鉴定依赖全基因组测序和 Sanger 验证，表型评分依赖角质层形态。
- **端到端状态**: 非端到端。研究是「序列分析 → 突变体表型 → 功能推断」的链条，但未直接证明 IDR 的分子机制（如是否介导相分离）。
- **算力成本**: 未提供。AlphaFold 预测来自公共数据库，无自建模型。
- **历史数据依赖**: 依赖公共数据库（NCBI, AlphaFold DB, D2D2）和已有文献中的结合位点信息。
- **模型依赖**: 不适用。
- **最难情形**: IDR 内突变体的表型解释受限于无义介导的 mRNA 降解可能性；无法区分「截短蛋白无功能」与「截短蛋白显性负效应」。
- **群体/领域边界**: 结论仅适用于果蝇 Canoe 和脊椎动物 Afadin 的 IDR，不能推广到所有 IDR。
- **不确定性**: 作者明确表示无法确定 IDR 内保守基序是否都直接参与蛋白互作；F-actin 结合位点的精确定位存在争议。
- **有边界的复述**: 在果蝇胚胎形态发生中，Canoe 的 C 端 IDR 包含多个进化保守的短基序，其中部分被 AlphaFold 预测为 α-螺旋，且与已知的 α-catenin 和 F-actin 结合位点对应；IDR 的完整性对 Canoe 功能至关重要，但 IDR 内不同区域的功能贡献不同，N 端部分（含 α-catenin 结合位点）比 C 端 FAB 区域更为关键。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 无法区分截短蛋白的稳定性 | 早熟终止密码子可能触发无义介导的 mRNA 降解，导致无法确定表型是「蛋白缺失」还是「特定区域功能缺失」 | 工程化产生稳定截短蛋白的等位基因 | Discussion 节 "Many early stop codons trigger nonsense-mediated mRNA decay" |
| F-actin 结合位点定位存在争议 | 不同研究组对 Afadin F-actin 结合区域的定位不一致 | 需要更精确的生化实验和结构信息 | Discussion 节 "The initial mapping of the F-actin binding region..." |
| 母源 Canoe 的持续存在限制表型分析 | 母源蛋白掩盖早期合子突变体的表型 | 使用母源/合子双突变体或条件性敲除 | Results 节 "Maternally contributed Cno persists until late in embryonic morphogenesis" |
| 遗传背景影响表型 | sdk 缺失可增强 cno 表型，提示背景基因可能混淆等位基因比较 | 在相同遗传背景下重做等位基因比较 | Results 节 "Loss of Sdk enhances the cno null zygotic phenotype..." |
| IDR 内保守基序的功能未逐一验证 | 仅通过序列保守性和位置对应推断功能 | 需要逐一突变基序进行功能测试 | Discussion 节 "It will be important to directly test whether this set of conserved motifs in Cno binds actin" |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|-----------------|----------------------|----------|----------|------|
| AlphaFold 预测的 IDR 内螺旋可能不代表真实结构 | AlphaFold 对 IDR 的预测可靠性有限，pLDDT 分数通常较低 | 若螺旋是预测伪影，则「保守基序=结构元件」的推断不成立 | 用圆二色谱或 NMR 验证 IDR 片段的二级结构 | Results 节 "In both cases, the full set of known domains... were clearly included in the predictions"；未提供 pLDDT 具体分数 |
| 保守基序与已知结合位点的对应可能只是巧合 | 已知结合位点本身是通过保守性鉴定的，存在循环论证风险 | 需要独立证据（如突变破坏结合）确认因果关系 | 对保守基序进行点突变，检测与 α-catenin/F-actin 的结合变化 | Results 节 "Strikingly, this region precisely matches the first AlphaFold predicted alpha-helix" |
| 角质层表型评分可能受母源蛋白影响 | 母源 Canoe 持续至晚期，合子突变体的表型可能低估 | 表型严重程度与突变位置的关联可能被母源效应混淆 | 使用母源/合子双突变体重新评分 | Results 节 "Maternally contributed Cno persists until late in embryonic morphogenesis" |
| 18 个等位基因的突变位置与表型关联未做统计检验 | 表型差异可能由突变体遗传背景差异而非突变位置导致 | 需要控制遗传背景或使用等位基因系列 | 在相同遗传背景下重做等位基因比较 | Results 节 "Loss of Sdk enhances the cno null zygotic phenotype" 提示背景效应 |
| IDR 功能可能不依赖保守基序，而是依赖整体物理化学性质 | 作者未测试 IDR 的相分离能力或凝聚体形成 | 如果 IDR 通过相分离发挥功能，则保守基序可能只是「钉子」，整体性质才是「胶水」 | 测试 IDR 是否介导相分离，比较不同物种 IDR 的相分离能力 | Discussion 节未提及相分离；IDR 组成差异大（电荷、疏水性） |

## 14 学到什么
**Agent 提炼的知识候选**：
1. **IDR 进化分析框架**: 在长进化距离下 IDR 序列不保守时，可在短进化距离（如属内、科内）鉴定保守基序，再通过跨物种比较验证其功能重要性。可迁移到其他 IDR 介导的互作研究。
2. **AlphaFold 预测作为 IDR 功能位点筛选工具**: 即使 IDR 整体无序，AlphaFold 预测的局部螺旋区域往往对应已知结合位点。可用于快速筛选候选功能基序。
3. **IDR 内保守基序与结合位点的对应关系**: 保守基序（特别是预测螺旋）是 IDR 功能的关键「锚点」，即使整体序列快速进化。这提示 IDR 的功能可能通过「短基序 + 局部结构」实现。
4. **突变体表型分析的策略**: 利用早熟终止密码子突变体系列，结合表型严重程度与突变位置的关联，可初步定位功能关键区域。但需注意无义介导降解的混淆效应。
5. **母源贡献的处理**: 在胚胎发育研究中，母源蛋白的持续存在会掩盖合子突变体的早期表型，需使用母源/合子双突变体或延时观察。
6. **遗传背景的干扰**: 非致死突变（如 sdk）可增强表型，提示遗传背景是表型比较的重要变量。

## 15 与已有知识连接
- **Canoe/Afadin 功能**: 已知 Canoe/Afadin 通过 RA 结构域结合 Rap1，通过 PDZ 结构域结合 nectin/Neurexin，通过 C 端区域结合 α-catenin 和 F-actin（参考文献 3-6, 19-22）。本文进一步细化了 IDR 内的保守基序与这些结合位点的对应关系。
- **IDR 进化**: 与 Dunker 等关于 IDR 快速进化的观点一致，但本文补充了「短保守基序」的存在，与 Davey 等关于 SLiMs 的研究呼应。
- **AlphaFold 在 IDR 研究中的应用**: 与近期多项工作一致，AlphaFold 预测的 IDR 内螺旋可作为功能位点候选（如 Ruff & Pappu 2021 的讨论）。
- **黏附连接-细胞骨架耦联**: 与 Yonemura 等关于 α-catenin 力敏感性的工作相关，本文的 IDR 保守基序可能参与力传导。
- **相分离**: 本文未涉及相分离，但 IDR 的组成差异（电荷、疏水性）提示其可能具有相分离能力，与 Banani 等的框架一致。可进一步测试 Canoe IDR 是否介导凝聚体形成。
- **候选方向**: 将本文的进化分析框架应用于其他连接蛋白（如 Vinculin、ZO-1）的 IDR，或测试 Canoe IDR 的相分离能力。

## 16 研究想法
**Agent 生成的研究候选**：

1. **候选名称**: Canoe IDR 相分离能力及其在黏附连接力学传导中的作用
   - **来源局限/观察**: 本文发现 Canoe IDR 组成在果蝇与人类间差异大（电荷、疏水性），但未测试相分离；IDR 内保守基序可能只是「锚点」，整体性质可能介导凝聚体形成。
   - **核心假设**: Canoe IDR 通过相分离形成凝聚体，富集 α-catenin 和 F-actin，增强黏附连接在力学载荷下的稳定性。
   - **初步方法**: 纯化 Canoe IDR 片段，体外测试相分离（浊度、荧光恢复）；在果蝇胚胎中表达 IDR 突变体，观察凝聚体形成与形态发生表型的关联。
   - **验证方式**: 突变 IDR 中预测的相分离驱动区域（如电荷块），检测凝聚体消失与表型增强。
   - **可能的失败模式**: IDR 可能不介导相分离，而是通过其他机制（如增强局部浓度）发挥功能。
   - **创新状态**: unverified

2. **候选名称**: 跨物种 IDR 替换实验：Canoe IDR 的功能保守性测试
   - **来源局限/观察**: 本文显示 Canoe 与 Afadin 的 IDR 序列不保守，但保守基序存在。未测试跨物种 IDR 是否功能互换。
   - **核心假设**: 即使序列不保守，果蝇 Canoe IDR 被人类 Afadin IDR 替换后仍能支持胚胎形态发生，表明 IDR 功能依赖整体性质而非特定序列。
   - **初步方法**: 利用 CRISPR 将果蝇 canoe 内源 IDR 替换为人类 Afadin IDR，评估胚胎存活率、角质层表型、蛋白定位。
   - **验证方式**: 若替换后功能正常，则支持「整体性质保守」假说；若功能丧失，则支持「特定基序必需」假说。
   - **可能的失败模式**: 替换后蛋白表达量或稳定性改变，混淆功能评估。
   - **创新状态**: unverified

3. **候选名称**: 机器学习预测 IDR 内功能性基序：以 Canoe/Afadin 为训练集
   - **来源局限/观察**: 本文通过进化保守性 + AlphaFold 预测鉴定基序，但方法依赖多序列比对，对快速进化的 IDR 可能失效。
   - **核心假设**: 利用已知功能的 IDR 基序（如 SLiMs 数据库）训练分类器，可预测新 IDR 中的功能位点，无需依赖序列保守性。
   - **初步方法**: 收集已知 IDR 结合位点（ELM 数据库），提取序列特征（组成、电荷、预测结构），训练随机森林或深度学习模型；在 Canoe/Afadin IDR 上测试预测精度。
   - **验证方式**: 预测的基序与本文保守基序重叠率；突变预测基序后功能丧失。
   - **可能的失败模式**: 训练数据不足，模型泛化能力差。
   - **创新状态**: unverified

4. **候选名称**: IDR 内保守基序的共进化分析：Canoe 与 α-catenin/F-actin 的协同进化
   - **来源局限/观察**: 本文发现保守基序对应已知结合位点，但未分析结合伴侣的共进化。
   - **核心假设**: Canoe IDR 内保守基序与 α-catenin/F-actin 的结合界面存在共进化信号，可用于预测新的结合位点。
   - **初步方法**: 收集多物种 Canoe/Afadin 和 α-catenin/F-actin 序列，使用共进化分析（如 EVcouplings）检测 IDR 基序与结合伴侣的协同变异。
   - **验证方式**: 共进化预测的残基对与已知结构/生化数据重叠；突变共进化残基后结合亲和力变化。
   - **可能的失败模式**: IDR 与折叠蛋白的共进化信号弱，难以检测。
   - **创新状态**: unverified

5. **候选名称**: 力传导中 Canoe IDR 的构象变化：分子动力学模拟
   - **来源局限/观察**: 本文提出 IDR 内保守基序可能参与力学传导，但未提供分子机制。
   - **核心假设**: 在拉伸力下，Canoe IDR 的预测螺旋区域发生构象转变，暴露 α-catenin 或 F-actin 结合位点，增强连接强度。
   - **初步方法**: 使用粗粒化或全原子 MD 模拟 Canoe IDR 在力载荷下的构象变化；结合 FRET 实验验证。
   - **验证方式**: 模拟预测的构象变化与实验 FRET 信号一致；突变螺旋区域后力学响应改变。
   - **可能的失败模式**: IDR 模拟采样不足，力载荷条件难以模拟生理环境。
   - **创新状态**: unverified