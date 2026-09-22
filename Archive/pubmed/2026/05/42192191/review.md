## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary information references
- **Assessment boundary** Scientific content, methodological rigor, validity of conclusions, and alignment with stated claims
- **Shared manuscript claim summary** The authors use molecular dynamics simulations and quantum chemical calculations to show that arginine (Arg) is consistently a stronger "sticker" than lysine (Lys) in biomolecular condensates across diverse environments, and that this difference is primarily driven by the higher dehydration penalty of Lys rather than by cation-π interaction strength. They also report that the preferred aromatic partner (Phe vs Tyr) for cation-π interactions depends on the dielectric environment.
- **Visible evidence base** Main text figures (Figs. 1-6), supplementary figures referenced (S1-S11), methods section, and cited literature
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided in the submitted material; raw simulation data and analysis scripts not available; details of force field parameters for organic solvents not fully specified

## Reviewer

- **Overall assessment** This manuscript addresses an important question in the field of biomolecular condensates: the molecular basis for the differential "stickiness" of Arg versus Lys. The combination of alchemical free energy calculations and quantum chemical methods is appropriate and the conclusions are generally well-supported by the presented data. The finding that transfer free energies, rather than intrinsic interaction strengths, dominate the Arg/Lys difference is a valuable contribution. However, several technical aspects require clarification and additional analysis before the case is fully established, particularly regarding the robustness of the alchemical calculations in heterogeneous condensate environments and the interpretation of the dielectric-dependent crossover in interaction energies.

- **Who would be interested in the results, and why** Researchers studying phase separation and biomolecular condensates, particularly those interested in sequence determinants of condensate formation. The work is also relevant to the broader biophysics community studying cation-π interactions, protein-protein interactions in confined environments, and the role of solvation in molecular recognition. The methodological approach combining alchemical free energy calculations with quantum chemistry will be of interest to computational biophysicists.

