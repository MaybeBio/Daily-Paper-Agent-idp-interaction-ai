## 01 基本信息

- **标题**: Regulation of tension-dependent localization of LATS1 and LATS2 to adherens junctions
- **作者**: De Silva, Chamika; Kelch, Brian A; McCollum, Dannel
- **单位**: 未提供（根据 McCollum 实验室背景，推测为 UMass Chan Medical School，但原文未明确）
- **期刊/平台**: PLOS ONE
- **年份**: 2026
- **论文类型**: 实验研究（分子机制解析）
- **领域**: 细胞生物学 / Hippo 信号通路 / 机械力传导
- **关键词**: LIMD1, LATS1/2, Hippo pathway, adherens junctions, mechanical strain, intrinsically disordered region, AlphaFold
- **DOI**: 10.1371/journal.pone.0342107
- **代码**: 未提供
- **数据**: 未提供（原始数据未公开）
- **阅读日期**: 2026-05-13
- **在该课题方向中的位置**: 本文是「IDP/IDR × 蛋白互作 × AI 方法」交叉方向的典型案例——使用 AlphaFold 预测蛋白互作界面，并发现 IDR 在机械力依赖的蛋白招募中发挥关键作用（可能通过 LLPS）。对无序蛋白/相分离课题读者而言，本文提供了「IDR 功能必要性 + AlphaFold 预测线性 motif + 实验验证」的完整范式。

---

## 02 一句话总结

本文通过 AlphaFold 建模、结构域截短和点突变实验，发现 LIMD1 通过其 LIM1/LIM2 结构域结合 LATS1/2 N 端一个保守线性基序（LATS-LATCH），而 LIMD1 的 N 端 IDR 虽不直接结合 LATS1/2，却是 LATS1 在机械张力下定位到黏附连接（AJs）所必需的，提示 IDR 可能通过相分离机制促进蛋白招募。

---

## 03 研究问题

- **具体问题**: LIMD1 如何响应机械张力将 LATS1/2 招募到黏附连接（AJs）？其分子结合界面是什么？IDR 在其中扮演什么角色？
- **为什么重要**: Hippo 通路调控细胞增殖、凋亡和分化，其核心激酶 LATS1/2 受机械力调控，但分子机制不清。理解这一机制对癌症、组织再生等疾病研究有直接意义。
- **现有方法不足**: 此前已知 LIMD1 家族蛋白（Ajuba, Zyxin, TRIP6）通过 LIM 结构域结合 LATS2，但具体结合位点、张力依赖性的分子基础、IDR 的功能均不清楚。
- **精确研究问题**: Can AlphaFold 预测的 LATS-LATCH 线性基序解释 LIMD1 对 LATS1/2 的张力依赖性招募，且 LIMD1 的 IDR 是否独立于 LATS 结合而参与这一过程？

---

## 04 背景与发展脉络

**脉络标注**: 仅本文框架（基于本文引文与叙述）

1. **阶段一：Hippo 通路发现与 LATS1/2 功能确立**（~2000s）
   - 代表工作：LATS1/2 磷酸化 YAP 调控细胞增殖 [1,2]
   - 局限：主要关注生化调控，机械力维度缺失

2. **阶段二：机械力调控 Hippo 通路的发现**（~2010s）
   - 代表工作：果蝇遗传筛选 [4] + 哺乳动物上皮细胞研究 [5,6] 表明 AJs 处机械张力抑制 LATS1/2
   - 关键蛋白：Ajuba/LIMD1 家族 LIM 蛋白
   - 局限：LIM 蛋白如何感知张力并结合 LATS 的分子细节未知

3. **阶段三：LIM 结构域蛋白作为张力传感器的机制**（~2020s）
   - 代表工作：LIM 结构域直接结合 strained F-actin [8-10]
   - 关键发现：保守苯丙氨酸残基介导张力感知
   - 局限：LIM 蛋白如何将张力信号传递给 LATS1/2 仍不清楚

