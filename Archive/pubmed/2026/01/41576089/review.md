## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends not provided)
- **Assessment boundary** Scientific claims, methodology, and evidence as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors present two protein language models (SeqDance and ESMDance) pretrained on biophysical dynamics data derived from molecular dynamics simulations and normal mode analysis. They claim these models capture dynamic interactions and residue comovement through attention mechanisms, encode global conformational properties, and can predict mutation effects on protein stability, particularly for proteins lacking evolutionary homologs such as designed and viral proteins.
- **Visible evidence base** Main text descriptions of results, methods section, figure references (Figs. 1-5), supplementary figure/table references (SI Appendix Figs. S1-S8, Tables S1-S3)
- **Missing materials affecting confidence** Figure panels and actual data values, supplementary information details, exact dataset compositions, hyperparameter configurations, baseline implementation details, statistical significance tests, and code verification

## Reviewer

- **Overall assessment** This manuscript presents a timely and potentially valuable contribution to the protein language model field by incorporating biophysical dynamics into pretraining objectives. The core idea of learning from dynamic properties rather than static sequences or structures is conceptually appealing and addresses a recognized limitation of current models. However, the evidence presented in the text raises several concerns about the strength of the claims, particularly regarding the comparative performance against established methods, the generalizability of the findings, and the practical utility of the proposed approach. The manuscript would benefit from clearer benchmarking, more rigorous statistical analysis, and a more balanced discussion of limitations.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, mutation effect prediction, and protein language models would find this work relevant. Researchers in protein engineering and design, particularly those working with designed or viral proteins where evolutionary information is limited, may find the approach useful. The broader structural biology community interested in integrating dynamics into machine learning frameworks would also be interested.

