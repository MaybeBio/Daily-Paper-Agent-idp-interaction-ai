## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, availability, data availability)
- **Assessment boundary** Scientific and technical evaluation of the presented method, experimental design, validation approach, and claims; no assessment of editorial fit or publication decision
- **Shared manuscript claim summary** The authors present DNAreader, a transformer encoder-based predictor of DNA-binding residues (DBRs) in both structured and disordered protein regions, trained with a combination of batch training and multi-center contrastive learning. The method is claimed to be the first to predict DBRs in both structured and disordered regions, to outperform existing tools by statistically significant margins on two low-similarity test datasets, and to substantially reduce cross-predictions (incorrectly labeling residues that bind non-DNA ligands as DBRs). A secondary module, DNAreaderDBIDR, is provided to predict DNA-binding IDRs.
- **Visible evidence base** Full text of the manuscript including methods, results, and discussion sections; references to Supplementary Tables S1–S8 and Supplementary Figures S1–S7; two case study proteins with visualizations described in Figure 3
- **Missing materials affecting confidence** Supplementary tables and figures referenced throughout the text were not provided; Figure 1 (workflow diagram), Figure 2 (comparative results), and Figure 3 (case study visualizations) were not available; exact numerical results for all metrics are only partially reported in the text; the loss function equations are present but the specific mathematical formulations are not fully legible in the provided text

## Reviewer
- **Overall assessment** The manuscript addresses a genuine and well-motivated gap in the field: existing predictors of DNA-binding residues are trained on either structured or disordered proteins, and the two annotation types are inconsistent. The authors propose a unified predictor that handles both, which is a meaningful contribution. The technical approach, combining a transformer encoder with batch training and contrastive learning, is reasonable and the ablation study is appropriately designed to isolate the contributions of each innovation. The comparative evaluation against 14 methods on two low-similarity test sets is thorough in scope. However, the manuscript as provided has several limitations that prevent full assessment: the supplementary materials containing the detailed results are not available, the exact numerical values for many reported metrics are not stated in the text, and the case studies, while illustrative, are qualitative. The claim of being the "first" predictor for both structured and disordered DBRs is strong and would benefit from a more explicit demonstration that no prior method has attempted this. The cross-prediction analysis is a particular strength, as this is a known weakness of existing tools and is often not systematically evaluated. Overall, the work appears technically sound and potentially impactful, but the evidence base as provided is incomplete for a full evaluation.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein function prediction, particularly those focused on DNA-binding proteins and protein–nucleic acid interactions. Researchers developing deep learning methods for biological sequence analysis would be interested in the application of contrastive learning and batch training to a residue-level prediction problem. Experimental biologists studying protein–DNA interactions, gene regulation, and chromatin biology may find the web server useful for generating hypotheses about uncharacterized proteins. The method's ability to handle both structured and disordered regions is relevant to the intrinsically disordered protein community, as disordered regions are increasingly recognized as important in DNA binding.

- **Major strengths**
  1. The problem is well-motivated and addresses a real gap: no existing predictor handles both structured and disordered DBRs with consistent annotation types.
  2. The technical approach is innovative, combining a transformer encoder with batch training and contrastive learning, with a clear rationale for each component.
  3. The ablation study is well-designed, isolating the contributions of batch training and contrastive learning, and comparing against a convolutional baseline.
  4. The evaluation is comprehensive, including 14 comparators, two test sets with different annotation schemes, and multiple metrics including cross-prediction and over-prediction rates.
  5. The cross-prediction analysis is a notable strength, as this issue is often ignored in the field.
  6. The authors provide a web server and source code, which enhances usability and reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that DNAreader "statistically outperforms existing tools" on both test datasets, with specific numerical values cited (e.g., AUROC of 0.86 on test set 1, 0.88 on test set 2).
