## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, supplementary file descriptions)
- **Assessment boundary** Scientific validity, methodological soundness, clarity of claims, and reproducibility based solely on the provided text
- **Shared manuscript claim summary** The authors propose a machine learning approach using logistic regression and several sequence-derived scoring functions to predict whether a protein sequence will undergo liquid-liquid phase separation (LLPS). They report AUC values around 0.84 for their best-performing scores (s3 and s4), which outperform the existing Vernon score on their dataset.
- **Visible evidence base** Abstract, Introduction, Results and Discussion, Materials and Methods (partial), Supplementary file descriptions
- **Missing materials affecting confidence** Full equations for scoring functions (Eqs. 1-5 are referenced but not displayed), Figures 1-3 and Tables 1-2 are referenced but not provided, detailed statistical outputs, complete methods for parameter optimization, and the actual datasets

## Reviewer

- **Overall assessment** The manuscript addresses an important and timely problem in the field of biomolecular condensates, namely the sequence-based prediction of protein phase separation. The authors combine existing scoring functions (PASTA, Vernon) with new sequence-derived features and apply logistic regression with AUC optimization. However, the manuscript in its current form has several critical weaknesses. The scoring functions are not explicitly defined in the text, the statistical analysis is incomplete, and the class imbalance problem (121 positive vs 43515 negative) is acknowledged but not adequately addressed. The claim that the negative set "do not undergo phase separation" is problematic, as the authors themselves state in the supplementary description that these proteins' phase separation behavior is "unknown or is assumed" to be negative. This fundamental labeling issue undermines the validity of the supervised learning approach. The manuscript would benefit from clearer presentation of the methods, more rigorous validation, and a more careful discussion of the limitations.

- **Who would be interested in the results, and why** Researchers in the fields of protein biophysics, computational biology, and cell biology, particularly those studying liquid-liquid phase separation, intrinsically disordered proteins, and membraneless organelles. The work could also be of interest to the machine learning community working on biological sequence classification problems. The potential practical application of predicting phase-separating proteins from sequence alone would be valuable for prioritizing candidates for experimental validation.

- **Major strengths**
  1. The problem addressed is of high current interest and biological importance.
  2. The authors build on established scoring functions (PASTA, Vernon) and extend them with additional sequence features.
  3. The use of cross-validation with multiple realizations is appropriate for assessing model stability.
  4. The work is accompanied by publicly available data and code, which supports reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data quality and labeling validity
