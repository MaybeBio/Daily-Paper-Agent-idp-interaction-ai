## Review setup

- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and significance of the reported findings
- **Shared manuscript claim summary** The authors present FrustrAI-Seq, a protein language model-based method for predicting local energetic frustration directly from protein sequences, trained on a new dataset of approximately 1 million proteins with precomputed frustration values. They report proteome-wide scalability, biological relevance across multiple use cases, and release the largest freely available precomputed frustration resource.
- **Visible evidence base** Results sections 2.1 through 2.9, including performance metrics on a held-out test set, ablation studies, comparisons to baselines and FrustraMPNN, use-case analyses on alpha-globin and beta-lactamase families, disorder coupling analysis, and proteome-scale inference
- **Missing materials affecting confidence** Supplementary figures and tables referenced throughout (Supplementary Figs. 1-11, Supplementary Tables 1-5) were not provided. The FrustratometeR software and its exact version/parameters are referenced but not described in sufficient detail. The FrustraMPNN evaluation protocol is described but the checkpoint details are incomplete. Code and model weights are promised via external repositories but were not inspected.

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important problem: making local energetic frustration analysis scalable to sequence space. The core idea, fine-tuning a protein language model on precomputed frustration values, is conceptually sound and the reported speed improvements are substantial. However, several technical concerns must be resolved before the central claims are fully established. The most significant issues are the lack of a rigorous comparison to structure-based methods on identical test sets, the unclear treatment of sequence length truncation in evaluation, the potential circularity in the disorder analysis, and the absence of error bars or statistical significance testing throughout. The proteome-scale analysis is impressive in scope but the interpretation of extreme frustration classes requires more careful handling of known biases in the underlying energy function. The biological use cases are suggestive but would benefit from quantitative comparison to established FrustraEvo results rather than qualitative agreement.

