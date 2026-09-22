## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, conclusions, methods, and figure legends
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and presentation quality of the described method IDBindT5 for predicting binding residues in disordered protein regions
- **Shared manuscript claim summary** The authors present IDBindT5, a machine learning model using ProtT5 protein language model embeddings and disorder annotations to predict binding residues in intrinsically disordered regions. They claim state-of-the-art performance comparable to ANCHOR2 and DeepDISOBind, with substantially faster runtime, and demonstrate robustness to predicted disorder input.
- **Visible evidence base** Main text figures (Figs. 1-3), supplementary tables and figures referenced (SOM_T1-T8, SOM_F1-F8), performance metrics with confidence intervals, runtime comparisons, and benchmark evaluations on Mobi195 and CAID2 datasets
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided in the submitted material; detailed hyperparameter search results; per-protein performance distributions; exact statistical test outputs beyond reported p-values; code or model weights for independent verification

## Reviewer
- **Overall assessment** The manuscript presents a useful and practical contribution to the field of binding residue prediction in disordered proteins. The methodological approach is sound, the comparisons are appropriately cautious, and the runtime advantage is clearly demonstrated. However, the claimed equivalence to state-of-the-art methods rests on statistical comparisons with overlapping confidence intervals, which the authors themselves acknowledge as inconclusive. The practical utility is evident, but the scientific advance over existing methods is incremental rather than transformative. The manuscript would benefit from clearer reporting of limitations and a more critical interpretation of the performance equivalence claims.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins and their interaction networks would find this method useful for prioritizing experimental validation. Computational biologists developing prediction tools for protein function would be interested in the demonstration that protein language model embeddings can replace evolutionary information in this specific task. Additionally, the broader community studying molecular recognition features and protein-protein interactions may adopt this tool for large-scale proteome analyses given its speed advantage.