- **Claim pointer** The authors claim that the negative set consists of proteins that "do not undergo phase separation" (Results section) and use these as negative examples in supervised learning.
- **Evidence pointer** Results and Discussion; Supplementary file 2 description
- **Concern** The negative set is described inconsistently. In the Results, the authors state the 43515 Human Proteome sequences "do not undergo phase separation," but in the supplementary file description, they state that the phase separation behavior of these proteins is "unknown or is assumed" to be negative. This is a critical distinction. If the negative labels are based on assumption rather than experimental evidence, the training labels are unreliable, and the model may be learning to distinguish known phase-separating proteins from a general protein population, which is a different and less well-defined task. This issue fundamentally affects the interpretation of all reported performance metrics.
- **Why it matters** Supervised learning requires reliable labels. If the negative set contains proteins that actually do phase separate (which is likely given the growing number of discovered phase-separating proteins), the model's performance metrics (AUC, MCC) are not trustworthy, and the model may not generalize to real-world prediction tasks.
- **Resolution test** The authors must clarify the provenance of the negative labels. If experimental evidence is not available for all 43515 proteins, they should either (a) use a curated negative set with experimentally verified non-phase-separating proteins, (b) reframe the problem as anomaly detection or ranking rather than binary classification, or (c) explicitly acknowledge and discuss the label uncertainty and its potential impact on results.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The authors define five scoring functions (s0 through s4) and state that they are "defined as following" (Results and Discussion), but the actual equations are not provided in the manuscript text.
- **Evidence pointer** Results and Discussion, paragraph 3; Eqs. (1)-(5) referenced but not displayed
- **Concern** The scoring functions are the core methodological contribution of this work, yet their explicit mathematical forms are absent from the manuscript. The reader cannot evaluate the novelty,合理性, or biological rationale of these functions without seeing them. This is a fundamental omission that prevents assessment of the work's technical soundness.
- **Why it matters** Without the explicit definitions, the work cannot be reproduced, evaluated, or compared with other methods. The scientific contribution is not assessable in its current form.
- **Resolution test** Provide the complete equations for s0 through s4 in the main text or a clearly referenced supplement. Each term should be defined, and the biological or physical rationale for including each feature should be stated.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Class imbalance and metric interpretation
- **Claim pointer** The authors report AUC values around 0.84 for their best scores and acknowledge that MCC is low due to the large negative set size.
- **Evidence pointer** Results and Discussion, paragraph 5; Table 2 (referenced)
- **Concern** With a positive-to-negative ratio of 121:43515 (approximately 1:360), the class imbalance is extreme. The authors correctly note that MCC approaches zero in this regime, but they do not address the implications for AUC. AUC can be misleadingly high in imbalanced settings if the model simply ranks the few positives reasonably well, even if the absolute number of false positives is very large. The practical utility of a classifier with AUC 0.84 but very low MCC needs to be discussed in terms of expected precision and recall at an operating point relevant to users.
- **Why it matters** The reported performance metric (AUC) may not reflect the practical usefulness of the predictor. A user applying this tool to a proteome would need to know the expected false positive rate at a given sensitivity threshold.
- **Resolution test** Report precision-recall curves, precision at fixed recall levels, or the expected number of false positives per true positive at a chosen operating threshold. Discuss the practical implications of the class imbalance for real-world use.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor and comparison
- **Claim pointer** The authors state that "AUC values for all the scoring functions are statistically significant from each other" based on one-way ANOVA, but that s3 and s4 are not significantly different from each other.
- **Evidence pointer** Results and Discussion, paragraph 4; Table 1 (referenced)
- **Concern** The use of one-way ANOVA on AUC values from cross-validation realizations is statistically questionable. AUC values from different folds of the same data are not independent, and the distributional assumptions of ANOVA may not hold. Furthermore, the authors do not report effect sizes, confidence intervals, or multiple comparison corrections. The claim that scores are "statistically significant from each other" is vague and not supported by the information provided.
- **Why it matters** The statistical comparison is used to justify the choice of the best-performing score. If the statistical analysis is flawed, the conclusion that s3 and s4 are the best may not be well-supported.
- **Resolution test** Use appropriate statistical tests that account for the non-independence of cross-validation folds (e.g., paired tests, corrected resampled t-tests). Report effect sizes and confidence intervals. Clarify what "statistically significant" means in this context.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalization and external validation
- **Claim pointer** The authors claim their scores are better predictors than the Vernon score on their dataset.
- **Evidence pointer** Results and Discussion, final paragraph; Figure 3 (referenced)
- **Concern** All evaluation is performed on the same dataset used for training (via cross-validation). No external validation on independent datasets is provided. The Human Proteome negative set is used both for training and testing, and the positive set is small (121 proteins). It is unclear whether the reported performance would generalize to other organisms, to proteins with different functions, or to experimentally validated phase-separating proteins not in the training set.
- **Why it matters** For a prediction tool to be useful, it must generalize beyond the training data. Without external validation, the practical value of the proposed scores is unproven.
- **Resolution test** Validate the best-performing scores on independent datasets of experimentally verified phase-separating and non-phase-separating proteins. If such datasets are not available, this limitation should be explicitly acknowledged and discussed.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, first sentence
- **Issue** The abstract contains a typographical error: "neuro-degenrerative" should be "neurodegenerative." Additionally, the abstract is written in a somewhat informal style ("We in this research build a predictor") that is not typical for a scientific manuscript.
- **Required correction** Correct the typo and revise the abstract to use more formal scientific language.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Materials and Methods, Register shift definition
- **Evidence pointer** Materials and Methods, "Register shift and PASTA score" section
- **Issue** The definition of register shift S is incomplete. The text states "the register shift S is defined as" but the actual formula is not provided. The description of how S is computed from the indices is also unclear.
- **Required correction** Provide the explicit formula for S and a clear explanation of how it is calculated from the best pairing indices.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data description
- **Affected element** Supplementary materials
- **Evidence pointer** Supplementary file descriptions
- **Issue** The description of the negative set is inconsistent (as noted in R1-M1). Additionally, the criteria for inclusion in the positive set (121 PhasePro proteins) are not described. How were these proteins selected? What experimental evidence supports their phase-separating behavior?
- **Required correction** Provide clear criteria for inclusion in both the positive and negative sets, including references to experimental evidence where available.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of results
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion, paragraph 3
- **Issue** The manuscript states "we report the performances of a total of 5 scoring functions, which are defined as following:" but the equations are missing. This is a major omission (see R1-M2), but even the surrounding text is unclear about what the variables (E, V, N, S, lp) represent in the context of each score.
- **Required correction** Provide the equations and clearly define all variables in the text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reference formatting
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** References are cited in a non-standard format (e.g., "[ 1 ]" with spaces). The manuscript should use a consistent citation style.
- **Required correction** Format references consistently according to the target journal's style.

## Risk / unsupported claims
- The claim that the negative set proteins "do not undergo phase separation" is unsupported, as the authors themselves acknowledge that this behavior is "unknown or is assumed" for these proteins.
- The claim that s3 and s4 are the best-performing scores is based on statistical analysis that is not fully described and may be methodologically flawed.
- The claim that the proposed scores are better predictors than the Vernon score is only supported on the authors' own dataset and has not been externally validated.
- The performance metrics (AUC ≈ 0.84) are reported without adequate discussion of the extreme class imbalance and its implications for practical use.
- The biological rationale for the specific combination of features in the scoring functions is not explained, making it difficult to assess whether the approach captures meaningful biophysical principles.