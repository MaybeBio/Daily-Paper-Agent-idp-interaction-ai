## 01 基本信息

- **标题**：Extending the MAD Toolbox: New Polymer Builder and Enhanced Martini Database
- **作者**：Marin R; Hilpert C; Grunewald F; Valerio M; Borges L; Janczarski S; Rossini N; Marrink S; Telles de Souza P; Launay G
- **单位**：未提供（根据通讯作者邮箱推断为 ENS de Lyon，法国里昂高等师范学校）
- **期刊/平台**：bioRxiv（预印本）
- **年份**：2026
- **论文类型**：方法/工具论文（软件更新报告）
- **领域**：粗粒化分子动力学模拟、Martini 力场、计算生物学工具开发
- **关键词**：Martini 3、粗粒化、MAD 服务器、聚合物构建器、GōMartini、无序蛋白、脂质组
- **DOI/ID**：10.64898/2026.01.23.700524
- **代码**：https://gitbio.ens-lyon.fr/LBMC/damm/mad/paper2026_si
- **数据**：MAD:Database（https://mad.ens-lyon.fr/explore）
- **阅读日期**：2026-05-13
- **该文在课题方向中的位置**：本文属于「无序蛋白/相分离 × 蛋白互作 × 物理模拟」方向中的**工具/基础设施层**贡献。它不直接研究 IDP 互作机制，而是为 IDP/IDR 的 Martini 3 CG 模拟提供**建模工具链**——特别是 MAD:Polymer Builder 支持从序列直接构建 IDP 的 CG 模型（利用 Martini3-IDP 扩展），以及 MAD:Molecule Builder 支持 GōMartini 与 water bias 的交互式配置，这些能力直接服务于 IDP 构象采样、IDP-膜互作、IDP 复合物组装等课题的模拟前处理环节。

---

## 02 一句话总结

本文报告了 MAD 服务器（https://mad.ens-lyon.fr）的重大更新：新增基于 polyply 框架的 MAD:Polymer Builder（支持从序列/图结构自动构建 Martini 3 CG 聚合物模型，包括合成聚合物、多糖和 IDP），升级 MAD:Molecule Builder 以支持 GōMartini 3 寡聚体建模和 water–protein interaction bias 配置，并将 MAD:Database 扩展至 1,274 个 CG 模型（含最新 Martini 3 lipidome），通过案例研究验证了生成模型的 Martini 3 模拟兼容性。

---

## 03 研究问题

**具体问题**：如何将 MAD 服务器从「分子数据库+基础转换工具」升级为覆盖更广分子类型（特别是聚合物和 IDP）的综合性 CG 建模平台，以满足 Martini 3 力场用户日益增长的自动化建模需求？

**为什么重要**：Martini 3 力场已广泛应用于生物分子、软物质和复杂材料体系的 CG 模拟，但缺乏统一的、用户友好的、支持复杂聚合物架构（支链、嵌段、无序蛋白）的自动化建模工具，限制了非专家用户的使用门槛和复杂体系的建模效率。

**现有方法为何不足**：
- 现有工具如 polyply 功能强大但需要命令行操作和编程知识，缺乏图形化界面；
- martinize2 支持蛋白建模但不支持合成聚合物；
- 其他工具（bentopy、COBY、TS2CG 等）各有所长但互不兼容，缺乏统一生态；
- 已有 CG 模型分散在不同来源，缺乏集中式数据库和 API 支持。

**精确的「Can ... ?」研究问题**：Can a web-based platform integrate polymer graph-based building, IDP-aware CG parametrization (Martini3-IDP), GōMartini oligomer modeling, and a searchable database with REST API into a unified, user-friendly ecosystem for Martini 3 CG simulation preparation?

---

## 04 背景与发展脉络

**阶段一：Martini 力场早期工具（2010s）**
- 代表性方法：Martini 2 力场 + 手动建模
- 优点：简单、计算效率高
- 局限：缺乏自动化工具，建模依赖专家经验

**阶段二：自动化建模工具涌现（2015-2021）**
- 代表性方法：martinize2（蛋白）、polyply（聚合物）、insane（膜）、TS2CG、COBY
- 优点：各自领域内自动化程度提高
- 局限：工具分散、互不兼容、学习曲线陡峭、缺乏统一数据库

**阶段三：Martini 3 力场发布（2021-2023）**
- 代表性方法：Martini 3 力场 + 配套工具更新
- 优点：改进的相互作用参数、更广的化学空间覆盖
- 局限：新力场需要新工具支持，IDP 建模仍需专门处理

