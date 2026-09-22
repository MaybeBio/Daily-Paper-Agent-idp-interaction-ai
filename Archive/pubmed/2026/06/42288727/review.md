## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, tables, and figure legends
- **Assessment boundary** Scientific validity, methodological rigor, claims substantiation, and presentation quality of the described prediction tool and its evaluation
- **Shared manuscript claim summary** The authors present MoRFchibi 2.0, an ensemble of four logistic regression convolutional neural network models, claiming it outperforms all existing MoRF-specific and general IDR protein-binding predictors, including those using AlphaFold data and protein language models, across multiple evaluation datasets
- **Visible evidence base** Abstract, introduction, methods (datasets, features, model architecture, evaluation measures), results (performance tables and figures, case studies), discussion, Table 1-4, Figure 2-3 legends
- **Missing materials affecting confidence** Actual prediction scores for individual proteins, statistical significance testing between methods, detailed hyperparameter search results, model convergence analysis, computational runtime comparisons, and the actual Figure 2 and Figure 3 images

## Reviewer
- **Overall assessment** The manuscript describes a potentially valuable contribution to the MoRF prediction field, with a thoughtfully designed ensemble architecture and careful attention to evaluation methodology. The authors address important issues such as data leakage, class imbalance, and the distinction between residue-level and protein-level performance. However, several methodological details and statistical validations are insufficiently described, and the claimed superiority over all existing methods requires stronger statistical support. The case studies are informative but raise questions about annotation quality that are not fully resolved.

- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics focused on intrinsically disordered proteins, protein-protein interaction prediction, and machine learning applications to biological sequence analysis. The community developing and benchmarking predictors for disordered protein binding regions would find the methodological comparisons and new datasets valuable. Experimental biologists studying protein disorder-to-order transitions may also benefit from an improved prediction tool.

- **Major strengths** The authors address a relevant problem with a well-motivated architectural choice. The ensemble approach with reverse Bayes normalization is a thoughtful contribution to score interpretability. The evaluation is more comprehensive than typical in this field, including multiple test sets, comparison against 17 methods, and consideration of AlphaFold-based approaches. The case studies provide useful qualitative insights into prediction behavior. The release of new datasets is a valuable community resource.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical validity
  - **Claim pointer** "MoRFchibi 2.0 outperforms all 17 tested predictors in both Area Under the ROC Curve (AUC) and Average Precision Score (APS) across Test-143 and its variations"
  - **Evidence pointer** Tables 2-4, Figure 2
  - **Concern** The claim of universal superiority is based on point estimates of AUC and APS without any statistical significance testing. Differences between methods could be within noise, particularly given the relatively small test set sizes. No confidence intervals, bootstrap resampling, or paired statistical tests are reported.
  - **Why it matters** Without statistical validation, the central claim of the paper is not established. The differences between top-performing methods may not be meaningful, and readers cannot assess the reliability of the reported performance gaps.
  - **Resolution test** Provide confidence intervals for all metrics, perform paired statistical tests (e.g., DeLong test for AUC, bootstrap for APS) between MoRFchibi 2.0 and each comparator, and report which differences are statistically significant.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Data quality and annotation
  - **Claim pointer** "This process yielded 899 high-quality MoRF segments (HQ MoRFs) across 769 sequences, totalling 46,694 residues"
  - **Evidence pointer** Methods, Datasets section; Table 1
  - **Concern** The construction of the training and test datasets relies on annotations from multiple databases (DisProt, DIBS, MFID, IDEAL) with potentially inconsistent annotation criteria. The masking strategy for ambiguous residues is described but the rationale for specific thresholds is not provided. The transfer of annotations between databases (e.g., using DisProt DtO annotations to filter DIBS segments) may introduce systematic biases.
  - **Why it matters** Dataset quality directly determines the validity of all performance claims. Inconsistent annotations could artificially inflate or deflate performance differences between methods, and the generalizability of the trained model depends on the representativeness of the training data.
  - **Resolution test** Provide detailed annotation statistics per database, describe the masking criteria with explicit thresholds, and perform sensitivity analyses showing that results are robust to annotation choices.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Methodological completeness
  - **Claim pointer** "All architectural and input hyperparameters were selected via a grid search to minimize loss on the validation sets"
  - **Evidence pointer** Methods, Model selection and optimization section
  - **Concern** The hyperparameter search space is not described. The selection of the third-best validation AUC across 15 independent runs is an unusual choice that requires justification. The potential for overfitting the validation set through this selection procedure is not addressed.
  - **Why it matters** Reproducibility is a core requirement for computational tools. Without a complete description of the hyperparameter search, other researchers cannot replicate the training procedure or assess whether the reported performance is specific to the chosen configuration.
  - **Resolution test** Provide the full hyperparameter search space, the selection criterion rationale, and an analysis of variance across the 15 independent runs to demonstrate the stability of the chosen configuration.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evaluation fairness
  - **Claim pointer** "MoRFchibi 2.0 surpasses predictors that utilize AlphaFold data and state-of-the-art protein language models"
  - **Evidence pointer** Tables 2-3, Figure 2
  - **Concern** The comparison against AlphaFold-based and language model-based methods may not be entirely fair. These methods were not specifically designed for MoRF prediction and may require fine-tuning or adaptation for this task. The authors do not describe whether any such adaptation was performed or whether the comparators were used in their default configurations.
  - **Why it matters** Unfair comparisons can lead to misleading conclusions about the relative merits of different approaches. The claim of superiority over language model-based methods is particularly strong and requires careful validation.
  - **Resolution test** Describe the exact usage of each comparator method, including any parameter adjustments. Consider including a version of the best-performing language model method that has been fine-tuned for MoRF prediction.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 2 description
  - **Evidence pointer** Figure 2 legend
  - **Issue** The figure legend mentions "the dotted black line" for DisoFLAG-PB in the bottom panels, but the legend text is ambiguous about which panels contain this line and how it should be interpreted relative to other methods.
  - **Required correction** Clarify in the legend which specific panels contain the DisoFLAG-PB line and explicitly state what the line represents.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Case study descriptions
  - **Evidence pointer** Figure 3 legend
  - **Issue** The case study descriptions reference specific protein examples but do not provide accession numbers or sequence identifiers, making it difficult for readers to verify the examples independently.
  - **Required correction** Add UniProt accession numbers or other stable identifiers for all proteins shown in Figure 3.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Table 2
  - **Evidence pointer** Table 2
  - **Issue** The table reports AUC and SR values but does not include any measure of variance or sample size information for each test subset.
  - **Required correction** Add the number of sequences and residues for each test subset, and consider adding confidence intervals or standard errors for the main metrics.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Presentation
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion, first paragraph
  - **Issue** The discussion repeats claims from the results section without adding new interpretation or context. The statement about "low disorder signature" is vague and not clearly defined.
  - **Required correction** Define what is meant by "low disorder signature" and provide a more substantive discussion of the implications and limitations of the findings.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods, Datasets section
  - **Evidence pointer** Methods, Datasets section
  - **Issue** The description of the Test-new-9 dataset is brief and does not specify how these sequences were selected or whether they were manually curated.
  - **Required correction** Provide additional details on the construction of Test-new-9, including the selection criteria and any manual curation steps.