4. **本文位置**：在阶段三基础上，用 AlphaFold 预测 + 实验验证，首次定义 LATS1/2 上的 LATS-LATCH 基序为 LIMD1 结合位点，并揭示 IDR 的独立功能。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| LATS1/2 与 LIMD1 的结合界面未知 | 已知 LIM 结构域参与结合，但具体氨基酸和基序不清楚 | 缺乏高分辨率结构；LIM 蛋白与 LATS 互作界面复杂 | Results 节 "LIMD1-LATS1/2 binding is mediated by the LIMD1 LIM domains" |
| 张力依赖性招募的分子机制不清 | LIMD1 在张力下才结合 LATS1/2，但机制不明 | 可能涉及 LIM 结构域结合 strained F-actin 后的构象变化 | Discussion 节 "why binding of the LATCH to LIMD1 depends on mechanical strain in vivo" |
| IDR 的功能完全未知 | LIMD1 N 端 IDR 保守性低，此前无功能注释 | IDR 可能通过 LLPS 促进蛋白富集，而非直接结合 | Results 节 "both the LIM domains and IDR region are required to recruit LATS1" |
| 点突变干扰张力感知但机制混淆 | F512A/F575A 突变同时影响 F-actin 结合和 LATS 结合 | 突变可能破坏 LIM 结构域整体折叠，而非特异性影响单一互作 | Results 节 "These mutations affect both binding to LATS2 and strained F-actin" |

---

## 06 核心思想

**1) 表面方法**：
- 结构域截短（LIMD1 N 端 vs C 端）进行体外结合实验
- AlphaFold 2/3 建模预测 LIMD1-LATS2 互作界面
- 点突变验证预测接触残基
- 活细胞成像检测 GFP 融合蛋白在 AJs 的定位
- Blebbistatin 处理破坏张力作为对照

**2) 核心洞察**：
- LATS1/2 上存在一个保守的线性基序（LATS-LATCH），以「线性肽沿 LIM 结构域表面延伸」的方式结合 LIMD1 的 LIM1/LIM2
- LIMD1 对 LATS1/2 的招募是**双部分（bipartite）机制**：LIM 结构域提供直接结合，而 N 端 IDR 提供独立于直接结合的招募功能（可能通过 LLPS）
- AlphaFold 预测的接触残基突变（4mut）能同时破坏结合和 AJ 定位，验证了计算模型的有效性

**3) 可能的普适教训 [Analysis]**：
- AlphaFold 不仅能预测折叠蛋白结构，对「线性基序-结构域」互作界面的预测也高度可靠，可作为 IDP/IDR 互作研究的第一筛选工具
- IDR 的功能不一定是直接结合——它可能通过相分离/凝聚体形成来「浓缩」互作伙伴，这种功能无法通过传统结合实验检测，需要活细胞定位实验来揭示
- 「结构域负责结合、IDR 负责富集」的双部分机制可能是 IDR 介导信号传导的普遍范式

---

## 07 方法总览

**输入**：
- LIMD1 全长及截短突变体（aa 1-467, aa 468-676, 各种 LIM 组合缺失）
- LATS1/2 N 端片段及 LATS-LATCH 突变体
- AlphaFold 2/3 预测的 LIMD1-LATS2 复合物模型

**输出**：
- 蛋白-蛋白结合能力（免疫共沉淀）
- LATS1 的 AJ 定位能力（活细胞成像，AJ/细胞质比率）
- LATS-LATCH 基序的序列特征和功能验证

**模块**：
1. 体外结合实验（co-IP）
2. AlphaFold 结构预测
3. 定点突变
4. 活细胞成像与定量
5. 药物处理（blebbistatin）控制张力

**训练**：不适用（无机器学习训练）

**工具**：AlphaFold 2/3、ImageJ/Fiji（含自写宏）、Nikon 荧光显微镜、EVOS M7000 活细胞成像系统

