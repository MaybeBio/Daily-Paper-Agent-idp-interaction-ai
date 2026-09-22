## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to methods, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors propose SEHI-PPI, an end-to-end deep learning framework for predicting human-influenza protein-protein interactions. The framework integrates a double-view architecture for global and local sequence features and an adaptive negative sampling strategy. Reported performance includes sensitivity of 0.986 and AUROC of 0.987 on benchmark comparisons, AUROC of 0.837 under a stringent unseen-family test, average sensitivity of 0.929 and AUROC of 0.928 across other human-virus PPI datasets, and AlphaFold3-guided case studies suggesting structural and functional clustering of viral proteins targeting the same human protein.
- **Visible evidence base** Abstract text only; no methodological details, dataset descriptions, baseline specifications, or quantitative results beyond those stated in the abstract
- **Missing materials affecting confidence** Full manuscript, methods section, dataset construction and split details, baseline model configurations, statistical significance testing, AlphaFold3 case study details, and any supplementary figures or tables

## Reviewer
- **Overall assessment** The abstract presents a potentially useful computational framework for host-virus PPI prediction, with strong reported performance metrics and a claim of generalizability across datasets. However, the absence of methodological detail, dataset descriptions, and validation procedures prevents independent assessment of the core claims. The performance figures, while impressive, cannot be evaluated for rigor without knowing the data splits, negative sampling ratios, baseline implementations, and whether the unseen-family test was truly leakage-free. The AlphaFold3-guided case studies are intriguing but described at a level too superficial to assess biological significance. The work addresses a relevant problem and the proposed double-view architecture with adaptive negative sampling is a reasonable technical contribution, but the evidence base provided is insufficient to establish the case.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on host-pathogen interaction prediction, particularly those developing deep learning methods for protein-protein interaction tasks. Virologists studying influenza-host interactions may also find the predicted interactions and AlphaFold3-guided structural insights useful for prioritizing experimental validation. Researchers developing negative sampling strategies for imbalanced biological interaction datasets would find the methodological contribution relevant.
- **Major strengths** The problem is well-motivated given the public health relevance of influenza and the incompleteness of experimentally validated host-virus PPI data. The proposed framework addresses two recognized limitations in existing methods, namely sample quality and modeling of interaction complexity, through adaptive negative sampling and a double-view architecture. The reported performance across multiple benchmarks and datasets, including a stringent unseen-family test, suggests potential generalizability. The integration of AlphaFold3-guided structural analysis to support biological relevance is a forward-looking validation approach.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: The combination of double-view sequence feature learning with adaptive negative sampling for host-virus PPI prediction is a reasonable incremental contribution, though similar architectural ideas exist in the broader PPI prediction literature. Scientific importance: The problem is important, but the abstract does not demonstrate a conceptual advance beyond improved performance metrics. Interdisciplinary readership: The work bridges computational biology and virology, but the abstract is written primarily for a machine learning audience and does not sufficiently convey biological insight. Technical soundness: Cannot be assessed from the abstract alone; critical details on data splits, baselines, and statistical rigor are missing. Readability for nonspecialists: The abstract is accessible but relies heavily on performance metrics without contextualizing their practical significance for virology.
- **Recommendation posture** Currently not established from the provided evidence. The claims are plausible but cannot be verified without the full manuscript. A revised assessment would require access to methodological details, dataset construction, baseline configurations, and statistical validation.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The framework outperforms multiple benchmarks including state-of-the-art large language models, achieving sensitivity of 0.986 and AUROC of 0.987.  
- **Evidence pointer** Abstract, performance results section; location not provided  
- **Concern** The abstract reports superior performance against multiple benchmarks but provides no information on which benchmarks were used, how they were configured, whether hyperparameters were tuned per baseline, or whether the comparison was conducted under identical data splits and evaluation protocols. Without this information, the claimed superiority cannot be verified.  
- **Why it matters** Benchmark comparisons are only meaningful when baselines are fairly and consistently evaluated. If baselines were not optimized or were evaluated under different conditions, the reported performance advantage may be artifactual.  
- **Resolution test** Provide full benchmark details including dataset splits, baseline versions, hyperparameter tuning procedures, and statistical significance tests (e.g., confidence intervals or paired tests) for all reported metrics.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** In a stringent test involving entirely unseen human and influenza protein families, SEHI-PPI maintains strong performance with an AUROC of 0.837.  
- **Evidence pointer** Abstract, unseen-family test; location not provided  
- **Concern** The abstract does not describe how the unseen-family split was constructed, what criteria defined family separation, whether sequence similarity between training and test sets was controlled, or whether the negative sampling strategy was applied consistently in this setting. Without these details, the claim of a stringent test cannot be evaluated.  
- **Why it matters** Unseen-family evaluation is a critical test of generalizability, but its validity depends entirely on the rigor of the split. If sequence leakage occurred or if the negative set was constructed differently, the reported AUROC may not reflect true generalization.  
- **Resolution test** Describe the family-level split procedure, report sequence identity thresholds used to ensure separation, and confirm that the same negative sampling protocol was applied in the unseen-family test as in the main experiments.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The model demonstrates high generalizability across other human-virus PPI datasets, with an average sensitivity of 0.929 and AUROC of 0.928.  
- **Evidence pointer** Abstract, cross-dataset generalization; location not provided  
- **Concern** The abstract does not specify which human-virus PPI datasets were used, how many datasets were included, whether the model was retrained or applied zero-shot, or how the negative samples were generated for these external datasets. The term average is used without reporting variance or per-dataset results.  
- **Why it matters** Cross-dataset generalization claims are only meaningful if the evaluation protocol is clearly defined. Different datasets may have different positive-to-negative ratios, and the negative sampling strategy may not transfer consistently.  
- **Resolution test** List the external datasets used, report per-dataset performance with variance, and describe whether the model was fine-tuned or applied without retraining, including the negative sampling procedure for each dataset.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Biological relevance  
- **Claim pointer** AlphaFold3-guided case studies reveal that viral proteins predicted to target the same human protein cluster together structurally and functionally, underscoring the biological relevance of our predictions.  
- **Evidence pointer** Abstract, AlphaFold3 case studies; location not provided  
- **Concern** The abstract states that viral proteins predicted to target the same human protein cluster structurally and functionally, but provides no details on the number of case studies, the clustering methodology, the structural metrics used, or how functional clustering was defined. The term cluster together is vague and could reflect trivial properties of the input sequences rather than meaningful biological signal.  
- **Why it matters** The biological relevance claim is a key differentiator for the work, but as presented it is not quantitatively supported. Without clear clustering criteria and statistical assessment, the claim remains anecdotal.  
- **Resolution test** Provide details on the case study selection, the structural and functional features used for clustering, the clustering algorithm and significance testing, and a comparison against appropriate controls.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Adaptive negative sampling strategy  
- **Evidence pointer** Abstract, methods description; location not provided  
- **Issue** The abstract introduces a novel adaptive negative sampling strategy but does not describe what makes it adaptive or how it differs from existing negative sampling approaches.  
- **Required correction** Provide a brief description of the adaptive mechanism and its rationale in the abstract or indicate where full details can be found in the manuscript.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Double-view architecture  
- **Evidence pointer** Abstract, methods description; location not provided  
- **Issue** The term double-view is used to describe the architecture capturing global and local sequence features, but the abstract does not clarify what distinguishes the two views or how they are integrated.  
- **Required correction** Clarify what constitutes the global and local views and how the two views are combined in the final prediction.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Performance metrics  
- **Evidence pointer** Abstract, performance results; location not provided  
- **Issue** The abstract reports sensitivity and AUROC but does not report precision, specificity, F1 score, or other metrics that would provide a more complete picture of performance, particularly given the class imbalance typical of PPI prediction tasks.  
- **Required correction** Include additional metrics such as precision, specificity, and F1 score, or justify why sensitivity and AUROC are the primary metrics of interest.

## Risk / unsupported claims
- The claim of outperforming state-of-the-art large language models is unsupported without baseline details and statistical testing.
- The claim of a stringent unseen-family test is unsupported without a description of the split procedure and sequence similarity controls.
- The claim of high generalizability across other human-virus PPI datasets is unsupported without dataset names, per-dataset results, and variance reporting.
- The claim that AlphaFold3-guided case studies reveal structural and functional clustering is unsupported without clustering methodology and statistical assessment.
- The overall claim of uncovering biologically meaningful host-virus interactions and potential therapeutic targets is not established from the abstract-level evidence provided.