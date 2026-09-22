## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, methodological rigor, claims versus evidence, and technical soundness of the machine learning approach and experimental validation
- **Shared manuscript claim summary** The authors present PSPire, a machine learning predictor that integrates residue-level and structure-level features to predict phase-separating proteins (PSPs), with a particular focus on improving identification of PSPs lacking intrinsically disordered regions (noID-PSPs). They report superior performance over existing predictors for noID-PSP classification and provide experimental validation showing 9 of 11 candidate PSPs form condensates in cells.
- **Visible evidence base** Main text figures 1-5, supplementary figures 1-7, supplementary tables 1-4, supplementary data 1-5 (referenced but not fully visible)
- **Missing materials affecting confidence** Supplementary Data files 1-5 contents not visible; Supplementary Tables 1-4 contents not visible; Supplementary Figures 1-7 contents not visible; exact training/test split compositions and feature lists partially described but not fully enumerated

## Reviewer

- **Overall assessment** The manuscript addresses a genuine gap in the phase separation prediction field: the bias of existing predictors toward IDR-containing proteins. The central hypothesis, that structure-based surface features can improve noID-PSP prediction, is well motivated and the results are largely consistent with this hypothesis. The development of PSPire is methodologically sound in its use of AlphaFold structures, SSUP definition, and XGBoost classification. The experimental validation, with 9 of 11 candidates confirmed, is a notable strength. However, several technical concerns regarding dataset construction, evaluation methodology, and the interpretation of feature importance warrant clarification before the claims can be fully accepted.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, computational biologists developing protein function predictors, and experimental biologists seeking candidate PSPs for validation. The work is also relevant to those interested in leveraging AlphaFold structures beyond fold prediction, and to the broader community studying the role of structured domains in multivalent interactions.

- **Major strengths** 
  1. Addresses a real and recognized limitation in the field: the systematic underprediction of noID-PSPs by existing tools.
  2. The SSUP concept is a sensible and novel way to extract structure-based features relevant to surface-mediated interactions.
  3. The inclusion of both IDR-based and SSUP-based features allows the model to handle both classes of PSPs within a unified framework.
  4. Experimental validation of multiple candidates, including in vitro condensation assays and FRAP, substantially strengthens the practical utility claim.
  5. The authors provide a web-accessible tool and clear documentation of the training procedure, supporting reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Dataset construction and label reliability
