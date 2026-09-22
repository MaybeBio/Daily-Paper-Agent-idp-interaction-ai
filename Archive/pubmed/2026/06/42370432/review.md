## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and conclusions
- **Assessment boundary** Scientific validity, methodological soundness, evidence quality, and alignment with claims presented in the manuscript
- **Shared manuscript claim summary** The authors introduce NMR-derived backbone dihedral terms into coarse-grained simulations to improve interdomain contact prediction in a mixed folded-disordered protein (DNAJB6 JD-GF construct), and validate these predictions against NMR relaxation data
- **Visible evidence base** Abstract, full text, methods, results, figures referenced (Fig. 1-4), supplementary figure references (Fig. S1-S10), tables referenced (Table S1, S2)
- **Missing materials affecting confidence** Supplementary figures and tables not provided; raw NMR data not provided; simulation parameter files not provided; specific numerical values for key metrics (e.g., contact lifetimes, correlation coefficients) not fully detailed in text

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to improving coarse-grained simulations of mixed folded-disordered proteins by incorporating NMR-derived backbone dihedral propensities. The biological system (DNAJB6) is relevant, and the methodological innovation is potentially useful. However, the evidence provided in the main text is insufficient to fully evaluate the validity of the approach, particularly regarding the quantitative agreement between simulations and experimental data. The claims about improved interdomain contact prediction rest heavily on comparisons that are only partially described in the visible text. The manuscript would benefit from clearer presentation of validation metrics and more explicit discussion of limitations.

- **Who would be interested in the results, and why** Researchers in computational biophysics, particularly those developing or using coarse-grained models for intrinsically disordered proteins; NMR spectroscopists interested in integrating experimental data into simulations; and structural biologists studying chaperone systems or mixed folded-disordered proteins. The methodological advance could be broadly applicable to systems where local backbone propensities influence long-range interactions.

- **Major strengths** 
  1. The conceptual idea of using NMR chemical shift-derived secondary structure propensities to inform coarse-grained simulations is timely and potentially impactful
  2. The biological system is well-chosen, with clear functional relevance (DNAJB6 anti-aggregation chaperone)
  3. The authors compare two popular CG force fields (Martini3IDP and CALVADOS), providing useful benchmarking
  4. The negative control experiment (GSS linker swap) is a good experimental design
  5. The software implementation is made freely available, supporting reproducibility

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence quality
  - **Claim pointer** "we generate conformational ensembles that yield accurate interdomain contact maps" and "the resulting ensembles show that even in the nominally open state the linker experiences motions that resemble those of the closed state"
  - **Evidence pointer** Fig. 3C, Fig. 4C, location not provided for quantitative comparison metrics
  - **Concern** The claim of "accurate" interdomain contacts is not supported by quantitative comparison metrics in the visible text. The authors state good agreement between calculated contact order values and long-range CSPs, but no correlation coefficients, RMSD values, or statistical tests are provided in the main text. The visual comparison in figures cannot be assessed without the actual figures.
  - **Why it matters** The central claim of the manuscript is that the modified CG simulations produce accurate interdomain contacts. Without quantitative validation metrics, the reader cannot assess whether the improvement is significant or coincidental. This is the core methodological advance, and its validation must be rigorous.
  - **Resolution test** Provide quantitative comparison between simulated contact order values and experimental CSP data, including correlation coefficients, p-values, and appropriate error estimates. Show that the agreement is significantly better than the unmodified CALVADOS simulations.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** "By tuning residue-specific backbone dihedral parameters (εd) to match NMR-derived secondary-structure propensities of the linker in CG-simulations, we generate conformational ensembles that yield accurate interdomain contact maps"
  - **Evidence pointer** Methods section, Table S2, location not provided
  - **Concern** The procedure for determining εd values is described only briefly. The authors state that εd values were "determined by maximizing the agreement with the observed secondary structure propensities calculated by Talos," but the optimization procedure, convergence criteria, and uniqueness of the solution are not described. It is unclear whether the εd values are overfitted to the specific system or transferable.
  - **Why it matters** If the εd parameters are tuned specifically to match the experimental data for this system, the approach may not be generalizable. The manuscript claims broad applicability, but the parameter determination procedure needs to be transparent and reproducible.
  - **Resolution test** Provide a detailed description of the εd optimization procedure, including the objective function, optimization algorithm, and sensitivity analysis. Show that the approach is robust to initial conditions and that the resulting parameters are physically reasonable.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence quality
  - **Claim pointer** "Analysis of NMR relaxation data revealed reduced dynamics for specific hydrophobic residues at both the N- and C-termini of the disordered GF linker, indicating sequence-dependent interactions with the folded J-domain"
  - **Evidence pointer** Fig. 1, Fig. S1, location not provided
  - **Concern** The interpretation of reduced dynamics (S2 values) as evidence for interactions with the J-domain is plausible but not directly demonstrated. The authors do not show direct evidence (e.g., intermolecular NOEs, PREs) that the reduced mobility of these residues is due to contacts with the J-domain rather than intrinsic backbone properties or transient secondary structure.
  - **Why it matters** The manuscript claims that the simulations reveal the physical basis for the observed dynamics. If the reduced dynamics are not actually caused by J-domain interactions, the interpretation of the simulation results would be incorrect.
  - **Resolution test** Provide additional experimental evidence (e.g., mutation studies, PRE data, or comparison with a construct lacking the J-domain) that directly links the reduced dynamics of specific residues to interdomain contacts.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods, spectral density mapping
  - **Evidence pointer** Methods section, equations 1 and 2
  - **Issue** The equations for determining τm and S2 are presented without derivation or context. The text states "as:1" and "by:152" but the equations themselves are not shown in the visible text.
  - **Required correction** Ensure equations are displayed in the final version and provide brief context for their derivation and assumptions.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, coarse-grained simulations
  - **Evidence pointer** Methods section, location not provided
  - **Issue** The simulation protocol is described briefly. Key parameters such as simulation length, temperature, salt concentration, and number of replicates are not stated in the visible text.
  - **Required correction** Provide complete simulation parameters in the Methods section or supplementary information.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Results, Fig. 4D and E
  - **Evidence pointer** Fig. 4D and E, location not provided
  - **Issue** The principal component analysis is described as showing that compaction of GF onto the front of helices 2 and 3 is the main component of motion, accounting for ~37% of total motion. It is unclear what the remaining 63% represents and whether this is sufficient to support the conclusions.
  - **Required correction** Provide a more complete description of the PCA results, including the fraction of variance explained by additional components and how this supports the interpretation.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Conclusions
  - **Evidence pointer** Conclusions section
  - **Issue** The authors state that the approach "allows for application of our method on systems of increasing size and complexity" but do not discuss potential limitations, such as the accuracy of the single-bead representation for capturing side-chain interactions or the transferability of the εd parameters to other systems.
  - **Required correction** Add a brief discussion of limitations and potential challenges for broader applicability.

- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative validation of contact accuracy), R1-M2 (transparency of εd optimization)

## Risk / unsupported claims
- The claim that the modified CG simulations yield "accurate interdomain contact maps" is not quantitatively supported in the visible text
- The claim that reduced dynamics of specific residues are due to interactions with the J-domain is inferred but not directly demonstrated
- The claim that the approach is broadly applicable to "regulatory IDRs in signaling proteins, transcription factors, and phase-separating or amyloid proteins" is speculative and not supported by data
- The statement that the approach "allows for application of our method on systems of increasing size and complexity" is not supported by benchmarks or examples beyond the single system studied

## Assessment against Nature-style criteria
- **Originality** The approach of incorporating NMR-derived backbone dihedral propensities into single-bead CG simulations is a novel contribution. While similar ideas exist in the literature (e.g., HPS-SS model), the specific application to mixed folded-disordered systems and the integration with NMR relaxation data is original.
- **Scientific importance** The work addresses a significant challenge in studying mixed folded-disordered proteins, which are prevalent in biology but difficult to characterize. The potential to improve CG simulations using readily available NMR data is important for the field.
- **Interdisciplinary readership** The work bridges NMR spectroscopy, computational biophysics, and protein biophysics. It would appeal to researchers in these areas, though the technical nature may limit broader readership.
- **Technical soundness** The methodological approach is reasonable, but the validation is incomplete. The lack of quantitative metrics for the central claim of "accurate" contacts is a significant weakness. The εd optimization procedure is not fully described, raising concerns about reproducibility and generalizability.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, with clear explanations of the biological context and methodological approach. However, some technical details (e.g., spectral density mapping, εd optimization) may be challenging for nonspecialists.

## Recommendation posture
Supportive if technical concerns are resolved. The conceptual advance is valuable, and the biological system is well-chosen. However, the central claim of accurate interdomain contact prediction requires quantitative validation, and the εd optimization procedure must be described transparently. If these issues are addressed, the manuscript could make a solid contribution to the field.