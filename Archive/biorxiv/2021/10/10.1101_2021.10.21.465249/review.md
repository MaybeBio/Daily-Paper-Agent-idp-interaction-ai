## Review setup
- **Input scope** Full manuscript text (abstract, introduction, design and implementation, applications, discussion, availability)
- **Assessment boundary** Technical soundness, completeness of evidence, and support for claims as presented in the provided manuscript text; no external validation performed
- **Shared manuscript claim summary** The authors report implementation of several residue-level coarse-grained (CG) models (AICG2+, 3SPN.2C, HPS/KH, PWMcos, structure-based RNA) in the GENESIS molecular dynamics software, with a new toolbox (GENESIS-CG-tool) for input generation, performance optimizations (multiple neighbor lists, MPI parallelization of random number generation), and demonstration on systems including protein-DNA complexes, IDR/RNA phase separation, virus capsid, and chromatin.
- **Visible evidence base** Benchmark figures (Fig 4A-D), application results (Figs 5-8), tables (Table 1-2), supplementary methods and figures referenced but not provided in full
- **Missing materials affecting confidence** Full supplementary methods, parameter files, input/output file examples, benchmark raw data, simulation setup details (e.g., box sizes, salt concentrations for each application), and code documentation are not fully available in the provided text; this limits independent verification of reproducibility and quantitative claims.

## Reviewer
- **Overall assessment** This manuscript describes a useful and timely software implementation effort, addressing a real need for unified residue-level CG model support in a scalable MD package. The choice of models and the optimization strategies are sensible, and the application examples demonstrate broad applicability. However, the manuscript as provided has several gaps in technical detail and quantitative evidence that prevent full assessment of the claims. The benchmark data are presented at a high level, and the application sections lack sufficient methodological detail to verify correctness or reproducibility. The work is potentially valuable to the computational biophysics community, but the current evidence base is insufficient to fully establish the stated capabilities.
- **Who would be interested in the results, and why** Computational biophysicists and molecular modelers studying large biomolecular assemblies, chromatin structure, phase separation, and protein-nucleic acid interactions. Developers of MD software and CG model parameterizations would also be interested in the implementation strategies and performance optimizations. The unified framework and toolbox lower the barrier for using multiple CG models in one simulation, which is attractive for multi-component systems.
- **Major strengths** 1) Addresses a clear gap: unified implementation of multiple residue-level CG models in a single, scalable MD engine. 2) Provides a user-facing toolbox (GENESIS-CG-tool) that simplifies input generation, a practical contribution. 3) Demonstrates performance optimizations (neighbor lists, MPI parallelization) that are relevant for large systems. 4) Application examples span diverse and biologically important systems, showing versatility. 5) The manuscript is generally well-organized and readable.
- **Major Concerns** 
  - R1-M1: Insufficient quantitative benchmark detail
  - R1-M2: Application examples lack methodological depth
  - R1-M3: Reproducibility and validation gaps
  - R1-M4: Performance claims not fully supported
- **Minor Comments** 
  - R1-m1: Terminology inconsistency
  - R1-m2: Figure referencing incomplete
  - R1-m3: Discussion of limitations is brief
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4 (as detailed below)
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The individual CG models are not new, but the unified implementation in GENESIS with a toolbox and performance optimizations is a novel contribution to the software ecosystem.
  - Scientific importance: High for the computational biophysics community, as it enables larger and more complex CG simulations. The demonstrated applications (capsid, chromatin) are of broad interest.
  - Interdisciplinary readership: Moderate. Primarily of interest to computational biologists, biophysicists, and software developers; less accessible to experimental biologists without computational background.
  - Technical soundness: Not fully assessable from the provided material. The implementation strategies are plausible, but quantitative evidence and methodological details are insufficient to verify correctness and performance claims.
  - Readability for nonspecialists: The manuscript is generally clear, but some sections (e.g., detailed potential energy functions) assume familiarity with CG modeling. The abstract and summary are accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The work addresses a real need and the approach is sound in principle, but the current evidence base does not fully establish the stated capabilities. Additional benchmark details, methodological clarity, and validation data are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that GENESIS CG simulations are scalable up to 64 MPI processes and that memory usage scales with system size, with specific numbers (e.g., ~40 MB for one PolII, ~22 GB for 1000 PolIIs).