**反馈回路**：AlphaFold 预测 → 突变设计 → 实验验证 → 修正模型

**假设**：
- 过表达体系能反映内源互作
- AlphaFold 预测的界面在体内具有功能相关性
- 70% 汇合度代表标准高张力状态

**文字流程**：
1. 先用截短突变体确定 LIMD1 C 端（含 LIM 结构域）负责结合 LATS1/2
2. 用 AlphaFold 建模 LIMD1-LATS2 互作，识别 LATS-LATCH 基序
3. 在 LATS1/2 中删除 LATCH 验证结合丧失
4. 将 LATS2-LATCH 单独融合 GFP 验证其足以定位到 AJs
5. 突变 LATCH 接触残基（4mut）验证结合和定位均被破坏
6. 意外发现：仅含 LIM 结构域的 LIMD1 突变体虽能结合 LATS1/2 但不能招募 LATS1 到 AJs → 发现 IDR 的必要性

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| LIMD1 截短突变体 | 定位结合域 | 确定哪个区域介导 LATS1/2 结合 | 输入：N 端/C 端片段；输出：结合能力 | Fig 1A-C：C 端 (aa 468-676) 结合，N 端不结合 | 预期：无法区分 IDR 与 LIM 结构域的功能差异 |
| AlphaFold 2/3 建模 | 预测互作界面 | 无实验结构，需计算指导 | 输入：LIMD1-LATS2 序列；输出：复合物模型 + 接触残基 | Fig 4B：预测 LATCH 沿 LIM 结构域延伸 | 预期：无法设计 4mut 突变体，结合位点仍未知 |
| LATS-LATCH 缺失突变体 | 验证基序必要性 | 确认 LATCH 是 LIMD1 结合的功能基序 | 输入：ΔLATCH LATS1/2；输出：结合丧失 | Fig 4D-E：ΔLATCH 破坏结合 | 预期：无法证明 LATCH 是功能性结合位点 |
| LATS2-LATCH-GFP 融合 | 验证基序充分性 | 证明 LATCH 足以驱动 AJ 定位 | 输入：GFP-LATS2-LATCH；输出：AJ 定位 | Fig 5B-C：LATCH 单独足以定位 AJs | 预期：无法区分 LATCH 是充分还是必要条件 |
| 4mut 点突变 | 验证预测接触残基 | 确认 AlphaFold 预测的界面残基具有功能 | 输入：L441G/V444A/K445D/R448D；输出：结合和定位均丧失 | Fig 5A-B：4mut 破坏结合和定位 | 预期：无法验证计算模型的功能相关性 |
| IDR 缺失突变体 | 测试 IDR 功能 | 意外发现 IDR 对招募必要 | 输入：ΔIDR LIMD1；输出：结合保留但招募丧失 | Fig 1D-F：ΔIDR 不能招募 LATS1 | 预期：无法发现双部分机制 |
| Blebbistatin 处理 | 控制张力条件 | 验证张力依赖性 | 输入：肌球蛋白抑制剂；输出：LATS1 AJ 定位丧失 | Methods "Drug treatments" | 预期：无法区分张力依赖与非依赖过程 |

---

## 09 关键公式符号

**不适用**（本文为实验生物学论文，无数学公式或计算模型）

---

## 10 实验设计与证据链

**数据集/群体**：
- 细胞系：HEK293, HEK293A, HEK293T（人胚肾）；MCF10A（人乳腺上皮）
- MCF10A LIMD1 敲除（LIMD1-KO）细胞系（此前已建立 [7]）
- 稳定表达 GFP 融合蛋白的 MCF10A 系（慢病毒转导）

**指标**：
- 免疫共沉淀（co-IP）结合强度
- LATS1 的 AJ/细胞质荧光比率
- AJ 定位的定性判断（活细胞成像）

