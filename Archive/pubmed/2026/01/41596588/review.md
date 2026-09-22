## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and internal consistency of the reported findings
- **Shared manuscript claim summary** The authors propose that intrinsically disordered inter-domain and inter-subdomain linkers in bacterial GntR-family transcription factors can function as sensors for carbohydrate metabolites. Using molecular dynamics simulations and sequential flexible docking, they report that these linkers bind carbohydrates with affinities comparable to nonspecific interactions, form multimolecular clusters in the UxuR monomer, and exhibit distinct binding modes across six studied transcription factors.
- **Visible evidence base** Figures 1–11 (described in text), Supplementary Figure S1 (referenced), statistical analyses described in Section 4.5
- **Missing materials affecting confidence** Figure files not provided; Supplementary Figure S1 not provided; PDB validation metrics not reported; docking pose coordinates not provided; MD simulation parameters incompletely specified; no RMSD plots visible for assessment

## Reviewer
- **Overall assessment** The manuscript addresses an interesting and timely question regarding the potential role of intrinsically disordered regions in bacterial transcription factors as metabolite sensors. The methodological approach combining MD simulations with sequential docking is reasonable for generating hypotheses. However, the evidence presented does not fully establish the central claim that these linkers function as specific metabolic sensors. Key limitations include the absence of quantitative validation against experimental data, unclear statistical treatment of docking results, and insufficient discussion of alternative interpretations. The manuscript would benefit from more rigorous analysis and clearer presentation of the evidence linking computational predictions to biological function.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, bacterial transcriptional regulation, and metabolite sensing would find this work relevant. The study contributes to the growing recognition that disordered regions in prokaryotic regulatory proteins may have functional roles beyond simple connectivity. The methodological approach of combining MD with sequential docking to probe weak interactions in disordered regions could be of interest to computational biologists working on protein-ligand interactions.

