## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and claims as supported by the provided text
- **Shared manuscript claim summary** The authors present Opt_PredLLPS, a two-task computational predictor that first identifies liquid–liquid phase separation (LLPS) proteins using a CNN-BiLSTM hybrid with evolutionary and multimodal features, and then classifies them as self-assembling (PS-Self) or partner-dependent (PS-Part) using XGBoost with 37 physicochemical properties. The model is validated on multiple benchmark datasets and compared against six existing methods.
- **Visible evidence base** Text descriptions of methods, results, and comparisons; references to Figures 1–5, Tables 1–5, and Supplementary Tables S1–S14
- **Missing materials affecting confidence** All figures, tables, supplementary data, dataset details, and code repository contents; exact performance metrics for most comparisons; statistical significance testing

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in computational biology, namely the prediction of phase separation proteins and their mechanistic classification. The two-task architecture is a reasonable extension of prior work, and the inclusion of a PS-Self versus PS-Part distinction is potentially valuable. However, the evidence presented in the text is insufficient to fully evaluate the claims. Key performance numbers are referenced only through figures and tables that are not provided, making it impossible to verify the reported improvements. The methodological description lacks critical details on data splitting, hyperparameter tuning, and the construction of negative datasets. The interpretability analysis, while interesting, is presented without sufficient methodological rigor or validation. The claim of being the "first" model to distinguish PS-Self and PS-Part proteins is contradicted by the authors' own citation of PhaSePred, which already performs this distinction. Overall, the work has merit but requires substantial clarification and additional evidence before its conclusions can be accepted.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those focused on phase separation and membraneless organelles. Researchers studying LLPS mechanisms, drug discovery targeting condensates, and developers of sequence-based prediction tools would find the two-task framework and feature engineering approach of interest. The interpretability analysis may also appeal to those interested in explainable AI in biology.

- **Major strengths**
  1. The two-task architecture addressing both LLPS identification and mechanistic subtyping is a logical and potentially useful design.
  2. The integration of evolutionary information (PSSM, HMM) with multimodal features is well motivated by prior literature.
  3. The use of multiple independent benchmark datasets for comparison is commendable.
  4. The interpretability analysis using in silico saturation mutagenesis represents a thoughtful attempt to provide biological insight beyond prediction.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that Opt_PredLLPS outperforms six state-of-the-art methods across multiple independent datasets.
