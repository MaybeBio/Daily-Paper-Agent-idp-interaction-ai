## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary information descriptions.
- **Assessment boundary** Scientific content, methodological rigor, validation approach, and claims as presented in the provided text. No access to supplementary datasets, figures beyond descriptions, or code.
- **Shared manuscript claim summary** The authors present MolPhase, a machine learning-based predictor of protein phase separation (PS) that integrates 39 physicochemical features and was trained on 606 experimentally validated PS proteins. They report superior performance compared to four existing predictors, identify key contributing features (pi-interactions, disorder, prion-like domains), and validate predictions experimentally using phytobacterial type III effectors (T3Es), showing that many T3Es undergo phase separation in vitro and in vivo.
- **Visible evidence base** Text descriptions of Figures 1–5 and EV1–EV4, methods section, and supplementary table descriptions. No raw data, numerical performance metrics beyond AUC, or full figure panels were available for direct inspection.
- **Missing materials affecting confidence** Supplementary tables (EV1–EV3), Dataset EV1, source data files, full figure images, and code availability. Performance comparison details against other predictors are only partially described. Experimental validation data (microscopy images, FRAP curves) are not directly assessable from text alone.

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful tool for predicting protein phase separation, with a reasonable feature set and a substantial training dataset. The application to T3Es is biologically interesting and provides some experimental validation. However, several methodological details and validation aspects are insufficiently described to fully assess the tool's reliability and generalizability. The claim of "advanced" performance over existing predictors requires more rigorous and transparent benchmarking. The experimental validation, while suggestive, is limited in scope and does not fully address the complexity of PS behavior in living systems.
- **Who would be interested in the results, and why** Researchers studying phase separation and biomolecular condensates, particularly those interested in prediction tools for identifying new PS proteins. The T3E application will interest plant pathologists and microbiologists studying bacterial effector function. The tool's potential for proteome-wide screening may appeal to a broader cell biology audience.
- **Major strengths** 1) Integration of a diverse set of 39 physicochemical features, which is more comprehensive than many existing tools. 2) Use of a relatively large, curated positive training set of 606 experimentally validated PS proteins. 3) The T3E case study provides a concrete biological application with both in vitro and in vivo validation. 4) The online interface enhances accessibility and practical utility.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (benchmarking transparency), R1-M2 (negative dataset validity), R1-M3 (experimental validation scope), R1-M4 (feature redundancy and interpretability).
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The approach combines existing features in a new way, but the conceptual framework is not fundamentally novel. The T3E application provides some originality.  
  *Scientific importance*: Moderate. A reliable PS predictor would be valuable, but the field already has several tools, and the incremental improvement needs to be clearly demonstrated.  
  *Interdisciplinary readership*: Moderate. Will appeal to computational biologists, cell biologists, and plant pathologists, but may not attract a broader readership.  
  *Technical soundness*: Needs improvement. Several methodological details and validation aspects require clarification and strengthening.  
  *Readability for nonspecialists*: Generally clear, but some sections assume familiarity with PS-specific concepts and machine learning terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising, but the current evidence does not fully establish the tool's superiority or generalizability.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Benchmarking
