## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) for the article "Repulsive vs Attractive Crowding Distinctly Regulate TDP-43 Condensates through Region-specific Structural Dynamics" by Zhang, Guoqing; Feng, Cibo; Chu, Xiakun, published in JACS Au (2025), DOI: 10.1021/jacsau.5c00876.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims relative to presented evidence, and alignment with Nature-style criteria. Editorial and formatting issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations with the HPS-Urry model to show that repulsive (steric) crowders promote TDP-43 CTD phase separation via entropic excluded-volume effects, while attractive crowders suppress or reshape condensation via competitive enthalpic interactions. They report region-specific internal architecture (helix-rich core, IDR-rich shell) and a structure-dynamics decoupling where helix-helix contacts are strong but short-lived, while IDR-IDR contacts are weaker but more persistent.
- **Visible evidence base** Main text figures (Figures 1-4, referenced as A-I panels), supplementary figures (S1-S24), methods section with model parameters, and simulation protocols. Specific numerical values for crowder volume fractions, simulation box sizes, and replica exchange parameters are provided.
- **Missing materials affecting confidence** Supplementary figures and tables (S1-S24, Tables S1-S2) are referenced but not provided in the submitted material. This limits verification of parameter details, convergence analyses, and robustness checks. No experimental validation data are included. The manuscript states "location not provided" for several figure references where specific panels are cited without clear labeling in the text.

## Reviewer

### Overall assessment
This manuscript presents a systematic computational study of how crowding agents of different chemical character (repulsive vs attractive) modulate the phase behavior of the TDP-43 C-terminal domain. The work is timely and addresses an important gap: most crowding studies focus on excluded-volume effects alone, while real cellular environments contain molecules that interact attractively with phase-separating proteins. The authors provide a coherent mechanistic picture linking single-chain properties to condensate-scale behavior, and they identify a plausible structure-dynamics decoupling mechanism. However, the study is purely computational, and several claims about biological relevance and experimental predictability extend beyond what the simulations can directly support. The distinction between "repulsive" and "attractive" crowding is clean in the model but may not map straightforwardly onto specific cellular molecules, which often exhibit mixed interaction character. The manuscript would benefit from clearer articulation of which predictions are directly testable and which are speculative extensions.

### Who would be interested in the results, and why
Researchers studying biomolecular phase separation, particularly those focused on TDP-43 and other RNA-binding proteins implicated in neurodegeneration, will find this work relevant. The study also speaks to the broader community investigating macromolecular crowding effects on protein behavior, including biophysicists and computational biologists. The region-specific analysis and the proposed structure-dynamics decoupling concept may interest experimentalists seeking to design crowding conditions that tune condensate properties. The framework could also inform studies of other prion-like domains and low-complexity regions beyond TDP-43.