- **Evidence pointer** Results section, "Comparative assessment on test dataset 1" and "Comparative assessment on the test dataset 2"; Supplementary Tables S6, S7, S8
- **Concern** The detailed numerical results for all 14 comparators across all metrics are only available in the supplementary tables, which were not provided for this review. The text reports only a subset of values (e.g., AUROC for the best comparators and for DNAreader), and the full comparison tables are essential to verify the claimed statistical significance of the improvements.
- **Why it matters** The central claim of the manuscript is that DNAreader outperforms existing tools. Without access to the full results tables, this claim cannot be independently verified. The statistical testing methodology (t-test on 100 subsampled evaluations) is described, but the actual distributions and effect sizes are not visible.
- **Resolution test** Provide the supplementary tables with full results for all methods on both test sets, including all metrics (AUROC, AULCratio, F1, AUCPC, AUOPC, CPRratio, OPRratio) and the P-values for pairwise comparisons between DNAreader and each comparator.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the transformer encoder "significantly outperforms" a convolutional architecture with the same input features and training strategy, based on results in Supplementary Figure S2.
- **Evidence pointer** Methods, "Step 2: Design and training of the transformer encoder-based network"; Supplementary Figure S2
- **Concern** The comparison between transformer and convolutional architectures is described only in a supplementary figure, with no numerical values reported in the text. The claim of significant improvement is made without presenting the actual metrics or the statistical test used for this specific comparison. Additionally, the hyperparameter tuning for the convolutional baseline is not described, raising the question of whether the comparison is fair.
- **Why it matters** The choice of transformer over convolutional architecture is a key design decision. If the comparison is not rigorously conducted, the justification for the more complex transformer model is weakened.
- **Resolution test** Report the numerical results of the transformer vs. convolutional comparison in the main text or provide the supplementary figure with clear annotations. Describe the hyperparameter search for both architectures and the statistical test used to establish significance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim substantiation
- **Claim pointer** The authors claim DNAreader is "the first predictor specifically designed to predict DBRs in the structured and disordered sequence regions."
- **Evidence pointer** Abstract; Introduction; Summary and discussion
- **Concern** The claim of being "first" is stated without a systematic demonstration. While the authors note that existing tools target either structured or disordered proteins, they do not provide a comprehensive literature search or a table showing that no prior method has attempted unified prediction. The HybridDBRpred meta-predictor, which they themselves published, combines outputs from both types of tools, which is related but not identical.
- **Why it matters** The novelty claim is a key part of the manuscript's contribution. If a prior method has attempted unified DBR prediction, the novelty is diminished. The claim should be substantiated with evidence.
- **Resolution test** Provide a systematic search strategy and results (e.g., PubMed queries, inclusion/exclusion criteria) demonstrating that no prior predictor has been designed to predict DBRs in both structured and disordered regions with a single model.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that the batch training approach "ensures that each batch adequately covers all six residue types" and that this "substantially boosts predictive performance."
- **Evidence pointer** Methods, "Step 2: Design and training of the transformer encoder-based network"; Results, "Ablation analysis"
- **Concern** The description of the batch training strategy is somewhat vague. The authors state that batches of 500 residues are sampled with proportions of non-binding and other-ligand-binding residues reflecting their native frequencies, and that DBR proportions are tuned via grid search (1–5%, selecting 4%). However, it is not clear how the grid search was conducted, what the objective function was, or whether the selected 4% proportion is optimal across both structured and disordered DBRs. The ablation results show that removing batch training reduces performance, but the mechanism by which batch training helps is not fully explained.
- **Why it matters** The batch training strategy is presented as a key innovation. A clearer description of the implementation and the rationale for the specific design choices would strengthen the manuscript.
- **Resolution test** Provide a more detailed description of the batch construction algorithm, including pseudocode or a formal algorithm box. Clarify the grid search procedure and report the performance across different DBR proportions in the batch.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that the contrastive learning approach with six anchors "minimizes cross-predictions" and that increasing from three to six anchors leads to "large and statistically significant improvements."
- **Evidence pointer** Methods, "Step 2: Design and training of the transformer encoder-based network"; Results, "Ablation analysis"; Supplementary Figure S1
- **Concern** The description of the contrastive learning approach is incomplete. The loss function equations are presented but not fully legible in the provided text. The choice of six anchors is justified empirically, but the rationale for the specific anchor definitions (structured DBR, disordered DBR, structured other-ligand, disordered other-ligand, structured non-binding, disordered non-binding) is not discussed in depth. The results in Supplementary Figure S1 are not visible.
- **Why it matters** Contrastive learning is a central innovation of the manuscript. A clear and complete description of the loss function and the anchor design is essential for reproducibility and for understanding why the method works.
- **Resolution test** Provide a complete and legible formulation of the loss function. Discuss the rationale for the six-anchor design and why this specific categorization of residue types is appropriate. Report the numerical results of the anchor comparison in the main text or in a clearly readable supplementary figure.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Step 1: Generation of the sequence profile"
- **Evidence pointer** Methods section, Step 1
- **Issue** The description of the sequence-derived features is a list without clear justification for why each feature was selected. The authors state that features include "relative amino acid propensity for protein–DNA binding, relative solvent accessibility, relevant physicochemical properties of amino acids, evolutionary conservation and couplings, and putative intrinsic disorder," but do not explain how these features complement the ESM-2 embeddings.
- **Required correction** Add a brief justification for the choice of each feature type and explain how they complement the ESM-2 embeddings. Consider citing prior work that used similar features for DBR prediction.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Step 2: Design and training of the transformer encoder-based network"
- **Evidence pointer** Methods section, Step 2
- **Issue** The hyperparameter values for the transformer encoder (e.g., number of layers, number of attention heads, hidden dimension, learning rate, dropout rate) are not reported in the text. The authors mention that the network consists of "three stacked transformer encoder units" and a "four-layer FCNN," but other critical hyperparameters are missing.
- **Required correction** Provide a table or a detailed paragraph listing all hyperparameters used for the transformer encoder, the FCNN, and the training procedure (optimizer settings, learning rate schedule, number of epochs, early stopping criteria).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Methods, "Assessment metrics and statistical analysis"
- **Evidence pointer** Methods section, "Assessment metrics and statistical analysis"
- **Issue** The authors state that they used the Anderson–Darling test at a 0.01 significance level to assess normality, and then used either Student's t-test or the Wilcoxon rank-sum test. However, they do not report the results of the normality tests or specify which test was used for which comparison.
- **Required correction** Report the normality test results or state that the choice of test was made per comparison based on the Anderson–Darling test outcome. Consider using a more robust approach, such as bootstrap confidence intervals, for all comparisons.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Case studies"
- **Evidence pointer** Results section, "Case studies"
- **Concern** The case studies are described qualitatively, with statements like "DNAreader produces high scores for the DBRs across both structured and disordered DNA-binding regions" and "hybridDBRpred2 predicts 30 residues with scores above its threshold." However, the actual scores and thresholds are not reported numerically, and the figures are not available.
- **Required correction** Report the numerical scores and thresholds for the case study proteins, or at least provide the figures with clear annotations. Consider adding a quantitative summary of the case study results (e.g., precision, recall, F1 for each method on each protein).

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Comparative assessment on test dataset 1"
- **Evidence pointer** Results section, "Comparative assessment on test dataset 1"
- **Issue** The authors report that DNAreaderDBIDR "secures similar results to DNAreader on the structure-annotated proteins while generating significantly more accurate results for the disorder-annotated proteins." However, the specific numerical values for DNAreaderDBIDR are not reported in the text, only in the supplementary tables.
- **Required correction** Report the key numerical results for DNAreaderDBIDR in the main text, at least for the primary metrics (AUROC, AULCratio) on the full test set and the disorder-annotated subset.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Availability section
- **Evidence pointer** Availability section
- **Issue** The web server URL and GitHub repository are provided, but there is no description of the expected runtime for a typical protein sequence, nor any information about the computational resources required to run the method locally.
- **Required correction** Add a brief statement about the expected runtime and hardware requirements for running DNAreader locally, and note any usage limits or queue times for the web server.

## Risk / unsupported claims
- The claim that DNAreader is the "first predictor specifically designed to predict DBRs in the structured and disordered sequence regions" is not substantiated with a systematic literature search.
- The claim that DNAreader "statistically outperforms existing tools" cannot be fully verified without access to the supplementary tables containing the complete comparative results.
- The claim that the transformer architecture "significantly outperforms" the convolutional baseline is not verifiable from the text alone, as the results are only in a supplementary figure.
- The specific numerical improvements attributed to batch training and contrastive learning in the ablation study are not fully reported in the text.
- The case study results are described qualitatively, and the quantitative scores and thresholds are not reported in the text.
- The loss function equations for the multi-center contrastive learning are not fully legible in the provided text, preventing assessment of the technical implementation.