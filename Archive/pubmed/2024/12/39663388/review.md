## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary information descriptions
- **Assessment boundary** Scientific validity, methodological rigor, claims versus evidence, and generalizability of the PICNIC machine learning model for predicting condensate-forming proteins
- **Shared manuscript claim summary** The authors present PICNIC, a gradient boosting machine learning classifier that predicts proteins localizing to biomolecular condensates using sequence co-occurrence, structural (AlphaFold2), and disorder features. They claim high accuracy across organisms, experimental validation of 24 predictions with 87.5% success, and no correlation between predicted condensate proteome fraction and organismal complexity or disorder content.
- **Visible evidence base** Figures 1-7, Supplementary Figures S1-S17, Supplementary Tables S1, Datasets S1-S6, Methods section
- **Missing materials affecting confidence** Raw experimental images beyond representative examples, complete dataset of negative predictions tested experimentally, code repository access not verified, detailed hyperparameter tuning results, statistical significance tests for comparative performance

## Reviewer
- **Overall assessment** The manuscript presents a valuable contribution to the field of biomolecular condensate prediction. The methodological approach of using amino acid co-occurrence features combined with AlphaFold2 structural information is novel and addresses a clear gap in existing predictors that focus primarily on disorder-driven phase separation. The experimental validation strategy is commendable, and the cross-species analysis adds breadth. However, several concerns regarding dataset construction, validation rigor, and interpretation of cross-species results need to be addressed before the claims are fully established.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and membraneless organelles would find this directly relevant. Computational biologists developing protein function predictors would benefit from the feature engineering approach. Cell biologists studying specific condensate-localized proteins could use PICNIC as a screening tool. The cross-species analysis may interest evolutionary biologists studying proteome complexity. The open-source availability and web resource make it accessible to the broader community.

