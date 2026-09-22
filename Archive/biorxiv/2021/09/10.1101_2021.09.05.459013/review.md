## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, acknowledgements, footnotes)
- **Assessment boundary** Scientific content, methodological soundness, claims vs. evidence, clarity, and suitability for a high-impact generalist journal
- **Shared manuscript claim summary** The authors present ScanNet, an end-to-end interpretable geometric deep learning model that learns spatio-chemical patterns directly from protein 3D structures to predict protein-protein binding sites and B-cell epitopes. They claim state-of-the-art performance, interpretability of learned filters, robustness to conformational change, and utility for unseen folds, with a demonstration on SARS-CoV-2 spike protein epitopes.
- **Visible evidence base** Main text figures (Fig. 1–5), tables (Table I), supplementary figures and tables referenced (S1–S22, S1–S4), methods sections A–G
- **Missing materials affecting confidence** Supplementary figures and tables not provided in the submitted material; exact numerical results for all comparisons not fully specified; details of baseline implementations partially described; no code or data availability at time of review

## Reviewer
- **Overall assessment** This manuscript introduces a novel geometric deep learning architecture for structure-based prediction of protein binding sites, with a strong emphasis on interpretability. The approach is technically sound, well-motivated, and the results are promising. The interpretability analysis is a significant strength that distinguishes this work from many black-box deep learning methods. However, several technical concerns and missing details limit the current strength of the claims, particularly regarding generalizability, comparison fairness, and statistical robustness. The manuscript is well-written and accessible, but requires revisions to fully establish the case.
- **Who would be interested in the results, and why** Computational biologists, structural bioinformaticians, and researchers in protein function prediction would be the primary audience. The interpretability aspect will also appeal to the broader machine learning community interested in geometric deep learning. The SARS-CoV-2 application extends relevance to virology and immunology researchers.
- **Major strengths** 1) Novel architecture that learns directly from raw 3D coordinates with built-in interpretability, addressing a key limitation of many deep learning models. 2) Comprehensive evaluation against multiple baselines, including a structural homology method and a handcrafted-feature ML model. 3) Detailed interpretability analysis with visualization of learned filters, connecting model behavior to known biochemical concepts. 4) Robustness analysis on conformational changes and noisy labels. 5) Practical utility demonstrated through a webserver and application to a relevant biological problem.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (comparison fairness with Masif-site), R1-M2 (statistical significance of performance differences), R1-M3 (generalizability claims), R1-M4 (interpretability validation)
- **Assessment against Nature-style criteria**  
  *Originality*: High. The architecture combines existing concepts (neighborhood convolution, attention) in a novel way tailored to protein structures, with a focus on interpretability that is relatively underexplored in this domain.  
  *Scientific importance*: Moderate to high. Accurate and interpretable binding site prediction has broad utility in functional annotation and drug discovery. The SARS-CoV-2 application adds timely relevance.  
  *Interdisciplinary readership*: Moderate. The work bridges structural biology and deep learning, but the technical depth may limit accessibility to a purely biological audience. The interpretability angle could broaden appeal.  
  *Technical soundness*: Generally sound, but several concerns (see Major Concerns) need addressing, particularly around comparison fairness and statistical validation.  
  *Readability for nonspecialists*: Good. The manuscript is clearly written, with helpful figures and intuitive explanations of the architecture. Some methods sections are dense but appropriate for the target audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core ideas are novel and promising, but the current evidence does not fully establish the claimed advantages over existing methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparison fairness
