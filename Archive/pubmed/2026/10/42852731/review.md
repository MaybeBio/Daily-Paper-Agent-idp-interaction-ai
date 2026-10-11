## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no figures, tables, methods, or supplementary material were provided
- **Shared manuscript claim summary** The authors combine the HyRes coarse-grained model with umbrella sampling to compute potentials of mean force for stages of IDP fibrillation (free-chain association, fibril-surface recruitment, multilayer growth) across three proteins (alpha-synuclein, TDP-43, FUS-FC). They report that sequence-encoded electrostatics dominate association free energies, that charge neutralization and patterning are critical, and that surface organization rather than fibril thickness governs recruitment.
- **Visible evidence base** Abstract text only; no numerical data, simulation details, convergence metrics, or validation against experiment are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, force-field validation, error estimates, and any comparison with experimental or prior computational results

## Reviewer
- **Overall assessment** The abstract presents a plausible and potentially valuable computational framework for dissecting the thermodynamics of IDP fibrillation. The choice of three representative proteins and the focus on sequence-encoded electrostatics are sensible. However, the abstract alone does not provide sufficient quantitative detail to assess the robustness of the methods, the magnitude of the reported free energies, or the statistical significance of the protein-specific differences. The central claims are qualitatively stated and cannot be verified from the supplied material.
- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular simulation of protein aggregation, experimentalists studying amyloid formation in neurodegenerative diseases (Parkinson, ALS, FTD), and developers of coarse-grained force fields for disordered proteins. The proposed thermodynamic framework could inform mechanistic hypotheses about sequence determinants of fibrillation propensity.
- **Major strengths** The study addresses a genuinely under-explored question, namely how sequence and conformational ordering reshape multi-chain free-energy landscapes across distinct fibrillation stages. The use of three different IDPs with contrasting charge properties provides a useful comparative design. The explicit treatment of fibril-surface recruitment and multilayer growth goes beyond typical two-state association studies.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "we demonstrate that sequence-encoded electrostatic interactions are a major determinant of association free energies"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract reports qualitative differences in association free energies among the three proteins but provides no numerical values, no error estimates, and no convergence criteria for the umbrella sampling calculations. Without these, the claim that electrostatics are a "major determinant" cannot be quantitatively assessed.
  - **Why it matters** The central conclusion rests on comparative free-energy differences. If the statistical uncertainty is comparable to the reported differences, the protein-specific ranking may not be robust.
  - **Resolution test** Provide free-energy values with standard errors for each protein and each stage, along with convergence diagnostics (e.g., overlap of umbrella windows, block-error analysis) in the full manuscript.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "Charge-neutralization simulations further reveal the critical role of electrostatics and charge patterning in controlling association"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract does not specify which residues were neutralized, how charge patterning was perturbed, or whether the simulations were re-equilibrated after mutation. The term "critical role" is not supported by any quantitative measure of effect size.
  - **Why it matters** Charge-neutralization experiments are only interpretable if the perturbation is well-defined and if the response is shown to be specific rather than a generic destabilization of the protein.
  - **Resolution test** Specify the neutralization protocol, report the resulting changes in free energy with uncertainties, and include control simulations with non-electrostatic perturbations.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "recruitment governed by the accessibility and arrangement of surface interaction sites rather than fibril thickness alone"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** The abstract does not describe how fibril thickness was varied, how surface site accessibility was quantified, or how the two factors were deconvolved. Without a systematic parameter sweep, the claim of causality is not established.
  - **Why it matters** This is a mechanistic claim that distinguishes the study from simpler geometric models. If the design does not independently vary thickness and site arrangement, the conclusion may be confounded.
  - **Resolution test** Describe the fibril models used, the range of thicknesses tested, and the metric for site accessibility. Show that the free-energy change tracks accessibility independently of thickness.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility
  - **Claim pointer** "we combine the hybrid-resolution coarse-grained HyRes model with umbrella sampling"
  - **Evidence pointer** Abstract; location not provided
  - **Concern** No simulation details are given, including the HyRes version, the number of umbrella windows, the reaction coordinate definition, the total simulation time, or the temperature and salt conditions. Reproducibility cannot be assessed.
  - **Why it matters** Coarse-grained simulations are highly sensitive to model parameters and sampling protocols. The absence of these details prevents independent verification.
  - **Resolution test** Provide a full methods section with all parameters, software versions, and sampling protocols.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Terminology
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The phrase "thermodynamic landscapes" is used without defining the dimensionality or the specific order parameters that define the landscape.
  - **Required correction** Define the reaction coordinates and the free-energy surface explicitly in the abstract or introduction.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Protein selection rationale
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states that the three proteins are "representative" but does not explain the selection criteria beyond their amyloid-forming propensity.
  - **Required correction** State the specific sequence features (e.g., net charge, charge distribution, hydrophobicity) that motivated the choice of these three proteins.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Validation
  - **Affected element** Comparison with experiment
  - **Evidence pointer** Abstract; location not provided
  - **Issue** No experimental comparison is mentioned, which weakens the claim that the model captures physiologically relevant thermodynamics.
  - **Required correction** Include at least one quantitative comparison with experimental association rates or free energies, or explicitly state the limitations of the model in this regard.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. These three concerns directly undermine the quantitative validity of the central claims. R1-M4 is important for reproducibility but is not strictly blocking if the full manuscript provides the details.
- **Assessment against Nature-style criteria**  
  Originality: The question of how sequence and conformational ordering reshape multi-chain free-energy landscapes across fibrillation stages is timely and not fully addressed in prior work. The comparative three-protein design adds value.  
  Scientific importance: If the claims hold quantitatively, the framework could inform mechanistic understanding of amyloid formation and guide sequence-based predictions. However, the importance is currently prospective rather than demonstrated.  
  Interdisciplinary readership: The topic bridges biophysics, computational chemistry, and neurobiology. The abstract is written in a way that is accessible to a broad physical-science audience, though the lack of quantitative detail limits its utility for experimentalists.  
  Technical soundness: Cannot be assessed from the abstract. The absence of convergence metrics, error bars, and validation is a major gap.  
  Readability for nonspecialists: The abstract is clear and well-structured, with jargon kept to a reasonable level. The key concepts are introduced adequately.
- **Recommendation posture** Currently not established from the provided evidence. The scientific question is worthwhile and the approach is plausible, but the abstract alone does not provide the quantitative support needed to validate the central claims. A supportive recommendation would require the full manuscript to address the blocking concerns.

## Risk / unsupported claims
- The claim that "sequence-encoded electrostatic interactions are a major determinant of association free energies" is unsupported without numerical free-energy values and error estimates.
- The claim that "charge-neutralization simulations further reveal the critical role of electrostatics and charge patterning" is unsupported without specifying the perturbation protocol and effect sizes.
- The claim that "recruitment governed by the accessibility and arrangement of surface interaction sites rather than fibril thickness alone" is unsupported without a systematic deconvolution of the two factors.
- The statement that "alpha-synuclein exhibits the strongest attraction and salt sensitivity" is unverifiable without quantitative free-energy comparisons.
- The statement that "association of the isolated FUS fibrillar core remains thermodynamically unfavorable" is unverifiable without the corresponding free-energy value.
- The overall claim of providing "a thermodynamic framework connecting sequence, conformation, and surface organization" is aspirational and cannot be evaluated from the abstract.