**阶段四：集成化平台时代（2023-至今）**
- 代表性方法：MAD 服务器（本文）、CHARMM-GUI Multicomponent Assembler
- 优点：统一生态、图形界面、数据库+工具集成
- 局限：仍在发展中，部分高级功能（如自动二面角生成）尚未完善

**本文主张的位置**：MAD 作为 Martini 生态的「一站式」Web 平台，通过 Polymer Builder 填补了聚合物/IDP 自动化建模的空白，通过数据库+API 实现了 CG 模型的集中管理和程序化访问。

> 注：此脉络基于本文引言和结论部分的叙述整理，属于「仅本文框架」，未经外部文献系统核验。

---

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 聚合物建模门槛高 | 用户需掌握 polyply 的命令行操作和图语法 | 现有工具面向专家，缺乏图形化界面 | 引言：polyply 等工具「each addressing different aspects of system assembly」；Polymer Editor 作为「graphical user interface and workflow manager for polyply」 |
| 工具碎片化 | 不同分子类型需使用不同工具，格式不互通 | 各工具独立开发，缺乏统一生态 | 引言：列举 bentopy、martinize2、COBY、TS2CG、polyply 等各自为政 |
| IDP 建模缺乏专门支持 | 标准 Martini 3 对无序蛋白的构象描述不准确 | IDP 需要专门的键合参数和相互作用修正 | Methods：MAD:Polymer Builder 支持 Martini3-IDP 扩展；Molecule Builder 新增「Define disordered region」选项 |
| 蛋白复合物建模受限 | 寡聚体的 Gō 网络配置复杂，难以手动完成 | 多链间相互作用需要精细调控 | Methods：Molecule Builder 支持「GōMartini 3 for protein complexes」；案例中 InhA 四聚体的链间 Gō 键编辑 |
| 数据库分散、不可编程访问 | CG 模型散落各处，难以批量获取 | 缺乏集中式存储和 API | Methods：MAD:Database 新增 REST API，支持 GET/LIST 操作 |
| 膜-蛋白互作建模困难 | 蛋白-膜界面相互作用需要精细调节 | 标准 Martini 3 对蛋白-水/膜界面描述不足 | Methods：water–protein interaction bias 可独立设置于 α-helix、β-strand、coil 区域；α-synuclein 案例 |

---

## 06 核心思想

### 1) 表面方法

本文表面上是 MAD 服务器的功能扩展报告：新增 Polymer Builder、升级 Molecule Builder、扩充 Database、提供 REST API。具体技术手段包括：
- 将 polyply 封装为 Web 图形界面（MAD:Polymer Editor）
- 集成 Martini3-IDP 扩展和 GōMartini 3 到 Molecule Builder
- 将 Martini 3 lipidome 等新模型纳入数据库
- 重构后端架构以提高模块化和可移植性

### 2) 核心洞察

**洞察一：CG 建模的瓶颈已从「力场精度」转向「工具可用性」**。Martini 3 力场本身已足够成熟，但用户无法有效利用——特别是非专家用户。MAD 的更新本质上是将「专家知识」（polyply 语法、Gō 网络配置、IDP 参数选择）编码为图形化工作流，降低使用门槛。

**洞察二：IDP 建模需要「混合策略」**。α-synuclein 案例展示了关键思路：同一蛋白的不同区域采用不同的建模策略——有序的 α-螺旋区用 GōMartini 保持结构，无序的 C-端用 Martini3-IDP 描述构象。这种「分区处理」是 IDP 相关 CG 模拟的核心方法论。

**洞察三：生态比工具更重要**。MAD 的价值不仅在于单个工具，而在于「数据库→构建器→系统组装→模拟」的完整链路。API 的引入使第三方工具可以程序化调用 MAD 资源，形成可扩展的生态。

### 3) 可能的普适教训 [Analysis]

**教训一**：对于 IDP/相分离研究，工具链的「交互式调试」能力至关重要。MAD 允许用户可视化地编辑 Gō 网络、调整 water bias，这种「所见即所得」的建模方式比黑箱自动化更适合科研探索——因为 IDP 的构象 ensemble 高度依赖建模参数的选择。

**教训二**：「序列驱动」的建模范式对 IDP 研究有启发意义。MAD:Polymer Builder 从 FASTA 序列直接生成 IDP 的 CG 模型（无需原子结构），这意味着**序列信息本身足以启动 IDP 模拟**——这对于缺乏实验结构的 IDP 体系尤为重要。