- **Major strengths** The study addresses a novel and biologically relevant question about the potential sensory role of disordered linkers in bacterial transcription factors. The use of multiple transcription factors from two bacterial species provides some comparative perspective. The sequential docking protocol is an interesting methodological choice for probing weak, multivalent interactions. The authors acknowledge limitations of their approach and discuss alternative interpretations in the Discussion section.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that the inter-domain linker of the UxuR monomer binds D-fructuronate, D-galacturonate, D-glucose, and D-glucuronate with affinities comparable to nonspecific interactions, yet these ligands formed multimolecular clusters.
- **Evidence pointer** Section 2.1.1, Figure 1c, Figure 2
- **Concern** The central observation of multimolecular clustering is based on sequential docking where previously docked ligands remain fixed in the protein structure. This protocol inherently biases subsequent ligands to bind near already-bound molecules, potentially creating artificial clusters. The authors address this concern in the Discussion (Section 3) with a control experiment, but the control is described only qualitatively. The number of ligands in clusters (7–9 molecules) seems surprisingly high for a linker region of approximately 20 residues, and no structural rationale is provided for how such dense packing could occur without steric clashes.
- **Why it matters** The clustering phenomenon is central to the authors' hypothesis that linkers can function as metabolite sensors. If clustering is an artifact of the sequential docking protocol, the primary conclusion is undermined.
- **Resolution test** Provide quantitative comparison of cluster formation between the sequential protocol and independent docking of individual ligands. Show that clusters do not form when ligands are docked independently to the same protein conformations. Provide structural validation that the proposed clusters are sterically feasible and energetically favorable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that binding affinities for linker regions were statistically significant against background when exceeding the mean nonspecific binding by more than three standard deviations.
- **Evidence pointer** Section 2.1.1, Section 4.5
- **Concern** The statistical threshold of three standard deviations is applied inconsistently. In Section 2.1.1, the authors state that most linker interactions "did not exceed the average level of random surface binding by more than three standard deviations," yet later claim "statistically significant" binding for certain complexes. The relationship between the 3-StD threshold and the reported p-value of 0.05 is not explained. Furthermore, the nonspecific binding baseline is calculated from pooled data across different protein conformations and ligands, which may not represent an appropriate null distribution for individual binding events.
- **Why it matters** The statistical framework determines which interactions are considered significant. Inconsistent application of thresholds undermines confidence in the reported findings.
- **Resolution test** Clearly define the null distribution for nonspecific binding. Report effect sizes and confidence intervals for all claimed significant interactions. Justify the 3-StD threshold with reference to the distribution of background binding affinities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** External validity
- **Claim pointer** The authors claim that their results "establish flexible linkers as pivotal metabolic sensors that directly integrate nutritional cues to alter gene expression in bacteria."
- **Evidence pointer** Abstract, Section 3
- **Concern** The study is entirely computational. No experimental validation is provided to support the claim that carbohydrate binding to linkers occurs in vivo or that such binding affects transcription factor function. The authors do not demonstrate that the proposed linker-carbohydrate interactions are biologically relevant, nor do they compare their predictions with any experimental data on these transcription factors. The leap from computational predictions to biological function is not justified by the evidence presented.
- **Why it matters** The central claim of the manuscript extends beyond what the computational evidence can support. Without experimental validation, the conclusion remains speculative.
- **Resolution test** Provide experimental evidence (e.g., mutagenesis, binding assays, reporter gene studies) demonstrating that linker-carbohydrate interactions affect transcription factor function. Alternatively, substantially temper the conclusions to reflect the hypothesis-generating nature of the study.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency
- **Claim pointer** The authors claim to have used molecular dynamics simulations and flexible docking to analyze six transcription factors.
- **Evidence pointer** Section 4.3, Section 4.4
- **Concern** The MD simulation parameters are incompletely described. The Open MMZephyr software package is not widely recognized in the literature, and no validation or benchmarking of this software is provided. The force field (Amber96) is outdated compared to current standards. The simulation length (up to 150 ns) may be insufficient for sampling the conformational space of disordered regions. Docking parameters, including grid box dimensions and exhaustiveness settings, are not reported.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Incomplete methodological details prevent other researchers from replicating or building upon this work.
- **Resolution test** Provide complete simulation parameters, software validation information, and docking settings. Justify the choice of force field and simulation length. Consider whether longer simulations or enhanced sampling methods would be more appropriate for disordered regions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparative analysis
- **Claim pointer** The authors claim that D-glucose interacted with linkers in NagR, FarR, and YydK, bridging inter-domain linkers and β-sheets within HutC-type E-domains.
- **Evidence pointer** Section 2.2.3, Figures 8–10
- **Concern** The comparative analysis across the five additional transcription factors is presented descriptively without quantitative comparison. The authors report differences in binding patterns but do not provide statistical analysis of whether these differences are significant. The selection criteria for the five additional transcription factors are described, but the rationale for choosing these specific proteins over other GntR-family members is not fully justified.
- **Why it matters** The comparative analysis is intended to demonstrate the generality of the proposed mechanism. Without quantitative comparison, the reader cannot assess whether the observed differences are meaningful or within the range of expected variation.
- **Resolution test** Provide quantitative comparison of binding affinities, occupancies, and interaction patterns across all six transcription factors. Include statistical tests for differences between proteins.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1.1, Figure 1c
- **Evidence pointer** Figure 1c
- **Issue** The description of Figure 1c is unclear regarding what exactly is plotted. The text mentions "average occupancy" and "binding affinity" but does not specify how these are represented in the figure.
- **Required correction** Clarify the figure axes and what each data point represents. Consider adding a legend or explanatory text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 2.1.1
- **Evidence pointer** Section 2.1.1
- **Issue** The term "nonspecific interactions" is used to describe baseline binding, but the definition of "nonspecific" is not provided. It is unclear whether this refers to interactions with any protein surface or specifically to interactions outside defined binding sites.
- **Required correction** Define "nonspecific" in the context of this study and explain how nonspecific binding sites were distinguished from specific ones.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Section 2.2.3
- **Evidence pointer** Section 2.2.3
- **Issue** The text refers to "YadK" in the abstract and introduction but uses "YydK" in the results section. This inconsistency could confuse readers.
- **Required correction** Use the correct protein name consistently throughout the manuscript.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.2
- **Evidence pointer** Section 4.2
- **Issue** The description of the template selection for homology modeling is incomplete. The authors state that the UxuR structure was modeled using the crystal structure of GntR from Streptococcus agalactiae (PDB: 6AZ6), but do not provide sequence identity or similarity values between the template and target.
- **Required correction** Report sequence identity and coverage between templates and targets. Justify template selection based on these metrics.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Section 2.2.1
- **Evidence pointer** Section 2.2.1
- **Issue** The statement that "the E. coli GntR itself represents another example of a rare modular structure" is presented as a conclusion but is based on limited comparative analysis. The evolutionary implications are not fully developed.
- **Required correction** Either expand the evolutionary analysis or temper the claim to reflect the preliminary nature of the observation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 4.5
- **Evidence pointer** Section 4.5
- **Issue** The Shapiro-Wilk test is mentioned, but the results of these tests are not reported. The authors state that "in almost all cases" the data violated normality assumptions, but do not specify which cases were exceptions.
- **Required correction** Report the test statistics and p-values for all normality tests. Specify which datasets were normally distributed and how this affected subsequent analysis.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Section 4.4
- **Evidence pointer** Section 4.4
- **Issue** The LigPlot+ software is cited as reference [77], but the text also mentions the Protein-Ligand Interaction Profiler (PLIP) in the Results section. It is unclear whether these are the same tool or different tools used for different purposes.
- **Required correction** Clarify which software was used for which analysis. Ensure citations are consistent with the tools described.

