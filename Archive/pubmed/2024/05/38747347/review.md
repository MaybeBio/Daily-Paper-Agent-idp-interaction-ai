## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials and methods, server description, use cases, conclusion, data availability, funding, acknowledgements) as provided.
- **Assessment boundary** Scientific and technical evaluation of the AIUPred method, its validation, and the web server implementation, based solely on the supplied material.
- **Shared manuscript claim summary** The authors present AIUPred, an updated version of the IUPred protein disorder prediction method, which replaces the original linear energy estimation and logistic regression with transformer-based neural networks while retaining the core energy estimation framework. They claim improved prediction accuracy over previous IUPred versions and competitive performance among single-sequence methods, alongside exceptional speed and scalability on GPUs. A new web server with enhanced visualization and programmatic access is described.
- **Visible evidence base** Abstract; introduction; materials and methods (including dataset descriptions and validation procedures); server description; two use case examples; conclusion; data availability statement. Tables 1 and 2 are referenced but not provided. Figures 1 and 2 are referenced but not provided. Supplementary Material is referenced but not provided.
- **Missing materials affecting confidence** Tables 1 and 2 (quantitative performance and speed comparisons); Figures 1 and 2 (prediction output examples); Supplementary Material (detailed network architectures, training procedures, hyperparameters); CAID2-PDB dataset details; exact definitions of evaluation metrics and statistical tests beyond the Mann-Whitney test mentioned.

