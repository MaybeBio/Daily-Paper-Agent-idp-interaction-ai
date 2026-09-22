## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or methods
- **Shared manuscript claim summary** The authors report coarse-grained simulations of binary mixtures of charge-symmetric (E25K25) and charge-asymmetric (E35K15) polyampholytes. They claim that E35K15 suppresses liquid-liquid phase separation (LLPS) in mixtures, with no LLPS at molar fractions of 0.5 and above, and that increasing E35K15 fraction leads to more collapsed E35K15 conformations, relatively unchanged E25K25 conformations, lower surface tensions, and enhanced polymer diffusivity in condensates.
- **Visible evidence base** Abstract text only; no quantitative data, simulation details, or figures provided
- **Missing materials affecting confidence** Full manuscript, simulation methodology, force field parameters, system sizes, equilibration protocols, phase boundary definitions, error bars, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study on how charge asymmetry modulates LLPS in polyampholyte mixtures. The central claim that charge-asymmetric E35K15 suppresses LLPS and alters condensate properties is plausible and could be of interest to the biomolecular condensate community. However, the abstract alone provides insufficient quantitative detail to evaluate the robustness of the findings. Key methodological choices, such as simulation model, concentration ranges, and criteria for LLPS determination, are not described. The mechanistic attribution to electrostatic repulsion is stated but not substantiated with direct evidence in the abstract. The work may be suitable for a specialized soft matter or biophysics journal, but the current evidence base is too limited to assess technical soundness or general significance.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, LLPS, intrinsically disordered proteins, and polyelectrolyte or polyampholyte phase behavior. The findings could inform understanding of how charge patterning and asymmetry influence phase separation in multicomponent protein mixtures, relevant to both synthetic biomimetic systems and cellular biology.
- **Major strengths** The study addresses a relevant and under-explored question about charge asymmetry in multicomponent polyampholyte mixtures. The use of model proteins with defined sequences (E25K25 and E35K15) provides a clear and systematic framework. The abstract reports multiple observables (phase behavior, conformations, surface tension, diffusivity) that together give a broad view of condensate properties.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation methodology and LLPS criteria not provided), R1-M2 (mechanistic claim of electrostatic repulsion not directly evidenced), R1-M3 (no quantitative data or error analysis presented)
- **Assessment against Nature-style criteria** Originality: moderate, as charge asymmetry effects on LLPS are not entirely new but the specific binary mixture design is a useful contribution. Scientific importance: moderate, relevant to condensate biophysics but not a transformative advance. Interdisciplinary readership: limited, primarily of interest to soft matter and biophysics specialists. Technical soundness: not assessable from the abstract alone, as simulation details and validation are absent. Readability for nonspecialists: the abstract is clear and accessible, though technical terms are used without definition.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a coherent study, but the lack of methodological and quantitative detail prevents assessment of whether the claims are supported. A full manuscript review would be required to determine if the case is convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that E35K15 suppresses LLPS in mixtures with E25K25, with no LLPS at molar fractions of 0.5 and above, based on coarse-grained simulations.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract provides no information about the simulation model, force field, system size, salt concentration, temperature, or the criteria used to define LLPS. Without these details, it is impossible to assess whether the reported phase behavior is robust or an artifact of specific simulation choices.
- **Why it matters** LLPS outcomes in coarse-grained simulations are highly sensitive to model parameters and to how phase separation is detected (e.g., density thresholds, cluster analysis, finite-size effects). The absence of this information undermines confidence in the central claim.
- **Resolution test** Provide a full methods section describing the simulation model, parameters, equilibration, and LLPS detection criteria, along with validation or convergence checks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors attribute the suppression of LLPS to electrostatic repulsion between negatively charged E35K15 polymers.
- **Evidence pointer** Abstract, location not provided
- **Concern** The abstract states this attribution without presenting direct evidence, such as radial distribution functions, electrostatic potential calculations, or comparisons with control systems where charge interactions are modified. The claim may be plausible, but it is not substantiated.
- **Why it matters** A mechanistic claim requires supporting evidence to distinguish it from alternative explanations, such as excluded volume effects, chain length differences, or changes in effective charge screening.
- **Resolution test** Include quantitative analyses that directly probe electrostatic interactions, such as pair correlation functions or energy decomposition, and discuss alternative mechanisms.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support
- **Claim pointer** The authors report that condensate density decreases with E35K15 fraction up to 0.4, surface tensions decline, and diffusivity is enhanced.
- **Evidence pointer** Abstract, location not provided
- **Concern** No numerical values, error bars, or statistical analyses are provided for any of these observables. The abstract reports trends without indicating their magnitude or significance.
- **Why it matters** Without quantitative data, the reader cannot evaluate the strength of the reported effects or whether they are statistically meaningful. This is essential for a computational study where reproducibility and precision are expected.
- **Resolution test** Present quantitative results with uncertainties, including phase diagrams, density profiles, surface tension values, and diffusion coefficients, in the full manuscript.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, location not provided
- **Issue** The term "charge-asymmetric" is used to describe E35K15, but the abstract does not define what asymmetry means in this context (e.g., net charge, charge distribution, or blockiness).
- **Required correction** Define charge asymmetry explicitly in the abstract or introduction, including the net charge of each polyampholyte.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Scope of claims
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states that E35K15 is "resistant to LLPS" but does not specify whether this is a kinetic or thermodynamic effect, which is a meaningful distinction in phase separation studies.
- **Required correction** Clarify whether the suppression is thermodynamic (shift in phase boundary) or kinetic (slower demixing), and provide supporting evidence.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Interpretation
- **Evidence pointer** Abstract, location not provided
- **Issue** The study uses only two specific sequences (E25K25 and E35K15), and the abstract does not discuss how the findings might generalize to other charge asymmetries or sequence patterns.
- **Required correction** Add a brief statement in the discussion about the expected generality or limitations of the findings.

## Risk / unsupported claims
- The claim that electrostatic repulsion between E35K15 polymers causes LLPS suppression is unsupported by direct evidence in the abstract.
- The quantitative trends for condensate density, surface tension, and diffusivity are reported without numerical data, making them unverifiable from the provided material.
- The statement that no LLPS occurs at molar fractions of 0.5 and above is not supported by any phase diagram or threshold definition.
- The conformational claims about E35K15 and E25K25 are not backed by any quantitative measures (e.g., radius of gyration) in the abstract.