## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, footnotes)
- **Assessment boundary** Scientific and technical evaluation of the described software update, benchmarking claims, and application analyses; no evaluation of code functionality beyond what is described
- **Shared manuscript claim summary** The authors present metapredict V2, an updated deep-learning-based predictor of protein disorder that integrates predicted pLDDT scores from AlphaFold2 to improve accuracy over the legacy version, while maintaining practical speed. They report benchmarking against the DisProt-PDB dataset, application to human transcription factors, and assessment on non-natural proteins.
- **Visible evidence base** Figures 1-9 referenced in text; Supplemental Figure 1; methods descriptions; external datasets cited (DisProt, CAID, Lambert et al., Tretyachenko et al., Anishchenko et al.)
- **Missing materials affecting confidence** Figures themselves are not provided; exact numerical benchmarking results (e.g., MCC values, error bars, statistical tests) are not given; details of the CAID evaluation protocol are only referenced; the full list of 22 random peptide sequences and their classifications is not included; no comparison of metapredict V2 to other predictors beyond a single aggregate accuracy metric is shown

## Reviewer
- **Overall assessment** This manuscript describes a practical update to an existing bioinformatics tool, with a clear motivation and a reasonable technical approach. The integration of predicted pLDDT scores into a disorder predictor is a sensible idea given the known correlation between low pLDDT and disorder. The authors provide several application examples that demonstrate the utility of the tool. However, the manuscript is written as a technical note rather than a full research article, and the evidence presented is largely qualitative or summarized without full statistical detail. The claim that metapredict V2 is "the second most accurate disorder predictor" is stated without showing the full benchmarking comparison. The application to transcription factors is descriptive and lacks biological validation. The non-natural protein assessment is encouraging but based on a small number of examples. Overall, the work is likely useful to the community, but the evidence as presented is insufficient to fully establish all claims.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, particularly those who need fast and accurate disorder prediction for large-scale proteome analyses. The tool's speed and ease of use make it attractive for bioinformaticians and computational biologists. The transcription factor analysis may interest researchers studying transcriptional regulation. The assessment on non-natural proteins may interest synthetic biologists and protein engineers.