**教训三**：数据库+API 的模式可迁移到 IDP 互作研究。如果 IDP 的 CG 模型、Gō 网络配置、water bias 参数等能被系统化存储和共享，将极大促进 IDP 模拟结果的可重复性和跨课题组比较。

---

## 07 方法总览

**输入**：
- 用户提供的分子序列（FASTA 格式，适用于蛋白/多肽）
- 或分子图结构（适用于合成聚合物、多糖）
- 或上传的 GROMACS ITP 文件 / polyply JSON 文件
- 或从 MAD:Database 中选择已有 CG 模型

**输出**：
- 完整的 Martini 3 CG 拓扑文件（ITP）
- 初始坐标文件（GRO）
- 可选的 GōMartini 网络配置（含链内/链间 Gō 键）
- 可选的 water–protein interaction bias 参数
- 系统组装所需的辅助文件（TOP 等）

**核心模块**：
1. **MAD:Polymer Editor**（新增）— 基于 polyply 的图形化聚合物构建器
2. **MAD:Molecule Builder**（升级）— 支持 GōMartini 3、Martini3-IDP、water bias
3. **MAD:System Builder**（升级）— 支持 lipidome 模型、兼容性检查
4. **MAD:Database**（扩展）— 1,274 个 CG 模型，976 个分子，REST API
5. **MAD:History** — 用户会话管理，跨工具数据流转

**训练/验证**：不适用（非机器学习方法）。验证方式为案例研究 + 短时 CG MD 模拟确认稳定性。

**工具链**：GROMACS 2024.x/2025.x、polyply、martinize2 (v0.15.0)、Martini 3 力场、Martini3-IDP 扩展、GōMartini 3

**文字流程**：
1. 用户登录 MAD 服务器，选择目标工具（Polymer Editor 或 Molecule Builder）
2. 输入序列（FASTA）或上传结构文件，或从 Database 选择模板
3. 在图形界面中编辑分子图：添加/删除节点（building blocks）、定义连接（edges）
4. 对于蛋白：选择力场变体（Martini 3 / Martini3-IDP）、配置 GōMartini 参数（链内/链间）、设置 water bias（按二级结构区域）
5. 服务器调用 polyply gen params 生成 ITP 参数文件；若失败，错误连接在界面中高亮（红色），用户手动选择 bond 参数
6. 生成坐标文件，进行能量最小化，输出松弛结构
7. 用户下载 ITP/TOP/GRO/PDB 文件，或直接转入 System Builder 进行膜/溶剂环境组装
8. 可选：将生成的模型存入个人 MAD:History，供后续会话使用

---

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| **MAD:Polymer Editor** | 图形化构建聚合物分子图，管理 building blocks 和连接 | 聚合物（合成、多糖、IDP）的自动化建模此前缺乏 Web 界面支持 | 输入：FASTA/图结构/ITP/JSON；输出：ITP/GRO/PDB | 案例：dextran、Sic1、PS-PMA 嵌段共聚物、PEG-lipid 均成功构建 | 预期影响：聚合物建模退回命令行 polyply，非专家用户无法使用（预期效应，未实测） |
| **MAD:Molecule Builder（GōMartini 3 支持）** | 交互式配置链内/链间 Gō 键网络，支持寡聚体 | 蛋白复合物的结构保持需要精细的 Gō 网络控制 | 输入：蛋白结构/序列；输出：含 Gō 网络的 ITP | InhA 四聚体案例：链间 Gō 键可编辑，移除过度约束的键后恢复生理波动 | 实测效应：InhA 案例中移除 164-165 残基的链间 Gō 键后，MD 波动与全原子参考一致 |
| **MAD:Molecule Builder（Martini3-IDP 支持）** | 定义无序区域，应用 IDP 专用键合参数 | 标准 Martini 3 对 IDP 构象描述不足 | 输入：蛋白序列+无序区域标注；输出：IDP 优化的 ITP | α-synuclein 案例：C-端无序区用 Martini3-IDP，螺旋区用 GōMartini | 预期影响：IDP 区域构象 ensemble 失真，回缩/聚集行为不准确（预期效应，未实测） |
| **MAD:Molecule Builder（water bias）** | 按二级结构设置蛋白-水相互作用修正 | 改善蛋白-膜/蛋白-水界面的行为 | 输入：蛋白结构+bias 参数（α/β/coil）；输出：含 bias 的 ITP | α-synuclein 案例：-1 kJ/mol α-helical water bias 稳定膜结合 | 预期影响：膜结合亲和力偏差，螺旋-膜界面行为异常（预期效应，未实测） |
| **MAD:Database** | 存储和检索 1,274 个 CG 模型 | 提供经过验证的 Martini 3 模型，避免重复参数化 | 输入：查询参数；输出：模型文件/JSON 列表 | Table 1：lipidome 加入后模型数大幅增加 | 预期影响：用户需自行参数化常见分子，效率降低（预期效应，未实测） |
| **REST API** | 程序化访问数据库 | 支持第三方工具集成和批量处理 | 输入：HTTP 请求（GET/LIST）；输出：模型文件/JSON | Methods 节：API 格式详细说明 | 预期影响：无法自动化工作流，MAD 生态封闭（预期效应，未实测） |
| **MAD:History** | 跨工具保存用户工作状态 | 支持多步骤工作流（构建→组装→模拟） | 输入：用户会话；输出：历史模型 | Methods：Polymer Editor 可从 History 启动 | 预期影响：多步骤工作流需重复上传/配置（预期效应，未实测） |

