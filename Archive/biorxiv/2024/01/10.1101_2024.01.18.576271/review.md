## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental procedures, supporting information references)
- **Assessment boundary** Scientific content, methodological soundness, and claims as presented in the provided text; no external data or unpublished materials consulted
- **Shared manuscript claim summary** The authors propose a molecular architecture for the autoinhibited full-length KIF5A homodimer, determined through a combination of negative-stain electron microscopy, crosslinking mass spectrometry, and AlphaFold2 modelling. They report that KIF5A adopts a compact bent conformation via a bend at P687, that the proximal C-terminal tail interacts with the motor domain, and that the exon-27 splice mutant associated with ALS shows a more labile autoinhibited state and aggregates in cells.
- **Visible evidence base** Abstract, Introduction, Results (three subsections), Discussion, Experimental Procedures, figure legends referenced but figures not provided, Supplemental Table 1 and 2 referenced but not provided
- **Missing materials affecting confidence** Figures 1–6 and Supplemental Figures 1–2 are referenced but not included; Supplemental Tables 1–2 (mutation list and XL-MS data) are not provided; raw mass spectrometry data and negative-stain EM maps are not accessible; no statistical analysis details for quantitative measurements

## Reviewer

- **Overall assessment** This manuscript addresses a relevant question in kinesin biology, namely the molecular architecture of autoinhibited KIF5A and the potential impact of disease-associated mutations on this regulation. The combination of nsEM, XL-MS, and AlphaFold2 is appropriate and timely. However, the evidence as presented is incomplete in several critical respects. The absence of the actual figures and supplemental data prevents full evaluation of the structural claims. The XL-MS data, which form a central pillar of the argument, are not shown in sufficient detail to assess their quality or interpretation. The functional cellular experiments are limited to a single qualitative readout (aggregation) and do not directly test the proposed mechanism of autoinhibition. The claim that the exon-27 mutant has a more labile autoinhibited state is inferred from increased crosslinking, which is an indirect and potentially confounded measure. The structural model is built with substantial manual intervention and low-resolution EM data, and the validation is not described with sufficient rigor. Overall, the work is potentially interesting but the case is not fully established from the provided materials.

- **Who would be interested in the results, and why** Cell biologists and biophysicists studying molecular motors, particularly kinesin regulation and autoinhibition mechanisms. Researchers interested in the structural basis of neurodegenerative diseases caused by kinesin mutations would also find the work relevant. The methodological combination of nsEM, XL-MS, and AlphaFold2 may interest structural biologists working on flexible or dynamic protein assemblies.

