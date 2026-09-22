## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary material notice)
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims relative to presented evidence, and suitability for a high-impact interdisciplinary journal
- **Shared manuscript claim summary** The authors propose a Siamese network-based framework (snLLPS and msnLLPS) that fuses ESM2 protein sequence embeddings with PPI network graph embeddings (Node2vec, DeepNF, Line2vec, Struct2vec) to predict liquid-liquid phase separation (LLPS) proteins, achieving high accuracy on small sample sets and outperforming existing LLPS predictors.
- **Visible evidence base** Benchmark dataset description (859 positive, 1560 negative), model architecture descriptions, performance comparisons across feature lengths, graph embedding methods, and PPI databases, human proteome prediction results with candidate proteins
- **Missing materials affecting confidence** Supplementary materials referenced but not provided; figure contents not visible; detailed hyperparameter settings not provided; exact dataset composition and overlap with training sets of compared methods not verifiable; statistical significance tests not reported

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in computational biology, namely the prediction of LLPS proteins, and proposes a reasonable methodological contribution by combining ESM2 embeddings with PPI network embeddings in a Siamese architecture. The core idea of fusing sequence-level and interaction-level features is sensible and potentially useful. However, the manuscript has several significant weaknesses that prevent the case from being fully established. The evaluation is incomplete in several respects: no comparison against state-of-the-art LLPS predictors on their own benchmark datasets, no statistical significance testing, no ablation study isolating the contribution of the Siamese architecture versus simpler fusion approaches, and no analysis of potential data leakage between training and test sets. The human proteome prediction section is largely anecdotal, presenting candidate proteins without experimental validation or quantitative assessment. The writing is generally clear but contains some imprecise statements and the methods section omits important implementation details.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those focused on phase separation and biomolecular condensates. Researchers developing deep learning methods for protein property prediction from sequence and interaction data may also find the Siamese network fusion framework of interest. The potential practical utility for prioritizing LLPS candidates for experimental validation could attract experimental biologists studying phase separation, though the current evidence does not yet demonstrate clear practical advantages over existing tools.

- **Major strengths**
  1. The problem is timely and biologically important, given the growing recognition of LLPS in cellular organization and disease.
  2. The methodological idea of fusing ESM2 sequence embeddings with PPI graph embeddings is novel in the LLPS prediction context and represents a reasonable extension of prior work.
  3. The use of a Siamese network with contrastive learning is well-motivated for small sample size scenarios, which is a genuine constraint in this field.
  4. The comparison of multiple graph embedding methods and feature dimensions is systematic and provides useful practical guidance.
  5. The framework is described as flexible and extensible, which could benefit future work in related prediction tasks.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that msnLLPS outperforms existing LLPS prediction models including PredLLPS_PSSM, DeePhase, PSpred, and PSPredictor.
