## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, conclusion, and figure legends, as provided.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and alignment with Nature-style criteria, based solely on the supplied material.
- **Shared manuscript claim summary** The authors propose that monomeric and tetrameric alpha-synuclein share sequence, disorder, and aggregation propensity similarities with 14-3-3 sigma, particularly in the NAC region and C-terminal tail, suggesting structural and functional homology that supports a chaperone role for alpha-synuclein and physiological relevance of its tetrameric state.
- **Visible evidence base** BLAST sequence alignments, PONDR disorder predictions, PASTA 2.0 and AMYLPRED2 aggregation predictions, PyMOL structural analysis of 14-3-3 and alpha-synuclein tetramer coordinates, STRING interaction network analysis, and PHYLIP phylogenetic tree.
- **Missing materials affecting confidence** Supplementary data files (e.g., Supplemental Figures S1.2, S2.1, S2.2, S4.1, S4.2, Table S1.1, and supplementary discussion) are referenced but not provided, limiting verification of detailed results. Raw sequence accession numbers for all proteins are not explicitly listed. Statistical significance testing for alignment and prediction comparisons is absent.

## Reviewer
- **Overall assessment** This manuscript presents a computational analysis exploring sequence and structural similarities between alpha-synuclein and 14-3-3 proteins, with a focus on the sigma isoform. The work builds on prior findings from 1999 and extends them using modern bioinformatics tools. The topic is of interest to the neurodegeneration community, and the hypothesis that alpha-synuclein shares chaperone-like features with 14-3-3 is plausible. However, the evidence provided is largely descriptive and correlative, with no experimental validation or robust statistical framework. Several claims, particularly regarding functional implications and tetramer relevance, are overstated relative to the computational nature of the data. The manuscript would benefit from clearer methodological details, inclusion of supplementary data in the main text, and a more cautious interpretation of results.
- **Who would be interested in the results, and why** Researchers studying alpha-synuclein biology, Parkinson's disease pathogenesis, protein misfolding and aggregation, chaperone functions, and intrinsically disordered proteins. The potential link between alpha-synuclein and 14-3-3 chaperone activity may interest those exploring therapeutic targets for synucleinopathies, though the computational nature limits immediate translational appeal.
- **Major strengths** The study addresses a relevant and under-explored question regarding alpha-synuclein's normal function and its similarity to chaperone proteins. The use of multiple complementary computational tools (sequence alignment, disorder prediction, aggregation prediction, structural analysis, interaction networks) provides a broad approach. The focus on isoform-specific differences, particularly highlighting 14-3-3 sigma, adds nuance. The inclusion of a phylogenetic tree is a nice touch for evolutionary context.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** Lack of experimental validation for predicted similarities; absence of statistical significance testing; incomplete presentation of supplementary data; overinterpretation of correlative computational results; potential bias in sequence alignment interpretation due to hidden gaps.
- **Assessment against Nature-style criteria** Originality: Moderate. The 1999 study already identified homology, and this work extends it, but the novelty is incremental. Scientific importance: Moderate. Understanding alpha-synuclein's normal function is important, but the computational evidence does not yet establish a definitive link. Interdisciplinary readership: Limited. The work is primarily bioinformatics-focused and may not attract a broad audience beyond computational biologists and neurodegeneration specialists. Technical soundness: Adequate but not rigorous. Methods are standard, but validation and statistical support are lacking. Readability for nonspecialists: Acceptable. The text is generally clear, though some sections are dense and would benefit from simplification.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting hypothesis but lacks the experimental or statistical rigor to support its stronger claims. Revisions and additional validation would be needed to make a compelling case.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim validity
- **Claim pointer** The authors claim that "the sequence homology results inform the structural analysis of alpha-synuclein's ordered states" and that similarities in disorder and aggregation predictions "support the physiological relevance of the tetrameric alpha-synuclein."
- **Evidence pointer** Results sections "Sequence alignment within the N-terminus and C-terminus" and "Predicted disorder within the BLAST sequence alignments"; Figures 1, 2, and 4.
- **Concern** The central claim of structural and functional homology between alpha-synuclein and 14-3-3 sigma is based solely on computational predictions. No experimental data (e.g., binding assays, mutagenesis, or functional studies) are provided to validate that the identified sequence similarities translate to actual structural or functional relevance. The leap from sequence alignment to physiological claims about tetramer stability and chaperone function is not justified by the evidence presented.
- **Why it matters** Without experimental validation, the conclusions remain speculative. The manuscript's title and discussion imply a stronger relationship than the data can support, which could mislead readers and overstate the significance of the findings.
- **Resolution test** Provide experimental evidence, such as co-immunoprecipitation or binding studies showing alpha-synuclein-14-3-3 interaction, or mutagenesis of key residues to test functional impact. Alternatively, temper the claims to clearly state that these are predictions requiring validation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the agreement between the probabilities reported by both programs (PASTA 2.0 and AMYLPRED2) serves to increase the confidence of the predicted amyloid-prone regions."
- **Evidence pointer** Methods section "PASTA 2.0 aggregation predictions" and "AMYLPRED2 aggregation predictions"; Figure 2b.
- **Concern** The manuscript lacks any statistical analysis to support the claimed agreement between prediction methods. Visual overlap in plots is not a quantitative measure of significance. Additionally, the thresholds for significance in BLAST alignments are not clearly defined, and the authors note that bit scores are below the common threshold of 50, yet they proceed with interpretation based on internal comparison. This undermines the robustness of the sequence alignment claims.
- **Why it matters** The validity of the core findings depends on the reliability of the computational predictions. Without statistical support, the reader cannot assess whether the observed similarities are meaningful or due to chance.
- **Resolution test** Include statistical tests (e.g., permutation tests, confidence intervals) to quantify the significance of overlaps between prediction methods and sequence alignments. Clearly justify the use of sub-threshold bit scores and provide a rationale for internal comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The authors reference multiple supplementary figures and tables (e.g., Supplemental Figures S1.2, S2.1, S2.2, S4.1, S4.2, Table S1.1) that are essential for understanding the results.
- **Evidence pointer** Methods and Results sections; figure legends.
- **Concern** The supplementary data are not provided in the manuscript, making it impossible to verify key details, such as the complete BLAST alignment output, detailed disorder predictions for all isoforms, and contact distance tables. This significantly limits the reproducibility and transparency of the work.
- **Why it matters** Nature-style criteria require that all data supporting the claims be accessible to reviewers and readers. Without the supplementary material, the manuscript is incomplete and cannot be fully evaluated.
- **Resolution test** Provide the supplementary data as part of the submission, or integrate the essential results into the main text and figures.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The authors conclude that "our results support alpha-synuclein function as a chaperone protein" and that the NAC region and C-terminal tail are "fundamental to the chaperone function."
- **Evidence pointer** Discussion section; Figure 1.
- **Concern** The link between sequence similarity to 14-3-3 and chaperone function is not established. 14-3-3 proteins have well-characterized chaperone activity, but alpha-synuclein's chaperone function is only indirectly supported by prior literature. The authors do not provide direct evidence that the identified regions confer chaperone activity, and the discussion overreaches by implying a causal relationship.
- **Why it matters** Overstated conclusions can lead to misinterpretation of alpha-synuclein's role in health and disease, potentially influencing future research directions inappropriately.
- **Resolution test** Soften the language to indicate that the findings are suggestive and require functional testing. Alternatively, include experimental data demonstrating chaperone activity linked to the identified regions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section "BLAST sequence alignment"
- **Evidence pointer** Methods section, first paragraph.
- **Issue** The description of the BLAST methodology is brief and lacks specific parameters (e.g., scoring matrix, gap penalties, E-value thresholds). This limits reproducibility.
- **Required correction** Provide detailed parameters used for BLAST searches, including the version and any non-default settings.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 legend.
- **Issue** The figure legend is dense and difficult to follow, with multiple colors and annotations that are not fully explained in the text.
- **Required correction** Simplify the legend and ensure all color codes and symbols are clearly defined, either in the legend or in the main text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Language
- **Affected element** Discussion section, first paragraph.
- **Evidence pointer** Discussion section, first paragraph.
- **Issue** The phrase "this appraoch" contains a typographical error ("appraoch" should be "approach").
- **Required correction** Correct the typo and proofread the manuscript for similar errors.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section "STRING interactions predictions"
- **Evidence pointer** Methods section, "STRING interactions predictions" paragraph.
- **Issue** The methods for STRING analysis are described, but the criteria for selecting the 27 common interactions are not fully explained, and the confidence score threshold of 0.4 is mentioned but not justified.
- **Required correction** Clarify the selection criteria and provide a rationale for the chosen confidence threshold.

## Risk / unsupported claims
- The claim that alpha-synuclein and 14-3-3 sigma are homologs with functional significance is unsupported without experimental validation.
- The assertion that the tetrameric alpha-synuclein is physiologically relevant based on computational similarity to 14-3-3 is not established.
- The conclusion that the NAC region and C-terminal tail are "fundamental" to chaperone function is speculative and not directly tested.
- The use of sub-threshold BLAST bit scores for interpretation is not adequately justified, and the significance of alignments is not statistically supported.
- The agreement between PASTA 2.0 and AMYLPRED2 predictions is claimed but not quantitatively demonstrated.