- **Who would be interested in the results, and why** Protein biophysicists studying energy landscapes and frustration would find this tool valuable for hypothesis generation. Computational biologists working on proteome-scale annotation would benefit from the speed improvement. Protein engineers and designers could use the method for screening designed sequences. Researchers studying intrinsically disordered proteins may find the frustration-disorder coupling analysis of interest. The resource itself, with approximately 1 million precomputed frustration profiles, would be useful to the broader protein science community.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of evaluation
- **Claim pointer** The claim that FrustrAI-Seq achieves a Pearson correlation of 0.86 and MAE of 0.33 on a held-out test set with structure-based topology split
- **Evidence pointer** Section 2.2, Table 1
- **Concern** The evaluation protocol truncates all sequences at 512 residues during training, and the test set evaluation appears to use the same truncation. The authors state that 92% of annotated residues are retained by this cutoff, but the remaining 8% of residues are evaluated separately in a supplementary analysis. The reported performance metrics appear to be computed on the truncated portion only. This is problematic because the method is presented as a general sequence-based predictor, and the behavior on long sequences is a critical practical consideration. The separate evaluation on residues beyond position 512 is mentioned but the results are not presented in the main text. If the model performs substantially worse on these residues, the claim of general applicability is weakened.
- **Why it matters** The truncation strategy directly affects the validity of the reported performance metrics and the practical utility of the method. Users applying FrustrAI-Seq to full-length proteins with more than 512 residues need to know whether predictions on the truncated portion are reliable.
- **Resolution test** Report performance metrics separately for residues below and above position 512 in the main text. If performance degrades on long sequences, discuss the implications and consider whether a sliding window or hierarchical approach would be more appropriate.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparison to existing methods
- **Claim pointer** The claim that FrustrAI-Seq outperforms FrustraMPNN on the highly frustrated class (F1 = 0.54 vs. 0.45)
- **Evidence pointer** Section 2.2, Table 1, Supplementary Table 4
- **Concern** The comparison to FrustraMPNN is potentially unfair for two reasons. First, FrustraMPNN was trained on labels computed with a different sequence separation parameter (SeqDist = 12) than the current default (SeqDist = 3) used for the FrustrAI-Seq training labels. This is acknowledged but the magnitude of the effect is not quantified. Second, FrustraMPNN operates on 3D backbones, which means it requires predicted structures as input. The comparison would be more informative if FrustraMPNN were evaluated on the same structures used to compute the FrustrAI-Seq training labels, or if the authors provided a direct comparison using identical input conditions. The current comparison conflates the effect of the architecture with the effect of the training data.
- **Why it matters** The claim of superiority over a structure-based method is central to the paper's significance. If the comparison is biased, the conclusion that sequence-based prediction is competitive with or superior to structure-based prediction is not established.
- **Resolution test** Retrain or fine-tune FrustraMPNN on the Funstration dataset with SeqDist = 3 labels, or provide a sensitivity analysis showing that the comparison holds across different SeqDist values. Alternatively, evaluate both methods on a common set of structures and sequences with matched training conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The claim that FrustrAI-Seq captures biologically relevant frustration patterns across multiple use cases
- **Evidence pointer** Sections 2.4 through 2.9
- **Concern** Throughout the use-case analyses, no error bars, confidence intervals, or statistical significance tests are reported. The correlations between FrustrAI-Seq and FrustratometeR are presented as point estimates without uncertainty quantification. The comparison of frustration distributions between natural and de novo proteins, the disorder coupling analysis, and the PTM enrichment analysis all lack statistical rigor. For example, the claim that FrustrAI-Seq shows a stronger separation between modified and unmodified positions (40% vs. 20% highly frustrated) compared to FrustratometeR (39% vs. 31%) is presented without any assessment of whether this difference is statistically meaningful.
- **Why it matters** The biological relevance claims are a key part of the paper's contribution. Without uncertainty quantification, it is impossible to assess whether the observed effects are robust or within the range of expected variation.
- **Resolution test** Provide bootstrap confidence intervals or other appropriate uncertainty measures for all reported correlations and effect sizes. For the PTM analysis, report a formal statistical test comparing the enrichment between methods.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of proteome-scale results
- **Claim pointer** The claim that the proteome-scale analysis reveals meaningful patterns of frustration across 136 million proteins
- **Evidence pointer** Section 2.9, Supplementary Fig. 11
- **Concern** The proteome-scale analysis identifies extreme cases of frustration, but the interpretation is complicated by known biases in the underlying energy function. The authors note that transmembrane proteins are enriched in highly frustrated residues because the AWSEM-MDH Hamiltonian assumes an aqueous environment. This is presented as a limitation, but the broader implications for the other extreme classes are not discussed. The finding that proteins with high proportions of neutral frustration show poor agreement between FrustrAI-Seq and FrustratometeR is concerning and not fully explained. The authors suggest these may be intrinsically disordered proteins, but this hypothesis is not tested.
- **Why it matters** The proteome-scale analysis is presented as a demonstration of the method's utility, but the interpretation of the results requires careful consideration of the energy function's biases. If the method systematically misclassifies certain protein classes, this limits its applicability.
- **Resolution test** Provide a more detailed analysis of the proteins with poor FrustrAI-Seq/FrustratometeR agreement, including sequence properties, predicted structure quality, and functional annotations. Test the hypothesis that these are predominantly disordered proteins using an independent disorder predictor.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalization claims
- **Claim pointer** The claim that FrustrAI-Seq generalizes to de novo designed proteins
- **Evidence pointer** Section 2.4, Supplementary Fig. 1, Supplementary Table 2
- **Concern** The de novo test set of 225 proteins is relatively small, and the analysis is presented as a single aggregate result. The differentiation by de novo class (enzymes, fibres, helical bundles, nanoparticles) shows varying performance, with nanoparticles showing the largest deviation from natural frustration distributions. The authors interpret this as the method capturing real differences, but it could also reflect systematic biases in how the model handles sequences far from the training distribution. The claim that the method generalizes to de novo proteins would be strengthened by a more detailed error analysis.
- **Why it matters** Generalization to non-natural sequences is a strong claim that distinguishes this method from simpler baselines. If the method fails on certain classes of de novo proteins, this limits its utility for protein design applications.
- **Resolution test** Provide per-class error analysis for the de novo test set, including examples of misclassified residues and discussion of whether the errors are systematic. Consider testing on additional de novo protein datasets if available.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Section 2.9, first paragraph
- **Evidence pointer** "These analysis are only possible because FrustrAI-Seq scales efficiently"
- **Issue** Grammatical error: "These analysis" should be "These analyses."
- **Required correction** Fix the grammatical error.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 5.10
- **Evidence pointer** "app.ying the same sequecne-filtering criteria"
- **Issue** Typographical errors: "app.ying" should be "applying" and "sequecne" should be "sequence."
- **Required correction** Fix the typographical errors.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 5.10
- **Evidence pointer** "frstarades" should be "frustration"
- **Issue** Typographical error in the description of the large-scale analysis.
- **Required correction** Fix the typographical error.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Section 2.2
- **Evidence pointer** "unseen porteins" should be "unseen proteins"
- **Issue** Typographical error.
- **Required correction** Fix the typographical error.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Section 5.2
- **Evidence pointer** Description of training hyperparameters
- **Issue** The description of the training procedure lacks specific hyperparameter values such as learning rate schedule details, batch size, number of epochs, and early stopping criteria beyond "stagnating validation loss over 5 validations."
- **Required correction** Provide complete hyperparameter details for reproducibility.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Section 5.1
- **Evidence pointer** Description of the Funstration dataset
- **Issue** The dataset description does not specify the exact version of FrustratometeR used, the computational resources required to generate the dataset, or the total compute time. This information is relevant for assessing the reproducibility and cost of the resource.
- **Required correction** Add details on FrustratometeR version and dataset generation cost.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Section 2.5
- **Evidence pointer** "Frustration states predicted by FrustrAI-Seq and computed by FrustratometeR show broad consistency"
- **Issue** The term "broad consistency" is vague. A quantitative measure of agreement beyond the Spearman correlation would strengthen this statement.
- **Required correction** Consider reporting additional agreement metrics such as Cohen's kappa or per-class F1 for the conserved positions.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Completeness of reporting
- **Affected element** Section 2.8
- **Evidence pointer** Description of the mutation analysis
- **Issue** The analysis of mutations at alpha-globin and beta-lactamase sites is described but the number of positions tested and the distribution of correlation values across positions are not reported. The range of Pearson correlations (0.70 to 0.97) is wide, and it would be informative to know how many positions fall at the lower end.
- **Required correction** Report per-position correlation values or a distribution summary.

