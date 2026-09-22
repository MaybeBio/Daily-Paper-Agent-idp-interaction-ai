## 01 基本信息

- **标题**: An in silico study of how histone tail conformation affects the binding affinity of ING family proteins
- **作者与单位**: Gul, Nadir; Yildiz, Ahmet（单位未在摘要中提供）
- **期刊/预印本平台**: PeerJ
- **年份**: 2022-10-07
- **论文类型**: 计算研究（in silico）
- **领域**: 表观遗传学、蛋白-蛋白互作、无序蛋白（组蛋白尾部）、分子对接
- **关键词**: Histone tail, ING family, PHD finger, intrinsically disordered protein, molecular docking, binding affinity
- **DOI/arXiv 号**: 10.7717/peerj.14029
- **代码**: 未提供
- **数据**: 使用 PDB 晶体结构（ING1/2/4/5 PHD finger 结构、MOZ PHD-H3 复合物 PDB: 4LK9）、UniProtKB 序列数据
- **阅读日期**: 2026-05-13
- **在该课题方向中的位置**: 本文直接以组蛋白尾部（IDR）的构象异质性为研究对象，通过分子对接（Haddock 2.4、ClusPro）和结合自由能预测（PRODIGY）系统评估 IDR 构象（螺旋 vs. 线性）对 reader 蛋白（ING 家族 PHD finger）结合亲和力的影响。属于「IDP/IDR 构象 × 蛋白互作 × 计算模拟」交叉方向，为 IDR 构象选择性识别提供了计算证据。

## 02 一句话总结

本文通过分子对接（Haddock 2.4 和 ClusPro）将四种 ING 家族蛋白的 PHD finger 结构域分别与两种线性、两种螺旋构象的组蛋白 H3 尾部（11 个氨基酸）进行对接，并用 PRODIGY 计算结合亲和力，发现线性构象的组蛋白尾部与 ING PHD finger 的结合亲和力在 99% 置信水平上显著高于螺旋构象，且该计算流程经 MOZ PHD-H3 复合物（已知偏好螺旋构象）验证可靠。

## 03 研究问题

- **具体问题**: 组蛋白 H3 尾部（一个 intrinsically disordered region, IDR）的构象（线性 vs. 螺旋）是否显著影响 ING 家族蛋白 PHD finger 结构域与其结合的亲和力？
- **为什么重要**: 组蛋白尾部是 IDR，构象高度异质，现有研究几乎全部聚焦于 PTM（如 H3K4me3）对结合亲和力的调控，而忽略了尾部构象本身作为选择性决定因素的可能性。若构象确实影响亲和力，则意味着 IDR 的构象偏好（而非仅 PTM 代码）是表观遗传 reader 识别特异性的一个未被充分认识的维度。
- **现有方法为何不足**: 实验方法（X-ray、NMR）只能捕获结合态构象，难以系统评估未结合态 IDR 的构象异质性对结合的影响；MD 模拟计算成本高，难以对多个蛋白-肽段组合进行系统比较。
- **精确研究问题**: Can the conformational state (linear vs. helical) of the intrinsically disordered histone H3 tail significantly alter the binding affinity of ING family PHD finger domains, as assessed by molecular docking and binding energy prediction?

## 04 背景与发展脉络

**脉络标注**: 仅本文框架（基于本文 Introduction 和 Discussion 的引用与叙述，未经外部系统核验）

1. **阶段一：组蛋白尾部 PTM 作为结合决定因素（主流范式）**
   - 代表方法: 实验结构生物学（X-ray、NMR）、突变研究
   - 核心发现: ING PHD finger 特异性识别 H3K4me3，K4 甲基化状态决定结合
   - 优点: 实验验证充分，机制清晰
   - 局限: 忽略尾部构象异质性的贡献；无法解释为何同一 PTM 状态下不同 reader 仍有选择性差异

2. **阶段二：IDP/IDR 构象异质性的认识（结构生物学视角）**
   - 代表方法: NMR、CD（圆二色谱）、单分子 FRET
   - 核心发现: 组蛋白尾部无固定结构，但存在偏好构象（如螺旋倾向）；乙酰化可增加 α-螺旋含量（Wang et al., 2000）
   - 优点: 揭示了 IDR 的动态构象景观
   - 局限: 难以直接关联构象偏好与特定 reader 的结合选择性

