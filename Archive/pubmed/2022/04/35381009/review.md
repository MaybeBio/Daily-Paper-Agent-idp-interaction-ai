## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Technical implementation, performance benchmarking, and application demonstrations of residue-level CG models in GENESIS
- **Shared manuscript claim summary** The authors report implementation of several residue-level coarse-grained models (AICG2+, 3SPN.2C, HPS/KH, PWMcos) in the GENESIS molecular dynamics software, including a new tool (GENESIS-CG-tool) for input preparation, performance optimizations (multiple neighbor lists, MPI-parallelized random number generation), and demonstrations on systems including protein-DNA complexes, IDR/RNA phase separation, HSV capsid, and chromatin.
- **Visible evidence base** Full text including equations, figures referenced (Fig 1-8, S1, S2), tables (Table 1-2), and benchmark data descriptions
- **Missing materials affecting confidence** Actual benchmark data values, figure contents, supplementary information details, and code repository contents were not available for direct verification

## Reviewer
- **Overall assessment** The manuscript presents a useful and timely implementation of multiple residue-level CG models within a single, well-established MD software package. The choice of models covers important use cases (folded proteins, IDRs, DNA, RNA) and the integration with a user-friendly topology generation tool addresses a real practical need. The performance optimizations described, particularly the multiple neighbor lists and MPI parallelization of random number generation, are sensible and address known bottlenecks in CG simulations. The application demonstrations are appropriate in scope, though the depth of validation is limited. The main weaknesses are the lack of quantitative performance comparisons against existing implementations, limited validation of the implemented models against reference data, and insufficient detail on the correctness of the implementations. The manuscript is well-written and will be of interest to the computational biophysics community, but the technical claims require stronger evidence.

- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular dynamics method development, particularly those working on coarse-grained simulations of large biomolecular systems such as chromatin, phase-separated condensates, and viral capsids. The unified implementation in GENESIS and the accompanying tool will be valuable for practitioners who need access to multiple CG models in one framework. The performance optimizations may also interest developers of MD software.

- **Major strengths**
  1. Comprehensive implementation of multiple complementary CG models in a single, widely used MD package, addressing a genuine gap in the field.
  2. The GENESIS-CG-tool provides a practical solution to the often tedious and error-prone process of generating CG topology and coordinate files.
  3. The performance optimizations, particularly the multiple neighbor lists and MPI-parallelized random number generation, are well-motivated and address real computational bottlenecks.
  4. The application demonstrations cover a diverse range of biologically relevant systems, from protein-DNA complexes to viral capsids and chromatin, showing the versatility of the implementation.
  5. The manuscript is clearly written and the design choices are well-justified.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the implemented CG models are correctly implemented and can reproduce expected behaviors, as demonstrated in the four application examples.
