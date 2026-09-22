## Review setup

- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract, with no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present PIONEER2, a computational pipeline integrating 3D structural similarity with geometric deep learning, for predicting binding partner-specific interfacial residues in human protein-protein interactions. They claim performance comparable to AlphaFold3 on PDB test structures, superior performance on low-confidence AlphaFold3 models and on PPIs without PDB structures, and experimental validation via 1,866 mutations tested across 5,010 mutation-interaction pairs. They further claim that PIONEER2-predicted interfaces match PDB structures in predicting disruptive mutations and outperform AlphaFold3 in accounting for population variant depletion and disease mutation enrichment. A comprehensive 3D interactome covering 352,124 binary human PPIs is reported, with a web server implementation.
- **Visible evidence base** Abstract text only. No figures, tables, methods, or supplementary data provided.
- **Missing materials affecting confidence** Full manuscript, all figures and tables, methods description, benchmark details, statistical analyses, experimental validation protocols, and supplementary information are unavailable. The abstract contains no quantitative performance metrics, no confidence intervals, no effect sizes, and no statistical significance values.

## Reviewer

- **Overall assessment** The abstract describes a potentially valuable resource for the human interactome field, with a plausible methodological integration of structural homology and deep learning. The scale of the experimental validation is impressive. However, the abstract alone provides insufficient evidence to evaluate the core claims. Critical details regarding benchmark construction, avoidance of data leakage, definition of the AlphaFold3 comparison set, experimental validation design, and statistical rigor are absent. The claim of superiority over AlphaFold3 for a large fraction of PPIs rests on an indirect inference from ranking scores that requires careful scrutiny. The manuscript may represent a significant contribution, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Structural biologists studying protein-protein interactions, computational biologists developing interface prediction methods, human geneticists interpreting variant pathogenicity, and researchers in personalized medicine would find value in a comprehensive 3D interactome with interface predictions. The experimental validation dataset of 1,866 mutations across 5,010 pairs would be a useful community resource. The web server implementation increases accessibility and practical utility.
- **Major strengths** The integration of structural homology with geometric deep learning is a sensible approach that leverages evolutionary and structural information. The scale of the predicted interactome, covering 352,124 experimentally detected binary PPIs, is comprehensive. The experimental validation effort, with 1,866 mutations tested across 5,010 pairs, is substantial and goes beyond typical computational benchmarks. The comparison to AlphaFold3 addresses a timely and relevant question. The web server implementation enhances the translational potential of the work.
- **Major Concerns** The concerns below identify specific issues that prevent the core claims from being established from the abstract alone.
- **Minor Comments** The minor comments note presentation and clarity issues that should be addressed in a full revision.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: The combination of structural homology with geometric deep learning for interface prediction is not entirely novel, as both approaches have been explored separately, but the integration and the scale of application to the human interactome may offer a new contribution. Scientific importance: The potential to provide interface predictions for the vast majority of human PPIs lacking structural data is scientifically important, particularly for variant interpretation and disease research. Interdisciplinary readership: The work bridges structural biology, machine learning, and human genetics, which would appeal to a broad readership. Technical soundness: Cannot be adequately assessed from the abstract. The absence of methodological details, benchmark descriptions, and statistical analyses prevents evaluation of technical rigor. Readability for nonspecialists: The abstract is generally readable, but terms such as "AlphaFold3 ranking scores" and "geometric deep learning" are used without sufficient explanation for a general audience. The claim structure is clear, but the evidentiary basis is not.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Benchmark validity
- **Claim pointer** The authors claim that PIONEER2 and AlphaFold3 show "quite similar" performance on a test set of PDB structures, and that PIONEER2 outperforms AlphaFold3 for complexes with AlphaFold3 ranking scores below 0.5.
- **Evidence pointer** Abstract, performance comparison section. Location not provided.
- **Concern** The abstract provides no details on the composition of the PDB test set, including how complexes were selected, whether redundancy with training data was controlled, how sequence identity thresholds were applied, and whether the test set spans diverse complex types and difficulty levels. The threshold of 0.5 for AlphaFold3 ranking scores is introduced without justification, and the claim of "quite similar" performance is not supported by any quantitative metrics such as precision, recall, AUC, or Matthews correlation coefficient.
- **Why it matters** Without a clearly defined and appropriately constructed benchmark, the performance comparison cannot be interpreted. Data leakage from training on homologous structures would inflate PIONEER2 performance. The choice of the 0.5 ranking score threshold directly determines the subset where PIONEER2 is claimed to be superior, and this threshold may not correspond to a meaningful confidence boundary.
- **Resolution test** Provide a detailed description of the test set construction, including redundancy removal procedures, sequence identity thresholds, and complex type distribution. Report quantitative performance metrics with confidence intervals for both methods across the full test set and for the subset with AlphaFold3 ranking scores below 0.5. Justify the 0.5 threshold with reference to calibration analyses.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that PIONEER2-predicted interfaces are "comparable to PDB structures" in predicting disruptive mutations, while AlphaFold3 performance is reduced, and that PIONEER2 outperforms AlphaFold3 in accounting for population variant depletion and disease mutation enrichment.
- **Evidence pointer** Abstract, experimental validation and variant analysis sections. Location not provided.
- **Concern** No statistical measures are reported for the experimental validation. There are no effect sizes, confidence intervals, p-values, or measures of predictive power such as area under the ROC curve. The comparison between PIONEER2, PDB structures, and AlphaFold3 is stated qualitatively without any indication of whether differences are statistically significant. The number of mutations and pairs is large, which suggests adequate power, but the results are not quantified.
- **Why it matters** The central claim of the paper is that PIONEER2 provides accurate interface predictions that are useful for variant interpretation. Without statistical evidence, the reader cannot assess whether the observed differences are meaningful or within noise. The claim of "comparable" performance to PDB structures requires equivalence testing or at least a demonstration that differences are not significant.
- **Resolution test** Report quantitative performance metrics for the mutation prediction task, including sensitivity, specificity, and AUC, with confidence intervals. Provide statistical tests comparing PIONEER2 to PDB structures and to AlphaFold3, including appropriate corrections for multiple testing. For the variant depletion and disease enrichment analyses, report odds ratios, enrichment scores, and significance levels.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of AlphaFold3 comparison
- **Claim pointer** The authors claim that approximately half of AlphaFold3 ranking scores for high-confidence PPIs not associated with PDB structures are below 0.5, indicating that PIONEER2 offers superior interface prediction for a large number of PPIs without available structures.
- **Evidence pointer** Abstract, AlphaFold3 comparison section. Location not provided.
- **Concern** The inference that low AlphaFold3 ranking scores imply superior PIONEER2 performance is indirect and not validated. The abstract does not establish that AlphaFold3 ranking scores correlate with interface prediction accuracy in the way the authors assume. The set of "high-confidence PPIs not associated with a PDB structure" is not defined, and the source of these PPIs is not specified. The claim that PIONEER2 is superior for these cases is an extrapolation from the PDB test set results, which may not transfer to non-PDB complexes.
- **Why it matters** The claim of broad superiority over AlphaFold3 for the majority of the human interactome is a major conclusion of the paper. If this inference is not directly validated, the claim is unsupported. The absence of structural ground truth for non-PDB PPIs makes direct validation challenging, but the authors should provide indirect evidence or clearly acknowledge the limitation.
- **Resolution Test** Provide a direct validation of PIONEER2 on a set of complexes where AlphaFold3 ranking scores are low but where some structural or experimental information is available. Alternatively, demonstrate a strong correlation between AlphaFold3 ranking scores and interface prediction accuracy on a held-out set, justifying the use of the 0.5 threshold as a proxy for PIONEER2 superiority.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation design
- **Claim pointer** The authors claim experimental validation by generating 1,866 mutations and testing their disruptive impact on 5,010 mutation-interaction pairs, with PIONEER2-predicted interfaces comparable to PDB structures in predicting disruptive mutations.
- **Evidence pointer** Abstract, experimental validation section. Location not provided.
- **Concern** The abstract provides no information on the experimental assay used, the selection criteria for mutations, the definition of "disruptive impact," the thresholds for calling a mutation disruptive, or the controls used. The relationship between the 1,866 mutations and the 5,010 pairs is unclear, as one mutation may be tested against multiple interaction partners. The possibility of ascertainment bias in mutation selection is not addressed.
- **Why it matters** The experimental validation is a key strength of the paper, but without details on the assay design and analysis, the results cannot be interpreted. Biases in mutation selection or assay conditions could substantially affect the conclusions. The comparison to PDB structures as a gold standard requires that the PDB structures used are of sufficient quality and that the interface definitions are consistent.
- **Resolution Test** Describe the experimental assay, mutation selection criteria, and analysis pipeline in detail. Provide information on assay reproducibility, controls, and how disruptive mutations were defined. Clarify the relationship between mutations and interaction pairs. Demonstrate that the results are robust to variations in thresholds and analysis choices.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors claim that PIONEER2 integrates 3D structural similarity with geometric deep learning to predict binding partner-specific interfacial residues.
- **Evidence pointer** Abstract, methods description. Location not provided.
- **Concern** The abstract provides no description of the PIONEER2 architecture, training data, feature representation, or how structural similarity is incorporated. There is no information on how binding partner specificity is encoded, how the model handles multi-chain complexes, or how the training set was constructed. The relationship to the earlier PIONEER method, if any, is not stated.
- **Why it matters** Reproducibility is a core requirement for computational methods. Without a clear description of the method, other researchers cannot apply or build upon the work. The novelty of the approach relative to existing methods cannot be assessed.
- **Resolution Test** Provide a complete description of the PIONEER2 architecture, training procedure, and feature engineering in the full manuscript. Include details on data sources, preprocessing, and hyperparameter selection. State clearly what is new relative to prior work.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, first sentence
- **Evidence pointer** Abstract, opening sentence. Location not provided.
- **Issue** The first sentence contains a grammatical error. "however" is used as a conjunctive adverb but is not properly punctuated, creating a run-on structure.
- **Required correction** Revise to "A significant portion of disease-causing mutations occur at protein-protein interfaces. However, the number of structurally resolved multi-protein complexes is extremely small."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, AlphaFold3 ranking scores
- **Evidence pointer** Abstract, performance comparison section. Location not provided.
- **Issue** The term "AlphaFold3 ranking scores" is used without definition. It is unclear whether this refers to the predicted template modeling score, the interface pTM, or another confidence metric.
- **Required correction** Define the specific AlphaFold3 confidence metric used and cite the relevant documentation or publication.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Resource availability
- **Affected element** Abstract, web server
- **Evidence pointer** Abstract, final sentence. Location not provided.
- **Issue** The web server URL is provided, but there is no statement about data availability for the full interactome predictions or the experimental validation dataset.
- **Required correction** State where the full prediction dataset and experimental validation data will be deposited, with accession numbers or persistent identifiers.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Abstract, PIONEER2 naming
- **Evidence pointer** Abstract, methods description. Location not provided.
- **Issue** The name "PIONEER2" implies a prior version, but no reference to the original PIONEER method is provided in the abstract.
- **Required correction** Cite the original PIONEER publication and briefly state what PIONEER2 adds.

## Risk / unsupported claims

- The claim that PIONEER2 outperforms AlphaFold3 for approximately half of high-confidence PPIs without PDB structures is unsupported. This is an indirect inference from AlphaFold3 ranking scores, and the abstract provides no direct validation on non-PDB complexes.
- The claim that PIONEER2-predicted interfaces are "comparable to PDB structures" in predicting disruptive mutations is unsupported. No quantitative comparison or statistical test is reported.
- The claim that PIONEER2 outperforms AlphaFold3 in accounting for depletion of common variants and enrichment of disease mutations is unsupported. No effect sizes or significance values are provided.
- The overall performance comparison between PIONEER2 and AlphaFold3 on the PDB test set is unquantified. The statement "quite similar" cannot be evaluated without metrics.
- The comprehensiveness of the 3D interactome covering 352,124 PPIs is not verifiable from the abstract. The source of these PPIs and the criteria for inclusion are not described.
- The experimental validation results are not interpretable without details on the assay, mutation selection, and analysis. The claim of validation is therefore not assessable.