3. **阶段三：计算模拟用于 IDR-蛋白互作预测（本文位置）**
   - 代表方法: 分子对接（Haddock、ClusPro）、结合能预测（PRODIGY）
   - 本文主张: 通过系统对接不同构象的 H3 尾部与 ING PHD finger，首次在计算层面证明构象本身（而非仅 PTM）是结合亲和力的显著决定因素
   - 优点: 可系统比较多种构象-蛋白组合；成本低于 MD；结果可统计检验
   - 局限: 对接方法对 IDR 柔性处理有限；未考虑 PTM 与构象的协同效应

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 构象异质性被忽视 | 大量研究聚焦 PTM 对组蛋白尾部结合的影响，几乎无人系统研究尾部构象本身的作用 | IDR 无固定结构，实验难以捕获未结合态构象；主流范式默认 PTM 是主要决定因素 | Introduction: "existing experimental studies concentrated on different PTMs while disregarding the conformation of the histone tail" |
| 数据库中的构象矛盾 | UniProt 中存在大量 H3K4me3 相关复合物结构，但同一修饰可对应不同尾部构象 | 未结合态 IDR 的构象偏好未被纳入复合物结构解读 | Introduction: "numerous complexes featuring a methylated fourth lysine residue of the histone tail can be found in the UniProt database" |
| 计算模拟 IDR 的困难 | IDR 柔性大，MD 模拟成本高，难以系统比较多个蛋白-肽组合 | IDR 无稳定三级结构，传统结构生物学方法难以直接应用 | Introduction: "Due to the limitations of molecular simulation techniques, we preferred molecular docking methods" |
| 缺乏构象-亲和力的定量证据 | 无研究系统比较同一 reader 对不同构象 IDR 的亲和力差异 | 缺乏合适的计算流程和统计检验框架 | 全文核心 gap，本文通过 docking + PRODIGY + t-test 填补 |

## 06 核心思想

### 1) 表面方法
将四种 ING 家族蛋白（ING1、ING2、ING4、ING5）的 PHD finger 晶体结构分别与四种组蛋白 H3 尾部构象（两种线性、两种螺旋，含 H3 前 11 个氨基酸 ARTKQTARKST）进行分子对接（Haddock 2.4 和 ClusPro 两种算法），对每个组合选取最优 4 个模型，用 PRODIGY 计算结合亲和力（ΔG）和解离常数（Kd），最后用双样本 t-test 检验线性 vs. 螺旋构象的亲和力差异是否显著。

### 2) 核心洞察
**IDR 的构象状态本身是结合选择性的决定因素，而非仅 PTM 代码。** 具体而言：组蛋白尾部虽然是 IDR，但其不同构象（线性 vs. 螺旋）对 ING PHD finger 的可及性和互补性有本质差异——线性构象暴露更多残基参与氢键和疏水相互作用（7 个氨基酸参与互作），而螺旋构象因残基被包裹在螺旋内部，仅 4 个氨基酸可及。这提示 IDR 的构象偏好（可能受 PTM 调控）是 reader 选择性的一个未被充分认识的维度。

### 3) 可能的普适教训 [Analysis]
- **对 IDP/IDR 互作研究**: 评估 IDR 介导的互作时，不能仅考虑序列基序和 PTM，必须将 IDR 的构象系综（conformational ensemble）纳入考量。计算流程（docking + 能量预测 + 统计检验）可作为系统评估 IDR 构象效应的模板。
- **对相分离/凝聚体研究**: 相分离中 IDR 的构象异质性直接影响多价互作和凝聚体形成。本文的方法可迁移为：对不同构象状态的 IDR 片段与互作伙伴进行 docking，评估构象偏好对凝聚体驱动力的贡献。
- **对 AI 方法**: 本文提示，AlphaFold 等结构预测工具对 IDR 的构象系综预测能力有限，未来 AI 方法应关注 IDR 的构象分布预测，而非单一结构。

## 07 方法总览

- **输入**: 
  - 4 个 ING 蛋白 PHD finger 晶体结构（来自 PDB）
  - 4 个组蛋白 H3 尾部构象模型（2 线性 + 2 螺旋，11 个氨基酸，UCSF Chimera 建模）
  - MOZ PHD-H3 复合物晶体结构（PDB: 4LK9，用于方法验证）
