## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2021)
- **Assessment boundary** Scientific claims, methodology, and reported results as presented in the provided text; no supplementary files, figures, or code were available for inspection
- **Shared manuscript claim summary** The authors present DeepRank-GNN, a graph neural network framework for learning patterns in protein-protein interfaces, and demonstrate its application to scoring docking models, reporting performance competitive with or superior to existing methods (DeepRank, DOVE, HADDOCK, iScore) with significant gains in speed and storage.
- **Visible evidence base** Abstract, Introduction, Methods (Sections 2.1–2.4), Results (Sections 3.1–3.3), Conclusion, Software/Data availability statements
- **Missing materials affecting confidence** All figures (Fig. 1–3), supplementary tables (S1–S17), supplementary figures (S1–S7), code repository, and documentation were not provided. These are essential for verifying architectural details, quantitative results, and reproducibility.

## Reviewer
- **Overall assessment** The manuscript describes a timely and potentially useful software framework that addresses a real limitation of CNN-based approaches (rotation dependence) by adopting graph representations for protein-protein interfaces. The motivation is clear and the modular design philosophy is commendable. However, the evidence presented in the text alone is insufficient to fully evaluate the central performance claims. Key quantitative results are described narratively without access to the corresponding figures or tables, and several methodological details (e.g., exact node feature definitions, hyperparameter choices, statistical significance of performance differences) are either incomplete or not verifiable from the provided material. The work is likely of interest to the structural bioinformatics and machine learning communities, but the case for its superiority over existing methods is not fully established from the supplied evidence.
- **Who would be interested in the results, and why** Computational structural biologists developing or using scoring functions for protein-protein docking; researchers applying graph neural networks to biomolecular problems; developers of deep learning frameworks for structural bioinformatics. The framework's modularity and speed improvements over grid-based CNN approaches could appeal to practitioners needing efficient, rotation-invariant representations of interfaces.
- **Major strengths** 1) Clear identification of a genuine limitation in existing CNN-based approaches (rotation dependence, fixed grid size) and a principled solution via graph representations. 2) The framework is designed to be modular and user-friendly, with support for custom architectures and target values, which enhances its potential utility. 3) The application to docking model scoring is a relevant and practically important benchmark task. 4) The reported computational gains (speed, storage) are practically significant if reproducible.
- **Major Concerns** 
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The claim that DeepRank-GNN "performs better than DeepRank, DOVE and HADDOCK scores and competes with iScore on the CAPRI score set" (Abstract; Section 3.2).
  - **Evidence pointer** Section 3.2; Figures 2 and 3 (not provided); Tables S13–S16 (not provided)
  - **Concern** The central performance comparison is presented only as narrative summary. The actual AUC values, success rates, and statistical variability across folds are not fully reported in the text. The claim of "competing with iScore" is ambiguous without quantitative comparison (e.g., mean and standard deviation of AUC across folds, per-complex breakdown). The dependence of results on the specific fold (e.g., "fold6 model") raises questions about model selection and whether the reported performance is cherry-picked.
  - **Why it matters** The primary scientific contribution is the demonstration that the GNN approach achieves state-of-the-art or competitive performance. Without the actual data, the reader cannot assess the magnitude of the improvement, its statistical robustness, or whether the comparison was fair (e.g., same training data, same test split, same evaluation metrics).
  - **Resolution test** Provide the full quantitative results in the main text or accessible supplementary material, including per-fold performance, mean±SD for all metrics, and a direct statistical comparison (e.g., paired tests) against all baselines. Clarify the model selection procedure (e.g., why fold6 was chosen as "best").
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Methodological completeness
  - **Claim pointer** The description of the GINet architecture and its components (Section 3.1, Figure 1B) is claimed to be a "new graph neural network architecture" with specific design choices (two distinct GCLs for interface and internal graphs, attention mechanism, pooling via MCL or Louvain).
  - **Evidence pointer** Section 3.1; Figure 1 (not provided); Equations 2, 4, 5 (partially described)
  - **Concern** The architectural description is incomplete. The exact formulation of the attention mechanism (Equations 4 and 5) is not fully specified in the text; the dimensions of the node and edge features are not listed; the number of layers, hidden units, and the specific pooling strategy (max pooling over clusters) are described but not quantified. The novelty of the architecture relative to existing GNN variants (e.g., standard GAT, EdgeConv) is not clearly delineated. The choice of MCL versus Louvain and its impact on performance is not discussed.
  - **Why it matters** For a methods paper, the architecture must be described with sufficient detail to be reproduced. The claimed novelty of GINet cannot be assessed without a complete specification. The choice of clustering algorithm for pooling could significantly affect results and needs justification.
  - **Resolution test** Provide a complete mathematical specification of the GINet layers, including all equations, tensor dimensions, and hyperparameters. Clearly state the novelty relative to existing GNN architectures. Report results with both MCL and Louvain pooling, or justify the choice of one.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility and data availability
  - **Claim pointer** The manuscript states that the software is freely available and that the data can be downloaded from a repository (Software and Data Availability sections).
  - **Evidence pointer** Software availability; Data availability; Section 2.1
  - **Concern** While the software link is provided, the manuscript does not specify the exact version of the code used for the reported experiments, nor does it provide a configuration file or a reproducible pipeline (e.g., random seeds, exact data splits, preprocessing steps). The data repository link is given, but the specific files used for training/testing are not enumerated. The statement that "a number of complexes displaying important clashes could not be converted into graphs" (Section 2.1) introduces an exclusion criterion that is not quantified or described in detail.
  - **Why it matters** Reproducibility is a core requirement for computational methods. Without exact versioning, configuration, and data handling details, independent verification of the results is difficult or impossible.
  - **Resolution test** Provide a versioned release of the code, a configuration file or script that reproduces the exact experiments, and a detailed description of the data preprocessing and exclusion criteria. Specify the number of complexes excluded and the reason.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Baseline comparison fairness
  - **Claim pointer** The comparison with DeepRank, DOVE, HADDOCK, and iScore (Section 3.2) implies that these baselines were evaluated under comparable conditions.
  - **Evidence pointer** Section 3.2; Section 2.1
  - **Concern** The text states that scores for DeepRank, DOVE, and HADDOCK were "computed on the CAPRI score set as described in Renaud et al., 2021." It is unclear whether the same train/test splits were used for all methods, whether the baselines were retrained or used as pre-trained models, and whether the evaluation metrics (AUC, success rate) were computed identically. The iScore results are referenced from the literature, which may have used different data splits or evaluation protocols.
  - **Why it matters** Fair comparison is essential for the claim of competitive or superior performance. Differences in data splits, training procedures, or metric definitions can materially affect the outcome.
  - **Resolution test** Clearly describe the evaluation protocol for all baselines, including data splits, training procedures, and metric computation. If iScore results are taken from the literature, state this explicitly and discuss potential differences in protocol.