- **Claim pointer** The authors claim MolPhase "showed improved accuracy and reliability among several available phase separation-prediction algorithms, including DeePhase, PSPredictor, FuzDrop, PSPer."
- **Evidence pointer** Figure 2E, F; Figure EV1D–G; "location not provided" for specific performance metrics
- **Concern** The benchmarking against other predictors is described only qualitatively. The text mentions density plots of prediction probabilities and confusion matrices, but no quantitative performance metrics (e.g., accuracy, F1, MCC, AUC on the same external test set) are reported for the comparison. It is unclear whether the same test sets and thresholds were used for all predictors, and how the comparison was standardized. This makes it impossible to evaluate the claimed superiority.
- **Why it matters** A central claim of the manuscript is that MolPhase outperforms existing tools. Without transparent, quantitative, and fair benchmarking, this claim is not substantiated. The field needs clear evidence of improvement to justify adopting a new tool.
- **Resolution test** Provide a table with performance metrics (e.g., accuracy, precision, recall, F1, MCC, AUC) for MolPhase and each comparator on the same external test sets, with clear descriptions of thresholds and any parameter tuning. Include confidence intervals or statistical tests for differences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Dataset construction
- **Claim pointer** The authors state that "Proteins deposited in the Protein Data Bank (PDB) are typically derived from monodispersed and homogenously packed proteins... Here we selected 1362 proteins from PDB as the negative PS dataset."
- **Evidence pointer** Methods section "Training and testing dataset construction"; "location not provided" for specific PDB selection criteria
- **Concern** The use of PDB structures as a negative set for PS is problematic. Many PDB proteins may undergo phase separation under certain conditions, and the selection criteria beyond a 30% similarity cutoff are not described. The authors acknowledge this limitation in the Discussion, but the potential contamination of the negative set with false negatives could bias the model and inflate performance estimates. The criteria for selecting "entirely structured single-chain proteins" are not detailed, and it is unclear how representative this negative set is of non-PS proteins in general.
- **Why it matters** The quality of the negative set directly affects model training and evaluation. A biased or contaminated negative set can lead to overestimated performance and poor generalizability to real-world applications where the distinction between PS and non-PS proteins is more nuanced.
- **Resolution test** Provide a detailed description of the PDB selection process, including any filters applied (e.g., resolution, organism, function). Perform a sensitivity analysis by training and evaluating the model with alternative negative sets (e.g., proteins from the same organisms that are not known to phase separate, or using a more conservative subset of PDB). Report performance under these conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation / Scope
- **Claim pointer** The authors state that "all the T3Es examined that were positively predicted by MolPhase displayed phase separation behaviors within live plants upon exogenous expression."
- **Evidence pointer** Figure 4; "location not provided" for quantification details
- **Concern** The experimental validation is limited to a small number of T3Es (eight predicted positive, five predicted negative). While the results are consistent with predictions, the sample size is small, and the validation is largely qualitative (visual inspection of microscopy images). The FRAP data are described but not quantitatively compared between in vitro and in vivo conditions. The authors note differences in material properties between in vitro and in vivo, but this is not systematically explored. The choice of T3Es may also be biased, as they were selected based on prediction scores, potentially overrepresenting clear cases.
- **Why it matters** The experimental validation is a key part of the manuscript's claim that MolPhase predictions are biologically meaningful. A small, potentially biased sample with qualitative assessment does not provide strong evidence for the tool's predictive power in diverse biological contexts.
- **Resolution test** Increase the number of validated proteins, including more borderline cases. Provide quantitative measures of PS (e.g., droplet size, number, fluorescence recovery rates) and statistical comparisons between predicted positive and negative groups. Include negative controls that are not predicted to phase separate but are tested under the same conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Feature analysis
- **Claim pointer** The authors state that "electrostatic pi-interactions, disorder, and prion-like domains" are key contributing factors, and that pi-interaction is the most significant feature.
- **Evidence pointer** Figure 2D; "location not provided" for feature importance values
- **Concern** The feature importance analysis is presented only as a bar plot (Figure 2D) without numerical values or error estimates. It is unclear how feature importance was calculated (e.g., gain, permutation importance, SHAP values) and whether the ranking is stable across different model runs or cross-validation folds. The high correlation between some features (e.g., disorder and prion-like domains) may affect the interpretation of individual feature contributions.
- **Why it matters** Understanding which features drive predictions is important for biological interpretation and for guiding experimental design. An unstable or poorly characterized feature importance analysis weakens the mechanistic insights the authors claim.
- **Resolution test** Report feature importance with confidence intervals or standard deviations across cross-validation folds. Specify the method used for importance calculation. Consider performing an ablation study (removing individual features or feature groups) to assess their contribution to model performance.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Methods section "Protein features extraction"
- **Evidence pointer** Table EV2; "location not provided"
- **Issue** The methods section refers to Table EV2 for feature extraction methods but does not describe the specific tools or parameters used for each feature. This limits reproducibility.
- **Required correction** Provide a more detailed description of the feature extraction process in the main text or ensure Table EV2 includes all necessary parameters and tool versions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 1 statistical comparisons
- **Evidence pointer** Figure 1A–N; "location not provided"
- **Issue** The figure legend mentions Mann–Whitney tests, but the exact P values are not reported, and multiple testing corrections are not mentioned. With 14 comparisons, some significant results may arise by chance.
- **Required correction** Report exact P values or indicate significance levels clearly. Consider applying a multiple testing correction (e.g., Benjamini-Hochberg) and state this in the methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity / Terminology
- **Affected element** Results section "Application of MolPhase for evaluating phytobacterial effectors' phase separation in plant host"
- **Evidence pointer** "location not provided"
- **Issue** The text states "or this purpose" which appears to be a typo for "for this purpose". Additionally, the term "2D phase separation" is used without clear definition.
- **Required correction** Correct the typo and define what is meant by "2D phase separation" in this context.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion section
- **Evidence pointer** "location not provided"
- **Issue** The Discussion mentions limitations of the negative dataset and the conditional nature of PS, but does not discuss potential limitations of the positive dataset, such as potential bias toward well-studied PS proteins or the possibility of false positives in the curated literature set.
- **Required correction** Add a brief discussion of potential biases in the positive training set and how they might affect model generalizability.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Online interface description
- **Evidence pointer** Figure EV4; "location not provided"
- **Issue** The online interface is described, but there is no mention of the underlying code being open-source or available for local installation, which may limit its use for high-throughput or custom analyses.
- **Required correction** State whether the code is available (e.g., on GitHub) and under what license, or clarify that the web interface is the only access point.

## Risk / unsupported claims
- The claim of "improved accuracy and reliability" over other predictors is not quantitatively supported in the provided text.
- The statement that MolPhase is "the most comprehensive tool" in terms of feature integration is not directly supported by a comparison of feature sets across all existing tools.
- The claim that T3Es "are highly prone to homotypic PS" based on the analysis of a limited set of effectors may be overstated without a broader survey.
- The assertion that MolPhase can "guide hypothesis generation and experimental design" is plausible but not directly demonstrated beyond the T3E case study.
- The generalizability of MolPhase to diverse protein types and conditions beyond the training set distribution is not assessed.