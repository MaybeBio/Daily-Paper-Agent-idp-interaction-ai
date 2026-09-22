## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and acknowledgments.
- **Assessment boundary** Scientific content, technical soundness, and alignment with stated claims. No assessment of editorial fit or publication venue.
- **Shared manuscript claim summary** The authors propose that conformational entropy of intrinsically disordered regions (IDRs) in biomolecular condensates creates a free-energy barrier that excludes non-interacting macromolecules ("intruders"), with exclusion scaling with intruder surface area for large particles, and that recruitment of clients requires attractive interactions to overcome this entropic cost.
- **Visible evidence base** Coarse-grained molecular dynamics simulations (sticker-spacer models with compact vs. IDR spacers), Widom insertion calculations, polymer scaling theory, and comparison with experimental data from the literature (dextran partitioning into LAF-1 condensates).
- **Missing materials affecting confidence** Supplementary figures (Fig. S1, Fig. S2) referenced but not provided. No experimental validation by the authors. No analysis of sensitivity to simulation parameters (e.g., sticker density, chain length, interaction strengths) beyond the specific cases shown.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting and potentially important hypothesis: that IDR conformational entropy provides a generic size-exclusion mechanism in biomolecular condensates. The combination of simulation and theory is well executed, and the scaling predictions are clearly derived. However, the central claim that this mechanism operates broadly in biological condensates rests on limited evidence, and the quantitative predictions depend on parameters (e.g., correlation length, volume fraction) that are not directly measured in experiments. The work is a solid contribution to the physical understanding of condensate selectivity, but the biological generality is asserted rather than demonstrated.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, polymer physics, and cellular organization. The work provides a physical mechanism for condensate selectivity that complements existing models based on specific interactions. It may also interest experimentalists studying condensate composition and permeability, as it offers testable predictions (e.g., size-dependent exclusion thresholds).
- **Major strengths** 1. Clear and compelling physical argument linking IDR conformational entropy to size exclusion. 2. Rigorous simulation methodology with careful comparison between compact and IDR spacers. 3. Derivation of a scaling law that connects microscopic parameters to macroscopic exclusion behavior. 4. Validation of the Widom insertion approach against direct coexistence simulations. 5. Application to published experimental data (dextran partitioning) provides a concrete test of the theory.
- **Major Concerns** 1. The claim that IDR-based exclusion is "generic" across biological condensates is extrapolated from a single in vitro system (LAF-1) and a simplified model. 2. The theory assumes that IDRs behave as flexible self-avoiding polymers, but real IDRs may have sequence-specific interactions, secondary structure propensities, or charge effects that alter their conformational statistics. 3. The role of condensate surface tension and interfacial effects on partitioning is not addressed, which could be significant for small condensates. 4. The derivation of Eq. (8) assumes independence of repulsive and attractive contributions, which may not hold when binding sites are located on the same polymer chains that cause exclusion.
- **Minor Comments** 1. The term "intruders" is used throughout but is not formally defined; clarify whether it refers to any non-interacting macromolecule or specifically to proteins/RNAs. 2. The discussion of pressure-volume work in Eq. (5) is brief; a more detailed explanation of when this term is relevant would aid the reader. 3. The authors state that "particles as small as the size of an average protein (4 nm in diameter) can be 97% excluded" but do not specify the condensate conditions (e.g., volume fraction) under which this applies. 4. The comparison with experimental data in Ref. [6] is qualitative; a more quantitative fit would strengthen the case.
- **Technical failings that need to be addressed before the case is established** 1. The assumption that IDRs in real condensates can be modeled as fully flexible, self-avoiding chains without sequence-specific effects needs justification or caveats. 2. The extrapolation from model simulations to biological condensates requires a clearer statement of the parameter ranges (e.g., IDR volume fraction, correlation length) that are realistic in cells. 3. The independence assumption in Eq. (8) should be tested in simulations where binding sites are placed on the IDR chains themselves, rather than as separate entities.
- **Assessment against Nature-style criteria** Originality: High. The idea that IDR entropy provides a generic exclusion mechanism is novel and distinct from prior work focusing on mesh size or specific interactions. Scientific importance: Moderate to high. If correct, the mechanism has broad implications for condensate composition and function, but the evidence is currently limited to simulations and one experimental system. Interdisciplinary readership: The work bridges polymer physics and cell biology, and the writing is accessible to both communities, though some polymer physics concepts (e.g., blob picture) may be challenging for biologists. Technical soundness: The simulations and theory are well executed, but the biological extrapolation is not fully supported. Readability for nonspecialists: The abstract and introduction are clear, but the results section assumes familiarity with polymer physics concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core physical insight is valuable and the methodology is sound, but the claim of biological generality requires either additional experimental validation or a more careful delineation of the conditions under which the mechanism applies.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim generality
- **Claim pointer** The authors state that "condensate IDRs may play a generic exclusionary role across organisms and types of condensates."
- **Evidence pointer** Discussion section, application to LAF-1 condensates (Ref. [6])
- **Concern** The claim of generic applicability is based on a single experimental example (LAF-1) and a simplified polymer model. Real IDRs have sequence-specific properties (charge patterning, hydrophobicity, secondary structure propensity) that could alter their conformational statistics and thus the exclusion behavior. The model treats IDRs as fully flexible, self-avoiding chains, which may not capture the behavior of all IDRs in biological condensates.
- **Why it matters** If the mechanism is not generic, the conclusions would be limited to specific systems, reducing the broader significance of the work.
- **Resolution test** Provide additional evidence, either from simulations with sequence-specific IDR models or from experimental data on multiple condensate types, that the exclusion mechanism holds across diverse systems. Alternatively, clearly delineate the conditions (e.g., IDR composition, concentration) under which the mechanism is expected to apply.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model realism
- **Claim pointer** The theory assumes that IDRs in condensates behave as flexible polymers in a good solvent, with no specific interactions beyond excluded volume.
- **Evidence pointer** Methods, simulation details for Fig. 2 (right panels); Eq. (5) and Eq. (6)
- **Concern** Real IDRs may have intramolecular interactions (e.g., electrostatic, hydrophobic) that affect their conformational entropy and thus the exclusion barrier. The model also neglects the possibility that IDRs form transient secondary structures or engage in homotypic interactions that could alter the effective polymer statistics. The choice of parameters (e.g., bond length, bead size) is reasonable but not justified against experimental measurements of IDR dimensions.
- **Why it matters** If the model does not capture the essential physics of real IDRs, the quantitative predictions (e.g., exclusion thresholds) may not be reliable for biological systems.
- **Resolution test** Compare model predictions to experimental measurements of IDR conformational properties (e.g., radius of gyration, scaling exponents) in condensates. If discrepancies arise, discuss how they would affect the exclusion predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Independence assumption
- **Claim pointer** Eq. (8) assumes that repulsive (exclusion) and attractive (binding) contributions to the free energy are independent.
- **Evidence pointer** Derivation of Eq. (8), Methods section
- **Concern** In real condensates, binding sites are often located on the same IDR chains that cause exclusion. The presence of a bound client may locally alter the chain conformation, potentially reducing the entropic cost of insertion. The independence assumption may therefore overestimate the exclusion barrier for clients that bind to the scaffold.
- **Why it matters** If the independence assumption is violated, the predicted recruitment free energy could be inaccurate, affecting the conditions under which molecules transition from intruders to clients.
- **Resolution test** Perform simulations where clients bind to stickers located on the IDR chains and compare the measured free energy to the prediction of Eq. (8). If deviations are found, modify the theory to account for coupling between binding and conformational entropy.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "intruders"
- **Evidence pointer** Abstract, Introduction
- **Issue** The term "intruders" is used to describe non-interacting macromolecules, but it is not formally defined. It is unclear whether this includes all proteins, only those above a certain size, or specifically non-interacting species.
- **Required correction** Provide a clear definition of "intruders" in the Introduction, specifying the size range and interaction criteria.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Quantitative detail
- **Affected element** Claim about 97% exclusion
- **Evidence pointer** Abstract, Results section
- **Issue** The statement that "particles as small as the size of an average protein (4 nm in diameter) can be 97% excluded" lacks context. The conditions (e.g., IDR volume fraction, correlation length) under which this applies are not specified.
- **Required correction** Specify the condensate conditions (e.g., volume fraction, correlation length) used to arrive at this number, or provide a range of values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of pressure-volume work
- **Evidence pointer** Results section, Eq. (5)
- **Issue** The pressure-volume term in Eq. (5) is mentioned but not explained in detail. It is unclear when this term is significant and how it affects the predictions.
- **Required correction** Add a brief explanation of the pressure-volume term, including when it is relevant and how it was accounted for in the simulations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Experimental comparison
- **Affected element** Comparison with dextran data
- **Evidence pointer** Results section, application to LAF-1
- **Issue** The comparison with experimental data from Ref. [6] is qualitative. A more quantitative fit (e.g., comparing predicted and measured partition coefficients) would strengthen the case.
- **Required correction** Provide a quantitative comparison, if possible, or discuss the limitations of the available data.

## Risk / unsupported claims
- The claim that IDR-based exclusion is "generic" across organisms and condensate types is not supported by the evidence, which is limited to one experimental system and a simplified model.
- The quantitative predictions (e.g., 97% exclusion for 4-nm particles) depend on parameters (e.g., volume fraction, correlation length) that are not directly measured in biological condensates.
- The independence assumption in Eq. (8) is not tested for the case where binding sites are located on the IDR chains themselves.
- The model neglects sequence-specific properties of real IDRs, which could affect the conformational entropy and thus the exclusion barrier.