- **输出**: 
  - 每个 ING-H3 组合的结合亲和力（ΔG）和 Kd
  - 线性 vs. 螺旋构象的亲和力差异统计检验结果
  - 蛋白-蛋白相互作用图谱（LigPlot）
- **模块**:
  1. 结构准备: PDB 结构获取、UCSF Chimera 建模 H3 尾部构象
  2. 活性位点预测: CASTp 识别 PHD finger 活性/被动残基
  3. 分子对接: Haddock 2.4（信息驱动柔性对接）+ ClusPro（刚性对接）
  4. 结合能预测: PRODIGY 计算 ΔG 和 Kd
  5. 相互作用分析: LigPlot 可视化氢键和疏水接触
  6. 统计分析: 双样本 t-test（99% 置信水平）
- **训练**: 不适用（无机器学习训练）
- **反馈回路**: 无显式反馈回路；Haddock 2.4 使用 CASTp 定义的活性残基作为 AIRs 约束
- **假设**: 
  - PHD finger 在结合过程中不发生显著构象变化（刚性假设，ClusPro 中更明显）
  - PRODIGY 对 IDR 肽段复合物的能量预测可靠
  - 计算得到的亲和力排序可反映实验结合倾向

**文字流程**: PDB 获取 ING PHD 结构 → UCSF Chimera 建模 4 种 H3 尾部构象 → CASTp 预测 PHD 活性位点 → Haddock 2.4 和 ClusPro 分别对接 16 种组合 → 每组合选最优 4 模型 → PRODIGY 计算 ΔG/Kd → 按构象类型分组（线性 vs. 螺旋）→ t-test 检验差异 → LigPlot 分析代表性复合物的互作模式 → 用 MOZ PHD-H3（已知偏好螺旋）验证方法可靠性。

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| 结构建模（UCSF Chimera） | 构建 H3 尾部的线性/螺旋构象模型 | 无实验结构覆盖所有构象状态，需计算建模 | 输入: H3 序列 (ARTKQTARKST)；输出: 4 个 3D 构象 | Methods "Structural design" 节 | 预期影响: 无法系统比较构象效应，研究无法进行 [Analysis] |
| 活性位点预测（CASTp） | 定义 PHD finger 的活性/被动残基 | Haddock 2.4 需要 AIRs 约束来引导对接 | 输入: PHD 结构；输出: 活性/被动残基列表 | Methods "Molecular docking analysis" 节 | 预期影响: Haddock 对接精度下降，可能产生假阳性复合物 [Analysis] |
| 分子对接（Haddock 2.4 + ClusPro） | 生成 ING-H3 复合物模型 | 两种算法互补，交叉验证结果可靠性 | 输入: PHD 结构 + H3 构象 + 约束；输出: 复合物模型及评分 | Methods "Molecular docking analysis" 节；Results 图 4 | 实测影响: 两种算法结果一致（均显示线性偏好），移除任一算法则无法交叉验证 |
| 结合能预测（PRODIGY） | 计算 ΔG 和 Kd | 定量比较不同构象的亲和力差异 | 输入: 复合物结构；输出: ΔG, Kd | Methods "Molecular docking analysis" 节；Results 图 4 | 预期影响: 无法定量比较亲和力，只能定性比较 docking score [Analysis] |
| 相互作用分析（LigPlot） | 可视化复合物中氢键和疏水接触 | 解释亲和力差异的结构基础 | 输入: 复合物结构；输出: 2D 互作图 | Results "Similar binding patterns" 节；图 5-7 | 预期影响: 无法解释为何线性构象亲和力更高 |
| 统计检验（t-test） | 检验线性 vs. 螺旋亲和力差异显著性 | 判断观察到的差异是否具有统计意义 | 输入: 每组 32 个 ΔG 值；输出: p 值 | Results "Linear conformations are preferred" 节 | 预期影响: 无法确认差异是否显著，结论缺乏统计支撑 |
| 方法验证（MOZ PHD-H3） | 用已知偏好螺旋构象的体系验证流程 | 确保计算流程能正确捕捉构象偏好 | 输入: MOZ PHD 结构 + H3 构象；输出: 亲和力比较 | Discussion 节 | 预期影响: 无法确认方法可靠性，结果可能受系统误差影响 |

## 09 关键公式符号

本文未使用复杂数学公式。核心定量工具为：

