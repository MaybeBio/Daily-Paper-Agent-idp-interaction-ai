## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supplementary material references)
- **Assessment boundary** Scientific content, methodological rigor, claims-to-evidence alignment, and technical soundness as presented in the provided text. No external data or code verification performed.
- **Shared manuscript claim summary** The authors present a kinase-centric deep learning framework (LSTM-based) for predicting intrinsically disordered regions (IDRs) in the human kinome, achieving high predictive performance (AUC = 0.97). They categorize short and long IDRs, analyze their distribution relative to kinase domains, compute a conservation index across 137 kinase families, identify 1039 functional disorder hotspots, and propose a structural integrity framework linking IDRs to signaling and substrate specificity.
- **Visible evidence base** Abstract, Introduction, Methods (data collection, feature selection, model architecture, functional significance scoring, family-based analysis, disorder-to-order transition), Results (model performance, disorder distribution, family conservation scores, hotspot identification, AKT1 case study), Discussion, Supplementary Material references, Code/data availability statement.
- **Missing materials affecting confidence** Supplementary Tables 1–9, Supplementary File (equations, parameter details, model validations), Figure 1–5 contents, actual code repository contents, detailed hyperparameter settings, training/validation data split specifics, and full results of comparative analyses. These are referenced but not provided in the submitted text.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely topic: the functional characterization of intrinsically disordered regions in the human kinome using a specialized deep learning approach. The authors present a reasonable motivation for a kinase-specific disorder predictor and report competitive performance metrics. However, several methodological details are underspecified, some claims appear overstated relative to the evidence shown, and the biological validation is largely descriptive rather than experimentally or statistically robust. The manuscript has potential but requires substantial revision and additional evidence to establish its claims convincingly.
- **Who would be interested in the results, and why** Researchers in computational biology, protein disorder prediction, kinase biology, and phospho-signaling. The resource (web server, code, data) may be useful for those studying kinase regulation, disorder-mediated interactions, and mutation effects in kinases. The conservation analysis across kinase families could interest evolutionary biologists studying disorder-function relationships.
- **Major strengths**
  1. The focus on a kinase-specific disorder predictor is well motivated, given the known limitations of generic proteome-wide predictors for this important protein family.
  2. The integration of multiple functional features (domain overlap, motif proximity, phosphorylation, mutations) into a scoring framework is a thoughtful approach.
  3. The authors provide a publicly accessible web server and code repository, which enhances utility and reproducibility.
  4. The comparative evaluation against several existing tools (flDPnn, ADOPT, DisoFLAG, AIUPred) is a useful benchmark.
  5. The identification of N-terminal bias in functional hotspots and the AKT1 case study provide concrete biological examples.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency and reproducibility
