## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, conclusions, materials and methods, and supplementary figure/table references.
- **Assessment boundary** Scientific validity, methodological soundness, clarity of claims, and alignment with stated conclusions. No assessment of editorial fit or journal policy.
- **Shared manuscript claim summary** The authors present a deep learning framework to predict 14-3-3 binding sites from peptide sequences. They benchmark multiple architectures and representations, select an ensemble model, apply it prospectively to seven medically relevant proteins, and validate eight predicted peptides experimentally via fluorescence anisotropy, X-ray crystallography, and molecular dynamics simulations.
- **Visible evidence base** Main text figures (Fig. 1, Fig. 2), tables (Tables 1–3), supplementary figures (SI Fig. S1–S6), supplementary tables (SI Table S1–S9), and methods descriptions.
- **Missing materials affecting confidence** Raw data files, model weights, hyperparameter search details, full crystallographic refinement statistics, MD simulation convergence metrics, and the complete list of 296 screened peptide sequences with scores were not fully accessible in the provided text. The web tool and GitHub repository were not evaluated.

## Reviewer
- **Overall assessment** This manuscript presents a well-structured and practically useful contribution to the prediction of 14-3-3 interaction sites. The combination of systematic model benchmarking, prospective application, and multi-method experimental validation is commendable and relatively rare in the machine learning for biology literature. The work is technically sound in its core claims, though several aspects of the experimental validation and model interpretation require clarification or additional evidence to fully support the conclusions. The manuscript is clearly written and accessible to a broad readership, though some methodological details are under-specified.

- **Who would be interested in the results, and why** Researchers in the fields of protein–protein interaction prediction, phospho-signaling, and intrinsically disordered protein biology would find this work directly relevant. The freely accessible web tool and open code will appeal to experimental biologists seeking to prioritize candidate 14-3-3 binding sites. The benchmarking against 14-3-3-Pred and the systematic comparison of sequence representations and architectures will interest computational biologists working on similar prediction problems.