- **Evidence pointer** Section "Application 1" through "Application 4", Figures 5-8
- **Concern** The application demonstrations are largely qualitative. For example, in Application 1 (protein target search on DNA), the authors state that sry is "preferentially bound to the consensus sequence" and that "we observed coupling between the sequence-specific recognition and DNA bending," but no quantitative analysis is provided. Similarly, in Application 2, the density of the condensate is reported, but there is no comparison to reference simulations or experimental data. In Application 3, the stability of the capsid is shown via Rg, RMSD, and Q, but no comparison to known capsid properties is made. In Application 4, the chromatin simulation is described but no quantitative validation is presented. Without quantitative validation against reference data or established results, the correctness of the implementations cannot be assessed.
- **Why it matters** The primary claim of the manuscript is that these models are correctly implemented and usable for production simulations. Qualitative demonstrations are insufficient to establish this. Users need confidence that the implementations reproduce known results before applying them to new systems.
- **Resolution test** Provide quantitative comparisons of simulation results against reference data, such as: (1) binding free energies or residence times for the sry-DNA system compared to previous all-atom or CG simulations; (2) condensate density and surface tension for the IDR/RNA system compared to published results using the same models in other software; (3) capsid radius and mechanical properties compared to experimental measurements or previous simulations; (4) nucleosome positioning and histone tail conformations compared to known structural data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the performance optimizations, including multiple neighbor lists and MPI-parallelized random number generation, improve the efficiency of CG MD simulations in GENESIS.
- **Evidence pointer** Section "Performance Optimization", Figure 4
- **Concern** The benchmark results are presented only as figures without numerical values. The strong scaling results show that performance scales up to 64 MPI processes, but the efficiency (relative to ideal scaling) is not quantified. More importantly, there is no comparison against existing implementations of the same models in other software packages (e.g., CafeMol, LAMMPS, OpenMM). The claim of improved performance is therefore not substantiated. Additionally, the memory benchmark shows linear scaling with system size, which is expected, but no comparison to other software is provided.
- **Why it matters** Performance is a key selling point of the manuscript. Without quantitative comparison to existing tools, users cannot determine whether the GENESIS implementation offers any advantage. The lack of efficiency numbers also makes it difficult to assess the quality of the parallelization.
- **Resolution test** Provide: (1) numerical values for the strong scaling efficiency at each process count; (2) a comparison of simulation speed (ns/day) for a standard benchmark system (e.g., a small protein or nucleosome) against at least one other software package implementing the same models; (3) a comparison of memory usage per particle against other packages.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The manuscript claims that GENESIS-CG-tool can generate CG topology and coordinate files from PDB or PDBx/mmCIF input files for various combinations of CG models.
- **Evidence pointer** Section "Preparation", Figure 2, S1 Fig
- **Concern** The description of GENESIS-CG-tool is high-level. While the authors state that the tool is available on GitHub and as part of GENESIS, the manuscript does not provide sufficient detail on the tool's architecture, the specific steps of the conversion process, or how users can customize parameters. The example command "aa_2_cg.jl PRO1.pdb" is given, but the full range of options and their meanings is not described. The manuscript also does not explain how the tool handles more complex cases, such as protein-nucleic acid complexes with multiple chains or post-translational modifications.
- **Why it matters** The tool is a key contribution of the manuscript. Without adequate documentation in the manuscript, users may struggle to use it effectively, and the reproducibility of the described workflows is compromised.
- **Resolution test** Provide a more detailed description of the tool's functionality, including: (1) a complete list of command-line options; (2) a step-by-step example of generating inputs for a multi-component system (e.g., protein-DNA complex); (3) a description of how the tool handles non-standard residues or modifications; (4) a link to the full documentation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that the combination of AICG2+ for folded proteins and HPS for IDRs is tested for the first time in this new framework, enabling studies of systems with both folded and disordered regions.
- **Evidence pointer** Section "Discussion", Application 4
- **Concern** While the combination of models is novel in the GENESIS framework, the manuscript does not demonstrate that this combination produces results that are distinct from or superior to using the models separately or in other frameworks. The chromatin application (Application 4) uses this combination but provides only a brief description of the simulation setup and no validation of the results. The claim of novelty is therefore not backed by a compelling demonstration of the value of this combination.
- **Why it matters** The ability to combine models for folded and disordered regions in one simulation is potentially important for studying systems like chromatin and phase-separated condensates. However, the manuscript does not show what new scientific insights this combination enables.
- **Resolution test** Provide a more detailed analysis of the chromatin simulation, including: (1) comparison of histone tail conformations with and without the HPS model; (2) analysis of nucleosome stability and positioning; (3) comparison of results with experimental data on chromatin structure.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract states that the framework "extends accessible spatial and temporal scales by multi-scale simulations," but the manuscript does not describe any multi-scale simulation methodology or demonstrate multi-scale capabilities.
- **Required correction** Either remove this claim or add a brief description of how the CG models can be used in multi-scale contexts, e.g., by coupling with all-atom simulations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table lists available CG models but does not provide information on the default parameters for each model or how users can modify them.
- **Required correction** Add a column or supplementary table with default parameter values and instructions for customization.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Section "Time Integration"
- **Evidence pointer** Section "Time Integration", Equations 26-28
- **Issue** The manuscript states that a 10 fs time step is used but does not discuss the stability of the integration scheme for the CG models, particularly for the flexible IDR models with potentially stiff bonded terms.
- **Required correction** Add a brief discussion of the choice of time step and any stability considerations, or reference previous studies that have used similar time steps with these models.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section "Application 2"
- **Evidence pointer** Section "Application 2", Figure 6
- **Issue** The simulation setup for the IDR/RNA phase separation is described only briefly. The number of chains, box size, and simulation length are given, but the initial configuration generation and equilibration protocol are not described.
- **Required correction** Provide a more detailed description of the simulation protocol, including initial configuration generation, equilibration, and production run parameters.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Availability and future directions"
- **Evidence pointer** Section "Availability and future directions"
- **Issue** The manuscript states that GENESIS v1.7.1 is available but does not specify the version of GENESIS in which the CG models are implemented. The abstract and introduction refer to GENESIS v1.7.0, while the availability section mentions v1.7.1.
- **Required correction** Clarify which version of GENESIS contains the CG model implementations and ensure consistency throughout the manuscript.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Design and implementation"
- **Evidence pointer** Section "Design and implementation", Equations 1-25
- **Issue** The equations are presented without much context or explanation of the physical meaning of each term. For readers not deeply familiar with CG models, this section may be difficult to follow.
- **Required correction** Add brief explanations of the physical significance of each energy term and how they relate to the underlying biology or chemistry.

## Risk / unsupported claims
- The claim that the GENESIS implementation enables "multi-scale simulations" is not supported by any demonstrated multi-scale methodology in the manuscript.
- The claim that the performance optimizations improve efficiency is not quantitatively supported by comparisons to other software.
- The claim that the combination of AICG2+ and HPS models is "tested for the first time" in this framework is not backed by a compelling demonstration of the value of this combination.
- The correctness of the implementations is not quantitatively validated against reference data for any of the four application examples.
- The manuscript states that the HSV capsid simulation is "one of the largest biological systems simulated with the residue-level CG models," but no comparison to other large-scale CG simulations is provided to support this claim.