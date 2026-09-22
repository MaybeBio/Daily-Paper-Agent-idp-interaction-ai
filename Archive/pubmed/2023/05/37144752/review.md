## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors selected seven intrinsically disordered and amyloidogenic antimicrobial peptides (AMPs) with reported activity against *Acinetobacter baumannii* and used computational methods (docking, binding energy, dissociation constant, molecular dynamics) to predict their molecular targets among seventeen candidate proteins. They report MurB as the most probable target for most AMPs, followed by Omp 33-36, MurE, and PorinSubF. Molecular dynamics analysis is claimed to identify MurB as the target of Bactenecin. The authors also report that the selected AMPs form oligomeric states and interact with targets in that state. The abstract concludes that experimental validation is needed.
- **Visible evidence base** Abstract text only; no methodological details, numerical results, figures, tables, or statistical measures provided
- **Missing materials affecting confidence** Full manuscript, methods section, docking scores, binding energy values, dissociation constants, molecular dynamics trajectories, simulation parameters, force fields, convergence criteria, oligomerization data, and any validation metrics

## Reviewer
- **Overall assessment** The abstract presents a computational screening study with potentially useful implications for antimicrobial peptide target identification. However, the evidence base available for review is limited to the abstract, which lacks quantitative results, methodological specifics, and validation metrics. The core claims regarding target identification and oligomerization are plausible but cannot be rigorously evaluated from the supplied material. The study is positioned as hypothesis-generating, and the authors appropriately acknowledge the need for experimental confirmation.
- **Who would be interested in the results, and why** Researchers in antimicrobial resistance, computational drug discovery, peptide therapeutics, and structural biology of bacterial membrane proteins would find these results relevant. The identification of potential targets for intrinsically disordered AMPs against a multidrug-resistant pathogen addresses a clinically important problem. Computational biologists working on protein-peptide interactions and molecular dynamics simulations may also be interested in the methodological approach.
- **Major strengths** The study addresses a clinically urgent problem, namely antibiotic resistance in *A. baumannii*. The focus on intrinsically disordered and amyloidogenic AMPs is a distinctive angle that may offer novel insights. The inclusion of multiple AMPs and multiple candidate targets provides a broad screening approach. The authors explicitly acknowledge the need for experimental validation, which reflects appropriate scientific caution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any quantitative docking scores, binding energy values, dissociation constants, or simulation convergence metrics. Without these, the ranking of targets and the claim that MurB is the most probable target cannot be assessed. The molecular dynamics analysis is described only qualitatively, with no information on simulation length, force field, system setup, or statistical validation. The oligomerization claim lacks any supporting data on oligomer size, stability, or stoichiometry.
- **Assessment against Nature-style criteria** 
  - Originality: The application of intrinsically disordered and amyloidogenic AMPs as a specific class for target prediction in *A. baumannii* has some novelty, though computational target prediction for AMPs is not new.
  - Scientific importance: The clinical relevance is high given the threat of multidrug-resistant *A. baumannii*, but the current evidence is hypothesis-generating rather than conclusive.
  - Interdisciplinary readership: The topic bridges microbiology, computational biology, and drug discovery, which could attract a broad audience if the results are robust.
  - Technical soundness: Cannot be evaluated from the abstract alone. The absence of methodological detail and quantitative results prevents assessment of technical rigor.
  - Readability for nonspecialists: The abstract is generally clear, though some specialized terms (e.g., MurB, Omp 33-36) are used without explanation. The writing is accessible to a scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a reasonable computational screening framework, but the absence of quantitative data and methodological detail means the core claims cannot be verified. A supportive posture would require access to the full manuscript with detailed results and validation metrics.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the most probable molecular targets of most of the intrinsically disordered amyloidogenic AMPs were MurB, followed by Omp 33-36, MurE, and PorinSubF" and that "molecular dynamics analysis concluded that the target of antimicrobial peptide Bactenecin is MurB."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no quantitative data to support the ranking of targets. No docking scores, binding energy values, dissociation constants, or statistical measures are reported. The basis for ranking MurB as the most probable target is not described. Similarly, the molecular dynamics conclusion for Bactenecin is stated without any supporting metrics such as binding free energy, stability analysis, or interaction persistence.
