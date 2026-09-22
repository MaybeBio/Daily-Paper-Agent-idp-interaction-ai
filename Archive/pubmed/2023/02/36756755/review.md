## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to show that adsorption of the intrinsically disordered amyloid beta40 (Abeta40) monomer on gold surfaces depends on substrate charge density (sigma). They identify key residues (ARG5, LYS16, LYS28, LEU17-ALA21, ILE31-VAL38) whose adsorption prevents beta-sheet formation, with a critical charge density (sigma(c)) of -0.167 e nm(-2). Beyond sigma(c), counterion condensation on the gold slab competes with key residue adsorption, leading to beta-sheet formation and potential fibrillation. The authors conclude that an optimal surface charge density is required for effective inhibition.
- **Visible evidence base** Abstract text only; no simulation details, force field parameters, system setup, convergence criteria, error estimates, or quantitative binding free energy values are provided
- **Missing materials affecting confidence** Full manuscript, methods section, simulation protocols, force field validation, binding free energy calculation details, error bars, convergence analysis, control simulations, and any figures or tables

## Reviewer
- **Overall assessment** The abstract presents a plausible mechanistic hypothesis linking substrate charge density to Abeta40 adsorption and beta-sheet formation, with potential relevance to nanoparticle-based inhibition of amyloid fibrillation. However, the evidence base is insufficient to evaluate the robustness of the claims. Key quantitative results, such as binding free energies and the critical charge density, are stated without error estimates or methodological context. The causal link between counterion condensation and loss of key residue adsorption is asserted but not demonstrated with direct evidence. The study's significance is moderate, and the conclusions are not fully established from the provided material.
- **Who would be interested in the results, and why** Researchers in biophysics, computational chemistry, and nanomedicine, particularly those studying amyloid aggregation, protein-surface interactions, and the design of nanoparticle-based inhibitors for neurodegenerative diseases. The findings could inform experimental efforts to optimize surface charge properties for therapeutic applications.
- **Major strengths** The study addresses a relevant and timely question about the role of surface charge density in protein adsorption, with clear practical implications. The identification of specific key residues and a critical charge density provides a testable hypothesis. The proposed competition mechanism between counterions and charged residues is conceptually interesting and could guide future experimental and computational work.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate; the concept of charge density effects on protein adsorption is not entirely new, but the specific focus on Abeta40 and the proposed counterion competition mechanism adds some novelty. Scientific importance is moderate, as the findings could inform inhibitor design, but the abstract does not demonstrate broad implications beyond this specific system. Interdisciplinary readership is plausible, given the intersection of biophysics, materials science, and neurobiology. Technical soundness cannot be assessed from the abstract alone, as no methodological details or error analysis are provided. Readability for nonspecialists is adequate, with clear language, but the lack of quantitative context limits accessibility.
- **Recommendation posture** Currently not established from the provided evidence. The claims are plausible but require full methodological details, error analysis, and direct evidence for the proposed mechanism before the case can be considered robust.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that binding free energy identifies key residues (ARG5, LYS16, LYS28, LEU17-ALA21, ILE31-VAL38) responsible for preventing beta-sheet formation.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that binding free energy was used to identify key residues, but no quantitative values, error estimates, or statistical significance are provided. It is unclear how the binding free energy was calculated, whether per-residue decomposition was performed, and what criteria were used to define "key" residues.
- **Why it matters** Without quantitative data and error analysis, the identification of key residues cannot be validated. The claim is central to the mechanistic interpretation, and unsupported identification could lead to incorrect conclusions about the inhibition mechanism.
- **Resolution test** Provide per-residue binding free energy values with standard errors, define the threshold for "key" residues, and include convergence checks for the free energy calculations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that a critical charge density (sigma(c)) of -0.167 e nm(-2) exists, beyond which key residues do not adsorb and beta-sheet formation occurs.
- **Evidence pointer** Abstract, location not provided
- **Concern** The critical charge density is stated as a single value without error bars or a description of how it was determined. The abstract does not specify the range of sigma values tested, the number of simulations per condition, or the criteria for defining the transition in adsorption behavior.
- **Why it matters** The existence of a sharp critical threshold is a strong claim that requires robust sampling and statistical analysis. Without this, the threshold could be an artifact of limited simulation time or insufficient sampling.
- **Resolution test** Show a plot of key residue adsorption versus sigma with error bars, describe the simulation protocol for each sigma value, and provide statistical tests to support the existence of a critical threshold.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** The authors claim that beyond sigma(c), counterion condensation on the gold slab competes with key residue adsorption, leading to beta-sheet formation.
- **Evidence pointer** Abstract, location not provided
- **Concern** The proposed competition mechanism is asserted but not directly demonstrated. The abstract mentions saturation of Na(+) condensation on Abeta40 at sigma(c), but no data are shown to link this saturation to the loss of key residue adsorption or to beta-sheet formation. The causal chain is speculative.
- **Why it matters** The mechanism is the core explanatory framework of the study. Without direct evidence, such as radial distribution functions, contact analysis, or free energy profiles, the competition hypothesis remains unverified.
- **Resolution test** Provide quantitative analysis of ion distributions near the surface and protein, correlation between ion condensation and residue desorption, and evidence that beta-sheet formation is directly caused by the loss of key residue adsorption.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of sigma
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract uses sigma for charge density but does not define its units or how it is varied in the simulations. The value -0.167 e nm(-2) is given, but the range and spacing of sigma values are not stated.
- **Required correction** Define sigma explicitly, state the range of values tested, and clarify how the charge density is implemented on the gold surface.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation details
- **Evidence pointer** Abstract, location not provided
- **Issue** No information is provided on the force field, water model, simulation box size, temperature, pressure, or simulation length. These details are essential for reproducibility.
- **Required correction** Include a brief description of the simulation setup in the abstract or refer to the methods section with specific parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Generalization of conclusions
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract concludes that an optimal surface charge density is required for effective inhibition, but this is based on a single protein (Abeta40) and a single surface (gold). The generalizability to other amyloid proteins or surfaces is not discussed.
- **Required correction** Acknowledge the system-specific nature of the findings and discuss potential limitations in the abstract or suggest future work.

## Risk / unsupported claims
- The identification of key residues (ARG5, LYS16, LYS28, LEU17-ALA21, ILE31-VAL38) as responsible for preventing beta-sheet formation is unsupported without quantitative binding free energy data.
- The existence of a critical charge density (sigma(c)) of -0.167 e nm(-2) is unsupported without error estimates and statistical analysis.
- The competition mechanism between counterion condensation and key residue adsorption is speculative and not directly demonstrated.
- The claim that lack of key residue adsorption leads to beta-sheet formation and subsequent fibrillation is an extrapolation not supported by the abstract's evidence.
- The conclusion that an optimal surface charge density is required for effective inhibition is plausible but not fully established from the provided material.