- **Major Strengths**
  1. The method addresses a genuine gap: binding residue prediction specifically in disordered regions, where traditional methods often fail
  2. The runtime advantage is substantial and practically meaningful, enabling proteome-wide applications
  3. The ablation study on disorder input provides useful insight into feature importance
  4. The authors appropriately restrict evaluation to disordered regions, avoiding the confounding issue of distinguishing order from disorder
  5. The use of a simple feedforward architecture is a deliberate and well-justified choice that reduces overfitting risk

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical validity of performance equivalence claims
- **Claim pointer** The abstract and results state that IDBindT5 "did not differ at the 95% CI from the state-of-the-art (SOTA) methods ANCHOR2 and DeepDISOBind" and that IDBindT5 "reached SOTA"
- **Evidence pointer** Figure 2, Supplementary Table SOM_T4, Results section "IDBindT5 reached SOTA"
- **Concern** The claim of state-of-the-art performance is based on overlapping confidence intervals, which the authors themselves note is not evidence of equivalence. The text states "no method stood out in a Welch test" but this is a statement about lack of detected difference, not demonstrated equivalence. The conclusion that IDBindT5 "reached similar levels" as SOTA methods is an overinterpretation of the statistical evidence presented. The authors need to either provide equivalence testing or clearly reframe their claims as "not significantly worse" rather than "reached SOTA."
- **Why it matters** The central claim of the paper is that IDBindT5 achieves state-of-the-art performance. If this claim is not statistically supported, the contribution reduces to a speed optimization of existing capability, which is a different and lesser claim. Readers may adopt this method based on the performance equivalence claim, and the statistical basis for that adoption must be sound.
- **Resolution test** Provide equivalence testing (e.g., TOST procedure) with predefined equivalence bounds, or reframe all claims to "not significantly different from SOTA" and adjust the abstract, results, and conclusions accordingly. If equivalence cannot be demonstrated, the authors should explicitly acknowledge that IDBindT5 may be slightly worse in predictive performance but offers substantial speed advantages.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of findings beyond the test set
- **Claim pointer** The manuscript claims IDBindT5 provides "accurate and fast SOTA per-residue binding predictions in disordered regions" and that it "maintains SOTA performance with predicted disorder as input"
- **Evidence pointer** Figure 3, CAID2 benchmark section, Results section "IDBindT5 performance with predicted disorder data remains high"
- **Concern** The CAID2 benchmark evaluation is based on only 78 proteins, and the authors note that "none of the SOTA methods consistently improved over the random baseline at levels that were statistically significant" on this benchmark. This raises questions about the informativeness of the CAID2 comparison. Additionally, the Mobi195 test set, while larger, was derived from the same source database (MobiDB) used for training, and the redundancy reduction procedures, while careful, cannot fully eliminate potential biases. The generalizability of the performance claims to diverse protein families and interaction types remains uncertain.
- **Why it matters** The practical value of the method depends on its performance across the diverse range of disordered proteins found in real applications. If the evaluation benchmarks are too small or too similar to the training distribution, the reported performance may not translate to broader use cases.
- **Resolution test** Provide additional validation on independent datasets not derived from MobiDB, or clearly discuss the limitations of the current benchmarks and temper the generalizability claims accordingly. If additional datasets are not available, the authors should explicitly acknowledge this limitation in the discussion.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of method description for reproducibility
- **Claim pointer** The methods section states that "We systematically combined the following architectures and parameters, creating different models" and describes the final model architecture
- **Evidence pointer** Methods section "Prediction methods", Supplementary Table SOM_T2
- **Concern** While the final model architecture is described, the full hyperparameter search space is not detailed in the main text. The criteria for selecting the final model from the validation set are described qualitatively ("two tied for best performance") but the specific metric used for this determination is not stated. Additionally, the threshold selection procedure is described but the relationship between the per-fold thresholds and the final model's threshold is unclear. The manuscript would benefit from a complete description of the hyperparameter grid, the selection metric, and the threshold optimization procedure.
- **Why it matters** Reproducibility is a core requirement for computational methods. Without complete details of the model selection process, independent researchers cannot fully replicate the method or assess potential overfitting to the validation set.
- **Resolution test** Provide a complete description of the hyperparameter search space, the exact selection criterion, and the threshold optimization procedure in the main text or supplementary materials. If this information is already in the supplementary materials, the authors should reference it more explicitly in the main text.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of statistical reporting
- **Affected element** Results section "IDBindT5 reached SOTA"
- **Evidence pointer** Figure 2, Supplementary Table SOM_T4
- **Issue** The manuscript reports confidence intervals for performance metrics but does not consistently report the exact p-values from the Welch tests. The statement "no method stood out in a Welch test" is vague.
- **Required correction** Report the specific p-values for all pairwise comparisons in the supplementary materials, and state the significance threshold used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Interpretation of ablation study
- **Affected element** Results section "IDBindT5 performance with predicted disorder data remains high"
- **Evidence pointer** Supplementary Table SOM_T5
- **Issue** The ablation study shows that using predicted disorder labels reduces recall significantly but other metrics remain within confidence intervals. The authors interpret this as "surprisingly stable" performance, but the recall drop could be practically important depending on the application.
- **Required correction** Discuss the practical implications of the recall drop when using predicted disorder, and consider whether users should be cautioned about this trade-off.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity of runtime comparison
- **Affected element** Results section "IDBindT5 good and fastest"
- **Evidence pointer** Supplementary Table SOM_T8
- **Issue** The runtime comparison is presented as a single measurement on a specific hardware configuration. The manuscript does not discuss how runtime scales with protein length or whether the comparison is fair in terms of implementation optimization.
- **Required correction** Provide runtime scaling information or at least acknowledge that the comparison reflects specific implementations and hardware conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of model availability
- **Affected element** Data availability statement
- **Evidence pointer** Abstract, Conclusions
- **Issue** The model is stated to be publicly available at a GitHub repository, but the manuscript does not specify the license, the programming language dependencies, or whether trained model weights are included.
- **Required correction** Provide a brief description of the repository contents, including the license, in the data availability section.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Abstract, Introduction, Results
- **Issue** The terms "binding residues," "binding regions," and "binding sites" are used somewhat interchangeably. While this is common in the field, the manuscript could benefit from consistent terminology, particularly when distinguishing between residue-level and region-level predictions.
- **Required correction** Define the terms at first use and use them consistently throughout the manuscript.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The statistical basis for the "reached SOTA" claim must be strengthened through equivalence testing or reframed as "not significantly worse"
  - R1-M2: The generalizability of performance claims requires either additional independent validation or explicit acknowledgment of benchmark limitations
  - R1-M3: The model selection and threshold optimization procedures must be described completely for reproducibility

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The application of protein language model embeddings to binding residue prediction in disordered regions is a reasonable incremental step, building on prior work demonstrating the utility of pLM embeddings for binding prediction in general. The specific focus on disordered regions and the systematic comparison of pLM choices adds some novelty, but the approach is not conceptually transformative.
  - **Scientific importance**: Moderate. The method addresses a real need in the field, as binding prediction in disordered regions is challenging and existing tools have limitations. However, the performance improvement over existing methods is not clearly established, and the primary advantage appears to be computational speed rather than predictive accuracy.
  - **Interdisciplinary readership**: Limited. The manuscript will primarily interest computational biologists and researchers working on intrinsically disordered proteins. The methods and results are presented in a way that is accessible to these audiences, but the broader significance for structural biology or molecular biology is not strongly articulated.
  - **Technical soundness**: Generally sound with caveats. The experimental design is reasonable, the redundancy reduction procedures are careful, and the comparisons are appropriately cautious. However, the statistical interpretation of performance equivalence is problematic, and the completeness of the method description for reproducibility is insufficient.
  - **Readability for nonspecialists**: Adequate. The manuscript is clearly written and the figures are informative. The abstract effectively summarizes the key findings. However, the statistical nuances of the performance comparisons may be difficult for nonspecialists to interpret correctly.

- **Recommendation posture** Supportive if technical concerns are resolved. The method has clear practical utility, particularly for large-scale applications where runtime is a limiting factor. The manuscript addresses a relevant problem and the approach is reasonable. However, the statistical claims of performance equivalence must be either strengthened or appropriately qualified, and the method description must be completed for reproducibility. Once these issues are addressed, the manuscript would be a solid contribution to the field.