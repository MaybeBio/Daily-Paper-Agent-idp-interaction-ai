## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methodology, results, discussion, conclusion, funding, acknowledgements, footnotes)
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency as presented in the provided text
- **Shared manuscript claim summary** The authors benchmark AlphaFold2's pLDDT score against traditional sequence-based disorder predictors using CAID-derived datasets, finding that pLDDT outperforms a naive DSSP-based approach for disorder prediction, that conventional predictors can outperform pLDDT on the DisProt dataset, and that pLDDT distributions relate to secondary structure in ways that may inform IDP dynamics.
- **Visible evidence base** Abstract, Introduction, Methodology (dataset generation), Results (three subsections), Discussion, Conclusion, Funding, Acknowledgements, Footnotes. Figures and tables are referenced but not provided.
- **Missing materials affecting confidence** All figures (Figs. 1–4, S1–S11), all tables (Tables S1–S4), Supplementary Information, the GitHub repository data, and the CAID benchmark details are referenced but not available for inspection. Statistical analysis code and parameter choices are not described in sufficient detail.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and relevant question: whether AlphaFold2's pLDDT score can serve as a reliable predictor of protein disorder. The authors identify a genuine methodological pitfall (naive DSSP-based disorder assignment) and propose pLDDT as a more rigorous alternative. The core comparison against CAID benchmark datasets is appropriate and the inclusion of 11 established predictors provides a reasonable baseline. However, the manuscript as presented has several critical weaknesses. The methodology section is incomplete, lacking any description of statistical tests, threshold selection procedures, or handling of dataset imbalances. The results section references numerous figures and tables that are not provided, making the evidence base impossible to verify. The claim that pLDDT "may reveal a fundamental connection to the dynamics of disordered proteins" is speculative and not supported by the data presented. The manuscript also contains typographical errors ("näaive" appears twice) and an unresolved footnote about a PAE/pLDDT terminology error that suggests the manuscript has undergone revision but may still contain inconsistencies. The central finding, that pLDDT outperforms naive DSSP use, is plausible but the magnitude and robustness of this effect cannot be assessed from the provided material. The comparison between pLDDT and sequence-based predictors on the DisProt dataset, where pLDDT underperforms, is an important caveat that is appropriately acknowledged but not deeply explored. Overall, the manuscript presents an interesting observation but the current evidence base is insufficient to fully establish the claims.

- **Who would be interested in the results, and why** Computational structural biologists, researchers working on intrinsically disordered proteins, developers of disorder prediction tools, and the broader AlphaFold user community. The manuscript addresses a practical question of how to interpret AlphaFold2 outputs for disordered regions, which is directly relevant to the many researchers now using AlphaFold2 as a standard tool. The potential link between pLDDT and IDP dynamics, if substantiated, would be of interest to biophysicists studying conformational ensembles.