- **Claim pointer** The authors claim a "standardized and kinase-centric approach for IDR prediction" with a "deep bidirectional LSTM network" achieving AUC = 0.97.
- **Evidence pointer** Methods: Model architecture; Results: Fig. 1, Table 1
- **Concern** The model architecture description is inconsistent between the Methods and Results sections. The Methods describe a bidirectional LSTM with 256 units, a dropout of 40%, a layer with 128 nodes, and 64 fully connected dense neurons. The Results describe "dual LSTM layers (100 and 50 units) interspersed with dropout (0.2)". These are materially different architectures. Additionally, the feature vector composition is described differently: the Methods mention hydrophobicity, disorder propensity, and net charge, while the Results mention a feature matrix scaled via StandardScaler without specifying which features. The training/validation data split, hyperparameter tuning procedure, and early stopping criteria are not described. The claim of "high predictive performance" cannot be fully assessed without these details.
- **Why it matters** Reproducibility is a core requirement for computational methods. Inconsistent architecture descriptions and missing training details prevent independent replication and undermine confidence in the reported performance metrics.
- **Resolution test** Provide a single, consistent description of the final model architecture, all input features, training/validation/test split strategy, hyperparameter optimization procedure, and the exact data preprocessing steps. Clarify which architecture was used for the final reported results.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for biological claims
- **Claim pointer** The authors claim to have uncovered "1039 functional disorder region hotspots that correlate with dynamic conformational shifts, phosphorylation sites, functional motif enrichment, and mutation impact embedded within IDRs."
- **Evidence pointer** Results: Analysis of functional hotspot disorder regions; Supplementary Tables 6–9
- **Concern** The term "functional disorder hotspots" is defined by a composite score with empirically determined weights (α, β, γ, δ), but the actual values of these weights are not provided in the main text. The threshold of 0.12 for hotspot classification is stated without justification. The correlation with "dynamic conformational shifts" is asserted but no direct evidence (e.g., molecular dynamics, experimental conformational data) is presented. The claim that hotspots "correlate" with phosphorylation sites and mutations appears to be based on co-occurrence within the same disordered region, but no statistical test (e.g., enrichment analysis against background) is described. The biological significance of the 1039 hotspots is therefore not established beyond descriptive co-localization.
- **Why it matters** The central biological contribution of the manuscript rests on the identification and functional interpretation of these hotspots. Without clear definitions, statistical support, and validation, the claim of "functional" hotspots is not supported.
- **Resolution test** Provide the exact values of all empirical weights, justify the 0.12 threshold (e.g., through sensitivity analysis or comparison to null distributions), and perform formal statistical enrichment tests for phosphorylation sites, mutations, and functional motifs within hotspots versus non-hotspot disordered regions. Clarify what evidence supports the link to "dynamic conformational shifts."

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of the disorder-to-order transition model
- **Claim pointer** The authors state they "developed a biophysically informed scoring framework" to evaluate disorder-to-order transitions, and present the AKT1 S2 phosphorylation case as evidence (ΔΔG = −0.500 kcal/mol, transition probability 77.02%).
- **Evidence pointer** Methods: Disorder to order transition; Results: Structural integrity section, Fig. 5
- **Concern** The "biophysically informed" model is described as an "empirical free energy model" combining Chou–Fasman propensities, Kyte–Doolittle hydrophobicity, net charge, side chain volume, flexibility indices, Shannon entropy, and a Miyazawa–Jernigan contact potential. However, no equation is provided in the main text, and the reader is referred to the Supplementary File for "all equations, parameter details, and model validations." The AKT1 example shows a ΔΔG of −0.500 kcal/mol for S2 phosphorylation, but the wild-type ΔG is not stated for this case. In the mutation example (V4L), the ΔG values are given as −0.274 and −0.208 kcal/mol, but the units are uncertain ("kcal/mol, I assume" in the text). The transition probability of 77.02% is presented without explaining how it is derived from the ΔG. The model's accuracy is not benchmarked against any experimental data on disorder-to-order transitions.
- **Why it matters** The disorder-to-order transition framework is presented as a novel contribution. Without the actual equations, parameter values, and validation against known experimental cases, the model's reliability and interpretability cannot be assessed.
- **Resolution test** Include the full model equations and all parameter values in the main text or a clearly referenced supplement. Provide a benchmark against experimentally characterized disorder-to-order transitions in kinases or related proteins. Clarify the units and the derivation of the transition probability from ΔG.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Comparative evaluation fairness and completeness
- **Claim pointer** The authors state their model "outperforms flDPnn, flDPnn2, ADOPT, DisoFLAG, AIUPred in AUC, and ROC metrics."
- **Evidence pointer** Results: Comparative analysis, Fig. 2, Table 2
- **Concern** The comparative evaluation is described only in terms of AUC values (flDPnn: 0.83, ADOPT: 0.93, DisoFLAG: 0.88, AIUPred: 0.77, flDPnn2: 0.84). It is unclear whether these tools were run on the same test set, with the same preprocessing, and with their default or optimized parameters. The authors' model achieves AUC = 0.97, but the comparison may be confounded by differences in training data, class definitions, or evaluation protocols. Additionally, the claim of "outperforming" is based solely on AUC; other metrics (precision, recall, F1, calibration) are not reported for the comparators.
- **Why it matters** A fair and comprehensive benchmark is essential to support the claim that a kinase-specific approach is superior to generic predictors. Incomplete or biased comparisons weaken this central argument.
- **Resolution test** Describe the exact evaluation protocol, including the test set composition, whether the same sequences were used for all tools, and how each tool was configured. Report multiple performance metrics (e.g., precision, recall, F1, Matthews correlation coefficient) for all methods. Consider statistical significance testing for performance differences.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor in conservation analysis
- **Claim pointer** The authors report "conserved mean disorder score of 0.50 ± 0.02 (n = 17 regions across three kinases)" for AKT and use a Kolmogorov–Smirnov test (P < .01) to compare CDK family disorder scores.
- **Evidence pointer** Results: Distribution of disorder scores across kinase families; Fig. 3; Supplementary Tables 4 & 5
- **Concern** The conservation analysis relies on three metrics (SSS, PSS, DRC) combined into a disorder score, but the weighting scheme is not described. The sample sizes are small (e.g., n = 1 for SRC), and the statistical comparison between short and long IDR conservation uses Spearman's rank correlation, but the reported correlation coefficient and p-value are not given. The Kolmogorov–Smirnov test is mentioned for CDK families, but the comparison groups and the rationale for this test are unclear. The claim that "long IDRs are more conserved" is not supported by a formal statistical test comparing the two distributions.
- **Why it matters** The conservation analysis is a key component of the functional characterization. Without proper statistical treatment and clear methodology, the conclusions about differential conservation of short versus long IDRs are not reliable.
- **Resolution test** Describe the weighting scheme for the disorder score, report the Spearman correlation coefficient and p-value, and perform a formal statistical comparison (e.g., Mann–Whitney U test) between short and long IDR conservation scores across families. Provide effect sizes and confidence intervals.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract, Results
- **Evidence pointer** Abstract; Results: High confidence prediction section
- **Issue** The abstract states "A ubiquitous and reversible phosphorylation is important for molecular signaling cascades," which is grammatically awkward. The Results section contains a sentence fragment: "Trained over 100 epochs with the Adam optimizer." The phrase "kcal/mol, I assume" in the Results section is informal and inappropriate for a scientific manuscript.
- **Required correction** Revise the abstract for grammatical correctness. Complete the sentence about training. Remove the informal "I assume" and provide the correct units with confidence.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure and table completeness
- **Affected element** Figures 1–5, Supplementary Tables 1–9
- **Evidence pointer** Results sections referencing figures and tables
- **Issue** The manuscript references five figures and nine supplementary tables, but none are included in the provided text. It is impossible to assess the data quality, the ROC curves, the distribution plots, or the detailed results in the tables.
- **Required correction** Ensure all figures and supplementary tables are included in the submission and are properly referenced and described in the text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Methods, Results
- **Evidence pointer** Methods: Model architecture; Results: High confidence prediction section
- **Issue** The model is described as "deep bidirectional LSTM" in the Methods and "dual LSTM layers" in the Results. The term "IDR" is used interchangeably with "disorder region" and "DR" in different sections.
- **Required correction** Use consistent terminology throughout the manuscript. Standardize on "IDR" for intrinsically disordered regions and provide a single, consistent description of the model architecture.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reference to external resources
- **Affected element** Web server URL, GitHub repository
- **Evidence pointer** Abstract; Code and data availability
- **Issue** The web server URL (https://ciods.in/kindisorder) and GitHub repository (https://github.com/naveen-joy-18/...) are provided, but their accessibility and content cannot be verified from the manuscript text.
- **Required correction** Ensure the web server and repository are functional and contain all necessary code, data, and documentation. Consider adding a statement about the date of last access or versioning.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Funding and conflict of interest
- **Affected element** Research support, Funding, N/A sections
- **Evidence pointer** Research support; Funding; N/A
- **Issue** The "Research support" section acknowledges funding from Yenepoya University and Dr. Mukhtar Ahmed (ORF-2025-984, King Saud University), but the "Funding" section states "None declared." This appears contradictory.
- **Required correction** Clarify the funding sources. If the research support is not financial funding, state so explicitly. Ensure consistency between the two sections.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Data collection
- **Evidence pointer** Methods: Data collection and processing
- **Issue** The description of the training data is unclear. The authors state they used DisProt 9.7 with 12,790 disordered regions across 3,114 proteins, then extracted 1,271 disordered regions specific to human proteins, and then "retrieved 523 human protein kinome disorder region entries from the UniProt database." The relationship between these datasets and how they were combined for training is not explained.
- **Required correction** Clarify the data curation pipeline, including how the DisProt and UniProt data were merged, how duplicates were handled, and how the final training set was constructed.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Results: Structural integrity section
- **Evidence pointer** Results: Structural integrity of intrinsically disordered regions in human kinome
- **Issue** The AKT1 case study is presented as evidence for the framework's utility, but only one example is shown. The statement "The proposed framework allows users to input a kinase, its disordered region, and a missense mutation, and returns a probability score" suggests a tool, but the validation of this tool is limited to a single anecdotal case.
- **Required correction** Provide additional validation examples or a systematic evaluation of the framework's predictions against known experimental data.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Inconsistent model architecture descriptions between Methods and Results.
  - R1-M2: Undefined empirical weights and threshold for hotspot classification; no statistical support for "functional" hotspot claims.
  - R1-M3: Missing equations and validation for the disorder-to-order transition model.
  - R1-M4: Incomplete comparative evaluation protocol.
  - R1-M5: Insufficient statistical rigor in conservation analysis.

- **Assessment against Nature-style criteria**
  - **Originality**: Moderate. The application of a kinase-specific LSTM predictor is a reasonable incremental contribution, but the underlying approach (deep learning for disorder prediction) is well established. The integration of multiple functional features into a scoring framework has some novelty, but similar concepts exist in the literature.
  - **Scientific importance**: Moderate. IDRs in kinases are functionally significant, and a reliable predictor could be useful. However, the biological insights presented are largely descriptive and do not fundamentally advance understanding of kinase regulation.
  - **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to computational biologists and kinase researchers. The methods and results are unlikely to attract a broad interdisciplinary audience.
  - **Technical soundness**: Currently insufficient. The methodological inconsistencies, missing details, and lack of statistical validation undermine confidence in the reported results.
  - **Readability for nonspecialists**: Below average. The manuscript contains jargon and informal language, and the logical flow is sometimes disrupted by incomplete descriptions and unclear transitions between sections.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant problem and has a useful resource component, but the methodological inconsistencies, missing details, and insufficient statistical support prevent the claims from being fully evaluated. Substantial revision and additional evidence are required before the case is established.