---

## 09 关键公式符号

本文为工具/方法论文，不涉及新的理论公式。以下列出与理解方法相关的关键参数和概念：

**1. GōMartini 3 Lennard-Jones 势**（用于结构保持）：
\[
V_{Gō}(r) = 4\varepsilon_{Gō}\left[\left(\frac{\sigma_{Gō}}{r}\right)^{12} - \left(\frac{\sigma_{Gō}}{r}\right)^{6}\right]
\]
- \( \varepsilon_{Gō} \)：Gō 键的相互作用强度（用户可调，InhA 案例中通过界面调整）
- \( \sigma_{Gō} \)：由参考结构中残基间距离决定
- 用途：保持蛋白二级/三级结构，防止 CG 模拟中结构塌缩
- 来源：Methods 节「GōMartini 3」配置部分

**2. Water–protein interaction bias**（水-蛋白相互作用修正）：
\[
\Delta V_{bias} = \varepsilon_{bias} \cdot f(\text{secondary structure})
\]
- \( \varepsilon_{bias} \)：偏置强度（α-synuclein 案例中设为 -1 kJ/mol 用于 α-helix）
- \( f(\text{secondary structure}) \)：按 α-helix、β-strand、coil 区域分别施加
- 用途：修正 Martini 3 对蛋白-水/膜界面的描述
- 来源：Methods 节「water biases」部分

**3. Martini3-IDP 键合参数**（无序蛋白专用）：
- 对 IDP 区域使用优化的键长、键角和二面角势参数
- 具体参数值未在文中给出，引用自 Martini3-IDP 原始文献 [14]
- 用途：改善无序蛋白的构象 ensemble 采样
- 来源：Methods 节「Martini3-IDP」部分

**4. 非键相互作用参数**（Martini 3 标准）：
- Lennard-Jones 截断：1.1 nm（potential-shift scheme）
- 静电：reaction-field 方法
- 来源：补充材料「Coarse-grained molecular dynamics simulations」部分

---

## 10 实验设计与证据链

**数据集/群体**：
- 案例 1：dextran（α-1,6-连接葡萄糖多糖，线性链）
- 案例 2：Sic1（酿酒酵母周期蛋白依赖性激酶抑制剂，残基 1-90，IDP）
- 案例 3：PS-PMA 嵌段共聚物（聚苯乙烯-聚丙烯酸甲酯，各 20 个单体）
- 案例 4：PEG-lipid（聚乙二醇-脂质，含四氢呋喃基团和油酸链）
- 案例 5：InhA（结核分枝杆菌烯酰-ACP 还原酶，四聚体，含 GōMartini 建模）
- 案例 6：α-synuclein（膜结合态，α-螺旋区 + 无序 C-端）

**规模**：每个案例为单一分子体系，未报告大规模统计。

**指标**：
- 建模成功率（能否生成完整 ITP/坐标文件）
- 模拟稳定性（短时 CG MD 无数值崩溃）
- 结构合理性（与参考全原子模拟的结构波动对比，InhA 案例）

**基线**：无定量基线。InhA 案例中与全原子参考模拟进行定性对比。

**预算/资源**：未报告具体计算资源。

**骨干/仪器**：GROMACS 2024.x/2025.x，Martini 3 力场

**Oracle 输入**：InhA 案例使用未发表的蛋白结构（「unpublished structures」）；α-synuclein 使用 NMR 结构（PDB ID: 1XQ8）