- **Major strengths** The manuscript addresses a timely and practical question with clear relevance to the structural biology community. The use of established CAID benchmark datasets provides a solid foundation for comparison. The identification of the naive DSSP pitfall is a useful practical warning. The inclusion of multiple traditional predictors as baselines is appropriate. The authors are appropriately cautious in some of their claims, particularly regarding the speculative link to IDP dynamics.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that pLDDT-based predictors outperform naive DSSP-based disorder assignment, supported by ROC curves, AUC values, precision-recall curves, Fmax values, and RMSD calculations.
- **Evidence pointer** Figures 1, 2, S1–S3; Tables S1–S4; location not provided for specific data points
- **Concern** The results section references numerous figures and tables that are not included in the provided material. Without access to these figures and tables, the core quantitative claims cannot be verified. The ROC curves, AUC values, precision-recall curves, Fmax values, and RMSD calculations are all presented as evidence, but the actual data is unavailable. Additionally, the methodology section does not describe how statistical significance was assessed, how threshold values were optimized, or how the datasets were balanced. The claim that pLD 72 outperforms DSSP is plausible but the magnitude of the effect and its statistical robustness cannot be evaluated.
- **Why it matters** The central claim of the manuscript rests entirely on quantitative comparisons that are not visible in the provided material. Without the figures and tables, the reader cannot assess whether the observed differences are meaningful or within noise. The lack of statistical methodology also prevents assessment of whether the reported differences are significant.
- **Resolution test** Provide all referenced figures and tables with clear axis labels, legends, and error bars. Describe the statistical tests used to compare methods, including how significance was determined. Report confidence intervals or effect sizes for the key comparisons.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "conventional predictors can outperform the pLDDT in disorder identification" on the DisProt dataset, with fIDPnn specifically outperforming all other predictors.
- **Evidence pointer** Results section, "Sequence predictors can still outperform AlphaFold2 on disorder prediction"; Figures 1 and S1; Tables S1 and S3; location not provided
- **Concern** The manuscript reports that on the DisProt dataset, pLDDT-based predictors perform significantly worse than several sequence-based predictors, with fIDPnn outperforming all others. However, the explanation for this discrepancy is not developed. The authors note that the DisProt dataset contains "uncertain" residues while DisProt-PDB does not, but they do not explain how this difference leads to the observed performance gap. The discussion of this finding is brief and does not explore whether the pLDDT is systematically biased in certain sequence contexts or whether the threshold selection procedure is suboptimal for the DisProt dataset.
- **Why it matters** This result is a significant caveat to the main claim that pLDDT is a useful disorder predictor. If pLDDT performs poorly on a standard benchmark dataset, its practical utility is limited. The manuscript should provide a more thorough analysis of why this discrepancy occurs and whether it can be mitigated.
- **Resolution test** Provide a detailed analysis of the performance gap on the DisProt dataset, including examination of error patterns, sequence features associated with pLDDT failures, and discussion of whether alternative threshold selection or post-processing could improve performance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that the relationship between pLDDT and secondary structure "hints at a broader application of the pLDDT to IDP dynamics" and that pLDDT "may reveal a fundamental connection to the dynamics of disordered proteins."
- **Evidence pointer** Abstract; Results section, "Secondary structure codons (SSC) reveal relationships between the pLDDT and secondary structure"; Discussion section; location not provided
- **Concern** The claim that pLDDT may be useful for studying IDP dynamics is presented as a significant implication of the work, but no direct evidence is provided to support this connection. The observation that pLDDT values vary across secondary structure types is descriptive and does not establish a link to dynamics. The authors speculate that low pLDDT helices may be "more transient" and high pLDDT coils may suggest "a disorder-order transition," but these are hypotheses without supporting data. The manuscript would benefit from either tempering this claim or providing preliminary evidence, such as comparison with experimental dynamics data or molecular simulations.
- **Why it matters** The potential link to IDP dynamics is presented as a key motivation for the work and a direction for future research. If this claim is overstated, it may mislead readers about the current capabilities of pLDDT. Conversely, if there is preliminary evidence, it should be presented to strengthen the case.
- **Resolution test** Either temper the language to clearly label this as speculation, or provide preliminary evidence such as correlation between pLDDT and experimental order parameters, comparison with simulation-derived dynamics metrics, or analysis of known dynamic regions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors introduce the concept of "secondary structure codons (SSC)" as a triplet describing local secondary structure at a given residue, and use this to analyze pLDDT distributions.
- **Evidence pointer** Results section, "Secondary structure codons (SSC) reveal relationships between the pLDDT and secondary structure"; Figures S8–S11; location not provided
- **Concern** The SSC concept is introduced but not clearly defined. The manuscript does not explain how the triplet is constructed (e.g., which residues are included, how the secondary structure assignments are encoded, whether the triplet is centered on the residue of interest). The analysis of pLDDT distributions for each SSC is described qualitatively, but no quantitative measures are provided. The relationship between SSC and the observed performance differences between pLDDT and DSSP is asserted but not demonstrated.
- **Why it matters** The SSC analysis is presented as a key contribution that explains the observed performance differences. Without a clear definition and quantitative analysis, this contribution cannot be evaluated or built upon by other researchers.
- **Resolution test** Provide a precise definition of SSC construction, including the encoding scheme and window size. Present quantitative summaries of pLDDT distributions for each SSC, such as means, standard deviations, and measures of bimodality. Demonstrate how SSC analysis explains the performance differences between pLDDT and DSSP.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, first sentence; Introduction, first paragraph
- **Issue** The manuscript contains typographical errors, including "näaive" (should be "naive") appearing twice in the abstract and once in the results section. The abstract also contains a double space in "provided a a paradigm-shift."
- **Required correction** Correct all typographical errors throughout the manuscript.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, dataset generation
- **Evidence pointer** Methodology section, "Dataset generation" paragraph
- **Issue** The manuscript states that the datasets are "composed of 475 targets" but does not explain why this is fewer than the 646 targets used at CAID beyond stating that "AlphaFold2 predicted structures do not exist for some sequences." The criteria for excluding targets are not described.
- **Required correction** Provide a clear description of the exclusion criteria and the number of targets excluded for each reason.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, dataset generation
- **Evidence pointer** Methodology section, "Dataset generation" paragraph
- **Issue** The manuscript states that "All residues not covered by either DisProt annotation or PDB structures are masked and were excluded from analysis" for the DisProt-PDB dataset, but does not describe how the PDB structures were selected or matched to the DisProt entries.
- **Required correction** Describe the procedure for matching PDB structures to DisProt entries, including any sequence identity thresholds or structural quality filters.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, dataset generation
- **Evidence pointer** Methodology section, "Dataset generation" paragraph
- **Issue** The manuscript states that "Thresholds for n were chosen based on the Matthews correlation coefficent (MCC)" but does not describe the optimization procedure, such as whether thresholds were optimized on a training set or on the full dataset.
- **Required correction** Describe the threshold optimization procedure, including whether thresholds were selected on the same data used for evaluation and whether this introduces optimism bias.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methodology, dataset generation
- **Evidence pointer** Methodology section, "Dataset generation" paragraph
- **Issue** The manuscript states that "For two vectors v and w we compute the RMSD as where m is the number of elements" but the equation is missing from the text.
- **Required correction** Include the RMSD equation in the text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section, "pLDDT performs better than naive use of DSSP for disorder prediction"
- **Evidence pointer** Results section, first subsection
- **Issue** The sentence "This is all to say that a naive application of DSSP for the prediction of disordered and ordered regions for AlphaFold2 structures, specifically the assumption that helical and strand regions are ordered and coiled regions are unstructured, leads to poorer prediction (i.e., higher RMSD, lower AUC and higher F max ) of disordered regions and an overestimation in disorder content" is overly long and contains a logical inconsistency. Higher Fmax indicates better performance, not poorer, so listing it alongside higher RMSD and lower AUC as evidence of poorer performance is confusing.
- **Required correction** Revise the sentence to clearly state that DSSP leads to higher RMSD, lower AUC, and lower Fmax, and clarify the direction of each metric.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section, "Sequence predictors can still outperform AlphaFold2 on disorder prediction"
- **Evidence pointer** Results section, second subsection
- **Issue** The manuscript reports that "tpLD performed exceptionally well on the DisProt-PDB dataset posting the largest Fmax (0.784) and one of the largest AUC (0.905) values of the methods considered" but does not specify which method achieved the largest AUC or how many methods were compared.
- **Required correction** Specify the number of methods compared and identify which method achieved the largest AUC.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion section
- **Evidence pointer** Discussion section, first paragraph
- **Issue** The sentence "While it is the case that a single, static, AlphaFold2 structure cannot adequately describe these often large conformational ensembles, the ability of the program to predict with relatively high accuracy the location of disordered regions is nonetheless impressive" is grammatically awkward and could be simplified.
- **Required correction** Revise for clarity and conciseness.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Footnotes
- **Evidence pointer** Footnotes section
- **Issue** The footnote states that "There was a typo that propagated through the manuscript regarding Predicted Aligned Error (PAE) and predicted Local Distance Difference Test (pLDDT)." This suggests a previous version of the manuscript contained an error that has been corrected, but the current text does not indicate where this error occurred or whether all instances have been corrected.
- **Required correction** Clarify the nature of the typo and confirm that all instances have been corrected in the current version.