- **Major strengths** The study addresses a question of clear biological relevance with a well-designed multi-scale approach. The use of alchemical transformations to directly compute transfer free energy differences is rigorous. The authors carefully consider the limitations of classical force fields for cation-π interactions and complement their MD results with DFT calculations. The comparison between interaction energies and contact energies provides mechanistic insight that goes beyond simple pairwise interaction strengths. The consideration of different neutralization conditions and multiple solvents strengthens the generality of the conclusions.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of alchemical calculations in condensate environment
- **Claim pointer** The authors claim that "the value of ΔΔGTransfer is negative in both the GSF and GSY condensates" and that this indicates "Arg has a stronger propensity to be part of the model peptide condensates than Lys."
- **Evidence pointer** Figure 2C, Methods section "Details of the simulations"
- **Concern** The alchemical free energy calculations are performed in a heterogeneous condensate slab environment. The authors note that the peptide "escapes from the condensate interior more readily and stays temporarily at the interface region" in the GSF condensate (Supplementary Fig. S3). This raises a critical question: are the free energy calculations sampling a well-defined thermodynamic state? If the peptide is not consistently buried within the condensate during the alchemical transformation, the computed ΔG values may represent a mixture of environments (interior, interface, and possibly bulk water), making the interpretation of ΔΔGTransfer ambiguous. The authors state they excluded configurations where the peptide was not buried, but the criteria for this exclusion and the fraction of configurations excluded are not provided.
- **Why it matters** The central conclusion of the manuscript rests on the reliability of these alchemical calculations. If the peptide samples multiple environments during the transformation, the computed free energy difference cannot be cleanly attributed to transfer into the condensate phase. This would undermine the quantitative claims about the Arg/Lys difference.
- **Resolution test** Provide a detailed analysis of the environment sampled by the peptide during the alchemical transformations, including the distribution of peptide positions relative to the condensate interface, the fraction of configurations excluded, and a demonstration that the computed free energies are converged with respect to the choice of starting configurations. Ideally, the authors should show that the results are robust when the analysis is restricted to configurations where the peptide is fully buried in the condensate interior.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of quantum chemical results
- **Claim pointer** The authors state that "at very low dielectric regimes, T-shaped structures are favoured in both Arg-Phe and Arg-Tyr complexes, whereas at higher dielectrics, stacked conformations predominate" and that "the preferred aromatic partner for these cations depends on the dielectric environment."
- **Evidence pointer** Figure 6A, B, C
- **Concern** The DFT calculations use isolated side chain analogues in a continuum solvent. While this approach is reasonable for probing intrinsic interaction preferences, the relevance of the very low dielectric values (approaching ε = 2) to actual condensate environments is not clearly established. The authors mention that condensates have ε around 40, but the crossover in interaction energy preferences occurs at much lower values. The biological relevance of the low-dielectric regime is therefore unclear. Additionally, the contact energy calculations combine transfer free energies from SMD with interaction energies from a different level of theory (ωB97XD vs B3LYP), and the consistency of this combination is not discussed.
- **Why it matters** The manuscript claims to provide "molecular determinants" of Arg/Lys behavior in condensates. If the dielectric regime where the interesting crossover behavior occurs is not representative of actual condensate conditions, the relevance of these findings to the biological system is limited. The mixed-level approach for contact energies could introduce systematic errors that affect the conclusions.
- **Resolution test** Provide a clearer justification for the range of dielectric constants considered, with explicit reference to estimated values in condensates and other relevant biological environments. Discuss the potential errors introduced by combining different levels of theory in the contact energy calculations, and ideally validate the approach against experimental data where available.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The authors conclude that "Arg promotes phase separation more effectively than Lys" and that this hierarchy is "consistent across diverse molecular environments."
- **Evidence pointer** Figures 2C, 3A, 6B
- **Concern** The conclusions are based on model systems: short peptides (GGXGG) in simplified condensates composed of only Gly, Ser, and Phe/Tyr, and isolated side chain analogues in quantum calculations. While the authors acknowledge this limitation in the conclusions, the strength of the claims in the abstract and introduction goes beyond what can be directly supported by these minimal models. Real condensates contain a complex mixture of residues, and the context-dependence of Arg/Lys behavior in full-length proteins may differ from what is observed in these simplified systems. The authors do not discuss how their findings might be modulated by the presence of other residue types, post-translational modifications, or nucleic acids.
- **Why it matters** The manuscript aims to explain "the distinct contributions of Arg and Lys to condensate stability" in biological systems. If the conclusions are only valid for the specific model systems studied, the broader claims about biological condensates are overstated.
- **Resolution test** Either temper the claims to more precisely reflect the model systems studied, or provide additional evidence (e.g., simulations with more complex sequences, comparison with experimental data on full-length proteins) that supports the generalizability of the findings.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2C
- **Evidence pointer** Figure 2C
- **Issue** The error bars in Figure 2C are not described in the figure legend. It is unclear whether they represent standard deviations, standard errors, or confidence intervals from the bootstrap analysis mentioned in the Methods.
- **Required correction** Specify the type of error bars shown and the number of bootstrap samples used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section "Details of the simulations"
- **Evidence pointer** Methods section
- **Issue** The authors state that simulations were run for "up to 5 μs" but do not specify the exact simulation lengths for each system. Additionally, the number of independent replicates for each condition is not stated.
- **Required correction** Provide a table or text specifying the simulation length and number of replicates for each system studied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Discussion of Figure 4
- **Evidence pointer** Figure 4
- **Issue** The authors interpret the orientational preference of Arg for stacked conformations as evidence for cation-π interactions. However, the classical force field used (Amber99SB*-ILDN) may not accurately capture the polarization effects that are important for cation-π interactions, as the authors themselves note. The connection between the MD-observed geometries and the DFT-computed interaction energies could be made more explicit.
- **Required correction** Discuss how the MD-observed geometries relate to the DFT-optimized structures, and whether the force field limitations could affect the observed conformational preferences.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of supplementary data
- **Affected element** Supplementary figures
- **Evidence pointer** Supplementary Figures S1-S11
- **Issue** The supplementary figures are referenced throughout the text but were not provided with the manuscript. This makes it impossible to fully evaluate the convergence of the simulations, the validation of the SMD approach, and the additional conformational analysis.
- **Required correction** Ensure that all supplementary material is available for review and clearly referenced in the main text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract
- **Issue** The term "sticker" is used without formal definition. While this term is common in the condensate field, a brief definition would improve accessibility for readers outside the immediate field.
- **Required correction** Add a brief definition or explanation of "stickers" and "spacers" at first use.

## Risk / unsupported claims
- The claim that Arg is "consistently" a stronger sticker than Lys across "diverse molecular environments" is supported for the specific solvents and condensate compositions tested, but the extrapolation to all biological condensates is not directly supported by the data presented.
- The statement that "the primary factor driving this difference is the higher dehydration penalty of Lys" is well-supported by the contact energy analysis, but the quantitative decomposition of this penalty into specific physical contributions (e.g., desolvation vs. interaction) is not fully established.
- The claim that "the preferred aromatic partner for these cations depends on the dielectric environment" is supported by the DFT calculations, but the biological relevance of the low-dielectric regime where the crossover occurs is not clearly demonstrated.
- The assertion that "monomer transfer energies are often the dominant factor in determining residue preferences" is a general statement that goes beyond the specific systems studied here and would require broader evidence to be fully supported.
- The relevance of the model condensates (composed of only Gly, Ser, and Phe/Tyr) to real biological condensates is acknowledged as a limitation, but the potential impact of this simplification on the conclusions is not quantitatively assessed.