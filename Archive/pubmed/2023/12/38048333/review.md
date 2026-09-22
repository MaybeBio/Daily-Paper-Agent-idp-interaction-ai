## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and supplementary figure legends
- **Assessment boundary** Scientific validity, methodological rigor, claims versus evidence, and suitability for the stated venue
- **Shared manuscript claim summary** The authors present the first empirical comparison of structure-trained versus disorder-trained DNA-binding residue predictors, identify performance gaps across annotation types, and introduce hybridDBRpred, a transformer-based meta-predictor combining three existing tools to achieve statistically superior accuracy and reduced cross-predictions
- **Visible evidence base** Abstract, full methods, results tables referenced but not shown, supplementary figure legends, data availability statements
- **Missing materials affecting confidence** Actual tables (Tables 2 and 3), supplementary figures (S1-S3), supplementary tables (S1 and S2), and the full training/validation/test dataset compositions were not provided. Statistical test details and exact p-values are referenced but not fully visible.

## Reviewer

- **Overall assessment** This manuscript addresses a relevant gap in the protein-DNA interaction prediction field by systematically comparing structure-trained and disorder-trained predictors and proposing a meta-approach to combine their strengths. The motivation is clear and the empirical analysis fills a genuine void. However, the core claims of hybridDBRpred's superiority rest on tables and figures that were not available for inspection, limiting the ability to fully verify the statistical and methodological rigor. The architectural choices are reasonable but the novelty of the transformer application is incremental. The manuscript is well-written and accessible, but several methodological details require clarification before the central claims can be fully accepted.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those developing or using sequence-based predictors of nucleic acid binding. The comparative benchmark data will be useful for method developers, and the meta-predictor offers a practical tool for researchers needing improved DNA-binding residue annotations. The analysis of cross-prediction issues is relevant to the broader community working on binding residue prediction for multiple ligand types.

