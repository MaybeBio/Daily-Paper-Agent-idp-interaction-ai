## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and presentation of the review article as provided
- **Shared manuscript claim summary** The authors present a narrative review of computational methods for predicting intrinsically disordered proteins/regions (IDPs/IDRs), covering disorder prediction, binding mode prediction, binding site prediction, and function prediction. They claim to be the first to review these interrelated prediction tasks uniformly, and they summarize methods, performance, and future directions.
- **Visible evidence base** The manuscript text includes descriptions of methods, tables referenced (Tables 1–5), one figure referenced (Figure 1), and citations to primary literature. No actual data tables or figures are provided in the submitted material.
- **Missing materials affecting confidence** Tables 1–5 and Figure 1 are referenced but not included. The manuscript lacks a dedicated methods section for the review itself (e.g., literature search strategy, inclusion criteria). No supplementary materials are provided. The full reference list is not available.

## Reviewer
- **Overall assessment** This manuscript provides a broad and organized overview of computational prediction methods for IDPs/IDRs, spanning disorder prediction, interaction prediction, and function prediction. The topic is timely and of interest to a growing community. However, the review is largely descriptive and lacks critical depth. Several claims are made without supporting evidence, and the absence of the referenced tables and figure prevents full evaluation. The manuscript would benefit from a more systematic approach, clearer criteria for method selection, and a more critical synthesis of the field's challenges and opportunities.
- **Who would be interested in the results, and why** Researchers in computational biology, bioinformatics, and structural biology, particularly those working on intrinsically disordered proteins, protein-protein interactions, and function annotation. The review could also serve as an entry point for newcomers to the field, and for experimentalists seeking to choose appropriate prediction tools.
- **Major strengths** The manuscript covers a wide range of prediction tasks in a unified framework, which is a useful organizational contribution. The authors correctly identify key challenges such as data quality, negative sample acquisition, and the need for quality assessment. The discussion of future directions, including multi-task learning and integration with structure prediction, is forward-looking and relevant.
- **Major Concerns** The review lacks critical depth and systematic methodology. Claims about "first" review are not substantiated. The performance comparisons are presented without sufficient context or statistical rigor. The manuscript does not clearly distinguish between well-established methods and speculative approaches. The absence of the referenced tables and figure is a significant gap.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide a reproducible or systematic review methodology. The performance data referenced in Tables 3 and 5 are not available for verification. The claim of being the "first" unified review is not supported by a literature search or comparison with existing reviews.
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The unified perspective is somewhat novel, but the individual topics have been reviewed extensively elsewhere.  
  *Scientific importance*: High. IDPs/IDRs are increasingly recognized as central to biology and disease, and computational prediction is a key enabling technology.  
  *Interdisciplinary readership*: Moderate. The topic is relevant to computational and experimental biologists, but the presentation is likely too specialized for a broad audience.  
  *Technical soundness*: Weak. The review lacks systematic methodology, and the performance comparisons are not rigorously presented or verifiable from the provided material.  
  *Readability for nonspecialists*: Moderate. The text is generally clear but assumes familiarity with machine learning and bioinformatics concepts.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript has potential but requires substantial revision, including a systematic methodology, inclusion of the referenced data, and a more critical synthesis.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to have "reviewed these prediction methods uniformly for the first time" and to have summarized their "computational methods and predictive performance."
