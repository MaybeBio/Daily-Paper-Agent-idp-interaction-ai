## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no methods, figures, tables, or supplementary materials were provided
- **Shared manuscript claim summary** The authors present a computational pipeline (LIR-DP) that integrates sequence pattern matching, IUPred3 disorder prediction, and AlphaFold3 modeling to identify putative LC3-interacting region (LIR) motifs in proteins from highly virulent viruses (HVVs). They report 43 putative LIRs across 166 proteins from 22 HVVs, predict 18 as functional, and validate four LIRs experimentally (Marburg virus nucleoprotein, Nipah virus phosphoprotein, Ebola virus VP35, Rift Valley fever virus NSs) as binding Atg8/LC3 family proteins, with the aromatic residue at position one being critical.
- **Visible evidence base** Abstract text only; no experimental data, statistical analyses, sequence alignments, structural models, or methodological details are available
- **Missing materials affecting confidence** Full methods, all experimental data (binding assays, mutagenesis results), computational pipeline details, validation metrics, sequence lists, structural models, and any negative or control results

## Reviewer
- **Overall assessment** The abstract describes a potentially useful integrative approach for identifying LIR motifs in viral proteins, and the combination of computational prediction with experimental validation is commendable. However, the evidence base available for review is limited to the abstract, which precludes rigorous assessment of methodological soundness, data quality, and the strength of the central claims. The reported numbers (43 putative, 18 predicted functional, 4 validated) suggest a substantial attrition that is not explained. The claim that the aromatic residue is critical is presented without supporting data. The broader claim that LIR-DP provides insight into HVV modulation of autophagy is plausible but not established from the supplied material.
- **Who would be interested in the results, and why** Virologists studying host-pathogen interactions, particularly those focused on hemorrhagic fever viruses and Nipah virus; autophagy researchers interested in viral subversion of cellular pathways; and computational biologists developing SLiM prediction tools. The pipeline could be of practical use to laboratories studying viral evasion of autophagy, and the specific validated LIRs may inform mechanistic studies of viral replication.
- **Major strengths** The integration of three distinct computational approaches (sequence pattern matching, disorder prediction, structural modeling) is a sensible strategy for SLiM discovery. The inclusion of experimental validation for a subset of predictions strengthens the credibility of the pipeline. The focus on highly virulent viruses with pandemic potential addresses an important biomedical gap. The identification of a critical aromatic residue is mechanistically consistent with known LIR biology.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** The abstract does not provide sufficient detail to evaluate the false positive rate of the pipeline, the criteria for classifying a LIR as "functional," the experimental methods used for binding validation, or the statistical significance of the results. Without these, the central claim that LIR-DP reliably identifies functional LIRs is not established.
- **Assessment against Nature-style criteria** 
  - Originality: The combination of tools is somewhat novel, though each component is established. The application to HVVs is a useful extension.
  - Scientific importance: Potentially high for virology and autophagy fields, but the significance depends on whether the identified LIRs have demonstrated functional relevance during infection, which is not shown.
  - Interdisciplinary readership: The work bridges virology, cell biology, and computational biology, which could attract a broad audience if the evidence is compelling.
  - Technical soundness: Cannot be assessed from the abstract alone. The lack of methodological detail and validation metrics is a major limitation.
  - Readability for nonspecialists: The abstract is clearly written and accessible, with appropriate context for the autophagy and LIR concepts.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a promising approach and preliminary validation, but the absence of methods and data prevents a supportive recommendation. A full manuscript with detailed methods, comprehensive results, and appropriate controls would be required to assess whether the claims are supported.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that LIR-DP identified 43 putative LIR motifs in 166 proteins from 22 HVVs and predicted 18 as functional.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract provides no information on the sensitivity, specificity, or false discovery rate of the pipeline. The criteria for classifying a motif as "putative" versus "functional" are not defined. The attrition from 43 putative to 18 predicted functional to 4 validated is not explained, and it is unclear whether the 18 predictions represent a statistically enriched set or simply a threshold-based selection.
- **Why it matters** Without performance metrics and clear classification criteria, the reader cannot judge whether the pipeline offers an improvement over existing LIR prediction methods or whether the 43 identified motifs are meaningful or largely false positives. The core utility claim of the pipeline depends on its reliability.
- **Resolution test** Provide precision and recall estimates against a known LIR dataset, define the scoring thresholds for "putative" and "functional" classifications, and report the number of predictions that failed experimental validation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that LIRs from Marburg virus nucleoprotein, Nipah virus phosphoprotein, Ebola virus VP35, and Rift Valley fever virus NSs bind to Atg8/LC3 family proteins, and that the aromatic amino acid at position one is critical.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The experimental methods used to demonstrate binding are not described. It is unclear whether binding was shown by co-immunoprecipitation, pull-down, fluorescence polarization, isothermal titration calorimetry, or another method. The mutagenesis data supporting the critical role of the aromatic residue are not shown. No quantitative binding affinities or statistical comparisons are provided.
- **Why it matters** The experimental validation is the strongest evidence for the pipeline's utility. Without details on the assays, controls, and quantitative results, the binding claims cannot be evaluated. The claim that the aromatic residue is critical requires mutagenesis data with appropriate controls.
- **Resolution test** Describe the binding assays in full, provide representative data with positive and negative controls, report quantitative binding measurements where applicable, and show mutagenesis results for the aromatic residue and at least one control residue.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scope of claim
- **Claim pointer** The authors state that the presence of LIR motifs in viral components suggests a role in hijacking or evading the host autophagy pathway, and that LIR-DP may provide insight into the mechanism by which HVVs modulate autophagy during infection.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract does not present any functional data demonstrating that the identified LIRs affect autophagy during viral infection. Binding to Atg8/LC3 proteins in vitro or in cellulo does not establish that these interactions are biologically relevant in the context of infection.
- **Why it matters** The broader significance of the work depends on whether the identified LIRs contribute to viral modulation of autophagy. Without infection-based experiments, the physiological relevance of the identified interactions remains speculative.
- **Resolution test** Include experiments showing that mutation of the identified LIRs in the context of viral infection alters autophagy flux, viral replication, or both.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of HVV
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract refers to "highly virulent viruses" and lists hemorrhagic fever viruses and Nipah virus as examples, but the inclusion criteria for the 22 viruses analyzed are not stated.
- **Required correction** Specify the list of viruses analyzed and the criteria for inclusion.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Negative results
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract reports 4 validated LIRs but does not mention how many of the 18 predicted functional LIRs failed validation or why.
- **Required correction** Report the number of predictions tested and the outcomes, including failures, to allow assessment of the pipeline's positive predictive value.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** AlphaFold3 usage
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that AlphaFold3 was used for modeling but does not describe how the models were used to assess LIR functionality.
- **Required correction** Briefly describe the role of structural modeling in the pipeline, such as whether models were used to assess accessibility or binding compatibility.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Pipeline applicability
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not discuss whether LIR-DP is applicable to non-viral proteins or to other SLiM types.
- **Required correction** Add a brief statement on the generalizability of the pipeline beyond HVV proteins.

## Risk / unsupported claims
- The claim that 18 of 43 LIRs are "predicted functional" is unsupported without defined prediction criteria and validation data.
- The claim that the aromatic residue at position one is critical for binding is unsupported without mutagenesis data.
- The claim that LIR-DP provides insight into how HVVs modulate autophagy during infection is unsupported without infection-based functional experiments.
- The overall utility of LIR-DP as a discovery pipeline cannot be assessed without performance metrics and comparison to existing methods.