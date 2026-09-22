## 01 基本信息

- **标题**: Implementation of residue-level coarse-grained models in GENESIS for large-scale molecular dynamics simulations
- **作者与单位**: Tan C; Jung J; Kobayashi C; Ugarte La Torre D; Takada S; Sugita Y（RIKEN 等，具体单位未在摘要中提供）
- **期刊/预印本平台**: bioRxiv（预印本）
- **年份**: 2021
- **论文类型**: 方法学/软件实现论文
- **领域**: 计算生物物理；粗粒化分子动力学模拟；软件工程
- **关键词**: coarse-grained model; molecular dynamics; GENESIS; IDP; phase separation; chromatin; capsid
- **DOI/arXiv 号**: 10.1101/2021.10.21.465249
- **代码**: GENESIS v1.7.0（https://www.r-ccs.riken.jp/labs/cbrt/website）；GENESIS-CG-tool（https://github.com/noinil/genesis_cg_tool）
- **数据**: 模拟文件与数据见 https://github.com/RikenSugitaLab/cg-development-GENESIS-1.7.0
- **阅读日期**: 未提供
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**: 本文属于物理模拟方法学范畴，为 IDP/IDR 相分离模拟提供了统一的残基级 CG 模型实现框架（HPS/KH 模型），并支持蛋白-DNA/RNA 混合体系的互作模拟。虽不涉及 AI/深度学习，但其多模型组合、输入文件生成自动化、大规模并行化的思路，为 AI 辅助的 CG 模型参数化与验证提供了可迁移的软件基础设施。

## 02 一句话总结

本文在 GENESIS MD 软件中实现了多种残基级粗粒化模型（AICG2+、3SPN.2C、HPS/KH、PWMcos 等），通过统一的 GROMACS 风格输入文件格式和 GENESIS-CG-tool 工具箱，支持包含折叠蛋白、IDR、DNA、RNA 的异质大体系的高效并行 MD 模拟，并在 sry-DNA 结合、FUS IDR 相分离、HSV 衣壳和染色质等体系上验证了其正确性与可扩展性。

## 03 研究问题

- **具体问题**: 如何在一个统一的 MD 软件框架中实现多种残基级 CG 模型，并支持包含折叠蛋白、IDR、DNA、RNA 的异质生物大分子体系的高效大规模模拟？
- **为什么重要**: 基因组尺度染色质折叠、相分离凝聚体等细胞尺度现象涉及多种生物大分子的协同互作，需要能同时处理折叠/无序蛋白和核酸的 CG 模型，且需具备百万级粒子的模拟能力。
- **现有方法为何不足**: 现有 CG 模型分散在不同软件中，输入文件格式不统一；不同模型（如蛋白 Gō 模型与 DNA 3SPN.2C）组合使用时缺乏标准接口；大规模并行性能不足；IDR 模型与折叠蛋白模型的联合使用缺乏现成实现。
- **精确的 "Can ... ?" 研究问题**: Can a unified software framework (GENESIS) with residue-level CG models efficiently and correctly simulate heterogeneous biomolecular systems containing folded proteins, IDRs, DNA, and RNA at scales of millions of CG particles?

## 04 背景与发展脉络

**注：以下脉络基于本文引言与讨论，属于「仅本文框架」的叙述，未经外部文献核验。**

1. **全原子 MD 的局限**: 全原子 MD 精度高但计算成本大，无法模拟细胞尺度的生物现象（如染色质折叠、相分离）。
2. **CG 模型的兴起**: CG 模型在精度与效率间取得平衡，残基级 CG 模型（一个氨基酸一个粒子）成为研究大尺度生物现象的主流工具。
3. **模型多样化**: 物理基础的 Gō 模型（蛋白质折叠）、3SPN.2C（DNA 序列依赖性）、HPS/KH（IDR 相分离）等各自发展，但缺乏统一实现。
4. **软件生态碎片化**: 不同模型在不同软件中实现（如 CafeMol、LAMMPS、OpenMM），组合使用困难，输入文件格式不兼容。
5. **本文主张的位置**: 在 GENESIS 中实现统一的残基级 CG 模型框架，提供标准化的输入文件生成工具（GENESIS-CG-tool），支持多模型组合与大规模并行，填补了「统一框架 + 异质体系 + 大规模模拟」的空白。