### Major Strengths
1. The systematic comparison of repulsive vs attractive crowding across multiple length scales (single chain, dimer, condensate) is well designed and provides a coherent mechanistic narrative.
2. The region-specific analysis (helix vs IDR1 vs IDR2) goes beyond bulk properties and reveals nontrivial internal organization that would be missed by global measures.
3. The identification of a structure-dynamics decoupling, where strong contacts can be short-lived and weak contacts persistent, is conceptually interesting and potentially generalizable.
4. The authors are appropriately cautious about the limitations of their CTD-only model and acknowledge the absence of NTD, RRMs, and RNA.
5. The discussion of testable predictions (orientation maps, relaxation times) provides a clear path for experimental validation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / model validation
- **Claim pointer** The authors claim that the HPS-Urry model with a rigid helix captures the essential physics of TDP-43 CTD phase separation under crowding, and that the observed trends are robust.
- **Evidence pointer** Methods section, Figures 1-4, Supplementary Figures S1-S24 (not provided)
- **Concern** The manuscript does not provide any validation of the coarse-grained model against experimental data for TDP-43 CTD. While the HPS-Urry model has been used for other IDPs, the specific parameters for TDP-43 CTD (e.g., the rigid helix treatment, the choice of σi and λij values) are not benchmarked. The authors reference previous studies for parameter values, but no comparison to experimental Rg, phase boundaries, or condensate properties is shown. Without such validation, it is unclear whether the predicted differences between repulsive and attractive crowding are quantitatively reliable or merely qualitative trends that could shift with parameter choices.
- **Why it matters** The central claims of the paper depend on the model faithfully representing TDP-43 CTD behavior. If the model overestimates or underestimates certain interactions, the proposed mechanism of structure-dynamics decoupling could be an artifact of the coarse-graining rather than a real physical property.
- **Resolution test** Provide a validation section comparing simulated single-chain Rg, dimerization propensity, and condensate density (at zero crowding) to available experimental data for TDP-43 CTD. If experimental data are limited, benchmark against atomistic simulations or other well-validated CG models. Additionally, perform a parameter sensitivity analysis (e.g., varying λij, helix rigidity) to demonstrate that the qualitative conclusions are robust.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency / claim support
- **Claim pointer** The authors claim that "repulsive crowders promote condensation via excluded-volume entropic stabilization, whereas attractive crowders modulate assembly through competitive enthalpic interactions" and that this leads to distinct condensate morphologies and internal architectures.
- **Evidence pointer** Figures 1-4, Supplementary Figures S1-S24 (not provided)
- **Concern** The manuscript presents simulation snapshots and density profiles, but the quantitative evidence for the proposed mechanisms is thin. For repulsive crowding, the claim of "entropic stabilization" is inferred from increased density and compaction, but no direct calculation of entropic contributions (e.g., free energy decomposition, potential of mean force) is shown. For attractive crowding, the claim of "competitive enthalpic interactions" is inferred from reduced contact numbers, but no direct analysis of the energy balance between protein-protein and protein-crowder interactions is provided. The correlation between Rg, Nc_inter, and ρh is presented as evidence, but correlation does not establish causation.
- **Why it matters** The mechanistic distinction between entropic and enthalpic crowding effects is the central conceptual contribution of the paper. Without direct thermodynamic or energetic analysis, the mechanism remains speculative and could be explained by alternative factors (e.g., kinetic trapping, finite-size effects).
- **Resolution test** Perform free energy calculations (e.g., umbrella sampling or thermodynamic integration) to decompose the free energy of condensation into entropic and enthalpic contributions under different crowding conditions. Alternatively, compute the potential of mean force between two TDP-43 CTD chains in the presence of repulsive vs attractive crowders and show that the barrier/well depths change in the predicted direction.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability / biological relevance
- **Claim pointer** The authors state that their findings "offer mechanistic links to physiological modulators such as RNA stoichiometry, ATP levels, chaperone engagement, and client size/permeability" and that the principles "have broad applicability to diverse phase-separating proteins."
- **Evidence pointer** Discussion section
- **Concern** The leap from generic CG crowders to specific physiological modulators is not well supported. RNA, ATP, and chaperones are not simple attractive or repulsive crowders; they have sequence-specific, multivalent, and often dynamic interactions with TDP-43. The authors acknowledge this in the discussion but still frame their results as providing "mechanistic links" to these modulators. The claim of broad applicability to other phase-separating proteins is also speculative, as the study only examines TDP-43 CTD.
- **Why it matters** Overstating the biological relevance could mislead readers into thinking the simulations directly model physiological conditions, when in fact they use idealized crowders. This could lead to inappropriate extrapolation of the results to disease mechanisms.
- **Resolution test** Either temper the claims in the discussion to clearly distinguish between "generic principles" and "direct physiological relevance," or add simulations with more realistic crowders (e.g., explicit RNA fragments, ATP-like molecules) to demonstrate that the qualitative trends hold. If the latter is not feasible, revise the language to avoid implying direct mechanistic links.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / simulation convergence
- **Claim pointer** The authors claim that their 5 μs NVT simulations for phase coexistence and 10 μs REMD simulations for single-chain/dimer systems are sufficient for convergence.
- **Evidence pointer** Methods section, "Simulation Protocols"
- **Concern** No convergence analysis is presented. For phase-separating systems, equilibration times can be very long, and 5 μs may not be sufficient to reach steady state, especially at high crowder concentrations where dynamics slow down. The REMD simulations use 32 replicas from 150-800 K, which is a wide range; the number of replicas may be insufficient to ensure adequate overlap between adjacent temperature distributions, potentially leading to poor sampling. The authors state that average exchange acceptance rates are >24%, but this is a global average and does not guarantee local overlap.
- **Why it matters** If the simulations are not converged, the reported density profiles, contact maps, and relaxation times could be biased by initial conditions or incomplete sampling, undermining the quantitative claims.
- **Resolution test** Provide convergence metrics: (a) time evolution of condensate density and contact maps showing plateau behavior; (b) replica exchange acceptance rates as a function of temperature; (c) comparison of results from independent simulations with different initial configurations; (d) block averaging or autocorrelation analysis to estimate statistical errors.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / reproducibility
- **Affected element** Methods, "Crowding Interactions"
- **Evidence pointer** Equations 6-8
- **Issue** The parameters for the crowding interactions are not fully specified. The reference diameter σref = 0.6 nm and the shift Δpc = 0.391 nm are given, but the energy scale ε for protein-crowder interactions is not explicitly stated for the attractive case. It is implied that ε = 0.2 kcal/mol (same as protein-protein), but this should be confirmed. Additionally, the cutoff distance for crowder-crowder and protein-crowder interactions is not specified.
- **Required correction** Specify the energy scale and cutoff for all interaction types. If the same ε is used for both protein-protein and protein-crowder interactions, state this explicitly. Provide the functional form of the attractive potential (e.g., LJ with a well depth) and the exact parameters used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure quality / interpretability
- **Affected element** Figures 1-4
- **Evidence pointer** Main text figures
- **Issue** The figure panels are referenced as "Figure A", "Figure B", etc., without specifying the figure number. This makes it difficult for the reader to locate the relevant data. Additionally, the color scales for density maps and contact maps are not described, and the units for density are not given.
- **Required correction** Use standard figure numbering (Figure 1A, 1B, etc.) and ensure each panel is clearly labeled. Add color bar legends with units for all heatmaps and density plots.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results, "TDP-43 CTD Phase Behaviors"
- **Evidence pointer** Figures 1D-E, 1F-G
- **Issue** The correlation between Rg and ρh is described as "strong" and "approximately linear," but no correlation coefficients or statistical significance tests are reported. Given that the data points appear to be few (likely one per crowder concentration), the strength of the correlation is unclear.
- **Required correction** Report Pearson or Spearman correlation coefficients with p-values, or state the number of independent data points and acknowledge the limited statistical power.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology / precision
- **Affected element** Discussion, "Structure-dynamics decoupling"
- **Issue** The term "structure-dynamics decoupling" is used to describe the observation that strong contacts are short-lived and weak contacts are persistent. This is a useful concept, but the term "decoupling" could be misinterpreted as implying that structure and dynamics are independent, which is not the case. A more precise term might be "strength-lifetime inversion" or "contact strength-persistence dissociation."
- **Required correction** Consider rephrasing or defining the term more carefully to avoid potential misinterpretation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness / reproducibility
- **Affected element** Methods, "Simulation Protocols"
- **Evidence pointer** Tables S1 and S2 (not provided)
- **Issue** The manuscript refers to Tables S1 and S2 for key model parameters and simulation details, but these tables are not included in the submitted material. Without them, the reader cannot fully reproduce the simulations.
- **Required correction** Ensure the supplementary tables are included in the final submission and that they contain all necessary parameters (e.g., Lennard-Jones parameters, bond constants, box sizes, number of chains, temperature ranges, etc.).