**评测协议**：无标准 benchmark。验证方式为「生成→模拟→确认稳定」的流程性验证。

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|-----------|------|------------|------------------|------|
| Dextran 构建 | Polymer Editor 能构建多糖 | 线性 α-1,6-连接葡萄糖链 | 成功生成 ITP/GRO | 支持多糖建模能力 | 未验证支链多糖 | Results 图 3A |
| Sic1 构建 | Polymer Editor 能从 FASTA 构建 IDP | 残基 1-90，Martini3-IDP 力场 | 成功生成模型 | 支持序列驱动的 IDP 建模 | 未验证全长 Sic1 或与其他 IDP 力场对比 | Results 图 3B |
| PS-PMA 嵌段共聚物 | Polymer Editor 能构建嵌段共聚物 | 各 20 单体，手动连接缺失键 | 成功生成，缺失键通过编辑工具解决 | 支持异质嵌段共聚物 | 未验证更复杂架构（星形、刷形） | Results 图 3C |
| PEG-lipid | Polymer Editor 能处理分支结构 | 四氢呋喃 + PEG 分支 + 油酸 | 成功生成，缺失键手动解决，脂肪酸 bead 类型改为 SN4a | 支持分支脂质构建 | 未验证与实验表征的定量对比 | Results 图 3D |
| InhA 四聚体 | Molecule Builder 支持 GōMartini 寡聚体 | 野生型 vs 突变体，链间 Gō 键编辑 | 移除 164-165 残基过度约束的链间 Gō 键后，MD 波动恢复 | 支持交互式 Gō 网络优化 | 未报告突变体具体结果 | Results 图 4 |
| α-synuclein 膜结合 | 混合建模策略（Gō + IDP + water bias） | NMR 结构（1XQ8），α-螺旋区 Gō + water bias，C-端 IDP | 成功生成稳定模型 | 支持 IDP-膜体系的分区建模策略 | 未验证膜结合自由能或构象 ensemble 的定量准确性 | Results 图 5 |
| 系统稳定性 | 生成模型可用于标准 Martini 3 模拟 | 所有案例在 GROMACS 中短时模拟 | 所有系统稳定，无数值崩溃 | 生成文件与标准协议兼容 | 未进行长时间模拟或定量验证 | 补充材料 |

---

## 11 结论正确解读

**任务范围**：本文的验证范围仅限于「生成的文件能被 GROMACS 读取并稳定运行短时模拟」。这不是对 Martini 3 力场精度的验证，也不是对 IDP 构象 ensemble 准确性的验证。

**Oracle/真值输入**：InhA 案例使用了未发表的蛋白结构作为输入，α-synuclein 使用了 NMR 结构。这些结构本身是实验/计算产物，其误差会传播到 CG 模型中。

**端到端状态**：本文展示了「建模→模拟」的端到端流程可行性，但未展示「模拟→科学发现」的完整闭环。所有案例均为方法演示，未产生新的生物学/材料学结论。

**算力成本**：未报告。短时模拟仅用于稳定性检查，不代表生产级模拟的成本。

**历史数据依赖**：MAD:Database 中的模型来自文献和用户贡献，其质量取决于原始参数化工作。

**模型依赖**：所有功能依赖于 polyply、martinize2 和 Martini 3 力场的正确性。GōMartini 3 和 Martini3-IDP 的适用性有各自的边界条件。

**最难情形**：本文未测试的困难场景包括：超长 IDP（>500 残基）、多域蛋白复合物、含翻译后修饰的蛋白、蛋白-核酸复合物、液-液相分离体系。

**群体/领域边界**：结论仅适用于 Martini 3 力场框架内的 CG 模拟准备。不适用于全原子模拟、其他 CG 力场（如 MARTINI 2、SPICA、UNRES）或非平衡模拟。

**不确定性**：作者未提供定量不确定性分析。Gō 网络的手动编辑、water bias 参数选择等步骤存在用户依赖性，可能影响结果可重复性。

**有边界的复述**：本文证明 MAD 服务器能够为多种分子类型（多糖、IDP、合成聚合物、分支脂质、蛋白复合物）生成 Martini 3 兼容的 CG 模型，且这些模型在短时模拟中保持稳定。该结论不延伸至模型精度、生物学准确性或长时间模拟的可靠性。

