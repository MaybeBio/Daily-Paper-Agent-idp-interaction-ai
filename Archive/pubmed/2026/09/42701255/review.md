## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors propose that biomolecular condensates alter the folding landscape of protein alpha-helices through a balance of multivalent interactions (promoting unfolding) and crowding (promoting folding), that helix-coil transitions are kinetically frustrated inside condensates due to coupling to contact rearrangement timescales, and that folding landscapes are dually sequence-dependent on both the helix and co-condensate proteins. They further claim implications for condensate-mediated proteinopathies and condensate design.
- **Visible evidence base** Atomistic simulations of the helix-coil transition in condensates versus dilute solution and inert crowders; Bayesian optimization-derived residue-resolution model applied to helices from TDP-43, Annexin A11, and Androgen Receptor in condensates of varying physicochemical properties
- **Missing materials affecting confidence** Full methods, simulation details, force field parameters, model validation metrics, quantitative results, figures, tables, and any statistical analyses. The abstract provides no numerical data or direct evidence for the stated claims.

## Reviewer
- **Overall assessment** The abstract presents an intriguing and potentially impactful hypothesis that condensates modulate alpha-helix folding through competing interaction and crowding effects. However, the evidence base is entirely descriptive at this stage. No quantitative results, model performance metrics, or direct comparisons are provided. The central claims, while plausible, cannot be evaluated for technical soundness or robustness from the supplied material. The work addresses a timely question in cellular biophysics, but the abstract alone does not establish the case.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, protein folding, cellular biophysics, and computational chemistry would find this relevant. Those studying phase separation in disease contexts, particularly neurodegeneration involving TDP-43 and related proteins, would be interested in the potential mechanistic link between condensate environment and protein conformational stability. Computational method developers may also be interested in the Bayesian optimization approach for residue-resolution folding models.
- **Major strengths** The question is well motivated and timely. The proposed framework, balancing multivalent interactions against crowding, provides a testable conceptual model. The inclusion of disease-associated proteins adds translational relevance. The use of Bayesian optimization for chemically specific modeling is a potentially novel methodological contribution.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The concept of condensate-specific folding landscapes is not entirely new, but the specific focus on alpha-helices and the dual sequence dependence is a fresh angle. Scientific importance: Potentially high, given the link to proteinopathies, but importance depends on the robustness of the simulation evidence. Interdisciplinary readership: The topic bridges biophysics, cell biology, and computational chemistry, which could attract a broad audience. Technical soundness: Cannot be assessed from the abstract alone; no methodological details or validation are provided. Readability for nonspecialists: The abstract is clear and accessible, though terms like "Bayesian optimization" and "residue-resolution model" may require some background.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising but lacks the quantitative detail needed to support the central claims. A full manuscript with rigorous simulation data, model validation, and statistical analysis would be required to assess whether the case can be made.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "Atomistic simulations suggest the helix-coil transition within condensates differs markedly from its behavior in dilute solution or in the presence of inert crowders."
- **Evidence pointer** Abstract, no specific section or figure provided
- **Concern** The abstract states that atomistic simulations "suggest" a marked difference, but no quantitative data, simulation conditions, or comparison metrics are provided. It is unclear how many systems were simulated, what force fields were used, how condensates were modeled, or what the magnitude of the difference was.
- **Why it matters** The central premise of the paper rests on this simulation result. Without quantitative evidence, the claim is unverifiable and the reader cannot judge whether the observed effect is robust or an artifact of specific simulation choices.
- **Resolution test** Provide simulation details, including system composition, force field parameters, simulation length, and convergence criteria. Report quantitative measures of helix propensity (e.g., fraction of helical conformations, free energy differences) in condensate, dilute, and crowder conditions, with error estimates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** "We then use Bayesian optimization to develop a chemically specific, residue-resolution model for quantification of alpha-helical folding and apply it to characterize diverse helices..."
- **Evidence pointer** Abstract, no specific section or figure provided
- **Concern** The Bayesian optimization model is described as "chemically specific" and "residue-resolution," but no details are given on the training data, feature representation, optimization procedure, or validation against experimental or simulation benchmarks. The abstract does not state how model accuracy was assessed.
- **Why it matters** The model is the tool used to generate the main results on disease-associated helices. If the model is not validated, the subsequent conclusions about sequence-dependent folding landscapes are unsupported.
- **Resolution test** Describe the training set, model architecture, and optimization protocol. Provide validation metrics (e.g., correlation with experimental helix propensities, cross-validation errors) and demonstrate that the model reproduces known helix-coil behavior in dilute solution.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** "Our results support a framework in which multivalent interactions drive unfolding while crowding promotes folding, and alpha-helix conformational ensembles inside condensates emerge from this balance."
- **Evidence pointer** Abstract, no specific section or figure provided
- **Concern** The abstract asserts that results "support" a framework, but no data are shown to demonstrate the relative contributions of multivalent interactions versus crowding. It is unclear how these effects were disentangled in the simulations or model predictions.
- **Why it matters** The proposed balance is the core mechanistic insight. Without explicit evidence that varying interaction strength or crowding independently shifts helix stability, the framework remains speculative.
- **Resolution test** Present systematic variation of interaction parameters and crowder concentrations, showing how helix propensity changes in response. Provide a quantitative decomposition of the contributions from multivalent interactions and crowding to the free energy of folding.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** "kinetically frustrated"
- **Evidence pointer** Abstract, "Additionally, we show that helix folding transitions are kinetically frustrated inside condensates..."
- **Issue** The term "kinetically frustrated" is used without definition or quantitative support. It is unclear whether this refers to slower folding rates, increased roughness of the free energy landscape, or something else.
- **Required correction** Define the term in the context of the simulations and provide quantitative evidence, such as folding timescales or landscape roughness measures, to support the claim.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** "condensates of varying physicochemical properties"
- **Evidence pointer** Abstract, "within condensates of varying physicochemical properties"
- **Issue** The abstract does not specify which properties were varied (e.g., charge, hydrophobicity, density) or how many condensate types were tested. This limits the reader's ability to assess the breadth of the claim.
- **Required correction** List the specific physicochemical properties varied and the range of conditions tested in the simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scope
- **Affected element** "implications for understanding condensate-mediated proteinopathies"
- **Evidence pointer** Abstract, final sentence
- **Issue** The implications for proteinopathies are stated without any direct connection to disease mechanisms or experimental validation. This is a forward-looking statement, but it is presented as a conclusion.
- **Required correction** Clarify that these are potential implications and discuss how the findings might relate to disease, or remove the claim if it is not directly supported by the data.

## Risk / unsupported claims
- The claim that helix-coil transitions "differ markedly" in condensates is unsupported without quantitative data.
- The claim that the Bayesian optimization model is "chemically specific" and "residue-resolution" is unverifiable without model details and validation.
- The framework of "multivalent interactions drive unfolding while crowding promotes folding" is presented as supported, but no evidence is shown.
- The claim of "kinetic frustration" is unsupported without timescale or landscape data.
- The statement that folding landscapes are "dually sequence-dependent" is plausible but not demonstrated with specific examples.
- The implications for proteinopathies and condensate design are speculative and not tied to any presented results.