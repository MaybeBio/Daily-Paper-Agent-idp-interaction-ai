## Review setup
- **Input scope** Full manuscript text including abstract, main text, figure legends, and supplementary material descriptions
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and presentation quality as presented in the supplied material
- **Shared manuscript claim summary** The authors review existing sequence-based computational tools for predicting phase-separating proteins, evaluate their performance on a curated human protein dataset, and propose that protein–protein interaction networks, post-translational modifications, and immunofluorescence images should be incorporated into future prediction tools to overcome the limitations of sequence-only approaches, particularly for proteins with low intrinsically disordered region content.
- **Visible evidence base** Main text, Tables 1–3, Figure 1 and Figure 2 legends, Figure 3 legend, Supplementary Figure S1 legend, and descriptions of Supplementary Tables S1–S6
- **Missing materials affecting confidence** Actual figures and tables are not visible; only legends are provided. Supplementary tables S1–S6 are referenced but their contents are not included. No methodological details for the performance evaluation are given beyond brief descriptions in the text.

## Reviewer
- **Overall assessment** This manuscript is a review article that also presents an original comparative analysis of six phase-separating protein prediction tools on a curated human protein dataset. The review component is informative and well-structured, covering the major sequence-based predictors and their underlying principles. The original analysis, while potentially useful, is presented with insufficient methodological detail to assess its validity. The proposal to incorporate PPI networks, PTMs, and IF images is reasonable and timely, but the supporting evidence provided is preliminary. The manuscript would benefit from a clearer separation between review content and original research, and from substantially more detail on the evaluation methodology.
- **Who would be interested in the results, and why** Researchers in the fields of phase separation, intrinsically disordered proteins, and computational biology would find this manuscript useful as a concise summary of available prediction tools. The comparative evaluation, if validated, would help users select appropriate tools. The proposal to integrate non-sequence features is likely to interest those developing next-generation prediction methods. The manuscript may also appeal to experimental biologists studying membraneless organelles who seek computational screening approaches.
- **Major strengths** The manuscript provides a clear and accessible overview of the biophysical basis of phase separation and the sequence features that correlate with it. The review of existing tools is organized logically, and the authors correctly identify a key limitation: most predictors are biased toward IDR-containing proteins. The inclusion of PPI networks, PTMs, and IF images as complementary features is a thoughtful and forward-looking perspective. The authors have made an effort to perform an original comparative analysis, which adds value beyond a purely descriptive review.
- **Major Concerns** The methodological details of the comparative analysis are severely underreported. The construction of the positive and negative sets, the scoring procedures, the handling of missing values, and the statistical tests are described only superficially. The claim that PTM frequency can discriminate phase-separating proteins is based on an analysis whose details are not fully provided. The proposal to use IF images is supported only by a reference to the authors' previous work, with no new evidence presented here. The manuscript does not clearly distinguish between established knowledge and the authors' new findings.
- **Minor Comments** The manuscript would benefit from a table summarizing the key features, input requirements, and output formats of each prediction tool. The discussion of PPI networks could be strengthened by mentioning specific databases beyond BioPlex. The authors should clarify whether the negative set is truly representative of non-phase-separating proteins, as this is a common source of bias. The figure legends are detailed but the figures themselves are not visible, making it impossible to assess the quality of the presented data.
- **Technical failings that need to be addressed before the case is established** The lack of methodological detail for the comparative evaluation is the primary technical failing. Specifically, the authors do not describe how the positive set was curated, how redundancy was handled, how scores from different tools were normalized, or how the ROC curves were computed when some tools do not provide scores for all proteins. The resampling procedure for the negative set is mentioned but not described in sufficient detail. The statistical comparison of PTM frequencies lacks information on effect sizes and confidence intervals.
- **Assessment against Nature-style criteria** Originality: The review component is not highly original, but the comparative analysis and the proposal to integrate non-sequence features offer a modest degree of novelty. Scientific importance: The topic is of significant current interest, and the identified limitation of existing tools is important. However, the manuscript does not provide a definitive solution, only a proposal. Interdisciplinary readership: The manuscript is likely to appeal to computational biologists, biochemists, and cell biologists, but the technical content is not deep enough to satisfy specialists in any one field. Technical soundness: The technical soundness cannot be fully assessed due to missing methodological details. Readability for nonspecialists: The manuscript is generally well-written and accessible, with clear explanations of key concepts.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant topic and offers a reasonable perspective, but the original analysis must be described in sufficient detail to allow evaluation and replication. The authors should also temper their claims about the utility of PTM frequency and IF images, as the evidence presented is preliminary.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** The authors claim to have performed a comparative evaluation of six phase-separating protein prediction tools on a curated human protein dataset, with results shown in Figure 2.
- **Evidence pointer** Section "Performance evaluation of phase separation predictors", Figure 2, Supplementary Tables S1–S3
- **Concern** The methodology for the comparative evaluation is described only in vague terms. The authors state that a positive set of 278 proteins was constructed from four databases and that the remaining human proteome was used as a negative set, but they do not describe how proteins were selected, how sequence redundancy was managed, how scores from different tools were obtained and normalized, or how the ROC curves were computed. The fact that some tools do not provide scores for all proteins is mentioned, but the handling of this issue is not explained. Without this information, the results in Figure 2 cannot be interpreted or reproduced.
- **Why it matters** The comparative evaluation is a central contribution of the manuscript. If the methodology is not transparent, the conclusions drawn from the comparison, such as the superior performance of certain tools, are not verifiable. This undermines the scientific value of the manuscript.
- **Resolution test** The authors should provide a detailed description of the evaluation methodology, including the exact criteria for inclusion in the positive and negative sets, the version and parameters of each prediction tool, the procedure for handling proteins for which a tool does not return a score, and the method for computing ROC curves and AUC values. Ideally, this information should be included in the main text or in a dedicated methods section.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors claim that PTM frequency can discriminate phase-separating proteins from non-phase-separating proteins, based on the analysis shown in Figure 3.
- **Evidence pointer** Section "PTMs", Figure 3, Supplementary Tables S4–S6
- **Concern** The analysis supporting the claim that PTM frequency is a useful discriminative feature is not described in sufficient detail. The authors state that PTM frequencies were calculated and compared between the positive and negative sets, and that a resampling procedure was used to control for IDR content, but the details of this procedure are not provided. The effect sizes are not reported, and it is unclear whether the observed differences are practically meaningful or merely statistically significant. The authors also acknowledge that the PTM database is biased toward well-studied proteins, which could confound the analysis.
- **Why it matters** The claim that PTM frequency is a useful feature for identifying phase-separating proteins is a key part of the authors' argument for incorporating non-sequence features into prediction tools. If this claim is not rigorously supported, the proposal loses much of its force.
- **Resolution test** The authors should provide a detailed description of the resampling procedure, report effect sizes and confidence intervals for the PTM frequency comparisons, and discuss the potential impact of database biases on their results. They should also consider performing a multivariate analysis that includes IDR content as a covariate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scope and framing
- **Claim pointer** The authors propose that PPI networks, PTMs, and IF images should be incorporated into future phase separation prediction tools.
- **Evidence pointer** Sections "PPI networks", "PTMs", "IF images", Conclusion and perspectives
- **Concern** The proposal to incorporate PPI networks, PTMs, and IF images is presented as a forward-looking perspective, but the authors do not provide a concrete framework for how these features would be integrated into a prediction tool. For PPI networks, the authors mention network embedding methods such as node2vec but do not discuss how the resulting vectors would be combined with sequence-based features. For IF images, the authors reference their previous work but do not describe the methodology or its limitations. The manuscript would be strengthened by a more concrete discussion of the practical challenges and potential solutions for integrating these heterogeneous data types.
- **Why it matters** The proposal is a major part of the manuscript's contribution. Without a more concrete discussion of implementation, the proposal remains at the level of a general suggestion rather than a actionable research direction.
- **Resolution test** The authors should provide a more detailed discussion of how PPI, PTM, and IF image features could be integrated with sequence-based features, including potential challenges such as data availability, feature representation, and model architecture. They could also discuss potential pitfalls and how these might be addressed.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Table 1 and Table 2
- **Evidence pointer** Table 1, Table 2
- **Issue** The tables listing IDR content analysis tools and phase separation analysis tools are described only by their titles in the text. No information is provided about the columns or the content of the tables.
- **Required correction** The authors should either include the tables in the manuscript or provide a description of their contents in the text, such as the tool names, URLs, and key features.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Performance evaluation of phase separation predictors"
- **Evidence pointer** Figure 2A
- **Issue** The authors state that the ROC curve for LARKS is shown as a point because it does not provide scores for each protein. This is confusing, as a ROC curve cannot be represented as a single point.
- **Required correction** The authors should clarify how the LARKS prediction was evaluated. If LARKS provides a binary classification (in the list or not), the authors should describe how sensitivity and specificity were calculated and how this was represented in the figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "IF images"
- **Evidence pointer** Section "IF images"
- **Issue** The authors mention that they previously built a CNN classifier to identify IF images with droplet-like structures, but they do not provide any details about this work, such as the training data, the architecture, or the performance.
- **Required correction** The authors should provide a brief description of their previous work, including the key results, or cite the relevant publication so that readers can access the details.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Language
- **Affected element** Section "PPI networks"
- **Evidence pointer** Section "PPI networks"
- **Issue** The phrase "with nephrin or N-WASP abscent" contains a typographical error ("abscent" should be "absent").
- **Required correction** The typo should be corrected.

## Risk / unsupported claims
- The claim that "all current phase separation prediction tools are developed based on sequence-dependent features" is supported by the review but may be an overstatement, as the authors do not provide an exhaustive survey of all available tools.
- The claim that "phase-separating proteins tend to have high PTM frequencies" is supported by the authors' analysis, but the analysis is not described in sufficient detail to assess its validity.
- The claim that "IF images with droplet-like structures could provide evidence that the labeled proteins aggregate in cells" is reasonable but is not supported by new evidence in this manuscript.
- The claim that "PPI networks can be useful in phase separation prediction" is plausible but is not supported by any new analysis in this manuscript.
- The performance comparison results shown in Figure 2 cannot be fully assessed because the methodology is not described in sufficient detail.
- The statement that "a more comprehensive approach that also considers PPI network information could be helpful" is presented as a suggestion rather than a tested hypothesis, which is appropriate for a review but should be clearly framed as such.