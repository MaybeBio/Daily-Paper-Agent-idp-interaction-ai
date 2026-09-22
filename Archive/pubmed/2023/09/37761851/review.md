## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, data interpretation, and conclusions as presented in the manuscript
- **Shared manuscript claim summary** The authors analyze AlphaFold-predicted structures of human proteins to investigate whether low complexity regions (LCRs), specifically homorepeats (polyX) and two-residue repeats (polyXY), within intrinsically disordered regions (IDRs) show increased propensity for secondary structure formation, particularly alpha-helices. They report that certain LCRs (polyE, polyQ, polyEK, polyER) show helical tendencies, that some LCRs accumulate at protein termini, and that proteins containing helix-prone polyXYs are enriched in RNA/DNA-related functions.
- **Visible evidence base** Full text including abstract, introduction, methods, results, discussion, and conclusions; references to supplementary tables and figures
- **Missing materials affecting confidence** Supplementary Tables S1–S6 and Figures 1–11 are referenced but not provided; no code or data availability statement; no statistical analysis details beyond p-values and odds ratios

## Reviewer

- **Overall assessment** The manuscript addresses a timely and relevant question about the structural propensities of low complexity regions within intrinsically disordered regions, leveraging AlphaFold predictions to expand on prior experimental observations. The topic is of interest to the protein science and bioinformatics communities. However, the analysis is largely descriptive and correlational, with several methodological details missing that prevent full evaluation of the robustness of the claims. The statistical approach is simplistic, and the causal or mechanistic interpretation of the observed associations is not well supported. The manuscript would benefit from clearer articulation of hypotheses, more rigorous statistical controls, and validation of key findings against independent datasets or experimental evidence.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, low complexity regions, homorepeats, and protein structure prediction. The findings on helical propensities of specific LCRs and their potential functional associations with nucleic acid binding could inform studies on protein-RNA/DNA interactions, phase separation, and disease mechanisms involving repeat expansions. The work also contributes to the ongoing evaluation of AlphaFold's utility for disordered regions.

- **Major strengths** 
  1. The study addresses an important and under-explored question about the structural behavior of LCRs within IDRs, building logically on prior work by the same group.
  2. The use of AlphaFold predictions allows a genome-wide scale of analysis that would be impractical experimentally.
  3. The authors make a reasonable effort to connect their findings to functional annotations via GO enrichment.
  4. The acknowledgment of limitations, particularly regarding AlphaFold's training bias and the need for experimental validation, is appropriate.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that polyX and polyXY regions within IDRs show increased secondary structure propensity compared to surrounding IDR residues, based on AlphaFold predictions.