---

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 缺乏自动二面角生成 | 「the lack of automated angle and dihedral generation remains a limitation」 | 未来开发自动拓扑生成策略，可能借鉴 AutoMartini、PyCGTOOL、Bartender 等 | Conclusion 节 |
| 手动 bond 编辑的视觉支持有限 | 「the visualization support during bond definition remains limited」 | 改进界面以更好地辅助用户定义 bond 参数 | Conclusion 节 |
| 蛋白结构预处理依赖外部工具 | 实验结构含缺失残基、不一致原子命名或不完整信息时，用户需手动清理 | 未来开发自动预处理流程 | Conclusion 节 |
| 翻译后修饰支持有限 | 文中提到脂质化等修饰「may be limited to cases where these modifications are already present in the reference atomistic structure」 | 未来集成更系统的 PTM 支持 | Conclusion 节 |
| 未实现 OLIVES 等新方法 | OLIVES 作为替代的蛋白柔性建模框架「not yet implemented in MAD」 | 未来可能集成 | Conclusion 节 |

**作者提及的相关约束**（非正式局限）：
- 案例研究仅用于验证文件生成和模拟稳定性，非定量 benchmark
- 部分案例使用了未发表的结构数据
- 模拟验证为短时运行，未进行长时间生产模拟

---

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|---------|---------|------|
| 验证深度不足 | 案例研究仅确认「文件生成+短时稳定」，未验证模型精度、构象 ensemble 质量或与实验数据的定量一致性 | 工具声称「ready for production simulations」，但「稳定」≠「准确」 | 对同一体系运行长时间 CG 模拟，与全原子模拟/实验数据（如 SAXS、FRET）定量对比 | 补充材料：模拟目的仅为「confirm stability」 |
| Gō 网络手动编辑的客观性 | InhA 案例中移除 164-165 残基的链间 Gō 键是基于「与全原子参考对比」的判断，但该判断标准未形式化 | 不同用户可能做出不同编辑决策，影响结果可重复性 | 多用户独立建模同一体系，比较输出差异；或制定明确的 Gō 键筛选标准 | Results 图 4D |
| water bias 参数选择的经验性 | α-synuclein 案例中 -1 kJ/mol 的 bias 值选择依据未明确说明 | bias 强度直接影响膜结合行为，缺乏系统扫描可能掩盖参数敏感性 | 对 bias 强度进行系统扫描（如 -0.5 至 -2 kJ/mol），观察膜结合行为的敏感性 | Results 图 5A |
| 「IDP 支持」的边界 | Martini3-IDP 仅对「定义为无序的区域」应用特殊参数，但无序/有序边界判定依赖用户输入 | IDP 的构象 ensemble 对边界定义敏感，错误划分可能导致人为的构象偏好 | 对同一 IDP 使用不同的无序区定义，比较生成的构象 ensemble | Methods 节「Define disordered region」 |
| 数据库增长策略 | 数据库从 1,274 个模型增长主要来自 lipidome 批量加入，用户贡献机制和质控流程未详细说明 | 数据库质量取决于模型来源的可靠性 | 检查数据库模型的来源标注和验证状态；建立社区贡献的同行评审机制 | Table 1 |
| 与现有工具链的互操作性 | 虽然支持 ITP/JSON 导入，但未提及与 CHARMM-GUI、Amber Tools 等主流工作流的双向兼容性 | 用户可能需要在多个平台间切换，降低采用意愿 | 测试从 CHARMM-GUI 生成的 Martini 输入导入 MAD 的兼容性 | Methods 节「uploading GROMACS ITP files」 |
| 性能基准缺失 | 未报告大型体系（如多聚体、长链聚合物）的建模耗时和资源消耗 | Web 服务器的实际可用性取决于性能 | 对 100+ 残基 IDP、10+ 链复合物进行建模性能测试 | 未提供 |

---

## 14 学到什么

**Agent 提炼的知识候选**：

1. **「分区建模」策略（可直接迁移）**：α-synuclein 案例展示了同一蛋白内不同区域采用不同建模策略的范式——有序区用 GōMartini 保持结构，无序区用 Martini3-IDP 描述构象，界面区用 water bias 调节。对于 IDP/IDR 介导的相分离研究，这种「混合建模」思路可迁移到多价互作体系：折叠域用 Gō 保持，IDR 用 IDP 参数，互作界面用 bias 调控。

2. **「序列驱动」的 IDP 建模流程（可直接迁移）**：MAD:Polymer Builder 从 FASTA 直接生成 IDP 的 CG 模型，无需原子结构。这意味着对于缺乏实验结构的 IDP 体系，可以仅凭序列信息启动模拟——这对相分离研究尤为重要，因为许多相分离蛋白缺乏高分辨率结构。