## Risk / unsupported claims
- The claim that flexible linkers are "pivotal metabolic sensors that directly integrate nutritional cues to alter gene expression" (Abstract) is not supported by the computational evidence presented. No experimental validation is provided.
- The claim that multimolecular clustering of carbohydrates on the UxuR linker has functional significance is speculative. The authors acknowledge this in the Discussion but do not provide sufficient evidence to distinguish between artifact and biological function.
- The assertion that D-glucose binding to the FarR linker indicates specific sensitivity to glucose is not supported by comparative analysis with other sugars or by experimental evidence.
- The evolutionary claim regarding the "mosaic structure" of E. coli GntR is based on limited sequence analysis and would require more comprehensive phylogenetic analysis to be substantiated.
- The statistical significance of linker binding events is not consistently established. The relationship between the 3-StD threshold and the reported p-value is unclear.
- The biological relevance of the proposed linker-carbohydrate interactions is not demonstrated. The authors do not show that these interactions occur at physiologically relevant concentrations or that they affect transcription factor function in vivo.

## Assessment against Nature-style criteria
- **Originality** The concept of disordered linkers in bacterial transcription factors serving as metabolite sensors is relatively novel and extends current understanding of IDR function in prokaryotes. However, the idea that disordered regions can bind small molecules is not entirely new, and the study does not provide a fundamentally new conceptual framework.
- **Scientific importance** If validated experimentally, the proposed mechanism could have implications for understanding metabolic regulation in bacteria. However, the current evidence is insufficient to establish the biological importance of the proposed interactions. The study is hypothesis-generating rather than hypothesis-testing.
- **Interdisciplinary readership** The topic bridges structural biology, computational chemistry, and microbiology, which could appeal to a broad audience. However, the technical nature of the methods and the lack of experimental validation may limit accessibility to non-specialists.
- **Technical soundness** The methodological approach is reasonable but has limitations. The sequential docking protocol may introduce artifacts, the statistical framework is not fully rigorous, and the MD simulation parameters are incompletely described. The lack of experimental validation is a significant weakness.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, with clear explanations of the biological context. However, some methodological details are presented without sufficient context for readers unfamiliar with computational docking approaches.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents an interesting hypothesis supported by preliminary computational evidence, but the central claims are not sufficiently validated. The authors should either provide experimental support for the proposed linker-carbohydrate interactions or substantially revise their conclusions to reflect the hypothesis-generating nature of the study. The methodological concerns regarding the sequential docking protocol and statistical analysis must be addressed before the case is established.