- **Major strengths**
  1. First systematic comparison of structure-trained versus disorder-trained DBR predictors, addressing a previously unexamined question
  2. Careful dataset construction with low sequence similarity to training sets, reducing optimism bias
  3. Inclusion of cross-prediction analysis, an important but often overlooked aspect of binding residue predictors
  4. Comprehensive ablation study isolating contributions of each architectural innovation
  5. Deployment as a web server and open-source code, supporting reproducibility and community use

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "HybridDBRpred provides accurate predictions and low levels of cross-predictions across the two annotation types, and is statistically more accurate than each of the ten tools and baseline meta-predictors"
- **Evidence pointer** Tables 2 and 3, location not provided
- **Concern** The central performance claims are based on Tables 2 and 3, which were not included in the provided material. Without these data, the statistical significance of hybridDBRpred's improvements over individual predictors and baselines cannot be independently verified. The manuscript states p-values ≤ 0.01 but the actual distributions, effect sizes, and variance measures are not visible.
- **Why it matters** The primary contribution of this work is the demonstration that the meta-predictor outperforms existing tools. If the underlying data are not available for scrutiny, the core claim cannot be validated, and the manuscript's contribution reduces to an architectural proposal without demonstrated efficacy.
- **Resolution test** Provide Tables 2 and 3 with full performance metrics, confidence intervals, and p-values for all pairwise comparisons. Ideally, include raw prediction scores or a reproducible analysis script to allow independent verification.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Methodological clarity
- **Claim pointer** "We use a new test dataset that includes structure- and disorder-annotated proteins that share low similarity to the training datasets of the evaluated methods"
- **Evidence pointer** Materials and methods, Datasets section
- **Concern** The dataset construction is described at a high level, but critical details are missing. The clustering procedure uses Blastclust at 25% similarity, but the exact sequence database, the number of clusters obtained, and the criteria for selecting "the most recently released protein" are not specified. More importantly, the statement that test proteins "share low similarity" to training sets of the evaluated methods is asserted but not demonstrated. The actual pairwise sequence identity distribution between test proteins and each predictor's training set is not reported.
- **Why it matters** The validity of the benchmark depends on the test set being genuinely novel relative to the training data of all evaluated predictors. If some test proteins are similar to training sequences of certain predictors, those predictors would have an unfair advantage, potentially biasing the comparison in favor of or against specific methods.
- **Resolution test** Provide a detailed description of the clustering parameters, the number of clusters, and a quantitative analysis of sequence identity between test proteins and the training sets of each of the ten predictors. Consider reporting the distribution of maximum sequence identity for each test protein against each training set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "We use a sliding window to present the amino acid-level feature in groups 1 and 2 to the model, which provides useful context for the selection of the best input prediction of DBRs"
- **Evidence pointer** Materials and methods, Architecture of the hybridDBRpred section; Figure 1, location not provided
- **Concern** The description of the transformer architecture is incomplete. The manuscript mentions "three stacked transformer modules" but does not specify the number of attention heads, the embedding dimension, the feedforward hidden layer size, the dropout rate, the number of training epochs, or the early stopping criteria. The sliding window size is stated as 15, but the handling of sequence boundaries (padding strategy) is not described. The input feature groups are listed in Supplementary Table S2, which was not provided.
- **Why it matters** Transformer models are highly sensitive to hyperparameter choices. Without these details, the architecture cannot be reproduced, and the claimed benefits of the transformer over simpler baselines cannot be attributed to specific design choices. The ablation study partially addresses this, but the baseline configurations must be fully specified for meaningful comparison.
- **Resolution test** Provide complete architectural specifications, including all hyperparameters, training procedures, and the full list of input features. Consider releasing the training code with a configuration file to ensure reproducibility.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** "We find that disproportionally higher numbers of putative DBRs are located immediately adjacent to a native DBR"
- **Evidence pointer** Results and discussion, Analysis of the putative DNA-binding residues; Figure 2, location not provided
- **Concern** The analysis of false positive localization near native DBRs is interesting, but the interpretation is speculative. The authors suggest that false positives near native DBRs "could be driven by the threshold-dependent nature of annotations, and perhaps should not be treated as mistakes." However, an alternative explanation is that these predictions reflect genuine sequence-level features that are not captured by the structural annotation threshold. The analysis does not distinguish between these possibilities.
- **Why it matters** The claim that performance may be underestimated has implications for how the field interprets prediction accuracy. If the authors wish to make this argument, they need to provide stronger evidence, such as showing that the "false positives" near native DBRs are enriched for known DNA-binding motifs or that they are confirmed by alternative experimental data.
- **Resolution test** Provide additional analysis of the false positive residues near native DBRs, such as conservation analysis, motif enrichment, or comparison with alternative annotation sources. Alternatively, temper the interpretation and present it as a hypothesis requiring further investigation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "We perform 100 random selections of 20 DNA-binding and 40 non-DNA binding proteins, with equal split of the structure- and disorder-annotated proteins, from the benchmark dataset"
- **Evidence pointer** Materials and methods, Datasets section
- **Concern** The statistical testing procedure is described but the rationale for the specific resampling scheme is not justified. The manuscript does not explain why 100 resamples of 20 DNA-binding and 40 non-DNA binding proteins were chosen, nor how this relates to the total test set size. The use of the Anderson-Darling test for normality at 0.05 significance followed by either t-test or Wilcoxon rank-sum test is standard, but the multiple testing correction across the many pairwise comparisons (10 predictors plus baselines) is not mentioned.
- **Why it matters** The resampling scheme affects the statistical power and the interpretation of the p-values. Without multiple testing correction, the probability of false positives increases across the many comparisons made. The choice of 20 DNA-binding proteins per resample may also be too small to capture the variability in the full test set.
- **Resolution test** Justify the resampling scheme with reference to the test set size and expected effect sizes. Report whether multiple testing correction was applied and, if not, discuss the implications. Consider reporting confidence intervals for the performance differences.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "We complete the first empirical analysis" which is grammatically awkward. The phrase "complete" suggests finishing something rather than performing it.
- **Required correction** Change to "We perform the first empirical analysis" or "We present the first empirical analysis."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, evaluation metrics
- **Evidence pointer** Materials and methods, Datasets section
- **Issue** The manuscript defines CPR and OPR but the equations are not fully rendered in the provided text. The definitions are understandable from context but should be clearly presented.
- **Required correction** Ensure the equations for CPR and OPR are properly formatted and defined in the final version.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data availability section
- **Issue** The manuscript states the source code is available on GitHub and Zenodo, but the specific version used for the reported results is not identified. The Zenodo DOI is provided but the GitHub repository link may not be version-stable.
- **Required correction** Include the specific commit hash or version tag of the GitHub repository used for the reported results, and ensure the Zenodo deposit is versioned to match.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, predictor selection
- **Evidence pointer** Materials and methods, Selection of predictors section
- **Issue** The criteria for selecting the "representative collection of ten predictors" from the 34 identified are not fully specified. The manuscript mentions recency, availability, and speed, but the relative weighting of these criteria is unclear.
- **Required correction** Provide a more explicit description of the selection criteria, including any exclusion criteria applied to the 34 predictors.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion of related work
- **Evidence pointer** Introduction
- **Issue** The introduction mentions "a recent survey" for DNA sequence-based predictors but does not cite it explicitly in the provided text. The citation appears to be reference 15, but the context is slightly ambiguous.
- **Required correction** Clarify the citation and ensure the survey is clearly identified in the text.