- **Major strengths** The study addresses a gap in knowledge regarding KIF5A-specific autoinhibition, as previous structural work focused on KIF5B and KIF5C. The combination of multiple structural and biochemical approaches is appropriate for studying a flexible, multi-domain protein. The inclusion of a disease-relevant splice mutant provides translational relevance. The authors are appropriately cautious in some interpretations, acknowledging limitations of the crosslinker reach and the possibility of alternative explanations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that XL-MS revealed extensive interactions between residues in the motor, between the motor and CC1, between coiled coils, and between the motor and the proximal C-terminal tail in the autoinhibited state.
- **Evidence pointer** Results section "Molecular architecture of autoinhibited KIF5A"; Figure 4; Supplemental Table 2 (not provided)
- **Concern** The XL-MS data are described only in summary form. The actual crosslinked residues, their positions in the structure, and the criteria for inclusion are not shown. The authors state that 38 out of 54 crosslinked pairs in the motor region were within the theoretical BS3 distance constraint, but the remaining 16 pairs are not discussed. No information is provided on how crosslinks were filtered, what false discovery rates were applied at the residue-pair level, or whether the crosslinks are consistent with a single conformational state or an ensemble.
- **Why it matters** The XL-MS data are used to validate the AlphaFold2 model and to support the claim that the proximal C-terminal tail interacts with the motor. Without seeing the actual crosslinks and their mapping onto the model, the reader cannot assess whether the data genuinely support the proposed architecture or whether they are equally consistent with alternative arrangements. The unexplained 16 out-of-distance crosslinks could indicate model inaccuracies or conformational heterogeneity.
- **Resolution test** Provide the full list of crosslinked residue pairs with their Cα-Cα distances in the final model, clearly mark those exceeding the BS3 constraint, and discuss how these outliers are reconciled with the proposed model. Show the XL-MS data mapped onto the structural model in a clear figure.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural evidence
- **Claim pointer** The authors claim that the final model, built by fitting AlphaFold2 segments into a 24 Å resolution negative-stain EM map, represents the molecular architecture of autoinhibited KIF5A.
- **Evidence pointer** Results section "Molecular architecture of autoinhibited KIF5A"; Figure 3; Experimental Procedures (EM reconstruction)
- **Concern** The EM map is at 24 Å resolution, which is very low. The authors describe manually positioning four AlphaFold2 segments into this map, using "flexibility provided by the disordered regions" and "iteratively improving the fit" with XL-MS restraints. The final model is not validated by any independent method, such as cross-validation with a subset of crosslinks, comparison to the known Drosophila crystal structure, or assessment of model-model agreement. The description of the fitting procedure is qualitative and does not include quantitative fit metrics.
- **Why it matters** At 24 Å resolution, the EM map can only provide a rough envelope. The manual fitting procedure introduces substantial subjectivity. Without quantitative validation, the model could be one of many equally plausible arrangements consistent with the low-resolution data. The claim that this model reveals the "molecular architecture" of autoinhibited KIF5A is therefore not fully supported.
- **Resolution test** Provide quantitative measures of model fit to the EM map (e.g., cross-correlation), describe the fitting procedure in a reproducible manner, and validate the model using a subset of XL-MS crosslinks not used in the fitting. If possible, compare the model to the known Drosophila kinesin-1 autoinhibited structure to demonstrate consistency.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation
- **Claim pointer** The authors state that the exon-27 KIF5A mutant showed aggregates when expressed as a GFP-fusion in mammalian cells, whereas wild-type protein had a diffuse organization, and that this suggests the mutant affects autoinhibition.
- **Evidence pointer** Results section "Full-Length KIF5A expressed and purified from Sf9 cells forms an autoinhibited dimer"; Figure 6
- **Concern** The cellular experiments are limited to a single qualitative observation of aggregation. No quantification is provided (e.g., percentage of cells with aggregates, number of aggregates per cell). The relationship between aggregation and autoinhibition is not directly established. The authors do not test whether the mutant is constitutively active, whether it fails to bind cargo, or whether the aggregation is due to misfolding rather than a specific defect in autoinhibition. The three missense mutations tested (P896L, D1002G, R1007G) showed a wild-type-like pattern, but this is presented without quantification or statistical comparison.
- **Why it matters** The paper's relevance to disease depends on linking the structural model to functional consequences of mutations. The current data are too preliminary to support the claim that the exon-27 mutant affects autoinhibition specifically. Aggregation could arise from many causes unrelated to the autoinhibitory mechanism.
- **Resolution test** Quantify the aggregation phenotype with clear criteria and statistical analysis. Include functional assays that directly test kinesin activity, such as microtubule binding, ATPase activity, or motility, for both wild-type and mutant constructs. If possible, test whether the exon-27 mutant affects the interaction between the C-terminal tail and the motor domain.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive caution
- **Claim pointer** The authors state that "the proximal region of the C-terminal tail (residues 890-910) close to the IAF motif is crosslinked to the motor domain" and interpret this as consistent with the known interaction of the IAK motif with the motor.
- **Evidence pointer** Results section "Molecular architecture of autoinhibited KIF5A"; Figure 4F
- **Concern** The crosslinks described are between residues upstream of the IAK motif (K901, K907, K911) and the motor domain, not the IAK motif itself. The authors acknowledge this but do not discuss whether these crosslinks are compatible with the known crystal structure of the motor-IK peptide complex. The distance between these residues and the IAK motif in the primary sequence is not trivial, and their spatial proximity to the motor in the model depends on the model's accuracy.
- **Why it matters** The interpretation that these crosslinks support the IAK-motor interaction is indirect. If the crosslinked residues are not in the IAK motif, their interaction with the motor could represent a different interface or a non-specific contact. The authors should clarify whether the crosslinked residues are spatially close to the IAK binding site in the model and whether the crosslinks are consistent with the known structure.
- **Resolution test** Map the crosslinked residues onto the known Drosophila motor-IK peptide structure and the final model, and discuss whether their positions are consistent with the IAK binding site. If the crosslinked residues are distant from the IAK binding site, discuss alternative interpretations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the C-terminal tail of KIF5A is "∼80 residues longer" than the other isoforms, but the Introduction states "about 70 residues longer." This discrepancy should be reconciled.
- **Required correction** Use a single consistent value or specify the exact length difference with reference to the alignment.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Experimental Procedures, XL-MS
- **Evidence pointer** Experimental Procedures
- **Issue** The description of the XL-MS data analysis is incomplete. The authors mention using XlinkX and Merox but do not specify how results from the two search engines were combined or reconciled. The criteria for accepting a crosslink (score thresholds, FDR) are described only as "cut off score set to 50" and "FDR threshold set to <0.01," but it is unclear whether this applies to peptide-spectrum matches, crosslinks, or both.
- **Required correction** Provide a more detailed description of the XL-MS data analysis pipeline, including how results from XlinkX and Merox were integrated, and define the FDR and score thresholds at each level.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, stalk length measurement
- **Evidence pointer** Results section "Full-Length KIF5A expressed and purified from Sf9 cells forms an autoinhibited dimer"; Figure 2F
- **Issue** The stalk length is reported as 31 ± 2.6 nm (mean ± SD), but the number of measurements (n) is not stated. It is also unclear whether this measurement was made on class averages or individual particles.
- **Required correction** State the number of measurements and the unit of analysis (class averages vs. individual particles).

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, exon-27 mutant
- **Evidence pointer** Results section "Full-Length KIF5A expressed and purified from Sf9 cells forms an autoinhibited dimer"; Supplemental Figure 2
- **Issue** The authors state that the exon-27 mutant was able to adopt the autoinhibited state based on nsEM, but no quantification or comparison to wild-type is provided. It is unclear whether the proportion of autoinhibited molecules differs between wild-type and mutant.
- **Required correction** Provide a quantitative comparison of the proportion of autoinhibited molecules between wild-type and exon-27 mutant, with appropriate statistics.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction, disease mutations
- **Evidence pointer** Introduction; Figure 1B; Supplemental Table 1
- **Issue** The authors state that "Disease causing mutations in KIF5A are far more common than those in KIF5B and KIF5C" and reference Supplemental Table 1. However, the source of this mutation list (HGMD) is described in the Experimental Procedures, and it is unclear whether the comparison to KIF5B and KIF5C is based on the same database and criteria.
- **Required correction** Clarify the source and criteria for mutation counts in all three isoforms, and ensure the comparison is apples-to-apples.

