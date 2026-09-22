## 01 基本信息
- **标题**：Protein SUMOylation promotes cAMP-independent EPAC1 activation
- **作者**：Yang, Wenli; Mei, Fang C; Lin, Wei; White, Mark A; Li, Li; Li, Yue; Pan, Sheng; Cheng, Xiaodong
- **单位**：未提供（根据通讯作者 Cheng Xiaodong 推测为 University of Texas Health Science Center at Houston，但原文未明确列出全部单位）
- **期刊/平台**：Cellular and Molecular Life Sciences (CMLS)
- **年份**：2024
- **论文类型**：原创研究论文
- **领域**：细胞信号转导；蛋白质翻译后修饰（SUMO化）；cAMP信号通路；EPAC1鸟苷酸交换因子
- **关键词**：SUMOylation; EPAC1; cAMP; Rap GTPase; Biomolecular condensate; Molecular dynamics
- **DOI/arXiv**：10.1007/s00018-024-05315-y
- **代码**：未提供
- **数据**：质谱数据（LC/MS/MS）已提交，但未提供公开数据库编号；分子动力学模拟参数见 Methods 节
- **阅读日期**：2026-05-13
- **在该课题方向中的位置**：本文直接涉及 **IDR/IDP 介导的蛋白互作 × 相分离/凝聚体** 与 **翻译后修饰（SUMO化）** 的交叉。EPAC1 含 intrinsically disordered regions（IDRs），其 SUMO化修饰发生在 RA 结构域（K561），且 SUMO 修饰促进 EPAC1 与 Rap1/2 的互作。本文同时使用 **分子动力学（MD）模拟** 解析 SUMO 修饰对蛋白互作界面的影响，属于「物理模拟 × 蛋白互作」范畴。对 IDP/IDR 课题的可迁移点：SUMO 作为可逆修饰如何通过改变互作界面（而非仅改变构象）调控 IDR 蛋白的凝聚体形成与下游信号。

## 02 一句话总结
本文通过质谱鉴定 EPAC1 的 K561 为 SUMO 化位点，证明热休克通过 SUMO 化修饰 EPAC1 的 RA 结构域（不依赖 cAMP），增强 EPAC1 与 Rap1/2 的互作界面（埋藏表面积从 1486 Å² 增至 2227 Å²），从而以 cAMP 非依赖方式激活 Rap GTPase。

## 03 研究问题
- **具体问题**：EPAC1 是否可以被 SUMO 化修饰？SUMO 化是否以及如何影响 EPAC1 的鸟苷酸交换活性（GEF 活性）？该修饰是否依赖 cAMP？
- **为什么重要**：EPAC1 是 cAMP 的主要效应蛋白之一，参与多种生理/病理过程。SUMO 化与 cAMP 信号是两条独立的应激响应通路，二者是否存在交叉尚不清楚。若 SUMO 化能独立于 cAMP 激活 EPAC1，则提供了一条新的信号整合机制。
- **现有方法为何不足**：此前研究未能成功检测到 EPAC1 的 SUMO 化，可能因为内源 SUMO 化水平极低且高度动态；缺乏有效的富集和质谱鉴定策略。
- **精确的 Can 问题**：Can SUMOylation of EPAC1 at K561 activate its GEF activity toward Rap1/2 in a cAMP-independent manner?