- **Evidence pointer** Section 4.1, Figure 3
- **Concern** The analysis relies entirely on AlphaFold predictions without any independent validation. AlphaFold is known to have reduced accuracy for disordered regions, and the pLDDT score is not a direct measure of secondary structure propensity. The authors acknowledge this limitation but do not provide any control analyses, such as comparison with experimental structures (beyond their prior work), alternative predictors, or assessment of prediction confidence at the residue level for the specific LCRs analyzed. The claim that "AlphaFold predictions support" prior findings is therefore not strongly established.
- **Why it matters** If AlphaFold predictions are systematically biased for LCRs (e.g., due to training set composition), the core conclusion about structural propensity could be an artifact. Without validation, the central claim of the paper is not robust.
- **Resolution test** Provide validation using an independent dataset (e.g., experimentally determined structures from PDB for homologous proteins), compare AlphaFold predictions with other secondary structure prediction tools, or demonstrate that the observed effects persist when controlling for pLDDT confidence thresholds.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report statistically significant differences in structural propensity between LCRs and surrounding IDR residues (odds ratios with confidence intervals).
- **Evidence pointer** Section 4.1, Figure 3
- **Concern** The statistical analysis appears to treat residues as independent observations, which is problematic because residues within the same protein and within the same LCR are not independent. This pseudoreplication can inflate statistical significance and lead to overly narrow confidence intervals. The authors do not describe any correction for clustering or protein-level random effects. Additionally, the comparison between LCR residues and "surrounding IDR residues" is not clearly defined in terms of how surrounding regions were selected and matched.
- **Why it matters** The reported p-values and odds ratios may be artificially significant due to non-independence of data points. This undermines the statistical evidence for the central claim.
- **Resolution test** Re-analyze the data using mixed-effects models with protein as a random effect, or use a permutation-based approach that accounts for clustering. Report effect sizes with appropriate confidence intervals.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that helix-prone polyXYs in IDRs are associated with RNA/DNA binding functions, implying a functional role for LCR structural propensity.
- **Evidence pointer** Section 4.6, Figures 10–11, Supplementary Table S5
- **Concern** The GO enrichment analysis is performed on proteins containing the top 10 helix-prone polyXYs, but the selection criteria for these polyXYs are based on the same AlphaFold data used for the structural classification. This creates a circularity issue: proteins are selected for having helix-prone LCRs, and then shown to be enriched in certain functions. The enrichment is not compared against a proper background (e.g., all proteins with polyXYs, or all IDR-containing proteins). Furthermore, the authors note that some enriched terms are associated with non-helical polyXYs, which weakens the specific claim about helical propensity being functionally relevant.
- **Why it matters** The functional interpretation is a key part of the paper's significance. If the enrichment is not specific to helix-prone LCRs or is an artifact of selection bias, the biological conclusions are not supported.
- **Resolution test** Perform GO enrichment comparing proteins with helix-prone polyXYs against proteins with non-helix-prone polyXYs of the same types, and against all IDR-containing proteins. Report whether the enrichment is specific to helical LCRs.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors describe positional preferences, such as polyAG and polyAK accumulating at the N-terminus, with polyAK showing increased helical propensity at that location.
- **Evidence pointer** Section 4.2, Figure 4, Table 1, Supplementary Table S4
- **Concern** The definition of "terminal" regions (100 amino acids or 30% for shorter proteins) is arbitrary and may not be biologically meaningful. The analysis of positional effects on helical propensity does not appear to control for LCR length, protein length, or other confounding factors. The comparison between N-terminal, C-terminal, and internal positions is descriptive without statistical testing.
- **Why it matters** Positional claims could be artifacts of the arbitrary terminal definition or confounding variables. Without proper statistical comparison, these observations are not well supported.
- **Resolution test** Use a continuous measure of relative position, control for LCR and protein length, and perform statistical tests comparing positional distributions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and Discussion
- **Evidence pointer** Section 1, Section 4
- **Issue** The manuscript assumes familiarity with IDR/LCR terminology and concepts without sufficient background for a general biology audience. Some terms (e.g., "conformational selection") are introduced without explanation.
- **Required correction** Add brief explanations of key concepts and terms for nonspecialist readers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Section 2
- **Issue** The methods section lacks details on how IDRs were defined and extracted from MobiDB, how polyX/polyXY boundaries were determined, and how overlapping LCRs were handled. The version of AlphaFold is stated as "v3" but the actual release or model version is not specified.
- **Required correction** Provide complete methodological details, including software versions, parameters, and data processing steps.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Section 4.4
- **Issue** The discussion of polyX/polyXY overlap is interesting but speculative. The claim that polyX can "help in understanding" polyXY structural patterns is not clearly substantiated by the data presented.
- **Required correction** Clarify the specific insights gained from the overlap analysis and avoid over-interpretation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figures
- **Evidence pointer** Figures 5–11
- **Issue** Figure captions are not provided in the manuscript text, making it difficult to interpret the figures without supplementary materials.
- **Required correction** Include self-contained figure captions that explain the key features and take-home message of each figure.

- **Technical failings that need to be addressed before the case is established** R1-M1 (validation of AlphaFold predictions), R1-M2 (statistical non-independence), R1-M3 (circularity in GO enrichment)

- **Assessment against Nature-style criteria**
  - **Originality** The question of LCR structural propensity within IDRs is not entirely new, given the authors' prior work, but the scale of analysis using AlphaFold is a novel contribution. However, the conceptual advance is incremental.
  - **Scientific importance** The findings could be relevant to understanding IDR function and the role of LCRs in nucleic acid interactions, but the lack of experimental validation and the descriptive nature of the analysis limit the immediate impact.
  - **Interdisciplinary readership** The topic bridges structural biology, bioinformatics, and molecular biology, and could appeal to researchers in these fields. However, the presentation is somewhat specialized.
  - **Technical soundness** The technical approach has significant limitations as detailed above, particularly regarding validation and statistics. These need to be addressed for the conclusions to be reliable.
  - **Readability for nonspecialists** The manuscript is generally well-written but assumes familiarity with IDR/LCR concepts. Some sections, particularly the results, are dense and would benefit from clearer framing.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an interesting question and has potential, but the central claims are not sufficiently supported due to lack of validation, statistical issues, and potential circularity in the functional analysis. Major revisions are required to address these concerns before the case is convincing.

## Risk / unsupported claims
- The claim that AlphaFold predictions "support" prior experimental findings is not fully supported without independent validation.
- The functional association between helix-prone polyXYs and RNA/DNA binding is potentially circular and not rigorously established.
- The positional preferences (e.g., N-terminal accumulation) are descriptive and lack statistical support.
- The statement that "polyX has higher structural propensity than polyXY" is presented without a direct statistical comparison between the two categories.
- The hypothesis about charge balancing in IDRs (Section 3) is speculative and not tested.
- The claim that AlphaFold's confidence scores "confirm" structural propensity is not well justified, as pLDDT is a confidence metric, not a direct measure of structure.