## 05 核心痛点

| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
|------|------|----------------|----------|
| 输入文件生成困难 | 异质体系（蛋白+DNA+RNA）的 CG 拓扑文件需手工处理，易出错 | 各 CG 模型参数格式不统一，缺乏自动化工具 | Introduction: "The first issue is the input file generations of highly heterogeneous systems... making it difficult to generate input data for the systems containing different types of biomolecules." |
| 多模型组合缺乏标准接口 | 折叠蛋白模型与 IDR 模型、蛋白模型与核酸模型难以在同一模拟中联合使用 | 各模型由不同团队开发，未考虑互操作性 | Introduction: "If someone wants to use two of them simultaneously, it is not straightforward to combine two different CG models by treating their input or output data properly." |
| 大规模并行性能不足 | 百万级粒子体系的模拟在普通软件中效率低下 | 非键相互作用列表构建与力计算未针对 CG 模型优化 | Results 图 4: 展示了不同体系下的并行扩展性测试，说明需要专门优化 |
| 随机数生成成为瓶颈 | Langevin 恒温器中的高斯随机数生成耗时显著 | 全原子模拟中该部分占比小，但 CG 模拟中非键计算减少后占比上升 | Results: "We found that random number generations for Gaussian distributions in the Langevin thermostat are one of the bottlenecks in CG MD simulations." |
| 大结构文件格式限制 | 病毒衣壳等超大结构超出 PDB 格式容量 | PDB 格式行数限制 | Application 3: "The number of atoms and the length scale exceed the PDB format's upper limit for such a vast structure." |

## 06 核心思想

### 1) 表面方法
在 GENESIS 的 atdyn 引擎中实现多种残基级 CG 势函数（AICG2+、3SPN.2C、HPS/KH、PWMcos 等），提供 GENESIS-CG-tool（Julia 脚本）自动生成 GROMACS 风格输入文件，并针对 CG 模型特点优化非键相互作用计算与并行策略。

### 2) 核心洞察
- **统一框架的价值**: 不同 CG 模型共享基础相互作用形式（键、角、二面角、非键对），可以在一个框架内实现并自由组合，避免「每个模型一套软件」的碎片化。
- **输入文件标准化**: 采用 GROMACS 风格格式作为通用接口，降低用户学习成本，同时利用 .itp 文件的模块化特性支持异质体系组装。
- **性能瓶颈识别**: CG 模拟中非键计算占比下降后，随机数生成等次要环节成为瓶颈，需要针对性优化而非简单移植全原子代码。
- **多尺度衔接**: 残基级 CG 模型作为连接全原子模拟与连续介质模型的桥梁，其实现需考虑与实验数据（如 cryo-EM、Hi-C）的对接。

### 3) 可能的普适教训 [Analysis]
- 软件框架设计应优先考虑「模型组合的灵活性」而非单一模型的极致优化，因为生物体系本质上是异质的。
- 性能优化需要针对目标模拟类型（CG vs 全原子）重新分析瓶颈，而非假设相同。
- 提供自动化工具链（输入生成、格式转换）是方法学被社区采纳的关键，其重要性不亚于模拟引擎本身。

## 07 方法总览

- **输入**: PDB 或 PDBx/mmCIF 格式的结构文件；用户指定的模型类型（蛋白：AICG2+；DNA：3SPN.2C；IDR：HPS/KH；RNA：HPS 或结构基模型）；序列信息（用于 PWM 等序列依赖性模型）
- **输出**: GROMACS 风格拓扑文件（.top, .itp）和坐标文件（.gro）；MD 模拟轨迹（DCD 格式）
- **核心模块**:
  1. **GENESIS-CG-tool**: Julia 脚本集合，主入口 `aa_2_cg.jl`，将原子坐标转换为 CG 拓扑/坐标；支持 PDBx/mmCIF 大结构解析；利用 Julia 线程并行加速 Gō 接触检测
  2. **atdyn 引擎**: 实现各 CG 势函数的能量/力计算；支持 velocity-Verlet 积分器 + Langevin 恒温器
  3. **非键相互作用模块**: 多邻居列表策略，每个非键势函数（E_bp, E_LJ, E_ele 等）独立维护邻居列表，基于 cell-linked list 方法
  4. **并行模块**: MPI 并行（复制数据方案）+ OpenMP 线程并行；随机数生成并行化