- **Evidence pointer** Section "Comparison of the Siamese network-based models with other liquid–liquid phase separation models", Figure 6
- **Concern** The comparison against existing LLPS predictors is not conducted on their respective benchmark datasets or under their original training conditions. The authors appear to have trained these methods on their own dataset, which may not be appropriate if those methods were optimized for different data distributions or feature representations. Moreover, the specific versions, hyperparameters, and training procedures for the compared methods are not described. Without a fair and standardized comparison protocol, the claimed superiority cannot be reliably assessed.
- **Why it matters** The central claim of the manuscript is that the proposed method achieves superior performance over existing tools. If the comparison is not conducted under equivalent conditions, the conclusion is not supported. This is the primary basis for recommending the method as an improvement over the state of the art.
- **Resolution test** The authors should provide a detailed description of how each compared method was trained and evaluated, including dataset splits, hyperparameters, and any preprocessing steps. Ideally, they should also evaluate their method on the benchmark datasets used in the original publications of the compared methods. If this is not feasible, the claims should be appropriately qualified.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the Siamese network approach achieves good accuracy even in small sample sets and that the multi-channel fusion provides synergistic advantages.
- **Evidence pointer** Section "Comparison of the Siamese network–based models with other liquid–liquid phase separation models", Figure 6
- **Concern** No ablation study is presented that isolates the contribution of the Siamese architecture itself versus a simpler concatenation-based fusion or a single-channel model. The comparison between snLLPS(ESM), snLLPS(PPI), and msnLLPS shows that fusion helps, but it does not demonstrate that the Siamese architecture specifically is responsible for the improvement. A baseline model that simply concatenates ESM2 and PPI features and feeds them into a standard classifier would be needed to establish the value of the Siamese design.
- **Why it matters** The methodological novelty claimed in the manuscript rests on the Siamese architecture with contrastive learning. Without an ablation study, it is unclear whether the performance gains come from the architecture, the feature fusion, or simply the use of more information. This weakens the scientific contribution.
- **Resolution test** Add an ablation study comparing msnLLPS against a non-Siamese baseline that uses the same fused features (e.g., a standard feedforward network or logistic regression on concatenated features). Report performance across all metrics and datasets.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report performance metrics (ACC, MCC, F1, AUC) across multiple experiments and claim consistent improvements.
- **Evidence pointer** Sections "Comparison of the Siamese network-based liquid–liquid phase separation models with different ESM2 feature lengths", "Comparison of the Siamese network-based liquid–liquid phase separation models with different protein–protein interaction feature lengths", "Comparison of the Siamese network-based liquid–liquid phase separation models with different graph-embedding methods", Figures 2-5
- **Concern** No statistical significance testing is reported for any of the performance differences. Given that the dataset is relatively small and the evaluation involves 10-fold cross-validation, the observed differences could be within the range of random variation. Confidence intervals or p-values are essential to determine whether the reported improvements are meaningful.
- **Why it matters** The manuscript makes numerous comparative claims (e.g., 128-dimensional PPI features are optimal, Node2vec outperforms other embedding methods, msnLLPS is more robust than snLLPS). Without statistical support, these claims are not substantiated and may mislead readers.
- **Resolution test** Report confidence intervals for all metrics across cross-validation folds, and perform appropriate statistical tests (e.g., paired t-test or Wilcoxon signed-rank test) for pairwise comparisons between models.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the benchmark dataset was "rigorously curated" and that negative samples were derived from PDB structures with a 30% sequence identity cutoff.
- **Evidence pointer** Section "Benchmark dataset"
- **Concern** The description of the dataset curation is insufficient to assess potential biases. Specifically, it is not stated whether the positive and negative sets were filtered for sequence similarity to each other, which could lead to trivial classification based on sequence homology. Additionally, the criteria for selecting the 859 positive proteins from the four databases are not described in detail, and the overlap between these databases is not discussed. The negative set is described as "PDB-derived" but the exact selection procedure is unclear.
- **Why it matters** Dataset construction is fundamental to the validity of any machine learning study. If there is sequence leakage between training and test sets, or if the positive and negative sets are not well-separated in terms of underlying biology, the reported performance may be artificially inflated.
- **Resolution test** Provide a detailed description of the dataset curation pipeline, including sequence identity filtering between positive and negative sets, the specific criteria for inclusion from each database, and the distribution of sequence lengths and species. Report the number of unique sequences and the pairwise sequence identity statistics.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the human proteome prediction identified several highly plausible LLPS proteins, including gelsolin, TIMP3, CBS, HSP70, ribosomal protein L7, GRIA2, and pyruvate carboxylase.
- **Evidence pointer** Section "Using Siamese network-based liquid–liquid phase separation models predict human proteome"
- **Concern** The human proteome prediction results are presented in a purely anecdotal manner. No quantitative assessment is provided, such as the number of proteins predicted as LLPS, the distribution of confidence scores, or a comparison against known LLPS proteins not in the training set. The selection of the seven highlighted proteins appears arbitrary, and no evidence is provided that these are novel predictions rather than proteins already known to undergo LLPS.
- **Why it matters** The human proteome prediction is presented as a demonstration of the method's practical utility. Without a systematic evaluation, this section does not add scientific value and may be seen as speculative.
- **Resolution test** Provide a quantitative analysis of the human proteome predictions, including the total number of predicted LLPS proteins, the distribution of scores, and a comparison against known LLPS proteins (e.g., from PhaSePro or LLPSDB) to estimate recall. If possible, validate a subset of novel predictions against published experimental evidence.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the multi-channel Siamese network model achieved optimal predictive performance when using ESM2 embeddings with 480 dimensions" and that "the msnLLPS model attained peak prediction performance with 256-dimensional PPI features but demonstrated best generalization with 64-dimensional features."
- **Evidence pointer** Sections "Comparison of the Siamese network-based liquid–liquid phase separation models with different ESM2 feature lengths" and "Comparison of the Siamese network-based liquid–liquid phase separation models with different protein–protein interaction feature lengths", Figures 2-3
- **Concern** The selection of optimal feature dimensions appears to be based solely on empirical performance without a principled justification. The observation that 256-dimensional PPI features perform best on the test set but 64-dimensional features generalize better suggests overfitting, yet no regularization strategy or model selection criterion is described. The authors do not explain how the final model configuration was chosen for subsequent experiments.
- **Why it matters** If the model configuration is selected based on test set performance, the reported results may be optimistically biased. A proper model selection procedure (e.g., using a validation set for hyperparameter tuning) is essential for unbiased evaluation.
- **Resolution test** Clarify the model selection procedure. If the test set was used for configuration selection, re-run the evaluation with a nested cross-validation scheme or a separate validation set. Report the variance of performance across configurations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Model architecture description
- **Evidence pointer** Section "Liquid–liquid-phase separation model based on Siamese network"
- **Issue** The description of the Siamese network architecture is incomplete. The number of layers, hidden dimensions, activation functions, dropout rates, and optimization details are not specified. The dynamic weighting layer is mentioned but its exact formulation is not given.
- **Required correction** Provide a complete specification of the network architecture, including layer sizes, activation functions, regularization, and the formula for the dynamic weighting mechanism. Consider including a pseudocode or a detailed algorithm box.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Training procedure
- **Evidence pointer** Section "Model training and evaluation"
- **Issue** The training procedure is not described in sufficient detail. The loss function is mentioned but the optimization algorithm, learning rate, batch size, number of epochs, and early stopping criteria are not provided.
- **Required correction** Add a subsection describing the training details, including the optimizer, learning rate schedule, batch size, and stopping criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Evaluation metrics
- **Evidence pointer** Section "Model training and evaluation"
- **Issue** The authors report Accuracy, Precision, F1-score, and MCC, but do not report sensitivity, specificity, or ROC-AUC consistently across all experiments. AUC is mentioned in some sections but not defined or consistently reported.
- **Required correction** Report a consistent set of metrics across all experiments, including sensitivity, specificity, and AUC where applicable. Define all metrics clearly.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure descriptions
- **Evidence pointer** Figures 2-6
- **Issue** The figure captions are not provided in the manuscript text, and the figures themselves are not visible. It is therefore impossible to assess the presented results.
- **Required correction** Ensure that all figures are included with detailed captions that describe the experimental setup, the compared methods, and the key observations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Code and data availability
- **Evidence pointer** Data availability section
- **Issue** The GitHub repository is mentioned, but it is not clear whether the code includes all preprocessing steps, model definitions, and evaluation scripts. The benchmark dataset is said to be available, but the exact format and access instructions are not provided.
- **Required correction** Provide a detailed README in the repository that describes the dataset format, the code structure, and instructions for reproducing all reported results.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Scientific context
- **Affected element** Related work discussion
- **Evidence pointer** Introduction
- **Issue** The introduction reviews existing LLPS prediction methods but does not discuss recent deep learning-based approaches in sufficient depth. The novelty of the proposed method relative to these approaches is not clearly articulated.
- **Required correction** Expand the related work section to include a more comprehensive comparison with recent deep learning methods for LLPS prediction, and explicitly state the novelty of the proposed approach.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout
- **Issue** The term "liquid-phase separation proteins" is used throughout, but the standard term in the field is "liquid-liquid phase separation proteins" or "phase-separating proteins." The abbreviation "LLPS" is used inconsistently.
- **Required correction** Use consistent terminology throughout the manuscript, and define all abbreviations at first use.

