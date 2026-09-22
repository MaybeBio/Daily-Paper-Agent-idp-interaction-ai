## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) for the manuscript "GENESIS CGDYN: large-scale coarse-grained MD simulation with dynamic load balancing for heterogeneous biomolecular systems" by Jung, Tan, and Sugita.
- **Assessment boundary** The review is based solely on the provided manuscript text. Figures, tables, supplementary materials, and source data files are referenced but were not provided for direct inspection.
- **Shared manuscript claim summary** The authors present a new hierarchical domain decomposition scheme with dynamic load balancing, implemented as the CGDYN engine within the GENESIS software package, for residue-level coarse-grained molecular dynamics simulations of heterogeneous biomolecular systems. They claim superior computational performance compared to existing methods (ATDYN, SPDYN-like, Open3SPN2, GROMACS, LAMMPS) and demonstrate its application to the study of liquid-liquid phase separation, specifically the fusion of TDP-43-LCD droplets and the observation of Ostwald ripening in large multi-droplet systems.
- **Visible evidence base** The provided text includes the abstract, introduction, results sections describing the domain decomposition scheme, benchmark tests, and droplet fusion simulations, a discussion section, and a methods section detailing potential functions, system preparation, and simulation protocols. Performance data is presented in the text and referenced figures (Fig. 2, Supplementary Figs. 4-8). Simulation results are described in the text and referenced figures (Fig. 3, Fig. 4).
- **Missing materials affecting confidence** The manuscript text references several key figures (Figs. 1-4), supplementary figures (Supplementary Figs. 1-9), tables (Supplementary Table 1), and movies (Supplementary Movies 1-2) that are not included in the provided material. Direct inspection of these figures is essential to fully evaluate the performance claims, the validity of the simulation results, and the quality of the presented data. The methods section is also incomplete in the provided text, with some sections marked as "N/A".