- **训练/参数化**: 本文不涉及训练；各模型参数来自原始文献（AICG2+、3SPN.2C、HPS/KH 等），用户可修改参数文件
- **反馈回路**: 不适用（无学习过程）
- **文字流程**: 用户提供结构文件 → GENESIS-CG-tool 解析并生成 CG 拓扑/坐标 → 用户编写 MD 控制文件 → atdyn 读取输入并执行模拟 → 输出轨迹供分析

## 08 核心模块拆解

| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
|------|------|----------|----------|----------|------------------------|
| GENESIS-CG-tool (`aa_2_cg.jl`) | 从原子结构生成 CG 拓扑和坐标 | 手工生成异质体系 CG 输入文件易出错且耗时 | 输入: PDB/PDBx/mmCIF；输出: .top/.itp/.gro | Results 图 2, S1 Fig | 预期影响：用户需手工处理输入，易出错，阻碍方法采用 [预期效应] |
| 多邻居列表非键计算 | 为不同非键势函数（E_bp, E_LJ, E_ele 等）分别维护邻居列表 | 各势函数具有不同截断距离和粒子子集，统一列表导致无效计算 | 输入: 粒子坐标、各势函数截断值；输出: 各势函数的邻居对列表 | Methods "Neighbor lists" 节, 图 3 | 预期影响：计算量显著增加，模拟速度下降 [预期效应] |
| MPI 并行随机数生成 | 并行化高斯随机数生成 | CG 模拟中随机数生成成为瓶颈 | 输入: 随机种子、并行进程数；输出: 各进程独立随机数流 | Results: "We found that random number generations... are one of the bottlenecks" | 实测影响：未提供具体加速比数据；预期影响：单进程模拟 Langevin 动力学效率极低 [预期效应] |
| 势函数库（AICG2+, 3SPN.2C, HPS/KH, PWMcos） | 提供各 CG 模型的能量/力计算 | 不同生物分子需不同相互作用模型 | 输入: CG 坐标、拓扑；输出: 能量/力 | Methods "Residue-level CG models" 节, Table 1 | 实测影响：未提供消融实验；预期影响：缺少任一模型则无法模拟对应体系 [预期效应] |
| 截断方案（E_bp=18Å, E_ele=52Å, E_LJ=39Å） | 控制非键计算范围 | 平衡精度与效率 | 输入: 截断值参数；输出: 邻居列表范围 | Methods "Cutoff scheme" 节, Table 2 | 预期影响：截断过小导致能量不连续或精度损失；过大则效率下降 [预期效应] |

## 09 关键公式符号

**1. 谐振键势（式 1）**
\[
V_{\text{bond}} = \sum_i k_{b,i}(b_i - b_{i,0})^2
\]
- \( b_i \): 相邻 CG 粒子间键长
- \( b_{i,0} \): 参考键长（来自天然结构）
- \( k_{b,i} \): 力常数

**2. 高阶键势（式 2，用于 3SPN.2C DNA）**
\[
V_{\text{bond}} = \sum_i \left[ k_{b,i}^{(2)}(b_i - b_{i,0})^2 + k_{b,i}^{(4)}(b_i - b_{i,0})^4 \right]
\]
- \( k_{b,i}^{(2)}, k_{b,i}^{(4)} \): 二次和四次项力常数

**3. 谐振角势（式 3）**
\[
V_{\text{angle}} = \sum_i k_{a,i}(\theta_i - \theta_{i,0})^2
\]
- \( \theta_i \): 三个相邻 CG 粒子形成的键角
- \( \theta_{i,0} \): 参考键角
- \( k_{a,i} \): 力常数

**4. 知识基角势（式 4，AICG2+）**
\[
V_{\text{angle}} = -k_B T \ln P_a(\theta_i)
\]
- \( k_B \): Boltzmann 常数
- \( T \): 温度
- \( P_a(\theta_i) \): 氨基酸类型依赖的角分布（来自 PDB 统计）

**5. 周期二面角势（式 5）**
\[
V_{\text{dihedral}} = \sum_i \sum_n k_{\phi,i,n}[1 + \cos(n\phi_i - \phi_{i,0})]
\]
- \( \phi_i \): 二面角
- \( n \): 周期性
- \( k_{\phi,i,n} \): 力常数

