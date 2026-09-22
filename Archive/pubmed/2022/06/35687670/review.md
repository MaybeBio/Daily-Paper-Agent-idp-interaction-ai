## Review setup
- **Input scope** Full manuscript text including Significance, Results, Discussion, Materials and Methods, and supplementary figure/figure legends references.
- **Assessment boundary** Scientific claims, methodology, data interpretation, and technical soundness as presented in the provided manuscript text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors present machine-learning models (SaPS and PdPS) that integrate multimodal features to predict two categories of phase-separating proteins: self-assembling and partner-dependent. They claim these models outperform existing predictors, particularly for partner-dependent proteins, and validate their utility on membraneless organelle (MLO) participant datasets. They also introduce a web server, PhaSePred, integrating multiple predictors.
- **Visible evidence base** Main text figures (Figs 1–5), supplementary figures (Figs S1–S5), datasets (S1–S8), and methodological descriptions in Materials and Methods.
- **Missing materials affecting confidence** Dataset files (S1–S8) were not provided for direct inspection. Supplementary figures were referenced but not available for detailed review. The web server was not accessed. Exact model hyperparameters, feature importance values, and full SHAP analysis outputs were not fully detailed in the text.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant gap in the phase separation prediction field by distinguishing self-assembling from partner-dependent proteins. The methodological approach is reasonable and the inclusion of multimodal features is a strength. However, several technical aspects require clarification and additional validation before the core claims can be fully supported. The experimental validation is limited to three proteins, and the generalizability of the models across diverse biological contexts remains uncertain.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and membraneless organelles would find this work useful. Computational biologists developing predictors for protein function would also be interested. The web server provides a practical tool for the broader cell biology community.
- **Major strengths** 1) Clear conceptual division of phase-separating proteins into two categories based on mechanism. 2) Integration of diverse feature types (sequence, structural, PTM, imaging) is a thoughtful approach. 3) Validation on multiple independent datasets, including MLO participant proteomes, strengthens the practical relevance. 4) The web server is a valuable community resource.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (dataset overlap and leakage), R1-M2 (class imbalance and negative set construction), R1-M3 (experimental validation scope), R1-M4 (SHAP interpretation and feature correlation).
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The two-category classification is a useful conceptual contribution, but the individual features and machine-learning approach are not entirely novel.  
  *Scientific importance*: Moderate to high. Improving prediction of partner-dependent proteins addresses a real need in the field.  
  *Interdisciplinary readership*: Moderate. The topic bridges computational biology and cell biology, but the technical detail may limit broader appeal.  
  *Technical soundness*: Needs improvement. Several methodological details require clarification and additional validation.  
  *Readability for nonspecialists*: Generally clear, though some sections (e.g., model training details) are dense.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is valuable, but the current evidence does not fully establish the claimed superiority of the models, particularly for partner-dependent proteins.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Data integrity and model validation  
