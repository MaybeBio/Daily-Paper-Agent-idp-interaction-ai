## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusion) as provided
- **Assessment boundary** Scientific and technical evaluation of the manuscript content only; no assessment of web server functionality or code availability beyond what is described
- **Shared manuscript claim summary** The authors present ARACoFusion, a deep learning architecture for Arabidopsis thaliana PPI prediction from primary sequences, incorporating reciprocal cross-attention, latent interaction projection, multi-source feature fusion, uncertainty-aware variance regularization, focal loss with label smoothing, and temperature scaling calibration. They claim superior performance over existing plant-specific predictors across multiple evaluation regimes, robust cross-species generalization, and improved calibration.
- **Visible evidence base** Abstract, Introduction, Materials and Methods (Sections 2.1-2.6), Results (Sections 3.1-3.3), Conclusion, Tables 1-13 (referenced), Figures 1-11 (referenced)
- **Missing materials affecting confidence** Actual figures and tables are not provided; only textual descriptions. No supplementary materials, code repository contents, or detailed hyperparameter configurations are available. Statistical significance testing details are not described.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in plant systems biology and proposes a technically sophisticated architecture. However, the evidence presented is insufficient to fully support the strong claims of superiority and generalizability. Several methodological details are incomplete or ambiguous, and the evaluation framework has potential weaknesses that are not adequately addressed. The work is potentially valuable but requires substantial revision and additional validation before the claims can be considered established.
- **Who would be interested in the results, and why** Plant biologists studying Arabidopsis interactomes, computational biologists developing PPI prediction methods, and researchers interested in uncertainty-aware deep learning for biological applications. The web tool may be useful for the Arabidopsis community, and the methodological innovations could inform future work in plant-specific prediction models.
- **Major strengths** The architecture is thoughtfully designed with multiple complementary components addressing known limitations in PPI prediction. The focus on calibration and uncertainty is a valuable contribution, as most existing methods do not address this. The cross-species evaluation on rice is a useful addition. The ablation study is systematic and helps attribute performance to specific components.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data quality and negative set construction
- **Claim pointer** The negative dataset construction is described as using random pairing of proteins after removing those with >40% sequence identity to positives. The authors claim this produces a valid negative set for training and evaluation.
- **Evidence pointer** Section 2.1, Table 1
- **Concern** The negative set construction methodology is problematic. Random pairing of proteins does not guarantee that the resulting pairs are true non-interactions; it only assumes that most random pairs are non-interactions. More critically, the description states that proteins with >40% sequence identity to positive samples were removed, but it is unclear whether this threshold was applied to individual proteins or to pairs. The final negative set of 77,290 pairs derived from 8,382 proteins plus positive-set proteins raises questions about potential redundancy and whether the negative set adequately represents the true distribution of non-interacting pairs in the Arabidopsis proteome. The lack of any experimental validation or literature-based curation of negatives is a significant concern.
- **Why it matters** The quality of the negative set directly determines the validity of all performance metrics. If negatives are not truly non-interacting, the reported AUPRC, MCC, and other metrics are unreliable. This is a foundational issue that affects every subsequent result.
- **Resolution test** Provide a detailed description of negative set construction, including the exact algorithm for random pairing, any filters applied to remove potential false negatives, and an analysis of the negative set's properties (e.g., sequence similarity distribution, functional annotation enrichment). Consider validating a subset of predicted negatives against literature or interaction databases.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evaluation methodology and data leakage
- **Claim pointer** The authors claim superior performance over existing plant-specific predictors using C1 for training and C2/C3 for testing, and 5-fold cross-validation on merged C1+C2+C3.
- **Evidence pointer** Section 2.5, Section 3.2, Tables 3-8
- **Concern** The evaluation methodology raises concerns about data leakage and fair comparison. First, the C1/C2/C3 split method from Park and Marcotte is referenced but not described in sufficient detail; it is unclear how sequence similarity is handled across splits. If proteins with high sequence similarity appear in both training and test sets, the reported performance may be optimistically biased. Second, for the 5-fold cross-validation on merged data, it is unclear whether the same protein pairs or highly similar proteins appear in multiple folds. Third, the comparison with ESMAraPPI uses the authors' original hyperparameters, but it is unclear whether ESMAraPPI was retrained on the same C1 data or used as a pre-trained model. If ESMAraPPI was not retrained, the comparison may be unfair. Finally, the AraCPINet comparison uses metrics taken directly from the original publication, which may have been evaluated on different data splits, making direct comparison inappropriate.
- **Why it matters** If the evaluation is not conducted under strictly controlled conditions with appropriate separation of training and test data, the reported performance advantages may not reflect genuine improvements. This undermines the central claim of the manuscript.
- **Resolution test** Provide detailed description of the C1/C2/C3 split methodology, including sequence similarity thresholds applied across splits. Clarify whether ESMAraPPI was retrained on C1 data and describe the exact training protocol. For AraCPINet, either reimplement and evaluate on the same splits or clearly state the limitations of cross-publication comparison.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical significance and uncertainty quantification
- **Claim pointer** The authors claim significant performance improvements over baselines across multiple metrics and datasets.
- **Evidence pointer** Section 3.2, Tables 3-11
- **Concern** No statistical significance testing is reported for any of the performance comparisons. Given the class imbalance (1:10 positive to negative ratio), small differences in AUPRC or MCC may not be meaningful. Additionally, the variance-based uncertainty regularization is described, but no analysis of prediction uncertainty is provided beyond the calibration discussion. The manuscript does not report confidence intervals, standard deviations across folds, or any measure of variability in the reported metrics.
- **Why it matters** Without statistical rigor, the claimed improvements could be due to random variation or specific characteristics of the data splits. The uncertainty-aware aspect of the model is a key selling point, but its benefits are not demonstrated quantitatively.
- **Resolution test** Report confidence intervals or standard deviations for all metrics across cross-validation folds. Perform appropriate statistical tests (e.g., paired bootstrap, McNemar's test) for comparisons with baselines. Provide analysis of predictive uncertainty, such as reliability diagrams with confidence bands or uncertainty-calibration curves.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Cross-species generalization claims
- **Claim pointer** The authors claim robust cross-species generalization based on evaluation on a rice dataset, achieving higher AUPRC than general-purpose predictors.
- **Evidence pointer** Section 3.2, Tables 10-11, Figures 8-9
- **Concern** The cross-species evaluation has several issues. First, the rice dataset construction is described briefly: "Protein pairs that were not rice PPIs were randomly selected as positive samples" - this appears to be a typo and likely should read "negative samples." Second, the rice dataset has only 611 positive interactions, which is small and may not be representative. Third, the AUPRC of 0.3519 for ARACoFusion on rice is quite low in absolute terms, despite being higher than baselines. The claim of "robust cross-species generalization" seems overstated given this modest performance. Finally, it is unclear whether the model was fine-tuned on any rice data or used purely as trained on Arabidopsis.
- **Why it matters** Cross-species generalization is a key claim of the manuscript, but the evidence is weak. The low absolute AUPRC suggests the model may not be practically useful for rice PPI prediction, and the comparison may not be fair if baselines were not evaluated under identical conditions.
- **Resolution test** Clarify the rice dataset construction (including the apparent typo). Provide more detailed analysis of cross-species performance, including precision-recall curves and discussion of why AUPRC is low. If possible, evaluate on additional plant species to strengthen the generalization claim.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Biological validation and practical utility
- **Claim pointer** The authors claim the model exhibits "clear class separability" in t-SNE visualizations and demonstrates utility in "true biological network inference" based on a case study of a 43-node subnetwork.
- **Evidence pointer** Section 3.2, Figures 5, 9, 10
- **Concern** The biological validation is limited. The t-SNE visualizations are qualitative and do not provide quantitative evidence of separability. The case study on a 43-node subnetwork with 70% accuracy is a very small-scale validation and does not demonstrate utility at the network level. No functional enrichment analysis, comparison with known biological pathways, or experimental validation of novel predictions is provided. The claim that the model is useful for "network-level inference" is not supported by the evidence presented.
- **Why it matters** For a biological audience, demonstrating biological relevance is crucial. Without functional validation or network-level analysis, the practical utility of the model remains unclear.
- **Resolution test** Provide quantitative metrics for cluster separability (e.g., silhouette score, Davies-Bouldin index). Expand the network analysis to a larger, more comprehensive evaluation, including functional enrichment of predicted interactions, comparison with known pathways, and analysis of network properties. If possible, validate a subset of novel predictions experimentally or through literature curation.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and resource availability
- **Claim pointer** The authors state that the web server and documentation are publicly available, and the model was implemented using PyTorch.
- **Evidence pointer** Section 2.6, Section 3.3
- **Concern** The manuscript does not provide sufficient details for reproducibility. The exact architecture hyperparameters (number of layers, hidden dimensions, attention heads, etc.) are not fully specified. The training procedure (number of epochs, batch size, learning rate schedule, early stopping criteria) is not described. The Optuna hyperparameter search space is not defined. No information is provided about the random seed, data preprocessing steps, or the exact code used for evaluation. While a web server is mentioned, no code repository link is provided in the manuscript text.
- **Why it matters** Reproducibility is a fundamental requirement for scientific publications. Without complete methodological details, other researchers cannot replicate or build upon this work.
- **Resolution test** Provide a complete description of the architecture, training procedure, and hyperparameter search space. Include a link to the code repository and trained model weights. Consider providing a Docker container or environment configuration file for easy reproduction.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness of methods
- **Affected element** Section 2.1, negative dataset construction
- **Evidence pointer** Section 2.1
- **Issue** The description of negative dataset construction contains an apparent error: "Protein pairs that were not rice PPIs were randomly selected as positive samples" should likely read "negative samples." Additionally, the sentence structure in Section 2.2 ("We found that ESM-1b's evolutionary-scale training provides superior resolution...") is informal and not typical of a methods section.
- **Required correction** Fix the typo in Section 2.1. Rewrite the informal statement in Section 2.2 to be more formal and objective, e.g., "ESM-1b was selected based on its superior performance in preliminary comparisons (Figure 3)."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation of results
- **Affected element** Section 3.2, Tables 3-4
- **Evidence pointer** Section 3.2, Tables 3-4
- **Issue** The manuscript states that Optuna optimization improved performance but does not provide the specific hyperparameter values found by the optimization. Table 2 is referenced but not visible. The text mentions "Tables 3 and 4" for results but does not clearly describe what metrics are shown in each table.
- **Required correction** Provide the optimized hyperparameter values in the text or in a visible table. Clearly describe what each table contains and highlight the key differences between optimized and baseline configurations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure quality and interpretation
- **Affected element** Figures 5, 9
- **Evidence pointer** Section 3.2, Figures 5, 9
- **Issue** The t-SNE visualizations are described as showing "clear class separability" but no quantitative metrics are provided. The color scheme for Figure 5 is confusing: "interacting pairs as true positive indicated by green dots" and "non-interactors as true negative indicated by blue dots" but the text also mentions "red" and "green" for Figure 9, creating potential confusion about color conventions across figures.
- **Required correction** Provide quantitative cluster quality metrics. Standardize color conventions across all figures and clearly state them in each figure caption.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Web server description
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3
- **Issue** The web server description is brief and does not specify the expected input format, maximum sequence length, or processing time. The URL is provided but no screenshot or user interface description is given.
- **Required correction** Provide more details about the web server interface, including input/output formats, example queries, and any usage limitations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction, Section 1
- **Evidence pointer** Section 1
- **Issue** The introduction cites several relevant works but does not provide a comprehensive comparison with recent deep learning-based PPI prediction methods beyond those specifically mentioned. The discussion of limitations of existing methods is somewhat brief.
- **Required correction** Expand the introduction to include a more thorough review of recent PPI prediction methods, particularly those using transformer architectures or uncertainty quantification, and clearly articulate the specific gaps that ARACoFusion addresses.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Conclusion overstatement
- **Affected element** Conclusion
- **Evidence pointer** Conclusion
- **Issue** The conclusion states that ARACoFusion offers a "calibrated, uncertainty-aware, and generalizable solution" but the evidence for generalizability is limited to one cross-species evaluation with modest AUPRC. The claim of "superiority" is based on comparisons that may not be fully fair.
- **Required correction** Moderate the language in the conclusion to accurately reflect the scope of evidence presented. Acknowledge limitations in cross-species generalization and suggest directions for future validation.

- **Technical failings that need to be addressed before the case is established** R1-M1 (negative set construction), R1-M2 (evaluation methodology and potential data leakage), R1-M3 (lack of statistical significance testing), R1-M6 (insufficient reproducibility details). These are foundational issues that must be resolved before the performance claims can be considered reliable.
- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The combination of reciprocal cross-attention, uncertainty-aware regularization, and calibration is novel in the context of plant PPI prediction, but each component has been explored individually in other domains. The specific application to Arabidopsis is valuable but not conceptually groundbreaking.
  - Scientific importance: Moderate. Accurate PPI prediction is important for plant biology, and the focus on calibration is a useful contribution. However, the practical impact depends on the reliability of predictions, which is not fully established.
  - Interdisciplinary readership: Limited. The manuscript is primarily of interest to computational biologists and plant molecular biologists. The methods are not presented in a way that would attract a broader readership.
  - Technical soundness: Currently insufficient. The evaluation methodology has potential flaws, and the lack of statistical rigor undermines confidence in the results. The architecture is reasonable but not fully validated.
  - Readability for nonspecialists: Below average. The methods section is dense and contains informal language. The results section assumes familiarity with PPI prediction metrics and deep learning concepts. Figures are referenced but not visible, making it difficult to assess clarity.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential, but the foundational issues with negative set construction, evaluation methodology, and statistical rigor must be addressed. The authors should also provide complete reproducibility details and strengthen the biological validation. If these concerns are adequately resolved in revision, the work could be suitable for publication in a specialized journal, though it may not meet the broad impact bar for Nature.

## Risk / unsupported claims
- Claim of "significantly outperforms" existing predictors is unsupported without statistical significance testing.
- Claim of "robust cross-species generalization" is overstated given the modest AUPRC (0.3519) on rice and the small dataset size.
- Claim of "clear class separability" in t-SNE is qualitative and not quantitatively supported.
- Claim of "calibrated" predictions is only supported by ECE reduction from 0.034 to 0.020, which is a small absolute improvement, and no comparison to other calibration methods is provided.
- The statement that ESM-1b provides "superior resolution" for plant-specific prediction is not rigorously justified beyond the single comparison shown in Figure 3.
- The claim that the model is useful for "network-level inference" is not supported by the limited case study (43 nodes).
- The web server's functionality and reliability cannot be assessed from the manuscript text alone.