- **Minor Comments** 
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of writing
  - **Affected element** Section 2.2, target value computation
  - **Evidence pointer** Section 2.2
  - **Issue** The rationale for choosing f nat over iRMSD or lRMSD as the target value is stated, but the sentence is grammatically awkward ("the f nat value is caped between 0 and 1, thus giving the same weight to all bad quality model"). The phrase "caped" should be "capped," and "model" should be "models."
  - **Required correction** Revise the sentence for grammatical correctness and clarity. For example: "The f nat value is capped between 0 and 1, thus assigning the same weight to all poor-quality models."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness of information
  - **Affected element** Section 2.1, dataset description
  - **Evidence pointer** Section 2.1
  - **Issue** The text mentions "23 500 models" generated with HADDOCK and then states "The overall dataset comprises 3337000 models." The relationship between these two numbers is unclear. It appears that 23,500 models were generated per complex, but this is not explicitly stated.
  - **Required correction** Clarify the relationship between the number of models per complex and the total dataset size. For example: "We generated 23,500 models per complex using HADDOCK, resulting in a total of 3,337,000 models across all complexes."
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical accuracy
  - **Affected element** Section 3.1, equation 2
  - **Evidence pointer** Section 3.1
  - **Issue** The text refers to "equation 2" for the interaction strength but does not provide the equation in the text. The equation is presumably in a figure or supplementary material, but this is not stated.
  - **Required correction** Either include the equation in the main text or explicitly refer to the figure or supplementary section where it can be found.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Section 3.2, performance variability
  - **Evidence pointer** Section 3.2
  - **Issue** The text notes "a variation in the performance depending on the data subset used for the training and the evaluation of the models" but does not report the range or standard deviation of the AUC across folds in the main text.
  - **Required correction** Report the mean and standard deviation (or range) of the AUC across the 10 folds in the main text or refer explicitly to the supplementary figure where this is shown.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section 3.2, "success rate"
  - **Evidence pointer** Section 3.2
  - **Issue** The term "success rate" is used but not defined in the text. It is presumably the fraction of complexes with at least one acceptable model in the top N, but this should be stated explicitly.
  - **Required correction** Define "success rate" when first used, e.g., "the success rate is defined as the fraction of complexes for which at least one acceptable-quality model is found within the top N ranked models."