## 04 背景与发展脉络
- **阶段一：SUMO 化作为应激响应修饰**（~2000s 至今）：SUMO 化被广泛认为参与应激响应、DNA 修复、转录调控等。代表性方法：SUMO 化预测工具（如 JASSA）、SUMO 突变体（如 SUMO3 Q89K）辅助质谱鉴定。局限：内源 SUMO 化底物鉴定困难，动态性高。
- **阶段二：EPAC 信号通路研究**（~1998 至今）：EPAC1/2 作为 cAMP 效应蛋白被发现，GEF 活性激活 Rap1/2。代表性方法：Rap-GTP pull-down、cAMP 类似物（如 8-CPT-2Me-cAMP）。局限：主要关注 cAMP 依赖的激活机制，对翻译后修饰（除磷酸化外）研究较少。
- **阶段三：相分离/凝聚体与信号整合**（~2018 至今）：本课题组前期发现 cAMP/EPAC1 通过促进 SUMO 机器凝聚体形成增强细胞 SUMO 化（[17]）。本文在此基础上反向探索：EPAC1 本身是否也是 SUMO 底物。
- **本文主张的位置**：首次证明 EPAC1 是 SUMO 底物，且 SUMO 化直接增强其 GEF 活性，形成「cAMP → EPAC1 → SUMO 化机器凝聚体 → EPAC1 SUMO 化 → Rap 激活」的正反馈/交叉放大环路。
- **脉络核验状态**：以上脉络基于本文引言与讨论，部分经外部文献核验（如 SUMO 化应激响应、EPAC 发现史），但「EPAC1 此前未被成功检测到 SUMO 化」为作者主张，未独立核验。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 内源 EPAC1 SUMO 化水平极低 | 常规免疫沉淀难以检测到 SUMO 化条带 | SUMO 化是高度动态、可逆的修饰，且可能只发生在特定应激条件（如热休克）下 | Results 节 Fig. 1A-C：热休克处理后出现高分子量 EPAC1 条带，SENP1 处理可消除 |
| 质谱鉴定 SUMO 化位点困难 | 常规胰蛋白酶消化后 SUMO 化肽段信号弱、无特征性 | SUMO 化修饰的肽段在质谱中信号低，且 SUMO 的 C 端尾部缺乏胰蛋白酶切位点 | Methods 节：使用 SUMO3(Q89K) 突变体产生特征性 TGG 标签肽段 |
| 区分 SUMO 化与泛素化信号 | 高分子量条带可能来自泛素化或其他修饰 | 需要 SUMO 特异性抗体和去 SUMO 化酶处理验证 | Results 节 Fig. 1C：SENP1 处理显著减少高分子量条带 |
| 功能研究受限于 SUMO 化位点未知 | 无法通过点突变验证 SUMO 化的功能 | 缺乏精确的 SUMO 化位点信息 | Results 节：质谱鉴定 K561 后，构建 K561R 突变体进行功能验证 |

## 06 核心思想
1. **表面方法**：通过热休克诱导内源 SUMO 化，结合 SUMO3(Q89K) 突变体富集 SUMO 化底物，质谱鉴定 EPAC1 K561 为 SUMO 化位点；随后通过点突变（K561R）、RNAi 敲低、Rap-GTP pull-down 和 MD 模拟验证功能。
2. **核心洞察**：SUMO 化修饰 EPAC1 的 RA 结构域（K561），该修饰不依赖 cAMP 结合，而是通过直接增加 EPAC1 与 Rap1/2 的互作界面（埋藏表面积 +50%）来增强 GEF 活性。SUMO 在此充当「分子胶水」角色，而非仅改变构象。
3. **可能的普适教训** [Analysis]：翻译后修饰（如 SUMO 化）可以通过直接参与蛋白-蛋白互作界面（而非仅诱导构象变化）来调控 IDR 蛋白的功能。对于含 IDR 的蛋白，修饰基团本身可能成为互作界面的「扩展模块」，这一概念可推广至其他 IDP/IDR 介导的互作体系。

## 07 方法总览
- **输入**：人源细胞系（HEK293、HeLa、HUVEC）；重组 EPAC1 蛋白；SUMO3(Q89K) 突变体；SUMO 化预测工具（JASSA）。
- **输出**：EPAC1 K561 为 SUMO 化位点；SUMO 化增强 EPAC1 对 Rap1/2 的 GEF 活性；MD 模拟揭示 SUMO 化增强互作界面的结构基础。
- **模块**：
  1. SUMO 化检测与位点鉴定（热休克处理、SENP1 处理、Ni-NTA 富集、LC/MS/MS）
  2. 功能验证（Rap-GTP pull-down、RNAi 敲低、K561R 突变体）
  3. 凝聚体成像（共聚焦显微镜，EPAC1-EYFP 与 UBA2-mRuby 共定位）
  4. 结构建模与 MD 模拟（基于同源模型，NAMD 软件，30 ns 模拟）
