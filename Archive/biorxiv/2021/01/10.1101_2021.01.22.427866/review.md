## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, appendices) as provided
- **Assessment boundary** Scientific and technical evaluation of the claims, methods, and evidence as presented; no assessment of code functionality or reproducibility beyond what is described
- **Shared manuscript claim summary** The authors present D-SCRIPT, a deep learning method that predicts physical protein-protein interactions from amino acid sequences alone, using a structure-aware intermediate representation (predicted inter-protein contact map) to improve cross-species generalization and interpretability. They claim superior cross-species performance compared to existing sequence-based methods, competitive intra-species performance when combined with PIPR, and that the intermediate contact maps partially recapitulate true docking contacts despite no structural supervision.
- **Visible evidence base** Abstract; Introduction; Methods (Sections 2.1, 2.2); Results sections on cross-species prediction, human cross-validation, functional module prediction, SARS-CoV-2 predictions, and contact map evaluation; Appendices A.1–A.6; Tables 1 and A.1; Figures 1–6 and A.2–A.3
- **Missing materials affecting confidence** Full training details (hyperparameter search, early stopping criteria, data splits beyond description); exact definitions of evaluation metrics and statistical significance tests; code or model weights for independent verification; details on the Bepler & Berger embedding dimensionality and frozen vs. fine-tuned status; complete results for all species in Table 1 (only partially visible); details on the hybrid method's threshold selection; full details of the functional module prediction pipeline (e.g., clustering parameters, number of clusters)

## Reviewer

