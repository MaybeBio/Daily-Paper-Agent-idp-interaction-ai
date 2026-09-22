## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, conclusions, and data availability statements.
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and presentation quality. No assessment of editorial fit or publication policy.
- **Shared manuscript claim summary** The authors evaluate three simple computational metrics (normalized radius of gyration, normalized second virial coefficient, and a newly proposed "expenditure density") for predicting phase separation propensity of intrinsically disordered proteins (IDPs). Using coarse-grained molecular dynamics simulations of 2,034 IDP sequences, they assess each metric's classification accuracy, predictability from sequence features via neural network surrogates, utility in predicting condensed-phase diffusivity, and sequence determinants via SHAP analysis. The expenditure density is claimed to outperform the other metrics across most tasks.
- **Visible evidence base** Full text with equations, figure captions, and references. Figures 1-7 are described in text but not visible. Supporting Information sections are referenced but not provided.
- **Missing materials affecting confidence** Figures 1-7 (only captions visible), all Supporting Information (Figures S1-S3, Sections S4-S5), and the referenced GitHub data repositories. These are essential for verifying quantitative claims, classification accuracy values, and methodological details.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and practically important question: which simple computational metric best predicts IDP phase separation propensity. The systematic comparison across 2,034 sequences using a consistent simulation protocol is a strength, and the proposed expenditure density metric is conceptually interesting. However, the manuscript has several significant issues that must be addressed. The definition of expenditure density is incomplete, the statistical treatment of classification accuracy lacks rigor, the computational cost analysis is presented without sufficient methodological detail, and several claims about metric performance are not fully supported by the visible evidence. The work has potential but requires substantial revision before the case is established.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, intrinsically disordered proteins, and computational biophysics would be interested. The work addresses a practical need for efficient screening tools in IDP phase behavior prediction. The comparison of metrics and the proposed expenditure density could inform method selection for both simulation-based studies and machine learning approaches. The analysis of sequence determinants may also interest those developing sequence-to-property prediction models.
- **Major strengths** 1) Systematic evaluation of multiple metrics on a large, diverse dataset of 2,034 IDP sequences. 2) The proposed expenditure density metric is conceptually novel and physically motivated. 3) The multi-task evaluation (classification, surrogate modeling, diffusivity prediction, sequence determinants) provides a comprehensive assessment. 4) The analysis of metric-specific failure modes via JS divergence is a thoughtful approach. 5) The work addresses a practical need for efficient screening tools in IDP research.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (incomplete metric definition), R1-M2 (insufficient statistical rigor), R1-M3 (unverifiable computational cost claims), R1-M4 (overstated surrogate model conclusions).
- **Assessment against Nature-style criteria** **Originality:** Moderate. The expenditure density is a new metric, but the overall approach of comparing simple metrics for phase separation prediction is not entirely novel. **Scientific importance:** Moderate to high. The question of efficient phase separation prediction is important, but the impact depends on the robustness of the findings. **Interdisciplinary readership:** Moderate. The work bridges polymer physics, computational biology, and machine learning, but the presentation is quite specialized. **Technical soundness:** Currently insufficient. Several methodological details are missing or unclear, and the statistical treatment needs strengthening. **Readability for nonspecialists:** Moderate. The introduction is accessible, but the methods and results sections assume significant domain expertise. The manuscript would benefit from clearer explanations of key concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the dataset is valuable, but the current manuscript does not fully establish the case for the expenditure density as a superior metric.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript introduces the "expenditure density" as a new metric but does not provide a complete mathematical definition. Equation (7) is referenced but not shown in the visible text.
- **Evidence pointer** Section 2.3, "Metrics of Phase-Separation Propensity"
- **Concern** The definition of expenditure density is incomplete. The text states "We introduce a new metric for phase-separation propensity, which we term the 'expenditure density', or ρ*" and refers to Equation (7), but the equation itself is not visible in the provided text. Without the explicit mathematical definition, the metric cannot be evaluated, reproduced, or compared against alternatives. This is a fundamental issue that prevents assessment of the manuscript's central contribution.
- **Why it matters** The expenditure density is the primary novel contribution of this work. If its definition is not fully specified, the entire manuscript's claims about its performance cannot be verified or built upon by other researchers.
- **Resolution test** Provide the complete mathematical definition of expenditure density, including all variables, integration limits, and the physical interpretation of each term. Clarify how the intensive work allowance ŵ* is chosen and whether results are sensitive to this choice.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript reports AUC values for classification accuracy (e.g., ρ* AUC=0.994, B̃₂ AUC=0.978, R̃g AUC=0.901) and claims statistically significant differences between metrics.
- **Evidence pointer** Section 3.2, "Analysis of Phase-separation Prediction Accuracy"; Figure 2
- **Concern** The statistical treatment of classification accuracy is insufficient. The manuscript reports point estimates of AUC without confidence intervals, and the claim that differences between metrics are meaningful is not supported by any statistical test. Given the large dataset (2,034 sequences), even small AUC differences could be statistically significant, but the practical significance of a 0.016 AUC difference between ρ* and B̃₂ is unclear. Additionally, the manuscript does not report how classification thresholds were selected or whether the reported AUC values account for the class imbalance between phase-separating and non-phase-separating sequences.
- **Why it matters** The central claim of the manuscript is that ρ* outperforms B̃₂ and R̃g. Without proper statistical analysis, including confidence intervals and significance testing, this claim is not established. The practical utility of a metric depends not only on its point estimate of accuracy but also on the uncertainty around that estimate.
- **Resolution test** Report confidence intervals for all AUC values, perform formal statistical comparisons between metrics (e.g., DeLong test for correlated ROC curves), and discuss the practical significance of observed differences. Clarify the class balance in the dataset and whether any adjustments were made for imbalanced classification.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that ρ* is computationally comparable to B̃₂ and that R̃g is considerably less expensive, with resource investment "about one to two orders of magnitude less" for R̃g.
- **Evidence pointer** Section 3.4, "Additional Considerations for Metric Use"; Figure 3
- **Concern** The computational cost analysis is presented without sufficient methodological detail. The manuscript does not specify what exactly is being measured (CPU hours, wall time, number of simulations), how costs are normalized across metrics, or what hardware/software configurations were used. The claim that ρ* and B̃₂ have comparable costs is surprising given that ρ* requires simulations at multiple densities while B̃₂ requires only two-chain simulations. The manuscript also does not discuss whether the cost of computing ρ* could be reduced through adaptive sampling or other strategies.
- **Why it matters** Computational cost is a key practical consideration for metric selection. If the cost analysis is not reproducible or the claims are not well-supported, readers cannot make informed decisions about which metric to use in their own work.
- **Resolution test** Provide a detailed breakdown of computational costs for each metric, including the number and duration of simulations, the system sizes, and the hardware used. Discuss the sensitivity of cost estimates to simulation parameters and whether any optimizations were applied.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that surrogate models trained on ρ* are more data-efficient than those trained on other metrics, achieving higher accuracy with smaller training sets.
- **Evidence pointer** Section 3.3, "Analysis of Surrogate Model-based Classification and Data Efficiency"; Figure 2B
- **Concern** The data efficiency analysis is limited to a single type of surrogate model (neural networks) with a specific architecture and training procedure. The manuscript does not explore whether the observed data efficiency advantages of ρ* generalize across different model classes, hyperparameter settings, or feature representations. Additionally, the comparison against binary labels as a training target is somewhat unfair, as binary labels inherently provide less information than continuous metrics. The manuscript should also discuss potential confounding factors, such as the correlation between ρ* and other sequence features.
- **Why it matters** The claim that ρ* enables more data-efficient learning is practically important for high-throughput screening applications. However, if this advantage is specific to the particular model configuration used, the generalizability of the finding is limited.
- **Resolution test** Test data efficiency across multiple model architectures and hyperparameter settings. Compare against additional baselines, such as continuous labels derived from other physical quantities. Discuss potential mechanisms for the observed data efficiency advantage.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2, "Simulation Details"
- **Evidence pointer** Equations (1)-(3)
- **Issue** The simulation details are presented with equations that are not fully visible in the provided text. The force field description is incomplete without the explicit functional forms.
- **Required correction** Ensure all equations are fully displayed and described. If the equations are standard, provide appropriate references.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.4, "Machine Learning Details"
- **Evidence pointer** Table 1, Section S4
- **Issue** The feature engineering is described as an "augmented scaled fingerprint" but the specific scaling procedure and the rationale for feature selection are not fully explained in the main text.
- **Required correction** Provide a more detailed description of the feature scaling procedure and justify the choice of features. If the details are in the Supporting Information, ensure they are comprehensive.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 3.1, "Visualization of Sequence Characteristics"
- **Evidence pointer** Figure 1
- **Issue** The UMAP visualization is described but the figure is not visible. The interpretation of the embedding is somewhat subjective without seeing the actual plot.
- **Required correction** Ensure the figure clearly shows the separation between phase-separating and non-phase-separating sequences and that the color scale for B̃₂ is legible.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.7, "Assessment of Metric Consistency with Observed Phase Behavior Outcomes"
- **Evidence pointer** Figures 6-7
- **Issue** The JS divergence analysis is interesting but the interpretation of the results is somewhat brief. The manuscript could benefit from a more detailed discussion of what the JS divergence values mean in practical terms.
- **Required correction** Expand the discussion of the JS divergence results, including what magnitude of JS divergence is considered meaningful and how this analysis informs metric selection.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 4, "Conclusions"
- **Evidence pointer** None
- **Issue** The conclusions section is somewhat repetitive of the results and could be more forward-looking. The discussion of limitations is brief.
- **Required correction** Strengthen the discussion of limitations and future directions. Consider adding a paragraph on the practical implications of the findings for the IDP phase separation community.

## Risk / unsupported claims
- The claim that ρ* "combines simplicity, low computational cost, and accuracy" is not fully supported without the complete metric definition and a more rigorous cost analysis.
- The claim that ρ* is "broadly useful" across different sequence types is based on the dataset analyzed, but the manuscript does not discuss potential limitations for sequences outside the training distribution.
- The statement that ρ* "shows promise in its ability to improve predictions of other properties" is based on a single test case (condensed-phase diffusivity) and should be framed more cautiously.
- The claim that the observed performance hierarchy reflects "the intrinsic capacity of each metric to capture multiscale interactions" is a plausible hypothesis but is not directly tested.
- The manuscript's statement that "neither this value nor the other constants in V₀ have any practical consequence for the performance of this metric" is not fully justified, as the choice of normalization could affect the metric's discriminative power.