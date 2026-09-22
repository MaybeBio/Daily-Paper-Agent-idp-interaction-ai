## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions)
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and interpretation of results as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose a machine-learning framework combining five feature ranking algorithms (CATboost, XGBoost, LASSO, LightGBM, PFI) with incremental feature selection (IFS) and random forest (RF) classifiers to identify Gene Ontology (GO) terms that distinguish phase-separation proteins (PSPs) from non-PSPs, achieving F1 scores above 0.960 and identifying ten GO terms consistently ranked as most essential across all methods.
- **Visible evidence base** Abstract, full methods section, results section with performance tables and figures referenced, discussion section with biological interpretation
- **Missing materials affecting confidence** Supplementary tables (S1–S4) and figures (1–3) referenced but not provided; no code availability statement; no hyperparameter details for machine learning models; no external validation dataset results; no statistical significance testing for performance differences

## Reviewer
- **Overall assessment** The manuscript presents a straightforward application of established machine learning methods to a biologically relevant classification problem. The computational framework is reasonable, and the reported performance metrics are strong. However, several methodological concerns regarding data leakage, class imbalance handling, and the interpretability of the "essential GO terms" weaken the current claims. The biological discussion is largely speculative and does not provide independent validation of the identified GO terms. The work is incremental relative to existing PSP prediction tools and does not clearly demonstrate a novel contribution beyond what is already available in the field.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, particularly those interested in the functional annotation of PSPs and the development of computational predictors. The identified GO terms may be of interest to cell biologists studying membrane-less organelles, RNA processing, and synaptic function. The methodological framework could also be of interest to bioinformaticians working on feature selection for high-dimensional biological data.

- **Major strengths** 
  1. The use of multiple complementary feature ranking algorithms provides a more robust assessment of feature importance than a single method.
  2. The IFS framework is a well-established approach for identifying optimal feature subsets in high-dimensional classification problems.
  3. The reported F1 scores above 0.960 suggest strong classification performance.
  4. The biological discussion connects identified GO terms to known PSP functions, providing some face validity.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data leakage / methodological validity
