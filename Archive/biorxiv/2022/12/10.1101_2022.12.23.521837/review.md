## Review setup
- **Input scope** Full manuscript text, including abstract, main text, figures (legends not fully provided), methods, and supplementary table titles.
- **Assessment boundary** Scientific validity, technical soundness, clarity of claims, and adequacy of evidence as presented in the provided manuscript text. Experimental details in the Methods are assessed for completeness based on the text provided.
- **Shared manuscript claim summary** The authors present HydRA, a hybrid ensemble machine-learning classifier that integrates protein-protein interaction (PPI) context and protein sequence information to predict RNA-binding capacity. The model reportedly outperforms existing sequence-based classifiers, enables domain-level prediction via Occlusion Mapping, and is validated by eCLIP experiments for selected candidates.
- **Visible evidence base** Main text figures (Figure 1-6, S1-S9) are referenced but not fully visible in the provided material. Methods section provides details on model architecture, training, and eCLIP procedures. Supplementary table titles are listed.
- **Missing materials affecting confidence** Figure contents and legends are not provided, preventing direct assessment of data quality, statistical significance, and effect sizes. Specific numerical results (e.g., AUC values, p-values) are mentioned in text but not fully contextualized. Details on hyperparameter tuning, cross-validation splits, and baseline comparisons are incomplete.