**6. 高斯型二面角势（式 6，AICG2+ 和 3SPN.2C）**
\[
V_{\text{dihedral}} = \sum_i \epsilon_{\phi,i} \exp\left[-\frac{(\phi_i - \phi_{i,0})^2}{2\sigma_{\phi,i}^2}\right]
\]
- \( \epsilon_{\phi,i} \): 势阱深度
- \( \sigma_{\phi,i} \): 高斯宽度

**7. Gō 型天然接触势（式 7）**
\[
V_{\text{Go}} = \sum_{i<j} \epsilon_{\text{Go},i} \left[ \left(\frac{\sigma_i}{r_{ij}}\right)^{12} - 2\left(\frac{\sigma_i}{r_{ij}}\right)^6 \right]
\]
- \( r_{ij} \): 接触对粒子间距离
- \( \sigma_i \): 天然接触距离
- \( \epsilon_{\text{Go},i} \): 力常数

**8. Lennard-Jones 势（式 9）**
\[
V_{\text{LJ}} = \sum_{i<j} \epsilon_{\text{LJ},i} \left[ \left(\frac{\sigma_i}{r_{ij}}\right)^{12} - 2\left(\frac{\sigma_i}{r_{ij}}\right)^6 \right]
\]

**9. 纯排斥势（式 10）**
\[
V_{\text{exv}} = \sum_{i<j} \epsilon_{\text{exv},i} \left[ \left(\frac{\sigma_i}{r_{ij}}\right)^{12} - 2\left(\frac{\sigma_i}{r_{ij}}\right)^6 + 1 \right], \quad r_{ij} < r_{C,\text{exv}}
\]

**10. 高斯势（式 12）**
\[
V_{\text{Gaussian}} = \sum_{i<j} -\epsilon_{G,i} \exp\left[-\frac{(r_{ij} - r_{0,i})^2}{2w_i^2}\right]
\]

**11. Morse 势（式 13a, 13b，3SPN.2C）**
\[
V_{\text{Morse}} = \sum_{i<j} \epsilon_{M,i} \left[ \left(1 - e^{-\alpha_i(r_{ij} - r_{0,i})}\right)^2 - 1 \right]
\]

**12. Debye-Hückel 静电势（式 14）**
\[
V_{\text{ele}} = \sum_{i<j} \frac{q_i q_j}{4\pi\varepsilon_0\varepsilon_r} \frac{e^{-r_{ij}/\lambda_D}}{r_{ij}}
\]
- \( \lambda_D \): Debye 屏蔽长度
- \( \varepsilon_r = e(T) \cdot a(C) \): 相对介电常数（温度与盐浓度依赖）

**13. 角度调制函数（式 15，3SPN.2C）**
\[
f(\Delta\theta) = 1 - \cos(\Delta\theta)
\]
- \( \Delta\theta \): 角度与参考值之差

**14. 速度-Verlet 积分（式 26）**
\[
r_i(t+\Delta t) = r_i(t) + v_i(t)\Delta t + \frac{1}{2}\frac{F_i(t)}{m_i}\Delta t^2
\]
\[
v_i(t+\Delta t) = v_i(t) + \frac{1}{2}\frac{F_i(t) + F_i(t+\Delta t)}{m_i}\Delta t
\]

**15. Langevin 动力学（式 27）**
\[
F_i = -\nabla_i V_{\text{total}} - \gamma m_i v_i + \xi_i(t)
\]
- \( \gamma \): 摩擦系数
- \( \xi_i(t) \): 高斯随机力，满足 \( \langle \xi_i(t)\xi_i(t')^T \rangle = 2\gamma k_B T m_i \delta_{t,t'} I \)

## 10 实验设计与证据链

**数据集/群体**:
- 系统 1: 120 拷贝蛋白 Dps（铁蛋白样蛋白），共 222,360 CG 粒子，AICG2+ 模型
- 系统 2: 5000 条 IDP 链（各 100 残基），共 500,000 CG 粒子，HPS 模型
- 系统 3: 512 拷贝核小体，共 1,044,480 粒子，AICG2+（组蛋白）+ 3SPN.2C（DNA）+ E_HB（蛋白-DNA 互作）
- 系统 4: HSV-2 B-衣壳，1,687,980 CG 粒子，AICG2+ 模型
- 系统 5: 不同拷贝数 Pol II（1 至 1000），用于内存测试

