## Review setup
- **Input scope** Full manuscript text (main text, methods summary, figure legends referenced but not provided in full)
- **Assessment boundary** Scientific claims, methodology, evidence quality, and interpretation as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that AlphaFold2 (AF2) structures in the AlphaFold Database (AFDB) can identify conditionally folded intrinsically disordered regions (IDRs), that high pLDDT scores in predicted IDRs correspond to conditionally folded states, that this phenomenon is widespread across the tree of life, and that AF2 predictions can rationalize disease-causing mutations in IDRs
- **Visible evidence base** Main text figures referenced (Figs 1–6), SI Appendix figures and tables referenced (Figs S1–S13, Tables S1–S5), methods summary for SPOT-Disorder analysis, GitHub code repository
- **Missing materials affecting confidence** Full figure panels and legends, SI Appendix content, detailed methods for AFDB parsing, docking calculations, and statistical tests; NMR experimental details; complete lists of databases and filtering criteria

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question: whether AlphaFold2 predictions can be meaningfully interpreted for intrinsically disordered regions, which constitute a large fraction of many proteomes and are poorly represented in training data. The authors present a systematic analysis of pLDDT scores in predicted IDRs, provide evidence that high-confidence AF2 structures of IDRs resemble conditionally folded states, and extend this to a proteome-wide survey and disease variant analysis. The work is conceptually interesting and the central observation, that AF2 assigns high confidence to some IDRs that fold under specific conditions, is likely correct and useful. However, the manuscript has several significant weaknesses. The validation against experimental data is limited to a small number of examples, the classification analysis relies on databases with inherent biases that are acknowledged but not fully addressed, the proteome-wide extrapolation depends on a single disorder predictor, and the disease variant analysis is largely correlative. The claim that AF2 has "learned" to identify conditionally folded IDRs is not fully established from the evidence presented, as alternative explanations (e.g., sequence composition effects on pLDDT) are not rigorously excluded. The manuscript would benefit from additional experimental validation, more careful control analyses, and tempering of some conclusions.

- **Who would be interested in the results, and why** Structural biologists, computational biologists, and researchers studying intrinsically disordered proteins will find this work of interest. The manuscript addresses a practical question: how should AF2 predictions be interpreted for IDRs, which are increasingly recognized as functionally important. The finding that high pLDDT scores in IDRs may indicate conditional folding has implications for the use of AF2 in structural genomics, variant interpretation, and drug discovery. The proteome-wide survey across archaea, bacteria, and eukaryotes provides a useful resource. Researchers working on protein-protein interactions, post-translational modification-dependent folding, and disease variant interpretation will also find relevant content.