- **Overall assessment** This manuscript presents a timely and potentially valuable contribution to the field of protein-protein interaction prediction. The core idea, using a structurally-motivated intermediate representation (contact map) within a sequence-based deep learning model, is conceptually appealing and addresses a real limitation of existing methods, namely poor cross-species generalization. The authors provide a reasonable set of experiments demonstrating that D-SCRIPT outperforms a state-of-the-art baseline (PIPR) in cross-species settings and that its intermediate representations carry structural signal. However, several technical and evidential gaps prevent full confidence in the claims as stated. The lack of detailed statistical comparisons, the somewhat ad hoc hybrid method, and the limited evaluation of the contact map quality (only median EMD p-values reported) are notable weaknesses. The functional module prediction analysis is interesting but would benefit from a more rigorous comparison to alternative approaches. Overall, the work is promising and likely of interest to the computational biology community, but the evidence presented does not fully establish all claims, particularly regarding the physical interpretability of the contact maps and the generalizability of the method beyond the specific evaluation settings.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, interactomics, and deep learning applications in biology. The method's focus on cross-species generalization is directly relevant to researchers studying non-model organisms or species with sparse interaction data. The interpretability aspect (contact map output) may also appeal to structural biologists interested in using sequence-based predictions to generate hypotheses about binding interfaces. The work is likely to be cited and built upon by groups developing sequence-based PPI prediction tools.
- **Major strengths** (1) The core architectural idea is novel and well-motivated: explicitly modeling the inter-protein contact map as an intermediate step is a sensible way to inject structural priors into a sequence-based model. (2) The cross-species evaluation is a relevant and practically important benchmark, and the reported improvements over PIPR are substantial. (3) The analysis of the intermediate contact maps against docking benchmarks is a commendable attempt to validate interpretability, even if the results are preliminary. (4) The manuscript is generally well-written and the figures are clear.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that D-SCRIPT "significantly outperforms" PIPR in cross-species prediction is based on a single table of metrics without reported confidence intervals or statistical tests.
- **Evidence pointer** Table 1, Section 3
- **Concern** The performance comparison between D-SCRIPT and PIPR in Table 1 reports point estimates for precision, recall, AUPR, and AUROC. No error bars, confidence intervals, or statistical significance tests (e.g., bootstrap, McNemar's test) are provided. Given the stochastic nature of deep learning training and the potential for variance across random seeds, it is unclear whether the observed differences are robust. This is particularly important for species where the performance gap appears modest (e.g., E. coli).
- **Why it matters** Without measures of uncertainty, the reader cannot assess whether the claimed improvements are meaningful or within the noise of the experimental setup. This is a fundamental requirement for establishing the reliability of a new method.
- **Resolution test** Provide confidence intervals (e.g., via bootstrapping over the test set) or perform repeated training runs with different seeds and report mean and standard deviation for each metric. Apply appropriate statistical tests (e.g., paired bootstrap or McNemar's test) to compare D-SCRIPT and PIPR for each species.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The claim that the intermediate contact map "partially discovers the structural mechanism of an interaction" is supported only by a median EMD p-value of 0.08 across 295 candidate pairs.
- **Evidence pointer** Section 3, Figure 6
- **Concern** The evaluation of the predicted contact maps against ground-truth docking structures is a key part of the interpretability claim. However, the reported result is a single median p-value across all candidate pairs, which is difficult to interpret. It is unclear how many of the 295 pairs had significant overlap, what the distribution of p-values was, and whether the significance is driven by a subset of easy cases. Furthermore, the choice of EMD as a metric, while reasonable, is not standard in the field, and its interpretation in terms of biological relevance is not discussed.
- **Why it matters** The interpretability claim is a major differentiator of this work. If the contact maps are not reliably informative, the added architectural complexity may not be justified. A more detailed and rigorous evaluation is needed to support this claim.
- **Resolution test** Report the full distribution of EMD p-values (e.g., histogram or cumulative distribution), the fraction of pairs with p < 0.05, and a comparison to a baseline (e.g., random contact maps or a simpler model). Consider using additional metrics such as precision-recall for contact prediction at various distance thresholds.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The claim that D-SCRIPT's improved cross-species generalization "translates to better functional inference" is based on a single analysis in Drosophila with a modest p-value (0.000723) and no comparison to alternative methods.
- **Evidence pointer** Section 3, Figure 3
- **Concern** The functional module prediction analysis is a nice addition, but it is limited in scope. Only one species (Drosophila) is tested, and the comparison is only against PIPR. It is unclear whether the observed improvement in cluster coherence is specific to the D-SCRIPT architecture or could be achieved by other means (e.g., better clustering algorithms, different thresholds). The p-value is reported without correction for multiple testing (though only one test is performed, so this is less of an issue).
- **Why it matters** The claim that better PPI prediction leads to better functional inference is important for the broader impact of the work. A more comprehensive evaluation would strengthen this claim.
- **Resolution test** Extend the analysis to additional species with available functional annotation data. Compare against a baseline using a simple sequence-similarity-based PPI prediction or a network-based method. Report the number of clusters and the robustness of the results to clustering parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The hybrid method (PIPR + D-SCRIPT) is described as performing "best of all" in human cross-validation, but the details of how the hybrid is constructed are vague.
- **Evidence pointer** Section 3, Table 1
- **Concern** The hybrid method is described as "when PIPR is highly confident that an interaction does occur, the predicted probability of D-SCRIPT is increased by 50%." This is a very specific and seemingly arbitrary rule. It is unclear how the threshold for "highly confident" was chosen, whether this was tuned on the test set (which would be a form of data leakage), and how sensitive the results are to this choice. The same applies to the reverse hybrid (D-SCRIPT adjusting PIPR) used in the human cross-validation.
- **Why it matters** If the hybrid rule was tuned on the evaluation data, the reported performance is optimistic and not representative of real-world use. The lack of detail makes it difficult to reproduce or assess the validity of the hybrid approach.
- **Resolution test** Clearly describe how the hybrid rule was developed, including any threshold selection procedure. If thresholds were tuned, use a nested cross-validation scheme to avoid data leakage. Report performance as a function of the threshold to show robustness.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The claim that D-SCRIPT is "robust to limitations in training data size" is not directly tested in the main text.
- **Evidence pointer** Section 3, Table 1
- **Concern** The abstract and introduction emphasize robustness to limited training data, but the experiments do not explicitly vary the training set size. The cross-species evaluation (training on human, testing on other species) is a form of transfer learning, but it does not directly address the question of how performance degrades as the amount of human training data is reduced.
- **Why it matters** The stated motivation for the method is to address data sparsity. A direct test of this claim would strengthen the paper.
- **Resolution test** Train D-SCRIPT and PIPR on subsets of the human training data (e.g., 10%, 25%, 50%, 100%) and evaluate on a held-out human test set and on cross-species benchmarks. Plot performance as a function of training set size.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Methods Section 2.1
- **Evidence pointer** Section 2.1
- **Issue** The description of the model architecture is dense and uses notation that may be challenging for readers not deeply familiar with deep learning terminology. For example, the equations for the broadcast matrix and the global pooling operation are presented without much intuitive explanation.
- **Required correction** Add a brief intuitive explanation of each major component (e.g., "the broadcast matrix captures pairwise interactions between residues," "the global pooling operation selects the most confident contact regions"). Consider adding a schematic figure of the full architecture.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2
- **Issue** The hyperparameter λ balancing the BCE and magnitude losses is set to 0.35, but there is no sensitivity analysis or justification for this choice.
- **Required correction** Provide a brief sensitivity analysis (e.g., performance for λ = 0.1, 0.5, 0.9) or cite prior work justifying the choice.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 3, SARS-CoV-2 analysis
- **Evidence pointer** Section 3, Appendix A.6
- **Issue** The SARS-CoV-2 analysis is presented as preliminary, which is appropriate, but the comparison to PIPR is only summarized with a p-value of 0.059. It would be helpful to see the actual overlap values or a figure showing the Jaccard similarities for each viral protein.
- **Required correction** Include a supplementary figure showing the per-protein Jaccard similarities for D-SCRIPT and PIPR, as in Figure A.3, and briefly discuss which viral proteins show the largest differences.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 3, "Prediction of Intra-Protein Self Contacts"
- **Evidence pointer** Section 3, Figure 5
- **Concern** The analysis of intra-protein self contacts uses a logistic regression on the embeddings to predict contacts. It is unclear how this relates to the D-SCRIPT model's own contact map output, which is for inter-protein contacts. The connection between the two analyses could be clarified.
- **Required correction** Briefly explain how the intra-protein analysis informs the claim that the embeddings capture structural information, and how this relates to the inter-protein contact map output.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Introduction, Related Work
- **Evidence pointer** Section 1
- **Issue** The related work section is brief and does not discuss recent advances in protein language models (e.g., ESM, ProtTrans) that are highly relevant to the approach.
- **Required correction** Add a brief discussion of how D-SCRIPT relates to and differs from recent protein language model-based approaches for PPI prediction.

- **Technical failings that need to be addressed before the case is established** (1) Lack of statistical significance testing for the main performance comparisons (R1-M1). (2) Insufficient detail on the hybrid method's construction and potential for data leakage (R1-M4). (3) The contact map evaluation is reported as a single median p-value without distribution or fraction of significant cases (R1-M2). (4) The claim of robustness to limited training data is not directly tested (R1-M5).
- **Assessment against Nature-style criteria** 
  - **Originality** The idea of using an explicit inter-protein contact map as an intermediate representation in a sequence-based PPI predictor is a novel contribution. While contact map prediction for single proteins is well-studied, applying this concept to the PPI prediction task in a way that is both interpretable and improves cross-species generalization is a fresh angle. The use of a pre-trained protein language model for embeddings is not new, but the specific architectural combination is.
  - **Scientific importance** The problem of PPI prediction, particularly for species with sparse data, is of significant importance in biology. The potential for improved cross-species generalization and the interpretability of the model are both valuable features. However, the importance is somewhat tempered by the fact that the improvements are demonstrated against a single baseline (PIPR) and the absolute performance numbers are not contextualized against the broader literature.
  - **Interdisciplinary readership** The work is likely to appeal to a broad audience of computational biologists, bioinformaticians, and potentially structural biologists. The writing is generally accessible, but the methods section is dense and may be challenging for non-specialists. The biological motivation is clearly stated.
  - **Technical soundness** The core methodology appears sound, but the lack of statistical rigor in the performance comparisons and the incomplete evaluation of the contact map quality are significant weaknesses. The hybrid method's construction is under-specified. These issues need to be addressed to fully establish the technical claims.
  - **Readability for nonspecialists** The abstract and introduction are clear and accessible. The results sections are reasonably readable. The methods section is the most challenging part and would benefit from additional intuitive explanations.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the initial results are encouraging, but the lack of statistical rigor and incomplete evaluation of key claims prevent full endorsement at this stage. The authors should address the major concerns, particularly around significance testing, the hybrid method, and the contact map evaluation, before the case is fully established.

## Risk / unsupported claims
- The claim that D-SCRIPT "significantly outperforms" PIPR in cross-species prediction is not supported by statistical tests (only point estimates in Table 1).
- The claim that the contact map output "partially discovers the structural mechanism" is weakly supported by a single median p-value; the fraction of significant cases is not reported.
- The claim that D-SCRIPT is "robust to limitations in training data size" is not directly tested.
- The performance of the hybrid method may be optimistically biased if thresholds were tuned on the test set; this is not described.
- The claim that D-SCRIPT's embeddings capture structural information is supported by the intra-protein contact analysis, but the connection to the inter-protein contact map output is not fully established.
- The comparison to the Richoux et al. method (Appendix A.3) is presented without statistical significance testing.
- The functional module prediction analysis is limited to one species and one comparison method; the generalizability of this finding is unclear.