- **Claim pointer** The authors claim that PSPire outperforms current predictors in classifying noID-PSPs from non-PSPs, based on training and testing datasets assembled from PhaSePred data plus additional PSPs from public databases.
- **Evidence pointer** Methods, Datasets section; Figure 1a; Figure 4a-c
- **Concern** The construction of the negative dataset is not described in sufficient detail. The authors state that negative training and testing datasets contained 8323 and 1961 proteins, respectively, but do not specify how these negatives were selected, whether they were filtered to remove potential unannotated PSPs, or how the balance between IDR-containing and non-IDR-containing negatives was managed. If the negative set is enriched for proteins with low PS propensity by construction, the reported AUROC values may not reflect real-world performance. Additionally, the authors do not report how many of the negative proteins contain IDRs, which is critical given the claim of improved noID-PSP detection.
- **Why it matters** The central claim of the paper is that PSPire improves noID-PSP prediction. If the negative set is biased or the positive set is incomplete, the performance comparison against existing predictors may be confounded. Without clarity on negative set composition, the reported improvements cannot be properly interpreted.
- **Resolution test** Provide a detailed description of negative set construction, including source databases, filtering criteria, and the distribution of IDR-containing versus non-IDR-containing proteins in both positive and negative sets. Report performance metrics stratified by IDR status of negatives.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evaluation methodology and comparison fairness
- **Claim pointer** The authors claim PSPire "significantly outperforms current predictors" for noID-PSP prediction, with AUROC of 0.84 versus best current predictor at 0.68.
- **Evidence pointer** Figure 4a-b; Figure 1a; Supplementary Table 2
- **Concern** The comparison with existing predictors may not be fully fair. The authors state that "the PSAP model was re-trained on the same training dataset with the same strategy," but it is unclear whether other predictors (PhaSePred, FuzDrop, etc.) were also retrained or used as-is with their default parameters. If other predictors were not retrained on the same data, the comparison may reflect differences in training data rather than model architecture. Furthermore, the authors do not report confidence intervals or statistical significance tests for the AUROC/AUPRC differences. Given the relatively small number of noID-PSPs (64 in the test set), the observed differences may not be statistically robust.
- **Why it matters** The performance improvement claim is the primary contribution of the paper. If the comparison is not conducted under controlled conditions, the magnitude of the claimed improvement cannot be trusted.
- **Resolution test** Clarify whether all baseline predictors were retrained on identical training data or used with default parameters. Report confidence intervals or bootstrap estimates for AUROC/AUPRC differences, and perform statistical significance testing (e.g., DeLong test for ROC curves).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Feature importance interpretation
- **Claim pointer** The authors use SHAP to identify the most important features and state that "the Phos frequency feature got the highest absolute SHAP score in both cases" (for ID-PSP and noID-PSP classification).
- **Evidence pointer** Supplementary Figure 4; Results section
- **Concern** The SHAP analysis is presented as supporting the role of SSUP-based features, but the dominance of the phosphorylation frequency feature raises questions. Phosphorylation sites are known to be enriched in IDRs, and the authors previously stated that Phos is "IDR-independent" based on their definition. However, the relationship between phosphorylation site density and IDR content in the training data is not examined. If phosphorylation frequency correlates strongly with IDR presence, then the SHAP results may not cleanly separate IDR-based and structure-based contributions.
- **Why it matters** The paper's conceptual contribution is that structure-based features matter for noID-PSP prediction. If the most important feature (Phos) is confounded with IDR content, the interpretation that SSUP features drive the improvement is weakened.
- **Resolution test** Report the correlation between Phos frequency and IDR content in the training set. Provide SHAP analysis with Phos feature excluded to show that SSUP features alone still contribute meaningfully to noID-PSP classification.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation scope
- **Claim pointer** The authors claim "9 out of 11 chosen candidate PSPs confirmed to form condensates within cells."
- **Evidence pointer** Figure 5a-d; Results section, Validation subsection
- **Concern** The experimental validation is a strength, but the selection criteria for the 11 candidates are not fully transparent. The authors state they considered "protein size, literature support of association with the biological processes of interest, the availability of antibodies for immunofluorescence, and the feasibility of expressing and purifying proteins." These criteria introduce potential selection bias. Additionally, the validation used overexpression of GFP-tagged proteins, which can drive artifactual aggregation. The authors do show endogenous staining for some candidates, which is good, but the number of endogenously validated proteins is limited. The in vitro condensation assays were performed for only 4 proteins, and the conditions (PEG concentrations) varied.
- **Why it matters** The validation rate of 9/11 is impressive, but if candidates were pre-selected for favorable properties, the true positive rate for arbitrary PSPire predictions may be lower. The field would benefit from a more systematic validation approach.
- **Resolution test** Provide a detailed description of candidate selection criteria and how many candidates were screened to arrive at the 11 tested. Report whether any candidates predicted by PSPire failed to validate and what their characteristics were. Consider validating a random subset of predictions to estimate the true positive rate.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of IDR definition
- **Affected element** Methods, IDR calculation
- **Evidence pointer** Methods section, IDRs calculation
- **Issue** The IDR definition uses a pLDDT threshold of 50, which is reasonable but not standard. Most IDR predictors use sequence-based methods (e.g., IUPred, VSL2). The choice of pLDDT-based IDR assignment should be justified and compared with sequence-based IDR predictions to ensure the noID-PSP classification is robust to the IDR definition.
- **Required correction** Add a comparison of IDR assignment using pLDDT versus at least one sequence-based method, and discuss how the choice affects the ID-PSP/noID-PSP classification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Generalizability to non-human proteomes
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The model is trained and evaluated on human proteins. The authors mention training models with and without the Phos feature for other species, but no performance evaluation on non-human proteomes is presented. Given that AlphaFold structures are available for many species, the generalizability of PSPire to other organisms is unclear.
- **Required correction** Add a brief evaluation on at least one non-human proteome (e.g., mouse or yeast) to demonstrate generalizability, or explicitly discuss the limitation.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Web server availability
- **Affected element** Abstract, Discussion
- **Evidence pointer** Abstract; Discussion
- **Issue** The authors state that PSPire is available as a web server, but no URL or access instructions are provided in the manuscript. This limits the practical utility for other researchers.
- **Required correction** Provide the web server URL and access instructions in the manuscript.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 4c
- **Evidence pointer** Figure 4c
- **Issue** The performance comparison across five MLO datasets is presented as a heatmap of AUC values, but no error bars or confidence intervals are shown. Given the small number of positive examples in some datasets, the AUC estimates may be noisy.
- **Required correction** Report confidence intervals or bootstrap estimates for the AUC values in Figure 4c, or state the number of positive examples in each dataset.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion of limitations focuses on AlphaFold accuracy and IDR definition. However, the authors do not discuss the potential circularity in using AlphaFold structures, which are trained on known protein structures and may embed information about protein function that could indirectly reflect PS propensity.
- **Required correction** Add a brief discussion of this potential limitation and how it might affect the interpretation of structure-based features.

## Risk / unsupported claims
- The claim that PSPire "significantly outperforms" current predictors for noID-PSP prediction is not supported by statistical significance testing; the reported AUROC differences lack confidence intervals.
- The claim that SSUP-based features are the key drivers of improved noID-PSP prediction is weakened by the dominance of the Phos frequency feature in SHAP analysis, and the potential confounding between Phos frequency and IDR content is not examined.
- The claim that 9 of 11 candidates form condensates is based on a potentially biased candidate selection process; the true positive rate for arbitrary predictions is not established.
- The generalizability of PSPire to non-human proteomes is claimed but not demonstrated with performance data.
- The statement that "most features employed by current PSP predictors do not favor noID-PSPs" is supported by the feature analysis in Figure 1b, but the analysis is limited to the top 10 features from PSAP and 6 from PhaSePred, which may not represent the full feature space of these predictors.