**指标**: 内存消耗、并行加速比（强扩展性）、模拟稳定性（RMSD、Rg、Q 值）

**基线/对比**: 无显式基线；对比不同系统规模下的扩展性

**预算/硬件**: Intel Xeon Gold-6148 (2.4GHz)，20 核/CPU，双 CPU/节点，InfiniBand EDR 网络；内存测试在 93 GiB RAM 机器上

**评测协议**: 强扩展性测试（固定问题规模，增加 MPI 进程数）；内存随系统规模增长测试

| 实验 | 检验的 claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
|------|-------------|------------|------|------------|-------------------|------|
| 内存测试（1-1000 Pol II） | 内存消耗随系统规模线性增长 | 不同拷贝数 Pol II | 40 MB（1 拷贝）至 22 GB（1000 拷贝） | 内存管理可支持百万级粒子体系 | 未测试更大规模；未与其他软件对比 | Results 图 4A |
| 强扩展性测试（Dps 蛋白） | MPI 并行可扩展至 64 进程 | 222,360 粒子，1-64 MPI 进程 | 至 64 进程仍保持加速 | 并行策略有效 | 非完美线性加速；未测试 >64 进程 | Results 图 4B |
| 强扩展性测试（IDP 体系） | 同上 | 500,000 粒子，HPS 模型 | 至 64 进程仍保持加速 | IDP 体系可高效并行 | 同上 | Results 图 4C |
| 强扩展性测试（核小体） | 同上 | 1,044,480 粒子，混合模型 | 至 64 进程仍保持加速 | 异质体系可高效并行 | 同上 | Results 图 4D |
| sry-DNA 模拟 | CG 模型可正确描述蛋白-DNA 互作 | 10^7 步模拟，PWMcos 序列特异性互作 | sry 优先结合共识序列，伴随 DNA 弯曲 | 模型组合有效 | 未与实验定量对比；单一样例 | Results 图 5 |
| FUS IDR 相分离模拟 | HPS 模型可模拟 IDR 凝聚 | 120 链，10^7 步，slab 采样 | 形成致密凝聚体，密度约 5 粒子/nm³ | HPS 模型实现正确 | 未与实验相图定量对比 | Results 图 6A-B |
| LAF1+RNA 共凝聚 | HPS RNA 模型可模拟蛋白-RNA 共凝聚 | 300/750 LAF1 + 100/250 A15 RNA | RNA 进入 LAF1 凝聚体 | 蛋白-RNA 互作可模拟 | 未定量分析分配系数 | Results 图 6C-E |
| HSV 衣壳模拟 | 可模拟百万粒子级病毒衣壳 | 1,687,980 粒子，2×10^6 步 | 结构稳定（RMSD、Rg 稳定） | 大规模体系可模拟 | 仅平衡模拟，未涉及组装/解聚 | Results 图 7 |
| 染色质模拟 | 可模拟含 IDR 组蛋白尾巴的染色质 | 1024 核小体，5×10^5 步 | 组蛋白尾巴构象变化可追踪 | 折叠/无序混合体系可模拟 | 未与 Hi-C 数据对比 | Results 图 8 |

## 11 结论正确解读

- **任务范围**: 本文是软件实现与验证论文，不提出新物理模型，而是将已有 CG 模型（AICG2+、3SPN.2C、HPS/KH、PWMcos）统一实现于 GENESIS 平台。
- **oracle/真值输入**: 各模型参数来自原始文献；结构输入来自实验（X-ray、NMR、cryo-EM）。
- **端到端状态**: 从结构文件到模拟轨迹的完整流程已打通，但分析工具（如相分离序参数计算）未在本文中系统验证。
- **算力成本**: 未提供具体 wall-time 数据；仅提供并行扩展性数据（64 MPI 进程内有效）。
- **历史数据依赖**: 不适用（无训练过程）。
- **模型依赖**: 结果正确性依赖于各 CG 模型原始参数；组合使用时（如 AICG2+ + 3SPN.2C）的交叉参数（如蛋白-DNA 非键作用）采用默认组合规则，未经系统优化。
- **最难情形**: 异质体系（蛋白+DNA+RNA）的输入文件生成与力场参数匹配；百万粒子级体系的并行效率。
- **群体/领域边界**: 适用于残基级 CG 模拟；不适用于全原子或亚残基级 CG 模拟；IDP 模型仅限单链或均质体系验证，多组分相分离的定量准确性未充分验证。
- **不确定性**: 模拟时间尺度（10^7 步）对相分离平衡是否充分未讨论；有限尺寸效应未分析。

