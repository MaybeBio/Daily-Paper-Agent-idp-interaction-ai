## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability)
- **Assessment boundary** Scientific and technical evaluation of the presented method, experimental design, results, and claims; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors present IDPFunNet, a hybrid deep learning model combining CNN, BiLSTM, residual MLP, and ProtT5 protein language model embeddings to predict six IDR functional classes (five binding subtypes and disordered flexible linkers). They claim state-of-the-art performance across six independent benchmarks including CAID2/3 blind tests, with ProtT5 embeddings outperforming ESM-family models and AlphaFold2 structural features. They further claim that multi-task learning enhances binding prediction, BiLSTMs are optimal for DFL identification, and self-attention shows potential for nucleic acid-binding.
- **Visible evidence base** Full manuscript text including methods, results narrative, and figure references; no actual figures, tables, or supplementary materials were provided for inspection
- **Missing materials affecting confidence** All figures (Figs 1-7), all supplementary materials (Supplementary Tables 1-5, Supplementary Figs 1-6, Supplementary Notes 1-6), actual performance data tables, and the underlying code/datasets. Without these, quantitative claims cannot be independently verified.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant and timely problem in IDP/IDR functional annotation, and the proposed dual-path architecture with ProtT5 embeddings is a reasonable design choice. However, the provided text alone is insufficient to evaluate the validity of the central performance claims. Key quantitative results, statistical analyses, and methodological details are referenced but not visible. The claims of state-of-the-art performance and the specific advantages attributed to ProtT5, multi-task learning, and the dual-path architecture require access to the actual data and figures to be assessed. The manuscript structure is logical and the writing is generally clear, but the evidence base as presented is incomplete for a rigorous scientific evaluation.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those focused on intrinsically disordered proteins and regions. Researchers developing deep learning methods for biological sequence analysis would also be interested in the comparative evaluation of protein language models and the architectural insights regarding CNN-BiLSTM hybrids versus pure BiLSTM or attention-based designs. The practical availability of a webserver and standalone package increases the potential utility for the broader IDP research community.

- **Major strengths**
  1. The problem is well-motivated: IDR functional annotation is a genuine gap, and the focus on multiple binding subtypes plus DFLs is more comprehensive than many existing tools.
  2. The dual-path architecture is a thoughtful design that explicitly addresses the potential negative transfer between binding and DFL prediction tasks.
  3. The systematic ablation studies (CNN vs BiLSTM, ProtT5 vs ESM vs AF2, single- vs multi-task, attention variants) are a commendable approach to understanding model design choices.
  4. Evaluation across multiple independent benchmarks including CAID blind tests is appropriate and strengthens the generalizability claims.
  5. The manuscript is clearly written and the logical flow from motivation to design to evaluation is easy to follow.

