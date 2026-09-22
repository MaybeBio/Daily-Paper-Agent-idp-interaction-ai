## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality. No assessment of formatting or editorial style beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors present an interpretable ensemble machine-learning framework integrating protein language model embeddings of sequence and predicted structure to predict liquid-liquid phase separation (LLPS) propensity, classify proteins as self-separating (PS-Self) or partner-dependent (PS-Part), identify critical phase-separating regions, and quantify mutation-induced perturbations in LLPS. They report superior performance over existing methods, particularly for partner-dependent proteins, and apply the framework to disease-associated variant databases to implicate LLPS dysregulation in disease pathogenesis.
- **Visible evidence base** Abstract, Introduction, Results (narrative only, no figures or tables visible), Discussion, Materials and Methods. Figure and table references are cited but their content is not visible in the provided material.
- **Missing materials affecting confidence** All figures, supplementary figures, supplementary tables, and supplementary data files are referenced but not provided. This includes the main performance comparison plots (Fig. 2B-F), critical region examples (Fig. 3), proteome-wide analyses (Fig. 4), variant effect distributions (Fig. 5), and individual case studies (Fig. 6). Without these, quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important problem: interpreting the pathogenic impact of coding variants in intrinsically disordered regions through the lens of liquid-liquid phase separation. The proposed framework is conceptually sound, combining sequence and structure embeddings in an ensemble architecture with a hierarchical classification strategy. The emphasis on interpretability and on the partner-dependent class, which is poorly handled by existing tools, is a genuine strength. However, the manuscript as provided is essentially a narrative summary of results without the supporting figures and tables. Several key claims, including the magnitude of performance gains, the statistical significance of enrichment analyses, and the validity of the ΔLLPS metric, cannot be assessed from the supplied material. The methods section is detailed but omits critical information about training data composition, negative set construction, and evaluation protocols. The work has clear potential for a high-impact venue, but the current submission does not provide sufficient evidence to establish the case.
- **Who would be interested in the results, and why** Researchers in computational biology, protein biophysics, and human genetics would be interested. Specifically, those working on variant effect prediction, phase separation, biomolecular condensates, and the molecular mechanisms of disease-associated mutations in disordered regions. The framework's interpretability and focus on partner-dependent proteins address known gaps in the field, making it relevant to both method developers and experimentalists studying condensate biology.
- **Major strengths** 1. The problem is well-motivated and clinically relevant, addressing a clear gap in variant interpretation for IDRs. 2. The hierarchical classification strategy that separates LLPS detection from PS-Self/PS-Part subtyping is a thoughtful design choice. 3. The integration of sequence and structure embeddings through cross-attention is technically sound and leverages state-of-the-art protein language models. 4. The emphasis on interpretability, with residue-level attribution and identification of critical regions, is a significant advantage over black-box predictors. 5. The application to disease-associated variant databases provides a concrete and potentially impactful use case.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (training data composition), R1-M2 (negative set construction), R1-M3 (ΔLLPS metric validation), R1-M4 (performance comparison methodology), R1-M5 (statistical reporting), R1-M6 (variant database filtering).
- **Assessment against Nature-style criteria** Originality: The combination of pLM embeddings, ensemble architecture, hierarchical classification, and interpretability for LLPS prediction is novel, though individual components have been used before. Scientific importance: High, given the growing recognition of LLPS in disease and the poor performance of existing tools on IDR variants. Interdisciplinary readership: The topic bridges computational biology, biophysics, and clinical genetics, appealing to a broad audience. Technical soundness: The architecture is reasonable, but the provided evidence is insufficient to verify performance claims. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some methods details are dense. Overall, the work has the potential to meet Nature-style standards, but the current evidence base is inadequate.
- **Recommendation posture** Supportive if technical concerns are resolved and full results are provided. The conceptual framework and motivation are strong, but the manuscript cannot be accepted in its current form without the missing figures, tables, and methodological clarifications.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and methods transparency
- **Claim pointer** The authors claim their framework outperforms existing methods on independent benchmark datasets, with the largest gains for partner-dependent proteins.
- **Evidence pointer** Results section, Figure 2B-F; location not provided
- **Concern** The composition of the training set is not fully described. The authors state they collected 4,857 LLPS proteins from multiple sources, but the exact breakdown by source, the criteria for inclusion, and the handling of redundancy (e.g., sequence similarity clustering) are not specified. This is critical because training set composition directly affects model performance and generalizability.
- **Why it matters** Without a clear description of the training data, it is impossible to assess potential biases, such as overrepresentation of certain protein families or sequence similarity to test set proteins, which could inflate reported performance.
- **Resolution test** Provide a detailed breakdown of the training set by source, a description of redundancy removal (e.g., CD-HIT clustering at a specified identity threshold), and a statement on whether any test set proteins share significant sequence identity with training proteins.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and methods transparency
- **Claim pointer** The authors state they constructed a negative set of proteins unlikely to undergo phase separation by removing positive set proteins and their first interactors from the PDB.
- **Evidence pointer** Materials and Methods, "Curating LLPS and non-LLPS protein datasets"; location not provided
- **Concern** The negative set construction is problematic. Removing only first interactors from the PDB is insufficient to ensure that remaining proteins do not undergo phase separation. Many PDB proteins may participate in phase separation through mechanisms not captured by interaction data, and the absence of evidence is not evidence of absence. Furthermore, the PDB is heavily biased toward well-folded, crystallizable proteins, which may not be representative of the diversity of non-LLPS proteins in the proteome.
- **Why it matters** A poorly constructed negative set can lead to a model that learns to distinguish LLPS proteins from a narrow class of structured proteins, rather than from the full diversity of non-LLPS proteins. This would undermine the model's generalizability and the validity of performance comparisons.
- **Resolution test** Describe additional filtering steps to exclude known LLPS proteins from the negative set, such as screening against LLPS databases and literature-curated lists. Consider including disordered non-LLPS proteins in the negative set to better reflect the target application. Provide a characterization of the negative set in terms of sequence diversity and functional annotation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Metric validity
- **Claim pointer** The authors define ΔLLPS as the sum of per-residue score differences between mutant and wild-type proteins and use it to quantify mutation-induced perturbations in LLPS.
- **Evidence pointer** Materials and Methods, "Genomic Variant Dataset Analyses" and "Amino Acid Composition Analyses and Mutation Effect Predictions"; location not provided
- **Concern** The ΔLLPS metric is defined as a sum over the entire protein sequence. This is problematic because a mutation at one position will affect the per-residue scores at many positions due to the sliding window approach, and summing these differences may amplify noise. Moreover, the metric is not normalized by sequence length, making comparisons across proteins of different lengths potentially misleading. The manuscript does not provide any validation that ΔLLPS correlates with experimentally measured changes in phase separation behavior.
- **Why it matters** The central application of this framework is to interpret disease variants. If the ΔLLPS metric is not validated against experimental data, the biological conclusions drawn from its application are unsupported.
- **Resolution test** Validate ΔLLPS against a set of experimentally characterized mutations with known effects on phase separation (e.g., from the literature on FUS, TDP-43, hnRNPA1). Report correlation coefficients and discuss any discrepancies. Consider normalizing ΔLLPS by sequence length or by the number of residues in the critical region.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evaluation methodology
- **Claim pointer** The authors claim their ensemble model outperforms existing methods on an external benchmark dataset.
- **Evidence pointer** Results section, Figure 2B-F; location not provided
- **Concern** The description of the external benchmark dataset is incomplete. The authors state it was compiled from various databases, but the exact composition, the number of proteins in each class, and the criteria for labeling are not provided. Furthermore, it is unclear whether the benchmark dataset was used consistently across all compared methods, and whether the comparison was fair in terms of training data overlap.
- **Why it matters** Performance comparisons are only meaningful if the benchmark is well-defined and the evaluation protocol is consistent across methods. Without this information, the reported improvements cannot be verified.
- **Resolution test** Provide a detailed description of the external benchmark dataset, including the number of proteins per class, the source databases, and the labeling criteria. State explicitly that no proteins in the benchmark were used in training or validation. Describe the evaluation protocol, including any hyperparameter tuning on the benchmark.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical reporting
- **Claim pointer** The authors report AUC and PR-AUC values for their models and comparisons with existing methods.
- **Evidence pointer** Results section, Figure 2B-F; location not provided
- **Concern** No confidence intervals, standard deviations, or statistical significance tests are reported for any of the performance metrics. Given the relatively small size of some classes (e.g., PS-Self and PS-Part), performance estimates may be noisy, and the reported differences between methods may not be statistically significant.
- **Why it matters** Without measures of uncertainty, it is impossible to assess whether the reported performance differences are meaningful or within the range of random variation.
- **Resolution test** Report confidence intervals for all performance metrics, ideally from multiple runs with different random seeds. Perform statistical significance tests (e.g., McNemar's test for paired comparisons) between the proposed method and each baseline.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** Yes
- **Axis** Data and methods transparency
- **Claim pointer** The authors state they analyzed variants from ClinVar and denovo-db, filtering for missense mutations and mapping them to predicted critical regions.
- **Evidence pointer** Materials and Methods, "Genomic Variant Dataset Analyses"; location not provided
- **Concern** The filtering criteria for ClinVar variants are described, but the exact numbers of variants retained at each step are not reported. The authors state they included variants with specific review statuses and clinical significance labels, but the distribution of these labels across the final dataset is not described. For denovo-db, the inclusion criteria are even less clear.
- **Why it matters** The interpretation of the variant analysis depends on the composition of the dataset. If the dataset is dominated by variants from a few genes or disease classes, the conclusions may not be generalizable.
- **Resolution test** Provide a flow diagram or table showing the number of variants retained at each filtering step for both ClinVar and denovo-db. Report the distribution of clinical significance labels and the number of unique genes represented.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states the framework "integrates protein language model embeddings of sequence and predicted structure" but does not specify which models are used. This is a key detail for reproducibility.
- **Required correction** Mention ESM2 and SaProt by name in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Overview of Our Computational Framework"
- **Evidence pointer** Results section, Figure 1; location not provided
- **Issue** The description of the ensemble architecture is brief. It is unclear how the cross-attention mechanism combines the two modalities and whether the ensemble weights are learned or fixed.
- **Required correction** Provide a more detailed description of the ensemble architecture, including the cross-attention mechanism and how the final prediction is computed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Dataset description and model performance evaluation"
- **Evidence pointer** Results section, Figure 2A; location not provided
- **Issue** The authors state they collected 4,857 LLPS proteins but do not specify how many were used for training versus validation. The text mentions a validation set of 232 proteins, but the training set size is not explicitly stated.
- **Required correction** State the exact number of proteins in the training and validation sets.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Identifying critical regions promoting protein phase separation"
- **Evidence pointer** Results section, Figure 3; location not provided
- **Issue** The sliding window approach is described, but the threshold for defining "critical regions" is not specified. The text mentions a "score threshold" but does not state its value.
- **Required correction** Specify the threshold value used to define critical regions and justify its selection.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Proteome-wide enrichment & biochemical features analyses"
- **Evidence pointer** Results section, Figure 4; location not provided
- **Issue** The authors report that 7,514 proteins (37%) show high propensity to phase separate, but the threshold for "high propensity" is not defined.
- **Required correction** State the score threshold used to classify proteins as having high LLPS propensity.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion mentions that the model "captures transient local structure and ensemble properties" but does not provide evidence for this claim. This is speculative without supporting analysis.
- **Required correction** Either provide evidence for this claim or soften the language to indicate it is a hypothesis.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Materials and Methods, "Curating LLPS and non-LLPS protein datasets"
- **Evidence pointer** Materials and Methods; location not provided
- **Issue** The authors state they used data from a recent experimental study identifying 1,518 endogenous condensate proteins, but the citation is not provided in the text.
- **Required correction** Add the citation for this study.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Materials and Methods, "Ensemble model architecture"
- **Evidence pointer** Materials and Methods; location not provided
- **Issue** The description of the training procedure is incomplete. The authors mention binary cross-entropy loss, Adam optimizer, and batch size, but do not specify the learning rate schedule or the number of training epochs.
- **Required correction** Provide full training details, including learning rate, number of epochs, and any regularization techniques.

## Risk / unsupported claims
- The claim that the framework "outperforms existing methods" cannot be verified without the performance comparison figures and tables.
- The claim that predicted critical regions "align with experimentally validated phase-separating regions" cannot be verified without the supporting figures and statistical tests.
- The claim that pathogenic mutations are "enriched in predicted phase-separating regions" cannot be verified without the variant analysis figures and tables.
- The claim that the model "captures transient local structure and ensemble properties" is speculative and not supported by the provided evidence.
- The claim that the framework "provides a mechanistic link between phase separation dysregulation and disease-associated mutations" is an interpretation that requires experimental validation, which is not provided.
- The ΔLLPS metric is presented as a measure of mutation impact, but its validity is not established against experimental data.