3. **Gō 网络的「过度约束」问题（方法学警示）**：InhA 案例中，默认 Gō 网络对 164-165 残基的链间约束过强，抑制了生理相关的构象波动。这提示在 IDP/IDR 互作模拟中，Gō 网络的使用需谨慎——IDR 的柔性是功能关键，过度约束会人为冻结构象。

4. **water bias 的「分区施加」思路（可迁移）**：bias 不是全局施加，而是按二级结构区域（α/β/coil）分别设置。对于 IDP-膜互作研究，可借鉴此思路：膜结合区施加吸引 bias，非结合区保持中性，以模拟 IDP 的「fuzzy」膜结合模式。

5. **数据库+API 的生态思维（基础设施层面）**：MAD 通过 REST API 实现程序化访问，使第三方工具可以集成其数据。对于 IDP/相分离领域，类似的「CG 模型数据库+API」模式可促进 IDR 参数的系统化共享和标准化。

6. **「错误可视化」的调试理念**：Polymer Editor 在 bond 参数缺失时高亮错误连接，引导用户手动修复。这种「可视化错误反馈」设计对 IDP 建模工具的开发有借鉴意义——IDP 的建模错误往往难以从文本日志中察觉。

7. **工具互操作性的重要性**：MAD 支持从 ITP/JSON 导入，允许用户从其他工具链迁移。在 IDP 研究中，这意味着用户可以在 MAD 中构建模型，然后导出到其他分析工具，形成灵活的工作流。

---

## 15 与已有知识连接

1. **Martini 3 力场**（Marrink et al., 2022, *Chem Sci*）：本文所有工具均基于 Martini 3 力场。Martini 3 重新定义了氨基酸 bead 类型和相互作用参数，是本文所有建模工作的基础。

2. **Martini3-IDP 扩展**（文献 [14]）：本文的 IDP 建模能力直接依赖此扩展。该扩展针对无序蛋白优化了键合参数，改善了 IDP 的构象 ensemble 描述。与本文的关联：MAD:Polymer Builder 和 Molecule Builder 均集成了此扩展。

3. **GōMartini 3**（文献 [15]）：本文的 GōMartini 支持基于此方法。GōMartini 通过引入 Gō 键保持蛋白结构，适用于折叠蛋白和复合物建模。与本文的关联：Molecule Builder 新增的寡聚体 Gō 网络编辑功能。

4. **polypy**（文献 [8]）：MAD:Polymer Builder 的后端引擎。polypy 是一个 Python 库，用于生成 Martini 兼容的聚合物拓扑。本文将其封装为 Web 界面。

5. **martinize2**（文献 [10]）：MAD:Molecule Builder 的基础工具。martinize2 将原子结构转换为 Martini CG 表示，本文升级至 v0.15.0。

6. **MAD 服务器前版**（文献 [9]）：本文是 MAD 的首次重大更新，前版主要提供数据库和基础转换功能。

7. **Martini 3 lipidome**（文献 [20]）：本文数据库扩展的主要来源。该 lipidome 提供了 Martini 3 兼容的脂质模型，对膜相关 IDP 研究（如 α-synuclein 案例）至关重要。

8. **CHARMM-GUI Multicomponent Assembler**（文献 [44]）：本文在结论中将其作为类似平台进行比较。该工具也提供 Web 界面的 Martini 系统组装功能，但本文强调 MAD 的数据库+API 优势。

9. **MDDB（Molecular Dynamics Data Bank）**（文献 [47]）：本文提出 MAD 与 MDDB 互补——MAD 提供拓扑和起始结构，MDDB 存储轨迹数据。对于 IDP 研究，这种「拓扑+轨迹」的完整数据链有助于相分离模拟数据的共享和复现。

10. **CGsmiles**（文献 [50]）：本文提出未来可能采用此标准进行 CG 模型表示。CGsmiles 提供分辨率无关的 CG 映射描述，可能促进不同 CG 力场间的模型转换。

---

## 16 研究想法

**Agent 生成的研究候选**：