## Risk / unsupported claims
- The claim that MoRFchibi 2.0 "outperforms all 17 tested predictors" is not statistically supported without significance testing
- The statement that MoRFchibi 2.0 "surpasses predictors that utilize AlphaFold data and state-of-the-art protein language models" is based on point estimates without confidence intervals
- The assertion that the score normalization makes outputs "individually interpretable and compatible with other tools" is plausible but not demonstrated with concrete examples
- The claim that the newly assembled datasets will be useful "for the community to optimize and test other models" is reasonable but the dataset quality and completeness are not fully validated
- The case study in Figure 3F suggesting that zinc finger motifs may be mispredicted as MoRFs is presented as a limitation but the frequency and impact of such cases are not quantified

## Assessment against Nature-style criteria
- **Originality** Moderate. The ensemble architecture and reverse Bayes normalization are incremental improvements over existing approaches. The systematic comparison against AlphaFold-based and language model methods is a useful contribution, but the core methodology follows established patterns in the field.
- **Scientific importance** Moderate. Improved MoRF prediction has practical value for the disorder research community, but the advance over existing methods appears incremental rather than transformative. The release of new training data is a useful community resource.
- **Interdisciplinary readership** Limited. The manuscript is primarily of interest to computational biologists and bioinformaticians specializing in protein disorder prediction. The methods and evaluation are too specialized for a broad interdisciplinary audience.
- **Technical soundness** The methodology is generally sound but has notable gaps. The lack of statistical significance testing is a significant weakness. The dataset construction is thoughtful but requires more detail. The evaluation design is comprehensive but the fairness of comparisons needs clarification.
- **Readability for nonspecialists** The manuscript is clearly written for a specialized audience. The methods are described with appropriate technical detail, but the introduction and discussion assume familiarity with the MoRF prediction field. The case studies help illustrate the practical behavior of the tool.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a potentially useful tool with a comprehensive evaluation, but the central claim of superiority over all existing methods requires statistical validation. The dataset release is a valuable contribution. The authors should address the statistical testing concern, provide more detail on dataset construction and hyperparameter selection, and clarify the fairness of comparisons against AlphaFold-based and language model methods.