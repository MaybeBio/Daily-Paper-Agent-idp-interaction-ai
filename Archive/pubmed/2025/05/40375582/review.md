## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations to show that phosphorylation of the SARS-CoV-2 nucleocapsid protein (N-protein) homodimer increases its conformational flexibility, particularly in the N-terminal domain and linker regions, and diminishes its binding affinity to RNA. They further report that RNA secondary structure, specifically of the SL4ext element from the 5' UTR, is critical for preferential binding to the N-terminal domain.
- **Visible evidence base** Results sections with figures referenced (Figures 1-5, S1-S13), tables (Tables 1-3, S1-S4), methods description, and discussion
- **Missing materials affecting confidence** Raw trajectory data not directly inspected; force field parameter files not provided; HADDOCK docking scores and validation metrics not shown; MM/GBSA convergence checks not described; specific simulation input files not available; supplementary figures and tables not accessible in the provided material

## Reviewer

- **Overall assessment** This manuscript presents a substantial computational study addressing an important question in SARS-CoV-2 biology: how phosphorylation of the nucleocapsid protein modulates its structural dynamics and RNA binding. The work is timely and relevant, given the ongoing interest in N-protein function and its potential as a drug target. The authors employ state-of-the-art atomistic molecular dynamics simulations with appropriate force fields and provide a comprehensive analysis of conformational changes, salt bridge dynamics, and binding free energies. The study is technically competent, and the conclusions are largely supported by the presented evidence. However, several concerns regarding sampling adequacy, statistical rigor, and the interpretation of binding free energy calculations need to be addressed before the case is fully established.

- **Who would be interested in the results, and why** Structural biologists studying viral nucleocapsid proteins and their RNA interactions; computational biochemists interested in phosphorylation-induced conformational changes in intrinsically disordered proteins; virologists investigating SARS-CoV-2 replication and assembly mechanisms; researchers developing antiviral strategies targeting N-protein-RNA interactions; and the broader community studying liquid-liquid phase separation in viral systems.

