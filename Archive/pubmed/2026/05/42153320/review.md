## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, conclusion, methods) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to provided evidence, and suitability for a high-impact generalist audience
- **Shared manuscript claim summary** The authors present MuFGPS, a machine learning framework that integrates sequence-derived physicochemical features, DSSP-annotated secondary structure, and graph-based structural embeddings from AlphaFold-predicted contact maps via a multi-head Graph Attention Network, with SMOTE oversampling and a stacking ensemble of Random Forest, XGBoost, and LightGBM, to predict liquid-liquid phase separation (LLPS) proteins. They report superior performance over six existing methods across all metrics, with ablation analyses supporting the contribution of structural features and ensemble learning.
- **Visible evidence base** Text descriptions of results including performance metrics (accuracy, precision, recall, F1-score, MCC, AUROC, AUPRC), ablation study outcomes, dataset construction details, and methodological descriptions. Figures and tables referenced but not visible. Supplementary materials referenced but not provided.
- **Missing materials affecting confidence** All figures (Figs 1-5), Table 1, Supplementary Tables S1-S2, the full dataset, code repository contents, and detailed hyperparameter settings. The exact performance values for baseline comparisons are only partially reported in text.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant problem in computational biology, namely the prediction of LLPS proteins, and proposes a reasonable multi-level feature integration strategy. The core idea of combining sequence features with AlphaFold-derived structural embeddings is timely and potentially useful. However, the current evidence base is insufficient to fully evaluate the claims. Key methodological details are missing, the comparison with baselines is not fully transparent, and the reported performance gains, while positive, are modest. The manuscript would benefit from clearer reporting of experimental setup, statistical rigor, and a more critical discussion of limitations.

- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics working on protein function prediction, particularly those focused on phase separation, intrinsically disordered proteins, and machine learning applications in structural biology. The integration of AlphaFold structures with graph neural networks is of general interest to the protein language model and structure prediction community. The method could also be relevant to experimental biologists studying LLPS who seek computational prioritization tools.

- **Major strengths**
  1. The problem is well-motivated and clinically relevant, given the link between LLPS dysregulation and neurodegenerative diseases.
  2. The integration of multiple feature levels (sequence, secondary structure, graph-based structural embeddings) is a sensible and potentially powerful approach.
  3. The use of AlphaFold-predicted structures is timely and leverages a widely available resource.
  4. The ablation study design is appropriate for isolating the contribution of individual components.
  5. The authors address class imbalance explicitly with SMOTE, which is a known issue in this domain.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "MuFGPS achieves superior performance across all metrics, with notable gains in F1-score and MCC" and "Benchmarks against six representative methods demonstrate that MuFGPS achieves superior performance across all metrics"