- **Concern ID** R1-m9
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 2.7
- **Evidence pointer** "we excluded AlphaFold2 predictions with an average pLD DT below 90 during data pre-processing"
- **Issue** The pLD DT threshold of 90 is quite stringent and may exclude many proteins with genuine structural heterogeneity. The authors should discuss the potential impact of this filtering on the diversity of the training data.
- **Required correction** Add a brief discussion of the pLD DT threshold choice and its implications.

- **Concern ID** R1-m10
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Discussion section
- **Evidence pointer** "FrustrAI-Seq establishes local energetic frustration as an AI-inferable evolutionary constraint"
- **Issue** This sentence is somewhat grandiose and could be interpreted as overclaiming. The evidence supports that frustration can be predicted from sequence, but "AI-inferable evolutionary constraint" is a strong framing.
- **Required correction** Consider softening this claim to better match the evidence presented.

## Risk / unsupported claims

- The claim that FrustrAI-Seq "retains biologically relevant performance" is supported only by qualitative agreement in the alpha-globin and beta-lactamase use cases. The quantitative comparison to FrustraEvo results is not presented in the main text.
- The claim that the method "expands frustration analysis to protein regions and classes that were previously inaccessible" is plausible but not directly demonstrated. The disorder analysis is suggestive but the authors acknowledge that disordered proteins were largely excluded from training data.
- The statement that the Funstration dataset is "the largest freely available dataset of local energetic frustration" cannot be fully verified without a systematic comparison to existing resources.
- The claim that FrustrAI-Seq "enables proteome-wide frustration profiling in minutes" is supported by the reported runtime for the human proteome, but the runtime for the full 136-million-protein dataset is not reported.
- The assertion that FrustrAI-Seq "captures the systematic reduction in local energetic frustration introduced by inverse folding" is based on correlation with FrustratometeR on a limited set of designs and would benefit from experimental validation.
- The statement that "FrustrAI-Seq consistently outperformed the Baseline model" for mutation analysis is supported by the reported correlations, but the margin of improvement is modest and the statistical significance is not assessed.