### Technical failings that need to be addressed before the case is established
1. **Lack of model validation (R1-M1)**: No benchmark against experimental data or atomistic simulations is provided. This is essential to establish that the HPS-Urry model with a rigid helix is appropriate for TDP-43 CTD.
2. **Insufficient mechanistic evidence (R1-M2)**: The entropic vs enthalpic distinction is inferred but not directly computed. Free energy decomposition or potential of mean force calculations are needed.
3. **No convergence analysis (R1-M4)**: The manuscript does not demonstrate that the simulations have reached steady state, which is critical for phase coexistence studies.
4. **Incomplete parameter specification (R1-m1, R1-m5)**: Key interaction parameters and supplementary tables are missing, preventing reproducibility.

### Assessment against Nature-style criteria
- **Originality**: The study addresses a relevant question (crowding character effects on phase separation) that has received limited systematic attention. The region-specific analysis and the proposed structure-dynamics decoupling are novel contributions. However, the overall concept of attractive vs repulsive crowding is not entirely new, and the originality lies mainly in the specific application to TDP-43 CTD.
- **Scientific importance**: The work has potential importance for understanding how cellular environments modulate phase separation, with implications for neurodegenerative disease. However, the purely computational nature and the idealized crowding model limit the direct biological impact. The importance would be significantly enhanced by experimental validation or by simulations with more realistic crowders.
- **Interdisciplinary readership**: The topic bridges biophysics, computational biology, and neuroscience. The writing is generally accessible, but the methods section assumes familiarity with CG simulations and phase separation concepts. The broader implications for disease are discussed, which could attract readers beyond the immediate simulation community.
- **Technical soundness**: The simulation methodology is standard and appears appropriate for the questions asked, but the lack of validation, convergence analysis, and mechanistic decomposition weakens the technical case. The rigid helix approximation is a potential concern that is not fully addressed.
- **Readability for nonspecialists**: The abstract and introduction are clear and accessible. The results and discussion are more technical but generally well-written. The figures, if properly labeled, would aid understanding. The discussion of physiological relevance is helpful but could be more carefully qualified.