- **Evidence pointer** Fig 4A-D, Table 2, "Benchmark of MD simulations with residue-level CG models" section
- **Concern** The benchmark results are presented as figures without raw data or error bars. The scaling behavior is described qualitatively ("scalable") without quantitative metrics such as parallel efficiency or speedup values. The memory benchmark uses duplicated PolII systems, but the relationship between particle count and memory is not explicitly quantified. The choice of 5 OpenMP threads and the specific MPI configuration is not justified, and the impact of these choices on the reported performance is unclear.
- **Why it matters** Performance claims are central to the manuscript's value proposition. Without quantitative details, readers cannot assess whether the implementation meets the stated goal of enabling large-scale simulations on regular computers or supercomputers. The lack of error analysis and configuration details undermines confidence in the reproducibility of the benchmarks.
- **Resolution test** Provide raw benchmark data (e.g., timings, memory usage) in a supplementary table or repository. Report parallel efficiency and speedup for each system. Justify the choice of thread/process counts and include error bars or multiple runs. Clarify the relationship between particle count and memory usage with a fitted scaling law.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The application examples (sry-DNA, IDR/RNA phase separation, virus capsid, chromatin) are presented as demonstrations of the implemented models, with claims such as "sry is preferentially bound to the consensus sequence" and "the structure was stably maintained."
- **Evidence pointer** Figs 5-8, "Application 1-4" sections, Supplementary Methods (referenced but not provided)
- **Concern** The application sections lack critical methodological details. For example, in Application 1, the simulation length (10^7 steps) is stated, but the time step, temperature, salt concentration, and equilibration protocol are not specified. In Application 2, the system setup (e.g., initial configurations, box dimensions) is only partially described. For the virus capsid and chromatin, the simulation conditions and analysis methods are not fully detailed. The supplementary methods are referenced but not included in the provided text, making it impossible to verify the correctness of the simulations or the validity of the conclusions.
- **Why it matters** The applications are intended to demonstrate the utility and correctness of the implementation. Without sufficient methodological detail, readers cannot reproduce the simulations or assess whether the observed behaviors (e.g., binding, phase separation) are artifacts of the model or simulation setup. This is critical for establishing the credibility of the software.
- **Resolution test** Provide complete simulation protocols for each application, including initial structure generation, equilibration, production run parameters, and analysis methods. Include the supplementary methods in the manuscript or as a clearly accessible supplement. Where possible, provide input files and parameter sets in the repository.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation
- **Claim pointer** The manuscript implies that the implemented models are correctly implemented and produce physically reasonable results, as evidenced by the application examples.
- **Evidence pointer** Figs 5-8, "Design and implementation" section
- **Concern** There is no explicit validation of the implemented models against reference data or previously published results. For example, the sry-DNA simulation results are not compared with experimental data or prior simulations using the same models in other software. The phase separation behavior of FUS IDR is not quantitatively compared with published results. The virus capsid and chromatin simulations are presented as feasibility demonstrations, but no metrics (e.g., structural stability, contact maps) are compared with known properties.
- **Why it matters** Validation is essential to ensure that the implementation is correct and that the models behave as intended. Without comparison to reference data, users cannot trust that results obtained with GENESIS are equivalent to those from other software or consistent with experimental observations. This is a key requirement for a software paper.
- **Resolution test** Include a validation section that compares results from GENESIS with published data or results from other software for at least one model (e.g., AICG2+ folding of a small protein, 3SPN.2C DNA melting). Provide quantitative comparisons (e.g., RMSD, binding free energies, phase diagrams) and discuss any discrepancies.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Performance optimization
- **Claim pointer** The manuscript claims that "multiple neighbor lists, each of which is attached to a different nonbonded interaction potential in the cell-linked list method" and "parallelize the computations with message-passing-interface (MPI)" improve performance.
- **Evidence pointer** "Performance Optimization" section, Fig 4
- **Concern** The performance optimization section describes the strategies but does not provide a detailed analysis of their individual contributions. For example, the benefit of using multiple neighbor lists versus a single list is not quantified. The MPI parallelization of random number generation is mentioned as addressing a bottleneck, but the speedup from this specific optimization is not isolated. The benchmark results show overall performance but do not attribute improvements to specific optimizations.
- **Why it matters** Understanding the impact of each optimization is important for users who may want to adapt or extend the implementation. It also helps in assessing whether the optimizations are generally applicable or specific to certain system types.
- **Resolution test** Provide a performance analysis that isolates the effect of each optimization (e.g., with and without multiple neighbor lists, with and without MPI random number generation). Report the speedup or efficiency gain for each optimization on representative systems.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** "Design and implementation" section, Eq (1)-(15)
- **Issue** The manuscript uses terms like "Gō-like" and "structure-based" somewhat interchangeably, and the notation for potential energy terms (e.g., V_AICG2+, V_3SPN.2C) is introduced but not consistently defined in a single table or glossary.
- **Required correction** Add a table or glossary defining all model abbreviations and potential energy terms, and use consistent terminology throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure referencing
- **Evidence pointer** Figs 5-8, "Application 1-4" sections
- **Issue** Some figures are referenced in the text but not fully described in the captions (e.g., Fig 5E and 5F are mentioned but the axes and units are not specified in the text). This makes it difficult to interpret the results without accessing the figures.
- **Required correction** Ensure all figure captions are self-contained, including axis labels, units, and a brief description of what is shown.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** "Discussion" section
- **Issue** The discussion of limitations is brief and focuses mainly on future plans (e.g., domain decomposition). It does not address potential limitations of the CG models themselves (e.g., accuracy of the HPS model for specific systems) or the scope of the current implementation (e.g., lack of support for certain features).
- **Required correction** Expand the discussion to include a more balanced assessment of the limitations of the models and the implementation, and how they might affect users.

## Risk / unsupported claims
- The claim that GENESIS CG simulations are "scalable" up to 64 MPI processes is not quantitatively supported by the provided data.
- The claim that the implemented models are "correctly implemented" is not validated against reference data.
- The claim that the application examples demonstrate "the possibility of using our GENESIS CG implementation to carry out studies on the large-scale chromatin dynamics" is not fully supported due to lack of methodological detail and validation.
- The claim that "random number generations for Gaussian distributions in the Langevin thermostat are one of the bottlenecks" is not supported by profiling data.
- The claim that the toolbox is "user-friendly" is not substantiated with usability tests or examples beyond a single command-line invocation.