- **Claim pointer** The authors claim that their models outperform existing predictors on independent test sets, including the PS-test set and MLO participant datasets.  
- **Evidence pointer** Results section "Datasets of PS-Self Proteins, PS-Part Proteins, and Non-PS Proteins"; Materials and Methods "Collecting PS and Background Proteins"  
- **Concern** The potential for data leakage between training and test sets is not adequately addressed. The authors state that CD-HIT with a 0.4 sequence identity cutoff was applied, but it is unclear whether this was done jointly across all datasets (training, test, and MLO participant sets) or separately. If the MLO participant datasets contain proteins with high sequence similarity to training proteins, the reported AUC values could be inflated. Additionally, the PS-test set (54 proteins) was derived from PhaSepDB but it is unclear whether these proteins were excluded from the training process entirely.  
- **Why it matters** Data leakage would compromise the validity of the reported performance metrics and the conclusion that the models generalize to unseen proteins.  
- **Resolution test** Provide a clear description of the sequence-similarity filtering process, including whether it was applied across all datasets jointly. Report the maximum sequence identity between training and test proteins. Recalculate AUC values after excluding any test proteins with >40% identity to training proteins.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Negative set construction and class imbalance  
- **Claim pointer** The authors state that 60,251 non-PS proteins were collected from 10 representative species and used as negative samples.  
- **Evidence pointer** Results section "Datasets of PS-Self Proteins, PS-Part Proteins, and Non-PS Proteins"; Materials and Methods "Collecting PS and Background Proteins"  
- **Concern** The construction of the negative set is not described in sufficient detail. It is unclear how "non-PS" status was determined. Proteins not yet annotated as phase-separating may still be capable of phase separation, leading to false negatives in the training data. Furthermore, the class imbalance is extreme (e.g., 128 positive vs. ~48,000 negative for SaPS training), which can bias model training and evaluation metrics. The authors do not report precision-recall curves or F1 scores, which are more appropriate than ROC-AUC under such imbalance.  
- **Why it matters** An unreliable negative set and unaddressed class imbalance could lead to overestimated model performance and poor real-world utility.  
- **Resolution test** Describe the criteria for defining non-PS proteins. Report precision-recall curves, F1 scores, and Matthews correlation coefficient for all models. Consider using a more balanced negative set or applying class-weighting techniques.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Experimental validation scope  
- **Claim pointer** The authors claim that experimental validation of DHX9, Ki-67, and NIFK demonstrates the effectiveness of their models.  
- **Evidence pointer** Results section "Experimental Validation of DHX9, Ki-67, and NIFK Show the Effectiveness of the SaPS and PdPS Models"; Figure 4  
- **Concern** Only three proteins were experimentally tested. DHX9 was selected because it was predicted by SaPS, PLAAD, and PScore, but the authors do not report how many proteins were in this intersection set or why DHX9 was chosen over others. Ki-67 and NIFK were selected from top-500 lists, but the selection criteria are not fully transparent. The negative controls (MBP and SUMO) are reasonable, but two negative controls are insufficient to establish specificity. The phase separation assays were performed in vitro with purified components, which may not reflect cellular conditions.  
- **Why it matters** The experimental validation is a key part of the claim that the models are practically useful. The current evidence is too limited to support broad conclusions about model effectiveness.  
- **Resolution test** Provide a more systematic selection process for experimental candidates. Test additional predicted positives and negatives. Include cellular validation (e.g., live-cell imaging) for at least one candidate. Report the full list of candidate proteins and their scores.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** SHAP interpretation and feature correlation  
- **Claim pointer** The authors use SHAP values to interpret model decisions and claim that Phos frequency is the most important feature.  
- **Evidence pointer** Results section "Model Explanation Using SHAP Value"; Figure 3C  
- **Concern** The SHAP analysis is performed on a single dataset (OpenCell nuclear punctae set). The authors note that IDR and LCR features are correlated with PLAAC and PScore, which could affect SHAP value interpretation. However, they do not formally test for multicollinearity or its impact on SHAP values. The claim that Phos frequency is "more important" may be an artifact of feature correlation or dataset-specific effects.  
- **Why it matters** If the feature importance interpretation is flawed, the biological conclusions drawn from the SHAP analysis (e.g., the role of phosphorylation) may be misleading.  
- **Resolution test** Perform SHAP analysis on multiple datasets. Conduct a correlation analysis of all features and report variance inflation factors. Consider using permutation-based feature importance as a complementary method.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of dataset definitions  
- **Affected element** Dataset S1  
- **Evidence pointer** Results section "Datasets of PS-Self Proteins, PS-Part Proteins, and Non-PS Proteins"  
- **Issue** The authors state that 658 proteins were collected from PhaSepDB, LLPSDB, and PhaSePro, but the overlap between these databases is not described. It is unclear how many proteins were unique to each database and whether redundant entries were removed before or after merging.  
- **Required correction** Provide a Venn diagram or table showing the overlap between databases. Describe the merging and deduplication process.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Model performance metrics  
- **Affected element** Table 1  
- **Evidence pointer** Results section "Models Integrating Multimodal Features Outperform Current Tools"  
- **Issue** The authors report AUC values but do not provide confidence intervals or statistical tests comparing their models to existing predictors.  
- **Required correction** Report 95% confidence intervals for all AUC values and perform a statistical test (e.g., DeLong test) for model comparisons.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Web server accessibility  
- **Affected element** PhaSePred web server  
- **Evidence pointer** Materials and Methods "Developing a Comprehensive Web Server"  
- **Issue** The web server URL is provided, but the authors do not state whether the server is freely accessible, what the expected response time is, or whether there are any usage restrictions.  
- **Required correction** Add a statement about accessibility and any usage policies.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Code availability  
- **Affected element** Model training code  
- **Evidence pointer** Materials and Methods "Constructing Machine-Learning Models"  
- **Issue** The authors do not state whether the model training code and feature calculation scripts are publicly available.  
- **Required correction** Provide a statement on code availability, ideally with a repository link.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Feature calculation details  
- **Affected element** Feature set  
- **Evidence pointer** Materials and Methods "Calculating PS-Related Properties at the Proteome Level"  
- **Issue** The authors list the tools used for feature calculation but do not specify the exact parameters or versions of these tools.  
- **Required correction** Provide version numbers and non-default parameters for all tools used.

- **Concern ID** R1-m6  
- **Severity** Minor  
- **Axis** Interpretation of PS-test results  
- **Affected element** Figure S2D  
- **Evidence pointer** Results section "Models Integrating Multimodal Features Outperform Current Tools"  
- **Issue** The authors interpret the low AUC of PScore on the PS-test set as evidence that these proteins are partner-dependent. However, the PS-test set contains proteins without Self or Partner annotations, and the actual mechanism is unknown. The interpretation is speculative.  
- **Required correction** Soften the interpretation and acknowledge that the mechanism of these proteins is not experimentally verified.

## Risk / unsupported claims
- The claim that partner-dependent proteins are "widespread in cells" based on MLO participant dataset analysis is not fully supported, as the datasets may be biased toward well-studied proteins.
- The claim that Phos frequency is the most important feature for model decisions is not robustly established due to potential feature correlation and dataset-specific effects.
- The claim that the models can accurately distinguish self-assembling from partner-dependent proteins is not fully validated, as the experimental confirmation is limited to three proteins.
- The generalizability of the models to species beyond the 10 used for training is not demonstrated.
- The biological significance of the pathway enrichment analysis (Fig. 5A) is not discussed in sufficient depth to draw meaningful conclusions.