- **Why it matters** Without quantitative results, the reader cannot assess whether the target ranking is statistically meaningful or within the margin of error of the computational methods. The claim that MurB is the most probable target for most AMPs is a central finding, and its validity depends entirely on the underlying numerical data.
- **Resolution test** Provide docking scores, binding energy values, dissociation constants, and appropriate error estimates for all seventeen targets across all seven AMPs. For the molecular dynamics analysis, report binding free energies, root-mean-square deviation and fluctuation data, and interaction occupancy over the simulation trajectory.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state that "calculation of docking score, binding energy, dissociation constant, and molecular dynamics analysis was performed with selected seventeen possible molecular targets."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not specify which docking software, scoring functions, force fields, simulation packages, or analysis protocols were used. No information is given on simulation length, temperature, pressure coupling, solvent model, or convergence criteria. The selection criteria for the seventeen targets are also not described.
- **Why it matters** Computational results are highly dependent on methodological choices. Different docking algorithms and force fields can produce divergent rankings. Without this information, the reproducibility and reliability of the results cannot be evaluated, and the claims cannot be independently verified.
- **Resolution test** In the full manuscript, provide a detailed methods section including software versions, parameter settings, validation of docking protocols against known complexes, simulation length and ensemble, and convergence assessment.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that "the selected AMPs form oligomeric states, and interact with their molecular targets in that state."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no data on oligomerization. No information is given on the oligomerization states observed, the methods used to assess oligomerization (e.g., coarse-grained simulations, all-atom simulations, or experimental data), the stability of these oligomers, or the stoichiometry of the AMP-target interaction in the oligomeric form.
- **Why it matters** The claim that AMPs interact with targets as oligomers is a significant mechanistic assertion that differs from the typical monomeric binding model. If unsupported, this claim could mislead subsequent experimental design. The biological relevance of oligomeric binding also requires demonstration that such states are populated under physiologically relevant conditions.
- **Resolution test** Provide data on oligomer size distribution, oligomer stability over simulation time, and comparative binding analysis between monomeric and oligomeric forms. If experimental data exist, include them; otherwise, clearly state that this is a computational prediction requiring validation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Target selection rationale
- **Evidence pointer** Abstract only; location not provided
- **Issue** The abstract does not explain why these seventeen specific proteins were selected as candidate targets. The relevance of these targets to AMP mechanism of action is not stated.
- **Required correction** Briefly state the selection criteria for the seventeen targets, such as known essentiality, membrane localization, or prior association with AMP activity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "intrinsically disordered and amyloidogenic"
- **Evidence pointer** Abstract only; location not provided
- **Issue** The abstract does not clarify whether all seven AMPs are both intrinsically disordered and amyloidogenic, or whether these properties vary among the selected peptides. The relevance of these properties to target selection is not explained.
- **Required correction** Specify which AMPs possess which properties and briefly explain why these properties are relevant to the computational approach.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Experimental validation statement
- **Evidence pointer** Abstract only; location not provided
- **Issue** The final sentence states that experimental validation is needed, but no indication is given of what specific experiments would be appropriate or whether any preliminary experimental data exist.
- **Required correction** Suggest specific experimental approaches, such as binding assays, mutagenesis, or antimicrobial activity assays with target overexpression or knockout strains.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Ranking of targets
- **Evidence pointer** Abstract only; location not provided
- **Issue** The abstract states that MurB is the most probable target for "most" AMPs but does not specify which AMPs target which proteins. The reader cannot determine the pattern of target specificity across the seven peptides.
- **Required correction** Provide a brief summary of which AMPs were predicted to target which proteins, or include a table in the full manuscript.

## Risk / unsupported claims
- The ranking of MurB as the most probable target for most AMPs is unsupported in the abstract due to the absence of quantitative data.
- The claim that molecular dynamics analysis identified MurB as the target of Bactenecin is unsupported without simulation details and binding metrics.
- The claim that AMPs form oligomeric states and interact with targets in that state is unsupported without oligomerization data.
- The overall predictive validity of the computational approach cannot be assessed without any experimental correlation or benchmarking against known AMP-target interactions.
- The clinical relevance of the predicted targets is asserted but not demonstrated, as no data link target engagement to antimicrobial activity.