1. **结合自由能（ΔG）**: 由 PRODIGY 基于原子接触预测，单位 kcal/mol。用于比较不同构象的亲和力。来源: PRODIGY 方法（Vangone & Bonvin, 2017）。

2. **解离常数（Kd）**: 由 PRODIGY 从 ΔG 推导，单位 M。Kd = exp(ΔG/RT)，其中 R 为气体常数，T 为温度（文中报告 25.0 °C）。来源: PRODIGY 输出。

3. **双样本 t-test 统计量**: 
   t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)
   其中 x̄ 为均值，s² 为方差，n 为样本量（每组 n=32）。用于检验线性 vs. 螺旋构象的 ΔG 差异。来源: Methods "Molecular docking analysis" 节。

4. **Haddock 2.4 评分函数**: 加权组合 van der Waals、静电、去溶剂化和 AIR 约束能。具体公式未在文中给出，但描述为 "weighted combination of van der Waals, electrostatic, desolvation, and restraint violation energies and as well as buried surface area"（Methods 节）。

## 10 实验设计与证据链

**数据集/群体**:
- 4 个 ING 蛋白 PHD finger 结构（ING1、ING2、ING4、ING5，来自 PDB）
- 4 个 H3 尾部构象模型（2 线性 + 2 螺旋）
- 16 个 ING-H3 组合 × 2 种对接软件 × 4 个最优模型 = 128 个复合物模型
- 验证体系: MOZ PHD-H3 复合物（PDB: 4LK9）

**指标**:
- PRODIGY 预测的 ΔG（kcal/mol）和 Kd（M）
- Haddock 2.4 和 ClusPro 的 docking score
- LigPlot 识别的氢键和疏水接触数量

**基线/对照**:
- 螺旋构象作为线性构象的对照
- MOZ PHD-H3 复合物作为方法验证（已知偏好螺旋）
- 原始晶体结构数据作为参考值（图 4 绿线）

**评测协议**:
- 每个 ING-H3 组合取最优 4 个模型
- 按构象类型分组（线性 vs. 螺旋），每组 32 个 ΔG 值
- 双样本 t-test，99% 置信水平（p < 0.0001）

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|------------------|------|
| 16 种 ING-H3 组合对接（Haddock + ClusPro） | 线性构象比螺旋构象结合亲和力更高 | 线性 vs. 螺旋，两种对接软件 | 所有 ING 蛋白的线性构象 ΔG 均显著低于螺旋构象（p < 0.0001） | 组蛋白尾部构象显著影响 ING PHD 结合亲和力，线性构象被优先选择 | 不能证明该结论在体内成立；不能排除其他构象（如 bent）的影响 | Results 图 4 |
| MOZ PHD-H3 验证实验 | 计算流程能正确捕捉已知的构象偏好 | MOZ PHD 与 H3 螺旋构象对接，与实验结构对比 | 计算结果与实验一致，显示螺旋构象偏好 | 方法可靠，可用于 ING 体系 | 仅验证了一个体系，不能推广到所有 PHD-组蛋白互作 | Discussion 节 |
| LigPlot 互作分析（ING1 代表） | 线性构象提供更多互作残基 | 线性 vs. 螺旋复合物的氢键/疏水接触 | 线性构象 7 个残基参与互作（A1, R2, T3, K4, T6, R8, K9），螺旋构象仅 4 个（R2, K4, R8, T11） | 线性构象因暴露更多残基而获得更高亲和力 | 仅分析了 ING1 代表模型，未对所有组合进行 | Results 图 6-7 |
| 参考晶体结构对比 | 计算结果与实验结构一致 | 计算 ΔG vs. 晶体结构 PRODIGY 值 | ING1 参考值位于线性/螺旋之间，ING4/5 参考值接近线性 | 计算模型与实验数据基本一致 | 参考值来自不同实验条件，可比性有限 | Results 图 4 |

## 11 结论正确解读