**基线/对照**：
- 未处理（DMSO）vs Blebbistatin 处理
- 野生型 LIMD1 vs 各种突变体
- LIMD1-KO 细胞中回补不同突变体

**预算/仪器**：
- 标准分子生物学与细胞培养设备
- Nikon Eclipse Ni-E 荧光显微镜
- EVOS M7000 活细胞成像系统
- ImageJ/Fiji（含自写宏）

**评测协议**：
- 每个突变体至少 3 次独立实验
- 统计方法：单因素 ANOVA（GraphPad Prism 10.5.0）
- 正态性检验：Shapiro-Wilk

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|-----------------|------|
| LIMD1 截短体 co-IP | C 端 LIM 结构域介导 LATS1/2 结合 | N 端 (1-467) vs C 端 (468-676) | C 端结合，N 端不结合 | LIM 结构域是结合所必需 | 不能排除 N 端有辅助结合作用 | Fig 1A-C |
| LIMD1 截短体 AJ 定位 | C 端足以招募 LATS1 到 AJs | 全长 vs 各截短体在 LIMD1-KO 中回补 | C 端结合但不招募 LATS1 | IDR 对招募必要 | 不能确定 IDR 的具体机制 | Fig 1D-F |
| LIM 组合缺失 | LIM1/LIM2 是功能关键 | 单 LIM vs 双 LIM 组合 | 仅 LIM1+2 组合可招募 LATS1 | LIM1 和 LIM2 均需同时存在 | 不能排除 LIM3 有调节作用 | Fig 2 |
| 点突变 F512A/F575A | 张力感知残基参与 LATS1 招募 | 单突变 vs 双突变 | 双突变破坏招募 | LIM1/LIM2 的 F-actin 结合对招募必要 | 突变可能影响蛋白折叠而非特异性互作 | Fig 3A-C |
| 点突变体 co-IP | 上述突变影响 LATS1/2 结合 | WT vs 突变体 | 突变体结合 LATS1/2 能力下降 | F-actin 结合与 LATS 结合耦合 | 不能区分直接 vs 间接效应 | Fig 3D-G |
| AlphaFold 预测 + LATCH 缺失 | LATCH 是 LIMD1 结合位点 | ΔLATCH vs WT LATS1/2 | ΔLATCH 丧失结合 | LATCH 是功能性结合基序 | AlphaFold 预测可能有假阳性 | Fig 4B-E |
| GFP-LATS2-LATCH | LATCH 足以驱动 AJ 定位 | LATCH-GFP vs GFP 对照 | LATCH-GFP 定位到 AJs | LATCH 是 AJ 定位的充分条件 | 不能排除其他区域也有定位功能 | Fig 5B-C |
| 4mut 突变 | 预测接触残基功能验证 | 4mut vs WT LATCH | 4mut 丧失结合和定位 | AlphaFold 预测的界面残基具有功能 | 不能排除 4mut 影响 LATCH 整体构象 | Fig 5A-B |

---

## 11 结论正确解读

