## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, and methods sections.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and structural claims as presented in the manuscript. No independent verification of experimental data was performed.
- **Shared manuscript claim summary** The authors report an NMR-derived complex structure of the SARS-CoV-2 nucleocapsid protein N-terminal domain (N-NTD) bound to a 58-nt DNA aptamer, A48. They identify the intrinsically disordered N-terminus (residues 26–43) and the basic finger region as key binding epitopes, with arginine residues in the IDR playing critical roles in both binding affinity and complex architecture. The study highlights the functional importance of the N-terminal IDR, which was excluded in most prior structural studies.
- **Visible evidence base** NMR spectroscopy data (HSQC, chemical shift perturbation, arginine side-chain assignments), surface plasmon resonance binding assays, mutagenesis experiments, HADDOCK docking, and molecular dynamics simulations. Figures 1–6 and Supplementary Figures S1–S6 are referenced.
- **Missing materials affecting confidence** Raw NMR spectra, chemical shift assignments, structural coordinates of the complex, validation statistics for the docked model, and full SPR sensorgrams are not provided. The manuscript does not include a PDB deposition code or a detailed description of the NMR restraints used for structure calculation.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question regarding the molecular basis of DNA aptamer recognition by the SARS-CoV-2 N protein, with a specific focus on the role of the intrinsically disordered N-terminus. The combination of NMR spectroscopy, mutagenesis, and binding assays is appropriate and the findings are potentially interesting. However, several technical aspects require clarification and additional evidence before the central claims can be fully supported. The structural model is derived from docking rather than experimental restraints, and the quantitative impact of IDR deletion on binding affinity is modest. The manuscript would benefit from a more rigorous presentation of the structural data and a clearer discussion of the limitations of the current approach.
- **Who would be interested in the results, and why** Researchers working on SARS-CoV-2 molecular biology, nucleic acid aptamer development, structural biology of viral nucleocapsid proteins, and biophysical characterization of intrinsically disordered regions. The findings may also be relevant to those developing aptamer-based diagnostics or therapeutics targeting the N protein.
- **Major strengths** The study addresses a previously underappreciated region of the N protein, the N-terminal IDR, and provides evidence for its functional role in aptamer binding. The combination of NMR and SPR approaches is complementary and appropriate. The mutagenesis strategy, particularly the use of conserved R-to-K substitutions, is thoughtful and allows for discrimination between direct binding residues and structural determinants. The comparison with previously reported N-NTD structures highlights a meaningful gap in the field.
- **Major Concerns** The structural model of the complex is based on HADDOCK docking rather than experimentally derived restraints, which limits the confidence in the atomic-level details. The reported binding affinities for the truncated constructs show only modest reductions, which may not fully support the claim that the IDR is "critical" for binding. The NMR data presentation is incomplete, and the assignment of arginine side-chain signals relies on a single-point mutant comparison approach that may not be fully unambiguous. The manuscript does not provide a clear quantitative analysis of the chemical shift perturbations or a statistical assessment of the structural model.
- **Minor Comments** The manuscript contains some typographical errors and inconsistent formatting. The methods section for the molecular dynamics simulations is brief and lacks convergence criteria. The discussion would benefit from a more explicit consideration of how the findings relate to the full-length N protein in the context of viral infection.
- **Technical failings that need to be addressed before the case is established** The lack of experimentally derived structural restraints for the complex, the incomplete NMR assignment strategy, and the absence of raw data or deposition of structural coordinates are the primary technical issues that need to be resolved.
- **Assessment against Nature-style criteria** Originality: The focus on the N-terminal IDR in aptamer binding is a novel contribution, as most prior studies used truncated constructs. Scientific importance: The findings have potential implications for understanding N protein function and for aptamer design, but the modest effect sizes and the docking-based model limit the strength of the conclusions. Interdisciplinary readership: The work will appeal to structural biologists, virologists, and aptamer researchers, but the technical presentation may limit broader accessibility. Technical soundness: The experimental design is generally sound, but the structural model lacks experimental validation and the NMR data are not fully presented. Readability for nonspecialists: The manuscript is reasonably well written, but the methods and results sections assume familiarity with NMR spectroscopy and docking approaches.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the structural model and the quantitative interpretation of the binding data.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural model validity
- **Claim pointer** The authors claim to report the "NMR-derived complex structure" of N-NTD with A48, and state that "the flexible N-terminus folds into a β-strand structure upon aptamer binding."
- **Evidence pointer** Section 2.5, Figure 5, Section 4.4
- **Concern** The complex structure is generated using HADDOCK docking followed by MD refinement, not by experimental NMR restraints such as intermolecular NOEs or residual dipolar couplings. The term "NMR-derived" is therefore misleading. The authors do not provide any experimental validation of the docked model, such as intermolecular distance restraints or relaxation data supporting the induced folding of the N-terminus.
- **Why it matters** The central structural claim of the manuscript, that the IDR folds into a β-strand upon binding, is based on a computational model rather than direct experimental evidence. Without experimental restraints, the atomic details of the interface and the conformational change in the IDR remain speculative. This affects the reliability of the proposed binding mechanism and the interpretation of the mutagenesis data.
- **Resolution test** The authors should either provide experimental NMR restraints (e.g., intermolecular NOEs) that support the docked model, or clearly rephrase the claim to indicate that the structure is a computational model guided by NMR chemical shift perturbation data. Deposition of the structural coordinates and validation statistics would also be necessary.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative binding data interpretation
- **Claim pointer** The authors state that "deletion of the N-terminal IDR or substitution of positively charged arginine residues with negatively charged glutamate residues in the IDR region substantially reduced the binding affinity for A48."
- **Evidence pointer** Section 2.2, Section 2.4, Figure 4
- **Concern** The reported Kd values for the truncated constructs are 3.09 nM (Δ25N-NTD) and 5.65 nM (Δ43N-NTD), compared to 0.36 nM for the full-length N-NTD. While these differences are statistically significant, the reductions are only 8.6-fold and 15.7-fold, respectively. The term "substantially reduced" may overstate the magnitude of the effect, particularly given that the Δ25N-NTD construct, which retains the IDR, still shows a 8.6-fold reduction. The authors do not provide a statistical analysis of the SPR data or a discussion of whether the remaining affinity is still in the nanomolar range, which may be sufficient for biological function.
- **Why it matters** The quantitative interpretation of the binding data is central to the claim that the IDR is "critical" for aptamer binding. If the truncated constructs still bind with nanomolar affinity, the functional importance of the IDR may be more nuanced than presented. A more careful statistical and functional analysis is needed to support the strength of the claim.
- **Resolution test** The authors should provide replicate measurements with error bars and statistical tests for the Kd values. They should also discuss the functional relevance of the residual nanomolar affinity in the context of aptamer-based applications.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** NMR assignment completeness
- **Claim pointer** The authors state that "approximately 30 additional residues became detectable in the A48-bound state" and that "residues G30–S51 and T91–K102 showed either newly observed signals or substantial chemical shift changes."
- **Evidence pointer** Section 2.2, Figure 2, Supplementary Figures S2–S3
- **Concern** The manuscript does not provide a complete list of assigned residues in the free and bound states, nor does it show the assignment process for the arginine side-chain signals. The use of single-point R-to-K mutants to assign arginine side chains is indirect and may be ambiguous if the mutations cause conformational changes beyond the local environment. The authors do not report the fraction of residues assigned or the completeness of the backbone and side-chain assignments.
- **Why it matters** The identification of binding epitopes relies on the completeness and accuracy of the NMR assignments. If assignments are incomplete or ambiguous, the interpretation of which residues are involved in binding may be incorrect. This is particularly important for the arginine residues in the IDR, which are central to the main claim.
- **Resolution test** The authors should provide a table of assigned residues with chemical shift values, a description of the assignment strategy, and a discussion of the confidence in the arginine side-chain assignments. If possible, additional experiments such as NOE-based assignments or site-directed labeling should be used to confirm the assignments.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Structural comparison interpretation
- **Claim pointer** The authors state that "comparison of the Δ25N-NTD-A48 complex with previously reported N-NTD-ligand structures revealed distinct binding patterns" and that "A48 primarily binds to the left side of N-NTD."
- **Evidence pointer** Section 2.5, Figure 6
- **Concern** The structural comparison is based on the docked model of the Δ25N-NTD-A48 complex, which has not been experimentally validated. The comparison with previously reported structures (8TFD, 7ACS, 7ACT, 7XWZ) is qualitative and relies on visual inspection of the figures. The authors do not provide quantitative measures of structural similarity or differences, such as RMSD calculations or interface area comparisons.
- **Why it matters** The claim that N-NTD adopts distinct binding modes for different ligands is an important conclusion, but it is based on a model that has not been experimentally verified. A more rigorous quantitative comparison would strengthen the conclusion and provide a clearer basis for understanding the specificity of aptamer recognition.
- **Resolution test** The authors should provide quantitative structural comparisons, such as interface area calculations, RMSD values, and a detailed description of the differences in binding modes. If possible, the docked model should be validated with additional experimental data.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and accuracy of terminology
- **Affected element** Abstract and Section 2.5
- **Evidence pointer** Abstract, Section 2.5
- **Issue** The term "NMR-derived complex structure" is used in the abstract and throughout the manuscript, but the structure is actually a computational model based on HADDOCK docking guided by NMR chemical shift perturbation data. This terminology is misleading and should be corrected.
- **Required correction** Replace "NMR-derived" with "NMR-guided" or "computationally derived with NMR restraints" to accurately describe the methodology.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.4, Figure 4
- **Evidence pointer** Section 2.4, Figure 4
- **Issue** The SPR data are presented without error bars or statistical analysis. The Kd values are reported as single numbers, which does not allow the reader to assess the variability or the significance of the differences between constructs.
- **Required correction** Provide replicate measurements with standard deviations or standard errors, and include statistical tests (e.g., t-tests) to support the claim that the observed differences are significant.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Section 4.4, Section 4.5
- **Evidence pointer** Section 4.4, Section 4.5
- **Issue** The methods for HADDOCK docking and MD simulations are brief and lack important details, such as the number of docking models generated, the scoring function used, the convergence criteria for the MD simulations, and the force field parameters for the DNA aptamer.
- **Required correction** Expand the methods section to include these details to allow reproducibility and to enable the reader to assess the quality of the computational model.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section 3
- **Evidence pointer** Section 3
- **Issue** The discussion does not address the limitations of the study, such as the lack of experimental structural restraints, the modest effect sizes in the binding assays, and the fact that the findings are based on a truncated construct rather than the full-length N protein.
- **Required correction** Add a paragraph discussing the limitations of the study and the implications for the interpretation of the results.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language and formatting
- **Affected element** Throughout the manuscript
- **Evidence pointer** Throughout
- **Issue** The manuscript contains several typographical errors and inconsistent formatting, such as the use of "We" with a capital W in the middle of a sentence in Section 3, and inconsistent use of italics for gene names.
- **Required correction** Carefully proofread the manuscript and correct typographical errors and formatting inconsistencies.

## Risk / unsupported claims
- The claim that the N-terminal IDR "folds into a β-strand structure upon aptamer binding" is not directly supported by experimental data and is based on a computational model.
- The claim that the IDR is "critical" for aptamer binding is based on modest reductions in binding affinity (8.6-fold and 15.7-fold) that may not be functionally significant.
- The claim that the N-NTD-A48 complex structure is "NMR-derived" is misleading, as the structure is a docking model.
- The claim that the findings "may have general implications for understanding how other viral nucleocapsid proteins interact with nucleic acids" is speculative and not directly supported by the data presented.
- The conservation analysis of the N protein across SARS-CoV-2 variants is mentioned but not shown in the manuscript, making this claim unverifiable.