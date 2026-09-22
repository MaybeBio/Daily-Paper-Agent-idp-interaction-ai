## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusion, data/code availability) as provided
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and presentation as presented in the supplied text
- **Shared manuscript claim summary** The authors present MPBind, a multitask deep learning method that integrates protein language models (PLMs) and equivariant graph neural networks (EGNNs) to predict five types of protein binding sites (protein, DNA/RNA, ligand, lipid, ion) from protein sequences and structures. They claim MPBind outperforms both general multitask methods (e.g., PeSTo) and task-specific methods (e.g., ScanNet, CLAPE, LMetalSite, GraphBind) across all binding site types, and that predictions on human proteome data align with UniProt functional annotations.
- **Visible evidence base** Abstract, Introduction, Methods (Sections 2.1–2.5), Results (Sections 3.1–3.5), Conclusion, Data/Code availability statements. Figures and tables are referenced but not provided. Supplementary tables (S1, S2) and figures (S1–S3) are referenced but not provided.
- **Missing materials affecting confidence** Figures 1–6, Tables 1, Supplementary Tables S1–S2, Supplementary Figures S1–S3, full training/validation details, hyperparameters, and exact dataset splits are not provided. This limits verification of quantitative claims and architectural details.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in structural bioinformatics: multitask prediction of protein binding sites across five interaction types. The proposed architecture combining PLMs and EGNNs is reasonable and timely. However, the evidence provided is insufficient to fully evaluate the claims. Key quantitative results are only summarized in text without access to figures or tables, and several methodological details are missing. The claim of outperforming both general and task-specific methods requires careful statistical validation, which is not fully visible. The human proteome analysis is descriptive and lacks statistical rigor. The manuscript has potential but requires substantial revision and additional evidence to support its conclusions.
- **Who would be interested in the results, and why** Computational biologists, bioinformaticians, and researchers in protein function prediction, drug discovery, and structural biology. The multitask approach and integration of PLMs with geometric deep learning may interest those developing general-purpose protein analysis tools. The human proteome analysis could appeal to researchers studying protein function at scale.
- **Major strengths** 1) Addresses a practical and timely problem with a multitask framework covering five binding site types. 2) Combines complementary information from two PLMs and EGNNs, a sensible architectural choice. 3) Uses a rigorous temporal split (Test2_data) to evaluate generalization to newer structures. 4) Includes an ablation study to justify feature choices. 5) Provides code and data availability statements.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing quantitative evidence), R1-M2 (statistical validation), R1-M3 (dataset leakage), R1-M4 (human proteome analysis rigor), R1-M5 (baseline comparability)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The combination of PLMs and EGNNs for multitask binding site prediction is a reasonable extension of existing work, but the novelty is incremental given prior multitask methods like PeSTo and task-specific methods like GraphBind. **Scientific importance**: High. Accurate binding site prediction is fundamental to understanding protein function and has broad applications. **Interdisciplinary readership**: Moderate. The work is primarily of interest to computational biologists and bioinformaticians; the biological insights from the human proteome analysis are limited. **Technical soundness**: Not fully assessable from the provided material. The architecture is plausible, but missing details on training, evaluation, and statistical testing prevent verification. **Readability for nonspecialists**: The introduction is accessible, but the methods section is dense and assumes familiarity with PLMs, EGNNs, and graph representations. Figures and tables are referenced but not provided, hindering comprehension.
- **Recommendation posture** Currently not established from the provided evidence. The core claims of superior performance and robust generalization cannot be verified without access to figures, tables, and statistical details. The manuscript is supportive in principle, but major revisions and additional evidence are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "MPBind outperforms both general bind site prediction methods and task-specific binding site prediction methods" (Abstract); "MPBind achieves ROC AUC and PR AUC scores of 0.83 and 0.54, respectively, substantially higher than 0.76 and 0.38 of PeSTo" (Section 3.1); "MPBind also consistently outperforms them across all types of binding site predictions" (Section 3.2)
- **Evidence pointer** Figures 2 and 3, Tables S1 and S2 (not provided)
- **Concern** The central quantitative claims are presented as text summaries without the actual figures or tables. The reader cannot verify the ROC curves, PR curves, or accuracy values. The magnitude of improvements (e.g., 0.83 vs 0.76 ROC AUC) is stated but not shown with confidence intervals or error bars. Without the visual evidence, the claims are unverifiable.
- **Why it matters** The primary contribution of the manuscript is the claimed performance advantage. If the figures and tables are not available, the core evidence is missing, and the claims cannot be assessed.
- **Resolution test** Provide Figures 2 and 3, and Tables S1 and S2, with clear axis labels, legends, and statistical annotations (e.g., confidence intervals, p-values) to support the stated performance differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** "MPBind achieves ROC AUC and PR AUC scores of 0.83 and 0.54, respectively, substantially higher than 0.76 and 0.38 of PeSTo" (Section 3.1); "MPBind also consistently outperforms them across all types of binding site predictions" (Section 3.2)
- **Evidence pointer** Sections 3.1 and 3.2, Figures 2 and 3 (not provided)
- **Concern** No statistical tests (e.g., bootstrap, permutation tests, or DeLong test for ROC AUC) are reported to assess whether the observed differences are significant. The term "substantially higher" is subjective without error bars or confidence intervals. The number of test chains varies across categories (e.g., 1,208 for protein-protein, 75 for DNA, 48 for RNA), and small sample sizes may inflate variance.
- **Why it matters** Without statistical validation, the claimed superiority could be due to chance, especially for categories with few test examples. This undermines the reliability of the conclusions.
- **Resolution test** Report confidence intervals or p-values for all performance metrics, and specify the number of test chains per category. Use appropriate statistical tests to compare MPBind with baselines.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Data leakage
- **Claim pointer** "The clustered chains were partitioned into training, validation, and test sets according to the exact same split used by PeSTo [11] such that the proteins between different sets have less than 30% sequence identity" (Section 2.1); "Since the proteins in Test2_data were released after the latest release date of the training/validation proteins of all the methods evaluated in this work and have <= 30% sequence identity with them, it is new for all the methods" (Section 2.1)
- **Evidence pointer** Section 2.1
- **Concern** The manuscript states that Test2_data is new for all methods, but it is unclear whether the baselines (PeSTo, ScanNet, CLAPE, LMetalSite, GraphBind) were retrained on the same training data or used as pre-trained models. If baselines were not retrained, their performance may be suboptimal, biasing comparisons. Additionally, the temporal split criterion (release date) may not fully prevent homology leakage if structures share functional domains or motifs.
- **Why it matters** Fair comparison is essential for the claim of outperforming baselines. If baselines are disadvantaged, the results are not convincing.
- **Resolution test** Clarify whether baselines were retrained on the same training set or used as-is. If used as-is, discuss potential biases. Perform an additional analysis controlling for sequence identity and structural similarity to ensure no leakage.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological validation
- **Claim pointer** "The results demonstrate that MPBind binding site predictions align well with the expected functional roles of the residues in the UniProt" (Section 3.4)
- **Evidence pointer** Section 3.4, Figures 5 and 6, Figures S1–S3 (not provided)
- **Concern** The human proteome analysis is descriptive. The manuscript reports proportions of UniProt features overlapping with predicted binding sites but does not provide statistical enrichment analysis (e.g., hypergeometric test, Fisher's exact test) or comparison to a null model. The claim of "align well" is not quantitatively supported.
- **Why it matters** The analysis is presented as validation of biological relevance, but without statistical rigor, it is anecdotal and does not strengthen the case for MPBind's utility.
- **Resolution test** Perform enrichment analysis with appropriate statistical tests and report effect sizes and p-values. Include a negative control (e.g., random predictions) to demonstrate specificity.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Baseline comparability
- **Claim pointer** "MPBind also consistently outperforms them across all types of binding site predictions" (Section 3.2)
- **Evidence pointer** Section 3.2, Figure 3 (not provided)
- **Concern** The baselines (CLAPE, LMetalSite, GraphBind) are task-specific and may have been trained on different datasets or with different evaluation protocols. The manuscript does not describe the training data or hyperparameters for these baselines, nor whether they were evaluated under identical conditions (e.g., same input features, same test set). This makes the comparison potentially unfair.
- **Why it matters** Inconsistent evaluation conditions can invalidate the comparative claims.
- **Resolution test** Provide detailed descriptions of baseline training and evaluation, and ensure identical test sets and metrics. If baselines were not retrained, discuss the implications.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.3, feature description
- **Evidence pointer** Section 2.3
- **Issue** The spatial orientation calculation is described as "calculated by , where Q i denotes the coordinates of i -th residue" but the formula is missing. This makes the feature description incomplete.
- **Required correction** Provide the full formula for spatial orientation and define all variables.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.5, evaluation metrics
- **Evidence pointer** Section 2.5
- **Issue** The accuracy equation is referenced but not shown. The text states "can be calculated by the following equation" but the equation is absent.
- **Required correction** Include the accuracy equation explicitly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 3.3, case studies
- **Evidence pointer** Section 3.3, Figure 4 (not provided)
- **Issue** The five case studies are described qualitatively without quantitative metrics (e.g., precision, recall at the case level). The selection criteria for these examples are not stated, which may introduce bias.
- **Required correction** Provide quantitative performance for each case and state how the examples were selected.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.1, dataset details
- **Evidence pointer** Section 2.1
- **Issue** The exact number of chains in training, validation, and test sets is not provided. The text mentions percentages (70%, 15%, 15%) but not absolute counts.
- **Required correction** Report the exact number of chains in each split.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Language
- **Affected element** Section 3.4, typo
- **Evidence pointer** Section 3.4
- **Issue** "predcted" should be "predicted".
- **Required correction** Correct the typo.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.4, architecture details
- **Evidence pointer** Section 2.4
- **Issue** The number of EGNN layers is stated as four, but the hidden dimensions, number of attention heads, and other architectural hyperparameters are not provided.
- **Required correction** Provide full architectural details for reproducibility.

## Risk / unsupported claims
- The claim that MPBind "outperforms both general bind site prediction methods and task-specific binding site prediction methods" is unsupported without access to Figures 2 and 3 and Tables S1 and S2.
- The claim that "MPBind binding site predictions align well with the expected functional roles of the residues in the UniProt" is unsupported without statistical enrichment analysis.
- The claim that Test2_data is "objective and rigorous" is weakened by the lack of detail on baseline training conditions and potential homology leakage.
- The ablation study results (Table 1) are referenced but not provided, making the claim that all five feature types are necessary unverifiable.
- The performance of MPBind on AlphaFold-predicted structures is mentioned in the Introduction but not evaluated in the Results, leaving this claim unsubstantiated.