- **任务范围**: 本文仅评估了组蛋白 H3 尾部两种极端构象（线性 vs. 螺旋）与 ING 家族 PHD finger 的结合亲和力差异。未覆盖其他构象状态（如 bent）、未考虑 PTM 与构象的协同效应、未包含 ING3（无晶体结构）。
- **oracle/真值输入**: 无实验测定的亲和力数据作为真值；仅用 MOZ PHD-H3 复合物（PDB: 4LK9）的已知构象偏好作为方法验证。PRODIGY 预测的 ΔG 是计算值，非实验测量值。
- **端到端状态**: 非端到端实验验证。计算流程（docking → 能量预测 → 统计检验）是完整的，但缺乏 wet-lab 验证（如 ITC、NMR 滴定）。
- **算力成本**: 未报告具体算力需求。使用在线服务器（ClusPro、Haddock 2.4、CASTp、PRODIGY），成本相对较低。
- **历史数据依赖**: 依赖 PDB 中已有的 ING PHD 晶体结构，这些结构来自不同实验条件，可能引入偏差。
- **模型依赖**: 结果高度依赖 docking 软件和 PRODIGY 的准确性。两种 docking 软件结果一致增加了可信度，但 PRODIGY 对 IDP 肽段复合物的预测能力未经验证。
- **最难情形**: 螺旋构象中残基被包裹导致互作减少，这是最直观的解释，但未考虑构象动态（IDP 在结合过程中可能发生构象转变）。
- **群体/领域边界**: 结论仅适用于 ING 家族 PHD finger 与 H3 尾部的互作。不能推广到其他 PHD finger 或组蛋白尾部修饰状态。
- **不确定性**: 未报告置信区间或误差范围；t-test 仅报告 p < 0.0001，未给出效应量。

**有边界的复述**: 在计算层面，组蛋白 H3 尾部的线性构象比螺旋构象与 ING1/2/4/5 PHD finger 的结合亲和力显著更高（p < 0.0001），该效应在两种 docking 软件中一致，且经 MOZ PHD-H3 体系验证方法可靠。但该结论尚未经实验验证，且不排除其他构象或 PTM 的调节作用。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| ING3 缺失 | ING3 无实验验证的晶体结构，无法纳入研究 | 未明确提及 | Methods "Structural design" 节 |
| 计算方法的固有局限 | 分子对接对 IDP 柔性处理有限 | 未明确提及 | 全文隐含 |
| 构象模型简化 | 仅构建了线性/螺旋两种极端构象，未覆盖中间状态 | "Further research is needed to better understand the mechanisms and also the possible relation between PTMs and the final conformation of the histone tail" | Conclusions 节 |
| PTM 与构象的协同未研究 | 未考虑 H3K4me3 等 PTM 与构象的交互效应 | "Further research... possible relation between PTMs and the final conformation" | Conclusions 节 |
| 缺乏实验验证 | 全部为计算预测，无 wet-lab 数据 | 未明确提及 | 全文隐含 |

**作者提及的相关约束**（非正式局限）:
- 使用小鼠 ING2 结构替代人类（因无人类晶体结构），但论证了序列一致性
- 仅用 MOZ 一个体系验证方法可靠性

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 构象模型过于简化 | 真实 IDP 构象系综远不止线性/螺旋两种状态，可能还有其他中间构象具有更高亲和力 | 若存在未探索的构象状态，结论可能不完整 | 使用 MD 模拟或构象系综采样生成更多构象状态进行 docking | Methods 仅描述 "two linear, two helical" 构象 |
| PRODIGY 对 IDP 肽段的适用性未验证 | PRODIGY 基于 globular protein 复合物训练，对 IDP 肽段的预测可能不准 | 若能量预测有偏，ΔG 差异可能被夸大或缩小 | 用实验数据（ITC、SPR）验证部分复合物的亲和力 | Methods 引用 PRODIGY 为 "atomic contacts-based prediction method" |
| 未考虑 PTM 与构象的交互 | 实际体内 H3K4me3 修饰可能改变尾部构象偏好，从而改变结论 | 若 PTM 诱导螺旋构象且增强结合，则结论需修正 | 对 K4me3 修饰的 H3 尾部进行同样的 docking 分析 | Introduction 提到 PTM 是已知结合决定因素，但 Methods 未纳入 |
| 刚性受体假设 | ClusPro 假设 PHD finger 刚性，Haddock 虽允许柔性但限于侧链，可能忽略 induced fit 效应 | 若 PHD finger 结合时发生构象变化，亲和力排序可能改变 | 使用 MD 模拟或 ensemble docking 方法 | Methods 描述 ClusPro 为 "rigid body docking algorithm" |
| 样本量小 | 仅 4 个 ING 蛋白、4 个构象，统计功效有限 | 结论的普适性存疑 | 扩展至更多 PHD finger 蛋白和更多构象变体 | Results 仅报告 4 个 ING 蛋白 |
| 缺乏阴性对照 | 未测试已知不结合 H3 的 PHD finger 作为阴性对照 | 无法排除 docking 方法本身偏好线性肽段的系统性偏差 | 加入已知不结合 H3 的 PHD 结构域作为阴性对照 | Methods 未提及阴性对照 |
| 验证体系单一 | 仅用 MOZ 一个体系验证方法，且 MOZ 与 ING 同属 PHD finger 家族，可能存在家族特异性偏差 | 方法可能对 PHD finger 家族有系统性偏好 | 用非 PHD finger 的 H3 结合蛋白（如 HP1 chromodomain）验证 | Discussion 仅提及 MOZ 验证 |