- **Major Strengths** 
  1. Novel feature engineering combining sequence co-occurrence with AlphaFold2 structural features, moving beyond disorder-centric approaches
  2. Thoughtful negative dataset construction using protein-protein interaction networks to reduce false negatives
  3. Extensive experimental validation with 24 proteins spanning diverse structural and functional categories
  4. Cross-species analysis across 26 organisms demonstrating generalizability
  5. Practical utility through the picnic-bio Python package and precomputed scores website
  6. Honest discussion of limitations, including the philosophical challenge of defining negative datasets

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Dataset construction and potential bias
- **Claim pointer** The negative dataset construction method is claimed to be "unbiased" and based on protein-protein interaction network exclusion
- **Evidence pointer** Methods section "Construction of positive and negative datasets", Figure 1a
- **Concern** The negative dataset construction relies on the assumption that proteins not directly interacting with known condensate proteins are non-condensate forming. This is a strong assumption that may introduce systematic bias. Proteins with no known interactions could be understudied rather than truly non-condensate forming. Additionally, the InWeb database is human-specific and may have incomplete coverage, potentially misclassifying true condensate proteins as negatives.
- **Why it matters** If the negative dataset contains a significant fraction of false negatives (true condensate proteins mislabeled as non-condensate), the model's discriminative ability could be artificially inflated. The model might be learning to distinguish well-studied from poorly-studied proteins rather than condensate-forming from non-condensate-forming proteins.
- **Resolution test** Provide additional validation using independent negative datasets, such as proteins experimentally confirmed to not localize to condensates under multiple conditions. Report the proportion of negative dataset proteins that have any literature evidence of condensate localization. Consider sensitivity analysis with different network centrality thresholds for negative selection.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation rigor
- **Claim pointer** "87.5% of PICNIC predictions were found to be correct" based on 24 tested proteins
- **Evidence pointer** Results section "Experimental validation of predicted condensate-forming proteins", Figure 4
- **Concern** The experimental validation has several limitations. First, only 24 positive predictions were tested, with no experimental validation of negative predictions. Second, the classification of "high confidence" versus "low confidence" condensates uses criteria (foci diameter >350 nm) that may exclude bona fide small condensates. Third, the validation was performed in a single cell line (U2OS) with overexpression, which may not reflect endogenous conditions. Fourth, the statement that 3 proteins "localized to the nucleoplasm without forming any detectable foci" does not definitively prove they do not form condensates under other conditions.
- **Why it matters** The 87.5% accuracy claim is central to the paper's conclusion. Without testing negative predictions, the false positive rate remains unknown. The single-cell-line overexpression system may overestimate condensate-forming propensity. The accuracy metric could be substantially different under more physiologically relevant conditions.
- **Resolution test** Validate a matched set of negative predictions (e.g., 20-30 proteins predicted as non-condensate forming) using the same experimental pipeline. Test a subset of proteins in additional cell lines or under stress conditions. Provide quantitative criteria for condensate classification that are more inclusive of small condensates. Report the dynamic range of expression levels and its correlation with condensate formation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Cross-species generalizability claims
- **Claim pointer** "PICNIC model is species-independent and is useful for different organisms" based on 50-100% correct identification of known condensate proteins across 14 species
- **Evidence pointer** Results section "Proteome-wide predictions detect no correlation", Figure 7a
- **Concern** The cross-species validation relies on known condensate proteins from CD-CODE, which may have variable annotation completeness across species. The zebrafish performance of only 50% suggests species-specific limitations. The claim of "species-independent" is strong given that the model was trained exclusively on human data and validated on a limited number of known positives per species. The number of known condensate proteins per species varies widely, and for some species (e.g., E. coli with N=6), the sample size is too small for reliable statistics.
- **Why it matters** The generalizability claim is a key selling point of the manuscript. If the model performs poorly on certain species or if the validation is based on incomplete annotations, the cross-species utility may be overstated. The 40-60% predicted condensate proteome fraction across all species is surprisingly high and may indicate overprediction.
- **Resolution test** Provide per-species breakdown of validation set sizes and performance confidence intervals. Test on additional species with experimentally verified condensate proteomes. Discuss potential reasons for zebrafish underperformance. Validate the high predicted fractions (40-60%) with independent experimental approaches in at least one prokaryotic and one eukaryotic species.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparative performance assessment
- **Claim pointer** "PICNIC has superior performance with a maximum F1-score of 0.81" compared to other predictors
- **Evidence pointer** Figure 2
- **Concern** The comparative evaluation may be biased. The test datasets from PhaSepDB and OpenCell were used to evaluate all methods, but the authors note that these datasets may include training data from previously published predictors, potentially inflating their performance. However, the reverse bias may also exist: PICNIC was trained on CD-CODE, and the CD-CODE test set is derived from the same database, potentially giving PICNIC an advantage. The comparison does not include the most recent predictors, and the evaluation metrics (F1-score at a single threshold) may not capture the full performance spectrum.
- **Why it matters** The claim of superiority over existing methods is important for establishing PICNIC as the state-of-the-art tool. Biased comparisons could mislead users in method selection.
- **Resolution test** Perform a more rigorous benchmark using a truly independent test set not used in training by any method. Report precision-recall curves and area under the curve across the full threshold range. Include additional recent predictors in the comparison. Consider cross-database validation where models trained on one database are tested on another.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Feature interpretability and biological insight
- **Claim pointer** "PICNIC may shed light on several sequence features important for condensates" including amino acid co-occurrence and secondary structure
- **Evidence pointer** Figure 1c-d, Discussion section
- **Concern** While the feature importance analysis identifies lysine, leucine, and specific co-occurrence patterns as important, the biological interpretation is somewhat superficial. The authors do not deeply explore why these specific features are predictive or how they relate to known biophysical mechanisms of condensate formation. The claim that structural features from AlphaFold2 are important is interesting but not mechanistically explained.
- **Why it matters** The paper positions itself as providing insights into the sequence determinants of condensate formation. Without deeper biological interpretation, the feature analysis remains descriptive rather than mechanistic, limiting its impact on understanding condensate biology.
- **Resolution test** Provide more detailed analysis of the most predictive features, including specific examples of how they distinguish condensate-forming from non-condensate-forming proteins. Discuss potential biophysical mechanisms (e.g., charge patterning, hydrophobic interactions, multivalency) that could explain the predictive power of specific features. Consider ablation studies to show the contribution of each feature class.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Model training and hyperparameter details
- **Evidence pointer** Methods section "Machine learning algorithms"
- **Issue** The description of model training lacks specific details on hyperparameter ranges, early stopping criteria, and the exact feature selection threshold. The statement "we chose the validation score (F1-score) of best iteration of each separate fold" is ambiguous regarding how the final model is selected.
- **Required correction** Provide a more detailed description of the training procedure, including hyperparameter search space, number of trees, learning rate, and the exact feature selection algorithm. Consider including a pseudocode or flowchart of the training pipeline.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Performance metrics and confidence intervals
- **Evidence pointer** Figures 2, 7
- **Issue** Performance metrics are reported without confidence intervals or statistical significance tests. The differences between PICNIC and other methods may not be statistically significant given the test set sizes.
- **Required correction** Add confidence intervals for all performance metrics, and perform statistical significance tests (e.g., McNemar's test for paired comparisons) to support claims of superiority.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental details
- **Affected element** Cell culture and imaging conditions
- **Evidence pointer** Methods section "Cloning, cell culture and imaging"
- **Issue** The description of the experimental validation lacks details on transfection efficiency, expression levels, and the number of cells analyzed per protein. The criteria for classifying a protein as forming "high confidence" versus "low confidence" condensates could be more explicitly defined.
- **Required correction** Provide quantitative data on transfection efficiency and expression levels. Specify the number of cells analyzed and the statistical methods used to classify condensate formation. Include a more detailed description of the image analysis pipeline.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Availability and reproducibility
- **Affected element** Code and data availability
- **Evidence pointer** Data availability section (not explicitly provided in the manuscript text)
- **Issue** While the authors mention the picnic-cd-code.org website and Python package, the manuscript does not provide a clear data availability statement or link to the code repository. The datasets used for training and validation are not explicitly listed with accession numbers.
- **Required correction** Add a clear data availability statement with links to the code repository, the PICNIC website, and all datasets used in the study. Provide version numbers and access dates for all external resources.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 4a
- **Evidence pointer** Figure 4a
- **Issue** The representative images in Figure 4a are small and difficult to evaluate. The scale bar is mentioned but not clearly visible in all panels. The inset highlighting condensates is not shown for all proteins.
- **Required correction** Provide larger, higher-resolution images with clearly visible scale bars. Show insets for all proteins, not just representative examples. Consider adding a supplementary figure with additional examples.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** While the authors acknowledge some limitations, they do not discuss the potential impact of using AlphaFold2 models, which may not accurately represent the conformational ensemble of proteins in condensates. The discussion of negative dataset limitations is brief.
- **Required correction** Expand the discussion of limitations to include the potential biases introduced by AlphaFold2 structural predictions and the inherent uncertainty in defining negative datasets. Discuss how these limitations might affect the interpretation of results.

## Risk / unsupported claims
1. The claim that PICNIC is "species-independent" is not fully supported given the variable validation set sizes across species and the 50% performance in zebrafish.
2. The claim of "unbiased" negative dataset construction is questionable given the inherent limitations of network-based approaches.
3. The 87.5% experimental validation accuracy is based on a small sample (24 proteins) with no validation of negative predictions, making the true accuracy uncertain.
4. The statement that "no correlation between predicted condensate proteome fraction and disorder content" across species is based on computational predictions, not experimental validation, and should be framed as a prediction rather than an established finding.
5. The claim that PICNIC "outperforms" other methods is based on potentially biased comparisons where test sets may overlap with training data of other methods.
6. The biological interpretation of feature importance (e.g., lysine and leucine contributions) is presented as insight but lacks mechanistic validation.