## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv 2024.05.08.593266)
- **Assessment boundary** Scientific content, methodology, claims, and evidence as presented in the provided text. No external data or code were accessed.
- **Shared manuscript claim summary** The authors present Graph Neural Network (GNN) models, at both atom-level and residue-level, to predict whether 30-residue peptide sequences function as transcriptional activation domains (ADs). They report that a residue-level GNN with features including amino acid type, residue position, acidic/basic/aromatic property, and secondary structure achieves the best performance (accuracy 97.9%, F1 71%, AUROC 97.1%), outperforming existing methods (ADPred, PADDLE, Mahatma et al. 2023) on the same dataset. They also use logistic regression to identify amino acid composition as the most important feature, with acidic and aromatic residues positively associated and basic residues negatively associated with function.
- **Visible evidence base** Abstract, Introduction, Methods (dataset description, GNN architectures, feature engineering, training details, post-processing), Results (performance tables, confusion matrices, feature importance analysis, comparison with prior methods), Conclusion, Acknowledgements. Tables 1-13 and Figures 1-4 are referenced but not shown in the provided text.
- **Missing materials affecting confidence** Actual tables and figures (performance metrics, confusion matrices, feature importance plots, architecture diagrams) are not included. Code, hyperparameters, and exact dataset splits are not provided. Details on the negative dataset construction (beyond the Gcn4 reference) are not fully described. Statistical significance tests for performance differences are not reported.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in transcriptional regulation, namely the prediction of activation domain function from sequence and predicted structure. The use of GNNs is a reasonable methodological advance over prior CNN-based approaches. However, the current evidence base is insufficient to fully evaluate the claims. Key performance metrics are reported without corresponding figures or tables, and the comparison with prior methods lacks statistical rigor. The feature importance analysis via logistic regression is informative but limited by the model's known saturation. The manuscript would benefit from clearer reporting of experimental details and more robust evaluation, including confidence intervals and external validation.
- **Who would be interested in the results, and why** Researchers in transcriptional regulation, intrinsically disordered proteins, and machine learning applied to biology. The work may also interest those developing structure-based predictors for protein function, given the use of predicted structures and GNNs.
- **Major strengths** 1) Addresses a challenging and biologically important problem with a novel methodological approach (GNNs) that can capture non-local dependencies. 2) Systematic exploration of multiple feature combinations, including structural features derived from predicted structures. 3) Inclusion of a logistic regression baseline for feature interpretability. 4) Comparison with several existing methods on the same dataset.
- **Major Concerns** See items below.
- **Minor Comments** See items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing data), R1-M2 (comparison rigor), R1-M3 (dataset balance and leakage), R1-M4 (feature importance interpretation).
- **Assessment against Nature-style criteria** **Originality**: Moderate. GNNs are not new, but their application to AD prediction is a novel contribution. **Scientific importance**: Moderate to high. Understanding AD function is a long-standing problem, and improved predictors could aid in synthetic biology and genome engineering. **Interdisciplinary readership**: Moderate. The work bridges machine learning and molecular biology, but the presentation is technical and may not fully engage a broad biological audience. **Technical soundness**: Currently not fully established due to missing data and incomplete evaluation. **Readability for nonspecialists**: The abstract and introduction are accessible, but the methods section is dense and assumes familiarity with GNNs and structural biology concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the manuscript requires substantial revisions to provide complete evidence and rigorous comparisons.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims the residue-level GNN with feature combination 3 achieves accuracy 97.9%, F1 71%, and AUROC 97.1%, outperforming other methods.
- **Evidence pointer** Results section, Tables 8, 10, 12, 13; Figures 2-4 (location not provided in text)
- **Concern** The key performance results are presented only as numbers in the text. The referenced tables and figures are not included in the provided material, making it impossible to verify the reported metrics, assess variance, or examine confusion matrices and ROC curves.
- **Why it matters** Without the actual data, the central claims of the paper cannot be independently evaluated. The reader cannot determine whether the reported improvements are meaningful or within noise.
- **Resolution test** Provide all tables and figures in the manuscript. Include confidence intervals or standard deviations for all metrics, and show confusion matrices and ROC curves.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative rigor
- **Claim pointer** The manuscript states the proposed model outperforms ADPred, PADDLE, and Mahatma et al. (2023) on the same dataset.
- **Evidence pointer** Results section, "Comparison with other methods" (location not provided)
- **Concern** The comparison with prior methods is not statistically validated. No significance tests (e.g., McNemar's test, DeLong's test for AUROC) are reported. Additionally, the comparison with Mahatma et al. is performed on a balanced subset, while other comparisons use the imbalanced test set, making direct comparisons inconsistent.
- **Why it matters** Claims of superiority require statistical evidence. Without it, the observed differences could be due to chance, especially given the class imbalance and the small number of positive examples.
- **Resolution test** Perform and report appropriate statistical tests for all comparisons. Ensure consistent evaluation protocols across methods (e.g., same test set, same threshold selection procedure).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and leakage
- **Claim pointer** The dataset is described as the Gcn4 dataset with 1,054,335 sequences, 37,923 functional. The train/validation/test split is 75:15:10.
- **Evidence pointer** Methods, "Dataset" and "Training" sections (location not provided)
- **Concern** The manuscript does not describe how the negative (non-functional) sequences were generated or whether there is any sequence similarity between train and test sets that could lead to data leakage. The Gcn4 dataset is referenced, but the details of its construction are not provided. Additionally, the class imbalance (3.6% positive) is extreme, and the handling of this imbalance beyond training set resampling is not described.
- **Why it matters** Data leakage or unrepresentative negative sets can inflate performance metrics. The extreme imbalance also affects the interpretation of accuracy, which is dominated by the majority class.
- **Resolution test** Clearly describe the origin and construction of the negative set. Perform and report a sequence-similarity-based split (e.g., CD-HIT clustering) to ensure no leakage. Report precision-recall curves and Matthews correlation coefficient in addition to accuracy and F1.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability
- **Claim pointer** The manuscript concludes that amino acid composition is the most important feature, with acidic and aromatic residues positively associated and basic residues negatively associated with function.
- **Evidence pointer** Results, "Feature importance" and Figure 4 (location not provided)
- **Concern** The logistic regression feature importance analysis is based on a model that achieves only 95.5% accuracy and is described as saturated. The coefficients for amino acid counts may reflect correlations with other features rather than causal effects. The analysis does not account for potential interactions between features.
- **Why it matters** The biological conclusions drawn from this analysis are used to support the broader narrative about AD function. Overinterpretation of coefficients from a saturated model could mislead.
- **Resolution test** Use a more interpretable model or a permutation-based feature importance method. Validate the findings on an independent dataset or with a held-out set. Discuss the limitations of the logistic regression approach.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Graph Neural Network (Residue-level GNN)"
- **Evidence pointer** Equation 14 (location not provided)
- **Issue** The definition of the adjacency matrix A2 in Equation 14 is incomplete. The text states "A2ij={e−λdij" but does not specify the condition for when this value is applied (e.g., for all pairs, or only within a cutoff distance). The description of the graph construction is ambiguous.
- **Required correction** Provide a complete definition of A2, including any distance cutoffs or normalization. Clarify whether the graph is fully connected or sparse.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Training"
- **Evidence pointer** Training section (location not provided)
- **Issue** The manuscript states models converged after approximately 350 epochs but does not provide details on early stopping criteria, learning rate scheduling, or the number of runs. The selection of the final model (e.g., based on validation loss or F1) is not described.
- **Required correction** Specify the model selection procedure, including the metric used for early stopping and the number of random seeds or runs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, "Evaluation metric"
- **Evidence pointer** Results section (location not provided)
- **Issue** The manuscript reports accuracy, F1, and AUROC but does not provide confidence intervals or any measure of variability. Given the class imbalance, reporting precision-recall AUC would be more informative.
- **Required correction** Report confidence intervals for all metrics and include precision-recall AUC.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2 (location not provided)
- **Issue** The introduction mentions prior work but does not clearly distinguish the novelty of the GNN approach over the cited CNN-based methods beyond the ability to capture long-range dependencies. The specific limitations of prior methods are not fully articulated.
- **Required correction** Expand the discussion of prior methods' limitations and explicitly state the expected advantages of GNNs in this context.

## Risk / unsupported claims
- The claim that the residue-level GNN outperforms all existing methods is unsupported without statistical tests and the actual comparison tables.
- The claim that amphipathic index is an important feature is based on a reduced dataset and a single model comparison; the generalizability of this finding is unclear.
- The biological conclusion that acidic and aromatic residues are necessary for function, while basic residues are detrimental, is based on logistic regression coefficients and may not hold under more complex models.
- The choice of ESMFold over AlphaFold is justified by speed and a preliminary analysis on 240 sequences, but the statistical significance of this analysis is borderline (p=0.03) and the rationale for preferring ESMFold for the main dataset is not fully established.