## Technical failings that need to be addressed before the case is established
- R1-M1 (performance claims not verifiable without figures/tables)
- R1-M2 (incomplete architectural specification)
- R1-M3 (reproducibility details missing)
- R1-M4 (baseline comparison protocol unclear)

## Risk / unsupported claims
- The claim that DeepRank-GNN "performs better than DeepRank, DOVE and HADDOCK scores and competes with iScore" is unsupported in the provided text because the actual quantitative results are not included.
- The claim of "significant gain in speed and storage requirement" is not verifiable without the referenced tables (S13–S16).
- The statement that "most GCL models globally perform equally or better than the HADDOCK scoring function" is a narrative summary without the underlying data.
- The claim that "iScore and DeepRank-GNN rank 1st and 2nd" on the CAPRI score set is not verifiable without the comparison data.
- The assertion that "simple geometric and physico-chemical properties could be as informative as (or more than) the approximative energy terms" is speculative and not directly tested in the presented results.

## Assessment against Nature-style criteria
- **Originality** Moderate. The application of GNNs to protein-protein interface scoring is not entirely new (iScore uses graph kernels), but the specific framework design, modularity, and the GINet architecture may offer incremental novelty. The authors do not clearly position their contribution relative to other GNN-based approaches (e.g., IGNN, GraphPPI).
- **Scientific importance** Moderate to high. Reliable scoring of docking models is a bottleneck in structural biology, and improvements in speed and accuracy are practically valuable. However, the importance of the specific framework depends on the robustness of the performance claims, which are not fully verifiable here.
- **Interdisciplinary readership** Moderate. The work bridges machine learning and structural biology, and the modular design could attract users from both communities. However, the manuscript assumes familiarity with both GNN concepts and protein-protein docking, which may limit accessibility.
- **Technical soundness** Not fully assessable. The methodological description is incomplete, and the key results are not presented in the text. The computational performance comparisons are referenced but not shown.
- **Readability for nonspecialists** Adequate but improvable. The introduction and motivation are clear, but the methods section contains jargon and incomplete descriptions that would challenge a nonspecialist. The grammatical errors noted above also detract from readability.

## Recommendation posture
Currently not established from the provided evidence. The manuscript describes a promising framework, but the central performance claims cannot be verified without the figures, tables, and supplementary materials. The methodological description is incomplete, and the baseline comparison protocol is unclear. The authors should be invited to resubmit a revised version that includes the full quantitative results, a complete architectural specification, and detailed reproducibility information.