- **Major strengths** The manuscript addresses an important and underappreciated problem: the interpretation of AF2 predictions for IDRs. The observation that a substantial fraction of predicted IDRs have high pLDDT scores, and that these may correspond to conditionally folded states, is novel and potentially impactful. The use of multiple complementary approaches (pLDDT distribution analysis, comparison with experimental structures, classification analysis, proteome-wide survey, disease variant analysis) provides a broad perspective. The specific example of 4E-BP2, where AF2 combines structural features from two different conditionally folded states, is particularly instructive and highlights both the power and limitations of AF2 for IDRs. The authors are appropriately cautious in some interpretations, such as acknowledging the empirical nature of the proteome-wide estimates.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for central claim
- **Claim pointer** The manuscript claims that "AlphaFold2 can readily identify structures for a subset of IDRs that fold under certain conditions (conditional folding)" and that high pLDDT scores in predicted IDRs correspond to conditionally folded states
- **Evidence pointer** Figures 1–3, Section "Comparing NMR Data and AlphaFold2 Structures for Experimentally Characterized IDRs"
- **Concern** The central claim that high pLDDT scores in IDRs correspond to conditionally folded states is supported by only three detailed experimental examples (α-synuclein, 4E-BP2, ACTR) plus a small set of additional comparisons referenced in the SI. While these examples are informative, they represent a very small sample size given the claim's generality. The manuscript does not provide a systematic, quantitative comparison between AF2 predictions and experimental data across a larger set of conditionally folded IDRs. The classification analysis (Fig 5A) uses databases of conditionally folded IDRs, but the authors do not report the false positive rate for their approach on a rigorously curated negative set. The possibility that high pLDDT scores in some IDRs reflect stable tertiary structure that is not conditionally folded (i.e., mis-annotated ordered domains) is discussed but not rigorously excluded with quantitative controls.
- **Why it matters** The manuscript's central contribution is the claim that AF2 can identify conditionally folded IDRs. If this claim is not supported by sufficient evidence, the manuscript's main conclusion is not established. The small number of validation examples and the acknowledged biases in the databases used for classification analysis leave open the possibility that the observed enrichment of high pLDDT scores in conditionally folded IDRs is partially or wholly explained by other factors.
- **Resolution test** The authors should provide a larger, systematically curated set of conditionally folded IDRs with experimental validation (e.g., from NMR or crystallography) and demonstrate that their pLDDT-based approach identifies these with high sensitivity and specificity against a matched control set of IDRs that do not conditionally fold. Alternatively, they should provide quantitative evidence that the observed enrichment of high pLDDT scores in conditionally folded IDRs cannot be explained by sequence composition, MSA depth, or other confounding factors.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of proteome-wide extrapolation
- **Claim pointer** The manuscript claims that "we leverage AlphaFold2's predictions of conditionally folded IDRs to quantify the extent of conditional folding across the tree of life" and reports percentages of conditionally folded IDRs in various organisms (Fig 5D–E)
- **Evidence pointer** Figure 5D–E, Section "AlphaFold2-Enabled Identification of Conditionally Folding IDRs in Other Organisms"
- **Concern** The proteome-wide analysis across 23 organisms relies on IUPred2A for disorder prediction, while the human proteome analysis uses SPOT-Disorder. The authors acknowledge that IUPred2A underestimates disorder extent but do not provide a systematic comparison of how this difference affects the identification of conditionally folded IDRs. The threshold for "high confidence" pLDDT (≥70) is applied uniformly across all organisms, but it is unclear whether this threshold is appropriate across diverse proteomes with different amino acid compositions and evolutionary histories. The authors report an "upper bound" estimate of conditionally folded IDRs but do not provide confidence intervals or sensitivity analyses for their estimates.
- **Why it matters** The proteome-wide survey is a major component of the manuscript's contribution. If the estimates of conditionally folded IDRs across organisms are not robust to the choice of disorder predictor, pLDDT threshold, or other analysis parameters, the conclusions about evolutionary patterns may not be reliable.
- **Resolution test** The authors should provide a sensitivity analysis showing how the estimated percentage of conditionally folded IDRs varies with (i) the choice of disorder predictor, (ii) the pLDDT threshold, and (iii) the minimum length of predicted IDRs. They should also provide confidence intervals for their estimates and discuss how the use of different disorder predictors affects the cross-organism comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of disease variant analysis
- **Claim pointer** The manuscript claims that "we leverage AlphaFold2's predictions of conditionally folded IDRs to rationalize disease-causing mutations in IDRs" and reports that disease-associated mutations are enriched in IDRs with high pLDDT scores
- **Evidence pointer** Figure 6, Section "Leveraging AlphaFold2 to Understand Disease-Causing Mutations in Conditionally Folding IDRs"
- **Concern** The disease variant analysis shows a statistical enrichment of OMIM mutations in high-pLDDT IDRs, but the mechanistic interpretation is limited. The single example (AL3X L168V) is used to illustrate how AF2 structures can provide mechanistic insight, but this is a single case and the predicted destabilization (ΔΔG = 7.3 kcal/mol) is not experimentally validated. The comparison between disease and non-disease mutations relies on the assumption that 1000 Genomes variants are predominantly non-pathogenic, which is reasonable but not without caveats. The analysis does not account for potential confounding factors such as mutation rate variation across genomic regions, selection effects, or the possibility that some 1000 Genomes variants are pathogenic at low penetrance.
- **Why it matters** The disease variant analysis is presented as a practical application of the manuscript's findings. If the statistical enrichment is confounded or the mechanistic interpretation is not validated, the practical utility of the approach for variant interpretation is not established.
- **Resolution test** The authors should provide additional validation of the mechanistic interpretation, either through experimental studies of the AL3X L168V variant or through additional examples where AF2 structures of conditionally folded IDRs provide mechanistic insight into disease mutations. They should also address potential confounding factors in the statistical analysis, such as controlling for local sequence context, mutation rate variation, and gene expression levels.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The manuscript claims that "AlphaFold2 has likely identified conditionally folded IDRs through the co-evolution of specific residues" and that the approach can be generalized to identify conditionally folded IDRs across proteomes
- **Evidence pointer** Section "Predicted IDRs with High pLDDT Scores Are Enriched in Charged and Hydrophobic Residues", Section "AlphaFold2 Confidently Assigns Structures for the Majority of IDRs Known to Conditionally Fold"
- **Concern** The manuscript does not fully explore the mechanisms by which AF2 assigns high pLDDT scores to conditionally folded IDRs. The authors suggest that co-evolution and sequence composition play a role, but they do not systematically test these hypotheses. For example, they do not compare the performance of AF2 with and without MSA information, nor do they test whether the observed enrichment of charged and hydrophobic residues in high-pLDDT IDRs is sufficient to explain the predictions. The generalizability of the findings to IDRs that fold upon post-translational modification (as opposed to binding) is not established, as the examples focus primarily on binding-induced folding.
- **Why it matters** Understanding the mechanism by which AF2 identifies conditionally folded IDRs is important for assessing the reliability of the approach and for improving future predictions. If the mechanism is not understood, it is difficult to know when the approach will fail.
- **Resolution test** The authors should perform additional analyses to test the mechanisms underlying AF2's predictions, such as (i) comparing AF2 predictions with and without MSA input, (ii) testing whether sequence composition alone can predict high pLDDT scores in IDRs, and (iii) examining whether the approach works for IDRs that fold upon post-translational modification.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of definitions
- **Affected element** Definition of "conditionally folded"
- **Evidence pointer** Section "Results", first paragraph
- **Issue** The definition of "conditionally folded" is provided but could be more precise. The authors state that a conditionally folded protein is "disordered in the absence of 1) a binding partner or ligand or 2) PTM, which then can acquire a stable fold in their presence." However, it is unclear whether this definition includes IDRs that fold upon changes in environmental conditions (e.g., pH, temperature, or concentration) or only upon binding or modification. Additionally, the relationship between "conditionally folded" and "conditionally disordered" (as used in the literature) is not clarified.
- **Required correction** The authors should clarify the scope of the definition and explicitly state what is excluded. They should also discuss how their definition relates to existing terminology in the field.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Statistical tests in Figures 4–6
- **Evidence pointer** Figures 4–6, Section "Predicted IDRs with High pLDDT Scores Are Enriched in Charged and Hydrophobic Residues"
- **Issue** The manuscript reports p-values for several comparisons (e.g., Fisher Exact Tests in Fig 6A, Mann-Whitney tests in Fig 4E–F) but does not consistently report effect sizes or confidence intervals. The number of independent tests performed and whether multiple testing corrections were applied is not stated.
- **Required correction** The authors should report effect sizes and confidence intervals for all key comparisons, state the total number of tests performed, and indicate whether multiple testing corrections were applied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods for AFDB parsing and filtering
- **Evidence pointer** Section "Methods", Section "Sequence-Based Prediction of IDRs in the Human Proteome"
- **Issue** The methods describe the use of SPOT-Disorder for predicting IDRs and mention that "the remaining methods are described online in SI Appendix." However, the main text does not provide sufficient detail on how AFDB files were parsed, how pLDDT scores were extracted, how IDRs were mapped to AFDB structures, or what filtering criteria were applied (e.g., minimum length, overlap thresholds). The GitHub repository is mentioned but not described in detail.
- **Required correction** The authors should provide a more complete description of the computational pipeline in the main text or ensure that the SI Appendix and GitHub repository contain all necessary details for reproduction.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of results
- **Affected element** Figure 5D–E
- **Evidence pointer** Figure 5D–E, Section "AlphaFold2-Enabled Identification of Conditionally Folding IDRs in Other Organisms"
- **Issue** The cross-organism comparison in Figure 5D–E is presented as a bar chart or similar, but the manuscript does not clearly state the number of organisms in each category (archaea, bacteria, eukaryotes) or the statistical significance of the differences between groups. The relationship between overall disorder content and the fraction of conditionally folded IDRs is described qualitatively but not quantified.
- **Required correction** The authors should provide the number of organisms in each group, statistical tests for group differences, and a quantitative description of the relationship between disorder content and conditional folding.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of prior work
- **Evidence pointer** Section "Discussion"
- **Issue** The discussion mentions that "AlphaFold2 has learned interesting properties about certain IDRs" but does not fully contextualize this finding with respect to prior work on AF2 and IDRs. Several studies have examined AF2 predictions for IDRs, and the manuscript would benefit from a more explicit comparison with these prior findings.
- **Required correction** The authors should cite and discuss prior work on AF2 predictions for IDRs more explicitly, highlighting what is new in their analysis and what confirms previous observations.