- **训练**：不适用（无机器学习模型）。
- **反馈回路**：MD 模拟结果与功能实验相互印证（SUMO 化增强互作 → 功能增强）。
- **假设**：SUMO 化位点 K561 位于 RA 结构域，该结构域参与 Rap 结合；SUMO 化通过空间位阻或直接互作增强 Rap 结合。
- **文字流程**：热休克处理细胞 → 富集 SUMO 化蛋白 → 质谱鉴定 K561 → 构建 K561R 突变体 → 功能实验验证 SUMO 化对 Rap 激活的影响 → MD 模拟解析结构基础 → 结合凝聚体成像提出模型。

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| SUMO3(Q89K) 突变体辅助质谱鉴定 | 产生特征性 TGG 标签肽段，便于质谱鉴定 SUMO 化位点 | 常规 SUMO 化肽段质谱信号弱，难以鉴定 | 输入：SUMO3(Q89K) 质粒；输出：K561 位点鉴定 | Results 节 Fig. 2C：MS/MS 谱图明确显示 K561 的 TGG 修饰 | 预期影响：无法鉴定 K561 位点，后续功能实验无法开展 |
| 热休克诱导 SUMO 化 | 提高内源 SUMO 化水平，使检测成为可能 | 基础 SUMO 化水平极低 | 输入：43°C 处理；输出：可检测的 EPAC1 SUMO 化条带 | Results 节 Fig. 1A-C | 预期影响：无法检测到 SUMO 化信号 |
| K561R 突变体 | 消除 SUMO 化位点，验证功能 | 证明 SUMO 化修饰 K561 的功能必要性 | 输入：K561R 突变质粒；输出：SUMO 化消失，Rap 激活减弱 | Results 节 Fig. 6 | 实测效应：K561R 完全消除热休克诱导的 Rap 激活 |
| Rap-GTP pull-down | 定量检测 Rap1/2 活性 | 直接反映 EPAC1 的 GEF 活性 | 输入：细胞裂解液；输出：Rap-GTP 水平 | Results 节 Fig. 5A-C | 预期影响：无法评估 SUMO 化的功能后果 |
| MD 模拟 | 解析 SUMO 化对 EPAC1-Rap1 互作界面的影响 | 提供结构层面的机制解释 | 输入：EPAC1-Rap1 同源模型 + SUMO 结构；输出：埋藏表面积变化 | Results 节 Fig. 7A-D | 预期影响：无法解释 SUMO 化增强互作的机制 |
| 凝聚体成像 | 观察热休克诱导的 EPAC1/UBA2 核内凝聚体 | 连接 SUMO 化与相分离现象 | 输入：EPAC1-EYFP + UBA2-mRuby；输出：共定位凝聚体图像 | Results 节 Fig. 4A-C | 预期影响：无法建立 SUMO 化与凝聚体的时空关联 |

## 09 关键公式符号
不适用。本文无数学公式或算法模型。MD 模拟使用标准分子动力学方程（牛顿运动方程、PME 静电计算），但原文未给出具体公式。

## 10 实验设计与证据链
- **数据集/群体**：HEK293（人胚肾）、HeLa（宫颈癌）、HUVEC（人脐静脉内皮细胞）；重组蛋白表达于 E. coli。
- **规模**：每组实验至少 3 次独立重复（文中注明 "at least three independent experiments"）。
- **指标**：SUMO 化条带强度（免疫印迹）、Rap1/2-GTP 水平（pull-down 后免疫印迹）、凝聚体形成（共聚焦成像）、埋藏表面积（MD 模拟）。
- **基线**：37°C 未处理细胞；野生型 EPAC1；对照 siRNA。
- **预算**：未提供。
- **骨干/仪器**：Orbitrap Fusion Tribrid 质谱仪；Nikon AXR/A1R 共聚焦显微镜；NAMD 分子动力学软件。
- **oracle 输入**：SUMO3(Q89K) 突变体（用于质谱鉴定）；已知 EPAC1-Rap1 同源模型（基于 EPAC2 晶体结构 3CF6）。
- **评测协议**：免疫印迹条带密度定量；Rap-GTP 水平标准化至总 Rap；MD 模拟后计算埋藏表面积。

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|-------------|-------------------|------|
| 热休克诱导 EPAC1 高分子量条带 | EPAC1 可被 SUMO 化 | 37°C vs 43°C；不同时间点 | 43°C 处理后出现时间依赖性高分子量条带 | EPAC1 是 SUMO 底物 | 未直接证明是 SUMO 而非其他修饰 | Results 节 Fig. 1A-B |
| SENP1 处理消除高分子量条带 | 高分子量条带来自 SUMO 化 | 有/无 SENP1 处理 | SENP1 处理后条带显著减少 | 条带确实来自 SUMO 化 | 未排除其他 SUMO 家族成员（如 SUMO1 vs SUMO2/3） | Results 节 Fig. 1C |
| 质谱鉴定 K561 | K561 是 SUMO 化位点 | SUMO3(Q89K) 富集后 LC/MS/MS | 明确鉴定 K561 的 TGG 修饰，FDR < 1% | K561 是 SUMO 化位点 | 未排除其他低丰度位点 | Results 节 Fig. 2C |
| SIM 突变（SIM/5A）消除 SUMO 化 | SIM 是 SUMO 化所必需 | WT vs SIM/5A | SIM/5A 完全丧失 SUMO 化 | SIM 介导酶-底物识别 | 未证明 SIM 直接结合 UBC9 而非其他 E3 | Results 节 Fig. 3A |
| UBC9 pull-down | EPAC1 通过 SIM 结合 UBC9 | WT vs V321A/V323A | WT 结合 UBC9，突变体丧失结合 | SIM 介导 UBC9 互作 | 未定量结合亲和力 | Results 节 Fig. 3B |
| K561R 消除热休克诱导的 Rap 激活 | K561 SUMO 化是 Rap 激活所必需 | WT vs K561R | K561R 完全消除 Rap1/2 激活 | SUMO 化直接增强 GEF 活性 | 未排除 K561R 影响蛋白折叠 | Results 节 Fig. 6 |
| 热休克不改变 cAMP 水平 | 激活不依赖 cAMP | 热休克 vs 对照 | cAMP 水平无显著变化 | 激活是 cAMP 非依赖的 | 未检测局部 cAMP 微域 | Results 节 Supplementary Fig. 8 |
| MD 模拟显示 SUMO 化增加埋藏表面积 | SUMO 化增强 Rap1 结合 | EPAC1 vs EPAC1-SUMO | 埋藏表面积从 1486 Å² 增至 2227 Å² | SUMO 提供额外互作界面 | 模拟仅 30 ns，未做重复 | Results 节 Fig. 7 |

