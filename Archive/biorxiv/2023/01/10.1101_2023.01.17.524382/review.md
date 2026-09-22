## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, conclusion, and supplementary data references
- **Assessment boundary** Scientific validity, methodological soundness, claims substantiation, and presentation quality of the described GraphGPSM model
- **Shared manuscript claim summary** The authors propose GraphGPSM, a global protein structure scoring model based on equivariant graph neural networks, which integrates geometric features, Rosetta energy terms, and residue-level topological descriptors. They claim superior correlation with TM-score over existing methods on CASP13, CASP14, and CAMEO benchmarks, improved modeling accuracy for orphan and multi-domain proteins, and competitive CASP15 performance.
- **Visible evidence base** Abstract, full methods section, results section with figures referenced, tables summarized in text, and supplementary data availability statements
- **Missing materials affecting confidence** Actual figures, tables, and supplementary data files are not provided; exact numerical values for many comparisons are absent; CASP15 official results are referenced but not reproduced; code and web server availability stated but not verified

## Reviewer
- **Overall assessment** The manuscript presents a technically plausible approach to global protein model quality assessment using an equivariant graph neural network architecture. The feature engineering is thoughtful, combining established physicochemical energy terms with geometric descriptors. However, the evidence as presented in the text is insufficient to fully substantiate the strong performance claims. Key quantitative results are described qualitatively, figures and tables are not available for inspection, and several methodological details require clarification. The work addresses an important problem in protein structure prediction, particularly for challenging cases like orphan and multi-domain proteins, but the current presentation does not allow independent verification of the central claims.

- **Who would be interested in the results, and why** Computational structural biologists, protein structure prediction researchers, and developers of model quality assessment methods would be the primary audience. The work is relevant to those working on refining AlphaFold2 predictions, developing scoring functions for protein modeling, and addressing the specific challenges of multi-domain and orphan protein structure prediction. The integration of geometric deep learning with classical energy functions may also interest researchers at the interface of machine learning and biophysics.