- **Major strengths** The prospective experimental validation of computationally predicted binding sites is a significant strength, as many similar studies stop at retrospective benchmarking. The use of multiple complementary validation methods (FA, crystallography, MD) provides convergent evidence. The systematic comparison of four sequence representations and three architectures is thorough and well-reported. The model interpretation via virtual mutation analysis is a thoughtful addition that connects model behavior to known structural biology.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation sufficiency
- **Claim pointer** The manuscript claims that "binding to 14-3-3 was confirmed for five out of eight sequences" based on FA assays, and that crystallography "validated the interaction of the newly discovered phosphorylated peptides to 14-3-3."
- **Evidence pointer** Results section, "Experimental validation of binding sites to 14-3-3"; Table 3; Fig. 2
- **Concern** The FA assay results show a wide range of Kd values (1.6 μM to >100 μM), and the classification of "binding" versus "non-binding" appears to rely on a threshold that is not explicitly defined. For peptides with Kd > 100 μM, it is unclear whether these are considered weak binders or non-binders. The crystallography section reports structures for "nearly all peptides that demonstrated binding," but the exact number of structures solved and the quality metrics (resolution, R-free) are not provided in the main text. The MD simulations were performed on only three peptides, and the criteria for selecting these three are not stated.
- **Why it matters** The central claim of the paper is that the model can identify novel, physiologically relevant binding sites. If the experimental validation criteria are not clearly defined, or if the crystallographic evidence is incomplete, the strength of this claim is weakened. The reader cannot fully assess whether the five "confirmed" binders represent a genuine success rate or an artifact of lenient thresholds.
- **Resolution test** Provide explicit criteria for classifying peptides as binders versus non-binders in the FA assay, including the Kd threshold and statistical significance. Report the number of crystal structures solved, their resolutions, and R-free values. State the criteria for selecting peptides for MD simulations and provide convergence metrics (e.g., RMSD over time, equilibration checks).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model evaluation and generalization
- **Claim pointer** The manuscript claims that the ensemble model "systematically outperformed 14-3-3-Pred" and that the model can generalize to "challenging cases like intrinsically disordered proteins."
- **Evidence pointer** Results section, "Model training and benchmarking"; Table 2; Discussion
- **Concern** The benchmarking against 14-3-3-Pred is performed on a single in-house dataset of 92 peptides. It is unclear whether this dataset was used for any model selection or threshold tuning, which could introduce bias. The claim about generalization to intrinsically disordered proteins is based on the inclusion of such proteins in the prospective screen, but the model was trained on short 15-mer peptides, and the performance on full-length disordered proteins is not directly assessed. The correlation between predicted scores and experimental Kd values (r = 0.74) is reported, but the confidence interval and the number of data points are not given.
- **Why it matters** The superiority claim over an existing tool is a key selling point. If the comparison is not rigorously controlled, the conclusion may not hold. Similarly, the generalization claim to disordered proteins is important for the broader applicability of the method, but the evidence is indirect.
- **Resolution test** Clarify whether the in-house dataset was used for any model development or threshold selection. Provide confidence intervals for the correlation coefficient and specify the number of data points. Discuss how the model's performance on disordered proteins compares to structured proteins, ideally with a stratified analysis.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Data leakage and training set composition
- **Claim pointer** The manuscript states that "test peptides with an edit distance on the AA sequence equal to or lower than four were removed to avoid data leakage."
- **Evidence pointer** Materials and Methods, "Model training"
- **Concern** The edit distance threshold of four is applied to remove similar sequences, but the rationale for this specific threshold is not provided. It is unclear whether this threshold is sufficient to prevent homology-based leakage, particularly for short 15-mer peptides where a single amino acid change can significantly alter binding. Additionally, the training set includes 262 "likely non-binding phosphosites obtained randomly from proteins of which already two 14-3-3-binding sites were defined." The assumption that these are non-binding is not experimentally validated and could introduce noise.
- **Why it matters** Data leakage can inflate performance estimates, and noisy labels can degrade model quality. The reader needs to understand the potential impact of these choices on the reported performance.
- **Resolution test** Justify the edit distance threshold with a sensitivity analysis (e.g., test different thresholds and show performance stability). Discuss the potential impact of the assumed non-binding labels and whether any filtering was applied to increase confidence in these labels.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of model interpretation
- **Affected element** Virtual mutation study
- **Evidence pointer** Results section, "Model interpretation"; Fig. 1e
- **Issue** The virtual mutation study is described as "randomly shuffling" amino acids, but the exact procedure is unclear. It is not specified whether shuffling is performed per position across all sequences, or whether the entire sequence is shuffled. The number of shuffles (15) is stated, but the statistical test used to determine significance is not described.
- **Required correction** Provide a precise description of the shuffling procedure and the statistical analysis used to identify positions that contribute most to predictions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility of the web tool
- **Affected element** Web resource
- **Evidence pointer** Abstract; Data availability
- **Issue** The web tool is stated to be freely accessible, but no information is provided about its implementation, input format, or output interpretation. The GitHub repository is mentioned, but the manuscript does not specify the software dependencies or the exact model version deployed.
- **Required correction** Add a brief description of the web tool's interface and functionality, and specify the model version and software environment in the Data availability section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Performance metrics
- **Evidence pointer** Table 2; Results section
- **Issue** Performance metrics are reported as mean ± standard deviation, but the number of replicates and the statistical significance of differences between models are not stated. The claim that the ensemble model "balanced the strengths and weaknesses" is qualitative.
- **Required correction** Report the number of replicates and perform a statistical test (e.g., paired t-test or Wilcoxon test) to support claims of significant differences between models.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of crystallographic data
- **Affected element** X-ray crystallography
- **Evidence pointer** Results section, "X-ray crystallography"; SI Table S9
- **Issue** The manuscript states that crystal structures were obtained for "nearly all peptides that demonstrated binding," but the exact number is not given. The resolution range and R-free values are only in the supplementary table, which was not fully accessible.
- **Required correction** State the number of structures solved in the main text and provide a summary of resolution and R-free values in a main-text table or figure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction
- **Issue** The term "interactome binding sites" is used in the title and abstract, but the manuscript focuses on linear peptide motifs. The distinction between full interactome mapping and motif prediction could be clarified.
- **Required correction** Consider rephrasing to "14-3-3 binding motifs" or "14-3-3 interaction sites" to more precisely reflect the scope of the work.

## Risk / unsupported claims
- The claim that the model can predict "physiologically relevant" binding sites is not directly supported, as the experimental validation was performed in vitro with isolated peptides, not in a cellular context.
- The statement that the model "captures intricate patterns underlying protein-protein interactions" is an interpretation of model performance, not a directly testable claim.
- The assertion that the identified sites "represent potential new binding sites within the 14-3-3 interactome" is reasonable but requires confirmation that these sites are not already known, which is only partially addressed.
- The claim that the model "systematically outperformed" 14-3-3-Pred is based on a single dataset and may not generalize; the statistical significance of the performance difference is not established.
- The relevance of the MD simulations to the physiological context is not fully established, as the simulations were performed on isolated peptides and extended sequences, not on full-length proteins in a cellular environment.