## 11 结论正确解读
- **任务范围**：本文仅证明 EPAC1 的 K561 SUMO 化在热休克条件下增强 Rap1/2 激活。未涉及其他应激条件、其他 SUMO 位点、其他 EPAC 底物。
- **oracle/真值输入**：质谱鉴定依赖 SUMO3(Q89K) 突变体，该策略可能偏向检测高丰度 SUMO 化事件；MD 模拟基于同源模型，非实验结构。
- **端到端状态**：从 SUMO 化鉴定到功能验证到结构模拟的完整链条，但未在动物模型或疾病背景下验证。
- **算力成本**：MD 模拟 30 ns，成本中等，未提供具体计算资源。
- **历史数据依赖**：依赖前期发现的 EPAC1 与 SUMO 机器的互作（[17]），本文为反向验证。
- **模型依赖**：MD 模拟结果依赖初始模型构建，SUMO 初始位置在 apo 状态下不受约束，可能影响结果。
- **最难情形**：内源 SUMO 化水平极低，需要热休克诱导才能检测；K561R 突变可能影响蛋白稳定性（未检测）。
- **群体/领域边界**：结论限于培养细胞体系；未在组织或体内验证。
- **不确定性**：SUMO 化对 EPAC1 的定量贡献（9% 化学计量比）是否足以解释全部功能效应未知；SUMO 化与 cAMP 通路是否存在协同或拮抗未探索。
- **有边界的复述**：在热休克条件下，EPAC1 的 K561 位点可被 SUMO 化修饰，该修饰通过增强 EPAC1-Rap1/2 互作界面（而非依赖 cAMP）激活 Rap GTPase；此机制在培养细胞中成立，其体内相关性和疾病意义尚待验证。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|---------------------|------|
| 内源 SUMO 化水平低 | 需要热休克诱导才能检测到 EPAC1 SUMO 化 | 未明确提及 | Results 节 Fig. 1 |
| 未检测 cAMP 对 SUMO 化的影响 | 仅证明 SUMO 化不依赖 cAMP，未反向测试 | "the effect of cAMP binding on EPAC1 SUMOylation is unknown and remains to be determined" | Discussion 节 |
| MD 模拟的初始模型限制 | apo 状态下 SUMO 初始位置不受约束 | 未明确提及 | Methods 节 |
| 未测试 K561 SUMO 化对 EPAC1 其他互作蛋白的影响 | 仅测试了 Rap1/2 | "It will be interesting to test the effects of K561 SUMOylation on EPAC1's interaction with β-arrestin2 or RanBP2" | Discussion 节 |
| 未在体内验证 | 所有实验均在培养细胞中进行 | 未明确提及 | 全文 |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|----------------------|----------|----------|------|
| K561R 突变可能影响蛋白折叠而非仅消除 SUMO 化 | K561 位于 RA 结构域，该残基可能对结构稳定性重要 | 若 K561R 导致蛋白 misfolding，则功能丧失不能归因于 SUMO 化缺失 | 检测 K561R 突变体的圆二色谱或热稳定性；或使用非保守突变（如 K561A） | Results 节 Fig. 6 |
| MD 模拟仅 30 ns，且未做重复 | 30 ns 可能不足以采样 SUMO 的构象变化 | 埋藏表面积差异可能受初始条件影响 | 延长模拟时间至 100+ ns，或做 3 次独立模拟 | Methods 节 |
| SUMO 化化学计量比仅 ~9% | 如此低比例的修饰如何产生显著功能效应？ | 可能存在「超化学计量」效应（如酶促放大）或未检测到其他位点 | 定量 SUMO 化 EPAC1 与总 EPAC1 的比例，并测试是否需达到阈值 | Results 节 Fig. 2C |
| 热休克可能通过其他机制激活 Rap | 热休克可能激活其他信号通路（如热休克蛋白） | 若其他通路也参与，则 SUMO 化的贡献可能被高估 | 使用 SUMO 化抑制剂（如 ML-792）或敲低 UBC9 验证 | Results 节 Fig. 5 |
| SIM 突变（SIM/5A）可能破坏蛋白整体结构 | SIM 与 SB 序列重叠，SB 对蛋白构象重要 | SIM/5A 效应可能来自 SB 功能丧失而非 SUMO 结合 | 使用更精细的 SIM 点突变（如 V321A/V323A）进行功能验证 | Results 节 Fig. 3A |
| 未检测 SUMO 化对 EPAC1 亚细胞定位的影响 | SUMO 化可能通过改变定位而非直接增强互作来激活 Rap | 若 SUMO 化促进 EPAC1 膜转位，则 Rap 激活可能是间接效应 | 进行亚细胞分级分离或活细胞成像 | Results 节 Fig. 4 |