## Reviewer
- **Overall assessment** The manuscript presents a potentially valuable computational resource for RBP prediction, with a novel combination of PPI and sequence-based features. The inclusion of Occlusion Mapping for domain-level prediction is a notable advance. However, the current evidence base is insufficient to fully evaluate the claims of "unparalleled" performance and the biological significance of the eCLIP validations. The lack of visible figures and detailed statistical reporting limits the ability to assess technical soundness and reproducibility.
- **Who would be interested in the results, and why** Researchers in RNA biology, computational biology, and genomics would be interested. The tool could aid in prioritizing RBP candidates from high-throughput screens and in annotating RNA-binding domains, which is relevant for understanding post-transcriptional regulation and disease mechanisms.
- **Major strengths**
    1.  The conceptual advance of combining PPI context with sequence-based deep learning is well-motivated and addresses a known limitation of sequence-only methods.
    2.  The use of Occlusion Mapping to provide domain-level predictions is a practical and useful feature for experimental validation.
    3.  The inclusion of eCLIP validation for a subset of predictions, including domain-deletion experiments, strengthens the biological relevance of the findings.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** "HydRA outperforms all available state-of-the-art RBP classifiers" and "unparalleled specificity and sensitivity".
    - **Evidence pointer** Figures 3B, S3C, S2A, S2B; Table S1.
    - **Concern** The claim of superior performance is based on comparisons with other tools, but the details of these comparisons are not fully described. It is unclear if the same training/testing splits, hyperparameter optimization, and evaluation metrics were used for all methods. The text mentions ROC-AUC and PR-AUC, but the specific values for each method and the statistical significance of differences are not reported in the provided text. Furthermore, the performance on "uncharacterized RBPs" is highlighted, but the definition and composition of this set are not clearly defined.
    - **Why it matters** Without a rigorous and transparent comparison, the central claim of the manuscript cannot be verified. The reported performance could be due to dataset-specific artifacts or unfair comparisons, which would undermine the utility of HydRA for the community.
    - **Resolution test** Provide a detailed table (e.g., in Table S1) with performance metrics (AUC, PR-AUC, F1, MCC) for HydRA and all baseline methods on the same test set, including confidence intervals. Describe the hyperparameter tuning process for each method and ensure that all methods are evaluated under identical conditions. Clearly define the "characterized" and "uncharacterized" RBP sets and provide a breakdown of performance on each.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness
    - **Claim pointer** "HydRA enables Occlusion Mapping to robustly detect known RNA-binding domains and to predict hundreds of uncharacterized RNA-binding domains."
    - **Evidence pointer** Figures 5, S8, S7; Table S3.
    - **Concern** The Occlusion Mapping methodology is described, but the validation of its predictions is not fully detailed. The claim of "robustly detect[ing] known RNA-binding domains" requires a quantitative comparison against a gold-standard set of domains. The eCLIP validation for domain-deletion mutants is presented for a few candidates, but the criteria for selecting these candidates and the statistical power of the eCLIP experiments are not fully described. The list of "hundreds of uncharacterized RNA-binding domains" is presented, but the evidence supporting these predictions is not shown in the text.
    - **Why it matters** The domain-level prediction is a key novelty of the work. If the validation is not rigorous, the predictions may be unreliable, and the biological conclusions drawn from them (e.g., the role of specific domains in RNA binding) would be unsupported.
    - **Resolution test** Provide a quantitative evaluation of Occlusion Mapping against known RBDs (e.g., from Pfam or RBPDB), including precision-recall curves. For the eCLIP validation, provide a clear description of the experimental design, including the number of replicates, the statistical tests used to compare FL vs. DD binding, and the effect sizes. Show the eCLIP data for the domain-deletion mutants in a clear format (e.g., genome browser tracks or scatter plots) to demonstrate the loss of binding.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Reproducibility
    - **Claim pointer** "The HydRA software and Occlusion Map are open source and available at https://github.com/YeoLab/HydRA."
    - **Evidence pointer** Data and code availability section.
    - **Concern** While the code is stated to be available, the manuscript does not provide a detailed description of the software environment, dependencies, or a step-by-step guide for reproducing the main results. The trained model weights are mentioned, but it is unclear if the exact training data and preprocessing steps are fully documented.
    - **Why it matters** For a computational tool, reproducibility is essential. Without clear documentation, other researchers may not be able to use or build upon the method effectively, limiting its impact.
    - **Resolution test** Provide a detailed README file in the repository with instructions for installation, data preparation, model training, and inference. Include a script to reproduce the main results (e.g., performance on the test set) and specify the exact versions of all software dependencies.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract and Introduction
    - **Evidence pointer** Abstract, Introduction
    - **Issue** The abstract states "unparalleled specificity and sensitivity" which is a strong claim. The introduction could be more concise in describing the limitations of existing methods.
    - **Required correction** Rephrase "unparalleled" to "high" or "state-of-the-art" and provide a more balanced view of existing methods in the introduction.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods: Dataset and Known RBPs collection
    - **Evidence pointer** Methods section
    - **Issue** The description of the positive and negative training sets is incomplete. It is unclear how non-RBPs were selected and whether the set is balanced.
    - **Required correction** Provide a clear description of the negative set, including the number of proteins and the criteria for selection. State the class balance in the training set.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods: Occlusion Mapping
    - **Evidence pointer** Methods section
    - **Issue** The description of the Occlusion Mapping procedure is somewhat brief. The choice of window size (20 amino acids) and the method for calculating p-values are mentioned but not fully justified.
    - **Required correction** Provide a more detailed explanation of the Occlusion Mapping algorithm, including the rationale for the window size and the statistical test used.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Results: HSP90 and YWHA sections
    - **Evidence pointer** Results section
    - **Issue** The description of the eCLIP results for HSP90 and YWHA is dense and could be clearer. The key findings (e.g., binding site enrichment in 3' UTRs) are mentioned but not fully explained.
    - **Required correction** Consider adding a summary figure or table that clearly shows the top binding motifs, the distribution of binding sites across transcript regions, and the results of the domain-deletion experiments.

## Risk / unsupported claims
- The claim of "unparalleled specificity and sensitivity" is not supported by the evidence provided in the text, as detailed comparisons are missing.
- The claim that Occlusion Mapping "robustly detect[s] known RNA-binding domains" is not quantitatively supported in the provided text.
- The statement that HydRA predicts "1,487 unclassified RBPs" is presented, but the false discovery rate and the criteria for this prediction are not fully described.
- The biological significance of the eCLIP results for HSP90 and YWHA is suggested but not fully established, as the functional consequences of the observed RNA binding are not explored.