- **Claim pointer** The authors claim that the RF classifiers can "distinguish PSPs from non-PSPs" with F1 scores over 0.960.
- **Evidence pointer** Section 2.1, Section 2.3, Section 3.2, Table 1
- **Concern** The feature selection process (IFS) is performed on the same dataset used to evaluate the classifiers. The optimal feature subsets are selected based on cross-validated performance on the full dataset, and then the same data are used to report the final performance. This creates a potential selection bias, as the feature selection procedure has "seen" the test folds during the selection process. The reported F1 scores are therefore likely optimistically biased and may not generalize to independent datasets.
- **Why it matters** If the reported performance is inflated due to selection bias, the practical utility of the classifiers for identifying novel PSPs is unclear. The core claim of the paper, that efficient classifiers were built, depends on unbiased performance estimates.
- **Resolution test** The authors should perform nested cross-validation, where feature selection is conducted within each training fold only, or validate the final models on a completely independent held-out dataset. The performance should be re-reported under these conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Class imbalance handling
- **Claim pointer** The authors state that SMOTE was used to address the extreme class imbalance between 578 PSPs and 58,563 non-PSPs.
- **Evidence pointer** Section 2.4
- **Concern** The description of SMOTE application is insufficient. It is unclear whether SMOTE was applied before feature selection, within each cross-validation fold, or only to the training set. If SMOTE is applied to the entire dataset before cross-validation, synthetic samples from the minority class will appear in both training and test folds, leading to data leakage and inflated performance estimates. Additionally, the ratio of synthetic to original samples is not specified.
- **Why it matters** Improper application of oversampling techniques in the presence of cross-validation is a well-documented source of bias. The validity of all reported performance metrics depends on correct handling of the class imbalance.
- **Resolution test** The authors should clarify the exact pipeline: SMOTE must be applied only to the training folds during cross-validation, and the test folds must contain only original samples. The oversampling ratio should be stated.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological interpretation / claim support
- **Claim pointer** The authors claim that the identified GO terms "are crucial for distinguishing between PSPs and non-PSPs" and that they "reveal the partial function of the PSPs."
- **Evidence pointer** Section 3.3, Section 4
- **Concern** The biological discussion is largely speculative. The authors connect identified GO terms to known PSP functions, but this is a post-hoc interpretation without independent experimental validation. The fact that a GO term is statistically important in a classifier does not establish a causal or mechanistic link to phase separation. Furthermore, the discussion does not address whether the identified GO terms are simply generic markers of protein abundance, cellular localization, or other confounding factors.
- **Why it matters** The paper's contribution to understanding PSP biology depends on the biological relevance of the identified GO terms. Without independent validation, the biological claims are not established.
- **Resolution test** The authors should either (a) provide independent evidence that the identified GO terms are enriched in known PSPs compared to appropriate controls, (b) experimentally validate at least a subset of predictions, or (c) temper the biological claims to reflect the computational nature of the findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility / methodological detail
- **Claim pointer** The authors state that five feature ranking algorithms were used and that RF classifiers were built within the IFS framework.
- **Evidence pointer** Section 2.2, Section 2.3
- **Concern** Critical hyperparameters for the machine learning models are not reported. For CATboost, XGBoost, LightGBM, and RF, the number of trees, learning rate, tree depth, and other regularization parameters are not specified. For LASSO, the regularization strength (alpha) is not given. The SMOTE parameters (k-neighbors, sampling strategy) are also missing. Without these details, the experiments cannot be reproduced.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. The lack of hyperparameter details prevents other researchers from replicating or building upon this work.
- **Resolution test** The authors should provide a complete table of all hyperparameters used for each algorithm, or make the code publicly available with a configuration file.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparison to existing methods
- **Claim pointer** The authors state that existing PSP prediction tools "cannot fully uncover essential differences between PSPs and non-PSPs" and imply that their approach is novel.
- **Evidence pointer** Section 1, Section 3
- **Concern** The manuscript does not provide a direct comparison between the proposed method and existing PSP predictors (e.g., PScore, PLAAC, PSPredictor, FuzDrop). The claim of novelty and improved performance is not supported by comparative experiments. It is unclear whether the GO-based approach offers any advantage over sequence-based or structure-based predictors.
- **Why it matters** Without a benchmark comparison, the contribution of this work relative to the state of the art is unclear. The claim that this approach provides new insights is not substantiated.
- **Resolution test** The authors should compare their method against at least one or two existing PSP predictors on a common benchmark dataset, reporting standard metrics such as accuracy, F1, AUC, and Matthews correlation coefficient.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1
- **Evidence pointer** Section 2.1
- **Issue** The text states "Sequences of these proteins were obtained from UniPort" which appears to be a typo for UniProt. Additionally, the version or release date of the UniProt database is not specified.
- **Required correction** Correct the typo to "UniProt" and specify the database version or retrieval date.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 3.2, Table 1
- **Evidence pointer** Section 3.2, Table 1
- **Issue** The performance metrics are reported as point estimates without confidence intervals or standard deviations. Given the small number of positive samples (578), the variability of the F1 scores across cross-validation folds should be reported.
- **Required correction** Report the mean and standard deviation (or 95% confidence intervals) of the performance metrics across the cross-validation folds.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, Section 1
- **Evidence pointer** Abstract, Section 1
- **Issue** The term "membranelle" is used, which is not a standard term in cell biology. The correct term is "membrane-less" or "membraneless."
- **Required correction** Replace "membranelle" with "membrane-less" or "membraneless" throughout the manuscript.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 2
- **Evidence pointer** Figure 2 (referenced in Section 3.2)
- **Issue** The IFS curves are described but the figure is not provided in the manuscript text. It is unclear whether the curves for all five feature lists are shown in a single panel or separate panels, and whether the inflection points are clearly marked.
- **Required correction** Ensure Figure 2 clearly displays all five IFS curves with distinct colors or line types, and that inflection points are labeled with the corresponding F1 scores.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Section 2.1, Supplementary Materials
- **Evidence pointer** Section 2.1
- **Issue** The authors state that proteins are provided in Table S1, but this supplementary table is not included in the provided manuscript. The accessibility of the data is therefore unclear.
- **Required correction** Confirm that all supplementary tables are publicly available and provide a data availability statement.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Section 4.1
- **Evidence pointer** Section 4.1
- **Issue** The sentence "On the basis of the fact that the RBPs involved in the formation of phase separation undergo phase separation" is redundant and awkwardly phrased.
- **Required correction** Rephrase for clarity, for example: "Given that RBPs involved in RNP formation undergo phase separation..."

## Risk / unsupported claims
- The claim that the identified GO terms are "crucial" for distinguishing PSPs from non-PSPs is not fully supported, as the feature selection was performed on the same data used for evaluation, and no external validation was performed.
- The claim that the study "offered recommendations for future research aimed at determining the functional roles of PSPs" is speculative and not directly supported by the experimental design.
- The biological interpretation in Section 4 relies on post-hoc reasoning without independent experimental validation, and the causal relationship between the identified GO terms and phase separation is not established.
- The performance comparison implied in the Introduction (that existing methods "cannot fully uncover essential differences") is not directly tested, making this claim unsupported.
- The generalizability of the classifiers to novel PSPs beyond the training set is not demonstrated, as no independent test set was used.