- **Technical failings that need to be addressed before the case is established**
  R1-M1 (missing performance tables), R1-M2 (incomplete dataset validation), R1-M3 (incomplete architectural details)

- **Assessment against Nature-style criteria**
  - Originality: Moderate. The comparative analysis of structure-trained versus disorder-trained predictors is novel and fills a gap in the literature. The meta-predictor approach itself is not conceptually new, but its application to this specific problem with transformer architecture is a reasonable incremental contribution.
  - Scientific importance: Moderate to high. DNA-binding residue prediction is an active area with practical applications. The identification of performance gaps across annotation types and the cross-prediction analysis have implications for both method development and practical use. However, the importance is somewhat limited by the incremental nature of the meta-predictor improvement.
  - Interdisciplinary readership: Moderate. The work will primarily interest computational biologists and bioinformaticians. The biological implications are clear but not deeply explored, limiting broader appeal to experimental biologists.
  - Technical soundness: Currently not fully assessable. The experimental design is thoughtful, but the missing tables and incomplete methodological details prevent full evaluation. The statistical approach is standard but the multiple testing issue needs addressing.
  - Readability for nonspecialists: Good. The manuscript is clearly written with logical flow. Technical terms are introduced in context. The abstract effectively summarizes the key findings and contributions.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant question with a thoughtful experimental design. The core claims are plausible but cannot be fully verified from the provided materials. If the authors provide the missing tables, complete the methodological details, and address the statistical concerns, the work would be a solid contribution to the field. The current version is not established from the provided evidence due to the missing performance data.

## Risk / unsupported claims
- The claim that hybridDBRpred is "statistically more accurate than each of the ten tools" cannot be verified without Tables 2 and 3.
- The claim that the test dataset shares "low similarity" to training sets of evaluated predictors is asserted but not demonstrated with quantitative data.
- The claim that false positives near native DBRs "could be driven by the threshold-dependent nature of annotations" is speculative and not directly supported by the presented analysis.
- The claim that the transformer architecture provides "large improvements over simpler meta-predictors" is plausible but depends on the ablation results in Supplementary Figures S2 and S3, which were not provided.
- The completeness of the "comprehensive collection of 34 predictors" cannot be verified without a systematic search strategy description.