- **Major strengths** The study addresses a biologically important question with clear translational relevance. The use of full-length N-protein homodimer rather than truncated constructs is a significant strength. The systematic comparison of phosphorylated and non-phosphorylated states across multiple RNA types is well designed. The identification of specific salt bridges (Arg107-Glu174, Arg89-Asp128) whose loss correlates with increased dynamics provides mechanistic insight. The integration of multiple analysis methods (RMSF, RMSD, contact maps, hydrogen bonding, MM/GBSA) strengthens the conclusions. The authors appropriately acknowledge limitations and suggest future directions.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and sampling adequacy
- **Claim pointer** The authors claim that phosphorylation increases N-protein conformational flexibility and decreases RNA binding affinity based on three 1 μs replicate simulations per system.
- **Evidence pointer** Results sections "Phosphorylation of the N-Protein Increases Its Conformational Flexibility" and "N-Protein:RNA Binding Is Diminished by Phosphorylation"; Table 1
- **Concern** The study relies on only three replicate simulations of 1 μs each for the apo N-protein systems and single 1 μs simulations for each N-protein:RNA complex. For a protein with large intrinsically disordered regions, this sampling may be insufficient to capture the full conformational ensemble. The authors do not provide convergence analysis, block averaging, or error estimates for the reported RMSF, RMSD, or binding free energy values. The claim of increased flexibility in the phosphorylated state is based on average values without statistical significance testing.
- **Why it matters** Without demonstrated convergence and statistical robustness, the observed differences between phosphorylated and non-phosphorylated states could arise from insufficient sampling rather than genuine biophysical differences. This is particularly critical for the binding free energy calculations, where MM/GBSA is known to be sensitive to conformational sampling.
- **Resolution test** Provide convergence plots (e.g., RMSD vs. time for cumulative averages), block error analysis for key observables, and statistical tests (e.g., bootstrap or Student's t-test) comparing phosphorylated and non-phosphorylated ensembles. For RNA binding, additional replicates or extended simulations should be performed to establish that the reported ΔΔG values are robust.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation of starting structures and docking poses
- **Claim pointer** The authors state that the N-protein homodimer structure was obtained from AlphaFold Multimer and validated by alignment with crystal structures, and that RNA molecules were docked to experimentally identified binding sites.
- **Evidence pointer** Methods section "System Preparation"; Figure S1; Table S1
- **Concern** The validation of the AlphaFold Multimer structure is limited to RMSD alignment of folded domains. The relative orientation of the two protomers and the arrangement of the disordered regions are not validated against experimental data. For the RNA docking, the authors used HADDOCK with prior knowledge of binding sites, but no docking scores, cluster analysis, or validation of the docked poses is provided. The choice of docking site (Arg92 and Arg107) is justified by literature, but the resulting complexes are not compared with any experimental structures or cross-linking data.
- **Why it matters** The initial conformation of the homodimer and the docked RNA poses are the starting points for all simulations. If these are not representative of the biologically relevant state, the subsequent dynamics and binding free energy calculations may be misleading. The authors acknowledge uncertainty in the initial conformation but do not provide sufficient evidence that their chosen starting structures are appropriate.
- **Resolution test** Provide a more detailed validation of the AlphaFold Multimer structure, including comparison of inter-domain distances and orientations with available experimental data (e.g., SAXS, cross-linking). For the RNA docking, show HADDOCK scores, cluster sizes, and a comparison of the docked poses with any available experimental structures or mutagenesis data. Consider performing simulations starting from alternative docking poses to test the robustness of the results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of binding free energy calculations
- **Claim pointer** The authors report that phosphorylation destabilizes N-protein:RNA interactions based on positive ΔΔG values across all RNA systems (Table 2).
- **Evidence pointer** Results section "N-Protein:RNA Binding Is Diminished by Phosphorylation"; Table 2
- **Concern** The MM/GBSA calculations are performed on single 1 μs trajectories for each RNA system. The authors correctly note that entropy is omitted and that relative values are most reliable. However, the magnitude of the reported ΔΔG values and their statistical uncertainty are not provided. The decomposition into per-residue contributions is used to identify specific interactions, but the cutoff of |ΔΔG| > 2.5 kcal/mol is arbitrary and not justified. The authors also do not discuss potential artifacts of the MM/GBSA method for highly charged systems such as RNA-protein complexes.
- **Why it matters** The central claim that phosphorylation diminishes RNA binding rests on these calculations. If the ΔΔG values are within the error of the method, the conclusion may not be robust. The per-residue decomposition is used to support mechanistic interpretations, so its reliability is important.
- **Resolution test** Provide error estimates for the MM/GBSA calculations (e.g., standard deviation across trajectory blocks or multiple runs). Justify the cutoff for per-residue contributions. Consider using an alternative method (e.g., MM/PBSA or potential of mean force calculations) to cross-validate the binding free energy results. Discuss the limitations of MM/GBSA for RNA-protein systems.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of RNA binding results
- **Claim pointer** The authors conclude that phosphorylation diminishes N-protein:RNA interactions and that the effect depends on RNA type, with SL4ext showing preferential binding to the NTD in its folded state.
- **Evidence pointer** Results sections "N-Protein:RNA Binding Is Diminished by Phosphorylation" and "NTD:RNA Interactions Depend on RNA Sequence and Structure"; Figures 3-5
- **Concern** The study tests only four RNA types (polyU, polyA, SL2SL3, SL4ext) with specific sequences and lengths. The authors generalize their findings to suggest that phosphorylation serves as a regulatory mechanism for N-protein function, but the limited RNA repertoire and the use of short RNA fragments may not capture the full complexity of N-protein-RNA interactions in vivo. The claim that SL4ext preferentially binds the NTD is based on simulations with a single docking pose and may not be representative.
- **Why it matters** The biological relevance of the findings depends on whether the tested RNA constructs are representative of the viral RNA elements that N-protein encounters during infection. Overgeneralization from a limited set of simulations could lead to incorrect conclusions about the regulatory role of phosphorylation.
- **Resolution test** Discuss the limitations of the RNA constructs used and how they relate to the full-length viral genome. If possible, perform additional simulations with longer RNA fragments or different sequences to test the generality of the findings. Alternatively, temper the conclusions to more clearly reflect the scope of the study.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figures 1-5
- **Evidence pointer** Results sections referencing Figures 1-5
- **Issue** The figures are referenced but not visible in the provided material. Based on the text descriptions, some figures appear to contain multiple panels with complex information (e.g., contact maps, RMSF plots, free energy decompositions). The authors should ensure that all panels are clearly labeled and that the figure captions are self-explanatory.
- **Required correction** Ensure that all figure panels are labeled (A, B, C, etc.) and that captions describe the content of each panel. Consider using color schemes that are accessible to color-blind readers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reporting of simulation parameters
- **Affected element** Methods section "Molecular Dynamics"
- **Evidence pointer** Methods section "Molecular Dynamics"
- **Issue** The methods section describes the simulation protocol but does not provide all parameters needed for reproducibility. For example, the specific temperature coupling algorithm, pressure coupling algorithm, and the frequency of output writing are not fully specified. The version of GROMACS is given, but the specific patch or build is not.
- **Required correction** Provide a complete list of simulation parameters, including thermostat and barostat settings, coupling constants, and output frequencies. Consider including a table summarizing the simulation setup for each system.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of force field limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors use the Amber ff19SB force field with the phosaa19SB extension for phosphorylated residues. While this is a reasonable choice, the limitations of the force field for describing phosphorylated intrinsically disordered regions are not discussed. The authors also do not mention the potential sensitivity of their results to the choice of force field.
- **Required correction** Add a brief discussion of the limitations of the chosen force field for this system and acknowledge that results may be force field dependent. Consider mentioning that future studies with alternative force fields could provide additional validation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility of data
- **Affected element** Data Availability Statement
- **Evidence pointer** Data Availability Statement
- **Issue** The authors state that raw trajectories are available on request and that aligned and skipped trajectories are available via a DOI. However, the analysis scripts and input files (e.g., topology files, docking poses) are not mentioned. This limits the reproducibility of the study.
- **Required correction** Consider making all input files, analysis scripts, and processed data available through a public repository (e.g., Zenodo, GitHub) to facilitate reproducibility and further analysis by the community.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency of terminology
- **Affected element** Throughout the manuscript
- **Evidence pointer** Abstract, Introduction, Results, Discussion
- **Issue** The authors use both "N-protein" and "nucleocapsid protein" throughout the text. While this is not incorrect, consistency would improve readability. Additionally, the term "phosphorylated N-protein" is used to describe a specific state, but the exact phosphorylation pattern (which sites, how many) is only described in the methods.
- **Required correction** Use consistent terminology throughout the manuscript. Consider defining the phosphorylation state clearly in the introduction and referring to it consistently in the results and discussion.

## Risk / unsupported claims
- The claim that phosphorylation "serves as a regulatory mechanism that determines N-protein function" is a reasonable hypothesis supported by the simulation data, but the study does not directly test this in a biological context. The authors appropriately frame this as a hypothesis in the discussion, but the abstract states it more strongly.
- The claim that "secondary structure is essential for the preferential binding of particular RNA elements from the 5' UTR to the N-terminal domain" is supported by the comparison of folded versus stretched SL4ext, but this is based on a single docking pose and limited sampling.
- The specific salt bridge loss (Arg107-Glu174) as the primary explanation for increased NTD dynamics is plausible but not directly proven. The authors note this is a hypothesis, which is appropriate.
- The generalizability of the findings to in vivo N-protein behavior is not directly testable from the presented simulations and should be considered speculative.
- The quantitative values of ΔΔG for RNA binding (Table 2) are presented without error estimates, making their reliability uncertain.