- **Technical failings that need to be addressed before the case is established** R1-M1 (comparison protocol), R1-M2 (ablation study), R1-M3 (statistical significance), R1-M4 (dataset curation details). These are the primary technical issues that must be resolved before the claims of superior performance and methodological novelty can be accepted.

- **Assessment against Nature-style criteria**
  - **Originality** The combination of ESM2 sequence embeddings with PPI graph embeddings in a Siamese network for LLPS prediction is a novel contribution, though the individual components are established. The originality is moderate and would be strengthened by a clearer demonstration of why this specific architecture is uniquely suited to the problem.
  - **Scientific importance** LLPS prediction is a relevant and growing field, and improved computational methods could aid experimental research. However, the current evidence does not demonstrate a substantial advance over existing tools, and the practical impact is not yet clear.
  - **Interdisciplinary readership** The topic sits at the intersection of computational biology, machine learning, and biophysics. The manuscript is likely to appeal to a specialized audience but may not attract broad interdisciplinary interest without clearer demonstrations of biological insight or methodological generalizability.
  - **Technical soundness** The technical soundness is currently insufficient due to the lack of statistical testing, incomplete ablation studies, and potential issues with the comparison protocol. These issues must be resolved.
  - **Readability for nonspecialists** The manuscript is generally readable, but the methods section assumes familiarity with deep learning and graph embedding concepts. Some terms are used without definition, and the figures are not described in the text. The readability could be improved with a more accessible introduction to the key concepts.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant problem and presents a reasonable methodological idea, but the claims of superior performance and methodological novelty are not adequately supported. The technical concerns regarding the comparison protocol, ablation study, statistical testing, and dataset curation must be addressed before the case can be made. I would be supportive of reconsideration if these issues are resolved with additional experiments and analyses.