## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose that transient tertiary interactions between two non-contiguous helical regions (SAH and H2) in the intrinsically disordered N-terminal domain of dynein intermediate chain (N-IC) are coupled to secondary structure formation and regulate differential binding to partners p150(Glued) and NudE. They further suggest that NudE binding shifts the conformational ensemble toward a more extended state with reduced H2 structure.
- **Visible evidence base** NMR paramagnetic relaxation enhancement experiments and restrained molecular dynamics simulations, as described in the abstract; specific data not available
- **Missing materials affecting confidence** Full manuscript, experimental details, NMR data, simulation parameters, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a mechanistically interesting hypothesis regarding the role of transient tertiary structure in an intrinsically disordered protein and its functional consequences for partner selection. The central claim that tertiary and secondary structure formation are coupled in IDPs is plausible and potentially significant, but the evidence as summarized is insufficient to fully evaluate the robustness of this conclusion. The differential effect of NudE binding on the conformational ensemble is a notable finding, yet the abstract does not provide quantitative detail or comparative data for p150(Glued) binding under the same conditions. The work is likely to interest researchers in dynein biology, IDP biophysics, and molecular recognition, but the current evidence base is too limited to establish the case definitively.
- **Who would be interested in the results, and why** Researchers studying cytoplasmic dynein regulation and cargo attachment, particularly those focused on the intermediate chain and its light chain partners. Also, the IDP community interested in transient tertiary structure, coupled folding and binding, and the functional role of conformational ensembles in molecular recognition. The methodological combination of NMR PRE and restrained MD simulations may appeal to computational and experimental biophysicists.
- **Major strengths** The study addresses a fundamental question in IDP biology, namely whether transient tertiary contacts can modulate partner specificity. The use of complementary experimental and computational approaches is appropriate. The identification of a specific structural mechanism (SAH-H2 interaction) that distinguishes binding to two different partners is conceptually elegant and potentially generalizable.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2
- **Assessment against Nature-style criteria** Originality is moderate to high, as the concept of transient tertiary structure regulating partner selection in IDPs is not entirely new but is applied here to a specific and biologically important system. Scientific importance is substantial given the central role of dynein in cellular processes and the general relevance to IDP function. Interdisciplinary readership is plausible, spanning cell biology, biophysics, and structural biology. Technical soundness cannot be fully assessed from the abstract alone, but the described methods are appropriate for the question. Readability for nonspecialists is adequate, though some terms (e.g., paramagnetic relaxation enhancement) may require background knowledge. Overall, the work has potential for a high-impact venue, but the evidence as presented is not yet sufficient to support all claims.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the quantitative evidence for the SAH-H2 interaction and the comparative analysis of NudE versus p150(Glued) binding.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract states that "transient tertiary interactions in this highly dynamic protein underlie the differences in its interactions with p150(Glued) and NudE" and that "tertiary and secondary structure formation are coupled in IDPs."
- **Evidence pointer** NMR paramagnetic relaxation enhancement experiments and restrained molecular dynamics simulations, as described in the abstract; specific data not provided
- **Concern** The abstract does not provide quantitative measures of the SAH-H2 interaction, such as PRE-derived distance restraints, population fractions of the interacting state, or free energy estimates from simulations. Without these numbers, the claim that tertiary interactions "underlie" the differential binding is not quantitatively supported. Additionally, the correlation between H2 length/stability and the extent of tertiary interaction is stated but not demonstrated with data.
- **Why it matters** The central mechanistic claim rests on the existence and magnitude of the SAH-H2 interaction. If the interaction is weak or its modulation by H2 properties is not statistically robust, the conclusion that this interaction regulates partner specificity would be overstated.
- **Resolution test** Provide quantitative PRE data (e.g., intensity ratios, distance bounds) and simulation-derived populations or free energy differences for the SAH-H2 contact, along with statistical error estimates. Show a clear correlation between H2 length/stability and the extent of tertiary interaction, ideally with a control where H2 is destabilized or deleted.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative analysis
- **Claim pointer** The abstract states that "These interactions are significantly attenuated when N-IC is bound to NudE, suggesting that NudE binding shifts the conformational ensemble to one that is more extended and with less structure in H2."
- **Evidence pointer** NMR PRE experiments and MD simulations, as described; comparative data for p150(Glued) binding not explicitly mentioned
- **Concern** The abstract reports attenuation of SAH-H2 interactions upon NudE binding but does not describe the corresponding effect of p150(Glued) binding. Without a direct comparison, it is unclear whether the attenuation is specific to NudE or a general consequence of partner binding. The claim that this difference "underlies" differential interactions requires a side-by-side analysis.
- **Why it matters** The proposed mechanism is that NudE specifically shifts the ensemble, whereas p150(Glued) does not, or does so differently. If p150(Glued) binding also attenuates SAH-H2 interactions, the mechanistic distinction would be weakened.
- **Resolution test** Include PRE and simulation data for N-IC bound to p150(Glued) under the same conditions, and show quantitative differences in SAH-H2 interaction strength and H2 structure between the two bound states.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional relevance
- **Claim pointer** The abstract concludes that "deviations of this protein from random-coil behavior provide a process for regulating these binding interactions and potentially the dynein motor."
- **Evidence pointer** Location not provided
- **Concern** The link between the observed conformational changes and functional regulation of dynein motor activity is speculative. The abstract does not present any functional assays (e.g., motor activity, cargo transport, or in vivo experiments) that connect the structural findings to dynein function.
- **Why it matters** The broader significance of the work depends on the functional consequences of the proposed mechanism. Without experimental evidence, the statement about regulating the dynein motor remains a hypothesis rather than a supported conclusion.
- **Resolution test** Add functional data, such as effects of H2 mutations on dynein-mediated transport or motor activity, or cite prior work that establishes a direct link between N-IC conformational changes and motor regulation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract, first sentence
- **Issue** The term "cargo attachment subcomplex" is used without definition or citation. Nonspecialist readers may not be familiar with this nomenclature.
- **Required correction** Define the term or provide a brief explanatory phrase, such as "the subcomplex that links dynein to its cargo."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Simulation description
- **Evidence pointer** Abstract, methods description
- **Issue** The abstract mentions "restrained molecular dynamics simulations" but does not specify the type of restraints (e.g., PRE-derived) or the force field used. This limits reproducibility assessment.
- **Required correction** Briefly state the source of restraints and the simulation protocol, or refer to a methods section where these details are provided.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Statement on H2 necessity
- **Evidence pointer** Abstract, second sentence
- **Issue** The abstract states that H2 is "necessary for tight binding to dynactin p150(Glued) but not to NudE." It is unclear whether "tight binding" refers to affinity, kinetics, or both, and whether this is based on prior work or new data.
- **Required correction** Clarify the basis of this statement and specify the binding parameter being referenced.

## Risk / unsupported claims
- The claim that tertiary and secondary structure formation are coupled in IDPs is presented as a general statement but is only supported by data from a single protein system; generalizability is not established.
- The statement that NudE binding shifts the ensemble to a "more extended" state is not quantitatively supported in the abstract.
- The suggestion that the proposed mechanism "potentially" regulates the dynein motor is speculative and not backed by functional evidence in the abstract.
- The differential effect of p150(Glued) versus NudE on SAH-H2 interactions is not directly compared, making the mechanistic distinction unverified from the supplied material.