## Reviewer
- **Overall assessment** This manuscript describes a valuable and timely software development effort, addressing a real bottleneck in coarse-grained simulations of heterogeneous biomolecular systems. The proposed cell-based kd-tree method with dynamic load balancing is a sensible and potentially impactful approach. The application to large-scale simulations of TDP-43-LCD droplet fusion and the observation of Ostwald ripening is compelling and demonstrates the utility of the new engine. However, the manuscript, as presented, has several significant weaknesses. The performance claims are based on a limited set of benchmarks, and the analysis of the scientific application, while interesting, is largely descriptive. The lack of access to the figures and supplementary materials makes it difficult to fully assess the technical soundness and the strength of the evidence. The manuscript would be significantly strengthened by a more detailed analysis of the load-balancing algorithm's behavior, a more comprehensive performance evaluation, and a deeper quantitative analysis of the droplet fusion and ripening phenomena.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the computational biophysics and molecular simulation communities, particularly those who use or develop coarse-grained models. The software is a practical tool for studying large-scale phenomena like phase separation, and the benchmark data will be useful for groups running similar simulations. The application to TDP-43-LCD droplets will also be of interest to the broader community studying neurodegeneration and biomolecular condensates.
- **Major strengths**
    - The manuscript addresses a significant and well-recognized problem: the load imbalance in parallel MD simulations of systems with non-uniform particle distributions.
    - The proposed solution, a cell-based kd-tree method, is a logical and potentially efficient approach for dynamic load balancing.
    - The implementation of the method in the widely used GENESIS software package increases its potential impact and accessibility.
    - The application to large-scale simulations of TDP-43-LCD droplet fusion, reaching sizes comparable to experimental observations, is a significant achievement and demonstrates the power of the new tool.
    - The observation of Ostwald ripening in the simulations is a scientifically interesting result that highlights the potential of the method to capture complex physical phenomena.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness and validation of performance claims
    - **Claim pointer** The manuscript claims that CGDYN "outperforms other MD programs in terms of computational performance" and shows "3-30 times better performances than ATDYN" and "at most 7.5 times" better than SPDYN-like algorithms.
    - **Evidence point** Results section "Benchmark tests of CGDYN for heterogeneous biological systems", Figure 2, Supplementary Figures 4-8.
    - **Concern** The performance claims are based on a limited set of benchmark systems and comparisons. The benchmarks are primarily focused on the authors' own previous implementation (ATDYN) and a "SPDYN-like" algorithm. While a comparison with GROMACS and LAMMPS is included, the details are limited. The claim of superiority is too broad without a more systematic comparison against other state-of-the-art MD engines that support CG simulations, such as GROMACS, LAMMPS, or OpenMM, across a wider range of system sizes, particle distributions, and hardware configurations. The text mentions that GROMACS is superior for a smaller system, which complicates the general claim of superiority. The performance data is presented in figures that were not available for review, making it impossible to verify the magnitude of the claimed speedups or the statistical significance of the results.
    - **Why it matters** The central contribution of this paper is a new software engine with claimed performance advantages. If these claims are not robustly validated, the core value proposition of the work is weakened. A more comprehensive and rigorous benchmark is essential to establish the technical soundness of the performance claims.
    - **Resolution test** The authors should provide a more extensive benchmark section, including: (1) a wider range of system sizes, including the very large systems they target; (2) a more diverse set of system compositions, including systems with more extreme density heterogeneities; (3) a direct comparison with other popular CG-capable MD codes (e.g., GROMACS, LAMMPS) under similar conditions; (4) an analysis of the overhead and benefits of the dynamic load-balancing algorithm itself, e.g., by comparing to a static decomposition with the same number of processes; and (5) a discussion of the scalability of the method, including strong and weak scaling results.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Scientific importance and validation of the scientific application
    - **Claim pointer** The manuscript claims that the simulations "directly observe Ostwald ripening" and that the changes in droplet shape correlate with the mixing of IDP chains during fusion.
    - **Evidence point** Results sections "Mechanisms of the fusion of two droplets" and "Toward the observation of ultra-large droplets...", Figures 3 and 4.
    - **Concern** The scientific application, while demonstrating the software's capability, is presented in a largely descriptive manner. The analysis of the fusion process relies on a small number of order parameters (D_IJ, m, η) and a visual inspection of snapshots. The claim of observing Ostwald ripening is based on the observation that small droplets shrink and large ones grow. However, a more rigorous analysis is needed to confirm this mechanism. For example, the authors could analyze the flux of material between droplets, the time-dependence of droplet size distributions, and compare the simulation results with theoretical models of Ostwald ripening (e.g., LSW theory). The correlation between shape change and mixing is also presented qualitatively. A more quantitative analysis, such as a cross-correlation function or a time-lagged analysis, would strengthen this claim.
    - **Why it matters** The application to droplet fusion is a key part of the paper, demonstrating the utility of the new tool for addressing biologically relevant questions. If the analysis is not sufficiently rigorous, the scientific conclusions drawn from the application are not fully supported, and the broader impact of the work is diminished.
    - **Resolution test** The authors should strengthen the analysis of the droplet dynamics. This could include: (1) a quantitative analysis of the growth/shrinkage rates of individual droplets to confirm the Ostwald ripening mechanism; (2) a comparison of the simulated droplet size distribution with theoretical predictions; (3) a more detailed analysis of the mixing process, such as calculating a mixing entropy or a spatial correlation function; and (4) a discussion of the time scales involved and how they relate to experimental observations.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness and reproducibility
    - **Claim pointer** The manuscript describes the implementation of the method in the CGDYN engine of GENESIS and states that it is "optimized for parallel computers with many processors."
    - **Evidence point** Results section "CGDYN structure", Methods section.
    - **Concern** The description of the implementation, particularly the load-balancing algorithm, is not sufficiently detailed to be fully reproducible. The manuscript mentions a "cell-based kd-tree method" but does not provide enough algorithmic detail on how the tree is constructed, how the load is balanced, how the communication patterns are updated, or how the method handles the different interaction types (e.g., bonded vs. non-bonded) during rebalancing. The methods section is also incomplete in the provided text, with a section marked as "N/A". This lack of detail makes it difficult for other researchers to implement or fully understand the proposed method.
    - **Why it matters** For a software/methods paper, the reproducibility of the method is paramount. Without a clear and detailed description of the algorithm, the contribution is less valuable to the community.
    - **Resolution test** The authors should provide a more detailed algorithmic description of the cell-based kd-tree method, including pseudocode or a clear step-by-step explanation. They should also ensure the methods section is complete and provides all necessary details for reproducing the simulations, including force field parameters, simulation setup, and analysis protocols.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability and clarity
    - **Affected element** Introduction and Discussion
    - **Evidence point** Introduction, Discussion
    - **Issue** The introduction and discussion sections are somewhat general and could be more focused. The discussion of other load-balancing methods is brief and could be expanded to better contextualize the novelty of the proposed approach.
    - **Required correction** The authors should more clearly articulate the specific advantages and disadvantages of their method compared to other dynamic load-balancing strategies (e.g., those based on space-filling curves, graph partitioning, or work-stealing). This would help to highlight the novelty of their contribution.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods section, Benchmark simulations
    - **Evidence point** Methods section "Validation and benchmark simulations"
    - **Issue** The description of the benchmark simulations is somewhat brief. For example, the text states that "we run the same runs five times and get the average as the benchmark results," but it does not report the variance or standard deviation of these runs. This makes it difficult to assess the statistical significance of the performance differences.
    - **Required correction** The authors should report the standard deviation or a confidence interval for their benchmark results. This would strengthen the claims about performance differences.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Results section "CGDYN structure"
    - **Evidence point** Results section "CGDYN structure"
    - **Issue** The description of the data structures and algorithms in the "CGDYN structure" section is quite technical and may be difficult for a non-specialist to follow. The use of terms like "cell-based kd-tree" and "SIMD" is not fully explained.
    - **Required correction** The authors should consider adding a high-level overview of the algorithm, perhaps with a schematic figure, to make the core ideas more accessible to a broader audience.

## Risk / unsupported claims
- The claim that CGDYN "outperforms other MD programs" is too broad and is not fully supported by the limited benchmarks presented. The comparison is primarily against the authors' own previous implementation and a "SPDYN-like" algorithm, with a limited comparison to GROMACS and LAMMPS.
- The claim of "directly observing Ostwald ripening" is based on qualitative observations of droplet sizes. A more rigorous quantitative analysis is needed to definitively confirm this mechanism.
- The claim that the "changes in droplet shape correlate with the mixing of IDP chains" is presented qualitatively. A quantitative correlation analysis is not provided.
- The performance and scalability claims for very large systems (e.g., "good scalability up to 4096 nodes on Fugaku") are based on data presented in figures that were not available for review, making them impossible to verify.
- The manuscript text is incomplete in the provided material, with a section in the Methods marked as "N/A", which prevents a full assessment of the methodology.