- **Evidence pointer** Abstract; Section 1; Tables 3 and 5 (referenced but not provided)
- **Concern** The claim of being the "first" unified review is not substantiated by any systematic literature search or comparison with existing reviews. Furthermore, the performance comparisons referenced in Tables 3 and 5 are not available in the submitted material, making it impossible to verify the accuracy or fairness of the comparisons.
- **Why it matters** A review's value depends on its completeness and accuracy. An unsubstantiated novelty claim and unverifiable performance data undermine the manuscript's credibility and utility.
- **Resolution test** The authors should provide a systematic search strategy and inclusion criteria, and explicitly compare their scope with prior reviews. The referenced tables must be included, with clear descriptions of datasets, metrics, and statistical tests used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "most of these methods are based on machine learning, especially on deep learning" and that deep learning methods perform best, citing CAID results.
- **Evidence pointer** Section 2.1; Section 2.2; Table 3 (referenced but not provided)
- **Concern** The discussion of predictive performance is superficial. The authors do not discuss the variability of performance across datasets, the impact of different training/test splits, or the statistical significance of differences between methods. The claim that deep learning methods are superior is presented as a general statement without critical analysis of when and why this holds.
- **Why it matters** Performance claims in a review should be nuanced and evidence-based. Overgeneralized statements can mislead readers in their choice of methods.
- **Resolution test** The authors should provide a detailed analysis of performance, including per-dataset results, discussion of factors influencing performance, and appropriate statistical comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "the computational methods related to IDPs/IDRs have been developed vigorously" and that the field has reached "a relatively mature state."
- **Evidence pointer** Section 1; Section 2.3; Section 7
- **Concern** The claim of maturity is contradicted by the authors' own discussion of unresolved problems, such as poor performance on fully disordered proteins and the lack of quality assessment tools. The review does not critically assess whether the field is truly mature or whether fundamental challenges remain.
- **Why it matters** An accurate assessment of the field's state is crucial for guiding future research. Overstating maturity could discourage necessary methodological innovation.
- **Resolution test** The authors should reconcile their claims of maturity with the identified limitations, and provide a more balanced assessment of the field's progress and remaining challenges.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Readability for nonspecialists
- **Claim pointer** The manuscript aims to review methods for a broad audience, including those new to the field.
- **Evidence pointer** Throughout the manuscript
- **Concern** The manuscript assumes significant prior knowledge of machine learning and bioinformatics. Terms such as "PSSM," "HMM profile," "CNN," "LSTM," and "transfer learning" are used without adequate explanation. The description of methods is often at a high level without sufficient detail for a nonspecialist to understand the key differences and trade-offs.
- **Why it matters** A review should be accessible to its intended audience. If the audience includes nonspecialists, the manuscript needs to provide more background and clearer explanations.
- **Resolution test** The authors should either target a more specialized audience or add a glossary and more detailed explanations of key concepts and methods.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1.1
- **Evidence pointer** "IURed" appears to be a typo for "IUPred" in the text.
- **Issue** The text reads "IURed [51,52]" and later "IUPred [51,52]". This inconsistency is confusing.
- **Required correction** Correct the typo to "IUPred" throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.2.1
- **Evidence pointer** "As shown in Table 1, nine predictors used SVM" — this likely refers to a different table (probably Table 4, which summarizes binding site predictors).
- **Issue** The cross-reference appears to be incorrect.
- **Required correction** Verify and correct the table cross-reference.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 6
- **Evidence pointer** "In CASP15, there are many targets containing potentially disordered regions, such as target H1129 (as shown in Figure 1)."
- **Issue** The relevance of this example to the review's scope is not clearly explained. It is unclear what the figure shows and how it supports the authors' point.
- **Required correction** Provide a clear explanation of the figure and its relevance to the discussion.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.1.3
- **Evidence pointer** "RDN-binding" appears to be a typo for "RNA-binding".
- **Issue** The text reads "RDN-binding" which is likely a typographical error.
- **Required correction** Correct the typo to "RNA-binding".

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 5
- **Evidence pointer** The section discusses features but does not provide a clear summary or comparison of which features are most useful for which prediction tasks.
- **Issue** The section is descriptive but lacks synthesis. A table or figure summarizing key features and their utility would be helpful.
- **Required correction** Consider adding a summary table or figure to synthesize the information.

## Risk / unsupported claims
- The claim of being the "first" unified review of these prediction tasks is unsupported without a systematic literature search.
- Performance comparisons and rankings of methods (e.g., "top five methods", "best AUC") are unverifiable without the referenced tables and data.
- The statement that "the development of these predictors has reached a relatively mature state" is contradicted by the authors' own discussion of significant unresolved challenges.
- The claim that "deep learning technology... can extract complex relationships" and is the reason for good performance is an oversimplification and not critically examined.
- The assertion that "introducing the research of disordered proteins into the prediction of the three-dimensional structure of proteins is more worthy of expectation in the future" is speculative and not supported by concrete evidence or examples.