**有边界的复述**: 本文证明 GENESIS 能够以统一的 GROMACS 风格输入格式运行多种残基级 CG 模型，并在 64 MPI 进程内实现有效并行，可稳定模拟从 22 万到 168 万粒子的体系；但未证明这些模型在定量预测相分离相图或染色质高级结构方面的准确性。

## 12 作者自认局限

| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
|------|----------|-------------------|------|
| 并行扩展性不足 | 强扩展性测试显示非完美线性加速 | 计划实现 domain-decomposition 策略和高效负载均衡器 | Discussion: "The domain-decomposition strategy and the efficient load balancer suitable to residue-level CG models are required to solve this problem" |
| 粒子数上限 | atdyn 的 atomic decomposition 方案限制了可模拟体系规模 | 在新 MD 引擎中实现 domain decomposition | Discussion: "There is an upper limit of particle number with the atomic decomposition scheme in atdyn" |
| 参数未优化 | 组合不同模型时使用默认参数，IDR 与其他组分的互作参数可能需重新校准 | 用户需根据实验数据优化参数；GENESIS 提供修改参数的便利接口 | Discussion: "For more practical applications... one may need to more carefully optimize interaction terms between the IDR and the other components and their parameters" |
| 计算效率仍不足 | 模拟细胞尺度体系（数十亿粒子）仍需更高效率 | 结合增强采样方法 | Discussion: "It is necessary to employ enhanced sampling methods" |

## 13 批判性分析

| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
|----------------|-------------------|----------|----------|------|
| 验证案例均为「展示性」而非「定量验证」 | FUS 相分离仅展示凝聚形成，未与实验临界浓度、液滴尺寸等定量对比 | 无法判断模型预测精度 | 与实验相图数据（如 FUS 临界浓度 vs 盐浓度）定量对比 | Results 图 6 |
| 并行扩展性测试仅至 64 进程 | 未展示更大规模（如 256/512 进程）行为；实际用户可能需要更多核 | 无法判断大规模并行实用性 | 补充 128/256/512 进程测试 | Results 图 4 |
| 未与现有 CG 软件（如 CafeMol、LAMMPS）性能对比 | 无法判断 GENESIS 实现的相对优势 | 用户选择软件需要客观对比 | 相同体系、相同硬件下对比 wall-time | Discussion 中仅提及 CafeMol 等，未做定量对比 |
| 内存测试仅用 Pol II 均质体系 | 异质体系（蛋白+DNA+RNA）的内存行为可能不同 | 内存优化需针对实际使用场景 | 用核小体或衣壳体系做内存测试 | Results 图 4A |
| 未讨论 CG 模型的时间尺度映射 | 10^7 步对应物理时间未说明；不同模型时间映射可能不同 | 影响对模拟结果物理意义的解读 | 明确各模型的时间映射关系 | Methods 未提供 |
| 未提供 IDR 单链构象验证 | FUS 单链的 Rg、端到端距离等是否与实验/全原子模拟一致未展示 | 单链性质是相分离模拟的基础 | 与 SAXS 或全原子模拟对比单链构象 | Results 图 6 仅展示多链体系 |

## 14 学到什么

**Agent 提炼的知识候选**

1. **多模型统一框架设计**: 将不同 CG 模型（Gō、3SPN.2C、HPS/KH）作为「基础相互作用模块」的组合，而非独立实现，可大幅降低异质体系模拟的工程成本。→ 可迁移至本课题：构建 IDP/IDR 互作预测的 AI 模型时，可将不同物理先验（疏水、静电、π-π）作为可组合的特征模块。