- **任务范围**: 本文仅研究 LIMD1 对 LATS1/2 的招募机制，不涉及 LATS1/2 激酶活性调控、YAP 磷酸化下游效应或体内（动物）验证。
- **Oracle/真值输入**: AlphaFold 预测作为「计算 oracle」指导突变设计，但所有结论均需实验验证；AlphaFold 预测本身不是真值。
- **端到端状态**: 非端到端。本文是机制解析，未构建完整通路模型。
- **算力成本**: 未提供（AlphaFold 推理成本未报告）。
- **历史数据依赖**: 依赖此前 LIMD1-KO 细胞系 [7] 和 LIM 蛋白家族研究 [8-10,15-17]。
- **模型依赖**: 所有结论基于过表达体系；内源蛋白行为可能不同。
- **最难情形**: 作者承认无法检测内源 LATS2（"endogenous LATS2 is very difficult to detect"），因此所有 LATS2 相关结论均基于过表达。
- **群体/领域边界**: 结论限于培养细胞（MCF10A, HEK293）；未在组织或体内验证。
- **不确定性**: 作者明确表示 IDR 促进 LATS1 招募的机制尚不清楚，LLPS 假说仅为推测（Discussion 节 "One intriguing possibility"）。
- **有边界的复述**: 在过表达培养细胞体系中，LIMD1 通过 LIM1/LIM2 结构域结合 LATS1/2 的 LATS-LATCH 基序，且 LIMD1 的 N 端 IDR 独立于直接结合而参与 LATS1 的 AJ 招募；该招募依赖机械张力，但 IDR 的具体分子机制（是否通过 LLPS）未证实。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 内源 LATS2 检测困难 | 所有 LATS2 实验均基于过表达 | 未明确提及 | Results 节 "all studies involving endogenous proteins focused on LATS1" |
| IDR 功能机制未明 | 不知道 IDR 如何促进 LATS1 招募 | 推测可能通过 LLPS，需进一步研究 | Discussion 节 "One intriguing possibility is that the IDR region of LIMD1 may promote liquid-liquid phase separations" |
| 点突变解释存在歧义 | F512A/F575A 同时影响 F-actin 结合和 LATS1/2 结合 | 未明确提及 | Results 节 "These mutations affect both binding to LATS2 and strained F-actin" |
| 体外结合可能不代表体内状态 | co-IP 在过表达、无张力条件下进行 | 未明确提及 | Methods 节 "Cell transfection, co-immunoprecipitation" |
| AlphaFold 预测的 helical hairpin 互作未被实验证实 | 预测存在第二个结合位点但实验不支持其必要性 | 推测 LATCH 可能作为张力依赖的 tether 使弱互作得以发生 | Discussion 节 "there is some reason to suspect that the predicted LIMD1-helical hairpin interaction may be relevant in vivo" |

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 所有结论基于过表达体系 | 过表达可能人为增强弱互作，内源水平下 LATS-LATCH 互作可能不成立 | 影响结论的生理相关性 | 使用内源抗体 ChIP/共定位实验，或 CRISPR 敲入标签 | Methods 节 "Cell transfection" |
| F512A/F575A 突变解释混淆 | 作者承认这些突变同时影响 F-actin 和 LATS1/2 结合，无法区分「张力感知缺陷」vs「直接结合缺陷」 | 核心机制（张力如何增强结合）未被直接证明 | 设计不参与 F-actin 结合的 LATS-LATCH 突变体，或在体外重建张力系统 | Results 节 Fig 3 |
| IDR 必要性实验缺乏机制验证 | 仅证明「删除 IDR 则无招募」，未证明 LLPS 参与 | LLPS 假说无直接证据 | FRAP 实验检测凝聚体动态；体外 LLPS 重建实验 | Discussion 节 |
| AlphaFold 预测的 helical hairpin 互作被忽略 | 预测存在两个结合位点但只验证了 LATCH；helical hairpin 可能在体内有功能 | 可能遗漏重要调控机制 | 构建 helical hairpin 突变体在体内测试 | Fig 4B, Discussion 节 |
| 缺乏定量结合亲和力数据 | 未提供 Kd 或结合动力学，无法判断互作强度 | 无法评估张力增强结合的幅度 | 表面等离子共振（SPR）或 MST 实验 | Methods 节 |
| 未测试其他 LIMD1 家族蛋白 | Ajuba, Zyxin, TRIP6 是否使用相同 LATCH 机制未知 | 影响结论的普适性 | 比较不同家族成员的 LATCH 结合 | Introduction 节 |
| 活细胞成像仅用 GFP 融合 | GFP 标签可能影响蛋白行为；未做内源水平验证 | 可能产生假阳性/假阴性定位结果 | CRISPR 内源标签或抗体染色交叉验证 | Methods 节 "Live cell imaging" |

