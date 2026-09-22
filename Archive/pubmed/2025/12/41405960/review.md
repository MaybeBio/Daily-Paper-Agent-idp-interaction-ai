## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusion sections. Figures and tables are referenced but not provided in full detail.
- **Assessment boundary** Scientific validity, methodological rigor, reproducibility, and clarity of claims. No assessment of editorial fit or journal-specific policy.
- **Shared manuscript claim summary** The authors propose a novel framework combining the ProtT5 protein language model with a KmerConv module and multi-head attention mechanism to predict liquid-liquid phase separation proteins. They claim superior performance over existing methods across multiple datasets, robust generalization across species, and provide biological validation through imaging and enrichment analyses.
- **Visible evidence base** Text descriptions of methods and results, including performance metrics (Accuracy, AUROC, PRAUC, MCC), cross-validation results, and qualitative descriptions of figures and tables. Specific numerical values are provided for some metrics.
- **Missing materials affecting confidence** Full figures and tables are not available in the provided text. Detailed hyperparameter settings, model architecture specifications (layer counts, hidden dimensions), and complete dataset composition are not fully described. The supplementary materials referenced are not accessible.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in computational biology with a reasonable methodological approach. The combination of a protein language model with local and global feature extraction modules is sensible and aligns with current trends in the field. However, several technical aspects require clarification and additional validation before the claims of superior performance and robustness can be fully established. The negative sample construction strategy is thoughtful but introduces potential biases that need more thorough discussion. The biological validation section is promising but currently lacks quantitative rigor.
- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics working on protein function prediction, particularly those focused on phase separation and membraneless organelles. The methodological framework may also interest those applying language models to biological sequence analysis. The predicted human proteome dataset could be a useful resource for the LLPS community.
- **Major strengths** The use of a two-step negative sample filtering strategy combining sequence similarity and imaging validation is a thoughtful approach to a known challenge in this field. The dual-model architecture is well motivated and the ablation study design is appropriate. The inclusion of multiple independent test datasets, including cross-species validation, strengthens the generalization claims. The biological validation through imaging and enrichment analyses adds practical relevance.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (dataset leakage), R1-M2 (baseline comparison fairness), R1-M3 (statistical rigor), R1-M4 (biological validation quantification).
- **Assessment against Nature-style criteria** **Originality**: Moderate. The combination of ProtT5 with KmerConv and attention is incremental over existing approaches, though the specific architecture is novel. **Scientific importance**: Moderate. LLPS prediction is an active area, but the methodological advance over existing tools appears incremental. **Interdisciplinary readership**: Limited. The work is primarily of interest to computational biologists; the biological validation is not deep enough to attract a broad biology audience. **Technical soundness**: Currently not fully established. Several methodological concerns need resolution. **Readability for nonspecialists**: Acceptable. The manuscript is generally clear, though some methods sections assume familiarity with deep learning concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core approach is promising, but the current evidence does not fully support the claims of superior performance and robustness.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data integrity and evaluation validity
- **Claim pointer** The authors claim the model achieves high predictive performance across multiple diverse datasets and generalizes effectively across different species.
- **Evidence pointer** Dataset construction section, Independent sample verification section, Table 3
- **Concern** The potential for data leakage between training and test sets is not adequately addressed. The authors state that "proteins included in both the training and test datasets were removed," but this only addresses exact sequence matches. Homologous proteins sharing significant sequence similarity could still appear in both sets, leading to inflated performance estimates. The manuscript does not describe any sequence similarity-based filtering (e.g., CD-HIT at a defined threshold) between training and test sets. This is particularly concerning for the cross-species validation, where homologous proteins across species could artificially boost generalization metrics.
- **Why it matters** Data leakage through sequence homology is a well-documented issue in protein function prediction. If homologs appear in both training and test sets, the reported performance metrics may not reflect true generalization to novel proteins, undermining the central claim of the manuscript.
- **Resolution test** Perform sequence similarity-based filtering between training and test sets (e.g., remove test proteins with >30% sequence identity to any training protein) and re-evaluate all reported metrics. Report performance on the filtered test sets and discuss any changes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparative evaluation validity
- **Claim pointer** The authors claim their model outperforms existing methods, including PSPHunter, across multiple datasets.
- **Evidence pointer** Benchmarking against existing predictors section, Figure 2D, Table 2
- **Concern** The comparison with existing methods appears potentially unfair. The authors compare their model against PSPHunter, SaPS, and PdPS, but the training conditions for these baseline methods are not described. If the baselines were not retrained on the same training data or were evaluated under different conditions, the comparison may not be meaningful. Additionally, the manuscript does not specify whether the baseline methods were used with their default parameters or optimized for the current datasets. The claim that PSPHunter shows "equivalent PRAUC" but lower Accuracy and MCC requires more context on how these metrics were computed for each method.
- **Why it matters** Unfair comparisons can lead to inflated claims of superiority. The central contribution of the manuscript is the claimed performance advantage over existing tools, and this must be demonstrated under controlled, equivalent conditions.
- **Resolution test** Describe the exact training and evaluation protocol for all baseline methods. Ideally, retrain all baselines on the same training data using their recommended procedures, and report performance on identical test sets. If retraining is not feasible, justify why the comparison remains valid.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors report performance metrics including Accuracy, AUROC, PRAUC, and MCC, and claim their model achieves state-of-the-art performance.
- **Evidence pointer** Model building section, Benchmarking against existing predictors section, Table 2, Table 4
- **Concern** The manuscript reports point estimates of performance metrics without confidence intervals or statistical significance testing. For a classification task with imbalanced datasets (as acknowledged for G3BP1 and RNAgranuleDB), single-point estimates can be misleading. The cross-validation results are mentioned but not fully reported with variance measures. The claim of "state-of-the-art performance" requires statistical support demonstrating that observed differences are not due to chance.
- **Why it matters** Without measures of uncertainty, readers cannot assess the reliability of the reported performance differences. This is particularly important when comparing methods where small differences in metrics may not be meaningful.
- **Resolution test** Report confidence intervals (e.g., bootstrap or across cross-validation folds) for all primary metrics. Perform statistical significance testing (e.g., McNemar's test for paired comparisons) between the proposed model and baselines. Report the variance across cross-validation folds.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological validation rigor
- **Claim pointer** The authors claim that imaging validation of high-prediction-score proteins revealed droplet-like aggregates consistent with LLPS characteristics, and that enrichment analyses corroborate the findings.
- **Evidence pointer** Relevant verification section, Figure 5, Figure 6
- **Concern** The biological validation is described qualitatively. The manuscript states that several proteins exhibited droplet-like structures, but does not provide quantitative measures such as the number of proteins examined, the proportion showing expected phenotypes, or comparison with negative controls. The enrichment analyses are described as "highly consistent" but no statistical measures (e.g., enrichment p-values, false discovery rates) are reported. The selection of the 128 candidate proteins (score > 0.985) is not justified.
- **Why it matters** The biological validation is presented as supporting evidence for the model's practical utility. Without quantitative rigor, this section reads as anecdotal and does not provide strong independent validation of the computational predictions.
- **Resolution test** Provide quantitative summary statistics for the imaging validation (e.g., number of proteins tested, proportion with droplet-like phenotypes, comparison with low-scoring controls). Report enrichment analysis results with statistical significance measures. Justify the score threshold used for candidate selection.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Model architecture description
- **Evidence pointer** Deep learning model building section
- **Issue** The model architecture is described at a high level, but specific details such as the number of attention heads, hidden layer sizes, dropout rates, and the exact structure of the KmerConv module are not provided. The training procedure mentions 50 epochs and the Adam optimizer, but learning rate schedules, batch sizes, and early stopping criteria are not described.
- **Required correction** Provide a complete specification of the model architecture and training hyperparameters, either in the main text or as a supplementary table. This is essential for reproducibility.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Negative sample construction
- **Evidence pointer** Data collection and collation section
- **Issue** The description of the negative sample filtering is somewhat unclear. The text states that 1,338 proteins with available images were examined, and 717 showed fully diffuse distribution. It is not clear how these 717 proteins relate to the 5,754 retained after CD-HIT filtering, or how the final negative set was constructed from these candidates.
- **Required correction** Clarify the step-by-step process of negative sample construction, including the number of proteins at each filtering stage and how the final negative set was selected.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure and table references
- **Evidence pointer** Throughout the manuscript
- **Issue** The manuscript references figures and tables extensively, but the actual content of these items is not available in the provided text. Some references are unclear, such as "Fig. 2B" being described as showing the model architecture while also being referenced in the results section for performance comparisons.
- **Required correction** Ensure all figure and table references are accurate and that the figures/tables are self-explanatory when viewed independently of the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Language and style
- **Affected element** Abstract and conclusion
- **Evidence pointer** Abstract, Conclusions
- **Issue** The abstract and conclusion contain some vague phrasing, such as "robust and efficient tool" and "novel insights," which are not fully supported by specific quantitative claims. The conclusion also introduces the limitation of negative control selection bias, which is appropriate, but this discussion could be more balanced with a discussion of the model's limitations in general.
- **Required correction** Strengthen the abstract and conclusion with specific quantitative results and a more balanced discussion of limitations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability section
- **Evidence pointer** Data availability section
- **Issue** The data availability statement mentions supplemental files and a GitHub repository, but the repository link is provided without a version or access date. It is unclear whether the code and data are publicly accessible at the time of submission.
- **Required correction** Provide a clear statement of data and code availability, including any access restrictions and a versioned release of the code repository.

## Risk / unsupported claims
- The claim of "state-of-the-art performance" is not fully supported without statistical significance testing and fair baseline comparisons.
- The claim of "generalizes effectively across different species" is weakened by the lack of sequence similarity-based filtering between training and test sets.
- The biological validation claims are qualitative and lack quantitative measures.
- The claim that the method "simplifies feature engineering" is not directly demonstrated, as no comparison of engineering effort or computational cost is provided.
- The performance on the non-human dataset is reported as "slightly lower than PSPHunter," which is acknowledged, but the implications for the claimed robustness are not fully discussed.
- The enrichment analysis results are described as "highly consistent" without statistical measures, making this claim unverifiable from the provided text.