2. **输入文件标准化策略**: 采用社区通用的 GROMACS 格式作为 CG 模型接口，降低用户迁移成本。→ 可迁移至本课题：AI 预测的 IDR 互作参数可输出为标准 CG 力场参数文件，直接用于 MD 验证。

3. **性能瓶颈重新分析**: CG 模拟中随机数生成成为瓶颈，说明优化需针对目标模拟类型重新 profiling。→ 可迁移至本课题：AI 辅助的 CG 模拟中，特征计算/推理可能成为新瓶颈，需针对性优化。

4. **IDR 与折叠蛋白的联合建模**: 本文首次在统一框架中组合 AICG2+（折叠）与 HPS（IDR），并应用于核小体组蛋白尾巴。→ 可迁移至本课题：IDR 介导的互作常涉及折叠结构域 + 无序区的协同，此组合建模思路可直接借鉴。

5. **实验结构到 CG 模型的自动化转换**: GENESIS-CG-tool 支持 PDBx/mmCIF 大结构解析，解决超大复合物的输入问题。→ 可迁移至本课题：AI 预测的 IDR 复合物结构（如 AlphaFold 输出）可自动化转换为 CG 模型进行动态验证。

6. **相分离模拟的 slab 采样方法**: 使用非对称盒子（18nm×18nm×200nm）模拟凝聚相与稀相平衡，是研究相分离的有效策略。→ 可迁移至本课题：AI 预测的 IDR 序列相分离倾向可通过此类模拟定量验证。

7. **多尺度模拟的衔接思路**: 作者展望将 CG 模型与全原子模型、实验数据（cryo-EM、Hi-C）结合，构建「Google Earth 式」的多分辨率模拟。→ 可迁移至本课题：AI 预测 + CG 验证 + 全原子精化的多尺度流程是 IDR 互作研究的可行范式。

## 15 与已有知识连接

- **Gō 模型（式 7）**: 源自 Go (1983) 的蛋白质折叠模型，本文使用的 AICG2+ 是其序列依赖性扩展（Li et al., 2014, J. Chem. Phys.）。本课题中 IDR 的 Gō 模型需谨慎使用，因 IDR 无稳定天然结构。
- **3SPN.2C DNA 模型（式 2, 13a, 13b, 15）**: 源自 Frezza et al. (2009) 的 3SPN 系列，本文使用其 2C 版本（Freeman et al., 2014）。本课题中 DNA 结合蛋白的 IDR 互作可借鉴此模型的序列依赖性。
- **HPS/KH 模型（式 16）**: HPS 源自 Ashbaugh & Hatch (2008) 的改进 Lennard-Jones 势，KH 源自 Kim & Hummer (2008)。两者均用于 IDP 相分离模拟，与 Dignon et al. (2018) 的 CALVADOS 系列同源。本课题核心方法之一。
- **PWMcos 模型（式 17）**: 源自 Tan & Takada (2020) 的序列特异性蛋白-DNA 互作模型，将位置权重矩阵（PWM）整合到 CG 力场。本课题中转录因子 IDR 的 DNA 靶向识别可借鉴。
- **GENESIS 软件**: 源自 Jung et al. (2015) 的 MD 软件包，本文扩展了 CG 功能。与 OpenMM（Eastman et al., 2017）、CafeMol（Kenzaki et al., 2011）形成竞争/互补关系。
- **相分离模拟**: 本文的 slab 采样方法与 Dignon et al. (2018) 的相图计算方法一致，后者已用于 IDR 相分离的 AI 预测验证。
- **与 AI 方法的衔接**: 本文不涉及 AI，但其 CG 模拟输出可作为 AI 模型的训练数据或验证基准。例如，HPS/KH 模拟的 IDR 构象系综可用于训练机器学习势函数。

## 16 研究想法

**Agent 生成的研究候选**

1. **候选名称**: IDR 互作 CG 力场的 AI 参数化
   - **来源局限/观察**: 本文 HPS/KH 模型参数为通用氨基酸疏水尺度，未针对特定 IDR 互作对优化；AI 方法可学习序列-互作强度映射。
   - **核心假设**: 基于深度学习的序列嵌入可预测 IDR-IDR 互作对的特异性 CG 参数（如 ε_LJ, λ），优于通用疏水尺度。
   - **初步方法**: 使用 IDR 相分离实验数据（临界浓度、液滴性质）训练序列→参数映射网络；将预测参数输入 GENESIS CG 模拟验证。
   - **验证方式**: 对训练集外的 IDR 序列，比较 AI 参数化 CG 模拟与实验相图/SAXS 数据。
   - **可能的失败模式**: 训练数据不足导致过拟合；序列-参数映射非唯一。
   - **创新状态**: unverified