## Risk / unsupported claims
- The claim that "AlphaFold2 has likely identified conditionally folded IDRs through the co-evolution of specific residues" is presented as a likely mechanism but is not directly tested; the manuscript does not provide evidence that co-evolution, rather than sequence composition or other factors, is the primary driver of high pLDDT scores in conditionally folded IDRs.
- The estimate that 15–25% of human IDRs are conditionally folded is presented as an "upper bound" but relies on assumptions about the false positive rate of the approach that are not rigorously validated; the uncertainty in this estimate is not quantified.
- The claim that "the majority of IDRs in eukaryotic organisms likely function in the absence of conditional folding" is an extrapolation from the analysis that depends on the accuracy of the disorder predictions and the pLDDT-based classification, both of which have acknowledged limitations.
- The mechanistic interpretation of the AL3X L168V mutation (predicted ΔΔG of 7.3 kcal/mol) is based on a single computational prediction and is not experimentally validated; the claim that this provides "a mechanistic hypothesis" is appropriately cautious but the significance of this example is overstated given the lack of experimental confirmation.
- The statement that "AlphaFold2 was not trained on NMR structures" is used to argue that the agreement between AF2 predictions and NMR-derived structures is remarkable; however, AF2 was trained on the PDB, which contains many NMR-derived structures, so this claim requires qualification.