- **Major Concerns**

  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence completeness
  - **Claim pointer** "IDPFunNet achieves state-of-the-art performance" and "consistently surpasses existing general predictors DisoFLAG and DeepDISOBind in protein-binding prediction"
  - **Evidence pointer** Results section, Fig. 6, Supplementary Figs 2-3, Supplementary Tables 3-4
  - **Concern** The central performance claims are presented in the text but the actual quantitative results are not visible in the provided material. No performance numbers, error bars, or statistical comparison tables are available for inspection. The reader is asked to accept the conclusions based on references to figures and tables that are not included.
  - **Why it matters** The primary contribution of this work is the claimed performance improvement over existing methods. Without access to the actual data, the validity of these claims cannot be assessed. The manuscript's scientific value hinges entirely on these results being correct and statistically robust.
  - **Resolution test** Provide the actual performance tables (Supplementary Tables 3-4) and figures (Fig. 6, Supplementary Figs 2-3) with all numerical values, standard deviations, and statistical significance indicators. The claims can then be verified against the reported data.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor
  - **Claim pointer** "representing significant gains of 1.5%–8.1% in AUC and 13.5%–26.7% in APS (p-value < 0.05)"
  - **Evidence pointer** Results section, Fig. 6, Supplementary Table 4
  - **Concern** The statistical significance testing methodology is not described in the visible text. The bootstrap resampling framework is mentioned in the methods, but the specific hypothesis tests, multiple comparison corrections, and how the p-values were derived are not detailed. With multiple metrics and multiple comparators across multiple datasets, the risk of false positives from multiple testing is substantial.
  - **Why it matters** The claim of statistical significance is a key part of the evidence for superiority. Without a clear description of the testing procedure and appropriate corrections, the p-values reported cannot be interpreted reliably.
  - **Resolution test** Provide a complete description of the statistical testing procedure, including the exact test used, how multiple comparisons were handled, and the full distribution of p-values across all comparisons. Ideally, provide effect sizes and confidence intervals in addition to p-values.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological completeness
  - **Claim pointer** "Leveraging ProtT5 evolutionary embeddings, which outperformed ESM-family models and AlphaFold2 structural features (by ≥1.3% average AUC and ≥12.7% average APS)"
  - **Evidence pointer** Methods section, Supplementary Notes 3-4, Fig. 3
  - **Concern** The comparison between ProtT5, ESM-family models, and AF2 features is a central methodological claim, but the details of how these alternative features were integrated and evaluated are not visible. The hyperparameters, training procedures, and evaluation protocols for each variant are not described in the main text. Without this information, it is impossible to determine whether the comparison is fair and whether the conclusions are justified.
  - **Why it matters** The choice of feature representation is a key design decision, and the claim that ProtT5 is superior to alternatives is a significant part of the paper's contribution. If the comparison is not conducted fairly, the conclusion may not hold.
  - **Resolution test** Provide full details of the feature comparison experiments, including how each feature type was computed, integrated into the model, and evaluated. Describe the hyperparameter tuning process for each variant to ensure a fair comparison.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Dataset representativeness
  - **Claim pointer** "we collected 83 newly deposited sequences from the DisProt database, which were added after version 9.4 but before version 9.6"
  - **Evidence pointer** Methods section, Benchmark datasets
  - **Concern** The TE83 dataset is described as newly deposited sequences, but the temporal gap between the training data (DisProt 9.4) and this test set is not quantified. If the new sequences are highly similar to training sequences, the evaluation may overestimate generalization. Additionally, the class distribution and annotation quality of TE83 are not described.
  - **Why it matters** The claim of cross-dataset generalization depends on the independence and representativeness of the test sets. If TE83 is too similar to training data or has different annotation characteristics, the results may not reflect true generalization performance.
  - **Resolution test** Provide a detailed characterization of TE83, including sequence identity distribution to training data, annotation sources, and class balance. Consider reporting performance stratified by sequence similarity to training data.

  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Comparison fairness
  - **Claim pointer** "we retrained DisoFLAG and DeepDISOBind on our datasets (DisoFLAG* and DeepDISOBind*)"
  - **Evidence pointer** Results section, Supplementary Note 6, Supplementary Fig. 6
  - **Concern** The retraining procedure for comparison methods is not described in the visible text. The hyperparameters, training epochs, and whether the original training protocols were followed are unknown. If the retrained models are not optimally configured, the comparison may be biased in favor of IDPFunNet.
  - **Why it matters** Fair comparison with existing methods is essential for the claim of state-of-the-art performance. If the comparison methods are not given sufficient training resources or hyperparameter tuning, the results may not reflect their true capabilities.
  - **Resolution test** Provide full details of the retraining procedure for each comparison method, including hyperparameter search, training epochs, and any modifications to the original architecture. Ideally, compare against the original published models as well as retrained versions.