## Reviewer
- **Overall assessment** The manuscript describes a meaningful incremental improvement to a widely used and well-established prediction tool. The core idea of integrating deep learning into the existing energy estimation framework is sensible and potentially valuable, and the reported speed advantages are notable. However, the provided material lacks sufficient quantitative detail to fully assess the claimed performance improvements. The validation is described only qualitatively, with key tables and figures absent, and the statistical rigor of the comparison is not fully documented. The web server features are described in detail and appear useful, but the scientific case for enhanced prediction is not fully established from the supplied evidence.
- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics, particularly those working on intrinsically disordered proteins, protein function prediction, and large-scale proteome analysis. The improved speed and accuracy could benefit users who need to analyze entire proteomes or who require rapid predictions. The community that has relied on IUPred for nearly two decades would be a natural audience, as would developers of other prediction tools seeking to combine biophysical models with deep learning.
- **Major strengths** The retention of the biophysical energy estimation framework while incorporating modern deep learning is a conceptually sound approach that may preserve interpretability and robustness. The reported speed improvements, especially the ability to analyze the human proteome in minutes on a consumer GPU, are practically significant. The web server appears well designed with modern features, including dark mode, Uniprot integration, and RESTful API access. The use of two distinct use cases helps illustrate practical applicability.
- **Major Concerns** The absence of quantitative results in the provided material is a major limitation. The claims of improved accuracy and top-three ranking are not verifiable without Tables 1 and 2. The statistical significance testing is mentioned only for one comparison, and the methodology for other comparisons is unclear. The training and test data splits are described, but the potential for data leakage between the energy model training set and the disorder prediction training set is not addressed. The choice of the Savitzky-Golay filter parameters is not justified. The comparison to SPOT-Disorder-Single is limited to a single metric (AUC) and does not account for potential differences in output calibration or usability.
- **Minor Comments** The manuscript would benefit from a clearer statement of the novelty relative to IUPred3, which is mentioned only in passing. The description of the negative dataset for disorder prediction training is brief and could be expanded. The use case examples are qualitative and would be strengthened by quantitative comparisons to other methods. The statement that the energy model was "never trained on disordered regions" is interesting but its implications for generalization are not discussed in depth.
- **Technical failings that need to be addressed before the case is established** The lack of provided quantitative validation data (Tables 1 and 2) prevents assessment of the central performance claims. The statistical methodology for comparing AIUPred to other methods is not fully described. The potential for overfitting or data leakage between the energy model and the disorder prediction model is not discussed. The reproducibility of the training procedures is not established without the Supplementary Material.
- **Assessment against Nature-style criteria** Originality: Moderate. The combination of a biophysical energy model with transformer networks is not entirely novel, but the specific application to disorder prediction and the retention of the energy framework offer some originality. Scientific importance: Moderate to high. Improved disorder prediction with high speed could have broad utility, but the incremental nature of the improvement limits its transformative potential. Interdisciplinary readership: Moderate. The work is primarily of interest to computational biologists and bioinformaticians, with limited appeal beyond these fields. Technical soundness: Not fully assessable from the provided material due to missing quantitative data and methodological details. Readability for nonspecialists: The manuscript is generally well written and accessible, though some technical details in the methods section may be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea and implementation appear sound, and the speed advantages are compelling. However, the central performance claims must be substantiated with the missing quantitative data and statistical details before the case for enhanced prediction is established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that AIUPred "scored amongst the top three single sequence based methods" on recent benchmark datasets and shows "great improvement over the previous iteration" in accuracy.
- **Evidence pointer** Tables 1 and 2 are referenced but not provided in the supplied material.
- **Concern** The central quantitative claims of improved prediction accuracy and competitive ranking are not verifiable from the provided material. The manuscript references Tables 1 and 2 for performance comparisons and speed benchmarks, but these tables are absent. Without these data, the reader cannot assess the magnitude of improvement, the statistical significance of differences, or the basis for the top-three ranking claim.
- **Why it matters** The primary scientific contribution of the manuscript is the claimed enhancement in prediction performance. If this claim cannot be evaluated, the core value proposition of the work is unsubstantiated. The ranking claim, in particular, requires a clear description of the comparison methods, datasets, and evaluation metrics.
- **Resolution test** Provide Tables 1 and 2 with full quantitative results, including AUC values, confidence intervals, and statistical tests for all comparisons. Clearly describe the evaluation protocol, including the exact datasets used, the methods compared, and the criteria for ranking.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** The manuscript states that the transformer network was trained to predict positional energies and that the second network for disorder prediction was trained using transfer learning, with datasets split 80-20 for training and testing.
- **Evidence pointer** Materials and methods section; Supplementary Material is referenced but not provided.
- **Concern** The description of the training procedures is insufficient to assess methodological rigor. The architecture of the transformer network, the transfer learning approach, the hyperparameter choices, and the training details are all relegated to the Supplementary Material, which is not provided. Additionally, the potential for data leakage between the energy model training set (derived from PDB structures) and the disorder prediction training set (derived from DisProt) is not addressed. If the same or similar proteins appear in both sets, the reported performance could be optimistically biased.
- **Why it matters** Reproducibility and robustness are essential for a method that is intended to be widely used. Without detailed methodological information, other researchers cannot replicate the training or independently verify the results. Data leakage could invalidate the performance claims.
- **Resolution test** Provide the Supplementary Material with full architectural details, training procedures, and hyperparameters. Discuss the potential for data leakage and describe any measures taken to prevent it, such as sequence identity-based filtering between the training sets.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Comparison fairness
- **Claim pointer** The manuscript compares AIUPred to SPOT-Disorder-Single, described as the highest-ranking single-sequence method in CAID2, reporting AUC values of 0.912 and 0.917, respectively, and highlighting speed advantages.
- **Evidence pointer** Materials and methods section; Table 2 is referenced but not provided.
- **Concern** The comparison to SPOT-Disorder-Single is limited to a single AUC value on one dataset. It is unclear whether this comparison is statistically meaningful, whether multiple runs or cross-validation were performed, and whether the AUC difference is significant. Furthermore, the speed comparison is presented only qualitatively, with no detailed benchmarking methodology described.
- **Why it matters** A fair and rigorous comparison is necessary to support the claim that AIUPred is among the top methods. A single AUC value without variance or statistical testing is insufficient to establish equivalence or superiority. The speed advantage is a key selling point, but it must be quantified with a clear benchmarking protocol.
- **Resolution test** Provide a detailed comparison including multiple evaluation metrics (e.g., AUC, Matthews correlation coefficient, F1 score), confidence intervals or standard deviations, and statistical tests for significance. Describe the hardware and software used for speed benchmarking, and report results for multiple datasets if available.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, paragraph 3
- **Evidence pointer** Location not provided
- **Issue** The statement that "subsequent versions of IUPred, including IUPred2A and IUPred3, have not introduced significant alterations to the underlying energy model" is vague. It is unclear what constitutes a "significant alteration" and how this claim is substantiated.
- **Required correction** Clarify the specific differences between IUPred versions, or provide a reference to a detailed comparison.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Materials and methods, dataset description
- **Evidence pointer** Location not provided
- **Issue** The negative dataset for disorder prediction is described as "a set of globular domains comprises sequence regions which encode single structural domains with determined monomeric structures in the PDB (4549 protein regions)." The criteria for selecting these domains and the redundancy filtering process are not described.
- **Required correction** Provide details on how the negative dataset was constructed, including any sequence identity thresholds and the source of domain definitions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Use cases, Example 1
- **Evidence pointer** Figure 1 is referenced but not provided.
- **Issue** The use case describes qualitative agreement with experimental data but does not provide a quantitative assessment of prediction accuracy for this specific example.
- **Required correction** Consider adding a quantitative comparison, such as the fraction of experimentally verified disordered residues correctly predicted, to strengthen the illustrative value.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Server description, downloadable package
- **Evidence pointer** Location not provided
- **Issue** The downloadable package is described as requiring Python 3.7+, PyTorch, and SciPy, but no version numbers or installation instructions are provided.
- **Required correction** Specify the exact versions of dependencies and provide installation instructions or a link to a repository with detailed setup guidance.

## Risk / unsupported claims
- The claim that AIUPred "scored amongst the top three single sequence based methods" is unsupported in the provided material, as the relevant tables are absent.
- The claim of "great improvement" in accuracy over previous IUPred versions is not quantitatively substantiated without Tables 1 and 2.
- The statement that the energy model was "never trained on disordered regions" and that this enables efficient IDR prediction is an interesting assertion but is not rigorously tested or discussed in terms of potential limitations.
- The speed comparison to SPOT-Disorder-Single is presented without a detailed benchmarking methodology, making the specific speed advantage claim unverifiable.
- The use case examples are qualitative and do not provide quantitative evidence of performance on these specific proteins.