- **Major strengths** The problem addressed is timely and important, particularly the focus on global quality assessment beyond local lDDT metrics. The feature design is comprehensive, combining multiple complementary information sources. The application to orphan and multi-domain proteins addresses a known limitation of current prediction methods. The integration of the scoring model into a modeling pipeline demonstrates practical utility beyond pure ranking.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims GraphGPSM outperforms all comparison methods on CASP13, CASP14, and CAMEO test sets, with specific correlation improvements cited (e.g., 2.4% over ModFOLD7 on CASP13, 21% over ModFOLD8 on CASP14).
- **Evidence pointer** Section 3.1, Figure 2, Supplementary Tables S1-S3
- **Concern** The quantitative results are presented as summary statistics in the text, but the actual figures and supplementary tables are not available for inspection. The claimed improvements vary substantially across datasets (2.4% to 21%), and it is unclear whether these differences are statistically significant. The comparison methodology, including whether the same decoy sets were used for all methods and how correlation coefficients were computed, is not fully described.
- **Why it matters** The central claim of the manuscript is that GraphGPSM provides superior global scoring. Without access to the underlying data and a clear description of the comparison protocol, this claim cannot be independently verified. The large variation in improvement across datasets raises questions about consistency and generalizability.
- **Resolution test** Provide the actual figures and supplementary tables, include confidence intervals or statistical significance tests for correlation differences, and describe the exact comparison protocol including decoy set composition and correlation computation methodology.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological clarity
- **Claim pointer** The manuscript describes the EGNN architecture with message passing, but the equations referenced in Section 2.3 are not shown in the provided text.
- **Evidence pointer** Section 2.3, equations referenced but not displayed
- **Concern** The core methodological contribution is the EGNN architecture, yet the defining equations are missing from the provided manuscript text. The description of the message function, aggregation function, and update function is incomplete without these equations. Additionally, the relationship between the coordinate update mechanism and the claimed equivariance properties is not fully explained.
- **Why it matters** Reproducibility is a fundamental requirement for computational methods. Without the full architectural details, other researchers cannot implement or build upon the proposed approach. The equivariance properties are central to the method's claimed advantages and must be precisely defined.
- **Resolution test** Include the complete set of equations defining the EGNN layers, clarify the equivariance properties, and provide sufficient detail for independent reimplementation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** The manuscript claims GraphGPSM improves modeling accuracy for orphan proteins by 13.1% and multi-domain proteins by 7.1% over AlphaFold2 predictions, and that the average TM-score increases by 66.5% over Rosetta REF2015 on 484 test proteins.
- **Evidence pointer** Section 3.4, Tables 1 and 2, Figure 5, Supplementary Tables S6-S8
- **Concern** The modeling improvement claims are substantial, but the experimental setup is not fully described. The selection criteria for the 35 orphan and 57 multi-domain proteins are not detailed. The baseline comparison with AlphaFold2 uses AlphaFold2 predictions as initial structures, which is an unusual protocol that may bias results. The 66.5% average TM-score improvement over REF2015 alone seems remarkably high and requires careful scrutiny of the baseline protocol.
- **Why it matters** These are the most practically significant claims in the manuscript, suggesting the method can substantially improve upon state-of-the-art predictions. If the experimental protocol is flawed or the protein selection is biased, these conclusions would be misleading. The unusual use of AlphaFold2 predictions as starting points for refinement needs justification.
- **Resolution test** Describe the protein selection criteria in detail, justify the use of AlphaFold2 predictions as initial structures, provide the full distribution of TM-score changes rather than just averages, and clarify whether the 66.5% improvement is relative or absolute.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Benchmark completeness
- **Claim pointer** The manuscript states GraphGPSM achieved competitive performance in CASP15 global accuracy estimation and entered the top 10 global scoring servers.
- **Evidence pointer** Section 3.2, Table 6, Supplementary Table S4
- **Concern** The CASP15 results are presented as a single summary statement with limited comparative analysis. The specific ranking, the number of targets used for evaluation, and the comparison with other top-performing methods are not fully detailed. The relationship between the CASP15 implementation and the standalone GraphGPSM model described in this manuscript is unclear.
- **Why it matters** CASP15 provides an independent, blind test of the method's performance. A more detailed analysis would strengthen the manuscript's claims and provide context for the method's practical utility. The distinction between the CASP15 server implementation and the standalone model is important for reproducibility.
- **Resolution test** Provide the full CASP15 results including rankings, per-target performance, and a description of how the CASP15 implementation differs from the standalone GraphGPSM model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 2.2, feature description
- **Evidence pointer** Section 2.2
- **Issue** The description of the distance and direction encoding contains an apparent typo in the unit vector formula, where "C αi − C αi" appears twice instead of "C αi − C αj".
- **Required correction** Correct the formula to read "C αi − C αj / ║C αi − C αj ║ 2" and ensure the directionality is clearly defined.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3.1, comparison methods
- **Evidence pointer** Section 3.1
- **Issue** The text mentions VoroMQA-A in the methods list but later refers to VoroMQA-v2 as the second-ranked method on CAMEO. It is unclear whether these are the same method or different versions.
- **Required correction** Clarify the relationship between VoroMQA-A and VoroMQA-v2, and ensure consistent naming throughout the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.1, data preparation
- **Evidence pointer** Section 2.1
- **Issue** The manuscript states that approximately 150 models are generated per protein but does not describe the distribution of model qualities or how the decoy sets were validated for diversity and coverage of conformational space.
- **Required correction** Provide additional details on decoy set construction, including quality distribution and diversity metrics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2.4, training details
- **Evidence pointer** Section 2.4
- **Issue** The training procedure is described briefly, but details on hyperparameter selection, early stopping criteria, and the specific train/validation split are not provided.
- **Required correction** Include a complete description of training hyperparameters and model selection procedures.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Section 3.1, performance comparison
- **Evidence pointer** Section 3.1
- **Issue** The performance improvements are reported as percentage differences in correlation coefficients, but no statistical significance testing is described.
- **Required correction** Add statistical tests (e.g., bootstrap or permutation tests) to assess whether observed differences are significant.

## Risk / unsupported claims
- The claim that GraphGPSM outperforms all comparison methods on CASP13, CASP14, and CAMEO cannot be fully evaluated without access to the actual figures and supplementary tables
- The 66.5% average TM-score improvement over Rosetta REF2015 alone is not adequately supported by the described experimental protocol
- The CASP15 competitive performance claim is not substantiated with sufficient comparative data
- The claim that GraphGPSM can effectively refine AlphaFold2 predictions for orphan and multi-domain proteins requires more detailed analysis of the refinement protocol and potential biases
- The statement that GraphGPSM is "faster and more accurate" than existing end-to-end methods is not supported by any computational efficiency data
- The web server availability claim cannot be verified from the provided materials