- **Evidence pointer** Section "Comparison with other state-of-the-art methods on independent datasets"; Figures 5A–C; Tables S10–S13
- **Concern** The text states that Opt_PredLLPS achieved AUC values of 0.92, 0.96, 0.94, and 0.94 on four test datasets, surpassing prior algorithms. However, the actual comparison data, including the performance of all competing methods, is only available in figures and supplementary tables that are not provided. Without these data, it is impossible to verify the claimed superiority, assess the magnitude of improvement, or determine whether differences are statistically significant.
- **Why it matters** The central claim of the manuscript is that the proposed method improves upon existing tools. If this claim cannot be verified from the provided evidence, the scientific contribution is not established.
- **Resolution test** Provide the full comparison tables with performance metrics for all methods on all datasets, including confidence intervals or statistical tests (e.g., DeLong test for AUC differences).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** The authors state that the first task model combines CNN and BiLSTM with evolutionary and multimodal features, and that the second task model uses XGBoost with 37 physicochemical properties following a three-step feature selection.
- **Evidence pointer** Section "Model architectures"; Section "Feature extraction"; Figure 1
- **Concern** The description of the model architecture is incomplete. Key details are missing: the exact architecture of the CNN (number of layers, kernel sizes, pooling strategy), the BiLSTM configuration (number of units, dropout), the fusion mechanism for combining the two branches, the training procedure (optimizer, learning rate, batch size, epochs, early stopping criteria), and the handling of variable-length sequences. For the second task, the three-step feature selection is described but the criteria for selecting the optimal feature subset are not fully specified. The text mentions "Feature_importances" from XGBoost but does not explain how the step size of 5 was chosen or whether this selection was performed on the training set only to avoid leakage.
- **Why it matters** Reproducibility is a fundamental requirement for computational biology tools. Without complete architectural and training details, other researchers cannot implement or validate the method.
- **Resolution test** Provide a complete specification of both models, including all hyperparameters, training procedures, and feature selection protocols. Ideally, provide the code with documentation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and benchmarking validity
- **Claim pointer** The authors state that the positive dataset contains 798 LLPS proteins after redundancy removal at 40% similarity, and that the negative dataset was constructed from the PDB* dataset with the same number of sequences.
- **Evidence pointer** Section "Data collection and preprocessing"; Table 1
- **Concern** Several critical details are missing. First, the exact composition of the positive dataset from each source database (LLPSDB2.0, PhaSePro, PhaSepDB2.1, DrLLPS) is not provided. Second, the construction of the negative dataset is described only briefly: it is unclear how proteins were selected from PDB*, whether they were filtered for known non-LLPS status, and whether any functional annotation was used. Third, the text mentions that 17 "confusing proteins" were omitted but does not define what constitutes a confusing protein. Fourth, the split between training and test sets for the first task model is not described. Finally, the independent test datasets (SaPS_Test, PdPS_Test, Ind_Test_I, Ind_Test_II) are referenced but their composition and size are not given in the text.
- **Why it matters** The validity of any machine learning prediction tool depends critically on the quality and construction of training and test data. If the negative set is not carefully curated, the model may learn trivial discriminative features. If test sets are not truly independent, reported performance may be optimistically biased.
- **Resolution test** Provide a detailed description of dataset construction, including source breakdown, filtering criteria, redundancy removal, and the exact composition of all training and test sets. Clarify the definition of "confusing proteins" and justify their exclusion.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability claim
- **Claim pointer** The authors state that in silico saturation mutagenesis was used to identify regions that play a key role in phase separation, and that cysteine, glycine, and proline show distinct importance patterns.
- **Evidence pointer** Section "Interpretable analysis of region importance"; Figure 6A–B
- **Concern** The interpretability analysis is described at a high level but lacks methodological detail. The text states that each amino acid was mutated to the other 19 alternatives and the probability difference was used as an importance score, but it does not specify which model was used for prediction (first or second task), how the scores were aggregated across mutations, or how statistical significance was assessed. The claim that cysteine "exhibited the widest influence" and that proline showed "negligible impact" is presented without quantitative support or comparison to a null distribution. The statement that the importance scores at positions 15, 17, and 19 are "more pronounced" is not backed by any statistical test.
- **Why it matters** The interpretability analysis is presented as a key contribution of the work. If the methodology is not rigorous, the biological conclusions drawn from it are not reliable.
- **Resolution test** Provide a detailed description of the ISM methodology, including the model used, the aggregation of scores, and statistical testing. Show quantitative results with error bars or confidence intervals.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Novelty claim
- **Claim pointer** The authors state that "for the first time, a special model was established to distinguish between PS-Self and PS-Part proteins."
- **Evidence pointer** Section "Introduction"; Section "Materials and methods"
- **Concern** This claim appears to be contradicted by the authors' own citation of PhaSePred, which is described as "the first predictor of self-assembling proteins (PS-Self) and partner-dependent proteins (PS-Part)." If PhaSePred already performs this distinction, then the claim of being the first is inaccurate. The novelty may lie in the specific approach or features used, but this is not clearly articulated.
- **Why it matters** Accurate novelty claims are essential for scientific integrity. An overstated claim undermines the credibility of the work.
- **Resolution test** Revise the novelty claim to accurately reflect the contribution, e.g., "the first to combine evolutionary and multimodal features in a two-task framework for this distinction" or similar.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the model was "validated on multiple benchmark datasets" but does not mention the comparison with existing methods or the key performance results. This makes it difficult for readers to assess the significance of the work from the abstract alone.
- **Required correction** Include a brief summary of the comparison results and the main performance metrics in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Feature extraction
- **Evidence pointer** Section "Feature extraction"
- **Issue** The formula for AAC is referenced but not shown in the text. The AAIndex_AAC formula is also referenced but not displayed. This makes it difficult to understand the exact feature construction.
- **Required correction** Include the actual formulas in the text or as numbered equations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Comparison with existing methods
- **Evidence pointer** Section "Comparison with other state-of-the-art methods on independent datasets"
- **Issue** The text reports AUC values for Opt_PredLLPS but does not report the corresponding values for the competing methods in the main text. It is unclear whether the improvements are statistically significant.
- **Required correction** Report the performance of all methods in the main text or provide a summary table, and include statistical significance testing.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Interpretability analysis
- **Evidence pointer** Section "Interpretable analysis of region importance"
- **Issue** The text states that the sequence was partitioned into 50 segments and then into 25 segments, but the relationship between these two analyses is not clearly explained. It is unclear whether the 25-segment analysis is a refinement of the 50-segment analysis or a separate analysis.
- **Required correction** Clarify the relationship between the two partitioning schemes and the purpose of each.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Section "Data availability"
- **Issue** The data availability statement provides a GitHub link but does not specify the license, the exact contents of the repository, or whether the code is documented and runnable.
- **Required correction** Provide a more detailed data availability statement, including the license and a description of the repository contents.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Location not provided
- **Issue** The manuscript contains several instances of awkward phrasing and grammatical errors (e.g., "the undergo of PS," "the reasons for the significant differences observed between PS-Self and PS-Part proteins remain unclear, necessitating separate consideration of these two types of phase separation proteins in further research"). These do not impede understanding but detract from readability.
- **Required correction** Perform a thorough language edit to improve clarity and fluency.

## Risk / unsupported claims
- The claim of being the "first" model to distinguish PS-Self and PS-Part proteins is contradicted by the authors' own citation of PhaSePred and is therefore unsupported.
- The claim that Opt_PredLLPS outperforms six state-of-the-art methods cannot be verified from the provided text, as the comparison data are only in figures and supplementary tables not included in the review materials.
- The biological conclusions drawn from the ISM analysis (e.g., cysteine having the widest influence, proline having negligible impact) are presented without quantitative support or statistical testing and are therefore not established.
- The statement that the integration of two components "minimizes the risk of overfitting" is not supported by any explicit overfitting analysis (e.g., training vs. validation performance curves).
- The claim that the model's effectiveness is "confirmed across various benchmark datasets" is weakened by the lack of detailed performance metrics in the text.