- **Major strengths** The conceptual framing of learning from biophysical dynamics is novel and addresses a real gap in current protein language models. The use of multiple data sources (MD simulations, NMA, experimental data) to create a diverse training set is thoughtful. The zero-shot evaluation framework for mutation effects is appropriate and allows comparison with existing methods. The analysis of attention mechanisms in relation to dynamic interactions provides mechanistic insight into what the model learns. The inclusion of designed and viral proteins as test cases addresses an important practical limitation of evolution-based methods.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "ESMDance achieves a median Spearman correlation of 0.46 across 412 proteins, significantly outperforming both ESM2-35M (0.33) and SeqDance (0.24)"
- **Evidence pointer** Figure 4F, location not provided
- **Concern** The claim of significant outperformance is not supported by any statistical testing. The manuscript reports median correlations but does not provide confidence intervals, paired statistical tests, or effect sizes. Given that the comparison is across the same 412 proteins, a paired analysis would be appropriate. Additionally, the variance across proteins is not reported, making it impossible to assess whether the observed differences are robust or driven by a subset of proteins.
- **Why it matters** The central claim of the manuscript is that ESMDance improves mutation effect prediction. Without statistical validation, the observed differences could be within noise, particularly given the modest absolute improvement (0.46 vs 0.33).
- **Resolution test** Provide per-protein correlation values with appropriate paired statistical tests (e.g., Wilcoxon signed-rank test), confidence intervals for median differences, and effect size measures. Report the distribution of per-protein correlations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "SeqDance and ESMDance can be directly applied to predict residue-level and pairwise dynamic properties for proteins dissimilar to those in the training set"
- **Evidence pointer** Figure 1D-G, location not provided
- **Concern** The evaluation of generalization to unseen proteins is confounded by potential data leakage. The authors state that test proteins share less than 50% sequence identity with training sequences, but this threshold may be insufficient to prevent homologs from influencing results. More critically, the NMA data covers "nearly all representative PDB structures," which means the test set for ordered proteins likely overlaps substantially with training data. The claim of generalization to dissimilar proteins is therefore not convincingly established.
- **Why it matters** The practical utility of the models depends on their ability to generalize to novel proteins. If the evaluation is confounded by training set overlap, the reported performance may not reflect real-world applicability.
- **Resolution test** Provide a clearer analysis of sequence similarity between test and training sets, including a similarity distribution. Consider evaluating on a truly held-out set of proteins with no detectable homologs in training data. Report performance stratified by sequence similarity to training set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** "Our results show that our pretraining strategy enables the transformer's attentions to effectively capture pairwise dynamic properties, using only 1/1,000th of the training sequences compared to ESM2"
- **Evidence pointer** Figure 2, location not provided
- **Concern** The comparison of attention mechanisms between SeqDance and ESM2-35M is described as "comparable," but the significance of this finding is unclear. The authors do not establish a clear baseline for what constitutes meaningful attention-based capture of dynamic properties. Moreover, the claim about using 1/1,000th of training sequences is misleading without context: ESM2 was trained on vastly more data for different objectives, and the comparison does not account for the additional computational cost of generating MD simulation data for pretraining.
- **Why it matters** The efficiency claim is presented as a key advantage, but the comparison is not apples-to-apples. The practical value of the approach depends on whether the reduced sequence data requirement offsets the substantial cost of generating dynamics data.
- **Resolution test** Provide a more nuanced comparison that accounts for total data acquisition and computational costs. Clarify what specific advantage the 1/1,000th claim represents in practical terms. Consider comparing against a model trained on the same number of sequences without dynamics objectives.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "SeqDance outperforms STARLING when generating 20 conformations but underperforms STARLING when generating 200 conformations"
- **Evidence pointer** Figure 3E-G, location not provided
- **Concern** The comparison with STARLING is presented without sufficient detail on evaluation protocol. STARLING generates an ensemble of conformations, and the number of generated conformations (20 vs 200) affects the quality of derived properties. The authors do not clarify whether the comparison is fair in terms of computational cost or whether the same downstream analysis was applied. Additionally, the claim that SeqDance is "orders of magnitude faster" is not quantified.
- **Why it matters** The practical advantage of SeqDance over generative models depends on the trade-off between speed and accuracy. The current presentation does not allow readers to assess this trade-off.
- **Resolution test** Provide runtime comparisons on the same hardware. Clarify the evaluation protocol for STARLING, including how many independent runs were performed and how variability was handled. Report the computational cost of generating 200 conformations with STARLING versus a single SeqDance forward pass.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "ESMDance demonstrates robust generalization: its performance is independent of the presence of homologs in its training set or in UniRef50"
- **Evidence pointer** Figure 4F-G, location not provided
- **Concern** The claim of robust generalization is based on a single dataset (Tsuboyama2023) and a specific evaluation protocol. The authors do not test on independent mutation effect datasets, such as deep mutational scanning data beyond ProteinGYM, or on other biophysical properties. The robustness claim is therefore overstated relative to the evidence.
- **Why it matters** The generalizability of the approach to diverse mutation effect prediction tasks is central to its utility. A single dataset, however large, does not establish robust generalization.
- **Resolution test** Evaluate on additional independent mutation effect datasets (e.g., ProTherm, deep mutational scanning databases). Report performance consistency across datasets and protein types.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and significance statement
- **Evidence pointer** Significance section, location not provided
- **Issue** The significance statement assumes familiarity with protein language models and dynamics terminology without sufficient context for a general scientific audience.
- **Required correction** Briefly define key terms (e.g., "normal mode analysis," "coarse-grained MD") and provide one or two sentences of background on why dynamics are important for protein function.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, model architecture
- **Evidence pointer** Methods section, location not provided
- **Issue** The description of the pairwise embedding computation (Eq. 1-2) is mathematically unclear. The notation for element-wise multiplication and the exact dimensions of intermediate tensors are not specified.
- **Required correction** Provide explicit tensor dimensions and clarify the mathematical operations. Consider including a diagram or pseudocode for the architecture.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, loss function weighting
- **Evidence pointer** Methods section, "Adjusting Weights of Dynamic Properties" subsection, location not provided
- **Issue** The description of how task-specific weights are calculated from standard deviations is vague. The exact formula for weight calculation is not provided.
- **Required correction** Provide the explicit formula for weight calculation and describe how the pairwise-to-residue loss ratio of 3:1 was determined.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of limitations
- **Evidence pointer** Discussion section, location not provided
- **Issue** The discussion does not adequately address the limitation that the models were only evaluated on proteins shorter than 1,024 residues, which excludes many biologically important proteins.
- **Required correction** Add a paragraph discussing the implications of this length limitation and potential strategies for extending the approach to longer proteins.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Evaluation of conformational properties
- **Evidence pointer** Figure 3, location not provided
- **Issue** The comparison with ESMFold for ordered proteins is described as "comparable," but the metric used (MAE) may not be the most appropriate for evaluating predicted radius of gyration, which has a strong length dependence.
- **Required correction** Report additional metrics (e.g., Pearson correlation, normalized error) and consider stratifying results by protein length.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure legends
- **Evidence pointer** Figures 1-5, location not provided
- **Issue** Figure legends are not provided in the manuscript text, making it difficult to interpret the results described in the main text.
- **Required correction** Ensure figure legends are self-contained and clearly describe the statistical tests, error bars, and sample sizes.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Data availability
- **Evidence pointer** Data, Materials, and Software Availability section, location not provided
- **Issue** The extracted dynamic properties dataset is approximately 100 GB, which may be impractical for many researchers to download and use.
- **Required correction** Consider providing a reduced version of the dataset or a data loader that streams data on demand.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Comparison with existing methods
- **Evidence pointer** Figure 5H, location not provided
- **Issue** The comparison with ProteinMPNN, Rosetta, and FoldX is limited to a single dataset and does not include more recent deep learning-based mutation effect predictors.
- **Required correction** Consider benchmarking against additional state-of-the-art methods (e.g., ESM variants, MSA-based methods) to provide a more comprehensive comparison.

## Risk / unsupported claims
- The claim that SeqDance and ESMDance "can be directly applied to predict residue-level and pairwise dynamic properties for proteins dissimilar to those in the training set" is not fully supported due to potential training set overlap, particularly for NMA data covering nearly all PDB structures.
- The claim of "robust generalization" for ESMDance is based on a single dataset and is therefore overstated.
- The efficiency claim of using "1/1,000th of the training sequences compared to ESM2" is presented without accounting for the computational cost of generating MD simulation data.
- The claim that attention mechanisms "capture dynamic interactions and comovement" is based on correlational analysis without establishing causality or demonstrating that this is unique to the proposed pretraining approach.
- The statement that "our models provide additional information to evolution-based models" is supported by the combination results, but the mechanism by which this additional information is provided is not clearly explained.
- The claim that linear regression models "can serve as an alternative to traditional biophysics-based models" is based on a single dataset and limited comparison, and the practical advantages in terms of speed are not quantified.
- The manuscript does not report performance on proteins longer than 1,024 residues, limiting the generalizability of the claims to the full protein universe.