## 14 Agent 提炼的知识候选

**可迁移概念**:

1. **IDR 构象作为结合选择性决定因素**: 本文核心概念——IDR 的构象状态（而非仅序列/PTM）可显著影响结合亲和力。对 IDP/IDR × 蛋白互作研究，这意味着评估互作时必须考虑构象系综，而非单一结构。

2. **计算流程模板**: docking（Haddock + ClusPro 双软件交叉验证）→ 能量预测（PRODIGY）→ 统计检验（t-test）→ 互作模式分析（LigPlot）→ 已知体系验证（MOZ）。该流程可作为 IDR-蛋白互作计算筛选的标准化模板。

3. **构象-亲和力关系的统计检验框架**: 将构象类型作为分组变量，对能量预测结果进行 t-test，为计算结果提供统计显著性支撑。

**可迁移方法**:

4. **双软件交叉验证策略**: 使用两种不同算法（信息驱动柔性 docking + 刚性 docking）交叉验证结果，降低单一软件偏差。可迁移到 IDR-蛋白 docking 研究中。

5. **已知偏好体系作为方法验证**: 用实验已知构象偏好的体系（MOZ-H3 螺旋）验证计算流程的可靠性，增强结果可信度。可迁移到其他 IDR 互作体系。

6. **LigPlot 互作模式对比**: 通过对比不同构象复合物的氢键/疏水接触数量，解释亲和力差异的结构基础。可迁移到 IDR 互作机制分析。

**对课题方向的启示**:

7. **对相分离研究**: 本文提示 IDR 构象偏好可能影响多价互作的强度和特异性，进而影响相分离/凝聚体的形成。可设计类似计算流程评估不同构象状态的 IDR 片段与互作伙伴的亲和力，预测凝聚体驱动力。

8. **对 AI 方法**: 本文强调 IDR 构象异质性的重要性，提示 AlphaFold 等结构预测工具对 IDR 的单一结构预测不足以捕捉功能相关构象。未来 AI 方法应关注 IDR 构象系综预测，或开发构象感知的互作预测模型。

9. **对 MD 模拟**: 本文的 docking 方法可作为 MD 模拟的初筛工具，快速识别高亲和力构象-蛋白组合，再用 MD 验证动态结合过程。

## 15 与已有知识连接

- **Vangone & Bonvin (2017)**: PRODIGY 方法原始文献，本文使用该工具预测结合亲和力。PRODIGY 基于原子接触预测 ΔG，对 globular 蛋白复合物验证良好，但对 IDP 肽段适用性需注意。

- **De Vries, Van Dijk & Bonvin (2010); Van Zundert et al. (2016); Honorato et al. (2021)**: Haddock 2.4 方法学文献，本文使用该工具进行信息驱动柔性 docking。Haddock 支持 AIRs 约束，适合利用已知活性位点信息引导 docking。

- **Kozakov et al. (2017); Desta et al. (2020); Vajda et al. (2017)**: ClusPro 方法学文献，本文使用该工具进行刚性 docking。ClusPro 基于 PIPER 算法，适合快速筛选。

- **Wang et al. (2000)**: 组蛋白尾部乙酰化增加 α-螺旋含量的实验证据，本文引用以支持螺旋构象的生理相关性。

- **Klein et al. (2017); Local et al. (2018)**: MORF、DPF3 等 PHD finger 与螺旋构象 H3 结合的实验证据，本文用于对比 ING 家族偏好线性构象的差异。