- **Major strengths** 1) Clear practical motivation and a well-described technical approach for improving disorder prediction. 2) The integration of AlphaFold2 pLDDT information is a timely and relevant idea. 3) The tool is made available through multiple interfaces (web server, Python package, command line), which increases its accessibility. 4) The authors address potential limitations of their approach, particularly regarding AlphaFold2's behavior on disordered regions. 5) The application to non-natural proteins is a thoughtful addition that goes beyond typical benchmarking.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "metapredict V2 was identified as the second most accurate disorder predictor, with the difference between metapredict V2 and the most accurate currently available predictor being just 0.281 residues per 100 predicted"
  - **Evidence pointer** Figure 9, location not provided
  - **Concern** The claim of being the second most accurate predictor is a strong quantitative statement, but the manuscript does not show the full benchmarking results, the list of 33 predictors compared, the statistical significance of the differences, or the variance across datasets. A single aggregate difference of 0.281 residues per 100 is presented without context on whether this is meaningful or within noise.
  - **Why it matters** This is a central claim about the tool's performance. Without the full comparison data, readers cannot assess whether the stated accuracy ranking is robust or whether it depends on specific dataset choices or evaluation protocols.
  - **Resolution test** Provide the full benchmarking table with all 33 predictors, per-protein or per-dataset accuracy measures, confidence intervals or statistical tests, and a description of the evaluation protocol. Show that the difference to the top predictor is not within the margin of error.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** "metapredict V2 correctly predicts this entire sequence to be disordered" (referring to HttEx1 Q40)
  - **Evidence pointer** Figure 6, location not provided
  - **Concern** The claim that metapredict V2 correctly predicts the Huntingtin exon 1 Q40 variant as fully disordered is based on a single example. The authors note that AlphaFold2 confidently predicts a helix in this region, but they do not provide quantitative comparison of disorder scores or show how robust this prediction is to sequence variations or to the choice of disorder threshold.
  - **Why it matters** This example is used to argue that metapredict V2 can correct for AlphaFold2's limitations on certain disordered regions. A single anecdotal example is insufficient to establish this as a general property of the tool.
  - **Resolution test** Provide additional examples of known disordered proteins where AlphaFold2 gives high pLDDT scores, and show that metapredict V2 consistently identifies them as disordered. Quantify the agreement with experimental annotations.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence sufficiency
  - **Claim pointer** "Human transcription factors are, on average, over 50% disordered"
  - **Evidence pointer** Figure 5B, C, location not provided
  - **Concern** The analysis of 1,608 human transcription factors is presented as a key application, but the manuscript does not provide details on the distribution of disorder across these proteins, the criteria for defining a transcription factor, or how the results compare to previous analyses of disorder in transcription factors. The claim that "on average" they are over 50% disordered is stated without showing the distribution or the variance.
  - **Why it matters** This is a potentially interesting biological observation, but without statistical context, it is difficult to assess its significance. It is also unclear whether this finding is novel or consistent with prior work.
  - **Resolution test** Show the distribution of disorder fractions across the 1,608 transcription factors, include confidence intervals, and compare to a control set of non-transcription-factor proteins. Discuss how this compares to previous estimates of disorder in transcription factors.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** "metapredict V2 correctly classified all but one of the sequences" (referring to the 22 random peptides from Tretyachenko et al.)
  - **Evidence pointer** Figure 8, location not provided
  - **Concern** The classification of the 22 random peptides as "disordered" or "ordered" is based on a 50% threshold of residues in IDRs. The authors do not specify how the experimental classification from Tretyachenko et al. was determined, whether it was based on circular dichroism spectra alone, and whether the threshold used by metapredict V2 is appropriate for these synthetic sequences. The single misclassified sequence is dismissed as potentially metastable, but this is speculative.
  - **Why it matters** This analysis is used to claim that metapredict V2 works well on non-natural proteins, which is an important extension of the tool's applicability. However, the small sample size and the lack of detail on the experimental reference standard limit the strength of this conclusion.
  - **Resolution test** Provide the full list of 22 sequences with their experimental classifications and metapredict V2 scores. Justify the 50% threshold. Discuss whether the misclassified sequence represents a systematic limitation or an outlier.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract, location not provided
  - **Issue** The abstract states that metapredict V2 has "substantially improved accuracy" but does not provide any quantitative measure of this improvement.
  - **Required correction** Include a specific accuracy metric (e.g., MCC improvement) in the abstract to support the claim.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, performance tests
  - **Evidence pointer** Methods, Performance tests, location not provided
  - **Issue** The performance test uses 500 randomly generated sequences of 500 amino acids. It is unclear whether these sequences are representative of real protein sequences, and the random generation method is not described.
  - **Required correction** Describe the random sequence generation method and consider using a benchmark set of real protein sequences for performance evaluation.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Results, non-natural proteins
  - **Evidence pointer** Results, Assessment against non-natural proteins, location not provided
  - **Issue** The analysis of de novo synthetic proteins uses only three examples. This is a very small sample size for drawing conclusions about the tool's performance on such sequences.
  - **Required correction** Acknowledge the limited sample size and suggest that a larger set of de novo proteins would strengthen the conclusion.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, location not provided
  - **Issue** The discussion mentions that metapredict V2 is "among the fastest disorder predictors currently available" but does not provide a quantitative comparison of speed with other tools.
  - **Required correction** Provide a speed comparison table or at least a reference to a benchmark study that includes metapredict V2.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods, human transcription factor analysis
  - **Evidence pointer** Methods, Human transcription factor analysis, location not provided
  - **Issue** The manuscript states that code and data are available on GitHub, but the specific version of the code used for the analyses is not indicated.
  - **Required correction** Specify the version of metapredict V2 and the commit hash or release tag used for the analyses.

- **Technical failings that need to be addressed before the case is established** The central benchmarking claim (R1-M1) needs to be supported with full data. The single-example demonstration of correcting AlphaFold2 limitations (R1-M2) needs to be expanded. The transcription factor analysis (R1-M3) needs statistical context. The random peptide classification (R1-M4) needs more detail on the reference standard.

## Risk / unsupported claims
- The claim that metapredict V2 is the "second most accurate disorder predictor" is not supported by the data shown in the manuscript.
- The claim that metapredict V2 "correctly predicts" the HttEx1 Q40 as disordered is based on a single example and is not generalizable.
- The statement that "all but one" of the 22 random peptides were correctly classified is not fully verifiable without the full dataset and classification criteria.
- The claim that human transcription factors are "on average, over 50% disordered" is presented without statistical analysis or comparison to prior work.
- The statement that metapredict V2 is "among the fastest" predictors is not quantified.
- The claim that the hybrid approach "resulted in a substantial increase in accuracy" is not quantified in the text.