2. **候选名称**: AlphaFold 预测的 IDR 复合物结构的 CG 动态验证
   - **来源局限/观察**: AlphaFold 对 IDR 复合物预测置信度低，本文 CG 框架可提供动态验证手段。
   - **核心假设**: AlphaFold 预测的 IDR 互作界面在 CG 模拟中不稳定，提示预测可能错误；稳定界面则可能正确。
   - **初步方法**: 将 AlphaFold 输出的 IDR 复合物结构转换为 CG 模型（使用 GENESIS-CG-tool），进行多副本 MD 模拟，分析界面残基接触稳定性。
   - **验证方式**: 对已知实验结构的 IDR 复合物（如 Nup 体系）测试，比较 CG 模拟稳定性与实验结合亲和力。
   - **可能的失败模式**: CG 模型分辨率不足以区分正确/错误界面；AlphaFold 预测的 IDR 构象本身偏离真实系综。
   - **创新状态**: unverified

3. **候选名称**: 多价 IDR-RNA 互作的 CG 模拟与凝聚体预测
   - **来源局限/观察**: 本文实现了 HPS 蛋白模型和 HPS RNA 模型，但未系统研究 IDR-RNA 多价互作对相分离的协同效应。
   - **核心假设**: IDR 中精氨酸-甘氨酸富集基序（RGG）与 RNA 的静电/π-π 互作是驱动 RNA-蛋白共凝聚的关键，CG 模拟可定量预测。
   - **初步方法**: 使用 GENESIS 中 HPS 蛋白 + HPS RNA 模型，对 RGG 重复序列与 poly-A RNA 的混合体系进行 slab 模拟，扫描序列长度、RNA 浓度、盐浓度。
   - **验证方式**: 与已有实验相图（如 LAF1 体系）对比；预测新序列的相分离倾向。
   - **可能的失败模式**: HPS RNA 模型过于简化，无法捕捉 RNA 碱基特异性互作；多组分体系有限尺寸效应严重。
   - **创新状态**: partially checked（已有 LAF1 案例，但未系统扫描）

4. **候选名称**: 基于 CG 模拟的 IDR 互作数据集生成与 AI 训练
   - **来源局限/观察**: 本文展示了大规模 CG 模拟能力，但未利用其生成训练数据；IDR 互作的 AI 模型缺乏高质量构象数据。
   - **核心假设**: 大规模 CG 模拟生成的 IDR 互作构象系综可作为 AI 模型（如 GNN 或扩散模型）的训练数据，学习 IDR 互作的能量景观。
   - **初步方法**: 对一组 IDR 序列进行 GENESIS CG 模拟，提取接触图、距离分布、氢键模式等特征；训练模型预测未见序列的互作模式。
   - **验证方式**: 与全原子模拟或实验（NMR 化学位移扰动）对比预测的接触图。
   - **可能的失败模式**: CG 模拟的粗粒化误差被 AI 模型放大；数据多样性不足。
   - **创新状态**: unverified

5. **候选名称**: 相分离凝聚体的多尺度模拟框架（CG ↔ 全原子回映）
   - **来源局限/观察**: 本文 CG 模拟可达到细胞尺度，但无法提供原子级互作细节；全原子模拟无法达到相分离尺度。
   - **核心假设**: 从 CG 凝聚体中提取代表性构象，回映至全原子并进行短时 MD，可揭示 CG 模型无法捕捉的原子级互作（如氢键网络）。
   - **初步方法**: 使用 GENESIS CG 模拟生成凝聚体构象，选取液滴内部/界面代表性构象，使用回映工具（如 CG2AT）转换为全原子模型，进行 100ns 级 MD。
   - **验证方式**: 比较回映后全原子模拟的互作能与 CG 模型预测的一致性；与实验突变数据对比。
   - **可能的失败模式**: 回映引入的构象偏差；全原子模拟时间尺度不足以平衡凝聚体。
   - **创新状态**: unverified