### Recommendation posture
**Supportive if technical concerns are resolved.** The manuscript addresses an interesting and timely question with a systematic computational approach. The core findings, if validated, would be a useful contribution to the phase separation field. However, the current evidence is insufficient to fully establish the mechanistic claims. The authors must address the model validation, provide direct thermodynamic evidence for the entropic/enthalpic distinction, and demonstrate simulation convergence. If these issues are resolved, the paper could be suitable for publication in a high-impact journal, though the purely computational nature may make it more appropriate for a specialized biophysics or computational biology venue rather than a general audience journal.

## Risk / unsupported claims
1. **"Repulsive crowders promote condensation via excluded-volume entropic stabilization"**: The promotion of condensation is supported by density data, but the entropic mechanism is inferred, not directly computed. Unsupported as stated.
2. **"Attractive crowders modulate assembly through competitive enthalpic interactions"**: The suppression of condensation is supported, but the enthalpic competition mechanism is not directly demonstrated. Unsupported as stated.
3. **"This establishes a structure-dynamics decoupling with strong but short-lived helix-helix contacts versus weaker yet more persistent IDR-IDR contacts"**: The contact strength and lifetime data are presented, but the claim of "decoupling" as a general principle is an interpretation that goes beyond the specific system studied. Partially supported, but the generalization is speculative.
4. **"Our results define crowding class as a tunable control knob for region-specific redistribution and dynamics, offering testable readouts and offering mechanistic links to physiological modulators such as RNA stoichiometry, ATP levels, chaperone engagement, and client size/permeability"**: The link to specific physiological modulators is speculative, as the simulations use generic crowders. The claim of "testable readouts" is reasonable but requires experimental confirmation. Unsupported as stated.
5. **"The principles uncovered here have broad applicability to diverse phase-separating proteins"**: This generalization is not supported by the data, which only examine TDP-43 CTD. Unsupported as stated.