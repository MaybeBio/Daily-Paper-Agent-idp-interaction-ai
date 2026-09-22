## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, availability statements) as provided in the submission.
- **Assessment boundary** Scientific and technical evaluation of the method, experimental design, reported results, and claims as presented. No assessment of code functionality or reproducibility beyond what is described in the text.
- **Shared manuscript claim summary** The authors present INTREPPPID, a deep learning method for protein-protein interaction (PPI) prediction that incorporates orthology information via a "quintuplet" network architecture. They claim state-of-the-art performance on both intra-species and cross-species PPI prediction tasks under strict evaluation protocols, and further claim that the performance gain is attributable to the biological relevance of orthology information. They also introduce two community resources: PPI.bio (a web server) and PPI Origami (a dataset generation tool).
- **Visible evidence base** Abstract, Introduction, Materials and Methods (partial), Results (partial), Discussion, Software and Data Availability, Supplementary Material descriptions. Tables and figures referenced but not fully visible: Table 1, Figures 2, 3, 4, 5, Supplementary Tables S1-S5, Supplementary Files S1-S2.
- **Missing materials affecting confidence** Full methods details (loss function equations, training hyperparameters beyond optimizer, dataset construction specifics), complete results tables and figures, statistical test details, baseline method configurations, and the actual supplementary files. The manuscript text contains placeholders where equations and figures should be, which limits verification of the technical claims.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant problem in computational biology: improving cross-species PPI prediction, which is important for studying non-model organisms. The proposed architecture is a reasonable extension of the authors' prior work (RAPPPID) with a clear rationale for incorporating orthology information. The strict evaluation protocol is commendable and aligns with best practices highlighted by prior work. However, the manuscript as provided has significant gaps in the methods and results sections that prevent full evaluation of the claims. The central claim that orthology information improves performance due to biological relevance is supported by the scrambling experiment, but the magnitude of improvement over RAPPPID appears modest. The community resources are valuable contributions. Overall, the work is potentially publishable but requires substantial clarification and additional analysis to fully support the claims.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on PPI prediction, particularly those interested in cross-species generalization and strict evaluation methodologies. Researchers studying non-model organisms who need computational tools for PPI inference would benefit from the web server. Developers of deep learning methods for biological sequence analysis may be interested in the quintuplet architecture and the orthologous locality task as a form of auxiliary supervision.
- **Major strengths** 1) Addresses an important and timely problem: cross-species PPI prediction for understudied organisms. 2) Adopts strict evaluation protocols (C3 splitting, sequence similarity control) which are methodologically sound and address known pitfalls in the field. 3) The scrambling experiment is a well-designed control that directly tests the contribution of orthology information. 4) The authors provide two practical resources (PPI.bio and PPI Origami) that could benefit the community. 5) The parameter sharing between the twin and triplet networks is an efficient design choice that avoids a large increase in model size.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The manuscript text contains placeholders for equations and figures, making it impossible to verify the technical details of the loss functions, architecture, and experimental results. The methods section is incomplete regarding dataset construction specifics, hyperparameter choices, and baseline configurations. The results section lacks the actual data tables and figures needed to assess the magnitude and statistical significance of the reported improvements.
- **Assessment against Nature-style criteria** Originality: The quintuplet architecture and the orthologous locality task are novel contributions, though they build directly on existing triplet network and contrastive learning concepts. Scientific importance: Cross-species PPI prediction is a significant problem, and the strict evaluation framework is valuable. Interdisciplinary readership: The work is primarily of interest to computational biologists; the biological insights are limited. Technical soundness: The approach is technically reasonable, but the incomplete methods prevent full assessment. Readability for nonspecialists: The manuscript is generally well-written but assumes familiarity with deep learning and PPI prediction terminology.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is sound and the evaluation approach is rigorous, but the manuscript requires substantial completion of the methods and results sections, additional analysis to quantify the improvement over RAPPPID, and clarification of several technical points before the claims can be fully assessed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that INTREPPPID outperforms all leading PPI inference methods on both intra-species and cross-species tasks using strict evaluation datasets.
- **Evidence pointer** Table 1, Figure 3A, Supplementary Table S4 (location not provided in the text)
- **Concern** The results section references Table 1 and Figure 3A but the actual data are not visible in the provided manuscript. The claim of outperforming all leading methods cannot be verified without the full results tables, including confidence intervals, standard deviations across the three datasets, and the specific metrics reported. Additionally, the statistical test mentioned (one-sided Wilcoxon signed rank test vs. RAPPPID = 0.03) is only reported for one comparison, and it is unclear whether similar tests were performed against all other baselines.
- **Why it matters** The central claim of the manuscript is that INTREPPPID achieves superior performance. Without the actual results data, this claim is unverifiable. The magnitude of improvement over RAPPPID is particularly important, as the authors state that INTREPPPID "performed slightly better than RAPPPID" in the intra-species task, which raises questions about whether the added complexity of the orthologous locality task is justified.
- **Resolution test** Provide the full results tables with all metrics, standard deviations, and statistical significance tests for all comparisons. Report effect sizes and confidence intervals. Clarify whether the improvement over RAPPPID is statistically significant in both intra-species and cross-species tasks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the orthologous locality loss increases performance because of the biological relevance of the orthologue data, and not due to some other aspect of the architecture.
- **Evidence pointer** Supplementary Table S5, Figure 4B (location not provided in the text)
- **Concern** The scrambling experiment is a good control, but the manuscript reports only that performance dropped to near random (AUROC = 0.524) in the scrambled case. It is unclear whether this experiment was repeated multiple times with different random seeds, whether the scrambled labels were generated once or multiple times, and whether the observed drop is statistically significant. Additionally, the claim that the effect is due to "biological relevance" rather than "some other specious aspect of the architecture" requires additional controls, such as training with randomly initialized orthology labels that are not scrambled but are permuted across training runs, or using a different auxiliary task (e.g., predicting protein family membership) to test whether any auxiliary task would produce similar gains.
- **Why it matters** The authors make a strong mechanistic claim about why their method works. If the improvement is simply due to the auxiliary task providing additional supervision signal, then the biological interpretation is overstated. The scrambling experiment is necessary but not sufficient to establish the biological relevance claim.
- **Resolution test** Provide details on the number of scrambling replicates and statistical significance of the performance drop. Add control experiments with alternative auxiliary tasks or non-biological label perturbations to strengthen the claim that orthology specifically is responsible for the improvement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript describes the INTREPPPID architecture and loss function, including the triplet margin loss with a fixed margin m = 1.
- **Evidence pointer** Materials and Methods, INTREPPPID architecture section (location not provided in the text)
- **Concern** The methods section contains placeholders where equations should be. The triplet loss formulation is described in words but the exact equation is not visible. The choice of margin m = 1 is stated but no sensitivity analysis is provided. It is unclear whether the performance is sensitive to this hyperparameter. Additionally, the manuscript states that the anchor protein is chosen as sβ when orthologues are known, but it is not clear how the anchor is selected when sβ has no known orthologues, or how the triplet task is balanced with the classification task during training (e.g., loss weighting).
- **Why it matters** The triplet loss and its margin are central to the proposed method. Without the exact formulation and hyperparameter sensitivity analysis, it is difficult to assess the robustness of the approach or to reproduce the results. The training dynamics between the two loss terms also affect the final learned representations.
- **Resolution test** Provide the full equations for all loss components. Include a sensitivity analysis for the margin parameter and the relative weighting of the two losses. Clarify the anchor selection strategy for proteins without known orthologues.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that PPI.bio can perform proteome-scale inference in about fifteen minutes.
- **Evidence pointer** Discussion section, PPI.bio description (location not provided in the text)
- **Concern** The claim of fifteen-minute proteome-scale inference is made without specifying the hardware used, the size of the proteome, or the number of queries. This performance claim is difficult to evaluate without these details. Additionally, the manuscript does not describe the computational resources required for training INTREPPPID, which is relevant for reproducibility.
- **Why it matters** Performance claims are important for users deciding whether to use the tool. Without hardware specifications and benchmark details, the claim is not reproducible or comparable to other methods.
- **Resolution test** Provide benchmark details including hardware specifications, proteome size, and query count. Report training time and resource requirements for INTREPPPID.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction (location not provided in the text)
- **Issue** The abstract states that INTREPPPID "outperforms all other leading PPI inference methods tested" but the Introduction does not clearly define the scope of "leading methods" or the criteria for inclusion. The term "leading" is subjective.
- **Required correction** Specify the criteria for selecting baseline methods and clarify whether the claim applies to all tested methods or a specific subset.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section
- **Evidence pointer** Results, Table 1, Figure 3A (location not provided in the text)
- **Issue** The manuscript reports mean AUROC values but does not consistently report standard deviations or confidence intervals across the three datasets. The variability across datasets is mentioned for D-SCRIPT but not systematically reported for all methods.
- **Required correction** Report standard deviations or confidence intervals for all metrics and all methods across the three datasets.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, Training procedure
- **Evidence pointer** Materials and Methods, Training procedure (location not provided in the text)
- **Issue** The training procedure mentions the Ranger21 optimizer and a learning rate schedule but does not specify the batch size, number of training steps, early stopping criteria, or the hardware used for training.
- **Required correction** Provide complete training details including batch size, number of epochs, early stopping criteria, and hardware specifications.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Software and Data Availability
- **Evidence pointer** Software and Data Availability section (location not provided in the text)
- **Issue** The manuscript states that datasets are deposited in Zenodo but does not specify which datasets correspond to which record numbers. It is unclear whether the raw data, processed data, or both are available.
- **Required correction** Clarify the contents of each Zenodo deposit and provide direct links to the datasets used in the study.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Biological interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion (location not provided in the text)
- **Issue** The discussion compares the orthologous locality task to contrastive self-supervised learning methods like SimCLR. While the analogy is reasonable, the discussion does not address potential limitations of this analogy, such as the fact that orthology is a discrete relationship rather than a continuous augmentation.
- **Required correction** Acknowledge the limitations of the analogy and discuss whether the orthologous locality task could be replaced by other forms of auxiliary supervision.

## Risk / unsupported claims
- The claim that INTREPPPID "outperforms all other leading PPI inference methods tested" is unverifiable without the full results tables and statistical analyses.
- The claim that the performance gain is due to "the biological relevance of the orthologue data" is supported by the scrambling experiment but requires additional controls to rule out alternative explanations.
- The claim that PPI.bio can perform proteome-scale inference in about fifteen minutes is unsupported without hardware and benchmark details.
- The claim that the orthologous locality task is "complimentary to the PPI classification task" is based on the scrambling experiment but the mechanism is not fully established.
- The manuscript states that INTREPPPID "performed slightly better than RAPPPID" in the intra-species task, which is a weak claim that may not justify the added complexity of the method.