- **Claim pointer** "ScanNet outperforms baseline methods based on ML, structural homology and surface-based geometric deep learning" (Abstract, Results Section B)
- **Evidence pointer** Table I, Sup. Fig. S17, Methods Section B
- **Concern** The comparison with Masif-site is potentially unfair. The authors state that Masif-site was not retrained on their dataset and that the test set overlaps with Masif-site's training set. This creates a confounding factor: Masif-site may perform worse on the test set due to domain shift, or better due to memorization. The authors acknowledge this limitation but still report Masif-site's performance in the main comparison table, which could mislead readers.
- **Why it matters** A fair comparison is essential to support the claim of state-of-the-art performance. If Masif-site were retrained on the same data, the performance gap might narrow or even reverse. The current presentation overstates the relative advantage of ScanNet.
- **Resolution test** Retrain Masif-site on the same training set (or a comparable subset) and report its performance on the same test set. Alternatively, clearly separate the "as-is" comparison from a "retrained" comparison and discuss the implications of each.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** "ScanNet achieved an AUCPR of 0.694... the best performance by a substantial margin" (Results Section B)
- **Evidence pointer** Table I, Sup. Fig. S17
- **Concern** No statistical significance testing is reported for the performance differences between ScanNet and the baselines. The AUCPR values are presented as point estimates without confidence intervals or error bars. Given the potential for variance across different train/test splits, it is unclear whether the observed differences are statistically meaningful.
- **Why it matters** Without statistical validation, the claim of "substantial margin" is not rigorously supported. This is particularly important given the known variance in deep learning model performance and the relatively small test sets in some homology-based subgroups.
- **Resolution test** Report confidence intervals (e.g., via bootstrapping) or perform significance tests (e.g., paired tests across test set samples) for the primary performance metrics. If computational cost is a concern, at least report variance across multiple training runs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** "demonstrate its accuracy - including for unseen protein folds" (Abstract); "ScanNet could both recognize previously seen folds and generalize to unseen ones" (Results Section B)
- **Evidence pointer** Fig. 2, Sup. Fig. S4(g)
- **Concern** The "unseen folds" claim is based on the homology-based subgroups (Val/Test Topology and Val/Test None). However, the definition of "unseen" is based on CATH classification at the topology level, which may still allow significant structural similarity. Additionally, the performance in the "None" subgroup is not explicitly quantified in the main text, and it is unclear how much the overall AUCPR is driven by the high-homology subgroups.
- **Why it matters** The ability to generalize to truly novel folds is a key selling point of the method. If the "unseen" subgroups are small or the performance drop is substantial, the claim may be overstated.
- **Resolution test** Report the AUCPR and other metrics separately for each homology subgroup, with sample sizes. Discuss the performance drop from high to low homology and whether the "None" subgroup is sufficiently large and diverse to support the generalization claim.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability validation
- **Claim pointer** "Through appropriate parameterization and regularization, the filters learnt by ScanNet can be readily visualized and interpreted" (Introduction, Results Section C)
- **Evidence pointer** Fig. 3, Fig. 4, Sup. Fig. S18, S19
- **Concern** The interpretability analysis is qualitative. The authors show that some filters resemble known motifs (e.g., hydrogen bonds, O-rings), but there is no quantitative assessment of how well the learned filters correspond to ground-truth structural or chemical features. The correlation between filter activities and binding energy components (Sup. Fig. S7) is a step in this direction, but it is limited to a small set of filters and energy terms.
- **Why it matters** Interpretability is a central claim of the paper. Without quantitative validation, the interpretability analysis remains suggestive rather than conclusive. This weakens the paper's contribution to the broader goal of understanding what deep learning models learn from protein structures.
- **Resolution test** Provide a more systematic evaluation, e.g., by comparing learned filters to a set of predefined structural motifs (e.g., secondary structure elements, hydrogen bond donors/acceptors, hydrophobic patches) and reporting overlap or enrichment statistics. Alternatively, use a perturbation-based analysis to show that specific filters are necessary and sufficient for predictions on specific motif-containing sites.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "demonstrate its accuracy - including for unseen protein folds" but does not provide any numerical results. This makes it difficult for a reader to gauge the magnitude of the claimed performance.
- **Required correction** Include key performance numbers (e.g., AUCPR) in the abstract, or at least a qualitative comparison with baselines.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods Section A
- **Evidence pointer** Methods Section A
- **Issue** The description of the network architecture, while detailed, lacks some specifics needed for exact reproduction, such as the exact number of filters per layer, the learning rate schedule, and the data augmentation strategy (if any).
- **Required correction** Provide a complete table of hyperparameters and training details, or make the code available at the time of review.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results Section B
- **Evidence pointer** Table I
- **Issue** The AUCPR values are reported to three decimal places, which may imply a precision that is not warranted given the potential variance. Additionally, the table does not include the number of test samples per subgroup.
- **Required correction** Report AUCPR with appropriate precision (e.g., two decimals) and include sample sizes in the table or legend.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Comparison completeness
- **Affected element** Results Section B
- **Evidence pointer** Table I, Sup. Fig. S17
- **Issue** The comparison with Discotope is only mentioned for the BCE task, not for PPBS. It would be informative to include Discotope (or a similar method) as a baseline for PPBS as well, if applicable.
- **Required correction** Either add Discotope to the PPBS comparison or justify its exclusion.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results Section D
- **Evidence pointer** Sup. Fig. S5
- **Issue** The analysis of conformational change effects is described briefly. The correlation values (r = 0.86, 0.78) are reported, but it is unclear how these translate to practical prediction accuracy on unbound structures.
- **Required correction** Report the AUCPR or accuracy on unbound structures, not just correlations, to give a clearer picture of practical utility.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Availability section
- **Evidence pointer** Availability section
- **Issue** The data and code availability statement says "will be released upon publication," which is standard but limits the ability of reviewers and readers to verify the results.
- **Required correction** Consider providing access to the code and data during review, or at least a detailed description of the data processing pipeline.

## Risk / unsupported claims
- The claim that ScanNet "learns some of the underlying physical principles of binding" (Discussion) is supported only by qualitative filter visualization and a limited correlation analysis. This is a strong claim that requires more rigorous validation.
- The claim of "state-of-the-art" performance is not fully supported due to the unfair comparison with Masif-site and lack of statistical testing.
- The generalizability to "unseen protein folds" is not fully quantified, and the definition of "unseen" may be too lenient.
- The claim that ScanNet is "suitable for functional site prediction tasks" broadly is not fully established, as only two related tasks (PPBS and BCE) are demonstrated.