## 14 Agent 提炼的知识候选
**标题：SUMO 化作为 IDR 蛋白互作界面的「可逆扩展模块」**

- **可迁移概念**：翻译后修饰（PTM）不仅可以通过构象变化调控蛋白功能，还可以直接作为互作界面的「扩展模块」，增加底物蛋白与效应蛋白的接触面积。对于含 IDR 的蛋白，PTM 基团（如 SUMO、泛素）可能充当「分子胶水」，稳定弱互作。
- **对 IDP/IDR × 蛋白互作课题的启示**：
  1. **互作界面预测**：在预测 IDR 蛋白的互作界面时，应考虑 PTM 位点附近的序列是否可能参与互作，而非仅关注线性 motif。
  2. **相分离调控**：SUMO 化通过增加互作界面可能促进多价互作，从而降低相分离的临界浓度。本文中 EPAC1 的 SUMO 化与核内凝聚体形成相关，提示 PTM 可作为相分离的「开关」。
  3. **MD 模拟策略**：本文展示了将 PTM 基团显式纳入 MD 模拟的可行性。对于 IDR 蛋白，可在模拟中引入 PTM 修饰，观察其对互作界面的影响。
- **可迁移方法**：
  1. **SUMO3(Q89K) 策略**：通过突变 SUMO 的 Q89 为 K，产生特征性 TGG 标签肽段，显著提高质谱鉴定 SUMO 化位点的灵敏度。该策略可推广至其他 PTM 的质谱鉴定。
  2. **热休克诱导 SUMO 化**：利用热休克作为可逆的应激刺激，提高内源 SUMO 化水平，便于检测。
  3. **MD 模拟 + 埋藏表面积分析**：通过比较修饰与未修饰蛋白的互作界面埋藏表面积，定量评估 PTM 对互作强度的贡献。
- **对 IDP/IDR 课题的具体应用建议**：
  1. 对已知含 IDR 的互作蛋白对，扫描 SUMO 化/泛素化位点，评估 PTM 是否位于互作界面附近。
  2. 在相分离体系中，引入 PTM 酶（如 SUMO 连接酶）或去修饰酶，观察相分离行为的动态变化。
  3. 使用 MD 模拟或增强采样方法，研究 PTM 基团与 IDR 的协同互作。

