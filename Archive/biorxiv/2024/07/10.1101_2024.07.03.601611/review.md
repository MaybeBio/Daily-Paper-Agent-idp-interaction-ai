## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no full text, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and umbrella sampling to test whether small molecules bind intrinsically disordered islet amyloid polypeptide (IAPP) via conformational selection of pre-structured states rather than by inducing new conformations. They report that a two-state model (alpha-helix and beta-sheet) predicts experimentally observed selectivity for two classes of IAPP binders, with foldamers showing incomplete conformational selection and sensitivity to rat IAPP sequence changes, while beta-breaking peptides conform to conformational selection and are less sequence-sensitive.
- **Visible evidence base** Abstract text only; no simulation details, force fields, sampling convergence metrics, experimental binding data, or sequence alignments are visible
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation parameters, error estimates, experimental datasets, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents a conceptually interesting hypothesis that distinguishes conformational selection from induced-fit mechanisms for disordered protein binders, and the proposed two-state model is a plausible framework. However, the evidence base is limited to a summary of results with no quantitative data, no methodological detail, and no direct comparison to experimental measurements. The core claims, particularly the predictive accuracy of the model and the mechanistic distinction between binder classes, cannot be evaluated from the supplied material. The work has potential interest for the IDP and drug discovery communities, but the case is not established from the abstract alone.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, conformational ensembles, and molecular recognition; computational chemists and biophysicists developing binding affinity prediction methods; medicinal chemists targeting IDPs in metabolic or neurodegenerative diseases, given IAPP relevance to Type II Diabetes.
- **Major strengths** The question addressed is timely and mechanistically important, distinguishing conformational selection from induced fit in IDP binding. The use of a two-state model with conformation-specific affinities is a tractable and testable approach. The abstract explicitly connects computational predictions to experimental selectivity data, which strengthens the potential translational relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality is moderate to high, as the conformational selection versus induced fit distinction for IDP binders is not new conceptually, but the specific application to IAPP with a two-state model is a useful contribution. Scientific importance is potentially significant for IDP drug discovery, but the abstract does not provide sufficient evidence to assess the robustness of the findings. Interdisciplinary readership is plausible, spanning biophysics, computational chemistry, and pharmacology, but the abstract lacks sufficient detail for nonspecialists to evaluate the methods. Technical soundness cannot be assessed from the abstract alone, as no simulation or experimental details are provided. Readability for nonspecialists is adequate, with clear language, but the lack of quantitative results limits comprehension of the actual findings.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising but requires full manuscript review to verify the computational methods, model validation, and experimental comparisons.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "our two-state model of IAPP faithfully predicts the experimentally observed selectivity of two classes of IAPP binders."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states that the model predicts experimental selectivity, but no quantitative data, statistical measures, or direct comparisons are shown. It is unclear how "faithfully" is defined, what the magnitude of the predicted versus observed selectivity is, and whether the agreement is within experimental error.
- **Why it matters** Without quantitative evidence, the central claim of predictive accuracy cannot be verified. The distinction between conformational selection and induced fit hinges on the model's ability to reproduce experimental binding preferences, so this is the core of the paper's contribution.
- **Resolution test** Provide a figure or table comparing predicted and experimental binding affinities or selectivity ratios for both binder classes, including error bars and statistical tests (e.g., correlation coefficients, confidence intervals).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the binding preferences of foldamers designed for human IAPP was not fully accounted for by conformational selection, unlike beta-breaking peptides."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not specify the magnitude of the discrepancy for foldamers, the criteria for "not fully accounted for," or the alternative mechanism proposed. It is also unclear whether the beta-breaking peptides show complete agreement or only partial agreement with the model.
- **Why it matters** This claim is central to the mechanistic distinction between binder classes. Without a clear definition of what constitutes "not fully accounted for" and a quantitative comparison, the conclusion that conformational selection sometimes overrides sequence specificity is unsupported.
- **Resolution test** Define a quantitative threshold for model agreement (e.g., within 2-fold of experimental affinity) and show the deviation for each binder class. Discuss possible alternative mechanisms for foldamers, such as induced fit or non-specific binding.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and data availability
- **Claim pointer** The authors claim that "the binding of these foldamers, but not beta-breaking peptides, was disrupted by changes in the rat IAPP sequence."
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract does not provide the rat IAPP sequence changes, the experimental or computational methods used to test this, or the quantitative effect on binding. It is unclear whether this is based on new simulations, published experimental data, or a combination.
- **Why it matters** This claim supports the conclusion that conformational selection can override sequence specificity, but without details on the sequence variants and binding measurements, the result cannot be reproduced or evaluated.
- **Resolution test** Provide the specific rat IAPP mutations, the binding affinity changes for both binder classes, and the statistical significance of the differences. Clarify whether these data are from experiments or simulations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "rapid ability to self-associate or bind non-specific neighbors" is vague and could be more precise about the timescales or mechanisms.
- **Required correction** Specify the relevant timescales or refer to specific biophysical properties, such as aggregation propensity or promiscuous binding kinetics.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Abstract, methods description
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract mentions "molecular dynamics simulations" and "umbrella sampling" but does not state the force field, simulation length, or system setup, which are critical for reproducibility.
- **Required correction** Add a brief methods summary in the abstract or refer to the full methods section with key parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Abstract, final conclusion
- **Evidence pointer** Abstract, location not provided
- **Issue** The statement "conformational selection sometimes overrides sequence-level specificity" is broad and could be misinterpreted as a general principle beyond the IAPP system.
- **Required correction** Qualify the conclusion to specify that this is observed for the tested IAPP binders and may not generalize to all IDP systems.

## Risk / unsupported claims
- The claim that the two-state model "faithfully predicts" experimental selectivity is unsupported without quantitative data.
- The claim that foldamers are "not fully accounted for" by conformational selection is unsupported without a defined threshold or alternative mechanism.
- The claim that rat IAPP sequence changes disrupt foldamer binding is unsupported without specific sequence and binding data.
- The general conclusion that conformational selection can override sequence specificity is not established from the abstract alone.