- **Technical failings that need to be addressed before the case is established** The manuscript cannot be fully evaluated without access to the referenced figures, tables, and supplementary information. The methodology section is incomplete, lacking descriptions of statistical tests, threshold optimization, and dataset construction details. The RMSD equation is missing from the text. The relationship between SSC analysis and the observed performance differences is asserted but not demonstrated. The claim regarding pLDDT and IDP dynamics is speculative and not supported by the presented data.

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of AlphaFold2 to disorder prediction is a natural extension of existing work, and the identification of the naive DSSP pitfall is useful but not conceptually novel. The SSC concept is new but its utility is not clearly established.
  - Scientific importance: Moderate. The question of whether AlphaFold2 can predict disorder is practically important given the widespread adoption of the tool, but the manuscript does not provide a definitive answer due to the incomplete evidence base.
  - Interdisciplinary readership: Limited. The manuscript is primarily of interest to computational structural biologists and IDP researchers. The potential link to IDP dynamics could broaden the appeal, but this is not developed.
  - Technical soundness: Not established. The missing figures, tables, and methodology details prevent assessment of the technical quality of the analysis.
  - Readability for nonspecialists: The manuscript is generally readable but contains some awkward phrasing and undefined terms (e.g., SSC). The abstract is clear but the results section relies heavily on references to unavailable figures.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant question and identifies a genuine methodological issue, but the evidence base is incomplete. The authors must provide all referenced figures, tables, and supplementary information, complete the methodology section, and either temper or support the claims regarding IDP dynamics before the case can be properly evaluated.

## Risk / unsupported claims
- The claim that pLDDT "may reveal a fundamental connection to the dynamics of disordered proteins" is speculative and not supported by the presented data.
- The claim that SSC analysis "may explain our observations" is asserted but not demonstrated with quantitative evidence.
- The claim that pLD 72 outperforms DSSP on both datasets is plausible but cannot be verified without the referenced figures and tables.
- The claim that "conventional predictors can outperform the pLDDT in disorder identification" on the DisProt dataset is reported but not analyzed in sufficient depth.
- The statement that "AlphaFold2 supplies both a pLDDT score, that can provide an accurate prediction of protein disorderedness" is an overstatement given the reported underperformance on the DisProt dataset.
- The footnote regarding the PAE/pLDDT typo suggests potential inconsistencies in the manuscript that are not fully resolved.