## 15 与已有知识连接
- **SUMO 化与相分离**：已有文献报道 SUMO 化参与 PML 核体（PML-NBs）等膜无细胞器的形成（如 Shen et al., 2006, *Molecular Cell*；Banani et al., 2017, *Nature Reviews Molecular Cell Biology*）。本文进一步将 SUMO 化与 EPAC1 的核内凝聚体联系起来，支持 SUMO-SIM 互作作为相分离驱动力的观点。
- **EPAC 信号通路**：EPAC1 的 GEF 活性传统上被认为严格依赖 cAMP 结合（de Rooij et al., 1998, *Nature*）。本文发现的 cAMP 非依赖激活机制扩展了 EPAC1 的调控模式，与近期报道的 EPAC1 磷酸化调控（如 PKA 磷酸化）形成互补。
- **IDR 与 PTM 互作**：IDR 区域富含 PTM 位点，PTM 可通过「修饰介导的相互作用」调控 IDR 功能（如 Bah & Forman-Kay, 2016, *Current Opinion in Structural Biology*）。本文的 SUMO 化案例为该领域提供了新的实例。
- **MD 模拟在 PTM 研究中的应用**：已有研究使用 MD 模拟研究磷酸化对 IDR 构象的影响（如 Mittal et al., 2018, *Nature Communications*）。本文将其扩展至 SUMO 化对互作界面的影响，方法上可迁移。
- **候选方向（未验证）**：SUMO 化是否通过影响 EPAC1 的液-液相分离（LLPS）来调控其信号输出？本文未直接测量 EPAC1 的相分离行为，但凝聚体成像结果提示该可能性。

## 16 研究想法
**候选 1：SUMO 化修饰对 IDR 蛋白相分离行为的系统调控**
- **来源**：本文发现 EPAC1 SUMO 化与核内凝聚体形成相关（Fig. 4），但未直接测量相分离。
- **假设**：SUMO 化通过增加多价互作（SUMO-SIM 互作）降低 IDR 蛋白的相分离临界浓度。
- **方法**：选择已知含 IDR 和 SIM 的蛋白，体外重构 SUMO 化体系，使用浊度测定或荧光显微镜观察相分离行为；比较 SUMO 化与未修饰蛋白的饱和浓度。
- **验证**：若 SUMO 化显著降低相分离临界浓度，则支持 PTM 作为相分离「开关」的假说。
- **创新状态**：unverified

**候选 2：基于 AI 的 SUMO 化位点与互作界面协同预测**
- **来源**：本文质谱鉴定 K561 为 SUMO 化位点，且该位点位于 RA 结构域（参与 Rap 结合）。现有 SUMO 化位点预测工具（如 JASSA）仅基于序列特征，未考虑互作界面信息。
- **假设**：整合蛋白互作界面信息可提高 SUMO 化位点预测的准确性，尤其是位于互作界面的功能性 SUMO 化位点。
- **方法**：构建数据集（含已知互作界面内的 SUMO 化位点），使用图神经网络（GNN）或 Transformer 架构，输入蛋白结构/序列 + 互作界面注释，预测功能性 SUMO 化位点。
- **验证**：在独立测试集上比较与现有工具（JASSA、GPS-SUMO）的 AUC 差异。
- **创新状态**：unverified

**候选 3：MD 模拟揭示 SUMO 化对 IDR 蛋白互作动力学的调控**
- **来源**：本文 MD 模拟显示 SUMO 化增加埋藏表面积，但仅 30 ns 且未做重复。
- **假设**：SUMO 化不仅增加互作界面，还可能通过改变 IDR 的构象动力学来调控互作。
- **方法**：对 EPAC1 的 IDR 区域（含 K561）进行增强采样 MD 模拟（如副本交换），比较 SUMO 化与未修饰蛋白的构象系综差异。
- **验证**：若 SUMO 化导致 IDR 区域构象更紧凑或更有序，则支持「构象选择」机制。
- **创新状态**：unverified

**候选 4：SUMO 化与 cAMP 信号的协同/拮抗调控网络**
- **来源**：本文证明 SUMO 化独立于 cAMP 激活 EPAC1，但未测试二者是否协同。
- **假设**：cAMP 结合与 SUMO 化可能通过不同机制（构象 vs 界面）协同增强 EPAC1 活性。
- **方法**：构建 EPAC1 突变体（cAMP 结合缺陷 + K561R），在细胞中比较单突变与双突变的 Rap 激活水平。
- **验证**：若双突变完全消除 Rap 激活，而单突变部分保留，则支持协同模型。
- **创新状态**：unverified