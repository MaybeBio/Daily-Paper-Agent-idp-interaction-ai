## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the supplied abstract and significance statement
- **Shared manuscript claim summary** The authors use residue-resolution coarse-grained molecular dynamics simulations to connect condensate viscoelasticity to the architectural heterogeneity and dynamic reconfigurability of IDP associative networks. They report sequence-dependent temperature sensitivity of elasticity, entropy-driven structural heterogeneity and reduced hydrophobicity favoring elasticity, graph-theoretical evidence that redundant node pathways enhance load-bearing capacity, and a key finding that elastic coupling emerges when single-molecule shape memory timescales approach meshwork reconfiguration timescales, formalized as a condensate Deborah number.
- **Visible evidence base** Abstract text and significance statement only. No figures, tables, methods, simulation parameters, or quantitative results are provided.
- **Missing materials affecting confidence** All quantitative data, simulation details, model validation, statistical analyses, figure panels, and methodological descriptions are absent. The abstract references "exponential scaling laws," "entanglement spacing," "graph-theoretical representations," and "Deborah number" without presenting any numerical values or derivations.

## Reviewer

- **Overall assessment** The abstract presents a conceptually appealing framework linking molecular timescales to condensate mechanics, and the proposed Deborah number analogy is potentially impactful. However, the supplied material is an abstract only, with no supporting data or methods. The central claims, particularly the timescale-matching mechanism and the graph-topology-to-elasticity link, cannot be evaluated for technical soundness. The significance statement is well written and accessible, but the evidence base is insufficient to establish the case.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, soft matter physics, and mechanobiology would be interested. The proposed sequence-dependent Deborah number offers a potentially predictive framework for condensate material design, which appeals to synthetic biology and biomaterials communities. The connection between single-molecule conformational memory and network rheology also speaks to polymer physics and IDP biophysics audiences.
- **Major strengths** The conceptual framing is clear and novel, particularly the timescale-ratio approach to condensate viscoelasticity. The abstract successfully bridges molecular-level IDP behavior to mesoscale mechanical responses. The significance statement is concise and accessible to nonspecialists. The proposed framework has clear experimental testability via accessible timescale measurements.
- **Major Concerns** The absence of any quantitative evidence or methodological detail prevents assessment of the central claims. The abstract makes strong universal claims ("is dictated by," "robust indicator") that require substantial validation across sequence space and conditions. The graph-theoretical and entanglement analyses are mentioned but not described in sufficient detail to judge their validity or interpretation.
- **Minor Comments** The abstract uses terms such as "entanglement spacing" and "mesh heterogeneity" without defining operational measures. The relationship between "redundant node pathways" and "load-bearing paths" is asserted but not mechanistically explained. The significance statement repeats the abstract's key points without adding new information.
- **Technical failings that need to be addressed before the case is established** No quantitative results, simulation protocols, model validation, or statistical analyses are provided. The central timescale-matching claim is presented without any data showing the crossover behavior. The graph-theoretical metrics are not defined, and their connection to mechanical stress storage is not demonstrated.
- **Assessment against Nature-style criteria** Originality is high, as the Deborah number analogy for condensates is a fresh conceptual contribution. Scientific importance is potentially high, given the need for predictive frameworks in condensate mechanics. Interdisciplinary readership is plausible, spanning biophysics, soft matter, and cell biology. Technical soundness cannot be assessed from the abstract alone. Readability for nonspecialists is good, particularly in the significance statement, though some jargon (e.g., "mesh reconfigurability," "shape memory timescales") would benefit from brief definitions.
- **Recommendation posture** Currently not established from the provided evidence. The conceptual framework is promising, but the abstract alone does not provide sufficient data or methodological transparency to support the claims. A full manuscript with quantitative results and methods would be required for a supportive posture.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "elastic coupling of IDPs within condensates emerges when single-molecule shape memory timescales approach meshwork reconfiguration timescales" and that this is "a robust indicator of whether a condensate is dominantly viscous or elastic."
- **Evidence pointer** Abstract, location not provided
- **Concern** The central mechanistic claim of the paper is presented without any quantitative data. No timescales, crossover behavior, or comparison across sequences or conditions are shown. The claim that this timescale ratio is "robust" requires demonstration across a range of IDP sequences, concentrations, and thermodynamic conditions.
- **Why it matters** This is the core novel finding and the basis for the proposed Deborah number framework. Without evidence, the claim remains an assertion. The robustness claim is particularly important because condensate mechanics are known to be sensitive to many parameters, and a single timescale ratio may not capture all relevant physics.
- **Resolution test** Provide data showing the viscoelastic response (e.g., storage and loss moduli) as a function of the ratio of single-molecule shape memory timescale to network reconfiguration timescale, across multiple IDP sequences and conditions. Demonstrate a clear crossover from viscous to elastic behavior at a consistent ratio value, with statistical significance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "interaction network topologies with an abundance of redundant node pathways translates to more load-bearing paths for mechanical stress storage."
- **Evidence pointer** Abstract, location not provided
- **Concern** The graph-theoretical analysis is mentioned but no details are given on how condensate networks are constructed as graphs, what nodes and edges represent, how redundancy is quantified, or how load-bearing paths are identified. The causal link between topological redundancy and mechanical stress storage is asserted without mechanistic explanation or validation.
- **Why it matters** This claim connects network architecture to mechanical function, which is a potentially important contribution. However, without defined metrics and validation, the claim is unfalsifiable from the provided material. The interpretation of "redundant node pathways" as beneficial for load-bearing is counterintuitive and requires careful justification.
- **Resolution test** Define the graph construction and metrics precisely. Show that condensates with higher redundancy metrics exhibit higher elastic modulus or slower stress relaxation in simulations. Provide a mechanistic explanation for why redundancy enhances load-bearing capacity, possibly through alternative pathway recruitment under deformation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "their temperature sensitivity of elasticity is sequence dependent and modeled by exponential scaling laws" and that "entropy-driven structural heterogeneity and reduced IDP hydrophobicity favor condensate elasticity."
- **Evidence pointer** Abstract, location not provided
- **Concern** These quantitative claims are presented without any numerical results, scaling exponents, or comparisons across sequences. The relationship between hydrophobicity and elasticity is stated as a general finding, but no data on sequence variants or hydrophobicity metrics are shown. The "entropy-driven" mechanism is not explained.
- **Why it matters** These claims form the basis for the sequence-dependent design principles proposed in the abstract. Without quantitative support, the predictive power of the framework cannot be evaluated. The hydrophobicity-elasticity relationship is particularly important because it suggests a simple design rule that requires validation.
- **Resolution test** Provide scaling exponents with confidence intervals for multiple sequences. Show a systematic variation of hydrophobicity (e.g., through sequence mutations) with corresponding changes in elastic modulus. Demonstrate that the entropy-driven mechanism is supported by structural or thermodynamic measurements in the simulations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The terms "entanglement spacing" and "mesh heterogeneity" are used without operational definitions. It is unclear whether these refer to specific simulation-derived quantities or conceptual constructs.
- **Required correction** Define these terms explicitly in the methods or results, including how they are computed from simulation trajectories.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Significance statement
- **Evidence pointer** Significance statement, location not provided
- **Issue** The significance statement largely repeats the abstract's key points without adding new context or implications for broader biological or materials science audiences.
- **Required correction** Expand the significance statement to discuss specific biological contexts where the Deborah number framework could be applied (e.g., mechanosensing, disease-related condensate stiffening) and potential experimental validation strategies.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Claim wording
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "is dictated by" in the title and abstract implies a deterministic relationship that may overstate the role of the timescale interplay given other known factors influencing condensate mechanics (e.g., concentration, salt, ATP).
- **Required correction** Soften the language to "is strongly influenced by" or "is modulated by" to reflect the multifactorial nature of condensate viscoelasticity.

## Risk / unsupported claims

- The central timescale-matching mechanism (Deborah number analogy) is unsupported by any quantitative data in the supplied material.
- The claim that graph-topological redundancy enhances load-bearing capacity is unsupported and lacks defined metrics.
- The sequence-dependent exponential scaling laws for temperature sensitivity of elasticity are unsupported without numerical exponents or fits.
- The claim that reduced hydrophobicity favors elasticity is unsupported without systematic sequence variation data.
- The assertion that the Deborah number is "experimentally accessible" is plausible but not substantiated with specific experimental protocols or precedents.
- The generalizability of the findings to "biologically relevant and synthetic condensates" is claimed but not demonstrated with specific systems or validation.