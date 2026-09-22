## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, discussion) without supplementary figures or tables
- **Assessment boundary** Scientific claims, methodological soundness, and evidence quality as presented in the provided text
- **Shared manuscript claim summary** The authors present LoRA-DR-suite, a suite of protein language model (PLM) based classifiers with low-rank adaptation (LoRA) for predicting intrinsic disorder regions (IDRs) and soft disorder regions (SDRs) from protein sequences. They also introduce SoftDis, a large-scale database of soft disorder annotations derived from crystallographic B-factors and missing residues across PDB structures. The authors report competitive or superior performance against established disorder predictors on CAID benchmarks and demonstrate that soft disorder predictions correlate with AlphaFold pLDDT scores.
- **Visible evidence base** Main text tables (Tables 1-2 for intrinsic disorder, Table 3 for soft disorder), Figures 1-4 described in text, Supplementary Tables S1-S9 referenced but not provided
- **Missing materials affecting confidence** Supplementary tables and figures (S1-S9), full benchmark results for all compared methods, detailed hyperparameter configurations, SoftDis database schema and statistics, attention/contact map analysis details

## Reviewer
- **Overall assessment** The manuscript presents a technically sound application of parameter-efficient fine-tuning to protein disorder prediction, with a valuable new database contribution. The core methodological idea, using LoRA-adapted PLM embeddings for both intrinsic and soft disorder classification, is sensible and the reported performance is competitive. However, several concerns regarding evaluation rigor, statistical significance, and the novelty of the soft disorder prediction task relative to existing tools need to be addressed. The SoftDis database is a potentially significant community resource, but its construction and validation require more detailed description.
- **Who would be interested in the results, and why** Researchers in computational biology and bioinformatics working on protein disorder prediction, structural biology, and protein function annotation. The SoftDis database will be of interest to those studying protein flexibility, dynamics, and interactions. The methodological approach may also interest machine learning practitioners applying parameter-efficient fine-tuning to biological sequence problems.
- **Major strengths** 1) The SoftDis database is a large-scale resource (approximately 500,000 chains) that addresses an underexplored aspect of protein disorder. 2) The use of LoRA for parameter-efficient adaptation of PLMs is timely and computationally practical. 3) The evaluation across multiple CAID benchmark editions provides a reasonable assessment of generalization. 4) The analysis linking soft disorder predictions to pLDDT scores offers a useful biological validation.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria** Originality: moderate. The application of LoRA to disorder prediction is incremental, though the SoftDis database adds a novel resource. Scientific importance: moderate to high, given the functional relevance of disorder and the potential utility of SoftDis. Interdisciplinary readership: limited; primarily bioinformatics and structural biology communities. Technical soundness: generally sound but with gaps in statistical rigor and comparison completeness. Readability for nonspecialists: adequate, though some methodological details are dense.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding statistical significance testing, comparison completeness, and database validation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** "ESM2_650M-LoRA achieved the best overall performance (ROC AUC 0.833, PR AUC 0.510)" and similar performance claims across Tables 1-3
- **Evidence pointer** Tables 1-3, Section 2.2, Section 2.4
- **Concern** Performance differences between models are reported without any measure of variance or statistical significance. The manuscript states that ESM2_650M-LoRA "achieved the best overall performance" but does not report confidence intervals, standard deviations across multiple runs, or significance tests (e.g., McNemar's test, DeLong's test for AUC comparison). Given that differences between some models appear small (e.g., ROC AUC 0.837 vs 0.838 on CAID2_NOX), it is unclear whether these differences are meaningful.
- **Why it matters** Without statistical significance testing, the claim that LoRA-DR-suite models "match or surpass state-of-the-art methods" is not rigorously supported. Small performance differences may be due to random variation, particularly given the stochastic nature of neural network training.
- **Resolution test** Provide confidence intervals or standard deviations for all reported metrics, and perform appropriate statistical tests (e.g., DeLong test for AUC, bootstrap resampling) to establish whether performance differences between models and against baselines are significant.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Comparison completeness
- **Claim pointer** "The performance of LoRA-DR-suite models was evaluated against several established methods for intrinsic disorder prediction"
- **Evidence pointer** Section 2.2, Tables 1-2
- **Concern** The comparison against established methods is incomplete. The text mentions "the best performing tools that participated in the corresponding CAID round" but does not specify which tools these are, nor does it report their full performance metrics. For CAID3, only the top 5 models with full residue coverage are compared, and the criteria for "best performing" are not defined. Additionally, the comparison on CAID3_NOX is complicated by the filtering of models based on residue coverage, which may bias results.
- **Why it matters** A fair and complete comparison is essential to substantiate the claim that LoRA-DR-suite is competitive with or superior to existing methods. Selective comparison could give a misleading impression of relative performance.
- **Resolution test** List all compared methods explicitly, report their full performance metrics on all benchmarks, and justify the inclusion/exclusion criteria. Consider reporting results on the full CAID3_NOX set without filtering, or clearly explain why filtering is necessary and how it affects comparability.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Database validation
- **Claim pointer** "SoftDis, a unique soft disorder database constructed for approximately 500,000 PDB chains"
- **Evidence pointer** Section 2.3, Section 3.2
- **Concern** The SoftDis database construction is described at a high level, but several critical details are missing. The clustering procedure (MMSeqs2 at 90% identity and 90% coverage) is stated, but the rationale for these thresholds is not given. More importantly, the database is not validated against any external reference. The authors state that "we statistically demonstrated a significant correlation between SDRs and interface sites" but do not provide the statistical details or results in the main text. The biological relevance of the soft disorder definition is asserted but not independently verified.
- **Why it matters** SoftDis is presented as a major contribution, but without validation, its reliability and utility are uncertain. Users need confidence that the annotations are biologically meaningful and not artifacts of the computational pipeline.
- **Resolution test** Provide a detailed validation of SoftDis, including: (1) comparison of soft disorder annotations against independent experimental data (e.g., hydrogen-deuterium exchange, limited proteolysis), (2) statistical analysis of the SDR-interface correlation with effect sizes and confidence intervals, (3) assessment of the impact of clustering parameters on database composition and downstream predictions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.7, Figure 4
- **Evidence pointer** Section 2.7
- **Issue** The analysis of attention scores via contact prediction is described briefly and the connection to disorder is not fully explained. The text states that "training on soft disorder leads to variations observed at much greater distances" but does not explain why this is biologically meaningful or how it relates to the disorder prediction task.
- **Required correction** Expand the description of the attention analysis, clarify the biological interpretation of the observed differences, and explain how this analysis supports the main claims of the paper.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 3.4
- **Evidence pointer** Section 3.4, Supplementary Table S8
- **Issue** The hyperparameter search is described as using "40 trials using random parameter search" but the specific hyperparameter ranges and the final selected values for each model are not provided in the main text. The supplementary table is referenced but not available for review.
- **Required correction** Provide the hyperparameter search space and final selected hyperparameters for each model in the main text or ensure the supplementary material is accessible and complete.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability section
- **Evidence pointer** Data availability section
- **Issue** The statement "LoRA-DR-suite models and SoftDis dataset are available at https://huggingface.co/CQSB" is vague. It is unclear whether the full database, model weights, and code are all accessible, and whether there are any usage restrictions.
- **Required correction** Specify exactly what is available (model weights, database files, code), the format of the data, and any licensing terms.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2.5, Figure 3
- **Evidence pointer** Section 2.5
- **Issue** The correlation values between pLDDT and disorder predictions are reported (e.g., 0.865, 0.816) but the text does not specify whether these are Spearman or Pearson correlations, nor does it provide confidence intervals or p-values.
- **Required correction** Specify the correlation type, report confidence intervals and p-values, and clarify the sample size for each correlation analysis.

## Risk / unsupported claims
- The claim that LoRA-DR-suite "matches or surpasses state-of-the-art methods" is not fully supported due to incomplete comparisons and lack of statistical significance testing.
- The claim that SoftDis annotations are biologically meaningful is asserted but not independently validated.
- The claim that "adapted embeddings better align with disorder" (Section 2.6) is based on a single supplementary table and lacks detailed methodology.
- The claim that soft disorder predictions correlate with pLDDT is presented without full statistical details.
- The claim that LoRA-DR-suite can "reliably identify putative binding regions without requiring task-specific training" (Section 2.2) is based on indirect evidence and requires further validation.