### 候选 1：IDP 相分离体系的「分区建模」自动化工作流
- **来源局限/观察**：α-synuclein 案例展示了「Gō + IDP + water bias」混合建模的可行性，但该过程需要大量手动配置。相分离蛋白（如 FUS、TDP-43）通常包含多个折叠域和长 IDR，手动建模极为繁琐。
- **核心假设**：基于序列特征（如预测的无序区、螺旋倾向性、已知互作基序）自动划分「有序/无序」区域，并自动配置相应的 Gō 网络和 water bias，可以生成适用于相分离模拟的 CG 模型。
- **初步方法**：利用 IUPred/AlphaFold 预测无序区，结合互作基序注释，开发自动分区算法；集成到 MAD:Polymer Builder 中；在 FUS 低复杂度域体系上验证相分离行为。
- **验证方式**：比较自动生成模型与手动建模模型的相分离相图（如临界浓度、簇大小分布）。
- **创新状态**：unverified

### 候选 2：IDR 互作界面的 water bias 参数系统扫描
- **来源局限/观察**：water bias 的强度（如 -1 kJ/mol）选择缺乏系统依据，且对 IDP-膜互作结果可能高度敏感。
- **核心假设**：不同 IDR 序列（如不同电荷分布、疏水模式）对 water bias 强度的最优值存在系统差异，可通过序列特征预测。
- **初步方法**：对一组模型 IDR 序列（如 Sic1、α-synuclein C-端、FUS LC）进行 water bias 强度扫描（-0.5 至 -3 kJ/mol），测量膜结合亲和力、构象 ensemble 变化；训练序列特征→最优 bias 的回归模型。
- **验证方式**：与实验数据（如膜结合亲和力、NMR 化学位移）对比。
- **创新状态**：unverified

### 候选 3：Gō 网络「过度约束」的自动检测与松弛
- **来源局限/观察**：InhA 案例中默认 Gō 网络过度约束了 164-165 残基，抑制了生理波动。IDR 附近的 Gō 网络可能系统性存在此问题。
- **核心假设**：Gō 网络中与 IDR 相邻的残基对容易产生过度约束，可通过残基波动性预测自动识别并松弛。
- **初步方法**：对 Gō 网络中的每个键计算「约束强度/局部柔性」比值，识别异常高值；开发自动松弛算法，在保持整体结构的同时释放局部柔性；在 IDP-折叠蛋白融合体系上验证。
- **验证方式**：比较松弛前后模型的构象 ensemble 与实验 SAXS/FRET 数据。
- **创新状态**：unverified

### 候选 4：MAD:Database 的「IDP 互作模块」扩展
- **来源局限/观察**：MAD:Database 已包含 1,274 个模型，但缺乏针对 IDP-IDP 互作、IDP-膜互作、相分离相关分子的系统化收录和注释。
- **核心假设**：建立专门的「IDP 互作」数据库模块（含 IDP 序列、预测无序区、已知互作伙伴、相分离相关注释），可显著降低相分离模拟的建模门槛。
- **初步方法**：从 UniProt、DisProt、LLPSDB 等数据库整合 IDP 相关数据；为每个条目提供 Martini 3 / Martini3-IDP 预参数化模型；开发基于序列相似性的模型推荐功能。
- **验证方式**：用户测试 + 与现有文献中的模拟结果对比。
- **创新状态**：unverified

### 候选 5：基于 CG 模型的 IDP 互作「预筛」→ 全原子验证流程
- **来源局限/观察**：MAD 生成的 CG 模型适合快速筛选，但精度有限。IDP 互作研究常需全原子模拟的细节。
- **核心假设**：CG 模拟可以高效预筛 IDP 互作候选（如结合位点、互作模式），然后通过 CG→AA 反向映射（如 Backward）进行全原子验证，形成两级工作流。
- **初步方法**：在 MAD 中集成 CG→AA 反向映射工具；对一组已知 IDP 互作对（如 Sic1-Cdc4、α-synuclein-膜）测试「CG 预筛→AA 验证」流程的效率和准确性。
- **验证方式**：比较两级流程的互作界面预测与实验结构/突变数据。
- **创新状态**：unverified

### 候选 6：GōMartini 与 Martini3-IDP 的「无缝切换」策略
- **来源局限/观察**：当前 GōMartini 和 Martini3-IDP 是两种独立模式，但真实 IDP 常在「结合时折叠」和「游离时无序」之间转换。
- **核心假设**：开发一种「条件性 Gō」策略——当 IDP 区域与互作伙伴接近时激活 Gō 约束，远离时释放——可以更真实地模拟 coupled folding and binding。
- **初步方法**：在 Martini 3 中实现距离依赖的 Gō 键开关；在 Sic1-Cdc4 体系上测试「folding upon binding」的模拟能力。
- **验证方式**：比较结合自由能、折叠路径与实验/全原子模拟结果。
- **创新状态**：unverified