---

## 14 学到什么

**Agent 提炼的知识候选**：

1. **AlphaFold 可预测「线性基序-结构域」互作界面**：本文展示了 AlphaFold 对 IDP/IDR 中线性基序与折叠结构域互作的预测能力。对于 IDP/IDR 互作课题，可将 AlphaFold 作为发现候选线性基序（如 LATCH 类 motif）的第一工具，再用突变验证。

2. **「结构域结合 + IDR 富集」双部分机制**：LIMD1 的 LIM 结构域负责直接结合 LATS1/2，而 IDR 独立负责招募（可能通过 LLPS）。这提示在研究 IDR 介导的互作时，不能只关注直接结合——IDR 可能通过相分离「浓缩」互作伙伴，这种效应在体外结合实验中不可见，必须在活细胞中检测。

3. **张力感知与互作耦合的设计思路**：LIMD1 通过 LIM 结构域结合 strained F-actin 来感知张力，进而增强 LATS1/2 结合。对于相分离课题，可借鉴「机械力 → 构象变化 → 增强互作/相分离」的调控逻辑。

4. **突变体设计的「双刃剑」警示**：F512A/F575A 突变同时影响 F-actin 和 LATS1/2 结合，说明 LIM 结构域中同一残基可能参与多个互作界面。在设计突变体时需谨慎区分「特异性破坏单一互作」vs「全局破坏结构域功能」。

5. **活细胞定位作为功能 readout**：本文用 AJ/细胞质比率作为定量指标，比单纯的结合实验更能反映生物学功能。对于 IDR/相分离研究，活细胞凝聚体形成/定位实验是验证 IDR 功能的关键手段。

6. **AlphaFold 置信度与实验验证的闭环**：本文展示了「计算预测 → 突变设计 → 功能验证 → 修正模型」的完整闭环，这是 AI 方法在 IDP/IDR 研究中可迁移的标准流程。

---

## 15 与已有知识连接

- **Hippo 通路与机械力传导**：本文建立在果蝇 [4] 和哺乳动物 [5,6] 前期工作之上，确认 LIMD1 家族蛋白是张力依赖的 LATS1/2 调控因子。与 Dupont et al. (2011) Nature 关于 YAP 机械力响应的经典工作形成互补。

- **LIM 结构域蛋白与 F-actin 张力感知**：本文引用的 [8-10] 表明 LIM 结构域蛋白（zyxin, TRIP6, LIMD1）直接结合 strained F-actin。这与 Winkelman et al. (2020) eLife 关于 zyxin LIM 结构域张力感知机制的工作一致。

- **AlphaFold 在蛋白互作预测中的应用**：本文使用 AlphaFold 2/3 预测 LIMD1-LATS2 互作，与近期 AlphaFold 用于预测 IDP 互作（如 Peptiderive 等工具）的趋势一致。可参考 Jumper et al. (2021) Nature 和 Abramson et al. (2024) Nature 的 AlphaFold 3 方法学。

- **IDR 与相分离在信号通路中的角色**：作者推测 IDR 可能通过 LLPS 促进 LATS1 招募，这与 Hippo 通路中相分离的研究（如 YAP/TAZ 凝聚体 [23-29]）一致。可连接 Sabari et al. (2018) Science 关于 YAP 相分离的工作。

- **LATS 激酶调控的分子机制**：本文发现的 LATS-LATCH 基序位于 LATS N 端无序区，与 LATS 激酶活性调控（MOB1 结合、磷酸化）的关系值得进一步探索。可参考 Ni et al. (2023) 关于 LATS 激酶结构的研究。

- **黏附连接与机械传导**：本文聚焦 AJs 作为机械力感知位点，与 E-cadherin/β-catenin 复合物的力传导研究（如 le Duc et al. (2010) JCB）形成连接。

---

## 16 研究想法

**Agent 生成的研究候选**：

