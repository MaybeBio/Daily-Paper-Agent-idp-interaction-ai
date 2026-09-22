## Review setup
- **Input scope** Full manuscript text including abstract, main text, tables, and figure legends
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and suitability for the stated journal context
- **Shared manuscript claim summary** The authors review deep learning-based predictors of intrinsic disorder in proteins, identify 13 such predictors published since 2013, analyze trends in their development, and empirically compare their predictive performance against non-deep-learning methods using the CAID benchmark dataset
- **Visible evidence base** Table 1 (36 predictors since 2013), Table 2 (13 deep learning predictors with inputs, architectures, AUC, runtime), Fig. 1 (development trends), Fig. 2 (heatmap comparison of 11 predictors), Fig. 3 (performance comparison between deep learning and other methods)
- **Missing materials affecting confidence** The CAID dataset details are referenced by URL but not fully described; statistical test results are summarized but individual p-values are not reported; runtime measurement methodology is not fully specified; the criteria for inclusion in Table 1 are described but the full search process is not reproducible from the text alone

## Reviewer
- **Overall assessment** This manuscript provides a useful and timely review of deep learning-based predictors of intrinsic disorder in proteins. The authors have compiled a comprehensive list of predictors, analyzed their architectural trends, and conducted an empirical comparison using a community benchmark. The work is generally well-organized and the conclusions are largely supported by the presented evidence. However, several methodological details regarding the empirical comparison require clarification, and the scope of the review could be more clearly defined relative to existing surveys.
- **Who would be interested in the results, and why** Computational biologists and bioinformaticians working on protein structure and function prediction would find this review valuable. Developers of disorder predictors would benefit from the comparative performance analysis and the identification of well-rounded tools. Experimental biologists studying intrinsically disordered proteins may use the review as a practical guide for selecting appropriate prediction tools. The analysis of architectural trends and future directions would also interest researchers applying deep learning to biological sequence analysis more broadly.
- **Major strengths** The manuscript fills a gap by providing the first dedicated review of deep learning-based disorder predictors. The empirical comparison using the CAID benchmark is a valuable contribution that goes beyond typical narrative reviews. The analysis of availability, runtime, and performance provides practical guidance for tool selection. The discussion of future directions, particularly regarding binding region and linker prediction, is thoughtful and well-motivated.
- **Major Concerns** The empirical comparison methodology has several aspects that need clarification. The statistical testing procedure is described but the specific implementation details are incomplete. The runtime measurements are not fully described in terms of hardware, input sequence characteristics, or number of replicates. The inclusion criteria for Table 1 rely on a manual PubMed search that may not be fully reproducible. The comparison between deep learning and other methods in Fig. 3 does not account for potential confounding factors such as training data differences or publication year.
- **Minor Comments** The manuscript would benefit from a more explicit statement of the search and inclusion criteria for predictors in Table 1. The figure legends could be more detailed to allow standalone interpretation. The discussion of future directions could be expanded with more specific recommendations for architectural innovations. Some statements about the superiority of deep learning methods could be tempered given the relatively small number of methods compared.
- **Technical failings that need to be addressed before the case is established** The statistical comparison methodology needs more detail to be reproducible. The runtime measurement protocol should be specified. The potential for bias in the manual literature search should be addressed.
- **Assessment against Nature-style criteria** Originality: The review is original in its focus on deep learning-based disorder predictors, though the topic overlaps with broader disorder prediction reviews. Scientific importance: The work addresses a growing and important area in computational biology, and the empirical comparison provides useful information for the community. Interdisciplinary readership: The manuscript is primarily relevant to computational biologists and bioinformaticians, with limited appeal to a broader interdisciplinary audience. Technical soundness: The empirical comparison is generally sound but lacks some methodological details that would strengthen reproducibility. Readability for nonspecialists: The manuscript is accessible to readers with a background in bioinformatics but may be challenging for those without prior knowledge of disorder prediction or deep learning concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript makes a useful contribution to the field, but the methodological details of the empirical comparison need to be clarified to fully support the claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological reproducibility
- **Claim pointer** The authors claim to compare predictive performance of 11 deep learning predictors using the CAID dataset and to assess statistical significance of differences.
- **Evidence pointer** Section "Prediction of intrinsic disorder using deep learning", Table 2, Fig. 3
- **Concern** The statistical testing procedure is described only briefly. The authors state that they use the t-test if data are normal and the Wilcoxon signed-rank test otherwise, with normality assessed by the Anderson-Darling test. However, they do not specify what data are being tested (per-protein AUC values? per-residue scores?), how many replicates were used, whether multiple testing correction was applied, or how the 20 random subsets were generated and whether results were consistent across them.
- **Why it matters** The claim that deep learning methods outperform other predictors rests on the statistical significance of the observed differences. Without a clear description of the testing procedure, readers cannot evaluate the robustness of this conclusion or reproduce the analysis.
- **Resolution test** Provide a detailed description of the statistical testing procedure, including the unit of analysis, number of replicates, multiple testing correction method, and results for each of the 20 random subsets. Alternatively, provide the analysis code or a more detailed methods section.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Concern** The runtime comparison is presented in Table 2 and Fig. 2, but the methodology for measuring runtime is not described. It is unclear what hardware was used, what input sequence length was tested, whether multiple runs were averaged, and whether the runtime includes preprocessing steps such as multiple sequence alignment generation.
- **Why it matters** Runtime is a key practical consideration for tool selection, and the authors use it to score predictors in Fig. 2. Without a clear methodology, the runtime values cannot be interpreted or compared across methods.
- **Resolution test** Add a description of the runtime measurement protocol, including hardware specifications, input sequence characteristics, number of replicates, and whether preprocessing steps are included.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scope and completeness
- **Concern** The inclusion criteria for predictors in Table 1 rely on a manual PubMed search using the query "(disorder[Title]) AND (prediction[Title]) AND protein". This search strategy may miss relevant predictors that do not use these exact terms in their titles. The authors also include predictors from community assessments and surveys, but the criteria for inclusion from these sources are not specified.
- **Why it matters** The completeness of the predictor list affects the validity of the trend analysis and the representativeness of the comparison. If predictors are missing, the conclusions about the field's development may be incomplete.
- **Resolution test** Describe the full search strategy, including databases searched, search dates, inclusion and exclusion criteria, and how predictors from community assessments were identified. Consider using additional search terms or databases to ensure comprehensive coverage.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Confounding factors
- **Concern** The comparison between deep learning and other predictors in Fig. 3 does not account for potential confounding factors. For example, deep learning predictors may have been trained on larger or more recent datasets, or may have benefited from advances in related fields. The comparison also mixes predictors from different eras, which may reflect improvements in training data quality rather than architectural advantages.
- **Why it matters** The claim that deep learning methods are superior could be confounded by these factors. Without controlling for them, the conclusion may overstate the advantage of deep learning architectures specifically.
- **Resolution test** Discuss potential confounding factors and, if possible, perform additional analyses that control for training data characteristics or publication year. Alternatively, temper the conclusion to acknowledge these limitations.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table lists predictors with "No" in the "Applies DNN" column, but the footnote states that "No" means the predictor was not published in a peer-reviewed journal. This is confusing because the column header suggests it indicates whether DNN is used.
- **Required correction** Clarify the column header or the footnote to avoid ambiguity. For example, change the column header to "Peer-reviewed publication" or revise the footnote to explain that "No" in this column means the predictor was not peer-reviewed.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Readability
- **Affected element** Fig. 2
- **Evidence pointer** Fig. 2
- **Issue** The heatmap uses color intensity to represent scores, but the legend is not fully described in the text. The scoring criteria for availability are clear, but the runtime categories are described only in the text, not in the figure legend.
- **Required correction** Add a more detailed legend to Fig. 2 that explains the scoring criteria for all three dimensions directly in the figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Section "Deep learning methods outperform other predictors of intrinsic disorder"
- **Evidence pointer** Fig. 3
- **Issue** The section title states that deep learning methods outperform other predictors, but the analysis only covers 11 deep learning predictors and 18 other predictors from a single benchmark. The title may overstate the generality of the finding.
- **Required correction** Consider revising the section title to be more precise, such as "Deep learning methods show favorable performance in the CAID benchmark."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Summary and outlook"
- **Evidence pointer** Section "Summary and outlook"
- **Issue** The discussion of future directions focuses on input features and architectural innovations but does not address potential improvements in training data quality, benchmark design, or evaluation metrics.
- **Required correction** Consider adding a brief discussion of these additional future directions to provide a more comprehensive outlook.

## Risk / unsupported claims
- The claim that deep learning methods are statistically better than other predictors is supported by the presented analysis but requires the statistical methodology to be fully described to be fully verifiable.
- The claim that the current designs "broadly explore the input and network topology spaces" is based on the 13 predictors listed in Table 2, but the diversity of designs may not be fully representative given the small sample size.
- The statement that "deep-learning-based methods will likely continue to show the greatest potential for future improvement" is presented as a conclusion from a cited work, but the authors do not provide independent evidence for this projection.
- The runtime values in Table 2 are presented without a described measurement methodology, making them unverifiable as reported.
- The completeness of the predictor list in Table 1 cannot be fully assessed without a more detailed description of the search and inclusion criteria.