- **Technical failings that need to be addressed before the case is established** R1-M1 (XL-MS evidence not shown in sufficient detail), R1-M2 (structural model validation insufficient at 24 Å resolution with manual fitting), R1-M3 (functional data too preliminary to support claims about autoinhibition)

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of a multiscale approach to KIF5A specifically is novel, but the general architecture (bent autoinhibited conformation) has been established for other kinesin-1 isoforms. The finding that KIF5A follows a similar pattern is incremental.
  - Scientific importance: Moderate. Understanding KIF5A autoinhibition is relevant to neurodegenerative disease, but the study does not yet provide mechanistic insight beyond what is known for KIF5B/KIF5C. The disease relevance is asserted but not deeply explored.
  - Interdisciplinary readership: Limited. The work will primarily interest kinesin and motor protein researchers. The methods combination is not sufficiently novel to attract a broad structural biology audience.
  - Technical soundness: Not fully assessable from the provided materials. The XL-MS data and structural fitting are described but not shown in sufficient detail. The low resolution of the EM map and manual fitting are concerns.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, but some sections (e.g., detailed XL-MS descriptions) assume specialist knowledge. The abstract is clear.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant question and the methodological approach is appropriate, but the evidence as presented is incomplete. The XL-MS data, which are central to the claims, are not shown in sufficient detail. The structural model is built on low-resolution data with manual fitting and lacks independent validation. The functional experiments are too preliminary to support the disease-related claims. The authors should be encouraged to resubmit after providing the missing data and strengthening the validation and functional analyses.

## Risk / unsupported claims
- The claim that the exon-27 mutant has a more labile autoinhibited state is inferred from increased crosslinking but is not directly demonstrated; the relationship between crosslinking efficiency and conformational stability is not established.
- The claim that the distal C-terminal region does not interact with the rest of the molecule is based on absence of crosslinks, which could be due to technical limitations (e.g., lack of lysine residues in the vicinity, steric inaccessibility).
- The statement that the model "offers a conceptual framework for understanding how mutations within the motor and stalk domain may affect motor activity" is speculative and not tested experimentally.
- The claim that the three missense mutations (P896L, D1002G, R1007G) do not affect autoinhibition is based solely on the absence of visible aggregates, which is a weak proxy for functional activity.
- The assertion that the absence of a shoulder in nsEM images is consistent with the absence of light chains is reasonable but not directly tested; no light-chain-containing control is shown.
- The statement that the measured stalk length (31 nm) is "slightly shorter than expected" is not quantitatively reconciled with the model or with the expected length of the coiled-coil regions.