1. **候选名称**: LATS-LATCH 基序在其他 LIMD1 家族蛋白中的保守性分析
   - **来源局限/观察**: 本文仅验证了 LIMD1-LATS 互作，但 Ajuba, Zyxin, TRIP6 是否使用相同基序未知
   - **核心假设**: LATS-LATCH 结合模式在 LIMD1 家族中保守，但亲和力差异决定功能特异性
   - **初步方法**: 序列比对 + AlphaFold 批量预测 + 突变验证
   - **验证方式**: 跨家族 co-IP 和 AJ 定位实验
   - **创新状态**: unverified

2. **候选名称**: LIMD1 IDR 的相分离能力及其在 LATS1 招募中的作用
   - **来源局限/观察**: 作者推测 IDR 通过 LLPS 促进招募，但无直接证据
   - **核心假设**: LIMD1 IDR 在张力下经历 LLPS，形成富集 LATS1/2 的凝聚体
   - **初步方法**: 体外 LLPS 重建（纯化 IDR + 不同浓度/盐条件）；活细胞 FRAP 检测凝聚体动态；光遗传学工具扰动凝聚体
   - **验证方式**: 凝聚体形成与 LATS1 招募的相关性；IDR 突变体破坏 LLPS 后招募丧失
   - **创新状态**: unverified

3. **候选名称**: 张力诱导的 LIMD1 构象变化如何增强 LATS-LATCH 结合
   - **来源局限/观察**: 作者提出「LIM 结构域结合 strained F-actin 后增强 LATS 结合」但机制不明
   - **核心假设**: F-actin 结合诱导 LIM 结构域构象变化，暴露/优化 LATS-LATCH 结合表面
   - **初步方法**: 分子动力学（MD）模拟 LIMD1-LATS-LATCH 复合物在有/无 F-actin 条件下的构象动力学；增强采样方法计算结合自由能
   - **验证方式**: MD 预测的构象变化通过交联质谱或 FRET 实验验证
   - **创新状态**: unverified

4. **候选名称**: 深度学习预测 LATS-LATCH 类线性基序的通用工具
   - **来源局限/观察**: 本文通过 AlphaFold 人工识别了 LATS-LATCH，但缺乏系统性发现线性基序的方法
   - **核心假设**: 可在蛋白互作组中系统搜索「LIM 结构域-线性基序」互作对
   - **初步方法**: 训练一个基于结构的线性基序预测器（如用 AlphaFold 批量预测 + 接触残基打分）；整合序列保守性特征
   - **验证方式**: 在已知 LIM 互作组中测试召回率；新预测互作对实验验证
   - **创新状态**: unverified

5. **候选名称**: 机械张力调控 LATS1/2 凝聚体形成的定量模型
   - **来源局限/观察**: 本文证明张力依赖的 LATS1 招募，但未量化张力大小与招募程度的关系
   - **核心假设**: 张力强度与 LATS1 AJ 定位量呈剂量依赖关系，且存在阈值
   - **初步方法**: 使用可调控张力的基底（如微柱阵列或光遗传学收缩系统）+ 定量荧光成像；建立 Hill 方程模型
   - **验证方式**: 模型预测与实验数据拟合；不同张力条件下的招募差异
   - **创新状态**: unverified

6. **候选名称**: LATS-LATCH 互作作为药物靶点的可行性评估
   - **来源局限/观察**: LATS1/2 是肿瘤抑制因子，增强其 AJ 定位可能抑制 YAP 活性
   - **核心假设**: 稳定 LATS-LATCH 互作的小分子可增强 LATS1/2 的 AJ 定位和 YAP 磷酸化
   - **初步方法**: 基于 AlphaFold 结构的虚拟筛选；SPR 验证结合；细胞实验检测 YAP 活性
   - **验证方式**: 化合物处理后的 LATS1 AJ 定位和 YAP 靶基因表达
   - **创新状态**: unverified