- **Bortoluzzi et al. (2017)**: 组蛋白尾部与 PHD finger 结合时存在螺旋、弯曲、完全伸展三种构象的计算研究，本文在此基础上聚焦线性 vs. 螺旋的对比。

- **Champagne & Kutateladze (2009); Champagne et al. (2008); Peña et al. (2006); Li et al. (2006); Kwan et al. (2003)**: ING PHD finger 识别 H3K4me3 的结构与功能研究，本文的互作模式分析与此一致。

- **Uversky, Gillespie & Fink (2000); Van der Lee et al. (2014)**: IDP 经典文献，本文引用以支持组蛋白尾部为 IDR 的论断。

- **对本课题的关联**: 本文为「IDR 构象 × 蛋白互作」提供了计算证据，与相分离研究中 IDR 构象系综调控多价互作的观点一致。其计算流程可迁移至其他 IDR-蛋白互作体系，也可为 AI 方法提供构象敏感的训练数据生成策略。

## 16 Agent 生成的研究候选

**候选 1: IDR 构象感知的互作预测模型**
- **来源局限/观察**: 本文证明构象显著影响 IDR-蛋白亲和力，但现有 AI 互作预测工具（如 AlphaFold-Multimer）仅预测单一结构，忽略构象系综。
- **核心假设**: 将 IDR 构象系综信息（如螺旋倾向、柔性分布）作为额外特征输入互作预测模型，可提高 IDP 参与互作的预测精度。
- **初步方法**: 对已知 IDR-蛋白复合物进行 MD 采样生成构象系综，提取构象特征（螺旋含量、溶剂可及性、残基波动），训练 GNN 或 transformer 模型预测结合亲和力。
- **验证方式**: 在本文 ING-H3 数据集及 PDB 中其他 IDR-蛋白复合物上测试，与 AlphaFold-Multimer 基线对比。
- **创新状态**: unverified

**候选 2: 相分离驱动力的构象选择性计算评估**
- **来源局限/观察**: 本文聚焦二元互作，但 IDR 构象偏好同样可能影响多价互作和相分离。现有相分离预测工具（如 catGRANules）主要基于序列组成，忽略构象。
- **核心假设**: IDR 的构象偏好（线性 vs. 螺旋）通过改变互作位点可及性，影响多价互作的强度和相分离倾向。
- **初步方法**: 对相分离相关 IDR（如 FUS、TDP-43）构建不同构象模型，与已知互作伙伴进行 docking，计算多价互作网络强度，与实验相分离数据（饱和浓度）关联。
- **验证方式**: 使用文献中已有相分离实验数据（如 LLPS 饱和浓度）作为 ground truth，检验构象感知的互作评分是否能更好预测相分离倾向。
- **创新状态**: unverified

**候选 3: PTM-构象协同效应的系统计算扫描**
- **来源局限/观察**: 本文未考虑 PTM 与构象的交互，但已知乙酰化可改变组蛋白尾部螺旋含量（Wang et al., 2000），PTM 可能通过改变构象间接调控结合。
- **核心假设**: 某些 PTM 通过改变 IDR 构象偏好（而非直接接触）来调控 reader 结合，存在「PTM-构象-亲和力」的间接调控路径。
- **初步方法**: 对 H3 尾部进行系统 PTM 修饰（甲基化、乙酰化、磷酸化），用 MD 模拟或构象采样评估各 PTM 状态的构象偏好，再对高偏好构象进行 docking 分析。
- **验证方式**: 与实验数据（如 ITC 测定的不同 PTM 状态亲和力）对比，检验构象介导的间接调控是否可预测。
- **创新状态**: unverified

**候选 4: IDR 构象偏好作为 reader 家族特异性的决定因素**
- **来源局限/观察**: 本文发现 ING 家族偏好线性构象，而 MOZ/DPF3 偏好螺旋构象，提示不同 reader 家族可能有不同的构象偏好。
- **核心假设**: PHD finger 的序列/结构特征（如结合沟深度、疏水残基分布）决定其对 IDR 构象的偏好，可作为 reader 家族分类的新维度。
- **初步方法**: 对 PDB 中所有 PHD finger-H3 复合物进行构象分析，提取结合态 H3 的构象特征，与 PHD 序列特征关联，训练分类器预测构象偏好。
- **验证方式**: 在留出集上测试分类精度，并用 docking 验证预测的构象偏好。
- **创新状态**: unverified