- **Minor Comments**

  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Model architecture description
  - **Evidence pointer** Methods section, Model architecture
  - **Issue** The description of the model architecture is high-level and lacks specific details on layer sizes, dropout rates, activation functions, and other hyperparameters. The reference to Supplementary Table 2 for "complete specification" is noted, but the main text should provide sufficient detail for a reader to understand the model without consulting supplementary materials.
  - **Required correction** Include a brief summary of key architectural hyperparameters in the main text, such as the number of CNN layers, kernel sizes, LSTM hidden dimensions, and the structure of the ResMLP blocks.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Training procedure
  - **Evidence pointer** Methods section, Training process
  - **Issue** The training procedure is described only briefly. Details on batch size, number of epochs, learning rate scheduling, early stopping criteria, and computational resources are not provided in the visible text.
  - **Required correction** Add a subsection describing the training procedure in detail, including all hyperparameters, optimization settings, and hardware used.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Result interpretation
  - **Affected element** Attention mechanism analysis
  - **Evidence pointer** Results section, Performance of attention mechanism
  - **Issue** The claim that "self-attention shows potential for nucleic acid-binding" is based on a single comparison (MHAmod achieving AUC 0.831 for nucleic acid binding). The text does not discuss whether this advantage is consistent across datasets or whether it is statistically significant.
  - **Required correction** Provide additional analysis of the attention mechanism's performance on nucleic acid binding, including results on both TE210 and TE83, and statistical significance testing.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Figure references
  - **Evidence pointer** Throughout Results section
  - **Issue** The text frequently references figures and supplementary materials that are not available in the provided material. While this is expected for a manuscript, the text should be self-contained enough for a reader to understand the main findings without constantly referring to figures.
  - **Required correction** Consider adding a brief summary of key numerical results in the text for each major comparison, in addition to the figure references.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "IDP functions" vs "IDR functions"
  - **Evidence pointer** Title, Abstract, throughout
  - **Issue** The title refers to "IDP functions" but the abstract and methods focus on IDR functions. While related, these are distinct concepts (intrinsically disordered proteins vs intrinsically disordered regions). The terminology should be consistent throughout.
  - **Required correction** Ensure consistent use of terminology, either "IDP functions" or "IDR functions," throughout the title, abstract, and main text.

- **Technical failings that need to be addressed before the case is established**
  1. The central performance claims cannot be verified without access to the actual data tables and figures (R1-M1).
  2. The statistical testing methodology is not described in sufficient detail to assess the validity of the reported p-values (R1-M2).
  3. The feature comparison experiments (ProtT5 vs ESM vs AF2) lack methodological detail to ensure a fair comparison (R1-M3).

- **Assessment against Nature-style criteria**
  - **Originality** The dual-path architecture separating binding and DFL prediction is a reasonable design choice, but the individual components (CNN, BiLSTM, ProtT5) are all established techniques. The originality lies primarily in the combination and systematic evaluation, which is moderate. The claim that this is the first to systematically evaluate these design choices for IDR function prediction is plausible but not fully verifiable from the provided text.
  - **Scientific importance** IDR functional annotation is an important problem in molecular biology, and improved prediction tools would be valuable. However, the incremental improvement over existing methods needs to be clearly demonstrated with robust evidence. The importance of the work depends on whether the claimed performance gains are real and substantial.
  - **Interdisciplinary readership** The work is primarily of interest to computational biologists and bioinformaticians. The methods section is technical and would be challenging for experimental biologists without computational background. The biological motivation is well-presented, but the technical depth limits the interdisciplinary appeal.
  - **Technical soundness** The overall approach is technically reasonable, but the lack of visible data and methodological details prevents a full assessment of technical soundness. The evaluation framework (multiple benchmarks, CAID blind tests) is appropriate, but the execution cannot be verified.
  - **Readability for nonspecialists** The abstract and introduction are accessible to a broad scientific audience. The methods and results sections are more technical and would require domain expertise to fully understand. The writing is clear and logical throughout.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an important problem with a reasonable approach, but the central claims of state-of-the-art performance cannot be verified without access to the actual data, figures, and methodological details. The authors should be encouraged to resubmit with the full evidence base available for review. If the reported results are accurate and the statistical analysis is sound, this could be a valuable contribution to the field.

## Risk / unsupported claims
- "IDPFunNet achieves state-of-the-art performance" - unsupported without access to actual performance data
- "consistently surpasses existing general predictors DisoFLAG and DeepDISOBind" - unsupported without access to comparison data
- "ProtT5 evolutionary embeddings outperformed ESM-family models and AlphaFold2 structural features" - unsupported without access to the comparison results
- "multi-task learning enhances protein/lipid/small molecule-binding" - unsupported without access to ablation study results
- "BiLSTMs are optimal for DFL identification" - unsupported without access to the relevant comparison data
- "self-attention shows potential for nucleic acid-binding" - unsupported without access to the relevant results
- "IDPFunNet thus provides an interpretable and generalizable framework" - the claim of interpretability is not substantiated in the visible text
- All specific performance numbers (AUC, APS, F1-max, MCC values) mentioned in the results section are unverifiable without the actual data tables