- **Evidence pointer** Table 1 (not visible), Results section "Comparative performance analysis"
- **Concern** The full comparison table is not visible, and the text only provides partial information. The reported accuracy improvement over the second-best method (MambaPhase) is only ~0.8%, which is small. The claim of "superior performance across all metrics" cannot be fully verified without seeing the complete table, including confidence intervals or variance measures across cross-validation folds. Additionally, the statistical test reported (paired one-sided Wilcoxon signed-rank test) is described as yielding "minimal attainable exact P-value" because MuFGPS outperformed baselines in all five folds, but this is a weak statement. With only five folds, the minimum possible p-value for a one-sided test is 1/32 = 0.03125, which is not highly significant. The authors should report effect sizes and confidence intervals.
- **Why it matters** The central claim of the paper is that MuFGPS outperforms existing methods. Without full transparency on the comparison, including variance and statistical significance, this claim is not established. A 0.8% accuracy gain may not be practically meaningful, and the lack of confidence intervals prevents assessment of whether the difference is robust.
- **Resolution test** Provide the full Table 1 with all metrics for all methods, including standard deviations or confidence intervals across folds. Report exact p-values from the Wilcoxon test and consider additional statistical tests (e.g., McNemar's test for paired classification). Discuss whether the observed improvements are practically significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "Class imbalance is addressed using Synthetic Minority Oversampling Technique (SMOTE)" and "SMOTE-based positive protein feature sample generation" section
- **Evidence pointer** Methods section "Stacking-based ensemble classification model", Results section "SMOTE-based positive protein feature sample generation"
- **Concern** The application of SMOTE is described, but critical details are missing. Specifically, it is unclear whether SMOTE is applied only to the training set within each cross-validation fold (which is correct practice) or to the entire dataset before splitting (which would cause data leakage). The text states "SMOTE over-sampling was performed exclusively within the training subset of each cross-validation fold after feature concatenation," which is correct, but the description of the t-SNE visualization in Fig 3 is not sufficient to demonstrate that the synthetic samples are realistic. More importantly, the authors do not report the degree of class imbalance (ratio of positive to negative samples) or the amount of oversampling applied. The claim that SMOTE "effectively alleviates the class imbalance issue" is not quantitatively supported.
- **Why it matters** Data leakage in oversampling is a common pitfall that inflates performance estimates. While the authors appear to have applied SMOTE correctly, the lack of detail on the imbalance ratio and oversampling factor makes it difficult to assess the robustness of the approach. The t-SNE visualization alone does not validate the quality of synthetic samples.
- **Resolution test** Report the class distribution in the dataset, the SMOTE parameters (e.g., sampling strategy, number of nearest neighbors), and provide quantitative evidence that SMOTE improves performance beyond simple class weighting or no oversampling. Clarify that no synthetic samples appear in the test set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "graph-based structural embeddings from AlphaFold residue contact maps via a multi-head Graph Attention Network" and "The GAT encoder is first pretrained in a self-supervised manner within each cross-validation training fold"
- **Evidence pointer** Methods section "Structural representation from residue contact maps"
- **Concern** The description of the GAT architecture and its pretraining is incomplete. The equations for the attention mechanism are referenced but not shown in the text provided. The pretraining procedure uses contrastive learning with random edge dropout and node feature masking, but the authors do not specify the batch size, number of negative samples, temperature parameter in NT-Xent loss, or how the pretrained GAT is integrated with the downstream classification. The claim that pretraining improves robustness is not directly tested; the ablation study removes the GAT entirely but does not compare pretrained vs. non-pretrained GAT. Additionally, the choice of SeqVec over other embeddings (e.g., ESM) is not justified beyond a brief comparison with ProtBERT.
- **Why it matters** The GAT component is a central novelty of the method. Without full architectural details and a direct test of the pretraining contribution, the technical soundness of this component cannot be assessed. The comparison with ProtBERT is useful but does not address whether pretraining itself is beneficial.
- **Resolution test** Provide the full GAT architecture (number of layers, hidden dimensions, attention heads, dropout rates), the pretraining details (batch size, epochs, temperature, augmentation parameters), and an ablation comparing pretrained vs. randomly initialized GAT. Justify the choice of SeqVec over other embeddings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "MuFGPS offers a scalable and high-accuracy framework for proteome-wide LLPS protein prediction"
- **Evidence pointer** Dataset construction section, Conclusion
- **Concern** The dataset construction is described, but the total number of positive samples (366) is relatively small, and the negative set (1302) is derived from only 10 species. The authors do not report the species composition of the positive set or the potential for species bias. The claim of "proteome-wide" applicability is not supported by the evaluation, which appears to be on a single benchmark dataset. No external validation on independent datasets (e.g., recently published LLPS proteins not in the training set) is reported. The extra test set of 29 positive and 124 negative samples is mentioned but its results are not described in the text.
- **Why it matters** For a prediction tool to be broadly useful, it must generalize beyond the training distribution. The small positive set and limited species diversity raise concerns about generalizability. The claim of proteome-wide scalability is not demonstrated.
- **Resolution test** Report the species distribution of the positive and negative sets. Perform external validation on an independent dataset not used in training. Discuss potential biases and limitations of the dataset. If proteome-wide prediction is claimed, provide a demonstration on a large-scale proteome.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "Ablation analyses confirm the synergistic contributions of structural features and ensemble learning to accuracy and robustness"
- **Evidence pointer** Results section "Ablation study"
- **Concern** The ablation study is described in text but the actual results (Fig 5) are not visible. The text reports that removing structural features decreases performance, but the magnitude of the decrease and the statistical significance are not reported. The comparison between No-Struct-No-Ensemble and RF shows that structural features alone contribute substantially, but the incremental contribution of the ensemble over a single classifier is not clearly quantified. The claim of "synergistic contributions" is not supported by the described analysis, which appears to be additive rather than synergistic.
- **Why it matters** The ablation study is critical for understanding which components of the method are essential. Without seeing the actual numbers and statistical tests, the claim of synergy is not established. The term "synergistic" implies an interaction effect, which would require a factorial design with interaction testing.
- **Resolution test** Provide the full ablation results with all metrics and statistical comparisons. If synergy is claimed, perform a formal interaction test or demonstrate that the combined model outperforms the sum of individual contributions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The introduction provides a good overview of LLPS biology but could benefit from a clearer statement of the specific gap in existing computational methods. The transition from "existing methods rely on sequence features" to "we integrate structural information" is logical but could be more explicit about what structural information adds beyond sequence.
- **Required correction** Add one or two sentences explicitly stating what types of structural information are currently missing from existing predictors and why this information is expected to improve prediction.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, dataset construction
- **Evidence pointer** Dataset construction section
- **Issue** The negative set is described as "proteins not recorded or reported to exhibit phase separation tendencies." This is a weak negative definition, as absence of evidence is not evidence of absence. Some proteins in the negative set may be false negatives.
- **Required correction** Acknowledge this limitation explicitly and discuss its potential impact on model evaluation. Consider using a more stringent negative set (e.g., proteins experimentally shown not to phase separate, if available).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, sequence feature extraction
- **Evidence pointer** Methods section "Sequence features extraction"
- **Issue** The text lists several tools used for feature extraction (ESpritz, SEG, LocalCIDER, PLAAC, PScore, catGRANULE, Protein-sol) but does not specify the exact features derived from each tool or the total dimensionality of the sequence feature vector.
- **Required correction** Provide a table or list of all features with their dimensions and the tools used to compute them.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, ensemble model
- **Evidence pointer** Methods section "Stacking-based ensemble classification model"
- **Issue** The hyperparameters for Random Forest, XGBoost, and LightGBM are not reported. The text states that logistic regression is used as the meta-learner but does not specify the regularization parameter or whether cross-validation is used for hyperparameter tuning.
- **Required correction** Report all hyperparameters for the base learners and the meta-learner, and describe the hyperparameter tuning procedure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Results, comparative analysis
- **Evidence pointer** Results section "Comparative performance analysis"
- **Issue** The text mentions "six representative LLPS prediction methods" but does not briefly describe what these methods are or their underlying approaches. Readers unfamiliar with the field may not understand the significance of the comparison.
- **Required correction** Add a brief description of each baseline method (e.g., "catGRANULE uses a weighted scoring system based on disorder and RNA-binding propensity") in the text or in a table.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, GAT pretraining
- **Evidence pointer** Methods section "Structural representation from residue contact maps"
- **Issue** The text states that the GAT is pretrained with contrastive learning but does not specify how the pretrained representations are used. Are the GAT weights frozen after pretraining, or is the GAT fine-tuned during classification?
- **Required correction** Clarify whether the GAT is frozen or fine-tuned during the classification training phase.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Incomplete reporting of comparison results and statistical significance
  - R1-M2: Insufficient detail on SMOTE application and class imbalance characteristics
  - R1-M3: Incomplete GAT architecture and pretraining details
  - R1-M4: Limited evidence for generalizability and proteome-wide applicability
  - R1-M5: Ablation results not fully reported, synergy claim not supported

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The combination of AlphaFold-derived structural graphs with sequence features for LLPS prediction is a reasonable extension of existing work, but the individual components (GAT, SMOTE, ensemble learning) are well-established. The novelty lies primarily in the specific integration, which is incremental rather than transformative.
  - **Scientific importance**: Moderate. LLPS prediction is an active area with practical utility, but the reported performance gains over existing methods are modest (~0.8% accuracy improvement over the second-best method). The method does not address a fundamental biological question but rather provides an improved computational tool.
  - **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to computational biologists and bioinformaticians. The biological implications are discussed but not deeply explored. The method is not likely to attract broad readership beyond the specialized community.
  - **Technical soundness**: Currently not fully established. Key methodological details are missing, and the statistical rigor of the comparisons is insufficient. The ablation study is appropriately designed but not fully reported.
  - **Readability for nonspecialists**: Acceptable. The manuscript is generally well-written and the logic is clear, but some sections (particularly the GAT description) assume familiarity with graph neural networks. The abstract is accessible.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant problem and the proposed approach is reasonable, but the evidence base is incomplete. The authors must provide the full comparison table with statistical measures, complete methodological details for the GAT and SMOTE components, and additional validation to support the generalizability claims. If these concerns are addressed, the manuscript could be suitable for publication in a specialized bioinformatics journal, though the modest performance gains and incremental novelty may limit its appeal for a high-impact generalist venue.